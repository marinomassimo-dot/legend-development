"""IT57 / ADV-066 K2 round (2026-11-18): map the per-arm outcome patterns of SCI's in vivo brief, section 4, into outcome_favourable and outcome_contrary of the two
comparison rows that carry the provoked-seizure experiment (INV-04 C-EP2, INV-09 C-GS1). Mapping only: no pattern, margin or reading is IT's own; the original cell text is kept and
the mapped text is appended under a marker. The brief's labels are named as the brief's (its E4 is 'no effect anywhere'; the package's E4 is the T-type route). Idempotent.
Run from this folder after build_packages.py:  python3 apply_k2_mapping_adv066.py"""
import csv
from pathlib import Path
HERE = Path(__file__).resolve().parent
MARK = "[K2 mapping, 2026-11-18, IT, from SCI's in vivo brief section 4 (priors file sha256 326846fb5180), mapped not authored:"
BRIEF = "experiment_brief_presidio013_sci_20261116/invivo_pup_adv059_sci_20261118/INVIVO_PUP_EXPERIMENT_BRIEF_V1_SCI_20261118.md"
EP2_FAV = (MARK + " each pattern is read only where the assay-sensitivity panel is valid at the age and wild type is above the floor. "
    "Brief E1: effect ratio in the knockout at most 0.7, wild type null, interaction ratio at most 0.7 -> favours a knockout-selective effect (does not show a T-type route or a spontaneous-seizure benefit). "
    "Brief E2: wild type null at the assay age and an effect at an older age -> favours an age-limited effect with a wild-type floor, so the published pattern is not knockout selectivity (does not show that the knockout effect is absent). "
    "Brief E3: similar effects in all genotypes, interaction ratio between 0.7 and 1.43 -> favours a general anticonvulsant effect (does not show selectivity or its absence at other ages). "
    "Brief C1: a selective T-type blocker beside ethosuximide gives the same pattern in the knockout -> a T-type route is plausible, not proven without engagement or genetics. "
    "Any arm: minimal-seizure incidence up while generalised incidence down -> favours a seizure-type-specific action (does not show benefit or harm in the null phenotype). Source: " + BRIEF + "]")
EP2_CON = (MARK + " Brief E4: no effect anywhere -> the published knockout effect did not replicate at this age and stimulus (says nothing about other ages or exposures). "
    "Brief C2: the selective T-type blocker has no effect where ethosuximide has one -> ethosuximide's effect is not carried by selective T-type block at this exposure and age, or the exposure was inadequate (which is not separated). "
    "Brief E5: a failed assay-sensitivity panel or a wild type at the floor -> not interpretable at that age. Source: " + BRIEF + "]")
GS1_FAV = (MARK + " Brief lithium rows, read where the panel is valid and wild type above the floor. "
    "Lithium and the second GSK-3 inhibitor effective in all genotypes (interaction ratio between 0.7 and 1.43) and the general comparator effective -> favours a general anticonvulsant effect of GSK-3 inhibition and of the comparator (does not show GSK-3 specificity in the knockout). "
    "Knockout-larger lithium effect, reproduced by the second GSK-3 inhibitor and not by the comparator -> favours a GSK-3 route that is knockout-enhanced (does not show a p-Ser9 or kinase change, which needs the add-on in the same treated animals); the interaction margin for 'knockout-larger' is outside 0.7 to 1.43 (brief 9.1, set P5 of the priors), exploratory if the interaction cannot be sized. Source: " + BRIEF + "]")
GS1_CON = (MARK + " Lithium effect in all genotypes with the comparator also effective is the 'general' reading itself; where the interaction cannot be sized, genotype specificity cannot be used to tell general from specific and the comparator decides (brief 9.1). Source: " + BRIEF + "]")
EDITS = {"inv04_ethosuximide_age_assay": ("C-EP2", EP2_FAV, EP2_CON), "inv09_lithium_gsk3_regimen": ("C-GS1", GS1_FAV, GS1_CON)}
for pkg, (row_id, fav, con) in EDITS.items():
    p = HERE / pkg / "output" / "comparison.tsv"
    rows = list(csv.reader(open(p, encoding="utf-8"), delimiter="\t"))
    h = rows[0]; i_f, i_c = h.index("outcome_favourable"), h.index("outcome_contrary")
    for r in rows[1:]:
        if r[0] == row_id:
            if MARK not in r[i_f]: r[i_f] = r[i_f] + " " + fav
            if MARK not in r[i_c]: r[i_c] = r[i_c] + " " + con
    with open(p, "w", newline="", encoding="utf-8") as f:
        csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
    print("mapped", pkg, row_id)
