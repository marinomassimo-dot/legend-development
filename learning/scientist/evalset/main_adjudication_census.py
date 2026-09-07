#!/usr/bin/env python3
"""Which of the 48 cases' papers already carry an ADJUDICATING ARTIFACT on `main`?

Pattern-matching for leaked answers is a screen and it misses paraphrase. There is a
structural question underneath it that does not: **has this laboratory already read and
adjudicated this paper, in a file that sits on `main`?** If it has, then every worktree of
this repository contains that adjudication, and any case on that paper is spent for any
actor reading inside a checkout — whatever words the adjudication happens to use.

Five artifact classes, each a file whose existence means "this paper was worked":

  MANIFEST     deepdive_manifests/PMID<x>.json          verbatim locators + propositions
  DOSSIER      fulltext_dossiers/PMID<x>.md             prose reading
  RECEIPT      a row in fulltext_read_receipts.jsonl    evidence_basis carries the findings
  PAGE_ADJ     page_adjudications/PMID<x>/              adjudicated figure crops
  QUEUE_NOTE   a full_text_queue_current.md entry with adjudicative language

Run from the repository root.
"""
import json, re, subprocess, sys, os, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))


def sh(*a):
    return subprocess.run(a, capture_output=True, text=True, cwd=REPO).stdout


ADJ = re.compile(
    r'READ FROM THE IMAGE|not established|unsupported|contradict|refut|overclaim|'
    r'does not support|never (measured|tested)|not measured|no (blot|test|antibody)|'
    r'is not |cannot be|empty for both|denied by|falsif|no evidence|does not decide', re.I)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pin-main', default='main')
    ap.add_argument('--json')
    a = ap.parse_args()
    main_ref = sh('git', 'rev-parse', a.pin_main).strip()

    cp = json.load(open(os.path.join(
        REPO, 'learning/scientist/evalset/case_pmids.json'), encoding='utf-8'))
    case_pmids, all_pmids = cp['case_pmids'], cp['all_pmids']

    tree = [n for n in sh('git', 'ls-tree', '-r', '--name-only', main_ref).split('\n') if n]
    ledger = sh('git', 'show', '%s:disease-models/wwox/registries/fulltext_read_receipts.jsonl' % main_ref)
    queue = sh('git', 'show', '%s:disease-models/wwox/research/full_text_queue_current.md' % main_ref)

    print("MAIN pinned at %s" % main_ref)
    print("tracked files at main: %d" % len(tree))
    print()

    # receipts, per pmid, with whether the evidence_basis carries adjudicative language
    receipts = {}
    for ln in ledger.split('\n'):
        if not ln.strip():
            continue
        try:
            r = json.loads(ln)
        except Exception:
            continue
        pm = str((r.get('study_id') or {}).get('pmid', ''))
        if not pm:
            m = re.search(r'FTR-\d+-(\d{7,8})-', str(r.get('event_id', '')))
            pm = m.group(1) if m else ''
        if not pm:
            continue
        eb = ' '.join(r.get('evidence_basis') or [])
        d = receipts.setdefault(pm, {'n': 0, 'adjudicative': False, 'chars': 0})
        d['n'] += 1
        d['chars'] += len(eb)
        if ADJ.search(eb):
            d['adjudicative'] = True

    # queue entries, per pmid
    queue_blocks = {}
    for pm in all_pmids:
        idx = [m.start() for m in re.finditer(re.escape(pm), queue)]
        if idx:
            txt = ' '.join(queue[max(0, i - 400):i + 1600] for i in idx[:4])
            queue_blocks[pm] = ADJ.search(txt) is not None

    rows = {}
    print("%-10s %-9s %-8s %-22s %-9s %-11s %s"
          % ("PMID", "MANIFEST", "DOSSIER", "RECEIPT", "PAGE_ADJ", "QUEUE_ADJ", "VERDICT"))
    print("-" * 104)
    for pm in all_pmids:
        man = 'disease-models/wwox/research/deepdive_manifests/PMID%s.json' % pm in tree
        dos = any(p.startswith('disease-models/wwox/research/fulltext_dossiers/PMID%s' % pm) for p in tree)
        padj = any(p.startswith('disease-models/wwox/research/page_adjudications/PMID%s/' % pm) for p in tree)
        rec = receipts.get(pm)
        qadj = queue_blocks.get(pm, False)
        worked = bool(man or dos or padj or rec)
        adjudicated = bool(man or padj or (rec and rec['adjudicative']) or qadj)
        verdict = 'ADJUDICATED_ON_MAIN' if adjudicated else ('WORKED_ON_MAIN' if worked else 'ABSENT_FROM_MAIN')
        rows[pm] = {'manifest': man, 'dossier': dos, 'page_adj': padj,
                    'receipts': rec['n'] if rec else 0,
                    'receipt_adjudicative': bool(rec and rec['adjudicative']),
                    'receipt_evidence_chars': rec['chars'] if rec else 0,
                    'queue_adjudicative': qadj, 'verdict': verdict}
        print("%-10s %-9s %-8s %-22s %-9s %-11s %s"
              % (pm, 'YES' if man else '-', 'YES' if dos else '-',
                 ('%d rows, %d chars%s' % (rec['n'], rec['chars'], ' ADJ' if rec['adjudicative'] else ''))
                 if rec else '-',
                 'YES' if padj else '-', 'YES' if qadj else '-', verdict))

    print()
    for lab in ('ADJUDICATED_ON_MAIN', 'WORKED_ON_MAIN', 'ABSENT_FROM_MAIN'):
        pms = [p for p, v in rows.items() if v['verdict'] == lab]
        print("%-22s %2d  %s" % (lab, len(pms), ' '.join(pms)))

    print()
    print("PER CASE — worst verdict across the case's papers")
    order = {'ABSENT_FROM_MAIN': 0, 'WORKED_ON_MAIN': 1, 'ADJUDICATED_ON_MAIN': 2}
    case_v = {}
    for c, pms in sorted(case_pmids.items()):
        if not pms:
            case_v[c] = 'NO_PMID'
            continue
        case_v[c] = max((rows[p]['verdict'] for p in pms), key=lambda x: order[x])
    for lab in ('ABSENT_FROM_MAIN', 'WORKED_ON_MAIN', 'ADJUDICATED_ON_MAIN', 'NO_PMID'):
        cs = sorted(k for k, v in case_v.items() if v == lab)
        print("  %-22s %2d  %s" % (lab, len(cs), ' '.join(cs)))

    if a.json:
        json.dump({'main': main_ref, 'per_pmid': rows, 'per_case': case_v},
                  open(a.json, 'w'), indent=1)
        print("\nwrote %s" % a.json)
    return 0


if __name__ == '__main__':
    sys.exit(main())
