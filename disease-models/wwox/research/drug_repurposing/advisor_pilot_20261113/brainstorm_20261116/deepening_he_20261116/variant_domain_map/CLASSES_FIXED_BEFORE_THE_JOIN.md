# Variant-to-domain map for WWOX: classes fixed before any variant is joined (HE, 2026-11-16; non-canonical; mechanism level; reference genotype class only; not medical advice)

Written for: ADV, IT, SCI (RP-015, missense functional evidence). This file is committed BEFORE the variant table of IT's P4 step 1 is read. The map is a position join, not a reading of assays: which functional evidence exists for a variant, and in which direction, stays with IT and SCI.

## Source
UniProtKB Q9NZC7 (human WWOX, 414 residues), JSON entry as served by the public REST API on 2026-11-16 (release 2026_04), sha256 recorded in the output. Mouse Wwox (Q91WL8) has the same domain boundaries (checked in the PPxY scan). Coordinates are protein positions of the canonical isoform (NP_057457-type numbering); a variant in a coordinate system other than that of the canonical protein is not mapped (it is listed `unmapped_coordinate_system`).

## Classes (UniProt feature boundaries, fixed now)
| class | residues | UniProt basis |
|---|---|---|
| N_terminal_disordered | 1 to 15 | Region 1-23 "Disordered" up to the start of WW1 |
| **WW1** | 16 to 49 | Domain "WW 1" |
| linker_1 | 50 to 56 | between WW1 and WW2; includes the nuclear localisation signal motif 50-55 |
| **WW2** | 57 to 90 | Domain "WW 2" |
| linker_2 | 91 to 124 | between WW2 and the start of the Region 125-414 |
| **SDR_catalytic_region** | 125 to 414 | Region 125-414 "Interaction with MAPT" (the short-chain dehydrogenase-like part of the protein; UniProt gives no separate SDR domain feature, so the region boundary is used and said so) |
Sub-flags inside a class, reported in their own column and never as classes: `NAD(P) binding site 131-137` and `site 260`; `active site 293`; `mitochondrial-targeting region 209-273`; `nuclear localisation signal 50-55`; `phosphosites 12, 14, 33, 287`; `UniProt mutagenesis or natural variant at the same position` (listed with its UniProt description, so the known DEE28 and SCAR12 entries at 47 and 372 are visible; a match is a pointer, not evidence for the child's variant).

## Variant types (mapped as their own rows, never merged)
`missense` (single residue, one position); `nonsense`; `frameshift` (position of the first changed residue; downstream residues are lost: the class of the first change and "truncation downstream: SDR lost / WW2 lost" are both reported); `in_frame_deletion`, `in_frame_insertion`, `indel` (the whole span: every class it touches, as its own row, not as a missense); `start_loss`; `splice` (an HGVS c. change at an intron-exon boundary has no protein position: listed as `splice_no_protein_position`, with the nearest exon boundary only if the table gives it); `synonymous`; anything the parser does not recognise: `unparsed`, kept verbatim and never guessed.

## Decision rule for the classification
A variant's class is the class containing its position (for a span, each class it touches, flagged `spans_classes`). A position outside 1-414 is `outside_protein`. The parser reads one-letter and three-letter HGVS protein notation with or without parentheses; the first and last position of a deletion are both mapped; nothing is imputed.

## Addendum (before the join; ADV, 2026-11-16): a model-line mark
A variant identical to the one carried by a model line is marked `same_variant_as_model_line` with the line named: **p.Pro47Thr = the P47T knock-in line (GSE215425)**; ADV verified in the held Al-Baradie 2022 Table 1 that patients 1.1, 1.2 and 4 (two families) are homozygous c.139C>A p.Pro47Thr ("Missense"). The mark is a pointer to a model, not a claim about protein state: for these children the protein state is not stated in the held record. The I8 wording is corrected accordingly: not "WW1 with protein: empty" but "no held child with WW1 variant AND protein stated present; three children carry the P47T variant, protein state not stated".
