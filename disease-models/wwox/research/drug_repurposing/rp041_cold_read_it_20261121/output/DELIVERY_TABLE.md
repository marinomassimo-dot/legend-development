# RP-041 / ADV-141: delivery table (IT, 2026-11-21)

Producer: cold reader, sonnet effort high, given only the two documents (A: pup brief v2 consolidated; B: in vivo brief with dated lines to 9.17). Blind second reader: sonnet effort high, given the two documents and the question text only. Both read back with `session_model_census.py` (see SEARCH_NOTES in the output folder). Nothing here is a scientific judgement; it is whether a laboratory could execute from the text. Same-family limit: both readers are the same model family.

## Answer first
The laboratory can start only with named gaps closed. The blind reader did not rescue any of the 27 questions the producer marked as blocking: 21 PARTLY (part of the answer, or two texts disagree) and 6 NOT ANSWERED; 0 answered. Across all 85 questions: 7 ANSWERED, 60 PARTLY, 18 NOT ANSWERED, 0 unclear. The seven the producer missed are minor (Q24, Q29, Q38, Q47, Q58, Q59, Q72; none blocking).

## The one table: blocking questions by who can close them
| Group | Who | Blocking questions (blind verdict in brackets) | What closing means |
|---|---|---|---|
| (a) Text governance | IT, one package after ADV-142 | Q01 which text governs [PARTLY]; with Q03 and Q04 (not flagged blocking but ranked first by the producer): '9.12' names two texts (A appendix counts its dated correction as 9.12; B has a separate 9.12 of 2026-11-21); B body not rewritten for later dated lines | One clean current text with a history section; old text recoverable; one numbering of dated lines |
| (b) Design numbers | SCI, with a pre-registered rule | Stimulus, route, schedule: Q12 [PARTLY], Q13 [NOT], Q14 [NOT], Q15 [PARTLY]; scale: Q18 [PARTLY]; pilot: Q19 [PARTLY], Q20 [NOT], Q21 [PARTLY], Q22 [PARTLY]; cell list: Q23 [PARTLY]; n and litters: Q31, Q32, Q33, Q34 [all PARTLY]; ages: Q37, Q39 [PARTLY]; line, genotyping, wild-type source: Q42 [PARTLY], Q43 [PARTLY], Q45 [NOT]; welfare: Q61, Q62 [PARTLY]; numeric rules: Q67 [PARTLY] panel valid, Q68 [NOT] floor; priors file: Q06 [PARTLY] | One protocol-level numbers sheet (24 questions); the priors file or its content supplied |
| (c) Operator or laboratory only | operator | Q74 funding, data ownership, authorship [PARTLY]; Q75 whom the laboratory asks [NOT] | A named contact route and terms; no agent contacts anyone |

Blind reader's five added questions (not in the list; for group (b)): lithium salt, vehicle, route and spacing of the three injections; feeding and thermal state at observation; may the laboratory use its own validated scale; are pilot animals reused in the main analysis and who signs off the pilot; does a stop rule end only its stage.

## The 19 'cannot tell' conflicts, split (IT reading of the producer's rows; C24, C33 and C36 re-checked against Document A and B text)
- **The documents themselves resolve, by scope (3):** C24 (death by about 4 weeks is the knockout in general; 'about day 17' is stated as 'in the comparator's panel'); C33 (the S-KO line seizes from P9, a different line from the germline null whose onset is after P12 to about P14); C36 (randomisation within genotype and litter is general; 'litter as a block for the vehicle groups where numbers allow' is the stated specific case, with its reason). These are readable as compatible once the scope is seen; they still need a clause saying so.
- **Arithmetically equivalent but unsaid (1):** C22 (area under stage against time over a 60-minute window versus mean stage over 60 minutes: the same quantity up to a division by 60 if the documents said so; they do not).
- **Different quantities with a stated basis, easily misread (1):** C05 (44 as a simple-effect n at one SD versus an interaction n per cell at SD 0.3; each is stated with its basis, but nothing tells the reader they are different quantities).
- **Real, only the programme can settle (14):** C02, C03, C06 (twice 36 to 109 is 72 to 218, not 180 to 320: an arithmetic gap), C08, C09, C16, C17, C18, C23, C25, C30, C31, C32, C35.
The 20 conflicts the producer marked 'a later or more specific line wins' are not re-examined here.

## Group (a) is mine: next
After ADV-142 lands, one package: a clean current text (A as spine, B's dated lines folded in order, superseded body statements moved to a history section with the old wording kept verbatim), one numbering of dated lines, and the terms the producer listed (75). I do not start closing gaps before ADV decides, as ADV instructed.

## Model and effort (read back with `session_model_census.py`)
Producer: model sonnet, effort high on 23 of 23 turns. Blind second reader: model sonnet, effort high on 7 of 7 turns (it made 8 tool calls for 85 verdicts, so its PARTLY/NOT_ANSWERED verdicts rest on one full read of two documents; a question it called NOT_ANSWERED was not searched twice by different routes). Both were told to open nothing else; the producer reported it did not read `delegation_budget.md` for that reason.
