# Benchmark I · I1 — deterministic retrieval recall · RESULTS (frozen)

> Harness evidence, non-scientific. Produced by `python3 framework/scripts/claim_retrieval_bench.py i1`
> against [`fixtures.json`](fixtures.json) under [`PREREGISTRATION.md`](PREREGISTRATION.md);
> raw per-fixture output, operations, candidate IDs, selection paths and diagnoses in
> [`i1_results.json`](i1_results.json). Two runs gave byte-identical rows apart from runtime.
> Every read was `BOUND` to the event's parent commit (a detached worktree, removed after use).

**Erratum to PREREGISTRATION § 2:** it says 21 STRONG / 4 USABLE_WITH_LIMITATION. The spec it
describes holds **22 STRONG / 3 USABLE_WITH_LIMITATION** (I08, I15, I25). The spec is
authoritative and was not changed; the count in prose was wrong.

**Instrument changes after the preregistration commit, before results were read as final:** the
`binding` field read a non-existent key (`state` → `verdict`), and a per-miss `diagnose` step was
added. Neither touches candidate generation; the rows are identical with and without them.

## Headline (STRONG, primary configuration: snippet seed, df_cap_fraction 0.10)

| | CURRENT (`get --pmid --hops 1`) | PROGRESSIVE (CURRENT ∪ literal terms) | FULL |
|---|---:|---:|---:|
| STRONG fixtures | 22 | 22 | 22 |
| target labels | 29 | 29 | 29 |
| **targets retrieved** | **13 / 29 (45 %)** | **25 / 29 (86 %)** | 29 / 29 by definition |
| fixtures fully retrieved | 9 / 22 | 18 / 22 | 22 / 22 |
| median candidates | 1 | 31 (of 35–39) | 35–39 |
| max candidates | 4 | 38 | 39 |
| **median registry fraction (claim bytes)** | **2.6 %** | **83.3 %** | 100 % |
| **unexplained misses** | — | **0** (4 misses, all diagnosed below) | — |
| runtime per fixture | 0.20–0.46 s | 0.29–0.84 s | — |

USABLE_WITH_LIMITATION (3 fixtures, 6 labels): CURRENT 1/6, PROGRESSIVE 6/6 at a median 84.1 %.
No-change control I00: CURRENT 0 candidates, PROGRESSIVE 7 (19.8 %).

### Pre-declared sensitivity (never replaces the primary)

| Setting | PROGRESSIVE targets | fully retrieved | median registry fraction |
|---|---:|---:|---:|
| df_cap 0.05 | 22 / 29 | 17 / 22 | 54.3 % |
| **df_cap 0.10 (primary)** | **25 / 29** | **18 / 22** | **83.3 %** |
| df_cap 0.20 | 29 / 29 | 22 / 22 | 91.1 % |
| proposition seed, 0.10 | 27 / 29 | 20 / 22 | 91.0 % |

**The shape of the result:** there is no setting at which literal retrieval is both complete and
small. The only configuration that reaches every target returns **91 %** of the registry; the
one route that is small (CURRENT, 2.6 %) reaches **45 %** of the targets. Recall is bought with
bytes almost one-for-one, because a paper's first-pass text shares *some* distinctive word with
most claims in a 40-claim registry about one gene.

## Per fixture

| Fixture | Class | Event | PMID | Targets | CURRENT hit | CUR n / % | PROGRESSIVE hit | PROG n / % | Terms kept/extracted | Miss class |
|---|---|---|---|---|---|---|---|---|---|---|
| I01 | STRONG | `ab5012e` | 30290271 | 005 | 0/1 | 0 / 0.0% | 1/1 | 28 / 80.4% | 36/161 |  |
| I02 | STRONG | `d0f6a78` | 19500159 | 005 | 0/1 | 0 / 0.0% | 1/1 | 31 / 88.6% | 70/211 |  |
| I03 | STRONG | `d0f6a78` | 31340538 | 014, 015 | 0/2 | 0 / 0.0% | 1/2 | 23 / 64.9% | 30/95 | LINK_GRAPH_GAP |
| I04 | STRONG | `ec7c09f` | 34747138 | 004 | 1/1 | 2 / 4.3% | 1/1 | 27 / 66.4% | 48/173 |  |
| I05 | STRONG | `f37d449` | 30755385 | 009 | 0/1 | 0 / 0.0% | 1/1 | 25 / 67.3% | 31/112 |  |
| I06 | STRONG | `419b680` | 34747138 | 003, 004 | 1/2 | 2 / 6.8% | 1/2 | 27 / 67.6% | 48/173 | QUERY_FORMULATION_GAP + LINK_GRAPH_GAP |
| I07 | STRONG | `419b680` | 32000863 | 016 | 0/1 | 0 / 0.0% | 1/1 | 38 / 96.8% | 86/270 |  |
| I08 | USABLE | `419b680` | 34831305 | 003, 004, 016 | 0/3 | 0 / 0.0% | 3/3 | 31 / 79.6% | 56/197 |  |
| I09 | STRONG | `749a9a9` | 21075834 | 009, 034 | 0/2 | 0 / 0.0% | 1/2 | 32 / 78.6% | 55/173 | QUERY_FORMULATION_GAP |
| I10 | STRONG | `749a9a9` | 17575124 | 032 | 1/1 | 1 / 3.7% | 1/1 | 14 / 40.1% | 19/55 |  |
| I11 | STRONG | `749a9a9` | 17360458 | 032, 036 | 2/2 | 4 / 13.7% | 2/2 | 19 / 50.3% | 22/76 |  |
| I12 | STRONG | `749a9a9` | 23254685 | 036 | 1/1 | 1 / 3.3% | 1/1 | 24 / 64.9% | 33/88 |  |
| I13 | STRONG | `749a9a9` | 18974271 | 036 | 1/1 | 1 / 3.3% | 1/1 | 23 / 59.9% | 24/80 |  |
| I14 | STRONG | `749a9a9` | 42422765 | 011 | 1/1 | 1 / 3.8% | 1/1 | 33 / 86.8% | 63/249 |  |
| I15 | USABLE | `2a35aec` | 34268881 | 002 | 1/1 | 8 / 23.2% | 1/1 | 35 / 91.1% | 56/186 |  |
| I16 | STRONG | `2a35aec` | 33916893 | 017, 019, 030, 033 | 2/4 | 4 / 14.0% | 4/4 | 36 / 92.4% | 82/272 |  |
| I17 | STRONG | `2a35aec` | 15070730 | 023 | 0/1 | 0 / 0.0% | 1/1 | 35 / 89.8% | 72/222 |  |
| I18 | STRONG | `2a35aec` | 21115974 | 023 | 1/1 | 2 / 6.7% | 1/1 | 35 / 90.5% | 105/401 |  |
| I19 | STRONG | `2a35aec` | 29724996 | 025 | 1/1 | 2 / 5.8% | 1/1 | 30 / 82.6% | 73/287 |  |
| I20 | STRONG | `2a35aec` | 41562193 | 029 | 1/1 | 1 / 2.0% | 1/1 | 35 / 90.6% | 75/343 |  |
| I21 | STRONG | `2a35aec` | 26499798 | 030 | 0/1 | 0 / 0.0% | 1/1 | 37 / 94.3% | 88/279 |  |
| I22 | STRONG | `2a35aec` | 20530675 | 036 | 0/1 | 1 / 5.2% | 1/1 | 37 / 95.2% | 86/366 |  |
| I23 | STRONG | `2a35aec` | 21731849 | 036 | 0/1 | 0 / 0.0% | 1/1 | 34 / 89.8% | 66/210 |  |
| I24 | STRONG | `3f65917` | 32581702 | 039 | 0/1 | 0 / 0.0% | 0/1 | 31 / 83.9% | 79/293 | AMBIGUOUS_FIXTURE |
| I25 | USABLE | `3bd71c8` | 42422765 | 005, 037 | 0/2 | 3 / 11.3% | 2/2 | 30 / 84.1% | 76/249 |  |

(CUR / PROG n / % = candidate claims / their whole-record bytes as a share of the claim registry
at the event's parent, which was 70,978–119,152 B and 35–39 claims across the events.)

## I1c — miss diagnosis (every PROGRESSIVE miss on a STRONG fixture)

Each stage below is computed by `diagnose()` and stored in `i1_results.json → rows[*].miss_diagnosis`.
All four targets were **addressable** at the parent (`select(record_id=…)` returned the record).

| Fixture | Target | PMID route (stage 1) | Term route (stage 2) | Class | Fixed? |
|---|---|---|---|---|---|
| I03 | CLAIM 015 | Paper record `PAPER 021` (PMID 31340538) exists at the parent and does **not** link CLAIM 015; CLAIM 015 **does** link `[[paper_registry_current#PAPER 021]]`. The tool follows links **out of** a hit, never **back into** one, so a claim citing the paper by record link is invisible to `--pmid`. | 7 shared terms, all over the cap (`gene, level, normal, than, that, with, wwox`) — the seed is postnatal (PND 5–21); the claim is about *prenatal* misassembly; they share no distinctive word. | **LINK_GRAPH_GAP** | **No** — see below |
| I06 | CLAIM 003 | `PAPER 005` (PMID 34747138) does not link CLAIM 003; CLAIM 003 does not cite the paper; CLAIM 004 (hit) does not link it. | 8 shared terms, all over the cap: `myelination` is in the claim and the seed, but it is in > 3 claims. The discriminating concept is common vocabulary in this registry. | **QUERY_FORMULATION_GAP + LINK_GRAPH_GAP** | No — needs concept weighting (ranking) or a semantic link |
| I09 | CLAIM 009 | `CORPUS P358` (PMID 21075834) links nothing relevant. | 10 shared terms, all over the cap. The discriminating acronym **ROS** occurs 6× in the seed and 4× in the claim, but the pre-registered token rule keeps 3-character tokens only with a digit. `redox` is in the claim and not in the seed. | **QUERY_FORMULATION_GAP** | No — changing the token rule after seeing results is tuning |
| I24 | CLAIM 039 | `PAPER 020` (PMID 32581702) does not link CLAIM 039. | 4 shared terms, all over the cap. **The seed contains no `cerebel*` token at all**: the triggering sentence (*"the development of cerebellum was delayed"*, P1) is **not among the 21 locators of the manifest at the parent** — the link was made later by a question-driven audit (BATCH_20260921_001), not by the first pass. The claim itself says *cervelletto* (Italian) and *cerebellar*. | **AMBIGUOUS_FIXTURE** (counted, not removed) | No — the seed does not carry the trigger |

**Why I03 was not repaired.** A candidate repair — a record that wikilinks to the paper's identity
record counts as a `mention` — was implemented and measured once (**post-hoc, non-deciding**:
[`i1_posthoc_backlink_mention.json`](i1_posthoc_backlink_mention.json)). It turns
`test_registry_records.CaseEReachableOnlyByExpansion` red: the D-layer pins that a claim reached
through a link is reached **only by `--hops`**, outward. Reversing that is a change of approved
semantics, not a defect inside them, so the repair was **reverted** and I03 stands as a
limitation. What it would have bought: CURRENT 13 → **17 / 29** at 3.5 % median (I03 gains two targets, I07 and
I16 one each); PROGRESSIVE 25 → 26 / 29. It does not reach I06, I09 or I24.

**Implementation defects found: 0.** Architectural limitations: 3 (I03, I06, I09). Fixture
ambiguity: 1 (I24, kept in the denominator, against retrieval).

## I1 verdict under the pre-registered acceptance rule

**I1 NOT ACCEPTABLE for preload removal.** PROGRESSIVE misses 4 of 29 STRONG targets; none is an
implementation defect inside D-layer semantics; three need either semantics the D-layer does not
have (backlinks, concept weighting, stemming / bilingual matching) or a different seed rule, and
the fourth needs an observation the first pass did not make. Independently of recall, the
progressive candidate set is **83 % of the registry at the median** — the preload it would replace
is, to within a sixth, what it returns.

I1 is **interpretable** (zero unexplained misses), so I2 proceeds on the 21 eligible fixtures
(18 STRONG + 3 USABLE whose every target PROGRESSIVE retrieved) plus the I00 control, exactly as
pre-registered.
