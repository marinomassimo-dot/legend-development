# IT47 P4: result of the new case (the GSK3 / eIF2B hypotheses package, INV-09), against the pre-registration

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Nothing here nominates a compound. Pre-registration: `prereg_it47.md` (committed before the package rows were read). Blind reader: `verify/VERDICTS.md` (sonnet, high; 71 tool calls, about 217k tokens, about 10 minutes). The reader's full report was read, not a summary.

## Counts on the same data
| Measure | 1 Simple target search | 2 Previous path | 3 Path with the package and the context |
|---|---|---|---|
| Molecules or tools | 6 distinct catalogue molecules with a curated inhibitor action on GSK3A or GSK3B; 2 on IMPA1; **0 rows for the eIF2B subunits** (not a catalogued target; the eIF2B activator probe is not found by name) | the INV-09 card: a selective inhibitor beside the non-selective agent, an inositol add-back, a selectivity caveat | the package's tools named, not ranked: an ATP-site GSK3 inhibitor of a defined chemotype and a second inhibitor of a different class (three compounds are named), genetic tools, an eIF2B activator as a probe, lithium as a labelled non-specific comparator; no repurposing candidate (the package's own abstention) |
| Conditional proposals | 0 | 0 | 5 (rows H1-H5), each with a relation, prerequisites, discriminating outcomes and rival rows |
| Premises or prerequisites absent from the card | | | 7 made explicit: baseline of eIF2B epsilon Ser535 phosphorylation with total GSK3 and replicate lanes; isoform by knock-down; phospho-resistant and catalytically dead epsilon as epistasis; the DYRK2 limit of Ser-to-Ala; a phosphomimetic at 535 unvalidated; an engagement control for the eIF2B activator; the null stated before the measurement (keywords absent from the card: S535, DYRK2, baseline, E572A, S535A, replicate, epistasis, engagement, translation, IMPase) |
| Cell-class context | | | GSK3B shared in both held tables (an effect attributed to it cannot be assigned to neurons without a cell-specific control); GSK3A and EIF2B5 not queried (unknown) |
| Next experiment | a compound arm | a compound arm first | **changed in order**: baseline and isoform first, genetic epistasis second, the probe with an engagement control third, a GSK3 compound arm after; lithium only as a labelled comparator |

## What the independent reader found
* The package's decisive evidence rows (E01, E04, E06, E07, E13, E14, E15, E16) were checked against the originals: **7 supported** (E04, E06, E07 at abstract level; the others with full text and figure images), **1 partly (E15)**: the catalytically dead eIF2B epsilon removed the Gsk3b-deletion gain, but there is **no arm with the dead form in tissue with intact Gsk3b**, so a non-specific dominant-negative effect is not excluded (a premise the package missed; now on the card and in IT47-Q01). The package misworded one limit of E01 ("no n": the legend states four independent experiments; the Methods give postnatal day 14 for blots against day 20 in the legend).
* The Ser-to-Ala limit (DYRK2 at the priming serine) is supported as logic and as to the residue; that DYRK2 is required in cells rests on one open full text in cardiomyocytes; nothing in neurons or WWOX models. No Ser535-to-Asp or -Glu phosphomimetic was found (abstract-level searches): "unvalidated" stands. Numbering (human 540, mouse 536, rat 535) is consistent with UniProt (human and mouse residues annotated by similarity to rat).
* Tools: the two named ATP-site inhibitors and SB-216763 and SB-415286 are ATP-competitive; TDZD-8 is reported non-ATP-competitive at class level; LY-2090314 has only secondary support; the eIF2B activator is not a kinase inhibitor; lithium is Mg2+-competitive, inhibits GSK3 beta in cells and acts on inositol monophosphatase.
* Catalogue modality (an independent field) for the named tools: small molecules (clinical candidate, tool probe, approved) or unknown modality (no reference); none contradicts the roles; the eIF2B activator is absent from the catalogue.

## Wrong links and errors (mine and the package's)
1. **A wrong link of mine, pre-registered:** the mapping read `requires_first` as the discriminating measure. The reader (R0) shows it names a prerequisite (and holds appended audit cautions); the discriminating outcomes are in `refuted_or_replaced_by`. Corrected in the mapping; the pre-registered rows are kept in `rows_preregistered_mapping.tsv`. This is the no-value outcome "the mapping reads a cell wrongly": **met**, and caught by the independent reader, not by the tests.
2. **A prediction of mine that was wrong:** prediction (c), "the context join adds nothing", was not tested (I left the gene list empty) and is false: GSK3B is in the held tables. Symbols added afterwards and reported as such.
3. The package's own gaps: the missing control (E15), a misworded limit (E01), and four of five rows whose context cell says "as H1" (not self-contained).
4. A claim of the package that stands: the abstention (no repurposing candidate).

## Against the pre-registration
(a) five conditional rows with premise and measure: held. (b) at least one item the card lacks: held (seven). (c) context adds nothing: **failed** (GSK3B has a statement; two symbols unknown). (d) no compound nominated, no direction: held. No-value outcomes: the package added premises; the independent reader found no unsupported decisive proposition carried (one partly, now stated); the next experiment changed in order; the mapping misread one cell (met, corrected).

## What this shows and does not show
Shows: with the package consumed, a thread whose card named a compound arm now starts from a baseline measurement and from controls that the card lacked; the independent check found one package gap and one error of the mapping that the tests could not see. Does not show: a better pharmacological prediction, a favourable compound, novelty against the literature, or that the gain would persist on a case chosen by someone else; one case, chosen by a rule fixed beforehand, whose rows I had not read.

## Cost and time observed
Reader: 71 tool calls, about 217k tokens (own estimate), about 10 minutes; generator run seconds; mapping, test and dashboard rows about 40 minutes of the session.

## Limits
Reader depth is abstract for three papers; the package's author is a Scientist session and the rows are hypotheses; the context cells of four rows are references to H1; dashboard rows for H1 and H4 were added from the same mapping; translations are the assistant's.
