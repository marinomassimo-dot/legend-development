"""SCI44: apply the V2 verifier's corrections to the producers' tables. Each edited cell keeps its text and gains a bracketed '[V2 correction: ...]' note (a few exact replacements are listed as such);
every edit is logged in CORRECTIONS_V2.tsv. Idempotent: a cell that already carries the note is not edited again.
  python3 apply_v2_corrections.py"""
import csv, sys
from pathlib import Path
H = Path(__file__).resolve().parent
EDITS = [
 ("a4/decisive.tsv","prop_id","A4D04","statement","the Vm/Rin null (13 vs 12 neurons) is the GFAP-Cre conditional knockout, which acts in neural progenitors (neurons and astrocytes), not an adult astrocyte-specific deletion; the astrocyte-specific AAV arm (12 vs 13 neurons) reports firing and lactate only",None),
 ("a4/decisive.tsv","prop_id","A4D10","statement","'without changing wild type' means not significant only; the wild-type glibenclamide means in the figure are higher (raster read, INFERENZA); 'almost completely inactive' is the authors' inference for juvenile dentate cells",None),
 ("a4/decisive.tsv","prop_id","A4D11","statement","attribution as A4D04 (GFAP-Cre conditional knockout); fAHP difference is 2.27 mV (8.30 vs 6.02, Source Data Fig 7f), not about 2.6; lactate arm: 15 neurons, 5 mice, Vm -66.0 vs -66.6 mV, Rin 0.161 vs 0.156 GOhm, 4 mM Mg-ATP pipette, slices at 24 C",None),
 ("a4/decisive.tsv","prop_id","A4D12","statement","NOT SUPPORTED as an absence claim: it holds only for the producers' read set. Counter-examples: Karagiannis 2021 (34766906, text read by the verifier; juvenile rat and mouse barrel cortex, layers I-IV: KATP modulators change membrane potential, resistance and firing; diazoxide roughly doubles whole-cell conductance; in perforated patch 15 mM lactate with 2.5 mM glucose roughly doubles firing, absent in Kcnj11-/-; pooled across cell types) and abstract-only 42263507, 42574076, 35188099, 19943846",None),
 ("a4/decisive.tsv","prop_id","A4D13","statement","'opposite to PDH release' is the producer's inference, not the source's",None),
 ("a4/decisive.tsv","prop_id","A4D14","statement","the clause 'no acetate test found' is refuted by 30787166 (PDH-deficient mouse, acetate partly rescues the deficits; abstract only); the Table 3 header n is 7, 8, 7, 6, not '7-9'",None),
 ("a4/k_coupling.tsv","row_id","K01","temperature","Methods state room temperature",None),
 ("a4/k_coupling.tsv","row_id","K03","temperature","Methods state room temperature",None),
 ("a4/k_coupling.tsv","row_id","K05","manipulation","GFAP-Cre conditional knockout (neural progenitor origin), not an adult astrocyte-specific deletion",None),
 ("a4/levers.tsv","row_id","L02","n","text gives 5 animals and 7 slices for the dF/F population",None),
 ("a4/levers.tsv","row_id","L06","tool_or_class","GFAP-Cre conditional knockout, not 'astrocyte-targeted' (see A4D04)",None),
 ("a4/evidence.tsv","ev_id","EV13","locator_quote","punctuation differs from the source",None),
 ("a4/evidence.tsv","ev_id","EV15","locator_quote","drops the word 'it'; 27 words, over the 25-word limit",None),
 ("decisive.tsv","prop_id","D09","statement","Fig 6 legend gives n = 4 per sham group and 5-7 per seizure group; the single-agent arms exist and only DCA plus pyruvate is significant (Fig 6 viewed by the verifier)",None),
 ("decisive.tsv","prop_id","D11","statement","the abstract's 'PDK2 low in neurons' is not contradicted by the mouse P7 table (different species, age and metric; a 20 percent difference between two pools each); independent data cut against the abstract: 11197747 (PDK2 mRNA the most abundant isoform in rat brain regions) and 37188779 (neuron-specific PDK2 silencing in vivo, mouse), both abstract level; so 'no isoform-selective loss was found in neurons' is not supported",None),
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
                if "[V2 correction" in r[ci]: done = True; break
                old = r[ci]
                if rep and rep[0] in r[ci]: r[ci] = r[ci].replace(rep[0], rep[1])
                r[ci] = r[ci] + f" [V2 correction: {note}]"
                log.append([f, rid, col, note]); done = True; break
        if not done: log.append([f, rid, col, "ROW NOT FOUND"])
        with open(p, "w", encoding="utf-8", newline="") as fh:
            csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(rows)
    with open(H / "CORRECTIONS_V2.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["file", "row", "column", "correction"]); w.writerows(log)
    print(len(log), "edits;", sum(1 for x in log if x[3] == "ROW NOT FOUND"), "rows not found")
if __name__ == "__main__":
    if len(sys.argv) > 1: print(__doc__)
    else: main()
