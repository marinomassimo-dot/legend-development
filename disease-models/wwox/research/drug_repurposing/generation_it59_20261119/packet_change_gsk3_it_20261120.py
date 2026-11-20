"""IT59 (2026-11-20): ONE packet change (ADV accepted compound-level units for the units whose numbers are verified in HE batches 1 to 9):
cards G01 (lithium / GSK3beta; unit U24) and D02 (Wnt-lowering and GSK3 modulation; unit U11). Class-level facts only, each labelled; no dose, no score, no ranking text.
Content comes from: CLAIM 035 Evidence boundary (BATCH_20261120_001), SCI's verified harm cell (VERIFIER_REPORT_HARM_CELL_AS_DELIVERED_20261120.md), HE ADV-098 batch 9, SCI v2.2 panel design.
Rebuild the two cards with the bridge afterwards. Idempotent (marker)."""
import json
from pathlib import Path

C = Path(__file__).resolve().parent.parent / "cards"
MARK = "[IT59 2026-11-20 packet change]"

def load(n): return json.loads((C / (n + ".packet.json")).read_text(encoding="utf-8"))
def save(n, p): (C / (n + ".packet.json")).write_text(json.dumps(p, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# ---- G01 (lithium)
g = load("G01_lithium_gsk3")
if MARK not in json.dumps(g):
    old3 = [i for i, s in enumerate(g["not_known"]) if "S9-independent inhibition" in s]
    assert len(old3) == 1, old3
    g["not_known"][old3[0]] = ("Whether GSK3beta abundance or Ser9 state tracks activity here: the sources are in tension and no kinase-activity assay exists in WWOX-deficient cells or tissue (the kinase assays of the cell-line paper are cell-free, with purified recombinant proteins, and show WWOX protein lowering GSK3beta-driven Tau phosphorylation in vitro). "
        "The cell-line paper reports phospho-Ser9 unchanged along a retinoic-acid time course while WWOX rises; no experiment in it manipulates WWOX and reads Ser9, and the phrase 'S9-independent' occurs nowhere in its text; "
        "the only tissue datum (Wwox-null brain, cerebellum, hippocampus and cortex; the legend says postnatal day 20 and the Methods say 14) reports LOWER phospho-Ser9, as a ratio to beta-actin, with representative results of four independent experiments and the number of animals not stated (registry CLAIM 035 Evidence boundary, BATCH_20261120_001; the earlier wording of this item, 'S9-independent inhibition', is withdrawn) " + MARK + ".")
    pc = g["p4_card"]
    pc["pharmacology"] += (" Label facts, read at source by a blind verifier on 2026-11-20 (US label record, class level, NOT WWOX EVIDENCE): a boxed warning that lithium toxicity is closely related to serum concentration and can occur at doses close to therapeutic concentrations; "
        "neurological signs of toxicity include ataxia and, among severe manifestations, seizure, and in rare cases neurological sequelae may persist after discontinuation and may be associated with cerebellar atrophy (the label hedges); "
        "lithium is concentrated in the thyroid and can lead to hypothyroidism (hyperthyroidism cases are also reported); in pregnancy the label says lithium may cause harm and names a floppy baby syndrome in neonates exposed late in pregnancy " + MARK + ".")
    pc["paediatrics_and_interactions"] += (" The label states paediatric safety and effectiveness as established for monotherapy of bipolar I disorder at ages 7 to 17 and not established below 7; that is a statement for another indication and is not a paediatric suitability for WWOX-DEE " + MARK + ".")
    pc["next_measurement"] += (" The substrate-phosphorylation readout is now DESIGNED, not measured: tau phospho-sites over total tau, Ser9 over TOTAL GSK3beta (not over actin) and beta-catenin, in the cortex of the neuronal-deletion line at postnatal day 17, with a decision per outcome fixed before data (SCI design v2.2 and v3.1, hypothesis level, no data) " + MARK + ".")
    save("G01_lithium_gsk3", g)

# ---- D02 (Wnt-lowering and GSK3 modulation)
d = load("D02_wnt_tankyrase")
if MARK not in json.dumps(d):
    d["not_known"] += [
        ("GSK-3 premise status after the 2026-11 comparison work (class level; hypothesis): the GSK-3 and Wnt transcript premise was not supported in the organoid and not distinguishable from random gene sets in the held postnatal day 17 mouse cortex (bulk, three against four animals; the Wnt sign agrees with the premise, inside the null band in the primary run and borderline in the blind recompute), and one interactome partner, GSK3beta, meets the registered criteria with narrowings "
         "(directness not shown by the assays; the pharmacology of the criterion is partial, lithium at abstract level and no GSK3beta-specific non-lithium constant read in a primary source; the cell readout is a retinoic-acid-differentiated neuroblastoma line; the only tissue datum, lower phospho-Ser9 in Wwox-null brain, is the direction of more active kinase, whereas the cell-line paper reports phospho-Ser9 unchanged and attributes its effect to binding: the sources are in tension on the role of Ser9); "
         "no GSK-3 substrate measurement exists in a Wwox-deficient neuron (the cell-line paper reads Tau phospho-sites after WWOX knockdown and overexpression in a neuroblastoma line) " + MARK + "."),
        ("Brain or plasma concentration of any non-lithium GSK-3 inhibitor, free or total, adult or juvenile: not found in rodents by public-database and literature-title routes (PubMed titles only) for five agents (tideglusib, SB-216763, CHIR-99021, LY2090314, AR-A014418); selectivity was not assessed " + MARK + "."),
    ]
    pc = d["p4_card"]
    pc["pharmacology"] = ("NOT WWOX EVIDENCE, class level (HE ADV-098 batch 9, public databases, 2026-11-20): five GSK-3 inhibitors of non-lithium chemistry exist, with beta potencies in vitro from sub-nanomolar to micromolar depending on the document and assay (one weak 2011 fluorescence assay of AR-A014418 is set apart by the sheet), "
        "alpha about 1.4- to 2.5-fold weaker than beta at most within one document and assay (none shown to separate alpha from beta by an order of magnitude); tideglusib is non-ATP-competitive and time-dependent, so its potency depends on pre-incubation and is not set against the ATP-competitive agents; "
        "no ordering of agents is read from these values; no brain or plasma concentration was found for any of the five; selectivity is not assessed; no US label was found for tideglusib; paediatric programmes of tideglusib exist as registry statuses only, results not read " + MARK + ".")
    pc["sources"]["external_not_wwox_evidence"] += [
        ("embryonic cortical progenitors, genetic and not pharmacological: siRNA knockdown in one study, gene deletion in the other (blind verifier, full text, 2026-11-20): in utero knockdown of either GSK-3 isoform at embryonic day 14.5 in a subset of cells (ICR mice, three brains) raised the proliferating fraction of electroporated cells; GSK3beta knockdown lowered the intermediate-progenitor and upper-layer-neuron fractions while GSK3alpha knockdown raised the intermediate-progenitor fraction and left the upper-layer fraction unchanged, and the authors say off-target effects of the knockdown reagents are not excluded (Ma 2017); "
         "conditional deletion of GSK3beta on a germline GSK3alpha-null background in neural progenitors gave progenitor over-proliferation and death at birth, which the authors attribute to loss of both isoforms (Kim 2009) " + MARK),
    ]
    pc["next_measurement"] = ("A GSK-3 substrate-phosphorylation panel in the cortex of the Wwox neuronal-deletion line at postnatal day 17 (tau phospho-sites over total tau, Ser9 over total GSK3beta, beta-catenin), designed with a decision per outcome and no data yet (SCI v2.2 and v3.1; a flat panel closes the candidate for this model and age, an elevated panel opens an inhibitor arm); "
        "then an activation-step measurement (reporter, nuclear beta-catenin) in a WWOX-deficient neural system, then the dose-by-timing series " + MARK + ".")
    save("D02_wnt_tankyrase", d)
print("ok")
