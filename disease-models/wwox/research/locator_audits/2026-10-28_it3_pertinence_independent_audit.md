# Independent audit of assertion_pertinence.tsv (L3/L4 rows), 2026-10-28

Producer: orchestrator. Verifier: independent subagent, card text only. Applied in the same commit: all proposed changes (A-KD-1 L4 yes->no is the material one: the ketogenic-diet record no longer counts as an L4 cell; L4 case-level 2->1).

# Audit of assertion_pertinence.tsv (in-scope rows: all L3/L4 = yes, plus benefit with empty flags)

Judged from card/packet text only (cards under disease-models/wwox/research/drug_repurposing/{cards,cards_early}). Basis column ignored.
Scope: 28 rows with L3 or L4 = yes. The only empty-flag rows are DR-AAV-GLU10-HD/LD (sign null, not benefit); no benefit row has empty flags.

| assertion_id (tsv line) | verdict | reason (card field) |
|---|---|---|
| DR-C01-001 (2) | CONFIRMED | disease_assertion.context + measured_result_note: Wwox-null mouse ECoG; treated KO fell to a level not different from WT vs KO baseline; "ONE vector level only", "n = 5 pups per group by caption". L4 ok (recovery vs KO baseline). Note n=5 is stated for the bracket, treated-arm n not carried. |
| DR-AAV-SURV-HD (3) | CONFIRMED | measured_result_note: HD n=30 plateau 76-77% to d300 vs untreated KO n=10 at zero by d13-21. L4 ok. Flag gap: add n (30 vs 10) and "adverse audit entries 40/46 repaired, not re-judged". |
| DR-AAV-MOTOR-HD (4) | CONFIRMED | KO ~3.6 vs HD ~0.3, not different from WT (DA-AAV-MOTOR-001 baseline). Flag gap: card says "panel states no age", n not carried (fertility panels ~3/group) -> add age_unstated;n_not_stated. |
| DR-AAV-GFAP-P5HD (5) | CONFIRMED | KO ~44 vs treated ~5, same panel S8I holds WT, KO, treated. Flag gap: injected at P5 (timing experiment, not the dose study) and "high-dose identity rests on the supplement caption"; no dose arm -> add timing_P5_arm;dose_identity_from_caption. |
| DR-AAV-SURV-LD (6) | UNDERCLAIMED (sign) | note: "postpones death ... a postponement, not a rescue"; median ~d48 vs KO dead by d21. That is partial benefit, not "mixed" (mixed implies benefit plus harm). L4 no correct. |
| DR-AAV-MOTOR-LD (7) | UNDERCLAIMED (sign) | note: "genuinely intermediate between knockout and high dose" = partial benefit. L4 no correct. |
| DR-AAV-WT-HD (8) | CONFIRMED (weak L4) | KO ~4.7 g at d15 (dead by d17) vs HD ~15.6 g d30, WT ~17.5; but "no significance marker is printed on panel C at all" and comparison is across ages. L4 defensible only as numeric recovery; add no_significance_marker. |
| DR-AAV-WT-LD (9) | CONFIRMED | note: equal to HD at P30 only, lags P15-P25, survivor-conditioned (~79% alive), series truncated d60. "mixed" fits. Add survivor_conditioned. |
| DR-AAV-GLU10-HD (10) | CONFIRMED | status NO_CHANGE: ns vs WT and ns vs untreated KO; text's "partial correction" is qualified by panel. Flags empty -> add high_dose_arm. |
| DR-AAV-GLU10-LD (11) | CONFIRMED | NO_CHANGE, ns vs WT and vs KO. Flags empty -> add low_dose_arm. |
| A-VGB-1 (12) | OVERCLAIMED (flags) | note: "n = 1; concurrent therapy; at two years profoundly delayed"; locator: vigabatrin added after partial prednisolone response. Concurrent therapy is stated, not "possible"; reading_depth queried_not_full_read; no electrographic criterion. Sign benefit and L3 ok; L4 acceptable only as case-level own-baseline (spasm cessation = recovery of the endpoint). |
| A-VGB-3 (13) | CONFIRMED (flags weak) | note: n=1, cessation >=4 weeks clinically, no EEG criterion, no imaging. Concomitant drugs not stated either way; keep "possible". L4 case-level only. |
| A-VGB-2 (14) | OVERCLAIMED (flags) | endpoint is "spasm burden (partial response; cessation not reached; residual cluster spasms at 11 months)" and locator says "despite four antiseizure drugs": concomitants are present, not possible. Sign partial_benefit, L4 no correct. |
| A-VGB-10 (15) | CONFIRMED | direction NO_CHANGE, WOREE series class, allele not carried, "criterion not carried by the registry entry". Add criterion_not_carried;allele_not_carried;one_case. |
| A-KD-1 (18) | OVERCLAIMED (L4) | note: "Uncontrolled, unblinded, retrospective; denominator not stated ... no count, score, latency or duration"; quote "notably improved seizure control"; reading partial. Improvement is not recovery against a baseline; L4 not supported by the card. L3 benefit ok. Flags lack uncontrolled;retrospective;denominator_unknown;shared_origin_inference. |
| A-ETX-1 (19, NEED-T-TYPE) | CONFIRMED (weak) | Wwox-/- mice, quote "ethosuximide suppressed PTZ-induced seizure in Wwox-/- mice (Fig. 7b)". Note: effect "confined to the second half of the hour", control varies between experiments "by a comparable order to the late effect", no interaction test, N=6 null. Benefit is the authors' claim; the card undercuts it. Add late_phase_only;control_variability_comparable_to_effect;no_T_type_measurement (no T-type readout in a Wwox system, so pertinence to the T-type need is by seizure phenotype only). L4 no correct. |
| A-ETX-1 (20, NEED-SEIZURE) | CONFIRMED (flags inconsistent) | same experiment; flag no_drug_by_genotype_test present on line 19 but missing here. Make both lines carry the same flags. |
| DR-LI-001 (21) | CONFIRMED | Wwox-/-, PTZ-alone N=6 vs +Li N=7, four-star bracket; DR-LI-002 shows same effect in WT, so "failed its specificity test". L4 no correct. Flags: add n=6_vs_7;late_values_of_control_differ_across_experiments. |
| DR-D01-001 (24) | OVERCLAIMED (sign) | note: "Treated knockout not significantly different from wild type"; no KO-vs-treated test stated for this endpoint; "No treated-WT arm, no dose-response, no randomisation or blinding"; reading_depth UNKNOWN; "panel values NO LONGER RE-AUDITABLE"; engineered organoid KO, multi-kinase compound. A WT-comparison only, so sign should be normalised_vs_wild_type (as for the C04 no-KO-arm rows), not benefit. L3 ok only as observed_depth_unknown; L4 no correct. |
| DR-W2-001 (34) | CONFIRMED | Synapsin-Cre neuron-specific Wwox KO slices; bursting "eliminated and recovered on washout"; n=5 slices/3 animals, d-APV full competitive block, AMPAR untested. L4 no is conservative (reversible block of a KO phenotype against own baseline) but defensible because it is a tool compound with no catalogue identity; leave. |
| DR-AAV-GLU20-HD (54) | CONFIRMED | status UNKNOWN; ~147 not different from WT; no untreated-KO arm at d20. normalised_vs_wild_type, L4 no correct. |
| DR-AAV-GLU20-LD (55) | CONFIRMED | ~128, one star below WT; no KO arm. not_normalised correct. |
| DR-AAV-GFAPAREA-HD (56) | CONFIRMED | ~1.9 not different from WT; "same missing baseline"; WT value shifts between S7 panels. Add cross_panel_wt_inconsistent. |
| DR-AAV-GFAPAREA-LD (57) | CONFIRMED | ~3.05, two stars WORSE than WT; no KO arm. not_normalised correct. |
| DR-D01-002 (60) | CONFIRMED | "MEASURED NO RECOVERY: knockout-versus-treated not significant for both markers, CTIP2 far below wild type"; depth UNKNOWN. Add not_reauditable. |
| A-VGB-5 (62) | CONFIRMED | direction UNKNOWN is a bridge encoding; note "A reported null effect" = the datum; ineffective in null/null child without West syndrome (endpoint pertinence to spasms is loose). |
| A-VGB-6 (63) | CONFIRMED | note "A reported null effect in a missense genotype"; vigabatrin added to phenobarbital did not stop spasms. |

Adjacent flag defect (L3/L4 = no row): DR-LI-003 (line 23) is the heterozygous arm (context genotype Wwox+/-; group sizes not carried) but carries flag control_arm_wild_type; DR-LI-002 (22) is correctly WT.

Cross-cutting: sign vocabulary inconsistent ("mixed" used for the C04 low-dose partial effects, "partial_benefit" used for A-VGB-2). The README plain statement ("other L4 cells are uncontrolled case-level clinical reports (vigabatrin, ketogenic diet)") would need to drop ketogenic diet if A-KD-1 L4 is withdrawn.

## Proposed changes
- A-KD-1: counts_L4 yes -> no; flags += uncontrolled;retrospective;denominator_unknown
- DR-D01-001: sign benefit -> normalised_vs_wild_type; flags += no_treated_wt_arm;not_reauditable;no_blinding
- DR-AAV-SURV-LD: sign mixed -> partial_benefit
- DR-AAV-MOTOR-LD: sign mixed -> partial_benefit
- A-VGB-1: flags concomitant_drugs_possible -> concomitant_drugs_present (prednisolone), keep L4 yes (case_level)
- A-VGB-2: flags concomitant_drugs_possible -> concomitant_drugs_present (four ASDs)
- DR-AAV-GLU10-HD: flags "" -> high_dose_arm
- DR-AAV-GLU10-LD: flags "" -> low_dose_arm
- DR-AAV-WT-HD: flags += no_significance_marker
- DR-AAV-SURV-HD: flags += n=30_vs_KO_n=10;audit_repair_not_rejudged
- DR-AAV-MOTOR-HD: flags += age_unstated;n_not_stated
- DR-AAV-GFAP-P5HD: flags += timing_P5_arm;dose_identity_from_caption
- A-ETX-1 (both lines): flags += late_phase_only;control_variability_comparable_to_effect; line 20 += no_drug_by_genotype_test; line 19 += no_T_type_measurement
- DR-LI-003: flag control_arm_wild_type -> control_arm_heterozygote
- A-VGB-10: flags += criterion_not_carried;allele_not_carried
