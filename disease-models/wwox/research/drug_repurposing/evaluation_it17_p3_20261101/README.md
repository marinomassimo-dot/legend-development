# IT17 P3: a prospective evaluation that can be trusted, and one task measured now

Non-canonical research material; not medical advice; computational results, no benefit claim. Public edition, WWOX-DEE genotype class. Package written 2026-11-01. The IT16 pre-registration is not edited; the IT16 analysis stays as a **descriptive** result (see `../predictive_it16_p2_20261101/README.md`).

## 1. Freeze: what is exact and what is reconstructed

IT16 called 2026-10-29 the freeze of "the ranking". The git history says:

| Item | State on 2026-10-29 (first commit with `selections.tsv`: `04ebdb5af51d6075fe1d2fab7e8f289fdb9d14fb`, 2026-10-29T22:36:17Z) | State read by the IT16 scorer |
|---|---|---|
| General selection, ids and order | U07 U17 U24 U21 U10 U15 U20 U25. **Exact**: identical in all 10 later commits that touch `selections.tsv` | same |
| Pool | 30 units (`units.tsv` sha256 `8da5626a5ef70514e43f8eccc522486472685ef8480d5ba73ee42eca39fca351`) | 69 units (built 2026-10-30 and 2026-10-31) |
| Rules | `RULES_VERSION` R1 | R4 |
| `member_evidence.tsv` (source of B1, B2 and the "tested" flag) | **did not exist**; first committed `087fd66f205c9d116985dcead1aff650009c1e40` (2026-10-30T10:46Z, R3) | current file |
| `selections.tsv` bytes | sha256 `8addeb799b070e519301f9919f90c4eb53515f4443d82d6f132a2b74cd5f3b4a` (text differs from today's; unit set and order do not) | current file |

So only the **set and order of the 8 selected units** is a faithful 2026-10-29 prediction. The 69-unit pool, the baselines B1 and B2 and the tested flags are later constructions; IT16 measures 3 and 4 used data that did not exist at the claimed freeze. `predictive_it16_p2.py` also reads the live tables, so a re-ranking would change what it calls "predicted". This is why the IT16 numbers are descriptive, not a prospective test (they were already declared not measurable by IT16's own rule).

## 2. New freeze (real instant, immutable references)

`prospective_eval.py freeze` wrote `freeze_20261101/FREEZE.json` and `freeze_20261101/frozen/` (copies of `units.tsv`, `selections.tsv`, `member_evidence.tsv`). It records: UTC instant (`frozen_at_utc`), git commit of the inputs, sha256 of every input, pool ids, selection (top 8), B1 baseline order, rules file path and sha256 with the version note (R4; referenced by digest, not copied), method version and the scorer's own sha256, the task, the success definition and the design's minimal-evidence rule. It refuses to run when an input differs from its committed copy and refuses to overwrite an earlier freeze.

`prospective_eval.py evaluate` re-hashes the frozen copies and **exits 3 on any mismatch**, then scores only from the frozen copies. A later re-ranking therefore cannot change what was predicted (fixture test). The frozen selection is the same eight units as on 2026-10-29; what is new is that pool, baseline and rules are now immutably tied to a real instant and commit.

## 3. Outcome semantics

Task before metric: **select interventions to test next**; the prediction is "a favourable result on the unit's stated objective in a WWOX-deficient system". "Was tested" is therefore not an outcome. Outcome row fields: `unit_id`, `intervention`, `system_context`, `endpoint`, `comparator`, `result` in {favourable, null, contrary, undeterminable}, `objective_match` in {yes, no, unknown}, `origin_group` (rows sharing an origin count once), `pub_date`, `provenance`.

Scoring rules (fixture-tested in `test_prospective_eval.py`): success needs favourable and objective_match yes and a date after the freeze day; contrary and null are reported as such and never as successes; a result on another endpoint (for example a safety finding) is `off_objective` and stays visible; undeterminable or unknown-match stays unknown and leaves the determinate denominator; the same origin counts once per unit and once toward the rule across units; conflicting rows of one origin become undeterminable, not netted. The minimal-evidence rule belongs to this design only (at least 3 determinate origin groups after the freeze, an arbitrary floor chosen so that one paper cannot be a result); below it the tool exits 2 and shows counts with no claim. IT16's threshold of 5 is not carried over and no other evaluation is blocked by either number.

Descriptive recoding of the 7 IT16 outcome rows (`outcomes_it16_recoded.tsv`, coded by me from the IT16 table and ranking caveats, papers not re-read, deliberately conservative): IT16 counted 7 of 7 tested units as hits; under the new semantics 2 units (lithium, ethosuximide) are favourable on objective from **1** origin paper, 4 units are undeterminable (d-APV and AAV9 only by my conservative "objective match unknown", ketogenic diet, A51), and vigabatrin's only recorded result is a safety finding on another endpoint. Sensitivity: coding d-APV and AAV9 as matching gives 3 origin groups. There are no post-freeze outcomes, so nothing is scored prospectively yet.

## 4. Task measured now: direction of action (technical correctness of one stored field)

Design and rules: `PRE_REGISTRATION_DIRECTION.md` (written before the run, amendment log, lock). Tool: `direction_task.py dev|eval`; tests `test_direction_task.py`; numbers `results_direction.json`; every discordant pair `discordant_pairs.tsv` (ids and coarse classes only). Inputs: catalogue ChEMBL curated mechanisms (human, direct) against GtoPdb release 2026.3.1 interactions (human), joined on parent ChEMBL id and UniProt; digests in the results file. Split by compound hash (dev 5 924 pairs, eval 5 993). No network, about 2 s. One dev-only amendment (partial agonists are direction-ambiguous and moved to "no direction" on both sides, justified before any EVAL read-out); one post-lock parser fix touching only the card-link subset (disclosed in the pre-registration).

| EVAL measure | Value |
|---|---|
| Module pairs in EVAL / with a GtoPdb counterpart | 5 993 / 992 (5 001 have none) |
| Unresolved among those 992 | 32 module no-direction, 32 GtoPdb no-direction, 2 GtoPdb conflict |
| Determinate pairs (both sides one direction) | 926 (shared-reference pairs: 158; independent-reference-only: 768) |
| Module (ChEMBL direction) correct | 923 / 926 = 0.997 (Wilson 0.990 to 0.999); independent-reference-only 765 / 768 = 0.996 (0.989 to 0.999) |
| B0 most-frequent label (DECREASE) | 706 / 926 = 0.762 (0.734 to 0.789) |
| B1 per-target majority from DEV | 802 / 926 = 0.866 (0.843 to 0.887) |
| Module right and B1 wrong / reverse | 124 / 3 (sign test p below 1e-30) |
| Discordant pairs retained | 3 in EVAL (3 more in DEV); all six have the module saying INCREASE where GtoPdb says DECREASE; none shares a reference |
| Module's own relations (compounds linked to a card; DEV plus EVAL, descriptive) | 28 linked compounds; 11 determinate pairs, 0 discordant (Wilson lower bound 0.74) |
| Cost | 1 script of about 270 lines, 2 s, 0 network calls, no curation rows |

Decision rules as registered: the accuracy lower bound (0.990) exceeds 0.90 on well over 100 pairs, so the stored direction is technically consistent with an independent curated source **within the covered space**; the gain over B1 is 13 points with p far below 0.05, so "added value over the target prior" holds, but the thing that adds the value is the imported ChEMBL curation, not any LEGEND reasoning.

### Shown
- On 926 compound-target pairs that both ChEMBL and GtoPdb describe with a clear direction, the catalogue carries ChEMBL's direction faithfully and it matches GtoPdb in 99.7 percent; the 6 discordances over dev and eval are listed.
- The card-linked subset is too small to say anything beyond "no discordance in 11".

### Not shown
- Coverage: 83 percent of the module's human mechanism pairs have no GtoPdb counterpart (and GtoPdb is biased toward well-studied receptors, enzymes and channels), so nothing is shown for them. The agreement is for the easy, well-documented space; few WWOX-relevant candidates sit in it.
- Independence is partial: the two curators draw on the same pharmacology literature, labels and each other; excluding shared PMIDs did not change the figure but does not remove upstream sharing.
- Not matching quality (which compound to propose), not hypothesis generation, not biological prediction, not benefit, and nothing about whether the documented direction is the beneficial direction for WWOX deficiency. NMDAR/GSK3 interaction is not reopened.

## 5. Files

`prospective_eval.py`, `test_prospective_eval.py` (14 tests: freeze record, digest refusal, contrary/null/off-objective/unknown handling, origin counted once, pre-freeze exclusion, no write on `--help`), `freeze_20261101/`, `outcomes_it16_recoded.tsv`, `PRE_REGISTRATION_DIRECTION.md`, `direction_task.py`, `test_direction_task.py`, `results_direction.json`, `discordant_pairs.tsv`. ChEMBL-derived (CC BY-SA 3.0) and GtoPdb-derived (CC BY-SA 4.0) labels in `discordant_pairs.tsv` and the results keep those terms; the raw third-party files stay in the gitignored cache.

## Sources and terms

The direction task compares labels derived from ChEMBL (EMBL-EBI, CC BY-SA 3.0, release as recorded in the pre-registration) and the IUPHAR/BPS Guide to PHARMACOLOGY (CC BY-SA 4.0, release 2026.3.1). Only identifiers and coarse direction classes are tracked here; the downloaded third-party files stay in the ignored corpus with their digests. Credit lines for the sources are in `ACKNOWLEDGEMENTS.md`.
