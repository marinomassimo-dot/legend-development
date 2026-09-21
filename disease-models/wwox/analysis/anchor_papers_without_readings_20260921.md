# Seven "anchor" papers stand integrated on no recorded reading — and both ratchets are blind to them

**Date:** 2026-09-21 · **Actor:** Orchestrator · **Status:** non-canonical analysis file.
**No canonical file edited.** Not medical advice.

> **How this was found.** Not by auditing the registry. It was found while chasing a *scientific*
> question — whether `CLAIM 032`'s sub-50 % therapeutic threshold has a source — and the answer
> generalised. The same afternoon produced three independent instances of one structural pattern,
> and the third is the general case.

---

## 0 · The three instances, in the order they appeared

| # | Instance | What was invisible, and to what |
|---|---|---|
| 1 | **`CLAIM 032`'s hypomorph sentence** | A therapeutic threshold below 50 % resting on `PMID 17823927`, a paper **absent from the claim's `Source` line**. The `UNREAD_PREMISE` ratchet read `0` throughout — correctly, because it scans reasoning-layer files for **PMIDs**, and this premise was *used without being named*. |
| 2 | **`CORPUS P306` / `PMID 21476439`** | The only published measurement of WWOX catalysis, tiered `C` / `background only`. `unread_gold.py` missed it on **both** paths: its selector regexes matched **zero** records in the live registry, and its mechanism lens had **no vocabulary for catalysis**. |
| 3 | **This file** | Seven `Status: integrated` `PAPER` records with **no receipt and no `full text reviewed` declaration** — five of them carrying the word **"anchor"** in their `Role` field. |

**The pattern, stated once.** Every check LEGEND owns verifies a *declaration*. The registry-only
ratchet counts records that **declare** `full text reviewed` without a receipt — so a record that
declares **nothing** is invisible. The unread-premise ratchet counts **named** PMIDs in
reasoning-layer files — so a premise carried by wikilink, by a model name, or by a record with no
identifier at all is invisible. 🔴 **Both instruments measure honesty, not coverage. A record that
says nothing passes both.**

---

## 1 · The measurement

Over `paper_registry_current.md`: **87 `PAPER` records**, of which those with `Status: integrated`
were cross-joined against `fulltext_read_receipts.jsonl` (keyed on `study_id.pmid`) and against
the string `full text reviewed`.

> **Seven integrated `PAPER` records have neither.**

| Record | Identity as the registry declares it | `clinical relevance` | `Role` |
|---|---|---|---|
| **`PAPER 001`** | Steinberg 2024 organoids · **`Identifier: preprint`** · bioRxiv | **HIGH** | **core baseline paper** |
| **`PAPER 002`** | Baryła 2022 · DOI `10.1007/s00109-022-02265-5` · *J Mol Med* | MODERATE | metabolic/redox framework paper |
| **`PAPER 003`** | Choi 2026 VABAM · **`PMID 41442931`** · *Pediatric Neurology* | **HIGH** | **safety anchor paper** |
| **`PAPER 004`** | Repudi 2021 · `PMID 33914858` · *Brain* | MODERATE | **myelination anchor paper** |
| **`PAPER 007`** | Hussain 2023 P47T · **`Identifier: pending normalization`** | LOW | **genotype caution anchor** |
| **`PAPER 008`** | Aldaz/Banne cluster · **`Identifier: multiple / pending normalization`** | MODERATE | **nosology anchor** |
| **`PAPER 026`** | Shkedi 2020 · `PMID 32185845` · *ChemBioChem* | LOW direct / HIGH | **mechanistic anchor paper** |

🔴 **Four of the seven declare no resolvable identifier at all** (`001`, `002` by DOI only,
`007`, `008`). A record without an identifier cannot be checked by *anything* — not by the
receipt ledger, not by the identity index, not by a census. Its "no receipt" status is therefore
**not a finding about the paper**; it is the absence of a question.

---

## 2 · The three that are genuinely actionable, separated from the three that are bookkeeping

### 2a · 🔴 `PAPER 003` — a **safety** anchor, unread and unreadable

`CLAIM 001` (*"Vigabatrin associated with VABAM in WWOX-DEE"*, `Status: conflicting evidence`,
`clinical relevance: HIGH`) is a **`BLOCCO 1` safety position**. Its safety anchor is
**`PMID 41442931`**, and:

- `fulltext_receipts.py status --pmid 41442931` → **`[]`**;
- `convert_article_ids(["41442931"])` returns **the PMID alone — no PMCID**;
- `get_copyright_status` → `"Published by Elsevier Inc."`, `found_in_pmc: 0`.

**Verified unobtainable by any automated route here.** ⇒ acquisition item.

**What the abstract does and does not support** (verbatim, PubMed metadata, tokens checked):

> *"We report vigabatrin-associated brain abnormalities on magnetic resonance imaging (VABAM) in
> **two children** affected by WWOX-related epileptic encephalopathy."*

> *"Brain magnetic resonance imaging during vigabatrin treatment revealed **new symmetrical signal
> changes in the globus pallidi and thalami** consistent with VABAM."*

✅ `CLAIM 001`'s core assertion **is** supported at abstract level. The claim does not overstate it.

⚠️ **But two things the abstract carries are not in the claim, and one of them is a confound:**

1. > *"Initial neuroimaging was characterized by **periventricular white matter volume loss and
   > atrophy of the corpus callosum**."*
   The brains were **already abnormal before vigabatrin**. A drug-attribution claim in a disease
   with progressive white-matter pathology needs that baseline stated, and `CLAIM 001` does not
   state it.
2. 🔴 The authors' own closing sentence is **a question, not a finding**:
   > *"**Further research is warranted to investigate whether** children with genetic epilepsy
   > related to the GABAergic pathway or delayed myelination are **more susceptible** to VABAM."*
   This is the `INTERROGATIVE-TO-DECLARATIVE` re-voicing hazard recorded on `PMID 25238782`,
   sitting in a **safety** claim. **Checked: LEGEND does not currently re-voice it** — the working
   model says *"a real safety signal"* and *"conflicting"*, never *"WWOX children are more
   susceptible"*. The claim is clean today. It is recorded here because the sentence is exactly
   the shape that gets firmed up on the next pass.

**Date discrepancy, flagged not resolved (§12).** The registry says `Year: 2026`; PubMed's
`publication_date` is **2025-12-06**, and the DOI is `10.1016/j.pediatrneurol.2025.12.001`, i.e.
`Pediatr Neurol` **175**:230–233. One is the online-first date and the other is plausibly the
issue year. **Not asserted as an error** — recorded so that any cohort-overlap or chronology
argument using this paper checks which date it means.

### 2b · 🔴 `PAPER 001` — the **core baseline paper** is filed as a preprint that has since been published

The registry holds it as `Steinberg 2024 organoids`, `Journal/source: bioRxiv`,
`Identifier: **preprint**`. The peer-reviewed version exists:

> **PMID 42397075** — Steinberg DJ, Zonca A, Abdellatif D, Rosh I, Kustanovich I, Hidmi O,
> Manenti C, Maroun K, Stern S, Davila-Velderrain J, **Aqeilan RI**. *"Disrupted WWOX-MYC interplay
> impairs neurogenesis in human brain organoids."* **Brain** 2026.
> DOI [10.1093/brain/awag239](https://doi.org/10.1093/brain/awag239)

⚠️ Note LEGEND **does** hold `42397075` elsewhere — a deep-dive manifest exists for it and
`PAPER 094` references it. So this is **not** an unread paper; it is a **split identity**: the
*core baseline* record points at the preprint while the reading sits under a different record.
Anyone reasoning from `PAPER 001` is reasoning from a bioRxiv version whose relationship to the
published text nobody in this repository has checked line by line.

🔴 **And the published abstract carries a genotype-class statement that the portfolio's window
argument does not:**

> *"**Patient-derived organoids exhibited milder phenotypes compared to knockout organoids**,
> showing functional neuronal impairments like hyperexcitability and delayed differentiation
> **rather than RG dysfunction**."*

> *"Remarkably, **gene therapy restored neuronal function, normalizing hyperexcitability and
> promoting maturation, without disturbing RG populations**."*

`TX-007` currently carries a general caveat that neuronal gene therapy *"does NOT repair the
progenitor defect (radial glia/neurogenesis), largely prenatal/early-postnatal"*. If the
radial-glia defect is **a property of complete knockout and not of patient-derived (residual
protein) lines**, that caveat is **genotype-class-specific**, not general — and it would run in the
**favourable** direction for every genotype with residual protein. 🔴 **FLAGGED, NOT SCORED.**
This is an abstract sentence about a comparison whose statistics, n, line provenance and
differentiation protocol are all in a body this environment has not verified for the published
version. Under the operator's verification rule it may not move `TX-007` until read. **It is,
however, the single most consequential unverified sentence now visible to this repository.**

### 2c · `PAPER 004` — known, already packet item `A4`

`PMID 33914858` (Repudi 2021, *Brain*), primary of `CLAIM 003` (`consolidated baseline`), no PMCID,
PDF surface `SUSPECT`, no PDF tooling. **Nothing new; re-counted here for completeness.**

### 2d · The three that are bookkeeping, and should be said to be

- **`PAPER 007`** is almost certainly **`PMID 36828035`** (Hussain, Aldaz et al., *Prog Neurobiol*
  2023, *"WWOX P47T partial loss-of-function mutation induces epilepsy, progressive
  neuroinflammation, and cerebellar degeneration in mice phenocopying human SCAR12"*), which
  **LEGEND HAS READ** — receipt `FTR-20260826-36828035-01`. ⇒ Its place on this list is an artefact
  of `Identifier: pending normalization`. **Normalising the identifier closes it; no reading is
  owed.** ⚠️ Stated as *almost certainly* rather than asserted: the identity is inferred from
  title, author, year and phenotype, not copied from a source that declares it.
- **`PAPER 008`** is a **cluster of reviews**, not a paper (`Identifier: multiple / pending
  normalization`). A cluster cannot carry a receipt. It should be split or marked
  `NOT_AN_ARTICLE`.
- **`PAPER 002`** carries a DOI but no PMID, which is why the PMID-keyed ledger cannot see it.

---

## 3 · What follows — and what deliberately does not

**Actionable (three items, none of them a new gate):**

1. `PMID 41442931` → acquisition packet, **priority ABOVE the method papers**, because it is the
   only unread **safety** anchor in the repository. Ask for: the two patients' **pre-vigabatrin**
   MRI description, the **dose and duration** of vigabatrin, and whether any **de-challenge /
   re-challenge or follow-up MRI** exists.
2. `PAPER 001` → reconcile its identity with `PMID 42397075` and decide which record is canonical.
   Until then, **no sentence may be attributed to "Steinberg 2024" without saying which version.**
3. `PAPER 007` and `PAPER 008` → identifier normalisation. Bookkeeping, but it is the bookkeeping
   that makes every other check possible.

**Refused (§26 — a scientific defect is repaired by correcting the science and reusing existing
mechanism):**

- ❌ **No third ratchet.** Two exist; the gap is not that a third is missing, it is that both
  measure declarations. Adding a third declaration-counter would inherit the same blindness.
- ❌ **No new gate, auditor, registry or mandatory workflow.**
- ❌ **No claim is touched by this file.**

**The operational rule that covers all three instances, and costs nothing:**

> 🔵 **When a record or a claim names a paper, a model, an animal or an allele that its own
> identity/`Source` line does not account for, that is an unsourced premise — regardless of what
> any ratchet reports.** The ratchets cannot see it, by construction, and a reader can, in one
> glance. This is a reading habit, not a check.

---

*Sources retrieved from **PubMed / PubMed Central**.
DOIs — [41442931](https://doi.org/10.1016/j.pediatrneurol.2025.12.001) ·
[42397075](https://doi.org/10.1093/brain/awag239) ·
[36828035](https://doi.org/10.1016/j.pneurobio.2023.102425).
`PMID 17823927` → [10.1002/gcc.20497](https://doi.org/10.1002/gcc.20497). `PMID 21476439` carries
no DOI in its PubMed record and none is invented here.
**No reading occurred and no receipt is claimed.** An abstract is not a reading. Not medical advice.*
