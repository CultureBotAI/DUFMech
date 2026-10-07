"""Guarded ownership tracking for a changing set of generated static pages."""

from __future__ import annotations

import fcntl
import hashlib
import json
import os
import re
import secrets
import stat
from contextlib import contextmanager
from pathlib import Path

from dufmech.report import ReportError

MANIFEST = "site-files.json"
PENDING = "site-files.pending.json"
GENERATED = re.compile(
    r"(?:\.nojekyll|(?:index|categories|sources|cross-mech|schema)\.html|"
    r"(?:index|catalogue)\.json|style\.css|(?:dashboard|theme)\.js|"
    r"families/PF[0-9]{5}\.(?:html|json)|browse/[0-9]+\.html|"
    r"category/[a-z_]+(?:-[0-9]+)?\.html|schema/[a-z_]+\.yaml|"
    r"datasets/[A-Za-z0-9_-]+(?:\.manifest)?\.(?:json|tsv)|"
    r"source/(?:data/families|history|reports)/[A-Za-z0-9_./-]+\.(?:yaml|yml|md))"
)


@contextmanager
def output_lock(out: Path):
    """Use one destination-adjacent lock, independent of each process's TMPDIR."""
    out = out.absolute()
    with output_tree(out.parent) as parent:
        descriptor = os.open(f".{out.name}.dufmech-render.lock",
                             os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW | os.O_NONBLOCK,
                             0o600, dir_fd=parent.descriptor)
        try:
            if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                raise ReportError("site render lock must be a regular file")
            fcntl.flock(descriptor, fcntl.LOCK_EX)
            yield
        finally:
            fcntl.flock(descriptor, fcntl.LOCK_UN)
            os.close(descriptor)


class SiteTree:
    """Operate relative to an opened site directory, never following output symlinks."""

    def __init__(self, root: Path, descriptor: int, parent_descriptor: int):
        self.root = root
        self.descriptor = descriptor
        self.parent_descriptor = parent_descriptor

    @contextmanager
    def parent(self, relative: str, *, create: bool = False):
        parts = Path(relative).parts
        if not parts or Path(relative).is_absolute() or ".." in parts:
            raise ReportError(f"unsafe output path: {relative}")
        descriptor = os.dup(self.descriptor)
        try:
            for part in parts[:-1]:
                if create:
                    try:
                        os.mkdir(part, dir_fd=descriptor)
                    except FileExistsError:
                        pass
                try:
                    child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=descriptor)
                except OSError as exc:
                    if isinstance(exc, FileNotFoundError):
                        raise
                    raise ReportError(f"output is not a regular directory (or uses a symlink): {relative}") from exc
                os.close(descriptor)
                descriptor = child
            yield descriptor, parts[-1]
        finally:
            os.close(descriptor)

    def read(self, relative: str) -> bytes | None:
        try:
            with self.parent(relative) as (parent, name):
                descriptor = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
                with os.fdopen(descriptor, "rb") as handle:
                    if not stat.S_ISREG(os.fstat(handle.fileno()).st_mode):
                        raise ReportError(f"output is not a regular file: {relative}")
                    return handle.read()
        except FileNotFoundError:
            return None
        except OSError as exc:
            raise ReportError(f"output is not a regular file (or uses a symlink): {relative}") from exc

    def write_new(self, relative: str, content: bytes) -> None:
        with self.parent(relative, create=True) as (parent, name):
            descriptor = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                                 0o644, dir_fd=parent)
            with os.fdopen(descriptor, "wb") as handle:
                handle.write(content)

    def replace_from(self, staged: SiteTree, relative: str) -> None:
        with (staged.parent(relative) as (source_parent, name),
              self.parent(relative, create=True) as (target_parent, target_name)):
            try:
                info = os.stat(target_name, dir_fd=target_parent, follow_symlinks=False)
            except FileNotFoundError:
                info = None
            if info is not None and not stat.S_ISREG(info.st_mode):
                raise ReportError(f"generated output is not a regular file: {relative}")
            os.replace(name, target_name, src_dir_fd=source_parent, dst_dir_fd=target_parent)

    def check_target(self, relative: str) -> None:
        try:
            with self.parent(relative) as (parent, name):
                info = os.stat(name, dir_fd=parent, follow_symlinks=False)
                if not stat.S_ISREG(info.st_mode):
                    raise ReportError(f"generated output is not a regular file: {relative}")
        except FileNotFoundError:
            pass

    def assert_attached(self) -> None:
        actual = os.fstat(self.descriptor)
        current = self.root.stat(follow_symlinks=False)
        if (actual.st_dev, actual.st_ino) != (current.st_dev, current.st_ino):
            raise ReportError("output directory was replaced during rendering")

    def remove(self, relative: str, digest: str) -> None:
        with self.parent(relative) as (parent, name):
            descriptor = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
            with os.fdopen(descriptor, "rb") as handle:
                info = os.fstat(handle.fileno())
                if (not stat.S_ISREG(info.st_mode)
                        or hashlib.sha256(handle.read()).hexdigest() != digest):
                    raise ReportError(f"refusing to remove changed obsolete page: {relative}")
                current = os.stat(name, dir_fd=parent, follow_symlinks=False)
                if (current.st_dev, current.st_ino) != (info.st_dev, info.st_ino):
                    raise ReportError(f"obsolete page changed during cleanup: {relative}")
                os.unlink(name, dir_fd=parent)
        parts = Path(relative).parts[:-1]
        while parts:
            try:
                with self.parent("/".join(parts)) as (parent, name):
                    os.rmdir(name, dir_fd=parent)
            except (OSError, ReportError):
                break
            parts = parts[:-1]

    @contextmanager
    def stage(self):
        if os.fstat(self.parent_descriptor).st_dev != os.fstat(self.descriptor).st_dev:
            raise ReportError("site output must be a subdirectory of its filesystem, not a mount root")
        name = f".{self.root.name}.dufmech-stage-{secrets.token_hex(12)}"
        os.mkdir(name, mode=0o700, dir_fd=self.parent_descriptor)
        descriptor = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                             dir_fd=self.parent_descriptor)
        try:
            yield SiteTree(self.root.parent / name, descriptor, self.parent_descriptor)
        finally:
            try:
                _clear_directory(descriptor)
            finally:
                os.close(descriptor)
            os.rmdir(name, dir_fd=self.parent_descriptor)


def _clear_directory(descriptor: int) -> None:
    for name in os.listdir(descriptor):
        info = os.stat(name, dir_fd=descriptor, follow_symlinks=False)
        if stat.S_ISDIR(info.st_mode):
            child = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=descriptor)
            try:
                _clear_directory(child)
            finally:
                os.close(child)
            os.rmdir(name, dir_fd=descriptor)
        else:
            os.unlink(name, dir_fd=descriptor)


@contextmanager
def output_tree(out: Path):
    descriptor = os.open(out.anchor, os.O_RDONLY | os.O_DIRECTORY)
    parent_descriptor = os.dup(descriptor)
    try:
        for part in out.parts[1:]:
            try:
                os.mkdir(part, dir_fd=descriptor)
            except FileExistsError:
                pass
            try:
                child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=descriptor)
            except OSError as exc:
                raise ReportError(f"output tree is not a regular directory (or uses a symlink): {out}") from exc
            os.close(parent_descriptor)
            parent_descriptor = os.dup(descriptor)
            os.close(descriptor)
            descriptor = child
        yield SiteTree(out, descriptor, parent_descriptor)
    finally:
        os.close(descriptor)
        os.close(parent_descriptor)


def _ownership(tree: SiteTree, name: str, *, pending: bool = False) -> dict:
    raw = tree.read(name)
    if raw is None:
        return {}
    try:
        payload = json.loads(raw)
    except ValueError as exc:
        raise ReportError(f"invalid site ownership manifest: {name}") from exc
    if not isinstance(payload, dict):
        raise ReportError(f"invalid site ownership manifest: {name}")
    for path, value in payload.items():
        digests = value if pending else [value]
        if (not GENERATED.fullmatch(path) or ".." in Path(path).parts
                or not isinstance(digests, list) or not digests
                or any(not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest)
                       for digest in digests)):
            raise ReportError(f"unsafe site ownership entry: {path}")
    return payload


def prepare_files(
    artifacts: dict[str, str], out: Path, *, tree: SiteTree | None = None,
) -> list[tuple[Path, str]]:
    """Stage a manifest and return only unchanged, previously owned obsolete files."""
    if tree is None:
        with output_tree(out.absolute()) as opened:
            return prepare_files(artifacts, out, tree=opened)
    for name in artifacts:
        if not GENERATED.fullmatch(name) or ".." in Path(name).parts:
            raise ReportError(f"unsafe generated site artifact: {name}")
        tree.check_target(name)
    previous = _ownership(tree, MANIFEST)
    for name, digests in _ownership(tree, PENDING, pending=True).items():
        content = tree.read(name)
        if content is None:
            continue
        digest = hashlib.sha256(content).hexdigest()
        if digest not in digests:
            raise ReportError(f"refusing to recover modified pending page: {name}")
        previous[name] = digest
    stale = []
    for name, digest in previous.items():
        if name in artifacts:
            continue
        content = tree.read(name)
        if content is not None:
            if hashlib.sha256(content).hexdigest() != digest:
                raise ReportError(f"refusing to remove modified obsolete page: {name}")
            stale.append((out / name, digest))
    artifacts[MANIFEST] = json.dumps({
        name: hashlib.sha256(content.encode()).hexdigest()
        for name, content in sorted(artifacts.items())
    }, indent=2, sort_keys=True) + "\n"
    return stale


def pending_ownership(artifacts: dict[str, str], tree: SiteTree) -> str:
    pending = _ownership(tree, PENDING, pending=True)
    for name, digest in _ownership(tree, MANIFEST).items():
        pending.setdefault(name, []).append(digest)
    for name, digest in json.loads(artifacts[MANIFEST]).items():
        pending.setdefault(name, []).append(digest)
    return json.dumps({name: sorted(set(digests)) for name, digests in sorted(pending.items())},
                      indent=2, sort_keys=True) + "\n"


def remove_obsolete(
    paths: list[tuple[Path, str]], out: Path, *, tree: SiteTree | None = None,
) -> None:
    """Remove verified stale artifacts after all replacements have succeeded."""
    if tree is None:
        with output_tree(out.absolute()) as opened:
            return remove_obsolete(paths, out, tree=opened)
    for path, digest in paths:
        tree.remove(path.relative_to(out).as_posix(), digest)
