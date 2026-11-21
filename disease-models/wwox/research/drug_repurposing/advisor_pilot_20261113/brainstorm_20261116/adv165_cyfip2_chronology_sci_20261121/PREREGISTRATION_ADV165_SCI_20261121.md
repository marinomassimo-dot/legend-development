# ADV-165 pre-registration: does a microglial or astrocytic marker precede documented behavioural recurrence in the Cyfip2 R87C knock-in mouse? (SCI successor Z, 2026-11-21; hypothesis level; adjacent mouse model, not WWOX; no dose; no contact; no e-mail address to any service; reference genotype class only; not medical advice)

Fixed BEFORE the source workbook (S38) or any GEO record was opened, and before any per-animal value was seen. What had been read when this was written: the complete Ma et al. 2025 article (PLOS Biology, PMID 41066510, DOI 10.1371/journal.pbio.3003192) as the publisher's JATS XML, text, figure legends, Methods and supporting-information legends (file hash below). What that reading already told me, stated so nobody mistakes the rules for blind: the Results text reports, for hippocampal CA1 and for prelimbic mPFC, that Olig2 intensity rose at PWK 7, IBA1 at PWK 14 and GFAP at PWK 14 and 28; the authors themselves write that the intervals are broad and that the order of microglial against astrocytic activation is uncertain. So the headline timing is known to me. What is fixed here is how the per-animal values will be judged, and what the best attainable conclusion is.

## Question
Can at least one already published microglial or astrocytic marker in ONE named region be shown to PRECEDE documented behavioural recurrence, rather than appear only when recurrence is observed? (ADV-165, Codex return 06.) The answer feeds only RP-012 and RP-039 as a dated design distinction between early and late readouts; it never orders developmental events in WWOX and selects no drug.

## Source and route record
* Article text: PLOS manuscript XML route (`journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.3003192&type=manuscript`), 337,057 bytes, SHA-256 `978bba907fda01fe93b4bc38575d0308707ca7c49c2d15da65eb7cce3c8db531`. This is a complete full text (body, legends, Methods, supporting-information legends), not an abstract. Figures are images; the numbers behind them are in the supporting workbooks, which are the next step.
* Numbers: S38 workbook (DOI suffix `.s038`; sheets named by ADV: Fig1B, Fig4C, FigS8) fetched by me and hashed against Codex's value; GEO series GSE292221 (R87C) and GSE292102 (heterozygotes) by record page and file listing only; no RNA-seq download.

## Cohorts: which are distinct (from the Methods and legends; the animal is the unit only where a per-animal point exists)
| Cohort | Ages | Animals (as stated) | Measures | Seizure ascertainment |
|---|---|---|---|---|
| Survival | PWK 3 to 30 | 9 to 32 per genotype (S1 Fig legend) | lethality, begins about PWK 14 | none (death) |
| Behavioural video | PWK 14 and PWK 28, separate groups | 4 mutants per age (N1 to N4), 5-day recording, one died on day 5 at PWK 28; WT and heterozygote controls n = 4 at PWK 28 | behavioural seizure events (Fig 1B) | behavioural only, no EEG |
| Video-EEG | PWK 20 | 3 surviving mutants and 3 WT (about 80 percent of mutants were lost around surgery) | tonic-clonic and myoclonic events (Fig 1C) | the only electrographic evidence; survivor-selected |
| Immunohistochemistry | PWK 1, 7, 14, 28 (cleaved caspase-3 also PWK 20) | 7 to 9 per genotype per age (Fig 4C legend) | NeuN, Olig2, IBA1, GFAP mean intensity in CA1 (Fig 4C) and prelimbic mPFC (S8 Fig); morphology only PWK 14 and 28 | none recorded for these animals |
| Bulk RNA-seq | PWK 1, 7, 14, 28, cortex and hippocampus | per deposit: four WT and four knock-in per group (to be checked on the record page) | GSEA of cell-type gene sets (Fig 2D) | none recorded for these animals |
| qRT-PCR | PWK 1, 7, 14, 28 | 6 per genotype | microglial-activation genes (Fig 5D) | none recorded |
| snRNA-seq, proteomics, lipidomics | PWK 28 only (snRNA-seq); PWK 14 and 28 (proteome, lipidome) | per legend | state and lipid readouts | none; no age before recurrence, so not usable for chronology |
Consequence fixed now: the seizure record and the marker record come from DIFFERENT animals at every age. No marker can be tied to a seizure in the same animal. Any chronology is a comparison of age-matched GROUP differences against a group-level seizure record from other cohorts. A significant late result beside a non-significant early one is not proof that the effect started late; rule W below demands more than that.

## The four clocks (kept apart; the dataset speaks to the first only through age)
1. Gene perturbation: constitutive heterozygous knock-in, present from conception. It has no onset inside the series.
2. First seizure-like event: neonatal spasms at PD8 (about PWK 1), reported in the authors' earlier paper and restated here; not re-observed in this dataset.
3. First verified electrographic seizure: not located. The only EEG in this paper is PWK 20 (n = 3, survivor-selected); the paper states a juvenile video-EEG at PD30 showed no significant seizures (earlier paper, not read by me). No EEG at PWK 7, 14 or 28.
4. Behavioural recurrence: first DOCUMENTED at PWK 14 (behavioural video, four mice); worse and more clustered at PWK 28. Between PD30 and PWK 14 there is no ascertainment: recurrence may have begun in that window. PWK 7 lies inside it.
Therefore the reference point available is "first documented recurrence = PWK 14", not "onset of recurrence". The ages 1 and 7 are both after clock 2 (PWK 1 is the neonatal-spasm age; PWK 7 is about six weeks after it).

## Readings and what attaches to them (fixed)
* **P, precedes the first documented recurrence (weak form only):** a microglial or astrocytic marker differs from age-matched WT at PWK 7 in the named region. It can NEVER be called "precedes recurrence onset": PWK 7 has no behavioural or EEG ascertainment, and a PWK 7 change is equally readable as a late consequence of the neonatal spasms (the authors read the PWK 7 Olig2 rise that way) rather than a precursor of the adult recurrence. A P outcome says "present before the first age at which recurrence was documented, onset unascertained, neonatal clock not separable".
* **W, appears only with or after documented recurrence:** no such difference at PWK 7 and a clear one at PWK 14 or later. Even this is only "not seen at the ages sampled": PWK 7 and PWK 14 are 7 weeks apart.
* **U, timing cannot discriminate at group level.**

## Primary comparison (fixed)
Region: **hippocampal CA1** (the region the authors take forward to morphology, with the pathology; source Fig 4C). Markers: **IBA1** (microglia) and **GFAP** (astrocytes), mean intensity, PWK 1, 7, 14, 28. Two markers, so alpha 0.025 each (97.5 percent intervals). Positive control: **Olig2** in CA1 at PWK 7 (the paper's earlier lineage signal; intensity, and cell numbers kept separate if the workbook has both). Neuronal reference: NeuN (not a glial marker; shows the late-onset change timing the method can see).
Unit and test: the animal, if the sheet holds per-animal points; per age the genotype difference with a Welch interval (the authors used a two-way ANOVA with Sidak correction; I do not reproduce it). If only mean, SEM and n are given, the interval is computed from summary statistics and labelled "from summary", and the animal is then not identified.

## Decision rules (fixed)
1. **Method sensitivity gate:** the Olig2 CA1 difference at PWK 7 must be visible (97.5 percent interval excluding zero). If it is not, the data cannot show an early event at that age, and W is not allowed; the outcome is at most U.
2. **P:** for IBA1 or GFAP in CA1, the PWK 7 difference is positive with the 97.5 percent interval excluding zero, and the sign at PWK 14 is the same. Reported as P-weak with the limits above.
3. **W:** both markers have PWK 7 intervals that include zero and an upper bound below half of that marker's PWK 14 point estimate, the PWK 14 difference is positive with its interval excluding zero in at least one marker, and rule 1 holds.
4. **U:** every other combination, including a PWK 7 point estimate in the same direction with an interval that includes zero and an upper bound of at least half the PWK 14 estimate.
5. **PWK 1** differences are read as the neonatal clock, never as precedent for adult recurrence.
6. The difference of differences (PWK 14 minus PWK 7) is reported with its interval as a descriptive line; it does not enter rules 2 to 4.
7. **Secondary region:** prelimbic mPFC (FigS8 sheet), same markers and rules, to check that the call is not region-specific. If CA1 and mPFC give different calls, both are stated and the primary remains CA1.
8. **Descriptive context only (no rule):** the bulk GSEA hippocampal microglia and astrocyte gene-set enrichment by age (Fig 2D, read from the legend and text unless the workbook holds the numbers) and the qRT-PCR microglial-activation genes (Fig 5D, per-animal values only if the workbook holds them). Any gene with a PWK 7 interval excluding zero is listed as a lead for P, not counted, because many genes were tested.
9. **CLOSE or PIVOT:** per-animal points (or mean, SEM, n) for CA1 IBA1 or GFAP at PWK 7 are missing; or rule 1 fails and the PWK 7 data cannot be read; or the result changes no named LEGEND choice. The reason and the reopening input are then written.

## Limits stated now
Adjacent germline monogenic mouse model of a different disease (West syndrome); a CYFIP2 toxic gain-of-function allele, expressed mainly in neurons; two brain regions; four ages; markers are mean fluorescence intensities, not cell counts (the authors state counting was not possible); the animals that carry the marker values are not the animals that carry the seizure record; behavioural ascertainment is four mice per age and only one EEG age; the heterozygous deletion series (GSE292102) is a different allele and is used only if comparable. Nothing here changes a ranking, a compound, or the frozen WWOX forecasts, and adult recurrence in one model orders no developmental event in WWOX. Mouse, adjacent evidence.

## Rejecting observation (named in advance)
Per-animal CA1 values showing an IBA1 or GFAP difference at PWK 7 whose interval excludes zero would overturn the text reading that glial markers rise at PWK 14 and would move the call to P-weak. The same values showing no PWK 7 effect with a wide interval would show U, not W.

## Consumer
ADV (result file and path). IT only for a named decision: an RP-012 / RP-039 dated line separating early (PWK 7, the neonatal-clock-confounded window) from late (PWK 14 and after) readouts, written as a design note, not a WWOX claim.
