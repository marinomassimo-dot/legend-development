# Question-row candidate CAND-NR03-DYE-01: does a resazurin-type dye track cell number or respiration? (IT, 2026-11-24)

Actor `orchestrator` (IT successor, session 7cf5e85a), task ORCH-ROADMAP-IT59-20261119. Requested by ADV (2026-11-24) as a row candidate for merging with SCI's ADV-222 list. Row in the open-questions-map columns: `CANDIDATE_ROW_NR03_DYE_IT_20261124.tsv`. Hypothesis level; not a claim; not medical advice; no need, card or ranking changes.

## Question
Resazurin-type dyes (alamarBlue, PrestoBlue and the resazurin reagent are one chemistry: reduction by cellular reductases, so the signal scales with viable cell number and reductase activity) are read in the literature as "mitochondrial redox activity". In WWOX work they carry **three signs across five readings**:

| System | Manipulation | Dye signal | Cell-number companion in the same paper |
|---|---|---|---|
| glioblastoma T98G (2014 paper, held, complete read) | gain | up (stated; no number, no panel; authors point to DLD mRNA more than 3-fold up) | apoptosis and invasion not significant; no dye-versus-count control |
| T98G and three other glioma lines (2023 paper, held, partial, figures at caption level) | gain | **down in all four lines** (`PAPER 405`) | proliferation **down** in T98G and U87MG, **up** in DBTRG-05MG (p < 0.0001) |
| bladder CAL-29 (2021 paper, held, complete read) | loss | **up** (significant from 15 min) | BrdU proliferation up with loss |
| bladder CAL-29 (same paper) | gain | **null at every point** | BrdU proliferation **down** (p < 0.0001) |
| human neural progenitors (`PAPER 022`, held) | knockdown | down about 32 percent at 270 min, raw RFU, no n | not stated |

## Why it matters
`NR-03` guards compound scoring against a wrong-direction respiration lever (complex I). A sentence such as "WWOX modulates mitochondrial activity" built on these dye readouts would pool opposite signs from different manipulations and systems. The registry does not pool them today (sweep, ADV-223 section 3); the risk arises when the stubs for the 2014 and 2021 papers become records.

## Competing explanations
(1) Cell number or proliferation (the dye follows viable cells); (2) reductase or diaphorase expression (the 2014 authors' own explanation, DLD); (3) respiration; (4) manipulation level and construct (stable line, transient, knockout versus knockdown); (5) read time, medium and density.

## What the held sources already separate (hypothesis; figures not all read)
* **2021 bladder paper:** with loss, dye and proliferation both rise (consistent with 1, 2 or 3); with gain proliferation falls and the dye does **not** (dye and proliferation diverge on the gain arm: against explanation 1 alone).
* **2023 glioma paper, DBTRG-05MG:** gain raises proliferation while the dye falls (the text says the dye fell in each line): a dissociation of the dye from proliferation, if the proliferation assay is independent of the dye (**not verified**: methods of that paper not re-read here; the figure panels are caption-level in the registry).
* **T98G, two papers:** the 2014 and 2023 readings have opposite signs for gain in the same line named T98G; the 2014 sign has no number to weigh it.

## Discriminating measurement
In one WWOX-deficient neural line (matched isogenic control): dye signal **normalised to cell count at the same time point**, plus oxygen consumption, plus a reductase-transcript check. Outcomes: dye follows cell count and oxygen consumption is unchanged, so no dye readout bears on `NR-03` (viability proxy only); dye departs from cell count and follows oxygen consumption, so `NR-03` gets its first respiration-related datum in a WWOX system; dye departs from both, so a reductase route (explanation 2) becomes the candidate and `NR-03` is untouched.

## The zero-spend half
Read the figure panels of the 2023 glioma paper (its receipt marks figures `captions_only`; the open-data bucket route used for other papers of this series is the route to try first) and tabulate, per line, proliferation direction against dye direction, and the assay used for each. That can confirm or remove the DBTRG-05MG dissociation without any wet lab.

## Limits
Cancer lines are not neural; the neural datum (`PAPER 022`) has no n and no normalisation; the T98G contrast mixes two laboratories' constructs; nothing here is a claim.
