#!/usr/bin/env python3
"""Inventory retained review source commits without Git writes (2026-11-16).

Inputs: repository root and a saved `git ls-remote --tags origin` snapshot.
Output: source-git-inventory.json under the supplied durable output directory.
Purpose/issue: local historical-source object availability for DUFMech #459/#460.
Includes ignored/hidden review files. Does not alter reviews, tags, or branches.
"""
from __future__ import annotations

import argparse
import collections
import datetime
import hashlib
import json
import pathlib
import re
import subprocess

import yaml


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=pathlib.Path, required=True)
    parser.add_argument('--remote-tags', type=pathlib.Path, required=True)
    parser.add_argument('--output', type=pathlib.Path, required=True)
    args = parser.parse_args()
    def git(*argv: str) -> bytes:
        return subprocess.check_output(['git', '--no-replace-objects', '-C', str(args.root), *argv])
    loader = getattr(yaml, 'CSafeLoader', yaml.SafeLoader)
    reports = []
    errors = []
    candidates = sorted((args.root/'reviews/structured').rglob('review.yaml'))
    for base in ['reports/yaml_record_review', 'reports/yaml_category_review', 'reports/repo_review']:
        candidates.extend(sorted((args.root/base).rglob('*.md')))
    for path in candidates:
        relative = path.relative_to(args.root).as_posix()
        if path.is_symlink():
            errors.append({'path': relative, 'error': 'symlink refused'})
            continue
        raw = path.read_bytes()
        try:
            if path.name == 'review.yaml':
                doc = yaml.load(raw, Loader=loader)
                revision = doc['source']['git_revision']
                state = doc['source']['state']
                kind = 'structured'
            else:
                text = raw.decode()
                if not text.startswith('---\n') or '\n---\n' not in text[4:]:
                    errors.append({'path': relative, 'error': 'legacy metadata missing'})
                    continue
                front = text[4:].split('\n---\n', 1)[0]
                doc = yaml.load(front, Loader=loader)
                revision = doc['context']['source_revision']
                state = doc['context'].get('source_state')
                kind = 'legacy'
            if not isinstance(revision, str) or not re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', revision):
                raise ValueError('source revision must be a full Git object ID')
            reports.append({'path': relative, 'kind': kind, 'source_revision': revision,
                            'source_state': state, 'sha256': hashlib.sha256(raw).hexdigest()})
        except (KeyError, TypeError, ValueError, yaml.YAMLError) as exc:
            errors.append({'path': relative, 'error': str(exc)})
    sources = collections.defaultdict(list)
    for report in reports:
        sources[report['source_revision']].append(report['path'])
    remote = {}
    for line in args.remote_tags.read_text().splitlines():
        oid, ref = line.split('\t', 1)
        remote[ref] = oid
    entries = []
    for revision, paths in sorted(sources.items()):
        probe = subprocess.run(['git', '--no-replace-objects', '-C', str(args.root),
                                'rev-parse', '--verify', revision+'^{commit}'], capture_output=True, text=True, check=False)
        available = probe.returncode == 0 and probe.stdout.strip() == revision
        matches = []
        for ref, oid in remote.items():
            if oid == revision:
                tag = ref.removesuffix('^{}')
                matches.append({'ref': tag, 'peeled': ref.endswith('^{}'),
                                'tag_object': remote.get(tag), 'commit': revision})
        entries.append({'revision': revision, 'local_commit_available': available,
                        'review_count': len(paths), 'reviews': paths,
                        'matching_remote_tags': matches,
                        'probe_stderr': probe.stderr.strip() if not available else ''})
    out = {'generated_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'repository_origin': git('remote', 'get-url', 'origin').decode().strip(),
           'checkout_head': git('rev-parse', 'HEAD').decode().strip(),
           'scope': 'authoritative structured review YAML and legacy review Markdown; recursive enumeration includes hidden/ignored files',
           'remote_tags_sha256': hashlib.sha256(args.remote_tags.read_bytes()).hexdigest(),
           'helper_sha256': hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
           'counts': {'candidate_files': len(candidates), 'reviews': len(reports),
                      'unique_source_revisions': len(sources), 'missing_commits': sum(not r['local_commit_available'] for r in entries),
                      'parse_errors': len(errors)},
           'errors': errors, 'sources': entries, 'reviews': reports}
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output/'source-git-inventory.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({'counts': out['counts'], 'errors': errors,
                      'missing': [entry for entry in entries if not entry['local_commit_available']]}, indent=2))


if __name__ == '__main__':
    main()
