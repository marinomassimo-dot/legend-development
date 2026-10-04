# COMMIT CANDIDATE — CC-20261004W9-A-THOMSEN-DRG-01 — the "macaque DRG grading in Table S5 / Figure S7" of PMID 42137291 does not exist; the debt is retired as "not printed", and `DL-METH-117`'s Table S3 gap is closed

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist`, Scientist A of intake wave 9, 2026-10-04.
**Change class:** **MINOR.** Corrects reading-debt wording in two discovery-ledger leads and in the
registry landing of one paper; narrows no `consolidated baseline` claim. Provisional ids and anchors.
`context_policy: QUESTION_DRIVEN`. **Not medical advice.** WWOX occurs zero times in the source.

---

## 1 · What the owed sections show

- **Table S5** is NHP GLP clinical pathology (blood chemistry and related tables). **Figure S7** is
  vector-genome biodistribution (brain, spinal cord and DRG as vg per diploid genome; CSF, serum, urine,
  feces as vg per mL) and shedding. The supplement holds **no DRG histopathology grading in any
  species**: the word DRG occurs in it only in biodistribution captions. The paper's NHP histopathology
  sentence stays a general statement; the DRG-specific evaluation shown is mouse (one field, Figure 8E).
- Figure S7B: NHP DRG vector genomes about 0.5-4 vg per diploid genome at every level and dose,
  no steep dose dependence (hand reading, n = 3 per bar). Figure 8C: the "no transgene mRNA in
  spinal cord or DRG" is a qualitative end-point RT-PCR with lanes for the three high-dose animals and
  one vehicle animal only; sensitivity not stated.
- Table S3 prints mouse total, dose per CSF mL and the NHP equivalent; recomputed 8.00E+11 / 0.04 mL =
  2.00E+13 vg/mL and x 10 mL = 2.00E+14 (exact); the 250-fold factor is exact. It has no human row and
  no margin calculation. NHP top dose per CSF mL is 3.05E+13 vg/mL, 1.525 times the mouse top dose per
  mL, while 381 times in total vg (3.05E+14 / 8.00E+11).

## 2 · Records gated and verdicts

| record | wording | verdict |
|---|---|---|
| `DL-MECH-114` | "the macaque DRG grading is in an unread supplement"; counter-evidence "Table S5, Figure S7 - both unread" would remove the observation | **Wording narrowed.** The grading is not in the supplement; neither table nor figure can remove or support the observation. The lead's causal statement is unaffected (it already said the grading "is not printed in the body"); it stays INFERENZA, compatible-with-not-demonstrated. |
| `DL-METH-117` wave-7 arm | "the printed margin calculation is not in the body and Table S3 is unread" | **Gap closed**: Table S3 read; it holds the CSF-volume conversion only, no margin. The arm's arithmetic (250, 2.00E+14) is confirmed. |
| `PAPER 216` | "Table S5 and Figure S7 were not fetched, so the DRG-specific NHP grading is unread"; "...is in an unfetched supplement" | **Narrowed**: fetched; the grading is not there. Depth stays `partial_fulltext_read`. |
| `LIT-0508` | next action names the same debt | **Narrowed** likewise. |
| `DIS-031`, `DL-METH-120`, `DL-THER-116` | | **Unaffected**: no immunosuppressed arm and no DRG grading exist here. |

## 3 · Ops (provisional; each `old` measured unique in its record)

### 3.1 · `disease-models/wwox/research/discovery_ledger_current.md`, record `DL-MECH-114`

| field | value |
|---|---|
| op | `replace` |
| old | `the macaque DRG grading is in an unread supplement` |
| new | `the macaque DRG-specific grading is not printed in the paper or its supplement` |

| field | value |
|---|---|
| op | `replace` |
| old | `a DRG-specific macaque table (Table S5, Figure S7 — **both unread**) showing graded mononuclear infiltrate or neuronal degeneration at the tested doses would remove the observation;` |
| new | `a DRG-specific macaque grading showing mononuclear infiltrate or neuronal degeneration at the tested doses would remove the observation — but wave 9 read the supplement and no such grading is printed (Table S5 is clinical pathology, Figure S7 is vector-genome biodistribution and shedding), so the observation can be neither removed nor supported from this paper;` |

| field | value |
|---|---|
| op | `replace` |
| old | `- **Reading debt declared:** Table S5 and Figure S7 of PMID 42137291 (` |
| new | `- **Reading debt retired 2026-10-04 (\`CC-20261004W9-A-THOMSEN-DRG-01\`):** Table S5 and Figure S7 of PMID 42137291 were read and do not carry DRG grading; the full histopathology report is not part of the publication. Earlier declaration: (` |

### 3.2 · `disease-models/wwox/research/discovery_ledger_current.md`, record `DL-METH-117`

| field | value |
|---|---|
| op | `replace` |
| old | `the printed margin calculation is not in the body and Table S3 is unread` |
| new | `the printed margin calculation is in neither the body nor Table S3 (read in wave 9: Table S3 prints mouse total, dose per CSF mL and NHP equivalent only; recomputed 8.00E+11 / 0.04 = 2.00E+13 vg/mL, x 10 mL = 2.00E+14, exact; no human row)` |

### 3.3 · `disease-models/wwox/registries/paper_registry_current.md`, record `PAPER 216`

| field | value |
|---|---|
| op | `replace` |
| old | `Partial: Table S5 and Figure S7 were **not fetched**, so the DRG-specific NHP grading is unread.` |
| new | `Partial: Table S5 and Figure S7 were fetched in wave 9 (receipt \`FTR-20261004-42137291-02\`) and carry no DRG grading (clinical pathology; vector-genome biodistribution); references and most supplementary figures remain unread.` |

| field | value |
|---|---|
| op | `replace` |
| old | `the DRG-specific NHP grading is in an unfetched supplement.` |
| new | `the DRG-specific NHP grading is not printed in the body or the supplement.` |

### 3.4 · `disease-models/wwox/registries/literature_tracking_log_current.md`, record `LIT-0508`

| field | value |
|---|---|
| op | `replace` |
| old | `**reading debt declared** — Table S5 and Figure S7 carry the DRG-specific NHP grading and were not fetched; they would decide whether the mononuclear-infiltrate-at-every-dose pattern holds in this package` |
| new | `**reading debt retired 2026-10-04** — Table S5 and Figure S7 were read: they carry no DRG-specific NHP grading, so the mononuclear-infiltrate-at-every-dose pattern cannot be tested in this package` |

## 4 · Verification before propagation

`deepdive_manifest.py --pmid 42137291 --verify-artifacts --require-current-schema` PASS at the commit of
this candidate. Receipt `FTR-20261004-42137291-02` recorded before the registry text changes.

### LOCATOR TRIPLES FOR BLIND AUDIT

- (Table S5 is clinical pathology | Table S5. NHP GLP toxicology clinical pathology tables | PMID 42137291, Document S1, Table S5 title)
- (Figure S7 is vector-genome biodistribution and shedding | Figure S7. INS1201 vg biodistribution and viral shedding in NHP, 3-month GLP study | PMID 42137291, Document S1, Figure S7 title)
- (The body cites Table S5 for liver-related clinical pathology only | without any correlating microscopic findings (see Table S5 for liver-related clinical pathology) | PMID 42137291, Results, GLP NHP toxicology paragraph)
- (NHP histopathology is a general statement | there were no significant INS1201-related effects on mortality, clinical signs, body weight, food consumption, ophthalmology, blood pressure, electrocardiogram, neurologic examination, nerve conduction velocity, physical examination, clinical pathology, blood cell count in the CSF, T cell responses, necropsy, organ weights, or histopathology | PMID 42137291, Results, GLP NHP toxicology paragraph)
- (The DRG-specific histology shown is mouse, one high-dose animal | image is from animal administered highest dose, 8.0E+11 vg | PMID 42137291, Figure 8 legend, panel E)
- (No NHP transgene mRNA in cord or DRG | INS1201 mRNA expression was not detected within any region of the spinal cord or DRG or injection site in NHPs dosed with INS1201 or vehicle. | PMID 42137291, Figure 8 legend, panel C)
