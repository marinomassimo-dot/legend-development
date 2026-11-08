# DREAM-4: one deposit carries the human-neural sign of ten needs — what that changes (2026-11-08)

Non-canonical working note; exploratory; not medical advice. Public edition, reference genotype class. No spend, no e-mail, no contact with EBI or the authors. Cost and checks at the foot.

## Answer first

**Which useful connection did LEGEND hold only in pieces, and what work changes once the pieces are joined?** Each need records its own composition or maturity caveat on the organoid transcript it leans on, but no place says that **ten needs lean on the same week-15 bulk deposit** (`GSE156243`, WiBR3 hESC knockout, 4 libraries against 2), that this deposit cannot separate genotype from composition, and that the only dataset that could replicate the signatures within matched cell populations and across patient-derived lines (`E-MTAB-14792`, answers HTTP 403, release request an unsent draft) is a **different genetic background** (JH-iPS11 iPSC). Joined, this changes three things: (1) what the operator's pending decision on the release request would decide: the question in the draft names Wnt only, the deposit bears on six more axes; (2) the needs carry a lost qualifier (line identity), delta prepared for the session that owns them; (3) a way to read the data once released that separates a signature that scales with the progenitor fraction from one that does not. Nothing here shows that the signatures are artefacts; it shows which readings would be separated, and by what.

## The chain

| Step | Content | Source and origin |
|---|---|---|
| Observations | Human-neural evidence of ISR, PDH, lactate, mitochondrial, inhibitory, GABA-chloride, Wnt, mTOR, glia and NRF2 needs includes the week-15 bulk organoid transcript of `GSE156243`; ISR, PDH, lactate and mitochondrial add a one-library-per-arm shRNA CAGE set; only Wnt, MYC and myelination hold single-cell or immunostained organoid data | `needs_human_neural_systems.tsv` (built from `needs/needs.json`; a keyword pass, so the "caveat present" column is an indicator, not a reading) |
| | That bulk deposit is composition-shifted and genotype is collinear with every composition score (2 wild-type libraries): the reanalysis "cannot separate" them, "weak lean away from composition explaining all of it"; composition z shifts RG +0.52, neurons −0.83, cortex −0.43, non-cortical +1.52 | `gse156243/independent_reanalysis_wnt_vs_maturation_20261025.md`, lines 30, 53, 61 (read) |
| | The 2026 paper's main knockout is the iPSC line JH-iPS11 (clones WKO-1C, WKO-2C); the WiBR3 hESC knockout of the 2021 study (reference 23 = PMID 34268881, the source of `GSE156243`) is used there for a validation, a drug treatment and NSC/ChIP-seq, and is "one of several independent models" | original text, `PMID42397075_..._layout.txt` lines 438-447, 694-695, 953, 1221-1223; independent check below (P1, P2) |
| | At week 7 the SOX2-positive share of nuclei is graded: WT about 13 %, patient lines (SCAR12, WOREE) about 43-48 %, knockout about 77 % (hand readings of Figure 1F, ±5 points); the paper states a genotype-dependent gradient with the knockout most severe | Figure 1F and lines 521-526; independent check (P3) |
| | MYC-positive share of SOX2-positive cells is raised about equally in the knockout and both patient lines (about 60, 50, 55 against 20 %, week 16) | `needs.json` NEED-MYC observations (as recorded; not re-read here) |
| | Single-cell data of the 2026 study: five libraries, one per condition (WT, knockout, SCAR12, WOREE, WOREE with add-back) | `census_reconciliation_it7_20261029.md` C8, from the preprint methods (published methods not read) |
| Relation proposed | A signature that is composition-driven should scale with the progenitor fraction (knockout > patient lines > wild type) and shrink within radial glia; a cell-autonomous or allele-general one should be present within radial glia at similar size in all three mutant lines, as the MYC share is | inference |
| Competing explanations | (a) composition or developmental stage; (b) cell-autonomous change; (c) regional-identity drift (non-cortical +1.52 z in the bulk reanalysis; dorsal identity assessed in the 2026 paper only as supplement); (d) background or clone (WiBR3 against JH-iPS11, one differentiation per line); (e) any mix. Cause, compensation and consequence stay open. | |
| Decision | Send or not the release question for `E-MTAB-14792` (operator); the order and the reading of the human-neural checks that sit behind the ISR, PDH, lactate, mitochondrial, Wnt, GABA and NRF2 needs | |
| Discriminating measure | Per-line gene-set scores **within radial glia** and **within neurons** in `E-MTAB-14792`, compared with the pseudobulk of the same line and with the progenitor fraction; direction concordance across knockout, SCAR12-class and WOREE-class lines is the available replicate-like check | `DL-MECH-181` (falsifier and limits there) |

## What was already known, and what was combined

| Kind | Items |
|---|---|
| Already present and used | Wnt against maturity (NR-04, HYP-20261025-09; the release draft states this use); ISR composition as a compatible reading, "cell-resolved data … not accessible" (`context_differences_it7_p4_20261029/README.md` line 99); MYC across three lines |
| Present, not used together | each need's own caveat; the reanalysis "cannot separate"; the 2026 gradient; the add-back library |
| New combination in the repository | the tally (ten needs, one bulk deposit); the fact that the single-cell deposit is a different background from the bulk one and no need carries the line identity (`JH-iPS11` occurs 0 times in `needs.json`, `WiBR3`/`hESC` once); the graded-against-allele-general reading rule |
| Novelty against the literature | not assessed; no claim |

## Controls where a plausible link was rejected or left open

* **"Wnt drives MYC" (the paper itself says the pathways can induce each other, refs 51-52): kept unresolved.** The Wnt rows rest on the bulk knockout, whose composition is shifted; the MYC rise is present in the patient lines, whose composition is graded and not wild-type-like at week 7. Nothing here gives an order between them.
* **"The patient lines are a composition-matched control" (my first reading, from `needs.json` O3: scRNA fractions within about 0.3 of wild type at week 16): rejected for week 7.** The immunostained SOX2-positive share is intermediate in both patient lines. The two readings hold at different stages and by different methods and are both kept; the patient lines are a graded comparator, not a matched one.
* **"The 2026 composition applies to the 2021 bulk" (the Wnt need uses the 2026 knockout composition to read the 2021 bulk): not licensed as stated.** Different parental background; the 2026 text reports a "similar imbalance" in the WiBR3 knockout at week 15 by immunostaining (Supplementary Fig. 4I-J, not held), which supports similarity, not equality.
* **"MYC raises the ISR target set" (a textbook coupling): not taken.** No file here measures ISR transcripts within the MYC-high compartment.

## Independent check of the decisive details

One typed delegate (`legend-delegate`, Sonnet, effort as the agent definition sets and not raised) received only three propositions and the original files, not this reasoning. Results: **P1 partly**: the JH-iPS11 knockout as the main Figure 1 system is supported, but "only a validation" is too strong, the WiBR3 system is also used for the A51 treatment, NSC derivation and ChIP-seq (text corrected above); **P2 partly**: reference 23 is the 2021 paper (supported); that its RNA-seq came from WiBR3 knockout derivatives is the natural reading of the paper but not stated verbatim for the RNA-seq panel (the 2021 methods say WiBR3 knockout clones and a WiBR3 wild type); **P3 partly**: the graded pattern is supported, the ordering of SCAR12 against WOREE is not resolved. Verdicts are in `results/verifier_verdicts.md`.

## What was delivered, and what is not yet applied

| Item | Where | State |
|---|---|---|
| Exploratory lead | `DL-MECH-181` in `discovery_ledger_current.md` | written; staged spec in `lead_staging/plan/` |
| Operator note | foot of `ebi_access_request_E-MTAB-14792_draft.md` | written; the request text is unchanged and **not sent** |
| Delta for the owners of the needs and the generator | `DELTA_FOR_IT39.md` | prepared, exact text; **not applied**: the needs and the generator belong to the main session |
| Use by the generator or a ranking | none | **not shown**; nothing consumes the lead yet |

## Micro-upgrade

None. The retrieval was done with existing tools; the helper `dream_pass.py` was not needed and was not changed.

## Cost and checks

Observed (harness report of the one verifier delegate): 31,074 tokens in total, 6 tool calls, 32.8 s wall; one delegate, no second round. The main-session cost of this pass is not separated. Estimated, not observed: none claimed. Checks: lead validated by `discovery_lead.py check`; the decisive details checked by the independent reader above; the gate and LINT were run on the changed files before landing.

## Limits

* The tally is built by a keyword pass over `needs.json`; "caveat present" is an indicator.
* Fraction values from Figure 1F are hand readings; the scRNA fractions and the MYC shares are taken as recorded in `needs.json`, not re-read.
* No data were analysed: the discriminating dataset is not accessible. This note orders questions and readings; it measures nothing.
* One library per condition limits what any release can resolve; a concordant direction across three lines is the most it gives.

## Change or remove

Delete this folder, the operator note at the foot of the draft, and close `DL-MECH-181` with a dated line (ledger entries are append-only). Nothing else depends on it.
