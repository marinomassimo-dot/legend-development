#!/usr/bin/env python3
"""Apply the V13 recheck residual corrections (SCI50) cell by cell; idempotent.

Run from this folder: python3 apply_v13_recheck.py. Changes are appended to CORRECTIONS.tsv;
narrative files get a banner and a dated section guarded by a marker.
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = "verify/verdicts.tsv item R / audit.md section 8"


def read(fname):
    with open(os.path.join(HERE, fname), encoding="utf-8") as fh:
        return fh.read().split("\n")


def write(fname, lines):
    with open(os.path.join(HERE, fname), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def set_cell(fname, key_col, key, field, fn, log, reason):
    lines = read(fname)
    head = lines[0].split("\t")
    kc, fc = head.index(key_col), head.index(field)
    for i, line in enumerate(lines[1:], 1):
        cells = line.split("\t")
        if len(cells) == len(head) and cells[kc] == key:
            new = fn(cells[fc])
            if new == cells[fc]:
                return
            log.append((fname, key, field, cells[fc][:300], new[:300], reason, SRC))
            cells[fc] = new
            lines[i] = "\t".join(cells)
            write(fname, lines)
            return
    sys.exit(f"{fname}: {key} not found")


def add_row(fname, key_col, row, log, reason):
    lines = read(fname)
    head = lines[0].split("\t")
    if any(l.split("\t")[0] == row[0] for l in lines[1:]):
        return
    assert len(row) == len(head), (fname, len(row), len(head))
    if lines and lines[-1] == "":
        lines = lines[:-1]
    lines.append("\t".join(row))
    write(fname, lines)
    log.append((fname, row[0], "row added", "", row[1][:200], reason, SRC))


def append_narr(fname, marker, text, log, banner=None):
    p = os.path.join(HERE, fname)
    body = open(p, encoding="utf-8").read()
    if marker in body:
        return
    if banner and not body.startswith("> **READ THE REVISED SECTIONS"):
        body = banner + "\n\n" + body
    body = body.rstrip("\n") + "\n\n" + marker + text
    open(p, "w", encoding="utf-8").write(body)
    log.append((fname, "narrative", "dated section", "", "appended", "V13 recheck residual", SRC))


BANNER = ("> **READ THE REVISED SECTIONS AT THE FOOT FIRST.** The text from the top is the generation-phase text, kept for history; "
          "the sections dated after V13 supersede it, and the last one (V13 recheck, final form) is the handover form.")


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        return
    log = []
    set_cell("levers.tsv", "lever_id", "L1-R2", "compound_or_probe_identity",
             lambda v: v.replace("held ledger rows, plus V13-read abstract of a brain-penetrant EBP inhibitor PMID 38470227)",
                                 "the identity and M1 affinity of the EBP inhibitor rest on held ledger rows and an abstract (PMID 38470227), re-verified from no primary paper by either reader; PIPE-307's own EBP activity is untested; the PIPE-307 assay is a primary rat cortical myelination assay (MBP/Tuj1), its neuron-OPC composition an inference)"),
             log, "identity wording and PIPE-307 assay composition (V13 recheck item 1)")
    set_cell("levers.tsv", "lever_id", "L1-R2", "control_that_separates_mechanism",
             lambda v: v if "assay-window gate" in v else v + "; PIPE-307 sterol profile and an assay-window gate (the drug must act on its own before an interaction is read); submaximal doses in a dose matrix (Hubler's non-additivity was at a maximal ketoconazole dose, n >= 3 wells) with a T3 headroom control; contrasts in Chrm1-null or EBP-null cells are read only when positive (the null baselines occlude); rat versus mouse OPC stated",
             log, "residual confounds of the additivity contrast (V13 recheck item 3)")
    set_cell("levers.tsv", "lever_id", "L3-NEW", "control_that_separates_mechanism",
             lambda v: v if "fresh-medium baseline" in v else v + "; positive control: recombinant CTGF and HEK-derived CTGF medium (Ercan reports both reduce MBP+ cells) in addition to Tsc2-knockdown neuron medium; fresh-medium baseline, a mixing arm (null medium with wild-type medium), neuron purity checked, a dilution series, the T3/B27 caveat",
             log, "missing controls for the conditioned-medium arm (V13 recheck item 3)")
    set_cell("levers.tsv", "lever_id", "L3-NEW", "known_in_neuron_driven_model",
             lambda v: v.replace("CTGF from neurons blocks OPC maturation in vitro", "the authors report that neuron-secreted CTGF is necessary and sufficient to block OPC maturation in vitro (the authors' claim, read at targeted depth; Methods and n unread)"),
             log, "CTGF conclusion is the authors' claim (V13 recheck item 2)")
    set_cell("evidence.tsv", "ev_id", "V25", "species_system",
             lambda v: "primary rat cortical myelination assay (MBP/Tuj1 segment-length index); its neuron-OPC composition is an inference, not stated in the text read",
             log, "assay composition (V13 recheck item 2)")
    set_cell("evidence.tsv", "ev_id", "V26", "note",
             lambda v: v if "authors' in vitro claim" in v else v + "; the CTGF 'necessary and sufficient' statement is the authors' in vitro claim (Methods and n unread); a Tsc model with no Wwox datum",
             log, "hedge (V13 recheck item 2)")
    add_row("open_questions.tsv", "oq_id", ["OQ4", "Does a lipid supply (cholesterol carrier, fatty acids) enter myelin membrane in the dish and change internode number in the null-neuron co-culture", "whether the lipid-supply note (L2-NOTE) deserves an arm", "wet_lab_measurement", "3", "internode scoring with a lipid carrier arm beside the vehicle; membrane incorporation read", "L2-NOTE", "a verified dish reagent exists"], log, "restored: the verifier's finding supports the question")
    add_row("open_questions.tsv", "oq_id", ["OQ7", "Does the Wwox-null co-culture deficit carry axon density or calibre differences that explain fewer myelinating-class cells", "whether a lower myelinating share is an OPC maturation effect or an axon-denominator effect (H1 alternative ii)", "wet_lab_measurement", "2", "axon density and calibre denominators per field in each genotype, blind scoring", "H1; minimum comparison denominators", "a co-culture arm is run"], log, "restored: axon density or calibre is H1's alternative (ii)")
    add_row("open_questions.tsv", "oq_id", ["OQ11", "Does the null-neuron medium effect survive neuron purification, mixing with wild-type medium and a fresh-medium baseline", "whether a soluble inhibitor is the explanation for the neuron-side limit (H4) rather than medium depletion or a non-neuronal DRG cell", "wet_lab_measurement", "3", "monoculture OPC maturation with purified-neuron medium, mixing arm, fresh-medium baseline, dilution series", "H4; INV-06 X1 (b)(c)", "INV-06 X1 is run"], log, "added from the verifier's recheck (row A)")
    add_row("open_questions.tsv", "oq_id", ["OQ12", "Is the null-neuron deficit reproduced blind, with independent preparations and axon-density denominators, and does it occur with cortical neurons", "whether the premise of every arm (a null-specific deficit) holds outside two experiments with n = 4 v 4 in a peripheral DRG co-culture", "wet_lab_measurement", "3", "blind scoring, independent preparations, cortical neurons beside DRG", "gate-0 of H1 and H4", "a co-culture is available"], log, "added from the verifier's recheck (row B)")
    append_narr("hypotheses.md", "<!-- v13-recheck -->", """
## Final form after the V13 recheck (Orchestrator, 2026-11-13; the sections above are history)
**H4 (the soluble-inhibitor hypothesis) is not a new combination for LEGEND.** The conditioned-medium test is already INV-06 X1 arms (b) and (c) (recorded in it36 ALT2); what is new is a **candidate mechanism from neuron-specific Tsc models** (CTGF, an authors' in vitro claim, no Wwox datum) and the **controls the old arm lacked**. Final form, conditional: *Wwox-null neurons release a factor that lowers OPC maturation (IPOTESI; no row links Wwox to CTGF or any secreted product).* Controls required for it to discriminate: a fresh-medium baseline and a mixing arm (a missing soluble cue versus an inhibitor), neuron purity (non-neuronal DRG cells carry the null genotype too), a dilution series, the B27/T3 caveat (medium depletion including T3), a positive control (recombinant CTGF or Tsc2-knockdown neuron medium), and a detection limit from the monoculture's own variance (not the 20-point threshold borrowed from the co-culture). Novelty: (a) modest, a refinement of INV-06 X1; (b) not asserted; (c) unvalidated. Decision changed: whether INV-06's 'soluble product' item can be closed before any compound is ordered. **H1 (the neuron ceiling)** stays conditional and is handed on only after gate 0: T3/T4 measured in the medium, the deficit reproduced blind, the OPC window checked with PIPE-307 tone and sterol engagement, and a clean rewrite of its block (reverse pairing first, a monoculture ceiling by dose-response, submaximal doses). **H2 and H3 are dropped** (H3 contradicted by the neonatal clemastine re-read; H2 has no neuron-side datum and the Camargo double mutant failed).
""", log, BANNER)
    append_narr("minimum_comparison.md", "<!-- v13-recheck -->", """
## Note after the V13 recheck (2026-11-13)
The final minimum comparison is in `../README.md` (one page). This file keeps the earlier text for history; it exceeds the page limit and lists arms that the recheck judged not indispensable (the clemastine comparator, neutralisation of a candidate that does not exist, M1/acetylcholine tone as a gate rather than an arm, the overlap of the T3 co-arm with the T3/T4 step, a second cortical preparation in block 1).
""", log, BANNER)
    append_narr("levers_notes.md", "<!-- v13-recheck -->", """
## Note after the V13 recheck (2026-11-13)
L1-R2 is an interpretable additivity contrast only conditionally: ligand tone (PIPE-307 alone must act first), saturation (submaximal doses, a dose matrix, a T3 headroom control), PIPE-307's EBP activity untested, the EBP inhibitor's M1 affinity resting on a CHO functional assay, rat versus mouse OPC; contrasts in Chrm1-null or EBP-null cells read only when positive. L3-NEW rests on an authors' in vitro claim from Tsc models; no Wwox-CTGF link exists. J4 is a global Tsc2 heterozygous model (mixed context), not a neuron-driven model.
""", log, BANNER)
    append_narr("answers.md", "<!-- v13-recheck -->", """
## Sentences accepted after the V13 recheck (2026-11-13)
(a) Compounds have been tested in neuron-specific Tsc1 knockout models (rapamycin and RAD001: myelination markers improved, no conduction readout) and, in a global Tsc2 heterozygous mixed-context model, at ultrastructural level (J4: EM g-ratio relationship; J4 is **not** a neuron-driven model). Within the strings run (Europe PMC title and abstract, 2026-11-13), no OPC-intrinsic enhancer was found assessed at sheath structure and conduction together in an isolated neuron-driven model. (b) The M1 and EBP readings of clemastine and benztropine disagree in the sources read: Chrm1-null abolishes the drug effect in primary OPCs that already differentiate about five-fold more, while antimuscarinics that block M1 in CHO reporter cells were inert in EpiSC-derived OPCs unless they inhibited EBP; no source opened tests both on one OPC preparation; the M1-selective PIPE-307 acts in primary OPCs but its EBP activity is untested; the premise is real and unresolved; ligand tone and preparation differences are untested explanations. (c) In neuron-specific Tsc models the authors report that neuron-secreted CTGF is necessary and sufficient to block OPC maturation in vitro and that neuronal CTGF loss restores the share of myelinated axons but not myelin thickness: an authors' claim at targeted depth, in a Tsc model with no Wwox datum; a neuron-derived inhibitory signal for Wwox-null neurons is a hypothesis, and the conditioned-medium test is already INV-06 X1.
""", log, BANNER)
    if log:
        with open(os.path.join(HERE, "CORRECTIONS.tsv"), "a", encoding="utf-8") as fh:
            for r in log:
                fh.write("\t".join(str(c).replace("\t", " ").replace("\n", " ") for c in r) + "\n")
    print(f"{len(log)} change(s)")


if __name__ == "__main__":
    main()
