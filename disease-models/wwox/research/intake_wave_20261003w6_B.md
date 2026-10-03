# Intake wave 6 — 2026-10-03 — Scientist B: IESS / DEE denominator-and-management literature

**context_policy:** `SOURCE_FIRST` — each source was read (JATS body, tables cell-wise, legends, the one reachable supplement) before any registry record, ledger lead or held dossier was opened. Before reading I knew only identity, acquisition state (`paper_packet.py`: identity none, receipts 0, for all six) and the group question. Held sources were opened afterwards, only to test patient overlap.
**ACTOR_ID:** `scientist` (Scientist B), branch `task/sci-B-20261003w6`. **Not medical advice.**

## Question (from the selection record, group B)
What does each source add to, or limit in, a genotype-stratified statement about how WWOX-DEE patients are counted and how they respond to treatment? How many WWOX patients does each contain, whose are they, and does it report a response or only an etiology?

## Per paper

| PMID | Verdict | WWOX patients in source | Whose | Response or etiology? | Receipt file |
|---|---|---|---|---|---|
| 40126049 Cerulli Irelli 2025 | **INGEST** | 3 (Table 2) | the study's own, alleles not printed; overlap with held cases undetermined (INFERENZA) | **response** (CBD, last follow-up) | `sciB_40126049_1.json` |
| 40019827 Innes 2025 | INGEST (re-tabulation) | 4 + 1 re-tabulated | 4 = PMID 37583270 (held, receipt-complete); 1 = PMID 29455050 (unread) | etiology only | `sciB_40019827_1.json` |
| 39850204 Zhu 2025 | INGEST (denominator) | 1 of 361 | own; no allele | etiology only | `sciB_39850204_1.json` |
| 38540325 Snyder 2024 | OFF-AXIS for WWOX (gene-list only) | 0 | — (uncited list entry) | neither | `sciB_38540325_1.json` |
| 40217411 Yuan 2025 | INGEST (with a do-not-count rule) | 18 pooled | unnamed primaries — cannot be de-duplicated | phenotype only | `sciB_40217411_1.json` |
| 42068099 Mohammad 2026 | INGEST (with a do-not-count rule) | 0 own | four rows all citing PMID 36779245 (held; PUBLICATION_INTEGRITY_HOLD) | phenotype only | `sciB_42068099_1.json` |

Dossiers: `research/fulltext_dossiers/PMID<pmid>.md`. Manifests: `research/deepdive_manifests/PMID<pmid>.json` (all six PASS `--verify-artifacts --require-current-schema`). Every reading is `partial_fulltext_read` (see "What was not read").

## Answer to the assigned question
1. **A genotype-stratified *response* statement naming WWOX now exists — and it is three patients.** PMID 40126049 Table 2: WWOX (3 pts), mean seizure reduction 41.7 % (SD 38.2), ≥ 50 % responders 2/3, CGI-I improved 2/3, at last follow-up on >99 % purified CBD added to a median of three ASMs. Denominator 3 for each fraction. Response = ≥ 50 % reduction in monthly seizure frequency versus the 3-month pre-CBD baseline, from diaries/records; CGI-I scored retrospectively. Nothing else about the three is printed. **Limits:** n = 3; open-label; adjunctive; no comparator; follow-up length unknown; ages unknown in a cohort whose median age at CBD is 12 years (survivor selection likely in a disorder with early mortality — INFERENZA); the authors themselves say rows of two or three may be chance. It supports "three WWOX patients were recorded with these outcomes", **not** "WWOX-DEE responds to CBD", and says nothing about any allele class or the reference genotype.
2. **Are the three held patients?** Undetermined. No held WWOX source is cited. Oliver 2023 (4/4 CBD *continuation*, not response) shares no named centre. Riva 2022 (one case, "CBD oil" ineffective) shares three authors and a contributing centre but names a different product. Both overlaps are INFERENZA. Rule adopted: count the three **once, as an unlinked aggregate**, never summed with held per-patient CBD observations.
3. **Counting.** Of the six sources, only two contain WWOX patients of their own (40126049: 3; 39850204: 1). 40019827 re-tabulates five (four already held, one unread primary). 42068099 re-describes one held cohort four times. 40217411 pools 18 from unnamed primaries — uncountable. 38540325 has none. Net new WWOX patients after de-duplication: **at most 4** (3 CBD + 1 IESS), each with no allele and each with overlap against held cases undetermined.
4. **Response vs etiology.** Only 40126049 reports a response. 39850204 measures response but stratifies only ACTH vs non-ACTH and etiology groups; 40019827 and 38540325 give unstratified ranges.

## What would change the model if true, and what would falsify it
- *If* a WWOX-specific CBD effect were real, a per-patient series with allele class, age, baseline and a fixed time point (e.g. 3 and 12 months) should show ≥ 50 % reduction in roughly the same proportion as the three here; a second real-world cohort with WWOX rows showing 0/n responders, or the authors' individual-level data showing the two responders were short-follow-up or co-started another ASM, would falsify the reading of this row as a signal. Neither changes the working model now: MINOR annotation only.
- Asking the authors (data-availability statement allows qualified requests) for the three rows' allele class, age and follow-up is the one action that would turn this from an aggregate into evidence. Not done (§21d: outreach is not mine to send).

## What the brief/selection record got wrong (tested against source)
- 40126049: the WWOX row is *not* "responder counts at two timepoints"; columns are mean reduction, ≥ 50 % responder rate and CGI improvement, all at last follow-up.
- 40019827: the two WWOX rows are *not* plausibly the same patients — two different cohorts (124-child confirmed-genetic cohort; 128-child panel cohort) from different groups.
- 40217411: WWOX is *not* in the chorea set (Table 1 or 2); the "chorea" reading is a flattened-text artefact. It *is* in dystonia, myoclonus, ataxia, tremor and hypokinesia.
- 42068099: there are **four** WWOX rows (white matter changes is the fourth), not three; WWOX occurs 6 times in the XML (4 rows + 2 in the ref-66 title), not 5.
- 39850204: the "enzyme-synthesis" class is an unassayed, unreferenced authorial grouping (it also includes MECP2).
- The "neonatal hypokinesia only with WWOX" framing (PMID 33919646) is **not** repeated in its 2025 successor; it has broadened.

## Reading-debt discharge (correction 15)
None of the six was a cited-and-unread primary behind an existing registry statement (no PAPER/LIT record existed). New debt created: Ko 2018 (PMID 29455050), the primary of a single WWOX patient, queued in the 40019827 manifest.

## Candidates
| id | class | triples |
|---|---|---|
| `CC-20261003W6-B-CBDRESPONSE-01` | MINOR (annotation on `DL-MECH-030`) | 6 |
| `CC-20261003W6-B-MOVEMENT-01` | MINOR (annotation on `DL-MECH-030`) | 7 |
| `CC-20261003W6-B-REGISTRY-01` | MINOR (`PAPER 151`–`156`, `LIT-0444`–`0449`, provisional) | 5 |

## What was not read (all six are `partial_fulltext_read`)
- Figure panels were not inspected as images for any paper (legends read). For 40126049, Figure 1 was viewed once; this session was then halted by a model safety classifier, and per corrections 13/21 I did not reopen the image. All later extraction used scripts that print narrow slices. Counts carried rest on tables and text, not panels.
- Supplements: 40126049 Appendix S1 read in full (text). 40019827 and 42068099: the Europe PMC supplementaryFiles stream was truncated (not a valid zip) on each attempt. 40217411: HTTP 500. 39850204 and 38540325 have none.
- The long mechanistic sections of 40019827, the background sections of 38540325 and the non-WWOX sections of the two movement reviews were read at section-head and keyword level.

## Halt record (correction 13)
A safety classifier halted the model once, immediately after the Figure 1 image of PMID 40126049 (a bar chart of patients per gene) was displayed. I did not reword or repeat that read. The figure carries nothing beyond Table 2 for WWOX.
