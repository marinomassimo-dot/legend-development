# Addendum to checkpoint HE-AA (2026-11-28, at ADV's direction)

The checkpoint `CHECKPOINT_HE_20261128_AA.md` (sha256 b3a620d06f6f54aac2384977073bae4df92058a65ebc33d6b2fd7d15bd230d5f) is not
edited; this file adds to its section 2 and section 5.

## FIRST harness item for the successor (goes before every item of section 2)
Make `safe_push`'s disk rule count **overlapping gate clones**. Finding of ADV-299 (`disk_adv299_he_20261128/RESULT_ADV299_HE_20261128.md`): the
2.0 GB free-space rule covers ONE clone (twice the measured 0.86 GB peak); the trace shows a clone beside a derived-surface regeneration,
or two gates overlapping, taking the disk from 3 GB to its floor and back (12 drops of 100 MB or more in 30 minutes). Options named by ADV:
refuse or queue when free space is below the sum of the declared peak of every live `safe_push` gate, or take the disk check inside the lock.
A micro-upgrade with a test; no workflow edit, no gate bypass, no `--no-landing-suites`.

## Operator list, as they stand
The 28 orphan headless Chromium processes (22 older than 66 hours, probably ours from earlier windows; 4 started after the watcher of 2026-11-25
with no watcher alive: amiloride x2, eeg-verify x2) and the launcher outside the repository (no tracked script names the `legend-amiloride-*` and
`eeg-verify.*` prefixes; 10 worktrees still lack `_watch_browser`) go to the operator unchanged. HE killed nothing and is asked to kill nothing without the
operator; the classifier refused ADV a deletion on 2026-11-28.

## Kept line
The PREREG of ADV-299 ranked the Codex writer first and the `/tmp` clones third; the trace showed the order was wrong (the landing gate itself is the writer).

## Second item, queued (SCI message of 2026-11-28, defects in my own `consumer_count.py`)
`DEFECTS_FOR_IT_AND_HE_ADV297_SCI_20261128.md` (on main since 79a736edd, `brainstorm_20261116/adv297_catalogued_triage_sci_20261128/`):
(1) `registry_ids()` takes every line containing "Identifier", so a prose Note in PAPER 055 makes a false consumer for PMID 25662954;
(2) citations by PMCID are not joined (discovery ledger line 29 cites PMC4374002). Candidate repairs are named there, neither applied nor tested.
Repair with a test in `test_consumer_count.py` (the file is tracked; run the 4 existing tests first), after the safe_push disk item above; HE owns the script (ADV-279 defect 2).
