# CC-20260922-NMD-PREMISE-WITHDRAWAL-01

**Status:** 🔴 **PROPOSED — NOT PROPAGATED**
**Targets:** `therapeutic_hypotheses_ledger_current.md` (line 216 Premise A) · `discovery_ledger_current.md`
(`DL-BIO-002` causal statement) · the query-hygiene rule set
**Class:** withdrawal of an unsourced premise that closes a therapeutic axis; **no new claim.**
**Produced by:** Scientist P (mechanistic) + Scientist Q (empirical) + Orchestrator (structural, §4)
**Verifier ≠ producer:** every load-bearing number below was re-measured by the Orchestrator against
the committed tree or the primary. §4 was produced **before** P returned and contradicts it.

---

## 1 · The finding

A therapeutic axis — **non-allele-specific WWOX upregulation** — is currently closed in the
hypotheses ledger by this sentence:

> `therapeutic_hypotheses_ledger_current.md:216` — *«L'allele di sito accettore del genotipo di
> riferimento (c.1057-2A>G) produce trascritto aberrante **destinato a NMD**: up-regolarlo spinge
> solo più trascritto verso la degradazione, senza proteina utile.»*

**Premise A («destinato a NMD») is not supported, and Premise B depends on it.**

### 1.1 It does not trace to nothing — it traces to the *wrong branch* of a predictor

- Line 216 (written 2026-07-09) carries **no citation, no locator, no epistemic tag** on the NMD clause.
- Its only upstream node is `DL-BIO-002` (2026-07-04, in-silico VEP/SpliceAI/MaxEntScan), which states
  a **disjunction**: `→ frameshift/PTC → NMD **or** truncated_protein`, tagged `IPOTESI`, belief
  *"medio sull'esito"*, *"Resta in-silico; DATO = RT-PCR wet."*
- 🔴 **Line 216 collapsed a hedged disjunction into a categorical assertion and dropped the tag, the
  hedge and the source.** This is the **same failure class the repository has already refused twice** —
  `Q230P` *"impaired translation **or** premature degradation"*, and `PAPER 044` *"not expressed **or**
  were degraded"*.
- 🔴 **`DL-MECH-045` reversed the premise to NMD-*escape* on 2026-07-10 — one day later. Line 216 was
  never updated.** The two loci that appear to "contradict" it (`paper_registry_current.md:6469`, `:6535`)
  are **downstream restatements of `DL-MECH-045`**, not independent sources. There was one source and
  one reversal, not a three-way disagreement.

### 1.2 The architecture excludes NMD under every producible outcome

Exon 9 is **terminal**; the lesion destroys **its** acceptor. Final EEJ = `c.1056 | c.1057`. A PTC is
NMD-triggering only if it ends at or before **c.1006** (50 nt) / **c.1001** (55 nt); `c.1057` is **51 nt
past even the looser threshold**. Per event, kept separate:

| event | PTC | NMD substrate |
|---|---|---|
| (a) exon 9 skipping | — | ⛔ **N/A — excluded by architecture** (no exon 10, no 3′UTR intron). *Undefined, not "no".* |
| (b) intron 8 retention | yes, ≥265 nt downstream of the last EEJ | 🟢 NO |
| (c) cryptic acceptor `c.1063` | 🎯 **none at all** | 🟢 NO — the question does not arise |
| (d1) upstream cryptic acceptor | excluded within the last 31 nt | 🟢 NO |
| (d2) intronic poly(A) / alt terminal exon | yes, downstream of last EEJ | 🟡 NO for EJC-dependent; **`UNKNOWN`** for long-3′UTR NMD |

**The verdict is architecture-level and survives the frame call:** shifting the acceptor moves the
junction with it; losing it promotes exon 7/8 to last. So `DL-MECH-045` reached the **right NMD verdict
from the wrong molecular event** (it assumed a `+8` frameshift), and its verdict is **upheld while its
mechanism is excluded**.

**Two caveats no prior repo document makes, and both change experiment design:**
1. A **779-kb** retained intron is likely **nuclear-retained and exosome-cleared — not NMD, and
   cycloheximide-insensitive.** A CHX-insensitive transcript loss must **not** be scored as NMD.
2. **Long-3′UTR NMD is the one branch the 50–55 nt rule cannot decide.** It is `UNKNOWN`, not `NO`, and
   needs **UPF1 knockdown, not cycloheximide.**

### 1.3 The empirical floor: `NEVER TESTED`

> 🔴 **No WWOX allele, of any class, in any species, has ever been assayed with an NMD-inhibition
> reagent or by NMD-discriminating transcript quantification.** `PREMISE: NOBODY_LOOKED`.

Re-measured by the Orchestrator against the committed tree (`8d0caf6`), **all exact**: `UPF2` `UPF3B`
`SMG6` `SMG7` `NMDI` `ataluren` `PTC124` `G418` `geneticin` `gentamicin` `readthrough` → **0 each**;
`cycloheximide` → **78**, every WWOX use a **protein-endpoint CHX chase**, never a transcript
measurement; `UPF1` → **22**, one paper, a bladder-cancer co-expression node; word-boundary `ASE` → **0**
(the bare-substring 8,842 is `database`/`phase`/`increase` noise).

**The sharpest single fact:** PMID 32581702 — a homozygous `p.Arg264Ter` fetus autopsied at 21 weeks,
**brain tissue taken, sectioned and stained — and no RNA extracted**; the paper resolves the question in
prose, *"either through protein truncation… **or** nonsense-mediated mRNA decay."* **The material was in
hand and the question was not asked.**

## 2 · 🔴 A FIFTH way a query-count zero is meaningless — and it is the dangerous one

The four known modes are all **query defects**, visible in `query_translation`. This one is an
**indexing-depth defect, and the translation looks perfect.**

Verified by the Orchestrator at the source:

```
WWOX AND cycloheximide  →  total_count: 0
query_translation: ("wwox protein human"[Supplementary Concept] OR "wwox protein human"[All Fields]
  OR "wwox"[All Fields]) AND ("cycloheximid"[All Fields] OR "cycloheximide"[Supplementary Concept]
  OR "cycloheximide"[All Fields] OR "cycloheximide"[MeSH Terms])
```

**Both terms expand flawlessly to MeSH *and* All Fields. The zero is still false.** According to
PubMed, PMID **24550385** (Abu-Odeh et al. 2014, *J Biol Chem* 289(13):8865-80,
[DOI](https://doi.org/10.1074/jbc.M113.506790), PMC3979411) is fully indexed with **WWOX in title,
abstract, MeSH and keywords**, and it ran a cycloheximide chase — as did PMIDs 23370280 and 25331887.

> **(e) A REAGENT named only in Methods or Results is invisible to `[All Fields]`, even when both
> terms expand perfectly. A reagent zero is not evidence of a reagent's absence.**
> In this gene the miss rate is **100%: 0 returned, ≥3 exist.**

**Consequence for §1.3, stated rather than hidden:** the `NEVER TESTED` verdict **does not rest on the
PubMed zeros.** It is carried by the **full-text sweep**, where Methods and supplements are searchable,
and only corroborated by PubMed. The residual — an unindexed NMD arm in the supplement of a full text
this repository does not hold — is **declared open**.

## 3 · What changes, and what does not

**Premise A is withdrawn ⇒ Premise B collapses ⇒ the axis reopens.** As the conditional it is:

> **IF** the `c.1063` cryptic acceptor is used (`DS_AG 0.64` — moderate, **never measured**), **THEN**
> the allele yields a **non-NMD** mRNA encoding a **412-aa** protein (`p.Gln353_Gln354del`), **AND** a
> non-allele-specific boost raises output from **both** alleles, not predominantly `Q230P`.

**What does NOT change:**
- 🟡 The **proteotoxic safety flag stands — and now applies to both alleles, not one.**
- **FLAG FIRST.** No re-score until mechanism + reagent + allele verification, i.e. until `TX-001` runs.
- ⚠️ **An unresolved tension, recorded not resolved:** if the allele already makes a near-full-length
  protein, splice correction recovers **2 residues, not a protein** — which *lowers* `TX-001`'s ceiling
  while *raising* the value of measuring it.
- ❌ **Nothing here is a claim that the protein is made, folded, stable or functional.** See §4.

## 4 · 🔴 The structural premise attached to this node is ALSO wrong — and it was wrong in the repository first

The Orchestrator measured the AlphaFold model directly (`analysis/gln353_gln354del_structural_adjudication_20260922.md`),
**before** Scientist P returned. Method positive control: **Q230 → helical, pLDDT 98.50, burial 201**,
reproducing the repository's independent SASA/SSE record.

| repository / P says | measured | verdict |
|---|---|---|
| *"model confidence lowest exactly there"* · *"pLDDT 60–76"* | **353 = 85.81, 354 = 87.25** (chain Q1 = 82.8) | 🔴 **FALSE.** 60.47/76.38 are residues **350/351** — an **off-by-three** misattribution |
| *"mid-α-helix"* | helix **352–363**; 353/354 at positions **2–3**, the **N-terminal edge**, adjacent to the 348–351 coil | 🔴 **FALSE** |
| *"in-frame and lethal, cf. exon 7"* | exon 7 deletes **62** residues through the SDR interior; this deletes **2** at a helix edge | 🔴 **unsound analogy — a factor of 31** |

The corrected structural reading is **two-sided**: the backbone admits a **low-strain local
accommodation** (span test — only 352→355 is strained, by 1.17 Å, and the adjacent coil has slack), so
the fold is **not required to collapse**; but the deletion removes **both partners of a six-contact
polar staple** to the 110–143 element **including the helix's own N-cap**, and sits **>20 Å from the SDR
catalytic tetrad** — making it a **packing/stability lesion, not an active-site lesion.**

## 5 · Proposed edits (exact, none applied)

1. **`therapeutic_hypotheses_ledger_current.md:216`** — withdraw Premise A; replace with the §3
   conditional; tag `PREDICTED, in-silico`; carry the proteotoxic flag onto **both** alleles.
2. **`discovery_ledger_current.md` `DL-BIO-002`** — the causal statement `→ frameshift/PTC → NMD or
   truncated_protein` has **both branches excluded**; replace with
   `→ cryptic acceptor c.1063 → in-frame p.Gln353_Gln354del → no PTC → no NMD` **(PREDICTED)**.
3. **`DL-MECH-045`** — **verdict upheld, mechanism withdrawn** (the `+8` frameshift is excluded by
   reference sequence).
4. **Query-hygiene rule set** — add mode **(e)** from §2.
5. **Withdraw** *"mid-α-helix, one turn from a buried face, model confidence lowest exactly there"*
   wherever it appears.

## 6 · Why this is NOT propagated here

Items 1–3 are **non-zero scientific deltas on canonical surfaces**, and the current Operator
authorization is scope-limited (*"No unrelated canonical changes are authorized by this approval"*).
Item 5 depends on §4, whose §4.2 contact inventory is the **least reliable part** of a predicted
structure and is the part carrying the most weight.

**One check would settle the architecture half at zero cost: the RefSeq `NM_016373.4` sequence**, which
converts four derived bases to read. Sequence egress **403 at CONNECT** throughout (Ensembl/NCBI/EBI) —
recorded as blocked, **not retried**, and **not** treated as a scientific stop (§27).

## 7 · The experiment, with the four constraints that each otherwise force a false negative

One RT-PCR across the exon 8→9 junction on allele-carrying RNA, **Sanger on every band**:
1. The aberrant product is **6 nt SHORTER, not +8 longer** (`+8` is a genomic offset) — 2.2% of a ~271 nt
   amplicon ⇒ **capillary/GeneScan, denaturing, 6-nt sizing standard; not agarose, not native PAGE.**
2. An **intron-8-anchored reaction + 3′ RACE is mandatory** — a retention species has no exon 9, so its
   absence would be silently misread as support for the cryptic outcome.
3. The **±cycloheximide arm has less power than the `TX-001` packet implies** (no PTC under the surviving
   outcome). Keep it to catch a competing PTC species and to test long-3′UTR NMD — with a vehicle twin
   and an **endogenous NMD-sensitive positive control**.
4. **Do not normalise to the exon 4–6 core** — the short isoform's exon 5–6 junction *rises* when the long
   isoform is lost, so that denominator moves with the lesion.

**And the cheapest experiment for the empirical floor** (§1.3): allele-specific ±NMD-block in a
**heterozygous carrier LCL**, not the proband — the carrier supplies the internal control every existing
WWOX measurement lacks, so *degraded* and *never transcribed* stop being the same observation.
**Standing material ask:** when WWOX post-mortem or termination material is next handled, **snap-freeze a
fragment before fixation.** One tube. PMID 32581702 is why.

---

## WAVE-2 READINESS (2026-09-27)

**Actor:** ACTOR_ID `scientist`, wave-2 package `splice_sdr` ·
**Verdict: `READY_MAJOR`.** It withdraws a premise that closes a therapeutic axis and reopens that axis
as a labelled conditional; that is a reversal of a stated position on a therapeutic surface, so it goes
to the batch with locator triples rather than being applied here.
**`context_policy` declared: `SYNTHESIS`** for the repository half (the ledgers and the structure file
are its intended inputs, reached by `registry_records.py` and by direct measurement), and
`QUESTION_DRIVEN` for the one source reopened under this package (`PMID 30362252`, for the NMD-attribution
question shared with `CC-20260922-SPLICE-ARM-01`).

### 1 · The structural contradiction is ADJUDICATED, from the files, and §4 wins

`CC-20260922-SPLICE-ARM-01` §9c and this candidate's §4 disagreed about the same residues. Measured
directly on `analysis/data/WWOX_Q9NZC7_AlphaFold.pdb` in this session (CA pLDDT per residue; helix
extent from CA(i, i+4) distances, the same geometric criterion the repository's P-SEA annotation
approximates):

| quantity | value measured here | verdict |
|---|---|---|
| pLDDT 353 / 354 | **85.81 / 87.25** | §4 is right; §9c's *"pLDDT 60.5 at 350 and 76.4 at 351"* are **real numbers about 350/351**, misframed as being *at the deletion* — an off-by-three |
| pLDDT 350 / 351 | 60.47 / 76.38 | the two values §9c quoted |
| helical CA(i, i+4) contacts | continuous from **350** through **361** | the helix starts at **350–352**, so 353/354 sit at positions **~3–5 of a ~12-residue helix**: **near the N-terminal edge, not mid-helix**. §9c's *"inside an α-helix (351–363)"* is the weaker description; §4's *"N-terminal edge"* is the better one |
| 340–349 | pLDDT 35–53 | the disordered run immediately upstream is real, and it is what makes local accommodation arguable |

⇒ **§5 item 5 of this candidate is upheld:** *"mid-α-helix, one turn from a buried face, model
confidence lowest exactly there"* must be withdrawn wherever it appears. 🔴 **And the correction is
symmetric, which is the part that must not be lost:** higher pLDDT at 353/354 does **not** make the
deletion benign — it makes the *confidence argument* unavailable in **both** directions. The two-sided
reading of §4 (low-strain accommodation possible; a six-contact polar staple and the helix N-cap lost)
stands, and the verdict remains **nobody can tell without the wet experiment**.

### 2 · What else was done under this package

- **The architecture half needs no new reading.** Exon 9 terminal ⇒ final EEJ `c.1056 | c.1057` ⇒ no
  producible outcome is an EJC-dependent NMD substrate. Re-derived here; unchanged.
- **The empirical floor (§1.3) is corroborated by a first-hand read, not only by a query census.**
  `PMID 30362252` was read in full (PMC JATS, `FTR-20260927-30362252-02`, receipt prepared and **not**
  recorded): `cycloheximide`, `puromycin`, `emetine`, `UPF1` occur **zero** times, and the PMC body has
  **no Methods section** — so *"NEVER TESTED"* survives its most obvious counter-candidate, the one
  paper in the corpus that asserts NMD for a WWOX allele. 🔴 **And the assertion it makes is a figure
  legend's inference from junction qPCR**, which is now locatored under
  `CC-20260922-SPLICE-ARM-01`. **That strengthens §1.3 materially:** the field's only NMD assertion for
  any WWOX allele rests on a junction ratio with no translation block.
- **The RefSeq check named in §6 is still blocked** — sequence egress to Ensembl/NCBI/EBI for raw
  sequence was not available; it is recorded as blocked, not retried, and it is **not** load-bearing:
  `c.1061 = A` is established twice from ClinVar's protein-consequence column.

### 3 · Exact operation list for the batch executor

#### OP 1 — `disease-models/wwox/research/therapeutic_hypotheses_ledger_current.md` · Premise A
**Op:** `replace-within` (the ledger is append-only on *leads*; this is a **premise correction inside an
Evidenza CONTRO bullet**, and the withdrawn wording is preserved in the replacement rather than deleted).

**old text (verbatim from the current file):**

```text
L'allele di sito accettore del genotipo di riferimento (c.1057-2A>G) produce trascritto aberrante destinato a NMD: **up-regolarlo spinge solo più trascritto verso la degradazione**, senza proteina utile.
```

**new text:**

```text
⚠️ **Premessa A RITIRATA il 2026-09-27 (wave-2 `splice_sdr`).** Il testo precedente diceva: *"L'allele di sito accettore del genotipo di riferimento (c.1057-2A>G) produce trascritto aberrante destinato a NMD: up-regolarlo spinge solo più trascritto verso la degradazione, senza proteina utile."* 🔴 **Non è sostenuto**: nessuna fonte, nessun locator, nessun tag lo accompagnava, e il suo unico nodo a monte (`DL-BIO-002`) affermava una **disgiunzione** in-silico *"NMD **o** proteina tronca"*, rovesciata a NMD-**escape** da `DL-MECH-045` il giorno dopo. **L'architettura esclude l'NMD sotto ogni esito producibile**: l'esone 9 è terminale, l'ultima giunzione esone-esone è `c.1056 | c.1057`, e ogni PTC producibile cade a valle di essa. **Condizionale che sostituisce la premessa (PREDETTO, in-silico, mai misurato):** *SE* è usato l'accettore criptico `c.1063` (`DS_AG 0.64`, moderato), *ALLORA* l'allele produce un mRNA **non-NMD** che codifica una proteina di **412 aa** (`p.Gln353_Gln354del`), **E** un boost non-allele-specifico aumenta l'output di **entrambi** gli alleli, non prevalentemente del missenso. 🟡 **La bandiera proteotossica resta e ora si applica a entrambi gli alleli, non a uno**; `FLAG FIRST`, nessun re-score finché non girano meccanismo + reagente + verifica d'allele (`TX-001`). ⚠️ Due rami non decisi dalla regola 50–55 nt: la ritenzione di un introne di **779 kb** è probabilmente nucleo-ritenuta e degradata dall'esosoma — **non NMD, e insensibile alla cicloesimide** — e l'**NMD da 3'UTR lungo** è `UNKNOWN`, non `NO`, e richiede knockdown di UPF1, non cicloesimide.
```

#### OP 2 — `disease-models/wwox/research/discovery_ledger_current.md` · `DL-BIO-002` and `DL-MECH-045`
**Already drafted, and deliberately NOT duplicated here.** Items 2 and 3 of §5 are carried verbatim by
`CC-20260922-SPLICE-ARM-01`'s `WAVE-2 READINESS` **OP 2 and OP 3** (append-only blocks on both records),
so that the two candidates cannot write two different sentences into the same ledger record. **If the
batch takes this candidate and not that one, OP 2/OP 3 of that section must be taken with it.**

#### OP 3 — query-hygiene rule set: mode (e)
**Op:** `append` one row to `disease-models/wwox/research/dismissal_ledger_current.md` under
`🩸 DEFAULTS THAT BIT US`. **D-number not allocated here**: `D-17` is reserved (operator-deferred), the
ledger ends at `D-16`, and several candidates in this lot propose rows — the batch allocates the numbers
in one pass. Row text: *"a reagent named only in Methods or Results is invisible to `[All Fields]`,
even when both terms expand perfectly to MeSH — in this gene the miss rate is 100%: 0 returned, ≥3
exist (`PMID 24550385`, `23370280`, `25331887`). A reagent zero is not evidence of a reagent's
absence."* **Detection rule:** a query-count zero on a *reagent* is not reportable without a
Methods-reaching surface.

### 4 · LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. The field's only NMD assertion for a WWOX allele is an inference from junction qPCR, printed in a figure legend | *"indicating that the deletion causes nonsense mediated decay of the two longer transcripts"* | `files/fulltext/PMID30362252_Davids2019_PMC_2026-09-27.xml` — Figure 2 legend, panel B
2. The same paper's running text does not resolve degradation against non-expression | *"suggesting that the two longer transcripts were not expressed or were degraded"* | same artifact — Results, expression-analysis paragraph
3. Residues 353 and 354 are not where the AlphaFold model is least confident | pLDDT `353 = 85.81`, `354 = 87.25` against `350 = 60.47`, `351 = 76.38` (CA B-factor column, chain A) | `disease-models/wwox/analysis/data/WWOX_Q9NZC7_AlphaFold.pdb` — ATOM records, CA of residues 350–354
4. The helix that carries them begins at 350–352, so they sit near its N-terminal edge | CA(i, i+4) distances: `349 → 11.48 Å` (non-helical), `350 → 5.72 Å`, `351 → 6.32 Å`, `352 → 6.29 Å`, continuous helical spacing to `361 → 5.59 Å` | same file — CA coordinates, residues 344–365

### 5 · What is still pending

- §4.2's **contact inventory** (the six-contact polar staple and the N-cap) is the least reliable part of
  a predicted structure and was **not** re-measured here; it is the one statement in §4 this section does
  not underwrite. Item 5's withdrawal does not depend on it.
- The **cheapest experiment named in §1.3** (allele-specific ±NMD-block in a heterozygous carrier LCL)
  is a material ask, not a repository act, and is unchanged.

## BATCH DISPOSITION — `BATCH_20260927_004` (2026-09-27, ACTOR_ID `scientist`), append-only

**Verdict: `PROPAGATED`.** `OP 1` applied: the therapeutic-hypotheses ledger's **Premise A is withdrawn in place**, with the withdrawn wording preserved inside the replacement rather than deleted, and replaced by a labelled conditional. `OP 2` was carried by `CC-20260922-SPLICE-ARM-01`'s ledger blocks, exactly as this candidate instructed, so the two cannot write two different sentences into one record. `OP 3` landed as **`D-25`**. **The structural contradiction is propagated as §4 resolved it, and symmetrically:** pLDDT 353/354 = 85.81/87.25, the 60.47/76.38 values belong to **350/351**, and the helix runs 350–361, so the residues sit near its N-terminal edge. 🔴 **The higher confidence does not make the deletion benign — it makes the confidence argument unavailable in BOTH directions**, and that is written into the ledger and into `TX-001`'s ceiling note. **No re-score, and the proteotoxic flag now applies to both alleles rather than one** — which is a widening of a caution, not a narrowing. §4.2's contact inventory is **not** underwritten by this batch either, as §5 asks.

**Operator authorisation, verbatim (2026-09-27, given in writing after being shown the MAJOR proposals):** *«procedi tu, ti autorizzo su tutto»*. **Mirror ex-post review due** under §21e — see `session_evaluations/2026-09-27_BATCH_20260927_004.md`.
