# COMMIT CANDIDATE — CC-20261003W4-B-MYELIN-CELLAUT-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 4 2026-10-03, branch `task/sci-B-20261003w4`.
**context_policy:** `SOURCE_FIRST` for the preprint; `QUESTION_DRIVEN`, declared, for PMID 33914858,
whose standing receipt had to be read before the source (see `research/intake_wave_20261003w4_B.md` § 1).
**Not medical advice.** Class-level statements about published models only.

## Target

`disease-models/wwox/registries/claim_registry_current.md` · `CLAIM 003` — one appended paragraph to
the evidence-boundary section of a **`consolidated baseline`** claim. The claim's `Status`, `Type`,
`Summary`, `Transferability` and `Source` lines are **not** touched.

## Why

`CLAIM 003`'s own evidence boundary names the experiment that would settle its open half:

> *«Non promuovibile senza una delezione o un rescue Olig2/CNP-specifici.»*

That experiment now exists. An **Olig2-Cre conditional deletion of *Wwox*** is reported in a bioRxiv
preprint (PPR1124524, doi 10.1101/2025.11.22.689900, posted 2025-11-24, read 2026-10-03,
`files/fulltext/PPR1124524_Abudiab2025_bioRxiv.pdf`). 🔴 **It is not peer reviewed, it is from the same
senior laboratory as the paper `CLAIM 003` rests on, and it therefore changes nothing about the claim's
status.** What it does change is that the condition is no longer *unaddressed*, and the next reader must
not re-derive that from scratch — nor mistake an unreviewed result for a discharge.

The scientific content is also narrower than "the oligodendrocyte requirement is confirmed":

- the oligodendroglial deletion gives **no baseline hypomyelination** — myelinated axons per field
  117.6 ± 12.5 vs 125.1 ± 9, P = 0.22 — only subtly thinner myelin;
- the phenotype appears **only under challenge**: ageing to 18 months, and cuprizone remyelination;
- demyelination itself is **equal between genotypes**; the deficit is in repair;
- the preprint states that it does not contradict the neuronal-deletion result and keeps a
  non-cell-autonomous contribution open.

So the two requirements are **complementary and differently timed**, not rivals, and the developmental
hypomyelination of WWOX-DEE remains attributed to the neuronal route.

## Change class

**MINOR.** It adds a bounded, source-labelled paragraph to an evidence-boundary section and narrows
nothing: no status change, no type change, no reversal, no removal. 🔴 It nonetheless touches a
`consolidated baseline` claim's record, so **`legend-locator-audit` is OWED on the triples below before
propagation**, and the batch that propagates it must say that the audit ran.

## Ordering

Receipts `FTR-20261003-33914858-02` and `FTR-20261003-PPR1124524-01` must be in the ledger before this
candidate propagates, so that no record cites a receipt the ledger does not hold. They are prepared,
not recorded: `scratchpad/receipts_pending_w4/sciB_33914858_1.json`,
`scratchpad/receipts_pending_w4/sciB_PPR1124524_1.json`.

## Op list — `claim_registry_current.md` (record-scoped; **dry run NOT executed**, see note)

```json
[
 {
  "op": "replace-within",
  "id": "CLAIM 003",
  "old": "Non promuovibile senza una delezione o un rescue Olig2/CNP-specifici.",
  "new": "Non promuovibile senza una delezione o un rescue Olig2/CNP-specifici. 🔴 **Quella delezione ora esiste, e non discharge nulla (2026-10-03, `CC-20261003W4-B-MYELIN-CELLAUT-01`).** Un preprint bioRxiv **non sottoposto a peer review** (PPR1124524, doi 10.1101/2025.11.22.689900, v1 2025-11-24, letto 2026-10-03, ricevuta `FTR-20261003-PPR1124524-01`) riporta una delezione condizionale Olig2-Cre di *Wwox*. Un preprint non alza mai lo stato di una claim, e il laboratorio è **lo stesso** di `PAPER 004`: non è un osservatore indipendente. Nel merito il risultato è più stretto di «la funzione oligodendrocitaria è confermata»: al basale la delezione oligodendrogliale **non** produce ipomielinizzazione (assoni mielinizzati per campo 117.6 ± 12.5 vs 125.1 ± 9, P = 0.22; solo mielina lievemente più sottile), il fenotipo emerge **solo sotto sfida** (invecchiamento a 18 mesi; rimielinizzazione dopo cuprizone, con demielinizzazione uguale fra i genotipi), e gli autori stessi scrivono che il loro dato non contraddice la delezione neuronale e lasciano aperta una componente non-cell-autonoma. Le due richieste sono quindi **complementari e di tempi diversi**; l'ipomielinizzazione dello sviluppo resta attribuita alla via neuronale. Condizione per promuovere: pubblicazione peer-reviewed di quel lavoro **e** una replica da un laboratorio indipendente, oppure un rescue oligodendrocita-specifico."
 }
]
```

🔴 **The dry run was not executed and must be run by the propagating batch.** This candidate was
prepared in a worktree whose brief forbids touching the four current files; `record_scoped_edit.py` was
therefore not run even in dry mode against them. The `old` string was measured unique **within
`CLAIM 003`** by reading the record through `registry_records.py get --id "CLAIM 003"` at commit
`296cd5ba5596`; a batch must re-measure it, because `CLAIM 003` has been edited by earlier batches and
may be edited again before propagation.

## What this candidate deliberately does NOT propose

- No change to `CLAIM 003`'s `Status`, `Type` or `Summary`.
- No new claim for the oligodendroglial requirement. On a preprint alone that would be a claim built on
  a source that cannot support one.
- No change to `PAPER 005`'s reading, which supplies the "incomplete rescue" half of the boundary.

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. An oligodendroglial-lineage conditional deletion of *Wwox* exists and is driven by Olig2-Cre on a floxed allele | Wwox conditional ablation from OPCs was achieved through crossing Wwox flox/flox mice with Olig2-Cre mice | PPR1124524, Methods, "Wwox ablation", `files/fulltext/PPR1124524_Abudiab2025_bioRxiv.pdf`
2. At baseline that deletion does not reduce the number of myelinated axons | a subtle reduction in myelin thickness in O-KO mice with no apparent changes in the number of myelinated axons (O-CTR: 117.6 ± 12.5 vs. O-KO: 125.1 ± 9 per FOV; P = 0.22) | PPR1124524, Results, "WWOX deficiency causes subtle myelination defects in vivo", same artefact
3. Both genotypes demyelinate equally; the difference is in repair | Both genotypes exhibited comparable demyelination, confirmed by reductions in MBP immunoreactivity and Luxol fast blue staining | PPR1124524, Results, cuprizone section, same artefact
4. The preprint does not present itself as contradicting the neuronal-deletion result | While previous studies suggest that neuronal deletion of WWOX leads to hypomyelination via a non-cell autonomous mechanism, our data demonstrate that oligodendroglia-specific deletion results in a distinct phenotype | PPR1124524, Discussion, second paragraph, same artefact
5. The preprint keeps a non-cell-autonomous contribution open | It is therefore possible that WWOX can also affect the remyelination potential of mature oligodendrocytes, and that non-cell autonomous processes may further exacerbate remyelination failure | PPR1124524, Discussion, third paragraph, same artefact
6. In the neuronal deletion the myelin deficit is large and is carried by the authors' own counts | The number of myelinated axons (S-Control, average = 180 ± 40, S-KO, average = 55 ± 35) in corpus callosum and unmyelinated axons (S-Control, average = 55 ± 20, S-KO, average = 270 ± 60) in optic nerve is counted per field of view | PMID 33914858, Results, printed page 27 of 48 of `files/fulltext/PMID33914858_Repudi2021_OUP_browserprint.pdf`, rendered at 140 dpi
7. In the neuronal deletion the oligodendrocytes are not dying | no significant oligodendrocyte cell death was observed in S-KO tissues when stained for CC1 and cleaved caspase 3 | PMID 33914858, Results, printed page 26 of 48, same artefact
