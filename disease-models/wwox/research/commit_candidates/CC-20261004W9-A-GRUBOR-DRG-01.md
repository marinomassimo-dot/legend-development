# COMMIT CANDIDATE — CC-20261004W9-A-GRUBOR-DRG-01 — the controlled immunosuppressed-versus-unmedicated primate DRG comparison exists (PMID 41404412); `FT-193` is stale and `DIS-031`'s wave-6 revival triggers are met in form, not in effect

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist`, Scientist A of intake wave 9, 2026-10-04.
**Change class:** **MINOR.** Every target is a research-layer record (queue, dismissal ledger,
discovery ledger, two registry status lines). No `consolidated baseline` claim is narrowed or
reversed. Provisional until the integrator measures anchors on current `main`.
`context_policy: QUESTION_DRIVEN` (the registry's question was held before the panels were opened).
**Not medical advice.** The source contains no WWOX content; nothing here transfers to a WWOX
construct beyond a design fact.

---

## 1 · What the owed sections show

Main Figures 6C, 7C and 8D (not the supplement) carry the datum `DIS-031` and `FT-193` ask for:
graded per-animal, per-level DRG histopathology for an immunosuppressed arm, a concurrent
unmedicated arm given the same vector and dose, and a vehicle arm, n = 3 each, in three cynomolgus
studies (three cargos; dexamethasone + MMF + tacrolimus in two, dexamethasone + tacrolimus in one).
The supplement adds no DRG per-arm table (Tables S1-S5 are clinical chemistry, EM of the IMS-free
time course, module p-values, CSF; Figures S13-S15 grade trigeminal ganglion, sciatic nerve and
roots).

Animals with a DRG neuronal finding, unmedicated vs immunosuppressed: 2/3 vs 1/3, 3/3 vs 1/3,
3/3 vs 1/3. Printed per-DRG counts: 10/26 vs 1/29 (38.5 % vs 3.4 %, recomputed) and 11/36 vs 1/36
(30.6 % vs 2.8 %, recomputed). Animals with mononuclear infiltrate: 2/3 vs 1/3, 3/3 vs 2/3, 3/3 vs
2/3 (hand count of the plots). Reduced in every study, **eliminated in none**; DRG transgene
expression did not differ between arms; no histopathology statistics; sponsor study; longest arm
43 days.

## 2 · Which landed records this gates, and what holds

| record | wording | verdict |
|---|---|---|
| `FT-193` | "OPEN — not acquired, not read" | **Stale.** The paper was read in wave 4 (`FTR-20261003-41404412-01`, partial) and re-read here. Correct the status line. |
| `DIS-031` wave-6 arm, `REVIVAL_TRIGGER` | "the controlled comparison none of these ten sources contains. Second, weaker trigger: read Grubor 2025 ... which this repository has not read" | **Both triggers are met in form.** The proposition the arm rejects ("immunosuppression bounds the DRG risk ... so a programme ... can treat that risk as addressed") is **still not supported**: residual neuronal findings in one animal of every treated arm, infiltrate in two of three in two studies, 43 days at most, n = 3. The arm's "only reduce rather than eliminate survives" is **confirmed by measurement**. What the arm lacked, a controlled comparison showing that reduction, is now on file. |
| `DIS-031` first arm | "Both directions are therefore unsupported as general claims" | **Unaffected**: the panels do not touch the postulate-versus-measurement point (no antigen-specific T cells detected). |
| `DL-THER-116` | dose moves neuron loss, not infiltrate, in PMID 36951961 | **Holds for its own dataset; falsifier half not met.** In the matched immunosuppressed-versus-not comparisons here infiltrate incidence was not unchanged; neuron loss fell more than infiltrate. The comparison varies regimen not dose, so the "two dials" lead is neither confirmed nor refuted. |
| `PAPER 162` / `LIT-0451` | "figure panels not inspected as images and no supplementary file fetched — owed" | **Narrowed**: panels read; supplement fetched, figures S1-S12/S14/S15 by caption. Still `partial_fulltext_read`. |
| `RL-C-20261003w6`, `RL-C-20261003w4a` | open questions | Not edited here; the integrator may cite this candidate. |

## 3 · Ops (provisional; each `old` measured unique in its record)

### 3.1 · `disease-models/wwox/research/full_text_queue_current.md`, record `FT-193`

| field | value |
|---|---|
| op | `replace` |
| old | `**Current status:** OPEN — not acquired, not read.` |
| new | `**Current status:** PARTIALLY DISCHARGED 2026-10-04 (intake wave 9, \`CC-20261004W9-A-GRUBOR-DRG-01\`) — the paper was read in wave 4 (\`FTR-20261003-41404412-01\`, \`partial_fulltext_read\`) and re-read with main Figures 1-4 and 6-8 as images and Document S1 fetched; the graded per-arm DRG histopathology is in main Figures 6C, 7C and 8D, not in the supplement. Supplementary Figures S1-S12, S14 and S15 were read by caption only.` |

### 3.2 · `disease-models/wwox/research/dismissal_ledger_current.md`, record `DIS-031`

| field | value |
|---|---|
| op | `replace` |
| old | `Second, weaker trigger: **read Grubor 2025** (doi \`10.1016/j.omtm.2025.101643\`), which is the published evidence the «reduce but not eliminate» sentence rests on and which this repository has not read.` |
| new | `Second, weaker trigger: **read Grubor 2025** — DONE 2026-10-04 (\`CC-20261004W9-A-GRUBOR-DRG-01\`). That paper is itself the first trigger's design: three cynomolgus studies with an immunosuppressed arm, a concurrent unmedicated arm and a vehicle arm, n = 3 each, graded DRG histopathology per animal (animals with a neuronal finding 2/3 vs 1/3, 3/3 vs 1/3, 3/3 vs 1/3). The rejection above is NOT revived: every treated arm kept a residual neuronal finding, infiltrate persisted in two of three animals in two studies, the longest arm ran 43 days, and it is a sponsor study; what is added is a controlled measurement that immunosuppression with a calcineurin inhibitor reduces both endpoints in macaques.` |

### 3.3 · `disease-models/wwox/research/discovery_ledger_current.md`, record `DL-THER-116`

| field | value |
|---|---|
| op | `replace` |
| old | `or a matched immunosuppressed-versus-not comparison at a single dose in which infiltrate incidence is unchanged.` |
| new | `or a matched immunosuppressed-versus-not comparison at a single dose in which infiltrate incidence is unchanged. [2026-10-04, wave 9: PMID 41404412 supplies three such comparisons and in none was infiltrate incidence unchanged (animals with infiltrate 2/3 to 1/3, 3/3 to 2/3, 3/3 to 2/3), while neuron loss fell further; they vary regimen, not dose, so the dose dial is untested and the lead is neither confirmed nor refuted.]` |

### 3.4 · `disease-models/wwox/registries/paper_registry_current.md`, record `PAPER 162`

| field | value |
|---|---|
| op | `replace` |
| old | `Partial: figure panels not inspected as images and no supplementary file fetched — owed.` |
| new | `Partial: main figure panels read as images (wave 9 re-read, receipt \`FTR-20261004-41404412-02\`) and Document S1 fetched; supplementary Figures S1-S12, S14 and S15 read by caption only.` |

### 3.5 · `disease-models/wwox/registries/literature_tracking_log_current.md`, record `LIT-0451`

| field | value |
|---|---|
| op | `replace` |
| old | `figure panels not inspected as images and no supplementary file fetched; record created by` |
| new | `main figure panels read as images and Document S1 fetched in wave 9 (supplementary figures by caption); record created by` |

## 4 · Verification before propagation

1. `deepdive_manifest.py --pmid 41404412 --verify-artifacts --require-current-schema` returned PASS at the commit of this candidate.
2. Receipt `FTR-20261004-41404412-02` must be in the ledger before the `PAPER 162` text is changed.

### LOCATOR TRIPLES FOR BLIND AUDIT

- (Unmedicated hGBA1 arm, per-DRG count | Minimal-to-moderate DRG neuron degeneration/necrosis in cervical, lumbar, and/or sacral DRGs was noted in all three AAV9-hGBA1-dosed animals (10 of 26 DRGs evaluated) in the absence of IMS#2. | PMID 41404412, Results, IMS study #2)
- (Immunosuppressed hGBA1 arm, per-DRG count | Only 1 out of 29 DRGs evaluated from animals that received AAV9-hGBA1 with IMS#2 had a finding of neuronal degeneration/necrosis | PMID 41404412, Results, IMS study #2)
- (mir-SOD1 arm, neuronal and infiltrate counts under immunosuppression | strikingly reduced the incidence of AAV9-mir-SOD1-mediated DRG neuronal degeneration/necrosis (one finding of mild severity of 36 DRGs evaluated), limited the incidence and severity of DRG mononuclear cell infiltrates to five findings of minimal severity | PMID 41404412, Results, IMS study #3)
- (Study 1 summary sentence | Collectively, IMS#1 reduced the severity and/or incidence of histopathological findings in the DRG and SC in response to ICM delivery of AAVhu68-hSMN1 | PMID 41404412, Results, IMS study #1)
- (IMS did not act through lower transgene expression | we confirmed that IMS#1 treatment did not reduce hSMN1 transgene expression in the DRGs compared to subjects that received no IMS treatment | PMID 41404412, Results, IMS study #1)
- (Not all peripheral endpoints moved | However, IMS#1 did not appear efficacious in decreasing TG mononuclear cell infiltrates and sciatic nerve fiber degeneration in NHP that received AAVhu68-hSMN1. | PMID 41404412, Results, IMS study #1)
