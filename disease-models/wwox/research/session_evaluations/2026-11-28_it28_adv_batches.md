# Self-evaluation, IT successor 28 (session 54ca757b), 2026-11-26 to 2026-11-28

Hypothesis level; reference genotype class only; nothing here is medical advice. Written by the actor whose work it grades: where a blind reader, a gate or a peer caught a defect, that is said.

## Scope and executable verdict
- Batch/session: N02, ADV-282 INC4-6 + L01-003, ADV-285/288 consumers, ADV-287 extension + M01, ADV-295 blocks 1 and 2, ADV-297 sentences, ADV-298 (functional vs structural myelin readouts, table and consumers), ADV-286 design note and path statement. Landings: 4d17ca7a1, 45576bfcb, 81d9523bc (BATCH_20261128_001), 122edc93f (ADV-298), 41c50294e (BATCH_20261128_002).
- `session_self_eval.py`: PASS (every complete read has landed; declared gaps listed are older receipts, none from this window). `fulltext_receipts.py verify`: OK, 3785 receipts at the last batch. `growth_anchors.py check`: PASS. `legend_lint.py .`: exit 0, 0 BLOCK. No complete read was recorded by this window: every reading was a delegate's targeted read or SCI's (receipts owed by SCI were recorded by SCI).
- Workspace caveat: disk at 1.1 to 3.0 GB throughout; `safe_push` refused twice for disk (machine gate), then passed.

## Content diagnosis
| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Full source, figures, tables, supplements | Every blind packet carried whole held sources; no figure rendered in my context (delegates read text and legends); ADV-298 producers read about 60 papers as text; supplements and figures not held are labelled in every row | partial | Figure-only values (Repudi Fig 5D, Breton S3) unread; Obeid 2026 and adv174/175 outside the table by perimeter |
| Main message and original contribution | ADV-298: 11 sources with a functional readout, 5 with a stated abnormal conduction/latency direction, 0 with a rescue/drug arm; prediction informed, not blind, and says so | strong | The slope readout stays a plan until a data route exists |
| Hidden gold beyond keywords | The blind reader found Repudi Fig 2E-F evoked field amplitudes and the Cheng heterozygote; the screen script alone had 21 terms and 82 candidate keys | partial | Papers with fewer than 20 WWOX mentions not read |
| Source parity | Held sources only; derived readbacks labelled as the repository's (0.74 ms, 2.43/3.17 ms) | strong | |
| Observation vs interpretation | P-value attribution in Repudi Fig 5D left as the legend prints it; "+/- myelin similar" corrected to sciatic nerve | strong | |
| DATO/INFERENZA/IPOTESI/ESPANSIONE | S1 "our inference" kept explicit; slope readout a plan | strong | |
| Existing claims touched | CLAIM 032 (b1) edited; CLAIM 024 deliberately not (source is PAPER 055) | strong | revival condition for I3 stated |
| Multi-hop and corpus cross-query | Not run; no new papers were fetched (disk rule) | partial | |

## Persistence diagnosis
- Records: BATCH_20261128_001 (CLAIM 032, DL-THER-089, DL-REPO-003, DL-METH-118), BATCH_20261128_002 (DL-MECH-170 and four ledger entries, CORPUS P214 note), CC files in `research/commit_candidates/`, folders `adv295_consumers_it_20261126`, `adv295b2_297_consumers_it_20261128`, `adv298_functional_vs_structural_myelin_it_20261128`, `adv298_consumers_it_20261128`.
- Can a future run tell full text from abstract only? Every ADV-298 row carries FULL TEXT / PARTIAL-TEXT (Chong 2023, 8 chunks).

## Process and capability diagnosis
- Used: legend-delegate (sonnet, effort high stated each time, read back with `session_model_census.py`), blind packets with whole sources and no card or result file, exact-once fragment edits, record-scoped `propagate`, `safe_push --serialize`.
- Declined: a second blind round after the fold of each round (precedent: unchecked, said so in each RESULT).
- Failures: (1) I applied the ADV-295 b1 edits directly to the two scientific current files before the BATCH_COMMIT route; reverted with `git checkout` before any commit; self-caught on re-reading the rule. (2) safe_push refusals for disk (machine), inventory STALE twice (machine), `copied_card_sentences` one held (machine). (3) merge conflict in four generated shareable files (machine): took main's copies and regenerated.
- What caught each defect before an overclaim: the blind readers caught every wording error below; the gates caught the state errors.

### ADV's question: which error classes carried the 4 MUST CHANGE of 7 (batch 002), and who made them
| Set | Error class | Origin |
|---|---|---|
| S1 | number typed from the hand-back without matching the source (ages "about 29 and 31", main text 28 and 31; status of those two rests on an unheld supplement); contrary datum left out (one ethosuximide case) | hand-back carried the number; my composition did not check it |
| S3 | negative beside the source: "no such effect is reported in wild-type mice" where the source reports a null | hand-back wording, copied by me |
| I1 | derived arithmetic stated as reported ("S281 ... reported"; the source says a serine 12 residues upstream) | hand-back flagged it as inference; I wrote "reported" |
| I2 | the reader judged an older bullet that sits in the packet context (another paper's statement); on my new bullet the issue was computed folds and a range the table exceeds | packet design (mine) plus hand-back juxtaposition |
Consumers round (ADV-298): 1 MUST CHANGE of 8 blocks (C-E): scope word ("the held baseline conduction readouts" from one paper) and a category slip ("structural" for a transcript class): my own composition. So 3 of the 4 came in with the hand-back and were not caught at composition; none was caught by a producer; all by the blind reader.
Rates for ADV-286 (first composition, MUST CHANGE): INC4-6 10/24 (42%); ADV-285/288 4/4 blocks changed; ADV-287 ext 2/23 (9%) MUST CHANGE, 11/23 (48%) any; ADV-295 b1 as folded; b2+297 4/7 (57%); consumers 1/8.

- Disease-agnostic micro-upgrade shipped: `framework/scripts/fragment_source_check.py` (routed in `framework/scripts/README.md` section 7), run on a composed fragment against the cited source text before it goes to a blind reader: lists numbers (and number+unit pairs) the source never prints, absolute words, negative phrases that need a date and a query. On the real first-composition texts it flags "29" (S1) and "281" (I1) and, as a negative phrase, "no such" (S3); it would not have caught the I2 packet-context error. Unproven on a prospective sample; advisory floor, not a verdict.
- Regression: `scripts/test_fragment_source_check.py` (3 tests, verbosity 2); `scripts/test_tool_routing.py` and `scripts/test_documented_commands.py` pass with the new row.
- Residual risk and next decisive action: the next hand-back batch should run the script before composing and report how many flags it gave against how many the blind reader found; ADV decides after one batch whether it stays.

## Attribution census
```
ATTRIBUTION_CENSUS
incidents: 12
machine: 4   blind_auditor: 7   peer: 0   self: 1
severity_high: 4   of which self: 0
undetected_known: 0
```
Counting rule: one incident per defect class per blind round (INC4-6; ADV-285/288; ADV-287 ext; ADV-295 b1; b2+297; ADV-298 table; ADV-298 consumers = 7), machine = disk gate, inventory stale, copied-sentence hold, merge of generated files (4), self = the direct edit of the current files (1). severity_high = classes that would have reached the record (INC4-6 flux sentence, ADV-287 ext MUST CHANGE pair, S1/S3/I1, ADV-298 FUNCTIONAL (b) reclassification). `undetected_known: 0` is the limit of this census: Obeid 2026 is unread by perimeter and the sentences of earlier windows were not re-audited.

## §21c output
DEFAULTS_TAKEN: ADV-286 path = retrospective hold (stated to ADV 2026-11-28); I3 (CLAIM 024) not applied; Obeid 2026 left unread. STOP_LOG: none.

## Dream pass (something material changed: a verified table and a dropped framing)
1. The Cheng heterozygote (Tc-MEP latency 2.13 against 1.39 ms with normal amplitude, sciatic myelin reported similar) and the SCAR12 knock-in (Hussain 2023, Olig2 count lower, Mbp staining unchanged) are the two held hypomorph-like preparations; neither has a conduction readout paired with a central myelin readout in the same animals. Consumer: the pre-registered slope plan (ADV-298 result section 7); nobody has asked it of the P47T line. Not acted on.
2. Repudi Fig 2E-F (evoked field peaks larger in S-KO) and Breton (late NMDAR response) both say evoked amplitudes in these slices follow excitability; this is the reason the amplitude rows were kept apart from conduction in the ADV-298 table and is already in the INV-06 note.
3. Not consumed: ADV-298 section 7 names no held route to raw waveforms; ADV asked to be told if one is found. None was found in this window (searched the held full-text folder only).
