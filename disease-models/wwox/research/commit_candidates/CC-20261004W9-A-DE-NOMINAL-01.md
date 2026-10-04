# COMMIT CANDIDATE — CC-20261004W9-A-DE-NOMINAL-01 — PMID 41345172: the WWOX deletion's drug-response association is nominal even within the gene; the record's gnomAD figures are confirmed on the same bytes

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist`, Scientist A of intake wave 9, 2026-10-04.
**Change class:** **MINOR.** Two clarifying replacements in one registry record (`PAPER 209`); `CLAIM 032`
is **not edited**. Provisional anchors. `context_policy: QUESTION_DRIVEN`. **Not medical advice.**

---

## 1 · What the owed sections show

- Supplementary Table 4 (re-analysed in full): 16,980 data rows, 14,283 unique; SANAD drug-response rows cover
  559 distinct WWOX probe locations and 1,609 (mode, location) pairs. Best drug-response p 1.68e-4 (LRR
  univariate, inside the deletion) versus a Bonferroni threshold of 0.05 / 559 = 8.9e-5 (3.1e-5 over the
  pairs); best genotype-based p 4.92e-3. The paper's correction adjusts for phenotype correlation (M not
  printed). So the association is nominal before any genome-wide correction, and fails a within-gene one.
- Table 13: "drug response" is binary 12-month remission.
- Supplementary Figure 19 (viewed): gnomAD DEL_16_156229, intronic, 78371638-78384898, 7355 / 21694 = 0.3390
  (recomputed), 1447 homozygotes; the multi-allelic record spans 78371850-78385000 at AF 0.545. The paper's
  region (78,371,638-78,385,000) joins both and states 34 % and 54 %.
- Supplementary Figure 6 (viewed): brain-region heatmaps of WWOX exon expression against CNV genotype carry no
  printed values or direction and the text makes no claim from them.

## 2 · Records gated and verdicts

| record | wording | verdict |
|---|---|---|
| `CLAIM 032` boundary ("a common intronic polymorphism, not a dosage datum"; gnomAD AF 0.339, 1447 homozygotes) | | **Holds, confirmed by measurement**: the figures are on the supplementary page and recompute. The boundary is, if anything, stronger (the nominal p fails a within-gene correction). Not edited. |
| `PAPER 209` Role | "the deletion's own best p is nominal (drug response 1.68e-4, Supplementary Table 4)" | **Sharpened**, wording holds. |
| `PAPER 209` Genotype/model | interval "78,371,638-78,385,000" | **Holds as the paper's printed region**; clarified that it joins two gnomAD entries. |
| `FT-181`/`CLAIM 032` other sources | | Unaffected. |

## 3 · Ops (provisional; each `old` measured unique in its record)

### 3.1 · `disease-models/wwox/registries/paper_registry_current.md`, record `PAPER 209`

| field | value |
|---|---|
| op | `replace` |
| old | `the deletion's own best p is nominal (drug response 1.68e-4, Supplementary Table 4)` |
| new | `the deletion's own best p is nominal (drug response 1.68e-4, Supplementary Table 4; the table covers 559 distinct WWOX probe locations, whose Bonferroni threshold of about 8.9e-5 it does not reach, wave-9 measurement; the paper's stated correction adjusts for phenotype correlation and prints no M; "drug response" is binary 12-month remission, Supplementary Table 13)` |

| field | value |
|---|---|
| op | `replace` |
| old | `common intronic deletion chr16:78,371,638-78,385,000 (GRCh37)` |
| new | `common intronic deletion chr16:78,371,638-78,385,000 (GRCh37; the paper's region joins the gnomAD deletion DEL_16_156229, 78,371,638-78,384,898, and a multi-allelic record ending at 78,385,000, wave-9 panel reading)` |

## 4 · Verification before propagation

`deepdive_manifest.py --pmid 41345172 --verify-artifacts --require-current-schema` PASS at this commit
(two panel-only coordinate warnings, as for the existing panel entry). Receipt `FTR-20261004-41345172-02`.

### LOCATOR TRIPLES FOR BLIND AUDIT

- (The paper's correction adjusts for phenotype-matrix correlation | we used a modified Šidák method for calculating the net effective number of tests (M) based on the degree of correlation structure in the phenotype matrix | PMID 41345172, Methods, multiple-testing correction)
- (The paper's own region and frequencies | We chose the WWOX intronic deletions as reported by the gnomAD database in the region chr16:78,371,638-78,385,000 (GRCh37/hg19) which has a deletion and a multi-CNV with allele frequency of 34% to 54% respectively | PMID 41345172, Methods, CNV pipeline fine-tuning)
- (Drug response is a binary remission | Time to 12 month remission; 1= achieved 12 month remission; 0=did not achieve 12 month remission | PMID 41345172, Supplementary Table 13, drug_response row)
- (Table 4 is the WWOX association table for drug response | Association results for the drug-response phenotype in SANAD for CNV genotypes and LRR using univariate and multivariate models | PMID 41345172, Supplementary Table 4, sheet SANAD caption)

## BATCH DISPOSITION — `BATCH_20261004_003` (2026-10-04, ACTOR_ID `scientist`, Scientist M), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** `PROPAGATED` (MINOR, WM_v7.15 → WM_v7.16).

**Surfaces written:** paper_registry_current.md

Both ops applied as declared, on `PAPER 209`. `CLAIM 032` is **not edited**: its boundary statement (*a common intronic polymorphism, not a dosage datum*) is confirmed by the measurement rather than narrowed by it, and the candidate asked for no edit there. Sampled, not audited blind: the ops add arithmetic and coordinate provenance to an existing record and assert no new proposition.

**Not medical advice.**
