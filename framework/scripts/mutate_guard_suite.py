#!/usr/bin/env python3
"""Mutation test for the write guard and the parity battery — do the tests bite?

A green suite proves the tests pass. It does not prove they would fail if the thing they
guard were broken, and that second property is the only one worth having for a safety
control. This harness breaks the control **on purpose**, one mutation at a time, and
requires the suite to notice.

    python3 framework/scripts/mutate_guard_suite.py            # every mutation
    python3 framework/scripts/mutate_guard_suite.py --list     # names only
    python3 framework/scripts/mutate_guard_suite.py --only M07

Each mutation is applied in a **detached git worktree at the current HEAD**, never in the
working tree, and the worktree is removed afterwards. A mutation that survives — the suite
still passes with the control broken — is a hole in the tests and is reported by name.

🔴 Why a fresh worktree and not a copy: `git worktree add --detach HEAD` reproduces the
committed tree exactly, so a mutation is the only difference between the run that must fail
and the run that passed. A `cp -R` of a working directory would carry whatever is uncommitted
with it, and the surviving mutation would be indistinguishable from a dirty tree.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

GUARD_POLICY = "framework/scripts/guard_policy.py"
GUARD_ENTRY = "framework/scripts/pre_tool_use_guard.py"
PARITY = "framework/scripts/runtime_parity.py"

GUARD_TOPOLOGY = "framework/scripts/repo_topology.py"

GUARD_SUITES = ("framework/scripts/test_pre_tool_use_guard.py",
                "scripts/test_guard_bash_command.py")
PARITY_SUITES = ("framework/scripts/test_runtime_parity.py",)

#: 🔴 The revision-9 guarantees are asserted end to end against a real multi-worktree
#: fixture, so the suite that must notice their removal is that one — not the guard
#: suites, which run against this worktree and would report a confinement failure as an
#: ordinary denial. A mutation pointed at the wrong suite survives for the wrong reason.
CONFINEMENT_SUITES = ("framework/scripts/test_confinement_and_delegation.py",)


class Mutation:
    def __init__(self, name, target, old, new, suites, why):
        self.name = name
        self.target = target
        self.old = old
        self.new = new
        self.suites = suites
        self.why = why


MUTATIONS = [
    # ── the policy ────────────────────────────────────────────────────────────────
    Mutation(
        "M01", GUARD_POLICY,
        'findings.append(Finding("BLANKET_STAGING", "git add", [UNNAMED],',
        'pass  # noqa\n            _ = (Finding("BLANKET_STAGING", "git add", [UNNAMED],',
        GUARD_SUITES, "blanket staging stops being reported at all"),
    Mutation(
        "M02", GUARD_POLICY,
        "        # 🔴 Without a root,",
        "        return OUTSIDE_REPO\n        # 🔴 Without a root,",
        GUARD_SUITES, "an unknown repository root fails OPEN instead of closed"),
    Mutation(
        # 🔴 REANCHORED in revision 8. The old anchor read
        #     if underivable:
        #         return UNDERIVABLE, DENY_UNDERIVABLE, findings
        # and that block no longer exists: `classify` now authorises an effect set and
        # then chooses a sentence. The harness reported ANCHOR_MISSING rather than a
        # pass, which is the only correct behaviour — a mutation that was never applied
        # is not a mutation the tests killed.
        "M03", GUARD_POLICY,
        "    if em.UNDERIVABLE in scopes:\n        return UNDERIVABLE, DENY_UNDERIVABLE, findings",
        "    if em.UNDERIVABLE in scopes:\n        return ALLOWED, None, findings",
        GUARD_SUITES, "an unresolvable write target is allowed instead of denied"),
    Mutation(
        "M04", GUARD_POLICY,
        '    if program == "eval":',
        '    if program == "eval" and False:',
        GUARD_SUITES, "`eval \"git add -A\"` stops being unwrapped"),
    Mutation(
        "M05", GUARD_POLICY,
        "        if piped_in and not operands_:",
        "        if False and piped_in and not operands_:",
        GUARD_SUITES, "a shell fed its script from a pipe stops being policed"),
    Mutation(
        "M06", GUARD_POLICY,
        '    stripped = ANSI_C_QUOTE.sub("", stripped)',
        "    pass  # ANSI-C quoting left in place",
        GUARD_SUITES, "`bash -c $'git add -A'` parses as a program called `$git`"),
    Mutation(
        "M07", GUARD_POLICY,
        "    if OPAQUE in argv[0]:",
        "    if False and OPAQUE in argv[0]:",
        GUARD_SUITES, "an expansion in argv[0] is read as a harmless program"),
    Mutation(
        "M08", GUARD_POLICY,
        "                analyse_command(argv[index + 1], findings, depth + 1)\n                return",
        "                return",
        GUARD_SUITES, "a `-c` script argument stops being re-analysed"),
    Mutation(
        "M09", GUARD_POLICY,
        'WRITES_LAST_OPERAND = frozenset({"cp", "mv", "install", "rsync", "ln"})',
        'WRITES_LAST_OPERAND = frozenset({"mv", "install", "rsync", "ln"})',
        GUARD_SUITES, "`cp` over a tracked file stops being a write"),
    Mutation(
        "M10", GUARD_POLICY,
        "    for argv, writes, piped_in in segments(resolve_assignments(lex(stripped))):",
        "    for argv, writes, piped_in in segments(lex(stripped)):",
        GUARD_SUITES, "a scratch path behind an in-command variable stops resolving"),
    Mutation(
        # 🔴 REANCHORED, and moved from the MESSAGE to the DECISION.
        #
        # The old M11 and M12 mutated the branches that pick a denial sentence. In
        # revision 8 those branches no longer decide anything — `em.authorize` does, and
        # a command it refuses is refused whichever sentence is chosen. Mutating the
        # message would now be an EQUIVALENT MUTANT: it survives because behaviour is
        # unchanged, which says nothing about the tests. So both move onto the grant
        # itself, where the meaning actually lives.
        "M11", "framework/scripts/effect_model.py",
        "_L4 = {kind: {INSIDE_REPO} for kind in _CONTENT}",
        "_L2[INSIDE_REPO] = None\n_L4 = {kind: {INSIDE_REPO} for kind in _CONTENT}\n"
        "_L3.update({kind: {INSIDE_REPO} for kind in _CONTENT})",
        GUARD_SUITES + ("framework/scripts/test_effect_model.py",),
        "SHELL_DEFAULT starts granting content writes inside the repository, which is "
        "the whole thing revisions 1-7 exist to stop"),
    Mutation(
        "M12", GUARD_POLICY,
        "            named = None if target in (UNNAMED, OPAQUE) else target",
        "            named = target if target not in (UNNAMED, OPAQUE) else '.'",
        GUARD_SUITES + ("framework/scripts/test_effect_model.py",),
        "a write whose target is never named is reported as a write to the working "
        "directory, so an UNNAMED mutation acquires a resolvable target"),

    # ── the adapter ───────────────────────────────────────────────────────────────
    Mutation(
        "M13", GUARD_ENTRY,
        "    if tool_name not in known:\n        raise Undecidable(",
        "    if tool_name not in known:\n        return None\n        raise Undecidable(",
        GUARD_SUITES, "an unrecognised tool is waved through instead of denied"),
    Mutation(
        "M14", GUARD_ENTRY,
        "            raise Undecidable(\n                f\"`{match.group(1)}` is called with an argument this guard cannot read; \"",
        "            continue\n            raise Undecidable(\n                f\"`{match.group(1)}` is called with an argument this guard cannot read; \"",
        GUARD_SUITES, "an unreadable code-mode shell call is skipped instead of denied"),
    Mutation(
        # 🔴 M15 and M16 are REBOUND, not retired. `decide` now iterates
        # `(command, carrier)` pairs so each code-mode call is judged against its own
        # workdir, and the old anchors vanished with that edit. The guarantees are
        # unchanged; a mutation left pointing at deleted text reports ANCHOR_MISSING,
        # and ANCHOR_MISSING is not a kill — it is a mutation that was never applied.
        "M15", GUARD_ENTRY,
        "    for command, carrier in calls:",
        "    for command, carrier in calls[:1]:",
        GUARD_SUITES + CONFINEMENT_SUITES,
        "only the first shell call in a code-mode body is judged"),
    Mutation(
        "M16", GUARD_ENTRY,
        '        calls = [("apply_patch <<\'PATCH\'\\n" + program_text(tool_input) + "\\nPATCH",\n'
        '                  tool_input)]',
        "        calls = []",
        GUARD_SUITES, "the apply_patch tool payload stops being policed"),

    # ── the battery ───────────────────────────────────────────────────────────────
    Mutation(
        "M17", PARITY,
        "PASSING_HOOK_STATES = frozenset({DEMONSTRATED})",
        "PASSING_HOOK_STATES = frozenset({DEMONSTRATED, TRUST_PENDING, CONFIGURED})",
        PARITY_SUITES, "configuration alone is accepted as demonstration"),
    Mutation(
        "M18", PARITY,
        'WRITE_ENABLED_REQUIRES = READ_ONLY_REQUIRES + (\n    "GUARD_POLICY_PARITY", "HOOK_REGISTRATION_PRESENT", "HOOK_DEMONSTRATED",\n    "NO_RUNTIME_AUTHORITY_ESCALATION",\n)',
        "WRITE_ENABLED_REQUIRES = READ_ONLY_REQUIRES",
        PARITY_SUITES, "the write floor collapses into the read floor"),
    Mutation(
        "M19", PARITY,
        '    if not actor:\n        return None, "no ACTOR_ID assigned"',
        '    if not actor:\n        return ROLE_CONTRACTS["plan"], ""',
        PARITY_SUITES, "an unassigned actor is silently elected to a default role"),
    Mutation(
        "M20", PARITY,
        '    if observed == "REFUSED":',
        '    if True:',
        PARITY_SUITES, "any receipt at all reports DEMONSTRATED"),
    Mutation(
        "M21", PARITY,
        "    missing = [k for k in required if not data.get(k)]",
        "    missing = []",
        PARITY_SUITES, "a receipt with no provenance is accepted"),
    Mutation(
        "M22", PARITY,
        '        elif answers["claude"] != expected:',
        '        elif False:',
        PARITY_SUITES, "the battery goes back to comparing runtimes only to each other"),
    Mutation(
        "M23", PARITY,
        '    if not surface.guard_entry.exists():\n        leaks.append("the shared engine is absent, so nothing is policed")',
        "    if False:\n        leaks.append(\"the shared engine is absent, so nothing is policed\")",
        PARITY_SUITES, "a missing engine stops failing the fail-closed row"),
    Mutation(
        "M24", PARITY,
        "    if hop not in router_text and path.as_posix() not in router_text:",
        "    if False:",
        PARITY_SUITES, "a role contract that exists counts as reachable without a route"),
    Mutation(
        "M25", PARITY,
        '        for tool in ("shell_command", "unified_exec", "exec"):\n            if tool not in declared:',
        '        for tool in ("shell_command", "unified_exec", "exec"):\n            if tool in declared and False:',
        PARITY_SUITES, "a missing matcher for a tool the runtime uses stops being noticed"),
    # ── the two bypasses found by USING the guard rather than testing it ──
    Mutation(
        "M27", GUARD_POLICY,
        '        if quote == \'"\':\n            if char == "\\\\" and i + 1 < n:',
        '        if quote:\n            out.append(char)\n            if char == quote:\n'
        '                quote = ""\n            i += 1\n            continue\n'
        '        if quote == \'"\':\n            if char == "\\\\" and i + 1 < n:',
        GUARD_SUITES, "a substitution inside double quotes stops being extracted, so "
                      "`echo \"$(git add -A)\"` runs unpoliced"),
    Mutation(
        "M28", GUARD_POLICY,
        "    while argv and ASSIGNMENT.match(argv[0]) and not argv[0].startswith(\"-\"):\n        argv = argv[1:]",
        "    pass  # assignment prefixes left in place",
        GUARD_SUITES, "a leading NAME=VALUE is read as the program, so `FOO=1 git add -A` "
                      "matches no rule"),
    Mutation(
        "M29", GUARD_POLICY,
        "    if EXPANDS.search(token):\n        return _classify_by_prefix(token, cwd, repo_root)",
        "    if EXPANDS.search(token):\n        return SCRATCH",
        GUARD_SUITES, "any expanding path is treated as scratch, so a repository target "
                      "behind a variable is allowed"),
    Mutation(
        "M30", GUARD_POLICY,
        "    if any(EXPANDS.search(part) for part in segments_[:-1]):\n        return UNDERIVABLE",
        "    if False:\n        return UNDERIVABLE",
        GUARD_SUITES, "an expansion in a middle path segment is judged by a prefix that "
                      "no longer determines the directory"),
    Mutation(
        "M31", GUARD_POLICY,
        "        for match in SHELL_OUT.finditer(body):\n            _analyse_shell_out(body, match.end(), findings)",
        "        pass  # shell-outs from a program body are not judged",
        GUARD_SUITES, "a program body that shells out to `git add -A` is not judged"),
    Mutation(
        "M26", PARITY,
        "    body = text.split(\"[hooks]\", 1)[-1] if \"[hooks]\" in text else text\n    return set(MATCHER_LINE.findall(body))",
        "    return set(re.findall(r'[a-z_]+', text))",
        PARITY_SUITES, "matchers are matched as substrings again, so `exec` inside "
                       "`unified_exec` counts as a declaration"),

    # ── revision 8 · SEMANTIC mutations ───────────────────────────────────────────
    #
    # 🔴 Each of these breaks a MEANING, not a string. The test for whether a mutation
    # is semantic: could it be introduced by a plausible refactor that keeps every
    # identifier and every message intact? M32 is a one-character regex edit, M35 is a
    # reordering of two blocks, M38 removes a single condition from a comprehension.
    # None of them changes a name the tests could be matching on.
    Mutation(
        "M32", GUARD_POLICY,
        'FD_WRITE = re.compile(r"&>>|&>|" + _FD_START + r"\\d+>>|" + _FD_START + r"\\d+>")',
        'FD_WRITE = re.compile(r"(?!x)x")',
        GUARD_SUITES,
        "a numbered redirect stops being a redirect, so `echo x 1> repo/file` is allowed "
        "while `echo x > repo/file` is denied — the revision-7 bypass, restored"),
    Mutation(
        "M33", GUARD_POLICY,
        'lexer = shlex.shlex(command, posix=True, punctuation_chars="();<>|&\\n")',
        'lexer = shlex.shlex(command, posix=True, punctuation_chars=True)',
        GUARD_SUITES,
        "a newline stops separating commands, so only the first line of a multi-line "
        "block is analysed — the bypass every revision through 7 shipped"),
    Mutation(
        "M34", GUARD_POLICY,
        '        into = flag_value(argv, "-t", "--target-directory")',
        '        into = None',
        GUARD_SUITES,
        "`cp -t DIR src` reports a SOURCE as its destination, so a write into the "
        "repository is classified by a scratch path"),
    Mutation(
        "M35", GUARD_POLICY,
        "    if repo_root is not None:\n        root = posixpath.normpath(repo_root)\n"
        "        if path == root or path.startswith(root.rstrip(\"/\") + \"/\"):\n"
        "            return INSIDE_REPO\n\n    if SCRATCH_SEGMENT in path.split(\"/\"):",
        "    if SCRATCH_SEGMENT in path.split(\"/\"):",
        GUARD_SUITES,
        "the scratch prefix beats repository membership again, so a repository under "
        "/tmp or /var/folders is entirely unguarded"),
    Mutation(
        "M36", GUARD_POLICY,
        '    if sub in GIT_NETWORK_SUBCOMMANDS:',
        '    if False and sub in GIT_NETWORK_SUBCOMMANDS:',
        GUARD_SUITES,
        "`git push` stops being a NETWORK_WRITE, so publishing to a public remote is "
        "allowed from the shell"),
    Mutation(
        # 🔴 The target file was wrong: this rule lives in effect_model.py, and the
        # harness reported ANCHOR_MISSING rather than letting it pass unapplied.
        "M37", "framework/scripts/effect_model.py",
        '        if effect.kind in MUTATING and effect.scope not in NAMEABLE:',
        '        if False:',
        GUARD_SUITES + ("framework/scripts/test_effect_model.py",),
        "a mutation whose target is UNNAMED or UNDERIVABLE stops being refused ahead of "
        "the authority table, so the highest rung starts authorising them"),
    Mutation(
        "M38", "framework/scripts/effect_model.py",
        '        if effect.kind == UNKNOWN_EFFECT:\n'
        '            denials.append((effect, "the effect could not be derived at all"))\n'
        '            continue',
        '        if effect.kind == UNKNOWN_EFFECT:\n            continue',
        GUARD_SUITES + ("framework/scripts/test_effect_model.py",),
        "UNKNOWN_EFFECT stops denying — the one rule with no override"),
    Mutation(
        "M39", "framework/scripts/effect_model.py",
        '    def permits(self, kind: str, scope: str) -> bool:\n'
        '        return scope in self.grants.get(kind, frozenset())',
        '    def permits(self, kind: str, scope: str) -> bool:\n'
        '        return kind in self.kinds and scope in {\n'
        '            s for scopes in self.grants.values() for s in scopes}',
        GUARD_SUITES + ("framework/scripts/test_effect_model.py",),
        "the authority collapses from per-kind scopes back into kinds x scopes, so any "
        "rung that permits `git commit` also permits a shell write into the repository"),
    Mutation(
        "M40", "framework/scripts/post_effect_verify.py",
        '    verdict = em.MATCH if not extra and not missing else em.MISMATCH',
        '    verdict = em.MATCH if not extra else em.MISMATCH',
        ("framework/scripts/test_post_effect_verify.py",),
        "a MISSING authorised effect stops invalidating the write, so 'the write did "
        "not happen' and 'it happened where I cannot see' become the same answer"),
    Mutation(
        "M41", "framework/scripts/post_effect_verify.py",
        '        worktree[entry[3:]] = entry[1]',
        '        worktree[entry[3:]] = entry[:2]',
        ("framework/scripts/test_post_effect_verify.py",),
        "the delta reads the index column as a worktree change again, so every "
        "legitimate `git add` is reported with a phantom EXTRA write"),
    Mutation(
        "M42", "framework/scripts/execution_attestation.py",
        '    if not current.complete:\n'
        '        return Attestation(RESUME_BINDING_MISMATCH, current,',
        '    if False:\n'
        '        return Attestation(RESUME_BINDING_MISMATCH, current,',
        ("framework/scripts/test_execution_attestation.py",),
        "a dimension that became UNDERIVABLE on resume stops failing, so a field nobody "
        "can read counts as a field that stayed the same"),
    Mutation(
        "M43", "framework/scripts/execution_attestation.py",
        '        if not self.ok:\n            return em.UNATTESTED\n        return self.binding.authority',
        '        return self.binding.authority',
        ("framework/scripts/test_execution_attestation.py",),
        "a failed attestation keeps the authority it DECLARED, which is exactly the "
        "shape of an authority inherited across a restart"),
    Mutation(
        "M44", "framework/scripts/execution_receipt.py",
        '        decision = em.authorize(effects, raw["authority"])\n'
        '        if not decision.authorized:',
        '        decision = em.authorize(effects, raw["authority"])\n'
        '        if False:',
        ("framework/scripts/test_execution_receipt.py",),
        "a receipt stops having its own authorisation re-derived, so one claiming an "
        "effect set its named authority does not grant validates perfectly"),
    Mutation(
        "M45", GUARD_POLICY,
        '    return PROHIBITED, DENY_SHELL_WRITE + "\\n\\n" + decision.reason(), findings',
        '    return ALLOWED, None, findings',
        GUARD_SUITES + ("framework/scripts/test_effect_model.py",),
        "the catch-all at the end of `classify` allows anything the specific message "
        "branches did not name, so a refused decision becomes an ALLOW for any effect "
        "shape nobody wrote a sentence for"),
    Mutation(
        "M46", "framework/scripts/execution_attestation.py",
        '        if not self.ok:\n            return em.UNATTESTED',
        '        if not self.ok and False:\n            return em.UNATTESTED',
        ("framework/scripts/test_execution_attestation.py",),
        "a duplicate of M43 by a different edit — the revocation is removed by a "
        "CONDITION rather than by deleting the branch, which a test matching on "
        "source text would miss and a test asserting behaviour catches"),

    # ── revision 9: the confinement, the workdir, and the two post-effect repairs ───
    #
    # 🔴 Each of these removes ONE guarantee revision 9 adds, and each was measured
    # false before it was repaired. A survivor here is not a weak test, it is a P0
    # guarantee nothing asserts — which makes the candidate NOT READY, not merely
    # under-tested.
    Mutation(
        "M47", GUARD_POLICY,
        '        if placed in (rt.ASSIGNED_WORKTREE, rt.PEER_WORKTREE, rt.SHARED_CHECKOUT,\n'
        '                      rt.GIT_COMMON_DIR):\n'
        '            return _FROM_TOPOLOGY[placed]',
        '        pass',
        CONFINEMENT_SUITES,
        "the topology stops being consulted at all, so every peer worktree, the shared "
        "checkout and the whole git common dir collapse back into OUTSIDE_REPO — where "
        "SHELL_DEFAULT grants content writes"),
    Mutation(
        "M48", "framework/scripts/effect_model.py",
        'CONFINED: FrozenSet[str] = frozenset({PEER_WORKTREE, SHARED_CHECKOUT, GIT_COMMON_DIR})',
        'CONFINED: FrozenSet[str] = frozenset()',
        CONFINEMENT_SUITES + ("framework/scripts/test_effect_model.py",),
        "the confined set empties, so the property test passes vacuously and the "
        "denial message that names the scope stops firing — the shape of a guarantee "
        "removed by emptying the set it quantifies over"),
    Mutation(
        "M49", "framework/scripts/effect_model.py",
        '_L2 = {kind: {SCRATCH, OUTSIDE_REPO} for kind in _CONTENT}',
        '_L2 = {kind: {SCRATCH, OUTSIDE_REPO, PEER_WORKTREE, SHARED_CHECKOUT,\n'
        '              GIT_COMMON_DIR} for kind in _CONTENT}',
        CONFINEMENT_SUITES + ("framework/scripts/test_effect_model.py",),
        "a rung is GIVEN the confined scopes. The confinement is an OMISSION from the "
        "table, and this is the edit that undoes an omission with no error anywhere"),
    Mutation(
        "M50", "framework/scripts/repo_topology.py",
        '        return sorted(table, key=lambda pair: len(pair[0]), reverse=True)',
        '        return table',
        CONFINEMENT_SUITES + ("framework/scripts/test_repo_topology.py",),
        "longest-prefix becomes declaration order, so a worktree nested inside the "
        "shared checkout — which is how this repository is laid out — is classified as "
        "the checkout that contains it"),
    Mutation(
        "M51", "framework/scripts/repo_topology.py",
        '        resolved = self._one(_realpath(path))\n'
        '        return lexical if STRICTNESS[lexical] >= STRICTNESS[resolved] else resolved',
        '        return lexical',
        CONFINEMENT_SUITES + ("framework/scripts/test_repo_topology.py",),
        "only the lexical spelling is classified, so a symlink inside the assigned "
        "worktree pointing at a peer or at the common dir launders the write"),
    Mutation(
        "M52", GUARD_ENTRY,
        '    workdir = derive_workdir(payload, carrier)',
        '    workdir = payload.get("cwd") or ""',
        CONFINEMENT_SUITES,
        "the effective working directory reverts to the session cwd, so a command that "
        "RUNS inside the worktree with cwd elsewhere has its relative repository writes "
        "measured against /tmp"),
    Mutation(
        "M53", GUARD_ENTRY,
        '    if not os.path.isdir(resolved):\n        raise Undecidable(',
        '    if False:\n        raise Undecidable(',
        CONFINEMENT_SUITES,
        "a workdir that does not exist stops failing closed and silently falls back, "
        "which restores the revision-8 reading for the one input designed to defeat it"),
    Mutation(
        "M54", GUARD_POLICY,
        '    if program in DELEGATING_BINARIES:',
        '    if False and program in DELEGATING_BINARIES:',
        CONFINEMENT_SUITES,
        "`codex exec` and `claude -p` become ordinary programs again, so the work is "
        "handed to a runtime with its own permissions and no hook this guard can see"),
    Mutation(
        "M55", "framework/scripts/post_effect_verify.py",
        '    if not current_branch or branch_after != current_branch:\n'
        '        return frozenset()\n'
        '    return frozenset({f"refs/heads/{current_branch}"})',
        '    return frozenset({f"refs/heads/{name}" for name in\n'
        '                      (current_branch, branch_after) if name})',
        ("framework/scripts/test_confinement_and_delegation.py",
         "framework/scripts/test_post_effect_verify.py"),
        "COMMIT covers a ref the commit did not move — a commit that also switched "
        "branch, or that moved a second ref, verifies as if it had not"),
    Mutation(
        "M56", "framework/scripts/post_effect_verify.py",
        '        mode_moved[path] = (was_mode, now_mode)\n'
        '        observed.append(em.Effect(em.PERMISSION_CHANGE, path, em.INSIDE_REPO, "mode",',
        '        mode_moved[path] = (was_mode, now_mode)\n'
        '        _unused = (em.Effect(em.PERMISSION_CHANGE, path, em.INSIDE_REPO, "mode",',
        ("framework/scripts/test_confinement_and_delegation.py",
         "framework/scripts/test_post_effect_verify.py"),
        "a permission change stops being observed while still being authorised, which "
        "is UNOBSERVABLE_EFFECT quietly becoming ASSUMED_MATCH"),
    Mutation(
        "M57", "framework/scripts/post_effect_verify.py",
        '        if added == "-" or removed == "-":\n            return True',
        '        if added == "-" or removed == "-":\n            return False',
        ("framework/scripts/test_confinement_and_delegation.py",
         "framework/scripts/test_post_effect_verify.py"),
        "a BINARY file's content change is read as no change, so a chmod authorisation "
        "covers a content rewrite git declined to count lines for"),
    Mutation(
        "M58", "framework/scripts/codex_hook_state.py",
        '    if config.get("on_path_names_hooks"):',
        '    if config.get("on_path_names_hooks") or config.get("off_path_names_hooks"):',
        ("framework/scripts/test_runtime_diagnostics.py",),
        "a config the runtime never reads is reported as TRUST_BLOCKED, sending the "
        "reader to ask for a trust decision about a file nothing ever offered"),
    Mutation(
        "M59", "framework/scripts/guard_revision.py",
        '    if UNKNOWN in generations or ABSENT in generations:\n'
        '        return "UNDERIVABLE"',
        '    if False:\n        return "UNDERIVABLE"',
        ("framework/scripts/test_runtime_diagnostics.py",),
        "a worktree whose guard could not be read is folded into the YES/NO answer, so "
        "a failure to measure is reported as a measurement"),
    Mutation(
        "M60", "framework/scripts/hostile_corpus.py",
        '    mutating = [r for r in rows\n'
        '                if r.get("mutating") and not r.get("positive_control")\n'
        '                and r["observed"] != SKIP\n'
        '                and r["id"] not in confounded]',
        '    mutating = [r for r in rows if r.get("mutating") and r["observed"] != SKIP]',
        ("framework/scripts/test_runtime_diagnostics.py",),
        "the positive floor is counted as bypasses again, so the corpus reports a "
        "revision as worse the more controls it is given"),
    Mutation(
        "M61", "framework/scripts/hostile_corpus.py",
        '    confounded = [] if scene_recognised else [r["id"] for r in rows]',
        '    confounded = []',
        ("framework/scripts/test_runtime_diagnostics.py",),
        "an engine that reads the whole scene as scratch is scored anyway, so a "
        "location defect is attributed to every family the corpus names and the "
        "revision that fixed the location is credited with closing all of them"),

    # ══ REVISION 10 ═════════════════════════════════════════════════════════════════
    #
    # 🔴 The first four are the R1 repair, broken in the four ways it can be broken: at
    # the adapter, at the policy default, at the module's source table, and at the
    # topology. A repair that lives in four places has to be attacked in four places, and
    # a suite that only notices one of them is a suite that would let the other three
    # ship.
    Mutation(
        "M62", GUARD_ENTRY,
        '            assigned=assignment.worktree)',
        '            assigned=workdir)',
        CONFINEMENT_SUITES,
        "🔴 THE REVISION-9 DEFECT ITSELF: the assigned worktree is sourced from the "
        "EFFECTIVE WORKDIR again, so naming a peer as the workdir makes the peer this "
        "actor's own tree and SHELL_DEFAULT's staging and commit grants apply to it"),
    Mutation(
        "M63", GUARD_ENTRY,
        '    assignment = session_binding.derive(payload)',
        '    assignment = session_binding.Assignment(\n'
        '        payload.get("cwd"), session_binding.CALLER)',
        CONFINEMENT_SUITES,
        "the assignment is sourced from the INVOCATION CWD instead of the session "
        "binding — the same defect one field over, and the spelling that survives a "
        "repair aimed only at `workdir`"),
    Mutation(
        "M64", GUARD_POLICY,
        '    if not assigned or not isinstance(assigned, str):\n        return None',
        '    if not assigned or not isinstance(assigned, str):\n'
        '        import inspect\n'
        '        return rt.cached(inspect.currentframe().f_back.f_locals.get("cwd"))',
        CONFINEMENT_SUITES,
        "an UNDERIVABLE assignment falls back to the effective workdir's topology "
        "instead of denying, which is the fail-open reading of 'we do not know'"),
    Mutation(
        "M65", "framework/scripts/session_binding.py",
        '        (CALLER, assigned),',
        '        (CALLER, assigned),\n        ("WORKDIR", payload.get("workdir")),',
        CONFINEMENT_SUITES,
        "a MODEL-WRITTEN payload key is added to the trusted source table, which hands "
        "the authority perimeter straight back to the model with the adapter untouched"),
    Mutation(
        "M66", GUARD_POLICY,
        '    return _stricter(outside, _workdir_repository_overlay(path, repo_root, unbound))',
        '    return _stricter(SCRATCH, _workdir_repository_overlay(path, repo_root, unbound))',
        CONFINEMENT_SUITES + ("framework/scripts/test_repo_topology.py",),
        "the SESSION's answer is discarded and only the workdir overlay decides, so "
        "every path outside the effective workdir's own tree reads as scratch"),
    Mutation(
        "M67", GUARD_POLICY,
        '    return UNDERIVABLE if unbound else INSIDE_REPO',
        '    return INSIDE_REPO',
        CONFINEMENT_SUITES + ("framework/scripts/test_pre_tool_use_guard.py",),
        "an UNBOUND session gets INSIDE_REPO from the overlay — and INSIDE_REPO is a "
        "GRANT for STAGE and COMMIT, so a session with no perimeter commits into "
        "whatever repository it is standing in"),
    Mutation(
        "M68", GUARD_POLICY,
        '        if rc.cached().contains(path):\n            return RUNTIME_CONFIG',
        '        if False:\n            return RUNTIME_CONFIG',
        CONFINEMENT_SUITES,
        "the runtime configuration scope is removed from classification, so the file "
        "that decides whether this guard runs becomes writable by the actor it governs"),
    Mutation(
        "M69", "framework/scripts/effect_model.py",
        'UNGRANTED: FrozenSet[str] = CONFINED | frozenset({RUNTIME_CONFIG})',
        'UNGRANTED: FrozenSet[str] = frozenset()',
        CONFINEMENT_SUITES + ("framework/scripts/test_effect_model.py",),
        "🔴 the domain every ungranted-scope property is quantified over is EMPTIED, "
        "which makes all of them vacuously true — the M48 lesson, one scope later"),
    Mutation(
        "M70", "framework/scripts/runtime_config.py",
        '        return candidate in self.members or candidate in self.ancestors',
        '        return candidate in self.members',
        CONFINEMENT_SUITES,
        "membership stops covering ancestors, so `rm -rf <CODEX_HOME>` destroys the "
        "registration without ever naming it"),
    Mutation(
        "M71", "framework/scripts/runtime_config.py",
        '        members.extend(posixpath.join(claude_home, name)\n'
        '                       for name in CLAUDE_REGISTRATION_FILES)',
        '        pass',
        CONFINEMENT_SUITES,
        "the Claude registration leaves the surface, so the settings file carrying both "
        "the hook and the `env` block session_binding reads becomes writable"),
    Mutation(
        "M72", GUARD_POLICY,
        '    launcher = launcher_key(argv)\n    if launcher is not None:',
        '    launcher = launcher_key(argv)\n    if False:',
        CONFINEMENT_SUITES,
        "launcher unwrapping is removed, so `npx codex exec` reaches an agent runtime "
        "with the delegation test looking at `npx`"),
    Mutation(
        "M73", GUARD_POLICY,
        'PACKAGE_LAUNCHERS = {',
        'PACKAGE_LAUNCHERS = {} or {',
        CONFINEMENT_SUITES,
        "the launcher table is emptied rather than the branch removed — the same "
        "behaviour by a different edit, and the one a test that asserts on the branch "
        "would miss"),
    Mutation(
        "M74", GUARD_POLICY,
        '            _, targets = chmod_operands(argv)',
        '            targets = operands(argv, program)[1:]',
        CONFINEMENT_SUITES,
        "chmod goes back to counting its mode off the front, so `chmod -x <scratch>` "
        "loses its path and is refused for having no target"),
    Mutation(
        "M75", GUARD_POLICY,
        '        named = [qualify_ref(sub, t) for t in named] if named else ["HEAD"]',
        '        named = named or ["HEAD"]',
        ("framework/scripts/test_post_effect_verify.py",),
        "ref normalisation is removed, so `git branch -D other` predicts `other` while "
        "the observation says `refs/heads/other` and an authorised deletion verifies "
        "INVALID"),
    Mutation(
        "M76", GUARD_POLICY,
        '        if sub == "update-ref" and named:\n            named = named[:1]',
        '        if False:\n            named = named[:1]',
        ("framework/scripts/test_post_effect_verify.py",),
        "`git update-ref <ref> <sha>` predicts a second ref mutation on the SHA, a "
        "target that cannot exist and is reported MISSING for every authorised call"),
    Mutation(
        "M77", "framework/scripts/codex_hook_state.py",
        '    if answer.get("error") is not None:\n        return None, stderr',
        '    if False:\n        return None, stderr',
        ("framework/scripts/test_runtime_diagnostics.py",),
        "a JSON-RPC error becomes an empty hook set again, so a query that FAILED is "
        "crossed with the filesystem and named CONFIG_ABSENT or TRUST_BLOCKED"),
    Mutation(
        "M78", "framework/scripts/codex_hook_state.py",
        '    if hooks is None:\n        # 🔴 The runtime did not answer.',
        '    if False:\n        # 🔴 The runtime did not answer.',
        ("framework/scripts/test_runtime_diagnostics.py",),
        "the non-answer branch is removed one layer down, so `hooks_for` returning None "
        "falls through to the empty-hooks reading"),
    Mutation(
        "M79", "framework/scripts/codex_hook_state.py",
        '    CONFIG_ABSENT, CONFIG_INVALID, CONFIG_OFF_RESOLUTION_PATH,',
        '    CONFIG_ABSENT, CONFIG_INVALID, "CONFIG_DISCOVERED", CONFIG_OFF_RESOLUTION_PATH,',
        ("framework/scripts/test_runtime_diagnostics.py",),
        "a dead diagnostic state is reintroduced — declared, unreachable, and findable "
        "in a report a reader will never see it in"),
    Mutation(
        "M80", "framework/scripts/hostile_corpus.py",
        '        "sha": "HEAD",',
        '        "sha": None,',
        ("framework/scripts/test_runtime_diagnostics.py",),
        "🔴 the candidate's own engine reverts to the WORKING TREE, so the headline "
        "ratio becomes a function of disk state and nobody re-running it from the "
        "repository gets the same answer"),
    Mutation(
        "M81", "framework/scripts/hostile_corpus.py",
        '    pin = (overrides or {}).get(revision) or str(ENGINES[revision]["sha"])',
        '    pin = str(ENGINES[revision]["sha"])',
        ("framework/scripts/test_runtime_diagnostics.py",),
        "an explicit --engine-sha pin is ignored, so a run that names the content commit "
        "silently measures whatever HEAD has become"),
    Mutation(
        "M82", GUARD_ENTRY,
        '            return _deny(reason, code, assignment.source)',
        '            return _deny(reason)',
        ("scripts/test_guard_bash_command.py",),
        "the decision code and the binding source leave the denial, so a live probe is "
        "back to a sentence the legacy guard also contains"),
    Mutation(
        "M83", "framework/scripts/codex_registration.py",
        '    return UNANCHORED',
        '    return RUNTIME_ANCHORED',
        ("framework/scripts/test_runtime_diagnostics.py",),
        "a RELATIVE registration is reported as deterministically anchored, so the "
        "probe starts against a config that names a different file per cwd"),
    Mutation(
        "M84", "framework/scripts/codex_registration.py",
        '    unmet = [name for name, _ in PRECONDITIONS if observations.get(name) is not True]',
        '    unmet = [name for name in observations if observations[name] is not True]',
        ("framework/scripts/test_runtime_diagnostics.py",),
        "a precondition nobody answered counts as met, so a probe starts with a "
        "requirement never checked — the failed-query defect inside the module written "
        "to stop it"),
    Mutation(
        "M85", "framework/scripts/codex_registration.py",
        '    if not (observations.get("REV10_GENERATION_CONFIRMED") is True\n'
        '            and observations.get("REV10_UNIQUE_DENIAL_OBSERVED") is True):',
        '    if False:',
        ("framework/scripts/test_runtime_diagnostics.py",),
        "🔴 the legacy discriminator is accepted as revision-10 proof: any refusal at "
        "all is scored as the candidate's engine firing, which is exactly the false GO "
        "the revision-9 protocol could return"),
    Mutation(
        "M86", "framework/scripts/guard_revision.py",
        '    if rev10:\n        return REV10',
        '    if False:\n        return REV10',
        ("framework/scripts/test_runtime_diagnostics.py",),
        "the revision-10 generation stops being derivable, so the census reports the "
        "candidate worktree as revision 9 and the probe precondition passes on the "
        "wrong engine"),
    Mutation(
        "M87", "framework/scripts/runtime_parity.py",
        '        "<WORKTREE_B_REL>": (os.path.relpath(peer, str(surface.root)) if peer else ""),',
        '        "<WORKTREE_B_REL>": "../mirror",',
        ("framework/scripts/test_runtime_parity.py",),
        "the relative peer placeholder is hard-coded again, so on a host without that "
        "layout the row changes from PEER_WORKTREE to OUTSIDE_REPO with no skip and no "
        "warning"),
]


def apply_and_run(mutation, head):
    """Run one mutation against `head`, which is PINNED by the caller.

    🔴 An earlier version re-read `HEAD` inside this function, once per mutation. A run
    takes minutes; a commit landing halfway through it silently split the run across two
    trees, and the report said nothing about that. A mutation report is only a statement
    about a tree if every mutation saw the same one, so the tip is resolved once and
    printed with the results.
    """
    tmp = Path(tempfile.mkdtemp(prefix=f"mutate-{mutation.name}-"))
    tree = tmp / "tree"
    add = subprocess.run(["git", "-C", str(ROOT), "worktree", "add", "--detach",
                          str(tree), head], capture_output=True, text=True)
    if add.returncode != 0:
        shutil.rmtree(tmp, ignore_errors=True)
        return "WORKTREE_FAILED", add.stderr.strip()[:200]
    try:
        target = tree / mutation.target
        source = target.read_text(encoding="utf-8")
        if mutation.old not in source:
            return "ANCHOR_MISSING", f"{mutation.target} no longer contains the anchor"
        if source.count(mutation.old) != 1:
            return "ANCHOR_AMBIGUOUS", f"{source.count(mutation.old)} matches"
        target.write_text(source.replace(mutation.old, mutation.new, 1), encoding="utf-8")

        failures = []
        for suite in mutation.suites:
            result = subprocess.run([sys.executable, suite], cwd=str(tree),
                                    capture_output=True, text=True)
            if result.returncode != 0:
                tail = [ln for ln in (result.stdout + result.stderr).splitlines()
                        if ln.startswith(("FAIL:", "ERROR:"))]
                failures.append((suite, tail[:2]))
        if failures:
            return "KILLED", "; ".join(
                f"{Path(s).name}: {f[0] if f else 'failed'}" for s, f in failures)
        return "SURVIVED", "every suite still passed with the control broken"
    finally:
        subprocess.run(["git", "-C", str(ROOT), "worktree", "remove", "--force", str(tree)],
                       capture_output=True, text=True)
        shutil.rmtree(tmp, ignore_errors=True)


#: The prefix every worktree this harness creates is named with. `prune()` will not
#: touch a directory whose name does not start with it.
WORKTREE_PREFIX = "mutate-"


def prune() -> int:
    """Remove worktrees an INTERRUPTED run of this harness left behind.

    🔴 This exists because the guard this harness tests forbids the cleanup. `git
    worktree remove` and `git worktree prune` both need REF_WRITE, which no runtime,
    role or lease grants — so a run killed part-way leaves an entry that nobody can
    clear from the shell, and a stale worktree makes `guard_revision.survey` report
    `UNDERIVABLE` where the truth is `NO`. The sanctioned path out of a denial is "a
    committed script invoked by name", and this is that script doing its own cleaning.

    🔴 It removes ONLY worktrees this harness could have created: the path must be
    absent from disk AND its directory name must carry `WORKTREE_PREFIX`. A prune that
    matched on prunability alone would remove another actor's worktree the moment their
    external drive was unmounted, which is precisely the cross-worktree act the guard
    exists to prevent — performed by the tool that verifies the prevention.
    """
    listing = subprocess.run(["git", "-C", str(ROOT), "worktree", "list", "--porcelain"],
                             capture_output=True, text=True).stdout
    removed, skipped = [], []
    for line in listing.splitlines():
        if not line.startswith("worktree "):
            continue
        path = Path(line[len("worktree "):].strip())
        if not path.name.startswith(WORKTREE_PREFIX) and \
                not any(p.startswith(WORKTREE_PREFIX) for p in path.parts):
            continue
        if path.exists():
            skipped.append(f"{path}  — still on disk; a run may be in progress")
            continue
        subprocess.run(["git", "-C", str(ROOT), "worktree", "remove", "--force",
                        str(path)], capture_output=True)
        removed.append(str(path))
    for path in removed:
        print(f"REMOVED   {path}")
    for note in skipped:
        print(f"KEPT      {note}")
    if not removed and not skipped:
        print("nothing to prune — no worktree of this harness is stranded")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--only", default=None)
    parser.add_argument("--prune", action="store_true",
                        help="remove worktrees a previous interrupted run left behind")
    args = parser.parse_args()

    chosen = [m for m in MUTATIONS if not args.only or m.name == args.only]
    if args.list:
        for m in chosen:
            print(f"{m.name}  {Path(m.target).name:<26} {m.why}")
        return 0
    if args.prune:
        return prune()

    head = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    dirty = subprocess.run(["git", "-C", str(ROOT), "status", "--porcelain=v1"],
                           capture_output=True, text=True).stdout.strip()
    print(f"MUTATION TEST — {len(chosen)} mutations, each in a detached worktree")
    print(f"TIP  {head}   (pinned once; every mutation sees this tree)")
    if dirty:
        print(f"🔴 {len(dirty.splitlines())} uncommitted path(s) — they are NOT in the "
              "worktrees below, so this run judges the committed tree, not yours")
    print()
    survivors, broken = [], []
    for m in chosen:
        verdict, detail = apply_and_run(m, head)
        print(f"{verdict:<16} {m.name}  {m.why}")
        if verdict == "SURVIVED":
            survivors.append(m)
            print(f"{'':<16}   🔴 {detail}")
        elif verdict not in ("KILLED",):
            broken.append(m)
            print(f"{'':<16}   ⚠️  {detail}")

    print()
    print(f"KILLED    {len(chosen) - len(survivors) - len(broken)}/{len(chosen)}")
    if broken:
        print(f"UNUSABLE  {len(broken)} — the anchor moved; the mutation was never applied, "
              "which is NOT a pass")
        for m in broken:
            print(f"          {m.name} {m.target}")
    if survivors:
        print(f"SURVIVED  {len(survivors)} — each is a hole in the tests:")
        for m in survivors:
            print(f"          {m.name} {m.why}")
    return 1 if (survivors or broken) else 0


if __name__ == "__main__":
    sys.exit(main())
