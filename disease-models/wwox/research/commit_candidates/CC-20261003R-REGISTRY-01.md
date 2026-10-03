# COMMIT CANDIDATE — CC-20261003R-REGISTRY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist R), intake wave 5 2026-10-03, branch `task/sci-R-33914858`.
**Purpose:** give the one PMID this reading handled a structured registry landing, so that no
completed reading sits in the ledger without a registry presence (`ORPHAN_COMPLETE_READ` is what
blocks `BATCH_COMMIT` when one does).
**Not medical advice.**

## Does this record need a landing? — measured, not assumed

| PMID | Registry presence today (`registry_records.py get --pmid 33914858`, commit `d6db8d578021`) | Receipt prepared | Landing needed |
|---|---|---|---|
| 33914858 | `PAPER 004` (integrated, myelination anchor) · duplicate identity `CORPUS-STUB-087` on the same DOI · `LIT-0110` (corpus placeholder, `discovered`) · linked from `CLAIM 003` and `CLAIM 015` · queue entry `FT-044` | `FTR-20261003-33914858-03` (`scratchpad/receipts_pending_w5/sciR_33914858_1.json`) | **No new record.** Enrichment of `PAPER 004` and `FT-044` is in `CC-20261003R-ARTEFACT-DEBT-01`; the duplicate identity and the tracking-log placeholder are addressed here |

**No new `PAPER`, `LIT` or `CLAIM` record is proposed by this candidate.** The reading added no new
paper to the corpus: the multi-hop enumerated 64 references, found 29 gene- or model-direct, and
**all 29 already have a registry presence** (checked one by one with `registry_records.py get
--pmid`); 25 of them already carry at least one read receipt. The four without one — PMID 10786676,
PMID 15026124, PMID 25411445, PMID 19465938 — are reading debt against records that already exist,
not missing records.

Next free numbers re-measured with `registry_records.py catalog` at commit `d6db8d578021`: highest
`PAPER 150`, highest `CLAIM 044`, highest `LIT-0443`, highest `FT-192`. 🔴 **Provisional** — several
actors are landing in parallel today, and the propagating batch must re-measure.

## Change class

**MINOR.** One duplicate-identity retirement to a pointer (nothing deleted; §21d reserves deletion of
unique material) and one tracking-log status correction. No claim is created or changed here.

## Ordering

Receipt `FTR-20261003-33914858-03` must be appended before any of this propagates.
`CC-20261003W4-B-REGISTRY-01` already proposes the same `CORPUS-STUB-087` retirement from wave 4; if
both are in the queue, **propagate that one and drop this op** — they must not both apply, and the
wave-4 text is the earlier claim on it.

## Op list — `paper_registry_current.md` (record-scoped; **dry run NOT executed**)

```json
[
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-087",
  "old": "**Status:** not_processed\n**Registry role:** corpus placeholder only\n**Claim links:** none\n**Next action:** screening / triage required",
  "new": "**Status:** superseded — identità duplicata\n**Registry role:** puntatore storico; il record vivo di questo DOI è [[paper_registry_current#PAPER 004]]\n**Claim links:** none\n**Next action:** nessuna. Lo stesso DOI (10.1093/brain/awab174) era portato da due record di identità, e un PMID con due identità è ciò che rende un lavoro contabile due volte; la nota di `PAPER 004` lo segnalava dal 2026-07-05. Risolto il 2026-10-03 con `CC-20261003R-REGISTRY-01` (oppure, se propagato prima, con `CC-20261003W4-B-REGISTRY-01`: i due non vanno applicati entrambi). Il testo originale dello stub è conservato sopra; nulla è cancellato."
 }
]
```

## Op list — `literature_tracking_log_current.md` (record-scoped; **dry run NOT executed**)

```json
[
 {
  "op": "replace-within",
  "id": "LIT-0110",
  "old": "**Status:** discovered\n**Primary pathway:** unassigned",
  "new": "**Status:** processed — il lavoro è `PAPER 004`, letto integralmente il 2026-10-03 (ricevuta `FTR-20261003-33914858-03`, `partial_fulltext_read`: video supplementari non visionati)\n**Primary pathway:** P4 — myelination / white matter"
 },
 {
  "op": "replace-within",
  "id": "LIT-0110",
  "old": "**Next action:** screening and tier assignment\n**Flags:** corpus placeholder / not yet screened",
  "new": "**Next action:** nessuna — il record vivo è [[paper_registry_current#PAPER 004]]; questa riga resta come traccia di scoperta\n**Flags:** corpus placeholder risolto 2026-10-03 (`CC-20261003R-REGISTRY-01`)"
 }
]
```

🔴 **No dry run was executed** — this worktree's brief forbids touching the four current files in any
mode. Each `old` string was measured unique **within its own record** by reading that record through
`registry_records.py get --pmid 33914858` at commit `d6db8d578021`. The propagating batch re-measures
and renumbers before `--apply`.

## What this candidate deliberately does NOT propose

- No new `PAPER` record: this paper already has one, and a second would recreate the duplicate
  identity this candidate retires.
- No change to `CLAIM 003` or to any claim: those are in `CC-20261003R-OKO-STRENGTH-01` and
  `CC-20261003R-CARRIER-WORDING-01`.
- No queue entry for the four unread gene-direct references: they already have registry records, and
  queueing is a triage act this reading did not perform.

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. The paper this candidate lands is the neuronal-deletion study whose own abstract states the myelin and excitability findings | Wwox-mutant mice exhibited reduced maturation of oligodendrocytes, reduced myelinated axons and impaired axonal conductivity | PMID 33914858, Abstract, journal page 3061, `files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.pdf` PDF page 1 rendered at 110 dpi
2. The paper's reagents and primers live in a supplementary table, which is why the deposited archive had to be opened to audit them | All antibodies and primer sequences used in this study and the related details are provided in Supplementary Table 3. | PMID 33914858, Materials and methods, Immunofluorescence, journal page 3063, same PDF, page 3 rendered at 110 dpi
