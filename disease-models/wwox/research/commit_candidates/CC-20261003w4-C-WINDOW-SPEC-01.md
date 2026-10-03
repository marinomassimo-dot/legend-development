# CC-20261003w4-C-WINDOW-SPEC-01 — which of the five risk parameters of a neuron-targeted AAV can be bounded in advance, and which cannot

- `context_policy: SOURCE_FIRST`
- Sources: PMID 42349402 (`FTR-20261003-42349402-01`), PMID 41992613 (`FTR-20261003-41992613-01`),
  PMID 42458834 (`FTR-20261003-42458834-01`). Supporting: PMID 35331006, PMID 36700120. All
  manifests validate (`--verify-artifacts --require-current-schema`, `VERDICT: PASS`).
  **None of the sources mentions WWOX.**
- Change class: **MINOR**. One research-line record and one dismissal-ledger negative, both research
  layer, both statements about **what is not yet specifiable**.
- Read **after** the first pass was written: `CC-20261003W3-C-RESTORATION-SPEC-01`. This candidate
  **corroborates and sharpens** that one; it overturns nothing in it.
- **Nothing here is medical advice.**

## The finding, in one sentence

Of the five parameters that would have to be fixed before a neuron-targeted AAV's risks could be
called bounded in advance — promoter cell-class reach, the therapeutic window's lower limb, its
upper limb, the systemic organ at risk, and a surveillance assay — **two can be bounded today and
three cannot**, and the source that comes closest to measuring a two-sided therapeutic window states
in its own text that it did not measure one.

## Parameter by parameter, with the transfer limit on each

| Parameter | Best measurement in this set | Measured or assumed | Transfer limit to WWOX-DEE |
|---|---|---|---|
| **Promoter cell-class reach** | PMID 42349402: a 410-bp mouse *Gad1* cassette at **92.2 % ± 1.3 %** inhibitory-neuron specificity after intravenous AAV-PHP.eB at 5.0 × 10¹¹ vg/mouse; ≈85 % of PV⁺ neurons transduced, >60 % of transduced cells PV⁺, SST⁺ 10–15 %, other subtypes ≈25 %; 94.5 % with a ChR2 cargo and 92.4 / 93.2 / 86.5 % with a GAD65 cargo in cortex, CA1 and CA3 | **MEASURED**, and the best-measured parameter in the group | The method transfers; the cassette does not — it is mouse-derived and no human orthologue is tested. 🔴 Specificity is **route-contingent**: the same cassette falls to 63.9 % ± 4.1 % and 61.4 % ± 0.9 % after direct hippocampal injection, which the authors attribute to local vector concentration. Specificity is a property of cassette × route × dose. WWOX's **required** cell set is unknown: the repository holds no measurement of which neuronal or glial populations need WWOX restored |
| **Therapeutic window, lower limb** | PMID 41992613: i.c.v. dose-ordered survival in SMNΔ7 mice from median 23 d at 2 × 10¹⁰ vg/animal to median 373 d and maximum 501 d at 2 × 10¹¹; minimum effective dose set at 2 × 10¹⁰ vg/animal (1.3 × 10¹³ vg/kg) | **MEASURED**, within one construct and one route | Vector genomes do not transfer between genes, capsids, promoters or species. What transfers is that a lower limb **can** be measured when a dose series and a survival endpoint exist |
| **Therapeutic window, upper limb** | PMID 41992613: a survival inversion — EXG001-307 improves with dose (35 d at 2 × 10¹⁴ → 191 d at 4 × 10¹⁴ vg/kg) while its codon-optimised derivative EXG001-340 reverses (205 d → **29.5 d**) | **INFERRED, NOT MEASURED**, and the source says so | The toxic arm is a **different construct**, so dose and expression change together; that cohort "did not undergo comprehensive necropsy or histopathological evaluation"; and the authors write that measuring protein there "would be valuable **to define this therapeutic window** and substantiate this conclusion". In primates the top dose tested became the **NOAEL**, so no toxic dose was reached at all. No window anywhere in this corpus is expressed in units of protein |
| **Systemic organ at risk** | PMID 42458834: strong ubiquitous expression after an intra-CSF injection in newborn mice killed **every** high-dose animal by P8 from **myocardial degeneration**, with hepatic steatosis, serum AST ×4.2 / ALT ×2.3 / triglycerides ×2.4, cardiac *Ifnb1* >1000-fold and *Cxcl10* ≈220-fold — while a promoter-matched control vector carrying a different transgene elicited none of the interferon response | **MEASURED**, and sponsor-adverse, which is the strongest kind | 🔴 **The organ at risk from a CNS vector may not be the CNS.** That lesson transfers. The *magnitude* does not: DDX3X's own roles in RIG-I/MAVS signalling, stress-granule biology and *Ddit3* transcription are plausibly the mechanism. **WWOX dose sensitivity is neither shown nor excluded by this** and must not be assumed in either direction. The transfer-critical fact: the lethal mouse dose, scaled by neonatal brain mass, equals ≈1 × 10¹⁵ vg in a human, which the paper states is a dose several intra-CSF AAV9 trials use |
| **Surveillance assay** | PMID 36700120 (see `CC-20261003w4-C-TOXBIOMARKER-01`) | **MEASURED**, nonclinically | Tier 3 under `LEGEND_CORE` §13 with respect to WWOX |

## The datum that matters most, and it is a negative

The one paper in this corpus whose thesis is that "both insufficient and excessive transgene
expression are suboptimal" **does not measure the excessive side**. It measures a survival inversion
between two different constructs, performs no histopathology on the inverted arm, never measures the
protein alleged to be excessive, and names that missing measurement itself. Its primate arm then
fails to reach a toxic dose at all, so the NOAEL is simply the highest dose tested.

The consequence for this repository is the same as wave 3's and is now better supported:
**"how much is too much" cannot be answered by a programme that has not measured the protein at the
dose that caused harm.** Wave 3 reached that conclusion from a set in which no source attempted a
two-sided window; wave 4 adds a source that attempted one and did not complete it. A negative with a
failed positive control is a stronger negative.

## What this adds to the wave-3 specification

Three contacts with `CC-20261003W3-C-RESTORATION-SPEC-01`, all corroborating:

1. **The window row stands.** Its claim that no therapeutic window has been measured for any DEE
   gene in its set survives the closest available challenge.
2. **The off-target-organ row needs a sixth organ.** Wave 3's row is populated by DRG, spinal cord
   and liver. PMID 42458834 adds the **heart**, after an intra-CSF route, with the brain spared
   morphologically — and it supplies the cause to carry with the organ: a strong ubiquitous promoter
   on a dose-sensitive transgene, not the organ alone.
3. **The cell-type row gains a route caveat.** Wave 3 records per-promoter excitatory/inhibitory and
   PV/SST/VIP coverage figures. PMID 42349402 shows those figures are **not portable across routes**:
   one cassette, two routes, a 30-point swing in specificity.

## Ops (provisional; anchors and next-free ids re-measured at commit time)

### 1 · `disease-models/wwox/research/research_lines_current.md`

| field | value |
|---|---|
| op | `append` (new record) |
| record | `RL-C-20261003w4b — The five risk parameters of a neuron-targeted AAV: which are measurable in advance, and which the 2022–2026 literature still assumes` |
| anchor | after the current final record `RL-GT-001`; the file's last line is `**Version update:** v1.3 — 2026-07-25 (integrity repair: restored the previously referenced RL-BIOM-001 record)`. If `RL-C-20261003w4a` from `CC-20261003w4-C-DRG-CONTRADICTION-01` is applied first, append after it |
| body | The five-parameter table above with every transfer limit retained; the explicit statement that the upper limb of the therapeutic window is **inferred and not measured** in the one source that claims it, with that source's own two admissions quoted; the heart as a sixth off-target organ for the wave-3 specification, with its cause; and the route-contingency caveat on every promoter-coverage figure. Status `open`, tag `INFERENZA`. Cross-reference `RL-GT-001` and `CC-20261003W3-C-RESTORATION-SPEC-01`. |
| next action | Carry the route of administration alongside every promoter-specificity figure the repository holds, since none is portable across routes; and treat "how much WWOX protein, in which cells" as the acquisition that precedes any dose statement, as the wave-3 candidate already proposes. |

### 2 · `disease-models/wwox/research/dismissal_ledger_current.md`

| field | value |
|---|---|
| op | `append` (new record, provisional id `DIS-032`; `DIS` max measured at **30**, and `DIS-031` is proposed by `CC-20261003w4-C-DRG-CONTRADICTION-01`) |
| record | `DIS-032 — «The upper limit of a safe transgene dose can be taken from the SMA precision-dosing literature» → ❌ REJECTED on the source read` |
| anchor | after `DIS-031` if applied, otherwise after `DIS-030` |
| body | **PREMISE: DATO** (2026-10-03, intake wave 4, Scientist C, `context_policy: SOURCE_FIRST`, from a `partial_fulltext_read` of PMID 41992613, receipt `FTR-20261003-41992613-01`; supplement and figure panels unread). The two-sided claim is real and is stated by the authors, but its upper limb rests on a survival inversion between **two different constructs**, on a cohort that received **no necropsy and no histopathology**, and on **no measurement of the protein** said to be excessive — all three stated in the paper. Its primate arm designated the **highest dose tested** the no-observed-adverse-effect level, so it establishes no ceiling. 🔴 A separate reason for caution about taking numbers from this source: the same rat doses are normalised to body weight **three mutually incompatible ways** (Table 1: 3.0 × 10¹² and 6.0 × 10¹² vg/kg; Results: 4.3 × 10¹² and 8.5 × 10¹³; Methods: 4.3 × 10¹² and 8.5 × 10¹²), and the Results high-dose figure is impossible on its face, since doubling vg per animal cannot multiply vg/kg twenty-fold. **Boundary:** this does not reject the paper's finding that excess can be harmful — PMID 42458834 demonstrates that independently and lethally. What is rejected is the use of **any numeric ceiling** from this literature as a bound on a WWOX dose. |
| `REVIVAL_TRIGGER` | A dosing study, in any gene, that holds brain transgene **protein** constant across two doses or two ages and still shows a toxicity threshold, with histopathology on the toxic arm — which would convert the window's upper limb from inferred to measured. |

## What would change the model if true, and what would falsify this

**Would change it:** a measurement of how much WWOX protein, in which cell classes, is needed —
nothing in this corpus or wave 3's bears on it, and `WWOX AND (adeno-associated OR AAV)` returns
**2** PubMed records (esearch 2026-10-03). Also: histopathology and protein quantification on
PMID 41992613's inverted arm, which would make the first two-sided window in the corpus real.

**Would falsify statements here:** a demonstration that WWOX is **not** dose-sensitive, which would
make the overexpression lessons cautionary rather than load-bearing. The converse is equally not
assumed: nothing in this reading shows that WWOX **is** dose-sensitive.

### LOCATOR TRIPLES FOR BLIND AUDIT

(The cassette's selectivity dropped by about a third when only the route changed. | direct hippocampal injection of AAV-GFP or AAV-hM4D(Gi) resulted in reduced specificity | Results, chemogenetic manipulation, `files/fulltext/PMID42349402_Fukai2026_PMC.xml`)

(The authors attribute that drop to the route rather than to the cargo. | it is influenced by the route of administration, with reduced specificity observed following direct parenchymal injection | Results, chemogenetic manipulation, `files/fulltext/PMID42349402_Fukai2026_PMC.xml`)

(The proposed cause is local vector concentration, which makes it a dose phenomenon as well. | This reduction may be attributable to high local vector concentrations. | Results, chemogenetic manipulation, `files/fulltext/PMID42349402_Fukai2026_PMC.xml`)

(The subtype bias is quantified in both directions, which is what makes the word preferentially auditable. | Approximately 85% of PV+ neurons were GFP positive | Results, preferential targeting of PV-positive interneurons, `files/fulltext/PMID42349402_Fukai2026_PMC.xml`)

(Off-target expression in excitatory neurons is not excluded by the measurement. | Although low-level expression in excitatory neurons cannot be completely excluded | Discussion, preferential targeting and network control, `files/fulltext/PMID42349402_Fukai2026_PMC.xml`)

(No toxicology was performed; it is named as future work. | further evaluation of long-term safety, off-target expression, and peripheral distribution will be required | Discussion, translational potential and limitations, `files/fulltext/PMID42349402_Fukai2026_PMC.xml`)

(The two-sided dose claim is made explicitly in the body of the paper. | as both insufficient and excessive expression fail to achieve the desired outcome | Discussion, paragraph on supraphysiological expression, `files/fulltext/PMID41992613_Song2026_PMC.xml`)

(The arm that defines the upper limit received no pathology workup. | did not undergo comprehensive necropsy or histopathological evaluation | Results, codon-optimised variants, `files/fulltext/PMID41992613_Song2026_PMC.xml`)

(The authors state that their own data do not yet define the window. | would be valuable to define this therapeutic window and substantiate this conclusion | Results, codon-optimised variants, `files/fulltext/PMID41992613_Song2026_PMC.xml`)

(No adverse effect was reached at the top primate dose, so that arm bounds nothing from above. | the high dose was designated the no-observed-adverse-effect level | Results, overall safety conclusion, `files/fulltext/PMID41992613_Song2026_PMC.xml`)

(The sensory ganglia were never collected in the rodent studies, so the rodent safety statement rests on behaviour. | DRGs were not harvested or analyzed | Results, route comparison and tissue expression, `files/fulltext/PMID41992613_Song2026_PMC.xml`)

(A mechanistic element of the design is carried without confirmation, for programme-speed reasons. | confirmatory experiments were not performed in order to prioritize program progression | Results, microRNA de-targeting, `files/fulltext/PMID41992613_Song2026_PMC.xml`)

(Death followed a CSF injection within a week, from a peripheral organ. | died abruptly by P8, 1 week post injection | Results, rapid death due to myocardial degeneration, `files/fulltext/PMID42458834_Boitnott2026_PMC.xml`)

(The lethal animal dose was scaled to a human dose by brain mass, which is what makes the result transferable. | if extrapolated by neonatal brain mass | Materials and methods, viral vector injections, `files/fulltext/PMID42458834_Boitnott2026_PMC.xml`)

(The lipid phenotype was organ-selective and absent from the brain. | Notably lipid droplets were not detected in the brain or kidney | Results, lipid accumulation and hepatic toxicity, `files/fulltext/PMID42458834_Boitnott2026_PMC.xml`)

(The brain was nonetheless not transcriptionally unaffected, and the authors cannot explain it. | Cxcl10 mRNA levels were also increased in the brain | Results, type I interferon signalling, `files/fulltext/PMID42458834_Boitnott2026_PMC.xml`)

(The mechanism is declared unaddressed in the same paragraph that proposes it. | While not mechanistically addressed in this paper | Discussion, paragraph 2, `files/fulltext/PMID42458834_Boitnott2026_PMC.xml`)

(The operational conclusion the authors draw is about promoter strength, not about this gene. | we raise caution to the use of strong promoters like CBA | Discussion, final paragraph, `files/fulltext/PMID42458834_Boitnott2026_PMC.xml`)

(The apparent age effect is attributed by the authors to dose per body weight, not to a developmental window. | it is more likely a factor of a higher dose per body weight at the younger age | Results, rapid death due to myocardial degeneration, `files/fulltext/PMID42458834_Boitnott2026_PMC.xml`)

(Bulk tissue measurement understates per-cell exposure, by the authors' own caveat. | represent average expression across bulk tissue | Results, rapid death due to myocardial degeneration, `files/fulltext/PMID42458834_Boitnott2026_PMC.xml`)


## BATCH DISPOSITION — `BATCH_20261003_003` (2026-10-03, ACTOR_ID `scientist`, Scientist H), append-only

**Verdict:** PROPAGATED

**PROPAGATED, authored from the prose specification.** `RL-C-20261003w4b` (the five-parameter table with every transfer limit, the measured/inferred verdict per parameter, the heart as a sixth off-target organ with its cause, and the route-contingency caveat on every promoter-coverage figure) and **`DIS-032`** (the SMA upper-limb rejection, with the three mutually incompatible vg/kg normalisations and the boundary that excess harm is *not* denied — PMID 42458834 shows it independently). Appended after `DIS-031` as the candidate specified. Its declared `DIS-032` was free. **Not superseded by, and not superseding, `CC-20261003W3-C-RESTORATION-SPEC-01`:** measured rather than assumed — the two rest on **disjoint** source sets (wave-3 PMIDs 39847501/40263630/40349107/42181696/42521212 against wave-4 PMIDs 35331006/36700120/41992613/42349402/42458834) with a prose Jaccard overlap of 0.276, so the wave-3 candidate stays queued on its own evidence.
