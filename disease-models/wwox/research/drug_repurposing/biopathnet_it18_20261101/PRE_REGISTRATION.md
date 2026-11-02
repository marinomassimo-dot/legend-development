# IT18 P-BIOPATHNET pre-registration: do BioPathNet's typed paths give WWOX relations with explanations that can be checked against sources?

Written 2026-11-01 by `scientist`, **before any BioPathNet code was installed or run and before any prediction or explanation path was computed**. At writing time only the following had been looked at: the repository at `b051a9003a13` (README, requirements, configs, `data/mock/README.md`, `script/visualize.py` head, the extension loader), the LFS pointers, the checkpoint training log, the six `PC_KEGG_0602` files (relation counts; the WWOX rows of the BRG; the absence of WWOX from G1), Pathway Commons 12 `datasources.txt`, the needs file's target and pathway fields, and the paper (Europe PMC XML). Non-canonical research material; not medical advice; computational link prediction only. Public edition, WWOX-DEE genotype class.

## Why this question and not the drug question
No drug-repurposing checkpoint is released (see `availability_terms.tsv`). Training BioPathNet on PrimeKG means a 5.7-million-edge message-passing graph trained on GPU by the authors; on this 4-core, 15 GB CPU machine shared with another job that is a second full stack, which the brief excludes. The **only distinct capability** that can be tested proportionately is the one the brief names: relation-typed, partly directional paths whose steps can be checked. The released gene-function checkpoint (Pathway Commons BRG with 13 typed relations, several directed: `controls-state-change-of`, `controls-phosphorylation-of`, `controls-expression-of`, `controls-transport-of`, `catalysis-precedes`...) is where that capability exists. WWOX is in the BRG (640 rows) and has **no** KEGG annotation in train/valid/test, so `(WWOX, KEGGPathway, ?)` is a genuine prediction, not a recovery.

## Inputs (fixed)
- Code: `emyyue/BioPathNet` at `b051a9003a1363b5655cdb7dfdad60609c0e4fe3`, scratch clone.
- Checkpoint: `model_epoch_12.pth`, sha256 `da298d1039b055852366362b494e773e86f5030abab33c8a620b2725c1ffe441`; config as in its training log (`gfun.yaml`: 6 layers x 32, distmult, pna, `remove_one_hop: yes`), CPU (`gpus: null`), `remove_pos: no` for prediction.
- Data: `PC_KEGG_0602` six files with the sha256 listed in the README.
- Provenance of steps: Pathway Commons 12 `PathwayCommons12.All.hgnc.txt.gz` (data sources and PubMed ids per SIF row), streamed and filtered in scratch.
- LEGEND needs: `needs/needs.json` on `it18-orch` (`156ed960`).

## Step 0 — feasibility (stop rule)
Throwaway venv outside the repository, CPU torch, torch-scatter, torchdrug. **Stop and record the exact limit** if: installation or extension compilation fails after two honest attempts; loading fails; one query (all 321 pathways for one gene) takes more than 10 minutes; resident memory exceeds 8 GB. Sanity of loading: tail-rank 100 test triplets (lowest sha256 of `head|tail`) among the 321 pathways, filtered for known positives; report MRR beside the logged 0.5579 (a sample, not a reproduction).

## Question and measures
1. **Predictions (a).** Top-10 KEGG pathways for `(WWOX, KEGGPathway, ?)`.
   - **Need-relevant** pathway (rule fixed now): a pathway with, in G1 train2, at least one gene equal to a `targets[].symbol` of any need in `needs.json` other than WWOX itself.
   - **B, simple reference**: neighbour vote — score(p) = number of distinct BRG neighbours of WWOX (any relation, either direction) annotated to p in train2; ties by pathway id.
   - **P4 contextual reference (LEGEND current path)**: the needs file already states the relevant axes; a top-10 pathway that is not need-relevant is an *added* relation, and is reported as such, never as a finding.
   - Report: need-relevant count in top-10 for BioPathNet and for B, overlap of the two top-10 lists. n = 1 query: **no superiority statement** unless the counts differ by at least 3, and even then only descriptively.
2. **Specificity (b).** Ten control genes: BRG degree within 0.8-1.25 times WWOX's (640), symbol not a needs target, chosen by lowest sha256 of the symbol. Jaccard of WWOX's top-10 with each control's top-10; hub pathways = in the top-10 of at least 8 of the 11 genes. **Non-specific** if the median Jaccard is at least 0.5 or at least 5 of WWOX's top-10 are hub pathways.
3. **Explanations (c).** Top-10 paths (the repository's `visualize.py` method: gradient edge importance, beam search) for the top-3 predicted pathways. Per step: head, relation, tail, direction as stored, whether the relation type is directed, whether the step is a G1 KEGG label (`KEGGPathway`), its Pathway Commons data sources and PubMed ids, and a **KEGG-leakage flag** when a BRG step's only data source is KEGG (the supervision source). Shares reported: directed steps, label steps, leakage steps.
4. **Source check.** At least 3 steps, chosen by rule: the WWOX-incident steps of the top path of each of the top-3 pathways, distinct, preferring directed types; if fewer than 3, the next-ranked paths. Each is checked against a primary paper (PubMed id from Pathway Commons where present, otherwise a PubMed search) and graded SUPPORTED (interaction and its type/direction stated in the paper), PARTIAL (interaction reported, type or direction differs or is only implied), NOT_SUPPORTED, or NOT_CHECKABLE (no primary source found), with a locator.

## Decision rules (fixed now)
- Step 0 fails -> **WATCH** with the exact limit as the reopen condition.
- **Verifiable explanations** = at least 3 checked steps SUPPORTED **and** at least one of the top-3 predictions has a top path whose every step is present in the released graph with at least one directed step and no leakage-only step.
- **Optional use** (explanation aid for gene-pathway relations of WWOX-adjacent genes; never drug evidence) only if verifiable explanations hold and the predictions are not non-specific.
- **WATCH** if the method runs but either condition fails, with the failing condition as the reopen trigger.
- **Discard for the current question** if explanations are not verifiable and predictions are non-specific.
- Whatever the outcome, the drug-target question stays unanswered by BioPathNet (no released drug model): stated as a limit, not as a result.
- An influential path is not a causal chain and not a pharmacological correction; no card, IPOTESI or queue entry is created from a path alone.
