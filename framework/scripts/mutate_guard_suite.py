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
        "M03", GUARD_POLICY,
        "    if underivable:\n        return UNDERIVABLE, DENY_UNDERIVABLE, findings",
        "    if underivable:\n        return ALLOWED, None, findings",
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
        "M11", GUARD_POLICY,
        "    if in_repo:\n        return PROHIBITED, DENY_SHELL_WRITE, findings",
        "    if False:\n        return PROHIBITED, DENY_SHELL_WRITE, findings",
        GUARD_SUITES, "a derived in-repository write stops being prohibited"),
    Mutation(
        "M12", GUARD_POLICY,
        "    if unnamed:\n        return PROHIBITED, DENY_UNNAMED, findings",
        "    if False:\n        return PROHIBITED, DENY_UNNAMED, findings",
        GUARD_SUITES, "a write whose target is never named is allowed"),

    # ── the adapter ───────────────────────────────────────────────────────────────
    Mutation(
        "M13", GUARD_ENTRY,
        "        raise Undecidable(\n            f\"`{tool_name}` is not a tool this guard knows.",
        "        return None\n        raise Undecidable(\n            f\"`{tool_name}` is not a tool this guard knows.",
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
    Mutation(
        "M26", PARITY,
        "    body = text.split(\"[hooks]\", 1)[-1] if \"[hooks]\" in text else text\n    return set(MATCHER_LINE.findall(body))",
        "    return set(re.findall(r'[a-z_]+', text))",
        PARITY_SUITES, "matchers are matched as substrings again, so `exec` inside "
                       "`unified_exec` counts as a declaration"),
]


def apply_and_run(mutation, keep_going=True):
    tmp = Path(tempfile.mkdtemp(prefix=f"mutate-{mutation.name}-"))
    tree = tmp / "tree"
    head = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
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

    print(f"MUTATION TEST — {len(chosen)} mutations, each in a detached worktree at HEAD\n")
    survivors, broken = [], []
    for m in chosen:
        verdict, detail = apply_and_run(m)
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
