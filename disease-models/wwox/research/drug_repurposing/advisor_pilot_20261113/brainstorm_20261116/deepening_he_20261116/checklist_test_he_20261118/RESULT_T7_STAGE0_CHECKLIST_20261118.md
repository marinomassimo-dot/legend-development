# Item-by-item checklist step, development stage 0 on T7: result (HE; 2026-11-18; TUNED-ON; non-canonical; not medical advice)

**TUNED-ON DEVELOPMENT STEP, NOT THE TEST ADV AUTHORISED (decision B, 2026-11-18): never scored as that test and never cited as a result of the generative engine's performance.** Written for: ADV, SCI (scores her own forecast, hash `712a48fafff233d42e46dbd489c63be34022ce4063fe1f091eecda913483a2ca`, written 2026-11-18T00:20:40Z before any target; I have not opened her file), then the operator's decision page item 8.
Frozen before the runs: checklist sha256 a4d70b5e272e01d8..., template 7492a446f9b3f81f..., composed T7 prompt bc4ced5de063754922ee8ff975025dc59bf0f1af1231eb599aa159e1f8ef08cd (equal to the family-first T7 prompt except for the added step), addendum `PREREG_ADDENDUM_T7_STAGE0.md` sha256 2c7aa8a4270231d104c0bb0aeeef9d7b61b0b83faa1847a6b469a24a7a643899 (hash sent to ADV and SCI at 00:29Z, before dispatch).

## Answer first
On T7 (GC-C gain of function; the atom is zinc lowering the cyclase) the item-by-item step made the model name zinc as a lowering modulator in **2 of 2 runs (LOOSE)** and carry it into a hypothesis in **1 of 2 (STRICT)**, where the history on this target was 0 of 4 uncued runs and 0 of 2 family-first runs. Preregistered: LOOSE in at least one of two runs 0.30, STRICT 0.20. By the decision rule written in advance this is a **positive on a tuned-on target**: it earns, and only earns, the sourcing of a non-tuned pair later with the list unchanged; it does not show an improvement of anything.
What it shows and what it does not: the model was ASKED about zinc (item 8 of 77), so this is answering by item, not volunteering; the answer was for the adenylyl cyclases, the neighbouring family, with the transfer to the receptor guanylyl cyclase marked as a hypothesis by the model; and the same two runs answered 'yes' for 26 and 29 of 77 items (noise, many indirect receptor-pathway effects), so the cost of the cue is a long table of mostly unusable lines.

## Runs and process
| run | tokens (harness) | tool calls | model and effort read back | output hash |
|---|---|---|---|---|
| CHK1 | 38,030 | none (only the final hand-back) | claude-sonnet-5-5, effort high | OUT_CHK1.txt 123cb936 |
| CHK2 | 41,753 | none (only the final hand-back) | claude-sonnet-5-5, effort high | OUT_CHK2.txt b76f939f |
Total **79,783 tokens** against the cap of 80,000; no usage-limit notice; the two delegates ran in parallel (two at once); no file was opened (path audit from the transcripts). Outputs verbatim in this folder.

## Scoring (terms and rules as registered; scored by me, not blind)
| item | CHK1 | CHK2 |
|---|---|---|
| item 8 (Zn2+) answered | yes, adenylyl cyclases, lowers ("Zn inhibits AC5/6 at micromolar concentrations; Zn-protoporphyrin inhibits sGC") | yes, AC5/6 and other transmembrane adenylyl cyclases, lowers ("in-vitro inhibition; low confidence for GC") |
| zinc in the MODULATORS table | yes, under adenylyl cyclases, lower (and Zn-porphyrin under soluble guanylyl cyclase, lower) | yes, under adenylyl cyclases, lower |
| zinc in STEP C | yes: "Zn/Li/Mg-type metal effects (the last transferred by analogy from AC, IPOTESI)", in the group of entries that lower the enzyme | no |
| zinc in the 15 hypotheses | **H7**: "Divalent cation tone (Zn2+, Mg2+) sets catalytic capacity; raising Zn2+ lowers cGMP", evidence "for GC-C, not known (IPOTESI)", with a discriminating manipulation (epithelial zinc-transporter gain) | none (0 mentions) |
| LOOSE (zinc lowering named as a modulator, any family) | **yes** | **yes** |
| STRICT (also carried as a corrective lever into STEP C or the hypotheses) | **yes** | **no** |
| zinc mentions by section (checklist / modulators / step C / hypotheses) | 3 / 2 / 1 / 8 | 1 / 1 / 0 / 0 |
| checklist items answered 'yes' (of 77) | 29 | 26 |
| items answered 'not known' | 39 | 43 |
Other preregistered numbers: P(item 8 'not known' in both runs) 0.55: observed in neither. P(25 or more 'yes' in a run) 0.60: observed in both (29, 26). Not recorded as a failure but worth saying: the family line named the right neighbours in both runs (adenylyl cyclases, soluble guanylyl cyclase, the kinase-like fold); the three stage-1 cues so far on T7 are enumeration (no zinc in 2 of 2), family-first (no zinc in 2 of 2), item-by-item (zinc in 2 of 2 loosely, 1 of 2 strictly).

## What a positive earns and what it does not
* Earns: the item-by-item step is a candidate stage-1 step. The honest next step is a test on a NON-TUNED pair with the list unchanged; that needs two targets that pass the standing rule's audits, and the sourcing pass of 2026-11-18 found none in about 190 titles (`SOURCING_YIELD_20261118.md`). So the positive does not buy a test by itself; it makes the sourcing worth attempting only if ADV or the operator judge it so.
* Does not earn: any claim that the generator improves; any statement about stage 2; any statement about levers that are drugs or genes (outside the list by design); any rate (one target, two runs, scorer not blind).
* What would change for generation if it were adopted on a later, non-tuned confirmation: stage 1 would carry a 77-line step of about 5,000 output tokens per run, whose yield is a few usable lines among 26 to 29 'yes' answers; the corpus step and stage 2 would see zinc only if it also survives into the hypotheses (1 of 2 runs here).
* Not proved: that this is retrieval of a member "not in view"; the item names the member. The result says the model answers correctly when the member is named as an item; the cue's value for a member that is on no list is untested by construction.

## For the operator's decision page, item 8 (one paragraph, as ADV asked)
The small test that option (b) described, a stage-1 checklist on two fresh targets, cannot be assembled at a sensible cost: a pass over about 190 recent titles found no new target whose lever is one item of a generic list acting on a defective molecule (the earlier pass found one per about 150 records), and I did not lower the audit to fill the number. A development step on the one tuned-on target did what an earlier cue did not (zinc named in 2 of 2 runs loosely, 1 of 2 strictly, against 0 of 6 before) for 79,783 tokens, but zinc was an item of the list, so it shows answering by item, not discovery. The honest recommendation is to drop the full test (about 1.35 million tokens) and to spend nothing further on the engine path until either a pair of non-tuned targets exists or the operator asks for the cue to be tried on the next real question that has a member to find.

## Limits
One target, tuned-on (the list's zinc item exists for the same reason as every other trace metal, but the project knew the answer when it chose this target); two runs; scorer not blind; recalled evidence in the model's own words, unchecked; one model and one delegate type; the model's answer for zinc was about adenylyl cyclases, and the transfer to the receptor guanylyl cyclase is its own hypothesis; token counts are the harness's.

## Update 2026-11-18: SCI's scoring and the forecasts
SCI scored the two runs independently (`deepening_sci_20261116/SCORE_FORECAST_CHECKLIST_TEST_SCI_20261118.md`, commit 4b16d7895, as the file stood when I read it): LOOSE 2 of 2 at 0.09 (-2.41 nats) against a naive -1.10, STRICT 1 of 2 at 0.22; her calibration note: loose per run near 0.8 when the atom is on the list. My own forecast was 0.30 for loose in at least one of two runs; observed 2 of 2, so I was under-confident by about the same direction as hers. Two forecasters, one target, one list: this says the forecasts under-weighted a named item, not that the cue works beyond the item it names. The result above is unchanged.
