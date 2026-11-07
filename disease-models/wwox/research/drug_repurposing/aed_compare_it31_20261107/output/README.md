# Antiseizure comparators for the seizure-control cards (P8, IT31)

Not medical advice. No dose, schedule or preference between agents. Three columns are kept apart in `comparison.tsv` (23 rows): general activity, WWOX-specific rationale, head-to-head.

## Answer

1. DATO: the three agents act on three different targets: ethosuximide on thalamic T-type calcium currents (PMID 42536722), levetiracetam on the vesicle protein SV2A (PMID 18552880), perampanel on the AMPA receptor (PMID 24559052). Seizure types differ: absence (ethosuximide), partial and generalised syndromes (levetiracetam), adjunctive partial-onset (perampanel).
2. DATO: only ethosuximide has a WWOX-specific experiment: suppression of PTZ-provoked seizure score in Wwox-null pups (PMID 32000863, one laboratory, one experiment, no drug-by-genotype test, wild-type arm possibly floor-limited, no T-type measurement in Wwox tissue). It is seizure-susceptibility partial benefit, Track A asserted not shown.
3. DATO: levetiracetam: NONE_HELD as a rationale. It is named in about 17 A1 locator or co-therapy cells (about 16 children, 10 of them patients of PMID 36779245; re-audit correction of an earlier count of 7); outcome per drug is stated for few: ineffective in one, 'controlled on levetiracetam and topiramate' in one (second diagnosis), 'valproate and levetiracetam only' in one; no per-drug denominator.
4. DATO: perampanel: no exposure in any Wwox model; A1 lists it for two children (patients 6 and 13 of PMID 36779245; the earlier '0 rows' was wrong); ethosuximide likewise appears for patient 6. Hypothesis-level only: raised mEPSC amplitude in knockout slices, an AMPAR inference, untested (card F01); network function, not development.
5. DATO (counter): the one adult case (PMID 39507621) took all three among seven drugs (levetiracetam and perampanel are the current regimen) with no sustained effect for the seven together (n=1, polytherapy, not counted among children).
6. DATO: no head-to-head in WWOX. Outside WWOX one rat absence model compares ethosuximide and levetiracetam (PMID 21635238) and one rat status epilepticus study includes levetiracetam and perampanel alone (PMID 40198515); neither gives a ranking. NONE_FOUND for ethosuximide vs perampanel.
7. INFERENZA: a more potent or selective analogue is not better without context: the T-type blocker study states its effect is by a mechanism distinct from ethosuximide (PMID 22344687) and has no WWOX data.

## Consequences fixed in the brief
* Ethosuximide may be a candidate comparator-field row on the seizure cards with endpoint (late-phase PTZ seizure score, Wwox-null pup) and the limits in item 2.
* Levetiracetam and perampanel: the cards keep general-activity wording only; perampanel may carry the F01 hypothesis row marked untested.
* Usage percentages: none is given. Levetiracetam exposure has no denominator in A1 (the 38 / 36 children are exposed to the four coded classes, not to this drug), so any percentage for it in a consumer has no source and is removed.

## Domains and tracks
Seizure control, development, network function and behaviour are not carried across: the ethosuximide mouse paper and the rat levetiracetam paper both show seizure control without a behavioural benefit. Track A and B, partial and broad recovery stay as in the cards.

## Depth and limits
Seven new sources at abstract level only (conditional leads); module-held sources used through their manifests, not reread. Searches: `queries.tsv`. Not reached: full texts of the seven new sources, not attempted; six unshown PubMed hits of Q05 and four of Q08. Unknown is not negative.

## Re-audit (verify/audit_p8.md, blind, abstract and PMC full text)
Corrected after it: the levetiracetam and perampanel counts above; the 'not a calcium-channel/glutamate or NMDA' negatives on the mechanism rows (not in the cited abstracts, removed; perampanel's AMPA target and levetiracetam's SV2A target stand); the GIRK wording. Unverifiable from the papers: the ethosuximide limits (small groups, floor-limited wild type) and lithium-in-wild-type, which rest on the module record (needs.json), and card F04's boxed warning.
