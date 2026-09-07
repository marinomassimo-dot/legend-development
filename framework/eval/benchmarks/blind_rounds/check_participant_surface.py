#!/usr/bin/env python3
"""PARTICIPANT SURFACE CHECK.

A participant handoff is allowed to carry six fields and nothing else. This command
decides that mechanically, so "no adjudication reached the participant" is a check rather
than a promise.

    python3 framework/eval/benchmarks/blind_rounds/check_participant_surface.py

Three checks per handoff file:

  SCHEMA      exactly the six permitted field names, each present exactly once, and no
              seventh field-shaped line
  LANGUAGE    no adjudicative or expectation-bearing token anywhere in the file
  CONTAINMENT no link or path that leaves this directory

A positive control runs first: a synthetic file carrying one forbidden token in each class
must FAIL all three. If the control passes, the checker cannot fail and the run is void —
which is the failure mode a checker most often has and least often reports.

Exit 0 = surface clean. Exit 1 = at least one finding. Exit 2 = control void.
"""
import argparse, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_PARTICIPANT = os.path.join(HERE, 'participant')

PERMITTED_FIELDS = ['CASE_ID', 'QUESTION', 'CORPUS_BOUNDARY', 'ALLOWED_SURFACES',
                    'EXCLUDED_SURFACES', 'STOP_CONDITION']
# A dispatch packet points at a BUILT surface, so it names a surface hash instead of a
# corpus boundary, and the exclusions live in the surface's own ASSIGNMENT.md rather than
# being restated here. Different shape, same rule: an enumerated field set, nothing else.
PACKET_FIELDS = ['CASE_ID', 'QUESTION', 'PARTICIPANT_SURFACE_HASH', 'ALLOWED_FILES',
                 'STOP_CONDITION']

# Any of these in a participant file means an evaluator sentence crossed the boundary.
FORBIDDEN_LANGUAGE = [
    r'\bEXPECTED_ANSWER\b', r'\bGOLD[_ ]?(LABEL|STANDARD|ELIGIBLE|SPEC)\b', r'\bGOLD-\d',
    r'\bEXPECTED_VERDICT\b', r'\bEXPECTED_EPISTEMIC', r'\bEXPECTED_OBSERVATION',
    r'\bEXPECTED_CORRECT', r'\bWHY_DIFFICULT\b', r'\bKNOWN_FAILURE\b', r'\bFAILURE_MODE\b',
    r'\bCOMMON_FAILURE\b', r'\bNEGATIVE_CONTROL\b', r'\bBENCHMARK_VALUE\b', r'\bBENCHMARK_CLASS\b',
    r'\bRANK\b', r'\bCONTAMINATION_STATUS\b', r'\bCLEAN_BLIND\b', r'\bPARTIALLY_CONTAMINATED\b',
    r'\bFULLY_CONTAMINATED\b', r'\bUNRESOLVABLE\b', r'\bSTRESS_ONLY\b', r'\bHC-[A-Z]\d',
    r'\bOVERCLAIM\b', r'\bUNDERCLAIM\b', r'\bFORBIDDEN_OVER', r'\bFORBIDDEN_UNDER',
    r'\bADJUDICAT', r'\bSCORING_DIMENSION', r'\bWHAT_WOULD_COUNT\b',
    r'the (correct|expected|right) answer', r'\bthe trap\b', r'\bthe answer is\b',
]

# A participant file may link only inside its own directory.
LINK = re.compile(r'\]\(([^)]+)\)')
FIELD_LINE = re.compile(r'^([A-Z][A-Z0-9_]{3,})\s{2,}\S')


def check_text(text, name, schema=None):
    findings = []
    schema = schema or PERMITTED_FIELDS

    # ---- SCHEMA -------------------------------------------------------------------
    fields = [m.group(1) for m in (FIELD_LINE.match(ln) for ln in text.split('\n')) if m]
    for f in schema:
        n = fields.count(f)
        if n != 1:
            findings.append(('SCHEMA', name, '%s appears %d times, expected exactly 1' % (f, n)))
    for f in sorted(set(fields) - set(schema)):
        findings.append(('SCHEMA', name, 'field %s is not one of the %d permitted'
                         % (f, len(schema))))

    # ---- LANGUAGE -----------------------------------------------------------------
    for pat in FORBIDDEN_LANGUAGE:
        for m in re.finditer(pat, text, re.I):
            ln = text[:m.start()].count('\n') + 1
            findings.append(('LANGUAGE', name, 'L%d matches %s -> %r'
                             % (ln, pat, text[max(0, m.start() - 30):m.end() + 30].replace('\n', ' '))))
            break

    # ---- CONTAINMENT --------------------------------------------------------------
    for m in LINK.finditer(text):
        t = m.group(1)
        if t.startswith(('http://', 'https://', '#')):
            continue
        if '/' in t or t.startswith('..'):
            findings.append(('CONTAINMENT', name, 'link leaves the directory: %s' % t))

    # ---- SUFFICIENCY --------------------------------------------------------------
    # A handoff that names no source is not a safe handoff: it is an unbounded reading.
    # This catches the document-level half of "remove required source". The packet-level
    # half -- is the named file actually IN the built surface -- is not decidable here
    # and belongs to `benchmark_input_surface.py verify`.
    body = '\n'.join(text.split('\n'))
    cb = re.search(r'^CORPUS_BOUNDARY\s{2,}(.*?)(?=^[A-Z][A-Z0-9_]{3,}\s{2,}|\Z)', body, re.M | re.S)
    if not cb or not re.search(r'\b(PMID|PMC|doi|DOI)\s*\d|\bPMC\d+', cb.group(1) or ''):
        findings.append(('SUFFICIENCY', name,
                         'CORPUS_BOUNDARY names no resolvable source identifier '
                         '(PMID/PMC/DOI) — the reading would be unbounded'))
    al = re.search(r'^ALLOWED_SURFACES\s{2,}(.*?)(?=^[A-Z][A-Z0-9_]{3,}\s{2,}|\Z)', body, re.M | re.S)
    if not al or len((al.group(1) or '').strip()) < 40:
        findings.append(('SUFFICIENCY', name, 'ALLOWED_SURFACES is empty or too thin to bound a reading'))

    return findings


CONTROL = """---
audience: PARTICIPANT
---
CASE_ID              CTRL-000
QUESTION             does the control fire?
CORPUS_BOUNDARY      none
ALLOWED_SURFACES     none
EXCLUDED_SURFACES    none
STOP_CONDITION       never
EXPECTED_ANSWER      yes, and the checker must say so
See [the set](../../../../learning/somewhere/evaluator.md).
"""
CONTROL_CLASSES = {'SCHEMA', 'LANGUAGE', 'CONTAINMENT', 'SUFFICIENCY'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dir', default=DEFAULT_PARTICIPANT,
                    help='participant directory to check (default: ./participant)')
    a = ap.parse_args()
    participant = a.dir

    ctrl = check_text(CONTROL, '<positive-control>')
    classes = {c for c, _, _ in ctrl}
    if classes != CONTROL_CLASSES:
        print("VOID: positive control fired only %s — the checker cannot fail in every class"
              % (sorted(classes) or 'nothing'))
        return 2
    print("POSITIVE CONTROL fired in all %d classes (%d findings) — checker is live"
          % (len(CONTROL_CLASSES), len(ctrl)))

    if not os.path.isdir(participant):
        print("VOID: %s does not exist" % participant)
        return 2

    PARTICIPANT = participant
    files = sorted(f for f in os.listdir(PARTICIPANT) if f.endswith('.md'))
    handoffs = [f for f in files if f != 'INDEX.md']
    print("PARTICIPANT FILES: %d  (%d handoffs + index)" % (len(files), len(handoffs)))
    if not handoffs:
        print("VOID: no handoff files to check")
        return 2

    all_f = []
    for f in files:
        text = open(os.path.join(PARTICIPANT, f), encoding='utf-8').read()
        if f == 'INDEX.md':
            # the index carries no fields; it takes LANGUAGE and CONTAINMENT only
            fs = [x for x in check_text(text, f) if x[0] not in ('SCHEMA', 'SUFFICIENCY')]
        elif f.endswith('_PACKET.md'):
            # a dispatch packet names a built surface, so SUFFICIENCY's corpus-boundary
            # test does not apply; the surface hash is what bounds the reading, and the
            # SCHEMA check above requires it to be present exactly once.
            fs = [x for x in check_text(text, f, PACKET_FIELDS) if x[0] != 'SUFFICIENCY']
        else:
            fs = check_text(text, f)
        all_f += fs

    if not all_f:
        print("\nVERDICT: PASS — %d files, 0 findings" % len(files))
        return 0
    print("\nVERDICT: FAIL — %d finding(s)" % len(all_f))
    for cls, name, msg in all_f:
        print("  [%-11s] %-20s %s" % (cls, name, msg))
    return 1


if __name__ == '__main__':
    sys.exit(main())
