# Intake wave 13 (2026-10-04) — Scientist A, Group A: re-read aimed at negatives

**ACTOR_ID** `scientist` · branch `task/sci-A-20261004w13` · `context_policy: QUESTION_DRIVEN` throughout
(every paper here was already held with a receipt; the wave question, the prior receipts and the landed
records were deliberately in hand before the owed surfaces were opened).

**Not medical advice.** Class level only: allele class × zygosity × phenotype band. No parent-of-origin
wording. Genotype caution: P47T ≠ Q230P ≠ G372R ≠ A141T ≠ P252A; a heterozygote is neither a demonstrated
negative nor a positive for haploinsufficiency; nothing transfers across alleles. Patients are counted
once — the five papers share no patient (four are not case reports at all; PMID 29390993 and PMID 24949445
describe different cohorts in different countries with different alleles and no overlapping genotype).

## Assigned question
> What do the owed tables, panels and appendices add to or limit in the carrier observation of `CLAIM 032`
> and in the allele-level architecture claims?

**Answer.** They *confirm the carrier observation by measurement* and they *break two landed negatives*.
`CLAIM 032` (b) rests on table cells, not on flattening artefacts, and every negative behind it survives a
search of every surface the paper has. The architecture records do not come through intact: a dismissal
headline and a discovery-ledger sentence both assert something the sources contradict, and a paper
registry record says a paper "never states" a fact that its own figure prints. Three of the five papers
needed artefacts that were **not in the corpus at all** before this wave — the thing the selection called
"owed" was in two cases not held.

## Per paper

### PMID 29390993 — Rim 2018, 172-gene panel in 74 intractable early-onset epilepsies
**Verdict: INGEST (re-read complete for the owed surface).** Owed: five `table-wrap` tables "read through
flattened JATS text". **The premise is wrong twice**: the ledger's single receipt is
`complete_fulltext_read`, not partial, and the JATS carries **3** `table-wrap` elements; the five
supplementary tables are xlsx sheets already read through a declared cell dump.

Tables 1–3 re-extracted from the `<tr>`/`<td>` markup. The two WWOX rows give, cell by cell, the
transcript, `c.1060C > T` / `p.Gln354Ter` / Heterozygosity / Pathogenic / `PVS1, PM2, PM3, PP4`, and
`exon 6–8 duplication` / `_` / Heterozygosity / Likely pathogenic / `PM2, PM3, PP4, PP5`, with the two
alleles attributed to different parents in a column of its own. **Identical to the flattened-text
locators: no artefact.** Tables 2–3 carry no WWOX row.

*FIND-X, over body + references + Tables 1–3 cell-wise + Figures 1–2 + sheets S1–S5:* "parents
asymptomatic by inclusion criterion, not by a reported examination" **holds**; "NMD escape expected; not
addressed by the source" **holds** (zero hits for NMD / nonsense-mediated / decay / transcript / mRNA /
RT-PCR; the 149 `western` hits are reference-list markup attributes); "no RNA, protein or functional test"
**holds**; "the paper does not place the stop in the last exon" **holds** — that is LEGEND's boundary map.

*Measured vs predicted:* nonsense allele — sequence call, Sanger and parental testing measured, consequence
**predicted** (PVS1), matrix none. Duplication — copy number measured by relative depth and, per Methods,
MLPA; tandem orientation, frame, transcript and protein **not measured**. Neither allele is the reference
genotype's class.

**Candidate:** `CC-20261004W13-A-CARRIERS-01` (MINOR) — `CLAIM 032` (b) confirmed, with one attribution
correction ("last-exon" is LEGEND's computation, not the source).

### PMID 24949445 — Szymańska 2014, seven paediatric encephalopathies
**Verdict: INGEST (re-read complete).** Premise wrong twice again: one `complete_fulltext_read` receipt,
and **4** `table-wrap` elements. The article genuinely has no figures and no supplement
(`pmc-prop-has-supplement: no`, no `fig`, no `supplementary-material`).

The interval behind `DIS-022` is a **Table 4 cell**, on an assembly the caption states. Re-mapped
independently: NCBI36 16:77,445,915–78,190,209 → GRCh37 16:78,888,414–79,632,708, which overlaps
**358,151 bp of WWOX** (distal intron 8 + exon 9); exon 8 lies 421,765 bp outside, beyond the stated
maximum size. So **`DIS-022`'s headline — *"the interval does not contain the gene"* — is false as
worded**, while its body and its dismissal are right. A second phrase mis-paraphrases: the record says
epilepsy "normalised on valproate"; the cell says valproic acid gave a complete **EEG** normalisation.

*FIND-X:* no orthogonal confirmation of the gain, no WWOX/MAF expression, no breakpoint, orientation or
inheritance (the cell reads `Unknown`) — all **hold**.

**Candidate:** `CC-20261004W13-A-DOSEGAIN-01` (MINOR; the wave's headline false-negative find).

### PMID 39952983 — Kim 2025, WWOX intronic SNVs and sleep duration
**Verdict: INGEST (owed supplement now read).** Premise: "6 `table-wrap`" — the JATS has **3**; the other
two tables are in the DOCX. All four declared artefacts present and matching, so `PAPER 135`'s
"artefacts absent / manifest BLOCK" is a resolved historical note.

New declared artefacts: a cell-wise DOCX text layer and the two embedded images extracted byte for byte.
Both supplementary figures were inspected and their axes measured with a stdlib PNG decoder.

- Every Table 2 / Table 3 number carried by the landed records matches the cells.
- Bonferroni family recomputed from the two numbers it names: 0.0197/1.11e-7 = **177,477**;
  0.0364/2.05e-7 = **177,561** ⇒ ≈ 1.775 × 10⁵, **confirming** the landed "about 1.8e5".
- **Supplementary Fig. 1** (the panel the Results cite for p = 1.11 × 10⁻⁷): genome-wide maximum
  −log₁₀ p ≈ **5.5**; nothing reaches the 6.95 that value would plot at, and its caption names a
  different covariate set. `PREMISE: INFERENZA` — a different model, never declared.
- **Supplementary Fig. 2**: top observed ≈ 5.5 at expected ≈ 5.85 ⇒ ≈ 7 × 10⁵ plotted tests, not
  6.42 million.

*FIND-X:* "no human WWOX expression measured" **holds** (zero expression/eQTL/GTEx hits in the supplement);
"suggestive by the authors' own statement" **holds**. `LIT-0433`'s "Supplementary Figures 1-2 remain
unviewed and are not blocking" is **retired** — they were not inert.

**Candidate:** `CC-20261004W13-A-SLEEP-01` (MINOR). `DL-MECH-013`'s three constraints are confirmed by
measurement; no edit proposed to it.

### PMID 28763065 — Xia 2017, infant brain-volume GWAS
**Verdict: INGEST (owed appendices acquired and read).** The selection's "PRESENT (6/6)" is true of the
six *declared* artefacts — but the appendices it calls owed **were not among them and were not on disk**.
Supplementary Table 5 and Appendices 2–3 are separate PDFs the JATS lists with md5 digests; I acquired all
three from the Europe PMC `supplementaryFiles` archive for PMC5611727 (every md5 equal to the JATS
`suppdata-md5`). Their fonts carry no ToUnicode CMap, so they are read as **rendered pages only**.

**Answer to the wave question: there is no intron-8 regulatory signal in the appendix plot books.** They
hold WWOX expression trajectories **by age** (Appendix 2 page 4: postnatal above prenatal in 15 of 16
regions, hippocampus the exception at P 0.1055; Appendix 3 page 5: an annotated intron-8 exonic segment at
about zero). Nothing is stratified by genotype. Supplementary Figure 4 shows rs10514437 alone at
−log₁₀ p ≈ 7.8 with no other SNP in the window above ≈ 3 — **no LD-supported regional architecture**;
Supplementary Figure 7 shows **no minor homozygote**, so the association is carried by heterozygotes
only; the permutation empirical p is **8 × 10⁻⁸**, above the study's own 1.25 × 10⁻⁸ threshold.
Supplementary Table 8, cell-wise, confirms the direction: `0.03` is the **Fst** column, G (frequency 0.97)
is the common allele, so the **minor** allele goes with more white matter.

*FIND-X:* `PAPER 132`'s "no eQTL and no functional link" **holds** on every surface. `DL-MECH-107`'s "none
reports expression or function" is **false as worded** for this paper — it reports expression, just never
by genotype, so its `REVIVAL_TRIGGER` (2) still does not fire. Its coordinate "chr16 78.459 Mb" is
**GRCh38** and carries no build label; on GRCh37 the SNP is 16:78,492,860, 26,211 bp into intron 8.
`CLAIM 003` (hypomyelination, `consolidated baseline`) is **unaffected**: volume in the normal range is
not myelin content.

**Candidate:** `CC-20261004W13-A-INTRON8-01` (MINOR).

### PMID 17679088 — Zhang & Freudenreich 2007, FRA16D Flex1 in yeast
**Verdict: INGEST (owed supplement read; figures partially read).** The held artefact was the reader HTML
alone, so both owed surfaces had to be acquired: the six figure images from the PMC CDN blob URLs printed
in that HTML, and the deposited supplement through `pmc_pow_fetch.py` (proof-of-work solved, HTTP 200).

**The wave question is answered yes, and the landed negative is wrong as worded.** `PAPER 128` says the
paper "never states which WWOX intron or exon Flex1 lies in — absent from the body". The second half is
true: no body sentence and no supplement sentence gives an exon, intron or coordinate (`WWOX` occurs once
in the supplement). The first half is false: the Figure 2 legend says the panel carries the WWOX/FOR exon
track, and panel B's labelled boxes are **exon 8** and **exon 9**, with Flex4, Control, Flex1 and Flex5-p
drawn between them — Flex1 is published as lying in **intron 8**.

This unblocks the position `LEAD-C1` was missing (it remains blocked on Finnis 2005 for allele lengths) and
changes nothing else: every measurement is a yeast YAC breakage or fork-stalling rate, no WWOX transcript
or protein is measured, `T3 — OFF-AXIS` stands. It is **not** convergence with `DL-MECH-107`: intron 8 is
most of the gene, and a replication-barrier AT repeat is a different object from a reporter-tested
cis-regulatory element.

**Candidate:** `CC-20261004W13-A-FLEX1-01` (MINOR).

## What would change the model, and what would falsify this wave's conclusions
- **Would change it:** WWOX expression stratified by intron-8 genotype in human brain or neural tissue
  (fires `DL-MECH-107` trigger 2 — neither Xia nor Kim supplies it); an RNA or protein measurement of the
  Rim 2018 alleles (would settle NMD escape and the duplication's frame, both currently predicted only);
  Finnis 2005's AT-allele length distribution with a fragility or rearrangement readout (would move
  `LEAD-C1` from `IPOTESI` toward a covariate).
- **Would falsify this wave:** a surface I did not search that prints a parental examination for Rim 2018,
  a WWOX expression-by-genotype analysis anywhere in the Kim or Xia supplements, or a different gene track
  reading of Zhang Figure 2B (the single panel on which the FLEX1 correction rests — it is a labelled
  figure, so a second reader can settle it in one look).

## What was wrong in the assignment
1. "partial, 1 receipt" for PMID 29390993 and PMID 24949445 — both hold a `complete_fulltext_read` receipt.
2. Table counts: 5 claimed vs **3** actual (29390993), 5 vs **4** (24949445), 6 vs **3** (39952983).
3. "PRESENT (6/6)" for PMID 28763065 — true of the declared artefacts, but the appendices the row calls
   owed were **not declared and not on disk**; same for PMID 17679088, whose figures and supplement had to
   be acquired before the "owed" surfaces existed locally.
4. The rows are otherwise accurate, and the 0-ABSENT census for these five held.

## What remains owed, and why
| Paper | Surface still owed | Record waiting on it | Route |
|---|---|---|---|
| 29390993 | nothing | — | the article and its supplement are read in full |
| 24949445 | nothing | — | the article has no figures and no supplement |
| 39952983 | the 58-item reference list (never read item by item) | nothing; no proposition rests on it | mechanical enumeration from the JATS `ref-list` |
| 28763065 | Supplementary Figures 1–3, 5–6, 8–11 as images; the other 14 region pages of Appendix 3 (read by panel title only) | nothing — no WWOX locus appears in their captions | all artefacts are now on disk; render with `pdftoppm` / extract from the DOCX |
| 17679088 | Figures 1 (remaining panels), 3–6 and S1–S2 as images | nothing — the position question is answered by Figure 2B | images are on disk; **a model-safety classifier halted the inspection**, so a re-read needs a different reader or route, not a reworded prompt |

## Receipts prepared (not recorded)
`scratchpad/receipts_pending_w13/sciA_29390993_1.json` · `sciA_24949445_1.json` · `sciA_39952983_1.json` ·
`sciA_28763065_1.json` · `sciA_17679088_1.json`, each copied to
`~/legend-receipts-backup-20261004/receipts_pending_w13/`. All five dry-recorded clean (exit 0) against a
throwaway ledger **and** state-manifest copy taken from this branch; the live ledger and manifest were not
touched.
