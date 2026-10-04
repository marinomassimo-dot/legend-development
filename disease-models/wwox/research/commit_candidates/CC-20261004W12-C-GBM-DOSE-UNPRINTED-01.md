# CC-20261004W12-C-GBM-DOSE-UNPRINTED-01 — the one-of-four GBM exception cannot be checked against the level of WWOX achieved, because that level is published only as a colour

- **Wave:** intake wave 12, 2026-10-04, Scientist C (RE-READ wave)
- **context_policy:** SOURCE_FIRST — the census and the supplement were read before CLAIM 011 was
  opened.
- **Target record:** `CLAIM 011` in `disease-models/wwox/registries/claim_registry_current.md`
  (status `flagged for review`, **not** `consolidated baseline`)
- **Change class:** **MINOR.** It adds a measured absence to an existing `PREMISE_TAG` block,
  narrows nothing, reverses nothing, demotes no evidence, and changes no dose figure. Blind-audit
  triples are supplied anyway, because the target is a claim record.
- **Source read:** PMID 37781246 (DOI 10.3389/fnins.2023.1260409). Package acquired free from the
  **Europe PMC supplementaryFiles archive for PMC10540236**; artefacts newly declared in
  `deepdive_manifests/PMID37781246.json`, among them
  `files/fulltext/PMID37781246_KK2023_supplement/fnins-17-1260409-g003.jpg` sha256
  `be9cac59a59ce1bf8e3952d437fb1a7ef0dbcfe673d4e948b5ade4a849f2abfb` and
  `…/Table_5.XLSX` sha256
  `0ee14f15f5292a4f91709b090b18e6737125880d5ce2354e7a7a1acf8dac6a5f`.
- **Receipt of the producing reading:** `FTR-20261004-37781246-02` (prepared, not recorded).

## Why

CLAIM 011's `PREMISE_TAG` block cites this paper as one of three sources recording that raising
WWOX is not uniformly benign, and already states correctly that the phenotype is **cited from the
group's preceding paper, not measured there**. The owed figure and supplement surfaces confirm that
attribution by census — `MTT` 0, `BrdU` 0, `transfect` 0 occurrences in the whole article — and add
one thing the record cannot currently say:

- The supplement shows the transduction **worked in all four lines** (`WWOX` is in the
  *«Upregulated in all cell lines»* set of Supplementary Table 5, and in all four cell-line columns
  of Supplementary Table 3), so the one-of-four phenotype is not a failure of overexpression
  elsewhere.
- But the **magnitude** raised per line is encoded in Figure 3A as node colour with **no printed
  value**, and no supplementary sheet carries a per-line WWOX log2 fold-change column. So the
  single question that would discriminate *line-specific biology* from *dose* — was WWOX raised
  higher in the discrepant line? — **cannot be answered from what is deposited**.

That is precisely the shape of the ceiling argument this `PREMISE_TAG` makes, and it is worth one
sentence in the record rather than being rediscovered.

## Exact op

**File:** `disease-models/wwox/registries/claim_registry_current.md`
**Record:** `CLAIM 011`
**Op:** `replace-within` the record.

`old` (verbatim, measured **1 occurrence in `CLAIM 011` and 1 in the whole file**):

```
lentiviral WWOX overexpression increased proliferation in 1 of 4 glioblastoma lines (PMID 37781246, and that phenotype is cited from the group's preceding paper, not measured there)
```

`new`:

```
lentiviral WWOX overexpression increased proliferation in 1 of 4 glioblastoma lines (PMID 37781246, and that phenotype is cited from the group's preceding paper, not measured there — ⚠️ **confermato per censimento e precisato 2026-10-04, `CC-20261004W12-C-GBM-DOSE-UNPRINTED-01`, receipt `FTR-20261004-37781246-02`:** in quell'articolo `MTT`, `BrdU` e `transfect` compaiono **zero** volte e le tre occorrenze di `viabilit` sono frasi narrative sullo studio precedente, quindi **nessun saggio di proliferazione, vitalità o clonogenicità vi è eseguito**; l'eccezione portata riguarda **specificamente la crescita e la formazione di colonie** — *«discrepancies related to colony growth and formation were noticed in one of the above GBM cell lines, i.e., DBTRG-05MG»* — accanto alla frase separata *«proliferative potential after WWOX overexpression was increased only in DBTRG-05MG»*. 🔵 Il supplemento, letto cella per cella, mostra che **la trasduzione ha funzionato in tutte e quattro le linee** (`WWOX` è nel set *«Upregulated in all cell lines»* della Tabella Supplementare 5 e compare in tutte e quattro le colonne di linea della Tabella Supplementare 3), quindi il fenotipo 1-su-4 **non** è un fallimento di sovraespressione nelle altre tre. 🔴 **Ma il LIVELLO raggiunto per linea non è stampato da nessuna parte:** in Figura 3A il log2FC per linea è codificato come colore del nodo senza alcun numero, e nessun foglio delle Tabelle Supplementari 1–7 porta una colonna di espressione o di log2FC di WWOX per linea. **La domanda che distinguerebbe una biologia di linea da una differenza di dose — WWOX era più alto nella linea discrepante? — non è rispondibile da ciò che è depositato**, ed è la stessa assenza di tetto che questo `PREMISE_TAG` argomenta altrove)
```

## Registry records

**None owed.** PMID 37781246 already has registry presence; this candidate creates no record.

## What would falsify it

A per-line WWOX log2 fold-change value printed in any deposited surface of this paper (checkable by
re-reading Supplementary Tables 1–7 cell-wise and Figure 3 at native resolution), or a
quantification in the group's preceding paper that ties the DBTRG-05MG exception to its achieved
WWOX level.

### LOCATOR TRIPLES FOR BLIND AUDIT

1. (This paper performs no proliferation, viability or colony assay of its own and attributes the phenotype to an earlier study | `Our previous research concluded that the anti-GBM activity of WWOX is mainly a consequence of reduced cell viability and invasion` | Results and discussion, introductory paragraph on the GBM literature — `files/fulltext/PMID37781246_KaluzinskaKolat2023_PMC.xml`)
2. (The carried one-of-four exception is specifically colony growth and formation | `discrepancies related to colony growth and formation were noticed in one of the above GBM cell lines, i.e., DBTRG-05MG` | Results and discussion, introductory paragraph on the GBM literature — `files/fulltext/PMID37781246_KaluzinskaKolat2023_PMC.xml`)
3. (WWOX was raised in all four lines according to the deposited supplement | `[spreadsheet attestation - read cell-wise from the workbook XML] In Supplementary Table 5 the sheet headed 'Upregulated in all cell lines' contains a row whose only cell is WWOX; in Supplementary Table 3 the sheet headed 'Genes filtered by variance' carries the four column headers DBTRG-05MG, T98G, U87MG and U251MG and the symbol WWOX appears in each of the four columns.` | Supplementary Table 5, sheet 'Up in all cell lines' block, and Supplementary Table 3, sheet 'Cell-line specific'; read cell-wise from the workbook XML — `files/fulltext/PMID37781246_KK2023_supplement/Table_5.XLSX`)
4. (The achieved magnitude per line is published only as a colour and nowhere as a number | `[figure attestation - pixels cannot be quote-matched] In Figure 3A the WWOX node, like every other node of the network, carries its per-cell-line log2 fold change as split colour halves with no numeral printed on or beside it, and no sheet of Supplementary Tables 1 to 7 carries a per-cell-line WWOX expression or log2 fold-change column.` | Figure 3, panel A, WWOX node; native JPEG inspected and the upper-left quadrant magnified — `files/fulltext/PMID37781246_KK2023_supplement/fnins-17-1260409-g003.jpg`)
