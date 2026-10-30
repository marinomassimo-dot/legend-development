# LEGEND Drug Repurposing — Logiche di candidatura e matching
## Versione 3 definitiva · 30 ottobre 2026

### 1. Il principio di candidatura

Un composto merita di entrare nella ricerca quando esiste almeno una ragione verificabile per attendersi un beneficio definito nel contesto WWOX: un effetto funzionale osservato oppure un’ipotesi biologica concreta da mettere alla prova.

La candidatura è un’ipotesi di lavoro. Non è una raccomandazione terapeutica e non implica efficacia, sicurezza o utilizzabilità clinica.

La priorità cresce con la qualità delle prove, la pertinenza del modello e le conferme realmente aggiuntive. Diminuisce con contraddizioni pertinenti e ostacoli rispetto all’obiettivo previsto. Non serve obbligatoriamente la concordanza fra più algoritmi: un recupero funzionale ben controllato può essere più informativo di molti predittori basati sulle stesse fonti.

Il criterio centrale è:

**Quale funzione vorremmo migliorare, in quale contesto, e quale osservazione permetterebbe di riconoscere o smentire il miglioramento?**

### 2. Tre obiettivi da mantenere aperti

| Obiettivo | Domanda operativa | Distinzione necessaria |
| --- | --- | --- |
| Recuperare una funzione di WWOX | Possiamo migliorare la quantità, maturazione, localizzazione o funzione di un prodotto residuo? | La possibilità dipende dall’allele e dal prodotto realmente presente; più proteina non significa più funzione. |
| Compensare la perdita | Un altro componente può sostenere una funzione compromessa anche senza recuperare WWOX? | La compensazione richiede un risultato funzionale pertinente. |
| Ottenere un beneficio parziale | Possiamo migliorare una conseguenza importante, anche senza correggere il difetto iniziale? | Un beneficio circoscritto non dimostra recupero globale. |

Gli obiettivi possono sovrapporsi. Un composto può contribuire a più di uno, ma deve dichiarare quale beneficio è sostenuto dai dati e quale resta ipotetico.

Non restringere preventivamente il repurposing al ruolo di ponte o adiuvante di una terapia genica. Questi sono impieghi possibili; restano aperti anche percorsi autonomi di compensazione e beneficio parziale. Le eventuali combinazioni richiedono una valutazione dedicata.

### 3. Separare dati, interpretazioni e metodi

| Categoria | Esempi | Cosa consente |
| --- | --- | --- |
| Dati | RNA, proteine, metaboliti, immagini, attività elettrica, risposte a perturbazioni | Descrivere ciò che è stato misurato in un sistema. |
| Organizzazione e interpretazione | Pathway, moduli di rete, ontologie fenotipiche come HPO | Collegare e interpretare osservazioni. |
| Metodi | Inferenza causale, predizione su grafo, inversione delle firme, simulazione metabolica | Produrre confronti e previsioni da dati e assunzioni. |

RNA, pathway e simulazione non sono tre prove indipendenti. Una stessa misura può essere interpretata attraverso un pathway e poi utilizzata da una simulazione.

Senza RNA del paziente si può lavorare con dati pubblici, modelli WWOX-deficienti, perturbazioni pertinenti e letteratura. Le previsioni riguardano però il sistema rappresentato, non ricostruiscono automaticamente il singolo paziente.

Mantieni distinguibili knockout completo, varianti missenso, difetti di splicing, modelli murini e cellule umane. WOREE e SCAR12 sono contesti da qualificare separatamente, non etichette intercambiabili.

### 4. Quindici logiche per generare candidati

Le logiche sono percorsi disponibili, non quindici requisiti. Selezionale in funzione della domanda e dei dati utilizzabili.

| # | Logica | Come genera il matching | Domanda e limite decisivo per WWOX |
| --- | --- | --- | --- |
| 1 | Nodo causale a monte | Cerca un regolatore modificabile che influenzi più conseguenze della perdita di funzione. | Le relazioni causali, la direzione e il contesto sono documentati oppure assunti? Un nodo molto connesso non è automaticamente un buon bersaglio. |
| 2 | Pathway e nodi con direzione qualificata | Collega alterazioni biologiche a farmaci capaci di modificarne componenti specifici. | L’intervento correggerebbe un danno o spegnerebbe una compensazione? |
| 3 | Inversione di firme molecolari | Cerca perturbazioni farmacologiche opposte a una firma della malattia o di un modello. | La firma è pertinente e riproducibile? Invertire RNA non equivale a recuperare una funzione. |
| 4 | Grafo di conoscenza e predizione zero-shot | Predice associazioni farmaco–malattia anche con pochi esempi terapeutici per quella malattia. | Quale informazione WWOX viene realmente utilizzata? Un percorso esplicativo non dimostra causalità. |
| 5 | Prossimità nell’interattoma | Cerca bersagli farmacologici vicini alle proteine coinvolte nel modulo di malattia. | La vicinanza è pertinente al tipo cellulare e specifica una direzione favorevole? |
| 6 | Matching fenotipico e HPO | Confronta fenotipi, indicazioni, controindicazioni ed effetti avversi descritti con termini condivisi. | Migliorare un fenotipo e provocarlo sono relazioni diverse. Somiglianze generiche come “epilessia” non bastano. |
| 7 | Soppressore genetico e synthetic rescue | Cerca una seconda perturbazione genetica che attenui un difetto WWOX, poi interventi farmacologici che possano riprodurla. | La seconda perturbazione recupera una funzione pertinente? Associazioni di fitness in cellule tumorali generano ipotesi, non dimostrano recupero neurologico. |
| 8 | Recupero fenotipico diretto | Seleziona composti che migliorano un difetto funzionale osservato, anche prima di conoscere il meccanismo. | Il miglioramento persiste distinguendolo da sedazione, tossicità e selezione delle cellule sopravvissute? |
| 9 | Recupero della proteina residua | Esplora espressione, maturazione, ripiegamento, stabilità, localizzazione e funzione del prodotto presente. | Quale prodotto esiste e quale difetto è recuperabile? La categoria di variante, da sola, non risponde. |
| 10 | Bypass e compensazione | Cerca una via alternativa per sostenere una funzione compromessa lasciando invariato il difetto WWOX. | Quale funzione viene restituita e quali altre conseguenze restano aperte? |
| 11 | Flussi e vincoli metabolici | Individua colli di bottiglia e alternative in un modello metabolico con assunzioni esplicite. | Quali vincoli sono misurati e quali assunti? Non attribuire a WWOX reazioni enzimatiche non dimostrate. |
| 12 | Stato cellulare e morfologia | Confronta firme di immagini cellulari per cercare composti che attenuino un fenotipo riproducibile. | La somiglianza o normalizzazione visiva corrisponde a un beneficio funzionale? |
| 13 | Analogia meccanicistica fra malattie | Trasferisce un’ipotesi da una condizione che condivide un difetto biologico qualificato. | Sono condivisi meccanismo, direzione e contesto, oppure soltanto sintomi? |
| 14 | Evidenze umane osservazionali | Usa casi, serie cliniche, risposte inattese e dati di pratica clinica per generare o rafforzare ipotesi. | Prescrizione, associazione e beneficio causale restano distinti; registra anche mancata risposta e peggioramento. |
| 15 | Combinazioni complementari | Abbina interventi su problemi distinti o su passaggi diversi dello stesso problema. | Il secondo intervento aggiunge beneficio rispetto ai singoli? Complementarità, sinergia misurata e tollerabilità sono dimensioni diverse. |

Per la proteina residua, separa aumento della trascrizione, modulazione dello splicing, stabilizzazione del prodotto e recupero della funzione: richiedono presupposti e prove differenti. Non assumere per Q230P degradazione, insolubilità o recuperabilità già dimostrate. Un intervento che richiede proteina presente non si trasferisce a un sistema in cui quel prodotto è assente.

La progettazione di nuove molecole resta un ramo distinto: un bersaglio convincente senza un composto adeguato può motivare drug development. Affinità predetta, legame sperimentale e recupero funzionale non sono equivalenti.

### 5. Come usare i pathway senza premiare la copertura apparente

Per ciascuna alterazione separa due domande:

| Campo | Valori possibili |
| --- | --- |
| Direzione osservata | Aumento, diminuzione, effetto misto, dipendente dal contesto, sconosciuto. |
| Ruolo interpretato | Causa, conseguenza dannosa, compensazione protettiva, effetto della composizione cellulare, misto o sconosciuto. |

Il ruolo causale deve avere una fonte o essere dichiarato come ipotesi. Può cambiare con tipo cellulare, intensità e fase di sviluppo.

Un effetto della composizione cellulare può rappresentare perdita o maturazione alterata di una popolazione: non è necessariamente un artefatto irrilevante. Riportare un segnale verso il controllo non è di per sé prova di beneficio.

Quando il ruolo è sconosciuto, conserva il processo come domanda esplorativa; non presentarlo come bersaglio qualificato e non espellerlo automaticamente dalla ricerca.

Non classificare i composti contando i pathway “coperti”. Controlla geni e relazioni condivisi, direzione e conseguenze funzionali. Pathway sovrapposti non sono conferme indipendenti, ma neppure vanno compressi con una regola universale “dieci uguale uno”.

La promiscuità farmacologica non riceve un bonus né una penalità automatica. Valuta quali bersagli sono modificati alle esposizioni pertinenti e se gli effetti sono complementari, antagonisti o ancora sconosciuti.

### 6. La scheda progressiva del candidato

L’unità di lavoro è una relazione **composto–azione–contesto–beneficio**, non soltanto il nome della sostanza. Lo stesso composto può avere candidature diverse per obiettivi o condizioni differenti.

Riusa i registri e i campi già presenti in LEGEND. La scheda deve contenere:

1. **Composto e intervento.** Identità, forma rilevante, bersaglio e direzione, quando conosciuti. Se il meccanismo è ignoto, descrivi l’effetto osservato.
2. **Contesto e beneficio.** Modello, variante quando pertinente, tipo cellulare, fase di sviluppo, funzione attesa e misura del risultato.
3. **Fondamento della candidatura.** Recupero osservato o ipotesi predittiva; fonti, condizioni e relazioni che sostengono il collegamento.
4. **Limiti e contraddizioni.** Risultati contrari, spiegazioni alternative, dipendenze fra fonti e dati mancanti.
5. **Prossima prova e decisione.** Il confronto più semplice che può cambiare la valutazione, con criterio per mantenere, scartare o lasciare inconclusa quella specifica ipotesi.

I campi sconosciuti restano visibili. Non richiedere un meccanismo completo a un candidato emerso da un recupero fenotipico. Quando non è ancora formulabile una prova discriminante, la prossima attività è chiarire la domanda; il candidato non è pronto per una valutazione sperimentale risolutiva.

### 7. Come valutare prove e convergenza

Non contare algoritmi, siti o famiglie di dati come voti indipendenti. Valuta l’origine dell’informazione.

| Situazione | Interpretazione |
| --- | --- |
| Due predittori usano lo stesso grafo | Concordanza fra metodi con evidenza condivisa. |
| Due strumenti interrogano le stesse firme | Analisi o accessi diversi allo stesso materiale sperimentale. |
| RNA e immagini provengono dallo stesso esperimento | Misure complementari che possono condividere fattori confondenti. |
| Due esperimenti dello stesso tipo sono svolti indipendentemente | Possono aggiungere conferma, se controlli e contesti sono adeguati. |
| Una previsione è seguita da recupero funzionale controllato | Evidenza di natura diversa, da pesare secondo qualità e pertinenza. |
| Molti segnali favorevoli e un risultato contrario pertinente | La contraddizione richiede una spiegazione; la maggioranza non la annulla. |

La convergenza deve riguardare una proposizione compatibile: stesso beneficio, direzione coerente e contesto trasferibile. Due interventi complementari possono agire in direzioni molecolari diverse; esplicita come dovrebbero produrre il beneficio comune.

Il peso delle controevidenze dipende dalla qualità e dalla pertinenza. Non esiste una simmetria automatica fra un risultato favorevole e uno contrario.

Distingui sempre: dichiarato nella fonte; implementato nel codice; testato dagli autori; riprodotto indipendentemente; verificato da LEGEND; trasferibilità WOREE. Pagina consultata e repository esistente non significano implementazione o validazione biologica.

### 8. Due priorità separate

| Priorità | Domanda | Criteri principali |
| --- | --- | --- |
| Ricerca | Quale candidato chiarisce meglio una domanda importante con una prova interpretabile? | Qualità del razionale, informatività, controlli, modello disponibile, costo e tempo. |
| Sviluppo | Quale candidato ha una strada credibile verso un beneficio nell’impiego previsto? | Evidenze pertinenti, esposizione al bersaglio, sicurezza, formulazione, disponibilità, interazioni e accesso. |

Le valutazioni farmacologiche iniziano presto, ma ogni limite vale rispetto alla decisione in esame. Una sonda senza dati pediatrici può restare utile in laboratorio. Un problema di esposizione può bloccare uno specifico impiego senza annullare il valore del meccanismo.

Per effetti cerebrali conta l’esposizione nel tessuto bersaglio; per un meccanismo periferico, esplicita la catena verso il beneficio neurologico. Non rendere l’attraversamento della barriera ematoencefalica un requisito universale per qualsiasi candidatura.

Non confrontare direttamente concentrazione nominale in vitro e dose umana: occorre qualificare esposizione, durata, quota libera quando disponibile e contesto dell’esperimento.

Usa tre esiti, accompagnati dal motivo:

- **Favorevole:** il dato sostiene quel requisito entro un ambito definito.
- **Sfavorevole:** esiste un ostacolo documentato rispetto a quell’impiego.
- **Sconosciuto:** il dato manca o non è trasferibile; diventa una domanda e sospende soltanto le decisioni che ne dipendono.

Integratore, OTC e Rx non stabiliscono la candidatura biologica. Identità, qualità, formulazione e disponibilità entrano quando influenzano l’esperimento o lo sviluppo; la facilità di acquisto non dimostra idoneità pediatrica.

Evita formule moltiplicative e pesi numerici non calibrati. Sono ammissibili confronti motivati, parità e candidati non sufficientemente valutati. Un punteggio predittivo non diventa una probabilità clinica di successo.

### 9. Come scegliere risorse esterne

Seleziona uno strumento quando risponde a una lacuna concreta, confrontandolo con l’alternativa più semplice e con ciò che LEGEND possiede già.

| Risorse esemplificative | Domanda che possono servire |
| --- | --- |
| MATRIX, TxGNN | Quali associazioni vale la pena approfondire? |
| INDRA, DisMech, NetworkCommons/CARNIVAL | Quali relazioni e direzioni possono sostenere un’ipotesi meccanicistica? |
| LINCS, SigCom, L2S2, drugfindR | Quali perturbazioni producono firme simili o opposte? |
| JUMP/Cell Painting | Quali perturbazioni modificano uno stato cellulare osservabile? |
| DepMap e screening di soppressori | Quali interazioni genetiche suggeriscono esperimenti di compensazione? |
| COBRApy | Quali interventi sono compatibili con un modello metabolico esplicito? |
| HPO e SIDEKICK | Come collegare fenotipi, indicazioni ed effetti avversi mantenendo distinte le relazioni? |
| SynergyFinderR | Come analizzare risposte sperimentali a combinazioni? |

Questa è una mappa d’uso, non una lista di installazioni o strumenti validati per WOREE. Per un impiego concreto verifica input reali, copertura pertinente, licenze di codice/dati/pesi, manutenzione e output conservabili.

GitHub, Hugging Face e paper dello stesso progetto non sono tre conferme. Gli agenti LLM possono cercare, estrarre, confrontare e usare strumenti; la loro concordanza non crea evidenza biologica indipendente.

Preferisci componenti pronti, raccordi piccoli, ambienti isolati e sostituibilità. LEGEND conserva provenienza, contraddizioni, input/output e riproducibilità, senza dover possedere ogni implementazione.

### 10. Usare i test LEGEND per migliorare le decisioni

Le lezioni emerse dalla diagnosi fornita restano distinte:

- Una lacuna di collegamento non è assenza di letteratura.
- Un identificatore corretto non dimostra che la fonte sostenga la proposizione.
- Una firma invertita non dimostra recupero funzionale.
- Un test informatico superato non dimostra validità biologica.

Ogni esito va collegato a dati, versione, metodo, contesto ed endpoint realmente provati. Un risultato negativo di una configurazione non squalifica automaticamente un’intera famiglia di metodi. Una ripetizione è utile quando cambia un elemento capace di cambiare la risposta.

Per i risultati negativi conserva la distinzione fra assenza di segnale, copertura insufficiente, errore di interrogazione, collegamento mancante e modello non informativo.

### 11. Applicazione iniziale al modulo

Il primo passo è una prova su un piccolo insieme di candidati già lavorati, scelto per includere casi favorevoli, controversi e incompleti.

Usa le evidenze esistenti, compila la scheda progressiva e confronta le due priorità con il ranking attuale. Misura se:

1. cambiano selezione o ordine, e quale evidenza giustifica il cambiamento;
2. diventano più precise le domande e le prossime prove;
3. emergono duplicazioni, dipendenze o contraddizioni prima invisibili;
4. si evitano verifiche inutili senza perdere candidati informativi.

L’esito può essere mantenere lo schema, semplificarlo o dichiarare il confronto inconcluso. Stabilizza soltanto i campi che aiutano le decisioni; evita nuovi registri paralleli e procedure obbligatorie prima di averne dimostrato l’utilità.

La revisione critica accompagna il lavoro in misura proporzionata. Gli audit approfonditi si concentrano sui collegamenti da cui dipende una decisione; non sono un adempimento da rinviare interamente alla fine.

### 12. Regola operativa finale

**Per ogni candidato, rendi leggibile il passaggio fra ciò che osservi, ciò che prevedi, il beneficio che cerchi e la prova che può cambiare la decisione.**

Mantieni aperti recupero, compensazione e beneficio parziale. Lascia visibili le incertezze. Fai crescere i requisiti con la decisione: esplorare un’ipotesi, impegnare un esperimento e proporre uno sviluppo richiedono evidenze diverse.

Documento metodologico definitivo di sintesi del confronto. La sua redazione non attesta nuove installazioni, validazioni biologiche, modifiche al repository o aggiornamenti della roadmap canonica.

