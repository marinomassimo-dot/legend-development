# IT43 P3: what the path produced for S9 (PDK inhibition), and where it stopped

Non-canonical working note. Not medical advice. Search run through the unchanged path (`action_search.py` with the relation file `relations_it43.tsv`; two env variables select input and output folders). Rows in `s9/search_rows.tsv`, `s9/molecules.tsv`.

## What the path returned (10 source rows, 3 molecules, all verdict CANDIDATE with no unknown field)
| Molecule | Source and action | Isoforms with a row | Affinity as recorded | Limit |
|---|---|---|---|---|
| dichloroacetate (sodium salt) | ChEMBL curated mechanism, inhibitor, family record (isoform unresolved) | PDK1-4 as one family record | none | a granularity, not selectivity; weak, pyruvate-analogue class (INFERENZA from the card chain, not a row) |
| AZD7545 | GtoPdb, inhibitor, human | PDK1 7.43, PDK2 8.19 (pIC50) | one biochemical enzyme assay (PMID 14641019) | PDK3 and PDK4 have no row: unknown, not zero |
| VER-246608 | GtoPdb, inhibitor, human, "family selective" | PDK1 7.46, PDK2 7.08, PDK3 7.40, PDK4 7.04 | one in vitro functional assay (PMID 25404640) | a different assay from AZD7545: the two sets of pIC50 are **not** compared with each other |

## Classification of what emerged (four classes kept apart)
* Known in WWOX: the lever (dichloroacetate and PDK inhibition) is the carded chain of INV-07 and card E03; its direction is unresolved because the kinase transcript is lower and the one PDH activity measurement shows no difference.
* Known in the repository: AZD7545 and VER-246608 already sit in card E03's endpoint ("PDK2 inhibition by AZD7545 or VER-246608") and in the IT10/IT21 candidate tables.
* New combination for LEGEND: none. Transferred hypothesis: none. Novelty verified in a stated search: none claimed.
* **What changed:** in the IT21 generator both compounds were listed as `unsigned_or_no_signed_direct_action` with identity unresolved (a family entry from a listing). The relation path gives each a typed, human, per-isoform inhibitor row, so the old exclusion was an artefact of reading only a listing (a false exclusion, corrected at the path level, not a new compound).

## Chain and comparison (conditional)
Relation S9 -> three typed molecules -> role by the comparison engine rules: the reference is dichloroacetate (the carded functional lever, no isoform data); the mechanism discriminator is VER-246608, a second chemotype with rows on all four isoforms; AZD7545 is an isoform-bias probe (PDK2 above PDK1, PDK3/PDK4 unread). All three stay **conditional**: the first decision is the premise (INV-07), not the molecule.
* Premise still needed: is PDH reduced in a WWOX-deficient human neural cell (flux with lactate, pyruvate and redox state measured directly)? Direction unresolved; an unrecorded isoform is not an absence.
* Discriminating experiment (after the premise): the same readout with the reference and a second chemotype; agreement supports a PDK-dependent effect, disagreement points to a compound-specific action. PDH phosphorylation as a target-engagement readout is INFERENZA from the card.
* What would raise or lower the lead: a measured PDH restraint raises it; no restraint (the available sign) lowers it to a premise-failed state without refuting the relation in other cell types; a lactate-supply role of the lineage reopens it with opposite sign.
* Stop point of the path: no row says a molecule reaches the brain or acts in neurons; exposure and cell-type expression of the four kinases are not in the sources read. Implementable gap: the kinase expression per cell type (a reading task, zero spend), recorded as open question IT43-Q02.

## Addendum (same day): what the DGIdb listing path adds to S9 (`dgidb_rows_it43.tsv`)
Six DGIdb-only records are new against the typed search; none has a typed PDK-inhibitor action from a source that gives one beyond the three above, and every row stays UNKNOWN (`listing_only`).
* **Same molecule, unreconciled name.** "Dichloroacetic acid" (a DTC listing) is the acid form of the typed sodium salt; the salt-stripping key does not join them. An identity reconciliation to make, not a new molecule.
* **A gene-symbol trap (INFERENZA, not read in a primary source).** The symbol PDK1 is also the historical symbol of a different kinase (3-phosphoinositide-dependent kinase 1; current symbol PDPK1). Listings of other compounds against "PDK1" through DTC, PharmGKB and a clinical-trial source may concern that kinase, not the pyruvate dehydrogenase kinase; they must not enter the S9 comparison without a check of the target in the source.
* **A listing that could be read the wrong way.** A lipoate-analogue clinical compound is listed against all four kinases through a clinical-trial source; the listing carries no direction, and the independent reader found abstracts giving its targets as the dehydrogenase complexes themselves (pyruvate and alpha-ketoglutarate dehydrogenase) and the kinases only as a hypothesis through raised PDH phosphorylation: not a kinase inhibitor on that evidence. Kept UNKNOWN; no direction is taken from a name or class.

## Independent reader (sonnet, high; `verify/VERDICTS.md`), corrections kept
* The two affinity sets are not shown comparable (one is a DELFIA enzyme assay on an E1 substrate; the other assay was not reached); substrate changes the answer for lipoamide-site compounds. The VER-246608 pIC50 values are one datum each (Table 1 IC50 values reproduce them).
* AZD7545's abstract names no isoform and gives no figure; the species recorded as human is not supported (indexed to the rat); the PDK3/PDK4 gap stays unknown.
* Celecoxib and OSU-03012 are reported as inhibitors of the other kinase (PDPK1): the symbol clash is confirmed for those rows (HGNC lists PDK1 as an alias of PDPK1). No prose sentence stating the clash was found.
* The MELAS trial figures are confirmed at abstract level (30 randomised; 15 of 15 against 4 of 15 stopped; 17 of 19 discontinuations for neuropathy; efficacy not judgeable); the arm split of the 17 is not given.
