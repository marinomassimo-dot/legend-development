# Adversarial review of BATCH_20261019_027 (CC-20261029-INTEGRATOR-IT6-REGISTRIES-01), 2026-10-29

Reviewer (not the producer). Scope: `git diff 70df75ec..42a54f36` in the worktree `.claude/worktrees/it6-batch`, branch `task/it6-batch`.
Read-only toward the batch; this file is the only addition. Non-canonical. Not medical advice. No registration, contact, spend or
access-control bypass was used.

Method and limit. R1 was done against the eight cycle verifier reports (`2026-10-29_it6_p2` ... `p11_verifier.md`), which quote the source
passages, and against the receipts' own coverage maps in `fulltext_read_receipts.jsonl`. I re-sourced only two decisive abstracts through
PubMed (the Steinberg 2026 organoid paper and the Breton 2021 slice paper): both agree with the registry text (gene therapy "restored
neuronal function ... without disturbing RG populations"; bursts "NMDAR and gap junction dependent", the second half already withdrawn in
the map). The remaining statements rest on the verifiers' quotes; I did not re-open the full texts.

## Tool results

| Check | Result |
|---|---|
| `legend_lint.py .` | WARN, 0 BLOCK (UNLINKED_SUPPORT warnings only, all pre-existing in kind) |
| `growth_anchors.py check` | PASS (claims 47, papers 558, unread_premises 0) |
| `public_release_gate.py` | PASS, 0 BLOCKS (REVIEW lines only, none in a file this batch touched) |
| `fulltext_receipts.py verify` | OK, 912 chained receipts, tail anchored |
| `candidate_ops_reconcile.py` on the candidate | MATCH, ops_parsed 29 |
| `test_repurposing_join.py` | 69 tests OK (includes `SupersededWordingGoneIT6`) |

R4: all 19 distinct `FTR-20261029-*` ids cited in the map, registries and ledgers exist in the ledger. Their coverage maps are thin (most are
question-driven `partial_fulltext_read` or `queried_not_full_read`), and the registry text says so each time. One mismatch of strength, not of
existence, is D3 below.

R3: no Status, Type, Title or Summary line changed. The discovery and hypotheses ledgers and the paper registry have zero removed lines. The
claim registry (CLAIM 040 evidence-boundary line) and the literature log (11 lines) show a removed line only because the same line is
re-emitted with text appended; the earlier wording is byte-identical. The map is not append-only and its in-place edits (M1 cell, R-01 cell,
CHAIN B node line) are permitted.

R5: no bare PMID-looking or e-mail-looking literal in any added registry, ledger or candidate line (the 7-8 digit strings are batch ids and
dates). The two alleles of the reference genotype class do not appear together in any added prose line. The three added lines that contain
both a Q230P string and a c.1057 string are inside the regenerated `view/index*.html` data blobs; the base file already carried the same
pairing (`git show 70df75ec:.../view/index.html` has `1057-2A`), so this is not introduced by the batch (see D13, informational).

## Defect list

### HIGH

None. No overclaim reverses a registry Status, no individual-level or re-identifying content, no receipt missing.

### MEDIUM

**D1. Working model line contradicted by the verified results (R8).**
`disease-models/wwox/registries/working_model_current.md:253`: "critical early postnatal window (P0-P5 in mouse)". CLAIM 011 wave note,
DL-MECH-011 update and map CHAIN A boundary 5 now say P1-P5 is the set of ages tested (main cohorts P0-P1, timing arms P1-P5, no P0 arm, no P4
survival curve, P3 arm 67 percent, P5 arm 75 percent) and that the authors state it is "not a definitive boundary"; the window is not
measured in either direction (`DIS-033`). "Critical" and the exact span assert a measured window. See R8 below for the proposed MINOR candidate.

**D2. Boundary 5 and the discovery-ledger update class motor score as PREVENTED/EARLY-WINDOW while the map already says motor is not rescued.**
`mechanism_intervention_map.md:202` ("survival, growth, glucose, SWD/ECoG ... motor score and gliosis") and `discovery_ledger_current.md:235`
("... spike-wave discharges, motor score and gliosis"). Against `mechanism_intervention_map.md:35` (R-01 SPLIT: "`motor` removed 2026-09-27 ...
`PARTIAL / NOT_NORMALISED`, not rescued") and the P7 verifier (gliosis at the low dose is above wild type, `**`; ns only at the high dose). The
new text lists motor and gliosis next to endpoints that were normalised, which reads as a rescue of both.
Fix: "... survival, growth, glucose, SWD/ECoG, and (partial, not normalised) motor score, and gliosis at the high dose only".

**D3. "inert" overstates a failed activity measurement (R2, R4).**
`mechanism_intervention_map.md:673` ("in ASPA C152W it accumulated inert pellet protein"), `therapeutic_hypotheses_ledger_current.md:343`
("... a negative precedent ... inert pellet protein" in the HYP-20260709-08 update), `literature_tracking_log_current.md:19256` ("insoluble, inert
protein"). Source (P6 verifier row 14): the protein was "insoluble", "not produced in significant amounts" for an assay, earlier studies found no
residual activity; "not measurable" is not "inert". The receipt `FTR-20261029-33914734-02` has abstract read and every other section
`not_read`, so the claim rests on a passage search. Also omitted (P6 D4): the mechanism work is mostly in yeast, the human part in U2OS.
Fix: "accumulated insoluble pellet protein with no measurable activity (yeast and U2OS; earlier reports also found no residual activity)".

**D4. HYP-20261029-01 falsifier is incoherent for the wild-type comparator (R6).**
`therapeutic_hypotheses_ledger_current.md:546`: "lowers burst frequency in knockout slices before it does in wild type". Wild-type slices did not
burst (0 of 11), so there is nothing to lower. The closing clause ("the same in wild-type slices made to burst") is the usable one, but a slice made
to burst by lowering Mg2+ would make the Mg2+ titration trivially positive. Fix: "... lowers burst frequency at a smaller Mg2+ rise in knockout
slices than in wild-type slices made to burst by a route that does not change Mg2+ (for example raised K+ or 4-aminopyridine); a response of the
same size in those slices closes the strand".

**D5. HYP-20261029-01 PRO evidence leaves the favourable half of the arithmetic coincidence (R2).**
`therapeutic_hypotheses_ledger_current.md:548`: "a rise of ... about 30 percent (range 25 to 57 percent) ... resembles the cerebrospinal-fluid
rise ... (+31 percent) ... a coincidence of crude numbers". The P11 verifier (D5, table) shows a cortical-type slope gives about +42 percent, above
what the most penetrant salt achieved in healthy mice, so the honest reading is "the reachable rise falls short", not "resembles". Also not in the
record: no liquid-junction correction in the source (absolute potentials uncorrected; ratio and offset unaffected), and the burst incidence figures
are shared with an earlier paper from the same group (P11 D3, D8).
Fix: replace "that resembles the cerebrospinal-fluid rise ... and is a coincidence of crude numbers, not a prediction" with "a cortical-type
voltage slope gives about +42 percent, above the +31 percent seen in healthy mice, so the reachable rise may fall short; the match is not a
prediction"; add "potentials are uncorrected for the liquid-junction potential" to the limits.

### LOW

**D6. "d-APV, a complete competitive block" (R2).** `mechanism_intervention_map.md:218`, `claim_registry_current.md:448`,
`discovery_ledger_current.md:82`. A competitive antagonist is surmountable; the P9 verifier (section 3.2) notes the high glutamate transient in a
burst can overcome it and that the 50 uM effect had no test on the arm. Fix: "d-APV 50 uM eliminated the bursting (a competitive antagonist; no test
on that arm)". Same word in the "ceiling" logic of HYP-20261029-01 (line 546 "d-APV as the ceiling"): add "if surmountability does not intervene".

**D7. Stale map lines still say "actionable node NMDAR/gap-junction" (R7).** `mechanism_intervention_map.md:1178-1179` ("NMDAR / gap-junction
dependence ... causal dependence was established inside a WWOX model") and `:1221` ("the actionable node is NMDAR/gap-junction ... the one
downstream dependence established inside a WWOX model"). The gap-junction half was withdrawn on 2026-09-27 and the CHAIN B node label was
changed in this batch from "ACTIONABLE NODE" to "NODE ... ACTIVITY IS REQUIRED". Not introduced here, but the batch edited CHAIN B and left
the summary lines contradicting it; `:100` (M2 row, "depends on NMDAR and gap-junction activity") likewise. Fix: "NMDAR (activity required, not shown raised; the gap-junction half withdrawn)".

**D8. "the one organism-level rescue by a domain fragment found in this review" (R2).** `paper_registry_current.md:4574` (CORPUS P318 update).
A negative-existence claim with no search behind the receipt (methods and results read, no figure, no dose). Fix: "the only such rescue noted in the readings
of this batch".

**D9. Radial-glia wording (R2).** `paper_registry_current.md` PAPER 094 update, CLAIM 002 wave note (`claim_registry_current.md`, CLAIM 002),
DL ledger lines: "radial-glia abnormalities NOT corrected". The PubMed abstract says patient-derived organoids showed neuronal impairments "rather
than RG dysfunction" and the gene therapy acted "without disturbing RG populations". Fix: "radial-glia abnormalities (present in the knockout
lines) were not corrected; the patient-line organoids' phenotype was neuronal".

**D10. "Every in-vivo genetic rescue in the corpus" (R2).** `mechanism_intervention_map.md:200`. An absence statement over the whole corpus;
the P7 verifier supports a bounded search only. Fix: "Every in-vivo genetic rescue read in this corpus (two mouse studies; a bounded
search for inducible neural Wwox models found none)".

**D11. F* and "what would close the strand" carry no numbers (R2).** `therapeutic_hypotheses_ledger_current.md:542` (HYP-20261027-01 update)
("an isolated current that is not raised with F* near complete"). P9 D2: thresholds undefined, F* undefined if bursts persist at the NAM plateau.
Fix: "F* is an exploratory readout; its criteria are written before the run".

**D12. Ordering language as implicit ranking (R6).** HYP-20261027-01 update ("A GluN2B-selective NAM is the first drug arm ... memantine the
translation probe afterwards"), DL-BIO-085 / HYP-20260709-08 ("Order of work: the ruler first, then ..."). Hypothesis ledgers state that the
ranking is the Orchestrator's. Fix: "a candidate first arm" / "a proposed order of work, not a ranking". The HYP-20261029-01 tag list also uses
`INFERENZA`, which is not in the ledger legend (`IPOTESI | ESPANSIONE`); and "Lever: 3 (nutrient)" is not a legend value (3 = repurposing).
Fix: "Lever: 3 (repurposing, nutrient class)" and drop `INFERENZA` or say "(the arithmetic is an inference inside the hypothesis)".

**D13. Informational.** Both alleles of the class co-occur in regenerated view blobs, as in the base. `DL-REPO-002` heading still reads
"direzione RISOLTA" (append-only; the update says so, but a consumer reading headings only is misled). The "no WWOX context for any of the 642
non-excluded rows" statement (`discovery_ledger_current.md`, DL-REPO-002 update) is not covered by a verifier row (P10 row 20 checks the
counts, not the absence of WWOX context); label it "by the catalogue's own fields".

## R7: map edits

CHAIN B line (`mechanism_intervention_map.md:218`): accurate and consistent with `:236` (T1 for d-APV only, unchanged), `:479` (R-02 update),
`:458` (R-02 MECHANISM "depends on NMDAR activity") and the withdrawn gap-junction node below it. Contradicted only by the stale summary lines
in D7. CHAIN A boundary 5 (`:200-205`): accurate except D2 and D10; the S8 numbers match the P7 verifier (P3 arm n=3, about 67 percent from about day 24;
P5 arm n=7, 75 percent from about day 35 to day 300; no P0 arm, no P4 survival curve). M1 cell (`:99`) keeps the check mark "restoration -> rescue"
in the "Direction resolved?" column; acceptable because the cell text now carries the qualifier.

## R6: HYP-20261029-01

Format matches HYP-20261027-01 (Track, Route BENEFICIO_PRECOCE, Lever, Tag, falsifiable statement, benefit, PRO, CONTRA, BLOCK-1, translatability,
falsifying experiment, reopening condition, ranking line, status). Status `generated`, no ranking line, no dose, preparation, route or schedule, no
individual advice, safety "unassessed" is correct, and the strongest contra data are present (CSF unchanged after oral sulfate in the mouse,
null seizure control in the add-on infant trial with its intramuscular phase named, no deficiency premise, heterozygote 4 of 23). Defects: D4, D5, D6, D12.
The EU novel-food sentence is correctly hedged and adult-only.

## R8: is the working model contradicted?

Searched `working_model_current.md` for rescue, recover, window, plasticity, AAV9, NMDAR, d-APV, glia, ISR, LDH.

- **Contradicted: line 253**, "critical early postnatal window (P0-P5 in mouse)" (D1). It is the only statement that turns the ages tested into a window.
- **Understated (not contradicted):** lines 103, 148 and 251 say "durable rescue" / "early postnatal window -> durable rescue" in the Wwox-null mouse without
  saying that every endpoint is PREVENTED or EARLY-WINDOW and that no after-onset mouse arm exists; they sit beside "early postnatal" and "post-natal dosing is future work",
  so a reader is warned, but the qualifier in the claim wave notes does not reach the model.
- **Not contradicted:** line 249, "therapeutic window ... still open in early childhood; plasticity at age ~3 is plausible, not guaranteed". It is an
  expert-sentiment sentence outside the mouse evidence, already hedged; the verified results neither support nor contradict it. Its tag could be made explicit
  (`PREMISE: DEFAULT_FROM_TEXTBOOK`/`IPOTESI`), which is not a content change.
- **d-APV node:** the model never says "pharmacologically established"; line 189 (CLAIM 021 row, "NMDAR blockade alone abolishes the burst") is consistent with
  "activity required". No contradiction, no edit needed.
- **Glia, ISR, LDH:** line 109 (neuroinflammation as a low-noise modifier; rescue reduces gliosis) and line 173 (regional glial reactivity in one systemic KO)
  claim no direction across models; no contradiction.

**A MINOR candidate is warranted, small:** (1) line 253 -> "early postnatal window tested (P0-P5 in mouse: ages tested, not a measured boundary)"; (2) lines 103, 148, 251
append "(early-window prevention in the null mouse; no after-onset mouse arm)"; (3) line 249 gets an explicit premise tag. No Status/Type/Summary change, no claim
reversed. The producer's decision to leave the model unchanged in this batch is defensible (research-layer batch, dedicated MINOR is the right vehicle) but it
should be filed as a follow-up candidate, not left as "a reviewer who wants it".

## Verdict

BATCH_20261019_027 is landable after repairing D2, D3, D4, D5 (wording only, in notes and the new hypothesis; no Status/Type/Title/Summary effect). D1 and the
other R8 items go to a separate MINOR candidate. Gates: LINT WARN/0 BLOCK, growth anchors PASS, release gate PASS, receipts OK, ops MATCH 29, join tests 69 OK.
