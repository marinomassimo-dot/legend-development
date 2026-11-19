# Decision dossier: one page per fundable candidate (template v1, IT, 2026-11-19, ADV-092 item 1)

Hypothesis level. Reference genotype class only. No dose, schedule or recommendation for any agent in any person. Not medical advice. No personal or individual-level information is used or recorded. Costs appear only as ranges the operator supplies (see `cost_ranges.tsv`); an agent never writes a cost.

**What the page is for.** A reader who must choose which costly study to fund needs, per candidate, the one result that would change one named decision, and what is done after each possible result. Funding order is not research order: this page does not rank anything; the ordinal view (`FUNDING_VIEW_SPEC_IT_ADV092.md`) reads its fields.

**Length.** One page. A field that cannot be filled says `unknown` (never a guess) and the dossier says in field 4 what was tried to fill it.

**Wording rule.** Every sentence of fields 1 to 3 that states what a source shows follows `framework/protocols/prompt_batch_commit.md` section 4.2.1: the verbatim anchor sentence with its locator or the word `INFERENCE`; a vector, preparation, species or causal verb only if it occurs in the held anchor text; the authors' own limit sentence beside any "so what"; a quantifier carries its unit; a value read from a figure says "by eye".

---

## 0. Header
`candidate_id` · `portfolio` (ambitious / conservative) · `cluster` · `dossier_date` · `author` · `package_sources` (paths) · `cost_ranges_item` (row key in `cost_ranges.tsv`, or `not supplied`)

## 1. The question as a chain (one row per link; the weakest link is marked)
| Link | Statement (one sentence) | Evidence class | Source and locator | Weakest? |
|---|---|---|---|---|
| L1 Target engaged (the agent reaches and acts on the target in this tissue and stage) | | held-original measurement / held-original text / secondary / inference / unknown | | |
| L2 Direction (the action moves the readout the intended way) | | | | |
| L3 Phenotype relevance (that readout bears on the seizures or development in the model) | | | | |
| L4 Transfer (to the reference genotype class and to the age that matters) | | | | |
Evidence classes are the repository's, stated per link; `unknown` is a valid value and is printed as such. The weakest link is the one with the lowest class; ties are all marked.

## 2. What we know (three lines at most, each with its limit)

## 3. The decisive uncertainty, and the decision it changes
One sentence: the uncertainty. Then the **outcome-to-decision table** (rows are the possible results; no row may be blank):
| Result | What we conclude (and which link it moves) | The named decision that changes | Next step | Cost range of the next step (operator-supplied or `not supplied`) |
|---|---|---|---|---|
| Positive | | | | |
| Negative, with the control passed | | | | |
| Ambiguous or null, with the control failed | | | | |
**Interpretable-null control (SCI's addition).** Name the engagement or assay-sensitivity control that must pass for a null to count as a negative (for example: the assay detects the effect of a known active agent, or the target is shown reached in this preparation). If no such control exists, a null is `UNRESOLVED` by construction and the dossier says so in this line, because then a null cannot change the decision.
**The "would we do anything different" check.** If this field names no decision that any row changes, or the decision is the same in every row, the dossier goes to **a person who can say "we would not do anything different"**: that person is asked one question, "which row would make you act differently?", and the answer is recorded here. A candidate that fails the check is not a fundable study (it may still be a held question).

## 4. Why no cheaper analysis reduces it (with the perimeter of "tried")
What was tried in silico or in held literature, by which route, over which sources (counts), and what it returned. A claim of absence ("no source reports X") is stated with its perimeter and a second route (see the repository's absence-claim rule). If a cheaper route exists and was not tried, it is listed and the dossier is not ready.

## 5. What a study of this class can and cannot resolve
A mid-chain study (cost class of a laboratory measurement) can resolve L1 and L2; it cannot resolve L3 or L4. Say which link(s) the proposed study resolves and which stay open after the best outcome. If the study resolves no weakest link, say that.

## 6. Shared assay
Which other candidates or controls the same readout serves (candidate ids), the preparation or measurement named once, and whether sharing changes the design (for example, an extra arm, an extra age).

## 7. Blind-check status
`not checked` / `checked by <role>, <date>, scope: <fields>` / `repairs after the check unaudited`. The locator audit covers fields 1 to 3; the status line says which sentences were checked and which were repaired afterwards.

---

## Consumers (who reads which field)
| Consumer | Reads |
|---|---|
| The ordinal funding view (`FUNDING_VIEW_SPEC_IT_ADV092.md`) | header, field 1 (classes, weakest link), field 3 (decision named: yes/no; the outcome table), field 6 (assay id), field 7, `cost_ranges_item` |
| The cards' "decisive experiment" field | field 3 |
| `research_portfolio.tsv` | header, field 3 |
| ADV's meeting page and the Foundation reader | the whole page |

## Filling checklist (what a reviewer checks first)
1. Four links present, each with a class; `unknown` printed as unknown.
2. Field 3 has three rows and a named control; or the line says the null is `UNRESOLVED` by construction.
3. Field 3 names a decision, or the "would we do anything different" question is answered.
4. Field 4 gives a perimeter, not only "none found".
5. Field 5 says which link stays open after the best outcome.
6. Field 7 is honest about repairs after the check.
