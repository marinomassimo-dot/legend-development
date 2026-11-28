# ADV-321 part B: why non-top compound dossiers stay under Targeted comparison, Assessment available or Deferred (IT33, 2026-11-28)

Hypothesis level; nothing here is medical advice. Producer: one read-only `legend-delegate` (sonnet 5.5, effort high stated, read back), reply as report; spot-checked by IT33 on code lines 12 and 83 to 96 of `framework/scripts/repurposing_compound_analyses.py` and on the zero count of "highest priority|priority follow-up" in `continuous_compounds/README.md` lines 208 to 615. **Not yet blind-reproduced**: the 40-dossier list rests on one reader's lexical rule; HE or a second reader should re-run it before any fix. Counts were measured with `load_cards` and no `public_compounds`; the live build can add "Analysis pending" cards from `generation_it41_20261109/compound_view.tsv` (21 rows), not reproduced here.

## Verdict
**Display-only misrouting, route to HE, no new schema, no new publication requirement.** Every programme card has a decision on its checkpoint line; the projection reads a clinical-disposition word (park/defer pediatric trial priority) plus one narrow phrase, not a research-investment word. A **content gap** also exists and a display fix cannot close it: no machine field gives a compound's research priority (query: `head -12 */README.md | grep -iE "^(priority|research_priority|group|disposition|tier):"` over `continuous_compounds/*/README.md` returned 0 lines); the only research-investment statements are the 4 rows of `cycle_20261123/README.md` and the pathway-level `ranking.json` `investigations[]` (37 compounds). That is the decision note ADV asked SCI for, not something HE should invent.

## Code path (`framework/scripts/repurposing_compound_analyses.py`)
* `programme_cards` lines 56 to 109 route 199 of 203 cards from the bold-led line under "## Current checkpoint" in `continuous_compounds/README.md` (lines 208 to 615): line 83 `lead`, line 84 `disposition = label + " " + lead`, lines 85 to 96 first-match chain: `Active compound:` (86), `RETAINED_COMPARISON` regex (line 12, `retain(ed)? (as|for) ... probe|comparator|comparison`) then comparison (88), `\b(parked|deferred)\b` then deferred (91), `high(est) priority|priority follow-up` then priority (93), `retained|prioritize|targeted comparison` then comparison (95), default unranked ("Assessment available"). Measured: 79 end at line 88, 83 at line 91, 37 at the default; lines 86, 93, 95 fire for none, so **priority is unreachable from this path**.
* `cycle_cards` lines 112 to 130 read `cycle_20261123/README.md` column 2: `startswith("Highest priority ")` gives priority (line 122; Ethosuximide, Perampanel), "Prioritize " comparison (Ganaxolone), "Lower priority " lower (Memantine).
* `load_cards` 182 to 200: a programme card replaces a cycle card for the same slug (184 to 187); a card with only a comparisons-table row defaults to comparison (189; lithium). `render` 209 to 219 orders groups by `GROUPS` (13 to 21), alphabetical inside a group (210).
* **Fragility:** the Ethosuximide and Perampanel checkpoint lines (README 236, 240) link outside `continuous_compounds/`, so no programme card is made for them; if the links resolved, line 184 would replace "priority" with "unranked". The two Priority cards rest on the 23 November register plus a link-path accident.
* One-line fix location: line 84 with the precedence at lines 88 to 91 (the pediatric-trial clause read as the group).

## Counts (`load_cards`, field `group`; total 203 = 199 programme + 3 cycle-only (ethosuximide, perampanel, memantine) + 1 comparisons-table-only (lithium))
| Group | Cards |
|---|---|
| Priority follow-up | 2 |
| Targeted comparison | 80 (79 line 88, plus lithium line 189) |
| Lower-priority follow-up | 1 |
| In progress | 0 |
| Assessment available | 37 |
| Follow-up deferred | 83 |
| Analysis pending | 0 in this run |

**Affected: 40 of 199 programme cards** (lexical rule: the same wording earns a different group elsewhere in the register): 3 in Follow-up deferred whose line retains a research role (bexicaserin "Keep as ... comparator", ivabradine "Retain Ih as a mechanistic probe", l_valine "Retain as a conditional substrate and tracer"); 37 in Assessment available: clemastine ("Completed targeted follow-up ... stays a preclinical comparator", matches nothing) and 36 whose base-form "Park/Defer" is missed by `parked|deferred`. Of the 36: 26 retain a probe/comparison/tool (belong in Targeted comparison; list below) and 10 are park-only (belong in Follow-up deferred: copper_histidinate, gamma_glutamylcysteine, guanosine (names a probe, arguably comparison), l_ornithine, l_theanine, l_tryptophan, n_acetylglucosamine, palmitoyl_oleoyl_phosphatidylserine, pantethine, sodium_phenylbutyrate). "Latest decision" freshness: the checkpoint line is the latest for 198 of 199 slugs (etifoxine has files added 4 minutes later, same day). Wider upper bound (not verified): a retain/keep research role appears in a Decision/Disposition line of 45 of 83 deferred, 30 of 37 unranked, 75 of 79 comparison dossiers, so "Follow-up deferred" mixes "parked, nothing kept" with "pediatric trial parked, probe kept".

Belong in Targeted comparison (26 retain-and-park/defer in Assessment available, plus clemastine): acamprosate_calcium, amiloride, benfotiamine, carglumic_acid, celecoxib, cysteamine_bitartrate, d_cycloserine, dextromethorphan, dimethylglycine, doxecitine, ebselen, es_481, fasudil, guanfacine, mavoglurant, meclizine, melatonin, menaquinone_4, methsuximide, nicotinic_acid, potassium_citrate, pridopidine, riluzole, sodium_selenate, soticlestat, tideglusib; and clemastine. In Follow-up deferred now but retain a research role: bexicaserin, ivabradine, l_valine.

Compounds named in the DisMech brief (sodium dichloroacetate, etifoxine, ganaxolone) already sit in Targeted comparison, in line with their decisions. Minor: lithium has no checkpoint line (group from the line-189 default, empty result text); 6 cards show a truncated fragment because line 83 splits at the first " [" (taurine, squalene, ascorbic_acid, valproate, oxcarbazepine, glycine).

## Roadmap distinction (roadmap_current.md lines 406 to 412, "Two orders, never one")
The group view orders depth of evaluation ("what has been shown"); the investigations view orders **research investment**, the value of the next discriminating test given cost and what its result would change ("what should be funded next"); evidence depth is displayed beside every row and never a gate. Implication: a Priority group should be driven by research investment, not by the pediatric-trial disposition; "retain as comparator" is a third thing, a research role, already in "Research use"; clinical priority stays an independent question (operator brief).

## Owners
HE: re-run the 40-card list blind, then decide the display rule (line 84 and the 88 to 91 precedence; inflection and noun variants). SCI/ADV: the research-priority decision note outside the current top two (no field exists). IT: nothing to edit; do not route this as a schema request.
