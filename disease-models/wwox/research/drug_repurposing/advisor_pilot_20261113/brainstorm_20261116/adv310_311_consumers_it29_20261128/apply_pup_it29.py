"""IT29: apply edits_it29b.py to the live pup brief by exact-once fragments. --dry writes nothing. Run from the repository root."""
import importlib.util, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("e", HERE / "edits_it29b.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
B = Path("disease-models/wwox/research/drug_repurposing/experiment_brief_presidio013_sci_20261116/current_text_adv143_it_20261121/PUP_BRIEF_CURRENT_IT_20261121.md")
t = B.read_text(encoding="utf-8")
for x in E.X:
    n = t.count(x["old"])
    if n != 1:
        if x["new"] in t: print("already", x["tag"]); continue
        raise SystemExit(f"COUNT {n} for {x['tag']}")
    t = t.replace(x["old"], x["new"], 1)
if "--dry" not in sys.argv: B.write_text(t, encoding="utf-8")
print("fragments", len(E.X), "dry" if "--dry" in sys.argv else "applied")
