# CC-20261004W12-C-SDR-ABUNDANCE-01 — "the clean case" is clean about decay rate, not about abundance; and the interactome behind POLE4 carries no statistic

- **Wave:** intake wave 12, 2026-10-04, Scientist C (RE-READ wave)
- **context_policy:** SOURCE_FIRST — the panels and the workbook were read before DL-BIO-001 was
  opened.
- **Target record:** `DL-BIO-001` in `disease-models/wwox/research/discovery_ledger_current.md`
- **Change class:** **MINOR.** Research-layer, non-canonical, append-only record; `Status` stays
  `open`, `Tag` stays `IPOTESI`, and the 2026-09-21 Belief setting (medio → medio-alto on the
  mechanism class) is **not** changed by this candidate. No consolidated baseline claim is touched.
- **Source read:** PMID 41124647 (DOI 10.1002/advs.202507602), figures and supplements.
  Artefacts newly declared in `deepdive_manifests/PMID41124647.json`, acquired free from the
  **Europe PMC supplementaryFiles archive for PMC12767083** (no spend, no author contact):
  `files/fulltext/PMID41124647_Zhang2025_supplement/ADVS-13-e07602-g007.jpg` sha256
  `a7583e6a74dbcf42852789e58729d4eb297dd9ca590cd7dd6878b813d2c168be`;
  `…-g005.jpg` sha256 `4ba794dc1701278293216785c05e650f4746c844c0dc6d5bf01d478d37992835`;
  `…-s003.xlsx` sha256 `d41da474dc6f618d0693b78bb2992daa3e29dc79cd0384837a8f003056db00ca`;
  `…-s002.xlsx` sha256 `e7711a554464c345da79eb3befc7c03123683cc3b9cf1e07ca3b4176deb1f8e5`.
  **Integrity check:** the already-declared `…-s001.docx` came back from the same archive
  **byte-equal** (`6e402eff70ea…`), which is what licenses trusting the rest of the package.
- **Receipt of the producing reading:** `FTR-20261004-41124647-03` (prepared, not recorded;
  `prior_receipt: FTR-20261003-41124647-02`).

## Why

DL-BIO-001 records, correctly, that P252A's loss is post-transcriptional and that P282A *«perde
funzione senza difetto di stabilità ed è il caso più pulito»*. The owed figure surface shows that
the second half of that sentence is about **decay rate** and cannot be about steady-state
abundance, because the compared lines are matched on neither transcript nor protein:

- Figure 4A (read as a panel): relative WWOX mRNA ≈ **72 (WT), 78 (P252A), 108 (P282A)** — P282A
  carries roughly **1.5× the WT transgene transcript** (108/72).
- Figure 4B: the cycloheximide chase has P282A `ns` against WT at every one of the five timepoints
  — a **decay-rate** null, which is what a CHX chase measures.
- Figure 2A: with that 1.5× transcript, the P282A protein band is **no stronger than WT in CAL-62
  and visibly weaker than WT in BCPAP**, on an even GAPDH row. The paper publishes **no
  densitometry** for this blot, and none is manufactured here.

So the function comparison of Figure 2B–F — where both mutants are `ns` against the empty vector on
colony formation, invasion and migration in both lines — is run between lines whose steady-state
WWOX abundance is unquantified and visibly unequal. That is a qualification of the record's
"cleanest case", not a reversal of it: the decay-rate null stands.

Separately, the interactome supplement that the POLE4 argument rests on was read cell-wise for the
first time and is a **presence-only list**: 261 rows, `Lost Detection` in all three control columns
of **every** row, one intensity column, no replicate, no fold change, no p-value, no FDR, and no
WWOX row. POLE4 is rank 52 of 261.

## Exact op

**File:** `disease-models/wwox/research/discovery_ledger_current.md`
**Record:** `DL-BIO-001`
**Op:** `replace-within` the record.

`old` (verbatim, measured **1 occurrence in `DL-BIO-001` and 1 in the whole file**):

```
`P282A` perde funzione **senza difetto di stabilità** ed è il caso più pulito
```

`new`:

```
`P282A` perde funzione **senza difetto di stabilità** ed è il caso più pulito — ⚠️ **precisato 2026-10-04 (`CC-20261004W12-C-SDR-ABUNDANCE-01`, intake wave 12 Scientist C, superficie figure letta a pannello, receipt `FTR-20261004-41124647-03`): «senza difetto di stabilità» vale per la VELOCITÀ DI DECADIMENTO, che è ciò che una caccia con cicloesimide misura** (Fig. 4B: `P282A` è `ns` contro WT a tutti e cinque i tempi, mentre `P252A` scende a circa 0,3 del proprio tempo zero con `*`, `**`, `***`, `**`, `*`). **Non vale per l'abbondanza allo stato stazionario, che in questo paper non è quantificata da nessun pannello:** in Fig. 4A l'mRNA relativo del transgene vale circa **72 (WT), 78 (P252A), 108 (P282A)**, cioè `P282A` porta circa **1,5× il trascritto di WT** (108/72), e con quel trascritto in più la sua banda proteica in Fig. 2A **non è più forte di WT in CAL-62 ed è visibilmente più debole di WT in BCPAP**, su una riga GAPDH uniforme — osservazione **visiva** di pannello, perché il paper non pubblica densitometria per quel blot e nessun rapporto è stato fabbricato qui. Di conseguenza i null funzionali di Fig. 2B–F (clonogenicità, invasione, migrazione: entrambi i mutanti `ns` contro vettore vuoto nelle due linee) sono confronti fra linee **non appaiate né per trascritto né per proteina**: «il caso più pulito» resta il migliore dei due, ma la pulizia è relativa. 🔴 **E il supplemento che regge l'argomento POLE4 è una lista di sola presenza:** la Tabella Supplementare 6 (`ADVS-13-e07602-s003.xlsx`, foglio `list`), letta cella per cella, ha **261 righe** in cui **tutte e tre le colonne di controllo riportano `Lost Detection`** e l'unica colonna numerica è `CAL-62_WT_Anti-Flag`; **nessuna replica, nessun fold change, nessun p, nessun FDR**, e `WWOX` non è una riga. `POLE4` è **rango 52 su 261** per intensità (1937463,375); `HSPA8`, `LAMP2`, `POLE3`, `POLD2` e `TP53` sono **assenti** dalla lista. 🔵 **Un dato laterale, registrato dove serve:** `DVL2` **è** nella lista (rango 190 su 261, intensità 375599,84375) — un pull-down di WWOX in una linea di carcinoma tiroideo recupera Dishevelled-2, il che tocca l'asse WWOX–DVL di [[discovery_ledger_current#DL-MOL-003 — Asse Wnt: direzione RISOLTA (WWOX-loss → IPER-attivazione) → leva = INIBIZIONE Wnt; ⚠️ litio CONTRO-indicato dal meccanismo|DL-MOL-003]] senza misurarlo: una IP singola, WWOX-Flag sovraespresso, nessuna replica, nessuna statistica, nessun readout di localizzazione o di segnale. 🔴 **E la domanda che questa voce pone — attività ossidoreduttasica — questo paper non la risponde affatto:** `oxidoreductase` compare **una** volta (l'espansione del nome del gene in Introduzione), `SDR`, `enzyme`, `catalytic`, `dehydrogenase` e `short-chain` **zero**; non esiste alcun saggio enzimatico per nessuno dei due alleli. La perdita di funzione misurata è **fenotipica**, non catalitica. Nessun trasferimento a Q230P: `P252A` non è `Q230P` e un missenso SDR non è un allele di sito accettore.
```

## Registry records

**None owed.** PMID 41124647 already has registry presence (see `paper_packet.py packet --pmid
41124647`); this candidate creates no `PAPER`/`LIT` record.

## What would falsify it

A densitometric quantification of Figure 2A showing P282A at wild-type abundance in both lines, or
a steady-state measurement normalised to transgene transcript; and, for the interactome, a deposited
replicate or statistical column in Supplementary Table 6 that this reading missed (checkable by
re-reading the sheet cell-wise).

### LOCATOR TRIPLES FOR BLIND AUDIT

1. (The compared lines are not matched on transgene transcript, and the cycloheximide chase result for the second allele is a decay-rate null | `[figure attestation - pixels cannot be quote-matched] Figure 4A plots relative WWOX mRNA expression in CAL-62 at approximately 0 for the empty vector, 72 for WWOX-WT, 78 for WWOX-P252A and 108 for WWOX-P282A, each marked **** against the vector. Figure 4B plots relative WWOX protein level over a ten-hour cycloheximide chase: WWOX-P252A falls to about 0.3 of its own time zero and is marked *, **, ***, ** and * at 2, 4, 6, 8 and 10 hours, while WWOX-P282A tracks WWOX-WT and is marked ns at every timepoint.` | Figure 4, panels A and B; native JPEG inspected and the top third re-cropped and magnified — `files/fulltext/PMID41124647_Zhang2025_supplement/ADVS-13-e07602-g005.jpg`)
2. (Steady-state protein is unequal across the compared lines and is not quantified | `[figure attestation - pixels cannot be quote-matched] Figure 2A shows two Flag-WWOX blots over a GAPDH loading row. In CAL-62 the Flag-WWOX band is strong for WWOX-WT, faint for WWOX-P252A and strong for WWOX-P282A; in BCPAP the WWOX-WT band is the strongest of the blot, WWOX-P252A is very faint and WWOX-P282A is visibly weaker than WWOX-WT, while the four GAPDH bands are even in both blots. The paper publishes no densitometry for this blot.` | Figure 2, panel A; native JPEG inspected, and the panel re-cropped and magnified twofold — `files/fulltext/PMID41124647_Zhang2025_supplement/ADVS-13-e07602-g007.jpg`)
3. (The interactome supplement carries no replicate and no statistic | `[spreadsheet attestation - read cell-wise from the workbook XML] Sheet 'list' of Supplementary Table 6 holds 261 protein rows under the columns Uniprot_ID, Gene_name, Description, CAL-62_WT_IgG, CAL-62_WT_Anti-Flag, CAL-62_pCMV-3Tag_IgG and CAL-62_pCMV-3Tag_Anti-Flag. Every one of the 261 rows carries the string 'Lost Detection' in all three control columns and a single numeric intensity in CAL-62_WT_Anti-Flag; no column holds a fold change, a p value or an FDR, and WWOX itself is not a row. POLE4 is rank 52 of 261 by intensity at 1937463.375.` | Supplementary Table 6, sheet 'list', all 261 data rows; read cell-wise from the workbook XML — `files/fulltext/PMID41124647_Zhang2025_supplement/ADVS-13-e07602-s003.xlsx`)
4. (The same supplement places DVL2 in the WWOX pull-down | `[spreadsheet attestation - read cell-wise from the workbook XML] Supplementary Table 6 row O14641 DVL2 'Segment polarity protein dishevelled homolog DVL-2' carries 'Lost Detection' in CAL-62_WT_IgG, CAL-62_pCMV-3Tag_IgG and CAL-62_pCMV-3Tag_Anti-Flag and the intensity 375599.84375 in CAL-62_WT_Anti-Flag, which is rank 190 of the 261 rows. HSPA8, LAMP2, POLE3, POLD2 and TP53 are absent from the list.` | Supplementary Table 6, sheet 'list', row DVL2; read cell-wise from the workbook XML — `files/fulltext/PMID41124647_Zhang2025_supplement/ADVS-13-e07602-s003.xlsx`)
5. (No enzymatic assay exists in this paper and the word oxidoreductase appears only in the gene's name | `The gene encoding WWOX (WW domain‐containing oxidoreductase), spanning chromosome region 16q23.1‐16q23.2 and crossing 1.1 million base pairs, ranks among the largest genes in the human genome.` | Introduction, opening sentence — `files/fulltext/PMID41124647_Zhang2025_PMC.xml`)
