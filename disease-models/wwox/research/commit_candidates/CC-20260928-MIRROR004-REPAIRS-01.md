# COMMIT CANDIDATE — CC-20260928-MIRROR004-REPAIRS-01

**Candidate ID:** CC-20260928-MIRROR004-REPAIRS-01
**Status:** `PROPOSED — NOT PROPAGATED`
**Base head:** `a3f68b1`
**Author:** ACTOR_ID `scientist`, package `mirror004-repairs`, dispatched by the Orchestrator under the
operator's standing authorisation of 2026-09-27 (*«procedi tu, ti autorizzo su tutto»*).
**Source of the task:** the Mirror ex-post review of `BATCH_20260927_004`, persisted verbatim at
[`session_evaluations/2026-09-27_BATCH_20260927_004_mirror_review.md`](../session_evaluations/2026-09-27_BATCH_20260927_004_mirror_review.md)
(verdict *CONFIRMED WITH FINDINGS*: 0 BLOCKING-SCIENTIFIC, 3 MINOR `F1`–`F3`, 6 NOTE `N1`–`N6`), plus the
Orchestrator's first-hand adjudication of `F1` recorded in that file's provenance header. This candidate
carries **every item of that review that needs one of the four scientific current files or
`therapeutic_strategies_current.md`**: `F1(b)`, `F2`, `F3`, `N1`, `N2`, `N3` (the `TX-007` half), `N5`, and
one item Mirror did not name (§2.2 `PR-1`). The non-canonical items (`N4`, `N6`, the `D-23` half of `N3`)
were applied directly by the same package and are listed in §5. **A reviewer's output is not gospel:**
every Mirror statement below was re-verified first-hand against the current file and, where it concerns a
source, against the fingerprinted artefact. One of them does not hold as written and is recorded
**CONTESTED IN PART** with the measurement (§1, `N3`).

**Declared change class: `MINOR`.** No claim or paper `Status`, `Classification`, `Type`,
`Transferability`, `clinical relevance` or `Claim links` value moves; no `BLOCCO 1` field and no clinical
position is touched; no claim, paper or `TX-` record is added or removed; **no score moves** (`N3`
explicitly names a surface without moving `SAFETY 1`). Two ops sit inside `consolidated baseline` records
(`CLAIM 002`, `CLAIM 021`) and both **only narrow or source what is already there**: `F1(b)` adds the
locator of a string the record already carries, and `N1` replaces a paraphrase with the source's own
longer sentence, restoring a dropped clause. `F2` **withdraws an assertion** from a paper record to match
a withdrawal `BATCH_20260927_004` already landed in `CLAIM 021` — it propagates a decision, it does not
make one. `F3` is pure markdown. `N2` and `PR-1` correct counts and a false bookkeeping sentence.

**Sources re-read this package.** `files/fulltext/PMID34634460_Breton2021_EPMC_2026-09-27.xml`, sha256
`934b4e1a42ac19f5cd8912994fb171beabdeb94a6631b23d9a383dab1db906aa` (**re-hashed here: equal to the
declared digest**) · `files/fulltext/PMID42422765_Obeid2026_PMC_2026-09-27.xml`, sha256
`7bea83346b708e541d2c432e5da4029f69673e1abc3c6fe70926ad0e3ec2eef2` (**re-hashed here: equal**).
**Receipts read:** `FTR-20260810-42397075-04` (PMID 42397075, `complete_fulltext_read`, `coverage` all
`read` / tables `not_present`) — **artefact absent from every reachable checkout**, which is why `F1(b)`
cites it by receipt + manifest entry rather than by a re-verification.
**Manifests read:** `deepdive_manifests/PMID42397075.json` (schema v2, 30 `verbatim_locators.entries`;
entries **13** and **20** as printed, indices 12 and 19, carry the two `CLAIM 002` strings — both
`snippet`s byte-equal to the landed text, checked here). **No manifest is modified by this candidate.**
**Audits read:** `research/locator_audits/2026-09-27_wave2_audit_A/B/C/D2/E.md`, counted packet by packet
for `N2`.

**`context_policy`: `QUESTION_DRIVEN`** — declared. Held before any source was reopened: the Mirror
review, `CLAIM 002`, `CLAIM 021`, `PAPER 001`, `PAPER 018`, `PAPER 031`, `PAPER 056`, `TX-007`, the
`working_model_current.md` `Last update` line and its `BATCH_20260927_004` changelog block, the five
wave-2 audits, `FTR-20260810-42397075-04` and `deepdive_manifests/PMID42397075.json`. Questions fixed
**before** the artefacts were opened: *(1) does Breton 2021 exclude pannexin blanketly, or only for the
CBX effect, and does §3.4 leave an earlier-developmental route open; (2) what exactly is the conjunction
whose second half `CLAIM 021`'s paraphrase drops; (3) what surface did the four zero counts actually run
on, and does that surface carry supplementary captions; (4) do the two `CLAIM 002` strings exist as
persisted locators of the complete read, and of which entries.* The two large registries were reached
with `registry_records.py`, never read whole.

---

## 1 · CURRENT_TARGET and first-hand verification of every Mirror item

Each `old` string below was measured in its target file: **all twelve occur exactly once.** Ten of
Mirror's eleven canonical statements are confirmed; one is confirmed in its conclusion and **contested in
its supporting count**.

| Item | Mirror's statement | Verdict | How verified, first-hand |
|---|---|---|---|
| `F1` (factual half) | two PMID 42397075 body strings are in `CLAIM 002`'s `Nota di provenienza`, while the batch report says the seven triples were *"deferred unwritten"* | ✅ **confirmed** | both strings present, 1 occurrence each; `working_model_current.md` and the report both carry *"deferred unwritten"* |
| `F1` (characterisation) | they are *"unlabelled quotations of unread material"*, to be labelled `UNVERIFIABLE_SURFACE` or de-quoted | ❌ **overturned** (Orchestrator adjudication, re-confirmed here) | both are `deepdive_manifests/PMID42397075.json` `verbatim_locators.entries` **13** and **20**, `"surface": "body"`, artefact `PMID42397075_Aqeilan2026_fitz.txt`, anchors *"Discussion, p. 16"* / *"Statistical analysis"*, receipt `FTR-20260810-42397075-04` — each `snippet` **byte-equal** to the landed string. A `complete_fulltext_read` whose artefact is off-disk is not an unverified attestation. Repair is a point-of-use citation |
| `F2` | `PAPER 031`'s `Note` still asserts *"burst NMDAR- e gap-junction-dipendenti (… pannexina no)"* | ✅ **confirmed** | string present, 1 occurrence; the batch edited `Claim links` and `Role` in the same record and left this clause standing. Mirror quotes the clause with bold that the file does not carry — immaterial |
| `F2` (merits, on the source) | the source excludes pannexin **only for the CBX effect**, adds that a subset may be pannexin-influenced, and §3.4 cannot rule out an earlier-developmental route | ✅ **confirmed** | on the Breton XML: *«the effects were not recapitulated with BB-FCF (10 μM), indicating that the suppressive effects of CBX were not due to pannexin 1 channel opening»* (1×) · *«suggesting that a subset of these bursts may be influenced by pannexin 1 channels»* (1×) · *«we cannot rule out the possibility that a pannexin 1 blocker could be an anti-epileptic treatment at earlier developmental stages»* (1×) · `BB-FCF` 7× |
| `F3` | `PAPER 056`'s `Note` carries an orphan `**` before *fosfo-S9* and an unmatched trailing `**` | ✅ **confirmed** | `**con la **fosfo-S9 invariata**` (1×) — a nested open, never closed; and `…`BATCH_20260927_004`)**.` (1×) |
| `N1` | `CLAIM 021`'s paraphrase drops *«yet these mice die between 3 and 4 postnatal weeks»* | ✅ **confirmed** | source sentence, verbatim and 1× in the de-tagged XML: *«Since the recordings were obtained at P13-17, yet these mice die between 3 and 4 postnatal weeks, the chosen age group may mimic a late-stage disorder of WWOX.»* The landed paraphrase carries only the second half |
| `N2` | the audits carry **82** triples, not *seventy-nine*, and **22** `UNVERIFIABLE_SURFACE` (**20** after the two contested), not *nineteen* | ✅ **confirmed, re-derived independently** | packet by packet: `audit_A` 6+5+4+7 = 22 (UNV 5) · `audit_B` 5+6+7 = 18 (UNV 12) · `audit_C` 11+4 = 15 (UNV 0) · `audit_D2` 5+6+4 = 15 (UNV 1) · `audit_E` 6+6 = 12 (UNV 4) → **82 / 22**, and 20 after the two `audit_B` verdicts overturned on re-acquired bytes. 19 needs an undeclared extra exclusion (`audit_E` t6) |
| `N3` (conclusion) | the surface the census ran on is not named; `mmc1.pdf` is absent, so a supplementary surveillance panel is not excluded | ✅ **confirmed, and better founded than Mirror's own version** | the artefact **declares its own missing surface**: `<supplementary-material id="mmc1">` captioned *«Document S1. Figures S1–S8»*, plus `mmc2`; `mmc1.pdf` is absent from every reachable checkout |
| `N3` (supporting count) | *"`Figure S1`, `Table S1`, `supplementary` all 0 as strings"* | ⚠️ **CONTESTED IN PART** | measured on those exact bytes: `Figure S1` **0** ✅ · `Table S1` **0** ✅ · `supplementary` **40** ❌ · `mmc1` **36** · `<supplementary-material` **2**. And *"the body cites S3E/S5J/S7I by reference"* → `S3E` **1**, `S5J` **0**, `S7I` **0**. Mirror's other counts reproduce exactly (`neoplas` 0 · `carcinog` 0 · `histopatholog` 0 · `necropsy` 0 · `histolog` 2 · `tumor` 15 + `tumour` 1 = 16 case-insensitively; case-sensitive `tumor` is 13). **The finding survives its own wrong count and is strengthened by the correction:** the surface carries no supplementary *captions*, and it names the file that holds them |
| `N5` | `PAPER 018`'s append-only trailer now reads as a contradiction of `processed` / `031 · 033` | ✅ **confirmed** | trailer present 1×, and the `Claim links` / `Status` fields two lines above carry the new values. The trailer is **inside `paper_registry_current.md`**, so it is a candidate item, not an outside-batch edit |
| `N4`, `N6` | chain diagram; `D-` table tail | ✅ **confirmed** | `analysis/mechanism_intervention_map.md` and `research/dismissal_ledger_current.md` are **non-canonical**; applied directly, see §5 |
| `PR-1` (**Mirror did not name it**) | `PAPER 001`'s `Note` says all five boundaries *"are **DEFERRED**"* | ✅ found here | two of the five are in `CLAIM 002`, so the sentence is false of exactly the two strings `F1` is about. Same defect as `F1`, one record away, on a canonical surface |

### Not proposed, and why

- **Mirror's own `F1` repair** (inline `UNVERIFIABLE_SURFACE` label, or de-quoting). Refused: it would
  record a receipted, manifested, strict-PASS `complete_fulltext_read` as unverified, and de-quoting
  would discard a verified string to satisfy one checkout's file inventory.
- **`TX-007`'s `SAFETY 1`.** Unchanged. `N3` asks for a scope, not a score, and gives no reason to move
  one.
- **`deepdive_manifests/PMID42397075.json`'s stale `receipt` field** (`-03`, while every citing record
  names `-04`). Recorded in the batch report's erratum §5.2, **not edited**: rewriting a manifest that a
  receipt fingerprints is not a bookkeeping edit, and nothing resolves the manifest through that field.
- **`D-` table re-ordering (`N6`).** Refused: append-only ledger. A dated allocator note was appended
  instead (§5).

---

## 2 · PROPOSED_DELTA — exact operation lists

### 2.1 `disease-models/wwox/registries/claim_registry_current.md` — `batch_commit.py propagate` (record-scoped)

Three `replace-within` ops. **Dry-run clean on base `a3f68b1`:**
`DRY RUN … 3 op(s) on ['CLAIM 002', 'CLAIM 002', 'CLAIM 021']`.

#### C2-1 (`F1(b)`) — `CLAIM 002` · `replace-within` · change class `MINOR`

Cites the two strings at point of use by receipt + manifest entry, the convention this repository already
uses for a locator whose bytes are not on the local disk (`CLAIM 021`: *"`deepdive_manifests/PMID34634460.json`
entry 3"*; `CLAIM 002`'s own Appendix Fig S1A attestation, which names the PDF, the page, the dpi and the
`source_pdf_sha256`).

**old (verbatim, 1 occurrence):**

```text
(il confronto WT-vs-trattato che il testo afferma e il pannello 6A(ii) non disegna; *«rescued neuronal functional phenotypes without correcting RG abnormalities»*; la proteina consegnata fra 0.4× e 7× il WT; il fenotipo di composizione come quello del KO ingegnerizzato; *«No randomization or blinding was applied in this study»*)
```

**new:**

```text
(il confronto WT-vs-trattato che il testo afferma e il pannello 6A(ii) non disegna; *«rescued neuronal functional phenotypes without correcting RG abnormalities»* — **locator verbatim persistito**, `FTR-20260810-42397075-04`, `deepdive_manifests/PMID42397075.json` entry **13**, superficie `body`, ancora *"Discussion, p. 16"*; la proteina consegnata fra 0.4× e 7× il WT; il fenotipo di composizione come quello del KO ingegnerizzato; *«No randomization or blinding was applied in this study»* — **locator verbatim persistito**, stesso receipt, `deepdive_manifests/PMID42397075.json` entry **20**, superficie `body`, ancora *"Statistical analysis"*)
```

#### C2-2 (`F1(b)`, `F1(d)`) — `CLAIM 002` · `replace-within` · change class `MINOR`

States, at the point where the deferral is justified, **what the two quoted strings are** and that the two
`audit_B` verdicts on them are adjudicated against the persisted locators.

**old (verbatim, 1 occurrence):**

```text
**Cosa sbloccherebbe il ripuntamento:** una superficie strutturata di PMID 42397075 acquisita per qualunque via lecita e gratuita, riletta a receipt, con le cinque qualificazioni come locator verbatim.
```

**new:**

```text
**Cosa sbloccherebbe il ripuntamento:** una superficie strutturata di PMID 42397075 acquisita per qualunque via lecita e gratuita, riletta a receipt, con le cinque qualificazioni come locator verbatim. 🔵 **Precisazione 2026-09-28 (Mirror `F1` su `BATCH_20260927_004`, aggiudicata).** Due delle cinque qualificazioni sono citate qui sopra alla lettera, **con il loro locator**: non sono attestazioni non verificate, ma **locator verbatim persistiti** di un `complete_fulltext_read` (`FTR-20260810-42397075-04`; manifest a 30 locator, schema v2, strict PASS). Ciò che manca su questo checkout è l’**artefatto**, non la lettura — la stessa assenza di byte che rese inutile `audit_D` prima che `audit_D2` lo superasse per ri-acquisizione. I verdetti `UNVERIFIABLE_SURFACE` delle triple 3 e 6 di `audit_B` sono quindi **aggiudicati contro i locator persistiti**, e l’audit stesso lo dice: *«This is a source-availability outcome, not a judgement on the triples.»* Restano DEFERRED alla condizione sopra il ripuntamento della `Source` e le altre tre qualificazioni.
```

#### C21-1 (`N1`) — `CLAIM 021` · `replace-within` · change class `MINOR` (narrowing by restoration)

**old (verbatim, 1 occurrence):**

```text
and in Discussion §3.4 that because the recordings are at P13–P17 the chosen age group *«may mimic a late-stage disorder»*
```

**new:**

```text
and in Discussion §3.4 — quoting the authors’ whole conjunction, because the paraphrase had dropped the half that makes the hedge intelligible (Mirror `N1`, repaired 2026-09-28) — *«Since the recordings were obtained at P13-17, yet these mice die between 3 and 4 postnatal weeks, the chosen age group may mimic a late-stage disorder of WWOX.»*
```

### 2.2 `disease-models/wwox/registries/paper_registry_current.md` — FULL REWRITE (records `PAPER 001`, `PAPER 018`, `PAPER 031`, `PAPER 056` only)

`batch_commit.py propagate` **refuses this file by name** (*"Benchmark J (J3_DECISION.md) did not support
it. Use the full rewrite of prompt_batch_commit.md Phase 4"*), so the executor takes the full-rewrite
path and applies the five exact replacements below, **each measured unique in the whole file (1
occurrence)** and each confined to the named record.

#### PR-1 (found by this package, the `F1` defect one record away) — `PAPER 001` · exact replace · `MINOR`

**old (verbatim, 1 occurrence):**

```text
That repointing, and the five boundaries the refereed reading carries, are **DEFERRED**
```

**new:**

```text
That repointing, and **three** of the five boundaries the refereed reading carries, are **DEFERRED** — ⚠️ **corrected 2026-09-28 (Mirror `F1`, as adjudicated): the other two boundaries were written**, as verbatim quotations in [[claim_registry_current#CLAIM 002]]’s provenance note, each cited there by receipt + manifest entry (`FTR-20260810-42397075-04`, `deepdive_manifests/PMID42397075.json` entries **13** and **20**). They are persisted locators of this complete read, not unverified attestations: what is absent from this checkout is the artefact, not the reading
```

#### PR-18 (`N5`) — `PAPER 018` · exact replace · `MINOR` (append-only trailer given its pointer, not rewritten)

**old (verbatim, 1 occurrence):**

```text
`Status: filtered_in` and `Claim links: pending` are deliberately NOT changed by that batch: whether this reading produces a claim is a scientific question it did not ask.
```

**new:**

```text
`Status: filtered_in` and `Claim links: pending` are deliberately NOT changed by that batch: whether this reading produces a claim is a scientific question it did not ask. ⚠️ **Superseded in turn by `BATCH_20260927_004`, which measured the population and decided** — see the `Claim links` field above: `Status` is now `processed` and the links are `031 · 033`. The sentence is kept rather than corrected, because it was true of `BATCH_20260920_001` and is the trace of what that batch declined to do; without this pointer it now reads as a contradiction of the fields two lines above it. Note added 2026-09-28 (Mirror `N5`).
```

#### PR-31 (`F2`) — `PAPER 031` · exact replace · `MINOR` (propagates a withdrawal `CLAIM 021` already landed)

**old (verbatim, 1 occurrence):**

```text
burst NMDAR- e gap-junction-dipendenti (d-APV abolisce; carbenoxolone ↓87%; pannexina no)
```

**new:**

```text
burst **NMDAR-dipendenti** (d-APV abolisce) — ⚠️ **la metà gap-junction di questa dipendenza è RITIRATA come non attribuibile il 2026-09-27 (`BATCH_20260927_004`, `CC-20260826-GAPJUNCTION-ATTRIBUTION-01`; vedi [[claim_registry_current#CLAIM 021]]) — ritiro di attribuzione, NON affermazione che le gap junction non siano coinvolte: l’occlusione non è mai stata testata.** Il carbenoxolone a 100 μM riduce la frequenza degli eventi dell’**87%** e la durata del **18%**, ma *«This did not return to normal levels after washout.»*, e gli autori stessi scrivono che *«CBX may not be specific to gap junctions»*. ⚠️ **E l’esclusione della pannexina NON è blanket — la sua narrowness viaggia con essa:** gli autori escludono quella via **per il solo effetto del CBX**, sulla base del BB-FCF (*«indicating that the suppressive effects of CBX were not due to pannexin 1 channel opening»*), **ma aggiungono immediatamente** che *«a subset of these bursts may be influenced by pannexin 1 channels»*, e in Discussion §3.4 che *«we cannot rule out the possibility that a pannexin 1 blocker could be an anti-epileptic treatment at earlier developmental»* stadi. Il precedente *«pannexina no»* era quindi falso come scritto; corretto il 2026-09-28 (Mirror `F2`), verificato su `files/fulltext/PMID34634460_Breton2021_EPMC_2026-09-27.xml`, sha256 `934b4e1a42ac19f5cd8912994fb171beabdeb94a6631b23d9a383dab1db906aa`)
```

> **Why this wording and not a shorter qualifier.** Mirror proposed appending a one-clause flag. That
> would leave *«pannexina no»* standing as a statement and hang a warning beside it. `CLAIM 021`'s landed
> text does not do that: it writes the exclusion's **scope** (the CBX effect, via BB-FCF), the sentence
> the authors add immediately after, and the §3.4 developmental caveat. This wording matches `CLAIM 021`
> clause for clause, because the whole point of the batch's own insistence — *«la sua narrowness viaggia
> con essa»* — is that the narrowness travels, not a pointer to where the narrowness is kept.

#### PR-56a, PR-56b (`F3`) — `PAPER 056` · two exact replaces · `MINOR` (formatting only, no prose changes)

| # | old (verbatim, 1 occurrence) | new |
|---|---|---|
| PR-56a | `**con la **fosfo-S9 invariata**` | `con la **fosfo-S9 invariata**` |
| PR-56b | ``(`CC-20260826-GSK3B-S9-AXIS-01` `D13`, `BATCH_20260927_004`)**.`` | ``(`CC-20260826-GSK3B-S9-AXIS-01` `D13`, `BATCH_20260927_004`).`` |

PR-56a removes the nested, never-closed open marker and **keeps** the bold on *fosfo-S9 invariata*, which
reads as the author intended; Mirror proposed de-bolding the phrase entirely, which loses an emphasis
that was wanted. PR-56b removes the unmatched close. The `Note`'s `**` count goes 52 → 50, no `****`
sequence is created, and **not one word of prose changes**.

### 2.3 `disease-models/wwox/registries/working_model_current.md` — `batch_commit.py propagate` (record-scoped)

Three `replace-within` ops. **Dry-run clean on base `a3f68b1`:**
`DRY RUN … 3 op(s) on ['Working Model Current', 'BATCH_20260927_004 — WM_v6.1 → **WM_v7.0_2026-09-27**
(MAJOR)', 'BATCH_20260927_004 — WM_v6.1 → **WM_v7.0_2026-09-27** (MAJOR)']` — anchored by `heading`, since
this file's identity level is 1 and the changelog block is a nested sub-block. The batch executor adds its
own `Version` / `Last update` / changelog row (`WM_v7.0` → **`WM_v7.1`**, MINOR) as usual.

#### WM-1 (`N2`) — `heading: Working Model Current` (the `Last update` line) · `replace-within` · `MINOR`

**old (verbatim, 1 occurrence):**

```text
Fifteen blind-audit verdicts across five auditors bound the wording; four OVERSHOOTs were rewritten to the source's own hedged words and nineteen UNVERIFIABLE_SURFACE statements entered as **declared attestations or not at all**.
```

**new:**

```text
Five auditors over fourteen packets returned **82** verdicts and bound the wording; **four** OVERSHOOTs were rewritten to the source's own hedged words and **22** `UNVERIFIABLE_SURFACE` statements — **20** after the two this batch contested and overturned on re-acquired bytes — entered as **declared attestations or not at all** (counts corrected 2026-09-28, Mirror `N2`: *fifteen* and *nineteen* were reachable by no stated rule).
```

> ⚠️ **Mirror did not name *fifteen*, and it is the weaker of the two figures.** No counting rule in the
> record yields 15 from 82 triples: 4 `OVERSHOOT` + 22 `UNVERIFIABLE_SURFACE` = 26 non-`SUPPORTED`
> verdicts, and the 4 `OVERSHOOT`s alone are what drove a rewrite. The op replaces it with the counts the
> audits support rather than with a third unexplained number.

#### WM-2 (`N2`, `F1`) — `heading: BATCH_20260927_004 — …` · `replace-within` · `MINOR`

**old (verbatim, 1 occurrence):**

```text
Nineteen such statements were handled this way, and the seven triples of `CC-20260826-PROVENANCE-01` were **deferred unwritten** because the bytes are not obtainable free.
```

**new:**

```text
**Twenty-two** such statements were handled this way — **20** after the two `audit_B` verdicts this batch contested and overturned on re-acquired bytes — and **five** of the seven triples of `CC-20260826-PROVENANCE-01` were **deferred unwritten** because the bytes are not obtainable free. ⚠️ **Corrected 2026-09-28 (Mirror `N2` and `F1`, adjudicated).** The earlier wording said *nineteen*, a figure no stated counting rule reaches, and said all seven triples were deferred unwritten. **Two of the seven were written** — the scope-of-rescue and the randomization/blinding boundary, in [[claim_registry_current#CLAIM 002]]’s provenance note — and they are **not** unverified attestations: they are persisted verbatim locators of a `complete_fulltext_read` (`FTR-20260810-42397075-04`, `deepdive_manifests/PMID42397075.json` entries **13** and **20**), now cited there at point of use. The **artefact** is absent from this checkout; the reading is not.
```

#### WM-3 (`N2`) — `heading: BATCH_20260927_004 — …` · `replace-within` · `MINOR`

**old (verbatim, 1 occurrence):**

```text
Five blind auditors, fourteen packets, seventy-nine triples.
```

**new:**

```text
Five blind auditors, fourteen packets, **82** triples — re-derived 2026-09-28 from the five persisted audits, packet by packet (`audit_A` 22 · `audit_B` 18 · `audit_C` 15 · `audit_D2` 15 · `audit_E` 12); the earlier figure *seventy-nine* is reachable by no rule this record states (Mirror `N2`).
```

### 2.4 `disease-models/wwox/therapeutics/therapeutic_strategies_current.md` — exact replace (`TX-007` ceiling note)

`batch_commit.py propagate` refuses this file by name as well, so it takes the exact-replace path. One
op; `old` measured unique in the whole file. **The `SAFETY 1` score does not move** — `N3` asks for the
scope the argument already needs, so the absence is asserted of a stated surface instead of of "the
paper".

#### TX7-1 (`N3`) — `TX-007` ceiling note · exact replace · `MINOR`

**old (verbatim, 1 occurrence):**

```text
(measured on the declared artefact: `neoplas` 0, `carcinog` 0, `histopatholog` 0, `necropsy` 0)
```

**new:**

```text
(measured on the **main-text JATS surface** `files/fulltext/PMID42422765_Obeid2026_PMC_2026-09-27.xml`, sha256 `7bea83346b708e541d2c432e5da4029f69673e1abc3c6fe70926ad0e3ec2eef2`: `neoplas` 0, `carcinog` 0, `histopatholog` 0, `necropsy` 0 — ⚠️ **and that surface carries no supplementary captions at all**, so the absence is asserted **of the article’s running text and captions**, which is what this argument needs. The artefact names its own missing surface: it declares `mmc1.pdf`, captioned *«Document S1. Figures S1–S8»*, and that file is **absent from this checkout** and on this batch’s deferral list, so a supplementary surveillance panel is **not excluded** by this census. Scope named 2026-09-28, Mirror `N3`; the score does not move)
```

---

## 3 · Simulation — all twelve ops applied to a scratch copy of `a3f68b1`

Run before this candidate was written, on copies, never on the live files:

| File | ops | result |
|---|---|---|
| `claim_registry_current.md` | 3 | applied, each `old` found exactly once, each `new` unique after |
| `paper_registry_current.md` | 5 | applied, each `old` found exactly once; `PAPER 056` `Note` `**` count 52 → 50, zero `****` |
| `working_model_current.md` | 3 | applied, each `old` found exactly once |
| `therapeutic_strategies_current.md` | 1 | applied, `old` found exactly once |
| — | **12** | **SIMULATION OK** |

Plus `batch_commit.py propagate` **dry runs** on the two files it supports, both clean (§2.1, §2.3).
**The live current files are byte-unchanged by this candidate** — it is `PROPOSED — NOT PROPAGATED`.

---

## 4 · LOCATOR TRIPLES FOR BLIND AUDIT

Six triples, all on artefacts present in this checkout with digests re-verified here. `F1(b)`'s two
strings are **deliberately not offered as triples**: their artefact is off-disk, a blind auditor would
return `UNVERIFIABLE_SURFACE` for source absence exactly as `audit_B` did, and the op does not assert
anything new about the source — it cites where the reading is persisted.

| # | proposition | quote / count | anchor · artefact |
|---|---|---|---|
| t1 | The pannexin exclusion is scoped to the CBX effect and rests on BB-FCF | *«Furthermore, the effects were not recapitulated with BB-FCF (10 μM), indicating that the suppressive effects of CBX were not due to pannexin 1 channel opening.»* — 1× | Results, CBX/BB-FCF paragraph · `PMID34634460_Breton2021_EPMC_2026-09-27.xml` (`934b4e1a…b906aa`) |
| t2 | The authors immediately admit a pannexin-influenced subset | *«suggesting that a subset of these bursts may be influenced by pannexin 1 channels»* — 1× | same paragraph, next sentence · same artefact |
| t3 | §3.4 leaves an earlier-developmental pannexin route open | *«we cannot rule out the possibility that a pannexin 1 blocker could be an anti-epileptic treatment at earlier developmental stages»* — 1× | Discussion §3.4 · same artefact |
| t4 | The age hedge is a conjunction whose first half is the lifespan | *«Since the recordings were obtained at P13-17, yet these mice die between 3 and 4 postnatal weeks, the chosen age group may mimic a late-stage disorder of WWOX.»* — 1× | Discussion §3.4, sentence before t3 · same artefact |
| t5 | CBX's suppression does not reverse on washout | *«This did not return to normal levels after washout.»* — 1× | Results, CBX paragraph · same artefact |
| t6 | The census artefact carries no supplementary captions and names the file that does | `Figure S1` **0** · `Table S1` **0** · two `<supplementary-material>` elements, the first captioned *«Document S1. Figures S1–S8»* pointing at `mmc1.pdf`; `neoplas`/`carcinog`/`histopatholog`/`necropsy` all **0** | whole-file census · `PMID42422765_Obeid2026_PMC_2026-09-27.xml` (`7bea83346b708e541d2c432e5da4029f69673e1abc3c6fe70926ad0e3ec2eef2`) |

**Offered against this candidate, not merely alongside it:** `t6` is the triple that, if it fails, breaks
`TX7-1`. If a reader finds supplementary captions in that artefact, the scope sentence is wrong and must
be rewritten — and Mirror's own falsifier item 1 (`mmc1.pdf` holding a histopathology panel) stays open
and unaffected by anything here.

---

## 5 · Applied outside this candidate by the same package (non-canonical, 2026-09-28)

| Mirror item | Surface | What was done |
|---|---|---|
| `N4` | `analysis/mechanism_intervention_map.md`, CHAIN B | the chain line now reads *"bursting DEPENDS ON NMDAR activity [CLAIM 021 — NMDAR half only; the gap-junction half of this dependence was WITHDRAWN as not attributable 2026-09-27 …]"*, and the `carbenoxolone (tool)` entry is flagged as sitting under the withdrawn node |
| `N6` | `research/dismissal_ledger_current.md`, `D-` table head | dated allocator note: the table is not in numeric order, its tail (`D-22`) is not its highest number, the next id comes from `max(D-nn) + 1`, `D-17` stays reserved, `D-27`–`D-30` not minted. **Rows not re-sorted** — append-only |
| `N3` (the `D-23` half) | `research/dismissal_ledger_current.md`, `D-23` | the census's surface named: main-text JATS with its sha256, no supplementary captions, `mmc1.pdf` declared *«Figures S1–S8»* and absent; and `histolog` 2 recorded as the wider token |
| `F1(c)`, `F1(d)`, `N2` | `session_evaluations/2026-09-27_BATCH_20260927_004.md` | append-only `## ERRATUM` (6 sections): the report's three *"deferred unwritten"* statements corrected including the `DEFAULTS_TAKEN` row; why Mirror's `F1` repair is refused; the two `audit_B` verdicts adjudicated and the review's third falsifier resolved in the batch's favour; `N2`'s counts re-derived; Mirror's `N3` count contested with the measurement; two further bookkeeping inaccuracies |
| — | `session_evaluations/2026-09-27_BATCH_20260927_004_mirror_review.md` | the review persisted verbatim with a two-line provenance header carrying the `F1` adjudication |

---

## 6 · DEFAULTS_TAKEN and DECISIONS_TAKEN for this candidate

| Condition | Default taken | Why it is safe | What would have been different |
|---|---|---|---|
| `N3`'s locator names both `TX-007` and `D-23`; `TX-007` is not one of the four current files, but the mandate routes `N3` to the candidate | **followed the mandate** — `TX-007` in the candidate, the `D-23` half applied outside it | both surfaces end up scoped; the canonical-looking one goes through the gate that reviews it | applying both outside the batch would have landed sooner and skipped a review the mandate asked for |
| Mirror's `N3` supporting count is wrong while its conclusion is right | recorded **CONTESTED IN PART** with the measurement, and kept the repair | a wrong count in a review is a finding about the review, not a reason to drop a correct finding | reporting `N3` as simply confirmed would have carried the false count forward |
| `working_model_current.md` also says *"fifteen blind-audit verdicts"*, which Mirror did not name and which no rule reaches | replaced with the two counts the audits support, in the same op | a derivable pair is strictly better than an underivable single | leaving it would have left one unreconciled figure beside two corrected ones |
| `PAPER 056`'s emphasis could be repaired by de-bolding (Mirror) or by removing the orphan open (here) | **removed the orphan open, kept the bold** | the prose is untouched either way; keeping the bold preserves an emphasis the author wanted | de-bolding would have silently dropped an emphasis while fixing a typo |
| `deepdive_manifests/PMID42397075.json` carries a stale `receipt` field | **recorded, not edited** | nothing resolves the manifest through that field, and a receipt fingerprints the manifest | editing it would have touched a fingerprinted artefact for a cosmetic mismatch |
| `D-` table is out of numeric order | **noted, not re-sorted** | append-only ledger; a note gives the next allocator exactly what it needs | re-sorting would have rewritten rows this package is not correcting |

| Decision | Alternatives rejected | Consulted | Reversibility | How to revert |
|---|---|---|---|---|
| Refuse Mirror's `F1` repair and cite by receipt + manifest entry instead | inline `UNVERIFIABLE_SURFACE` label; de-quoting to a description | the Orchestrator's first-hand adjudication; `audit_B`'s own closing note; the existing `CLAIM 021` entry-3 convention | fully reversible | drop `C2-1`/`C2-2`, `PR-1`, `WM-2` |
| Write `PAPER 031`'s qualifier as `CLAIM 021`'s full scoped wording, not a one-clause flag | Mirror's proposed append-only flag | `CLAIM 021`'s landed text; the batch's own *«la sua narrowness viaggia con essa»* | fully reversible | replace `PR-31`'s `new` with the shorter flag |
| Keep `TX-007` at `SAFETY 1` | moving the score on the corrected scope | `N3` asks for a scope, not a score | n/a — nothing moved | n/a |

---

## WAVE READINESS (2026-09-28)

`READY`. Twelve ops, four files, all `old` strings unique and simulated; two files dry-run clean under
`batch_commit.py propagate`, two on the full-rewrite / exact-replace path the tool routes them to. Change
class `MINOR` throughout. Six locator triples offered for blind audit, one of them adversarial against
this candidate's own `TX7-1`. No score, `Status`, `Classification`, `Transferability`, `Claim links`,
`BLOCCO 1` field or clinical position moves. **Nothing here is medical advice.**
