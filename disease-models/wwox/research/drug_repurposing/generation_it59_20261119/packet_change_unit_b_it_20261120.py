"""IT59 (2026-11-20): ONE second packet change (ADV accepted, scope: the ethosuximide card and the clemastine / thyromimetic card, from the verified HE batches 1 to 6): class-level exposure and pharmacology facts only,
each labelled NOT WWOX EVIDENCE, no dose, no score; the card-checker's dose-looking-token rule is kept (units are written out, no dose is carried). Cards EB-ETX-01 (unit U17, cards_early) and F02 (myelination agents, cards).
Not carried by design: the pragmatic-null and tolerance-limited rules (design, in v3.1), any statement that the GSK-3 panel is elevated, HE batch 10 (identity only). Rebuild the cards with the bridge afterwards. Idempotent."""
import json
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
MARK = "[IT59 2026-11-20 unit B packet change]"

def load(p): return json.loads(p.read_text(encoding="utf-8"))
def save(p, d): p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# ---- EB-ETX-01
pe = DR / "cards_early" / "EB-ETX-01.packet.json"; e = load(pe)
if MARK not in json.dumps(e):
    r = e["p4_roadmap_fields"]
    r["pharmacology"] += (" Class-level exposure and potency facts, no dose, no score, NOT WWOX EVIDENCE " + MARK + ": in male Swiss mice of 24 to 30 grams (no age given), total brain ethosuximide was 134.9 micrograms per gram of wet tissue (about 0.96 millimolar as total tissue, not a free concentration; the brain was homogenised 1 to 2 in water and no dilution correction is stated) "
        "at the time scheduled for a seizure test, 45 minutes after an intraperitoneal dose that was about half the dose of the one Wwox experiment (arithmetic; the value is the saline co-treated arm of a mouse interaction study of another question, PMID 22315091); in the mouse, serum and brain concentrations equilibrate within minutes and the half-life is about one hour (an old abstract-level report). "
        "Potency at T-type channels is reported inconsistently in the sources read, by different assays that are not comparable: about six-tenths of a millimolar in a ChEMBL row without a mapped gene (SCI's reading of the primary paper reports a persistent current in recombinant human channels) against above five millimolar in one FLIPR assay at one channel subtype (one ChEMBL transcription). "
        "PUP EXPOSURE IS UNKNOWN: no juvenile exposure of any kind was found by the routes read, and the age of the one Wwox drug experiment is not stated; the first measurement an exposure-controlled test needs is the brain exposure at the regimen of that experiment. "
        "Label (openFDA record, newest 2026-05-25): indicated for absence seizures; safety and effectiveness below the age of three years not established.")
    e["not_known"] = [("exposure and CNS exposure in a pup or in WOREE (a total brain value exists in male Swiss mice of 24 to 30 grams, no age given; potency at T-type channels is reported inconsistently; nothing was found for a pup or for WOREE by the routes read) " + MARK) if s == "exposure and CNS exposure" else s for s in e["not_known"]]
    assert any(MARK in s for s in e["not_known"])
    save(pe, e)

# ---- F02 (clemastine and thyromimetics, class level)
pf = DR / "cards" / "F02_myelination_activity_sign.packet.json"; f = load(pf)
if MARK not in json.dumps(f):
    assert f["p4_card"]["pharmacology"] == "Not assessed: no compound is carded."
    f["p4_card"]["pharmacology"] = (
        "NOT WWOX EVIDENCE, class level, no dose, no score, no compound carded " + MARK + ". CLEMASTINE (public-database rows of HE ADV-098 batch 6 and SCI's verified reading of primary papers): strong histamine H1 and muscarinic binding; within one document muscarinic M1 is the most potent of five subtypes with a six-fold range, an indication of M1 preference and not an identified selectivity; "
        "no measured myelination or oligodendrocyte-precursor differentiation row exists in those rows (the link from M1 antagonism to differentiation is mechanism from the literature). Exposure: a total plasma Cmax of 44.0 ng/mL in the neonatal mouse at steady state of one daily oral regimen, dosed on the fumarate salt basis, that was not the lowest dose tested (Odell 2024, read at source by a blind verifier); no unbound and no brain value in that paper; "
        "juvenile rat brain detection is qualitative only (one paper, inconsistent about the age). Harm: in the healthy developing mouse, at the single higher dose described, slower conduction with fewer nodes, more differentiated cells and thinner myelin in thin axons (one dose only, so no margin can be read). "
        "Label (US label record, public database): clemastine fumarate syrup for allergic rhinitis, paediatric use confirmed from 6 to 12 years for that indication (labels in other countries differ). "
        "THYROMIMETICS: thyroid-hormone-receptor beta preference depends on the readout (sobetirome: seven of eight same-document pairs beta-preferring by 3.4- to 26-fold, one reversed; tiratricol: beta-preferring by about three-fold in binding and alpha-preferring in one reporter assay); the natural hormone is about equipotent on both receptors in nearly every same-document pair; no measured myelination row in those rows; "
        "papers exist on brain delivery of sobetirome prodrugs after systemic dosing in mice (the abstract gives no age) and on tiratricol brain content after intracerebroventricular delivery in Mct8-deficient mice (titles and abstracts read, numbers not read; a different disease context); a late start gave no myelination gain in one small mouse study of thyroid-hormone transporter deficiency, so the window may matter; "
        "label: tiratricol is authorised for peripheral thyrotoxicosis in MCT8 deficiency (a different disorder; nothing about myelination); none found for sobetirome.")
    f["not_known"].append("Brain exposure of clemastine or of a thyromimetic in a Wwox-deficient pup, or in any neonatal or juvenile mouse: unknown (a total plasma value in the neonatal mouse was found for clemastine; none was found for the thyromimetics by the routes read, where papers on juvenile tiratricol dosing in Mct8-deficient mice exist with numbers not read; no neonatal brain concentration was found for either class) " + MARK + ".")
    save(pf, f)
print("ok")
