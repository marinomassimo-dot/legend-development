# ADV-242 result: the GSE156243 library-to-clone map is not stated (SCI, 2026-11-25)

Actor `orchestrator` (SCI). Hypothesis level; reference genotype class; nothing here is medical advice. Held files, plus free GEO sample metadata for three comparator deposits; no spend, no contact, no delegate. Pre-registration: `PREREG_ADV242_SCI_20261125.md` (time and digest in the companion files; written in the job scratch folder while a gated push held the worktree).

## 1. Answer

1. **No source read ties any of cko1 to cko4 to a knockout clone.** The 20-minute exit applies: no clone-level removal was run. The organoid rows stay "not testable" (ADV-239), and they cannot be said to include both clones.
2. **What the sources do state** (PMID 34268881, held XML and files):
   * two knockout clones, 1B (KO1) and A2 (KO2), "were selected for the organoid generation";
   * "A total of 8 CO samples were sequenced (4 WT COs and 4 KO COs)", with no clone given for the KO samples;
   * the authors' reply in the peer-review file says another assay used "a totally different batch of the one we performed the RNA-seq", which reads as **one** sequencing batch; the GEO design says the wild types are age- and batch-matched.
3. **The two removed wild types were not removed for the same reason.** One failed quality control; the other "did not cluster with any of the other samples (neither WWOX-KO nor WT)". The control arm of 2 is what remained after an outlying control was taken out, and its counts are not in the deposited table, so its influence cannot be measured.
4. **Consequence.** The four knockout libraries may come from one clone or from two. Until the map is known they support "knockout organoids of this one line and batch", not "two clones agree".

## 2. Where I looked

| Source | What it says about clone or batch |
|---|---|
| GEO sample records (held SOFT file) | "Knock out of WWOX", 15 weeks, WiBR3; no clone, no batch per sample |
| Article body and legends | two clones selected for organoids; RNA-seq "WT: n = 2, KO: n = 4" |
| Figure EV3A (PCA) and Figure 4 (heat maps), viewed | labels KO / WT or CKO / CWT only |
| Supplement tables s002, s003, s005, s006, s008 (header strings) | no per-sample column |
| Appendix (s001) and peer-review file (s007), text search | the batch sentence above; no clone map |

Not read: the supplement's remaining PDF pages as images, and the raw reads.

## 3. What was already known

This is mostly not new, and my proposal's duplicate check was too narrow. My own dated line of 2026-11-20 (`adv099_neuron_discovery_sci_20261120/DATED_LINE_ORGANOID_LIBRARY_GROUPS_NOT_CELL_CLUSTERS_NOR_CLONES_SCI_20261120.md`) already says that the deposit does not state clones or batches and withdraws the word "clones" for the two library groups. The two exclusion reasons are already in `deepdive_manifests/PMID34268881.json` and in `analysis/therapeutic_canonical_repair_package.md`. Added today: the article names the two organoid clones (so a clone split is possible but unassigned), the batch sentence, and the search of figures, supplements and review file.

Wording that is now known to be incomplete: ADV-069's result and the 2026-11-20 line say that two wild types "failed quality control"; only one did.

## 4. Units of the three deposits ADV-239 did not compile

Held files give at most a sample count (GSE274921: 9; GSE327470: 292, both from earlier record-page reads); no group split. The GSE268132 paper (PMID 40140574) is not among the held full texts (the held "Chen 2025" is PMID 39847501, another study). The split below comes from GEO records fetched today (digests in `geo_metadata_sha256.txt`).

| Deposit | Units | Leave-one-out possible? | Used by |
|---|---|---|---|
| GSE274921 | 9 libraries of bulk E16-17 mouse forebrain: 5 wild type, 4 germline heterozygote. The records label the samples "Astrocytes"; the growth protocol says bulk forebrain | yes, if per-sample values were taken (not done) | RP-033 |
| GSE268132 | 24 libraries of mouse fibroblasts: 3 knockdown conditions, polysome and total RNA, 4 replicate cultures each | yes on replicate cultures, which are not individuals | RP-018 |
| GSE327470 | superseries: GSE326044 has 5 single-cell libraries (organoid days 8, 13, 20, 25, each mixing lines A1, A2, B1, B2, and one pooled embryo sample); GSE327468 has 287 single cells | no: one library per age | RP-043 |

## 5. Predictions

| | Prediction | Outcome |
|---|---|---|
| P1 | the sources tie each knockout library to a clone (0.4) | Not met |
| P2 | if so, Wnt and glycolytic items agree across clones | Not testable |
| P3 | units recoverable from held files for at least one of the three deposits | Not met: counts only |

## 6. Proposed wording

For the organoid rows (K01, D01, D02, M01, E02, I01, INV-16, RP-008, CLAIM 002; claim text only through a candidate): "four knockout against two wild-type organoid libraries of one parental line, apparently one batch; which knockout clone each library comes from is not stated; one further wild type was excluded for not clustering."

## 7. A route not taken

The raw reads (SRX8947985 to SRX8947988) may carry each clone's edit in WWOX: the article shows Sanger sequences of the clones, and reads over the targeted exon could assign each library. This needs a raw-read download, outside this assignment, and works only if the two edits differ and the exon is covered; neither was checked. It is the one free route found that could turn "not stated" into a map.

## 8. DREAM

Not yet consumed: the wording of section 6, and ADV-239's finding that a pre-registered "declared threshold" can differ between two carriers of the same run (only the P47T candidate has taken it in).
