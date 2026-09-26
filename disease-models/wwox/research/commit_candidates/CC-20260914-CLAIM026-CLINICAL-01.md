# COMMIT CANDIDATE — CC-20260914-CLAIM026-CLINICAL-01

**Actor:** `orchestrator` · **Date:** 2026-09-14 · **Mandate:** `SCIENCE-EXEC-20260914` steps C1 and C3
**Class:** MINOR, one field of one claim · **§21d consultation:** owed before propagation
**Status of the claim:** `in observation` — not consolidated baseline, so no R4 precondition on its fields
Public, disease-level, de-identified. **Nothing here is medical advice.**

## 1 · The defect (C1)

`CLAIM 026` was narrowed in `BATCH_20260914_005 (VPS batch, never on main)`: its Title, Type, Genotype/model relevance,
Transferability, clinical relevance, Summary and Impact now state that the coupling of the trafficking
and metabolic halves is an **untested hypothesis**, on one prey list, one cell line, n = 2, with no
metabolic quantity and no trafficking assay. One field was outside that consulted perimeter and still
reads:

> Non cambia la pratica immediata per il genotipo di riferimento. **Apre un asse di ricerca di alto
> valore:** la disfunzione metabolica WWOX-related potrebbe essere in parte una disfunzione logistica
> endomembranosa, non solo un problema di segnalazione HIF1A.

"Di alto valore" is a value judgement the evidence cannot carry, and it contradicts the claim's own
`Impact on Working Model`, which reads *"hypothesis-generating for P5; no measured refinement"*. A
field that grades a hypothesis the rest of the record declares untested is the overshoot the batch
closed everywhere else.

## 2 · The proposed change

Replace the field with:

> Non cambia la pratica per il genotipo di riferimento. **Genera un'ipotesi, non misurata:** che parte
> della disfunzione metabolica WWOX-related sia di logistica endomembranosa oltre che — `INFERENZA`, e con l'eccezione HIF1α-indipendente registrata in
> [[claim_registry_current#CLAIM 025]] — di segnalazione HIF1A. Nessuna delle due fonti accoppia le due metà, e non vi è misurata né una quantità
> metabolica né una funzione di traffico.

The hypothesis is kept — an under-claim is a defect too — and only its grade is removed.

## 3 · C3 — the VOPP1 point, after `SCI-CONSULT-20260914` found my first answer wrong

🔴 **My first §3 said the three competing mechanisms "live only in the abstracts of `FT-185` to
`FT-189`". That was false, and the consultation caught it.** My measurement searched only
`claim_registry_current.md` and `working_model_current.md`; `paper_registry_current.md` holds **16**
of the VOPP1 mentions and was outside the surface I measured. Verified by me before accepting the
finding: that file does hold 16 occurrences, and `PAPER 095`'s `Note` carries the import sentence
verbatim. Replacement text, as prescribed:

> The three competing mechanisms are **named in canon**, not only in unread abstracts:
> `paper_registry_current.md` `PAPER 095`'s `Note` records that three of the five VOPP1 antecedents
> *"propose mutually competing mechanisms"* and that `FT-187`, *"from which this corpus imports
> VOPP1's lysosomal identity"*, shows only partial co-localisation and casts doubt on the direct
> NF-κB route. Measured on 2026-09-14: that imported identity is **load-bearing in no claim** —
> `CLAIM 026` names "lysosomal" only to deny that any lysosomal-delivery assay exists, and
> `PAPER 032`'s lysosomal / NF-κB / oxidative tokens are the source's own KEGG pathway names. Canon
> presents VOPP1 as a convergent line **for the interaction** (`PAPER 032` + `PAPER 095`, which two
> papers do support) and **not** for any downstream mechanism. **No claim repair is owed. Revival
> trigger:** if any of `FT-185`–`FT-189` is read, or if the trafficking category is ever used to
> license a mechanism, C3 is re-examined at `PAPER 095`'s `Note` first.

**The method limit, recorded so the next census does not repeat it:**

> The 400-character window measured `claim_registry_current.md` and `working_model_current.md` only;
> `paper_registry_current.md` holds 16 of the VOPP1 mentions and was outside it. A co-occurrence
> window also cannot see attribution carried by a **category name** ("endomembrane trafficking
> protein"), which is how this import actually travelled.

## 4 · What this candidate asks the consultation

1. Is the replacement text faithful to the record's own scope, neither over- nor under-claiming?
2. Is the C3 verdict — no repair owed — correct, or does a surface I did not measure present VOPP1's
   downstream mechanism as convergent?

---

## BATCH DISPOSITION — appended by the integrator, append-only

**Status:** **RE-QUEUED** — recovered 2026-09-26 from the VPS backup (`06ee25a`). The VPS batch that disposed of this candidate never reached `main`: re-queued for `BATCH_20260926_ALDAZ`. Identifiers written on the VPS are annotated in place as `(VPS numbering)` / `(VPS batch, never on main)`; full-text queue ids were renumbered (see `disease-models/wwox/research/vps_recovery_20260925/README.md`).
