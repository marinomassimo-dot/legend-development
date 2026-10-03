# CC-20261003W3-C-RESTORATION-SPEC-01 — what a WWOX-restoration strategy can and cannot specify today

- `context_policy: SOURCE_FIRST`
- Sources: PMID 40349107 (`FTR-20261003-40349107-01`), PMID 39847501 (`FTR-20261003-39847501-01`),
  PMID 40263630 (`FTR-20261003-40263630-01`), PMID 42181696 (`FTR-20261003-42181696-01`),
  PMID 42521212 (`FTR-20261003-42521212-01`). All five manifests validate (`--verify-artifacts`,
  VERDICT: PASS). **None of the five mentions WWOX.** Every statement below is a transferable lesson
  from another gene with its transfer limit stated, as the brief requires.
- Change class: **MINOR**. Nothing here narrows or reverses a `consolidated baseline` claim; it adds
  one research-line record and one dismissal-ledger negative, both in the research layer, and both
  are statements about **what is not yet specifiable**.
- **Nothing here is medical advice.**

## The finding, in one sentence

Of the six parameters a WWOX-restoration strategy would have to fix — how much protein, in which cell
types, by what route, inside what window, with what off-target organ risk, measured by what
pharmacodynamic assay — the 2025–2026 DEE gene-therapy literature **measures route, cell-type reach
and off-target organ risk well, measures dose only as vector genomes and not as rescued protein,
does not measure the window at all, and has no WWOX-specific pharmacodynamic assay** — and the one
paper that did measure the protein found the therapy worked **without raising it detectably**.

## Parameter by parameter, with the transfer limit on each

| Parameter | Best measurement in this set | Transfer limit to WWOX-DEE |
|---|---|---|
| **Dose** | PMID 40349107: mouse 1E10–1E11 vg/animal ICV at PND1, dose-dependent rescue, brain STXBP1 rising from ~0.4 to ~2.2 ng/µg; NHP 1E14 vg/animal. PMID 39847501: 1.1–1.7E11 vg/mouse at P2. PMID 42181696: 1E10–1E11 vg/mouse, **non-monotonic** | Vector genomes do not transfer between genes, capsids, promoters or species. What transfers is the shape of the problem: in two of the three, the **highest dose was not the best dose** |
| **Cell type** | PMID 40349107 quantifies excitatory vs inhibitory coverage per promoter (STXPro5 51 %/35 %, Syn1 and CB biased excitatory). PMID 39847501 gives PV 46 %/36 %, SST 64 %/51 %, VIP 8 %/18 % coverage from a Gad1-promoter construct | Transferable as method and as the warning that "pan-neuronal" promoters are not pan-neuronal. WWOX's required cell set is **unknown**: the repository has no measurement of which neuronal or glial populations need WWOX restored |
| **Route** | ICV, bilateral in neonatal mice, unilateral in NHP (2 mL at 0.1 mL/min after MRI-guided stereotaxy); ICV + IV when a peripheral organ is implicated (PMID 42181696); intrathecal lumbar for an oligonucleotide in a preterm infant (PMID 40263630) | Route transfers best of the six, because it is set by anatomy and by the capsid, not by the gene |
| **Window** | **Not measured anywhere in this set.** PMID 39847501 looks like a window result and is not: the authors attribute the P10 failure to transgene level and distribution and show the underexposure themselves. PMID 40349107 doses only PND1. PMID 42181696 doses P0 and P14 and finds the P14 failure is a **dose** problem (3.5E10 kills, 1E10 rescues) | No source here licenses a statement of the form "after age X, WWOX restoration cannot work". The honest statement is that **no therapeutic window has been measured for any of these genes**, and the two apparent window results both resolve to delivery |
| **Off-target organ risk** | PMID 40349107, the strongest contribution in the set: DRG and spinal-cord histopathology graded blind, nerve conduction, serum NfL as a toxicity biomarker (≥1,719 pg/mL in affected animals vs ≤679 pg/mL with the detargeting element), transient liver-enzyme rises in every arm | DRG toxicity is an **AAV class effect**, not an STXBP1 effect, so it transfers to any AAV CNS programme including a WWOX one. The detargeting element's generality rests on three promoters and two transgenes |
| **PD assay** | PMID 42521212: endogenous HiBiT knock-in plus LgBiT complementation, bidirectional validation, in a line whose untagged allele is a frameshift. PMID 40349107: protein in ng/µg plus serum NfL | Methodologically transferable. **Nothing WWOX-specific exists**: `WWOX AND HiBiT` returns 0 PubMed records (ESearch, 2026-10-03) |

## The datum that matters most, and it is a negative

PMID 42181696 rescued survival (50 → 84.2 %), febrile seizures (11/15 → 2/13) and spontaneous
seizures (1.12 → 0.03 per mouse per day) in a blinded, randomised study — and under that rescue
cortical NaV1.1 protein went from ~0.45 to ~0.49 of wild type, **not significantly different**, while
cortical mRNA moved about 8 % of the wild-type level. Two readings are live and the paper keeps both:
the antibody is insensitive, or full normalisation is not required. Either way the consequence for
this repository is the same and it is actionable: **"how much protein is needed" cannot be answered by
a programme that has no assay sensitive enough to see the increment**. That is the concrete argument
for acquiring a WWOX pharmacodynamic readout before, not after, a restoration strategy is specified.

## Ops (provisional; anchors and next-free ids re-measured at commit time)

### 1 · `disease-models/wwox/research/research_lines_current.md`

| field | value |
|---|---|
| op | `append` (new record) |
| record | `RL-C-20261003w3 — The six parameters of a WWOX-restoration strategy, and which of them any source actually measures` |
| body | A table of the six parameters as above; the explicit statement that **no therapeutic window has been measured for any DEE gene in the 2025–2026 set read in this wave**, with PMID 39847501 and PMID 42181696 named as the two results that look like window results and resolve to delivery and to dose; the PMID 42181696 protein null as the reason an assay precedes a dose; and the PMID 42521212 HiBiT architecture as the named next acquisition. Status `open`, tag `INFERENZA`. |

### 2 · `disease-models/wwox/research/dismissal_ledger_current.md`

| field | value |
|---|---|
| op | `append` (new record) |
| record | `DIS-C-20261003w3 — "A developmental window for WWOX restoration can be bounded from the DEE gene-therapy literature" — REJECTED on the sources read` |
| body | The negative, with its two premises: PMID 39847501 attributes its P10 failure to transgene level and distribution and shows restricted expression at P10; PMID 42181696 inverts its own P14 failure by lowering the dose. Revival trigger: a published dosing study in which **expression is matched across ages** and efficacy still falls with age. |

### 3 · `disease-models/wwox/research/research_candidates_current.md`

| field | value |
|---|---|
| op | `append` (new record) |
| record | `RC-C-20261003w3 — Acquire a WWOX pharmacodynamic readout before specifying a restoration dose` |
| body | The HiBiT architecture of PMID 42521212 as the template, with its four stated limits carried: not WWOX-specific; C-terminal tagging tolerance for WWOX untested; abundance is not oxidoreductase activity; and the source line's own caveats (single plating, unquantified dynamic range, a 20q11.21 duplication including BCL2L1) must be designed out rather than inherited. |

## What would change the model if true, and what would falsify it

**Would change it:** a dosing study in any DEE gene that holds brain expression constant across two
ages and still shows an age effect — that would convert "window" from an unmeasured parameter into a
measured one. **Would falsify the central claim here:** a source in this set that does measure a
WWOX-relevant therapeutic window, or a demonstration that the PMID 42181696 NaV1.1 assay was
adequately powered to detect the increment it reports as null (in which case the rescue happened
without the protein, which is a different and larger finding).

### LOCATOR TRIPLES FOR BLIND AUDIT

(The target protein did not rise measurably under the arm that rescued the phenotype. | was not significant when compared to PBS control group | Results, neonatal molecular assessment, `files/fulltext/PMID42181696_Diaz2026_PMC.xml`)

(The authors state the therapeutic range is narrow, from their own dose reduction. | we showed that this treatment has a narrow therapeutic range | Discussion, P14 paragraph, `files/fulltext/PMID42181696_Diaz2026_PMC.xml`)

(The highest dose was the worst outcome, and the authors attribute it to overshoot. | exceeds the optimal therapeutic range, resulting in toxic side effects rather than benefit | Discussion, dose paragraph, `files/fulltext/PMID42181696_Diaz2026_PMC.xml`)

(The authors offer, as one reading, that full protein normalisation may not be required. | normalization of in NaV1.1 expression to wild-type levels may not be entirely required to have a therapeutic benefit | Discussion, protein paragraph, `files/fulltext/PMID42181696_Diaz2026_PMC.xml`)

(The concluding sentence is stronger than the Results it summarises. | modestly increasing NaV1.1 production | Discussion, final para, `files/fulltext/PMID42181696_Diaz2026_PMC.xml`)

(The P10 failure is attributed by the authors to transgene level and distribution, not to a closed developmental window. | We attribute this effect to the relatively low level and distribution of the Nav | Discussion, para 3, `files/fulltext/PMID39847501_Chen2025_PMC.xml`)

(The authors' own imaging shows the P10 cohort was underexposed, which is the evidence for that attribution. | Brain expression of Navβ1-myc protein in P10-injected animals was substantially restricted in comparison with P2-injected animals. | Results, cellular and temporal specificity, `files/fulltext/PMID39847501_Chen2025_PMC.xml`)

(The mouse age effect is not mapped onto human development by this paper. | it remains to be established whether this phenomenon occurs in human infants | Discussion, para 3, `files/fulltext/PMID39847501_Chen2025_PMC.xml`)

(Overexpression in wild-type brain changed interneuron excitability even though it produced no seizures. | we observed a leftward, hyperpolarizing, shift in the I-O curve for AAV-Nav | Results, PV+ interneuron excitability, `files/fulltext/PMID39847501_Chen2025_PMC.xml`)

(Every seizure datum in that study is video-scored behaviour without electrographic confirmation. | Without electrographic evidence, we cannot be confident that these events were indeed seizures. | Results, seizure severity, `files/fulltext/PMID39847501_Chen2025_PMC.xml`)

(The headline seizure endpoint rests on three mice per arm with no statistical test in the table. | [figure attestation — pixels cannot be quote-matched] (the table is published only as an image) Table 1 lists three untreated null mice and three AAV-Nav-beta-1-treated null mice, each scored on P14, P15 and P16, with per-day counts of seizure-like events under and over 10 s; the untreated average is 16.4 and 8.7 events per day and the treated average is 8 and 0; no statistical test, confidence interval or p value appears anywhere in the table. | Table 1, `files/fulltext/PMID39847501_Chen2025_supplement/jci-135-182584-g230.jpg`)

(Dorsal-root-ganglion and spinal-cord adversity occurred in every arm without the detargeting element and in none with it. | Potentially adverse findings in SC and DRG were observed after treatment with AAV9-EF1 | Results, NHP safety section, `files/fulltext/PMID40349107_Aeran2025_PMC.xml`)

(Serum neurofilament light was used as a toxicity biomarker with a stated threshold. | all reached serum NfL concentrations of 1,719 pg/mL or greater | Results, NHP safety section, `files/fulltext/PMID40349107_Aeran2025_PMC.xml`)

(Functional nerve-conduction changes occurred in half the animals in two arms. | Vector-related peripheral sensory axonopathies were observed in 2/4 animals administered with AAV9-STXPro5-STXBP1 | Results, nerve conduction, `files/fulltext/PMID40349107_Aeran2025_PMC.xml`)

(The therapeutic window is cited from other groups, not measured in that study. | Other groups have also reported phenotypic reversal following adult delivery | Discussion, `files/fulltext/PMID40349107_Aeran2025_PMC.xml`)

(The redosing interval is derived from measured CSF concentrations and modelled retention. | These data suggest that it is necessary to administer elsunersen at intervals of 4–6 weeks. | Main, PK paragraph, `files/fulltext/PMID40263630_Wagner2025_PMC.xml`)

(The exposure accounting does not agree with itself, first figure. | resulting in a cumulative dosage of 30.5 mg elsunersen across all seven doses | Main, initial observation period, `files/fulltext/PMID40263630_Wagner2025_PMC.xml`)

(Second of the three exposure figures. | the patient received further ten dosages of 8 mg elsunersen on a monthly basis | Main, extended observation period, `files/fulltext/PMID40263630_Wagner2025_PMC.xml`)

(Third of the three exposure figures, in an Extended Data caption. | A total of 94 mg elsunersen (intrathecal) doses were administered | Extended Data Fig. 5 caption, `files/fulltext/PMID40263630_Wagner2025_PMC.xml`)

(Seizure control was obtained without demonstrated developmental benefit. | the need for future studies to explore whether elsunersen can contribute to neurodevelopment improvements beyond seizure control | Main, extended observation period, `files/fulltext/PMID40263630_Wagner2025_PMC.xml`)

(The authors decline causal attribution from a single case. | Given that the data are based on one single patient, establishment of a definitive causal link will require further validation through formal clinical trials. | Main, penultimate para, `files/fulltext/PMID40263630_Wagner2025_PMC.xml`)

(The assay's dynamic range is not quantified and is admitted to need optimisation. | Future studies will optimize conditions to improve dynamic range. | Discussion, `files/fulltext/PMID42521212_Saravanan2026_PMC.xml`)

(Reproducibility across independent platings was not tested. | each HiBiT assay was conducted from a single plating of cells | Discussion, `files/fulltext/PMID42521212_Saravanan2026_PMC.xml`)

(The uORF lever failed when the authors tried to act on it with ASOs. | failed to increase luciferase activity in transfected cells or in vitro translation systems | Discussion, first para, `files/fulltext/PMID42521212_Saravanan2026_PMC.xml`)

(The reporter line carries a copy-number change that confers a growth advantage. | a 20q11.21 duplication including BCL2L1, which can confer a survival advantage | Results, reporter development, `files/fulltext/PMID42521212_Saravanan2026_PMC.xml`)
