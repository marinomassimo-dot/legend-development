# `c.517-3C>A` — does the new intron-5 allele give RNA-RESCUE its first experimental handle?

**Scientist B · 2026-09-21 · READ-ONLY toward every canonical file and every ledger.** No canonical file modified, no `*_current.md` touched, no `BATCH_COMMIT`, no commit candidate, no receipt written, nothing committed or pushed. No splice predictor was run and no score was generated. No experiment is proposed as a plan, `TX-001`–`TX-007` are not re-ranked, and no contact with any person or group is proposed — that is an Operator action and is out of scope here.

🔴 **This is an evidence assessment for research planning. It is NOT treatment advice, NOT a recommendation, and NOT a statement about any individual.** It reasons about a WWOX-DEE genotype class assembled from published literature. Nothing here is medical advice.

**One artefact was used and it was already on disk — nothing was re-fetched.** No new full text was read.

| Artefact | Bytes | Chars | sha256 |
|---|---|---|---|
| `files/fulltext/PMID37583270_PMC_MCPtext.txt` | **52,764** | **52,224** | `0cf97dd004186ac91e5933586e12fb447b89eb2d23f1c6fd21d49323c62f926b` |

---

## 1 · VERDICT

**CONDITIONAL, and the condition is the one thing nobody has looked at.** `c.517-3C>A` does **not** inherit a handle from `c.517-2A>G`: every existing reagent for this junction carries the **−2** allele, whose acceptor `AG` is destroyed, and the `TX-001` packet's junction assay reads the **intron 8 / exon 9** acceptor, not this one. The single fact that decides it is arithmetic on LEGEND's own verified boundary map: **exon 6 is `c.517–605` = 89 nt, and 89 is not a multiple of three** — so if `c.517-3C>A` does what `c.517-2A>G` is *reported* to do, the product is frameshifted, non-productive, `GENE-REPLACEMENT`, and **RNA-RESCUE stays empty**. The allele earns interest for exactly one reason, and it is a reason `c.517-2A>G` can never supply: at **−3** the acceptor `AG` is **intact**, so a *leaky* partial-correct-splicing outcome — the only outcome an ASO could amplify — is mechanistically permitted rather than excluded, and it has never been measured in any WWOX allele.

---

## 2 · The two alleles side by side

**Binding distinction, applied to every row:** **ANNOTATED** = called splice-affecting by position, pipeline or predictor — a *prediction*, no RNA looked at. **MEASURED** = RNA or cDNA actually run. They are never combined.

| | `c.517-2A>G` | `c.517-3C>A` |
|---|---|---|
| **Position** | the **A of the canonical acceptor `AG` dinucleotide**, intron 5 | the **−3 position**, the last base before the `AG`; the pyrimidine (`Y`) slot of the `YAG` consensus and the 3′ end of the polypyrimidine tract |
| **Base change** | `A>G` — 🔴 **abolishes the acceptor dinucleotide outright** | `C>A` — 🔴 **pyrimidine → purine at a context position.** The `AG` is untouched. *(The reference and alternate bases are read from the HGVS string itself, which is roman-class and therefore admissible; nothing here is inferred from genome sequence.)* |
| **Class of lesion** | **null-type by position.** There is no correct junction to make. | **context-type.** Acceptor strength is reduced, by an amount that is **variable and not determined by position alone**. |
| **What is generally known about this position class** *(general splicing knowledge — NOT measured for this allele, NOT for any WWOX allele, and NOT computed here)* | −1/−2 substitutions abolish the 3′ splice site; the outcome is aberrant splicing, typically skipping of the downstream exon or use of a cryptic acceptor. | −3 substitutions span the whole range: **silent, partial/leaky, or fully null.** Purines occur at −3 in a minority of functional human acceptors, so `C>A` is a change *away* from consensus without being categorically disabling. **Which of the three it is cannot be read off the position**, and LEGEND holds no measurement, no score and no assay for it. |
| **ANNOTATED** | ✅ — `CLAIM 018`, `consolidated baseline` | ✅ — but only as the source's own typing: *"Deletion; splice site"*, *"Exonic deletion and 3′ splice site"*, novelty column *"Uncertain; Novel"*. 🔴 **No ACMG class is given for this allele alone**; the ACMG column carries **one** value for the compound genotype, *"Likely pathogenic"*, under the cohort's stated rule that *"only children with confirmed pathogenic and likely pathogenic variants were included"*. **Preserve the mood: the paper calls the allele "Novel" and the genotype "Likely pathogenic". It does not call the allele pathogenic.** |
| **MEASURED** | ⚠️ **MEASURED (reported)** only — *"Complementary DNA sequencing demonstrated…"* exon 6 skipping, `PMID 30853297`. 🔴 **LEGEND has never seen this measurement** (§ 3.2). | ❌ **Nothing.** `SpliceAI`, `MaxEntScan`, `RT-PCR`, `cDNA`, `mRNA`, `minigene` and `RNA analysis` occur **0 times** in the persisted artefact — an instrument reading over the extracted text, reported as a count. No predictor value exists for this allele anywhere in LEGEND's records, and none was generated here. |
| **Frame consequence *if* exon 6 is skipped** | 🔴 **Frameshift.** Exon 6 = `c.517–605` = **89 nt**, `89 mod 3 = 2`. *(LEGEND's arithmetic over its own verified boundary map — not a statement by any source.)* | 🔴 **Identical arithmetic, identical conclusion** — *if* the outcome is skipping. That "if" is the entire question. |
| **Patients reported** | **≥2**, per the class census, `DOS`-level | **exactly 1** — Patient 39, female, WWOX, compound heterozygous, onset GTC 2 mo / ES 3 mo, `MIC, C HYP, UTN, SP`; *"FIHT, response with ZON"*; outcome codes *"PES, SF (6)"*. ⚠️ **The outcome codes `PES` (persistent epileptic spasms) and `SF` (seizure free) are reported together in the source row; the tension is reproduced, not resolved.** |
| **Allele in trans** | reported in a compound-heterozygous setting; the trans partner is deliberately not reproduced here | 🔴 **the exon-6-containing deletion `(516+1_517–1)_(1056+1_1057‐1)del`** — HGVS **as published, not normalised** (mixed U+2013 / U+2010 dashes; lowercase `c` in `c.517‐3c>A`) |
| **Evidence level** | `consolidated baseline` for pathogenicity; **LOW for rescuability** | **novel single observation, annotation-only.** No functional data of any kind. |
| **Therapeutic class today** | **GENE-REPLACEMENT** (`CLAIM 018`) | **UNASSIGNABLE** — the same verdict the census gives `c.605+5G>A`, the only other non-canonical WWOX splice-region allele. It is **not** an RNA-RESCUE member and must not be recorded as one. |

**Do not generalise from −2 to −3.** The transfer is the thing under test, and it fails on the one axis that matters: the −2 allele *cannot* produce correct transcript, the −3 allele *might*. Everything downstream — reagents, assay, class assignment — follows from that asymmetry and not from the one-nucleotide distance.

### 2.1 · Where `c.517-3C>A` sits in the census

LEGEND's splice census held **nine** splice-affecting WWOX alleles, of which exactly **one** was non-canonical (`c.605+5G>A`, +5, **UNASSIGNABLE**). `c.517-3C>A` is the **tenth allele and the second non-canonical one — and the first non-canonical allele at an *acceptor***. That is its only structural novelty, and it is a real one: every other WWOX acceptor allele LEGEND holds (`c.517-2A>G`, `c.606-1G>A`, `c.1057-2A>G`) destroys the `AG`.

---

## 3 · The reagent question — does "already exists" survive scrutiny?

### 3.1 · What exists, and it is more than LEGEND's shorthand suggests

The claim under test was *"two independent WOREE iPSC lines"* for `c.517-2A>G`. **It survives, with a corrected reading and four qualifications.**

Verified from the manifest `deepdive_manifests/PMID42397075.json` and the receipt `FTR-20260810-42397075-04` (`complete_fulltext_read`), which tabulate five patient lines from `PMID 42397075` (Steinberg / Aqeilan, *Brain* 2026, `PAPER 094`):

| Line | Disease | Genotype as tabulated | Carries `c.517-2A>G`? |
|---|---|---|---|
| **WSM S** | WOREE | `NM_016373.4:c.517-2A>G` **homozygous** | ✅ — **the clean one** |
| **WCH S** | WOREE | `NM_016373.4: c.410G>T p.Gly137Val, c.517-2A>G` (**compound heterozygous**) | ✅ — but with a **missense in trans** |
| LM-iPS | WOREE | `c.864G>A` over `arr[GRCh37] 16q23.1(78,356,662_78,450,052)del` | ❌ |
| WPM S | SCAR12 | `c.1114G>C` homozygous | ❌ |
| WPM D | SCAR12 | `c.1114G>C` homozygous | ❌ |

Independently corroborated inside LEGEND from a **second paper and a second receipt**: `DL-MOL-010` records the **WSM** line (`c.517-2A>G`, splice, homozygous) from `PMID 34268881` (Steinberg 2021, *EMBO Mol Med*, **`PAPER 039`**, `FTR-20260814-34268881-03`, **`partial_fulltext_read`**), Materials & Methods and Tables EV3–EV5, alongside `WiBR3` hESC `WWOX`-KO, a stable `W-AAV` safe-harbour rescue line, lenti-WWOX, cerebral and forebrain organoids, LFP and cell-attached electrophysiology, γH2AX/53BP1 foci, astrogenesis, and RNA-seq at **GEO `GSE156243`**. **This is a real, characterised, published human neural bench, and the c.517-2A>G lines in it are real.**

### 3.2 · The four qualifications, and each of them bites

1. 🔴 **"Independent" means two independent *families*, not two independent *laboratories*.** WSM S and WCH S both sit in **one** laboratory (Aqeilan, and the two papers share first and senior authors). Availability is therefore **single-source**. LEGEND's shorthand *"2 independent WOREE iPSC lines"* is true about provenance of genotype and misleading about provenance of supply; it should be read as the latter wherever a feasibility argument rests on it.
2. 🔴 **The genotype table is a figure attestation from pixels, not a quotable text string.** The manifest locator carries the marker *"[figure attestation — pixels cannot be quote-matched]"* and places the table at **Supplementary Figure 1, panel E**, read at ~170 effective ppi. LEGEND holds it **first-hand** — a LEGEND actor looked at the panel — but it is **unmatchable by construction**, and it is therefore recorded here as a first-hand *attestation*, not a re-matched quote.
3. 🔴 **The artefact is not in this container.** `files/fulltext/` holds **20 files** and **none of them is `PMID42397075_*`**; the manifest's `source_artifacts` point at `PMID42397075_Aqeilan2026.pdf` (`b6b44816…`), `…_fitz.txt` (`9c48aa09…`) and five supplementary PDFs, **all absent from disk today**. The attestation cannot be re-verified here, and the ledger's hash chain (`fulltext_receipts.py verify` → **OK, 196 chained receipts, tail anchored**) attests to the *receipt*, not to the file's presence.
4. 🔴 **No availability statement of any kind exists in LEGEND's records.** `deposit`, `hPSCreg`, catalogue number, MTA, biobank and "available on request" return **nothing** for these lines across the whole disease model — and this is despite the receipt declaring the detailed Materials and methods (supplementary File009) **read in full**. **Obtainability is therefore UNKNOWN, not established and not absent.** A "reagent already exists" argument that has not established obtainability has established only that the reagent was *made*.

### 3.3 · And the decisive point for this question

**None of these lines carries `c.517-3C>A`.** They carry the **−2** allele. A cell system for the −2 allele is, for the −3 allele, a **comparator**, not a test article. It can show what a destroyed acceptor does at this junction; it cannot show what a weakened one does. **For `c.517-3C>A` the correct statement is: there is no cell system, no RNA, no DNA and no construct anywhere in LEGEND's records.** There is one reported patient and one published table row.

The one genuinely transferable asset is smaller and should be named precisely: **the WSM S homozygote is the ideal negative-direction comparator** for any future exon-5/6 junction assay, because it is the only WOREE line at this junction with no second WWOX allele contributing normal-length product. WCH S carries a **missense** in trans, whose transcript is normal-length, so any junction readout on WCH S is a two-allele mixture. That distinction is not currently recorded anywhere in LEGEND and is the most useful operational thing in this section.

---

## 4 · Assay reuse — does the `TX-001` packet's junction assay read `c.517-3C>A` unmodified?

### 🔴 **NO. And the premise that it would is wrong on the record.**

The `TX-001` experiment decision packet specifies, verbatim: *"The affected junction** is the intron 8 / exon 9 acceptor"*, with *"forward primer in **exon 8**, reverse primer in **exon 9**"*. Its public worked-example allele is **`c.1057-2A>G`**. **It is not an exon-5/exon-6 assay.** A junction amplicon anchored in exons 8 and 9 cannot report on an event at the `c.517` acceptor, which lies **three exons upstream**.

**What would have to change, stated exactly:**
- **New primer pair**, forward in **exon 5**, reverse in **exon 6** or **exon 7**, spanning the `c.517` junction. *(No sequences are asserted here; the packet itself withholds primer sequences deliberately and for good reason, and the same reason applies.)*
- **A new normaliser**, because the packet's existing one breaks — see below.
- **A new expected-product table.** The packet's shift table is computed for exon 9; exon 6 skipping removes **89 nt**, a different product and a different frame consequence.
- Everything else transfers **unchanged and at genuinely near-zero marginal cost**: the ± cycloheximide arm, the vehicle twins, the endogenous NMD-sensitive positive control, the healthy-donor baseline, capillary-electrophoresis / densitometry quantification, and the escalation to long-read cDNA if multiple species appear. **The method transfers; the reagents do not.**

### 4.1 · 🔴 A design defect the comparison exposes, recorded because it is load-bearing and was not visible before

The packet's normaliser is *"**Normaliser amplicon:** **exons 4–6** (\"core\")"*, chosen *"upstream of the affected junction"* to report total WWOX transcript. **An exons 4–6 amplicon spans the exon 5 → exon 6 junction — the `c.517` acceptor.** In any sample where an allele skips exon 6, the "core" amplicon is **not** constant: it shortens by 89 nt on that allele, and the denominator it is supposed to provide is corrupted by the very kind of event the assay exists to measure.

This is **not** a defect for the packet's own stated subject — the public worked example `c.1057-2A>G` has no exon-6 lesion. It becomes one the moment the assay is run on **any** sample carrying an exon-6-affecting allele, which includes both alleles discussed in this file and `c.516+1G>A`, `c.606-1G>A` and the exon 6–8 deletion besides. **Stated as a conditional design observation on an existing non-canonical packet. Nothing is re-ranked, no experiment is proposed, and the packet is not edited.**

### 4.2 · One property of Patient 39's genotype that is worth recording precisely

The allele in trans, `(516+1_517–1)_(1056+1_1057‐1)del`, **removes exon 6**. *(Whether the deleted span is exons 5–8 as the source's column says, or exons 6–8 as LEGEND's boundary map computes, the deletion covers `c.517→c.1056` and exon 6 is gone under both readings — so this conclusion does not depend on resolving that discrepancy.)* Consequently an exon-5/exon-6 junction amplicon would amplify **only from the `c.517-3C>A` allele**: the trans allele contributes no template at that junction. That is a **hemizygous-equivalent readout** — the cleanest possible allele-specific measurement of a −3 outcome, with no deconvolution needed.

⚠️ **This is a property of a genotype, not an opportunity that exists.** No RNA, no cells and no material from this patient exist in any form LEGEND can see, and none is sought here.

---

## 5 · Patient availability — what the literature reports, and nothing more

| | `c.517-2A>G` | `c.517-3C>A` |
|---|---|---|
| Patients reported | **≥2** (class census, `DOS`) | **1** |
| Independent reporting groups | ≥2 (`30853297`, `33916893` curation, `42397075`) | **1** |
| Characterised cell material | **2 iPSC lines**, one laboratory, obtainability **UNKNOWN** (§ 3.2) | **none of any kind** |
| Banked RNA / DNA | not recorded in LEGEND's records | not recorded in LEGEND's records |

🔴 **A correction to today's FT-116 triage that bears on this section.** FT-116 states the Indian cohort was *"recruited Jan 2021–Jun 2022"*. The persisted artefact's Methods say the children were *"tested between January 2018 and June 2022"*. **The artefact wins.** FT-116 used the later window to exclude the 2019 series and the 2021 curation from overlap; on the artefact's own window **that exclusion does not hold as stated**, and overlap with earlier reports cannot be excluded on recruitment dates alone. This does not change the count for `c.517-3C>A` — the allele is novel and occurs **zero** times elsewhere in LEGEND — but it removes a stated ground for confidence and is recorded so it is not re-voiced.

⚠️ **No contact with any author, group, biobank or family is proposed, implied or prepared here.** Whether any material is reachable is an Operator question and is out of scope.

---

## 6 · VERBATIM LOCATORS — re-match count and provenance order

Every quote below was re-matched **programmatically** (exact substring count over the file's bytes) at the time of writing. **26 propositions submitted · 26 matched · 0 failed.** Eight are **first-order** (the persisted artefact); eighteen are **second-order** (a LEGEND file or manifest). **The two claims that cannot be quote-matched at all are declared as such and are not counted as matches.**

### 6.1 · FIRST-ORDER — `files/fulltext/PMID37583270_PMC_MCPtext.txt` @ `0cf97dd0…f926b`

| # | Quote (as published / as extracted — **not normalised**) | Matches |
|---|---|---|
| L1 | `(516+1_517–1)_(1056+1_1057‐1)del; c.517‐3c>A` | 1 |
| L2 | `Exonic deletion and 3′ splice site` | 1 |
| L3 | `Exons 5 to 8; Intron 5` | 1 |
| L4 | `Deletion; splice site` | 1 |
| L5 | `Uncertain; Novel` | 1 |
| L6 | `Compound heterozygous` | 5 |
| L7 | *"only children with confirmed pathogenic and likely pathogenic variants were included"* | 1 |
| L8 | *"The variant classification was done as per the American College of Medical Genetics and Genomics (ACMG) 2015 recommendations"* | 1 |

**Instrument readings over the same artefact** (counts, not quotes): `SpliceAI` · `MaxEntScan` · `RT-PCR` · `cDNA` · `mRNA` · `minigene` · `RNA analysis` — **0 combined occurrences.** 🔴 **Token-class note:** these are *arabic-class* absences from an extractor that elides italics, superscripts and citation numerals, so a zero is weak evidence of true absence for formatting-sensitive tokens — but these are plain roman words in running text, and the same artefact's **roman-class** `c.`/`p.` HGVS strings and rsIDs survive intact (L1, plus `rs756762196`, `rs759794876` elsewhere in the table), which is what licenses every variant-level reading in § 2.

### 6.2 · SECOND-ORDER — LEGEND files

| # | File | Quote | Matches |
|---|---|---|---|
| L9 | `woree_therapeutic_class_census_20260921.md` | *"RNA-RESCUE has zero demonstrated members"* | 1 |
| L10 | same | *"a +5 change may be silent, leaky or null; nothing distinguishes them here"* | 1 |
| L11 | same | *"does not repair the sequence and cannot recreate the abolished acceptor"* | 1 |
| L12 | same | *"No productive alternative outcome has been demonstrated for any WWOX allele in any system."* | 1 |
| L13 | same | *"SpliceAI acceptor-loss 0.96; MaxEntScan 7.28 → −0.67; cryptic acceptor gain +8 nt, 0.64"* — **held values for `c.1057-2A>G`, quoted, not computed** | 1 |
| L14 | same | *"≥2, plus 2 independent WOREE iPSC lines"* | 1 |
| L15 | `claim_registry_current.md` | `CLAIM 018` title: *"The exon 6 splice-site variant c.517-2A>G is pathogenic and causes exon 6 skipping in humans"* | 1 |
| L16 | same | `CLAIM 018` Source: *"Weisz-Hubshman / Piard 2019 abstract-supported + prior claim integration"* | 1 |
| L17 | `tx001_experiment_decision_packet_20260921.md` | *"The affected junction** is the intron 8 / exon 9 acceptor"* | 1 |
| L18 | same | *"forward primer in **exon 8**, reverse primer in **exon 9**"* | 1 |
| L19 | same | *"**Normaliser amplicon:** **exons 4–6** (\"core\")"* | 1 |
| L20 | `wwox_splice_transcript_census_20260921.md` | *"No WWOX paper in this census reports intron retention or a cryptic splice site."* | 1 |
| L21 | same | *"Complementary DNA sequencing demonstrated"* | 1 |
| L22 | `ft116_cohort_triage_20260921.md` | *"a −3 change may be silent, leaky or null; nothing distinguishes them here"* | 1 |
| L23 | `deepdive_manifests/PMID42397075.json` | *"WOREE WSM S NM_016373.4:c.517-2A>G (homozygous)"* | 1 |
| L24 | same | *"[figure attestation — pixels cannot be quote-matched]"* | 15 |
| L25 | same | *"WOREE WCH S NM_016373.4: c.410G>T p.Gly137Val, c.517-2A>G (Compound Heterozygous)"* | 1 |
| L26 | `missense_splice_reclassification_risk_20260921.md` | *"exon 6 = c.517–605"* | 1 |

🔴 **A quote-integrity defect in today's FT-116 triage, found by this re-match and reported because it is a mood change inside quotation marks.** L22 (FT-116) reads *"a **−3** change may be silent, leaky or null…"*; L10, its source in the class census, reads *"a **+5** change may be silent, leaky or null…"*. FT-116 substituted the position **inside the quoted string**, converting a statement about `c.605+5G>A` into an apparent statement about `c.517-3C>A`. The underlying judgement happens to transfer — this file reaches the same **UNASSIGNABLE** verdict on its own grounds in § 2 — but **the quotation does not**, and a reader auditing FT-116 would find a source that does not say what the quote marks claim. **Recorded, not repaired: FT-116 is not this file's to edit.**

### 6.3 · Declared as UNMATCHABLE, and therefore not counted

- **The `c.517-2A>G` exon-6-skipping measurement itself** (`PMID 30853297`). LEGEND holds *"Complementary DNA sequencing demonstrated…"* **as an abstract sentence carried in its own census** (L21), not from the paper. The paper has `pmc_id: null`, is Elsevier-paywalled, and the splice census records it as **`unrecoverable_by_these_routes`** (`FT-003`). **There is no receipt for `PMID 30853297` anywhere in the ledger** — it appears only inside the evidence basis of another paper's receipt. The measurement underpinning `CLAIM 018`, a `consolidated baseline`, is **reported, never read, and not first-order at any depth**.
- **The iPSC genotype table** (`PMID 42397075` Supplementary Figure 1E). First-hand pixel attestation, explicitly unmatchable (L24), and its artefact is **not on disk in this container** (§ 3.2).

### 6.4 · Provenance JOIN — all five methods, reported separately per paper

| PMID | `registry_records.py` | `grep -rn` over `disease-models/` | `fulltext_read_receipts.jsonl` | `deepdive_manifests/` | `discovery_ledger_current.md` |
|---|---|---|---|---|---|
| **37583270** | **no record matched** | 6 files | **0 receipts** | **absent** | 🔴 `DL-MECH-060`, *"letti integralmente"*, dossier path **does not exist** |
| **30853297** | `PAPER 025`; linked from `CLAIM 018` | 12 files | 🔴 **0 own receipts** (1 incidental mention inside `FTR-20260921-39101447-01`) | **absent** | 1 hit — records it as *"riportato-come-misurato ma non letto"* |
| **42397075** | `PAPER 094`, `processed` | many | **6 mentions; `FTR-20260810-42397075-04` = `complete_fulltext_read`** | **present**, 6 locators, schema v2 | 3 hits |
| **33916893** | **`PAPER 040`** | many | 2 receipts; `FTR-20260909-33916893-01` = `complete_fulltext_read` (prior `-01` was a **`legacy_reconstruction`**, `partial`) | **present** | 1 hit |
| **34268881** | **`PAPER 039`** | several | `FTR-20260814-34268881-03` = **`partial_fulltext_read`** | not checked | `DL-MOL-010` |

🔴 **Two registry/ledger discrepancies found by the JOIN and reported, not repaired.** (a) `PAPER 094` states the manifest carries *"6 locators"*; the receipt `-04` and `discovery_ledger_current.md` both state **30 locators**, and the manifest's `receipt` field points at the **superseded `-03`**, not at `-04`. The on-disk manifest has **6** `verbatim_locators` entries, so the registry matches the file and the receipt and the ledger do not. (b) `PAPER 039`'s (`PMID 34268881`) `Evidence depth` reads `partial_fulltext_read` with *"Appendix Figures S1–S6 … assenti"*, while `DL-MOL-010` rests its whole reagent inventory on that paper's Materials & Methods and Tables EV3–EV5 — **which are inside the read scope**, so the lead survives, but it is carried on a **partial** read and should be cited as such. **Neither is edited here.** Both are the kind of one-directional drift that FT-116's own § 2 warns about, found by running all five methods rather than fewer.

---

## 7 · NEGATIVE RESULTS — and they are the substance of this file

1. 🔴 **RNA-RESCUE stays empty. `c.517-3C>A` does not populate it and cannot, on present evidence.** Nothing was measured, so the class gains a *candidate*, not a *member*. The census's *"zero demonstrated members"* and *"No productive alternative outcome has been demonstrated for any WWOX allele in any system"* both stand **unchanged after this analysis**. **This was the most likely outcome and it is the honest one.**
2. 🔴 **The "reagent already exists" argument, as stated for `c.517-3C>A`, is false.** The existing lines carry **−2**. For **−3** there is no cell line, no RNA, no DNA and no construct. The argument survives only in a much weaker and more useful form: *a comparator line and an assay design exist at this junction*.
3. 🔴 **The `TX-001` assay does not read this allele unmodified.** Its junction amplicon is exon 8 → exon 9. The premise that it carries exon 5 / exon 6 primers **is not what the packet says**.
4. 🔴 **Marginal cost is not near zero.** It is "one new validated primer pair plus a new normaliser plus a new expected-product table, on material that does not exist" — a different statement from "add a lane".
5. **No minigene exists for WWOX exon 6.** The only WWOX minigene LEGEND has read the measurement of is `c.172+1G>C` at **exon 2**, in HEK293T with an artificially shortened intron. A −3 minigene at exon 6 would be built from nothing, not adapted.
6. **The held predictor values point away from productivity even for the reference-genotype allele.** For `c.1057-2A>G` LEGEND holds a cryptic-acceptor gain at **+8 nt** (`DS_AG 0.64`) — an 8-nt shift, which is not a multiple of three and is therefore **frameshifting, not productive**. Quoted as a held value; **no predictor was run here and no score was generated for `c.517-3C>A` or for any other allele.**
7. **Neither allele's outcome distinguishes "absent" from "degraded".** No WWOX splice allele has ever been assayed with an NMD inhibitor — `cycloheximide`, `emetine`, `actinomycin` and `nonsense-mediated` are **zero** across the reachable literature. A leaky −3 allele and a fully skipped one are, without an NMD arm, **the same gel**.
8. **The −3 position does not carry an in-repo precedent to lean on.** `c.605+5G>A`, LEGEND's only other non-canonical splice-region allele, is **UNASSIGNABLE** and abstract-level. There is no WWOX non-canonical splice allele anywhere with a measured outcome.
9. **Per-patient consanguinity, family structure and any biobanking for Patient 39 are UNKNOWN — unavailable, not absent.**

---

## 8 · INFORMATION GAIN

| Item | Gain | One line |
|---|---|---|
| **Mechanistic graph** | 🟢 **YES** | Adds the distinction the graph did not carry: **acceptor-destroying (−1/−2) vs acceptor-weakening (−3/+5)** lesions are different nodes with different reachable outcomes, and exon 6 = 89 nt makes skipping frameshifting at this junction for **both** alleles. |
| **Therapeutic hypothesis** | 🟡 **PARTIAL** | No new hypothesis. It **sharpens the existing one** into a falsifiable precondition: RNA-RESCUE requires a *productive outcome to already exist*, which a −2 allele forbids and a −3 allele merely permits — so the class's only route into WWOX runs through non-canonical alleles, of which there are now two. |
| **Experimental roadmap** | 🔴 **NO — and this reverses today's FT-116 entry** | FT-116 scored this **🟢 YES** on *"the same acceptor, testable with the same construct"*. The construct does not exist, the lines carry the wrong allele, and the `TX-001` assay reads a different junction. What survives is smaller and true: **WSM S is the right homozygous comparator** for any future exon-5/6 assay, and WCH S is not, because it carries a missense in trans. |
| **Genotype stratification** | 🟢 **YES** | Tenth splice allele, **second non-canonical, first non-canonical acceptor**; `UNASSIGNABLE`, not RNA-RESCUE. Patient 39's trans deletion removes exon 6, making that genotype **hemizygous-equivalent** at this junction — a stratification property not previously recorded. |
| **Intervention ranking** | 🔴 **NO — deliberately** | Nothing is re-ranked. An unmeasured single-patient annotation-only allele supplies no basis for moving `TX-001`–`TX-007`, and doing so on a one-nucleotide adjacency is precisely the transfer this file rejects. |
| **Uncertainty** | 🟢 **YES** | Separates general splicing knowledge from what is measured (nothing) on every −3 row; downgrades *"2 independent iPSC lines"* to **two families in one lab with obtainability UNKNOWN and the artefact off-disk**; finds a **mood change inside a quotation** in FT-116 and a **recruitment-window error** against the artefact; finds **two registry/ledger locator and read-depth discrepancies**; and records that the measurement behind `CLAIM 018`, a `consolidated baseline`, has **no receipt at any depth**. |

---

## 9 · DEFAULTS_TAKEN

1. **No new full text read.** The single new-allele artefact was already on disk and its sha256 was re-verified before analysis (`0cf97dd0…f926b`, 52,764 bytes / 52,224 chars). Nothing was fetched.
2. **No splice predictor run, no score generated, for any allele.** Held values for `c.1057-2A>G` are **quoted** from `woree_therapeutic_class_census_20260921.md`. The `c.517-3C>A` prediction row is left **empty**, which is its true state.
3. **HGVS reproduced as published / as extracted, never normalised** — `c.517‐3c>A` keeps its lowercase `c` and U+2010 hyphen; the CNV keeps its two different dash characters. The ASCII form `c.517-3C>A` is used **only** in this file's own prose and headings, and never inside a quotation.
4. **`c.517-3C>A` classed UNASSIGNABLE, not RNA-RESCUE**, following the census's binding rule that splice-affecting alleles default away from RNA-RESCUE wherever no productive outcome has been demonstrated — i.e. everywhere.
5. **The exon-6 length and frame arithmetic (89 nt, `mod 3 = 2`) is declared as LEGEND's own arithmetic** over its verified boundary map, not as a statement by any source.
6. **The source's own moods preserved**: the allele is *"Novel"*, the genotype *"Likely pathogenic"*, the CNV *"Uncertain"*, the outcome codes *"PES, SF (6)"* reproduced with their internal tension intact and unresolved.
7. **The exon-label discrepancy for Patient 39** (*"Exons 5 to 8"* vs LEGEND's computed exons 6–8) is **not adjudicated**; every conclusion here was framed so as not to depend on it.
8. **Defects found in FT-116, `PAPER 094`, `PAPER 039` and the `TX-001` packet are reported, not repaired.** This file is READ-ONLY toward all of them, and toward every canonical file and every ledger.
9. **No contact, outreach or acquisition is proposed**, and no experiment is proposed as a plan. Section 4 states what would have to change for an assay to read this allele; it does not schedule one.

---

*Scientist B, 2026-09-21. READ-ONLY. No canonical file modified, no ledger appended, no receipt written, no commit candidate created, nothing committed or pushed. Nothing here is medical advice, and no clinical action is proposed.*
