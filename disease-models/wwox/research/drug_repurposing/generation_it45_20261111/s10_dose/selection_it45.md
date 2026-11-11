# IT45 P2: S10 (KEAP1/NRF2) pointers chosen before any document was opened

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Written 2026-11-11 after the dose-response read and before the primary documents were opened.

## What was read, and what IT44 had
* Frame, relation row and the competing explanations H1-H6 are the IT43 ones (`../../generation_it43_20261110/fourth_relation_it43.md`, `s10/relations.tsv`): the frame was written before any name and is not re-written.
* IT44 read for the three S10 targets: five activity types, `max_pages=5`; the NFE2L2 target was TRUNCATED at 5,000 rows (Harness HE45 count: 93,391 rows, 92,628 of type Potency) and no catalogue-status molecule of S10 reached `pointers_it44.tsv`.
* IT45: the four dose-response types (IC50, EC50, Kd, Ki) read alone, `--max-pages 20`: all three targets COMPLETE, 1,587 rows, 1,281 molecule x relation rows, **10 with a catalogue status** (`activity_molecules.tsv` here). Verdict of every row: ACTIVITY_ONLY. The Potency screen is not read in this run (separate read, own coverage; not needed for the question).

## Selection rule (fixed before reading; not potency order)
1. pertinence to the one thing the frame says is missing: a reagent that can separate H5 (benefit independent of NRF2) and a KEAP1-directed compound of a different binding mode from the covalent forms;
2. same document or same assay for the compounds that are to be compared (comparable conditions are possible only there);
3. an opposite-action row or a possible wrong-target row (kept, not dropped);
4. a primary source that is reachable (a ChEMBL document with a PubMed id and DOI).
A review document is a pointer to its own primary sources, not a source (halofuginone row). Lowest nM was not used.

## The ten catalogue-status molecules and the document each row comes from (ChEMBL document records)
| Molecule (catalogue name) | Row type on target | Document (PMID) | Why it is, or is not, in the reading set |
|---|---|---|---|
| sulforaphane, dimethyl fumarate, monomethyl fumarate | EC50 NFE2L2, reporter or translocation, human U2OS cells | 37187090; 38116420 | rule 2: three compounds in one assay system; the parent ester and its circulating form side by side |
| non-covalent KEAP1 binder (catalogue: tool_probe) | Kd, Ki, IC50 KEAP1, recombinant protein | 27031670; 31411465 (a comparative assessment of known Keap1-Nrf2 protein-protein-interaction inhibitors) | rule 1: the different-binding-mode compound; rule 2: a comparison done in one laboratory |
| bardoxolone methyl; bardoxolone (acid) | EC50 NFE2L2 (methyl ester); Kd KEAP1 (acid) | 28753294; 37386884 | two catalogue entries for two structures; potencies from different systems must not be merged (rule 2 fails across documents) |
| curcumin, resveratrol | EC50 NFE2L2, ARE reporter | ChEMBL documents CHEMBL3286393, CHEMBL4138237, CHEMBL3877327 (no PubMed id read yet) | in the set only if the first four questions leave room; electrophile or promiscuous behaviour is expected, to be read |
| halofuginone | IC50 NFE2L2 in two cancer cell lines | 39241669 (a review) | rule 3: opposite action; the primary source is wanted |
| molibresib | IC50 > 10,000 nM, KEAP1 | 21964340 (a BET-inhibitor paper) | rule 3: possible wrong-target row; check whether the paper measured KEAP1 at all |

Selection made first (this file); document reading follows in `../verify_s10/`. Nothing here nominates a compound for use; an EC50 on a reporter is an activity, not an action on KEAP1, and not a benefit.
