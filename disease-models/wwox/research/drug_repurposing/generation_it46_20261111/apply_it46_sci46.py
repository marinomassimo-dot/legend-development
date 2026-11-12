#!/usr/bin/env python3
"""IT46 P5: the SCI46 KEAP1/NRF2 delivery reaches its consumers (idempotent; marker "[IT46 SCI46]"). Rows 1, 2, 5, 6, 9, 10 of keap1_nrf2_sci46_20261111/consumer_delta.md.
V19 name and counter were edited in the table directly with the manifest row and the engine aliases; this script adds the INV-08 and V19 step texts and the open-question rows.
Not applied here (stated in p5_sci46_it46.md): row 7 (needs.json is an input digest of the ranking), rows 3, 4, 8, 11 (Harness). python3 apply_it46_sci46.py [--check]"""
import csv, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
MARK = "[IT46 SCI46]"
STEPS = (MARK + " Reagent pair named (SCI46): the non-covalent KEAP1 Kelch binder KI-696 against a covalent comparator, in one neural cell class at a time. X0: nuclear NRF2, two target genes (G6PD may be one), NQO1 enzyme activity and a risk panel (glutathione, GPX4, lipid peroxidation); the same lysates serve INV-07 step 1 and INV-19 (a shared preparation, not a shared cause). "
         "X1: a graded occupancy ladder matched on on-target response, not on concentration. X2: an adequacy criterion for NFE2L2 and KEAP1 loss fixed before the experiment, a KEAP1-loss occlusion arm, and a panel or array whose survivors after loss are read beyond NQO1. X3: neuron-only and astrocyte-only loss. Viability is read beside a function endpoint. "
         "Source: keap1_nrf2_sci46_20261111/experiment_ladder.tsv, outcome_matrix.tsv, hypotheses.tsv (NH1-NH4).")
UNC = (MARK + " Where an NRF2 loss was verified (primary rat microglia) the binder's effect was lost and KEAP1 loss occluded it; in a human neuronal line a partial loss left the effect unchanged (uninterpretable); one human neuronal use on an already NRF2-high background moved ferroptosis markers in the harmful direction; the source's own siRNA arms are categorical labels in the database copy. Nothing is measured in a WWOX-deficient neural system. Source: keap1_nrf2_sci46_20261111/README.md.")
V19N = (MARK + " Interpretable pair: each reagent with and without a verified NFE2L2 loss in the same neural cell, a KEAP1-loss occlusion arm, reagents matched on on-target response, a readout beyond NQO1 (survivors after loss) and viability beside function; the engine derives the binder as a primary-read probe with a comparison that is not yet interpretable (system strings not recognised).")
EDITS = [(DR / "ranking_it8_p9_20261029/investigations_it20.tsv", "inv_id", "INV-08", "next_test", STEPS), (DR / "ranking_it8_p9_20261029/investigations.tsv", "inv_id", "INV-08", "next_test", STEPS),
         (DR / "ranking_it8_p9_20261029/investigations_it20.tsv", "inv_id", "INV-08", "decisive_uncertainty", UNC), (DR / "ranking_it8_p9_20261029/investigations.tsv", "inv_id", "INV-08", "decisive_uncertainty", UNC),
         (DR / "generation_it41_20261109/compound_view.tsv", "item_id", "V19", "next_test", V19N),
         (DR / "batch_sci_20261105/map/open_questions_map.tsv", "qid", "IT45-Q03", "blocking_reason", " " + MARK + " Reagent pair named: binder KI-696; covalent comparators dimethyl fumarate and monomethyl fumarate, bardoxolone methyl conditional. The Davies arm exists only as categorical database labels; verified NRF2 dependence exists in primary microglia, not in neurons.")]
S = "keap1_nrf2_sci46_20261111/consumer_delta.md"
NEWQ = [("IT46-Q05", "Davies 2016 Supporting Information: the numbers behind the categorical NRF2-siRNA labels of the non-covalent binder and bardoxolone methyl (closed access; no contact is made). DATO gap.", "Decides whether the source's own knockdown arm can be read as numbers.", "data_access_blocked", "Closed access, no repository copy.", "no"),
        ("IT46-Q06", "Winkel 2015 full text and its knock-out verification for the second non-covalent binder (abstract reached only). Reading task.", "Decides whether a second binder meets the knockdown criterion.", "literature_executable", "Full text returned an error twice; not retried by another route.", "yes"),
        ("IT46-Q07", "What is an adequate NFE2L2 or KEAP1 loss in a neuron (residual protein, time, target-gene survivors), fixed before the experiment? A partial loss left an effect unchanged in one neuronal line.", "Decides whether a maintained effect under loss is read as independence.", "decision", "No criterion exists; one neuronal line gave a partial knockdown.", "yes"),
        ("IT46-Q08", "Does a risk panel (glutathione, GPX4, lipid peroxidation) beside NQO1 separate benefit from harm in a neural cell whose NRF2 response is already induced?", "Decides whether a raised NRF2 readout can be read as benefit.", "wet_lab_measurement", "One human neuronal datum in the harmful direction, no loss arm.", "no"),
        ("IT46-Q09", "Sulforaphane with a null arm in neural cells (no source with a null arm was reached).", "Decides whether the commonest covalent comparator can be read as NRF2-dependent in neurons.", "literature_executable", "Untested in SCI46.", "yes")]


def main(check=False):
    csv.field_size_limit(10**9); changed = 0
    for f in sorted({e[0] for e in EDITS}):
        rows = list(csv.reader(open(f, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]
        for ff, idc, idv, col, txt in EDITS:
            if ff != f:
                continue
            i, c = h.index(idc), h.index(col)
            for r in rows[1:]:
                if r[i] == idv and MARK not in r[c]:
                    r[c] = (r[c] + (txt if txt.startswith(" ") else " " + txt)).strip(); changed += 1
        if f.name == "open_questions_map.tsv":
            have = {r[0] for r in rows}
            for q, text, dec, kind, block, ex in NEWQ:
                if q not in have:
                    r = [""] * len(h)
                    for k, v in dict(qid=q, source_ref=S, question_text_max300=text, decision_at_stake_max200=dec, kind=kind, status="OPEN", status_evidence=S, last_touched="2026-11-12", blocking_reason=block, executable_zero_spend=ex).items():
                        r[h.index(k)] = v
                    rows.append(r); changed += 1
        if not check:
            csv.writer(open(f, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    print(("would change " if check else "changed ") + str(changed))


if __name__ == "__main__":
    main("--check" in sys.argv)
