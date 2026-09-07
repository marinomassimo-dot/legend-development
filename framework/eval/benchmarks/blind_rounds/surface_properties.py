#!/usr/bin/env python3
"""STRUCTURAL PROPERTY BATTERY for a built blind surface.

`check_blind_surface.py` gates the FILES. This gates everything a file walk cannot see:
the object store, the recorded identity, the commit metadata, what sits ABOVE the surface,
and whether the case specification the assignment was rendered from was ever approved.

Measured this session, against the checker as it stood, on a surface that passed it with
zero findings:

    M8   answer written into the commit message           NOT CAUGHT
    M9   local git identity unset -> global identity      NOT CAUGHT
    M10  CLAUDE.md created in the surface's parent        NOT CAUGHT
    M13  answer written into the case spec's `question`   NOT CAUGHT

M13 is the deep one. The checker re-renders `ASSIGNMENT.md` from (template + case spec)
and compares byte-for-byte, which defeats a leak written into the assignment. It cannot
defeat a leak written into the SPEC, because then the leak renders faithfully and the
comparison succeeds. The same hole has a filename form: a `dest` naming the answer is
allowlisted by construction, so only the filename word-list stands in its way, and
`supplement_01_zero_kinase_signal_any_panel.pdf` passed it.

There is no pattern that decides whether a free-text question leaks. So the control is not
a pattern. The participant-facing PROJECTION of the case spec -- exactly the fields that
reach a reader, and no evaluator field -- is hashed, and the digest must appear in
`cases/approved_inputs.json`. That converts an undecidable question ("is this text clean?")
into a decidable one ("is this the text that was approved?"). It does not make the text
clean. It makes a change to it visible, which is the most a checker can honestly do.

    python3 framework/eval/benchmarks/blind_rounds/surface_properties.py \
        --surface <dir> --manifest <build_manifest.json> --case <case.json> [--dispatch-gate]

Exit 0 clean · 1 findings · 2 void (a control failed / inputs missing).

EVALUATOR TOOL. Passing authorizes no run and hands nothing to anyone.
"""
import argparse, ast, hashlib, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
APPROVALS = os.path.join(HERE, 'cases', 'approved_inputs.json')

# Files that an agent runtime discovers by walking UPWARD from its working directory. A
# surface placed under any of them inherits an instruction surface nobody allowlisted.
PARENT_INSTRUCTION_SURFACES = ('CLAUDE.md', '.claude', 'AGENTS.md', '.cursorrules',
                               'GEMINI.md', '.github', '.git')


def git(surface, *args):
    return subprocess.run(('git',) + args, cwd=surface, capture_output=True, text=True)


def literal_digest_from_source(name):
    """Read a module-level string constant out of the builder's SOURCE BYTES, never by
    importing it.

    An import can be served from a bytecode cache that does not reflect the file on disk --
    measured on this platform, see the STALE BYTECODE note below. The reference value a
    check compares against must come from the object itself."""
    try:
        tree = ast.parse(open(os.path.join(HERE, 'build_blind_surface.py'),
                              encoding='utf-8').read())
    except (OSError, SyntaxError):
        return None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(
                getattr(t, 'id', None) == name for t in node.targets):
            try:
                return hashlib.sha256(ast.literal_eval(node.value).encode('utf-8')).hexdigest()
            except ValueError:
                return None
    return None


def rendered_authored_digest(case):
    """Digest of everything AUTHORED at build time, as a reader would receive it.

    🔴 Pinning ASSIGNMENT_TEMPLATE alone was the same gap one level over. Adding
    PROVENANCE.json and CONTAMINATION_DECLARATION.md put two more participant-facing
    templates in the surface, plus the uniform strings embedded in `render_provenance`, and
    the template pin saw none of them. What must be bound is not one constant but
    everything a reader is handed: this hashes the rendered OUTPUT of every renderer in
    AUTHORED, so a change to any template, any embedded string, any renderer or the spec
    moves it.

    Reached by import, and therefore only trustworthy while the stale-bytecode control
    below passes -- which is why that control is VOID rather than FAIL."""
    sys.path.insert(0, HERE)
    try:
        from build_blind_surface import AUTHORED
    except ImportError:
        return None
    h = hashlib.sha256()
    for rel, renderer in sorted(AUTHORED):
        h.update(rel.encode('utf-8') + b'\0' + renderer(case).encode('utf-8') + b'\n')
    return h.hexdigest()


def participant_projection(case):
    """The case-spec fields that REACH A READER, and only those.

    Derived from the two renderers, not guessed:
      * `render_assignment` consumes  case_id, question, stop_condition, packet[*].dest
      * `template` consumes           pmids[0], doi, case_id,
                                      packet[*].dest, packet[*].why_required.split(';')[0]

    Everything else in a case spec is evaluator-side and may change without re-approval:
    `internal_ref` (verified absent from a built surface), `kind`,
    `no_adjudication_assertion`, `source`, `excluded`, `declared_residuals`,
    `answer_patterns`. That boundary is the point -- an approval that also covered the
    evaluator fields would expire every time a residual was recorded, and an approval
    that expires constantly stops being read.
    """
    return {
        'case_id': case['case_id'],
        'question': case['question'],
        'stop_condition': case['stop_condition'],
        'pmid': case['pmids'][0],
        'doi': case['doi'],
        'packet': [{'dest': r['dest'], 'why_required_head': r['why_required'].split(';')[0]}
                   for r in case['packet']],
    }


def projection_digest(case):
    blob = json.dumps(participant_projection(case), sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(blob.encode('utf-8')).hexdigest()


def check(surface, manifest, case_path, approvals_path=APPROVALS, dispatch_gate=False):
    findings, advisories = [], []
    surface = os.path.abspath(surface)
    case = json.load(open(case_path, encoding='utf-8'))
    apr = json.load(open(approvals_path, encoding='utf-8'))
    req = apr['required_surface_constants']

    # ---- control: the battery must be able to fail -----------------------------------
    # Each family is exercised against a value it MUST reject. A battery whose families
    # cannot fire reports PASS on everything.
    ctrl = {
        'ancestry': any(os.path.basename('/x/CLAUDE.md') == s for s in PARENT_INSTRUCTION_SURFACES),
        # 🔴 NOT a real address, and it must never become one. This control only
        # asserts that the identity family CAN FIRE, so the value carries no information
        # beyond "differs from the required one". A real person's address here is
        # published by every clone of this branch, which is what happened.
        # `@example.invalid` over a bare `@invalid` deliberately: the release gate
        # ALLOWLISTS this domain, whereas a dotless one passes only because the gate's
        # regex does not recognise it as an address at all. Passing because you are
        # permitted survives a scanner being tightened; passing because you are invisible
        # does not -- and the suite next door had exactly that bug an hour after it was
        # written.
        'identity': 'leaked-host-identity@example.invalid' != req['git_user_email'],
        'projection': projection_digest(case) != hashlib.sha256(b'').hexdigest(),
        'approval': 'no-such-case-id' not in apr['approved_cases'],
    }
    dead = [k for k, v in ctrl.items() if not v]
    if dead:
        return 2, [('VOID', '-', 'control families cannot fire: %s' % ','.join(dead))], []
    print("CONTROL  %d property families live" % len(ctrl))

    # ---- P1 · ANCESTRY -----------------------------------------------------------------
    # The BUILDER refuses such a destination. That is a build-time guard, and the parent
    # can be created after the build -- which is exactly what M10 does. So it is re-checked
    # here, at the surface, at the time the surface is gated.
    p = os.path.dirname(surface)
    while True:
        for name in PARENT_INSTRUCTION_SURFACES:
            if os.path.exists(os.path.join(p, name)):
                findings.append(('ANCESTRY', p,
                                 '%r above the surface; it is discovered by walking upward'
                                 % name))
        nxt = os.path.dirname(p)
        if nxt == p:
            break
        p = nxt

    # ---- P2 · ROOT APPROVED -------------------------------------------------------------
    root = os.path.dirname(surface)
    if root not in apr['approved_bench_roots']:
        findings.append(('ROOT', root, 'not an approved BENCH_ROOT'))
    if os.path.basename(surface) != case['case_id']:
        findings.append(('ROOT', surface, 'directory name %r != case_id %r'
                         % (os.path.basename(surface), case['case_id'])))

    # ---- P3 · PATH NEUTRALITY -----------------------------------------------------------
    # Secondary to P2 and deliberately so: P2 is identity against an approved list, this is
    # a token screen, and a token screen is the weaker instrument. It stays because the
    # failure it catches -- a surface whose own `pwd` names the repository it is blind to --
    # was a DECLARED RESIDUAL of the prototype and would otherwise be enforced by memory.
    low = surface.lower()
    for tok in apr['repository_identifying_tokens']:
        if tok.lower() in low:
            findings.append(('PATH', surface, 'path contains %r: the reader sees the '
                                              'provenance in its own working directory' % tok))

    if not os.path.isdir(os.path.join(surface, '.git')):
        findings.append(('GIT', '.git', 'no repository'))
        return (1, findings, advisories)

    # ---- P4 · GIT IDENTITY --------------------------------------------------------------
    # Required values come from the APPROVALS file, never from the build manifest: if the
    # checker read what the builder recorded, a builder change would silently relax the
    # check. The manifest is compared as a third party, not trusted as the source.
    for key, want in (('user.name', req['git_user_name']), ('user.email', req['git_user_email'])):
        got = git(surface, 'config', '--local', '--get', key).stdout.strip()
        if got != want:
            findings.append(('IDENTITY', '.git/config', '%s is %r, required %r'
                             % (key, got or '<unset>', want)))
    ids = git(surface, 'log', '--format=%an|%ae|%cn|%ce').stdout.strip().split('\n')
    for row in [r for r in ids if r]:
        an, ae, cn, ce = row.split('|')
        if (an, ae, cn, ce) != (req['git_user_name'], req['git_user_email'],
                                req['git_user_name'], req['git_user_email']):
            findings.append(('IDENTITY', 'commit', 'recorded identity %r' % row))

    # ---- P5 · GIT METADATA ---------------------------------------------------------------
    # The commit message is re-derived against a declared constant for the same reason
    # ASSIGNMENT.md is re-rendered: it is free text authored at build time, so identity is
    # the only check that catches an arbitrary sentence.
    msgs = [m for m in git(surface, 'log', '--format=%s%n%b').stdout.strip().split('\n') if m]
    if msgs != [req['commit_message']]:
        findings.append(('METADATA', 'commit message', 'is %r, required exactly %r'
                         % (msgs, [req['commit_message']])))
    n = git(surface, 'rev-list', '--all', '--count').stdout.strip()
    if n != str(req['commit_count']):
        findings.append(('METADATA', '.git', '%s commits, required %d' % (n, req['commit_count'])))
    refs = [l.split()[1] for l in git(surface, 'show-ref').stdout.strip().split('\n') if l.strip()]
    if refs != ['refs/heads/%s' % req['branch']]:
        findings.append(('METADATA', '.git/refs', 'refs are %r, required exactly %r'
                         % (refs, ['refs/heads/%s' % req['branch']])))
    for stray in ('ORIG_HEAD', 'MERGE_HEAD', 'CHERRY_PICK_HEAD', 'packed-refs',
                  'refs/stash', 'refs/notes'):
        if os.path.exists(os.path.join(surface, '.git', stray)):
            findings.append(('METADATA', '.git/' + stray, 'present on a freshly built surface'))
    rl = os.path.join(surface, '.git', 'logs', 'HEAD')
    if os.path.exists(rl):
        entries = [l for l in open(rl, encoding='utf-8').read().split('\n') if l.strip()]
        if len(entries) != req['commit_count']:
            findings.append(('METADATA', '.git/logs/HEAD', '%d reflog entries, required %d'
                             % (len(entries), req['commit_count'])))

    # ---- P6 · OBJECT STORE ----------------------------------------------------------------
    # An object can enter a store with no remote and no alternate: `git hash-object -w`
    # from another repository's `cat-file` output does it, and the existing remote/alternate
    # checks see nothing. Reachability is the property that holds regardless of the route in.
    allobj = set(git(surface, 'cat-file', '--batch-all-objects',
                     '--batch-check=%(objectname)').stdout.split())
    reach = set(l.split()[0] for l in git(surface, 'rev-list', '--objects', '--all')
                .stdout.strip().split('\n') if l.strip())
    orphan = allobj - reach
    if orphan:
        findings.append(('OBJECTSTORE', '.git/objects',
                         '%d object(s) in the store unreachable from the surface\'s own ref: %s'
                         % (len(orphan), ' '.join(sorted(orphan)[:4]))))
    extra_reach = reach - allobj
    if extra_reach:
        findings.append(('OBJECTSTORE', '.git/objects',
                         '%d ref-reachable object(s) not resident: the store is borrowing'
                         % len(extra_reach)))

    # ---- P7a · ASSIGNMENT TEMPLATE APPROVAL --------------------------------------------------
    # 🔴 Found by changing the template and watching the wrong thing happen. An assignment is
    # (template + spec). Binding only the spec caught the case whose spec I edited and let the
    # OTHER case pass unchanged — while the text its reader would be handed had changed too.
    # The template is a shared object, so it is pinned once and a change to it invalidates
    # every case at once, which is exactly what a change to it does.
    tdig = literal_digest_from_source('ASSIGNMENT_TEMPLATE')

    # ---- P7a-bis · STALE BYTECODE ------------------------------------------------------------
    # 🔴 Measured, and it defeated the check above in its first form. Python validates a
    # cached .pyc by (source mtime, source size). An edit that preserves size and lands in
    # the same second as the cached compile passes both, and the stale module is served. On
    # this platform the cache is ~/Library/Caches/com.apple.python/<abs source path>.pyc --
    # OUTSIDE the repository, invisible to every repo-scoped search and to any __pycache__
    # check. The template pin read its reference value BY IMPORT and so certified a template
    # that was not the one on disk.
    #
    # This is VOID, not FAIL: if the runtime is serving stale bytecode then `render_assignment`
    # in check_blind_surface.py's DERIVATION check is suspect too, and that is the primary
    # leak control. A battery cannot report on a runtime it cannot trust.
    try:
        sys.path.insert(0, HERE)
        from build_blind_surface import ASSIGNMENT_TEMPLATE as _imported
        idig = hashlib.sha256(_imported.encode('utf-8')).hexdigest()
        if tdig is not None and idig != tdig:
            return 2, [('VOID', 'bytecode cache',
                        'the imported template (%s) differs from the template in the source '
                        'file (%s): this runtime is serving stale bytecode, so every '
                        'import-based check here and in check_blind_surface.py is '
                        'untrustworthy. Clear the interpreter cache and re-run.'
                        % (idig[:16], tdig[:16]))], []
    except ImportError:
        pass

    # ---- P7b · CASE INPUT APPROVAL ----------------------------------------------------------
    # Two pins with two distinct meanings, and the distinction is the diagnostic:
    #   participant_projection  moves when the CASE SPEC changes
    #   rendered_authored       moves when ANYTHING a reader is handed changes -- the spec,
    #                           any template, any embedded string, any renderer
    dig = projection_digest(case)
    rdig = rendered_authored_digest(case)
    rec = apr['approved_cases'].get(case['case_id'])
    if rec is not None and rdig is not None and \
            rec.get('rendered_authored_sha256') != rdig:
        findings.append(('APPROVAL', 'rendered authored files',
                         'what a reader is handed digests to %s, approved %s'
                         % (rdig[:16], str(rec.get('rendered_authored_sha256'))[:16])))
    if rec is None:
        findings.append(('APPROVAL', case['case_id'],
                         'no approval on record; participant projection %s' % dig[:16]))
    elif rec['participant_projection_sha256'] != dig:
        findings.append(('APPROVAL', case['case_id'],
                         'participant projection is %s, approved %s -- the text a reader '
                         'will be handed is not the text that was approved'
                         % (dig[:16], rec['participant_projection_sha256'][:16])))
    else:
        # ---- P8 · APPROVER EXPOSURE (advisory here, blocking under --dispatch-gate) -------
        # An approver who has read the case's answer can still verify that text has not
        # CHANGED. They cannot serve as the independent review that the text does not leak.
        # Those are different acts, so they get different gates rather than one blended one.
        exp = rec.get('approver_case_exposure', 'UNKNOWN')
        if exp != 'NOT_SEEN':
            msg = ('approved by %r whose exposure to this case is %s: adequate to detect a '
                   'CHANGE to the text, not to certify it does not leak'
                   % (rec.get('approved_by', '?'), exp))
            (findings if dispatch_gate else advisories).append(('APPROVAL_EXPOSURE',
                                                                case['case_id'], msg))

    # ---- manifest cross-check: informational, never authoritative --------------------------
    if os.path.exists(manifest):
        man = json.load(open(manifest, encoding='utf-8'))
        if man.get('case_id') != case['case_id']:
            findings.append(('MANIFEST', manifest, 'manifest case_id %r != case spec %r'
                             % (man.get('case_id'), case['case_id'])))
    return (1 if findings else 0), findings, advisories


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--surface', required=True)
    ap.add_argument('--manifest', required=True)
    ap.add_argument('--case', required=True)
    ap.add_argument('--approvals', default=APPROVALS)
    ap.add_argument('--dispatch-gate', action='store_true',
                    help='additionally require an approval by an actor that has NOT seen '
                         'this case\'s answer. Building a surface and handing it to a reader '
                         'are different acts and are gated separately.')
    a = ap.parse_args()
    if not os.path.isdir(a.surface):
        print("VOID: surface not found: %s" % a.surface); return 2
    rc, findings, advisories = check(a.surface, a.manifest, a.case, a.approvals, a.dispatch_gate)
    print("SURFACE  %s" % a.surface)
    print("MODE     %s" % ('DISPATCH GATE' if a.dispatch_gate else 'build properties'))
    print()
    for cls, where, msg in advisories:
        print("  (advisory) [%-12s] %-30s %s" % (cls, str(where)[:30], msg[:100]))
    if rc == 0:
        print("VERDICT: PASS — 0 property findings")
        return 0
    if rc == 2:
        for _c, _w, m in findings:
            print("VOID: %s" % m)
        return 2
    print("VERDICT: FAIL — %d property finding(s)" % len(findings))
    for cls, where, msg in findings:
        print("  [%-12s] %-34s %s" % (cls, str(where)[-34:], msg[:110]))
    return 1


if __name__ == '__main__':
    sys.exit(main())
