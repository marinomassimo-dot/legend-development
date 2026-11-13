#!/usr/bin/env python3
"""Apply the V14 recheck corrections (SCI51) by exact-substring replacement; idempotent.

Run from this folder: python3 apply_v14_recheck.py. Each applied replacement is appended to CORRECTIONS.tsv;
a replacement whose old text is absent (already applied or never present) is reported, not forced.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = "verify/verdicts.tsv item R / audit.md section 9"
R = [
 ("reagents.tsv", "Identity WITHHELD by the developer, not merely unread:", "Structure not public (not merely unread):", "the notice does not say who withheld it"),
 ("reagents.tsv", " PIPE-307 cannot be built or tested from the public record", " Whether the compound can be obtained from its developer or licensee is not stated in anything read; its EBP activity is unmeasured in every source reached", "overstatement: availability is not addressed by the notice"),
 ("reagents.tsv", "; not a clean source", "; the notices concern a data-policy deviation and a competing-interest omission, not the validity of the data", "overstatement"),
 ("reagents.tsv", "(tropane stereo form as returned; ChEMBL parent CHEMBL85236 / mesylate CHEMBL1200383 differ in stereo layer)", "(tropane stereo form as returned; the ChEMBL parent is CHEMBL1201203 per the V14 correction at the end of this cell, not CHEMBL85236)", "stale sentence ahead of the correction"),
 ("activities.tsv", "Unmeasurable from outside while the structure is withheld.", "Unmeasured in every source reached; the structure is not public.", "retracted wording"),
 ("activities.tsv", "Absence is within the ChEMBL perimeter queried 2026-11-13", "Superseded by the correction at the end of this cell: absence is within the ChEMBL perimeter queried 2026-11-13", "stale sentence ahead of the correction"),
 ("activities.tsv", "bears on \"an M1 antagonist cannot be assumed EBP-inert\"", "INFERENZA: bears on \"an M1 antagonist cannot be assumed EBP-inert\"", "missing INFERENZA label"),
 ("evidence.tsv", "PIPE-307 cannot be built or tested from the public record", "structure not public; availability from the developer or licensee not stated in anything read", "overstatement"),
 ("outcomes.md", "(PIPE-307 class or MT7)", "(an M1-selective reagent of disclosed structure; PIPE-307 only if its structure and EBP activity become available; MT7 is a peptide toxin probe)", "arm B wording"),
 ("../README.md", "**cannot be sourced or built from the public record**: its structure is withheld;", "has **no public structure**: the Expression of Concern states that a global licence and development agreement prevented its inclusion, and whether the compound can be obtained from its developer or licensee is not stated in anything read;", "overstatement"),
 ("../README.md", "For **no** other M1 antagonist is there an EBP datum:", "For no **M1-selective** antagonist is there an EBP datum in the sources reached (clemastine and benztropine have positive EBP data in Hubler, and four unnamed antimuscarinics were EBP-negative in EpiSC OPCs):", "wrong as written"),
 ("../README.md", "**The CW compounds are not M1-clean as the text implies:**", "**The CW compounds are M1-low in one single-point assay, not shown M1-clean:**", "overgeneralised"),
 ("../README.md", "a **fourth preparation** (mouse primary cortical OPCs, Extended Data 5: TASIN-1 and amorolfine at 300 nM) shows the EBP route outside EpiSC cells.", "a **fourth preparation** (mouse primary cortical OPCs, Extended Data 5: TASIN-1 and amorolfine at 300 nM, MBP+ at 72 h and zymostenol at 24 h) carries the same experiment (legend read, outcomes not).", "legend, not results, was read"),
 ("../README.md", "about 21–29 per field): **the null", "about 21–29 per field, my arithmetic from the fold range and not a printed value): **the null", "arithmetic label"),
 ("../README.md", "is **answered in the negative for the public record** (unmeasured, and unmeasurable for PIPE-307 from outside)", "is **unanswered in the public record** (unmeasured in every source reached; the structure is not public)", "retracted wording"),
 ("../README.md", "Candidate disclosed M1-selective antagonists exist in the literature (for example VU6077564, PMID 42411178: no OPC datum, no EBP datum, abstract only), so the role can be filled,", "Other M1-selective antagonists exist in the literature (for example VU6077564, PMID 42411178: abstract only, no structure seen by us, no OPC or EBP datum), so the role may be fillable,", "VU6077564 is not shown to be disclosed"),
 ("../README.md", "**The corrections were not rechecked by the verifier** (time budget); five corrected cells were spot-checked by me against the verdicts and agree.", "**The corrections were rechecked narrowly by the same verifier** (53 rows: 38 correct, 15 defective: three in the correction cells, one in the added rows, two in `outcomes.md`, nine in my README, answer and delta, which overstated: the notice's reason, availability, 'no other M1 antagonist has an EBP datum', 'CW not M1-clean', 'unmeasurable from outside'); all are corrected by `output/apply_v14_recheck.py` (logged in `CORRECTIONS.tsv`); two of the retracted phrases were the verifier's own first-pass wording.", "recheck result"),
 ("../consumer_delta.md", "no M1 antagonist has an EBP datum", "no M1-selective antagonist has an EBP datum in the sources reached", "wrong as written"),
 ("../consumer_delta.md", "the M1-selective reagent named in SCI50 cannot be sourced (structure withheld; PNAS Correction and Expression of Concern)", "the M1-selective reagent named in SCI50 has no public structure (PNAS Correction and Expression of Concern; availability from its developer not stated)", "overstatement"),
 ("../consumer_delta.md", "unmeasured, unmeasurable for the named reagent from the public record", "unmeasured in every source reached (structure not public)", "retracted wording"),
 ("../consumer_delta.md", "unmeasurable for the named reagent from the public record", "unmeasured in every source reached (structure not public)", "retracted wording"),
 ("../consumer_delta.md", "**no identity** (structure withheld)", "**no identity** (structure not public)", "wording"),
]
APPEND = {
 "outcomes.md": ("<!-- v14-recheck -->", """
## Recheck correction (2026-11-13, after the V14 narrow recheck)
The sentence "the null baseline is as large as the drug effect" is superseded: Chrm1-null about 4 v 16 MBP+ cells per field against drug-treated wild type about 21-29 (my arithmetic): occlusion is a weaker confound than stated, still a confound. **Arm G (added): C plus a muscarinic agonist or ACh add-back** for the M1 residue of CW3388 (about 18-19% in one single-point CHO assay; the residue at its OPC-active dose is unmeasured). **Fourth preparation:** mouse primary cortical OPCs (Hubler Extended Data 5: TASIN-1 and amorolfine at 300 nM, MBP+ at 72 h, zymostenol at 24 h; legend read, outcomes not). Arm B is a role: an M1-selective reagent of disclosed structure whose EBP activity is measured in the preparation used; PIPE-307 qualifies only if its structure and EBP activity become available.
"""),
 "answer.md": ("<!-- v14-recheck -->", """
## Sentences accepted after the V14 recheck (2026-11-13)
*PIPE-307 identity and availability:* The structure and characterisation data of PIPE-307 are not in the primary paper or its appendix. A PNAS Editorial Expression of Concern (PMID 40512803, June 2025) states that a global licence and development agreement prevented inclusion of the chemical structure, a restriction not disclosed at submission; the Correction (PMID 39432800) concerns competing interests. No structure was found in PubChem, ChEMBL or Europe PMC by name. Whether the compound can be obtained from its developer or licensee is not stated in anything read, and its EBP activity is unmeasured in every source reached. *CW compounds:* In one single-point M1-NFAT-CHO antagonist assay (Allimuthu Fig 4E, n = 2, relative to clemastine = 100% at 1 uM), CW9009 and CW9956 read about 0-3% and CW3388 about 18-19%; TASIN-1 read about 2 and 10% at 100 nM; single-concentration readings, not affinities; no M2-M5, sigma, hERG or Kir datum exists in any source reached; CW3388's residue at its OPC-active dose (110 nM and above) is unmeasured: the compounds are M1-low in that assay and not shown M1-clean. *Form of the answer:* An improved design, not a build-ready comparison: the pair lacks an M1-selective reagent of disclosed structure with its EBP activity measured in the OPC preparation used, and a measured, plating-density-controlled M1 tone there. Until both are measured, a difference between arms cannot be attributed to one target.
"""),
}


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        return
    log, missing = [], []
    for f, old, new, why in R:
        p = os.path.join(HERE, f)
        body = open(p, encoding="utf-8").read()
        if old in body and new not in body:
            open(p, "w", encoding="utf-8").write(body.replace(old, new))
            log.append((os.path.basename(f), "text", "replace", old[:150], new[:150], why, SRC))
        elif new not in body:
            missing.append((f, old[:80]))
    for f, (marker, text) in APPEND.items():
        p = os.path.join(HERE, f)
        body = open(p, encoding="utf-8").read()
        if marker not in body:
            open(p, "a", encoding="utf-8").write("\n" + marker + text)
            log.append((f, "narrative", "dated section", "", "appended", "V14 recheck", SRC))
    if log:
        with open(os.path.join(HERE, "CORRECTIONS.tsv"), "a", encoding="utf-8") as fh:
            for r in log:
                fh.write("\t".join(str(c).replace("\t", " ").replace("\n", " ") for c in r) + "\n")
    print(f"{len(log)} change(s); not found and not already applied: {missing}")


if __name__ == "__main__":
    main()
