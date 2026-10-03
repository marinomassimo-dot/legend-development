# COMMIT CANDIDATE — CC-20261003W4-A-AUTOPHAGY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 4 2026-10-03, branch `task/sci-A-20261003w4`.
**context_policy:** `SOURCE_FIRST` — first pass written from the sources before any registry record was opened; comparison afterwards (see `research/intake_wave_20261003w4_A.md`).
**Not medical advice.** Class-level statements about published genotypes only.

## Target
`full_text_queue_current.md` · `FT-074`: one status paragraph. (`PAPER 152` is created by `CC-20261003W4-A-REGISTRY-01`.) Debt paid: `33300063` was a stub read only by title in the autophagy-direction argument.

## Finding (transfer limit: ovarian carcinoma lines, overexpression/one siRNA; nothing neural)
The title's direction holds on **steady-state protein abundance** (WWOX up → Beclin-1/LC3 down; down → up), concordant with `24008736`; flux is clamped only on the paclitaxel arm. p-mTOR moves with WWOX dose in both directions — a correlation, no epistasis; p-p70S6K not detected although the Discussion asserts "mTOR/p70S6K"; PTX raises p-4E-BP1 while lowering p-mTOR. The abstract's "reduced WWOX" in the resistant line contradicts its Results. **The corpus-level conclusion of `FT-074` stands with one amendment** (mTOR route correlated with WWOX dose in one cancer system, causally untested).

## Change class
**MINOR**.

## Op list — `full_text_queue_current.md` (record-scoped; dry run 2026-10-03 with `record_scoped_edit.py apply` on copies of `main` 663970a (merged into the branch, after `BATCH_20261003_002` landed): exit 0, 1 op(s), keys ['FT-074'])

```json
[
 {
  "op": "replace-within",
  "id": "FT-074",
  "old": "**Next action aggiornata:** `-043` resta il primo da leggere",
  "new": "✅ **`-056` letto per intero il 2026-10-03** (intake wave 4, Scientist A; ricevuta `FTR-20261003-33300063-01`, PDF bronze-OA dell'editore più Supplementary Figure S1; `CC-20261003W4-A-AUTOPHAGY-01`; lo stub è promosso a `PAPER 152`, numero provvisorio) — **tre dei quattro letti.** È **concordante con `-139` e ha la stessa lacuna**: WWOX su → Beclin-1 e LC3 giù, WWOX giù → su, su blot rappresentativi senza densitometria né statistica; l'unico clamp (clorochina) è sul braccio **paclitaxel**, mai su un braccio WWOX; nessun p62 sui bracci WWOX. **Nuovo rispetto alla forma ristretta:** p-mTOR segue la dose di WWOX in entrambe le direzioni (sovraespressione su, siRNA giù) — una correlazione fosfo misurata, senza epistasi con un inibitore di mTOR, con i totali dei bersagli a valle non misurati e p-p70S6K non rilevato (la Discussione scrive comunque «mTOR/p70S6K»). L'abstract dice «WWOX ridotto» nella linea resistente; i Results gli danno il WWOX basale più alto. Forma ristretta con un emendamento: *la via mTOR è correlata alla dose di WWOX in un sistema tumorale e non testata causalmente in nessun punto di questo corpus.* Ancora niente di neurale. La domanda posta a `-043` qui sotto vale anche per `-056`, e la risposta per `-056` è **no**.\n\n**Next action aggiornata:** `-043` resta il primo da leggere"
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(WWOX overexpression lowers Beclin-1 and LC3 on blots | expression inhibited autophagy, as evidenced by the notable | PMID 33300063, Results 'WWOX inhibits autophagy'; files/fulltext/PMID33300063_Zhao2020_Spandidos.txt)
(phospho-p70S6K was not detectable | p‑p70S6K kinase (at Thr389 and Ser371) was barely detected | PMID 33300063, Results; files/fulltext/PMID33300063_Zhao2020_Spandidos.txt)
(the Discussion nevertheless says WWOX activated mTOR/p70S6K | Beclin‑1. Furthermore, WWOX activated mTOR/p70S6K | PMID 33300063, Discussion; files/fulltext/PMID33300063_Zhao2020_Spandidos.txt)
(the abstract says the resistant line has reduced WWOX | (A2780/T) were characterized by reduced WWOX expression | PMID 33300063, Abstract; files/fulltext/PMID33300063_Zhao2020_Spandidos.txt)
(the Results say the resistant line has the highest basal WWOX | EOC cell lines and the highest protein expression levels of | PMID 33300063, Results; files/fulltext/PMID33300063_Zhao2020_Spandidos.txt)
