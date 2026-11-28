"""IT30: apply the ADV-302 and ADV-309 fragments by exact-once replacement (ledger, map, therapeutic-hypotheses ledger, disease_model.md). The record-scoped ops (claim registry, working model) go through batch_commit.py propagate. Run from the repository root; --dry writes nothing."""
import importlib.util, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
dry = "--dry" in sys.argv
def load(name):
    spec = importlib.util.spec_from_file_location("m", HERE / name); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
frags = load("edits_302_it30.py").X + load("edits_ledger_w309_it30.py").X
o = json.loads((HERE / "ops_disease_model_it30.json").read_text(encoding="utf-8"))[0]
frags.append({"path": "disease-models/wwox/disease_model.md", "tag": "retraction-ADD", "old": o["old"], "new": o["new"]})
texts = {}
for e in frags:
    t = texts.setdefault(e["path"], Path(e["path"]).read_text(encoding="utf-8"))
    n = t.count(e["old"])
    if n != 1:
        if t.count(e["new"]) == 1: print("already", e["tag"]); continue
        raise SystemExit(f"COUNT {n} for {e['tag']} in {e['path']}")
    texts[e["path"]] = t.replace(e["old"], e["new"], 1)
    print("ok", e["tag"].split()[0])
if not dry:
    for p, t in texts.items(): Path(p).write_text(t, encoding="utf-8")
print("fragments", len(frags), "dry" if dry else "applied")
