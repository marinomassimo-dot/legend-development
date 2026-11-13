#!/usr/bin/env python3
"""Apply the V15 recheck residual corrections (ADV-001) by exact-substring replacement; idempotent.

Run from this folder: python3 apply_v15_recheck.py. Changes are appended to CORRECTIONS.tsv.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = "verify/verdicts.tsv item R / audit.md recheck section"
R = [
 ("annotation_compounds.tsv", "Hubler R36/R37 are its OPC/spheroid rows (to be confirmed by the verifier)", "Hubler (open full text) attributes ifenprodil to TM7SF2; R36/R37 are not EBP rows for ifenprodil in the source's own reading", "stale basis cell"),
 ("annotation_compounds.tsv", "\t6 (CHEMBL305187)\t", "\t7 (CHEMBL305187; six guinea-pig liver rows plus one human EBP row under the (S,R) stereoisomer)\t", "row count"),
 ("annotation_compounds.tsv", "Sax 35833657 (abstract/targeted depth by the SCI51 verifier; tables and SI not reached)", "Sax 35833657 (main text read by the verifiers through the PubMed tool: one sentence; figures, tables and SI not reached)", "depth wording"),
 ("annotation_compounds.tsv", "target agonist; Hubler uses it as an additive comparator; EBP unmeasured (ChEMBL 0)", "target agonist; indirect OPC sterol-profile negative (Hubler: minimal effects on sterol levels); no direct EBP assay; ChEMBL 0 rows", "stale basis cell"),
 ("annotation_compounds.tsv", "target agonist; EBP unmeasured (ChEMBL 0)\tHubler 30046109; 21131950 (S1-10)", "target agonist; indirect OPC sterol-profile negative (Hubler: minimal effects on sterol levels); no direct EBP assay; ChEMBL 0 rows\tHubler 30046109 (R35). Not the RXR rows S1-10/S1-11 (those are 9-cis retinoic acid, HX630, PA024: R42)", "source cell mapping error"),
 ("annotation_compounds.tsv", "stated target supported by an antagonist control; no sterol claim; EBP unmeasured (ChEMBL 0)", "stated target supported by an antagonist control; indirect sterol-profile negative (Sax abstract/main text: the only compound that did not inhibit cholesterol synthesis); no direct EBP assay; ChEMBL 0 rows", "stale basis cell"),
 ("annotation_compounds.tsv", "the name did not resolve in the ChEMBL name search (no EBP row looked for)", "the name search did not resolve it; apicidin is CHEMBL443392 (V15), no EBP row in the pulled rows", "name resolution"),
 ("annotation_compounds.tsv", "unmeasured is not inactive; the conflict between the screen hit and Hubler's inert antimuscarinics is unresolved", "unmeasured is not inactive; Hubler's four inert antimuscarinics are unnamed in the text and probably differ from these compounds (INFERENZA), so no conflict is shown", "S0 'unresolved conflict' not shown"),
 ("annotation_compounds.tsv", "Hubler: amorolfine route via TM7SF2; no EBP datum in the sources read", "Hubler: amorolfine named as a TM7SF2 (sterol 14-reductase) inhibitor enhancing MBP+ formation; accumulation of 14-dehydrozymostenol and zymostenol is reported for 'amorolfine and TASIN-1' together; the text does not say which compound gives zymostenol; no EBP datum in the sources read", "amorolfine statement"),
 ("annotation_compounds.tsv", "the nearest mammalian datum is fenpropimorph Ki 30 nM at human EBP (database/abstract)", "the nearest mammalian datum is one ChEMBL row for fenpropimorph (Ki 30 nM at human EBP; 'close analogue' is the verifier's inference)", "fenpropimorph depth"),
 ("annotation_compounds.tsv", "Hubler: zymostenol accumulation with amorolfine is also the EBP-substrate readout; ", "", "amorolfine statement not in the source"),
 ("annotation_signed_rows.tsv", "receptor agonist; no sterol claim; EBP unmeasured", "receptor/nuclear-receptor agonist rows: S1-09 compound clobetasol (indirect sterol-profile negative, Sax); S1-10 and S1-11 are retinoids (9-cis retinoic acid, HX630, PA024; R42) with sterol profile unmeasured in the sources read", "S1-09..S1-11 mapping"),
 ("annotation_signed_rows.tsv", "sterol-pathway by design; EBP unmeasured for these compounds", "other sterol enzyme by design (S1-05, S1-08); EBP unmeasured for these compounds: not cleared", "unmeasured is not cleared"),
]
APPEND = ("CORRECTIONS.tsv", [
 ("apply_v15_corrections.py", "reason texts", "reason", "'NOT_APPLICABLE covers a stated target with no sterol claim'", "S0 defines NOT_APPLICABLE as a stated target that is not an enzyme-inhibitor route; HDAC, cholinesterase inhibitors and receptor agonists with no sterol datum are EBP_UNMEASURED because no EBP datum exists, not because NOT_APPLICABLE is wrong in kind", "the reason texts of the four renames were wrong (V15 recheck)", SRC),
 ("annotation_compounds.tsv", "sobetirome", "ebp_category", "NOT_APPLICABLE", "EBP_UNMEASURED", "not a V15 first-pass correction: a recheck-stage rename made so that the four-way split sums to 15 (V15 had judged NOT_APPLICABLE correct for it); recorded here for honesty", SRC),
])


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        return
    log = []
    for f, old, new, why in R:
        p = os.path.join(HERE, f)
        body = open(p, encoding="utf-8").read()
        if old in body and new not in body:
            open(p, "w", encoding="utf-8").write(body.replace(old, new))
            log.append((f, "text", "replace", old[:150], new[:150], why, SRC))
    c = os.path.join(HERE, APPEND[0])
    body = open(c, encoding="utf-8").read()
    if "reason texts" not in body:
        log += APPEND[1]
    if log:
        with open(c, "a", encoding="utf-8") as fh:
            for r in log:
                fh.write("\t".join(str(x).replace("\t", " ").replace("\n", " ") for x in r) + "\n")
    print(f"{len(log)} change(s)")


if __name__ == "__main__":
    main()
