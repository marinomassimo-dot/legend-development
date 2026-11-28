"""IT29: apply edits_it29.py (exact-once fragments; G01 target_expression in packet and card). Idempotent; --dry writes nothing. Run from the repository root."""
import importlib.util, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("e", HERE / "edits_it29.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
dry = "--dry" in sys.argv
def rep(path, old, new, expect, tag):
    p = Path(path); t = p.read_text(encoding="utf-8")
    if new in t and old not in t: print("  already", tag, path); return
    n = t.count(old)
    if n != expect: raise SystemExit(f"COUNT {n} (expected {expect}) for {tag} in {path}")
    if not dry: p.write_text(t.replace(old, new), encoding="utf-8")
    print("  ", tag, path, "occurrences", n)
for x in E.X: rep(x["path"], x["old"], x["new"], 1, x["tag"])
for g in E.G01_FILES: rep(g, E.G01_OLD, E.G01_NEW, 2 if g.endswith("card.json") else 1, "G01")
