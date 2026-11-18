# IT58 — audit of earlier reader tests for unelicited criteria, and a diagnosis of the no-difference comparisons

Non-canonical working note (IT, 2026-11-18). Not medical advice; no dose, schedule or recommendation. Reference genotype class only. Measurement validity, reuse only; no reader was run for this note. The audit's rule (`PREREG_AUDIT_RULE.md`, sha256 prefix `33744d762227`) was written and its hash printed (23:33:34 UTC) before I re-read the IT52 and IT57 preregistrations and tasks.

## Answer first
1. **No earlier verdict changes.** Of the three test families only one criterion was unelicited by its task text and it was already known: K2 of ADV-066 round 1 (the task never asked for an outcome pattern per explanation); no arm met it, so the round-1 verdicts (+1, +2, NO DIFFERENCE) are the same with or without it, and the K2 round already repaired it. IT57: all eight criteria are elicited by "arms, controls and measurements" and "first three actions"; verdict IMPROVED unchanged. IT52: criteria (a) to (d) are mechanical properties of the generator output (no reader involved); (e) rests on a reader dispatch whose text was not kept in the folder or found in the transcripts I searched: **unauditable**, not unelicited (the reader report is organised by proposition and verdict, which shows that support was asked; whether actionability was asked is undocumented).
2. **No rerun, by Rule 3**: no verdict could change.
3. **The diagnosis of the two no-difference comparisons is mostly "the criteria were too easy or too coarse, and the other consumer had already carried the knowledge"**, not "the generator adds nothing": see section 3. The generator does add items that no criterion counted (in vivo tissue readouts for INV-09, per-explanation patterns with margins, the E2 reading for INV-04), and it adds them at a token cost that the K2 mapping did not repay.
4. **A real bifurcation exists, retrospective and cheap** (section 4): the KCC2-above-NKCC1 development statement that was carried in a package cell and then withdrawn by SCI after an independent verifier. It tests whether a counter-evidence carried in the material changes a reader's comparison and whether the old wording transfers a sign. Offered to the advisor as an option next to ADV-067 (lithium regimen); not started.

## 1. Elicitation, per test (Rule 1; task text quoted)

| Test | Criterion | Task sentence that elicits it | Verdict |
|---|---|---|---|
| ADV-066 r1 (`../generation_adv066_20261118/READER_TASK.txt`) | K1 better comparison | "(3) which candidates or classes the material says are more promising, on which endpoint and at what evidence level" | elicited |
| | K2 discriminating prediction | none | **UNELICITED** (repaired in the K2 round by part 6) |
| | K3 corrected premise | "(4) what cannot be concluded from the material" | elicited |
| | K4 withdrawn or avoided duplication | "(3) ... and what it says is withdrawn or unresolved" | elicited |
| | K5 demonstrated limit | "(4) what cannot be concluded" and "(5) the one decision ... without asking someone" | elicited |
| ADV-066 K2 round (`k2_round/READER_TASK_K2.txt`) | K2, PAT | "(6) for each competing explanation ... the outcome pattern, with its numeric margin" | elicited |
| IT57 (`../generation_it57_20261118/READER_TASK.txt`) | C1 to C8 (pilot, not sizing on the published effect, age series, panel, non-floor stimulus, seizure type and motor control, dose check, T-type arm) | "(1) the first three actions" and "(2) the arms, controls and measurements you would include" | elicited |
| | H5 cannot say what it does not show | "(3) what this experiment cannot show" | elicited |
| IT52 (`../generation_it52_20261114/prereg_it52.md`) | (a) to (d) | not a reader criterion: properties of the generator output, checked mechanically | not applicable |
| | (e) reader finds the output actionable | reader dispatch text not preserved in the folder; not found in the transcripts searched | **UNAUDITABLE** |

Caveat that the audit adds for IT57, outside Rule 1: its criteria C1 to C8 are the contents of the clause that was added to the card, so a reader that copies the clause meets all of them. That measures that the stored cell reaches a reader who reads it (which is what the claim says: "changes what a fresh reader would build"), not that a reader would reason to the design unaided. Class 4 below.

## 2. What changes in a verdict (Rule 2)
* ADV-066 round 1: (a) as published INV-04 +1, INV-09 +2; (b) counting only elicited criteria K1, K3, K4, K5: INV-04 BEFORE 3 and AFTER 4 (+1); INV-09 BEFORE 2 and AFTER 4 (+2). **UNCHANGED**; the bound the rule needed was +3.
* IT57: **UNCHANGED**. IT52: **UNCHANGED** where auditable; (e) unauditable, the NO DIFFERENCE of iteration 1 and the IMPROVED of iteration 2 stay as recorded.
* The 'before' baselines: the ADV-066 BEFORE text already held the IT57 next-test wording (the stored investigation rows, landed earlier the same day). The baseline was therefore "the engine with the day's knowledge already in its other consumer", which is what ADV asked for ("current generator output"), and which is why K3 to K5 were met in both arms.

## 3. Diagnosis of the no-difference comparisons (Rule 4; ADV's six classes; from the existing reader reports and views)

| Observed gap or absence of gain | Class | Evidence (reader reports and views, round 1 and K2 round) |
|---|---|---|
| K3, K4, K5 met by BEFORE and AFTER readers in both threads | **4 comparison too easy** (for those criteria) | BEFORE INV-04 text already carries the IT57 clause: "the published effect cannot be used to power it ...", "no T-type current has been measured in any WWOX system"; reader 1 reproduces them |
| INV-09: p-Ser9, total GSK-3beta and a kinase readout in the treated animals, and E_GABA by perforated patch, appear in the AFTER answer (reader 4 round 1; reader 5 K2 round) and not in the BEFORE answers; not in the BEFORE text | **1 new knowledge that changes a decision**, as a measurement added to the experiment; **no criterion counted it** | package new_measurements rows M-1 to M-4 reached the AFTER material; absent from BEFORE view and answer |
| INV-04: E2 (age-limited: wild-type null at the assay age, an effect at an older age) and the T-type route as an explanation appear in AFTER answers, not in BEFORE (K2 round, readers 2 and 3 against 1) | closest to 1 but **does not change an action** (BEFORE already proposes a wild-type age series): interpretive gain only; by Rule 4 not class 1 | AFTER rows E2, E4; BEFORE card names no explanation list |
| INV-09 BEFORE reader (K2 round) states "general if the effect appears in all genotypes; a genotype effect needs a non-GSK-3 comparator" | **2 or already in the BEFORE text**: the BEFORE card already lists the comparator and the second inhibitor; cannot be separated without a no-material condition | reader 4 K2 round; BEFORE card text |
| Per-explanation patterns for the cell-level explanations (INV-09 H1 to H5, regimen artefact L3) stay qualitative; readers say "the material gives no numeric margin" | **5 insufficient to support a new hypothesis** (no data to anchor a margin) | readers 4, 5, 6 K2 round, part 6 |
| K2 mapping: AFTER2 equals AFTER on K2 and on patterns matching the key; AFTER2 adds about 3 KB (INV-04) and 1.9 KB (INV-09) | **6 cost without observable benefit** for the mapping; the same patterns were already in the hypothesis rows | views AFTER and AFTER2, readers 2 and 3, 5 and 6 |
| AFTER material 33 to 40 KB against 300 to 600 word answers | **3 loaded but not used**: NOT ESTABLISHED. No systematic check was made of which of the ten comparison rows each answer reproduces; the answers reproduce four endpoints (round 1 reader 2) and several 'nothing is more promising on ...' statements (K2 round reader 3), so a row can be used as an absence statement; a per-row trace would be needed | readers 2 and 5 (round 1), 3 (K2 round) |
| The 'KCC2 beats NKCC1 on development' sentence repeated by AFTER readers (it counted toward K1 for INV-09 in round 1) | not a gain: a **withdrawn statement carried and repeated** (class 4-adjacent: a reader repeats what the cell says, true or not) | round 1 reader 4 (INV-09 AFTER); K2 round reader 5 (INV-09 AFTER); SCI's withdrawal |

Class 2 cannot be tested on the existing material: it needs a no-material condition (the card question alone, or the question with the task only). That is the one addition the audit names; it costs two short readers per thread, is not a repetition of any earlier comparison, and tells whether "the model already knew it" is the reason the packages' content is not visible in the answers.

## 4. A concrete, informative bifurcation, retrospective (Rule 5)

**Case.** Development endpoint, KCC2 branch against NKCC1 blocker (package cells INV-04 C-EP5 and INV-09 C-GS3). Two versions of the same cell exist with a known truth-direction: the version carried until 23:1x UTC (SCI ADV-065b: "KCC2 branch is more promising than an NKCC1 blocker on development on evidence level only") and the corrected version (SCI ADV-065c, withdrawn after an independent verifier: not rankable; neither has Wwox data; KCC2 side one sponsor-funded Cdkl5 pup dataset; NKCC1 side neonatal studies in other genetic models with durable outcomes and adverse signals). The counter-evidence is a context condition that changes the pharmacological comparison.

**Retrospective** (the outcome is known: the corrected reading is the accepted one); no predictive validity is claimed.

**Conditions** (same model, effort, tools, word allowance, one pass each, blind): OLD cell; CORRECTED cell; (optional, the class-2 test) NO cell, the question and the stored card only.

**What counts, fixed before any reader runs:** better pharmacological comparison = the reader states "not rankable between the branches" and names at least one adverse signal and one durable-outcome study from the NKCC1 side; more useful conditional hypothesis = the reader states what measurement would make development rankable (E_GABA in a WWOX preparation; a KCC2 and NKCC1 readout in the null pup); more discriminating experiment = the experiment named is the E_GABA measurement before either arm; no difference = OLD and CORRECTED readers state the same comparison; harm = the reader ranks KCC2 above NKCC1 on development (an unjustified transfer of sign), or reads 'not rankable' as 'equal', or invents numbers not in the material. Expected under the retrospective frame: OLD readers repeat the ranking; the informative result is whether CORRECTED readers stop doing so and whether NO-cell readers rank at all.

**Relation to ADV-067** (lithium regimen, started by the advisor): that case is a prospective-style bifurcation on a regimen context condition; this one is cheaper and retrospective and tests transmission of a limit, not generation. They answer different questions; the advisor chooses.

## 5. Kept apart
Delivered: the withdrawal reached IT by message, then SCI's note (path named, landing pending). Integrated: package cells C-EP5 and C-GS3, ADV-053 and IT57-Q01 dated lines, F03 counter-evidence item (landed `d69f4de0c88f`). Read by the generator: `conditional_comparison_adv066.tsv` rows C-EP5 and C-GS3 (regenerated). Decision changed: the development row of the comparison no longer ranks the branches; no rank, tier, need or direction moved (digest `ff38fcaa61295a5a`). Residual carriers of the old wording outside IT's files, for their owners: SCI's ADV-065b note (line 8), the advisor's IDEAS_ORDER_DREAM5 and KDS synthesis (both already carry the advisor's dated correction in IDEAS_ORDER and the decision page).
