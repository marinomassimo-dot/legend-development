"""SCI44: apply the V1 verifier's corrections to the producers' tables. Each edited cell keeps its text and gains a bracketed '[V1 correction: ...]' note (a few exact replacements are listed as such);
every edit is logged in CORRECTIONS_V1.tsv. Idempotent: a cell that already carries the note is not edited again.
  python3 apply_v1_corrections.py"""
import csv, sys
from pathlib import Path
H = Path(__file__).resolve().parent
EDITS = [  # file, id column, row id, column to edit, note, optional (old, new)
 ("decisive.tsv","prop_id","D02","statement","HPA single-nucleus numbers are the cluster-type aggregate of 34 supercluster types pooled over 11 brain regions (Siletti 2023, three postmortem donors), not cortex; cortex-only region values give the same ranking (neurons PDK3 59.6-121.1, PDK2 16.2-31.4, PDK4 0.0-2.6 nCPM). 'AZD7545 has no recorded PDK3 or PDK4 row' means the repository has none: Kato 2007 measured PDK3 (IC50 0.60 uM with core; 10-fold stimulation without core)",None),
 ("decisive.tsv","prop_id","D03","statement","the rise of PDK4 with maturation holds for human only; the mouse series in the same GEO table goes the other way (adult astrocytes Pdk2 above Pdk4)",None),
 ("decisive.tsv","prop_id","D05","statement","species and preparation are confounded; two human datasets differ 3-8 fold for macrophage/myeloid PDK4 (192.5 FPKM immunopanned; 22.6 nCPM snRNA aggregate; 57.9 cortex-only), so 'differ by species' is not established",None),
 ("decisive.tsv","prop_id","D09","statement","n = 5 sham and 8 seizure holds for Methods and the behaviour panel; blot panels n = 3 or 4; staining panels n = 4 sham and 5-7 seizure; the percentages come from the blot and staining panels",None),
 ("decisive.tsv","prop_id","D15","statement","44 PubMed hits, 25 screened; the unscreened records add isoform-specific neural genetic work (see verify/v1/audit.md section 6; title or abstract level only)",None),
 ("a3/decisive.tsv","prop_id","A3D02","statement","'dual-role' is the authors' word for PDK3 only; PDK1 core-free 1.3-fold is called marginal (mean of two experiments, one concentration); PDK2 was not tested in the paper; the authors expect inhibition in situ because PDK3 is scaffold-bound",None),
 ("a3/decisive.tsv","prop_id","A3D05","statement","justified for PDK4 only (core-free stimulation, no core-bound measurement); for PDK3 the measured core-bound inhibition (IC50 0.60 uM, 31% residual at 10 uM) may be recorded with its condition and the 10-fold core-free stimulation; not comparable with the 2003 PDK1 value",None),
 ("a3/decisive.tsv","prop_id","A3D06","statement","three truncated His-tagged constructs and one full-length (PDK-4, residues 1-412); PDK-4 enzyme 20 nM against 10 nM for the others; species unnamed (a residue-range hint of human PDK-1 and rodent PDK-4 is INFERENZA of the verifier)",None),
 ("a3/decisive.tsv","prop_id","A3D07","statement","the 138-148% PDH activity is read off a raster bar: INFERENZA, not DATO",None),
 ("a3/decisive.tsv","prop_id","A3D09","statement","adds PDK4: 0.25 mM DCA lowers core-free kcat from 35.1 to 2.6 per min (Wynn 2008 Table 3); 'rat-isoenzyme' for the 1998 Ki is an inference, not in the abstract",None),
 ("a3/decisive.tsv","prop_id","A3D10","statement","'closes the kinase' belongs to the PDK2 and PDK4 structures, not to the PDK1 structure of Kato 2007",None),
 ("a3/decisive.tsv","prop_id","A3D11","statement","CHEMBL257158 is GlcNAc-thiazoline (sulfur, C8H13NO4S), not the selenazoline; the conclusion (PDK1 means PDPK1) is unchanged",None),
 ("a3/symbol_check.tsv","row","SC02","compound","CHEMBL257158 is GlcNAc-thiazoline (sulfur), not the selenazoline",("selenazoline","thiazoline [V1: ChEMBL formula C8H13NO4S]")),
 ("a3/evidence.tsv","ev_id","EV10","locator_quote","IC50 subscript restored",("ICvalue","IC50 value")),
 ("a3/evidence.tsv","ev_id","EV11","locator_quote","IC50 subscript restored",("ICvalues","IC50 values")),
]
def main():
    log = []
    for f, idc, rid, col, note, rep in EDITS:
        p = H / f
        with open(p, encoding="utf-8", newline="") as fh:
            rows = list(csv.reader(fh, delimiter="\t"))
        hdr = rows[0]; ci = hdr.index(col); ii = hdr.index(idc); done = False
        for r in rows[1:]:
            if r[ii] == rid:
                if "[V1 correction" in r[ci]: done = True; break
                old = r[ci]
                if rep and rep[0] in r[ci]: r[ci] = r[ci].replace(rep[0], rep[1])
                r[ci] = r[ci] + f" [V1 correction: {note}]"
                log.append([f, rid, col, note]); done = True; break
        if not done: log.append([f, rid, col, "ROW NOT FOUND"])
        with open(p, "w", encoding="utf-8", newline="") as fh:
            csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(rows)
    with open(H / "CORRECTIONS_V1.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["file", "row", "column", "correction"]); w.writerows(log)
    print(len(log), "edits;", sum(1 for x in log if x[3] == "ROW NOT FOUND"), "rows not found")
if __name__ == "__main__":
    if len(sys.argv) > 1: print(__doc__)
    else: main()
