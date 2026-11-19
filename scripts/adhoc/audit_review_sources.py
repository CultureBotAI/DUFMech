#!/usr/bin/env python3
"""Read-only consolidation safety inventory, dated 2026-11-16.

Purpose: inspect immutable review identity, verdict, and pinned input hashes.
Inputs: repository Git objects and audit_pr_preservation.py JSON ledger.
Output: review-sources.json in the explicit output directory.
Issue: evidence-only fleet maintenance inventory; no repairs or scientific claims.
Requires PyYAML from the existing repository environment; does not install it.
"""
from __future__ import annotations

import argparse
import collections
import datetime
import hashlib
import json
import pathlib
import subprocess

import yaml


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=pathlib.Path, required=True)
    ap.add_argument('--ledger', type=pathlib.Path, required=True)
    ap.add_argument('--output', type=pathlib.Path, required=True)
    a=ap.parse_args()
    def git(*args): return subprocess.check_output(['git','-C',str(a.repo),*args])
    d=json.loads(a.ledger.read_text())
    cache={}; tree_cache={}; rows=[]; ids=collections.defaultdict(list)
    def tree(revision):
        if revision not in tree_cache:
            entries={}
            for item in git('ls-tree','-r','-z',revision).split(b'\0'):
                if item:
                    meta,path=item.split(b'\t',1)
                    mode,kind,oid=meta.decode().split()
                    entries[path.decode()]={'mode':mode,'type':kind,'oid':oid}
            tree_cache[revision]=entries
        return tree_cache[revision]
    def digest(oid):
        if oid not in cache: cache[oid]=hashlib.sha256(git('cat-file','blob',oid)).hexdigest()
        return cache[oid]
    for pr in d['prs']:
        if not pr['review_only']: continue
        for change in pr['changed_paths']:
            if not change['path'].endswith('/review.yaml'): continue
            raw=git('cat-file','blob',change['source_entry']['oid'])
            doc=yaml.safe_load(raw)
            rid=doc.get('review_id'); ids[rid].append(change['path'])
            source=doc['source']; rev=source['git_revision']; st=tree(rev)
            inputs=[]
            for inp in source['inputs']:
                entry=st.get(inp['path']); actual=digest(entry['oid']) if entry and entry['type']=='blob' else None
                current=tree(d['published_main']).get(inp['path'])
                main_actual=digest(current['oid']) if current and current['type']=='blob' else None
                inputs.append({'path':inp['path'],'role':inp.get('role'),
                               'declared_sha256':inp['sha256'],'source_git_entry':entry,
                               'source_git_sha256':actual,'matches_source_git':actual==inp['sha256'],
                               'main_sha256':main_actual,'matches_current_main':main_actual==inp['sha256']})
            rows.append({'pr':pr['number'],'path':change['path'],'sha256':hashlib.sha256(raw).hexdigest(),
                         'review_id':rid,'id_matches_directory':rid==pathlib.PurePosixPath(change['path']).parent.name,
                         'source_revision':rev,'source_state':source.get('state'),
                         'snapshot_id':source.get('snapshot_id'),'completion':doc.get('completion'),
                         'verdict':doc.get('verdict'),'native_verdict':doc.get('native_verdict'),
                         'scientific_review':doc.get('scientific_review'),
                         'targets':[{'id':t.get('target_id'),'path':t.get('path'),'digest':t.get('semantic_digest')} for t in doc.get('targets',[])],
                         'inputs':inputs})
    summary={'review_bundles':len(rows),'review_ids':len(ids),
             'duplicate_review_ids':{k:v for k,v in ids.items() if len(v)>1},
             'id_directory_mismatches':[r['path'] for r in rows if not r['id_matches_directory']],
             'source_revisions':dict(collections.Counter(r['source_revision'] for r in rows)),
             'source_states':dict(collections.Counter(r['source_state'] for r in rows)),
             'verdicts':dict(collections.Counter(r['verdict'] for r in rows)),
             'native_verdicts':dict(collections.Counter(r['native_verdict'] for r in rows)),
             'scientific_review_flags':dict(collections.Counter(str(r['scientific_review']) for r in rows)),
             'snapshot_ids':dict(collections.Counter(r['snapshot_id'] for r in rows)),
             'source_git_mismatches':[{'pr':r['pr'],'review':r['path'],'input':i} for r in rows for i in r['inputs'] if not i['matches_source_git']],
             'input_count':sum(len(r['inputs']) for r in rows),
             'current_main_input_mismatch_count':sum(not i['matches_current_main'] for r in rows for i in r['inputs'])}
    out={'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'main':d['published_main'],'ledger_sha256':hashlib.sha256(a.ledger.read_bytes()).hexdigest(),
         'helper_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'scope':'structural inventory only; no scientific or schema-validity judgement',
         'summary':summary,'reviews':rows}
    a.output.mkdir(parents=True,exist_ok=True)
    (a.output/'review-sources.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
