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

## Core (sempre)
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

# FRASE FINALE

> Meglio bloccare un commit
> che perdere mesi di ricerca
