# CC-20260922-SDR-HOMODIMER-PREMISE-01

**Status:** 🔴 **PROPOSED — NOT PROPAGATED**
**Target:** `discovery_ledger_current.md:852` (the `Limiti` bullet of the Q230P structural node) ·
any downstream file repeating the clause
**Change class:** **TAG.** Nothing is deleted, reversed or re-scored — an uncited assertion is given
its correct epistemic label.
**Review floor:** R2.
**Source:** Scientist B's query census in
[`q230p_structural_mechanism_20260922.md`](../../analysis/q230p_structural_mechanism_20260922.md),
verified against the ledger text by the Orchestrator.
**BLOCK-1:** no molecule, no dose, no route. Nothing here is medical advice.

---

## 1 · The defect

`discovery_ledger_current.md:852` reads, inside a limitations bullet:

> *"relSASA e SSE sono calcolati su un **monomero**, ma WWOX **omodimerizza via SDR** e l'interfaccia
> non è modellata"*

🔴 **The clause "WWOX omodimerizza via SDR" carries no source, no PMID, no wikilink and no epistemic
tag.** It is stated as background fact inside a caveat — which is the least visible place in a
document for an unsupported premise to sit, because a reader checking the caveat is checking the
*limitation*, not the *claim inside it*.

## 2 · What the search found

Fully-expanded PubMed queries, OR blocks checked **term-by-term** against the returned
`query_translation` (trap **(f)**), with the positive control `WWOX AND Gln230` firing on PMID
29808465:

| query class | result |
|---|---|
| `WWOX AND (dimerization OR …)` | **1 record** — and it is **p-WWOX/p-p53 *HETERO*-dimers** (PMID 39894307) |
| `WWOX AND ("self-association" OR "homo-dimer" OR "SEC-MALS" OR …)` | **2 records — both about TIAF1 and Zfra**, not WWOX |

> **No published source establishing that WWOX homodimerises through its SDR was found.**

⚠️ **Bounded as a query census, not as proof of absence.** `[All Fields]` **cannot see Methods or
supplements** — trap **(e)**, measured at a **100% miss rate in this gene**. So the correct label is
`PREMISE: UNVERIFIED`, **not** *false*, and **not** `NOBODY_LOOKED`.

## 3 · Why it matters more than a missing citation

🔴 **The premise was amplified, by me, into a therapeutic fork.** I wrote it into
`gln353_gln354del_structural_adjudication_20260922.md` § 9 as established, built the chain
*interface-disrupting ⇒ aggregation ⇒ **a boost is actively dangerous*** on it, and **reported that
fork to the Operator as "the single structural fact that would flip the sign of the reopened
upregulation axis."** An uncited clause in a caveat became a load-bearing therapeutic consideration
in two files and one operator report.

🟢 **And the irony is that the question it framed was answerable without it.** `Gln230`'s SASA in the
free monomer is **0.00 Å²** — independently re-measured by the Orchestrator with a Shrake–Rupley
implementation — and an interface residue must satisfy `SASA_monomer > 0` to be buried by a partner.
**So Q230 is excluded from any interface, whatever the topology**, and the fork's premise never
needed to be settled for Q230. *(It does still matter for Gln353/Gln354, measured at **30.01** and
**38.71 Å²** — those cannot be excluded.)*

## 4 · Proposed edits

1. **`discovery_ledger_current.md:852`** — replace the bare clause with: *"…ma **si assume** che WWOX
   omodimerizzi via SDR (🔴 `PREMISE: UNVERIFIED` — nessuna fonte pubblicata trovata; l'unico record
   di dimerizzazione è **etero**-dimero p-WWOX/p-p53, PMID 39894307) e l'interfaccia non è
   modellata."*
2. **Add a `REVIVAL_TRIGGER`:** any published SEC-MALS, native-PAGE, crosslinking, analytical
   ultracentrifugation or structural evidence of WWOX self-association, **or** a deposited WWOX
   multimer.
3. **Do NOT delete the limitation itself.** The monomer caveat on relSASA/SSE is **correct and
   still binding** — only its justifying clause is unsourced.

## 5 · What this candidate does NOT do

- ❌ Does **not** assert WWOX is monomeric. Unverified is not refuted.
- ❌ Does **not** re-score the Q230P folding interpretation, which rests on geometry measured in the
  monomer and is unaffected.
- ❌ Does **not** remove the Gln353/Gln354 monomer limitation — their SASA is non-zero and the
  limitation stands with numbers attached.
- ❌ Does **not** touch `DL-MOL-010`, `HYP-08`, or the G372R negative-control design in the same node.

## 6 · Verification before propagation

1. 🔴 **Trace the clause to its origin** — a prior session, an inherited review sentence, or an
   inference. B named this as *"the cheapest fix in the whole node: minutes of work, and it re-rates
   several downstream files."* **Not yet done.**
2. Re-run the census with a **Methods-reaching** surface (full texts, not `[All Fields]`), because
   trap (e) makes the literature half of § 2 weak by construction.
3. Enumerate every downstream file repeating the clause, so the tag propagates with it.

---

## WAVE-2 READINESS (2026-09-27)

**Actor:** ACTOR_ID `scientist`, wave-2 package `splice_sdr` · **Verdict: `READY_MINOR`.**
**`context_policy` declared: `QUESTION_DRIVEN`.** The ledger clause and this candidate were held while
the source was reopened; the question was narrow — *does `PMID 24308844` support SDR-mediated WWOX
self-association, and about which domain does it speak* — and `registry_records.py` was the only route
to LEGEND's own records.

### What was done (not a note about it)

1. 🔴 **The source was re-read first-hand.** `files/fulltext/PMID24308844_Schuchardt2013_PMC.xml` was
   **absent from this checkout** (evidence locality: `files/` is gitignored) and was re-acquired by
   `efetch db=pmc id=3906126`; the re-acquired bytes reproduce the manifest's recorded
   `sha256 00da56df985d59b873d8ceea546fdb870138201aaa8c3e22badec660c30581ce` **exactly**, so no new
   artifact entry was needed.
2. **Two verbatim locators APPENDED** to `deepdive_manifests/PMID24308844.json` as **entries 20–21**
   (nothing earlier renumbered or altered), verified by
   `deepdive_manifest.py --pmid 24308844 --verify-artifacts` with **no `BLOCK` on either**:
   - entry 20 — *"Our data indicate that WW domains alone and in the context of WW1–WW2 tandem module
     predominantly adopt a monomeric conformation in solution."*
   - entry 21 — *"Finally, the possibility that the WW1–WW2 tandem module self-associates into a dimer
     or an higher-order oligomer to adopt quaternary structure cannot be ruled out either."*
3. 🎯 **This closes §6 item 2 more sharply than the census could.** The paper's self-association
   experiment uses **WW1, WW2 and the WW1–WW2 tandem** — **the SDR domain is not in it at all** — and
   what it reports is a **predominantly monomeric** solution state. So the local corpus does not merely
   lack support for *"omodimerizza via SDR"*: the one paper that measured WWOX self-association measured
   a different construct and found monomer. The `WW1` shoulder (entry 1, captured in 2026-08 for another
   purpose) is disclaimed by its own authors at 100–200 µM.
4. **§6 item 1 (origin) is answered from git:** the clause enters at the public-edition import
   (`a2e0dd0`, 2026-07-26) — **inherited, with no source at any point in this edition's history**, which
   is why no citation was ever dropped: there never was one.
5. ⚠️ **§4's proposed wording is corrected before it lands.** *"l'unico record di dimerizzazione è
   etero-dimero p-WWOX/p-p53"* is **inaccurate** — a homodimerisation record exists, for `WW1`, negative
   and concentration-dependent. The replacement text below carries it.
6. **Receipt prepared, NOT recorded** (the ledger is a hash chain and other packages run in parallel):
   `receipts_pending/splice_sdr_24308844_1.json` — `FTR-20260927-24308844-02`,
   `partial_fulltext_read`, `reread_reason: new_question_outside_prior_coverage`,
   prior `FTR-20260810-24308844-01`.
7. **Declared gap, PRE-EXISTING and not caused by this session:** the manifest's five figure artifacts
   (`nihms547377f2–f6.jpg`) do not exist in this checkout and cannot be re-acquired — the PMC CDN
   answers a bot challenge and serves HTML under a `.jpg` name (fetched, inspected, deleted rather than
   persisted). `--verify-artifacts` therefore reports the same five `BLOCK`s at `HEAD` as after this
   append; verified by running the validator on the stashed tree.

### Exact operation list for `batch_commit.py propagate`

**File:** `disease-models/wwox/research/discovery_ledger_current.md` (research ledger, record-scoped;
the `Limiti` bullet of the `Q230P` structural node, line 868 in this tree — the candidate header's
`:852` is stale and is corrected here)
**Record:** the `DL-MECH-037` / `Q230P` structural node · **Op:** `replace-within`

- **old text (verbatim from the current file):**
  `relSASA e SSE sono calcolati su un **monomero**, ma WWOX **omodimerizza via SDR** e l'interfaccia non è modellata`
- **new text:**

```text
relSASA e SSE sono calcolati su un **monomero**, e **si assume** che WWOX omodimerizzi via SDR (🔴 `PREMISE: UNVERIFIED` — clausola ereditata dall'import di edizione pubblica `a2e0dd0`, senza fonte in tutta la storia di questa edizione; nessuna fonte pubblicata trovata al censimento 2026-09-22. L'unico record di **omo**dimerizzazione nel corpus locale riguarda **WW1, non SDR**, è **negativo** — *"predominantly adopt a monomeric conformation in solution"* — ed è dichiarato non fisiologico dagli autori stessi a 100–200 µM (`PMID 24308844`, locator 20–21); l'unico record di dimerizzazione positivo è un **etero**-dimero p-WWOX/p-p53, `PMID 39894307`), e l'interfaccia non è modellata. `REVIVAL_TRIGGER`: qualsiasi SEC-MALS, native-PAGE, crosslinking, ultracentrifugazione analitica o struttura depositata che mostri self-association di WWOX, **o** un multimero WWOX depositato
```

**The limitation itself is NOT deleted** (§4 item 3): the monomer caveat on `relSASA`/`SSE` stands, and
for `Gln353`/`Gln354` (SASA 30.01 / 38.71 Å²) it stands with numbers attached.

### Downstream files repeating the clause (§4 item 3 / §6 item 3) — enumerated, NOT edited here

`analysis/wwox_missense_stability_census_20260922.md` (:252, :621) ·
`analysis/q230p_structural_mechanism_20260922.md` (:548) ·
`analysis/gln353_gln354del_structural_adjudication_20260922.md` (:308) ·
`research/OPERATOR_DECISION_PACKET_6_20260922.md` (:67, :69) ·
`analysis/REREAD_schuchardt2013_sdr_homodimer_20260922.md` (:31).
Each already quotes the clause **as the ledger's text under examination**, not as its own assertion, so
none carries the defect once the ledger line is tagged. **No edit is owed to them**, and that is a
change from §4 item 3's assumption — recorded rather than silently dropped.

### What is still pending after this section

Only §6 item 2's **Methods-reaching re-census** (trap (e)): a corpus-wide, full-text search for WWOX
self-association evidence in Methods and supplements. It cannot change the tag — `UNVERIFIED` is
already the weakest claim compatible with a negative census — so it gates nothing.
