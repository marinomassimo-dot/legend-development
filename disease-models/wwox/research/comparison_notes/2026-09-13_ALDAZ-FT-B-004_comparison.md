# M4b — PMID 14526170 against what this corpus already held

| | |
|---|---|
| **Actor / task** | `scientist-b` · `ALDAZ-FT-B-004` · 2026-09-13 |
| **Receipt** | `FTR-20260913-14526170-01` · `complete_fulltext_read` · `first_read` · 171 chained, tail anchored |
| **Manifest** | `deepdive_manifests/PMID14526170.json` — schema v2, **STRICT PASS, 0 gaps**, 23 locators (15 body, 8 figure), 10 fingerprinted artefacts |
| **Phase discipline** | This note is a **separate phase**, opened only after the receipt landed. The blind pass received the sources, the method and `paper_packet.py packet` only. `comparison_check.py facts` and `inventory` were run **before** this note was written, and the coverage block below was read before the verdict. |
| **Tooling** | `comparison_check.py facts` (records reached hop 0–1: 4) · `inventory` (7 caveat sentences) · `manifest_queue_id_crosscheck --strict` exit 0 |

---

## 0 · Coverage block, read before the verdict

`comparison_check.py facts` reports **4 records reached at hop 0–1**: `CORPUS-STUB-130`,
`LIT-0149`, `FT-079` and `FT-179`. It also reports, and it is right to:

- 🔴 **the identity records DISAGREE** — `CORPUS-STUB-130` says `not_processed`, `LIT-0149` says
  `discovered`. Both are now contradicted by a persisted `complete_fulltext_read`.
- 🔴 **`flag drift` exited 2 — NOT A PASS.** Re-run after the manifest commit, it returns
  `INSUFFICIENT_DATA` with the reason stated in the tool's own words: *"a declared-effort flag cannot
  drift across a single revision … This is the tool's reach, not the manifest's condition."* It is
  recorded here as unscreened rather than as clean.
- `contradicts_locator` is **absent** on all 23 entries, and absent is not `false`. Correct here: no
  prior persisted locator of this paper existed to contradict — this was first contact with the text.

**What the inventory's 7 caveat sentences bear on:** all seven belong to `FT-079` and `FT-179`, i.e.
to the two entries this reading was dispatched to discharge. None is carried into a conclusion below
without being re-derived from the artefact.

---

## 1 · The chain, and where it now stops

```
PMID 16941225  ──delegates specificity──▶  PMID 15982416  ──cites ref 12 for the antibody──▶  PMID 14526170
                                      └──▶  PMID 15692750  ──cites ref 12 for the antibody──▶  PMID 14526170
                                                                                                     │
                                                                                              ◀── STOPS HERE
```

**The chain terminates, and it terminates at immunoblot grade.** The characterisation *is* in this
paper. It is not another hand-off, and the honest finding is neither "the terminus rescues the
atlas" nor "the terminus is empty" — it is that the terminus contains a genuine, and genuinely
narrow, reagent validation.

---

## 2 · The four questions `FT-179` asked in advance, answered in its own order

`FT-179`'s **Next action** named four things to look for and to name in order. All four are answered.

| `FT-179` asked | Answer from the artefact |
|---|---|
| **the actual immunogen** | *«The antiserum was raised using a GST fusion to WWOX amino acid residues 12–94 containing both of the WW domains.»* — manuscript page 6. Stated **once**, unambiguously. |
| **any pre-immune, blocking or pre-absorption control SHOWN** | **None. Not shown and not even asserted.** `pre-immune` 0 occurrences, `pre-absor` 0, `isotype` 0, `peptide block` 0, `no primary` 0. The unshown pre-absorption that `15982416` asserts has **no counterpart at the terminus** — the terminus does not make the claim at all. |
| **a second antibody** | **None.** `polyclonal` 0 occurrences, `monoclonal` 0; the word `antibody` appears **once** in the whole article and `antiserum` five times, six sentences in total. |
| **any immunohistochemical validation at all** | **None, and none is possible:** there is no immunohistochemistry anywhere in this paper. `immunohistochem` 0, `immunostain` 0, `immunoperoxidase` 0, `tissue microarray` 0. The single `paraffin` hit is in a reference title. |

---

## 3 · An `IPOTESI` of my own promoted to `DATO` — the immunogen discrepancy dissolves

`fulltext_dossiers/PMID15982416.md` recorded, as an explicit hypothesis under its epistemic tags:

> `IPOTESI` — that «the WW domains» and «recombinant GST-WWOX fusion protein» name one construct.

and named this paper as *"the only way to settle which construct was the immunogen"*.

**Settled, and in the direction the hypothesis proposed.** One construct: a **GST fusion** to
**residues 12–94**, which **contains both WW domains**. So `15982416`'s two descriptions — *«raised
against the WW domains»* in Results and *«the recombinant GST-WWOX fusion protein used to raise the
antibody»* three paragraphs later — are **both true of the same reagent**, describing the fusion
partner and the insert respectively.

🔴 **This is a discrepancy dissolved, not adjudicated.** The lot's brief asked me to judge what this
paper says *against both* descriptions rather than inherit either, and the answer is that neither was
wrong. The corpus should stop recording an internal tension in `15982416` on this point. What it
should record instead is narrower and more useful: the epitope is **N-terminal**, in exons 1–3.

Cross-checked against this paper's own Fig. 3, inspected at native 4200×3703: the first WW box begins
at L17 and the second ends near P86 — **both inside 12–94**. The immunogen description and the
paper's own sequence map agree.

---

## 4 · 🔴 The consequence that matters most, and `FT-179` predicted it

`FT-179` wrote, before this paper was read:

> **`PMID 11572989`** … La fonte del fatto che PEO1 sia un vero null per WWOX (delezione omozigote).
> **È l'unico controllo negativo di entrambi gli immunoblot**: se il null conservasse un prodotto
> N-terminale, il controllo varrebbe meno di quanto i due paper gli attribuiscano — **e l'anticorpo è
> cresciuto contro la regione WW, cioè l'N-terminale.**

That was a hypothesis about a risk. Three facts now converge on it, and **two of them are new**:

1. **The epitope is upstream of the deletion.** My own prior artefacts record PEO1's lesion as a
   **homozygous deletion of exons 4–8**, cited to `11572989`
   (`deepdive_manifests/PMID15982416.json`, locator: *«does not express WWOX due to a homozygous
   deletion affecting exons 4–8 of this gene [4]»*). The terminus paper puts the epitope at residues
   **12–94**, i.e. **exons 1–3** — *outside* the deleted interval.
2. **The terminus paper's wording is careful and narrower than the corpus has been reading it.** Not
   "produces no WWOX protein" but: *«has a homozygous deletion of the WWOX gene and **does not
   produce full-length WWOX**»*. The qualifier `full-length` is the authors', not mine.
3. **The null lane is not blank.** At 900 dpi, Fig. 5A shows a faint higher-molecular-weight band in
   **both** lanes, including Peo/Vector, plus a fainter lower band in both; in Fig. 5B the same faint
   upper band runs across all four lanes, including the two the caption calls undetectable.

**What this does and does not license, stated so nobody over-reads it.** `IPOTESI`, not `DATO`. The
faint band is **unidentified**: Fig. 5A carries **no molecular-weight ladder at all**, so nothing on
that panel can place it, and non-specific serum background is a fully adequate competing explanation.
What is `DATO` is narrower and still worth having: *the only negative control in the entire chain is a
line whose deletion removes exons 4–8 while the antiserum's epitope lies in exons 1–3, and the
terminus paper's own claim for that line is about full-length protein only.* The loss-of-signal
argument is therefore an argument about the **full-length species**, which is exactly what the paper
says and less than what a reader would assume.

**`REVIVAL_TRIGGER`:** the exon extent of the PEO1 lesion read from `11572989` itself, together with
any evidence of a residual N-terminal transcript or product in that line. `11572989` is already the
second identifier of `FT-179` and remains unread; this reading raises its value rather than
discharging it.

**A difference between papers, recorded rather than smoothed.** My earlier readings found the null
lane **blank** in `15982416` Fig. 1A at 8× and blank-for-WWOX-with-actin-present in `15692750` at 6×.
The terminus paper's null lane is *not* blank. Three blots, one reagent, one null line, and the
cleanest lanes are in the later papers. I do not know why, and I am not inferring from it.

---

## 5 · What the paper is in its own right — its own data separated from restatement and from assertion

The lot required this separation because the genre's failure mode is known: `24932569`, read earlier
in this batch, is the same shape, and its census found *"or carcinogenic"* attributed to a paper
containing no such data. **The failure mode reproduces here, and in the paper's own abstract.**

### 5.1 · Its own new data — first published here, on the evidence of the paper itself

| What | Where | Standing |
|---|---|---|
| **The antiserum and its specificity blot** | Fig. 5A, page 6 text | 🔴 **The reason this lot existed.** *"We have **recently generated** WWOX specific antiserum"* — first description. Genetic null + reconstituted positive, one epithelial lysate. |
| **Breast-line WWOX protein panel** | Fig. 5B | New protein data, correlated by the authors to their own earlier Northern/RT-PCR (Bednarek 2000, 2001). Carries the paper's only two MW marks. |
| **SDR deletion mutants and their localisation** | Fig. 8, page 11 | New: Δ5-7 and Δ8 GFP fusions in MCF10F, both losing Golgi localisation. |
| **Aphidicolin metaphase + YAC933H2 FISH** | Fig. 4 | Presented as the laboratory's own independent confirmation that WWOX maps to FRA16D. |

### 5.2 · Restatement of named primaries — carried, not evidence

Figs. 1, 2 and 7 restate Bednarek 2000/2001, Chen 1996 and Ried 2000. The allelotype grid, the
physical map with its four myeloma breakpoints, and the transcript-variant schematic are all
compilations with their sources named in the captions. Fig. 7's "only in cancer" restriction is
asserted in its key, not measured in the figure, and its accession list carries an evident typo
(AF2119443 for variant 5 against AF211943 for variant 1).

### 5.3 · 🔴 Unpublished assertions — three, and one of them is in the abstract as fact

| Assertion | Body's own modality | Abstract's modality |
|---|---|---|
| The WW1 domain binds PPXY, defining it as Group I | *"In **preliminary studies** we have observed…"* + *"(Ludes-Meyers et al., **manuscript in preparation**)"*, then upgraded one sentence later to *"These studies **confirm**…"* | 🔴 *"We **have identified** the WWOX WW domain ligand as the PPXY motif **confirming** the biochemical activity of this domain"* |
| Transcript variant 1 is the mRNA encoding the full-length protein, by MALDI-TOF of immunoprecipitated WWOX | *"(Ludes-Meyers et al, **unpublished observation**)"* — no spectra, no coverage, no peptide list | not mentioned |
| The SDR domain alone suffices for perinuclear localisation | *"(J.H. Ludes-Meyers, **data not shown**)"* | 🔴 *"we **will demonstrate** that Golgi localization requires an intact SDR"* |

`unpublished` occurs once in the article, `manuscript in preparation` once, `data not shown` once —
and each marks a claim the abstract or a caption states without the qualifier. The paper also draws
a **"necessary and sufficient"** conclusion whose necessity leg is in Fig. 8 and whose sufficiency leg
is the "data not shown" fusion; Fig. 8's own caption title asserts the sufficiency the figure cannot
show, and cross-references a "Fig. 7a" that does not exist. That coupling is the manifest's single
`text_contradicted_by_panel` entry, pointed at `entries[10]` with its needle.

### 5.4 · The sex-steroid frame, third paper in a row

Restated, never tested: *"we **postulated** that WWOX may be an enzyme involved in sex-steroid
metabolism"*, supported by tissue distribution and by the company WWOX keeps in an SDR cluster
analysis. No substrate, product, assay or steroid measured. This matches what `ALDAZ-FT-B-003` found
across the two 2005 papers — restated, not tested, and in the ovarian paper partially disconfirmed
(ER p=0.984). Three papers, one laboratory, one hypothesis, zero measurements of it. Field density
measured today: `WWOX AND sex steroid metabolism` = **10** records in twenty-odd years.

---

## 6 · Records that now need qualifying, and how far — no overshoot into refutation

### 6.1 · `DL-MECH-012` — the live text is now **two steps stale**

The live record (`discovery_ledger_current.md:209`) still reads *«specificità delegata a due paper
**non letti**»*. That was already false after `ALDAZ-FT-B-003`. And `CC-20260913-ALDAZ-B003-01` §3.1
proposed a replacement ending *«entrambi delegano la caratterizzazione dell'anticorpo a `PMID
14526170`, **ancora non letto**»* — which this reading makes stale in turn. **That candidate has not
been propagated** (it is one of the 31 in the backlog), so the correct action is to **supersede its
proposed wording**, not to edit the live record twice. My candidate does exactly that and says so.

🔴 **Direction, stated so nobody over-reads it:** this makes `DL-MECH-012`'s IHC negative **weaker as
evidence**, which *reinforces* its own stated conclusion that the endothelial finding is a tension and
not a refutation. Its `IPOTESI` tag, its direction, its `REVIVAL_TRIGGER` (`PMID 38563965`) and its
microglia caveat all stand untouched.

### 6.2 · The `PMID 16941225` atlas — qualified, and now with a terminus

Every cell-type call and every organ-level negative in that atlas rests on a reagent whose validation
**terminates** at immunoblot grade on epithelial lysate against a cell-line null, with **no
immunohistochemical control at any point in the chain** and **no neural validation anywhere**. The
calls stand as that paper's observations. What changes is that the reagent basis is no longer a
declared unknown pointing at an unread paper — it is measured and closed.

The premise withdrawal that `ALDAZ-FT-B-003` recorded for `fulltext_dossiers/PMID16941225.md` §4.1
(`PREMISE: INFERENZA — the delegated control is adequate` → `PREMISE: DATO` with the boundary)
**completes here** and can be stated without a forward reference. 🔴 Not edited by this task: it is a
previous lot's artefact and it is named for whoever propagates.

### 6.3 · A reagent boundary that is now sayable in one sentence

> The anti-WWOX antiserum of the Aldaz laboratory is validated, at its own point of origin, by
> loss-of-signal of a ~46 kDa species in a WWOX-deleted ovarian line and gain-of-signal on
> reconstitution; its epitope is residues 12–94, spanning both WW domains, so it cannot distinguish
> full-length WWOX from the SDR-deleted isoforms, by the authors' own statement; the panel asserting
> the 46 kDa size carries no molecular-weight ladder; and nothing in the chain validates it for
> immunohistochemistry, for tissue, or for neural tissue.

### 6.4 · Unaffected — checked, not assumed

| Not touched | Why |
|---|---|
| **Every consolidated baseline claim** | `claim_registry_current.md` was grepped for `antibod`, `antiserum`, `specificit`, `tissue distribution` and `16941225`: the only hits are `CLAIM 016` (lithium/PTZ genotype specificity) and the Src/p73 routing boundary, neither of which names this PMID or rests on this reagent. **No claim names 14526170. No claim is narrowed, reversed, corroborated or removed.** |
| **R4 / `legend-locator-audit`** | **Not triggered.** No consolidated baseline claim is touched, no MAJOR is declared, and no persisted locator is contradicted. |
| **`DL-MECH-012`'s endothelial and microglial legs** | untouched in substance; only the reagent parenthetical moves. |
| **The four scientific current files and `disease_model.md`** | not touched by this task at all — a commit candidate is produced instead. |
| **BLOCCO 1 / safety** | nothing in a 2003 cancer-genetics review bears on it. |

---

## 7 · Debt: what is discharged, what is raised, and what needs no new address

| Entry | Disposition |
|---|---|
| **`FT-079`** | Its antibody residue — which after B-003 read *«la catena non termina qui … `→ 14526170`, senza ricevuta in questo ledger»* — is now **fully discharged as to the antibody's characterisation**. The terminus is read and the characterisation is described. |
| **`FT-179`** | **First of four identifiers discharged.** `14526170` has a receipt; its four questions are answered in §2. Still open: `15073846` (the only external group named, antibody unstated — the independence question), `11572989` (now **more** valuable, see §4), `14695174` (the published localisation disagreement). Priority stays HIGH on the strength of `11572989` alone. |
| **`PMID 10861292`** (Ried 2000) | Surfaced again here as a gene-direct antecedent absent from every registry file. 🔴 **It needs no new address: `FT-080` already carries it**, resolved from ref 43 of `18674750`. Recorded so nobody mints duplicate debt. |
| **`CORPUS-STUB-130` / `LIT-0149`** | Identity records disagree with each other and both are contradicted by the receipt. Promotion and completion proposed in the candidate. |

---

## 7b · Answers to `comparison_check check` — because "not audited" is not "passed"

`comparison_check.py check` returned **ANSWER FOR THESE**. Its questions, answered rather than left
to the reader.

### 7b.1 · COVERAGE (3): caveats this note lists but does not argue from

All three belong to `FT-079` (`full_text_queue_current.md:3984`, `:3997`, `:4001`) and concern the
`16941225` atlas's **quantification** — that the ACIS values are not reported, that the grades are
categorical, and that its organ-level result is *"non è un negativo e non può essere trasportato come
tale"*. **Correctly listed and correctly not argued from:** this reading bears on the atlas's
*reagent basis*, not on its scoring or its quantification, and nothing in §6 rests on those three
sentences. They remain open and belong to `FT-079`, untouched by this lot.

### 7b.2 · 🔴 COMPARATOR NOT IN THE SOURCES — the flagged sentence, with its addresses

The tool flagged §4's closing sentence, on the null lane being *blank* in the two 2005 papers. Its
warning is exactly right — *"that is what a paraphrase looks like, and it is also what an invention
looks like, and this command cannot tell them apart"* — and the reason it cannot is that the values
are attested **in my own prior artefacts**, which are not among *this* paper's declared sources.

The addresses, so the sentence is checkable rather than recollected:

- `fulltext_dossiers/PMID15982416.md:62` — *«PEO1, an ovarian line carrying a **homozygous deletion of
  exons 4–8**, run as negative control; «no immunoreactive products». Figure 1A, inspected: **the null
  lane is blank**, the transfectant lane carries one discrete band, actin present in both.»*
- `fulltext_dossiers/PMID15692750.md:61` — *«`NEG.` = PEO1. At 6× the lane is **blank for WWOX while
  carrying actin in that same lane** — the control is demonstrably loaded, not merely empty.»*
- The exon extent used in §4 is a persisted locator, not a memory:
  `deepdive_manifests/PMID15982416.json` — *«does not express WWOX due to a homozygous deletion
  affecting exons 4–8 of this gene [4]»*.

The "8×" and "6×" are magnifications recorded in those readings, not measurements of this paper.
**Nothing in §4's conclusion depends on them** — it depends on the exon extent, the authors'
`full-length` qualifier, and this paper's own Fig. 5A at 900 dpi.

### 7b.3 · NOT AUDITED (23 sentences)

Declared, not waved past. Every value in those sentences is one of three things, each already
addressed: (a) a measurement of **this** paper backed by a manifest locator (the 4200×3703 Fig. 3
dimensions, the `85 kd` / `39.5 kd` marks, residues 12–94, exons 1–3); (b) a **tool output** quoted
with its verdict (`flag drift` INSUFFICIENT_DATA, the 88→4 intrusion spans, 20-of-56 references
screened); or (c) a **quotation from a prior artefact of mine**, now carrying its address in §7b.2.
The comparator list's silence is not evidence that there is no comparison here, and none of the 23 is
reported as attested.

---

## 8 · Verdict

**The reading answers the question the lot was created for, and the answer is a boundary rather than a
rescue or a condemnation.** The antibody's characterisation is at the terminus; it consists of one
immunoblot against a genetic null with a reconstituted positive; it is immunoblot-grade, epithelial,
non-quantitative as to size, blind to isoforms by design, and it contains no immunohistochemistry of
any kind. The deferral chain the corpus had been following ends here — it does not end in an absence,
and it does not end in the control the tissue atlas presupposed.

Everything downstream is **QUALIFIED, not refuted**. One discovery-ledger clause changes. Two identity
records get promoted. One premise tag completes its withdrawal. No claim moves, no status moves, no
baseline is narrowed, and no audit is owed.
