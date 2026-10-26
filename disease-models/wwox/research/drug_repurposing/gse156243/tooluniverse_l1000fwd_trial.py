#!/usr/bin/env python3
"""ToolUniverse capability test (scientist-c, 2026-10-26): the L1000FWD reversal search for the declared GSE156243 gene sets S1, S0 and the direction-shuffled S1P, S1P2.
Run ONLY inside an isolated environment that has `tooluniverse` installed (1.5.7 was used; nothing is installed in the repository):
  <venv>/bin/python -I tooluniverse_l1000fwd_trial.py <this directory>
Writes tool_responses/l1000fwd_via_tooluniverse_results.json. Asked for 100 results per set in 'opposite' mode; the tool returned 50 (see tooluniverse_capability_test_20261026.md)."""
import sys as _sys
if any(a in ("-h", "--help") for a in _sys.argv[1:]):  # answers --help without network, install or writes
    print(__doc__)
    raise SystemExit(0)
import json, sys
from tooluniverse import ToolUniverse
G = sys.argv[1]
tu = ToolUniverse(); tu.load_tools()
q = json.load(open(G + "/derived/query_sets.json"))
sets = {"S1": q["S1"], "S0": q["S0"], "S1P": json.load(open(G + "/derived/query_sets_S1P.json"))["S1P"], "S1P2": json.load(open(G + "/derived/query_sets_S1P2.json"))["S1P2"]}
out = {k: tu.run({"name": "L1000FWD_sig_search", "arguments": {"up_genes": v["up"], "down_genes": v["down"], "n_results": 100, "mode": "opposite"}}) for k, v in sets.items()}
json.dump(out, open(G + "/tool_responses/l1000fwd_via_tooluniverse_results.json", "w"))
