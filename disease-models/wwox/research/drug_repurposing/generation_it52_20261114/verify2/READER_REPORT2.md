# READER_REPORT2: independent read of AFTER (verify2) against the originals, levers L1, L2 (judged), L3, L6 (controls)

Non-canonical research material. Not medical advice. Reference genotype class only. No compound is recommended and no ranking, need or qualification is changed. Written in English as required for files.

Paths below are relative to `disease-models/wwox/research/drug_repurposing/` (D) unless stated. BEFORE = `D/generation_it52_20261114/baseline_levers_L1_L2_L3_L6.tsv`. AFTER = `D/generation_it52_20261114/verify2/after2_rows_L1_L2_L3_L6.tsv` (4 rows; the new content sits in `design_join`, `lever_attachments`, and in how lever cells are placed in slots). Originals read in full: ADV-006 `measurements.tsv` (28 rows), `conflicts.tsv` (25 rows), README; SCI42 `new_measurements.tsv`; SCI47 `README.md`, `levers.tsv`, `levers_notes.md`, `matrix.tsv`, `design_review.md`; ADV-004 `README.md`. I also read ADV-006 `output/order.md` and one line of `commit_candidates/CC-20260826-EGABA-EXPERIMENT-01.md` (to see what "this order" is). The owner table `levers_owner_confirmation_presidio001_20261114/confirmation.tsv` was read as a claim, and where I use it I say so. No other file under `generation_it52_20261114` was opened. I did not open `conditional_design_steps_it50.tsv`, so R21 is partly unchecked.

Ids: M01..M28 and CF.. are ADV-006's. SCI42's own M01..M10 are another space (translation, from ADV-006 `measurements.tsv` `requests_merged`: SCI42 M03 = ADV-006 M01, M04 = M02, M06 = M03, M05 = M04, M01 = M05, M07 = M06, M02 = M08, M08 = M09, M09 = M11, M10 = M15). I checked every M-id that appears in AFTER's L1/L2 text against this. No id is read in the wrong space in L1 or L2 (details in section 4).

---

## 1-3 and 7. The propositions, source check, epistemic type, verdict

Type key: OBS = states an observation; COND = the sources' conditional reading (if X is shown, then Y is interpretable or favoured); DEP = dependency or priority order; DESIGN = a design requirement or comparator; OWNER = an owner's reading (the confirmation table).

### R1. L1 and L2 are "interpretable only after" mIPSC, agonist response and E_GABA (ids M02, M04, M05)
- AFTER (L1 and L2 `design_join`): "its `interpretable_after`, quoted, is the sources' conditional reading and not an observation: 'M02, M04, M05 ("A GABA-supply arm (L1) or a postsynaptic-modulation arm (L2) is interpretable only after mIPSC, agonist response and E_GABA place the deficit." (README.md, answer 3))'". Also prints `rows named at the start of that cell: M02, M04, M05`.
- Source: SCI47 `README.md` answer 3, verbatim "A GABA-supply arm (L1) or a postsynaptic-modulation arm (L2) is interpretable only after mIPSC, agonist response and E_GABA place the deficit."; ADV-006 `measurements.tsv` M16, column `interpretable_after`: `M02, M04, M05 ("A GABA-supply arm (L1) ...` and M16 `lever_or_comparison_gated` = "is itself the lever L1". M02 = mIPSC, M04 = agonist response, M05 = E_GABA, so the ids are right.
- Type: COND / DEP of interpretation. AFTER keeps the "not an observation" label. It does not say that this is a dependency of interpretation and not a run order. ADV-006's own `order.md` D5 and the owner row 3.02 say "Dependency of interpretation, not an order of running", so AFTER says less than the originals here.
- Limit: the README triple is narrower than L1's own status cell ("kept, conditional on O01/O04/O06 mapping to E2 (and E_GABA not above threshold)"). The owner row 4.03 (OWNER) calls the real gate the union: event identity (O06, ADV-006 M01), mIPSC, agonist response, E_GABA. AFTER prints both triples (status in `premise_and_action`, README in `lever_attachments`) and never reconciles them. M01 and M03 are absent from `interpretable_after`.
- Verdict: SUPPORTED (for what it says). The gate set is under-stated relative to L1's status cell.

### R2. L2 "stays gated by the Phase-0 measurements" (ADV-004 update), again with ids M02, M04, M05
- AFTER (L2 `design_join`): `M02, M04, M05 ("L2 stays gated by the Phase-0 measurements and is not ungated by this reading." (README.md, Update 2026-11-14))`.
- Source: ADV-006 M17 `interpretable_after`, identical text. SCI47 `README.md`, Update 2026-11-14: "L2 stays gated by the Phase-0 measurements and is not ungated by this reading."
- The quote names "the Phase-0 measurements" (SCI47 design_review Phase 0 list (i)-(vii) = M01, M02, M03, M04, M05, M07 and burst status). The three ids in front of it are ADV-006's selection and are not in the quote. The quote says MORE than the ids: for L2 the gate is Phase 0 as a whole.
- Type: COND/DEP. Label kept.
- Verdict: PARTLY. The quote is exact. The id list that heads it is narrower than the quote.

### R3. M01 (sIPSC re-record) is a "second-hop row, NOT followed (an order of cost or priority may sit there)", with CF01 and CF03 "for the reader to weigh"; the same row elsewhere treats M01 as first hop
- AFTER (L1 and L2 `design_join`): "second-hop rows named by the gating rows, listed and NOT followed (an order of cost or priority may sit there): M01; genuine conflicts on them, for the reader to weigh: CF01, CF03". AFTER L1 `lever_attachments`: "ADV-006 rows whose requests_merged names an attached matrix row: M01, M02, M03, M04". AFTER L2 `lever_attachments`: "ADV-006 row M01 (...): owners' reading: first hop for the lever; no declared key of this row reaches it (owner-stated, SCI PRESIDIO-001)".
- Source: ADV-006 `order.md`: "The first-then-second order of M01 (sIPSC re-record) and M05 (E_GABA) is a cost and priority order ("cheapest"), not a dependency". SCI42 `new_measurements.tsv` M03 `separates`: "It is the cheapest and goes first." SCI42 M05 and M06 `required_from_start`: "no (required if M03 confirms the amplitude loss)". SCI47 lists the agonist response unconditionally (CF22, typed gap). ADV-006 `measurements.tsv` M01 `requests_merged` names matrix O02, O03, O06, O10, O18, so by AFTER's own rule M01 is reached for L1 (O02, O06, O10) and for L2 (O02, O03).
- What AFTER does: it keeps cost or priority apart from dependency ("an order of cost or priority may sit there"; "no order here is a result"). It does not convert cost into dependency. But "may sit there" does not say which of two different things it is. There are two: (a) SCI42's README order (cost/priority) and (b) SCI42's "required if M03 confirms the amplitude loss" (result-conditioned, in SCI42 only; CF22 is the difference). CF22 appears in the L1 and L2 lists only as "CF22 (gap)", with no content, so the one result-conditioned order in the originals is unreadable from AFTER.
- Internal inconsistency in the same row: M01 is "second hop, NOT followed" in `design_join` and "first hop for the lever" (L2) or a member of the first-hop group (L1) in `lever_attachments`. The owner table (rows 1.41, 3.04, 3.05; OWNER) corrected exactly this ("For L1, M01 is first-hop through O06 ... a precondition, not a cost order"). AFTER carries both statements.
- Verdict: PARTLY. No over-read, but the statement is non-committal and self-inconsistent, and it hides the one real conditional order.

### R4. M03 (evoked IPSC) is first hop for L1 and L2
- AFTER L2: "ADV-006 row M03 (Evoked IPSC ...): first hop through O01/O05 in ADV-006's M03". AFTER L1 lists M03 in the M01-M04 group.
- Source: ADV-006 M03 `requests_merged` = "... sci47_inhibitory#matrix:O01 ; sci47_inhibitory#matrix:O05 ; ..."; M03 `lever_or_comparison_gated` = "L1 versus L2 selection (matrix O05)".
- Type: structural attachment (which measurement row speaks to the lever). Not an order.
- Verdict: SUPPORTED.

### R5. A matched non-GABAergic comparator is required for every drug arm; comparator and control cohorts
- AFTER L1: M16 `cohort_and_genotype_arms` 'against M15 and non-Wwox hyperexcitable slices'; "rows whose `lever_or_comparison_gated` names M16 as a whole token ...: M15 'every drug arm (M16, M17, M18, M19, M20)'". AFTER L2: M17 arms 'age-matched wild type under driven bursts (SCI42) and wild-type baseline (SCI47): CF16'.
- Source: ADV-006 M15 `lever_or_comparison_gated` = "every drug arm (M16, M17, M18, M19, M20)" and `indispensable_or_substitutable` = "co-requirement of every drug arm ("yes (for any drug arm)" (new_measurements.tsv, M10:required_from_start))". M16 `cohort_and_genotype_arms` = "against M15 and non-Wwox hyperexcitable slices". M17 = "age-matched wild type under driven bursts (SCI42) and wild-type baseline (SCI47): CF16". CF16 (gap): "(they are additive comparators)". SCI47 design_review (e): "(2) wild-type slices given the same drug at the same concentration, to see the baseline effect and the floor; (3) a non-Wwox hyperexcitable slice preparation brought to a matched baseline burst rate, with the caveat that its burst mechanism may not be NMDAR-dependent".
- LESS than the sources: AFTER prints only the gated-cell fragment, not the word "co-requirement" or SCI42's "yes (for any drug arm)". It also drops the design_review (e)(3) caveat about the non-Wwox preparation. The two-metric rule and the time-matched vehicle (SCI42 M10 `control_for_null`, "Quantified on two metrics (charge; peak or slope); time-matched vehicle and washout") are not carried.
- Type: DESIGN requirement. AFTER prints it as a gating relation, not as an observation. The distinction holds.
- Verdict: SUPPORTED as quoted; under-delivers the requirement and the caveat.

### R6. Conflicts that bear on the arm: genuine CF04, CF05a, CF05b, CF23; gap and synonym rows named as "not conflicts"
- AFTER L1/L2 `design_join`: "conflicts of type genuine whose m_id names any of M16, M02, M04, M05, M15: CF04 [...]; CF05a [...]; CF05b [...]; CF23 [...]", then "rows of other types (gap or synonym: not conflicts)": L1 CF06, 07, 08, 09, 10, 11, 12, 12b, 13, 14, 15, 17, 21, 22; L2 the same plus CF16.
- Source check (ADV-006 `conflicts.tsv`): CF04 m_id "M02", genuine; CF05a "M01;M02;M05", genuine; CF05b "M01;M03;M05", genuine; CF23 "M15", genuine. Types of the gap/synonym list match the file (CF08, CF10, CF12b synonym; the others gap). All printed quotes match. The L1 list correctly omits CF16 (m_id M17;M11) and L2 includes it.
- Problem 1, preparation moved without saying so. ADV-006 README answer 3: "Across the August design's preparation (2): CF04 mIPSC in a perforated cohort (SCI47) against whole-cell high-chloride after rupture (August design); CF05a same-cell sequence (August design) against two nested cohorts (SCI47)". The August side (`CC-20260826-EGABA-EXPERIMENT-01`) is the global Wwox allele, CA3 primary, other age windows (ADV-006 M14, CF06/CF07). AFTER prints the CC file path in the quote but never says that this side is another line and preparation. A reader of L1/L2 (Synapsin-Cre slice, layer II/III, P13-17) takes CF04 and CF05a as conflicts inside the arm's own preparation.
- Problem 2, the conflict's consequence is not printed. AFTER prints `cell_type`, the two quotes and `adjudicable_from_the_packages`. It omits ADV-006's `why_both_cannot_be_met_in_one_recording` and `which_would_change_the_interpretation`. For CF03 this matters most: the reason is that "A glutamate-receptor block present in the bath removes the NMDAR-dependent burst", and AFTER prints only "Re-record sIPSC with glutamate-receptor block ..." beside "(vii) KO slices that do and do not burst." with no reason.
- Problem 3, the one literal order among recordings is printed without its content. CF05a quote: "One cell yields both measurements only in this order". The CC source (section 3b) completes it: "perforated first, ruptured second, never the reverse". AFTER leaves "this order" undefined. AFTER also calls the order "a design claim" tested by no recording. The CC text presents it as a constraint of the cell: rupture is terminal and the whole-cell E_GABA is "meaningless".
- Type: documentary disagreement between design texts, not an observation. AFTER labels type and adjudicability and takes no side. Distinction kept.
- Verdict: PARTLY (ids, types, quotes SUPPORTED; preparation shift, consequence and the content of "this order" missing).

### R7. CF23 owner note: "A tension inside SCI47, incomplete, not wrong ... no side is taken"
- AFTER (L1, L2, L3 `design_join`): the owner note (SCI, PRESIDIO-001 blind reader) that SCI47 design_review (b) gives a reason against matching a reuptake arm on membrane potential and input resistance (the matched measure there is tonic current or sIPSC decay), and "says nothing about SCI42's variable".
- Source: design_review (b): "'same measured cellular effect' is a membrane-potential and input-resistance shift for A, but a reuptake blocker acts on membrane potential only through GABA-A conductance (tonic current), not as a direct hyperpolarisation; its matched measure would be a tonic current or sIPSC decay, a different quantity." Fix: "calibrate each arm on its own cellular readout and then on a shared, arm-independent readout (the LFP burst rate and a fixed fraction of cells' rest/threshold)". SCI42 M10 `matching metric`: "the matching metric (a design choice)". `conflicts.tsv` CF23 `adjudicable_from_the_packages`: "yes: SCI42's own design_choice_not_finding cell calls the metric a design choice; SCI47 does not give a reason". The owner note is correct: design_review (b) addresses p9's design (lever B = reuptake block), not SCI42's "percent of evoked synaptic charge removed". The note is also what makes ADV-006's "SCI47 does not give a reason" incomplete.
- AFTER prints ADV-006's "adjudicable ... yes" and then the correction. That is two statements side by side. It chooses no side. Slight tilt: "yes" printed first. The design_review (b) Fix (shared readout) is not printed, so the reader sees a "tension" with only one half of what (b) says.
- Verdict: SUPPORTED. This is real new content for L1 (L1's own comparator cell uses the membrane-potential/input-resistance match that (b) argues against for a reuptake arm).

### R8. CF01 "NOT attached: SCI47 is not consistent on the sIPSC configuration"
- AFTER L1 (and L3) `lever_attachments`: "CF01 NOT attached: SCI47 is not consistent on the sIPSC configuration (its Phase 0 item (i) asks a pipette-set chloride, its cohort sentence names perforated native chloride): stating the conflict for a lever needs a choice that is the owners'". AFTER L2: CF01 appears only as an id in the second-hop list and in the 53-row list. No sentence.
- Source: design_review Phase 0: "the minimum that survives is a perforated-patch cohort for native-chloride sIPSC, mIPSC and evoked IPSC plus puffed agonist ... (i) sIPSC with a physiological-chloride pipette and with the high-chloride pipette in different cells". ADV-006 README update point (1): "CF01 is typed genuine and quotes only SCI47's cohort sentence; item (i) of the same Phase 0 asks the pipette-set physiological-chloride sIPSC ... so the typing is too strong". Confirmation 3.06 (OWNER): CF01 "belongs to L2 by L2's own words": L2's gate is "E3 ... in physiological chloride" and its action cell says "confirm the deficit with a physiological-chloride pipette".
- AFTER L1 is correct. AFTER L2, the lever whose own gate uses the words "physiological chloride", gets CF01 as a bare id with no content, and it prints CF01 in the design_join as "genuine" under "for the reader to weigh" (ADV-006's typing, which ADV-006's README update calls too strong).
- Verdict: SUPPORTED for L1; NOT SUPPORTED as delivered for L2 (the L2 row does not carry what its own gate needs).

### R9. CF03 attached to L2 "by the owners' reading (unverified when built): the E5 stratification side"
- Source: CF03 (M01 only; genuine; adjudicable "partly (the sequence is not stated by either source; the conflict is simultaneous only)"). SCI47 matrix O10 and levers_notes E5 ("L1/L2 treat a consequence") are the E5 content. Confirmation 2.07, 3.07 (OWNER) attach O10 and the E5 row to both L1 and L2.
- AFTER L2 attaches CF03 "the E5 stratification side" but does not attach the E5 row, O10 or the burst-status measurement (SCI47 design_review Phase 0 item (vii)) to L2 at all (L2 lists E1, E3, E4 and O01, O02, O03, O05, O14 only; checked in the row). So the conflict is attached to a lever without the observation it is about.
- Verdict: PARTLY.

### R10. Attached matrix observations and their outcome and decision cells
- AFTER L1: O01, O04, O06 (named by L1's status), O02, O05 (route E via E2), O10, O14 (route E via E5). AFTER L2: O01, O02, O03, O05, O14 (route E). Plus O12 (both, owner-stated).
- Source check: every quoted cell matches `matrix.tsv` (O01 "[measured] sIPSC mean amplitude 57.3 -> 27.5 pA (-52%, own arithmetic); KS on events p 9e-135; 14 cells/7 animals vs 9/5; 140 mM KCl, -70 mV, no antagonist"; O04 "[declared] no miniature IPSC (TTX) recording"; O06 "[declared] no GABA-A antagonist or glutamate-receptor antagonist named for sIPSC ... [measured] sEPSC KO mean amplitude 24.7 pA and frequency 10.1 Hz are close to the KO 'sIPSC' 27.5 pA and 8.4 Hz"; etc.). Route-E labels are correct for O01, O02, O05 (outcome cells name E2 and E3/E1) and for O14 (E4/E5).
- Epistemic type: the `[measured]` / `[declared]` tags are kept. `what_each_outcome_would_favour` is COND in form ("if ... ->"). `pharmacological_decision_it_would_change` mixes COND and dependency in the package's own voice ("Required before any presynaptic (supply) versus postsynaptic (receptor) lever is chosen" (O04); "without it no GABA-A, supply or chloride lever has a measured target" (O06)). AFTER prints them under their field names with no further label. The `why` column, where the package marks `[inferred]` and the V9 qualifiers, is not printed, so the inference status of these decisions is lost. Examples: O14 `why` has the omitted conditions of the −67 mV value; O01 `why` has "[inferred] ... a mean fall can come from fewer large inputs (E1), smaller quanta (E2) or fewer or less responsive receptors (E3)".
- Errors or inconsistencies in the selection: (a) The label "route E ... the same rows reach the other GABA lever, so this route does not separate them" is printed for O10 on L1, but AFTER's L2 row does not attach O10 (and E5 is not in L2's cells), so by AFTER's own rule the sentence is false for O10. (b) L1 has no O03 although the owner row 2.13 (OWNER) says O03 and O14 attach to both, and L1's own status says "E_GABA not above threshold". (c) Only rows named in the lever's own cells print `compatible_explanations`, `weakened_explanations` and `discriminating_measure` (L1: O01, O04, O06). Route-E rows print only observation, outcome and decision. L2 names no matrix row, so none of L2's rows print a discriminating measure. (d) AFTER L1 prints "14 cells/7 animals vs 9/5" with no qualifier. SCI47 O16 (V9) says the component animal counts do not sum (4+4 = 8 against 7), the KS unit is undeclared, and there is no animal-level statistic. O16 is not attached to L1 or L2 (the owner row 2.16 leaves it unattached on purpose as a package-level caveat).
- Verdict: SUPPORTED on text; PARTLY on selection and on the omitted `why` qualifiers.

### R11. Explanation-to-lever table: E2 and E5 for L1; E1, E3, E4 for L2
- Source: `levers_notes.md` rows E1-E5, text exact ("mIPSC amplitude down, agonist response normal | E2 (supply per event) | L1 GABA availability | L2 starts from normal receptors", etc.). AFTER prints them verbatim and labels them "the explanation-to-lever table".
- Asymmetry: the rows that name the other lever by id are not attached. E3's "lever that does not" cell says "L1 raises a signal onto fewer receptors"; E1 "L1 and L2 act on a smaller input set"; E4 "boosting GABA is conditional and may aggravate". None is attached to L1. E2 ("L2 starts from normal receptors") and E5 ("L1/L2 treat a consequence") are not attached to L2. So L1 is missing its own "not interpretable if E3" rule and L2 its "not interpretable if E2" rule.
- AFTER does not carry the table's own caveat: "Nothing in PMID 34634460 chooses a row (matrix O01-O06)" and "(protocol-level; no single cause is chosen)". The row labels "if the recordings show:" keep it conditional.
- Type: COND. Distinction kept.
- Verdict: SUPPORTED (text); PARTLY (coverage).

### R12. E_GABA gates L1 and L2 (L3's status); L4 names L1/L2 as arms to compare at equal recorded effect
- Source: `levers.tsv` L3 status "dropped as a drug arm now; E_GABA kept as the measurement that gates L1 and L2"; L4 `functional_comparator` "matched hyperpolarisation (L5) and GABA arms (L1/L2) at equal recorded effect". Verbatim.
- Mostly repetition of BEFORE's L3 row and L4 row for L1 and L2.
- Verdict: SUPPORTED.

### R13. "Already-used antiseizure drugs" (conditions for adding anything over general anticonvulsant action)
- Source: `levers_notes.md`, verbatim: "If a GABA-transaminase inactivator or a benzodiazepine-site drug is the compound under test, the rationale adds nothing over general anticonvulsant action until (i) the deficit is confirmed in physiological chloride with identified events and (ii) the matrix row that points to supply (E2) or receptor (E3) is shown. A lower burst incidence under such a drug would be read against a matched non-GABAergic arm and a non-Wwox hyperexcitable preparation."
- New against BEFORE: "with identified events" and the explicit comparator reading. The rest repeats `adds_over_general_anticonvulsant_action`. Locator is the heading line (levers_notes.md:29, text at line 30), same for design_review.md:17 (heading of (d), text line 18). Cosmetic.
- Verdict: SUPPORTED.

### R14. A burst reduction is not evidence of correction; the defect must move; genotype-by-drug on the defect measure
- Source: design_review (d), "Yes. INFERENZA. ... Burst reduction is therefore not evidence that the lever corrects the Wwox defect. A correction needs the defect itself to move in the right direction (sIPSC or mIPSC amplitude, E_GABA, passive properties) and a genotype-by-drug interaction on that measure, not on the burst alone." README answer 3: "Only one read on the burst endpoint with the defect measured in the same slices, against a matched non-GABAergic arm, and the genotype-by-drug interaction on the defect measure." AFTER prints both verbatim, and the "INFERENZA" label stays inside the quote. This is a requirement written by the package as inference, and AFTER keeps it as one.
- Verdict: SUPPORTED. Real new content for L1 and L2 (BEFORE's rejection cell lists burst-based criteria; "interaction on the defect measure" is new).

### R15. d-APV comparator: "d-APV (50 uM) abolishes bursts in 5 slices/3 animals ... it is the comparator for any inhibitory lever"
- Source: matrix O12, verbatim. README answer 3: "NMDAR dependence (L4, ...) is the generic comparator, not a correction." AFTER does not print ADV-006 M18 ("the abolition is measured (levers.tsv L4); the submaximal arm is not held"), so the reader does not see that the submaximal arm that L1's comparator cell asks for has no source datum. It also does not print O12's "no GABA-A antagonist was applied to WT slices", which is in the printed observation (it is there; M12 as the row for that test is not named).
- Verdict: SUPPORTED.

### R16. How the dropped levers read from L1/L2
- AFTER prints (README#3) "Chloride transport (L3) stays a **measurement** (E_GABA) that gates L1 and L2; gap junction (L6) is dropped" and the L3 status; L6 is otherwise only a title in the list headed "other rows of the same package".
- Source verbatim. See section 5 for the control check.
- Verdict: SUPPORTED. Soft spot: in L1 and L2 the `competing_explanations` slot lists "L3: Chloride transport ..." and "L6: Gap junction or pannexin block ..." as titles without the word "dropped", inside a column named competing_explanations.

### R17. M06 (tonic GABA-A current) as "L1 readout" and as the extrasynaptic class of M17
- AFTER L2 only: "rows whose `lever_or_comparison_gated` names M17 as a whole token: M06 'the extrasynaptic modulator class of M17 (SCI42 conditional_prediction row 9); L1 readout'".
- Source: ADV-006 M06 `lever_or_comparison_gated`, verbatim. `conditions`: "GABA-A block alone; with and without uptake block; fixed ambient GABA".
- Asymmetry: for L1, the lever whose action cell asks for "a change in the recorded cells (sIPSC decay, tonic current)", AFTER does not mention M06, because the join keys on the token "M16" and M06's cell says "L1".
- Verdict: SUPPORTED for L2; omission for L1 (see section 6).

### R18. Preparation and age for the arm: "Synapsin-Cre slice, layer II/III, P13-17"
- AFTER L1: M16 preparation "'Synapsin-Cre slice, layer II/III, P13-17 (L1 row)'" matches ADV-006 M16 and L1's context in BEFORE. AFTER L2: M17 'Synapsin-Cre slice, layer II/III, P13-17'.
- Source: ADV-006 M17 `preparation` reads the same, but unlike M16 it carries no "(L2 row)": the L2 row in `levers.tsv` states no preparation or age; the context is inherited through "functional_comparator: as L1" and SCI47's single design (design_review "Limits": "It stays in the Synapsin-Cre slice at one age"). BEFORE's L2 counter-evidence has "diazepam aggravated events at P11 but not P14". So AFTER gives L2 an age that BEFORE's L2 does not state, without saying it is inherited. The inheritance is defensible. It is unlabelled.
- Verdict: PARTLY.

### R19. ADV-004: "(ADV-004 wording applies unchanged; pointer: gabaa_subtype_adv004_20261114/README.md answer 6)"
- See section 4 for the wording check. AFTER's L2 subtype sentence is identical to BEFORE's.
- Verdict: SUPPORTED (pointer; nothing added beyond ADV-004).

### R20. Build-state statement: "mapping drafted by HE and read by the owners (SCI, PRESIDIO-001, 2026-11-14), whose own blind reader had not reported when this was built"
- The confirmation table carries "[verifier V: ...]" entries, so a reader has since reported. The sentence is dated "when this was built", so it is true as of the build, but the second build still carries it while the table's corrections (rows 1.41, 3.04, 3.05, 4.01, 4.03) are only partly reflected (R3, R8, R10). Not checked beyond the table text.
- Verdict: PARTLY (stale relative to the table; honest about its own date).

### R21. "53 design rows are in conditional_design_steps_it50.tsv for INV-05 ... not linked to this hypothesis by any package (a design is not an observation)"
- The id list printed is M01-M28 plus CF01-CF23 including CF05a, CF05b, CF12b: 28 + 25 = 53, which matches ADV-006 `measurements.tsv` (28 rows) and `conflicts.tsv` (25 rows). "Not linked by any package": consistent with ADV-006 README answer 6 ("no generic mapping covers the thread"). I did not open the it50 file.
- Verdict: SUPPORTED by count; the file claim is not checked.

---

## 4. Side-taking, cost versus dependency, moved contexts, GABA-A subunit wording

- Chooses a side on a disagreement? No, on every point I checked. CF23: both ADV-006's "adjudicable: yes" and the owner correction are printed, and "no side is chosen on any conflict; no order here is a result" closes the cell. CF01: "stating the conflict for a lever needs a choice that is the owners'". The only tilt is presentation: "adjudicable ... yes" is printed before the correction, and CF01 is printed under "genuine ... for the reader to weigh" after ADV-006's own README update called that typing too strong.
- Reads cost or priority as dependency? No. M01 is explicitly "an order of cost or priority may sit there". The opposite error exists: the one result-conditioned order in the sources (SCI42: agonist response and evoked IPSC "required if M03 confirms the amplitude loss", CF22) is reduced to the bare tag "CF22 (gap)". The L1/L2 gate (R1, R2) is a dependency of interpretation. AFTER's label "conditional reading, not an observation" is correct, but it never says "interpretation, not run order", which the originals do.
- Moves a context between preparations or ages without saying so? Yes, in three places. (1) CF04 and CF05a: August-design side (global allele, CA3) attached to a Synapsin-Cre layer II/III arm (R6). (2) L2 inherits P13-17 and the Synapsin-Cre slice from L1 with no "(L2 row)" mark (R18). (3) E_GABA's age: SCI47 O14 and ADV-006 M05 add P11 ("P11 added by SCI47 O14: CF21"). L2's own counter-evidence is an aggravation at P11. AFTER carries P11 only inside the L3 row; the L1 and L2 rows carry O14 without its `discriminating_measure`, so P11 never reaches them.
- Id-space or same-name merges? Checked and found none in L1/L2: every M-id printed is ADV-006's; SCI42's ids inside quotations are labelled (L3: "ids inside the quotation of `interpretable_after`, a source's own id space (SCI42's or SCI47's, not ADV-006 rows): M01"; CF23 cites "SCI42 new_measurements.tsv M10" by file). The one label error is in a control row, L3: the matrix rows O03 and O14 are tagged "named in requests_merged of M05, M20 (declared for this lever)". M05 does name both and declares levers:L3. ADV-006 M20 declares levers:L3 but names neither O03 nor O14 in `requests_merged`, so the tag overstates for M20. Its `requests_merged` is "conditional_prediction r02 ... ; sci47_inhibitory#levers:L3".
- Route labelled "declared" that is not: "owner-stated attachment (SCI, PRESIDIO-001; not reached by a declared key of this row)" is used honestly. The L2 M01 line says "no declared key of this row reaches it", while ADV-006 M01 `requests_merged` names O02 and O03, which L2 attaches by route E. That is a rule difference (E-route is not "declared"), not an error, but it differs from L1's phrasing for the same row.
- GABA-A subunit wording beyond ADV-004? No. L2's `context` sentence is identical in BEFORE and AFTER. ADV-004 README answer 6 "May": "in one laboratory's rat-subunit series NDMC potentiates α2 and α3 more than α1 in efficacy (printed ratio 1.77 ...), the human-oocyte series points the same way on a total-response basis (1.33) and calls it non-selective; ... no independent same-design replication with diazepam exists". AFTER carries a subset: it drops "potency differs little among α1, α2 and α5 and α3 is least potent" and the Hammer parenthesis. "May not" is carried for "α2-preferring" as established and "subtype-discriminating pair", but not the third item "any attribution of an effect in a Wwox slice to α2" (the owner row 2.17 notes this). AFTER's pointer "ADV-004 wording applies unchanged" therefore points at a longer text than the one printed. The 1.33 is derived (README answer 4: "Hammer does not print it"); the printed phrase "points the same way on a total-response basis (1.33)" follows README answer 6 and does not say derived. No effect-in-slice attribution to a subtype is made anywhere in AFTER.

---

## 5. L3 and L6 as controls

- L3: `kind` = "package_row_dropped_by_the_package"; `nomination` = "NOT PROPOSED: the package drops this row (its own status label: 'dropped as a drug arm now; E_GABA kept as the measurement that gates L1 and L2'); kept so the drop is visible"; `design_rows_same_investigation` = "dropped by the package: ... not repeated for a row nobody proposes"; `premise_and_action` = "status: dropped as a drug arm now; E_GABA kept as the measurement that gates L1 and L2"; `expected_result` = "n/a (no arm)". It reads as dropped as an arm and kept as a measurement, matching SCI47 README answer 3 and levers_notes ("Kept as the measurement E_GABA, not as an arm").
- Soft spots in L3: (a) `design_join` joins M05 (E_GABA) and M20, "chloride-gradient arm M20", ADV-006's arm row. M20's own cell says "arm conditional; dropped by SCI47: CF15", but that cell is not printed. CF15 appears only as "CF15 (gap)". So a drug-arm design row is attached to a dropped lever with its drop unmarked in that join. (b) The O03/O14 tag error above. (c) `decision_measure` carries "KO E_GABA equal to control" as a rejection test for an arm nobody runs (same as BEFORE). (d) "CF01 NOT attached" is printed in L3 (CF01 concerns sIPSC configuration, not L3), apparently the same template.
- L6: `kind` dropped, `nomination` "NOT PROPOSED ... (its own status label: 'dropped')", `design_join` = "no ADV-006 measurement row declares sci47_inhibitory#levers:L6 in requests_merged: not joined (not stated is not tested and absent)". Check: no ADV-006 `requests_merged` contains levers:L6 (I listed those that declare levers: M05, M16, M17, M18, M19, M20). Supported. The first slot, `starting_observation_and_chain`, begins "known_in_WWOX: burst frequency -87% with carbenoxolone 100 uM (4 slices, 3 animals)" (same as BEFORE). It sits beside "the effect is not attributable to gap junctions" and "the repository withdrew the gap-junction half of the burst claim on 2026-09-27". SCI47 README adds a V9 note: "SR08 (-87% printed against -96% from the medians)". That is not carried. This is a minor mismatch for a dropped row.
- Does the output make a dropped lever look active? Not in the L3 and L6 rows themselves. In the L1 and L2 rows, L3 and L6 sit as titles under `competing_explanations`, without "dropped" (R16). The README#3 sentence in the attachments says "gap junction (L6) is dropped", so the information is present, but not at the point where the list is read.
- L3 also shows what L1/L2 lack: the K-gluconate caveat from matrix O03 `discriminating_measure` (see section 6).

---

## 6. Actionability for planning the next experiment on L1 or L2

Items that change what the experiment must include, or in what order, compared with BEFORE alone:

1. R14 (README answer 3 and design_review (d)): arms must read the defect measure in the same slices and test the genotype-by-drug interaction on it. Burst reduction alone is "not evidence that the lever corrects". BEFORE's rejection and comparator cells do not contain this. This is the most design-changing item for both levers.
2. R10, O06 (and O01 conditions) for L1: the premise datum (−52% sIPSC) was recorded with 140 mM KCl, −70 mV and no antagonist, and KO sIPSC is numerically close to KO sEPSC. Event identity has to be re-established before the sIPSC fall is a target. BEFORE's L1 states the fall as "measured". BEFORE's L2 action cell already asks "event identity by antagonist".
3. R6/R9 (CF03): a glutamate-receptor block removes the NMDAR-dependent burst, so burst-status stratification and the artefact control cannot be done in one slice at the same time. The experiment needs separate slices or a stated sequence. AFTER prints the quotes but not the reason or the consequence; a reader has to open `conflicts.tsv` to see why.
4. R6 (CF05a/CF05b + the Phase 0 sentence "Not as one protocol in every cell ..."): E_GABA by perforated patch, whole-cell high-chloride IPSC measures, mIPSC and evoked IPSC with paired-pulse "cannot all be run in one cell without compromise [V9]". L2's action cell asks for "mIPSC and agonist response in the same cells". Owner row 3.08 (OWNER) says L2's subset is not excluded by that sentence. The cohort structure still has to be chosen. The CC-side order ("perforated first, ruptured second, never the reverse") is the only technical order, and AFTER leaves it undefined.
5. R7 (design_review (b)): for a reuptake arm, calibrate on its own readout (tonic current or sIPSC decay), then on a shared readout, not on membrane potential and input resistance, which is what L1's comparator cell asks. Changes how L1's comparator is built.
6. R5: a matched non-GABAergic arm for every drug arm, plus wild-type slices at baseline and a non-Wwox hyperexcitable preparation. BEFORE has the matched arm only.
7. R1/R2: no GABA arm is read until mIPSC, agonist response and E_GABA place the deficit, and L2 is not ungated by the subtype wording. In BEFORE the gate is already in each status cell, so this is mostly repetition; what is new is E_GABA as a gate for L2 and the explicit "not ungated".

Pointers or repetition (no change to the experiment): R12 (L3 gate, L4 comparator naming), R16, R19 (ADV-004 pointer), the route-L rows ("levers.tsv row L2 names L1 ... as L1"), the bullets from levers_notes for L1 and L2 (restate BEFORE), R13 (largely restates `adds_over_general_anticonvulsant_action`), the 53-row list (R21), all bare ids of gap and synonym conflicts (they carry no content), the R3 "second-hop" sentence (non-committal).

What the originals show matters for the arm that neither BEFORE nor AFTER reaches:
- Physiological-chloride sIPSC at −70 mV. SCI47 matrix O03 `discriminating_measure`: "K-gluconate-internal sIPSC (pipette about 12 mM Cl, E_Cl about -63 mV by own arithmetic: driving force at -70 mV a few mV, sign undetermined without junction correction) [V9]". It appears only in the L3 row. L2's gate rests on "physiological chloride", and a physiological-chloride sIPSC at −70 mV may be nearly unreadable.
- The −67 mV E_GABA reference (BEFORE and AFTER both use it). Matrix O14 `why` lists the omitted conditions: 22-25 °C against 35 °C here, mean ± SEM (SD about 12.5 mV), pooled cortex and hippocampus, and "Scn1b-null neurons at -51.1 mV" in the same age bin. The "E_GABA not above threshold" gate rests on this value.
- The −52% comparison is KO against pooled controls (O18: "S-CTL pools" WT and HT), with the heterozygote bursting in 4/23 slices and no animal-level statistic (O16, O18). Neither is attached (the owner left O16 unattached on purpose).
- Tonic current as the L1 readout depends on a fixed ambient-GABA and uptake condition (ADV-006 M06; SCI42 M07 "tonic current depends on uptake and ambient GABA (P12: 170 against 12 pA; 9 against 41 pA ...)"). M06 is not joined to L1.
- Age: SCI47 O14 adds P11 to the E_GABA measure. L2's own counter-evidence is a P11 aggravation. The L1 and L2 rows do not print it.
- ADV-006 M08: the age series with survivor-selection control and burst-onset determination, which E5 ("L1/L2 treat a consequence") needs. M08 is listed for L3 but not L1 or L2, although L1 attaches O10 and O14, which M08 names.
- Slice-level design (design_review (c)): simultaneous LFP and whole-cell in the same slice, several cells per slice, slice nested in animal, against animals as the unit in Phase 0 (CF11 appears only as an id).
- ADV-006 M18: the submaximal NMDAR arm "is not held". L1's comparator asks for it.
- ADV-004's third "may not" (attribution of a slice effect to α2), and `order.md`: "L1 and L2 are not ordered against each other; they are alternatives selected by what Phase 0 shows", combination only as an exploratory occlusion test.

---

## 7. Verdict per R

| R | Proposition (short) | Verdict |
|---|---|---|
| R1 | L1/L2 interpretable only after mIPSC, agonist response, E_GABA (M02, M04, M05) | SUPPORTED (narrower than L1's status cell; "interpretation, not run order" not said) |
| R2 | L2 stays gated by Phase-0 measurements (M17) | PARTLY (quote exact; the three ids are narrower than the quote) |
| R3 | M01 second hop, cost-or-priority; CF01, CF03 to weigh | PARTLY (non-committal; contradicts first-hop statement in the same row; CF22 content absent) |
| R4 | M03 first hop | SUPPORTED |
| R5 | matched comparator for every drug arm; WT and non-Wwox arms | SUPPORTED as quoted; LESS than sources |
| R6 | genuine CF04, CF05a, CF05b, CF23 plus gap/synonym list | PARTLY (types and quotes right; preparation of CF04/CF05a unsaid; consequence and "this order" missing) |
| R7 | CF23 owner note, tension inside SCI47 | SUPPORTED |
| R8 | CF01 not attached; SCI47 inconsistent on configuration | SUPPORTED for L1; NOT SUPPORTED as delivered for L2 (bare id) |
| R9 | CF03 attached to L2 via E5 | PARTLY (E5 row, O10 and burst-status measurement not attached to L2) |
| R10 | attached matrix observations and decisions | SUPPORTED on text; PARTLY on selection (no O03 for L1; `why` and inference tags omitted; "reach the other lever" false for O10; counts printed without O16) |
| R11 | explanation-to-lever rows | SUPPORTED on text; PARTLY on coverage (rows naming the other lever by id not attached) |
| R12 | L3 gate, L4 comparator naming | SUPPORTED |
| R13 | already-used antiseizure drugs paragraph | SUPPORTED |
| R14 | burst reduction not evidence of correction; interaction on defect measure | SUPPORTED |
| R15 | d-APV comparator, O12 | SUPPORTED |
| R16 | dropped levers read from L1/L2 | SUPPORTED (titles in competing_explanations lack "dropped") |
| R17 | M06 as extrasynaptic class and "L1 readout" | SUPPORTED for L2; absent for L1 |
| R18 | prep/age for L1, L2 | PARTLY (L2 inherited without a mark) |
| R19 | ADV-004 pointer | SUPPORTED (nothing beyond ADV-004; third "may not" not printed) |
| R20 | "blind reader had not reported" | PARTLY (stale against the table) |
| R21 | 53 design rows | SUPPORTED by count; file not opened |

L3/L6 controls: both read as dropped. L3 carries a design row for a dropped arm (M20) with the drop unmarked in the join, and a mis-tagged route (M20 does not name O03/O14).

### Plain-words conclusion

AFTER adds real, correctly quoted material to L1 and L2: the gate in the originals' own words, the comparator requirement, the corrected owner note on how to match a reuptake arm, the statement that a burst reduction does not show correction, and the observations that the starting datum was recorded in high chloride without an antagonist. It is careful on the points you asked about. It does not pick a side on any disagreement, it does not turn "cheapest first" into a dependency, it keeps "conditional reading, not an observation" on every order, and it adds no subtype claim beyond ADV-004. I found no id read in the wrong id space in L1 or L2. Its weaknesses are of three kinds. First, it states less than the originals where that matters: the one result-conditioned order (SCI42, CF22) shrinks to a tag, "this order" is left undefined, conflict rows lose their reason and consequence, and the "−67 mV" and O03 caveats do not reach the rows that need them. Second, it moves some context without saying so: the August design's global-allele conflicts are attached to the Synapsin-Cre arm, and L2 inherits L1's preparation and age. Third, it is uneven and sometimes self-contradictory: L1 gets a correct CF01 sentence and L2 does not, M01 is both second hop and first hop, the "same rows reach the other lever" sentence is false for O10, and the E-rows that name the other lever are attached to neither. Against BEFORE alone, the items that change an experiment are R14, the L1 event-identity point in R10, CF03 (R6/R9), the cohort-structure sentence (R6), R7 and R5. Most of the rest is pointer or repetition. The originals' K-gluconate-pipette caveat, the conditions of the −67 mV reference, the pooled-control and animal-count limits, the tonic-current conditions and the P11 age are not in AFTER where L1 and L2 would need them.

---

Model, effort and turns: Sonnet 5.5 (claude-sonnet-5-5), reasoning effort set to 10 (low) by the session, about 28 turns (tool-calling turns plus the final writing). Read-only except this file. No agents started, nothing committed, no receipt recorded.
