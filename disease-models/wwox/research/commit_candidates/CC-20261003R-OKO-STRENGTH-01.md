# COMMIT CANDIDATE — CC-20261003R-OKO-STRENGTH-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist R), intake wave 5 2026-10-03, branch `task/sci-R-33914858`.
**context_policy:** `SOURCE_FIRST` — the article and supplement were read in full before `CLAIM 003`
was opened.
**Not medical advice.** Class-level statements about published mouse models only.

## Target

`disease-models/wwox/registries/claim_registry_current.md` · `CLAIM 003` — one sentence appended to
the existing evidence-boundary paragraph of a **`consolidated baseline`** claim. `Status`, `Type`,
`Summary`, `Transferability`, `Source` and every wikilink are untouched.

## Why

`CLAIM 003` is "neuronal WWOX deletion induces **non-cell-autonomous** hypomyelination". The word
*non-cell-autonomous* is licensed, in the source, by the negative result in the oligodendroglial
conditional. With the paper's own pages and its complete supplement in hand, that negative can now be
weighed, and it is thin:

- the O-KO arm consists of weight and survival to about 120 days (O-Control n = 11, O-KO n = 10,
  log-rank P = 1.0), a hind-limb clasping image, and **one unquantified MBP comparison at P17**;
- there is **no** electron microscopy, **no** g-ratio, **no** axon count, **no** CC1 or OPC count,
  **no** electrophysiology and **no** age beyond P17 for the O-KO;
- so a myelin phenotype that is subtle, challenge-dependent or late could not have been detected by
  anything that was done;
- and the authors themselves write that they "cannot exclude the cell autonomous functions of WWOX in
  oligodendrocytes".

Two further bounds belong with it, both from the source: the in-vitro demonstration of neuron→OPC
signalling uses **embryonic dorsal root ganglion neurons from the constitutive null**, not
Synapsin-Cre cortical neurons; and the Synapsin deletion is **incomplete in cortex at transcript
level** (residual *Wwox* normalised counts 172.7 / 187.0 / 331.4 in S-KO cortex against 18.8 / 18.8 /
28.0 in S-KO hippocampus, Supplementary Table 1 per-sample columns), which is expected from
non-neuronal cells in a cortical sample and is never stated — while cortex is where the myelin
intensity quantification is done.

This does **not** reverse the claim. The S-KO hypomyelinates while WWOX is stated to be intact in its
CC1⁺ oligodendrocytes, and that remains the strongest form of the argument. What changes is that the
registry will say how strong the licensing negative is, instead of leaving the next reader to derive
it.

## Change class

**MINOR.** One appended bounding sentence; no status, type, summary or source change; nothing is
reversed or removed. 🔴 It nonetheless touches a `consolidated baseline` claim, so
**`legend-locator-audit` is OWED on the triples below before propagation**, and the propagating batch
must record that the audit ran.

## Ordering

Receipt `FTR-20261003-33914858-03`
(`scratchpad/receipts_pending_w5/sciR_33914858_1.json`) must be in the ledger first. If
`CC-20261003W4-B-MYELIN-CELLAUT-01` propagates in the same batch, it should propagate **before** this
one: it edits the same paragraph's final sentence, and this candidate appends after it.

## Op list — `claim_registry_current.md` (record-scoped; **dry run NOT executed**, see note)

```json
[
 {
  "op": "replace-within",
  "id": "CLAIM 003",
  "old": "Non promuovibile senza una delezione o un rescue Olig2/CNP-specifici.",
  "new": "Non promuovibile senza una delezione o un rescue Olig2/CNP-specifici. 🔴 **Quanto è forte il negativo che autorizza la parola «non-cell-autonoma» (2026-10-03, `CC-20261003R-OKO-STRENGTH-01`, letto sull'articolo tipografico e sul supplemento completi forniti dall'operatore).** Il braccio O-KO di [[paper_registry_current#PAPER 004]] consiste in peso e sopravvivenza fino a circa 120 giorni (O-Control n = 11, O-KO n = 10, log-rank P = 1.0), un'immagine di hind-limb clasping e **una singola comparazione MBP non quantificata a P17**: nessuna microscopia elettronica, nessun g-ratio, nessun conteggio di assoni, nessun conteggio CC1/OPC, nessuna elettrofisiologia e nessuna età successiva a P17. Un fenotipo mielinico lieve, tardivo o dipendente da una sfida **non sarebbe stato visibile** a ciò che è stato fatto, e gli autori stessi scrivono di non poter escludere una funzione cell-autonoma di WWOX negli oligodendrociti. Due vincoli collaterali dalla stessa fonte: la dimostrazione in vitro del segnale neurone→OPC usa **neuroni del ganglio della radice dorsale embrionali del null costitutivo**, non neuroni corticali Synapsin-Cre (n = 4 per condizione, due esperimenti); e la delezione Synapsin è **incompleta nella corteccia a livello di trascritto** (conte normalizzate residue di *Wwox* 172.7 / 187.0 / 331.4 nella corteccia S-KO contro 18.8 / 18.8 / 28.0 nell'ippocampo S-KO, colonne per-campione della Supplementary Table 1), cosa attesa per le cellule non neuronali di un campione corticale e mai dichiarata — mentre la corteccia è dove si quantifica l'intensità di mielina. La claim **non** è rovesciata: il S-KO ipomielinizza mentre WWOX è dichiarato intatto nei suoi oligodendrociti CC1-positivi, e questa resta la forma più forte dell'argomento."
 }
]
```

🔴 **The dry run was not executed.** This worktree's brief forbids touching the four current files in
any mode, so `record_scoped_edit.py` was not run against them. The `old` string was measured unique
**within `CLAIM 003`** by reading the record through `registry_records.py get --id "CLAIM 003"` at
commit `d6db8d578021`. 🔴 It is the **same anchor** `CC-20261003W4-B-MYELIN-CELLAUT-01` edits, so
whichever propagates second must re-measure it against the text the first one left.

## What this candidate deliberately does NOT propose

- No change to `CLAIM 003`'s `Status` (`consolidated baseline` stands), `Type`, `Summary` or `Source`.
- No new claim about an oligodendrocyte-intrinsic requirement: this paper does not test one, and the
  preprint that does is not peer reviewed.
- No change to the fold-change figures in `PAPER 004` — those are in
  `CC-20261003R-ARTEFACT-DEBT-01`.

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. The oligodendroglial conditional's myelin readout is a single unquantified MBP comparison at one age | comparable myelin signal in O-KO compared to O-Control at P17 | PMID 33914858, Supplementary Figure Legends, Supplementary Fig 8(A), `files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied_supplement/extracted/awab174-suppl_data/brain-2020-02464-File009.txt`
2. The oligodendrocyte and astrocyte deletions are followed for survival and weight with small groups and no significance | O-Control, n = 11 and O-KO, n = 10, P-value 1.0, no significance, log-rank Mantel-Cox test | PMID 33914858, Figure 1 legend panels J–O, journal page 3066, `files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.pdf` PDF page 6 rendered at 110 dpi
3. The authors state the negative does not exclude a cell-autonomous oligodendrocyte function | though we cannot exclude the cell autonomous functions of WWOX in oligodendrocytes or astrocytes in other neurological disorders | PMID 33914858, Discussion, journal page 3073, same PDF, page 13 rendered at 110 dpi
4. The in-vitro arm uses dorsal root ganglion neurons from the constitutive null | we performed a co-culture assay of wild-type OPCs with DRG neurons isolated either from wild-type or Wwox-null mice | PMID 33914858, Results, journal page 3071, same PDF, page 11 rendered at 110 dpi
5. The co-culture n is four per condition from two experiments | Results are shown in a box plot from two independent experiments (WT-DRGs + WT-OPCs, n = 4; KO- | PMID 33914858, Figure 6 legend panel D, journal page 3072, same PDF, page 12 rendered at 110 dpi
6. WWOX is stated to be intact in the oligodendrocytes of the neuronal conditional, which is what makes the phenotype non-cell-autonomous by construction | levels of WWOX are maintained in oligodendrocytes (stained with CC1) in S-KO compared to S- | PMID 33914858, Supplementary Figure Legends, Supplementary Fig 1(D), File009 text layer
