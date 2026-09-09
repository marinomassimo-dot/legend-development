# Inventario di trasferimento — root → desktop, stessa VPS

**La migrazione non attraversa la rete.** Cambia l'utente Linux sulla stessa macchina, quindi il
problema non è la copia ma **proprietà e permessi**: tutto ciò che segue appartiene oggi a `root`,
e parte è in `/tmp`, che il riavvio cancella.

Generato da
[`data/2026-09-09_migration_manifest.py`](data/2026-09-09_migration_manifest.py); il manifest per
file, con byte e SHA-256, è in
[`data/2026-09-09_transfer_manifest.jsonl`](data/2026-09-09_transfer_manifest.jsonl) — **837 voci,
245.688.191 byte (234,3 MiB)**. Nessun percorso qui è abbreviato.

## 1 · Indispensabile — nulla lo riproduce

| Gruppo | Percorso assoluto | File | Byte |
|---|---|---:|---:|
| Evidenze | `/root/legend-development/files` | 249 | 107.951.245 |
| Trascrizioni | `/root/.claude/projects/-root-legend-development` | 140 | 131.963.079 |
| Plugin Claude Code | `/root/.claude/plugins` | 447 | 5.773.812 |
| Impostazioni Claude Code | `/root/.claude/settings.json` | 1 | 55 |

**Evidenze** — `files/` è in `.gitignore` per copyright e `git ls-files files/` restituisce 0. Senza,
ogni manifest riporta artefatti ASSENTI e nessuna lettura passata è riverificabile localmente. Le
letture restano valide e attestate: è la loro *riverificabilità* che si azzera.

**Trascrizioni** — sono la dipendenza necessaria alla ripresa delle sessioni, e stanno fuori dalla
cartella di progetto. Contengono cascate tentate, vie rifiutate e ragioni delle decisioni: nulla le
ricostruisce. Il nome della directory codifica il percorso del progetto (`-root-legend-development`):
se il progetto cambia percorso sotto l'utente desktop, la nuova sessione **non le troverà** e vanno
rinominate di conseguenza.

**Plugin e impostazioni** — dipendenze di ripresa fuori progetto. Le skill del progetto stanno invece
dentro il repository (`/root/legend-development/.claude/skills`) e arrivano con il clone.

## 2 · Ricostruibile — non copiare

| Gruppo | Percorso assoluto | File | Byte |
|---|---|---:|---:|
| Scratchpad di sessione | `/tmp/claude-0/-root-legend-development/3e1bc608-80c5-4c1c-a5a3-3c4da9b68c75` | 824 | 285.873.323 |

272,6 MiB, e sono **derivati**: 322 PNG di ritagli e render, 85 JSON, 79 txt, 45 XML, 29 PDF — tutti
riproducibili dalle evidenze. Le tre cose che *non* lo erano sono già state messe in salvo:

- **Il verbale d'audit cieco** su PMID 25331887 è in
  `/root/legend-development/disease-models/wwox/research/locator_audits/2026-09-09_PMID25331887_SI_blind_audit.md`,
  **verificato byte-identico** all'originale nello scratchpad (SHA-256
  `26426d8d921197aee5c92afba8bf8912c5091fd163ffc88752a2e9c8535e0732`).
- **I JSON degli eventi receipt** sono stati appesi al ledger e vivono lì.
- **`legend_commit.sh`** è ricreabile: il brief permanente ne prescrive la ricostruzione a ogni
  ripresa e ne descrive il contenuto.

Il worktree ausiliario `/tmp/legend-startup-context-audit` è pulito e il suo commit è su `main`: non
contiene nulla di unico.

## 3 · Da NON copiare — credenziali

| Percorso assoluto | Byte | Perché |
|---|---:|---|
| `/root/.claude/.credentials.json` | 566 | Credenziale dell'utente `root`. **L'utente desktop si autentica da sé**; copiarla trasferirebbe un segreto invece di un accesso |
| `/root/.claude.json` | 51.119 | Stato del CLI legato all'account e alla macchina, con cronologia e percorsi. Si rigenera al primo avvio |

Il manifest non calcola l'hash di questi due, deliberatamente. **Nel repository non c'è alcuna
credenziale**, e l'accesso a GitHub è via chiave SSH dell'utente: l'utente desktop dovrà avere la
propria chiave registrata, oppure riusare quella di sistema.

## 4 · Sequenza per lo stesso host

```bash
# come root, dopo aver creato l'utente desktop
install -d -o desktop -g desktop /home/desktop/legend-development
cp -a  /root/legend-development/.           /home/desktop/legend-development/
cp -a  /root/.claude/projects/-root-legend-development \
       /home/desktop/.claude/projects/-home-desktop-legend-development
cp -a  /root/.claude/plugins /root/.claude/settings.json  /home/desktop/.claude/
chown -R desktop:desktop /home/desktop/legend-development /home/desktop/.claude
```

`cp -a` conserva mtime e permessi; `chown` è il passaggio che rende davvero la migrazione. La
directory delle trascrizioni **va rinominata** al nuovo percorso di progetto, altrimenti la ripresa
non le trova.

Poi, come utente desktop:

```bash
python3 -m pip install --break-system-packages pymupdf numpy
python3 framework/scripts/tool_preflight.py      # deve riportare 6/6
python3 framework/scripts/fulltext_receipts.py verify
python3 framework/scripts/evidence_presence.py --disease wwox | tail -1
```

L'ultimo comando è la verifica che il trasferimento delle evidenze è riuscito: prima della copia
riporterebbe assenza totale.

## 5 · Verifica del trasferimento

Il manifest porta un SHA-256 per file, quindi la copia si verifica invece di darla per riuscita:

```bash
python3 - <<'PY'
import hashlib, json
from pathlib import Path
SRC, DST = "/root", "/home/desktop"
bad = 0
for line in open("disease-models/wwox/analysis/orchestration_reviews/data/2026-09-09_transfer_manifest.jsonl"):
    r = json.loads(line)
    p = Path(r["path"].replace(SRC, DST, 1))
    if not p.exists():
        print("MANCANTE", p); bad += 1; continue
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    if h != r["sha256"]:
        print("DIVERSO ", p); bad += 1
print("difformita':", bad)
PY
```

Zero difformità su 837 voci significa trasferimento completo e integro. Qualunque altro numero
nomina esattamente i file da ricopiare.

---

## 6 · Ripresa delle trascrizioni — la rinomina non basta, e si vede da cosa

**Da cosa dipende davvero la ripresa.** Due cose, non una:

1. **La directory delle trascrizioni**, il cui nome **codifica il percorso di lavoro**:
   `/root/.claude/projects/-root-legend-development` ↔ cwd `/root/legend-development`. Il picker
   `--resume` offre solo le sessioni la cui directory corrisponde alla cwd corrente, quindi sotto
   l'utente desktop il nome deve diventare `-home-desktop-legend-development`. Il manifest applica
   questa rimappatura nel campo `dest`: è una **rimappatura**, non uno spostamento.
2. **Lo stato per-progetto in `~/.claude.json`**, che è indicizzato per **percorso assoluto**. Sotto
   `projects["/root/legend-development"]` vivono `hasTrustDialogAccepted`, `allowedTools`,
   `mcpServers`, `enabledMcpjsonServers`. Quel file è in **DO_NOT_COPY** perché contiene anche
   `userID`, `machineID` e le credenziali di sessione.

**Conseguenza, dichiarata come tale:** copiare le trascrizioni e rinominarne la directory è
**necessario e non sufficiente**. Lo stato per-progetto non arriva, e non deve arrivare per copia
integrale.

**Raccomandazione, e il motivo.** L'utente desktop **riaccetta il trust dialog e ri-autorizza gli
strumenti** invece di ereditare `allowedTools` da `root`. Non è pedanteria: `allowedTools` è una
decisione di permesso presa da un altro utente, e trapiantarla farebbe agire il nuovo account su
autorizzazioni che non ha mai dato. Le due sessioni sono `3e1bc608-80c5-4c1c-a5a3-3c4da9b68c75` e
`d9ba7473-cfd2-4fcc-865b-0b236437dd03`.

### Collaudo — la migrazione delle trascrizioni non è riuscita finché questo non passa

Come utente desktop, dalla nuova directory di progetto:

```bash
cd /home/desktop/legend-development
ls ~/.claude/projects/-home-desktop-legend-development/*.jsonl   # 1. i file sono al loro posto
claude --resume                                                  # 2. il picker le elenca
claude --resume 3e1bc608-80c5-4c1c-a5a3-3c4da9b68c75             # 3. si apre per id
```

| Passo | Cosa dimostra | Esito richiesto |
|---|---|---|
| 1 | Copia e rimappatura riuscite | due `.jsonl`, byte e hash uguali al manifest |
| 2 | Il picker **trova** le sessioni dalla nuova cwd | entrambi gli id compaiono |
| 3 | La sessione **si apre e ha contenuto** | la conversazione carica e mostra la storia dello sweep |

**Il passo 2 è quello che la sola rinomina non garantisce**, ed è il motivo per cui il collaudo
esiste. Se il picker non le elenca, la causa più probabile è che il nome della directory non
corrisponde alla cwd — si verifica confrontando `pwd` con il nome codificato, non ipotizzando.

Finché il passo 3 non è passato **l'ambiente originale sotto `root` resta intatto**: è la copia di
sicurezza, ed è l'unica. Solo dopo un collaudo verde ha senso valutare la dismissione, che comunque
resta una tua decisione e non una conseguenza automatica del collaudo.

### Un vincolo temporale sulle trascrizioni

La trascrizione di **questa** sessione è in scrittura mentre la sessione è viva:
`3e1bc608-…jsonl` cambia a ogni turno. Una copia presa ora è corretta fino all'istante della copia e
**non conterrà la coda**. Due modi leciti, entrambi verificabili con il manifest:

- copiare **dopo** la chiusura di questa sessione, e rigenerare il manifest subito prima; oppure
- copiare ora e **risincronizzare quel singolo file** alla fine, ricalcolandone l'hash.

Gli altri 142 file di trascrizione e tutte le evidenze sono **quiescenti**: ultima scrittura in
`files/` alle 18:45, nei plugin alle 20:40, e nessun processo Claude è vivo oltre a questa sessione.
