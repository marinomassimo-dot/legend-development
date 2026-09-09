# I quattro casi residui e le tre questioni di schema — 2026-09-09

Chiusi o circoscritti quanto la mia autorità consente. Ciò che resta all'operatore è isolato in § 5,
ed è deliberatamente corto.

---

## 1 · `33914858` — Repudi 2021, *Brain* — richiede il browser

**Perché conta più della sua posizione in lista:** è la **fonte primaria di `CLAIM 003`**, una
*consolidated baseline* (ipomielinizzazione non-cell-autonoma da delezione neuronale di Wwox), in un
campo di 8 record PubMed per `WWOX AND myelin`. Nessun receipt è mai esistito per questo PMID.

**Cascata esaurita, 19 tier** (2026-09-09, `scientist-a`): nessun record PMC; bronze OA con una sola
location dell'editore dietro Cloudflare in ogni forma di header; OpenAIRE `instance: null`; CORE,
BASE, DOAJ, Zenodo, HAL vuoti; Wayback vuoto su quattro prefissi; i record istituzionali espongono
solo link DOI; nessun preprint esiste. **Una via rifiutata e non fallita**: l'HTML dell'editore è
leggibile e `WebFetch` lo raggiunge, ma restituisce una ricostruzione del modello, non i byte
dell'autore — regola 5c, e un locator verificato contro una ricostruzione **passa combaciando con la
ricostruzione**.

### Cosa devi acquisire, esattamente

| | |
|---|---|
| DOI | `10.1093/brain/awab174` |
| Cosa | il **PDF dell'editore**, salvato dal browser (non stampato-su-PDF, non «salva come HTML») |
| Dove depositarlo | `files/fulltext/PMID33914858_Aqeilan2021.pdf` — **questo nome esatto**, è quello che `FT-044` registra |
| Se esiste un supplemento | `files/supplement/PMID33914858/` con i nomi originali |

Crea le directory se non esistono; `files/` è gitignorato per progetto, quindi **non committare nulla
di ciò che depositi** — il manifest ne registrerà le impronte.

### Cosa cambia rispetto all'ultima volta che è stato sospeso

La voce `FT-044` sospese la lettura il 2026-08-09 **non** per copertura o budget, ma per invalidità
della superficie testuale: l'estrazione deterministica restituisce `P 5 0.05` dove la pagina stampa
`P < 0.05`, con zero occorrenze di `<`, `>`, `≤`, `≥` in tutto il documento contro 14 di `P 5 0.0…`.
`fitz`, `pdfplumber` e `pypdf` concordano tutti e tre sul carattere sbagliato, **quindi incrociare
due estrattori non rileva il difetto**. La sospensione diceva che ripararlo «richiede un gate che non
esiste ancora».

🟢 **Quel gate ora esiste ed è eseguibile.** PyMuPDF è stato installato oggi, e la regola 5e —
ancorare i locator alla **pagina renderizzata** invece che al livello testuale — è passata da
ineseguibile in questo deployment a usata davvero: `scientist-a` ha prodotto oggi la prima lettura
per aggiudicazione di pagina di questo repository (`24510053`, 9 locator, 9/9 rigenerano). Quindi
appena il PDF è sul disco, la lettura può procedere **senza riparare il testo** e senza il rischio
che la sospensione voleva evitare.

**Non ho ritentato la cascata**: era esaurita stamattina e nulla è cambiato nell'accessibilità.

---

## 2 · `20146584` — Salah 2010 — due immagini, e forse non serve il browser

**Stato:** `partial_fulltext_read` per **declassamento dichiarato e corretto**. Il testo è stato letto
per intero; le due immagini di figura non sono state ottenute, quindi `figures: captions_only`, che
declassa il receipt. I due locator di figura nel manifest sono `surface: body` e attestano **solo il
testo della didascalia**.

| | |
|---|---|
| PMCID | `PMC2832309` |
| Le due immagini | `nihms-180622-f0001.jpg` · `nihms-180622-f0002.jpg` |
| Dove andrebbero | `files/figures/PMID20146584/` con i nomi originali |
| Costo del debito, misurato | la Figura 2 è il pannello che il testo indica **due volte** come il proprio riassunto di signalling |

### Cosa ho verificato io oggi, oltre alla cascata già registrata

- **La variante «nessun User-Agent» non risolve gli asset.** `/bin/nihms-180622-f0001.jpg` e `-f0002.jpg`
  restituiscono **HTTP 200 con la pagina di challenge** (21.400 e 21.397 byte di HTML) anche senza
  User-Agent. Conferma il reperto di `scientist-b` — l'asset esiste dietro il reCAPTCHA — e **ne
  delimita il workaround**: togliere lo User-Agent sblocca l'HTML dell'articolo, non i percorsi asset.
- **L'endpoint OA REST risponde 404**, il che è coerente e non è un guasto: è un *author manuscript*
  NIHMS, quindi fuori dal subset open-access di PMC. Europe PMC lo diceva già con
  *«not open access one»*.
- **La via `?pdf=render` di Europe PMC è ora rate-limited (429)**, non fallita. Quando fu tentata
  restituì 429 e poi **HTTP 500** due volte, cioè un guasto di servizio, non un rifiuto.

🟡 **Conseguenza operativa: questo caso può chiudersi senza di te.** Merita **un solo ritentativo** di
`?pdf=render` a distanza di ore; se il PDF arriva, PyMuPDF — installato solo oggi — estrae le due
figure alla risoluzione depositata e il receipt sale a `complete`. Solo se anche quello fallisce
serve il browser, e in quel caso le due immagini si salvano dalla pagina PMC dell'articolo.

---

## 3 · `25331887` e `34268881` — copertura reale contro impedimento di schema

Questi due **non sono letture mancanti** e vanno tenuti distinti dai due casi sopra. Documentati
separatamente, come richiesto.

### `25331887` — Abu-Odeh 2014, *PNAS*

| Dimensione | Stato |
|---|---|
| **Copertura effettiva** | **completa**. Il corpo fu letto nel 2026-08 e la sua coverage map non contiene alcun `not_read`; l'unica ragione di parzialità era `supplementary: unavailable`. Oggi il supplemento è stato ottenuto (`pmc_pow_fetch.py`, 6 pagine), letto come immagini renderizzate sotto la regola 5d perché il suo livello testuale è SUSPECT e **rifiutato, non ripulito**, e sottoposto a un audit cieco su 10 triple |
| **Verifica indipendente** | l'audit ha corretto 6 overshoot su 10, ha trovato **due attestazioni fattualmente sbagliate**, e ha fatto **ritirare per intero** il ponte P47T che il lettore aveva definito «attraente» |
| **Impedimento** | il receipt di oggi attesta ciò che *quell'evento* ha fatto: leggere il supplemento. Non può dichiarare `complete` senza scrivere una coverage map per sezioni che l'evento non ha aperto |
| **Perché non è stato aggirato** | manufacturare quella mappa sarebbe stato l'unico modo di far coincidere il numero con la realtà, ed è esattamente ciò che il protocollo vieta |

### `34268881` — Steinberg 2021, EMBO Mol Med

| Dimensione | Stato |
|---|---|
| **Copertura effettiva** | **completa già prima di oggi**. Il dispatch assegnava `inadequate_prior_coverage`, ma il lettore ha verificato che il receipt del 2026-08-14 aveva letto ogni sezione e tutti i 69 pannelli: **l'insieme delle sezioni scoperte è vuoto** |
| **Cosa mancava davvero** | non una lettura, ma i **byte**: nessuno dei 21 artefatti era nel checkout. Tutti e 21 riacquisiti, **ognuno byte-identico** al digest dichiarato; il validator è passato da 22 BLOCK a PASS |
| **Impedimento** | il receipt esistente resta etichettato `partial` perché il suo autore lo dichiarò tale per figure d'appendice citate ma mai distribuite. Sotto la lettera del contratto quel receipt **si qualificherebbe come completo** |
| **Domanda aperta** | dove vada il materiale citato ma non distribuito in una coverage map. Due letture difendibili, ed è questo il problema |

**Da entrambi i casi: nessuna attestazione è stata modificata retroattivamente.** La discrepanza fra
«copertura reale» e «profondità registrata» è documentata, non appianata.

---

## 4 · Le tre questioni di schema

Per ciascuna: riproduzione minima, impatto misurato, rimedio proposto, e la regressione che
dimostrerebbe il rimedio. **Nessuna è stata implementata** — toccano il contratto di un ledger
append-only, cioè il significato di attestazioni già scritte.

### 4.1 · Rollup a livello di studio — **la sola con impatto numerico oggi**

- **Riproduzione minima.** Un receipt A dichiara `supplementary: unavailable`, tutto il resto letto.
  Un receipt B, mesi dopo, legge il supplemento e nient'altro. Nessuno dei due può dichiarare
  `complete_fulltext_read`: A non ha il supplemento, B non ha il corpo. Non esiste campo che dica che
  **l'unione** delle due coperture è completa.
- **Impatto misurato.** 2 dei 54 (`25331887`, `34268881`) restano `partial` pur avendo copertura
  piena. Con la contabilità attuale il lotto legge 19/23 invece di 21/23.
- **Rimedio proposto.** Un `record_kind: study_coverage_rollup` che **non contenga letture proprie**,
  citi due o più `prior_receipt` e dichiari solo l'unione delle loro coverage map — non potendo
  quindi mai asserire una sezione che nessun evento ha letto.
- **Regressione che lo dimostrerebbe.** Un fixture con due receipt le cui mappe si uniscono a completa
  produce un rollup `complete`; un secondo fixture in cui **resta un buco** deve produrre `partial` e
  fallire se produce `complete`; un terzo deve rifiutare un rollup che dichiari una sezione assente da
  entrambi i genitori.

### 4.2 · `identity_correction`

- **Riproduzione minima.** Un receipt persiste un DOI sbagliato. Il writer rifiuta poi il DOI corretto
  con `conflicting identifiers for the same study`. `receipt_correction` deve **preservare** l'identità
  di studio, cioè proprio il campo sbagliato; `receipt_invalidation` riguarda evidenze appartenenti a
  uno studio **diverso**. Esito netto: **il ledger rifiuta l'identificatore corretto perché ne è stato
  scritto uno sbagliato prima**.
- **Impatto.** Occorso una volta oggi (`scientist-c`, wave 1). Il valore vero sopravvive solo in prosa
  dentro `evidence_basis` e nel dossier — cioè fuori dai campi su cui qualunque strumento interroga.
- **Rimedio proposto.** `record_kind: identity_correction` che modifichi **solo** `study_id`, congeli
  ogni campo di lettura e si colleghi via `prior_receipt`.
- **Regressione.** Un fixture che tenti di alterare un qualsiasi campo di lettura dentro un
  `identity_correction` deve fallire; uno che corregga solo il DOI deve passare e lasciare invariata la
  profondità.
- **Rischio: basso.** È l'unica delle tre che non tocca il significato di «completo».

### 4.3 · Relazioni fra pannelli sui locator aggiudicati

- **Riproduzione minima.** Sotto la regola 5e i locator ancorati alla pagina renderizzata portano
  `surface: figure`. Il marcatore di relazione accoppiata va, per regola documentata, sulla voce
  *figure*. Un locator di **testo** aggiudicato eredita quindi `surface: figure` e la relazione non
  trova dove essere dichiarata.
- **Impatto.** `scientist-c` aveva **tre relazioni genuine** su `16223882` e non ha potuto dichiararne
  nessuna. La perdita colpisce **esattamente i paper la cui superficie è peggiore**, cioè quelli in
  cui l'aggiudicazione serve di più.
- **Rimedio proposto.** Un valore di `surface` distinto per il testo aggiudicato (per esempio
  `page_adjudicated_text`), oppure permettere la relazione accoppiata su quel sottotipo.
- **Regressione.** Un fixture in cui un locator di testo aggiudicato dichiara una relazione accoppiata
  deve passare la validazione strict; e la regola esistente che vieta la relazione su una voce di
  corpo non aggiudicata deve restare rossa.

---

## 5 · Cosa resta davvero all'operatore

1. **Il PDF di `33914858`** dal browser, in `files/fulltext/PMID33914858_Aqeilan2021.pdf`. È l'unico
   dei quattro che nessuna automazione può risolvere.
2. **Una decisione su § 4.1 e § 4.3**, perché cambiano cosa significa un'attestazione già scritta.
3. **§ 4.2 è pronta e a rischio basso**: se autorizzi, si implementa con la sua regressione.

`20146584` **non** è nella lista: merita prima un ritentativo automatico.
