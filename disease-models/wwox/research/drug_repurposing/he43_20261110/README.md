# HE43 — quantities kept as reported, query errors that do not become biology, attributed names, and the cost of starting (Harness, 2026-11-10)

Non-canonical working note. Not medical advice. No pharmacological conclusion is drawn here: the readings stay with the scientific producer. Task record `ledger/tasks/plan/PLAN-HE43-QUANTITATIVE-PHARMACOLOGY-MEMORY-COST-20261110.json`. Baseline main `a4799320`.

## 1. Units, quantities and conditions (H1) — `framework/scripts/measurement.py`
Defect reproduced on real data (GtoPdb 2026.3.1, 24,968 interaction rows, input sha256 in the output file): the search path reduces a registry row to one string ("6.95 pIC50 (=)"): the original quantity type, the nanomolar column,
the range and the relation are gone, so a unit slip cannot be seen downstream. Two checks, kept apart:
* **inside one row** (`measurement.py scan-gtopdb --tsv`): the log value and the registry's own nanomolar column agree in 13,737 rows and disagree by a factor of exactly 1000 in 7 rows
  (Cs+ on HCN1, HCN2 and HCN4; decavanadate on TRPM4; DkTx on TRPV1; two farnesyl diphosphate synthase rows); five other rows disagree by other factors and are left unexplained (`registry_unit_flags.tsv`, 12 rows).
  Which column is wrong is not decided by the check (the Cs+ pIC50 of 3.7 reads as about 200 micromolar, the nM column says 201).
* **between two measurements** (`compare`): same quantity, target, species, system and stated conditions, or `NO`/`UNKNOWN` with the reason; a ratio within 5% of a power of 1000 is `UNIT_CONFLICT_SUSPECT`. A conversion to nM gives commensurable scale, never the same measurement.
The DQP-1105 case is a fixture and a limit: its registry row has a pIC50 and a nanomolar column that agree with each other, so the in-row check does NOT find it (tested); the second check finds it as soon as the source value (113 micromolar) is a second row.
Missing unit, censored (`<`, `>`), approximate and range values are flagged and kept; absence of a condition is `UNKNOWN`, never a block. 12 tests (`test_measurement.py`).
In the IT41 search table the S2 rows for Cs+ on HCN1 to HCN4 show the pIC50 (the consistent column); three of them (HCN1, HCN2, HCN4) are the flagged registry rows, so a consumer that had read the nM column would have been a factor 1000 off; no rank changes.

## 2. Query errors (H2) — `compound_identity.target_evidence`
The ChEMBL adapter already separates (tests exist): negative answer inside a declared query (NO_MATCH_FOUND, "never absence"), failed call (QUERY_ERROR), paginated answer (COMPLETE / TRUNCATED / PARTIAL_ERROR / NOT_READ), conflicting labels (declaration rows), and an absent tool (`NOT_READ`). The consumer collapsed three of them. Reproduced with canned answers, then fixed:
| Case | Before | Now |
|---|---|---|
| activity answer TRUNCATED, PARTIAL_ERROR or with target genes missing, nothing found for the gene | `EMPTY_RESULT` | `READ_INCOMPLETE` (coverage and rows read named) |
| declared ChEMBL id absent from the release (stale, merged or mistyped), activity read COMPLETE with 0 rows | `EMPTY_RESULT` | `ID_NOT_RESOLVED` (the adapter now sets `identity_basis: declared_chembl_id_not_found`) |
| an answer with no defined status (empty dict, "TIMEOUT") | `EMPTY_RESULT` | `READ_ERROR` |
Namespace collision: all 44,211 catalogue ids carry `CAT:`, are unique, and the search layer prefixes GtoPdb ligand ids: no collision found, no code. No new universal state beyond the two above; no consumer parses the levels with a closed vocabulary (checked by grep), so they pass through.
Declared absence needs source, version, query and completion: the adapter output carries `request`, `source_version`, `requests_sent`, `retrieved_at` and `coverage`; a positive control on the same path is not a substitute.

## 3. Reproducible inputs and identity (H3)
Reusing HE42 on a new input (the IT43 DGIdb names, 330) found two defects in `join_names`, both fixed with tests: a stereo descriptor ("(+)-MK-801", "(+/-)-X", "(S)-(+)-X") was split on its `+` or `/`, and a parenthesis inside a chemical name was deleted ("N-(2,4-dimethyl)glycine" became "N-glycine", falsifying the part text); no wrong identity was assigned
(the results were PROPOSED_ONLY or NO_CANDIDATE), but true links were lost. Split now only outside parentheses; a comment is a trailing parenthesis only.
`compound_identity.parent_form(name)` gives (key, stereo/isotope prefix, salt) for consumers that must group molecules: salts merge, stereo stays apart. On the IT43 names the dgidb_listing key merges `(R)-Ef-1520` with `(S)-Ef-1520` (1 pair of 330 names) and `parent_form` keeps them apart; it also showed that `(Rs)-(Tetrazol-5-Yl)Glycine` must not collapse into `Glycine` (tested).
`action_search.py` clean-clone behaviour is unchanged from HE42 (pinned cache, exit 3, sorted order).

## 4. Cost of starting (H4), measured with agents
Three questions answerable from the repository (label conflict of one compound; the DQP-1105 source values and the wrong registry rows; which commits the passing battery did not cover), Sonnet at low effort, one fresh delegate per cell, tokens and time from the task usage report.
| Question | Start | Tokens | Tool calls | Time | Answer |
|---|---|---:|---:|---:|---|
| Q1 label conflict | checkpoint + originals | 24,649 | 4 | 14.0 s | correct, complete |
| Q1 | targeted reader | 21,146 | 2 | 11.1 s | correct, complete |
| Q1 | reads three READMEs first (simulation) | 30,284 | 4 | 9.4 s | incomplete (identifiers and file missing) |
| Q2 DQP-1105 values | checkpoint + originals | 22,075 | 2 | 4.7 s | correct, complete |
| Q2 | targeted reader | 20,880 | 2 | 5.6 s | correct, complete |
| Q2 | reads three READMEs first (simulation) | 29,979 | 4 | 8.3 s | incomplete (values missing, factor inferred) |
| Q3 commits not covered | checkpoint + originals | 20,290 | 2 | 5.8 s | both commits named, one not verified |
| Q3 | targeted (`git log --stat`) | 19,329 | 2 | 5.8 s | correct, complete |
Reading: the floor of a fresh delegate is about 19 thousand tokens; a targeted start saves 5-15% against checkpoint-plus-originals, and reading unrelated originals first adds about 9 thousand (+40%) and was incomplete in both questions tried (the answer lived in an original it was not pointed to).
Limits: one run per cell, one model and effort, no variance; the third start is a simulation of carrying context, not a session; Q3 was not run in that start; this does not measure the coordinator's long-context cost found in HE42 (65% of cache read), because every delegate starts small: it shows that
starting small from a checkpoint with pointers to the originals loses no correctness on these questions. No conversion to plan share or money.

## 5. Compound names on the shareable page (H5)
Why they were withheld: ChEMBL (CC BY-SA 3.0) and GtoPdb (ODbL / CC BY-SA 4.0) are share-alike and the repository's rule allows a name only where an independent class-A source states it; none of the compound_view entries had one (HE42).
Option chosen, the smallest that can be verified: **Wikidata item labels, joined only through the ChEMBL id (property P592)**. Terms read 2026-11-10 (wikidata.org/wiki/Wikidata:Licensing, revision 2548950862): "All structured data (i.e. the main, Property, Lexeme, and EntitySchema namespaces) is released into the public domain"; the page does not mention labels by name and says additional terms may apply, and it cannot say where one label's wording came from. That is the specific uncertainty kept; it is not a legal clearance, and the code licence does not extend to data.
Not chosen: a class-B file alone does not put names on the page (it carries the record in a separate file; kept as it was); links to the source remain the fallback for every compound without a name.
Result on the real build (`name_source_wikidata.py`, `view/name_source_wikidata.tsv`, 14 ChEMBL ids): 12 labels, 2 without a Wikidata item (onfasprodil, NP10679). A label is shown only when it is the identity table's bare name: four labels were withheld by that guard (GYKI-2466 for GYKI 52466, a code name for GYKI 53655, a systematic name for Ro 25-6981, CERC-301 for rislenemdaz) and one salt form (EVT-101 dihydrochloride) which the audit also refused. Shown: ifenprodil, NBQX, perampanel, ivabradine, radiprodil, traxoprodil, carbenoxolone, on 6 of the 12 entries; the other 6 entries (d-APV, onfasprodil, NP10679, DQP-1105, and two entries with no identity row) carry no name.
Provenance: each name carries its Wikidata item number in the page, the footer and `NOTICE.md` credit the source, `shareable_sources.json` lists it as a class-A name source. Static audit and the dynamic audit of the package: PASS, 0 violations (the audit first refused the salt form and an unlisted host, which were corrected). Published history untouched.

## 6. For IT43 — what to consume, how, and how to remove it
* `measurement.measure/compare/from_gtopdb`: in `action_search.py`, replace the affinity string by `from_gtopdb(row)` and keep `internal.state` in a column; `registry_unit_flags.tsv` lists the 12 rows now. Effect to expect: the Cs+ rows of S2 for HCN1, HCN2 and HCN4 flagged, no rank changed. Cost: about 10 lines in your file; I did not edit it (you hold uncommitted changes there).
* `compound_identity.parent_form`: replace the `key()` in `dgidb_listing.py` (it removes stereo tokens `r`/`s`); one pair in your data changes.
* `READ_INCOMPLETE` and `ID_NOT_RESOLVED` appear in the `evidence_level` column of the identity join: render them as non-evidence states with the others.
* Names: to name a compound on the page add its ChEMBL id to the call of `name_source_wikidata.py` and rerun `repurposing_view.py run --source shareable` then `package`; the audit decides.
* Removal: delete `name_source_wikidata.tsv` (the page returns to withholding names, the audit follows); the other changes are independent functions with their own tests.
Limits: the quantitative component does not read a paper; it cannot say which of two disagreeing values is right. The biology stays with SCI43.

## 7. DREAM (H6): what was connected, what it changed, what was not consumed
Material: SCI42 S5 (the DQP-1105 unit slip), HE42 identity work, the IT43 DGIdb listing, and the HE43 results above. Strength of evidence, relevance to a decision and priority are kept apart; recency and frequency are not used as validity.
| Connection | Separated information | Proposed association | Control | Consumer | Observable change | State |
|---|---|---|---|---|---|---|
| Unit slip class | one source-verified slip (DQP-1105, two rows) | the same class sits in other registry rows the generator reads | in-row check does NOT find DQP-1105 (negative control, tested); it finds 7 rows at exactly 1000 on 24,968 (13,737 agree) | IT43 `action_search.py` affinity column; the Ih tool arm (V04, S2) | Cs+ on HCN1, HCN2, HCN4: the nM column is 1000 off its own pIC50; the page and ranks show the pIC50 (consistent), so nothing is corrected, a flag becomes possible | delivered to IT43, not yet consumed |
| Name joins on a new input | `join_names` (HE42) and the IT43 DGIdb names | the new input exposes cases HE42 fixtures did not | 330 names: old key merged one enantiomer pair; two splitter defects on chemical names reproduced and fixed | `dgidb_listing.py` (IT43), `consume_reader.py` (already calls `join_names`, verified by grep) | one pair separated; true stereo links no longer lost | component corrected; IT43 swap delivered |
| Attributed names | HE42 shareable basis (no class-A name) | a class-A source exists for part of the list | Wikidata P592 join, label guard (5 labels withheld), static and dynamic audit PASS | the public page (6 of 12 entries now carry a name, 7 names) | names with item number and credit; two ids without an item stay unnamed | consumed on this branch |
Stale conditions presented as current: none found. The IT41 comparison note carries its update line for DQP-1105 (checked), and the compound list text already states the resolved value; the verifier's historical file keeps its dated text.
Not examined (inputs belong to the scientific producers): BNIP3, per-compound maxima, source-versus-reasoning candidates. A discriminating question handed to SCI43: for the three flagged Cs+ rows, does the primary paper give 200 micromolar or 201 nanomolar? (the pIC50 says the former); the answer decides which column of the registry is wrong for that class of rows.
