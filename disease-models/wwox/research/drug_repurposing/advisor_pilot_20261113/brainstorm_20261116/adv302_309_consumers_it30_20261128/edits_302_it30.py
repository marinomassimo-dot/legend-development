# IT30 revision of the producer fragments after the ADV-302 blind round.
X = [{'new': 'Il paper studia i costrutti **WW1 (residui 16-50), WW2 (57-91) e tandem (16-91) di WWOX umano**, in vitro (ITC a 25 °C, pH 7,0) e in silico (omologia + MD).',
  'old': 'Il paper studia **esclusivamente i residui 1-91** (moduli WW1-WW2).',
  'path': 'disease-models/wwox/research/discovery_ledger_current.md',
  'tag': 'J1'},
 {'new': '\n'
         '*Dai lavori precedenti degli stessi autori, non misurato qui:* secondo i lavori precedenti degli stessi autori (ref 13), WW1 da solo è parzialmente destrutturato; questo articolo non misura sperimentalmente '
         'ripiegamento o stabilità (il CD è su peptidi liberi).\n'
         '\n'
         '→ **Esistenza-prova (ridimensionata):** un dominio',
  'old': '- **WW1 da solo è parzialmente destrutturato e si ripiega legando il ligando**; nel modulo tandem il legame avviene su un **WW1 già completamente ripiegato**.\n\n→ **Esistenza-prova:** un dominio',
  'path': 'disease-models/wwox/research/discovery_ledger_current.md',
  'tag': 'J2'},
 {'new': 'La stabilizzazione di WW1 da parte di WW2 è un risultato dei lavori precedenti (ref 13, 31); qui non è misurata sperimentalmente (gli autori la presentano come confermata dalla MD, che però non calcola la '
         "stabilità di WW1). La MD mostra un'associazione WW2-WW1 solo nella corsa senza ligando (Fig 8-9), non in quella con ligando. Il valore di circa 1 Å è l'RMSD del backbone dei nuclei dei singoli domini WW (WW1 "
         '22-43, WW2 63-84) rispetto alla struttura iniziale, simile in entrambe le corse: indica rigidità di ciascun dominio, non una stabilizzazione di WW1 da parte di WW2. Non è dimostrata qui e non prova che un '
         'legante esterno possa stabilizzare WWOX.',
  'old': 'un dominio instabile di WWOX viene **riscattato in stato ripiegato e funzionale** da un partner che vi si aggancia. **Stabilizzare un fold floscio di WWOX non è ipotetico: è il design nativo della proteina.** '
         'Cade l\'obiezione *"non puoi stabilizzare WWOX legandoci qualcosa"*.',
  'path': 'disease-models/wwox/research/discovery_ledger_current.md',
  'tag': 'J3'},
 {'new': 'Secondo gli autori, WWOX risolverebbe il conflitto con uno **switch allosterico**: la dissociazione di WW2 da WW1 sarebbe entropicamente favorevole e compenserebbe il costo (*binding-coupled dissociation*); '
         "il modello (Fig 10) è proposto: l'entropia di dissociazione e le popolazioni aperto/chiuso non sono né misurate né calcolate (gli autori lo sostengono con la MD, Fig 7-9, e con il TΔS dell'ITC meno "
         'sfavorevole).',
  'old': 'WWOX risolve il conflitto con uno **switch allosterico**: il ligando paga il costo entropico e solleva il coperchio (*binding-coupled dissociation*).',
  'path': 'disease-models/wwox/research/discovery_ledger_current.md',
  'tag': 'J4'},
 {'new': 'DL-MECH-049 — In WWOX **stabilità e funzione sono forse in TENSIONE STRUTTURALE**: WW2 stabilizza WW1 (lavori precedenti) e nella MD senza ligando ne copre in parte il solco (Fig 9, simulazione non verificata '
         "sperimentalmente); l'affinità misurata per otto peptidi PPXY è maggiore con WW2 presente. Vincolo di progetto ipotetico per uno stabilizzatore di Q230P.",
  'old': "DL-MECH-049 — In WWOX **stabilità e funzione sono in TENSIONE STRUTTURALE**: la stabilità si compra con l'occlusione. Vincolo di progetto per qualunque stabilizzatore di Q230P.",
  'path': 'disease-models/wwox/research/discovery_ledger_current.md',
  'tag': 'J5a-title'},
 {'new': 'DL-MECH-049 — In WWOX **stabilità e funzione sono forse in TENSIONE STRUTTURALE**: WW2 stabilizza WW1 (lavori precedenti) e nella MD senza ligando ne copre in parte il solco (Fig 9, simulazione non verificata '
         "sperimentalmente); l'affinità misurata per otto peptidi PPXY è maggiore con WW2 presente. Vincolo di progetto ipotetico per uno stabilizzatore di Q230P.",
  'old': "DL-MECH-049 — In WWOX **stabilità e funzione sono in TENSIONE STRUTTURALE**: la stabilità si compra con l'occlusione. Vincolo di progetto per qualunque stabilizzatore di Q230P.",
  'path': 'disease-models/wwox/analysis/mechanism_intervention_map.md',
  'tag': 'J5b-anchor in the mechanism map (title change would break this wikilink)'},
 {'new': 'Resta una possibilità, non un fatto: WW2 stabilizza WW1 (lavori precedenti, ref 13, 31), e nella MD senza ligando di questo articolo si appoggia su WW1 coprendone in parte il solco (Fig 9; simulazione, non '
         "verificata sperimentalmente); a livello misurato l'affinità per otto peptidi PPXY da 12 residui è maggiore con WW2 presente (Kd WW1/Kd tandem: 1,78 a 5,13; ΔΔG da -0,36 a -0,98 kcal/mol). Che lo stesso valga "
         'per uno stabilizzatore di Q230P non è mostrato. → default',
  'old': "Non era solo una possibilità: **in WWOX la stabilità si compra con l'occlusione, e l'occlusione è anti-funzione.** → default",
  'path': 'disease-models/wwox/research/discovery_ledger_current.md',
  'tag': 'J5c-body (restatement of the design constraint)'},
 {'new': '> *"In the absence of ligand, the equilibrium between the open and the closed state predominantly lies in favor of the latter"* (modello proposto, Fig 10)',
  'old': '> *"in assenza di ligando, l\'equilibrio aperto↔chiuso è **nettamente a favore del chiuso**"*',
  'path': 'disease-models/wwox/research/discovery_ledger_current.md',
  'tag': 'J6'},
 {'new': 'lega **più forte** che da solo (Kd WW1/Kd tandem da 1,78 a 5,13; gli autori scrivono «2-3 volte»), con **penalità entropica minore** (TΔS meno negativo in 8 su 8, ancora negativo in 6) ed entalpia peggiore in '
         '8 su 8 (ΔΔH da +1,27 a +10,5 kcal/mol).',
  'old': 'lega **2-3× più forte** che da solo, con **guadagno entropico**.',
  'path': 'disease-models/wwox/research/discovery_ledger_current.md',
  'tag': 'J7'},
 {'new': '**`DATO` (ITC a 25 °C, pH 7,0, n≥3; CD a quattro scansioni; peptidi PPXY da 12 residui, Kd da 42 a 763 µM; stechiometria fissata a 1):**',
  'old': '**`DATO` (ITC/CD, n≥3):**',
  'path': 'disease-models/wwox/research/discovery_ledger_current.md',
  'tag': 'J8a-scope ITC/CD'},
 {'new': '(omologia FBP21/2JXW + MD; 4 μs nei Metodi (2-4 μs nella legenda della Fig 8), ma «2-μs» nel testo e «2μs» nella legenda della Fig 9)',
  'old': '(omologia FBP21/2JXW + MD 4 μs, 4 force field)',
  'path': 'disease-models/wwox/research/discovery_ledger_current.md',
  'tag': 'J8b-MD length'},
 {'new': 'Dati solo per AMBER99SB-ILDN; la riproducibilità su GROMOS, CHARMM e OPLS è affermata senza dati.',
  'old': 'Riprodotto su AMBER/GROMOS/CHARMM/OPLS.',
  'path': 'disease-models/wwox/research/discovery_ledger_current.md',
  'tag': 'J8c-force fields'},
 {'new': '\n'
         "- ⚠️ **Livello abstract (2026-11-28, SCI ADV-302; full text mai aperto, FT-180):** la dipendenza dal dominio (WW e non SDR) non è mostrata da nulla di letto in questo repository e non è nell'abstract di "
         "Bouteille 2009, che riporta associazione two-hybrid/co-IP, inibizione della via con WWOX forzato e sequestro citoplasmatico di Dvl-2, senza nominare né i WW né l'SDR come responsabili. UNSETTLED finché "
         "l'articolo non è letto.\n"
         '- **Status**: open · **Tag**: INFERENZA · **Fonte**: Bouteille 2009 (PMID 19465938)',
  'old': '\n- **Status**: open · **Tag**: INFERENZA · **Fonte**: Bouteille 2009 (PMID 19465938)',
  'path': 'disease-models/wwox/research/discovery_ledger_current.md',
  'tag': 'C1 (abstract-level)'},
 {'new': '— TSN "candidate agonist": solo abstract, full text chiuso; l\'abstract non riporta un aumento del livello di WWOX; cellule di carcinoma epatocellulare e modelli in vivo)',
  'old': '— TSN attiva WWOX)',
  'path': 'disease-models/wwox/research/discovery_ledger_current.md',
  'tag': 'C2a-source (abstract-level)'},
 {'new': "TSN (abstract-level, full text chiuso; l'abstract non riporta un aumento del livello di WWOX; cellule tumorali) — non usabile come supporto all'up-modulazione della proteina residua",
  'old': 'esistenza di un attivatore di WWOX (TSN) = WWOX è up-modulabile',
  'path': 'disease-models/wwox/research/discovery_ledger_current.md',
  'tag': 'C2b-evidence (abstract-level)'},
 {'new': 'and 15240510 (notice 42713750, 2026-09-09) in 2026.\n'
         "- 🔵 **Append-only retraction fact, 2026-11-28 (IT, ADV-302; SCI's reading of the notice PMC7429703 and of the article's PMC record).** 26041563 (Bendinelli 2015, *Mol Cancer* 14:112) was retracted by a "
         'retraction note published 15 August 2020 (*Mol Cancer* 19:126, notice PMID 32799870) after an investigation by the Università degli Studi di Milano, which found manipulations of the vinculin loading-control '
         'bands in its Figs 2 and 3 (band reuse from other publications of the same groups in Fig 2; band rotation, "seems to have been performed", in Fig 3); the note calls the results unreliable; the authors do not '
         'agree to the retraction.\n',
  'old': 'and 15240510 (notice 42713750, 2026-09-09) in 2026.\n',
  'path': 'disease-models/wwox/research/discovery_ledger_current.md',
  'tag': 'R1-DL-MECH-025 append-only retraction note (inserted after the narrowing bullet)'},
 {'new': 'paper RITRATTATO con nota di ritiro del 15 agosto 2020 (*Mol Cancer* 19:126, PMID 32799870) per manipolazione delle bande di vinculina usate come controllo di caricamento nelle Fig. 2 e 3 (non di tutti i '
         'western blot; gli autori non concordano)**',
  'old': 'paper RITRATTATO per manipolazione di western blot**',
  'path': 'disease-models/wwox/research/discovery_ledger_current.md',
  'tag': 'R2-FM-006'}]

if __name__ == "__main__":
    import sys, pathlib
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    root = pathlib.Path(".")
    bad = 0
    texts = {}
    for e in X:
        p = root / e["path"]
        t = texts.setdefault(e["path"], p.read_text(encoding="utf-8"))
        n = t.count(e["old"])
        print(f'{e["tag"]}: old occurs {n}x in {e["path"]}')
        if n != 1:
            bad += 1
    if mode == "apply" and not bad:
        for e in X:
            assert texts[e["path"]].count(e["old"]) == 1, e["tag"]
            texts[e["path"]] = texts[e["path"]].replace(e["old"], e["new"], 1)
        for path, t in texts.items():
            (root / path).write_text(t, encoding="utf-8")
        print("applied")
    sys.exit(1 if bad else 0)
