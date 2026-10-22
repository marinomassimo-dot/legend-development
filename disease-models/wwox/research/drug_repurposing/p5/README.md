# P5 — two comparisons as visible dimensions (RECUPERO_PROFONDO and BENEFICIO_PRECOCE)

Actor `scientist-a`, task `REPURP-10H-P5-A-20261022`, 2026-10-22. Non-canonical research material; **not medical advice**.
No score, rank, probability, blended index, dose, route, schedule or paediatric suitability. Owned by one task; nothing outside
this directory and the note [`../../repurposing_10h_scientist-a_p5_20261022.md`](../../repurposing_10h_scientist-a_p5_20261022.md) was written.

| File | What it is |
|---|---|
| [`p5_comparison.md`](p5_comparison.md) | **Start here.** Rules, the two non-dominated statements pair by pair, origins counted once, convergence, the plain lookup, what changes in the next experiment, stale fields, bridge gaps, the one question |
| [`tables_deep.md`](tables_deep.md) · [`tables_early.md`](tables_early.md) | One block per row (every candidate and every abstention): the card's own field verbatim, or UNKNOWN, with the field path |
| [`matrix.md`](matrix.md) | Where a card cell carries content (V) or is UNKNOWN-led (U); V is not favourable |
| `cells.json` | The cells in machine form (generated) |
| `lookup_summary.json` | The Monarch/DGIdb thin-slice run, with its coverage states; raw packet digest recorded, raw not committed |
| `build_p5.py` · `p5_check.py` | Rebuild the tables from `../cards/` and `../cards_early/`; check every cell is a contiguous piece of its card field, no forbidden key, no dose-like token, tables reproducible |

Regenerate: `python3 build_p5.py`; check: `python3 p5_check.py` (offline). The lookup rerun needs the network:
`python3 .claude/skills/legend-hypothesis-forge/scripts/kg_thin_slice.py WWOX --limit 2000 --raw-dir <scratch> --json`.

Reading limits: the cards were audited once and repaired; the repairs are unaudited. Everything that is not a verbatim cell
(origin counts, comparability, staleness, the reading of the lookup) is a reader's derivation, **OWED a blind audit by someone else**.
