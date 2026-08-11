# Deep-dive manual — how a paper becomes a claim

> **Public edition — de-identified, generic.** The full procedure for a LEGEND deep dive: coverage discipline, the epistemic tagging of every extracted statement, transfer assessment across genotype / model / endpoint, and the shape of the resulting COMMIT CANDIDATE. This is the document that makes the pipeline reproducible by someone else. Written against a *reference genotype* (a disease-level genotype class), never a person. Preserved in its original language. **Not medical advice.**

---

# DEEP_DIVE.md
# Protocollo di analisi profonda — Sistema LEGEND

---

## PROTOCOLLO — DEEP_DIVE

### STATUS

Questo protocollo è:

- OBBLIGATORIO
- NON INTERPRETABILE
- NON RIDUCIBILE
- NON BYPASSABILE

Ogni analisi di paper / studio / pubblicazione deve aderire integralmente a questo protocollo.

Se non aderisce:
→ ANALISI NON VALIDA

---

## 1. SCOPO

Eseguire analisi scientifica completa, rigorosa, profonda e non superficiale di paper WWOX-related o biologicamente connessi, con priorità assoluta al full text, generazione di inferenze disciplinate e identificazione di nuove linee di ricerca.

> Legend non archivia paper. Legend estrae conoscenza.
> Legend non riassume. Legend inferisce.
> Legend non segue gli autori. Legend legge oltre gli autori.
> Legend non legge un paper da solo. Legend lo legge dentro il sistema.
> Legend non si ferma al pathway. Legend cerca spazio terapeutico, biomarcatori e repurposing hypotheses.

---

## 2. DIVIETO ASSOLUTO

È espressamente vietato:

- riassumere solo abstract
- classificare paper per titolo
- fare mapping superficiale a pathway
- aggiornare registry senza comprensione profonda
- produrre output ordinato ma vuoto
- simulare comprensione senza deep reading

Questo tipo di output è definito:

> AMMINISTRAZIONE MASCHERATA DA ANALISI

→ NON ACCETTABILE

---

## 3. OBIETTIVO REALE

Per ogni paper, l'obiettivo è:

> estrarre il massimo contenuto informativo esplicito + implicito + latente

Inclusi:
- segnali deboli
- implicazioni non dichiarate dagli autori
- tensioni biologiche
- possibilità di inferenze multi-livello
- aperture di ricerca
- connessioni cross-domain

Ogni paper va trattato come:
- possibile generatore di conoscenza
- possibile ponte tra domini
- possibile generatore di ipotesi
- possibile trigger di nuove research lines

NON come semplice oggetto da archiviare.

---

## 4. FULL TEXT RULE (MANDATORY)

### 4.1 Obbligo

Devi sempre:
- cercare il full text
- usare il full text se disponibile

### 4.2 Se full text non disponibile

Devi dichiarare esplicitamente:

> FULL TEXT NOT AVAILABLE — LIMITED ANALYSIS MODE

E in questo caso devi:
- ridurre la forza delle inferenze
- evitare conclusioni strutturali
- evitare output presentati come analisi completa

### 4.3 Violazione

Analisi basata solo su abstract senza dichiarazione esplicita:
→ INVALIDA

### 4.4 Evidence depth (obbligatorio)

Per ogni paper importante devi sempre indicare:

- **Evidence depth:** full text reviewed / partial full text / abstract-only
- **Full text status:** found / not found / user upload needed

### 4.5 Locator verbatim (obbligatorio dal 2026-08-04)

**Mentre il documento è aperto**, per ogni affermazione che porterai fuori dalla lettura,
registra la frase esatta che la sostiene:

| Campo | Cosa contiene |
|---|---|
| `proposition` | che cosa la citazione sostiene — se non lo sai dire, la citazione è decorativa |
| `snippet` | la frase **verbatim** dalla fonte, minimo 30 caratteri |
| `anchor` | dove si trova: sezione, figura o tabella |

Vanno nel work manifest, sezione `verbatim_locators`, e sono validati da
[`deepdive_manifest.py`](../scripts/deepdive_manifest.py).

> 🔴 **Perché è obbligatorio.** Un receipt attesta che il documento è stato **letto per
> intero**. Non attesta *quale frase sostiene quale affermazione* — sono due fatti diversi.
> Il 2026-08-04 un export verso una knowledge base esterna ha trovato che **nessun locator
> verbatim esisteva in tutto lo stato canonico**, per nessuna delle letture complete a
> ledger: quattordici sono stati recuperati a posteriori da due paper già letti, riaprendo i
> file e emettendo receipt mirati. Catturare la frase mentre il documento è aperto costa
> secondi; recuperarla dopo costa la lettura una seconda volta.

Se la lettura non sostiene alcuna affermazione — letta per trasferimento di metodo, o
atterrata solo nel discovery ledger — si usa il waiver, che richiede un argomento di almeno
40 caratteri. Il waiver è legittimo; il silenzio no, e compare come `[DECLARED GAP]` in
`session_self_eval.py`.

> **Chi consuma i locator, e perché la ragione non è solo storica.** La motivazione qui sopra
> guarda indietro. Quella che conta guarda avanti: **l'export verso DisMech non può emettere una
> proposizione senza la frase che la sostiene.** Ogni nodo esportato porta il testo citato
> verbatim, l'ancora di sezione e il receipt della lettura che l'ha prodotto — una conclusione
> raggiunta con cura ma senza la sua citazione **non ha modo di entrare**, e non perché la regola
> lo vieti: non c'è nulla da attaccarle come evidenza.
>
> La conseguenza operativa è aritmetica. Una lettura fatta oggi senza locator è una lettura che
> va **rifatta** prima di poter essere esportata. Su un corpus che cresce di centinaia di full
> text, catturare al momento è l'unica strategia che non produce un debito proporzionale al
> lavoro svolto. Vedi [`analysis/README.md`](../../disease-models/wwox/analysis/README.md#the-dismech-export-pipeline).

---

## 4bis. PREFLIGHT DI SUPERFICIE — il primo gesto, prima di aprire qualunque cosa

> La regola 5d dice **preferisci XML/HTML PMC al PDF, e registra l'assenza**. Questa sezione
> esiste perché quella regola descrive una preferenza e non un gesto: nessuno sapeva *quando*
> guardare, quindi si guardava dopo aver già aperto il PDF — cioè mai.

**Prima di leggere una riga**, cerca la superficie strutturata, e **registra l'esito in
entrambi i casi**. «Non esiste» è un risultato che va scritto, non un silenzio: `PMID 17803050`
non ha DOI, non ha PMCID e non ha deposito aperto, e il fatto che ciò sia *dichiarato* è ciò
che rende quel paper una classe diversa invece di una lettura scadente.

### 🔴 Nessuna singola via è autorevole. Interrogale tutte e tre e registra il disaccordo.

Questo non è zelo. È misurato, il 2026-08-10, da due attori in due direzioni opposte:

- su `PMID 24308844` l'`oa.fcgi` risponde **non-OA**, Europe PMC risponde **404**, e `efetch`
  restituisce **174 KB di JATS completo**. Due vie sancite su tre l'avrebbero mandato al PDF;
- cinque voci del corpus portano `inPMC: Y` insieme a `isOpenAccess: N` — manoscritti d'autore
  depositati. **La superficie strutturata esiste e il paper non è open access**, che sono due
  fatti diversi e vengono confusi da qualunque controllo che ne legga uno solo.

Le tre vie:

```
oa.fcgi        https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=<PMCID>
Europe PMC     https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML
efetch         https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=<PMCID>
```

**Un annuncio non è una consegna e un rifiuto non è un'assenza.** Registra quale via ha
risposto e quali hanno negato: il disaccordo fra loro è il dato, e senza registrarlo il
prossimo lettore ripete la stessa cascata e arriva alla stessa conclusione sbagliata.

### Perché è il primo gesto e non il secondo

Un manifest costruito contro la superficie sbagliata **non sembra sbagliato**. Il 2026-08-10
l'estrattore fabbricava uno spazio a ogni confine di markup: su `PMID 24550385` questo
produceva `2` occorrenze di `PPXY` invece di `31` e **zero** citazioni di figura invece di
`32`. Un lettore su quella superficie non fallisce — **sceglie le citazioni che il difetto
lascia passare**, cioè adatta le prove allo strumento. È la regola 5c al contrario, ed è
invisibile a chi la sta facendo.

---

## 4ter. BUDGET DI FIGURE DICHIARATO — la manopola che nessuno aveva impostato

`coverage.figures: read` senza un solo locator su una figura **non regge**. È la casella più
facile da spuntare e la più difficile da contestare a posteriori, perché nulla nel record dice
quante figure c'erano.

**Ogni figura principale riceve un locator oppure una rinuncia nominata.** Non un numero fisso
— sarebbe la costante piantata a mano che `CLAUDE.md` vieta, e la vieta perché una soglia
ricordata da una persona è una soglia che si aggiorna per far tornare il verde.

**Il denominatore è dei pannelli, non del lettore.** *Pannelli coperti su pannelli presenti*,
con `figures_present` derivato dalle didascalie — un rapporto `figure per paper` misura quanto
è stato letto **diviso quanto quel lettore ha deciso di guardare**, che è una misura di sé
stessi. Il criterio eseguibile vive nel comando che lo calcola e viene **ri-misurato a ogni
corsa**: quello che sta scritto qui è la regola, mai la soglia.

### Registra anche la risoluzione, non solo la superficie

Il CDN serve 760 px dove gli autori ne hanno depositati 1397. Su un pannello di statistiche è
la differenza fra **leggere un asterisco e indovinarlo** — e un asterisco indovinato è
esattamente la classe di errore che il 2026-08-06 stava fra «non significativo» e «non
testato». La risoluzione a cui hai letto va nell'`anchor` del locator, con le dimensioni
native.

---

## 5. LETTURA PROFONDA OBBLIGATORIA

Non è consentito limitarsi a: abstract, conclusion.

Devi analizzare, quando disponibili:
- risultati
- figure
- tabelle
- metodi rilevanti
- struttura dei dati
- distribuzione degli effetti
- dettagli non enfatizzati dagli autori
- segnali secondari ma biologicamente significativi

---

## 6. MODALITÀ OPERATIVA

- Attiva Deep Search / Deep Research
- Non fermarti a titolo o abstract
- Per ogni paper rilevante: tentare recupero full text
- Usare i file current e il framework Legend come contesto vivo
- Mantenere sempre distinzione netta tra: DATO / INFERENZA / IPOTESI
- Non trasformare inferenze in fatti
- Non proporre output clinici senza filtro completo

---



### 6.0 RESEARCH GROUP ANALYSIS (STEP 0 — da eseguire PER PRIMO)

La prima cosa da guardare in uno studio sono gli **autori e il gruppo**, non solo il tipo di paper. Prima del full-state scan:

1. Leggi `researchers.md` (knowledge base persistente dei gruppi WWOX).
2. **Disambigua gli autori**: stesso cognome + iniziale diversa = persone potenzialmente DISTINTE (soprattutto nomi asiatici: Wang, Kim, Chen, Liu, Hsu, Lo, Chang). Stessa persona può avere iniziale singola/doppia o varianti. **Si disambigua per AFFILIAZIONE** (+ ORCID / email corrispondente / overlap co-autori). Identità non risolta → `AMBIGUOUS — verify`.
3. **Profila il gruppo lead** (senior/corresponding): ricerca sperimentale vera (lab/modelli/terapia/trial) vs solo osservazionale vs *produzione accademica* (sintesi senza nuovo messaggio); lab, finanziamenti, conflitti d'interesse, track record; focus — WWOX pediatrico WOREE/SCAR12 = **PLUS**; adulti/animali = ok ma più lontano; cancer-only = più lontano.
4. Aggiorna `researchers.md` (tagga `[verified]`/`[to-verify]`, change log) e fai **self-lint** sui nomi.
5. Emetti **ALERT** se il gruppo è ad alta credibilità/rilevanza.

Delegabile al subagent `research-group-analyst`. La credibilità del gruppo NON decide la verità del claim (quella è la deep dive), ma alza/abbassa priorità e profondità d'analisi.

### 6.1 Full-state context scan (MANDATORY)

Prima di analizzare qualsiasi paper, devi sempre eseguire un controllo contestuale completo.

## Regola generale
Devi usare **il massimo contesto disponibile coerente con il tipo di sessione**, ma senza violare la gerarchia del sistema.

### Gerarchia obbligatoria delle fonti
1. **File markdown current** = base viva e fonte di verità operativa
2. **Meta file e research files** = ampliamento inferenziale e contestuale
3. **Memoria della chat / continuità conversazionale** = supporto interpretativo, priorità, vincoli, ipotesi già emerse
4. **Manuali / note operative del framework** = disciplina procedurale

### Minimo obbligatorio
I seguenti file sono sempre obbligatori quando disponibili:
- `working_model_current.md`
- `claim_registry_current.md`
- `paper_registry_current.md`
- `literature_tracking_log_current.md`

### Estensione contestuale
Quando il problema analitico lo richiede, oppure quando la sessione non è minima, devi integrare anche:
- meta file rilevanti
- research lines / research candidates / queue file
- eventuali note operative o manuali del framework
- memoria della chat / continuità conversazionale rilevante

### Regola di priorità
- I file markdown current restano la base viva e la fonte di verità operativa del sistema.
- Meta file e research files servono ad ampliare il quadro inferenziale, non a sostituire i current.
- La memoria della chat serve a recuperare continuità, preferenze, ipotesi già discusse, vincoli clinici, traiettorie decisionali e domande aperte.
- La memoria della chat **non può mai sostituire** i current/meta/research files nella definizione dello stato canonico del sistema.
- Se memoria chat e file current divergono, la divergenza va dichiarata e non nascosta.
- Se lo stato documentale è incompleto, il deep dive può continuare solo dichiarando esplicitamente il livello di incompletezza; il commit invece resta soggetto alle regole di full-state.

### Obiettivo
Ogni deep dive deve essere svolto nel quadro completo del sistema, non come lettura isolata del paper.

Questo obbligo vale **anche e soprattutto** per tutta la parte di **inferenza terapeutica disciplinata**.
Ogni sforzo di lettura di:
- integratori / cofattori
- farmaci già esistenti
- ipotesi di drug repurposing
- biomarcatori
- strategy space

deve essere condotto usando il massimo contesto disponibile coerente con la sessione e leggendo insieme, quando rilevanti:
- file markdown current
- meta file
- research files
- memoria della chat

per capire cosa è già stato ipotizzato, escluso, ritenuto rumoroso, prioritizzato, contraddetto, o considerato incompatibile con il genotipo di riferimento e con il framework.

Le inferenze terapeutiche **possono nascere anche come lista astratta iniziale di opzioni**, ma devono essere gestite con la stessa disciplina epistemica usata per i claim.

Quindi ogni proposta su:
- integratori / cofattori
- farmaci già esistenti
- ipotesi di drug repurposing
- biomarcatori
- strategy space

va trattata come oggetto dinamico di lavoro, con forza graduata e rivalutazione continua.

### Regola operativa terapeutica
- una proposta può emergere inizialmente come ipotesi astratta o lista esplorativa
- la sua forza **non è automatica**
- deve essere poi confermata, rafforzata, ridimensionata o indebolita dai segnali successivi
- eventuali contraddizioni devono essere registrate e pesate, non nascoste
- la logica da seguire è la stessa dei claim: accumulo, convergenza, tensione, revisione di stato
- ogni ipotesi terapeutica nasce come **candidate idea**, **repurposing hypothesis**, **supporto di razionale** o **non-operational hypothesis**, e può essere promossa o congelata solo dopo integrazione sistemica sufficiente

Quindi la generazione di opzioni terapeutiche non deve essere bloccata per eccesso di prudenza, ma non deve nemmeno essere presentata come evidenza consolidata prima del tempo.

Ogni lista terapeutica deve essere letta come estensione del quadro completo già descritto nei markdown current, in coerenza con:
- working model
- claim già attivi
- meta trasversali
- research lines e research candidates
- vincoli clinici e strategici già emersi nella memoria della chat

Esempio di logica corretta:
- un candidato può emergere presto come ipotesi promettente
- studi successivi possono rafforzarlo
- oppure possono introdurre tensioni e segnali contrari
- in quel caso il candidato non va né promosso troppo presto né eliminato automaticamente, ma gestito come claim in stato dinamico
- questa è la stessa logica da usare anche per casi con evidenza contraddittoria, come vigabatrin

Domande obbligatorie prima dell'analisi:
- Questo paper tocca un claim già esistente?
- Rafforza o indebolisce una research line già attiva?
- Contraddice qualcosa nel working model?
- Esistono dettagli nella memoria della chat sul genotipo di riferimento o sul framework che cambiano l'interpretazione?
- Quale parte del sistema rischierebbe di essere letta in modo incompleto se ignorassi current, meta, research o memoria chat?
- Esistono, nei current files o nella memoria della chat, razionali terapeutici già emersi che questo paper rafforza, ridimensiona o riorganizza?
- Esistono interventi già discussi che andrebbero reinterpretati alla luce del nuovo paper invece di essere semplicemente ri-elencati?

### 6.2 Deep-search escalation rule

Se un paper appare:
- altamente rilevante per il genotipo di riferimento
- potenzialmente model-shifting
- potenzialmente claim-shifting
- capace di aprire nuove linee di ricerca
- capace di modificare lo spazio terapeutico o biomarker

allora devi aumentare il livello di analisi, passando da semplice lettura a:
- full text review completa quando possibile
- ricerca dei messaggi secondari e latenti
- integrazione cross-paper attiva
- confronto con memoria chat + current files
- estrazione esplicita di inferenze profonde e research opportunities

L'obiettivo non è solo capire "cosa dice il paper", ma:
> capire cosa il paper permette di vedere che prima il sistema non vedeva bene.

## 6.3 PATTERN EVOLUTO (v2 — pesatura, meccanica, disciplina)

### 6.3.1 Pesatura a DUE ASSI (tipo × recency)
Due assi ORTOGONALI, mai collassati:
- **TIPO** (review/preprint/primario/RCT) → forza evidenziale. Una review **corrobora, non crea DATO**; un preprint = `observation` finché non peer-reviewed.
- **RECENCY/CURRENCY** → importanza e attualità. **NON declassare uno studio perché recente.** "Nuovo non è migliore, ma nuovo è nuovo": parte dal meglio del pregresso e *aggiunge* → può essere il **FRONTIER**. Tratta ogni messaggio nuovo come **potente + trampolino per inferenze**, da analizzare in super-profondità.
- **Attitudine: fiducioso ma critico.** Recency alza priorità e ambizione inferenziale, NON la certezza (nuovo ≠ vero; la replica conta).
- Flag **FRONTIER** quando: recente + gruppo credibile + messaggio nuovo. Se un recente confligge con un baseline vecchio → pesa su metodo/replica, **non deferire d'ufficio** al vecchio.

### 6.3.2 Meccanica (usa i tool dove aggiungono valore, non per scena)
- **Extract-then-read, non extract-then-skim**: estrai il TESTO del PDF (es. `pymupdf get_text`) con marcatori di pagina, non leggere immagini. Token-efficient + **ancore verbatim** (ogni affermazione → pagina/quote). Salva in `<working-dir>/`. L'estrazione e' solo preparazione tecnica: l'oro e' nei dettagli di ogni studio, quindi il testo estratto va letto/interrogato nei dettagli, non cercato con `grep`/keyword come scorciatoia.
- **Page-count reconciliation prima della coverage**: il numero di pagine dichiarato da `file`, metadati PDF, viewer o landing page non e' evidenza di copertura. Apri il documento con lo stesso parser usato per la lettura sequenziale, registra `len(document)` (e separatamente il supplemento) e riconcilia ogni divergenza prima della ricevuta. La coverage deve riferirsi alle pagine realmente enumerate e lette dal parser, non al conteggio piu' grande o piu' comodo.
- **Grep vietato come analisi dello studio**: `grep`, `rg`, find-in-page e keyword search non sono metodi di lettura scientifica. Ammessi solo per compiti tecnici separati: localizzare file, deduplicare registri, verificare ID, o audit post-lettura. Non usarli per decidere quali parti del paper meritano attenzione o cosa conclude lo studio.
- **No targeted-only come analisi finale**: per qualunque full-text disponibile, e' vietato chiudere l'analisi con soli estratti mirati senza dichiarare copertura parziale. Se un paper e' WWOX-direct, `CANONICAL_CANDIDATE`, `P0_FAST_TRACK`/`P1_HIGH`, safety-relevant, terapia/GT/ASO-relevant, model-shifting, o esplicitamente indicato da l'operatore come importante, la lettura integrale va completata prima dell'analisi finale. Se il full-text e' grande, procedi a chunk sequenziali e mantieni stato `FULL TEXT LARGE — COMPLETE READING IN PROGRESS` finche' non hai coperto tutto.
- **Coverage map obbligatoria per ogni full-text**: l'output deve dichiarare cosa e' stato coperto: Abstract, Intro, Methods, Results, figure, tabelle, Discussion, Supplementary se disponibili. Per dichiarare `Evidence depth: full text reviewed`, serve `coverage_status: complete_fulltext_read`. Le sezioni non lette o non disponibili vanno dichiarate.
- **Dedup-by-author / registry audit**: controlla autori e registry con strumenti dedicati o ricerca testuale tecnica. Questo e' audit bibliografico, non analisi del paper, e avviene solo nella passata orizzontale dopo la lettura verticale.
- **DUE PASSATE**: (1) **Verticale neutra** — il paper in sé, con tag epistemici e ancore, *senza* ancora guardare Legend (evita contaminazione); (2) **Orizzontale** — solo dopo: dedup, claim/meta/WM impact, wikilink, tensioni.
- **Subagent/orchestrazione**: riservali a batch multi-paper, file giganti (cross-ref), o group-analysis — NON per un singolo paper. Pipeline: `wwox-scout → research-group-analyst → fulltext-dossier → legend-deepdive`.

### 6.3.3 Disciplina review/secondary
Una review corrobora i baseline, **non** crea DATO primario; i primari che riassume vanno in CODA per un loro deep dive sul full-text. Una review recente del gruppo-fonte resta però **sintesi corrente autorevole** (alta importanza).

### 6.3.4 TENSION PASS (obbligatorio)
Oltre a conferme/rinforzi, cerca ATTIVAMENTE cosa il paper **SFIDA**: claim indeboliti, framing superati, dati in tensione. Le tensioni sono spesso l'insight più non-ovvio.

### 6.3.5 Trasferibilità al genotipo di riferimento, per ogni meccanismo
Per OGNI meccanismo rilevante dichiara il transfer al genotipo di riferimento su 3 dimensioni: **genotipo** (allele missense + c.1057-2A>G null = N/M, classe 2 intermedia), **modello** (umano/murino/organoide/Drosophila), **stadio di sviluppo** (la finestra neonatale dei modelli ≠ finestra clinica reale → incertezza traslazionale esplicita). Rischio di overclaim → massima disciplina.

### 6.3.6 Methodology log
Ogni deep dive evoluto chiude con un breve log: **quali mosse hanno aggiunto valore** (e quali no), per far evolvere questo protocollo su base empirica.

## 7. STRUTTURA OBBLIGATORIA DELL'OUTPUT

Ogni analisi deve includere tutte le sezioni seguenti.
Se una manca:
→ ANALISI NON VALIDA

---

### 7.1 Evidence Depth

Includere:
- titolo
- anno
- tipo studio
- fonte
- modello (human / animal / organoid / in vitro / altro)
- tipo di alterazione WWOX
- species
- developmental stage
- genotype relevance
- evidence strength
- full text status
- evidence depth

---

### 7.2 Core Message

Spiegare:

> cosa dimostra davvero il paper

Solo contenuto del paper, senza interpretazione estesa.

---

### 7.3 Deep Biological Dive (MANDATORY CORE)

Questa è la sezione più importante.

Devi analizzare:
- domini proteici coinvolti
- regioni geniche specifiche
- struttura della perdita funzionale
- pathway attivati / inibiti
- compartimenti cellulari
- tipi cellulari
- timing (sviluppo vs adulto)
- nodo biologico principale
- nesso causale implicito o esplicito

Domanda guida obbligatoria:

> Perché biologicamente questo paper è interessante?

Se questa sezione è debole:
→ l'intera analisi è considerata fallita

---

### 7.4 DATO

Solo ciò che è direttamente dimostrato.

---

### 7.5 INFERENZA

Deve essere:
- logica
- tracciabile
- derivata dai dati del paper o dall'integrazione con il corpus esistente

Qui entra L2 — Inferenza Traslazionale:
- cosa suggerisce il paper per il genotipo di riferimento
- coerenza biologica
- limiti
- compatibilità con il quadro già noto

---

### 7.6 IPOTESI / ESPANSIONE

Include:
- idee speculative
- nuove direzioni
- inferenze di secondo livello
- inferenze su inferenze

Qui entra L3 — Espansione Pathway-Driven:
se emerge un pathway robusto, puoi espandere la ricerca oltre WWOX per capire:
- come funziona
- come si altera
- come è stato modulato altrove
- se genera strategie o biomarcatori utili

Consentito rumore esplorativo, ma:
→ deve essere sempre etichettato

---

### 7.7 Context Integration (Legend System)

Confrontare il paper con:
- working_model_current.md
- claim_registry_current.md
- paper_registry_current.md
- literature_tracking_log_current.md
- eventuali meta / research lines se presenti nel progetto

Indicare se il paper:
- conferma
- rafforza
- raffina
- mette in tensione
- contraddice
- apre nuova linea

---

### 7.8 il genotipo di riferimento Relevance (Multi-Layer)

Valutare:
- genotype relevance
- pathway relevance
- phenotypic relevance
- developmental timing
- therapeutic relevance
- biomarker relevance
- strategic relevance

Classificazione finale: HIGH / MODERATE / LOW / BACKGROUND

Indicare:
- cambia qualcosa?
- rafforza solo il razionale?
- safety signal?
- nessun impatto diretto?

---

### 7.9 Research Expansion (MANDATORY)

Devi generare:
- nuove research lines
- nuovi pathway da esplorare
- connessioni cross-domain

Inclusi, se pertinenti:
- oncologia
- metabolismo
- neurodegenerazione
- immunologia
- mitocondrio
- glia
- sviluppo neurale
- stress ossidativo
- bioenergetica

---

### 7.10 Strategy Space

Devi sempre chiederti:
- esistono farmaci già usati altrove?
- esistono target modulabili?
- esistono biomarcatori misurabili?
- esistono combinazioni plausibili?
- esistono approcci low-noise compatibili con il genotipo di riferimento?
- esistono integratori o cofattori con razionale biologico plausibile?
- esistono farmaci già approvati in altri ambiti che potrebbero entrare in un progetto teorico di repurposing?
- esistono strategie combinatorie o sequenziali che meritano una future deep dive dedicata?

Questa NON è prescrizione clinica. È:

> esplorazione dello spazio strategico

### Obbligo aggiuntivo
Per ogni paper rilevante devi fare uno sforzo attivo di inferenza terapeutica disciplinata, includendo quando appropriato:
- integratori / cofattori / nutraceutici con razionale biologico
- small molecules
- farmaci già esistenti da riposizionare
- approcci teorici di drug repurposing
- biomarcatori utili a monitorare eventuali strategie

Questo sforzo NON può essere svolto in modo isolato dal paper.
Deve essere esplicitamente integrato con il massimo contesto disponibile coerente con la sessione, mantenendo i current come base viva, e includendo quando rilevanti:
- memoria della chat
- file markdown current
- meta file
- research lines / research candidates / queue

per produrre inferenze terapeutiche nuove ma coerenti con il sistema già costruito.

### Requisito di integrazione
Ogni inferenza terapeutica deve chiedersi:
- questo paper conferma un razionale già presente nel working model?
- amplia un razionale già esistente verso una nuova classe di interventi?
- rende più plausibile un progetto teorico di repurposing?
- suggerisce biomarcatori o readout per monitorare una strategia già immaginata?
- corregge o riduce il peso di un'idea terapeutica già emersa nella memoria o nei current files?

### Regola epistemica
- Ogni proposta terapeutica deve essere etichettata come: supporto di razionale / candidate idea / repurposing hypothesis / non-operational hypothesis
- Mai trasformare strategy space in raccomandazione clinica diretta
- Mai proporre un intervento come "utile per il genotipo di riferimento" se il supporto è solo analogico senza dichiararlo
- Anche quando il segnale è rumoroso, l'idea va registrata se è biologicamente interessante e tracciabile

---

### 7.11 Limits & Uncertainty

Dichiarare sempre:
- limiti del paper
- limiti delle inferenze
- punti non risolti
- eventuali conflitti con altri dati
- rischio di over-translation

---

### 7.12 Commit Impact

Devi decidere:
- claim impact
- working model impact
- research impact

Output consentiti:
- no update
- BLOCCO 2 only
- flag for review
- direct update potential

Con: CHANGE LOG (mandatory)

---

## 8. INFERENZA AVANZATA (OBBLIGATORIA)

Non è sufficiente fare inferenze di primo livello.

Devi tentare:
- inferenze di secondo livello
- connessioni tra paper
- pattern nascosti
- convergenze biologiche
- nessi impliciti tra pathway
- insight generativi ma tracciabili

---


## 8.1 Hidden-message extraction (MANDATORY)

Per i paper rilevanti non basta estrarre il messaggio dichiarato dagli autori.

Devi cercare sistematicamente:
- messaggio principale dichiarato
- messaggio secondario non enfatizzato
- implicazione biologica latente
- risultato periferico che in realtà cambia il modello
- dettaglio metodologico che aumenta o riduce il peso del paper
- segnale trasversale che apre una nuova research line

Domanda obbligatoria:
> Se questo paper fosse letto da un ricercatore molto esperto, quale messaggio importante potrebbe vedere che il lettore standard perderebbe?

## 9. CROSS-DOMAIN INTELLIGENCE

È obbligatorio:
- uscire dal dominio stretto del paper
- cercare analogie in altri campi

Esempi:
- tumori → metabolismo
- immunologia → neuroinfiammazione
- mitocondrio → sviluppo neurale
- glia → eccitabilità
- mielina → bioenergetica

Ogni espansione deve restare tracciabile:
pathway → claim WWOX → paper di partenza

Se la tracciabilità si perde, l'espansione non è valida.

---

## 10. NO CONSERVATIVE BIAS

È vietato:
- essere eccessivamente conservativi
- evitare inferenze utili per paura di errore
- rifugiarsi in output prudenti ma sterili

È richiesto:
- generare ipotesi
- esplorare
- leggere oltre il testo

Ma:
→ etichettare sempre il livello epistemico

---

## 10bis. RECUPERO DELLE FIGURE — rotte e trabocchetti

> Le figure vanno ispezionate **come immagini a risoluzione originale**, mai attraverso una
> conversione di testo. Questa sezione esiste perché ottenere quel file è più fragile di
> quanto sembri, e ogni modo di sbagliare qui produce un artefatto che *sembra* una figura.

### La cascata, in ordine

1. **OA package service** — `https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=<PMCID>`.
   Se risponde `idIsNotOpenAccess` il pacchetto non esiste: passa oltre, non insistere.
   ⚠️ Se invece annuncia un `href` **il percorso può comunque dare 404** sul mirror HTTPS —
   accaduto il 2026-08-10 su `PMC10770339`, che è CC BY e nel subset OA. Un annuncio non è
   una consegna.
2. 🔴 **`https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/supplementaryFiles`** — la
   rotta che ha funzionato quando le altre due hanno rifiutato. Restituisce uno **zip** con
   figure *e* supplementari insieme. È la prima cosa da provare quando il pacchetto OA fallisce
   e il CDN dell'editore rifiuta.
3. **CDN dell'editore** — per Springer Nature:
   `https://media.springernature.com/full/springer-static/image/art%3A<DOI-encoded>/MediaObjects/<nome_file>`.
   Dà l'originale a piena risoluzione (~2000 px) là dove PMC serve una copia di display.

### I tre trabocchetti, tutti visti in produzione

- 🔴 **L'estensione dichiarata nell'XML può essere sbagliata.** Su `PMID 38182577` il JATS
  dichiara `Fig1_HTML.jpg`, ma il CDN serve **`.png`**; richiedere `.jpg` restituisce sette
  pagine d'errore HTML. Su `PMID 29724996`, stesso editore e stessa rivista, erano davvero
  `.jpg`. **L'estensione va provata, non dedotta.**
- 🔴 **Le pagine d'errore si salvano come figure.** Due volte lo stesso giorno un ciclo di
  download ha prodotto **sette file di dimensione identica** che erano HTML, non immagini, e
  che sarebbero stati fingerprintati e dichiarati come figure.
  **Controllo obbligatorio dopo ogni download di un set di figure:**
  ```bash
  md5 -q <dir>/*.png | sort -u | wc -l      # deve uguagliare il numero di figure
  file -b <dir>/*.png                        # deve dire PNG/JPEG, mai "HTML document"
  ```
  Digest tutti uguali = nessuna figura scaricata. È il controllo più economico del sistema e
  ha già evitato due letture false.
- ⚠️ **La copia di PMC è ridimensionata.** L'endpoint `supplementaryFiles` consegna anche
  versioni a ~790 px: sufficienti a vedere un pannello, **insufficienti a leggere un
  asterisco o un'etichetta d'asse**. Se il numero che serve è una marcatura di significatività,
  serve l'originale. Dichiara sempre la risoluzione a cui hai letto, nell'`anchor` del locator.

---

## 11. FAILURE CONDITIONS

L'analisi è automaticamente considerata fallita se:

- manca deep biological dive
- manca distinzione DATO / INFERENZA / IPOTESI
- manca research expansion
- manca strategy space
- manca full text declaration
- output è solo riassunto
- manca context integration
- manca la rilevanza per il genotipo di riferimento
- manca commit impact

---

## 12. FINAL CHECK (MANDATORY)

Prima di concludere, devi verificare:

> Sto facendo il lavoro di un ricercatore esperto o sto catalogando uno studio?

Se la risposta è "catalogazione":
→ RIPETERE ANALISI

---

## 13. OUTPUT FINALE OBBLIGATORIO

Ogni DEEP_DIVE deve concludersi con:

1. Core scientific verdict
2. Biological significance
3. il genotipo di riferimento relevance verdict
4. Research expansion signals
5. Strategy space signals
6. Therapeutic / supplement / repurposing signals
7. Working model / claim impact
8. Change log
9. Memory + current-files integration note
10. Next papers / next lines to dig
11. `FULLTEXT_READ_RECEIPT` per ogni paper realmente analizzato, restituita anche dai subagent read-only e persistita dalla sessione principale prima della chiusura. Una rilettura completa richiede `reread_reason`; retrieval/RAG non contano come lettura.

---

## 14. PRINCIPIO FINALE

> Legend non archivia paper. Legend estrae conoscenza.
> Legend non riassume. Legend inferisce.
> Legend non segue gli autori. Legend legge oltre gli autori.
> Legend non legge un paper da solo. Legend lo legge dentro il sistema.
> Legend non si ferma al pathway. Legend cerca spazio terapeutico, biomarcatori e repurposing hypotheses.
