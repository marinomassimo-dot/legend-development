# Therapeutic Hypotheses Ledger — LEGEND (NON canonico)

> **Public edition — de-identified, disease-level.** The scored portfolio produced by the `legend-hypothesis-forge` co-scientist loop (generate → critique → rank → evolve). Every entry is a **HYPOTHESIS or EXTENSION**, never a datum, and every entry carries a BLOCK-1 safety verdict. Nothing here is a therapy, a recommendation, or medical advice.
>
> All individual-linking material has been removed: no identified person, no treatment schedule, no family-relationship data, no institution. Hypotheses are framed against **the reference genotype** — a disease-level WWOX-DEE genotype class — not against a person. Body text is preserved in its original language where it was written that way.
>
> **Layer non canonico, READ-ONLY verso i 4 current e verso Layer 9.** Spazio-strategia: qui vivono IPOTESI ed ESPANSIONE, mai DATI. Nulla entra nei current se non via `INGEST → DEEP_DIVE → COMMIT CANDIDATE → BATCH_COMMIT`.
>
> **Non è parere medico.** È supporto al confronto col team curante.

- **Generato da:** skill `legend-hypothesis-forge`
- **WM di riferimento:** WM_v3.0_2026-07-14
- **Ultimo aggiornamento:** 2026-07-14 — repair causale Q230P

## Legenda
- **Leve:** 1 correzione-difetto · 2 compensazione-pathway · 3 repurposing · 4 protezione-finestra · 5 biomarcatore-abilitante
- **Tag epistemico:** `IPOTESI` | `ESPANSIONE`
- **Status:** `generated` → `stress-tested` → `ranked` → `proposed-to-L9` → `parked` → `refuted` → `flagged`

---

## Ipotesi

### HYP-20260705-01 — Sleep/network-state come endpoint distale WWOX-linked
- **Leva:** 4 + 5
- **Tag:** `IPOTESI`
- **Enunciato falsificabile:** Se WWOX regola stabilità sonno/network-state, allora actigraphy + EEG sleep architecture dovrebbero mostrare pattern alterati in WWOX-DEE e migliorare parzialmente quando la rete è stabilizzata.
- **Meccanismo:** WWOX variants associate a sleep duration in human GWAS; Wwox-LoF in fly altera durata/qualità del sonno senza abolire il ritmo circadiano.
- **Evidenza PRO:** [[discovery_ledger_current#DL-MECH-013 — WWOX come regolatore di sleep/network-state: bridge umano + Drosophila funzionale|DL-MECH-013]]; convergenza con network-state/hyperexcitability già nel ledger.
- **Evidenza CONTRO / incertezze:** endpoint distale, confondibile da farmaci, crisi, alimentazione, infezioni; non è biomarker WWOX Tier 1/2.
- **Sicurezza (BLOCCO 1):** verde come misurazione; nessun intervento.
- **Traslabilità al modello di malattia:** alta come monitoring passivo, bassa come biomarker causale.
- **Tempo-sensibilità:** alta: sonno/crisi/rete sono finestre dinamiche.
- **Esperimento minimo di falsificazione:** actigraphy+EEG longitudinali; se nessuna relazione con crisi/rete/interventi, resta solo background.
- **Ranking:** azionabilità 3/3 · evidenza 2/3 · sicurezza 3/3 · time-to-benefit 3/3 · valore-parziale 3/3 → **14/15**
- **Status:** `ranked`
- **Note L9:** candidato a endpoint/protezione-finestra, non a terapia.

### HYP-20260705-02 — Asse JAK2/STAT3 come ponte WWOX-low → neuroinfiammazione
- **Leva:** 3
- **Tag:** `ESPANSIONE`
- **Enunciato falsificabile:** Se WWOX basso de-reprime JAK2/STAT3 anche in cellule gliali/neuronali, allora modelli WWOX-LoF dovrebbero mostrare aumento pJAK2/pSTAT3 e marker inflammatory, riducibili da interventi anti-JAK in vitro.
- **Meccanismo:** paper RNF138/NPC: WWOX mRNA destabilizzato → JAK2/STAT3 attivo → PD-L1/immune evasion.
- **Evidenza PRO:** [[discovery_ledger_current#DL-MECH-014 — Asse RNF138→hnRNPA0→WWOX mRNA→JAK2/STAT3/PD-L1: WWOX come freno di segnale immuno-oncologico|DL-MECH-014]], convergenza direzionale con neuroinfiammazione WWOX [[discovery_ledger_current#DL-MECH-012 — WWOX è un *freno* del segnale infiammatorio: la sua perdita de-reprime microgliosi/astrogliosi e cascata citochinica (asse Aldaz, multi-tessuto)|DL-MECH-012]].
- **Evidenza CONTRO / incertezze:** oncologia, abstract-only, nessun dato CNS/WOREE; JAK inhibitors immunosoppressivi.
- **Sicurezza (BLOCCO 1):** **giallo-rosso**. JAK inhibition sistemica in bambina DEE = rischio infezioni/emato; non sale senza dati neuro-WWOX specifici.
- **Traslabilità al modello di malattia:** solo come esperimento in vitro/glia, non come proposta clinica.
- **Tempo-sensibilità:** media, se neuroinfiammazione è driver progressivo.
- **Esperimento minimo di falsificazione:** misurare pSTAT3/pJAK2 in iPSC/glia WWOX-LoF ± rescue WWOX; se assente, parcheggiare.
- **Ranking:** azionabilità 1/3 · evidenza 1/3 · sicurezza 0/3 · time-to-benefit 1/3 · valore-parziale 2/3 → **5/15**
- **Status:** `flagged`
- **Note L9:** non proporre a Layer 9; solo next-search/meccanismo.

### HYP-20260705-03 — SCD5/oleic-acid/macrophage axis come ponte immunometabolico WWOX
- **Leva:** 3 + 5
- **Tag:** `ESPANSIONE`
- **Enunciato falsificabile:** Se WWOX-LoF spinge un asse lipidico-immunitario, allora modelli neuro-WWOX dovrebbero mostrare alterazioni SCD5/OA e polarizzazione microgliale/macrofagica normalizzabili da rescue WWOX.
- **Meccanismo:** WWOX deficiency → SCD5/OA → M2-like macrophage polarization in HCC.
- **Evidenza PRO:** [[discovery_ledger_current#DL-MECH-015 — WWOX/NME2/KAT1/SCD5/oleic-acid axis: ponte immunometabolico verso macrofagi M2|DL-MECH-015]], coerenza con WWOX neuroinflammation [[discovery_ledger_current#DL-MECH-012 — WWOX è un *freno* del segnale infiammatorio: la sua perdita de-reprime microgliosi/astrogliosi e cascata citochinica (asse Aldaz, multi-tessuto)|DL-MECH-012]].
- **Evidenza CONTRO / incertezze:** tumore/fegato, non microglia; SCD5 inhibitors non sono una via pediatrica pronta.
- **Sicurezza (BLOCCO 1):** giallo. Qualunque modulazione lipidica sistemica richiede cautela; ok come readout in vitro.
- **Traslabilità al modello di malattia:** media come biomarker/metabolomics hypothesis, bassa come farmaco.
- **Tempo-sensibilità:** media.
- **Esperimento minimo di falsificazione:** lipidomics in cellule WWOX-LoF/rescue; misurare OA/SCD5 e marker microgliali.
- **Ranking:** azionabilità 1/3 · evidenza 2/3 · sicurezza 1/3 · time-to-benefit 1/3 · valore-parziale 2/3 → **7/15**
- **Status:** `ranked`
- **Note L9:** non ancora; può alimentare meta-neuroinfiammazione/metabolismo.

### HYP-20260705-04 — Bcl-XL/Mcl-1 lysosomal turnover come safety-readout per strategie pro-WWOX/proteostasi
- **Leva:** 5
- **Tag:** `IPOTESI`
- **Enunciato falsificabile:** Se aumentare/stabilizzare WWOX modifica Bcl-XL/Mcl-1, allora nei saggi di rescue Q230P va controllato che non si induca stress apoptotico eccessivo.
- **Meccanismo:** WWOX induction promuove degradazione lisosomiale di Bcl-XL/Mcl-1 sotto stress.
- **Evidenza PRO:** [[discovery_ledger_current#DL-MECH-016 — WWOX induction degrada Bcl-XL/Mcl-1 via lisosoma: stress-response e proteostasi anti-apoptotica|DL-MECH-016]], collegamento a TX-003.
- **Evidenza CONTRO / incertezze:** cell model/stress context; non è dimostrato in neuroni WWOX-DEE.
- **Sicurezza (BLOCCO 1):** verde come readout; rosso per farmaci anti-Bcl/Mcl come terapia pediatrica.
- **Traslabilità al modello di malattia:** utile nei test in vitro di chaperone/proteostasis.
- **Tempo-sensibilità:** bassa-media.
- **Esperimento minimo di falsificazione:** in cellule donor-derived-derived, dopo stabilizzatore/proteostasis rescue, misurare WWOX, Bcl-XL, Mcl-1, caspase/viability.
- **Ranking:** azionabilità 2/3 · evidenza 2/3 · sicurezza 3/3 · time-to-benefit 2/3 · valore-parziale 2/3 → **11/15**
- **Status:** `ranked`
- **Note L9:** come safety-readout associato a TX-003, non nuova terapia.

### HYP-20260705-05 — Zfra peptide: monitorare ma non promuovere
- **Leva:** 3
- **Tag:** `ESPANSIONE`
- **Enunciato falsificabile:** Se Zfra sopprime neurodegenerazione via rete WWOX-independent o context-specific, allora modelli WWOX-LoF dovrebbero mostrare beneficio senza ulteriore riduzione dannosa di WWOX.
- **Meccanismo:** Zfra interagisce con WWOX e viene riportato come soppressore di neurodegenerazione, ma può accelerare degradazione WWOX.
- **Evidenza PRO:** [[discovery_ledger_current#DL-MOL-006 — Zfra peptide come asse neurodegeneration-suppression WWOX-related|DL-MOL-006]].
- **Evidenza CONTRO / incertezze:** rischio teorico forte in WWOX-LoF: degradare WWOX è la direzione sbagliata se resta proteina residua utile. Full text Lee 2017 (PMID 29067327): numeri/attrition incoerenti, peptide non rilevato nel cervello, cross-link/degradazione proteica non selettiva, beneficio ipotizzato via milza e fallimento con trattamento più tardivo.
- **Sicurezza (BLOCCO 1):** rosso. Peptide sperimentale, nessun profilo pediatrico/CNS.
- **Traslabilità al modello di malattia:** molto bassa.
- **Tempo-sensibilità:** bassa.
- **Esperimento minimo di falsificazione:** test in vitro su neuroni WWOX-LoF/rescue; se riduce WWOX residuo o peggiora viability/network, refuted.
- **Ranking:** azionabilità 0/3 · evidenza 1/3 · sicurezza 0/3 · time-to-benefit 0/3 · valore-parziale 1/3 → **2/15**
- **Status:** `flagged` — confermato 2026-07-09; belief terapeutico declassato
- **Note L9:** non sale; resta monitor.

### HYP-20260705-06 — WWOX gene-delivery non-CNS come prova di principio, non strategia di riferimento
- **Leva:** 1
- **Tag:** `ESPANSIONE`
- **Enunciato falsificabile:** Se diverse piattaforme riescono a ripristinare WWOX localmente, allora il problema centrale per il genotipo di riferimento non è "WWOX non consegnabile" ma "delivery CNS, timing, dose e sicurezza".
- **Meccanismo:** hydrogel lentivirale intravescicale WWOX in bladder cancer mostra local delivery WWOX con immuno/ROS effects.
- **Evidenza PRO:** PMID 40006511 / PMCID PMC11858974; coerente con AAV WWOX già in TX-005.
- **Evidenza CONTRO / incertezze:** completamente non-CNS, oncologia, lentiviral/hydrogel intravescicale non trasferibile a cervello.
- **Sicurezza (BLOCCO 1):** non applicabile al genotipo di riferimento; no proposta clinica.
- **Traslabilità al modello di malattia:** bassa biologicamente, media solo come "delivery principle".
- **Tempo-sensibilità:** bassa.
- **Esperimento minimo di falsificazione:** nessuno per il genotipo di riferimento; usare solo come tecnologia comparativa.
- **Ranking:** azionabilità 0/3 · evidenza 1/3 · sicurezza 1/3 · time-to-benefit 0/3 · valore-parziale 1/3 → **3/15**
- **Status:** `parked`
- **Note L9:** non sale.

### HYP-20260705-07 — Folate/neural-tube bridge resta background, non repurposing
- **Leva:** 4
- **Tag:** `ESPANSIONE`
- **Enunciato falsificabile:** Se folate-pathway modifies early neural development risk, allora potrebbe informare solo contesto prenatale/metabolico, non una nuova leva WWOX postnatale.
- **Meccanismo:** folate×genetic risk in neural tube defects, non WWOX-specific.
- **Evidenza PRO:** PMID 41378749 nel batch.
- **Evidenza CONTRO / incertezze:** nessun WWOX direct, nessuna ipotesi terapeutica nuova per il genotipo di riferimento; folinato già nel BLOCCO 1 come contesto separato.
- **Sicurezza (BLOCCO 1):** verde solo come non-modifica; non usare per cambiare terapia.
- **Traslabilità al modello di malattia:** bassa.
- **Tempo-sensibilità:** storicamente prenatale, quindi non azionabile ora.
- **Esperimento minimo di falsificazione:** non prioritario.
- **Ranking:** azionabilità 0/3 · evidenza 1/3 · sicurezza 2/3 · time-to-benefit 0/3 · valore-parziale 0/3 → **3/15**
- **Status:** `parked`
- **Note L9:** non sale.

### HYP-20260705-08 — Corrigendum WWOX/p73/HIF1A come evidence-safety gate
- **Leva:** 5
- **Tag:** `IPOTESI`
- **Enunciato falsificabile:** Se il corrigendum al paper WWOX/p73/HIF1A modifica figure/dati chiave, allora ogni ipotesi metabolica basata su quel paper deve essere declassata o corretta.
- **Meccanismo:** non è una terapia; è un gate qualità per il ramo HIF1A/glycolysis.
- **Evidenza PRO:** INBOX-009 / FT-015, PMID 40263068.
- **Evidenza CONTRO / incertezze:** testo del corrigendum non ancora analizzato; potrebbe essere solo correzione formale.
- **Sicurezza (BLOCCO 1):** verde come audit; impedisce overclaim.
- **Traslabilità al modello di malattia:** alta come igiene epistemica.
- **Tempo-sensibilità:** media: evita costruire su base difettosa.
- **Esperimento minimo di falsificazione:** recuperare corrigendum e confrontare con paper originale.
- **Ranking:** azionabilità 3/3 · evidenza 1/3 · sicurezza 3/3 · time-to-benefit 3/3 · valore-parziale 2/3 → **12/15**
- **Status:** `ranked`
- **Note L9:** non terapia; priorità di full-text check.

---

## Sintesi ranking 2026-07-05
| Rank | ID | Ipotesi | Verdetto |
|---:|---|---|---|
| 1 | HYP-20260705-01 | Sleep/network-state endpoint | usare come monitoring candidate, non biomarker WWOX |
| 2 | HYP-20260705-08 | Corrigendum HIF1A/p73 gate | verificare prima di rafforzare metabolismo |
| 3 | HYP-20260705-04 | Bcl-XL/Mcl-1 safety-readout | aggiungere ai test proteostasi Q230P |
| 4 | HYP-20260705-03 | SCD5/OA immunometabolic bridge | next-search microglia/metabolomics |
| 5 | HYP-20260705-02 | JAK2/STAT3 bridge | flagged: solo in vitro/ricerca |
| 6 | HYP-20260705-06 | hydrogel/lentiviral WWOX delivery | parked, technology-only |
| 7 | HYP-20260705-07 | folate bridge | parked |
| 8 | HYP-20260705-05 | Zfra peptide | flagged, non salire |

## Change-log
- **2026-07-05** — sessione forge su PubMed GALNT14/export batch: 8 ipotesi generate, 8 stress-tested/ranked, 2 flagged, 2 parked, 0 proposed-to-L9. Nessun parere medico; output non canonico.
- **2026-07-09** — batch storico 50: Zfra ulteriormente declassato; evodiamina/digossina/paclitaxel-axis parcheggiati o esclusi come candidati clinici. Nuove ipotesi usate solo come pannelli sperimentali HIF/UPR/DDR; 0 proposte a Layer 9.

---

## Run 2026-07-09 — ipotesi dal batch 50-studi WWOX 2015–2016

> Generate da `legend-hypothesis-forge` a valle della lettura integrale di 12 full-text. Nessuna è un DATO. Nessuna è parere medico.

### HYP-20260709-01 — Dieta chetogenica con razionale WWOX-specifico (non solo antiepilettico empirico)
- **Leva:** 2 (compensazione-pathway) + 4 (protezione-finestra)
- **Tag:** `IPOTESI`
- **Enunciato falsificabile:** Se la perdita di WWOX de-reprime HIF1α → PDK → blocca PDH, allora le cellule donor-derived mostreranno un rapporto glicolisi/OXPHOS spostato (Seahorse: ECAR↑, OCR↓) e i corpi chetonici, entrando nel TCA **a valle di PDH**, dovrebbero ripristinare flusso ossidativo *senza* dover riattivare PDH.
- **Meccanismo:** MEF Wwox-KO → ↑glucosio, ↑lattato, ↓ATP, ↓consumo O₂, **HIF1α↑ in normossia**; inibizione di HIF1α reverte il fenotipo. GLUT1 inversamente correlato a WWOX. La KD bypassa la glicolisi fornendo acetil-CoA direttamente al ciclo di Krebs.
- **Evidenza PRO:** [[discovery_ledger_current#DL-MECH-020 — WWOX-loss induce un fenotipo Warburg-like via HIF1α: razionale meccanicistico WWOX-specifico per la dieta chetogenica|DL-MECH-020]] (DATO in MEF/cancro); convergenza indipendente: la KD è già standard-of-care nelle encefalopatie epilettiche, e la **GLUT1-deficiency** — un'encefalopatia da difetto di ingresso del glucosio — è trattata proprio con KD. Wwox-KO murino ha **ipoglicemia**.
- **🔺 UPGRADE 2026-07-10 — il caveat principale è caduto.** Avevo scritto che il fenotipo Warburg era documentato "in MEF e in cancro, **mai nel neurone WWOX-carente**". **Falso**: Steinberg 2021 ([[discovery_ledger_current#🎯 DL-MECH-034 — Il fenotipo Warburg è confermato **in tessuto neurale umano**: chiude il gap che indeboliva l'ipotesi chetogenica|DL-MECH-034]], PMID 34268881) mostra per RNA-seq su **organoidi cerebrali umani WWOX-KO** l'inibizione della fosforilazione ossidativa e della sintesi di ATP accoppiata al trasporto di elettroni, con arricchimento della glicolisi. Modello indipendente, tecnica diversa, **tessuto neurale umano**. Il razionale WWOX-specifico esce sostanzialmente rafforzato. (Quel paper era in corpus, Tier A, mai letto — vedi [[discovery_ledger_current#^fm-015|FM-015]].)
- **⚠️ Evidenza CONTRO / la contraddizione che resta aperta:** il topo Wwox-KO muore di ipoglicemia a 4 settimane — il genotipo di riferimento no. E soprattutto: **l'unico dato di spettroscopia cerebrale umana in un paziente WWOX riporta lattato "estremamente basso"**, non alto ([[discovery_ledger_current#⚠️ DL-BIO-008 — Contraddizione sul lattato: alto nel siero del topo, **"extremely low" nell'MRS cerebrale umana**|DL-BIO-008]], Davids 2019); l'unico screening metabolico umano completo in un WOREE null è **interamente normale** (Abdel-Salam 2014). Il modello Warburg predice lattato alto. **La direzione del metabolismo umano WWOX-deficiente non è stata misurata.** Il razionale poggia sul blocco PDK1→PDH e sulla OXPHOS depressa — non sul lattato — quindi non è falsificato; ma **abbiamo perso l'endpoint più facile per verificarlo**, e questo è un peggioramento reale della testabilità.
- Il trascrittoma non è il flusso metabolico: l'espressione genica di OXPHOS/glicolisi **non dimostra** un flusso alterato (serve Seahorse/fluxomica). N basso (WT n=2, KO n=4). Il ramo HIF1α/WWOX è stato lavorato anche dal gruppo Desiderio, oggi in watchlist per ritrattazioni → **non conta come corroborazione indipendente**.
- **🔺 UPGRADE 2026-07-09b (dati primari acquisiti, PMID 25012504 / PMC4211377):** l'anello mancante è stato misurato. Nei Wwox-KO **PDK1 è direttamente upregolato** (qRT-PCR), insieme a **GLUT1, HK2, PKM2**, PFK-1, aldolasi, TPI. In vivo: **lattato sierico ↑, ipoglicemia, morte entro 4 settimane**. WWOX lega HIF1α **via WW1** (GST-pulldown; il mutante W44F/P47A non lega). L'inibizione farmacologica di HIF1α (**digossina**) reverte il fenotipo nei KO. → La catena `WWOX↓ → HIF1α↑ → PDK1↑ → ⊣PDH` **non è più un'inferenza a due salti: l'enzima-chiave è misurato come sovraespresso.** Vedi [[discovery_ledger_current#DL-BIO-007 — Lattato sierico, glicemia e insulina come biomarcatori metabolici in vivo del deficit di WWOX|DL-BIO-007]], [[discovery_ledger_current#DL-MECH-028 — WWOX lega HIF1α via **WW1**, non via SDR: l'asse metabolico potrebbe essere parzialmente preservato in Q230P|DL-MECH-028]].
- **Sicurezza (BLOCCO 1):** 🟢 **verde.** Intervento dietetico già in uso pediatrico nelle EE, con monitoraggio noto (acidosi, calcolosi, crescita, dislipidemia). Nessuna molecola nuova, nessun problema BBB. Il rischio è gestito da un protocollo esistente, non da noi.
- **Traslabilità al modello di malattia:** alta.
- **⚖️ CONTRAPPESO ONESTO (2026-07-09c):** avevo scritto che "la letteratura sul null non ha mai testato questa leva". **È falso.** Oliver 2023 ([[discovery_ledger_current#DL-MECH-030 — Genotipo e mortalità in WWOX-DEE: il dato prognostico più diretto che esista per il genotipo di riferimento (e i suoi limiti)|DL-MECH-030]]) riporta che nella sua coorte WWOX-DEE la **dieta chetogenica è stata tentata in 3 pazienti e continuata solo in 1** (2 sospese per scarsa tolleranza o beneficio). Non è una misura di efficacia — è un pattern di continuazione — ma è un segnale del mondo reale che **va nella direzione opposta** al razionale meccanicistico. Il razionale resta valido; l'aspettativa di beneficio va calibrata verso il basso. Per contro, **il cannabidiolo è stato continuato in 4/4** pazienti che lo hanno iniziato.
- **Tempo-sensibilità:** alta (mielinizzazione e carico di crisi degradano precocemente — vedi [[discovery_ledger_current#DL-MECH-022 — Posizionamento genotipo-fenotipo: il genotipo di riferimento sta tra il null puro (WOREE) e l'ipomorfo (SCAR12)|DL-MECH-022]]).
- **Esperimento minimo di falsificazione:** **Seahorse OCR/ECAR su fibroblasti o LCL del genotipo di riferimento** vs controllo — ora l'unico endpoint valido, dato che il lattato è ambiguo. Se il profilo bioenergetico è normale, il razionale WWOX-specifico cade. Secondo test, a costo quasi zero: **Seahorse sugli organoidi WWOX-KO** già esistenti nel lab Aqeilan (chiuderebbe il salto trascrittoma→flusso).
- **🔻 RICALIBRAZIONE 2026-07-10c ([[discovery_ledger_current#DL-BIO-009 — Il metabolismo umano nel deficit di WWOX è, per quanto misurato, **normale**. Il modello murino non si trasferisce.|DL-BIO-009]]):** il metabolismo umano nel deficit di WWOX è, per quanto misurato, **normale**. Quattro fonti indipendenti: Shaukat 2018 (due pazienti — lattato, ammonio, acilcarnitine, aminoacidi, acidi organici, transferrina: tutti normali), Abdel-Salam 2014 (screening metabolico e mitocondriale completo, normale), Battaglia 2023 (MRS normale). L'unico outlier (lattato cerebrale bassissimo, Davids 2019) ha una seconda variante confondente in HSPG2.
  → Il fenotipo Warburg è **robusto nel topo e negli organoidi, ma non si manifesta come anomalia biochimica misurabile nel paziente**. Non è una contraddizione logica (un difetto bioenergetico neuronale può non alterare il metabolismo sistemico), ma significa che **non esiste oggi alcun biomarcatore metabolico utilizzabile nel genotipo di riferimento**, né periferico né MRS. **Non cercare conferme nel sangue: sono già state cercate quattro volte, e sono normali.**
  L'unico test che può falsificare l'ipotesi resta il **Seahorse OCR/ECAR su cellule donor-derived**. Se anche quello risultasse normale, l'ipotesi cade.
- **Ranking (aggiornato 2026-07-10c):** azionabilità 3/3 · **evidenza 2/3** (il Warburg è documentato in modelli, mai nel paziente) · sicurezza 3/3 · time-to-benefit 3/3 · valore-parziale 2/3 (KD abbandonata in 2/3 dei casi WWOX in cui è stata tentata) → **13/15**
- **Status:** `ranked` → **`proposed-to-L9`**
- **Note L9:** ⚠️ **La KD è una decisione clinica del team curante, non di questo sistema.** Ciò che questo batch aggiunge non è "provate la chetogenica" — è un **razionale meccanicistico WWOX-specifico** da mettere sul tavolo del confronto clinico, insieme all'esperimento (Seahorse) che lo può falsificare prima di qualunque decisione.

### HYP-20260709-02 — Boost dell'espressione di WWOX da solo ha verso incerto: va accoppiato a stabilizzazione di Q230P
- **Leva:** 1 (correzione-difetto) + 2
- **Tag:** `IPOTESI`
- **Enunciato falsificabile:** Se Q230P è prevalentemente misfolded e degradata, allora aumentare la trascrizione/traduzione di WWOX **non** aumenterà la proteina funzionale in proporzione, e potrà aumentare il carico proteotossico (UPS saturato, aggregati). Se invece Q230P folda parzialmente, il boost aumenterà la proteina residua funzionale.
- **Meccanismo:** tre leve indipendenti documentate su WWOX endogeno — miR-153 (repressore, 3'UTR), contesto **Kozak rs11545028** (l'allele T, −5 dall'ATG, **abbassa** traduzione: luciferasi p<0.05 in 3 linee, qPCR, IHC p=0.022, eQTL GTEx), sito **Sp1/Sp3 rs11644322** (introne 8; allele G lega Sp1 più forte → più WWOX; EMSA + supershift). Tutte agiscono sul **trascritto endogeno, non allele-specificamente**.
- **Evidenza PRO:** i tre paper dimostrano che trascrizione e traduzione di WWOX sono **colli di bottiglia realmente modulabili** (DATO). In tutti e tre, ↓WWOX = peggio → la direzione "aumentare WWOX" è oncologicamente sicura.
- **Evidenza CONTRO / incertezze:** ⚠️ **asimmetria cruciale.** L'allele di sito accettore del genotipo di riferimento (c.1057-2A>G) produce trascritto aberrante destinato a NMD: **up-regolarlo spinge solo più trascritto verso la degradazione**, senza proteina utile. Quindi un boost non-allele-specifico amplifica **prevalentemente l'allele Q230P** — e il segno del beneficio dipende *interamente* dal destino di folding di Q230P, ad oggi **ignoto**. Più sintesi di una proteina destabilizzata (ΔΔG +1.51 kcal/mol) in un neurone può essere neutro **o dannoso**.
- **Sicurezza (BLOCCO 1):** 🟡 **giallo.** Non per tossicità d'organo, ma per **rischio proteotossico** e per il fatto che WWOX è pro-apoptotico in contesti sperimentali (Drosophila: WWOX↑ → ROS↑, potenzia l'eliminazione cellulare Egr/TNFα-mediata). **L'obiettivo è ripristinare la funzione fisiologica, non sovra-attivare.**
- **Traslabilità al modello di malattia:** condizionata. **Non promuovibile finché non è caratterizzato sperimentalmente il fenotipo di Q230P** (quanta proteina residua? degradata o aggregata? lega ancora i partner SDR?).
- **Esperimento minimo di falsificazione:** quantificazione allele-specifica di RNA e **sintesi nascent** (pulse-labeling), frazionamento solubile/insolubile, emivita e test di boost controllato; associare sempre abbondanza a funzione.
- **Ranking:** azionabilità 1/3 · evidenza 2/3 · sicurezza 2/3 · time-to-benefit 1/3 · valore-parziale 2/3 → **8/15**
- **STATUS: `stress-tested` (repair 2026-07-14).** Il precedente `refuted` è ritirato: Johannsen mostra mRNA normale + proteina non rilevata, ma lascia aperta **traduzione compromessa oppure degradazione prematura**. Il boost resta condizionato e non prioritario finché il collo di bottiglia non è separato; non va accoppiato automaticamente né escluso automaticamente.
- **Corollario:** confrontare boost, rescue del turnover e combinazione nello stesso sistema Q230P, con controllo della funzione e del carico proteotossico.

### HYP-20260709-03 — Anti-miR-153 per de-reprimere WWOX endogeno
- **Leva:** 3 (repurposing / oligonucleotide)
- **Tag:** `ESPANSIONE`
- **Enunciato falsificabile:** Se miR-153 reprime WWOX anche nel tessuto neurale, allora un antagomiR-153 aumenterebbe la proteina WWOX residua.
- **Meccanismo:** in HCC, miR-153 lega il 3'UTR di WWOX; antisense/antagomir → **↑ marcata di proteina WWOX** in vitro e **in vivo** (antagomir sistemico, modello DEN); mutagenesi del seed abolisce l'effetto (specificità confermata).
- **Evidenza PRO:** è l'unico esperimento del batch in cui **inibire un repressore aumenta davvero la proteina WWOX in un animale**.
- **Evidenza CONTRO / incertezze:** ⚠️ (a) il paper **non dice se miR-153 è espresso nel cervello** — studia solo fegato; (b) la sequenza/posizione del sito 3'UTR è **solo in figura**, non nel testo; (c) il paper (Oncotarget 2015) ha refusi sostanziali ("miR-163", "miR-300 mimics" dove intende miR-153) → **trust-but-critical**; (d) miR-153 ha molti altri bersagli documentati (PTEN, AKT) → un antagomiR è **pleiotropico**.
- **Sicurezza (BLOCCO 1):** 🔴 **rosso.** Non è WWOX-specifico. Off-target di un antagomiR nel CNS pediatrico (incl. de-repressione di oncogeni via PTEN/AKT) sono un rischio non caratterizzato. Inoltre eredita per intero il problema di HYP-02: amplificherebbe l'allele Q230P misfolded.
- **Status:** `stress-tested` → **`flagged`** — non promuovibile. Conservato perché *dimostra il principio* (de-reprimere WWOX endogeno è possibile in vivo), non perché sia la molecola.
- **Prossimo passo a costo zero:** verificare da fonte dedicata l'espressione cerebrale di miR-153 e recuperare da TargetScan il sito esatto sul 3'UTR di WWOX.

### HYP-20260709-04 — Peptide pTyr33-WWOX come rescue funzionale a valle della variante
- **Leva:** 2 + 3
- **Tag:** `ESPANSIONE`
- **Enunciato falsificabile:** Se un peptide pTyr33-WWOX ripristina segnale WWOX-dipendente in vivo, allora dovrebbe mitigare il fenotipo neurologico anche in un modello WWOX-deficiente (non solo MPP+).
- **Meccanismo:** un peptide-mimetico sostituisce la funzione a valle senza dover correggere l'allele — aggira sia il difetto di splicing sia il misfolding dell'allele missense.
- **Evidenza PRO:** Sze 2015 riporta che il peptide **mitiga la sindrome Parkinson-like da MPP+ nel ratto** e lo propone esplicitamente "for the restoration of neural function under WWOX deficiency in vivo".
- **Evidenza CONTRO / incertezze:** il dato è **su MPP+, non su WWOX-null**. Il commentary non riporta dose, via di somministrazione, penetrazione BBB, durata. Fonte primaria (Lo 2008, PMID 18371080) **non ancora letta**.
- **Sicurezza (BLOCCO 1):** ⚪ non valutabile — nessun dato ADMET/BBB.
- **🔻 STATUS: `refuted` (2026-07-09b) — la premessa era sbagliata.** Acquisito l'abstract della fonte primaria (Lo CP et al. 2008, *Eur J Neurosci*, PMID 18371080, [DOI](https://doi.org/10.1111/j.1460-9568.2008.06139.x), via PubMed): *"activated WOX1 plays an **essential role in the MPP+-induced neuronal death**"*. WOX1 fosforilato in Tyr33 è **pro-apoptotico**; il peptide **blocca** la morte neuronale, cioè agisce da **inibitore competitivo** della funzione WWOX-dipendente, non da suo sostituto. In una paziente **carente** di WWOX, inibire la funzione WWOX non ripristina nulla. **Il commentary di Sze 2015 aveva sovra-interpretato il primario.** Vedi [[discovery_ledger_current#DL-MOL-008 — Peptide pTyr33-WWOX: un candidato di "restoration" già testato in vivo su un modello neurologico|DL-MOL-008]] e [[discovery_ledger_current#^fm-010|FM-010]].
- **Cosa resta:** il peptide potrebbe avere un interesse come **neuroprotettore generico** (blocca una via di morte neuronale a valle) — ma è un meccanismo diverso, mai testato in WWOX-deficiency. Non è la stessa ipotesi e non eredita il suo razionale.
- **Nota d'onestà:** il full-text è paywalled (Wiley 402); la confutazione poggia sull'abstract, che è però esplicito. Se il full-text mostrasse altro, va riaperta.

### HYP-20260709-05 — Dicloroacetato (DCA) per riattivare PDH a valle del blocco HIF1α→PDK
- **Leva:** 3 (repurposing)
- **Tag:** `IPOTESI` / `ESPANSIONE`
- **Enunciato falsificabile:** Se in WWOX-deficiency HIF1α↑ induce PDK che inibisce PDH, allora un inibitore di PDK (DCA) dovrebbe riattivare PDH e ripristinare il flusso piruvato→TCA.
- **Meccanismo:** DCA è un inibitore di PDK con uso documentato in disordini mitocondriali. Il paper **non nomina DCA**: il bersaglio è implicato dal pathway (HIF1α→PDK→⊣PDH), non testato.
- **Evidenza PRO:** l'asse HIF1α→PDK→PDH è esattamente il punto in cui DCA agisce; coerente con [[discovery_ledger_current#DL-MECH-020 — WWOX-loss induce un fenotipo Warburg-like via HIF1α: razionale meccanicistico WWOX-specifico per la dieta chetogenica|DL-MECH-020]].
- **Evidenza CONTRO / incertezze:** inferenza a due salti (WWOX→HIF1α è DATO; HIF1α→PDK→PDH è biologia nota ma **non misurata in questi paper**). Nessun dato in tessuto neurale WWOX-carente.
- **Sicurezza (BLOCCO 1):** 🟡→🔴 **neurotossicità periferica dose-dipendente nota per DCA** (neuropatia). In un bambino con encefalopatia, il rapporto rischio/beneficio è sfavorevole senza prova del meccanismo.
- **Status:** `generated` → **`parked`.** **Richiede `legend-safety-triage` (ADMET/BBB/alert) prima di qualunque considerazione**, e comunque a valle della falsificazione di HYP-01 (se il profilo bioenergetico del genotipo di riferimento è normale, DCA non ha razionale). **La dieta chetogenica ottiene lo stesso bypass metabolico con un profilo di sicurezza incomparabilmente migliore** → HYP-01 domina HYP-05.

### HYP-20260709-06 — Assay di inclusione dell'esone 9 come biomarcatore abilitante e endpoint dell'ASO
- **Leva:** 5 (biomarcatore-abilitante)
- **Tag:** `IPOTESI`
- **Enunciato falsificabile:** Se c.1057-2A>G abolisce l'accettore dell'esone 9, allora una RT-qPCR che spanna la giunzione esone8→esone9 mostrerà una frazione ridotta di trascritto corretto nelle cellule donor-derived rispetto ai controlli, e tale frazione **aumenterà** se un ASO splice-correcting funziona.
- **Meccanismo:** Schirmer 2016 ha già costruito e validato un assay qPCR che quantifica separatamente i trascritti della giunzione es8-es9 e i trascritti core (es4-6) — esattamente la giunzione colpita dall'allele di sito accettore del genotipo di riferimento.
- **Evidenza PRO:** [[discovery_ledger_current#DL-BIO-003 — Assay qPCR region-specifico esone 8–9 vs core (esoni 4–6): misura diretta dell'effetto dell'allele di sito accettore|DL-BIO-003]] (DATO: assay pubblicato, n=89 LCL, r=0.68 intra-linea).
- **Evidenza CONTRO / incertezze:** loro misuravano *espressione*, non *splicing aberrante*. Servono primer che spannino la giunzione e un controllo NMD (cicloesimide/SMG1i) per smascherare il trascritto degradato. Da affiancare a RNA-seq per identificare l'evento reale (exon skipping vs intron retention vs sito criptico +8, già predetto da SpliceAI DS_AG 0.64).
- **Sicurezza (BLOCCO 1):** 🟢 **verde** — è una misura su cellule, nessun intervento sull'individuo oltre a un prelievo/biopsia standard del percorso diagnostico.
- **Traslabilità al modello di malattia:** alta e immediata.
- **Ranking:** azionabilità 3/3 · evidenza 2/3 · sicurezza 3/3 · time-to-benefit 2/3 · valore-parziale 3/3 → **13/15**
- **Status:** `ranked` → **`proposed-to-L9`**
- **Note L9:** **abilita [[therapeutic_strategies_current#TX-001 — Correcting a canonical splice-acceptor allele: RNA assay → ASO/editing choice|TX-001]] (ASO splice-correcting).** Senza un endpoint molecolare misurabile, un ASO non è testabile: questo assay è il pezzo mancante. È il contributo più concreto del batch alla leva 1.

### HYP-20260709-07 — Pro-mielinizzanti per la finestra mielinica, **condizionata a un esperimento che nessuno ha ancora fatto**
- **Leva:** 4 (protezione-finestra) + 3 (repurposing)
- **Tag:** `IPOTESI`
- **Enunciato falsificabile:** Se l'ipomielinizzazione WWOX-dipendente è un **arresto della maturazione** degli oligodendrociti (precursori presenti che non differenziano) e non una perdita di precursori, allora un pro-mielinizzante che sblocca il differenziamento degli OPC dovrebbe aumentare MBP/CNPase e il numero di oligodendrociti maturi in un modello WWOX-deficiente.
- **Meccanismo:** nel ratto *lde/lde* (lesione esone 9, **lo stesso esone dell'allele di sito accettore del genotipo di riferimento**): MBP e CNPase severamente ridotti da PND5, **oligodendrociti maturi (APC/CC1) ridotti** da PND15 — mentre **numero di neuroni, spessore corticale e distribuzione per strato sono normali**. Wwox è espresso negli oligodendrociti (primo report). Nel W44X umano la mielinizzazione è persa già a 9 settimane, progressivamente.
- **Evidenza PRO:** [[discovery_ledger_current#DL-MECH-027 — Nel *lde*: ipomielinizzazione con oligodendrociti maturi ridotti e **neuroni intatti**. Il substrato è salvabile|DL-MECH-027]] (DATO, full-text); [[discovery_ledger_current#DL-MECH-022 — Posizionamento genotipo-fenotipo: il genotipo di riferimento sta tra il null puro (WOREE) e l'ipomorfo (SCAR12)|DL-MECH-022]] (mielina persa a 9 settimane nel null umano); il danno è di **maturazione/connettività, non di sopravvivenza neuronale** → c'è substrato da salvare. Esistono pro-mielinizzanti già in uomo: **clemastina** (antistaminico approvato, ha superato un trial di fase II nella sclerosi multipla con endpoint di latenza VEP), benztropina, miconazolo, **T3/ormone tiroideo**, quetiapina.
- **⚠️ Evidenza CONTRO / il vincolo che decide tutto:** **Tochigi 2019 non conta i precursori** (nessun NG2, PDGFRα, Olig2). Misura solo i maturi. Quindi **non sappiamo se gli OPC ci sono e non maturano, o se mancano.** Se mancano, non c'è nulla da sbloccare e l'intera ipotesi cade. Gli indizi interni inclinano verso l'arresto di maturazione, ma **non lo dimostrano**. Inoltre: ratto ≠ uomo; il *lde* modella il lato **splice-null** del genotipo di riferimento, non Q230P; e il segno del fenotipo gliale è **regione- e modello-dipendente** (Hussain 2019 trova gliosi ippocampale, Tochigi riduzione corticale).
- **Sicurezza (BLOCCO 1):** 🟡 **giallo, in attesa.** La clemastina è approvata, penetra la BBB, ha un profilo pediatrico noto come antistaminico — ma sedazione e effetti anticolinergici in un bambino con encefalopatia epilettica non sono banali, e nella SM l'effetto sulla remielinizzazione era **modesto**. **Nessuna molecola sale a L9 senza `legend-safety-triage`.**
- **Traslabilità al modello di malattia:** potenzialmente alta, **ma il prerequisito non è soddisfatto.**
- **Tempo-sensibilità:** massima. La finestra mielinica si chiude presto (PND5-21 nel ratto; 9 settimane nel W44X umano).
- **Esperimento minimo che decide:** conta OPC (NG2/PDGFRα/Olig2) nella corteccia *lde/lde*, e differenziamento in vitro di OPC *lde/lde* ± pro-mielinizzante. **È l'esperimento singolo a più alta resa emerso da tutto il batch**: apre o chiude un'intera leva terapeutica.
- **🔄 RIORIENTAMENTO (2026-07-09c) — il prerequisito che avevo posto era la domanda sbagliata.** Ho eseguito il "prossimo passo a costo zero": **nessuno ha mai contato gli OPC in un modello WWOX-deficiente** (query PubMed `WWOX AND (Olig2 OR NG2 OR PDGFRA OR oligodendrocyte precursor)` → **0 risultati**). Ma la risposta è arrivata da un'altra direzione, ed è più informativa: **Repudi 2021 (via Obeid 2026, [[discovery_ledger_current#DL-MECH-031 — L'ipomielinizzazione WWOX è **secondaria al neurone**, non un difetto autonomo dell'oligodendrocita. E la finestra della terapia genica è neonatale|DL-MECH-031]]) mostra che la delezione di Wwox negli oligodendrociti (Olig2-Cre) e negli astrociti (GFAP-Cre) NON produce anomalie evidenti, mentre la delezione nei neuroni (Synapsin-Cre) ricapitola l'intero fenotipo, difetti di mielina inclusi.** E la terapia genica **neurone-ristretta** (hSynI) recupera la mielina, mentre quella diretta agli oligodendrociti non fa nulla (con il caveat, dichiarato dagli autori, che AAV9 ha scarso tropismo oligodendrocitario per via ICV neonatale → quel braccio è tecnicamente confuso).
- **Conclusione:** l'ipomielinizzazione WWOX-dipendente è in larga parte **secondaria al difetto neuronale/assonale, non autonoma dell'oligodendrocita**. Contare gli OPC non era la domanda decisiva: **anche se ci fossero tutti, spingerli da soli renderebbe poco**, perché non ricevono il segnale assonale.
- **Ranking (rivisto):** azionabilità 1/3 · evidenza 1/3 · sicurezza 2/3 · time-to-benefit 3/3 · valore-parziale 2/3 → **9/15**
- **Status:** `stress-tested` → **`parked`** — un pro-mielinizzante **oligodendrocita-autonomo** non è la leva giusta. Non `refuted`: il braccio AAV-oligo è confuso, e un beneficio parziale non è escluso.
- **La leva si sposta:** poiché la mielinizzazione è **attività-dipendente**, ridurre il carico di crisi potrebbe migliorare la mielina **indirettamente**. `IPOTESI`
- **🔻 MA INDEBOLITA IL 2026-07-10c, e va detto.** Shaukat 2018 ([[discovery_ledger_current#🔴 DL-MECH-039 — È una **DEE, non una EE**: controllare le crisi non salva lo sviluppo. E questo tocca la logica stessa di "guadagnare tempo".|DL-MECH-039]]) documenta che in WWOX **il deficit cognitivo precede le crisi e non migliora quando le crisi vengono controllate**: nel loro caso 1 il vigabatrin **ha risolto gli spasmi** e a due anni il bambino era comunque profondamente ritardato. È una **DEE**, non una EE. Converge con Oliver 2023 (l'unico paziente non farmaco-resistente è morto a 8 anni).
  → L'anello finale della catena "meno crisi → più mielina → migliore sviluppo" **non è supportato**. Il controllo delle crisi resta importante per qualità di vita, prevenzione dello stato epilettico e del SUDEP — **ma non va contato come protezione dello sviluppo.**
- **Ranking (rivisto 2026-07-10c):** azionabilità 1/3 · evidenza 1/3 · sicurezza 2/3 · time-to-benefit 2/3 · valore-parziale 1/3 → **7/15**. Resta `parked`.
- **Corollario che rafforza il resto del portafoglio:** se l'esito di sviluppo non risponde al controllo dei sintomi, **solo le leve causali possono modificarlo** — terapia genica e rescue proteostatico dell'allele Q230P. Coerente con Obeid 2026, dove il rescue *neuronale* recupera comportamento, mielina e sopravvivenza, mentre nessun antiepilettico lo fa.

### HYP-20260709-08 — Allele missense SDR: distinguere difetto di sintesi, insolubilità e turnover prima del rescue proteostatico
- **Leva:** 1 (correzione-difetto, sull'allele missense)
- **Tag:** `IPOTESI` condizionata su un `DATO` umano di endpoint, non di meccanismo
- **Enunciato falsificabile:** se Q230P è sintetizzata a velocità normale e degradata prematuramente, un intervento sul turnover deve aumentare proteina **solubile e funzionale**; se la sintesi è ridotta, il rescue degradativo da solo non deve funzionare. Il confronto fra questi esiti decide quale ramo proseguire.
- **Meccanismo — questo è il punto:** Johannsen 2018 ([[discovery_ledger_current#🔴 DL-MECH-029 — Q230P: trascritto normale, **proteina non rilevata**; causa traduttiva versus degradativa non risolta|DL-MECH-029]]) misura, in **fibroblasti di due sorelle omozigoti per la variante su Gln230**: **trascritto WWOX a livelli normali, proteina WWOX assente** (qRT-PCR + Western blot). Gli autori concludono per *"impaired translation or premature degradation"*. Dunque, sull'allele missense del genotipo di riferimento:
  - ✅ la **trascrizione funziona** (l'mRNA c'è, in quantità normale);
  - ✅ **non c'è NMD** (è un missense, non un codone di stop prematuro);
  - ✅ **non serve un ASO** (non è un difetto di splicing — quello è l'allele *di sito accettore*);
  - ⚠️ **il collo di bottiglia non è identificato:** Johannsen propone traduzione compromessa **oppure** degradazione prematura e non misura sintesi o turnover.
  Il primo obiettivo è distinguere i rami, non scegliere in anticipo la terapia.
- **Evidenza PRO:** [[discovery_ledger_current#🔴 DL-MECH-029 — Q230P: trascritto normale, **proteina non rilevata**; causa traduttiva versus degradativa non risolta|DL-MECH-029]] dimostra l'endpoint sulla variante esatta. AlphaFold/ESM-2/ThermoMPNN (+1.514 kcal/mol) rendono plausibile una perturbazione di core, ma non discriminano sintesi, insolubilità o degradazione e non dimostrano recuperabilità.
- **Evidenza CONTRO / le tre incertezze che contano:**
  1. ⚠️ **L'assunzione centrale non è testata da nessuno: che Q230P, una volta ristabilizzata, sia funzionale.** Potrebbe essere stabile-ma-inerte. Johannsen non lo verifica (non aveva proteina da testare).
  2. ⚠️ Il dato è su **fibroblasti**, non neuroni. La stabilità proteica è tessuto-specifica.
  3. ⚠️ "Assenza" al Western blot è un limite di sensibilità, non uno zero assoluto. Quanta proteina residua c'è davvero?
  4. Il readout non può essere solo la catalisi: il SDR media anche il **binding** a tau/GSK3β/TPC6AΔ ([[discovery_ledger_current#DL-MECH-019 — Q230 cade nel dominio SDR che media il binding a tau/GSK3β/TPC6AΔ: catalisi intatta ≠ funzione conservata|DL-MECH-019]]), e una destabilizzazione può abolire il binding lasciando intatto il sito attivo.
- **Sicurezza (BLOCCO 1):** 🟡 **giallo, e dipende interamente dalla molecola.** Gli inibitori del proteasoma (bortezomib) sono **inaccettabili** come terapia cronica pediatrica. I chaperoni chimici approvati — **4-fenilbutirrato (4-PBA)** e **acido tauroursodesossicolico (TUDCA)** — hanno profili molto migliori (4-PBA è approvato nei disturbi del ciclo dell'urea, anche in età pediatrica; TUDCA è in studio nella SLA). **Nessuna molecola sale a L9 senza `legend-safety-triage` (ADMET + BBB + alert strutturali).** Nota di cautela biologica: WWOX è **pro-apoptotico** in alcuni contesti — l'obiettivo è ripristinare livelli fisiologici, **non sovraesprimere**.
- **Traslabilità al modello di malattia:** alta come programma sperimentale su cellule già clinicamente disponibili; non è una proposta terapeutica e il readout non è binario.
- **Tempo-sensibilità:** alta — ma è l'unica leva del portafoglio che **non dipende da una finestra di sviluppo che si sta chiudendo**: una proteina degradata oggi può essere stabilizzata domani.
- **🧪 Esperimento minimo che decide (in ordine, ciascuno informativo da solo):**
  1. **Western blot WWOX su fibroblasti donor-derived** vs controlli sani → quanta proteina c'è? (attesa: molto ridotta). *Questo da solo vale l'intera ipotesi.*
  2. **qRT-PCR WWOX** sugli stessi → il trascritto è normale? (replica di Johannsen sul genotipo del genotipo di riferimento, che è compound-het, non omozigote).
  3. **Sintesi nascent + pulse-chase**, con frazionamento solubile/insolubile, per separare produzione e scomparsa.
  4. **Sonde ortogonali di turnover**: bracci proteasomiale e lisosomiale con vitalità; HSC70/LAMP1 sono readout associativi, non prova di CMA. Evitare di assumere efficacia di 4-PBA/TUDCA.
  5. Se aumenta la proteina: funzione, localizzazione e partner binding obbligatori.
- **Ranking:** azionabilità 3/3 · evidenza 2/3 · sicurezza 2/3 · time-to-benefit 2/3 · valore-parziale 3/3 → **12/15**
- **Status:** `stress-tested` — ritirato `proposed-to-L9` finché il ramo causale non è discriminato
- **Note L9:** non promuovere una molecola. Alimenta [[therapeutic_strategies_current#TX-003 — Pharmacological chaperone / proteostasis modulators (Q230P example)|TX-003]] solo come programma di discriminazione causale e rescue funzionale condizionato.
- **📮 Azione ad alta resa, a costo quasi zero:** **Markus A. Schirmer** (Göttingen) è coautore **sia** di Johannsen 2018 (il dato funzionale su Q230P) **sia** del paper JNCI da cui viene l'assay di inclusione dell'esone 9 ([[discovery_ledger_current#DL-BIO-003 — Assay qPCR region-specifico esone 8–9 vs core (esoni 4–6): misura diretta dell'effetto dell'allele di sito accettore|DL-BIO-003]]). Lo stesso gruppo possiede **entrambi i pezzi sperimentali necessari a caratterizzare i due alleli del genotipo di riferimento**. Un contatto è probabilmente il singolo passo a più alto rapporto valore/costo dell'intero programma.

---

## Aggiornamento 2026-07-10 a HYP-20260709-08 (rescue proteostatico) — **la domanda cambia forma**

> Non aggiungo un'ipotesi: raffino quella che c'è, perché la serie allelica appena chiusa ne cambia il bersaglio.

**Cosa è successo.** Avevo formulato HYP-08 come: *"se Q230P è sintetizzata ma degradata, impedirne la degradazione farà riemergere proteina."* Il pezzo mancante era **Mallaret 2014** (P47T), letto oggi. Insieme a Steinberg 2021 e Abdel-Salam 2014, chiude la serie ([[discovery_ledger_current#⭐ DL-MECH-037 — Q230P è **l'unica delle tre varianti a essere una lesione di ripiegamento del core**. Il ΔΔG non lo diceva; la sepoltura sì.|DL-MECH-037]]):

- **P47T** (WW1): proteina **a livelli normali**, **binding PPxY abolito** → **fenotipo lieve** (pazienti vivi a 17-26 anni). Gli autori: *"the dehydrogenase/reductase domain of the mutant protein is presumably still functional."*
- **G372R** (SDR): proteina **quasi non rilevabile**, organoidi **quasi normali** → **fenotipo lieve**.
- **Q230P** (SDR): proteina **assente** → **fenotipo severo**.
- **p.Arg54\*** (null): proteina zero → **letale a 16 mesi**.

**Le due conseguenze, una buona e una scomoda.**

🟢 **Buona:** il fatto che P47T abbia proteina normale e una funzione (WW1-binding) completamente abolita, e sia comunque **lieve**, dice che **la funzione WW1/PPxY non è quella che determina la gravità. Il SDR sì.** Q230P è nel SDR. Questo mette il nostro bersaglio nel punto giusto. E il topo ipomorfo (proteina bassa ma presente) è **vitale**, mentre il null muore: **una quota residua di proteina funzionante cambia il destino.**

🔴 **Scomoda, ed è la più importante:** **Q230P e G372R sono entrambe missense nel SDR, entrambe danno poca proteina rilevabile — ma una è severa e l'altra lieve.** Quindi *la quantità di proteina non spiega la severità*. Steinberg lo dice apertamente: conta il **livello funzionale**, non quello totale. → **Il collo di bottiglia potrebbe non essere solo la degradazione.** Se Q230P, stabilizzata, fosse comunque inerte (o peggio, aggregante e proteotossica), il rescue proteostatico non darebbe funzione.

**Quindi la domanda di HYP-08 non è più "quanta proteina Q230P riusciamo a salvare", ma: "la proteina Q230P salvata è funzionale?"** Era l'assunzione che avevo già marcato come non testata. Ora so che **è l'unico snodo che conta**, e che esiste un **controllo naturale** per interrogarlo: G372R.

**⚠️ Nota metodologica onesta ([[discovery_ledger_current#^fm-014|FM-014]]):** la serie mette insieme Western blot su fibroblasti (P47T, Q230P) e immunofluorescenza su organoidi (G372R). **Non sono la stessa misura.** L'inferenza regge come indicazione, non come quantificazione.

### Piano rivisto, in ordine di costo crescente

1. **✅ ESEGUITO (2026-07-10) — e ha dato una risposta migliore della domanda.** Vedi [[discovery_ledger_current#⭐ DL-MECH-037 — Q230P è **l'unica delle tre varianti a essere una lesione di ripiegamento del core**. Il ΔΔG non lo diceva; la sepoltura sì.|DL-MECH-037]] e `staging/insilico_20260710/RESULT.md`.
   - **Lo scenario favorevole regge, ma la metrica era sbagliata.** Il **ΔΔG non discrimina**: P47T ha il ΔΔG più alto (+2.81) e **proteina a livelli normali** con fenotipo lieve; P47R (stesso residuo, ΔΔG +2.53) è severo; Q230P (+1.51) e G372R (+1.58) hanno ΔΔG quasi identici e severità opposte.
   - **Discrimina il contesto strutturale.** **Q230 è l'unico residuo completamente sepolto** (relSASA **0.000**), su **α-elica**, 22 contatti entro 5 Å, pLDDT 98.5, a 8.2 Å dalla triade. **Gln→Pro in un'α-elica sepolta è il caso peggiore possibile.** G372 (relSASA 0.163) e P47 (0.286) sono **superficiali, su β-strand**: lesioni di superficie/funzione, non di folding. Coerente con il dato wet: P47T ha proteina normale ma **binding PPxY abolito**.
   - **⚠️ Correzione interna**: l'euristica "finestra recuperabile ΔΔG 0.8–3.5" classifica **tutte e tre** le varianti come recuperabili → **non ha valore predittivo** e va declassata in CLAIM 019 ([[discovery_ledger_current#^fm-016|FM-016]]).
   - **Conclusione**: **Q230P è, delle tre, l'unica lesione di ripiegamento del core** — l'unica per cui un chaperone ha un razionale meccanicistico diretto.
   - 🔴 **Il dubbio residuo, ora preciso**: una prolina sepolta in un'α-elica impone un vincolo di backbone che **un chaperone non può rimuovere**. Un chaperone aiuta a raggiungere uno stato foldato; non cambia la chimica del backbone. **Esiste per Q230P uno stato foldato *e* attivo raggiungibile?** A favore: Q230 dista 8.2 Å dalla triade (prossimità, non contatto). Contro: core denso (22 contatti). **In silico non è dirimibile.**
   - 🧪 **Il risultato genera il controllo negativo che mancava** (vedi punto 3).
2. **🧫 Wet, su cellule donor-derived.** Western blot WWOX su fibroblasti (quanta proteina c'è?) + qRT-PCR (il trascritto è normale, come in Johannsen?) + pulse-chase (emivita) + rescue in vitro con **4-PBA / TUDCA** (chaperoni chimici clinicamente rilevanti) e MG132 **solo come sonda meccanicistica**.
   **Il readout non può essere l'abbondanza** (DL-MECH-033 mostra che inganna): deve essere **funzionale** — attività ossidoreduttasica, binding a tau/GSK3β/TPC6AΔ ([[discovery_ledger_current#DL-MECH-019 — Q230 cade nel dominio SDR che media il binding a tau/GSK3β/TPC6AΔ: catalisi intatta ≠ funzione conservata|DL-MECH-019]]), soppressione di HIF1α ([[discovery_ledger_current#DL-MECH-028 — WWOX lega HIF1α via **WW1**, non via SDR: l'asse metabolico potrebbe essere parzialmente preservato in Q230P|DL-MECH-028]]), **e localizzazione subcellulare** ([[discovery_ledger_current#DL-MECH-036 — Vie di degradazione di WWOX già note e druggabili (ma probabilmente non quelle giuste)|DL-MECH-036]]: il SDR governa anche quella).
3. **🧠 L'esperimento che decide — e ora ha un controllo negativo.** Il lab **Aqeilan** possiede iPSC da paziente **SCAR12 con missense SDR (G372R)**, iPSC da paziente **WOREE**, linee KO, rescue W-AAV/lentivirale, organoidi, elettrofisiologia, RNA-seq ([[discovery_ledger_current#DL-MOL-010 — Il banco per testare HYP-08 esiste già. Manca un solo reagente, e il genotipo di riferimento lo possiede.|DL-MOL-010]]). **Manca solo una linea Q230P — e il genotipo di riferimento la può fornire.**
   **Il disegno, reso interpretabile dal risultato in-silico:** trattare in parallelo cellule **Q230P** e **G372R** con 4-PBA/TUDCA.
   - Predizione: **Q230P** (lesione di folding del core) → la proteina **riemerge**. **G372R** (lesione di superficie) → **non riemerge**, o poco.
   - **Se G372R rispondesse identicamente a Q230P, il modello strutturale è falso** e il rescue sarebbe un artefatto aspecifico dei chaperoni. Senza questo controllo, un risultato positivo su Q230P **non sarebbe interpretabile**.
   Endpoint **funzionali** obbligatori (non abbondanza): attività SDR, binding a tau/GSK3β, soppressione di HIF1α, localizzazione subcellulare.

### Sicurezza (BLOCCO 1) — aggiornata, e più severa
🟡→⚠️ Oltre a quanto già scritto: Steinberg mostra che **la perdita di WWOX causa proliferazione di progenitori con danno al DNA e perdita del checkpoint apoptotico**, e che il suo rescue **supra-fisiologico** ha dato un recupero **solo parziale**, con esplicito richiamo al *"fine-tuning of expression levels"*. WWOX è un oncosoppressore pro-apoptotico in alcuni contesti. → **L'obiettivo è il livello fisiologico, non il massimo.** Vale per il chaperone quanto per la terapia genica ([[discovery_ledger_current#^fm-013|FM-013]]).
Nota rassicurante e reale: i nulli **umani** (Abdel-Salam) e il ratto *lde* **non sviluppano tumori** → sul fronte oncologico, **stabilizzare/ripristinare WWOX è protettivo, non rischioso**. Il rischio è di sovraesprimere, non di ripristinare.

### Status
**Stato storico superseduto:** `proposed-to-L9`, 13/15. Lo stato attivo è definito nel repair 2026-07-14 sotto: `stress-tested`, 12/15.

---

## Aggiornamento storico 2026-07-12 a HYP-20260709-08 — **SUPERSEDED dal repair 2026-07-14**

> Non è un raffinamento. È una **correzione del disegno sperimentale** prima che venga eseguito. Fonte: *CC-2026-07-12-005 (private commit queue)* · Zhang 2025, Adv Sci, PMID 41124647 · [[discovery_ledger_current#DL-MECH-047 — P252A mostra degradazione lisosomiale HSC70-associata; **CMA e trasferimento a Q230P non dimostrati**|DL-MECH-047]]

**Premessa storica ora ritirata.** HYP-08 aveva interpretato Johannsen come prova di degradazione Q230P. Il paper lascia invece aperta traduzione compromessa oppure degradazione prematura; il testo seguente documenta la traiettoria dell'ipotesi, non lo stato attivo.

**Cosa sappiamo ora.** Nell'analogo più vicino disponibile — **WWOX-P252A**, missense **nello stesso dominio SDR**, con la **stessa firma** (mRNA normale, proteina bassa):
- **MG-132 non produce alcun accumulo.** Il proteasoma **non è la via**.
- **Clorochina e NH₄Cl ripristinano la proteina.** La via è **lisosomiale**.
- **3-MA non fa nulla** → non è macroautofagia.
- Il mutante **lega HSC70** (il WT no) e **co-localizza con LAMP1**.
- WWOX porta un **motivo KFERQ-like (LRSVQ, aa 187-191)**; la missenso **aumenta la flessibilità conformazionale** e — modello degli autori — **espone il motivo** all'HSC70.
→ **Autofagia mediata da chaperone (CMA), nel lisosoma.**

### 🔴 Le tre conseguenze

**1. L'esperimento decisivo, come scritto, rischia un FALSO NEGATIVO.**
Il punto 4 del piano prevede MG-132 come sonda. Nell'analogo, MG-132 è muto. Un risultato negativo verrebbe letto come *"la degradazione non è il collo di bottiglia"* — **e sarebbe sbagliato**, uccidendo l'ipotesi meglio scorata del portafoglio (13/15).
**Correzione (costo: pochi pozzetti):** aggiungere il **braccio lisosomiale (clorochina / NH₄Cl)** — quello che con ogni probabilità funziona — più **3-MA** come controllo, **co-IP HSC70** e **co-localizzazione LAMP1**. MG-132 resta, ma come **controllo negativo atteso**.

**2. I due chaperoni a ledger sono della classe sbagliata.**
**4-PBA e TUDCA** agiscono sullo stress del **reticolo endoplasmatico**. WWOX è **citosolica/mitocondriale**, e la via è **CMA/lisosoma**. Il compartimento non torna. *(Gli autori stessi contrastano con NPC1-I1061T, che misfolda nell'ER ed è degradato da proteasoma + ER-autofagia: **WWOX non segue quella via**.)*

**3. ⚠️ I co-induttori di HSP70 potrebbero peggiorare le cose — e includo un candidato che io stesso avevo proposto.**
**Arimoclomol** ha un profilo pediatrico che sembrava ideale (NPC, 2-18 anni, FDA-approvato, OLE 48 mesi). Ma **HSC70 è il chaperone che consegna il mutante al lisosoma**. Amplificare l'asse HSP70 rischia di **accelerare** la degradazione di Q230P. **Ritiro il candidato**: la direzione dell'effetto non è nota e potrebbe essere invertita. Vale come monito generale: *"è un chaperone" non dice il segno dell'effetto — dipende da quale chaperone e da quale via.*

### 🟢 Cosa la CMA apre, invece

Il mutante non è degradato perché **rotto**: è degradato perché **floscio**. La flessibilità espone il KFERQ. Quindi il bersaglio corretto è un **stabilizzatore conformazionale del fold SDR**, che dovrebbe (a) ridurre l'esposizione del motivo → meno CMA → più proteina, e (b) forse restituire funzione.
**Novità operativa: ora esiste un readout meccanicistico diretto per misurarlo** — perdita del co-IP con HSC70 e della co-localizzazione con LAMP1. Prima il readout era solo "quanta proteina vedo", che [[discovery_ledger_current#⭐ DL-MECH-033 — La serie allelica di WWOX: **la quantità di proteina non predice la severità. Conta la funzione residua.**|DL-MECH-033]] ci aveva già insegnato a diffidare.

🔴 **BLOCCO 1 — la CMA generica NON è un bersaglio terapeutico.** Clorochina cronica in una bambina = retinopatia; e la CMA è **neuroprotettiva** nei neuroni: inibirla globalmente è pericoloso. **Clorochina/NH₄Cl sono sonde da banco, mai terapia.**

### ⚠️ La notizia scomoda: "stabile ma inerte" non è più un timore, è un fenotipo dimostrato

Lo stesso paziente porta **P282A**: stesso dominio SDR, **proteina stabile, nessun legame con HSC70** — e **completamente priva di funzione** (non inibisce crescita né invasione, in vitro e in vivo; perde il binding a POLE4).
→ **Per le missenso SDR di WWOX, stabilità e funzione sono separabili.** Il dubbio già marcato in HYP-08 (*"potrebbe essere stabile-ma-inerte"*) ha ora un **caso reale**. **Il readout funzionale non è opzionale: è la misura che conta.**

### Limiti onesti

- Il paziente omozigote P252A+P282A **non aveva malattia neurologica**: sono **ipomorfi**, non equivalenti a Q230P (WOREE severa). **Il meccanismo si trasferisce; la severità no.**
- Tutto in linee di cancro tiroideo e HEK293T **in sovraespressione**, non in neuroni né cellule di paziente. La CMA è tessuto-specifica.
- **Q230P non è mai stato testato.** La via CMA per Q230P è **IPOTESI PONTE debole/non discriminata**, non DATO né inferenza forte.

### Status
HYP-20260709-08 resta **`proposed-to-L9`** e **⭐ la meglio scorata del portafoglio**. Il ranking non cambia: cambia — e migliora — **l'esperimento che la decide**, che ora ha una via candidata precisa e un readout meccanicistico.

---

## Repair 2026-07-14 — supersede degli aggiornamenti 2026-07-10/12 su HYP-08

Gli aggiornamenti storici sopra sono preservati, ma le loro conclusioni causali sono **supersedute** da `CC-2026-07-14-001`:

- Johannsen **non** dimostra che Q230P sia sintetizzata normalmente né che venga degradata;
- Zhang dimostra per **P252A** degradazione lisosomiale HSC70-associata, ma HSC70 + clorochina + LAMP1 non distinguono da soli CMA da altre forme di microautofagia/endosomal microautophagy; manca LAMP2A-dipendenza;
- `LRSVQ` è phosphorylation-generated solo se S189 è fosforilata; `ERLIQ 402-406` è il candidato canonico. Nessuno dei due degron è stato testato per epistasi in Q230P;
- P252A/P282A non sono controlli validati della rottura dell'elica e C299R non è un controllo off-lid/catalitico pulito;
- lo stabilizzatore SDR resta `conditional / not design-ready`; abbondanza senza funzione non è un successo.

**Stato attivo:** HYP-08 = `stress-tested`, 12/15. Sequenza: sintesi nascent → solubilità → turnover → route mapping → rescue funzionale. Nessuna azione clinica.
