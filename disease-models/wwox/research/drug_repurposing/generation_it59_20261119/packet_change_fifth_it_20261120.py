"""IT59 (2026-11-20): ONE fifth packet change (ADV asked: decide whether the glial card J01 and the metabolic card I01 need one dated class-level line from SCI's ADV-104
(glial and inflammatory axis, carried as a READOUT beside glucose, not an arm) and ADV-101 increment 2 (agents with exposure facts, marginal utility, promote and park rules)).
Decision: yes, one block each; class level, no dose, no score, no promotion, NOT WWOX EVIDENCE for any agent; the card checker's dose-looking-token rule is kept (units written out).
Rebuild the cards with the bridge afterwards. Idempotent (a marker guards each card); to repair committed text, patch the packet JSON in place."""
import json
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
MARK = "[IT59 2026-11-20 fifth packet change]"

def load(p): return json.loads(p.read_text(encoding="utf-8"))
def save(p, d): p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# ---- J01 (glial reactivity modulation): SCI ADV-104
pj = DR / "cards" / "J01_glial_reactivity_modulation.packet.json"; j = load(pj)
if MARK not in json.dumps(j):
    c = j["p4_card"]
    c["pharmacology"] += (" Added from SCI's ADV-104 (class level, no dose, NOT WWOX EVIDENCE for any agent) " + MARK + ": no HE sheet covers an agent directed at microglia or inflammation, so none is carded. "
        "The two agents in HE's sheets nearest to this axis are ganaxolone and clemastine, and neither is a glia-state agent: ganaxolone has rat pharmacokinetic and intravenous titles only (no brain concentration and no juvenile or pup exposure found; in the one focal demyelination model in ovariectomised adult female rats that SCI read at passage level, microglial clearance of myelin debris and remyelination were enhanced while astrocytosis and cytokines were unaffected, a debris-clearance mechanism with no counterpart in an uninjured knockout cortex), "
        "and clemastine has a qualitative detection in juvenile rat brain and a plasma level in neonatal mouse (both from SCI's check, not re-read by HE) without a brain concentration, with an oligodendrocyte-precursor rationale rather than a glial-inflammation one.")
    c["next_measurement"] += (" THE GLIAL AXIS IS CARRIED AS A READOUT BESIDE GLUCOSE, NOT AS AN ARM " + MARK + " (SCI's ADV-104, hypothesis level): every glial measurement in the held texts is at postnatal days 14 to 20 (area fractions of GFAP and Iba1, a few cytokine transcripts), "
        "while the earliest documented seizures are at day 9 in the neuronal-deletion line and 'within a few days after birth' in the germline null; none of the held texts measures a glial marker before the first seizure in any line, so 'not measured' is the finding, not 'not present'. "
        "SCI's condition that would promote the axis: a per-animal glial series in the neuronal-deletion cortex or the germline null at days 5, 7, 9 and 12 showing a rise before the first seizure, AND a replicated glial-state-specific manipulation that moves seizures or survival in a neuronal-primary developmental model; what would park it: gliosis first appearing at or after seizure onset in every line that reports timing, with the manipulation question still empty (no timing below day 14 has been measured by anyone, so neither condition is met today). "
        "GFAP and Iba1 are already endpoints of the gene-addition benchmark, so scoring them on the same slides of any pilot arm costs no animals.")
    j["not_known"].append("Whether a glial or inflammatory state can be changed independently of neuronal rescue in the held Wwox texts " + MARK + ": the only manipulation that moves it is neuronal restoration, which moves GFAP, Iba1, survival, weight, glucose and myelination together; "
        "deletion of Wwox restricted to astrocytes or to oligodendrocyte-lineage cells gave no phenotype in the held text; in the nearest studied neuronal-primary model (Rett), one microglia-replacement report was not replicated in three models (abstract level), so the independent route is contested there and untested here.")
    save(pj, j)

# ---- I01 (PDK inhibition, premise seizure and glycaemia): SCI ADV-101 increment 2
pi = DR / "cards" / "I01_pdk_inhibition_dca_premise_seizure_glycaemia.packet.json"; i = load(pi)
if MARK not in json.dumps(i):
    c = i["p4_card"]
    c["next_measurement"] += (" Added from SCI's ADV-101 increment 2 (class level, hypothesis level, no dose, no recommendation) " + MARK + ": only two interventions on the glycaemia axis carry any exposure statement and neither is usable for a pup: dichloroacetate (HE found no brain concentration in mice and no juvenile exposure by its query; a millimolar-range potency in one assay) and a ketogenic diet (no ketone, glucose or intake value in any Wwox-deficient animal or child); no third was found by the sheets and searches used. "
        "Digoxin is a probe of the axis, not a candidate. On held data the axis is a COVARIATE TO MEASURE, NOT AN ARM: no agent with a pup brain exposure fact was found by these routes and the fuel-supply arm is not yet specified, an independently modifiable glycaemic step is untested in the neuronal-deletion and progenitor-targeted lines, and the deciding test is cheap (a glucose reading with same-animal EEG). "
        "What would make it the preferred broad candidate (fixed in SCI's pre-registration): glucose already low at or before day 9 in those pups AND a glucose or fuel-supply arm that, without restoration of WWOX, changes the spike rate, the seizure score or survival (recorded as EEG or ECoG); what would park it: normoglycaemia across days 7 to 14 while the pups seize and die, glucose falling only after the first seizure or spike epoch, or a supply arm that corrects glucose and weight but not the EEG or survival. "
        "The unfavourable reading, as it stands: the one correction that exists (neuronal AAV9) normalises glucose, weight, seizures and survival together and is not separable.")
    i["not_known"].append("Whether a glucose-lowering diet or fuel-shifting intervention helps or harms pups already hypoglycaemic from about day 10 (the first glucose value, in the germline null; none exists for the neuronal-deletion or progenitor-targeted lines), and the direction of the glucose response of dichloroacetate in a hypoglycaemic pup (unmeasured; the adult response with raised glucose is a fall) " + MARK + ".")
    save(pi, i)
print("ok")
