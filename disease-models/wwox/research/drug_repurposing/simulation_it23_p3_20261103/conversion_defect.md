# NORDic drug-target aggregator: sign conversion defect (minimal reproduction)

Code read: NORDic, GitHub clreda/NORDic, single commit 9db480d (2026-08-07), file `src/NORDic/NORDic_DS/get_drug_targets.py`, function `retrieve_drug_targets`.
Reproduced by running the REAL function on five synthetic cached source tables (no network, no credentials): `defect_repro.py`, log `logs/defect_repro.log`, JSON `results/defect_repro.json`.

## What the code does (line numbers of the cloned file)

| line | code | effect |
|---|---|---|
| 313 (inside `get_targets_TTD`) | `drug_targets["MOA"] = [("-" if (m in decrease_expr_MOA) else "+") for m in drug_targets["MOA"]]` | any TTD mode-of-action string NOT in an 11-word inhibitor list becomes `+` (activation). `?`, `binding`, empty, `modulator`, `binder` all become activation |
| 114-115 | `is_inhibitor = np.vectorize(lambda x : "-" in x)` then `targets_df[is_inhibitor(...)] = "-1"` | the per-source strings are CONCATENATED across sources and the inhibitor test runs first: a cell holding both `+` and `-` (contrasting signs) becomes inhibition |
| 119 | `targets_df[(targets_df!="0")&(targets_df!="-1")&(targets_df!="1")] = "-1"#"1"` | every other non-empty string, i.e. the `*` that MINERVA, DrugBank, LINCS and DrugCentral write to mean "a target, direction not stated", becomes inhibition (the commented `"1"` shows the alternative was considered) |

So the statement given in the brief is right in effect but the route differs: unknown direction from the unsigned databases becomes INHIBITION (line 119) and contrasting signs become INHIBITION (line 114); an unknown or `binding` annotation inside TTD becomes ACTIVATION (line 313). The decrease list also contains `replacement` (replacement therapy read as lowering expression) and `antisense`.

Downstream (`NORDic_DS/functions.py`, `simulate_treatment`, line 330): `mutants = {t: {gx: str(int(targets.loc[gx][t]>0)) ...}}` then `f[i] = fi`: sign +1 clamps the node to 1, sign -1 (and, via the same test, nothing else) clamps it to 0; 0 means no edge. So a wrong sign is a wrong clamp.

## Minimal reproduction (output of `defect_repro.py`)

| row | synthetic input | NORDic output | what it should be |
|---|---|---|---|
| D1/G1 | TTD MOA = `inhibitor` | -1 | -1 (correct control) |
| D2/G2 | TTD MOA = `?` | +1 | unknown, no edge |
| D3/G3 | TTD MOA = `binding` | +1 | unknown, no edge |
| D4/G4 | DrugCentral presence only (`*`) | -1 | unknown, no edge |
| D5/G5 | TTD MOA = `agonist` (`+`) and a second signed source `-` | -1 | conflict, reported, not resolved |

Two caveats stated honestly. (1) The TTD column of the cached table was built by applying the TTD line-313 expression itself (the function would otherwise download TTD files); the aggregator part (lines 107-123) is the unmodified installed function. (2) With the shipped sources TTD is the only one that writes signs, so a `+`/`-` collision needs a second signed source (injected here as a cached DrugBank file, which the function accepts); the code path still resolves it as inhibition.

## What LEGEND does instead (not imported)

NORDic's table is not used. If a pipeline needs a drug-target table, the smallest acceptable input is the long-form `inputs_q5/actions_explicit.tsv`, derived from `generation_it21_p2_20261103/results/actions/family_actions.tsv.gz`, with these rules:

1. A row exists only when the action direction is stated (the catalogue builder already keeps only `stated` and `stable` signs; `mean_sign` must equal exactly +1 or -1).
2. Unknown stays unknown: no row, no edge, no 0 that could be mistaken for "no effect". `?`, `binding`, `modulator`, presence-only annotations are never mapped to a sign.
3. Contrasting signs are never averaged or resolved: a family-target with `mean_sign` not in {-1, +1} (one such value of -0.7143 and one 0.0000 exist among 19,920 rows) is counted as `n_mixed_or_zero_dropped` and left out.
4. The action is attached to a named node LAYER (activity/protein, not transcript), because the sign says what happens to the activity of the target, not to its mRNA.

How it is enforced: `defect_repro.py` runs `explicit_sign()` on the same five rows and gets {D1: -1, D2: none, D3: none, D4: none, D5: CONFLICT}; `build_inputs_q5.py` writes the dropped-row count per target; `sim_q5.py` only builds interventions from the explicit table's targets (nine switches, all inhibitors, EP300 flagged as having one activating family). A regression check to add if this is ever adopted: any converter output must be a subset of the stated-sign rows (set inclusion), with the five rows above as a unit test.
