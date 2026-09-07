#!/usr/bin/env python3
"""EVALUATOR-SIDE FROZEN SET — the recipe, not an attestation.

Emits `frozen_set_v1.json` deterministically from the table below plus three
measurements taken from the tree at run time. The digest of the emitted bytes is the
frozen-set hash; the command that produces it is printed beside it, so the hash can be
reproduced rather than trusted.

    python3 learning/scientist/evalset/emit_frozen_set.py --emit > /tmp/f.json
    shasum -a 256 /tmp/f.json

NON-CANONICAL. Mutates nothing. Authorizes no benchmark run.
NOT A PARTICIPANT SURFACE — this file states expected answers by implication and must
never enter a reader's allowlisted surface.

Axes are kept apart on purpose:

  ELIGIBILITY          can this case carry a gold standard at all
  SURFACE_LEAK         what the participant-readable inherited surface discloses (L0..L3)
  READER_PRIOR_WORK    what each reader has already written about the case in its own branch
  SURFACE_HELD         whether the deciding artifact is on disk

The single label the task asks for is DERIVED from those by `single_label()`, whose
precedence rule is stated in code so it can be disputed.
"""
import argparse, hashlib, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))

FROZEN_SET_ID = 'EVALSET-BLIND-R1-2026-08-26'

# --------------------------------------------------------------------------------------
# Surface-leak grades, from the sweep over the TRUE inherited participant population
# (surface_spec.json common_files + MODE_A/MODE_B = 13 files), not the prior 12-file
# hand-set which overlapped it by 8.
#
#   L3 ANSWER      the text states the case's answer or its decisive discriminating fact
#   L2 PREMISE     it states a necessary premise, or hands the discriminating concept
#   L1 ATTENTION   it names the paper AND says something evaluative about it
#   L0 INCIDENTAL  it names the paper only as an example about tooling
#   --            no hit
# --------------------------------------------------------------------------------------
LEAK = {
    'HC-B1':  ('L3', 'fulltext_read_receipt.md L145-147 states the complete answer with its reasoning'),
    'HC-A1':  ('L3', 'deepdive_manifest.py L100-101 states the complete answer'),
    'HC-A2':  ('L2', 'deepdive_manifest.py L100-101 gives the panel observation the level question sits on'),
    'HC-I2':  ('L3', 'deepdive_manifest.py L559 names the paper and the exact corruption (p73b->p73h, ug->Ag)'),
    'HC-I1':  ('L3', 'deepdive_manifest.py L340-349 carries the diagnosis and the fix'),
    'HC-F2':  ('L2', 'deepdive_manifest.py L98-99 gives the text finding AND the Figure 4A ordering'),
    'HC-F1':  ('L2', 'epistemic_discipline.md L39 hands the K48/K63 discriminant; names neither WWOX nor ITCH'),
    'HC-E1':  ('L2', 'via the L3 HC-A1 comment on the same figure, plus fulltext_read_receipt.md on 22193544'),
    'HC-J3':  ('L2', 'deepdive_manifest.py names 32000863; fulltext_read_receipt.md names 22193544'),
    'HC-J2':  ('L1', 'fulltext_read_receipt.md names 22193544 and says its supplement repays inspection'),
    'HC-G2':  ('L1', 'fulltext_read_receipt.md names 22193544'),
    'HC-I10': ('L1', 'deepdive_manifest.py L578: 18487609 text layer is unusable - procedural, no science'),
    'HC-I8':  ('L2', 'deepdive_manifest.py names three of the four panel-count papers as parser-hostile'),
    'HC-B2':  ('L1', 'deepdive_manifest.py L578 on 18487609 text layer; no science disclosed'),
    'HC-D2':  ('L1', 'as HC-B2'),
    'HC-G1':  ('L1', 'as HC-B2'),
    'HC-G4':  ('L1', 'as HC-B2'),
    'HC-X5':  ('L1', 'four of its PMIDs named in deepdive_manifest.py as tooling examples'),
    'HC-C3':  ('L1', 'deepdive_manifest.py L343/L601: 24550385 markup boundaries, reading anchored to XML'),
    'HC-D4':  ('L1', 'as HC-C3, plus L463 on 26675548 timepoint labels'),
    'HC-D1':  ('L1', 'deepdive_manifest.py L1275 (19500159 mutation test) and L1383 (19936220 EPMC example)'),
    'HC-I5':  ('L0', 'deepdive_manifest.py L463: 26675548 "two days (D2), D5 and D7" is a timepoint label'),
    'HC-E2':  ('L0', 'deepdive_manifest.py L463 only - a timepoint-label example, no science'),
    'HC-H1':  ('L2', '42422765 named x14 across three surface files; 42397075 x12 in the instructions'),
    'HC-E3':  ('L2', 'BENCHMARK_INSTRUCTIONS.md and OUTPUT_SCHEMA.md are paper-specific to 42397075'),
    'HC-I4':  ('L2', 'as HC-E3 - the case IS 42397075 provenance and the instructions enumerate it'),
}
LEAK_DEFAULT = ('--', 'no hit over the 13-file inherited population, 27 PMIDs + 50 content patterns')

# --------------------------------------------------------------------------------------
# Reader prior work. VERIFIED_* rows were read line by line this session; SCREENED_* rows
# come from the adjudicative-language screen and are an UPPER BOUND, not a classification.
# --------------------------------------------------------------------------------------
READER = {
    'HC-D1':  ('ADJUDICATED', 'CLEAN', 'VERIFIED', 'lettore: "PMID 19936220 ... epileptogenesis not measured in any form" and "a Table 2 whose Epilepsy row is empty for both mouse models"'),
    'HC-C1':  ('ADJUDICATED', 'CLEAN', 'VERIFIED', 'lettore: "Figure 6: four bar charts ... not one significance marker or p-value anywhere in the figure"'),
    'HC-G1':  ('ADJUDICATED', 'CLEAN', 'VERIFIED', 'lettore: "Panel 5A measures the in-vivo direction and it is up, not down: RUNX2 at 1.50 in femur"'),
    'HC-C2':  ('ADJUDICATED', 'CLEAN', 'VERIFIED', 'lettore: "Figure 3\'s caption inverts the asterisk convention (* p = 0.0036, ** p = 0.027) while Figure 6 has it right"'),
    'HC-C4':  ('ADJUDICATED', 'CLEAN', 'VERIFIED', 'lettore: "one affected fetus against one control fetus - Methods say one, Results say three"'),
    'HC-B6':  ('CLEAN', 'ADJUDICATED', 'VERIFIED', 'lettore-b: "Calpain. Rejected as an established WWOX turnover route (DIS-008): no proteolysis was ever ..."'),
    'HC-D4':  ('ADJUDICATED', 'CLEAN', 'VERIFIED', 'lettore: "The text says ... but not the mutated form WWOX-K274R. The blot shows a clear band. Reduced, not abolished."'),
    'HC-F1':  ('ADJUDICATED', 'CLEAN', 'VERIFIED', 'lettore types the claim "DNA damage promotes ITCH-dependent K63 ubiquitination of WWOX at Lys274 | DATO" and carries a DEGRADATION_DIRECTION_GATE'),
    'HC-G4':  ('ADJUDICATED', 'CLEAN', 'VERIFIED', 'lettore: "three heterozygote-sensitive readouts (slice bursting incidence, sIPSC amplitude, resting ...)"'),
    'HC-I8':  ('ADJUDICATED', 'WORKED', 'VERIFIED', 'lettore and lettore-b both report per-paper panel-count errors on the case\'s own papers'),
    'HC-A1':  ('ADJUDICATED', 'ADJUDICATED', 'VERIFIED', 'both branches carry the PMID32000863 lithium adjudication pilot (62/111 references)'),
    'HC-A2':  ('ADJUDICATED', 'ADJUDICATED', 'VERIFIED', 'as HC-A1, same figure'),
    'HC-E1':  ('ADJUDICATED', 'ADJUDICATED', 'VERIFIED', 'as HC-A1; lettore-b holds PILOT_PMID32000863_GSK3B_LITHIUM_ADJUDICATION'),
    'HC-J3':  ('ADJUDICATED', 'ADJUDICATED', 'VERIFIED', 'as HC-A1'),
    'HC-B1':  ('WORKED', 'WORKED', 'VERIFIED', 'both name 22193544; neither restates the Tau finding, which is already in the discipline file'),
    'HC-J2':  ('WORKED', 'WORKED', 'VERIFIED', 'both name 22193544; neither touches GS-1 or substrate selectivity'),
    'HC-D3':  ('ADJUDICATED', 'WORKED', 'VERIFIED', 'lettore cites manifest PMID42128308 entry 9 on the Olig2-Cre readout as a designed false negative'),
    'HC-H1':  ('ADJUDICATED', 'WORKED', 'VERIFIED', 'lettore cites manifest PMID42128308 entry 24 on the Abudiab preprint / successor relation'),
    'HC-A3':  ('MENTIONED', 'WORKED', 'VERIFIED', 'neither names the paper and the cell-identity terms on one line; lettore-b asserts a progenitor defect at model level'),
    'HC-B2':  ('WORKED', 'CLEAN', 'VERIFIED', 'lettore quantifies Figure 4B tissue density and reports a misread bar in panel 3D, not 4B'),
    'HC-B4':  ('CLEAN', 'CLEAN', 'VERIFIED', 'zero lines on either branch match Fig 5D or the caption-vs-panel terms'),
    'HC-B5':  ('WORKED', 'MENTIONED', 'VERIFIED', 'no line names the paper and the fragile-site taxonomy together; zero taxonomy hits on both'),
    'HC-A4':  ('WORKED', 'WORKED', 'VERIFIED', 'no line names the paper and the two amplitude arms together'),
    'HC-C3':  ('MENTIONED', 'MENTIONED', 'VERIFIED', 'both mention 24550385 only for panel-count / extractor defects'),
    'HC-E2':  ('MENTIONED', 'CLEAN', 'VERIFIED', 'lettore names 26675548 three times, all on the K274R blot and the caption census; zero on ATR or the title'),
    'HC-I5':  ('MENTIONED', 'CLEAN', 'VERIFIED', 'as HC-E2, same three lines'),
    'HC-G3':  ('WORKED', 'WORKED', 'VERIFIED', 'no line names 34268881 and the stage-confound terms together'),
    'HC-D2':  ('WORKED', 'WORKED', 'VERIFIED', 'no line names 18487609 and the osteoclast terms together'),
    'HC-F4':  ('CLEAN', 'MENTIONED', 'VERIFIED', 'one bare mention on lettore-b; no adjudication'),
    'HC-I1':  ('CLEAN', 'CLEAN', 'VERIFIED', 'zero hits'),
    'HC-I7':  ('CLEAN', 'CLEAN', 'VERIFIED', 'zero hits'),
    'HC-I9':  ('CLEAN', 'CLEAN', 'VERIFIED', 'zero hits'),
    'HC-J1':  ('CLEAN', 'CLEAN', 'VERIFIED', 'zero hits'),
    'HC-X3':  ('CLEAN', 'CLEAN', 'VERIFIED', 'zero hits'),
}
READER_DEFAULT = ('SCREENED', 'SCREENED', 'SCREEN_ONLY',
                  'adjudicative-language screen fired; NOT read line by line - an upper bound, not a classification')

# --------------------------------------------------------------------------------------
# Eligibility. `prior` is the prior artifact's assignment; `now` is this session's, and
# every row where they differ carries the measurement that moved it.
# --------------------------------------------------------------------------------------
ELIG = {
    'HC-A1': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-A2': ('UNRESOLVABLE', 'UNRESOLVABLE', ''),
    'HC-A3': ('GOLD_ELIGIBLE', 'UNVERIFIABLE_SURFACE',
              'the deciding panel is required and PMID 32581702 is held as PMC XML only - no PDF, no figure asset, no page-adjudication crop'),
    'HC-A4': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE',
              'confirmed text-decidable: 23.3 / 24.7 / 57.3 / 27.5 each occur in the held XML, so no figure surface is needed'),
    'HC-B1': ('UNRESOLVABLE', 'UNRESOLVABLE', ''),
    'HC-B2': ('GOLD_ELIGIBLE', 'UNVERIFIABLE_SURFACE',
              'the bar assignment is read off Figure 4B; PMID 18487609 is held as PDF + PMC HTML, so the figure IS reachable - retained as GOLD_ELIGIBLE only if the reader renders from the PDF; flagged because the prior spec cited no render route'),
    'HC-B3': ('STRESS_ONLY', 'STRESS_ONLY',
              'and additionally surface-incomplete: the axis sign lives in a Breton figure and no figure surface is held'),
    'HC-B4': ('GOLD_ELIGIBLE', 'UNVERIFIABLE_SURFACE',
              'the case turns on what the PANEL prints against what the caption says; PMID 34634460 is held as PMC XML only, its six graphic hrefs (gr1..gr6.jpg) are not on disk, and the string "5D" occurs 0 times in the XML'),
    'HC-B5': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-B6': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-C1': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-C2': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE',
              'confirmed text-decidable: both asterisk definitions are printed inside <fig> captions in the held XML'),
    'HC-C3': ('GOLD_WITH_MULTIPLE', 'GOLD_WITH_MULTIPLE', ''),
    'HC-C4': ('UNRESOLVABLE', 'UNRESOLVABLE',
              'the Methods-vs-Results half is text-decidable in the held XML; the third surface (the Ctrl column) is not held'),
    'HC-D1': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-D2': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-D3': ('STRESS_ONLY', 'STRESS_ONLY', ''),
    'HC-D4': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-E1': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-E2': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-E3': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-F1': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-F2': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-F3': ('GOLD_WITH_MULTIPLE', 'GOLD_WITH_MULTIPLE', ''),
    'HC-F4': ('UNRESOLVABLE', 'UNVERIFIABLE_SURFACE',
              'neither terminal surface is held: PMID 12065620 absent, and the citing review PMC3139124 absent - only Saeki (PMID 21212533) is on disk. The prior artifact named one acquisition; there are two'),
    'HC-G1': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-G2': ('STRESS_ONLY', 'STRESS_ONLY', ''),
    'HC-G3': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-G4': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-H1': ('UNVERIFIABLE_SURFACE', 'UNVERIFIABLE_SURFACE', ''),
    'HC-I1': ('EXCLUDE', 'EXCLUDE', ''),
    'HC-I2': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-I3': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-I4': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-I5': ('UNVERIFIABLE_SURFACE', 'CASE_PREMISE_FALSIFIED',
              'the supplement IS held: files/fulltext/PMID26675548_assets/oncotarget-07-4344-s001.pdf, 1527965 bytes, 7 pages, page 4 headed "Supplementary Figure S4: Impaired checkpoint activation in MCF7 cells". The prior status rested on an INHERITED claim that it sat behind a challenge. E-1 does not fail, so the gold "a declared, addressed gap" is void'),
    'HC-I6': ('STRESS_ONLY', 'STRESS_ONLY', ''),
    'HC-I7': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-I8': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-I9': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-I10': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-J1': ('UNVERIFIABLE_SURFACE', 'UNVERIFIABLE_SURFACE', ''),
    'HC-J2': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-J3': ('GOLD_ELIGIBLE', 'GOLD_ELIGIBLE', ''),
    'HC-X1': ('UNVERIFIABLE_SURFACE', 'UNVERIFIABLE_SURFACE', ''),
    'HC-X2': ('EXCLUDE', 'EXCLUDE', ''),
    'HC-X3': ('EXCLUDE', 'EXCLUDE', ''),
    'HC-X4': ('EXCLUDE', 'EXCLUDE', ''),
    'HC-X5': ('EXCLUDE', 'EXCLUDE', ''),
}

# Cases contaminated by construction: the question IS repository state, so no allowlist
# build can make them blind. Recorded separately from the measured leak.
BY_CONSTRUCTION = {'HC-I6', 'HC-I7', 'HC-J3', 'HC-I4', 'HC-I10'}


def single_label(case, leak_grade, reader_a, reader_b, elig_now):
    """Precedence, stated so it can be disputed:
    contamination outranks eligibility, because a spent case cannot be run at all;
    among uncontaminated cases the eligibility class is the informative label."""
    if case in BY_CONSTRUCTION:
        return 'FULLY_CONTAMINATED'
    if leak_grade == 'L3' or 'ADJUDICATED' in (reader_a, reader_b):
        return 'FULLY_CONTAMINATED'
    if leak_grade == 'L2' or 'SCREENED' in (reader_a, reader_b):
        return 'PARTIALLY_CONTAMINATED'
    if leak_grade == 'L1' or 'WORKED' in (reader_a, reader_b):
        return 'PARTIALLY_CONTAMINATED'
    if elig_now in ('UNRESOLVABLE', 'STRESS_ONLY'):
        return elig_now
    return 'CLEAN_BLIND'


# The five requested labels describe CONTAMINATION and, for two of them, eligibility class.
# None of them can say "this case cannot be run at all", so a case whose surface is missing
# comes out CLEAN_BLIND - clean, and unrunnable. That is the very confusion the rubric warns
# against: rewarding "cannot be determined" where the honest answer is "go and get the file".
# `dispatchable` and `blocker` carry it separately rather than overloading the label.
NOT_DISPATCHABLE = {
    'UNVERIFIABLE_SURFACE': 'deciding surface not held - acquire it, then re-classify',
    'CASE_PREMISE_FALSIFIED': 'the case rests on a fact this session measured to be false',
    'EXCLUDE': 'excluded by the rubric; not a benchmark item',
}


def dispatchable(label, elig_now):
    if elig_now in NOT_DISPATCHABLE:
        return False, NOT_DISPATCHABLE[elig_now]
    if label == 'FULLY_CONTAMINATED':
        return False, 'answer already held by a required surface or by a reader'
    if label == 'PARTIALLY_CONTAMINATED':
        return True, 'dispatchable only with the residual declared to the evaluator'
    return True, ''


def sh(*a):
    return subprocess.run(a, capture_output=True, text=True, cwd=REPO).stdout.strip()


def digest(path):
    try:
        with open(path, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    except OSError:
        return None


def build(corpus_root, pins=None):
    pins = pins or {}
    case_pmids_src = os.path.join(REPO, 'learning/scientist/HARD_CASE_MINING_BENCHMARK_CANDIDATES_SCIC_v1.md')
    txt = open(case_pmids_src, encoding='utf-8').read()
    starts = [(m.start(), m.group(1)) for m in re.finditer(r'^#### `(HC-[A-Z]\d+)`', txt, re.M)]
    case_pmids = {}
    for i, (pos, cid) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(txt)
        case_pmids[cid] = sorted(set(re.findall(r'PMID\s*(\d{7,8})', txt[pos:end])))

    held = {}
    if os.path.isdir(corpus_root):
        names = os.listdir(corpus_root)
        for pm in sorted({p for v in case_pmids.values() for p in v}):
            held[pm] = sorted(n for n in names if pm in n)

    cases = {}
    for cid in sorted(case_pmids):
        lg, lev = LEAK.get(cid, LEAK_DEFAULT)
        ra, rb, rprov, rev = READER.get(cid, READER_DEFAULT)
        ep, en, emv = ELIG[cid]
        lbl = single_label(cid, lg, ra, rb, en)
        disp, blocker = dispatchable(lbl, en)
        cases[cid] = {
            'pmids': case_pmids[cid],
            'surfaces_held': {pm: held.get(pm, []) for pm in case_pmids[cid]},
            'eligibility_prior': ep,
            'eligibility_now': en,
            'eligibility_moved_by': emv,
            'surface_leak_grade': lg,
            'surface_leak_evidence': lev,
            'reader_prior_work': {'scientist_a_branch_lettore': ra,
                                  'scientist_b_branch_lettore_b': rb,
                                  'provenance': rprov, 'evidence': rev},
            'contaminated_by_construction': cid in BY_CONSTRUCTION,
            'single_label': lbl,
            'dispatchable': disp,
            'blocker': blocker,
        }

    inputs = {}
    for p in ['learning/scientist/HARD_CASE_MINING_BENCHMARK_CANDIDATES_SCIC_v1.md',
              'learning/scientist/BENCHMARK_ELIGIBILITY_AND_BLIND_DESIGN_SCIC_v1.md',
              'framework/eval/benchmarks/BENCH-AB-001/surface_spec.json',
              'framework/protocols/controlled_benchmark_ab.md']:
        inputs[p] = digest(os.path.join(REPO, p))

    spec = json.load(open(os.path.join(REPO, 'framework/eval/benchmarks/BENCH-AB-001/surface_spec.json')))
    population = sorted(set([c['source'] for c in spec['common_files']]) |
                        {f['source'] for v in spec['per_actor_files'].values()
                         for f in v if 'MODE_' in f['source']})

    # The reader_prior_work axis is measured against two LIVE branches. Binding it to their
    # tips is not decoration: both moved by ~1000 added lines while this set was being built,
    # and an axis measured against an unnamed object is an attestation.
    tips = {}
    for b in ('lettore', 'lettore-b'):
        ref = pins.get(b) or b
        tip = sh('git', 'rev-parse', ref)
        mb = sh('git', 'merge-base', 'main', tip)
        tips[b] = {
            'tip': tip,
            'pinned': bool(pins.get(b)),
            'merge_base_with_main': mb,
            'commits_ahead': sh('git', 'rev-list', '--count', mb + '..' + tip),
            'committed_at': sh('git', 'log', '-1', '--format=%cI', tip),
        }

    return {
        '_schema': 'LEGEND evaluation - evaluator-side frozen case set v1',
        '_warning': 'EVALUATOR ONLY. Never place this file, or anything derived from it, '
                    'in a participant surface.',
        'frozen_set_id': FROZEN_SET_ID,
        'head': sh('git', 'rev-parse', pins.get('head') or 'HEAD'),
        'head_pinned': bool(pins.get('head')),
        'branch': sh('git', 'rev-parse', '--abbrev-ref', 'HEAD'),
        'corpus_root': corpus_root,
        'corpus_root_note': 'files/ is gitignored, so the held-surface census is a property of '
                            'this working directory, not of the repository. A worktree with an '
                            'empty files/ would report every surface absent.',
        'reader_branch_tips': tips,
        'reader_axis_shelf_life': 'The reader branches are live. This axis describes their tips '
                                  'above and nothing later. Re-run before any dispatch; a case '
                                  'clean at these tips can be spent by the next commit.',
        'inherited_participant_population': population,
        'inherited_participant_population_n': len(population),
        'prior_handset_overlap': '8 of 13 (62%) - the prior sweep swept 4 files not in the '
                                 'surface and missed 5 that are',
        'inputs_sha256': inputs,
        'label_precedence': 'by_construction > L3|reader_ADJUDICATED > L2|reader_SCREENED > '
                            'L1|reader_WORKED > eligibility(UNRESOLVABLE|STRESS_ONLY) > CLEAN_BLIND',
        'cases': cases,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--emit', action='store_true')
    ap.add_argument('--corpus-root', default='<REPO_ROOT>/files/fulltext')
    ap.add_argument('--summary', action='store_true')
    ap.add_argument('--pin-lettore', default=None,
                    help='commit to measure branch lettore at; omit to use the live tip')
    ap.add_argument('--pin-lettore-b', default=None,
                    help='commit to measure branch lettore-b at; omit to use the live tip')
    ap.add_argument('--pin-head', default=None,
                    help='the commit this set is anchored to; omit to use the live HEAD. '
                         'Pin it, or the digest moves every time this branch commits.')
    a = ap.parse_args()
    pins = {'lettore': a.pin_lettore, 'lettore-b': a.pin_lettore_b, 'head': a.pin_head}
    data = build(a.corpus_root, pins)
    blob = json.dumps(data, indent=1, sort_keys=True, ensure_ascii=True) + '\n'
    if a.emit:
        sys.stdout.write(blob)
        return
    print("FROZEN_SET_ID %s" % data['frozen_set_id'])
    print("HEAD          %s" % data['head'])
    print("SHA256        %s" % hashlib.sha256(blob.encode()).hexdigest())
    t = data['reader_branch_tips']
    print("RECIPE        python3 learning/scientist/evalset/emit_frozen_set.py --emit \\\n"
          "                --corpus-root %s \\\n"
          "                --pin-head %s \\\n"
          "                --pin-lettore %s \\\n"
          "                --pin-lettore-b %s | shasum -a 256"
          % (a.corpus_root, data['head'], t['lettore']['tip'], t['lettore-b']['tip']))
    if not data['head_pinned']:
        print("              ^ HEAD was NOT pinned for this run: the digest above moves the next "
              "time this branch commits.")
    print()
    counts = {}
    for c in data['cases'].values():
        counts[c['single_label']] = counts.get(c['single_label'], 0) + 1
    for k in sorted(counts):
        print("  %-24s %d" % (k, counts[k]))
    print("  %-24s %d" % ('TOTAL', sum(counts.values())))
    disp = [k for k, v in data['cases'].items() if v['dispatchable']]
    print()
    print("  DISPATCHABLE             %d   %s" % (len(disp), ' '.join(sorted(disp))))
    clean_disp = [k for k in disp if data['cases'][k]['single_label'] == 'CLEAN_BLIND']
    print("  ...of which CLEAN_BLIND  %d   %s" % (len(clean_disp), ' '.join(sorted(clean_disp))))
    if a.summary:
        print()
        print("%-8s %-22s %-4s %-11s %-11s %-23s %s"
              % ("CASE", "ELIGIBILITY_NOW", "LEAK", "READER_A", "READER_B", "LABEL", "DISP"))
        for cid, c in data['cases'].items():
            r = c['reader_prior_work']
            print("%-8s %-22s %-4s %-11s %-11s %-23s %s"
                  % (cid, c['eligibility_now'], c['surface_leak_grade'],
                     r['scientist_a_branch_lettore'], r['scientist_b_branch_lettore_b'],
                     c['single_label'], 'YES' if c['dispatchable'] else 'no'))


if __name__ == '__main__':
    main()
