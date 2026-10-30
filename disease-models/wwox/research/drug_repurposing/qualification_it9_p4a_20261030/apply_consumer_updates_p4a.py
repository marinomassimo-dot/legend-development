#!/usr/bin/env python3
"""IT9 P4a: restates the three IT8 decisions with the verified formulations in the card packets (E02, E03, I01, F03) and the work order. Idempotent.
Each edit replaces a segment found by start and end markers, or does nothing when the new text is already present. Run from the repository root; it rebuilds the four
cards with the bridge. `--help` prints this text only. Prose uses spelled-out units (check_cards.py refuses digit+unit tokens) and carries no compound-target pair next to
a database marker (the shareable audit refuses it): compound names and ids live in the cycle record, not in the cards."""
import json, subprocess, sys
from pathlib import Path

if "--help" in sys.argv or "-h" in sys.argv:
    print(__doc__)
    sys.exit(0)
D = Path("disease-models/wwox/research/drug_repurposing")
DOC = "qualification_it9_p4a_20261030"


def load(p):
    return json.loads(Path(p).read_text())


def dump(p, o, indent=1):
    Path(p).write_text(json.dumps(o, indent=indent, ensure_ascii=False) + "\n")


def seg(text, start, end, new, tag):
    if new in text:
        return text
    a = text.find(start)
    assert a >= 0, f"{tag}: start marker absent"
    b = text.index(end, a) + len(end)
    return text[:a] + new + text[b:]


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
        c["next_measurement"], "Only then a compound arm. IT8 P3 2026-10-29:", "separable from LDH.",
        "Only then a compound arm. IT8 P3 2026-10-29, restated IT9 P4a 2026-10-30: stiripentol is not sufficiently supported as an LDH-engagement probe, because the readable enzyme data give 7 percent inhibition at 2 millimolar "
        "and about 10 percent at 0.5 millimolar (no fitted value: no enzyme-level support), the US label names no LDH mechanism, and the one cell-level signal found (four rows of a 2022 glycolate-oxidase and LDHA "
        "double-inhibitor series: relative oxalate output 0.27 to 0.70 at 10 micromolar in mouse hepatocytes) does not establish LDH engagement; all 88 curated rows for the racemate were read, 8 concern LDH (4 enzyme-level, 4 cell-level) "
        "and none is a fitted LDH potency; the 42 to 500 micromolar range quoted for it is a secondary figure. The arm is a nanomolar human-LDHA inhibitor taken from the curated database target entries: 205 qualify, "
        "116 have no LDHB datum at all (unknown, not non-selective) and, of the 89 with a same-document LDHA and LDHB pair, 74 have a pair under 10 fold and only 2 are 30 fold or more on every pair, so selectivity over LDHB "
        f"must be established per compound (list by id in {DOC}/ldha_nanomolar_selectivity.tsv); stiripentol is kept as a complex I and GABA-A comparator so that its other pharmacology is separable from LDH.", "e02.next")


def e03(o):
    c = o["p4_card"]
    c["next_measurement"] = seg(
        c["next_measurement"], "IT8 P3 2026-10-29: the probe of the genotype-by-inhibitor arm", "(see card I01). ",
        "IT8 P3 2026-10-29, restated IT9 P4a 2026-10-30: a nanomolar inhibitor is added alongside dichloroacetate for the genotype-by-inhibitor arm (see card I01). ", "e03.next")


def i01(o):
    c = o["p4_card"]
    t = c["next_measurement"]
    if "pdk_*.tsv)." in t and "3 to 10 fold" in t:   # intermediate wording of this same edit: cut back to the end marker
        t = t.replace("pdk_*.tsv).", "pdk_*.tsv).")
        a = t.find("IT8 P3 2026-10-29")
        t = t[:a] + "IT8 P3 2026-10-29: XX with the free exposure of each measured." + t[t.index("pdk_*.tsv).", a) + len("pdk_*.tsv)."):]
        c["next_measurement"] = t
    c["next_measurement"] = seg(
        c["next_measurement"], "IT8 P3 2026-10-29", "with the free exposure of each measured.",
        "IT8 P3 2026-10-29, restated IT9 P4a 2026-10-30: dichloroacetate inhibits the recombinant human kinase isoforms only at high concentrations in curated database rows (from about 0.1 millimolar for the most sensitive isoform to above 5 millimolar for the least, "
        "unknown-origin enzymes, with the same isoform differing about 7 to 18 fold between laboratories), so a null with it alone at cell-attainable concentrations cannot separate 'the kinase does not matter' from 'the kinase was not inhibited'. "
        "A more potent inhibitor can make the experiment more interpretable than dichloroacetate alone: in the one document that measured both on all four isoforms, a nanomolar pan-isoform research inhibitor gave about 20 to 170 nanomolar "
        "against 0.1 to above 5 millimolar for dichloroacetate (the second-isoform assay used a different substrate), and the same inhibitor varies about 3 to 11 fold between documents. The caveats are that it is pan-isoform (no isoform attribution), "
        "that its availability for research use is not stated by the sources, and that neuronal engagement and brain exposure are not shown. It is therefore added alongside dichloroacetate as the probe, "
        f"with the free exposure of each measured (names, ids and rows in {DOC}/pdk_*.tsv).", "i01.next")


def f03(o):
    c = o["p4_card"]
    c["pharmacology"] = seg(
        c["pharmacology"], "A systemic arm is therefore interpretable only", "is the exposure target.",
        "A systemic bumetanide response therefore requires verification of relevant exposure, that is a free brain concentration in the NKCC1 range of about 1.5 to 2.5 micromolar; arithmetic from the mouse figures (brain unbound fraction 6 to 17 percent for three diuretics, "
        "brain to plasma ratio about 0.015 to 0.02) puts the corresponding total brain concentration at about 9 to 42 micromolar, an assumption-bound figure and not a prediction (the neonatal maturation of the barrier and efflux in the Wwox-null model is not addressed by these sources; "
        "the human plasma concentration is not stated in the US label excerpt read, so it is UNKNOWN here). The premise test is ex vivo with the drug in the bath, where the NKCC1 range of about 1.5 to 2.5 micromolar is the exposure target.", "f03.pharm")
    c["next_measurement"] = seg(
        c["next_measurement"], "the compound is applied in the bath ex vivo", "(IT8 P3);",
        "the compound is applied in the bath ex vivo, and a systemic response requires verification of relevant exposure (IT8 P3, restated IT9 P4a);", "f03.next")


edit_packet("E02_ldh_inhibition", e02)
edit_packet("E03_pdk_inhibition_dca", e03)
edit_packet("I01_pdk_inhibition_dca_premise_seizure_glycaemia", i01)
edit_packet("F03_bumetanide_chloride_gradient", f03)

wp = D / "view" / "work_order.json"
w = load(wp)
w["docs"]["IT9-P4a"] = {"path": f"{DOC}/README.md", "label": "IT9 P4a record: LDHB selectivity, PDK profile, stiripentol and bumetanide restated"}
for e in w["entries"]:
    if e["need"] == "NEED-LACTATE-LDH":
        e["data"] = seg(e["data"], "IT8 P3 2026-10-29: the compound arm", "the 42 to 500 micromolar figure is a secondary range.",
            "IT8 P3 2026-10-29, restated IT9 P4a 2026-10-30: the compound arm is a nanomolar human-LDHA inhibitor chosen from the curated target entries (205 qualify; 116 have no LDHB datum, 89 have a same-document LDHA and LDHB pair, "
            "of which only 2 are 30 fold or more on every pair, so selectivity over LDHB is to be established per compound); stiripentol stays only as a complex I and GABA-A comparator. Datum: enzyme data giving 7 percent inhibition at 2 millimolar "
            "and about 10 percent at 0.5 millimolar, no fitted LDH potency among its 88 curated rows (all read; one 2022 cell-level mouse-hepatocyte oxalate-output signal weighed, not decisive), a US label that names no LDH mechanism; "
            "stiripentol is not sufficiently supported as an LDH-engagement probe; the 42 to 500 micromolar figure is a secondary range.", "wo.lactate")
    if e["need"] == "NEED-PDH-PYRUVATE-AXIS":
        e["data"] = seg(e["data"], " IT8 P3 2026-10-29: the probe of the genotype-by-inhibitor arm", "would be uninterpretable.",
            " IT8 P3 2026-10-29, restated IT9 P4a 2026-10-30: a nanomolar pan-isoform inhibitor is added alongside dichloroacetate for the genotype-by-inhibitor arm, because dichloroacetate inhibits the recombinant human kinase isoforms only at about 0.1 to above 5 millimolar "
            "in curated database rows and a null with it alone at cell-attainable concentrations would be uninterpretable, whereas in the one document that measured both on all four isoforms the inhibitor acts at about 20 to 170 nanomolar; "
            "caveats: pan-isoform (no isoform attribution), availability for research use not stated by the sources, neuronal engagement and brain exposure not shown, second-isoform assay on a different substrate.", "wo.pdh")
        e["summary_it"] = "Capire se la fosforilazione di PDH è più alta nelle cellule neurali prive di WWOX e se un inibitore di PDK la modifica in modo dipendente dal genotipo, aggiungendo un inibitore nanomolare pan-isoforma accanto al dicloroacetato (con riserve su selettività e disponibilità)."
    if e["need"] in ("NEED-LACTATE-LDH", "NEED-PDH-PYRUVATE-AXIS"):
        if "IT9-P4a" not in e["updated_by"]:
            e["updated_by"].append("IT9-P4a")
        if "IT9-P4a" not in e["docs"]:
            e["docs"].append("IT9-P4a")
        e["date"] = "2026-10-30"
dump(wp, w, indent=2)
print("IT9 P4a consumer edits applied (4 packets rebuilt, work order 2 entries + docs)")
