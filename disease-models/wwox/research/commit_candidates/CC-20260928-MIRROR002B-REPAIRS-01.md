# COMMIT CANDIDATE — CC-20260928-MIRROR002B-REPAIRS-01

**Candidate ID:** CC-20260928-MIRROR002B-REPAIRS-01
**Status:** `PROPOSED — NOT PROPAGATED`
**Base head:** `e3f4201` — `main` merged into `task/mirror002b-repairs` after Harness Engineering landed `ee94838`; dispatched against `cf40b73`, re-measured against the merge. ⚠️ **The op list grew by two after the merge** (`P118-2` widened, `LIT-1` added): see § 2.2 and § 2.3.
**Author:** ACTOR_ID `scientist`, package `mirror002b`, dispatched by the Orchestrator under the
operator's standing authorisation of 2026-09-28 (*"improve whatever is improvable, including choices the
operator authorised earlier in a sub-optimal form"*; *"procedi sempre"*).
**Source of the task:** the MIRROR ex-post review of `BATCH_20260928_002`, persisted verbatim at
[`session_evaluations/2026-09-28_BATCH_20260928_002_mirror_review.md`](../session_evaluations/2026-09-28_BATCH_20260928_002_mirror_review.md)
(verdict **CONFIRMED WITH FINDINGS**: **0 BLOCKING-SCIENTIFIC**, 6 MINOR (F1–F4, F8, F9), 3 NOTE
(F5–F7); the review also **retracts three of its own earlier findings** in its `WHERE I WAS WRONG`
section, and one of those retractions is what makes FINDING 2 possible).
This candidate carries **only the items that need one of the four scientific current files or
`disease_model.md`**: **FINDING 1** (canonical half), **FINDING 2**, **FINDING 3**, **FINDING 4**, and
the canonical residue of **FINDING 7** (none — see § 4.2). It **also discharges `REP-26`** of
[`research/record_repair_queue_current.md`](../record_repair_queue_current.md), which Harness
Engineering opened at `ee94838` after `manifest_receipt_repoint.py` repaired
`deepdive_manifests/PMID42589397.json`'s `receipt` field and left two canonical records saying, in the
present tense, that it *«still names»* the old value — the same two records (`PAPER 118`, `LIT-0420`)
this candidate already opens, so the clauses are folded into **one op list per record** rather than
racing two candidates on the same lines. FINDINGS 5 and 6 are NOTEs applied outside
any batch as append-only correction notes; FINDING 8 is the stub
[`CC-20260928-GRAPH-HYGIENE-01.md`](CC-20260928-GRAPH-HYGIENE-01.md); FINDING 9 is a Harness
Engineering hand-off and is deliberately **not** written here (§ 6). Everything applied outside this
candidate is listed in § 5. Three of the reviewer's statements did **not** survive re-measurement and
are recorded CONTESTED in § 4 with their evidence rather than repaired as stated.
**Declared change class: `MINOR`.** Every item is a wording repair, a ground replacement or a bounded
measurement replacing a false universal. 🔴 **No claim `Status`, `Type`, `Transferability`, `clinical
relevance`, BLOCCO 1 field or therapeutic `SCORE`/`SAFETY` value moves; no datum changes; no claim,
paper or literature record is added or removed; `CLAIM 005` is not touched; no DisMech-sealed block
(`CLAIM 016 / 024 / 035`, `PAPER 019 / 055 / 056`) is touched.** Two items (`C30-1`, `C30-2`, and their
echoes `WM-2` and `DM-1`) change what a claim paragraph asserts — one drops a universal, one opens a
boundary the previous text had closed — so **locator triples are supplied in § 3**.
**Per-item change class:** `P118-1` MINOR (stale status) · `P118-2` MINOR (ground) · `C2-1` MINOR
(ground) · `PR-1` MINOR (ground) · `C30-1` **MINOR — narrowing** (a universal is withdrawn and replaced
by a bounded measurement; the claim's conclusion is unchanged and its stated support is *strengthened*,
because it now rests on the allele-level premise alone) · `C30-2` **MINOR — narrowing** (an enumeration
is corrected upward and a previously-asserted inertness becomes a declared open boundary) · `WM-1`,
`WM-2`, `WM-3` MINOR (§ 7.2 in-place corrections of historical rows; superseded wording quoted inside
each row) · `DM-1` MINOR (narrative view, tracks `C30-1`).
**Receipts read, none written:** `FTR-20260928-42589397-03`, `FTR-20260927-42589397-02` and
`FTR-20260921-42589397-01` (PMID 42589397, the whole three-event lineage, read with
`fulltext_receipts.py status --pmid` to settle FINDING 1) · the ledger verified as a chain:
`fulltext_receipts.py verify` → `OK: 259 chained receipt(s), tail anchored`. 🔴 **No
`fulltext_receipts.py record` was run by this package.** The PMID 36779245 artefact was re-read this
session and it **read the Methods, which the prior receipt `FTR-20260927-36779245-05` declares
`not_read`** — so the reading widens coverage and the owed event is a **new `partial_fulltext_read`**,
`FTR-20260928-36779245-06`, not a `receipt_correction`. It is prepared as JSON under the session
scratchpad's `receipts_pending/` and is **not** appended — see § 5(e), which records why the first
classification of this event was wrong.
**Artefact re-hashed this session:** `files/fulltext/PMID36779245_Oliver2023_PMC_2026-09-27.xml` =
`780f42de9b3982fa5bf9bf1e6bb76f71384c943aa197fb2d4de80be7ac7e7a34` (**equal** to the fingerprint
`PAPER 018`'s lineage carries). Read in the **root checkout**, which is where the gitignored full texts
live; this worktree has no `files/`.
**Manifests read, none edited:** `deepdive_manifests/PMID42589397.json` and
`deepdive_manifests/PMID42397075.json`, both through `manifest_receipt_provenance.py` rather than by
hand.
**`context_policy`: `QUESTION_DRIVEN`** — declared. Held before any source was opened: the Mirror
review of `BATCH_20260928_002` **in full, including `WHERE I WAS WRONG` and all seven
`WHAT_WOULD_CHANGE_MY_MIND` conditions**; `CLAIM 002` and `CLAIM 030`, `PAPER 001` and `PAPER 118`, and
`LIT-0420` read **by record** with `registry_records.py get`, never by grep or `cat` over the two large
registries; `working_model_current.md` lines 5–7 and its `## Changelog` row for `WM_v7.2`;
`disease_model.md`'s `WM v7.0 → v7.1` paragraph; the batch report
`session_evaluations/2026-09-28_BATCH_20260928_002.md` and the candidate
`CC-20260928-MIRROR0928-REPAIRS-01`; `framework/protocols/fulltext_read_receipt.md` ll. 355–380 (the
🟢 CLOSED block) and `prompt_batch_commit.md` § 4.0 and § 7.2;
`analysis/data/pathograph_export.jsonl` and `analysis/data/dismech_phase2_baseline.json`.
Questions fixed **before** any source was reopened: *(1) is `FTR-20260928-42589397-03` in the ledger,
and is it the event the previous candidate §5(d) prepared; (2) when exactly did the manifest-`receipt`
OPEN close, relative to the propagation commit; (3) how many of Table 1's twelve examination axes have
zero variance across the 13 patients, and how many discriminate; (4) does the artefact settle what `ES
(gene panel)` means; (5) how many claim→claim edges are one-directional, under which counting rule; (6)
what does `growth_anchors check` report at HEAD.*

---

## 1 · Verification of each Mirror item, first-hand

**A reviewer's output is not gospel — including a reviewer that has just retracted three of its own
findings.** Every statement below was re-measured against the source, the tool or the current file
before it was accepted. Each `old` string was measured as occurring **exactly once in its whole file**
and **exactly once inside its own record**, and the whole eleven-op list was **simulated** (§ 2.6).

| # | Mirror severity | verdict here | what was measured |
|---|---|---|---|
| **F1** | MINOR | ✅ **CONFIRMED** (established by the Orchestrator; re-verified, not re-litigated) | `FTR-20260928-42589397-03` is in `registries/fulltext_read_receipts.jsonl`, appended at `082ed19` (committer date 2026-09-28 05:52:41 +0000, `event_at 2026-09-28T05:49:52Z`) — **`BATCH_20260928_002`'s own base commit**, 44 minutes before its propagation commit `c5eec22` (06:36:42 +0000). `fulltext_receipts.py verify` → `OK: 259 chained receipt(s), tail anchored`: the count the batch quoted **already contained** the event. |
| **F2** | MINOR | ✅ **CONFIRMED, and the conclusion it grounds gets STRONGER** | `9b8378e` (2026-09-28 07:01:12 +0000, **25 minutes after** the batch's last commit) closed the OPEN: `fulltext_read_receipt.md` now reads 🟢 *«CLOSED 2026-09-28 — a manifest's `receipt` names the reading that PRODUCED the manifest: the EARLIEST ledger event for the same study whose `outputs` name that manifest file»*. `manifest_receipt_provenance.py` at HEAD: 116 manifests, 17 non-conforming, **`PMID42397075.json` is not among them** (0 mentions in the whole report), while `PMID42589397.json` is `UNNAMED — declared FTR-20260921-42589397-01, should be FTR-20260927-42589397-02`. So the pointer `CLAIM 002` / `PAPER 001` annotate is **the** correct value, not one of two admissible ones — and the stated ground is false in two canonical records. |
| **F3** | MINOR | ✅ **CONFIRMED and reproduced to the character** | All **12** examination axes re-parsed from the JATS `table-wrap` (label `TABLE 1`, caption *"Genetic and neurological examination features."*, **22 rows**; `Examination` block rows carry 14 cells = label + 13 patients, no `colspan`). My independent count reproduces the reviewer's table cell for cell — see § 3.1. **Three** axes have zero variance, not two, and the third (`Axial hypotonia` 13/13) had never been named. |
| **F4** | MINOR | ⚠️ **CONFIRMED on the enumeration · CONTESTED on "not equally screened" — Mirror's own falsifier does NOT resolve, and neither does the artefact** | The enumeration is short by one: `Genetic studies` is a **fourth** differing row of the same `Genetics` block (patient 2 `ES`, patient 5 `ES (gene panel)`, measured). But Mirror's falsifier asked whether `ES (gene panel)` means a full exome *reported* through a panel filter, and said the Methods would settle it. **I fetched the Methods and they do not settle it** — see § 4.1. The repair therefore writes the boundary as **unresolved**, not as unequal screening. |
| **F5** | NOTE | ✅ **CONFIRMED — Mirror is right and the batch was wrong** | `PAPER 118` runs 595 115 → 598 521 = `len(text)`; `LIT-0420` runs 518 196 → 521 108 = `len(text)`; **no heading follows either**. Span-to-EOF **is** the record for the last record at its level. Applied outside this candidate as an append-only correction (§ 5(b)) — **no canonical text is owed**. |
| **F6** | NOTE | ✅ **CONFIRMED — the tension is with a help line** | The shipped resealer parses the ordinal **once, at the write**, stores it as an integer, and *«ordering is never read off the spelling»*; the help line reads as if it were inferred at read time. Applied outside this candidate (§ 5(b)) — no canonical text. |
| **F7** | NOTE | ✅ **CONFIRMED · nothing canonical** | `growth_anchors.py check` at HEAD: **14** candidates, all `CC-*`, verdict **PASS**, plus the declared pre-existing `CHECK_ERROR`. The `30` and its causal attribution live only in the batch report's DEFAULTS_TAKEN; grepped for across the four current files and `disease_model.md` — **absent**. Corrected by erratum (§ 5(a) E4). |
| **F8** | MINOR | ✅ **CONFIRMED · nothing canonical** | 15 asymmetric edges re-derived **twice**, once from the export and once from the registry itself; the stub is written (§ 5(c)). |
| **F9** | MINOR | ✅ **CONFIRMED · Harness surface** | Re-read `prompt_batch_commit.md` § Phase 5 and the batch's own commit order: the propagation `c5eec22` precedes the phase that fires ABORT, so `git checkout -- <path>` restores post-batch bytes. Hand-off, § 6. |

### 1.1 · Mirror's own `WHAT_WOULD_CHANGE_MY_MIND` conditions, checked before each finding was accepted

| # | the condition | holds? | consequence |
|---|---|---|---|
| **1** | *F1 dissolves if the ledger `-03` is a **different** event from the one §5(d) prepared — a different `prior_receipt`, or a correction of something other than the 5 → 7 locator count* | ✅ **holds (it is the same event)** | Read with `fulltext_receipts.py status --pmid 42589397`: `prior_receipt: FTR-20260927-42589397-02` · `reread_reason: receipt_correction` · `record_kind: contemporaneous_receipt` · unchanged `source_fingerprint ae7f429190e0b48faaf91f9df0c79e66dd7986d23c65c21f5564ef8607f898af` · `evidence_basis` naming the same two appended manifest entries (6 = `Results 2.6.2`, 7 = `Methods 5.1`) and the same 5 → 7 correction, and even carrying §5(d)'s own closing sentence *«NOT RECORDED BY ITS AUTHOR — prepared for the Orchestrator to append»*. It is the prepared event, recorded. **F1 stands.** |
| **2** | *F2 dissolves if `9b8378e` landed **before** `c5eec22` in wall-clock terms, making the OPEN-based ground correct as of the write* | ✅ **holds (it landed after)** | Committer dates on this host, read with `git log --format='%ci'`: `082ed19` 05:52:41 · `c5eec22` 06:36:42 · `9b8378e` **07:01:12**, all +0000 on 2026-09-28. The ground was true when written and false 25 minutes later. **F2 stands as a repair, not as a NOTE about merge order** — and note the asymmetry the reviewer draws correctly: F2's *conclusion* strengthens while its *ground* fails. |
| **3** | *F3 dissolves if any normative file defines gravità/severity as exactly {intellectual disability, speech, ambulation}* | ✅ **holds (no definition exists)** | Searched: `framework/instruction/*.md`, `framework/master/*.md`, `framework/protocols/*.md` and `working_model_current.md` carry the token `gravit` **zero** times; `claim_registry_current.md` carries it five times and **none is a definition** (`CLAIM 030` twice in the paragraph at issue, once in its `Summary`, plus `CLAIM 033`). `CLAIM 030` says so itself. **F3 stands**, and the repair names the claim's own axes with their measured variance instead of presupposing a category. |
| **4** | *F4 dissolves if `ES (gene panel)` means a full exome **reported** through a panel filter with the remaining calls retained and reviewed — the paper's Methods, read to a receipt, would settle it; the reviewer did not fetch them* | ❌ **DOES NOT RESOLVE — and this is a finding against F4's second limb** | I fetched the Methods. § 2.3 *Genetic variants* says, in full on this point: *«Pathogenic variants in WWOX were identified by local clinical and research genetic pipelines that included a combination of high-throughput sequencing (exome/genome/gene panel) and chromosomal microarray for CNV detection.»* It declares a **combination across heterogeneous local pipelines** and specifies **nothing per patient**; the abbreviation key defines `ES` as *exome sequencing*, so `ES (gene panel)` is exome-based sequencing reported through a panel, but whether the out-of-panel calls were **retained and reviewed** is nowhere stated. The falsifier is therefore neither satisfied nor refuted. **F4's first limb (the enumeration) stands; its second limb (*«the two patients were not equally screened»*) is CONTESTED and the repair writes the boundary as open** — § 4.1. |
| **5** | *F8 dissolves if a graph-hygiene candidate, or a dated owned hand-off for the fifteen edges, already exists somewhere the reviewer did not look* | ✅ **holds (neither exists)** | 154 files in `research/commit_candidates/` at `cf40b73`, listed: the only graph-named one is `CC-20260825-GRAPH-MATERIALIZATION-01`, which materialised the graph and closes no edge; the three 2026-08-26 `CROSS-CLAIM-CENSUS` files count links without owning them. `growth_anchors check` backlog: 14, none a graph candidate. **F8 stands**, and its second limb is now satisfied because the stub was written (§ 5(c)). |
| **6** | *ITEM 3's PASS reverses if the reviewer's own level-2 splitter mis-partitions the paper registry* | ⚪ **not re-tested — and deliberately** | ITEM 3 is a PASS on a completed batch, not a finding, and re-deriving a third independent splitter would change nothing this candidate writes. Recorded as untested rather than silently inherited. |
| **7** | *ITEM 4's PASS reverses if `scope_sha256` is computed over something wider than the named `scope_blocks`* | ⚪ **not re-tested** | Same reason. What I did verify, because this candidate must not break it: `inputs.claim_registry.scope_blocks = ["CLAIM 016","CLAIM 024","CLAIM 035"]` and `inputs.paper_registry.scope_blocks = ["PAPER 019","PAPER 055","PAPER 056"]`, and **none of those six records is touched by any op below** — so whatever the digest's width, this candidate cannot drift it through a sealed block. |

---

## 2 · PROPOSED_DELTA — exact operation lists

Every `old` is **verbatim from the current file at `cf40b73`** and was measured as occurring exactly
once in the file and once in its record (§ 2.6). **Eleven ops over five files.**

### 2.1 `disease-models/wwox/registries/claim_registry_current.md` — `batch_commit.py propagate` (record-scoped)

**`C2-1` · `CLAIM 002` · `replace-within` · MINOR (ground replacement, conclusion unchanged) · FINDING 2**

- `old` (unique in file, unique in record):
  > `` `framework/protocols/fulltext_read_receipt.md` lascia **deliberatamente aperto** quale delle due un campo `receipt` designi e dichiara che *nessuna delle due è un difetto referenziale*, quindi chi segue il link trova l'altro dei due bersagli ammessi e non una catena rotta (annotato 2026-09-28, `CC-20260928-MIRROR0928-REPAIRS-01`, Mirror FINDING 10, contestato in parte) ``
- `new`:
  > 🟢 **deciso 2026-09-28** (`framework/protocols/fulltext_read_receipt.md`, CLOSED): un campo `receipt` nomina la lettura che **ha prodotto** il manifest — il **primo** evento di ledger, per lo stesso studio, i cui `outputs` nominino quel file — quindi `-03` non è soltanto *ammissibile*, è **il** valore corretto, e `manifest_receipt_provenance.py` non elenca `PMID42397075.json` fra i manifest non conformi. Il link è integro: la conclusione di questa nota ne esce **più forte**, non più debole (fondamento riscritto 2026-09-28 da `CC-20260928-MIRROR002B-REPAIRS-01`, Mirror FINDING 2 su `BATCH_20260928_002`, al posto di *«lascia deliberatamente aperto quale delle due un campo `receipt` designi e dichiara che nessuna delle due è un difetto referenziale»*: quell'OPEN è stato chiuso 25 minuti dopo l'ultimo commit del batch che lo citava come fondamento)

**`C30-1` · `CLAIM 030` · `replace-within` · MINOR — NARROWING · FINDING 3 · triples § 3.1**

🔴 **This is the third round on one defect class, and the instruction from the review is explicit: do
not narrow the universal a fourth time — drop the form.** The replacement contains no universal.

- `old` (unique in file, unique in record):
  > La concordanza della coppia non è dunque una somiglianza misurata fra questi due pazienti: è l'**assenza, in questa tabella, di un asse di gravità che discrimini** — il che rende la lettura **neutra** indipendente da quale coppia si scelga fra gli **11** pazienti concordanti anche sul linguaggio.
- `new`:
  > 🔴 **Corretto 2026-09-28 (`CC-20260928-MIRROR002B-REPAIRS-01`, revisione ex-post Mirror di `BATCH_20260928_002`, FINDING 3): l'universale precedente — *«l'assenza, in questa tabella, di un asse di gravità che discrimini»* — era falso, terzo di una serie in cui ogni giro restringeva l'universale invece di abbandonarne la forma; qui la forma è abbandonata e sostituita da una misura delimitata.** Ri-misurati dal markup JATS tutti e **12** gli assi del blocco `Examination` della Table 1 (13 pazienti per asse): **tre hanno varianza nulla** — `Intellectual disability` 13/13 `Profound`, `Walking/ambulant` 13/13 `No` e `Axial hypotonia` 13/13 `Yes`, quest'ultimo **mai nominato in nessun giro precedente** — e `Speech` ha varianza minima, `Nonverbal` 11/13. Su questi assi la concordanza è vera **per costruzione** e non porta informazione. ⚠️ **Ma la tabella stampa anche assi che discriminano fra i 13 pazienti**: `Movement disorder` ha **6 valori distinti** (modale 5/13), `Short stature` 7/13, `Scoliosis` 9/13, `Acquired microcephaly` e `Spasticity/limb hypertonia` 10/13, `Facial dysmorphisms`, `Feeding tube` e `Ophthalmologic features` 11/13 — e su due di essi (`Short stature`, `Ophthalmologic features`) la coppia stessa **differisce**, come questa stessa nota dice due frasi sopra. Un universale del tipo *«nessun asse di gravità discrimina»* era dunque autocontraddittorio, e sopravviveva solo sulla stipulazione `gravità = {disabilità intellettiva, linguaggio, deambulazione}` che il capoverso stesso disconosce. 🔴 **La neutralità della coppia non dipende da questa misura e non ne ha mai avuto bisogno: segue dalla sola premessa a livello di allele** — due omozigoti per lo stesso allele hanno, per la regola di questo claim, la stessa funzione residua, e non possono quindi discriminare una regola enunciata sugli alleli. Questo è l'argomento che porta la conclusione; la misura dei 12 assi lo accompagna e non lo sostituisce.

**`C30-2` · `CLAIM 030` · `replace-within` · MINOR — NARROWING · FINDING 4 · triples § 3.2**

- `old` (unique in file, unique in record):
  > oltre a tre righe di contesto (`Country`, `Family history for epilepsy`, `Consanguineous`)
- `new`:
  > oltre a **quattro** righe del blocco `Genetics` — `Country`, `Family history for epilepsy`, `Consanguineous` e `Genetic studies` (🔴 **enumerazione corretta 2026-09-28, `CC-20260928-MIRROR002B-REPAIRS-01`, Mirror FINDING 4, da *«tre righe di contesto»***: la quarta riga era stata omessa e liquidata come riga di metodo). ⚠️ **`Genetic studies` non è inerte, e il suo confine resta APERTO:** il paziente 2 ha `ES`, il paziente 5 `ES (gene panel)`, e la tabella definisce `ES` come *exome sequencing*, quindi la riga descrive un accertamento **riportato attraverso un filtro a pannello**. 🔴 **Se i due accertamenti siano equivalenti NON è decidibile su questo artefatto** e non va asserito: il § 2.3 dei Metodi dichiara soltanto *«Pathogenic variants in WWOX were identified by local clinical and research genetic pipelines that included a combination of high-throughput sequencing (exome/genome/gene panel) and chromosomal microarray for CNV detection»* — nessuna specifica per paziente, e nessuna affermazione che le chiamate fuori pannello siano state conservate e riviste. **Registrato come confine, non aggiudicato:** se il pannello fosse un filtro su un esoma con il resto conservato, i due accertamenti sarebbero equivalenti e la riga sarebbe davvero inerte; se fosse un pannello virtuale chiuso, i due pazienti **non** sarebbero stati screenati allo stesso modo, e un'asimmetria di screening tocca direttamente la **prima** delle spiegazioni rivali elencate qui sotto, i loci modificatori. In nessuno dei due casi la conclusione di questa nota si inverte — il ramo aperto la **sostiene**, perché lascia aperte le rivali invece di chiuderne una. `REVIVAL_TRIGGER`: qualunque lettura, a ricevuta, dei Supplementary Methods o della corrispondenza di PMID 36779245 che dichiari cosa il laboratorio del paziente 5 abbia conservato fuori pannello

**Post-condition for this file:** 197 111 → **200 994** characters; 41 `## CLAIM` blocks before and
after, same key set and same order; exactly **two** blocks differ, `CLAIM 002` and `CLAIM 030`; the
preamble byte-identical; `CLAIM 005`, `CLAIM 016`, `CLAIM 024` and `CLAIM 035` byte-identical.

### 2.2 `disease-models/wwox/registries/paper_registry_current.md` — **FULL REWRITE**, unchanged blocks copied verbatim

🔴 `batch_commit.py propagate` **refuses this file by name (exit 4)** — `prompt_batch_commit.md` § 4.0.
The propagating batch therefore rewrites the file whole and must verify the post-condition below, at
**block level and not by line offsets**, which is the stronger check the previous Mirror review
recommended.

**`PR-1` · `PAPER 001` · `replace-within` (inside the full rewrite) · MINOR (ground) · FINDING 2**

- `old` (unique in file, unique in record):
  > `` `framework/protocols/fulltext_read_receipt.md` leaves the target of a manifest's `receipt` field deliberately open — the producing reading, or the most recent one — and states that **neither is a referential defect**, so the hop is traversable and is not a broken link (annotated 2026-09-28, `CC-20260928-MIRROR0928-REPAIRS-01`, Mirror FINDING 10, contested in part) ``
- `new`:
  > 🟢 **decided 2026-09-28** (`framework/protocols/fulltext_read_receipt.md`, CLOSED): a manifest's `receipt` names the reading that **produced** the manifest — the **earliest** ledger event for the same study whose `outputs` name that file — so `-03` is not merely *one admissible* target but **the** correct value, and `manifest_receipt_provenance.py` does not list `PMID42397075.json` among its non-conforming manifests. The hop is intact and this conclusion is **stronger**, not weaker (ground rewritten 2026-09-28 by `CC-20260928-MIRROR002B-REPAIRS-01`, Mirror FINDING 2 on `BATCH_20260928_002`, replacing *«leaves the target of a manifest's `receipt` field deliberately open — the producing reading, or the most recent one — and states that neither is a referential defect»*: that OPEN was closed 25 minutes after the last commit of the batch that rested on it)

**`P118-1` · `PAPER 118` · `replace-within` · MINOR (a canonical record asserted an unrecorded event that was recorded before the batch began) · FINDING 1**

- `old` (unique in file, unique in record):
  > a `receipt_correction` event on that lineage is **owed for the count** and is prepared for the Orchestrator to append
- `new`:
  > the `receipt_correction` for that count is **recorded**: `FTR-20260928-42589397-03` (`prior_receipt: FTR-20260927-42589397-02`, `reread_reason: receipt_correction`, `event_at 2026-09-28T05:49:52Z`), appended by the Orchestrator at commit `082ed19` — which is `BATCH_20260928_002`'s own base commit, 44 minutes before that batch's propagation commit `c5eec22`, so the correction was already in the ledger before the batch that called it *owed* began (corrected 2026-09-28 by `CC-20260928-MIRROR002B-REPAIRS-01`, Mirror FINDING 1 on `BATCH_20260928_002`, replacing *«a `receipt_correction` event on that lineage is owed for the count and is prepared for the Orchestrator to append»*)

**`P118-2` · `PAPER 118` · `replace-within` · MINOR (ground; the conclusion is unchanged and hardens from "wrong under both open targets" to "a defect under the decided rule") · FINDING 2**

🔴 **This op is larger than Mirror scoped it, because the defect grew while this candidate was being
written.** Mirror's FINDING 2 asked only that the *stale protocol OPEN* be replaced as the clause's
ground. On 2026-09-28 Harness Engineering then landed `ee94838`, which built
`framework/scripts/manifest_receipt_repoint.py` **and used it**: the manifest's `receipt` field was
repaired from `FTR-20260921-42589397-01` to `FTR-20260927-42589397-02`, derived from the ledger.
So the clause's *present tense* — *«still names `FTR-20260921-42589397-01`»* — is now **false on disk**,
and `REP-26` of [`research/record_repair_queue_current.md`](../record_repair_queue_current.md) was
opened for exactly this. Harness correctly did not touch the record: a canonical sentence moves only
through `BATCH_COMMIT`. **One op list per record beats two candidates racing on the same lines**, so
this op covers the whole sentence and **discharges `REP-26`**.

- `old` (unique in file, unique in record):
  > The manifest's own `receipt` field still names `FTR-20260921-42589397-01`, which is **neither** the reading that produced the manifest **nor** the most recent reading of this paper — the two targets `framework/protocols/fulltext_read_receipt.md` deliberately leaves open for that field — so it is wrong under **both** and is routed to whoever owns manifest re-pointing; the manifest is not hand-edited.
- `new`:
  > The manifest's `receipt` field carried `FTR-20260921-42589397-01` until 2026-09-28 and now names **`FTR-20260927-42589397-02`**, the reading that produced it. 🟢 **Repaired 2026-09-28 by `framework/scripts/manifest_receipt_repoint.py`**, which derives the value from the ledger rather than from any report, under the semantics `framework/protocols/fulltext_read_receipt.md` decided the same day (CLOSED: *«a manifest's `receipt` names the reading that PRODUCED the manifest: the EARLIEST ledger event for the same study whose `outputs` name that manifest file»*); `manifest_receipt_provenance.py --pmid 42589397` now reports **CONFORMS**. 🔴 **The old value was wrong on two independent grounds, and the second is the checkable one:** `-01` names this manifest in no `outputs` at all (`UNNAMED`), *and* its `source_fingerprint` is `572a7e6b14b8d10ec993c901dd367b2163437077f5b6fb429e874a5fc43e6e16` — a **different document** from the `ae7f429190e0b48faaf91f9df0c79e66dd7986d23c65c21f5564ef8607f898af` this manifest declares in `source_artifacts` and against which every locator in it verifies, which `-02` fingerprints exactly. The repair therefore tightened the artefact binding `require_work_manifest` enforces, not only the pointer semantics. ⚠️ The manifest was **not** hand-edited: it was rewritten by a sanctioned instrument, and its bytes are pinned — `pathograph_export.jsonl`'s derivation manifest carries an **aggregate** sha256 over its whole 119-file input set, deep-dive manifests included, so the one-byte change made the pathograph STALE and it was regenerated in the same landing. (Present tense corrected 2026-09-28 by `CC-20260928-MIRROR002B-REPAIRS-01`, discharging **`REP-26`** of `research/record_repair_queue_current.md` and applying Mirror FINDING 2 on `BATCH_20260928_002`, from *«still names `FTR-20260921-42589397-01` … the two targets `fulltext_read_receipt.md` deliberately leaves open for that field … routed to whoever owns manifest re-pointing»*.)

**Verified first-hand before this op was written, not taken from the hand-off:** the manifest on disk
carries `"receipt": "FTR-20260927-42589397-02"`; its `source_artifacts[0].sha256` is
`ae7f429190e0b48faaf91f9df0c79e66dd7986d23c65c21f5564ef8607f898af`; the ledger's `-01` carries
`source_fingerprint 572a7e6b14b8d10ec993c901dd367b2163437077f5b6fb429e874a5fc43e6e16` and `-02` carries
`ae7f4291…f898af`; `manifest_receipt_provenance.py --pmid 42589397` → `1 manifest(s) · CONFORMS 1`.

**Post-condition for this file (the full-rewrite guard):** 601 712 → **604 349** characters; **482**
level-2 blocks before and after, **same key set and same order**; **480 byte-identical**; the only two
whose bytes differ are `PAPER 001` and `PAPER 118`; **the preamble byte-identical**; 108 `PAPER`
records before and after; `PAPER 019 / 055 / 056` byte-identical.

### 2.3 `disease-models/wwox/registries/literature_tracking_log_current.md` — `batch_commit.py propagate` (record-scoped)

⚠️ **This file entered scope after the candidate was drafted, and for a different reason than Mirror
gave.** Mirror's FINDING 2 locator says the stale *«deliberately open»* framing *«appears in `PAPER
118` / `LIT-0420`»*; measured, **it does not appear in `LIT-0420`** (§ 4.3, CONTESTED). What `LIT-0420`
does carry is the same **present-tense** statement about the manifest field that `ee94838` falsified,
so the record is in scope under `REP-26` and not under Mirror's locator. One op.

**`LIT-1` · `LIT-0420` · `replace-within` · MINOR (present tense of a repaired field) · `REP-26`**

- `old` (unique in file, unique in record):
  > its `receipt` field still names `FTR-20260921-42589397-01` and is routed for re-pointing
- `new`:
  > its `receipt` field carried `FTR-20260921-42589397-01` and now names **`FTR-20260927-42589397-02`**, the reading that produced it — 🟢 repaired 2026-09-28 by `framework/scripts/manifest_receipt_repoint.py`, which derives the value from the ledger; `manifest_receipt_provenance.py --pmid 42589397` reports **CONFORMS**. The old value named this manifest in no `outputs` and fingerprinted a different document from the artefact the manifest declares, so the repair tightened the artefact binding as well as the pointer (present tense corrected 2026-09-28 by `CC-20260928-MIRROR002B-REPAIRS-01`, discharging `REP-26`, from *«still names `FTR-20260921-42589397-01` and is routed for re-pointing»*)

**Post-condition for this file:** 521 670 → **522 275** characters; **423** level-2 blocks before and
after, same key set and same order; exactly **one** block differs, `LIT-0420`; 401 `LIT-` records before
and after; preamble byte-identical.

🔴 **`REP-26`'s own VERIFY condition is what the propagating batch must run:** `grep -n "still names"
disease-models/wwox/registries/*.md` returns no row for PMID 42589397, and
`manifest_receipt_provenance.py --pmid 42589397` reports `CONFORMS`. When both hold, the batch moves
`REP-26` to `CLOSED` in `research/record_repair_queue_current.md` with that verification named — a
non-canonical surface, so it is closed outside the batch's canonical op list. ⚠️ **The receipt ledger's
own account of the field** (`FTR-20260928-42589397-03`, *«NOT CORRECTED HERE, AND DELIBERATELY»*) is
append-only history, describes the state at its own event time, is **correct as written** and is **not
touched** — `REP-26` says so explicitly and this candidate obeys it.

### 2.4 `disease-models/wwox/registries/working_model_current.md` — `batch_commit.py propagate` (record-scoped)

🔴 **All three ops are § 7.2 in-place corrections of a historical record of a completed act**, and each
carries the three things § 7.2 requires **inside the row it corrects**: the correcting candidate, the
date, and the superseded wording verbatim. None of them overwrites a row's stated **conclusion** — what
each replaces is a statement of fact about a source or a protocol that has since been measured false,
which is the class § 7.2 permits (*"a count, a date, an identifier, a typo, a wrong figure"*). Nothing
is re-dated: the `frozen`/`released` dates, the version labels and the batch ids do not move.

⚠️ **Declared, because § 7.2 says it is a real cost and it is accepted on one condition:** each
corrected row now carries a **forward reference** to a candidate that did not exist when the version it
documents was released. The condition is that the superseded wording travels inside the row, and it
does, in all three. The batch's own Phase-4.6 row for the new version **also** names the `WM_v7.2` row
it supersedes, so a reader has both routes.

**`WM-1` · line 7, the `BATCH_20260928_002` `Last update` line · `replace-within` · MINOR · FINDING 2**

- `old` (unique in file):
  > `` `CLAIM 002` and `PAPER 001` annotate which of the two targets `framework/protocols/fulltext_read_receipt.md` leaves open a manifest's `receipt` field names, the hop being traversable and **not** a broken chain ``
- `new`:
  > `CLAIM 002` and `PAPER 001` annotate which reading a manifest's `receipt` field names, the hop being traversable and **not** a broken chain [corrected 2026-09-28 from *«which of the two targets `framework/protocols/fulltext_read_receipt.md` leaves open a manifest's `receipt` field names»* by `CC-20260928-MIRROR002B-REPAIRS-01`, Mirror FINDING 2 on `BATCH_20260928_002`: that protocol OPEN was closed at 2026-09-28T07:01 — 25 minutes after this batch's last commit — on the reading that **produced** the manifest, under which the annotated pointer is not merely admissible but correct]

**`WM-2` · the `WM_v7.2` `## Changelog` row · `replace-within` · MINOR · FINDING 3**

- `old` (unique in file):
  > so the concordance is the absence of a discriminating axis in that table and the reviewer's own *«all 13, zero variance»* is false on `Speech`
- `new`:
  > so the concordance is uninformative on the axes this claim names and the reviewer's own *«all 13, zero variance»* is false on `Speech` [corrected 2026-09-28 from *«so the concordance is the absence of a discriminating axis in that table»* by `CC-20260928-MIRROR002B-REPAIRS-01`, Mirror FINDING 3 on `BATCH_20260928_002`: all 12 examination axes were re-measured and the table **does** print discriminating axes — `Movement disorder` 6 distinct values, `Short stature` 7/13, `Scoliosis` 9/13, microcephaly and spasticity 10/13 — while exactly three have zero variance, intellectual disability, ambulation and **axial hypotonia**, all 13/13; the pair's neutrality follows from the allele-level premise alone and never needed the universal]

**`WM-3` · the `WM_v7.2` `## Changelog` row · `replace-within` · MINOR · FINDING 2**

- `old` (unique in file):
  > `` `CLAIM 002` / `PAPER 001` annotate the manifest `receipt` field as pointing at the **producing** reading, one of the two targets the receipt protocol leaves open, so the hop is traversable and the finding of a *broken chain* is contested ``
- `new`:
  > `CLAIM 002` / `PAPER 001` annotate the manifest `receipt` field as pointing at the **producing** reading, so the hop is traversable and the finding of a *broken chain* is contested [corrected 2026-09-28 from *«one of the two targets the receipt protocol leaves open»* by `CC-20260928-MIRROR002B-REPAIRS-01`, Mirror FINDING 2 on `BATCH_20260928_002`: the protocol closed that OPEN on the producing reading at 2026-09-28T07:01, so the annotated pointer is **the** correct value rather than one of two admissible ones — the conclusion is strengthened, not withdrawn]

**Post-condition for this file:** 101 156 → **102 454** characters *before* Phase 4.6's own three
additions (version line, prepended `Last update`, new top changelog row), which the batch adds on top
and must account for separately — the arithmetic error the previous batch's report made and reported
against itself. 🔴 **`BLOCK 1`, `BLOCK 2` and `BLOCK 3`'s scientific body must be byte-identical
afterwards**: all three ops land in the version header and the `## Changelog`, and none is anchored by
`id: "BLOCK 3"` — whose span runs 49 194 → 96 155 = EOF and covers six `##` headings including the
whole changelog, which is exactly why no op here uses it.

### 2.5 `disease-models/wwox/disease_model.md` — narrative view, edited with the batch

**`DM-1` · the `WM v7.0 → v7.1` paragraph · `replace-within` · MINOR — NARROWING · FINDING 3 · triples § 3.1**

- `old` (unique in file):
  > so the concordance is the **absence of a discriminating axis in that table** rather than a measured similarity between these two patients — which is what makes the neutral reading independent of which pair is picked
- `new`:
  > so the concordance on those axes is **uninformative by construction** rather than a measured similarity between these two patients. *(Re-scoped 2026-09-28, `CC-20260928-MIRROR002B-REPAIRS-01`, Mirror FINDING 3: the previous wording — «the absence of a discriminating axis in that table» — was the third narrowing of one false universal, and all 12 examination axes measured off the source markup falsify it. Three axes have zero variance across the 13 patients — intellectual disability, ambulation and **axial hypotonia**, 13/13 each — but the table also prints axes that do discriminate: movement disorder takes six distinct values, short stature splits 7/6, scoliosis 9/13, microcephaly and spasticity 10/13, and on two of them the pair itself differs. The neutral reading does not rest on any of this: it follows from the allele-level premise alone, which is the argument named in the next sentence.)*

**Post-condition:** 23 132 → **23 822** characters; one paragraph touched; the `Not medical advice`
closing intact.

🔴 **`disease_model.md` is a canonical disease-model file by the state manifest's own § 3.1 table and
is now inside the Phase-3 `SNAPSHOT_DECLARATION` (added at `a510aa7`, crediting `BATCH_20260928_002`).**
The propagating batch snapshots it with the rest and **does not** hand-copy it.

### 2.6 Simulation — run, not predicted

The eleven ops were applied in order to in-memory copies of the five files, by exact string
replacement, with `count(old) == 1` asserted per op **and** per record. All eleven applied. Measured,
not forecast, at merge base `e3f4201` (`main` after `ee94838`):

| file | before | after | Δ |
|---|---|---|---|
| `claim_registry_current.md` | 197 111 | **200 994** | +3 883 |
| `paper_registry_current.md` | 601 712 | **604 349** | +2 637 |
| `literature_tracking_log_current.md` | 521 670 | **522 275** | +605 |
| `working_model_current.md` | 101 156 | **102 454** | +1 298 (excl. Phase 4.6) |
| `disease_model.md` | 23 132 | **23 822** | +690 |

⚠️ **The five "before" figures are exactly the five the Mirror review measured after
`BATCH_20260928_002`** (197 111 / 601 712 / 521 670 / 101 156 / 23 132), from an independent partition
— and they are unchanged by `ee94838`, which touched no current file. That agreement is a cross-check
on the base, not a prediction about the result. Per-op deltas:
`P118-1` +564 · `P118-2` +1 576 · `LIT-1` +605 · `C2-1` +484 · `PR-1` +497 · `C30-1` +1 643 ·
`C30-2` +1 756 · `WM-1` +377 · `WM-2` +595 · `WM-3` +326 · `DM-1` +690.
**A predicted number that happens to be right is still not a measurement**: the batch re-measures all
five after propagation and reports what it measured.

**Cardinality must not move:** `claims=41 · papers=108 · corpus=361 · literature=401 |
registry_only=10 | unread_premises=0`. Not one op adds, removes or re-segments a record.

---

## 3 · LOCATOR TRIPLES FOR BLIND AUDIT

Two ops change what a claim paragraph asserts. The triples below are **(proposition, verbatim quote,
anchor)** for a blind auditor holding only the source artefact — never this candidate, never the
conclusions. **Source for all triples:** `files/fulltext/PMID36779245_Oliver2023_PMC_2026-09-27.xml`,
sha256 `780f42de9b3982fa5bf9bf1e6bb76f71384c943aa197fb2d4de80be7ac7e7a34` (re-hashed **equal** this
session in the root checkout). The table is the **first** of three `table-wrap` elements, `label`
`TABLE 1`, caption *"Genetic and neurological examination features."*, **22 `tr` rows**. Alignment was
verified **before any value was read across a row**: the `Examination` rows (11–22) carry **14** cells
with no `colspan`, so label + 13 patients align trivially; the `Genetics` rows (4–9) carry **13** cells
because one bears `colspan="2"`, and that cell is the **9th data cell**, covering patients **9–10**,
i.e. *after* both patients of interest.

### 3.1 · FINDING 3 — the twelve examination axes, cohort variance (supports `C30-1`, `WM-2`, `DM-1`)

| # | proposition | verbatim quote (the row's 13 patient values, in column order) | anchor |
|---|---|---|---|
| T1 | `Intellectual disability` has **zero variance**: one distinct value in 13 of 13 patients | `Profound` ×13 | Table 1, `Examination` block, row 11 of 22 |
| T2 | `Walking/ambulant` has **zero variance**: one distinct value in 13 of 13 | `No` ×13 | Table 1, row 13 of 22 |
| T3 | **`Axial hypotonia` has zero variance: one distinct value in 13 of 13** — a third invariant axis, named in no previous round | `Yes` ×13 | Table 1, row 20 of 22 |
| T4 | `Speech` has **three** distinct values, modal 11 of 13 — minimal but **non-zero** variance | `Nonverbal`, `Nonverbal`, `Nonverbal`, `Nonverbal`, `Nonverbal`, `Single word "Dad"`, `Nonverbal`, `Nonverbal`, `Nonverbal`, `Single word "Mama"`, `Nonverbal`, `Nonverbal`, `Nonverbal` | Table 1, row 12 of 22 |
| T5 | `Movement disorder` takes **six** distinct values, modal 5 of 13 — it discriminates strongly across the cohort | `Dystonic–dyskinetic movements`, `Dystonia`, `Dystonia`, `Dystonic–dyskinetic movements`, `Dystonia`, `Bradykinetic movement disorder`, `Bradykinetic movement disorder; parkinsonism`, `Dystonia`, `No`, `No`, `Dystonic–dyskinetic movements`, `Hyperekplexia`, `Dystonia` | Table 1, row 21 of 22 |
| T6 | `Short stature` splits **7/6** across the cohort, and patient 2 differs from patient 5 | `Yes`, **`No`**, `Yes`, `Yes`, **`Yes`**, `No`, `No`, `Yes`, `No`, `No`, `Yes`, `No`, `Yes` | Table 1, row 16 of 22 (footnote a: *"Short stature defined as height = 3 SD below the mean for age"*) |
| T7 | `Scoliosis` is modal 9 of 13 — it discriminates | `Yes`, `Yes`, `Yes`, `Yes`, `Yes`, `Yes`, `Yes`, `Yes`, `No`, `No`, `No`, `No`, `Yes` | Table 1, row 17 of 22 |
| T8 | `Acquired microcephaly` is modal 10 of 13 — it discriminates | `Yes`, `Yes`, `Yes`, `Yes`, `Yes`, `Yes`, `Yes`, `Yes`, `No`, `No`, `Yes`, `No`, `Yes` | Table 1, row 15 of 22 |
| T9 | `Spasticity/limb hypertonia` is modal 10 of 13 — it discriminates | `Yes`, `Yes`, `Yes`, `Yes`, `Yes`, `Yes`, `Yes`, `Yes`, `No`, `No`, `No`, `Yes`, `Yes` | Table 1, row 19 of 22 |
| T10 | `Ophthalmologic features` has three distinct values, modal 11 of 13, **and patient 2 differs from patient 5** — so the same sentence that denied a discriminating severity axis cited one | `Poor eye contact`, **`Absent eye contact; erratic ocular movements`**, `Poor eye contact`, `Poor eye contact`, **`Poor eye contact`**, `Poor eye contact`, `Poor eye contact`, `Absent eye contact`, `Poor eye contact`, `Poor eye contact`, `Poor eye contact`, `Poor eye contact`, `Poor eye contact` | Table 1, row 22 of 22 |
| T11 | `Facial dysmorphisms` and `Feeding tube` are each modal 11 of 13 with two distinct values | `Yes` ×7, `NA`, `Yes` ×4, `NA` — and `Yes`, `Yes`, `Yes`, `Yes`, `Yes`, `Yes`, `Yes`, `Yes`, `No`, `Yes`, `Yes`, `No`, `Yes` | Table 1, rows 14 and 18 of 22 |
| T12 | The `Examination` block contains exactly **twelve** axes, and rows 11–22 are all of them | rows 11–22 inclusive, the block opening at the single-cell `colspan="14"` header `Examination` (row 10) | Table 1, rows 10–22 of 22 |

**What the auditor is being asked:** for each triple, (i) does the quote support the proposition, and
(ii) does the source say **more** or **less** than the proposition claims. 🔴 **The proposition the
triples must NOT be read as supporting is the withdrawn one** — *«the table prints no discriminating
severity axis»*. T5–T10 falsify it, and the replacement text says so.

### 3.2 · FINDING 4 — the `Genetic studies` row and the boundary it leaves open (supports `C30-2`)

| # | proposition | verbatim quote | anchor |
|---|---|---|---|
| T13 | `Genetic studies` is a row of the `Genetics` block and patients 2 and 5 carry **different** values | row values in column order: `GS`, **`ES`**, `ES/MLPA`, `ES`, **`ES (gene panel)`**, `ES, CMA`, `ES, CMA`, `CMA`, `CMA, ES`, `ES (gene panel)`, `ES (gene panel)/CMA`, `ES` (12 cells + label: the 9th data cell bears `colspan="2"` and covers patients 9–10, after both patients of interest) | Table 1, `Genetics` block, row 9 of 22 |
| T14 | The table's own key defines `ES` as exome sequencing, so `ES (gene panel)` denotes exome sequencing qualified by a panel | *"Abbreviations: CMA, chromosomal microarray; dec., deceased; **ES, exome sequencing**; F, female; FDIU, fetal death in utero; GS, genome sequencing; … MLPA, multiplex‐ligation dependent probe amplification; NA, not available"* | Table 1 footnote, abbreviation key |
| T15 | 🔴 **The Methods do NOT state whether the panel was a filter on a retained exome, per patient or at all** — the equivalence of the two patients' screens is **not decidable** from this artefact | *"Pathogenic variants in WWOX were identified by local clinical and research genetic pipelines that included a combination of high‐throughput sequencing (exome/genome/gene panel) and chromosomal microarray for CNV detection. Parental segregation was performed to confirm that genetic variants were in trans."* | Methods § 2.3, *Genetic variants*, first two sentences |
| T16 | The paper's own Discussion treats panel breadth as a **real** limit on what a screen can see, which is why T15's gap matters rather than being pedantry | *"Importantly, sequencing technologies are also evolving to better detect CNVs; multiexon gene panels and a move toward genome (over exome) sequencing will further enable the dual detection and interpretation of single nucleotide variants and CNVs."* | Discussion, paragraph on CNV detection (the sentence following the *"lack of probe coverage"* argument) |

🔴 **The auditor should test one thing above all: whether T15 says LESS than the proposition it
carries.** The proposition is a **negative** — *the artefact does not settle it* — and a negative is the
easiest thing to over-claim. If a reader can find, anywhere in this artefact, a statement of what
patient 5's laboratory retained outside its panel, T15 fails and `C30-2`'s open branch must be replaced
by the resolved reading.

---

## 4 · CONTESTED — what did not survive as stated

### 4.1 · FINDING 4's second limb — *«the two patients were not equally screened»* is NOT established

**Mirror's statement:** *"Patient 2 is `ES`; patient 5 is `ES (gene panel)`. The two patients were
**not equally screened** — a virtual-panel analysis cannot see a variant outside the panel."*

**Mirror's own falsifier, which the review declared and did not test:** the finding dissolves if
`ES (gene panel)` means a full exome *reported* through a panel filter with the remaining calls
retained and reviewed.

🔴 **I fetched the Methods, which Mirror said would settle it, and they do not.** § 2.3 declares
*«local clinical and research genetic pipelines that included a combination of high-throughput
sequencing (exome/genome/gene panel) and chromosomal microarray»* — a **combination across
heterogeneous sites**, with **no per-patient specification** and **no statement about out-of-panel
calls**. The abbreviation key defines `ES` as exome sequencing, so the row does report an exome-based
assay qualified by a panel; that is all the artefact licenses. Neither branch is supported:

- *If* the panel was a reporting filter on a retained exome → the screens are equivalent and the row is
  genuinely inert, and Mirror's ground fails.
- *If* it was a closed virtual panel → the screens differ and Mirror's ground holds.

**The repair therefore writes the boundary as unresolved, and says which reading would settle it.** This
is the discipline the repair series exists to enforce: the previous rounds' error was asserting a
universal a source did not license, and asserting *«not equally screened»* on this artefact would repeat
it in the opposite direction. **What survives of FINDING 4 without any new reading:** the enumeration
*was* short by one, `Genetic studies` *does* differ between the two patients, and the row is *not* a
methods footnote when the paragraph's own first-listed rival explanation is modifier loci. Those are
written; the causal claim is not. `REVIVAL_TRIGGER` is carried in the `new` text.

### 4.2 · FINDING 7 — confirmed, and it leaves **nothing** canonical

Mirror says *«Repair: none owed»* and that is right, but it was worth checking rather than inheriting.
Measured: the token `30`-item backlog and the phrase *«known blind spot»* in that sense appear in
`session_evaluations/2026-09-28_BATCH_20260928_002.md` line 255 and in the `BATCH_20260928_001` Mirror
review, and **nowhere in the four current files or `disease_model.md`**. `growth_anchors.py check` at
HEAD reports **14** candidates (all `CC-*`), verdict **PASS**, with one declared pre-existing
`[CHECK_ERROR] UNREADABLE_DISPOSITION` on `CC-20260922-CLAIM025-SIGN-INVARIANCE-01`. The batch's causal
attribution — that its own candidate's absence from the list was *«the known blind spot in that
counter»* — is withdrawn as unverified in the report's erratum (§ 5(a) E4): the counter closes a
candidate on its own disposition record, which is what `78ce3bf` wrote, so the candidate was absent
because it was **closed**. No canonical op.

### 4.3 · FINDING 2's locator is wrong about `LIT-0420`

The finding says the stale framing *«appears in `PAPER 118` / `LIT-0420`»*. `LIT-0420`'s `Evidence
depth` and `Status note` were read in full: they say the manifest's `receipt` *«still names
`FTR-20260921-42589397-01` and is routed for re-pointing»* and **nothing about two open targets**. That
sentence was true under the decided rule and *stronger* under it, so on Mirror's ground **no op was
owed** and the candidate's first draft wrote none.

⚠️ **The record nevertheless has an op — `LIT-1` — and the distinction matters.** `ee94838` repaired
the field on disk, so the sentence's **present tense** became false for a reason Mirror could not have
seen (its review predates the tool by hours). `LIT-1` therefore lands under **`REP-26`**, not under
FINDING 2, and the contest stands exactly as stated: the stale *«deliberately open»* framing Mirror
located in this record **is not in it**. The `CLAIM 002` and `PAPER 001` limbs of the locator are exact
and are repaired as FINDING 2 asks. 🔴 **Recorded rather than quietly merged**, because a finding
repaired for a different reason than it gives is a finding that was not confirmed, and the next reader
must be able to tell the two apart.

### 4.4 · One statement in `CLAIM 030` that this candidate deliberately does NOT touch

The paragraph's earlier sentence *«la discordanza rilevante per l'esito è la sopravvivenza; ma non è
l'unica»* is correct as it stands and is left alone. So is the 🔴 correction note from
`CC-20260928-MIRROR003-REPAIRS-01` and the one from `CC-20260928-MIRROR0928-REPAIRS-01`: **the history
of the three narrowings stays visible in the record**, because a paragraph that shows its own three
rounds is the only evidence the ladder worked. `C30-1` replaces the sentence that is false; it does not
tidy the trail.

---

## 5 · Applied outside this candidate by the same package (non-canonical, 2026-09-28)

Verified, one by one, that none of these is one of the four scientific current files nor
`disease_model.md`.

**(a) The review is persisted verbatim** at
[`session_evaluations/2026-09-28_BATCH_20260928_002_mirror_review.md`](../session_evaluations/2026-09-28_BATCH_20260928_002_mirror_review.md),
with a one-line provenance header declaring **one** mechanical transformation and no word changed: the
three abbreviated digests/filenames (8-hex-plus-ellipsis forms, on which the publication gate BLOCKs)
were expanded to their full values, `780f42de…7e7a34` →
`780f42de9b3982fa5bf9bf1e6bb76f71384c943aa197fb2d4de80be7ac7e7a34` (re-derived with `sha256sum`,
**equal**), `ae7f42…f898af` → `ae7f429190e0b48faaf91f9df0c79e66dd7986d23c65c21f5564ef8607f898af`, and
`PMID42589397…xml` → `PMID42589397_ZZ2026_PMC_2026-09-27.xml`. A programmatic **round-trip check**
confirmed the persisted body is identical to the session artefact under the inverse substitution.

**The batch report** `session_evaluations/2026-09-28_BATCH_20260928_002.md` carries an appended
**ERRATUM** with five items and **no rewriting of its body**: `E1` strikes the Deferred row for
`FTR-20260928-42589397-03` with the commit and time evidence (FINDING 1); `E2` moves the Deferred row
`Mirror 4, field half` out of Deferred, its unblocking condition having occurred at `9b8378e` (FINDING
2); `E3` withdraws the over-broad `Mirror 13` row and states the `a510aa7` adjudication a future reader
should implement (FINDING 5); `E4` corrects the backlog figure to **14 at `cf40b73`** and withdraws the
unverified causal attribution (FINDING 7); `E5` records what the erratum does **not** change.

**(b)** `CC-20260928-MIRROR0928-REPAIRS-01` carries an appended, append-only **CORRECTION NOTE** with
three items: `C1` withdraws its § 2.4 containment reasoning and amends hand-off `13` to *refuse a span
that covers headings, not one that merely reaches EOF* — with the measured spans and the note that a
refusal keyed on EOF alone would have refused two of its own nine **correct** ops (FINDING 5); `C2`
amends hand-off `7` to *align the help line with the contract the tool's body states* (FINDING 6); `C3`
strikes its BATCH DISPOSITION's closing *«still owed and still unrecorded»* (FINDING 1). Nothing above
those notes is rewritten and none of its nine propagated ops is reopened.

**(c)** The graph-hygiene stub FINDING 8 asked for exists:
[`CC-20260928-GRAPH-HYGIENE-01.md`](CC-20260928-GRAPH-HYGIENE-01.md) — **owner** ACTOR_ID `scientist`,
**trigger** the next batch whose scope already opens one of the eleven records, **or** the dated review
**2026-10-05** with an append-only review line that must be written on that date. It enumerates the
fifteen edges with the record to edit for each, names **both** counting rules (**15** any declared
field / **10** `Wikilinks` only, measured at `cf40b73` from the registry itself and cross-checked
against the export), and writes down the cost Mirror measured: `016 → 033` and `016 → 039` require
editing **`CLAIM 016`, a DisMech-sealed block**, so closing them drifts a sealed digest and obliges
`--absorb` plus a fresh revision ordinal. ⚠️ The earlier pass's **11** is not reproducible under either
rule today, and the stub says why.

**(d)** Nothing was written to `framework/`, `governance/`, `scripts/`, `roles/` or `.claude/` by this
package. FINDING 9 and the amended FINDING 5 / 6 hand-offs are stated in the session report (§ 6).

**(e) A receipt is prepared, not recorded — and it is NOT a `receipt_correction`.** 🔴 **This package
did not run `fulltext_receipts.py record`**: the dispatch forbids it. The event is prepared as
`FTR-20260928-36779245-06.json` under the session scratchpad's `receipts_pending/` directory.

⚠️ **The class of the event was measured, not assumed, and the first assumption was wrong.** The
obvious reading was that § 3's re-measurement sits **inside** the coverage of
`FTR-20260927-36779245-05` and is therefore a metadata `receipt_correction`. It does not.
`-05`'s coverage map declares **`methods: "not_read"`**, and to test Mirror's own declared falsifier
for FINDING 4 this reading **read the Methods** (§ 2.3, *Genetic variants*). A reading that opens a
section a prior receipt declares unread **widens coverage**, so the honest instrument is a new
`partial_fulltext_read` event with a widened coverage map and `prior_receipt:
FTR-20260927-36779245-05` — not a correction of the prior one. Recording it as a `receipt_correction`
would have understated what was read, which is the same failure mode in the opposite direction from the
one FINDING 1 caught. The prepared JSON carries: the re-hashed fingerprint
`780f42de9b3982fa5bf9bf1e6bb76f71384c943aa197fb2d4de80be7ac7e7a34` (**equal** to `-05`'s), the widened
coverage (`methods` `not_read` → `read`, everything else unchanged), an `evidence_basis` that states all
twelve axes with their distinct-value and modal counts, the four-row Genetics comparison, the Methods
§ 2.3 quotation in full and the declared gap (Supplementary Methods unfetched), and a `workflow` note
recording that it is deliberately not in the ledger.

**No manifest was edited by this package.** `deepdive_manifests/PMID36779245.json` is unchanged; the
twelve measurements live in § 3 of this candidate, because appending manifest entries is a write the
dispatch did not authorise.

**The lesson of FINDING 1 is applied to this very sentence:** whoever records the event must then check
with `fulltext_receipts.py status --pmid 36779245` that it is there, and **not** infer its status from
the ledger's total count — that inference is exactly what FINDING 1 caught.

---

## 6 · Harness Engineering hand-offs — deliberately NOT written into `framework/`

`framework/protocols/` and `framework/scripts/` are Harness Engineering's surface and two other agents
are landing there today. All three items below are stated as hand-offs and **no protocol, tool or
generated surface is touched by this package**.

| Mirror # | owner surface | one-line statement |
|---|---|---|
| **F9** (MINOR) | `framework/protocols/prompt_batch_commit.md` § Phase 3 note | **`git checkout -- <path>` is the pre-batch value only BEFORE the propagation commit.** Phase 5 fires `ABORT + restore from snapshot` on a post-propagation `BLOCK_BATCH_COMMIT`, and a batch has *committed* the propagation by then — so from that commit onward `git checkout -- <path>` restores the **post**-batch bytes and the only correct restore is `git checkout <pre-batch commit> -- <path>` (or a revert of the propagation commit). The command as written is right exactly during the uncommitted window and silently wrong after it, which is the window the Phase-5 ABORT actually lives in. **The fix is two sentences in Phase 3:** state the restore with its base, and require the **pre-batch commit SHA to be recorded in Phase 3** beside the `SNAPSHOT_DECLARATION`, so the correct command is writable when it is needed. Moot for `disease_model.md` (`a510aa7` put it in the declaration); the reasoning is what gets reused. |
| **F5** (NOTE) | `framework/scripts/record_scoped_edit.py` — hand-off `13` amended | **The refusal is keyed on covering headings, not on reaching EOF, and the shipped tool already does this.** For the last record at its level the `_span_from` EOF fallback returns the record's **true end**: `PAPER 118` 595 115 → 598 521 = `len(text)`, `LIT-0420` 518 196 → 521 108 = `len(text)`, no heading after either. A refusal keyed on EOF alone would have refused two **correct** ops. The genuine instance is `id: "BLOCK 3"` in `working_model_current.md`, 49 194 → 96 155, which covers six `##` headings including the whole `## Changelog`. **Nothing to implement if the current behaviour is as `a510aa7` describes; the ask is that the docstring say *covering headings*, so the next reader does not implement the overbroad version.** |
| **F6** (NOTE) | `disease-models/wwox/analysis/scripts/reseal_dismech_baseline.py` — hand-off `7` amended | **Align the help line with the contract the body states.** The help text reads as if the revision ordinal were inferred from a label's spelling at read time; the body parses it **once, at the write**, stores an integer, and states *«ordering is never read off the spelling»*. One line of help text. The abridged-history and three-coexisting-conventions limbs of the original hand-off stand. |

---

## 7 · What this candidate does NOT do

- It does not touch `CLAIM 005`, `CLAIM 016`, `CLAIM 024`, `CLAIM 035`, `PAPER 019`, `PAPER 055` or
  `PAPER 056` — the six DisMech-sealed blocks — so **no sealed digest can drift** and no `--absorb` or
  revision ordinal is owed. The propagating batch runs `reseal_dismech_baseline.py --check` and expects
  `anchor:` only.
- It does not move any claim `Status`, `Type`, `Transferability`, `clinical relevance`, BLOCCO 1 field
  or therapeutic `SCORE`/`SAFETY` value; it adds, removes and re-segments **no** record.
- It does not touch `therapeutic_strategies_current.md`, the dismissal ledger, the discovery ledger,
  the full-text queue, any manifest, the receipt ledger, any tool or any generated surface. Its one
  literature-log op (`LIT-1`) is scoped to `LIT-0420` alone.
- It does not close a claim→claim edge or add a wikilink: that is
  `CC-20260928-GRAPH-HYGIENE-01`'s scope and it is a **stub**, not a proposal.
- It does not re-point any manifest and does not edit one. `deepdive_manifests/PMID42589397.json`
  was repaired by `manifest_receipt_repoint.py` at `ee94838`, by a sanctioned instrument and from the
  ledger; this candidate only brings two canonical sentences into agreement with that outcome, and the
  receipt ledger's own append-only account of the field is left exactly as written.
- ⚠️ **It asserts nothing about the other non-conforming manifests.** 16 remain; of those, 10 are
  reported batch-repairable by the same tool, **5 are refused for artefact divergence** — a later,
  deeper reading rewrote a manifest an earlier reading created, so *which* reading the manifest
  describes is a **scientific** decision and not a mechanical repoint — and 1 has no producing event in
  the ledger at all and needs a **reading**, not a repoint. None of that is decided here, and no record
  this candidate touches implies otherwise.
- It does not reopen `BATCH_20260928_002`'s `MINOR` classification, its `WM_v7.1 → WM_v7.2` bump, or
  any of the nine ops that batch propagated. Mirror's verdict on it is **CONFIRMED**.
- It does not assert *«the two patients were not equally screened»* — see § 4.1. The artefact does not
  license it.

**Not medical advice.**
