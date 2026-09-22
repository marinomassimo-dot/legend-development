# `Q230P` — structural, evolutionary and biochemical mechanism adjudication

**Actor:** Scientist B · **Date:** 2026-09-22 · **Reports to:** Orchestrator
**Status:** 🔴 **NON-CANONICAL.** This file touches no registry, no queue, no ledger, no receipt chain,
no state manifest, and no `*_current.md`. No `BATCH_COMMIT`. No git operation was run. It proposes;
the Orchestrator verifies and lands.
**Nothing here is medical advice.** No molecule, dose, route, prognosis or safety claim is recommended
anywhere below, and no therapeutic recommendation follows from any of it.
**Genotype classes are held apart throughout.** `Q230P` ≠ `P47T` ≠ `P252A` ≠ `P282A` ≠ `G372R` ≠
`A141T` ≠ `L239R`. A measurement on one is never carried to another.
**This is the public edition and reasons about a WWOX-DEE reference genotype class, not an individual.**

---

## VERDICT UP FRONT

> ## 🟡 **A COMBINATION, and it is a specific and lopsided one.**
>
> **`Gln230` is a buried, interior, mid-helix packing residue of SDR helix αE whose side chain is one
> arm of a five-contact polar node that staples αE to strand βC across ~45 residues of sequence. The
> proline substitution is not a marginal change at that site: the modelled Pro Cδ occupies the exact
> position of the helical amide hydrogen and comes to 1.60 Å of the Glu226 carbonyl oxygen — a 1.44 Å
> hard overlap — so the local backbone cannot stay as modelled. Both available accommodations are
> expensive, because the nearest coil is four residues too far upstream and every residue downstream
> is core.**
>
> **On the seven listed possibilities the answer is: YES to core packing, YES to a conserved-position
> hydrogen-bond network (with the Gln's own identity NOT the conserved element), YES to
> secondary-structure stabilisation, NO to cofactor environment, NO to substrate-binding region, NO
> to a solvent-exposed interaction surface, and — the result with the therapeutic stakes —
> 🟢 **NO to the oligomer/dimer interface, for a reason that does not depend on knowing where the
> interface is**: `Gln230` has **relSASA 0.000 / SASA 0.0 Å²** in the monomer model, and a residue
> already fully occluded by its own chain cannot be buried further by a partner subunit.**
>
> 🔴 **And one premise underneath the whole question did not survive checking.** A fully-expanded
> PubMed query for WWOX dimerisation returns **one** record, and it is about p-WWOX/p-p53
> **hetero**-dimers, not a WWOX homodimer. **I could not find a published source establishing that
> WWOX homodimerises through its SDR domain at all.** The repository's premise is
> `PREMISE: UNVERIFIED`, not established.
>
> 🔴 **What this verdict is NOT.** It is not a statement that the protein is destabilised, degraded,
> cleared, insoluble, aggregated, or functional. **Every number below is a prediction computed on a
> predicted monomer structure.** `Q230P` has never had stability, solubility, aggregation propensity
> or turnover measured — `PREMISE: NOBODY_LOOKED` — and this file does not change that by one datum.
>
> ⭐ **And the stakes are the highest in the gene.** `Q230P` is the **most recurrent WWOX allele of
> any class — 8 patients across 6 families** (§0.3), so this mechanism verdict carries more patients
> than any verdict about any other WWOX variant. 🔴 **Yet both of its experimental data — "transcript
> normal" and "protein not detected" — are `abstract-depth`: PMID 29808465 is
> `unrecoverable_by_these_routes`, `pmc_id: null`, and nobody here has read its body** (§0.4). The
> largest constituency in the disease rests on one unread abstract.

**Therapeutic sign (§9):** 🟡 **the boost axis reads NOT-DANGEROUS-ON-THIS-EVIDENCE but still
UNDETERMINED.** The specific aggregation trigger the fold family supplies — substitution *at* an SDR
dimer interface — is **not** the class `Q230P` belongs to. That removes the identified red flag; it
does not license the boost, because no WWOX solubility measurement exists in either direction.
`IPOTESI`.

---

## 0 · Four bounds imported before I start — and the cap that applies to every line below

These come from [`missense_splice_reclassification_risk_20260921.md`](missense_splice_reclassification_risk_20260921.md)
— **another actor's work on another branch, imported at commit `b30dfbf`, cited here as that actor's
attestation and not as my reading.** They arrived after §§1–12 were computed; none of them changes a
measurement, two of them narrow the mechanism space, one raises the stakes, and one **caps what may
be asserted anywhere in this file.**

### 0.1 🟢 The splice confound is excluded — and that is all it does

`Q230P` is **`c.689A>C` in exon 7**, **66–84 nt from any junction** (acceptor 84; donor 66–155). That
actor's codon arithmetic was validated against **nine independent published c./p. pairs before being
relied on**, and `c.689`/p.230 is one of the nine that passed. The allele's splice risk is rated
**LOW**, *"deep exonic on both sides of the undetermined boundary."*

> ✅ **Consequence for this file: the substitution acts on protein, not on splicing, so no
> cryptic-splice confound competes with the structural reading in §§2–5.**
>
> 🔴 **And that is strictly a confound removal, not evidence.** *"Not a splice allele"* says nothing
> about folding, packing, stability, solubility or turnover, and it is used nowhere below as if it
> did. A variant can be purely protein-acting and still be perfectly tolerated.

### 0.2 🟢 Transcript level is reported NORMAL — so the lesion is post-transcriptional

qRT-PCR in donor-derived fibroblasts reports **normal WWOX transcript levels** for `Q230P`. This
corroborates the Johannsen picture from a second direction and places the lesion **downstream of
transcription**. ⚠️ **It is not a splice assessment** — the amplicon position is unstated, so an
NMD-escaping aberrant isoform would be counted as message.

> **Combined with §8.1: normal message + protein not detected leaves exactly three candidate causes —
> reduced translation, accelerated turnover, and insolubility. The authors named the first two and
> tested neither. The third is un-named, and nobody has looked in the pellet.** `PREMISE: NOBODY_LOOKED`.

### 0.3 ⭐ `Q230P` is the most recurrent WWOX allele of any class — 8 patients across 6 families

That actor's finding, in its own words: *"the therapeutically decisive allele is the safest one"* —
the largest single allele-specific constituency in the disease is also the one least exposed to the
splice threat.

> **This is a fact about clinical weight, not about mechanism, and it does not move any verdict
> below by one step.** It changes only the consequence of being wrong: **whatever this file concludes
> about `Q230P`'s mechanism carries more patients than any conclusion about any other WWOX variant.**
> That is a reason for the confidence statements in §8.1 to be read strictly as written, not a reason
> to strengthen any of them.

### 0.4 🔴 THE CAP — every `Q230P` protein-level statement available to anyone here is ABSTRACT-LEVEL

**PMID 29808465 (Johannsen 2018), the only `Q230P` functional paper in existence, is recorded in
`full_text_queue_current.md` as `unrecoverable_by_these_routes`, `pmc_id: null`, closed at Springer.**

> 🔴 **Nobody in this repository has read its body.** The `n`, the controls, the densitometry and the
> loading behind that Western **have never been read by anyone here**, and neither has the qRT-PCR
> amplicon position.
>
> **Therefore: both of `Q230P`'s protein- and RNA-level data — "protein not detected" and "transcript
> normal" — are `abstract-depth` / `PREMISE: UNREAD_PRIMARY`, and are labelled as such on every line
> of this file that touches them.** Where an earlier draft of §8.1 or §9 read as though the Western
> were a read datum, this cap governs.

### 0.5 Calibration — the emptiness is the field's, not this allele's

Of the **19 distinct WWOX missense alleles** the repository can enumerate, **exactly one has ever had
RNA examined**. Against Piard's own denominator of *"11 aa changes in 12 families"*: **1 of 11 with
experimental evidence, 10 of 11 without — 90.9% none**, by two independent routes (89.5% and 90.9%,
one of them the source's own count).

> **So `Q230P` is not an unusually neglected allele. It is a normally neglected allele in a gene where
> neglect is the norm — and it is simultaneously the most recurrent one.** That combination is the
> reason this node exists.

---

## 1 · Measurements I made myself, with method and positive control

### 1.1 Input and tooling

| item | value |
|---|---|
| Structure | `disease-models/wwox/analysis/data/WWOX_Q9NZC7_AlphaFold.pdb` — AlphaFold Monomer v2.0, Q9NZC7, **414 residues**, B-factor column = pLDDT |
| Geometry engine | direct **numpy** on atom coordinates (no DSSP, no biopython in this deployment) |
| SASA engine | the repository's own `disease-models/wwox/analysis/scripts/residue_context.py` — sampled Shrake–Rupley, relSASA against a per-residue max-ASA table, P-SEA-like SSE |
| Sequence identity | extracted from the coordinates and confirmed independently: residue **230 is GLN**; flanks `…L225 E226 T227 T228 F229 **Q230** V231 N232 H233 L234…` |
| MD | 🔴 **ROUTE BLOCKED, RECORDED ONCE, NOT RETRIED.** `md_status.py` → *"MD screen: incomplete — 0/12 complete"*; no `openmm`, no gromacs. No molecular dynamics informs anything below. |
| External structure / sequence databases | 🔴 **ROUTE BLOCKED, RECORDED ONCE.** `files.rcsb.org`, `rest.uniprot.org`, `www.ebi.ac.uk` all return **000 / connect_rejected** at CONNECT, and the `example.com` control returns the same — an allowlist, not a per-host failure. **No deposited SDR homodimer could be downloaded and no orthologue alignment could be built in this session.** |

### 1.2 🟢 Method positive control — REQUIRED before any number below is believed

Two methods that were not tuned on this site were asked to reproduce a fact the repository recorded
independently (*"Gln230 nel core SDR, in un segmento elicoidale ben confident"*, `CLAIM 034` source
block):

| measure | numpy backbone/neighbour method | `residue_context.py` (Shrake–Rupley + P-SEA) | repository's independent record | agree |
|---|---|---|---|---|
| secondary structure | helical, φ −65.4° ψ −50.3° | `alpha_helix` | *"segmento elicoidale"* | ✅ |
| confidence | pLDDT **98.50** | pLDDT 98.5, `very_high` | *"ben confident"* | ✅ |
| burial | neighbour count **200** (chain Q1 104 / med 142 / Q3 183 / max 232) → **83.8th percentile** | **SASA 0.0 Å², relSASA 0.000**, `buried_core` | *"nel core SDR"* | ✅ |

**Three independent routes converge.** Without this control nothing in §§2–5 would be usable. It also
reproduces the Orchestrator's own control value in
[`gln353_gln354del_structural_adjudication_20260922.md`](gln353_gln354del_structural_adjudication_20260922.md) § 2
(burial 201 vs my 200 — a one-atom difference from atom-set handling, not a discrepancy).

### 1.3 The measurements, complete

**(a) Local backbone and confidence, 218–245.**

| res | aa | φ | ψ | pLDDT | burial | burial %ile | relSASA |
|---|---|---|---|---|---|---|---|
| 226 | E | −59.4 | +132.8 | 97.81 | 195 | 81.4 | 0.005 |
| 227 | T | −63.3 | −39.3 | 98.19 | 174 | 70.0 | 0.107 |
| 228 | T | −66.0 | −49.0 | 96.38 | 220 | 96.4 | 0.024 |
| 229 | F | −59.5 | −47.9 | 98.25 | 204 | 86.2 | 0.013 |
| **230** | **Q** | **−65.4** | **−50.3** | **98.50** | **200** | **83.8** | **0.000** |
| 231 | V | −66.8 | −44.3 | 98.06 | 181 | 73.7 | 0.090 |
| 232 | N | −77.7 | −35.2 | 98.00 | 207 | 88.2 | 0.004 |
| 233 | H | −117.9 | −66.9 | 98.69 | 216 | 93.7 | 0.004 |
| 234 | L | −64.5 | −39.1 | 98.69 | **232** | **99.8 — chain maximum** | 0.000 |
| 239 | L | −56.1 | −49.3 | 98.94 | 214 | 92.3 | 0.000 |

**(b) The α-helical hydrogen-bond ladder, measured O(i−4)···N(i).** This is the DSSP-class criterion
and it resolves a size question the dihedral window alone gets wrong.

```
N229 ← O225  6.88   |  N229 ← O226  3.44  (i−3, weak)
N230 ← O226  3.03 HB
N231 ← O227  2.95 HB
N232 ← O228  2.99 HB
N233 ← O229  3.07 HB
N234 ← O230  3.22 HB
N235 ← O231  4.82   (ladder ends)
N236 ← O232  5.27   |  N236 ← O233  3.11  (i−3)
N237 ← O233  2.86 HB   … continuous α through N244
```

🔴 **Correction to the brief's framing, and it runs against the comfortable direction.** The brief
(inheriting the repository's `WWOX_Q230P_residue_context.csv`) describes *"a 6-residue helix
(227–232)"*. Three criteria disagree about its length and **all three agree Q230 is interior**:

| criterion | helix assigned | Q230's position in it |
|---|---|---|
| strict dihedral window (φ ∈ [−100,−30], ψ ∈ [−80,−5]) | **227–232** (6 res) | position 4 of 6 |
| **α-helical H-bond ladder (measured here)** | **226–234** (9 res) | **position 5 of 9 — geometric centre** |
| P-SEA, via the repository's own `residue_context.py` | **226–251** (26 res) | position 5 of 26 |

The "6-residue helix" is an artefact of the strictest of the three cutoffs: the run breaks at H233
**on φ alone** (−117.9°, ψ −66.9° is helical), and 234–242 are helical again. **The element is one
long helix with a single-residue kink at His233, not a short isolated helix.** This matters for §3:
a longer helix means more buried downstream register to displace, not less.

**(c) Q230 side-chain polar contact inventory — NE2/OE1 to any N or O within 3.6 Å, with sequence separation.**

| donor/acceptor | partner | distance | Δseq | class |
|---|---|---|---|---|
| **Q230 OE1** | **T221 OG1** | **2.54 Å** | **−9** | side-chain, **strong** |
| **Q230 NE2** | **D223 OD2** | **2.72 Å** | **−7** | side-chain, **strong** |
| **Q230 NE2** | **A185 O** | **3.20 Å** | **−45** | backbone, **long-range** |
| **Q230 NE2** | **L184 O** | **3.46 Å** | **−46** | backbone, **long-range** |
| Q230 NE2 | L186 N | 3.58 Å | −44 | backbone, long-range, **borderline** |

**Five contacts, three of them long-range (Δseq 44–46).** `NE2` is a **trifurcated** donor. And the
node is larger than Q230's own contacts: measuring T221 and D223 outward,

- **T221 OG1** is a local hub — besides Q230 OE1 it caps the backbone amides of K222 (3.41), D223
  (3.23), G224 (3.50) and L225 (3.38) and the 221–225 turn.
- **D223 OD2** is itself a tertiary connector — besides Q230 NE2 it binds **L187 N (2.84 Å)** and
  **A185 O (3.46 Å)**.

> **So Gln230's side chain is one arm of a four-way polar node — Q230·D223·A185/L187 — that pins
> helix αE to strand βC (176–185) across ~45 residues, with a second arm (OE1·T221) buttressing the
> cap of the 221–225 turn.** This is a long-range tertiary staple, not a local stabiliser. It is the
> same structural motif class the Orchestrator found at Gln353/Gln354, at a different site.

**(d) Heavy-atom contact accounting for the substitution.**

| Q230 atom | contacts ≤4.5 Å to other residues | fate in Pro |
|---|---|---|
| CB | 7 | retained (ring atom) |
| CG | 6 | retained (ring atom) |
| CD | 11 | retained **but relocated onto N** — see §3 |
| **OE1** | **13** | 🔴 **LOST** |
| **NE2** | **18** | 🔴 **LOST** |

**31 heavy-atom contacts and all five polar contacts are removed by Q→P**, before any backbone
consequence is counted.

### 1.4 🔴 Three defects in the repository's held record for this site, found by measuring

| repository says (`data/WWOX_Q230P_residue_context.csv`) | measured | verdict |
|---|---|---|
| *"Salt-bridge partner: Asp223 (NE2–OD2 2.72 Å)"* | distance **2.72 Å — correct**; but NE2 is a **neutral amide donor** | 🔴 **NOT a salt bridge.** It is a neutral-donor/charged-acceptor **hydrogen bond**. The geometry is right and the label inflates its energetic weight. Should be corrected. |
| *"Side-chain H-bonds: 4 (Thr221, Asp223, Ala185, Leu184)"* | **5** within 3.6 Å (adds L186 N at 3.58 Å, borderline) | ⚠️ minor undercount; the four named are all confirmed at the stated partners |
| *"Secondary structure: α-helix (227–232)"* | 227–232 / 226–234 / 226–251 depending on criterion | ⚠️ **understates the element.** Not wrong about Q230 being helical and interior — which is the load-bearing part — but "6-residue helix" invites the wrong accommodation argument (§3) |
| *"Backbone H-bond (i,i−4): N230–O226 = 3.03 Å (present)"* | **3.03 Å, N–H···O angular deviation 9°** | ✅ **confirmed, and it is near-ideal** |

🔴 **And the 0-based trap was checked, not assumed.** `WWOX_ThermoMPNN_saturation.csv` row
`position=229` carries `wildtype=Q`, `mutation=P`, `ddG_pred=1.5143499` — so the repository's
`+1.514` for `Q230P` is the right cell. **Per the stability census §6.1 that value carries no
evidential weight in either direction and is not used as evidence anywhere in this file.** It is
used once, in §6.3, only to compare two predictors against each other.

---

## 2 · Gln230's structural role, assessed separately against each of the seven possibilities

Each row is answered on its own evidence. **No mechanism is forced, and the seven are not made to
sum to one.**

| # | possibility | verdict | the measurement that decides it | confidence |
|---|---|---|---|---|
| 1 | **SDR-domain core packing** | 🟢 **YES — strongly** | **SASA 0.0 Å², relSASA 0.000**; burial 200 = 83.8th percentile; 22 heavy-atom contacts within 5 Å; two independent methods agree, third-party repository record agrees | **high** (as a statement about the model) |
| 2 | **oligomer / dimer interface** | 🟢 **NO** | **relSASA 0.000.** An interface residue must be solvent-accessible in the free monomer to be buried by a partner (ΔSASA > 0 requires SASA_monomer > 0). Q230 is already fully occluded by its own chain. Nearest solvent-exposed residue on αE is **Q241 at 14.3 Å**; on αF, **F277 at 12.5 Å**; Q230 is **19.2 Å** from αG and **18.1 Å** from the βG-equivalent strand. **Whole segment 226–240 has max relSASA 0.107 — it has no exposed face at all.** | **moderate-high**, and 🔴 see §5 for the monomer caveat and why it does not rescue the interface reading |
| 3 | **cofactor environment** | 🟢 **NO** | The Rossmann glycine-rich motif is **`T130-G131-A132-N133-S134-G135-I136-G137` = `TGxxxGxG`, located not assumed.** Q230's closest heavy atom to it is **10.01 Å** (to T130 OG1); CA–CA 14.0 Å. Q230 sits **12.60 Å** from the cofactor-cleft axis, **rank 114 of 414 residues** | **high** |
| 4 | **substrate-binding region** | 🟢 **NO** | Catalytic tetrad closest heavy atoms: **S281 6.79 Å · Y293 9.37 Å · K297 9.68 Å**. Side-chain vector CA→NE2 points **141° away from Y293-OH** and **136° away from K297-NZ** — into the core, not into the cleft | **high** |
| 5 | **conserved hydrogen-bond network** | 🟡 **YES as a network; NO as a conserved glutamine** | The network is measured and real (§1.3c: five contacts, four-way node, Δseq −45). But the **position**, not the residue, is what the sequence model constrains: ESM2 ranks **P worst of all 19 substitutions** at 230 (LLR −9.08, rank 1/19) while ranking **G (+1.78) and A (+0.55) as *better* than Gln itself** — see §6 | **moderate** for the network (side-chain rotamers are the least reliable part of any predicted model); **moderate** for the conservation reading, with §6's limits |
| 6 | **secondary-structure stabilisation** | 🟢 **YES — directly, through the backbone** | N230–H donates the i,i−4 helical hydrogen bond to **O226 at 3.03 Å with 9° angular deviation** — a near-ideal α-helical bond that **Pro cannot make at all** | **high** (backbone geometry, the firmest class of number here) |
| 7 | **solvent-exposed interaction surface** | 🟢 **NO** | **SASA 0.0 Å².** There is no surface to interact with | **high** |

**Composite, stated without forcing:** roles 1, 5, 6 are **YES** and they are three descriptions of the
same physical fact — an interior helical residue whose backbone amide holds the helix and whose side
chain holds the helix to a distant strand. Roles 2, 3, 4, 7 are **NO** on measured distances. **The
lesion class this geometry supports is folding/packing and local secondary structure. It is not an
interface lesion, not a catalytic lesion and not a cofactor lesion.**

---

## 3 · The proline-specific question — does P at 230 break the helix, and what is downstream?

This is the question that decides whether the substitution is marginal or severe, and it is answerable
from backbone geometry alone — which is the part of a predicted model that survives
`PMID 35716775`'s warning that *"AlphaFold2 cannot be used to assess effects of point mutations, since
it relates to point mutations as 'local noise'"*. **No predictor score is used here.** ([DOI](https://doi.org/10.1016/j.jbc.2022.102145), via PubMed)

### 3.1 🟢 φ is NOT the problem — and this is the honest half

- **φ(230) = −65.4°.** Proline's φ is restricted to roughly **−63 ± 15°**. The observed backbone
  torsion at 230 is **already almost exactly proline's preferred φ.** ψ(230) = −50.3° is α-helical and
  allowed for Pro.
- So the naive "proline restricts φ" argument **does not apply at this site.** Anyone who reaches for
  it here is reaching for the wrong argument.

### 3.2 🔴 The operative fact is the Cδ, and it is a hard steric overlap — measured

Proline's ring closes back onto the backbone nitrogen, so **Cδ occupies the direction in which the
amide hydrogen points.** I placed the idealised amide H (1.01 Å) and Cδ (1.473 Å) along that
direction and measured what is there:

| modelled atom | nearest neighbours | distance | vdW contact minimum | overlap |
|---|---|---|---|---|
| idealised **H** on N230 | **O226** | 2.04 Å | — | ✅ a near-ideal helical H-bond |
| **PRO230 Cδ** | **E226 O** | **1.60 Å** | 3.22 Å (C···O) | 🔴 **1.44 Å** |
| PRO230 Cδ | F229 C | 2.43 Å | 3.22 Å | 🔴 0.79 Å |
| PRO230 Cδ | F229 N | 2.62 Å | 3.07 Å | 🔴 0.45 Å |
| PRO230 Cδ | E226 C | 2.77 Å | 3.22 Å | 🔴 0.45 Å |
| PRO230 Cδ | F229 CA | 2.78 Å | 3.22 Å | 🔴 0.44 Å |
| PRO230 Cδ | T227 C | 2.96 Å | 3.22 Å | 🔴 0.26 Å |
| PRO230 Cδ | T227 O | 3.02 Å | 3.04 Å | 🔴 0.02 Å |
| PRO230 Cδ | F229 CB | 3.11 Å | 3.22 Å | 🔴 0.11 Å |

> 🔴 **Eight steric overlaps, the worst of them 1.44 Å, and the worst one is against the very carbonyl
> oxygen that the lost amide hydrogen was satisfying.** This is the textbook reason prolines are
> excluded from α-helix interiors, and here it is **measured on the actual coordinates rather than
> asserted from a propensity table.** The local backbone as modelled **cannot** host a proline at 230.

### 3.3 Does the helix break? — two accommodations, and both are expensive

The backbone must do one of two things. I costed both.

**Branch A — the helix frays back and Pro230 becomes the helix N1 residue.** Proline is *common and
favoured* at helix position N1, so this is the accommodation that would rescue the site — and it is
exactly the escape that existed at Gln353/Gln354, where the lesion sat at helix positions 2–3
directly adjacent to a pre-existing 348–351 coil. **Here it does not come free**, because Q230 is at
ladder position 5, not 2, so fraying must unmake three further helical bonds and leave four buried
carbonyls unsatisfied:

| bond lost if 227–229 become coil | distance now | acceptor's relSASA | cost |
|---|---|---|---|
| N230 ← O226 (3.03) | — | E226 **0.005** | lost in every branch (Pro has no NH) |
| N231 ← O227 | 2.95 | T227 **0.107** | 🔴 buried carbonyl left unsatisfied |
| N232 ← O228 | 2.99 | T228 **0.024** | 🔴 buried carbonyl left unsatisfied |
| N233 ← O229 | 3.07 | F229 **0.013** | 🔴 buried carbonyl left unsatisfied |

An unsatisfied buried backbone carbonyl is one of the more expensive things a fold can carry, and
here there would be **four**, all at relSASA ≤ 0.107 with no water access.

**Branch B — the helix kinks and keeps its register.** A mid-helix proline is normally accommodated by
a ~20–30° kink plus a bulge, which displaces everything downstream. **Downstream is the worst place in
the protein for that:**

| res | 231 | 232 | 233 | 234 | 235 | 236 | 237 | 238 | 239 | 240 |
|---|---|---|---|---|---|---|---|---|---|---|
| burial | 181 | 207 | 216 | **232** | 215 | 213 | 221 | 208 | 214 | 188 |
| %ile | 73.7 | 88.2 | 93.7 | **99.8** | 92.8 | 91.3 | 96.9 | 89.1 | 92.3 | 76.3 |
| relSASA | 0.090 | 0.004 | 0.004 | **0.000** | 0.000 | 0.012 | 0.007 | 0.075 | **0.000** | 0.006 |

- **Eight of the ten residues downstream are above the 75th burial percentile.**
- **Leu234 — four residues downstream, the acceptor of O230's own helical bond — is the single most
  buried residue in the entire 414-residue chain** (burial 232, 99.8th percentile, SASA 0.000).
- **Leu239 — nine residues downstream on the same helix — is itself an independently reported
  pathogenic WWOX allele** (`L239R`; see [`l239r_intraallelic_comparator_20260921.md`](l239r_intraallelic_comparator_20260921.md),
  another actor's reading, treated here as that actor's attestation). It is buried at relSASA 0.000.
  **That is an intra-helix, intra-domain demonstration that this specific helix does not tolerate
  substitution, from a source independent of any structural prediction.** ⚠️ It is a *phenotype*
  co-occurrence, not a measurement of `L239R` protein — no `L239R` protein-level datum exists.
- Asn232 additionally sits **5.82 Å from the cofactor-cleft axis** — the only residue of 226–240 that
  reaches the cleft rim at all. **A kink at 230 is two residues from a cleft-rim residue.** This is
  the one indirect route by which a packing lesion at 230 could reach the active site, and it is
  geometry, not evidence of anything functional.

**Answer to the question as posed:** ✅ **Yes — P at 230 is incompatible with helix 227–232/226–234 as
modelled, and the incompatibility is a Cδ/O226 collision rather than a φ restriction.** Whether the
protein *resolves* it by fraying (Branch A) or kinking (Branch B) cannot be told from a static model,
**and the two branches were not both explored by molecular dynamics because no MD engine exists in this
deployment.** What the model does establish is that **neither branch is cheap**, and that — unlike the
Gln353/Gln354 case, where an adjacent coil supplied a low-strain accommodation off by about six
residues — **here the adjacent coil is four residues too far upstream and every residue downstream is
core.** `IPOTESI`.

---

## 4 · Cofactor and catalytic-site geometry — distances measured, not assumed

### 4.1 The motifs were located before they were used

| motif | assigned position | how |
|---|---|---|
| **Rossmann glycine-rich cofactor motif (`TGxxxGxG`-like)** | **`T130-G131-A132-N133-S134-G135-I136-G137`** = **`TGANSGIG`** | read out of the coordinate-derived sequence, **not assumed**. It is an exact `TG-xxx-G-x-G` match immediately following strand βA (125–131) — the canonical SDR position |
| **catalytic `Y-x-x-x-K`** | **Y293-N294-R295-S296-K297** | confirms the brief's `Y293…K297` |
| **catalytic Ser** | **S281** | ✅ independently corroborated: [`lectin_readout_domain_dependence_20260921.md`](lectin_readout_domain_dependence_20260921.md) (**another actor's attestation, FT-143, not my reading**) records the WWOX catalytic-triad substitutions used in the field as **S281A / Y293F / K297A**. My geometry independently puts S281 at 6.79 Å from Q230 and **4.19–5.29 Å from the cofactor-cleft axis** for the neighbouring serines — consistent with a catalytic serine at that position |

### 4.2 The cofactor cleft, defined geometrically and then measured against

I defined the cleft axis as the segment from the **Gly-rich loop centroid (CA of 131–135)**, where the
adenosine of NAD(P) binds in every SDR, to **Y293-OH**, the nicotinamide end. Its length is **13.87 Å**
— the right span for a bound dinucleotide, which is itself a check that the axis is real and not an
artefact.

**First-shell cleft residues, by minimum heavy-atom distance to that axis:**

```
Y293 0.00 · S134 1.81 · G131 1.81 · N133 2.39 · A132 2.46 · K297 3.20 · N210 3.33
A212 3.45 · F138 3.54 · G137 3.82 · G135 4.01 · S260 4.19 · F214 4.53 · I136 4.54
A211 4.92 · I331 4.99 · S259 5.02 · T130 5.12 · S262 5.29 · T213 5.31 · V258 5.39
C155 5.39 · N232 5.82 · P323 6.09 · S329 6.12
```

| measurement | value |
|---|---|
| **Q230 → cleft axis** | **12.60 Å — rank 114 of 414 residues** |
| Q230 → nearest atom of `TGANSGIG` (T130 OG1) | **10.01 Å** |
| Q230 → S281 (catalytic Ser) | 6.79 Å |
| Q230 → Y293 (catalytic Tyr) | 9.37 Å |
| Q230 → K297 (catalytic Lys) | 9.68 Å |
| CA→NE2 vector vs CA→Y293-OH | **141°** — pointing away |
| CA→NE2 vector vs CA→Gly-loop | 93° — orthogonal |

> 🟢 **Verdict: `Gln230` is NOT a cofactor residue and NOT a substrate-pocket residue.** It is
> **second shell**: ~7–10 Å from the catalytic tetrad, ~10 Å from the cofactor motif, 12.6 Å from the
> cleft axis, with its side chain pointing 141° away from the catalytic tyrosine.
>
> ⚠️ **But do not over-read the comparison with Gln353/Gln354.** That site is >20 Å from the tetrad
> and is unambiguously remote. `Gln230` at 6.8–9.7 Å is **nearer than that but still outside the
> site** — and its own helix contributes **Asn232 at 5.82 Å from the cleft axis**. So the honest
> statement is: *a direct catalytic/cofactor lesion is excluded; an indirect one, via helix distortion
> propagating two residues to a cleft-rim residue, is **geometrically available and completely
> untested.*** `IPOTESI`.

### 4.3 What the biochemistry can and cannot contribute

According to PubMed, the **entire** WWOX enzymology literature is one paper — Sałuda-Gorgul, Seta,
Nowakowska & Bednarek, *Z Naturforsch C* 2011;66(1–2):73–82, **PMID 21476439**, *"WWOX oxidoreductase
— substrate and enzymatic characterization"*; there is no PMCID and the body is unreachable from this
deployment. As held in [`wwox_sdr_function_per_molecule_census_20260921.md`](wwox_sdr_function_per_molecule_census_20260921.md)
(**another actor's reading, abstract-depth, treated as that actor's attestation**), it reports
oxidoreductase activity **in a crude bacterial extract**, on **wild-type** protein, with NAD⁺/NADP⁺
dependence and Km values, and no purified enzyme and no catalytically-dead control.

🔴 **Consequences, stated plainly:**
1. **No WWOX protein has ever been shown to bind NAD(P) directly.** Cofactor dependence was inferred
   from activity in crude extract. So §4.2's "cofactor cleft" is a **geometric inference from a fold
   assignment**, not a mapped binding site.
2. **No disease allele has ever been through any catalytic assay**, so there is no functional readout
   against which a "catalytic/cofactor defect" hypothesis for `Q230P` could even be tested.
3. Even a rescued-abundance `Q230P` could not be scored for function today:
   [`missense_rescue_methodology_census_20260921.md`](missense_rescue_methodology_census_20260921.md)
   (**another actor's census, built from titles and abstracts — "an abstract is not a read", nothing in
   it promotable without a full-text read and a receipt**) states *"No functional measurement has ever
   been made on a WWOX missense protein whose abundance was restored."*
   [`mave_portability_to_wwox_20260921.md`](mave_portability_to_wwox_20260921.md) (**same status;
   verdict `CONDITIONAL`; one of its two papers, PMID 42425971, is a bioRxiv `[PREPRINT]` and that
   weight is preserved here**) locates the binding constraint precisely: the abundance half of a MAVE
   is portable, the **function** half is not, because WWOX has no validated cell-autonomous
   antibody-detectable downstream consequence of its activity. That file also reports the quantified
   brake that bears directly on this node — in TSC2, **31 of 80 (38.75%) ClinVar P/LP missense
   variants had NORMAL abundance**, which is the `P282A` problem measured at scale.
4. 🔴 **No sensor programme and no MAVE programme is proposed here.** Both are materially new research
   programmes and the Operator's decision, per
   [`wwox_activity_sensor_census_20260921.md`](wwox_activity_sensor_census_20260921.md).

---

## 5 · The dimer-interface question — the single fact that would flip the sign

### 5.1 🟢 RESOLVED IN THE NEGATIVE, by an argument that does not require knowing where the interface is

> **`Gln230` has SASA = 0.0 Å² and relSASA = 0.000 in the monomer model.**
>
> **A dimer interface buries residues that were solvent-accessible in the free subunit.** That is the
> operational definition of an interface residue: ΔSASA on complexation > 0, which requires
> SASA_monomer > 0. **A residue with zero accessible surface is already completely occluded by its own
> chain and contributes nothing to any interface, wherever that interface turns out to be.**

This argument is **topology-independent**, which is what makes it usable against a monomer model. I
then checked it against both dimerisation modes the SDR literature actually documents.

### 5.2 Where WWOX's interface *could* be — SDR topology mapped, then measured

I derived the SDR-domain topology from the repository's own `residue_context.py` SSE assignment and
mapped it onto the canonical Rossmann/SDR order:

| segment | residues | canonical SDR element | note |
|---|---|---|---|
| β 125–131 | 7 | **βA** | carries `T130-G131`, start of the Gly-rich loop |
| α 135–148 | 14 | αB | |
| β 150–155 | 6 | βB | |
| α 157–172 | 16 | αC | |
| β 176–185 | 10 | **βC** | 🔴 **the strand Q230's side chain staples to** |
| α 186–200 | 15 | αD | |
| β 201–223 | 23 | **βD** | carries `N210-A211-A212-T213` (`NNAG`-position) |
| **α 226–251** | **26** | 🔴 **αE** | 🔴 **Q230 is here, at position 5** |
| β 252–262 | 11 | βE | contains P252 |
| β 265–270 · β 274–276 | 6 · 3 | **a ~25-residue βE→αF insertion (263–276)** | see §5.3 |
| α 277–281 + α 283–315 | 5 + 33 | **αF** | carries **S281**, and **Y293…K297** |
| β 317–330 | 14 | βF | |
| **α 335–349** | **15** | **αG** | see §5.4 |
| α 351–363 | 13 | the Gln353/Gln354 helix | |
| β 370–376 · α 377–381 · β 382–384 · α 385–400 | | C-terminal | |

**The two documented SDR dimerisation modes, and Q230's distance from each.** According to PubMed:

| mode | documented source | WWOX element | Q230's distance |
|---|---|---|---|
| **the αE/αF four-helix bundle** (the classic homodimer/homotetramer interface) | Hoffmann *et al.*, *J Biotechnol* 2006, **PMID 17258342**, `abstract-depth`: *"a 28 amino acids insertion into the classical Rossmann-fold motif between strand betaE and helix alphaF. This insertion is masking helices alphaE and alphaF, thus preventing the formation of a four helix bundle"* ([DOI](https://doi.org/10.1016/j.jbiotec.2006.11.024)). Corroborated by Zhao *et al.*, *BBRC* 2023, **PMID 37285720**, `abstract-depth`: in the SDR **cnTSC10/KDSR**, *"the homo-dimer interface involves both hydrophobic and hydrophilic interactions mediated by helices α4 and α5, as well as the loop connecting strand β4 and helix α4"* ([DOI](https://doi.org/10.1016/j.bbrc.2023.05.109)) | **αE = 226–251**, **αF = 277–315** | 🔴 **Q230 is ON αE — but relSASA 0.000.** The whole segment **226–240 has max relSASA 0.107 and no exposed face**. The nearest solvent-exposed residue is **Q241 (relSASA 0.228) at 14.3 Å** on αE and **F277 (0.265) at 12.5 Å** on αF |
| **the αG/βG (P-axis) interface** | Grimm *et al.*, *JBC* 2000, **PMID 11007791**, `abstract-depth`: 3α-HSD/CR *"Dimerization takes place via an interface essentially built-up by helix alphaG and strand betaG of each subunit. So far this type of intermolecular contact has exclusively been observed in homotetrameric SDRs but never in the structure of a homodimeric SDR"* ([DOI](https://doi.org/10.1074/jbc.M007559200)); restated in Maser *et al.*, *Chem Biol Interact* 2001, **PMID 11306088** ([DOI](https://doi.org/10.1016/s0009-2797(00)00302-1)) | **αG = 335–349** | **19.2 Å** from Q230 (nearest residue 338); the βG-equivalent strand 370–376 is **18.1 Å** away |

> 🟢 **Under either documented mode, `Gln230` is not an interface residue.** It is a first-shell
> **packing** residue *of* the canonical dimerisation helix, ≥12.5 Å from the nearest solvent-exposed
> residue on that helix or its partner helix, and itself at relSASA 0.000.

### 5.3 ⚠️ A partial, honest finding about which mode WWOX could use — reported including the half that failed

WWOX **does** carry a ~25-residue insertion between βE (252–262) and αF (277–315) — residues 263–276 —
structurally analogous in position and length to the 28-residue insertion that in 3α-HSD/CR masks
αE/αF and forces dimerisation through αG/βG (PMID 17258342). **I tested whether it masks the αE/αF
face, and it only half does:**

- insertion 263–276 vs **αF (277–315)**: **133 atom pairs across 23 residue pairs** — it does pack
  against αF, including over R279, L280, L291, N294, R295, K297, L298
- insertion 263–276 vs **αE (226–251)**: 🔴 **0 atom pairs.** **It does not touch αE at all.**

**So the analogy is real for αF and false for αE, and I report it that way rather than as a clean
result.** It does not establish which mode WWOX uses. `IPOTESI`, weak.

### 5.4 The candidate interface the data actually points at — and why its confidence is poor

Measuring exposed hydrophobic clustering across the SDR domain (relSASA ≥ 0.25, hydrophobic,
single-link at 8 Å CB–CB) returns exactly **two** clusters, and both are on αG:

| cluster | exposed hydrophobic SASA | mean pLDDT | min CB distance to Q230 |
|---|---|---|---|
| **W335, W336, V337, Y338, L340, L341, L344** | **826 Å²** | 🔴 **42.4** | **22.4 Å** |
| M326, Y328, F348 | 365 Å² | 🔴 40.8 | 24.8 Å |

αG (335–349) carries **1495 Å² of total SASA** with relSASA 0.33–0.74 across most of its length,
including a solvent-exposed tryptophan pair (W335 0.545, W336 0.657). **An exposed adjacent
tryptophan pair with ~340 Å² of accessible aromatic surface is what an unsatisfied protein–protein
interface looks like** — and it lands precisely on the element that PMID 11007791's P-axis mode uses.

🔴 **But that region is the lowest-confidence part of the whole chain (pLDDT 35–53).** So the reading
is genuinely two-sided: either AlphaFold cannot place αG because its binding partner is absent from
the input (which is the interpretation that makes it an interface), or the prediction there is simply
wrong. **I cannot tell these apart, and I will not choose.** Either way it is **22.4 Å from Q230**, so
neither reading touches this file's verdict.

### 5.5 🔴 THE PREMISE UNDERNEATH THE QUESTION DID NOT SURVIVE CHECKING

The whole interface fork rests on the repository's statement, held in Italian in
`discovery_ledger_current.md:852` and quoted forward into the stability census and the Gln353
adjudication, that *"WWOX **omodimerizza via SDR**"*. **I went looking for its source and could not
find one.** According to PubMed:

| query | `query_translation` checked term-by-term | total | what came back |
|---|---|---|---|
| `WWOX AND (dimerization OR dimerisation OR homodimer OR oligomerization)` | ✅ **every limb expanded, nothing silently dropped** from the OR block | **1** | 🔴 **PMID 39894307** — a toosendanin/ferroptosis HCC paper reporting *"the nuclear distribution of p-WWOX and p-p53 **dimers**"*. **A hetero-dimer with p53. Not a WWOX homodimer, and nothing about the SDR interface.** ([DOI](https://doi.org/10.1016/j.bcp.2025.116790)) |
| `WWOX AND ("self-association" OR "homo-dimer" OR "homodimeric" OR "quaternary structure" OR "SEC-MALS" OR "analytical ultracentrifugation")` | ✅ all limbs expanded | **2** | 🔴 **Neither is WWOX self-association.** PMID 22534828 is **TIAF1** self-aggregation ([DOI](https://doi.org/10.1038/cddis.2012.36)); PMID 17567906 is **Zfra** self-association ([DOI](https://doi.org/10.1186/1471-2199-8-50)). WWOX co-occurs in both as an interaction partner |
| **positive control** — `WWOX AND Gln230` | `("wwox protein human"[Supplementary Concept] OR … OR "wwox"[All Fields]) AND "Gln230"[All Fields]` | **1 → PMID 29808465** | ✅ **the control fires** |

> 🔴 **On the searches I can run, there is no published demonstration that WWOX homodimerises through
> its SDR domain, and certainly no mapping of such an interface.** The premise is
> **`PREMISE: UNVERIFIED`** — which is a *different* label from the `PREMISE: NOBODY_LOOKED` that
> applies to the measurements.

⚠️ **Bounds on that negative, stated rather than hidden.** These are `[All Fields]` queries, which do
**not** index Methods or supplements — trap (c), whose miss rate in this gene has been 100% for
method-only terms. A gel-filtration or co-IP result appearing only in a Methods section, or a paper
phrasing it as "WWOX oligomer" inside a figure legend, would be invisible. **I therefore report this
as a query census, not as a biological zero.** The repository's Italian sentence may well trace to a
review statement or to the SDR fold assignment rather than to a WWOX experiment; **finding its actual
source is a cheap, high-value acquisition (§10).**

### 5.6 What this does to the fork, exactly

| the fork as posed | status after this section |
|---|---|
| *"Whether `Gln230` lies at the SDR dimer interface"* | 🟢 **Answered NO** — on relSASA 0.000, on ≥12.5 Å to the nearest exposed residue of either documented interface element, and on the whole 226–240 segment having no exposed face |
| *"No monomer model can establish it"* | ⚠️ **Partly superseded.** A monomer model cannot establish where an interface **is**. But it **can** exclude a residue from any interface, because zero monomer accessibility is a sufficient exclusion. **That asymmetry is the methodological result of this file.** |
| the residual monomer caveat | 🔴 **Real and retained.** If WWOX is an obligate dimer and AlphaFold predicted the *subunit-in-dimer* conformation, then (i) interface residues would already read partly buried and (ii) an interface contact cannot appear at all. **Both distortions run in the direction of under-counting exposure, i.e. they could make a truly exposed residue look buried.** For Q230 that would require SASA to move from **exactly 0.0 Å²** to a non-zero interface contribution — the one residue class where the distortion has no room to operate. **A residue at relSASA 0.000 cannot be made an interface residue by correcting a monomer bias downward.** |

---

## 6 · Evolutionary / conservation evidence, with its limits

🔴 **Stated before the evidence: my two best evolutionary routes were both blocked.** No orthologue
FASTA could be fetched (UniProt, EBI both `connect_rejected`), no SDR-family MSA could be built, and
no deposited SDR homodimer could be downloaded to transfer interface residues by alignment. **So there
is no residue-level, alignment-based conservation measurement in this file.** What follows is weaker
than what the brief hoped for, and I say so rather than dress up a substitute.

### 6.1 What the literature supplies — whole-protein, not residue-level

According to PubMed, at `abstract-depth`:

- Tanna & Aqeilan, *Front Oncol* 2018, **PMID 30370248**: *"A high sequence conservation of \[WWOX\]
  orthologues from insects to rodents and ultimately humans suggest its significant role in
  physiology and homeostasis."* ([DOI](https://doi.org/10.3389/fonc.2018.00420))
- Battaglia *et al.*, *Front Pediatr* 2023, **PMID 38161429**: *"WWOX protein is highly conserved
  among species…"* ([DOI](https://doi.org/10.3389/fped.2023.1301166))

⚠️ **Both are whole-protein statements in reviews. Neither says anything about position 230.** They
establish that WWOX is under strong purifying selection as a protein; they cannot distinguish a core
residue from an interface residue from a catalytic residue, which is exactly the discrimination the
brief asked conservation to make. **They carry no weight on the mechanism question.**

### 6.2 The sequence-model signal already in the repository — and what it actually says

`data/WWOX_ESM2_Q230_scores.json` holds a saturation LLR at position 230. 🔴 **ESM2 is a prediction,
not a measurement** — but it is a prediction *from evolutionary sequence statistics*, so it does not
inherit the inversion that disqualifies the ΔΔG predictor (stability census §6.1), which is a
structure-based folding-energy model calibrated on a different quantity entirely.

| substitution | LLR | rank of 19 |
|---|---|---|
| **P** | **−9.078** | 🔴 **1 — the single worst substitution at position 230** |
| W / K / I / R | −7.73 / −7.64 / −7.31 / −7.11 | 2–5 |
| N / T | −4.98 / −4.91 | 11–12 |
| S | −2.68 | 17 |
| **A** | **+0.545** | 18 — *preferred over Gln* |
| **G** | **+1.780** | 19 — *preferred over Gln* |

**Two readings, and they point in different directions. Both are reported.**

🟢 **The robust part.** Proline is ranked **worst of all nineteen** at this position, by a clear margin
(−9.08 against −7.73 for the runner-up). That is an evolutionary-statistics signal that agrees with my
independent backbone geometry (§3.2), which the model had no access to. **Two independent
methods — a sequence model and a measured steric overlap — converge on proline specifically being
uniquely intolerable at 230.** That convergence is the strongest single result in this file.

🔴 **The part that cuts the other way, and it is the honest limit on possibility 5.** ESM2 prefers
**Gly and Ala over Gln itself** at 230. Read literally, the family consensus at this position is a
**small residue**, and **Gln230's own amide identity is not the conserved element.** If so, the
constraint at 230 is on **backbone conformation and side-chain volume**, not on the specific hydrogen
bonds §1.3c inventories — which would mean the five-contact polar node is a *human-WWOX-specific
elaboration* rather than a conserved network. **I flag this as the reading that would most weaken §2
row 5, and I do not resolve it.**

### 6.3 A predictor discordance worth recording, used only to compare predictors

At position 230, ThermoMPNN's worst substitutions are **R (+1.807), K (+1.667), G (+1.599), P
(+1.514)** — i.e. **it ranks proline only fourth**, and it ranks **Gly as nearly as bad as Pro** while
ESM2 ranks Gly as *better than wild type*. So the two predictors disagree about the nature of the
constraint at this site, and **my measured Cδ/O226 collision is a mechanism a ΔΔG model that scores
rotamer repacking is structurally unable to see.** ⚠️ **Used here only as a statement about two
predictors, not as evidence about `Q230P`.** Per stability census §6.1, `+1.514` carries no evidential
weight in either direction and no argument in this file depends on it.

### 6.4 Limits, stated plainly

1. No alignment, no per-site conservation score, no orthologue-level check on position 230 — **the
   route the brief flagged as unused remains substantially unused, for a tool reason, and that is a
   gap not a finding.**
2. ESM2 is a prediction. Its LLR is **not** a conservation measurement; it is a language model's
   next-token statistics over evolutionary sequence data.
3. **I could not do the discrimination the brief asked for** — interface vs catalytic vs core
   residues have different conservation signatures, and telling them apart needs a family MSA I could
   not build. §5's conclusion therefore rests on **geometry (relSASA, distances), not on
   conservation.**

---

## 7 · Transferred fold-family evidence — labelled as transferred

> 🔴 **EVERYTHING IN THIS SECTION IS TRANSFERRED. NOT ONE DATUM BELOW IS ABOUT WWOX.** A mechanism
> class can transfer; a conclusion cannot. Rows inherited from
> [`wwox_missense_stability_census_20260922.md`](wwox_missense_stability_census_20260922.md) § 8 are
> **Scientist S's reading at `abstract-depth`, treated as that actor's attestation, not re-read here**
> (`FT-137`, all `PREMISE: UNREAD_PRIMARY`).

| protein | fold | lesion class | outcome | source · depth |
|---|---|---|---|---|
| **11β-HSD2** | SDR | Tyr338His, Arg337His — patient missense, **monomer core** | 🟢 WT t½ **21 h** → **3 h / 4 h**; partial rescue at 26 °C and with glycerol/dexamethasone, *"indicating thermodynamic instability and misfolding"*; **proteasomal** | Atanasov 2007, PMID 17314322, `abstract-depth` |
| **HSD17B10 / SDR5C1** | SDR | p.V12L vs p.V176M | 🟢 **two different mechanisms in one SDR** — *"reduced stability"* vs *"impaired kinetics and complex formation"* | Oerum 2017, PMID 28888424, `abstract-depth` |
| **HSD17B10 / SDR5C1** | SDR | multiple | 🟢 some *"disrupt the homotetramerization"* | Vilardo & Rossmanith 2015, PMID 25925575, `abstract-depth` |
| 🔴 **17β-HSDcl** (*Cochliobolus lunatus*) | SDR homodimer | **F124, F132, F133, F177 — hydrophobic residues AT THE DIMER INTERFACE** | 🔴 *"inactive aggregates and oligomers with high molecular masses"* | Brunskole 2008, PMID 18775764, `abstract-depth` |
| **3α-HSD/CR** (*C. testosteroni*) | SDR homodimer | — (topology, not a lesion) | dimerises via **αG + βG**, not the four-helix bundle; the βE→αF insertion masks αE/αF | Grimm 2000, **PMID 11007791**, `abstract-depth` ([DOI](https://doi.org/10.1074/jbc.M007559200)) · Hoffmann 2006, **PMID 17258342** ([DOI](https://doi.org/10.1016/j.jbiotec.2006.11.024)) — **read at `abstract-depth` by me, this session, via PubMed** |
| **cnTSC10 / KDSR** | SDR | — (topology) | homodimer interface *"mediated by helices α4 and α5, as well as the loop connecting strand β4 and helix α4"*; interface H-bond/salt-bridge residues **not conserved** between fungal TSC10 and mammalian KDSR | Zhao 2023, **PMID 37285720**, `abstract-depth`, **read by me this session** ([DOI](https://doi.org/10.1016/j.bbrc.2023.05.109)) |

**What transfers as a mechanism class:**
- In the SDR fold, a destabilising missense **in the monomer core** characteristically yields a
  short-half-life protein cleared by a quality-control route, and that phenotype is
  temperature- and chemical-chaperone-rescuable in at least one human disease gene.
- 🔴 **The route does NOT transfer.** Proteasomal for 11β-HSD2; **lysosomal and MG-132-insensitive**
  for the one WWOX allele ever routed (`P252A`). **The fold does not fix the route.**
- Two missense in the same SDR can fail by two different mechanisms — the fold-family restatement of
  `P252A` vs `P282A`.
- 🆕 **An SDR can dimerise through at least two distinct interfaces** (αE/αF four-helix bundle;
  αG/βG P-axis), and **which one a given SDR uses is not predictable from the fold assignment alone.**
  That is new in this repository and it is why §5 tested both.
- 🆕 **Interface residues are not conserved across SDR family members even between orthologous
  enzymes** (PMID 37285720). 🔴 **This independently forecloses the brief's proposed route of mapping
  a deposited SDR homodimer's interface residues onto WWOX by alignment** — even had the download
  worked, the transfer would not have been sound.

**What does NOT transfer:**
- Any statement about `Q230P`. None of these proteins is WWOX; none is measured in a neuron.
- 🔴 **`GTPBP3` p.Q230P must not be transferred**, notwithstanding that it is a *measured*
  aggregation-and-degradation result at an identical `c.689A>C (p.Q230P)` (PMID 41957021, *Nat Commun*
  2026; PMID 38515655). Different gene, different fold, different disease. **A bare `"Q230P"` PubMed
  query returns 2 records and neither is WWOX** — the namespace tripwire of `FT-138`, re-confirmed by
  not falling into it.

### 7.1 🔴 The exception that would have flipped the sign — and why it does not apply

Brunskole 2008 is the one SDR aggregation result, and it is **specific about the lesion class**:
*"Phenylalanine substitutions introduced **at the dimer interface** produced inactive aggregates and
oligomers with high molecular masses."*

| the trigger, as documented | `Q230P`, as measured here |
|---|---|
| substitution **at** the dimer interface | 🟢 **relSASA 0.000** — no interface contribution possible |
| **hydrophobic** residues (F124/F132/F133/F177) substituted **to other phenylalanines**, i.e. exposed aromatic surface remodelled | a **buried polar** residue substituted to a **cyclic aliphatic** one, with no exposed surface involved |
| lesion on a **solvent-exposed** interface face | lesion ≥12.5 Å from the nearest exposed residue of either candidate interface element |

> 🟢 **`Q230P` is not a member of the lesion class that produced aggregation in the fold family.** It
> is a member of the **monomer-core** class, whose documented fold-family default is **degradation**.
>
> 🔴 **And that is a statement about a transferred prior, not about WWOX.** The route in WWOX would
> still have to be measured, and the one time it was measured in this gene it was **lysosomal**, not
> the proteasomal route the transferred exemplar used.

---

## 8 · MECHANISM VERDICT

### 8.1 Per component, with confidence

| component | verdict | confidence | what it rests on |
|---|---|---|---|
| **Folding / stability (core packing)** | 🟢 **SUPPORTED as the primary lesion class** | **moderate-high** *as a prediction* · 🔴 **ZERO as a measurement** | relSASA 0.000; burial 83.8th %ile; a measured **1.44 Å Cδ/O226 steric overlap**; loss of a near-ideal helical H-bond (3.03 Å, 9° deviation); 31 heavy-atom and 5 polar contacts removed; no low-cost accommodation on either branch (§3.3) |
| **Secondary-structure destabilisation** | 🟢 **SUPPORTED — and it is the sharpest single fact** | **high** *for the geometry* | Pro cannot donate the i,i−4 amide hydrogen that N230 donates to O226, and its Cδ collides with that same oxygen. **Backbone-only; survives PMID 35716775's point-mutation warning** |
| **Interface disruption** | 🟢 **NOT SUPPORTED** | **moderate-high** | relSASA 0.000 (a topology-independent exclusion); ≥12.5 Å to the nearest exposed residue of either documented SDR interface mode; 226–240 has no exposed face. 🔴 Residual monomer caveat §5.6, which cannot lift a residue from exactly 0.0 Å² |
| **Aggregation** | 🟡 **NOT SUPPORTED, NOT EXCLUDED** | **low** | The only documented SDR aggregation trigger is interface substitution (§7.1) and `Q230P` is not that class. 🔴 **But "not the known trigger" is not "will not aggregate":** a core lesion that misfolds without being cleared is a generic aggregation risk, and **nobody has looked in the pellet** for any WWOX allele |
| **Catalytic / cofactor** | 🟢 **NOT SUPPORTED as a direct lesion** · 🟡 **available as an indirect one** | **high** direct · **very low** indirect | 12.60 Å from the cofactor-cleft axis (rank 114/414), 10.0 Å from `TGANSGIG`, 6.8–9.7 Å from S281/Y293/K297, side chain 141° away. **Indirect:** Asn232 sits 5.82 Å from the cleft axis, two residues from a helix that must distort |
| **Degradation / turnover** | ⚪ **NOT ASSESSABLE** | — | 🔴 `PREMISE: NOBODY_LOOKED`. Never measured for `Q230P` or for any WWOX missense variant. A structural prediction cannot supply a half-life |
| **Abundance** | 🟡 **TWO indirect data, both `abstract-depth`, cause untested** | 🔴 **capped by §0.4** | Protein **not detected** on one Western of homozygous patient fibroblasts; **transcript normal** by qRT-PCR in donor-derived fibroblasts (Johannsen 2018, PMID 29808465). 🔴 **Both are `abstract-depth` / `PREMISE: UNREAD_PRIMARY`** — the paper is `unrecoverable_by_these_routes`, `pmc_id: null`, closed at Springer; **n, controls, densitometry and the qRT-PCR amplicon position have never been read by anyone here.** Normal message localises the lesion **post-transcriptionally** and leaves exactly three causes: **reduced translation, accelerated turnover, insolubility.** The authors named the first two and tested neither; **the third is un-named and nobody has looked in the pellet** |
| **Splicing / cryptic-splice confound** | 🟢 **EXCLUDED** | **moderate-high** (another actor's attestation, §0.1) | `c.689A>C`, exon 7, **66–84 nt from any junction**; codon arithmetic validated on nine published c./p. pairs including `c.689`/p.230. 🔴 **This removes a competing explanation; it is not evidence about folding and is used as none** |

### 8.2 The verdict in one paragraph, with the labels on

🟡 **`IPOTESI`.** On structural, evolutionary-model and transferred biochemical evidence, `Q230P` is
best supported as a **combined folding/packing + local secondary-structure lesion in the SDR monomer
core**, with **no support for an interface, cofactor-environment, substrate-pocket or
solvent-exposed-surface role for Gln230**, and with **turnover, solubility and aggregation propensity
entirely unmeasured**. The two structural facts carrying the most weight are a **measured 1.44 Å
steric overlap** between the modelled proline Cδ and the Glu226 carbonyl, and **relSASA 0.000**. Both
are geometry, on a predicted monomer, from a model whose own field warns it treats point mutations as
*"local noise"* — so the correct reading is: **the geometry says what class of lesion this could be,
and says nothing about what the protein actually does.**

### 8.3 🔴 What would falsify this — stated as a list of specific observations

| component | a single observation that would falsify it |
|---|---|
| core packing / folding | A thermal-shift or CD melt on purified `Q230P` SDR showing **Tm indistinguishable from wild type**. (🔴 Not available at any price today: the WWOX SDR domain has never been expressed or purified by anyone, and PMID 35716775 — the only WWOX biophysics that exists — covers residues **16–91** only) |
| secondary-structure lesion | An experimental structure (crystal or cryo-EM) of WWOX showing residue 230 **not** in a helix, or showing N230 **not** donating to O226 — i.e. the AlphaFold backbone being wrong at a pLDDT-98.5 site |
| **interface exclusion — the cheapest falsifier** | 🔴 **Any experimental or AlphaFold-Multimer WWOX dimer in which residue 230 is within 5 Å of the partner chain.** That single observation would invert §9's sign. **This is the one falsifier that is achievable with no wet work** (§10, item 1) |
| aggregation not-supported | A solubility split on `Q230P` finding protein **in the insoluble pellet** — which would make the boost axis dangerous regardless of §5 |
| catalytic not-supported | A purified-enzyme assay finding `Q230P` protein **present, folded, and catalytically dead at matched abundance** — the `P282A` pattern at this allele |
| the whole composite | Any demonstration that the AlphaFold monomer is the **wrong conformation** for WWOX — e.g. that the SDR is an obligate dimer whose free subunit is substantially unfolded. Then every SASA number here, including the 0.000 the interface exclusion rests on, would need recomputing |

---

## 9 · The therapeutic sign

> ## 🟡 **The non-allele-specific WWOX-upregulation axis reads NOT-DANGEROUS-ON-THIS-EVIDENCE, and STILL UNDETERMINED.** `IPOTESI`.

**Where the sign stood entering this file** (per
[`gln353_gln354del_structural_adjudication_20260922.md`](gln353_gln354del_structural_adjudication_20260922.md) § 9
and the stability census § 8.3):

| if the lesion is… | consequence | therapeutic reading |
|---|---|---|
| degradation-prone, interface intact | cleared | 🟢 a chaperone / proteostasis route is coherent |
| **interface-disrupting** | **aggregation** | 🔴 **a boost is actively dangerous** |

**What this file changes, and only this:**

1. 🟢 **The identified red flag is removed.** The specific trigger that produced *"inactive aggregates
   and oligomers with high molecular masses"* in the one SDR aggregation exemplar is **substitution at
   the dimer interface** (PMID 18775764). **`Gln230` has relSASA 0.000 and is ≥12.5 Å from the nearest
   solvent-exposed residue of either documented SDR dimerisation element. `Q230P` is not that lesion
   class.** So the branch that made a boost *actively dangerous* is **not supported by the structural
   evidence.**
2. 🔴 **And a second, larger uncertainty was exposed rather than closed.** The interface fork
   presupposed a WWOX SDR homodimer, and **I could not find a published source establishing that WWOX
   homodimerises through its SDR at all** (§5.5). `PREMISE: UNVERIFIED`. A fork whose premise is
   unverified cannot be resolved *in favour of either branch* — and the correct response is to stop
   treating the interface branch as a live 50% and start treating it as **unsourced**.
3. 🔴 **Removing one identified danger is not establishing safety, and the boost axis does not become
   green.** Three reasons, each independently sufficient:
   - **The pellet has never been looked in.** No WWOX allele has ever had a solubility split. A
     core-misfolding lesion that is *not* an interface lesion is still a generic aggregation risk —
     §7.1 shows only that it is not the *documented* trigger. **`PREMISE: NOBODY_LOOKED`.**
   - **Abundance is not stability is not solubility is not function.** `Q230P`'s protein-level
     evidence is a single non-detection on one Western of patient fibroblasts, alongside a normal
     transcript by qRT-PCR — 🔴 **both `abstract-depth`, from a paper recorded
     `unrecoverable_by_these_routes` whose body nobody here has read** (§0.4). The normal message
     rules the lesion post-transcriptional and leaves **reduced translation, accelerated turnover and
     insolubility all untested** — three lesions with three different therapies. A boost is coherent
     for one of the three and futile-to-harmful for the other two.
   - 🔴 **And the emptiness is structural, not incidental.** Of 19 enumerable WWOX missense alleles,
     **one** has ever had RNA examined; against Piard's own denominator, **10 of 11 have no
     experimental evidence at all — 90.9%** (§0.5). A sign derived in a 90.9%-empty evidence base is
     a bookkeeping statement, not a safety finding.
   - **`P282A` is the standing proof that a stable WWOX missense protein can be functionally dead**,
     and [`missense_rescue_methodology_census_20260921.md`](missense_rescue_methodology_census_20260921.md)
     (another actor's abstract-built census) records that *"No functional measurement has ever been
     made on a WWOX missense protein whose abundance was restored."* **More of a protein whose
     function has never been measured is not a therapy.**
4. ⚠️ And one geometric route this file opened rather than closed: **Asn232 is 5.82 Å from the
   cofactor-cleft axis, two residues from the helix a proline at 230 must distort.** A
   packing-to-active-site propagation is **geometrically available and completely untested**, and it
   would mean a restabilised `Q230P` could be abundant and still inert — the `P282A` outcome by a
   different road. `IPOTESI`, weak.

5. ⭐ **Why the residual uncertainty is expensive here specifically.** `Q230P` is the **most recurrent
   WWOX allele of any class — 8 patients across 6 families** (§0.3), so a non-allele-specific boost
   axis evaluated against `Q230P` is being evaluated against the **largest single allele-specific
   constituency in the disease**. That does not change the sign; it changes the cost of getting the
   sign wrong in either direction — a wrongly-red sign forecloses the route with the biggest
   constituency, and a wrongly-green one exposes it. **It is an argument for §10 item 3 (one blot,
   two lanes), not for resolving the sign on prediction.**

🔴 **Nothing in this section is medical advice, and no therapeutic recommendation follows from it.**
The sign of a therapeutic axis is an epistemic bookkeeping statement about this repository's evidence,
not a clinical statement about any person. **No prognosis attaches to a genotype class, and this file
makes none.**

---

## 10 · What I could not establish, and the cheapest thing that would move it

| # | open fact | why it did not resolve | cheapest move, and its cost |
|---|---|---|---|
| **1** ⭐ | **Whether WWOX residue 230 is within contact distance of a partner subunit in a real WWOX dimer** | No AlphaFold-Multimer / dimer model of WWOX exists in this repository; `files.rcsb.org` is off the allowlist; no MD engine to dock with | 🟢 **Run AlphaFold-Multimer (or any dimer predictor) on WWOX ×2 and measure ΔSASA at residue 230.** **No wet work, no spend.** This is the single falsifier of §9's sign that is achievable computationally, and it would also finally place the exposed W335/W336 patch. **It is the highest-value item in this node and it is cheap** |
| **2** ⭐ | **Whether WWOX homodimerises through its SDR at all** — the source of the repository's own premise | The premise is quoted forward through three analysis files with no citation; my query census returns nothing (§5.5); `[All Fields]` cannot see Methods | 🟢 **A record move, not an experiment: trace `discovery_ledger_current.md:852` to its source and label it.** If the source is a review or a fold inference, the interface fork was never a 50/50 and several downstream files should say so. **Minutes of work** |
| **3** | **Whether `Q230P` protein is in the soluble or insoluble fraction** | Never done, for any WWOX allele | 🔴 **A solubility split (soluble/pellet Western) on the existing `Q230P` patient fibroblasts.** One blot, two lanes, reagents that already exist somewhere. **This single lane decides §9's sign more definitively than any prediction can**, and the un-named third cause of Johannsen's non-detection is exactly what it reads |
| **4** | Whether the helix resolves the Pro by fraying (Branch A) or kinking (Branch B) | 🔴 **MD route BLOCKED — `md_status.py` 0/12, no `openmm`, no gromacs. Recorded once, not retried** | Install an MD engine, then run the **pre-registered** WT-vs-`Q230P` protocol already on disk (`md_q230p_protocol.md`) against the **fast** observable it specifies. ⚠️ That protocol's own self-correction warns the slow observable yields an expensive `INCONCLUSIVE` |
| **5** | Residue-level conservation at position 230 across orthologues and the SDR family | 🔴 UniProt / EBI / RCSB all `connect_rejected`; no local MSA; and PMID 37285720 shows SDR **interface** residues are not conserved even between orthologues, so the alignment-transfer route was unsound anyway | Fetch ~20 WWOX orthologue sequences through an allowlisted route and compute a per-site score. ⚠️ **Note this can only strengthen or weaken §2 row 5 (the network); it cannot touch §5, which rests on geometry** |
| **6** ⭐ | Johannsen 2018's `n`, controls, densitometry **and the qRT-PCR amplicon position** | 🔴 PMID 29808465 is recorded **`unrecoverable_by_these_routes`**, `pmc_id: null`, closed at Springer; publisher egress blocked. **Nobody here has read its body** | **Author contact, the WWOX Foundation, or ILL.** 🔴 **Both of the only two experimental data about the most recurrent WWOX allele in the disease — 8 patients, 6 families — are currently `abstract-depth`.** For the highest-constituency allele in the gene, one PDF is the cheapest evidence purchase available anywhere in this node |
| **7** | The body of PMID 21476439 — the only WWOX enzymology paper ever published | No PMCID; three independent checks confirm no PMC deposit | Author contact (Bednarek's group is still active) or ILL. **It is the only source that could say whether WWOX binds NAD(P) at all**, which §4.2's whole cleft geometry currently assumes from the fold |
| **8** | Whether the exposed αG face (1495 Å² SASA, W335/W336 exposed, pLDDT 35–53) is a real interface or a prediction failure | Cannot be told apart from a monomer model | Resolved for free by item 1 |

### 10.1 Routes recorded as blocked — once each, not retried

| route | state | evidence |
|---|---|---|
| Molecular dynamics | 🔴 **BLOCKED** | `md_status.py` → *"0/12 complete"*; no `openmm`, no gromacs |
| RCSB / PDB structure download | 🔴 **BLOCKED** | `files.rcsb.org:443 — connect_rejected` |
| UniProt / EBI sequence retrieval | 🔴 **BLOCKED** | `rest.uniprot.org:443`, `www.ebi.ac.uk:443 — connect_rejected` |
| general web egress | 🔴 **allowlist confirmed** | `example.com:443 — connect_rejected` (the control behaves as the brief predicts) |
| PMID 29808465 full text | 🔴 no PMCID exists | prior-session checks, three independent methods |
| PMID 21476439 full text | 🔴 no PMCID exists | prior-session checks, three independent methods |

🔴 **A tool block is not a scientific stop, and none of the above stopped a scientific question:**
§§1–8 were answered with numpy on coordinates the repository already holds, plus PubMed.

---

## 11 · Reproducibility and declared limits

**Reproducibility.** Every number in §§1–5 comes from direct numpy geometry on
`disease-models/wwox/analysis/data/WWOX_Q9NZC7_AlphaFold.pdb`, plus the repository's own
`disease-models/wwox/analysis/scripts/residue_context.py` for SASA and P-SEA SSE. Conventions:

- **Dihedrals** from atom coordinates; helix window φ ∈ [−100°, −30°], ψ ∈ [−80°, −5°]
- **Burial** = heavy-atom neighbour count within 10 Å of CB (CA for Gly), always reported against the
  chain-wide distribution (min 22 / Q1 104 / med 142 / Q3 183 / max 232), never as an absolute
- **Polar contact** = any N or O within 3.6 Å of Q230 NE2/OE1
- **α-helical H-bond** = O(i−4)···N(i) ≤ 3.5 Å
- **Cofactor-cleft axis** = segment from the mean CA of residues 131–135 to Y293-OH; per-residue
  distance is the minimum over all heavy atoms to that segment
- **Modelled Pro Cδ** placed at 1.473 Å from N230 along the idealised amide-hydrogen direction
  −[û(C229→N230) + û(CA230→N230)]; vdW contact minima C···O 3.22, C···N 3.07, C···C 3.22 Å
- **ThermoMPNN** read at `position = 229` (**0-based**) with `wildtype = Q` verified before use

**Limits, stated plainly and not minimised.**

1. 🔴 **This is a predicted structure.** Backbone confidence at 230 is excellent (pLDDT 98.50) and
   §§3.1–3.2 rest on backbone geometry only, which is the firmest class of number here.
   **§1.3c's side-chain contact inventory is the weakest**, because side-chain rotamers are the least
   reliable part of any predicted model at any pLDDT — it is a *hypothesis about contacts*, not a
   measurement of them, and it is the part most likely to be wrong.
2. 🔴 **`PMID 35716775`'s warning applies and was respected**: *"AlphaFold2 cannot be used to assess
   effects of point mutations, since it relates to point mutations as 'local noise'."* No claim here
   is built from a predictor's variant score. §§3 and 5 are built from **coordinates of the wild-type
   model** plus **idealised geometry of the substituting residue**, which is a different operation.
   ⚠️ It does **not** exempt this file from the monomer limitation (§5.6).
3. 🔴 **Monomer.** Every burial and SASA number is a **lower bound on burial** and every contact list
   is an **incomplete inventory**, exactly as the Orchestrator recorded against its own Gln353/Gln354
   analysis. **§5.6 explains the one place this bias cannot operate** — a residue at exactly 0.0 Å²
   cannot be lifted to interface status by correcting a monomer bias in the direction of *more*
   burial — and that is the whole load-bearing structure of this file's interface conclusion.
4. 🔴 **No prediction was promoted to `MEASURED` anywhere.** ΔΔG, LLR, pLDDT, SASA, burial, dihedrals,
   SSE assignments, motif assignments and all distances computed on a predicted model **are
   predictions**. The only experimental facts about `Q230P` in existence remain: **normal transcript
   by qRT-PCR, and protein not detected on one Western of homozygous patient fibroblasts** — and
   🔴 **per §0.4 both reach this repository only at `abstract-depth`, from a body nobody here has
   read.** They are therefore `PREMISE: UNREAD_PRIMARY`, not clean measurements, and every line above
   that touches them says so.
5. **No molecular dynamics. No figure panel inspected. No full-text read performed in this act** —
   PMIDs 17258342, 37285720, 11007791, 11306088, 39894307, 22534828, 17567906, 30370248 and 38161429
   were read at **`abstract-depth` via PubMed metadata this session**, and nothing was promoted from
   them beyond the sentences quoted verbatim above. **No `FULLTEXT_READ_RECEIPT` is claimed for any
   of them, and none is owed, because no full-text route was taken.**
6. **Attribution.** Bibliographic records, abstracts and DOIs in §§4–7 were obtained from **PubMed**;
   every referenced article carries its DOI link at the point of use.
7. **Other actors' work is labelled as theirs.** `wwox_missense_stability_census_20260922.md`
   (Scientist S), `gln353_gln354del_structural_adjudication_20260922.md` (Orchestrator),
   `wwox_sdr_function_per_molecule_census_20260921.md` (Scientist A),
   `l239r_intraallelic_comparator_20260921.md`, `lectin_readout_domain_dependence_20260921.md`
   (Scientist A, FT-143), `mave_portability_to_wwox_20260921.md` (FT-141, **one paper `[PREPRINT]`**),
   `missense_rescue_methodology_census_20260921.md` (Orchestrator, **abstract-built**) and
   `wwox_activity_sensor_census_20260921.md` and
   `missense_splice_reclassification_risk_20260921.md` (**imported at commit `b30dfbf`; the source of
   all four bounds in §0**) are **research-layer, self-marked non-canonical, written by other
   actors**. Where relied on above they are cited as **that actor's attestation, not as my reading**,
   and nothing from the abstract-built files is promoted here.
8. 🔴 **Self-contamination avoided.** No count in this file was verified by grepping a tree containing
   this file. Repository counts were taken with `git grep … HEAD`.
9. **No registry, queue, ledger, receipt, canonical file or state manifest was written. No
   `BATCH_COMMIT`. No git command was run.** One output file was created: this one.

---

## 12 · Summary table — the seven possibilities, one line each

| # | possibility | verdict | decisive measurement |
|---|---|---|---|
| 1 | SDR core packing | 🟢 **YES** | relSASA **0.000**, burial 83.8 %ile, 22 contacts ≤5 Å |
| 2 | oligomer / dimer interface | 🟢 **NO** | relSASA **0.000**; ≥12.5 Å to nearest exposed αE/αF residue; 19.2 Å to αG; 226–240 has no exposed face |
| 3 | cofactor environment | 🟢 **NO** | **12.60 Å** from cleft axis (rank 114/414); **10.01 Å** from `TGANSGIG` (T130–G137) |
| 4 | substrate-binding region | 🟢 **NO** | S281 6.79 Å · Y293 9.37 Å · K297 9.68 Å; side chain **141° away** from Y293-OH |
| 5 | conserved H-bond network | 🟡 **network YES, conserved-glutamine NO** | 5 polar contacts, 3 long-range (Δseq −44 to −46); but ESM2 prefers **G/A over Q** at 230 |
| 6 | secondary-structure stabilisation | 🟢 **YES** | N230–H···O226 **3.03 Å, 9° deviation**; Pro Cδ lands **1.60 Å** from that same oxygen (**1.44 Å overlap**) |
| 7 | solvent-exposed interaction surface | 🟢 **NO** | SASA **0.0 Å²** |
| — | *(confound, not one of the seven)* cryptic splicing | 🟢 **EXCLUDED** | `c.689A>C`, exon 7, **66–84 nt from any junction** (§0.1, another actor's attestation) — removes a competing explanation, supplies no evidence about folding |

### 12.1 The three numbers to carry forward

| | |
|---|---|
| 🟢 **relSASA 0.000** | why `Gln230` cannot be a dimer-interface residue, whatever the interface turns out to be — and therefore why the aggregation branch of the therapeutic fork is not supported |
| 🔴 **1.44 Å** | the modelled Pro230 Cδ / Glu226 carbonyl overlap — why the substitution is not marginal, measured rather than asserted from a propensity table |
| 🔴 **8 patients / 6 families** | the constituency this verdict carries, resting on **one unread abstract** |

---

**END OF FILE — `q230p_structural_mechanism_20260922.md`. This is a complete run: sections 0–12 all
present — imported bounds and the abstract-level cap in §0, own measurements in §1, the seven
possibilities in §2, the proline question in §3, cofactor/catalytic geometry in §4, the dimer
interface in §5, evolution in §6, transferred evidence in §7, verdict and falsifiers in §8,
therapeutic sign in §9, open facts in §10, limits in §11, summary in §12.**
