# COMMIT CANDIDATE — CC-20260921-LOCATOR-COUNT-REDERIVATION-01

**Source:** not a reading. Scientist B checked four `paper_registry_current.md` records against the
manifests on disk and found three wrong; the Orchestrator then ran the full sweep with a purpose-built
tool. **The sweep is the evidence, and it is reproducible in one command.**
**Ledger:** `fulltext_receipts.py verify` → **OK: 188 chained receipt(s), tail anchored**.
**Change class:** **MINOR** — sixteen numbers corrected in one canonical file. **No claim, no
status, no conclusion, no evidence changes.** Every correction makes the registry claim **more**
evidence, never less.
**Target:** `working_model_version` MINOR bump at batch time. No `BLOCCO 1` change.
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R2.** `paper_registry_current.md` is canonical, so `BATCH_COMMIT` only — but
nothing here is a judgement. Each new value is `len(manifest["verbatim_locators"]["entries"])`,
re-derived mechanically, and a reviewer can reproduce all sixteen with:

```bash
python3 framework/scripts/locator_count_crosscheck.py .
```

---

## 1 · The measurement

**16 of 34** locator-count declarations in `paper_registry_current.md` disagree with the manifest
they name.

> 🔴 **Every one of the sixteen UNDERSTATES. Not one overstates.** Deltas run **+2 to +27**.

That direction is the finding, not a detail. **Random transcription error produces both
directions.** One direction means a systematic cause — and it rules out the frightening reading:
the registry is **not** claiming evidence it does not have. It is **failing to claim evidence it
does have.** A locator count is a *measurement of another file*; these were true when written and
were never re-derived as their manifests grew.

| registry line | PMID | declared | manifest holds | delta |
|---|---|---|---|---|
| 416 | `36779245` | 5 | **20** | **+15** |
| 439 | `32000863` | 5 | **25** | **+20** |
| 461 | `32581702` | 10 | **21** | **+11** |
| 485 | `31340538` | 4 | **11** | **+7** |
| 549 | `25012504` | 5 | **22** | **+17** |
| 2562 | `18487609` | 5 | **23** | **+18** |
| 3545 | `24550385` | 7 | **20** | **+13** |
| 5028 | `22634283` | 5 | **14** | **+9** |
| 6050 | `31428585` | 7 | **20** | **+13** |
| 6178 | `42082822` | 5 | **9** | **+4** |
| 6224 | `38182577` | 7 | **30** | **+23** |
| 6247 | `38499540` | 7 | **34** | **+27** |
| 6270 | `27308504` | 12 | **14** | **+2** |
| 7137 | `39416860` | 7 | **11** | **+4** |
| 7161 | `42397075` | 6 | **30** | **+24** |
| 7185 | `33255508` | 4 | **8** | **+4** |

## 2 · Two named causes, and one of them is a reconciliation that did not reconcile

🔴 **(a) The batch that fixed these declarations left them wrong.** `PMID 32000863` (line 439) and
`PMID 32581702` (line 461) both carry, in their own text, the sentence *"declaration reconciled
from the ledger by `CC-20260920-REGISTRY-LEDGER-DEPTH-01` (BATCH_20260920_001)"* — and both counts
are still wrong, by **+20** and **+11**. **A reconciliation that restates instead of re-deriving is
not a reconciliation.** This is the strongest argument in the candidate for making the derivation
runnable rather than doing it once by hand again.

🔴 **(b) `verbatim_locators` is an OBJECT, not a list, and `len()` on it returns 6.** Its keys are
`waived`, `source_fulltext_indexed`, `source_fulltext_indexed_evidence`,
`abstract_anchoring_waived`, `surface_note`, `entries` — the locators live in `entries`.
**Two independent actors hit this on the same day**: Scientist A's first parse reported 6 entries
for a 30-entry manifest, and the Orchestrator independently made the identical mistake an hour
later and briefly concluded the *receipt* was over-claiming — the alarming direction, and wrong.
`PMID 42397075` is declared at exactly **6**. **Any locator count of 6 in this repository should be
read twice.**

⚠️ **Cause (b) cannot explain most of the sixteen** — the wrong values are 4, 5, 5, 5, 5, 5, 7, 7,
7, 7, 10, 12, 4, 5, 6, 7, not uniformly 6. **Cause (a) fits all sixteen**, and the 18 correct
declarations fit it too: those are the records whose manifests never grew after the count was
written. Stated as the better-supported explanation, not as a proven one.

## 3 · What is proposed

**(a) `paper_registry_current.md`** — replace each of the sixteen declared counts with the
re-derived value in the table above. **Mechanical substitution; no prose changes.**

**(b) Ship the derivation, since doing it by hand is what failed.** New tool, already written,
routed and regression-backed:

- `framework/scripts/locator_count_crosscheck.py` — read-only; asks one question and no more:
  *does `N` still equal `len(manifest["verbatim_locators"]["entries"])`?* It explicitly does **not**
  ask whether the locators are good, whether they verify, or whether the reading was adequate —
  `deepdive_manifest.py`, `locator_audit.py` and `dossier_quote_audit.py` own those.
- `framework/scripts/test_locator_count_crosscheck.py` — **10 tests, mutation-tested: 3 fail when
  the dict-keys bug is reintroduced.** They pin the dict-versus-list trap; the **anti-vacuity** rule
  (a scan finding no declarations must FAIL, not pass — a guard with an empty population agrees
  with nothing); and the **direction** rule, because understating and overstating are different
  findings and must not be flattened into one number.
- Routed in `framework/scripts/README.md`; `scripts/test_tool_routing.py` passes.

🔵 **The one assertion the tool makes about the future**, and it is deliberately the strict half:
`test_no_declaration_overstates_its_manifest` fails the day any declaration claims **more** depth
than its manifest holds. The sixteen understatements are tracked here as known debt; an
**overstatement** would be a canonical file claiming evidence that does not exist, and that must
fail loudly on the day it appears rather than joining a backlog.

**(c) `dismissal_ledger_current.md` → `🩸 DEFAULTS THAT BIT US`** — one row:

> **D-23** · *"a number copied from another file stays true"* · **Why it is FALSE here:** sixteen of
> thirty-four locator counts in the canonical paper registry had decayed, **all in the same
> direction**, because the manifests they measure kept growing and the copies did not. **And the
> batch explicitly convened to reconcile two of them left both wrong**, because it restated the
> declaration instead of re-deriving it. The repository already knows this shape — it is the same
> argument that made `growth_anchors.py` the only writer of its own constants, and the rule there
> is the rule here: *updating a constraint must cost at least as much as complying with it.*
> **Detection rule:** a number that describes another artefact is **derived, not written**. If it
> must appear in prose, ship the derivation next to it.
> ⚠️ **Numbering:** `D-17` is **reserved** (proposed 2026-09-21, **DEFERRED by the operator**, not in
> the ledger). `D-18`–`D-22` are proposed by this session's other candidates.

## 4 · What is explicitly REFUSED

- ❌ **No claim, status, conclusion or piece of evidence changes.** Sixteen numbers move; the
  readings behind them are untouched and were always what the manifests say.
- ❌ **No automatic rewriting of the registry.** The tool **reports**; it does not edit. A canonical
  file changes through `BATCH_COMMIT`, and a tool that silently corrected the registry would be a
  writer of canonical state, which is precisely what this candidate argues against.
- ❌ **No new gate.** `locator_count_crosscheck.py` blocks nothing. It is a question you can ask,
  routed next to the other questions, in the same read-only style as
  `manifest_queue_id_crosscheck.py`.
- ❌ **No claim that the readings were shallow.** The opposite is true: the readings were **deeper
  than the registry says**, in every one of the sixteen cases.

## 5 · Growth delta

`claims +0 · papers +0 · corpus +0`.

---

*No canonical file edited by this candidate. No reading occurred; no receipt claimed.
Not medical advice.*
