# Comparative decision dossier (ADV-092 template, updated for the operator clarification of 2026-11-19)

Hypothesis level. Reference genotype class only. No dose, schedule or recommendation for any agent in any person. Not medical advice. No personal or individual-level information is used or recorded. Any quote is optional study-planning information, not a prerequisite for scientific selection.

**What the page is for.** Explain why an intervention is preferable to its strongest rival after relevant in-silico analyses, then name the priority experiment and what each outcome would change. Current direction: [Scientific selection before laboratory work](../../../../roadmap_current.md#scientific-selection-before-laboratory-work). The existing view reads study-preparation fields only; neither a complete dossier nor its diagnostic orderings establish candidate superiority. Adapt the template to the question; it is not a release or research gate.

**Length.** Aim for a short decision page with pointers to complete analysis outputs. A field that cannot be filled says `unknown` (never a guess) and field 4 identifies useful remaining work. Unknown is not evidence of no benefit.

**Wording rule.** Every sentence of fields 1 to 3 that states what a source shows follows `framework/protocols/prompt_batch_commit.md` section 4.2.1: the verbatim anchor sentence with its locator or the word `INFERENCE`; a vector, preparation, species or causal verb only if it occurs in the held anchor text; the authors' own limit sentence beside any "so what"; a quantifier carries its unit; a value read from a figure says "by eye".

**Method status of the generative step (dated line, 2026-11-20, added by IT on ADV's instruction; nothing above is changed).** The repository's generative step has been tested prospectively twice on unread full texts, with a blind scorer, a domain-prior baseline and an abstract-only arm: one text and five slots (ADV-106), then three texts and 28 slots (ADV-109), 33 slots in all. The arms converged on most slots and no advantage of the repository materials over the abstract alone was shown (pooled hits of 28: generator 18, abstract-only 17, rule-faithful baseline 17, frozen baseline 15; the pre-registered margin of four was not met and the arms differed on only four slots, so the second test is inconclusive); the generator's unique hits were reached from general knowledge, not from the repository files. The step is therefore **not shown to be predictive, and must not be cited as predictive or forecasting**; its value, if any, is organising (it retrieves and arranges what the repository holds). The facts that decide a pharmacological comparison and that only a paper's body holds (vehicle, sample loss, unreported weights, enantiomer enrichment) were missed by every arm. Records: `prospective_rp005_adv106_20261120/RESULT_RP005_ADV106_IT_20261120.md` and `prospective_rp005_adv109_20261120/RESULT_RP005_ADV109_IT_20261120.md`; portfolio RP-005 parked by ADV with the resume condition stated there.


**Unit of comparability (dated line, 2026-11-21, added by IT on ADV's instruction after ADV-158; nothing above is changed; removable: this one line).** Any sentence that states a margin or an ordering names, first, the unit on which the two sides are comparable: species, age, matrix (total or free) and measurement basis for an exposure; preparation, line, age and unit of the measurement (animal, organoid, cell) for a functional contrast; where the sides are not comparable on that unit, the sentence says so and stops at the per-agent or per-line values with their gaps. Source: ADV-158 result, advisor_pilot_20261113/brainstorm_20261116/it_adv158_20261121/ADV158_TWO_COMPARISONS_AND_CONSUMER_CHECK_IT_20261121.md.
---

## 0. Header
`candidate_id` · `portfolio` (ambitious / conservative) · `cluster` · `dossier_date` · `author` · `package_sources` (paths) · `cost_ranges_item` (row key in `cost_ranges.tsv`, or `not supplied`) · `check_reader` (the person who can say "we would not do anything different"; **the operator for the first cases**, ADV 2026-11-19)

## 1. The question as a chain (one row per link; the weakest link is marked)
| Link | Statement (one sentence) | Evidence class | Source and locator | Weakest? |
|---|---|---|---|---|
| L1 Target engaged (the agent reaches and acts on the target in this tissue and stage) | | held-original measurement / held-original text / secondary / inference / unknown | | |
| L2 Direction (the action moves the readout the intended way) | | | | |
| L3 Phenotype relevance (that readout bears on the seizures or development in the model) | | | | |
| L4 Transfer (to the reference genotype class and to the age that matters) | | | | |
Evidence classes are the repository's, stated per link; `unknown` is a valid value and is printed as such. The weakest link is the one with the lowest class; ties are all marked.

## 2. What we know (three lines at most, each with its limit)

## 2a. Preferred intervention against its strongest rival
Name the intended functional benefit and relevant context, the currently preferred intervention and rival (or why no preference is justified), the analyses actually executed with result pointers, and the before/after consequence for that preference. State the assumptions or counterevidence that could reverse it. Do not substitute literature volume, dossier completeness or a named assay for this comparison.

## 2b. Safety cell: one line per agent and age (its own cell, never merged into the chain or an ordering)
For each agent the study would use and each age that matters: the label limit (minimum age, warnings), the harm signal from held sources, and the source class. `unknown` is printed as unknown. Example of the kind of entry (from held labels, not advice): an agent whose label states safety not established below a given age. A conservative-cluster candidate whose safety cell is unknown or states a limit above the target age is not assumed safe because the cluster is called conservative.

## 3. The decisive uncertainty, and the decision it changes
One sentence: the uncertainty. Then the **outcome-to-decision table** (rows are the possible results; no row may be blank):
| Result | What we conclude (and which link it moves) | The named decision that changes | Next step | Cost range of the next step (operator-supplied or `not supplied`) |
|---|---|---|---|---|
| Positive | | | | |
| Negative, with the control passed | | | | |
| Ambiguous or null, with the control failed | | | | |
**Interpretable-null control (SCI's addition).** Name the engagement or assay-sensitivity control that must pass for a null to count as a negative (for example: the assay detects the effect of a known active agent, or the target is shown reached in this preparation). If no such control exists, a null is `UNRESOLVED` by construction and the dossier says so in this line, because then a null cannot change the decision.
**The "would we do anything different" check.** If no result would change a named decision, the authors and ADV reconsider the question, analysis or experiment autonomously. A second reader can help when useful; an operator reply is not required for ordinary research design. Keep the question open or choose a better one rather than declare a completed template sufficient for selection.

## 4. Analyses capable of changing the comparison (with the perimeter of "tried")
What was executed in silico or in held literature, by which route and over which sources, with its outputs, limits and effect on the candidate comparison. Name useful remaining analyses, or why further available analysis is unlikely to change the choice. A claim of absence states its actual search perimeter under the existing source rules. Availability of another tool or free source does not require an exhaustive sweep; no monetary quote or proof that no cheaper route exists is required.

## 5. What a study of this class can and cannot resolve
State the particular model, intervention and endpoint, which propositions they can test and which stay open after the best outcome. In-vitro or ex-vivo work can test a functional phenotype or a variant-specific response in that model; it does not itself establish clinical efficacy or unrestricted transfer. Price is not a biological limit. The least documented link is not automatically the next useful question, and a functionally informative experiment need not resolve every causal detail.

## 6. Shared assay
Which other candidates or controls the same readout serves (candidate ids), the preparation or measurement named once, and whether sharing changes the design (for example, an extra arm, an extra age).

## 7. Blind-check status
`not checked` / `checked by <role>, <date>, scope: <fields>` / `repairs after the check unaudited`. The locator audit covers fields 1 to 3; the status line says which sentences were checked and which were repaired afterwards.

---

## Consumers (who reads which field)
| Consumer | Reads |
|---|---|
| The study-preparation diagnostic (`FUNDING_VIEW_SPEC_IT_ADV092.md`; legacy command `funding_view.py`) | header, field 1, field 2b (classes and gaps), field 3 (decision named and outcome table), field 6 (assay id), field 7; optional planning costs |
| The cards' "decisive experiment" field | field 3 |
| `research_portfolio.tsv` | header, field 3 |
| ADV's meeting page and the Foundation reader | the whole page |

## Filling checklist (what a reviewer checks first)
1. Four links present, each with a class; `unknown` printed as unknown.
2. Field 3 has three rows and a named control; or the line says the null is `UNRESOLVED` by construction.
3. Field 2a compares a preferred intervention with its strongest rival, or states why no preference is justified; field 3 explains what the experiment changes. An ordinary design question is for the authors and ADV, not a mandatory operator handoff.
3b. Field 2b has a line per agent and age (or `unknown`).
4. Field 4 gives a perimeter, not only "none found".
5. Field 5 says which link stays open after the best outcome.
6. Field 7 is honest about repairs after the check.
