#!/usr/bin/env python3
"""Apply the V12 recheck residual corrections (SCI49 package B) cell by cell; idempotent.

Run from this folder: python3 apply_v12_recheck.py. Every change is appended to CORRECTIONS.tsv.
Narrative files are corrected by dated sections appended by the same run (guarded by a marker).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = "verify/verdicts.tsv item R / audit.md section 10"
T = {
 ("compounds.tsv", "C17", "human_use_status"): ("approved", "approved is recollection (not in the abstract); the verifier read an abstract only"),
 ("compounds.tsv", "C18", "potency_value_unit_and_conditions"): ("30 uM: +66.4 percent inward (-120 mV), +60.4 percent outward (-50 mV), n=6", "30 uM: +66.4 percent inward (-120 mV), +60.4 percent outward (-50 mV); n=6 belongs to the counter-screen, not to the potency"),
 ("compounds.tsv", "C18", "human_use_status"): ("approved (veterinary/anthelmintic context; status not checked)", "not stated in the sources read (status not checked)"),
 ("compounds.tsv", "C21", "human_use_status"): ("approved", "not stated in the abstract read (status not checked)"),
 ("compounds.tsv", "C24", "compound_name"): ("VU6073995 and five chemotypes from the 2026 HTS paper", "VU6073995 and a second selected hit from the 2026 HTS paper (the abstract gives six scaffolds from 48 hits)"),
 ("compounds.tsv", "C25", "potency_value_unit_and_conditions"): ("0.24 uM; >40-fold over Kir4.1, >=10-fold over ten other Kir", "0.24 uM; >40-fold over Kir4.1, pore block (the >=10-fold over ten other Kir figure belongs to the screening hit VU0493690, not to VU6036720; selectivity over other Kir not stated)"),
 ("compounds.tsv", "C25", "counter_screen"): ("as potency", "over Kir4.1 only, as printed in the full abstract"),
 ("roles.tsv", "dronedarone", "what_it_can_discriminate"): ("nothing", "Kir2.1 from Kir2.2/2.3 as a blocker in oocytes (abstract of the ChEMBL-cited paper), slow onset, multi-channel drug"),
 ("roles.tsv", "dronedarone", "what_it_cannot"): ("everything", "attribute a conductance in a neuron (no native evidence; other channels)"),
 ("roles.tsv", "dronedarone", "missing_datum_that_would_change_the_role"): ("a primary source with a Kir2 assay", "the full text of the cited paper and a counter-screen against other Kir and hERG"),
}
OQ = {
 "OQ1": {
  "question": "Does the ML133-sensitive part of the Ba2+ difference current (or of the Ba2+-induced rise in Rin) in L2/3 pyramidal neurons at P13-P17 survive the removal of KATP (glibenclamide) and a hERG-sparing condition, and is the recombinant-like positive control reproduced in the same bath on the same day?",
  "decisive_measure_if_experimental": "Rin or holding current before and after Ba2+ at a stated concentration, ML133 over a concentration range with glibenclamide present, a positive control preparation recorded with the same bath solution (Kir2.1-expressing cells or an identified Kir2-dominant native cell), and (if the site of action permits, not verified) pipette versus bath delivery in the recorded neuron",
 },
 "OQ5": {
  "linked_compound_or_comparison_or_thread": "VU6036720 (Kir4.1/5.1, full text unread) rather than VU0134992 (equal activity on Kir3 and Kir4.2); K7",
 },
}
NARR = {
 "hypotheses.md": ("<!-- v12-recheck -->", """

## Recheck by V12 and final form of H1 (Orchestrator, 2026-11-12; the sections above are kept)
The blind verifier's recheck found H1 not yet fully discriminating. Final form handed on as a **conditional hypothesis, family-level mechanism test, direction of benefit unused**: (1) **KATP arm** - Kir6.2/SUR1 is Ba2+-sensitive and ML133-sensitive (7.7 uM; the ML133 paper itself advises removing KATP with glibenclamide first), so 'the ML133 effect is occluded by Ba2+' does not separate Kir2 from KATP; the test is run with glibenclamide present; (2) **hERG** is within about 2.7-fold of Kir2.1 on the same automated platform: report the voltage range and keep the test in the subthreshold range; (3) **positive control** defined: a preparation in which Kir2 is established (Kir2.1-expressing cells, or an identified Kir2-dominant native cell) recorded the same day with the same bath ML133 solution, readout the ML133-sensitive inwardly rectifying current; (4) **bath versus pipette logic, corrected**: a blocker in the pipette reaches only the recorded neuron, so an effect that persists with pipette delivery is neuronal, and bath-only delivery cannot separate neuron from glia (whether pipette delivery of ML133 works is not verified; it depends on the site of action); (5) the pH 6.5 arm stays withdrawn. Alternatives named: K2P/TASK, KATP, glial Kir4.1/Kir2.1 with indirect action through K+ handling. Rejected by: no ML133-sensitive part of the Ba2+ difference once KATP is removed, or a positive control that fails. Decision changed: whether ladder step 2b needs a Kir2-directed step. Novelty: (a) new combination for LEGEND, (b) not checked, (c) unvalidated.
"""),
 "gaps.md": ("<!-- v12-recheck -->", """

## Recheck correction (2026-11-12)
The sentence that all direct-mechanism activators are restricted to homotetrameric Kir2.1 and spare heteromers over-generalises: the Kir2.1+2.2 and Kir2.1+2.3 heteromer test exists for **flecainide** only (not increased, n=10); for propafenone and timolol only Kir2.2/2.3 homomers (propafenone) or the Cys311 interaction (timolol) are reported at abstract depth. Blocker role as the verifier would accept it: ML133 blocks the recombinant Kir2 family (IC50 1.9-4.0 uM at pH 7.4; Kir2.4 untested), spares Kir1.1, Kir4.1 and Kir7.1 by 17- to more than 150-fold, also blocks Kir6.2/SUR1 (7.7 uM) and hERG (about 5 uM in a PubChem automated-patch deposit of unstated final pH; about 2.7-fold more potent than Kir2.1 on the same platform), has no K2P or cortical-neuron test and is limited by its authors to in vitro use: a family-level comparator probe that can attribute a conductance to 'Kir2 family or KATP/hERG-type' only after those are excluded.
"""),
 "answers.md": ("<!-- v12-recheck -->", """

## Recheck correction (2026-11-12, Orchestrator)
V12 recheck count: 87 verdict lines (60 first-pass rows including one source_silent, 27 item-R rows). The activator sentence is corrected: flecainide, propafenone (EC50 12 nM, abstract level) and timolol raise Kir2.1 current through Cys311 in recombinant cells and spare Kir2.2/2.3 homomers; **only flecainide was tested on Kir2.1+2.2 and Kir2.1+2.3 heteromers (not increased)** and on native guinea-pig ventricular IK1 (+19.5 percent); none is tested in neurons; flecainide and propafenone are also Na+ channel blockers; zacopride, tetramisole (rat myocytes) and sildenafil (Kir2.2 at 10 uM, mixed effect) are claims without a direct mechanism. H1 in its final form is in `hypotheses.md`; OQ1 and OQ5 are rewritten accordingly.
"""),
}


def edit_tsv(fname, key_col, key_val, field, new, log, reason):
    path = os.path.join(HERE, fname)
    lines = open(path, encoding="utf-8").read().split("\n")
    head = lines[0].split("\t")
    kc, fc = head.index(key_col), head.index(field)
    for i, line in enumerate(lines[1:], 1):
        cells = line.split("\t")
        if len(cells) == len(head) and cells[kc] == key_val:
            if cells[fc] == new:
                return
            before = cells[fc]
            cells[fc] = new
            lines[i] = "\t".join(cells)
            open(path, "w", encoding="utf-8").write("\n".join(lines))
            log.append((fname, key_val, field, before, new, reason, SRC))
            return
    sys.exit(f"{fname}: {key_val} not found")


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        return
    log = []
    for (f, k, fld), (_, reason) in sorted(T.items()):
        # the 'after' text is the second element of the tuple's partner; see below
        pass
    NEW = {
     ("compounds.tsv", "C17", "human_use_status"): "not stated in the abstract read (class and use are recollection)",
     ("compounds.tsv", "C18", "potency_value_unit_and_conditions"): "30 uM: +66.4 percent inward (-120 mV), +60.4 percent outward (-50 mV); n=6 belongs to the counter-screen, not to the potency",
     ("compounds.tsv", "C18", "human_use_status"): "not stated in the sources read (status not checked)",
     ("compounds.tsv", "C21", "human_use_status"): "not stated in the abstract read (status not checked)",
     ("compounds.tsv", "C24", "compound_name"): "VU6073995 and a second selected hit from the 2026 HTS paper (the abstract gives six scaffolds from 48 hits)",
     ("compounds.tsv", "C25", "potency_value_unit_and_conditions"): "0.24 uM; >40-fold over Kir4.1, pore block (the >=10-fold figure belongs to the screening hit VU0493690; selectivity over other Kir not stated)",
     ("compounds.tsv", "C25", "counter_screen"): "over Kir4.1 only, as printed in the full abstract",
     ("roles.tsv", "dronedarone", "what_it_can_discriminate"): "Kir2.1 from Kir2.2/2.3 as a blocker in oocytes (abstract of the ChEMBL-cited paper); slow onset; multi-channel drug",
     ("roles.tsv", "dronedarone", "what_it_cannot"): "attribute a conductance in a neuron (no native evidence; other channels)",
     ("roles.tsv", "dronedarone", "missing_datum_that_would_change_the_role"): "the full text of the cited paper and a counter-screen against other Kir and hERG",
    }
    for (f, k, fld), (_, reason) in T.items():
        key_col = "compound" if f == "roles.tsv" else "row_id"
        edit_tsv(f, key_col, k, fld, NEW[(f, k, fld)], log, reason)
    for oq, cells in OQ.items():
        for fld, new in cells.items():
            edit_tsv("open_questions.tsv", "oq_id", oq, fld, new, log, "V12 recheck: OQ1 stale pH arm / OQ5 compound link")
    for fname, (marker, text) in NARR.items():
        p = os.path.join(HERE, fname)
        body = open(p, encoding="utf-8").read()
        if marker not in body:
            open(p, "a", encoding="utf-8").write("\n" + marker + text)
            log.append((fname, "narrative", "dated section", "", "appended", "V12 recheck residual defect", SRC))
    if log:
        with open(os.path.join(HERE, "CORRECTIONS.tsv"), "a", encoding="utf-8") as fh:
            for r in log:
                fh.write("\t".join(str(c).replace("\t", " ").replace("\n", " ") for c in r) + "\n")
    print(f"{len(log)} change(s)")


if __name__ == "__main__":
    main()
