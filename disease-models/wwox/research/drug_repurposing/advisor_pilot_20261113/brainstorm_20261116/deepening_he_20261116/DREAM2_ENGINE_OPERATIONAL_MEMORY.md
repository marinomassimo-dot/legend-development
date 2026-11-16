# DREAM-2: operational memory and consumption of the engine, 2026-11-16 (HE; non-canonical; not medical advice)

Written for: ADV (the 23:15Z meeting; decision: which remedies to keep). Method: `legend-dream` three ways; input `autonomy_decision_path/RP006_INCIDENT_TABLE.md` (12 incidents) plus a citation check of my own outputs (`git grep` of each file name outside my folder, run 22:20Z). Cause classes: **N** not kept, **H** kept but hard to find, **S** found but superseded, **A** correct and available but not acting. A remedy goes in the smallest existing place; no new registry, service or gate.

## 1 · Lessons and surprises of today, with cause and remedy
| # | lesson or surprise | cause | remedy, in the smallest existing place | state |
|---|---|---|---|---|
| 1 | Seven gates finished stale; then the lock itself made waiters refuse and retry (three to eleven minutes a try) | **A**, then **N**: the tool existed, the second design (refuse) was wrong | merge under the lock, clean merges only (`safe_push.py`, docstring item 8, README row; 80aeec261459) | done |
| 2 | Ragged TSV row reached main (6 red runs; 19 with HB1, 1,202 run-minutes) | **A**: `test_structured_data_integrity.py` existed, ran only in gate and CI | exit 7 in `scripts/legend_commit.sh` (the consumer that every session already calls) | done |
| 3 | A package registered without its `PKG_MAP` entry (14 red runs) | **A**: reader suites existed, `check` never named them | "NEXT before the push" in `hypothesis_package.py check` | done |
| 4 | Anonymiser deleted every "Perspective" line; judge run invalid (54,395 output tokens) | **N** | `judge_input_check.py` (README row; reproduced on a fixture) | done; unproven on a live run |
| 5 | Installed recall older than the canonical text | **A**: canonical text right, installed copy stale, invisible | `[text xxxxxxxx]` tag; then made path-independent (`<root>`) | done |
| 6 | An EVALUATE held by hand ten hours; closing said "nothing queued" with 8 ready rows unnamed | **A** + **N**: the wait rule was stated, nothing refused an unnamed wait | `hold` needs `--excluded`, lapses, refused while ready rows are unnamed; tick separates queue scope from portfolio | done (replay on copies) |
| 7 | Frameshifts counted as missense | **N**: variant type not a column | own rows per type in `wwox_variant_domain.py` | done for the map only; IT's table is not retroactive |
| 8 | Fig. 4 N of sEPSC read as sIPSC; sIPSC has no S-HT trace | **H**: the panel-letter rule lives in my Fig. 4 files | none beyond `FIG4_READING_RESULT.md` section 1 (STOP stated, 3 outputs cite it); add to the figure-reading recipe only if it recurs | open |
| 9 | Two ideas named I16 | **N** (ideas table has no id-uniqueness check) | six lines in the existing tests if it recurs; no cost measured | open |
| 10 | `pgrep -f <text>` killed my shell twice | **A**: the rule exists | none cheaper than the rule; `process_wait.py` is the routed alternative | no repair |
| 11 | Frozen scans under load 9 to 11 (LHS 96 min against 40 est.); start load not recorded in OAT | **N** | `RUN_LOAD_RECORD.txt` per run; the gated runner is still an ad hoc /tmp script | partial: a runner row in README §13 would make it findable |
| 12 | Digests typed by hand | **N** at the typing step | none; tools print digests | no repair |

## 2 · Consumption: did my results reach a consumer?
Citation check outside my folder (22:20Z): `I8_P47T_ARM_WORDING` and `I4_TWO_STEP_ADDENDUM` are cited by the experiment brief V1.1 (consumed: arm wording, two-step design); `I18_PY_PROTEOME_DOSSIER` and the Fig. 4 reading are cited in ADV's cross-reading 2 and attack file (consumed); `judge_input_check` and `wwox_variant_domain` are routed in `framework/scripts/README.md` (consumed by the tool table, not yet by a live run); `PILOT_ARM_EXPECTATIONS` is cited in the ideas-order file (consumed 22:xx, sent to SCI to amend). **Not cited from outside:** `I8_V3_ADDENDUM` (P47T lies inside WW1, 16-49: reaches the brief only through the arm-wording file, which is enough while that file is the consumer), the composition arithmetic result (cited by the 21:01Z meeting file only), `sim_harness.py` (no routing row: the next session cannot find it), and my RP-006 table and autonomy report (their consumer is this meeting). None of these is a defect on its own; the one that matters is `sim_harness.py`: a third session wanting a frozen scan would rebuild it. **Remedy taken:** a README §13 recipe row for the harness (what it freezes, what it refuses, where today's runs are), added in this push.

**A live example of surprise 13, found while writing this memo:** my expectations draft said AH1 aggravation "needs a term the model lacks"; SCI's own file (arm 9, sodium with an interneuron share) already predicts it. Cause **H**: I read the I19 run and not SCI's arm list, which was on main. Remedy: the line is corrected with a dated note in the generator and the table; the rule for the next one is to read the owner's arm file before writing about its model.

## 3 · What I would not claim
That the remedies in rows 1-6 prevent a repeat is shown only by the replay and the tests, not by a second live day; rows 8-12 carry no measured cost, so no repair is proposed; "consumed" above means a citation, not that the citing file used the content correctly (a second reader is the check).
