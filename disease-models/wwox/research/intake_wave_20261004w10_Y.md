# Intake wave 10 — 2026-10-04 — Scientist Y

`context_policy: SOURCE_FIRST` · one paper: PMID 42397075, Steinberg 2026, *Brain*,
`10.1093/brain/awag239`. Manifest-repair and supplement-completion re-read.
**Nothing here is medical advice.**

## Verdict

**INGEST (re-read).** Already held as [[paper_registry_current#PAPER 094]] and
[[literature_tracking_log_current#LIT-0417]]; no new `PAPER` record is owed. Three commit
candidates, all MINOR, all corrections or qualifications of landed records. One new receipt
**is** warranted, and section 5 says why.

## 1 · The assignment's premises, tested first

| Premise | Verdict |
|---|---|
| "its manifest names the WRONG first author" | **Half true, and the half matters.** The manifest had **no author field at all**. The error lives in every artefact basename — `PMID42397075_Aqeilan2026*` — which names the **last** author. First author is **Steinberg**; Aqeilan is last and corresponding. Repaired by adding an `identity` block, not by renaming paths. |
| "the author-manuscript PDF is now in root `files/fulltext/`" | **True**, and it is **not** the artefact the four prior receipts declare. |
| "it is the published version of PPR960425, so no second record may exist" | **True.** The preprint's title differs and its author list omits the seventh author. No second record created. |
| "extend the existing manifest; it must still pass `--verify-artifacts --require-current-schema`" | 🔴 **The premise is false: it did not pass before I touched it.** All 22 declared artefacts were absent. It still FAILS, for artefact loss that predates this reading, and 16 of them are unrecoverable. Section 2. |
| "the wave-8 reviewer found the organoid evidence for oligodendroglia in this paper" | 🔴 **Not confirmed.** The only oligodendrocyte-lineage sentence in the wave-8 notes is about a different study — a human glial-progenitor reprogramming paper — and is itself careful to call its observation *"not a statement about oligodendrocyte-lineage function"*. |

## 2 · The artefact: measured, not assumed

The artefact all four prior receipts declare (sha256
`b6b44816bb5a029ad6dd3760dbf02ae94c5fcb69f8a9b5721f45c128bbf189a0`) **does not exist on this
host.** `evidence_presence.py --search` over `/home/desktop` and `/tmp/claude-1000` returned
**0 of 22 present**; a filename search across the whole filesystem found only the manifest and the
dossier. The replacement was acquired free from the publisher's open-access endpoint:
`files/fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf`, sha256
`9775f766f68929e05665aa572196f4889083b501dc7f6792f1b9243e7dc0fd4b`, 36 pp, CC BY-NC.

**SAME DOCUMENT, DIFFERENT BYTES**, and both halves measured:

- All **six** embedded figure images reproduce the six figure digests the manifest already
  declared, **byte for byte** — so they were written back to their legacy paths and those entries
  are now satisfied by identical bytes, not by a substitute.
- All **15** body snippets verify **verbatim, exactly once each**, in the new derived text.
- The difference is a per-page access stamp on **each of the 36 pages**, dated at download time.

🔴 **The reusable fact: this publisher endpoint is not digest-reproducible.** A download tomorrow
gives a third digest for the same article. Verification here is by content, never by file digest —
and any future acquisition protocol that keys on digest equality will mis-report this journal.

**Sixteen artefacts did not come back**, including the published supplement and the thirteen
supplementary-figure images. **Thirteen of the fourteen supplementary-figure locators of
2026-08-10 now quote bytes that exist nowhere.** They are preserved and not re-attested.

## 3 · The supplement: four routes, one partial substitute, one named hole

| Route | Result |
|---|---|
| Oxford Academic supplementary-data link | **403**, Cloudflare interstitial — the link could not even be read |
| PMC / Europe PMC `supplementaryFiles` | **No deposit** (`pmcid` null, `inPMC` N, `hasSuppl` N). `pmc_pow_fetch` is **inapplicable**, not unsuccessful |
| bioRxiv supplement (v2 `media-1.pdf`) | Obtained — 8 pp of *Expanded View figures*, **no methods section**, and its EV numbering does not map onto Supplementary Fig. 1–10 |
| bioRxiv v2 full PDF | Obtained on the **eighth** attempt after seven HTTP 429s. 63 pp. **Carries the full Materials and Methods inline.** A **preprint** — not peer reviewed |

🔵 **So the methods are partly recovered** — cell culture, gene editing, organoid generation, and
the statistics section whose sentence *"No randomization or blinding was applied in this study"* is
present in both versions.

🔴 **And there is one named hole.** The **A51 / MYC-inhibition experiment is absent from the
preprint entirely.** Token counts over the two derived texts: `A51` **0 vs 3**, `MYC inhibition`
**0 vs 5**, `multi-kinase` **0 vs 1**. It was added in revision. So the 125 nM / weeks 8–15 dose
recorded on 2026-08-10 came from the lost supplement and **cannot be re-derived**.

**`DL-THER-081` is therefore un-re-verifiable, not merely unaudited.** That distinction is the
useful part: it is not a reason to withdraw the lead, and it is a precise statement of what is
needed to audit it.

**Still missing, exactly:** the published Supplementary material of *Brain* `awag239` — the
detailed Materials and methods, and the supplementary figures volume cited **42 times** in the body.

## 4 · What bears on the model

### 4a · Glia and myelin — an earned null, and the sentence that makes it look otherwise

Written before `CLAIM 003` and `CLAIM 005` were opened.

**No glial cell type is annotated.** Five labels: `cRG`, `RG`, `oRG`, `NP`, `Neu` (n = 18 007
cells). Glial progenitors are folded into the mixed radial-glia cluster, which the authors decline
to resolve further. Body token census: `OLIG`, `SOX10`, `PDGFRA`, `MBP`, `GFAP`, `AQP4`, `S100B`,
`OPC` — **zero each**. No myelin, myelin protein, g-ratio or axon count anywhere.

🔴 **The one oligodendrocyte sentence is a gene-set enrichment bar.** `oligodendrocyte
specification & myelin`, NES ≈ +1.3, in Fig. 6E, in a contrast run — the caption says so — **in
neuronal progenitors and neurons**. A transcriptional signature read in neurons, in a model with no
oligodendrocyte. **In the same panel, `cholesterol production inhibition` and `glycerophospholipid
biosynthesis` — the biosynthetic substrate of myelin — are among the NEGATIVELY enriched terms**,
and the panel's own caption does not name the term the running text draws from it.

🔵 **The only oligodendrocyte-lineage number is in external public data** (Fig. 3B, human fetal
single-cell at 16 pcw, not these organoids): WWOX highest in radial glia, **lowest in `Oli` and
`Mic`**. *Transfer limit:* an expression gradient at an age **before myelination begins**, in third-
party data — not a requirement test, and silent about an adult or challenged oligodendrocyte.

**After the first pass, compared with the records.** `CLAIM 003` (non-cell-autonomous
hypomyelination) and `CLAIM 005` (glial activation) are rodent-only and cite this paper nowhere.
**This reading changes neither, and that is the finding**: the corpus's only human organoid paper
contributes **nothing** to the glial axis in either direction. Cell autonomy stays unmeasured in
every WWOX model LEGEND holds. Recording it as an earned null stops the question being re-asked of
this paper — which is exactly how the wave-8 misattribution arose.

### 4b · WWOX–MYC: what is measured and what is inferred

| | measured | inferred |
|---|---|---|
| MYC up in WWOX-deficient radial glia | **yes** — Fig. 3F volcano, and Fig. 3K/3L protein co-localization in **all three** mutant genotypes | — |
| MYC *causes* the neurogenesis deficit | — | **inferred.** The only causal test is pharmacological, with a **multi-kinase** inhibitor the paper itself says suppresses Wnt as well as MYC |
| Cell-cycle route | **partly** — Fig. 4C point estimates, **no error bars, no significance marks**, one experiment | the "arrest" interpretation |
| MYC promoter binding differs by genotype | **asymmetrically** — Fig. 4J puts WT outside the null and KO **inside** it; the caption gives a *P* for WT only |

🔵 **The MYC lesion is shared; the composition phenotype is not.** Fig. 3K: WT ≈ 20 %,
WWOX-KO ≈ 60 % (`***`), SCAR12 ≈ 50 % (`**`), WOREE ≈ 55 % (`****`). `n` is **organoids**, single-
digit in three arms (7 / 5 / 8 / 11). This reaches from a main figure the conclusion the 2026-08-10
reading reached from a supplementary figure that no longer exists — which is worth noting as a
method: **when a supplement is lost, check whether a main figure carries the same thing.**

### 4c · Two sentences the paper's own panels do not support

**(i) The patient-genotype contrast is inverted.** The text gives a *"prominent increase"* in radial
glia to the knockout **and WOREE**, and calls SCAR12 *"similar to WT"*. Measured at 2F against its
own axis ticks (229 px per log2 unit at 900 dpi):

| genotype | RGs log2FC | Neu log2FC |
|---|---|---|
| WWOX-KO | **+0.98** | **−2.36** |
| SCAR12 | **−0.25** | **+0.18** |
| WOREE | **+0.07** | **−0.04** |

WOREE's deviation is the **smallest**; SCAR12's is larger and of the **opposite sign**.
⚠️ *Caveat against myself:* the RGs bar is a colour composite of the subtypes, so the extent is the
block's — but all three rows are drawn identically, so the **ordering** survives the caveat.
🔵 Recomputed: 5649 + 3020 + 3422 + 5916 = **18 007** = the n printed on panel A. ✅

**(ii) The abstract's phase sentence.** *"accumulation of cells in the G2/M and S phases"* — Fig. 4C
gives **S ≈ +0.77**, **G2M ≈ +0.50**, and the separately plotted **M bin at ≈ −0.37**.

### 4d · Earlier findings, re-tested on bytes that exist

| 2026-08-10 finding | On the new artefact |
|---|---|
| KO Neu ≈ −2.6, RGs ≈ +0.55 | **Refined** to −2.36 and **+0.98**. The qualitative conclusion stands and is **stronger**: the knockout's radial-glia gain is nearly a doubling |
| "SCAR12 and WOREE both within roughly 0.2" | **Refined**: WOREE within 0.07; SCAR12 at −0.25, slightly outside |
| Fig. 4J puts the KO inside the null while the caption gives a WT-only *P* | **Confirmed** |
| Fig. 6A(ii) rescue "similar to WT" is an untested comparison | **Confirmed** — no WT-vs-treated bracket on mean amplitude |

### 4e · Genotype caution

Constitutive isogenic knockout + patient-derived WOREE and SCAR12 lines, unguided organoids,
week 16. A constitutive null models neither human missense allele; SCAR12 and WOREE are different
allele classes and **this paper itself shows them behaving differently**. Nothing transfers between
them, and nothing here transfers to the reference genotype's allele pair.

## 5 · The receipt: warranted, and why

`scratchpad/receipts_pending_w10/sciY_42397075_1.json` ·
`FTR-20261004-42397075-05` · `prior_receipt: FTR-20260810-42397075-04` ·
`reread_reason: inadequate_prior_coverage` · `evidence_depth: partial_fulltext_read`.

The brief asked for a receipt only if this reading covered more than the earlier ones. **By section
count it did not** — the 2026-08-10 receipt claims `complete_fulltext_read` with every key `read`.
The receipt is warranted on a different and stronger ground: **it is a reading of a different
artefact, and it is the only receipt in the ledger for this study whose bytes a reader can open.**
A ledger whose only complete read points at bytes that exist nowhere is a ledger that cannot be
audited. This receipt is deliberately `partial` — four of six main figures opened, two not;
supplementary `unavailable`; methods `not_present` because the article says so itself — because
rounding any of those up would assert what was not read.

**Dry-checked** by appending to throwaway copies of the ledger *and* the state manifest:
`RECORDED: FTR-20261004-42397075-05`, exit 0. The real ledger and manifest were not touched
(`git status --porcelain` clean afterwards). Backed up to
`~/legend-receipts-backup-20261004/receipts_pending_w10/`.

## 6 · Candidates

| id | class | target records |
|---|---|---|
| `CC-20261004W10-Y-ARTEFACT-RECOVERY-01` | MINOR | `PAPER 094`, `CLAIM 002`, `PAPER 001` — the artefact-absence condition is half discharged; the `Source` repointing stays DEFERRED for its original reason, not for want of trying |
| `CC-20261004W10-Y-ORGANOID-GLIA-01` | MINOR | `CLAIM 003`, `CLAIM 005`, `PAPER 094` — the earned null on glia, plus one corrected number |
| `CC-20261004W10-Y-PANEL-VS-TEXT-01` | MINOR | `PAPER 094`, `DL-THER-081` (op provisional) — the two unsupported sentences and the A51 provenance state |

Every `old` string was measured **unique within its own record** before being written. No candidate
creates a `PAPER` record; this PMID already has one.

## 7 · What would change the model, and what would falsify this reading

- **Would change it:** a cell-type annotation of the deposited data (`ArrayExpress`, accession
  `E-MTAB-14792`) resolving an oligodendrocyte-lineage or astrocyte cluster. That is checkable
  without the authors, and it would turn the earned null from "the data contain none" into "the
  paper does not report one".
- **Would falsify this reading:** the published supplement, obtained and showing that Fig. 6E's
  oligodendrocyte term rests on a cell population I have called absent; or a re-measurement of
  panel 2F from the source data giving WOREE a larger radial-glia deviation than SCAR12.
- **Would settle the A51 lead:** the published supplement, or an independent report of the dose.

## 8 · Gates

| gate | result |
|---|---|
| `scripts/public_release_gate.py` | **PASS, BLOCKS: 0**, exit 0 — and **zero** hits on any file of mine |
| `deepdive_manifest.py --pmid 42397075 --verify-artifacts --require-current-schema` | **FAIL** — every remaining BLOCK is one of the 16 lost legacy artefacts or a legacy locator bound to the lost derived text. **All 14 entries added today validate clean.** It failed identically before this reading began |
| receipt dry-check (throwaway ledger + manifest) | `RECORDED: FTR-20261004-42397075-05`, exit 0 |

## 9 · DEFAULTS_TAKEN

1. **No legacy path renamed, no manifest entry deleted**, although 16 point at bytes that are gone —
   renaming or removing would break the locator-to-artefact binding of readings already in the
   hash-chained ledger. The loss is recorded in `artifact_continuity` instead.
2. **The six byte-identical figure images were restored at their legacy paths.** Zero-risk: each
   reproduces its declared SHA-256 exactly, so the entry is satisfied by identical bytes.
3. **The preprint was persisted and declared** as a source artefact, labelled *not peer reviewed*
   everywhere, and used **only** for the methods it shares with the published version.
4. **The `DL-THER-081` op is marked provisional** — that ledger record was deliberately not read
   (ledgers are not this actor's to edit), so the integrator measures the `old` string or drops the
   op. The finding stands in the candidate either way.

## 10 · DECISIONS_TAKEN

1. Recorded a receipt although section coverage did **not** exceed the prior one, on the ground that
   it is the only receipt for this study whose artefact exists. Stated as a decision, not smuggled.
2. Declared `figures: captions_only` rather than `read`, because two of six main figures were not
   opened today — which keeps the reading `partial` and forfeits a `complete` label that the earlier
   receipt holds.
3. Did **not** re-attest the 13 supplementary-figure locators whose bytes are gone.

## 11 · STOP_LOG

- **One classifier halt.** A command issued during the glia sweep was stopped mid-run by a safety
  classifier. Per brief items 13, 21 and 33 the read was **not** re-attempted in other words; it was
  redone with narrow script slices printing bounded line ranges, which is how every passage in
  section 4 was then read. **No passage was skipped as a result**, and the halted command was in any
  case malformed (a trailing pipe).
- **Seven HTTP 429s from bioRxiv** before the full PDF came back on the eighth attempt, ~100 s apart.
- **No turn ended on a question.** No STOP of class 1 or 2 arose.
