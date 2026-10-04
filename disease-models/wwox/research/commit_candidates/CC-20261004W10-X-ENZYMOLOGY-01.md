# COMMIT CANDIDATE — CC-20261004W10-X-ENZYMOLOGY-01

**Title:** PMID 21476439 is read. Four landed statements now have a primary behind them; four do not
hold as worded.
**Actor:** Scientist X, intake wave 10, branch `task/sci-X-20261004w10`
**`context_policy`:** `SOURCE_FIRST` — the whole paper was read and the dossier's first pass written
before the residue candidate `CC-20260921-WWOX-ENZYMOLOGY-P306-01` and the registry records were
opened.
**Evidence:** `disease-models/wwox/research/fulltext_dossiers/PMID21476439.md` ·
manifest `disease-models/wwox/research/deepdive_manifests/PMID21476439.json`
(`--verify-artifacts --require-current-schema` → **PASS, 0 gaps**) ·
receipt prepared, **not recorded**: `scratchpad/receipts_pending_w10/sciX_21476439_1.json`
**Change class:** **MINOR**. No `consolidated baseline` claim is narrowed or reversed; no claim is
created. What changes is prose in two queue entries, the depth tags on one corpus/LIT pair, and one
contradiction statement that the primary shows is not a contradiction.
**Status:** `PROPOSED — NOT PROPAGATED`. Registry writes are not the scientist's; numbers are
provisional and the integrator renumbers.
**Not medical advice.**

---

## 0 · Reading-debt discharge: which landed statements now have a primary behind them

`PMID 21476439` was a cited-and-unread primary behind statements in `CORPUS P306`, `LIT-0306`,
`FT-130`, `FT-147` and the residue candidate `CC-20260921-WWOX-ENZYMOLOGY-P306-01`. It is now read
in full from the version of record.

### CONFIRMED by the primary — these statements hold as worded

| Record | Statement | Verdict |
|---|---|---|
| `FT-130` | "The measurement is on bacterially expressed fusion proteins in crude extract — not endogenous protein, not human cells, not patient-derived material, and **not a single disease allele**." | ✅ **exactly right**, and the primary is stronger than the record: purification *abolished* the activity in both expression systems, so the crude extract was a forced choice, not a shortcut. |
| `FT-147` | "heterologous expression has been reported **at least twice**" | ✅ confirmed: a NusA fusion in pET 44a(+) and a GST fusion in pGEX 2TK. |
| `FT-147` | "no purified, folded, biophysically characterised WWOX SDR protein exists" | ✅ confirmed and strengthened by the authors' own sentence that activity was lost in every purification attempt. |
| `FT-147` | "**no yield, purity, Tm or monomer fraction is reported anywhere**" | ✅ confirmed. Add: no Vmax, no kcat, no specific activity, no units, and no identification of any reaction product. |
| `CC-20260921` §2 / §2bis | crude extract · wild-type only · no disease allele · no catalytically-dead control · no folded-monomer normalisation · no physiological substrate assigned · "an activity **report** is not an **assay**" | ✅ **every one of the six caveats is confirmed by the source.** This candidate's HALF TWO was correct and remains correct. |

### DOES NOT HOLD as worded — corrections proposed below

| # | Record | Problem |
|---|---|---|
| 1 | `FT-147` | Its self-correction **over-corrected**. The retracted sentence was *"the SDR domain has never been expressed or purified by anyone"*; the paper expressed **full-length WWOX**, never an SDR-domain-only construct. Read narrowly, the retracted sentence was true. |
| 2 | `CC-20260921` §2bis | The "live contradiction" with the 2015 retinal-oxidoreductase proposal **is not a contradiction**: this paper never tested all-trans-retinal. Its negative covers seven steroids only. |
| 3 | `FT-130` | "**oxidation yes, reduction no**, across every substrate tested — a real constraint on assay design" over-weights an unillustrated negative: it is a **results-not-shown** sentence with no panel, no table and no number. |
| 4 | `FT-130` | Title and acquisition verdict (*"unacquirable, confirmed on two routes"*, *"no DOI, no PMCID"*) are superseded; and the affiliation line names only Analytical Chemistry, which **misassigns the senior author**, who is in Molecular Cancerogenesis. |

### NEW, and not in any record — found only by reading

| | |
|---|---|
| **No Vmax, ever** | Methods promise Lineweaver–Burk Km *and* Vmax; the word `Vmax` occurs once in the paper, in that sentence. No Vmax, kcat, specific activity or catalytic efficiency is reported for any substrate. |
| **The Km is a difference of two Km values** | Table II's own footnote: *"Km values are the difference between NUS-WWOX and NUS."* A difference of Michaelis constants is not a kinetic constant of a resolved enzyme. |
| **13 of 14 Km values lie below the lowest substrate concentration used** | Comparing Table II against Table I; lowest [S] / Km runs 1.06 to 4.13. Every Km but one is a double-reciprocal extrapolation from the saturated arm, which is what the asymmetric confidence intervals show (two span 3–3.5 × their own Km). |
| **The p column is unattainable** | Methods: "the means of at least two or three demonstrations". For an exact Mann–Whitney test the smallest attainable two-sided p is 0.333 at n = 2 and 0.100 at n = 3. **All 14 printed p values (0.0000–0.0091) are below that floor**, and `p = 0.0000` is not an attainable exact value. |
| **The estrone conclusion is the weakest, not the strongest** | The paper's central biological inference is that the lowest Km (estrone) means WWOX participates in estrone metabolism in vivo. Read from the panels, estrone has the **largest** empty-vector background of all seven substrates (0.80 of a 1.24 trace) and the **smallest** WWOX-specific increment (0.44). |
| **The Results text mis-ranks its own panels** | Text: host activity "3- to 6-fold lower" for 5α-DHP-allo, E and T. Measured: 2.46 ×, 1.55 ×, 1.94 × — none reaches 3. The four substrates it calls "blank level" measure 2.67–4.68 ×. The two groups are close to rank-inverted. |
| **Near-complete substrate consumption** | With ε = 6270 M⁻¹ cm⁻¹, the 30-min NAD⁺ curves correspond to 78–89 % consumption of the 0.24 µmol/ml steroid, so these are end-point, not initial-velocity, curves. |
| **A substrate-independent signal that tracks the construct** | The NUS-WWOX extract with no steroid reaches A₃₄₀ ≈ 0.23 (NAD⁺) and ≈ 0.29 (NADP⁺); with NADP⁺ that blank exceeds the entire empty-vector-plus-substrate control in all seven panels. |
| **No ladder, no blot** | Figure 1 has no molecular-weight marker lane and no size annotation in either panel, and the paper contains no Western blot, antibody or mass-spectrometric confirmation. Band identity rests on expected migration alone. |
| **Full-length only** | The cDNA was subcloned whole; there is no SDR-only construct, no WW-deleted construct, and no active-site point mutant. "The SDR domain has dehydrogenase activity" is an attribution, not a measurement on the domain. |

---

## 1 · Exact operations

> ⚠️ Every `old` below is **record-scoped** and several of these strings are not unique file-wide.
> The executor addresses the record (`FT-130`, `FT-147`, `CORPUS P306`, `LIT-0306`) and replaces
> within it. `record_scoped_edit.py` refuses an ambiguous anchor.

### OP 1 — `disease-models/wwox/research/full_text_queue_current.md` · `FT-130` · **append** (append-only surface)

Append, verbatim, at the end of the `FT-130` entry:

```text
### CORRECTION — 2026-10-04, the paper is read (Scientist X, intake wave 10)

This entry's own heading and acquisition verdict are superseded and are left standing above, labelled, rather than rewritten.

1. **"unacquirable, confirmed on two routes" is no longer the state.** The version-of-record PDF was acquired at zero spend and is held as `files/fulltext/PMID21476439_SaludaGorgul2011_DeGruyter.pdf`, sha256 `f3a43c1174c023cf9a00f45397aeb82043bbe8a37adc12c0d71f826fbbeb4505`, ten typeset pages with a clean text layer. Read in full 2026-10-04; manifest `deepdive_manifests/PMID21476439.json` PASSes with 0 gaps.
2. **"no DOI"** was already corrected elsewhere in this repository; note additionally that the article's own front matter prints **no DOI at all**. The citation line it does print is `Z. Naturforsch. 66 c, 73 - 82 (2011); received May 12/September 14, 2010`. Any DOI carried for this paper is a publisher assignment resolvable to it, not an identifier on the article.
3. **The affiliation line here names only the Department of Analytical Chemistry, which misassigns the senior author.** The article carries two departments of the Medical University of Lodz: Analytical Chemistry (first author) and **Molecular Cancerogenesis** (the corresponding author and two co-authors). The capability mapping this entry builds should name the second.
4. **The oxidation-yes / reduction-no asymmetry is narrower than this entry treats it.** The negative is a single Results sentence marked **"results not shown"**: no panel, no table, no number, no statistic, and it covers **the seven steroid substrates only**. It is a weak, unillustrated negative and must not be carried as a hard constraint on assay design.
5. **It establishes less than "a measurable activity, defined substrates, and a cofactor requirement" implies.** No Vmax, kcat, specific activity or unit of enzyme is reported; no reaction product was identified by any method; and Table II's own footnote says the reported Km values are *the difference between NUS-WWOX and NUS*.
6. **"the only published measurement of WWOX catalysis that exists"** is a claim about the literature this entry cannot make, and is scoped here as `CORPUS P306` was already scoped: *the only one identified in the corpus read here*, `PREMISE: INFERENZA`.
```

### OP 2 — `disease-models/wwox/research/full_text_queue_current.md` · `FT-147` · **append**

```text
### CORRECTION — 2026-10-04, the correction was itself too strong (Scientist X, intake wave 10)

This entry retracted the sentence *"the SDR domain has never been expressed or purified by anyone"* on the strength of PMID 21476439's abstract. With the paper now read in full: the construct is the **full-length WWOX cDNA**, subcloned whole as a BamHI/EcoRI fragment into pET 44a(+) and into pGEX 2TK. **No SDR-domain-only construct was made, and none was purified** - purification abolished the activity in both systems. So the retracted sentence was over-retracted: *WWOX* has been heterologously expressed twice, but *the SDR domain* has not been expressed on its own by this paper, and this paper was the sole basis for the retraction.

The practical consequence runs the other way from the one recorded here: this paper **does not** lower the cost estimate for a purified-SDR route, because it supplies no construct boundary for the domain, no purification protocol that preserves activity, and no yield. What it does supply is a documented failure mode - activity lost on both glutathione-sepharose and cobalt affinity resin - which is worth more to a protocol designer than the expression precedent was.

**REVIVAL_TRIGGER, adjudicated: it does NOT fire.** The trigger was *"if this body reports purified enzyme with a dead-triad control"*. The body reports neither: no purified enzyme (stated explicitly), and no catalytically-dead mutant of any kind - not of the YNRSK substrate motif at 293-297, not of the GANSGIG cofactor motif at 131-137. A purified-protein specific-activity assay therefore does **not** displace the engagement assay on this evidence.
```

### OP 3 — `paper_registry_current.md` · `CORPUS P306` (record-scoped)

- `replace-within`: old `**Status:** screened — corpus placeholder`
  → new `**Status:** read in full 2026-10-04 — receipt and manifest exist; still a corpus placeholder pending promotion`
- `replace-within` within the `Role` line: old
  `(`PREMISE: INFERENZA`; abstract depth, no receipt, no locator)`
  → new
  `(`PREMISE: INFERENZA` for the *only-one* scoping; the paper itself is now READ IN FULL — receipt `FTR-20261004-21476439-01`, manifest `deepdive_manifests/PMID21476439.json`, 17 verbatim locators)`
- `replace-within` within the `Note`: old
  `dehydrogenase activity on steroid substrates with NAD⁺ and NADP⁺ and published Km values, oxidation only (abstract depth; `PREMISE: UNREAD_PRIMARY`, no receipt, no locator).`
  → new
  `dehydrogenase activity on seven steroid substrates with NAD⁺ and NADP⁺ and published apparent Km values, oxidation only. 🔵 **READ IN FULL 2026-10-04** (`FTR-20261004-21476439-01`): the activity is in an unfractionated bacterial crude extract because purification abolished it; the protein is WILD-TYPE FULL-LENGTH human WWOX, no allele and no domain-only construct; **no Vmax, kcat, specific activity or reaction product is reported**; Table II's footnote states the Km values are the DIFFERENCE between the WWOX and empty-vector extracts; 13 of the 14 Km values lie below the lowest substrate concentration Table I used; and all 14 printed Mann-Whitney p values are below the floor attainable with the stated n of two or three. The reduction negative is a results-not-shown sentence. See `CC-20261004W10-X-ENZYMOLOGY-01`.`

### OP 4 — `literature_tracking_log_current.md` · `LIT-0306` (record-scoped)

- `replace-within`: old `**Current status:** queued for deep-dive — A; unacquired, not unread`
  → new `**Current status:** READ IN FULL 2026-10-04 — version-of-record PDF held, receipt FTR-20261004-21476439-01, manifest PASS 0 gaps`
- `replace-within`: old `**Date processed:** triage only` → new `**Date processed:** 2026-10-04`
- `replace-within`: old
  `**Next action:** record as UNACQUIRED, not unread — hybrid-OA publisher PDF exists at DOI 10.1515/znc-2011-1-210 and is blocked only by an automated-traffic challenge; one human fetch closes it (FT-130 / packet A11). Do not re-run automated acquisition.`
  → new
  `**Next action:** none for acquisition — acquired and read 2026-10-04. Open reading debt moves to its references: PMID 10786676 (the sole source of the GANSGIG and YNRSK motif annotations this paper's interpretation rests on), PMID 11896615 and PMID 12829805. See the manifest's multihop block.`

### OP 5 — `disease-models/wwox/research/commit_candidates/CC-20260921-WWOX-ENZYMOLOGY-P306-01.md` · **append** a dated disposition

> ⚠️ **Executor note.** The first line below is written here as `## <DISPOSITION-HEADING>` on
> purpose. Expand it to the queue's standard batch-disposition h2 heading when appending, reading
> `— intake wave 10 (2026-10-04, ACTOR_ID scientist, Scientist X), append-only`. It is held back
> because `growth_anchors.py` parses that literal heading wherever it appears and would read a
> disposition block quoted inside a candidate as a disposition **of** that candidate.

```text
## <DISPOSITION-HEADING> — intake wave 10 (2026-10-04, ACTOR_ID scientist, Scientist X), append-only

**Nothing above this line was rewritten.**

**Verdict: the paper is READ; HALF ONE and HALF TWO both survive, and one paragraph does not.**

**HALF ONE** (treat the 2011 result as a real historical biochemical result) - upheld. It is a real primary with a real substrate panel, real cofactor dependence and real apparent Km values. **HALF TWO** (it is not a validated functional assay for disease alleles) - upheld in every particular: crude extract, wild-type full-length protein only, no disease allele, no catalytically-dead control, no folded-monomer normalisation, no physiological substrate assigned. The reading adds that there is also **no Vmax, no product identification, no molecular-weight marker and no immunodetection**, and that Table II's Km is a *difference* between two extracts.

🔴 **The one paragraph that does not survive is §2bis's "live contradiction".** It states that a 2015 review proposing a reversible retinal oxidoreductase and this 2011 primary *"disagree on reversibility, which is the one property an assay design must choose"*. **They do not disagree.** This paper never tested all-trans-retinal: its no-reduction sentence covers the SAME SEVEN STEROIDS with NADH/NADPH, and is reported as **"results not shown"** - no panel, no table, no number. A negative on seven steroids says nothing about a different substrate, and an unillustrated negative is weak evidence even on the substrates it covers. The corrected statement: **the two proposals concern different substrates and have never been tested against each other; there is no contradiction on the record, only an untested question.** The sentence *"no experiment has ever been run that could tell them apart"* is the part that stands.

**§4(c) (the TX-003 obstacle line) is now writable, and this is what survives of it.** The proposed wording - *"measured in-vitro dehydrogenase activity on steroid substrates with both NAD+ and NADP+, and published Km values; oxidation only"* - is supported, with three qualifications that must travel with it: (i) "measured" means measured on a crude lysate containing a WWOX fusion, never on resolved WWOX, and no construct ties the activity to the SDR active site; (ii) the Km values are apparent, are differences between two extracts, and 13 of 14 were extrapolated from above saturation; (iii) "oxidation only" is a results-not-shown negative over seven steroids. **TX-003's score still does not move**, for the reason §5 already gives: a wild-type in-vitro activity with no allele arm changes the description of the blocker, not the probability of the strategy. Whether to write it is the integrator's call, not this reader's.

**Not medical advice.**
```

---

## 2 · What is explicitly REFUSED

- ❌ **No claim is created.** A wild-type bacterial-lysate activity supports no canonical claim about
  the disease.
- ❌ **No allele-level statement of any kind.** The paper tests no variant; P47T ≠ Q230P ≠ G372R ≠
  A141T ≠ P252A and none of them appears here.
- ❌ **No promotion of `CORPUS P306` to a `PAPER` record by this candidate.** The registry landing is
  proposed separately in `CC-20261004W10-X-REGISTRY-01` so the two can be taken independently.
- ❌ **No `TX-003` edit.** §4(c) is adjudicated above, not applied.
- ❌ **No neurosteroid bridge**, and no inference from steroid substrates to a neural substrate.
- ❌ **No change to any ratchet, gate or ceiling.**

## 3 · Growth delta

`claims +0 · papers +0 · corpus +0`. Two queue appends, one corpus/LIT depth update, one candidate
disposition.

---

### LOCATOR TRIPLES FOR BLIND AUDIT

Artefacts on disk, verified by sha256 in `deepdive_manifests/PMID21476439.json`:
`files/fulltext/PMID21476439_SaludaGorgul2011_DeGruyter.txt` (article text, derived),
`files/figures/PMID21476439/page03_fig1_gels.png`,
`files/figures/PMID21476439/page04_fig2_indanol.png`,
`files/figures/PMID21476439/page06_fig3A_NAD.png`,
`files/figures/PMID21476439/page07_fig3B_NADP.png`,
`files/figures/PMID21476439/page08_tableII_rotated.png`.

(The article's citation line is Z. Naturforsch. 66 c, 73-82 (2011) | `Z. Naturforsch. 66 c, 73 – 82 (2011); received May 12/September 14, 2010` | front matter, citation line)

(The construct expressed is the full-length WWOX cDNA, subcloned as a BamHI/EcoRI fragment | `BamHI and EcoRI enzymes was subcloned from` | Experimental, Expression and soluble fraction with WWOX fusion protein)

(Every kinetic measurement was made on an unfractionated bacterial crude extract because purification abolished the activity | `oxidoreductase activity was lost in` | Results, NUS-WWOX and GST-WWOX fusion proteins extraction)

(The Methods promise a Vmax from Lineweaver-Burk fitting | `ics method, and Lineweaver-Burk analysis was` | Experimental, Enzyme assays)

(The stated replication is two or three demonstrations | `means of at least two or three demonstrations.` | Experimental, Enzyme assays)

(The absence of reduction activity is reported without any panel, table or number | `(results not shown), which indicates that the` | Results, reduction activities paragraph)

(The authors describe 0.24 micromol/ml steroid as sufficient or excessive for the 30-minute NAD+ reactions | `at 0.24 μmol/ml was sufﬁcient or even excessive` | Results, Dehydrogenase activity of SDR domain in the WWOX protein)

(The highest reported Km values are for 5-alpha-androstane-3,17-dione with NAD+ and testosterone with NADP+ | `(5.864 · 10–5 M) and testosterone (14.551 · 10–5 M)` | Results, closing paragraph)

(Table II's footnote states the reported Km values are a difference between two extracts | `Km values are the difference between NUS-WWOX and NUS.` | Table II footnote)

(Table I records the substrate concentration ranges used for the kinetics | `5α-Androstane-3,17-dione (5α-A)` | Table I, first row)

(The two sequence motifs the SDR interpretation rests on are cited to an earlier paper, not measured here | `GANSGIG at position 131 – 137 and the poten-` | Introduction)

(Figure 2's curves are from one of two experiments | `The curves shown are from one of two experiments, each` | Figure 2 caption)

(Neither SDS-PAGE panel carries a molecular-weight ladder lane or any size annotation | `[figure attestation — pixels cannot be quote-matched] Page 75, Figure 1. Panel A: three lanes numbered 1, 2, 3, no marker lane, no kDa labels; lane 1 carries an intense mid-gel band that is absent from lane 3, where a new slower-migrating band appears near the top. Panel B: four lanes numbered 1, 2, 3, 4, no marker lane, no kDa labels; lane 1 carries an intense low band, lane 3 a prominent higher band plus a strong mid band, lanes 2 and 4 neither.` | Figure 1, panels A and B, page 75)

(The empty-vector NusA control carries roughly 45 per cent of the NUS-WWOX signal on S-indan-1-ol, and the two expression systems disagree in magnitude | `[figure attestation — pixels cannot be quote-matched] Page 76, Figure 2. Panel A y-axis 0 to 1, NUS-WWOX filled markers plateau near 0.95 by 20 min, NUS open markers rise steadily to about 0.43 at 30 min. Panel B y-axis 0 to 1, GST-WWOX filled markers plateau near 0.47 by 15 min, GST open markers reach about 0.07 at 30 min. No error bars on any point of either panel.` | Figure 2, panels A and B, page 76)

(For estrone the empty-vector-plus-substrate trace is the largest host background of all seven substrates, and the WWOX extract without steroid still reaches about a quarter of the signal | `[figure attestation — pixels cannot be quote-matched] Page 78, Figure 3A, NAD+. In-figure legend: open triangle NUS NO SUBSTRATE, filled triangle NUS-WWOX NO SUBSTRATE, open circle NUS WITH SUBSTRATE, filled circle NUS-WWOX WITH SUBSTRATE. End-point values at 30 min, filled circle / open circle / filled triangle / open triangle: 5alpha-DHP-allo 1.18 / 0.48 / 0.22 / 0; progesterone 1.11 / 0.28 / 0.23 / 0; 5alpha-A 0.80 / 0.30 / 0.23 / 0; 4-A 1.33 / 0.39 / 0.22 / 0; 17beta-E 1.03 / 0.22 / 0.24 / 0; estrone 1.24 / 0.80 / 0.24 / 0; testosterone 1.34 / 0.69 / 0.23 / 0.` | Figure 3A, all seven panels and the trace legend, page 78)

(With NADP+ the substrate-free WWOX trace exceeds the entire empty-vector-plus-substrate control in every panel | `[figure attestation — pixels cannot be quote-matched] Page 79, Figure 3B, NADP+, y-axis 0 to 1. End-point values at 30 min, filled square NUS-WWOX with substrate / open square NUS with substrate / filled diamond NUS-WWOX no substrate / open diamond NUS no substrate: 5alpha-DHP-allo 0.90 still rising / 0.145 / 0.29 / 0; progesterone 0.57 / 0.11 / 0.29 / 0; 5alpha-A 0.56 / 0.065 / 0.29 / 0; 4-A 0.55 / 0.08 / 0.29 / 0; 17beta-E 0.51 / 0.155 / 0.29 / 0; estrone 0.49 / 0.14 / 0.29 / 0; testosterone 0.52 / 0.07 / 0.29 / 0.` | Figure 3B, all seven panels, page 79)

(Table II has no Vmax column, and its row order is 5-alpha-A, 4-A, 17-beta-E, estrone, 5-alpha-DHP-allo, progesterone, testosterone | `[figure attestation — pixels cannot be quote-matched] Page 80, Table II upright. Columns: Substrate, then NAD+ (Km 10^-5 M, C.I. for 95%, p<0.05) and NADP+ (same three). Rows: 5alpha-A 5.864 / 4.42-8.72 / 0.0011 and 2.620 / 2.36-2.94 / 0.0000; 4-A 3.632 / 2.79-5.20 / 0.0006 and 3.703 / 2.81-5.43 / 0.0003; 17beta-E 3.123 / 2.62-3.87 / 0.0002 and 3.359 / 1.96-13.79 / 0.0091; estrone 1.523 / 1.11-2.42 / 0.0009 and 1.998 / 1.47-3.13 / 0.0007; 5alpha-DHP-allo 3.985 / 2.80-6.93 / 0.0016 and 4.702 / 3.24-8.56 / 0.0017; progesterone 4.219 / 2.82-8.34 / 0.0023 and 3.021 / 2.48-3.92 / 0.0001; testosterone 4.161 / 3.13-6.19 / 0.0010 and 14.551 / 8.40-54.47 / 0.0025. No Vmax column appears.` | Table II, page 80, rendered upright)
