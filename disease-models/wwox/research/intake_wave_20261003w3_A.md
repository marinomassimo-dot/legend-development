context_policy: SOURCE_FIRST

# Intake wave 3 — 2026-10-03 — Scientist A: is WWOX-DEE one genotype-ordered spectrum, and which case series are independent?

- **Actor:** ACTOR_ID `scientist` (Scientist A), branch `task/sci-A-20261003w3`, dispatched by the Orchestrator under the standing authorisation of 2026-09-28.
- **Papers (6):** PMID 41153369 · PMID 37583270 · PMID 27495153 · PMID 35712340 · PMID 42092735 · PMID 38161429.
- **Method:** every source acquired as JATS XML (Europe PMC; one artefact from 2026-09-27 reused), every table, figure legend and figure image read, the one existing supplement read; first-pass notes written before any registry record was opened. **Declared exposures before reading:** (1) the receipt-status output for PMID 41153369 showed that a prior reading had paired it with PMID 42092735 as an intra-allelic comparison for p.L239R; (2) the metadata block of the existing PMID 38161429 manifest was seen after reading that text and before writing its notes. `FIRST-PASS OBSERVATIONS COMPLETE → PRIOR KNOWLEDGE ADMITTED FOR COMPARISON` — admitted: `registry_records.py get --pmid N --hops 1` for all six and for PMID 30094525, `CLAIM 001`, and the 2026-09-21 analyses that cite these papers.
- Patients are described at class level only. **Not medical advice.**

## 1 · Question assigned

> What does each source add to, or limit in, the claim that the WWOX-DEE phenotype is a *single* genotype-ordered spectrum — allele class predicts seizure onset and drug response, developmental ceiling, MRI signature and survival — and is each WWOX case series an independent observation or a re-description of patients already counted elsewhere?

## 2 · Per paper

| PMID | Verdict | Allele class × zygosity | What is new versus held | Receipt (prepared) | Candidates |
|---|---|---|---|---|---|
| 41153369 (cohort, 129 DEE) | INGEST (re-read; tables first seen) | missense p.L239R × homozygous, two siblings | Table 1 confirms the two siblings (one West, one EIDEE); only EEG and syndrome are reported; hypsarrhythmia attributed to different siblings in table and text; same university as PMID 42092735, no cross-citation | `sciA_41153369_1.json` (complete) | L239R-01, REGISTRY-01 (LIT) |
| 37583270 (IESS, 124) | INGEST | 2 × frameshift+nonsense; in-frame exons 6-8 deletion + `c.517-3C>A`; nonsense × homozygous | First structured landing (no identity record existed); per-patient treatment and outcome; three of four reached clinical spasm control on different drugs | `sciA_37583270_1.json` (complete) | REGISTRY-01, VIGABATRIN-01 |
| 27495153 (two sisters) | INGEST | nonsense × homozygous | Older sister alive at 7 years (vegetative, ventilated); younger sister's partial response included phenobarbitone; registry declared complete against a legacy event | `sciA_27495153_1.json` (complete; `first_read` after a legacy reconstruction) | W44X-01, REGISTRY-01 (LIT) |
| 35712340 (one boy) | INGEST — as a boundary case | missense × homozygous (`c.406A>G`, p.Ile136Val) | No seizures, normal MRI, walking: not WWOX-DEE, and attribution unproven; must not be counted as WOREE or SCAR12 | `sciA_35712340_1.json` (complete) | REGISTRY-01 |
| 42092735 (one boy) | INGEST | missense p.Leu239Arg × homozygous | Neurotransmitters never measured; perinatal confounders; vigabatrin failed, valproate + clobazam worked; its cited prior report is Serin 2018, not the cohort | `sciA_42092735_1.json` (partial: Serin 2018 queued) | REGISTRY-01, L239R-01, VIGABATRIN-01 |
| 38161429 (mini-review) | INGEST (re-read; background only) | mixed (collation) | "101" is a sum of overlapping sources; "all patients" with MRI anomalies contradicted by its own Piard row; 13% progression is a denominator artefact; Q230P "8 cases" is its citation of a review | `sciA_38161429_1.json` (partial: multihop queue open) | BATTAGLIA-01 |

Receipt files are in the Orchestrator's scratch `receipts_pending_w3/`; none is appended. All six were dry-recorded into a throwaway copy of the ledger with a copy of the state manifest: six `exit 0`, copy `verify` OK.

## 3 · Dedup — each patient counted once

- **p.L239R (homozygous):** Serin 2018 (one girl, a different centre; abstract only) · cohort PMID 41153369 (two siblings) · case report PMID 42092735 (one boy, same university as the cohort). The case report's patient may be the cohort's case 49 (same sex, age band, West-type spasms) or not (the report says no consanguinity and no family history, while case 49 has an affected sister). **Count: 3 or 4 children in 2 or 3 families; never 4 independent observations without author confirmation.**
- **PMID 37583270:** none of the four WWOX rows carries the paper's "previously published" mark, and none of the four genotypes matches an individual LEGEND holds; the homozygous `c.790C>T p.Arg264Ter` is the allele seen elsewhere (Riva 2022 in compound; Piard 2019 homozygous pair) but in a different genotype or setting. Testing began in January 2018, so overlap with earlier national reports is not excluded by the source. **Count: 4, provisionally independent.**
- **PMID 27495153:** two sisters, one family; tabulated again in later reviews (PMID 35712340's Table 3 does not list them). **Count: 2 in 1 family.**
- **PMID 35712340:** one boy; the affected brother (seizures) is ungenotyped. **Count: 1 genotyped, not a WWOX-DEE case.**
- **PMID 38161429:** no new patient; its Figure 1 re-uses Iacomino 2020. Its "101" must never enter a census.
- **New individuals this wave adds to LEGEND:** 4 (Nagarajan) + 1 (Sukkar, boundary) + 1 (Serce Pehlevan, possibly already the cohort's case 49). Elsaadany's two and the cohort's two were already registered.

## 4 · Answer to the question, with its limits

**The sources do not support a single genotype-ordered spectrum on any axis except, weakly, survival — and even there they add counter-cases.**

- *Seizure onset:* predicted null/null (W44X 7 weeks; Nagarajan frameshift/nonsense 2-4 months), a homozygous SDR-region missense (L239R day 13 to 3 months) and an in-frame deletion + non-canonical acceptor genotype (2-3 months) overlap entirely. The one missense child with **no** seizures (I136V) is not evidence of a milder WWOX class, because the variant's causality is not established.
- *Drug response:* resistance is not uniform within the predicted-null class. Two W44X sisters: four failures vs partial response. Nagarajan: of three predicted null-like compound genotypes, clinical control with vigabatrin, nitrazepam and zonisamide respectively; the homozygous p.Arg264Ter child refractory including ketogenic diet. L239R: vigabatrin failed, valproate + clobazam controlled spasms. All are clinical (no EEG criterion), n = 1 per drug, follow-up 4-30 months. Response tracks neither allele class nor a drug.
- *Developmental ceiling:* uniformly profound wherever reported (W44X, Nagarajan non-ambulatory, L239R), with no class contrast available; the only "good" development is the I136V child who does not have the disease phenotype.
- *MRI signature:* thin corpus callosum and frontotemporal atrophy recur across classes (W44X, L239R); the review that claims "all affected patients" have MRI anomalies contradicts its own Piard row, and the "13% progress" figure is a denominator artefact — among serially imaged patients progression is the rule (Oliver 7/7 re-imaged; Tabarki 5/5; W44X 9 → 23 weeks).
- *Survival:* a predicted null/null genotype survived to 7 years under ventilation (W44X); no Nagarajan WWOX child had died at 6-30 months. Survival under intensive support is therefore not a clean readout of allele class.

**Independence:** of the four primary sources, two (the cohort and the L239R case report) come from one university and may share a patient; the review is purely re-description; the IESS series is provisionally independent.

**Limits.** Case reports and small series; ascertainment toward severe; clinical-only response definitions; no RNA, protein or functional datum in any of the six sources — every allele class here is predicted.

## 5 · What would change the model, and what would falsify it

- **Would change it:** an EEG-defined, genotype-stratified response table (same drug, ≥ 3 patients per allele class) — none exists in these sources; the full text of Serin 2018 describing the motor phenotype of an independent L239R carrier; author confirmation whether the 2026 case is the cohort's case 49.
- **Would falsify "allele class predicts phenotype" as used in LEGEND:** within-class discordance on a hard endpoint in independent families with measured (not predicted) allele consequence. The W44X sisters already show within-family drug-response discordance; a measured residual-function difference between the Nagarajan genotypes with no matching phenotype difference would complete the test.
- **Would rescue it:** a measured residual function for the in-frame exon 6-8 deletion or for `c.517-3C>A` that tracks the milder course of that child — not present here (that child had persistent spasms at 6 months).

## 6 · Corrections to LEGEND found after the first pass (all as candidates or notes)

- `PAPER 013`: Table 1 detail; not a "no parkinsonism" comparator; possible shared patient with PMID 42092735 (`CC-20261003W3-A-L239R-01`).
- `FT-107`, `analysis/l239r_intraallelic_comparator_20260921.md`, `analysis/wwox_neonatal_parkinsonism_audit_20260921.md`: the case report's "previously reported ... without prominent parkinsonian features" cites **Serin 2018 (PMID 30094525)**, not PMID 41153369 — noted in L239R-01, not edited (other actors' files).
- `PAPER 049`: phenobarbitone omitted; 7-year survival missing; evidence depth without a receipt (`CC-20261003W3-A-W44X-01`).
- `PAPER 046`: "101" carried as a patient count; "nega la polimicrogiria" (the review is silent); 7/13 read as a progression rate; Q230P "8 cases" provenance (`CC-20261003W3-A-BATTAGLIA-01`). Noted for the discovery ledger (not proposed): `DL-MOL-012` provenance and `DL-MECH-042`'s "first detectable sign is cerebellar".
- `DL-MECH-060` calls all four Nagarajan genotypes "null-like"; row 39 (in-frame exons 6-8 deletion + `c.517-3C>A`) is not predicted null — noted, not proposed (discovery ledger).
- `CLAIM 001`: two n = 1 vigabatrin observations in opposite directions (`CC-20261003W3-A-VIGABATRIN-01`).
- Identity records for PMID 37583270, PMID 35712340, PMID 42092735 (`CC-20261003W3-A-REGISTRY-01`).

## 7 · Where the selection's hypotheses held and where they did not

- A1: "two new patients with a coordinate-level allele" — held for the allele; "new" is uncertain because of the same-university case report. The patient-level WWOX content behind the 18 body occurrences is two table rows and three sentences; the rest are gene lists.
- A2: "exon-pair notation denotes CNVs or compound-het SNVs" — **neither, as framed:** rows 37 and 38 are two small indels/SNVs each (frameshift + nonsense), row 39 is a multi-exon deletion + an intronic SNV, row 40 is a homozygous SNV; "three of them novel" — two genotypes are fully novel, row 39's deletion is "Uncertain" and row 40 is a known rsID; "WWOX … VGB" is one child of four.
- A3: "intractable" — held for one sister, not the other (partial response); W44 lies in the first WW domain (the paper's own Discussion), upstream of WW2 and the SDR domain, so truncation would precede the SDR domain by position; nothing was measured.
- A4: "Cureus review table a double-counting hazard" — held, and worse: its table carries transcription errors; more importantly the index case does not have DEE.
- A5: "whether parkinsonian features are a vigabatrin effect" — the features precede vigabatrin (neonatal); the real confounders are perinatal injury and the untested neurotransmitter hypothesis.
- A6: "denominator per feature likely unstated" — held; the total itself is double-counted.
