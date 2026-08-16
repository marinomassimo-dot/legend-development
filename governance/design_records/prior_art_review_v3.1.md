# LEGEND GOVERNANCE v3.1 — TARGETED HOSTILE PRIOR-ART REVIEW
## Matrice cross-framework e proposta di emendamenti (max 10)

**Mandato:** review della governance corrente contro Paperclip, Microsoft Agent Framework (MAF), Google ADK 2.0, A2A, OpenHands, Agno, Pydantic AI, Letta (solo identity/memory). Estrarre pattern, non dipendenze. No migrazioni di runtime. Ogni ADAPT con GUARANTEE / FAILURE MODE STILL POSSIBLE / DETECTION / RECOVERY.

**Nota di sequenza:** la review è eseguita sulla **v3.1** (che ha già assorbito Paperclip), non sulla v3.0: funge da validazione pre-congelamento. Esito possibile: congelare 3.1, o emettere 3.1.1 con gli emendamenti accettati.

**Stato delle fonti (verifica primaria, ago 2026):**
- Paperclip — repo GitHub verificato (turno precedente): checkout atomico, approval queue, budget hard-stop, org chart, export/import. ✔
- MAF — docs Microsoft Learn: checkpoint per superstep, resume con verifica di struttura (hash: graph diverso → resume RIFIUTATO), Durable Extension "completed calls aren't repeated"; critica terza parte: nessun failure detection/lease nativo. ✔
- ADK 2.0 — stabile 19/05/2026: Workflow Runtime (retry, state, HITL, nested), Task API con modi Chat/Task/SingleTurn. ✔
- A2A — spec Linux Foundation: Agent Card, task lifecycle `submitted, working, input-required, completed, failed, canceled, rejected`, messageId per dedup, push notifications. ✔
- OpenHands — event stream append-only come backbone e memoria; "state changes by appending events, never by mutating"; replay-by-construction; V1: unico oggetto mutabile = ConversationState. ✔
- Pydantic AI — deferred tools con `requires_approval`, ApprovalRequired, DeferredToolResults per tool_call_id (APPROVED anche con argomenti modificati | DENIED con messaggio); durable execution (Temporal/Restate/DBOS/Prefect) con replay che NON riesegue i passi completati; nota di sicurezza: l'approval non sostituisce l'authorization dentro l'azione. ✔
- Letta — memory blocks con label e **character budget**, attached/detached, blocchi condivisi, block checkpointing/versioning; Agent File (.af) per serializzazione portabile; critica terza parte: blocchi riscritti in place = provenance debole (LEGEND evita già questo con lossless+derived_from). ✔
- **Agno — NON verificato indipendentemente** in questa review (solo descrizione secondaria: control plane, RBAC, approval, audit). Le sue righe sono marcate ⚠ e il deep dive è nel registro DEFER. Nessun emendamento poggia solo su Agno.

---

## PARTE 1 — PREMESSA ONESTA: GARANZIE SERVER-BACKED CHE LEGEND NON HA

| Garanzia | Chi la possiede | LEGEND file/worktree-based |
|---|---|---|
| Task checkout atomico (lock) | Paperclip (server) | NO — single-assigner + claim record + rilevazione conflitto (A.3) |
| Exactly-once / delivery garantita | A2A push, broker | NO — ACK + dedup MESSAGE_ID + reinvio (B.3) |
| Transactional workflow state + replay automatico | MAF Durable, Temporal/Restate | NO — snapshot + restore manuale documentato (D.4) + rehydration |
| Failure detection + restart automatico | Temporal; NON MAF standard | PARZIALE — heartbeat + DOWN + operatore riapre (§36.4) |
| RBAC enforced a runtime | Agno ⚠, Paperclip | NO per attori interattivi — authority testuale + audit (misurato: enforcement solo su alcune superfici) |
| Singleton garantito (CAS) | server DB | NO — lease record + rilevazione doppio ACTIVE + stop condition (I.3) |

Questa tabella diventa l'**emendamento 10**: oggi questi fatti sono sparsi nei blocchi G/F/D/R; consolidarli in un unico punto citabile.

---

## PARTE 2 — MATRICE PER PRIMITIVE

Colonne: design v3.1 → prior art rilevante → failure mode non coperto → verdetto → emendamento.

| # | Primitive | LEGEND v3.1 | Prior art | Failure mode non coperto | Verdetto | Em. |
|---|---|---|---|---|---|---|
| 1 | First-run bootstrap | Parte 0 + Annex I: BOOTSTRAP_CONTROLLER → qualificazione → lease | Paperclip CEO-first; A2A lifecycle Creation (card pubblicata prima del servizio) | nessuno materiale; A2A conferma "identità pubblicata prima dell'operatività" | **KEEP** | — |
| 2 | Actor identity | ACTOR_ID ≠ SESSION_REF + registry I.4 | A2A Agent Card (identità + capabilities + skills); Letta .af | il registry non dichiara le CAPABILITIES: Orchestrator assegna per ruolo presunto, non per capacità dichiarate e verificate | **ADAPT** | E5 |
| 3 | Singleton Orchestrator | Lease con heartbeat/expiry/STALE/reacquisition (I.3, G/F/D/R) | MAF: nessun lease (lacuna loro); Paperclip: server-side | già dichiarato onestamente il race sulla reacquisition | **KEEP** | — |
| 4 | Assignment/ACK/claim/generation | Annex A completo | Paperclip atomic checkout; ADK Task API; A2A task object | il Task Contract non dichiara se l'attore PUÒ fermarsi con domande (modo d'interazione) | **ADAPT** | E6 |
| 5 | Task concurrency | claim + generation, G/F/D/R onesto | Paperclip execution locks | già coperto al livello onestamente possibile | **KEEP** | — |
| 6 | Messaging | Annex B: envelope, tipi, ACK, dedup | A2A: messageId dedup (identico), input-required, push | nomenclatura stati incompatibile con lo standard di fatto → costo futuro di interop | **ADAPT** (mappa nominale, non rinomina) | E5 |
| 7 | Heartbeat | B.3, alimenta DOWN | Paperclip heartbeats (wake-model: REJECT); MAF: assente | nessuno | **KEEP** | — |
| 8 | Actor/Lab state | J.2 (ORPHAN come LAB_STATE) | A2A task states; Paperclip agent states | manca lo stato task AWAITING_APPROVAL (≈ A2A input-required) | **ADAPT** | E3 |
| 9 | Interruption / recovery | §36 rotazione + rehydration + DOWN | **MAF: checkpoint con verifica di struttura — resume su graph mutato RIFIUTATO** | il checkpoint LEGEND non è un oggetto formale: nessun binding a governance/directive/generation → resume su stato incompatibile possibile e silenzioso | **ADAPT** (il reperto più importante della review) | E1 |
| 10 | Approvals / HITL | Gate 3, HUMAN_APPROVAL_QUEUE J.3 | Pydantic: APPROVED-con-modifica / DENIED-con-messaggio; "approval ≠ authorization" | (a) esito approvazione binario; (b) non è scritto che i gate si applicano COMUNQUE dopo l'approval | **ADAPT** | E3, E4 |
| 11 | Cost controls | COST_POLICY J.4, envelope | Paperclip budget hard-stop | nessuno per il target attuale (contabilità sofisticata = overengineering) | **KEEP** | — |
| 12 | Event ledger | J.1 append-only, one-writer, G/F/D/R | **OpenHands: eventi come backbone; action→observation pairing; replay-by-construction** | eventi "aperti" senza linkage all'esito → il ledger dice cosa è iniziato, non sempre come è finito | **ADAPT** | E8 |
| 13 | Commit transactionality | Gate 0–5, content hash, restore D.4 | MAF/Temporal; Zylos: "ogni operazione mutante è un confine di transazione" | il principio idempotente "completed work is not repeated" esiste solo per le letture (receipt ledger), non generalizzato al resume di ogni task | **ADAPT** | E2 |
| 14 | Review workflows | Ladder + floor, formato unico, Annex C | ADK HITL nodes; OpenAI SDK guardrails (non verificato qui) | nessuno materiale | **KEEP** | — |
| 15 | Durable execution | rehydration + stato durevole + WORK_COMMIT | MAF Durable, Temporal (server-backed) | coperto onestamente dalla Parte 1; runtime esterni = REJECT | **KEEP + REJECT runtime** | — |
| 16 | Learning / memory compression | E.5 lossless + derived_from + subset per ruolo | **Letta: block con character budget**; critica ai blocchi riscritti in place | i subset ACTIVE_LESSONS non hanno budget dimensionale → ricrescita silenziosa fino a mangiare il context | **ADAPT** (+ conferma forte del design lossless) | E9 |
| 17 | Portability | I.5 lab definition ≠ runtime instance | Letta .af; Paperclip export/import | nessuno materiale (la repo È il formato di serializzazione di LEGEND) | **KEEP** | — |

**REJECT espliciti (invariati):** runtime heartbeat/wake-sleep (Paperclip, MAF hosting) — opposto al requisito attori visibili; sostituzione delle chat con job; adozione integrale A2A come protocollo di trasporto (oggi non serve: un solo control plane).

---

## PARTE 3 — I 10 EMENDAMENTI PROPOSTI

### E1 · CHECKPOINT come oggetto formale con STRUCTURE BINDING — da MAF ★ il più importante
Oggi "checkpoint su stato durevole" (§36.2) è un obbligo senza schema. Formalizzare (Annex A o J):

```
CHECKPOINT: CHECKPOINT_ID / ACTOR_ID / TASK_ID + DIRECTIVE_VERSION + GENERATION /
GOVERNANCE_VERSION / milestone raggiunte / puntatori a output durevoli / timestamp
```

Regola (il pattern MAF del rifiuto su mismatch): **la rehydration che trova un checkpoint con directive_version, generation o governance_version diversi da quelli correnti NON riprende il lavoro — segnala e chiede stato a Orchestrator.**

```
GUARANTEE:  un attore non riprende mai silenziosamente lavoro sotto contratto o governance superati
FAILURE:    checkpoint non scritto prima del crash → si riparte dall'ultimo valido (lavoro perso accettato, §3)
DETECTION:  mismatch rilevato alla rehydration; checkpoint assente = ultimo valido più vecchio
RECOVERY:   richiesta stato a Orchestrator → nuovo contratto o conferma → ripresa
```

### E2 · RESUME IDEMPOTENTE — "completed work is not repeated" generalizzato — da MAF/Temporal
Il pattern receipt-ledger (il ledger decide se un paper è letto) diventa regola generale: **prima di rieseguire un passo dopo resume/retry, l'attore verifica nello stato durevole se l'output di quel passo esiste già; se esiste, non lo rifà.** Corollario (Zylos): ogni operazione mutante è un confine di transazione — milestone committata subito dopo l'operazione, non a fine task.

```
GUARANTEE:  niente doppio lavoro sui passi già completati e resi durevoli
FAILURE:    passo completato ma non ancora durevole al crash → verrà rifatto (accettato, è il caso base)
DETECTION:  esistenza dell'output nello stato durevole
RECOVERY:   skip del passo + registrazione RESUMED_FROM_MILESTONE
```

### E3 · Stato task AWAITING_APPROVAL + esito approvazione ricco — da Pydantic AI / A2A
Aggiungere ad A.5: `IN_PROGRESS → AWAITING_APPROVAL → IN_PROGRESS | CANCELLED` (≈ A2A `input-required`). Il task si parcheggia al punto esatto (checkpoint E1) e riprende senza rifare lavoro (E2). Esito dell'approval (J.3) arricchito: `APPROVED | APPROVED_WITH_MODIFICATION (argomenti/scope modificati, nuova directive_version) | DENIED (con motivazione che torna all'attore) | REVISION_REQUESTED`.

```
GUARANTEE:  la semantica di un'approvazione mid-task è definita; il diniego è informativo, non un buco
FAILURE:    approvazione arrivata dopo che il contesto dell'attore è degradato/ruotato
DETECTION:  checkpoint E1 + generation check alla ripresa
RECOVERY:   rehydration → ripresa dal checkpoint del punto di parcheggio
```

### E4 · Clausola "APPROVAL ≠ AUTHORIZATION" — da Pydantic AI (nota di sicurezza)
Una riga in J.3: **l'HUMAN_APPROVAL autorizza l'intento, non bypassa i gate: l'esecuzione approvata resta soggetta a GATE 0–5, stop conditions e authority matrix.** Un MAJOR approvato con root dirty resta NO BATCH. (Chiude un'ambiguità reale: oggi si potrebbe leggere l'approval come lasciapassare.)

### E5 · LEGEND AGENT CARD + mappa nominale A2A — da A2A
(a) Arricchire l'ACTOR_ID registry (I.4) con `CAPABILITIES:` dichiarate nel role contract e **verificate in L2** (una capability dichiarata ma non smoke-tested è marcata UNVERIFIED — CONFIGURED != PROVEN applicato alle capacità). Orchestrator assegna sulle capabilities verificate, non sul ruolo presunto — abilita anche il soft routing §32.
(b) Documentare in Annex B una **mappa nominale** (non una rinomina): `ASSIGNED≈submitted · IN_PROGRESS≈working · AWAITING_APPROVAL/BLOCKED≈input-required · COMPLETE≈completed · CANCELLED≈canceled · REJECTED(ACK)≈rejected`. Costo ~zero oggi; interop non preclusa domani.

```
GUARANTEE:  assegnazioni basate su capacità verificate; vocabolario convertibile allo standard di fatto
FAILURE:    capability degradata dopo L2 (deriva del runtime)
DETECTION:  fallimenti ripetuti sullo stesso tipo di task → Mirror coordination review
RECOVERY:   capability retrocessa a UNVERIFIED → nuovo smoke
```

### E6 · INTERACTION_MODE nel Task Contract — da ADK 2.0 (Chat/Task/SingleTurn)
Campo in A.1: `INTERACTION_MODE: AUTONOMOUS_COMPLETE | QUESTIONS_ALLOWED | SINGLE_TURN`. Dichiara ex ante se l'attore può fermarsi con un BLOCKER/domanda o deve completare autonomamente. Elimina l'ambiguità "si è fermato legittimamente o non doveva fermarsi?" — che oggi finirebbe in DIAGNOSE senza criterio.

### E7 · RETRY_POLICY per task — da ADK Workflow Runtime
Campo in A.1: `RETRY_POLICY: max_attempts / classi di errore ritentabili / on_exhaust: REASSIGN | PARK | ESCALATE`. Oggi il retry è discrezione di Orchestrator senza contratto; con E2 il retry è anche idempotente. Default definito da Plan; Orchestrator può derogare con rationale.

### E8 · EVENT ledger: linkage apertura→esito + replayability dichiarata — da OpenHands
In J.1: (a) ogni evento "aperto" (TASK_ASSIGNED, REVIEW_OPENED, HUMAN_REQUIRED_OPENED, LEASE_ACQUIRED…) referenzia l'evento di chiusura quando esiste (`closed_by: EVENT_ID`) — il ledger risponde anche "com'è finita", non solo "cos'è iniziato"; (b) principio esplicito: **la vista di runtime è ricostruibile per replay del ledger consolidato, ma lo stato repo resta sovrano** (in conflitto vince il repo; il ledger è audit e analisi, mai seconda fonte di verità). Conferma inoltre la scelta v3.1 "mai mutare, solo appendere".

### E9 · Budget dimensionale per gli ACTIVE_LESSONS — da Letta (block limits)
In E.5: ogni subset role-specific ha un **budget di dimensione** definito da Plan (caratteri/token per ruolo). Superato il budget: Mirror comprime o retrocede lezioni (mai cancellando il RAW, che resta lossless). Nota di conferma per il record: il confronto con Letta valida il design LEGEND — i blocchi Letta riscritti in place hanno provenance debole; lossless + `derived_from` è la scelta più forte, e va mantenuta.

### E10 · Tabella unica "GARANZIE NON POSSEDUTE" in Annex J
La tabella della Parte 1 entra in Annex J come sezione normativa, referenziata dai CLAUDE.md. Un punto solo dove ogni attore (e l'operatore) legge cosa il sistema NON garantisce, con puntatori ai G/F/D/R di dettaglio.

---

## PARTE 4 — REGISTRO DEFER (con trigger di riapertura)

| Voce | Trigger di riapertura |
|---|---|
| Adozione A2A come protocollo | attori eterogenei fuori dal control plane Claude, o deployment multi-macchina con agenti remoti |
| Runtime durable esterno (Temporal/MAF Durable) | mai, salvo abbandono del requisito attori visibili (decisione operatore) |
| Team coordinators (gerarchia a 2 livelli) | > 8 attori persistenti |
| AgentScope / distribuzione multi-host | LEGEND oltre il singolo Mac |
| Deep dive Agno ⚠ + OpenAI Agents SDK | prossimo ciclo prior-art, post primi batch reali |

---

## PARTE 5 — VERDETTO

La v3.1 regge bene il confronto: **10 KEEP su 17 primitive**, nessun REJECT di design proprio, e su learning pipeline e honest-guarantees LEGEND è più avanti del prior art esaminato (Paperclip: organizational learning ancora in roadmap; Letta: provenance dei blocchi più debole del lossless+derived_from; MAF: nessun failure detection né lease — LEGEND li ha).

I 10 emendamenti sono chirurgici: 2 sostanziali (E1 checkpoint con structure binding, E2 resume idempotente — insieme chiudono la classe "ripresa su stato incompatibile / doppio lavoro al resume" che nessuna sezione attuale copre), 4 medi (E3, E5, E7, E8), 4 clausole leggere (E4, E6, E9, E10). Nessuno tocca l'architettura; tutti entrano come patch agli annessi A, B, E, I, J + tre righe nel corpo.

**Raccomandazione: emettere v3.1.1 con i 10 emendamenti (o il sottoinsieme che l'operatore ratifica) e CONGELARE. Poi materializzazione Plan → hostile review Mirror → HUMAN_APPROVAL → canonical commit → bootstrap.** Dopo il congelamento, stop all'architettura per alcuni cicli: la v3.2 dovrà essere evidence-driven, alimentata da autonomy ledger, review yield e dissent lifecycle — non da altro brainstorming.
