# ADV-292 increment 2: repository sentences put to the second reader (SCI, 2026-11-26)

Dispatch: `legend-delegate`, model sonnet, effort high stated in the prompt. The reader sees copies of the held source files for five records (folders F to J) and the verbatim repository sentences below, not the first reader's conclusions.

Each sentence is taken verbatim from a research repository that cites the paper in the named folder (the wording may name the paper by its first author, by PMID, or not at all). For EACH sentence, check it against that folder only, and give a verdict:
- MUST CHANGE: some factual part is wrong or unsupported as written (say which words, what the source shows, and a corrected wording);
- ADD: nothing is wrong, but a window, dose, species, unit or evidence level is missing and a reader would be misled without it (say what);
- STANDS: supported as written.
Be strict and look for errors; do not assume the sentences are right or wrong. Check supplements, figures and tables, not only the text. Quote the panel, row or sentence you rely on. Where a sentence cites other papers or other records of this repository (paper numbers, claim numbers), judge only what rests on the folder named for it.

## S6a (folder F)
IT32 reading of neural precedents: a catalytic-domain mutant of HDAC5 (two cysteines) lost deacetylase activity in vitro and abolished the effect of nuclear HDAC5 on one transcript and on a behaviour in rat nucleus accumbens (PMID 39923817, full text; no SLC2A1 or glucose readout, and loss of binding to another factor is not excluded), so the earlier statement that no neural catalytic arm exists is out of date  [A research-repository table cell about neural precedents; judge what it says about the paper in folder F.]

## S6b (folder F)
Conditional hypothesis: the edge has one muscle origin read at abstract level and the compound side is compiled data; a catalytic-domain mutant of HDAC5 exists in rat neurons for other outputs (PMID 39923817) but none reads SLC2A1 in a human neural cell (no ranked unit, so no evaluation depth applies: this is not a depth of zero)  [Another cell of the same table; judge only what it says about the paper in folder F.]

## S7a (folder G)
**Role:** **Not an independent patient (DATO):** the paper's own Table 1 records its WWOX case as *«Reported as Patient 11 (Table S1) in case series in Piard et al»*, i.e. Patient 11 of [[paper_registry_current#PAPER 117]], and the genotype matches that paper's Supplementary Table 1. **Count once.** The in-frame exons 6-8 deletion is coded with a null criterion (`PVS1, PM2, PM3`) and **no RNA or protein was measured** — a rule, not a measurement. See `CC-20261004W8-A-PATIENT-OVERLAP-01` and `CC-20261004W8-A-MEASURED-01`.

## S7b (folder G)
**Genotype/model:** in-frame deletion of exons 6-8 + `c.705dup p.(His236fs)`; DNA only
**Model/species:** human — DNA only

## S7c (folder G, a claim paragraph; PAPER 218 is the paper in folder G, PAPER 219 is another paper)
(c) [[paper_registry_current#PAPER 218]] (= Piard 2019 Patient 11, counted once) and [[paper_registry_current#PAPER 219]]: an in-frame exons 6-8 deletion and an exon-5 deletion are coded `PVS1` (null) with **no RNA and no protein measured**. A missense allele in trans does not by itself mean detectable protein, and an in-frame deletion coded null is a **rule, not a measurement** — which is exactly what riserva (1) says. 🔴 ⚠️ A third amendment: `c.517-1G>A` is labelled an **intron-5 acceptor** allele nowhere in its source — the supplementary row types it *«Exonic or near-exon variant»* and prints no intron number, so the intron-5 label is **this repository's derivation from the WWOX exon map** (`INFERENZA`) and is quoted for nothing. `PREMISE: DATO` (one blot and one PCR, both qualitative) + `PREMISE: INFERENZA` (the classification).   [Judge only what concerns PAPER 218 (the in-frame exons 6-8 deletion).]

## S8a (folder H)
**Role:** Both consequences are **predicted by rule** (`PVS1, PM2, PM3, PP3`) with **no RNA and no protein assay**. An allele coded null without a measurement is a classification. See the dossier and `CC-20261004W8-A-MEASURED-01`.

## S8b (folder H)
**Genotype/model:** `c.517-1G>A` + single-exon deletion spanning exon 5; trio-phased
**Transferability:** T3 — an **intron-5** acceptor allele. 🔴 `c.517-1G>A` is **not** the `c.517-2A>G` allele of [[paper_registry_current#PAPER 039]] and **not** the reference genotype's acceptor allele; a shared position class is not a shared allele
**Model/species:** human — DNA only, trio-phased

## S8c (folder H, a claim paragraph; PAPER 219 is the paper in folder H, PAPER 218 is another paper)
(c) [[paper_registry_current#PAPER 218]] (= Piard 2019 Patient 11, counted once) and [[paper_registry_current#PAPER 219]]: an in-frame exons 6-8 deletion and an exon-5 deletion are coded `PVS1` (null) with **no RNA and no protein measured**. A missense allele in trans does not by itself mean detectable protein, and an in-frame deletion coded null is a **rule, not a measurement** — which is exactly what riserva (1) says. 🔴 ⚠️ A third amendment: `c.517-1G>A` is labelled an **intron-5 acceptor** allele nowhere in its source — the supplementary row types it *«Exonic or near-exon variant»* and prints no intron number, so the intron-5 label is **this repository's derivation from the WWOX exon map** (`INFERENZA`) and is quoted for nothing. `PREMISE: DATO` (one blot and one PCR, both qualitative) + `PREMISE: INFERENZA` (the classification).   [Judge only what concerns PAPER 219 (the exon-5 deletion and c.517-1G>A).]

## S9 (folder I)
non-T-type routes of ethosuximide are reported in non-WWOX systems (GIRK inhibition, PMID 37275776; broad-band cortical suppression, PMID 42536722; FOXO-pathway rescue in worms, PMID 36282524 and its primary PMID 26419537, which carries a wild-type arm with no effect and a direct test that loss of the worm T-type channel does not remove the benefit)  [Only the clause about FOXO-pathway rescue in worms and the primary PMID 26419537 rests on the paper in folder I; the other items concern other papers.]

## S10 (folder J)
an APP/PS1 line (PMID 31781019) shows same-direction effects in both genotypes for the spike classes present in both  [Judge only the clause about the APP/PS1 line.]

- For S10 note: recompute any direction or ratio you rely on from the per-mouse supplementary table over ALL rows (all mice, all sessions) and say which mice you included or excluded and why.
