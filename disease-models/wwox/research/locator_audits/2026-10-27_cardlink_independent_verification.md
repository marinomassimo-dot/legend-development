# Independent verification: roadmap iteration 2, package W1.1 (curated-card linkage), 2026-10-27

Verifier did not produce the package. Scope: `disease-models/wwox/research/drug_repurposing/README.md` section "Roadmap
iteration 2, package W1.1" at main 42fdb489, cards G01, G02, C04, E04, D02 and the join outputs. Tested against the
manifests, the figure images in `files/` (Fig 3 of PMID42422765 `gr3.jpg`, Fig S8 page 10) and the rescue scaffold,
not against the producer's summary. No paper was reacquired; no receipt written. Verdict vocabulary:
SUPPORTED / OVERSHOOT / UNDERSHOOT / NOT_IN_SOURCE / UNVERIFIABLE_SURFACE; each non-SUPPORTED item is marked
ERROR (the file says something the source does not) or UNCERTAINTY (a judgement the source cannot settle).

Tests: `framework/scripts/test_repurposing_join.py` 44 tests OK (47 s). `cards/check_cards.py` 22 packets, 0 problems.

## 1. G01 lithium vs PMID32000863 entries 0, 22, 27, 28: SUPPORTED
- Entry 0 and 22: three stacked panels (+/+, +/-, -/-), each with its own four-star bracket; caption and Results name only
  the null. G01 DR-LI-001/002/003 carry exactly this; DR-LI-002 says "NOT WWOX EVIDENCE of a disease-specific effect".
- Entry 27 (null PTZ-alone N = 6, LiCl N = 7; control differs from Fig 7b control) and entry 28 (wild-type N = 12 vs 8,
  separation confined to first 5-10 min, floor-limited) are reproduced faithfully, including entry 28's own counter-point
  that a floor does not by itself prevent detection. Entry 30 (same dose in all genotypes) ✓.
- Three-genotype claim: one OPPOSES_DISEASE_CHANGE (null), two UNRESOLVED. The two UNRESOLVED are produced mechanically
  by "context.genotype: mismatch", not by a judgement that the drug failed; README says the UNRESOLVED "is the specificity
  failure", which is true of the biology and not of the status. UNCERTAINTY of wording, not an error.
- Ser9 rows (entries 2, 4, 23): densitometry numbers and "heterozygote not intermediate" match entry 23 exactly.
- Trap PMID22193544 entry 5: confirmed (RA differentiation, "phospho-GSK3 S9 remained normal"); G01 states it is a
  WWOX-gain differentiation context, and uses entry 8 (pTau S396 after RNAi) only as a Tau row. Not used as a disease row.
- Minor wording: the card's phrase "failed its specificity test" is stronger than entry 22 ("does not establish");
  UNCERTAINTY, cosmetic.

## 2. G02 memantine: SUPPORTED at field level; OVERSHOOT risk at headline; conflict with F01
- No field reads as a memantine result. Candidate name, identity and DR-MEM-001/002 notes all say d-APV is the tool and
  memantine was never given. Entry 2 of PMID34634460 (d-APV bar absent = 0; washout about 1.85; CBX bracketed, d-APV not
  bracketed) matches DR-MEM-001. Disease rows (0/11, 4/23, 36/42) match entry 0.
- Headline risk (UNCERTAINTY): the derived Q-R-02 card is titled "Memantine" and its directional summary is
  OPPOSES_DISEASE_CHANGE, which is a sign comparison of a competitive full-block tool, and sits in the same record as the
  heading. The caveats are in the rows but the summary line has none. Recommend the join print the tool-compound note beside
  the summary for this record.
- Overlap with scientist-c's `F01_glutamate_receptor_node` (P4-F-01): same candidate (memantine) on the same Breton 2021
  bursting node. Real conflicts:
  1. Evidence scope of the same datum: F01 DA-W2-001 and DA-W2-003 (neuron-specific KO bursting, delayed evoked response)
     are `WWOX_BIOLOGY_OTHER_CONTEXT`; G02 DA-MEM-BURST-001 and DA-MEM-EVOKED-001 are `WWOX_EXPERIMENT_IN_DEE_SYSTEM`.
     F01 gives DEE_SYSTEM only to its d-APV drug row. Two cards, one datum, two labels (see item 6).
  2. F01 carries the memantine adverse datum (DR-W2-004, accelerated seizure stages in wild-type rats) and the GRIN
     gain/loss-of-function human precedent; G02 carries neither. A Q-R-02 that links only G02 shows an OPPOSES summary and
     no adverse row. Directional summaries differ (G02 OPPOSES, F01 UNRESOLVED).
  Recommendation: link F01 to Q-R-02 and merge, or link neither without first harmonising the two scope labels.

## 3. C04 vs scaffold section 2, entries 40, 41, 10 (repaired audits re-judged): mostly SUPPORTED, two defects
Re-judged against the figures, not against the repair notes.
- Entry 40, Fig 3B (`gr3.jpg`): KO+RI extinct by about day 20 (first death about day 9 to 10); LD (n = 20) a staircase to
  zero at about day 77; HD (n = 30) 100 percent to about day 50 then flat at about 76-77 percent; WT+RI about 72 percent
  from about day 120. Caption p = 0.78 (HD vs WT) and LD better than KO+RI (entry 46). DR-AAV-SURV-HD/LD and
  DA-AAV-SURV-001 are SUPPORTED, including the "postponement, not a rescue" wording for LD and the "WT arm itself lost about
  29 percent" caveat.
- Entry 10, Fig S8 (page 10): S8A shows P1, P2, P3, P5 only (no P4; P3 falls to about 67 percent at day 24); S8B shows P1
  at 100 percent and P5 at 75 percent to day 300; S8C/D include a P4 bar. The repaired entry is SUPPORTED. The caption
  states the 2.63e11 vg arm, so "high dose" for the P5 GFAP row is confirmed by the supplement caption, not by entry 9.
- Entry 41, Fig 3C: LD below HD from P15 to P25 (about 9.5 vs 12.5 g at P25), superimposed at P30 (about 15.3 vs 15.6);
  Fig 3D LD series ends at about day 60. The entry withdrew the claim "dose does not grade body weight at any age".
  DEFECT 1 (OVERSHOOT, ERROR): C04 DR-AAV-WT-LD says "equal to the high dose: NOT dose-graded". The scaffold W1 row says the
  same and entry 41 withdrew it for all ages other than P30; the card omits the P15-P25 lag that is visible in the figure.
  The survivor-conditioning caveat is present, which limits the harm. Repair: "equal at P30 only; LD below HD at P15-P25".
- DEFECT 2 (minor, ERROR of locator): DR-AAV-GFAP-P5HD says "Entry 10 carries a repaired adverse audit". Entry 10 describes
  S8A-D (survival, weight, glucose), not the GFAP panel (entry 9). The audit is not about this datum.
- Low-dose and equality rows: LD survival is written as a postponement; weight LD as non-graded (see defect 1); glucose P10 as
  two NO_CHANGE rows (ns vs WT and vs KO+RI, entry 37 ✓); P20 LD about 128 (*), HD about 147 (** vs LD) ✓; P20 and P30 correctly
  carry no untreated arm. GFAP-area (S7H) LD ** worse than WT, HD ns, no KO arm: ✓ entries 8, 44. MBP: only representative
  images, no treated quantification: ✓ entries 6, 43. No row states a dose in vector genomes (searched: none).
- UNCERTAINTY: the motor rows are inherited as "genuinely intermediate" (entry 27) while entry 11 says LD mice did not
  survive to P90 and the panel states no age; a survivor or age effect on that panel is not excluded by any source.
- UNCERTAINTY: the Q-R-01 headline changed from OPPOSES to CONFLICTING. Counted by status it is 8 OPPOSES, 2 NO_EFFECT_REPORTED,
  6 UNRESOLVED (matches the README). The label "CONFLICTING" reflects endpoint heterogeneity, not contradiction between
  studies; a reader may take it for a refutation. Wording only.

## 4. E04 target census (SLC16A1) on Q-R-05: SUPPORTED, with a limit
The census arrives as a pointer only (directory plus symbol list), no hits are printed. DGIdb rows are AZD3965 (MCT1
inhibitor), valproic acid and sodium butyrate (NO_TYPE). The card calls MCT1 blockade a "direction control" for the diet, so it
is not offered as support. Residual risk (UNCERTAINTY): the record is "Ketogenic diet", the census concerns a transporter whose
inhibitor is the opposite lever, and valproate (an antiseizure drug) sits in the same list without an action type. The pointer
cannot mislead by itself; a printed list would need the "target presence is not therapeutic utility" label.
The seizure-side comparison A-KD-1 OPPOSES comes from EB-KD-01 (clinical rows), and A-KD-2 / A-KD-3 are UNRESOLVED; the handoff row
(5 / 3 rows, BENEFICIO_PRECOCE, Track A) matches.

## 5. D02 does not pull lithium in: SUPPORTED, one proximity
D02 has no drug rows (abstention NO_DRUG_ASSERTIONS_SUPPLIED), one disease row (organoid beta-catenin/TCF target transcripts
up; the README is right that a route and one disease row arrive). Lithium is never named. However D02's `missing_datum`
paragraph describes "a GSK3 inhibitor given acutely to Wwox-null mice ... (PMID 32000863)" as a partial exception, and its
candidate name is "Wnt-lowering (tankyrase-type) agents and GSK3 modulation". Not a row and not evidence, so no lithium result
reaches Q-R-03; but a reader of the Q-R-03 abstention is pointed at the lithium experiment. The "GSK3 inhibitor ... wrong direction"
limit is correctly in D02 and is the reason lithium is not linked. Separate point (UNCERTAINTY): D02 attaches
RECUPERO_PROFONDO to a card that only abstains; the route is the card's stated pathway, not evidence of a route.

## 6. Scope label WWOX_EXPERIMENT_IN_DEE_SYSTEM for engineered-null and neuron-specific mouse: UNVERIFIABLE_SURFACE (uncertainty)
`framework/scripts/repurposing_bridge.py` line 42 gives the closed vocabulary only as names; no file in `framework/protocols`
or the join defines the label. The only definitional text is in `lucas_clarke_followup_20261026/regeneration_proof.md`: "a registered
reading documents the reading; it does not say the system read is WWOX-DEE". Usage already in the repository: the join test labels
the AAV9 null-mouse reading as DEE_SYSTEM (`test_repurposing_join.py` line 453); F01 labels the neuron-specific KO slice disease rows
OTHER_CONTEXT but the d-APV drug row on the same slices DEE_SYSTEM; the Teplyshova patient n = 1 is DEE_SYSTEM. So the label has no
settled meaning for an engineered-null or conditional-KO mouse, and two actors disagree. The producer's choice (mouse model of the
disease) is defensible, and each G01/G02/C04 card says "engineered null, NOT the Q230P class" in the context fields, but a reader
who reads the scope column alone sees the same level for a patient case and a conditional mouse knockout. Not an error; a missing
definition. Recommendation: one-line definition in the bridge, then harmonise F01/G02.

## 7. Classification of the 28 rows
Counted: 3 linked in iteration 1 + 6 queries now (N-02, R-04, R-02, R-01, R-03, R-05) + 9 (a) + 6 (b) + 3 (c) + 1 (d) = 28. ✓
- (d) Q-N-06 lactate and blood biomarkers: SUPPORTED. E02/E04 hold lactate observations but their route and candidate are
  interventions; the record is a biomarker; a route would be wrong.
- Table inconsistency (wording, not content): Q-N-13 and Q-R-07 are tabulated as (b)/(c) "at measurement; (a) since", so the true
  count of pertinent-card-exists rows is 11, not 9; the README counts 9.
- Q-N-03 (EB-ETX-01 must not be linked, T-type vs sodium-channel): SUPPORTED. Q-N-04 (EB-VGB-01 covers vigabatrin only): SUPPORTED.

Which (a) rows could be linked next with no wrongness (candidate, endpoint and limits agree; the card is an abstention or an
exact class match):
| Query | Card | Verdict |
|---|---|---|
| Q-R-07 bumetanide | F03 | LINK. Same candidate, abstention, only computational rows; the record's chloride premise is the card's missing datum. |
| Q-N-13 pro-myelinating agents | F02 | LINK. Same agent classes; F02 holds the oligodendrocyte/astrocyte-compartment content that is the N-13 failure mode. F02's separate "activity manipulation" question is not the record's and must not be read into it. |
| Q-N-10 splice-switching ASO | C02 | LINK. Abstention (no aberrant-to-normal ratio) is the record's own limit. |
| Q-N-05 boosting WWOX expression | C03 | LINK. Abstention. |
| Q-N-01 mTOR inhibitors | EB-MTOR-AX-01 | LINK. Abstention on unmeasured mTOR activity, as the record says. |
| Q-N-12 HSP70 co-inducers | A05 | LINK. A05 names arimoclomol; the record is a prediction of harm and the card is an abstention. |
| Q-N-11 4-PBA / TUDCA | A01 | LINK WITH CARE. Candidate matches, but A01 is a RECUPERO_PROFONDO class card with five rows and no scope labels; N-11's statement is "wrong compartment", which should be visible beside the route. |

Should NOT be linked (as it stands):
- Q-N-15 to EB-DEV-AX-01: the record is an inference error about counting seizure control as development protection; the card is an
  axis with no candidate. A route on it would be wrong. Agree with the producer.
- Q-R-09 (umbrella) to A01-A05: linking all five puts three families' not-WWOX rows on one record; linking one makes the record
  look covered. Agree: do not link without a card written for R-09 itself (site-specific chaperone, kinetic stabilizer, indirect
  regulator).
- Q-R-08 base/prime editing to C02: the card names "editing" in its candidate, but its search record covers 'antisense' and
  'oligonucleotide' only. Link only after the card states an editing search bound; until then a link would import an absence claim
  that was not searched for editing. (Higher caution than the producer's "the verifier decides"; UNCERTAINTY.)
- Q-N-04 to EB-VGB-01: half the record (benzodiazepines) is uncovered. Agree.

## 8. Errors found (summary)
1. C04 DR-AAV-WT-LD "NOT dose-graded" is withdrawn by entry 41 for all ages but P30 (OVERSHOOT).
2. C04 DR-AAV-GFAP-P5HD cites an audit note on entry 10 that concerns a different panel (locator).
3. G02 / F01 label the same Breton 2021 disease rows with different evidence scopes; G02 lacks F01's adverse and human-precedent
   memantine rows (conflict, not yet visible because F01 is not linked).
4. README counts nine (a) rows; Q-N-13 and Q-R-07 are (a) as well (eleven).
Everything else tested is SUPPORTED. Not checked: the early-benefit card EB-KD-01's own row readings; the Karnstedt and Alekseeva
records inside F01; figure-pixel values beyond those readable in Fig 3 and Fig S8 at the resolution shown.
