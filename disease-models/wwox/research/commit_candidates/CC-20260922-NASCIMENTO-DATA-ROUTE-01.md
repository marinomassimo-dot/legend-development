# COMMIT CANDIDATE — CC-20260922-NASCIMENTO-DATA-ROUTE-01

**Source:** Scientist N (restarted from zero after the rate-limit loss),
`nascimento_supplement_retrieval_20260922.md`. **Every load-bearing claim independently re-verified
by the Orchestrator**, who cloned the repository and read it directly.
**Change class:** **MINOR** in edit size. 🔴 **It falsifies the premise of its own task and of two
prior repository conclusions.**
**Target:** `CC-20260922-POSTNATAL-SVZ-01` §7c(iii) (the controlled-access inference) and §7d (the
supplementary-table route) · `nascimento_accession_and_g372r_20260922.md`.
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R2.**
**Proposes:** `D-37` — *"when a paper's data are unreachable, look for the authors' code before
concluding the data are closed."*

---

## 1 · 🔴 The three supplementary DE tables were NOT acquired — and the question is exactly as open

**No table was read. No `WWOX` row is reported, in either direction.** `PREMISE: UNVERIFIED`.

**Why, and it is closed rather than a list of failures.** Eight further hosts were probed once each
and all returned **403 at CONNECT**, including `static-content.springer.com` — the correct Springer
Nature ESM host, never tried before. 🔴 **The decisive control: `example.com` and `www.google.com`
are ALSO 403.**

> **Egress here is an ALLOWLIST (GitHub, Anthropic, package registries), not a publisher blocklist.
> There is no reachable host anywhere that serves a supplementary file.**

**Enumerating more publishers or mirrors is the same block re-measured.** That closes a whole class
of future work, and it should have been established months ago.

---

## 2 · 🟢 But the premise was false: the data are OPEN, and the route is the authors' own code

`github.com/massisnascimento/ECstream` — **cloned and read by the Orchestrator directly.**
15 files across six analysis stages. `1.merging/1.merging.rmd`, verbatim:

> *"Count matrices and metadata are **downloaded from GEO** and saved in a folder named
> `matrices`."*

And `1.merging/gsm_samples.RData` — read by the Orchestrator — pairs **eighteen per-sample GEO
accessions, `GSM8002943`–`GSM8002960`** (contiguous), with eighteen sample names. 🎯 **`EC_Stream` is
one of them**, verified in the file.

**So `D1` moves from *"hours plus an access application"* to *"hours, egress being the only
blocker."*** 🔴 **And `CC-20260922-POSTNATAL-SVZ-01` §7c(iii)'s controlled-access inference is WRONG
for the count-matrix tier.** ⚠️ It may still hold for **FASTQs** — those carry germline genotype and
the study genetically demultiplexes against a 1000 Genomes VCF. **Count matrices do not.** The
inference was reasonable and it was still wrong; what made it wrong was never looking for the code.

🔵 **A second, independent route:** the repository's `README.md` names a public **CELLxGENE
collection**, `cae8bad0-39e9-4771-85a7-822b0e06de9f`. 🔴 **That object is the strictly better
target than the supplementary tables**, because it carries **per-nucleus counts** — so the
matched-abundance **dropout control becomes computable in the same object**. *The route this task was
set to pursue is the inferior of the two.*

⚠️ **All of §2 is `author-code` depth, not publisher-confirmed.** The accessions could not be
resolved — every host that would resolve them is blocked.

---

## 3 · 🔴 `WWOX` = 0 in the authors' code — and the near-miss is the more valuable half

- **`WWOX`, case-sensitive: ZERO** across all 15 files. **Verified by the Orchestrator.**
- ⚠️ **Case-insensitive returns 7 — and all seven are FALSE POSITIVES.** Verified independently: every
  hit sits inside a `data:image/png;base64` payload (`…J+ryh1wrw5kUsrw510wwOxQTLzXShL8kJv8bPxFA…`),
  and every line carrying one begins `<p><img src="data:image/png;base64,`. **A plain-text grep of an
  `.nb.html` searches base64, not content.**

> 🔴 **Had the delegate counted them, it would have reported a `WWOX` result that does not exist.
> A zero is not absence — and a non-zero is not presence.** That is a new trap and it belongs beside
> the other four.

- **Positive controls, verified present:** `LAMP5`, `SOX2`, `GAD2`, `DCX`, `PAX6`, `TOP2A`,
  `SLC17A7`, `HOPX`. The surface carries gene symbols abundantly, so the zero is a measurement.

**What the zero means, exactly:** only that `WWOX` is not among the hand-picked `FeaturePlot` marker
genes and is named nowhere in the code. 🔴 **It is NOT *"absent from Supplementary Table 4/5/6"*** —
those tables are not in the repository in any form; every DE call ends in `saveRDS()` and
`.gitignore` excludes `*.rds` — **NOT *"not tested"*, NOT *"not differentially expressed"*, and
emphatically NOT *"not expressed."***

---

## 4 · 🔴 Four filtering mechanisms sit upstream of biology — and they invert the informativeness

From the authors' own code and Methods: `filterByExpr(min.count=10, min.total.count=20)`; *"filtered
for genes expressed in at least 50% of cells"*; **`FindAllMarkers(..., only.pos = T)`** — which
excludes down-regulated genes **by construction**; and the significance threshold.

> 🎯 **For a ~6 TPM gene, filter-exclusion is the EXPECTED outcome. So presence in a DE table would
> be informative; absence would be close to uninformative.**

**This materially re-prices the whole supplementary-table plan** and should be recorded before anyone
spends effort on it: the plan's best case was always weak, and its worst case was always
uninterpretable.

---

## 5 · 🔴 A NEW hazard, specific to Supplementary Table 5

Table 5 is *"DE genes in the main dataset … the dataset comprising **all samples**."* **The authors'
merge script imports three external adult samples into the same matrix folder** — verified in
`1.merging.rmd` lines 81–91, which fetch a tarball, untar it, and move its contents into
`matrices/` alongside the study's own eighteen.

> 🔴 **"All samples" therefore includes 50–79-year-old adult cortex from a different study. Anyone
> reading a `WWOX` row out of Table 5 must NOT read it as postnatal.**

**That hazard did not previously exist in the repository's record.** Tables 4 (EC-stream dataset) and
6 (interneuron maturation) do not carry it.

🔵 **And there are FOUR DE tables, not three:** **Supplementary Table 8** — *"DE genes between
superficial and deep-layer Lamp5+ cells."* ⚠️ Its contrast is documented in the code as *"only cells
in the postnatal EC, **excluding the EC stream**"* — **so the original choice of Tables 4–6 was
correct**, and Table 8 is the wrong object for this question.

---

## 6 · ✅ The mis-attribution trap is CLOSED, by recording rather than by withholding

The delegate met the trap, **read both external accessions verbatim from the authors' code, and held
them out of its write-up under the Orchestrator's own bound**, asking for a decision rather than
acting unilaterally. **That was the correct call at its level.**

**The Orchestrator's decision: record them, under explicit attribution.** The bound existed to
prevent *mis-attribution*, not to prevent knowledge — and an unnamed hazard is the more dangerous
state, because a later reader who sees *"downloaded from GEO"* in the Methods will go looking and
attribute whatever they find to this study.

**Verified directly in `1.merging.rmd` lines 81–91:**

| accession | what it is | ⚠️ what it is NOT |
|---|---|---|
| **`GSE186538`** | the series the **re-used adult samples originate from** — the authors' own code names the extracted folder `samples_from_GSE186538` and the tarball `franjic_et_al_samples.tar.gz` | 🔴 **NOT Nascimento's deposit** |
| **`GSE199762`** | the series the tarball is **fetched from** | 🔴 **NOT asserted to be either party's primary deposit** — the code only shows the fetch |
| **`GSM8002943`–`GSM8002960`** | the **study's own eighteen per-sample deposits**, including `EC_Stream` | — |

🟢 **And the re-used data are now POSITIVELY SEPARABLE** — by sample name (`hsb*`) and by age
(50–79 y versus 23 GW–27 y). **It can never again be confused with this study's own.** That is what
closing the hazard means.

⚠️ **Depth: `author-code`. None of these accessions was resolved against GEO** — the hosts are
blocked — and none was guessed, constructed or pattern-matched.

---

## 7 · What is still unknown, and what a session with egress should do first

🔴 **Whether `WWOX` is even present in the object's ~21,563-gene universe is unknown.** **That is the
first thing to test — before any DE-table question.** If the gene is not in the feature set, every
downstream question is moot; if it is, the CELLxGENE object answers the abundance question directly
and carries its own dropout control.

**Bounds unchanged and re-verified in today's fetch:** absence from a DE table is
`NOT_TESTED_OR_NOT_SIGNIFICANT` and **must not be re-voiced as non-expression**; a DE table bounds
membership, not abundance; the dropout constraint stands; and the authors' own negative —
*"In the EC stream microdissection, we did not find intermediate progenitors for interneurons or a
differentiation trajectory connecting the local RG to the immature inhibitory neurons"* — means any
finding reads as **"WWOX in postnatal human periventricular radial glia"**, never as *"WWOX in the
progenitor supplying the stream."*

**`D-37`: when a paper's data are unreachable, look for the authors' code before concluding the data
are closed.** Two prior waves exhausted twenty routes between them and concluded the accession did
not exist here. **It was in a public GitHub repository the whole time, and GitHub was never blocked.**
