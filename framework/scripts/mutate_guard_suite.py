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

GUARD_SUITES = ("framework/scripts/test_pre_tool_use_guard.py",
                "scripts/test_guard_bash_command.py")
PARITY_SUITES = ("framework/scripts/test_runtime_parity.py",)


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
        GUARD_SUITES,
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
        "M15", GUARD_ENTRY,
        "    for command in commands:\n        reason = guard_policy.verdict(command, cwd=cwd, repo_root=root)",
        "    for command in commands[:1]:\n        reason = guard_policy.verdict(command, cwd=cwd, repo_root=root)",
        GUARD_SUITES, "only the first shell call in a code-mode body is judged"),
    Mutation(
        "M16", GUARD_ENTRY,
        '        commands = ["apply_patch <<\'PATCH\'\\n" + program_text(tool_input) + "\\nPATCH"]',
        "        commands = []",
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
        GUARD_SUITES,
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--only", default=None)
    args = parser.parse_args()

    chosen = [m for m in MUTATIONS if not args.only or m.name == args.only]
    if args.list:
        for m in chosen:
            print(f"{m.name}  {Path(m.target).name:<26} {m.why}")
        return 0

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
