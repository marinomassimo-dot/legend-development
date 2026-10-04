# CC-20261004W7-C2-DOSE-ROUTE-01 — two more dose scalars in use, a neonatal IV capsid arm with a liver-enzyme and DRG-transduction signal, and no immune readout in either

`context_policy: SOURCE_FIRST`
**Date:** 2026-10-04 · **Author:** Scientist C2, intake wave 7 · **Change class:** MINOR
**Target records:** `disease-models/wwox/research/discovery_ledger_current.md` (append one lead)
Receipts: `FTR-20261004-42511902-01`, `FTR-20261004-42137291-01` (prepared, not recorded) · Manifests PASS · Dossiers `PMID42511902.md`, `PMID42137291.md`
**Nothing here is medical advice. WWOX occurs zero times in either source; earned nulls for the gene.**

## 1 · What it adds to, bounds, and leaves untouched

- **Adds** to `CC-20261003W5-C-DOSE-SCALAR-01`: a per-body-weight conversion used for a neonatal IV dose (about 5E12 vg/kg from 1E10 vg in a ~2 g pup, authors' arithmetic), and a CSF-volume scale-up of 250 (0.04 to 10 mL, juvenile NHP) in a package where NHP per-animal totals span animals of different weight (GLP 1-2 kg; non-GLP 2-4 kg). The same per-animal total is therefore a different per-kg dose by roughly a factor of two within one paper (INFERENZA arithmetic).
- **Adds** to the restoration-spec route row: neonatal IV with four capsids; DRG transduction by reporter intensity high with AAV9 and MacpnS1, 4- to 6-fold lower with rAAV2-retro and PHP.eB; serum ALT and AST raised only with MacpnS1 at one time point.
- **Bounds** both: single dose, single age, single harvest in 42511902; sponsor package with a muscle promoter in 42137291; no immunosuppression and no immune endpoint beyond anti-AAV9 antibody presence (42137291) or none (42511902).
- **Leaves untouched** the window record (`CC-20261003W5-A-WINDOW-STATUS-01`): neither paper has an age contrast.
- **Adds** that the same package's planned human fixed starting doses (5.0E+14 and 1.0E+15 vg) exceed its highest NHP per-animal total (3.05E+14 vg): a per-animal-total comparison and a CSF-volume comparison give different margins (the printed margin calculation is not in the body; Table S3 unread).
- **Carried-number integrity:** 42511902 states a 2 uL injection volume and describes a ~22 uL mixture, and n "at least four" against n = 6 and n = 8 in legends; carry its numbers with these.

## 2 · Op — discovery_ledger_current.md

`op: APPEND` one lead. No `old` text.

```
### DL-METH-xxx (provisional) — Dose in the CNS-delivery literature is also quoted per kilogram and by CSF-volume scale-up inside the same paper; a per-animal total spans a factor of two in per-kg dose across animal sizes

**Tag:** INFERENZA
**Status:** open
**Created:** 2026-10-04 · intake wave 7, Scientist C2
**Causal statement:** The dose-scalar lead of wave 5 lists fixed totals, per-gram-of-brain and per-CSF-volume scalars. Two further sources show the per-kilogram scalar
(neonatal IV, about 5E12 vg/kg, from a per-pup total) and a CSF-volume scale-up of 250 used to declare 8.0E+11 vg in a mouse equivalent to 2.0E+14 vg in a juvenile NHP,
while the NHP studies dose per animal in animals of 1-4 kg. A reader carrying a per-animal NHP total without the animal weight carries a quantity that changes by about
two-fold per kilogram within a single paper.
**Reasoning chain:**
1. 42511902 doses 1E10 vg per P2 pup and converts to about 5E12 vg/kg using a stated body weight of about 2 g.
2. 42137291 doses NHP at 2.5E+13 to 2.0E+14 (non-GLP, 2-4 kg) and 5.28E+13 to 3.05E+14 vg per animal (GLP, 1-2 kg) and scales by CSF volume (0.04 to 10 mL, 250-fold).
3. Its efficacy plateaued across mouse doses; the authors attribute this to treatment age, not to a ceiling in dose-response.
**Counter-evidence / what would refute this lead:** target exposure measured as flat across animal sizes at fixed total dose (as in the wave-5 lead).
**Falsifying experiment:** as in the wave-5 lead.
**Operational consequence (proposed, not a gate):** carry dose with its scalar and its animal weight or CSF volume in the same field.
**Transfer limit to WWOX:** none of the vector genome numbers transfers between genes, promoters, capsids or species; the lead is about how dose is reported.
**Not medical advice.**
```

### LOCATOR TRIPLES FOR BLIND AUDIT

- (Per-pup dose converted to a per-kilogram figure | For a P2 pup (~2.0 g body weight), this corresponds to approximately | Results 3.1, para 1, `files/fulltext/PMID42511902_Gao2026_PMC.xml`)
- (Injection volume stated as 2 uL | Each neonatal mouse received an absolute dose of 1 × 1010 vg in a 2 µL injection volume intravenously via the temporal vein. | Methods 2.1, `files/fulltext/PMID42511902_Gao2026_PMC.xml`)
- (Injected mixture described as about 22 uL | The full ~22 µL mixture was aspirated into a 1 mL insulin syringe fitted with a 29-gauge needle for injection. | Methods 2.2, `files/fulltext/PMID42511902_Gao2026_PMC.xml`)
- (DRG transduction 4- to 6-fold lower for retro and PHP.eB | approximately 4- to 6-fold lower than those of AAV9 and AAV-MacpnS1 | Results 3.3, `files/fulltext/PMID42511902_Gao2026_PMC.xml`)
- (Only MacpnS1 raised ALT and AST | Only the AAV-MacpnS1 group registered significant increases in both | Results 3.5, `files/fulltext/PMID42511902_Gao2026_PMC.xml`)
- (No immune endpoints measured | without evaluation of broader immune responses, including cytokine profiles, anti-AAV antibody production, or complement activation | Discussion, limitations, `files/fulltext/PMID42511902_Gao2026_PMC.xml`)
- (Mouse-to-NHP CSF-volume scale-up | scale up from mice with estimated CSF volume of 0.04 mL to juvenile NHP with estimated CSF volume of 10 mL | Results, Biodistribution, `files/fulltext/PMID42137291_Thomsen2026_PMC.xml`)
- (GLP NHP animal size | male juvenile (7–12 months of age, with an average body weight of 1–2 kg) cynomolgus macaque NHPs | Methods, Nonhuman primates, `files/fulltext/PMID42137291_Thomsen2026_PMC.xml`)
- (Planned human fixed starting doses | fixed starting doses of INS1201 (5.0E+14 vg and 1.0E+15 vg) | Introduction, last paragraph, `files/fulltext/PMID42137291_Thomsen2026_PMC.xml`)
- (Dose plateau attributed to treatment age | further increases in dose might not be expected to provide additional added benefit when dosed at this time point | Discussion, `files/fulltext/PMID42137291_Thomsen2026_PMC.xml`)


---

## BATCH DISPOSITION

**Verdict:** `PROPAGATED — MERGED into DL-METH-117` by `BATCH_20261004_001` (2026-10-04, MINOR, WM_v7.13 → WM_v7.14; ACTOR_ID `scientist`, Scientist K, batch integrator).
**Surfaces written:** discovery_ledger_current.md

**Merged rather than written as a second record**, and the verdict reads `PROPAGATED — MERGED into DL-METH-117` because `MERGED` alone is not in `growth_anchors`' closing vocabulary and would leave this candidate counted as open — the tooling fact `BATCH_20261003_004` recorded and `BATCH_20261003_005` applied.
**Why merged.** The dispatch asked for a deduplication pass against the landed dose-scalar records. `DL-METH-117` already *is* the dose-scalar lead: it enumerates fixed total vg, per gram of brain and per CSF volume, and its reasoning chain already names a programme that scales by CSF volume. A second record asserting that *dose is also quoted per kilogram and by CSF-volume scale-up* would let a reader cite the same lesson twice. The candidate's genuine increments were therefore added **inside** `DL-METH-117` as its wave-7 arm: the **per-kilogram** scalar as a fourth kind, the stated 250× CSF factor, and the observation the landed record did not hold — that a per-animal macaque total is about a **two-fold** different per-kilogram dose inside a single paper, because that paper's animals span 1–2 kg and 2–4 kg. `DL-METH-117`'s operational consequence was extended accordingly: carry dose with its scalar **and** the animal weight or CSF volume in the same field.
**Both recomputable figures were re-derived and are exact:** 1 × 10¹⁰ vg ÷ 0.002 kg = 5.0 × 10¹² vg/kg, and 10 mL / 0.04 mL = 250. The planned human starting doses exceeding the highest macaque per-animal total is carried with the fact that the printed margin calculation is absent and Table S3 unread.
