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
