# HE47 — usable knowledge, preserved meaning, sustainable cost

Harness Engineering (ACTOR_ID plan), mandate record `ledger/tasks/plan/PLAN-HE47-USABLE-KNOWLEDGE-PRESERVED-MEANING-SUSTAINABLE-COST-20261112.json`.
Each section: problem observed, minimal change, consumer, before/after, what is not shown, how to remove.

## 1 · H1 — an explicit intention replaces the textual 'independent route' guard

**Problem.** `comparison_engine.py` (IT46) kept a statement out of a compound's tier when a regex found "independent route", "NRF2-independent" or "independent of NRF2".
It worked for one sentence of one package. Another wording of the same idea, or a statement that only names the compound (identity, a numbers-are-not-transferable remark),
promoted the compound to PRIMARY probe, and the compound read "no proposition in the package names it" when one did.

**Fields already in the packages (checked first).** Reading depth: `depth`. What is measured: `class` and the readout in the conditions cell. Reagent role: derived by the engine.
Support for a proposal: the hypotheses layer. The row-to-proposition link in `comparison.tsv` (`source_locator_depth`) says where a proposition is used, not how it relates to the mechanism:
C-K2 cites D05 and D13 (NRF2-dependence of DMF) together with D14 and D15 (other routes), so the existing fields cannot separate them.
The two missing facts are therefore two optional cells of `decisive.tsv`, written by the package author (contract: docstring of `framework/scripts/hypothesis_package.py`):

| cell | values | meaning |
|---|---|---|
| `relation` | mechanism, other_route, context | how what the proposition measures relates to the mechanism the comparison tests |
| `direction` | supports, opposes, null, mixed, not_applicable | direction of the measured result for the proposal the row serves; `null` is a measured null result |

Blank or no column = `unclassified` (the author said nothing; counts as before). A value outside the vocabulary is `unrecognised:<value>` and fails `check`. Nothing is read from the statement text.
Direction never changes depth or tier. Agreed with the IT46 Orchestrator (default for unclassified: as today) and with Science, who wrote the cells for the 21 propositions of `keap1_nrf2_sci46_20261111` (task/sci47, cf1f39b0, picked here unchanged).

**Engine.** Tier counts propositions whose relation is mechanism or unclassified. `uncounted_props` lists the others with their relation; `counter_props` lists opposes/null/mixed;
`unclassified_props` names counted propositions with no relation. Three additive columns of `compound_decisions_*.tsv`.

**Before/after (INV-08, same package, same engine otherwise).**

| compound | before (regex) | after (cells) |
|---|---|---|
| monomethyl fumarate | NONE, "no proposition in the package names it" | NONE, "named only in propositions that do not measure the mechanism tested (D14 other_route)"; D14 also in `counter_props` |
| KI-696 | PRIMARY probe from D01, D02, D07, D10, D21 | PRIMARY probe from D10; D01, D02, D07, D21 listed as context; comparison_state NOT_COMPARABLE (D07 against D10) becomes SINGLE_OR_NONE because D07 is no longer a mechanism measurement |
| DMF, bardoxolone methyl | ABSTRACT unresolved | unchanged |

Second package, a different mechanism (INV-05 NMDA, INV-07 PDH/PDK): no cell is written there, every proposition reads `unclassified`, tier and role are identical to before (21 tests, `test_decisions_file_is_current`).
A negative probe is pinned by a synthetic case: a `direction=null` proposition keeps PRIMARY probe.

**Not shown.** That Science's classification of the 21 propositions is right (it is theirs); that the cells are written for packages other than INV-08 (older packages stay unclassified, by design);
the `limit of Dxx` rule of the engine is still a text rule, as is the `absence` class handling.

**Remove.** Delete the two columns from a package: it reads as before. To drop the engine part, restore `INDEPENDENT_ROUTE` from commit cff57778 (the regex and its test).

## 2 · H3 — what the comparison keeps of scope and uncertainty

Concrete misleading outputs found on real packages, then fixed at the smallest point:

* **A state read as a verdict on the compound.** `perampanel: NOT_COMPARABLE: D10 and D11 ...` hid that Ro 25-6981 has one agreeing pair against five incompatible ones, and AZD7545 one incompatible pair against five insufficient ones.
  The state text keeps its prefix and names the failing pairs; a bracket now gives the counts ([pairs: 5 incompatible, 0 insufficient, 1 agreeing, of 6]). Roles do not depend on it.
* **`RT-qPCR` read as room temperature.** `\bRT\b` matched an assay name; a HT22 line cell (`hif1a_bnip3_it41_20261109` D08) received an invented 18-26 C and 13 pair reasons said "temperature stated only in b".
  Fixed (`RT` followed by `-`, `/` or a word character is not a temperature). Over 1,108 real pairs: 13 reasons change, 0 states change.
* **A convention shown as a stated value.** Room temperature is supplied by the reader as 18-26 C; the field now carries `convention` and a comparison that rests on it carries `by_convention: true`
  (18 real pairs do). The state keeps its name; the flag says the interval was not the source's.
* **pH wording the reader cannot place** (`pH jump 7.4 to 6.5`) is listed in `unplaced`; before it was dropped without a trace. pHo / pHi / step / difference stay four fields (test).

Not shown: that the pair-count bracket reaches a human reader of the views (the files are regenerated; the view text was not changed). The merge across packages still keeps one package's bracket.

## 3 · H6 — temporaries and CI waits

* `verify_run.py reap` concluded runs by **actor** as well as by session. Two sessions both named `plan` could remove each other's finished clone.
  Reproduced by a test, fixed: `reap` acts on the own session or on `--session <exact id>`; `--actor` only lists other sessions' runs, never touches them.
* `ci_runs.py` polled once a minute for a run that lasts an hour (the whole unauthenticated quota of 60 requests an hour for one waiter). It now polls every 120 s and shares one API answer per commit,
  and one declared rate-limit pause, with every waiter on the machine (a cache under `$TMPDIR`). Run #658 on the closure commit 4e453e1b of HE46 concluded success (read through the tool, twice, one request).

## 4 · H4 — one extractor for the public RNA tables

**Measured duplication.** `kchan_expression.py` (SCI44), `nrf2_expression.py` (SCI46) and `chloride_gaba_expression.py` (IT46) are three copies of the same 50 lines:
the gene list, the output names, one extra human symbol (G6PD) and the docstring are the only differences (diff of each pair: 6 changed lines).

**Change.** `framework/scripts/rna_class_means.py` takes the genes and the prefix as arguments. The three concluded analyses are reproduced **byte for byte** (6 of 6 files: mouse and human for each),
from the same public inputs the originals recorded by hash (read in place, read-only). It adds one file, `<prefix>_extraction_report.tsv`: per requested gene FOUND, DUPLICATE_ROWS or NOT_FOUND ("missing, not zero"),
with the input hash. No threshold or presence call exists in it; the mean is the only number. An empty or non-numeric human cell is left out of its mean and counted (before, it raised an error).
The original scripts stay as the record of what was run.

**What the report shows that the outputs did not.** For the NRF2 list: mouse Hcar2 NOT_FOUND (the table lists the protein as Niacr1, found), human Hcar2, Niacr1 and G6pdx NOT_FOUND under the requested names. SCI46's own README states exactly this deviation (NP4), so the report confirms its handling and makes it
machine-readable.

**Not shown.** Aliases (Hcar2 for Niacr1) are not mapped by the tool: the caller names the symbol the table uses, and the report keeps what was requested. The reproduction test is opt-in (`RNA_REPRO_RAW`, `RNA_REPRO_CSV`, `RNA_REPRO_XLRD`)
because the raw tables are not in the repository.

**Remove.** Delete the script, its test and its README row; the three originals still run.

## 5 · H2 — the boundary of `hypotheses_for` (technical part only)

* No code outside `hypothesis_package.py show` calls `hypotheses_for`: the loader and the manifest are in place, a generator that consumes them is not (that consumption is IT47's). Not demonstrated by a real generator run, and stated as such.
* Qualified identifiers (`package::key`), cell provenance (`source_ref`), empty table vs absent table vs table without a key column (`EMPTY`, `MISSING`, `NO_KEY_COLUMN`) were already explicit.
* Added: a table with **two** id-like columns (`id` and `hyp_id`) was read through the first one silently; it is now the state `AMBIGUOUS_KEY` and no row is returned. No real table is affected (checked on all committed tables).
* GSK3/eIF2B (`gsk3_eif2b_20261107`, 5 hypotheses, pertinent to several investigations): the current format already serves it, one manifest row per investigation with the same folder
  (pinned by a test with a folder listed for two investigations). No code change is needed; which investigations get a row is for their owners.

## 6 · H5 — cost: what the context carries longest

**Measured, not estimated** (`session_model_census.py --carry`, new; a proxy: bytes of a tool result times the assistant turns after it, so not tokens and blind to compaction).
Two long sessions since 2026-11-11T20:00 (this one: 818 turns; SCI46: 353 turns):

| | this session | SCI46 session |
|---|---|---|
| tool results | 427 (690 kB) | 176 (409 kB) |
| results over 3 kB | 72, carrying 63% of carried bytes | 44, carrying 82% |
| tool carrying most | Bash | Bash 64%, Read 29% |
| read in the first 50 turns | 21% of carried bytes | 50% |

**Dominant factor:** a few large results read early (files, logs, listings) are re-read by every later turn. Counterfactual: a 3 kB cap per result would have removed an estimated 29% and 50% of the carried bytes.
That is arithmetic on a transcript, **not a saving**: the capped text was text those turns used, no comparable task was re-run, and a compaction resets what is carried.

**Change.** Measurement (`--carry`, one test) and one doc-only habit row in `framework/scripts/README.md` section 13. No startup file was widened or shortened, no output is capped by any tool, and no report was replaced by a brief.
**CHANGE for the cost itself: none demonstrated.** A correction made while writing this: a first pass of the measurement filtered the wrong time window (the timestamp contained a colon that the loop split on) and gave 3,509 and 3,865 turns; the table above is the corrected run.

**Remove.** Delete the `--carry` option and the README row.

## 7 · H7 — what the DREAM pass found, and where behaviour changes

| Finding | Kind | Where it changes behaviour |
|---|---|---|
| `compound_decisions_inv07_it44.tsv` carried a comparison reason one HE46 reader improvement behind (VER-246608 "system: values overlap ...") | a correction that had not reached its consumer | regenerated in the H1/H3 commit; the freshness test compares roles only, so it could not have noticed (not changed: it is the Orchestrator's test) |
| `hypotheses_for` is called by nothing but `show` | a capability available and not called | H2 section 5; the generator that should call it is IT47's |
| KI-696 was PRIMARY partly through D21, a proposition that opposes the proposal in a transfer system, and through identity statements D01/D02 | an association that changes the next brief | `counter_props` of the KI-696 row names D21 (opposes), `uncounted_props` names D01, D02, D07, D21 (context): a brief written from the row now sees the counter-evidence |
| three copies of one extractor, differing in a gene list | a habit that repeats work | `rna_class_means.py` (H4); the README row says not to copy it again |
| the first cost measurement filtered the wrong window and gave 3,509 and 3,865 turns | a first draft overturned by its own check | corrected table in section 6; the filter bug was a colon inside a timestamp split by a shell loop |

Nothing was written to a new memory, graph or score. The new card view was **not** extended to show `counter_props` (the shareable payload has its own wording rules): the columns reach the files and the Orchestrator's test, not yet the cards. Not shown: that any brief has been rewritten from them.

## 8 · H8 — Claude Science comparison (light)

No dedicated path exists; the Orchestrator's standing practice is "material evaluated whole, with separate provenance" (IT44, IT45 records). Nothing was built. When complete artefacts arrive, reuse what exists:

* **Intake as a package.** A pharmacological claim list becomes a `decisive.tsv` in the existing layout (`depth`, `class`, conditions cell, and the new `relation` / `direction`), registered by one `hypothesis_packages.tsv` row whose `why` names the source system and the snapshot; hypotheses in their own layout use the role `hypotheses_only`. The engine, the reader and the receipts then apply unchanged.
* **Retrieval, inference, proposal, validation** are kept apart by cells that exist: `depth` (what was read), `class` (DATO or inference), `relation` (does it measure the mechanism), `direction`; a proposal is a hypothesis row, never a decisive row; validation means a measurement in a WWOX-relevant preparation, which nothing external supplies.
* **To record per artefact:** snapshot identifier and date, the originals the tool says it read (compare by SHA-256 with the corpus), tools actually used (from its own log, not its prose), code and parameters, and the output files whole. Anything missing is a state ("not supplied"), not a defect of the comparison.
* **The Auto-mode problem** belongs to the external runtime. Nothing here relaxes a permission, adds an allowlist or promises that a prompt removes requests.

Not shown: that any external artefact has been compared; no access to the external session is claimed.
