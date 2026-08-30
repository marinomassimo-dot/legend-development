#!/usr/bin/env python3
"""Which guard is actually RUNNING in each worktree of this repository?

A candidate branch can only change the guard in the worktree that has it checked out.
Every other actor keeps whatever its own branch carries, and there is no mechanism in
this repository that propagates a guard across worktrees — so "revision 9 closes N
families" is a statement about one directory until every directory has it.

Measured here on 2026-08-29, against the revision-8 engine:

```text
11 worktrees   1 carries the effect-model engine   10 carry the legacy single-file guard
```

That is not a defect of revision 8; it is the ordinary consequence of branch isolation,
and it is stated because the readiness verdict depends on it. A repository-wide write
floor cannot be claimed while `GUARD_REVISION_UNIFORM` is `NO`, and nothing in a
candidate branch can make it `YES` — only a merge can.

🔴 **Read-only, and deliberately so.** This module hashes and reports; it never writes
into a worktree it did not start in. Upgrading a peer's guard from here would be the
cross-worktree write that `repo_topology.py` exists to forbid, performed by the tool that
measures the forbidding.

## What "generation" means, and why it is not a version string

Nothing in the guard declares its own version, and adding a version constant would make
this module read a claim rather than the code. The generation is derived from the SHAPE
of the installed engine — which modules exist, and whether the policy imports the
topology — so a worktree cannot report a generation it does not structurally have.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional

LEGACY = "LEGACY"        # a single-file guard, no effect model
REV8 = "REV8"            # guard_policy + effect_model, no topology
REV9 = "REV9"            # the above, plus repository-topology confinement
REV10 = "REV10"          # the above, plus the session-bound assigned worktree
REV11 = "REV11"          # the above, plus the silence rules and the stdin repair
ABSENT = "ABSENT"        # no guard entrypoint at all
UNKNOWN = "UNKNOWN"      # an entrypoint that matches no known shape

GENERATIONS = (LEGACY, REV8, REV9, REV10, REV11, ABSENT, UNKNOWN)

#: Newest first. The survey walks this in order and takes the first generation whose
#: structural signature is present, so a worktree carrying revision 10 is never reported
#: as revision 9 merely because revision 9's signature is also there — every generation
#: is a superset of the one below it.
GENERATION_ORDER = (REV11, REV10, REV9, REV8)

#: The entry point every runtime registers, relative to a worktree root.
GUARD_ENTRY = Path("scripts/guard_bash_command.py")
#: The runtime-neutral engine, introduced in revision 8.
GUARD_POLICY = Path("framework/scripts/guard_policy.py")
GUARD_ADAPTER = Path("framework/scripts/pre_tool_use_guard.py")
#: Introduced in revision 9. Its IMPORT in the policy is what makes confinement reachable.
GUARD_TOPOLOGY = Path("framework/scripts/repo_topology.py")
#: Introduced in revision 10. Its IMPORT in the ADAPTER is what makes the assigned
#: worktree session-bound: the policy can accept an assignment all day, and it is the
#: adapter passing one that stops the model choosing it.
GUARD_SESSION_BINDING = Path("framework/scripts/session_binding.py")
GUARD_RUNTIME_CONFIG = Path("framework/scripts/runtime_config.py")

#: 🔴 The import, not the file. A worktree could carry `repo_topology.py` as an untracked
#: leftover while its policy never calls it, and a file-existence test would report REV9
#: for a guard with revision-8 behaviour. The generation has to be derived from what the
#: executing code DOES.
TOPOLOGY_IMPORT = "import repo_topology"
#: 🔴 Same rule, one revision on, and the SITE matters more here than the file did.
#: `session_binding` imported by the policy would prove nothing — the policy's default is
#: to ask the session for an assignment, and a revision-9 adapter that never passes one
#: would still leave the perimeter derived from the effective workdir. The signature is
#: therefore the ADAPTER importing it, and the adapter calling `adjudicate` with an
#: `assigned=` argument.
SESSION_BINDING_IMPORT = "import session_binding"
SESSION_BINDING_CALL = "assigned=assignment.worktree"
RUNTIME_CONFIG_IMPORT = "import runtime_config"

#: 🔴 Revision 11, and this rung had to exist or the census would go BLIND at exactly the
#: moment it matters most.
#:
#: The ladder stopped at REV10, so a worktree carrying revision 11 reported `REV10`. That
#: is not a cosmetic gap: after a merge the census would read `{LEGACY: 0, REV10: 13}` and
#: `GUARD_REVISION_UNIFORM = YES` while some trees carried REV10 and some REV11 — a family
#: closed here and open there, with the instrument that exists to say so reporting
#: uniformity. `GUARD_REVISION_UNIFORM` is the precondition on every write-floor claim in
#: this protocol, and a detector that cannot see the newest generation answers it wrongly
#: in the permissive direction.
#:
#: Two CALL SITES, following the rule this module already applies to
#: `SESSION_BINDING_CALL`: the presence of a function proves nothing if nothing invokes
#: it, and both of these repairs are exactly of the kind that can be present and
#: unreachable — which is the defect revision 11 is about.
HERESTRING_CALL = "stripped, herestrings = extract_herestrings(command)"
SILENCE_CALL = "unclassified(argv, program, findings)"


def _sha256(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return ""


def _git(cwd: str, *args: str) -> str:
    try:
        out = subprocess.run(["git", "-C", cwd, *args], capture_output=True,
                             text=True, timeout=15)
    except (OSError, subprocess.SubprocessError):
        return ""
    return out.stdout.strip() if out.returncode == 0 else ""


def worktrees(cwd: str) -> List[str]:
    listing = _git(cwd, "worktree", "list", "--porcelain")
    return [line[len("worktree "):].strip()
            for line in listing.splitlines() if line.startswith("worktree ")]


def _read(path: Path) -> Optional[str]:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def generation_of(root: Path) -> str:
    """Derive the guard generation from the shape of what is installed."""
    entry, policy = root / GUARD_ENTRY, root / GUARD_POLICY
    if not entry.is_file() and not policy.is_file():
        return ABSENT
    if not policy.is_file():
        # The single-file guard: the entry point IS the policy.
        return LEGACY if entry.is_file() else UNKNOWN
    source = _read(policy)
    if source is None:
        return UNKNOWN
    adapter = _read(root / GUARD_ADAPTER) or ""
    rev10 = (
        SESSION_BINDING_IMPORT in adapter
        and SESSION_BINDING_CALL in adapter
        and RUNTIME_CONFIG_IMPORT in source
        and (root / GUARD_SESSION_BINDING).is_file()
        and (root / GUARD_RUNTIME_CONFIG).is_file()
    )
    if rev10 and HERESTRING_CALL in source and SILENCE_CALL in source:
        return REV11
    if rev10:
        return REV10
    if TOPOLOGY_IMPORT in source and (root / GUARD_TOPOLOGY).is_file():
        return REV9
    return REV8


def actor_of(root: Path) -> str:
    """A best-effort name for whoever works here, from the directory and the branch.

    🔴 Derived, and labelled as derived everywhere it is printed. A directory name is a
    convention, not an identity: `ACTOR_ID != RUNTIME != SESSION != WORKTREE`, and this
    function knows only the last of those. It is here so a report is readable, never so
    a decision can rest on it.
    """
    return root.name


def uniformity(generations) -> str:
    """`YES` / `NO` / `UNDERIVABLE` from the set of generations found.

    🔴 A pure function so a test can drive all three answers without eleven worktrees.
    It was inline, and the only test of the UNDERIVABLE arm asserted that
    `generation_of(<empty dir>)` is `ABSENT` — true, and silent about what the SURVEY
    then does with an `ABSENT` row. A mutation that folded unreadable worktrees into the
    YES/NO answer survived, because nothing ever asked this question.

    "Not uniform" is a measurement. "One of them could not be read" is a failure to
    measure, and reporting the second as the first makes an unreadable worktree look
    like a merely stale one — which is the difference between "nine actors need a merge"
    and "one actor's tree is broken".
    """
    generations = set(generations)
    if not generations:
        return "UNDERIVABLE"
    if UNKNOWN in generations or ABSENT in generations:
        return "UNDERIVABLE"
    return "YES" if len(generations) == 1 else "NO"


def survey(cwd: str = ".") -> Dict[str, object]:
    """Every worktree, its guard, and whether they agree. Reads only."""
    roots = worktrees(cwd)
    rows: List[Dict[str, object]] = []
    for raw in roots:
        root = Path(raw)
        entry = root / GUARD_ENTRY
        policy = root / GUARD_POLICY
        generation = generation_of(root)
        rows.append({
            "worktree": str(root),
            "actor_derived_from_directory_name": actor_of(root),
            "branch": _git(raw, "branch", "--show-current") or "<detached>",
            "head": _git(raw, "rev-parse", "HEAD")[:12],
            "guard_path": str(GUARD_ENTRY) if entry.is_file() else "<absent>",
            "guard_entry_hash": _sha256(entry)[:16],
            "guard_policy_hash": _sha256(policy)[:16],
            "guard_generation": generation,
        })

    generations = {row["guard_generation"] for row in rows}
    uniform = uniformity(generations)

    return {
        "worktrees": rows,
        "generations": sorted(generations),
        "counts": {g: sum(1 for r in rows if r["guard_generation"] == g)
                   for g in sorted(generations)},
        "guard_revision_uniform": uniform,
    }


def render(report: Dict[str, object]) -> str:
    lines = [
        f"{'WORKTREE':<34} {'ACTOR*':<22} {'BRANCH':<34} {'HEAD':<13} "
        f"{'ENTRY':<17} {'POLICY':<17} GEN",
        "-" * 150,
    ]
    for row in report["worktrees"]:  # type: ignore[index]
        lines.append(
            f"{Path(str(row['worktree'])).name:<34} "
            f"{str(row['actor_derived_from_directory_name']):<22} "
            f"{str(row['branch'])[:33]:<34} {str(row['head']):<13} "
            f"{str(row['guard_entry_hash']) or '<none>':<17} "
            f"{str(row['guard_policy_hash']) or '<none>':<17} "
            f"{row['guard_generation']}")
    lines.append("")
    lines.append(f"counts                    {report['counts']}")
    lines.append(f"GUARD_REVISION_UNIFORM =  {report['guard_revision_uniform']}")
    lines.append("")
    lines.append("* ACTOR is derived from the directory name and is a convention, not an "
                 "identity. No decision rests on it.")
    if report["guard_revision_uniform"] != "YES":
        lines.append("")
        lines.append("🔴 A repository-wide write floor may NOT be claimed while this is "
                     "not YES: the worktrees below the newest generation run a different "
                     "policy, and a family closed here is open there.")
    return "\n".join(lines)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--cwd", default=".")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    report = survey(args.cwd)
    print(json.dumps(report, indent=2) if args.json else render(report))
    # 🔴 Exit 0 regardless. Non-uniformity is a FACT to report, not a failure of this
    # tool, and a non-zero exit here would make a release runner treat an accurate
    # measurement as a broken check.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
