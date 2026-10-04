# COMMIT CANDIDATE — CC-20261003R-ARTEFACT-DEBT-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist R), intake wave 5 2026-10-03, branch `task/sci-R-33914858`.
**context_policy:** `SOURCE_FIRST`.
**Not medical advice.**

## Target

`disease-models/wwox/registries/paper_registry_current.md` · `PAPER 004` (the myelination anchor) —
one appended paragraph recording the artefact that now exists, the two prior findings this artefact
withdraws, and the measurement bounds that belong with the quantities.
`disease-models/wwox/research/full_text_queue_current.md` · `FT-044` — one appended status line,
because that entry still says the reading is suspended for want of a valid text surface.

## Why

Three things changed on 2026-10-03, and all three live in records that currently say otherwise.

**1 · The surface debt is superseded, not discharged.** `PAPER 004` and the wave-4 candidate record
that the publisher HTML named by `FTR-20260923-33914858-01` is absent from the checkout and that its
locators are unauditable. That remains true — but it no longer matters for evidence: the operator
supplied the **typeset article PDF** (sha256
`113522bb09b42a2dc0252bc1d7b112b66e3a68323ab1348c042f0ac8c8e8fa4c`) and the **complete supplementary
archive** (sha256 `cfb264e45a6d6e2d7082853de293431594c8235cf087fbecbd0b3fcf1956c276`), and the
current reading is anchored to those. Nothing canonical now depends on the missing HTML.

**2 · Two recorded findings are withdrawn by the artefact itself.**
- `FTR-20260923-33914858-01` recorded that the legend for Supplementary Fig. 3 was **missing** from
  File009, leaving the neocortical-origin claim without n, ages or depths. File009 in this archive
  has the **same sha256** as the file that receipt names and **does** carry that legend (1125 bursts
  across all layers; 149 / 834 / 142 in three S-KO examples; 100–200 s of recording). The absence was
  a property of that reading's extraction.
- The same receipt recorded an earned zero for a data-availability statement. The article carries
  one — *"The data and code that support the findings of this study are available from the
  corresponding author upon reasonable request"* — which deposits nothing and gives no accession. The
  substance survives; the wording does not.

**3 · The quantities need their unit of analysis beside them.** The counts the registry is about to
gain (180 ± 40 vs 55 ± 35; 55 ± 20 vs 270 ± 60; CC1⁺ halved; OPCs up) all come from **n = 3 animals
per genotype**, while every panel plots 13–15 points and the asterisks are computed over **fields of
view**. And the paper's own fold changes are inflated: "~3.5–4-fold" measures 3.3× from the authors'
averages, "~6-fold" measures 4.9× from them and ~4.2× from the panel. A registry that carries the
numbers without the unit invites the next reader to treat them as animal-level.

One digest discrepancy is recorded and not resolved: `FTR-20260923-33914858-01` names File010.mp4
with a different sha256 from this archive's member. Two byte-level instances exist; the earlier one is
absent, so they cannot be compared.

## Change class

**MINOR.** Appended provenance and bounds on a `PAPER` record and a queue entry. No claim changes, no
status reversal, nothing removed. (The claim-level consequence is in
`CC-20261003R-OKO-STRENGTH-01`.)

## Ordering

Receipt `FTR-20261003-33914858-03` first. If `CC-20261003W4-B-REGISTRY-01` propagates in the same
batch it should go **first**: it rewrites `PAPER 004`'s `**Note:**` anchor, and this candidate
appends after whatever that leaves.

## Op list — `paper_registry_current.md` (record-scoped; **dry run NOT executed**)

```json
[
 {
  "op": "replace-within",
  "id": "PAPER 004",
  "old": "**Wikilinks:** [[claim_registry_current#CLAIM 003]]",
  "new": "**Artefatto e misura, aggiornati il 2026-10-03 (`CC-20261003R-ARTEFACT-DEBT-01`, ricevuta `FTR-20261003-33914858-03`):** l'operatore ha fornito il **PDF tipografico dell'articolo** (17 pagine, sha256 `113522bb09b42a2dc0252bc1d7b112b66e3a68323ab1348c042f0ac8c8e8fa4c`) e l'**archivio supplementare completo** (sha256 `cfb264e45a6d6e2d7082853de293431594c8235cf087fbecbd0b3fcf1956c276`: metodi e nove figure supplementari, due video, tre fogli di calcolo). Il debito sull'HTML dell'editore è **superato, non saldato** — quell'artefatto resta assente, e nulla di canonico vi poggia più. Il layer di testo derivato dal nuovo PDF è **rifiutato** come superficie di citazione (screen del validatore: 24 controlli C0, più le sostituzioni stampabili note di questa rivista), quindi ogni locator dell'articolo è `rendered_text` o `figure` su pagina resa; il testo del supplemento è invece **pulito** allo stesso screen. 🔴 **Due reperti precedenti sono ritirati da questo artefatto:** la legenda della Supplementary Fig. 3, che `FTR-20260923-33914858-01` dichiarava **mancante** da File009, è **presente** nello stesso file con lo stesso sha256 (1125 burst, 149 / 834 / 142 in tre esempi S-KO, 100–200 s) — l'assenza era dell'estrazione, non del documento; e un **data-availability statement esiste** («available from the corresponding author upon reasonable request»), pur senza alcun accession, il che conferma la sostanza del reperto precedente e ne corregge la formulazione. 🔴 **Vincolo di misura su ogni quantità di mielina di questo lavoro:** tutte vengono da **n = 3 animali per genotipo**, mentre ciascun pannello riporta 13–15 punti e gli asterischi sono calcolati **sui campi visivi**, non sugli animali; e i fold change del testo corrente sono gonfiati in una sola direzione — «~3.5–4 volte» misura 3.3 volte sulle medie degli autori stessi, «~6 volte» misura 4.9 volte sulle loro medie e circa 4.2 volte sul pannello a 600 dpi. ⚠️ Discrepanza di digest registrata e non risolta: `FTR-20260923-33914858-01` nomina File010.mp4 con sha256 `2ef48d089be350fb3bef68799c443305b9ca9124ea318066f6a2fad8607ecb3c`, l'archivio attuale con `87ec870a96251af9ee3211d4b7b0599360d1a035c2e1cbd41ca46ced6adf52bd`; l'artefatto precedente è assente e i due non sono confrontabili.\n**Wikilinks:** [[claim_registry_current#CLAIM 003]]"
 }
]
```

## Op list — `full_text_queue_current.md` (record-scoped; **dry run NOT executed**)

```json
[
 {
  "op": "replace-within",
  "id": "FT-044",
  "old": "**Current status:** 🔴 **LETTURA SOSPESA 2026-08-09 — NESSUNA RECEIPT EMESSA.**",
  "new": "**Current status (2026-10-03):** ✅ **LETTO** sull'articolo tipografico e sul supplemento completi forniti dall'operatore — ricevuta `FTR-20261003-33914858-03`, `partial_fulltext_read` (video supplementari campionati a fotogrammi, non visionati), manifest `deepdive_manifests/PMID33914858.json` con validatore `MANIFEST STRICT PASS` e 0 lacune, dossier `fulltext_dossiers/PMID33914858.md` parte 2. La sospensione del 2026-08-09 riguardava una superficie testuale non valida: quella diagnosi **regge** anche sul nuovo PDF (il suo layer di testo è rifiutato dallo stesso screen), e la lettura è stata fatta **sulle pagine rese**, non riparando il testo. Lo storico qui sotto è conservato invariato.\n**Current status storico:** 🔴 **LETTURA SOSPESA 2026-08-09 — NESSUNA RECEIPT EMESSA.**"
 }
]
```

🔴 **No dry run was executed** (this worktree may not touch the four current files, and
`full_text_queue_current.md` is a generated-adjacent registry surface this brief also forbids). Each
`old` was measured unique **within its own record** through `registry_records.py get` at commit
`d6db8d578021`, and must be re-measured by the propagating batch.

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. The supplement contains the legend of Supplementary Fig. 3, with the burst count and the recording window | A total of 1125 bursts were identified across all layers | PMID 33914858, Supplementary Figure Legends, Supplementary Fig 3(C), `files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied_supplement/extracted/awab174-suppl_data/brain-2020-02464-File009.txt`
2. The article carries a data-availability statement that deposits nothing | The data and code that support the findings of this study are available from the corresponding author upon reasonable request. | PMID 33914858, Data and code availability, journal page 3065, `files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.pdf` PDF page 5 rendered at 110 dpi
3. The electron-microscopy quantification rests on three animals per genotype | Graphs represent the myelinated axons (S-Control, n = 2500 and S-KO, n = 1200) in corpus callosum | PMID 33914858, Figure 5 legend panel B, journal page 3071, same PDF, page 11 rendered at 110 dpi
4. The running text states the fold changes the panel does not support | significantly a greater number (6-fold) of unmyelinated axons in optic nerves of S-KO | PMID 33914858, Results, journal page 3069, same PDF, page 9 rendered at 110 dpi
5. The cell counts come from three sections of three mice per genotype | from three independent sections of S-Control (n = 3) and S-KO mice (n = 3) | PMID 33914858, Figure 4 legend panel G, journal page 3070, same PDF, page 10 rendered at 110 dpi

---

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261003_005` · 2026-10-03 · ACTOR_ID `scientist` (Scientist J, batch integrator), under the operator's standing authorisation *«procedi sempre»*
**Operations applied:** 2
**Change class as judged by the batch:** MINOR (§7) — every target's live `Status` was read from the registry before judging.

`PAPER 004` gains the operator-supplied artefact with both digests, the rejection of its derived text layer as a citation surface, the two findings the artefact withdraws, the measurement bound and the unresolved File010.mp4 digest discrepancy; `FT-044`'s suspension is closed with the historic line preserved and `partial full text` added beside `partial_fulltext_read`. 🔴 **One blind-audit NOT_SUPPORTED verdict was repaired by re-sourcing, not by dropping the claim:** the quote offered for *n = 3 animals per genotype* is Figure 5(B)'s legend, whose n = 2500 and n = 1200 are **axons counted, not animals**. The three-animals figure is in the same legend's parts (A) and (C) and in Figure 4(G), so the record now names those and states explicitly that 5(B)'s numbers are axon counts — which strengthens the candidate's own point about the unit of analysis. A second amendment keeps the printed tilde: the text says *∼6-fold*, a declared approximation, so what is recorded is that the approximation rounds in one direction only, not that the authors asserted a point value.

**Nothing above this line was rewritten.**
