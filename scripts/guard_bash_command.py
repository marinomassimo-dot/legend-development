#!/usr/bin/env python3
"""Claude Code's registration of the shared `PreToolUse` write guard.

This file used to *be* the guard. It is now the Claude adapter's entry point and
nothing else: the policy lives in `framework/scripts/guard_policy.py` and the payload
handling in `framework/scripts/pre_tool_use_guard.py`, both runtime-neutral, and Codex
registers the same engine. Two copies of a safety rule drift, and the drift is invisible
until the runtime that has the weaker copy is the one that runs.

The path is kept because `.claude/settings.json` names it, and moving a registered hook
path is a change to the registration, not to the guard. `verdict` is re-exported because
`scripts/test_guard_bash_command.py` asserts the policy through this module — that test
is the Claude side of the parity battery, and it should keep testing what Claude runs.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "framework" / "scripts"))

import pre_tool_use_guard  # noqa: E402
from guard_policy import verdict  # noqa: E402,F401  (re-exported: this is the entry point)

main = pre_tool_use_guard.main

if __name__ == "__main__":
    sys.exit(main())
