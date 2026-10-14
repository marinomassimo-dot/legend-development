# CC-20261004W10-Y-ORGANOID-GLIA-01 — PMID 42397075 contains no oligodendroglial or astroglial measurement, and its one myelin statement is an enrichment term in a neuronal comparison

`context_policy: SOURCE_FIRST` — the panels below were measured against the source before
[[claim_registry_current#CLAIM 003]] and [[claim_registry_current#CLAIM 005]] were opened.
**Change class: MINOR.** This writes an **earned null** into two records and corrects one number
in a third. No claim's `Status`, `Type`, `Summary`, `Transferability` or `Source` moves, and the
cell-autonomy question both claims leave open stays open.

## Why this exists

The glial axis of [[claim_registry_current#CLAIM 003]] (neuronal WWOX deletion induces
non-cell-autonomous hypomyelination) and [[claim_registry_current#CLAIM 005]] (glial activation)
rests entirely on **rodent** work. The only human organoid paper in the corpus that could bear on
it is PMID 42397075, and it is cited in neither. Whether it carries organoid evidence for
oligodendroglia is a question that should be answered by measurement and then closed, so that it
is not re-asked.

**It does not. The answer is an earned null, and it is worth recording precisely because the
paper's own running text sounds as if the answer were yes.**

## What was measured, on `files/fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf`

**Token census over the 36-page body**: `myelin` 3, `oligodendro` 2, `astrocyt` 1, `microglia` 1 —
and four of those seven are in the **reference list**. `OLIG`, `SOX10`, `PDGFRA`, `MBP`, `GFAP`,
`AQP4`, `S100B`, `OPC`: **zero occurrences each**.

🔴 **No glial cell type is annotated.** The clustering yields five labels — `cRG`, `RG`, `oRG`,
`NP`, `Neu` (Fig. 2A, n = 18 007 cells). Glial progenitors are **folded into** the mixed radial-glia
cluster and the authors decline to resolve it: *"of outer RGs (oRGs), cycling RGs (cRGs), and a
mixed population of vRGs, neuroectodermal"* cells and glial progenitor cells. There is no
oligodendrocyte, astrocyte or microglial cluster, and no myelin-protein, g-ratio, axon-count or OPC
measurement anywhere in the paper.

🔴 **The single oligodendrocyte statement is one bar in a gene-set enrichment chart.** The body
writes, of AAV9-WWOX-treated versus untreated WOREE organoids, *"promotion of oligodendrocyte
differentiation and myelination, and synaptic function (Fig. 6D"* and Fig. 6E. Measured at the
panel: the term `oligodendrocyte specification & myelin` is one of four positively enriched terms
at NES ≈ +1.3 in a contrast labelled `WOREE^WWOX+ versus WOREE`, run — the caption says so — **in
neuronal progenitors and neurons**. It is a transcriptional signature read in neurons, in a model
that contains no oligodendrocyte.

🔴 **The same panel moves the biosynthetic substrate of myelin the other way.** Two of the four
*negatively* enriched terms in that same contrast are `cholesterol production inhibition` and
`glycerophospholipid biosynthesis`.

⚠️ **And the caption of the panel does not name the term the running text draws from it.** Fig. 6E's
caption reads *"an increase in OXPHOS and oxidative stress terms in WOREE-WWOX compared to WOREE,"*
and continues with lipid metabolism downregulated.

🔵 **The one oligodendrocyte-lineage number in the paper is in external public data.** Fig. 3B plots
WWOX expression by cell type in a published post-conceptional-week-16 human fetal single-cell
dataset — **not** these organoids: RG highest (median ≈ 0.57), IP ≈ 0.48, ExN/InN ≈ 0.20, Other
≈ 0.14, **Oli ≈ 0.10, Mic ≈ 0.07**, the two lowest of seven. **Transfer limit:** external data at
16 pcw, i.e. **before myelination begins**; an expression gradient, not a requirement test, and
silent about an adult or challenged oligodendrocyte. It neither supports nor refutes a
cell-autonomous oligodendrocyte function.

## Ops

### Op 1 — `claim_registry_current.md`, record `CLAIM 003`, append to the `Evidence boundary`

- `old` (measured unique in `CLAIM 003`):
  `Audit cieco dei locator eseguito prima della propagazione (18 triple Repudi, 18 QUOTE_FOUND, 0 UNVERIFIABLE).`
- `new`:
  `Audit cieco dei locator eseguito prima della propagazione (18 triple Repudi, 18 QUOTE_FOUND, 0 UNVERIFIABLE). 🔵 **Il solo organoide umano del corpus non porta nulla su questo asse, ed è un nullo guadagnato (2026-10-04, \`CC-20261004W10-Y-ORGANOID-GLIA-01\`, intake wave 10).** PMID 42397075 ([[paper_registry_current#PAPER 094]]) — organoidi cerebrali umani da iPSC, knockout isogenico più linee derivate da paziente, riletto a receipt su artefatto ri-acquisito — **non misura alcun oligodendrocita, astrocita, OPC o microglia in nessun genotipo**, e non misura mielina, proteina mielinica, g-ratio né alcun esito di mielinizzazione. Il clustering produce cinque etichette (\`cRG\`, \`RG\`, \`oRG\`, \`NP\`, \`Neu\`; n = 18 007 cellule) e i progenitori gliali sono **inglobati** nel cluster misto di glia radiale, che gli autori dichiarano di non voler risolvere più finemente. Censimento sui token del corpo: \`OLIG\`, \`SOX10\`, \`PDGFRA\`, \`MBP\`, \`GFAP\`, \`AQP4\`, \`S100B\`, \`OPC\` **zero occorrenze ciascuno**. ⚠️ **L'unica frase su oligodendrociti e mielina è un termine di arricchimento, non una misura:** \`oligodendrocyte specification & myelin\` è una barra (NES ≈ +1.3) nel pannello 6E, in un confronto \`WOREE^WWOX+ versus WOREE\` condotto — lo dice la didascalia — **in progenitori neuronali e neuroni**; nello stesso pannello \`cholesterol production inhibition\` e \`glycerophospholipid biosynthesis\`, substrato biosintetico della mielina, sono fra i termini **negativamente** arricchiti, e la didascalia del pannello non nomina affatto il termine che il testo corrente ne trae. 🔵 L'unico dato di lignaggio oligodendrocitario è in **dati pubblici esterni** (Fig. 3B, single-cell fetale umano a 16 settimane post-concezionali, non questi organoidi): WWOX è **massimo nella glia radiale e minimo in \`Oli\` e \`Mic\`**, i due più bassi di sette. **Limite di trasferimento:** gradiente di espressione a un'età che precede la mielinizzazione, in dati di terzi — non un test di necessità, e muto sull'oligodendrocita adulto o sotto sfida. **Nulla di tutto questo tocca l'autonomia cellulare**, che resta non misurata in ogni modello che LEGEND possiede.`

### Op 2 — `claim_registry_current.md`, record `CLAIM 005`, append to the `Evidence boundary`

- `old` (measured unique in `CLAIM 005`):
  `**Nothing in this claim's own measurements is changed:** cell autonomy of the glial change remains unmeasured in every WWOX model LEGEND holds, and this claim asserts none.`
- `new`:
  `**Nothing in this claim's own measurements is changed:** cell autonomy of the glial change remains unmeasured in every WWOX model LEGEND holds, and this claim asserts none. 🔵 **And the human organoid does not change that either (2026-10-04, \`CC-20261004W10-Y-ORGANOID-GLIA-01\`, intake wave 10).** PMID 42397075 ([[paper_registry_current#PAPER 094]]) annotates **no astrocyte, oligodendrocyte or microglial population at all** — five cell labels, glial progenitors folded into a mixed radial-glia cluster, \`GFAP\`, \`AQP4\` and \`S100B\` at **zero occurrences** in the body — so it contributes **no human glial measurement** to this axis, in either direction. An earned null, recorded so the question is not re-asked of this paper.`

### Op 3 — `paper_registry_current.md`, record `PAPER 094`, correct a measured number and add the null

- `old` (measured unique in `PAPER 094`):
  `Figure 2F plots a neuronal cell-fraction log2FC of about −2.6 against wild type`
- `new`:
  `Figure 2F plots a neuronal cell-fraction log2FC of about −2.4 against wild type, with the radial-glia block at about +1.0 (re-measured 2026-10-04 at 900 dpi against the panel's own axis ticks, \`CC-20261004W10-Y-ORGANOID-GLIA-01\`; the earlier figures of −2.6 and +0.55 were read from a rendering of an artefact that no longer exists, and the knockout's radial-glia gain is the larger of the two corrections)`

### Op 4 — `paper_registry_current.md`, record `PAPER 094`, append the glial null to `**Note:**`

- `old` (measured unique in `PAPER 094`):
  `Composition and maturation are separable and the paper shows them separately.`
- `new`:
  `Composition and maturation are separable and the paper shows them separately. 🔵 **A THIRD BOUNDARY, ADDED 2026-10-04 (\`CC-20261004W10-Y-ORGANOID-GLIA-01\`): this paper measures no glia.** No oligodendrocyte, astrocyte, OPC or microglial population is annotated — five cell labels only, with glial progenitors folded into a mixed radial-glia cluster — and no myelin, myelin protein, g-ratio or axon count is measured. Its one oligodendrocyte sentence cites a **gene-set enrichment bar** in a comparison run in neuronal progenitors and neurons, in the same panel where two lipid-synthesis pathways move the opposite way. It therefore bears on neither [[claim_registry_current#CLAIM 003]] nor [[claim_registry_current#CLAIM 005]], and that is an **earned null**, not an omission.`

## What would falsify this

A cell-type annotation in these data resolving an oligodendrocyte-lineage or astrocyte cluster — the
deposited single-cell data are named (`ArrayExpress`, accession `E-MTAB-14792`), so this is
checkable without the authors. If such a cluster is recoverable, the earned null narrows to "the
paper does not report one" rather than "the data contain none".

## DEFAULTS_TAKEN

- The brief states that a wave-8 reviewer found organoid evidence for oligodendroglia in this paper.
  **I could not confirm that premise.** The only oligodendrocyte-lineage sentence in the wave-8
  notes (`intake_wave_20261004w8_A.md`) is about a different study — a human glial-progenitor
  reprogramming paper — and is itself careful to call its observation *"not a statement about
  oligodendrocyte-lineage function"*. Reported rather than acted on.

### LOCATOR TRIPLES FOR BLIND AUDIT

(Each artefact confirmed on disk before the triple was written.)

1. (The organoids annotate no glial cell type; glial progenitors are folded into a mixed radial-glia cluster the authors decline to resolve | `of outer RGs (oRGs), cycling RGs (cRGs), and a mixed population of vRGs, neuroectodermal ` | `files/fulltext/PMID42397075_Steinberg2026_OUP-AM_fitz.txt`, Results, p. 7)
2. (The paper's only oligodendrocyte and myelin statement is drawn from a gene-set enrichment panel | `promotion of oligodendrocyte differentiation and myelination, and synaptic function (Fig. 6D ` | `files/fulltext/PMID42397075_Steinberg2026_OUP-AM_fitz.txt`, Results, p. 13)
3. (The caption of the panel that statement is drawn from names other terms and not that one | `an increase in OXPHOS and oxidative stress terms in WOREE-WWOX compared to WOREE, ` | `files/fulltext/PMID42397075_Steinberg2026_OUP-AM_fitz.txt`, Figure 6 caption, panel E)
4. (In that panel the oligodendrocyte term is positively enriched while two lipid-synthesis pathways are negatively enriched in the same contrast | `[figure attestation] Figure 6E, 'pathway enrichment', WOREE^WWOX+ versus WOREE: positive bars OXPHOS Electron transport chain, hippo signaling, 'oligodendrocyte specification & myelin', oxidative stress; negative bars PPAR-alpha pathway, synaptic vesicle pathway, cholesterol production inhibition, glycerophospholipid biosynthesis` | `files/fulltext/PMID42397075_Steinberg2026_assets/figs/fig_p36_1430x1754.jpeg`, Figure 6 panel E)
5. (In the external human fetal reference the paper uses, WWOX is highest in radial glia and lowest in the oligodendrocyte and microglial populations | `[figure attestation] Figure 3B, 'WWOX cell type expression', post-conceptional week 16 human fetal single-cell data: RG median near 0.57, IP near 0.48, ExN and InN near 0.20, Other near 0.14, Oli near 0.10, Mic near 0.07` | `files/fulltext/PMID42397075_Steinberg2026_assets/figs/fig_p34_1430x1589.png`, Figure 3 panel B)
6. (The knockout's neuronal and radial-glia cell-fraction changes, measured against the panel's own axis ticks | `[figure attestation] Figure 2F, 'RGs and Neu cell fraction changes': WWOX-KO RGs block 0 to +0.98 and Neu block -2.36 to 0; SCAR12 RGs block -0.25 to 0 and Neu block 0 to +0.18; WOREE RGs block 0 to +0.07 and Neu block -0.04 to -0.01` | `files/fulltext/PMID42397075_Steinberg2026_assets/fig2F_600dpi.png`, Figure 2 panel F)

---

## BATCH DISPOSITION — `BATCH_20261004_004` (2026-10-04, ACTOR_ID `scientist`, Scientist N), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED — **all four ops landed; one figure reading corrected by the audit.**

**Class, re-judged: MINOR, and the judgement is the one the dispatch asked for.** Both `CLAIM 003` and `CLAIM 005` are `consolidated baseline`. This candidate writes an **earned null** into each: it adds evidence-boundary text, narrows nothing, withdraws no measurement, moves no `Status`, `Type`, `Summary`, `Transferability` or `Source`, and leaves the cell-autonomy question exactly as open as it was. An earned null that adds a boundary without narrowing is MINOR; **the blind audit was still mandatory and was run**, because the records touched are baseline.

**Blind locator audit (separate sub-agent, 6 triples, figure panels read on rendered images):** **6/6 SUPPORTED**, 0 NOT_SUPPORTED, 0 UNVERIFIABLE. The auditor independently reproduced the token census (`OLIG`, `SOX10`, `PDGFRA`, `MBP`, `GFAP`, `AQP4`, `S100B`, `OPC`: zero each; `astrocyt` and `microglia` once each and **only in the reference list**), the five cluster labels, the printed n = 18 007 and the per-condition counts, the absence of any myelin, g-ratio, axon-count or OPC measurement, and the deposited accession.

🔵 **One correction at source, and it makes the null cleaner rather than weaker.** Fig. 3B's lineage values were re-measured as **`Oli` ≈ 0.08 and `Mic` ≈ 0.08 — tied**, not 0.10 and 0.07. Every landed sentence now says *lowest, and tied*, and the earlier ordering is withdrawn where it appeared. The panel-extent figures of Fig. 2F were likewise re-measured (`RGs` +0.99, `Neu` −2.38 for the knockout), which is why `PAPER 094`'s corrected numbers are stated as **−2.4 and +1.0 on two independent measurements** rather than on one.

**Ops as landed.** Op 1 → `CLAIM 003` `Evidence boundary` (record-scoped, Italian, with the falsification route and the `ArrayExpress` accession). Op 2 → `CLAIM 005` `Evidence boundary` (record-scoped, with an explicit `PREMISE: DATO` tag, which answers Mirror note F8's concern for this append without touching the record's older style). Op 3 → `PAPER 094`'s cell-fraction figures. Op 4 → `PAPER 094`'s `Note`, as a third declared boundary.

🔵 **The candidate's own DEFAULTS_TAKEN is upheld and worth repeating:** the premise that a wave-8 reviewer had found organoid evidence for oligodendroglia in this paper **could not be confirmed**, and the candidate reported that rather than acting on it. Nothing in this batch rests on it.

**Not medical advice.**
