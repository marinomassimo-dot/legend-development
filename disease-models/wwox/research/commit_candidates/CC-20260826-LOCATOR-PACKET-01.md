# LOCATOR PACKET — independent blind verification, MAJOR changes of 2026-08-26

**Packet ID:** CC-20260826-LOCATOR-PACKET-01
**Date:** 2026-08-26
**For:** Mirror, or any reviewer performing a `legend-locator-audit`
**Status:** verification instrument. **Asserts no claim and changes nothing.**

---

## 🔴 NORMALISATION CONTRACT — read before matching a single quote

**This packet has 14 entries.** An earlier summary said 13; that count was never run.

**Every quote below is matchable only under the repository's own normalisation.** A naive
substring match will fail on **7 of 14 entries** and the failures are *artefacts of the matcher*,
not defects in the locators. That was established by trying to falsify this packet before
shipping it — see §Precheck.

Match with, and only with:

```python
# framework/scripts/deepdive_manifest.py :: _normalise_text
re.sub(r"\s+", " ", unicodedata.normalize("NFKC", html.unescape(text)))
```

and, for XML/HTML surfaces, strip tags to **nothing**:

```python
re.sub(r"<[^>]+>", "", body)      # NOT  re.sub(r"<[^>]+>", " ", body)
```

Three reasons this matters, each of which produced a false failure in the precheck:

1. **Ligatures.** `U+FB01 ﬁ` and `U+FB02 ﬂ` appear in the printed text layer where the page shows
   `fi` / `fl`. `L-037-c` contains two. **NFKC folds them; nothing else does.**
   ⚠️ **25 of 55 local PDFs carry ligature characters**, and neither `deepdive_manifest.py`'s
   SUSPECT screen nor `surface_census.py` looks for them — they are handled silently by NFKC and
   are invisible to a reviewer who does not normalise.
2. **Inline markup boundaries.** Gene names sit in `<italic>` runs. Stripping tags to a *space*
   turns `Wwox−/−` into `Wwox −/−` and breaks six quotes that straddle the boundary.
3. **Prime and minus characters.** `″` folds to `′′`, `−` is U+2212 not a hyphen.

🔴 **If a quote fails to match, apply this contract before recording a mismatch.** A mismatch that
survives the contract is a real finding and should be reported loudly.

---

## How to use this packet

Each entry gives you a **surface**, a **way to reach it**, and **one fact to check**. Answer only:

1. **Does the surface contain the stated fact, verbatim or at the stated panel?** `YES` / `NO` / `PARTIAL`
2. **Does the surface say MORE or LESS than the stated fact?**

🔴 **You are not being asked whether any conclusion follows.** Each entry carries a `DO_NOT_INFER`
line naming the inference that is *not* being asked about. The candidates that these locators
support are deliberately **not** cited here, so that a `NO` verdict is available to you without
having to contradict a narrative.

**Surface classes used below, because they are not interchangeable:**

| Class | Meaning |
|---|---|
| `structured_text` | publisher JATS/PMC markup. Quotes are matchable character-for-character |
| `pdf_text_dump` | 🔴 markup or `.txt` wrapping a **PDF text layer**. Rule 5d: quotes here may differ from the printed page. **Adjudicate against the rendered page** |
| `rendered_page` | pixels rendered from a PDF at a declared dpi and rect |
| `figure_raster` | a published image file, read at native resolution |

---

## GROUP A — the `CLAIM 037` / `CLAIM 005` basis (MAJOR: a headline deleted as false)

### `L-037-a` · does the source say "absent", or does it say "not reported"?

- **SOURCE_ID:** PMID 19500159 — Suzuki et al. 2009, *Genes Brain Behav* 8:650–660
- **ARTIFACT:** `files/fulltext/PMID19500159_Suzuki2009.pdf`
  · `sha256 e1a0a87dc7faac002c20f060293aa7f6962f8ba61105bf6237e72bc4a0dd5c56`
- ⚠️ **The co-located `PMID19500159_Suzuki2009.html` is a `pdf_text_dump`**, not publisher markup
  (`surface_census.py` classifies it as such). Use the PDF and the rendered page.
- **PAGE:** 2 (Introduction)
- **VERBATIM_LOCATOR:**
  > *"Although neither epileptic seizures nor abnormal behavior **has been reported** in Wwox KO
  > (knockout) mice, our preliminary experiments showed that sound stimulation often induced WR in
  > lde/lde rats."*
- **EXPECTED_FACT_TO_VERIFY:** the sentence's predicate about KO mice is **"has been reported"**
  (a statement about the literature) and **not** a statement that the phenotype is absent in the
  animal.
- **DO_NOT_INFER:** whether Wwox KO mice do or do not have seizures. That is not what this entry
  asks.

### `L-037-b` · Table 2 — what does an empty cell mean here?

- **SOURCE_ID / ARTIFACT:** as `L-037-a`
- **PAGE / TABLE:** page 9, **Table 2**, *"Phenotypic comparison in the WWOX mutated animals"*
- **VISUAL_RECIPE:** `source_pdf_sha256 e1a0a87d…` · page `9` · crop rect (PDF pt)
  `(40.00, 60.00, 560.00, 470.00)` · **400 dpi** → 2890 × 2279 px ·
  `image_sha256 290cfc8b31d59afc810ca717eca92ce233d568a2e898614feabb7241d329dba5`
- **EXPECTED_FACT_TO_VERIFY:** three things, independently.
  (a) The `Epilepsy` row is **empty in both mouse columns** (`*Wwox⁻/⁻`, `†Wwox^gt/gt`) and filled
  only for `lde/lde`.
  (b) The footnotes read `*Data from Aqeilan et al. 2007, 2008, and 2009.` and
  `†Data from Ludes-Meyers et al. 2007.` — i.e. the mouse columns are **sourced to a fixed set of
  prior papers**.
  (c) The `Viability` row gives `†Wwox^gt/gt` as **2 years**.
- **DO_NOT_INFER:** that an empty cell implies absence, or that it implies presence. Report only
  what the cell and its footnote contain.

### `L-037-c` · the authors' own word for the mouse negative

- **SOURCE_ID / ARTIFACT:** as `L-037-a` · **PAGE:** 9–10 (Discussion, spanning the column break)
- **VERBATIM_LOCATOR:**
  > *"Although the reason for **no detection** of spontaneous epilepsy in the KO mice is unknown,
  > in addition to genetic background and species specificity influencing on survival and
  > epileptogenesis, the KO mice **may** die before they experience epileptic seizure."*
- **EXPECTED_FACT_TO_VERIFY:** the phrase is **"no detection"**, and the die-first explanation is
  offered with the modal **"may"** as one of three candidate reasons — not asserted.
- **DO_NOT_INFER:** whether the die-first explanation is correct.

---

## GROUP B — the falsifiers (MAJOR: they are what makes the headline false)

### `L-016-a` · spontaneous seizures in a `Wwox⁻/⁻` mouse

- **SOURCE_ID:** PMID 32000863 — Cheng et al. 2020, *Acta Neuropathol Commun* 8:6
- **ARTIFACT:** `files/fulltext/PMID32000863_Cheng2020_PMC.xml` · `structured_text`
  (sha256 as declared in `deepdive_manifests/PMID32000863.json`)
- **SECTION:** Results, *"Defective CNS development…"* narrative
- **VERBATIM_LOCATOR:**
  > *"In our generated Wwox−/− mice, spontaneous epileptic seizures were commonly observed after
  > postnatal day 12. Seizures were frequently induced by mild stressors including noise, strobe
  > lights and novel cage during routine handling (Additional file 2: Movie S1)."*
- **EXPECTED_FACT_TO_VERIFY:** the sentence exists; it concerns `Wwox−/−` **mice**; the detection
  method named is **routine handling plus one movie**, with **no scored protocol, no denominator
  and no rate**.
- **DO_NOT_INFER:** a penetrance figure, or that this is or is not adequate evidence.

### `L-016-b` · provoked seizure susceptibility and its control genotypes

- **SOURCE_ID / ARTIFACT:** as `L-016-a` · **SECTION:** Results, convulsant models; **Fig. 7a–b**
- **VERBATIM_LOCATOR:**
  > *"Half of the pilocarpine- or PTZ-injected Wwox−/− mice evolved into status epilepticus (SE,
  > defined as three or more tonic-clonic seizures during 1-h observation). SE was not observed in
  > Wwox+/+ and Wwox+/− mice."*
- **EXPECTED_FACT_TO_VERIFY:** SE occurred in `−/−` and **not** in either `+/+` or `+/−`.
- **DO_NOT_INFER:** anything about lithium or about genotype-specific drug response. ⚠️ A separate,
  already-canonical boundary covers that and is **not** under review here.

### `L-011-a` · spike-wave discharges in a `Wwox`-null mouse, and their rescue

- **SOURCE_ID:** PMID 42422765 — Obeid et al. 2026, *Mol Ther Methods Clin Dev* 34:201791
- **ARTIFACT:** `files/fulltext/PMID42422765_Obeid2026_PMC.html` · `structured_text` ·
  `sha256 00fadaf411998f4e453f…`
- **FIGURE:** Figure 7, panel **E** (legend)
- **VERBATIM_LOCATOR:**
  > *"(E) Quantification of SWD events per animal across groups (WT, KO, and KO + AAV9-hSynI-hWWOX
  > [HD]). WWOX KO pups exhibited a significantly higher number of SWDs relative to WT, whereas
  > WWOX-rescued pups (HD) showed a marked reduction in SWD incidence. Data are presented as
  > mean ± SEM (n = 5 pups per group). Statistical significance was determined using Student's t
  > test. ∗∗∗∗p < 0.0001; ns, non-significant."*
- **EXPECTED_FACT_TO_VERIFY:** SWDs are measured **in the KO mouse**, `n = 5` per group, with
  `∗∗∗∗p < 0.0001`.
- **DO_NOT_INFER:** that SWD is or is not equivalent to a clinical seizure; that the result does or
  does not transfer to humans.

### `L-011-b` · the recording method

- **SOURCE_ID / ARTIFACT:** as `L-011-a` · **SECTION:** Methods, *"Surgery and ECoG data acquisition"*
- **VERBATIM_LOCATOR:**
  > *"Immediately after surgery, continuous wireless ECoG acquisition was initiated without a
  > recovery interval. Recordings were maintained for 7 consecutive days… ECoG traces were manually
  > screened for interictal spikes and SWDs by a blinded investigator."*
- **EXPECTED_FACT_TO_VERIFY:** three properties — recording began **with no recovery interval**;
  it ran **7 consecutive days**; the reader was **blinded**. Also confirm the electrode count:
  the same Methods paragraph should state a **single-channel** transmitter with one recording and
  one reference electrode.
- **DO_NOT_INFER:** whether the absence of a recovery interval did or did not affect the result.

### `L-011-c` · 🔴 a printed p-value against a plotted point count

- **SOURCE_ID / ARTIFACT:** `files/fulltext/figures/PMID42422765/gr7.jpg` · `figure_raster` ·
  `sha256 3a01e962c0cb5d6986f4c0cd5d57aeaaf1107d36679cc6828bcf67e11425ce7c`
- **FIGURE:** Figure 7, panels **B** and **C**
- **VISUAL_RECIPE:** open at native resolution and magnify panel C until individual plotted points
  are separable (~9× has been sufficient).
- **EXPECTED_FACT_TO_VERIFY:** three counts, reported independently.
  (a) The number printed over the WT-vs-KO bracket in panel **C**.
  (b) The number of plotted points in the **KO** group of panel C.
  (c) The number of plotted points in the **WT** group of panel C.
  Then: does panel **B** carry any significance marker at all?
- **DO_NOT_INFER:** what the printed number means statistically. Report the digits and the counts.
  ⚠️ This entry exists because the running text and the panel are believed to disagree; **do not
  read the running text before answering**, and say so if you already have.

---

## GROUP C — the dose adjudication (MAJOR: a `consolidated baseline` quantity qualified)

### `L-DOSE-a` · what is in the Repudi vector cassettes?

- **SOURCE_ID:** PMID 34747138 — Repudi et al. 2021, *EMBO Mol Med* 13:e14599, **Appendix**
- **ARTIFACT:** `files/fulltext/figures/PMID34747138/EMMM-13-e14599-s001.pdf`
  · `sha256 1e5c30a903d96726cffae487e14f2e80593e4a6adf2e8b08efb70a5762f86cd2`
- **FIGURE:** Appendix Fig **S1**, panel **A**
- **VISUAL_RECIPE:** page `2` · full page rect `(0.00, 0.00, 510.00, 567.00)` pt · **300 dpi** →
  2125 × 2363 px · `image_sha256 e362bdf80c8d850bb32859d20ff39d6264569f1332cb7455fdc649aac61f9c02`
- **EXPECTED_FACT_TO_VERIFY:** transcribe, element by element, the cassette printed for each of
  `AAV-mWwox`, `AAV-hWWOX` and `AAV-GFP`. State explicitly, for each, **whether a `WPRE` element
  is drawn**.
- **DO_NOT_INFER:** what the presence or absence of WPRE implies about any dose comparison.

### `L-DOSE-b` · the matched-dose statement in the other paper

- **SOURCE_ID / ARTIFACT:** as `L-011-a` (`structured_text`) · **SECTION:** Results, WPRE removal
- **VERBATIM_LOCATOR:**
  > *"At a dose of 4 × 10¹⁰ vg, exclusion of WPRE was insufficient to rescue lethality in KO mice,
  > whereas treatment with WPRE-containing vectors at the same dose resulted in survival rates
  > comparable to WT (Figure 2B). … Increasing the dose of the WPRE-lacking vector to 8 × 10¹⁰ vg
  > was associated with improved outcomes, including rescue of lethality…"*
- **EXPECTED_FACT_TO_VERIFY:** the two doses (`4 × 10¹⁰`, `8 × 10¹⁰`) and which arm each is said
  to rescue.
- **DO_NOT_INFER:** any comparison with any other paper's dose.

### `L-DOSE-c` · how long was each survival experiment followed?

- **ARTIFACTS AND RECIPES:**
  - `files/fulltext/figures/PMID42422765/gr2.jpg` — Figure 2, panel **B**.
    Crop `(0, 0, 726, 320)` of 726 × 942, ×3 →
    `image_sha256 bd2b6d9b1f6b2dc86ae4e9f04db6c5ebf876171f4cada402cd60cdf9f1b8c2b4`
  - `files/fulltext/figures/PMID42422765/gr3.jpg` — Figure 3, panel **B**.
    Crop `(436, 0, 726, 297)` of 726 × 708, ×4.5 →
    `image_sha256 4c6f2fdd31867e96ce450eacdc4222e82ddb85a8e3624e85adbc66ddd586b996`
  - `files/fulltext/figures/PMID34747138/EMMM-13-e14599_article.pdf`
    (`sha256 32ee98733a6f45550f6b924b701734e111d171992ecba2535f0c32a5e105b438`) — Figure **2C**.
    Page `4` · rect `(400.00, 70.00, 545.00, 205.00)` pt · **600 dpi** →
    `image_sha256 ac41ab21703026d593a30a18ced4dba09a038455df7528844e55956cdb3972fd`
- **EXPECTED_FACT_TO_VERIFY:** for each of the three panels, report **(i) the maximum value on the
  x-axis** and **(ii) the terminal survival fraction of each plotted arm**, with the legend `n` for
  each arm.
- **DO_NOT_INFER:** whether any arm "rescued" anything. The word is not being tested — the axes are.

⚠️ `gr2.jpg` and `gr3.jpg` are **PMC CDN renditions at 726 px wide**, not native originals. If a
tick label is not legible at that resolution, report `ILLEGIBLE` rather than estimating.

---

## GROUP D — the other mouse genotype (supports a Title rewrite)

### `L-007-a` · video-EEG in a non-null mouse

- **SOURCE_ID:** PMID 36828035 — Hussain et al. 2023, *Prog Neurobiol* 223:102425
- **ARTIFACT:** `files/fulltext/PMID36828035_Hussain2023_PMC.xml` · `structured_text` ·
  `sha256 004c59b54b5f57e462ccb39643b5f3adb44e7ecaef5eff8d786cb77c3568fd22`
- **SECTION:** Results 2.3
- **VERBATIM_LOCATOR:**
  > *"We detected very frequent interictal cortical spike discharges (0–3098/hour) … repeated
  > spontaneous generalized convulsive activity (11–22 seizures during 43–53 h monitoring periods)
  > … Wildtype mice displayed infrequent spike activity (0–68/hour) but no evidence of seizures."*
- **EXPECTED_FACT_TO_VERIFY:** the genotype these numbers describe (state it exactly as printed),
  the group sizes, and whether the animals are adult or juvenile.
- **DO_NOT_INFER:** that this genotype is or is not equivalent to a null.

### `L-007-b` · the montage and the recovery interval

- **SOURCE_ID / ARTIFACT:** as `L-007-a` · **SECTION:** Methods 4.4
- **VERBATIM_LOCATOR:**
  > *"silver wire electrodes (0.005″ diameter) soldered to a connector were surgically implanted
  > bilaterally into the subdural space over frontal and parietal cortex. Mice were allowed to
  > recover for 14 days before recording."*
- **EXPECTED_FACT_TO_VERIFY:** the number of recording sites implied, and the recovery interval.
- **DO_NOT_INFER:** that either property makes this study better or worse than any other.

---

## GROUP E — the abundance/function pair (supports a premise tag, not a claim reversal)

### `L-007-c` · protein level versus binding

- **ARTIFACT:** `files/fulltext/PMID36828035_Hussain2023_assets/nihms-1957654-f0001.jpg` ·
  `figure_raster` · `sha256 3a8e73046dd28bb4…` · 1801 × 1412
- **FIGURE:** Figure 1, panel **a**
- **VISUAL_RECIPE:** open at native resolution.
- **EXPECTED_FACT_TO_VERIFY:** for each of the four blots labelled `Anti-Wwox - Dvl2 pulldown`,
  `Anti-Wwox - Wbp1 pulldown`, `Anti-Wwox - 10% input`, `Anti-Hsp90`, report whether the
  `P47T/P47T` lanes carry band intensity **comparable to** or **markedly weaker than** the `WT/WT`
  lanes. Also report **how many lanes per genotype** are present.
- **DO_NOT_INFER:** that this generalises to any other WWOX variant.

---

## §Precheck — I tried to falsify this packet before shipping it

**Result: 14/14 entries sound. Zero content defects. One documentation defect, now fixed above.**

| Check | Result |
|---|---|
| `SOURCE_EXISTS` — artifact present in the shared checkout | **14/14** |
| Text quotes present in declared artifact, under the contract | **18/18 fragments** |
| Image source digests match published values | **7/7** |
| Image recipes **re-run** to the published `image_sha256` | **5/5 byte-identical** |

🔴 **Two "defects" I found and then had to withdraw, recorded because the withdrawal is the
lesson.**

1. **I reported `L-037-c` as carrying a wrong quote.** My matcher showed the surface reads
   `speciﬁcity`/`inﬂuencing` with ligatures while my quote had ASCII. **Withdrawn:** the
   repository normalises NFKC, which folds exactly those, and the quote matches. What I had
   actually found was that *my verifier* did not implement the repository's contract.
2. **I reported that the pre-existing canonical locator `deepdive_manifests/PMID19500159.json`
   `entries[1]` does not match its own declared artifact.** **Withdrawn on the same ground** —
   it matches under NFKC, and `deepdive_manifest.py --verify-artifacts` correctly returns `PASS`.
   ⚠️ I was one step from filing a canonical-state defect against a manifest that is fine.

**The general shape:** *"the gold is wrong"* and *"my instrument is wrong"* produce identical
output, and the second is far more likely. The discriminator is to run the repository's own
validator against the same object before believing your own matcher — which is what settled both.

### Per-entry adversarial notes

Fields the operator asked for that were not already in each entry. `SOURCE_EXISTS` = yes and
`SURFACE_CLASS` / `PAGE` / `RECIPE` / `FACT` / `DO_NOT_INFER` are in the entries themselves.

| Entry | ALTERNATIVE_READING a reviewer could reach | FAILURE_IF_LOCATOR_WRONG |
|---|---|---|
| `L-037-a` | *"has been reported"* could be read as the authors merely being polite about an absence they believe real | 🔴 **The whole `CLAIM 037` Title repair loses its cleanest support.** Not fatal — Cheng 2020, Repudi 2021, Obeid 2026 falsify the clause independently |
| `L-037-b` | An empty table cell could mean "tested, negative" rather than "not reported". **The footnotes are what decide it**, and a reviewer who reads only the row will reach the wrong reading | The `NOT_REPORTED ≠ ABSENT` framing weakens to an inference. ⚠️ **Table columns are separate text runs** — a text-layer extraction will not preserve alignment; adjudicate at the crop |
| `L-037-c` | *"may die before"* could be read as the authors' preferred explanation rather than one of three | Δ2's deletion of *"i topi potrebbero morire prima"* loses its warrant |
| `L-016-a` | *"commonly observed"* without a denominator could be a strong claim or a weak one | 🔴 **The earliest falsifier (2020) is lost and the mouse-seizure date moves to 2026** — which is what the superseded candidate wrongly asserted |
| `L-016-b` | SE absent in `+/+` and `+/−` could reflect dose choice rather than genotype | The provoked-susceptibility axis weakens; spontaneous axis unaffected |
| `L-011-a` | `∗∗∗∗` with n=5 and a t-test on possibly non-normal count data could be over-stated | 🔴 **`CLAIM 040` cannot be proposed.** The rescue triad is the only one in the corpus |
| `L-011-b` | "blinded investigator" may cover screening but not event definition | The methodological contrast with `PAPER 007` softens; the SWD result stands |
| `L-011-c` | 🔴 **The printed `0.2000` could be a real negative rather than a rank-test floor.** A reviewer who counts 5 and 5 points instead of 3 and 2 reaches the opposite conclusion | The `UNRESOLVED` verdict on spike rate collapses to either "significant" (text) or "not different" (naive panel read) — **both wrong** |
| `L-DOSE-a` | A cassette schematic may omit elements present in the plasmid. **Absence of a drawn `WPRE` is not proof of absence in the construct** | 🔴 **The dose contradiction reverts to `NEEDS_ADJUDICATION`.** ⚠️ This is the single weakest inferential step in the dose package and is flagged as such |
| `L-DOSE-b` | "insufficient to rescue lethality" is the authors' summary of a 3-animal arm | The matched-dose comparison loses its anchor |
| `L-DOSE-c` | Terminal survival fractions read off a 726 px CDN rendition could be misread by a few percent | The *direction* survives (LD→0 by ~80 d vs Repudi ~93 % at 270 d); only the precise fractions would move |
| `L-007-a` | Counts from n=3 with a wide range (0–3098/hour) may be driven by one animal | The "strongest electro-behavioural dataset" characterisation weakens; the Title rewrite does not depend on it |
| `L-007-b` | 4 electrodes over 2 regions is not the same as 4 independent channels | Only the methodological contrast is affected |
| `L-007-c` | An input lane is a loading reference, not a quantified western. **"Comparable" by eye is not quantification** | 🔴 The abundance/function dissociation drops from `DATO` to `INFERENZA`. `CLAIM 007` is unaffected — it rests on the *pulldown* lanes, not the input lane |

### Surfaces flagged for special care

| Surface | Entries | Care required |
|---|---|---|
| `pdf_text_dump` | `L-037-a/b/c` | `PMID19500159_Suzuki2009.html` is markup around a PDF text layer. **Use the PDF and the rendered page.** The census marks it `clean` (no C0 controls) — but ~80 % of rule-5d damage is printable, so `clean` is not `verified` |
| Table column alignment | `L-037-b` | Columns are separate text runs. **The crop, not the extraction, is the surface** |
| Figure-only | `L-011-c`, `L-DOSE-a`, `L-007-c` | No text layer exists for these facts. A verdict must come from pixels |
| CDN rendition | `L-DOSE-c1/c2`, `L-011-c` | 726 px, not native. Report `ILLEGIBLE` rather than estimating |

---

## Reviewer's own controls

1. 🔴 **`L-037-a` and `L-011-c` are the two entries where a `NO` verdict would be most costly to
   the work this packet supports.** They are placed here in the open for that reason.
2. **If any artifact named above is absent from your working tree, stop and say so.** `files/` is
   gitignored and does not travel with a branch; the shared checkout carries 175 items, and a
   worktree may carry far fewer. A verdict of "cannot find" is a result, not a failure.
3. **Do not repair a locator you find wrong.** Report it. A locator corrected by its own reviewer
   has not been independently verified.
4. **Where a `pdf_text_dump` is the only surface** (`L-037-a/b/c`), a quote that fails to match
   character-for-character is expected and is **not by itself a finding** — re-check against the
   rendered page before recording a mismatch.
