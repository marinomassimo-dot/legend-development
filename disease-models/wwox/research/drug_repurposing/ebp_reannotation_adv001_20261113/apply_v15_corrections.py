#!/usr/bin/env python3
"""Apply the V15 verifier corrections (ADV-001) to annotation_compounds.tsv cell by cell; idempotent.

Run from this folder: python3 apply_v15_corrections.py. Changes are appended to CORRECTIONS.tsv.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = "verify/verdicts.tsv; verify/audit.md; hubler_fulltext_note.md"
E = {  # (compound, field): (new, reason)
 ("ifenprodil", "ebp_category"): ("EBP_DOCUMENTED (binding only; the source attributes TM7SF2)", "database emopamil-displacement binding rows only (Ki 2.7-19.8 nM, guinea-pig liver; one human EBP row Ki 5.0 nM); Hubler: 'affinity for TM7SF2 (ifenprodil)', not an EBP inhibitor in its own reading; strict set is 4"),
 ("ifenprodil", "note"): ("Hubler (open full text) attributes ifenprodil to TM7SF2; no functional EBP inhibition datum for ifenprodil in OPCs; R36 and R37 are not EBP rows for ifenprodil in the source's own reading", "verifier V15 and Hubler text"),
 ("quetiapine", "note"): ("one main-text sentence in Sax ('inhibited EBP in our assays'): a cell sterol readout, not a biochemical EBP assay; figures and SI unreached; the weakest of the five", "verifier V15"),
 ("clobetasol", "ebp_category"): ("EBP_ABSENCE_DOCUMENTED (indirect: OPC sterol-profile negative)", "Sax: clobetasol was 'the only compound that did not inhibit cholesterol synthesis' (abstract/targeted depth); an indirect negative, not a direct enzyme assay"),
 ("liothyronine", "ebp_category"): ("EBP_ABSENCE_DOCUMENTED (indirect: OPC sterol-profile negative)", "Hubler: 'liothyronine and bexarotene showed minimal effects on sterol levels in OPCs'; indirect"),
 ("bexarotene", "ebp_category"): ("EBP_ABSENCE_DOCUMENTED (indirect: OPC sterol-profile negative)", "as liothyronine"),
 ("trichostatin", "ebp_category"): ("EBP_UNMEASURED", "S0's own definition: NOT_APPLICABLE is for a stated target with no sterol claim and an EBP datum is not required; renamed by the verifier"),
 ("apicidin", "ebp_category"): ("EBP_UNMEASURED", "as trichostatin"),
 ("fimepinostat", "ebp_category"): ("EBP_UNMEASURED", "as trichostatin"),
 ("neostigmine", "ebp_category"): ("EBP_UNMEASURED", "as trichostatin"),
 ("sobetirome", "ebp_category"): ("EBP_UNMEASURED", "as trichostatin: a receptor agonist with no sterol datum is EBP_UNMEASURED under S0's definition"),
 ("amorolfine", "note"): ("Hubler: zymostenol accumulation with amorolfine is also the EBP-substrate readout; fungal Erg2p (delta8-delta7 isomerase) is inhibited by phenylmorpholines (abstract level, 3 papers); the nearest mammalian datum is fenpropimorph Ki 30 nM at human EBP (database/abstract); an amorolfine EBP effect is plausible and unmeasured (IPOTESI); no azole EBP datum found", "verifier V15"),
}


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        return
    p = os.path.join(HERE, "annotation_compounds.tsv")
    lines = open(p, encoding="utf-8").read().rstrip("\n").split("\n")
    head = lines[0].split("\t")
    log = []
    for i, line in enumerate(lines[1:], 1):
        cells = line.split("\t")
        for (comp, field), (new, why) in E.items():
            if cells[0] == comp:
                fi = head.index(field)
                if cells[fi] != new:
                    log.append(("annotation_compounds.tsv", comp, field, cells[fi][:200], new[:200], why, SRC))
                    cells[fi] = new
        lines[i] = "\t".join(cells)
    open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    if log:
        c = os.path.join(HERE, "CORRECTIONS.tsv")
        new = not os.path.exists(c)
        with open(c, "a", encoding="utf-8") as fh:
            if new:
                fh.write("file\trow_id\tfield\tbefore\tafter\treason\tsource\n")
            for r in log:
                fh.write("\t".join(x.replace("\t", " ").replace("\n", " ") for x in r) + "\n")
    print(f"{len(log)} change(s)")


if __name__ == "__main__":
    main()
