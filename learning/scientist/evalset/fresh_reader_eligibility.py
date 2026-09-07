#!/usr/bin/env python3
"""FRESH-READER ELIGIBILITY — not A/B eligibility.

A fresh reader is an actor with no history in this repository, reading on a surface built
by allowlist outside every checkout. It therefore holds exactly two things: the thirteen
inherited participant files, and the packet. `main` is not there. Neither reader branch is
there. So `main` contamination, which spends 43 of 48 cases in a checkout, is IRRELEVANT
here -- and that is the whole point of building the surface.

Six fields per case, all measured:

  SOURCE_AVAILABLE              every surface the case's minimum evidence names is on disk
  QUESTION_SELF_CONTAINED       answerable from published sources alone; a question about
                                repository state is not
  SURFACE_BUILDABLE             SOURCE_AVAILABLE and the boundary is nameable as files
  GOLD_AVAILABLE_OR_ADJUDICATABLE   a determinate answer exists on the packet
  UNRESOLVABLE                  the gold IS "the record does not decide"
  ANSWER_LEAKAGE                L2/L3 in the thirteen inherited files -- the only leak a
                                built surface cannot remove

Run from the repository root.
"""
import json, os, sys, importlib.util, argparse

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
CORPUS = '<REPO_ROOT>/files/fulltext'

# Questions whose subject is repository or pipeline state, not a published record.
# A fresh reader has no repository, so these are unanswerable on a built surface by
# construction -- not contaminated, simply not this kind of question.
REPO_STATE = {'HC-I6', 'HC-I7', 'HC-I10', 'HC-I4', 'HC-X2', 'HC-I9'}
# Cases whose minimum evidence is a figure raster for a paper held as text only.
FIGURE_NOT_HELD = {'HC-A3', 'HC-B3', 'HC-B4', 'HC-C4', 'HC-X4'}
# Excluded by the rubric for reasons unrelated to contamination.
RUBRIC_EXCLUDED = {'HC-I1', 'HC-X3', 'HC-X5', 'HC-I5'}
UNRESOLVABLE = {'HC-A2'}
GOLD_MULTIPLE = {'HC-C3', 'HC-F3'}


def load_frozen():
    spec = importlib.util.spec_from_file_location(
        "efs", os.path.join(REPO, 'learning/scientist/evalset/emit_frozen_set.py'))
    m = importlib.util.module_from_spec(spec)
    argv, sys.argv = sys.argv, ['x']
    spec.loader.exec_module(m)
    sys.argv = argv
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--json')
    a = ap.parse_args()
    m = load_frozen()
    cp = json.load(open(os.path.join(REPO, 'learning/scientist/evalset/case_pmids.json')))
    case_pmids = cp['case_pmids']
    names = os.listdir(CORPUS) if os.path.isdir(CORPUS) else []

    rows = {}
    for cid in sorted(m.ELIG):
        leak_grade = m.LEAK.get(cid, ('--', ''))[0]
        answer_leakage = leak_grade in ('L2', 'L3')

        pms = case_pmids.get(cid, [])
        held = all(any(pm in n for n in names) for pm in pms) if pms else False
        if cid in FIGURE_NOT_HELD:
            held = False
        source_available = held

        self_contained = cid not in REPO_STATE and bool(pms)
        buildable = source_available and self_contained
        unres = cid in UNRESOLVABLE
        elig_now = m.ELIG[cid][1]
        gold_ok = (elig_now in ('GOLD_ELIGIBLE', 'GOLD_WITH_MULTIPLE', 'UNRESOLVABLE')
                   and cid not in RUBRIC_EXCLUDED)

        eligible = (buildable and gold_ok and not answer_leakage)
        why = []
        if answer_leakage:
            why.append('answer/premise in the inherited files (%s)' % leak_grade)
        if not source_available:
            why.append('source not held' if pms else 'no bounded packet')
        if not self_contained:
            why.append('question is about repository state')
        if not gold_ok:
            why.append('eligibility: %s' % elig_now)
        rows[cid] = {'source_available': source_available,
                     'question_self_contained': self_contained,
                     'surface_buildable': buildable,
                     'gold_available_or_adjudicatable': gold_ok,
                     'unresolvable': unres,
                     'answer_leakage': leak_grade if answer_leakage else 'none',
                     'fresh_reader_eligible': eligible,
                     'not_eligible_because': why}

    print("%-8s %-6s %-6s %-6s %-6s %-6s %-8s  %s"
          % ("CASE", "SRC", "SELF", "BUILD", "GOLD", "UNRES", "LEAK", "FRESH_READER"))
    print("-" * 104)
    for cid, r in rows.items():
        print("%-8s %-6s %-6s %-6s %-6s %-6s %-8s  %s"
              % (cid, 'Y' if r['source_available'] else '-',
                 'Y' if r['question_self_contained'] else '-',
                 'Y' if r['surface_buildable'] else '-',
                 'Y' if r['gold_available_or_adjudicatable'] else '-',
                 'Y' if r['unresolvable'] else '-', r['answer_leakage'],
                 'ELIGIBLE' if r['fresh_reader_eligible'] else
                 'not: ' + '; '.join(r['not_eligible_because'])[:58]))
    el = [c for c, r in rows.items() if r['fresh_reader_eligible']]
    print()
    print("FRESH_READER_ELIGIBLE  %d  %s" % (len(el), ' '.join(el)))
    print("NOT_ELIGIBLE           %d" % (len(rows) - len(el)))
    reasons = {}
    for c, r in rows.items():
        if not r['fresh_reader_eligible']:
            reasons.setdefault(r['not_eligible_because'][0], []).append(c)
    for k, v in sorted(reasons.items(), key=lambda kv: -len(kv[1])):
        print("   %-52s %2d  %s" % (k, len(v), ' '.join(v)))
    if a.json:
        json.dump(rows, open(a.json, 'w'), indent=1)
        print("\nwrote %s" % a.json)


if __name__ == '__main__':
    main()
