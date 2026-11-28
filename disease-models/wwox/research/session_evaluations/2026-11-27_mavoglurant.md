# Mavoglurant batch self-evaluation

## Scope and executable verdict

- SCI_CODEX examined adult PET engagement, age-specific exposure, pediatric functional outcomes and untreated WWOX expression in a question-driven comparison. Targeted receipts FTR-20261127-33545349-01, FTR-20261127-37651202-01 and FTR-20261127-39483619-01 record partial coverage.
- Session self-evaluation PASS and receipt verification OK, 3,267 anchored entries. Structural LINT reported existing link warnings. Nine output tables were byte-identical on replay. [Dossier and replay](../drug_repurposing/continuous_compounds/mavoglurant/occupancy_and_disposition_20261127.md)

| Dimension | Evidence and limit | Grade |
|---|---|---|
| Source coverage | Original adult figures and PK/PET tables, published FXLEARN full-text sections and registered outcomes, protocol PK appendix and biomarker subcohort. Raw PET input and quantitative FXLEARN plasma summaries were unavailable. | Partial |
| Hidden detail | Tracer displacement and modeled occupancy differ. Digitized midpoint sensitivity and pediatric arithmetic means preserve the measurement scales. The two sources report different completion counts. A subgroup interval also differs within the publication. | Strong |
| Replication and transfer | Longer-term pediatric fragile X outcomes, healthy adult PET and untreated WWOX models answer different questions. The blood substudy comes from FXLEARN. Mouse nuclei contain one pool per genotype. | Strong |
| Discriminating observation | Candidate-specific rescue requires engagement and preferential recovery at matched initial recruitment while preserving adaptation and physiological inhibition. Bulk targets and basal ARC separate exposure selection from the functional readout. | Strong |
| Revival and decision | Retain the native mGlu5-versus-mGlu1 comparison. Hold trial prioritization pending a local functional rescue and age-relevant engagement and safety data. No canonical claims promoted. | Strong |

## Persistence and method

Evidence hashes and exact read locators are in the shared evidence directory. Published dose and concentration model fits stay separate. The plotted-point analysis reports the leave-one-dose range in place of a participant-level confidence interval. The simulations substitute aggregate pediatric concentrations into an adult model. This is an explicitly conditional use of an adult estimate. No new complete-read claim was made. The public outcomes and partial-read analysis leave no point estimate of seizure benefit or brain occupancy for children with WWOX.

Independent review is deferred until verified completeness definitions, original PET input or time-stamped pediatric exposure are available. These data would change the exposure or endpoint interpretation. The current preclinical disposition is robust to the observed record inconsistencies.

```text
ATTRIBUTION_CENSUS
incidents: 2
machine: 2   blind_auditor: 0   peer: 0   self: 0
severity_high: 0   of which self: 0
undetected_known: 0
```

**Defaults taken.** Retain separate published and registered completion counts and both printed exploratory subgroup values. Use group average exposure only as a model sensitivity and report leave-one-library and leave-one-dose ranges with distinct units.

**Stop log.** No operator dependency. The compound has an explicit reopen criterion and the programme continues.
