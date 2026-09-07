#!/usr/bin/env python3
"""CLEAN(case, actor, surface-set) — contamination as a function, not a property.

A case is not "contaminated" full stop. It is contaminated FOR AN ACTOR, because of WHICH
SURFACES THAT ACTOR HOLDS. The same case can be spent for `scientist-a` reading in
`lettore`, and untouched for the same model reading in an allowlisted surface built
outside every checkout.

This command sweeps six surface sets, grades every hit by what it discloses, and prints
CLEAN / NOT_CLEAN per (case, actor).

    python3 learning/scientist/evalset/clean_for_actor.py --case HC-E2
    python3 learning/scientist/evalset/clean_for_actor.py --all --json out.json

SURFACE SETS
  MANDATORY   the 13 inherited participant files enumerated by BENCH-AB-001 surface_spec.json
              (common_files + MODE_A + MODE_B). Every actor holds these; they cannot be
              removed without breaking parity or removing the rules the reading is graded on.
  MAIN        every tracked text file at `main`. Present in every worktree of this repository.
  A_BRANCH    lines ADDED on `lettore`   since its merge-base with main
  B_BRANCH    lines ADDED on `lettore-b` since its merge-base with main
  C_BRANCH    lines ADDED on `lettore-c` since its merge-base with main  (evaluator; swept so
              that evaluator leakage is measured rather than assumed away)
  PARTICIPANT lines ADDED on `bench-blind-participant` relative to main

ACTORS AND WHAT THEY HOLD
  a_in_checkout      MANDATORY + MAIN + A_BRANCH      reading inside the `lettore` worktree
  b_in_checkout      MANDATORY + MAIN + B_BRANCH      reading inside the `lettore-b` worktree
  a_on_surface       MANDATORY                        same model, allowlisted surface, no checkout
  b_on_surface       MANDATORY
  fresh_reader       MANDATORY                        an actor with no branch history here

  `*_on_surface` and `fresh_reader` are byte-identical as FILE sets. They differ only in
  session memory, which no command can inspect; the difference is reported, never claimed
  as measured.

GRADES
  L3 ANSWER    states the case's answer or its decisive discriminating fact  -> NOT_CLEAN
  L2 PREMISE   states a necessary premise, or hands the discriminating concept -> NOT_CLEAN
  L1 QUESTION  names the paper and says something evaluative about it        -> CLEAN, declared
  L0 ID_ONLY   names the paper incidentally / as a tooling example           -> CLEAN

NON-CANONICAL. Mutates nothing. EVALUATOR ONLY - it states answers by implication.
"""
import argparse, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))


def sh(*a):
    return subprocess.run(a, capture_output=True, text=True, cwd=REPO).stdout


# ---------------------------------------------------------------------------------------
# CASE SPECS.
#   ids     : identifiers - a hit alone is L0 unless it co-occurs with something else
#   premise : facts the answer rests on; a hit is L2
#   answer  : the answer or its decisive discriminating fact; a hit is L3
#   question: reveals what is being asked without answering it; a hit is L1
# Every pattern is case-sensitive unless it starts with '(?i)'.
# ---------------------------------------------------------------------------------------
CASES = {
    'HC-E2': dict(
        pmids=['26675548'],
        ids=[r'26675548', r'AbuOdeh2016', r'oncotarget-07-4344'],
        question=[r'ATR-mediated', r'(?i)support\w*\s+its\s+title', r'(?i)WWOX modulates the ATR'],
        premise=[r'(?i)\bCHK1\b.{0,60}(proxy|surrogate|readout for ATR)',
                 r'(?i)KU-?55933', r'(?i)ATM inhibitor'],
        answer=[r'(?i)ATR\b.{0,60}(never|not) (measured|tested|assayed|inhibited|knocked)',
                r'(?i)no ATR (antibody|inhibitor|knockdown|siRNA|shRNA)',
                r'(?i)(title|abstract).{0,80}(unsupported|not supported|overclaim|overshoot)',
                r'(?i)does not support its title',
                r'(?i)ATR.{0,40}\bnot\b.{0,40}\bmeasured\b'],
    ),
    'HC-B3': dict(
        pmids=['34634460'],
        ids=[r'34634460', r'Breton2021'],
        question=[r'(?i)cross[- ]correlation lag', r'(?i)Fig(ure)?\.? ?2C', r'(?i)sign of the lag'],
        premise=[r'(?i)layer II/III.{0,40}lead', r'(?i)which region leads'],
        answer=[r'(?i)minus sign is missing', r'(?i)missing (the )?minus sign',
                r'(?i)axis reads.{0,30}100, 0, 100', r'(?i)unsigned axis'],
    ),
    'HC-E3': dict(
        pmids=['42128308', '42397075'],
        ids=[r'42128308', r'42397075', r'Aqeilan2026'],
        question=[r'(?i)restore\w*\s+SATB2', r'(?i)gene therapy.{0,40}restore'],
        premise=[r'(?i)SATB2.{0,40}(10|ten)\s*[x×]', r'(?i)CTIP2.{0,40}(3|three)\s*[x×]',
                 r'(?i)WT-vs-treated bracket'],
        answer=[r'(?i)above (wild[- ]?type|WT) levels?', r'(?i)"?restored"? is\s+`?UNSUPPORTED',
                r'(?i)overshoot\w*\s+wild[- ]?type', r'(?i)the bracket .{0,30}not drawn'],
    ),
    'HC-F2': dict(
        pmids=['36779245', '42128308'],
        ids=[r'36779245', r'Oliver2023', r'42128308'],
        question=[r'(?i)intermediate[- ](severity )?(class|phenotype)', r'null/missense'],
        premise=[r'(?i)three genotypic classes', r'(?i)one (versus|vs\.?) two missense',
                 r'(?i)Figure 4A orders'],
        answer=[r'(?i)no evidence to support an .?intermediate',
                r'(?i)intermediate class is\s+`?UNSUPPORTED',
                r'(?i)denied by its own source', r'(?i)binary (survival )?stratification'],
    ),
    'HC-F3': dict(
        pmids=[],
        ids=[r'(?i)vigabatrin', r'(?i)VABAM', r'(?i)Shaukat', r'(?i)Choi 2026'],
        question=[r'(?i)defensible position on vigabatrin', r'(?i)vigabatrin.{0,40}(WWOX|DEE)'],
        premise=[r'(?i)MRI (toxicity|abnormalit)', r'(?i)spasms resolved',
                 r'(?i)depolaris\w+ GABA'],
        answer=[r'(?i)conflicting evidence.{0,60}sustain',
                r'(?i)two non-exclusive axes', r'(?i)resolving is the error'],
    ),
    'HC-G2': dict(
        pmids=['42128308'],
        ids=[r'(?i)P47T', r'(?i)SCAR12', r'42128308'],
        question=[r'(?i)protein (level|abundance).{0,40}(functional )?readout',
                  r'(?i)abundance[- ]as[- ]severity'],
        premise=[r'(?i)P47T.{0,60}(WT|wild[- ]?type)[- ]level protein',
                 r'(?i)SCAR12.{0,60}minimal protein'],
        answer=[r'(?i)abundance and function dissociate',
                r'(?i)falsified from both directions',
                r'(?i)(abundance|protein level).{0,50}false in this system'],
    ),
    'HC-I10': dict(
        pmids=['18487609', '15070730', '42395553'],
        ids=[r'18487609', r'42395553', r'15070730'],
        question=[r'(?i)has the full text been retrieved', r'(?i)pdf_only', r'(?i)surface class'],
        premise=[r'(?i)efetch.{0,40}200', r'(?i)8,?781|7,?406|7,?159'],
        answer=[r'(?i)metadata dressed as full text',
                r'(?i)200 is not a body',
                r'(?i)measured property of a named file'],
    ),
    'HC-I2': dict(
        pmids=['16061658'],
        ids=[r'16061658', r'075fdbbcd1e17c3b'],
        question=[r'(?i)text layer.{0,30}usable', r'(?i)Aqeilan 2005'],
        premise=[r'(?i)44,?465', r'(?i)significan\b'],
        answer=[r'(?i)p73[βb]?\s*(as|->|→)\s*p73h', r'(?i)p73h\b', r'(?i)µg.{0,10}(as|->|→).{0,4}Ag',
                r'(?i)zero occurrences of', r'(?i)text layer.{0,30}UNVERIFIABLE_SURFACE',
                r'(?i)63\\x01'],
    ),
    'HC-I3': dict(
        pmids=['23370280'],
        ids=[r'23370280', r'Salah2013', r'd6d46a8c7a2d8ee9'],
        question=[r'(?i)will a reader see (their|the) captions', r'(?i)how many figures does'],
        premise=[r'(?i)caption.{0,30}outside .{0,10}<?body', r'(?i)renderer clips'],
        answer=[r'(?i)6 figures, 0 inside', r'(?i)0/6', r'(?i)zero.{0,20}inside .{0,10}<?body',
                r'(?i)figures: read.{0,40}INVALID'],
    ),
    'HC-I4': dict(
        pmids=['42397075'],
        ids=[r'42397075', r'9c48aa09'],
        question=[r'(?i)regenerated from its declared method', r'(?i)text surface recipe'],
        premise=[r'(?i)PyMuPDF 1\.26\.5', r'(?i)pages joined in order'],
        answer=[r'(?i)NOT_REPRODUCIBLE', r'(?i)bab5bc5d|f2f053fd|76943b7b',
                r'(?i)none match', r'(?i)identity by digest'],
    ),
    'HC-I6': dict(
        pmids=['32185845'],
        ids=[r'(?i)CLAIM 023', r'(?i)CORPUS P206', r'(?i)PAPER 026', r'32185845'],
        question=[r'(?i)what paper supports .?CLAIM 023', r'(?i)Tyr33'],
        premise=[r'(?i)Identifier: PENDING', r'(?i)likely overlaps PAPER 026'],
        answer=[r'(?i)chain of custody does not exist', r'(?i)provenance.{0,20}UNRESOLVED',
                r'(?i)opposite direction for Tyr33', r'(?i)direction reversal into a baseline'],
    ),
    'HC-X1': dict(
        pmids=['29808465'],
        ids=[r'29808465', r'(?i)Johannsen'],
        question=[r'(?i)rests on an abstract', r'(?i)declare[- ]the[- ]limit'],
        premise=[r'(?i)47 citations', r'(?i)seven canonical files'],
        answer=[r'(?i)UNVERIFIABLE_SURFACE', r'(?i)mechanism is undiscriminated',
                r'(?i)closed on all four routes'],
    ),
    'HC-X2': dict(
        pmids=['30356099', '31543760', '39952983'],
        ids=[r'30356099', r'31543760', r'39952983'],
        question=[r'(?i)Europe PMC.{0,30}efetch', r'(?i)body[- ]size disagreement'],
        premise=[r'(?i)45,?559|35,?239|56,?746|40,?700|40,?456|26,?299'],
        answer=[r'(?i)UNRESOLVED — OPEN QUESTION', r'(?i)that is a policy, not a finding',
                r'(?i)never been adjudicated'],
    ),
    'HC-X4': dict(
        pmids=['34634460'],
        ids=[r'34634460', r'(?i)`?ch\?`?'],
        question=[r'(?i)published placeholder', r'(?i)ch\?'],
        premise=[],
        answer=[r'(?i)unresolved placeholder in the published figure'],
    ),
    'HC-X5': dict(
        pmids=['24550385'],
        ids=[r'24550385'],
        question=[r'(?i)motif[- ]tree', r'(?i)leaves sum'],
        premise=[r'(?i)\b563\b|\b355\b|\b240\b|\b144\b'],
        answer=[r'(?i)motif[- ]tree .{0,40}(does not sum|inconsisten)'],
    ),
}

ACTOR_SURFACES = {
    'a_in_checkout': ['MANDATORY', 'MAIN', 'A_BRANCH'],
    'b_in_checkout': ['MANDATORY', 'MAIN', 'B_BRANCH'],
    'a_on_surface': ['MANDATORY'],
    'b_on_surface': ['MANDATORY'],
    'fresh_reader': ['MANDATORY'],
}
BLOCKING = ('L3', 'L2')
TEXT_SUFFIXES = ('.md', '.txt', '.json', '.py', '.yaml', '.yml', '.jsonl', '.tsv', '.cff', '.toml')


def load_surfaces(pins):
    spec = json.load(open(os.path.join(REPO, 'framework/eval/benchmarks/BENCH-AB-001/surface_spec.json')))
    mandatory = sorted(set([c['source'] for c in spec['common_files']]) |
                       {f['source'] for v in spec['per_actor_files'].values()
                        for f in v if 'MODE_' in f['source']})
    surf = {}

    # MANDATORY: whole files, with their line numbers
    rows = []
    for p in mandatory:
        fp = os.path.join(REPO, p)
        if not os.path.exists(fp):
            print("FATAL: mandatory surface missing: %s" % p, file=sys.stderr)
            sys.exit(2)
        for i, ln in enumerate(open(fp, encoding='utf-8', errors='replace'), 1):
            rows.append((p, i, ln.rstrip('\n')))
    surf['MANDATORY'] = rows

    # MAIN: every tracked text file at main
    rows = []
    names = [n for n in sh('git', 'ls-tree', '-r', '--name-only', pins['main']).split('\n') if n]
    for n in names:
        if not n.endswith(TEXT_SUFFIXES):
            continue
        blob = sh('git', 'show', '%s:%s' % (pins['main'], n))
        for i, ln in enumerate(blob.split('\n'), 1):
            rows.append((n, i, ln))
    surf['MAIN'] = rows
    surf['_MAIN_FILES'] = len(names)

    # branch diffs: ADDED lines only
    for key, ref in (('A_BRANCH', pins['lettore']), ('B_BRANCH', pins['lettore-b']),
                     ('C_BRANCH', pins['lettore-c']), ('PARTICIPANT', pins['participant'])):
        base = pins['main'] if key == 'PARTICIPANT' else sh('git', 'merge-base', pins['main'], ref).strip()
        d = sh('git', 'diff', '--unified=0', '%s..%s' % (base, ref))
        rows, cur = [], '?'
        for ln in d.split('\n'):
            if ln.startswith('+++ b/'):
                cur = ln[6:]
            elif ln.startswith('+') and not ln.startswith('+++'):
                rows.append((cur, 0, ln[1:]))
        surf[key] = rows
    return mandatory, surf


def grade_case(spec, surf, which):
    """Return (hits, ungated) where each is (grade, surface, path, line_no, excerpt).

    🔴 GATING. An answer/premise phrase is evidence about THIS case only if it sits in a
    file that also names this case's paper. Without that gate, generic wording matches
    everywhere: `(title|abstract).{0,80}unsupported` fired on a peer's PMID 32000863
    adjudication and was about to be scored as a leak of a PMID 26675548 answer, and
    `ATM inhibitor` fired in four manifests for four other papers.

    The gate is FILE-level, not line-level, and deliberately so: it is the permissive
    direction. A ledger that names every paper gates everything in, which over-reports;
    requiring the id on the same line would silently drop a leak two lines below its
    heading, which under-reports. For a contamination check, over-reporting is the safe
    error and under-reporting is the one that spends a case.
    """
    id_pats = spec['ids'] + [re.escape(p) for p in spec['pmids']]
    files_naming_case = set()
    for s in which:
        for path, _lno, text in surf[s]:
            if path in files_naming_case or not text:
                continue
            for pat in id_pats:
                try:
                    if re.search(pat, text):
                        files_naming_case.add(path)
                        break
                except re.error:
                    continue

    hits, ungated = [], []
    pats = ([('L3', p) for p in spec['answer']] +
            [('L2', p) for p in spec['premise']] +
            [('L1', p) for p in spec['question']] +
            [('L0', p) for p in spec['ids'] + [re.escape(p) for p in spec['pmids']]])
    for s in which:
        for path, lno, text in surf[s]:
            if not text:
                continue
            for grade, pat in pats:
                try:
                    m = re.search(pat, text)
                except re.error:
                    continue
                if m:
                    rec = (grade, s, path, lno, text[max(0, m.start() - 40):m.end() + 60].strip())
                    if grade in ('L3', 'L2') and path not in files_naming_case:
                        ungated.append(rec)
                    else:
                        hits.append(rec)
                    break
    return hits, ungated


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--case', action='append')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--json')
    ap.add_argument('--pin-main', default='main')
    ap.add_argument('--pin-lettore', default='lettore')
    ap.add_argument('--pin-lettore-b', default='lettore-b')
    ap.add_argument('--pin-lettore-c', default='lettore-c')
    ap.add_argument('--pin-participant', default='bench-blind-participant')
    ap.add_argument('--verbose', action='store_true')
    a = ap.parse_args()

    pins = {k: sh('git', 'rev-parse', v).strip() for k, v in
            (('main', a.pin_main), ('lettore', a.pin_lettore), ('lettore-b', a.pin_lettore_b),
             ('lettore-c', a.pin_lettore_c), ('participant', a.pin_participant))}

    cases = list(CASES) if a.all else (a.case or [])
    if not cases:
        print("nothing to do: pass --case HC-XX or --all"); return 2
    unknown = [c for c in cases if c not in CASES]
    if unknown:
        print("unknown case(s): %s" % ' '.join(unknown)); return 2

    mandatory, surf = load_surfaces(pins)

    print("PINS")
    for k, v in pins.items():
        print("  %-12s %s" % (k, v))
    print("SURFACE SIZES (lines swept)")
    print("  %-12s %d   (%d files)" % ('MANDATORY', len(surf['MANDATORY']), len(mandatory)))
    print("  %-12s %d   (%d tracked files at main, text suffixes only)"
          % ('MAIN', len(surf['MAIN']), surf['_MAIN_FILES']))
    for k in ('A_BRANCH', 'B_BRANCH', 'C_BRANCH', 'PARTICIPANT'):
        print("  %-12s %d" % (k, len(surf[k])))
    print()

    # positive control: MANDATORY must contain the one leak we already know is there
    ctrl = [r for r in surf['MANDATORY']
            if 'fulltext_read_receipt' in r[0] and '22193544' in r[2]]
    print("POSITIVE CONTROL  22193544 in fulltext_read_receipt.md within MANDATORY -> %d hit(s) %s"
          % (len(ctrl), 'OK' if ctrl else '*** VOID ***'))
    if not ctrl:
        return 2
    print()

    results = {}
    for cid in cases:
        spec = CASES[cid]
        hits_by_surface, ungated_by_surface = {}, {}
        for s in ('MANDATORY', 'MAIN', 'A_BRANCH', 'B_BRANCH', 'C_BRANCH', 'PARTICIPANT'):
            hits_by_surface[s], ungated_by_surface[s] = grade_case(spec, surf, [s])
        verdicts = {}
        for actor, which in ACTOR_SURFACES.items():
            blocking = [h for s in which for h in hits_by_surface[s] if h[0] in BLOCKING]
            verdicts[actor] = {
                'clean': not blocking,
                'blocking_hits': [{'grade': h[0], 'surface': h[1], 'path': h[2],
                                   'line': h[3], 'excerpt': h[4][:200]} for h in blocking[:8]],
                'blocking_count': len(blocking),
            }
        results[cid] = {
            'surface_hit_counts': {s: {g: sum(1 for h in v if h[0] == g)
                                       for g in ('L3', 'L2', 'L1', 'L0')}
                                   for s, v in hits_by_surface.items()},
            'ungated_dropped': {s: len(v) for s, v in ungated_by_surface.items()},
            'actors': verdicts,
        }

        print("=" * 104)
        print("CASE %s" % cid)
        print("=" * 104)
        print("  %-12s %6s %6s %6s %6s %10s" % ('surface', 'L3', 'L2', 'L1', 'L0', 'ungated'))
        for s in ('MANDATORY', 'MAIN', 'A_BRANCH', 'B_BRANCH', 'C_BRANCH', 'PARTICIPANT'):
            c = results[cid]['surface_hit_counts'][s]
            flag = '  <-- BLOCKING' if (c['L3'] or c['L2']) else ''
            print("  %-12s %6d %6d %6d %6d %10d%s" % (s, c['L3'], c['L2'], c['L1'], c['L0'],
                                                      results[cid]['ungated_dropped'][s], flag))
        print()
        for actor in ('a_in_checkout', 'b_in_checkout', 'a_on_surface', 'b_on_surface', 'fresh_reader'):
            v = verdicts[actor]
            print("  %-16s %-10s %s" % (actor, 'CLEAN' if v['clean'] else 'NOT_CLEAN',
                                        '' if v['clean'] else '(%d blocking)' % v['blocking_count']))
        if a.verbose:
            for s in ('MANDATORY', 'MAIN', 'A_BRANCH', 'B_BRANCH', 'C_BRANCH', 'PARTICIPANT'):
                for h in hits_by_surface[s]:
                    if h[0] in BLOCKING:
                        print("    [%s %-11s] %s:%s  %s" % (h[0], h[1], h[2], h[3] or '-', h[4][:150]))
        print()

    if a.json:
        json.dump({'pins': pins, 'results': results}, open(a.json, 'w'), indent=1)
        print("wrote %s" % a.json)
    return 0


if __name__ == '__main__':
    sys.exit(main())
