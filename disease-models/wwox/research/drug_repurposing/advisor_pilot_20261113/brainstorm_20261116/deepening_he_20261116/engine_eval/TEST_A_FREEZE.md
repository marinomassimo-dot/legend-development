# Test (a), frozen before any run: time-sliced retrodiction on the repository at a dated cut (HE; 2026-11-16; non-canonical; not medical advice)

Written for: ADV and the 23:15Z meeting (decision: go / no-go for test (a), and whether the target below is acceptable). Nothing has been run. Costs and design: `ENGINE_EVAL_DESIGN.md`.

## 1 · The cut
Commit `1867a26a8` (2026-09-20 12:50:57 +0000), the parent of the commit that registered Steinberg 2026 (`e396f698c`). The repository's history starts with one public-edition commit on 2026-07-26, so cuts earlier than that cannot be reproduced; the engine at the cut = the checkout of this commit, read by a delegate with no other file and no memory index (delegates inherit the memory index otherwise: run it with the memory-free setup IT used for the baseline arm).

## 2 · Contamination check of the candidate targets (the check is part of the freeze; Sibyl's checklist applied to our own corpus)
`git grep` at the cut, inside `disease-models/`, files naming the target:
| candidate target | files naming it at the cut | verdict |
|---|---|---|
| Steinberg 2026, WWOX-MYC organoids (PMID 42397075; PubMed date 2026-07-03) | 30 files by PMID, 42 by author name (analysis files, reviews, pathograph export) although the registry record was created at e396f698c | **REJECTED: already held and used** |
| Lucas-Clarke 2026, Wwox in Drosophila Aβ models (PMID 42909904; published 2026-10-09, after the cut; first named in the repository 2026-10-26) | PMID: 0 files. Author name: 8 files (the 2025 preprint of the same group, reached through the Obeid 2026 review, held as a nuance: "WWOX metabolic effect HIF1α-independent (via ATF4/UPR; neuroprotection via methionine suppression, not lactate)") | **PARTLY CONTAMINATED: atom 2 below was already held; atom 3 is held as the opposite** |
| Hammouz 2026 (42589397), Tang 2026 (42738875: not WWOX) | PMID: 0 | clean but not a mechanism a generator could derive (oncology breast subtypes; an HIV biomarker paper) |

## 3 · The target and its atoms (read from the PubMed abstract of 2026-11-16, [DOI 10.1093/braincomms/fcag385](https://doi.org/10.1093/braincomms/fcag385); the full text is not read for this freeze)
Atom 1 (direction): neuronal loss of Wwox worsens, and overexpression reduces, amyloid-beta toxicity in the fly. Atom 2 (route): stress-responsive ATF4 activation. Atom 3 (effector): raised lactate dehydrogenase expression and lactate, with genetic reduction of the dehydrogenase rescuing locomotion (pyruvate metabolism as the mediator). **Credit rule:** atom 2 is NOT credited (held at the cut); atom 1 is credited only if stated as a prediction with its direction before the unit of toxicity; atom 3 is the only atom that discriminates, because the held nuance says "not lactate". A hypothesis that names only the gene or only "metabolism" scores 0.

## 4 · Procedure and rubric (fixed now)
Delegate A (engine condition): the checkout at the cut, question "propose 10 mechanisms by which loss of WWOX in neurons could worsen amyloid pathology", the leap-round hypothesis template. Delegate B (baseline condition): same question, no repository files, the leap round's memory-free bundle. Scorer: me, one pass, atoms against the abstract, no LLM judge as gate; a second reader (a different delegate, one active at a time) checks only the atom-3 decision. Output: atoms credited per condition, hypotheses that named lactate or pyruvate, hypotheses that contradicted the held nuance.

## 5 · Predictions committed before any run
Engine reaches atom 1 (yes, trivially) and atom 3 in at most 1 of its 10 hypotheses; the baseline reaches atom 1 and atom 3 in at most 1 of 10. If the engine's atom-3 count is higher than the baseline's by 2 or more, the held corpus helped; if both are 0, the engine did not generate the revision from the held nuance, and the ~340k-token cost bought a negative result. Reported either way; no card, row or ranking changes.

## 6 · Limits
Abstract-only atoms; one target; the 2025 preprint contamination of atom 2 is partial and disclosed; a PubMed publication date is not the date the engine's underlying model could have seen a preprint; a single run per condition is anecdote, not a rate.
