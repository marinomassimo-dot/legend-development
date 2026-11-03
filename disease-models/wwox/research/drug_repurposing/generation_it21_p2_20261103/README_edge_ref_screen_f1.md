# IT21 F1 - edge-reference sign screen

Non-canonical research material. Actor `orchestrator-delegate` (package F1), branch `task/it21-f1`. **Not medical advice.** Reference genotype class only; no individual-level record; zero spend; no contact string sent to any service (OmniPath, NCBI E-utilities at about 2 requests per second); no scientific current file, registry or ledger edited.

## Decision

1. **The screen is built and usable as a prompt, not as a verdict.** Edge -> the PMIDs the network record itself cites -> PubMed abstract -> sentence-level direction of effect -> `SUPPORTS | OPPOSES | SPLIT | NO_ABSTRACT_EVIDENCE` with the quoted sentences (`edge_ref_sign_screen_it21.py`). **Depth: abstract keyword/sentence heuristic. An abstract is not a read; nothing here is a full-text reading.**
2. **Validation on the six P4a proposals (8 edges with a manual verdict): the screen is recall-oriented and imprecise.** Flagged (OPPOSES/SPLIT) edges: 4; correct flags 2 (EZH2->IL6, SIRT1->MYC); false flags 2 (STAT3->NPY, BCL3->TNF); true misses 1 (KDM4C->HIF1A: its only reference is a review with no measured sign, so the screen says `NO_ABSTRACT_EVIDENCE`; the separate `basis_flag` column does catch it). Precision 2/4 = 0.50, recall 2/3 = 0.67 on this tiny set. EZH2->TNF (manual: contested) is not in any handed-over path and was not scored. **The heuristic was revised three times while looking at this set (alias loss words, cue multiplication, clause scoping), so these figures are not held out and are optimistic.**
3. **The 7 remaining proposals: no chain is OPPOSED; one keeps a standing "contested" note; none is closed; nothing is qualified.** `edge sign contested by its own references` stands for **IT21P2-0388 (CEP-11981)** only. Status stays `CONDITIONAL_*` for all seven; `CLOSED_AS_WRITTEN` was not used (it needs an opposed chain and no alternative arm, and every one of the seven has alternatives).

## The 7 proposals

| Proposal | Compound | Edge labels (screen) | Hand check of the quoted opposing sentences | Outcome |
|---|---|---|---|---|
| 0014 | ASTX-660 | XIAP->HIF1A SUPPORTS; HIF1A->HK2 SPLIT (34 v 8 sentences over 91 abstracts) | all 6 quoted opposing sentences actually support the edge (inhibiting HIF-1 lowers HK2) | CONDITIONAL_H_HARM, no contest standing |
| 0221 | SAR-407899 | ROCK2->EP300 NO_ABSTRACT_EVIDENCE; EP300->TNF SPLIT (5 v 2) | both opposing sentences support (p300 knockdown or blocked recruitment lowers TNF) | CONDITIONAL_H_HARM, no contest standing; first edge unscreened |
| 0236 | LGH-447 | PIM2->NFATC1 NO_ABSTRACT_EVIDENCE; NFATC1->IL6 SPLIT (4 v 1) | the one opposing sentence supports | CONDITIONAL_H_HARM, no contest standing; first edge unscreened |
| 0296 | ravoxertinib | MAPK3-|BRD4 SUPPORTS; BRD4->TNF SUPPORTS | n/a | CONDITIONAL_H_PROTECT; chain CLEAR at abstract depth only (2 sentences per edge at most) |
| 0388 | CEP-11981 | MAP3K7-|NFKBIB NO_ABSTRACT_EVIDENCE; NFKBIB->IL1B SPLIT (1 v 6) | genuine: IkappaBbeta overexpression/replacement attenuates IL1B and IL6 (PMIDs 21646597, 25908863), i.e. it acts as an NF-kB inhibitor there, opposite to the network's `+` | CONDITIONAL_H_PROTECT, **note: edge sign contested by its own references**; no alternative arm removed |
| 0456 | AZ960 | JAK2->MYC NO_ABSTRACT_EVIDENCE (1 reference) | n/a | CONDITIONAL_H_HARM, sign unverified |
| 0542 | lonaprisan | PGR->MYC NO_ABSTRACT_EVIDENCE (16 abstracts, no sentence naming both with a direction) | n/a | CONDITIONAL_H_HARM, sign unverified |

The hand check covers only the sentences the screen quoted, at abstract depth, by the F1 actor; it is recorded in `HAND_CHECK` in the script and in the `hand_check_of_opposing_sentences` column. The machine label stays in the table unedited, so a reader sees both.

## Limits (read before using a label)

* Sentence-level, abstract-only: a sign stated only in the full text, in a figure or in a supplement is invisible; context (cell type, species, transcript v protein, drug v genetic perturbation) is not read. A SPLIT on an edge with many references (HIF1A->HK2: 91) is expected noise; the counts are in the table, not a ranking of truth.
* Failure modes seen: inhibitor/miR wording read with the wrong subject, `activation`/`inhibition` nouns, two genes in one clause, regulator and target in different clauses (`NO_ABSTRACT_EVIDENCE` then). Phosphorylation (P) edges usually cite one reference and often return `NO_ABSTRACT_EVIDENCE`.
* `NO_ABSTRACT_EVIDENCE` is not "no contradiction": it is "the screen saw none". Four of the 11 new edges and two of the 8 validation edges returned it.
* A `CLEAR` chain (0296) means two abstract sentences per edge agree, nothing more; it does not qualify anything.
* References come from the OmniPath record as served (P4a's copy for the 11 edges it already held, a fresh query for the other 11); the cache of abstracts is third-party text, stays outside git (SHA-256 prefix of each abstract is in the quote tables).

## Files

| File | Content |
|---|---|
| `edge_ref_sign_screen_it21.py` | `fetch` (network, cache outside git) / `screen` / `validate` (offline) |
| `test_edge_ref_sign_screen_it21.py` | 16 offline tests: sentence rules, labels, parsing, table vocabulary, no status upgrade, the miss is kept |
| `results/edge_ref_screen/edge_screen_remaining7.tsv`, `edge_screen_quotes_remaining7.tsv` | the 12 edges of the seven, labels and quoted sentences |
| `results/edge_ref_screen/dispositions_remaining7.tsv` | chain label, hand check, status before/after, note |
| `results/edge_ref_screen/validation_p4a_edges.tsv`, `edge_screen_p4a6.tsv`, `edge_screen_quotes_p4a6.tsv` | the validation against the manual P4a verdicts |

Re-run: `python3 edge_ref_sign_screen_it21.py fetch --cache <dir>`, then `screen` and `validate` with `--out results/edge_ref_screen`.
