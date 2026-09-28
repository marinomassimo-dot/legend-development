# COMMIT CANDIDATE — CC-20260928-MIRROR003-REPAIRS-01

**Candidate ID:** CC-20260928-MIRROR003-REPAIRS-01
**Status:** `PROPOSED — NOT PROPAGATED`
**Base head:** `a3f68b1` (`main` at dispatch; this candidate was written on `task/mirror003-repairs`)
**Author:** ACTOR_ID `scientist`, package `m003`, dispatched by the Orchestrator under the operator
standing authorisation of 2026-09-27 (*"procedi tu, ti autorizzo su tutto"*).
**Source of the task:** the Mirror ex-post review of `BATCH_20260927_003`, persisted verbatim at
[`session_evaluations/2026-09-27_BATCH_20260927_003_mirror_review.md`](../session_evaluations/2026-09-27_BATCH_20260927_003_mirror_review.md)
(overall verdict *CONFIRMED WITH FINDINGS*: **1 BLOCKING-SCIENTIFIC**, 9 MINOR, 6 NOTE).
This candidate carries **every item of that review that needs one of the four current files**: B1, M2,
M3, M4, M5, M6, M7, M8, M9, and the canonical halves of N2, N4 and N6 — which the dispatch had
expected to be non-canonical and which are not (see §1.1). The items applied outside a batch, the two
Harness hand-offs (M10, N5) and the one finding contested in part (M6b) are in §5 and §6.
**Declared change class: `MINOR`, with one `MINOR — INFERENCE WITHDRAWN` item (B1) and one
`MINOR — STRUCTURAL` item (M3/N6).** Per-item classes are declared in §1 and again beside each op.
No claim `Status`, `Type`, `Transferability`, BLOCCO 1 field or therapeutic `SCORE`/`SAFETY` text
moves; `CLAIM 005`'s epileptogenesis prohibition is not touched (the one `CLAIM 005` op addresses the
`Wikilinks` line only); no claim is added or removed.
**Receipts read:** `FTR-20260927-42589397-02` (PMID 42589397, `partial_fulltext_read`,
`files/fulltext/PMID42589397_ZZ2026_PMC_2026-09-27.xml`, sha256 `ae7f4291…f898af`, re-hashed this
session: **equal**) · `FTR-20260921-42589397-01` (the earlier verification receipt) ·
the PMID 36779245 and PMID 36828035 artefacts re-hashed this session:
`files/fulltext/PMID36779245_Oliver2023_PMC_2026-09-27.xml` = `780f42de…c7e7a34` (equal) and
`files/fulltext/PMID36828035_Hussain2023_PMC.xml` = `004c59b5…568fd22` (equal).
**Manifests:** `deepdive_manifests/PMID36828035.json` (64 → **65** entries, entry 64 added here) ·
`deepdive_manifests/PMID42589397.json` (5 → **7** entries, entries 5–6 added here; one further entry
was written and **withdrawn** — see §5(h)). `deepdive_manifests/PMID36779245.json` and
`PMID40875931.json` unchanged: the locators B1 and M8 rest on were already there.
**`context_policy`: `QUESTION_DRIVEN`** — declared. Held before any source was opened: the Mirror
review; `CLAIM 005 · 016 · 025 · 030 · 033 · 038 · 040`, `PAPER 007 · 018 · 042 · 059 · 117`,
`CORPUS P306 · CORPUS-STUB-058` read **by record** with `registry_records.py get` / record-scoped
`awk`, never by grep over the two large registries; WM rows 016 and the two count sentences; the
four manifests and two receipts named above; `CC-20260826-CROSS-CLAIM-CENSUS-02`,
`CC-20260922-CLAIM025-SIGN-INVARIANCE-01`, the `BATCH_20260927_003` report and
`state_history.md` § 4. Questions fixed **before** reopening a source: *(1) are the two `Q230P`
patients of PMID 36779245 Table 1 really homozygous for the same allele, and do they differ on
anything besides survival; (2) what is the full Fig. 4e caption of PMID 36828035, sentence by
sentence; (3) what are the cohort sizes and the event counts of PMID 42589397, on the body surface
and not the abstract; (4) how many directed claim→claim edges did `BATCH_20260927_003` actually add,
and is the whole graph closed under reciprocity.*

---

## 1 · CURRENT_TARGET and verification of each Mirror item

Every Mirror statement below was re-checked against the current file (each `old` string measured as
occurring exactly once inside its record) and, where it concerns a source, against the fingerprinted
surface. **Twelve items are confirmed, one is confirmed in part with its second half contested, and
one was already repaired by Harness Engineering before this package opened it.** Nothing was taken
on the reviewer's word.

| Item | Mirror claim | Verified | How |
|---|---|---|---|
| **B1** | `CLAIM 030`'s *"Osservazione a due code"* says the pair *rafforza* the thesis; two patients homozygous for the same allele have the same residual function, so the claim's own rule predicts **similar** outcomes | ✅ **and more** | PMID 36779245 Table 1 read first-hand off the JATS XML: `Patient # 2` = *"c.689A > C, p.Gln230Pro (homozygous)"*, `Age, sex` *"23 y 11 m, M"*; `Patient # 5` = the same variant string, *"8 y 3 m (dec.), F"*; the `Genetic combination` row gives **both** as *Missense/missense*. **Additionally**: on the axis the claim calls *gravità* the two are **concordant** — Table 1 gives both `Intellectual disability: Profound`, `Speech: Nonverbal`, `Walking/ambulant: No`. The discordance is **survival only**. Mirror did not state this and it strengthens B1 |
| **B1 falsifier** | B1 falls if some record says residual function is not genotype-determined | ✅ **none found** | `CLAIM 030`, `CLAIM 019`, `CLAIM 033` read by record: no such statement. The new text therefore names individually varying proteostatic capacity as an **unenumerated rival** and says in place that asserting it would make the rule unfalsifiable by genotype — the escape hatch is named, not taken |
| **M2** | `CLAIM 038`'s unit note says the factor is `1.000`; `mg/ml → mg/dL` is ×100 | ✅ | 1 dL = 100 ml; the same sentence's own conversions are `40.3 → 4.030` and `169.0 → 16.900`, i.e. ×100 in Italian thousands notation. The stated factor is off by ten. The `state_history` half is handled in §5(c) |
| **M3** | `CLAIM 025` rests on PMID 42589397 with no PAPER/CORPUS/LIT record at all | ✅ | `registry_records.py get --pmid 42589397` returns no record; `grep -rn 42589397` over the three registries hits only `CLAIM 025`, `reading_state.md` and the receipt ledger. `trace_claim_foundation --claim "CLAIM 025"` → **`PAPER 091` alone**. LINT emits `[INFO] UNLINKED_SUPPORT_UNCHECKED … no registry record's Identifier names this PMID`. `CC-20260922-CLAIM025-SIGN-INVARIANCE-01` closed `PROPAGATED` and proposed no record |
| **M4** | WM BLOCK 2 row 016 and `CLAIM 016`'s `Impact on Working Model` still concede an elevated abundance | ✅ | WM:177 *"…not merely elevated abundance"*; `CLAIM 016` `Impact` *"(si perde un freno, non solo un livello)"*. The claim's own `PREMISE_TAG` says the carrying premise *"non è più l'abbondanza, che il claim non asserisce più"* |
| **M5** | `CLAIM 005` has no edge of any class to PMID 24369382 | ✅ | `trace_claim_foundation --claim "CLAIM 005"` lists `PAPER 006 · 057 · 058` only. `CLAIM 005`'s `Wikilinks` names `PAPER 006` alone; `PAPER 042`'s `Claim links` no longer names `005` (removed by `BATCH_20260927_003`) while `PAPER 042`'s **own** `Wikilinks` does name `CLAIM 005` — the asymmetry Mirror describes. `PAPER 059`'s `Claim links` names `037 · 038 · 039`, **not** `005`, so it has no edge either |
| **M5 precision** | *"quotes PMID 24369382 verbatim in four places"* | ⚠️ **three, not four** | Three verbatim quotes of that paper stand in the boundary — *«a few spontaneous seizures at ∼2 weeks of age»*, *«three of eight»*, *«No wild-type mice of matched age and background (n = 8)»*. The fourth `Mallaret` mention is a citation, and the fourth quoted string in the block (*«Seizures in the Wwox literature are a rat `lde/lde` phenotype»*) is LEGEND's own withdrawn sentence, not the paper's. For `PAPER 059` the boundary **cites** but does not quote. The finding stands unchanged; the count does not |
| **M6a** | `CLAIM 016 → CLAIM 040` was added with no return edge, so the census's *"closed under reciprocity"* is false | ✅ | `CLAIM 040`'s `Wikilinks`: `PAPER 011 · CLAIM 004 · 005 · 011 · 037` — no `016`. Reciprocity recomputed over the **whole** 41-claim graph and over the census's own pair set: of the 14 pairs its ops touched, **13 are closed and exactly one is not** — `016 ↔ 040` |
| **M6b** | *"`CLAIM 040 → CLAIM 004` was likewise left unreciprocated"* | ⚠️ **CONTESTED — see §6** | True as a graph fact, false as a defect of `BATCH_20260927_003`: `040 → 004` **pre-existed**, `004 ↔ 040` was never an adjudicated pair, and `OP-1` added `011 · 005 · 037` to `CLAIM 004` and not `040`. It is one of **nine** pre-existing one-directional edges in the graph, none created by that batch |
| **M7** | `PAPER 007`'s Olig2 boundary drops the locator's sampling-unit caution | ✅ | Fig. 4 caption read first-hand: *"Each data point shows measurement from a single independent region from n = 3 mice/group. Scale bar= 100 μm, data is represented as mean ± SEM, *p-value < 0.01, unpaired Student's t-test."* Locator entry 58's proposition says *"ITS UNIT IS THE REGION"*; its `snippet` stops one sentence earlier, so the record's *"`n = 3` mice per group, unpaired t-test"* had nothing carrying the unit. Entry **64** added here to carry it |
| **M8** | `CLAIM 033` (6a) calls a zero-event comparison a non-replication | ✅ | `deepdive_manifests/PMID40875931.json` entry 1: snippet *"Premature death 0 (0.0) 1 (7.7) 0 (0.0) 2 2.44 0.432"*, anchor *"columns N/N (n = 25), N/M (n = 13), M/M (n = 6), df, chi-square, Fisher exact p"* → **1 death in 25 + 13 + 6 = 44 genotyped individuals**. ⚠️ Declared: the three denominators come from the locator's **anchor**, not from a quoted table header, and that paper's full text is in no checkout here — so the new text says so in place |
| **M9** | `PAPER 117`'s *"largest WOREE cohort"* and `CORPUS P306`'s *"the only published assay"* are unqualified corpus-scoped universals | ✅ **and one more surface** | `PAPER 018` (PMID 36779245) pools **75** (13 + 62, per `CLAIM 033`); `PMID 40875931` has **50**; `PAPER 117` is *"20 additional cases … and review of the literature"*. Mirror named the `Role` field; the same superlative also sits in `PAPER 117`'s **`Genotype/model`** field, which Mirror did not name and which is repaired here too. `CORPUS P306` carries it in `Role` **and** `Note`, at abstract depth with `PREMISE: UNREAD_PRIMARY` and no receipt |
| **N2** | *"Twelve claim-to-claim wikilinks"* against 23 directed / 13 new pairs; *"38 of 38"* against *"39 of 39"* | ✅ **and canonical** | Counted from `CC-20260826-CROSS-CLAIM-CENSUS-02`'s own `OP-1`…`OP-8`: **23** directed edges (3 + 4 + 5 + 3 + 4 + 1 + 1 + 2) over **14** pairs, 13 newly connected. 🔴 *"Twelve"* stands in **`working_model_current.md` twice** — the `Last update` line and the `WM_v6.1` changelog row — so this half of N2 is canonical, not a research-layer note. The `38/39` half is non-canonical: §5(b), §5(c) |
| **N4** | *"la coorte ovarica — la più numerosa"* is ambiguous | ✅ **and canonical** | The sentence is in `CLAIM 025`'s evidence boundary. Verified first-hand: *"final DFS-proxy cohorts of 390 BRCA patients (22 events, 368 censored) and 228 OV patients (161 events, 67 censored)"*; *"(for example, Luminal A: n = 181)"*; *"A total of 618 patients … five molecular groups"*. OV is the largest **stratum** and smaller than the **BRCA cohort** the same sentence contrasts. ➕ The event counts, added here, show the ovarian null is **event-rich**, not underpowered — which Mirror did not note and which matters to how the bound reads |
| **N6** | `CORPUS-STUB-059` was deleted where the visible convention preserves | ✅ **decisively, and canonical** | The convention is not merely visible, it is **declared in the stub records' own fields**: `CORPUS-STUB-119` `Registry role` reads *"corpus placeholder only — conservato append-only come storia di audit, **mai cancellato**"*, and the stub **immediately adjacent** to the deleted one, `CORPUS-STUB-058`, was promoted to `PAPER 026` and kept: `Status: superseded`, `Registry role: preserved corpus placeholder`, `Next action: none — upgraded to PAPER 026`. 🔴 And the deletion's stated reason does not select its target: *"no record with an empty `Authors` field survives"* — `CORPUS-STUB-059` had **no `Authors` field at all**, and neither do the **167** stubs still in the file. Decision and repair in §2.3 and §4.3 |
| **M10** | the DisMech revision label regressed | ✅ — **harness, not this candidate** | Label history re-derived from git: `rev.7 → 12 → 7 → 12 → 7 → 8 → 9 → 15 → 16 → 16 → 17 → 13 → 14`. **The current baseline's label is NOT monotone**: it is `rev.14` while three earlier seals are labelled 15, 16 and 17. Hand-off in §5(i) |
| **N5** | `append_only_prefix` slices before it checks | ✅ at `53c9927` — **already fixed** | At `53c9927` the line was `prefix = sha256(…lines[:count]); if len(lines) < count or prefix != …`. Harness Engineering's `9ae0f58` moved the length check **first** and split it into its own message (*"the ledger was truncated, which is an incident, not a re-seal"*). Nothing is owed; §5(i) records it closed |

### 1.1 · Three items the dispatch expected to be non-canonical and which are not

The dispatch routed N2, N4 and N6 to "non-canonical surfaces … an appended dated correction note or a
minimal edit". Measured: **N2's count sits in `working_model_current.md` (twice)**, **N4's sentence
sits in `CLAIM 025`**, and **N6's repair is a record in `paper_registry_current.md`**. All three are
therefore in this candidate, which is where the four current files change. Only their research-layer
echoes — the batch report's `38 of 38`, the census candidate's disposition line, the `CLAIM 025`
candidate's disposition — are handled outside a batch, in §5.

---

## 2 · PROPOSED_DELTA — exact operation lists

### 2.1 `disease-models/wwox/registries/claim_registry_current.md` — `batch_commit.py propagate` (record-scoped)

Nine `replace-within` ops; all dry-run clean on base `a3f68b1`
(`DRY RUN … 9 op(s) on ['CLAIM 030', 'CLAIM 038', 'CLAIM 016', 'CLAIM 005', 'CLAIM 040', 'CLAIM 033',
'CLAIM 033', 'CLAIM 025', 'CLAIM 025']`). The ops JSON is the concatenation of the `op`/`id`/`old`/`new`
fields below, in order.

#### C30-1 (B1) — `CLAIM 030` · `replace-within` · **change class: `MINOR — INFERENCE WITHDRAWN`**

An inference inside a `T1` / `clinical relevance: VERY HIGH` claim about the reference genotype is
withdrawn and replaced by its negation. No `Status`, `Type` or `Transferability` moves and no datum
changes: the facts of the paragraph were verified correct patient by patient. It is classed as an
inference withdrawal rather than a wording repair **because the sign of the paragraph's conclusion
reverses**, and locator triples are supplied in §4.1 for that reason.

**old (verbatim):**

```text
✅ Questo **rafforza** la tesi di questo claim invece di contrastarla: se la gravità segue la **funzione residua** e non l'abbondanza né la classe sintattica, un genotipo che copre entrambe le code è esattamente ciò che ci si aspetta di vedere.
```

**new:**

```text
🔴 **Corretto 2026-09-28 (`CC-20260928-MIRROR003-REPAIRS-01`, revisione ex-post Mirror di `BATCH_20260927_003`, rilievo B1): questa coppia NON DISCRIMINA, e la lettura precedente — che «rafforza» la tesi — invertiva la regola del claim stesso.** I due pazienti sono omozigoti per lo **stesso** allele; poiché questo claim tratta la funzione residua come una proprietà dell'**allele** (`PREMISE: INFERENZA` — nessun record qui asserisce che la funzione residua vari fra individui a parità di allele), essi hanno la **stessa** funzione residua, e la regola del claim predice esiti **simili**, non due code opposte. La coppia quindi **non corrobora** la tesi: mostra che il genotipo, di qualunque classe, **non determina** l'esito individuale, e resta **neutra** fra questa tesi e le sue rivali. ⚠️ **La discordanza è inoltre solo sulla sopravvivenza:** sull'asse che questo claim chiama *gravità* la Table 1 dà **entrambi** i pazienti con disabilità intellettiva profonda, non verbali e non deambulanti — cioè **concordanti**. 🔴 **Le spiegazioni rivali non sono enumerate qui e restano tutte aperte:** loci modificatori, carico convulsivo, gestione clinica, capacità proteostatica individuale che facesse variare la funzione residua a parità di allele (se venisse asserita, renderebbe la regola non falsificabile dal genotipo, e nessun record la asserisce), bias di arruolamento. ✅ Ciò che la coppia **falsifica** è la **classe sintattica come predittore individuale** — vedi [[claim_registry_current#CLAIM 033]] riserva (6).
```

#### C38-1 (M2) — `CLAIM 038` · `replace-within` · **change class: `MINOR` (numeric correction)**

**old (verbatim):**

```text
e il fattore è lo stesso (1.000) su entrambe le righe
```

**new:**

```text
e il fattore è lo stesso (**×100**, perché 1 dL = 100 ml; corretto 2026-09-28, `CC-20260928-MIRROR003-REPAIRS-01` M2 — la cifra precedente, `1.000`, era sbagliata di un fattore dieci e contraddiceva le due conversioni della frase stessa) su entrambe le righe
```

#### C16-1 (M4) — `CLAIM 016` · `replace-within` · **change class: `MINOR` (mirror alignment)**

**old (verbatim):**

```text
(si perde un freno, non solo un livello)
```

**new:**

```text
(si perde un freno, e **nessun livello è asserito** — il dato di abbondanza è ritirato, `NOT_TESTED` in entrambe le direzioni; corretto 2026-09-28, `CC-20260928-MIRROR003-REPAIRS-01` M4)
```

#### C5-1 (M5) — `CLAIM 005` · `replace-within` · **change class: `MINOR` (navigation edge, non-evidential)**

Adds two **`wikilink_only`** edges. `trace_claim_foundation.EVIDENTIAL_EDGES = {"source_field",
"claim_links"}`, so a `Wikilinks` entry is rendered `reference only (wikilink_only)` and is excluded
from the species-drift test by construction — verified in §3. This is the class Mirror's own F5 said
existed and was not used; it is used here and nowhere else. The op addresses the `Wikilinks` line
only and does **not** intersect `CLAIM 005`'s epileptogenesis prohibition.

**old (verbatim):**

```text
**Wikilinks:** [[paper_registry_current#PAPER 006]] · [[claim_registry_current#CLAIM 004]]
```

**new:**

```text
**Wikilinks:** [[paper_registry_current#PAPER 006]] · [[paper_registry_current#PAPER 042]] · [[paper_registry_current#PAPER 059]] · [[claim_registry_current#CLAIM 004]]
```

#### C40-1 (M6a) — `CLAIM 040` · `replace-within` · **change class: `MINOR` (reciprocity)**

**old (verbatim):**

```text
**Wikilinks:** [[paper_registry_current#PAPER 011]] · [[claim_registry_current#CLAIM 004]] · [[claim_registry_current#CLAIM 005]] · [[claim_registry_current#CLAIM 011]] · [[claim_registry_current#CLAIM 037]]
```

**new:**

```text
**Wikilinks:** [[paper_registry_current#PAPER 011]] · [[claim_registry_current#CLAIM 004]] · [[claim_registry_current#CLAIM 005]] · [[claim_registry_current#CLAIM 011]] · [[claim_registry_current#CLAIM 016]] · [[claim_registry_current#CLAIM 037]]
```

#### C33-1 (M8) — `CLAIM 033` · `replace-within` · **change class: `MINOR` (heading)**

**old (verbatim):**

```text
(a) **Mancata replica:**
```

**new:**

```text
(a) **Non replicata, su un test senza eventi:**
```

#### C33-2 (M8) — `CLAIM 033` · `replace-within` · **change class: `MINOR` (event count carried)**

**old (verbatim):**

```text
il confronto di mortalità fra classi genotipiche **non è significativo** (`0 (0.0) 1 (7.7) 0 (0.0) 2 2.44 0.432`), con **zero morti fra i null/null**;
```

**new:**

```text
il confronto di mortalità fra classi genotipiche **non è significativo** (`0 (0.0) 1 (7.7) 0 (0.0) 2 2.44 0.432`), con **zero morti fra i null/null**. 🔴 **Un solo decesso fra i 44 individui genotipizzati di quella Table 2** (25 null/null + 13 null/missense + 6 missense/missense): un test di Fisher costruito su **un evento** non ha potenza per riprodurre un'associazione di sopravvivenza, quindi questa è una **non-misura**, non una smentita — lo stesso principio che `BATCH_20260927_003` ha applicato a [[claim_registry_current#CLAIM 016]] come `NOT_TESTED` in entrambe le direzioni. I tre denominatori vengono dall'**anchor** del locator (entry 1 di `deepdive_manifests/PMID40875931.json`), il full text di quel paper non essendo presente in questo checkout (aggiunto 2026-09-28, `CC-20260928-MIRROR003-REPAIRS-01` M8);
```

#### C25-1 (N4) — `CLAIM 025` · `replace-within` · **change class: `MINOR` (disambiguation)**

**old (verbatim):**

```text
nella coorte ovarica — la più numerosa — il rapporto **non è significativo**
```

**new:**

```text
nella coorte ovarica (`n = 228` — **il più numeroso dei cinque strati molecolari**, di cui il maggiore fra i sottotipi mammari è Luminal A a `n = 181`, ma **più piccola** della coorte BRCA intera a `n = 390` di cui la stessa frase contrappone il modello; disambiguato 2026-09-28, `CC-20260928-MIRROR003-REPAIRS-01` N4) il rapporto **non è significativo**
```

#### C25-2 (N4, addition beyond the review) — `CLAIM 025` · `replace-within` · **change class: `MINOR` (datum added from the cited source)**

**old (verbatim):**

```text
(`HR 1.11, 95% CI 0.92–1.35, p = 0.27; concordance 0.49`)
```

**new:**

```text
(`HR 1.11, 95% CI 0.92–1.35, p = 0.27; concordance 0.49`) — e **non per difetto di eventi**: la coorte ovarica porta *«228 OV patients (161 events, 67 censored)»* contro *«390 BRCA patients (22 events, 368 censored)»*, quindi il nullo ovarico è **ricco di eventi** ed è la coorte mammaria a esserne povera
```

### 2.2 `disease-models/wwox/registries/working_model_current.md` — `batch_commit.py propagate` (record-scoped)

Three `replace-within` ops, all dry-run clean on base `a3f68b1`
(`DRY RUN … 3 op(s) on ['BLOCK 2', 'Working Model Current', 'BLOCK 3']`).

#### WM-1 (M4) — record `BLOCK 2 — claim registry mirror (baseline)` · `replace-within`

**old (verbatim):**

```text
now framed as **de-repression** (loss of a physical brake), not merely elevated abundance
```

**new:**

```text
now framed as **de-repression** (loss of a physical brake); the abundance datum is **withdrawn** — Fig. 7c is single-lane densitometry, `NOT_TESTED` in both directions (`BATCH_20260927_003`; mirror corrected 2026-09-28, `CC-20260928-MIRROR003-REPAIRS-01` M4)
```

#### WM-2 (N2, M6a) — record `Working Model Current` · `replace-within`

**old (verbatim):**

```text
Twelve claim-to-claim cross-links close the adjudicated contradiction pairs under reciprocity.
```

**new:**

```text
**23 directed** claim-to-claim cross-links close the adjudicated contradiction pairs — 14 pairs touched, 13 of them newly connected (`CLAIM 005 ↔ CLAIM 037` already carried one direction) — and reciprocity holds on **13 of the 14**: `CLAIM 016 → CLAIM 040` was left one-directional and its return edge is added by `CC-20260928-MIRROR003-REPAIRS-01` (count corrected 2026-09-28, Mirror N2/M6; the earlier figure *twelve* is supported by no measurement of the applied edges).
```

#### WM-3 (N2, M6a) — record `BLOCK 3 — flowchart logic summary` · `replace-within`

**old (verbatim):**

```text
Twelve reciprocal claim-to-claim cross-links.
```

**new:**

```text
23 directed claim-to-claim cross-links over 14 pairs, 13 newly connected, reciprocal on 13 of 14 — the `CLAIM 016 → CLAIM 040` return edge is added by `CC-20260928-MIRROR003-REPAIRS-01` (corrected 2026-09-28, Mirror N2/M6).
```

### 2.3 `disease-models/wwox/registries/paper_registry_current.md` — FULL REWRITE (`propagate` refuses this file by name, exit 4)

Records addressed: `PAPER 007`, `PAPER 117`, `CORPUS P306`, `CORPUS-STUB-059` (restored),
`PAPER 118` (new). Every byte outside these records is copied verbatim. Each `old` string below was
measured as occurring **exactly once** in the whole file.

#### P7-1 (M7) — `PAPER 007` · **change class: `MINOR` (sampling unit carried)**

**old (verbatim):**

```text
`n = 3` mice per group, unpaired t-test at `p < 0.01`:
```

**new:**

```text
`n = 3` mice per group, unpaired t-test at `p < 0.01` — 🔴 **ma l'unità del dato è la REGIONE, non l'animale**: la didascalia prosegue *«Each data point shows measurement from a single independent region from n = 3 mice/group»*, quindi il test gira su **~9 regioni da 3 animali** — **pseudoreplicazione non corretta dagli autori**; l'`n` biologico è **3** (locator entry 64, aggiunto 2026-09-28 da `CC-20260928-MIRROR003-REPAIRS-01` M7, come metà «unità di campionamento» della entry 58 il cui snippet si fermava una frase prima):
```

#### P117-1 (M9) — `PAPER 117` `Role` · **change class: `MINOR` (universal scoped)**

**old (verbatim):**

```text
**Role:** largest WOREE cohort in the model's cohort reasoning; genotype-phenotype correlation, null genotypes most severe
```

**new:**

```text
**Role:** largest **primary** WOREE case series in the corpus read here as of 2026-09-28 — **20 new cases** (`PREMISE: INFERENZA`); as *cohorts* both `PMID 40875931` (50 individuals / 45 families) and [[paper_registry_current#PAPER 018]] (75 pooled: 13 primary + 62 from the literature) are **larger**. Genotype-phenotype correlation, null genotypes most severe. Scoped 2026-09-28 by `CC-20260928-MIRROR003-REPAIRS-01` M9; the earlier unqualified *"largest WOREE cohort"* was false against two records this registry already holds
```

#### P117-2 (M9, a surface Mirror did not name) — `PAPER 117` `Genotype/model`

**old (verbatim):**

```text
biallelic WWOX variants across null and missense classes; the largest WOREE cohort in this model's cohort reasoning
```

**new:**

```text
biallelic WWOX variants across null and missense classes; the largest **primary** WOREE case series in the corpus read here as of 2026-09-28 (20 new cases; `PREMISE: INFERENZA`) — **not** the largest cohort, see `Role`
```

#### P306-1 (M9) — `CORPUS P306` `Role`

**old (verbatim):**

```text
**Role:** deep-dive — full text required; the only published assay of WWOX catalysis
```

**new:**

```text
**Role:** deep-dive — full text required; the only assay of WWOX catalysis **identified in the corpus read here as of 2026-09-28** (`PREMISE: INFERENZA`; abstract depth, no receipt, no locator). Scoped 2026-09-28 by `CC-20260928-MIRROR003-REPAIRS-01` M9
```

#### P306-2 (M9) — `CORPUS P306` `Note`

**old (verbatim):**

```text
this is the only published measurement of WWOX catalytic activity
```

**new:**

```text
this is the only measurement of WWOX catalytic activity **identified in the corpus read here as of 2026-09-28** (`PREMISE: INFERENZA` — the record is at abstract depth with `PREMISE: UNREAD_PRIMARY` and no receipt, so *"the only published"* was a claim about the literature this record cannot make)
```

#### P59-1 (N6) — `CORPUS-STUB-059` · **RESTORED** · **change class: `MINOR — STRUCTURAL` (corpus 360 → 361)**

**Decision recorded, as Mirror asked (*"Either the convention or the departure should be written
down once"*): the stub should have been preserved, and it is restored here.** The convention is not
an unwritten habit — it is declared in the stub records' own `Registry role` field
(`CORPUS-STUB-119`: *"conservato append-only come storia di audit, **mai cancellato**"*) and is what
the **adjacent** `CORPUS-STUB-058` did on exactly this event: promoted to `PAPER 026` and kept, with
`Status: superseded` and `Next action: none — upgraded to PAPER 026`. `BATCH_20260927_003`'s stated
reason — *"no record with an empty `Authors` field survives for a byline to be borrowed from
again"* — **does not select its target**: `CORPUS-STUB-059` carried no `Authors` field at all, and
neither do the 167 stubs still in the file, so the reason would have licensed 167 more deletions. The
byline hazard it named is real and is addressed where it belongs, in `PAPER 025`'s and `PAPER 117`'s
own notes, which already name it. The restored record follows `CORPUS-STUB-058`'s wording so the next
promotion does not have to re-decide.

**Insert after** the `CORPUS-STUB-058` record (currently followed directly by `## CORPUS-STUB-060`),
restoring the ordinal sequence:

```text
## CORPUS-STUB-059
**Corpus paper no:** 59
**Full title:** The phenotypic spectrum of WWOX-related disorders: 20 additional cases of WOREE syndrome and review of the literature
**Identifier:** PMID 30356099 / DOI 10.1038/s41436-018-0339-3
**Status:** superseded
**Registry role:** preserved corpus placeholder — **conservato append-only come storia di audit, mai cancellato**
**Claim links:** none
**Next action:** none — upgraded to PAPER 117
**Note:** Preserved for lossless corpus alignment. Full integrated record now lives in [[paper_registry_current#PAPER 117]] (`BATCH_20260927_003`). 🔴 **Restored 2026-09-28 by `CC-20260928-MIRROR003-REPAIRS-01` (Mirror N6):** `BATCH_20260927_003` deleted this placeholder rather than preserving it, on a reason — *"no record with an empty `Authors` field survives for a byline to be borrowed from again"* — that did not distinguish it from the 167 stubs which have no `Authors` field either. **The convention, written down once here:** a placeholder promoted to a full record is re-statused `superseded` and kept, never deleted; the audit trail from corpus ordinal to PAPER record is the whole point of the placeholder. The byline hazard is carried by `PAPER 025`'s and `PAPER 117`'s own notes instead.
```

#### P118-1 (M3) — `PAPER 118` · **NEW RECORD** · **change class: `MINOR — STRUCTURAL` (papers 107 → 108)**

**Append at the end of the file** (after `PAPER 117`, before the closing `---`). 🔴 **`Claim links`
declares `025` because a first-hand reading with a receipt and a manifest stands behind the bound** —
this is the opposite of the anti-pattern Mirror's F5 named, where an edge was declared to silence a
warning with no reading behind it. The consequence is intended and is verified in §3: the LINT `INFO
UNLINKED_SUPPORT_UNCHECKED` disappears and `trace_claim_foundation --claim "CLAIM 025"` shows the
bounding source at depth 1.

```text
## PAPER 118
**Short title:** Hammouz 2026 IJMS — WWOX/HIF1A balance across breast subtypes and ovarian carcinoma (TCGA, DFS proxy)
**Full title:** WWOX/HIF1A Balance Delineates Context-Dependent Molecular States in Breast Cancer Subtypes and Ovarian Carcinoma
**Authors:** Hammouz RY, Maciejek K, Bednarek AK
**Year:** 2026
**Source type:** primary research — retrospective bioinformatic analysis of TCGA RNA-seq and clinical data
**Journal/source:** *Int J Mol Sci* 2026;27(15):6740
**Identifier:** PMID 42589397 / PMCID PMC13467099 / DOI 10.3390/ijms27156740
**Status:** processed
**Record provenance:** created 2026-09-28 by `CC-20260928-MIRROR003-REPAIRS-01` (Mirror ex-post review of `BATCH_20260927_003`, finding M3). 🔴 **Why it did not exist:** `BATCH_20260927_003` bounded [[claim_registry_current#CLAIM 025]] on a first-hand reading of this paper and registered no record for it, so the bounding source was invisible to `trace_claim_foundation` — which showed `CLAIM 025` resting on [[paper_registry_current#PAPER 091]] alone — and LINT could only emit `[INFO] UNLINKED_SUPPORT_UNCHECKED`, the weaker screen. Metadata taken from the declared JATS artefact's own `article-meta`.
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20260927-42589397-02` (first-hand, PMC JATS XML, `files/fulltext/PMID42589397_ZZ2026_PMC_2026-09-27.xml`, sha256 `ae7f429190e0b48faaf91f9df0c79e66dd7986d23c65c21f5564ef8607f898af`); prior receipt `FTR-20260921-42589397-01` is a **verification receipt of another actor's reading** and declares tables and figures unavailable. Manifest `deepdive_manifests/PMID36779245.json` is a different paper; this one's is `deepdive_manifests/PMID42589397.json` (7 verbatim locators, 5 declared gaps). ⚠️ **Declared gap:** Supplementary Tables S4–S8 were not fetched, so the per-subtype survival directions are receipted at the level of the authors' running text only.
**Primary pathway:** P5 — HIF1A / metabolism (oncological context)
**Model/species:** human tumour datasets (TCGA breast `n = 390`, ovarian `n = 228`); no WWOX allele, no perturbation, no neural material
**Genotype/model:** none — expression-ratio analysis, not a genotype study
**Transferability:** T3
**clinical relevance:** BACKGROUND — bounds the DIRECTION of the ratio–outcome association; authorises no transfer to a non-tumoural CNS claim
**Claim links:** 025 (**bounding source, not corroborating** — same group, same dataset family, tumour only, no perturbation, so it does not raise `CLAIM 025`'s corroboration weight)
**Role:** the source that removes sign-invariance from the WWOX/HIF1A ratio–outcome association: the direction is subtype-dependent and the authors call their subtype effects *"descriptive and hypothesis-generating rather than formally validated prognostic groupings"*. Also the source of the ovarian null's event structure — 161 events in 228 against 22 in 390 — which shows that null is event-rich rather than underpowered.
**LIT link:** [[literature_tracking_log_current#LIT-0420]]
**Note:** ⚠️ **Not the same paper as `LIT-0019`** (PMID 41007296, *Biology* 2025, same group, overall survival): checked by PMID, DOI, PMCID and title. 🔴 The authors' own hedge travels with the record: the subtype directions are *"tended to show"*, and the breast bootstrap leaves optimism-corrected C-indices *"centred close to 0 with a wide interval (approximately −0.50 to 0.46)"*.
```

### 2.4 `disease-models/wwox/registries/literature_tracking_log_current.md` — `batch_commit.py propagate` (record-scoped)

One `insert-after` op, dry-run clean on base `a3f68b1` (`DRY RUN … 1 op(s) on ['LIT-0419']`).

#### LIT-1 (M3) — `insert-after` record `LIT-0419` · **change class: `MINOR — STRUCTURAL` (literature 400 → 401)**

The inserted record is `LIT-0420` and its text is the one in
`research/commit_candidates/ops/` form reproduced here in full:

```text
## LIT-0420
**Short title:** Hammouz 2026 IJMS — WWOX/HIF1A balance across BRCA subtypes and ovarian carcinoma (TCGA, DFS proxy)
**Authors:** Hammouz RY, Maciejek K, Bednarek AK
**Year:** 2026
**Source type:** primary research — retrospective bioinformatic analysis of TCGA RNA-seq and clinical data
**Journal/source:** *Int J Mol Sci* 2026;27(15):6740
**Identifier type:** PMID / DOI / PMCID
**Identifier value:** PMID 42589397 / DOI 10.3390/ijms27156740 / PMC13467099
**Date discovered:** 2026-09-21 (`FT-144`, singleton imported from `human_genotype_and_claim025_wave1b_20260921.md`)
**Date processed:** 2026-09-27 (first-hand read, `FTR-20260927-42589397-02`)
**Discovery window:** wave-1b sibling-node import, 2026-09-21
**Discovery source:** `FT-144`; the PMID had no record in this log (checked by PMID, DOI, PMCID and title — the same group's PMID 41007296 is `LIT-0019` and is a DIFFERENT paper)
**Discovery query:** `CLAIM 025` sign-invariance bound
**Status:** processed
**Status note:** `partial_fulltext_read` — receipts `FTR-20260921-42589397-01` (a verification receipt of another actor's reading, tables and figures declared unavailable) and `FTR-20260927-42589397-02` (first-hand, PMC JATS XML). 🔴 **Record created 2026-09-28 by `CC-20260928-MIRROR003-REPAIRS-01` (Mirror M3):** the reading bounded `CLAIM 025` on 2026-09-27 while no registry record named this PMID at all, so the bound was invisible to `trace_claim_foundation` and LINT could only emit `UNLINKED_SUPPORT_UNCHECKED`.
**Primary pathway:** P5 — HIF1A / metabolismo (contesto oncologico)
**Genotype/model tag:** dati umani tumorali TCGA (mammella, ovaio); nessun allele WWOX, nessun materiale neurale, nessuna perturbazione
**Transferability:** T3
**clinical relevance:** BACKGROUND — bounds `CLAIM 025` on the direction of the ratio–outcome association; authorises no CNS transfer
**Claim links:** 025 (bounding source, non-corroborating: same group, same dataset family, tumour only, no perturbation)
**Working Model impact:** none — no block is redefined; the record bounds an existing claim's direction
**Report mentions:** `CC-20260922-CLAIM025-SIGN-INVARIANCE-01` · `BATCH_20260927_003` · `CC-20260928-MIRROR003-REPAIRS-01`
**Next action:** Supplementary Tables S4–S8 unfetched — the per-subtype survival numbers are receipted at the level of the authors' running text only
**Flags:** read — partial; supplementary debt open
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20260927-42589397-02`; manifest `deepdive_manifests/PMID42589397.json` (7 verbatim locators, 5 declared gaps)
**Registry record:** [[paper_registry_current#PAPER 118]]
**Note:** Title: WWOX/HIF1A Balance Delineates Context-Dependent Molecular States in Breast Cancer Subtypes and Ovarian Carcinoma. The authors declare their subtype effects *"descriptive and hypothesis-generating rather than formally validated prognostic groupings"*.
```

### 2.5 Not proposed

- **No edge to `PAPER 059` from `CLAIM 005`'s side beyond the `wikilink_only` one**, and no change to
  `PAPER 059`'s `Claim links`. The boundary **cites** that paper (as the chain's terminus) and does
  not quote it; a `claim_links` edge would be evidential, and this candidate does not create one.
- **No `Status`, `Type`, `Transferability` or BLOCCO 1 change anywhere**, and no therapeutic file is
  touched. `therapeutic_strategies_current.md` is not in this candidate's scope at all.
- **The other nine one-directional claim→claim edges** (§6): recorded, not repaired. Each is a link
  one record chose to make in one direction and none was adjudicated by the census; closing them is a
  graph-hygiene decision for a dedicated candidate, not a repair of `BATCH_20260927_003`.
- **`CLAIM 005`'s epileptogenesis prohibition**: untouched, and no op of this candidate intersects it.
- **`deepdive_manifests/PMID40875931.json`**: no locator added. That paper's full text is in no
  checkout here, so a new verbatim locator could not be verified against a declared artefact; the
  denominators are attributed to the existing locator's anchor **in the claim text itself** (C33-2)
  rather than to a quote nobody can re-check.

---

## 3 · Simulation — **run, not predicted**: the whole candidate applied on `a3f68b1`, measured, then reverted

Every op above was applied in this worktree (`propagate --apply` for the three record-scoped files, a
scripted full rewrite for the paper registry), the checks below were **run**, and the four current
files were then restored with `git checkout --` so that this candidate remains a proposal. The
post-revert state was re-measured: LINT `WARN`/0 BLOCK and `growth_anchors` `PASS` with
`papers=107 · corpus=360 · literature=400`, i.e. byte-clean.

| check | before (measured) | after (measured) |
|---|---|---|
| `legend_lint.py .` | `WARN`, **0 BLOCK** · 10 `WARN_BUT_PROCEED` · advisories: `INFO MISSING_WIKILINK` (`CLAIM 010`) and `INFO UNLINKED_SUPPORT_UNCHECKED` (`CLAIM 025`) | `WARN`, **0 BLOCK** · 10 `WARN_BUT_PROCEED` (**identical set**) · the `CLAIM 025` `UNLINKED_SUPPORT_UNCHECKED` is **gone** and **nothing was added** — cleared by a record with a reading behind it, not by an invented edge |
| `trace_claim_foundation --claim "CLAIM 025"` | `PAPER 091` alone, 1/1 manifest-backed | `PAPER 091` **and `PAPER 118`** (`PMID 42589397`, `human`, `evidence`, `claim_links`, `locator-backed`), **2/2** manifest-backed, *"No species drift"* |
| `trace_claim_foundation --claim "CLAIM 005"` | `PAPER 006 · 057 · 058`, all `evidence`, 3/3 | the same three as `evidence`, **plus `PAPER 042` and `PAPER 059` rendered `reference only (wikilink_only)`**; 🔴 **`SPECIES DRIFT` unchanged** — still the single pre-existing `PAPER 058` (rat) finding, because the drift test reads `EVIDENTIAL_EDGES` only, so rat `PAPER 059` and multi-species `PAPER 042` add none. Coverage 3/3 → **5/5**, still 100%. One informational line appears, `SPECIES_MULTIPLE: PAPER 042`, which is a *loss* note about that record's own field and not a finding against `CLAIM 005` |
| `test_trace_claim_foundation.py` | OK, 20/20 | **OK, 20/20** |
| `test_scientific_consistency.py` | OK, 8/8 | **OK, 8/8** |
| `test_support_linkage.py` | OK, 23/23 | **OK, 23/23** |
| `test_canonical_structure.py` | OK, 4/4 | **3/4 — one expected failure**, `test_cardinality_matches_the_declared_growth_anchor`, whose message *is* the three structural deltas below. It is cleared by the `growth_anchors.py record` the propagating batch owes and by nothing else; the other three tests pass, including `test_record_identifiers_are_unique` (so the restored `CORPUS-STUB-059` and the new `PAPER 118` / `LIT-0420` collide with nothing) |
| `growth_anchors.py check` | `PASS` — claims 41 · papers 107 · corpus 360 · literature 400 · registry_only 10 · unread_premises 0 · backlog 27 | `BLOCK` with exactly three `STRUCTURAL_DRIFT` lines and nothing else: **papers 107 → 108**, **corpus 360 → 361**, **literature 400 → 401**. `claims` stays 41, `registry_only` stays 10, and 🔴 **`unread_premises` stays 0** — the zero-headroom ratchet is not touched, because `PAPER 118` carries a receipt and a restored placeholder is not a premise. Backlog 27 → **28** (this candidate), which is the expected effect of adding one |
| `public_release_gate.py` | `PASS`, **0 BLOCKS** | **`PASS`, 0 BLOCKS** — no PMID-shaped or address-shaped literal in the new records trips it |
| `fulltext_receipts.py verify` | `OK`, 258 chained, tail anchored | untouched — **no receipt is recorded by this candidate** |

**Owed by the propagating batch:** `growth_anchors.py record --batch <ID> --papers +1 --corpus +1
--literature +1`, then Phase 4.7 (`coverage_report`, `batch_queue`, `pathograph`, `reading_state`,
the DisMech sidecar). One Phase-4.7 prediction, stated so it can be checked: the DisMech
`sealed_scope` entries seal `CLAIM 016 · 024 · 035` and `PAPER 019 · 055 · 056`, and **no op above
touches any of those six records** — `CLAIM 016`'s op edits its `Impact on Working Model` line, which
*is* inside a sealed block, so the **claim-registry** scope hash **will** move and the baseline needs
a re-seal naming `CLAIM 016`; the **paper-registry** scope hash should **not** move at all.

---

## 4 · LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

### 4.1 · B1 — `CLAIM 030`, the two-tailed observation

1. Patient 2 of PMID 36779245 Table 1 is homozygous for the same `Q230P` allele as Patient 5 | *"c.689A > C, p.Gln230Pro (homozygous)"* | `files/fulltext/PMID36779245_Oliver2023_PMC_2026-09-27.xml` — Table 1, row *"WWOX (NM_016373.3) variant(s) (hg19)"*, Patient 2 column; the identical string stands in the Patient 5 column
2. Both patients are classed by the paper itself as the same genotype class | *"Missense/missense"* | same artefact — Table 1, row *"Genetic combination"*, Patient 2 and Patient 5 columns
3. Patient 2 is 23 years 11 months and living; Patient 5 died at 8 years 3 months | *"23 y 11 m, M"* … *"8 y 3 m (dec.), F"* | same artefact — Table 1, row *"Age, sex"*, Patient 2 and Patient 5 columns; 23 y 11 m is the maximum of that row
4. On the severity axis the two patients are concordant, not opposite | *"Profound"* … *"Nonverbal"* … *"No"* | same artefact — Table 1, rows *"Intellectual disability"*, *"Speech"* and *"Walking/ambulant"*, Patient 2 and Patient 5 columns (each row prints the same value for both)
5. The single non-drug-resistant patient of the cohort is Patient 5 | *"Epilepsy was resistant to antiseizure medications (ASMs) in all patients, except Patient 5."* | same artefact — Results, antiseizure-medication paragraph (pre-existing locator, `deepdive_manifests/PMID36779245.json` entry 26)

### 4.2 · M7 — `PAPER 007`, the Olig2 sampling unit

6. The Olig2⁺ test's data points are regions, three per animal from three animals, so the test is run on ~9 regions and the biological n is 3 | *"Each data point shows measurement from a single independent region from n = 3 mice/group. Scale bar= 100 μm, data is represented as mean ± SEM, *p-value < 0.01, unpaired Student's t-test."* | `files/fulltext/PMID36828035_Hussain2023_PMC.xml` — Figure 4 caption, panel (e), the two sentences immediately after *"…counted in three independent 500 μm2 regions spanning the entire imaged corpus callosum."* (new locator, `deepdive_manifests/PMID36828035.json` entry 64)

### 4.3 · N4 / C25-2 — `CLAIM 025`, the ovarian cohort

7. The ovarian cohort is n = 228 with 161 events and the breast cohort n = 390 with 22 events, so the non-significant ovarian association is event-rich and the breast one event-poor | *"resulting in final DFS-proxy cohorts of 390 BRCA patients (22 events, 368 censored) and 228 OV patients (161 events, 67 censored)"* | `files/fulltext/PMID42589397_ZZ2026_PMC_2026-09-27.xml` — Methods 5.1, cohort-assembly sentence, citing Supplementary Tables S1 and S2 (new locator, `deepdive_manifests/PMID42589397.json` entry 6)
8. Luminal A, the largest breast subtype stratum, is n = 181 and therefore smaller than the ovarian 228 | *"Subtype-specific analyses were strictly constrained by very low DFS event counts (for example, Luminal A: n = 181)."* | same artefact — Results 2.6.2, *Subtype-Specific Analyses*, opening sentence (new locator, entry 5)
9. The study analyses exactly two cohorts and five strata | *"A total of 618 patients were included and categorized into distinct molecular groups (Basal-like, Luminal A, Luminal B, HER2-enriched, and OV)"* | same artefact — Results 2.1, *Patient Stratification and Subtype Composition*, opening sentence

### 4.4 · M9 — `PAPER 117`'s and `CORPUS P306`'s superlatives

10. `PAPER 117` is a 20-case primary series with a literature review, not the largest cohort in this registry | *"The phenotypic spectrum of WWOX-related disorders: 20 additional cases of WOREE syndrome and review of the literature"* | `paper_registry_current.md` `PAPER 117` `Full title`, itself verified at PubMed by `BATCH_20260927_003` (PMID 30356099, *Genet Med* 2019;21(6):1308-1318) — a registry-internal triple, declared as such

---

## 5 · Applied outside this candidate by the same package (non-canonical, 2026-09-28)

- **(a)** Mirror review persisted verbatim with a one-line provenance header:
  `session_evaluations/2026-09-27_BATCH_20260927_003_mirror_review.md` (243 body lines, byte-identical
  to the reviewer's scratchpad output — diffed).
- **(b) N1** — dated correction note appended to
  `session_evaluations/2026-09-27_BATCH_20260927_003.md`: the re-seal absorbed **two** batches' drift,
  not one. Re-derived with the protocol's own `registry_scope_bytes`: `PAPER 019`'s block digest moved
  `19cbaa26… → a3bf24f1…` at `7718c41` (`BATCH_20260920_001`) and `→ 14fcd6c2…` at `c99dfe5`
  (`BATCH_20260927_001`), while the baseline's declared paper-registry scope was still the pre-`7718c41`
  value `86869835ba…` and the re-seal moved it to `867ca36187…`. The disclosure's *"last moved in
  BATCH_20260927_001"* is true; *"this re-seal absorbs it"* understates the span by one batch.
- **(c) N2 second half, N3, M2's second surface** — one dated note appended at the head of
  `framework/state/state_history.md` § 7 (the state-control carve-out: § 4 is never edited, § 7 is
  where dated notes go). It records three corrections to `batch_20260927_003_scope`: the quotation
  count is `38 of 38` on the batch report against `39 of 39` here; *"fixes the factor at 1000"* is
  **×100**; and *"the human and mouse datasets that had already falsified the rat-only sentence"*
  names three **mouse** records only (`PAPER 019`, `PAPER 011`, `PAPER 007`) — the human limb was
  handled by scoping the sentence to *"`Wwox` rodent models"*, which is a different repair from the
  one that line describes.
- **(d) M6a's disposition wording, N2's first half** — dated correction note appended to
  `CC-20260826-CROSS-CLAIM-CENSUS-02.md`: the applied edges are **23 directed over 14 pairs**, not
  twelve, and *"closed under reciprocity"* fails on exactly one of its own adjudicated pairs,
  `016 ↔ 040`. The nine pre-existing one-directional edges of the whole graph are listed there as a
  measurement, with §6's adjudication.
- **(e) M3's disposition** — dated correction note appended to
  `CC-20260922-CLAIM025-SIGN-INVARIANCE-01.md`, **re-disposing it `PROPAGATED IN PART`**: the claim
  was bounded on a reading whose source the candidate never proposed to register, and the registry
  record it owed is `PAPER 118` / `LIT-0420` above.
- **(f) M7's locator** — `deepdive_manifests/PMID36828035.json` entry **64** added (the Fig. 4 caption's
  sampling-unit and test sentences); `deepdive_manifest.py --pmid 36828035 --verify-artifacts
  --require-current-schema` → **PASS, 0 gaps**.
- **(g) N4's locators** — `deepdive_manifests/PMID42589397.json` entries **5–6** added (Luminal A
  `n = 181`; the Methods 5.1 cohort-and-event sentence); verifier **PASS** with the manifest's five
  pre-existing declared gaps and one pre-existing WARN on entry 0 that is not this package's.
- **(h) Refused and withdrawn** — a third locator was written for PMID 42589397 quoting the Abstract's
  *"BRCA (n = 390) and OV (n = 228)"* and the verifier **refused it**: *"quote occurs in the abstract
  but not the non-abstract body"*. It was **withdrawn, not reclassified** — the same refusal
  `CC-20260927-MIRROR002-REPAIRS-01` met on its N1. Nothing proposed above rests on it; the body
  sentence in (g) carries both figures.
- **(i) M10 and N5 — HANDED TO HARNESS ENGINEERING, no tool edited.** The resealer was rewritten by
  Harness Engineering at `9ae0f58` (`main` `21d1156`) after `BATCH_20260927_003`, so this package
  measured it and wrote the hand-off rather than touching it. **M10 is open and the label is not
  monotone today:** the current baseline reads `rev.14` while three earlier seals are labelled
  `rev.15`, `rev.16` and `rev.17`; the full label history, re-derived commit by commit, is
  `rev.7 → 12 → 7 → 12 → 7 → 8 → 9 → 15 → 16 → 16 → 17 → 13 → 14`, and `--revision` is still free
  text validated by nothing (`parser.add_argument("--revision", help=…)`, then
  `baseline["revision"] = arguments.revision`). `rev.17`'s substantive note — *"extractor strips
  trailing block separators; per-block digests added"* — is recoverable only from git. **N5 is already
  closed:** `9ae0f58` moved the length check ahead of the digest and gave truncation its own message
  (*"the ledger was truncated, which is an incident, not a re-seal"*).

---

## 6 · CONTESTED — M6b, and the reciprocity census that adjudicates it

**Mirror M6 second sentence: *"`CLAIM 040 → CLAIM 004` was likewise left unreciprocated."* Contested
as a finding against `BATCH_20260927_003`.** The graph fact is true; the attribution is not.

Reciprocity recomputed over the whole 41-claim `Wikilinks` graph — **11 one-directional edges**:

| edge | created by `BATCH_20260927_003`? |
|---|---|
| `CLAIM 016 → CLAIM 040` | ✅ **yes** — `CC-20260826-CROSS-CLAIM-CENSUS-02` `OP-4`. **This is M6a and it is repaired above** |
| `CLAIM 040 → CLAIM 004` | ❌ no — pre-existing; `OP-1` added `011 · 005 · 037` to `CLAIM 004`, never `040`, and `004 ↔ 040` is not in the census's adjudicated pair set |
| `CLAIM 030 → 032` · `032 → 031` · `033 → 019` · `033 → 030` · `034 → 028` · `035 → 028` · `035 → 030` · `036 → 005` · `041 → 007` | ❌ no — all nine pre-existing and untouched by that batch |

So of the **14 pairs** the census's own ops touched, **13 are closed under reciprocity and one is
not**, and that one is `016 ↔ 040`. The census's disposition sentence is wrong about one pair, not
two. **Consequence for the repair:** the `040 → 016` return edge is added (C40-1) because the batch
created that asymmetry and claimed to have closed it; the other ten are **recorded and not touched**,
because each is a link some record chose to make one-directionally, none was adjudicated, and adding
a back-link is an adjacency judgement — the census's own rule is *"Nothing ambiguous is linked"*. A
dedicated candidate should decide them as a set; treating `040 → 004` differently from the other nine
only because a reviewer named it would be the arbitrary act.

**What would change my mind:** if the census's *"closed under reciprocity"* were defined over the
adjudicated **pairs** rather than the applied **edges**, M6a would also soften to a NOTE — but it
would not vanish, because `016 ↔ 040` is in the pair set either way.

---

## WAVE-2 READINESS (2026-09-28)

**Actor:** ACTOR_ID `scientist`, package `m003` · **Verdict: `READY_MINOR`** (whole candidate).
**`context_policy` declared: `QUESTION_DRIVEN`** (questions and held records in the header).

**What was done (not noted — done):**
- **Every Mirror finding re-verified first-hand before any op was written.** Twelve confirmed, one
  (M6b) contested with the graph census that settles it, one (N5) found already repaired by Harness
  Engineering, and **three items promoted from the dispatch's non-canonical route to this candidate**
  because measurement showed they sit in the four current files (§1.1).
- **Three findings extended beyond the review, each on evidence:** B1 gains the severity-axis
  concordance from Table 1 (the pair differs on survival **only**), M9 gains `PAPER 117`'s second
  superlative in `Genotype/model`, N4 gains the event counts that show the ovarian null is event-rich.
- **Two counts in the review corrected against the source:** `CLAIM 005` carries **three** verbatim
  quotes of PMID 24369382, not four, and `PAPER 059` is cited rather than quoted; the M6 asymmetry is
  **one** adjudicated pair, not two.
- **Three verbatim locators added and verified; one refused and withdrawn** (§5 f–h). Every quotation
  introduced into a current file by this candidate is backed by a locator in a verified manifest, with
  one declared exception stated in place: M8's three denominators come from an existing locator's
  **anchor**, the paper being in no checkout here.
- **Every `old` string measured at this head:** 9 claim-registry ops, 3 working-model ops and 1
  literature-log op dry-run clean under `batch_commit.py propagate`; the 5 paper-registry
  substitutions each occur **exactly once** in the whole file (`grep -cF` = 1 for all five).
- **No receipt recorded.** Nothing here is a new reading of a source: the two receipts that matter
  already exist, were re-read, and their artefacts were re-hashed equal.

**Change class: `MINOR`**, with the two non-wording items declared: **B1 withdraws an inference** in a
`T1`/VERY HIGH claim (locator triples in §4.1 for that reason, as the discipline requires of a
`consolidated baseline`-adjacent reversal even though `CLAIM 030` is `in observation` and its `Status`
does not move), and **M3 + N6 are structural** (papers 107 → 108, corpus 360 → 361, literature
400 → 401, so `growth_anchors.py record` is owed by the propagating batch).

**Operation list:** §2.1 (9 × `replace-within`, `claim_registry_current.md`) · §2.2 (3 ×
`replace-within`, `working_model_current.md`) · §2.3 (paper registry **full rewrite**: 5 substitutions,
1 record restored, 1 record appended) · §2.4 (1 × `insert-after`, `literature_tracking_log_current.md`)
· then `growth_anchors.py record` and Phase 4.7.

**Pending, owned elsewhere:** M10 (Harness Engineering — a monotonicity check and a
`revision_ordinal` field on `reseal_dismech_baseline.py`, plus restoring `rev.17`'s note from git);
the ten remaining one-directional claim→claim edges (§6 — a dedicated graph-hygiene candidate); the
Supplementary S4–S8 debt of `PAPER 118`.

---

## BATCH DISPOSITION — `BATCH_20260928_001` (2026-09-28, ACTOR_ID `scientist`), append-only

**Nothing above this line was rewritten.** **Status: `PROPAGATED`** — all 19 operations applied.

`BATCH_20260928_001`: MINOR, MANUAL, `WM_v7.0` → **`WM_v7.1`**, under the operator's standing
authorisation of 2026-09-27 given in writing, verbatim: ***«procedi tu, ti autorizzo su tutto»***.
Propagated jointly with `CC-20260928-MIRROR004-REPAIRS-01`; the two candidates collide on **no
record**, and the one file-level and one record-level co-edit are named in the batch report.

| op | record | verdict |
|---|---|---|
| `C30-1` (B1) | `CLAIM 030` | **PROPAGATED** — and the classification was re-adjudicated, not accepted. See below |
| `C38-1` (M2) | `CLAIM 038` | PROPAGATED |
| `C16-1` (M4) | `CLAIM 016` | PROPAGATED — its sealed block drifted as predicted and is absorbed by name in `rev.18` |
| `C5-1` (M5) | `CLAIM 005` | PROPAGATED — the two edges render `reference only (wikilink_only)` and the species-drift finding is unchanged, both measured |
| `C40-1` (M6a) | `CLAIM 040` | PROPAGATED |
| `C33-1`, `C33-2` (M8) | `CLAIM 033` | PROPAGATED |
| `C25-1`, `C25-2` (N4) | `CLAIM 025` | PROPAGATED |
| `WM-1` (M4) | WM `BLOCK 2` | PROPAGATED |
| `WM-2` (N2, M6a) | WM `Working Model Current` | PROPAGATED — co-edited with `MIRROR004`'s `WM-1` in the same record, on a different sentence |
| `WM-3` (N2, M6a) | WM `BLOCK 3` | PROPAGATED. ⚠️ **Locator correction:** the sentence is in the `WM_v6.1` **changelog row**, not in the flowchart-logic prose the section heading names. The record id is right and the op is well formed; the description is not |
| `P7-1` (M7) | `PAPER 007` | PROPAGATED |
| `P117-1`, `P117-2` (M9) | `PAPER 117` | PROPAGATED |
| `P306-1`, `P306-2` (M9) | `CORPUS P306` | PROPAGATED |
| `P59-1` (N6) | `CORPUS-STUB-059` | PROPAGATED — restored between `CORPUS-STUB-058` and `CORPUS-STUB-060`, ordinal sequence closed |
| `P118-1` (M3) | `PAPER 118` | PROPAGATED — `Claim links: 025` allowed to stand only after the receipt and the manifest were verified first-hand (below) |
| `LIT-1` (M3) | `LIT-0420` | PROPAGATED — inserted after `LIT-0419` |

**B1's classification, adjudicated by the verifier on its own reading and not carried over.**
`MINOR — INFERENCE WITHDRAWN` **stands**, and the batch's grounds are its own. Table 1 of PMID
36779245 was re-read off the JATS XML (`780f42de9b3982fa5bf9bf1e6bb76f71384c943aa197fb2d4de80be7ac7e7a34`, re-hashed **equal**) **with the column
alignment checked cell by cell before any value was read across**: the variant, genetic-combination
and country rows carry 12 data cells for 13 patients because one `colspan="2"` cell covers the
sibling pair at **columns 9–10** — *after* both patients of interest — so the columns line up and
patients 2 and 5 are read correctly. Both carry `c.689A > C, p.Gln230Pro (homozygous)` and
`Missense/missense`; both are `Profound` / `Nonverbal` / `Walking: No`; the ages are `23 y 11 m, M`
and `8 y 3 m (dec.), F`. The concordance the candidate added beyond the review is **confirmed** and
the discordance is survival only. It is **not** a baseline reversal: `CLAIM 030` is `in observation`,
its `Status`, `Type` and `Transferability` do not move, no datum changes, and the claim's thesis —
severity tracks residual function — is untouched. What is withdrawn is a **corroboration**, and
withdrawing a corroboration from a non-baseline claim is a MINOR change under §7.

**`PAPER 118`'s `Claim links: 025` — the condition was checked, not assumed.** The receipt
`FTR-20260927-42589397-02` is in the ledger as a `contemporaneous_receipt`, `partial_fulltext_read`,
with `source_fingerprint` equal to the sha256 of the artefact re-hashed on disk here, and
`deepdive_manifests/PMID42589397.json` holds 7 `verbatim_locators.entries`. A first-hand reading with
a receipt and a manifest stands behind the field, so it was propagated and the advisory is cleared by
evidence rather than by declaration.

**§6's contest is carried as a contest.** M6b is **not resolved** by this batch: the graph fact
stands, the attribution to `BATCH_20260927_003` does not, and the ten remaining one-directional
claim→claim edges are recorded and untouched, for a dedicated graph-hygiene candidate.

**One prediction of §3 was wrong, and it was wrong only because of the merge.** §3 predicted the
paper-registry `sealed_scope` hash would **not** move. Measured: it moved, because
`CC-20260928-MIRROR004-REPAIRS-01` edits `PAPER 056`, which is a sealed block and which this
candidate could not see. Both drifted blocks are named with `--absorb` in `rev.18`.

**Owed and discharged:** `growth_anchors.py record --batch BATCH_20260928_001 --papers +1 --corpus +1
--literature +1`, measured against the files after propagation and not taken from this candidate —
papers 107 → **108**, corpus 360 → **361**, literature 400 → **401**, `claims` 41, `registry_only`
10 and `unread_premises` 0 all unchanged. `growth_anchors check` → **PASS**;
`test_canonical_structure.py` → **4/4 OK**.

**Residue, still open:** M10 (Harness Engineering — the revision-label monotonicity check; this batch
chose `rev.18` so as not to make it worse, and said why in the seal itself); the ten one-directional
claim→claim edges of §6; `PAPER 118`'s Supplementary S4–S8 debt.
