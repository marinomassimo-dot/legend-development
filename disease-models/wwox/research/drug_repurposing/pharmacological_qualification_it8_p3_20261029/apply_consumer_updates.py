#!/usr/bin/env python3
"""Applies the three decision changes of IT8 P3 to the consumers (card packets, work order). Idempotent: each edit asserts
that its anchor text is present exactly once or already replaced. After it runs, rebuild the cards and the view:
  python3 framework/scripts/repurposing_bridge.py <packet> > <card>   (done by this script for the touched packets)
  python3 disease-models/wwox/research/drug_repurposing/cards/check_cards.py
Run from the repository root. Prose here uses spelled-out units because check_cards.py refuses digit+unit tokens.
`--help` does nothing else."""
import json, subprocess, sys
from pathlib import Path

if "--help" in sys.argv or "-h" in sys.argv:
    print(__doc__)
    sys.exit(0)

D = Path("disease-models/wwox/research/drug_repurposing")
DOC = "pharmacological_qualification_it8_p3_20261029"


def load(p):
    return json.loads(Path(p).read_text())


def dump(p, o, indent=1):
    Path(p).write_text(json.dumps(o, indent=indent, ensure_ascii=False) + "\n")


def swap(text, old, new, tag, prev=()):
    for p in prev:   # an earlier wording of the same edit (rejected by the shareable audit): migrate in place
        if p in text:
            return text.replace(p, new)
    if new in text:
        return text
    assert text.count(old) == 1, f"{tag}: anchor found {text.count(old)} times"
    return text.replace(old, new)


def seg(text, start, end, new, tag):
    """Replace text[start .. end] (end included) by new; if start is absent and new is present, nothing to do."""
    if new in text:
        return text
    a = text.find(start)
    assert a >= 0, f"{tag}: start marker absent"
    b = text.index(end, a) + len(end)
    return text[:a] + new + text[b:]


# ---- cards -------------------------------------------------------------------------------------------------------------------
def edit_packet(name, fn):
    p = D / "cards" / f"{name}.packet.json"
    o = load(p)
    fn(o)
    dump(p, o)
    card = subprocess.run([sys.executable, "framework/scripts/repurposing_bridge.py", str(p)], capture_output=True, text=True, check=True).stdout
    (D / "cards" / f"{name}.card.json").write_text(card)


def e02(o):
    c = o["p4_card"]
    c["next_measurement"] = seg(
        c["next_measurement"], "Only then a compound arm", "separable from LDH.",
        "Only then a compound arm. IT8 P3 2026-10-29: stiripentol is not carried as the LDH-engagement probe, because the readable enzyme data give 7 percent inhibition at 2 millimolar and about 10 percent at 0.5 millimolar "
        "(no fitted value: no enzyme-level support), the US label names no LDH mechanism, the one cell-level signal found (four rows of a 2022 glycolate-oxidase and LDHA double-inhibitor series: relative oxalate output 0.27 to 0.70 "
        "at 10 micromolar in mouse hepatocytes) does not establish LDH engagement, and the 42 to 500 micromolar range quoted for it is a secondary figure; the arm is a nanomolar human-LDHA inhibitor taken from the ChEMBL target rows "
        f"(every retrieved qualifying molecule is listed by ChEMBL id in {DOC}/measures_detail.tsv, not ranked), with selectivity over LDHB to be established per compound, and stiripentol is kept as a complex I and GABA-A comparator "
        "so that its other pharmacology is separable from LDH.", "e02.next")
    c["pharmacology"] = seg(
        c["pharmacology"], "IT8 P3 2026-10-29 (ChEMBL molecule-first", "no peak concentration). ",
        "IT8 P3 2026-10-29 (ChEMBL molecule-first on the racemate: 28 rows under the type filter IC50, Ki, Kd, EC50, Kb, Potency and Inhibition, 88 unfiltered, none a fitted LDH potency; one comparator document with LDH5 and LDH1 "
        "inhibition of 7 percent at 2 millimolar and no value at 0.5 millimolar; four cell-level rows of another document, mouse hepatocyte oxalate output 0.27 to 0.70 at 10 micromolar, a pathway shared with glycolate oxidase, weighed and not decisive; "
        "the US label of 2026-04-27 states that the human mechanism is unknown and names GABA-A and cytochrome P450 inhibition as possible mechanisms, gives protein binding of 99 percent and no peak concentration). ", "e02.pharm")
    against = c["evidence_for_and_against"]["against"]
    new = ("IT8 P3 (2026-10-29): there is no enzyme-level support for stiripentol as a way to test the LDH node - 7 percent inhibition at 2 millimolar (ChEMBL) and about 10 percent at 0.5 millimolar (independent report), "
           "no fitted LDH potency among its filtered and unfiltered ChEMBL rows, a label that does not name LDH; one cell-level signal (mouse hepatocyte oxalate output at 10 micromolar, shared with glycolate oxidase) is not LDH engagement; "
           "the third report (Sada 2015) remains abstract-only and secondary.")
    for i, t in enumerate(against):
        if t.startswith("IT8 P3 (2026-10-29): the pertinence of stiripentol"):
            against[i] = new
    if new not in against:
        against.append(new)


def e03(o):
    c = o["p4_card"]
    c["next_measurement"] = swap(
        c["next_measurement"], "The same discriminating assay as the ketogenic hypothesis,",
        "IT8 P3 2026-10-29: the probe of the genotype-by-inhibitor arm is a PDK inhibitor of nanomolar potency, not dichloroacetate (see card I01). "
        "The same discriminating assay as the ketogenic hypothesis,", "e03.next")


def i01(o):
    c = o["p4_card"]
    t = c["next_measurement"]
    a = t.find("IT8 P3 2026-10-29: dichloroacetate inhibits")
    if a >= 0:   # earlier wording of the same edit: cut it, then write the current one
        end = "with the free exposure of each measured."
        t = t[:a] + "a free-DCA exposure and a second PDK inhibitor of different chemistry as orthogonal controls." + t[t.index(end, a) + len(end):]
        c["next_measurement"] = t
    c["next_measurement"] = swap(
        c["next_measurement"],
        "a free-DCA exposure and a second PDK inhibitor of different chemistry as orthogonal controls.",
        "IT8 P3 2026-10-29: dichloroacetate inhibits the recombinant human kinase isoforms only at high concentrations in curated database rows (from about 0.1 millimolar for the most sensitive isoform to above 5 millimolar for the least, unknown-origin enzymes, with the same isoform differing about 7 to 18 fold between laboratories), so a null with it at cell-attainable concentrations cannot separate "
        "'the kinase does not matter' from 'the kinase was not inhibited'; the premise experiment therefore uses an inhibitor of nanomolar potency (curated target rows; every retrieved qualifying molecule is listed by id in "
        f"{DOC}/measures_detail.tsv, not ranked, and the kinase pulls are truncated; availability and neuronal engagement are not shown) as the probe and dichloroacetate as the clinically known comparator, with the free exposure of each measured.", "i01.next")


def f03(o):
    c = o["p4_card"]
    o["translation"]["cns_exposure"] = (
        "Mouse primary pharmacokinetics (abstract level, PMID 25449033 and PMID 33279441): brain to plasma ratio about 0.015 to 0.02; at the single intravenous dose reported, far above the human diuretic range, modelled free brain concentrations were in the NKCC1-inhibitory range. Human CSF value UNKNOWN.")
    c["pharmacology"] = seg(
        c["pharmacology"], "IT8 P3 2026-10-29: GtoPdb", "is the exposure target.",
        "IT8 P3 2026-10-29: GtoPdb (human, one document) gives pIC50 5.60 for NKCC1 and 6.48 for the kidney transporter, so the drug is about 7.6 fold more potent on the renal target; mouse brain to plasma ratio about 0.015 to 0.02 "
        "and efflux at the blood-brain barrier (abstract level); at the single intravenous dose reported, far above the diuretic range, modelled free brain concentrations were in the NKCC1-inhibitory range, and diuretic-range doses do not reach neuronal inhibitory concentrations; "
        "a close derivative that does not inhibit NKCC1 reproduces some CNS effects (PMID 30248303), so a CNS effect of the drug is not evidence of NKCC1 action. "
        "A systemic arm is therefore interpretable only if the free brain concentration is measured (the neonatal maturation of the barrier and efflux in the Wwox-null model is not addressed by these sources); the premise test is ex vivo with the drug in the bath, where the NKCC1 range of about 1.5 to 2.5 micromolar is the exposure target.", "f03.pharm")
    nk = o["not_known"]
    for i, t in enumerate(nk):
        if t == "Brain exposure of bumetanide at a relevant dose.":
            nk[i] = "Human brain or CSF exposure of bumetanide (the mouse brain to plasma ratio is about 0.015 to 0.02, abstract level)."
    c["next_measurement"] = swap(
        c["next_measurement"], "discriminating result:",
        "the compound is applied in the bath ex vivo, and a systemic arm is interpretable only with a measured free brain concentration (IT8 P3); discriminating result:", "f03.next",
        prev=("the compound is applied in the bath ex vivo and a systemic arm is not used to test the premise (IT8 P3); discriminating result:",))


edit_packet("E02_ldh_inhibition", e02)
edit_packet("E03_pdk_inhibition_dca", e03)
edit_packet("I01_pdk_inhibition_dca_premise_seizure_glycaemia", i01)
edit_packet("F03_bumetanide_chloride_gradient", f03)

# ---- work order ----------------------------------------------------------------------------------------------------------------
wp = D / "view" / "work_order.json"
w = load(wp)
w["docs"]["IT8-P3"] = {"path": f"{DOC}/README.md", "label": "IT8 P3 record: pharmacological qualification, three decisions changed"}
for e in w["entries"]:
    if e["need"] == "NEED-LACTATE-LDH":
        # the IT7 P6 tests require the card's first sentence and the 'added value' tail to stay in the entry: compose from the original pieces
        O_DATA = ("Card E02 next measurement: lactate and LDH activity in WWOX-deficient human neural cells, the fly Ldh-alone arm and Wwox mRNA in the double line; exposure against the 42 to 500 micromolar LDH range. "
                  "IT7 P6 2026-10-29: read LDHA and LDHB activity separately (LDHB was the discordant gene in the P47T transfer test); no computational ranking selects the compound arm. "
                  "(IT7 P6: the network routes added no value and the signature route was not detected, not excluded.)")
        O_TAIL = ("A computational ranking of compounds does not change this: the IT7 P3 comparison found no added value for the network routes and an effect not detected, not excluded for the signature route, "
                  "so the kind of study and the position of the need are unchanged.")
        e["question"] = ("Is LDH activity or lactate raised in WWOX-deficient neural cells? (IT8 P3 2026-10-29: the former second half of this question, whether stiripentol reaches an inhibitory level at all, "
                         "is answered without enzyme-level support on primary data and is no longer asked of it.)")
        e["data"] = (O_DATA.replace("exposure against the 42 to 500 micromolar LDH range.", "the 42 to 500 micromolar LDH range is withdrawn as an exposure target for stiripentol (IT8 P3, below).")
                     + " IT8 P3 2026-10-29: the compound arm is a nanomolar human-LDHA inhibitor chosen from the curated target rows (selectivity over LDHB to be established per compound); stiripentol stays only as a complex I and GABA-A comparator. "
                     "Datum: enzyme data giving 7 percent inhibition at 2 millimolar and about 10 percent at 0.5 millimolar, no fitted LDH potency among its 28 filtered rows (88 unfiltered; one 2022 cell-level mouse-hepatocyte oxalate-output signal weighed, not decisive), a US label that names no LDH mechanism; "
                     "the 42 to 500 micromolar figure is a secondary range.")
        e["would_change"] = ("If lactate is not raised, the need loses its WWOX observation and E02 moves to P3 by rule; if raised, the node is tested with a nanomolar human-LDHA inhibitor, not with stiripentol (IT8 P3), "
                             "and a stiripentol effect would be read as complex I or GABA-A pharmacology. " + O_TAIL)
        e["summary_it"] = "Capire se lattato o attività LDH sono aumentati nelle cellule neurali prive di WWOX; per lo stiripentolo non c'è sostegno a livello enzimatico da dati primari, e il test del nodo usa un inibitore nanomolare di LDHA umana la cui selettività su LDHB è da stabilire."
    if e["need"] == "NEED-PDH-PYRUVATE-AXIS":
        marker = " IT8 P3 2026-10-29: the probe of the genotype-by-inhibitor arm"
        if marker in e["data"]:
            e["data"] = e["data"][:e["data"].index(marker)]
        e["data"] = e["data"] + (marker + " is an inhibitor of nanomolar potency (curated target rows; qualifying retrieved molecules listed by id in the cycle record, not ranked, kinase pulls truncated), with dichloroacetate as the "
                                 "clinically known comparator, because dichloroacetate inhibits the recombinant human kinase isoforms only at about 0.1 to above 5 millimolar in curated database rows and a null at cell-attainable concentrations would be uninterpretable.")
        if "A null with dichloroacetate alone" not in e["would_change"]:
            e["would_change"] = e["would_change"] + " A null with dichloroacetate alone is not read as absence of a PDK effect."
        e["summary_it"] = "Capire se la fosforilazione di PDH è più alta nelle cellule neurali prive di WWOX e se un inibitore di PDK la modifica in modo dipendente dal genotipo, usando come sonda un inibitore nanomolare e il dicloroacetato come confronto."
    if e["need"] in ("NEED-LACTATE-LDH", "NEED-PDH-PYRUVATE-AXIS"):
        if "IT8-P3" not in e["updated_by"]:
            e["updated_by"].append("IT8-P3")
        if "IT8-P3" not in e["docs"]:
            e["docs"].append("IT8-P3")
        e["date"] = "2026-10-29"
dump(wp, w, indent=2)
print("consumers updated: 4 packets + cards rebuilt, work_order.json (2 entries + docs)")
