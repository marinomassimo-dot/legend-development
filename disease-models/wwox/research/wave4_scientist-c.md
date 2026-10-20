# Wave 4, group W2 first half — scientist-c

Task W4-W2A-C-20261019 · branch task/W4-W2A-C-20261019 · worktree `.claude/worktrees/w4-c`. English; nothing
here is medical advice; public, disease-level edition. Per paper: what it MEASURES (system, genotype,
tissue, readout) and what that changes or fails to change in the disease model; the negative is the product;
no novelty is claimed; no hypothesis is promoted to a claim. Rows labelled SUBSTITUTE are disease-class
papers and are **not WWOX evidence**.

## 0. Lot and stated questions (written before any body was opened)

Lot: the first eight rows of group W2 in file order, excluding 29481666 (known unreachable per the
coordinator). Staged-receipt directories and the ledger were checked for every PMID: none holds a receipt.
All are `first_read` (`context_policy: SOURCE_FIRST`; the held context is only the selection row's one-line
"why it matters"). Receipts are staged under `receipt_staging/scientist-c/`, not appended.

| PMID | Question held before reading |
|---|---|
| 25779665 Chen 2015 | Does the temperature thread have any basis in WWOX biology beyond cell-death assays: does the body report only 4 C bubbling death, or any in vivo cold or fever sensitivity? |
| 36587184 Friemel 2022 | Is the NASH-HCC WWOX copy-number loss tumour genomics only, or does any panel or table tie WWOX to a metabolic or steatosis readout? |
| 41141138 Sharma 2025 | In seven bone-tumour cases against five controls, what is measured for WWOX and RUNX2, in which tissue, and what does it support for the RUNX2 link? |
| 37686047 Rushing 2023 | Is the WWOX copy-number line in alkylating-agent-resistant NCI-60 lines more than a gene-list sentence: is a metabolic readout tied to WWOX? |
| 22842668 Pluciennik 2012 | In Wilms' tumour, what WWOX alterations are measured, and is there any renal-function or metabolic content? |
| 29899766 Mastrangelo 2018 (SUBSTITUTE) | Which treatable cofactor and metabolic causes (B6, folate, biotin, creatine, CoQ10, serine) belong in a DEE work-up, and what can a negative screen say? |
| 36980111 Mastrangelo 2023 (SUBSTITUTE) | Which seizure phenotypes respond to B6 across the B6-dependent diseases, and what would a pyridoxine response look like in a class-level reading? |
| 38978529 Girgis 2024 (SUBSTITUTE) | What does a cerebral folate transport deficiency look like in practice, and which CSF readout defines it? |

---

## 1. PMID 25779665 — Chen 2015, UV/cold shock-mediated apoptosis switched to bubbling cell death at low temperature (WWOX-direct, W2 temperature axis) — receipt FTR-20261020-25779665-01

**What it MEASURES.** System: cultured COS7, L929 and B16F10 cells and Wwox+/+ versus Wwox-/- MEFs, in vitro.
Trigger: UVC 480 mJ/cm2 then 5 min at 4 C, then incubation at 4, 22 or 37 C. Readouts: percent of cells that
extrude a single nuclear "gas bubble", DNA laddering, annexin V, NOS2 and TRAF2 by immunofluorescence and
blot, p53 and pS46-p53, EM of the burst nucleus, one human frostbite IHC pair.

**Question and answer.** Does the temperature thread rest on anything beyond a cell-death assay? No. Temperature
is a post-irradiation culture condition of cell lines (Figure 1B-D: at 4 C versus 37 C bubbling is about 57%
versus 18% at 2 h and converges at 4 h; DNA laddering is blocked at 4 C). The only in-tissue datum is a
frostbite-versus-normal human skin IHC pair (Figure 7C: WWOX up above 80%, TRAF2 down above 90% in the text)
with no n, no plotted quantification and "skin sections from patient" in the Methods. There is no in vivo
cold or fever experiment. The direction for WWOX loss is protection: Wwox-/- MEFs resist bubbling death
(Figure 6B: about 28/45/85% bubbling in +/+ at 0.5/1/2 h versus about 0-2% in -/-, n = 3), so nothing
here supports a WWOX-loss cold sensitivity or hypothermia mechanism. The metabolic statements are "data not
shown" (bubbling "does not require ATP"; HIF1alpha involvement "unknown"); nutrient stress changes the
outcome (24-48 h starvation gives autophagic death without bubbles) but only in a representative movie that
is not retrievable.

**What it does not support.** A link between WWOX and body temperature, thermogenesis, hypothermia or cold
tolerance; any energy-metabolism readout; any neural or in vivo statement about WWOX loss.

**Effect on the model.** The "temperature" axis in W2 stays "no WWOX evidence beyond cell-death assays". It
does not explain the whole-body-null hypothermia read earlier in this batch (a runted, fat-depleted animal): that
phenotype has no mechanistic bridge in this paper. Class MINOR; no claim touched. Debts: nine
supplementary movies and the laboratory's UV/TRAF2/p53 primaries (queued in the commit candidate).

---

## 2. PMID 36587184 — Friemel 2022, single-cell ploidy and chromosomal aberrations in NASH-induced HCC and precursor lesions (WWOX-direct, W2 liver steatosis axis; tumour genomics) — receipt FTR-20261020-36587184-01

**What it MEASURES.** System: archival FFPE liver from Zurich, 11 NASH-associated HCC resections and 11
NAFLD/NASH biopsies; single-nucleus multiplex FISH (eight loci, WWOX on a custom 560 kb BAC contig at
16q23.1) with FISHtrees phylogenies. Readout: signal number per nucleus (gain or loss), ploidy, an
instability index. No WWOX RNA or protein, no metabolic variable beyond the clinical steatosis percentage.

**Question and answer.** Does any panel or table tie WWOX to metabolism or steatosis? No. (1) The WWOX
signal is an HCC event: "NAFLD/NASH lesions did not show any clonal copy number changes" for the whole
probe panel, so there is no WWOX loss in the steatosis or steatohepatitis tissue. (2) Instability index
against macrosteatosis is flat (Figure 2C, p = 0.26, 11 points); only tumour grade correlates (p = 0.01).
(3) A count problem the text hides: the headline is WWOX loss in 4 of 11 cases (Table 1: cases 2, 3, 7, 8),
but Figure 3A marks 15% WWOX loss in case 1 (and Figure 3B draws a WWOX-negative terminal clone), no
loss-calling threshold is stated, case 3's WWOX value is printed in the gains column in
Supplementary Figure 3 and coloured green in one copy and red in the other although Table 1 lists it as a
loss, and cases 4 and 5 have no panel anywhere. Per-case losses read from the figures: 93% (case 2), 3%
or a 44% gain/loss conflict (case 3), 35% (case 7), 49% (case 8), 15% (case 1), 6%, 3%, 1% (cases 9-11), 0% (case 6).

**What it does not support.** Any statement about WWOX function in hepatocytes, steatosis, glucose or lipid
handling; a WWOX copy-number change in the precursor lesion; "WWOX loss is a novel NASH-HCC finding" beyond
a small unreplicated FISH series with an unspecified call threshold.

**Effect on the model.** Liver steatosis stays "no WWOX evidence" (tumour genomics only). The count and
colour inconsistencies are logged in the commit candidate. Class MINOR.

---

## 3. PMID 41141138 — Sharma 2025, WWOX and RUNX2 immunohistochemistry in childhood Ewing sarcoma, a seven-case pilot (WWOX-direct, W2 bone axis; tumour biomarker) — receipt FTR-20261020-41141138-01

**What it MEASURES.** System: FFPE tissue from seven Ewing sarcoma cases and five unspecified controls
(one Indian centre, 2019-2024), IHC intensity scores for WWOX and RUNX2 with ImageJ, a Kaplan-Meier curve of
overall survival. No genotype, no function, no neural tissue.

**Question and answer.** What is plotted for WWOX and RUNX2 and what does it support for the RUNX2 link?
WWOX does not differ (medians about 204 versus 197, P = 0.876); RUNX2 is higher in cases (about 238 versus
155, P = 0.005). The paper therefore reports no WWOX-RUNX2 relationship and no response endpoint, although
its title promises both; the control tissue is never named; Figure 1c-d are unmatched fields. Survival
statistics are internally inconsistent: the caption gives a median OS of 45 months, the curve crosses 50% at
about 8 months, and it plateaus at about 29% (two survivors) while Table 1 and the text give six deaths
of seven. The authors themselves call the WWOX result a pilot-power negative.

**What it does not support.** A WWOX role in Ewing sarcoma; a WWOX-RUNX2 inverse relation in this tissue;
any prognostic statement for WWOX or RUNX2 (no stratified survival); any bone-metabolism, calcium or vitamin D
content. It cannot be cited for the RUNX2 arm of the Wwox-null bone phenotype beyond "no WWOX change at n = 7".

**Effect on the model.** None; the bone axis stays "Wwox-null osteoblast and RUNX2 arm already read; no
supplementation or bone-metabolism datum in humans". Class MINOR.

---

## 4. PMID 37686047 — Rushing 2023, NCI-60 multi-omics and sensitivity to alkylating agents (WWOX-direct only as a CNV gene-list line; W2 one-carbon/amino-acid axis) — receipt FTR-20261020-37686047-01

**What it MEASURES.** System: 58 NCI-60 human cancer cell lines, public baseline metabolomics,
transcriptomics, proteomics and SNP-array copy-number intensities against the rank-ordered sensitivity to 51
alkylating agents; Q1 (most sensitive) versus Q4 (most resistant), about 14-15 lines each. WWOX is not
perturbed or measured as a function; it is one of 15 genes with more than 5 DIABLO-selected CNV markers.

**Question and answer.** Is the WWOX line more than a gene-list sentence, and is a metabolic readout tied to it?
No metabolic readout is tied to WWOX. The paper's metabolic result is purine metabolism (P = 0.0054 with
transcripts, 0.012 with proteins, uncorrected), and its WWOX-metabolism sentence is a literature citation.
What the supplement adds, and the main text omits: (1) the "decreased" call rests on 22 CNV markers with a
mean of about -0.17 in Q4 against +0.19 in Q1 (Table S7), a quartile-mean shift; (2) the transcript does not
follow: five WWOX probes, Q4/Q1 fold change 0.73-0.95, smallest P about 0.074, DIABLO loading -0.34 below the
0.6 cutoff (Tables S2, S5); (3) in the CREAMMIST data WWOX expression correlates weakly and negatively with IC50
for five alkylating agents (rho -0.20 to -0.25; Table S3), same direction as the copy number (more WWOX, more
sensitive). The DIABLO separation of the two quartiles is a supervised fit on about 29 samples and says little
by itself (INFERENCE).

**What it does not support.** A role of WWOX in cancer metabolism or in alkylating-agent resistance mechanism;
any one-carbon, folate, or amino-acid statement about WWOX; any neural content.

**Effect on the model.** One-carbon and amino-acid axes stay "no WWOX evidence"; the paper adds a
weak, unreplicated, tumour-line association of WWOX copy number and expression with alkylator sensitivity.
Class MINOR.

---

## 5. PMID 22842668 — Płuciennik 2012, genetic alterations of WWOX in Wilms' tumour (WWOX-direct, W2 kidney axis; tumour genetics) — receipt FTR-20261020-22842668-01

**What it MEASURES.** System: 23 resected Wilms' tumours from children (Lodz, Wroclaw). Readouts: WWOX and ten other
transcripts by (semi-nested) real-time PCR against a reference RNA, two 16q microsatellites for LOH,
promoter methylation by a restriction-digestion qPCR assay, a six-tumour western blot. No normal-kidney
comparator, no function, no renal or metabolic measurement.

**Question and answer.** What is measured and is there renal or metabolic content? Alterations: LOH,
promoter methylation, expression. None of the readouts is physiological. Corrections the text-level reading would
miss: the "LOH in 30.4%" is the observed hemizygosity at the intron-8 marker; Table I subtracts a population
homozygosity of 26% and gives a predicted LOH of 4.4% (about one tumour) at intron 8 and 0 at intron 1, so the
statement that LOH "did not influence" expression concerns a very small group. Methylation, seen in about 3 and 2
tumours, goes with lower expression (15.9 vs 4.0, P = 0.036; 14.9 vs 0.8, P = 0.0037). The expression
assay is a 77-cycle semi-nested PCR; the six-sample blot (Figure 1) does not show the 40-280-fold mRNA
difference at protein level. Table II (BCL2, BCL2/BAX, TP73, ERBB4 JM-a, EGFR positive; both cyclins -0.66 with an
identical printed coefficient and P value) is co-expression in tumour with no correction for eleven genes.

**What it does not support.** Any kidney-function, hormonal-metabolism or biochemical statement (the only metabolism
word is an Introduction citation); a clinical or prognostic WWOX effect (no correlation with age, stage or risk);
loss of heterozygosity as a mechanism at this sample size.

**Effect on the model.** Kidney axis stays "tumour genetics only, no renal-function evidence". Class MINOR.

---

## 6. PMID 29899766 — Mastrangelo 2018, treatable inborn errors of metabolism causing epilepsy (SUBSTITUTE, NOT WWOX EVIDENCE; W2 umbrella cofactor axis) — receipt FTR-20261020-29899766-01

**What it MEASURES.** Nothing: a narrative review of eight disease classes (pyridoxine-dependent epilepsies,
cerebral folate deficiency, serine disorders, biotinidase deficiency, creatine disorders, molybdenum cofactor
deficiency, GLUT1 deficiency) with six pathway schematics and a work-up checklist (Table 1, an image). No WWOX
occurrence in the body.

**Question and answer (screening logic).** A DEE work-up should rule out, by level: first-level blood
count, gases, glucose, liver tests, ammonia, uric acid and thyroid function; therapeutic trials of pyridoxine,
pyridoxal phosphate or folinic acid in newborns and infants; lactate, pyruvate, guanidinoacetate, creatine/creatinine,
pterins and a CSF glucose ratio in epilepsy with movement disorder; acylcarnitines, amino acids, folates and
homocysteine in multi-organ cases. What a negative screen can say is stated by the review itself: a
lacking pyridoxine response "has no diagnostic value" and does not exclude the disease; the folate disease is
defined by a CSF 5-methyltetrahydrofolate measurement without peripheral depletion, so blood folate cannot
answer it; and treatment effect is better on seizures and motor signs than on cognition.

**What it does not support.** Any statement about WWOX, a cofactor requirement of a WWOX-related DEE, or a
benefit of any supplement in WWOX loss. A negative cofactor screen can exclude a treatable cause in a case; it
says nothing about WWOX biology, and a positive response in a WWOX case would be a coincident diagnosis
or a modifier, not evidence about WWOX.

**Effect on the model.** Defines the exclusion work-up for any WWOX-DEE case series in class terms; no claim
touched. Class MINOR.

---

## 7. PMID 36980111 — Mastrangelo 2023, epilepsy phenotypes of vitamin B6-dependent diseases, systematic review (SUBSTITUTE, NOT WWOX EVIDENCE; W2 vitamin B6 axis) — receipt FTR-20261020-36980111-01

**What it MEASURES.** A registered systematic review of published paediatric cases with a molecular diagnosis of a
B6-dependent epilepsy: 497 patients from 128 papers (62 ALDH7A1, 28 PNPO, 17 PLPBP, 1, 14 and 6 for the rest), mostly
case reports. Readouts: seizure types, EEG, MRI, therapy and developmental outcome as published. No WWOX.

**Question and answer (what a pyridoxine response looks like).** Of 312 patients given pyridoxine, 173 became seizure-free and 38
had a significant reduction (about 55% and 12%); pyridoxal phosphate gave complete control in only five patients; the
modal phenotype is neonatal-onset (67.8%) generalised or focal motor seizures with burst suppression. The response is a
seizure endpoint: the Background says it can be incomplete or delayed up to three weeks and omits other manifestations; an EEG
response to intravenous pyridoxine is no longer a diagnostic criterion; neurocognitive tests exist for 50 of 497
patients; detailed follow-up seizure types for 18.7%; there is no comparator. The supplement's responsiveness column is
blank in about 175 of 288 ALDH7A1-labelled rows (script count; some rows are column-shifted), and Table 2's PLP-responder
cells (12 and 2) do not obviously match the text's five.

**What it does not support.** Any WWOX statement; a B6 requirement or response in WWOX loss; neurocognitive benefit
of supplementation (explicitly not drawable). A response in a WWOX case would show a co-diagnosis or a seizure modifier
at most, and a non-response excludes nothing.

**Effect on the model.** Supplies the trial-interpretation logic (seizure endpoint only, delayed response possible, EEG
not a criterion) for any future WWOX B6 observation. Class MINOR.

---

## 8. PMID 38978529 — Girgis 2024, cerebral folate transport deficiency in two cases with intractable myoclonic epilepsy (SUBSTITUTE, NOT WWOX EVIDENCE; W2 folate axis) — receipt FTR-20261020-38978529-01

**What it MEASURES.** Two unrelated Egyptian girls (8 and 12 years) with myoclonic-atonic drop attacks, global
developmental delay, hypotonia and ataxia, exome-diagnosed with homozygous FOLR1 variants; MRI, CT, EEG, routine
metabolic screen; folinic acid by intramuscular injection. No WWOX.

**Question and answer (what it looks like in practice, and which readout defines it).** A school-age onset of
myoclonic-atonic seizures after a delay already present, cerebellar atrophy, bilateral basal-ganglia and
periventricular calcifications on CT, normal routine metabolic screen (ammonia, lactate, acylcarnitines, organic
acids, CSF glucose, protein and lactate, a normal CSF-to-blood glucose ratio), and a partial response to folinic acid
(no seizure counts given). The defining readout, CSF 5-methyltetrahydrofolate, was **not measured** in either
patient ("the test is not present in our country"), so the report diagnoses by genotype and cannot show the
CSF readout; the Discussion supplies the reference thresholds from the literature (below 5 nmol/L typical, 11 the
highest reported). Reporting issues: case 1's variant is called nonsense but written p.R128W, an Arg-to-Trp
(missense) change by the usual notation (INFERENCE from the notation); case 2 text has transcription errors. The
Discussion's class caution stands: folic acid competes at the receptor and is contraindicated.

**What it does not support.** Any WWOX statement; the CSF folate level in these patients; the size of the
response to folinic acid; that a cerebral folate readout exists for a WWOX model.

**Effect on the model.** The folate axis stays a pure substitute with no WWOX datum: this report adds that a
normal routine screen does not exclude the disease and that the confirmatory CSF assay may be unavailable.
Class MINOR.

---

## 9. Blind locator audit and the wave's balance sheet

One auditor with no history received six load-bearing triples (Friemel Figure 3A against Table 1; Sharma
Kaplan-Meier against the caption and table; Rushing Tables S2, S3, S7; Płuciennik Table I; Chen Figure 6B; Girgis
cases). Verdicts: six SUPPORTED. Two precision notes taken, not edited into the manifests (they change no
claim): the "two survivors" reading of the Sharma plateau is loose (the curve implies about 2 of 7; the contradiction with six deaths
holds either way), and the intron-8 wording of the Płuciennik LOH rate comes from the Discussion while the Results
sentence names only the marker D16S3096. No baseline claim is narrowed, so the audit was run on the brief's instruction, not a
mandatory trigger.

| PMID | Role | Depth | Receipt | Manifest |
|---|---|---|---|---|
| 25779665 | WWOX-direct, temperature | partial | FTR-20261020-25779665-01 | PASS 0 gaps |
| 36587184 | WWOX-direct, liver | partial | FTR-20261020-36587184-01 | PASS 0 gaps |
| 41141138 | WWOX-direct, bone | partial | FTR-20261020-41141138-01 | PASS 0 gaps |
| 37686047 | WWOX CNV line, one-carbon | partial | FTR-20261020-37686047-01 | PASS 0 gaps |
| 22842668 | WWOX-direct, kidney | partial | FTR-20261020-22842668-01 | PASS 0 gaps |
| 29899766 | SUBSTITUTE | partial | FTR-20261020-29899766-01 | PASS 0 gaps |
| 36980111 | SUBSTITUTE | partial | FTR-20261020-36980111-01 | PASS 0 gaps |
| 38978529 | SUBSTITUTE | partial | FTR-20261020-38978529-01 | PASS 0 gaps |

All depths are partial because references are unread. 29481666 was skipped as instructed.
