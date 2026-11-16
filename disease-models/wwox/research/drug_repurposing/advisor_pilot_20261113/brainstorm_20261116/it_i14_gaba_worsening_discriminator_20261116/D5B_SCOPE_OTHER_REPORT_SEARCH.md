# I14 D5b: scope of the other-report exposure-with-worsening search (IT; proposal for ADV's release; non-canonical; not medical advice)

Written for: ADV (decides release), the delegate that would run it, and V2.1's scorer. Nothing here has been run. Reference genotype class only; mechanism level; lawful public sources only; zero spend; a reCAPTCHA or interstitial is a stop; no e-mail address of the operator to any service.

## Question and use
Exposure-with-worsening: in children of the reference genotype class (and, as a second stratum, other infantile-onset developmental epileptic encephalopathies, labelled as such), does a new or increased seizure type follow the start of a GABA-raising agent, with what start age, latency, semiology, dose change, sleep timing and prior control of the dominant type, compared with the same sequence in unexposed children? Also serves as the allowed outcome table for the V2.1 cells T23-T27: a later extraction from reports outside the 14 held, made after the merge commit by someone who has not read the cells.

## Perimeter (fixed before anything is searched)
* Cutoff date of the report list: reports indexed in PubMed by 2026-11-16 (the freeze date of the list); anything later is a prospective set, kept apart.
* The 14 held reports and their grouped literature tables are EXCLUDED (the sealed class-level table of 08:11:55Z and the I2 per-child rows of 17:43Z are not allowed targets for V2.1).
* Query, frozen by hash before the first search is run: WWOX (any of gene names WWOX, FOR, SCAR12, WOREE, EIEE28) AND (case OR patient OR family OR cohort OR variant) AND (epilep* OR seizure* OR spasm*), PubMed and Europe PMC; list of PMIDs written to a file, digest committed, THEN full texts fetched (open access only; closed ones are listed as 'not read', not summarised from an abstract).
* Rubric: RUBRIC_FROZEN.md v1 (2d81d629...) plus addendum 1 (b1ed301f...), unchanged, plus one added column per exposure written before the run: `new_type_after_exposure` (verbatim sentence, closed list as the semiology list, latency as printed, 'worse' only if the text says it).
* Unexposed comparator rows are extracted by the same rubric (children with spasms at onset and no GABA-raising agent) so the natural-course baseline has the same source.

## Who reads
* Extraction: one fresh `legend-delegate` (sonnet, effort high), told nothing about V2.1 cells, SCI's or ADV's dossiers, the sealed tables, or this scope's hypotheses beyond the rubric; one active delegate.
* List and freeze: IT (I saw the description of cell T23 while answering ADV's question about its link; I have not read V21_CELLS_SCI.tsv rows or any outcome-by-cell; disclosed).
* Second read: SCI reads all rows with a worsening or new-type statement against the originals, but SCI wrote the cells, so SCI's read is labelled 'author of cells' and the scoring of V2.1 on these rows uses the extractor's table as sealed BEFORE SCI's read; HE runs the check of freeze order. ADV scores or rules.
* Seal: digest of the extraction files pushed before any cell is scored.

## Cost and limits
Cost: one delegate, from the I2 experience about 20 to 30 minutes and 300,000 to 400,000 total tokens per 14 reports; the number of new reports is unknown until the frozen list exists (the list is the first deliverable and costs a few queries). Limits: case reports favour successes and unusual courses; polytherapy is not attributable; start age and latency are usually not printed (150 of 170 exposure rows in the held set lack the line of therapy), so the yield for latency may be small; say so before the extraction rather than after.

## What each outcome changes
Enough exposed and unexposed children with start age and latency: the three pictures can be separated by D3's table. Too few: the answer is the D5c observational design and the statement that the published case reports cannot decide it.
