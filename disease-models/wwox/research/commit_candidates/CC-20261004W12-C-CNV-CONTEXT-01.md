# CC-20261004W12-C-CNV-CONTEXT-01 — the 1447 annotation holds at 400 dpi; the deletion is one of several common WWOX intronic SVs, and it is not a rank-1 result in the authors' own table

- **Wave:** intake wave 12, 2026-10-04, Scientist C (RE-READ wave)
- **context_policy:** SOURCE_FIRST — the page and the workbook were read before DIS-036 and
  CLAIM 032 were opened.
- **Target record:** `DIS-036` in `disease-models/wwox/research/dismissal_ledger_current.md`
- **Records checked and left unchanged:** `CLAIM 032` (`in observation`) — its figures
  *«gnomAD AF 0.339, 1447 homozygotes»* are **confirmed digit for digit** at 400 dpi; no op.
- **Change class:** **MINOR.** Append-only addition to a research-layer rejection that makes the
  rejection better grounded; nothing narrowed, reversed or demoted. No baseline claim touched.
- **Source read:** PMID 41345172 (DOI 10.1038/s41598-025-28338-2).
  `files/fulltext/PMID41345172_De2025_supplement/41598_2025_28338_MOESM15_ESM.pdf` sha256
  `2b7f1229a893a82078deff5aac44f8d96620f066b0b70e86fd8c937f6b91085c` (already declared; page 21
  re-rendered at 400 dpi) and `…/41598_2025_28338_MOESM1_ESM.xlsx` sha256
  `78d6f924a95cd30343cf1964c1cb3fb323561a228a4993955e12fd40a7178e91` (newly acquired free from the
  Europe PMC supplementaryFiles archive for PMC12753814; the three files already held came back
  byte-equal).
- **Receipt of the producing reading:** `FTR-20261004-41345172-03` (prepared, not recorded).

## Exact op

**File:** `disease-models/wwox/research/dismissal_ledger_current.md`
**Record:** `DIS-036`
**Op:** `insert-before` the line below (measured **1 occurrence in `DIS-036` and 1 in the file**).

`old` anchor:

```
- **Confine:** this rejects a **disease-allele or dose** reading only.
```

`new` (inserted as its own bullet immediately before that line):

```
- 🔵 **Re-read 2026-10-04 (`CC-20261004W12-C-CNV-CONTEXT-01`, intake wave 12 Scientist C, receipt `FTR-20261004-41345172-03`) — two further facts from the same supplement, both strengthening this rejection.** (1) **The 1447 annotation survives** a 400 dpi re-render of Supplementary Figure 19 (earlier read at 70 dpi): `DEL_16_156229`, 7355 / 21694 = 0.3390, 1447 homozygotes. **And it is not alone:** the same gnomAD table lists fourteen structural variants inside WWOX, and the three rows after it are also common — `DEL_16_156234` (89 bp, AF 0.318, **220** homozygotes), `INS_16_101038` (321 bp, AF 0.186, 122), `INS_16_101054` (321 bp, AF 0.101, **327**). WWOX carries several common intronic SVs; this one is the most frequent, not a singular event. (2) **The authors' own rank-1 table does not contain it:** Supplementary Table 1, read cell-wise, holds 139 rank-1 result cells across every cohort, method and phenotype, and **none** carries a coordinate in the WWOX interval; the only chromosome-16 cell is `16:75296761; BCAR1`. For SANAD drug response the rank-1 cells are `0.0000146; 14:19785775` and `1.7e-05; 8:140765991; TRAPPC9`, both stronger than the deletion's 1.68 × 10⁻⁴. The body's framing of this CNV as the most distinct common signal is the authors' emphasis, not their top-ranked result.
```

## Registry records

None owed; PMID 41345172 is `PAPER 209` / `LIT-0501`.

### LOCATOR TRIPLES FOR BLIND AUDIT

1. (The 1447-homozygote figure holds at high resolution | `[figure attestation - pixels cannot be quote-matched] Supplementary figure 19, page 21 rendered at 400 dpi: row DEL_16_156229, intronic, deletion, position 78371638 - 78384898, size 13.3 kb, allele count 7355, allele number 21694, allele frequency 3.39e-1, number of homozygotes 1447.` | Supplementary figure 19 (PDF page 21), re-rendered at 400 dpi — `files/fulltext/PMID41345172_De2025_supplement/41598_2025_28338_MOESM15_ESM.pdf`)
2. (Other common intronic WWOX structural variants sit in the same table | `[figure attestation - pixels cannot be quote-matched] Supplementary figure 19 at 400 dpi lists fourteen structural-variant rows inside WWOX; immediately after DEL_16_156229 the highlighted block continues with DEL_16_156234, intronic deletion 78394517 - 78394606, 89 bp, 6867 of 21572, 3.18e-1, 220 homozygotes; INS_16_101038, intronic insertion at 78692826, 321 bp, 4033 of 21640, 1.86e-1, 122 homozygotes; INS_16_101054, intronic insertion at 79190720, 321 bp, 2167 of 21506, 1.01e-1, 327 homozygotes.` | Supplementary figure 19 (PDF page 21), rows 2 to 4 of the highlighted block — `files/fulltext/PMID41345172_De2025_supplement/41598_2025_28338_MOESM15_ESM.pdf`)
3. (The authors' rank-1 table carries no WWOX-interval result | `[spreadsheet attestation - read cell-wise from the workbook XML] Supplementary Table 1 holds 139 packed result cells of the form 'p; chromosome:position; gene; MAF'. No cell carries a position on chromosome 16 between 78 and 80 Mb; the only chromosome-16 cell is '2.91e-09; 16:75296761; BCAR1'. For SANAD drug_response the rank-1 cells are '0.0000146; 14:19785775' (genotype univariate) and '1.7e-05; 8:140765991; TRAPPC9' (log-r ratio univariate).` | Supplementary Table 1, all result cells — `files/fulltext/PMID41345172_De2025_supplement/41598_2025_28338_MOESM1_ESM.xlsx`)
