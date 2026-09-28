---
record_type: HARNESS_SCOUT
week: 2026-W40
author: plan
handoff_to: plan
status: PROPOSED
---

# Harness scout — 2026-W40

Sessione "Scouting" dell'operatore, 2026-09-28. Input: un radar settimanale esterno incollato
dall'operatore (tornata 1). Ogni repo è stato aperto e il suo README letto il 2026-09-28; i
punteggi "NN/100" del radar sono suoi e non sono stati riprodotti. Tutto ciò che il radar
riporta e che non è stato verificato è marcato *non verificato*.

Il perimetro di questo file è la macchina, non la scienza: i punti biomedici del radar sono in
fondo, instradati e non valutati.

| # | candidate | source (URL) | what it adds to LEGEND | integration cost (h) | license | risk | proposed verdict | HE verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | AgentIdeaBench (HKUST-KnowComp) | https://github.com/HKUST-KnowComp/AgentIdeaBench | Il protocollo Static-vs-Active a parità di tutto il resto (5 paper consegnati contro solo il sottocampo + max 10 SEARCH/FETCH), le tre guardie anti-copia (coherence, factual consistency, boilerplate) con il baseline `copy`, il critic a media troncata che scarta il voto più generoso. Serve come disegno del run di controllo che `legend-discovery-method` § 4 dichiara ancora dovuto, via `legend-research-loop`. Non si esegue così com'è | 6 (disegno importato, run nativo LEGEND); 0 per eseguire il repo, che non si esegue | MIT codice, CC BY 4.0 dati | Richiede OpenRouter a pagamento, fuori dal vincolo di spesa zero. Nessuna interfaccia per un dominio custom. Repo di 3 settimane, 6 stelle. Tutti e cinque i punteggi sono giudizi LLM | TRIAL | |
| 2 | Theorizer / Literature-Driven Theories at Scale (AllenAI, ACL 2026) | https://github.com/allenai/asta-theorizer | Il metodo di validazione "congela il corpus a T0, genera predizioni, rivela la letteratura T1, assegna i punti". È un backtest per `preregister_prediction`, l'unica primitiva in stato KEEP, costruibile sul corpus WWOX già letto con le date di pubblicazione del registro dei paper. Punteggio contro gli esiti pubblicati, non un voto da judge | 8 | Apache-2.0 | Per i domini usa Semantic Scholar e un LLM. Da qui si importa il metodo, non il codice. Rischio di leakage: il modello conosce già la letteratura T1 dal training, quindi T1 deve cadere dopo il cutoff del modello o essere controllato | TRIAL | |
| 3 | TruthInsightBench | https://github.com/TruthInsight-stack/TruthInsightBench | 40 task blind (obiettivo e dati dati, conclusione nascosta) con un valutatore a 29 voci ancorato agli artefatti. Tra gli agenti valutati c'è Claude Code 2.1.220, cioè il runtime stesso di LEGEND. Riferimento per "la scoperta non è ricostruzione" | 10+ (Docker, endpoint del judge, un task biomedico da scegliere) | Apache-2.0 codice; i dati scientifici mantengono i termini a monte, non commerciali | Il judge è GLM-5.1 su un endpoint compatibile OpenAI, quindi spesa o hosting. I domini non sono elencati nel README e un task biomedico non è verificato. Il plateau 58–60 citato dal radar non è verificato. Repo di 4 settimane | WATCH | |
| 4 | ResearchBench (ACL 2026) | https://github.com/ankitala/ResearchBench | Scomposizione in tre parti: recupero delle ispirazioni (hit ratio esatto, senza judge), composizione (judge), ranking (a coppie). Il split di retrieval potrebbe misurare `connect_domains` senza un judge LLM | 5 per un sottoinsieme solo-retrieval su 20 task biologici | MIT codice, CC BY-NC 4.0 dati (su HF, non nel repo) | Endpoint compatibile OpenAI. Nel repo c'è solo un campione di smoke test da 12. Le discipline non sono enumerate nel README. I dati NC vanno bene per ricerca ma non vanno ridistribuiti nel repo pubblico | WATCH | |
| 5 | MC-NEST (hypothesis search via MCTS) | https://github.com/corei5/MC_NEST | Pattern: tenere vive più ipotesi-nodo, raffinarle e ripunteggiarle prima di potare. LEGEND ha già entrambe le metà (`diverge_hypotheses` in discovery-method; generate→critique→rank→evolve in `legend-hypothesis-forge`). L'unico delta reale: in forge il CRITIQUE viene subito dopo la generazione, prima di ogni raffinamento | 1 (una frase sull'ordine in forge, se il pilot 1/2 lo giustifica) | Nessuna licenza sul repo | Codice non riusabile (nessuna licenza, API GPT-4, ultimo push 2025-09). Il reward è giudicato da un LLM. Il "pubblicato il 25-09-2026" del radar è la versione su rivista di arXiv 2503.19309 (marzo 2025): non è un delta fresco | WATCH | |
| 6 | Micro-upgrade del radar "DIVERGE → PREDICT → DISCRIMINATE" come nuova fase tra Evidence e Mirror | radar (nessun repo) | Nessuna capacità nuova: DIVERGE, PREDICT e DISCRIMINATE sono già `diverge_hypotheses`, `preregister_prediction` e `compress_experiment`, e REVISIT è `recursive_reread`. I suoi quattro "test decisivi" però sono un buon disegno di valutazione e vanno nel TRIAL della riga 1 | 0 come fase; il disegno di valutazione è incluso nella riga 1 | n/a | Aggiungerla come fase o workflow obbligatorio viola la direttiva di task §26 citata in `legend-discovery-method` (nessun nuovo gate o workflow), e l'autore della skill dice che la primitiva che diventa gate ha fallito | REJECT | |
| 7 | Apprendimento di skill dalle traiettorie di ricerca | radar (ispirato alle trace di AgentIdeaBench) | Conservare query → risultato → guadagno di ipotesi e distillarne abitudini di ricerca riutilizzabili. Prerequisito da verificare prima: se le query di ricerca oggi sopravvivono in una receipt o in un transcript | 2 (solo l'audit); build non stimata | n/a | Rischio di un nuovo store, che `discovery-method` § 3 esclude esplicitamente ("There is no store for this and none should be built") | WATCH | |
| 8 | Ecosistema MIMS Harvard / Zitnik (ToolUniverse, ATHENA, AutoScientists, Medea) | radar (watchlist portata avanti) | Watchlist a livello di ecosistema, nessun artefatto singolo proposto questa settimana | 0 | varie | Nessuna in questa tornata; non riaperto | WATCH | |

## Top 3 for this week

1. **Il run di controllo dovuto, con disegno AgentIdeaBench (riga 1 + i test della riga 6).**
   `legend-discovery-method` § 4 dice che nessuna primitiva ha un controllo negativo e che un
   run disegnato tramite `legend-research-loop` è ancora dovuto. Il pilot: un nodo WWOX maturo
   (il radar propone oligodendrociti/mielina), stesso Scientist, stesso budget, due bracci:
   **Static** (10 paper consegnati) contro **Active** (solo la domanda, fino a 10 retrieval
   scelti in autonomia). Si punteggia con le quattro misure del radar: almeno 3 meccanismi
   causalmente distinti, almeno 1 predizione osservabile per ipotesi non contenuta nel
   pacchetto di evidenze, almeno 1 esperimento che discrimina almeno 2 ipotesi, un REVISIT che
   cambia qualcosa di sostanziale. A queste si aggiunge un baseline `copy` (un abstract
   riformulato passato allo stesso critic) per verificare che il critic sappia rifiutare la
   ricostruzione. Mirror punteggia in cieco rispetto al braccio. Nessuna fase nuova, nessun
   gate: l'output è una riga KEEP/DISCARD/INCONCLUSIVE di research-loop e una riga di
   osservabilità in `discovery-method` § 3.
   **Da confermare:** che il run tocchi il perimetro dello Scientist, non solo quello di HE.
2. **Backtest di preregistrazione T0/T1 (riga 2).** Si sceglie una data T0 **dopo il cutoff di
   training del modello** (altrimenti il modello ricorda T1). Si congelano gli stessi input
   dello Scientist ai paper del registro con data ≤ T0, si generano N predizioni per
   `preregister_prediction` e le si punteggiano contro i paper di data > T0 già letti.
   L'ordine di grandezza di N e la finestra T1 disponibile vanno misurati prima di impegnarsi.
   Si testa su un campione a mano, poi si decide se diventa uno script (`framework/scripts/`,
   instradato una volta sola secondo `test_tool_routing.py`).
3. **Audit delle traiettorie di ricerca (riga 7), 2 h.** Prima di qualsiasi costruzione, una
   domanda sola: le query di un giro di retrieval dello Scientist sopravvivono oggi da qualche
   parte (receipt, transcript di subagent)? Se sì, TRIAL leggendole; se no, la riga resta
   WATCH, perché costruire uno store è escluso.

## Watch-list carried forward

| candidate | first seen | why still WATCH |
|---|---|---|
| TruthInsightBench | 2026-09-28 | Il judge richiede un endpoint pagato o ospitato; nessun task biomedico confermato; si riapre quando il repo elenca i domini |
| ResearchBench | 2026-09-28 | Il sottoinsieme retrieval-only è economico, ma nessuna domanda di LEGEND ne ha ancora bisogno; si riapre se `connect_domains` va misurato |
| MC-NEST | 2026-09-28 | Il pattern è coperto da forge e discovery-method; si riapre solo se il TRIAL 1 mostra che le ipotesi vengono potate prima di essere raffinate |
| Apprendimento dalle traiettorie di ricerca | 2026-09-28 | Dipende dall'audit del Top 3 n. 3 |
| Ecosistema MIMS Harvard / Zitnik | carried (dal radar) | Si segue come ecosistema, nessun artefatto singolo |

## Looked at and rejected (one line each)

- La fase obbligatoria "DIVERGE → PREDICT → DISCRIMINATE" — duplica quattro primitive esistenti e diventerebbe un gate (§26). Il suo disegno di valutazione viene tenuto (Top 3 n. 1).
- Il codice MC-NEST — nessuna licenza, API GPT-4, fermo da un anno.

## Fuori dal perimetro harness — instradato, non valutato

Il radar contiene anche voci biomediche. Non sono candidati harness e non sono state verificate
qui. Appartengono a una sessione Scientist attraverso `legend-study-intake-triage` → `legend-ingest`:

- La terapia genica AAV9-WWOX neurone-specifica nel modello murino WOREE, che secondo il radar
  è passata da preprint a paper peer-reviewed (*Molecular Therapy Advances*, 2026-09-10).
  L'idea di follow-up del radar: stratificare i readout in rescued / partial / persistent.
- L'asse WWOX–MYC nella neurogenesi di organoidi cerebrali umani (*Brain*, 2026).
- Una review di *Cell* (2026-09-18) sulla biologia degli oligodendrociti, collegata al nodo
  di ipomielinizzazione WWOX. È un candidato per il nodo pilota del Top 3 n. 1.

## Handoff

Harness Engineering (ACTOR_ID `plan`) dà i verdetti su questa tabella al prossimo intervento
sull'harness e implementa ogni ADOPT e TRIAL a T0; questo file viene aggiornato con la colonna
HE verdict, `status: TRIAGED` e il commit che le porta su `main`.
