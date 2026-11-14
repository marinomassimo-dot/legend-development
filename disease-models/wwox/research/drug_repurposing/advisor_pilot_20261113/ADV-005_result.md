# ADV-005 result (Harness): the activity tool and its cache

Taken in charge by Harness in `ledger/tasks/plan/PLAN-ADV-SESSION-20261113.json` (block `ADV_ASSIGNMENTS`). Zero spend, no new dependency, service, gate, register or scheduler; no third-party raw added to git.

## Choice, and why this one only

The assignment allowed either the activity-tool item or, instead, the scout-feed defects, not both. **Chosen: the activity-tool item.** It had a concrete consumer (IT52-Q01, a third session would otherwise write a third ad-hoc script) and its cause turned out to be small and checkable. The scout-feed defects (the daily briefing's CONTEXT line reading `roadmap_current` as dated 2026-11-01 and not seeing the Operator roadmap section; one plan surface parsing 0 items; weekly tables stopping at 2026-W40) are **not touched**; they remain open for the presidio to assign or leave.

## What was found

* `generation_it44_20261110/activity_search.py` is not unable to run. Its ChEMBL target file and GtoPdb table sit in `disease-models/wwox/research/drug_repurposing/catalog/cache`, which is gitignored and so exists once per checkout. The primary checkout holds it; a worktree does not.
* Reproduced on 2026-11-14 from a fresh worktree: without configuration the tool ended in a `FileNotFoundError` traceback; with `LEGEND_CATALOG_CACHE` pointing at the primary checkout's cache, one relation (`HDAC6`) returned 9,161 activity rows and 6,596 molecule x relation rows (network read, tool as shipped).
* The tool takes a table of relations with target symbols. It is not a by-molecule query, so IT52-Q01 as worded (by molecule) is not its input; the online by-accession query of ADV-003 (`isr_target_route_adv003_20261113/isr_target_probe.py`) is an example that needs no cache.
* ADV-003's statement that the tool "cannot run in this checkout" was true of its worktree and is corrected here by this note only; the ADV-003 package is not edited.

## What changed (all removable)

1. `activity_search.py`: a missing cached target file now stops with a message naming `LEGEND_CATALOG_CACHE` and the primary checkout (exit 2, "nothing was read") instead of a traceback; one regression test (`test_activity_search.py`, 13 tests OK).
2. `framework/scripts/README.md`: one routing row for this tool saying where it runs, the variable for a worktree, that it takes target symbols and not a molecule, and the example of the cache-free route.

Removal: revert those two edits; nothing else depends on them.

## Open, not done here

The by-molecule route for IT52-Q01 itself (which molecule-to-activity query form to use, and whether a shipped tool, `framework/scripts/target_activity.py`, already covers it) is for that question's executor; it was not tested here.

## Deliver to

Orchestrator (disposition; a note against IT52-Q01 so the next executor knows the route), and ADV (the presidio) for the evidence level.
