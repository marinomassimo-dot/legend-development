# Intake wave 13 (2026-10-04) — Scientist C: re-read of six sources for negatives

`context_policy: QUESTION_DRIVEN` — this is a re-read wave. Each paper's selection row named its
landed records and the negative being tested before the source was opened.
Reader: ACTOR_ID `scientist` (Scientist C), branch `task/sci-C-20261004w13`. **Not medical advice.**
Class-level only. No individual-level record appears here.

Group question: what do the owed panels and supplements add to, or limit in, the mechanism and
biomarker layer? That layer is the rescue-readout set behind CLAIM 014, the three rejected biomarker
families, and the HIF1α / phospho-code arcs.

Method: rule 46 (FIND-X). Before a negative is carried or retired, every surface of the paper is
enumerated and searched, and the surfaces that were unavailable are named.

---

## 1 · PMID 31543760 — Kośla 2019, hNPC WWOX knockdown

* **Verdict:** INGEST (re-read, supplement). Receipt `sciC_31543760_1.json` →
  `FTR-20261004-31543760-04`, `partial_fulltext_read`.
* **Premise check:** the row's "all 11 figure panels present only as stripped captions" is stale. The
  panels have been on disk and inspected since 2026-10-02. What was owed was Supplementary Tables 1–3
  and Supplementary Figures S3–S5.
* **New against held:** Supplementary Table 3 has **108** gene-set rows; the body says 109. Table 2
  has 44, which matches. S3 and S5 carry no WWOX node and no printed value. S4 has no text layer, and
  its labels were not legible at the resolution rendered.
* **FIND-X:** the knockdown-depth negative (DL-METH-114) **survives** on every surface; the declared
  densitometry has no printed result. The claim that no surface measures migration, layering, glial
  development or a prenatal phenotype **survives**. That narrows CLAIM 014's evidence boundary, which
  says the prenatal component "rests on Iacomino and Kośla".
* **Candidate:** `CC-20261004W13-C-CLAIM014-SCOPE-01` — **MAJOR**, seven blind-audit triples, dry
  run executed.
* **Records:** CLAIM 014 → narrows. DL-METH-114 → holds. PAPER 022 / LIT-0024 → hold.
  FT-005/020/057 → unaffected.
* **Transfer limit:** this is an shRNA knockdown of unquantified depth in H9-derived progenitors. It
  is not a biallelic null and not a missense allele, and it says nothing about any allele class.

## 2 · PMID 37897534 — Cheng 2023, Wwox-null MEF senescence escape

* **Verdict:** INGEST (re-read, panels and supplement). Receipt `sciC_37897534_1.json` →
  `FTR-20261004-37897534-02`, `partial_fulltext_read`.
* **Acquired:** seven figures and the 16-page supplement, from the PMC OA bucket (CC BY).
* **🔴 STOP_LOG:** the inspection of Figure 6 was **halted by a model safety classifier**. Per rules
  13/21 it was not retried and is recorded as **not read**. Figure 6 carries the microsatellite and NAC
  panels, so DIS-029's statements about them are unverified on the panel. Figures 3, 4, 5 and 7 were not
  inspected as images either.
* **New against held (Figs 1d and 2):**
  * Every comparison is heterozygote versus null.
  * Nothing differs at early passage.
  * γH2AX: about 20.5 % vs 35.5 % at passages 20–30. Passage alone raises the heterozygote about
    4.6-fold.
  * SA-β-gal **falls** with loss.
  * p27 mRNA is N.S. at both passages.
  * Knockdown arm: shRNA in HEK293T and in primary human skin fibroblasts (S3–S4).
* **FIND-X:** no surface read carries a WWOX re-expression, wild-type γH2AX or in vivo arm.
* **Candidate:** `CC-20261004W13-C-SENESCENCE-PANELS-01` — **MINOR**. DIS-028's rejection holds and is
  qualified; DIS-029's premise "All four respond" is corrected. Both dry runs were executed.
* **Transfer limit:** a constitutive mouse null in embryonic fibroblasts after 20–30 serial passages.
  It is not neural, not in vivo, and models no missense allele.
