# L-leucine · re-extraction of the fly knockdown spectra

26 November 2026 · SCI_CODEX

## Attribution and quality controls

In each published polarity assay file, all **40** experimental identifiers match the sample sheet through both MS Assay Name and Extract Name, and their prefixes match the raw and converted spectrum filenames. For all 40, the assay row's separate Sample Name field differs. The two polarity tables contain the same conflict. This recovers an explicit deposit-based crosswalk, without independently verifying the labels against lab notes. The earlier report identified the field conflict and could only infer candidate filenames. [Earlier field audit](fly_feature_20261126.md) · [Resolved deposit crosswalk](fly_assay_crosswalk.tsv)

The positive-mode mzXML extraction used the standard-assigned mass **132.1019**, a **±5 ppm** window and a **30 s** integration around the maximum of the mean pooled trace. The apex was **607.7 s**, **20.5 s** later than the deposited annotation. The pooled median area was **95.9 times** the blank median. Spearman agreement with the deposited areas was **0.839** over 12 pooled spectra, meeting the prespecified 0.70 gate. Agreement within the two six-pool label sets was weaker (**0.314 and 0.371**). No secondary maximum above the prespecified threshold was resolved within the integration window. The retention offset, weaker within-set agreement and potential co-elution of structural isomers qualify the chemical assignment. The effect below is for the extracted, standard-assigned feature, and requires targeted confirmation to call absolute L-leucine. [Prespecified gates and scope](fly_reintegration_pretest_20261126.md) · [QC areas and spectral checksums](fly_leucine_qc.tsv) · [Quality summary](fly_leucine_qc.json) · [Public deposit](https://www.ebi.ac.uk/metabolights/MTBLS12344)

## Result

Ratios are geometric means for knockdown divided by matched RNAi control within each background, with **five replicate pools of ten fly heads per arm** as reported by the study. The one-pool omission ranges are sensitivity checks, not confidence intervals.

| Fly background | Raw area ratio and omission range | TIC-normalized ratio and omission range |
|---|---:|---:|
| LacZ | 1.094 (0.913–1.244) | 1.152 (0.976–1.300) |
| Aβ42 | 0.528 (0.485–0.591) | 0.548 (0.504–0.615) |

In LacZ the estimated effect is below the 1.25-fold practical threshold at the primary window, and the omission sensitivity crosses unity. In Aβ42 the decreases survive one-pool omissions, both normalizations and both adjacent windows. The unadjusted within-background exact permutation P values are 0.746 and 0.0159 for raw area. Exchangeability across independently processed pools is unverified, and the permutations do not test a genotype-by-background interaction. Aβ42 exposure and the fly's age and pooled tissue prevent interpreting the difference as a pediatric neuronal substrate deficit. It remains possible that technical run factors contribute to the across-background contrast. [Sample-level values](fly_leucine_sample_areas.tsv) · [All contrasts](fly_leucine_contrasts.tsv) · [Spectrum digests](fly_leucine_sample_inputs.tsv)

## Decision

Park L-leucine for an unselected pediatric WWOX trial. The fly observation supports a **conditional response under additional stress** as an assay hypothesis. The standard-assigned feature does not show a comparable decrease in the LacZ condition. The human one-library CAGE sensitivity also leaves the previously seen charging-enzyme signal unresolved. Reopen for a stage-matched WWOX neuronal experiment with matched baseline and demand. Test whether a measured decline in free leucine and charging can be reversed above a replete baseline at comparable ATP and preserved recovery. An intact charging response with reduced labelled oxidative product at matched α-ketoisocaproate would instead place the bottleneck downstream. [Human CAGE comparison](neural_cage_interpretation_20261126.md) · [Charging controls](charging_capacity_20261126.md)

To reproduce, run `python3 -B fly_leucine_eic.py SAMPLES_JSON POSITIVE_ASSAY_JSON NEGATIVE_ASSAY_JSON OUTPUT --maf ASSIGNMENT_TSV --spectra POSITIVE_MZXML_DIRECTORY --compare`. The metadata JSON endpoints, original tab-delimited MAF and hashes are listed separately. Each positive file is under `FILES/DERIVED_FILES/Positive/STEM.mzXML` in the public FTP study directory. The script writes results for experimental pools only when the pooled control passes the prespecified gate. [Input metadata](fly_leucine_metadata_inputs.tsv) · [Script](fly_leucine_eic.py) · [Primary study](https://doi.org/10.1093/braincomms/fcag385)
