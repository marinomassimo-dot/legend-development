# Riconciliazione dei 54 PMID Aqeilan — 2026-09-09

> **Verificabile, non trascritta.** Ogni colonna è derivata dal ledger, dai manifest, dai contratti di
> task e dalla coda dei candidati. Il generatore è versionato accanto a questo file come
> [`data/2026-09-09_reconcile54.py`](data/2026-09-09_reconcile54.py) e il suo output grezzo come
> [`data/2026-09-09_reconcile54.json`](data/2026-09-09_reconcile54.json). Rieseguire lo script
> rigenera la tabella; nessun valore qui è stato scritto a mano.

## 1 · La contabilità, verificata

| Insieme | Stato ora | Numero |
|---|---|---:|
| 31 esclusi dal dispatch | `complete_fulltext_read` | **31** |
| 23 assegnati | `complete_fulltext_read` | **19** |
| 23 assegnati | `partial_fulltext_read` | **3** |
| 23 assegnati | nessun receipt | **1** |
| | **totale** | **54** |

31 + 19 + 3 + 1 = 54. La dichiarazione regge.

**I 31 non sono stati saltati: sono stati esclusi da un gate che ho riverificato.** Il gate
anti-duplicazione del 2026-09-08 li ha esclusi perché già portatori di un receipt completo, e il
controllo rieseguito oggi conferma che **nessuno dei 31 è privo di lettura completa** — l'esclusione
era corretta, non una svista.

## 2 · Perché 24 receipt non sono 24 paper

Il ledger è passato da 130 a 154 eventi: **24 receipt appesi oggi**. Non corrispondono a 24 letture.

| | |
|---|---:|
| Receipt appesi oggi | 24 |
| di cui su studi della lista dei 54 | 23 |
| di cui su uno studio **fuori lotto** | 1 |
| Studi unici dei 54 toccati oggi | **22** |

Le tre differenze, ciascuna con la sua ragione:

- **Uno studio fuori lista.** `28373548`, la expression of concern su `16223882`, è stata letta come
  fonte a sé e ha quindi obbligato a un receipt: leggere un full text obbliga ad attestarlo. Non è
  uno dei 54 e non è conteggiato fra loro.
- **Uno studio con due receipt.** `31428585` porta `-01` e `-02`, il secondo un
  `receipt_correction` lecito, non una seconda lettura.
- **Uno studio assegnato mai toccato.** `33914858`: la cascata di acquisizione si è esaurita prima di
  qualunque lettura, quindi non esiste receipt e non doveva esistere.

22 studi toccati + 1 fuori lotto = 23 studi unici; 23 studi + 1 correzione = 24 receipt.

## 3 · Disponibilità locale delle superfici

La colonna «Evidenze locali» è misurata da `evidence_presence.py`, e per i 23 assegnati non è stata
misurata separatamente perché le loro superfici sono state riacquisite durante la lettura stessa.

Per i 31 esclusi il numero è netto: **248 artefatti dichiarati, 248 ASSENTI, 0 DIGEST_MISMATCH**.
La causa è strutturale e verificata, non un'omissione: `files/` è in `.gitignore` e
`git ls-files files/` restituisce **0**, quindi nessun byte di evidenza è mai versionato e ogni
checkout nuovo parte senza. Il verdetto del tool stesso è «expected in a fresh checkout».

**Assenza locale non significa lettura mai avvenuta.** Significa che quella lettura, oggi, non è
riverificabile qui senza riacquisire. Le due cose sono tenute separate in tutta questa tabella e
nessuna attestazione è stata modificata per farle coincidere.

## 4 · Tabella per PMID

| PMID | Insieme | Attore | Stato prima | Stato ora | Receipt oggi | Manifest | Dossier | Evidenze locali | Flag drift | Candidati | Integrato |
|---|---|---|---|---|---|---|---|---|---|---:|---|
| `15070730` | 23 assegnati | scientist-a | partial | **complete** | 1 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `16223882` | 23 assegnati | scientist-c | none | **complete** | 1 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `18460020` | 23 assegnati | scientist-c | none | **complete** | 1 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `18674750` | 23 assegnati | scientist-b | partial | **complete** | 1 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `20146584` | 23 assegnati | scientist-b | none | **partial** | 1 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `20530675` | 23 assegnati | scientist-c | partial | **complete** | 1 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `21115974` | 23 assegnati | scientist-c | none | **complete** | 1 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `21731849` | 23 assegnati | scientist-c | none | **complete** | 1 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `24510053` | 23 assegnati | scientist-a | none | **complete** | 1 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `25238781` | 23 assegnati | scientist-b | none | **complete** | 1 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `25245215` | 23 assegnati | scientist-b | none | **complete** | 1 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `25331887` | 23 assegnati | scientist-a | partial | **partial** | 1 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `26499798` | 23 assegnati | scientist-a | none | **complete** | 1 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `27551470` | 23 assegnati | scientist-b | none | **complete** | 1 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `29724996` | 23 assegnati | scientist-b | partial | **complete** | 1 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `30470736` | 23 assegnati | scientist-b | none | **complete** | 1 | si | si | non misurata (nel lotto 23) | - | — | nessun candidato |
| `31428585` | 23 assegnati | scientist-a | none | **complete** | 2 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `33914858` | 23 assegnati | scientist-a | none | **none** | 0 | NO | no | non misurata (nel lotto 23) | - | — | nessun candidato |
| `33916893` | 23 assegnati | scientist-a | partial | **complete** | 1 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `34268881` | 23 assegnati | scientist-a | partial | **partial** | 1 | si | si | non misurata (nel lotto 23) | - | 2 | no - in coda a BATCH_COMMIT |
| `38355659` | 23 assegnati | scientist-c | none | **complete** | 1 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `38499540` | 23 assegnati | scientist-b | partial | **complete** | 1 | si | si | non misurata (nel lotto 23) | - | — | nessun candidato |
| `41562193` | 23 assegnati | scientist-c | partial | **complete** | 1 | si | si | non misurata (nel lotto 23) | - | 1 | no - in coda a BATCH_COMMIT |
| `17360458` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/5 | no | — | nessun candidato |
| `17575124` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/3 | no | — | nessun candidato |
| `18487609` | 31 esclusi | - | complete | **complete** | 0 | si | no | 0/17 | no | — | nessun candidato |
| `18974271` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/6 | no | — | nessun candidato |
| `21318118` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/4 | no | 1 | no - in coda a BATCH_COMMIT |
| `22634283` | 31 esclusi | - | complete | **complete** | 0 | si | no | 0/10 | no | — | nessun candidato |
| `23254685` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/6 | no | — | nessun candidato |
| `23370280` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/8 | no | 1 | no - in coda a BATCH_COMMIT |
| `24550385` | 31 esclusi | - | complete | **complete** | 0 | si | no | 0/9 | SI | — | nessun candidato |
| `24871327` | 31 esclusi | - | complete | **complete** | 0 | si | no | 0/7 | no | — | nessun candidato |
| `25012504` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/17 | no | 1 | no - in coda a BATCH_COMMIT |
| `25491415` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/3 | no | — | nessun candidato |
| `26256646` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/5 | no | — | nessun candidato |
| `26675548` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/18 | no | 1 | no - in coda a BATCH_COMMIT |
| `27308416` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/2 | no | — | nessun candidato |
| `27308504` | 31 esclusi | - | complete | **complete** | 0 | si | no | 0/4 | no | — | nessun candidato |
| `27550453` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/4 | no | 1 | no - in coda a BATCH_COMMIT |
| `30082886` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/4 | no | 1 | no - in coda a BATCH_COMMIT |
| `30370248` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/4 | no | 1 | no - in coda a BATCH_COMMIT |
| `30755385` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/16 | no | — | nessun candidato |
| `31075076` | 31 esclusi | - | complete | **complete** | 0 | si | no | 0/2 | no | — | nessun candidato |
| `32300104` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/5 | no | 1 | no - in coda a BATCH_COMMIT |
| `34634460` | 31 esclusi | - | complete | **complete** | 0 | si | no | 0/7 | no | — | nessun candidato |
| `34747138` | 31 esclusi | - | complete | **complete** | 0 | si | no | 0/10 | no | — | nessun candidato |
| `34831305` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/3 | no | 1 | no - in coda a BATCH_COMMIT |
| `36572673` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/4 | no | 1 | no - in coda a BATCH_COMMIT |
| `38182577` | 31 esclusi | - | complete | **complete** | 0 | si | no | 0/12 | no | — | nessun candidato |
| `41984841` | 31 esclusi | - | complete | **complete** | 0 | si | si | 0/7 | no | 1 | no - in coda a BATCH_COMMIT |
| `42128308` | 31 esclusi | - | complete | **complete** | 0 | si | no | 0/6 | SI | — | nessun candidato |
| `42397075` | 31 esclusi | - | complete | **complete** | 0 | si | no | 0/22 | no | — | nessun candidato |
| `42422765` | 31 esclusi | - | complete | **complete** | 0 | si | no | 0/18 | no | 1 | no - in coda a BATCH_COMMIT |
**Legenda.** «Stato prima» = profondità attestata prima del 2026-09-09. «Evidenze locali» =
artefatti presenti / dichiarati, misurato solo sui 31. «Flag drift» = esito di
`manifest_flag_drift.py`, misurato solo sui 31. «Integrato» = presenza del candidato nei quattro
file current, non nella coda.

## 5 · Anomalie rilevate dall'audit meccanico sui 31

| PMID | Anomalia | Natura |
|---|---|---|
| `24550385` | `multihop.performed: false -> true` senza nota nello stesso edit | advisory: una domanda, non un'accusa |
| `42128308` | `multihop.performed: false -> true` con nota nello stesso edit | advisory; se la nota riguardi il flag lo giudica un lettore |

29 dei 31 passano senza rilievi. **Il verde meccanico non è prova di correttezza scientifica**: dice
che i flag dichiarati non sono migliorati senza traccia di lavoro, e nient'altro.

## 6 · Stato d'integrazione

**33 commit candidate** esistono sui 54 PMID. Nessuno è integrato: i quattro file scientifici current
si muovono solo attraverso `BATCH_COMMIT`, che non era ancora stato eseguito al momento di questa
riconciliazione. «In coda» e «integrato» restano colonne distinte proprio per non confonderli.
