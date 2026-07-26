# Protocollo MD — WT vs Q230P — **pre-registrato**

> **Public edition — method asset.** A **pre-registered** molecular-dynamics protocol: the observable, the acceptance criterion and the falsification are fixed *before* the run. It is published because the interesting part is the **self-correction** — the originally proposed production protocol aimed at the wrong observable and would have produced an expensive second `INCONCLUSIVE`. Nothing here is medical advice.

---


> Correzione del protocollo di produzione proposto dopo il pilot del 2026-07-12 (`md_q230p_pilot.py`).
> **Il pilot è valido e va tenuto: dimostra che la pipeline gira.** Ma il protocollo di produzione proposto **punta all'osservabile sbagliato** e produrrebbe un altro `INCONCLUSIVE`, solo più costoso.

---

## 🔴 L'errore da evitare: misurare la conseguenza lenta invece della causa veloce

La catena del modello ([[discovery_ledger_current#DL-MECH-052 — **WEAKENED:** ipotesi di packing elica/degron, non catena meccanicistica Q230P|DL-MECH-052]]):

```
Q230P → perturba il segmento 227-249? → cambia il packing dei candidati degron? → route HSC70/endolisosomiale?
        [screen EXPLO]              [non assegnato]                         [non assegnata]
```

Il protocollo proposto misurava **SASA di 187-191** — **l'ultimo anello, il più lento.** Esporre un motivo sepolto richiede uno **srotolamento locale**: centinaia di ns → μs. Con 414 residui in box da 12 nm (~140k atomi) su M5/OpenCL si fanno ~5-20 ns/giorno → **mesi**, per poi scoprire che non è successo nulla.

> **Misura il passo VELOCE che il modello asserisce, non la conseguenza lenta che il modello predice.**

Lo screen misura soltanto una risposta conformazionale del modello computazionale. Un negativo non esclude sintesi/turnover né la route; un positivo non dimostra esposizione del degron, HSC70 o CMA.

---

## Osservabile primario

**Occupanza dei legami H di backbone `O(i)···N(i+4)` lungo l'elica 226-251**, per-residuo, WT vs Q230P.

⚠️ **Non contare `O226···N230`.** La prolina **non ha l'idrogeno ammidico**: quel legame è perso **per costruzione topologica**, non per dinamica. **Non è evidenza.**
**L'evidenza è la PROPAGAZIONE**: si destabilizzano anche `227→231`, `228→232`, `229→233`, `231→235`…? L'elica si sfilaccia o si piega?

## Osservabili secondari
- **RMSF per-residuo** dei residui 226-251 (atteso: aumento locale in Q230P).
- **Contatti** Q230/P230 ↔ L187/V190 (persistenza).
- **Angolo/kink** dell'elica (asse spezzato attorno a 230).
- Coda **402-409** (I405, R408, L409 sono co-occlusori del motivo: si stacca?).
- **SASA 187-191** — si registra, ma **non è il criterio**: su questa scala è atteso non muoversi.

---

## 🎯 Criterio pre-registrato (scritto PRIMA di guardare i risultati)

| Esito | Condizione |
|---|---|
| **`SUPPORT_EXPLORATORY`** | In **≥2 repliche su 3**, Q230P mostra una variazione concordante del segmento, esclusa la perdita topologica verso Pro230. Autorizza soltanto un test dinamico migliore, non la catena biologica. |
| **`WEAKEN_EXPLORATORY`** | Con campionamento/equilibrazione adeguati Q230P resta indistinguibile dal WT sulle metriche pre-registrate. Indebolisce la specifica risposta simulata, non decide biologia o route. |
| **`INCONCLUSIVE`** | Repliche discordanti, controlli non separati, potenza/campionamento insufficienti o assenza di differenza senza assay sensitivity dimostrata. → piu' campionamento, metodo diverso o test wet. |

Gli esiti restano `EXPLO`: non vengono tradotti in KEEP/DISCARD biologico.

## Controlli meccanicistici obbligatori

| Sistema | Ruolo | Aspettativa pre-registrata |
|---|---|---|
| WT | baseline | elica 226-251 stabile |
| **Q230P** | test il genotipo di riferimento | perdita propagata di H-bond/kink, non solo il legame topologicamente impossibile verso Pro230 |
| **P252A** | comparatore biologico | Zhang mostra turnover lisosomiale/HSC70; non prova rottura del segmento né CMA |
| **P282A** | comparatore biologico | proteina stabile e HSC70-negativa nel sistema Zhang; non calibra il segmento 227-249 |

P252A/P282A contestualizzano lo screen ma non ne calibrano l'assay sensitivity biologica. Qualunque esito resta `EXPLO` finché non è collegato a misure wet sulla variante esatta.

---

## Sistema — correzioni al pilot

| # | Problema del pilot | Correzione |
|---|---|---|
| 1 | Simula **tutti i 414 residui** | **Solo il dominio SDR (~137-414).** I domini WW (1-91) + linker flessibile sbatacchiano, dominano RMSD/RMSF e **aggiungono rumore su un'osservabile che non li riguarda**. Box più piccola → **~3× più campionamento a parità di tempo**. |
| 2 | Box cubica **12 nm** | Con SDR-only bastano **~8,5 nm** (verificare padding minimo 1,2 nm dal soluto). |
| 3 | Timestep **2 fs** | **HMR (hydrogen mass repartitioning) + 4 fs** → **~2× speedup**. |
| 4 | Nessuna equilibrazione dichiarata | **NVT (100 ps, posizioni ristrette) → NPT (1 ns, ristrette) → NPT libero.** Verificare **plateau di densità e di RMSD** prima di iniziare la produzione. |
| 5 | Confronto di **energia potenziale totale** WT vs Q230P | ❌ **Privo di significato** (numero di acque diverso). *Il pilot lo ha già intercettato — corretto.* **Confrontare solo osservabili strutturali.** |
| 6 | 1 seed | **≥3 repliche indipendenti** per variante, seed diversi. |
| 7 | Il mutante nasce dal backbone WT dell'elica | ⚠️ **Limite intrinseco**: PDBFixer inserisce la Pro **mantenendo il backbone dell'elica WT perfetta**. La simulazione deve *trovare* la distorsione. Va **dichiarato**, ed è un motivo in più per usare repliche e per **non** interpretare i primi ns. |

## Durata
- **Fase 1 esplorativa:** WT/P252A/P282A, come comparatori; la loro separazione non calibra una route biologica.
- **Fase 2 Q230P:** solo se la calibrazione regge, **100 ns × ≥3 repliche** per WT e Q230P. Le stime temporali sono da misurare con benchmark locale; non assumere throughput prima del benchmark SDR-only.
- **Screen rapido alternativo (giorni, non settimane):** repliche a **T alta (400-450 K), 20 ns** — accelera esattamente l'evento di interesse (srotolamento locale) e dà la **stabilità relativa** dell'elica WT vs Q230P. ⚠️ È un **proxy**: i force field a 450 K sono meno affidabili. Da usare come **screen**, non come prova.

---

## ⚠️ Il punto strategico che conta più di tutto il resto

**La MD non è il test più economico né il più discriminante.** Il primo test wet deve separare sintesi, insolubilità e turnover sulla variante esatta.

> **C299R è ritirato come killer control:** il precedente 3,44 Å verso K297 era backbone-backbone; SG(C299)-NZ(K297) = 10,706 Å e C299 contatta H233 a 3,435 Å.

C299R può restare come comparatore esplorativo, non come controllo off-route. Priorità wet: Q230P esatta con sintesi nascent, frazionamento solubile/insolubile, emivita, sonde ortogonali di turnover e funzione; poi epistasi separata dei candidati `LRSVQ` e `ERLIQ` e dipendenza da LAMP2A. La MD è complementare, non sostitutiva.

---

*Nulla di questo è parere medico. Le predizioni in-silico sono `IPOTESI`, non validazione.*
