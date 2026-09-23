# `Q230P` — reconciling the unique-person count against the standing "8 patients, 6 families"

**SCIENTIST-B · 2026-09-23 · READ-ONLY toward every canonical file and every ledger. No commit candidate, no receipt, no registry edit, no `*_current.md` touched. No canonical count is changed by this file.**

🔴 **Not medical advice.** This reasons about a WWOX-DEE **genotype class** assembled from published literature, never about a person known to this project.

🔴 **Public-edition de-identification.** Role labels replace every within-family identifier. Transmission attribution, family-tree coordinates and demographic descriptors are **deliberately not recorded**; ancestry is kept at **family level** and is never decomposed. None of that is needed for the count, which is the only question here.

---

## 1 · VERDICT

> ## `Q230P UNIQUE AFFECTED COUNT: provisional 11; unresolved range 10–13 pending deduplication / post-2023 cases.`

🔴 **That line, not a bare number, is the state of record.** A point estimate printed without its range is exactly how *"8 patients, 6 families"* went stale — and §4 shows that figure was **arithmetically correct for its cutoff**. Reprinting **11** without **10–13** attached would repeat the failure this file exists to diagnose.

**The defensible provisional figure is 11 people affected with a `c.689A>C` / `p.(Gln230Pro)` allele, across 9 reported families, as of Oliver 2023** — plus **2 further unaffected `Q230P` heterozygous carriers** who are people but are not cases, giving **13 people known to carry the allele**. Two candidate rows remain genuinely unresolved and are named in §5; neither can move the count by more than one.

**"8 patients, 6 families" is not wrong. It is a 2021 tally, and it is arithmetically exact for its own cutoff** — see §4, where it is decomposed to the individual. It is **superseded as a current figure**, not corrected.

Yesterday's estimate of **10–11** was low by one for a specific, correctable reason: it discarded `Piard pt #19` as unusable. §3.2 restores it.

---

## 2 · Sources and the precedence actually applied

| Tier | Source | What it may settle |
|---|---|---|
| **PRIMARY** | Johannsen 2018 · PMID [29808465](https://pubmed.ncbi.nlm.nih.gov/29808465/) — full text read 2026-09-23 (`johannsen2018_fulltext_q230p_revival_20260923.md`) | its own family, zygosity, count |
| **PRIMARY** | Weisz-Hubshman 2019 · PMID [30853297](https://pubmed.ncbi.nlm.nih.gov/30853297/) — full text read 2026-09-23 (`ft117_weiszhubshman2019_fulltext_read_20260923.md`) | its own families, zygosity, count |
| **PRIMARY for its own cohort** | Oliver 2023 Table 1 · PMID [36779245](https://pubmed.ncbi.nlm.nih.gov/36779245/) — reconstructed in `oliver2023_table1_independent_reconstruction_20260921.md` | Oliver's own 13 cases: zygosity **and** count |
| **COMPILATION** | Oliver 2023 Supplementary Table S1 · `files/fulltext/PMID36779245_Oliver2023_suppl_TableS1.xlsx`, read cell-by-cell this session | enumerating *reports*; **never** a person count |
| **SECONDARY** | Banne 2021 · PMID [33916893](https://pubmed.ncbi.nlm.nih.gov/33916893/), *Cells* review · Piard 2019 · PMID [30356099](https://pubmed.ncbi.nlm.nih.gov/30356099/) (partial read; Supplementary Tables 1–4 recorded UNAVAILABLE) | cross-check only |

🔴 **An Oliver Table S1 row is an allele-observation, not a person.** Measured directly in the file: the sheet carries **exactly 9 rows bearing `c.689A>C; p.Gln230Pro`**, and its own `# times reported` cell reads **9** on every one of them — so that "9" counts *rows*, not people. Two of those rows are multi-person keys (`Johannsen … | Family1`; `Weisz-Hubshman … | Family 2`). The sheet demonstrably uses multi-person keys elsewhere (`Piard … | sibs #13, #14`; `Oliver … | sibs #9, #10`), so single-`pt #` keys are read here as one person each. **There is no zygosity column anywhere in the sheet.**

---

## 3 · THE TABLE — rows are candidate unique persons

| # | Source | Family | Source identifier | Genotype | `Q230P` status | Ancestry / geography (family level, as printed) | Likely duplicate of | Evidence |
|---|---|---|---|---|---|---|---|---|
| 1 | Johannsen 2018 | J-1 | S1 key `Family1` → homozygote A | `c.689A>C`/`c.689A>C` | **homozygous** | Afghan | — | **PRIMARY** |
| 2 | Johannsen 2018 | J-1 | S1 key `Family1` → homozygote B | `c.689A>C`/`c.689A>C` | **homozygous** | Afghan | — | **PRIMARY** |
| 3 | Weisz-Hubshman 2019 | W-2 | family 2 / compound heterozygote 1 | `c.689A>C`/`c.517-2A>G` | compound het | Yemenite + Moroccan Jewish + Kurdish *(one family-level string; not decomposed)* | — | **PRIMARY** |
| 4 | Weisz-Hubshman 2019 | W-2 | family 2 / compound heterozygote 2 | `c.689A>C`/`c.517-2A>G` | compound het | as above | — | **PRIMARY** |
| 5 | Weisz-Hubshman 2019 | W-2 | family 2 / unaffected `Q230P` carrier 1 | `c.689A>C`/WT | **carrier — not a case** | as above | — | **PRIMARY** |
| 6 | Weisz-Hubshman 2019 | W-2 | family 2 / unaffected `Q230P` carrier 2 | `c.689A>C`/WT | **carrier — not a case** | as above | — | **PRIMARY** |
| 7 | Piard 2019 | P-a | `pt #6` | `c.689A>C`/`c.1138dup p.Cys380LeufsTer149` | compound het | France | — | COMPILATION |
| 8 | Piard 2019 | P-b | `pt #7` | `c.689A>C`/**second allele not listed** | 🟡 **UNRESOLVED** | Iran | — | COMPILATION |
| 9 | Piard 2019 | P-c | `pt #19` | `c.689A>C` **+ `c.1073C>T p.Thr358Ile` + `c.598A>G p.Lys200Glu`** — three alleles on one key | 🔴 **UNRESOLVED** (§3.2) | France | — | COMPILATION, **defective row** |
| 10 | Piard 2019 | P-d | `pt #20` | `c.689A>C`/**not listed** | 🟡 **UNRESOLVED** | Moroccan | ⚠️ possibly row 13 | COMPILATION |
| 11 | Oliver 2023 | O-a | `pt #1` | `c.689A>C`/**exon 7–8 deletion** | compound het | Italy | — | **PRIMARY** (own Table 1) |
| 12 | Oliver 2023 | O-b | `pt #2` | `c.689A>C`/`c.689A>C` | **homozygous** | Italy | — | **PRIMARY** (own Table 1) |
| 13 | Oliver 2023 | O-c | `pt #5` | `c.689A>C`/`c.689A>C` | **homozygous** | North Africa | ⚠️ possibly row 10 | **PRIMARY** (own Table 1) |

**Beyond the named source set** — two further people carrying the allele, outside Oliver's 2023 horizon and therefore absent from Table S1. Listed so the count is not silently short; **excluded from the headline figure** because the artefact was not read this session:

| # | Source | Family | Source identifier | Genotype | `Q230P` status | Geography | Likely duplicate of | Evidence |
|---|---|---|---|---|---|---|---|---|
| 14 | PMID [40875931](https://pubmed.ncbi.nlm.nih.gov/40875931/) 2025 registry cohort | R-a | `case ID 11` | `c.689A>C`/`p.Gln72*` | compound het | not recorded here | ⚠️ overlap with earlier literature not excludable | SECONDARY (LEGEND locator) |
| 15 | PMID 40875931 | R-b | `case ID 23` | `c.689A>C`/`c.689A>C` | **homozygous** | not recorded here | declared *"Novel"* in the source | SECONDARY (LEGEND locator) |

### 3.1 · Where zygosity actually comes from

Oliver's own Table 1 states it in words — *"p.Gln230Pro in three of our patients (homozygous in two; compound heterozygous in one)"* — which is why rows 11–13 carry **PRIMARY** strength while sharing a key space with rows that do not. **For rows 8 and 10 no source in hand states zygosity**, and Table S1's single-allele listing cannot distinguish a homozygote from a compound heterozygote whose partner allele went unlisted.

### 3.2 · 🔴 The correction that moves 10 → 11: `pt #19` is a person, not a defect

Piard 2019 states in its own text: ***"p.(Gln230Pro) was found in four families."*** Table S1 carries **exactly four Piard keys** bearing the allele — `pt #6`, `#7`, `#19`, `#20` — none of them a `sibs` key. The primary's own count therefore **requires all four to be real people**.

The three-allele anomaly on `pt #19` is a defect **in the compilation's transcription**, not evidence that the person does not exist. Yesterday's map excluded the row *"from any count"*; that was the wrong remedy. The right one: **keep the person, mark the genotype unresolved.** Its `Q230P` status is `UNRESOLVED` because one of the two listed partner alleles must be mis-assigned, and Table S1 cannot say which.

### 3.3 · The de-duplication that must NOT be performed

Banne 2021 is a **review that aggregates rows 1–10**. Oliver 2023's 75 cases are **13 new plus 62 from the literature**, and Piard's series sits inside that 62. 🔴 **These cohorts re-report one another and must never be summed.** The table above is built from the publication that *first* reported each person, which is the only summation rule that does not double-count.

---

## 4 · Where "8 patients, 6 families" came from — decomposed exactly

The figure appears in `missense_splice_reclassification_risk_20260921.md` (§ verdict and the allele table). Its upstream source is **not** a primary paper: it is the **Banne 2021 *Cells* review**, recorded in `q230p_survival_paradox_20260921.md` §2.4 as *"The 2021 census: **8 patients across 6 families**."*

It decomposes without residue:

| Contributor | People | Families |
|---|---|---|
| Johannsen 2018 | 2 | 1 |
| Weisz-Hubshman 2019 (affected only) | 2 | 1 |
| Piard 2019 (*"four families"*) | 4 | 4 |
| **Total** | **8** | **6** |

🎯 **The arithmetic is exact, and that is the proof of provenance.** The figure is a **2021 literature cutoff**, counted over **affected people only** (it correctly omits the 2 unaffected carriers) and over **first-report families**.

### 4.1 · Its status now

| Question | Answer |
|---|---|
| Simply wrong? | **No.** Every one of the 8 is in the table above, at rows 1–4 and 7–10. |
| Still correct under a different counting rule? | **Yes — under a pre-Oliver cutoff.** As a statement of "the published `Q230P` constituency **as of 2021**, affected people only", it stands unamended. |
| Superseded? | **Yes, as a current figure.** Oliver 2023 adds **3 affected people in 3 families from its own cohort** (rows 11–13), which post-date the review. 8 → **11**, 6 → **9**. |
| Why the older file did not catch it | It records Johannsen 2018 as *"`unrecoverable_by_these_routes`… abstract-level"* and never held Oliver's Table S1. Both are on disk as of 2026-09-23. **The figure aged out; it was not mis-derived.** |

🟡 **One presentational hazard worth naming:** `missense_splice_reclassification_risk_20260921.md` prints "8 patients, 6 families" as a bare parenthetical with no *as-of* date and no attribution to Banne 2021. A cutoff-bound number that does not carry its cutoff will go stale silently again. **Flagged, not edited — read-only actor.**

---

## 5 · The exact remaining ambiguity, and what would settle each

Nothing below moves the headline by more than one person in either direction.

| ID | Unresolved rows | The question | What would settle it |
|---|---|---|---|
| **R1** | row 9 (`Piard pt #19`) | Which two of the three listed alleles are this genotype? Is `Q230P` here homozygous, in trans with `c.1073C>T`, or in trans with `c.598A>G`? | **Piard 2019 Table 1 and Supplementary Tables 1–4.** LEGEND holds a **partial** read of this paper (`FTR-20260811-30356099-01`) and its supplementary tables are recorded **UNAVAILABLE, not empty**. Acquiring them closes R1 and R3 together. **Does not change the count** — only the genotype cell. |
| **R2** | rows 10 and 13 (`Piard pt #20` ↔ `Oliver pt #5`) | Same person reported twice? Both carry `Q230P`; geographies ("Moroccan" / "North Africa") are compatible. | Oliver declares its cohort **13 new cases**, and separately lists Piard's people under Piard's own key — strong, but **self-declared**. A definitive settle needs Oliver's per-case recruitment site plus an explicit prior-publication statement, or author contact. **This is the only ambiguity that can change the count: 11 or 10.** Checked and found insufficient: `files/fulltext/PMID36779245_Oliver2023_suppl_S1_info.docx` contains figure legends only, no case narratives. |
| **R3** | rows 8 and 10 | Homozygous, or compound heterozygous with an unlisted partner allele? | Same acquisition as R1. **Does not change the count.** |
| **R4** | rows 14 and 15 | Are the 2025 registry cases new people, or re-reports of rows 1–13? | Read PMID 40875931 against this table. Row 15 is self-declared *"Novel"*; row 14 is not. **Resolving R4 upward gives 13 affected people; it is excluded from the headline until read.** |

**So the count is stated as a range with its causes attached, not as a point estimate:**

- **11 affected people / 9 families** — **provisional**, on the named sources, as of Oliver 2023. 🔴 **Never quote it without the 10–13 range.**
- **10** if R2 resolves as a duplicate.
- **13** if R4 resolves as two new people.
- **13 people carrying the allele** if the 2 unaffected heterozygous carriers (rows 5–6) are counted as people rather than as cases. 🔴 **State which of the two you mean. Most of the disagreement in this repository's `Q230P` numbers is a people-versus-cases equivocation, not a disagreement about the literature.**

---

## 6 · Two rules that must travel with this table

1. 🔴 **Only rows 1–2, 12, 13 and 15 are `Q230P`/`Q230P`.** Rows 3–4, 7, 11 and 14 carry a second, different deleterious allele — including a demonstrated exon-6 skipping splice allele, a frameshift, a multi-exon deletion and a nonsense allele. **Any phenotype in those people is a two-allele phenotype and cannot be used to isolate the molecular effect of `Q230P`.** Rows 8, 9 and 10 are unrated on this axis until R1/R3 close.
2. 🔴 **The 1:177 carrier rate belongs to `c.517-2A>G` alone**, measured as 2/353 controls in a founder population. **No founder denominator of any kind has ever been measured for `Q230P`**, and the family at rows 3–6 carries a mixed family-level ancestry string. Attaching that rate to `Q230P` would be a straightforward error.

---

## 7 · What this file does NOT do

No canonical count is edited. `missense_splice_reclassification_risk_20260921.md` is **not** amended — its figure is correct for its cutoff, and rewriting a dated tally in place would destroy the evidence that the count moved. The successor figure lives here, with its cutoff attached, its decomposition shown and its residual ambiguity named. Promotion is a `BATCH_COMMIT` decision, not this actor's.
