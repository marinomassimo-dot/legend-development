"""IT47 P4/P5: two dated clauses on live investigation cards. INV-09 receives what the generator now reads from the GSK3 / eIF2B hypotheses package (prerequisites, epistasis caveats, a probe with an engagement control, the null stated first);
INV-10 receives the separation of evidence layers for antiseizure drugs. Idempotent (markers).  python3 apply_it47_cards.py [--check]"""
import csv, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
G = ("[IT47 package] Hypotheses read by the generator from the GSK3 and eIF2B package (five rows, no direction asserted, no repurposing candidate named): before any compound arm, the baseline of eIF2B epsilon Ser535 phosphorylation (human Ser540) with total GSK3 and replicate lanes in the WWOX-deficient cells against corrected controls; "
     "the isoform (beta or alpha) by genetic knock-down; a phospho-resistant epsilon (Ser to Ala) and a catalytically dead epsilon as epistasis, with two limits found by the independent reader: Ser to Ala cannot separate GSK3 from DYRK2 acting at the priming serine, and the catalytically dead form needs its own control in tissue with intact Gsk3b; "
     "an eIF2B activator only as a discriminating probe, with an engagement control; the null (the GSK3 route is not engaged) stated before the measurement. Lithium stays a labelled non-specific comparator. Source: generation_it47_20261112/p4_gsk3/result_it47.md.")
A = ("[IT47 layers] For any antiseizure drug named on this thread three layers are kept apart: clinical evidence (what is recorded in children with WWOX-related disease; here single reports without an instrument), preclinical rationale (what an experiment in a WWOX model shows) and untested hypothesis (a mechanism proposed from outside WWOX). "
     "An antiseizure effect does not by itself support a preference or a better development; a drug already in clinical use may deserve a comparison only if a WWOX-specific rationale emerges. The order of the investigations is an investment in research, not an expected benefit for a child.")
EDITS = [("INV-09", G), ("INV-10", A)]
FILES = [DR / "ranking_it8_p9_20261029/investigations_it20.tsv", DR / "ranking_it8_p9_20261029/investigations.tsv"]


def main(check=False):
    csv.field_size_limit(10**9); changed = 0
    for f in FILES:
        rows = list(csv.reader(open(f, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; i, c = h.index("inv_id"), h.index("next_test")
        for r in rows[1:]:
            for inv, txt in EDITS:
                if r[i] == inv and txt.split("]")[0] + "]" not in r[c]:
                    r[c] = (r[c] + " " + txt).strip(); changed += 1
        if not check:
            csv.writer(open(f, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    print(("would change " if check else "changed ") + str(changed))


if __name__ == "__main__":
    main("--check" in sys.argv)
