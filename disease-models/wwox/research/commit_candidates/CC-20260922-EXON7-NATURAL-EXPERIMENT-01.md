# COMMIT CANDIDATE — CC-20260922-EXON7-NATURAL-EXPERIMENT-01

**Source:** Orchestrator, working the exon-7 question directly after two delegate launches died
on server 529s without writing anything (LOST, not PARTIAL — no partial conclusions to distrust).
**Change class:** **MINOR**, and it is a **closing negative** rather than an opening. It withdraws
therapeutic interest this session itself created eight commits ago, and corrects a provenance error
in the candidate that created it.
**Target:** `discovery_ledger_current.md` (`DL-MECH-045` neighbourhood) · corrects
`CC-20260922-SPLICE-ARM-01` §1.
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R2.**
**Proposes:** `D-30` — *"in-frame is a statement about the reading frame, not about the fold."*

---

## 1 · 🔴 First, a provenance error in my own candidate, corrected before it travelled

`CC-20260922-SPLICE-ARM-01` §1 states:

> *"The acceptor of exon 7 is `c.606-1G>A` — **a five-patient homozygous allele**, already in this
> repository: `paper_registry_current.md:6398`, *"caso 2: splice acceptor omozigote c.606-1G>A
> (introne 6…)"*…"*

**The count is right, the quote is right, and they come from different papers.**

| | | |
|---|---|---|
| **PMID 26345274** — Tabarki 2015, *Am J Med Genet A* | **five patients, two consanguineous families**, all homozygous `NM_016373.3:c.606-1G>A` | the source of the *count* (`acquisition_packet_20260920.md` § A8) |
| **PMID 30361190** — *Epileptic Disord* 2018 | **one patient** — case 2 of two unrelated children | the source of the *quote*, at line 6398 |

I attached a count from one paper to a quotation from another — **the exact defect class this
session has corrected in two delegates and in itself twice already**, committed while writing the
correction of someone else's version of it.

🔵 **The corrected statement is stronger, not weaker: there are at least SIX published
`c.606-1G>A` homozygotes across two independent papers** — and, crucially, the second one carries
usable phenotype detail. **Proposed:** `CC-20260922-SPLICE-ARM-01` §1 is amended accordingly.

---

## 2 · What an in-frame exon-7 skip actually removes — arithmetic, and it matters

Exon 7 = `c.606–791` (186 nt, `mod 3 = 0`), boundaries directly observed in ClinVar.
Codon positions computed as `n = (c+2)//3`, `base = c − 3(n−1)`:

| position | codon | base within codon |
|---|---:|---:|
| `c.606` | **202** | 3rd |
| `c.791` | **264** | 2nd |

So the skip fuses `c.605` (codon 202, base 2) to `c.792` (codon 264, base 3), creating a **hybrid
codon** at position 202 and deleting residues **203–263** outright. Net **62 codons**, giving a
**352-aa** product from 414. ✅ Independently reproduces the 352 aa figure.

**Now the part that decides everything:**

| landmark | residue | fate |
|---|---:|---|
| **Q230** | 230 | 🔴 **DELETED** |
| catalytic triad **S281 / Y293 / K297** | 281, 293, 297 | ✅ **spared** |
| GSK3β-binding region **388–407, incl. L404** | 388–407 | ✅ **spared** |

Domain boundaries are not assumed: they are read from the body of PMID 22193544 / `PMC3354054`,
retrieved in full by me this session — *"various WWOX functional domains, ww1 (1–60 a.a.), ww2
(40–110 a.a.), ww (1–110 a.a.) and **ADH (110–414 a.a.)**"* — and *"WWOX amino acids **388–407** are
required for its interaction with GSK3β."* The triad is the repository's own (`H-006`).

### 2a · 🔴 In-frame, sparing both functional landmarks — and almost certainly dead anyway

The deletion removes **62 residues from the middle of a ~305-residue SDR/ADH domain**, roughly a
fifth of it. The SDR fold is a Rossmann-type β-α-β sandwich in which the catalytic residues are
**positioned by** the surrounding scaffold. Excising residues 203–263 from its interior does not
produce a shortened enzyme; it produces a domain that cannot fold.

🎯 **The triad being "spared" is a statement about the primary sequence and nothing more.**
S281, Y293 and K297 would be *present* and could not be *positioned*. `Q230`'s own recorded context
makes the point concretely: relSASA **0.000**, on an α-helix, **22 heavy contacts within 5 Å**,
8.2 Å from the triad (`DL-MECH-037`). A residue that buried is structural, and 61 of its neighbours
go with it.

**So the in-frame prediction, which looked like the most favourable outcome any allele in this
model has carried, is an artefact of reading frame rather than a hypomorph.** `D-30`.

---

## 3 · 🎯 The natural experiment, and it agrees

**If `c.606-1G>A` produced a working hypomorph, its homozygotes should be milder than null/null
patients.** Six are published. What the repository already holds:

**PMID 30361190, case 2** — `paper_registry_current.md`, verbatim:
> *"caso 2 — fenobarbital → miglioramento; **vigabatrin → risposta parziale**; **a 11 mesi spasmi
> in cluster nonostante 4 antiepilettici**."*

Infantile spasms in clusters at 11 months, refractory to four antiepileptics. And that record's own
genotype field classifies **both** its cases — the exon 3–4 deletion **and** the `c.606-1G>A`
homozygote — as **`null biallelici`**, with `clinical relevance: VERY HIGH` and `Transferability:
T1`. **The paper that reported this allele treated it as a null, and its patient behaved like one.**

**PMID 26345274, five patients** — via the A8 entry: periventricular white-matter volume loss,
corpus callosum atrophy, selective mediodorsal thalamic degeneration in one, cerebellum spared.
⚠️ **`abstract-depth` — the body has never been read here**, so this is corroboration, not proof.

**Verdict: the evidence points to severe, typical WOREE — not mild.** By the pre-registered
reading of this experiment, that means **either exon-7 skipping does not occur, or the in-frame
product is non-functional.** §2a says the second is expected on structural grounds, and the two
lines of reasoning are independent.

⚠️ **Bounded honestly.** Phenotype detail is rich for one patient and abstract-depth for five.
Nobody has measured this allele's RNA either, so *"skipping does not occur"* remains untested. What
is excluded is the **therapeutically interesting** version — a well-tolerated internal deletion
retaining function.

---

## 4 · What this costs, and why the negative is worth more than the positive was

Eight commits ago this session wrote that `c.606-1G>A` *"is not a null"* and would be
*"a structurally defined hypomorph… in a different therapeutic class."* **That is withdrawn.**
It survived four hours, and the thing that killed it was available in the repository the whole time.

🔵 **What survives, and is still worth keeping:**
- **Exon 7 is in-frame.** The arithmetic is correct and independently reproduced. What was wrong was
  the inference from frame to function.
- **The three-regime point stands.** WWOX splice alleles are not one uniform PTC/NMD class —
  internal frameshifting (exon 6), internal in-frame (exon 7), terminal-exon (exon 9). An in-frame
  internal exon still needs its own reasoning; it just does not automatically get a favourable one.
- 🔴 **And it sharpens the live question on the reference genotype's own allele.** `c.1057-2A>G`'s
  predicted cryptic-acceptor product is an in-frame **two-codon** deletion (`p.353_354del`) in the
  **last** exon — 2 residues, not 62. **The reason this exon-7 case dies does not transfer**, and
  the contrast is the argument: 62 residues from a domain interior destroys a fold; 2 residues near
  the C-terminus may not. **That prediction is untouched by this negative and its value goes up**,
  because the obvious objection to it has now been tested somewhere else and shown to be
  fold-dependent rather than frame-dependent.

---

## 5 · Provenance

- **Codon arithmetic** computed here, reproducing the 352-aa figure from an independent direction.
- **Domain boundaries and the 388–407 region** are verbatim from PMID 22193544 / `PMC3354054`,
  body retrieved in full by me this session. The triad is the repository's `H-006`.
- **Phenotype quotations** are verbatim from `paper_registry_current.md`; the five-patient
  neuroimaging description is `abstract-depth` from `acquisition_packet_20260920.md` § A8 and is
  labelled as such at every use.
- **Genotype classes kept separate throughout.** `c.606-1G>A/c.606-1G>A` is **not** the reference
  genotype and **not** null/null by sequence — though its own reporting paper files it as a null.
- **`UNREAD_PREMISE`: measured, not predicted** — `growth_anchors.py check` before landing.
- ⛔ **Still owed:** PMID 26345274's body has never been read (`FT-032`, packet `A8`) and would
  convert five abstract-depth patients into five read ones. It is now the **highest-value
  unacquired paper for this allele**, and the natural experiment above is only as good as it.
