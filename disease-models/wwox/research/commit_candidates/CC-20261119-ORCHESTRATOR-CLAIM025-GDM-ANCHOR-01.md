# COMMIT CANDIDATE — CC-20261119-ORCHESTRATOR-CLAIM025-GDM-ANCHOR-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (ADV-081 line, reading-debt follow-up) · **Date:** 2026-11-19
**Paper:** PMID 33520443 (Baryla et al. 2021, *PeerJ* 9:e10604; `PAPER 262`, `LIT-0560`)
**Receipt:** `FTR-20261019-33520443-01` · `partial_fulltext_read` (manifest: whole article read incl. Methods, both tables, all seven figures as images and Supplemental Information 1; NOT opened: Supplemental Information 2-12 and eleven raw qRT-PCR plate files)
**Target WM version:** no bump proposed. Nothing here reverses a consolidated baseline: `CLAIM 025` is `in observation`.
**Status:** PROPOSED — for the orchestrator's `BATCH_COMMIT`; the claim registry is NOT edited by this actor.

> Public, disease-level, de-identified. Nothing here is medical advice.

## 1 · Why this candidate exists
The six `CORPUS` placeholders restored by lint with `Identifier: PENDING` were examined one by one (`generation_it59_20261119/DEEP_DIVED_PLACEHOLDERS_IT59.md`). One of them, `CORPUS P191` ('WWOX/HIF1A axis in human non-tumoral GDM → CLAIM 025', tracking update 2026-04-17), is the only record that stands for the GDM statement of `CLAIM 025`; the claim's declared foundations (`PAPER 091` hepatic mouse, `PAPER 118` breast and ovarian TCGA, `PAPER 567` Drosophila) contain **no GDM paper**. The GDM paper is `PAPER 262` (Baryla 2021), read partially on 2026-10-19, with `Claim links: none`. So the GDM sentence of the claim is **anchored to a placeholder**, and the paper that carries it says something weaker than the claim.

## 2 · The claim's current sentences (verbatim, `claim_registry_current.md`, `CLAIM 025`)
* `Genotype/model relevance`: «studio su leucociti umani non tumorali (GDM); WWOX ridotto, HIF1A aumentato, ratio marcatamente ridotto».
* `Summary`, first sentences: «In human GDM leukocytes, WWOX is reduced, HIF1A is increased, and the WWOX/HIF1A ratio is markedly decreased. Lower ratio associates with increased expression of glycolytic genes and correlates with inflammatory and Wnt-related components.»

## 3 · What the paper says (verbatim snippets from `deepdive_manifests/PMID33520443.json`, `verbatim_locators.entries`, anchors given)
* Design (entry 1, Methods): «A total of 135 Caucasian pregnant women consisted of 37 women with normal glucose tolerance (NGT) and 98 women with GDM were enrolled»; third trimester; blood leukocyte mRNA by RT-qPCR; no neural or pancreatic tissue.
* WWOX (entry 3, Results, Gene expression studies): «There was also a tendency for lower leukocyte WWOX expression in the women with GDM vs the controls with NGT»; manifest note: p about 0.04 called a tendency, eleven genes compared, **no multiple-testing correction named** anywhere in the text (searched by term: zero hits). Figure 2A (entry 5): the WWOX boxplots of GDM and NGT overlap almost entirely; one asterisk.
* Fold changes (entry 4): «as evidenced by an 1.4- fold decrease for WWOX and a 3.8-fold increase for HIF1A in the diabetic patients»; ratio about 6.5-fold down by the stated folds. HIF1A: three asterisks (Fig 2B).
* HK2, a canonical HIF1A target, unchanged (entry 6): «the leukocyte HK2 transcript level remained unchanged between the two groups».
* Correlations (entries 7 to 9): in GDM WWOX and HIF1A are not correlated with each other (rho -0.05); WWOX does not correlate with HK2, PKM2 or SLC2A1; the strong correlations of the ratio with HIF1A and with glycolytic genes 'are the arithmetic of a ratio with HIF1A in its denominator' (manifest wording); in NGT WWOX correlates positively with PFK (0.30) and LDHA (0.32).
* Metabolic parameters (entry 10): in NGT more insulin and HOMA-IR go with HIGHER WWOX; in GDM neither WWOX nor the ratio correlates with any metabolic parameter. Postpartum (entry 15): WWOX about 2-fold higher than in the same women during GDM (8 and 12 paired women).
* Figure-versus-text: Figure 6C and 6E print statistics that differ from the running text (manifest note, entries 12 and 13).

## 4 · Proposed change (a rewording of one claim's first two sentences and one anchor; no status change)
1. **Anchor:** add `PAPER 262` (Baryla 2021; `partial_fulltext_read`) as the supporting record of the GDM sentence, with its depth stated; the claim's foundations then list a GDM paper.
2. **First sentence, proposed:** «In blood leukocytes of 98 third-trimester women with gestational diabetes against 37 with normal glucose tolerance, HIF1A transcript is increased (3.8-fold) and WWOX shows only a tendency to be lower (1.4-fold, p about 0.04, no multiple-testing correction named for eleven genes); the WWOX/HIF1A ratio is lower (about 6.5-fold) because of the HIF1A change (Baryla 2021, PAPER 262, partial read).»
3. **Second sentence, proposed:** replace «Lower ratio associates with increased expression of glycolytic genes and correlates with inflammatory and Wnt-related components» by: «The ratio's correlations with HIF1A and HIF1A-induced genes are those of a ratio with HIF1A in its denominator; WWOX itself is not correlated with HIF1A (rho -0.05) or with the glycolytic genes in GDM, HK2 is unchanged, and in normal pregnancy WWOX correlates positively with PFK and LDHA.»
4. `Genotype/model relevance` first clause: «WWOX ridotto» → «WWOX con sola tendenza a ridursi (p circa 0,04, nessuna correzione per test multipli)».
`Status` unchanged (`in observation`); `Type` unchanged; the cross-context boundaries already in the claim (hepatic occupancy at five promoters; direction not invariant across contexts) are untouched. No claim is created, reversed or promoted.

## 5 · Limits of this candidate
Partial read: Supplemental Information 2 to 12 and the raw plate files were not opened; the text XML named by the manifest (`files/fulltext/PMID33520443_Baryla2021_PMC7811782.xml`) is NOT recoverable by SHA-256 search of the real `files/` tree (figures and the supplementary docx are), so the quotes above rest on the manifest's verbatim snippets, which a locator audit has not re-opened against the bytes in this session; the proposed sentences should pass the `legend-locator-audit` check (blind triples proposition, quote, anchor) before the batch applies them, because the candidate narrows a claim.
