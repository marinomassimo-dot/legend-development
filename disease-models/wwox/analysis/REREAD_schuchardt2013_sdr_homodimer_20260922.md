# RECURSIVE RE-READ — Schuchardt 2013 (`PMID 24308844`) under a question its first reader did not have

> **Discovery-space artefact.** `HYPOTHESIS ≠ CLAIM`. Touches no `*_current.md`, no registry, no
> ledger, no receipt chain, no state manifest. No `BATCH_COMMIT`.
> **Not medical advice.** Reference WWOX-DEE genotype class, never an individual. No molecule, dose
> or route. Alleles and domains are never pooled.
> **Actor:** Orchestrator · **Date:** 2026-09-22 · Primitive: `recursive_reread` + `adversarial_verify`

---

## 0 · 🔴 HONEST PROVENANCE, STATED FIRST

**This re-read was NOT pre-registered.** It was found while adversarially verifying a Scientist's
hand-back, and the question formed *after* the artefact was open. By this method's own standard
that makes it **weaker evidence than a pre-registered cycle**, and it is recorded at that strength.
Writing it up as though the question came first would be precisely the post-hoc narration
`preregister_prediction` exists to prevent — and the temptation was real, because the result is
tidy.

---

## 1 · The two questions

| | Question | When |
|---|---|---|
| **Q1** | *What does this paper establish about WWOX's engagement partners and PPxY/PY-motif binding?* | original read — `partial_fulltext_read`, `reading_state.md:67` |
| **Q2** | *Does anything in our corpus actually support the assertion that **WWOX homodimerises via its SDR**?* | today |

**Why Q2 exists now.** `discovery_ledger_current.md:852` carries, inside a `Limiti` bullet:

> *"relSASA e SSE sono calcolati su un **monomero**, ma WWOX **omodimerizza via SDR** e l'interfaccia
> non è modellata"*

🔴 **No source, no PMID, no wikilink, no epistemic tag** — verified at source this session.
`CC-20260922-SDR-HOMODIMER-PREMISE-01` already proposes tagging it. Q2 asks the next question the
tag does not answer: *is it true, and does our own corpus say anything at all?*

---

## 2 · What the re-read returned

`PMID 24308844` (Schuchardt 2013) carries a `verbatim_locator` that the Q1 reading captured for a
different purpose entirely:

> **Snippet:** *"we believe that the propensity of WW1 domain to homodimerize is unlikely to be
> physiologically relevant"*
> **Anchor:** Results and Discussion, analytical light-scattering paragraph
> **Reader's proposition (Q1):** *"A self-declared artefact of concentration: the dimerisation the
> light scattering sees is called probably irrelevant by the authors themselves, because the assay
> required 100–200 µM."*

**Three separations, and all three matter:**

| The ledger's premise | What the corpus actually holds |
|---|---|
| homodimerisation **via the SDR** | the observation is of **WW1** — a different domain |
| stated as **background fact** | the authors call it **"unlikely to be physiologically relevant"** |
| used to caveat a structural calculation | it is a **concentration artefact**, requiring 100–200 µM |

🎯 **The only homodimerisation evidence in the local corpus concerns the wrong domain, is
explicitly disclaimed by its own authors, and is an artefact of concentration.**

---

## 3 · 🔴 What this does NOT establish — the bound is the whole discipline

**It does not show that WWOX fails to homodimerise through its SDR.** That would be the exact error
this session has already committed twice: reading *absence in our corpus* as *absence in the
literature*. The scoped statement is:

> *No support for SDR-mediated WWOX homodimerisation was identified in this repository
> (`FILE TYPE` Markdown + JSON · `DOCUMENT CLASS` manifests, ledgers, analysis files ·
> `SOURCE SCOPE` repository only, **not** the published literature ·
> `SOURCE DEPTH` `partial_fulltext_read` for `PMID 24308844`). The nearest local evidence concerns
> **WW1**, is **negative**, and is **concentration-dependent**.*

`PMID 24308844` is `partial_fulltext_read`, not complete — an SDR observation could sit in a part
not read.

---

## 4 · Consequence, at exactly the strength the evidence allows

The premise was doing **load-bearing work as a limitation**: it weakened the monomer `relSASA
0.000` calculation at residue 230 by asserting an unmodelled interface. If SDR homodimerisation is
unsupported, **that limitation is weaker than stated**, and the interface-exclusion argument at
residue 230 is correspondingly *less* qualified than the ledger implies.

🔴 **This cuts toward the structural argument, which is exactly why it needs the tightest bound.**
A finding that flatters the current model is the one most likely to be waved through. It is
recorded as: *the caveat is unsupported in our corpus*, **not** *the caveat is false*.

**Effect on the existing candidate.** `CC-20260922-SDR-HOMODIMER-PREMISE-01` is strengthened from
*"uncited assertion"* to *"uncited assertion whose nearest local evidence concerns a different
domain and points the other way."* No change is proposed to the candidate here — it remains
Operator-gated, and this file is analysis only.

---

## 5 · Grade

**`NEW CONNECTION`** — an already-read paper answered a question its first reader was not asking,
and the answer bears on a premise in a different file.

Not `EXPERIMENT-CHANGING`: no experiment changes, because the decisive test
(AlphaFold-Multimer on WWOX ×2, ΔSASA at residue 230) is **not executable in this deployment** —
`tool_preflight` reports `git` and `flock` present, all other tooling absent, with egress blocked.

**Effect class:** `FOUND NEW CONNECTION` + `CREATED FOLLOW-UP`.

**Method note.** The value sat in a locator captured for an unrelated purpose — the third time this
session that a re-read's yield came from *the part of the paper the first reader's question made
irrelevant*. That is now three instances of the same pattern, which is the strongest evidence
`recursive_reread` has.
