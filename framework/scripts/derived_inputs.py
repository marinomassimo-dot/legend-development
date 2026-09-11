#!/usr/bin/env python3
"""Bind a derived surface to identifiable, committed inputs — or refuse to derive it.

WHY THIS EXISTS
---------------
On 2026-09-09 (retrospective C22) `scientist-c` regenerated the shared derived surfaces —
`batch_queue.md`, `coverage_report.md`, `reading_state.md`, the pathograph inventory and
export — in the middle of a wave, and the regeneration baked in two peers' UNCOMMITTED
manifests. The actor noticed and reverted rather than land three actors' in-flight state
under its own name. Nothing in the generators had refused; the only control was the actor's
attention, and the orchestrator's wave-close commit (`a8a6a1d`) had to state in prose that
"the tree holds no actor's in-flight work, so the surfaces now re-derive from committed state
only". A property that has to be asserted in a commit message is a property nobody checks.

This module is the check. A generator that is about to WRITE a surface asks for the git state
of the inputs it reads; if any input is modified or untracked in the working tree, the write
is refused with the list — because on a shared checkout a dirty input is, until proven
otherwise, somebody else's unfinished work — unless the caller states in one sentence why it
is safe (`--inputs-dirty-because`). The one ordinary legitimate case is `BATCH_COMMIT` phase
4.7, where the dirty registries are the batch's own edits and land in the same commit as the
surface; the protocol passes the reason explicitly, so a reader of the transcript sees it.

WHAT IT CANNOT ESTABLISH
------------------------
- Whose the dirty file is. Git records no actor for an uncommitted change. The refusal names
  the file; the reader decides.
- Anything outside git. A workspace that is not a git repository is UNBOUND: the generator
  proceeds and says so on stderr, because the suites build their fixtures in plain temporary
  directories and a guard that broke every generator test would be removed the same day.
  UNBOUND is a named state, never a pass.
- Semantic staleness. A committed input can still be wrong; this binds the derivation to a
  commit, it does not audit the commit.

    state = derived_inputs.input_state(root, [registries_dir, manifest_dir], exclude=[out])
    code = derived_inputs.refuse_if_dirty(state, reason=args.inputs_dirty_because)
    if code is not None:
        return code
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

BOUND = "BOUND"        # every input is committed; HEAD identifies the derivation's sources
DIRTY = "DIRTY"        # at least one input is modified or untracked in the working tree
UNBOUND = "UNBOUND"    # not a git repository; the binding cannot be made and is not claimed

# Surfaces that are themselves generated live beside their inputs (the registries directory
# holds coverage_report.md, batch_queue.md and reading_state.md). Regenerating one of them
# after another must not read the earlier output as a dirty input.
GENERATED_SIBLINGS = ("coverage_report.md", "batch_queue.md", "reading_state.md",
                      "surface_census.md", "pathograph_inventory.md", "pathograph_export.jsonl")

FLAG = "--inputs-dirty-because"


@dataclass
class InputState:
    verdict: str
    head: str = ""
    inputs: list[str] = field(default_factory=list)
    dirty: list[tuple[str, str]] = field(default_factory=list)  # (status, path)
    detail: str = ""

    @property
    def is_dirty(self) -> bool:
        return self.verdict == DIRTY


def _git(cwd: Path, *args: str) -> str | None:
    try:
        done = subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True)
    except OSError:
        return None
    return done.stdout if done.returncode == 0 else None


def input_state(root: Path, inputs: list[Path], *, exclude: list[Path] | None = None) -> InputState:
    """The git state of ``inputs`` (files or directories) under ``root``.

    ``exclude`` names paths whose dirtiness is not an input problem — the surface being
    written, and its generated siblings. Everything else modified, staged, or untracked under
    an input is DIRTY.
    """
    root = Path(root).resolve()
    top = _git(root, "rev-parse", "--show-toplevel")
    if not top:
        return InputState(UNBOUND, detail=f"{root} is not inside a git repository")
    top_path = Path(top.strip()).resolve()
    head = (_git(top_path, "rev-parse", "HEAD") or "").strip() or "UNBORN"
    excluded = {Path(p).resolve() for p in (exclude or [])}
    present = [Path(p).resolve() for p in inputs if Path(p).exists()]
    rel_inputs = []
    for path in present:
        try:
            rel_inputs.append(str(path.relative_to(top_path)))
        except ValueError:
            continue
    if not rel_inputs:
        return InputState(UNBOUND, head=head,
                          detail="none of the declared inputs exists inside the repository")
    porcelain = _git(top_path, "status", "--porcelain", "--untracked-files=all", "--", *rel_inputs)
    if porcelain is None:
        return InputState(UNBOUND, head=head, detail="git status failed")
    dirty: list[tuple[str, str]] = []
    for line in porcelain.splitlines():
        if len(line) < 4:
            continue
        status, rel = line[:2], line[3:]
        if " -> " in rel:
            rel = rel.split(" -> ", 1)[1]
        absolute = (top_path / rel).resolve()
        if absolute in excluded or absolute.name in GENERATED_SIBLINGS:
            continue
        dirty.append((status.strip() or "?", rel))
    return InputState(DIRTY if dirty else BOUND, head=head, inputs=rel_inputs, dirty=dirty)


def refuse_if_dirty(state: InputState, *, reason: str | None, surface: str = "",
                    stream=None) -> int | None:
    """Exit code 2 to refuse, or None to proceed. Says which of the three states it saw."""
    stream = stream or sys.stderr
    label = f" for {surface}" if surface else ""
    if state.verdict == UNBOUND:
        print(f"inputs UNBOUND{label}: {state.detail}; the derivation is not bound to a commit",
              file=stream)
        return None
    if state.verdict == BOUND:
        print(f"inputs BOUND{label}: {len(state.inputs)} input path(s) committed at {state.head[:12]}",
              file=stream)
        return None
    listing = "\n".join(f"    {status:>2}  {rel}" for status, rel in state.dirty[:40])
    more = f"\n    … and {len(state.dirty) - 40} more" if len(state.dirty) > 40 else ""
    if reason and reason.strip():
        print(f"inputs DIRTY{label}, proceeding because: {reason.strip()}\n"
              f"  {len(state.dirty)} uncommitted input(s) at HEAD {state.head[:12]}:\n{listing}{more}",
              file=stream)
        return None
    print(f"REFUSED{label}: {len(state.dirty)} input(s) are uncommitted in the working tree, "
          f"and on a shared checkout an uncommitted input is somebody's unfinished work until "
          f"proven otherwise (2026-09-09 C22). Commit or wait, or state why it is safe with "
          f"{FLAG} \"<reason>\".\n{listing}{more}", file=stream)
    return 2


def add_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(FLAG, dest="inputs_dirty_because", default="", metavar="REASON",
                        help="derive even though some inputs are uncommitted, for the stated "
                             "reason (BATCH_COMMIT phase 4.7 is the ordinary one)")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=".")
    parser.add_argument("inputs", nargs="+", help="files or directories the derivation reads")
    parser.add_argument("--exclude", action="append", default=[])
    add_argument(parser)
    args = parser.parse_args(argv)
    root = Path(args.root)
    state = input_state(root, [root / p for p in args.inputs], exclude=[root / p for p in args.exclude])
    code = refuse_if_dirty(state, reason=args.inputs_dirty_because)
    print(state.verdict)
    return code or 0


if __name__ == "__main__":
    sys.exit(main())
