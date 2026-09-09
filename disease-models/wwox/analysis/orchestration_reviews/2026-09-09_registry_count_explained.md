# Da 67 a 59 — cosa misurano davvero i due numeri

Vanno separati subito, perché letti di fila sembrano un calo e **non lo sono**: il registro è solo
cresciuto. 67 e 59 misurano **cose diverse in momenti diversi**.

## 1 · Le due definizioni

| Metrica | Definizione |
|---|---|
| **Occorrenze** | Quante volte una delle quattro stringhe di `batch_queue.FULL_TEXT_MARKERS` compare in `paper_registry_current.md`: `full text reviewed`, `full text verificato`, `complete_fulltext_read`, `full text read` |
| **Record** | Quanti blocchi `PAPER n` contengono **almeno una** di quelle stringhe |

Non coincidono perché **un singolo record ne porta spesso due** — tipicamente uno stato in prosa e
una profondità di receipt — e in un caso ne porta sei.

## 2 · Il comando di conteggio

Riproducibile su qualunque revisione:

```bash
cat > /tmp/count_markers.py <<'PY'
import re, sys
markers = ("full text reviewed", "full text verificato", "complete_fulltext_read", "full text read")
t = sys.stdin.read().lower()
occ = sum(t.count(m) for m in markers)
heads = [m.start() for m in re.finditer(r"^#{1,4}\s*paper\s+\d+", t, re.M)]
bounds = list(zip(heads, heads[1:] + [len(t)]))
recs = sum(1 for a, b in bounds if any(m in t[a:b] for m in markers))
print(f"occorrenze={occ}  record_PAPER_con_marcatore={recs}  intestazioni_PAPER={len(heads)}")
PY

git show 690b865:disease-models/wwox/registries/paper_registry_current.md | python3 /tmp/count_markers.py
git show 2a35aec:disease-models/wwox/registries/paper_registry_current.md | python3 /tmp/count_markers.py
git show HEAD:disease-models/wwox/registries/paper_registry_current.md      | python3 /tmp/count_markers.py
```

## 3 · I numeri, misurati sui commit

| Revisione | Occorrenze | Record con marcatore | Intestazioni `PAPER` |
|---|---:|---:|---:|
| `690b865` — commit **prima** del batch | **67** | **48** | 70 |
| `2a35aec` — `BATCH_20260909_001` | **89** | **59** | 82 |
| `HEAD` — ora | 89 | 59 | 82 |

**Nessuna diminuzione.** Il registro ha guadagnato **12 record `PAPER`**, **22 occorrenze** e **11
record che dichiarano full text**. Il 67 appartiene al *prima* ed è misurato in occorrenze; il 59
appartiene al *dopo* ed è misurato in record. Accostarli è il confronto sbagliato, ed è esattamente
l'errore che stava dentro il gate.

## 4 · Modifiche al registro

L'unica scrittura è `BATCH_20260909_001` (`2a35aec`), che ha propagato 18 candidati su 33 creando 12
nuovi record `PAPER` (081–092) e aggiornandone altri. Dopo il batch il registro non è più cambiato:
i due commit successivi (`6308487`, `ae51990`) hanno rigenerato **superfici derivate**, non il
registro. Nessuna riga è stata riscritta per far quadrare un conteggio.

## 5 · Perché il numero è cambiato di significato a metà giornata

Il gate `test_coverage_is_not_overstated_against_the_registry` confrontava **studi** (conteggio per
studio, dal ledger) contro **stringhe** (tally di sottostringhe sul registro). Con 67 occorrenze
falliva — segnalando un problema vero. Dopo il batch, con 89 occorrenze contro 80 studi letti,
**passava**: verde proprio sulla condizione che esiste per rifiutare, perché il lato registro era
gonfiato di 30 rispetto al numero reale di paper.

La riparazione (`f9fc8b2`) conta ora i record `PAPER`, e il verdetto onesto è rosso:

> **80 studi letti contro 59 record di registro che dichiarano full text.**

## 6 · Lo scarto vero

| Momento | Studi letti | Record | Scarto |
|---|---:|---:|---:|
| Prima del batch | 80 | 48 | **32** |
| Dopo il batch | 80 | 59 | **21** |

Il batch ha fatto lavoro reale — 11 paper registrati — e **lo scarto resta aperto**. I 21 residui
sono studi con lettura completa e nessun record: non si chiudono con un altro giro di integrazione,
perché per quelli i candidati non esistono e vanno scritti. `BATCH_20260909_001` aveva dichiarato il
ratchet chiuso; il suo stesso autore ha ritirato l'affermazione (`596e7dd`) dopo che la riparazione
del gate ha mostrato che la chiusura era un artefatto dell'unità sbagliata.
