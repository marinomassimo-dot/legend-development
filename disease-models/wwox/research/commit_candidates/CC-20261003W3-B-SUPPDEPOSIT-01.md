# COMMIT CANDIDATE — CC-20261003W3-B-SUPPDEPOSIT-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 3 2026-10-03, branch `task/sci-B-20261003w3`.
**context_policy:** `SOURCE_FIRST` — every source was read and its first pass written before any registry
statement about it was opened; the comparison is in `research/intake_wave_20261003w3_B.md`.
**Not medical advice.** Class-level statements about published models only.

## Target
`disease-models/wwox/research/full_text_queue_current.md` · `FT-074` — one replacement of the record's
`Current status` line, carrying three facts the record cannot currently state.

## What is wrong now
1. **The status line contradicts the record's own body.** It reads *«⬜ aperto — debito di lettura
   dichiarato il 2026-08-26, nessuno dei quattro letto»*, while the block above it, dated 2026-09-21,
   records that one of the four was read.
2. **The record counts an arm that cannot be inspected.** It treats PMID 24008736's `Wwox+/−` / `Wwox−/−`
   MEF LC3-II result as the loss-of-function member of the four. That result lives in Supplementary
   Figure 7, and **the supplement deposited under that article's identifier is a different article's
   supplement** — measured from two independent routes, same bytes:

   | Route | sha256 | content |
   |---|---|---|
   | PMC OA S3 open-data bucket `PMC3789168.1/cddis2013308x1.pdf` | `dc13d0427a4777bf4e09661df3e6cab669f005edb232adbc5d2cb4bda957004f` | five figures of an unrelated haematology study |
   | Europe PMC `supplementaryFiles` for PMC3789168 | identical | identical |

   It is not systematic: the supplement of PMID 21368882, fetched the same way in the same pass, is that
   article's own.
3. **The stalemate is no longer "one paper against one".** Measured 2026-10-03 with PubMed `esearch`
   (`tool=LEGEND-research`): `WWOX AND autophagy` returns 10 records, and
   `WWOX AND autophagy NOT Chang NS[au] NOT Hsu LJ[au]` returns 8 — so the axis is mostly independent of the
   originating laboratory. A second independent laboratory (PMID 33300063, `CORPUS-STUB-056`) is on the same
   side as PMID 24008736.

## Change class
**MINOR** — a research-layer queue record's status line (§ 7). It does not reverse a `consolidated baseline`
claim: it narrows an artefact-availability fact and corrects a status line against the record's own body.

## Ordering
The receipts named below must be appended to the ledger before this candidate is propagated, so that no
record cites a receipt the ledger does not hold. They are prepared, not recorded:
`scratchpad/receipts_pending_w3/sciB_<pmid>_1.json`, event ids `FTR-20261003-<pmid>-01` or `-02`.

## Op list — `full_text_queue_current.md` (record-scoped; dry run 2026-10-03 on `main` 0e6fd4e9b886 with `record_scoped_edit.py apply`: exit 0, 1 op(s), keys ['FT-074'])

```json
[
 {
  "op": "replace-within",
  "id": "FT-074",
  "old": "**Current status:** ⬜ aperto — debito di lettura dichiarato il 2026-08-26, nessuno dei quattro letto.",
  "new": "**Current status:** 🟨 **parzialmente chiusa — due dei quattro letti, e la riga precedente (*«nessuno dei quattro letto»*) era già falsa quando il blocco 2026-09-21 sopra la contraddiceva.** Aggiornato 2026-10-03 (`CC-20261003W3-B-SUPPDEPOSIT-01`, intake wave 3, Scientist B).\n\n🔴 **IL BRACCIO LOSS-OF-FUNCTION DI `-139` NON È ISPEZIONABILE: il supplemento depositato sotto l'identificativo di PMID 24008736 è il supplemento di un altro articolo.** Misurato, non dedotto: il file `cddis2013308x1.pdf` (5 pagine, sha256 `dc13d0427a4777bf4e09661df3e6cab669f005edb232adbc5d2cb4bda957004f`) contiene cinque figure di uno studio ematologico non correlato, e **gli stessi byte** arrivano da due rotte indipendenti — il bucket open-data PMC OA S3 e l'endpoint `supplementaryFiles` di Europe PMC. Non è un errore di fetch e non è sistematico: il supplemento di PMID 21368882, preso con la stessa rotta nello stesso passaggio, è quello giusto. Conseguenza per questa voce: la **Supplementary Figure 7** — il pannello LC3-II nei MEF `Wwox+/−` e `Wwox−/−`, cioè l'unico braccio in cui la variabile è un genotipo germinale e non un farmaco, e il braccio che questa voce conta come membro loss-of-function dei quattro — **resta una singola frase di testo corrente senza pannello ispezionabile**. Idem per S4 (Atg12 a 21 kDa), S5 (MG132) e S6 (colocalizzazione e co-IP WWOX–mTOR). Cosa lo sbloccherebbe: il file supplementare dalla pagina dell'editore, oppure una richiesta all'autore corrispondente — nessuna delle due tentata qui (nessuna spesa esterna, nessuna corrispondenza senza l'operatore).\n\n✅ **`-139` riletto per intero il 2026-10-03 con i pannelli** (ricevuta `FTR-20261003-24008736-02`, dossier `research/fulltext_dossiers/PMID24008736.md`): la lettura 2026-09-21, fatta su un'estrazione testuale senza figure, **regge**, e due punti si precisano. (1) Il clamp lisosomiale esiste ed è quantificato — Fig 3c, LC3-II 1,0 / 0,5 (MTX) / 1,6 (E64d+pepstatina A) / 1,0 (MTX + E64d+pepstatina A) a 12 h — ma è applicato **al farmaco**, mai a una manipolazione di WWOX: il passo WWOX→autofagia non è mai misurato come flusso. (2) La perdita di LC3 è instradata al **proteasoma** (MG132 la blocca), che è una rotta diversa da quella lisosomiale che lo stesso laboratorio assegna nel 2026 a Bcl-XL/Mcl-1 nello stesso fondo SCC-15: carico diverso, non lo stesso meccanismo detto due volte.\n\n✅ **`-043` resta non letto e non ha PMCID**; la sua direzione opposta (*WWOX attiva l'autofagia*) rimane non verificabile di prima mano. Ma lo stallo **non è più «un paper contro uno»**: censimento misurato il 2026-10-03 (`esearch`, tool=LEGEND-research) — `WWOX AND autophagy` = 10 record, di cui **8 né Chang NS né Hsu LJ**. Sul lato «sopprime» c'è un secondo laboratorio indipendente (PMID 33300063, carcinoma ovarico, paclitaxel, `CORPUS-STUB-056`); sul lato «attiva» c'è `-043` (PMID 36621327, danno polmonare acuto da LPS, mTOR–ULK1). La differenza fra i due poli non è solo il laboratorio: è lo **stress** (antimetabolita/chemioterapico contro infiammatorio) e il **tessuto** (epitelio tumorale contro epitelio polmonare in danno acuto). Nessuno dei due è neurale, nessuno dei due è un genotipo umano.\n\n**Next action aggiornata:** `-043` resta il primo da leggere, e la domanda da portargli è ora precisa — *il suo LC3-II è misurato sotto clamp lisosomiale, e su una manipolazione di WWOX?* Se non lo è, nessuno dei due poli ha mai misurato il flusso sulla variabile giusta, e la contraddizione è fra due marcatori statici, non fra due flussi."
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(the loss-of-function arm of this paper is one sentence pointing at a supplementary figure | In our recently developed Wwox gene knockout mouse embryonic fibroblasts, increased expression of LC3-II protein was detected in the cytosolic protein extracts from the Wwox+/− and Wwox−/− cells using western blotting, as compared with the Wwox+/+ control cells | PMID 24008736, Results 'WWOX suppresses autophagy in SCC cells'; files/fulltext/PMID24008736_Tsai2013_PMC.xml)
(the lysosomal clamp was applied to the drug and the LC3 fall survived it | the presence of E64d and pepstatin A did not prevent MTX-induced downregulation of LC3 protein expression | PMID 24008736, Results 'MTX modulates autophagy in SCC cells'; files/fulltext/PMID24008736_Tsai2013_PMC.xml)
(the LC3 loss is routed to the proteasome in this paper | Treatment of SCC-15 cells with a proteasome inhibitor MG132 blocked MTX-induced LC3 protein downregulation, indicating that LC3 protein is degraded via the ubiquitin/proteasomal pathway post MTX treatment | PMID 24008736, Results 'MTX modulates autophagy in SCC cells'; files/fulltext/PMID24008736_Tsai2013_PMC.xml)
(the causal order through mTOR is offered as a possibility | raising the possibility that WWOX may regulate autophagy through mTOR activation in MTX-treated SCC-15 cells | PMID 24008736, Results 'MTX treatment modulates mTOR signaling in SCC cells via WWOX'; files/fulltext/PMID24008736_Tsai2013_PMC.xml)
(the file deposited as this article's supplement carries another study's figures | Supplementary Figure 1 | PMID 24008736, page 1 of the deposited supplementary PDF; files/supplements/PMID24008736/cddis2013308x1.pdf)


---

## BATCH DISPOSITION — `BATCH_20261003_002` (2026-10-03, ACTOR_ID `scientist`, Scientist G), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED (MINOR)

One op applied to `FT-074`. Blind audit: all 5 triples SUPPORTED; the auditor independently confirmed the deposited `cddis2013308x1.pdf` is an unrelated haematology study (five figures, nothing on WWOX, methotrexate, carcinoma or autophagy), and that the article cites Supplementary Figures 5 and 7 which the deposit does not contain.

**Not medical advice.**
