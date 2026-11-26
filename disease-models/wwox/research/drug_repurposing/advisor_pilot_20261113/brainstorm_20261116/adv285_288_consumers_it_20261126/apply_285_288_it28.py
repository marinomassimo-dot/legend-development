"""IT28: apply edits_285_288_it28.py to the pup brief, the current pup text, the slice package, the two ordering pages and INV-06 (tsv). Idempotent."""
import importlib.util, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
DR = HERE.parents[2]  # .../drug_repurposing
spec = importlib.util.spec_from_file_location("e", HERE / "edits_285_288_it28.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
EB = DR / "experiment_brief_presidio013_sci_20261116"
JOBS = [
 (EB / "v2_consolidated_sci_20261119/PUP_BRIEF_V2_CONSOLIDATED.md", [(E.F_OLD_PUP, E.F_NEW_PUP), (E.G_OLD_PUP, E.G_OLD_PUP + E.G_ADD)]),
 (EB / "current_text_adv143_it_20261121/PUP_BRIEF_CURRENT_IT_20261121.md", [(E.F_OLD_PUP, E.F_NEW_PUP), (E.G_OLD_PUP, E.G_OLD_PUP + E.G_ADD)]),
 (EB / "v2_consolidated_sci_20261119/SLICE_PACKAGE_V2_CONSOLIDATED.md", [(E.F_OLD_SLICE, E.F_NEW_SLICE), (E.G_OLD_SLICE, E.G_OLD_SLICE + E.G_ADD)]),
 (EB / "v2_consolidated_sci_20261119/ORDERING_PAGE.md", [(E.ROW_OLD, E.ROW_NEW)]),
 (DR / "advisor_pilot_20261113/brainstorm_20261116/materials_test2_sci_20261119/ORDERING_PAGE_COPY_WITH_ONE_SLOT_LINE_SCI_20261119.md", [(E.ROW_OLD, E.ROW_NEW)]),
]
dry = "--dry" in sys.argv
for p, pairs in JOBS:
    t = p.read_text(encoding="utf-8")
    for old, new in pairs:
        if new in t: print("already", p.name, old[:30]); continue
        assert t.count(old) == 1, (p.name, old[:40], t.count(old))
        t = t.replace(old, new); print("replace", p.name, old[:30])
    if not dry: p.write_text(t, encoding="utf-8")
def inv_tsv(p):
    L = p.read_text(encoding="utf-8").split("\n"); h = L[0].split("\t"); c = h.index("evidence_available"); k = h.index("inv_id"); n = 0
    for i, l in enumerate(L):
        f = l.split("\t")
        if i and len(f) == len(h) and f[k] == "INV-06" and E.INV06_NOTE.strip() not in f[c]:
            f[c] = f[c].rstrip() + E.INV06_NOTE; L[i] = "\t".join(f); n += 1
    if not dry: p.write_text("\n".join(L), encoding="utf-8")
    return n
RK = DR / "ranking_it8_p9_20261029"
print("INV-06 tsv", inv_tsv(RK / "investigations.tsv"), inv_tsv(RK / "investigations_it20.tsv"))
