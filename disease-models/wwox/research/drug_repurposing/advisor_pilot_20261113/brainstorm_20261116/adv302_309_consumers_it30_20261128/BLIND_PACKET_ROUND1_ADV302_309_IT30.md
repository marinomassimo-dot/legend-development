# Blind-reader packet (hypothesis level; nothing here is medical advice)

## Instructions
You see only the sentences below and the source texts named in the mapping table (two folders: <scratch>/src/ and <scratch>/src/). For each item:
- Check it against the WHOLE named source only (not against any other paper, nothing from memory).
- Verdict per item: KEEP, MUST CHANGE or OPTIONAL. For MUST CHANGE or OPTIONAL give the exact words that fail and a replacement that the source supports.
- Check every number, and every absolute or negative word (only, never, no, none, all, every, not measured, without data, ...) against the whole source. A negative statement is true only if the source is silent on the point; say what you searched (terms, sections, tables, figure legends).
- Pointers to record numbers (for example "ref 13, 31", "DL-...", "Fig 10") that refer to the source's own reference list or figures can be checked; pointers to repository records cannot, say "not checkable".
- A sentence can be wrong in what it attributes (who measured or proposed what, which part of the paper) even when every number is right: check attribution too.
- Return your report as your reply (do not write a file).

## Items (each is the NEW text only)

**J1.** Il paper studia i costrutti WW1 (residui 16-50), WW2 (57-91) e tandem (16-91) di WWOX umano, in vitro (ITC a 25 °C, pH 7,0) e in silico (omologia + MD).

**J2.** Secondo i lavori precedenti degli stessi autori (ref 13), WW1 da solo è parzialmente destrutturato; questo articolo non misura ripiegamento o stabilità (il CD è su peptidi liberi).

**J3.** La stabilizzazione di WW1 da parte di WW2 è un risultato dei lavori precedenti (ref 13, 31) più un'associazione vista nella MD (nuclei WW a circa 1 Å in entrambe le corse); non è dimostrata qui e non prova che un legante esterno possa stabilizzare WWOX.

**J4.** Secondo gli autori, la dissociazione di WW2 da WW1 sarebbe entropicamente favorevole e compenserebbe il costo; il modello (Fig 10) è proposto, non misurato né simulato.

**J6.** "In the absence of ligand, the equilibrium between the open and the closed state predominantly lies in favor of the latter" (modello proposto, Fig 10).

**J7.** Il modulo tandem lega 2-3× più forte che WW1 da solo, con penalità entropica minore (TΔS meno negativo in 8 su 8, ancora negativo in 6) ed entalpia peggiore in 8 su 8 (ΔΔH da +1,27 a +10,5 kcal/mol).

**J8.** Dati: ITC a 25 °C, pH 7,0, almeno tre misure; CD a quattro scansioni; peptidi PPPY da 12 residui, Kd da 42 a 763 µM; stechiometria fissata a 1. Le MD sono dichiarate di 4 μs nei Metodi, ma nel testo e nella Fig 9 compare «2-μs»; i dati mostrati sono solo per AMBER99SB-ILDN, mentre la riproducibilità su GROMOS, CHARMM e OPLS è affermata senza dati.


**J5a (a record heading).** In WWOX **stabilità e funzione sono forse in TENSIONE STRUTTURALE**: WW2 stabilizza WW1 (lavori precedenti) e ne copre in parte il solco (modello); l'affinità misurata per otto peptidi PPPY è maggiore con WW2 presente. Vincolo di progetto ipotetico per uno stabilizzatore di Q230P.

**J5c (a body sentence).** Resta una possibilità, non un fatto: WW2 si appoggia su WW1 e lo stabilizza (lavori precedenti) mentre ne copre in parte il solco (modello); a livello misurato l'affinità per otto peptidi PPPY da 12 residui è maggiore con WW2 presente (Kd WW1/Kd tandem: 1,78 a 5,13; ΔΔG da -0,36 a -0,98 kcal/mol). Che lo stesso vale per uno stabilizzatore di Q230P non è mostrato. → default

**R1 (retraction ADD).** 26041563 (Bendinelli 2015) è stato ritirato il 15 agosto 2020 (Mol Cancer 19:126, PMID 32799870) dopo un'indagine dell'Università degli Studi di Milano, che ha trovato manipolazioni delle bande di vinculina usate come controllo di caricamento nelle sue Fig 2 e 3 (riuso di bande in Fig 2, rotazione di bande in Fig 3); la nota definisce i risultati inaffidabili; gli autori non concordano con il ritiro. «Retracted in 2022» vale per 28151481, non per 26041563.

## Items from a second package (source folder <scratch>/src/)
**X1 (a clinical-meaning sentence, Italian).** qualunque fenotipo ippocampale o cerebrale misurato a P18 in un null **sistemico** della linea EIIA-Cre è misurato in un animale con glucosio ridotto (143.5 vs 250.6 mg/dL), BUN raddoppiato (37.25 vs 17.67 mg/dL) e CO₂ totale ridotta (14.50 vs 21.67 mEq/L) — valori che gli autori leggono come compatibili con insufficienza renale e acidosi metabolica, ma senza pH né creatinina misurati — e con leucopenia e segni di anemia (WBC 4.2 vs 9.45 ×10³/µL, `n=2/gruppo`, età della conta non dichiarata; eritrociti nucleati al 3% in uno solo dei due topi KO esaminati; nessun emocromo completo: solo una conta manuale dei leucociti e una formula da striscio, non mostrata). La chimica ematica (`n=3/3/4`) esiste solo a P18: a P14 l'unica misura è il peso corporeo (4.2 g contro 6.82 e 7.07 g), e per i topi KO BK5-Cre di due settimane di PMID 30290271 non esiste alcuna chimica ematica, quindi lo stesso confondente è lì una possibilità, non una misura.

**X2 (an addendum to a summary).** (Ages and tissues sampled: Iacomino 2020 — one WWOX-deficient human fetus at 21 gestational weeks, lde/lde rat brain at P1 with BrdU given at E16.5 and traced to P1, and human neural progenitor cells in vitro (a re-analysis of the Kośla 2019 deposit); Tochigi 2019 — hypomyelination and reduced cortical GFAP and Iba1 in lde/lde rat cortex at PND 5 to 21 only; Kośla 2019 — human neural progenitor cells in vitro (WWOX silenced), no animal and no WWOX-deficient fetal tissue; its only fetal age is a public Fantom5 comparison of WWOX expression in the whole brain, adults versus 20-33-week fetuses (17.7 vs 9.2 TPM RLE).)

**X3 (a record heading, Italian).** Nel *lde*: ipomielinizzazione con oligodendrociti maturi ridotti (PND 15-21) e **numero di neuroni invariato ma crescita dei neuriti ridotta (MAP2)**. Il substrato è salvabile (ipotesi; nessun rescue testato; PND 5-21)

Source map for X1 to X3: X1 p19936220.txt (mouse EIIA-Cre line, necropsy and blood chemistry) and p30290271.txt (two-week BK5-Cre mice); X2 p32581702.txt, p31340538.txt, p31543760.txt; X3 p31340538.txt.

## Item to source map (first package)
J1 to J8, J5a, J5c: p25703206.txt (Schuchardt 2015, whole article incl. Tables 1 and 2 and figure legends; Table 1 is WW1 alone, Table 2 the WW1-WW2 tandem; tables render as rows with ' | ' between cells). R1: p32799870.txt (retraction note) and p26041563.txt (Bendinelli 2015 article record).
