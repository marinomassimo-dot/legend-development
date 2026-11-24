"""ADV-208 (IT, 2026-11-24): four dated wording lines on existing rows; old text kept; idempotent (one marker per line).
Item 1 INV-06 next_test (stage wording + carnosine constraint); item 2 INV-01 evidence_available (panel-specific P5 survival reading);
item 3 INV-01 next_test (bridge readout grid + restoration-only inference correction) and a WO-02 pointer; item 4 INV-08 next_test (zonisamide Fig 5C unit + comparator).
Item 5 (PAPER 542 label) is NOT applied: the label lives in two of the four scientific current files (BATCH_COMMIT only) and the depth queue is a generated file.
Run from the repository root. Hypothesis level; reference genotype class only; no ranking, drug, arm or priority change."""
import json
from pathlib import Path

DR = Path("disease-models/wwox/research/drug_repurposing")
R = DR / "ranking_it8_p9_20261029"
COORD = "laboratory coordination directory (not in git)"

L1 = (" [ADV-208 item 1, 2026-11-24, two wording constraints for any continuous-compound reading carried against this row; no ranking, drug or priority change. "
      "(a) Stage: the cholinergic-lipid transcript contrast in the held juvenile hippocampal nuclei table (continuous_compounds/citicoline/cell_types.tsv; one pooled library per condition, marker-assigned classes; Codex strategic review 20, arithmetic reproduced by ADV and by IT from the held table) "
      "is worded by identity and maturation stage, not as 'early versus late' or 'early precursors are spared'. Slc44a1 knockout-to-control log2 ratio of counts per million is +0.53 in precursor cells (OPC) and -0.73 in mature oligodendrocytes (MOL), but -0.15 for the grouped OPC, COP and NFOL classes and -0.35 for the grouped MFOL and MOL classes; "
      "Pcyt1b is +0.38 (OPC), -0.84 (MOL), +0.48 grouped early and -1.00 grouped late. The sparing reading does not survive grouping three earlier states, and MOL Flvcr1 rests on 8 against 16 gene counts. "
      "Agreement across three normalisations is descriptive robustness, not replication, cell-autonomous expression, enzyme activity or flux; no cross-age inference. If a functional test is ever run, uptake limitation and downstream conversion stay rivals (precursor and product in the same maturity-matched class, with absolute lipid and viable-axon denominators). "
      "The citicoline dossier note (continuous_compounds/citicoline/myelin.md) belongs to its dossier owner and is pointed to, not edited. "
      "(b) Carnosine: tissue exposure, protection during injury, survival of mature oligodendrocytes and recovery of conduction are four separate questions. Neither the 2023 paper (PMID 37774767; abstract plus author preprint) nor the 2024 genetic paper (PMID 39360557) supports a claim of carnosine-induced remyelination: the 2024 study has no exogenous carnosine arm, and in the 2023 preprint a rise of tissue carnosine under cuprizone came with no reported benefit on callosal myelin protein or oligodendrocyte counts. "
      "A decisive observation would be preserved or recovered propagation after a verified rise of intact carnosine in the same WWOX tract and developmental window, read against surviving axons and mature oligodendrocytes, with homocarnosine measured separately; new-sheath claims need a stage-matched recovery contrast with coverage per eligible axon. "
      "The figure-level carnosine numbers are Codex's readings of the originals and were not verified by ADV or IT. "
      "Review-level compressions such as 'improved growth and myelination' are not imported over the held quantified readings of this row. "
      "Sources: Codex strategic reviews 20 and 23 (" + COORD + "); continuous_compounds/citicoline/cell_types.tsv; continuous_compounds/l_carnosine/README.md]")

L2 = (" [ADV-208 item 2, 2026-11-24, wording only; no ranking change; no post-onset datum: the timing panels of the neonatal gene-addition primary's supplement (Fig S8, PMID 42422765) are read panel by panel. "
      "The P5 arm carries the same label and nominal n = 7 in both survival panels: S8A (about 40 days) stays near 100 percent and S8B (300-day plot) steps to about 75 percent at about day 35 and stays there. "
      "Two independent figure readings agree on both panels (the deep-dive manifest, locator entry 10, re-inspected at 400 dpi; the Codex follow-up of 2026-11-24). Keep the two panel readings separate: do not stitch them into one P5 trajectory and do not turn the step into a count of deaths, "
      "because no animal identifiers or event and censor table say whether the two panels describe the same analysis set. P4 appears only as weight and glucose bars, with no P4 survival curve. "
      "The S8 question reopens only on cohort provenance or a time-to-event and censor table. Older notes saying that both P1 and P5 plateau near 75 percent, or that P4 is absent from all of S8, are superseded by the manifest. "
      "The working-model entry TX-007 carries no P5 curve wording (checked) and is not edited here. ADV did not re-read the figure. "
      "Sources: the held deep-dive manifest for PMID 42422765; Codex follow-up note on the DEE review (" + COORD + ")]")

L3 = (" [ADV-208 item 3, 2026-11-24, readout grid and one inference correction for the bridge comparison; wording only; no arm, ranking or priority change. "
      "Grid (consumed 2026-11-23 from the joint review of the 2026 DEE review): separate (i) acute suppression, (ii) function that persists after the acute drug action, and (iii) maturational outcomes; read an evoked response only where baseline state and activity are comparable; where raw or paired data are missing, mark the contrast unidentifiable rather than infer it. "
      "Inference correction (Codex reply 36): a post-onset arm with restoration alone estimates what restoration alone recovers at that stage. It cannot by itself identify an added benefit of a bridge, whether a bridge only needs to precede restoration, or an interaction. "
      "A claim that a bridge adds value needs its own time-matched comparison against restoration alone, with acute event suppression separated from persistent function, and a drug-only arm where available to separate independent benefit from interaction. "
      "The review adds no WWOX datum for any of this: its bridge sentence repeats the primary's own hypothesis. "
      "Sources: meeting acknowledgement of the DEE synthesis, the Codex follow-up note on the DEE review and Codex reply 36 (" + COORD + ")]")

W2 = (" [IT 2026-11-24 ADV-208 items 2 and 3, pointer only: the panel-specific P5 survival reading, the readout grid and the restoration-only inference correction are carried in INV-01 evidence_available and next_test; no arm or priority change.]")

L4 = (" [ADV-208 item 4, 2026-11-24, wording only; no ranking, compound or arm change. Placement: the glutathione and redox readouts are in this row; INV-07 is the PDH axis and carries no zonisamide or glutathione text. "
      "(a) The zonisamide neuronal glutathione staining result (rat cervical compression model, PMID 32753675, Fig 5C, ChAT-positive motor neurons; Mann-Whitney, three rats per group; both anterior horns counted independently by two blinded observers; no per-rat table, aggregation rule or sidedness stated) has an unresolved analysis unit. "
      "With three independent rat-level values per group the smallest exact two-sided p is 0.10 (20 allocations); a no-tie normal approximation gives 0.04953 without and 0.08086 with continuity correction. The star is not an animal-level inference until the unit is shown (arithmetic recomputed by Codex, by ADV and by IT). "
      "(b) Comparator for the next ordinary comparison of the zonisamide and acetylcysteine redox dossiers (Codex strategic review 22): contrast a glial supply effect, a neuronal bypass of a cysteine-uptake limit and a direct neuronal drug effect, at matched baseline activity and culture composition; require neuron-specific precursor incorporation plus function; keep glutamate clearance as a counter-outcome; "
      "if the effects do not separate, keep both as mechanistic probes. Held pointers: continuous_compounds/zonisamide/motor_neurons.md (exact enumeration only; the asymptotic values and the comparator are not yet in that note, left to its owner) and continuous_compounds/acetylcysteine. "
      "Sources: Codex strategic review 22 and the ADV acknowledgement of 2026-11-24 (" + COORD + ")]")

EDITS = [("INV-06", "next_test", "ADV-208 item 1", L1), ("INV-01", "evidence_available", "ADV-208 item 2", L2),
         ("INV-01", "next_test", "ADV-208 item 3", L3), ("INV-08", "next_test", "ADV-208 item 4", L4)]


def edit_tsv(p):
    L = p.read_text(encoding="utf-8").split("\n"); h = L[0].split("\t"); n = 0
    for i, l in enumerate(L):
        f = l.split("\t")
        if i and len(f) == len(h):
            for inv, col, mark, line in EDITS:
                c = h.index(col)
                if f[h.index("inv_id")] == inv and mark not in f[c]:
                    f[c] += line; n += 1
            L[i] = "\t".join(f)
    p.write_text("\n".join(L), encoding="utf-8"); return n


def edit_json(p):
    raw = p.read_text(encoding="utf-8"); d = json.loads(raw); n = 0
    for x in [y for k in ("investigations", "further_investigations", "conditional_hypotheses") for y in d.get(k, [])]:
        for inv, col, mark, line in EDITS:
            if x["inv_id"] == inv and mark not in x[col]:
                old = json.dumps(x[col], ensure_ascii=False)[1:-1]
                assert raw.count(old) == 1, (inv, col, raw.count(old))
                raw = raw.replace(old, old + json.dumps(line, ensure_ascii=False)[1:-1]); n += 1
    json.loads(raw)
    p.write_text(raw, encoding="utf-8"); return n


def edit_map(p):
    L = p.read_text(encoding="utf-8").split("\n"); h = L[0].split("\t"); n = 0
    for i, l in enumerate(L):
        f = l.split("\t")
        if i and len(f) == len(h) and f[0] == "WO-02" and "ADV-208" not in f[h.index("status_evidence")]:
            f[h.index("status_evidence")] += W2
            f[h.index("last_touched")] = max(f[h.index("last_touched")], "2026-11-24")
            L[i] = "\t".join(f); n += 1
    p.write_text("\n".join(L), encoding="utf-8"); return n


print("investigations_it20.tsv", edit_tsv(R / "investigations_it20.tsv"))
print("investigations.tsv", edit_tsv(R / "investigations.tsv"))
print("ranking.json", edit_json(R / "ranking.json"))
print("open_questions_map WO-02", edit_map(DR / "batch_sci_20261105/map/open_questions_map.tsv"))
