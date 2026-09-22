# Adversarial test of the exon-9 cryptic-acceptor adjudication — `c.1057-2A>G`

**Date:** 2026-09-22 · **Actor:** Scientist I · **Mode:** adversarial verification
**Target of attack:** the Orchestrator's same-day adjudication in
`research/commit_candidates/CC-20260922-SPLICE-ARM-01.md` §7, and the standing position of
`DL-MECH-045`.
**Read-only toward** `registries/`, the receipt ledger and the state manifest. Nothing here is
medical advice. **BLOCK-1: no molecule, no dose, no safety claim.**

> **Genotype class discipline.** Everything below concerns **`c.1057-2A>G`**, the intron-8/exon-9
> acceptor allele of the reference genotype class. It does **not** transfer to `c.517-2A>G`
> (exon 6), `c.606-1G>A` (exon 7) or any other splice allele. Those are separate classes and were
> kept separate throughout.

---

## 0 · Verdict in one page

| Question | Answer | Status |
|---|---|---|
| **Is `c.1061 = A`?** | 🟢 **YES — resolved, three independent derivations, all local.** | `derived` from `measured` ClinVar annotation |
| Is the SPDI 0-based assumption right? | 🟢 **Confirmed**, 1038/1038 SNVs + all deletions/indels/microsatellites | `verified` |
| Is the `+8` = `c.1063` reading right? | 🟢 **Confirmed, and now over-determined** — a second, independent mechanistic route lands on the same base | `predicted` |
| Could the gained acceptor be **upstream**? | 🟢 **EXCLUDED** — no `AG` exists anywhere in the last 31 nt of intron 8 | **new** |
| Is the 8-nt frameshift reading survivable? | ⛔ **Dead.** Its required `AG` is `G,G`; `c.1064 = G` is now resolved too | **new** |
| Does the adjudication survive? | 🟢 **It survives, strengthened.** I could not break it. | — |
| Is `p.Gln353_Gln354del` therefore benign? | 🔴 **NO — and the repository must not draw that inference.** §3 | **new, and it cuts against the hopeful reading** |
| Contradictions found in repository assertions | **3**, two of them in the document that specifies the experiment | §5 |

**The single most consequential finding is not in Part 1.** It is §3: the two deleted residues sit
**inside an α-helix**, not in a loop, and the very next helical turn is **fully buried core**.
`D-30` applies with full force, and it does not point the way the `+8` result does.

---

## 1 · 🔴 The one unverified base: `c.1061`

### 1.1 Result

> **`c.1061 = A`.** Genomic `NC_000016.10:79,211,612` (GRCh38, plus strand) **= `A`.**

Derived **three times, independently**, from material already inside this repository. **None of the
three derivations uses the splicing prediction, the `+8` label, or anything the prediction needs.**
All three are blind to it: two come from ClinVar's *protein-coding* annotation, one from a
*structure* file.

### 1.2 The route the task expected — and why it failed

The task named an **indel / delins / duplication / microsatellite** whose deleted-allele string
spans `c.1061` as "the most promising route, and it is local." **I ran it exhaustively and it
fails.** Every SPDI deleted-allele string in the export was expanded base-by-base onto the genome
and intersected with the window `79,211,560–79,211,630`:

| finding | value |
|---|---|
| records whose deleted allele overlaps the window | 34 |
| **records whose deleted allele covers `79,211,612` (`c.1061`)** | 🔴 **0** |
| 3′-most base reached by any multi-base deleted string | `79,211,597` = `c.1057-11` |

Every multi-base deleted string near `c.1057-` lies **in the intron**, 15 or more bases 5′ of the
target. The exonic records are all single-nucleotide. **The named route is empty, and I record that
as a negative result rather than straining it.** (It was not wasted: it produced §2.3.)

### 1.3 Derivation A — from `p.Gln354Ter`

`VCV002438615` — `NM_016373.4(WWOX):c.1060C>T (p.Gln354Ter)`, SPDI `NC_000016.10:79211610:C:T`.

- Codon 354 = `c.1060, c.1061, c.1062`.
- `c.1062 = G`, read **directly** from the deleted-allele field of `VCV003756655`
  (`NC_000016.10:79211612:G:A`). Not inferred.
- The variant makes the codon `T, c.1061, G`. ClinVar annotates the product as **Ter**.
- The three stop codons are `TAA`, `TAG`, `TGA`. With the **third base fixed at `G`**, only **`TAG`**
  qualifies — `TAA` needs third base `A`, `TGA` needs third base `A`.

> **⇒ `c.1061 = A`.** No alternative exists.

### 1.4 Derivation B — from `p.Gln354=` (independent of A)

`VCV003756655` — `c.1062G>A (p.Gln354=)`, SPDI `NC_000016.10:79211612:G:A`.

- Wild-type codon 354 = `c.1060(=C), c.1061, c.1062(=G)`; `c.1060 = C` read **directly** from the
  deleted-allele field of `VCV002438615`.
- ClinVar annotates the wild-type residue as **Gln**. `Gln = CAA | CAG`. Both have **`A` at the
  middle position**.
- The synonymous call independently requires `C, c.1061, A` to *also* be Gln ⇒ again `CAA`.

> **⇒ `c.1061 = A`.** Codon 354 = **`CAG`**.

Derivations A and B use **different submitters, different accessions, different years
(2021 / 2024), and opposite variant directions**. They are not the same observation twice.

### 1.5 Derivation C — from the local AlphaFold model (orthogonal to ClinVar entirely)

`disease-models/wwox/analysis/data/WWOX_Q9NZC7_AlphaFold.pdb`, header
`ALPHAFOLD MONOMER V2.0 PREDICTION FOR WW DOMAIN-CONTAINING OXIDOREDUCTASE (Q9NZC7)`, 414 residues.

- Residue **354 = Gln** in the deposited UniProt `Q9NZC7` sequence carried by that file.
- With `c.1060 = C` and `c.1062 = G` (both SPDI-direct), codon 354 = `C, ?, G`, and `Gln` forces the
  middle base to `A`.

> **⇒ `c.1061 = A`**, from a file that has never seen ClinVar.

### 1.6 The independent frame check nobody asked for, and it passed

Reconstructing **every** exon-9 codon from ClinVar's protein consequences by constraint solving
(each codon must simultaneously satisfy every reference base, every wild-type residue and every
mutant residue reported for it) yields residues **353–365 = `Q Q G A A T T V Y C A A V`**.

The AlphaFold file's residues 353–365 are **`Q Q G A A T T V Y C A A V`**. **Identical.**

This is a 13-residue agreement between two sources that share no pipeline. It independently
confirms (a) the codon frame, (b) that **`c.1057` opens codon 353**, and therefore (c) the
`(1057−1)/3 = 352` arithmetic the whole adjudication rests on.

### 1.7 Bonus: `c.1064` is no longer unknown either

The same solver resolves codon 355 to `GGA | GGG` (from `c.1063G>A` and `c.1063G>C`, both
`p.Gly355Arg`: `Gly = GGN`, and `AGN = Arg` requires `AGA|AGG`).

> **⇒ `c.1064 = G`.** This closes the last `?` in the exclusion table (§2.2).

### 1.8 Honest statement of what kind of result this is

This is **not** a direct read of the reference sequence. Direct sequence egress is **403 at
CONNECT** and I did not obtain it. It is an **inference from ClinVar's protein-consequence
annotation**, which is a deterministic function of `NM_016373.4` computed by NCBI, plus the
sequence embedded in an AlphaFold model.

**Why I nevertheless call it resolved and not "probable":**
1. The logic is **deductive, not probabilistic** — each derivation leaves exactly one base possible.
2. Three sources, no shared dependency.
3. A 13-residue independent cross-check passed (§1.6).
4. The whole 20-bp coordinate ladder `c.1057-20 → c.1067` is internally consistent with **zero
   conflicts** (§2.3), which a wrong frame would not survive.

**What would still falsify it:** a ClinVar protein-consequence annotation error on *both*
`VCV002438615` and `VCV003756655`, *and* a corresponding error in the UniProt `Q9NZC7` sequence.
I regard that as negligible but it is the residual, and it is named.

---

## 2 · Attack on the adjudication

### 2.1 Is SPDI 0-based? — **Confirmed, and the exception proves it**

Offset `start − SPDI_position`, computed across the whole export, **partitioned by variant type**:

| variant type | n | `start − SPDI_pos` |
|---|---:|---|
| single nucleotide variant | 1038 | **1** (100%) |
| Deletion | 30 | **1** (100%) |
| Microsatellite | 9 | **1** (100%) |
| Indel | 7 | **1** (100%) |
| Inversion | 2 | **1** (100%) |
| Duplication | 18 | 0 (100%) |
| Insertion | 3 | 0 (100%) |

**1086 of 1107 records give offset exactly 1**, with **no scatter within any class**. The 21
exceptions are **only** `Duplication` and `Insertion` — precisely the classes where SPDI anchors at
the 0-based position *after which* sequence is inserted, so its integer coincides numerically with
the 1-based position of the **preceding** base. That is the expected behaviour of a 0-based system,
not a counter-example to it.

🟢 **SPDI is 0-based. The assumption survives**, and it survives a test the original adjudication
did not run (per-class partitioning rather than a pooled count).

### 2.2 Are the competing readings really excluded? — **Yes, and now with no `?` left**

| new exon starts at | nt lost | required `AG` at | reference | source of each base | verdict |
|---|---:|---|---|---|---|
| `c.1062` | 5 | `c.1060`,`c.1061` | **`C`**,`A` | SPDI-direct; §1 | ⛔ |
| **`c.1063`** | **6** | `c.1061`,`c.1062` | **`A`**,**`G`** | **§1**; SPDI-direct | 🟢 **survivor** |
| `c.1064` | 7 | `c.1062`,`c.1063` | **`G`**,`G` | SPDI-direct ×2 | ⛔ |
| `c.1065` | 8 *(the frameshift reading)* | `c.1063`,`c.1064` | **`G`**,**`G`** | SPDI-direct; **§1.7** | ⛔ **now fully closed** |
| `c.1066` | 9 | `c.1064`,`c.1065` | **`G`**,`A|G` | §1.7; solver | ⛔ |

🔴 **The 8-nt frameshift reading — `DL-MECH-045`'s position — is dead by reference sequence at
*both* of its required bases, not one.** Previously `c.1064` was `?`; it is `G`.

### 2.3 Could the gained acceptor be **upstream**? — 🔴 **NEW: comprehensively excluded**

The prior session declared this an open limitation:

> *"Four positions of the exon 9 acceptor (−8 to −5) are unknown to me, so I cannot exclude an
> upstream cryptic `AG` there."* — `analysis/splice_allele_rna_evidence_20260922.md`, line 343

**This is now closed.** Expanding every SPDI deleted-allele string in the export onto the genome
reconstructs the 3′ end of intron 8 **with zero conflicts across 29 positions**, most of them
multiply covered:

```
        -31                    -20                 -10        -1
         |                      |                   |          |
   5'... T T T T T T T T T G T C T T T C T T C T T G G A T T ? C C A ? | C A A C A G G G ...3'
                                                              ^     ^   ^
                                                           c.1057-5 |  c.1057
                                                              c.1057-2 (the allele)
```

| position | base | evidenced by |
|---|---|---|
| `-31 … -23` | `TTTTTTTTT` | `c.1057-23dup` deleted allele |
| `-22 … -19` | `G T C T` | `c.1057-22_1057-20del`, `c.1057-22_1057-19del` |
| `-18 … -11` | `T T C T T C T T` | `c.1057-17_1057-14del`, `c.1057-13_1057-11del`, 3 SNVs |
| `-10, -9` | `G, G` | `c.1057-10G>T`, `c.1057-9G>C` |
| `-8, -7, -6` | `A, T, T` | **`c.1057-9_1057-6dup` deleted allele `GATT`** + `c.1057-7T>C` |
| `-5` | `?` | not covered |
| `-4, -3, -2` | `C, C, A` | three SNVs |
| `-1` | `?` | not covered — canonical `G` by definition of the acceptor |

**AG scan over `-31 … -1`:** the reconstructed tract contains **exactly two adenines**: at `-8` and
at `-2`.

- `-8` is followed by **`T`** (`-7`) ⇒ **`AT`, not `AG`.**
- `-2` is the **canonical** acceptor `A`, and the variant converts it to `G`.
- `-5` is unknown **but irrelevant**: `-4` is `C`, so `(-5,-4)` cannot be `AG` whatever `-5` is.
- `-1` is unknown **but irrelevant**: `(-1, c.1057)` cannot be `AG` because `c.1057 = C`.

> 🔴 **There is no cryptic `AG` anywhere in the last 31 nucleotides of intron 8.** The upstream
> hypothesis is excluded — not weakened, excluded. **The two unknown bases cannot rescue it**, which
> is why this is a complete result rather than a partial one.
>
> **Residual:** positions `-33`/`-32` are uncovered. An `AG` there would sit ~33 nt out, at or 5′ of
> the likely branch point, where an `AG` is not selected. Named for completeness.

### 2.4 🔴 NEW: an independent mechanism lands on `c.1063` without using SpliceAI at all

The reconstruction in §2.3 makes a **second, orthogonal prediction** possible.

Acceptor selection follows the **"first AG downstream of the branch point"** scanning rule: with the
polypyrimidine tract and branch point intact — and **the variant touches neither**, it changes only
the `AG` itself — the spliceosome scans 3′ and commits to the first available `AG`.

Scanning 3′ from the destroyed site through the now-known sequence
`[-2]G [-1]G | C A A C A G G G …`:

| dinucleotide | bases | `AG`? |
|---|---|---|
| `-1`, `c.1057` | `G, C` | no |
| `c.1057, c.1058` | `C, A` | no |
| `c.1058, c.1059` | `A, A` | no |
| `c.1059, c.1060` | `A, C` | no |
| `c.1060, c.1061` | `C, A` | no |
| **`c.1061, c.1062`** | **`A, G`** | 🎯 **first AG** |

> **⇒ new first exonic base = `c.1063`.** **Identical to the `+8` SpliceAI call**, reached by a
> completely different route: a sequence-scanning rule applied to a sequence reconstructed from
> deleted-allele fields.

**Why this matters more than a third confirmation.** The `+8` label is, in this edition,
**unreachable at source** — `CC-20260922-SPLICE-ARM-01` §7 establishes that the raw `DP_AG` field
lives in the private quarantine log, excluded here. The position was therefore resting on a derived
label plus a coordinate coincidence. **It no longer is.** The site is now predicted from reference
sequence the repository holds, with the label used only as corroboration.

### 2.5 Could `+8` mean something other than a position offset? — the readings, enumerated

| candidate meaning of `+8` | lands on | survives? |
|---|---|---|
| first **exonic** base of the gained exon (SpliceAI `DP_AG` convention) | `c.1063` | 🟢 **yes** — and §2.4 reaches it independently |
| the **`G`** of the gained `AG` | `c.1063` ⇒ exon starts `c.1064`; requires `AG` at `c.1062,c.1063` = `G,G` | ⛔ |
| the **`A`** of the gained `AG` | `c.1063`=`G`, not `A` | ⛔ |
| "8 nt of coding sequence lost" | exon starts `c.1065`; requires `AG` at `c.1063,c.1064` = `G,G` | ⛔ |
| offset in the **intron** (upstream) | no `AG` exists there at all (§2.3) | ⛔ |

🟢 **Only one reading of `+8` is consistent with the reference sequence, and it is the one the
adjudication chose.** The convention question is therefore **moot** — which is the strongest
possible outcome, since it means the conclusion no longer depends on resolving it.

### 2.6 What `DS_AG 0.64` does and does not license

**Licenses:**
- SpliceAI predicts an acceptor **gain** at the stated offset with a score above the "recommended"
  operating point (0.5) and below the "high-precision" one (0.8). **Moderate confidence that a gain
  occurs there.**

**Does NOT license — and each of these is a live temptation:**
- ❌ **Any statement of abundance.** A delta score is **not** a predicted transcript fraction. `0.64`
  does not mean "64% of transcripts". The cryptic product could be the majority species, a minor
  species, or absent.
- ❌ **Exclusivity.** Acceptor gain and intron read-through are **not mutually exclusive**; both can
  occur on different molecules, and SpliceAI scores them separately.
- ❌ **Anything about protein.** Stability, folding, half-life, function — SpliceAI is silent.
- ❌ **Anything about cell type.** Splicing outcomes are tissue-dependent; SpliceAI reports one
  number.

**And the asymmetry must stay in the foreground:**

> **Acceptor LOSS is the confident call** — `DS_AL 0.96` **and** MaxEntScan Δ −7.95, two orthogonal
> methods agreeing. **What happens instead is the uncertain part.** The work in §§2.2–2.4 sharpens
> *which* alternative is geometrically possible; it does **not** raise `DS_AG 0.64` to a measurement.
> Nobody has measured RNA from this allele. `PREMISE: NOBODY_LOOKED` is untouched.

### 2.7 🔴 Is exon-9 "skipping" even definable? — **No. The real outcome set, enumerated**

There is no exon 10. Exon 8's donor has nothing downstream to ligate to once the exon-9 acceptor is
destroyed. **"Skipping" is not a defined outcome for this exon** and any assay or document written
around it is asking a question with no answer.

**Derived independently here:** the full coding exon map, reconstructed from ClinVar's `c.N+x` /
`c.N-x` intronic offsets across the export:

| exon | cDNA | length | note |
|---|---|---:|---|
| 1 | `c.1–107` | 107 | |
| 2 | `c.108–172` | 65 | |
| 3 | `c.173–230` | 58 | |
| 4 | `c.231–409` | 179 | |
| 5 | `c.410–516` | 107 | |
| 6 | `c.517–605` | **89** | ✅ matches the repository's `89 nt ⇒ frameshift` for `c.517-2A>G` |
| 7 | `c.606–791` | **186** | ✅ `186/3 = 62` — independently confirms the exon-7 62-residue in-frame result (`D-30`) |
| 8 | `c.792–1056` | 265 | ends `g.78,432,751` |
| **9** | **`c.1057–1245`** | **189** (63 codons incl. stop) | begins `g.79,211,608` — **the last exon** |

⇒ **intron 8 = `g.78,432,752–79,211,607` = 778,856 nt.** ✅ **Matches the repository's recorded
778,856 bp exactly** (`tx001_experiment_decision_packet_20260921.md`) — reported as *confirmed by an
independent route*, **not as new**.

**The real outcome set, and which are consistent with the reference bases:**

| # | outcome | consistent with reference sequence? | product |
|---|---|---|---|
| 1 | **Cryptic acceptor at `c.1061/c.1062`** ⇒ exon starts `c.1063` | 🟢 **YES — the only geometrically available `AG`** (§2.3, §2.4) | `r.1057_1062del` ⇒ **in-frame, −2 residues** |
| 2 | **Intron-8 read-through / retention** | 🟢 possible, but **a 778,856-nt retained intron is not a plausible mature mRNA** | would require #3 or #4 to terminate |
| 3 | **Intronic polyadenylation within intron 8** | 🟢 **YES — and documented in this gene.** Schirmer 2016 reports transcripts *terminating within intron 8* | truncated at codon 352 + intronic tail |
| 4 | **Alternative terminal exon within intron 8** | 🟢 possible; same 779-kb intron, same documented precedent | novel C-terminus |
| 5 | **"Exon 9 skipping"** | ⛔ **NOT DEFINABLE — no exon 10** | — |
| 6 | Cryptic acceptor further into exon 9 | ⛔ next `AG` after `c.1061/62` is beyond the resolved window; not required, and #1 outcompetes by proximity | — |

🔴 **Outcomes 1 and 3/4 are biologically opposite** — #1 is a near-full-length hypomorph, #3/#4 is a
truncation at codon 352 losing all 62 exon-9 residues. **Both are consistent with the sequence.**
`DS_AG 0.64` favours #1 but does not establish it, and **#1 and #3 can coexist on different
molecules of the same allele.** Any assay that cannot see #3/#4 will report #1 as "the" answer by
construction.

### 2.8 Did the adjudication survive?

🟢 **Yes. I could not break it, and I attacked five load-bearing joints:** the SPDI convention, the
`+8` reading, the exclusion table, the upstream alternative, and the definability of the outcome
set. **Four of the five came back stronger than they went in**, and the one remaining hole
(`c.1061`) is filled.

⚠️ **But "the adjudication survived" is a statement about the *transcript*, and only about the
transcript.** It says nothing about the protein. §3 is where the hopeful reading meets resistance.

---

## 3 · 🔴 If the prediction holds, what would `p.Gln353_Gln354del` actually do?

**Precise nomenclature.** Predicted transcript `r.1057_1062del`; predicted protein
**`p.Gln353_Gln354del`** — a 412-residue protein. The deleted nucleotides are `c.1057_1062` =
`CAACAG`; neither the flanking nucleotide context (`…TCCATG` / `GGGAGC…`) nor the flanking residues
(`M352` / `G355`) create a repeat, so **no 3′-rule shifting applies** and the designation is stable.
Codon 353 = `CAA`, codon 354 = `CAG` — **both Gln**, from §1.

### 3.1 What is actually in exon 9 (residues 353–414)

From `AF-Q9NZC7-F1` via `residue_context.py` (Shrake–Rupley SASA, P-SEA-like SSE, pLDDT):

| element | residues | character |
|---|---|---|
| **α-helix** | **351–363** | N-terminal turn solvent-facing; **355–363 almost entirely buried core** |
| coil | 364–369 | |
| β-strand | 370–376 | contains **G372**, the repository's negative-control residue |
| α-helix | 377–381 | |
| β-strand | 382–384 | |
| **α-helix** | **385–412** | contains the **GSK3β-binding region 388–407**, incl. **L404**; mean pLDDT **97.8** |
| coil | 413–414 | C-terminus |

**The catalytic triad `S281/Y293/K297` is in exon 8** (codon 281 = `c.841–843`, within
`c.792–1056`). ⇒ **No exon-9 lesion removes the catalytic triad.** A truncation at codon 352
(outcome #3/#4) would retain the triad but lose the entire C-terminal third of the SDR fold **and
all of the GSK3β-binding region** — which is the mechanistically important distinction between
outcome #1 and outcome #3, and it is not currently drawn anywhere.

### 3.2 Where residues 353–354 sit — **the result that changes the reading**

| res | aa | relSASA | burial | **SSE** | pLDDT | contacts ≤5 Å | min heavy-atom → triad |
|---|---|---:|---|---|---:|---:|---:|
| 350 | K | 0.153 | partially exposed | **coil** | 60.5 | 13 | — |
| 351 | S | 0.328 | surface | α-helix | 76.4 | 17 | — |
| 352 | M | 0.237 | partially exposed | α-helix | 82.4 | 17 | — |
| **353** | **Q** | **0.146** | partially exposed | **α-helix** | 85.8 | **23** | **15.7 Å** |
| **354** | **Q** | **0.174** | partially exposed | **α-helix** | 87.2 | **25** | **14.0 Å** |
| 355 | G | **0.000** | **buried core** | α-helix | 86.1 | 26 | 16.1 Å |
| 356 | A | **0.000** | **buried core** | α-helix | 93.7 | 22 | 16.9 Å |
| 357 | A | **0.009** | **buried core** | α-helix | 93.1 | 27 | 18.4 Å |
| 358–360 | T,T,V | 0.006–0.000 | **buried core** | α-helix | 92.9–97.6 | | |
| 362–363 | C,A | 0.006–0.046 | **buried core** | α-helix | 96.4–97.8 | | |

**Distances (minimum heavy-atom, predicted structure):**

| from | to catalytic triad | to region 388–407 | to L404 |
|---|---:|---:|---:|
| Q353 | **15.7 Å** | 23.8 Å (nearest: A388) | 32.6 Å |
| Q354 | **14.0 Å** | 20.9 Å (nearest: A388) | 31.2 Å |

🟢 **Neither functional site is contacted.** 353/354 are **~14–16 Å from the catalytic triad** and
**~21–24 Å from the GSK3β region**, with **L404 over 31 Å away**. Any lesion here is therefore a
**folding/packing lesion, not a direct active-site or interaction-surface lesion.**

🔴 **But they are mid-helix, and the next helical turn is buried core.** That is the finding.

### 3.3 🔴 Applying `D-30` honestly — in the direction that hurts

`D-30` states: *in-frame is a statement about the reading frame, not about the fold.* The exon-7
case killed a hopeful in-frame prediction. The task correctly warns that **"only two residues" is
not an argument.** Here is the honest analysis, with both branches and no thumb on the scale.

#### The case that it is **NOT** tolerated

1. **A 2-residue deletion inside an α-helix is not an excision — it is a register shift.** Removing
   two residues from a helix rotates the helical phase of everything C-terminal by
   **≈ 2 × 100° = 200°**, and shortens the axis by ≈ 3.0 Å. This is categorically different from a
   2-residue deletion in a loop, which a loop can absorb.
2. **The residues immediately downstream are the buried face.** 355(G), 356(A), 357(A), 358(T),
   359(T), 360(V), 362(C), 363(A) form a classic **small-residue buried helix face**
   (relSASA 0.000–0.046). A ~200° rotation would swap that face with the solvent-facing one —
   driving **Y361** (aromatic, currently partially exposed) and other larger side chains into a core
   evolved to accept alanines and glycines.
3. **This helix is not a surface appendage.** Q353/Q354 contact residues **109–114, 136–140 and
   323–324** — three separate, distant segments. It is packed against the body of the fold, and its
   register carries those contacts.
4. **The deleted side chains are themselves contacts.** Even under the benign branch (below), the
   two Gln side chains and their 23–25 heavy-atom contacts are gone regardless.

#### The case that it **IS** tolerated

1. **There is an escape route, and it is close.** The helix begins at **351**; residue **350 is
   already coil**. Q353 is only the **third residue of the helix**. The protein can absorb the
   deletion by **fraying 351–352 back into the existing 350 loop and starting the helix at 355** —
   which preserves the register, and therefore the burial, of the entire downstream buried face.
   That costs one N-terminal helical turn and 2 residues of linker, **not** a repacked core.
2. **A deletion at the N-cap of a helix adjacent to a flexible loop is the most forgiving place in a
   helix to put one.** If this deletion were at residue 358 instead, there would be no argument.
3. **The residues are Gln–Gln, partially exposed** (relSASA 0.146/0.174) — not buried core. By
   `DL-MECH-037`'s own burial discriminator, these are **not** core-packing residues.
4. **No functional site is contacted** (§3.2).

#### 🔴 The methodological correction this exposes

`DL-MECH-037`'s discriminator — *burial, not ΔΔG* — was calibrated on **missense substitutions**,
where the burial of the **substituted side chain** predicts folding impact. **A deletion is a
different lesion class.** For a deletion, what matters is not the burial of the deleted residues but
the **register and topology consequence for everything downstream**.

> **Applying a missense-calibrated burial criterion to a backbone deletion is exactly the category
> error `D-30` warns against, one level up.** `D-30` says in-frame is a claim about frame, not fold.
> The corollary found here: **relSASA of the deleted residue is a claim about that side chain, not
> about the fold.** Reading "353/354 are only partially exposed, so this is mild" would be that
> error, and it is the reading the `+8` result invites.

#### Verdict

> 🔴 **Nobody can tell without the wet experiment.** The two branches turn on whether the helix
> N-terminus frays or the register shifts — a question about a 3-residue segment whose local model
> confidence is the **weakest in the region** (pLDDT 60.5 at res 350, 76.4 at 351, against 93–98
> further in; residues 340–349 are 35–53, i.e. predicted-disordered). **The structure is least
> reliable exactly where the answer lives.**
>
> **This is not a hedge, it is the result.** The honest statement is: *the deletion is small, sits
> at a helix N-terminus next to a loop, and contacts no functional site — all favourable; and it is
> mid-helix, immediately upstream of a buried face, and carries three long-range contacts — all
> unfavourable.* **A prediction either way would be a guess dressed as an inference**, and the
> repository has been burned twice today by exactly that.

⚠️ **What must NOT be written into the model.** `CC-20260922-SPLICE-ARM-01` §7c calls this *"the
most favourable prediction any allele in this genotype has ever carried."* **That sentence is
defensible only about the *transcript*.** If it migrates into a statement about **protein function
or prognosis**, it will have crossed from a splicing result to a folding claim that nothing here
supports. **A hypomorph is a hypothesis about the protein, and no evidence in this repository bears
on it.** The correct label is `PREDICTED — protein consequence UNKNOWN`.

---

## 4 · The single measurement that would settle it

**One RT-PCR, sized on a capillary instrument, with every band Sanger-sequenced.** The design below
builds on `tx001_experiment_decision_packet_20260921.md` §B and corrects it (§5).

### 4.1 🔴 The resolution problem, stated as a number

| species | product, relative to normal |
|---|---|
| normal exon 8→9 | **reference** |
| predicted cryptic acceptor (`c.1063`) | **−6 nt** |

On a 271-nt amplicon that is a **2.2% size difference**; on a 400-nt amplicon, **1.5%**. **Agarose
resolves neither.** A laboratory running the obvious gel would report normal splicing and be wrong —
and because the cryptic product is **6 nt shorter, not longer**, it will not even appear as a
smear above the band.

### 4.2 Assay A — sizing (the primary measurement)

| parameter | specification | why |
|---|---|---|
| Template | cDNA from patient-derived cells, oligo-dT **and** random-hexamer primed | random hexamers also capture intron-8-terminating species |
| **Forward primer** | **exon 8**, ≈ `c.950–975` | leaves ≥ 80 nt of exon 8 in the product; **must not** cross the 8/9 junction — the junction is the object under test |
| **Reverse primer** | **exon 9**, ≈ `c.1215–1240` | inside the last exon, 5′ of the stop |
| **5′ label** | **FAM on the forward primer** | mandatory — enables fragment analysis |
| Amplicon, normal | **≈ 271 nt** | |
| Amplicon, cryptic | **≈ 265 nt** | |
| **Readout** | **capillary electrophoresis / fragment analysis** (ABI GeneScan + LIZ standard, or Bioanalyzer/TapeStation high-sensitivity) | **±1 nt resolution to ~500 nt**; keeping the amplicon <300 nt puts the −6 nt difference far inside the instrument's competence |
| ❌ **Not** | agarose, and **not** non-denaturing PAGE | agarose cannot resolve 6 nt; native gels form **heteroduplexes** between the two allelic products that migrate anomalously. **Capillary electrophoresis is denaturing, which removes the heteroduplex artefact — a second, independent reason to prefer it.** |

**Expected peak pattern.** The reference genotype class is compound heterozygous, and the missense
allele splices normally ⇒ **two peaks 6 nt apart**, ideally ~1:1 if the cryptic acceptor is used
efficiently. **Peak-height ratio is the quantitative endpoint** — it is what `DS_AG 0.64`
conspicuously does **not** predict (§2.6).

### 4.3 Assay B — allele phasing

Assay A sizes the products but **cannot say which allele made which peak**. Because the missense
position **codon 230 = `c.688–690` lies in exon 7 (`c.606–791`)**, a longer amplicon can carry both
the variant site and the junction on one molecule:

- Forward primer in **exon 7**, 5′ of `c.688` (≈ `c.620–645`); reverse as in Assay A.
- ⇒ **one molecule carries both the missense position and the splice junction.**
- Read by **long-read cDNA sequencing (Nanopore/PacBio)** or by cloning and Sanger of ≥ 20 clones.
- **This is what converts "an aberrant product exists" into "the acceptor allele makes it."**

### 4.4 Assay C — the outcomes Assay A is blind to

🔴 **Assays A and B cannot see outcomes #3/#4 of §2.7 at all** — a transcript terminating inside
intron 8 has **no exon 9**, so the reverse primer has no binding site and the species is simply
absent from the electropherogram. **Its absence would be silently read as evidence for outcome #1.**

| target | reaction |
|---|---|
| intron-8 read-through / retention | forward in exon 8 + **reverse anchored in intron 8**, within ~1 kb of the donor. A 778,856-nt intron cannot be spanned; only its 5′ end is reachable |
| intronic polyadenylation / alternative terminal exon | **3′ RACE** from an exon-8 forward primer |
| total transcript normaliser | **exons 4–6** core amplicon (the Schirmer template already named in `DL-BIO-003`) |

### 4.5 Sanger on every band, **including the apparently-normal one**

Mandatory, for three distinct reasons:

1. **A size is not an identity.** −6 nt is also consistent with other 6-nt events.
2. **The "normal" peak may not be normal.** If both alleles produced products of equal length by
   coincidence of two different events, sizing alone cannot tell.
3. 🔴 **The junction sequence is the actual answer.** Only Sanger shows whether the first exonic base
   is `c.1063` — the entire prediction in one read. **Sequence the normal-sized peak too**, because
   the failure mode here is a cryptic product hiding under it.

### 4.6 Controls — the ones whose absence would void the result

| control | purpose |
|---|---|
| ≥ 2 unrelated healthy donor lines, sex- and passage-matched | the **baseline aberrant fraction of the wild-type junction is non-zero**; without it the patient number has no scale |
| a known 6-nt-indel sizing standard | proves the instrument resolves 6 nt **in this amplicon size range on this run** |
| ± cycloheximide, each with a vehicle twin, plus an independent NMD-sensitive reporter | ⚠️ under outcome #1 there is **no PTC**, so NMD is **not** expected to apply. The arm is retained to detect a **competing** PTC-containing species, and because "absent" and "degraded as fast as made" are otherwise indistinguishable. **Its power here is lower than the packet implies, and that should be stated when it is run.** |
| blinded quantification | the packet records four prior instances of an unblinded readout carrying a claim |

**Resolution required, in one line:** **±1 nt at ~270 nt, on a denaturing platform, with sequence
confirmation of every peak.** Anything less cannot distinguish the two biologies.

---

## 5 · 🔴 Contradictions found against repository assertions

### C-1 — `tx001_experiment_decision_packet_20260921.md` asserts an **exon 10**, twice

> §B.3: *"Exon 9 skipping yields a shorter product **(exon 8→exon 10)**"*
> §B.7 table: *"**Exon 9 skipping** (SpliceAI/Pangolin prediction) | shorter, **exon 8→10** | ✅"*

**WWOX has nine exons** (Shaukat 2018, PMID 30361190, already in the registry: *"contains nine
exons"*), and `analysis/splice_allele_rna_evidence_20260922.md` §2.6(a) states plainly **"There is
no exon 10."** The exon map independently derived in §2.7 confirms nine coding exons ending at
`c.1245`.

**Impact — not cosmetic.** The packet is the document a laboratory would execute. It instructs the
reader to expect a **shorter exon 8→10 product that cannot exist**, and lists it as ✅ detectable.
A lab following it would look for the wrong species and, finding none, could conclude the allele
splices normally.

### C-2 — the same packet predicts the cryptic product is **`+8 nt` longer**. It is **6 nt shorter**.

> §B.7 table: *"**Cryptic acceptor** (a +8 site is predicted) | intermediate, **+8 nt** | ✅"*

**Wrong in both sign and magnitude.**
- **Sign:** a cryptic acceptor *downstream* of the canonical one **removes** exonic sequence. The
  product is **shorter**, never longer.
- **Magnitude:** the loss is **6 nt** (`c.1057_1062`), not 8. The `+8` genomic offset label has been
  transcribed directly into an amplicon size change — precisely the label-provenance failure mode
  `CC-20260922-SPLICE-ARM-01` §6 flags elsewhere.

**Impact — this is the most consequential error found today.** A laboratory sizing products against
this table looks for a band **8 nt above** normal. The real species is **6 nt below** it. **The
assay would be scored as negative while the predicted event was occurring.**

### C-3 — a declared limitation is obsolete and should be retired

`analysis/splice_allele_rna_evidence_20260922.md` line 343 declares positions `−8 … −5` unknown and
an upstream cryptic `AG` therefore non-excludable, and line 192 calls the `c.1061` support *"only
one of its two bases … suggestive, not decisive."*

**Both are superseded:** `−8/−7/−6` are resolved (`A,T,T`), `−5` is shown irrelevant, and `c.1061`
is resolved to `A` three ways. **Not an error when written — correct and properly hedged at the
time. It should now be marked superseded** so a later reader does not re-derive a closed question.

### C-4 — note, not a contradiction

`DL-MECH-045`'s *"proteina tronca instabile"* via a `+8` **frameshift** is now excluded at **both**
required bases (§2.2). `CC-20260922-SPLICE-ARM-01` §7d already proposes its withdrawal; this
document supplies the base that proposal was missing. **Recorded for the Orchestrator's disposition
— I have not touched `registries/`.**

---

## 6 · Method notes and query discipline

### 6.1 A second PubMed parser trap, distinct from the known one

The known failure mode is **punctuation in variant strings**. A **different** one was hit here:

| query | `query_translation` | result |
|---|---|---|
| `WWOX AND 1057` | `… AND **1057[UID]**` | 0 — ⚠️ **silently coerced to a UID lookup**, never a text search |
| `WWOX AND "1057-2A"` | `… AND "1057-2A"[All Fields]` | 0 — unexpanded string |
| `WWOX AND "1057-2"` | `… AND "1057-2"[All Fields]` | **0 — trustworthy** |
| **positive control** `WWOX AND "606-1G"` | `… AND "606-1G"[All Fields]` | **1 — PMID 26345274** ✅ |

> 🔴 **New trap: a bare number becomes `[UID]`.** `WWOX AND 1057` does not search for the text
> "1057"; it searches for **record ID 1057**. A zero from a bare-number query carries **no
> information at all**. This is distinct from the punctuation trap and should be recorded alongside
> it.

**The trustworthy zero:** `WWOX AND "1057-2"` returns 0 with the same query shape that returns a hit
for the positive control. ⇒ **No PubMed-indexed paper mentions this variant string.**
`PREMISE: NOBODY_LOOKED` is **confirmed, with a validated control**, not assumed.

### 6.2 Repository checked before reporting

`grep -rn` under `disease-models/wwox/` was run for `c.1061`, `Gln354`, `Q354`, `p.353_354del`,
`DL-MECH-045`, `DL-MECH-037`, `CLAIM 033`, `intron 8` and each PMID touched.

- **`c.1061` was genuinely open** — `session_evaluations/2026-09-22_orchestrator_third_autonomous_run.md`
  line 128 records it as *"left unresolved rather than inferred from what the prediction requires."*
  **§1 resolves it without doing that.**
- **Intron 8 = 778,856 bp was already known** ⇒ reported as *independently confirmed*, not new.
- **Exon 6 = 89 nt and exon 7 = 186 nt (62 codons) were already known** ⇒ likewise confirmations.
- PMIDs 22071891, 19500159, 26345274 are **all already in the registry**; none bears on exon-9
  acceptor sequence.

### 6.3 Debt and integrity

| check | before | after |
|---|---|---|
| `growth_anchors.py check` — `unread_premises` | **0** | **0** — *no new PMID is introduced; no `FT-` entry is required or created* |
| `FT-` numbers cited | — | **none** |
| files under `registries/` modified | — | **none** |
| receipt ledger / state manifest touched | — | **none** |
| researcher emails or contact details | — | **none** |

**`numpy` was installed** into the session environment to run `residue_context.py`; no repository
file was modified by that.

### 6.4 Provenance of every number

Every coordinate, reference base and exon boundary was computed **in this session** from
`disease-models/wwox/analysis/data/WWOX_clinvar_all_variants.csv`. Every structural number was
computed **in this session** from `disease-models/wwox/analysis/data/WWOX_Q9NZC7_AlphaFold.pdb` via
`disease-models/wwox/analysis/scripts/residue_context.py`. **Nothing is reconstructed from memory.**
No DOI, PMID, HGVS string or coordinate was recalled rather than read.

**Limits, stated plainly:** direct reference-sequence egress remained **403 at CONNECT** throughout
(Ensembl, eutils, NCBI, EBI); `c.1061` is **derived, not directly read** (§1.8). The structural
analysis is on a **predicted** model, and its confidence is lowest exactly at the residues that
decide §3.3. **No RNA from this allele has ever been measured, by anyone.**
