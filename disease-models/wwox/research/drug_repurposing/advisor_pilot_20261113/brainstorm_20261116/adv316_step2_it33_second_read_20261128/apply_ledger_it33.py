"""IT33: DL-MECH-159 causal statement, exact-once replacement. Run from the repository root."""
from pathlib import Path
P = Path("disease-models/wwox/research/discovery_ledger_current.md")
old = "[[paper_registry_current#PAPER 362]] (no marker row in the fractionation blot)"
new = "[[paper_registry_current#PAPER 362]] (Fig 4C an alpha-tubulin row under the cytosol lanes only and Fig 4D a cytochrome C row under the mitochondria lanes that is faint in Control, 0 and 1 h and strong at 2 and 3 h by eye; no blot carries both, and no n is stated for either)"
t = P.read_text(encoding="utf-8")
assert t.count(old) == 1, t.count(old)
P.write_text(t.replace(old, new, 1), encoding="utf-8"); print("ok")
