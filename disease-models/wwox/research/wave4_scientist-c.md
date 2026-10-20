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
