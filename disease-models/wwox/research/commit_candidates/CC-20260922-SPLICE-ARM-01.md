# COMMIT CANDIDATE — CC-20260922-SPLICE-ARM-01

**Source:** Scientist E, RNA/splice-rescue node
([`splice_allele_rna_evidence_20260922.md`](../../analysis/splice_allele_rna_evidence_20260922.md)).
**Every load-bearing item below was re-derived or re-read by the Orchestrator**, not accepted from
the hand-back: the exon arithmetic was recomputed from the repository's own ClinVar file, the
PubMed false zero was reproduced with its control, and PMID 30362252's body was retrieved in full.
**Change class:** **MINOR** for §1 and §3; 🔴 **MODERATE** for §2 — a canonical `PAPER` record quotes
an abstract sentence as a *"Finding trasferibile"* that its own body does not support.
**Target:** `paper_registry_current.md` (`PAPER 044` Note) · `discovery_ledger_current.md`
(`DL-MECH-045`, `DL-BIO-002`) · `tx001_experiment_decision_packet_20260921.md`.
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R3** for §2 (canonical registry text, quoted finding, record declared
`complete_fulltext_read`); **R2** for §1 and §3.
**Proposes:** `D-28` — *"an unexpanded `query_translation` is a parser failure, not a zero."*

---

## 1 · 🔴 Exon 7 is the one internal exon that is in-frame — and the repository has no node for it

**Re-derived independently by the Orchestrator** from `analysis/data/WWOX_clinvar_all_variants.csv`
(1,327 records, HGVS on `NM_016373.4`, SPDI on `NC_000016.10`/GRCh38), by binning exonic SNVs on the
`genomic − cDNA` offset. Reliability **measured, not assumed**:

```
offset classes: 9        exonic SNVs: 729
reference-base concordance: 729/729   (⇒ plus strand, no coordinate slippage)
```

Nine classes for nine exons, **no outliers**, and every reference base agrees.

| exon | cDNA | nt | mod 3 | skipping |
|---:|---|---:|---:|---|
| 6 | 517–605 | **89** | **2** | **frameshift** ✅ *the repository's working figure, confirmed* |
| **7** | **606–791** | **186** | **0** | 🔴 **IN-FRAME** |
| 9 | 1057–1245 | 189 | 0 | **last exon** — no exon 10 |

⭐ **Exon 7's boundaries are observed directly** — ClinVar carries SNVs at both `c.606` and `c.791` —
which is the strongest case this dataset can produce. Exons 2, 4 and 5 are bounded inside their true
extent because no ClinVar SNV sits on their terminal base; **exon 7 is not.**

### Why this matters therapeutically

🔴 **The acceptor of exon 7 is `c.606-1G>A` — a five-patient homozygous allele**, already in this
repository: `paper_registry_current.md:6398`, *"caso 2: **splice acceptor omozigote c.606-1G>A**
(introne 6…)"*, and counted in `FT-110`'s ten-patients argument. Intron 6 is the intron immediately
5′ of exon 7, so the mapping closes.

If that allele causes exon-7 skipping, the product is a **352-aa internally deleted protein with no
premature termination codon and therefore no NMD at all** — and the excised segment contains
**codon 230**. That is not a null. It is a **structurally defined hypomorph**, and it belongs to a
different therapeutic class from every other splice allele in the model.

⚠️ **`PREDICTED`, and hedged as such.** Loss of an acceptor does not compel exon skipping —
cryptic-acceptor use and intron retention are live alternatives, and nobody has measured this
allele's RNA. What is **measured** is the arithmetic: 186 nt, mod 3 = 0.

**Proposed:** record exon-7 in-frame status in `DL-MECH-045`, and stop reasoning about WWOX splice
alleles under a single uniform PTC/NMD frame. **There are at least three regimes in this one gene** —
internal frameshifting (exon 6), internal in-frame (exon 7), and terminal-exon (exon 9, where
skipping is not even a defined outcome and everything escapes NMD).

---

## 2 · 🔴 `PAPER 044` quotes the abstract's "nonsense-mediated decay"; the body never says it

`paper_registry_current.md` `PAPER 044` (Davids 2019, PMID 30362252), **Evidence depth: full text
reviewed (`complete_fulltext_read`)**, carries under **Note** — *"Finding trasferibile"*:

> *"the deletion led to **nonsense-mediated decay** of the NM_016373.3 transcript…"*

**Orchestrator retrieved PMC6296882 in full this session.** According to PubMed
([DOI](https://doi.org/10.1002/humu.23675)), that sentence is from the **abstract**. The body's
corresponding sentence is:

> *"The exon 1–2 junction, however, was detected and was only slightly reduced in our patient,
> whereas the exon 7–8 junction was barely detectable, **suggesting that the two longer transcripts
> were not expressed or were degraded**."*

🔴 **Three findings, each verified in the returned text:**

1. **The body states two alternatives and resolves neither** — *"not expressed **or** were
   degraded"*. That is **structurally identical to Johannsen's *"impaired translation or premature
   degradation"***, which this repository refuses to collapse for `Q230P` and reversed a baseline
   over on 2026-07-14. The same refusal is owed here.
2. **The words *nonsense-mediated* appear in the abstract and nowhere in the body.**
3. **No NMD inhibitor was used.** The methods are qPCR junction assays and western blot. **NMD is
   not derivable from a junction ratio without a translation block.**

⚠️ **And the record declares a complete full-text read** — so the body was available to whoever
wrote the note, and the abstract's stronger indicative was taken anyway. This is the **`LIT-0405`
failure class recurring inside a record that declares the read which should have prevented it**:
there, *"decreased plasma GH"* was refused as a reading and the body reported it as not significant.

**Proposed edit — `PAPER 044` Note.** Replace the quoted finding with the body's sentence and mark
the divergence:

> **Finding trasferibile (dal CORPO, non dall'abstract):** *"the exon 7–8 junction was barely
> detectable, suggesting that the two longer transcripts were **not expressed or were degraded**."*
> ⚠️ **L'abstract afferma *"nonsense-mediated decay"*; il corpo non usa mai quelle parole e
> **nessun inibitore dell'NMD è stato impiegato**. Il metodo è qPCR di giunzione + western: un
> rapporto di giunzione non dimostra NMD senza un blocco della traduzione. Le due alternative —
> mancata espressione contro degradazione — **restano irrisolte**, esattamente come in
> [[claim_registry_current#CLAIM 019]].

🔴 **Consequence for the whole axis, and it strengthens the negative:** this was the field's **only**
citable instance of measured NMD in WWOX. With it withdrawn, **no WWOX allele of any class — splice,
nonsense, deletion — has ever been assayed with an NMD inhibitor.**

---

## 3 · The experiment gains three corrections the arithmetic forces

Against `tx001_experiment_decision_packet_20260921.md`:

1. 🔴 **Resolution.** Candidate cryptic products differ from normal by **6 or 8 nt**. **Agarose
   cannot resolve 6 nt.** Capillary/fragment analysis plus **Sanger on every product, including a
   single apparently-normal band** — because a 6-nt in-frame cryptic product *is* an apparently
   normal band.
2. 🔴 **An intron-8-anchored reaction is mandatory, not optional.** Intron 8 is ~779 kb, and a
   junction-spanning primer pair is structurally blind to read-through, retention and intronic
   polyadenylation — which Schirmer documented exist in this gene.
3. 🔴 **The exon 4–6 "core" normaliser is not inert, and Davids measured why.** Verbatim from the
   body: *"The residual expression of the exon 1–2 junction may be explained by the amplification of
   [the alternative transcript], **which has increased expression of its exon 5–6 junction**."* The
   short isoform's own exon 5–6 junction **rises when the long isoform is lost** — so that
   denominator moves with the lesion. Use a long-transcript-specific amplicon (exon 7–8, as Davids
   did) and report isoform composition rather than a ratio to a moving baseline.

**±cycloheximide stays mandatory, with an endogenous NMD-sensitive positive control.** NMD escape
being *predicted* for the exon-9 allele is a reason to run the arm, not to skip it.

---

## 4 · 🔴 The instrument defect, reproduced with its control

Scientist E reported a PubMed **false zero**. **Reproduced by the Orchestrator:**

| query | `total_count` | `query_translation` |
|---|---:|---|
| `WWOX AND "c.606-1G>A"` | **0** | `WWOX AND "c.606-1G>A"` — 🔴 **raw string, `WWOX` not even resolved** |
| `WWOX AND "606-1G"` | **1** (PMID 26345274) | `("wwox protein human"[Supplementary Concept] OR "wwox protein human"[All Fields] OR "wwox"[All Fields]) AND "606-1G"[All Fields]` |

**The zero was a parser failure, not a search.** The same allele, the same index, one punctuation
class apart. Since the repository's variant strings are full of `>`, `+` and `-`, **this defect is
aimed squarely at the token class this model is built from.**

> **Rule proposed (`D-28`): read `query_translation` before believing any zero. An unexpanded
> translation — one that echoes the raw query and does not resolve the gene symbol — is a parser
> failure and must not be reported as absence.**

🔵 **And it makes the trustworthy zeros legible.** The `c.1057-2A>G` zero is sound, because PubMed
**decomposed** that phrase (`"c 1057 2a" AND "g"`) while **preserving** `"c.517-2A>G"` and
`"c.516+1G>A"` for the two alleles that do exist — the decomposition is itself the evidence.

⚠️ **This is the second independent proof this session that query-count negatives need guarding.**
Scientist D's census proved a different one: PubMed `[All Fields]` does not read **Methods**, so two
papers that performed video-EEG and ECoG appear in no EEG query. **Different mechanisms, same
lesson** — and every query-count negative this repository holds was produced without either guard.

---

## 5 · Also verified, and one correction to a prior session artefact

- ✅ **`PREMISE: NOBODY_LOOKED` upheld with harder counts.** Three splice-allele measurements in the
  entire field; one on an acceptor; **zero** quantified, **zero** with an NMD block, **zero** with a
  protein readout, **zero** with a correction arm, **zero** on the reference genotype's allele, and
  **zero** on any of the four `−3` alleles where leaky splicing is mechanically possible.
- 🔴 **Correction to feasibility item C-2**, which states *"No −3 neighbour variant exists in LEGEND
  for either."* **`c.1057-3C>T` is in the repository's own ClinVar file** and is the `−3` neighbour
  of the reference genotype's own allele, as are `c.108-3C>T`, `c.231-3C>A` and `c.410-3T>C`. C-2's
  substantive half — that `−1/−2` and `−3` are **opposite regimes**, AG destroyed versus AG intact —
  is confirmed.
- ✅ **`FT-110` partly closed:** `PMID 38902482` is an oesophageal-cancer Hippo/YAP study, **not a
  splice paper**. That debt is not-applicable; the `42721537` debt stands.
- ⛔ **Unresolved and named as the cheapest open item in the axis:** the `+8` cryptic-acceptor frame
  call for `c.1057-2A>G`. Under SpliceAI's standard `DP_AG` convention the new exon starts at
  `c.1063` ⇒ 6 nt lost ⇒ **in-frame, a hypomorph**; under the alternative reading ⇒ 8 nt ⇒
  frameshift ⇒ NMD-escaping truncation, which is `DL-MECH-045`'s current position. **Opposite
  biology, opposite `TX-001` headroom, and it turns on a coordinate convention nobody wrote down.**
  **Not adjudicated here.** Re-reading the raw `DP_AG` field is free and decides it.

---

## 6 · Provenance and integrity

- **Independently re-derived, not accepted:** the exon table was recomputed by the Orchestrator from
  the repository's own ClinVar export with the offset-class count and the 729/729 concordance as its
  own quality control. Direct sequence egress is **403 at CONNECT** (Ensembl, eutils, NCBI, EBI), so
  RefSeq could not be consulted — **declared, not glossed.**
- ⚠️ **Extraction defect observed again, in the paper this candidate corrects.** The returned body of
  PMID 30362252 reads *"loss of the longer isoform (/), which contains the short-chain
  dehydrogenase/reductase domain, and the increased expression of the shorter isoform (/)"* — **the
  kDa values have been deleted**, while `33kDa` survives in the next sentence. **The 46/19 kDa
  figures in `PAPER 044` are therefore not re-verifiable from this route and are not restated here.**
- **`UNREAD_PREMISE`: to be measured with `growth_anchors.py check` before landing, not predicted.**
- **No receipt is claimed for PMID 30362252 in this candidate.** The body was retrieved to adjudicate
  two named sentences; that is a targeted adjudication, not a complete read, and `PAPER 044` already
  declares a prior full-text read whose depth is not in question — **only its quotation is.**

---

## 7 · ✅ APPEND-ONLY — §5's open item is RESOLVED, from the repository's own data, the same day

Scientist E called the `+8` frame call *"the cheapest open item in the whole document"* and declined
to adjudicate it, on the grounds that the raw SpliceAI `DP_AG` field would have to be re-read.

🔴 **The raw field cannot be re-read here, by design.** Its provenance is
`discovery_ledger_current.md:43`: *"**ESEGUITO 2026-07-04** … vedi **inbox entry INBOX-005 (private
quarantine log)**"*. That log is part of the **private overlay, which is excluded from this edition**.
The public edition retains the derived label — *"sito criptico +8"*, `DS_AG 0.64` — and **not the
field the label was derived from**. So a conclusion in `DL-MECH-045` rests on a datum this edition's
readers cannot reach: the session's recurring pattern, in its most consequential instance.

**But the question does not need the raw field. It can be settled from coordinates.**

### 7a · The `+8` position, fixed exactly by three independent anchors

All from `WWOX_clinvar_all_variants.csv`. SPDI is **0-based**, so 1-based = SPDI + 1:

| record | SPDI | 1-based | cDNA |
|---|---|---:|---|
| `c.1057-2A>G` | `…:79211605:A:G` | **79,211,606** | the allele — ✅ matches `DL-BIO-002`'s recorded coordinate |
| `c.1057C>T` | `…:79211607:C:T` | 79,211,608 | `c.1057` |
| `c.1063G>A` | `…:79211613:G:A` | **79,211,614** | `c.1063` |

`79,211,606 + 8 = 79,211,614`. 🎯 **`+8` from the variant is `c.1063`, exactly.** The ladder closes
with no slack: `c.1057-2` = 606, `c.1057-1` = 607, `c.1057` = 608, and every intervening cDNA
position that ClinVar covers (`1059`, `1060`, `1062`, `1063`) sits where it should.

### 7b · 🔴 The reference bases exclude every competing reading

A gained acceptor requires an **`AG`** immediately 5′ of the new first exonic base. Reference bases
recoverable from ClinVar's deleted-allele field: **`c.1057=C`, `c.1059=A`, `c.1060=C`, `c.1062=G`,
`c.1063=G`** (`c.1058` and `c.1061` are not covered by any record).

| if the new exon starts at… | required `AG` at | reference says | verdict |
|---|---|---|---|
| **`c.1063`** (⇒ **6 nt** lost) | `c.1061`, `c.1062` | `?`, **`G`** ✅ | 🟢 **the only survivor** |
| `c.1064` (⇒ 7 nt) | `c.1062`, `c.1063` | **`G`**, `G` | ⛔ first base is `G`, not `A` |
| `c.1065` (⇒ **8 nt**, the frameshift reading) | `c.1063`, `c.1064` | **`G`**, `?` | ⛔ first base is `G`, not `A` |
| `c.1062` (⇒ 5 nt) | `c.1060`, `c.1061` | **`C`**, `?` | ⛔ first base is `C`, not `A` |

**`c.1063` is the only start position in the neighbourhood whose upstream dinucleotide can be `AG`** —
and its second base is confirmed `G`. **The 8-nt frameshift reading is excluded by the reference
sequence**, not by a convention argument.

⚠️ **The one unverified base is `c.1061`, which must be `A`.** No ClinVar record covers it, and
direct sequence egress is 403 at CONNECT. If `c.1061 ≠ A` then *no* reading in the table works and
the `+8` label itself would need re-deriving. **Stated as the single remaining check, and it is one
base.**

### 7c · What the surviving reading means — and it moves `TX-001`

New exon start `c.1063` ⇒ **`c.1057`–`c.1062` lost = 6 nt**. And the frame is clean:
`(1057 − 1) / 3 = 352` exactly, so **`c.1057` is the first base of codon 353**. The loss is therefore
**exactly codons 353 and 354 — an in-frame two-residue deletion, `p.353_354del`, in a 414-aa
protein.**

🎯 **No frameshift. No premature termination codon. No NMD question at all.** Under this prediction
the acceptor allele of the reference genotype does not produce a truncated unstable protein — it
produces a **near-full-length protein two residues short**, which is a **hypomorph**, and the most
favourable prediction any allele in this genotype has ever carried.

🔴 **This contradicts `DL-MECH-045`**, whose position is *"probabilmente produce una **proteina
tronca instabile**"* and whose causal statement reads *"(predetto) → frameshift/PTC → NMD or
truncated_protein"*. **Proposed:** `DL-MECH-045`'s predicted outcome is **withdrawn and replaced**
by the in-frame two-codon deletion, with the coordinate derivation above recorded in place of the
unreachable `DP_AG` label, and `c.1061` named as the one base that would falsify it.

### 7d · What this does NOT license, stated because the temptation is obvious

- ❌ **It remains `PREDICTED`.** `DS_AG 0.64` is a **moderate** score: SpliceAI predicting an
  acceptor gain is not the site being used. Acceptor **loss** is the confident call (`DS_AL 0.96`,
  MaxEntScan Δ −7.95, two orthogonal methods); what happens *instead* is the uncertain part, and
  cryptic-acceptor use competes with exon-9 outcomes that are not even definable (no exon 10) and
  with intron-8 read-through.
- ❌ **Nobody has measured this allele's RNA** — the census stands at **zero** for it. A better
  prediction is still a prediction, and `PREMISE: NOBODY_LOOKED` is untouched.
- ❌ **No claim about protein function.** A two-residue in-frame deletion can still abolish folding
  or binding; `p.353_354del` sits in the SDR span and the repository has learned twice this session
  that predicted structural consequence does not track measured outcome.
- ✅ **What it does do is raise the value of the experiment `TX-001` already specifies** — and
  sharpen it. Under this prediction the aberrant product differs from normal by **6 nt**, which is
  precisely why §3's resolution correction is not pedantry: **on agarose this allele would look
  normal.** A laboratory running the obvious gel would report wild-type splicing and be wrong.

**Provenance:** every coordinate and reference base above was read by the Orchestrator directly from
`disease-models/wwox/analysis/data/WWOX_clinvar_all_variants.csv` in this session. Nothing is
reconstructed from memory, and the SpliceAI positional convention is **not relied upon** — the
adjudication rests on which dinucleotides the reference sequence permits.
