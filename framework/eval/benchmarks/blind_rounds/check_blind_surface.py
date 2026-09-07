#!/usr/bin/env python3
"""LEAKAGE CHECKER for a built blind surface.

Different from `check_participant_surface.py`, which gates handoff DOCUMENTS. This gates a
built SURFACE, and the difference matters: `framework/eval/failure_taxonomy.md` is a
taxonomy of overclaims and legitimately contains the word. A blanket language scan over a
surface fires on the very files that define the discipline.

So the checks are scoped by how a file got there:

  INHERITED (discipline, mode directive)  -> checked by IDENTITY. Byte-identical to the
        canonical file recorded in the build manifest, or it is a finding. No language scan:
        its vocabulary is the rulebook.
  DERIVED (instructions, output schema)   -> IDENTITY against the manifest's dest_hash,
        plus a scan for the identifiers of the paper it was derived FROM.
  AUTHORED (assignment)                   -> full LANGUAGE scan.
  PACKET (publisher bytes)                -> IDENTITY only. It is the source; it is SUPPOSED
        to contain the evidence, so scanning it for the case's answer is incoherent.
  ANYTHING ELSE                           -> unallowlisted. A finding, always.

Plus, over the surface as a whole:
  HISTORY      no remotes, no alternates, one local branch, and `git show main:<path>` fails
  FILENAMES    no path component that states a conclusion
  ANSWER       the case's answer patterns, scanned everywhere EXCEPT the packet

    python3 framework/eval/benchmarks/blind_rounds/check_blind_surface.py \
        --surface <dir> --manifest <build_manifest.json> [--case <case.json>]

Exit 0 clean · 1 findings · 2 void (control failed / inputs missing).
"""
import argparse, hashlib, json, os, re, subprocess, sys

TEXT_SUFFIXES = ('.md', '.txt', '.json', '.py', '.yaml', '.yml', '.jsonl')

LANGUAGE = [
    r'\bEXPECTED_ANSWER\b', r'\bEXPECTED_VERDICT\b', r'\bEXPECTED_EPISTEMIC',
    r'\bEXPECTED_OBSERVATION', r'\bEXPECTED_CORRECT', r'\bGOLD[_ ]?(LABEL|STANDARD|SPEC|ELIGIBLE)\b',
    r'\bGOLD-\d', r'\bWHY_DIFFICULT\b', r'\bCOMMON_FAILURE\b', r'\bNEGATIVE_CONTROL\b',
    r'\bBENCHMARK_VALUE\b', r'\bBENCHMARK_CLASS\b', r'\bCONTAMINATION_STATUS\b',
    r'\bCLEAN_BLIND\b', r'\bPARTIALLY_CONTAMINATED\b', r'\bFULLY_CONTAMINATED\b',
    r'\bHC-[A-Z]\d', r'\bWHAT_WOULD_COUNT\b', r'\bFORBIDDEN_OVER', r'\bFORBIDDEN_UNDER',
    r'\bSCORING_DIMENSION', r'the (correct|expected|right) answer', r'\bthe answer is\b',
]
# Adjudication FIELD names, as they appear in this repository's records.
ADJ_FIELDS = [
    r'"verbatim_locators"', r'"propositions"', r'"adjudicates"', r'"evidence_basis"',
    r'"needles"', r'\bREAD FROM THE IMAGE\b', r'"claim_links"', r'"invalidates_receipt"',
    r'\bFTR-\d{8}-\d{7,8}-\d\b', r'"why_this_article_is_adjudicated"',
]
INTERPRETIVE_NAME = re.compile(
    r'rationale|refut|contradict|unsupported|overclaim|defect|wrong|missing|empty|proof|'
    r'proves|indispensable|responsible|unfavou?rable|asymmetry|invisible|significance|'
    r'never|absent|generalis', re.I)


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(65536), b''):
            h.update(b)
    return h.hexdigest()


def walk(surface):
    for root, dirs, files in os.walk(surface):
        dirs[:] = [d for d in dirs if d != '.git']
        for f in sorted(files):
            fp = os.path.join(root, f)
            yield os.path.relpath(fp, surface), fp


def read_text(fp):
    try:
        return open(fp, encoding='utf-8').read()
    except (UnicodeDecodeError, OSError):
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--surface', required=True)
    ap.add_argument('--manifest', required=True)
    ap.add_argument('--case')
    ap.add_argument('--answer-pattern', action='append', default=[])
    a = ap.parse_args()

    if not os.path.isdir(a.surface):
        print("VOID: surface not found: %s" % a.surface); return 2
    man = json.load(open(a.manifest, encoding='utf-8'))
    entries = {e['destination_neutral_name']: e for e in man['entries']}

    # ---- control: the checker must be able to fail -----------------------------------
    ctrl = [p for p in LANGUAGE if re.search(p, 'EXPECTED_VERDICT: the title is unsupported')]
    ctrl2 = [p for p in ADJ_FIELDS if re.search(p, '{"evidence_basis": ["..."]}')]
    ctrl3 = INTERPRETIVE_NAME.search('p03_CT_indispensable_no_structure.png')
    if not (ctrl and ctrl2 and ctrl3):
        print("VOID: one of the three pattern families cannot match its own control"); return 2
    print("CONTROL  language/%d adj/%d filename/%s — all three families live"
          % (len(ctrl), len(ctrl2), 'ok' if ctrl3 else 'DEAD'))

    findings = []
    kind_of = {k: e.get('kind') for k, e in entries.items()}
    packet_kinds = {'article_binary', 'article_text', 'supplement'}
    inherited_kinds = {'discipline', 'mode_directive'}

    present = []
    for rel, fp in walk(a.surface):
        present.append(rel)
        e = entries.get(rel)
        if e is None:
            findings.append(('UNALLOWLISTED', rel, 'present in the surface, absent from the build manifest'))
            continue
        if e.get('dest_hash') and sha256(fp) != e['dest_hash']:
            findings.append(('DIGEST', rel, 'bytes differ from the build manifest'))

    for rel in entries:
        if rel not in present:
            findings.append(('MISSING', rel, 'in the build manifest, absent from the surface'))

    # ---- DERIVATION: re-render what the build authored, and compare -------------------
    # 🔴 A digest check proves a file has not changed SINCE the build. It proves nothing
    # about the build. Measured: a paraphrased answer written into ASSIGNMENT.md at build
    # time, with the manifest regenerated to match, passed every other check in this file.
    # The repair is not a wider word list — it is that the one authored file must be
    # reproducible from (template + case spec), so any sentence that is not in the template
    # fails regardless of how it is phrased.
    if a.case:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        try:
            from build_blind_surface import AUTHORED
        except ImportError:
            findings.append(('DERIVATION', '*',
                             'cannot import the renderers — derivation not checkable'))
            AUTHORED = None
        if AUTHORED is not None:
            # Every file authored at build time, not just the assignment. A renderer added
            # to AUTHORED is checked here without an edit; an authored file left OFF that
            # list is unchecked by construction, which is the failure mode this loop exists
            # to make impossible to reach by omission.
            spec = json.load(open(a.case, encoding='utf-8'))
            for rel, renderer in AUTHORED:
                want = renderer(spec)
                got_p = os.path.join(a.surface, rel)
                got = read_text(got_p) if os.path.exists(got_p) else None
                if got is None:
                    findings.append(('DERIVATION', rel, 'absent'))
                elif got != want:
                    findings.append(('DERIVATION', rel,
                                     'does not re-render from (template + case spec); %+d bytes'
                                     % (len(got) - len(want))))
    else:
        findings.append(('DERIVATION', '*',
                         '--case not supplied: the build-time-authored files were NOT '
                         're-derived, and a digest check cannot substitute'))

    # ---- language / adjudication-field scan, scoped by origin -------------------------
    for rel, fp in walk(a.surface):
        kind = kind_of.get(rel)
        if kind in packet_kinds or kind in inherited_kinds:
            continue          # identity-checked above; scanning them is incoherent
        if not rel.endswith(TEXT_SUFFIXES):
            continue
        t = read_text(fp)
        if t is None:
            continue
        for pat in LANGUAGE:
            m = re.search(pat, t, re.I)
            if m:
                findings.append(('LANGUAGE', rel, '%s -> %r' % (pat, t[max(0, m.start()-30):m.end()+40].replace('\n', ' '))))
                break
        for pat in ADJ_FIELDS:
            m = re.search(pat, t)
            if m:
                findings.append(('ADJ_FIELD', rel, '%s -> %r' % (pat, t[max(0, m.start()-30):m.end()+40].replace('\n', ' '))))
                break

    # ---- answer scan: everywhere EXCEPT the packet ------------------------------------
    answer_pats = list(a.answer_pattern)
    if a.case:
        c = json.load(open(a.case, encoding='utf-8'))
        answer_pats += c.get('answer_patterns', [])
    for rel, fp in walk(a.surface):
        if kind_of.get(rel) in packet_kinds:
            continue
        if not rel.endswith(TEXT_SUFFIXES):
            continue
        t = read_text(fp)
        if t is None:
            continue
        for pat in answer_pats:
            m = re.search(pat, t, re.I)
            if m:
                findings.append(('ANSWER', rel, '%s -> %r' % (pat, t[max(0, m.start()-30):m.end()+40])))

    # ---- filenames ---------------------------------------------------------------------
    for rel, _ in walk(a.surface):
        for part in rel.split(os.sep):
            if INTERPRETIVE_NAME.search(part) and kind_of.get(rel) not in inherited_kinds:
                findings.append(('FILENAME', rel, 'path component %r reads as a conclusion' % part))
                break

    # ---- history ------------------------------------------------------------------------
    def git(*args):
        return subprocess.run(('git',) + args, cwd=a.surface, capture_output=True, text=True)

    if not os.path.isdir(os.path.join(a.surface, '.git')):
        findings.append(('HISTORY', '.git', 'no repository: the reader cannot meet its WORK_COMMIT obligation'))
    else:
        r = git('remote', '-v')
        if r.stdout.strip():
            findings.append(('HISTORY', '.git', 'remotes configured: %r' % r.stdout.strip()[:120]))
        alt = os.path.join(a.surface, '.git', 'objects', 'info', 'alternates')
        if os.path.exists(alt):
            findings.append(('HISTORY', '.git', 'objects/info/alternates present — borrows another object store'))
        branches = [b.strip(' *') for b in git('branch').stdout.split('\n') if b.strip()]
        if len(branches) != 1:
            findings.append(('HISTORY', '.git', 'expected exactly one branch, found %r' % branches))
        for ref in ('main', 'master', 'lettore', 'lettore-b', 'lettore-c'):
            if git('rev-parse', '--verify', '-q', ref).returncode == 0:
                findings.append(('HISTORY', '.git', 'ref %r resolves inside the surface' % ref))
        n = git('rev-list', '--all', '--count').stdout.strip()
        if n and int(n or 0) > 3:
            findings.append(('HISTORY', '.git', '%s commits — a built surface should carry its own, few' % n))

    print("SURFACE  %s" % a.surface)
    print("files    %d present · %d in manifest" % (len(present), len(entries)))
    print("tree     %s" % man.get('surface_tree_sha256'))
    print()
    if not findings:
        print("VERDICT: PASS — 0 findings")
        return 0
    print("VERDICT: FAIL — %d finding(s)" % len(findings))
    for cls, rel, msg in findings[:40]:
        print("  [%-13s] %-46s %s" % (cls, rel, msg[:110]))
    return 1


if __name__ == '__main__':
    sys.exit(main())
