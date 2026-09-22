# FT-125 — Targeted re-read of PMID 36537114 (Chong 2023)

**Node:** `FT125_TARGETED_REREAD_PMID_36537114` · **Actor:** Scientist A · **Date:** 2026-09-21
**Status:** non-canonical analysis file. No canonical file edited, no registry written, no receipt claimed, no
commit. **Read-only toward every canonical file. Public edition. Not medical advice.**

---

## 1 · The direct answer

**The method works, and the first thing it did was overturn two of my own Wave 5 findings.**

A targeted re-read of an already-read paper did yield material LEGEND did not hold — five new `DATO` items, §4.
But the headline result is a **source-attribution failure of mine**, caught by reading the paper's own Discussion:

🔴 **PMID 36537114 states, in its own Discussion, that all five of its patients carry null variants.** Its
Introduction says it presents five patients. **It therefore does not contain the Q230P-plus-exon-5-deletion
patient, the `GRIA4` variant, or the blood/fibroblast RNA-sequencing statement that I attributed to it in Wave 5.**
LEGEND's existing `PAPER 017` record — *"5 pazienti WOREE (tutti null/null)"* — was **right all along**, and my
Wave 5 attribution was wrong.

**The cause is an instrument defect worse than `FT-126`.** `FT-126` established that this surface deletes
characters inside variant strings. This wave establishes something further: **the surface also assembles chunks
that mix content from unrelated documents while labelling them with one article's internal IDs.** A chunk carrying
`ajmga63074-*` cross-reference markers also carried a **blood-donation logistic-regression table** — *"Number of
days to donate after prior donation"*, `Importance / Courtesy / Phlebotomist / Discomfort`. That content is not in
a WWOX case series. **Passage-ID matching is therefore not a safe attribution method on this surface**, and that is
precisely how I attributed N-33 and N-35 in Wave 5.

So: **Task 3 is answered in the negative** (the genotype is not in this paper), **Tasks 1 and 2 concern a different
paper** and were never about this one, and **Task 4 succeeded** — the re-read is where the real yield is.

🔵 **The principle the wave was testing survives, with a caveat that makes it stronger.** A receipt does record
only that a paper was read, not that everything was extracted — the re-read proved that by finding five new items.
But the same wave shows the complementary rule: **a finding surfaced while working a different node inherits that
node's attribution risk**, and must be re-attributed before it is used.

---

## 2 · Surfaces and depth, declared per item

| Surface | What it is | Depth | Used for |
|---|---|---|---|
| **`PAPER 017` / `LIT-0017`** in LEGEND | registry records, `Evidence depth: partial full text (Scholar Gateway, 47 chunk — non open access)` | 🟢 read directly | §3, §5, §6 |
| **Receipt `FTR-20260726-36537114-01`** | `evidence_depth: partial_fulltext_read`, `record_kind: legacy_reconstruction`, **every coverage field `unknown_legacy`**, `source_fingerprint: null`, `analysis_at: null` | 🟢 read directly | §6 — this matters more than it looks |
| **Dossier / manifest** | 🔴 **NEITHER EXISTS.** No `fulltext_dossiers/PMID36537114*`, no `deepdive_manifests/PMID36537114*` | — | the absence is itself a finding (§6) |
| **Scholar Gateway passages** | one targeted query, 14 results; **2 chunks carry `ajmga63074` cross-reference IDs** (the target's DOI suffix) | 🟡 corpus-passage depth, **and contaminated** (§1) | §4, with every item's risk stated |
| **PubMed metadata** | `get_article_metadata`, `get_copyright_status` | 🟢 | DOI verification (§8) |

🔴 **No PMC body exists** (verified by the coordinator: no PMCID, `found_in_pmc: 0`, © 2022 Wiley Periodicals LLC).
**This wave did not re-establish that**, per instruction. **Nothing below is a reading of the published article's
full text**; the deepest surface available is a contaminated corpus passage.

---

## 3 · Tasks 1, 2 and 3 — three negatives, and why each is a result

### Task 1 — the heterozygous Q230P brother: **not this paper. Different cohort, still unidentified.**

🔴 **I must correct the brief before answering it.** My Wave 5 file attributed this to *"an Epileptic Disorders
cohort paper"* with identity *"INFERRED from the passage-ID scheme (`epd212565`) only — not verified"*, explicitly
**not** to PMID 36537114. Wave 6's brief bundles it with the Chong re-read. **They are different papers**, and
conflating them would put a sibling observation into the wrong cohort — the §12 error this node exists to prevent.

**What the surface shows about that other paper** (reported without stacking identifying attributes, per the
de-identification rule): it is a **nine-patient cohort drawn from six families in a single country**, all with
homozygous WWOX variants, compared against 61 literature patients from 19 studies. Four homozygous variant classes
are represented; one patient carries the Q230P missense. The passage about the sibling reads that the brother of
that patient carried the same variant in the **heterozygous** state, was **labelled a carrier**, had a clinical
presentation described as similar to his brother's, **died at 10 years**, and that further testing was underway to
determine whether a second, compound-heterozygous allele exists.

**Tag: `IPOTESI`, and deliberately the weakest tag available.**
⚠️ **The most likely explanation is a missed second variant, not a modifier — and the paper says so itself**: the
authors state that testing is underway precisely to look for one. A heterozygous carrier with a severe
recessive-disease phenotype is, in the overwhelming majority of cases, an incompletely genotyped compound
heterozygote. **It must not be read as evidence against Wave 4's negative** (no discordant sibling pair), because
it is not a discordant pair on a shared genotype — it is a pair whose genotypes are *reported as different* and one
of which is *suspected to be incompletely characterised*.
🔴 **It is not resolvable here.** The source is unidentified: `WWOX WOREE syndrome nine patients cohort` and
`WWOX WOREE syndrome cohort Epileptic Disorders nine patients` return **0 and 1** records respectively, and the one
is **PMID 30356099 (Piard 2019, *Genet Med*, 20 patients / 18 families)** — **not** this cohort. **Identification
is the prerequisite, and it failed.** Recorded as an open acquisition item, not as a finding.

### Task 2 — `GRIA4`: **attribution withdrawn; the finding is now unanchored.**

**N-35 as filed in Wave 5 is withdrawn as an attributed finding.** The text describing a *de novo* likely-pathogenic
intronic `GRIA4` variant predicted by multiple algorithms to activate a cryptic acceptor sat in an
`ajmga63074`-tagged chunk — but so did the blood-donation table (§1), and the paper's own Discussion excludes the
patient that text describes (§3, Task 3).

**Supporting but non-decisive:** `GRIA4 WWOX` → **0 records in PubMed**. ⚠️ **This is weak evidence and I will not
lean on it**: PubMed indexes titles, abstracts and MeSH, **not body text**, so a body-only co-mention would not
appear. The zero is *consistent with* non-membership; it does not establish it.

**What remains true and worth keeping:** `GRIA4` appears **nowhere in this repository** (repo-wide scan). If the
observation is real in *some* paper, it is the nearest thing this session has found to an oligogenic modifier
candidate in a disease of pharmacoresistant epilepsy, and `GRIA4` encodes an AMPA-receptor subunit — **which is
exactly why it must not be scored from a contaminated surface.** ⚠️ The brief's own warning applies and was
correct: *"a predicted cryptic acceptor is a prediction"*. **Tag: `IPOTESI`, unanchored, source unknown.**

### Task 3 — the Q230P + 36.3 kb exon-5 deletion genotype: **not in this paper.**

**`DATO`, from the target's own Discussion:**

> *"All WWOX variants in these five patients are predicted to be null, consistent with the proposed mechanism of WOREE syndrome."*

and from its Introduction:

> *"In this study, we present five pediatric patients with WOREE syndrome."*

A `p.Gln230Pro` missense allele is not null. **Five patients, all null ⇒ no Q230P patient in this cohort.** The
paper's only engagement with Q230P is as **literature**, citing Johannsen 2018 and Weisz-Hubshman 2019 (§4, D-3).

⇒ **The genotype cannot be added to the allelic series from this source. Where it actually comes from is
unresolved**, and is now an open item rather than a held fact.

---

## 4 · Task 4 — what this surface holds that LEGEND does not

Five items. Each tagged, each with its risk stated. **All five come from the two `ajmga63074`-tagged chunks and
therefore carry the contamination risk of §1** — but unlike the withdrawn items, each is *internally consistent
with the paper's declared cohort* (five patients, all null, no distinctive dysmorphism), which is the only
attribution check available.

| # | Item | Tag | Status |
|---|---|---|---|
| **D-1** ⭐ | **The cohort is explicitly all-null**, stated as a conclusion, not a table entry: *"All WWOX variants in these five patients are predicted to be null, consistent with the proposed mechanism of WOREE syndrome."* | **`DATO`** | Confirms `PAPER 017`; **new as a quotable sentence** — LEGEND held the fact, not the source statement |
| **D-2** ⭐ | 🔴 **A negative on facial dysmorphism, and it contradicts another paper in LEGEND's corpus:** *"In contrast, none of our patients showed distinctive facial features."* — against Havali/Piard's 12 of 20 (60%), and against **PMID 30853297's** claim to be *"the first detailed description of patients harbouring a splice-site variant"* with dysmorphism as an expansion of the phenotype. The paper's own conclusion: *"it is important to remark that dysmorphic features and scoliosis may not always be present in patients with WOREE syndrome."* | **`DATO`** (the observation) + **`INFERENZA`** (the tension) | **NEW.** LEGEND's `PAPER 017` note does not carry it. **Directly relevant to FT-117**: the paper LEGEND cannot read is the one claiming dysmorphism as a phenotype expansion, and here is a contemporaneous cohort reporting its absence |
| **D-3** 🔴 | **The paper reproduces the Q230P transcript/protein result — and renders the residue number differently from every other source in this repository.** The sentence attributes to Johannsen 2018 that patients homozygous for the variant showed normal WWOX transcript levels but absence of WWOX protein in fibroblasts. ⚠️ **The residue number as it appears on this surface is `239`, not `230`.** I cannot determine whether that is a typographical error in the published paper or an extraction artefact, **so per the quotation rule the token is not quoted** and the sentence is paraphrased. | **`DATO`** on the biology (LEGEND holds it independently via `CLAIM 019`/`CLAIM 030`); **token UNRESOLVED** | **NEW as a defect.** Whatever its origin, a published or extracted `Gln239Pro` for `Gln230Pro` is exactly the `+5`→`−3` class. ⚠️ **Anyone searching the literature for `Gln239Pro` would find a phantom allele; anyone searching for `Gln230Pro` would miss this citation.** |
| **D-4** | **Pancreatitis, with three details LEGEND does not hold.** LEGEND's `PAPER 017` note records *"pancreatite ricorrente"* only. The surface adds: it **resolved 18 months after onset**; it was judged unrelated to antiepileptic medication because *"pancreatic enzymes were persistently elevated and did not resolve with change of anticonvulsant medications"* and the patient *"was never treated with sodium valproate"*; and *"No variants in genes associated with hereditary pancreatitis were ascertained by genetic testing."* | **`DATO`** | **NEW.** The valproate exclusion and the negative pancreatitis-gene panel are what make this a candidate phenotype expansion rather than a drug effect. The authors' own mood is cautious: *"It is not known whether this feature will become a key feature within the clinical spectrum"* |
| **D-5** | **Scoliosis is also under-represented**: *"While scoliosis or kyphosis was present in 13 of 20 (65%) patients reported by Piard et al., only two of our patients developed mild scoliosis."* | **`DATO`** | **NEW** to LEGEND's record of this paper |

### Items explicitly NOT found on this surface — empty extractions, reported as results

| Sought | Result |
|---|---|
| **Any WWOX protein or transcript measurement performed by these authors** | 🔴 **None.** The only transcript/protein statement is **cited to Johannsen 2018** (D-3). This cohort measured no WWOX protein and no WWOX transcript of its own |
| **A named ASM response beyond what LEGEND holds** | 🔴 **Nothing new on this surface.** LEGEND's `PAPER 017` note already carries the ketogenic-diet 3/5 result and the vigabatrin detail; the chunks retrieved this wave did not reach the treatment tables |
| **Any age, death or follow-up datum** | 🔴 **None reached.** The patient table was not in the retrieved chunks. **This is a retrieval limitation, not evidence of absence** |
| **Family identifiers usable for §12** | 🔴 **None.** No family numbering, no recruitment window, no per-patient identifiers on the retrieved chunks |

---

## 5 · §12 — Cohort overlap, extending Wave 5 rather than rediscovering it

**What is resolved.**
- **This cohort is all-null (D-1).** It therefore **contributes nothing to the Q230P denominator**, and Wave 5's warning that `DL-MOL-012`'s *"8 cases"* has a re-reporting hazard inside it is **narrowed, not widened**: PMID 36537114 is not one of the contributors. That is a small but real tightening.
- **My Wave 5 claim that this paper carries a Q230P compound heterozygote is withdrawn** (§3, Task 3), so no spurious Q230P patient enters the count.

**What remains unresolvable from here, stated as unresolvable.**
- **Whether Chong's five patients overlap any other series.** The author affiliations span Baylor, CUHK and the Undiagnosed Diseases Network, but **affiliation is not recruitment site**, no recruitment window was retrieved, and no patient-level identifiers were reached. **No independence claim may be made in either direction.**
- **Whether the unidentified nine-patient cohort behind Task 1 overlaps anything LEGEND holds.** It cannot be checked until the paper is identified. It reports **61 literature patients from 19 studies** as its comparison set — meaning it is itself an aggregator, and **any count taken from it would double-count** unless its literature set is enumerated.
- **Where the Q230P + exon-5-deletion patient actually comes from.** Now an open question rather than an answered one.

🔴 **The hazard compounds.** Wave 5 established that these series re-report one another. This wave adds: **an
aggregating cohort that tabulates 61 previously published patients alongside its own nine is a re-reporting engine**,
and summing it with the primaries it aggregates would double-count by construction.

---

## 6 · What LEGEND already knew, separated from what is new

**Already held — and `PAPER 017` was right where I was wrong:**
- *"5 pazienti WOREE (tutti null/null)"* — confirmed by D-1.
- The ketogenic-diet result (3/5), the vigabatrin detail, the lactate value, recurrent pancreatitis as a headline, sensorineural deafness, and the visual-deficit recommendation.
- *"Q230P/SDR: trascritto normale ma proteina assente/instabile"* — held, and correctly attributed by LEGEND to the underlying Johannsen result rather than to this paper.
- The DOI `10.1002/ajmg.a.63074`.

**New this wave:**

| # | Finding |
|---|---|
| **N-39** 🔴 | **The corpus surface assembles chunks that mix unrelated documents under one article's internal IDs** — a blood-donation regression table inside an `ajmga63074`-tagged chunk. **Passage-ID matching is not a safe attribution method.** This is strictly worse than `FT-126`, which concerned characters inside strings; this concerns **whole passages** |
| **N-40** ⭐ | **D-2** — an explicit cohort-level negative on facial dysmorphism and scoliosis, in tension with the dysmorphism claim of the paper FT-117 cannot acquire |
| **N-41** 🔴 | **D-3** — a `Gln239Pro`/`Gln230Pro` residue-number discrepancy on a published-literature citation, origin undetermined, creating a phantom allele for anyone searching by HGVS |
| **N-42** | **D-4, D-5** — the pancreatitis qualifiers (18-month resolution, valproate never given, negative hereditary-pancreatitis panel) and the scoliosis under-representation |
| **N-43** | **D-1** as a quotable source sentence for the all-null cohort composition |
| **N-44** | **The receipt for this paper is a `legacy_reconstruction` with every coverage field `unknown_legacy`, `source_fingerprint: null` and `analysis_at: null`, and there is no dossier and no manifest.** ⚠️ **This is the class of receipt most likely to hide unextracted material** — it records that a read happened without recording what was covered. A targeted-re-read sweep, if one is run, should be prioritised by exactly this signature |

---

## 7 · Corrections

| # | Standing text | Correction | Basis |
|---|---|---|---|
| **C-1** 🔴 | **My own Wave 5 `N-33` and `N-35`**, attributing the blood/fibroblast RNA-sequencing statement and the `GRIA4` variant to PMID 36537114 on the basis of `ajmga63074` passage IDs. | **WITHDRAWN as attributed findings.** The paper's own Discussion states all five of its patients carry null variants (D-1), which excludes the Q230P compound heterozygote that text describes; and the same ID-tagged chunks carry content from an unrelated blood-donation study (N-39). **The attribution method was unsound.** The observations may still exist somewhere; they are no longer anchored to a paper. | this wave |
| **C-2** ℹ️ | **The brief** bundles Task 1 (the heterozygous brother) into the Chong re-read. | **Different paper.** My Wave 5 file placed it in an *Epileptic Disorders* cohort with identity explicitly unverified, not in 36537114. Recorded so the sibling observation is not filed into the wrong cohort. | Wave 5 file; this wave |
| **C-3** ✅ | **The coordinator's adjudication of N-33** — using `CLAIM 019` (Johannsen: WWOX transcript measured at normal levels in patient fibroblasts) to conclude the truncated sentence concerns another gene, leaving `DL-BIO-003` and `HYP-20260709-08` standing. | **The conclusion stands and is now doubly safe.** It was already correct on LEGEND-internal evidence; it is now additionally the case that **the sentence's provenance is unknown**, so it never had standing to threaten those experiments. **The experiments are not at risk.** | this wave |
| **C-4** ⚠️ | Any future use of the Scholar Gateway surface. | **`FT-126` should be widened.** It currently prohibits quoting **variant coordinates** from this surface. On N-39 the prohibition needs a second limb: **no content may be attributed to an article on the basis of its passage/cross-reference IDs alone.** Attribution requires an independent check — the article's own declared cohort, or a second surface. | this wave |
| **C-5** ℹ️ | LEGEND's `PAPER 017` and its `partial_fulltext_read` receipt. | **`PAPER 017`'s substance is confirmed, not corrected** — its all-null cohort description is right. What is incomplete is coverage: D-2 through D-5 were available on the same surface class and were not extracted. **The record is accurate; the extraction was partial, exactly as the receipt declares.** Flagged for re-read completion, not edited. | this wave |

---

## 8 · Declaration

Author: **Scientist A**. Date: **2026-09-21**. **READ-ONLY** toward every canonical file, registry, ledger and
queue: nothing was edited, no registry record created or amended (C-5 flagged only), no receipt recorded, no commit
candidate produced, no git operation performed. This file is the single file written.

🔴 **Public edition compliance.** No contact details and no identifying information of any living person. **The
de-identification rule for this wave was applied actively:** the nine-patient cohort in §3 is described by
**family and patient counts only**. Its per-patient table — which stacks country, ethnicity, age, sex,
consanguinity and clinical findings on single rows — **was retrieved and is deliberately not reproduced here, in
whole or in part**, because that stack is how a de-identified record becomes identifying. Ages are given only
where they are already load-bearing in LEGEND and only in isolation from the other attributes.

**Not medical advice.**

**Declared limits.** 🔴 **Nothing in this file is a reading of the published full text of PMID 36537114**; there is
no PMC body, and the deepest surface available is a corpus passage now shown to be **contaminated** (N-39). Every
`DATO` in §4 carries that risk and is marked. **D-3's residue number is unresolved and deliberately unquoted.**
The Task-1 source is **unidentified**, so nothing from it is scored. The Task-2 `GRIA4` observation is
**unanchored**. Empty extractions in §4 are reported as **retrieval limitations, not as evidence of absence** — the
patient table and treatment tables were simply not in the retrieved chunks. The `GRIA4 WWOX` → 0 census is **weak
evidence only**, because PubMed does not index body text. No figure panel was inspected.

*Article metadata retrieved from **PubMed**; passages via **Scholar Gateway**.*

**DOIs — verified on two routes each, per `FT-126`** (`get_article_metadata.identifiers.doi` and
`get_copyright_status.available_at.doi_url`; the converter was not relied on):
[36537114](https://doi.org/10.1002/ajmg.a.63074) ·
[30853297](https://doi.org/10.1016/j.ejpn.2019.02.003) ·
[30356099](https://doi.org/10.1038/s41436-018-0339-3) *(DOI from `get_article_metadata` this wave; second-route confirmation not run — flagged rather than asserted as verified)*.

**Deliberately not cited with a DOI:** the *Epileptic Disorders* cohort behind Task 1 — **identity unverified**,
and PubMed queries this wave failed to resolve it.
