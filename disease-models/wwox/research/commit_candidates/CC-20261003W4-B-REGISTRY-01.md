# COMMIT CANDIDATE — CC-20261003W4-B-REGISTRY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 4 2026-10-03, branch `task/sci-B-20261003w4`.
**Purpose:** give every record this wave read a structured landing, so that no completed reading sits in
the ledger without a registry presence (`ORPHAN_COMPLETE_READ` is what blocks `BATCH_COMMIT` when it does).
**Not medical advice.**

## Does each record need a landing? — measured, not assumed

| Record | Registry presence today | Receipt prepared | Landing needed |
|---|---|---|---|
| PMID 33914858 | `PAPER 004` (integrated) **and** duplicate `CORPUS-STUB-087` on the same DOI | `FTR-20261003-33914858-02` | **Repair**: enrich `PAPER 004`, merge/retire the duplicate |
| PMID 35328751 | `PAPER 023` | `FTR-20261003-35328751-02` | handled by `CC-20261003W4-B-HIF1A-SCOPE-01` |
| PMID 35460704 | **none** (`registry_records.py get --pmid 35460704` → NO RECORD MATCHED) | `FTR-20261003-35460704-01` | **new `PAPER`** |
| PMID 33612478 | `CORPUS-STUB-109`, `not_processed` | `FTR-20261003-33612478-01` | **upgrade the stub** |
| bioRxiv PPR1124524 | none | `FTR-20261003-PPR1124524-01` | **new `PAPER`**, labelled preprint |
| bioRxiv PPR1015434 | none | `FTR-20261003-PPR1015434-01` | **new `PAPER`**, labelled preprint |

Next free numbers re-measured with `registry_records.py catalog` after merging `main` at `58bd066`:
highest `PAPER 142`, highest `LIT-0431`, highest `CORPUS-STUB-179`, highest `CLAIM 044`. (At
`296cd5ba5596`, three hours earlier, the highest `PAPER` was 132 and the highest `CLAIM` 042 — the
numbers moved under this branch while it was being written, which is why they are renumbered here and
must be renumbered again.) 🔴 **All of these are
provisional**: three scientists and an integrator are landing in parallel this day, so the propagating
batch must re-measure and renumber before applying.

## Change class

**MINOR** — registry additions and one stub upgrade. No claim is created here (the only new claim this
wave proposes is `CC-20261003W4-B-CARRIER-01`), nothing is reversed, nothing is deleted.

## Ordering

All six receipts must be appended first, in event order:
`scratchpad/receipts_pending_w4/sciB_33914858_1.json`, `sciB_PPR1124524_1.json`,
`sciB_PPR1015434_1.json`, `sciB_35460704_1.json`, `sciB_35328751_1.json`, `sciB_33612478_1.json`.

## Op list — `paper_registry_current.md` (record-scoped; **dry run NOT executed**; numbers provisional)

```json
[
 {
  "op": "insert-after",
  "id": "PAPER 142",
  "new": "## PAPER 143\n**Short title:** Dong 2022 JLR — exome sequencing in hypoalphalipoproteinemia\n**Full title:** Whole-exome sequencing reveals damaging gene variants associated with hypoalphalipoproteinemia\n**Year:** 2022\n**Source type:** human genomic discovery study (whole-exome sequencing, candidate-gene filter + binomial burden test)\n**Journal/source:** *Journal of Lipid Research* 2022;63(6):100209\n**Identifier:** PMID 35460704 / PMCID PMC9126845 / DOI 10.1016/j.jlr.2022.100209\n**Status:** processed\n**Evidence depth:** `partial_fulltext_read` — ricevuta `FTR-20261003-35460704-01`, JATS Europe PMC, manifest `deepdive_manifests/PMID35460704.json` (6 locator, validatore PASS con `--verify-artifacts`), dossier `fulltext_dossiers/PMID35460704.md`. Parziale: pannelli non ispezionati come immagini, lista dei riferimenti non letta.\n**Integrity status:** clean\n**Primary pathway:** P5 — metabolismo / lipidi\n**Model/species:** umano, 204 persone selezionate per HDL-C sotto il 10º percentile di una sola coorte di ricerca\n**Genotype/model:** nessuna perturbazione; varianti rare annotate in silico\n**Transferability:** T3\n**clinical relevance:** LOW\n**Claim links:** 045\n**Role:** il negativo umano più nitido disponibile sull'eterozigote WWOX\n**Note:** 🔴 **DO_NOT_CITE come «quattro portatori WWOX con un'anomalia biochimica».** Le quattro «occorrenze» WWOX sono **tre alleli missenso eterozigoti distinti** — p.Gly30Arg (gnomAD 5.61 × 10⁻⁶, 1 partecipante), p.Arg120Trp (gnomAD 7.50 × 10⁻³, ClinVar **Benign**, 2 partecipanti), p.Leu307Val (gnomAD 5.28 × 10⁻⁵, 1 partecipante) — senza alcun allele loss-of-function, frameshift, di splicing o omozigote. WWOX **non** raggiunge la significatività nel burden test (la raggiungono ABCA1, LDLR, HK3, CFTR); nessun valore lipidico è riportato per un portatore WWOX; e gli autori stessi dichiarano di non avere coorte di confronto a HDL-C normale. Earned null utile: **nessun evento di copy-number** in alcuno dei 104 geni candidati HDL, quindi nessuna delezione o duplicazione WWOX in questa coorte, entro l'insensibilità dichiarata del CNV calling da esoma. «Probably damaging» è una predizione di dieci strumenti, non un saggio.\n**Wikilinks:** [[claim_registry_current#CLAIM 045]]\n\n---\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 143",
  "new": "## PAPER 144\n**Short title:** Abudiab 2025 bioRxiv — WWOX e riparazione della mielina (**PREPRINT**)\n**Full title:** WWOX deficiency uncovers a cell-autonomous mechanism impairing myelin repair\n**Year:** 2025\n**Source type:** 🔴 **preprint bioRxiv, NON sottoposto a peer review** — v1 del 2025-11-24, CC-BY-NC-ND. Layer di ricerca: non può alzare lo stato di alcuna claim.\n**Journal/source:** bioRxiv\n**Identifier:** DOI 10.1101/2025.11.22.689900 / bioRxiv PPR1124524 — **nessun PMID**\n**Status:** processed (research layer)\n**Evidence depth:** `partial_fulltext_read` — ricevuta `FTR-20261003-PPR1124524-01`, PDF bioRxiv `files/fulltext/PPR1124524_Abudiab2025_bioRxiv.pdf` con layer di testo derivato, dossier `fulltext_dossiers/PPR1124524.md`. **Nessun deep-dive manifest**: i manifest sono indicizzati per PMID e un file con nome PPR non sarebbe risolvibile dal modulo di provenance; i locator stanno nel dossier e in `CC-20261003W4-B-MYELIN-CELLAUT-01`.\n**Integrity status:** clean\n**Primary pathway:** P4 — mielinizzazione / sostanza bianca\n**Model/species:** topo (condizionale Olig2-Cre; colture OPC dal null costitutivo), linea Oli-neu, HEK293T, dati umani snRNA-seq di lesioni di sclerosi multipla\n**Genotype/model:** delezione di lignaggio oligodendrogliale (**non** inducibile, **non** temporizzata sull'OPC adulto)\n**Transferability:** T2 per il meccanismo, T3 per la sclerosi multipla\n**clinical relevance:** MODERATE\n**Claim links:** none — un preprint non fonda una claim\n**Role:** l'esperimento che `CLAIM 003` nomina come condizione, in una fonte che non può discharge quella condizione\n**Note:** al basale **nessuna ipomielinizzazione** (assoni mielinizzati per campo 117.6 ± 12.5 vs 125.1 ± 9, P = 0.22); il fenotipo emerge solo sotto sfida (18 mesi; rimielinizzazione dopo cuprizone, con demielinizzazione uguale fra i genotipi). Meccanismo proposto: WWOX lega e stabilizza SOX10 via dominio WW1. **Stesso laboratorio senior di `PAPER 004`** — non è un osservatore indipendente. Nessun braccio eterozigote: i topi `Wwox +/−` sono nominati nei Metodi e non usati. Disponibilità dei dati «upon publication», nessun accession.\n**Wikilinks:** [[paper_registry_current#PAPER 004]] · [[claim_registry_current#CLAIM 003]]\n\n---\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 144",
  "new": "## PAPER 145\n**Short title:** Lucas-Clarke 2025 bioRxiv — dose di *Wwox* in un modello amiloide di *Drosophila* (**PREPRINT**)\n**Full title:** Alzheimer's disease risk gene Wwox protects against amyloid pathology through metabolic reprogramming\n**Year:** 2025\n**Source type:** 🔴 **preprint bioRxiv, NON sottoposto a peer review** — v1 del 2025-05-07, CC-BY. Layer di ricerca.\n**Journal/source:** bioRxiv\n**Identifier:** DOI 10.1101/2025.05.01.651195 / bioRxiv PPR1015434 — **nessun PMID**\n**Status:** processed (research layer)\n**Evidence depth:** `partial_fulltext_read` — ricevuta `FTR-20261003-PPR1015434-01`, JATS Europe PMC `files/fulltext/PPR1015434_LucasClarke2025_EPMC.xml` più supplemento, dossier `fulltext_dossiers/PPR1015434.md`. Nessun manifest, per la stessa ragione di `PAPER 144`.\n**Integrity status:** clean\n**Primary pathway:** P5 — metabolismo (piruvato / UPR)\n**Model/species:** *Drosophila melanogaster*\n**Genotype/model:** RNAi pan-neuronale, pan-gliale e sul clock; **CRISPRa** al sito di inizio della trascrizione di *Wwox* (circa 2× mRNA); cDNA di *Wwox* di mosca e di *WWOX* umano\n**Transferability:** T3\n**clinical relevance:** LOW-MODERATE (classe di leva, non evidenza clinica)\n**Claim links:** none\n**Role:** l'unica fonte del corpus che muove WWOX in **entrambe le direzioni nello stesso modello**, e che misura la ri-fornitura come **up-regolazione endogena a dose modesta**\n**Note:** il knockdown accorcia la vita e, con Aβ42, è sinergico (interazione p < 0.0001) e alza l'Aβ42 **solubile**; la via è PERK–Atf4 → Ldh → lattato, e il knockdown di *Ldh* **recupera** il deficit locomotorio. Il reporter di HIF1α (*sima*) **non** si muove: un negativo diretto sull'asse WWOX/HIF1A in questo sistema. L'up-regolazione riduce il carico amiloide e recupera vita e locomozione **senza riportare giù il lattato**, abbassando invece la L-metionina — la risposta non percorre a ritroso lo stesso meccanismo. Nessun endpoint di mielina (la mosca non ha mielina nel CNS); nessun livello proteico di WWOX misurato; «AD risk gene» è un'attribuzione GWAS/eQTL su una variante intergenica fra *WWOX* e *MAF*. Dati depositati (ArrayExpress E-MTAB-14948, E-MTAB-14949; MetaboLights MTBLS12344).\n\n---\n"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-109",
  "old": "**Status:** not_processed\n**Registry role:** corpus placeholder only\n**Claim links:** none\n**Next action:** screening / triage required",
  "new": "**Status:** processed — letto per intero il 2026-10-03, verdetto **OFF-AXIS**\n**Registry role:** record di lettura; nessuna claim ne discende\n**Evidence depth:** `partial_fulltext_read` — ricevuta `FTR-20261003-33612478-01`, JATS Europe PMC (PMC7950260), manifest `deepdive_manifests/PMID33612478.json` (4 locator, validatore PASS), dossier `fulltext_dossiers/PMID33612478.md`\n**Claim links:** none\n**Next action:** nessuna. 🔴 **DO_NOT_CITE a sostegno di un effetto di dose di WWOX sui lipidi.** Studio di associazione su SNP comuni (MAF > 10% per costruzione) in una sola popolazione; i due SNP assegnati a WWOX distano circa 500 kb e sono in LD debole **per ammissione degli autori**, e le posizioni che il lavoro stesso stampa collocano rs2222896 **fuori dal corpo del gene** WWOX nello stesso build usato da `PAPER 143`; gli autori **ritirano** l'associazione rs2548861–HDL-C («we speculated that mutations at rs2548861 were not correlated with HDL-C concentration in these subjects»); nulla di WWOX è misurato o perturbato, e gli autori elencano il lavoro funzionale fra i propri limiti. Due incoerenze interne registrate: l'abstract dà l'interazione rs3132584 × rs2222896 come 2.548× «and predicted hypertension» mentre i Risultati danno 1.523× per l'ipertensione, e la Tabella 1 stampa il peso del gruppo normale come 54.48 ± 110.29 kg."
 }
]
```

## Op list — `paper_registry_current.md`, the duplicate identity

`PAPER 004` and `CORPUS-STUB-087` carry the **same DOI** (10.1093/brain/awab174). `PAPER 004`'s own note
has flagged this since 2026-07-05 and it is still open. One PMID with two identity records is what makes
a paper countable twice, and this wave adds a receipt to it. **Proposed:** retire `CORPUS-STUB-087` to a
pointer rather than delete it (deleting unique material is reserved, §21d):

```json
[
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-087",
  "old": "**Status:** not_processed\n**Registry role:** corpus placeholder only\n**Claim links:** none\n**Next action:** screening / triage required",
  "new": "**Status:** superseded — identità duplicata\n**Registry role:** puntatore storico; il record vivo di questo DOI è [[paper_registry_current#PAPER 004]]\n**Claim links:** none\n**Next action:** nessuna. Mergiato il 2026-10-03 con `CC-20261003W4-B-REGISTRY-01`, come la nota di `PAPER 004` chiedeva dal 2026-07-05. Il testo originale dello stub è conservato sopra; nulla è cancellato."
 }
]
```

## Op list — `PAPER 004`, the quantitative enrichment its own note deferred

```json
[
 {
  "op": "replace-within",
  "id": "PAPER 004",
  "old": "**Note:** justifies MRI + DTI logic.",
  "new": "**Evidence depth:** `partial_fulltext_read` — ricevute `FTR-20260923-33914858-01` e `FTR-20261003-33914858-02`, manifest `deepdive_manifests/PMID33914858.json` (6 locator su pagina resa, validatore PASS), dossier `fulltext_dossiers/PMID33914858.md`.\n**Quantità, dalla pagina stampata (2026-10-03, `CC-20261003W4-B-REGISTRY-01`), che la nota qui sotto rimandava a un PDF mai ottenuto:** assoni mielinizzati per campo nel corpo calloso a P17, S-Control 180 ± 40 contro S-KO 55 ± 35 — circa **3.3 volte**, non le «3.5–4 volte» a cui il testo corrente del lavoro arrotonda; assoni non mielinizzati nel nervo ottico 55 ± 20 contro 270 ± 60; g-ratio significativamente più alto in entrambi i tratti; oligodendrociti maturi CC1-positivi ridotti di **due volte** con OPC significativamente più numerosi; **nessuna morte oligodendrocitaria** significativa (CC1 + caspasi 3 clivata). Limite di potenza su ogni numero di spessore: l'analisi del g-ratio è potenziata a livello di assone, circa 600 assoni, 100 per topo, **n = 3 per genotipo**.\n🔴 **Debito di artefatto, dichiarato 2026-10-03:** l'HTML dell'editore che la ricevuta `FTR-20260923-33914858-01` dichiara come propria superficie di testo autorevole — `files/fulltext/PMID33914858_Repudi2021_OUP.html`, sha256 `3baf27af9f906a8bfa013924a90a0eca7713b25463d6f039fddef0242caac902` — **non è presente in questo checkout**, né lo sono i cinque supplementi che quella ricevuta nomina; cercati per nome su tutta la macchina e per SHA-256 su 504 file candidati. I locator di quella lettura sono quindi **non auditabili** finché l'artefatto non rientra. La ri-acquisizione è stata ritentata il 2026-10-03 e fallisce su ogni rotta libera: OUP risponde HTTP 403 dietro Cloudflare su tre URL, non esiste PMCID, Unpaywall e OpenAlex nominano solo quella posizione bronze con `has_repository_copy: false`, e l'indice CDX di Wayback non ha alcuna cattura. Cosa sbloccherebbe: una copia dell'operatore dello stesso HTML, o un prestito interbibliotecario.\n**Note:** justifies MRI + DTI logic."
 }
]
```

🔴 **No dry run was executed for any list above** — this worktree's brief forbids touching the four
current files in any mode. Every `old` string was measured unique **within its record** by reading that
record through `registry_records.py get` at commit `296cd5ba5596`. The propagating batch re-measures,
renumbers, and runs the dry propagation before `--apply`.

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. The dyslipidaemia paper's two WWOX SNPs are far apart and weakly linked | rs2222896 and rs2548861 at chromosomal positions 78058601 and 78624496, respectively, were about 500 kb from each other, resulting in a weak LD between them | PMID 33612478, Discussion, `files/fulltext/PMID33612478_Liu2021_PMC.xml`
2. Its authors withdraw the WWOX-HDL-C association | Thus, we speculated that mutations at rs2548861 were not correlated with HDL-C concentration in these subjects. | PMID 33612478, Discussion, same artefact
3. Its variants are common by construction | Only SNPs with MAF greater than 10% were included. | PMID 33612478, Materials and methods, SNP selection, same artefact
4. The exome study found no structural variant in any HDL candidate gene | No CNVs were found among our list of 104 HDL candidate genes | PMID 35460704, Results, Copy number variants, `files/fulltext/PMID35460704_Dong2022_PMC.xml`
5. The neuronal-deletion paper's myelin counts | The number of myelinated axons (S-Control, average = 180 ± 40, S-KO, average = 55 ± 35) in corpus callosum and unmyelinated axons (S-Control, average = 55 ± 20, S-KO, average = 270 ± 60) in optic nerve is counted per field of view | PMID 33914858, Results, printed page 27 of 48, `files/fulltext/PMID33914858_Repudi2021_OUP_browserprint.pdf`
6. Its g-ratio analysis is powered at the axon level | myelinated axons (~600, 100 axons per mouse, n = 3 per genotype) from electron microsope images either from corpus callosum or optic nerve were analysed, by dividing inner axonal diameter over the total axonal diameter | PMID 33914858, Methods, Electron microscopy, printed page 10 of 48, same artefact
7. The fly preprint's HIF1α-homologue reporter does not move | No changes in endogenously tagged sima:GFP (HIF1α homolog) levels were observed in the adult fly brain after neuronal Wwox knockdown in Aβ42 overexpressing flies | PPR1015434, Results, lactate/Atf4 section, `files/fulltext/PPR1015434_LucasClarke2025_EPMC.xml`
8. Its upregulation arm is a measured, modest endogenous increase | This was sufficient to achieve ~2-fold increase in Wwox mRNA levels in the fly head | PPR1015434, Results, CRISPRa section, same artefact


## BATCH DISPOSITION — `BATCH_20261003_003` (2026-10-03, ACTOR_ID `scientist`, Scientist H), append-only

**Verdict:** PROPAGATED

**PROPAGATED, renumbered.** The declared `PAPER 143`/`144`/`145` were taken by `BATCH_20261003_002`; applied as **`PAPER 156`** (Dong 2022), **`157`** (Abudiab preprint) and **`158`** (Lucas-Clarke preprint), with the first `insert-after` re-anchored from `PAPER 142` to `PAPER 155`. The ops were authored with the key `new` where the editor expects `text` on an insert; they were normalised, not forced. **Preprint identity, decided and stated:** neither preprint has a PMID and their receipts (`FTR-20261003-PPR1124524-01`, `-PPR1015434-01`) are keyed by DOI alone, so each record is keyed `DOI … / bioRxiv PPR… — no PMID`, which is the convention `PAPER 114` and `LIT-001` already use for a preprint; `coverage_report`'s receipt index resolves a record by PMID **or** DOI, so the landing is machine-resolvable. Three `LIT` records the candidate did not propose were authored for the pairing convention: `LIT-0445`–`0447`. **AM4:** `PAPER 004`'s depth line was rewritten — it declared `partial_fulltext_read` while naming both receipts, and the depth was read off the ledger's coverage maps instead (`-02` partial on the rendered browser print, `-01` complete on the publisher HTML that is absent from this checkout). LINT then returned `UNBACKED_FULLTEXT_DECLARATION` because the literal `complete_fulltext_read` is a FULL_TEXT marker **anywhere** in the field; the sentence now says *complete depth* in words. The artefact-debt paragraph is propagated verbatim: the browser-print PDF the audited triples cite **is** in the checkout, so those locators are not unauditable — audit 1 verified 6/6 of them against it, page numbers included.
