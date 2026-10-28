# Exploration view (local, regenerable)

`index.html` is one self-contained file (inline CSS and JS, data embedded as JSON, no network, no
server). Open it by double-click. It is generated; do not edit it by hand. Non-canonical research
material: not a ranking of treatments, not a probability of benefit, not medical advice.

```bash
python3 -B framework/scripts/repurposing_coverage.py run     # refresh the module data (offline, ~6 s)
python3 -B framework/scripts/repurposing_view.py run         # write view/index.html (deterministic, reads no clock)
python3 -B framework/scripts/repurposing_view.py check       # exit 1 if the file is stale
python3 -B framework/scripts/test_repurposing_view.py        # offline regressions (browser tests skip if no Chromium)
```

Reads `coverage/` (summary, matrix, priorities), `catalog/` (stats, cache manifest), `needs/needs.json`
and the card files (for relative links). Every displayed count is derived from those files; headline
numbers carry `data-k` / `data-v` attributes that the test compares with the source JSON.

Sections: funnel with explicit units (records, families, pairs, interventions; "evaluated against
WWOX" has its own definition), access categories with the unknown share and scope note, needs panel,
matrix (four levels side by side, never summed), priorities with the seven distinct dispositions and
per-criterion reasons, honest limits, technical details (sources, versions, licences, source states,
digests, regeneration command). Filters: access, need, need evidence scope, observation scope,
Track, recovery goal, disposition, text. Filters can be set through the URL hash, for example
`#f=disp:exploration_candidate&need:NEED-ISR-ATTENUATION`.

Size: about 1.5 MB; matrix and priorities are embedded as a trimmed projection, lists are paginated
(30 per page). A failed, stale, truncated or never-fetched source is shown with its own badge and is
never rendered as an empty or OK result. DGIdb-derived rows are not cleared for public release.
