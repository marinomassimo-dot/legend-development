#!/usr/bin/env python3
"""READER ELIGIBILITY, in four classes that are NEVER summed.

    SURFACE_CLEAN     the files in front of the reader
    REPOSITORY_CLEAN  the object store, the ancestry, the recorded identity
    SESSION_CLEAN     what the RUNTIME hands the actor before it opens anything
    MEMORY_CLEAN      what the actor already knows

They are separated because they are provable to different degrees, and a single
"eligible" verdict launders the weakest one behind the strongest. The first two are
decided by commands and are now decided by two of them. The third is PARTIALLY decidable —
this file decides the part that is. The fourth is decidable by NO command, and this file
will never print PASS for it.

🔴 What SESSION_CLEAN found, and why it is the class that matters now.

A built surface removes the repository. It does not remove the harness the reader runs
inside. Measured in this checkout:

    .claude/skills/          21 skills, named legend-*, including legend-aso-designer and
                             legend-proband-priority-matrix
    .claude/agents/          wwox-scout.md, legend-deepdive.md, fulltext-dossier.md
    project memory           MEMORY.md, auto-loaded into context EVERY session; 46 files,
                             25 of which name the gene or the project

An actor started in this project is told the gene, the pipeline and the therapeutic
programme in its system prompt, before its first tool call. No allowlist reaches that. It
is not removed by building a surface, because it was never on the surface.

The consequence is a requirement, not a caveat: a fresh reader must be launched from a
working directory whose upward walk reaches no `.claude`, and with no project memory
bound to it. That is a property of the LAUNCH, and this file measures it at the launch
directory rather than trusting a promise about it.

    python3 learning/scientist/evalset/reader_eligibility_classes.py --cwd <surface> \
        [--surface <dir> --manifest <m.json> --case <c.json>]

Exit 0 every DECIDABLE class passes · 1 a decidable class fails · 2 inputs missing.
Exit 0 NEVER means the reader is eligible. It means nothing decidable is known against it.
"""
import argparse, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
BR = os.path.join(REPO, 'framework/eval/benchmarks/blind_rounds')

# What an agent runtime discovers by walking UPWARD from its working directory, or loads
# from a per-project store keyed by a path. Each is a channel that carries instructions or
# knowledge the allowlist never saw.
RUNTIME_DISCOVERED = ('CLAUDE.md', 'AGENTS.md', '.claude', '.cursorrules', 'GEMINI.md',
                      '.github', '.git')
MEMORY_ROOT = os.path.expanduser('~/.claude/projects')


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def surface_clean(surface, manifest, case):
    if not (surface and manifest and case):
        return None, ['not evaluated: --surface/--manifest/--case not supplied']
    rc, out = run([sys.executable, os.path.join(BR, 'check_blind_surface.py'),
                   '--surface', surface, '--manifest', manifest, '--case', case])
    notes = [l.strip() for l in out.split('\n') if l.startswith('  [')][:6]
    return (rc == 0), (notes or ['allowlist, digests, derivation, language, filenames, answer'])


def repository_clean(surface, manifest, case):
    if not (surface and manifest and case):
        return None, ['not evaluated: --surface/--manifest/--case not supplied']
    rc, out = run([sys.executable, os.path.join(BR, 'surface_properties.py'),
                   '--surface', surface, '--manifest', manifest, '--case', case])
    notes = [l.strip() for l in out.split('\n') if l.startswith('  [')][:6]
    return (rc == 0), (notes or ['ancestry, root, identity, commit metadata, object store, '
                                 'case-input approval'])


def session_clean(cwd):
    """The DECIDABLE part of SESSION_CLEAN: what a runtime launched at `cwd` would find by
    walking up, and whether a project memory store is bound to that path.

    What it CANNOT decide, and says so: the actor's system prompt, its tool roster, its
    additional working directories, and anything a prior turn of the same conversation put
    in its context. Those are properties of the launch, not of the filesystem."""
    findings, undecidable = [], []
    cwd = os.path.abspath(cwd)

    # 🔴 Scoped STRICTLY ABOVE the launch directory. The first run of this check flagged the
    # surface's own CLAUDE.md and its own .git — both required, both allowlisted, both
    # decided by SURFACE_CLEAN against the build manifest. A check that fires on the thing
    # it exists to protect is the same defect as last session's builder refusing a clean
    # paper for citing the wrong author, one tool over: the population was drawn wider than
    # the property.
    p = os.path.dirname(cwd)
    while True:
        for name in RUNTIME_DISCOVERED:
            fp = os.path.join(p, name)
            if os.path.exists(fp):
                findings.append('%s at %s — discovered by walking upward from the launch dir'
                                % (name, p))
        nxt = os.path.dirname(p)
        if nxt == p:
            break
        p = nxt

    # A project memory store is keyed by the project path with '/' replaced by '-'.
    #
    # 🔴 DECODED first, and the decode is ambiguous: `-Users-⟨op⟩-Desktop-legend-public`
    # decodes to `<HOME>/Desktop/legend/public`, because the project directory name
    # contains a hyphen of its own. The probe therefore matched nothing and printed
    # "no project memory store bound to it" for a checkout that has 46 of them. A check that
    # cannot fire is worse than no check: it reports the absence it was unable to look for.
    #
    # ENCODE instead. '/' -> '-' is total; '-' -> '/' is not.
    if os.path.isdir(MEMORY_ROOT):
        entries = set(os.listdir(MEMORY_ROOT))
        probe, seen = cwd, []
        while True:
            seen.append(probe)
            key = probe.replace('/', '-')
            mem = os.path.join(MEMORY_ROOT, key, 'memory')
            if key in entries and os.path.isdir(mem):
                n = len([f for f in os.listdir(mem) if f.endswith('.md')])
                idx = os.path.join(mem, 'MEMORY.md')
                findings.append('project memory bound to %s: %d file(s)%s'
                                % (probe, n,
                                   ', MEMORY.md auto-loaded into context EVERY session'
                                   if os.path.exists(idx) else ''))
            nxt = os.path.dirname(probe)
            if nxt == probe:
                break
            probe = nxt

    undecidable = [
        'the actor\'s system prompt — a skill or agent roster naming the gene contaminates '
        'before the first tool call, and no filesystem check sees it',
        'the actor\'s tool roster — a literature search tool makes the packet boundary '
        'advisory rather than enforced',
        'additional working directories granted by the harness',
        'anything an earlier turn of the same conversation placed in context',
    ]
    return (not findings), findings, undecidable


def memory_clean():
    """There is no command. This returns None forever, on purpose.

    The only route to MEMORY_CLEAN is CONSTRUCTION: an actor identity with no prior session
    against this material. It is established by how the reader is created, and asserted by
    whoever created it — never measured here, and never inferred from the absence of
    evidence that the actor read something."""
    return None, [
        'no command inspects what an actor has already read',
        'ESTABLISHED BY CONSTRUCTION ONLY: a reader with no prior session against this '
        'material, attested by whoever created it',
        'NOT established by: a clean surface, a clean repository, a clean launch directory, '
        'or the absence of evidence of prior exposure',
    ]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cwd', required=True, help='the directory the reader would be launched in')
    ap.add_argument('--surface')
    ap.add_argument('--manifest')
    ap.add_argument('--case')
    a = ap.parse_args()

    print("READER ELIGIBILITY — four classes, never summed")
    print("launch dir  %s" % os.path.abspath(a.cwd))
    print("=" * 92)

    rc = 0
    sc, sn = surface_clean(a.surface, a.manifest, a.case)
    rp, rn = repository_clean(a.surface, a.manifest, a.case)
    se, sf, su = session_clean(a.cwd)
    mc, mn = memory_clean()

    def emit(name, ok, notes, decidable=True):
        if ok is None:
            v = 'NOT EVALUATED' if decidable else 'UNPROVABLE'
        else:
            v = 'PASS' if ok else 'FAIL'
        print()
        print("%-18s %s" % (name, v))
        for n in notes:
            print("    · %s" % n)
        return ok is False

    rc |= emit('SURFACE_CLEAN', sc, sn)
    rc |= emit('REPOSITORY_CLEAN', rp, rn)
    rc |= emit('SESSION_CLEAN', se,
               sf or ['no runtime instruction surface above the launch directory',
                      'no project memory store bound to it'])
    print("    — undecidable by any filesystem check, and therefore REQUIREMENTS on the launch:")
    for u in su:
        print("        · %s" % u)
    emit('MEMORY_CLEAN', mc, mn, decidable=False)

    print()
    print("=" * 92)
    decided = [x for x in (sc, rp, se) if x is not None]
    print("DECIDABLE CLASSES PASSING   %d of %d" % (sum(1 for x in decided if x), len(decided)))
    print("MEMORY_CLEAN                UNPROVABLE — by construction only, never measured")
    print()
    print("🔴 Exit 0 does not mean the reader is eligible. It means nothing DECIDABLE is")
    print("   known against it, while the class that disqualified every actor in this")
    print("   laboratory remains the one no command can read.")
    return 1 if rc else 0


if __name__ == '__main__':
    sys.exit(main())
