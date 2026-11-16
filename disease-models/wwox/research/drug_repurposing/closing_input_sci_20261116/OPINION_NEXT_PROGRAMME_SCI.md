# What I would change in the next programme's design: SCI opinion for the closing synthesis (2026-11-16)

**OPINION, not a finding.** Written at about 08:45Z from the day's results so far (before IT's scoring detail and the extractor second read). Non-canonical; not medical advice; no recommendation to use any agent.

## What worked (and why I would keep it)
1. **Freeze by hash plus a separate scorer.** It made the matrix's real strength visible and honest: a five-way tie from one origin, a null that is undefined, a 0.09 margin that does not claim. A looser design would have produced a ranking that looked decisive.
2. **Cheap held-data pre-tests as rejecters.** In seconds they rejected the recombination-artefact explanation of the hippocampal silence, downgraded ErbB4 and mTOR, found that the myelin-gene loss is larger where the bursts are NOT, and showed PV loss is not a fixed feature across laboratories. Cost: a script and 20 seconds each.
3. **The origin hunt.** One search told us that every slice-electrophysiology claim rests on one network. That changed what is worth doing more than any further reading would have.
4. **Independent second reads of single-reader landings** (IT of my 25 cells; me of WO-11): small corrections, no change of the top set. A cheap robustness check.
5. **Isolated-worktree pushes.** It was the only reliable way to publish while the shared checkout kept moving.

## What cost without information
1. **Class-level scoring against a table with at most 6 classifiable pairs.** It was declared uninformative in advance, and was; the extraction of 206 rows and the delegates behind it bought a 'not claimed'. Next time compute the projected number of classifiable pairs FIRST and build the extraction only if it reaches 10.
2. **The size of the cell table.** 244 cells, most neutral by rule; the result (five-way tie) is determined by three threads from one origin. Cells beyond those threads added little. Next time build the threads first, count independent origins, and build a matrix only where at least two origins exist for the axis.
3. **Adding columns changes the yardstick.** Empty columns raise 1 - k/N by themselves; I would adopt R2 (count scorable classes only) before any new column exists, not after.
4. **Hypotheses generated after the held-table scan.** H4 and H5 of my leap file were shaped by data that then served as their pre-test. Next time the author logs which tables were seen before writing, and the pre-test is run by someone who did not generate.
5. **Landing races.** About an hour and a half of wall-clock went to refused pushes ('HEAD moved') with up to six sessions gating the same checkout. A landing queue or an agreed isolated-worktree push from the start would have saved it; HE could give `safe_push.py` a mode that gates and pushes an explicit commit list.

## What I would change
* **Experiment first.** The single-origin finding means every computational ranking is conditional on a measurement we do not have. Build the next programme around the pilot (four animals per genotype: variance, within-animal correlation, bursts in both regions) and WO-10; keep computation to pre-registration and held-table lookups until the pilot returns.
* **Declare thresholds, units and the readout before cells exist**, and carry R1 to R3 from the first freeze.
* **Treat 'null undefined' as a design signal:** if all contributing tiers are equal, the matrix cannot score; fix the evidence structure (a second origin) before scoring.
* **Report cost per surviving statement and per decided hypothesis** in the same table as the result, so a step that buys only 'uninformative' is visible when it is chosen.
