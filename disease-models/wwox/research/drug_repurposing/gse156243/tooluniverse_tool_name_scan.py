#!/usr/bin/env python3
"""Lists the ToolUniverse tool names that contain clue, lincs, sigcom, ilincs, l1000, cmap or enrichr, plus the installed version, so the claim
'no CLUE tool in 1.5.7' is checkable. Run ONLY in an isolated environment that has `tooluniverse` installed:
  <venv>/bin/python -I tooluniverse_tool_name_scan.py > tool_responses/tooluniverse_1.5.7_tool_name_scan.txt"""
import sys as _sys
if any(a in ("-h", "--help") for a in _sys.argv[1:]):  # answers --help without any install, network or write
    print(__doc__)
    raise SystemExit(0)
import importlib.metadata as md
from tooluniverse import ToolUniverse
tu = ToolUniverse(); tu.load_tools()
names = sorted(tu.all_tool_dict)
hits = [k for k in names if any(s in k.lower() for s in ("clue", "lincs", "sigcom", "ilincs", "l1000", "cmap", "enrichr"))]
print("tooluniverse", md.version("tooluniverse"), "tools", len(names))
print("matches", len(hits))
for k in hits:
    print(k)
print("names containing 'clue':", [k for k in names if "clue" in k.lower()])
