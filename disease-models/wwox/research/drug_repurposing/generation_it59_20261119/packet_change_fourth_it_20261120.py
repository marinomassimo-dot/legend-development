"""IT59 (2026-11-20): ONE fourth packet change (ADV accepted: cards EB-ETX-01 (ethosuximide, unit U17, cards_early) and H01 (apinocaltamide, unit U25) from HE ADV-098 BATCH 11 with its two dated corrections, SCI's T-type comparison
(ttype_compound_comparison_sci_20261120) and the held full texts it cites; plus the Obeid 2026 Fig 7 limit on card C01 from SCI's measurement (swd_bridge_readout_sci_20261120)). Class-level facts only, each labelled NOT WWOX EVIDENCE, no dose, no score;
the card checker's dose-looking-token rule is kept (units are written out, no dose is carried). Not carried by design: ulixacaltamide as a conditional attribution arm and the slice panel (design in v3.1 6.14 and 6.17, not card facts), any ranking of the T-type agents.
Rebuild the cards with the bridge afterwards. Idempotent (a marker guards each card); to repair committed text, patch the packet JSON in place."""
import json
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
MARK = "[IT59 2026-11-20 fourth packet change]"

def load(p): return json.loads(p.read_text(encoding="utf-8"))
def save(p, d): p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# ---- EB-ETX-01 (ethosuximide; the anchor of the T-type class)
pe = DR / "cards_early" / "EB-ETX-01.packet.json"; e = load(pe)
if MARK not in json.dumps(e):
    r = e["p4_roadmap_fields"]
    r["pharmacology"] += (" Added class-level facts from the T-type sheet and the held full texts, no dose, no score, NOT WWOX EVIDENCE, no ranking of the agents " + MARK + ": "
        "WITHIN ONE DOCUMENT (Epilepsia Open 2026, adult Gabrb3 D120N knock-in mice, atypical-absence video-EEG, a within-subjects crossover; the full text was read by SCI and the abstract by HE) ethosuximide and ulixacaltamide each reduced seizure incidence against its own vehicle; the authors' printed Results give a 64 percent reduction for both, from separate comparisons against vehicle, with different vehicle means and unequal group sizes, so the two figures are NOT a direct contrast (the abstract gives no percentage, no ethosuximide-against-ulixacaltamide test is reported, and the paper measures no exposure). "
        "In adult rats kindled in the amygdala (Casillas-Espinosa 2015, open full text) ulixacaltamide at four doses, ethosuximide and carbamazepine were given to the same rats in a randomised crossover (abstract); ulixacaltamide was not effective at suppressing seizures in fully kindled rats (HE read the full text; ethosuximide's own result in that document is SCI's reading) while it delayed the progression of kindling, which the authors describe as no anti-seizure effect in that model. "
        "HARM, class level and animal only: in the same document ulixacaltamide produced slight sedation and slow movement at the third of its four doses in fully kindled rats, not statistically different from vehicle, and mild adverse effects (a score of 1) in the first week of kindling progression, a different arm (HE read the full text); at the top dose the animals were sedate with reduced movement and a higher score (the paper's words; 'marked' is SCI's word, which HE did not re-read); a 2018 abstract reports subtle impairment of a touchscreen learning task at the highest of three doses. "
        "A class hypothesis, not a finding about ethosuximide: the T-type blocker TTA-A2 acutely increased sleep, lowered core body temperature and prevented diet-induced weight gain in normal-weight animals and reduced body weight and fat mass in obese rodents (a 2009 abstract), so a weight or temperature effect in a small pup is a reading to make before any comparison. "
        "ORDERING: the potency rows of ulixacaltamide (the same three numbers in three records) and of apinocaltamide (one document) are one origin each, and TTA-A2 has its binding and Cav3.2 values quoted again; no document tests two of the three selective agents; they sit at single digits to tens of nanomolar in cell assays, against sub-millimolar to millimolar or above for ethosuximide in different assays and laboratories (the one within-document pair is TTA-P2 against ethosuximide in one plate assay at one channel subtype, a difference of orders of magnitude on potency only); no brain concentration of any selective agent was found by these routes, and the adult mouse total brain value above is the only measured brain figure in the class found by these routes; potency, state dependence and exposure therefore do not order the agents.")
    e["not_known"].append("Whether any selective T-type blocker reaches the brain of a Wwox-deficient pup at a measured concentration (none is held for ulixacaltamide, apinocaltamide or TTA-A2), and whether ethosuximide and a selective blocker differ in effect in one assay (the one within-document pair has no direct contrast and different vehicle means) " + MARK)
    save(pe, e)

# ---- H01 (apinocaltamide)
ph = DR / "cards" / "H01_apinocaltamide_ttype.packet.json"; h = load(ph)
if MARK not in json.dumps(h):
    h["p4_card"]["pharmacology"] += (" Added class-level facts from the T-type sheet (HE ADV-098 batch 11 and its dated corrections), no dose, no score, NOT WWOX EVIDENCE " + MARK + ": "
        "the database holds 24 potency rows for apinocaltamide, ALL from one document (the 2017 discovery paper), so every figure is that paper's, once: human recombinant Cav3.1, Cav3.2 and Cav3.3 with IC50 values of 6.4, 18 and 7.5 nanomolar in a plate assay with 3 minutes of pre-incubation; values for rat (three channels), mouse (two), dog (three) and monkey (one) within about 3-fold of the human ones (the sheet says about 2.5-fold; its own rows give 3.1-fold for dog Cav3.1) except rat Cav3.3 (about 4-fold lower than human); binding to the inactivated state of human Cav3.3 by patch clamp in CHO cells with a Ki of 20 nanomolar (the IC50 values are from HEK293 cells); L-type Cav1.2 IC50 2.41 micromolar and hERG 5.5 micromolar; selectivity beyond those rows is a sentence of a 2025 abstract, not a row. "
        "Human abstract-level data (healthy adults, plasma, total concentration): in the single-dose study (65 men) a half-life of 36 to 43 hours, a 1.6-fold higher peak with food and saliva correlated with plasma; in the multiple-dose study (46 adults of both sexes) a half-life of 45 to 53 hours, steady state after 5 to 7 days and about three-fold accumulation; the most frequent events listed in the abstracts are dizziness, somnolence and headache, with weak induction of intestinal CYP3A4. "
        "NOT OBTAINABLE by a free route: any animal brain, plasma or CSF concentration (the full texts of the 2017 discovery paper and of the 2025 rodent paper are not open); no juvenile or pup study was found by these routes; the registry holds three studies by name search, all in adults (two phase 1 and one phase 2 in photosensitive epilepsy with 5 participants), with results and any paediatric registration not found by these routes. "
        "The 2025 abstract describes efficacy as equivalent to or better than first-line monotherapy without naming the comparator: COMPARATOR UNREAD, so no statement is made about apinocaltamide against ethosuximide; the 2025 abstract is sponsor-affiliated (the earlier note of IT) and the potency is one origin.")
    h["not_known"].append("The comparator of the 2025 rodent abstract's 'equivalent to or better than first-line monotherapy' (unread: the abstract does not name it; the full text is not open) and any animal brain exposure of apinocaltamide (not obtainable by a free route) " + MARK)
    save(ph, h)

# ---- C01 (AAV9 WWOX): the Obeid 2026 Fig 7 limit from SCI's measurement; the card already says the spike-count panel contradicts its own text
pc = DR / "cards" / "C01_aav9_wwox.packet.json"; c = load(pc)
if MARK not in json.dumps(c):
    c["not_known"].append("LIMIT on the electrographic readout of Obeid 2026 Figure 7, from SCI's measurement of the figure (PLAUSIBLE, not adopted) " + MARK + ": panel 7C shows two wild-type and three knockout points with p = 0.2000 on SCI's reading of the panel (the smallest exact two-sided value for 2 against 3), whereas the legend says n = 5 per group and the Results call the elevation significant: text and panel disagree and the disagreement is unresolved; panel 7E has 5 per group with per-animal values that do not overlap between knockout and wild type, pooled over a seven-day recording from about postnatal day 14, with the survivors per day not stated; whether panels 7B and 7C and panel 7E are the same animals is not stated.")
    save(pc, c)
print("ok")
