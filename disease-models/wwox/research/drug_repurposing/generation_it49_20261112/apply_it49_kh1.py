"""IT49: the three SCI43 corrections of IT48 made explicit on KH1 (dated clause on the premise cell; idempotent; the original text stays)."""
import csv, sys
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
TXT = ("[IT49 update] Three limits travel with this row. (1) A Ba2+ response does not identify Kir2: 60 uM Ba2+ blocks Kir2-type channels, K2P-type leak channels and astroglial Kir4.1 alike. "
       "(2) Shares measured in different preparations or cohorts (here the Ba2+ and the Ih panels, different cells) are not additive and are not a decomposition of one resting conductance. "
       "(3) No measurement exists in the pertinent age band and layer (about P13-P17, layer II/III): the premise is unresolved, neither supported nor refuted, and the 23 percent figure is a transfer from an older age.")
def main(check=False):
    csv.field_size_limit(10**9)
    f = DR / "potassium_conductances_sci43_20261110/output/hypotheses.tsv"
    rows = list(csv.reader(open(f, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; n = 0
    i, c = h.index("hyp_id"), h.index("premise")
    for r in rows[1:]:
        if r[i] == "KH1" and "[IT49 update]" not in r[c]:
            r[c] = (r[c] + " " + TXT).strip(); n += 1
    if not check and n: csv.writer(open(f, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    print(("would change " if check else "changed ") + str(n))
if __name__ == "__main__":
    main("--check" in sys.argv)
