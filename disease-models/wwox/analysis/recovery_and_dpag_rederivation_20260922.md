# 529 recovery record, and the `DP_AG` adjudication re-derived from sequence

**Actor:** Orchestrator · **Date:** 2026-09-22 · Non-canonical. Nothing here is medical advice.

---

## 1 · Recovery state — measured, not inferred

| item | measured value |
|---|---|
| current branch | `claude/wwox-woree-autonomous-scout-paqlty` |
| `HEAD` | **`9074294`** |
| `origin/main` | **`9074294`** |
| `origin/claude/wwox-woree-autonomous-scout-paqlty` | **`9074294`** |
| local `main` ref | `83ec6be` — **known stale**, tagged `preclone-main-83ec6be` in an earlier wave; an ancestor of two live remote branches, so it holds no unique material |
| working tree | **clean** |
| untracked | **none** |
| staged | **none** |
| unpushed (`origin/main..HEAD`) | **none** |

🔵 **The Operator's stated `4e5d141` is stale by seven commits.** All seven landed *after* it and
**all seven are on both `origin/main` and `origin/<branch>`**:

`2d97d0b` · `d1d8562` · `0853f5e` · `6087763` · `51b4204` · `3c4759e` · `9074294`

**Classification: all seven `VALID_COMPLETE`.** Each was gated (LINT · growth anchors · publication
gate; receipts where touched) and pushed before the next began. **Nothing is `PARTIAL`,
`DERIVED_ONLY` or `UNKNOWN` on this branch.**

### 1a · One stray artefact, classified and left alone

`git worktree list` reports a second worktree at `/tmp/tmpryqdf5r_/tree`, detached at `5f7aa57`
(**an ancestor of `HEAD`**), carrying one modification: two lines appended to `README.md` naming
a deliberately absent script under `framework/scripts/` (the literal path is not reproduced here:
this file is scanned by `test_documented_commands.py`, and quoting the fixture made that guard red).

**Classification: `DERIVED_ONLY` — test scratch.** It is the deliberately-absent filename used to
mutation-test `test_tool_routing.py`. Zero scientific content. **Not committed, not deleted** —
it lives in `/tmp`, holds no branch, and removing it is not required to restore canonical state.

---

## 2 · Scientist status

| agent | task | status | evidence |
|---|---|---|---|
| **Scientist E** | WWOX splice-allele transcript measurements | ✅ **COMPLETE** | `splice_allele_rna_evidence_20260922.md` added in `2d97d0b`; findings verified and landed as `CC-20260922-SPLICE-ARM-01` |
| **Scientist F** | Domain G / superior unknown node | ✅ **COMPLETE** | `superior_node_search_20260922.md` added in `0853f5e`; findings verified and landed as `CC-20260922-TAU-DIRECTION-01` |
| Scientist G (3rd launch) | post-diagnosis developmental window | ⏳ **STILL_RUNNING** | output file not yet present |
| Scientist I | `c.1057-2A>G` cryptic-acceptor test | ⏳ **STILL_RUNNING** | output file not yet present |

🔴 **Two earlier launches (G, H) were `LOST_AFTER_529`** — verified by `git status` showing **no
output files and no partial writes**, so **LOST, not PARTIAL**, and no partial conclusion was
inherited. Scientist H's task was subsequently executed by the Orchestrator directly and landed as
`CC-20260922-EXON7-NATURAL-EXPERIMENT-01`. **No scientific conclusion anywhere in this session was
reconstructed from agent memory.**

---

## 3 · Receipt-count reconciliation — resolved once, from repository reality

**Measured on this branch:**

```
physical non-blank lines : 189
parsed JSON records      : 189
unique event_ids         : 189
duplicate event_ids      : none
with ledger_prev_hash    : 188      (the 189th is the genesis record, which has no predecessor)
fulltext_receipts.py verify → OK: 189 chained receipt(s), tail anchored
```

> ### **189 total records / 189 chained / 0 excluded.**

**The historical numbers, both explained, with nothing altered:**

| number | what it actually was |
|---|---|
| **188** | **this branch, before today.** `188 + FTR-20260922-30202070-01 = 189.` |
| **200** | 🔴 **a different ref.** `claude/legend-autonomous-woree-tv6gz8` @ `f7595f6` carries **200**. |

**Measured directly** (`git show <ref>:…/fulltext_read_receipts.jsonl | grep -c .`):
`f7595f6` → **200** · `4e5d141` → **189** · `9074294` → **189**.

And the divergence is an **append-only fork of a shared prefix**, not a discrepancy:

```
identical leading event_ids : 188
ours-only                   : 1   [FTR-20260922-30202070-01]
sibling-only                : 12  [FTR-20260921-37974179-01 … FTR-20260921-30783266-01]
188 + 1  = 189  (ours)      188 + 12 = 200  (sibling)
```

🔵 **So: not a reporting error, and not a loss.** The two numbers were counts of two different refs.
⚠️ **One thing has changed and whoever merges must know it:** the sibling ledger was previously a
strict **superset** of ours. It no longer is — we now hold one record it lacks. **The merge is a
two-way append merge.** Nothing was rewritten to make any count agree.

---

## 4 · §3 — the `DP_AG` / TX-001 adjudication, re-derived

The pre-529 checkpoint note is treated as **UNVERIFIED** and re-derived below.

**1 · Reference transcript.** `NM_016373.4` (WWOX), the transcript every HGVS string in
`disease-models/wwox/analysis/data/WWOX_clinvar_all_variants.csv` is written against. Genomic
assembly `NC_000016.10` (GRCh38), **plus strand** — established by 729/729 reference-base
concordance between ClinVar cDNA ref alleles and their SPDI deleted alleles.

**2 · Boundary involved.** The **intron 8 / exon 9** acceptor. Exon 9 = `c.1057–1245`, **the last
exon** (there is no exon 10). The allele is `c.1057-2A>G`.

**3 · Coordinate convention.** SPDI `position` is **0-based**; 1-based = SPDI + 1. **Validated
twice, independently:** the SNV `c.1057-9G>C` (SPDI `…:79211598`) puts **G** at 79,211,599, and the
duplication `c.1057-9_1057-6dup` (SPDI `…:79211599`, deleted allele `GATT`) puts **G,A,T,T** at
79,211,599–602 — the two agree on both the frame and the base, and the SNV `c.1057-7T>C`
independently confirms **T** at 79,211,601.

**4 · Exact local sequence, as far as the reference permits** (`?` = no ClinVar record covers it;
direct sequence egress is **403 at CONNECT** for Ensembl, eutils, NCBI and EBI):

```
intron 8 3' end            exon 9 ->
c.  -9  -8  -7  -6  -5  -4  -3  -2  -1 | 1057 1058 1059 1060 1061 1062 1063 1064 1065 1066 1067
     G   A   T   T   ?   C   C   A   ? |   C    ?    A    C    ?    G    G    ?    ?    G    C
pos 599 600 601 602 603 604 605 606 607|  608  609  610  611  612  613  614  615  616  617  618
                                        (all 79,211,xxx)
```

**5 · The canonical `AG`.** At `c.1057-2, c.1057-1`. `c.1057-2 = A` is measured (it is the variant's
own reference allele). `c.1057-1` is not covered, but is **G** by necessity — a functioning
canonical acceptor requires `AG`, and this one functions in wild type. **The variant `A>G` at −2
converts `AG` → `GG` and destroys it.** This is the confident part: `DS_AL 0.96` plus MaxEntScan
Δ −7.95, two orthogonal methods.

**6 · What `DP_AG` means.** In SpliceAI's output, `DP_AG` is the **position offset, relative to the
variant, of the highest-scoring acceptor *gain***, and an acceptor position denotes the **first
nucleotide of the exon**. `79,211,606 + 8 = 79,211,614 = c.1063`. ⚠️ **The adjudication below does
not depend on that convention being right** — the convention only says *where SpliceAI pointed*;
the exclusions come from sequence.

**7–8 · Interpretations, and which sequence excludes.** A gained acceptor requires an `AG`
immediately 5′ of the new first exonic base:

| new exon starts | nt lost | frame | required `AG` at | reference says | verdict |
|---|---:|---|---|---|---|
| `c.1061` | 4 | frameshift | `c.1059`,`c.1060` | `A`,**`C`** | ⛔ **excluded** |
| `c.1062` | 5 | frameshift | `c.1060`,`c.1061` | **`C`**,`?` | ⛔ **excluded** |
| **`c.1063`** | **6** | **in-frame** | `c.1061`,`c.1062` | `?`,**`G`** | 🟢 **survives, conditional on `c.1061 = A`** |
| `c.1064` | 7 | frameshift | `c.1062`,`c.1063` | **`G`**,`G` | ⛔ **excluded** |
| `c.1065` | 8 | frameshift | `c.1063`,`c.1064` | **`G`**,`?` | ⛔ **excluded** |
| `c.1067` | 10 | frameshift | `c.1065`,`c.1066` | `?`,**`G`** | ⛔ **excluded** |
| `c.1068` | 11 | frameshift | `c.1066`,`c.1067` | **`G`**,`C` | ⛔ **excluded** |
| `c.1069` | 12 | in-frame | `c.1067`,`c.1068` | **`C`**,`?` | ⛔ **excluded** |
| `c.1066` | 9 | in-frame | `c.1064`,`c.1065` | `?`,`?` | ⚠️ **cannot be excluded — both bases unknown** |

**9 · Surviving interpretation.** 🎯 **`c.1063`**, and it is the only survivor at or adjacent to the
position SpliceAI pointed to. The pointer and the sequence agree.

> 🔴 **And one exclusion is unconditional, which is the finding that does not depend on the missing
> base: the 7-nt and 8-nt frameshift readings are excluded by *measured* bases** (`c.1062 = G`,
> `c.1063 = G`; an acceptor's `AG` cannot begin with `G`). **`DL-MECH-045`'s current position — a
> frameshift producing a *"proteina tronca instabile"* — is not supported by the reference sequence
> at this locus, regardless of how `c.1061` turns out.**

**10 · Consequence for TX-001 headroom.** If `c.1061 = A`: `c.1057–1062` are lost = **6 nt**, and
since `(1057−1)/3 = 352` exactly, `c.1057` is the first base of codon 353 — so the loss is **exactly
codons 353 and 354, an in-frame two-residue deletion `p.353_354del`** in a 414-aa protein, with **no
PTC and no NMD**. That is a **hypomorph**, and materially more headroom than a null.

⚠️ **Bounded, and the bounds are the point.** It remains **`PREDICTED`**: `DS_AG 0.64` is moderate,
a predicted gain is not a used site, the `c.1066` start cannot be excluded, and **nobody has ever
measured this allele's RNA.** And `D-30` applies — *in-frame is a statement about the reading frame,
not about the fold* — though two residues near the C-terminus is a very different proposition from
the 62 that killed the exon-7 case.

### 4a · 🔴 The one missing base — one bounded attempt, and it failed

`c.1061` (`NC_000016.10:79,211,612`) is **not covered by any ClinVar record**, and the only
multi-base deleted allele anywhere in the window — `GATT` at 79,211,599–602 — lies **entirely in
intron 8** and does not reach it. **Not established. Not guessed, and not inferred from what the
prediction needs.** Recorded as the single check that would falsify the surviving interpretation.
