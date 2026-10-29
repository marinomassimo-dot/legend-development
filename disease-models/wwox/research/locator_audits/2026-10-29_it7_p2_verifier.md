# IT7 package P2 (usable-compound census): independent verification

Verifier, 2026-10-29. Object: commit 2aea0d40, directory `disease-models/wwox/research/drug_repurposing/usable_compounds_it7_p2_20261029/`.
Method: recomputation with independent code from `catalog/catalog.jsonl.gz` and the public LINCS GEO metadata, and sampling against the
cached ChEMBL, GtoPdb and DGIdb source files. The producer's flag table was used only afterwards, to compare. The two library routines
that define "passes the catalogue's artefact rules" and the up/down action sets (`repurposing_search.artefact_reason` and its DOWN/UP sets)
were reused as the definition under test, not re-implemented; everything else (families, stated action, stable id, LINCS join) was rewritten.

## Verdict

The funnel is reproduced exactly, at record and at family level, and per record (0 of 44 211 flags differ). The M-sig definition and the
LINCS facts hold, with two description errors (below). Source-only records are correctly treated as UNKNOWN in the text, but not in the
machine-readable flag table. No sentence equates link coverage with disease treated. The access-category facts are correct. The query tool
works and is deterministic, but reports record-level flags where the census unit is the family, which produces a misleading answer for
memantine. No defect changes a headline count; the highest-ranked defects change how the counts can be read.

## 1. Funnel recomputation

| Step | Records (mine = producer) | Families (mine = producer) |
|---|---:|---:|
| catalogued | 44 211 | 40 268 |
| any target row | 24 423 | 23 425 |
| stated action before artefact rules | 16 424 | 15 508 |
| documented action (rule-passing) | 16 362 | 15 447 |
| M-net usable | 14 125 | 13 379 |
| M-sig any context | 2 478 | 2 310 |
| M-sig neural strict | 1 008 | 931 |
| overlap M-net x neural: both / only M-net / only M-sig / neither | 376 / 13 749 / 632 / 29 454 | 578 / 12 801 / 353 / 26 536 |
| overlap M-net x any context | 880 / 13 245 / 1 598 / 28 488 | 1 280 / 12 099 / 1 030 / 25 859 |

Also reproduced: families 40 268 (own union-find over ChEMBL parent, first-block key and `family_join`); full-InChIKey matches 2 068; records
with no skeleton key 28 969; 21 299 distinct compound perturbagens, 312 438 `trt_cp` signatures (205 034 + 107 404), 3 685 perturbagens with a
strict neural signature, 9 893 distinct first blocks; neural signature and compound counts per cell id (NPC 5 538 / 3 625, NEU 4 440 / 2 659,
NPC.TAK 1 207 / 212, NPC.CAS9 1 032 / 169, MNEU.E 355 / 63, FIBRNPC 1 312 / 626); 485 families with signatures in 2 or more neural cell ids,
100 with two or more concentrations at one cell and time, median 2 and maximum 99 signatures per family; every FIBRNPC perturbagen also has a
strict signature (strict = extended). Percentages in the README (33, 2.3, 5.7, 1.4) recompute. Differences found: none in any count.

## 2. M-sig definition and LINCS metadata

* GSE92742 metadata read from the on-disk copy; GSE70138 `pert_info`, `sig_info`, `cell_info` re-fetched from the GEO FTP series directory;
  all six files match their series `SHA512SUMS` (the phase II cell file is byte-identical to the phase I one).
* `SHSY5Y` is in `cell_info` (neuroblastoma, autonomic ganglia) and has no compound signature in either series: confirmed (0).
* `ASC` and `ASC.C`: primary site adipose, subtype "normal primary adipocyte stem cells": confirmed adipose stem cells, not astrocytes.
  No cell id in `cell_info` has a glioma/astrocyte/brain subtype; the only cells with primary site "central nervous system" are NPC, NPC.CAS9, NPC.TAK.
* The six strict ids are the complete neural set by `cell_info` text (NEU, NEU.KCL and MNEU.E are identified only by modification text; their
  primary site is unrecorded). Matching by first block reproduces 2 478 / 1 008.

## 3. UNKNOWN versus negative, documented action, M-net, 30-row sample

* Pilot sample of 30 signed rows (10 ChEMBL, 10 GtoPdb-claim, 10 DGIdb-other, fixed seed) checked against `mechanisms.jsonl.gz`, GtoPdb
  `interactions.csv` and DGIdb `interactions.tsv`: 10/10 ChEMBL rows match action and are Homo sapiens with a UniProt id; 10/10 DGIdb-other rows exist in
  the raw DGIdb file with the same claim source and type; 10/10 GtoPdb rows exist with a Human target, 9/10 with the same type word (one is catalogued
  "inhibitor" where GtoPdb says Antagonist; the sign, down, is the same).
* 37 ChEMBL rows have `action_type = OTHER`; they count as "stated" (so in L2) but are never signed. L2 also admits non-pharmacological action classes
  (vaccine antigen, exogenous protein, hydrolytic enzyme, chelating, sequestering).
* Source-only records: 28 969 records have no skeleton key and cannot match LINCS. The README correctly says UNKNOWN, not negative.

## 4. Access facts

openFDA NDC export `last_updated` 2026-10-27 (138 143 products) matches; DSLD `bulk_list_planned_names` 4 697 and `bulk_list_probed` 971 match the catalogue
stats; EU datasets (last modified 2024-08-13, 67 probe rows, no record-level EU category) and the Italian register (anti-bot page, not worked around,
not obtained) match the catalogue README; category counts (2 101 / 906 / 238 / 13 021 / 28 234) recompute from the catalogue. Diets: the
ketogenic-diet card is `dietary_intervention`, outside every funnel step.

## 5. Indicator definitions

Every indicator in sections 2 and 3 of the README names a unit and a denominator; overlaps are given for records and families. The phrases "not a
share of the disease treated" (sections 2, 6) and "not coverage of the disease" are present; no sentence found that equates link coverage with disease
treated. "M-sig neural coverage" in gap 1 is a share of catalogue families, as stated there.

## 6. Query tool

`need NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR`: 179 records, 173 families, 121 signed on the need target, 143 M-net, 1 M-sig neural; output ordered by catalogue id
(no ranking), byte-identical between runs. The flag `signed-on-need-target` is true exactly when some link row to a need target states up/down (121 Y, 58 n; the
n rows are unstated or modulator-type, for example piracetam, phenobarbital, CX-717), so it works as defined. `compound memantine` returns one record (see D2).

## Defects, ranked

**D1 (medium): the flag table cannot express UNKNOWN.** `record_usability.tsv.gz` gives `Msig_any_context` and `Msig_neural_strict` as 0/1 for all 44 211
records, so the 28 969 records that cannot be matched read as 0 (negative). The README says UNKNOWN, the query tool says UNKNOWN in prose, but any
consumer of the table (including the overlap "neither" cells, 29 454 records / 26 536 families) conflates unmatchable with unsignatured. Sizing of
the unknown: a name-equality probe (diagnostic only, not a rule) finds 2 001 of the 28 969 unmatchable records whose name equals a LINCS compound name,
1 215 of them M-net usable; so M-sig coverage is plausibly understated by a magnitude comparable to the matched 2 478. Only 11 899 of 40 268 families
contain any structure key, so the shares 2.3 and 5.7 percent have a denominator that includes 28 369 families that cannot be tested; a share among
families with a key (19.4 percent any context) is not given. Fix: a third state in the table; give both denominators.

**D2 (medium): the query tool reports record-level flags where the unit is the family.** `compound memantine` resolves to the free-base record, prints
"M-net=no ... missing for M-net: no target row in any source used" and "M-sig-any=yes", while its family-mate memantine hydrochloride is M-net usable and
has "M-sig-any=no" (the salt has a different first block; the family links them by the ChEMBL parent). The needs are listed "via" the family member,
but the method line contradicts the family-level picture the census counts. Same effect in `need`: M-sig flags attach to the record, not the family.
Fix: add a family roll-up line (any member M-net / M-sig) to `compound` and `need`.

**D3 (low-medium): the `need` list shows "signed" without direction.** For the "down" excitatory-gain need, positive allosteric modulators (neboglamine,
farampator, mibampator) show `signed-on-need-target=Y` beside antagonists; the compound view labels consistent/opposed/unresolved but the need list does
not. The header says "not a directional prediction", but a reader skimming Y/n can take Y as favourable. Also the list truncates at `--limit` (default 40)
without a "showing N of M" line.

**D4 (low-medium): neural-context description errors.** MNEU.E is differentiated from embryonic stem cells, not iPSC; NEU has no recorded origin;
NEU.KCL is KCl-stimulated and has 0 compound signatures (inert in the list); NPC.CAS9 stably expresses Cas9 (engineered). README section 2 and
`usable_query.py` call all of them "iPSC-derived", and gap 1 calls them "wild-type iPSC-derived cells". `cell_info` documents no WWOX status at all;
"wild-type for WWOX" is an assumption, not a source statement, and sits oddly beside "UNKNOWN genotype". Replace with "no WWOX perturbation documented; genotype UNKNOWN".

**D5 (low): wording.** (a) README gap 2 and section 3 call the 28 969 unmatchable records "source-only"; 4 691 of them are ChEMBL records without a structure
key (24 278 are source-only). (b) The ketogenic-lactate card is recorded as `dietary_intervention_plus_transport_blockade` (contains a separately
classed MCT1 blockade), not plain `dietary_intervention`. (c) "1 046 probes OK, 0 errors": the probe file keeps 36 ERROR rows, all re-probed OK;
true as final state, worth saying. (d) `counts.json` `lincs.series.GSE70138` reads "phase II (2017 expansion), same" (truncated text). (e) "Documented
pharmacological action" admits non-pharmacological classes (listed in section 3); rename or exclude.

**D6 (low): M-net includes DGIdb listing claims at face value.** 4 099 records carry usable rows from DGIdb-other (clinical-trial and cancer-knowledge-base
listings, identity "as served"; sampled examples include MAP2K4/MAP2K5 and MAPKAP1 "inhibitor" rows for kinase-inhibitor trial compounds). The README
discloses the groups and the exclusive-region table (11 848 records remain with ChEMBL or GtoPdb support), so this is a sensitivity to state, not an error.

## Not done

No live LINCS portal query; no re-derivation of the pilot's LINCS context table beyond the family statistics above; no check of the openFDA UNII
matching beyond the category totals.
