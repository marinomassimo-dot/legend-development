# Blind-reader packet (hypothesis level; nothing here is medical advice)

## Instructions
You see only the sentences below and the source texts named in the mapping table (folder <scratch>/src/). For each item:
- Check it against the WHOLE named source only (not against any other paper, nothing from memory).
- Verdict per item: KEEP, MUST CHANGE or OPTIONAL. For MUST CHANGE or OPTIONAL give the exact words that fail and a replacement that the source supports.
- Check every number, and every absolute or negative word (only, never, no, none, all, every, not measured, without data, ...) against the whole source. A negative statement is true only if the source is silent on the point; say what you searched (terms, sections, tables, figure legends).
- Pointers to record numbers (for example "ref 13, 31", "DL-...", "Fig 10") that refer to the source's own reference list or figures can be checked; pointers to repository records cannot, say "not checkable".
- A sentence can be wrong in what it attributes (who measured or proposed what, which part of the paper) even when every number is right: check attribution too.
- Return your report as your reply (do not write a file).

## Items (each is the NEW text; fragments of a longer record, judge the text as written)

**J2.** *Dai lavori precedenti degli stessi autori, non misurato qui:* secondo i lavori precedenti degli stessi autori (ref 13), WW1 da solo è parzialmente destrutturato; questo articolo non misura sperimentalmente ripiegamento o stabilità (il CD è su peptidi liberi).

→ **Esistenza-prova (ridimensionata):** un dominio

**J3.** La stabilizzazione di WW1 da parte di WW2 è un risultato dei lavori precedenti (ref 13, 31); qui non è misurata. La MD mostra un'associazione WW2-WW1 solo nella corsa senza ligando (Fig 8-9), non in quella con ligando. Il valore di circa 1 Å è l'RMSD del backbone dei nuclei dei singoli domini WW (WW1 22-43, WW2 63-84) rispetto alla struttura iniziale, simile in entrambe le corse: indica rigidità di ciascun dominio, non una stabilizzazione di WW1 da parte di WW2. Non è dimostrata qui e non prova che un legante esterno possa stabilizzare WWOX.

**J4.** Secondo gli autori, WWOX risolverebbe il conflitto con uno **switch allosterico**: la dissociazione di WW2 da WW1 sarebbe entropicamente favorevole e compenserebbe il costo (*binding-coupled dissociation*); il modello (Fig 10) è proposto: l'entropia di dissociazione e le popolazioni aperto/chiuso non sono né misurate né calcolate (gli autori lo sostengono con la MD, Fig 7-9, e con il TΔS dell'ITC meno sfavorevole).

**J5a (heading).** DL-MECH-049 — In WWOX **stabilità e funzione sono forse in TENSIONE STRUTTURALE**: WW2 stabilizza WW1 (lavori precedenti) e nella MD senza ligando ne copre in parte il solco (Fig 9, simulazione non verificata sperimentalmente); l'affinità misurata per otto peptidi PPXY è maggiore con WW2 presente. Vincolo di progetto ipotetico per uno stabilizzatore di Q230P.

**J5c (body).** Resta una possibilità, non un fatto: WW2 stabilizza WW1 (lavori precedenti, ref 13, 31), e nella MD senza ligando di questo articolo si appoggia su WW1 coprendone in parte il solco (Fig 9; simulazione, non verificata sperimentalmente); a livello misurato l'affinità per otto peptidi PPXY da 12 residui è maggiore con WW2 presente (Kd WW1/Kd tandem: 1,78 a 5,13; ΔΔG da -0,36 a -0,98 kcal/mol). Che lo stesso valga per uno stabilizzatore di Q230P non è mostrato. → default

**J7.** lega **più forte** che da solo (Kd WW1/Kd tandem da 1,78 a 5,13; gli autori scrivono «2-3 volte»), con **penalità entropica minore** (TΔS meno negativo in 8 su 8, ancora negativo in 6) ed entalpia peggiore in 8 su 8 (ΔΔH da +1,27 a +10,5 kcal/mol).

**J8a.** **`DATO` (ITC a 25 °C, pH 7,0, n≥3; CD a quattro scansioni; peptidi PPXY da 12 residui, Kd da 42 a 763 µM; stechiometria fissata a 1):**

**J8b.** (omologia FBP21/2JXW + MD; 4 μs nei Metodi (2-4 μs nella legenda della Fig 8), ma «2-μs» nel testo e «2μs» nella legenda della Fig 9)

**R1a (ledger text).** and 15240510 (notice 42713750, 2026-09-09) in 2026.
- 🔵 **Append-only retraction fact, 2026-11-28 (IT, ADV-302; SCI's reading of the notice PMC7429703 and of the article's PMC record).** 26041563 (Bendinelli 2015, *Mol Cancer* 14:112) was retracted by a retraction note published 15 August 2020 (*Mol Cancer* 19:126, notice PMID 32799870) after an investigation by the Università degli Studi di Milano, which found manipulations of the vinculin loading-control bands in its Figs 2 and 3 (band reuse from other publications of the same groups in Fig 2; band rotation, "seems to have been performed", in Fig 3); the note calls the results unreliable; the authors do not agree to the retraction.


**R1b (ledger text).** paper RITRATTATO con nota di ritiro del 15 agosto 2020 (*Mol Cancer* 19:126, PMID 32799870) per manipolazione delle bande di vinculina usate come controllo di caricamento nelle Fig. 2 e 3 (non di tutti i western blot; gli autori non concordano)**

**R1c (a current-file sentence).** 15240510). Of these, 26041563 (Bendinelli 2015) was retracted by a retraction note published 15 August 2020 (Mol Cancer 19:126, PMID 32799870) after an investigation by the University of Milan, which found manipulations of the vinculin loading-control bands in its Figs 2 and 3 (band reuse in Fig 2, band rotation, which "seems to have been performed", in Fig 3); the note calls the results unreliable; the authors do not agree. The review cites 28151481 for its Figure 3B

## Source map
All items: p25703206.txt (Schuchardt 2015, whole article incl. Tables 1 and 2 and figure legends; Table 1 is WW1 alone, Table 2 the WW1-WW2 tandem) except R1a, R1b, R1c: p32799870.txt (retraction note), p32799870_meta.txt (its record metadata) and p26041563.txt (Bendinelli 2015 record). Pointers to other repository records (DL-, PMID 28151481, 25447306, 19357348, 15240510, notices) are not checkable here: ignore them and judge only the statements about 26041563 and its retraction note.
