context_policy: SYNTHESIS — you are classifying LEGEND's own records against LEGEND's own records; no paper is read, no claim is created, strengthened or weakened.

You are a LEGEND scientist-reviewer (read-only). Repository: /home/desktop/legend-development at commit a923e10. Do NOT edit any repository file. Nothing here is medical advice.

TASK — a live-qualification census of the Working Model's history-shaped text.
`disease-models/wwox/registries/working_model_current.md` (WM) holds, besides its live model, three history-shaped regions: the `**Last update:**` stack (lines 7–22), the `## Changelog` table (lines 250–294), and three `## BATCH_…` sections (lines 295–359). They are about to be moved to a cold history file that scientific routes will NOT load. Before that is allowed, every statement in them that is still SCIENTIFICALLY LIVE must be shown to exist in a place a current reader still sees.

"A place a current reader still sees" means exactly one of:
  (L) the WM's LIVE sections — lines 30–249 (Disease identity, Genotype rules, Mechanistic architecture, BLOCK 1, BLOCK 2 claim mirror, BLOCK 3 flowchart, Monitoring endpoints, Gene therapy context); or
  (C) the claim registry record that the statement qualifies, in `disease-models/wwox/registries/claim_registry_current.md` (every route that loads the WM also loads the claim registry whole).
Nothing else counts (not the discovery ledger, not the therapeutic ledger, not other history rows).

The units are numbered in the JSON file INPUT_UNITS (uid, lines, verbatim text). Classify EVERY unit:
  A  LIVE_ALREADY_REPRESENTED — it contains live content, and EVERY live element of it is present at (L) or (C) with the same strength, scope and conditions.
  B  LIVE_ONLY_IN_HISTORY — at least one live element is absent from (L) and (C), or present only in a weaker/broader/unconditioned form.
  C  PURE_HISTORY — provenance/process only: which batch, who authorised, what was repaired, audit mechanics, counts of candidates, version numbers, superseded states. Knowing it does not change how a Scientist should reason today.
  D  AMBIGUOUS — you cannot decide without new scientific judgement.

"Live" includes: a qualification, limitation, boundary, species/model restriction, evidence downgrade/upgrade, withdrawal (a withdrawn attribution is live: a reader must not re-assert it), contradiction, unresolved uncertainty, caveat on a current claim, current negative, falsifier, dependency, dose/age/context condition, therapeutic ceiling/floor, priority relation. "Old" does not mean "dead": a 2026-08 note can still be live. A statement SUPERSEDED by a later one (e.g. a later batch withdrew it) is not live in its old form — say which later text supersedes it.

For every live element (in A, B or D) give:
  - "element": the verbatim phrase from the unit (short, exact);
  - "concerns": CLAIM id(s) and/or WM live section heading;
  - for A: "represented_at": {"where": "L" or "C", "locator": the WM heading or `CLAIM NNN`, "quote": a VERBATIM quote from that place that carries it};
  - for B: "missing_because": absent | weaker | broader | unconditioned; and "proposed_destination": the WM live section heading (or BLOCK 2 row for CLAIM NNN) where it belongs; and "proposed_text": wording that REUSES the unit's own words, adding nothing, dropping no condition.
Read records with `python3 framework/scripts/registry_records.py get --id "CLAIM 016" --source claim_registry_current` (whole record, with provenance) rather than grepping fragments; grep may FIND, the tool READS. Read WM lines 30–249 whole once.

Be exhaustive and conservative: when an element is present at (L)/(C) only in weaker or less conditioned form, it is B, not A. When unsure between B and C, it is B. When unsure whether it is live at all, it is D.

OUTPUT: write ONLY the file OUTPUT_PATH, JSON:
{"reviewer": "<your label>", "units": [{"uid": "H001", "class": "A|B|C|D", "why": "<one sentence>", "live_elements": [...]}]}
covering all 99 uids, then reply with a 5-line summary (counts per class, and the B uids). Do not write anywhere else.
