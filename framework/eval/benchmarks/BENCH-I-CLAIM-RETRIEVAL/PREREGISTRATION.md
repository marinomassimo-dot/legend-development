# Benchmark I — claim-registry preload vs progressive targeted retrieval · PREREGISTRATION

> **Harness evidence, non-normative, non-scientific.** Nothing here is a claim, a conclusion
> about WWOX or an edit to a scientific current file. Fixtures quote historical registry state;
> they do not change it. Written and committed **before** any fixture was run through a
> retrieval strategy or a model.

## 0 · The question

`framework/manuals/operator_manual.md` § 1.1 loads `claim_registry_current.md` whole in every
scientific profile because *"una claim che il paper contraddice può non essere collegata al
paper — un recupero selettivo non può garantirlo"*. Benchmark I measures that sentence on the
repository's own history, in two separate experiments:

- **I1 — retrieval.** Does the affected claim reach the candidate set? Deterministic, no model.
- **I2 — attention.** On fixtures where I1 succeeded, does a model identify the affected claim as
  reliably from the retrieved records (Arm C) as from the whole registry (Arm A)?

A miss in I1 is a retrieval failure; a miss in I2 is an attention failure. They are never pooled.
There is no desired winner: a result that keeps the preload is a successful benchmark.

## 1 · I0 baseline (measured at `main` = `9666003`)

| Quantity | Value |
|---|---|
| Canonical path | `disease-models/wwox/registries/claim_registry_current.md` |
| Bytes / lines | **127,862 B** / 746 lines |
| Claim records | **40** (`## CLAIM 001` … `## CLAIM 040`; 45 `##` headings — 5 are prose sections) |
| Fields per claim | Title · Status · Type · Pathway · Genotype/model relevance · Transferability · clinical relevance · Summary · Clinical meaning · Source · Wikilinks · Impact on Working Model, plus appended dated boundaries |
| Retrieval fields | `registry_records.py`: `--pmid` (identity / mention), `--id`, `--theme` (literal, case-insensitive substring, `all`/`any`), `--field NAME=VALUE`, `--hops` (wikilinks), `catalog`, `fields` |
| Routes that preload it whole | `operator_manual.md` § 1.1, § 1.2, § 2 · `deep_dive_manual.md` (minimum obligatory set, § 7.7) · `legend-start` · `legend` (comparison, step 3) · `legend-deepdive` skill (stage 4) · `legend-deepdive` agent · `legend-discovery` (step 2b, novelty check) · `legend-hypothesis-forge` (step 0) |
| Routes already targeted | paper registry and literature log **by record** (`registry_records.py get --pmid <PMID> --hops 1`) in all of the above; discovery ledger by `--theme` / `--id` in `legend-discovery` |
| Model runner | `claude -p` (Claude Code 2.1.282) headless, `--tools ""`, `--strict-mcp-config`, `--setting-sources ""`, `--no-session-persistence`, `--system-prompt` replacing the default. Verified: an independent API call per invocation, JSON output with **native** usage (input / cache / output tokens). `MODEL_RUNNER_AVAILABLE = YES` · `REPETITIONS_POSSIBLE = YES`. Temperature is **not exposed** by the CLI. |
| Prior Benchmark-I work | none found (no design record, prototype or strategy names). The D-series named no B/C/D strategies; the names below are new and are the only ones. |

## 2 · Fixtures (I1a)

Source: every commit that changed a `## CLAIM` record since the public edition (`git log --
claim_registry_current.md`, unshallowed history, 11 commits, 34 record-level changes).
Curated input: [`fixture_spec.json`](fixture_spec.json). Built output: [`fixtures.json`](fixtures.json),
by `python3 framework/scripts/claim_retrieval_bench.py build`.

- **Unit.** One fixture = one historical event `(commit C, triggering PMID P)`.
- **Ground truth — derived, not chosen.** Target claims = claims that exist at `C^`, changed in
  `C`, and whose added diff lines reference `P` (the PMID string, or a wikilink to a paper record
  whose Identifier at `C` names `P`) more often than the removed lines. One declared manual
  override (I15), with its evidence in the spec.
- **Seed — the first pass, before comparison.** The `verbatim_locators.entries[*].snippet` of
  `deepdive_manifests/PMID<P>.json` **at `C^`**, i.e. the reading as it stood before the claim
  change landed; `CLAIM nnn` tokens and double-bracket wikilinks scrubbed and counted (0 in every snippet
  seed; the proposition seeds of I17, I18, I21, I23 carried 4, 3, 6 and 1 — which is why
  propositions are **secondary** only).
- **Classes.** 21 STRONG · 4 USABLE_WITH_LIMITATION (I08 review with a secondary role; I15
  manual override; I25 multi-dataset synthesis) · 11 INVALID / accounted-for events in the
  appendix of `fixture_spec.json` with reasons · 1 NO_CHANGE control (I00, the erratum
  PMID 30470736; I2 only, no retrieval target).
- **Headline** = STRONG only. USABLE_WITH_LIMITATION reported separately.

## 3 · I1 strategies and procedure (I1b)

All retrieval runs against a detached worktree at `C^` (the registries **before** the change),
with `registry_records.py` at the benchmark's commit.

| Strategy | Definition |
|---|---|
| **FULL** | Not a retrieval. All claims; the context-size reference. |
| **CURRENT** | `registry_records.select(pmid=P, hops=1)` over all seven surfaces — the call `legend` step 3 already makes. Candidate claims = claim records among its hits (mention, or one wikilink hop). |
| **PROGRESSIVE** | CURRENT ∪ a literal term query on the claim registry: tokens of the seed (`[^\W_](?:[\w-]*[^\W_])?`, lower-cased, length ≥ 4, or ≥ 3 with a digit); document frequency read from the tool's own `term_report`; terms kept when `1 ≤ DF ≤ df_cap`, `df_cap = max(1, floor(0.10 × N_claims))` (4 of 40); candidate set = `select(theme=kept, match=any, sources=[claim_registry_current], hops=0)`. No stemming, synonyms, embeddings, ranking or cap on the union. |

- **Primary configuration:** snippet seed, `df_cap_fraction = 0.10`.
- **Sensitivity (pre-declared, reported beside, never replacing the primary):** `df_cap_fraction`
  0.05 and 0.20; proposition seed at 0.10.
- **Recorded per fixture × strategy:** targets, operations, candidate IDs, target present,
  candidate count, claim bytes returned (whole records), registry fraction, selection path per
  candidate (PMID route with its match reason, or the literal terms that matched), binding state
  and commit read, runtime.

## 4 · I1 acceptance and miss diagnosis (I1c)

- **I1 acceptable** ⇔ PROGRESSIVE retrieves **every target of every STRONG fixture**, or every
  miss is diagnosed, classified (`QUERY_FORMULATION_GAP` · `FIELD_COVERAGE_GAP` ·
  `LINK_GRAPH_GAP` · `RECORD_STRUCTURE_GAP` · `AMBIGUOUS_FIXTURE` ·
  `OTHER_DETERMINISTIC_RETRIEVAL_GAP`) **and** repaired as an implementation defect within D-layer
  semantics (then all fixtures re-run). A miss whose repair needs semantics, synonyms,
  embeddings or new architecture is **recorded as a limitation and makes I1 not acceptable for
  the preload-removal decision.**
- Candidate count and bytes are secondary; bytes are never optimised at the expense of recall.
- The parameters above are **frozen now**. They are not changed after results are seen; a
  post-hoc variant, if ever run, is labelled post-hoc and cannot decide anything.

## 5 · I2 protocol (pre-registered now, frozen again at the I1 freeze point)

- **Eligible fixtures:** every STRONG and USABLE_WITH_LIMITATION fixture whose **every** target
  PROGRESSIVE retrieved (primary configuration), plus the I00 no-change control. **No further
  selection**: all eligible fixtures run, so the subset cannot be cherry-picked. Difficulty is
  reported per fixture afterwards (linked vs term-only retrieval; single vs multi-target;
  relationship type; candidate count).
- **Arms — identical except the claim context.**
  - **A (FULL PRELOAD):** the whole `claim_registry_current.md` at `C^`, verbatim.
  - **C (PROGRESSIVE):** the same file's preamble (the bytes before its first `##`, which
    `registry_records.py` ships with every answer) + the PROGRESSIVE candidate records, whole,
    in registry order, each exactly as in the file.
  - Both: the same system prompt, the same task text, the same source line (`PMID <P>`) and the
    same first-pass observations (the snippet seed). No target label reaches either arm.
- **Task.** Return JSON `{"affected": [{"claim_id", "relationship", "reason"}]}`, relationship ∈
  `supports / strengthens` · `narrows / qualifies` · `contradicts / weakens` · `requires review`;
  an empty list means *no affected existing claim*.
- **Model and runner.** `claude-opus-5-5` through `claude -p` as in § 1; CLI-default effort; no
  tools; temperature not exposed (recorded as such). **3 independent repetitions per fixture per
  arm.** Order: the full job list (fixture × arm × repetition) is shuffled with
  `random.Random(20260925)` and run with 4 workers. Each context is hashed (SHA-256) before the
  run; hashes, native token usage and the raw output are stored.
- **Blind grading.** Deterministic: outputs are keyed by an opaque job id; the grader reads only
  the fixture's target set, its relationship label and the parsed answer. Arm is joined **after**
  grading. No model grader is used.
  - Target identification per run: **correct** (every target named) · **partial** (some) ·
    **incorrect** (none). For I00: correct ⇔ empty answer.
  - Secondary: relationship match on identified targets; non-target claim IDs named ("extras" —
    reported as *unlabelled*, not as wrong: history labels what changed, not everything a paper
    touches).
  - Error taxonomy, per missed target: `TARGET_NOT_IN_CONTEXT` (retrieval — must be 0 in I2) ·
    `TARGET_IN_CONTEXT_NOT_SELECTED` (attention: missed, no non-target named) ·
    `WRONG_NEARBY_CLAIM` (discrimination: missed while a non-target was named) ·
    `EXTRA_UNSUPPORTED_CLAIMS` (precision, counted per run) · `RELATIONSHIP_WRONG`
    (interpretation, per identified target) · `OTHER` (unparseable answer).
- **Decision standard (zero margin; no existing record pre-registered one).** Per fixture and
  arm, score = identified targets / (targets × repetitions). A fixture *favours A* when
  `score_A − score_C ≥ 0.5`, and *favours C* symmetrically.
  - **SUPPORTED** ⇔ I1 acceptable **and** no fixture favours A **and** pooled C identifications ≥
    pooled A identifications.
  - **NOT SUPPORTED** ⇔ I1 not acceptable, **or** ≥ 2 fixtures favour A and pooled C < pooled A.
  - **INCONCLUSIVE** ⇔ anything else, or I2 could not run validly.
  - No significance test is claimed on a sample this small; the paired raw table is the result.

## 6 · I3 routing consequence (pre-declared)

- SUPPORTED → the smallest change: the benchmarked comparison routes load claims **on demand**
  through `registry_records.py` instead of whole; the registry, its storage and explicit
  full-registry use for census/review tasks are untouched.
- NOT SUPPORTED or INCONCLUSIVE → the preload stays; the reason is recorded; no retrieval
  redesign inside Benchmark I.
