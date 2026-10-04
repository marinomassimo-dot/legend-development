# COMMIT CANDIDATE — CC-20261004W9-A-KHADIJA-PANELS-01 — PMID 42807679: the WWOX-bearing 16q23q24 deletion is evidenced by one table row only; no profile, karyotype, FISH or imaging panel shows it

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist`, Scientist A of intake wave 9, 2026-10-04.
**Change class:** **MINOR.** One clarifying replacement in one registry record. `CLAIM 032` is **not edited**:
the panels neither fire nor refute its trigger. Provisional anchors. `context_policy: QUESTION_DRIVEN`.
**Not medical advice.** Figure 2 (patient photographs) was not opened.

---

## 1 · What the owed panels show

- Figure 6 (array-CGH and MLPA montage): 14 labelled panels, none for the 16q deletion; Figure 4 karyotypes
  are three other patients; Figure 5 FISH images are seven other patients. The text calls the profiles
  representative. The deletion's evidence in the paper is its Table 3 row (hg18 interval, de novo,
  pathogenic classification) and nothing else.
- No figure shows brain imaging; the callosal phenotype is a table cell. Figure 3B marks one chromosome 16
  long-arm pathogenic or likely pathogenic CNV, no breakpoints.
- Arithmetic: 10 / 54 = 18.5 %; 16 / 54 = 29.6 %; 4 / 107 = 3.7 %; interval 87,891,103 - 74,718,513 =
  13,172,590 bp. The supplement is a STROBE checklist.

## 2 · Records gated and verdicts

| record | wording | verdict |
|---|---|---|
| `CLAIM 032` third heterozygous observation | "karyotype and array-CGH (hg18); inheritance" examined; "Not a dosage datum either way" | **Holds, unaffected.** The ~13 Mb size remains derived from the printed interval (recomputed 13.17 Mb). The panels add that no image of the deletion is published, which narrows nothing the claim states. |
| `PAPER 208` Role | | **Clarified** by the op below. |

## 3 · Ops (provisional; `old` measured unique in its record)

### 3.1 · `disease-models/wwox/registries/paper_registry_current.md`, record `PAPER 208`

| field | value |
|---|---|
| op | `replace` |
| old | `Cannot bear on the Tabarki 2015 overlap (that report is a homozygous sequence allele).` |
| new | `Cannot bear on the Tabarki 2015 overlap (that report is a homozygous sequence allele). Wave-9 panel reading: the deletion is evidenced only by its Table 3 row; Figures 3-6 carry no array-CGH profile, karyotype or FISH image for it (Figure 6 is a representative montage without it; Figure 3B marks a chromosome 16 long-arm pathogenic CNV), and the paper contains no brain-imaging figure. Figure 2 (patient photographs) was not opened.` |

## 4 · Verification before propagation

`deepdive_manifest.py --pmid 42807679 --verify-artifacts --require-current-schema` PASS at this commit.
Receipt `FTR-20261004-42807679-02`.

### LOCATOR TRIPLES FOR BLIND AUDIT

- (Profiles shown are described as representative | Representative array-CGH profiles are shown in Figure 6 | PMID 42807679, Results, array-CGH paragraph)
- (Array-CGH yield | pathogenic or likely pathogenic CNVs were identified in 10 patients, corresponding to a diagnostic yield of 18.5% (10/54) | PMID 42807679, Results, array-CGH paragraph)

## BATCH DISPOSITION — `BATCH_20261004_003` (2026-10-04, ACTOR_ID `scientist`, Scientist M), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** `PROPAGATED` (MINOR, WM_v7.15 → WM_v7.16).

**Surfaces written:** paper_registry_current.md

The single op applied, **amended at source after the blind audit**. The candidate's *«Figure 6 is a representative montage without it»* was replaced by what the artefact prints: the montage is array-CGH **and MLPA**, it is called *representative* **only in the running text and not in its own caption**, its panels include variants of uncertain significance, one panel is not array-CGH at all, and **two of the ten pathogenic or likely pathogenic carriers have no panel**. The landed text also carries the recomputed arithmetic and the fact that the 54 tested are a **selected** subset of the cohort, which the audit supplied. **Blind locator audit: 2 triples, 2/2 SUPPORTED, 0 NOT_SUPPORTED, 0 UNVERIFIABLE** — one with the scope caveat just described. `CLAIM 032` is **not edited**: the panels neither fire nor refute its trigger.

**Not medical advice.**
