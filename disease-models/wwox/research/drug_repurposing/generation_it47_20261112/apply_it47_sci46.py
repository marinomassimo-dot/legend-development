"""IT47 P2: two dated clauses on live consumers after the SCI46 value table was read mechanically (assay_rows_summary.py): a correction (V19 counter) and the reading limits of RNA readouts (INV-08 next test).
Idempotent (markers "[IT47 correction]" and "[IT47 reading limits]").  python3 apply_it47_sci46.py [--check]"""
import csv, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
CORR = ("[IT47 correction] The sentence above that no neuron or astrocyte data exist for any of these compounds is too strong for the covalent class: the SCI46 value table holds abstract-level data in primary mixed neuron-astrocyte cortical cultures with an Nrf2-knockout arm for one electrophile "
        "(the knockout result of a second electrophile is not stated in the abstract), data in neurons and astrocytes without a loss arm for the two fumarates, and a neurotoxicity series for a covalent triterpenoid in a human neuronal line. For the non-covalent binder the statement stands: no primary neuron or astrocyte datum, "
        "and the one neuronal line has a partial or inadequate loss. Source: keap1_nrf2_sci46_20261111/engine/assay_rows.tsv (rows A36, A47-A53), counted by generation_it47_20261112/assay_rows_summary.py.")
LIM = ("[IT47 reading limits] RNA class means do not say what a cell can do: a low value is not an absent function, a gene readable in neurons is not thereby an NRF2-specific readout (other regulators act on each), and KEAP1 RNA in a class does not show that the protein is available to a binder. "
       "The held RNA reads Hcar2 only in microglia, so a culture without microglia is not expected to test the HCAR2 route of a fumarate unless Hcar2 protein is shown in the cells used.")
EDITS = [(DR / "generation_it41_20261109/compound_view.tsv", "item_id", "V19", "counter", CORR), (DR / "ranking_it8_p9_20261029/investigations_it20.tsv", "inv_id", "INV-08", "next_test", LIM), (DR / "ranking_it8_p9_20261029/investigations.tsv", "inv_id", "INV-08", "next_test", LIM)]


def main(check=False):
    csv.field_size_limit(10**9); changed = 0
    for f in sorted({e[0] for e in EDITS}):
        rows = list(csv.reader(open(f, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]
        for ff, idc, idv, col, txt in EDITS:
            if ff != f: continue
            i, c = h.index(idc), h.index(col); mark = txt.split("]")[0] + "]"
            for r in rows[1:]:
                if r[i] == idv and mark not in r[c]:
                    r[c] = (r[c] + " " + txt).strip(); changed += 1
        if not check:
            csv.writer(open(f, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    print(("would change " if check else "changed ") + str(changed))


if __name__ == "__main__":
    main("--check" in sys.argv)
