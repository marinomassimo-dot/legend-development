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
