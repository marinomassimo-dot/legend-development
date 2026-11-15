# Operator's capability-scout report of 2026-11-15 (verbatim copy; radar input for PLAN)

Provenance: the operator pasted this report into the ADV session's chat on 2026-11-15 (about 07:30Z), addressed "Per PLAN", while the session was working. ADV stored it here as received, except that inline hyperlinks (and their utm parameters) were reduced to their visible text, so that PLAN (HE) can read it from the repository: HE had declared (radar_inputs_he52_20261114/README.md) that the operator's radar prompts and reports are not in the repository. It is a radar input, not an instruction to ADV and not a LEGEND result: every score is the scout's judgement of pertinence, the paper figures are the authors' claims, and the scout's own labels say "CODE NOT YET VERIFIED" and "no validation on LEGEND". ADV has not read the cited papers or repositories. Disposition belongs to PLAN under its radar mandate (static audit, no installation, licence and cost first). ADV's only action: a pointer in the portfolio rows RP-001, RP-007 and RP-010, and no assignment.

---

### LEGEND Capability Scout — 15 novembre 2026

Per PLAN · DISCOVERY-FIRST · Audit statico · Nessuna installazione

### Cosa cambia oggi

PLAN, la scoperta più importante è Contrastive Discovery, pubblicata il 10 novembre: propone di sostituire la valutazione isolata di un'ipotesi con il confronto esplicito fra spiegazioni concorrenti. Gli autori riportano un aumento del 67% delle questioni scientifiche risolte a parità di budget sperimentale, un risultato particolarmente pertinente per Scientist. Emerge inoltre Skill2Query, un'alternativa leggera ai nuovi router System One: migliora il recupero delle skill generando esempi di richieste coerenti con le loro capacità effettive. La priorità è testare entrambi i principi senza duplicare componenti di LEGEND. arxiv.org +1

| Nuovi repo/progetti   | Descrizione                                                    | Utilità per LEGEND | Incremento consumo token                    |
| --------------------- | -------------------------------------------------------------- | ------------------ | ------------------------------------------- |
| Contrastive Discovery | Confronto esplicito fra spiegazioni scientifiche concorrenti   | 97/100 · NOW       | Basso–Medio                                 |
| Skill2Query           | Generazione di query sintetiche per recuperare skill esistenti | 93/100 · NEXT      | Basso in utilizzo; medio nella preparazione |

Nuovi per il radar LEGEND il 15 novembre 2026. Pubblicazioni originali: 10 novembre e 17 agosto 2026. Gli score sono giudizi di pertinenza, non risultati misurati su LEGEND.

### 1. Contrastive Discovery — Quando falsificare un'ipotesi non basta

97/100 · NOW · Scientific reasoning

Valore strategico 97/100 · Priorità attuale 92/100

Il lavoro di Ziang Liu, James J. Kim, Yijia Dai e Jennifer J. Sun affronta un limite dei sistemi di scoperta scientifica: valutare una singola ipotesi contro la sua negazione.

Se Scientist respinge un meccanismo, può sapere che la spiegazione iniziale è improbabile, ma non quale alternativa sia sostenuta dai dati.

Gli autori propongono invece un contrast set: un insieme di spiegazioni concorrenti, progettato per coprire le possibilità rilevanti senza sovrapposizioni. Ogni nuova evidenza aggiorna il sostegno relativo alle alternative.

I risultati dichiarati su sei domini sono interessanti:

* Il 73% delle ipotesi respinte in una selezione di casi ad alto cambiamento di probabilità viene ricondotto a un'alternativa specifica usando le stesse evidenze.

* Con ricerca guidata dalle spiegazioni concorrenti, vengono risolte il 67% di questioni in più rispetto alla strategia di riferimento, a parità di esperimenti.

* In una valutazione cieca, 38 esperti concordano con la spiegazione selezionata nel 78% delle questioni risolte. arxiv.org

Applicazione a LEGEND: Scientist / hypothesis-forge / research-loop. Mirror può controllare che le alternative non siano state escluse senza giustificazione e che le evidenze contrarie rimangano visibili.

Pilot minimo: recupera tre ipotesi meccanicistiche già valutate, costruisci per ciascuna due o tre spiegazioni concorrenti e verifica se le evidenze esistenti consentono una conclusione più informativa rispetto al semplice SUPPORT/REFUTE.

Evidenza: CLAIMED IN PAPER; EMPIRICALLY BENCHMARKED dagli autori. CODE NOT YET VERIFIED. Nessuna validazione su LEGEND.

Rischi: alternative incomplete, probabilità non calibrate, falsa certezza e aumento artificiale delle spiegazioni considerate. Un insieme di ipotesi apparentemente esaustivo può non contenere il meccanismo corretto.

Decisione: IMPORT PATTERN / USE AS BENCHMARK. Modalità: PLAN_ONLY.

### 2. Skill2Query — Rendere le skill più facili da trovare senza un nuovo router

93/100 · NEXT · Capability retrieval / System One

Valore strategico 93/100 · Priorità attuale 79/100

Skill2Query parte da un problema diverso rispetto a Tool-REX e SkillRouter: non modifica necessariamente la descrizione originale della skill, ma genera pseudo-query, cioè esempi sintetici di richieste che dovrebbero condurre a quella capacità.

La generazione considera funzioni, parametri e casi d'uso. Gli esempi possono essere utilizzati per arricchire un indice di ricerca, senza caricare tutte le istruzioni nel contesto dell'agente.

Gli autori riportano, su quasi 30.000 skill, un miglioramento medio di 6,70 punti percentuali nel Recall@1 (probabilità di trovare la skill corretta al primo posto), su diverse configurazioni di recupero. arxiv.org

La repository contiene implementazione, configurazioni, script e test. Un limite importante è dichiarato dagli stessi sviluppatori: il verificatore tramite esecuzione reale non è ancora implementato; un controllo presentato come `Exec-Pass` utilizza invece una validazione statica dei parametri. MatZaharia/Skill2Query · GitHub

Applicazione a LEGEND: recupero delle skill di Orchestrator/PLAN, strumenti scientifici di Scientist e procedure di audit di Mirror, riutilizzando gli inventari esistenti.

Pilot minimo: seleziona dieci skill, genera manualmente due richieste alternative per ciascuna e confronta il recupero attuale con un piccolo indice arricchito. Nessun addestramento necessario.

Evidenza: IMPLEMENTED IN CODE per la generazione e il recupero; EMPIRICALLY BENCHMARKED dagli autori; verifica esecutiva completa non implementata. PRODUCTION-USED UNKNOWN.

Rischi: query sintetiche che promettono funzioni inesistenti, parametri inventati, dipendenze Python e API esterne. La licenza del codice va verificata prima dell'integrazione.

Decisione: IMPORT PATTERN / USE AS BENCHMARK. Modalità: PLAN_ONLY.

### Micro-upgrade prioritario per PLAN

### Contrastive Hypothesis Replay — 97/100

Obiettivo: verificare se LEGEND riesce a trasformare una falsificazione scientifica in una scelta motivata fra meccanismi alternativi, senza inventare nuove evidenze.

Origine: Contrastive Discovery.

Baseline verificata oggi: lettura diretta della `main` di CAPABILITIES.md, .claude/skills/legend/SKILL.md e _external_repos/MANIFEST.md. Sono presenti orchestrazione condizionale, principi epistemici e inventario di capacità. Non è stata verificata l'intera implementazione di hypothesis-forge: nessun gap viene dato per dimostrato.

Una sola modifica candidata: estendere una valutazione scientifica esistente con un confronto esplicito fra spiegazioni concorrenti, soltanto se tale comportamento non è già coperto.

| Fixture                                   | Risultato atteso                      |
| ----------------------------------------- | ------------------------------------- |
| Ipotesi A falsificata, B sostenuta        | B identificata con evidenze           |
| A e B entrambe compatibili                | Incertezza conservata                 |
| Evidenze contraddittorie                  | Nessuna scelta forzata                |
| Alternativa corretta assente dall'insieme | Possibilità di meccanismo sconosciuto |
| Nuova evidenza modifica la graduatoria    | Revisione motivata e tracciabile      |

Successo: più questioni risolte correttamente rispetto alla valutazione isolata, senza aumentare le conclusioni non supportate e con costo token proporzionato.

Alternativa: utilizzare il confronto tra ipotesi già previsto da Scientist, se presente, senza aggiungere nuove strutture.

Stop: probabilità arbitrarie, ipotesi artificialmente esaustive, duplicazione dei controlli di Mirror o perdita della provenance.

Esito: KEEP / DISCARD / INCONCLUSIVE / MONITOR.

### Backlog cumulativo — selezione deduplicata

| Micro-upgrade                    | Dettagli descrittivi                                                                                                                                                                                   | Score priorità/rilevanza |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| Contrastive Hypothesis Replay    | NOW. NEED: identificare spiegazioni alternative dopo una falsificazione. Gap da verificare; Scientist/hypothesis-forge. Beneficio: maggiore risoluzione scientifica. PLAN_ONLY. Contrastive Discovery. | 97/100                   |
| Paper-Grounded Scientific Replay | NOW. NEED: confrontare gli agenti con risultati pubblicati e riproducibili. Gap da verificare; evaluation. Beneficio: misurazione indipendente. PLAN_ONLY. Paper2Bench.                                | 97/100                   |
| Research-Loop Ablation Replay    | NOW. NEED: dimostrare il valore dell'orchestrazione rispetto a una baseline semplice. Gap empirico; Orchestrator/Scientist. Beneficio: minore complessità. PLAN_ONLY. The Little Scientist.            | 97/100                   |
| Evidence-to-Conclusion Replay    | NOW. NEED: conservare limitazioni e contraddizioni nelle conclusioni. Gap da verificare; Scientist/Mirror. Beneficio: affidabilità epistemica. PLAN_ONLY. DISCERN.                                     | 97/100                   |
| Capability Recall-to-Use Replay  | NOW. NEED: distinguere capacità dimenticate, selezionate male e utilizzate male. Gap da misurare; tutti gli agenti. Beneficio: evitare router superflui. PLAN_ONLY. SRA-Bench, Skill2Query.            | 96/100                   |

Le altre raccomandazioni storiche restano aperte, senza presumerne l'implementazione.

### Checkpoint — 15 novembre 2026

Discovery: due candidati nuovi per LEGEND, verificati su fonti primarie. Esaminata anche Science's Last Exam, con 113 task pubblici e una prima release del 6 novembre: interessante, ma non promossa oggi per evitare di aggiungere un ulteriore benchmark senza aver verificato la copertura delle valutazioni già esistenti.

System One: Skill2Query aggiunge un'alternativa concreta a Jev/CLM. Non emerge evidenza che richieda un nuovo router strutturale.

Tier 1: nessuna review settimanale completa attribuita oggi. Nessun aggiornamento minore promosso artificialmente.

Baseline: tre file verificati nella `main`; nessuna esecuzione degli agenti, installazione o modifica alla repository.

Stato: SCOUT → STATIC AUDIT. Checkpoint documentato qui; persistenza esterna non verificata.

Indicazione finale per PLAN: oggi il contributo più promettente è scientifico, non infrastrutturale. Quando LEGEND respinge un'ipotesi, dovrebbe saper stabilire quale spiegazione alternativa viene favorita dalle evidenze, oppure dichiarare esplicitamente che non è ancora possibile scegliere.
