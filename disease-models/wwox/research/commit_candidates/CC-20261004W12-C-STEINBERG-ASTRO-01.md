# CC-20261004W12-C-STEINBERG-ASTRO-01 — the organoid astrogenesis finding is an IF/immunoblot finding, and an unreported NPY collapse sits beside it

- **Wave:** intake wave 12, 2026-10-04, Scientist C (RE-READ wave)
- **context_policy:** SOURCE_FIRST — the marker panel was matched cell-wise against both deposited
  differential-expression tables before CLAIM 002 and CLAIM 005 were opened.
- **Target records:** `CLAIM 002` (**`consolidated baseline`**) and `CLAIM 005`
  (**`consolidated baseline`**), both in
  `disease-models/wwox/registries/claim_registry_current.md`
- **Change class:** **MAJOR.** Op 1 **narrows** a phrase of a `consolidated baseline` claim: it
  confines *«Astrogenesi aumentata»* to the assay that carries it and records that the paper's own
  transcriptome carries neither marker. Op 2 is an addition to a second `consolidated baseline`
  claim. Per §7 of the batch protocol this file is MAJOR and is **not applied by its author**;
  blind-audit triples are below. Nothing is reversed, no evidence is demoted, and no harm endpoint
  is involved.
- **Source read:** PMID 34268881 (DOI 10.15252/emmm.202013610). Artefacts, both declared in
  `deepdive_manifests/PMID34268881.json`, PRESENT, digests matching:
  `files/fulltext/PMID34268881_assets/EMMM-13-e13610-s006.xlsx` sha256
  `83857ec6006928d9810f7a4c284b93b04266792fce38d960e21731f72f944eeb`;
  `files/fulltext/PMID34268881_assets/EMMM-13-e13610-s005.xlsx` sha256
  `82a03fc996b2ca3da0ff96032ba6a6b011458f9cf0df29a6129165bc7bed2718`;
  `files/fulltext/PMID34268881_Steinberg2021_PMC.xml` sha256
  `de340289bc6704c9b9ec752f81afed64a02211a83d95d675a1d46f40be6304f6`.
- **Receipt of the producing reading:** `FTR-20261004-34268881-07` (prepared, not recorded).

## Why

The paper reports *«a marked increase in astrocytic cells»* and quantifies it with
immunofluorescence for GFAP and S100β plus a week-20 immunoblot. An exact-symbol match over the
2,267 rows of its own two deposited differential-expression lists returns **zero rows for GFAP and
zero rows for S100B**. What the tables do carry on that axis is AQP4 +2.70 (padj 5.69e-2), SOX9
+0.51 (3.75e-2) and VIM +0.82 (4.15e-5) up, and ALDH1L1 −0.56 (6.74e-2) down — and `AQP4` occurs
**zero** times in the article body. The IF result is not contradicted; it is *unaccompanied* by the
transcriptome published beside it, and a baseline summary that says *«Astrogenesi aumentata»*
without naming the assay invites the reader to assume both.

Separately, the same tables carry `NPY` at log2FC **−6.24, padj 4.62e-15** — the strongest signal
of the 50-marker panel — and the authors never mention it. A systemic murine constitutive null
independently shows lower NPY-positive counts in the dentate gyrus. Two species, two systems, one
direction for one neuropeptide; CLAIM 005 should hold that concordance with its limits written in.

## Op 1 — CLAIM 002, narrow the astrogenesis phrase to its assay

**File:** `disease-models/wwox/registries/claim_registry_current.md`
**Record:** `CLAIM 002`
**Op:** `replace-within` the record.

`old` (verbatim, measured **1 occurrence in `CLAIM 002` and 1 in the whole file**):

```
Astrogenesi aumentata;
```

`new`:

```
Astrogenesi aumentata **per immunofluorescenza e immunoblot** (🔴 **qualificata 2026-10-04**, `CC-20261004W12-C-STEINBERG-ASTRO-01`, re-read di PMID 34268881 a receipt `FTR-20261004-34268881-07`: i due marcatori che il paper quantifica, `GFAP` e `S100B`, **non compaiono in nessuna delle due liste di espressione differenziale deposte** — zero righe su 2.267 per ciascuno, per match esatto di simbolo —, mentre le tabelle portano `AQP4` log2FC 2.70 padj 5.69e-2, `SOX9` 0.51 padj 3.75e-2 e `VIM` 0.82 padj 4.15e-5 in su e `ALDH1L1` −0.56 padj 6.74e-2 in giù, e la stringa `AQP4` compare **zero** volte nel corpo dell'articolo. Il reperto IF **non è contraddetto**: è *non accompagnato* dal trascrittoma pubblicato accanto. Limiti: RNA-seq bulk di **2 WT vs 4 KO** con difetti dichiarati di regionalizzazione, dove un non-reperto di trascritto non è un non-reperto di proteina e non separa un effetto cellulare da uno di composizione; null costitutivo, nessun trasferimento ad alcun allele missense o splice);
```

## Op 2 — CLAIM 005, record the human concordance on NPY

**File:** `disease-models/wwox/registries/claim_registry_current.md`
**Record:** `CLAIM 005`
**Op:** `replace-within` the record.

`old` (verbatim, measured **1 occurrence in `CLAIM 005` and 1 in the whole file**):

```
NPY-positive counts are lower **in DG only**
```

`new`:

```
NPY-positive counts are lower **in DG only** (🔵 **concordanza umana indipendente, aggiunta 2026-10-04**, `CC-20261004W12-C-STEINBERG-ASTRO-01`, re-read di PMID 34268881 — [[paper_registry_current#PAPER 039]] — a receipt `FTR-20261004-34268881-07`: nelle tabelle di espressione differenziale deposte di quel paper `NPY` è il segnale più forte del pannello misurato, log2FC **−6.24**, padj **4.62e-15**, e gli autori non lo menzionano mai nel corpo dell'articolo. ⚠️ **Limiti, da leggere insieme al dato:** trascritto contro conta di cellule marcatore-positive; organoide cerebrale senza risoluzione regionale, quindi nessun equivalente del DG; null costitutivo in entrambi i sistemi; **nessun trasferimento ad allele missense o splice** — non dice nulla su P47T, Q230P, G372R, A141T, P252A né su un allele accettore. Non cambia nessuna misura di questa claim e non è parere medico)
```

## What this candidate deliberately does NOT propose

- No change to the glial **cell-autonomy** statement of CLAIM 005: the organoid cannot test it
  either. Eight microglial markers (AIF1, P2RY12, CX3CR1, TMEM119, ITGAM, PTPRC, CSF1R, TREM2) are
  absent from both lists, as expected for a platform that has no microglia — an earned null about
  the platform, recorded so the IBA1 axis is not re-asked of this paper.
- No change to CLAIM 002's GABAergic marker sentence: the re-read **confirms** it at RNA-seq level
  (GAD1 +3.57, SLC32A1/VGAT +3.28 up; GABRB2 −1.78, GABRB3 −0.92 down; `SLC17A7`/VGLUT1 absent from
  both lists, i.e. not differentially expressed). `GAD2` is absent from the tables, but the landed
  wording rests on the Fig 1D **qPCR** panel — a different assay, not a contradiction.
- No myelin or oligodendroglial claim: PDGFRA +3.02 and MBP +1.41 up, with OLIG1, OLIG2, SOX10,
  PLP1 and CSPG4 absent from both lists, in a week-15 organoid. Two markers without a lineage.
- No new `PAPER`/`LIT` record: PMID 34268881 is `PAPER 039` (`claim_linked`), with `LIT-0365`.

## What would falsify it

For Op 1: a deposited GFAP or S100B row in either list (measurable: re-run an exact-symbol match
over the two `symbol` columns), or a single-cell dataset from the same organoids showing the
astroglial rise in transcript. For Op 2: an NPY row absent or positive in the same table, or a
re-analysis attributing the fall to the loss of a whole neuronal population rather than to NPY.

### LOCATOR TRIPLES FOR BLIND AUDIT

1. (The two astrocytic markers this paper quantifies by immunofluorescence are absent from both of its deposited differential-expression lists, while four other astroglial genes are present with the values given | `[spreadsheet attestation — read cell-wise from the workbook XML] An exact-symbol match over the 'symbol' column of both lists (1,246 + 1,021 = 2,267 rows) returns zero rows for GFAP and zero rows for S100B, while AQP4 appears in Table EV1 with padj 5.69E-2 and log2FoldChange 2.70, SOX9 with padj 3.75E-2 and log2FoldChange 0.51, VIM with padj 4.15E-5 and log2FoldChange 0.82, and ALDH1L1 appears in Table EV2 with padj 6.74E-2 and log2FoldChange -0.56.` | Tables EV1 and EV2, exact-symbol match over both 'symbol' columns; read cell-wise from xl/worksheets/sheet1.xml — `files/fulltext/PMID34268881_assets/EMMM-13-e13610-s006.xlsx`)
2. (The astrocytic increase is reported from immunofluorescence staining of two markers | `we used immunofluorescence staining to visualize the astrocytic markers glial fibrillary acidic protein (GFAP) and S100 calcium‐binding protein B (S100β) in week 15 and week 24 COs` | Results, astrogenesis section — `files/fulltext/PMID34268881_Steinberg2021_PMC.xml`)
3. (NPY transcript is strongly reduced in the knockout organoids and the article body never mentions it | `[spreadsheet attestation — read cell-wise from the workbook XML] Table EV2 carries NPY with padj 4.62E-15 and log2FoldChange -6.24, the lowest adjusted P value of the 50-symbol glial, GABAergic and oligodendroglial panel matched against the two lists; the string NPY occurs zero times in the article JATS body.` | Table EV2, row matched by exact gene symbol NPY; read cell-wise from xl/worksheets/sheet1.xml — `files/fulltext/PMID34268881_assets/EMMM-13-e13610-s005.xlsx`)
4. (Microglial markers are absent as a class from both lists and the oligodendroglial signal is two markers without a lineage | `[spreadsheet attestation — read cell-wise from the workbook XML] Exact-symbol match over both lists returns zero rows for AIF1, P2RY12, CX3CR1, TMEM119, ITGAM, PTPRC, CSF1R and TREM2, and zero rows for OLIG1, OLIG2, SOX10, PLP1 and CSPG4, while PDGFRA appears in Table EV1 with padj 6.55E-3 and log2FoldChange 3.02 and MBP with padj 4.46E-2 and log2FoldChange 1.41.` | Tables EV1 and EV2, exact-symbol match over both 'symbol' columns; read cell-wise from xl/worksheets/sheet1.xml — `files/fulltext/PMID34268881_assets/EMMM-13-e13610-s006.xlsx`)
5. (The GABAergic marker pattern already landed for this paper is confirmed at RNA-seq level, and GAD2 is not in the tables | `[spreadsheet attestation — read cell-wise from the workbook XML] Table EV1 carries GAD1 padj 1.22E-2 log2FoldChange 3.57 and SLC32A1 padj 4.33E-2 log2FoldChange 3.28; Table EV2 carries GABRB2 padj 3.36E-4 log2FoldChange -1.78 and GABRB3 padj 2.44E-3 log2FoldChange -0.92; exact-symbol match returns zero rows for GAD2, SLC17A7 and SLC17A6.` | Tables EV1 and EV2, exact-symbol match over both 'symbol' columns; read cell-wise from xl/worksheets/sheet1.xml — `files/fulltext/PMID34268881_assets/EMMM-13-e13610-s006.xlsx`)
6. (The comparison behind both deposited lists is two wild-type samples against four knockout samples | `These two samples were extracted from further analysis, giving a total of six samples used for further analysis.` | Materials and Methods, Library preparation and RNA sequencing — `files/fulltext/PMID34268881_Steinberg2021_PMC.xml`)

## BATCH DISPOSITION — `BATCH_20261004_006` (2026-10-04, ACTOR_ID `scientist`, Scientist P), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED

Class re-judged **MAJOR** and confirmed as such: op 1 narrows a phrase of a `consolidated baseline` claim (`CLAIM 002`) and op 2 adds to a second (`CLAIM 005`). **Blind locator audit by cell before propagation: 6 triples and 3 independent checks, by an auditor that had seen no candidate — 5 SUPPORTED, 1 NOT_SUPPORTED_AS_LABELLED.** Every cell value the candidate quoted matched the workbooks exactly, including the two zero-row nulls, which the auditor verified additionally by Ensembl ID and by alias sweep. Four framing repairs were made **at source before landing**, and they are the reason the audit was worth its cost: (1) the astrocytic increase rests on immunofluorescence **plus immunoblot plus qPCR**, not on immunofluorescence alone, so the landed narrowing names all three assays and the paper's own caveat that `GFAP` also marks radial glia; (2) the two deposited lists are cut at **raw P < 0.01**, and **370 of 2,267 rows sit above padj 0.05** — including both of the up/down comparators the narrowing cites — so their presence is not FDR significance; (3) **absence from a differential-expression list is not absence of expression**, now written into the claim and promoted to a reading rule in the working model; (4) the `NPY` datum is the strongest signal **of the marker panel interrogated**, not the lowest padj of the list, which belongs to `DACT2` — landed with that distinction explicit. `Status`, `Type` and `Summary` of both claims are byte-identical before and after; the candidate's own selection-row note (that the baseline this paper founds is `CLAIM 002`) is accepted and is what the ops reflect.
