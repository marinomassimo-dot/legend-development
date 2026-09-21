# FT-116 cohort triage — do the eight untriaged multi-gene epilepsy cohorts change LEGEND's allele picture?

**Scientist B · 2026-09-21 · READ-ONLY toward every canonical file and every ledger.** No canonical file modified, no `BATCH_COMMIT`, no commit candidate, no receipt written, nothing committed or pushed. The class census ([[woree_therapeutic_class_census_20260921]]) is **not edited and nothing is re-ranked**; § 8 states what *would* change and by how much, and stops there.

🔴 **This is bibliographic classification for research planning. It is NOT treatment advice, NOT a recommendation, and NOT a statement about any individual.** It reasons about a WWOX-DEE genotype class assembled from published literature.

Bibliographic records and full text below are from **PubMed / PubMed Central**. DOI links are given per source.

---

## 1 · VERDICT

**MARGINALLY — and the margin is one paper.** Seven of the eight are gene-list mentions, secondary sources, or cohorts whose WWOX finding was published elsewhere; the eighth (**PMID 37583270**, 4 WWOX children, India) carries a **complete per-patient variant table** with **five WWOX alleles LEGEND does not hold, one independent recurrence of `c.790C>T` p.(Arg264Ter), and one probable recurrence of the exon 6–8 deletion** — and a sixth paper (**PMID 31618474**) reports a second, overlap-confounded occurrence of **p.(Glu17Lys)**. The single fact that decides it: **every new allele in this entire set is null-like — there is not one new missense allele across all eight papers**, so the set *strengthens* the census's central null-majority finding and leaves the 19-allele missense enumeration numerically untouched.

---

## 2 · Provenance — the JOIN, per paper, all four methods reported separately

🔴 **The task specified three check methods. A fourth is required, and it is the one that fires.** The state of a paper here is the join of **(a)** `registry_records.py get --pmid`, **(b)** `grep -rn "<PMID>" --include=*.md disease-models/`, **(c)** the receipt ledger `disease-models/wwox/registries/fulltext_read_receipts.jsonl`, **(d)** the manifest directory `disease-models/wwox/research/deepdive_manifests/` — **and (e) `discovery_ledger_current.md`, which for two of the eight records a completed full read that (a)–(d) all deny.**

| PMID | (a) registry | (b) grep `.md` | (c) receipts | (d) manifest | (e) discovery ledger |
|---|---|---|---|---|---|
| `32214227` | **NO RECORD MATCHED** | 5 files — `full_text_queue` (FT-116) · `surface_census` (`absent`) · `batch_queue` (`unmatched`, *"✎ corrected"*) · `next_node_scout` · census § gene-list table | **0** | none | **0** |
| `35715422` | **NO RECORD MATCHED** | 6 files, incl. `discovery_ledger_current` | **0** | none | 🔴 **`DL-MECH-059`, `promoted-to-CC`** |
| `37583270` | **NO RECORD MATCHED** | 6 files, incl. `discovery_ledger_current` | **0** | none | 🔴 **`DL-MECH-060`, `promoted-to-CC`** |
| `31618474` | **NO RECORD MATCHED** | 5 files (`batch_queue` *"✎ corrected"*) | **0** | none | **0** |
| `37095367` | **NO RECORD MATCHED** | 5 files, incl. `discovery_ledger_current` | **0** | none | 🔴 **1 mention — and it is a type error, see below** |
| `29390993` | **NO RECORD MATCHED** | 4 files | **0** | none | **0** |
| `33919646` | **NO RECORD MATCHED** | 3 files | **0** | none | **0** |
| `30783266` | **NO RECORD MATCHED** | 5 files | **0** | none | **0** |

### 2.1 · 🔴 Provenance defect A — FT-116's *"mai guardati"* is FALSE for two of the eight

`discovery_ledger_current.md` carries two `promoted-to-CC` leads whose sources are declared read **in full**:

- **`DL-MECH-059`** — source *"Yang et al. 2022, PMID 35715422 / PMCID PMC9205988; testo, cinque tabelle e Figura 1 **letti integralmente**. Dossier: `staging/deepdive_PMID35715422_Yang2022.md`."*
- **`DL-MECH-060`** — source *"Nagarajan et al. 2023, PMID 37583270 / PMCID PMC10690684; testo, quattro tabelle, tre figure e supplementi S1–S2 **letti integralmente**. Dossier: `staging/deepdive_PMID37583270_Nagarajan2023.md`."*

Both leads are interconnected to `[[claim_registry_current#CLAIM 031]]` and to private commit-queue candidates. **Neither dossier exists**: `disease-models/wwox/research/staging/` does not exist, and `find` locates no `staging` directory anywhere in the repository. So FT-116's measure — *"Nessuno dei 39 ha un record … non sono **non letti**, sono **mai guardati**"* — is **wrong for `35715422` and `37583270`**: both were read, analysed and promoted, and left no trace in the registry, the receipt ledger or the manifest directory. The reproducible measure behind FT-116 (registry `Status` over the 706-record seed) **cannot see the discovery ledger**, which is where these two live. That is a gap in the measurement instrument, not a defect in the papers.

### 2.2 · 🔴 Provenance defect B — `37095367` was filed as a corrigendum, which it is not

`discovery_ledger_current.md` line 1411 reads *"…dopo collegamento audit-only **del corrigendum PMID 37095367**…"*. PMID 37095367 is **not** a corrigendum: it is the primary Bayanova *et al.* 2023 WGS article. Its `batch_queue.md` row carries the marker *"✎ corrected —"*, which means *this article has a correction*, and it was read as *this article **is** a correction*. `32214227` and `31618474` carry the same marker. This is the likeliest mechanism by which a primary cohort paper drops out of triage entirely, and it is a **different failure mode** from the five recorded earlier today.

### 2.3 · What was NOT checked
`literature_tracking_log_current.md`, `paper_registry_current.md` and `inbox` were reached only through `registry_records.py` and `grep`, not read directly. `surface_census.md` independently reports `absent` for the five FT-116 rows it carries (`31618474`, `32214227`, `35715422`, `37095367`, `37583270`) — consistent with (c) and (d), and blind to (e).

---

## 3 · Retrievability — tested by fetching and measuring, never by `is_open_access`

Four bodies were fetched through the PubMed MCP `get_full_text_article` and **persisted before any analysis**. Four were left at abstract level by design (§ 4).

| PMID | Artefact | **bytes** | **chars** | **sha256** |
|---|---|---|---|---|
| `37583270` | `files/fulltext/PMID37583270_PMC_MCPtext.txt` | **52,764** | **52,224** | `0cf97dd004186ac91e5933586e12fb447b89eb2d23f1c6fd21d49323c62f926b` |
| `31618474` | `files/fulltext/PMID31618474_PMC_MCPtext.txt` | **26,045** | **26,029** | `36ee57333f2eb05f953a5e3f79e748eb0b05c631ab78e8b993666ca12f4442fe` |
| `32214227` | `files/fulltext/PMID32214227_PMC_MCPtext.txt` | **15,855** | **15,808** | `f3c8650d5314b6d8c513f2cf5c36e26d30a7487a54291e8618cf5c850e97f466` |
| `30783266` | `files/fulltext/PMID30783266_PMC_MCPtext.txt` | **356** | **356** | `e98e005bae344e066e0a24b4674bffb367331aff1402247d76a2ffdbd361b721` |

**Verbatim re-match:** 25 quoted strings were re-matched programmatically against their artefacts. **25/25 matched, 0 failed.**

### 3.1 · Instrument class, per artefact — which zeros are admissible

| Artefact | Gene symbols | Verdict |
|---|---|---|
| `PMID37583270` | **survive** (`WWOX` 5 · `ALDH7A1` 18 · `SCN2A` 13 · `ALG13` 10 · `CDKL5` 10) | Gene-token counts **are** readings here |
| `PMID31618474` | 🔴 **elided throughout.** `WWOX` **0** · `GABRA1` **0** · `PIGA` **0** · `ITPA` **0**; `KCNT1`/`SCN2A`/`CDKL5`/`AIMP1`/`KARS` = **1 each**, surviving only where they sit in roman-type headings or prose | 🔴 **`WWOX` = 0 is an instrument reading, not a negative.** Every gene attribution in § 5.2 is an inference, flagged as such |
| `PMID32214227` | mostly elided; `WWOX` **1** (survives inside a roman parenthesis), `PAX7` **0** | The one surviving `WWOX` is the decisive sentence |
| `PMID30783266` | `WWOX` elided from the title (*"WWOX-related"* → *"-related"*) | Irrelevant — the body is two sentences |

**Roman-class tokens are admissible in all four.** HGVS `c.`/`p.` strings and rsIDs survived: `PMID37583270` yields a complete `c.`/`p.` variant table; `PMID31618474` yields `p.E17K` (1), `p.W151*` (1), `p.` ×10, `c.` ×3.

### 3.2 · Unavailable, not empty
- **`PMID31618474` Supp Table 2 (*"Variants associated with EIMFS"*)** — named in the body, **absent from the extraction**. This is where the WWOX HGVS strings live. **Unavailable, not empty.**
- **`PMID31618474` Supp Table 1 (*"Phenotypic details of 135 patients"*)** — same.
- **`PMID32214227` supplementary Table 1** and the **entire reference list** — absent from the extraction. The citation identifying the separately published WWOX paper is therefore **unavailable, not absent**.

---

## 4 · Per-paper triage table

| PMID | WWOX patient present? | n | Variants named? | Already held (a)/(b)/(c)/(d)/(e) | Retrievability tested how | **VERDICT** |
|---|---|---|---|---|---|---|
| **`37583270`** [DOI](https://doi.org/10.1002/epi4.12811) | 🟢 **YES** — 4 children, table-level, all AR | **4** | 🟢 **YES — all four genotypes, `c.` + `p.`, with rsIDs** | none / 6 files / 0 / none / **`DL-MECH-060` full read, dossier missing** | **FULL TEXT** fetched + persisted, 52,764 B | 🔴 **INGEST-WORTHY — the only one** |
| **`31618474`** [DOI](https://doi.org/10.1002/ana.25619) | 🟡 **PROBABLY** — 1 patient (P93), gene attribution **inferred**, not read | **0–1** | 🟡 **one of two** — `p.E17K` named; the trans allele is *"a novel intronic deletion"*, **unnamed** | none / 5 files / 0 / none / none | **FULL TEXT** fetched + persisted, 26,045 B | **INGEST-WORTHY (conditional)** — conditional on acquiring Supp Table 2 |
| **`37095367`** [DOI](https://doi.org/10.1007/s12035-023-03346-3) | 🟡 **YES per abstract** — WWOX among *"6 novel disease gene variants"* | **≥1** | ❌ not in abstract | none / 5 files / 0 / none / 🔴 **misfiled as a corrigendum** | **ABSTRACT only** — not fetched by design | **INGEST-WORTHY** — a novel allele in a population LEGEND has zero representation from |
| **`29390993`** [DOI](https://doi.org/10.1186/s12920-018-0320-7) | 🟡 **YES per abstract** — *"pathogenic or likely pathogenic SNVs in 17 genes including … WWOX (n = 1)"* | **1** | ❌ not in abstract | none / 4 files / 0 / none / none | **ABSTRACT only** — not fetched by design | **INGEST-WORTHY (low priority)** — n = 1, panel, Korea |
| **`35715422`** [DOI](https://doi.org/10.1038/s41598-022-13974-9) | 🔴 **NOT A DEFENSIBLE WOREE PATIENT** — see § 6.1 | **0** (1 excluded) | 🟡 named in LEGEND's own ledger, not in the abstract | none / 6 files / 0 / none / **`DL-MECH-059` full read, dossier missing** | **ABSTRACT** + LEGEND's own full-read record | **ABSTRACT-SUFFICIENT** |
| **`33919646`** [DOI](https://doi.org/10.3390/ijms22084202) | ❌ **NO** — systematic review 2000–2020 over literature LEGEND already holds | **0 new** | ❌ | none / 3 files / 0 / none / none | **ABSTRACT only** — not fetched by design | **ABSTRACT-SUFFICIENT** (one phenotype datum, § 6.3) |
| **`32214227`** [DOI](https://doi.org/10.1038/s41431-020-0609-9) | ❌ **NO** — the WWOX family's data are **published elsewhere** | **0** | ❌ **no WWOX variant anywhere in this paper** | none / 5 files / 0 / none / none | **FULL TEXT** fetched + persisted, 15,855 B | **OFF-AXIS** (but see § 7.1 — it is a *pointer*) |
| **`30783266`** [DOI](https://doi.org/10.1038/s41436-019-0460-y) | ❌ **NO** — Published Erratum, 356-byte body | **0** | ❌ | none / 5 files / 0 / none / none | **FULL TEXT** fetched + persisted, 356 B | **OFF-AXIS — confirmed, closed** |

**Split: INGEST-WORTHY 4 (one unconditional, three conditional/low) · ABSTRACT-SUFFICIENT 2 · OFF-AXIS 2.**

---

## 5 · New variants and new patients

### 5.1 · `PMID 37583270` — the one real yield (FULL TEXT, persisted, re-matched)

The variant table gives all four WWOX genotypes. Transcript as published in every row: `(ENST00000566780.6)`. 🔴 **Attribution note:** the gene column was **elided by the extractor in rows 37–39**, leaving only the parenthetical transcript; **row 40 reads `WWOX` literally**. The attribution of rows 37–39 to WWOX is settled independently and decisively by the **clinical table**, which lists patients **37, 38, 39, 40 all as `WWOX`** — all four also read `Chromosome 16` and carry the identical transcript. This is a read, not an inference.

| Patient | Exon(s) as published | Genotype, HGVS **as published — not normalised** | Zygosity | Class | Already in LEGEND? |
|---|---|---|---|---|---|
| **37** | *"Exons 6 and 9"* | `c.553_566del` **p.Ala185ArgfsTer6** (rs759794876) **and** `c.1193G>A` **p.Trp398Ter** (*Novel*) | compound het | frameshift + nonsense | 🟢 **BOTH NEW.** `c.553_566` and `c.1193G>A` occur in **zero** files; `Trp398` occurs **only** in `discovery_ledger_current.md`, as an *integrity note*, never as an allele |
| **38** | *"Exons 2 and 7"* | `c.155_156del` **p.Arg52Lyster16** **and** `c.744C>A` **p.cys248Ter** (*Novel; Novel*) | compound het | frameshift + nonsense | 🟢 **BOTH NEW** — zero occurrences of either |
| **39** | *"Exons 5 to 8; Intron 5"* | `(516+1_517–1)_(1056+1_1057‐1)del` (*Uncertain*) **and** `c.517‐3c>A` (*Novel*), labelled *"Exonic deletion and 3′ splice site"* | compound het | CNV + non-canonical splice-region | 🟡 **CNV = probable recurrence** (§ 6.2); 🟢 **`c.517-3` is NEW** — zero occurrences |
| **40** | *"Exon 7"* | `c.790C>T` **p.Arg264Ter** (rs756762196, *Pathogenic*) | 🔴 **HOMOZYGOUS** | nonsense | 🔴 **ALREADY HELD — recurrence, § 6.2** |

🔴 **Nomenclature defects, flagged and NOT normalised** (binding rule: do not invent or normalise HGVS):
- **`p.Arg52Lyster16`** — no valid HGVS reads this way. It is almost certainly a mangled `p.Arg52LysfsTer16`, but *"almost certainly"* is not a transcript. **UNKNOWN as published.**
- **`p.cys248Ter`** — lowercase three-letter code; as published/extracted. **Not corrected here.**
- **`c.517‐3c>A`** — lowercase reference base, and a U+2010 hyphen rather than ASCII `-`. **Not normalised.**
- **`(516+1_517–1)_(1056+1_1057‐1)del`** — uses **two different dash characters inside one string** (U+2013 then U+2010). Whether that is the source or the extractor **cannot be determined from the artefact**.
- **`p.Trp398Ter` is classed *"missense"` in the source's own Type column.** It is a nonsense change. This corroborates, from the primary table, the integrity defect LEGEND's discovery ledger already recorded: *"p.Trp398Ter e' etichettata missense"*.
- 🔴 **The source's exon label for patient 39 disagrees with its own coordinates.** The column says *"Exons 5 to 8"*; the coordinates delete c.517→c.1056, which by LEGEND's own verified boundary map ([[missense_splice_reclassification_risk_20260921]]: *exon 6 = c.517–605*, *exon 8 ends c.1056*) is **exons 6–8**. Reported as the discrepancy it is; neither reading is adopted.

**Genotype–phenotype, all four (clinical table, verbatim codes):** epileptic-spasm onset 2–4 months; **microcephaly and cortical hypotonia in 4/4**; movement disorder in 1/4 (P40, dystonia at 8 months). Outcome: **P37 seizure-free (12 mo f/u, responded to VGB)** · **P38 seizure-free (12 mo, relapse then response to NZ)** · **P39 seizure-free (6 mo, responded to ZON)** · 🔴 **P40 — the homozygous `p.Arg264Ter` — *"FIHT, poor responder, Failed KD"*, drug-resistant epilepsy, non-ambulatory at 30 months.**

⚠️ **This is not a predictor and must not be read as one.** n = 4, follow-up 6–30 months, no uniform protocol, and LEGEND's own `DL-MECH-060` already records that this cohort *"parte dai geneticamente confermati e non conserva il denominatore"*. The observation is: **the only homozygous-null patient is the only treatment failure, and the three compound heterozygotes were all classed seizure-free.** Direction only. **Preserve the source's mood:** the paper says *"seizure-free"* at these follow-up lengths, not *"remission"*.

**Consanguinity:** cohort-wide *"history of consanguinity in 15%"* (abstract). 🔴 **Per-patient consanguinity for the four WWOX children is not in the retrievable text — UNKNOWN, not absent.**

### 5.2 · `PMID 31618474` — one patient, and the gene name is an inference

🔴 **The gene symbols are elided from this artefact (`WWOX` = 0, an instrument reading).** The assignment of **Patient 93** to WWOX rests on elimination, and is reported as an inference, not a read:

1. The **PubMed abstract record** (gene names intact) names the four novel **recessive** EIMFS genes: **ITPA, AIMP1, KARS, WWOX**.
2. The body: *"Four patients had inherited homozygous or compound heterozygous recessive variants in novel EIMFS genes"* → **Patients 88, 89, 90, 93**.
3. **P88** = ITPA (*"a recurrent homozygous variant in (p.W151\*), previously reported in a Pakistani family"*; Discussion: *"encodes inosine triphosphate pyrophosphatase"*).
4. **P89 and P90** = the two multi-tRNA-synthetase-complex genes (**AIMP1, KARS**) — Discussion: *"we implicated three genes that form part of the multi-tRNA synthetase complex (MSC); two new to EIMFS"*.
5. By elimination **P93 = WWOX**, corroborated by the Discussion's phenotype sentence: *"Reported encephalopathy cases have had DEEs with infantile spasms and Lennox-Gastaut syndrome; our patient also developed epileptic spasms."*

**What the body states about P93, verbatim:** *"We identified compound heterozygous variants in [gene] in Patient 93, a recurrent missense change (p.E17K) and a novel intronic deletion predicted to alter splicing. She had profound ID, spasticity, scoliosis and acquired microcephaly with a head circumference of 89 percentile at 6 months and <1 percentile at 6 years 9 months."*

- **`p.E17K`** — 🔴 **this is `p.(Glu17Lys)`, row 2 of LEGEND's 19-allele missense enumeration**, held from PMID 30356099 and classed **UNASSIGNABLE** by the census. See § 6.
- **The trans allele is a novel intronic deletion predicted to alter splicing, and it is NOT NAMED.** Its HGVS is in **Supp Table 2, which is unavailable**. **UNKNOWN — unavailable, not absent.**
- 🔴 **Preserve the mood:** *"predicted to alter splicing"*. No RNA was examined. This is annotation, not measurement — and it therefore does **not** create an RNA-RESCUE member.

### 5.3 · New patients — a RANGE, because overlap cannot be excluded

| Source | WWOX patients | Overlap that cannot be excluded |
|---|---|---|
| `37583270` | 4 | India, 6 centres, recruited Jan 2021–Jun 2022. The 2019 series (30356099) and the 2021 curation (33916893) both **predate** recruitment → those two are excludable. 🔴 **The 2025 registry (40875931, 50 individuals / 45 families) does not, and its artefact is gone with the container — overlap with it cannot be excluded.** |
| `31618474` | 0–1 | 🔴 **High.** Burgess recruits from **UK (34), Italy (20), USA (18)**; the 2019 Piard/Kini series draws on **Oxford (UK), Bosisio Parini (Italy), Pittsburgh (USA)**. Burgess states *"42/55 previously reported"* among its solved cases, and **its own authors call `p.E17K` "recurrent"** — i.e. reported before. P93 may be the same person as Piard's E17K carrier. |
| `32214227` · `30783266` · `33919646` | 0 each | n/a |
| `35715422` | 0 (1 excluded, § 6.1) | n/a |
| `37095367` · `29390993` | ≥1 each, **ABSTRACT-LEVEL**, allele unknown | Kazakhstan and South Korea — no LEGEND cohort from either → overlap low, but the alleles are unknown so they cannot be joined to anything |

🔴 **NEW WWOX PATIENTS FROM THIS SET: a range of 0–5, most plausibly 4–5.** No point count is defensible. The floor of 0 is formal, not likely: it requires all four Indian children to sit inside the 2025 registry *and* P93 to be Piard's E17K carrier. The ceiling of 5 requires none of that. **Add `37095367` and `29390993` and the bracket becomes 0–7, but those two are abstract-level with unnamed alleles and are not counted into any figure here.**

---

## 6 · Recurrences with alleles LEGEND already holds — the highest-value output

### 6.1 · 🔴 `c.790C>T` p.(Arg264Ter) — an independent third cohort, homozygous

| | LEGEND before | `PMID 37583270` adds |
|---|---|---|
| Count | **2 patients / 2 families** (census rank **=9**) | **+1 patient, homozygous, India** |
| Zygosity | *"homozygous / compound het"*; separately, 1 proband with R264\* + an 84,828 bp exon-6 deletion | **homozygous**, `rs756762196`, ACMG **Pathogenic** |
| Source | `33916893` (**DOS** — dossier of a secondary curation) | 🟢 **primary cohort, full text, persisted, re-matched** |
| Lever | GENE-REPLACEMENT; **READ-THROUGH candidate** (in-frame PTC) | unchanged — **but the constituency grows by 50 %** |

**Why this is the most valuable line in the file:** allele-specific therapy feasibility scales with how many patients share an allele, and `p.(Arg264Ter)` is the **only nonsense allele in the WWOX literature that would reach three reported patients**. It is also a **READ-THROUGH candidate**, and read-through is the one allele-specific lever in the census with no demonstrated members at all. ⚠️ Overlap with the 2025 registry **cannot be excluded**, so the count is **2–3 patients**, not 3.

### 6.2 · 🟡 The exon 6–8 deletion — a probable recurrence, on LEGEND's own arithmetic

`(516+1_517–1)_(1056+1_1057‐1)del` deletes **c.517→c.1056**. LEGEND's verified boundary map puts exon 6 at c.517–605 and the end of exon 8 at c.1056, and `[[missense_splice_reclassification_risk_20260921]]` already carries the in-frame **exon 6–8** deletion `c.517_1056del` / `His173_Met352del` from PMID 37974179. The census records *"Deletion encompassing exons 6–8 — **5 ALLELES**, the most frequent pathogenic CNV … by allele it outranks everything except Q230P."*

🔴 **This identification is LEGEND's arithmetic, not the paper's.** The paper labels the same row *"Exons 5 to 8"* and classes the CNV **Uncertain**. Reported as **probable recurrence, not adopted**.

### 6.3 · 🟡 `p.(Glu17Lys)` / `p.E17K` — a second report, and the source itself says "recurrent"

Census status today: **UNASSIGNABLE** (§ 2.4), *"not in a known functional domain"*, from `30356099` only, entangled in P19's triple-missense genotype *"It is not possible to determine whether one or both of these variants are the disease-causing missense variant"*. `PMID 31618474` calls it *"a recurrent missense change"* in an independent international cohort.

🔴 **This does NOT resolve it, and may not even be a second patient.** (i) The overlap in § 5.3 is real and unexcluded. (ii) Even if P93 is a second patient, the trans allele is an **unnamed intronic deletion predicted to alter splicing**, so the genotype is as unmatched as Piard's was — the missense contribution still cannot be isolated. **`p.(Glu17Lys)` stays UNASSIGNABLE.** What it gains is *independent annotation as a recurrent allele by a second group*, which is the weakest form of corroboration and is recorded as such.

### 6.4 · 🔴 `c.517-3C>A` — new, and it lands on a canonical acceptor LEGEND already reasons about
`c.517‐3c>A` is **non-canonical** (−3, not ±1/±2), exactly the ambiguity class of `c.605+5G>A` — *"a −3 change may be silent, leaky or null; nothing distinguishes them here"*. Its interest is positional: it sits **one nucleotide further into intron 5 than `c.517-2A>G`**, which is `CLAIM 018`, a **consolidated baseline**, the only recurrent splice allele for which characterised patient-derived material (two independent WOREE iPSC lines) already exists. **A minigene or patient-RNA assay built for `c.517-2A>G` would test `c.517-3C>A` at the same acceptor with the same construct.** That is a roadmap observation, not a claim; nobody has measured either.

---

## 7 · NEGATIVE RESULTS — and they are the majority

🟢 **This is the honest headline: six of the eight are gene-list mentions, pointers or secondary sources with no new WOREE patient behind them.**

### 7.1 · `32214227` — a pointer, not a source. Settled by one sentence
Full text persisted and read. The body: *"…this helped (i) to identify two novel disease genes (**WWOX** and [PAX7], both published elsewhere [refs])…"*, and the abstract: *"Two separately published candidate genes (WWOX and PAX7) were identified in this study."* 🔴 **There is no WWOX variant anywhere in this paper** — WWOX is absent from the abstract's 34-gene diagnostic list and from the body's variant discussion. The high-consanguinity WWOX family exists, but **its variant and phenotype are in a different publication**, whose citation sits in a reference list **absent from the extraction (unavailable, not absent)**. This paper is **OFF-AXIS as a source** and a **lead as a pointer** — identifying that separate publication is the actionable follow-up, and it was not attempted here because no reference list is reachable.

### 7.2 · `30783266` — erratum confirmed, closed
Body is **356 bytes, two sentences**, re-matched verbatim: *"The article has been corrected to account for one patient being investigated through genome sequencing rather than exome sequencing as originally published; thus amendments to the Abstract and Methods have been made as well as addition of the relevant authors and acknowledgment."* 🟢 **Confirmed: no variant changes, no patient added, no genotype altered.** FT-116's and the census's characterisation both hold. **Closed. Do not re-propose.**

### 7.3 · `35715422` — 🔴 the false positive this task warned about, and it is real
LEGEND's own `DL-MECH-059` records the single WWOX case as **`p.M1?` (likely pathogenic) + `p.H78Y` (VUS)**, carried alongside **a pathogenic *ATP7A* frameshift with low ceruloplasmin and a Menkes phenotype**. This fails the WOREE-patient test on two independent grounds: **(i)** the WWOX genotype is *likely pathogenic + VUS*, never *pathogenic + pathogenic*; **(ii)** a competing, fully established second diagnosis explains the phenotype. This is the same exclusion logic that removed `31353122` (monoallelic 6.8 Mb deletion, *"no pathogenic variants … in the other allele"*). 🔴 **`p.M1?` and `p.H78Y` must NOT enter the census allele table.** The abstract's own mood is preserved: WWOX *"**may be** associated with poor prognosis"*.

### 7.4 · `33919646` — a secondary source over literature LEGEND already holds
Systematic review, 2000–2020, 28 genes across 49 papers. **No new patients, no new alleles.** One datum worth a line, **ABSTRACT-LEVEL**: *"The rate of hypokinetic MD was low, and was described from the neonatal period only, with WW domain containing oxidoreductase (pathogenic variants."* (the sentence is extractor-mangled at the parenthesis; read no further into it). 🟡 That WWOX is the review's named gene for **neonatal-onset hypokinetic movement disorder** is consistent in direction with the parkinsonian presentation of the `p.(Leu239Arg)` index case — but the census already records that *"the same homozygous allele in ≥2 other children did not produce the parkinsonian presentation"*, so this **corroborates a syndrome-level association, not an allele-level one**, and changes nothing.

### 7.5 · Two more explicit negatives
- 🟢 **Not one new missense allele in the entire eight-paper set.** Every new allele is frameshift, nonsense, CNV or splice-region. The **19-allele missense enumeration is numerically unchanged**.
- 🟡 **Burgess Patient 54** had *"a heterozygous 6.8 Mb deletion that included two known EIMFS genes"* — the same size and zygosity as the Japanese West-syndrome case `31353122` that LEGEND already excluded as **monoallelic, not a WOREE patient**. Whether these are the same report cannot be determined (gene names elided). **It does not matter: heterozygous is not WOREE either way, and it is counted nowhere in this file.** Flagged only so it is not "discovered" again.

---

## 8 · What this WOULD change in the class census — stated, then stopped

🔴 **The class census is NOT edited here and nothing is re-ranked.** For the record only, and only if `37583270` and `31618474` were ingested and the overlap in § 5.3 were resolved in favour of novelty:

| Census element | Today | Would become | Confidence |
|---|---|---|---|
| `p.(Arg264Ter)` rank =9 | **2 patients / 2 families** | **3 / 3** — the only nonsense allele reaching 3; ties rank 4–5 | 🟡 conditional on 2025-registry overlap |
| Allele table rows | as published | **+5 new named alleles** (`c.1193G>A`, `c.553_566del`, `c.155_156del`, `c.744C>A`, `c.517-3C>A`), all null-like or splice-region | 🟢 high — full text, persisted, re-matched |
| Exon 6–8 deletion | *"5 ALLELES"* | **6 alleles** | 🟡 LEGEND's arithmetic, source says *"Exons 5 to 8"*, CNV classed *Uncertain* |
| `p.(Glu17Lys)` | UNASSIGNABLE, 1 source | **UNASSIGNABLE, 2 sources** — bin unchanged | 🟡 overlap unexcluded |
| **19-allele missense enumeration** | 19 | 🟢 **19 — UNCHANGED** | 🟢 high |
| Null / missense split (63/88 alleles, 25/44 individuals null/null) | as published | **direction reinforced** — 8 new alleles, **8 null-like, 0 missense**. Naively 71/96 = 74.0 % vs 71.6 % | 🔴 **the arithmetic is NOT defensible** — these denominators draw on overlapping cohorts and the census's own DEFAULT 4 forbids adding them. **Direction only.** |
| RNA-RESCUE members | **zero demonstrated** | 🟢 **still zero** — `c.517-3C>A` is unmeasured and the Burgess intronic deletion is *"predicted"* | 🟢 high |
| `TX-001`–`TX-007` ranking | — | 🔴 **NOT re-ranked. Nothing here justifies it.** | — |

---

## 9 · INFORMATION GAIN

| Axis | Verdict | One line |
|---|---|---|
| **Mechanistic graph** | ❌ **NO** | Not one measurement in eight papers. No RNA assay, no Western, no functional readout, no abundance datum. Every allele here is annotation. |
| **Therapeutic hypothesis** | ❌ **NO** | No new lever, no new target, no new mechanism. The levers are the same seven. |
| **Experimental roadmap** | 🟢 **YES** | `c.517-3C>A` sits **one nucleotide** from `c.517-2A>G` (`CLAIM 018`, consolidated baseline), the only recurrent WWOX splice allele with characterised patient-derived iPSC lines already in existence — **the same acceptor, testable with the same construct**. That is a concrete, cheap experiment this triage did not previously have. |
| **Genotype stratification** | 🟢 **YES, marginally** | `p.(Arg264Ter)` gains an independent third cohort and becomes the only nonsense allele reaching 3 patients; five new null-like alleles enter the picture; **zero new missense alleles**, which is itself a stratification datum. |
| **Intervention ranking** | ❌ **NO** | 🔴 Explicitly **NO**, and this is the honest answer. A 50 % growth in the READ-THROUGH constituency for one allele does not move a ranking built on a 44-individual denominator, and the overlap is unexcluded. **Nothing is re-ranked.** |
| **Uncertainty** | 🟢 **YES** | Two new provenance failure modes: **(A)** the discovery ledger holds completed full reads that the registry, receipt ledger and manifest directory all deny, with the dossiers gone — so FT-116's *"mai guardati"* is false for two of eight; **(B)** the `"✎ corrected"` batch-queue marker was read as *"is a corrigendum"*, which is why a primary cohort paper (`37095367`) dropped out of triage entirely. |

**Four NO, three YES.** The two NOs that matter — mechanistic graph and intervention ranking — are the ones the task said must be honest, and they are NO.

---

## 10 · DEFAULTS_TAKEN

1. **Full texts read: 4, not 2.** The budget was two. `30783266` was fetched because the task mandated confirming the erratum; `32214227` was bundled into the same call as a retrievability test and its body settled the question in **one sentence**, so it was read rather than discarded. The two *elective* reads were `37583270` and `31618474`. **Declared rather than concealed.**
2. **Which two elective reads:** chosen by WWOX-patient count × allele novelty from the abstracts. `37583270` (n = 4, the largest WWOX yield of the eight) and `31618474` (WWOX named as a **novel recessive EIMFS gene**, largest cohort, highest overlap risk with LEGEND's held cohorts). `37095367` and `29390993` were **left at abstract level despite qualifying**, purely on budget; both are flagged INGEST-WORTHY.
3. **`31618474` Patient 93 = WWOX is an INFERENCE by elimination**, because the extractor elided every gene symbol (`WWOX` = 0 is an instrument reading). Reported as inference throughout; **not treated as a read**.
4. **`37583270` rows 37–39 = WWOX is a READ**, settled by the clinical table which names WWOX literally for patients 37–40. Not an inference.
5. **No HGVS normalised.** `p.Arg52Lyster16`, `p.cys248Ter`, `c.517‐3c>A` and the dual-dash CNV string are reproduced **as published/extracted** and marked defective. `p.Trp398Ter` is left in the source's own (wrong) *"missense"* Type class, with the error named.
6. **No point count of new patients is given** — a range of **0–5** (0–7 including the two abstract-level cohorts, which are excluded from every figure). Overlap with the 2025 registry (`40875931`) cannot be excluded and its artefact is gone with the container.
7. **`35715422`'s WWOX case is EXCLUDED** on the `31353122` precedent: likely-pathogenic + VUS, with a competing pathogenic *ATP7A* diagnosis. `p.M1?` and `p.H78Y` are named here **only to record the exclusion**, and must not be counted as WOREE alleles.
8. **`p.E17K` is recorded as a second annotation, not a second patient.** The overlap between Burgess (UK/Italy/USA) and the 2019 Piard series (Oxford/Bosisio Parini/Pittsburgh) is real and unexcluded.
9. **Vigabatrin note, not a safety claim:** `37583270` P37 (compound het frameshift + nonsense) is recorded as *"FIHT, response with VGB"*. LEGEND holds `PAPER 003` (vigabatrin-associated brain-MRI abnormalities in two WWOX children, `41442931`, **abstract-level**) as a BLOCK-1 safety anchor. 🔴 **These two facts are recorded side by side and are NOT combined into any statement about risk or benefit.** Nothing here is medical advice.
10. **Nothing written outside this file** except the four artefacts under `files/fulltext/`. No receipt, no manifest, no registry edit, no commit candidate, no commit, no push. `files/` is gitignored and these artefacts will not survive the container.
