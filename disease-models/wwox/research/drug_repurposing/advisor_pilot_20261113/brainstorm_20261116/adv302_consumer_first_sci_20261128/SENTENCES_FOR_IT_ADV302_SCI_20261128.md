# For IT: proposed wordings from ADV-302 step 2 (SCI, window 64fc909a; hypothesis level; not medical advice)

Sources: 25703206 held file `files/fulltext/PMID25703206_Schuchardt2015_PMC.xml` (Tables 1 and 2); 26041563 and its note PMC7429703. Reports and numbers: `RESULT_ADV302_SCI_20261128.md`. Wordings are proposals; each can be checked on the quoted table or sentence.

## DL-MECH-049 (`research/discovery_ledger_current.md`, line 1216 onward), 25703206

| # | sentence now | proposed |
|---|---|---|
| J1 | "Il paper studia esclusivamente i residui 1-91" | "il paper studia i costrutti WW1 (residui 16-50), WW2 (57-91) e tandem (16-91) di WWOX umano, in vitro (ITC a 25 °C, pH 7,0) e in silico (omologia + MD)" |
| J2 | DATO (ITC/CD): "WW1 da solo è parzialmente destrutturato e si ripiega legando il ligando; ... WW1 già ripiegato" | move out of the DATO list: "secondo i lavori precedenti degli stessi autori (ref 13), WW1 da solo è parzialmente destrutturato; questo articolo non misura ripiegamento o stabilità (il CD è su peptidi liberi)" |
| J3 | "Esistenza-prova ... è il design nativo ... Cade l'obiezione" | "la stabilizzazione di WW1 da parte di WW2 è un risultato dei lavori precedenti (ref 13, 31) più un'associazione vista nella MD (nuclei WW a circa 1 Å in entrambe le corse); non è dimostrata qui e non prova che un legante esterno possa stabilizzare WWOX" |
| J4 | "il ligando paga il costo entropico e solleva il coperchio" | "secondo gli autori, la dissociazione di WW2 da WW1 sarebbe entropicamente favorevole e compenserebbe il costo; il modello (Fig 10) è proposto, non misurato né simulato" |
| J5 | head: "la stabilità si compra con l'occlusione; l'occlusione è anti-funzione" | "WW2 si appoggia su WW1 e lo stabilizza (lavori precedenti) mentre ne copre in parte il solco (modello); a livello misurato l'affinità per otto peptidi PPPY da 12 residui è maggiore con WW2 presente (Kd tandem/WW1: 1,78 a 5,13; ΔΔG da -0,36 a -0,98 kcal/mol)"; the design-constraint conclusion for Q230P stabilisers needs a re-statement on that basis |
| J6 | quote "equilibrio aperto↔chiuso è nettamente a favore del chiuso" in quotation marks | quote the English ("predominantly lies in favor of the latter", proposed model) or paraphrase without quotation marks |
| J7 | "guadagno entropico" | "penalità entropica minore (TΔS meno negativo in 8 su 8, ancora negativo in 6) con entalpia peggiore in 8 su 8 (ΔΔH da +1,27 a +10,5 kcal/mol)" |
| J8 | scope | ADD: 12-mer PPPY peptides, Kd 42 to 763 µM, ITC n at least 3 (CD: four scans), stoichiometry fixed to 1; the three other force fields are asserted without data; MD length 4 µs in Methods but "2-us" in text and Fig 9 |

## Retraction lines naming 26041563 (DL-MECH-025 narrowing note, FM-006, `disease_model.md` line 33, `working_model_current.md` line 81)

ADD: "26041563 (Bendinelli 2015) retracted 15 August 2020 (Mol Cancer 19:126, PMID 32799870) after an investigation by the University of Milan, which found manipulations of the vinculin loading-control bands in its Figs 2 and 3 (band reuse in Fig 2, band rotation in Fig 3); the note calls the results unreliable; the authors do not agree". The "retracted in 2022" of the same sentence is true of 28151481 only. "per manipolazione di western blot" (FM-006) is too broad: vinculin loading controls in two figures. The review (2017) predates every retraction named.
