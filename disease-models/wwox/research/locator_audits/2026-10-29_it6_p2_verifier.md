# IT6 P2 independent verification: F/C/P priority positions (verifier part)

Actor: independent verifier (not the producer). Reviewed commit `da31daff` on `task/it6-p2`. Read-only toward the producer's files; this report is the only file added. Non-canonical. No score, no ranking of treatments, no efficacy or dosing statement.

Method. (A) I chose the card-need links and derived F/C/P labels from the sources and the rule text of `priority_rules_it5_20261029.md`, not from the code. (B) I then compared with the producer's table and the code output (`repurposing_view.py positions`). (C) I re-opened the sources behind data corrections D1 to D5. (D) I recomputed the guard hash and read the diff. (E) I judged the category effect and the EB-KD-01 question. Both test suites were run in the worktree.

Order caveat. Two incidental leaks before the derivation was complete: a search output showed the producer's EB-KD-01 label (C2), and a search hit showed D1/D2 wording. The other labels below were derived before I read the producer's table.

Sources opened in this session: PubMed abstracts 40165594 (apinocaltamide), 35573960 (Riva 2022), 36537114 (Chong 2023); the full text of PMC9100683 (Riva 2022, full case description); the local full texts of Rico-Molina 2024 (Table 2 and its footnotes), Bacq 2024, Obeid 2026 (Figure 3 caption, "reference item" definition) and Steinberg/Aqeilan 2026 (PMID 42397075, Results text on the A51 experiment); the deep-dive manifests for PMID 42422765, 32000863 and 42397075.

## 1. Test results

| check | result |
|---|---|
| `python3 -B framework/scripts/test_repurposing_view.py` | Ran 92 tests, OK |
| `python3 -B framework/scripts/test_repurposing_coverage.py` | Ran 54 tests, OK |
| guard hash of `classify_rows` + `assign_need_position` + `overview_positions` | `e94c0aae178aaf2d`, equals the pin; the revision at `9c39392f` gives `244882c7cd5d1965`, equals the old pin |

The tests being green says nothing about defects V1 to V3 below: the tests pin the producer's own data and carrier list.

## 2. (A) My derived labels, 22 links (rule text applied to the sources)

Position meaning as in the rules file. "Mine" is derived from the source; "Code" is the `positions` output; "Prod." is the producer's table.

| # | card x need | critical case | source reading (what decides it) | mine | code | prod. |
|---|---|---|---|---|---|---|
| 1 | C01 x gene addition | controlled single endpoint | SWD rate falls to wild-type level vs untreated knockout; complete read; one vector level, n = 5, single channel, "limited cohort" in the authors' words | F1 by the flag list; F2 if "one experiment" is applied as it is for EB-ETX-01 (see V5) | F1 | F1 |
| 2 | C04 x gene addition | benefit alongside weaker rows | survival high dose vs KO + RI controls p < 0.0001 and vs wild type p = 0.78 (Figure 3 caption, text), n = 30 vs 10; low dose is postponement, not rescue | F1 | F1 | F1 |
| 3 | C04 x glycaemia/growth | benefit beside nulls | body weight benefit; low dose mixed; P10 glucose not significant vs either comparator at both doses | C2 | C2 | C2 |
| 4 | EB-VGB-01 x seizure | benefit alongside nulls | three case-level benefits and three reported nulls, all queried not read; Riva 2022 text confirms vigabatrin listed as ineffective | C2 | C2 | C2 |
| 5 | EB-KD-01 x seizure | favourable precedent with contrary case | Chong 2023: epilepsy responded in three patients; Riva 2022 (biallelic null): "The ketogenic diet did not significantly improve seizures and was suspended" | C2 | F2 | F2 in code, C2 by source |
| 6 | EB-ETX-01 x seizure | one graphical experiment | Fig. 7b, controlled, complete read, graphical, one experiment, late phase only | F2 | F2 | F2 |
| 7 | EB-ETX-01 x T-type | same card, second need | same experiment; the endpoint is a seizure score, no T-type measurement | F2 (downstream, see V6) | F2 | F2 |
| 8 | G01 x seizure | wild-type effect | lithium suppresses in the knockout panel and as strongly in wild type (floor-limited); two further rows are wild-type or heterozygote arms and do not count | F2 | F2 | F2 |
| 9 | D01 x MYC/progenitor | wild-type-only claim | see V1: the paper compares treated vs untreated knockout, and layer-neuron markers do not recover | C2 (rule text), F2 if the downstream row is excluded; not C1 | C1 | C1 |
| 10 | F01 x excitatory gain | tool compound | d-APV eliminates bursting, recovers on washout, n = 5 slices from 3 animals; tool compound | F2 | F2 | F2 |
| 11 | H01 x seizure | favourable external precedent with counter | abstract of 40165594: benefit in AGS mice and MEST at higher concentration; no effect on focal-onset kindling; no WWOX row | F3 | F3 | F3 |
| 12 | H01 x T-type | same card, second need | SWD suppressed in two absence rat models; abstract only | F3 | F3 | F3 |
| 13 | E02 x lactate/LDH | tool compounds, engagement | tool inhibitors, liver oligonucleotide, fly genetic precedent; candidate itself 9.9 percent at 500 micromolar; exposure gap | F3 with counter tag | F3 | F3 |
| 14 | E02 x mitochondrial respiration | nothing recorded | no pertinent row | P3 | P3 | P3 |
| 15 | H02 x myelination | harm only | seven harm rows (vigabatrin: label, rat, dog, case reports), no favourable row | C3 | C3 | C3 |
| 16 | H02 x seizure | same card, other need | CPP-115 rat spasm model (abstract) and one child on concurrent vigabatrin | F3 (thin) | F3 | F3 |
| 17 | I01 x PDH axis | harm outside | MELAS trial neuropathy and paediatric follow-up harm; engagement unresolved | C3 | C3 | C3 |
| 18 | I01 x lactate/LDH | engagement benefit beside trial null | blood lactate benefit row, paediatric randomised null | F3 | F3 | F3 |
| 19 | I01 x seizure | all null/harm | adult mouse models null or slightly proconvulsant | C3 | C3 | C3 |
| 20 | E01 x ISR | limited reading depth | four rows, all abstract only | F3 (thin) | F3 | F3 |
| 21 | B01 x PTC read-through | favourable precedent, no WWOX observation on the need | benefit in an unrelated nonsense allele, one phenotypic null | P3 | P3 | P3 |
| 22 | A03 x protein rescue (and the other abstentions) | missing premise | card abstains, `NO_DRUG_ASSERTIONS_SUPPLIED` | P1 | P1 | P1 |

Also checked and agreed: A01, A02 F3; D01 x Wnt P3; G01 x GSK3beta P3; E03 x PDH F3, E03 x lactate P3, E03 x seizure P3; EB-VGB-01 x myelination and inhibitory hypofunction P3; B02 P1.

## 3. (B) Disagreements with the producer and the code

Two links differ from the code output and one more differs in how it is carried:

1. **EB-KD-01 x seizure**: mine C2, code F2. The producer agrees on the source label (C2) and left the code at F2.
2. **D01 x MYC**: mine C2 (rule text) or F2, code and producer C1. The producer's own alternative reading (P3) is also unsupported, see V1.
3. **C04 x gene addition**: same label (F1), but the carrier list names rows that should not carry it, see V3.
4. **C01 x gene addition**: F1 by the flag list; F2 if the flag vocabulary were applied as it is to EB-ETX-01. The need-level label stays F1 because C04 carries it.

All other 19 links agree.

## 4. (C) Data corrections D1 to D5 against their sources

| id | claim | verdict | what I read |
|---|---|---|---|
| D1 | DR-E02-004: stiripentol racemate 9.9 percent inhibition of human LDHA at 500 micromolar, IC50 above 500; sign benefit to null | Verified | Rico-Molina 2024 Table 2: "Stiripentol ((+/-)-1) 9.9 +/- 2.3, > 500"; footnote a: n = 4 replicates at a single concentration of 500 micromolar. The enantiomers are 34.0 and 38.4 percent, IC50 above 500. The null is correctly worded as poor engagement of the candidate itself. |
| D2 | new row DR-E02-007: effective LDH concentrations 42 to 500 micromolar above therapeutic; free brain 0.2 to 1 micromolar | Verified, two wording points | Bacq 2024 (Biocodex authors): "the effective concentrations on the LDH target (42-500 microM) are globally higher than therapeutic concentrations"; free brain/hepatic 0.2 to 1 micromolar. The row basis says "LDH is not the dominant mechanism in vivo"; Bacq says only that high concentrations were needed, "suggesting that other MoAs were involved". The card direction for this assertion is UNKNOWN while the pertinence sign is null (V8). |
| D3 | DR-D01-002 CTIP2: no recovery; flag `endpoint_downstream_of_need` | Verified as a fact; the position built on it is not (V1) | Manifest PMID 42397075 entry [23] and the paper text: "no change in CTIP2+ neurons"; CTIP2+ about 0.3 percent vs wild type about 12.5 percent (four stars), ns knockout vs A51. |
| D4 | DR-H01-002 benefit and DR-H01-003 null on the seizure need | Verified | Abstract 40165594: reduced generalised convulsive seizure severity in audiogenic mice and in the mouse maximal electroshock threshold test, "albeit at higher concentration"; "no effect on focal onset seizures" (amygdala kindling rat). The abstract-level reading is correctly flagged. The absence-model SWD rows (DR-H01-001) stay on the T-type need only (V10). |
| D5 | comparators of survival and motor rows to `untreated_same_genotype` | Verified | Figure 3 caption: high dose "significantly extended survival relative to the LD group (p < 0.0001) and the KO + RI controls (p < 0.0001)"; RI is the "reference item" and the Results call the RI-injected knockout "untreated Wwox-null controls". Supplementary S4A: KO about 3.6, LD about 1.8, HD about 0.3 (figure attestation). The correction is right, with the carrier consequence in V3. |

## 5. (D) Guard pin and diff of the three functions

The pin `e94c0aae178aaf2d` equals the SHA-256 (first 16 hex) of the concatenated source of exactly `classify_rows`, `assign_need_position` and `overview_positions` in `da31daff`. `overview_positions` is unchanged.

Diff of `framework/scripts/repurposing_view.py` against `9c39392f` (the merge base shown by `git merge-base` is `05fd12b1`; the file diff is the same 78 lines): inside the three functions it contains exactly the following, and nothing else.

- R1: `te` list; `o_counter` adds engagement rows with sign null or harm.
- R2: `support = o_fav + n_engagement_fav` computed before the C3 test; C3 requires `support == 0`.
- R3 facts: `shallow`, `n_basis`, `downstream` returned by `classify_rows` (used only for tags).
- R4: `READING_FLAGS` / `DESIGN_FLAGS` split into `clean_read_any` / `clean_design_any`, `weak_reading` / `weak_design`; the F1 test (`firm`) is unchanged.

Outside the three functions (not hashed): the constants, `card_compounds`, `sibling_counters`, tags in `build_curated`, `CRIT_IT`. The union of the eleven weakening flags is identical before and after (old tuple vs `READING_FLAGS + DESIGN_FLAGS`), so R4 cannot move a position.

Observations on the pin: (a) R1 and R2 do change position logic (I01 x lactate C3 to F3; H01 x seizure P3 to F3 is data D4). The test message calls the pin "rules untouched" while it is re-pinned for a rule change; the producer states this openly, which is acceptable. (b) The pin hashes display-only facts (`shallow`, `downstream`) so any later tag tweak will force a re-pin, which dilutes its meaning; (c) the module constants that decide positions (`FAV_SIGNS`, `FIRM_DEPTHS`, `WWOX_KINDS`, `OUT_KINDS`, `NOT_RECOVERY`, the two flag tuples) are not in the hash, so a change there passes the guard (V7).

## 6. (E) Categories and EB-KD-01

Simplify or multiply? Positions: no change, still nine ids in three families. R2 removes an asymmetry (C3 and F3 used different notions of support) and R1 lets engagement nulls travel the same counter path as other nulls; both simplify. R4 adds one criterion line (four to five). What does grow is the tag layer: tool compound, counter outside WWOX (now also on P3), P3-only-because, reading depth, downstream, sibling, F1 qualifier and not-recovery count, eight free-text tag kinds, four added in this iteration. Net: the position set is simpler, the tag layer is becoming a second taxonomy. Recommendation: no further tag kind unless one is retired; fold "reading depth" into the criteria line where the other reading facts already sit.

EB-KD-01. Yes, fix now, as a card change and not a rule change.

- Evidence. Chong 2023 (PubMed 36537114): "epilepsy that responded to a ketogenic diet in three patients". Riva 2022 (PubMed 35573960, Results, Clinical Features): "The ketogenic diet did not significantly improve seizures and was suspended" in a child with a stop variant on one allele and an exon 6 deletion on the other (biallelic null, first-day onset). Both are WWOX clinical case reports on the same need; by rule 3 a favourable and a null WWOX case-report row together give C2, exactly as for EB-VGB-01.
- The repository already knows it: `needs/needs.json` lists the Riva ketogenic failure as counter-evidence for the seizure need (discovery-ledger entry DL-MOL-007), and the EB-KD-01 `known_roads_state` quotes the sentence. The view therefore prints F2 for the card on a page whose need record carries the contradicting case. That is a displayed inconsistency, not an open scientific question.
- Cost: one assertion, one pertinence row, rebuild of card and packet (`input_sha256`), view regeneration. No code change, pin unaffected.

Proposed assertion (append to `input.drug_assertions` of `cards_early/EB-KD-01.card.json` and the packet, then rebuild):

```json
{
 "id": "A-KD-4",
 "target_id": "seizure_burden",
 "endpoint": "clinician-reported seizure control on the ketogenic diet",
 "direction": "NO_CHANGE",
 "source": "Riva 2022, Front Pediatr (PMID 35573960, PMC9100683); one patient; carried by CLAIM 001 / DL-MOL-007",
 "locator": "Results, Clinical Features: «The ketogenic diet did not significantly improve seizures and was suspended.»",
 "epistemic_status": "DATO",
 "reading_depth": "complete_fulltext_read",
 "context": {
  "disease_id": "WOREE (WWOX-related epileptic encephalopathy)",
  "genotype": "biallelic null: stop variant on one allele and an exon 6 deletion on the other; first-day-of-life onset",
  "species": "human",
  "cell_type": "NOT_APPLICABLE_WHOLE_ORGANISM",
  "developmental_stage": "paediatric"
 },
 "note": "n = 1; one sentence in a diagnostic case report; diet duration, ketosis level, seizure counts and the criterion for 'significantly' are not stated; other levers were also tried and failed in the same child. A reported null, not a controlled comparison. Whether this child overlaps the Chong series is not expected (different centre and report) but is not stated."
}
```

Pertinence row (tab-separated, same columns as the file):
`EB-KD-01	A-KD-4	NEED-SEIZURE-CONTROL-SYMPTOMATIC	card	case_report_wwox_clinical	null	yes	no	case_level;reported_null;no_instrument;uncontrolled;duration_and_ketosis_not_stated;biallelic_null_first_day_onset	reported null effect of the ketogenic diet on seizures in one biallelic-null child; the other half of the Chong benefit count	none_uncontrolled_case_report`

Expected result by rule: EB-KD-01 x seizure F2 to C2; no other link moves. The reading-depth tag will not fire (A-KD-1 is partial read, A-KD-4 complete read).

## 7. Defects

| id | severity | defect | evidence | proposed fix |
|---|---|---|---|---|
| V1 | High | D01 x MYC is labelled C1 ("the only signed result is the null") because DR-D01-001 is flagged `comparison_with_wild_type_only;not_a_recovery_comparison` and so counts neither way. The source does not support that flag. | PMID 42397075 Results: "We observed a marked reduction in both progenitor populations" after A51 in knockout organoids, i.e. treated vs untreated knockout. Manifest entry [23]: SOX2+MYC+ about 72 (knockout) to about 50 (A51), brackets "***, ** and ns" in the order wild type vs knockout, knockout vs A51, wild type vs A51; SOX2+ the same pattern. The producer wrote "not re-opened" and took the flag from the ledger entry as quoted in the card. The paper was read (30 locators, strict pass); the card holds depth at UNKNOWN on purpose, which also makes the new depth tag say "none read beyond abstract" for a paper that was read. | Re-code DR-D01-001 as `readout_in_wwox_system`, sign benefit, comparator `untreated_same_genotype`, drop `not_a_recovery_comparison`; keep the weakening flags the source supports (no blinding, no treated wild-type arm, multi-kinase compound). Position then follows by rule: favourable (depth UNKNOWN keeps it below F1) beside the downstream null gives C2; if the downstream row is to be excluded from the need, the result is F2 plus the downstream tag. State the choice in the rules file. The producer's next-step question ("does normalisation survive an untreated-knockout comparison") is answered by the paper. |
| V2 | High | EB-KD-01 x seizure shows F2 although the repository's own need record and the card's known-roads note carry a contradicting case; source label C2. | Section 6. | Add A-KD-4 and the pertinence row above; rebuild card, packet and views. |
| V3 | Medium | The F1 "carried by" list for C04 x gene addition names five rows including the two low-dose partial-benefit rows (DR-AAV-SURV-LD, DR-AAV-MOTOR-LD), whose own basis says "not counted as recovery" and whose survival ends at zero by about day 77. `firm` in `classify_rows` accepts any favourable sign including `partial_benefit`. The test now pins `len(carrier) == 5`, fixing the defect in place. The position itself is unaffected (the high-dose rows carry it). The motor row (S4A) is figure-attested ("pixels cannot be quote-matched") yet carries no `graphical` flag. | Output of the page data for C04 x gene addition; manifest PMID 42422765 entry [27]. | Restrict `firm` to `benefit` and `normalised_vs_wild_type`, or exclude rows with `low_dose_arm`; assert the carrier ids, not their count. Flag the S4A row as graphical. (Any change inside `classify_rows` re-pins the guard.) |
| V4 | Medium | The reading-depth tag is computed over all signed rows of the position, so a fully read counter row hides abstract-only favourable rows. H01 x T-type: three favourable/null rows are abstract only, the harm row DR-H01-004 is `complete_fulltext_read`, so no depth tag is printed; H01 x seizure does print it. | `shallow` uses `any(depth in FIRM_DEPTHS for r in basis)`; links dump for H01. | For F positions compute `shallow` over favourable rows only; for C positions over the counter rows. |
| V5 | Medium | F1 versus F2 depends on hand-entered flags with no mechanical definition. C01 (SWD, one vector level, one week of recording, n = 5, single channel, "limited cohort", no replication) has no `one_experiment` flag and is F1; EB-ETX-01 has it and is F2. The lithium row is a figure attestation without a `graphical` flag. The need-level F1 survives because C04 carries it. | Pertinence flags; manifest entries [27], [28] of PMID 32000863. | Write the flag definitions in the rules file (what counts as one experiment, graphical) and apply them uniformly; decide C01 explicitly. |
| V6 | Low | The "downstream of the need" tag is applied to D01 but not to EB-ETX-01 x T-type, whose only WWOX row is a seizure score with no T-type measurement. | Section 2 row 7. | Flag the ETX T-type row `endpoint_downstream_of_need`, or drop the distinction. |
| V7 | Low | The guard hashes three functions only; the constants that decide a position (`FAV_SIGNS`, `FIRM_DEPTHS`, `WWOX_KINDS`, `OUT_KINDS`, `NOT_RECOVERY`, `READING_FLAGS`, `DESIGN_FLAGS`) and the display-only facts inside `classify_rows` are not separated. | Section 5. | Hash the constants too and keep display-only facts in a separate function. |
| V8 | Low | DR-E02-007: pertinence sign null versus card direction UNKNOWN; "not the dominant mechanism in vivo" is stronger than the source; E02 F3 still rests on engagement rows coded benefit at 500 micromolar (DR-E02-005, about 40 percent, second-hand) beside the new 9.9 percent at the same concentration; DR-E02-001 not opened (the producer lists it as open item U1). F3 is still the right label because of the tool compounds and the fly precedent. | Sections 4 and 2 row 13. | Align the card direction; soften the basis wording; open U1. |
| V9 | Low | EB-PDANCHOR-AX-01 has no linked need and therefore appears under no position. | `positions` output. | List it in the view as "no linked need". |
| V10 | Low | D4 maps the generalised and focal rows to the seizure need but leaves the absence-model SWD row (DR-H01-001) on T-type only, although SWD is the endpoint C01 uses on gene addition. F3 is unchanged either way. | Abstract 40165594. | Decide whether SWD belongs to the seizure need. |

Blocking for sign-off: V1 and V2 change labels on the page (two card-need links). V3 to V5 change tags and carrier lists, not positions, except V5 for C01 alone. Everything else is presentational. The guard hash and the five data corrections are otherwise sound; the tests are green.

No registration, e-mail, contact, spend or access-control step was performed.
