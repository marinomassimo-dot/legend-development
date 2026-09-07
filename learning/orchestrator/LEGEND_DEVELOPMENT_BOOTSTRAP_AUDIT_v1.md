---
artifact: LEGEND DEVELOPMENT BOOTSTRAP AUDIT
version: v1
status: PROPOSED — analisi indipendente, nessuna modifica applicata
mandate: LEGEND Development Bootstrap Audit v1
subject: legend-development · workflow "Public release gate" · run 32666385829 · main @ 788c357
authored_on: 2026-08-23
normative: no — questo documento propone, non legifera
coordination: nessuna. Sessione indipendente da Orchestrator, Mirror e Plan.
---

# LEGEND DEVELOPMENT BOOTSTRAP AUDIT v1

**Ambito.** Analisi, classificazione e proposta. Nessuna modifica è stata applicata a
`legend-development`, ai workflow, ai test o alla repository. Nessun commit, nessun push,
nessuna PR. Questo file è creato non committato.

**Metodo.** Ogni affermazione qui sotto è stata verificata direttamente: il log completo del run
(2 133 righe, scaricato con `gh run view --log`), il file di workflow, il codice dei test
falliti, il codice sotto test, i modi dei file nell'albero git, le dipendenze dichiarate, la
configurazione di entrambe le repository via API GitHub, e la storia git delle cause radice.
Dove un numero compare, compare con il denominatore da cui è stato ricavato.

---

## 1 · Executive summary

### Cosa è fallito

Un solo step: **`Regression tests`** (`python3 scripts/run_release_regressions.py`), exit 1.

Lo step `Structural framework lint` non è mai partito perché il precedente ha fallito.
Lo step **`Public release gate`** — il gate di pubblicazione vero e proprio — **è passato**
(gira con `if: always()`, quindi ha eseguito ed emesso il suo verdetto). Anche
`Upload gate report` è passato.

> Il failure **non viene dal gate di pubblicazione**. Viene dalla batteria di regressioni, che è
> igiene di repository e coerenza interna. Questa distinzione è la chiave dell'intero audit e
> smonta la lettura più comoda («è un gate di release, non riguarda development»).

`REGRESSION VERDICT: FAIL` su **8 suite**, riconducibili a **4 cause radice**:

| # | Causa radice | Suite colpite |
|---|---|---|
| A | 5 token normativi rimossi da `CLAUDE.md` dalla migrazione a router | 4 |
| B | Una suite esiste nel repository e la batteria non la esegue mai | 1 |
| C | 4 entrypoint con shebang committati con modo `100644` | 1 |
| D | Ambiente CI: PyMuPDF assente + clone superficiale | 2 |

### Il failure indica un problema reale?

**Sì, in parte — e la parte reale è più grave di quella cosmetica.**

- **B e C riproducono in locale**, senza CI, senza rete, su qualsiasi checkout completo. Sono
  difetti di contenuto verificati: 1 suite su 66 non viene mai eseguita, 4 file su 4 hanno il
  modo sbagliato *nell'indice git* (non sul filesystem del runner).
- **D non dice nulla sul contenuto**: è ambiente e workflow. Ma rivela un difetto di
  progettazione reale (F-09) in un contratto di degradazione che il repository *aveva già
  scritto e testato* per il caso adiacente.
- **A è la più delicata**: nessuna regola è andata persa — tutte e 5 sopravvivono nella loro
  sede normativa. Ma la migrazione ha spostato le «inviolable facts» sulla sola superficie che
  **non** viene caricata automaticamente nelle sessioni Claude. Il test misura all'indirizzo
  vecchio, ma la proprietà che difende è ancora vera. Vedi §4A: non è un test obsoleto.

### È atteso in una development repository?

**No.** Nessuna delle 8 suite fallite verifica una proprietà specifica della pubblicazione.
Verificano: che ogni test scritto venga eseguito, che gli entrypoint siano avviabili, che le
regole operative raggiungano la superficie di avvio sessione, che il freeze DisMech regga.
Sono esattamente le proprietà che servono **di più** dove agenti lavorano in autonomia.

L'unica suite con «release» nel nome, `test_release_surface.py`, ha prodotto un finding
(il bit di esecuzione) che è vero anche in development: un `.py` con shebang e modo 644
non si avvia come `./<script>.py` in nessun ambiente.

### Il workflow è progettato correttamente per questo ambiente?

**No, per tre ragioni indipendenti.**

1. `on: push` senza filtro di branch → la batteria completa (65 suite, ~3 min) gira su ogni
   push di ogni branch di una repository a sviluppo continuo.
2. `--mode release` è cablato nello step. `public_release_gate.py` espone
   `staging | release | clone`: **non esiste un modo development**.
3. `fetch-depth: 1` è incompatibile con un verificatore che risolve un commit di freeze
   distante 415 commit. Il workflow è stato scritto per una repository dove quel verificatore
   non esisteva ancora.

### Il fatto che riscrive la cornice

`legend-development` è stata creata **oggi alle 20:47Z**; il run analizzato è **l'unico run mai
eseguito** in quella repository (`total_count: 1`). Ma lo stesso identico workflow è **verde
4 volte su 4** sulla repository stabile `wwox-rare-disease-legend`, l'ultima il **2026-08-01**.

Fra quel run verde e `788c357` ci sono **455 commit in 22 giorni**, e le date d'introduzione
delle quattro cause radice cadono tutte dentro quella finestra:

| Causa | Introdotta | Commit |
|---|---|---|
| D (freeze DisMech) | 2026-08-04 | `3dbedf3` / freeze `8ca2712` |
| D (test `fitz` non guardato) | 2026-08-10 | `385dd28` |
| A (CLAUDE.md → router) | 2026-08-16 | `04cbd3b` |
| C (3 dei 4 file non eseguibili) | 2026-08-16 / 08-17 | `9720a0c`, `36305c6`, `b2c326b` |
| B (suite non registrata) | 2026-08-17 | `b2c326b` |
| C (quarto file) | 2026-08-18 | `325da04` |

> **Il problema non è che il gate sia stato applicato a development. È che per 22 giorni e 455
> commit non è stato applicato nulla.** Il run di oggi non ha introdotto i difetti: li ha
> mostrati tutti insieme, per la prima volta.

---

## 2 · Lista completa dei finding

Categorie ammesse: `BUG_REALE` · `DEBITO_ARCHITETTURALE` · `TEST_OBSOLETO` ·
`WORKFLOW_PROBLEM` · `ENVIRONMENT_PROBLEM` · `DEVELOPMENT_SCOPE_MISMATCH`.

**Distribuzione:** BUG_REALE 3 · DEBITO_ARCHITETTURALE 6 · WORKFLOW_PROBLEM 2 ·
ENVIRONMENT_PROBLEM 2 · DEVELOPMENT_SCOPE_MISMATCH 2 · **TEST_OBSOLETO 0**.
Lo zero è deliberato e argomentato in §4A: la categoria è stata considerata e respinta.

---

### F-01 — `CLAUDE.md` non contiene più 5 token che 4 suite pretendono

| Campo | Contenuto |
|---|---|
| **ID** | F-01 |
| **Descrizione** | La migrazione di `CLAUDE.md` a router puro (`04cbd3b`, 2026-08-16) ha rimosso 5 stringhe che 4 suite di regressione asseriscono debbano trovarsi *in quel file*. Nessuna regola è andata persa: tutte e 5 sopravvivono nella loro sede normativa (verificato uno per uno). Ciò che è caduto è la copia sulla superficie di avvio sessione. |
| **Evidenza** | 5 fallimenti in 4 suite: `test_locator_obligation_reaches_every_route.py:121` (`verbatim_locators`) · `test_abstract_corpus_is_not_evidence.py:234` (`pubmed_corpus_harvest`) · `test_fulltext_trace_contract.py:29,38` (`FULLTEXT_READ_RECEIPT`, `state-control`) · `framework/scripts/test_session_self_eval.py:62` (`session_self_evaluation.md`). Verifica locale: tutti e 5 ASSENTI sia in `788c357:CLAUDE.md` sia nel working tree. Verifica delle sedi normative: `verbatim_locators` PRESENTE in `framework/protocols/fulltext_read_receipt.md`; `FULLTEXT_READ_RECEIPT`, `state-control` e `POST-BATCH SELF-DIAGNOSIS` PRESENTI in `framework/instruction/LEGEND_CORE.md`; `state-control` PRESENTE anche in `state_manifest_current.md`; il vincolo sul corpus PRESENTE in `AGENTS.md`. |
| **Categoria** | `DEBITO_ARCHITETTURALE` |
| **Impatto** | **Alto** |
| **Rischio futuro** | Due decisioni normative deliberate e opposte convivono su `main`: governance v3.1.1 §0.3 impone il router; 4 suite impongono la duplicazione. Finché non si sceglie, la batteria resta rossa e ogni futuro run va letto «a meno di quelle 5», che è il modo in cui una batteria smette di essere letta. |
| **Soluzione possibile** | *Proposta, non applicata.* Tre opzioni mutuamente esclusive in §4A. La raccomandazione dell'audit è l'opzione 3 (superficie di avvio dichiarata in un registro, test parametrizzati su quel registro) perché è l'unica che sopravvive alla prossima migrazione. |
| **Decisione umana richiesta** | **Sì** — governance |

---

### F-02 — Le «inviolable facts» sono uscite dall'unica superficie auto-caricata per Claude

| Campo | Contenuto |
|---|---|
| **ID** | F-02 |
| **Descrizione** | I 4 test di F-01 iterano sulla coppia `("CLAUDE.md", "AGENTS.md")` come «superfici di bootstrap». Dopo la migrazione, le inviolable facts vivono **solo** in `AGENTS.md`, che è dichiarato «entry point per Codex e tooling agentico compatibile». `CLAUDE.md` è il file che Claude Code carica automaticamente in ogni sessione; `AGENTS.md` no. La migrazione ha quindi spostato le regole inviolabili **fuori** dalla superficie auto-caricata per le sessioni Claude, e **dentro** quella auto-caricata per Codex. |
| **Evidenza** | `AGENTS.md` (37 righe) contiene la sezione «Inviolable facts» con `FULLTEXT_READ_RECEIPT`, `verbatim_locators` e il vincolo `pubmed_corpus_harvest`; `CLAUDE.md` non contiene nessuno dei tre. Evidenza diretta e osservata: il contesto di *questa* sessione Claude riceve `CLAUDE.md` come istruzioni di progetto e **non** `AGENTS.md`. `AGENTS.md` §Sync rule dichiara esso stesso l'asimmetria: «CLAUDE.md routes, it does not adjudicate». |
| **Categoria** | `BUG_REALE` |
| **Impatto** | **Alto** |
| **Rischio futuro** | Una sessione Claude che non apre spontaneamente `LEGEND_CORE.md` opera senza aver letto le regole che i test chiamano «inviolabili» — fra cui il divieto di `grep` come metodo di analisi e l'obbligo di ricevuta full-text. Con agenti autonomi questo è il difetto che non lascia traccia: non fallisce, produce lavoro. È anche la ragione per cui F-01 **non** si risolve puntando i test su `AGENTS.md`. |
| **Soluzione possibile** | *Proposta.* Il router può restare tale e portare comunque un blocco «prima di leggere altro» di 5–8 righe con i puntatori *e* le stringhe delle regole inviolabili — non la legge duplicata, ma il suo indirizzo verificabile. In alternativa, un meccanismo che carichi `AGENTS.md` anche nelle sessioni Claude. La prima è realizzabile senza toccare l'harness. |
| **Decisione umana richiesta** | **Sì** — architetturale |

---

### F-03 — Una suite esiste nel repository e la batteria non la esegue mai

| Campo | Contenuto |
|---|---|
| **ID** | F-03 |
| **Descrizione** | `governance/scripts/test_candidate_content_hash.py` è tracciata da git dal 2026-08-17 e non compare né in `TESTS` di `run_release_regressions.py` né in `NOT_RUN_BY_DESIGN`. Non è mai stata eseguita dalla batteria. |
| **Evidenza** | `scripts/test_release_runner_verdict.py:55`. Censimento locale ricalcolato con il modulo runner importato (non con regex): **65 suite registrate, 66 file di test tracciati, esattamente 1 mai eseguita**, 0 registrate inesistenti. Il docstring del test a `:25` nomina due precedenti identici (`test_dossier_quote_audit.py`, `test_reading_state.py`) e un terzo (`test_recapture_snippets.py`): è la quarta ricorrenza dello stesso difetto. |
| **Categoria** | `BUG_REALE` |
| **Impatto** | **Medio** |
| **Rischio futuro** | Falsa sicurezza esatta e misurabile: la batteria dichiarerebbe PASS su 65 bersagli mentre un guard scritto, verde e mai invocato non protegge nulla. `TESTS` è una tupla letterale a manutenzione manuale — il difetto si ripresenterà a ogni nuova suite finché la registrazione resta un atto di memoria. |
| **Soluzione possibile** | *Proposta.* Due opzioni: (a) registrare la suite mancante — chiude questo caso, non la classe; (b) derivare `TESTS` dallo stesso `git ls-files` che il test già usa, riducendo la tupla letterale a un elenco di **esclusioni motivate** (`NOT_RUN_BY_DESIGN`), che è già presente e vuota. (b) è l'unica che chiude la classe. Nota: l'ordine di esecuzione oggi è deterministico e leggibile; una derivazione automatica deve preservarlo (ordinamento esplicito). |
| **Decisione umana richiesta** | **No** per (a) · **Sì** per (b) — tecnica delegabile con un vincolo dichiarato |

---

### F-04 — Quattro entrypoint con shebang sono committati non eseguibili

| Campo | Contenuto |
|---|---|
| **ID** | F-04 |
| **Descrizione** | Quattro file `.py` che iniziano con `#!` hanno modo `100644` nell'albero git invece di `100755`. Non sono avviabili come `./<script>.py`. |
| **Evidenza** | `scripts/test_release_surface.py:334`. Verificato in locale su `788c357` con `git ls-tree` e su disco con `stat`: `framework/scripts/lease_state.py`, `governance/scripts/candidate_content_hash.py`, `governance/scripts/governance_fingerprint.py`, `governance/scripts/test_candidate_content_hash.py` — tutti `disk=644 git=100644`, con `core.fileMode=true`. Sweep esaustivo su tutti i `.py` tracciati a modo `100644` con shebang: **esattamente questi 4, nessun altro**. |
| **Categoria** | `BUG_REALE` |
| **Impatto** | **Basso** in esecuzione (`python3 file.py` funziona), **medio** in convenzione |
| **Rischio futuro** | `CLAUDE.md` §3 documenta `python3 governance/scripts/governance_fingerprint.py compose --all` come check eseguibile, quindi l'uso documentato regge. Il rischio è un altro: la stessa svista si ripete a ogni file nuovo, e il guard che la rileva gira solo in CI — che in questa repository non girava. |
| **Soluzione possibile** | *Proposta.* `git update-index --chmod=+x` sui 4 file. È l'unico finding con una correzione meccanica priva di ambiguità. Va accoppiato a F-05, altrimenti si richiude un caso e non la classe. |
| **Decisione umana richiesta** | **No** — tecnica delegabile |

---

### F-05 — Nessun controllo del bit di esecuzione al momento della creazione

| Campo | Contenuto |
|---|---|
| **ID** | F-05 |
| **Descrizione** | Il repository possiede un guard sul bit di esecuzione (`test_release_surface.py`) e persino una batteria di mutation testing che verifica che quel guard morda (`scripts/guard_mutation_battery.py:200`, mutazione «executable bit stripped»). Non possiede nulla che **imposti** il bit quando il file nasce. Il guard è interamente a valle, e a valle in questa repository significava «mai». |
| **Evidenza** | Nessun hook in `.claude/hooks/` (directory inesistente nel repository). Nessuna occorrenza di `chmod +x` o `0o755` nelle convenzioni di `framework/protocols/` o in `framework/scripts/test_record_conventions.py`. I 4 file di F-04 sono nati il 2026-08-16, 08-17 e 08-18, tutti dopo l'ultimo run verde. |
| **Categoria** | `DEBITO_ARCHITETTURALE` |
| **Impatto** | **Medio** |
| **Rischio futuro** | Il guard misura la cosa giusta nel momento sbagliato. Ogni finestra senza CI accumula silenziosamente il difetto, e la correzione arriva sempre in blocco come oggi — quattro file insieme, tre settimane dopo. |
| **Soluzione possibile** | *Proposta.* Un hook `PostToolUse` locale che imposti `+x` quando un file scritto inizia con `#!`, oppure un pre-commit che rifiuti il modo `100644` su un file con shebang. Non richiede modifiche a GitHub Actions. |
| **Decisione umana richiesta** | **No** — tecnica delegabile |

---

### F-06 — `test_figure_ppi_preflight.py` fallisce invece di degradare

| Campo | Contenuto |
|---|---|
| **ID** | F-06 |
| **Descrizione** | La suite importa `fitz` (PyMuPDF) a livello di modulo, senza guardia. In un ambiente senza PyMuPDF non salta: va in `ModuleNotFoundError`, esce 1 e la batteria la conta come fallimento. Cinque consumatori di `fitz` su sei usano import differito, commentato esplicitamente come «optional dependency». Questo è l'unico sito che se ne discosta — insieme al modulo che testa. |
| **Evidenza** | Log CI: `framework/scripts/test_figure_ppi_preflight.py`, `line 10, in <module>: import fitz` → `ModuleNotFoundError`. Censimento locale dei 6 consumatori: `benchmark_input_surface.py:1007`, `regenerate_adjudications.py:175`, `surface_census.py:253`, `deepdive_manifest.py:613` importano dentro funzione con commento «optional dependency»; `test_deepdive_manifest.py:1027-1029` usa `try/except ImportError → skipTest("PyMuPDF unavailable")`; `figure_ppi_preflight.py:16` e il suo test importano a livello di modulo. |
| **Categoria** | `ENVIRONMENT_PROBLEM` |
| **Impatto** | **Medio** |
| **Rischio futuro** | Finché resta così, ogni ambiente senza PyMuPDF vede un rosso che non riguarda il contenuto. È la forma di rumore che porta a disattivare una suite, e la suite disattivata è quella che sorveglia la risoluzione delle figure — cioè la profondità di lettura. |
| **Soluzione possibile** | *Proposta.* Applicare al sito mancante il pattern già scritto tre righe più in là in `test_deepdive_manifest.py`: `try: import fitz / except ImportError: raise unittest.SkipTest("PyMuPDF unavailable")` a livello di modulo. Nessuna nuova invenzione: applicazione uniforme di una convenzione esistente. |
| **Decisione umana richiesta** | **No** — tecnica delegabile |

---

### F-07 — PyMuPDF non è dichiarata fra le dipendenze

| Campo | Contenuto |
|---|---|
| **ID** | F-07 |
| **Descrizione** | `requirements-analysis.txt` contiene una sola riga: `numpy==2.0.2`. PyMuPDF non è dichiarata da nessuna parte, benché sia documentata come strumento portante della lettura PDF («PDF text via PyMuPDF 1.26.5» in `surface_census.md`, e ricorrente nei dossier full-text). L'ambiente che il CI costruisce non può quindi esercitare l'intera superficie PDF. |
| **Evidenza** | `cat requirements-analysis.txt` → 2 righe di cui 1 commento. Nessun match per `pymupdf` in alcun file `requirements*.txt`. Nel run: **13 test saltati** in `test_deepdive_manifest.py` con motivo `'PyMuPDF unavailable'` — su 19 skip totali dichiarati dalle suite. |
| **Categoria** | `ENVIRONMENT_PROBLEM` |
| **Impatto** | **Medio-alto** |
| **Rischio futuro** | Anche risolta F-06, questi 13 controlli continuerebbero a saltare. Un run verde certificherebbe una superficie probatoria che non è mai stata toccata — proprio quella che decide se un PDF è leggibile e se una citazione è verificabile. |
| **Soluzione possibile** | *Proposta.* Dichiarare PyMuPDF (pin esplicito, es. la versione già citata nel censimento) in un `requirements-dev.txt` separato da `requirements-analysis.txt`, e installarlo nello step CI. Decisione collegata: se PyMuPDF sia opzionale (allora gli skip vanno resi visibili, F-11) o obbligatoria (allora l'assenza deve essere un errore, non uno skip). |
| **Decisione umana richiesta** | **Sì** — architetturale (opzionale vs obbligatoria) |

---

### F-08 — `fetch-depth: 1` è incompatibile con il verificatore del freeze DisMech

| Campo | Contenuto |
|---|---|
| **ID** | F-08 |
| **Descrizione** | Il workflow fa checkout superficiale. `verify_phase2_baseline()` risolve `git_head_at_freeze` = `8ca2712` (2026-08-04) e poi confronta ogni artefatto sigillato contro `git cat-file` a quel commit. In un clone di profondità 1 quel commit non esiste: 14 errori in un colpo. |
| **Evidenza** | `.github/workflows/public-release-gate.yml`: `fetch-depth: 1`. `dismech_independent_protocol.py:226` produce `git_head_at_freeze is not an available commit`; il ciclo a `:268` (`if verify_git and freeze:`) produce un errore per ciascun artefatto. Aritmetica confermata: `dismech_phase2_baseline.json` dichiara **12 input + 1 output = 13 artefatti**, più l'errore sul commit = **14**, esattamente quanti il test ne riporta. Distanza verificata: `8ca2712` è **415 commit** dietro `788c357`. |
| **Categoria** | `WORKFLOW_PROBLEM` |
| **Impatto** | **Alto** |
| **Rischio futuro** | È l'unico verificatore del freeze DisMech, cioè della catena che sostiene l'export. Finché fallisce per ragioni ambientali non può segnalare una violazione vera: un sigillo realmente rotto arriverebbe come il quindicesimo errore in una lista che nessuno legge più. |
| **Soluzione possibile** | *Proposta.* Tre opzioni, ordinate per costo crescente: (a) `fetch-depth: 0` — corretto e immediato, costa banda a ogni run e cresce con la storia; (b) `fetch-depth: 0` solo per un job dedicato al freeze, lasciando superficiale la batteria; (c) rilevare la superficialità e degradare (F-09). (c) è quella che risolve il problema anche fuori dal CI; (a) è quella che rende il verificatore realmente attivo. Le due sono complementari, non alternative. |
| **Decisione umana richiesta** | **Sì** — architetturale (quale delle tre, o quali due) |

---

### F-09 — Il contratto di degradazione esiste ma non conosce lo stato «git superficiale»

| Campo | Contenuto |
|---|---|
| **ID** | F-09 |
| **Descrizione** | Il repository ha già progettato, scritto e testato il contratto giusto: «una verifica ancorata a git che non può girare va **riportata come non eseguita**, non ripiegata in un PASS pulito». Funziona per il caso *git assente* (archivio sorgente). Non conosce il terzo stato: **git presente ma storia troncata**. Nello stesso run e nella stessa classe di test, un test salta correttamente e l'altro fallisce duro, per la stessa identica causa. |
| **Evidenza** | `test_dismech_independent_protocol.py`: `test_two_file_reseal_disagrees_with_pinned_git_tree` → `skipped "sealed blob ... unavailable: git blob unavailable: 8ca2712..."` (intercetta l'eccezione); `test_current_phase2_baseline_verifies` → FAIL (chiama `verify_phase2_baseline()`, che **restituisce** errori invece di sollevarli). Il contratto è enunciato in `scripts/test_release_runner_verdict.py:112-117` e implementato dal runner con il verdetto `PASS WITH SKIPS` (`run_release_regressions.py:100-107`). L'interruttore esiste già nell'API: `verify_phase2_baseline(..., verify_git: bool = True)` — nessun chiamante lo usa. Il rilevatore meccanico esiste in git: `git rev-parse --is-shallow-repository`. |
| **Categoria** | `DEBITO_ARCHITETTURALE` |
| **Impatto** | **Medio-alto** |
| **Rischio futuro** | Ogni futuro ambiente con clone superficiale (CI, container, worktree esportati) riprodurrà lo stesso rosso non informativo. E ogni futuro guard ancorato a git erediterà lo stesso punto cieco, perché la distinzione da fare non è codificata da nessuna parte. |
| **Soluzione possibile** | *Proposta.* Rendere la condizione di ancoraggio a tre stati anziché due — *completo* / *superficiale* / *assente* — con `--is-shallow-repository` come discriminante, e far degradare a `skipTest` con motivo esplicito («shallow clone: freeze verification unavailable») nello stato intermedio. È l'estensione di un contratto già accettato, non un contratto nuovo. Il commento a `test_release_runner_verdict.py:112` autorizza esplicitamente la crescita del numero di skip di questo tipo. |
| **Decisione umana richiesta** | **No** sull'estensione del contratto · **Sì** sul suo confine (vedi F-11) |

---

### F-10 — Il workflow gira in modo `release` su ogni push di una repository di sviluppo

| Campo | Contenuto |
|---|---|
| **ID** | F-10 |
| **Descrizione** | `on: push` senza filtro di branch o percorso; step `Regression tests` senza selezione; gate invocato con `--mode release`. `public_release_gate.py` espone `--mode` con `choices=("staging", "release", "clone")`: non esiste un modo pensato per lo sviluppo continuo. |
| **Evidenza** | `.github/workflows/public-release-gate.yml` (43 righe, unico file in `.github/`): `on: push / pull_request / workflow_dispatch`; `--mode release`. `scripts/public_release_gate.py:939`: `"--mode", choices=("staging","release","clone"), default="staging"`. `:873`: «Final release review must run from a clean committed tree». Il workflow risale a `a2e0dd0`, il commit di apertura dell'edizione pubblica, e non è mai stato rivisto. |
| **Categoria** | `DEVELOPMENT_SCOPE_MISMATCH` |
| **Impatto** | **Medio** |
| **Rischio futuro** | Costo fisso di ~3 minuti per push su una repository ad aggiornamento frequente, e un verdetto che mescola due domande distinte: «questo commit è sano?» e «questo stato è pubblicabile?». Mescolate, la seconda rende rumorosa la prima e la prima rende ottimistica la seconda. |
| **Soluzione possibile** | *Proposta.* Opzioni in §3. La direzione raccomandata è **due gate distinti sullo stesso corpo di test**, non due batterie diverse: un `development gate` che gira sempre e un `release gate` che gira su tag/branch di release o su `workflow_dispatch`. |
| **Decisione umana richiesta** | **Sì** — architetturale |

---

### F-11 — Nessuna soglia sugli skip: un PASS può nascondere qualsiasi quantità di non-eseguito

| Campo | Contenuto |
|---|---|
| **ID** | F-11 |
| **Descrizione** | Il runner distingue correttamente `PASS` da `PASS WITH SKIPS` e nomina ogni skip col suo motivo — progettazione buona. Non esiste però alcun massimo, né alcuna distinzione fra skip attesi e skip che segnalano un ambiente incompleto. |
| **Evidenza** | Censimento completo degli skip del run (denominatore: 19 skip dichiarati dalle suite, sommati da `skipped=N`): **13** `'PyMuPDF unavailable'` · **4** `'local full-text corpus is gitignored and absent from this checkout'` · **1** `'local full-text corpus not present in this checkout'` · **1** `"sealed blob ... unavailable"`. I 5 sul corpus sono per progetto; i 14 restanti sono deficienze d'ambiente (F-07, F-08). `run_release_regressions.py:100-107` formatta il verdetto senza confrontarlo con alcuna soglia. |
| **Categoria** | `DEBITO_ARCHITETTURALE` |
| **Impatto** | **Medio** |
| **Rischio futuro** | È il rischio che si materializza **dopo** aver risolto tutto il resto: la prima batteria verde dirà `PASS WITH SKIPS (65 targets, 19 skipped)` e verrà letta come «verde». 14 di quei 19 significano «questo ambiente non ha potuto verificare la superficie PDF né il sigillo DisMech». |
| **Soluzione possibile** | *Proposta.* Dichiarare per ogni motivo di skip se è **atteso** (corpus gitignored) o **degradazione d'ambiente**, e far fallire il gate — o almeno emettere un avviso distinto — quando la seconda categoria è non vuota in un contesto che pretende di verificare tutto. Il meccanismo per riportarlo esiste già; manca solo il giudizio. |
| **Decisione umana richiesta** | **Sì** — architetturale (dove passa il confine) |

---

### F-12 — 455 commit in 22 giorni senza alcun gate

| Campo | Contenuto |
|---|---|
| **ID** | F-12 |
| **Descrizione** | L'ultimo run verde dello stesso workflow è del 2026-08-01 sulla repository stabile. Da allora a `788c357` ci sono 455 commit e nessuna esecuzione. Tutte e quattro le cause radice sono nate in quella finestra. Non esisteva un gate di sviluppo perché non esisteva una repository di sviluppo con CI. |
| **Evidenza** | `wwox-rare-disease-legend`: 4 run, **4 successi**, ultimo `30691910733` del 2026-08-01T08:30Z. `legend-development`: creata 2026-08-23T20:47Z, `total_count: 1`, quel run. `git rev-list --count 8ab8e4b..788c357` = **455**. Date d'introduzione delle cause radice: tabella in §1. |
| **Categoria** | `DEVELOPMENT_SCOPE_MISMATCH` |
| **Impatto** | **Alto** |
| **Rischio futuro** | Se la risposta a questo run fosse restringere il gate, la finestra cieca si riaprirebbe con una copertura formale a giustificarla. Il tasso osservato è **4 difetti reali di contenuto in 22 giorni** (F-02, F-03, F-04 e le loro classi): non è un tasso che tollera altre tre settimane senza controlli. |
| **Soluzione possibile** | *Proposta.* Trattare questo run come il **baseline di bootstrap**, non come una regressione: registrarne il contenuto, poi far valere il ratchet da lì in avanti. È il metodo che il repository già usa altrove (`growth_anchors.py`, i baseline con soglia che può solo migliorare). |
| **Decisione umana richiesta** | **Sì** — governance |

---

### F-13 — La migrazione di `CLAUDE.md` è su `main`, il suo record di evidenza è ancora `PROPOSED`

| Campo | Contenuto |
|---|---|
| **ID** | F-13 |
| **Descrizione** | `governance/design_records/claude_md_migration_map.md` dichiara `status: PROPOSED — part of INTEGRATION_CANDIDATE v3.1.1, subject to Mirror hostile review`. La migrazione che documenta è però già applicata su `main` da `04cbd3b`. Il record afferma «the transformation lost nothing»: l'audit conferma la metà verificabile (nessuna regola persa dalle sedi normative) e trova non coperta l'altra metà (le 4 suite e l'asimmetria di caricamento di F-02). |
| **Evidenza** | Frontmatter del record, `authored_by: plan`, `authored_on: 2026-08-16`. 21 voci nell'inventario, **tutte** `REPLACED_BY_EQUIVALENT`, nessuna `PRESERVED` né `UNRESOLVED`. `04cbd3b` è antenato di `788c357`. Nessuna delle 21 voci menziona le suite che asseriscono la presenza dei token in `CLAUDE.md`. |
| **Categoria** | `DEBITO_ARCHITETTURALE` |
| **Impatto** | **Medio** |
| **Rischio futuro** | Un inventario che cerca le regole solo nella prosa non vede quelle codificate nei test. La prossima migrazione ripeterà lo stesso taglio con la stessa metodologia e produrrà lo stesso rosso. |
| **Soluzione possibile** | *Proposta.* Estendere il metodo di inventario: prima di rimuovere una stringa da una superficie normativa, cercarla anche nella batteria di test (`grep` sul solo elenco `TESTS`). Costa secondi e avrebbe intercettato tutti e 5 i token. |
| **Decisione umana richiesta** | **Sì** — governance (chi chiude la Mirror hostile review, e se il record va aggiornato o riaperto) |

---

### F-14 — Le action del workflow puntano a Node.js 20 (deprecato)

| Campo | Contenuto |
|---|---|
| **ID** | F-14 |
| **Descrizione** | Tre action del workflow dichiarano Node.js 20 e vengono forzate su Node 24 dal runner. Annotazione, non errore. |
| **Evidenza** | Annotazione del run: `actions/checkout@11bd719`, `actions/setup-python@a26af69`, `actions/upload-artifact@ea165f8`. Nota positiva: sono **tutte pinnate a SHA di commit**, e `test_release_surface.py::test_github_actions_are_pinned_to_commit_shas` è passato. |
| **Categoria** | `WORKFLOW_PROBLEM` |
| **Impatto** | **Basso** |
| **Rischio futuro** | Alla rimozione di Node 20 dai runner il workflow smette di partire, e lo farà nel momento meno scelto. |
| **Soluzione possibile** | *Proposta.* Aggiornare i tre pin a versioni su Node 24, mantenendo il pinning a SHA. Da fare in un cambio isolato e verificabile, mai insieme a una correzione di contenuto. |
| **Decisione umana richiesta** | **No** — tecnica delegabile |

---

### F-15 — `legend-development` è pubblica, senza protezione del branch, con action non vincolate

| Campo | Contenuto |
|---|---|
| **ID** | F-15 |
| **Descrizione** | Configurazione osservata della repository dove «agenti lavorano autonomamente»: `visibility: public`, `fork: false`, `main` senza branch protection, `allowed_actions: all`, `sha_pinning_required: false`. |
| **Evidenza** | `gh api repos/<operator-account>/legend-development` → `{"visibility":"public","fork":false,"archived":false}`. `.../branches/main/protection` → HTTP 404 «Branch not protected». `.../actions/permissions` → `{"enabled":true,"allowed_actions":"all","sha_pinning_required":false}`. |
| **Categoria** | `DEBITO_ARCHITETTURALE` |
| **Impatto** | **Medio** |
| **Rischio futuro** | Lo sviluppo continuo di un modello di malattia è visibile pubblicamente prima di passare il gate di pubblicazione — che è precisamente ciò che il gate esiste per evitare. `allowed_actions: all` con `sha_pinning_required: false` significa che il pinning oggi presente nel workflow è una convenzione, non un vincolo: nulla impedisce a una futura modifica di introdurre una action non pinnata. |
| **Soluzione possibile** | *Proposta.* Valutare `private` per l'ambiente di sviluppo continuo; attivare `sha_pinning_required` per rendere vincolo ciò che il test già verifica; valutare la protezione di `main` in funzione del numero di agenti che vi scrivono. Nessuna di queste è tecnica: sono scelte sul rischio accettato. |
| **Decisione umana richiesta** | **Sì** — governance |

---

## 3 · Development repository vs stable repository

### Il dato che precede ogni opzione

Lo stesso workflow è **verde 4/4 sulla repository stabile** e rosso al primo run su
`legend-development`. La differenza fra i due esiti non è l'ambiente: è **455 commit** di
sviluppo che nessun gate ha visto. Ciò significa che la domanda «il Public Release Gate deve
girare sempre?» è posta al livello sbagliato. La domanda che il dato impone è:

> Quale sottoinsieme di proprietà deve valere **a ogni commit** di sviluppo, e quale può valere
> **solo alla pubblicazione**?

L'audit ha esaminato le 8 suite fallite contro questa domanda. Il risultato è netto:

| Suite fallita | Proprietà verificata | Deve valere in development? |
|---|---|---|
| `test_release_runner_verdict.py` | ogni test scritto viene eseguito | **Sì** — è il presupposto di ogni altra verifica |
| `test_release_surface.py` | gli entrypoint sono avviabili | **Sì** — un agente li invoca |
| `test_locator_obligation...` | l'obbligo dei locator raggiunge la superficie di avvio | **Sì** — è disciplina di lettura |
| `test_abstract_corpus_is_not_evidence.py` | un abstract non è una lettura | **Sì** — è disciplina probatoria |
| `test_fulltext_trace_contract.py` | nessuna lettura è senza memoria | **Sì** — è disciplina probatoria |
| `test_session_self_eval.py` | l'autodiagnosi è cablata prima dei takeaway | **Sì** — è disciplina di sessione |
| `test_figure_ppi_preflight.py` | la risoluzione delle figure è misurata | **Sì**, se l'ambiente lo consente |
| `test_dismech_independent_protocol.py` | il sigillo DisMech regge | **Sì** — protegge un export |

**Nessuna delle 8 è specifica della pubblicazione.** Il criterio non è «release vs
development»: è **igiene e disciplina** (sempre) contro **superficie di pubblicazione** (solo
alla release). Le proprietà genuinamente di pubblicazione — scansione privacy, assenza di
linkage individuale, esecuzione da un albero pulito, coerenza README — stanno tutte in
`public_release_gate.py`, che oggi **passa**.

### Le quattro opzioni

Presentate senza scelta. La raccomandazione dell'audit è indicata ma non decide.

**Opzione 1 — Lasciare tutto com'è.**
Il gate gira sempre, in modo `release`, su ogni push.
*A favore:* zero lavoro; nessuna finestra cieca; una sola verità.
*Contro:* ~3 min per push; il verdetto mescola due domande; il rumore d'ambiente (F-06, F-08)
addestra a ignorare il rosso — che è il modo in cui una batteria muore.

**Opzione 2 — Adattare il gate esistente con un quarto modo.**
Aggiungere `--mode development` a `public_release_gate.py`, che salta i soli controlli
propriamente di pubblicazione.
*A favore:* un solo strumento, una sola manutenzione; il modo dice esplicitamente cosa non è
stato controllato.
*Contro:* tocca il gate, che è il componente che si vorrebbe più stabile; e un modo che «salta
qualcosa» tende ad allargarsi.

**Opzione 3 — Due workflow distinti sullo stesso corpo di test** *(raccomandata)*.
`development-gate.yml`: `on: push`, batteria completa, `fetch-depth: 0`, dipendenze complete,
**senza** `--mode release`.
`release-gate.yml`: `on: workflow_dispatch` + tag di release, tutto quanto sopra **più**
`public_release_gate.py --mode release`.
*A favore:* separa le due domande senza indebolire nessuna delle due; la batteria resta una
sola, quindi non può divergere; risolve F-08 e F-10 nel punto giusto.
*Contro:* due file da mantenere allineati; richiede una convenzione esplicita su cosa sia un
«release point».

**Opzione 4 — Development gate ridotto + release gate completo.**
Solo un sottoinsieme «veloce» a ogni push, batteria completa alla release.
*A favore:* il più economico per push.
*Contro:* **è la ricostruzione del difetto che stiamo analizzando.** F-12 mostra che una
finestra senza copertura completa produce ~4 difetti reali in 22 giorni. Un sottoinsieme
ridotto è una finestra più stretta, non chiusa. L'audit la sconsiglia esplicitamente.

### Separazione development/stable: mantenerla

Sì, e il dato la sostiene: la repository stabile è ferma dal 2026-08-01 ed è verde; quella di
sviluppo è a 455 commit e ha 4 difetti reali. La separazione ha **funzionato** — ha impedito
che 455 commit non verificati raggiungessero il punto di pubblicazione.

Ciò che manca non è la separazione: è il **ratchet** in mezzo. Oggi passare da development a
stable è un `git push`; dovrebbe essere il momento in cui il gate di release gira per la prima
volta con esito vincolante. La configurazione osservata in F-15 (`main` non protetto,
repository pubblica) non implementa ancora questa separazione a livello di piattaforma.

---

## 4 · Analisi dei quattro failure principali

### A · `CLAUDE.md` / `AGENTS.md`

**I test cercano nel posto corretto?**

*Cercano la cosa giusta, all'indirizzo giusto, per la ragione giusta — e la migrazione ha
svuotato l'indirizzo senza spostare il destinatario.*

La proprietà difesa è enunciata nel docstring stesso del test:
«CLAUDE.md is read at the start of every session; a rule absent there is optional.»
Questa premessa **è ancora vera per le sessioni Claude** ed è verificabile direttamente: il
contesto di questa sessione riceve `CLAUDE.md` come istruzioni di progetto; non riceve
`AGENTS.md`. `AGENTS.md` si autodescrive come «entry point for Codex and compatible agentic
tooling».

Quindi la migrazione non ha soltanto spostato prosa fra due file equivalenti: ha spostato le
regole inviolabili **dalla superficie auto-caricata per Claude a quella auto-caricata per
Codex** (F-02). Il test rosso sta segnalando questo, in modo indiretto e con un messaggio
fuorviante.

**La migrazione rende i test obsoleti?**

**No — e questa è la conclusione centrale dell'audit.** La categoria `TEST_OBSOLETO` è stata
considerata per tutti e 5 i fallimenti e respinta per tutti e 5:

- un test obsoleto misura una proprietà che ha smesso di contare. Qui la proprietà conta
  ancora — anzi conta di più, perché il numero di agenti autonomi è cresciuto;
- l'indirizzo `CLAUDE.md` non è morto: è tuttora l'unico file auto-caricato nelle sessioni
  Claude;
- il test non è stato invalidato da una decisione che lo consideri. La migration map (21 voci,
  tutte `REPLACED_BY_EQUIVALENT`) inventaria **la prosa** e mai la batteria di test. Nessuna
  delle 21 voci nomina questi 5 token come rimossi con conseguenze note (F-13).

Marcarli obsoleti e riscriverli su `AGENTS.md` produrrebbe un verde e lascerebbe le sessioni
Claude senza le regole inviolabili sulla superficie che leggono. Sarebbe esattamente
«ottimizzare per avere un workflow verde».

**Qual è la soluzione corretta?**

Tre opzioni. Sono mutuamente esclusive e la scelta è di governance.

| | Opzione | Cosa comporta | Costo del difetto residuo |
|---|---|---|---|
| **1** | **Modificare i test** — puntarli su `AGENTS.md` e sulle sedi normative | Verde immediato; coerente con governance v3.1.1 §0.3 | Non chiude F-02: le sessioni Claude restano senza le regole sulla superficie che leggono |
| **2** | **Modificare la documentazione** — riportare i 5 token in `CLAUDE.md` | Chiude F-01 e F-02 insieme | Contraddice frontalmente il principio del router, appena adottato e documentato |
| **3** | **Duplicazione intenzionale, dichiarata e minima** *(raccomandata)* | Un registro esplicito delle «superfici di avvio sessione» (`CLAUDE.md`, `AGENTS.md`, ed eventuali future), con l'elenco delle stringhe che devono raggiungerle tutte. I test si parametrizzano su quel registro invece di cablare i nomi dei file. `CLAUDE.md` porta un blocco breve — puntatori più le stringhe delle regole inviolabili, non la legge duplicata | Richiede di ammettere che il router non può essere *puro*: deve portare il minimo che rende la legge raggiungibile da chi lo legge per primo |

L'opzione 3 è raccomandata per una ragione strutturale: è l'unica che sopravvive alla
**prossima** migrazione. Le opzioni 1 e 2 riparano l'istanza; la 3 codifica dove va cercata la
risposta, così che il prossimo spostamento di superficie fallisca in modo leggibile invece di
lasciare 4 suite rosse con messaggi che parlano di token e non di superfici.

Nota di merito, non trascurabile: nell'opzione 3 il testo del router deve dire *che cosa* è
inviolabile e *dove* sta, non ripeterne il contenuto. Il rischio che il repository teme —
«two parallel normative files drift», scritto in `AGENTS.md` — resta reale e va limitato a un
elenco di puntatori verificabili meccanicamente.

---

### B · Suite non registrate

**Esistono test presenti ma non eseguiti?**

Sì. Uno, e conosciuto con precisione: **65 suite registrate, 66 file di test tracciati, 1 mai
eseguita** — `governance/scripts/test_candidate_content_hash.py`, dal 2026-08-17.
(Censimento rifatto in locale importando il modulo runner, non con espressione regolare: la
lettura per regex dava 67 perché due voci di `TESTS` sono scritte come letterali stringa
concatenati implicitamente su due righe. Il numero corretto è 65.)

**Rischio di falsa sicurezza**

È il rischio più insidioso dei quattro, perché **non produce rosso**. Una batteria che dichiara
PASS su 65 bersagli mentre un guard scritto, verde e mai invocato non protegge nulla, è peggio
di una batteria assente: crea affidamento.

Il repository lo sa già. Il docstring del test elenca i precedenti: `test_dossier_quote_audit.py`
e `test_reading_state.py` («reported PASS over 57 targets while ignoring them»), poi
`test_recapture_snippets.py`, sfuggito perché la prima versione del guard usava un
`git ls-files` nudo che non vede i file non committati. **Questa è la quarta ricorrenza**, e il
guard ha funzionato: ha trovato la quarta. Ciò che non ha cambiato è la causa.

**Come dovrebbe essere mantenuta la batteria**

La causa è che `TESTS` è una tupla letterale a manutenzione manuale: una suite nuova è
verificata solo se il suo autore si ricorda di registrarla. Il guard sposta il difetto da
«silenzioso» a «rumoroso», che è un progresso reale ma non una chiusura.

*Proposta.* Invertire il default: derivare l'elenco dallo stesso `git ls-files --cached --others
--exclude-standard "*test_*.py"` che il guard già esegue, e ridurre la manutenzione manuale a un
elenco di **esclusioni motivate** — `NOT_RUN_BY_DESIGN`, che esiste già ed è oggi vuoto. Una
suite nuova sarebbe eseguita per costruzione; escluderla richiederebbe di scriverne la ragione.

Due vincoli che la proposta deve rispettare, entrambi già presenti nel codice attuale:
l'ordine di esecuzione oggi è deterministico e leggibile (va preservato con un ordinamento
esplicito), e il guard deve continuare a vedere i file **non ancora committati**, che è
precisamente il momento in cui serve.

---

### C · Permessi e bit di esecuzione

**Il problema è reale?**

Sì, ed è verificato indipendentemente dal CI. I quattro file hanno modo `100644` **nell'albero
git a `788c357`** e `644` sul filesystem locale, con `core.fileMode=true`. Non è un artefatto
del runner: il checkout ripristina il modo dall'indice, quindi il difetto viaggia con il
commit. Sweep esaustivo su tutti i `.py` tracciati: esattamente 4, nessun altro.

L'impatto operativo è contenuto — `CLAUDE.md` §3 documenta l'invocazione come
`python3 <path>`, che funziona. Ma un file con shebang dichiara di essere avviabile
direttamente; se non lo è, la dichiarazione è falsa e un agente che la crede perde un ciclo.

**Deriva dal processo di commit?**

Sì. I quattro file sono nati il 2026-08-16, 08-17 e 08-18 — tutti dentro la finestra senza CI.
Il repository possiede un guard (`test_release_surface.py:334`) e persino una batteria di
mutation testing che verifica che quel guard morda quando il bit viene rimosso
(`guard_mutation_battery.py:200`, «executable bit stripped»). Il guard è corretto e il suo
test è corretto: entrambi girano **a valle**, e a valle qui significava «mai».

**Esiste un controllo automatico mancante?**

Sì, ed è a monte: nulla imposta `+x` quando il file nasce. Nessun hook in `.claude/hooks/`
(la directory non esiste nel repository), nessuna convenzione su `chmod` in
`framework/protocols/` o in `record_conventions.py`.

*Proposta.* Un hook `PostToolUse` locale che imposti il bit quando un file scritto inizia con
`#!`, oppure un pre-commit che rifiuti il modo `100644` su un file con shebang. Entrambi
agiscono nel momento in cui l'informazione è disponibile e la correzione costa zero. Nessuna
modifica a GitHub Actions.

---

### D · Dipendenze d'ambiente

**PyMuPDF / `fitz`**

Due difetti distinti che vanno separati, perché la correzione dell'uno lascia intatto l'altro.

1. *Il test non degrada* (F-06). `test_figure_ppi_preflight.py:10` importa `fitz` a livello di
   modulo. Cinque consumatori su sei nel repository importano `fitz` **dentro le funzioni**,
   con il commento esplicito «optional dependency»; `test_deepdive_manifest.py:1027-1029` usa
   `try/except ImportError → skipTest("PyMuPDF unavailable")`. La convenzione è scritta, è
   documentata nel codice, ed è applicata ovunque tranne che in questo sito. È il difetto che
   questo repository nomina di continuo: *pattern risolto in un sito e non portato al
   successivo*.

2. *La dipendenza non è dichiarata* (F-07). `requirements-analysis.txt` contiene solo
   `numpy==2.0.2`. Anche con la guardia a posto, il CI salterebbe **13 controlli**
   (`'PyMuPDF unavailable'`, contati sul log) e la superficie PDF non verrebbe mai esercitata —
   proprio quella che decide se un documento è leggibile e se una citazione è verificabile.

*Decisione a monte, che va presa prima di correggere:* PyMuPDF è **opzionale** o
**obbligatoria** per l'ambiente di sviluppo? Se opzionale, gli skip vanno resi visibili e
contati (F-11). Se obbligatoria, la sua assenza deve essere un errore, non uno skip, e va
dichiarata e pinnata.

**Shallow clone e `fetch-depth`**

`fetch-depth: 1` produce un clone senza storia. `verify_phase2_baseline()` risolve un commit di
freeze **415 commit** indietro e poi confronta 13 artefatti sigillati contro quel commit:
1 + 13 = **14 errori**, esattamente quanti il test riporta.

La cosa importante non è il numero: è che **il contratto di degradazione giusto esiste già in
questo repository, scritto e testato**. `test_release_runner_verdict.py:112-117` lo enuncia:

> «The property under test is that a git-anchored verification which cannot run is REPORTED as
> unrun, not folded into a clean PASS.»

E funziona — per il caso *git assente* (archivio sorgente estratto). Il punto cieco è il terzo
stato: **git presente, storia troncata**. Nello stesso run, nella stessa classe di test:
`test_two_file_reseal_disagrees_with_pinned_git_tree` **salta** correttamente (intercetta
l'eccezione), `test_current_phase2_baseline_verifies` **fallisce duro** — perché
`verify_phase2_baseline` *restituisce* una lista di errori invece di sollevarli.

**Test che falliscono invece di degradare: la valutazione**

Un test che fallisce quando l'ambiente non gli consente di misurare non sta misurando il
sistema: sta misurando il runner. Ma la degradazione ha un costo speculare, ed è il costo che
il repository ha già scelto di pagare a metà: uno skip non contato è un PASS che mente.

L'audit propone di trattare le due cose come una sola decisione, non due:

- **estendere il contratto a tre stati** — `completo` / `superficiale` / `assente` — con
  `git rev-parse --is-shallow-repository` come discriminante meccanico, e degradare a
  `skipTest("shallow clone: freeze verification unavailable")` nello stato intermedio (F-09).
  L'interruttore esiste già nell'API: `verify_phase2_baseline(..., verify_git=False)`, che oggi
  nessun chiamante attiva;
- **e contestualmente** dare agli skip un confine (F-11): distinguere gli skip *attesi*
  (i 5 sul corpus full-text, gitignored per progetto) dagli skip di *degradazione d'ambiente*
  (i 14 restanti), e non lasciare che i secondi si sommino silenziosamente in un PASS.

Fatta solo la prima, il run diventa verde con 15 skip invece di 8 fallimenti, e il sigillo
DisMech risulta «verificato» senza esserlo mai stato. È esattamente il fallimento contro cui il
contratto era stato scritto.

---

## 5 · Ordine di intervento consigliato

Nessuno di questi interventi è autorizzato da questo mandato. È una sequenza proposta.

Il criterio di ordinamento non è la gravità: è **quale intervento rende leggibile il
successivo**. Un rosso che non si sa leggere blocca tutto ciò che verrebbe dopo.

### Priorità 1 — Affidabilità del sistema

Problemi per cui il sistema oggi **non sa dire se sta funzionando**.

| # | Intervento | Perché prima | Dipendenze | Rischio |
|---|---|---|---|---|
| 1.1 | **F-12 — Dichiarare questo run il baseline di bootstrap** | Nulla è interpretabile finché non si decide se questi 8 fallimenti sono *regressioni* (qualcuno ha rotto qualcosa) o *debito accumulato in 22 giorni ciechi* (l'evidenza dice questo). Da questa etichetta dipende il tono di ogni intervento successivo | nessuna | Basso. Il rischio è di **non** farlo: senza baseline, ogni run futuro si confronta con un ideale mai raggiunto |
| 1.2 | **F-03 — Registrare la suite mai eseguita** | È l'unico difetto che rende **non verificabili gli altri**: finché una suite può esistere senza girare, ogni PASS successivo è condizionato. Correzione a rischio quasi nullo | 1.1 per l'etichetta | Basso. La suite potrebbe rivelarsi rossa una volta eseguita: sarebbe un guadagno, non un problema |
| 1.3 | **F-08 + F-09 — Sbloccare il verificatore del freeze DisMech** | È l'unico guard sulla catena che sostiene l'export. Oggi non può segnalare una violazione vera: un sigillo rotto arriverebbe come il quindicesimo errore in una lista già ignorata | 1.2 | **Medio.** Con `fetch-depth: 0` il verificatore gira davvero per la prima volta dal 2026-08-04 e **potrebbe trovare una violazione reale**. È il rischio da correre, non da evitare: è l'informazione che 415 commit hanno reso indisponibile |
| 1.4 | **F-02 — Riportare le regole inviolabili sulla superficie auto-caricata per Claude** | Riguarda ciò che gli agenti leggono **prima** di lavorare. Ogni sessione che parte senza è lavoro da rifare, e non lascia traccia di essere stato fatto male | Decisione umana su §4A | Medio. Tocca un file appena migrato per decisione di governance: va fatto **con** quella decisione, non contro |

### Priorità 2 — Falsi positivi

Problemi che producono rosso senza dire nulla sul contenuto. Vanno dopo la P1 perché **la P1 va
letta anche attraverso il rumore**; vanno prima della P3 perché il rumore consuma l'attenzione
che la P3 richiede.

| # | Intervento | Perché qui | Dipendenze | Rischio |
|---|---|---|---|---|
| 2.1 | **F-06 — Guardia sull'import di `fitz`** | Applicazione uniforme di una convenzione già scritta tre righe più in là. Nessuna invenzione | nessuna | **Basso, ma non nullo:** se PyMuPDF venisse dichiarata obbligatoria (F-07), la guardia trasformerebbe un errore legittimo in uno skip. Fare **dopo** aver deciso F-07 |
| 2.2 | **F-07 — Dichiarare PyMuPDF, o dichiararla opzionale** | Sblocca 13 controlli oggi mai eseguiti sulla superficie PDF | Decisione umana: opzionale vs obbligatoria | Medio. Se dichiarata obbligatoria, 13 test tornano vivi e **potrebbero essere rossi**. Anche qui: è l'informazione che manca |
| 2.3 | **F-01 — Chiudere il conflitto sui 5 token** | Toglie 5 fallimenti dalla lettura di ogni run futuro. Va **dopo** 1.4 perché la decisione architetturale (dove vivono le regole inviolabili) precede la sua meccanizzazione nei test | 1.4 | Medio. L'opzione 1 di §4A dà verde immediato e lascia aperto F-02: è la scorciatoia da riconoscere come tale |
| 2.4 | **F-04 — Correggere i 4 bit di esecuzione** | Meccanica, non ambigua, senza dipendenze | nessuna | Nullo |
| 2.5 | **F-14 — Aggiornare i pin delle action a Node 24** | Rimuove un'annotazione ricorrente e previene un'interruzione a tempo scelto da altri | nessuna | Basso. Da fare **isolato**: mai insieme a una correzione di contenuto, o si perde quale delle due ha cambiato l'esito |

### Priorità 3 — Miglioramenti architetturali

Problemi la cui correzione chiude una **classe**, non un caso. Vanno per ultimi non perché
contino meno — F-11 e F-05 sono le cause per cui la P1 e la P2 esistono — ma perché una regola
strutturale si scrive dopo aver visto i casi, non prima.

| # | Intervento | Perché qui | Dipendenze | Rischio |
|---|---|---|---|---|
| 3.1 | **F-11 — Dare un confine agli skip** | Va **subito dopo** P1 e P2: è il momento in cui la prima batteria verde dirà `PASS WITH SKIPS (65 targets, ~19 skipped)` e verrà letta come «verde». Se la soglia non esiste prima di quel run, non verrà più scritta | 1.3, 2.2 | Basso tecnicamente, **alto se omesso**: è il difetto che si manifesta esattamente quando tutti gli altri sembrano risolti |
| 3.2 | **F-10 — Separare development gate e release gate** | Codifica la distinzione che questo audit ha dovuto ricostruire a mano. Va dopo che si sa quali suite reggono in quale ambiente | 1.3, 2.2, 3.1 | Medio. Due workflow possono divergere: l'opzione 3 di §3 li tiene su **un solo** corpo di test proprio per questo |
| 3.3 | **F-03(b) — Derivare `TESTS` invece di elencarlo** | Chiude la classe di cui 1.2 chiude il caso. Quarta ricorrenza documentata | 1.2 | Medio. Una derivazione automatica può cambiare l'ordine di esecuzione e includere suite mai girate: va introdotta con ordinamento esplicito e su un run osservato |
| 3.4 | **F-05 — Bit di esecuzione a monte** | Chiude la classe di cui 2.4 chiude il caso | 2.4 | Basso |
| 3.5 | **F-13 — Estendere il metodo di inventario delle migrazioni ai test** | Impedisce che la prossima migrazione normativa ripeta il taglio. Costa secondi per migrazione | Decisione su F-01 | Basso |
| 3.6 | **F-15 — Rivedere la configurazione della repository** | Visibilità, protezione di `main`, `sha_pinning_required`. Non è tecnica: è rischio accettato | Decisione umana | Non valutabile senza la decisione |

---

## 6 · HUMAN DECISIONS REQUIRED

### 6.1 · Decisioni tecniche delegabili

Meccaniche, a esito verificabile, senza scelta di principio. Restano non applicate: questo
mandato non le autorizza.

| Rif. | Decisione | Nota |
|---|---|---|
| F-04 | Impostare `+x` sui 4 entrypoint con shebang | `git update-index --chmod=+x`. Nessuna ambiguità |
| F-03(a) | Registrare `governance/scripts/test_candidate_content_hash.py` in `TESTS` | Chiude il caso, non la classe (→ 3.3) |
| F-06 | Guardia `try/except ImportError → skipTest` sull'import di `fitz` | **Solo dopo** la decisione 6.2/D-3 |
| F-14 | Aggiornare i tre pin di action a versioni su Node 24, mantenendo il SHA | In un cambio isolato |
| F-05 | Hook locale che imposti `+x` sui file con shebang | Non tocca GitHub Actions |

### 6.2 · Decisioni architetturali

Cambiano la forma del sistema. Nessuna ha una risposta ricavabile dal codice.

| Rif. | Decisione | Opzioni | Raccomandazione dell'audit |
|---|---|---|---|
| **D-1** | *Dove vivono le regole inviolabili, dato che `CLAUDE.md` si auto-carica per Claude e `AGENTS.md` per Codex?* (F-01, F-02) | 1. modificare i test · 2. modificare la documentazione · 3. registro delle superfici di avvio + duplicazione minima dichiarata | **Opzione 3.** È l'unica che sopravvive alla prossima migrazione. Richiede di ammettere che il router non può essere puro |
| **D-2** | *Il gate deve girare sempre, in che forma?* (F-10) | 4 opzioni in §3 | **Opzione 3** (due workflow, un solo corpo di test). L'audit **sconsiglia esplicitamente** l'opzione 4: ricostruisce la finestra cieca di F-12 |
| **D-3** | *PyMuPDF è opzionale o obbligatoria per l'ambiente di sviluppo?* (F-07) | opzionale → skip visibili e contati · obbligatoria → assenza = errore | Nessuna raccomandazione: dipende da quanto della disciplina probatoria deve essere verificabile a ogni commit. È il presupposto di 2.1 e 2.2 |
| **D-4** | *Dove passa il confine fra skip atteso e degradazione d'ambiente?* (F-11) | soglia · categorie dichiarate per motivo · nessun confine | Categorie dichiarate. Il meccanismo di riporto esiste già; manca il giudizio. Va deciso **prima** del primo run verde, non dopo |
| **D-5** | *Come si estende il contratto di degradazione allo stato «git superficiale»?* (F-08, F-09) | `fetch-depth: 0` · job dedicato · rilevare e degradare · combinazioni | Rilevare **e** approfondire: `--is-shallow-repository` per non fallire fuori dal CI, `fetch-depth: 0` perché il verificatore giri davvero. Sono complementari |

### 6.3 · Decisioni di governance

Non sono scelte tecniche. Riguardano cosa il sistema dichiara di sé e chi risponde di cosa.

| Rif. | Decisione | Perché è governance |
|---|---|---|
| **G-1** | *Questi 8 fallimenti sono un baseline di bootstrap o un blocco?* (F-12) | Determina se `main` di `legend-development` è utilizzabile oggi. L'evidenza sostiene «baseline»: 455 commit senza gate, tutte le cause radice interne alla finestra. Ma è una dichiarazione sullo stato del sistema, e va fatta da chi ne risponde |
| **G-2** | *Chi chiude la Mirror hostile review di `claude_md_migration_map.md`?* (F-13) | Il record è `PROPOSED` mentre la migrazione è su `main` da 7 giorni. La sua tesi — «the transformation lost nothing» — è confermata per le sedi normative e **non coperta** per la batteria di test e per l'asimmetria di caricamento. Il record va aggiornato o riaperto |
| **G-3** | *`legend-development` deve restare pubblica, con `main` non protetto?* (F-15) | Lo sviluppo continuo di un modello di malattia è visibile prima di passare il gate che esiste per decidere cosa è pubblicabile. Con agenti che scrivono in autonomia, la protezione del branch e `sha_pinning_required` sono vincoli, non preferenze |
| **G-4** | *Che cosa costituisce un «release point» fra development e stable?* (§3, D-2) | Oggi il passaggio è un `git push`. La separazione ha funzionato — ha trattenuto 455 commit non verificati — ma il ratchet in mezzo non è definito da nessuna parte |
| **G-5** | *Quale tasso di difetto è accettabile fra due esecuzioni del gate?* (F-12) | Tasso osservato: 4 difetti reali di contenuto in 22 giorni e 455 commit. Ogni opzione di §3 implica una risposta a questa domanda; conviene darla esplicitamente invece di ereditarla da una scelta di workflow |

---

## Appendice · Base di evidenza

Tutto ciò che è stato ispezionato direttamente, con il metodo di verifica.

| Oggetto | Metodo | Esito |
|---|---|---|
| Run 32666385829 | `gh run view --log`, 2 133 righe | 1 job, 8 suite fallite, 19 skip |
| `.github/workflows/public-release-gate.yml` | letto integralmente (43 righe) | unico workflow del repository |
| Modi dei file a `788c357` | `git ls-tree` + `stat` + sweep esaustivo sui `.py` tracciati | 4 su 4, nessun altro |
| Censimento delle suite | modulo runner importato (non regex) | 65 registrate · 66 tracciate · 1 mai eseguita |
| Token in `CLAUDE.md` | `grep -F` su `788c357:CLAUDE.md` e sul working tree | 5 su 5 assenti in entrambi |
| Sopravvivenza delle regole | `grep -F` sulle sedi normative, una per token | 5 su 5 presenti altrove |
| Consumatori di `fitz` | censimento dei 6, riga per riga | 5 import differiti · 1 a livello di modulo |
| Censimento degli skip | `skipped=N` sommati + motivi distinti, apici singoli **e** doppi | 19 totali: 13 + 4 + 1 + 1 |
| Aritmetica del freeze DisMech | conteggio input/output del baseline JSON | 12 + 1 + 1 = 14, coincide col test |
| Distanza del commit di freeze | `git rev-list --count` | 415 commit |
| Finestra senza CI | `gh run list` su entrambe le repo + `git rev-list --count` | 4/4 verdi fino al 2026-08-01 · 455 commit · 0 run |
| Configurazione repository | `gh api` su repo, branch protection, actions permissions | pubblica · `main` non protetto · `allowed_actions: all` |
| `requirements-analysis.txt` | letto integralmente | 1 dipendenza: `numpy==2.0.2` |
| Contratto di degradazione | `test_release_runner_verdict.py` + `run_release_regressions.py` | esiste per «git assente», cieco su «git superficiale» |

**Correzione effettuata durante l'audit e non propagata al documento.** Un primo censimento
delle suite, ricavato con espressione regolare sulla tupla `TESTS`, dava 67 registrate: due voci
sono scritte come letterali stringa concatenati implicitamente su due righe e venivano contate
doppie. Il numero corretto — 65 registrate, 66 tracciate, 1 mai eseguita — è stato ottenuto
importando il modulo runner ed è quello riportato ovunque in questo documento.

**Limiti dichiarati di questo audit.** Le suite fallite non sono state rieseguite in locale:
la classificazione di F-01, F-03 e F-04 come difetti riproducibili fuori dal CI si fonda su
verifica diretta dei contenuti e dei modi (token assenti nel blob, modi `100644` nell'indice,
censimento delle suite dal modulo runner), non su un'esecuzione locale della batteria. Le
correzioni proposte non sono state provate. Nessun ambiente con `fetch-depth: 0` è stato
costruito per verificare se il freeze DisMech, una volta reso verificabile, regga davvero —
è la prima cosa che l'intervento 1.3 renderà nota, ed è la ragione per cui il suo rischio è
segnato **medio** e non basso.
