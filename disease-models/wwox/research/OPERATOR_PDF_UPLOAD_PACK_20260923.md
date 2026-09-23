# Operator PDF upload pack — 2026-09-23

**Actor:** Orchestrator · **Class:** operator-facing acquisition packet · **Session:** consolidation + audit

> 🔴 **Non-canonical operational artefact.** READ-ONLY toward the four scientific current files, every
> registry, every queue, the receipt ledger and the state manifest. Nothing promoted. No `BATCH_COMMIT`.
> No receipt claimed. 🔴 **Nothing here is medical advice.** 🔵 **Public edition** — genotype-class level only.
> Bibliographic metadata retrieved from **PubMed / PubMed Central**.

---

## § 1 · The rule this pack obeys

**No item enters this pack because a receipt says `partial`.** Every item below was checked against the
ledger's **coverage union across all its receipts**, not against its worst single receipt. Seven
candidates proposed to this session were **removed by that check** — see § 4.

Ranked by `scientific consequence × present blockage × P(one upload closes the question)`.

---

## § 2 · The pack — 7 items

### 1 · `PMID 36779245` — **`TABLE S1` only, not the article**
*Oliver KL et al. 2023, "Harnessing gene expression networks to prioritize candidate epileptic
encephalopathy genes", **Epilepsia*** · [DOI](https://doi.org/10.1111/epi.17542) · `PMC10952634`

| Field | Value |
|---|---|
| **Exact missing surface** | 🔴 **Supplementary Table S1** (and `Supplementary Material S1`). **The article body is already read.** |
| **Current evidence depth** | body `complete` (~31,000 chars, Table 1 and the genotype-class denominators included) |
| **Why LEGEND needs it** | The body states *"We stratified all 75 cases into one of three genetic groups: (1) null/null (= 45), (2) null/missense (= 15), (3) missense/missense (= 15)."* **The 13 new patients are in Table 1; the other 62 are in `TABLE S1`** — named in the body and not in it. |
| **Question unlocked** | 🎯 **Does `CLAIM 033`'s "≥1 missense" survival advantage survive removing `Q230P`?** Direction is genuinely unpredictable: removing `Q230P` removes the class's **longest survivor** (23 y 11 m, a censored observation anchoring the right tail) **and at least two of its deaths**. `CLAIM 033` is the most directly prognostic statement in the model. |
| **Normal PDF sufficient?** | 🔴 **NO — the article PDF is useless here.** Needed: the **supplementary file** (`.docx`/`.xlsx`/`.pdf`) from the Epilepsia article page. |
| **Extract** | per patient: both alleles · genotype class as the authors assigned it · age at last follow-up or death · alive/dead · any family identifier permitting overlap resolution |

⚠️ §12 applies: Oliver's 75 = 13 new + 62 from the literature, which **contains** the 2021 census's 56 and
Piard's 20. **These cohorts re-report each other and must never be summed.**

> **Why this is #1 and the paper is open access:** the article is OA, so nothing about the *paper* is
> blocked. The supplementary payload is simply **not on the PMC surface**, and this was measured rather
> than assumed — Scholar Gateway chunks article bodies, and every supplementary index retrieved came
> back as *a list of filenames with no contents*.

---

### 2 · `PMID 29808465` — full body, and above all the Western blot
*Johannsen J et al. 2018, "Excessive seizure-induced neuronal damage …", **Neurogenetics** 19(3):151–156*
· [DOI](https://doi.org/10.1007/s10048-018-0549-5) · **no PMCID** (verified twice, 2026-09-21 and today)

| Field | Value |
|---|---|
| **Exact missing surface** | **Full body**, and specifically: the **Western blot figure + legend**, the **antibody and its epitope range**, the **loading control**, how much wild-type lysate was loaded alongside, and any statement of **assay sensitivity** |
| **Current evidence depth** | 🔴 **`abstract_only`** — every other coverage field `unavailable` |
| **Why LEGEND needs it** | This is the source of the `Q230P` *"protein not detected"* datum, and therefore of `CLAIM 019` and half of `CLAIM 030`. `CLAIM 030` carries `PREMISE: DETECTION_FLOOR` — **not detected is not absent, and the floor has never been measured.** |
| **Question unlocked** | 🎯 **Does `Q230P` leave a protein pool below the assay floor?** This decides **whether `TX-003` has anything to act on at all.** |
| **Normal PDF sufficient?** | 🟢 **YES** — the publisher PDF carries the blot and its legend |

🔴 Springer, no PMCID, absent from the Scholar Gateway corpus under three independent framings, and
citation-chaining returned a decisive negative (the field's leading review does not reproduce Johannsen's
buffer, antibody or HEK293 result, and records the `Q230P` mechanism as *unknown*). **Institutional access only.**

---

### 3 · `PMID 33914858` — the founding primary of a `consolidated baseline` claim, with **no receipt of any kind**
*Repudi S et al. 2021, "Neuronal deletion of Wwox, associated with WOREE syndrome, causes epilepsy and
myelin defects", **Brain** 144:3061–3077* · **no PMCID**

| Field | Value |
|---|---|
| **Exact missing surface** | **Full body — as a text surface that is not silently corrupt** |
| **Current evidence depth** | 🔴 **NO RECEIPT EXISTS.** Confirmed today against the ledger by `study_id`: zero records. |
| **Why LEGEND needs it** | It is the **primary source of `CLAIM 003` (`consolidated baseline`)** — non-cell-autonomous hypomyelination from neuronal `Wwox` deletion. The claim is consolidated; its source has never been read to receipt depth. |
| **Why the existing copy cannot be used** | 🔴 The reading was **suspended 2026-08-09 for surface invalidity, not for budget.** Deterministic extraction returns `Results were considered significant when P 5 0.05` where the page **prints** `P < 0.05` (proven by rendering p. 5 at 600 dpi). Document-wide: **zero occurrences of `<`, `>`, `≤`, `≥`** against 14 of `P 5 0.0…`. `fitz`, `pdfplumber` and `pypdf` **all three agree on the wrong character**, so cross-checking two extractors does not detect it. |
| **Normal PDF sufficient?** | 🟡 **A DIFFERENT PDF, or preferably the publisher HTML.** Re-downloading the same file may carry the same defect in its text layer. 🎯 **Best single ask: the Oxford Academic HTML full text** (saved page or print-to-PDF from the browser), which bypasses the embedded text layer entirely. |

---

### 4 · `PMID 30853297` — the only **measured** WWOX splice transcript in the repository
*Weisz-Hubshman M et al. 2019, **Eur J Paediatr Neurol*** · **no PMCID** (verified today) · Elsevier

| Field | Value |
|---|---|
| **Exact missing surface** | **Full body** — Methods and Results for the transcript assay |
| **Current evidence depth** | 🔴 **No receipt in the ledger**, despite an analysis file existing |
| **Why LEGEND needs it** | It carries a **measured exon-6 skip** for `c.517-2A>G` — the **only** measured WWOX splice transcript the repository names — **and** it is a second `Q230P` primary |
| **Question unlocked** | How was the skip demonstrated, **on what tissue**, with what controls, and what exactly is the **1:177 carrier-rate denominator**? This is the closest published precedent for the assay design the reference acceptor-site allele needs |
| **Normal PDF sufficient?** | 🟢 **YES** |

🔴 **Do not substitute Yang 2019's second-hand table — it mis-transcribes the missense allele.**

---

### 5 · `PMID 17470496` — the SCAR12 imaging primary, currently read through a secondary that contradicts it
*Gribaa M, Salih M, Anheim M, … Koenig M, 2007, **Brain*** · [DOI](https://doi.org/10.1093/brain/awm078)
· **no PMCID at all** (verified today)

| Field | Value |
|---|---|
| **Exact missing surface** | **Full body + the MRI figures** |
| **Current evidence depth** | 🔴 **Abstract only; `SOURCE_BLOCKED`.** Sibling-attested everywhere it is used |
| **Why LEGEND needs it** | It is the **sole imaging source for the SCAR12 (ataxia) pole** of WWOX disease |
| **Question unlocked** | 🎯 **A live primary-versus-secondary contradiction, running in two directions at once.** Aldaz & Hussain 2020 § 3.1 says *"Mild cerebellar atrophy … in MRI of **two** affected children."* Gribaa's **own abstract** says MRI *"of **ONE** patient revealed … **POSTERIOR WHITE MATTER HYPERINTENSITIES**."* The secondary differs on **the patient count** *and* **the named finding** — and posterior white-matter hyperintensity **is not a cerebellar finding at all**. ⇒ **Any statement that the SCAR12 pole shows cerebellar atrophy on imaging currently rests on a secondary its own primary's abstract does not match.** |
| **Normal PDF sufficient?** | 🟢 **YES** — but the **figures must be legible**, since the imaging is the point |

---

### 6 · `PMID 39868255` — a **free preprint** this deployment physically cannot reach
*"Partial Wwox Loss of Function Increases Severity of Murine Sepsis and Neuroinflammation"* ·
[DOI](https://doi.org/10.1101/2025.01.17.633677) · `PMC11761808`

| Field | Value |
|---|---|
| **Exact missing surface** | **Full body** |
| **Current evidence depth** | 🔴 **Abstract only.** Re-measured **first-hand today**: the `PMC11761808` deposit returns `full_text: ""` |
| **Why LEGEND needs it** | Partial (not complete) `Wwox` loss of function + **neuroinflammation and gliosis** — a hypomorph-adjacent CNS phenotype, on an axis the repository holds open |
| **Classification** | 🔴 **`NETWORK_BLOCKED`, NOT a literature dead end.** Four routes exhausted: PMC body empty · bioRxiv `.full` **egress-blocked** · Europe PMC REST **CONNECT tunnel 403** · Scholar Gateway `NO MATCH`. 🔴 **Re-verified today: ALL direct outbound HTTPS fails, including the `example.com` control.** This is a deployment allowlist, not a property of the paper |
| **Normal PDF sufficient?** | 🟢 **YES — and it is FREE.** One tap on the bioRxiv page |

> 🎯 **Lowest-effort item in the pack.** It costs the Operator nothing and cannot be closed autonomously
> here at any price. A deployment with bioRxiv egress closes it in one act and this item disappears.

---

### 7 · `PMID 25411445` — the cohort-overlap key
*Mignot C et al. 2014, **J Med Genet*** · **no PMCID** (verified today) · BMJ

| Field | Value |
|---|---|
| **Exact missing surface** | **Full body, and specifically the patient table** |
| **Current evidence depth** | 🔴 **No route ever attempted, and none exists here.** BMJ is a publisher no retrieval wave has ever sampled |
| **Why LEGEND needs it** | One of the field's **two founding WOREE cohorts** |
| **Question unlocked** | How were the genotype classes assigned, and **which patients does it share with Oliver's 62 and Piard's 20**? `FT-122` §12 forbids summing cohorts that re-report each other — **and item 1 of this pack cannot be safely analysed without it** |
| **Normal PDF sufficient?** | 🟢 **YES** |

🔵 **Pairs with item 1.** Table S1 gives the rows; Mignot decides which rows are double-counted.

---

## § 3 · If only three can be uploaded

`36779245 TABLE S1` · `29808465` · `33914858`.

They close, respectively: the **prognostic** claim's denominator, whether the **`TX-003` target exists**,
and the **unread founding primary of a `consolidated baseline` claim**.

---

## § 4 · Candidates REMOVED, and the measurement that removed each

🔴 **Seven items proposed for this pack do not belong in it.** Each was removed on evidence, not on judgement.

| Candidate | Measured state | Verdict |
|---|---|---|
| `PMID 17803050` | Ledger carries a **`complete_fulltext_read`** receipt (2026-08-06), **32 verified locators** (25 body, 4 table, 3 figure), zero gaps, `supplementary: not_present`. Its "licence-blocked" listing concerns **re-reads**, not the discharged debt | 🟢 **REMOVE — already solved** |
| `PMID 34747138` (Repudi Appendix) | Final receipt 2026-08-10 is **`complete_fulltext_read`** with **`supplementary: read`**. No real gap in the coverage union | 🟢 **REMOVE — already solved** |
| `PMID 25331887` | 2 receipts; **coverage union has NO real gap** (`tables: not_present`). Historical "receipt/rollup issue" **confirmed**: the debt is a rollup artefact of reading one receipt instead of the union | 🟢 **REMOVE — `RECEIPT_OR_STATE_ONLY`** |
| `PMID 34268881` | 4 receipts; union gap is **`supplementary: unavailable`** only; body/figures/tables all `read` | 🟡 **REMOVE — supplement-only, no named question depends on it** |
| `PMID 20146584` | Union has **no real gap**; `figures: captions_only`. The downgrade was **deliberate and declared** — the body was read section by section, manifest at STRICT PASS, 15 verbatim locators, and only the two figure **images** were unretrievable | 🟡 **REMOVE — the `partial` is honest bookkeeping, not missing evidence.** Exactly the case §1 forbids promoting |
| `PMID 24369382` (Mallaret 2014, `PAPER 042`) | 🎯 **`PMC3914474` exists** (verified today). The registry says "full text reviewed"; the ledger holds only a `legacy_reconstruction` with all ten fields `unknown_legacy` | 🟢 **REMOVE — `AUTONOMOUSLY_ACQUIRABLE`.** LEGEND can close this itself |
| `PMID 30619736` (`PAPER 032`) | 🎯 **Body retrieved first-hand today** via `PMC6300487` — full Methods, Results, both tables, Discussion | 🟢 **REMOVE — `AUTONOMOUSLY_ACQUIRABLE`, receipt debt only** |

---

## § 5 · What this pack deliberately does NOT ask for

- 🔴 Anything LEGEND can lawfully retrieve itself (§ 4, last two rows).
- 🔴 Low-value analogy literature that is merely unread.
- 🔴 Anything requiring laboratory material, archive custody or correspondence — those are
  `HUMAN_ASSET_OR_CUSTODY` and **no upload closes them**: `A-f4` (2021/2026 mouse AAV tissue retention);
  `lde/lde` custody at Nippon Veterinary and Life Science University; deposit requests `P-1`/`P-2`.
- 🔴 `Supplementary gene data` for `PMID 36828035`. It is a **named object** whose existence was verified
  first-hand, and it may already be the matrix `P-2` proposes asking a laboratory to deposit — but it sits
  behind the same supplementary-surface block as item 1 and is a **second-order** ask. Raise it only if
  item 1's route proves easy for the Operator.
