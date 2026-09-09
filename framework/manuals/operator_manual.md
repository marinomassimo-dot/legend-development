# Operator manual — running LEGEND

> **Public edition — de-identified, generic.** The day-to-day operating guide: session types, what to load, which mode to declare, when a batch commit is allowed, and the safety gates around it. It contains method only — no individual, no clinical content, no case history. Paths refer to the public three-layer structure (`framework/`, `disease-models/<disease>/`); the private N-of-1 overlay is not part of this repository. Preserved in its original language: it is the working text the system is actually run from. **Not medical advice.**

---

# OPERATOR_MANUAL.md
# Guida operativa unica — Sistema LEGEND
# Version: v1.1 — freeze-ready

---

## SCOPO

Ridurre al minimo il carico operativo mantenendo la massima qualità del sistema.

> Legend pensa
> L'operatore esegue operazioni semplici, chiare e verificabili

---

# 1. MODALITÀ DI SESSIONE

Scegliere e dichiarare `SESSION_PROFILE` in base al **compito**, non al ruolo o al runtime.
I profili sono `HARNESS`, `MINIMAL`, `STANDARD`, `FULL`. Senza un compito definito usare
`MINIMAL`; un compito misto applica anche il profilo scientifico prima del lavoro scientifico.
Se il compito cambia, caricare il contesto del nuovo profilo prima di procedere.

## 1.0 SESSIONE HARNESS — manutenzione tecnica

**Quando**
- codice, test, documentazione, skill, governance o strumenti, senza analisi scientifica

**Caricare**
- catena iniziale di `AGENTS.md` / `CLAUDE.md`: manifest di stato, istruzioni e governance,
  contratto del ruolo assegnato, indice dei protocolli e skill di avvio/chiusura richieste
- file di implementazione, protocolli e test pertinenti al compito
- registri scientifici solo se necessari all'ispezione tecnica: cercare gli identificativi
  o la struttura interessata e leggere i record/sezioni completi pertinenti; ampliare la
  lettura se la dipendenza lo richiede, senza un tetto che nasconda il contesto necessario

**Verificare**
- LINT strutturale anche in questo profilo: il programma legge i file dal disco, senza
  riversarli nel contesto del modello; non equivale ad averli letti scientificamente
- controlli e regressioni richiesti da `LEGEND_CORE.md` §21e

Una manutenzione del validatore o una ricerca tecnica non attesta una lettura scientifica.
Prima di analizzare un paper, formulare conclusioni o propagare evidenze, passare al profilo
scientifico pertinente e caricarne il contesto. Le letture full-text, i receipt, i locator e
`BATCH_COMMIT` conservano i propri obblighi; il profilo non li sostituisce.

## 1.1 SESSIONE MINIMA — veloce

**Quando**
- triage paper
- analisi singola
- insight locale

**Caricare**
- 4 file current

**Non fare**
- no meta
- no commit
- no research layer

---

## 1.2 SESSIONE STANDARD — lavoro reale

**Quando**
- nuovi paper rilevanti
- insight strutturati

**Caricare**
- 4 current
- meta_index
- meta rilevanti (solo quelle coinvolte)

**Fare**
- aggiornare claim
- aggiornare meta

---

## 1.3 SESSIONE FULL — commit

**Quando**
- fine ciclo
- nuova meta
- cambio modello

**Caricare**
- tutti i file (tutti i layer)

**Fare**
- commit completo
- propagation checklist

---

## REGOLA

> Non tutte le sessioni devono essere FULL

---

# 2. FILE DA USARE (PRATICA)

## Core scientifico (MINIMAL / STANDARD / FULL; per HARNESS vedere §1.0)
- working_model_current.md
- claim_registry_current.md
- paper_registry_current.md
- literature_tracking_log_current.md

## Meta (quando serve)
- meta_index_current.md
- meta_*.md rilevanti

## Research (avanzato)
- research_lines_current.md
- research_candidates_current.md
- full_text_queue_current.md

---

# 3. GESTIONE FILE (ANDROID)

## Struttura consigliata

Cartella unica:

`WWOX_LEGEND/`

Dentro: tutti i .md del sistema

---

## Se parti da file sparsi

Su Android:

1. Apri File Manager
2. Crea cartella → `WWOX_LEGEND`
3. Sposta dentro tutti i file uno a uno

---

## Regola critica

> NON usare i file dai "recenti" senza verificarli

---

# 4. DOPO UN COMMIT

Quando Legend produce output:

## Passaggi

1. Scarica file (finisce in Download)
2. Apri file
3. Usa "Sposta" o "Copia in"
4. Spostalo in `WWOX_LEGEND`
5. Sovrascrivi file esistente

---

## Regola

> Devi sostituire il file vecchio, non tenerli entrambi

---

# 5. ERRORI DA EVITARE

## Priorità reale

### 1. Versione sbagliata (più pericoloso)
Carichi file vecchio dai recenti → sistema corrotto

### 2. File duplicati
Esempi:
- file (1).md
- file_new.md

### 3. File aggiornati lasciati in Download
Non vengono usati → sistema disallineato

### 4. Commit parziale applicato
Solo alcuni file aggiornati → incoerenza

### 5. Editing manuale fuori sistema
Modifichi file ma non lo ricarichi

---

# 6. CHECK PRIMA DI SESSIONE FULL

## CURRENT
- tutti presenti
- nessun duplicato

## META
- coerenti con meta_index

Come verificare (Android):
1. Apri `meta_index_current.md`
2. Leggi i nomi delle meta attive
3. Vai nella cartella `WWOX_LEGEND/`
4. Verifica che ogni file meta esista davvero

❗ Se una meta è nel file ma non nella cartella → incoerenza

## FILESYSTEM
- uso cartella corretta
- no file da Download

## COMMIT
- ultimo commit applicato

---

## Decisione

✔ tutto ok → FULL
⚠ dubbio → STANDARD
❌ problema → STOP

---

# 7. RECOVERY

Se non sei sicuro, carica almeno i 4 current + meta_index, poi scrivi:

> "verifica coerenza tra i file caricati e dimmi se posso fare commit o serve riallineamento"

---

# 8. OUTPUT LEGEND (COSA FAI TU)

Legend ti dirà:

- FILE DA CREARE
- FILE DA AGGIORNARE
- FILE INVARIATI

## Tu devi fare solo:

- salvare
- sostituire file
- ricaricare

---

## CHANGE LOG (OBBLIGATORIO)

Legend produce anche:

- CHANGE LOG per ogni file modificato

Contiene:
- cosa è stato aggiunto
- cosa è stato modificato
- eventuali anomalie (es. stati claim non standard)

## Cosa devi fare

- leggilo rapidamente
- NON devi interpretare o modificare
- serve solo per capire cosa è cambiato

---

## Regola

> Il CHANGE LOG è parte del commit, non opzionale

---

## Regola generale

> Zero interpretazione
> Zero editing manuale

---

# 9. PRINCIPIO OPERATIVO

> Meglio una sessione STANDARD pulita
> che una FULL su stato incerto

---

# 10. FILOSOFIA DEL SISTEMA

- il rischio vero è la desincronizzazione
- il sistema funziona solo se i file sono coerenti
- Legend è responsabile del contenuto
- l'operatore è responsabile dello stato dei file

---

# SESSION TYPES — AUTOPILOT-ERA ADDITIONS

*(Workflow additions to the context profiles in §1. Profile selection and load lists live
there; this section adds the applicable scientific workflow.)*

**Always read the state manifest first**, in every session type. It is the first load target, not
an optional extra, and `current_state: READY` is confirmed before analytical work begins.

Every profile applies `legend-start`, `legend-capability-scout` and `legend-session-takeaways`.

**Harness** — technical maintenance follows §1.0 and the harness lifecycle in `LEGEND_CORE.md`
§21e. A framework change does not by itself require a Full scientific session.

**Minimal** — if studies are supplied, apply intake triage, the batch inferential
sweep and the priority matrix. No commit required.

**Standard** — with a study list, use
the autopilot by default and continue autonomously through ingest / full-text / deep-dive /
discovery / therapeutic fan-out where the gates allow. Produces commit candidates; propagation
happens only through `BATCH_COMMIT`.

**Full** — scientific bootstrap, scientific recovery, batch consolidation and meta propagation.
Rigorous commit mandatory. First-run laboratory setup follows `BOOTSTRAP.md`.

> Prefer a clean Standard session over a Full session on uncertain state.

---

# FRASE FINALE

> Meglio bloccare un commit
> che perdere mesi di ricerca
