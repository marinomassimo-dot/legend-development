# Quota: audit indipendente del pannello VS Code

2026-09-11 · HARNESS ENGINEERING / ACTOR_ID `plan` · runtime Codex · HARNESS.
Continuazione di HARNESS-QUOTA-RESUME-001, directive_version 2, generation 1.
Il requisito resta il pannello Claude Code esistente in VS Code.

**Esito circoscritto:** nelle superfici esaminate non è stato trovato un metodo
supportato per inviare automaticamente una continuazione alla chat già aperta.
Esiste invece un URI pubblico per aprire/mostrare una sessione e precompilare testo:
non lo invia. Il percorso quota del pannello ispezionato aggiorna lo stato visivo,
senza un collegamento individuato al percorso di invio. Non è una dimostrazione
di impossibilità dell'intero obiettivo, né una deduzione dal requisito TTY del CLI.

## Identificazione della versione

- `/proc/291356/exe` e `/proc/291537/exe`: binario privato dell'estensione **2.1.267**.
- Entrambi appartengono all'extension host VS Code 279105; input/output stream-json.
- Il log Claude VSCode registra gli avvii dal percorso 2.1.267 il 2026-09-10;
  l'ultimo percorso rilevato è delle 20:58:26.706. I riferimenti 2.1.266 nei log
  precedenti non sono stati usati per identificare i processi attuali.
- Nessun wrapper personalizzato rilevato nel controllo precedente. Il percorso
  delle risorse lanciate e i log identificano 2.1.267 come bundle pertinente.
  Non è stato interrogato l'oggetto dell'estensione dentro l'extension host vivo:
  l'identificazione del bundle JS è corroborata dal lancio, non da un dump della
  memoria del pannello. La versione del binario vivo è osservata direttamente.
- **2.1.268** è installata, non sostituita ai processi attivi. Anche i suoi handler
  di apertura e precompilazione conservano i limiti descritti sotto.

L'[inventario di evidenze](SLR-plan-20260911-quota-panel-evidence.json) contiene
SHA-256 dei bundle, comandi e locator riproducibili. Gli offset sono indici di
caratteri UTF-8 decodificati, non offset byte. Le sorgenti sono sotto
`~/.vscode/extensions/anthropic.claude-code-<version>-linux-x64/`.

## Interfacce esaminate, oltre alle impostazioni

| Superficie | Percorso effettivo | Limite per questo incarico |
|---|---|---|
| URI pubblico `/open?session=ID&prompt=TESTO` | `registerUriHandler` → `claude-vscode.primaryEditor.open` → `createPanel` | apre/mostra la chat; non invia testo |
| Sessione già nel registro dei pannelli | `sessionPanels.get(ID)` → `reveal()` e ritorno | il prompt è esplicitamente rifiutato |
| Sessione non già aperta | caricamento sessione → `initialPrompt` → `setInputText` | solo bozza; se l'ID non viene trovato può nascere una nuova chat |
| Comandi VS Code registrati | 27 registrazioni letterali in 2.1.267, comprese quelle non nel manifest; elenco integrale nell'inventario | nessun comando di invio o ripresa quota di una sessione identificata |
| `newConversation` | notifica `create_new_conversation` | crea altra conversazione |
| `reopenClosedSession` | riapre ultimo tab chiuso o fallback al comando VS Code | non invia una continuazione e non indirizza il task quota |
| Export di estensione | modulo con `activate`/`deactivate`; `activate` inizializza il pannello senza restituire un'API sessioni | nessuna API di invio restituita al chiamante individuata |
| Webview → host | `send` → `sendInput` → `io_message` → `transportMessage` → coda del canale | trasporto privato, non comando/API pubblica per un processo esterno |
| Server IDE MCP | registrazioni `openDiff`, diagnostica, file/editor/selezione, salvataggio e notebook | nessun tool di invio a una chat; non è stato connesso un client di prova |

La [guida ufficiale VS Code](https://code.claude.com/docs/en/vs-code#launch-a-vs-code-tab-from-other-tools)
documenta `session` e `prompt`: quest'ultimo precompila soltanto il campo; una
sessione già aperta viene mostrata, mentre un ID assente può aprire una chat nuova.
Nel bundle, il ramo della sessione già aperta espone inoltre il messaggio:
“Session is already open. Your prompt was not applied — enter it manually.”
Questo ramo precede la creazione del webview. Non è stato aggirato.

Il server IDE MCP ammette un solo client attivo e il suo handler può scollegare
quello precedente: l'ispezione è rimasta statica per non interferire con gli agenti.
Un metodo interno presente nel bundle non diventa per questo un'API supportata;
non sono stati chiamati socket interni, iniettato JavaScript o modificati file
dell'estensione. Nessuna automazione di clic o tastiera.

## Percorso quota del pannello, indipendente dal CLI

Il tracciamento è stato effettuato nel bundle 2.1.267:

1. L'host inoltra `rate_limit_event` nel canale `io_message`. Se sono presenti
   `unifiedWindows`, chiama `onRateLimitWindows`, poi il relay delle barre quota.
   Il relay produce `panel_usage_update`; non produce un messaggio utente.
2. Nel webview, `readMessages` riceve l'evento, aggiorna le finestre e chiama
   `setUsageLimitGrace`. `DN1` decide show/clear/keep-hidden; `YF0` formatta
   l'avviso e l'ora del reset. L'eventuale notifica overage è un altro ramo visivo.
3. `setUsageLimitGrace` gestisce finishing/stopped/covered/dismissed. L'effetto
   reattivo trasforma finishing in stopped quando `busy` termina. Non pianifica
   l'invio al reset.
4. Le dipendenze `shownRateLimit`, `frameRateLimitWarning`, `rateLimitWarning` e
   le 18 occorrenze di `resetsAt` sono state seguite: deduplica degli avvisi,
   riconciliazione delle finestre, formattazione e barre. Non è stato trovato un
   passaggio da quei dati a `sendInput`.
5. Sono stati controllati anche i riferimenti di invio, retry e timer nella parte
   applicativa. I retry individuati riguardano fra l'altro sincronizzazione lista
   sessioni, lettura quota e altre UI; non sono stati scambiati per retry del task.
   I timer delle librerie incluse non sono stati tutti analizzati integralmente.
6. Il percorso che invia un turno è distinto: `session.send()` costruisce un
   messaggio utente con UUID, riutilizza `claudeChannelId` se presente, aggiorna
   `busy` e passa a `connection.sendInput`. I chiamanti applicativi esaminati sono
   invio utente e azioni specifiche come una risposta approvata a una domanda
   ripristinata o aiuto debugger/notebook. Non è esposto al processo locale come
   continuazione quota supportata.

Queste sono evidenze statiche del pannello. Non si dichiara un collaudo dinamico
completo né l'assenza assoluta di ogni comportamento possibile dietro feature flag.
L'esclusione del percorso CLI interattivo, documentata nel rapporto precedente,
è un'evidenza **separata** e non la premessa di questa conclusione.

## Altre vie supportate considerate

- `claude --help` e `claude agents --help` eseguiti soltanto per leggere l'help,
  senza prompt, sessione nuova o inferenza. La gestione/discovery degli agenti
  non offre lì un comando deterministico di invio alla chat VS Code attiva.
- [Cross-session messaging](https://code.claude.com/docs/en/cross-session-messaging)
  documenta `ListAgents` e `SendMessage` come strumenti che Claude usa. La pagina
  non documenta un client esterno senza LLM per il socket di una sessione. Non è
  stato implementato un protocollo ricavato dai file interni.
- I [channels](https://code.claude.com/docs/en/channels) sono una vera API per
  eventi esterni, non sono stati ignorati. Richiedono opt-in per sessione tramite
  `--channels`; la presenza di un server MCP non basta. I processi vivi non hanno
  quel flag. Non è stato trovato nel pannello un comando supportato per abilitarlo
  sulla conversazione viva. La documentazione avverte inoltre che l'uso channels
  non interattivo disabilita alcuni tool che chiedono input: non si è presunta
  equivalenza alle approvazioni del pannello. Nessun plugin, launcher o server
  alternativo è stato introdotto per forzare questa strada.

Non si afferma che channels o un'API futura non possano mai coprire la GUI. Manca
oggi, nelle superfici verificate, il contratto dimostrato di invio alla stessa
chat aperta con le autorizzazioni attuali.

## Subagent: verifica separata

Nel pannello `task_started` registra l'ID del figlio e il tool-use originario;
`task_updated` elimina dall'elenco gli stati completed/failed/killed;
`task_notification` elimina l'ID notificato. `background_tasks_changed`
riconcilia l'elenco. Non è stato individuato in questi handler un timer di
recupero quota o una richiesta di resume del figlio.

La [documentazione subagent](https://code.claude.com/docs/en/sub-agents#resume-subagents)
descrive una capacità reale: Claude può inviare `SendMessage` all'ID/nome di un
agente riprendibile, avviando un nuovo run sotto lo stesso ID e con la cronologia
precedente. Un agente annullato dall'utente non riparte automaticamente; i
messaggi non costituiscono approvazione per richieste pendenti. Non basta una
nuova invocazione generica di `Agent`, che può creare un'altra istanza.

**Esito:** capacità di ripresa del figlio documentata; recupero automatico quota
dei Scientist del laboratorio NON COLLAUDATO. Non sono stati inviati messaggi
ai figli reali o al coordinatore. Il futuro test deve osservare il medesimo ID
del figlio, nuovo stato running, continuazione del transcript e skip delle
milestone già concluse; un solo nuovo turno del padre non supera il test.

## Collaudo, stato e limite esatto

Nessuna sessione di prova è stata avviata: non è emerso un candidato che supporti
l'invio richiesto. La via URI è esclusa già dal suo contratto documentato e dal
ramo applicativo. Non viene presentato un test con mock o una bozza precompilata
come prova di continuazione reale. **Nessun timer introdotto.**

| Verifica | Stato |
|---|---|
| Configurazione true e backup del primo intervento | invariati |
| Identificazione binario vivo e audit bundle pertinente | eseguiti, limite di osservazione JS dichiarato |
| Comandi, URI, export, percorso evento quota e invio | ispezionati |
| Metodo supportato per submit alla stessa chat viva | NON TROVATO nelle superfici verificate |
| Test reale su chat di prova, senza duplicati | NON ESEGUITO: manca quel metodo |
| Ripresa reale Scientist dopo quota | NON VERIFICATA |
| Timer locale / modifica estensione / migrazione al terminale | NON IMPLEMENTATI |

Il test naturale del rapporto precedente resta disponibile, ma non si presume
che salvi una funzione assente dal percorso verificato. Per proseguire serve un
comando/API che accetti l'identità della chat viva e invii davvero un turno,
oppure un'attesa nativa del pannello documentata e osservabile. Solo dopo il test
di identità si aggiungerebbe un'unica ripartenza pendente per sessione, ammessa
esclusivamente sullo stato esplicito quota e cancellata per attività, conclusione,
annullamento o approvazione pendente. Nessuna modifica al modello o alla spesa.

## Correzione del primo rapporto e session learning

La precedente formula «GUI non coperta» era più ampia della sua prova principale:
il requisito interattivo escludeva il percorso CLI nativo, non dimostrava da solo
il comportamento del pannello. Questo approfondimento aggiunge l'audit autonomo
del pannello e il limite concreto del suo URI pubblico. Il registro conserva la
prima evidenza e distingue la nuova, senza trasformarle in un'impossibilità assoluta.

DEFAULTS_TAKEN: mantenute tutte le sessioni e la configurazione; niente timer
senza attuatore dimostrato. STOP_LOG: nessuna richiesta di approvazione; limite
tecnico circoscritto, documentato secondo la direttiva 2. DECISIONS_TAKEN: nessuna
infrastruttura alternativa, nessuna riapertura di agenti reali, nessuna modifica
ai task harness altrui.

Micro-upgrade di capability-scout: inventario riproducibile dei punti d'ingresso
con separazione fra **mostrare**, **precompilare**, **inviare** e **riprendere un
figlio**. Verifica documentale/statica, nessuna conclusione scientifica.
