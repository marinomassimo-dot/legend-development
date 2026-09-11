# Ripresa dopo limite quota — configurazione e primo audit del percorso nativo

**Approfondimento successivo, direttiva 2:** [audit indipendente del pannello](SLR-plan-20260911-quota-panel-audit.md).
La restrizione interattiva qui rilevata riguarda il percorso CLI nativo e, da sola,
non dimostra il comportamento del pannello. Il secondo rapporto verifica comandi,
URI, trasporto ed eventi del pannello e circoscrive il limite dell'integrazione.

Data: 2026-09-11 UTC. ACTOR_ID: `plan`, ruolo assegnato dall'operatore:
HARNESS ENGINEERING; runtime Codex; SESSION_PROFILE HARNESS.
Incarico: `ledger/tasks/plan/HARNESS-QUOTA-RESUME-001.json` (ACK, claim e baseline).
Governance 3.1.1; fingerprint nel contratto. Manifest READY; LINT PASS.

**Esito:** `autoContinueAtUsageLimit: true` è salvato e il cambiamento è stato
rilevato dai processi esistenti. Tuttavia il meccanismo nativo ispezionato non copre
i pannelli VS Code attuali: richiede un terminale interattivo. Nessuna ripartenza
reale è stata collaudata. La configurazione non soddisfa da sola l'obiettivo GUI.

## Modifica e ripristino

- File utente: `/home/desktop/.claude/settings.json`.
- Backup privato: `/home/desktop/.claude/settings.json.bak-quota-resume-20260911T100631Z`, permessi 0600.
- Modifica atomica con controllo di concorrenza prima della sostituzione. JSON valido;
  valore booleano true; confronto strutturale di tutte le altre proprietà PASS;
  backup confrontato byte per byte PASS. Hash prima/dopo nel contratto.
- Non sono stati modificati modello, abbonamento, extra usage, credenziali,
  autorizzazioni, hook, impostazioni scientifiche o altre preferenze.
- Per disabilitare: cambiare **soltanto** questa proprietà in `false` nel file utente.
  Rimuoverla non equivale necessariamente a disabilitarla: nel terminale supportato
  la funzione è normalmente attiva per default. Il backup serve per recuperare lo
  stato precedente; non ripristinarlo integralmente dopo ulteriori modifiche utente.

## Versione, processi e copertura

Fotografia locale del 2026-09-11, non inventario permanente:

| Superficie | Evidenza | Copertura della ripresa automatica |
|---|---|---|
| Processo Claude 291356 | eseguibile nell'estensione 2.1.267, parent 279105 (VS Code); sessione `d9ba7473…`; transcript con incarichi rivolti all'Orchestrator | escluso dalla condizione interattiva |
| Processo Claude 291537 | stesso eseguibile e parent; session metadata `b1601d03…`; identità di ruolo non accertata | stesso limite; non conteggiato come Scientist indipendente |
| Scientist osservati | tool `Agent`, `subagent_type: claude`, `run_in_background: true`; transcript figli sotto `subagents/` della conversazione coordinatrice | nessuna attesa autonoma dimostrata; ripresa del padre non prova ripresa del figlio |
| Estensione 2.1.268 installata | schema presente; binario conserva il requisito interattivo | un aggiornamento alla 2.1.268 non risolve il limite trovato |
| Eventuali terminali interattivi dello stesso utente | ereditano il file utente salvo impostazioni ammesse prevalenti; nessuno osservato nel censimento | configurazione pertinente, comportamento reale ancora da verificare |

Entrambi i processi attivi hanno `CLAUDE_CODE_ENTRYPOINT=claude-vscode`, HOME
`/home/desktop`, cwd del progetto, input/output `stream-json` e
`--setting-sources=user,project,local`. Stdout è un socket, non un TTY. Nessun
`CLAUDE_CONFIG_DIR`, `--settings` o override di lancio pertinente osservato.
Non è stata aperta alcuna conversazione CLI concorrente.

Il transcript storico `3e1bc608…` contiene altri incarichi e subagent; non è stato
scambiato per una terza sessione attiva. Nei transcript del coordinatore e di due
figli risultano errori quota del 2026-09-11 intorno alle 06:48 UTC, **precedenti**
alla modifica delle 10:06:31 UTC: non costituiscono un test della nuova impostazione.

## Impostazioni prevalenti ed efficacia

La proprietà era assente dal file utente e dal file progetto. File locale assente;
nessun `/etc/claude-code/managed-settings.json` né frammento
`managed-settings.d/*.json` rilevato. Nessuna occorrenza della proprietà in
`~/.claude.json` o nelle impostazioni utente VS Code. Non sono state interrogate
credenziali o policy remote dell'account: il controllo locale non certifica lo
stato amministrativo del servizio.

La chiave ha regole di consenso proprie: non va trattata come una generica
preferenza che il repository può accendere. La documentazione descrive anche
un veto da repository quando manca un valore utente/CLI/managed applicabile.
Qui è stata impostata esplicitamente dall'utente tramite l'incarico.
[Precedenza e aggiornamenti](https://code.claude.com/docs/en/settings).

Il log esistente
`~/.config/Code/logs/20260909T170316/window1/exthost/Anthropic.claude-code/Claude VSCode.log`
riporta rilevamenti della modifica alle **10:06:32.839 e 10:06:32.845 UTC**.
È evidenza del watcher, non dell'armamento del timer. L'impostazione è letta dal
modulo nativo al momento dell'armamento; non richiede il riavvio per il suo normale
percorso supportato. Accenderla dopo un errore già terminato non prova che quell'errore
venga riarmato retroattivamente.

Nessun agente è stato fermato o riavviato. Non è necessaria una riapertura per
salvare questa preferenza. Per un futuro aggiornamento che aggiunga esplicitamente
supporto GUI: attendere che le chat e i figli abbiano completato o depositato un
checkpoint, riaprire le conversazioni dalla cronologia nello stesso pannello e
ricontrollare eseguibile e ID. Non ricaricare VS Code durante lavoro o attesa quota.

## Perché lo schema non basta

Ispezione statica del JavaScript incluso nei binari installati, senza eseguirli:

1. In 2.1.267 `hu()` legge `launchOptions.isInteractive()`.
2. `zmr()` identifica come non interattivo anche stdout non TTY; l'avvio chiama
   `YBn(!O)` con tale risultato.
3. Il modulo quota usa `F() = hu() && !_t()`; `_t()` identifica il background.
   `_de()` richiede quella condizione, login/billing pertinenti e quota rifiutata
   con reset finito. `TKn()` controlla inoltre consenso, finestra e deduplicazione.
4. Il modulo corrispondente in 2.1.268 mantiene la condizione interattiva.
5. Nei webview di entrambe le versioni il gestore `rate_limit_event` aggiorna gli
   avvisi; nessuna occorrenza di `autoContinueAtUsageLimit`, `quota_auto_resume` o
   `auto-continuation`. Quest'assenza è solo evidenza complementare alla condizione
   positiva del binario, non una prova universale di assenza di ogni automazione.

SHA-256 dei binari esaminati:

| Versione | SHA-256 |
|---|---|
| 2.1.267 | `0399c793ff571d5946ef923d80b4f330d05ac4b6842a6b0775468f5d389403c0` |
| 2.1.268 | `9691a2b7bd796712ca8cffb8e32e54ff7fc45b662540233171a16a94a0425653` |

La [documentazione della modalità interattiva](https://code.claude.com/docs/en/interactive-mode#wait-for-a-usage-limit-to-reset)
conferma il perimetro: abbonamento claude.ai, sessione aperta, esclusione del
background e delle esecuzioni non interattive. L'attesa usa il reset, non richieste
periodiche al modello. La prosecuzione è un normale turno con consumo ordinario e
richieste di permesso. Reset oltre 24 ore, sospensione prolungata, chiusura o
trasferimento della sessione e ripetuti limiti possono impedire la prosecuzione.

## Distinzione degli arresti e collaudi eseguiti

| Caso | Evidenza statica / esito |
|---|---|
| Quota temporanea | richiede errore quota, stato rejected, reset numerico finito e billing compatibile |
| Lavoro concluso | un completamento ordinario non è il trigger quota |
| Arresto volontario | percorsi di annullamento per Escape/Ctrl+C, invio manuale, cambio conversazione e uscita; deduplica della finestra annullata |
| Autenticazione scaduta | non trattata dal predicato come quota con reset; recupero login non implementato da questo incarico |
| Errore non recuperabile | non è trigger quota; un fallimento della continuazione può cancellare l'attesa |
| Duplicati | UUID della continuazione e reset-key dedup nel modulo; non è garanzia exactly-once delle operazioni scientifiche |

JSON, backup e conservazione impostazioni: PASS. Watcher: modifica rilevata.
Controllo isolato di sette casi dei predicati trascritti: PASS (quota, successo,
auth, errore fatale, reset assente, overage, modalità non interattiva). È un controllo
con dipendenze simulate, non esecuzione del prodotto né prova di classificazione
degli errori backend. Il tentativo iniziale con Node locale non è partito perché
`node` manca; ripetuto nel motore JavaScript degli strumenti, senza installazioni.
Annullamento, ripresa reale, conservazione ID, assenza di doppie esecuzioni,
Scientist e viewer disconnesso: **NON COLLAUDATI**.

## Collaudo minimo al prossimo evento naturale — PENDENTE

Nessun servizio, cron, loop LLM o messaggio periodico aggiunto. Il test è osservativo;
non induce consumo per raggiungere il limite. Con queste versioni si prevede che
il pannello mostri il limite senza armare l'attesa: registrarlo come mancata
copertura, non come test riuscito e non avviare tentativi ripetuti.

1. Annotare versione realmente in esecuzione, ID della conversazione, PID,
   TASK_ID/generation e ultima milestone già durevole. Identificare separatamente
   gli ID dei figli Scientist; non basta il titolo della chat.
2. Al limite naturale, registrare timestamp UTC, tipo quota e reset mostrato.
   Cercare l'indicazione esplicita di attesa/prosecuzione automatica. Un semplice
   avviso di quota, una chat inattiva o un PID vivo non attestano il timer.
3. Se l'attesa viene effettivamente armata, lasciare VS Code e desktop VPS aperti;
   scollegare soltanto il viewer TurboVNC e annotare disconnessione/riconnessione.
   Verificare poi che i messaggi successivi al reset abbiano timestamp compresi
   nell'intervallo senza viewer. Processi Xvnc, XFCE e Code esistenti confermano
   l'architettura persistente, non questo risultato operativo.
4. Dopo il reset, controllare la stessa conversazione e lo stesso transcript,
   il primo turno automatico e gli output prodotti senza invio umano. Annotare
   se un prompt di approvazione ferma correttamente il lavoro.
5. Per ogni Scientist interrotto verificare identità, stato e milestone ripresa.
   Un figlio rimasto terminato per quota è un FAIL anche se l'Orchestrator riparte.
6. Contare riprese/UUID, tool-call e milestone: nessun processo parallelo sulla
   stessa chat, nessun secondo claim e nessuna ripetizione di output già completati.
   Il contratto A.6–A.7 resta il riferimento per il lavoro, non il solo timer.
7. Registrare PASS/FAIL/NOT OBSERVED per ciascuna riga seguente; concludere
   `RIPARTENZA_REALE_VERIFICATA` solo se tutte le condizioni applicabili sono PASS.

| Evento UTC / versione / sessione / Scientist | Attesa armata | Ripresa dopo reset | Stesso ID | No duplicati | Viewer scollegato | Permessi rispettati |
|---|---|---|---|---|---|---|
| PENDENTE | NOT OBSERVED | NOT OBSERVED | NOT OBSERVED | NOT OBSERVED | NOT OBSERVED | NOT OBSERVED |

Usare il log Claude Code già presente e i transcript locali sotto
`~/.claude/projects/-home-desktop-legend-development/`, inclusi i sottoalberi
`<session-id>/subagents/`. Conservare soltanto metadati del collaudo nel rapporto;
non copiare conversazioni o credenziali. Nessun observer automatico è installato.

## Alternativa deterministica: non implementabile nel perimetro dimostrato

Un controllo locale ogni 30 minuti sarebbe economico, ma manca il suo attuatore:
non è stato dimostrato un metodo pubblico supportato per inviare la ripresa a una
precisa conversazione **già aperta nel pannello** senza duplicarla. I comandi
contribuiti dall'estensione includono riapertura e gestione dei tab, non un comando
documentato di ripresa quota della chat attiva. La
[guida VS Code](https://code.claude.com/docs/en/vs-code) descrive cronologia e
interazione utente, non quel contratto di automazione.

Non si deduce da ciò che nessuna futura API possa esistere. L'evidenza oggi è
insufficiente per il requisito imposto dall'operatore: non è stato costruito alcun
daemon, non sono stati usati clic automatici o protocolli interni e non è stato
lanciato `claude --resume` contro una chat viva. Il limite residuo richiede supporto
nativo del pannello o un'interfaccia supportata con identità e deduplicazione;
un timer da solo non lo risolve. Migrare al terminale cambierebbe l'interfaccia
richiesta e non è stato fatto.

## DEFAULTS_TAKEN / DECISIONS_TAKEN / STOP_LOG

- Conservata l'identità di ogni peer e il task HARNESS-SELFTEST-001 già presente;
  nessuna loro modifica inclusa. Registrazione separata, nessun ruolo Orchestrator.
- Scelta la configurazione utente autorizzata, reversibile con false. Nessuna
  alternativa a pagamento o cambio modello/permessi considerata necessaria.
- Nessuna riapertura per applicare la preferenza; watcher osservato e impossibilità
  della GUI documentata. Nessuna promessa di riarmo retroattivo.
- STOP_LOG classe 3: domanda prematura sull'identità, ritirata dopo aver letto la
  mappatura esplicita HARNESS ENGINEERING → plan. Nessuna attesa ha bloccato il lavoro.
- Limite tecnico finale: manca la capacità supportata di ripresa del pannello;
  non è un'attesa di approvazione per costruire un sistema vietato dal perimetro.
- Scout settimanale W37 mancante all'avvio: registrato, non acquisito come nuovo task.

## Session learning e micro-scout

Applicate `legend-capability-scout` e `legend-session-takeaways` in forma tecnica.
Micro-upgrade: procedura riutilizzabile di accettazione con verifica del runtime
effettivo e della topologia padre/figli prima di dichiarare una funzione operativa.
Verdetto AUDIT sulla funzione nativa; nessun componente esterno importato.
Lezione: schema, caricamento configurazione, ammissibilità del runtime e ripartenza
reale sono quattro evidenze distinte. Nessun risultato scientifico prodotto.
