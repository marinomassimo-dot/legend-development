"""IT57 / ADV-066 (2026-11-18, after SCI's withdrawal, message to IT): the development wording 'the KCC2 branch is more promising than an NKCC1 blocker on evidence level only' (SCI ADV-065b)
is WITHDRAWN by SCI after an independent verifier with full inputs. Replacement text is SCI's own, verbatim. The withdrawn clause is replaced in the two comparison cells that carried it
(INV-04 C-EP5, INV-09 C-GS3) and named as withdrawn in the same cell; nothing else changes. Idempotent. Run from this folder after build_packages.py and apply_k2_mapping_adv066.py."""
import csv
from pathlib import Path
HERE = Path(__file__).resolve().parent
WD = "[WITHDRAWN 2026-11-18 by SCI (ADV-065c, after an independent verifier): the statement that the KCC2 branch is more promising than an NKCC1 blocker on development on evidence level only]"
SCI_LONG = ("Development: not rankable between the KCC2 and NKCC1 branches; neither has Wwox data. KCC2 side: one sponsor-funded Cdkl5 pup dataset (a shift in timing of a self-resolving phenotype and adult effects, litters randomised, no wild-type-on-agent group). "
            "NKCC1 side: neonatal studies in other genetic models with durable outcomes (Kv7 with controls unaffected; Fmr1; Dravet behaviour without seizure effect) and adverse signals (R43Q pro-seizure hazard; a two-genotype social reduction). All abstract or single-paper level.")
SCI_SHORT = "development: not rankable between branches; neither has Wwox data"
EDITS = {
 ("inv04_ethosuximide_age_assay", "C-EP5", "documented_action_and_limits"): (
    "is more promising than an NKCC1 blocker on this endpoint on evidence level only; against the other candidates it is not rankable (their development data were not searched). Neither branch is more promising overall;",
    SCI_LONG + " " + WD + ". Against the other candidates it is not rankable (their development data were not searched). Neither branch is more promising overall;"),
 ("inv09_lithium_gsk3_regimen", "C-GS3", "documented_action_and_limits"): (
    "the KCC2 branch is more promising than an NKCC1 blocker on development on evidence level only, not rankable against the other candidates; neither branch is more promising overall;",
    SCI_SHORT + " (SCI's replacement, 2026-11-18; the long form is in the INV-04 C-EP5 cell); " + WD + "; neither branch is more promising overall;"),
}
for (pkg, row_id, col), (old, new) in EDITS.items():
    p = HERE / pkg / "output" / "comparison.tsv"
    rows = list(csv.reader(open(p, encoding="utf-8"), delimiter="\t"))
    ic = rows[0].index(col); done = False
    for r in rows[1:]:
        if r[0] == row_id:
            if "[WITHDRAWN 2026-11-18 by SCI (ADV-065c" in r[ic]: done = True
            else:
                assert r[ic].count(old) == 1, (pkg, row_id)
                r[ic] = r[ic].replace(old, new)
    with open(p, "w", newline="", encoding="utf-8") as f:
        csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
    print(("already applied" if done else "replaced"), pkg, row_id)
