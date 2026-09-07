#!/usr/bin/env python3
"""BUILD A BLIND SURFACE — a standalone repository, from nothing, outside every checkout.

Measured, this session: an orphan-branch worktree of this repository resolves
`git show main:<receipt>` and lists 915 commits and 65 branches. A branch of any shape
shares an object store, so `NO_REPOSITORY_HISTORY` cannot be met by a branch. The surface
is a fresh `git init` in a directory that is not inside any checkout and shares no objects
with one -- which is what controlled_benchmark_ab.md 2.2 already prescribes.

    python3 framework/eval/benchmarks/blind_rounds/build_blind_surface.py \
        --case framework/eval/benchmarks/blind_rounds/cases/BLIND-FR-001.case.json \
        --dest /some/neutral/root/BLIND-FR-001 \
        --corpus-root <REPO_ROOT>/files/fulltext

Two of the thirteen inherited participant files are paper-specific to BENCH-AB-001's own
paper (BENCHMARK_INSTRUCTIONS.md x12, OUTPUT_SCHEMA.md x6). They are DERIVED by a declared
substitution table rather than re-authored, so the derivation is auditable and cannot
drift from the canonical text: both digests go in the build manifest and the result is
re-scanned for the old paper's identifiers.

The build manifest is written OUTSIDE the surface. It names repository paths, and a
repository path is history.

EVALUATOR TOOL. Building a prototype authorizes no run and hands nothing to anyone.
"""
import argparse, hashlib, json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))

VERBATIM = [
    ('framework/eval/benchmarks/BENCH-AB-001/instructions/SURFACE_CLAUDE.md', 'CLAUDE.md'),
    ('roles/scientist.md', 'roles/scientist.md'),
    ('framework/instruction/epistemic_discipline.md', 'framework/instruction/epistemic_discipline.md'),
    ('framework/master/gold_is_in_the_details.md', 'framework/master/gold_is_in_the_details.md'),
    ('framework/protocols/fulltext_read_receipt.md', 'framework/protocols/fulltext_read_receipt.md'),
    ('framework/protocols/scientist_reading_modes.md', 'framework/protocols/scientist_reading_modes.md'),
    ('framework/eval/failure_taxonomy.md', 'framework/eval/failure_taxonomy.md'),
    ('framework/scripts/deepdive_manifest.py', 'framework/scripts/deepdive_manifest.py'),
    ('framework/scripts/corpus_firewall.py', 'framework/scripts/corpus_firewall.py'),
]
TEMPLATED = [
    ('framework/eval/benchmarks/BENCH-AB-001/instructions/BENCHMARK_INSTRUCTIONS.md',
     'benchmark/BENCHMARK_INSTRUCTIONS.md'),
    ('framework/eval/benchmarks/BENCH-AB-001/instructions/OUTPUT_SCHEMA.md',
     'benchmark/OUTPUT_SCHEMA.md'),
]
MODE = ('framework/eval/benchmarks/BENCH-AB-001/instructions/MODE_A.md', 'benchmark/MODE_DIRECTIVE.md')
OUTPUT_SLOTS = ['output/', 'output/renders/']

# Identifiers of BENCH-AB-001's own paper. After templating, the surface is re-scanned for
# these and a single hit fails the build.
OLD_PAPER = re.compile(r'42397075|awag239|Aqeilan2026|brain-2025-03809|Steinberg|Zonca|Abdellatif')


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(65536), b''):
            h.update(b)
    return h.hexdigest()


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def assert_outside_every_checkout(dest):
    """dest must not be inside any git working tree, and must not be under REPO."""
    real = os.path.realpath(dest)
    if real.startswith(os.path.realpath(REPO) + os.sep) or real == os.path.realpath(REPO):
        sys.exit("REFUSED: destination is inside the LEGEND repository: %s" % real)
    p = os.path.dirname(real)
    while True:
        if os.path.exists(os.path.join(p, '.git')):
            sys.exit("REFUSED: an ancestor of the destination is a git working tree: %s" % p)
        if os.path.exists(os.path.join(p, 'CLAUDE.md')) or os.path.isdir(os.path.join(p, '.claude')):
            sys.exit("REFUSED: an ancestor carries CLAUDE.md/.claude, which is discovered upward: %s" % p)
        nxt = os.path.dirname(p)
        if nxt == p:
            break
        p = nxt


ASSIGNMENT_TEMPLATE = (
    "---\nartifact: {case_id} — assignment\ncase_id: {case_id}\n---\n\n"
    "# ASSIGNMENT — `{case_id}`\n\n"
    "```\nCASE_ID               {case_id}\n"
    "ROLE                  scientist    contract: roles/scientist.md\n"
    "MODE                  see benchmark/MODE_DIRECTIVE.md\n"
    "INTERACTION_MODE      AUTONOMOUS_COMPLETE  do not ask questions to proceed\n"
    "WORKING SURFACE       this directory — its own git repository, its own branch\n```\n\n"
    "## QUESTION\n\n{question}\n\n"
    "## ALLOWED_FILES\n\nEverything in this directory, and nothing outside it. The packet is:\n\n"
    "```\n{packet}\n```\n\n"
    "Render what you need from those files into `output/renders/` and declare every render "
    "with its SHA-256. A caption is not a panel.\n\n"
    "## EXCLUDED_SURFACES\n\n"
    "DO_NOT_OPEN anything outside this directory: no other checkout, no registry, ledger, "
    "receipt, manifest or dossier, no other reader's work, no open web, no PubMed. "
    "If you open one by accident, do not discard the reading — record what you opened, "
    "when, and what you saw, and continue.\n\n"
    "## STOP_CONDITION\n\n{stop}\n\n"
    "For every question in this benchmark, one admissible outcome is that the published "
    "record does not decide it. If you reach that, say so and name the exact object that "
    "would decide it. This paragraph is byte-identical in every assignment and tells you "
    "nothing about this case.\n\n"
    "When you declare completion your reading is frozen immediately, before its content is "
    "read by anyone.\n\n> **Nothing here is medical advice.**\n")


def render_assignment(case):
    """🔴 The assignment is the ONLY file authored at build time, which makes it the only
    place a build-time leak can be introduced without tripping a digest check. Measured:
    a paraphrased sentence carrying the answer, with no case identifier and no
    expectation-bearing token, passed the language and answer scans and matched the
    manifest because the manifest was written after it.

    So it is RENDERED, not written: template plus three fields from the case spec, and the
    checker re-renders and compares byte-for-byte. Any extra sentence fails, whatever its
    wording, because it is not in the template. Identity catches what pattern cannot."""
    return ASSIGNMENT_TEMPLATE.format(
        case_id=case['case_id'], question=case['question'],
        packet='\n'.join(r['dest'] for r in case['packet']), stop=case['stop_condition'])


# The declaration is BYTE-IDENTICAL for every case, and that is a design constraint, not a
# convenience. The obvious version would state what this case excluded and why -- the case
# specs record, for instance, eight prior-reader renders dropped for encoding a prior
# reader's attention. But the COUNT is itself a proxy for that attention: a paper with eight
# excluded renders was worked harder than one with four, and a reader who is told the number
# learns something about the case from a file that exists to protect it. Uniform text cannot
# carry a per-case signal.
CONTAMINATION_DECLARATION = """\
---
artifact: contamination declaration
---

# CONTAMINATION DECLARATION

This paragraph is byte-identical in every assignment of this benchmark. It states what
was done to the surface you are reading, in general terms that are the same for every
case, and it tells you nothing about this one.

## What this surface is

A directory built by allowlist: every file in it is listed in a build manifest held
outside it, and every file listed is present. It is its own git repository, with one
commit, one branch, no remote, no borrowed object store, and an explicit neutral identity.
It descends from no other repository and can reach no other repository's objects.

## What was removed

Artifacts produced by earlier readers of this material were excluded, whether or not they
stated a conclusion — including renders of the source, because *which* pages someone chose
to render, and at what resolution, encodes where their attention went. Records that
adjudicate this material were excluded. Filenames that state a conclusion were excluded.
The number of items in each of those categories is not stated here, because the number is
itself a fact about this case.

## What could not be removed

Three things are outside the reach of any surface, and you should know they were not
solved by building one:

1. **Whatever you already know.** No check inspects it. If you recognise this material,
   say so in your output — that is a finding about the benchmark, not a failure by you.
2. **Whatever your runtime told you before you opened this directory.** A tool roster, a
   skill list or a memory store can name the subject matter before your first tool call.
3. **The identifiers in your packet.** The source is named by its published identifiers.
   If you have a tool that reaches the open web, the boundary in your assignment is a rule
   you are asked to keep, not a wall that keeps you.

## What you owe

If you cross the boundary, by accident or by tool, do not discard the reading. Record what
you opened, when, and what you saw, and continue. A declared crossing is data. An
undeclared one is the only thing here that cannot be repaired.

> **Nothing here is medical advice.**
"""


def render_contamination_declaration(case):
    """Takes `case` and ignores it, by design — see the constant above. The signature
    matches the other renderers so the checker can re-derive all three the same way."""
    return CONTAMINATION_DECLARATION


def render_provenance(case):
    """Participant-safe provenance: WHITELISTED structural fields only.

    What is emitted: the destination name, the digest of the bytes as placed, the kind, and
    a uniform assertion per kind. What is NOT emitted: the corpus filename (it carries the
    first author and year), the case's `why_required` and `no_adjudication_assertion` prose
    (both authored per case, so both can leak), and anything derived from an adjudication.

    These packets are attention-free because they contain whole published objects only —
    a complete article, a complete deposit, a mechanical whole-document extraction. A packet
    containing a CROP would not be: a crop rectangle states where a prior reader looked,
    more precisely than the renders the case specs already exclude for exactly that reason.
    If a crop ever enters a packet, this renderer must refuse it rather than describe it."""
    kinds = {'article_binary': 'publisher bytes, unmodified',
             'article_text': 'text surface, unmodified; no LEGEND actor has written into it',
             'supplement': 'publisher bytes of a published deposit, unmodified'}
    rows = []
    for r in case['packet']:
        if r['kind'] not in kinds:
            raise SystemExit("REFUSED: packet kind %r has no uniform provenance assertion; "
                             "describing it per case would leak the description" % r['kind'])
        rows.append({'name': r['dest'], 'kind': r['kind'], 'assertion': kinds[r['kind']]})
    return json.dumps({
        '_what': 'provenance of the packet, by whitelist',
        '_uniform': 'field names and assertions are identical for every case of this '
                    'benchmark; only the packet contents differ',
        'case_id': case['case_id'],
        'sources': rows,
        'digests': 'each file\'s SHA-256 is recorded in the build manifest held outside '
                   'this surface; compute them yourself and declare what you computed',
    }, indent=1, sort_keys=True) + '\n'


# Every file AUTHORED at build time, with the renderer that must reproduce it byte-for-byte.
# A digest proves a file has not changed SINCE the build; only re-rendering says anything
# about the build. Any authored file not on this list is unchecked by construction.
AUTHORED = [
    ('ASSIGNMENT.md', render_assignment),
    ('PROVENANCE.json', render_provenance),
    ('CONTAMINATION_DECLARATION.md', render_contamination_declaration),
]


def template(text, case, packet_rows):
    """Declared substitution table. Every rule is listed in the returned record."""
    rules = []

    def sub(pattern, repl, why, flags=0):
        nonlocal text
        new, n = re.subn(pattern, repl, text, flags=flags)
        rules.append({'pattern': pattern, 'replacement': repl, 'applied': n, 'why': why})
        text = new

    pmid = case['pmids'][0]
    lines = []
    for r in packet_rows:
        lines.append('%-56s %s' % (r['dest'], r['why_required'].split(';')[0]))
    packet_block = ('```\nPMID %s · doi %s\n\n%s\n```' % (pmid, case['doi'], '\n'.join(lines)))

    sub(r'```\nPMID 42397075[\s\S]*?\n```', packet_block.replace('\\', '\\\\'),
        'the paper-and-packet block in section 1 is the case, and is replaced whole')
    sub(r'PMID42397075', 'PMID%s' % pmid, 'output paths are derived from the PMID by the validator')
    sub(r'10\.1093/brain/awag239', case['doi'], 'the doi field of the work manifest')
    sub(r'42397075', pmid, 'any remaining bare identifier')
    sub(r'BENCH-AB-001', case['case_id'], 'the benchmark id this surface belongs to')
    sub(r'identical_for: scientist-a, scientist-b', 'identical_for: every reader of this case',
        'this surface is built for one reader, not a pair')
    return text, rules


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--case', required=True)
    ap.add_argument('--dest', required=True)
    ap.add_argument('--corpus-root', default='<REPO_ROOT>/files/fulltext')
    ap.add_argument('--manifest-out', required=True)
    ap.add_argument('--force', action='store_true')
    a = ap.parse_args()

    case = json.load(open(a.case, encoding='utf-8'))
    dest = os.path.abspath(a.dest)
    assert_outside_every_checkout(dest)
    if os.path.exists(dest):
        if not a.force:
            sys.exit("REFUSED: %s exists (use --force to rebuild from scratch)" % dest)
        shutil.rmtree(dest)
    os.makedirs(dest)

    entries = []

    def place(src_abs, rel, kind, why, assertion, origin):
        d = os.path.join(dest, rel)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        shutil.copyfile(src_abs, d)
        entries.append({'source_object': origin, 'source_hash': sha256(src_abs),
                        'destination_neutral_name': rel, 'kind': kind,
                        'why_required': why, 'no_adjudication_assertion': assertion,
                        'dest_hash': sha256(d)})

    # 1 · the packet
    for r in case['packet']:
        src = os.path.join(a.corpus_root, r['source'])
        if not os.path.exists(src):
            sys.exit("REFUSED: packet source absent: %s" % src)
        place(src, r['dest'], r['kind'], r['why_required'], r['no_adjudication_assertion'],
              'corpus:' + r['source'])

    # 2 · the inherited participant files, copied verbatim
    for src_rel, rel in VERBATIM:
        place(os.path.join(REPO, src_rel), rel, 'discipline',
              'defines the output the reading is graded against',
              'canonical framework text; measured 0 hits for this case’s identifiers '
              'except where declared_residuals says otherwise', 'repo:' + src_rel)

    # 3 · the mode directive
    place(os.path.join(REPO, MODE[0]), MODE[1], 'mode_directive',
          'the reading mode addressed to this reader', 'canonical protocol text', 'repo:' + MODE[0])

    # 4 · the two paper-specific files, DERIVED
    derivations = []
    for src_rel, rel in TEMPLATED:
        raw = open(os.path.join(REPO, src_rel), encoding='utf-8').read()
        out, rules = template(raw, case, case['packet'])
        d = os.path.join(dest, rel)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        open(d, 'w', encoding='utf-8').write(out)
        derivations.append({'source_object': 'repo:' + src_rel,
                            'source_hash': sha256_bytes(raw.encode()),
                            'destination_neutral_name': rel,
                            'dest_hash': sha256_bytes(out.encode()),
                            'substitutions': rules})
        entries.append({'source_object': 'repo:' + src_rel, 'source_hash': sha256_bytes(raw.encode()),
                        'destination_neutral_name': rel, 'kind': 'instructions_derived',
                        'why_required': 'the common instructions and the output schema, '
                                        'retargeted to this case by declared substitution',
                        'no_adjudication_assertion': 'derived from canonical text by the '
                                                     'substitution table in this manifest; '
                                                     're-scanned for the source paper’s identifiers',
                        'dest_hash': sha256_bytes(out.encode())})

    # 5 · the participant-facing files AUTHORED for this build — every one RENDERED from
    #     (template + case spec), never written, so the checker can re-derive each and any
    #     sentence that is not in a template fails whatever its wording.
    AUTHORED_WHY = {
        'ASSIGNMENT.md': ('assignment', 'identity, question, boundary, stop condition',
                          'six participant fields only; no verdict, no gold, no difficulty, '
                          'no classification'),
        'PROVENANCE.json': ('provenance', 'what each packet file is and what was done to it',
                            'whitelisted structural fields and per-kind uniform assertions; '
                            'no corpus filename, no per-case prose, nothing derived from an '
                            'adjudication'),
        'CONTAMINATION_DECLARATION.md': ('declaration',
                                         'what was removed, what could not be, what the '
                                         'reader owes on crossing the boundary',
                                         'byte-identical for every case, so it cannot carry '
                                         'a per-case signal'),
    }
    for rel, renderer in AUTHORED:
        p = os.path.join(dest, rel)
        open(p, 'w', encoding='utf-8').write(renderer(case))
        kind, why, assertion = AUTHORED_WHY[rel]
        entries.append({'source_object': 'authored:this build', 'source_hash': None,
                        'destination_neutral_name': rel, 'kind': kind,
                        'why_required': why, 'no_adjudication_assertion': assertion,
                        'dest_hash': sha256(p)})

    for slot in OUTPUT_SLOTS:
        os.makedirs(os.path.join(dest, slot), exist_ok=True)
    os.makedirs(os.path.join(dest, 'disease-models/wwox/research/deepdive_manifests'), exist_ok=True)
    os.makedirs(os.path.join(dest, 'disease-models/wwox/research/fulltext_dossiers'), exist_ok=True)

    # 6 · standalone repository, explicit identity, no remote
    def git(*args):
        return subprocess.run(('git',) + args, cwd=dest, capture_output=True, text=True)
    git('init', '-q', '-b', 'reading')
    git('config', 'user.name', 'benchmark participant')
    git('config', 'user.email', 'participant@invalid')
    git('add', '-A')
    git('commit', '-q', '-m', 'surface as handed over')

    # 7 · the surface tree hash — sorted "path\0sha256\n" over every regular file, .git excluded
    rows = []
    for root, dirs, files in os.walk(dest):
        dirs[:] = [d for d in dirs if d != '.git']
        for f in sorted(files):
            fp = os.path.join(root, f)
            rows.append('%s\0%s\n' % (os.path.relpath(fp, dest), sha256(fp)))
    tree_hash = sha256_bytes(''.join(sorted(rows)).encode())

    # 8 · the paper-specific re-scan — over DERIVED AND AUTHORED FILES ONLY.
    #
    # 🔴 It first scanned everything, including the packet, and the second build refused:
    # PMID 42128308 is a review that cites Steinberg in its bibliography, and Steinberg is
    # an author of the paper the templates were derived from. Aqeilan is senior author of
    # half this corpus, so a whole-surface scan would have blocked most builds it was
    # written to protect. The scan exists to catch a TEMPLATING FAILURE — a derived
    # instruction file still naming the paper it came from — and a packet cannot fail that
    # way, because nobody templated it. Scanning publisher bytes for a name is the same
    # incoherence as scanning the source for the case's answer.
    scan_targets = {rel for _src, rel in TEMPLATED} | {rel for rel, _fn in AUTHORED}
    leaks = []
    for rel in sorted(scan_targets):
        fp = os.path.join(dest, rel)
        if not os.path.exists(fp):
            continue
        try:
            t = open(fp, encoding='utf-8').read()
        except (UnicodeDecodeError, OSError):
            continue
        for m in OLD_PAPER.finditer(t):
            leaks.append((rel, m.group(0)))

    manifest = {
        '_schema': 'LEGEND blind surface — build manifest v1',
        '_warning': 'EVALUATOR ONLY. It names repository paths, and a repository path is history. '
                    'It is written OUTSIDE the surface and must never be copied into one.',
        'case_id': case['case_id'], 'internal_ref': case.get('internal_ref'),
        'built_at_repo_head': subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=REPO,
                                             capture_output=True, text=True).stdout.strip(),
        'dest': dest, 'corpus_root': a.corpus_root,
        'surface_tree_sha256': tree_hash,
        'file_count': len(rows),
        'entries': entries,
        'derivations': derivations,
        'excluded': case.get('excluded', []),
        'declared_residuals': case.get('declared_residuals', []),
        'source_paper_rescan': {'pattern': OLD_PAPER.pattern, 'hits': leaks},
    }
    json.dump(manifest, open(a.manifest_out, 'w'), indent=1)

    print("SURFACE      %s" % dest)
    print("files        %d" % len(rows))
    print("tree sha256  %s" % tree_hash)
    print("manifest     %s" % a.manifest_out)
    print("source-paper rescan hits: %d %s" % (len(leaks), 'OK' if not leaks else '*** FAIL ***'))
    for rel, tok in leaks[:10]:
        print("   %s -> %s" % (rel, tok))
    return 1 if leaks else 0


if __name__ == '__main__':
    sys.exit(main())
