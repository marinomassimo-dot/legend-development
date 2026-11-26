# ADV-294: the ten and their queries (IT, written 2026-11-26T01:08:51Z, before any search was run)

Universe by the PREREG recipe: 132 mentioning negative sentences over 30 cards (488 negative sentences with any or no
mention). Checkpoint 26 counted 39 and 143 with an unrecorded regular expression; the difference is the recipe.
Exposure: a sentence is "shareable" when its first 100 characters occur in a shareable page; "not_found" includes
fields the pages do not render.

## Screened out under rule 4 (not a negative about a measurement or a holding)
Ranks 1 ("Access for a WWOX study: UNKNOWN."), 4 and 5 ("WWOX-DEE: UNKNOWN." in pediatric suitability), 28
(a disease context label).

## The ten (rank in universe_adv294.tsv) and the query written for each
Corpus search is case-insensitive; "near" means within 400 characters in one document.

| n | rank | card | negative claimed | query |
|---|---|---|---|---|
| N01 | 2 | F04 | Banke 2026 (PMID 40994429): supplements not held | every file name and receipt for 40994429, PMC12677382 and the DOI, all of `files/` |
| N02 | 3 | F04 | no NMDAR/AMPAR current, subunit or surface level in any WWOX system; no subunit-selective, pore-blocking, glycine-site or AMPAR drug applied to a Wwox system | wwox near (NMDA, GluN, GRIN, AMPA, GluA, GRIA, memantine, ketamine, MK-801, ifenprodil, Ro 25-6981, perampanel, D-AP5, NBQX, CNQX, EPSC) |
| N03 | 6 | E02 | the fly rescue: no Ldh-alone arm, Wwox mRNA not reported in the double line, lactate not measured in it, lifespan and amyloid load not tested | the source paper and its supplement, whole: Ldh, lactate, lifespan, Abeta load, Wwox mRNA |
| N04 | 7 | E02 | no source retrieved links an LDH inhibitor to WWOX deficiency (dated 2026-10-26) | wwox near (oxamate, stiripentol, GSK2837808, FX11, isosafrole, NCI-006, "LDH inhibit", "lactate dehydrogenase inhib") |
| N05 | 8 | E02 | the LDH lever is UNKNOWN in WWOX-DEE | wwox near (lactate, lactic, LDH, "lactate dehydrogenase"), patient measurements read |
| N06 | 16 | A01 | no enzyme and no WWOX system tested with the phenylbutyrate class | wwox near (phenylbutyrate, 4-PBA, 4PBA, phenylbutyric, TUDCA, tauroursodeoxycholic, "chemical chaperone") |
| N07 | 17 | A01 | no held measurement gives a calibrated value for Q230P, P252A or P282A | (Q230P, Gln230Pro, c.689A>C, P252A, Pro252Ala, P282A, Pro282Ala) near (activity, protein level, abundance, half-life, stability, expression, Western) |
| N08 | 18 | A01 | Johannsen 2018: no healthy fibroblast control, no detection limit, function not measured | PMID 29808465 held text and figure, whole |
| N09 | 29 | H02 | several WWOX vigabatrin reports on EB-VGB-01 describe no follow-up MRI | the reports on EB-VGB-01, each read for imaging after vigabatrin, with supplements |
| N10 | 30 | H02 | no Wwox-deficient animal given vigabatrin in any source found; survival of the neuron-specific deletion into the window not established | wwox near (vigabatrin, VGB, "vinyl GABA", Sabril); (Synapsin, Syn1, neuron-specific, Nex-Cre, Neurod6) near (surviv, died, lethal, lifespan) with wwox in the document |

Overlap check: SCI's second random 20 (ADV-287) samples fold, ratio, range and superlative statements; these ten are
negatives. H02 and A01 are also named in SCI's pending list; SCI is told which sentences these are.
