# CC-20261004w8-B-RESTORATION-SPEC-01 — promoter, capsid and route bounds for a CNS restoration cassette

```yaml
context_policy: SOURCE_FIRST
actor: scientist (Group B, intake wave 8 2026-10-04)
branch: task/sci-B-20261004w8
change_class: MINOR
targets:
  - disease-models/wwox/registries/claim_registry_current.md
depends_on: CC-20261004w8-B-REGISTRY-01   # for the PAPER ids these claims cite
```

> **Not medical advice.** Public edition: class level only. **Every source behind this candidate
> mentions WWOX zero times.** Nothing here is a statement about WWOX biology; each item is a
> vector-engineering bound with its transfer limit stated.

## Why MINOR, and what it bears on

`working_model_current` BLOCK 3 holds a design-principles bullet — *"human synapsin promoter
(neuron-specific); WPRE removed (avoid overexpression); controlled dose; critical early postnatal
window"* — and an adjacent safety caveat about dose-limiting peripheral toxicity at high systemic
AAV dose. **None of the four sources contradicts either.** They bound them with measured numbers from
adjacent systems. `claim_registry_current` holds no consolidated baseline claim on promoter, capsid
or route that is narrowed or reversed (searched; 44 records). By §7 of the batch protocol this is an
**addition**: class **MINOR**.

The candidate is one record with four numbered bounds, so that a future reading cites one id rather
than four papers it has not read.

## Op — claim_registry_current.md

**Op:** append one new record. **No `old` text is replaced**, so no `old`/`new` pair is given.

**Proposed record (provisional id — the integrator assigns the next free `CLAIM` number):**

> **Statement.** A CNS AAV restoration cassette can be partly, but not fully, specified in advance.
> Four bounds are measured in adjacent systems:
>
> **(1) Cell-restricted is not peripherally silent.** In a ten-promoter head-to-head comparison in
> neonatal mouse by intracerebroventricular ssAAV9, the astrocyte-restricted promoter produced the
> **most hepatic transgene protein of any promoter tested** — more than the ubiquitous promoter —
> while whole-organ fluorescence in liver showed almost nothing. A cassette whose safety case rests
> on promoter restriction must measure hepatic **protein**, not hepatic fluorescence and not hepatic
> transcript alone.
>
> **(2) Restriction costs intensity, not reach.** In the same comparison, the neuron-restricted
> promoter covered 41% of brain area against the ubiquitous promoter's 42%, at about one third of
> the mean intensity (154.0 against 474.8 relative fluorescence units), with 72% of its transduced
> cells neuronal and 1.9% astrocytic.
>
> **(3) Promoter and route must be specified together.** The same promoter, in the same capsid, at
> the same dose, in the same mouse strain, ranked **best of four** by the intrathecal route in cortex
> and cerebellum and **among the worst of four** by the intracerebroventricular route in hippocampus,
> hypothalamus, cortex and cerebellum. A promoter chosen on one CSF route's data cannot be carried to
> another.
>
> **(4) The route reaches primate brain, thinly, and the dose ceiling does not move by capsid alone.**
> Lumbar intrathecal rAAV9 in cynomolgus macaque gave **1–4 vector genomes per diploid genome** in
> brain, uniform across regions, only at doses ≥ 5.8 × 10^13 vg/animal, with **sublinear** dose
> scaling (4× dose → ~2.5× brain vector) and **cerebellum the lowest brain region**, about five-fold
> below prefrontal cortex. Separately, a five-mutation liver-de-targeted AAV9 variant cut hepatic
> vector genomes ~127-fold but packaged **eight-fold worse**, dropped whole-animal transgene signal
> about two orders of magnitude, and put **significantly fewer vector genomes into the brain** than
> the parent capsid.
>
> **Classification.** `DATO` for each measured number; `INFERENZA` for the composite statement that a
> cassette can be "partly specified".
>
> **Status.** `open`.
>
> **Transfer limits, which apply to every item above.** Mouse for (1), (2) and the capsid half of
> (4); cynomolgus macaque for the route half of (4). Reporter transgenes throughout — EGFP, eGFP and
> firefly luciferase, never a 414-codon oxidoreductase. Neonatal dosing for (1) and (2); adult for
> (3). **(3) is measured in AAV-DJ, not AAV9.** The primate numbers are vector genomes in
> homogenate, which those authors explicitly state must not be read as a transduced-cell fraction and
> which carry no assurance the genome is intact or nuclear; **no expression of any kind was measured
> in that study.** The liver-de-targeted capsid study contains **no toxicity endpoint**, so its
> dose-ceiling implication is a mechanism hypothesis, not a safety result. None of the four papers
> mentions WWOX.
>
> **Route is not only a distribution parameter.** The primate biodistribution source reports, in its
> own limitations, a canine study in which — at comparable biodistribution — intracerebroventricularly
> dosed animals developed strong and in one case fatal encephalitis driven by T cells specific to the
> transgene product, while intracisternally dosed animals did not; the relevance to primates and
> humans is stated as uncertain.
>
> **What would change this claim.** Promoter ranking reproducing across routes in a second
> laboratory; a liver-de-targeted capsid with unchanged brain vector genomes *and* unchanged
> packaging yield; or any of these comparisons repeated with a therapeutic transgene rather than a
> reporter.
>
> **What would falsify it.** The unretrieved supplementary western-blot figure of the promoter study
> showing that the astrocyte-restricted promoter's hepatic protein is **not** the highest — bound (1)
> rests on the authors' Results sentences describing that figure, not on the panel.
>
> **Paper links.** `[[paper_registry_current#PAPER 153]]`, `[[paper_registry_current#PAPER 154]]`,
> `[[paper_registry_current#PAPER 155]]`, `[[paper_registry_current#PAPER 156]]` (provisional; see
> `CC-20261004w8-B-REGISTRY-01`).
>
> **Note.** Class-level record; no individual-level detail. Not medical advice.

## Consequential edits

If this lands, the `Claim links:` field of `PAPER 153`–`PAPER 156` changes from `none` to the id this
record receives. Those four records are created by `CC-20261004w8-B-REGISTRY-01` in this same wave,
so the substitution is made by the integrator at renumbering time.

## Change class

**MINOR.** One appended record; four field substitutions in records this wave is itself creating.

### LOCATOR TRIPLES FOR BLIND AUDIT

(A cell-restricted astrocyte promoter produced confirmed significant transgene protein in the liver although whole-organ fluorescence there showed minimal signal | Although sensitive qPCR analysis revealed robust EGFP mRNA in the liver and only low-level transcripts in the heart (Figure 2B), whole-organ fluorescence showed minimal signal in either tissue (Figure 3); however, western blot quantification confirmed the significant protein expression in the liver (Figure S1). | files/fulltext/PMID41036104_Chornyy2025_PMC.xml, Results, 'Examination of promoter-driven EGFP mRNA expression and protein distribution in CNS and peripheral tissues post-ssAAV9 delivery')

(The cell-restricted promoter is the one that put the most protein into the liver, stated by the authors as a ranking | with CAG driving the most EGFP protein in BA1, BA2, and the heart; CNP driving the most EGFP protein in BA3; and, finally, gfa1405 driving the most EGFP protein in the liver (Figure S1) | files/fulltext/PMID41036104_Chornyy2025_PMC.xml, Results, same section)

(The neuron-restricted promoter matched the ubiquitous promoter for brain-area coverage | while the p546 promoter's total distribution area was comparable to CAG (41% of the total brain area), the protein expression pattern was distinct, with lower intensity in projections compared to soma-restricted expression | files/fulltext/PMID41036104_Chornyy2025_PMC.xml, Results, 'Comparative fluorescent analysis of EGFP protein expression and distribution in the mouse brain post-ssAAV9 i.c.v. injection')

(The measured cell-type specificity of each promoter | For astrocytes, the EGFP signal levels were found to be quite varied: CAG, 36%; p546, 1.9%; GFAP, 44%; gfaABC(1)D, 58%; and gfa1405, 37.7% colocalization with astrocytes. On the other hand, neuronal colocalization presented a different pattern: 27% with CAG, 72% with p546, 13% with GFAP, 19% with gfaABC(1)D, and 11.9% with gfa1405 | files/fulltext/PMID41036104_Chornyy2025_PMC.xml, Results, 'Colocalization analysis of EGFP protein expression with cell-specific biomarkers in the brain')

(The doses of the head-to-head promoter comparison are not matched across arms | The viral genome (vg) doses for each vector were as follows: 7.50E10 vg per animal for AAV9.GFAP.EGFP, AAV9.gfa1405.EGFP, AAV9.gfaABC(1)D.EGFP, AAV9.P546.EGFP, AAV9. CAG.EGFP, and AAV9.EFS.EGFP; 7.00E10 vg per animal for AAV9.tCAG.EGFP; 8.50E10 vg per animal for AAV9.CNP.EGFP and AAV9.rMBP.EGFP; and 8.00E10 vg per animal for AAV9.MAG.EGFP. | files/fulltext/PMID41036104_Chornyy2025_PMC.xml, Materials and methods, 'Intracerebroventricular injections')

(By the intrathecal route the mini-promoter outperformed all three established promoters in cortex and cerebellum | In the cortex and cerebellum, CP040-mediated eGFP expression levels were significantly higher than seen with the CBA, EF1α, and hSYN promoters (Figures 5C and 5E). | files/fulltext/PMID42137269_Chauhan2026_PMC.xml, Results, paragraph on transcript comparison)

(By the intracerebroventricular route the same promoter at the same dose in the same capsid ranked below the ubiquitous promoters | In the ICV administration cohorts, eGFP transcript levels from the CP040 mini-promoter were lower than those obtained from either of the ubiquitous CBA and EF1α promoters and equivalent to the hSYN promoter in the hippocampus and hypothalamus | files/fulltext/PMID42137269_Chauhan2026_PMC.xml, Results, same paragraph)

(The in vivo capsid in that promoter comparison is AAV-DJ and not AAV9 | The CP040 mini-promoter was cloned upstream of the eGFP reporter gene in an AAV inverted terminal repeat (ITR) containing vector and packaged into the AAVDJ capsid. | files/fulltext/PMID42137269_Chauhan2026_PMC.xml, Results, second paragraph)

(Lumbar intrathecal rAAV9 reaches primate brain at one to four vector genomes per diploid genome and only at the higher doses | Mean level of rAAV9 DNA in the brain corresponded to 1 to 4 vg/DG at all doses ≥ 5.8 × 1013 vg/animal (HED: 5.0 × 1014 vg), with an apparent dose-dependence seen both in the Day 90 brain samples and the Day ≥180 brain samples (Figure 4). | files/fulltext/PMID42136830_Haque2026_PMC.xml, Results, 'Dose-dependence and temporal effects on rAAV9 levels in the brain')

(Dose scaling by that route is sublinear | the four-fold increase in input dose with TSHA-105 was associated with a ~2.5-fold increase in vector genome levels detected in brain tissues; this difference was seen at both necropsy time points | files/fulltext/PMID42136830_Haque2026_PMC.xml, Results, 'TSHA-105 at 90 and 180 days post-lumbar IT administration')

(Cerebellum is the lowest brain region measured by that route | Biodistribution was consistent across brain regions mean values ranging from ~2.5 × 104 vg/μg (0.16 vg/DG) in the cerebellum to ~1.3 × 105 vg/μg (0.8 vg/DG) in the prefrontal lobe. | files/fulltext/PMID42136830_Haque2026_PMC.xml, Results, 'TSHA-101 CNS biodistribution at 30 days post-lumbar IT administration')

(No expression of any kind was measured in the primate biodistribution study, and the authors say why | Analysis was restricted to vector biodistribution, rather than gene or protein expression, because the vectors all differed in their promoter and other regulatory sequences, precluding any comparison across experiments. | files/fulltext/PMID42136830_Haque2026_PMC.xml, Discussion, 'Strengths and limitations')

(The authors forbid reading vector genomes per diploid genome as a transduced-cell fraction | mean vg/DG must not be understood as an estimate of the proportion of transduced cells. Among other concerns, neuronal and non-neuronal cell-type differences may affect the efficiency of rAAV9 uptake, and rAAV9 DNA detection offers no assurance that the vector genome is fully intact or that it has been internalized into the cell and cell nucleus. | files/fulltext/PMID42136830_Haque2026_PMC.xml, Discussion, 'Strengths and limitations')

(Two cerebrospinal-fluid routes with comparable biodistribution differed in whether they produced a fatal transgene-directed immune response | the authors noted a stark difference between the ICM and ICV approaches with regard to safety; ICV-dosed dogs experienced a strong (and, in one case, fatal) encephalitis, apparently driven by T cells specific to the transgene product, but no such response was seen in ICM-treated animals. The relevance of the canine safety and biodistribution data to NHP and human GT is not certain. | files/fulltext/PMID42136830_Haque2026_PMC.xml, Discussion, 'Strengths and limitations')

(The liver-de-targeted capsid packages about eight-fold worse than its parent | AAV9 yields were in line with the general field consensus at 3.58 × 1013 vector genomes (vgs) (Figure 1B). We found both AAV9-16 and AAV9-HR to result in slightly lower yields than AAV9 at ~2.0 × 1013 vgs (Figure 1B). However, the reduction in packaging efficiency was more pronounced in the AAV9-DM, which yielded 4.5 × 1012 vgs (Figure 1B). | files/fulltext/PMID41744777_Nabakowski2026_PMC.xml, Results, '3.2. Packaging Efficiencies')

(The liver reduction is about 127-fold | AAV9-DM resulted in a ~127 fold reduction in vector genome copies as compared to AAV9, which is the most significant reduction in any variant tested (Figure 4A). | files/fulltext/PMID41744777_Nabakowski2026_PMC.xml, Results, '3.4. Evaluation of Vector Genome Biodistribution in Different Tissues')

(Every mutated capsid including the new one put significantly fewer vector genomes into the brain than the parent | In the brain, all mutated capsids resulted in significantly lower vector genome copies as compared to AAV9, though relative expression levels were consistent amongst all capsids investigated. | files/fulltext/PMID41744777_Nabakowski2026_PMC.xml, Discussion, fifth paragraph)

(Whole-animal transgene signal from the new capsid is about two orders of magnitude below the parent at the same dose | AAV9 was placed in the high group and reached a peak AR of 7.3 × 107, AAV9-16 and AAV9-HR were in the medium group and reached a peak AR of 6.6 × 106 and 3.5 × 106, respectively, and AAV9-DM was in the low group and reached a peak AR of 5.8 × 105 (Figure 2). | files/fulltext/PMID41744777_Nabakowski2026_PMC.xml, Results, '3.3. AAV9-DM Capsid Results in Liver De-Targeting and Durable Transgene Expression')
