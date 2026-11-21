# ADV-137 / RP-039 pre-registration (IT, 2026-11-21), committed BEFORE any retrieval for this question

Reference-genotype class only; hypothesis level; a transfer question about OTHER early-onset epilepsy models, never Wwox evidence; no dose, no schedule, no recommendation; nothing here is medical advice; aggregate published literature only.

Limit stated first: every reader here is a model of the same family; no specialist has read a source. The assignment text is ADV's message of 2026-11-21 (the file `assignments/ADV-137.md` lands with ADV's next push; this note quotes the message).

## Question
In published early-onset epilepsy models other than Wwox, are glial or energy readouts (histology: GFAP, Iba1 or equivalent; marker: transcripts or protein of glial identity or activation; metabolic: lactate, glucose uptake, FDG-PET or equivalent) already different from wild type at ages BEFORE the first documented seizure, with age, denominator, n, significance and marker-versus-function stated per row?

## Exclusion (ADV's, registered before ADV-115 was opened)
No GEO or public-transcriptome route (ADV-115: 19 series inspected, none usable; near-miss GSE112627 run as ADV-116: Scn1a het at P14, no glial or energy set difference). This work reads papers only.

## What is already held (counted read first)
ADV-104 (no glial measurement before P14 in any held Wwox line; earliest documented seizures P9 for the neuron-targeted line), ADV-105 (energy supply after onset), ADV-101 (glucose before P10 absent; the null's growth lag from day 4), ADV-115/116 (public transcriptomes). The counted read is recorded in `HELD_READ_ADV137_IT_20261121.md`.

## Sign prediction, fixed now (before any retrieval)
My prior, stated as a prediction that can be wrong: **in most early-onset genetic epilepsy models a glial histology or marker measure is NOT yet different from wild type at an age that precedes the first documented seizure, and the glial change appears at or after onset**; the exception class is a model whose primary lesion sits in a glial or metabolic gene (a different question, and listed apart). For metabolic readouts I expect no prediction better than "unknown": a pre-onset FDG-PET or lactate change is plausible where the lesion is metabolic and unlikely where it is a channel or synaptic lesion.

## Definitions (fixed now)
1. **Model:** a published animal model (mouse, rat, zebrafish excluded unless it reports histology or metabolic readouts at stated ages) of an early-onset genetic epilepsy or developmental and epileptic encephalopathy, other than Wwox; acquired models, adult-onset models, cell cultures and organoids do not count.
2. **Qualifying row:** one model, one readout, one age, with (a) a documented age of first seizure for that model stated in the same paper or in a paper it cites for that purpose, (b) the reading age strictly earlier than that age, (c) a genotype-against-wild-type contrast with n per arm stated, (d) the paper's own statement of significance or of no difference.
3. **Pre-onset:** the reading age is earlier than the first documented seizure age by the paper's own statement. A reading "at onset" or an undocumented onset does not qualify and is listed apart.
4. **Marker versus function:** a row is `MARKER` when the readout is a stain, transcript or protein; `FUNCTION` when it measures a physiological property (uptake, lactate, flux, PET). Never merged.
5. **Independent models:** different genes (or different, independently generated alleles by different laboratories). Two papers on one allele count once.
6. **Absence claim:** needs two routes (PubMed and Europe PMC full-text search); a challenge page is a STOP for that route, recorded as the route result.

## Rejecting observations and what each does (ADV's, made operational)
* **RISE:** at least 2 independent models with a significant rise of a glial or energy readout in a qualifying row (same direction as the glial arm's pre-onset test status) = the pre-onset test status is kept with the stated sign prediction (a rise before onset), and the sign prediction above is FALSE.
* **FLAT or LOWER:** at least 2 independent models with a stated no-difference or a decrease in a qualifying row and none rising = the glial arm moves toward "consequence of seizures"; the sign prediction above is TRUE.
* **CONFLICT:** qualifying rows of both kinds = R3 with the conflicting rows.
* **THIN:** fewer than 2 independent models with qualifying rows in either direction = a named missing measure, stated per readout.

## Method
1. Counted read of the held notes (done first, persisted).
2. PubMed (field-tagged queries) and Europe PMC full-text search for the model genes of early-onset epilepsy (Scn1a, Scn2a, Scn8a, Kcnq2, Kcnq3, Stxbp1, Cdkl5, Syngap1, Gabrg2, Gabra1, Grin2a, Grin2b, Depdc5, Tsc1, Tsc2, Mecp2 where seizures are reported, Arx, Pcdh19, Slc6a1, Gnao1, Dnm1, Kcnt1, and others the first queries surface) crossed with GFAP, Iba1, astrocyte, microglia, gliosis, lactate, glucose uptake, FDG, PET, metabolic, and ages (neonatal, P5, postnatal, pre-symptomatic, before seizure onset); candidate papers listed with the queries and hit counts.
3. Complete reads (receipt with verbatim locators) of the papers whose rows carry the statement; a producer delegate (model and effort stated and read back; one at a time, none recursive) reads the candidate papers into a row table; a blind verifier receives the rows' sentences and sources, never the conclusions.
4. Plain clients only (no browser-header spoofing, no contact-address service, the operator's e-mail never sent anywhere); a challenge page is a STOP for that route.

## Output
`RESULT_ADV137_IT_20261121.md`: answer first; the counted held read; the queries and hit counts; the qualifying rows (model, gene, readout, class marker or function, age, first-seizure age and its source, n, significance, direction, reading depth); rows not qualifying and why; the verdict (RISE, FLAT or LOWER, CONFLICT or THIN) with the prediction's outcome; marker-versus-function separately; counters (a null in a small n is not absence; seizures at onset may precede the first video-EEG; a pre-onset age in a model whose onset is only inferred; adult-onset or acquired models excluded); delivered to ADV and SCI.
