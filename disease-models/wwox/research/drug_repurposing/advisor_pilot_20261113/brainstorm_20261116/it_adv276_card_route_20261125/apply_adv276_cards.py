"""ADV-276 card route (IT, 2026-11-25): applies the wording lines of CC-20261125-ORCHESTRATOR-ADV276-WORDING-01 to the
packets of cards F04, P11, H02, H01, F03 and E01, as corrected by the blind check (VERIFIER_REPORT_AS_DELIVERED_ADV276_IT_20261125.md),
then rebuilds each card with framework/scripts/repurposing_bridge.py. Line 2 of the candidate (Table 3 of PMID 35222658 not
reproducible) is NOT applied: the blind check showed that it came from assigning an unlabelled table row to the wrong group;
the P11 row carries the corrected statement instead. check_cards.py (cards/) forbids dose-, route- and concentration-looking tokens
(a number with nM, uM, mg, mg/kg, vg, mL, kg) in card text, so the values with units stay in the candidate and the verifier report. Idempotent: every edit checks for its own marker first."""
import json
import subprocess
from pathlib import Path

DR = Path(__file__).resolve().parents[3]
CARDS = DR / "cards"
BRIDGE = DR.parents[3] / "framework/scripts/repurposing_bridge.py"
MARK = "ADV-276"
R = "FTR-20261125-"


def load(name):
    p = CARDS / (name + ".packet.json")
    s = p.read_text(encoding="utf-8")
    d = json.loads(s)
    for ind in (1, 2):
        for ea in (False, True):
            if json.dumps(d, indent=ind, ensure_ascii=ea) + "\n" == s:
                return p, d, ind, ea
    raise SystemExit("unknown JSON layout: " + name)


def row(d, rid):
    return next(r for r in d["drug_assertions"] if r["id"] == rid)


def sub(text, old, new):
    assert text.count(old) == 1, (text.count(old), old[:80])
    return text.replace(old, new)


def add_note(r, key, text):
    if MARK not in r[key]:
        r[key] = r[key].rstrip() + " " + text


def save(p, d, ind, ea, name):
    p.write_text(json.dumps(d, indent=ind, ensure_ascii=ea) + "\n", encoding="utf-8")
    out = subprocess.run(["python3", str(BRIDGE), str(p)], capture_output=True, text=True, check=True).stdout
    (CARDS / (name + ".card.json")).write_text(out, encoding="utf-8")


# ---- F04 ----
n = "F04_nmdar_intervention_class"
p, d, ind, ea = load(n)
r = row(d, "DR-P9-006")
if MARK not in r["source"]:
    r["source"] = "Banke et al 2026, Brain (PMID 40994429; partial full text read 2026-11-25, ADV-276, receipt " + R + "40994429-01; supplements not held; NOT WWOX EVIDENCE)"
    r["reading_depth"] = "partial_fulltext_read"
    r["endpoint"] = sub(r["endpoint"], "delay of pentylenetetrazole seizures", "incidence of tonic-clonic seizures and latency among animals that seized after pentylenetetrazole")
    r["locator"] = r["locator"].rstrip() + " ; full text (ADV-276): Table 2, Table 3 'Rescue: animals' and the Results paragraph on S810R mice"
add_note(r, "measured_result_note",
    "Full text (ADV-276, 2026-11-25): radiprodil was equally or more effective than at wild type in 22 of 27 variants by potency (printed) and in 21 of 27 (77.8 percent) when maximal inhibition is also counted (our count from Table 2, not printed; the one addition is I150V, which keeps potency but reaches 31 percent maximal inhibition against 85 percent at wild type). "
    "S810R, the variant of the mouse model, is one of five potency losses: the text prints 1.9-fold; Table 2 gives a ratio of about 1.5 against the pooled wild type (the printed fold changes are not reproducible from the pooled value, and one paragraph reverses the two values). "
    "S810R mice, radiprodil or vehicle, then pentylenetetrazole 30 minutes later (Table 3; doses in the paper): latency to first myoclonic jerk 131 +/- 33 s (n = 26) against 99 +/- 8.4 s (vehicle; n = 21 in the Results text, 20 in Table 3), P = 0.40; "
    "latency to generalised tonic-clonic seizure 458 +/- 90 s (the 16 mice that seized) against 207 +/- 23 s (the 20 that seized), mean +/- SEM, P = 0.0053 by unpaired t-test among animals that seized; 16 of 26 radiprodil mice against 20 of 21 vehicle mice seized (Fisher two-sided 0.013, our computation, not printed). "
    "Wild-type littermates: 6 of 18 radiprodil against 5 of 21 vehicle seized. The direction DECREASE stays at receptor level; the seizure endpoint is incidence and latency among animals that seized, not a general delay.")
save(p, d, ind, ea, n)

# ---- P11 ----
n = "P11_magnesium_nmdar_gate"
p, d, ind, ea = load(n)
r = row(d, "DR-P11-004")
if MARK not in r["measured_result_note"]:
    r["measured_result_note"] = sub(r["measured_result_note"], "and Table 3 margins disagree with Table 2.",
        "and Table 3's margins agree with Table 2 once its unlabelled 'Low' row (4/2/3, printed in the table footer of the XML) is assigned to the non-intervention group by the group totals (an earlier reading that they disagreed assigned that row to the intervention group; corrected 2026-11-25, ADV-276, after a blind check). "
        "Table 3's printed p values (0.003 intervention, 0.42 non-intervention) reproduce by chi-square from the counts (0.0029 and 0.418; intervention Low 4/4/0 and Normal 2/3/13, non-intervention Low 4/2/3 and Normal 3/2/8); Table 4's 0.004 and the seizure-control 0.69 also reproduce, and only the EEG p value of Table 2 does not.")
r = row(d, "DR-P11-005")
add_note(r, "measured_result_note",
    "Full text (ADV-276, 2026-11-25, receipt " + R + "36967744-01): 302 patients collected, 229 enrolled; 64 of the 229 had failed a first adrenocorticotropic hormone course (50 not seizure-free at its end, 14 relapsed within 1 to 12 months) and all 229 received it with magnesium, so magnesium cannot be separated; the paper states that it lacked a control group. UNKNOWN stands.")
save(p, d, ind, ea, n)

# ---- H02 ----
n = "H02_gabaat_inactivator_myelin_exposure"
p, d, ind, ea = load(n)
add_note(row(d, "DR-H02-019"), "note",
    "Full text (ADV-276, 2026-11-25, receipt " + R + "40670421-01): the rise after stopping is Table 3, six of the 11 children of the imaging-finding group (left 0.273 to 0.367, p = 0.044; right 0.286 to 0.437, p = 0.050, which is not below 0.05 although the text says P < 0.05), with no unexposed time control. "
    "In Table 2 the exposed group with normal imaging is not significantly below controls (right median 0.463 against 0.427; left 0.390 against 0.410); the starred difference is the imaging-finding group against controls. Medians with quartiles are reported while the test named is a one-way analysis of variance.")
add_note(row(d, "DR-H02-012"), "note", "Rapamycin association and the exposure figures of this cohort: see DR-H02-013 (ADV-276, 2026-11-25).")
add_note(row(d, "DR-H02-013"), "note",
    "Full text (ADV-276, 2026-11-25, receipt " + R + "36601084-01): concomitant rapamycin (60 children, all in the tuberous sclerosis group, none in the other group) is associated with lower odds of the abnormality (multivariate odds ratio 0.152, 95 percent interval 0.028 to 0.715, p = 0.019, Table 3); observational, and not separable from aetiology. "
    "The cohort-wide exposure of 170 +/- 12 days does not reconcile with the subgroup means (261 days, 80 children; 134 days, 92 children; weighted 193); peak dose shows the same mismatch (cohort 103.5, weighted subgroup mean 97.8). Not written as 'protective'.")
add_note(row(d, "DR-H02-027"), "note",
    "Full text (ADV-276, 2026-11-25, receipt " + R + "24321005-01; main text, supplement not opened): hippocampal histology on 23 brains (8 vehicle, 10 at the lowest dose, 5 at the middle dose). 81 rats were included across vehicle (33) and the CPP-115 low (14), middle (25) and highest (9) dose groups, plus 9 no-surgery controls; "
    "the highest-dose group was not assessed after postnatal day 6 because 8 of 9 rats had died by day 7, so no postnatal day 20 histology exists at that dose (our inference: histology was at day 20).")
add_note(row(d, "DR-H02-034"), "note",
    "Full text (ADV-276, 2026-11-25, receipt " + R + "42470358-01): male mice, two-day subcutaneous infusion; n per group not stated in the passage read; values mean +/- SD; OV329 against vigabatrin at doses that were not matched (our label; doses in the paper); the toxicology studies are attributed to the EILAT XVI progress report.")
save(p, d, ind, ea, n)

# ---- H01 ----
n = "H01_apinocaltamide_ttype"
p, d, ind, ea = load(n)
lst = d["p4_card"]["sources"]["external_not_wwox_evidence"]
if not any(MARK in x for x in lst):
    lst[1] = sub(lst[1], "29116786, 31004346, 31994022, 40165594, 38605177 (abstract level; none carries a receipt)",
        "29116786, 31004346, 31994022, 40165594 (abstract level; none carries a receipt); 38605177, partial full text read 2026-11-25 (ADV-276, receipt " + R + "38605177-01): cryo-EM structure of human Cav3.2 with ACT-709478, TTA-A2, TTA-P2 and ML218, and HEK293T electrophysiology; no epilepsy-model datum; the text never uses the name apinocaltamide (zero hits, 2026-11-25)")
save(p, d, ind, ea, n)

# ---- F03 ----
n = "F03_bumetanide_chloride_gradient"
p, d, ind, ea = load(n)
if not any(MARK in x for x in d["not_known"]):
    d["not_known"][3] = sub(d["not_known"][3], "the chloride rise measured in one of them is seizure-induced (PMID 20810895), not measured in a genetic model.",
        "the chloride rise measured in one of them is seizure-induced (PMID 20810895; ADV-276, 2026-11-25: Clomeleon imaging in neonatal CLM-1 mice, 187 cells from 4 intact hippocampi under low-magnesium solution, mean +/- SE; in vitro), not measured in a genetic model.")
    d["evidence_against"][5] = sub(d["evidence_against"][5], "(PMID 20810895, partial text)",
        "(PMID 20810895, partial text; intact neonatal hippocampi, seizures induced in vitro; 187 cells from 4 hippocampi, ADV-276, 2026-11-25)")
save(p, d, ind, ea, n)

# ---- E01 ----
n = "E01_isr_modulators"
p, d, ind, ea = load(n)
if not any(MARK in x for x in d["not_known"]):
    d["not_known"][6] = sub(d["not_known"][6], "and the compound's target is disputed (PMID 28447936).",
        "and the compound's target is disputed: an in vitro study with purified PPP1R15A fragments found Sephin1 at the tested concentration without effect on complex association or dissociation (biolayer interferometry) and Sephin1 at escalating concentrations (top concentration not stated in the text or legend) without effect on eIF2alpha-P dephosphorylation, and guanabenz inert at the high concentration tested in the enzymatic assay (PMID 28447936, Figures 7 and 8; ADV-276, 2026-11-25); the authors limit the statement of no direct interference with complex assembly or stability to that experimental system.")
save(p, d, ind, ea, n)
print("ok")
