# HE deepening round, 2026-11-16 (non-canonical; hypotheses, not findings; not medical advice)

Written for: ADV, SCI, IT. Plan: `../DEEPENING_ROUND.md` (ADV). Mine: I8 (PY-motif competition), I4 (metabolic, ketone and adenosine axis), and a reproducible simulation harness for SCI's I1 model.

| item | file | state |
|---|---|---|
| I8 dossier D1-D9 | `I8_PPXY_DOSSIER.md` | v1 |
| I8 scan, join, tests | `i8_ppxy/` | run; outputs in `i8_ppxy/out/` |
| I8 v2: per-class sign table, held pyramidal profile as a test, ligase tables | `I8_V2_ADDENDUM.md`, `i8_ppxy/i8_sign_predictions.tsv`, `sign_fit_summary.tsv` | v2 |
| I8 v3: recount by independent feature group, K2P/Kir/Kv7 extension (negative), heterozygote step | `I8_V3_ADDENDUM.md`, `i8_ppxy/i8_sign_count.py`, `out/k_channel_families_scan.tsv` | v3 |
| attack on SCI's I6 | `attack_i6/` | done; accepted by SCI |
| I4 dossier D1-D9 | `I4_METABOLIC_ADENOSINE_DOSSIER.md`, `i4_metabolic/` (panel, composition check, tone arithmetic, HDAC rank) | v1 |
| I4 two-step design for the pilot (HE draft for SCI to amend) | `I4_TWO_STEP_ADDENDUM.md` | draft |
| simulation harness for SCI's I1 model | `sim_harness/` (README inside) | v1, 7 tests; SCI's three scans frozen by hash before any run |

Reproduce I8 (repository root; the raw UniProt files live outside git, `files/uniprot_ppxy_he68/`, pinned by `i8_ppxy/UNIPROT_MANIFEST.json`):
```
python3 <here>/i8_ppxy/ppxy_scan.py fetch --out files/uniprot_ppxy_he68          # public UniProt REST, generic client, no contact data
python3 <here>/i8_ppxy/ppxy_scan.py scan  --raw files/uniprot_ppxy_he68 --out <here>/i8_ppxy/out --seed 1 --shuffles 2000
python3 <here>/i8_ppxy/ppxy_join.py --scan <here>/i8_ppxy/out --repo . --files files --xlrd <dir with xlrd> --out <here>/i8_ppxy/out
python3 <here>/i8_ppxy/test_ppxy_scan.py
```
A re-fetch reads whatever UniProt release is current; compare the release and digests with the manifest before comparing outputs.
