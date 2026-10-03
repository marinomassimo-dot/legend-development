# COMMIT CANDIDATE — CC-20261003W4-B-HIF1A-SCOPE-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 4 2026-10-03, branch `task/sci-B-20261003w4`.
**context_policy:** `QUESTION_DRIVEN`, declared — the acquisition-state check for this PMID returns a
standing receipt whose `evidence_basis` states the paper's findings, and it was read before the source.
**Not medical advice.**

## Target

`disease-models/wwox/registries/paper_registry_current.md` · `PAPER 023` (Baryła 2022, PMID 35328751) —
two field-scoped repairs plus an evidence-depth line. `CLAIM 009`, which links to this paper, is **not**
touched: nothing here contradicts it.

## What is wrong or missing now

| Field as it stands | What the source says |
|---|---|
| `**Model/species:** mixed mechanistic / non-CNS direct` | One immortalised **human skin fibroblast line**, 1BR.3.N (ECACC 90020508), under four crossed oxygen × glucose conditions. "Mixed" is vaguer than the design and lets a reader import a second system that does not exist. |
| `**Genotype/model:** WWOX downregulation framework` | **Two** arms. Down: CRISPR/Cas9 sgRNA, puromycin-selected, polyclonal — about 3× lower mRNA and 8.5× lower protein, which the paper calls "KO" throughout. **Up:** lentiviral WWOX cDNA at about 850× mRNA and >700× protein. The up-arm appears in **no LEGEND record at all**. |
| no `**Evidence depth:**` line | A partial receipt has stood since 2026-09-21 and a second, deeper one is prepared. |

The reason this matters to the model rather than to tidiness: the up-arm is the only **re-supply** arm in
the metabolic literature this corpus holds, and it is **not a mirror image of the down-arm**. Medium
lactate rises on WWOX depletion in all four conditions *and also rises* on WWOX overexpression relative
to wild type in two of them; glucose uptake reverses sign with condition in both arms. A lactate or
uptake endpoint therefore cannot be specified as a monotone reporter of WWOX dose in this system, and a
re-supply programme cannot assume that the loss-of-function direction simply inverts.

## Change class

**MINOR** — paper-registry fields and an added evidence-depth line. No claim status, no working-model
block, no reversal.

## Ordering

Receipt `FTR-20261003-35328751-02` (`scratchpad/receipts_pending_w4/sciB_35328751_1.json`) must be in
the ledger before propagation.

## Op list — `paper_registry_current.md` (record-scoped; **dry run NOT executed**, see note)

```json
[
 {
  "op": "replace-within",
  "id": "PAPER 023",
  "old": "**Model/species:** mixed mechanistic / non-CNS direct",
  "new": "**Model/species:** una sola linea di fibroblasti cutanei umani immortalizzati, 1BR.3.N (ECACC 90020508), in quattro condizioni incrociate ossigeno × glucosio [corretto 2026-10-03 da «mixed mechanistic / non-CNS direct» con `CC-20261003W4-B-HIF1A-SCOPE-01`]"
 },
 {
  "op": "replace-within",
  "id": "PAPER 023",
  "old": "**Genotype/model:** WWOX downregulation framework",
  "new": "**Genotype/model:** **due bracci, non uno** [corretto 2026-10-03 da «WWOX downregulation framework» con `CC-20261003W4-B-HIF1A-SCOPE-01`]. (a) perdita: sgRNA CRISPR/Cas9 con selezione in puromicina, policlonale — mRNA circa 3× più basso e proteina circa 8.5× più bassa; il lavoro la chiama «KO» ovunque, ma è un knockdown, e ogni affermazione che eredita da qui la parola knockout eredita una deplezione parziale. (b) ri-fornitura: cDNA WWOX lentivirale a circa 850× mRNA e >700× proteina — sovrafisiologica, e **assente da ogni record LEGEND fino a questa lettura**. 🔴 I due bracci non sono speculari: il lattato nel mezzo sale nella perdita in tutte e quattro le condizioni **e sale anche** nella sovraespressione rispetto al wild type in normossia-normoglicemia e in ipossia-iperglicemia, e l'uptake di glucosio inverte di segno con la condizione in entrambi i bracci. Nessun endpoint di questo sistema è quindi un reporter monotono della dose di WWOX."
 },
 {
  "op": "replace-within",
  "id": "PAPER 023",
  "old": "**Note:** complements PAPER 002 by giving a more focused WWOX/HIF1A axis paper",
  "new": "**Evidence depth:** `partial_fulltext_read` — ricevuta `FTR-20261003-35328751-02` su JATS Europe PMC (PMC8955937), manifest `deepdive_manifests/PMID35328751.json` (7 locator, validatore PASS con `--verify-artifacts`), dossier `fulltext_dossiers/PMID35328751.md`. Parziale per due ragioni dichiarate: i pannelli non sono stati ispezionati come immagini e le Figure S1–S6 **non sono scaricabili** (l'endpoint `supplementaryFiles` di Europe PMC restituisce HTTP 500 per questo PMCID), quindi ogni affermazione sul braccio di sovraespressione poggia su testo corrente che porta i propri numeri. Ricevuta precedente `FTR-20260921-35328751-01`, su un'estrazione testuale che aveva cancellato ogni token in corsivo.\n**Integrity note (2026-10-03, `CC-20261003W4-B-HIF1A-SCOPE-01`):** due saggi della stessa quantità si contraddicono dentro il lavoro e solo uno arriva alla Discussione. La Discussione afferma aumento di HIF1α «together with its translocation to the nucleus»; il blot frazionato riporta la proteina **ridotta nel citoplasma** del knockdown in due condizioni e «We didn't observed WWOX influence on HIF1α protein in nuclear fraction», mentre l'immunocitochimica su cellula intera mostra un aumento nelle due condizioni normossiche. Il positivo robusto del lavoro è il reporter di transattivazione HRE, non il livello proteico e non la traslocazione. Misurato anche un **negativo**: espressione e attività della citrato sintasi non mostrano influenza di WWOX in alcuna condizione, e non esiste respirometria.\n**Note:** complements PAPER 002 by giving a more focused WWOX/HIF1A axis paper"
 }
]
```

🔴 **The dry run was not executed** — the brief forbids this worktree touching the four current files in
any mode. Each `old` string was measured unique **within `PAPER 023`** by reading the record through
`registry_records.py get --id "PAPER 023"` at commit `296cd5ba5596`. The propagating batch re-measures
them and runs the dry propagation before `--apply`.

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. The loss-of-function arm is a partial depletion that the paper calls KO | The relative expression level of WWOX mRNA was three times lower in 1BR.3.N WWOX KO variant in comparison to CONTR, and 850 times higher in 1BR.3.N WWOX OE than WT. | PMID 35328751, Results 2.1, `files/fulltext/PMID35328751_Baryla2022_PMC.xml`
2. Glucose uptake reverses sign between conditions under WWOX loss | We observed that WWOX silencing significantly increased glucose uptake in normoxia normoglycemia and reduced glucose uptake in hypoxia hyperglycemia conditions in the absence of insulin. | PMID 35328751, Results 2.3, same artefact
3. The re-supply arm raises lactate rather than restoring it | Lactate concentration were significantly higher in case of WWOX overexpression in comparison to 1BR.3.N WT cell line in normoxia normoglycemia and hypoxia hyperglycemia | PMID 35328751, Results 2.5, final paragraph, same artefact
4. The oxidative arm was measured and was null | Nonetheless, in our study, citrate synthase expression and activity were tested and we did not observe WWOX influence on it. | PMID 35328751, Discussion, citrate synthase paragraph, same artefact
5. The nuclear translocation asserted in the Discussion was not detected by the blot | We didn’t observed WWOX influence on HIF1α protein in nuclear fraction. | PMID 35328751, Results 2.6.1, same artefact
6. Whole-cell immunocytochemistry reports the opposite direction from the cytoplasmic blot | WWOX downregulation resulted in HIF1α increase in normoxia normoglycemia and hyperglycemia condition (both p < 0.01). | PMID 35328751, Results 2.7, same artefact
7. The paper's own therapeutic language targets WWOX in diabetes and not the brain | However, strategies to normalize glucose metabolism by targeting WWOX may have promise as therapies in the future. | PMID 35328751, Conclusions, final sentence, same artefact
