# Next scientist / node scouting — who carries the batch after Chang/NCKU

**Date:** 2026-09-20 (file dated 2026-09-21 per task) · **Actor:** Scientist B
**Mode:** READ-ONLY scouting. **No batch started. No canonical file edited. No commit candidate.
No therapy proposed.** Non-canonical analysis file; one output only.

**Method.** Author census over `corpus_seed_pubmed_20260806.jsonl` (706 records, disambiguated on
`last_name`+`initials` and re-checked on `affiliations`), cross-joined with receipt coverage from
`reading_state.md` (97 papers, 154 receipts) and with record identity via `registry_records.py`
(`--pmid` / `--id`; the two large registries were never grepped). External completion by PubMed
field-census. **Acquisition feasibility was tested, not assumed**: every candidate first-wave paper
was put through `convert_article_ids` and `get_copyright_status`. Prior art read first, not redone:
`scientist_node_scouting_20260920.md`, `chang_ncku_wave2_node_independence_20260920.md`,
`wwox_developmental_timing_audit_20260920.md`, `hnpc_differentiation_audit_20260920.md`,
`wwox_heterozygote_phenotype_audit_20260920.md`, `acquisition_packet_20260920.md`.

> 🔴 **The constraint that decides this file.** `tool_preflight.py` in this checkout reports
> `fitz`, `pdftotext`, `pdftoppm`, `pdfimages` **all absent**. The PubMed MCP server reaching the
> **PMC open-access subset** is the only reading route. A paper with no PMCID, or with a PMCID but
> `is_open_access: false`, is **not readable here by any route** — and, with no PDF tooling, not
> readable even if a PDF were supplied. This is not a footnote: it re-orders the candidate list.

---

## 0 · The finding that comes before the ranking

**Every mechanistically relevant laboratory in the WWOX field is now either saturated or
acquisition-blocked.** That is a census result, not an impression:

| Node | State |
|---|---|
| Chang / NCKU | formally saturated (this batch) |
| Aqeilan (HUJI) | 53/65 read; the **neuro arm is complete** except `PMID 33914858`, which is unreadable here |
| Aldaz (MD Anderson) | 38 papers, 8 read — but the **neuro arm is fully read** (`36828035` P47T, `30290271` GABA/microglia, `33255508`, `24369382`, `24871327`, `24932569`). The unread residue is oncology and DNA-repair |
| Suzuki / Tochigi (`lde` rat) | **exhausted** — 4 WWOX papers in *all of PubMed*, and LEGEND has read `19500159`, `31340538`, `32581702` and `17803050` |
| Richards / O'Keefe (Adelaide) | 8 of 9 unread — but **6 of the 8 cannot be retrieved** (see §1) |
| Bednarek / Kośla (Lodz) | 40 papers, ~4 read — but the developmental output is **one primary and one review** |

The unread residue of the 706-record corpus is dominated by (a) oncology, (b) Alzheimer/Parkinson
**common-variant GWAS** in which WWOX is one locus among dozens, and (c) small single-family case
reports redundant with the large WOREE cohorts LEGEND has already read (`30356099` Philippe 2019,
`36779245` Scheffer 2023 epileptology+mortality, `40875931` Gold 2025, `42193054` Falsaperla 2026).

**There is therefore no lab left whose unread corpus can carry a full batch.** The next unit of
work is necessarily either (i) a *question* node assembled across labs, or (ii) acquisition.

---

## 1 · Scoring

Columns as requested. "Readable" = PMC open-access subset, verified this session.

### 1a · Richards / O'Keefe (Adelaide) — the standing baseline candidate

| Field | Value |
|---|---|
| Corpus papers | **9 distinct** (Richards RI 9, O'Keefe LV 7, fully nested) |
| Already read | **1** — `21075834` (Drosophila WWOX in aerobic metabolism, complete read) |
| Composition of the 8 unread | **3 reviews** (`34210081`, `25595186`, `16242840`) + **5 primaries** (`26302329`, `26390919`, `23765596`, `15814586`, `16007179`) |
| **Readable (OA-verified)** | **2 of 8** — `26302329` (PMC4547717, CC BY) and `34210081` (PMC8305172, CC BY). `25595186` is in PMC but `is_open_access: false`. `16242840`, `26390919`, `23765596`, `15814586`, `16007179` have **no PMCID at all** |
| WOREE relevance | **LOW at title/MeSH level — zero of the 9 is neuro-titled.** The node is fragile-site genomics, cancer-cell metabolism and Drosophila tumour biology |
| Therapeutic leverage | Indirect. Touches the metabolic axis (`DL-MECH-020`, `HYP-20260709-01` ketogenic rationale) — but that axis's primaries are **already read** (`25012504`, `27308416`, and the human-organoid confirmation `34268881` → `DL-MECH-034`) |
| Independence | **HIGH** — independent of Chang, Aqeilan, Aldaz, Lodz |
| Life-stage fit | **POOR** — adult flies, immortalised cell lines, radiation and fragile-site assays. No developmental or perinatal readout |
| What could change in the queue | Almost nothing reachable. The two papers that justify the candidacy — `26390919` *"WWOX moderates the mitochondrial respiratory complex"* and `23765596` *"metabolic reprograming in cells"* — **cannot be opened in this environment** |
| Principal risk | 🔴 **A first wave of unreadable papers is not a first wave.** A Richards batch here is one oncology primary plus one review |

> **Verdict: DEMOTED, on acquisition, not on merit.** The Chang batch's lesson was that volume is
> not value; the Adelaide node fails one step earlier — its value is not *retrievable*. The correct
> home for `26390919` and `23765596` is the acquisition packet, not a batch.

### 1b · Bednarek / Kośla (Lodz)

| Field | Value |
|---|---|
| Corpus papers | Bednarek AK **37**, Kośla K **13** (node ≈ 40 distinct) |
| Already read | **3–4**; neuro-titled papers in the whole node: **5** |
| Developmental output, precisely | **One primary** — `31543760` hNPC shRNA transcriptome, read and audited 2026-09-20 — **one review** — `32389029` *"The WWOX gene in brain development and pathology"*, unread, **readable** (PMC7400721, CC BY-NC) — and **co-authorship** on `32581702`, already read |
| WOREE relevance | **MODERATE and narrow.** `31543760` names WOREE and SCAR12 correctly, but the hNPC audit found no migration assay, no layering readout, no allele, and an abstract-vs-Results inversion (p = 0.0626 reported as a finding) |
| Therapeutic leverage | **MODERATE, and it lives in the metabolic sub-line, not the developmental one**: `35328751` (WWOX/HIF1A → glucose metabolism, PMC8955937), `36271927` (review, PMC9691486), `33520443` (WWOX/HIF1A ↔ gestational diabetes, PMC7811782) — **all three readable and unread** |
| Independence | **HIGH, and pointed.** `DL-MECH-020` carries a standing caution that the HIF1α/WWOX branch was also worked by a group on a **serial-retraction watchlist**, so that branch *cannot* be used as independent corroboration. Lodz is the clean replacement line |
| Life-stage fit | **MIXED** — hNPC is a culture state with no developmental date (the audit is explicit); `33520443` is gestational but human-association, not mechanism |
| What could change | Independence of `DL-MECH-020`; the durability of `HYP-20260709-01` (ketogenic rationale); whether Lodz's developmental interest is a line at all |
| Principal risk | The node is **predominantly oncology**, and its two developmental items are one already-read primary and one review. **The developmental line is an isolated pair, not a coherent programme** — that is the answer to the question the brief posed |

### 1c · Suzuki / Tochigi (`lde` rat)

| Field | Value |
|---|---|
| Corpus papers | 5 · **PubMed total: 4 WWOX papers** |
| Already read | **4** — `19500159`, `31340538`, `32581702`, `17803050` |
| Genuinely unread | **1** — `33565365` (Wwox in **testicular** development / spermatogenesis; PMC8013998 but `is_open_access: false` → **not readable**) |
| WOREE relevance | **HIGHEST in the field per paper.** `DL-MECH-026` records the `lde` rat as the animal proxy of the reference genotype's splice-acceptor allele (exon-9 lesion → protein absent + audiogenic seizures in 95%) |
| Therapeutic leverage | Already extracted — `DL-MECH-027` (neurons intact, oligodendrocytes reduced, "the substrate is salvageable"), `CLAIM 038`/`CLAIM 039`, and the prenatal migration result in `32581702` |
| Independence | HIGH | Life-stage fit | **BEST in the field** — E16.5 birth-dating read at P1; PND 5–21 protein time course |
| What could change | **Nothing — the node is empty.** |
| Principal risk | n/a |

> 🔴 **Two corrections this census produced, both of the kind the Chang Wave 2 trap warned about.**
> (a) The `lde` laboratory is **Nippon Veterinary and Life Science University**, not Tokyo
> University of Agriculture & Technology as the brief states — affiliation string verified on
> `19500159`, `31340538`, `33565365`.
> (b) `PMID 38407561` ("novel splice-site WWOX variant with paternal uniparental isodisomy") carries
> a **Suzuki H of Keio University School of Medicine — a different person.** A surname-only
> independence screen would have credited it to the `lde` lab. **Disambiguate on affiliation.**

### 1d · Aqeilan (HUJI / Ohio State)

| Field | Value |
|---|---|
| Corpus papers | 65 · **read 53** |
| Neuro arm | **Complete** — `34747138`, `42422765`, `34268881`, `34634460`, `33916893`, `32300104`, `41562193`, `41984841`, `38499540`, `38355659`, `38182577`, `36572673`, `33916893` all carry receipts |
| The one gap | **`PMID 33914858`** (Repudi 2021, *Brain*, neuronal `Wwox` deletion → epilepsy + myelin defects) — primary source of `CLAIM 003`, *consolidated baseline*, and **it has never been read** |
| Acquisition | 🔴 **No PMCID** (verified). `FT-044` is **suspended** because the PDF text layer prints `P 5 0.05` where the page prints `P < 0.05` — and with `fitz`/`pdftoppm` absent in this checkout, neither extraction nor page adjudication can be run. **Unreadable here by any route** |
| Therapeutic leverage | High — it also contains the human WWOX-KO **organoid** hyperexcitability + hypomyelination result cross-linked to `CLAIM 002` |
| What could change | Removal of a second-hand dependency under a consolidated baseline claim |
| Principal risk | It is an **acquisition task (packet item A4), not a batch** |

### 1e · A non-person node — *"what must be restored, and where can it be screened?"*

| Field | Value |
|---|---|
| Papers | **3 core, all readable and unread** — `25649963`, `26302329`, `34210081` — plus `32389029` as a fourth |
| Already read anchors | `21075834` (Drosophila, aerobic metabolism) · `36828035` (P47T = WW1-domain partial LoF mouse) · `29808465` (SDR missense → complete loss of WWOX protein) · `CLAIM 035` (SDR 388–407 / L404 as the GSK3β docking surface) |
| WOREE relevance | **HIGH and direct.** The reference genotype is an SDR missense plus a splice-acceptor allele that destroys the exon-9 acceptor — i.e. **both lesions are domain-localised**, and `DL-MECH-045` already argues the splice allele yields a truncated unstable protein rather than a silent null |
| **Therapeutic leverage** | **The highest available.** `DL-MECH-021` holds, *second-hand and without a receipt*, the only in-vivo **domain-sufficiency** experiment in the entire field: in zebrafish, co-injection of mRNA for the **ADH/SDR domain alone** rescues the knockdown phenotype (n = 770). If that survives locator discipline it bears on **`TX-003`** (is stabilising an SDR missense the right lever?), **`TX-007`** (does an AAV construct need full-length WWOX, a live packaging question), and **`TX-001-bis`** (is an exon-9 truncation functionally null?) |
| **Independence** | **Three independent labs, none of them Chang, Aqeilan or Aldaz** — Tsuruwaka/Shimada (zebrafish), O'Keefe/Richards (Drosophila), plus the already-read P47T mouse from a fourth |
| Life-stage fit | **GOOD** — zebrafish 30 hpf embryos are the only *embryonic in vivo* WWOX perturbation readable in this environment. Directly answers the life-stage mismatch the Chang batch exposed |
| What could change in the queue | (1) `DL-MECH-021` promoted from `belief: medio` to receipted evidence, or removed; (2) a ready **in-vivo screening platform** for Q230P — the ledger's own proposed experiment is "express human WWOX-Q230P in the morphant"; (3) the Adelaide candidacy settled on evidence rather than on absence |
| Principal risk | Thin (3 papers) · `25649963` is a **2015 morpholino-era** study, and morpholino off-target toxicity is a known confound — mitigated but not eliminated by its independent siRNA arm and its rescue arm · the Ca²⁺ result is described qualitatively (no amplitude, frequency or latency) · `26302329` is oncology-framed and may return nothing |

---

## 2 · Recommendation

> ### The next dedicated unit of work is a **question node**, not a person:
> ### `NODE_WWOX_DOMAIN_SUFFICIENCY_AND_EMBRYONIC_PLATFORM`
> ### and it is a **SMALL TARGETED WAVE (4 papers), not a full batch.**

**Research question.** *Which part of WWOX must be restored for an intact in-vivo phenotype — and
does a non-mammalian embryonic model exist in which a specific allele of the reference genotype
could be tested?*

This wins for four reasons that follow directly from what the Chang batch taught. It can change a
therapeutic conclusion (construct scope for `TX-007`, target validity for `TX-003`) rather than
merely adding papers *(lesson 1)*. Its evidence is **independent across three labs** *(lesson 2)*.
Its central datum is currently held **second-hand and without a receipt** — the exact failure mode
the Chang chain exposed. And it is the only readable material in the corpus that sits at an
**embryonic** life stage *(lesson 4)*.

### Proposed first wave — 4 named papers, acquisition status verified this session

| # | PMID | Paper | Acquisition | What it would settle |
|---|---|---|---|---|
| 1 | **25649963** | Tsuruwaka Y, Konishi M, Shimada E 2015, *PeerJ* 3:e727 — *"Loss of wwox expression in zebrafish embryos causes edema and alters Ca²⁺ dynamics"* | ✅ **PMC4312067 · CC BY 4.0 · `is_open_access: true`** | Whether *"the ADH/SDR domain alone rescues"* is locator-verifiable — with its n, its controls and its stage — converting `DL-MECH-021` from a receipt-less holding into evidence or removing it; and whether the Ca²⁺ result is quantitative or, as the ledger suspects, qualitative only |
| 2 | **26302329** | O'Keefe LV, …, Richards RI 2015, *PLoS One* 10(8):e0136356 — *"Tumor Suppressor WWOX Contributes to the Elimination of Tumorigenic Cells in Drosophila"* | ✅ **PMC4547717 · CC BY 4.0 · `is_open_access: true`** | The **decisive cheap test of the standing baseline candidate**: whether the Adelaide *Drosophila* platform carries any neural, developmental or domain readout at all, or is purely a cell-competition oncology assay. Settles Richards on evidence instead of on absence |
| 3 | **34210081** | Lee CS, …, O'Keefe LV 2021, *Cells* 10(7):1637 — *"Molecular Biology of the WWOX Gene That Spans Chromosomal Fragile Site FRA16D"* | ✅ **PMC8305172 · CC BY 4.0 · `is_open_access: true`** | What the **two unobtainable Adelaide primaries** (`26390919` mitochondrial respiratory complex, `23765596` metabolic reprogramming) actually claim, in their own authors' words — and therefore what precise sentence and figure a human should be asked for. Turns two dead ends into a sharpened packet entry |
| 4 | **32389029** | Kośla K, …, Bednarek AK 2020, *Exp Biol Med* 245(13):1122–1129 — *"The WWOX gene in brain development and pathology"* | ✅ **PMC7400721 · CC BY-NC 4.0 · `is_open_access: true`** | Whether Lodz's developmental interest is a **line or a one-off** — the brief's own question about Bednarek — and which of the field's brain-development claims this review sources to primaries LEGEND does not yet hold |

**Optional fifth, flagged as off-node:** `PMID 42092735` (Serce Pehlevan / Tekin Orgun 2026,
*J Paediatr Child Health*, **PMC13378201, CC BY, OA-verified**) — *"WWOX Mutation as a Rare Cause of
Neonatal-Infantile Parkinsonism Mimicking a Neurotransmitter Disorder."* It does not belong to the
domain question, but it is 2026, unread, readable, and raises a **symptomatic-lever and diagnostic-
mimic** question LEGEND does not currently hold. Include only if the wave runs short.

**Explicitly excluded from the wave for cause:** `26390919`, `23765596`, `15814586`, `16007179`,
`16242840`, `25595186` (Adelaide — no PMCID or not OA) · `33914858` (no PMCID, PDF surface `SUSPECT`,
no PDF tooling) · `33565365` (PMC, not OA) · `39868255` (PMC deposit returns an **empty body** —
established in `wwox_heterozygote_phenotype_audit_20260920.md`, do not re-queue).

**Rules the wave inherits.** Five abstract-versus-Results inversions have now been found in five
different papers in this literature, one of them in `31543760` yesterday. Every paper in this wave
is read **Results-first**, and no abstract sentence is carried without its Results counterpart. The
MCP extraction strips italicised gene and genotype tokens and superscript exponents; genotype
inferences are marked, never asserted verbatim. No figure panel is inspectable in this checkout, so
no finding may rest on one.

---

## 3 · Why not the others

**Richards / O'Keefe — not because they are weak, but because they are shut.** Six of their eight
unread papers have no PMC deposit and the seventh is in PMC without an open licence. The two that
motivate the candidacy at all — the mitochondrial respiratory complex and the metabolic reprogramming
primaries — are precisely the two that cannot be opened. Their one readable primary is a *Drosophila*
tumour-cell-elimination study, and none of their nine papers is neuro-titled. They are a screening
platform whose description is unavailable; that belongs in the acquisition packet. **Wave item #3 is
designed to extract the maximum obtainable from this node without pretending to have read it.**

**Bednarek / Kośla — the developmental line does not exist as a line.** It is one primary
(`31543760`, read and audited yesterday, with a migration claim resting on GO enrichment at
FDR < 0.25 and no migration assay), one review (`32389029`, in this wave), and a co-authorship on a
paper LEGEND already holds. The rest of ~40 papers is oncology. Their genuinely interesting
independent asset is **metabolic, not developmental** — the WWOX/HIF1A trio `35328751`, `36271927`,
`33520443`, all readable — and that is named here as the **runner-up node**, because it could
repair an independence defect `DL-MECH-020` already flags (a corroborating branch on a serial-
retraction watchlist). It loses to the recommendation only on life-stage fit and on the fact that
the neural half of the Warburg question was already closed by `DL-MECH-034` (human organoids).

**Suzuki / Tochigi — nothing left to read.** Four WWOX papers exist in all of PubMed; LEGEND has
read four (including `17803050`, outside the corpus). The single unread item is about testis and is
not open access. This is the highest-value node per paper in the field and it is **empty**. Its
remaining value is not literature but the experiment nobody has run.

**Aqeilan — saturated, and the one gap is an acquisition problem.** `33914858` is the primary under
a *consolidated baseline* claim and it has never been read; but it has no PMCID, its PDF surface is
`SUSPECT`, and this checkout has no PDF tooling. Escalating it into a batch would produce a wave
that cannot start. It stays as packet item **A4**. The het×het colony question raised in the brief
was **already answered yesterday** by `wwox_heterozygote_phenotype_audit_20260920.md`, which
established the evidence state behind `CLAIM 032` across 17 sources.

**"Prenatal/developmental evidence wherever it lives" — already harvested, and its primaries are
locked.** `wwox_developmental_timing_audit_20260920.md` mapped this node one day ago. Its two
decisive primaries — `15026124` (the only developmental expression paper, four incompatible
secondary restatements, no PMC deposit) and `33914858` — are both unobtainable. What remains
readable and unread at an embryonic stage is essentially `25649963`, which is why that paper leads
the recommended wave rather than anchoring a separate node.

**"Human WOREE natural history" — not unmined.** It looked like the largest untouched body (67
unread neuro non-cancer corpus records), and it is not: the large cohorts are read (`30356099`,
`36779245`, `40875931`, `42193054`, `24369382`, `24456803`, `36537114`, `39507621`), and the unread
residue is small single-family reports plus AD/PD common-variant GWAS where WWOX is one locus among
dozens. Most of it is also Elsevier/Wiley with no PMC deposit. Low incremental value, poor
retrievability.

---

## 4 · Does it dominate?

**No. This is a close call.**

The recommendation wins on every axis the brief names — therapeutic leverage, independence,
life-stage fit, retrievability — but it wins **a small contest**. The wave is four papers, three of
them carrying a single decisive question each, and one of those (`34210081`) is a review whose
purpose is to sharpen an acquisition ask rather than to produce a claim. Its central datum, the
SDR-only rescue, is already held in the discovery ledger at `belief: medio`; a clean read would
**confirm, qualify or remove** it, which is real but incremental. Against it stands the Lodz
metabolic trio, which is the same size, equally readable, and touches the one lever a treating team
could act on today — and the choice between them is a judgement about whether domain scope or
metabolic independence matters more, not a fact the census settles.

**Therefore: this wave should not start without the operator.** Under §21d the distinction matters
exactly here — a clear dominance would license starting; a close call does not.

And the honest ordering of *all* available work puts something else first: the single highest-value
action for WOREE right now is **not a batch at all**. It is clearing `acquisition_packet_20260920.md`
— `15126504`, `15026124`, `27569545`, `24369382`, `33914858` — five papers that each sit under a
live claim and that **no automated route in this environment can reach**. One hour of institutional
access would move the model further than any wave proposed above.

---

*No canonical file was read for edit or written. No commit candidate. No batch started. No
therapeutic proposal. Sources: PubMed / PMC via the PubMed MCP server; LEGEND registries via
`registry_records.py`; corpus census over `corpus_seed_pubmed_20260806.jsonl`. Not medical advice.*
