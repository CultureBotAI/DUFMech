#!/usr/bin/env python3
"""Read-only Git PR preservation audit (2026-11-16).

Purpose: distinguish exact preserved PR payloads from unique branch work.
Inputs: local repository containing captured objects; exact main commit;
        REST open-PR snapshot; gh pr list JSON snapshot including changed files.
Outputs: ledger.json and REPORT.md in an explicit durable output directory.
Issue: evidence helper for the authorized fleet maintenance assignment; it does
not repair an issue or make a scientific assessment. No network or Git writes.
All paths and identities are command-line inputs, so this helper is public-safe.
"""
from __future__ import annotations

import argparse
import collections
import datetime
import hashlib
import json
import pathlib
import subprocess


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=pathlib.Path, required=True)
    ap.add_argument('--main', required=True)
    ap.add_argument('--prs', type=pathlib.Path, required=True)
    ap.add_argument('--checks', type=pathlib.Path, required=True)
    ap.add_argument('--output', type=pathlib.Path, required=True)
    args = ap.parse_args()
    def git(*argv: str) -> bytes:
        return subprocess.check_output(['git', '-C', str(args.repo), *argv])
    def txt(*argv: str) -> str:
        return git(*argv).decode().strip()
    def sha256(path: pathlib.Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    prs = json.loads(args.prs.read_text())
    checks = {p['number']: p for p in json.loads(args.checks.read_text())}
    assert len({p['number'] for p in prs}) == len(prs)
    assert set(checks) == {p['number'] for p in prs}
    main_sha = txt('rev-parse', args.main + '^{commit}')
    source_heads = {str(p['number']): p['head']['sha'] for p in prs}
    targets = {'main': main_sha, **source_heads}
    graph = {}
    for line in git('rev-list', '--parents', *targets.values()).decode().splitlines():
        commit, *parents = line.split()
        graph[commit] = parents
    def ancestors(head: str) -> set[str]:
        seen: set[str] = set()
        todo = [head]
        while todo:
            item = todo.pop()
            if item not in seen:
                seen.add(item)
                todo.extend(graph.get(item, []))
        return seen
    ancestry = {target: ancestors(head) for target, head in targets.items()}
    changed_by_pr = {}
    merge_bases = {}
    all_paths = set()
    for p in prs:
        number = p['number']; head = p['head']['sha']
        assert checks[number]['headRefOid'] == head
        merge_base = txt('merge-base', main_sha, head)
        assert '\n' not in merge_base, 'multiple merge bases require manual assessment'
        merge_bases[number] = merge_base
        # No rename detection: each removed/added path is independently assessed.
        raw = git('diff', '--name-status', '--no-renames', '-z', merge_base, head)
        fields = raw.decode().split('\0')[:-1]
        assert len(fields) % 2 == 0
        changes = list(zip(fields[::2], fields[1::2]))
        assert all(s in {'A', 'M', 'D', 'T'} for s, _ in changes)
        changed_by_pr[number] = changes
        all_paths.update(path for _, path in changes)
    trees = {}
    tree_ids = {}
    for target, head in targets.items():
        tree_ids[target] = txt('rev-parse', head + '^{tree}')
        tree = {}
        for item in git('ls-tree', '-r', '-z', head).split(b'\0'):
            if not item:
                continue
            meta, raw_path = item.split(b'\t', 1)
            path = raw_path.decode()
            if path in all_paths:
                mode, kind, oid = meta.decode().split()
                tree[path] = {'mode': mode, 'type': kind, 'oid': oid}
        trees[target] = tree
    rows = []
    for p in sorted(prs, key=lambda p: p['number']):
        number = p['number']; key = str(number); head = p['head']['sha']
        changes = changed_by_pr[number]
        peers = [target for target in targets if target != key]
        match_counts = collections.Counter()
        path_proofs = []
        for status, path in changes:
            source = trees[key].get(path)
            equal = [target for target in peers if trees[target].get(path) == source]
            match_counts.update(equal)
            path_proofs.append({'path': path, 'change': status, 'source_entry': source,
                                'exact_matching_targets': equal})
        full = [target for target in peers if match_counts[target] == len(changes)]
        peer_ancestors = [target for target in peers if head in ancestry[target]]
        api_paths = {f['path'] for f in checks[number]['files']}
        git_paths = {path for _, path in changes}
        missing_from_api = sorted(git_paths - api_paths)
        extra_api = sorted(api_paths - git_paths)
        assert not extra_api, f'API/Git unexpected paths on {number}: {extra_api}'
        review_only = all(path.startswith('reviews/structured/') for _, path in changes)
        if full:
            disposition = 'exact_payload_preserved_review_closure_candidate'
        elif review_only:
            disposition = 'retain_unique_immutable_review_payload'
        else:
            disposition = 'retain_unique_nonbatch_payload_manual_review_required'
        rows.append({'number': number, 'title': p['title'], 'url': p['html_url'],
            'source_snapshot_updated_at': p['updated_at'], 'draft': p['draft'],
            'head': head, 'head_ref': p['head']['ref'], 'head_tree': tree_ids[key],
            'api_base': p['base']['sha'], 'api_base_ref': p['base']['ref'],
            'published_main': main_sha, 'merge_base_with_published_main': merge_bases[number],
            'head_ancestor_of': peer_ancestors,
            'three_dot_path_count': len(changes), 'api_changed_path_count': len(api_paths),
            'api_path_comparison': 'complete_match' if not missing_from_api else 'api_snapshot_partial_git_complete',
            'api_omitted_path_count': len(missing_from_api),
            'api_extra_paths': extra_api,
            'exact_containment_targets': full,
            'partial_preservation_targets': [
                {'target': t, 'matched_paths': match_counts[t], 'total_paths': len(changes)}
                for t in peers if 0 < match_counts[t] < len(changes)],
            'zero_match_targets': [t for t in peers if match_counts[t] == 0],
            'disposition': disposition, 'review_only': review_only,
            'changed_paths': path_proofs})
    report = {
        'schema_version': 1, 'generated_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'repository_origin': txt('remote', 'get-url', 'origin'),
        'published_main': main_sha, 'published_main_tree': tree_ids['main'],
        'read_only': True, 'target_commits': targets, 'target_trees': tree_ids,
        'inputs': {'prs_sha256': sha256(args.prs), 'checks_sha256': sha256(args.checks),
                   'helper_sha256': sha256(pathlib.Path(__file__))},
        'method': ['Actual git merge-base(main, head) and three-dot changed paths, with rename detection disabled.',
                   'Exact Git object id, type and mode for every changed path compared to main and every other captured PR head.',
                   'Deleted files require verified absence in the comparison tree.',
                   'Ancestry calculated from full reachable Git parent graph; ancestry alone never proves preservation.',
                   'GitHub path snapshot compared separately; its 100-file truncation is recorded explicitly.',
                   'Git tree enumeration includes all tracked files regardless of gitignore. Untracked local work cannot establish published containment.',
                   'No scientific claims, review judgements, human approvals or merge readiness inferred.'],
        'coverage': {'snapshot_prs': len(prs), 'audited_prs': len(rows), 'comparison_targets_per_pr': len(peers),
                     'unique_changed_paths': len(all_paths),
                     'review_only_prs': sum(r['review_only'] for r in rows),
                     'closure_candidates': [r['number'] for r in rows if r['exact_containment_targets']],
                     'api_partial_path_prs': [r['number'] for r in rows if r['api_omitted_path_count']]},
        'prs': rows}
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output/'ledger.json').write_text(json.dumps(report, indent=2) + '\n')
    lines = ['# DUFMech PR payload preservation audit', '',
             f"Captured main: `{main_sha}`. Audited {len(rows)}/{len(prs)} captured open PR heads.", '',
             ('Every changed path was compared against current published main and all other captured open PR heads. '
             'Exact containment requires the same Git object, mode and type (or proven absence for deletions). '
             'The comparison is based on the merge-base three-dot delta; branch age and titles are not evidence of supersession.'), '',
             f"Closure candidates: {report['coverage']['closure_candidates'] or 'none'}. No branch or review payload may be discarded on the basis of this audit.", '',
             '| PR | Exact head | Three-dot paths | Head ancestors among other targets | Complete payload in | Disposition |',
             '|---|---|---:|---|---|---|']
    for row in rows:
        lines.append(f"| #{row['number']} | `{row['head']}` | {row['three_dot_path_count']} | "
                     f"{', '.join(row['head_ancestor_of']) or 'none'} | {', '.join(row['exact_containment_targets']) or 'none'} | {row['disposition']} |")
    lines.extend(['', ('The complete JSON ledger records every path and its blob/mode/type, all compared commit/tree identities, '
                  'ancestry, exact matches, and API/Git path coverage. This is a structural preservation audit, not an assessment '
                  'of scientific validity or review quality. Live heads must be rechecked before acting.'), '',
                  'Issue: not applicable to this read-only evidence helper. No source or Git/GitHub state was changed.', ''])
    (args.output/'REPORT.md').write_text('\n'.join(lines))
    print(json.dumps(report['coverage'], indent=2))

if __name__ == '__main__':
    main()
