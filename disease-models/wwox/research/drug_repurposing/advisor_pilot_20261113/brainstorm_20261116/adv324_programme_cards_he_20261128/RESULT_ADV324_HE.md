# ADV-324: programme-card display groups, blind re-run and fix (HE, 2026-11-28)

Hypothesis level; display only; nothing here is medical advice. This does **not** create a research-priority ordering: no machine
research-priority field exists and none is added. That decision belongs to SCI's note (ADV-322) and ADV.

## 1 Blind re-run
- Input to the reader: only the checkpoint label and lead text of each of the 200 programme lines (`## Current checkpoint` of the
  continuous-compounds register), no group, no code, no IT label. Reader: one `legend-delegate`, sonnet 5.5, effort medium (stated;
  read back from its transcript: claude-sonnet-5-5, medium, 8 turns, 4,625 output tokens). The list of 200 came from the register, not from IT's list of 40.
- Rule given: five neutral classes (active, retained role, parked, priority, prioritise, none) from the words of the line alone.
  Result table: `blind_classes_200.tsv` (slug, class, quote, note). The reader returned only RETAINED (110) and PARKED (90).
- **Limit, said plainly:** the reader took 7 tool calls and 41 s and put every line that begins with Retain or Keep in RETAINED; it is
  a second lexical reader, independent of IT's labels but not an independent judgement of the science. It did not mark any line
  PRIORITY, PRIORITISE or NONE.
- Agreement with IT: the 40 cards are confirmed. IT's 30 in Targeted comparison (26 + clemastine + bexicaserin, ivabradine, l_valine):
  30 of 30 RETAINED. IT's 10 in Deferred: 10 of 10 PARKED. Differences: none. Outside IT's 40: 0 of 160 disagree with the group
  the code gave. One boundary line, not for HE to decide: guanosine ("a conditional clearance probe", no Retain or Keep wording) was
  read PARKED, as IT placed it.
- The mixed lines (retain a role and park or defer the pediatric trial priority) were all read RETAINED, as the code's own comment says
  ("The source may defer a trial and explicitly retain an experiment").

## 2 Cause and fix (`framework/scripts/repurposing_compound_analyses.py`, 8 lines)
The register writes the base forms "Park for pediatric WWOX trial priority" and "Retain a ... probe", "Keep as a ... comparator", "stays a
... comparator"; the code matched only "parked" or "deferred" and only "retain(ed) as or for ... probe, comparator or comparison".
- `RETAINED_COMPARISON` also matches a clause that begins with Retain or Keep, and "stays a ... probe, comparator or comparison". A clause
  start keeps a result sentence such as "8/10 slices retained an abnormal response" out of the rule.
- The park test is now `PARKED_OR_DEFERRED` (park, parked, parking, defer, deferred, deferring).
- The precedence is unchanged: retained role, then parked or deferred, then priority wording, then the default. The priority regex
  is still unreachable from the programme path; that is the cycle register's business and is not changed. No schema, field, file or
  publication requirement is added; the page template is unchanged.
- Test added: `test_programme_group_follows_the_standing_the_line_states_not_the_verb_form` (seven lines). It fails on the old module
  (keepdefer: unranked; resultword: comparison) and passes on the new one.

## 3 Counts, `load_cards` without public compounds, same call before and after
| Group | Before (this checkout) | After |
|---|---|---|
| Priority follow-up | 2 | 2 |
| Targeted comparison | 81 | 111 |
| Lower-priority follow-up | 1 | 1 |
| Assessment available | 37 | 0 (group not drawn: an empty group is skipped) |
| Follow-up deferred | 83 | 90 |
| Total | 204 | 204 |
IT measured 80 in Targeted comparison; the one more in this checkout is a card added after that measurement. Moves: 30 into
Targeted comparison (27 from Assessment available, 3 from Deferred), 10 from Assessment available into Deferred. The programme path
now agrees with the blind table on all 200 lines (110 comparison, 90 deferred).

## 4 What this does not do
- The Priority group still holds only the two cycle-register cards (Ethosuximide, Perampanel) and rests on the link-path accident IT
  named; a programme card cannot reach it. Whether any compound deserves it is the research-priority decision for SCI and ADV.
- Targeted comparison now has 111 cards in alphabetical order inside the group; the order carries no priority.
- "Analysis pending" cards come from the public compound view and were not part of this count.
- `repurposing_view.py package --check` reports the package current: the compound pages are built at publication
  (`package --pages-out`), so no committed page changed.

## 5 Suites run, and one not completed
- Passed: `test_repurposing_compound_analyses.py` (3 tests), `repurposing_view.py package --check` ("package is current"),
  `test_structured_data_integrity.py`, `test_link_targets.py`, `test_section_references.py`, `test_documented_commands.py`, the gate on the exact SHA at push.
- **Not completed:** the README's shareable-view classes (`test_repurposing_view.py DeepenedCasesShareable ShareableAudit It6P13Data
  It21P7InvestigationsContext`) were started and stopped by HE at 342 s with no result, because the host's available memory fell to about
  500 MB (the suite process held 1.3 GB with its browser). Reading the code instead: `repurposing_shareable_audit.py` uses `load_cards`
  only for card names and links (`split_dossier_backlinks`), never `group`, so this change cannot alter what those classes assert.
  If ADV wants the run, it is a request for a quiet host.
