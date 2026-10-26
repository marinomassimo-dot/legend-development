# P3A: what does local WWOX knowledge contribute? A small first trial (2026-10-26/27)

Scientist `scientist-a`. Non-canonical, exploratory, research-work quality only: no therapeutic-efficacy gold set was
invented, nothing here is medical advice, no dose, no wet-lab claim. Task `P3A`; drug_repurposing roadmap step P7 is
still "not started" as a gold-set evaluation; this is a work-quality probe, not that step.

## Design
- Five cases already qualified in the repository: C1 ISR modulators (E01), C2 LDH/stiripentol (E02), C3 DCA/PDK (E03),
  C4 ketogenic diet / lactate (E04, a card-level abstention), C5 lithium/GSK3beta (with isoform-risk counter-evidence in the literature). Support, counter-evidence and abstention are all present.
- Same three questions per case ([`questions.md`](questions.md)): target/direction/endpoint/context; counter-evidence and transfer risks; next measure or abstention.
- Three conditions run as tool-access conditions in three fresh-context subagents, each told its allowed inputs:
  A external only (Open Targets, ChEMBL, DGIdb, PubTator 3 via the adapters, PubMed), B local only (cards, ledgers, mechanism map via `registry_records.py` / `repurposing_join.py`, no network), C both. Answers: [`answer_a.md`](answer_a.md), [`answer_b.md`](answer_b.md), [`answer_c.md`](answer_c.md).
- Reference fixed first ([`reference.md`](reference.md), SHA-256 and UTC time in [`pre_answer_hashes.txt`](pre_answer_hashes.txt): 22:35:34Z, answers files 22:37-22:39Z). Built from PMC full text of PMID 42909904 and PMID 32000863 and PubMed abstracts of seven other papers; no card conclusion was read to write it. Scoring: [`scoring.md`](scoring.md) (binary rubric items).
- Transcript check: A's tool calls contain no repository-content read; B made no network or adapter query. Agent-reported counts are in `scoring.md`.

## Contamination (declared)
1. The producer (this actor) had no memory of earlier work but is the same actor identity that wrote parts of the Lucas-Clarke follow-up; the task text itself told it that E01-E04 exist and that E04 is an abstention.
2. Before writing the reference the producer read the first 40 lines of `lucas_clarke_followup_20261026/README.md` to identify the paper. That page states the PDK1/PDPK1 collision, the empty DGIdb/Open Targets rows for eIF2B activators and "no Wnt/GSK3 premise"; rubric item 3.5 and the ISRIB items were written after seeing it. The remaining reference content comes from the primary sources.
3. The reference rubric overlaps with what the local cards encode because both rest on the same full text (PMID 42909904); this favours conditions B and C on the fly-paper items.
4. The subagents are the same model family as the producer; A, B and C could not be made blind to general model knowledge (e.g. ISRIB, DCA neuropathy). Condition A is "external-tool only" for retrieval, not for prior knowledge.
5. Producer scored; no independent scorer yet.

## Results (case items max 26, total max 30)
| | A external | B local | C both |
|---|---|---|---|
| Case items | 18.5 | 22.0 | 22.5 |
| Total with cross-cutting | 22.5 | 26.0 | 26.5 |
| Transfer errors (fly/mouse presented as WOREE efficacy) | 0 | 0 | 0 |
| Recall of counter-evidence | lowest (generic) | high for local negatives and compound potency | high; plus live identifier traps |
| Abstentions | present, correct | present, with reopening conditions | present, with reopening conditions |
| Tool calls / tokens / time | 19 / 81k / 113 s | 18 / 145k / 162 s | 21 / 138k / 219 s |

Where each condition lost: A missed the Abeta-dependence detail, the PDK1/PDPK1 collision and the stiripentol potency limit, and its counter-evidence stayed generic. B and C lost the same items (nobody retrieved the GSK-3 loss-of-function seizure papers 30237424 and 35253420, the lactate-may-be-adaptive point, or the GCN2/ISRIB-toxicity sources). B did not cite the WOREE ketogenic case series (36537114). C added the live checks (identifiers, KD series, a DCA safety paper) at the cost of a longer run and flagged three local-versus-external disagreements without resolving them.

## What this can and cannot support
- Can: on these five cases, local knowledge added context fidelity, negatives and abstention reasons that external tools alone did not return, and external tools added identifier and compound checks and one primary clinical series that local alone did not carry. The reading is "complementary", with local the larger single contribution on this rubric (+3.5 case points of 26 for B over A).
- Cannot: general superiority, efficacy, or ranking of candidates. n = 5 cases, one run per condition, one producer-scorer, a rubric built partly from the same paper the cards encode, same-model subagents, abstract-depth for seven of nine reference sources. Differences of a point or two are inside this noise; the C-over-B gap (0.5) is not a finding.

## Decisive judgements for the independent verifier (must not be the producer)
1. Reference items resting on abstracts only: 1.4 (GC 24146979, SI 23741617), 2.2 (SA 25792327), 3.3 (DC 16476929), 4.1 (WO 36537114), 5.3 (G1 30237424, G2 35253420). Re-check the wording against full text where available.
2. Lithium: does Fig. 7d of PMID 32000863 (PMC6990504) show lithium suppressing PTZ seizures in wild-type mice as B and C reported from the local ledger? The text read states Wwox-/- only. This decides whether B/C's "specificity failed" is a correct local correction or an over-reading, and whether item 5.2 should be stricter.
3. Scoring of 1.4, 2.1, 2.3, 3.3, 5.4 (the half-credit items) and the four items nobody met (3.4, 5.3 and parts of 1.4/5.4): are they fair?
4. Whether the 4.1 half credit for B is right: it cited a different cohort observation (3 tried, 1 continued) that may conflict with 36537114 "responded in three"; the two should be compared in the full texts.
5. Independence of the contamination account (item 2 above) and whether rubric item 3.5 should be dropped as contaminated (dropping it moves A to 22.5 vs B 25.0 vs C 25.5 of 29).
6. Stiripentol potency claim (B): Bacq 2024 (38443647) and the stiripentol complex I paper (41570991) say what B reports.

Not repeated: this trial changed no card, registry or ledger. Records: line added to [`../README.md`](../README.md).
