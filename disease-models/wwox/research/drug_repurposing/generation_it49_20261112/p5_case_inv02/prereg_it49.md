# IT49 P5: generalisation case, fixed before any row of the case was read

Non-canonical working note. Not medical advice. Reference genotype class only. IPOTESI unless a line says DATO or INFERENZA. No rank, sign or qualification is changed by this case.

## Selection rule (written before looking)
The lowest-numbered investigation of `investigations_it20.tsv` that (a) has a compound or class arm (not "No compound" or "No lever"), (b) has direction unresolved, and (c) was not the subject of any IT43-IT49 case or package mapping (INV-05, INV-07, INV-08, INV-09, INV-10, INV-18 were). Only the id, rank, need and intervention title were read to apply the rule: **INV-02 (integrated-stress-response modulators, class), need NEED-ISR-ATTENUATION.** It was not used to build the IT47 or IT49 mappings.

## Arms (same inputs for each)
1. Simple target search: catalogue molecules by curated target for the ISR kinases (EIF2AK1-4), eIF2B subunits (EIF2B1-5), PPP1R15A/B and EIF2S1, by the existing catalogue tools (software, no reasoning).
2. Previous path: the INV-02 row of the ranking table and the cards it carries.
3. Path with hypotheses, context and premises: `hypothesis_package.hypotheses_for(INV-02)`, the cell-class join for the relation genes, and the premises and discriminating measures of the ISR package that exists on disk (`isrib_discrim_20261108`, not registered in the manifest).

## Predictions (fixed now)
* P1. `hypotheses_for(INV-02)` returns no rows: no ISR package is registered with a hypotheses role. The generalisation question is therefore whether a package of a new layout can be consumed by a **declarative** change only (a manifest row and a `PKG_MAP` entry); if it needs code beyond that, it does not generalise.
* P2. The cell-class join returns NOT_IN_TABLE (unknown, not low) for most of the ISR genes, because no held table queried them; any statement of "low" would be an error.
* P3. The ISR package holds premises or discriminating measures the previous path lacks (the premise that an ISR sign in a WWOX preparation is unmeasured; a phosphosite-level readout); the new path lists them with their sources.
* P4. No molecule is nominated and no direction is stated (the package row is a design, not a result).

## Outcomes that would count as failure of the capability
* A mapping that needs a code change beyond a manifest row and a mapping entry.
* A false link (a panel or screening row read as a target hit, an alias merged into an identity).
* A premise carried that the package does not state, or a direction invented.
* Arm 3 equal to arm 2 in the next experiment and in premises.

## Reference and limits
No independent reference for "the right hypotheses" exists. Any conclusion is limited to what was verified: whether the capability consumed a new layout, which premises it exposed with sources, which false links the checks found. A retrospective single case does not show predictive superiority. Independent reading of decisive propositions, if any, follows the usual producer/verifier split.
