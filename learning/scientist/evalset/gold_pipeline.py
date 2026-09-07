#!/usr/bin/env python3
"""GOLD PIPELINE — what each case still needs, computed rather than asserted.

Three stages, and a case advances only by an ACT, never by a judgement about it:

    FIRST_ADJUDICATION            an adjudicated answer exists, by a named actor
    SECOND_INDEPENDENT_ADJUDICATION   a second, by a DIFFERENT actor who did not see the
                                  first and is not disqualified for the case
    GOLD_READY                    both exist and agree, or their disagreement is itself
                                  adjudicated

🔴 The finding this file exists to make unavoidable.

`main` carries an adjudicating artifact for 24 of 27 case papers, spending 43 of 48 cases
in every worktree. So any evaluator who has worked in this repository is disqualified as
independent adjudicator for almost every case — including me, for every case I have
adjudicated. I hold three FIRST adjudications and can supply zero SECONDs.

That makes the gold pipeline blocked on the SAME resource as the reading pipeline: an
actor with no history here. And it needs that resource TWICE PER CASE, in two roles that
cannot be the same actor —

    the READER, who must not know the answer, and
    the SECOND ADJUDICATOR, who must not have seen the first adjudication

— because an actor who adjudicates a case has thereby read its answer and can never be its
reader, and an actor who reads a case has produced the output the adjudication grades.

    N distinct uncontaminated actors are required, not one recruited N times.

    python3 learning/scientist/evalset/gold_pipeline.py
    python3 learning/scientist/evalset/gold_pipeline.py --state <state.json>

EVALUATOR TOOL.
"""
import argparse, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_STATE = os.path.join(HERE, 'gold_pipeline_state.json')


def stage(case, actors):
    """Compute a case's stage and its single next blocking act."""
    first = case.get('first_adjudication')
    second = case.get('second_adjudication')
    blockers = []

    if not first:
        missing = case.get('missing_act_for_first')
        blockers.append('FIRST_ADJUDICATION: %s' % (missing or 'not started'))
        return 'NO_ADJUDICATION', blockers

    # A second adjudicator must be a DIFFERENT actor, and must not be disqualified.
    if not second:
        disq = sorted({first['by']} | set(case.get('disqualified_actors') or []))
        eligible = [a for a, rec in actors.items()
                    if a not in disq and rec.get('exposure_to_this_repository') == 'NONE']
        if eligible:
            blockers.append('SECOND_INDEPENDENT_ADJUDICATION: available now from %s'
                            % ', '.join(eligible))
        else:
            blockers.append('SECOND_INDEPENDENT_ADJUDICATION: no eligible actor exists. '
                            'Disqualified: %s' % ', '.join(disq))
        return 'FIRST_ONLY', blockers

    if second['by'] == first['by']:
        blockers.append('SECOND_INDEPENDENT_ADJUDICATION: same actor as the first; not independent')
        return 'FIRST_ONLY', blockers

    if case.get('agreement') is None:
        blockers.append('GOLD_READY: two adjudications exist and have not been compared')
        return 'TWO_UNCOMPARED', blockers
    if case['agreement'] is False and not case.get('disagreement_adjudicated'):
        blockers.append('GOLD_READY: the two disagree and the disagreement is unadjudicated')
        return 'DISAGREEMENT_OPEN', blockers
    return 'GOLD_READY', []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--state', default=DEFAULT_STATE)
    a = ap.parse_args()
    if not os.path.exists(a.state):
        print("VOID: no declared state at %s" % a.state)
        return 2
    st = json.load(open(a.state, encoding='utf-8'))
    actors = st.get('actors', {})
    cases = st.get('cases', {})

    counts = {}
    print("%-10s %-20s %s" % ('CASE', 'STAGE', 'NEXT BLOCKING ACT'))
    print("-" * 100)
    for cid in sorted(cases):
        s, b = stage(cases[cid], actors)
        counts[s] = counts.get(s, 0) + 1
        print("%-10s %-20s %s" % (cid, s, (b[0] if b else '—')[:66]))

    print()
    for k in ('NO_ADJUDICATION', 'FIRST_ONLY', 'TWO_UNCOMPARED', 'DISAGREEMENT_OPEN',
              'GOLD_READY'):
        print("  %-22s %d" % (k, counts.get(k, 0)))

    print()
    print("GOLD_READY_COUNT   %d" % counts.get('GOLD_READY', 0))
    clean = [a_ for a_, r in actors.items()
             if r.get('exposure_to_this_repository') == 'NONE']
    print("UNCONTAMINATED ACTORS ON RECORD   %d %s" % (len(clean), clean or ''))
    print()
    need = counts.get('FIRST_ONLY', 0) + counts.get('NO_ADJUDICATION', 0)
    print("🔴 Every case short of GOLD_READY is short of the SAME resource: an actor with no")
    print("   history in this repository. %d case(s) need one, and each needs TWO distinct" % need)
    print("   ones — a reader who must not know the answer, and a second adjudicator who must")
    print("   not have seen the first. Neither role can be filled by the other's occupant.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
