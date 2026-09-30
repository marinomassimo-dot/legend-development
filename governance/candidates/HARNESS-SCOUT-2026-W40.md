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
| 9 | ToolUniverse (mims-harvard) | https://github.com/mims-harvard/ToolUniverse | Il livello di **lookup live** che a LEGEND manca: il README dichiara più di 1000 tool (UniProt, openFDA, Open Targets, PubMed, Europe PMC, bioRxiv, Semantic Scholar più modelli ML), esposti come server MCP, plugin di Claude Code, SDK Python e CLI `tu`, con un Compact Mode che riduce il catalogo a 4-5 tool di scoperta. Oggi quasi tutto il `_external_repos/MANIFEST.md` è DESCRIBED, cioè instradato ma non richiamabile: gli unici lookup di database dal vivo sono PubMed/Scholar (connettori claude.ai) e `kg_thin_slice.py` (Monarch + DGIdb) | 4 (TRIAL: MCP via `uvx tooluniverse` in Compact Mode, 10 lookup WWOX a livello di gene, output instradato come IPOTESI secondo le regole del MANIFEST, voce MANIFEST con pin) | Apache-2.0; alcuni provider richiedono chiavi proprie | Contesto: 1000 tool senza Compact Mode. Rete: solo query su gene, allele o molecola pubblici, mai l'overlay privato. Un risultato di tool non è una lettura (`gold_is_in_the_details`). Installarlo come plugin tocca `.claude/`, che richiede l'autorizzazione dell'operatore. `uvx` c'è già; il modulo non è installato | TRIAL | |
| 10 | Open-Rosalind (maris205) | https://github.com/maris205/open-rosalind | 21 wrapper di skill (UniProt, ClinVar, gnomAD, STRING, ChEMBL, Open Targets, GWAS Catalog, HPA, Bgee, PDB, PharmGKB, BLAST, PubChem, BindingDB, CIViC, EFO…) dentro un agente proprio con planner a template fissi, UI React, SQLite e log JSONL. Tutte le sorgenti le copre già la riga 9; l'agente e la UI duplicano Claude Code. L'unica idea portabile, "fatti solo dai tool registrati, ogni chiamata in una traccia JSONL", LEGEND ce l'ha già con le receipt | 0 | MIT | 12 stelle, un solo maintainer. Richiede OpenRouter. Online per quasi tutte le skill | REJECT | |
| 11 | Claude Science (Anthropic, beta dal 2026-06-30) | https://www.anthropic.com/news/claude-science-ai-workbench | App separata, **non Claude Code**, chiusa: più di 60 skill e connettori (nominati: UniProt, PDB, Ensembl, Reactome, ClinVar, ChEMBL, GEO, PubMed), modelli NVIDIA BioNeMo (Evo 2, Boltz-2, OpenFold3), rendering 3D di strutture e tracce genomiche, calcolo su SSH/HPC o Modal, artefatti riproducibili con codice, ambiente e cronologia, un reviewer agent su citazioni e calcoli. Non si integra nel harness. Serve all'operatore come banco di calcolo (struttura e varianti) su input pubblici, con il risultato che rientra in LEGEND come IPOTESI | 0 harness; 1-2 per una prova dell'operatore | proprietaria, inclusa nei piani Pro, Max, Team ed Enterprise (beta) | Il calcolo su Modal può essere a pagamento. Nessun input dall'overlay privato. I suoi artefatti non sono receipt LEGEND | WATCH | |
| 12 | Connettori claude.ai Life Sciences già presenti ma non autorizzati | connettori claude.ai della sessione (Clinical Trials, bioRxiv, Synapse) | Tre connettori sono già elencati in questa sessione ma aspettano l'OAuth. bioRxiv copre i preprint (oggi `find-fulltext` e wwox-scout lo raggiungono solo via web), Clinical Trials serve al tracker terapeutico | 0,5 (autorizzazione dell'operatore dalle impostazioni dei connettori claude.ai) | termini del servizio | Nessuno nuovo: stessi confini di privacy di PubMed | ADOPT | |
| 13 | DisMech: schema #7439 (direzione separata dalla directness) | https://github.com/monarch-initiative/dismech | Upstream ha **rimosso `PARTIAL` e `WRONG_STATEMENT`**: `EvidenceItemSupportEnum` ora vale solo SUPPORT, REFUTE o NO_EVIDENCE, e c'è un nuovo slot `directness` (DIRECT, INDIRECT, UNKNOWN). Verificato sul `dismech.yaml` di `main` il 2026-09-28. `disease-models/wwox/analysis/dismech_export_spec.md` mappa ancora DATO-indiretto e INFERENZA su `PARTIAL` (righe 318-319) e cita `WRONG_STATEMENT`. La directness di LEGEND ha finalmente un campo di destinazione nativo | 5 (ri-pin, diff della spec, crosswalk v3) | BSD-3-Clause | Lo schema upstream si muove ogni settimana (quattro commit di schema dal 17 al 28 settembre): pin esplicito obbligatorio. Nessun dato esce | ADOPT | |
| 14 | DisMech: hook PreToolUse "simula l'edit → valida → exit 2" | https://github.com/monarch-initiative/dismech (`.claude/hooks/validate_disorder_hook.py`) | Il pattern di guardia prima dell'edit, instradato al worktree che si sta davvero modificando e non al checkout principale. Candidato per le modifiche ai file canonici | 4 | BSD-3-Clause | Scrive sotto `.claude/`, quindi serve l'autorizzazione dell'operatore. Da confrontare con la guard esistente prima di adottarlo, perché potrebbe essere un doppione. Il dettaglio viene da un report di subagent e non l'ho letto io | WATCH | |
| 15 | ARA: `trace/exploration_tree.yaml` | https://github.com/ARA-Labs/Agent-Native-Research-Artifact | Un grafo del percorso di ricerca con i vicoli ciechi e le piste non ancora provate. Chiude la domanda della riga 7 (traiettorie) senza bisogno di uno store nuovo, se diventa un campo del ledger di discovery che c'è già. Il suo `research-fuzzer` (predizione prima dell'azione, auto-confutazione) è già coperto da `preregister_prediction` | 6 | MIT | Rischio di due fonti di verità in competizione con claim e receipt. L'installer npx scrive in `.claude/`: va portato a mano | TRIAL | |
| 16 | Autoresearch: declassamento automatico con CI e `min_effect` | https://github.com/hugoferreira/autoresearch | In `legend-research-loop`: bootstrap BCa al 95% con seed, confronto con il baseline originale e con il miglior baseline precedente, e un "supported" che scende da solo a INCONCLUSIVE se il CI attraversa lo zero o l'effetto è sotto il `min_effect` preregistrato | 4 (clean-room in Python) | **nessuna licenza**: si prende l'idea, non il codice | Si applica solo agli esperimenti di harness misurabili, non alla scienza | TRIAL | |
| 17 | Gemma curation agents: dismiss-rate per giudice e per categoria | https://github.com/PavlidisLab/gemma-curation-agents-v1.1 | La precisione di Mirror misurata dalle disposizioni che l'operatore o lo Scientist danno ai suoi rilievi. Serve alla parte "misurare la qualità della review" | 4 | Apache-2.0 (il file LICENSE; l'API riporta NOASSERTION) | Da verificare prima: i record Mirror hanno un campo di disposizione? Se no, cresce il costo | TRIAL | |
| 18 | BioDSA: `biodsa/tools/` (Open Targets, HPO, STRING, Reactome, ChEMBL, UniProt, GO, HPA, openFDA…) | https://github.com/RyanWangZf/BioDSA | Wrapper Python standalone su API pubbliche: è l'alternativa alla riga 9 per i lookup live. La takeaway 25 del design record (§129) preferisce l'architettura sottile di ToolUniverse | 8 | MIT | Doppione della riga 9: solo uno dei due. L'autenticazione per servizio non è documentata e UMLS vuole una licenza | WATCH | |
| 19 | scholar-loop: calibrazione per agente (`CalibrationLog`) | https://github.com/renee-jia/scholar-loop | Punteggiare più tardi ogni predizione contro l'esito e restituire all'agente la fiducia accumulata. Si somma al backtest della riga 2, che fornisce proprio gli esiti | 8 | MIT | Nella biologia rara la verità arriva lenta o non arriva: il segnale sarebbe scarso. Si valuta dopo il TRIAL della riga 2 | WATCH | |
| 20 | K-Dense scientific-agent-skills: `database-lookup` | https://github.com/K-Dense-AI/scientific-agent-skills | Una skill fatta di circa 90 file di riferimento, senza codice, che copre quasi tutti i buchi di lookup: gnomAD (GraphQL, senza chiave), ClinVar, UniProt, Open Targets, STRING, GTEx, ChEMBL, AlphaFold/AlphaMissense, PDB, Ensembl/VEP, ClinicalTrials, openFDA, Reactome, HPO, Monarch, LINCS L1000. **È la terza candidata per lo stesso buco, dopo le righe 9 e 18: la si decide con un solo confronto** (vedi Top 3 aggiornato). Non copre SpliceAI | 8 (vendorizzare circa 14 file di riferimento con attribuzione MIT e una skill wrapper) | MIT a livello di repo; alcune skill dichiarano licenze proprie (bioservices GPLv3, primekg "Unknown") | Sono ricette in prosa, non client testati: le API cambiano e i file si datano. Installare l'intero plugin aggiungerebbe 166 skill in concorrenza di attivazione con quelle di LEGEND. Solo query per classe di genotipo, mai individuali | TRIAL | |
| 21 | K-Dense `database-lookup/retrieval-contract.md` | https://github.com/K-Dense-AI/scientific-agent-skills | Una checklist di provenienza per ogni lookup: entità, identificatore, build e versione; conteggio prima di paginare; log di ogni pagina; confronto tra atteso e ottenuto; stop oltre 10.000 record o 100 chiamate. Serve **qualunque backend si scelga fra le righe 9, 18 e 20** ed è coerente con `DATA_SOURCES.md` e con il divieto di ricostruire dalla memoria | 2 | MIT | Nessuno; è un testo di regole | ADOPT | |
| 22 | K-Dense skill `alphagenome` | https://github.com/K-Dense-AI/scientific-agent-skills | Punteggio di splicing ed effetto delle varianti (tracce di splicing, Atlas precalcolato): è l'unico candidato di calcolo per una domanda su un allele di splicing | 3 | Chiave DeepMind gratuita ma **non commerciale**: la compatibilità con gli output in un repo pubblico non è verificata | La sequenza di riferimento esce verso DeepMind (è pubblica, ma resta traffico esterno). Solo GRCh38 | WATCH | |
| 23 | Rubrica K-Bench (arXiv 2608.21601) | https://arxiv.org/abs/2608.21601 | 8 dimensioni da 0 a 10, fra cui `honesty_calibration`, con un tag di **overclaiming** (applicato al 31,4% delle valutazioni) e il confronto fra lavoro dichiarato e lavoro consegnato sull'albero degli artefatti. I task sono privati: si prende solo la rubrica. È un'estensione di `legend-session-self-eval` / `legend-research-loop` | 4 | CC BY 4.0 | Giudice LLM senza calibrazione umana: serve un piccolo set valutato dall'operatore. L'auto-preferenza dei giudici è documentata (+0,83) | TRIAL | |
| 24 | AutoSciRub (zjunlp) | https://github.com/zjunlp/AutoSciRub | La rubrica **eseguibile**: ogni criterio dichiara dati, analisi, artefatti attesi e condizione di soddisfazione, più una lista `claims_to_avoid`; la verifica è binaria contro gli artefatti e `all_satisfied` non può valere se manca un input. Esplicito: un esito negativo o inconclusivo può soddisfare una domanda ben posta. Si innesta nel critique di `legend-hypothesis-forge`. Funziona offline con Claude Code come host | 8 (lo schema dei criteri nel critique, più un A/B di research-loop contro la rubrica a 5 criteri) | MIT | Nessun accordo con valutatori umani: il paper usa giudici LLM. Il guadagno viene soprattutto dal ciclo di revisione. L'installer scrive in `~/.claude/skills`, fuori dal test del catalogo: si copia il pattern | TRIAL | |
| 25 | reef-eval (Human-Agent-Society) | https://github.com/Human-Agent-Society/reef-eval | **Isolamento del giudice**: il riferimento nascosto sta fuori dal contenitore dell'agente, `grade()` è deterministico e ricalcola tutto dal file consegnato, c'è un budget di consegne. Più le metriche `transfer` e `forgetting`. È esattamente la struttura che serve al backtest T0/T1 della riga 2, dove i paper successivi a T0 fanno da riferimento nascosto | +6 sulla riga 2 (porting in stile `--local` in `framework/eval/benchmarks`) | Apache-2.0 | 26 stelle, fermo dal 2026-08-31. Un giudice deterministico premia il ritrovare fatti noti, non la scoperta | TRIAL | |
| 26 | reef (Human-Agent-Society) | https://github.com/Human-Agent-Society/reef | Una piattaforma di self-improvement (serve → observe → grow → commit) che assorbe CORAL come ricetta beta. L'idea portabile è il formato del report di esito (`score`, `feedback`, `references` alle receipt di interazione) per i verdetti di research-loop | 3 (solo la convenzione) | Apache-2.0 | 4 settimane di vita. Ogni ricetta vuole un valutatore scalare, che per la scienza manca. L'harness che si auto-modifica è in conflitto con la governance | WATCH | |
| 27 | ARK (mims-harvard) | https://github.com/mims-harvard/ark | Due tool locali, ricerca BM25 globale e espansione del vicinato a 1 hop filtrata per tipo di nodo e arco, con Claude Code come esploratore. Ricostruiti su PrimeKG, che è già nel MANIFEST come DESCRIBED, danno percorsi multi-hop WWOX → pathway → farmaci → fenotipi senza spesa, come semi per `legend-hypothesis-forge` | 10 (ricostruito dal paper, non dal codice) | README "MIT", ma **nessun file LICENSE** e l'API riporta null; la licenza dei dati PrimeKG non è verificata | Fermo da aprile. Gli archi di un knowledge graph sono una nuova classe di evidenza e vanno classificati. È un risultato da benchmark (STaRK-PRIME) | TRIAL | |
| 28 | SkillNet + SkillNet-Fabric (zjunlp) | https://github.com/zjunlp/SkillNet | Relazioni tipizzate fra skill (`compose_with`, `similar_to`) e un contratto per ogni skill (capacità, input, output, condizioni d'uso). Il dato di Fabric: una shortlist locale batte il catalogo completo | 4 | MIT | Valutazione e analisi usano endpoint a pagamento; il servizio ospitato è su http in chiaro. I risultati valgono per 500-79.000 skill, mentre LEGEND ne ha circa 22 | WATCH | |
| 29 | k-dense-byok ("Kady") | https://github.com/K-Dense-AI/k-dense-byok | App desktop co-scientist, un runtime parallelo e concorrente di Claude Code. Da leggere solo i documenti su lab notebook, provenance ed evidence packages come riferimento per il ledger delle ipotesi | 2 (lettura e nota di design) | MIT | Il secondo posto su CompBioBench è autodichiarato. È in beta e i percorsi di default sono a pagamento | WATCH | |
| 30 | K-Dense scientific-agents (503 profili) | https://github.com/K-Dense-AI/scientific-agents | I profili `rna-biologist` e `medical-geneticist` come personaggi critici nel critique di forge | 3 | MIT | Prompt di personaggio generici che possono annacquare i file normativi di LEGEND; non vanno mai usati come AGENTS.md di radice | WATCH | |
| 31 | Claude Code 2.1.221 → 2.1.284 (08-04 → 09-28) | https://github.com/anthropics/claude-code | Controlli già fatti: la versione sull'host è 2.1.284 (≥2.1.246, il fix della sweep che cancellava i worktree in `.claude/worktrees/`); `TaskOutput`, rimosso, non compare in nessun file. **Aperti:** (a) dalla 2.1.284 le sessioni interattive partono in auto mode se non si configura nulla, e le settings di progetto sono `{}`, quindi va deciso se fissare `defaultMode` nelle settings utente (**decisione dell'operatore**); (b) `omitClaudeMd` per gli agenti in sola lettura (fulltext-dossier, legend-deepdive); (c) ritestare il pin del modello dei subagent (2.1.251, più `CLAUDE_CODE_SUBAGENT_MODEL_FORCE`) contro la nota di memoria; (d) `notify_when_idle` al posto del polling negli handoff; (e) `/skill-doctor` e `/doctor prompt-audit` una volta come audit | 5 | proprietario | Il report viene da un subagent che ha letto il CHANGELOG; ho verificato io solo i punti già marcati come controllati. Le impostazioni non si toccano senza l'operatore | ADOPT | |
| 32 | Codex rust-v0.146.1 → 0.158.0 (08-05 → 09-28) | https://github.com/openai/codex | Da controllare sull'host Codex (qui non è installato): (a) dalla 0.150 **i progetti non trusted non caricano l'AGENTS.md di progetto**, e un worktree non trusted girerebbe senza AGENTS.md senza avvisare; (b) i worktree gestiti da Codex sono attivi di default dalla 0.156 e potrebbero collidere con il layout di LEGEND; (c) `codex exec --full-auto` è stato rimosso: il caso M-03 del guard (`CAND-20260829-RTBRIDGE9.md`) deve riconoscere anche `--sandbox workspace-write`; (d) il planning tool è disattivato di default dalla 0.152; (e) il budget del catalogo skill (0.149) può troncare la lista: va rilanciato lo script di parità | 4 | Apache-2.0 | Un AGENTS.md che manca in silenzio è il rischio più alto della tornata | ADOPT | |

## Top 3 for this week

Queste priorità sono state consolidate dopo 4 tornate e dopo il censimento delle
implementazioni (§ in fondo). Il criterio è l'ordine di valore diviso per costo; la verifica
che rompe viene prima di ciò che aggiunge.

1. **Controllo di rottura del runtime (righe 31 e 32), circa 5 h, prima di tutto.** Il rischio
   più alto emerso è Codex 0.150+: un worktree non trusted perde l'AGENTS.md senza avvisare. Poi
   il guard M-03 per `--sandbox workspace-write` e la decisione dell'operatore su `defaultMode`,
   perché dalla 2.1.284 l'auto mode è il default.
2. **Lookup live: un confronto, non tre adozioni (righe 9, 18, 20, più la 21 da adottare
   comunque), circa 8 h.** Si prendono le stesse 10 query WWOX a livello di gene (gnomAD,
   ClinVar, UniProt, Open Targets, STRING, GTEx, ChEMBL…) e le si fanno girare su ToolUniverse
   (MCP, Compact Mode) e su `database-lookup` di K-Dense (le ricette). Si punteggiano per
   risposta corretta, provenienza completa secondo `retrieval-contract` (riga 21) e costo di
   contesto. Ne vince uno; BioDSA resta la riserva. L'output entra come IPOTESI. ARK su PrimeKG
   (riga 27) viene dopo, come secondo livello multi-hop.
3. **Misurare la discovery (righe 1, 2, 23, 24, 25): un solo banco di prova, non cinque.**
   - **Backtest T0/T1 (riga 2) con il giudice isolato di reef-eval (riga 25).** T0 va scelto
     **dopo il cutoff di training del modello**. I paper di data > T0 già letti fanno da
     riferimento nascosto. Il punteggio lo dà un `grade()` deterministico fuori dal contesto
     dell'agente.
   - **Run di controllo Static contro Active (riga 1)** su un nodo WWOX maturo (il radar propone
     oligodendrociti/mielina), con i quattro test della riga 6 e il baseline `copy`. Mirror
     punteggia in cieco rispetto al braccio. È il controllo negativo che
     `legend-discovery-method` § 4 dichiara ancora dovuto. **Tocca il perimetro dello
     Scientist:** chi lo esegue va deciso al triage.
   - **Giudice (righe 23 e 24):** la rubrica eseguibile di AutoSciRub contro la rubrica a 5
     criteri di forge, in un A/B di research-loop, con il tag di overclaiming di K-Bench. Prima
     serve un piccolo set di calibrazione valutato dall'operatore.

Economici e indipendenti, da infilare dove c'è spazio:
- **DisMech #7439 (riga 13, ADOPT, 5 h)**: la spec di export è già sbagliata rispetto a upstream.
- **Campo lineage delle ipotesi in forge (2-3 h, dal censimento)**: è la versione minima
  dell'albero di MC-NEST, ARA e AI-Scientist-v2 (righe 5 e 15).
- **`tool_preflight.py --require` (4 h, dal censimento)**: una capacità mancante dichiarata come
  BLOCKED o DEGRADED prima di iniziare una lettura, non scoperta a metà.
- **Audit delle traiettorie di ricerca (riga 7, 2 h)** prima di qualsiasi costruzione.

## Tornata 2 — cosa hanno in più rispetto a LEGEND (2026-09-28)

LEGEND è più forte sul metodo (epistemica, receipt, parità delle fonti, discovery) e più debole
sui lookup strutturati in tempo reale e sul calcolo. Il MANIFEST instrada molti strumenti, ma
quasi tutti sono DESCRIBED, cioè nessuna sessione li può chiamare. `tool_preflight.py` verifica
solo gli estrattori PDF.

| Capacità | LEGEND oggi | ToolUniverse | Open-Rosalind | Claude Science |
|---|---|---|---|---|
| Varianti (ClinVar, gnomAD) | ClinVar DESCRIBED, nessun lookup live | da verificare | sì | ClinVar |
| Proteina (UniProt, PDB, AlphaFold) | AlphaFold DB DESCRIBED | UniProt nominato | UniProt, PDB | UniProt, PDB, OpenFold3, Boltz-2 |
| Target e malattia (Open Targets) | no | sì | sì | non nominato |
| Interazioni ed espressione (STRING, HPA, GTEx, Bgee) | GTEx DESCRIBED | da verificare | STRING, HPA, Bgee | GEO, Reactome |
| Farmaci e sicurezza (ChEMBL, PubChem, openFDA) | DGIdb via `kg_thin_slice.py`; ADMET-AI DESCRIBED | openFDA nominato | ChEMBL, PubChem, BindingDB, PharmGKB | ChEMBL |
| Trial clinici | connettore claude.ai non autorizzato | da verificare | sì | non nominato |
| Letteratura | PubMed + Scholar MCP, cascata full-text, PaperQA | PubMed, Europe PMC, bioRxiv, S2 | PubMed | PubMed |
| Calcolo (struttura, genomica, docking) | ESM/ThermoMPNN DESCRIBED, nessuna GPU | modelli ML dichiarati, non enumerati | BLAST | BioNeMo + Modal/HPC |
| Visualizzazione 3D e tracce genomiche | no | no | no | sì |
| Epistemica, receipt, parità delle fonti | **sì, e solo LEGEND** | no | log JSONL | reviewer agent su citazioni e calcoli |

"da verificare" significa che il README non lo nomina; si controlla nel TRIAL della riga 9.

## Tornata 4 — K-Dense, reef, ZJUNLP, ARK, runtime Claude Code / Codex (righe 20-32)

Questa tornata coincide per intero con la **coda post-Tier-1** che l'operatore ha confermato
nella tornata 5: Claude Code → Codex → Reef → reef-eval → AutoSciRub → SkillNet →
SkillNet-Fabric → ARK → K-Dense BYOK → Scientific Agents → Scientific Agent Skills, più K-Bench
come benchmark trasversale. La coda è chiusa. I nomi del longlist di mining (ContinuumCellAgent,
Orion, SpatialDataAgent, HGNet, MedLog, bio-posttrain, Flowcept/PROV-AGENT, BioRouter,
EurekAgent, M3A, BiomniBench, BioDesignBench, MatClaw, NIMO) **non** sono stati promossi e qui
non sono censiti; Open-Rosalind è stato visto a parte (riga 10).
CORAL, AutoScientists e ToolUniverse sono già coperti dalle tornate 1-3. K-Bench non ha un
repo: se ne prende solo la rubrica (riga 23). SpliceAI non c'è in nessuna delle librerie di
skill guardate; per lo splicing l'unico candidato è `alphagenome` (riga 22).

## Tornata 3 — le 18 repo Tier-1: sono già state lette tutte

L'elenco incollato dall'operatore corrisponde, nello stesso ordine, alle **Review 01-18** di
[`governance/design_records/sviluppo_lettori.md`](../design_records/sviluppo_lettori.md),
archiviate il 2026-09-11: 10.612 righe, con le 25 takeaway del § 129. Non si ri-scoutano da capo.
Questa tornata ha fatto due sole cose: cercare **delta upstream** dopo le review e **pattern
concreti** da portare nel harness che non fossero ancora nella tabella. Il risultato sono le
righe 13-19. Sulla base del README, per le altre non c'è delta:

- Robin (Review 01), AutoScientists (02, **senza licenza**), ATHENA (07, modello da 8B su GPU; la parte utile è ToolUniverse, riga 9), Medea (09, LLM a pagamento; MedeaDB contiene trascrittomi di pazienti).
- CORAL (05, serve un grader calcolabile che la scienza di LEGEND non ha; si riapre dopo il TRIAL della riga 2).
- Paperclip (06, runtime già rifiutato in `GOVERNANCE_v3.1.1.md` e `prior_art_review_v3.1.md`).
- ARIS (08: il reviewer cross-model è a pagamento; la regola "si scarta un'idea solo nominando il paper che la contiene già" è coperta da `enumerate_baseline_before_scoring`).
- ResearchOS (12, 0 stelle, 4 commit), llm4xray (13, fuori dominio), AI-Scientist-v2 (14, licenza custom, GPU, 15-20 $ a run, fermo dal 2025-12), OpenScientist (15, solo provider a pagamento).

🔴 **La domanda più utile per il prossimo intervento non è quale repo leggere, ma quali dei
pattern marcati `ADOPT CANDIDATE` nel design record siano già implementati.** Il § 121
(BioDSA) e il § 124 (Autoresearch) da soli ne elencano più di 15: capability allowlist per
task, token telemetry, fail-to-INCONCLUSIVE, fresh independent gate reviewer, frozen brief,
content-addressed raw artifacts… Un censimento "candidato → implementato sì/no, dove" costa
circa 3 h ed è il vero backlog del harness.

## Censimento: pattern del design record e ciò che LEGEND ha davvero (2026-09-28)

Il design record [`sviluppo_lettori.md`](../design_records/sviluppo_lettori.md) contiene circa
150 righe classificate ADOPT, VERY STRONG o CRITICAL BUILD, che si riducono a circa 40 pattern
distinti. Letture fatte da un subagent in sola lettura; i giudizi marcati "uncertain" poggiano
solo su header e `git grep`. `roles/plan.md` dice che il record non vincola nessun attore.

- **Già implementati (circa 22):** completezza deterministica del full-text, grounding
  verbatim e dei numeri, reviewer fresco e cieco, memoria dei vicoli ciechi e dei negativi,
  catena di validazione non aggirabile, resume fail-closed, supersede senza sovrascrivere,
  disclosure progressiva delle capacità, discovery distinta dalla lettura del corpus,
  INCONCLUSIVE di prima classe, frozen brief, read model derivato distinto dal truth store,
  ammissione dell'evidenza prima del riuso, anti-duplicazione, freschezza degli artefatti,
  lettura senza troncamenti.
- **Parziali (circa 14)**, da colmare in ordine di valore/costo:
  - lineage delle ipotesi (2-3 h);
  - hand-back strutturato dei subagent e normalizzazione dei transcript (4-6 h);
  - health gate delle capacità (4 h);
  - denominatore di figure e tabelle (6-10 h; è l'ultimo CRITICAL BUILD sulla completezza);
  - capability allowlist per task (3 h);
  - token-normalized yield (3-4 h);
  - artefatti content-addressed (4-8 h).
  Polarità e tipizzazione della fonte aspettano l'adozione di `scientist_evidence_standard.md`
  (DRAFT). La separazione fra modello corrente e storia aspetta la decisione dell'operatore
  (`harness_cost_20260928.md` § 9).
- **Non implementati:** una catena deterministica di risoluzione ontologica (8-12 h), il
  batching cross-item (basso valore), la sintesi gerarchica con provenienza (prematura a questa
  scala), e soprattutto la **semantica READY/CLAIMED/STALE sulla coda** (16-30 h). È il
  CRITICAL BUILD più ripetuto nelle 18 review; A.3 e J.0 ammettono che manca un checkout
  atomico. Serve quando la lettura diventa parallela.
- **Rifiutato in seguito:** supervisor deterministico con heartbeat
  (`prior_art_review_v3.1.md`, `GOVERNANCE` § 34).

## Watch-list carried forward

| candidate | first seen | why still WATCH |
|---|---|---|
| TruthInsightBench | 2026-09-28 | Il judge richiede un endpoint pagato o ospitato; nessun task biomedico confermato; si riapre quando il repo elenca i domini |
| ResearchBench | 2026-09-28 | Il sottoinsieme retrieval-only è economico, ma nessuna domanda di LEGEND ne ha ancora bisogno; si riapre se `connect_domains` va misurato |
| MC-NEST | 2026-09-28 | Il pattern è coperto da forge e discovery-method; si riapre solo se il TRIAL 1 mostra che le ipotesi vengono potate prima di essere raffinate |
| Apprendimento dalle traiettorie di ricerca | 2026-09-28 | Dipende dall'audit del Top 3 n. 3 |
| Ecosistema MIMS Harvard / Zitnik | carried (dal radar) | ToolUniverse è alla riga 9 (TRIAL); ATHENA, AutoScientists e Medea sono già stati letti (Review 07, 02, 09) e non hanno delta: si chiude come ecosistema |
| alphagenome (K-Dense) | 2026-09-28 | Si riapre quando i termini non commerciali della chiave DeepMind risultano compatibili con gli output in un repo pubblico |
| reef, SkillNet/Fabric, k-dense-byok, scientific-agents | 2026-09-28 | reef: si riapre quando CORAL TTT o GEPA pubblicano risultati riproducibili. SkillNet: oltre 50-100 skill. byok e profili: solo come letture di riferimento |
| Claude Science | 2026-09-28 | App chiusa, fuori dal harness; si riapre se espone skill o connettori riusabili in Claude Code |

## Looked at and rejected (one line each)

- La fase obbligatoria "DIVERGE → PREDICT → DISCRIMINATE" — duplica quattro primitive esistenti e diventerebbe un gate (§26). Il suo disegno di valutazione viene tenuto (Top 3 n. 1).
- Il codice MC-NEST — nessuna licenza, API GPT-4, fermo da un anno.
- Open-Rosalind — i suoi 21 wrapper sono un sottoinsieme della riga 9; l'agente e la UI duplicano Claude Code.

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
