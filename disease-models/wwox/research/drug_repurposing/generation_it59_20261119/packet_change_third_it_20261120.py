"""IT59 (2026-11-20): ONE third packet change (ADV approved: cards E01, L01, E03, I01, M01 and F02 from the verified HE batches 7, 8 and 10 and the COMPARABLE? lines; plus the three unaudited scope
clarifications of the D02 sentences and the correction of IT's own earlier wording on the GSK-3 panel). Class-level facts only, each labelled NOT WWOX EVIDENCE, no dose, no score; the card checker's
dose-looking-token rule is kept (units are written out, no dose is carried). Rebuild the cards with the bridge afterwards. An idempotent script skips text already committed: to repair committed text,
the packet JSON is patched in place (string replace) and asserted. Sources: advisor_pilot_20261113/adv098_agent_sheets_he_20261119/BATCH7, BATCH8 and BATCH10 sheets (HE)."""
import json
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
MARK = "[IT59 2026-11-20 third packet change]"

def load(p): return json.loads(p.read_text(encoding="utf-8"))
def save(p, d): p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def add(path, field_path, text):
    """Append text to a p4_card string field once (marker-guarded)."""
    d = load(path)
    if MARK in json.dumps(d):
        return
    node = d
    for k in field_path[:-1]:
        node = node[k]
    node[field_path[-1]] += text
    save(path, d)

def add_not_known(path, text):
    d = load(path)
    if any(MARK in s for s in d["not_known"]):
        return
    d["not_known"].append(text + " " + MARK)
    save(path, d)

# ---- E01 (ISR modulators: ISRIB, trazodone as an ISR claim)
pe = DR / "cards" / "E01_isr_modulators.packet.json"
if MARK not in json.dumps(load(pe)):
    d = load(pe)
    d["p4_card"]["pharmacology"] += (
        " Added class-level facts, no dose, no score, NOT WWOX EVIDENCE " + MARK + " (HE ADV-098 batches 7 and 8, public-database rows, hypothesis level): "
        "ISRIB is not found by name in the identity tool and is identified by structure; the database holds ONE row for it, an ATF4 reporter in human H4 cells after 24 hours with an IC50 of 2.7 nanomolar (one document): a cell readout of the stress-response output, not a binding and not an eIF2B measurement. "
        "No eIF2B activity row, no binding or selectivity row, no value in neurons and none from a second laboratory were found by those routes (not found by these routes is not absence); no measured brain or plasma concentration of ISRIB was found, and the one PubMed hit for brain pharmacokinetics was an unrelated neuropathology paper by its title. No label is expected (a research compound). "
        "TRAZODONE: the database holds 284 rows, with 5-HT2A, 5-HT1A, D2 and 5-HT2B among the main groups; no row measures PERK, eIF2 alpha phosphorylation or any integrated stress response assay, so the stress-response link is the literature's and not measured here; two papers disagree by title (a 2017 mouse report that repurposed drugs targeting eIF2 alpha phosphorylation prevent neurodegeneration, and a 2025 paper titled as reporting that trazodone, dibenzoylmethane and tauroursodeoxycholic acid do not prevent motor dysfunction and neurodegeneration (the sheet cuts the title; neither read)). "
        "The serotonin 5-HT2A potency differs about twelve-fold by assay type on the sheet's figure (a binding IC50 of 20 nanomolar against 243 nanomolar in a cyclic-AMP assay), so the same receptor does not give one number. Label (openFDA record, newest 2026-07-14): adults with major depressive disorder; safety and effectiveness in the paediatric population not established, with the antidepressant boxed warning on suicidality in children.")
    d["not_known"].append("Whether ISRIB or any eIF2B activator reaches or acts in a Wwox-deficient neural cell: the database holds one cell-reporter row for ISRIB, no eIF2B row and no exposure value; trazodone has no stress-response row " + MARK + ".")
    save(pe, d)

# ---- L01 (NRF2 axis: omaveloxolone)
pl = DR / "cards" / "L01_nrf2_axis.packet.json"
if MARK not in json.dumps(load(pl)):
    d = load(pl)
    d["p4_card"]["pharmacology"] += (
        " Added class-level facts, no dose, no score, NOT WWOX EVIDENCE " + MARK + " (HE ADV-098 batch 8, database rows): the database holds TWO potency rows for omaveloxolone, both anti-necroptotic cell readouts of one 2021 document (EC50 1.41 micromolar in human HT-29 cells and 5.25 micromolar in mouse L929 cells); no KEAP1 or NRF2 row at all was found by those routes, so the NRF2 mechanism is the literature's and is not measured in these rows. "
        "Two searches for a brain concentration (one of them specific to mice) found no record (two query shapes). Label (openFDA record, effective 2026-04-06): Friedreich's ataxia in adults and adolescents of 16 years and older; effectiveness established from age 16 and nothing for younger children.")
    d["not_known"].append("Whether omaveloxolone acts on NRF2 at a measured concentration in a mouse or human neural cell: no KEAP1 or NRF2 potency row and no mouse brain concentration were found by the routes read " + MARK + ".")
    save(pl, d)

# ---- E03 (PDK inhibition, dichloroacetate)
p3 = DR / "cards" / "E03_pdk_inhibition_dca.packet.json"
if MARK not in json.dumps(load(p3)):
    d = load(p3)
    d["p4_card"]["pharmacology"] += (
        " Added class-level facts, no dose, no score, NOT WWOX EVIDENCE " + MARK + " (HE ADV-098 batch 8, database rows): dichloroacetic acid acts at millimolar concentrations in most rows read (the fibroblast EC50 below is sub-millimolar). Within ONE 2017 document (an enzyme-linked assay on full-length PDHA1 as substrate, 30 minutes) the IC50 is 1.03 millimolar for PDK1, 0.50 for PDK2 and 5.56 for PDK3: an eleven-fold range across isozymes in one assay, a comparable contrast; "
        "an older row gives more than 2 millimolar against PDK in vitro and an EC50 of 100 micromolar in normal human dermal fibroblasts, a different readout, with no order between the two documents read; Five leukaemia cell-line rows give 8 to 14 millimolar (MTT cytotoxicity, 48 hours, 2016). "
        "No brain concentration of dichloroacetate in mice and no juvenile exposure were found (the rat brain PDK distribution paper of 1984 and a rat GSTZ1 paper are by title only; one neonatal query found no record); the openFDA label route returned no match for dichloroacetic acid, a statement about that route and not about development status.")
    save(p3, d)

# ---- I01 (PDK inhibition, premise, seizure and glycaemia): the exact statement ADV required, and the DCA pointer
pi = DR / "cards" / "I01_pdk_inhibition_dca_premise_seizure_glycaemia.packet.json"
if MARK not in json.dumps(load(pi)):
    d = load(pi)
    d["p4_card"]["pharmacology"] += (
        " Added class-level facts, no dose, no score, NOT WWOX EVIDENCE " + MARK + " (HE ADV-098 batch 8): in one 2017 document the IC50 of dichloroacetic acid is 0.50 to 5.56 millimolar across PDK1, PDK2 and PDK3 (an eleven-fold range in one assay); no brain concentration in mice and no juvenile exposure were found by the routes read.")
    d["p4_card"]["next_measurement"] += (
        " THE METABOLIC AXIS IS NEITHER PROMOTED NOR PARKED ON HELD DATA " + MARK + ": no glucose measurement in the neuron-targeted deletion line (S-KO) or the progenitor-targeted deletion line (N-KO) was found in the held texts searched; no held text searched manipulates glycaemia or the PDH axis and reads a seizure or a survival endpoint (the appendix glucose panels and some figure values are not held as text, so figures are not covered); "
        "the decisive datum is blood glucose from postnatal day 7 with same-animal EEG from postnatal day 9 (the earliest glucose anywhere in the held literature is day 10, a plot reading by the ADV-074 producer not re-read by SCI, and the seizures of the neuronal-deletion line start at day 9); the preregistration and the first reading are SCI's ADV-101 documents, folder advisor_pilot_20261113/brainstorm_20261116/glycaemia_axis_adv101_sci_20261120/. "
        "Wild-type glucose differs about two-fold between laboratories, so no absolute hypoglycaemia severity is compared across papers. The dichloroacetate seizure datum already on this card (abstract level, adult mice, negative or slightly proconvulsant) is a PDH-axis manipulation with a seizure readout outside the held full texts searched.")
    d["not_known"].append("Whether glucose is lower in the Synapsin-Cre or Nestin-Cre line before or at seizure onset (no measurement in the held texts searched), and whether any manipulation of glycaemia or PDH moves a seizure or survival endpoint there (none found in the held texts searched) " + MARK + ".")
    save(pi, d)

# ---- M01 (neurogenic output and MYC window): 10058-F4 as a literature compound, no compound carded
pm = DR / "cards" / "M01_neurogenic_output_myc_window.packet.json"
if MARK not in json.dumps(load(pm)):
    d = load(pm)
    d["p4_card"]["pharmacology"] += (
        " Added class-level facts, no compound carded, no dose, no score, NOT WWOX EVIDENCE " + MARK + " (HE ADV-098 batch 10; identity by structure, not found by name; the geometric form each study used is not resolved): "
        "10058-F4, named in the literature as a MYC-MAX dimerisation inhibitor, has FIVE rows in the database (one without a value), all cell growth after 96 hours in one 2025 document: 35.1 to 59.5 micromolar for the four with a value, with MYC-expressing P493-6 cells 1.7-fold more sensitive than the same cells with MYC repressed (one document, a weak dependence); no row on MYC, MAX or MYC-MAX dimerisation was found by those routes, and none is asserted. "
        "In mice with prostate-cancer xenografts (abstract read, intravenous route) the plasma peak was about 300 micromolar at 5 minutes with a terminal half-life of about one hour, tissue values were highest in fat, lung, liver and kidney, the tumour peak was at least ten-fold lower than the plasma peak, and no significant tumour growth inhibition was seen at the two doses tested; the abstract says the lack of activity may have resulted from rapid metabolism and low tumour concentration, brain is not named, and the full text was not read. "
        "No label and no clinical trial were found. Two other agents of the same batch, tazemetostat (an EZH2 inhibitor; the abstract of a mouse study says P-glycoprotein limits its brain accumulation, no brain concentration figure found by these routes; the abstract names the compound EPZ-6438 and the identity with tazemetostat is the sheet's; label: epithelioid sarcoma from age 16, follicular lymphoma in adults) and TMP195 (a class IIa HDAC inhibitor, no exposure found by these routes), have no card and are carried as open-question lines only.")
    d["not_known"].append("Whether 10058-F4 or any selective MYC lever reaches a Wwox-deficient neural progenitor at a measured concentration: five growth rows, no MYC-MAX row, no brain value in the abstract read " + MARK + ".")
    save(pm, d)

# ---- F02 (myelination agents: benztropine, miconazole, clobetasol, bexarotene)
pf = DR / "cards" / "F02_myelination_activity_sign.packet.json"
f = load(pf)
if MARK not in json.dumps(f):
    f["p4_card"]["pharmacology"] += (
        " Added class-level facts, no compound carded, no dose, no score, NOT WWOX EVIDENCE " + MARK + " (HE ADV-098 batch 7, database rows and label records): four agents with four different mechanisms, so no potency comparison across them. "
        "None of the four has a database row that measures an oligodendrocyte-differentiation or myelination effect: the potency rows are the primary-target rows and are not the myelination mechanism (the link is literature; for the agents whose literature the sheet lists it was read at title level only). "
        "BENZTROPINE: muscarinic M1 Ki of 0.59 and 0.95 nanomolar in rat brain membranes and 0.13 nanomolar in a human panel (a seven-fold spread between sources); pharmacokinetic and brain-distribution hits found by title for benztropine analogs only, none for benztropine itself by these routes; label: caution in paediatric patients over three years. "
        "MICONAZOLE: a human CYP51 IC50 of 200 nanomolar (lanosterol demethylase in a cell system, 2007) is among the rows, the largest row groups being other cytochromes and a transporter, and the sterol-pathway mechanism proposed for oligodendrocyte differentiation is not found in the rows; no rodent concentration found; the label is a topical over-the-counter antifungal, which says nothing about CNS exposure. "
        "CLOBETASOL PROPIONATE (read separately from the parent record): glucocorticoid receptor IC50 3.17 nanomolar in rat liver cytosol against Ki 0.66 nanomolar in a human panel (different species and sources); no rodent brain concentration of the plain compound found (central delivery is said to be a formulation problem by one paper read at title level only); label: topical, not recommended under 12 years. "
        "BEXAROTENE: within one 1997 document the RXR-beta, RXR-gamma and RXR-alpha Ki values (5.9, 8.3 and 16 nanomolar) against 180 nanomolar for RAR-alpha give an eleven- to thirty-fold RXR preference, a comparable contrast; other documents give RXR-alpha EC50 of 28 and 42 nanomolar; a mouse plasma and brain quantification method paper exists (numbers not read); label: cutaneous T-cell lymphoma, paediatric safety and effectiveness not established.")
    f["not_known"].append("Brain exposure of benztropine, miconazole, clobetasol or bexarotene in a neonatal or juvenile mouse: not found by the routes read (a mouse brain quantification method exists for bexarotene, numbers not read) " + MARK + ".")
    save(pf, f)

# ---- D02: the three scope clarifications of the nine-statement audit are already in the packet (marker section of the recheck branch); here ONLY the GSK-3 panel wording is corrected in place.
pd = DR / "cards" / "D02_wnt_tankyrase.packet.json"
OLD = "a flat panel closes the candidate for this model and age, an elevated panel opens an inhibitor arm"
NEW = "a flat panel excludes ONE proposition only (that GSK-3 beta restraint on tau is released in bulk cortex of the neuronal-deletion line at postnatal day 17, at the tested tau sites, above the margin fixed before data) and does not close the candidate or the class, an elevated panel is the condition under which an inhibitor arm exists; the earlier wording 'closes the candidate' is corrected on SCI's v3.1 section 6.10 " + MARK
s = pd.read_text(encoding="utf-8")
if OLD in s:
    s = s.replace(OLD, NEW)
    pd.write_text(s, encoding="utf-8")
assert NEW in pd.read_text(encoding="utf-8") or OLD not in pd.read_text(encoding="utf-8")
print("ok")
