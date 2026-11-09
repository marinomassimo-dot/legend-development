"""IT41 P7: same case (S1, GluN2B-directed negative modulation), same universe, three paths. Counts only; no score; no predictive claim."""
import csv, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
def tsv(p): return list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))
rows = [r for r in tsv(HERE / "search_rows.tsv") if r["relation_id"] == "S1"]
ch = [r for r in rows if r["source"].startswith("ChEMBL")]; gt = [r for r in rows if r["source"].startswith("GtoPdb")]
mol = lambda rs: len({r["molecule"] for r in rs})
ortho = [r for r in gt if r["site_or_granularity"] in ("glutamate site", "glycine site")]
chan = [r for r in gt if r["action"].startswith("Channel blocker")]
nam = [r for r in gt if r["action"].startswith(("Allosteric modulator/Negative", "None/Inhibition"))]
assembly = [r for r in ch if r["site_or_granularity"] == "two_gene_assembly_record"]
out = [
 ["molecules a symbol lookup of GRIN2B returns (ChEMBL mechanisms only, previous path and baseline)", mol(ch), "", ""],
 ["molecules after adding the GtoPdb interaction table (same symbol)", "", mol(rows), ""],
 ["of which orthosteric (glutamate- or glycine-site) ligands, not modulators of the ifenprodil kind", "", "", mol(ortho)],
 ["of which channel blockers", "", "", mol(chan)],
 ["molecules documented as GluN2B-directed negative modulators (two-gene assembly record)", mol(assembly), "", mol(assembly)],
 ["additional documented negative modulators from the GtoPdb table (same species context stated)", 0, 0, mol(nam)],
 ["rows whose assay was on another subunit than the target they sit under (transfer avoided)", "not seen", "not seen", sum(1 for r in nam if "GluN2C" in r["assay_or_note"])],
 ["compounds that entered the comparison as emerged (not previously discussed as comparators)", 0, 0, 2],
]
with open(HERE / "measure_it41.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["measure", "previous path (ChEMBL mechanism, symbol)", "simple baseline (symbol, both tables)", "IT41 path (action, site, species, assay text)"]); w.writerows(out)
for o in out: print(" | ".join(str(x) for x in o)[:200])
