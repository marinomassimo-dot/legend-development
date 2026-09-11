# sviluppo_lettori.md

## Scopo

Registro cumulativo degli spunti utili allo sviluppo dei **Scientist / lettori di LEGEND** emersi dalle review Tier-1.

Questo file non sostituisce i forensic delle singole repository. Serve a registrare, in modo incrementale:

- pattern utili per i Scientist di LEGEND;
- elementi che diventano più forti dopo nuove review;
- elementi che si indeboliscono o risultano non dimostrati;
- decisioni ancora aperte;
- design incrementale emergente;
- separazione tra attività realmente scientifiche e attività che dovrebbero essere software deterministico.

**Regola cumulativa:** le conclusioni precedenti non vengono cancellate. Quando una review modifica la forza di un pattern, viene aggiunta una nuova nota con stato aggiornato.

---

# 0. Baseline iniziale LEGEND — prima delle nuove review

## Scientist attuali

LEGEND utilizza tre Scientist con profilo scientifico sostanzialmente comune, mantenuti in parallelo soprattutto per aumentare la velocità di lettura e analisi.

Il valore da preservare non è l'identità permanente `Scientist A / B / C`, ma il principio:

> **più Scientist equivalenti possono lavorare in parallelo sullo stesso grande corpus per aumentare il throughput scientifico.**

Capacità comuni già considerate preziose:

- lettura del full text;
- attenzione a figure, tabelle e dettagli;
- separazione tra **dato / inferenza / ipotesi**;
- tracciamento dei full text analizzati;
- data curation;
- cross-paper inference;
- output compatibile con criteri DisMech;
- parafrasi scientifica;
- supporto verbatim / fonte precisa dove richiesto;
- ricerca di contraddizioni;
- conservazione della provenienza;
- lavoro scientifico parallelo coordinato dall'Orchestrator.

## Problema architetturale da non confondere con il valore dei Scientist

Le review precedenti su LEGEND hanno mostrato che il problema non è il parallelismo dei Scientist.

Il problema è legare:

`Scientist identity = permanent branch = permanent worktree = permanent runtime topology`

Il design emergente deve quindi preservare:

`N Scientist equivalenti in parallelo`

eliminando, se possibile:

`N identità Git permanenti`.

---

# 1. Review 01 — Robin

Repository analizzata: `Future-House/robin`

## 1.1 Nuovi spunti utili per gli Scientist LEGEND

### A. Fan-out scientifico per domanda, non solo per documento

Robin distribuisce il lavoro principalmente come:

`scientific question → parallel research task`

piuttosto che:

`paper → fixed reader`

Questo suggerisce che LEGEND non dovrebbe limitarsi a una pipeline:

`paper 1 → Scientist 1`

`paper 2 → Scientist 2`

ma consentire anche:

`mechanistic question → bounded parallel research branches`.

### Implicazione

Il Scientist generalista dovrebbe poter ricevere sia:

- un documento da leggere profondamente;
- una domanda scientifica da esplorare attraverso più fonti.

**Stato:** EMERGING.

---

### B. Specializzazione funzionale diversa dal semplice parallelismo

Robin separa funzioni scientifiche differenti:

- literature research;
- deep review;
- computational analysis;
- ranking/evaluation;
- synthesis.

Questo suggerisce che LEGEND può mantenere un **General Scientist Pool** ampio e, contemporaneamente, aggiungere specialisti o modalità specialistiche.

### Design emergente

```text
GENERAL SCIENTIST POOL
    S1 S2 S3 S4 ...

SPECIALIST MODES / WORKERS
    Hostile Reviewer
    Evidence Verifier
    Curator
    Mechanism Synthesizer
    Computational Scientist
    Experimental Scientist
```

Non è necessario che ogni specializzazione diventi un attore permanente.

**Stato:** STRONGER.

---

### C. Scientific judgment + deterministic aggregation

Robin separa bene:

`LLM scientific comparison`

da:

`deterministic BTL aggregation`.

Principio trasferibile:

> **l'agente giudica ciò che richiede ragionamento; il software aggrega ciò che può essere calcolato deterministicamente.**

Possibili applicazioni LEGEND:

- ranking di ipotesi;
- ranking di candidate terapeutiche;
- priorità tra meccanismi;
- aggregazione di pairwise comparisons;
- consensus scoring.

**Stato:** STRONGER.

---

### D. Bounded parallelism

Robin dimostra un parallelismo forte senza ricorsione agentica illimitata.

Questo indebolisce l'idea che ogni Scientist debba necessariamente poter creare una gerarchia arbitraria di subagent.

### Implicazione

Il Scientist può avere:

`missing need → bounded branch → result → reintegration`

ma:

- profondità limitata;
- budget limitato;
- concurrency limitata;
- nessun recursive swarm come default.

**Stato:** STRONGER.

---

### E. Hierarchical scientific compression

Robin evita di mandare tutto il corpus a ogni passaggio.

Pattern:

`retrieval/query-specific evidence → local report → synthesis → hypothesis → deeper targeted analysis`

Per migliaia di paper questo è fondamentale.

### Implicazione per Scientist

Ogni Scientist dovrebbe lavorare con **contesto locale rilevante**, non con l'intero patrimonio scientifico LEGEND.

Il sistema dovrebbe recuperare solo:

- paper assegnato;
- evidence packets pertinenti;
- claims/meccanismi correlati;
- contraddizioni rilevanti;
- task objective;
- lezioni applicabili.

**Stato:** STRONGER.

---

### F. Multi-trajectory scientific analysis

Robin utilizza più analisi indipendenti dello stesso dataset e poi consensus/meta-analysis.

Questo suggerisce una forma di parallelismo diversa dalla semplice divisione del corpus:

> **più Scientist possono analizzare indipendentemente lo stesso problema quando l'incertezza o l'importanza scientifica lo giustifica.**

Possibile policy:

- paper ordinario → 1 deep reader;
- paper critico → 2 blinded readers;
- claim meccanicistica critica → independent verification;
- dataset importante → multiple trajectories.

**Stato:** EMERGING / BENCHMARK.

---

### G. Closed scientific loop

Pattern Robin:

`literature → mechanism → hypothesis → experiment → result → next hypothesis`

Questo amplia il ruolo futuro dello Scientist LEGEND.

Il Scientist non dovrebbe essere solo un lettore/curatore, ma poter entrare in un loop:

- leggere;
- inferire;
- formulare ipotesi;
- proporre test;
- usare strumenti computazionali;
- interpretare risultati;
- riaprire il modello scientifico.

**Stato:** STRONGER.

---

### H. Tre review semanticamente diverse

Dalla forensic Robin emerge la necessità di distinguere:

1. **Ranking review**
   - “A è migliore di B?”

2. **Evidence verification**
   - “La fonte sostiene davvero questa claim?”

3. **Hostile scientific review**
   - “L'interpretazione scientifica regge a falsificazione e spiegazioni alternative?”

Queste funzioni non devono essere fuse.

**Stato:** STRONGER.

---

### I. Full-text completeness non deve essere affidata a un secondo Scientist

Robin mostra una lacuna importante: non può provare di aver coperto interamente un corpus chiuso.

Per LEGEND, la lezione non è aggiungere un agente che controlli meccanicamente la lettura.

Il controllo di:

- documenti attesi;
- pagine;
- figure;
- tabelle;
- supplements;
- parsing;
- hash;
- DOI/PMID;
- locator;

deve essere **software deterministico**.

Il Reviewer deve invece controllare:

> “Il Scientist ha scientificamente compreso ciò che era disponibile?”

**Stato:** STRONGER.

---

### J. Persistent prose non basta come memoria scientifica

Robin conserva report utili ma prevalentemente narrativi.

LEGEND deve mantenere una memoria scientifica più strutturata:

`paper → evidence → claim → mechanism → hypothesis → review`.

**Stato:** STRONGER.

---

## 1.2 Cosa Robin indebolisce

### Idea indebolita: molti attori permanenti = migliore scienza

Robin non supporta questa equivalenza.

La sua efficacia deriva da:

- decomposition;
- specialization;
- bounded fan-out;
- tools;
- deterministic aggregation;
- closed-loop experimentation.

Non dalla quantità di identità permanenti.

**Stato:** WEAKER.

---

### Idea indebolita: ogni Scientist deve avere recursive subagents

Non dimostrato.

Un fan-out bounded e predefinito può essere più stabile.

**Stato:** WEAKER / UNRESOLVED.

---

# 2. Review 02 — AutoScientists

Repository analizzata: `mims-harvard/AutoScientists`

## 2.1 Nuovi spunti utili per gli Scientist LEGEND

### A. Horizontal parallelism è una primitive scientifica valida

AutoScientists usa più worker equivalenti per ruolo:

- Analyst ×3;
- GPU workers ×6.

Questo rafforza direttamente l'idea di LEGEND di mantenere più Scientist equivalenti per aumentare velocità e throughput.

### Implicazione

Il futuro design dovrebbe esplicitare:

```text
ScientistPool(size=N)
```

dove N è un parametro di deployment e workload, non una proprietà semantica del ruolo.

Esempi:

- N=3 oggi;
- N=10 con corpus maggiore;
- N=50 se runtime, budget e synthesis layer lo consentono.

**Stato:** STRONGER.

---

### B. Generalist Pool + Specialist Pool

AutoScientists combina:

- worker equivalenti;
- ruoli funzionalmente diversi.

Questo rafforza il design emerso da Robin:

```text
ORCHESTRATOR
      │
GENERAL SCIENTIST POOL
      │
      ├─ paper reading
      ├─ evidence extraction
      ├─ inference
      └─ hypothesis generation

SPECIALIST MODES / WORKERS
      ├─ hostile review
      ├─ evidence verification
      ├─ computation
      ├─ curation
      ├─ synthesis
      └─ experiment design
```

**Stato:** STRONGER.

---

### C. Team scientifici organizzati intorno a ipotesi falsificabili

AutoScientists non organizza il lavoro solo per “dominio”.

Forma team intorno a ipotesi e li riorganizza quando l'evidenza le indebolisce.

### Implicazione per LEGEND

Dopo la lettura individuale dei paper, Scientist equivalenti potrebbero essere temporaneamente raggruppati intorno a:

- meccanismo;
- contraddizione;
- target terapeutico;
- fenomeno;
- ipotesi falsificabile.

La specializzazione può quindi essere **temporanea e task-driven**, non identitaria.

**Stato:** STRONGER.

---

### D. Self-regroup senza microrouting continuo dell'Orchestrator

AutoScientists permette ai worker scientifici di reagire a stagnazione e risultati negativi.

Questo rafforza il principio:

> l'Orchestrator autorizza obiettivo, budget, priorità e review floor; gli Scientist decidono localmente come esplorare scientificamente il task entro quei limiti.

### Implicazione

Possibili azioni locali dello Scientist:

- richiedere una capability;
- aprire un bounded subtask;
- cambiare microstrategia;
- proporre una nuova ipotesi;
- chiedere un secondo lettore;
- chiedere un'analisi computazionale;
- riformare un gruppo temporaneo.

Senza cambiare:

- scope;
- authority;
- canonical state;
- human gate;
- budget massimo.

**Stato:** STRONGER.

---

### E. Dynamic work claiming

AutoScientists utilizza queue e worker che prendono lavoro disponibile.

Per migliaia di paper questo è più adatto della partizione statica:

`50 paper / 5 Scientist = 10 ciascuno`.

Design preferibile:

```text
READY_PAPERS
    ↓
atomic claim
    ↓
next available Scientist
```

Vantaggi:

- paper di lunghezza diversa;
- worker più veloci non restano inattivi;
- recupero da failure;
- elastic scaling.

**Stato:** STRONGER.

---

### F. Dead-end memory

AutoScientists conserva:

- pattern vincenti;
- direzioni esaurite;
- esperimenti falliti;
- hypotheses falsificate.

Questo rafforza un requisito importante per Scientist LEGEND:

> **non ripetere lavoro scientifico già dimostrato inutile salvo nuova evidenza che giustifichi revival.**

Possibile struttura:

```text
LESSON / DEAD_END
evidence
context
reason
conditions
reopen_if
```

Da combinare con il dismissal/revival già presente in LEGEND.

**Stato:** STRONGER.

---

### G. LIST first → selective READ

AutoScientists utilizza una strategia di context economy:

> prima inventario/search, poi leggere selettivamente ciò che serve.

Questo è molto importante per migliaia di pubblicazioni.

Non significa leggere superficialmente i paper assegnati.

Significa:

- non caricare tutta la memoria globale a ogni Scientist;
- recuperare solo ciò che serve al task corrente;
- una volta assegnato un paper, leggerlo profondamente secondo protocollo.

### Principio

> **global knowledge selective; assigned evidence exhaustive.**

**Stato:** STRONGER.

---

### H. Falsification deve essere parte del lavoro Scientist

AutoScientists rende espliciti:

- hypothesis;
- prediction;
- falsification;
- experimental result;
- KEEP/DISCARD.

Per LEGEND questo suggerisce che una buona ipotesi dovrebbe contenere almeno:

```text
HYPOTHESIS
PREDICTION
FALSIFICATION CONDITION
SUPPORTING EVIDENCE
CONTRADICTORY EVIDENCE
NEXT TEST
```

Questo rende l'inferenza più scientificamente operativa.

**Stato:** STRONGER.

---

### I. Computation specialist ≠ generic Scientist

Il GPU worker mostra che alcune attività possono meritare una modalità specializzata di esecuzione.

Per LEGEND:

- bioinformatics;
- statistical analysis;
- structural analysis;
- omics;
- simulation;
- model execution;

possono essere gestite da:

`Scientist(mode=computational)`

o da capability dedicate.

Non serve necessariamente creare attori permanenti distinti.

**Stato:** STRONGER.

---

### J. Monitor/watchdog non è Scientist

AutoScientists conferma che worker health, stale claims, retry e queue status sono meccaniche operative.

Per LEGEND:

- stale task detection;
- retry;
- task lifecycle;
- timeout;
- worker health;
- restart;
- queue accounting;

devono diventare **software/runtime**, non ruolo cognitivo.

**Stato:** STRONGER.

---

### K. Model quality può essere una variabile del ruolo

AutoScientists documenta che modelli più deboli possono non eseguire correttamente responsabilità agentiche complesse.

Implica che LEGEND dovrebbe separare:

```text
ROLE
MODEL
PROVIDER
HARNESS
```

e benchmarkare quale modello serve per:

- deep reading;
- hostile review;
- synthesis;
- evidence verification;
- routine classification.

Non tutti i task richiedono necessariamente lo stesso modello.

**Stato:** EMERGING / BENCHMARK.

---

## 2.2 Cosa AutoScientists indebolisce

### Roster fisso come scaling model

`3 Analyst + 6 GPU` funziona nel caso nativo ma non è una buona primitive generale.

Per LEGEND:

`ScientistPool(size=N)` è preferibile.

**Stato:** REJECT fixed roster.

---

### Permanent named Scientist identities

AutoScientists mostra che worker dello stesso ruolo sono ampiamente fungibili.

Questo indebolisce ulteriormente l'idea che `Scientist A/B/C` debbano essere primitive architetturali permanenti.

Il valore è nel **contratto comune + instance identity**, non nel nome.

**Stato:** WEAKER.

---

### Shared context come prova di independent review

AutoScientists possiede falsification e peer discussion, ma non una vera hostile review indipendente.

Quindi:

> peer criticism ≠ independent hostile review.

**Stato:** STRONGER distinction.

---

# 3. Disegno incrementale emergente dopo Robin + AutoScientists

## 3.1 Topologia scientifica provvisoria

```text
                              ORCHESTRATOR
                                   │
                    objectives / priority / budget
                                   │
                          SCIENTIFIC TASK POOL
                                   │
                  ┌────────────────┴─────────────────┐
                  │                                  │
        GENERAL SCIENTIST POOL                SPECIALIST LAYER
                  │                                  │
        S1 S2 S3 S4 S5 ...              ┌───────────┼────────────┐
                  │                      │           │            │
          deep paper reading        Reviewer     Curator      Compute
          evidence extraction       hostile      evidence     bioinfo
          inference                 verifier     schema       statistics
          hypothesis                    │           │            │
                  │                      └───────────┼────────────┘
                  │                                  │
                  └──────────────────┬───────────────┘
                                     ▼
                            HIERARCHICAL SYNTHESIS
                                     │
                                     ▼
                           MECHANISMS / HYPOTHESES
                                     │
                                     ▼
                            EXPERIMENT / TOOL LOOP
                                     │
                                     ▼
                              NEW EVIDENCE
```

---

# 4. General Scientist — contratto emergente

Ogni General Scientist dovrebbe condividere un core comune.

## Common scientific capabilities

- deep full-text reading;
- inspect Methods;
- inspect Results;
- inspect figures;
- inspect tables;
- inspect supplementary material where available;
- evidence extraction;
- exact provenance;
- data curation;
- observation/data identification;
- author interpretation identification;
- agent inference;
- hypothesis generation;
- contradiction detection;
- cross-paper reasoning;
- uncertainty recording;
- falsifiability;
- structured scientific output;
- tool use;
- request bounded specialist assistance.

## Non deve gestire

- process lifecycle;
- retry;
- worker health;
- task queues mechanically;
- filesystem bookkeeping;
- page-count completeness;
- hash checks;
- duplicate file checks;
- runtime recovery.

---

# 5. Scientist pool — design emergente

## Principio

> **stesso contratto, molte istanze.**

Non:

```text
Scientist A
Scientist B
Scientist C
```

come ruoli semantici differenti.

Ma:

```text
ScientistContract
    ↓
Instance 001
Instance 002
Instance 003
...
```

Possibili campi:

```text
ACTOR_ID
INSTANCE_ID
SESSION_ID
TASK_ID
MODE
MODEL
PROVIDER
HARNESS
CAPABILITIES
INDEPENDENCE_GROUP
BUDGET
REVIEW_REQUIREMENT
```

## N è parametrico

```text
ScientistPool(size=N)
```

N dipende da:

- corpus;
- budget;
- API rate limits;
- runtime;
- urgency;
- synthesis capacity;
- review capacity.

---

# 6. Specialist layer — design emergente

## Possibili specialisti

### Hostile Reviewer

Funzione:

- cercare alternative explanations;
- causal overreach;
- contradictions;
- unsupported claims;
- confounders;
- missing controls.

Preferibilmente:

- fresh context;
- independence group diverso;
- eventualmente modello differente.

Non necessariamente permanente.

---

### Evidence Verifier

Funzione:

- riaprire la fonte;
- controllare che il passaggio sostenga davvero la claim;
- verificare figure/tabelle rilevanti;
- produrre SUPPORT / PARTIAL / DOES_NOT_SUPPORT.

Ephemeral e selettivo.

---

### Curator

Funzione:

- normalizzazione;
- schema;
- ontology mapping;
- entity resolution;
- claim normalization.

Gran parte del lavoro deve essere ibrido:

`software/schema + scientific judgment`.

---

### Computational Scientist

Funzione:

- code execution;
- statistics;
- omics;
- simulations;
- structural analysis;
- quantitative validation.

Può essere:

`Scientist(mode=compute)`

più capability specialistiche.

---

### Mechanism / Synthesis Scientist

Funzione:

- integrare molte letture;
- costruire meccanismi;
- conservare minority evidence;
- identificare contraddizioni;
- produrre cross-paper inference.

Potrebbe diventare il principale bottleneck su corpus grandi.

Richiede benchmark.

---

# 7. Full-text completeness — design emergente

## Deterministic gate

Ogni documento dovrebbe avere un manifest simile a:

```text
paper_id
DOI
PMID
source_hash
page_count
pages_available
pages_processed
figure_count
figures_available
tables_count
supplements_expected
supplements_available
parse_status
reader_task
reader_status
```

Software deve poter dire:

> tutti gli artefatti previsti sono stati resi disponibili al Scientist?

Non deve pretendere di dire:

> il Scientist li ha capiti scientificamente?

Questa seconda domanda resta agentica.

---

# 8. Evidence package — design emergente

Per claim scientificamente importante:

```text
claim_id
paper_id
epistemic_type
paraphrased_claim
verbatim_support
locator
figure/table/panel
source_hash
scientist_id
confidence
contradictions
review_status
```

Possibili epistemic types:

```text
OBSERVATION
AUTHOR_INTERPRETATION
AGENT_INFERENCE
HYPOTHESIS
NEGATIVE_RESULT
CONTRADICTION
```

---

# 9. Review architecture — design emergente

Tre funzioni separate.

## Ranking

Agentic judgment + deterministic aggregation quando possibile.

## Evidence verification

Fresh independent verification su claims selezionate.

## Hostile review

Fresh independent scientific falsification delle interpretazioni importanti.

### Risk-based review

Non tutto deve ricevere doppio costo.

Possibile policy:

```text
ordinary paper
→ one deep Scientist
→ deterministic completeness

high-impact paper
→ one deep Scientist
→ fresh evidence verifier

major mechanism
→ synthesis
→ hostile reviewer

high-risk therapeutic conclusion
→ independent review
→ possible second model
```

---

# 10. Parallelism — design emergente

Tre tipi distinti.

## 10.1 Throughput parallelism

Molti Scientist equivalenti analizzano paper/task diversi.

Serve alla velocità.

## 10.2 Hypothesis diversity

Team/Scientist diversi esplorano spiegazioni concorrenti.

Serve ad evitare local scientific minima.

## 10.3 Replication / verification

Due o più Scientist esaminano indipendentemente lo stesso oggetto.

Serve alla robustezza.

Questi tre tipi non devono essere confusi.

---

# 11. Task claiming — design emergente

Preferenza corrente:

```text
READY_TASK
    ↓
atomic claim
    ↓
next eligible Scientist
```

piuttosto che partizioni permanenti.

Il task può essere:

- paper;
- evidence verification;
- mechanism synthesis;
- contradiction analysis;
- computation;
- hostile review;
- experiment proposal.

---

# 12. Context architecture — design emergente

Principio:

> **global knowledge selective; assigned evidence exhaustive.**

Scientist non deve ricevere:

- intero repository;
- intero history;
- migliaia di paper;
- tutta la governance.

Deve ricevere:

- Task Contract;
- paper/evidence assegnato;
- strumenti;
- claims correlate;
- prior contradictions;
- relevant lessons;
- relevant mechanism state.

Per il paper assegnato deve però poter fare deep reading completo.

---

# 13. Experience / dead-end memory — design emergente

Gli errori e fallimenti non devono accumularsi automaticamente nel prompt Scientist.

Classificazione preferita:

```text
failure / lesson
   ↓
DETERMINISTIC BUG → test + code fix
INVARIANT → kernel rule
SCIENTIFIC DEAD END → searchable scientific memory
CONTEXTUAL LESSON → retrievable lesson
NOISE → log only
```

Per la scienza:

```text
dead_end
supporting evidence
why rejected
conditions
reopen_if
```

---

# 14. Open questions dopo due review

## UNRESOLVED — Elastic Scientist Pool

Robin non lo dimostra pienamente.

AutoScientists supporta worker equivalenti ma roster fisso.

Serve ulteriore convergenza.

---

## UNRESOLVED — Permanent specialist vs Scientist mode

Non è ancora dimostrato quali specialisti meritino un contratto permanente.

Tendenza attuale:

- General Scientist → permanent contract;
- Hostile Reviewer → ephemeral mode;
- Evidence Verifier → ephemeral mode;
- Curator → mode/hybrid;
- Compute → mode/capability;
- Synthesis → possibly dedicated mode/worker.

---

## UNRESOLVED — Same model vs different model reviewer

Da benchmarkare:

- same model + fresh context;
- different model + fresh context.

Independence of context appears more fundamental than mere model diversity, but this is not yet proven.

---

## UNRESOLVED — One paper per Scientist vs question-driven exploration

Probabile combinazione:

### corpus coverage layer

`paper → deep reader`

### scientific discovery layer

`mechanistic question → parallel research branch`.

I due pattern sembrano complementari.

---

## UNRESOLVED — Hierarchical synthesis topology

Per 5,000 paper non può esistere una sola final synthesis call.

Serve probabilmente:

```text
paper
→ claim
→ topic/mechanism cluster
→ intermediate synthesis
→ higher-order mechanism
→ disease model
```

Ma la migliore topologia deve ancora emergere dalle prossime review.

---

# 15. Cumulative pattern ledger

| Pattern | Stato dopo Robin | Stato dopo AutoScientists | Stato cumulativo | Evidenza |
|---|---|---|---|---|
| Multiple equivalent Scientists | EMERGING | STRONGER | **STRONGER** | AutoScientists |
| Elastic `ScientistPool(N)` | EMERGING | PARTIAL | **UNRESOLVED but favored** | AutoScientists fixed roster |
| Generalists + specialists | STRONGER | STRONGER | **STRONGER** | Robin + AutoScientists |
| Fixed named permanent Scientists | WEAKER | WEAKER | **WEAKER** | both |
| Permanent worktree per Scientist | not supported | not supported | **REJECT direction** | prior LEGEND evidence |
| Query-driven scientific fan-out | STRONG | complementary | **STRONGER** | Robin |
| Dynamic work claiming | partial | strong pattern | **STRONGER** | AutoScientists |
| Hypothesis-driven teams | partial | strong | **STRONGER** | AutoScientists |
| Self-regroup | limited | strong | **STRONGER** | AutoScientists |
| Recursive unbounded subagents | weak | unnecessary | **WEAKER** | both |
| Bounded delegation | strong | strong | **STRONGER** | both |
| Specialized compute role | strong | strong | **STRONGER** | both |
| Hostile reviewer | absent | partial/distributed | **NEEDED but not natively solved** | both |
| Evidence verifier | partial | absent | **NEEDED** | both |
| Deterministic full-text completeness | absent | absent | **STRONGER requirement** | both fail |
| Evidence packet | absent/partial | absent | **STRONGER requirement** | both fail |
| Epistemic typing | absent/partial | hypothesis only | **STRONGER requirement** | LEGEND advantage |
| Persistent structured claim store | absent | absent | **STRONGER requirement** | both fail |
| Hierarchical synthesis | strong | experimental analogue | **STRONGER** | Robin + AutoScientists |
| LIST/selective READ | implicit | strong | **STRONGER** | AutoScientists |
| Multi-trajectory analysis | strong | multiple workers/experiments | **STRONGER / BENCHMARK** | both |
| Agent judgment + deterministic aggregation | strong | metric-driven | **STRONGER** | both |
| Closed hypothesis→experiment loop | strong | very strong computationally | **STRONGER** | both |
| Dead-end memory | limited | strong | **STRONGER** | AutoScientists |
| Monitor/watchdog as agent | no need | exists but mechanical | **REJECT as Scientist role** | AutoScientists |
| Runtime/task recovery as software | favored | clearly applicable | **STRONGER** | AutoScientists |
| Risk-based independent double reading | plausible | absent | **UNRESOLVED / BENCHMARK** | neither implements |
| Different-model review | plausible | unproven | **UNRESOLVED / BENCHMARK** | neither proves |

---

# 16. Current provisional Scientist design

> **This is an incremental hypothesis, not a frozen architecture.**

```text
ORCHESTRATOR
    │
    │ objectives / priority / budget / review floor
    ▼
SCIENTIFIC TASK POOL
    │
    ├───────────────────────────────────────┐
    │                                       │
    ▼                                       ▼
GENERAL SCIENTIST POOL                SPECIALIST MODES
N interchangeable instances          on demand
    │                                       │
    ├─ deep reading                         ├─ hostile review
    ├─ evidence extraction                  ├─ evidence verification
    ├─ curation                             ├─ computation
    ├─ inference                            ├─ advanced curation
    ├─ hypothesis                           ├─ synthesis
    └─ tool use                             └─ experiment design
    │                                       │
    └──────────────────┬────────────────────┘
                       ▼
                STRUCTURED RESULTS
                       │
             deterministic gates
                       │
                       ▼
             HIERARCHICAL SYNTHESIS
                       │
                       ▼
             MECHANISMS / HYPOTHESES
                       │
                 hostile review
                       │
                       ▼
                 scientific state
                       │
                       ▼
             experiment / next question
```

---

# 17. Current strongest Scientist principles

1. **Maintain multiple equivalent Scientists for throughput.**
2. **Make Scientist count elastic rather than structurally fixed.**
3. **Share one strong General Scientist contract.**
4. **Use specialist modes/workers only where specialization has measurable value.**
5. **Do not turn runtime mechanics into Scientist responsibilities.**
6. **Deep-read assigned evidence exhaustively; retrieve global context selectively.**
7. **Separate data/observation, author interpretation, agent inference and hypothesis.**
8. **Require evidence packets for important claims.**
9. **Track deterministic document completeness separately from scientific understanding.**
10. **Use independent review selectively according to scientific risk.**
11. **Distinguish ranking, evidence verification and hostile scientific review.**
12. **Allow bounded Scientist-local delegation within authorized scope.**
13. **Use dynamic task claiming to maximize throughput.**
14. **Preserve failed hypotheses/dead ends and define revival conditions.**
15. **Organize temporary teams around scientific hypotheses when useful.**
16. **Let software aggregate, schedule, retry and validate mechanical facts.**
17. **Keep computational outputs separate from their scientific interpretation.**
18. **Support hypothesis → experiment → result → revised hypothesis loops.**
19. **Design context for thousands of papers through hierarchical synthesis.**
20. **Treat every current conclusion as revisable by future Tier-1 evidence.**

---

# 18. Update protocol for future Tier-1 reviews

For every subsequent repository review append a new section:

```text
# Review NN — <repository>

## New Scientist patterns
## Patterns strengthened
## Patterns weakened
## New specialist roles
## New deterministic-software candidates
## Scaling implications
## Review implications
## Evidence/provenance implications
## Context/token implications
## Scientific-loop implications
## Changes to provisional design
## New unresolved questions
```

Then update the **Cumulative pattern ledger** without deleting prior states.

Use state vocabulary:

- **EMERGING**
- **STRONGER**
- **WEAKER**
- **UNRESOLVED**
- **BENCHMARK**
- **REJECT**
- **ADOPT CANDIDATE**

Where a later repository contradicts an earlier conclusion, record both:

```text
Previous state:
New evidence:
Updated state:
Reason:
```

Do not silently overwrite history.


# 19. Review 03 — DisMech

Repository analizzata: `monarch-initiative/dismech`

## 19.1 Nuovi spunti utili per gli Scientist LEGEND

### A. Structured scientific memory è una primitive centrale, non un semplice output finale

DisMech rafforza molto un punto che Robin e AutoScientists lasciavano debole: il lavoro dello Scientist non dovrebbe terminare principalmente in prose/report, ma in **scientific state machine-readable e riusabile**.

Pattern nativo:

```text
research artifact
→ exact evidence
→ structured disease entity
→ atomic pathophysiology node
→ causal edge
→ mechanistic hypothesis
→ review
→ canonical KB
```

Per LEGEND questo implica che ogni deep-reading task dovrebbe produrre qualcosa che possa essere integrato incrementalmente in una memoria strutturata, non solo una sintesi narrativa.

**Stato:** STRONGER.

---

### B. Exact snippet + provenance deve diventare standard per le claims importanti

DisMech usa EvidenceItem con:

- riferimento;
- exact snippet;
- SUPPORT / REFUTE / NO_EVIDENCE;
- evidence source;
- explanation;
- immagini opzionali.

Questo rafforza fortemente il requisito di LEGEND di mantenere:

```text
paraphrased scientific claim
+
verbatim support
+
source identity
+
locator/provenance
```

La forensic mostra però che DisMech non garantisce sempre locator forense completo come pagina/panel/supplemento.

Quindi il design LEGEND dovrebbe **mantenere il punto forte DisMech e irrigidirlo sui locator full-text**.

**Stato:** STRONGER.

---

### C. SUPPORT / REFUTE come polarity nativa

DisMech non conserva solo evidenze a favore.

Può rappresentare:

```text
SUPPORT
REFUTE
NO_EVIDENCE
```

Questo è molto utile per LEGEND.

Implica che lo Scientist non dovrebbe produrre solo “findings”, ma anche evidenza negativa strutturata.

### Design emergente per evidence packet

```text
claim_id
source_id
epistemic_type
polarity:
    SUPPORT
    REFUTE
    NO_EVIDENCE
evidence_source
verbatim
locator
explanation
```

**Stato:** STRONGER.

---

### D. Evidence-source typing

DisMech distingue almeno:

- HUMAN_CLINICAL;
- MODEL_ORGANISM;
- IN_VITRO;
- COMPUTATIONAL;
- OTHER.

Questo rafforza un punto importante per i lettori LEGEND: non tutte le evidenze devono entrare nel meccanismo con lo stesso peso epistemico.

Per il futuro Scientist contract conviene includere almeno:

```text
EVIDENCE_SOURCE
```

separato da:

```text
EPISTEMIC_TYPE
```

Esempio:

```text
epistemic_type = OBSERVATION
evidence_source = MODEL_ORGANISM
```

sono due assi differenti.

**Stato:** STRONGER.

---

### E. Edge-specific evidence

Una delle lezioni scientifiche più forti di DisMech:

> due nodi ben supportati non dimostrano automaticamente il nesso causale tra loro.

Quindi:

```text
Node A supported
Node B supported
```

non implica:

```text
A → B supported
```

Per LEGEND questo suggerisce di rendere il **causal edge** un oggetto scientifico con evidenza propria.

### Implicazione

Il Mechanism/Synthesis Scientist deve distinguere:

- evidence for entity/state A;
- evidence for entity/state B;
- evidence for relation A→B.

**Stato:** ADOPT CANDIDATE / STRONGER.

---

### F. Atomic mechanistic decomposition

DisMech tende a separare eventi biologici in nodi atomici invece di condensare molte trasformazioni in una frase unica.

Questo è molto utile per LEGEND perché facilita:

- contradiction detection;
- edge review;
- provenance;
- incremental update;
- machine-readable pathograph;
- hypothesis reopening.

### Regola emergente

> **Una claim meccanicistica complessa deve essere decomponibile in atomic events + explicit relations.**

**Stato:** STRONGER.

---

### G. Mechanistic hypotheses come oggetti persistenti

DisMech mantiene ipotesi con:

- stable ID;
- status;
- description;
- evidence;
- subtype applicability;
- notes.

Questo rafforza il requisito di non lasciare le ipotesi disperse nelle prose.

Per LEGEND:

```text
HYPOTHESIS_ID
STATUS
PREDICTION
FALSIFICATION
SUPPORTING_EVIDENCE
REFUTING_EVIDENCE
NEXT_TEST
REOPEN_CONDITION
```

dovrebbe diventare un oggetto riusabile.

**Stato:** STRONGER.

---

### H. Proposed experiment come oggetto scientifico strutturato

DisMech rappresenta un esperimento con:

- model system;
- perturbation;
- assay;
- readout;
- controls;
- decision criterion;
- would_support;
- would_refute.

Questo amplia la lezione Robin/AutoScientists sul falsification loop.

Il future Scientist non dovrebbe limitarsi a:

> “servirebbe verificare X”.

Dovrebbe poter produrre:

```text
EXPERIMENT
model
perturbation
controls
readouts
decision_rule
would_support
would_refute
```

**Stato:** STRONGER.

---

### I. Fresh hostile review dopo deterministic validation

Questo è forse il contributo più forte di DisMech al design dei reviewer LEGEND.

Pattern:

```text
candidate scientific model
→ deterministic schema/reference/ontology validation
→ fresh-context hostile scientific reviewer
→ repair
→ independent PR review
```

Principio:

> **Il Reviewer non deve spendere token a rifare i controlli che il software sa già fare.**

Deve concentrarsi su:

- biological plausibility;
- causal overreach;
- missing mechanisms;
- source-to-claim semantic support;
- wrong scientific ontology concept despite valid CURIE;
- under-consumption;
- model completeness.

**Stato:** ADOPT CANDIDATE / VERY STRONG.

---

### J. Producer ≠ validator diventa molto più forte

Robin aveva ranking separation.
AutoScientists aveva metric/execution separation.
DisMech dimostra una forma più adatta a LEGEND:

```text
Curator/Scientist
→ deterministic validators
→ fresh reviewer
→ canonical decision
```

Questo rafforza:

> **canonical scientific synthesis should not be self-certified by its producer.**

**Stato:** STRONGER.

---

### K. Research-first curation

DisMech impone una sequenza:

```text
research first
→ persist report/citations
→ consume scientifically
→ curate structured model
```

Questo è utile perché impedisce allo Scientist di costruire direttamente il modello da memoria del modello.

Per LEGEND può diventare:

```text
SOURCE SURFACES
→ EVIDENCE PACKETS
→ SYNTHESIS
```

non:

```text
prompt
→ disease model
```

**Stato:** STRONGER.

---

### L. Persist research artifacts prima della synthesis canonica

DisMech conserva:

- research reports;
- citation sidecars;
- provider artifacts;
- reference cache;
- history;
- hypotheses.

Questo rafforza una separazione importante:

```text
RAW / RESEARCH ARTIFACT
≠
CANONICAL SCIENTIFIC MODEL
```

Per LEGEND:

- input scientifici e derived evidence devono rimanere ispezionabili;
- la synthesis non deve cancellare il livello precedente.

**Stato:** STRONGER.

---

### M. Provider abstraction

DisMech può cambiare deep-research provider mantenendo una superficie downstream relativamente stabile.

Questo suggerisce che lo Scientist LEGEND non dovrebbe essere legato a un provider specifico.

Design:

```text
SCIENTIFIC ROLE
≠ MODEL
≠ PROVIDER
≠ RETRIEVAL ENGINE
```

Il provider diventa capability parametrica.

**Stato:** STRONGER.

---

### N. Ephemeral equivalent workers sono compatibili con curation rigorosa

DisMech usa general-purpose curators equivalenti e task-scoped.

Questo rafforza quanto già emerso da AutoScientists:

> il valore è nel contratto comune e nello scientific task, non nel nome permanente del worker.

**Stato:** STRONGER.

---

### O. Hierarchical synthesis con provenance preservata

DisMech comprime:

```text
research output
→ exact evidence
→ structured nodes
→ edges
→ hypotheses
```

senza affidarsi solo a summary prose.

Questo è molto utile per corpus grandi.

Il fan-in futuro di LEGEND dovrebbe quindi sintetizzare **evidence packets strutturati**, non migliaia di raw PDFs o narrative summaries.

**Stato:** STRONGER.

---

### P. Structured curation può essere il punto di fan-in tra molti lettori

Dopo Robin e AutoScientists restava aperto il problema:

> cosa fanno 50 deep readers dopo aver letto 50 paper?

DisMech offre una risposta promettente:

```text
N reader outputs
→ common evidence/claim schema
→ atomic mechanism graph
```

Quindi la memoria strutturata può diventare l'interfaccia tra:

- horizontal reading;
- cross-paper synthesis;
- review;
- incremental updates.

**Stato:** EMERGING / STRONGER.

---

### Q. Continuous research: scientific object persists, worker does not

DisMech conserva:

- disease YAML;
- hypotheses;
- research artifacts;
- Git history.

Questo rafforza:

> **persist the scientific object, not the conversational worker.**

Per LEGEND, il Scientist può morire dopo il task se:

- evidence packet;
- claims;
- hypotheses;
- review;
- provenance;
- status;

sono persistiti.

**Stato:** STRONGER.

---

## 19.2 Cosa DisMech indebolisce o mantiene non dimostrato

### Bounded-corpus completeness resta irrisolto

DisMech è molto forte downstream, ma non dimostra:

```text
50 supplied PDFs
→ 50/50 fully read
```

Quindi tre review su tre non risolvono questo punto.

La necessità di una nostra deterministic corpus layer diventa ancora più forte.

**Stato:** STRONGER REQUIREMENT.

---

### Deep-research report ≠ exhaustive corpus reading

Un provider può produrre un eccellente report e tuttavia non aver incluso un paper critico.

Quindi:

> **retrieval quality ≠ bounded-corpus completeness.**

**Stato:** STRONGER distinction.

---

### Horizontal pool per paper ancora non dimostrato end-to-end

DisMech dimostra worker equivalenti fino a 8 per disease tasks, ma non un elastic paper-reader pool.

Quindi `ScientistPool(N)` resta un design fortemente favorito, ma non ancora pienamente validato da una repo.

**Stato:** UNRESOLVED but increasingly supported.

---

### Permanent specialist hierarchy ulteriormente indebolita

DisMech fa molto con:

- generalist curator;
- skills;
- provider;
- validators;
- fresh reviewer.

Questo indebolisce ulteriormente la necessità di creare molti specialisti permanenti.

**Stato:** WEAKER.

---

# 20. Aggiornamento del disegno incrementale dopo Robin + AutoScientists + DisMech

## 20.1 Topologia scientifica provvisoria aggiornata

```text
                                  ORCHESTRATOR
                                       │
                        objective / priority / budget
                                       │
                               SCIENTIFIC TASK POOL
                                       │
                  ┌────────────────────┴─────────────────────┐
                  │                                          │
                  ▼                                          ▼
        GENERAL SCIENTIST POOL                         SPECIALIST MODES
        N ephemeral instances                         fresh / on-demand
                  │                                          │
        ┌─────────┼──────────┐               ┌───────────────┼──────────────┐
        │         │          │               │               │              │
        ▼         ▼          ▼               ▼               ▼              ▼
   deep read   evidence   inference      hostile        evidence       computational
              extraction  hypothesis     reviewer       verifier       scientist
        │
        ▼
   EVIDENCE PACKETS
        │
        ├── exact snippet
        ├── locator
        ├── SUPPORT/REFUTE
        ├── evidence source
        ├── epistemic type
        └── provenance
        │
        ▼
  ATOMIC CLAIM / MECHANISM LAYER
        │
        ├── nodes
        ├── edge-specific evidence
        ├── contradictions
        └── hypotheses
        │
        ▼
 HIERARCHICAL SYNTHESIS
        │
        ▼
 DETERMINISTIC VALIDATION
        │
        ▼
 FRESH HOSTILE REVIEW
        │
        ▼
 CANONICAL SCIENTIFIC STATE
        │
        ▼
 EXPERIMENT / NEXT QUESTION / DELTA UPDATE
```

---

# 21. General Scientist contract — aggiornamento dopo DisMech

## Capacità comuni ora più chiaramente supportate

Ogni General Scientist dovrebbe poter:

1. deep-read assigned full-text evidence;
2. inspect Methods, Results, figures, tables, supplements when available;
3. extract exact evidence;
4. record precise source identity;
5. classify evidence polarity:
   - SUPPORT;
   - REFUTE;
   - NO_EVIDENCE;
6. classify evidence source:
   - human;
   - model organism;
   - in vitro;
   - computational;
   - other;
7. distinguish:
   - observation;
   - author interpretation;
   - agent inference;
   - hypothesis;
8. identify negative evidence;
9. detect contradictions;
10. create atomic mechanistic claims;
11. avoid bundling unsupported causal steps;
12. attach evidence to causal edges separately from nodes;
13. generate stable hypotheses;
14. specify predictions/falsification conditions;
15. propose structured experiments;
16. use provider/tool capabilities;
17. produce machine-readable output;
18. persist provenance;
19. request fresh independent review when policy requires;
20. leave enough state for another Scientist to continue without its conversational history.

---

# 22. Evidence packet — aggiornamento dopo DisMech

Schema concettuale cumulativo:

```text
EVIDENCE_PACKET
    paper_id
    PMID
    DOI
    source_hash

    source_surface:
        page
        section
        figure
        panel
        table
        supplement

    verbatim_support
    paraphrased_claim

    epistemic_type:
        OBSERVATION
        AUTHOR_INTERPRETATION
        AGENT_INFERENCE
        HYPOTHESIS
        NEGATIVE_RESULT
        CONTRADICTION

    polarity:
        SUPPORT
        REFUTE
        NO_EVIDENCE

    evidence_source:
        HUMAN_CLINICAL
        MODEL_ORGANISM
        IN_VITRO
        COMPUTATIONAL
        OTHER

    directness:
        DIRECT
        INDIRECT
        UNASSESSED

    entity_context
    method_context
    limitations
    scientist_id
    review_status
```

**Nota:** DisMech rafforza in modo sostanziale polarity, evidence source, exact snippet e claim→evidence linkage. LEGEND dovrebbe aggiungere locator/surface completeness più rigorosi.

---

# 23. Mechanism representation — nuovo disegno emergente

DisMech rafforza la necessità di separare:

```text
NODE EVIDENCE
```

da:

```text
EDGE EVIDENCE
```

Possibile struttura:

```text
MECHANISM_NODE
    node_id
    biological_event
    context
    evidence[]

MECHANISM_EDGE
    source_node
    relation
    target_node
    edge_evidence[]
    confidence
    contradictions[]
```

### Nuova regola emergente

> **No causal edge may inherit support merely because its endpoint nodes are separately supported.**

**Stato:** ADOPT CANDIDATE.

---

# 24. Review architecture — aggiornamento dopo DisMech

## Stage 1 — deterministic verification

Software verifica:

- schema;
- identifiers;
- quote exactness;
- source hashes;
- locator validity;
- ontology existence;
- corpus completeness;
- task state.

## Stage 2 — fresh scientific review

Reviewer verifica:

- semantic source support;
- biological plausibility;
- missing mechanisms;
- overclaim;
- causal edges;
- entity appropriateness;
- contradictory evidence;
- under-consumption;
- synthesis completeness.

## Stage 3 — risk-based additional review

Solo per output critici:

- blinded second read;
- different-model reviewer;
- human adjudication.

### Principio rafforzato

> **Do not spend reviewer tokens rechecking deterministic facts.**

---

# 25. Synthesis architecture — aggiornamento dopo DisMech

Design ora più concreto:

```text
PAPER
  ↓
EVIDENCE PACKET
  ↓
CLAIM / ATOMIC EVENT
  ↓
MECHANISM CLUSTER
  ↓
CAUSAL PATHOGRAPH
  ↓
MECHANISTIC HYPOTHESIS
  ↓
EXPERIMENT
```

### Vantaggio

Consente:

- thousands-paper scaling;
- local updates;
- contradiction insertion;
- edge review;
- provenance;
- incremental re-synthesis;
- selective context retrieval.

---

# 26. Continuous research — aggiornamento dopo DisMech

La memoria persistente dovrebbe essere organizzata intorno a oggetti scientifici:

```text
SOURCE
EVIDENCE
CLAIM
NODE
EDGE
HYPOTHESIS
EXPERIMENT
REVIEW
```

non attorno a sessioni.

Quando arrivano nuovi paper:

```text
NEW SOURCE
→ evidence packet
→ match affected claims/nodes/edges/hypotheses
→ reopen only relevant synthesis
```

Il dependency mapping dovrebbe essere software; il significato scientifico resta agentico.

**Stato:** STRONGER.

---

# 27. Cumulative pattern ledger — aggiornamento dopo DisMech

| Pattern | Robin | AutoScientists | DisMech | Stato cumulativo |
|---|---|---|---|---|
| Multiple equivalent Scientists | partial | strong | equivalent curators 1–8 | **STRONGER** |
| Elastic ScientistPool(N) | absent | fixed roles | bounded 1–8, not paper pool | **UNRESOLVED but strongly favored** |
| Generalists + specialists | strong | strong | strong via modes/tools/reviewer | **STRONGER** |
| Fixed permanent named Scientists | weak | fixed implementation but fungible | ephemeral workers | **WEAKER** |
| Permanent specialist hierarchy | unnecessary | unnecessary | mostly absent | **WEAKER / likely reject** |
| Query-driven fan-out | strong | hypothesis-driven | search-driven/provider | **STRONGER as complementary mode** |
| Paper-level dynamic claiming | absent | experiment queue analogue | absent | **BUILD candidate / unresolved implementation** |
| Hypothesis-driven teams | partial | very strong | structured hypotheses | **STRONGER** |
| Self-regroup | limited | strong | not central | **STRONGER but not universal** |
| Bounded delegation | strong | strong | strong/capped | **STRONGER** |
| Recursive swarm | unnecessary | unnecessary | absent | **WEAKER** |
| Hierarchical synthesis | strong | experimental analogue | strong structured fan-in | **STRONGER** |
| Structured scientific memory | weak | experimental memory only | **very strong** | **STRONGER / ADOPT candidate** |
| Exact verbatim evidence | weak | absent | **strong** | **STRONGER requirement** |
| SUPPORT/REFUTE polarity | weak | KEEP/DISCARD experiment analogue | **native strong** | **STRONGER / ADOPT candidate** |
| Evidence-source typing | absent | absent | **native strong** | **EMERGING / ADOPT candidate** |
| Epistemic typing observation/inference/hypothesis | partial | hypothesis strong | partial | **LEGEND remains stronger; keep** |
| Edge-specific evidence | absent | absent | **strong** | **EMERGING / ADOPT candidate** |
| Atomic mechanistic nodes | absent | hypothesis teams | **strong** | **EMERGING / ADOPT candidate** |
| Stable hypothesis objects | partial | hypotheses + teams | **strong** | **STRONGER** |
| Structured experiment object | closed loop | executable experiments | **strong schema** | **STRONGER** |
| Fresh hostile reviewer | absent | distributed falsification | **strong/runtime demonstrated** | **STRONGER / ADOPT candidate** |
| Evidence verifier | partial | absent | **strong hybrid** | **STRONGER** |
| Producer ≠ validator | ranking separation | metric separation | **strong candidate/reviewer separation** | **STRONGER** |
| Deterministic full-text completeness | absent | absent | absent | **CRITICAL BUILD requirement** |
| Full-text surface inventory | absent | absent | absent/partial provider | **CRITICAL BUILD requirement** |
| Research-first workflow | strong retrieval | task/experiment first | **strong** | **STRONGER** |
| Persist raw research artifacts | run artifacts | logs/results | **strong** | **STRONGER** |
| Provider abstraction | limited | model/runtime separation partial | **strong multi-provider** | **STRONGER** |
| LIST/selective READ | progressive | strong | skills/cache/report selective | **STRONGER** |
| Multi-trajectory analysis | strong | parallel workers | possible providers/review | **BENCHMARK / STRONGER** |
| Agent judgment + deterministic aggregation | strong | metric feedback | validators + reviewer | **STRONGER** |
| Dead-end memory | limited | strong | hypotheses/history/refute | **STRONGER** |
| Runtime watchdog as Scientist role | not needed | monitor exists | deterministic tooling preferred | **REJECT** |
| Risk-based double reading | plausible | absent | absent | **UNRESOLVED / BENCHMARK** |
| Different-model review | plausible | unproven | fresh context, model diversity unproven | **UNRESOLVED / BENCHMARK** |
| Source→claim dependency index | absent | absent | partial via structured KB, no full delta engine | **EMERGING / BUILD candidate** |
| Scientific object persists; worker ephemeral | partial | strong pattern | **strong** | **STRONGER** |

---

# 28. Patterns strengthened specifically by convergence of all three reviews

## 28.1 General Scientist should remain broad

None of the three reviews supports a future architecture composed only of narrow specialist personas.

Convergence favors:

> **broad General Scientist contract + specialist modes/tools on demand.**

---

## 28.2 Multiple equivalent Scientists are useful, but identities should be fungible

AutoScientists and DisMech strongly support equivalent worker replication.

Robin does not contradict it.

Convergence:

> **horizontal parallelism is useful; permanent identity is not the reason it works.**

---

## 28.3 Deterministic software should own mechanical guarantees

All three reviews reinforce:

- scheduling;
- aggregation;
- validation;
- completeness;
- retries;
- worker lifecycle;
- source identity;

as software responsibilities.

---

## 28.4 Independent scientific judgment belongs after deterministic validation

Robin had incomplete review separation.
AutoScientists had distributed falsification.
DisMech demonstrates the clearest production pattern.

Current strongest design:

```text
Producer
→ deterministic validation
→ fresh independent hostile reviewer
```

---

## 28.5 Scientific memory must outlive the Scientist

Robin's prose memory is insufficient.
AutoScientists' dead-end/experiment memory is useful.
DisMech shows the strongest machine-readable scientific persistence.

Current direction:

> **scientific state lives in structured durable objects; agents are replaceable processors.**

---

# 29. New unresolved questions after DisMech

## UNRESOLVED — How much LinkML/ontology structure should LEGEND adopt?

DisMech demonstrates large value from structured schema and ontology normalization.

Open question:

- minimal schema;
- richer DisMech-like schema;
- graph model;
- hybrid.

Need benchmark against complexity and maintenance cost.

---

## UNRESOLVED — Should directness become mandatory?

DisMech supports directness but does not populate it universally.

LEGEND could make:

```text
DIRECT
INDIRECT
UNASSESSED
```

mandatory for important evidence.

Needs evaluation.

---

## UNRESOLVED — What exact source locator is sufficient?

DisMech exact snippet is strong but does not universally require:

- page;
- section;
- paragraph;
- panel;
- supplement.

LEGEND's exhaustive-reading goal likely needs a stronger locator contract.

---

## UNRESOLVED — How hierarchical should synthesis become?

DisMech gives strong schema-level hierarchy but mostly one curator performs fan-in.

At 5,000 papers, likely need several synthesis levels.

Still to benchmark against later Tier-1 repos.

---

## UNRESOLVED — Worktree isolation for ephemeral readers

DisMech shows task-scoped worktree isolation can work productively.

LEGEND's permanent worktree model failed operationally.

Open question:

> when is an ephemeral worktree actually needed for a read/curation task versus a simpler task sandbox?

Do not infer that worktree itself should disappear in every circumstance.

---

# 30. Current strongest Scientist design after three reviews

> **Still provisional. Updated by cumulative evidence.**

```text
ORCHESTRATOR
    │
    ▼
SCIENTIFIC TASK POOL
    │
    ▼
GENERAL SCIENTIST POOL (N elastic)
    │
    ├─ deep full-text reading
    ├─ figure/table/supplement scientific inspection
    ├─ evidence extraction
    ├─ SUPPORT / REFUTE
    ├─ evidence-source typing
    ├─ observation/inference/hypothesis separation
    ├─ atomic mechanistic claims
    ├─ edge-specific reasoning
    ├─ contradiction detection
    ├─ hypothesis generation
    └─ structured experiment proposal
    │
    ▼
EVIDENCE / CLAIM STORE
    │
    ▼
HIERARCHICAL MECHANISM SYNTHESIS
    │
    ▼
DETERMINISTIC VALIDATORS
    │
    ▼
FRESH HOSTILE REVIEWER
    │
    ▼
CANONICAL SCIENTIFIC STATE
    │
    ├─ mechanisms
    ├─ contradictions
    ├─ hypotheses
    ├─ experiments
    └─ provenance
    │
    ▼
NEXT SCIENTIFIC TASKS / COMPUTE / DELTA UPDATE
```

Parallel runtime support beneath:

```text
task claiming
completeness
source hashing
worker lifecycle
retry
provider limits
context retrieval
```

should be software.

---

# 31. Current top Scientist takeaways after three Tier-1 reviews

1. **Keep many equivalent General Scientists for speed.**
2. **Make N elastic and independent from role semantics.**
3. **Do not bind Scientist identity to permanent Git topology.**
4. **Use specialist modes only where scientific function genuinely differs.**
5. **Fresh hostile reviewer is now strongly supported.**
6. **Evidence verification should be hybrid: software exactness + agent semantic judgment.**
7. **Full-text completeness must be deterministic and external to Scientist self-report.**
8. **Every important claim should preserve exact source support.**
9. **Evidence should carry polarity: SUPPORT / REFUTE / NO_EVIDENCE.**
10. **Evidence source and epistemic type are separate dimensions.**
11. **Mechanistic nodes and causal edges need separate evidence.**
12. **Avoid bundled causal claims.**
13. **Hypotheses should be persistent objects with falsification conditions.**
14. **Experiment proposals should be structured and decision-oriented.**
15. **Research artifacts should survive separately from canonical synthesis.**
16. **Structured machine-readable scientific memory is preferable to report-only memory.**
17. **Workers may be ephemeral if scientific objects/provenance persist.**
18. **Use hierarchical fan-in for thousands of papers.**
19. **Global context should be selective; assigned evidence exhaustive.**
20. **Provider/model/tool choice should be parametrized, not fused to Scientist role.**
21. **Do not let reviewer tokens duplicate deterministic validators.**
22. **Preserve negative and contradictory evidence rather than collapsing it.**
23. **Use dynamic task claiming for heterogeneous paper lengths.**
24. **Separate throughput parallelism, hypothesis diversity and replication.**
25. **Keep current conclusions revisable as more Tier-1 reviews arrive.**


# 32. Review 04 — Gemma Curation Agents

Repository analizzata: `PavlidisLab/gemma-curation-agents-v1.1`

## 32.1 Nuovi spunti utili per gli Scientist LEGEND

### A. Deterministic-first + selective semantic escalation

Questa review rafforza molto un principio che era già emerso, ma qui è implementato in modo particolarmente pulito:

```text
deterministic scan / resolver / validator
→ semantic residue
→ specialist agent only if needed
→ review only if disputed
```

Il punto più trasferibile per LEGEND è:

> **non usare un Scientist per risolvere ciò che il software può risolvere prima; usa l'agente sul residuo semanticamente ambiguo.**

Esempi:

- sample structure;
- ontology exact match;
- duplicate detection;
- deterministic assignment constraints;
- source status;
- convergence bookkeeping;
- idempotency;
- watchdog;
- retry/resume.

**Stato:** STRONGER / ADOPT CANDIDATE.

### B. Per-item explicit state

Gemma mantiene uno stato esplicito per ogni unità di lavoro (`GseState`).

Per LEGEND, il corrispettivo naturale è:

```text
PaperTaskState
StudyState
EvidenceTaskState
ReviewTaskState
```

Questo è utile per parallelismo, resume, drop-out degli item completati, failure isolation, selective reprocessing e incremental update.

**Stato:** STRONGER.

### C. Cross-item batching

Gemma dimostra che si può ottenere throughput elevato senza creare necessariamente N Scientist permanenti:

```text
many independent work items
→ one batched model request
```

Per LEGEND questo suggerisce di distinguere `SCIENTIST IDENTITY` da `MODEL EXECUTION BATCHING`.

**Stato:** EMERGING / BENCHMARK.

### D. Converged-item dropout

Gemma smette di spendere risorse sugli item settled/converged.

```text
OPEN
→ resolved
→ removed from later expensive rounds
```

Per LEGEND, claims non controverse, paper validati, evidence packet stabili e ontology mappings certi non dovrebbero continuare a ricevere review aggiuntiva.

**Stato:** STRONGER.

### E. Bounded specialist fan-out

Quando la specializzazione ha confini semantici chiari, può essere un modulo bounded e non una gerarchia ricorsiva.

**Stato:** STRONGER.

### F. Challenger → Responder → Arbiter

Pattern:

```text
candidate
→ challenger
→ responder
→ arbiter only if disagreement remains
```

Interessante perché il costo cresce solo con l'incertezza. Da benchmarkare contro un semplice fresh hostile reviewer.

**Stato:** EMERGING / BENCHMARK.

### G. Strong model only on disagreement

Gemma usa escalation selettiva:

```text
LOW-UNCERTAINTY
→ cheap/deterministic path

HIGH-UNCERTAINTY
→ stronger model / independent review
```

**Stato:** STRONGER.

### H. Gold-blind comparison

La clean-slate comparison proposal riduce anchoring e contamination.

Possibili usi LEGEND:

- critical paper double read;
- major mechanism synthesis;
- blind benchmark;
- reviewer calibration.

**Stato:** EMERGING / BENCHMARK.

### I. Source accounting come stato esplicito

Gemma conserva `paper_is_fulltext` e `paper_status.jsonl`.

Per LEGEND il requisito deve essere più forte:

```text
expected
retrieved
fulltext
pages
figures
tables
supplements
failures
```

**Stato:** STRONGER.

### J. Human full-text fill come HUMAN_REQUIRED esplicito

Il pattern `--pause-for-papers` è particolarmente utile:

> **missing inaccessible source = explicit HUMAN_REQUIRED retrieval boundary, not silent degradation.**

**Stato:** ADOPT CANDIDATE.

### K. Selective section retrieval è task-dependent

Gemma privilegia Methods/Materials/Results per il proprio task.

Per LEGEND non va copiato come regola universale: il deep mechanistic reader deve mantenere accesso al paper completo.

> **section filtering is a capability, not a universal Reader rule.**

**Stato:** STRONGER distinction.

### L. Supplement token hygiene

Gli allegati vanno inventariati tutti, ma prose, numeric tables, images e raw datasets possono richiedere pipeline diverse.

**Stato:** STRONGER.

### M. Exact evidence schema

`FindingEvidence` rafforza la convergenza verso evidence object strutturati con quote, source, location, context, URL e highlight spans.

> **exact evidence should be a structured object, not a citation string.**

**Stato:** STRONGER.

### N. Ontology resolver chain con escalation

Pattern:

```text
exact deterministic match
→ dense/specialized resolver
→ agentic fallback only if needed
```

**Stato:** ADOPT CANDIDATE.

### O. Central common validation chain for all emitters

Pattern:

```text
many emitters
→ one invariant layer
```

Evita bypass e regole divergenti tra Scientist e skill.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

### P. Content-idempotent writes

Fingerprint/content identity evitano duplicati logici su retry.

Applicabile a evidence packets, claims e review records.

**Stato:** STRONGER.

### Q. Watchdog liveness come software

> **worker liveness must be runtime software.**

**Stato:** STRONGER / REJECT agent role.

### R. Resume fail-closed

Gemma mostra anche un anti-pattern: stato malformed che può essere trattato permissivamente.

Per LEGEND:

```text
CORRUPT_STATE
→ explicit block/recovery
```

mai silent fresh/drop.

**Stato:** REJECT pattern / new guarantee.

### S. Extra review concentrata sull'incertezza

Possibile policy:

```text
high confidence + deterministic validation
→ accept for synthesis

uncertain / conflict / high impact
→ independent review

still unresolved
→ arbiter / human
```

**Stato:** STRONGER.

## 32.2 Cosa Gemma indebolisce o mantiene non dimostrato

### General Scientist Pool non è dimostrato dalla repo

Gemma ottiene throughput con stage concurrency, batch API e specialist modules. Il pool generalista resta utile per LEGEND, ma non è l'unica tecnica di scaling.

**Stato:** UNRESOLVED implementation choice.

### Multi-agent debate universale è indebolito

Il debate sembra utile soprattutto sul residuo contestato.

**Stato:** WEAKER universal debate.

### Selective Methods/Results reading non è una best practice generale

**Stato:** REJECT as universal Reader policy.

### Fail-soft corruption handling non è accettabile per canonical science

**Stato:** REJECT.

# 33. Aggiornamento del disegno incrementale dopo quattro review

```text
SCIENTIFIC TASK POOL
        │
        ▼
PER-ITEM STATE
        │
        ├── deterministic preprocessing
        ├── source status
        ├── ontology/entity resolution
        ├── completeness
        └── task-local context
        │
        ▼
GENERAL SCIENTIST / SPECIALIST MODE
        │
        ▼
STRUCTURED EVIDENCE / CLAIM OUTPUT
        │
        ▼
COMMON VALIDATION CHAIN
        │
        ├── schema
        ├── locator
        ├── source
        ├── ontology
        ├── duplicate/idempotency
        └── state integrity
        │
        ▼
UNCERTAINTY ROUTER
        │
        ├── settled → synthesis
        │
        └── disputed
                ↓
        challenger / fresh reviewer
                ↓
        responder if needed
                ↓
        arbiter / human only if unresolved
```

# 34. Review architecture — aggiornamento dopo Gemma

```text
Stage 0 — deterministic validation
Stage 1 — ordinary scientific producer
Stage 2 — risk classifier / uncertainty detector
Stage 3 — fresh reviewer or challenger only if needed
Stage 4 — responder only if dispute is meaningful
Stage 5 — arbiter / human only if still unresolved
```

> **Review depth should scale with uncertainty and consequence, not be fixed for every scientific object.**

# 35. Context/token architecture — aggiornamento dopo Gemma

```text
GLOBAL STATE
→ retrieve only relevant slice

ASSIGNED PAPER
→ inspect deeply

SPECIALIST
→ receive only task-relevant context

REVIEWER
→ receive candidate + necessary evidence

ARBITER
→ only disputed packet
```

Aggiunte:

- batch equivalent calls;
- drop settled items;
- strongest model only for residue;
- supplement size gating;
- no whole-corpus context.

**Stato:** STRONGER.

# 36. Failure semantics — aggiornamento dopo Gemma

Silent degradation può essere tollerata solo per metadata opzionali non load-bearing.

Deve essere vietata per:

- source missing;
- evidence missing;
- corrupt state;
- claim dropped;
- unparsed critical paper.

Failure states espliciti:

```text
FAILED_RETRIEVAL
FAILED_PARSE
INCOMPLETE_SURFACE
CORRUPT_STATE
REVIEW_UNRESOLVED
HUMAN_REQUIRED
```

# 37. Cumulative pattern ledger — aggiornamento dopo Gemma

| Pattern | Robin | AutoScientists | DisMech | Gemma | Stato cumulativo |
|---|---|---|---|---|---|
| Multiple equivalent Scientists | partial | strong | equivalent curators | not native | **STRONGER but not sole scaling pattern** |
| Elastic ScientistPool(N) | absent | fixed | bounded | absent | **UNRESOLVED / favored for large corpus** |
| Per-item explicit state | partial | task/experiment state | disease/task state | **very strong** | **STRONGER** |
| Cross-item batching | partial | parallel workers | multi-disease dispatch | **strong** | **EMERGING / ADOPT candidate** |
| Generalists + specialists | strong | strong | strong | specialist-heavy | **STRONGER** |
| Bounded specialist fan-out | strong | bounded | skills/providers | **strong static five** | **STRONGER** |
| Recursive swarm | absent | unnecessary | absent | absent | **WEAKER / likely reject** |
| Dynamic claiming | absent | experiment queue | absent | absent | **BUILD candidate at large scale** |
| Converged-item dropout | partial | task completion | partial | **strong** | **EMERGING / ADOPT candidate** |
| Risk-based review | partial | partial | strong | **strong selective debate** | **STRONGER** |
| Challenger/responder/arbiter | absent | distributed falsification | reviewer loop | **strong** | **EMERGING / BENCHMARK** |
| Gold-blind comparison | absent | independent workers | fresh reviewer | **clean-slate proposer** | **EMERGING / BENCHMARK** |
| Strong model only for residue | implicit | model quality matters | fresh reviewer | **explicit escalation** | **STRONGER** |
| Fulltext source status | weak | absent | partial | **paper_status** | **STRONGER but completeness still missing** |
| Deterministic corpus completeness | absent | absent | absent | partial only | **CRITICAL BUILD requirement** |
| Human retrieval gate | absent | absent | possible manual | **pause-for-papers** | **ADOPT candidate** |
| Section-selective retrieval | strong | selective state | selected evidence | **strong task-specific** | **STRONGER as optional capability** |
| Universal selective sections | n/a | n/a | n/a | task-specific | **REJECT as universal rule** |
| Supplement token hygiene | partial | n/a | provider dependent | **strong** | **STRONGER** |
| Exact evidence object | partial | absent | strong | **strong** | **STRONGER** |
| Evidence polarity | weak | KEEP/DISCARD analogue | strong | absent general | **STRONGER from DisMech remains** |
| Edge-specific evidence | absent | absent | strong | absent | **ADOPT candidate remains** |
| Ontology normalization | absent | limited | strong | **very strong** | **STRONGER** |
| Deterministic-first resolver chain | partial | partial | strong | **very strong** | **ADOPT candidate** |
| Common invariant/validation chain | partial | metric gates | strong validators | **very strong** | **VERY STRONG / ADOPT candidate** |
| Idempotent writes | not central | partial | Git/state | **strong content fingerprint** | **STRONGER** |
| Resume | limited | strong | partial | **strong but permissive corruption** | **ADOPT with fail-closed hardening** |
| Watchdog | partial | monitor | software preferred | **strong watchdog** | **STRONGER** |
| Corrupt-state silent fallback | n/a | n/a | n/a | present | **REJECT** |
| Hierarchical synthesis | strong | experimental | structured | absent cross-paper | **STRONGER overall** |
| Structured scientific memory | weak | experiment memory | strong | curation state only | **STRONGER from DisMech** |
| Provider abstraction | limited | model/runtime | strong | provider-specific | **STRONGER but not universal** |
| Worker ephemeral | yes | yes-ish | yes | yes | **STRONGER** |
| Permanent specialist personas | unnecessary | unnecessary | unnecessary | absent | **WEAKER / likely reject** |
| Review only unresolved items | partial | partial | risk based | **strong** | **STRONGER** |

# 38. New open questions after Gemma

## UNRESOLVED — Can model batching replace some Scientist multiplicity?

Benchmark:

```text
N Scientist sessions
vs
batched equivalent task calls
```

su deep-reading quality, context isolation, latency e costo.

## UNRESOLVED — Challenger/responder/arbiter vs simple hostile reviewer

Confrontare qualità, token cost, anchoring e false-positive review rate.

## UNRESOLVED — Uncertainty routing

Definire regole misurabili per:

```text
SETTLED
DISPUTED
HIGH_IMPACT
NEEDS_REVIEW
```

## UNRESOLVED — Selective section retrieval vs full deep read

Da testare con ablation sul workload LEGEND.

# 39. Current top Scientist takeaways after four Tier-1 reviews

1. Keep a broad General Scientist contract.
2. Scale with equivalent workers where useful, but do not assume worker multiplicity is the only throughput primitive.
3. Treat model batching as a separate runtime optimization.
4. Maintain explicit per-item scientific state.
5. Use deterministic preprocessing before agentic interpretation.
6. Route only semantic residue to models.
7. Use bounded specialist modules, not recursive swarms.
8. Use one common deterministic validation chain for all emitters.
9. Drop settled items from later review rounds.
10. Escalate expensive models only on uncertainty/disagreement.
11. Keep source availability and degradation explicit.
12. Missing inaccessible full text should become explicit HUMAN_REQUIRED when required for completeness.
13. Do not use task-specific section filtering as universal deep-reading policy.
14. Inventory supplements deterministically and control token-heavy formats by modality.
15. Evidence must be a structured object with exact support.
16. Keep ontology/entity normalization mostly deterministic-first.
17. Use challenge/response/arbitration only where its incremental value beats simpler review.
18. Maintain content-idempotent scientific writes.
19. Worker liveness/watchdog belongs to software.
20. Resume/recovery must fail closed on corrupt scientific state.
21. Spend independent review on uncertain/high-impact outputs.
22. Preserve producer ≠ validator on canonical scientific conclusions.
23. Preserve structured machine-readable scientific memory.
24. Keep workers ephemeral when durable scientific objects survive.
25. Continue collecting patterns broadly now; adoption remains surgical later.


# 40. Review 05 — CORAL

Repository analizzata: `Human-Agent-Society/CORAL`

## 40.1 Nuovi spunti utili per gli Scientist LEGEND

### A. Fungible General Scientist Pool + specializzazione temporanea

CORAL rafforza molto il pattern:

> **worker equivalenti per throughput + specializzazione temporanea quando serve.**

La configurazione consente:

```text
agents.count = N
```

oppure assignments eterogenei con model/runtime/role diversi.

Il punto utile per LEGEND è:

```text
GENERAL SCIENTIST POOL
N fungible workers
```

con specializzazioni espresse come:

- role;
- posture;
- lane;
- ephemeral subagent;
- tool/capability.

Non come identità permanenti.

**Stato:** STRONGER.

---

### B. Lane ≠ posture

CORAL distingue:

- **lane** = su quale problema/tecnica si lavora;
- **posture** = che tipo di contributo si sta producendo.

Questa distinzione è utile per LEGEND perché evita di trasformare ogni funzione temporanea in un ruolo permanente.

Esempio:

```text
Scientist instance
lane = WWOX mitochondrial mechanism
posture = Researcher
```

poi:

```text
same Scientist contract
lane = same mechanism
posture = Reviewer
```

o un'altra istanza fresca.

**Stato:** EMERGING / ADOPT CANDIDATE.

---

### C. Deep Researcher come ephemeral specialist

CORAL implementa un `deep-researcher` specializzato che può essere invocato quando emerge un knowledge gap.

Pattern:

```text
parent Scientist
→ targeted research need
→ deep-researcher
→ raw sources + research note
→ grounding check
→ reintegration
```

Per LEGEND questo rafforza il design:

> specialisti di ricerca possono essere **modalità effimere**, non attori permanenti.

**Stato:** STRONGER.

---

### D. Librarian: separare housekeeping da semantic curation

CORAL introduce anche un `librarian`.

La lezione utile non è “creare un Librarian agent permanente”.

È:

- indexing;
- dedup candidates;
- note organization;
- schema checks;
- file layout;

→ software.

Solo:

- ambiguous semantic merge;
- conflicting scientific note interpretation;

→ curator/Scientist.

**Stato:** STRONGER.

---

### E. Immutable raw-source persistence

Uno dei pattern più forti di CORAL:

```text
source
→ save raw
→ synthesize
→ review
```

Il raw source non dovrebbe essere perso o sovrascritto dalla sintesi.

Per LEGEND:

```text
RAW SOURCE
≠ EVIDENCE PACKET
≠ CLAIM
≠ SYNTHESIS
```

e tutti i livelli load-bearing devono essere recuperabili.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### F. Grounding checker deterministico

CORAL aggiunge `check_grounding.py` per controlli come:

- orphan findings;
- broken source links;
- broken coverage links;
- missing raw-source metadata;
- high-confidence note without review.

Questo rafforza:

> **grounding structure should be linted deterministically.**

Il Reviewer non deve controllare:

- link esistente;
- raw source presente;
- metadata obbligatori;
- review artifact presente.

**Stato:** STRONGER.

---

### G. Independent per-claim grounding review

Il Synthesis Reviewer verifica ogni substantive claim contro i raw sources e assegna:

```text
grounded
partially-grounded
inferred
contradicted
unverifiable
```

Questo è molto interessante per LEGEND perché aggiunge una review più granulare del semplice “report approvato”.

Possibile mapping:

```text
CLAIM
→ fresh reviewer
→ SUPPORT STATUS
```

con quote di supporto.

**Stato:** STRONGER / ADOPT CANDIDATE.

---

### H. High-confidence claim should require review artifact

CORAL introduce una regola particolarmente interessante:

> un output ad alta confidenza dovrebbe avere evidence/review separata.

Per LEGEND:

```text
confidence = HIGH
```

potrebbe richiedere:

```text
review_status = VERIFIED
```

oppure un diverso evidence threshold.

**Stato:** EMERGING / BENCHMARK.

---

### I. Structured note graph

CORAL conserva frontmatter strutturato con elementi come:

- claim;
- status;
- confidence;
- based_on;
- evidence;
- supersedes;
- refutes;
- next.

Questo rafforza molto la direzione già emersa con DisMech:

> **scientific memory should be graph-like and lineage-aware.**

Particolarmente utili:

```text
supersedes
refutes
based_on
```

per non perdere evoluzione e contraddizioni.

**Stato:** STRONGER.

---

### J. Supersede / refute invece di overwrite

CORAL evita che una nuova sintesi cancelli il passato.

Pattern:

```text
old claim
→ superseded_by new claim
```

oppure:

```text
claim A
↔ refutes
claim B
```

Questo è molto importante per LEGEND:

> **scientific state should evolve non-destructively.**

**Stato:** ADOPT CANDIDATE.

---

### K. Consolidation heartbeat

CORAL usa un heartbeat di knowledge consolidation.

Quando esistono diverse note correlate:

```text
3+ related notes
→ synthesis
→ connections
→ open questions
```

Per LEGEND questo suggerisce una possibile **synthesis trigger policy**:

- non sintetizzare dopo ogni singolo paper;
- sintetizzare quando:
  - cluster reaches threshold;
  - contradictions appear;
  - new high-impact evidence arrives;
  - mechanism neighborhood changes materially.

**Stato:** EMERGING / BENCHMARK.

---

### L. Persistent open questions

CORAL mantiene `_open-questions.md`.

Questo è un pattern molto forte:

> **incertezza scientifica deve essere un artefatto persistente, non solo testo dentro una conclusion.**

Per LEGEND:

```text
OPEN_QUESTION
reason
supporting evidence
blocking uncertainty
next evidence needed
```

**Stato:** STRONGER.

---

### M. Contradiction preservation

CORAL rafforza la convergenza già vista in DisMech:

- `refutes`;
- contradicted;
- open questions;
- do-not-merge contradictions.

Quindi:

> **contradictions should remain first-class unresolved scientific state.**

**Stato:** STRONGER.

---

### N. Exact-commit grader separation

CORAL ha un pattern molto forte per computational science:

```text
candidate
→ exact commit
→ isolated grader
→ score/feedback
```

Il producer non può modificare retroattivamente ciò che viene valutato.

Per LEGEND questo è molto utile quando lo Scientist produce:

- code;
- analysis;
- computational experiment;
- statistical output;
- model.

**Stato:** STRONGER / ADOPT CANDIDATE for computational work.

---

### O. Grader error ≠ candidate failure

CORAL separa:

```text
EVALUATOR FAILURE
```

da:

```text
SCIENTIFIC CANDIDATE FAILURE
```

Questa distinzione è essenziale.

Un errore del reviewer/tool/runtime non deve diventare automaticamente:

> “hypothesis false”.

**Stato:** STRONGER.

---

### P. Computational hypothesis loop

CORAL offre un loop molto forte:

```text
hypothesis
→ implementation / computational experiment
→ exact candidate
→ grader
→ score / diagnostics
→ reflect
→ next hypothesis
```

Questo rafforza Robin e AutoScientists sul punto:

> Scientist should be able to progress from literature inference to executable computational falsification.

**Stato:** STRONGER.

---

### Q. Reflect / consolidate / pivot triggers

CORAL usa trigger espliciti per:

- reflect;
- consolidate;
- pivot on plateau.

Per LEGEND questo suggerisce che non tutte le iterazioni devono essere libere.

Il runtime può attivare un scientific prompt specifico quando:

```text
plateau detected
contradiction density rises
queue stalls
enough evidence accumulated
```

**Stato:** EMERGING / BENCHMARK.

---

### R. Raw sources + notes reduce conversational memory dependence

CORAL dimostra bene:

> **knowledge should live outside the model context.**

Gli agenti possono restart/resume e recuperare:

- raw sources;
- research notes;
- synthesis;
- experiments;
- attempts.

Questo rafforza:

```text
worker ephemeral
scientific memory durable
```

**Stato:** STRONGER.

---

### S. Equivalent worker count is deployment policy

CORAL supporta realmente `count=N`.

Questa è una delle conferme più chiare del nostro design:

> **N non deve essere una proprietà semantica del ruolo Scientist.**

Può essere:

```text
N=3
N=10
N=50
```

in funzione di:

- workload;
- provider capacity;
- synthesis capacity;
- review capacity;
- budget.

**Stato:** STRONGER.

---

### T. Mixed model/runtime pool

CORAL permette worker eterogenei:

- stronger model for research/synthesis;
- cheaper model for implementation/execution;
- runtime diversification.

Per LEGEND:

```text
ROLE
≠ MODEL
≠ RUNTIME
```

e la selezione può essere task-dependent.

**Stato:** STRONGER.

---

### U. Process runtime stronger than scientific task allocation

CORAL dimostra un punto importante:

- process spawning;
- worktrees;
- restart;
- heartbeat;
- grader;

sono maturi.

Ma la paper allocation resta soft/advisory.

Questo rafforza:

> **runtime scalability and scientific workload scalability are separate problems.**

**Stato:** STRONGER distinction.

---

### V. Advisory claims are insufficient at corpus scale

CORAL usa soft/advisory claims.

Per 50 o 5,000 paper non basta.

Serve:

```text
READY
→ atomic CLAIMED
→ IN_PROGRESS
→ DONE / FAILED / STALE
```

**Stato:** STRONGER BUILD requirement.

---

### W. Figure-loss visibility is useful even before figure understanding exists

CORAL esplicita che figure/equations can be lost and usa placeholder.

Questo è un pattern importante:

> **known missing surface must remain visible.**

Per LEGEND:

```text
FIGURE_PRESENT
FIGURE_NOT_PARSED
FIGURE_NOT_INSPECTED
```

è meglio di fingere che il paper sia stato letto interamente.

**Stato:** STRONGER.

---

## 40.2 Cosa CORAL indebolisce o mantiene non dimostrato

### Search-driven coverage ≠ corpus completeness

CORAL `_coverage.md` misura research dimensions, non papers.

Questo rafforza ulteriormente:

> **conceptual coverage ≠ document coverage.**

**Stato:** STRONGER distinction.

---

### Warm-start all-agent research può duplicare token

Molti agenti che fanno research warm start possono cercare le stesse fonti.

Quindi il parallelismo iniziale deve essere benchmarkato rispetto a:

- overlap;
- duplicate retrieval;
- marginal coverage.

**Stato:** BENCHMARK.

---

### Synthesis Reviewer non è ancora universal hostile review

È forte per grounding, ma non equivale a:

- alternative mechanism attack;
- causal falsification;
- missing biology search.

Quindi le tre review functions restano distinte.

**Stato:** STRONGER distinction.

---

### Soft claim coordination non scala

Per piccolo team può funzionare.

Per 50/500/5000 paper no.

**Stato:** REJECT at scale.

---

### Generic web search non sostituisce biomedical retrieval substrate

CORAL ha WebSearch/WebFetch ma non integra nativamente PubMed/PMC/HPO/Monarch ecc.

Questo rafforza:

> **runtime tool flexibility ≠ scientific substrate quality.**

**Stato:** STRONGER distinction.

---

# 41. Aggiornamento del disegno incrementale dopo cinque review

```text
                         ORCHESTRATOR
                              │
                              ▼
                    SCIENTIFIC TASK POOL
                              │
                              ▼
                     PER-ITEM STATE
                              │
               ┌──────────────┼───────────────┐
               │              │               │
               ▼              ▼               ▼
       source manifest   deterministic    relevant context
       completeness      preprocessing    retrieval
               │              │               │
               └──────────────┼───────────────┘
                              ▼
                    GENERAL SCIENTIST POOL
                      N fungible instances
                              │
                              ├── deep reading
                              ├── evidence extraction
                              ├── inference
                              ├── hypothesis
                              └── optional specialist delegation
                              │
                              ▼
                      RAW SOURCE STORE
                              │
                              ▼
                      EVIDENCE PACKETS
                              │
                              ▼
                      CLAIM / NOTE GRAPH
                 based_on / refutes / supersedes
                              │
                              ▼
                    COMMON VALIDATION CHAIN
                              │
                              ▼
                      UNCERTAINTY ROUTER
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
              settled                 high-risk/disputed
                 │                         │
                 ▼                         ▼
             synthesis              fresh verifier/reviewer
                 │                         │
                 └────────────┬────────────┘
                              ▼
                    HIERARCHICAL SYNTHESIS
                              │
                              ├── mechanism
                              ├── contradiction
                              ├── open questions
                              └── hypotheses
                              │
                              ▼
                  COMPUTE / EXPERIMENT LOOP
                              │
                              ▼
                      exact candidate
                              │
                              ▼
                         grader
                              │
                              ▼
                  reflect / consolidate / pivot
```

---

# 42. Review architecture — aggiornamento dopo CORAL

Ora abbiamo quattro review semantics distinte:

## 42.1 Grounding verification

```text
Does the source support the claim?
```

CORAL Synthesis Reviewer rafforza questa funzione.

## 42.2 Hostile scientific review

```text
Is the interpretation scientifically defensible?
```

DisMech resta il riferimento più forte.

## 42.3 Ranking / evaluator

```text
Which candidate performs better?
```

Robin/CORAL supportano bene questa funzione.

## 42.4 Computational falsification

```text
Does the hypothesis survive an executable test?
```

CORAL/AutoScientists/Robin rafforzano questa funzione.

Queste quattro funzioni non vanno fuse in un singolo “Reviewer”.

---

# 43. Knowledge architecture — aggiornamento dopo CORAL

Nuovo design cumulativo:

```text
RAW SOURCE
→ EVIDENCE PACKET
→ CLAIM
→ CLAIM LINKS
    based_on
    supports
    refutes
    supersedes
→ MECHANISM NODE
→ MECHANISM EDGE
→ HYPOTHESIS
→ EXPERIMENT
→ REVIEW
```

Open questions e contradictions restano first-class.

---

# 44. Scaling architecture — aggiornamento dopo CORAL

Convergenza:

## 50 papers

- N generalists;
- dynamic queue;
- bounded review;
- local synthesis.

## 500 papers

- hierarchical synthesis;
- source/claim index;
- batching;
- risk-based review;
- stronger dependency mapping.

## 5,000 papers

- deterministic corpus layer mandatory;
- elastic pool;
- provider backpressure;
- sharded synthesis;
- structured memory;
- incremental delta engine.

### Nuovo principio

> **process parallelism is easy; scientific state fan-in is the real scaling problem.**

---

# 45. Cumulative pattern ledger — aggiornamento dopo CORAL

| Pattern | Robin | AutoScientists | DisMech | Gemma | CORAL | Stato cumulativo |
|---|---|---|---|---|---|---|
| Multiple equivalent Scientists | partial | strong | equivalent curators | not native | **strong configurable pool** | **STRONGER** |
| Elastic ScientistPool(N) | absent | fixed | bounded | absent | **configurable count** | **STRONGER but scientific queue still missing** |
| Worker identity as role semantics | unnecessary | fungible | ephemeral | ephemeral | fungible | **WEAKER / reject permanent identity** |
| Temporary specialization | strong capabilities | teams | modes/tools | bounded specialists | **roles/postures/subagents** | **STRONGER** |
| Lane ≠ posture | n/a | partial | n/a | n/a | **explicit** | **EMERGING** |
| Per-item explicit state | partial | strong | task/disease | very strong | note/focus/attempt state | **STRONGER** |
| Raw source persistence | partial | limited | strong research artifacts | paper context/status | **strong immutable raw** | **VERY STRONG** |
| Exact evidence object | partial | absent | strong | strong | reviewer quotes/raw links | **STRONGER** |
| Grounding checker | partial | metric checks | validators | common chains | **explicit check_grounding** | **STRONGER** |
| Independent per-claim grounding | partial | absent | semantic review | partial | **strong Synthesis Reviewer** | **STRONGER** |
| Hostile scientific review | weak | falsification | **strong** | candidate challenge | partial posture | **STRONGER overall** |
| Ranking/evaluation | strong | metric | review-driven | eval package | **exact-commit grader** | **STRONGER** |
| Computational falsification | strong loop | strong | proposed experiment | absent | **strong** | **STRONGER** |
| Open questions as persistent state | partial | dead ends | gaps/hypotheses | stuck items | **strong** | **STRONGER** |
| Contradiction preservation | partial | falsified hypotheses | REFUTE | debate/stuck | **refutes/open questions** | **STRONGER** |
| Supersede instead of overwrite | partial | memory | Git/history | rerun state | **explicit supersedes** | **EMERGING / ADOPT candidate** |
| Consolidation trigger | hierarchical | regrouping | synthesis | stage fan-in | **heartbeat consolidate** | **EMERGING / BENCHMARK** |
| Dynamic paper claiming | absent | task queue analogue | absent | absent | advisory only | **CRITICAL BUILD requirement** |
| Advisory claims | n/a | stronger queue | issue claim | futures | **soft claim** | **REJECT at scale** |
| Cross-item batching | partial | parallel | dispatch | **strong** | process/runtime parallelism | **STRONGER** |
| Mixed model pool | partial | model matters | provider abstraction | model tiers | **strong assignments** | **STRONGER** |
| Strong model only for residue | implicit | partial | reviewer | strong | researcher stronger model pattern | **STRONGER** |
| Fulltext completeness | absent | absent | absent | absent | absent | **CRITICAL BUILD requirement** |
| Figure completeness | absent | absent | partial | absent | explicitly missing | **CRITICAL BUILD requirement** |
| Human retrieval gate | absent | absent | possible | strong pause | not native | **ADOPT candidate remains** |
| Hierarchical synthesis | strong | team synthesis | structured | absent cross-paper | **strong notes→synthesis** | **STRONGER** |
| Structured scientific memory | weak | experiment memory | strong | curation state | **structured note graph** | **STRONGER** |
| Biomedical ontology normalization | absent | limited | strong | strong | absent | **VALUE CONFIRMED but repo-dependent** |
| Common invariant chain | partial | metric gates | validators | **very strong** | grounding/checks | **VERY STRONG** |
| Watchdog/restart software | partial | monitor | software | watchdog | **strong AgentManager** | **STRONGER** |
| Exact-commit evaluation | n/a | experiment metrics | no | no | **strong** | **EMERGING / ADOPT computationally** |
| Evaluator failure ≠ candidate failure | implicit | partial | review separate | audit state | **explicitly strong** | **STRONGER** |
| Process scalability ≠ scientific scaling | implicit | partial | provider bottleneck | batch bottleneck | **very clear** | **STRONGER distinction** |

---

# 46. New open questions after CORAL

## UNRESOLVED — Should lane/posture be explicit Scientist parameters?

Potential fields:

```text
TASK_LANE
POSTURE
```

Need test whether this improves diversity without adding cognitive overhead.

---

## UNRESOLVED — How often should synthesis heartbeat run?

Candidates:

- after N papers;
- after evidence density threshold;
- after contradiction appears;
- after mechanism cluster changes.

Needs empirical benchmark.

---

## UNRESOLVED — Per-claim grounding review threshold

Potential policy:

```text
HIGH confidence
CAUSAL
THERAPEUTIC
CONTRADICTORY
LOAD-BEARING
```

→ mandatory fresh verification.

Need optimize cost/benefit.

---

## UNRESOLVED — Multi-island exploration

CORAL supports multi-island execution.

Potentially useful for:

- competing mechanism models;
- independent hypothesis teams.

But likely too complex for default LEGEND Reader.

**Stato:** WATCH only.

---

# 47. Current top Scientist takeaways after five Tier-1 reviews

1. Keep many fungible General Scientists for throughput.
2. Make worker count deployment policy, not role semantics.
3. Use temporary specialization via mode/posture/lane/capability.
4. Keep raw sources immutable and recoverable.
5. Persist scientific memory outside worker context.
6. Maintain per-item explicit state.
7. Use dynamic atomic work claiming at corpus scale.
8. Keep process runtime deterministic and separate from scientific allocation.
9. Make evidence packets structured and source-backed.
10. Add independent per-claim grounding for high-impact claims.
11. Keep grounding review distinct from hostile scientific review.
12. Keep ranking/evaluation distinct from scientific review.
13. Keep computational falsification as a separate scientific verification channel.
14. Preserve contradictions and open questions explicitly.
15. Prefer supersede/refute over destructive overwrite.
16. Use hierarchical synthesis for large corpora.
17. Consider synthesis triggers rather than continuous global resynthesis.
18. Use mixed models/runtimes only where benchmarked value exists.
19. Keep strongest models for high-uncertainty/high-value reasoning.
20. Keep housekeeping/indexing/liveness in software.
21. Do not use advisory claims for exhaustive 50/500/5000-paper work.
22. Process parallelism alone does not solve scientific scaling.
23. Full-text/figure/table/supplement completeness remains a critical missing primitive across all reviewed repos.
24. Scientific state fan-in is emerging as the principal scaling bottleneck.
25. Continue broad best-practice census now; final LEGEND adoption remains minimal and surgical.


# 48. Review 06 — Paperclip

Repository analizzata: `paperclipai/paperclip`

## 48.1 Nuovi spunti utili per gli Scientist LEGEND

### A. Durable task ownership deve restare fuori dal Scientist

Paperclip rafforza in modo molto forte:

```text
task identity
checkout
run ownership
locks
retry/recovery
blockers
idempotency
```

come responsabilità del control plane, non del reasoning agent.

Per LEGEND questo significa che il Scientist dovrebbe ricevere un task già definito e posseduto deterministicamente, senza dover ragionare su:

- chi lo possiede;
- se è duplicato;
- se può essere ritentato;
- se il worker precedente è morto;
- quale run è authoritative.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### B. Immutable/hash-backed raw source

Il pattern LLM Wiki:

```text
captured source
→ content hash
→ raw immutable source
→ source metadata
```

rafforza ulteriormente CORAL e DisMech.

Per LEGEND ogni fonte dovrebbe avere:

```text
SOURCE_ID
CONTENT_HASH
RAW_ARTIFACT
SOURCE_METADATA
```

indipendentemente dal modello che la leggerà.

**Stato:** VERY STRONG.

---

### C. Source identity deve essere indipendente dal Scientist

Paperclip mostra bene che:

> il worker può cambiare, ma la source identity non cambia.

Questo è un principio molto utile:

```text
Scientist instance is replaceable
Source identity is durable
```

**Stato:** STRONGER.

---

### D. Incremental source-driven knowledge maintenance

Il Wiki segue:

```text
new source
→ ingest
→ update entities/concepts/synthesis
→ preserve contradictions
→ revision metadata
```

Questo è utile per LEGEND perché conferma che la memoria scientifica deve poter essere aggiornata incrementalmente, non ricostruita da zero.

**Stato:** STRONGER.

---

### E. Revisioned scientific state

Paperclip mantiene revision metadata e atomic page writes.

Per LEGEND:

```text
CLAIM / SYNTHESIS
→ revision history
```

deve essere preferibile a overwrite distruttivo.

**Stato:** STRONGER.

---

### F. Contradiction-preserving updates

Paperclip esplicitamente evita silent overwrite delle contraddizioni.

Questo rafforza il pattern già forte da DisMech/CORAL:

> **new evidence may refute or complicate old knowledge without deleting it.**

**Stato:** STRONGER.

---

### G. Source→entity→concept→synthesis hierarchy

La topologia Wiki:

```text
raw source
→ source page
→ entity/concept
→ synthesis
```

rafforza il principio di hierarchical fan-in.

Per LEGEND il corrispettivo scientifico potrebbe essere:

```text
source
→ evidence packet
→ claim
→ mechanism entity/edge
→ synthesis
```

**Stato:** STRONGER.

---

### H. Single knowledge-maintainer is an anti-pattern at scale

Paperclip ha un solo Wiki Maintainer che:

- reads;
- integrates;
- synthesizes;
- lints.

Per high-rigor science questo crea:

- correlated error;
- throughput bottleneck;
- producer=validator;
- synthesis bottleneck.

Quindi:

> **single long-lived producer+integrator+linter should not be copied.**

**Stato:** REJECT.

---

### I. Scientific independence is weaker than operational independence

Paperclip è fortissimo su:

```text
producer task
≠ control-plane validator
```

ma debole su:

```text
producer scientific interpretation
≠ independent scientific validator
```

Questo rafforza una distinzione già emersa:

> **operational correctness ≠ scientific validity.**

**Stato:** STRONGER distinction.

---

### J. Generic lint ≠ evidence verification ≠ hostile review

`wiki-lint` controlla:

- contradictions;
- provenance;
- stale claims;
- weak links.

Ma non sostituisce:

- evidence verifier;
- hostile scientific reviewer.

**Stato:** STRONGER distinction.

---

### K. End-to-end read instruction is not proof of completeness

Il Wiki skill dice “read end to end; do not skim”.

Ma questo resta prompt-level.

Per LEGEND:

> **declared deep-reading instruction ≠ deterministic reading receipt.**

**Stato:** STRONGER requirement.

---

### L. External preprocessing can dominate scientific quality

Paperclip riceve `contents: string`.

Quindi per PDFs:

```text
quality of parser / extraction
```

può contare più del wrapper agentico.

Questo rafforza:

> **document substrate quality is a first-order scientific variable.**

Per LEGEND vanno benchmarkati:

- PDF parser;
- JATS/XML;
- figures;
- tables;
- supplements.

**Stato:** STRONGER.

---

### M. Plugin/tool boundary è utile

Paperclip ha un buon capability boundary.

Questo rafforza il principio:

```text
Scientist role
≠ capability implementation
```

Per LEGEND:

- PubMed;
- PMC;
- DOI resolver;
- ontology;
- statistics;
- figure parser;
- bioinformatics;

dovrebbero essere modular capabilities.

**Stato:** STRONGER.

---

### N. Generic task decomposition is reusable, scientific decomposition no

Paperclip può creare child tasks, blockers e fan-in.

Questo è utile, ma non definisce:

- scientific child types;
- evidence semantics;
- bounded research recursion.

Quindi:

> **reuse decomposition mechanics, not generic task semantics as scientific protocol.**

**Stato:** STRONGER distinction.

---

### O. Blockers separate from hierarchy

Paperclip distingue child hierarchy e blockers.

Questo è utile per LEGEND:

```text
task A depends on B
```

non deve implicare che B sia “subordinate Scientist”.

Scientific dependency e organizational hierarchy sono cose diverse.

**Stato:** EMERGING / ADOPT CANDIDATE.

---

### P. Compact heartbeat/context deltas

Paperclip usa compact context/inbox-lite/cursor windows.

Questo rafforza:

> **worker should receive delta/context slice, not whole history.**

**Stato:** STRONGER.

---

### Q. Persistent application state ≠ portable scientific state

Paperclip Wiki state vive in folder + DB.

Se si clona solo il repo, la knowledge state non segue automaticamente.

Per LEGEND:

> **scientific state must be explicitly exportable/portable, not merely durable on one deployment.**

**Stato:** STRONGER requirement.

---

### R. Scientific omission can hide behind runtime success

Paperclip conferma ancora:

```text
run = success
```

non significa:

```text
all scientific evidence = processed
```

Il rischio dominante resta:

> **scientific omission without runtime failure.**

**Stato:** VERY STRONG.

---

### S. Dynamic pool needs shared compatible-task claim semantics

Paperclip ha forte ownership, ma non un vero:

```text
READY_SCIENCE_TASKS
→ next compatible Scientist claims
```

Quindi la nostra idea di pool continua a richiedere:

- capability compatibility;
- dynamic claiming;
- explicit task state.

**Stato:** STRONGER BUILD requirement.

---

### T. Manual agent cloning ≠ elastic Scientist Pool

Paperclip può duplicare agent config.

Questo non equivale a:

```text
ScientistPool(size=N)
```

con auto-scaling/load balancing.

**Stato:** STRONGER distinction.

---

## 48.2 Cosa Paperclip indebolisce o lascia unresolved

### Markdown-only knowledge store non scala come canonical science

Markdown è leggibile e ottimo come human surface.

Ma a 500/5000 papers:

- claim identity;
- dedup;
- dependency graph;
- ontology;
- evidence links;

richiedono struttura più forte.

**Stato:** REJECT as sole canonical store.

---

### Single-maintainer semantic integration non scala

**Stato:** REJECT.

---

### Generic plugin flexibility non prova scientific quality

Plugin modularity è utile, ma:

> più tools disponibili ≠ migliore scienza.

**Stato:** STRONGER benchmark requirement.

---

### Provider-neutral runtime non implica provider-neutral scientific quality

**Stato:** UNRESOLVED / BENCHMARK.

---

# 49. Aggiornamento del disegno incrementale dopo sei review

```text
SCIENTIFIC SOURCE LAYER
    │
    ├── stable source ID
    ├── content hash
    ├── raw artifact
    └── document-object inventory
    │
    ▼
SCIENTIFIC TASK LAYER
    │
    ├── durable task ID
    ├── atomic claim
    ├── blocker/dependency
    ├── retry/recovery
    └── worker compatibility
    │
    ▼
GENERAL SCIENTIST POOL
    │
    ├── fungible worker
    ├── bounded context
    ├── mode/posture
    └── tools/capabilities
    │
    ▼
EVIDENCE / CLAIM LAYER
    │
    ├── evidence packet
    ├── epistemic type
    ├── source polarity
    ├── claim identity
    ├── refutes
    ├── supersedes
    └── revision history
    │
    ▼
COMMON VALIDATION
    │
    ▼
RISK / UNCERTAINTY ROUTER
    │
    ├── evidence verifier
    ├── hostile reviewer
    └── computational evaluator
    │
    ▼
HIERARCHICAL SYNTHESIS
    │
    ▼
PORTABLE SCIENTIFIC STATE
```

---

# 50. Cumulative pattern ledger — aggiornamento dopo Paperclip

| Pattern | Robin | AutoScientists | DisMech | Gemma | CORAL | Paperclip | Stato cumulativo |
|---|---|---|---|---|---|---|---|
| Fungible generalists | partial | strong | curators | not native | strong | configurable generic agents | **STRONGER** |
| Elastic ScientistPool(N) | absent | partial | bounded | absent | partial | manual clone only | **UNRESOLVED but favored** |
| Durable task ownership | partial | task claims | partial | stage state | strong runtime | **very strong** | **VERY STRONG** |
| Atomic paper claiming | absent | task analogue | absent | absent | absent/advisory | absent shared-pool | **CRITICAL BUILD** |
| Blockers separate from hierarchy | n/a | partial | n/a | n/a | partial | **strong** | **EMERGING** |
| Immutable raw source | partial | weak | strong | partial | **strong** | **strong hash-backed** | **VERY STRONG** |
| Source hash identity | weak | absent | partial | content fingerprints | partial | **strong** | **STRONGER** |
| Source→knowledge hierarchy | strong | partial | strong | local proposal | strong notes | **strong wiki** | **STRONGER** |
| Contradiction preservation | partial | dead ends | REFUTE | debate | strong | **strong** | **VERY STRONG** |
| Revision history | partial | experiment history | Git/history | run merge | supersede | **page revisions** | **STRONGER** |
| Producer≠scientific validator | weak | partial | strong | strong candidate review | grounding selective | weak | **NEEDS explicit review layer** |
| Generic lint | n/a | n/a | validator | strong | grounding | **wiki-lint** | **useful but not review** |
| Evidence verifier | partial | absent | strong | partial | strong grounding | absent | **STRONGER requirement** |
| Hostile reviewer | weak | falsification | strong | candidate challenge | partial | absent | **STRONGER requirement** |
| External document substrate importance | PaperQA strong | low | provider | BioLit | parser/tool | **very clear** | **VERY STRONG** |
| Plugin/tool modularity | limited | capability layer | strong | modules | strong runtime | **strong** | **STRONGER** |
| Permanent specialist actors | unnecessary | unnecessary | unnecessary | absent | temporary | wiki maintainer anti-pattern | **WEAKER / reject** |
| Single semantic integrator | not central | teams | curator | proposer | synthesis task | **single maintainer** | **REJECT at scale** |
| Markdown-only canonical state | reports | logs | structured YAML | JSONL | structured notes | **Wiki Markdown** | **REJECT alone** |
| Incremental update | weak | experiment memory | partial | resume | strong qualitative | **strong source-driven** | **STRONGER** |
| Portable scientific state | weak | partial | Git artifacts | run files | run state | deployment-local folder+DB | **STRONGER requirement** |
| Runtime success ≠ scientific completeness | yes | yes | yes | yes | yes | **yes** | **VERY STRONG** |
| Context deltas / bounded windows | hierarchical | selective | structured | strong | strong | **strong** | **STRONGER** |

---

# 51. New open questions after Paperclip

## UNRESOLVED — Should scientific state be DB-first, files-first, or hybrid?

Paperclip shows benefits of files + DB.

DisMech shows strong structured files.

Need benchmark for:

- portability;
- diffability;
- query speed;
- scale;
- human audit.

---

## UNRESOLVED — How much task-state detail should be visible to Scientist?

Paperclip suggests most runtime state should stay hidden.

Likely only:

```text
task objective
constraints
source state
review requirements
```

Need minimal effective interface.

---

## UNRESOLVED — How should capability compatibility affect claiming?

At scale:

```text
task requires:
    vision
    statistics
    bioinformatics
```

Pool claiming should match worker/tool profile.

Need deterministic capability matcher.

---

# 52. Current top Scientist takeaways after six Tier-1 reviews

1. Keep Scientist workers fungible.
2. Keep N separate from role semantics.
3. Make task ownership deterministic.
4. Add dynamic compatible-task claiming.
5. Keep blockers/dependencies separate from organizational hierarchy.
6. Make raw scientific sources immutable and hash-backed.
7. Separate source identity from worker identity.
8. Persist revision history.
9. Preserve contradictions and supersession.
10. Keep scientific memory incremental.
11. Keep scientific memory portable, not only deployment-durable.
12. Treat document preprocessing quality as first-order science infrastructure.
13. Keep tool/plugin capability separate from Scientist reasoning contract.
14. Do not confuse control-plane correctness with scientific validity.
15. Do not confuse lint with evidence verification or hostile review.
16. Keep independent evidence verification for high-impact claims.
17. Keep hostile review selective and independent.
18. Avoid single producer+integrator+linter topology.
19. Avoid Markdown as sole canonical scientific state at large scale.
20. Keep context deltas small and task-relevant.
21. Keep runtime details hidden from Scientist where possible.
22. Keep scientific omission visible as an explicit failure class.
23. Preserve hierarchical source→evidence→claim→synthesis structure.
24. Continue benchmarking specialist modes vs simple generalists.
25. Final adoption remains surgical: maximum gain, minimum harness.

# 53. Review 07 — ATHENA

Repository analizzata: `mims-harvard/ATHENA`

## Nuovi pattern cumulativi

- **General Scientist forte + capability discovery dinamico:** `scientific need → discover capability → invoke tool → reintegrate result`. **VERY STRONG / ADOPT CANDIDATE**.
- **Progressive disclosure delle capability:** molte capability disponibili, poche residenti nel contesto. **VERY STRONG**.
- **Database-specific Scientist roles:** da evitare; EuropePMC, Semantic Scholar, PubTator, OpenTargets, Monarch, ChEMBL, EFO sono tool/capability. **REJECT permanent tool-specific roles**.
- **Shallow intra-task branching:** `parent → CallAgent(subquestion) → child → structured result → parent reintegration`. **STRONGER**.
- **Task-conditioned specialization:** i child sono mini-Scientist equivalenti; la specializzazione deriva da subquestion/plan/tools/backend. **STRONGER**.
- **Parent-owned reintegration:** il child non promuove direttamente knowledge canonica; il parent resta responsabile della transizione scientifica. **ADOPT CANDIDATE**.
- **Deep recursive trees:** ATHENA documenta depth=2 con ~25 agenti e >10 minuti su una sola domanda. **REJECT come scaling architecture**.
- **Due parallelismi distinti:** `ScientistPool(N)` per il corpus; bounded sibling branches per la complessità locale. **VERY STRONG distinction**.
- **Free-form child answer:** debole come fan-in a scala; preferire structured result/evidence/uncertainty/contradictions. **ADOPT CANDIDATE**.
- **Context compaction:** utile operativamente ma pericolosa scientificamente; comprimere active context senza distruggere durable evidence. **VERY STRONG**.
- **Citation allowlist:** il modello può citare solo fonti registrate nel trace; da estendere a source ID + valid locator + evidence packet. **ADOPT CANDIDATE**.
- **Citation validity ≠ evidence validity:** fonte valida non implica supporto semantico della claim. **VERY STRONG distinction**.
- **Substrate attribution:** ToolUniverse fornisce gran parte della potenza biomedicale; ATHENA aggiunge adaptive sequencing, capability choice, delegation e reintegration. **STRONGER**.
- **Capability health first-class:** la race di Tool_RAG dimostra che il sistema può continuare mentre ha perso una capability critica. `CAPABILITY_REQUIRED + unavailable → DEGRADED/BLOCKED`, mai silent fallback. **VERY STRONG / ADOPT CANDIDATE**.
- **Silent capability degradation:** nuova classe di failure scientifico. **REJECT**.
- **Shared lazy-init safety:** capability registry/retrieval deve essere inizializzato e health-checked deterministicamente prima del parallelismo. **ADOPT runtime invariant**.
- **Strong harness, light Scientist prompt:** capability estese sotto il cofano, minima superficie attiva nel contesto. **VERY STRONG**.
- **Permanent Planner:** ulteriormente indebolito; planning locale può restare nel General Scientist. **WEAKER / likely reject**.

## Disegno incrementale dopo sette review

```text
SCIENTIFIC TASK
      ↓
GENERAL SCIENTIST
      ├─ direct reasoning
      ├─ capability need → dynamic capability retrieval → tool
      └─ subanalysis need → shallow ephemeral branch
                              ↓
                     structured result
                              ↓
                     parent reintegration
                              ↓
                  evidence / claim store
```

Parallelismo:
- `ScientistPool(N)` = scala corpus;
- bounded sibling CallAgents = complessità locale.

## Capability architecture

```text
CAPABILITY REGISTRY
metadata / schema / provider / health / cost / latency / permissions
        ↓
Scientist identifies need
        ↓
retrieve minimum relevant capability descriptions
        ↓
execute
        ↓
structured result
```

> **Capability discovery should be dynamic; capability health should be deterministic.**

## Context architecture

```text
DURABLE STATE
raw sources / evidence / claims / contradictions / hypotheses
        ↓
TASK CONTEXT RETRIEVER
        ↓
small active context
        ↓
Scientist
```

## Nuovi failure states

- `CAPABILITY_REQUIRED_BUT_UNAVAILABLE`
- `CAPABILITY_DEGRADED`
- `TOOL_DISCOVERY_FAILED`
- `TOOL_EXECUTION_FAILED`
- `SUBAGENT_FAILED`
- `CONTEXT_COMPACTION_LOSS_RISK`

> **A system that continues without a required scientific capability is degraded, not successful.**

## Ledger delta ATHENA

| Pattern | Stato cumulativo |
|---|---|
| Strong broad General Scientist | **STRONGER** |
| Dynamic capability discovery | **VERY STRONG** |
| Progressive tool disclosure | **VERY STRONG** |
| Permanent tool-specific Scientist | **REJECT** |
| Shallow intra-task branching | **STRONGER** |
| Deep recursive branching | **REJECT** |
| Parent-owned reintegration | **STRONGER** |
| Global Scientist Pool separate from recursion | **VERY STRONG requirement** |
| Local parallel siblings | **STRONGER** |
| Structured branch return | **ADOPT CANDIDATE** |
| Context compaction with durable provenance | **ADOPT with hardening** |
| Durable evidence outside context | **VERY STRONG requirement** |
| Citation allowlist | **EMERGING / ADOPT CANDIDATE** |
| Capability health state | **VERY STRONG requirement** |
| Silent capability degradation | **REJECT** |
| Shared lazy-init safety | **ADOPT runtime invariant** |
| Permanent Planner | **WEAKER / likely reject** |
| Search-driven open research | **KEEP as discovery mode** |
| Exhaustive corpus completeness | **CRITICAL BUILD requirement** |
| Independent evidence review | **SELECTIVE REQUIRED layer** |
| Hostile review | **SELECTIVE REQUIRED layer** |

## Open questions dopo ATHENA

1. Quanto autonomy dare alla capability selection: broad read-only access vs task allowlist?
2. Qual è il minimo structured child-return schema utile senza irrigidire il ragionamento?
3. Qual è la branch width ottimale: 1/2/4/8?
4. Quanto context compaction possiamo tollerare senza ridurre scientific recall?

## Current top Scientist takeaways after seven Tier-1 reviews

1. Keep the General Scientist broad and capable.
2. Let the Scientist recognize missing scientific needs.
3. Retrieve capabilities dynamically instead of preloading every tool/skill.
4. Keep active context small even if capability universe is large.
5. Treat database/retrieval specialists as tools, not agents.
6. Allow shallow bounded intra-task subanalyses.
7. Keep child workers ephemeral and task-conditioned.
8. Keep parent responsibility for reintegration.
9. Return structured child results, not only free-form prose.
10. Separate global corpus parallelism from local subagent parallelism.
11. Use ScientistPool(N) for corpus throughput, not recursive trees.
12. Reject deep recursive swarms as default architecture.
13. Keep durable evidence outside conversational context.
14. Use context compaction only over reconstructable durable state.
15. Use source/citation allowlists as deterministic anti-fabrication gates.
16. Do not confuse citation validity with evidence validity.
17. Treat capability health as explicit deterministic state.
18. Never silently continue after loss of a required scientific capability.
19. Initialize shared capability infrastructure safely before parallel use.
20. Keep Planner as a function/mode unless benchmark proves a separate actor helps.
21. Keep tool execution separate from scientific interpretation.
22. Preserve independent evidence verification as a separate selective layer.
23. Preserve hostile scientific review as a separate selective layer.
24. Search-driven discovery remains valuable but does not prove corpus completeness.
25. Final LEGEND adoption remains surgical: minimum patterns, maximum measured scientific gain.


# 61. Review 08 — ARIS

Repository analizzata: `wanshuiyin/Auto-claude-code-research-in-sleep` (`ARIS`)

## 61.1 Nuovi spunti utili per gli Scientist LEGEND

### A. Execution / generation ≠ acceptance

ARIS rende particolarmente esplicita una distinzione già emersa in altre review:

```text
generated / executed
≠
accepted
```

Un task può essere `done` senza essere `accepted`.

Per LEGEND questo è molto importante perché il Reader/Scientist può:

- leggere;
- estrarre;
- proporre;
- eseguire;
- sintetizzare;

senza che ciò significhi automaticamente:

> “scientificamente valido / promosso”.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### B. Type-A vs Type-B judgments

ARIS distingue concettualmente:

- **Type-A** = fatti/meccaniche verificabili deterministicamente;
- **Type-B** = giudizi scientifici o di merito che richiedono una vera valutazione indipendente.

Questo è un pattern potenzialmente molto utile per LEGEND.

Esempi:

```text
Type-A
- source exists
- result file exists
- DOI resolves
- hash matches
- task completed
- number present in raw output

Type-B
- evidence supports claim
- mechanism is defensible
- result is novel
- interpretation is not overclaimed
```

### Principio

> **Type-A may be accepted by software; Type-B must not self-acquit.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### C. Fan-out ≠ jury

ARIS è una delle repo più chiare su questo punto.

Same-family shards possono aumentare:

- breadth;
- throughput;
- candidate generation.

Ma non devono essere trattati come indipendent jury.

Quindi:

```text
N same-family Scientists
→ breadth / replication

≠

independent validation
```

Per LEGEND questo rafforza:

> **parallelism and validation are separate dimensions.**

**Stato:** VERY STRONG.

---

### D. Cross-family / fresh-context reviewer

ARIS usa reviewers esterni/fresh-context per Type-B judgments.

Questo rafforza fortemente il design:

```text
producer
→ deterministic pre-check
→ fresh independent reviewer
```

e, quando utile:

```text
different model family
```

La model-family diversity non è automaticamente migliore, ma ARIS dimostra una vera implementazione di heterogeneous review.

**Stato:** STRONGER / BENCHMARK.

---

### E. Raw-artifact-first review

`paper-claim-audit` è particolarmente interessante perché il reviewer riceve:

- paper;
- raw results;

e non executor summaries.

Questo riduce anchoring e narrative contamination.

Per LEGEND:

> **high-impact review should preferentially reopen raw evidence, not merely review the producer's prose.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### F. Zero-context verification

ARIS usa fresh/zero-context audit per alcune verifiche.

Questo rafforza una delle questioni già aperte:

```text
same model + fresh context
vs
different model + fresh context
```

ARIS supporta fortemente almeno la componente:

> **fresh context matters.**

**Stato:** STRONGER.

---

### G. Hostile attack + independent adjudication

`kill-argument` implementa:

```text
fresh attacker
→ strongest rejection argument
→ separate fresh adjudicator
→ classify whether attack stands
```

Questo è un pattern di hostile review più sofisticato del semplice “critic”.

Potrebbe essere utile per:

- major mechanistic synthesis;
- therapeutic implication;
- causal claim;
- experiment-driving hypothesis.

Non va applicato a ogni microfinding.

**Stato:** STRONGER / BENCHMARK.

---

### H. Review should be selective, not universal

ARIS spende cross-model/jury budget soprattutto sui Type-B judgments che contano.

Questo converge con Gemma:

> **review depth and independence should scale with consequence/uncertainty.**

**Stato:** VERY STRONG.

---

### I. Structured shard outputs

ARIS fan-out richiede output strutturati con:

- `shard_id`;
- entries/candidates;
- `dedup_key`.

Per LEGEND questo rafforza il requisito:

> **parallel workers should return mergeable structured packets, not free-form prose.**

**Stato:** VERY STRONG.

---

### J. Mechanical dedup before expensive jury

Pattern:

```text
fan-out
→ union
→ mechanical dedup
→ expensive independent review
```

Questo è un ottimo pattern di efficienza.

Per LEGEND:

- dedup findings;
- dedup claims;
- dedup candidate hypotheses;

prima di mandare tutto a Reviewer.

**Stato:** ADOPT CANDIDATE.

---

### K. Three-tier fan-out fallback

ARIS implementa un pattern runtime-portable:

1. true parallel Workflow;
2. Agent fan-out;
3. sequential fresh-context fallback.

La semantica scientifica resta simile anche se cambia il livello di parallelismo.

Questo suggerisce:

> **scientific contract should not depend on one specific concurrency backend.**

**Stato:** STRONGER.

---

### L. Skill-first specialization

ARIS usa molte specializzazioni come skills/modes:

- citation audit;
- paper claim audit;
- research review;
- kill argument;
- result-to-claim;
- proof checker;
- research wiki.

Questo rafforza molto:

> **specialization should usually be a mode/skill, not a permanent actor.**

**Stato:** VERY STRONG.

---

### M. But too many always-on skills would be a mistake

ARIS ha molti skill disponibili, ma il valore viene dal fatto che sono invocati quando servono.

Per LEGEND:

> **large skill library is acceptable only with selective loading / invocation.**

Questo è coerente con ATHENA e con il nostro obiettivo di strong harness + light prompt.

**Stato:** VERY STRONG.

---

### N. Progressive reading as optional discovery optimization

DeepXiv usa:

```text
search
→ brief
→ head
→ section
→ full if needed
```

Questo è molto efficiente per **open discovery**.

Ma `/research-lit` ha:

- max 20 local PDFs;
- first 3 pages.

Quindi ARIS fornisce anche un chiaro anti-pattern per il nostro bounded corpus.

### Regola LEGEND

> **progressive reading is useful in discovery mode, not as proof of exhaustive assigned-paper reading.**

**Stato:** STRONGER distinction.

---

### O. Discovery mode and corpus mode should be separate

ARIS rende molto evidente che un buon sistema scientifico può avere almeno due modalità:

```text
DISCOVERY MODE
search/prioritize/progressive read

CORPUS MODE
declared sources/exhaustive processing/completeness
```

Non va costretto un solo protocollo a fare entrambe le cose.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### P. Research Wiki as project memory, not evidence kernel

ARIS Wiki conserva:

- papers;
- ideas;
- experiments;
- claims;
- edges:
  - extends
  - contradicts
  - supports
  - invalidates
  - supersedes
  - inspired_by
  - tested_by

È molto utile come project memory.

Ma non garantisce:

- exact literature locator;
- experiment/panel-level evidence;
- biomedical ontology.

Quindi:

> **project knowledge graph ≠ canonical evidence store.**

**Stato:** STRONGER distinction.

---

### Q. Failed-idea retention

ARIS mantiene failed ideas nella memoria/query pack.

Questo converge con AutoScientists dead-end memory.

Per LEGEND:

```text
FAILED_HYPOTHESIS
FAILED_DIRECTION
REOPEN_IF
```

dovrebbe essere persistente.

**Stato:** STRONGER.

---

### R. Compact query pack

ARIS usa un `query_pack.md` con budget ~8k chars.

Questo è un esempio concreto di **compressed working memory** separata dal knowledge store completo.

Per LEGEND:

```text
full durable state
→ task-specific compact pack
→ Scientist context
```

**Stato:** STRONGER.

---

### S. Result existence pre-check before semantic review

`result-to-claim` prima verifica deterministicamente che l'evidenza esista.

Solo dopo chiede:

> cosa significa scientificamente?

Questo è uno dei pattern più puliti del corpus.

```text
raw evidence exists?
→ deterministic YES/NO

does it support the claim?
→ independent scientific judgment
```

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### T. Raw computation ≠ interpretation

ARIS separa molto bene:

```text
raw result
→ deterministic existence/integrity
→ semantic result-to-claim review
→ scientific claim
```

Questo rafforza Robin/CORAL.

**Stato:** VERY STRONG.

---

### U. Citation audit must check context, not only existence

ARIS `citation-audit` distingue:

1. source exists;
2. metadata correct;
3. source actually supports the local sentence.

Questo è un pattern molto importante.

> **real citation ≠ correct citation.**

**Stato:** VERY STRONG.

---

### V. Scheduler/task manager belongs to software

Experiment queue mostra ancora una volta:

- retry;
- OOM handling;
- stuck state;
- queue state;

come software.

Per LEGEND corpus Reader:

- task claiming;
- stale recovery;
- retry;
- worker liveness;

devono essere runtime.

**Stato:** STRONGER.

---

### W. Graceful degradation only for non-load-bearing optional sources

ARIS consente warn/skip per provider opzionali.

Questo è sensato in discovery mode.

Ma:

> **load-bearing completeness/review capability must fail closed.**

Questa distinzione converge con ATHENA capability-health semantics.

**Stato:** VERY STRONG.

---

## 61.2 Cosa ARIS indebolisce o lascia unresolved

### Search-driven literature workflow as corpus reader

Fortemente indebolito dalla stessa implementazione ARIS:

- max 20 local PDFs;
- first 3 pages.

**Stato:** REJECT for corpus mode.

---

### Same-family multi-agent voting as independence

ARIS lo rifiuta esplicitamente.

**Stato:** REJECT.

---

### Permanent specialist actors

Ulteriormente indeboliti.

**Stato:** WEAKER / likely reject.

---

### Universal heavy review

ARIS suggerisce review selettiva per Type-B.

**Stato:** WEAKER universal review.

---

### Wiki summary as evidence kernel

**Stato:** REJECT as sole evidence store.

---

# 62. Aggiornamento del disegno incrementale dopo otto review

```text
                 SCIENTIFIC WORK
                        │
                classify transition
                        │
          ┌─────────────┴──────────────┐
          │                            │
          ▼                            ▼
      TYPE-A                        TYPE-B
 deterministic                  scientific merit
 mechanics                         judgment
          │                            │
          ▼                            ▼
      software gate             candidate producer
                                       │
                                       ▼
                              deterministic pre-check
                                       │
                                       ▼
                              fresh independent jury
                                       │
                                  accept/reject
```

Parallelism:

```text
breadth fan-out
→ structured shards
→ mechanical dedup
→ independent jury only where needed
```

---

# 63. Discovery mode vs Corpus mode

## DISCOVERY MODE

```text
search
→ progressive retrieval
→ prioritize
→ synthesize
→ explore hypotheses
```

Optimization target:
- breadth;
- novelty;
- token efficiency;
- speed.

## CORPUS MODE

```text
declared corpus
→ manifest
→ every source assigned
→ exhaustive declared-surface processing
→ completion gate
→ synthesis
```

Optimization target:
- coverage;
- traceability;
- reproducibility.

### Principle

> **Do not force one reading policy to serve both discovery and exhaustive corpus curation.**

---

# 64. Review architecture — aggiornamento dopo ARIS

Review spectrum cumulativo:

```text
Type-A deterministic gate
        ↓
Evidence Verifier
        ↓
Hostile Reviewer
        ↓
Attacker + independent Adjudicator
```

Risk-based escalation:

```text
ordinary low-risk claim
→ deterministic validation only

important evidence claim
→ fresh evidence verifier

major mechanism/therapy claim
→ hostile review

load-bearing controversial conclusion
→ attack + adjudication
```

---

# 65. Context architecture — aggiornamento dopo ARIS

```text
FULL SCIENTIFIC STATE
    raw sources
    evidence
    claims
    contradictions
    failed ideas
    experiments
          │
          ▼
COMPACT QUERY PACK
          │
          ▼
Scientist task context
```

The compact pack is a retrieval/view layer, never the authoritative store.

---

# 66. Cumulative pattern ledger — aggiornamento dopo ARIS

| Pattern | Stato cumulativo dopo ARIS |
|---|---|
| Execution ≠ acceptance | **VERY STRONG / ADOPT CANDIDATE** |
| Type-A vs Type-B | **VERY STRONG / ADOPT CANDIDATE** |
| Fan-out ≠ jury | **VERY STRONG** |
| Same-family voting as independence | **REJECT** |
| Fresh-context review | **STRONGER** |
| Cross-family review | **STRONGER / BENCHMARK** |
| Raw-artifact-first review | **VERY STRONG / ADOPT CANDIDATE** |
| Attack + independent adjudication | **STRONGER / BENCHMARK** |
| Risk-based review | **VERY STRONG** |
| Structured shard outputs | **VERY STRONG** |
| Dedup before jury | **ADOPT CANDIDATE** |
| Runtime-portable fan-out | **STRONGER** |
| Skill-first specialization | **VERY STRONG** |
| Always-on skill overload | **REJECT direction** |
| Progressive reading in discovery | **KEEP** |
| Progressive reading as corpus completeness | **REJECT** |
| Discovery mode distinct from corpus mode | **VERY STRONG / ADOPT CANDIDATE** |
| Research Wiki as project memory | **KEEP** |
| Wiki as evidence kernel | **REJECT as sole source** |
| Failed-idea retention | **STRONGER** |
| Compact query pack | **STRONGER** |
| Result existence before interpretation | **VERY STRONG / ADOPT CANDIDATE** |
| Raw computation ≠ interpretation | **VERY STRONG** |
| Citation existence ≠ citation support | **VERY STRONG** |
| Scheduler/liveness/retry as software | **VERY STRONG** |
| Graceful degradation for optional sources | **KEEP** |
| Graceful degradation for load-bearing guarantees | **REJECT** |

---

# 67. New open questions after ARIS

## UNRESOLVED — Type-A / Type-B taxonomy for LEGEND

Need define a minimal list of transitions that are:

- deterministic;
- hybrid;
- scientific merit judgments.

Goal: avoid overengineering.

---

## UNRESOLVED — Different-model vs same-model fresh reviewer

ARIS adds strong evidence for heterogeneous review, but we still need benchmark:

```text
same model + fresh isolated context
vs
different model + fresh isolated context
```

on actual WWOX paper tasks.

---

## UNRESOLVED — Attack + adjudication threshold

Need determine when `kill-argument`-style review pays for itself.

Likely only:

- major mechanism;
- therapeutic recommendation;
- experiment-driving hypothesis;
- disputed high-impact conclusion.

---

## UNRESOLVED — Discovery/Corpus mode boundary

Need define exact switch conditions:

```text
task objective
corpus declared?
completeness required?
```

without burdening Scientist prompt.

---

# 68. Current top Scientist takeaways after eight Tier-1 reviews

1. Keep a broad General Scientist.
2. Keep specialist behavior mostly as selectively loaded skills/modes.
3. Separate discovery mode from exhaustive corpus mode.
4. Do not reuse progressive-reading shortcuts as corpus-completeness guarantees.
5. Keep execution/generation separate from acceptance.
6. Distinguish Type-A deterministic facts from Type-B scientific judgments.
7. Never let same-family fan-out masquerade as independent validation.
8. Use fan-out for breadth, not for jury authority.
9. Return structured shard outputs.
10. Deduplicate mechanically before expensive review.
11. Use fresh independent review selectively.
12. Prefer raw-artifact-first review for load-bearing claims.
13. Benchmark same-model fresh context vs different-model review.
14. Keep attack+adjudication only for the highest-risk conclusions.
15. Keep result existence/integrity checks deterministic.
16. Keep scientific interpretation separate from raw computation.
17. Audit whether a citation supports the local claim, not only whether it exists.
18. Preserve failed hypotheses and dead ends.
19. Use compact query packs as views over durable state, not as authoritative memory.
20. Keep runtime fan-out portable across concurrency backends.
21. Keep scheduler/retry/liveness in software.
22. Allow graceful degradation only for optional non-load-bearing capabilities.
23. Fail closed when a load-bearing scientific capability disappears.
24. Keep corpus completeness as a deterministic system guarantee.
25. Final adoption remains surgical: collect broadly now, benchmark later, implement only the minimum high-yield subset.


# 69. Review 09 — Medea

Repository analizzata: `mims-harvard/Medea`

## 69.1 Nuovi spunti utili per gli Scientist LEGEND

### A. Structured capability registry
Medea usa `tool_info.json` come registro esplicito di capability scientifiche con descrizioni, import path, parametri e output.

Per LEGEND questo rafforza:
> **scientific capabilities should be explicit, inspectable and selectively loadable.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

### B. Capability registry + context checker registry
`tool_id_checker.json` separa:
- capability disponibile;
- compatibilità biologica/contestuale.

Questo è un pattern molto forte:

```text
Scientist chooses capability
→ deterministic biological/context preflight
→ execute only if compatible
```

**Stato:** VERY STRONG / ADOPT CANDIDATE.

### C. LLM proposes required checks, software executes them
Medea usa un pattern ibrido:
- modello identifica quali controlli servono;
- software esegue checker deterministici.

Questo è utile, ma solo se l'assenza di un required check non viene interpretata come PASS.

**Stato:** STRONGER / HARDEN.

### D. Fail-open scientific validation è un anti-pattern
Medea auto-approva in alcune condizioni:
- integrity verifier exhausted;
- malformed quality-review output;
- iteration ceiling.

Per LEGEND:
> **validator failure must never become scientific approval.**

Stati corretti:
`UNKNOWN / UNVERIFIED / BLOCKED`.

**Stato:** REJECT.

### E. Real computational execution sotto planning scientifico
Medea implementa:
`objective → plan → code → subprocess → output → debug → quality check`.

Questo rafforza molto:
> **scientific reasoning should be able to produce executable evidence, not only prose.**

**Stato:** VERY STRONG.

### F. Raw computation and interpretation are separable
Medea conserva code/output separati dalla successiva interpretazione scientifica.

Per LEGEND:
```text
raw computation
≠
scientific interpretation
```

Serve aggiungere execution receipt/hashes, ma la separazione concettuale è valida.

**Stato:** VERY STRONG.

### G. Bounded nested scientific reasoning
`scientific_reasoning_agent` consente a un computation task di richiedere letteratura supplementare con:
- call budget;
- cache;
- bounded invocation.

Questo è un ottimo esempio di local scientific autonomy controllata.

**Stato:** STRONGER / ADOPT CANDIDATE.

### H. Specialist nested tool, not recursive swarm
Il child è uno specialista letteratura, non un general-purpose recursive tree.

Questo rafforza:
> **bounded specialist invocation can be useful without recursive multi-agent topology.**

**Stato:** STRONGER.

### I. Query cache as optimization, not scientific memory
Il cache MD5 riduce lavoro ripetuto dentro la run, ma è temporaneo.

Lezione:
> **retrieval cache ≠ durable scientific memory.**

**Stato:** STRONGER distinction.

### J. Partial-result survival
Medea salva il research plan prima che computation/literature branch possano fallire.

Questo è un pattern utile:
> **valid upstream scientific work should survive downstream failure.**

**Stato:** ADOPT CANDIDATE.

### K. Coarse modality fan-out
Medea separa:
- computational branch;
- literature branch;
poi fa fan-in.

Questo suggerisce un parallelismo complementare a quello per-paper:
> **different evidence modalities can progress independently and converge later.**

**Stato:** STRONGER.

### L. Modality-level redundancy ≠ independent paper replication
Computation/literature/backbone sono traiettorie diverse, ma non equivalgono a due blinded readers dello stesso paper.

**Stato:** STRONGER distinction.

### M. Negative evidence ≠ technical failure
Medea prova a distinguere:
- no supporting literature;
- retrieval failure.

Questo è scientificamente essenziale.

Ma la forensic mostra che retrieval errors possono degradare in "no papers found".

Per LEGEND:
```text
NEGATIVE_EVIDENCE
≠
FAILED_RETRIEVAL
```
deve essere tipizzato deterministicamente.

**Stato:** VERY STRONG / HARDEN.

### N. Retrieval failure masquerading as no evidence è un failure critico
Se una branch fallisce e downstream la interpreta come assenza di letteratura, si crea una falsa conclusione scientifica negativa.

Nuovo invariant:
> **technical absence must never be promoted to scientific absence.**

**Stato:** VERY STRONG.

### O. Per-paper judge failure can silently reduce corpus
PaperJudge failures sono loggati ma il paper può essere escluso e il sistema continua.

Per LEGEND corpus mode:
> **failed paper assessment must remain an explicit incomplete task, not disappear from denominator.**

**Stato:** STRONGER requirement.

### P. Stateful validator leakage across samples
`ContextVerification._call_count` può accumulare tra samples e indebolire controlli successivi.

Per LEGEND:
> **task-local scientific validation state must be isolated per task/run.**

**Stato:** VERY STRONG / ADOPT invariant.

### Q. Specialist classes do not require permanent identities
Medea ha planning, literature, computation, auditing come moduli, non come attori permanenti con identità lunga.

Questo rafforza:
> **specialization ≠ permanent actor identity.**

**Stato:** VERY STRONG.

### R. Tool selection should be dynamic, tool registry static
Pattern:
- capability universe dichiarato;
- selection dinamica per task.

Converge con ATHENA.

**Stato:** VERY STRONG.

### S. Lazy loading of tools/models
Medea usa lazy import/load per ridurre overhead.

Questo è coerente con light harness.

**Stato:** STRONGER.

### T. Code debugger context packing
`CodeDebug` preserva:
- full code;
- traceback tail;
- compact tool metadata;
- compressed context.

Questo è un buon esempio di **task-specific context packing**.

**Stato:** ADOPT CANDIDATE.

### U. Rerank/top-N is excellent for discovery, dangerous for corpus mode
Medea fa early narrowing molto aggressivo.

Per open QA è efficiente.
Per exhaustive corpus:
> **rerank/top-N must not decide whether a declared paper "counts as read".**

**Stato:** STRONGER distinction.

### V. Consensus panel ≠ evidence verification
Medea ha auditor + panel + vote, ma nessuno riapre la fonte primaria.

Quindi:
> **multi-model consensus does not substitute source-grounded verification.**

**Stato:** VERY STRONG.

### W. Hidden vote counts can reduce conformity
Panelists vedono viewpoints senza popularity counts nelle round successive.

Questo può ridurre bandwagon effects.

**Stato:** EMERGING / BENCHMARK.

### X. Confidence-weighted voting is not calibrated evidence strength
Medea pesa voti per confidence.

Questo può essere utile come helper, ma:
> model confidence ≠ scientific evidence strength.

**Stato:** WATCH / BENCHMARK.

### Y. Deterministic grounding warnings
Quando branch falliscono, Medea appende grounding warnings deterministici.

Questo è un pattern piccolo e forte:
> **known degradation should be impossible for the final LLM to erase.**

**Stato:** ADOPT CANDIDATE.

### Z. Computational execution receipts are the missing minimum
Medea ha real execution ma manca:
- code hash;
- environment;
- input hash;
- output hash.

Per LEGEND:
> **real execution should emit a deterministic receipt automatically.**

**Stato:** STRONGER requirement.

## 69.2 Cosa Medea indebolisce o lascia unresolved

- Specialist pipeline only: **WEAKER as corpus architecture**.
- General Scientist Pool: **still required for exhaustive corpus throughput**.
- Abstract-centric literature path: **REJECT as deep-reading substitute**.
- Panel consensus as validation: **REJECT**.
- Fail-open validator behavior: **REJECT**.
- Temporary cache/CSV as scientific memory: **REJECT**.
- Rerank/top-N as completeness mechanism: **REJECT**.

# 70. Aggiornamento del disegno incrementale dopo nove review

```text
GENERAL SCIENTIST
      │
      ├─ understands objective
      ├─ selects capability
      │      ↓
      │  deterministic context/preflight checker
      │      ↓
      │  tool / computation
      │
      ├─ if knowledge gap:
      │      bounded specialist invocation
      │
      └─ returns typed evidence/result
             ↓
      durable evidence store
             ↓
      selective verification/review
```

Computational branch:

```text
scientific plan
→ generated code
→ deterministic execution
→ execution receipt
→ raw output
→ scientific interpretation
```

# 71. Capability/preflight architecture — aggiornamento dopo Medea

```text
CAPABILITY REGISTRY
    │
    ├─ name
    ├─ schema
    ├─ provider
    ├─ inputs
    ├─ outputs
    ├─ health
    └─ compatibility requirements
          │
          ▼
Scientist selects capability
          │
          ▼
REQUIRED CHECKS
          │
          ▼
DETERMINISTIC PREFLIGHT
          │
    PASS / FAIL / UNKNOWN
```

Regola:
> **UNKNOWN must never be silently coerced to PASS.**

# 72. Failure semantics — aggiornamento dopo Medea

Nuovi stati/invariant:

- `FAILED_RETRIEVAL`
- `NO_EVIDENCE_FOUND`
- `FAILED_JUDGE`
- `UNVERIFIED_PLAN`
- `UNVERIFIED_ANALYSIS`
- `VALIDATION_STATE_LEAK`
- `CAPABILITY_CONTEXT_UNVERIFIED`

Regole:
1. technical failure ≠ negative evidence;
2. validator failure ≠ approval;
3. task-local validator state must reset;
4. dropped item remains incomplete in corpus denominator.

# 73. Cumulative pattern ledger — aggiornamento dopo Medea

| Pattern | Stato cumulativo dopo Medea |
|---|---|
| Structured capability registry | **VERY STRONG / ADOPT CANDIDATE** |
| Context compatibility registry | **VERY STRONG / ADOPT CANDIDATE** |
| LLM selects checks, software executes | **STRONGER / HARDEN** |
| Validator failure → approval | **REJECT** |
| Real computational execution | **VERY STRONG** |
| Raw computation ≠ interpretation | **VERY STRONG** |
| Bounded nested specialist reasoning | **STRONGER** |
| Specialist invocation ≠ recursive swarm | **VERY STRONG distinction** |
| Retrieval cache | **KEEP as optimization only** |
| Cache as scientific memory | **REJECT** |
| Partial-result survival | **ADOPT CANDIDATE** |
| Modality-level parallelism | **STRONGER** |
| Modality redundancy ≠ paper replication | **STRONGER distinction** |
| Negative evidence ≠ technical failure | **VERY STRONG** |
| Retrieval failure masquerading as no evidence | **REJECT / critical failure class** |
| Per-item failure disappearing from corpus | **REJECT** |
| Task-local validator isolation | **VERY STRONG invariant** |
| Specialist class without permanent identity | **VERY STRONG** |
| Dynamic selection over static capability registry | **VERY STRONG** |
| Lazy tool/model loading | **STRONGER** |
| Task-specific context packing | **ADOPT CANDIDATE** |
| Rerank/top-N in discovery | **KEEP** |
| Rerank/top-N as corpus completeness | **REJECT** |
| Multi-model consensus as evidence verification | **REJECT** |
| Hidden vote counts | **BENCHMARK** |
| Confidence-weighted voting | **WATCH / BENCHMARK** |
| Deterministic degradation warning | **ADOPT CANDIDATE** |
| Computational execution receipt | **STRONGER requirement** |

# 74. New open questions after Medea

1. Quanto planning scientifico deve restare nel General Scientist vs essere un separate mode?
2. Quali biological/context preflight checkers sono davvero ad alto rendimento per WWOX?
3. Quando il multi-modal fan-out `literature + computation` migliora davvero il risultato rispetto a un solo Scientist con tools?
4. Hidden-vote debate migliora scientific accuracy o solo diversity?
5. Quanto vale un panel di 3 modelli rispetto a un solo fresh hostile reviewer?
6. Qual è il minimum execution receipt utile senza aggiungere overhead?

# 75. Current top Scientist takeaways after nine Tier-1 reviews

1. Keep the General Scientist broad and tool-aware.
2. Make scientific capabilities explicit in a structured registry.
3. Separate capability availability from biological/context compatibility.
4. Let the Scientist identify needed capabilities; let software validate compatibility.
5. Never turn missing/failed validation into PASS.
6. Keep validation state isolated per task/run.
7. Preserve real computational execution as a first-class scientific capability.
8. Keep raw computation separate from scientific interpretation.
9. Emit deterministic execution receipts.
10. Allow bounded specialist literature/computation calls inside a task.
11. Do not use recursive general-purpose swarms.
12. Preserve valid upstream work when downstream branches fail.
13. Treat literature/computation as complementary evidence modalities.
14. Do not confuse modality redundancy with independent reading replication.
15. Encode negative evidence separately from retrieval failure.
16. A failed paper/judge cannot disappear from an exhaustive corpus denominator.
17. Keep specialization as mode/module rather than permanent identity.
18. Keep tools/models lazily loaded and selectively exposed.
19. Use task-specific context packing rather than whole-history context.
20. Use rerank/top-N aggressively in discovery mode, never as corpus-completeness logic.
21. Do not use multi-model consensus as substitute for source-grounded verification.
22. Surface known grounding degradation deterministically in final output.
23. Keep confidence aggregation secondary to actual evidence strength.
24. Keep corpus state, completeness and task ownership deterministic.
25. Final LEGEND adoption remains surgical: census broadly now; implement only primitives that survive measured ablation.


# 76. Review 10 — ARA

Repository analizzata: `ARA-Labs/Agent-Native-Research-Artifact`

## 76.1 Nuovi spunti utili per gli Scientist LEGEND

### A. Universal deep-reader contract per bounded source unit
ARA è la repo che più chiaramente dimostra un **General Scientist/Compiler** capace di:
- leggere l'intero input assegnato;
- ispezionare appendici;
- estrarre evidenza;
- sintetizzare meccanismi;
- preservare negative evidence;
- produrre artifact persistente.

Questo rafforza il nostro design:
> **one bounded source packet → one interchangeable General Scientist → one standard scientific artifact.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### B. Read every page + appendices come scientific protocol
Il Compiler impone full-page reading e appendici, con fino a tre coverage reread.

Questo è più vicino all'obiettivo LEGEND rispetto ai workflow search-driven.

Ma resta prompt/protocol-level, non prova deterministica di attenzione.

Lezione:
> **keep the deep-reading obligation; externalize proof of document completeness to software.**

**Stato:** VERY STRONG / HARDEN.

---

### C. Figure/table exhaustive pass
ARA impone una evidence ledger per ogni numbered figure/table, screenshot + Markdown, direct visual inspection, exact-vs-approximate distinction, confidence, axis/unit/log-scale awareness.

Questo è uno dei pattern più direttamente utili al Reader LEGEND.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### D. Exact vs approximate visual extraction
ARA impone di non fabbricare numeri quando una figura è qualitativa o il valore non è leggibile.

Possibile output:
```text
EXACT
APPROXIMATE
UNREADABLE
```

con confidence.

**Stato:** VERY STRONG.

---

### E. Mechanism-oriented claim schema
ARA usa claims con:
- statement;
- Conditions;
- falsification criteria;
- Proof/evidence basis;
- dependencies;
- status.

Questo rafforza l'idea di non fermarsi a “paper summary”.

Per LEGEND:
> **reader output should include reusable mechanistic claims, not only observations.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### F. Conditions + falsifier come default per hypothesis/causal claim
ARA rende espliciti scope e falsificabilità.

Questo converge con AutoScientists/DisMech/ARIS.

Per LEGEND:
```text
CLAIM
CONDITIONS
FALSIFICATION
```

può essere un minimo ad alto rendimento.

**Stato:** VERY STRONG.

---

### G. Load-bearing number grounding
ARA richiede riapertura della fonte e verbatim matched line per numeri load-bearing.

Questo è un pattern molto pragmatico:
> **not every sentence needs maximal forensic overhead, but load-bearing quantitative claims do.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### H. Evidence strictness can be risk-weighted
ARA suggerisce implicitamente un buon compromesso con il nostro obiettivo “minimum harness”:
- stronger grounding for load-bearing numbers;
- lighter structure for less critical statements.

Questo supporta:
> **evidence rigor should be concentrated where scientific consequence is high.**

**Stato:** STRONGER.

---

### I. Negative/dead-end preservation
ARA conserva:
- dead ends;
- refuted/weakened claims;
- unresolved conflicts;
- negative channel in Foresight.

Questa convergenza è ormai fortissima.

**Stato:** VERY STRONG.

---

### J. Current understanding vs journey/history
Research Manager distingue:
```text
logic/ = current best understanding
trace/ = research journey/history
```

Questo è un pattern molto utile:
> **current model can stay clean without deleting how we got there.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### K. Progressive crystallization
Tentative knowledge resta staging/history finché non matura.

Pattern:
```text
observation
→ staging
→ closure/sufficient support
→ crystallize into current logic
```

Per LEGEND questo può evitare premature canonization.

**Stato:** STRONGER / BENCHMARK.

---

### L. Contradictions are preserved, not collapsed
ARA mantiene conflict markers, unresolved decisions e contradiction reports.

**Stato:** VERY STRONG.

---

### M. Grounded inference vs speculative leap
Foresight distingue esplicitamente:
- grounded inference;
- speculative leap.

Questo è perfettamente coerente con l'epistemic discipline di LEGEND.

**Stato:** VERY STRONG / KEEP.

---

### N. Negative-aware retrieval
Foresight include anche negatives/dead ends nel retrieval.

Questo è importante:
> **future reasoning should retrieve not only what worked, but also what failed/refuted a direction.**

**Stato:** STRONGER / ADOPT CANDIDATE.

---

### O. Artifact-local hostile review
Rigor Reviewer controlla:
- causal overclaim;
- missing ablations/baselines;
- generalization;
- methodological rigor;
- contradictions;
- reproducibility;
- argument coherence.

È uno dei migliori hostile-review rubrics del corpus.

**Stato:** VERY STRONG.

---

### P. Hostile review still needs original-source reopening for evidence verification
Rigor Reviewer spot-checks artifact-local evidence, non universalmente original paper bytes.

Quindi:
> **artifact hostile review ≠ original-source evidence verification.**

**Stato:** VERY STRONG distinction.

---

### Q. Kill-shot investigation gate
Research Fuzzer richiede una “kill shot”: l'azione più probabile per rompere la claim prima della conclusione.

Questo è un pattern elegante e leggero da benchmarkare.

Potrebbe diventare una singola domanda obbligatoria per claim ad alto impatto:
> “What observation/experiment would most efficiently falsify this?”

**Stato:** EMERGING / ADOPT CANDIDATE.

---

### R. Persistent scientific artifact is a major Reader output
ARA non produce solo report: produce durable structured files con logic/evidence/trace.

Questo rafforza:
> **the Reader should leave reusable scientific state, not transient prose.**

**Stato:** VERY STRONG.

---

### S. Machine graph projection from human-readable artifact
`build_manifest.py` deriva `manifest.json` da Markdown/YAML.

Questo suggerisce un pattern interessante:
> **human-readable scientific state can coexist with deterministic machine projection.**

Non necessariamente serve DB-first.

**Stato:** STRONGER / BENCHMARK.

---

### T. Per-unit artifact + later corpus fan-in
ARA mostra che il singolo paper può essere trasformato in un artifact ricco.

Ma non implementa cross-ARA corpus synthesis.

Questo rende più concreto il nostro likely map/fan-in:
```text
paper
→ per-paper structured artifact
→ normalized evidence/claims
→ corpus synthesis
```

**Stato:** VERY STRONG direction.

---

### U. Equivalent ephemeral workers fit naturally
Il Compiler non dipende da identità permanenti.

RE-Bench mostra one equivalent child per bounded run.

Questo rafforza:
> **Compiler-like Reader instances can be fungible and ephemeral.**

**Stato:** VERY STRONG.

---

### V. Depth-one fan-out is enough for many bounded extraction tasks
RE-Bench usa one child per run, central collect/dedup/merge/scrub.

Questo è una prova ulteriore contro recursive swarms.

**Stato:** VERY STRONG.

---

### W. Paginated no-truncation reading
RE-Bench documenta un failure reale: preview/truncation causava perdita silenziosa di tail data.

Pattern hardened:
```text
dump chunk to file
→ paginated Read
→ never skip chunk
```

Per LEGEND PDF/full-text ingestion:
> **never rely on truncated previews for declared exhaustive reading.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### X. Progressive disclosure over durable artifact
ARA usa:
```text
PAPER.md
→ logic layers
→ details/evidence/code
```

Foresight recupera solo ciò che serve.

Questo è fortemente coerente con “strong harness, light prompt”.

**Stato:** VERY STRONG.

---

### Y. One giant 50-paper Reader is implicitly discouraged
ARA's own progressive-disclosure design suggests that one monolithic Compiler over 50 papers risks:
- context overload;
- identity confusion;
- forgotten early evidence;
- source provenance complexity.

Quindi per LEGEND:
> **bounded per-paper or per-source tasks + later hierarchical fan-in** is stronger than one giant reading session.

**Stato:** STRONGER.

---

### Z. Corpus fan-in is the real scaling bottleneck
ARA conferma una convergenza sempre più forte:
> **replicating readers is easier than merging their science without losing provenance/minority evidence.**

At 500/5000 papers, bottleneck:
- claim/entity normalization;
- contradiction matching;
- review routing;
- synthesis.

**Stato:** VERY STRONG.

---

## 76.2 Cosa ARA indebolisce o lascia unresolved

### One Compiler over all 50 papers
**WEAKER / likely reject** as default exhaustive architecture.

### Prompt-only single-writer semantics
Research Manager's single-writer/append-only discipline non va trattata come hard concurrency guarantee.

**REJECT as authority primitive.**

### Artifact-local review as universal evidence verifier
**REJECT equivalence.**

### Per-paper ARA as sufficient corpus architecture
Per-paper artifacts without cross-corpus normalized fan-in become an artifact library, non a disease model.

**REJECT as complete solution.**

### Permanent specialist identities
Nuovamente non supportate.

**WEAKER / likely reject.**

# 77. Aggiornamento del disegno incrementale dopo dieci review

```text
CORPUS MANIFEST
      ↓
READY PAPER/SOURCE TASKS
      ↓
GENERAL SCIENTIST / COMPILER x N
      │
      ├─ full source reading
      ├─ appendices
      ├─ figures/tables
      ├─ observations
      ├─ negative evidence
      ├─ mechanistic claims
      ├─ conditions/falsifiers
      └─ structured artifact
      ↓
DETERMINISTIC COMPLETENESS + SOURCE VALIDATION
      ↓
NORMALIZED EVIDENCE / CLAIM FAN-IN
      ↓
CONTRADICTION / ENTITY / CLAIM INDEX
      ↓
SELECTIVE EVIDENCE VERIFIER
      ↓
SELECTIVE HOSTILE REVIEWER
      ↓
CORPUS SYNTHESIS
```

# 78. Reader output architecture — aggiornamento dopo ARA

Minimum high-value output candidate:

```text
SOURCE
  id / hash / metadata

READING STATUS
  surfaces / completeness

OBSERVATIONS
  positive / negative

EVIDENCE
  verbatim / locator / figure/table
  exact|approximate|unreadable

CLAIMS
  statement
  conditions
  falsification
  dependencies
  evidence links
  status

CONTRADICTIONS
DEAD ENDS
OPEN QUESTIONS
```

Questo è molto più vicino a un Reader artifact che a un summary.

# 79. Visual evidence architecture — aggiornamento dopo ARA

```text
deterministic figure/table inventory
        ↓
render / crop
        ↓
Scientist visual inspection
        ↓
EXACT | APPROXIMATE | UNREADABLE
        ↓
structured evidence
```

Rule:
> **Unreadable is an admissible scientific state; invented precision is not.**

# 80. Scientific memory architecture — aggiornamento dopo ARA

```text
CURRENT BEST MODEL
    logic/current
        │
        ├── claims
        ├── mechanisms
        └── constraints

HISTORY / JOURNEY
    trace
        ├── dead ends
        ├── pivots
        ├── contradictions
        └── revisions

STAGING
    tentative observations/inferences
```

Potentially useful, but must be simplified to avoid recreating heavy governance.

# 81. Cumulative pattern ledger — aggiornamento dopo ARA

| Pattern | Stato cumulativo dopo ARA |
|---|---|
| Bounded-source universal General Scientist | **VERY STRONG / ADOPT CANDIDATE** |
| Full-page + appendix reading obligation | **VERY STRONG / HARDEN deterministically** |
| Exhaustive figure/table inspection | **VERY STRONG / ADOPT CANDIDATE** |
| Exact vs approximate visual evidence | **VERY STRONG** |
| Mechanism claims with Conditions/falsifier | **VERY STRONG / ADOPT CANDIDATE** |
| Load-bearing number verbatim grounding | **VERY STRONG / ADOPT CANDIDATE** |
| Risk-weighted evidence strictness | **STRONGER** |
| Negative/dead-end preservation | **VERY STRONG** |
| Current model vs history | **VERY STRONG / ADOPT CANDIDATE** |
| Progressive crystallization | **STRONGER / BENCHMARK** |
| Grounded inference vs speculative leap | **VERY STRONG / KEEP** |
| Negative-aware retrieval | **STRONGER / ADOPT CANDIDATE** |
| Artifact-local hostile review | **VERY STRONG** |
| Artifact hostile review = source verification | **REJECT equivalence** |
| Kill-shot/falsification gate | **EMERGING / ADOPT CANDIDATE** |
| Durable per-paper scientific artifact | **VERY STRONG** |
| Human-readable state + machine projection | **STRONGER / BENCHMARK** |
| Per-paper artifact → corpus fan-in | **VERY STRONG direction** |
| Equivalent ephemeral Compiler workers | **VERY STRONG** |
| Depth-one fan-out | **VERY STRONG** |
| Paginated no-truncation reading | **VERY STRONG / ADOPT CANDIDATE** |
| Progressive disclosure | **VERY STRONG** |
| One giant 50-paper context | **WEAKER / likely reject** |
| Corpus fan-in as scaling bottleneck | **VERY STRONG** |
| Prompt-only single-writer | **REJECT as hard guarantee** |

# 82. New open questions after ARA

1. Quanto del Compiler contract migliora davvero scientific recall rispetto a un simpler deep-reader prompt?
2. La mandatory figure/table ledger aumenta qualità abbastanza da giustificare il costo su ogni paper?
3. Conditions + falsifier devono essere obbligatori per ogni claim o solo per mechanistic/high-impact claims?
4. Il pattern current-model/history/staging può essere ridotto a 2 livelli senza perdere valore?
5. Quanto costa un per-paper ARA-like artifact rispetto a un più piccolo EvidencePacket?
6. Qual è la minimum source-grounding rule: tutti i claims o solo load-bearing claims?
7. Kill-shot before acceptance migliora realmente falsification quality?
8. Markdown/YAML + derived manifest è sufficiente a 500/5000 papers o serve DB/hybrid?

# 83. Current top Scientist takeaways after ten Tier-1 reviews

1. Keep one broad interchangeable General Scientist contract.
2. Make its natural unit a bounded source/paper packet, not an unbounded corpus.
3. Require deep full-source reading in corpus mode.
4. Verify document/surface completeness outside the model.
5. Treat figures and tables as first-class scientific evidence.
6. Preserve exact/approximate/unreadable distinctions for visual evidence.
7. Produce reusable mechanistic claims, not only summaries.
8. Attach Conditions and falsification to high-impact mechanistic claims.
9. Ground load-bearing quantitative statements strongly.
10. Concentrate forensic evidence overhead where claims are load-bearing.
11. Preserve negative results, dead ends and contradictions.
12. Separate current best model from scientific history without deleting either.
13. Distinguish grounded inference from speculative leap.
14. Retrieve failed/refuted directions when relevant to future reasoning.
15. Keep hostile review separate from original-source evidence verification.
16. Consider a lightweight kill-shot step for major claims.
17. Persist Reader output as durable structured scientific state.
18. Use human-readable artifacts with deterministic machine projections where useful.
19. Fan out bounded units to equivalent ephemeral Readers.
20. Prefer depth-one bounded fan-out over recursive swarms.
21. Never use truncated previews in exhaustive reading mode.
22. Use progressive disclosure over durable state to keep context small.
23. Avoid one monolithic 50-paper Reader context.
24. Treat corpus fan-in—not worker replication—as the primary large-scale scientific bottleneck.
25. Continue broad census now; final LEGEND integration remains minimal, surgical and ablation-tested.


# 84. Review 11 — Scholar Loop

Repository analizzata: `renee-jia/scholar-loop`

## 84.1 Nuovi spunti utili per gli Scientist LEGEND

### A. Stateless scientific workers
Scholar Loop usa agenti sostanzialmente stateless mentre lo stato durevole vive in ledger/registry/skills.

Per LEGEND:
> **worker context should be disposable; scientific state should survive externally.**

Questo rafforza fortemente quanto già emerso da CORAL, Paperclip, ATHENA e ARA.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### B. Strict structured I/O for agent outputs
`Agent` usa JSON schema + retry/postcheck.

Per LEGEND questo suggerisce che i passaggi tra Scientist, Reviewer e runtime dovrebbero avere output minimi e machine-checkable.

**Stato:** VERY STRONG.

---

### C. Truth-producing boundary: producer cannot self-certify
Il pattern più forte della repo è:

```text
editable producer
→ artifact
→ pristine frozen evaluator
→ trusted measurement
```

Per LEGEND:
> **a scientific producer should not be authoritative for the truth value of its own artifact/result.**

Questo converge fortemente con ARIS, CORAL, DisMech.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### D. Validate the artifact, not the producer's report
Scholar Loop ignora il training stdout per il metric e valuta il vero model artifact con frozen scorer.

Lezione trasferibile:
> **review the underlying artifact/source/result, not merely the narrative summary produced by the Scientist.**

**Stato:** VERY STRONG.

---

### E. Experimental truth boundary is much stronger than literature grounding
Questa repo rende molto chiara una distinzione:
- computational result verification: strong;
- literature source support: weak.

Per LEGEND:
> **truth boundary must be designed separately for each evidence modality.**

**Stato:** STRONGER distinction.

---

### F. Cheap-before-expensive evaluation
Scholar Loop usa smoke → verify → full.

Per LEGEND può tradursi in:
```text
cheap deterministic checks
→ selective semantic review
→ expensive hostile review only if needed
```

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### G. Multi-fidelity scientific evaluation
Non ogni candidate merita il massimo costo.

Questo converge con Gemma risk-based review.

**Stato:** STRONGER.

---

### H. Persistent experiment ledger
`experiments.jsonl` conserva:
- hypothesis;
- config;
- result;
- fidelity;
- metric;
- verdict;
- parent;
- reasoning.

Per LEGEND:
> **scientific attempts should form an appendable durable ledger, especially for computation/experiments.**

**Stato:** STRONGER.

---

### I. Verified numeric registry
Scholar Loop conserva misure trusted separatamente dal prose writer.

Questo è un pattern molto utile:
```text
measured fact store
≠
narrative scientific interpretation
```

**Stato:** VERY STRONG / ADOPT CANDIDATE for computational evidence.

---

### J. Numeric grounding audit before publication
Writer non dovrebbe poter introdurre numeri che non esistono nel registry.

Per LEGEND:
> **all quantitative claims derived from computation should resolve to verified measured values.**

**Stato:** VERY STRONG.

---

### K. Debate panel is selection review, not truth verification
Critics decidono se un esperimento vale la pena di essere eseguito.

Questo rafforza la separazione:
- candidate triage;
- evidence verification;
- hostile review;
- evaluator.

**Stato:** VERY STRONG distinction.

---

### L. Persona debate should be selective
Innovator/Pragmatist/Contrarian possono migliorare proposal diversity, ma non vanno usati come proof.

**Stato:** BENCHMARK / selective only.

---

### M. Stateless specialist modes
Director, LitScout, Reasoner, Critic, Reflector, Advisor, Writer, Reviewer sono task-scoped.

Questo rafforza:
> **specialization can be ephemeral and context-specific.**

**Stato:** VERY STRONG.

---

### N. Narrow role-specific context
Ogni ruolo riceve solo il contesto necessario.

Per LEGEND:
> **do not expose all durable state to every role.**

**Stato:** VERY STRONG.

---

### O. Reflection → skill memory
Reflector produce lessons persistibili.

Questo può essere utile per Metacognition/Scientist learning, ma solo se:
- provenance exists;
- stale lessons decay;
- relevance is ranked.

**Stato:** STRONGER / BENCHMARK.

---

### P. Deterministic skill relevance/decay
Scholar Loop non carica tutto il history: seleziona lessons rilevanti.

Questo è molto coerente con ATHENA progressive disclosure.

**Stato:** VERY STRONG.

---

### Q. Skills are memory, not executable plugins
Importante distinzione:
- `SkillLibrary` = lessons/prompt memory;
- capability/plugin = executable tool.

Per LEGEND:
> **do not conflate procedural memory with capabilities.**

**Stato:** STRONGER distinction.

---

### R. Governor as deterministic bounded-autonomy primitive
Cost/round/convergence stop conditions sono software.

Questo rafforza:
> **budget and stopping criteria should not live only in agent judgment.**

**Stato:** VERY STRONG.

---

### S. Convergence/plateau as runtime signal
Advisor può decidere pivot/refine, ma governor misura limiti/round.

Per LEGEND:
> software may detect plateau; Scientist decides what it means scientifically.

**Stato:** STRONGER hybrid boundary.

---

### T. Parallelism should be applied to independent expensive work units
Scholar Loop parallelizza smoke experiments, non ogni cognitive step.

Questo è un pattern di efficienza:
> **parallelize where work units are naturally independent and mergeable.**

**Stato:** STRONGER.

---

### U. Same stateless-worker lifecycle can support future General Scientist Pool
La repo non ha deep readers, ma il suo lifecycle è compatibile con:
```text
Scientist(task) → structured output → durable state
```

Questo rafforza il nostro pool design.

**Stato:** STRONGER.

---

### V. Literature provider failure can silently degrade grounding
Se arXiv/OpenAlex/S2 falliscono, il workflow può continuare con meno evidence.

Per LEGEND:
> **retrieval degradation must become explicit scientific state.**

Converge con Medea e ATHENA.

**Stato:** VERY STRONG.

---

### W. Source string is not evidence
Scholar Loop può persistere una `source` string senza exact source text/locator/support verification.

Questo è un anti-pattern netto per biomedical science.

**Stato:** REJECT.

---

### X. Abstract/summary compression belongs only in discovery mode
`summary[:600]` è efficiente per topic scouting, ma scientificamente insufficiente per bounded deep reading.

**Stato:** REJECT for corpus mode / KEEP discovery only.

---

### Y. Experiment ledger memory is stronger than literature memory
Questa asimmetria è istruttiva:
> **durable state quality should be equally strong for literature evidence and computational evidence.**

**Stato:** STRONGER requirement.

---

### Z. Failure-preserving experiment semantics
Experiment failures are explicit:
- timeout;
- seed failure;
- missing artifact;
- modified scorer;
- killed run.

Questo è un modello migliore rispetto a literature omissions che spariscono.

Per LEGEND:
> **scientific failure should stay typed and durable.**

**Stato:** VERY STRONG.

---

## 84.2 Cosa Scholar Loop indebolisce o lascia unresolved

### Specialist-only pipeline for literature science
**WEAKER / not suitable** for exhaustive corpus work.

### Abstract/summary retrieval as evidence
**REJECT**.

### Persona critics as scientific truth authority
**REJECT**.

### Reflection skills without provenance
**BENCHMARK / harden**.

### Persistent Scientist persona
Nuovamente non supportata.

**WEAKER / reject direction.**

# 85. Aggiornamento del disegno incrementale dopo undici review

```text
SCIENTIST / PRODUCER
      ↓
structured candidate artifact
      ↓
CHEAP DETERMINISTIC CHECKS
      ↓
artifact/source/result validation
      ↓
risk routing
   ┌───────────────┴───────────────┐
   │                               │
   ▼                               ▼
accept low-risk              independent reviewer
                                  ↓
                             hostile/jury if needed
```

For computation:

```text
hypothesis
→ executable artifact
→ frozen evaluator
→ verified registry
→ interpretation
```

For literature:

```text
paper
→ evidence packet
→ source-support verifier
→ claim
```

# 86. Truth-boundary architecture — aggiornamento dopo Scholar Loop

Different evidence modalities need distinct validators:

| Evidence modality | Truth boundary |
|---|---|
| computational metric | frozen deterministic evaluator |
| source existence/hash | deterministic software |
| quote/locator integrity | deterministic software |
| claim supported by source | independent semantic verifier |
| mechanism defensibility | hostile scientific reviewer |
| final numeric prose | registry grounding audit |

### Principle
> **There is no single universal Reviewer; each truth-producing transition needs the cheapest validator capable of establishing its guarantee.**

# 87. Memory architecture — aggiornamento dopo Scholar Loop

```text
DURABLE STATE
  evidence ledger
  claim store
  experiment ledger
  verified registry
  failed ideas
  skills/lessons
        ↓
RELEVANCE / DECAY / RETRIEVAL
        ↓
small task-specific context
```

# 88. Cumulative pattern ledger — aggiornamento dopo Scholar Loop

| Pattern | Stato cumulativo dopo Scholar Loop |
|---|---|
| Stateless ephemeral workers | **VERY STRONG / ADOPT CANDIDATE** |
| Structured agent I/O | **VERY STRONG** |
| Producer ≠ validator | **VERY STRONG / ADOPT CANDIDATE** |
| Validate artifact, not producer narrative | **VERY STRONG** |
| Per-modality truth boundaries | **VERY STRONG** |
| Cheap-before-expensive validation | **VERY STRONG / ADOPT CANDIDATE** |
| Multi-fidelity evaluation | **STRONGER** |
| Persistent experiment ledger | **STRONGER** |
| Verified numeric registry | **VERY STRONG** |
| Numeric grounding audit | **VERY STRONG** |
| Debate as selection only | **VERY STRONG distinction** |
| Ephemeral specialization | **VERY STRONG** |
| Narrow role-specific context | **VERY STRONG** |
| Reflection→skill memory | **STRONGER / BENCHMARK** |
| Skill relevance/decay | **VERY STRONG** |
| Skill memory ≠ executable capability | **STRONGER distinction** |
| Deterministic governor | **VERY STRONG** |
| Plateau detection software + interpretation agentic | **STRONGER** |
| Parallelize independent expensive work units | **STRONGER** |
| Retrieval degradation explicit | **VERY STRONG requirement** |
| Source string as evidence | **REJECT** |
| Abstract summary as corpus evidence | **REJECT** |
| Failure-preserving experiment state | **VERY STRONG** |

# 89. New open questions after Scholar Loop

1. Can a simple `verified fact registry` improve literature quantitative grounding without adding too much schema?
2. Which Reader transitions deserve deterministic validation versus independent semantic verification?
3. Does multi-fidelity review improve quality/cost versus one fresh reviewer?
4. Are Reflector-derived skills helpful for Reader performance, or do they create stale cognitive bias?
5. What skill decay/relevance policy maximizes scientific freshness?
6. Should plateau/convergence trigger synthesis or new search automatically?

# 90. Current top Scientist takeaways after eleven Tier-1 reviews

1. Keep workers stateless/ephemeral whenever possible.
2. Persist scientific state outside worker context.
3. Require strict structured outputs at agent boundaries.
4. Never let the producer self-certify a truth-producing result.
5. Validate the underlying artifact/source/result rather than producer prose.
6. Define separate truth boundaries for literature, computation and synthesis.
7. Use the cheapest reliable validator first.
8. Escalate expensive review only for risk/uncertainty.
9. Preserve verified quantitative facts separately from narrative interpretation.
10. Ground all computational numbers against measured registry values.
11. Keep debate/critics as selection mechanisms, not evidence truth.
12. Keep specialist modes ephemeral and narrowly contextualized.
13. Keep memory bounded through relevance/decay rather than loading everything.
14. Separate learned skills/procedures from executable capabilities.
15. Keep budgets, rounds and hard stopping criteria deterministic.
16. Detect plateau mechanically; interpret/pivot scientifically.
17. Parallelize naturally independent work units, not every cognitive step.
18. Make retrieval/capability degradation explicit.
19. Never treat a source identifier/string as sufficient evidence.
20. Keep abstract-level compression confined to discovery mode.
21. Make literature evidence persistence as rigorous as computational evidence persistence.
22. Preserve failures as typed durable state.
23. Use stateless-worker lifecycle as substrate for the future General Scientist Pool.
24. Keep corpus completeness/task ownership deterministic.
25. Continue broad census now; final LEGEND changes remain surgical and ablation-tested.


# 91. Review 12 — ResearchOS

Repository analizzata: `arnavbathla/ai-scientist` (`ResearchOS`)

## 91.1 Nuovi spunti utili per gli Scientist LEGEND

### A. Deterministic Supervisor over durable scientific state

ResearchOS usa un Supervisor deterministico che sceglie il prossimo stage in base allo stato persistito.

Pattern:

```text
durable state
→ deterministic next action
→ bounded agent task
→ verifier
→ checkpoint
→ repeat
```

Questo è molto forte per LEGEND perché separa:

- scientific reasoning;
- lifecycle/orchestration.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### B. Durable run/task/event/checkpoint model

PostgreSQL conserva:

- run;
- session;
- tasks;
- memories;
- checkpoints;
- events;
- sources;
- hypotheses;
- evidence;
- debates;
- rankings;
- final report.

Questo rafforza:

> **scientific state should survive worker death and not depend on conversation context.**

**Stato:** VERY STRONG.

---

### C. Redis lock + heartbeat + stale recovery

ResearchOS implementa:

```text
one run owner
heartbeat
stale detection
requeue
```

Per LEGEND:

- worker liveness;
- duplicate execution;
- stale recovery;

devono essere software.

**Stato:** VERY STRONG / ADOPT runtime pattern.

---

### D. Run-level scaling ≠ corpus-level Scientist scaling

BullMQ può scalare run indipendenti, ma non crea un ScientistPool dentro una singola run.

Questa distinzione è molto utile:

> **runtime worker concurrency does not imply scientific work-unit parallelism.**

**Stato:** VERY STRONG distinction.

---

### E. Strong run-level state model can be reused for paper-task state

`AgentTask` ha status, priority, parent relation.

La repo non implementa paper claiming, ma dimostra una base che potrebbe essere adattata a:

```text
READY
CLAIMED
RUNNING
COMPLETE
FAILED
STALE
```

**Stato:** STRONGER / BUILD candidate.

---

### F. Hypothesis as first-class structured object

ResearchOS ha una delle rappresentazioni più ricche di hypothesis nel corpus:

- title;
- summary;
- mechanism;
- novelty rationale;
- testability;
- proposed experiment;
- risk;
- confidence/novelty/feasibility/impact/evidence scores;
- parentHypothesisIds;
- status.

Questo rafforza:

> **hypotheses should be durable objects with lineage, not only prose.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### G. Hypothesis lineage

`parentHypothesisIds` rende esplicita evoluzione/combinazione.

Per LEGEND:

```text
HYPOTHESIS
→ derived_from
→ revised_from
→ supersedes
```

può essere molto utile.

**Stato:** STRONGER.

---

### H. SupportType is useful but insufficient alone

ResearchOS usa:

- supports;
- contradicts;
- mixed;
- background;
- unsupported.

Questo rafforza il polarity model già visto in DisMech.

Ma manca l'epistemic type del contenuto.

Quindi:

> **support relation and epistemic type are orthogonal.**

**Stato:** VERY STRONG distinction.

---

### I. Pairwise scientific ranking + deterministic Elo

Pattern:

```text
pairwise model judgment
→ deterministic Elo aggregation
```

Questo può essere utile per prioritizzazione di hypotheses.

Non è evidence verification.

**Stato:** STRONGER / BENCHMARK.

---

### J. Ranking should remain downstream of evidence quality

ResearchOS ranka hypotheses su summaries/mechanisms, non su full raw evidence.

Per LEGEND:

> **do not rank weakly grounded objects with high confidence merely because ranking is structured.**

**Stato:** STRONGER requirement.

---

### K. Reflection / Proximity / Evolution are task profiles, not permanent actors

Questa repo conferma ancora:

- critique;
- clustering;
- evolution;
- synthesis;

possono essere ephemeral task modes.

**Stato:** VERY STRONG.

---

### L. DomainRetrievalAgent is really a tool service

ChEMBL, UniProt, AlphaFold retrieval non richiedono un Scientist identity.

Questo è un esempio molto chiaro di over-agentization evitabile.

**Stato:** REJECT permanent retrieval agent.

---

### M. Structured DB state + Markdown/JSON projection

FinalReport conserva JSON + Markdown.

Questo rafforza un pattern utile:

> **canonical machine-readable state + human-readable projection.**

**Stato:** STRONGER.

---

### N. DB durability ≠ portable scientific state

Se cloni il repo senza DB perdi tutta la scienza prodotta.

Quindi:

> **durability and portability are separate guarantees.**

Per LEGEND serve export/snapshot/versioning.

**Stato:** VERY STRONG distinction.

---

### O. Same-run continuation is real

`appendRunMessage()` può riaprire un run terminale mantenendo tutto lo stato.

Questo è un buon pattern per:

- follow-up;
- new constraints;
- targeted continuation.

**Stato:** STRONGER.

---

### P. Continuation ≠ incremental scientific dependency update

Non esiste:

```text
new paper
→ affected claims
→ reopen mechanisms
```

Quindi continuation manuale e delta-aware science restano distinti.

**Stato:** VERY STRONG distinction.

---

### Q. Memory compaction with preserved identifiers

Dopo molti events, ResearchOS comprime older state mantenendo IDs essenziali.

Questo è utile:

> **compress narrative/event history while preserving addressable scientific objects.**

**Stato:** STRONGER / ADOPT CANDIDATE.

---

### R. Bounded active context over large durable state

`buildContextBlock` usa importance/recentness con char budget.

Questo converge fortemente con ATHENA/ARA/Scholar Loop.

**Stato:** VERY STRONG.

---

### S. Skills injected globally can create prompt bloat

Skills DB-backed vengono iniettate nei model-agent prompts.

Questo evidenzia un anti-pattern potenziale:

> **capability/procedure library should not be globally injected by default.**

Meglio lazy/selective retrieval.

**Stato:** WEAKER global Skill injection.

---

### T. Operational failure visibility is strong

ResearchOS persiste:

- model-agent failure;
- worker crash;
- source API failure;
- ranking failure;
- budget exhaustion.

Questo è un buon pattern.

**Stato:** VERY STRONG.

---

### U. Scientific omission can still look successful

Nonostante il runtime forte, manca:

- bounded corpus;
- full text;
- figures;
- exact quote;
- completeness.

Quindi:

> **runtime success can still conceal scientific incompleteness.**

Convergenza ormai assoluta.

**Stato:** VERY STRONG.

---

### V. “Exact-ish quote” is an anti-pattern

VerificationAgent produce quote model-generated senza exact-match.

Per LEGEND:

> **never call a quote exact unless software reopens and matches it.**

**Stato:** REJECT.

---

### W. Structural verifier ≠ scientific verifier

Task verifier controlla presenza di Evidence rows, non correttezza semantica.

Questo è un esempio molto chiaro di:

```text
output exists
≠
output is scientifically valid
```

**Stato:** VERY STRONG distinction.

---

### X. Completion floors are useful but must measure the right denominator

ResearchOS usa min floors:
- ≥3 hypotheses;
- evidence exists;
- ranking exists;
- evolution exists.

Ma nessuno di questi prova corpus coverage.

Per LEGEND:

> **completion gates must be tied to declared scientific denominator, not only stage outputs.**

**Stato:** VERY STRONG / ADOPT principle.

---

### Y. Context efficiency should happen after extraction, not before inspection

ResearchOS risparmia token selezionando/troncando sources prima che il modello le legga.

Per corpus mode questo è scientificamente pericoloso.

Principio:

> **compress after per-paper evidence extraction, not before full assigned-paper inspection.**

**Stato:** VERY STRONG.

---

### Z. Durable hypothesis loop can sit downstream of deep readers

Il loop nativo:

```text
Generation
→ Reflection
→ Proximity
→ Verification
→ Ranking
→ Evolution
→ MetaReview
```

potrebbe essere riusato **dopo**:

```text
full paper
→ EvidencePacket
```

Questa è una delle migliori implicazioni architetturali della review.

**Stato:** STRONGER / ADOPT CANDIDATE.

---

## 91.2 Cosa ResearchOS indebolisce o lascia unresolved

### Specialist pipeline as corpus architecture
**WEAKER / reject as exhaustive Reader topology.**

### Run-level concurrency as ScientistPool
**REJECT equivalence.**

### Global Skill injection
**WEAKER / likely simplify.**

### Exact-ish quote
**REJECT.**

### Completion based on output counts
**REJECT as corpus completeness.**

### Database-only persistence as portability
**INSUFFICIENT.**

# 92. Aggiornamento del disegno incrementale dopo dodici review

```text
CORPUS / SCIENTIFIC STATE STORE
        │
        ├── sources
        ├── tasks
        ├── evidence
        ├── hypotheses
        ├── reviews
        ├── rankings
        └── events/checkpoints
        │
        ▼
DETERMINISTIC SUPERVISOR
        │
        ▼
NEXT READY SCIENTIFIC TASK
        │
        ▼
EPHEMERAL SCIENTIST / SPECIALIST MODE
        │
        ▼
STRUCTURED OUTPUT
        │
        ▼
DETERMINISTIC VERIFICATION
        │
        ▼
SELECTIVE SEMANTIC REVIEW
        │
        ▼
PERSIST + CHECKPOINT
```

# 93. Completion architecture — aggiornamento dopo ResearchOS

Completion must separate:

```text
PROCESS COMPLETION
all required stages ran
```

from:

```text
CORPUS COMPLETION
all expected papers/surfaces accounted for
```

from:

```text
SCIENTIFIC SUFFICIENCY
enough evidence to support current conclusion
```

These are distinct states.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

# 94. Scientific state portability — aggiornamento

ResearchOS demonstrates that:

```text
durable DB
≠
portable science
```

Target LEGEND should support at least:

```text
EXPORT / SNAPSHOT
source identities
evidence
claims
hypotheses
reviews
events needed for reproducibility
```

without requiring the original runtime DB instance.

# 95. Cumulative pattern ledger — aggiornamento dopo ResearchOS

| Pattern | Stato cumulativo dopo ResearchOS |
|---|---|
| Deterministic Supervisor | **VERY STRONG / ADOPT CANDIDATE** |
| Durable task/event/checkpoint model | **VERY STRONG** |
| Lock/heartbeat/stale recovery | **VERY STRONG** |
| Run concurrency ≠ Scientist concurrency | **VERY STRONG distinction** |
| Paper-level READY/CLAIMED state | **BUILD candidate / critical at scale** |
| Structured Hypothesis object | **VERY STRONG / ADOPT CANDIDATE** |
| Hypothesis lineage | **STRONGER** |
| Support polarity | **VERY STRONG** |
| Support polarity ≠ epistemic type | **VERY STRONG distinction** |
| Pairwise judgment + Elo | **STRONGER / BENCHMARK** |
| Ephemeral task profiles | **VERY STRONG** |
| Retrieval agents as tools/services | **REJECT permanent actor** |
| Machine-readable canonical + human projection | **STRONGER** |
| Durability ≠ portability | **VERY STRONG requirement** |
| Same-run continuation | **STRONGER** |
| Continuation ≠ delta-aware update | **VERY STRONG distinction** |
| Memory compaction preserving IDs | **STRONGER / ADOPT CANDIDATE** |
| Small active context over durable state | **VERY STRONG** |
| Global Skill injection | **WEAKER / simplify** |
| Operational failure visibility | **VERY STRONG** |
| Runtime success ≠ scientific completeness | **VERY STRONG** |
| Model-generated exact-ish quote | **REJECT** |
| Structural verifier ≠ semantic verifier | **VERY STRONG distinction** |
| Completion floors | **KEEP process-level only** |
| Completion tied to corpus denominator | **VERY STRONG requirement** |
| Compress after extraction, not before inspection | **VERY STRONG** |
| Hypothesis loop downstream of evidence packets | **STRONGER / ADOPT candidate** |

# 96. New open questions after ResearchOS

1. Quanto del Supervisor/state model vale la pena riusare versus un kernel ancora più piccolo?
2. Quale subset minimo di task/event/checkpoint tables serve davvero a LEGEND?
3. Hypothesis lineage aumenta scientific utility o solo auditability?
4. Pairwise Elo ranking migliora davvero la selezione di hypotheses rispetto a direct scoring?
5. Quale state export formato rende la scienza portable senza duplicare il DB?
6. Quali Skills devono essere lazy-loaded e quali zero-shot nel General Scientist?
7. Completion should stop on corpus coverage, scientific sufficiency, budget, or a combination?

# 97. Current top Scientist takeaways after twelve Tier-1 reviews

1. Keep scientific workers ephemeral.
2. Keep scientific state durable outside the model.
3. Use a deterministic Supervisor for lifecycle sequencing.
4. Keep task/event/checkpoint state machine-verifiable.
5. Keep lock, heartbeat, stale detection and recovery in software.
6. Do not confuse run-level worker scaling with ScientistPool scaling.
7. Make paper/source tasks explicit and claimable.
8. Keep hypotheses as durable structured objects.
9. Preserve hypothesis lineage where it helps audit/revision.
10. Keep evidence polarity separate from epistemic type.
11. Treat pairwise ranking as prioritization, not truth.
12. Keep specialist phases as task profiles, not permanent identities.
13. Convert retrieval/database “agents” into tools/services where possible.
14. Keep canonical machine state separable from human-readable reports.
15. Make durable scientific state portable/exportable.
16. Distinguish continuation from delta-aware incremental science.
17. Compact context while preserving addressable scientific IDs.
18. Load Skills/procedures selectively, not globally.
19. Preserve explicit operational failures.
20. Remember that operational success does not imply scientific completeness.
21. Never accept model-generated “exact-ish” quotes as exact evidence.
22. Keep structural verification separate from semantic scientific verification.
23. Separate process completion, corpus completion and scientific sufficiency.
24. Compress after evidence extraction, not before assigned-paper inspection.
25. Reuse strong hypothesis-generation/reflection/ranking loops only downstream of auditable full-text evidence.


# 98. Review 13 — llm4xray

Repository analizzata: `zhantaochen/llm4xray`

## 98.1 Nuovi spunti utili per gli Scientist LEGEND

### A. One strong Scientist owns a bounded local scientific loop

Il pattern più forte di `llm4xray` è estremamente semplice:

```text
bounded scientific objective
→ Scientist observes
→ Scientist selects a tool
→ tool changes/measures world state
→ Scientist interprets
→ Scientist replans
→ repeat
```

Non c'è un manager che microrouta ogni passaggio.

Per LEGEND:
> **un General Scientist dovrebbe poter possedere localmente un bounded task end-to-end, entro guardrail e capability autorizzate.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### B. Tool-first specialization

`llm4xray` non crea:

- Fitting Scientist;
- Crystallography Scientist;
- Motor Scientist;
- Image Scientist.

Usa tools deterministici.

Questa è una delle conferme più nette del principio:

> **if a specialized need can be solved by deterministic capability, call the tool instead of spawning another Scientist.**

**Stato:** VERY STRONG.

---

### C. Specialist identity encoded by prompt + capability bundle + environment

L'“AI X-ray Scientist” è specializzato attraverso:

- domain prompt;
- tool vocabulary;
- experiment state;
- multimodal observations;
- simulator/live backend.

Non tramite identità permanente.

Per LEGEND questo rafforza:
> **specialization can be task/profile/tool-driven rather than actor-driven.**

**Stato:** VERY STRONG.

---

### D. External scientific state queried on demand

Il modello non riceve tutto il mondo serializzato nel prompt.

Chiede:

- scan;
- detector image;
- motor state;
- log;
- recent file;

quando gli serve.

Per LEGEND:
> **scientific state should live externally and be progressively disclosed to the Scientist.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### E. Progressive disclosure of world state

`llm4xray` è un ottimo esempio di active context piccolo:

```text
current task
+ only requested scientific observation
```

invece di:

```text
all possible state
```

Questo converge con ATHENA, ARA, Scholar Loop e ResearchOS.

**Stato:** VERY STRONG.

---

### F. Virtual-first scientific development

La repo usa virtual beamline/simulator prima del real deployment.

Pattern generalizzabile quando esiste un model/simulator:

```text
safe/cheap virtual environment
→ benchmark/reliability testing
→ live backend
```

Per LEGEND:
- computational simulations;
- synthetic benchmark corpora;
- controlled scientific test harnesses;

possono essere usati prima di real high-cost operations.

**Stato:** STRONGER / ADOPT CANDIDATE where applicable.

---

### G. Stable scientific interface across simulator/live backend

Lo stesso reasoning loop può passare:

```text
virtual backend
↔
real beamline backend
```

dietro capability simili.

Questo rafforza:
> **scientific reasoning contract should be backend-portable where possible.**

**Stato:** STRONGER.

---

### H. Hidden truth evaluator

Nel simulator esiste ground truth separato dal model belief.

Il sistema può misurare:

- alignment error;
- lattice error.

Questo è importantissimo per benchmarkare agent scientifici.

Per LEGEND:
> **when synthetic/known-truth tasks exist, evaluator truth must remain independent from producer reasoning.**

**Stato:** VERY STRONG / ADOPT BENCHMARK PATTERN.

---

### I. Repeated independent trajectories

La pubblicazione valuta run indipendenti sotto perturbazioni.

Questo rafforza un principio che può diventare centrale nei benchmark Reader:

```text
same scientific task
→ repeated independent trajectories
→ variance / success / failure distribution
```

Non basta un singolo run buono.

**Stato:** VERY STRONG.

---

### J. Perturbation testing

I benchmark introducono:

- random offsets;
- wrong nominal parameters;
- harder multi-grain conditions;
- reduced reasoning budget.

Questo è un pattern eccellente per LEGEND benchmarks:

> **test robustness by changing the scientific conditions, not only by repeating the same clean task.**

**Stato:** VERY STRONG / ADOPT BENCHMARK PATTERN.

---

### K. Multimodal scientific observation

Il Scientist lavora con:

- detector images;
- scan plots;
- state/logs.

Questo rafforza:
> **scientific evidence is not text-only; Reader architecture must treat images/figures/tables as first-class evidence.**

**Stato:** VERY STRONG.

---

### L. Prompt SOP is useful but insufficient for critical invariants

Il long prompt codifica procedure importanti:

- inspect image;
- capture full peak;
- account for offsets;
- avoid implausible lattice changes.

Ma molte non sono machine-enforced.

Per LEGEND:
> **expert procedure may live in prompt, but load-bearing invariants should move into software when checkable.**

**Stato:** VERY STRONG.

---

### M. One-agent simplicity avoids orchestration overhead

La repo non ha:
- planner chain;
- recursive agents;
- reviewers;
- role explosion.

Il vantaggio è:
> **very low coordination overhead.**

Per LEGEND questo è un reminder importante:
> **do not add an agent boundary unless it creates an independent scientific guarantee.**

**Stato:** VERY STRONG.

---

### N. No subagent delegation can be a strength

Quando serve calcolo:
→ tool.

Quando serve observation:
→ tool.

Quindi il sistema evita recursive branch explosion.

Per LEGEND:
> **agent→agent delegation should be reserved for genuinely independent scientific judgment, not computational subroutines.**

**Stato:** VERY STRONG.

---

### O. Experimental closed-loop science

Pattern:

```text
goal
→ action
→ observation
→ interpretation
→ updated belief
→ next action
```

Questo è uno dei loop scientifici più genuini del corpus.

Per LEGEND può essere usato downstream della letteratura:

```text
literature-derived hypothesis
→ computation/experiment
→ result
→ interpretation
→ hypothesis update
```

**Stato:** VERY STRONG.

---

### P. Raw deterministic computation vs interpretation

La repo separa:
- simulation;
- fitting;
- motor state;
- lattice calculation;

da:
- scientific interpretation.

Questo converge fortemente con Medea, Robin, CORAL, Scholar Loop.

**Stato:** VERY STRONG.

---

### Q. Producer vs outcome evaluator separation

L'LLM produce lo stato sperimentale; metriche deterministiche misurano il risultato.

Questa è una forma forte di:
> **producer ≠ evaluator**

ma solo outcome-level.

**Stato:** STRONGER.

---

### R. Evaluator capability isolation is weak

`reveal_true_offsets()` e evaluator methods sono nello stesso experiment object, richiamabile via generic method dispatch.

Quindi il benchmark blindness non è hard-enforced.

Per LEGEND benchmark harness:
> **ground truth/evaluator capabilities must not be reachable by the producer.**

**Stato:** VERY STRONG / HARDEN.

---

### S. Generic `execute_code()` as normal bus is dangerous

Grande flessibilità, ma pessimo authority boundary.

Per LEGEND:
> **use restricted typed scientific capabilities, not unrestricted generic code execution as the default interface.**

**Stato:** REJECT as default scientific bus.

---

### T. Generic `call_method()` should be narrowed

Stesso problema:
- dynamic convenience;
- weak capability isolation.

Meglio:
```text
typed capability
declared input/output
permissions
health
```

**Stato:** STRONGER / HARDEN.

---

### U. Process-local session state is an anti-pattern for durable science

`sessions = {}` significa che process death cancella il working world state.

Per LEGEND:
> **scientific state must survive runtime death.**

**Stato:** REJECT process-local canonical state.

---

### V. Local scientific autonomy can coexist with deterministic infrastructure

`llm4xray` dimostra che si può mantenere il Scientist autonomo senza fargli gestire:

- simulator physics;
- fitting math;
- environment mechanics.

Questo supporta direttamente il nostro obiettivo:
> **scientifically free Scientist, mechanically strong harness.**

**Stato:** VERY STRONG.

---

### W. Sequential dependence should not be parallelized blindly

Nel beamline loop ogni action dipende dalla precedente observation.

Questo ricorda che:
> **not all science should be parallelized just because parallelism is available.**

Per LEGEND:
- paper reads can fan out;
- path-dependent local experiment loops often cannot.

**Stato:** STRONGER.

---

### X. Scientific unit type determines parallelism strategy

`llm4xray` chiarisce tre casi:

```text
independent papers
→ horizontal pool

one path-dependent experiment
→ mostly sequential local loop

independent benchmark trajectories
→ replicated parallel runs
```

**Stato:** VERY STRONG distinction.

---

### Y. On-demand evidence access is more important than global context

Per un futuro Reader:
```text
Scientist receives bounded task
→ asks for exact source surfaces when needed
```

anziché caricare l'intero corpus.

**Stato:** VERY STRONG.

---

### Z. Architecture value may come more from scientific substrate than agent wrapper

La pubblicazione stessa non introduce un nuovo agent algorithm.

Il valore deriva molto da:
- simulator;
- scientific tools;
- multimodal observations;
- evaluator.

Per LEGEND:
> **benchmark the harness/substrate, not only the prompt/persona architecture.**

**Stato:** VERY STRONG.

---

## 98.2 Cosa llm4xray indebolisce o lascia unresolved

### Multi-agent hierarchy
Non necessaria per il suo scientific success.

**Stato:** WEAKER / likely reject as default.

### Permanent specialists
Non supportati.

**Stato:** WEAKER.

### Agent delegation for calculations
Fortemente indebolita.

**Stato:** REJECT.

### Process-local scientific memory
**REJECT.**

### Prompt-only critical scientific invariants
**WEAKER / harden where deterministic.**

### Generic unrestricted execution surface
**REJECT as production default.**

### Literature/corpus capabilities
Praticamente assenti; la repo non informa direttamente:
- evidence packet;
- corpus completeness;
- literature review.

**Stato:** NO SUPPORT / do not infer.

# 99. Aggiornamento del disegno incrementale dopo tredici review

```text
GLOBAL SCIENTIFIC RUNTIME
        │
        ├── deterministic task allocation
        ├── persistent state
        ├── capability registry
        ├── capability health
        ├── retries/recovery
        └── review routing
        │
        ▼
BOUNDED SCIENTIFIC TASK
        │
        ▼
ONE GENERAL SCIENTIST
        │
        ├── observes
        ├── reasons
        ├── selects tool
        ├── interprets
        └── replans
        │
        ▼
TYPED SCIENTIFIC CAPABILITIES
        │
        ├── retrieval
        ├── parsing
        ├── computation
        ├── statistics
        ├── simulation
        └── multimodal evidence
        │
        ▼
STRUCTURED RESULT
        │
        ▼
INDEPENDENT EVALUATOR / REVIEW
```

# 100. Parallelism architecture — aggiornamento dopo llm4xray

```text
INDEPENDENT CORPUS UNITS
→ ScientistPool(N)

PATH-DEPENDENT LOCAL SCIENCE
→ one Scientist closed loop

RELIABILITY BENCHMARK
→ repeated independent trajectories
```

This three-way distinction should remain explicit.

# 101. Benchmark architecture — aggiornamento dopo llm4xray

Potential LEGEND Reader benchmark:

```text
same paper/task
→ repeated independent Scientist runs
→ perturb:
   - context budget
   - model
   - tool availability
   - missing figure
   - misleading abstract
   - contradictory supplement
→ hidden/gold evaluator
→ measure robustness
```

Important metrics:
- scientific recall;
- false positive claims;
- contradiction detection;
- figure/supplement recovery;
- hypothesis diversity;
- run-to-run variance;
- tool-call cost;
- context sensitivity.

# 102. Capability architecture — aggiornamento dopo llm4xray

Target:

```text
Scientist
   ↓
typed capability interface
   ↓
deterministic scientific substrate
   ↓
observation/result
```

Avoid:

```text
Scientist
   ↓
unrestricted execute_code/call_method
```

except sandboxed experimental contexts.

# 103. Cumulative pattern ledger — aggiornamento dopo llm4xray

| Pattern | Stato cumulativo dopo llm4xray |
|---|---|
| One strong Scientist owns bounded local loop | **VERY STRONG / ADOPT CANDIDATE** |
| Tool-first specialization | **VERY STRONG** |
| Specialization by prompt+capability+environment | **VERY STRONG** |
| External scientific state queried on demand | **VERY STRONG / ADOPT CANDIDATE** |
| Progressive disclosure | **VERY STRONG** |
| Virtual-first development | **STRONGER where applicable** |
| Simulator/live backend parity | **STRONGER** |
| Hidden-truth evaluator | **VERY STRONG benchmark primitive** |
| Repeated independent trajectories | **VERY STRONG** |
| Perturbation testing | **VERY STRONG benchmark primitive** |
| Multimodal scientific evidence | **VERY STRONG** |
| Prompt SOP | **KEEP but harden critical checks** |
| Agent hierarchy | **WEAKER as default** |
| Agent delegation for deterministic operations | **REJECT** |
| Experimental closed loop | **VERY STRONG** |
| Raw computation ≠ interpretation | **VERY STRONG** |
| Producer ≠ outcome evaluator | **STRONGER** |
| Evaluator reachable by producer | **REJECT / harden** |
| Generic execute_code as default bus | **REJECT** |
| Generic unrestricted call_method | **HARDEN/NARROW** |
| Process-local canonical state | **REJECT** |
| Sequential dependency-aware execution | **STRONGER** |
| Unit-type-specific parallelism | **VERY STRONG** |
| Harness/substrate benchmark | **VERY STRONG** |
| Corpus/full-text/provenance architecture | **NO SUPPORT from repo** |

# 104. New open questions after llm4xray

1. How much of Reader performance comes from model intelligence vs evidence/tool substrate?
2. Can a single strong General Scientist with excellent tools outperform multi-agent Reader topologies?
3. Which Reader tasks are truly path-dependent and should remain single-loop?
4. What perturbation suite best measures robustness of scientific reading?
5. Can simulator-style hidden truth be created for literature benchmarks using synthetic/annotated corpora?
6. How should evaluator capabilities be isolated so producer cannot access gold truth?
7. Which domain SOP rules deserve deterministic enforcement versus prompt guidance?
8. What is the minimum typed capability boundary that preserves flexibility without unrestricted execution?

# 105. Current top Scientist takeaways after thirteen Tier-1 reviews

1. Keep one strong General Scientist capable of owning a bounded scientific task end-to-end.
2. Give it broad local autonomy inside deterministic system boundaries.
3. Use tools rather than specialist agents for deterministic scientific operations.
4. Encode specialization primarily through task/profile/capability bundles.
5. Keep external scientific state outside the model and retrieve it on demand.
6. Preserve progressive disclosure to keep context small.
7. Use simulator/virtual backends before expensive real operations where possible.
8. Keep scientific interfaces stable across virtual/live backends.
9. Use hidden-truth evaluators whenever known truth can be constructed.
10. Benchmark reliability using repeated independent trajectories.
11. Add controlled perturbations, not only clean repeated runs.
12. Treat multimodal evidence as first-class science.
13. Keep expert SOPs in prompt only where software cannot enforce the invariant.
14. Do not add agent boundaries that provide no independent scientific guarantee.
15. Reserve agent delegation for independent scientific judgment, not calculations.
16. Preserve adaptive experiment/computation loops downstream of literature-derived hypotheses.
17. Keep raw deterministic computation separate from interpretation.
18. Keep evaluator/gold capabilities inaccessible to producers.
19. Avoid unrestricted execute_code/call_method as default production interfaces.
20. Never keep canonical scientific state only in process memory.
21. Respect path dependence: not every scientific loop should be parallelized.
22. Distinguish corpus throughput, local path-dependent execution and benchmark replication.
23. Use on-demand exact evidence access rather than global corpus contexts.
24. Benchmark scientific substrate/harness separately from persona/model effects.
25. Continue the broad census; final LEGEND Reader should implement only the minimum ablation-proven subset.


# 106. Review 14 — AI-Scientist-v2

Repository analizzata: `SakanaAI/AI-Scientist-v2`

## 106.1 Nuovi spunti utili per gli Scientist LEGEND

### A. Ephemeral equivalent workers around durable scientific objects

Il pattern più forte di AI-Scientist-v2 è:

```text
persistent task/result lineage
→ select bounded work units
→ ephemeral equivalent workers
→ structured result nodes
→ deterministic fan-in
```

Il worker non è l'unità scientifica durevole. Lo sono:

- Node;
- Journal;
- stage;
- parent-child lineage.

Per LEGEND:
> **Scientist identity should be disposable; scientific task/result identity should be durable.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### B. Horizontal parallelism with bounded equivalent workers

`ParallelAgent` usa `ProcessPoolExecutor(max_workers=N)` e workers equivalenti.

Questo è una delle implementazioni più concrete del pattern:

```text
ScientistPool(size=N)
```

anche se il task nativo è experiment-tree node e non paper.

Per LEGEND:
> **the mechanical pool pattern is reusable even if the scientific work unit changes from experiment node to paper/evidence task.**

**Stato:** VERY STRONG.

---

### C. N is deployment policy, not role semantics

`num_workers` è configurabile e limitato dalle GPU disponibili.

Questo rafforza:
> **N should be runtime/deployment policy, not a semantic property of Scientist role.**

**Stato:** VERY STRONG.

---

### D. Bounded tree search

AI-Scientist-v2 evita branch explosion con:

- `num_workers`;
- `num_drafts`;
- `max_debug_depth`;
- stage iteration ceilings;
- execution timeouts;
- `num_seeds`.

Questo è molto importante.

Per LEGEND:
> **scientific branching may exist, but breadth/depth/budget must be explicit and bounded.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### E. Independent draft roots for diversity

Multiple draft roots permettono exploration diversity senza creare permanent teams.

Per LEGEND questo può ispirare:

```text
high-value hypothesis task
→ K independent candidate trajectories
→ compare / retain diverse survivors
```

Non per ogni paper.

**Stato:** STRONGER / BENCHMARK.

---

### F. Selective replication after candidate importance is established

Il best node viene poi sottoposto a multi-seed evaluation.

Pattern:

```text
many cheap candidates
→ select promising
→ replicate important candidate
```

Per LEGEND:
> **redundancy should often be selective and importance-triggered, not universal.**

Applicazioni:
- high-impact paper double read;
- major mechanistic claim;
- computational hypothesis.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### G. Real execution validates computational proposals

Generated Python viene realmente eseguito.

Questo rafforza fortemente:

```text
proposed computation
≠
executed computation
```

Per LEGEND:
> **computational claims should derive from actual execution artifacts, not LLM-described results.**

**Stato:** VERY STRONG.

---

### H. Raw result vs interpretation separated in persistent state

Il sistema conserva:

- code;
- terminal output;
- `.npy`;
- metric;
- plot;

separatamente da:

- `analysis`;
- VLM interpretation;
- summaries.

Questo è un pattern scientifico molto forte.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### I. Node/Journal lineage

Parent-child lineage rende esplicito come un candidate scientifico evolve.

Per LEGEND:
- hypothesis refinement;
- computation variants;
- alternative mechanism trajectories;

possono usare una lineage simile.

**Stato:** STRONGER.

---

### J. Centralized anti-duplication before parallel execution

Hyperparameter/ablation ideas vengono tracciate centralmente per evitare duplicazioni.

Per LEGEND:
> **dedup scientific work units before dispatching expensive workers.**

**Stato:** STRONGER / ADOPT CANDIDATE.

---

### K. Stage-local context

Workers ricevono:

- current task;
- stage;
- parent node;
- memory summary;
- relevant metric.

Non tutto il global history.

Questo converge fortemente con ATHENA, ARA, ResearchOS, Scholar Loop.

**Stato:** VERY STRONG.

---

### L. Hierarchical summaries reduce context burden

Journal summary + stage summaries + filtered writeup context sono una forma di fan-in gerarchico.

Per LEGEND:
> **large corpus synthesis should operate on structured intermediate summaries/evidence packets, not raw whole-corpus context.**

**Stato:** VERY STRONG.

---

### M. VLM feedback on scientific plots

La repo usa VLM per interpretare experiment plots.

Questo rafforza:
> **visual scientific evidence should be independently inspectable by a vision-capable reasoning step.**

Per il Reader:
- figures;
- panels;
- plots;

devono essere first-class.

**Stato:** VERY STRONG.

---

### N. PDF figure/caption review already exists—but only for generated manuscript

La repo mostra un pattern che può essere rewired:

```text
PDF
→ extract figures
→ VLM inspect
→ caption/reference review
```

Per LEGEND può diventare:
```text
source paper PDF
→ figure extraction
→ Scientist/VLM scientific interpretation
```

**Stato:** STRONGER / REUSE PATTERN, not native source evidence.

---

### O. Fresh manuscript reviewer

Final writer e reviewer sono separati.

Questo rafforza:
> **fresh final review after synthesis is useful, but must reopen source evidence if the guarantee is evidence validity.**

**Stato:** STRONGER.

---

### P. Reviewer of prose ≠ evidence verifier

La repo rende molto chiara questa distinzione:

```text
generated manuscript
→ critic
```

non equivale a:

```text
claim
→ reopen original source
→ verify support
```

**Stato:** VERY STRONG distinction.

---

### Q. Producer≠validator is strongest in computation

Code producer:
→ actual Interpreter run.

Feedback/VLM:
→ separate evaluator paths.

This is much stronger than literature-side validation.

Per LEGEND:
> **extend execution-backed truth boundaries to every modality where deterministic validation is possible.**

**Stato:** VERY STRONG.

---

### R. Fixed staged specialization does not imply permanent actor identity

Ideation, feedback, VLM, citations, writeup, review sono task-scoped functions.

Per LEGEND:
> **specialization should remain ephemeral unless persistent identity adds measurable scientific value.**

**Stato:** VERY STRONG.

---

### S. Parallel workers do not claim tasks from a durable queue

Il manager centralmente seleziona e `submit()`.

Questo è utile ma non sufficiente per corpus scale.

Per LEGEND:
> **paper Scientist pool still needs atomic READY→CLAIMED semantics.**

**Stato:** STRONGER BUILD requirement.

---

### T. Central manager assignment may become fan-in bottleneck

Il sistema ha central Journal/manager selection.

A 500/5000 papers:
> **central selection/fan-in can saturate before worker pool.**

Questo converge con il nostro bottleneck hypothesis.

**Stato:** VERY STRONG.

---

### U. Selective branch survival can erase minority science

Branches non best possono essere:
- deprioritized;
- compressed;
- omitted from writeup.

Per LEGEND:
> **negative/minority evidence must survive even if its producing trajectory loses ranking.**

**Stato:** VERY STRONG requirement.

---

### V. Citation search/abstract layer is discovery-only

Semantic Scholar fornisce abstract-level support.

Per LEGEND:
> **abstract-level retrieval is excellent for discovery and novelty search, not for bounded corpus evidence.**

**Stato:** VERY STRONG distinction.

---

### W. Citation existence ≠ claim support

La repo può produrre polished manuscript + BibTeX, ma senza source-grounded verification.

Questo rafforza una convergenza ormai assoluta.

**Stato:** VERY STRONG.

---

### X. Checkpoint writing is useful but restore semantics must be proven

`checkpoint.pkl` e `manager.pkl` vengono scritti.

Ma full fresh-process resume non è dimostrato nel trace.

Per LEGEND:
> **checkpoint existence ≠ recovery guarantee.**

Need:
```text
kill process
→ fresh process
→ restore
→ same semantic state
```

**Stato:** VERY STRONG / BENCHMARK.

---

### Y. Run-directory persistence is durable but not canonical portability

Experiment artifacts sopravvivono su disk, ma non diventano automaticamente portable scientific state.

Per LEGEND:
> **durable run folder should be exportable/replayable independently of local runtime.**

**Stato:** STRONGER.

---

### Z. Bounded delegation is preferable to recursive free-form agent trees

AI-Scientist-v2 ha una delegated tree, ma hard-bounded.

Questo è un buon compromesso:
> **allow bounded branch exploration only where the scientific search space benefits.**

**Stato:** VERY STRONG.

---

## 106.2 Cosa AI-Scientist-v2 indebolisce o lascia unresolved

### Fixed worker count as scientific design
**REJECT.** N should remain parametric/deployment-controlled.

### Central manager assignment as large-corpus scheduler
**WEAKER at scale.**

### Abstract-level literature layer
**REJECT as corpus evidence.**

### Manuscript review as evidence verification
**REJECT equivalence.**

### Unrestricted generated code under normal OS authority
**REJECT as production default; sandbox required.**

### Best-path-only memory
**WEAKER; minority/negative trajectories must persist.**

# 107. Aggiornamento del disegno incrementale dopo quattordici review

```text
DURABLE SCIENTIFIC TASK STORE
        │
        ├── task id
        ├── parent/lineage
        ├── priority
        ├── state
        └── output pointer
        │
        ▼
READY TASK QUEUE
        │
        ▼
EPHEMERAL GENERAL SCIENTIST POOL (N)
        │
        ├── equivalent workers
        ├── local context
        ├── bounded branch budget
        └── tools
        │
        ▼
STRUCTURED RESULT OBJECT
        │
        ├── evidence
        ├── raw execution
        ├── interpretation
        ├── uncertainty
        └── lineage
        │
        ▼
DETERMINISTIC FAN-IN / DEDUP
        │
        ▼
SELECTIVE REPLICATION / REVIEW
        │
        ▼
HIERARCHICAL SYNTHESIS
```

# 108. Replication architecture — aggiornamento dopo AI-Scientist-v2

Three distinct redundancy regimes:

```text
A. exploration diversity
   multiple draft trajectories

B. robustness replication
   same promising candidate × multiple seeds/runs

C. independent scientific validation
   fresh reviewer / verifier
```

These must not be conflated.

# 109. Worker architecture — aggiornamento

Target Scientist worker:

```text
ephemeral process/model instance
+
durable task ID
+
durable result object
+
optional parent lineage
```

No permanent Scientist name is scientifically required.

# 110. Cumulative pattern ledger — aggiornamento dopo AI-Scientist-v2

| Pattern | Stato cumulativo dopo AI-Scientist-v2 |
|---|---|
| Ephemeral equivalent worker pool | **VERY STRONG / ADOPT CANDIDATE** |
| Durable work identity in task/result object | **VERY STRONG** |
| N as deployment policy | **VERY STRONG** |
| Bounded branch breadth/depth | **VERY STRONG / ADOPT CANDIDATE** |
| Independent draft roots | **STRONGER / BENCHMARK** |
| Selective replication after importance | **VERY STRONG / ADOPT CANDIDATE** |
| Real execution validates computation | **VERY STRONG** |
| Raw result ≠ interpretation | **VERY STRONG / ADOPT CANDIDATE** |
| Node/Journal lineage | **STRONGER** |
| Central anti-duplication | **STRONGER / ADOPT CANDIDATE** |
| Stage-local context | **VERY STRONG** |
| Hierarchical summaries | **VERY STRONG** |
| VLM scientific plot review | **VERY STRONG** |
| Source figure review pattern | **STRONGER / REWIRE candidate** |
| Fresh final reviewer | **STRONGER** |
| Reviewer prose ≠ evidence verifier | **VERY STRONG distinction** |
| Producer≠validator strongest via execution | **VERY STRONG** |
| Ephemeral specialization | **VERY STRONG** |
| Atomic dynamic claiming | **CRITICAL BUILD requirement** |
| Central fan-in bottleneck | **VERY STRONG scaling concern** |
| Minority evidence preservation | **VERY STRONG requirement** |
| Abstract-level discovery | **KEEP discovery only** |
| Citation existence ≠ source support | **VERY STRONG** |
| Checkpoint existence ≠ resume guarantee | **VERY STRONG / BENCHMARK** |
| Run-folder durability ≠ portability | **STRONGER requirement** |
| Bounded delegation | **VERY STRONG** |
| Recursive unbounded delegation | **REJECT** |
| Generated code without sandbox | **REJECT as production default** |

# 111. New open questions after AI-Scientist-v2

1. What is the optimal bounded branching policy for literature-derived hypothesis exploration?
2. Can `Node/Journal`-like lineage be simplified enough for claims/hypotheses without becoming heavy governance?
3. When should a high-impact paper/claim trigger selective replication?
4. Does independent draft diversity improve scientific novelty enough to justify extra cost?
5. How much central fan-in can one Synthesis Scientist handle before hierarchical sharding is required?
6. What checkpoint/recovery test should be mandatory before claiming resumability?
7. Can VLM figure-review logic materially improve Reader recall on source papers?
8. How should non-winning/minority branches be retained without flooding context?

# 112. Current top Scientist takeaways after fourteen Tier-1 reviews

1. Keep equivalent Scientist workers ephemeral.
2. Put durable identity in tasks/results, not worker names.
3. Make N a deployment/runtime policy.
4. Use bounded branch breadth/depth/timeout budgets.
5. Allow independent candidate trajectories only where diversity matters.
6. Replicate promising high-impact candidates selectively.
7. Require real execution for computational scientific claims.
8. Persist raw computation separately from interpretation.
9. Preserve parent/child lineage for evolvable scientific objects.
10. Deduplicate expensive work before parallel dispatch.
11. Keep worker context local and stage/task-specific.
12. Use hierarchical summaries/evidence packets for fan-in.
13. Treat visual scientific evidence as first-class.
14. Reuse VLM figure-review patterns on source figures, not just generated papers.
15. Keep final prose review separate from evidence verification.
16. Extend producer≠validator via deterministic execution wherever possible.
17. Keep specialist functions ephemeral.
18. Add atomic dynamic claiming for real corpus Scientist pools.
19. Treat central synthesis/fan-in as a likely scaling bottleneck.
20. Preserve minority/negative branches even when they lose ranking.
21. Keep abstract search strictly as discovery/novelty support.
22. Never equate citation existence with claim support.
23. Prove resume semantics by kill/restart tests, not checkpoint existence.
24. Keep durable run state portable/replayable.
25. Continue broad census now; final LEGEND Reader remains minimum-harness, ablation-driven and surgical.


# 113. Review 15 — OpenScientist

Repository analizzata: `openscientist-io/openscientist`

## New Scientist patterns

### 1. One strong interchangeable General Scientist
Canonical OpenScientist runs one scientific producer per job, with tools, skills, persistent state and iterative hypothesis-driven work.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

### 2. Skills-before-actors
Genomics, metabolomics, data science, structural biology, hypothesis generation, prioritization, result interpretation and stopping criteria are skills/tools around the same generalist rather than permanent scientific identities.

**Stato:** VERY STRONG.

### 3. Provider ≠ harness
`AbstractAgent`/factory separate scientific role from model/provider/runtime harness (Claude Code, Codex, OMP).

**Stato:** VERY STRONG / ADOPT CANDIDATE.

### 4. Persistent KnowledgeState
Hypotheses, findings, literature, analysis logs, iteration summaries, feedback and consensus survive outside conversation.

**Stato:** VERY STRONG.

### 5. Structured hypotheses and negative outcomes
Hypotheses have durable status such as pending/testing/supported/rejected.

**Stato:** VERY STRONG.

### 6. Evidence ≠ biological interpretation
Findings distinguish at least `evidence` from `biological_interpretation`.

**Stato:** STRONGER / ADOPT CANDIDATE.

### 7. Corpus transport ≠ corpus execution
OpenScientist can accept/copy all 50 files and persist metadata, but this does not create paper tasks, read receipts, or a completion denominator.

**Stato:** VERY STRONG distinction.

### 8. Document access ≠ deep-reading proof
PyMuPDF reading exists, but invocation is optional and there is no per-page/per-surface completion record.

**Stato:** VERY STRONG distinction.

### 9. 100k-character truncation is incompatible with exhaustive corpus mode
Truncation is disclosed but not automatically repaired/chunked.

**Stato:** REJECT for corpus completeness.

### 10. Parser quality must be explicit
No native OCR fallback means scanned/image PDFs can degrade while the job continues.

**Stato:** VERY STRONG requirement.

### 11. Figure/table/supplement access ≠ completeness
Selected surfaces can be inspected through tools/code, but there is no deterministic all-surface inventory/gate.

**Stato:** CRITICAL BUILD requirement.

### 12. Warning-only citation mismatch is unsafe
Abstract citation matching can return mismatch/unchecked while the finding remains admitted.

**Stato:** REJECT.

### 13. Literal citation matching remains useful as a cheap pre-gate
Exact/normalized abstract substring validation is a low-cost deterministic check, but not semantic evidence verification.

**Stato:** KEEP as mechanical pre-gate.

### 14. Same-agent synthesis is efficient but correlated
The same Discovery Agent reads, hypothesizes, interprets, records and synthesizes.

**Stato:** KEEP for low-risk/exploratory mode; not universal high-rigor validation.

### 15. Real computational loop
`hypothesis → code → isolated executor → raw output → interpretation → hypothesis update`.

**Stato:** VERY STRONG.

### 16. Raw computation ≠ interpretation
Code/output/plots/logs are separable from biological interpretation.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

### 17. Dynamic skill lifecycle
`SkillSyncScheduler` supports startup/periodic sync, SHA cache, rate limits, persisted error state and forced sync.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

### 18. Context reset with durable-state reconstruction
Scientific continuity can survive runtime/session reset because persisted state is re-injected.

**Stato:** VERY STRONG.

### 19. On-demand evidence access
Documents and PubMed are queried as needed rather than loading the whole corpus into context.

**Stato:** VERY STRONG, but Discovery-mode strength only unless paired with deterministic corpus tasks.

### 20. Whole-job concurrency ≠ ScientistPool
`max_concurrent` runs independent jobs, not multiple Scientists over one shared scientific task graph.

**Stato:** VERY STRONG distinction.

### 21. Honest restart cancellation
Stale running jobs are cancelled after service restart instead of being falsely called resumable.

**Stato:** VERY STRONG.

### 22. Persistence ≠ resumability
DB/files can survive while the active scientific process cannot resume.

**Stato:** VERY STRONG distinction.

### 23. Artifact freshness check
Report generation verifies a fresh artifact was actually written and retries boundedly.

**Stato:** STRONGER / ADOPT CANDIDATE.

### 24. Transcript normalization
Cross-harness runtime traces are normalized, useful for audit, Metacognition and benchmarking.

**Stato:** STRONGER / ADOPT CANDIDATE.

### 25. Report regeneration ≠ incremental scientific update
A completed job can regenerate a report from prior state, but there is no native `+5 papers → affected claims → selective reopen` loop.

**Stato:** VERY STRONG distinction.

## Patterns strengthened

- Generalist-first topology.
- Skills/tools before specialist actors.
- Persistent scientific state outside chat context.
- Provider/runtime neutrality.
- Real executable computation.
- On-demand context retrieval.
- Small active context over durable state.
- Explicit operational lifecycle and failure states.
- Permanent specialist identities are increasingly unjustified by evidence.

## Patterns weakened

- One-agent topology as a universal scaling solution.
- Warning-only grounding failures.
- Treating PDF access as proof of corpus coverage.
- Treating whole-job concurrency as intra-corpus parallelism.
- Treating persistence as resume semantics.
- Treating search-driven adaptive reading as exhaustive corpus processing.

## Scaling implications

### ~50 papers
A high-rigor minimal configuration could plausibly be:

```text
1–3 General Scientists
+ deterministic corpus completeness
+ exact evidence packets
+ selective fresh review
```

A Scientist pool helps latency but is not required to establish correctness.

### ~500 papers
Need:
- real ScientistPool;
- dynamic claiming;
- dedup/entity normalization;
- structured fan-in.

### ~5,000 papers
Need:
- hierarchical synthesis;
- delta-aware updates;
- sharded reducers/state;
- review routing;
- provider backpressure.

## Review implications

Canonical OpenScientist has no independent scientific reviewer. The best future pattern remains:

```text
cheap deterministic grounding
→ semantic evidence verifier for selected claims
→ hostile reviewer only for major/high-risk conclusions
```

## Evidence/provenance implications

OpenScientist's PMID + abstract-snippet linkage is useful but insufficient. The target remains:

```text
source ID/hash
+ exact evidence
+ precise locator
+ claim link
+ epistemic type
+ review status
```

## Context/token implications

OpenScientist strongly supports:
- on-demand source access;
- persistent state outside context;
- summary budgets;
- runtime reset.

But compression can hide minority/contradictory evidence unless it has already been promoted into durable structured scientific state.

## Changes to provisional design

```text
DETERMINISTIC CORPUS/TASK LAYER
        ↓
INTERCHANGEABLE GENERAL SCIENTIST
        ↓
SELECTIVELY LOADED SKILLS/TOOLS
        ↓
PERSISTENT SCIENTIFIC STATE
        ↓
RISK ROUTER
    low-risk → synthesize
    high-risk → fresh verifier/reviewer
        ↓
HIERARCHICAL SYNTHESIS
```

Key identity separation:

```text
ROLE ≠ SKILL ≠ TOOL ≠ MODEL ≠ HARNESS
```

Completeness states should not collapse:

```text
FILE PRESENT
≠ FILE PARSED
≠ FILE INSPECTED
≠ SCIENTIFICALLY CONSUMED
```

## New unresolved questions

1. At 50 papers, does 1 strong Scientist + deterministic completeness beat 3 parallel Scientists after cost normalization?
2. Which `KnowledgeState` fields improve scientific accuracy versus only auditability?
3. How much skill lifecycle machinery is actually necessary in LEGEND?
4. Should citation mismatch hard-block all findings or only load-bearing findings?
5. What is the minimum parser-completeness state needed to catch truncation/OCR/figure/supplement failure?
6. Does periodic context reset improve scientific freshness?
7. At what corpus size does single-agent synthesis materially lose minority evidence?
8. Which exact state must be exported for true cross-machine scientific portability?
9. Can OpenScientist-style whole-job state machinery be simplified into paper-task machinery?
10. Is report regeneration from durable state useful once canonical scientific state exists?

# 114. Cumulative Pattern Ledger — delta after OpenScientist

| Pattern | Stato cumulativo |
|---|---|
| One strong interchangeable General Scientist | **VERY STRONG / ADOPT CANDIDATE** |
| Skills-before-actors | **VERY STRONG** |
| Provider ≠ harness | **VERY STRONG / ADOPT CANDIDATE** |
| Runtime-neutral tool surface | **VERY STRONG** |
| Persistent scientific state outside conversation | **VERY STRONG** |
| Structured hypotheses | **VERY STRONG** |
| Evidence ≠ interpretation | **VERY STRONG** |
| Curator as permanent actor | **WEAKER / likely reject** |
| Corpus transport ≠ corpus execution | **VERY STRONG distinction** |
| Document access ≠ deep-reading proof | **VERY STRONG distinction** |
| Character truncation in corpus mode | **REJECT** |
| Parser quality/completeness state | **VERY STRONG requirement** |
| Figure/table/supplement completeness | **CRITICAL BUILD requirement** |
| Warning-only citation mismatch | **REJECT** |
| Literal citation match as early gate | **KEEP** |
| Literal match ≠ semantic support | **VERY STRONG distinction** |
| Same-agent synthesis | **KEEP low-risk mode only** |
| Independent scientific review on canonical main | **ABSENT** |
| Real computation loop | **VERY STRONG** |
| Raw computation ≠ interpretation | **VERY STRONG** |
| Isolated execution | **VERY STRONG** |
| Dynamic skill lifecycle | **VERY STRONG / ADOPT CANDIDATE** |
| Context reset from durable state | **VERY STRONG** |
| On-demand source access | **VERY STRONG but mode-dependent** |
| Context compression over durable objects | **VERY STRONG requirement** |
| Whole-job concurrency ≠ ScientistPool | **VERY STRONG distinction** |
| Honest restart cancellation | **VERY STRONG** |
| Persistence ≠ resumability | **VERY STRONG distinction** |
| Artifact freshness check | **STRONGER / ADOPT CANDIDATE** |
| Transcript normalization | **STRONGER / ADOPT CANDIDATE** |
| Report regeneration ≠ incremental science | **VERY STRONG distinction** |
| Small-scale topology ≠ large-scale topology | **VERY STRONG** |

# 115. Current top Scientist takeaways after fifteen Tier-1 reviews

1. Keep one broad interchangeable General Scientist contract.
2. Default specialization to skills/tools before new actors.
3. Keep role identity independent from provider/model/harness.
4. Keep scientific capabilities behind stable runtime-neutral interfaces.
5. Persist scientific state outside conversational memory.
6. Keep hypotheses and rejected outcomes as durable objects.
7. Separate evidence from biological interpretation.
8. Avoid permanent Curator identity unless benchmark proves value.
9. Distinguish corpus transport from corpus execution.
10. Distinguish document access from proof of deep reading.
11. Never allow untracked truncation in exhaustive corpus mode.
12. Make parser/OCR/surface completeness explicit.
13. Treat figures/tables/supplements as first-class expected source surfaces.
14. Use literal citation matching only as a cheap pre-gate.
15. Never admit load-bearing findings after failed grounding without an explicit unresolved state.
16. Keep same-agent synthesis for low-risk/exploratory work, not as universal validation.
17. Preserve real executable computation and raw-output logging.
18. Keep computation isolated from scientific interpretation.
19. Treat skill lifecycle/version/health as infrastructure, not Scientist cognition.
20. Allow context reset if durable scientific state can reconstruct continuity.
21. Keep source access on-demand, but pair it with deterministic corpus tasks in exhaustive mode.
22. Keep whole-job concurrency conceptually separate from ScientistPool scaling.
23. Be honest when restart means cancellation rather than resume.
24. Distinguish persistence, resumability and portability as separate guarantees.
25. Scale topology only when corpus size demands it; final LEGEND Reader remains minimum-harness and benchmark-driven.


# 121. Review 16 — BioDSA / DeepEvidence

Repository analizzata: `RyanWangZf/BioDSA` — componente `DeepEvidence`

## 121.1 Nuovi spunti utili per gli Scientist LEGEND

### A. Breadth-vs-depth specialization
DeepEvidence implementa due modalità scientifiche distinte:

```text
BFRS/BFS = broad search
DFRS/DFS = deep search
```

Questa è una specializzazione utile perché cambia davvero la strategia di ricerca, non solo il nome del ruolo.

Per LEGEND:
> **breadth/depth can be explicit task modes of an otherwise common Scientist contract.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### B. Focused delegation contract
L'Orchestrator delega tramite:

```text
search_target
+ selected knowledge bases
+ search/action budget
```

Questo produce child context stretto e task-local.

Per LEGEND:
> **subanalysis delegation should pass a narrow scientific objective and capability allowlist, not the whole global context.**

**Stato:** VERY STRONG.

---

### C. Bounded delegation
BFRS/DFRS sono limitati da round/action budgets.

Questo rafforza:
> **scientific delegation can remain useful without becoming recursive or unbounded.**

**Stato:** VERY STRONG.

---

### D. Ephemeral specialist modes, not permanent identities
BFRS/DFRS sono invocazioni temporanee e non attori scientifici persistenti.

**Stato:** VERY STRONG.

---

### E. Retrieval/tool substrate contributes much of the scientific power
PubMed/PMC/PubTator e i database gene/disease/drug/target/pathway/compound/variant/trials rappresentano una parte enorme del valore scientifico.

Per LEGEND:
> **benchmark retrieval/tool substrate separately from orchestration/persona quality.**

**Stato:** VERY STRONG.

---

### F. Tool-level parallelism ≠ Scientist-level parallelism
Alcuni tool usano batching/threading, ma DeepEvidence stesso resta sostanzialmente sequenziale.

Questa distinzione è fondamentale:

```text
parallel API retrieval
≠
parallel scientific reasoning workers
```

**Stato:** VERY STRONG distinction.

---

### G. Single sequential Orchestrator is a scientific throughput bottleneck
Il path nativo è:

```text
Orchestrator
→ one BFRS or DFRS
→ return
→ Orchestrator
```

e `parallel_tool_calls=False`.

Per 500/5000 papers:
> **the reasoning control path saturates before the retrieval substrate.**

**Stato:** VERY STRONG scaling concern.

---

### H. Search-driven deep research ≠ bounded corpus execution
DeepEvidence parte da una scientific question e cerca ciò che ritiene rilevante.

Non crea:
- one task per supplied paper;
- 50/50 denominator;
- paper ownership/completion.

**Stato:** VERY STRONG distinction.

---

### I. Generic framework capability must not be credited to native workflow
BioDSA possiede `ReadPdfTool`/`ReadImageTool`, ma DeepEvidence non li espone nel tool mapping ispezionato.

Questa è un'importante regola metodologica:
> **framework-level capability ≠ component-native capability unless wired into the actual execution trace.**

**Stato:** VERY STRONG benchmark discipline.

---

### J. Filtered passage retrieval is not full-paper reading
`FetchPaperContentTool` filtra contenuto in base a keywords/regex e restituisce contesto locale.

È efficiente per search mode, ma:
> **selected passages are not equivalent to exhaustive inspection.**

**Stato:** REJECT equivalence in corpus mode.

---

### K. Evidence graph is useful as derived research memory
Il graph JSONL/BM25 permette:
- entity/relation memory;
- retrieval;
- within-run association.

Questo è utile come derived memory.

**Stato:** STRONGER / KEEP as derived layer.

---

### L. Evidence graph is too weak to be canonical scientific truth
Schema:

```text
Entity(name, entity_type, observations)
Relation(from_entity, to_entity, relation_type)
```

manca:
- mandatory provenance;
- exact locators;
- epistemic type;
- evidence strength;
- claim object;
- contradiction object.

Per LEGEND:
> **a convenient research graph should not become canonical evidence state unless these guarantees are structural.**

**Stato:** REJECT as canonical truth.

---

### M. Prompt-only provenance is insufficient
Il prompt chiede provenance, ma schema non la rende obbligatoria.

**Stato:** REJECT as guarantee.

---

### N. Default graph reset is good for isolated benchmarks, bad for continuous science
`go()` default clearisce la graph cache.

Questo è utile per clean-run evaluation, ma distruttivo per continuous knowledge accumulation.

Per LEGEND:
> **fresh benchmark mode and persistent scientific-memory mode should be separate explicit policies.**

**Stato:** STRONGER distinction.

---

### O. Graph reuse ≠ incremental scientific update
Impostare `clear_evidence_graph_cache=False` conserva memory, ma non produce:
- new-paper delta;
- impacted-claim analysis;
- structured reopen logic.

**Stato:** VERY STRONG distinction.

---

### P. Cross-study reasoning is strong, but provenance-bearing inference is weak
L'Orchestrator può creare collegamenti scientifici sofisticati tra fonti.

Ma l'inferenza non diventa un object con mandatory support edges.

Per LEGEND:
> **model-level cross-paper reasoning is valuable only if the resulting inference remains addressable to its evidence.**

**Stato:** VERY STRONG requirement.

---

### Q. SUPPORTS/REFUTES/INCONCLUSIVE relations are useful but not enough
Il prompt incoraggia relazioni di evidence polarity.

Questo è utile e converge con DisMech/ResearchOS.

Ma polarity alone non sostituisce:
- evidence packet;
- epistemic type;
- source locator.

**Stato:** STRONGER.

---

### R. Static KB→tool mapping is simple and robust
DeepEvidence usa una map esplicita tra knowledge-base types e tool wrappers.

Questo è meno flessibile di ATHENA Tool_RAG ma anche più deterministicamente ispezionabile.

Per LEGEND:
> **static registry + dynamic selection may be preferable to unconstrained semantic tool discovery for core biomedical capabilities.**

**Stato:** BENCHMARK / design option.

---

### S. Capability allowlist per task is useful
L'Orchestrator/subagent riceve selected knowledge bases.

Questo è un buon compromise tra:
- flexibility;
- reproducibility;
- capability sprawl.

**Stato:** STRONGER / ADOPT CANDIDATE.

---

### T. Code execution belongs to capability layer
Python/R sandbox è tool substrate, non Computational Scientist identity.

**Stato:** VERY STRONG.

---

### U. Token telemetry is first-class
DeepEvidence accumula provider-reported input/output token usage anche attraverso subgraphs.

Questo è essenziale per il nostro futuro ablation benchmark.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### V. Real token cost can be very high even for bounded deep research
Il tutorial riportato nel dossier mostra ~150k tokens per un singolo example run.

Lezione:
> **scientific depth must be benchmarked against token-normalized yield, not only qualitative output quality.**

**Stato:** VERY STRONG.

---

### W. Concise child returns reduce context, but can lose provenance
BFRS/DFRS restituiscono branch summaries compatti.

Questo è buono per parent context, ma:
> **fan-in should ideally be structured evidence/results + concise synthesis, not only prose compression.**

**Stato:** VERY STRONG requirement.

---

### X. No independent evidence verifier
Nessun actor riapre la source per validare claim→support.

**Stato:** ABSENT / selective layer still required.

---

### Y. No hostile reviewer
Nessun fresh critic cerca overclaim, alternatives, missing controls, contradictions.

**Stato:** ABSENT / selective layer still required.

---

### Z. Sandbox degradation must not silently change guarantees
Se sandbox manca/dies, code execution può fallback local Python.

Questo migliora resilience ma cambia isolation guarantee.

Per LEGEND:
> **capability degradation that changes safety/reproducibility must be explicit policy state.**

**Stato:** VERY STRONG / HARDEN.

---

### AA. Corrupted graph-line skip is a dangerous silent degradation
Invalid JSONL lines possono essere ignorate dal loader.

Per scientific state:
> **corrupt durable state must not silently disappear.**

**Stato:** REJECT.

---

### AB. Auto-created placeholder entity can mask data inconsistency
Relation targeting missing entity may create placeholder entity.

Questo è convenient, ma canonical science should prefer explicit unresolved/inconsistent state.

**Stato:** HARDEN / BENCHMARK.

---

## 121.2 Patterns strengthened

- Generalist ownership of scientific question.
- Ephemeral specialist modes.
- Bounded local delegation.
- Narrow child context.
- Tools/services rather than permanent specialists.
- Retrieval substrate as independent architectural layer.
- Token telemetry as a first-class benchmark variable.
- Cross-study reasoning should remain agentic.
- Deterministic corpus/task/provenance mechanics remain external to agent cognition.

## 121.3 Patterns weakened

- Single sequential Orchestrator as exhaustive scaling architecture.
- Mutable weakly-typed graph as canonical scientific truth.
- Prompt-only provenance.
- Search-filtered passages as full reading.
- Framework-level capability inferred as component-native.
- Graph persistence mistaken for delta-aware science.
- Silent fallback that changes runtime guarantees.
- Silent corruption skipping.

## 121.4 Scaling implications

### 50 papers
DeepEvidence-style breadth/depth modes could be useful **inside** a bounded corpus architecture, but only after each supplied paper becomes a deterministic accountable unit.

### 500 papers
Need:
- dynamic paper queue;
- equivalent General Scientist pool;
- dedup;
- structured evidence fan-in;
- reviewer routing.

### 5,000 papers
Need:
- sharded/hierarchical synthesis;
- incremental delta engine;
- persistent versioned evidence state;
- provider/rate-limit backpressure;
- reviewer capacity planning.

The current single Orchestrator should not remain the only scientific labor path.

## 121.5 Review implications

Recommended staged pattern remains:

```text
deterministic source/completeness checks
→ ordinary General Scientist
→ risk classifier
→ fresh Evidence Verifier if needed
→ Hostile Reviewer for major conclusions
```

BFRS/DFRS are discovery/depth modes, not reviewers.

## 121.6 Evidence/provenance implications

The evidence graph is useful only as a projection/derived memory.

Canonical science still needs:

```text
source identity/hash
+ exact evidence
+ locator
+ claim
+ epistemic type
+ polarity
+ review status
```

## 121.7 Context/token implications

DeepEvidence strongly supports:
- narrow delegated context;
- targeted retrieval;
- concise branch return;
- direct token telemetry.

But token efficiency must account for:
- overlapping searches;
- repeated history;
- repeated source discovery;
- lack of read-once source cache;
- lossy branch compression.

## 121.8 Changes to provisional design

```text
CORPUS TASK
   ↓
GENERAL SCIENTIST
   │
   ├─ direct reasoning
   ├─ BREADTH MODE
   └─ DEPTH MODE
          │
          ↓
capability allowlist
          ↓
biomedical tool substrate
          ↓
structured evidence/result packet
          ↓
parent reintegration
```

Important:
- breadth/depth are modes;
- not permanent actors;
- not corpus-scaling workers.

## 121.9 New unresolved questions

1. Does explicit breadth/depth mode improve Reader scientific recall over one unrestricted generalist?
2. Should breadth/depth selection be Scientist-decided or deterministic/risk-routed?
3. Static core capability registry vs ATHENA-style semantic capability discovery: which is more robust for biomedical production?
4. What minimum child return schema preserves provenance without overloading parent context?
5. Does a derived evidence graph add enough synthesis value beyond claim/entity indexes?
6. Should benchmark runs default to clean memory while production runs default to persistent versioned memory?
7. At what task size does one sequential Orchestrator become slower than a pool after fan-in overhead?
8. What token-normalized scientific yield does breadth/depth delegation add versus direct frontier-model tool use?
9. How should capability fallback be surfaced when isolation/reproducibility guarantees change?
10. Should graph corruption/placeholders fail closed or enter explicit repair states?

# 122. Cumulative Pattern Ledger — delta after BioDSA/DeepEvidence

| Pattern | Stato cumulativo |
|---|---|
| Breadth/depth Scientist modes | **VERY STRONG / ADOPT CANDIDATE** |
| Focused delegation contract | **VERY STRONG** |
| Bounded delegation | **VERY STRONG** |
| Ephemeral specialist modes | **VERY STRONG** |
| Retrieval substrate as separate value layer | **VERY STRONG** |
| Tool-level parallelism ≠ Scientist parallelism | **VERY STRONG distinction** |
| Sequential Orchestrator bottleneck | **VERY STRONG scaling concern** |
| Search-driven research ≠ corpus execution | **VERY STRONG distinction** |
| Framework capability ≠ native component capability | **VERY STRONG benchmark rule** |
| Filtered passage retrieval ≠ full reading | **REJECT equivalence** |
| Evidence graph as derived memory | **KEEP / STRONGER** |
| Evidence graph as canonical truth | **REJECT** |
| Prompt-only provenance | **REJECT** |
| Clean benchmark memory vs persistent production memory | **STRONGER distinction** |
| Graph reuse ≠ delta-aware science | **VERY STRONG distinction** |
| Cross-study reasoning | **VERY STRONG agentic capability** |
| Provenance-bearing inference | **VERY STRONG requirement** |
| Evidence polarity relations | **STRONGER** |
| Static registry + dynamic selection | **BENCHMARK** |
| Capability allowlist per task | **STRONGER / ADOPT CANDIDATE** |
| Code execution as tool | **VERY STRONG** |
| Token telemetry | **VERY STRONG / ADOPT CANDIDATE** |
| Token-normalized scientific yield | **VERY STRONG benchmark requirement** |
| Concise child return | **KEEP with structured provenance** |
| Independent Evidence Verifier | **ABSENT / SELECTIVE REQUIRED** |
| Hostile Reviewer | **ABSENT / SELECTIVE REQUIRED** |
| Isolation-changing fallback | **HARDEN / explicit state** |
| Silent corrupt-state skipping | **REJECT** |
| Placeholder entity auto-healing | **HARDEN / BENCHMARK** |

# 123. Current top Scientist takeaways after sixteen Tier-1 reviews

1. Keep one broad interchangeable General Scientist contract.
2. Represent breadth and depth as task modes, not permanent identities.
3. Delegate narrowly with explicit search target, capability allowlist and budget.
4. Keep delegation shallow and bounded.
5. Separate biomedical retrieval substrate from agent orchestration quality.
6. Never confuse parallel retrieval with parallel scientific labor.
7. Do not rely on one sequential Orchestrator for exhaustive large-corpus throughput.
8. Keep search-driven deep research distinct from bounded corpus processing.
9. Credit only capabilities actually wired into the native execution path.
10. Never equate filtered passages with complete paper inspection.
11. Use evidence graphs as derived research memory, not canonical truth unless provenance/epistemics are structural.
12. Reject prompt-only provenance as a scientific guarantee.
13. Separate clean-run benchmark memory policy from persistent production memory policy.
14. Do not confuse retained graph state with incremental science.
15. Preserve cross-study reasoning but make its evidence dependencies addressable.
16. Keep evidence polarity separate from exact provenance and epistemic type.
17. Benchmark static capability registries against dynamic semantic discovery.
18. Use task-level capability allowlists when they improve reproducibility.
19. Keep code execution as capability, not Scientist identity.
20. Make token telemetry mandatory for architecture comparisons.
21. Optimize for scientific yield per token, not raw autonomy.
22. Return structured branch evidence/results plus concise synthesis.
23. Add independent Evidence Verifier selectively.
24. Add Hostile Reviewer selectively for high-impact claims.
25. Final LEGEND Reader remains generalist-first, deterministic underneath, horizontally scalable only where workload justifies it.


# 124. Review 17 — Autoresearch

Repository analizzata: `hugoferreira/autoresearch`

## 124.1 Nuovi spunti utili per gli Scientist LEGEND

### A. Evidence-producing kernel instead of narrative evidence

Autoresearch impone una distinzione estremamente forte:

```text
Hypothesis
→ Experiment
→ machine-produced Observation
→ deterministic analysis
→ Conclusion
```

L'`Observation` non è prose inventata dall'agent: è prodotta da un instrument.

Per LEGEND Reader il trasferimento più importante è:

> **EvidencePacket should be to literature what Observation is to computational experiments: a constrained, source-bound evidence object that cannot be hand-waved into existence by prose.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### B. Content-addressed raw artifacts

Autoresearch conserva evidence artifacts con SHA/path/bytes/MIME.

Per LEGEND:
- source PDF/full text;
- rendered figure/panel;
- extracted table;
- computational outputs;

dovrebbero essere content-addressed quando load-bearing.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### C. Candidate/baseline provenance is exact

La repo lega observation a:
- candidate ref/SHA;
- baseline SHA;
- worktree;
- instrument.

Questo è un modello forte di provenance.

Per letteratura l'analogo è:
```text
claim
→ exact source artifact/hash
→ exact locator/surface
→ exact extracted evidence
```

**Stato:** VERY STRONG.

---

### D. Strict supported→inconclusive firewall

Se evidence quantitativa non raggiunge i criteri, il sistema forza `inconclusive`.

Questo è uno dei pattern epistemici più forti del corpus.

Per LEGEND:
> **when minimum proof conditions are not met, the system should downgrade to UNVERIFIED / INCONCLUSIVE rather than let prose upgrade the claim.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### E. First-class INCONCLUSIVE

Autoresearch non forza binary support/refute.

Per letteratura questo suggerisce:
```text
SUPPORTED
REFUTED
INCONCLUSIVE
UNVERIFIED
```

come stati distinti.

**Stato:** VERY STRONG.

---

### F. Fresh independent gate reviewer

Il reviewer:
- parte fresh;
- non riceve producer reasoning;
- riapre raw evidence;
- può downgrade/reject.

Questo è probabilmente uno dei migliori reviewer patterns del corpus.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### G. Reviewer cannot upgrade without new evidence

Asimmetria importante:
> **review may reject/downgrade, but must not create a stronger scientific claim from the same evidence.**

Questo riduce false-positive escalation.

**Stato:** VERY STRONG.

---

### H. Anti-Goodharting scientific review

Il reviewer cerca:
- gaming;
- mechanism mismatch;
- side effects;
- scope creep;
- baseline drift;
- environment divergence.

Per LEGEND biomedicale l'analogo è:
- surrogate evidence mistaken for mechanism;
- model-system artifacts;
- assay confounds;
- causal overreach;
- translational overclaim.

**Stato:** VERY STRONG / ADAPT.

---

### I. Frozen task-specific child context

`.autoresearch-brief.json` contiene solo:
- Goal;
- Hypothesis;
- Experiment;
- relevant Lessons;
- instrument contracts;
- forbidden changes.

Questo è un eccellente handoff primitive.

Per LEGEND:
> **child Scientist / specialist should receive a frozen authoritative task packet, not mutable global conversation history.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### J. Fresh non-recursive one-cycle producer

L'orchestrator esegue esattamente un cycle e yielda.

Questo limita:
- context drift;
- runaway autonomy;
- recursion;
- hidden accumulated state.

Per LEGEND:
> **fresh bounded Scientist instances are a strong default for atomic scientific work.**

**Stato:** VERY STRONG.

---

### K. Coder isolated from scientific authority

Il coder modifica candidate code in worktree ma non controlla research-store truth.

Pattern:
> **execution helper should not own scientific acceptance.**

Per LEGEND computation:
- tool/coder can produce candidate computation;
- Scientist interprets;
- reviewer/gates admit.

**Stato:** VERY STRONG.

---

### L. Authoritative read packets instead of transcript replay

`cycle-context` e `review-packet` ricostruiscono solo ciò che serve.

Questo converge fortemente con task-scoped context architecture.

**Stato:** VERY STRONG.

---

### M. Derived Frontier is not a second truth store

Frontier è un read model derivato da authoritative state.

Per LEGEND:
> **mechanism dashboards/summaries should be projections over canonical evidence/claims, not mutable competing truth stores.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### N. Lessons linked to reviewed evidence

Lessons derivano da conclusions e possono essere invalidated/superseded.

Questo è un buon pattern per scientific memory.

**Stato:** VERY STRONG.

---

### O. Observation idempotence

Repeated measurement può top-up senza duplicare semanticamente lo stesso observation unless explicitly append.

Per LEGEND:
> **reprocessing the same immutable source/task should be content-idempotent unless a deliberate new version/review is requested.**

**Stato:** STRONGER / ADOPT CANDIDATE.

---

### P. Deterministic statistics should stay software

Sample sufficiency, CI, effect calculation e ranking aggregation non richiedono Statistical Scientist.

**Stato:** VERY STRONG / REJECT permanent Statistical Scientist.

---

### Q. Experimental feedback loop is genuine

Native:
```text
Hypothesis
→ Experiment
→ Observation
→ Evaluation
→ Conclusion
→ Lesson
→ next Hypothesis
```

Questo è altamente trasferibile downstream dei Reader.

**Stato:** VERY STRONG.

---

### R. Evidence admission must be constrained before reuse

Il pattern centrale:
> **a result should not enter reusable scientific memory merely because an agent wrote a convincing interpretation.**

Per LEGEND:
```text
candidate finding
→ deterministic source/provenance checks
→ selective semantic review
→ admitted claim
```

**Stato:** VERY STRONG / ADOPT CANDIDATE.

---

### S. Strong computational epistemics do not imply literature capability

Autoresearch non ha:
- PDF;
- PubMed;
- corpus;
- figure pipeline;
- biomedical schema.

Questo è una categoria diversa.

**Stato:** VERY STRONG benchmark discipline.

---

### T. Single-writer state is explicitly not a pool foundation

`state.go` dichiara il single-writer assumption.

Per LEGEND:
> **do not copy local single-writer storage as the basis of ScientistPool(N).**

**Stato:** REJECT as scaling foundation.

---

### U. Worktree isolation ≠ multi-writer scientific state safety

Multiple candidate worktrees non equivalgono a safe concurrent research-state mutation.

**Stato:** VERY STRONG distinction.

---

### V. No task claiming

Manca:
- READY queue;
- atomic claim;
- lease;
- reassignment.

Quindi horizontal Scientist scaling non è implementato.

**Stato:** CRITICAL BUILD remains.

---

### W. Durable local state ≠ portable scientific state

`.research/` è durable locally ma gitignored by default.

Per LEGEND:
> **scientific state must have explicit export/version/transport semantics.**

**Stato:** VERY STRONG requirement.

---

### X. JSONL events ≠ cryptographic provenance

Append-oriented `events.jsonl` è utile ma:
- no hash chain;
- malformed lines can be skipped.

Per authoritative scientific audit:
> **event convenience must not be overstated as tamper-proof provenance.**

**Stato:** STRONGER distinction.

---

### Y. Malformed event skip is acceptable operationally but not as evidence integrity

Se events diventano load-bearing scientific provenance, silent skip è insufficiente.

**Stato:** HARDEN / BENCHMARK.

---

### Z. Scalar-first scientific ontology is domain-specific

Autoresearch è eccellente quando goal è misurabile.

Non va generalizzato a tutta la biologia.

Per LEGEND:
> **use scalar/instrument kernel for executable hypotheses, not as universal literature ontology.**

**Stato:** VERY STRONG distinction.

---

## 124.2 Patterns strengthened

- Producer ≠ validator.
- Fresh-context review.
- Raw-artifact-first verification.
- Machine-produced evidence.
- Fail-closed epistemic states.
- Durable scientific objects over conversation memory.
- Frozen task packets.
- Ephemeral workers.
- Tools/software for deterministic truth.
- Review only where consequence is high.
- Derived views should not become competing truth stores.

## 124.3 Patterns weakened

- Agent-authored evidence as authoritative.
- Universal binary support/refute.
- Reviewer allowed to upgrade same evidence.
- Permanent Statistical Scientist.
- Single-writer files as ScientistPool substrate.
- Worktree count as proof of parallelism.
- JSONL event log as sufficient integrity layer.
- Scalar optimization model as universal scientific ontology.

## 124.4 Scaling implications

Autoresearch gives almost no native literature throughput pattern, but gives a strong guarantee architecture.

For corpus scaling:

```text
READY PAPER TASK
→ ephemeral Scientist
→ candidate EvidencePackets/Claims
→ deterministic source gate
→ selective fresh reviewer
→ canonical apply
```

The store must support:
- atomic claims;
- concurrent-safe candidate ingestion;
- serialized or transactional canonical apply.

## 124.5 Review implications

Autoresearch materially strengthens a specific reviewer contract:

```text
fresh reviewer
+ no producer reasoning
+ raw evidence
+ deterministic recomputation/checks
+ authority to downgrade/reject
- no authority to invent stronger conclusion
```

For LEGEND this should be benchmarked against simpler fresh-review prompts.

## 124.6 Evidence/provenance implications

Literature equivalent of native Observation:

```text
EVIDENCE_PACKET
  source_id
  source_hash
  locator
  exact content/surface
  extraction method
  parser/reader version
  evidence type
  producer
  deterministic validation state
```

Only after this should semantic interpretation become a reusable Claim.

## 124.7 Context/token implications

Strong patterns:
- fresh atomic worker;
- authoritative compact context;
- frozen child packet;
- reviewer receives only necessary evidence;
- no full transcript replay.

These are directly relevant to keeping Scientist scientifically fresh.

## 124.8 Changes to provisional design

```text
SOURCE / COMPUTATION
        ↓
DETERMINISTIC EVIDENCE-PRODUCING PATH
        ↓
CANDIDATE EVIDENCE OBJECT
        ↓
SCIENTIST INTERPRETATION
        ↓
CANDIDATE CLAIM
        ↓
STRICT ADMISSION GATE
        │
        ├─ insufficient → INCONCLUSIVE / UNVERIFIED
        └─ sufficient → selective fresh review if high-impact
                               ↓
                         CANONICAL CLAIM
```

## 124.9 New unresolved questions

1. Can an Autoresearch-style `Observation` invariant be adapted to literature without over-structuring the Reader?
2. Which literature claims deserve fail-closed admission versus soft unresolved states?
3. Should reviewer be downgrade-only in all scientific domains?
4. Does frozen task context improve Reader independence/freshness enough to justify serialization overhead?
5. Can `Frontier`-style derived views replace some current LEGEND narrative summaries?
6. What minimum hash/content-addressing policy gives meaningful provenance without bloating storage?
7. How should candidate scientific writes be concurrency-safe while canonical apply remains serialized?
8. Are Lessons useful for Reader improvement, or should Metacognition own them separately?
9. Which event transitions require cryptographic chaining, if any?
10. Can computational `inconclusive` semantics be mapped cleanly to literature evidence strength?

# 125. Cumulative Pattern Ledger — delta after Autoresearch

| Pattern | Stato cumulativo |
|---|---|
| Machine-produced/constrained evidence path | **VERY STRONG / ADOPT CANDIDATE** |
| EvidencePacket as literature Observation analogue | **VERY STRONG direction** |
| Content-addressed raw artifacts | **VERY STRONG / ADOPT CANDIDATE** |
| Exact candidate/source provenance | **VERY STRONG** |
| Fail-to-INCONCLUSIVE | **VERY STRONG / ADOPT CANDIDATE** |
| First-class INCONCLUSIVE/UNVERIFIED | **VERY STRONG** |
| Fresh independent gate reviewer | **VERY STRONG / ADOPT CANDIDATE** |
| Reviewer downgrade-only without new evidence | **VERY STRONG** |
| Anti-Goodharting hostile review | **VERY STRONG / ADAPT** |
| Frozen task-specific brief | **VERY STRONG / ADOPT CANDIDATE** |
| Fresh one-cycle producer | **VERY STRONG** |
| Execution helper separated from scientific authority | **VERY STRONG** |
| Authoritative read packets | **VERY STRONG** |
| Derived Frontier/read model ≠ truth store | **VERY STRONG / ADOPT CANDIDATE** |
| Provenance-linked Lessons | **VERY STRONG** |
| Observation/result idempotence | **STRONGER / ADOPT CANDIDATE** |
| Statistics as software | **VERY STRONG** |
| Permanent Statistical Scientist | **REJECT** |
| Experimental feedback loop | **VERY STRONG** |
| Evidence admission before reusable knowledge | **VERY STRONG / ADOPT CANDIDATE** |
| Worktree isolation ≠ multi-writer safety | **VERY STRONG distinction** |
| Single-writer local files as pool substrate | **REJECT** |
| Atomic task claiming | **CRITICAL BUILD** |
| Local durability ≠ portability | **VERY STRONG requirement** |
| JSONL events ≠ cryptographic provenance | **STRONGER distinction** |
| Silent malformed-event skip | **HARDEN if authoritative** |
| Scalar-first ontology | **KEEP computationally / REJECT universally** |

# 126. Current top Scientist takeaways after seventeen Tier-1 reviews

1. Keep evidence creation separate from interpretation.
2. Require load-bearing evidence to enter through a constrained evidence-producing path.
3. Treat literature EvidencePacket as the analogue of an instrument-produced Observation.
4. Content-address important raw source/evidence artifacts.
5. Preserve exact provenance between evidence and the object that produced it.
6. Make INCONCLUSIVE/UNVERIFIED first-class outcomes.
7. Never let prose talk weak evidence into strong support.
8. Use fresh independent reviewers for consequential claims.
9. Prefer reviewers that can downgrade/reject but not upgrade without new evidence.
10. Give reviewers raw evidence and exclude producer reasoning when independence matters.
11. Use anti-Goodharting/adversarial review for high-impact scientific claims.
12. Give child workers frozen task-specific context packets.
13. Keep scientific workers fresh, bounded and non-recursive by default.
14. Separate execution helpers from scientific acceptance authority.
15. Build compact authoritative read packets instead of replaying conversation history.
16. Keep summaries/frontiers as derived views, not competing canonical truth.
17. Link reusable lessons back to reviewed evidence.
18. Make repeated processing idempotent where the scientific object has not changed.
19. Keep statistics and machine-checkable proof rules in software.
20. Preserve computational hypothesis→experiment→observation→conclusion loops downstream of literature.
21. Never confuse worktree isolation with concurrency-safe scientific state.
22. Build atomic claims/leases before horizontal Scientist scaling.
23. Make durable scientific state explicitly portable.
24. Do not overstate JSONL logs as integrity guarantees.
25. Final LEGEND Reader should copy Autoresearch's epistemic boundaries, not its domain ontology or single-writer scaling model.


# 127. Review 18 — ToolUniverse

Repository analizzata: `mims-harvard/ToolUniverse`
Benchmark snapshot: `main @ 7fe234c093856b5603d337147bfdecebdba82205`

## 127.1 New Scientist patterns

### A. Capability plane as first-class architecture
ToolUniverse's strongest reusable primitive is not an agent topology but a capability substrate:

```text
discover
→ select
→ lazy-load
→ validate
→ execute
→ return
```

For LEGEND:
> **keep the Scientist contract thin and let capabilities scale independently underneath it.**

**Stato:** VERY STRONG / ADOPT CANDIDATE.

### B. Progressive capability disclosure
The model need not receive every tool schema up front. It can discover a relevant capability, inspect only the necessary contract, then execute it.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

### C. Lazy capability loading
Capabilities can remain unloaded/unexpanded until actually needed.

**Stato:** VERY STRONG.

### D. Capability identity ≠ Scientist identity
Tools, external APIs, AgenticTools and runtime profiles can vary without creating new permanent scientific roles.

**Stato:** VERY STRONG.

### E. ROLE ≠ TOOL ≠ SKILL ≠ MODEL ≠ PROVIDER ≠ TRANSPORT
ToolUniverse reinforces a clean separation among scientific role, executable capability, scientific procedure, model, provider and local/remote transport.

**Stato:** VERY STRONG / architecture invariant candidate.

### F. AgenticTool as bounded ephemeral reasoning capability
`AgenticTool` demonstrates a lightweight specialist pattern:

```text
parent Scientist
→ narrow task
→ LLM-backed capability
→ result
→ parent reintegration
```

**Stato:** STRONGER / ADOPT CANDIDATE.

### G. Capability delegation, not agent-society delegation
Delegate capabilities first; spawn another Scientist only when independent scientific judgment is required.

**Stato:** VERY STRONG.

### H. Tool-level parallelism ≠ Scientist-level parallelism
Concurrent tool execution is real; an elastic scientific-worker pool is not native.

**Stato:** VERY STRONG distinction.

### I. ScientistPool is a natural extension, not a native feature
ToolUniverse fits cleanly underneath `GeneralScientist × N`, but queue/claim/recovery/fan-in must be supplied deterministically elsewhere.

**Stato:** VERY STRONG direction.

### J. Worker identity should not become scientific ontology
Durable identity belongs to task/evidence/output/execution/model-runtime provenance, not permanent `Scientist_A/B/C`.

**Stato:** VERY STRONG.

### K. Scientific task claiming remains deterministic infrastructure
`TaskManager` handles runtime tool jobs, not scientific paper ownership.

**Stato:** CRITICAL BUILD.

### L. Capability-context efficiency ≠ evidence-context efficiency
ToolUniverse solves which capability to expose; it does not solve which scientific evidence from thousands of papers belongs in the current reasoning context.

**Stato:** VERY STRONG distinction.

### M. Explicit scientific memory must replace repeated evidence ingestion
Result caches do not replace canonical evidence packets and claims.

**Stato:** VERY STRONG.

### N. Review duplication can be scientifically justified
A fresh verifier reopening source evidence is justified duplication when independence is the guarantee.

**Stato:** STRONGER.

### O. Runtime failure visibility ≠ scientific omission visibility
Tool failures can be explicit while skipped papers, missing supplements or uninspected figures remain invisible.

**Stato:** VERY STRONG distinction.

### P. Source-rich retrieval ≠ source-faithful claim provenance
ToolUniverse does not universally bind claim → exact evidence → precise locator → source fingerprint.

**Stato:** VERY STRONG requirement.

### Q. Execution provenance ≠ scientific evidence provenance
Operational metadata about model/provider/tool invocation does not identify the exact experiment or passage supporting a biological claim.

**Stato:** VERY STRONG distinction.

### R. Tool schema validation ≠ scientific-state validation
The runtime validates calls; it does not enforce epistemic correctness of scientific knowledge.

**Stato:** VERY STRONG distinction.

### S. Optional validation bypass must not cross governed boundaries
`validate=False` may be acceptable for low-level development but not for canonical scientific mutation.

**Stato:** HARDEN / DO NOT COPY as default.

### T. Ranking ≠ evidence verification ≠ hostile review
These are three distinct scientific functions and must remain separate.

**Stato:** VERY STRONG.

### U. Independent review should be selective and ephemeral
Evidence Verifier, Hostile Reviewer and high-level Mechanism/Synthesis reviewer are strongest as fresh task-scoped instances.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

### V. Statistical Analyst should usually be software, not actor
Numerical computation belongs in deterministic software; biological meaning belongs to the Scientist.

**Stato:** VERY STRONG / REJECT permanent Statistical Scientist.

### W. PDF/Citation/Ontology/Scheduler specialists should mostly be tools/software
Do not anthropomorphize deterministic capabilities.

**Stato:** VERY STRONG.

### X. Scientific inference needs typed durable state
Model reasoning should be materialized as observation / author interpretation / agent inference / hypothesis / contradiction / uncertainty objects when load-bearing.

**Stato:** VERY STRONG requirement.

### Y. Epistemic expressivity ≠ epistemic kernel
A model can express distinctions in prose without the system enforcing them.

**Stato:** VERY STRONG distinction.

### Z. Tool fan-out / model fan-in is useful but insufficient at corpus scale
At large scale, provenance-preserving hierarchical fan-in is required.

**Stato:** VERY STRONG.

### AA. Amdahl-like scientific limit
Evidence acquisition can parallelize aggressively, but integrative reasoning, contradiction adjudication, shared state and review become the serial bottleneck.

**Stato:** VERY STRONG scaling principle.

### AB. Scientific state + synthesis saturate before capability execution
For exhaustive large-corpus research, adding more agents is not the primary fix.

**Stato:** VERY STRONG.

### AC. External API/model quotas are architectural constraints
Requests/minute, tokens/minute, cost, service quotas and reliability must feed scheduling.

**Stato:** STRONGER / benchmark requirement.

### AD. Dynamic claiming should beat static partitioning for heterogeneous papers
`READY papers → next free Scientist` is the preferred counterfactual pattern.

**Stato:** STRONGER / BUILD candidate.

### AE. Result cache ≠ scientific memory
Reuse cache for deterministic/retrieval performance, never as canonical truth.

**Stato:** VERY STRONG / REJECT equivalence.

### AF. TaskManager ≠ campaign state
In-memory runtime task tracking is not durable scientific orchestration.

**Stato:** REJECT as durable scheduler.

### AG. Repository reproducibility ≠ research-state reproducibility
A clean clone restores software, not scientific progress.

**Stato:** VERY STRONG distinction.

### AH. Incremental retrieval ≠ incremental scientific updating
Finding new papers is easy; determining impacted old claims/mechanisms requires dependency-aware state.

**Stato:** VERY STRONG distinction.

### AI. Scientific dependency graph is the missing primitive for continuous update
At scale:

```text
source
→ evidence
→ claim
→ mechanism
→ hypothesis
```

should support targeted impact analysis.

**Stato:** VERY STRONG / ADOPT CANDIDATE.

### AJ. Preserve ToolUniverse thinness under scale
Add deterministic corpus/work/provenance state around the capability plane, not more permanent roles or handoffs.

**Stato:** VERY STRONG.

## 127.2 Patterns strengthened

- Thin General Scientist contract.
- Skills/tools before permanent actors.
- Dynamic capability discovery.
- Lazy loading.
- Progressive disclosure.
- Runtime/provider neutrality.
- Narrow delegated context.
- Fresh verifier/reviewer only where independence matters.
- Deterministic task ownership/completeness/persistence.
- Scientific state outside model conversation.
- Horizontal throughput via interchangeable workers, not permanent worker identities.
- Hierarchical synthesis at large corpus scale.
- Risk-based review.
- EvidencePacket + claim store + dependency graph.

## 127.3 Patterns weakened

- Tool-level concurrency presented as Scientist scaling.
- TaskManager reused as durable scientific scheduler.
- Cache treated as scientific memory.
- Search-driven research treated as exhaustive corpus curation.
- Prompt-only epistemic typing.
- Permanent PDF/Citation/Ontology/Statistical agents.
- Large permanent specialist hierarchy.
- Optional validation bypass on canonical boundaries.
- One giant host context as large-corpus synthesis architecture.

## 127.4 Scaling implications

### ~50 papers
```text
1–3 General Scientists
+ ToolUniverse-style capability plane
+ deterministic completeness
+ EvidencePackets
+ selective review
```

### ~500 papers
Need persistent queue, atomic claiming, equivalent Generalist pool, normalized claims, dedup, contradiction index and structured fan-in.

### ~5,000 papers
Need hierarchical reducers, dependency-aware incremental updates, persistent/versioned evidence state, review routing, provider/API backpressure, semantic work dedup and sharded scientific state.

## 127.5 Review implications

Keep distinct:

```text
RANKING
Is A better than B?

EVIDENCE VERIFICATION
Does source S support claim C?

HOSTILE REVIEW
Is claim/mechanism scientifically defensible?
```

Recommended policy:

```text
deterministic source/locator checks
→ ordinary General Scientist
→ risk classifier
→ fresh Evidence Verifier if needed
→ fresh Hostile Reviewer for major conclusions
```

## 127.6 Evidence/provenance implications

Target minimal evidence chain:

```text
source_id / hash
→ exact evidence
→ precise locator
→ normalized observation
→ typed claim
→ review state
→ mechanism/hypothesis links
```

Operational execution metadata remains separate from scientific evidence provenance.

## 127.7 Context/token implications

ToolUniverse contributes one of the strongest context patterns in the census:

```text
large capability universe
→ discover small relevant subset
→ load detailed schema only then
```

LEGEND must separately solve:

```text
large scientific state
→ retrieve only relevant evidence/claims
```

## 127.8 Changes to provisional design

```text
DETERMINISTIC CORPUS / TASK STATE
        ↓
GENERAL SCIENTIST × N
        │
        ├── thin stable role contract
        ├── dynamic capability discovery
        ├── lazy tool loading
        ├── bounded AgenticTool specialists
        └── exact evidence access
        ↓
TOOLUNIVERSE-LIKE CAPABILITY PLANE
        ↓
EVIDENCE PACKETS / CLAIMS
        ↓
PERSISTENT SCIENTIFIC STATE
        ↓
RISK-BASED INDEPENDENT REVIEW
        ↓
HIERARCHICAL SYNTHESIS
        ↓
VERSIONED MECHANISM STATE
```

## 127.9 New unresolved questions

1. Does ToolUniverse-style capability discovery materially improve Reader quality, or mainly context/cost?
2. What is the minimum capability discovery API LEGEND needs?
3. Static capability registry vs semantic tool finder: which is safer/more efficient?
4. How many tool schemas can a frontier model tolerate before progressive disclosure materially helps?
5. Can capability discovery itself introduce tool-selection misses that reduce scientific recall?
6. Should critical capabilities be statically guaranteed while optional capabilities remain dynamically discovered?
7. What is the minimum durable scientific queue needed before `GeneralistPool(N)` becomes worthwhile?
8. At which corpus size does hierarchical synthesis outperform one strong synthesis model?
9. How should API/provider quotas feed back into queue scheduling?
10. What semantic dedup layer is required before N=10/N=50 stops wasting tokens?
11. Can AgenticTool-like bounded specialists outperform same-model task-mode switching?
12. Which validation boundaries must be impossible to bypass?

# 128. Cumulative Pattern Ledger — delta after ToolUniverse

| Pattern | Stato cumulativo |
|---|---|
| Thin interchangeable General Scientist | **VERY STRONG / ADOPT CANDIDATE** |
| Dynamic capability plane | **VERY STRONG / ADOPT CANDIDATE** |
| Progressive capability disclosure | **VERY STRONG / ADOPT CANDIDATE** |
| Lazy capability loading | **VERY STRONG** |
| Capability identity ≠ worker identity | **VERY STRONG** |
| ROLE ≠ TOOL ≠ SKILL ≠ MODEL ≠ PROVIDER ≠ TRANSPORT | **VERY STRONG** |
| AgenticTool-style bounded specialist | **STRONGER / ADOPT CANDIDATE** |
| Capability delegation before Scientist delegation | **VERY STRONG** |
| Tool parallelism ≠ Scientist parallelism | **VERY STRONG distinction** |
| ScientistPool as external deterministic extension | **VERY STRONG direction** |
| Durable task/evidence/output identity | **VERY STRONG** |
| Scientific task claiming | **CRITICAL BUILD** |
| Capability-context efficiency | **VERY STRONG** |
| Evidence-context efficiency | **CRITICAL separate problem** |
| Result cache ≠ scientific memory | **VERY STRONG / REJECT equivalence** |
| Runtime failure visibility ≠ scientific omission visibility | **VERY STRONG distinction** |
| Source-rich retrieval ≠ source-faithful curation | **VERY STRONG distinction** |
| Execution provenance ≠ evidence provenance | **VERY STRONG distinction** |
| Tool schema validation ≠ scientific-state validation | **VERY STRONG distinction** |
| Optional validation bypass | **HARDEN / REJECT at governed boundary** |
| Ranking ≠ evidence verification ≠ hostile review | **VERY STRONG** |
| Fresh selective independent review | **VERY STRONG / ADOPT CANDIDATE** |
| Permanent Statistical Scientist | **REJECT** |
| PDF/Citation/Ontology/Scheduler agents | **REJECT as permanent actors** |
| Epistemic expressivity ≠ epistemic kernel | **VERY STRONG distinction** |
| Tool fan-out / model fan-in | **KEEP small scale / insufficient large scale** |
| Hierarchical synthesis | **VERY STRONG scale requirement** |
| Amdahl-like scientific limit | **VERY STRONG scaling principle** |
| Scientific state+synthesis as bottleneck | **VERY STRONG** |
| Provider/API quota backpressure | **STRONGER requirement** |
| Dynamic claiming for heterogeneous corpus | **STRONGER / BUILD candidate** |
| TaskManager as campaign truth | **REJECT** |
| Repository reproducibility ≠ research-state reproducibility | **VERY STRONG distinction** |
| Incremental retrieval ≠ incremental scientific update | **VERY STRONG distinction** |
| Source→evidence→claim→mechanism dependency graph | **VERY STRONG / ADOPT CANDIDATE** |
| Preserve architecture thinness under scale | **VERY STRONG** |

# 129. Current top Scientist takeaways after eighteen Tier-1 reviews

1. Keep one thin, broad, interchangeable General Scientist contract.
2. Scale capabilities independently from role semantics.
3. Discover relevant capabilities progressively.
4. Lazy-load detailed tool schemas only when needed.
5. Separate role, skill, tool, model, provider and transport.
6. Prefer capability delegation before Scientist delegation.
7. Use bounded ephemeral LLM specialists when a genuinely different reasoning context helps.
8. Never confuse tool-call parallelism with horizontal scientific labor.
9. Build the ScientistPool above the capability plane, not inside it.
10. Keep worker identity ephemeral; persist task/evidence/output/execution identity.
11. Put READY/CLAIMED/STALE/retry semantics in software.
12. Solve capability-context and evidence-context scaling as separate problems.
13. Use caches for computation/retrieval reuse, never as canonical scientific memory.
14. Track scientific omissions separately from runtime failures.
15. Distinguish operational execution provenance from scientific evidence provenance.
16. Keep tool schemas validated, but separately validate scientific state.
17. Make canonical scientific validation boundaries non-bypassable.
18. Keep ranking, evidence verification and hostile review separate.
19. Use fresh Evidence Verifier/Hostile Reviewer selectively where independence matters.
20. Keep statistics, parsing, citation resolution, ontology lookup and scheduling as tools/software.
21. Give models the jobs that actually require scientific judgment.
22. Convert model inference into typed durable scientific objects.
23. Use tool fan-out/model fan-in only while corpus scale remains small.
24. Introduce hierarchical provenance-preserving synthesis before final context becomes the bottleneck.
25. Preserve ToolUniverse's thin capability architecture while adding deterministic corpus/work/provenance infrastructure around it.

