---
name: legend-ingest
description: Brings a new LEGEND source through the inbox quarantine — classifies it (deep-dive / queue / filter) and records it in the inbox without skipping quarantine. Use it when a new paper/source arrives that must be assessed before the pipeline.
---

# legend-ingest — Quarantine

Paths are relative to root. Procedure: `framework/protocols/ingest_protocol.md`.

## What it does
0. If the source comes from a study list, or if it has not already been deduplicated, run `legend-study-intake-triage` first. Do not ingest known duplicates or items already in the pipeline.
1. Classify the source: WWOX-relevant? → deep-dive · worth a closer look? → queue · out of scope? → filter.
2. Append to the inbox (append-only, never delete).
3. If "deep-dive" → in manual use, suggest `legend-deepdive`; inside the `legend` autopilot, continue autonomously to `find-fulltext`/`legend-deepdive` where the gates allow.
4. Update the state manifest (`framework/state/state_manifest_current.md`).

## Note
Nothing skips quarantine. Outside the `legend` autopilot, ingest does not start the analysis on its own; inside the autopilot it is an intermediate phase and may continue automatically.
