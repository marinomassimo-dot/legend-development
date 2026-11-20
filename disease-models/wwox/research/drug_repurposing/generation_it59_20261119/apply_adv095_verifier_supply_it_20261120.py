"""IT59 (2026-11-20), ADV-097 item 3: SCI's blind verifier pass on the agent and bridge-exposure producer reports (VERIFIER_PASS_READING_SCI_20261120; the verifier's reading of sources, not re-read by SCI)
and SCI's supply search for a cortical cell-type-resolved Wwox-deficient deposit, carried as dated lines into WO-27, WO-20 and WO-21. CLASS-LEVEL qualifiers only: no dose, concentration or exposure number is carried
into any row or card (producer and verifier figures stay in SCI's folder). No row is added, no status change; cards and ranking inputs are not edited. Idempotent."""
import csv
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
REC = " Record: advisor_pilot_20261113/brainstorm_20261116/adv097_consumption_it_20261119/CONSUMPTION_RECORD_ADV097_IT_20261119.md section 10."
WO27 = (" [IT 2026-11-20, ADV-097 consumption, on SCI's verifier pass and supply search (verifier: no quote fabricated, no pivotal number wrong; qualifiers listed; this is the verifier's reading of sources, not re-read by SCI): "
        "CLASS-LEVEL qualifiers now carried. Clemastine class: the positive results are in small groups and in hypoxia and a Tcf4 model whose starting state is an OPC EXCESS, the opposite of the Wwox-deficient cortex (OPC intact, stages from the committed precursor lower); one harm signal in healthy developing mouse at a SINGLE dose, so no dose-response exists; the negative rat result in genetic hypomyelination is not an absolute null; no quantitative juvenile brain, CSF or unbound value (one qualitative detection in a paper inconsistent about age). "
        "Thyromimetic class: window dependence is for myelination (a late start did not improve it) and the class is model- and route-dependent (worse in one genetic demyelination model on a hyperthyroid diet, promoting repair in two gliotoxin models); in vivo normalisation in the Tcf4 mouse is for the brain-targeted prodrug Sob-AM2, and the producer's claim for sobetirome in vivo is NOT supported; the tiratricol EU authorisation concerns peripheral thyrotoxicosis in MCT8 deficiency, not myelination; maternal toxicity is reported in one transporter-deficient background. "
        "SUPPLY SEARCH (SCI): no public cortical cell-type-resolved Wwox-deficient deposit by GEO, ArrayExpress, PRIDE, Zenodo, CELLxGENE, the Single Cell Portal and Europe PMC; the hippocampal single-nucleus deposit (held) is the only cell-type-resolved Wwox mouse deposit and every public cortical Wwox-mouse deposit is bulk: the activity-dependent branch of A3 therefore STAYS stopped; a cortical counterpart could only come from the authors (an external contact: not authorised here and not asked). "
        "IN-SILICO part still able to change the comparison: SCI's compound-level unit C and the exposure round; MEASUREMENT only an experiment supplies: the cell-level lineage readout named above." + REC + "]")
WO20 = (" [IT 2026-11-20, ADV-097 consumption, on SCI's verifier pass (bridge exposure producer; verifier's reading of sources): the Cheng 2020 ethosuximide regimen is verified (single intraperitoneal pretreatment before the convulsant; NO drug concentration measured; NO age or day given for the drug experiments); a recombinant human T-type potency exists but the abstract sentence that native-neuron studies disagree is the paper's own premise, not evidence, and its inactivated-state values are for a methsuximide metabolite; a mouse total-brain ethosuximide value exists in another paper (total tissue, not free, dose not matched to Cheng's); ten more exposure papers are abstract-level and belong to the exposure round. No number is carried here. "
        "IN-SILICO part that can still change the comparison: the exposure round (does the target explain the effect at the exposures used; free against total; juvenile against adult); MEASUREMENT only an experiment supplies: the same-day three-genotype design with measured exposure and the interaction term (this row), unchanged." + REC + "]")
WO21 = (" [IT 2026-11-20, ADV-097 consumption, on SCI's verifier pass: the Cheng 2020 lithium regimen is verified (several intraperitoneal doses within one hour before the convulsant; no concentration; no age or day for the drug experiments; whether the dose is stated as salt or as lithium is still to be read by the exposure round); the lithium exposure papers found are rat poisoning models at abstract level, not regimen-matched. With the unit A reading above (GSK-3/Wnt premise weakened) the lithium effect stays a general, regimen-dependent finding; the in-silico part left is the exposure comparison, the measurement is the GSK-3 activity and the second GSK-3 class, unchanged." + REC + "]")
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"
rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t"))
i = rows[0].index("status_evidence"); j = rows[0].index("last_touched")
n = 0
for r in rows[1:]:
    for q, t in (("WO-27", WO27), ("WO-20", WO20), ("WO-21", WO21)):
        if r[0] == q and "on SCI's verifier pass" not in r[i]:
            r[i] += t; r[j] = "2026-11-20"; n += 1
with open(p, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("ok", n)
