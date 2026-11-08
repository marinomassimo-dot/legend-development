# Blind audit, INV-07 (PDH, pyruvate, lactate) — actor vf-07, task ORCH-IT38OS-20261108

Date 2026-11-08. Written before opening README.md, phase1_note.md or chains.tsv (not opened). Labels: DATO / INFERENZA / IPOTESI. No source below was reached only through a page summariser; two summariser attempts (PMC and the publisher page for 42909904) failed and nothing rests on them. PMIDs claimed for vf-07 before reading: 42909904, 16476929, 25012504, 16517405, 35984507, 42559713, 34747138, 32000863.

## How each source was reached (depth honesty)

| PMID | Route and depth |
|---|---|
| 42909904 (fly) | NCBI efetch of the PMC XML (main text, all Results and Discussion, methods) plus the local supplement text derived files `files/fulltext/PMID42909904_supplement/*_derived.txt` (legend text and tables). Figures not viewed; Fig 5D schematic not seen. |
| 16476929 (DCA MELAS) | PubMed abstract only (full text not reachable). |
| 25012504 (WWOX, HIF1alpha) | Abstract plus the local full-text file `files/fulltext/PMC4211377_PMID25012504_pmc_html_fulltext_2026-10-30.txt` searched and read at the Results passages on lactate, OCR, Pdk1; Supplementary Fig S2A only as cited in the text and in the repository manifest. |
| 16517405 (HIF-1, PDK1) | PubMed abstract only. |
| 35984507 (SH-SY5Y) | PubMed abstract plus a local Wayback copy of the PMC page, regex-searched for control arms, scrambled/genetic arms and lactate/PDH terms; methods and discussion passages read, not read end to end. |
| 42559713 (PDCD cohort) | Full text via the PMC tool, read end to end. |
| 40290041, 42012479, 36537114, 41710159, 42955568, 23611579 | PubMed abstracts. |
| 32000863 (lithium) | Local PMC XML (lithium passages) and the local Fig 7 image (viewed); module card `cards/G01_lithium_gsk3.card.json` read. |
| 34747138 (Repudi) | Local PMC XML, hypoglycaemia passages; Appendix Fig S1C/D not viewed. |
| DisMech WOREE | `/tmp/legend-dismech-audit-20261107/kb/disorders/WWOX-Related_Developmental_and_Epileptic_Encephalopathy.yaml` (1773 lines; an audit copy of unknown revision, not a repository file), keyword-searched. |

## A. Verdict per proposition

| id | verdict | basis (short) |
|---|---|---|
| P01 | SUPPORTED (as an absence inside its perimeter) | Independent PubMed-tool queries today: `(WWOX OR Wwox) AND (pyruvate dehydrogenase OR PDHA1 OR "pyruvate dehydrogenase kinase" OR dichloroacetate OR PDK1)` returned 42909904 and 33629572 only; `(WWOX OR Wwox) AND (lactate OR lactic) AND (neuron OR brain OR neural OR organoid)` returned 42909904 only. The perimeter is title/abstract: the same query does not return 25012504, whose body reports Pdk1 (see P02), so full-text-level data are outside it. Unknown, not negative. The fibroblast datum (no PDH activity difference; PDK transcript up in one condition) is in `needs/needs.json` NEED-PDH-PYRUVATE-AXIS O2, which I read. |
| P02 | SUPPORTED | Abstract; Results: lactate higher in Wwox-KO MEF medium, lower oxygen consumption (Seahorse), lower ATP, higher glucose uptake. Cell types are MEFs and tumour lines, no neural cell. Omission to note: the same paper reports higher Pdk1 transcript in KO cells and higher serum lactate in KO mice (see corrections 5). |
| P03 | SUPPORTED (abstract level) | Abstract: HIF-1 "directly trans-activating the gene encoding pyruvate dehydrogenase kinase 1 (PDK1)"; PDK1 inactivates PDH. Wording caveat: the abstract says "HIF-1alpha null cells"; "MEFs" rests on the MeSH terms Fibroblasts and Mice, and the transactivation claim and the null-cell rescue are two separate experiments. PDH-phosphorylation figures not read by me either. The statement that the WWOX link is a transfer through the HIF1alpha node is an INFERENZA and holds. |
| P04 | SUPPORTED | Main text and supplement text: Ldh transcript, L-lactate (interaction p = 0.0174 at 10 percent FDR; Wwox knockdown alone in the LacZ background p = 0.0636) and Atf4 immunostaining are the readouts. The downregulated pyruvate-pathway transcripts are named: `Pepck2`, `CG11052`, `Adh`; no PDH subunit, no Pdk, and "PDH", "Pdk" or "pyruvate dehydrogenase" occur nowhere in the body. Pyruvate does not appear as a measured metabolite (85 standard-matched compounds; supplement tables list no pyruvate row; only a pathway term). "No pyruvate value reported" holds for main text and supplement text; figures unseen. Model A and B not exclusive: INFERENZA, reasonable. |
| P05 | SUPPORTED | Atf4 was only stained (up in Abeta42 flies on Wwox knockdown, not in LacZ flies); no Atf4 RNAi or overexpression anywhere. Discussion: "the rescue we witnessed was partial" (verbatim sense). Rescue is combined Wwox+Ldh RNAi, startle-induced locomotion (days 14, 21, 28); the supplementary qPCR shows Ldh RNAi with Abeta42 only as a knockdown check, not as a behavioural arm. Head homogenate, Abeta42 background. Further relevant point the item does not carry: Discussion states Wwox overexpression rescue "occurs without a reduction in Ldh or 2-hydroxyglutarate", so Ldh is not shown to mediate Wwox protection generally. |
| P06 | SUPPORTED | Design: high glucose with Zfra1-31 given at 3 h or 24 h; comparator is cells without peptide; no scrambled peptide, no genetic WWOX arm; the paper says Zfra1-31 does not affect control cells but marks it "data not shown". No lactate, pyruvate or PDH measurement found by keyword search (only sodium pyruvate in media). Not a sign reversal of a loss model: INFERENZA, holds. |
| P07 | SUPPORTED (abstract level); the report's own phrasing is NOT SUPPORTED | Abstract: double-blind crossover, 30 patients, 25 mg/kg/day; "15 of 15 randomized to DCA were taken off study medication, compared to 4 of 15" placebo (15 + 4 = 19); "discontinued in 17 of 19 patients because of onset or worsening of peripheral neuropathy"; terminated early for peripheral nerve toxicity. So 17 of 19 is a share of the 19 who stopped, 19 is not the cohort, the cohort is 30, and the abstract does not split the 17 by arm. The report (L13 "17/19 patients affected", L24 "17 of 19 patients developed or worsened peripheral neuropathy") uses 19 as if it were the trial population: wrong denominator framing. "Documents risk in MELAS, not WWOX" holds. Also from the 23611579 abstract: 8 patients, 3 PDC-deficient, not on ketogenic diets; DCA kept lactate normal; nerve conduction fell and led to dose reduction or temporary stop in 3, "symptomatic worsening of peripheral neuropathy did not occur". The report's "reduced nerve conduction in some" is accurate; it omits that DCA worked in PDC deficiency without KD. |
| P08 | SUPPORTED | L13 "not mechanistically justified", L23-26 heading "conditionally justified at best", L26 "justified only under a narrow, currently unsatisfied condition", L79 table row: same unmet prerequisite. Abstract of 16517405: forced PDK1 in hypoxic HIF-1alpha null cells raises ATP and lowers ROS. The report's quotation drops "HIF-1alpha null"; transfer to WWOX neurons is IPOTESI, as the item says. |
| P09 | SUPPORTED | 42559713 full text: KD in 30 of 41; prenatal group 6 of 7 with epilepsy had reduced seizure frequency, postnatal 2 of 2 with active epilepsy became seizure-free (8 of 9); outcome by treating physician on a 5-point scale, retrospective; thiamine (300-500 mg/day) in 28 and concurrent with KD; no control arm. 40290041: narrative review, PDCD among "absolute indications". 42012479: "Lactate levels decreased ... in all patients with PDCD" in a pooled "GLUT1D and PDCD (n = 20)" group; the PDCD count is not in the abstract. 36537114 abstract: epilepsy "responded to a ketogenic diet in three patients" of five. Inferences hold. |
| P10 | PARTLY | I confirm the DisMech YAML text has no lactate, acidosis, PDH or mitochondrial node; its only glucose item is the mouse hypoglycaemia in the AAV model. But "no lactic acidosis in human WOREE" is therefore a statement about the card, not about patients, and LEGEND's own registry already holds a lactate datum the producer did not use: `registries/paper_registry_current.md` PAPER 017 (PMID 36537114): lactate "lievemente elevato in P4 (2.4-3.3 mmol/L)" in one of five null/null individuals. The item's "clinical lactate and glucose data were not re-read" is true and is exactly the gap. |
| P11 | SUPPORTED, with two refinements | Fig 7d viewed: LiCl lowers the PTZ stage in all three genotypes (bracket marked four asterisks in each of +/+, +/-, -/-). In the null the PTZ-alone peak is about 3.5 and about 1.3 with LiCl, so seizures are suppressed, not abolished; the report's "abolishes" repeats the paper's abstract wording ("significantly abolishes the onset"), uncited. Refinement 1: "equal in wild type and heterozygote" means "also present", not equal magnitude; wild-type and heterozygous PTZ-alone scores are low (about 1), so a floor effect limits what can be seen, and no genotype-by-drug test is given; "non-specific" is an INFERENZA of the card (the card itself says so: "equally present in wild type and heterozygote: non-specific"). Refinement 2: the card also states the attribution to GSK3beta rests on lithium alone and the Ser9 datum is one blot, one site; Cheng 2020 reports pSer9, not a Wnt measurement, so "Wnt/GSK-3beta dysregulation is an independent seizure driver" is not established. |
| P12 | SUPPORTED | Table L86-97 has 12 PMIDs; text adds 34747138 (L32) and the DisMech YAML; footer L124 says 25 papers reviewed; 12 reviewed papers are untraceable. |
| P13 | SUPPORTED as a statement of content | L13 and L122 wording confirmed. That it "follows from" P01/P07/P08/P09 is the producer's reading; note it does not engage with 23611579 (DCA normalised lactate in PDC deficiency without KD). |
| P14 | SUPPORTED | 34747138 text: neuron-restricted vectors gave "normal blood glucose levels when compared to the wild-type mice (Appendix Fig S1C and D)"; no sentence about the human course. The "no direct counterpart in the human course" wording is in the DisMech YAML limitations field (lines 1291-1293: hypoglycaemia and premature lethality "have no direct counterpart in the human course"), i.e. the curators', not the paper's. Appendix figure not viewed. |

Substantive points not in any item (found while verifying, DATO from the local full text of 25012504): Results state higher Pdk1 in Wwox-KO cells ("we observed higher levels of Pdk1", RT-PCR, Fig 3a text) and higher serum lactate in KO mice (Supplementary Fig S2A, n = 4 vs 12 in the manifest). The report's node table lists PDK1 expression as "inferred from HIF1 biology (16517405)"; a WWOX-specific transcript datum exists, non-neural, no PDH activity or phosphorylation measured. It does not change the neural conclusion; it changes "separation of WWOX datum vs transfer" for the PDK1 node.

## B. Coverage audit (12 points, complete report read)

| # | report point (line) | extraction row | result |
|---|---|---|---|
| 1 | UI text "View full report" (L3-4) | E66 | PRESENT |
| 2 | MONDO id (L6) | E67 | PRESENT |
| 3 | hypoglycaemia "consistent with" glycolytic consumption (L19) | E08 | PRESENT |
| 4 | "all WWOX metabolic data derive from cancer cell lines and MEFs" (L21) | E03 (says the chain was assembled only in tumour biology) | PRESENT_NARROWED: the universal claim is not recorded as such; it also conflicts with the report's own SH-SY5Y, fly and Wwox-null mouse material |
| 5 | long-term DCA in congenital lactic acidosis (L24) | E26 | PRESENT |
| 6 | lithium "abolishes" PTZ seizures, uncited (L26) | E29 | PRESENT |
| 7 | Wwox overexpression reduced amyloid (L38) | E16 | PRESENT |
| 8 | scenario 4, fixed ETC/OXPHOS defect (L82) | E49 | PRESENT |
| 9 | KD "established adjunct" in drug-resistant genetic epilepsy (L29) | E35 | PRESENT |
| 10 | "The only direct neural dissection of pyruvate handling" and "the only direct human-neuron WWOX-mitochondria study" (L98) | none | MISSING |
| 11 | DisMech has no metabolic node, no prior (L112) | E09 | PRESENT |
| 12 | "Neither metabolic therapy is disease-modifying; root-cause strategy WWOX gene replacement" (L122) | E64 | PRESENT |

Result: 10 PRESENT, 1 PRESENT_NARROWED, 1 MISSING (10 of 12 fully present, 11 of 12 present in some form).

Extension scan after the MISS (same kind: uniqueness/universal/absence claims and framing sentences): further misses are (a) L98 second "only" (human-neuron study) counted with point 10 above; (b) L9 "never interrogated in human neurons, brain organoids, or isogenic WWOX-null neural models" is carried only partly (E02 covers human neural cells; E54 the experiment); (c) L72 lactate row of the node table ("neural only in fly; non-specific") is spread across E15/E38, not recorded as a table row (narrowed, harmless); (d) L91 "the condition most analogous to a putative WWOX PDH defect" is a framing sentence, covered in spirit by E32 (narrowed). No other class of content (compound, experiment, caveat, counter-argument) was found missing: the experiment list (L114-121), decision table (L79-83), caveats (L102-112) and footer are all present.

## C. Reconciliation sample (8 rows)

`reconcile.tsv` has no row with `legend_class = new_to_legend` (classes: 23 already_present_and_used, 12 unverified, 6 verified_or_corrected, 4 present_not_used, 2 superseded_or_contradicted). The only row marked new is E35 in the `legend_novelty` column, so I used it as the new-to-legend slot and say so.

| row | class | pointer check | result |
|---|---|---|---|
| E35 | `legend_novelty` = new_to_legend | EV09 (36537114) exists in evidence.tsv; but the repository already holds the paper | NOT CONFIRMED: `registries/paper_registry_current.md` PAPER 017 (PMID 36537114), "Note: KD associata a miglioramento crisi in 3/5", corrected 2026-09-29 (CLAIM 042: three responders named, number who started the diet not stated), and `analysis/ft125_chong2023_targeted_reread_20260921.md` lines 140 and 167 repeat it. Not new; should be present_not_used. The PAPER 017 note also holds the lactate datum (P10). |
| E02 | already_present_and_used | `ranking_it8_p9_20261029/investigations.tsv` INV-07 (row exists, "one human activity measurement shows no difference"); `needs/needs.json` O2 (read: PDH activity no difference in any condition, lactate higher in all four) | CONFIRMED |
| E40 | already_present_and_used | previous BRIEF.md item 3: "PDK1 of pyruvate dehydrogenase is not PDPK1" | CONFIRMED; prior fate `kept` correct |
| E29 | present_not_used | `cards/G01_lithium_gsk3.card.json` p4_fields text matches the row | CONFIRMED; prior fate `omitted` correct (previous BRIEF.md does not name lithium; it only tells the reader not to duplicate the gsk3_eif2b package) |
| E26 | present_not_used | receipt `FTR-20261023-23611579-01` exists in `registries/fulltext_read_receipts.jsonl` with whole JATS body read (stronger than "not reopened" suggests) | CONFIRMED; prior fate `omitted` correct (23611579 not in the previous BRIEF.md) |
| E17 | superseded_or_contradicted | `metabolic_inv07_20261107/output/evidence.tsv` E02 and E22 exist and say what the row says | CONFIRMED; prior fate `modified` consistent with BRIEF item 2 |
| E21-E23 | superseded_or_contradicted | `output/README.md` and `explanations.tsv` exist | CONFIRMED on content; prior fate `narrowed` is too soft: the previous BRIEF.md says the report "prematurely favours LDH/ISR" and says not to read the Ldh rescue as excluding PDH, which is `modified` |
| E11 | verified_or_corrected | `deepdive_manifests/PMID34747138.json` "entries 541-542 and 601" | pointer wrong unit: 541-542 and 601 are file line numbers (the file has 29 entries, indices 0-28); the content at those lines is right; prior fate `omitted` correct |

Four rows checked for `prior_brief_fate` against `metabolic_inv07_20261107/BRIEF.md`: E40 kept, E29 omitted, E26 omitted, E11 omitted (all agree); E21-E23 and E17 also read (E21-E23 disagree in degree, see above).

## D. Evidence sample (`evidence.tsv`, all 9 rows)

All nine locator quotes are verbatim in the source at the stated place and carry what the role says: EV01 (abstract, 8/9; body 6/7 + 2/2), EV02 (Discussion, retrospective), EV03 and EV04 (abstract), EV05 and EV06 (abstract of 42012479), EV07 and EV08 (abstract of 16517405), EV09 (abstract of 36537114: "epilepsy that responded to a ketogenic diet in three patients").
Limits: EV08 supports "HIF-1 transactivates PDK1" but not "MEF" (P03 wording); EV05 carries "all patients with PDCD" only as an abstract statement inside a pooled group.
Gap: evidence.tsv backs only P03, P08 and P09. The decisive P02, P04, P05, P06, P07, P11, P14 and P10 have no row; they rest on prior-package ids (i7:E24-E32), cards and manifests. Not an error in a row, but a reader of this folder alone cannot check them.

## Corrections the producer must make

1. `extraction.tsv` E25 (and any decisive/README line repeating it): the content sentence "terminated early because 17 of 19 patients developed or worsened peripheral neuropathy" reproduces the report's wrong framing. Record the abstract: 30 randomised, 19 taken off study medication (15 DCA, 4 placebo), 17 of those 19 for onset or worsening of neuropathy, trial stopped for nerve toxicity; mark the report's "17/19 patients affected" as a denominator misreading.
2. `reconcile.tsv` row E35: change `legend_novelty` from new_to_legend to no and `legend_class` to present_not_used; `where_in_legend` = PAPER 017 in `registries/paper_registry_current.md` and `analysis/ft125_chong2023_targeted_reread_20260921.md` lines 140, 167; keep the note that three responders are named but the number who started the diet is not stated. State that this package has no new_to_legend row.
3. `reconcile.tsv` row E10 and decisive P10: replace "clinical lactate/glucose data not re-read" by the existing registry datum (PAPER 017: lactate mildly elevated in one of five, 2.4-3.3 mmol/L, one patient) and keep "absent in the card is not a normal biochemical result".
4. `reconcile.tsv` row E11: "entries 541-542 and 601" to "lines 541-542 and 601 (the manifest has entries 0-28)".
5. `reconcile.tsv` row E05 ("not a WWOX datum") and `extraction.tsv` E05, E39: add that 25012504 reports higher Pdk1 transcript in Wwox-KO cells and higher serum lactate in KO mice (non-neural; PDH activity and phosphorylation not measured there), and fix the report's "inferred from HIF1 biology" accordingly.
6. `extraction.tsv`: add rows for L98 "the only direct neural dissection of pyruvate handling under Wwox loss" and "the only direct human-neuron WWOX-mitochondria study" (absence/uniqueness claims, no perimeter stated), and for L21 "all WWOX metabolic data derive from cancer cell lines and MEFs" (universal claim contradicted by the report's own Findings 4 and 6).
7. `extraction.tsv` E16: add the Discussion statement that the Wwox-overexpression rescue occurred without Ldh or 2-hydroxyglutarate falling; it limits the reading of Ldh as the mediator of Wwox effects.
8. `reconcile.tsv` rows E21-E23: prior_brief_fate `narrowed` to `modified`.
9. `evidence.tsv`: add rows (or cross-reference ids) for P02, P04, P05, P06, P07, P11, P14, with the depth stated.
10. Decisive P03 wording: "HIF-1alpha null cells" (abstract), not "MEFs", unless the full text is read. Decisive P11 wording: "also present in wild type and heterozygote at low baseline; no genotype-by-drug test; seizures suppressed, not abolished (null peak about 3.5 to about 1.3, read from the figure)".

## Open uncertainties

- 16476929 and 16517405 were reached at abstract level only; PDH-phosphorylation panels of 16517405 and the full denominators of 16476929 (arm split of the 17) remain unread.
- 42909904: figures, Fig 5D schematic and the metabolite table were not viewed as images; "no pyruvate value" rests on main text and supplement text. The statement that the fly rescue is "partial" rests on the authors' Discussion.
- 35984507: Wayback copy regex-searched, not read end to end; "data not shown" for peptide alone on control cells.
- 34747138: Appendix Fig S1C/D not viewed; DisMech YAML is a /tmp audit copy of unknown revision (the repository's own copy was not located).
- P01 is an absence claim with title/abstract perimeter; two PubMed-tool queries today, no second database run by me, and full-text-only mentions (as with Pdk1 in 25012504) are invisible to it.
- The mild lactate elevation in one WOREE individual is an abstract-independent registry note (partial full text, non-open access); I did not re-open the paper.
