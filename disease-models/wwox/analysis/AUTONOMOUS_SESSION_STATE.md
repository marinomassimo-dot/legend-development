# Autonomous session — continuation state

> 🔴 **2026-09-22, FIFTH BLOCK — WRITTEN LAST, READ FIRST.** Supersedes the blocks below where they
> disagree. **Not a handoff and not a stop.** Two Scientists running as this is written.

## State — head `ebc05d9`, `HEAD == origin/main == origin/<branch>`, tree clean

Gates at every landing: **LINT PASS · growth anchors PASS (measured, never predicted) · receipts
verify 189 chained, tail anchored · publication gate PASS 0 blocks · prose `FT-` refs unresolved 0**.

### ✅ THE 27-DAY BLOCKER IS CLEARED — operator authorized, verified, PROPAGATED

**`BATCH_20260922_SEIZURE`, WM_v4.5 → WM_v5.0 (MAJOR).** All four first-hand datasets verified
first; Cheng 2020 against both its manifest **and** its retrieved body. `CLAIM 037`'s *"explicitly
absent in Wwox-null mice"* **deleted as false**; `CLAIM 005`'s prohibition **retargeted, not
deleted** — it now bans asserting *epileptogenesis as a process* (unmeasured in every WWOX model)
instead of banning description of the animal. **New `CLAIM 040`.** Four axes kept separate and
forbidden to merge. **One limb of the candidate was DROPPED for want of verification** (the `Syn-Cre`
P9 falsifier rests on a paper with no PMCID). Both blocking gates fired first and were obeyed.

### 🔴 TWO RULES I LANDED MYSELF ARE WRONG — corrected today

1. **`is_open_access: false` is a LICENCE field, not a retrievability verdict.** PMID 36779245 and
   23583307 both flag `false` and **both were served in full**; two papers with PMCIDs return empty
   bodies. My *"pre-test 6/6"* was scoring a rule whose failures it had not met, and skipping on it
   would have cost a wave its two best sources. **ORDER attempts with it; never SKIP.**
   `FT-128/129/130`'s dispositions are re-labelled **unacquirable by attempt, not by licence** — and
   Mallaret was then attempted: `PMC3914474` → `full_text: ""`. Right answer, wrong reasoning.
2. **`P1–P5` is not a window** — it is the set of ages tested, and our own locator file for that
   paper records the authors calling it *"rather than a definitive boundary for therapeutic
   responsiveness."* **I relayed that filter to the Operator as "the binding one" without checking
   our own file.** `D-31`.

### 🎯 The live science, ranked

1. 🟢 **`c.1061 = A`, established deductively** from ClinVar protein-consequence records, twice
   independently (`p.Gln354Ter` and `p.Gln354=` each force it) plus the local AlphaFold file. **The
   `AG` the prediction needs exists.** The site is **over-determined without SpliceAI**: intron 8's
   last ~29 nt contain no `AG`, and the first-AG-downstream rule reaches `c.1061/62` first ⇒ exon
   starts `c.1063` ⇒ **in-frame `p.Gln353_Gln354del`**. The 8-nt frameshift reading is dead at both
   required bases. ⚠️ **But the PROTEIN consequence is UNKNOWN and structurally contested** —
   mid-α-helix, one turn from a buried face, model confidence lowest exactly there. Correct label:
   **`PREDICTED at transcript level — protein consequence UNKNOWN`.**
2. 🎯 **The compartment we assumed closed is measurably OPEN.** Sanai 2011 (*Nature*): migrating
   immature neurons in infant human SVZ/RMS **before 18 months**, prefrontal-targeting stream at
   4–6 months, ~25-fold DCX⁺ decline over 6 months. WOREE presents at a **median 5 weeks**.
   🔴 **The intersection is empty on the WWOX side, not the plasticity side** — zero WWOX
   measurement in postnatal SVZ, any species, any age. **One desk-or-tissue experiment decides
   filter 2.** Being worked now.
3. 🔴 **Nobody has ever reported age at molecular diagnosis in a WWOX cohort.** Verified zero with an
   expanded translation and a positive control. Filter 2 supports only a **one-sided bound**.
4. 🔴 **The exon-7 hypomorph is dead** (`D-30`: in-frame is about frame, not fold) — and its
   corollary from today: **the relSASA of a *deleted* residue is a claim about that side chain, not
   about the fold.** `DL-MECH-037`'s discriminator was calibrated on *substitutions*.
5. 🔴 **Tau-lowering must not be imported into WWOX-DEE** — Tau is the effector of the benefit.
6. 🔴 **`PAPER 044`'s "nonsense-mediated decay" is from the abstract**; no WWOX allele of any class
   has ever been assayed with an NMD inhibitor.

### 🔴 The defect that would have wasted a real experiment

`tx001_experiment_decision_packet_20260921.md` — **the document a lab executes** — said the cryptic
acceptor gives `+8 nt`. It gives **6 nt SHORTER**. Wrong in **sign and magnitude**: `+8` is a genomic
offset, not an amplicon size change. **A lab sizing against it would score the assay negative while
the predicted event was occurring.** Fixed **at the point of error**, with the method constraint
added (capillary, denaturing, 6-nt sizing standard; not agarose, not native PAGE) and the intron-8
blind spot given a row. It also asserted an exon 10, twice; WWOX has nine exons.

### Three proven ways a query-count zero is meaningless

(a) punctuation ⇒ raw query echoed **unexpanded** ⇒ 0; (b) a **bare number** ⇒ `NNNN[UID]`, a
record-ID lookup; (c) `[All Fields]` **does not index Methods**. **Read `query_translation` before
believing any zero, and always carry a positive control.**

### Recovery facts, measured

`4e5d141` was stale by seven commits, **all `VALID_COMPLETE`**. Receipts: **189 total / 189 chained /
0 excluded**; the historical `200` is the **sibling branch** `f7595f6`, sharing an identical
188-record prefix — **ours + 1, theirs + 12**, so the merge is now **two-way**, not a superset.
Two Scientists were `LOST_AFTER_529` with **no** partial writes; one of those tasks I did myself.

### Immediately next

- **Running:** Scientist J — TX-007 dose challenge and replication search. Scientist K — is WWOX in
  postnatal human SVZ answerable from public data. **Verify both against primary sources; refill on
  return.**
- Standing: `VERIFY → LAND → SAFE_PUSH MAIN → REASSESS → REFILL`. **QUEUE EMPTY ≠ SESSION DONE.**
- Delegate base rate: **ten waves — three clean, four corrected, one false alarm, two lost to 529s.**

---


> 🔴 **2026-09-22, FOURTH BLOCK — WRITTEN LAST, READ FIRST.** Supersedes the blocks below where
> they disagree. **Not a handoff and not a stop.** One Scientist running as this is written.

## State — head `51b4204`, landed on canonical `main` and on the task branch

Gates at every landing: **LINT PASS · growth anchors PASS (`unread_premises=0`, measured never
predicted) · receipts verify 189 chained, tail anchored · publication gate PASS 0 blocks · prose
`FT-` references unresolved 0 · release regressions clean** (only declared environment skips: no
PyMuPDF, no numpy, shallow clone, `files/` gitignored — the KNOWN ENVIRONMENT class).
**No canonical registry file has been modified today.** Everything is candidates, queue entries,
receipts, analysis and one harness upgrade.

### The items an operator decision is owed on

1. 🔴 **`CC-20260826-SEIZURE-RECONCILIATION-01` — MAJOR, queued unapplied for 27 days.** It shows
   `CLAIM 005`'s prohibition forbids statements three canonical claims already make (`004`, `011`,
   `016`), and `CLAIM 037`'s headline is false against four first-hand datasets, earliest 2020. It
   states it requires operator authorization. **Needs a decision, not another candidate.** R4.
2. **`D-17` remains reserved (operator-deferred).** `D-18`…`D-30` are proposed across ten
   candidates, none propagated.

### The live science, ranked

1. 🎯 **`c.1057-2A>G` — the reference genotype's own splice allele — predicts an IN-FRAME two-codon
   deletion (`p.353_354del`), not a truncation.** Adjudicated from our own ClinVar export: `+8` from
   the variant is `c.1063` exactly (three SPDI anchors), and the reference bases **exclude** every
   competing reading (`c.1062=G`, `c.1063=G`; an acceptor needs `AG`, so starts at `c.1064`/`c.1065`
   are impossible). **Contradicts `DL-MECH-045`'s "truncated unstable protein".** ⚠️ One base
   unverified: **`c.1061` must be `A`** — no ClinVar record covers it, sequence egress is 403.
   Still `PREDICTED`; `DS_AG 0.64` is moderate and nobody has measured this allele's RNA.
2. 🔴 **The exon-7 hypomorph is DEAD — I proposed it and killed it the same day.** The skip deletes
   residues 203–263 (62 codons, 414→352 aa). Triad `S281/Y293/K297` and region `388–407` are spared
   **in sequence only**: the deletion removes ~62 residues from the interior of the ADH/SDR domain
   (110–414 a.a., verbatim `PMC3354054`), and a Rossmann fold positions its catalytic residues by
   the scaffold around them. The natural experiment agrees — `PMID 30361190`'s `c.606-1G>A`
   homozygote had cluster spasms at 11 months on four antiepileptics, filed as `null biallelici`.
   **`D-30`: in-frame is a statement about the reading frame, not about the fold.**
3. 🔴 **Tau-lowering must NOT be imported into WWOX-DEE.** The pathway looks like a tauopathy, and
   the arrow points the other way: *"Neither WWOX overexpression nor GSK3β knockdown promoted
   neurite outgrowth in the Tau knockdown condition, indicating that Tau is the effector of both"*
   (`PMC3354054`, read in full by me). **No repository text said this.**
4. 🔴 **`PAPER 044`'s "nonsense-mediated decay" is from the abstract.** The body says *"not expressed
   **or** were degraded"* — two alternatives, unresolved — and **no NMD inhibitor was used**. With it
   withdrawn, **no WWOX allele of any class has ever been assayed with an NMD inhibitor.**
5. 🔴 **`HYP-08`'s lysosomal arm would have returned a false negative** — chloroquine + NH₄Cl,
   imported from an over-expressing line; Schultz 2018 on endogenous protein in primary patient
   fibroblasts has **bafilomycin positive, chloroquine not**. Add bafilomycin. And the step order is
   not executable: a chase from an undetectable band is undetectable at every timepoint.
6. 🔴 **Nobody has ever audiogenically provoked a Wwox mouse**, and **`Wwox^gt/gt` has never been
   observed, EEG'd or provoked** (`Epilepsy` cell empty in Suzuki's Table 2). The survival-confound
   explanation is an *unattempted experiment on an available animal*, not an open question.
   ⚠️ **CORRECTED 2026-09-22:** I wrote *"viable 2 years"* here. That is **Suzuki's Table 2, a
   secondary source at `panel` depth**, and the **primary contradicts it** — Ludes-Meyers 2007's own
   abstract says the `gt/gt` mice *"had a **significantly shorter lifespan**."* Both are on file,
   never reconciled; neither is a read of the primary's body. **Stop using the 2-year figure
   unqualified.** Also corrected: `gt/gt` is **not** established as *"a hypomorph with residual
   protein"* in brain — the primary says *"no detectable Wwox protein in most tissues examined,
   although a low level could be detected in a minority of tissues"*, and **names no tissue and not
   brain.**
7. **Domain G returned NEGATIVE.** No node superior to the portfolio. Three near-exclusive filters
   explain why; the binding one is **"is anything still plastic after diagnosis?"** — now the
   running Scientist's question.

### Two instrument defects proven today, both of which invalidate classes of negative

- 🔴 **PubMed returns a FALSE ZERO on punctuated variant strings.** `WWOX AND "c.606-1G>A"` → **0**
  with `query_translation` echoing the raw string **unexpanded**; `WWOX AND "606-1G"` → the paper,
  fully expanded. **Read `query_translation` before believing any zero.**
- 🔴 **PubMed `[All Fields]` does not index Methods**, so a query-count negative about a *method*
  proves nothing — proven from inside Scientist D's own census.

### What I got wrong today — the list is the point

- Nearly landed *"the experiment was run and never propagated"*; **`DL-MECH-037` is the
  propagation**, and better than my version. Caught while writing it.
- Wrote `UNREAD_PREMISE impact: none`; the ratchet returned **10**, naming a paper I had read
  myself and never declared. **Never predict that number; measure it.**
- Framed `D-25`'s seizure section as new when a MAJOR candidate had held it 27 days, and ranked a
  paywalled abstract above full-text mouse data from 2020.
- Attached a five-patient count from `PMID 26345274` to a quotation from `PMID 30361190` — the exact
  defect class I had corrected in two delegates hours earlier.
- Proposed the exon-7 hypomorph and killed it four hours later with data that was in the repository
  the whole time.

### Delegate base rate, recorded because it matters

**Eight waves: two clean** (Scientist C bafilomycin, Scientist F Tau direction — both verified
unchanged), **three corrected**, **one false alarm** (`C-2`), **two lost to server 529s** with no
output (LOST, not PARTIAL — nothing to distrust).

### Immediately next

- **Running:** Scientist G — is anything still developmentally plastic at diagnosis
  (`postdiagnosis_window_evidence_20260922.md`). **Verify against primary sources before landing;
  refill the slot on return.**
- **Second slot open** — 529s have been rejecting launches; retry.
- ⛔ **Highest-value unacquired paper: `PMID 26345274`** (Tabarki 2015, five `c.606-1G>A`
  homozygotes, `FT-032` / packet `A8`). Never read; the natural experiment is only as good as it.
- Standing: `VERIFY → LAND → REASSESS → NEXT TASK`. **QUEUE EMPTY ≠ SESSION DONE.**

---


> 🔴 **2026-09-22 — THIRD BLOCK, WRITTEN LAST, READ FIRST.** Everything below remains accurate
> except where this block supersedes it. **Not a handoff and not a stop.** Two Scientists are
> running as this is written; the session continues.

## Where the work stands — head `cb4ae25`, landed on canonical `main` and on the task branch

Gates at every landing: **LINT PASS · growth anchors PASS (`unread_premises=0`) · publication gate
PASS, 0 blocks · ledger 188 chained, tail anchored.** No canonical registry file was modified today;
everything is candidates, queue entries and analysis.

### The four findings that would be expensive to lose

1. 🔴 **A MAJOR commit candidate has been queued and unapplied for 27 days, and it is the most
   important open item in the repository.** `CC-20260826-SEIZURE-RECONCILIATION-01` establishes that
   `CLAIM 005`'s prohibition — *"No canonical statement may describe a Wwox-null mouse as showing
   epileptogenesis"* — **forbids statements three canonical claims already make** (`CLAIM 004`,
   `011`, `016`), and that `CLAIM 037`'s headline *"explicitly absent in Wwox-null mice"* is **false
   against four first-hand datasets, earliest 2020.** It states that it requires operator
   authorization, which is why it has not been applied. **This needs an operator decision, not
   another candidate.** It is an R4 item.

2. 🔴 **The decisive animal has existed since 2007 and nobody has looked at it.** Suzuki's own
   Table 2: `Wwox^gt/gt` viability **2 years**, `Epilepsy` cell **empty**. An animal that lives two
   years cannot "die before it seizes" — so the field's standing survival-confound explanation for
   the mouse/rat discordance is **an unattempted experiment, not an open question.** And **no Wwox
   mouse of any allele has ever been audiogenically provoked**, so the species contrast under a
   canonical claim has never been run with the same stimulus. → `CC-20260922-SEIZURE-ASCERTAINMENT-01`
   (`D-27`).

3. 🔴 **`HYP-20260709-08`'s lysosomal arm would have returned a false negative.** It specifies
   chloroquine + NH₄Cl, imported from a paper run in **over-expressing CAL-62 cells**. Schultz 2018
   (PMID 30202070, read in full this session) ran the comparison on **endogenous protein in primary
   patient fibroblasts**: bafilomycin A1 recovered the mutant to WT levels, chloroquine *"did not
   significantly alter"* them. **Add bafilomycin.** Also: the minimal experiment's step order is not
   executable — a chase from an undetectable band is undetectable at every timepoint, so inhibitors
   must come first. → `CC-20260922-HYP08-LYSOSOMAL-ARM-01` (`D-26`). ⛔ **Blocked on a receipt**:
   30202070 was read in full and no receipt was persisted; depth is `partial_fulltext_read` because
   the route stripped every figure number.

4. 🟢 **`TX-003`'s in-silico support does not discriminate, and `DL-MECH-037` already said so.**
   `il ΔΔG non discrimina`; burial discriminates, ΔΔG does not; and a **buried proline in an α-helix
   imposes a backbone constraint a chaperone cannot remove.** I nearly landed a false finding that
   this had never been propagated — see below.

### What I got wrong today, recorded because the corpus is only as honest as this list

- 🔴 **I nearly landed a false "never propagated" finding.** Having found `DL-MECH-033` calling an
  in-silico test *"il prossimo passo prioritario"*, I drafted the conclusion that it was run and
  never propagated back. `DL-MECH-037`, 87 lines below in the same file, **is** the propagation, and
  is better than what I was about to write. Caught by checking before writing it up. Census: `self`,
  `severity_high`.
- 🔴 **I wrote `UNREAD_PREMISE impact: none` and the ratchet returned `10`** — naming a paper I had
  read myself and never declared. All ten now declared in `FT-129`; ratchet back to 0.
  **Never predict that number again; measure it.**
- 🔴 **I framed `D-25`'s seizure section as a new discovery** when a MAJOR candidate had held it for
  27 days, and I ranked a paywalled abstract above full-text mouse data from 2020. Corrected
  append-only; §1 (chain naming) stands, §2 withdrawn.
- 🟢 **Scientist C's headline survived verification unchanged** — the first delegate lead item today
  that needed no correction. Verified by retrieving the primary body myself.

### The standing rules that paid out today

- *Check the repository before reporting anything as absent.* Paid out **five times**; twice it found
  the repository at fault, once it found **me**, mid-sentence.
- *A query-count negative about a METHOD is not evidence the method was not performed* — PubMed
  `[All Fields]` does not read Methods, **proven from inside Scientist D's own census**.
- `get_copyright_status` as a one-call pre-test: **6/6**. **A PMCID is not a body** — six instances.
- **A paywall is not a route failure.** PMID 24369382 and 21476439 are unacquirable here; PMID
  36779245's Table S1 was open access and unreachable, which is a different problem.

### Immediately next

- ⛔ **Persist the `FULLTEXT_READ_RECEIPT` for PMID 30202070.** `D-26` may not propagate without it.
- Two Scientists running: **E** — what the field has actually *measured* about WWOX splice-allele
  transcripts (`splice_allele_rna_evidence_20260922.md`); **F** — Domain G, the superior unknown node
  (`superior_node_search_20260922.md`). **Verify both against primary sources before landing, and
  refill each slot on return.**
- Standing: `VERIFY → LAND → REASSESS → NEXT TASK`. **QUEUE EMPTY ≠ SESSION DONE.**

---


> 🔴 **2026-09-21, SECOND autonomous run (operator in transit). READ THIS BLOCK FIRST.**
> The sections below it are the *previous* run's state and remain accurate except where this
> block says otherwise. **Not a handoff and not a stop.**

## Since the checkpoint — four more waves, and three of them cut AGAINST the lead

**All landed on canonical `main`.** Gates green at every landing.

1. 🔴 **`TX-004`'s only supporting experiment is weaker than it looked.** `A51` is almost certainly
   **BTX-A51 — a CK1α / CDK7 / CDK9 inhibitor, not a MYC inhibitor** (Phase I verified at source by
   the Orchestrator; Ben-Neriah at the same institution as the Aqeilan lab; identification stays
   `INFERENZA`). Its Phase I PD readout is **reduced RNA Pol II phosphorylation** — a CDK9
   elongation effect for which MYC is the *readout*, not the target. **`TX-004` names a target its
   only reagent does not have.** And CK1α is the β-catenin **priming** kinase, with an independent
   study reporting **increased** β-catenin under the compound — the **opposite** direction from the
   one `TX-004` requires (one paper, abstract level, virus-infected cells ⇒ **FLAG, not
   refutation**).
2. 🔴 **And the schedule indicts the experiment itself.** Continuous CDK9 inhibition causes
   developmental adverse effects; a **two-hour window avoids all of them**; `AZD4573` was
   independently engineered for *transient* engagement. **`A51` was given to the organoids
   continuously for seven weeks — the regimen this literature flags as harmful.** ⇒ the `SOX2⁺`
   fall 60→33 % with layer markers unmoved **cannot be distinguished from an anti-proliferative
   effect** on the published data (no proliferation index, no death readout). *Under test in the
   open wave.*
3. 🔴 **`PMID 30853297` is genuinely blocked** — seven routes, each measured. `CLAIM 018` remains a
   `consolidated baseline` resting on an abstract, and that debt is documented, **not discharged**.
4. ✅ **Table S1 is unreachable from here** (403 on both PMC hosts, `EGRESS_BLOCKED`, deposit ends
   with two file names and no content) — **but the body came back**, Table 1 was reconstructed with
   its alignment established against three anchors, and the Operator's question is answered in
   [`oliver2023_table1_independent_reconstruction_20260921.md`](oliver2023_table1_independent_reconstruction_20260921.md):
   **the descriptive imbalance is real, the log-rank is as reported, and the survival inference
   does not carry to an individual** — syntactic exposure variable the authors decline to validate,
   flagship allele on both tails, two strata pooled that differ in ascertainment *and* composition
   (23 % vs 38 % mortality, 8 y 2 m vs 3 y 4 m mean age), and censoring that is **age at
   publication, not follow-up**.
5. 🔵 **A flag that would have undermined two of our own planned experiments does NOT hold.** A
   passage suggested WWOX is not expressed in blood or skin fibroblasts, which would have made
   `DL-BIO-003` and `HYP-20260709-08` uninterpretable. **`CLAIM 019` settles it**: Johannsen
   measured **WWOX transcript at normal levels in patient fibroblasts by qRT-PCR**. Both experiments
   stand.
6. 🟢 **New and reachable:** `FT-125` — `PMID 36537114` is **already read with a receipt** and
   carries a heterozygous `Q230P` brother dead at 10 years, a *de novo* intronic **`GRIA4`** variant
   (a gene absent from this repository), and a `Q230P` + 36.3 kb exon-5 deletion genotype. **No
   acquisition required.** *A receipt records that a paper was read, not that everything in it was
   extracted.*
7. 🔴 **Two instrument defects, both in the token class this repository is most fragile on**
   (`FT-126`): the Scholar Gateway surface **silently deletes hyphens and asterisks inside variant
   strings** (`c.606-1G>A` → `c.6061G>A`) — **the `+5`→`−3` class**, so that surface is **refused**
   for variant coordinates; and `lookup_article_by_citation` transposes `pmid` and `key`.
8. 🔴 **A third error of mine, same class as the other five:** I called two DOIs absent on
   `convert_article_ids` alone. **Both exist** — `10.1016/j.ejpn.2019.02.003` and
   `10.1002/ajmg.a.63074` — and two other routes return them. **A missing identifier from one route
   is not an absence.** Caught by Scientist A, against my own brief, for the second time.
9. 🔵 **Credit, twice:** the `Q230P` both-tails datum was **already in `CLAIM 019`**, and the
   *"severe without being deterministic for early death"* reading was already in `CLAIM 030`'s
   2026-09-09 note. **LEGEND wrote both first.** A sixth instance of the session's structural
   pattern in a new form — **existence in the wrong place**, a finding filed under one claim that
   another claim's analysis needed, with no link between them.

---

## 🔴 BRANCH AND LEDGER RECONCILIATION — measured 2026-09-21 on Operator instruction

Two anomalies were raised and both are now resolved by measurement. **Neither was a loss.**

### 1 · The branch was NOT stale, and canonical `main` is now current

| Ref | SHA | Receipts |
|---|---|---|
| `origin/main` **before** this reconciliation | `9a20920` | 188 |
| `origin/main` **now** | **`89f36db`** | 188 |
| this branch | `89f36db` (identical) | 188 |

`9a20920` **was** an ancestor of this branch's HEAD — the work was based on current canonical main
throughout. All **16** commits are now **on `main`**, landed by fast-forward.

⚠️ **Two traps a later reader will hit unless warned.**
- 🔴 **The local `origin/main` tracking ref was STALE at `83ec6be`** and `git fetch` reported a
  `forced update` `83ec6be…9a20920`. **Do not trust the tracking ref here; read the remote**
  (`git ls-remote origin refs/heads/main`).
- 🔴 **This clone is SHALLOW** (`.git/shallow`, 2 grafted roots; `main` depth 50, HEAD depth 65), so
  **`git merge-base` returns "no common ancestor" between lineages that genuinely share one.**
  That is a truncation artefact, **not** unrelated histories, and it is exactly the sort of proxy
  reading this run got wrong five times elsewhere.
- `83ec6be` (156 receipts) is **not unique material** — it is an ancestor of the live remote
  branches `claude/legend-architecture-evaluation-zovohw` and `claude/wwox-next-scientist-batch-n74f0z`.
  Tagged locally as `preclone-main-83ec6be` anyway; nothing was deleted.

### 2 · 188 vs 200 is a CONCURRENT SIBLING SESSION, not a missing-receipt defect

**`claude/legend-autonomous-woree-tv6gz8` = `f7595f6`, 200 receipts, anchor 200, committed
2026-09-21 19:51.** It branched from the same `9a20920` and appended **12** events.

> ✅ **Verified by byte comparison: their first 188 lines are identical to this branch's 188.**
> Their 200 is a **strict superset**. The chain did not fork; it was extended by one side only.

🔵 **And the merge is safe in either order, for one specific reason: this run persisted ZERO
receipts.** `git diff 9a20920..HEAD` over
`fulltext_read_receipts.jsonl`, `state_manifest_current.md` and the **four canonical scientific
current files** returns **empty**. Only one side ever changed the ledger or the anchor, so git
resolves both cleanly and **no hash chain is at risk**.

**Order of operations for whoever lands the sibling:** merge `main` into `tv6gz8` (or rebase it),
keep **its** ledger at 200 and **its** manifest anchor at 200, then push. **Do not** regenerate,
re-anchor or "fix" the ledger to make counts agree — the counts are supposed to differ until the
12 events land.

⚠️ `main` is **not** an ancestor of `f7595f6`. That session still owes a merge.

---

## 🔴 OPERATOR BOUNDARY on the structural findings — recorded so it is not overstepped

The run surfaced a class of *existence-without-record* defects: **29** read and receipted papers
with no `PAPER` record · **16 of 34** locator counts wrong (all understating) · seven "anchor"
papers on no recorded reading · `CLAIM 032`'s unsourced hypomorph · `CORPUS P306`'s tier · a
harvest-to-registry gap estimated near **304 of 706**.

> **The Operator's instruction, 2026-09-21: DO NOT start the previously fenced-off broad
> registry ↔ ledger reconciliation.** Instead: **(1) document the class · (2) repair only defects
> directly encountered by current scientific work · (3) continue science.**
> **A systematic audit remains a separate Operator decision.**

**What this permits, and it is narrower than it looks.** `CORPUS P306` was repaired because the
enzymology node hit it. `PAPER 025` is proposed because the `c.517-2A>G` work hit it. The sixteen
locator counts are proposed as **one mechanical re-derivation with the derivation shipped**, not as
an audit. 🔴 **The 29 and the ~304 are DOCUMENTED AND NOT ACTIONED** — they are written up in
[`harvest_to_registry_gap_20260921.md`](harvest_to_registry_gap_20260921.md) and
[`anchor_papers_without_readings_20260921.md`](anchor_papers_without_readings_20260921.md) and
**nothing was created for them.**

⚠️ **The specific temptation to refuse:** bulk-creating placeholders for the ~304 harvested records
would make `unread_gold.py` report three hundred items of "gold" nobody has judged — **manufacturing
exactly the false coverage the finding is about.** It was refused once already this run and should
be refused again.

---

## The second run in one screen

**Branch:** `claude/wwox-woree-autonomous-scout-paqlty`, pushed. **Gates at every landing:** LINT
PASS · publication gate PASS / 0 blocks · receipts **188** chained and tail-anchored · growth
anchors PASS · `unread_premises` **0/0** (it went above zero four times and was driven back each
time by declaring the debt, never by removing the citation).

**Node selection.** A fresh scout rejected re-running the previous scout's proposed wave and chose
two nodes on expected therapeutic information gain: `MECHANISM_WWOX_SDR_FUNCTION_AND_MISSENSE_RESCUE`
(the blocker on `TX-003`) and `MECHANISM_DOWNSTREAM_WWOX_INDEPENDENT_RESCUE` (the only class with a
short path for null/null). Both ran four waves; a third and fourth node followed from what they
found. **Two Scientists, never more, as instructed.**

### The six results that change something

1. 🔴 **`TX-007` has a measured efficacy FLOOR and no measured CEILING.** Two doses 2.1× apart give
   opposite survival outcomes while being `ns` on vector genomes and mRNA in **7 of 8** regional
   comparisons — the minimum effective dose is bracketed **in capsids, not in biology**. Expression
   at P300 is **regional, not scalar**: forebrain 5–11× wild type, **cerebellum 1.4× and 0.6×** —
   the therapy under-doses the ataxia organ at every dose and timepoint. `WPRE`, removed as *"a
   proactive risk-mitigation step"* against *"no overt toxicity was observed"* (**a non-observation,
   not a safety result**), was the element that most boosted cerebellum. **No published experiment
   asks whether excess WWOX harms a neuron** — the census returned two records, both now opened,
   neither asks it — for a tumour suppressor whose induction is pro-apoptotic, delivered for life
   by a vector scored `REVERS 0`, with **no tumour surveillance** in the dose study.
   → `CC-20260921-TX007-CEILING-AND-DOSE-CONTROL-01` (proposes `SAFETY 1–2` → **1**).
2. 🔴 **An assay of WWOX catalysis exists and was filed as background.** `PMID 21476439` (2011,
   Lodz) measured steroid-substrate dehydrogenase activity with NAD⁺/NADP⁺ and **Km values** —
   oxidation only, no reduction. It sat as `CORPUS P306`, Tier C, `background only`, unread.
   **Orphaned, not overturned**: Bednarek's own 2025 retrospective has zero occurrences of
   substrate/Km/cofactor/NAD/steroid/retinal and reframes the SDR as an interaction surface. A 2015
   **review** proposes a *retinal* oxidoreductase acting **reversibly** — contradicting 2011 on the
   one property an assay must choose. **An assay of function *per molecule* still exists nowhere,
   for any allele.** → `CC-20260921-WWOX-ENZYMOLOGY-P306-01`.
3. 🔴 **The developmental headline is a looking limit, not an onset.** Earliest mammalian
   examination **E12.5** — already abnormal. Earliest human tissue **GW21** — already abnormal.
   Holoprosencephaly and embryonic deaths on the record, never followed up. **Prenatal WWOX
   interventions: zero.** Every portfolio therapy acts at or after spontaneous seizures; the
   `P0–P5` window opens ~2 weeks after the first measured lesion.
4. **Domain F closes with a negative and one live residue.** Every survival outlier is explained by
   allele class or by ascertainment; **no discordant sibling pair exists**; WWOX has no paralogue;
   **no modifier has ever been identified in any species.** 🔵 **The residue:** the allele-class
   rule's mechanism is **not** residual protein — Q230P abolishes protein on western blot and
   homozygous Q230P patients are the longest survivors in two cohorts. Same question as `TX-003`,
   arriving from the opposite direction, now with a human survival statistic on it.
5. **Ethosuximide is the only genotype-specific pharmacological result in the WWOX animal
   literature** (`n.s.` in `+/+` and `+/−`, significant in `−/−`, 150 mg/kg i.p.) — and lithium, in
   the same figure, suppressed **all three** genotypes including wild type. The floor-effect
   objection dies on that same panel. **Bounded and not promoted:** the mouse discharge has never
   been characterised (`Hz` = 0 occurrences in a body read in full), there is **no T-type calcium
   evidence in WWOX deficiency at all**, the human picture is **not** absence epilepsy, and
   ethosuximide has already been given to a WWOX patient with no sustained effect.
6. **`TX-001`'s RNA question is closed on public data.** `GSE156243` has the right instrument and
   the **wrong cells** (WT vs engineered KO — zero molecules of any patient splice allele); the 2026
   dataset has the right cells, no established accession, and droplet chemistry that cannot reach a
   mid-gene junction.

### Structural findings — five instances of ONE pattern
`CLAIM 032`'s unsourced hypomorph · `CORPUS P306`'s tier · seven "anchor" papers on no recorded
reading · **16 of 34** locator counts wrong (**all understating**) · **29** papers read, receipted
and never given a `PAPER` record.
> 🔵 **Every LEGEND check verifies a record against itself. Nothing verifies that a thing which
> exists HAS a record.** All five were found by hand, while chasing something else.

### 🔴 Errors this run made, caught, and recorded
Five first measurements were wrong because a **proxy** was measured instead of the thing (an
identity index; `len()` on a dict; a record-id prefix). **Twice a DOI was reconstructed from memory
instead of copied** — both caught before landing. **Two alleles were conflated in a delegate brief**
— `c.517-2A>G` is exon 6, `c.1057-2A>G` is exon 9 and the **last** exon; opposite NMD regimes;
Scientist A caught it. The publication gate **blocked a batch over a living researcher's e-mail**
in a delegate's file — correctly; removed.

### Candidates PROPOSED this run — none propagated, none a blocker
`CC-20260921-CLAIM032-HYPOMORPH-PREMISE-01` · `-WWOX-ENZYMOLOGY-P306-01` ·
`-TX007-CEILING-AND-DOSE-CONTROL-01` · `-PAPER025-IDENTITY-01` · `-SUPERSEDED-TEXT-POINTERS-01` ·
`-LOCATOR-COUNT-REDERIVATION-01`. ⚠️ **`D-17` is RESERVED** (operator-deferred); these propose
`D-18`–`D-23`. **Do not renumber into `D-17`.**

### Harness changes landed at T0 (regression-backed, mutation-tested)
`unread_gold.py` — both field spellings, a **catalysis** clause, a **substrate-class** clause, and a
**receipt-ledger cross-check** (19 stale rows now annotated rather than silently re-dispatched);
13 tests, 5 fail on revert. `locator_count_crosscheck.py` — new, routed, 10 tests, 3 fail on revert.

### Where to resume
1. **`FT-117` / `PMID 30853297`** — highest-value unread: carries a **measured** exon-6 skip **and**
   is a `Q230P` primary; `CLAIM 018` (`consolidated baseline`) rests on it at abstract depth.
2. **`FT-114` / `PMID 41442931`** — the only **safety** anchor standing on no reading. Ask for the
   pre-vigabatrin MRI, the dose/duration, and any de-challenge.
3. **`FT-118` / `PMID 25866966`** — the Angelman age-of-restoration design; windows are
   **phenotype-specific within one gene**, which is the shape `TX-007`'s ceiling question needs.
4. **`A11` / `PMID 21476439`** — three content-named asks (Km table; protein-prep Methods and
   whether any catalytically-dead control; whether any retinoid was screened).
5. The **29** read-but-unrecorded papers — `36828035` and `30356099` first; each resolves a defect
   already written into a candidate.

⚠️ **Run-ending condition:** a Scientist agent terminated on an **API session rate limit**, and the
literature MCP dropped and returned. That is `HARD_RESOURCE_LIMIT` territory, **not** a scientific
stop — every node above is still open and every route above is still live.

---

# Autonomous session — continuation state (FIRST run, 2026-09-21 — retained verbatim)


**Updated:** 2026-09-21 · **Purpose:** recovery point. If this session is interrupted, a cold reader
resumes from here. **Not a handoff and not a stop.**

## Current state — 2026-09-21, end of the autonomous continuation

- `main` == `origin/main` · working tree clean · LINT **PASS** · publication gate **PASS, 0 blocks**
  · receipts **186 chained, tail anchored** · growth anchors **PASS** · `session_self_eval.py`
  **PASS** · release regressions exit 0 (every non-pass a declared environment absence).
- 🔴 **`UNREAD_PREMISE` ratchet: 2 → 0.** For the first time this repository leans on **no** paper
  that nobody has opened. Manifest baseline lowered to match; `growth_anchors` reports
  `RATCHET_IMPROVED`.
- 🔴 **The accessible reading queue is EMPTY, and that is measured rather than assumed.** Every
  copyright-verified open paper carrying no receipt has been read. What remains is **human
  acquisition**: packet items `A1`–`A9`, each with its route tried and recorded.
- **Read and receipted in this continuation (13 events over 11 papers):** `21766012` (+ correction)
  · `25650666` (adversarial re-read) · `27845895` · `25238782` · `24008736` · `41124647` ·
  `35573960` · `39101447` · `33134515` · `35328751` · `36271927` · `27869163`.
- **Tools shipped, both routed and regression-backed:** `scoped_record_edit.py` (16 tests) ·
  `extraction_damage_report.py` (11 tests).
- **Self-evaluation:** Parts 1–3 complete —
  `research/session_evaluations/2026-09-21_orchestrator_autonomous_continuation.md`.
  **Capability scout:** appended to `research/capability_scout_log.md` with the host-keyed preflight.

### The corpus-wide measurement, so nobody re-derives it

`extraction_damage_report.py` over all **29** local artefacts:
**29/29 italic-class counts INADMISSIBLE · 29/29 reference list ABSENT.**
So **no italic-class zero from any local artefact has ever been admissible as evidence**, and **no
citation attribution has ever been traceable from one**. Run the tool before offering any count.

## ✅ BATCH_20260921_001 — the four parked candidates are LANDED (2026-09-21)

**Operator-approved, propagated, `WM_v4.4 → WM_v4.5` (MINOR).** No claim reversed, no status
changed, no other pending candidate dragged in. **`D-17` deferred by the Operator and excluded.**

| Candidate | Canonical effect |
|---|---|
| `CLAIM032-ENDPOINT-QUALIFIER` | Title, Summary and dose corollary now name the endpoint class actually measured; `PREMISE: NOBODY_LOOKED` on cognition, EEG, network excitability. **State: «evidence insufficient for a general conclusion of no phenotype»** — and it still does not demonstrate disease in carriers. *"three independent laboratories"* **not propagated**. |
| `DETECTION-FLOOR` | `CLAIM 030`: *proteina assente* → *proteina non rilevata al Western blot*, `PREMISE: DETECTION_FLOOR`, aligned to `CLAIM 019`. |
| `CLAIM039-CEREBELLAR` | Title narrowed to the light-microscopy endpoint; boundary records that **neither stream establishes nor excludes** a cerebellar contribution. **Stays a rat-model claim**; human MRI not imported. |
| `PAPER34140629-PROMOTION` | `CORPUS-STUB-150` → **`PAPER 096`**, `T3`/`LOW`, generating no claim. |

**BLOCK 2 mirror rows 032 and 039 moved with their claims** — the defect the working model's own
previous last-update note recorded. Growth delta declared (`papers +1`). `batch_queue.md`
regenerated against the committed registries.

⚠️ **Remote housekeeping is BLOCKED BY TOOLING**, not by policy: deleting
`origin/claude/wwox-next-scientist-batch-n74f0z` (0 commits not on `main`) fails with
`send-pack: unexpected disconnect` on every attempt through this proxy. A second fully-merged
branch, `origin/claude/legend-architecture-evaluation-zovohw`, is also present and **was not
touched** — no authorisation was given for it.

---

## 🔴 The three results a cold reader should know before anything else

1. **Every therapeutic candidate this literature has produced acts by ANTAGONISING WWOX**, and an
   independent laboratory now says so in neurons. `PMID 35984507` (Coimbra, outside NCKU):
   *"**WWOX inhibition** by Zfra1-31 **restores** mitochondrial homeostasis and viability of
   neuronal cells exposed to high glucose."* With the pTyr33 peptide (`18371080`: *"activated WOX1
   plays an essential role in the MPP+-induced neuronal death"*) and the C1q axis (`19484134`:
   *"C1q activates WOX1 in neurons, which ultimately leads to cell death"*), that is three lines.
   **A WWOX antagonist has nothing to antagonise in a WWOX-deficient brain. This is a category
   objection, not a dosing one.**
   🔴 ~~Packet item `A9`; rests on an abstract, so it must be *read*.~~ **`A9` HAS NOW BEEN READ —
   2026-09-21, operator-supplied PDF + supplementary**
   ([`A9_fulltext_read_20260921.md`](A9_fulltext_read_20260921.md); `FTR-20260921-35984507-01`,
   `-02`), **and the reading narrows this bullet.** There is **no genetic WWOX arm**, **no
   inactive-peptide control**, and **total WWOX was never reported** although `ABN413` is in the
   methods and the blots are normalised to β-actin. So `35984507` shows that **Zfra1-31 is
   protective in neurons and lowers pY33-WWOX** — *not* that inhibiting WWOX is. And line 1 of the
   three appears *inside* `35984507` only as a citation to its ref [18], so under `D-15` it is not
   a second observation. **The category objection is unchanged and firmer** — inhibition and
   substrate-consumption point the same way in a genotype short of functional WWOX — but the
   sentence that carries it must now be the narrow one.
2. **The first node of the Chang cascade disclaims its own load-bearing step.** `25650666`'s
   Discussion asserts TGF-β1 dissociates WWOX from TPC6AΔ and, two paragraphs later, says
   *"Whether TGF-β1 regulates the binding of WWOX with TPC6AΔ **is unknown**"*. There is **no
   binding assay in the paper**. And `TRAPPC6AΔ` and `TIAF1` are **one measurement, not two**.
3. **All four levers the model cared about were finally tried in a WOREE null, and all four
   failed** (`35573960`): vigabatrin, ACTH, CBD oil, ketogenic diet. `n = 1`, null/null,
   day-one onset — **not a refutation for a genotype with residual protein**, and the ledger
   says so.

## Completed programme so far
1. **`SCIENTIST_CHANG_NS_…` waves 1–5** — closed, formally saturated.
2. **Fallback queue P1–P5** — closed.
3. **Open-ended continuation** (current) — dynamic queue, regenerated at each boundary.

## Standing commit candidates — `PARKED_PENDING_OPERATOR`, do not re-litigate
| Candidate | Class | One line |
|---|---|---|
| `CC-20260920-CLAIM032-ENDPOINT-QUALIFIER-01` | MINOR | `CLAIM 032`'s cognition leg is *nobody looked*; headline quote is a tumour sentence |
| `CC-20260920-DETECTION-FLOOR-01` | MINOR | `CLAIM 030` says *proteina assente* where `CLAIM 019` says *non rilevata*; proposes `D-17` |
| `CC-20260920-CLAIM039-CEREBELLAR-01` | ORDINARY | *not cerebellar* rests on one hedged sentence; a P1 contradiction was read and never landed |
| `CC-20260920-PAPER34140629-PROMOTION-01` | MINOR | `CORPUS-STUB-150` → `PAPER 096` |

**None is a session blocker.** Revisit only if new evidence materially changes one.

## Live findings a cold reader must not re-derive
- **Six abstract-versus-results inversions** across six papers: `32764489` (brain engagement),
  `29067327` (Zfra pY33), `25650666` (null rendered temporal), `31543760` (p=0.0626 conjoined),
  `42092735` (neurotransmitter studies "normal" when never obtained), `25649963` (breast-cancer
  similarity unsupported). **In this literature the abstract does not index the results.**
- **Normal by blunt instrument, abnormal by sharp one** — four instances. Proposed as `D-17`.
- **The heterozygote phenotype is inside the control groups**, not missing from the literature.
- **Two "read but never landed" locators** (`CLAIM 016` lithium, `CLAIM 039` cerebellar) plus three
  more found in the narrow audit (spontaneous het tumours ×2, het bone deficit).
- **Zfra / all WWOX peptides: DISMISSED for WOREE.** No brain engagement; never dosed in a
  WWOX-deficient animal by anyone.
- **Lithium: DOWN.** One record in all of PubMed; no GSK3β inhibitor ever used in any WWOX context.
- **SDR missense readout: NO.** Nine of nine candidates fail on "would the protein even be there?"
- **`DL-MECH-021` lowered** medio → basso; domain-sufficiency arc demoted to author assertion; the
  seizure bridge withdrawn as a category transfer. **The platform survives.**

## Method rules earned here — apply, do not rediscover
- **Never grep `paper_registry_current.md` or `literature_tracking_log_current.md`** — use
  `registry_records.py`.
- **The MCP extractor elides gene lists into empty commas.** An abstract read through it is not a
  reliable index of a paper's content. *(This bit us on `PMID 41153369`, against our own registry.)*
- **No figure panel is inspectable in this environment.** No JATS, no PDF tooling, egress denied to
  NCBI/EBI/publishers. Per `D-14`, no figure-asserted negative may be adjudicated here.
- **A paper can be in PMC and outside the OA subset** — that is a permanent licence wall. Check
  `get_copyright_status` before re-queuing.
- **The broad `landing`-field audit is a definitional artefact** (74/81) and expands into the
  fenced-off mass reconciliation. Run that screen only against a specific claim under question.
- 🔴 **An identifier or a byline enters a durable record only by copy, in the same act, from a
  verified source — never from recall and never from a delegate's prose.** This failed **twice in
  two days**, both times mine, both times against a repository that already held the correct value:
  `FT-108` was written with `CORPUS P331` and "Hsu L-J … Chang N-S" (correct: `CORPUS P330`,
  first author **Hong Q**), and `FTR-20260921-21766012-01` was written with "Houlihan LM, Harris SE,
  Luciano M" (correct: **Hamilton G**, Harris SE, Davies G, Liewald DC, Tenesa A, Starr JM,
  Porteous D, Deary IJ — the queue entry and the analysis file both had it right). Corrected by
  append in `FTR-20260921-21766012-02`.
- 🔴 **Never re-fetch an article to a path an existing receipt already fingerprints, and check the
  ledger for the PMID before dispatching a read.** `PMID 25650666` was re-fetched to
  `files/fulltext/PMID25650666_PMC_MCPtext.txt` on 2026-09-21; the bytes changed
  (`9635516b…` → `c6e336a9…`) and the original is **unrecoverable**, because `files/` is in
  `.gitignore` and the artefact was never under version control. The earlier reading stands — its
  quotations are all present in the current artefact and were re-verified — but its fingerprint no
  longer binds to a file. Declared in `FTR-20260921-25650666-02` rather than quietly re-anchored.
- 🔴 **A DELEGATE'S CENSUS DESCRIBES THE FIELD, NEVER THIS REPOSITORY — and this cost three
  corrections in one day.** A census that says *"nobody has done X"* or *"paper Y is unread"* has
  measured PubMed, not LEGEND. **Before acting on any such statement, check the receipt ledger AND
  the discovery and therapeutic ledgers.** Today: `FT-102` was re-read a day after it had been read
  (stale queue entry); the two AAV9-SynI-WWOX papers were reported unread while carrying **four and
  seven** ledger events; and the oligodendrocyte-autonomy question was reported open while
  `DL-MECH-031` had settled it and `HYP-20260709-07` had been **parked** on it in July. **When a
  delegate chooses which paper to read, the ledger check must be written into the brief** — the
  Orchestrator cannot pre-check a paper it has not yet named.
- 🔴 **`is_open_access: false` is often a NOT-CHECKED reading, not a paywall.** Look at
  `checked_sources`: if it is `["pubmed"]` alone, PMC was never consulted and the flag means
  nothing. **A PMCID existing is not evidence of retrievability either** (`PMC4935222` and
  `PMC6965410` both resolve and both return a zero-length body). **Retrievability is established
  only by attempting the fetch and measuring the body length.** Both halves of this rule cost this
  session real work before it was written down.
- 🔴 **INTERROGATIVE-TO-DECLARATIVE RE-VOICING — a citation-fidelity failure mode that string
  comparison cannot catch.** A source's *question* is quoted accurately and re-attributed as its
  *finding*. Every content word matches, so quote-matching and grep find nothing; only reading the
  sentence's **grammatical mood** catches it. Found on `PMID 25238782`, whose abstract asks
  *"a question that emerges is whether fragility in these regions is only a structural 'passive'
  incident…"* and which was cited as having *concluded* that it is *"unlikely only a structural
  'passive' incident"*. **When auditing a citation, check the mood of the sourced sentence, not
  just its words.** Distinct from the seven abstract-versus-results inversions recorded here, which
  are contradictions *inside* one paper.
- **A stale queue entry will dispatch duplicate work.** `FT-102` still read *"non acquisito"* a day
  after the paper had been read. Close a queue entry in the same cycle as the read, not later.
- **A zero string count for a gene symbol in MCP body text is an instrument reading, not a
  negative.** Demonstrated conclusively on `PMID 21766012`: `TRAPPC6A` occurs **zero** times in the
  body — as do `APOE`, `APP`, `BIN1`, `CLU`, `PICALM`, which the paper is entirely about — while the
  symbol **survives intact in the PubMed metadata abstract**. The extractor deletes italicised
  tokens. Under `D-15`, never let such a count carry a negative; rest the conclusion on study
  design stated in Methods, or on prose you can quote.

## Next queue, ranked (as of this write)
0. **Landed this cycle:** `FT-102` / `PMID 25650666` (adversarial re-read — internal contradiction
   on the load-bearing binding step; human arm is an age-confounded null; TPC6AΔ and TIAF1 collapse
   to **one** node) and `FT-073` / `PMID 27845895` (the DisMech quote is real but is the strongest
   of four statements, and the axis **attenuates** death when WWOX is scarce). `DL-BIO-004` and
   `DL-MOL-008` updated; `PMID 18371080` added to the acquisition packet as **A6**.
1. ~~**FT-090** / `PMID 25416187`~~ — **CLOSED, `EVIDENCE_BLOCKED` (licence).** `PMC4935222` is a
   metadata-only stub (`full_text:""`, `is_open_access: false`, `found_in_pmc: 0`). **But the
   question that mattered is answered from metadata: `27551470` cites a REVIEW as evidence**
   (`article_types` includes `Review`; *"The aim of this review is to summarize…"*). The chain does
   not bottom out there — it passes through. Acquisition debt `A7`; **ask for the reference list,
   not the body.**
2. ~~**FT-018** / `PMID 28123895`~~ — **NOT ACCESSIBLE.** The surface census already records it as
   `idIsNotOpenAccess` / `pdf_only`. Do not re-dispatch; it is acquisition work.
3. ~~**FT-098 / FT-099** — the other two independent `TRAPPC6A` cohorts.~~ **CLOSED.** `FT-099`
   read (fails its own permutation); `FT-098` licence-walled. With `FT-097` already null, **all
   three legs of the `TRAPPC6A` node-independence claim are down and the claim is retracted in
   full** — see the retraction appended to `chang_ncku_wave2_node_independence_20260920.md`.
4. ~~**FT-092** / `PMID 25238782`~~ — **CLOSED, read.** The 2016 framing is the faithful one: the
   chapter **proposes**, it does not conclude, and the phrase attributed to it is its **question**.
   Named the re-voicing failure mode above.
5. ~~**FT-074** — four mTOR/autophagy stubs two reasoning files already lean on.~~ **PARTLY
   CLOSED, and the standing negative is FALSIFIED as stated.** `24008736` read: it **fixes** the
   sign (WWOX ⊣ autophagy), four times, including a **germline `Wwox`-knockout MEF arm** that is
   loss-of-function, drug-free and non-cancer. The narrowed form that survives: the direction **is**
   fixed on **steady-state autophagy-protein abundance**; it is **not** established on **flux**
   (no clamp was ever applied to a WWOX manipulation, and the paper's own MG132 result shows LC3 is
   being degraded proteasomally in that system), **not** established in neural tissue, and the
   **mTOR-mediated route is asserted, never tested**. The two-directions standoff now reduces to
   **one** discordant paper, `36621327`, whose acquisition priority rises above the other two.
6. **`PMID 27869163`** (Wwox–Brca1, CC BY-NC-ND) — copyright-verified open, never dispatched.

## Permanently evidence-blocked — do not retry automated routes
`15126504` (`FT-024`, no PMCID) · `27569545` (`FT-105`, **licence wall**, verified) · `15026124`
(no PMC) · `33914858` (no PMCID) · `24369382` (empty PMC body) · `17803050` (no DOI/PMCID).
Packaged for a human in `acquisition_packet_20260920.md`.

**Added 2026-09-21, each verified with `get_copyright_status` and/or `convert_article_ids` — do not
re-test:**

| PMID | Why it is blocked | Where it now lives |
|---|---|---|
| `18371080` | **no PMCID** (record returns the PMID alone); Wiley paywall | `FT-109` · packet **`A6`** |
| `25416187` | PMCID **`PMC4935222` exists but is a metadata-only stub** — `full_text:""`, `is_open_access:false`, `found_in_pmc:0` | `FT-090` · packet **`A7`** |
| `26345274` | **no PMCID** | `FT-032` · packet **`A8`** |
| `33134515` | licence wall | `FT-098` |
| `33300063` | ⚠️ **weaker than first written — see the correction below** | `FT-074` |
| `31966718`, `36621327` | verified unobtainable earlier in this session | `FT-074` |
| `30094525` | ⚠️ **weaker than first written — see the correction below** | `FT-032` |
| `11719429` | ⚠️ **weaker than first written — see the correction below** | `FT-032` |
| `17360458` | `PMC1820689` exists, PNAS 2007, **not OA-licensed**; a local PDF exists but **this checkout has no PDF tooling** | `FT-032` |
| `28123895` | `PMC5214935`, `idIsNotOpenAccess` / `pdf_only` per the surface census | `FT-018` |

🔴 **CORRECTION TO THE THREE ROWS MARKED ABOVE, made the same hour, against myself.**
`is_open_access: false` is **not** a statement that a paper is paywalled. For `33300063`,
`30094525` and `11719429` the tool returned `source: "not_available"` with
`checked_sources: ["pubmed"]` — **PMC was never consulted**, so the flag records *what was not
checked*, not *what is not there*. Demonstrated within this session: `41124647` returned
`is_open_access: false` with `checked_sources: ["pubmed"]`, and its body then came back **in full at
68,491 characters**. Those three rows are therefore **not verified blocked**; they are *untested*.
The authority on whether a PMCID exists is **`convert_article_ids`**, and the only authority on
retrievability is **attempting the fetch and measuring the body length**. The rows that ARE verified
are the ones where `checked_sources` includes `pmc`, or where a fetch was attempted and returned an
empty body.

⚠️ **The stub trap, stated once so it is not rediscovered:** a **PMCID existing does not mean a body
exists**. `PMC4935222` resolves, round-trips through `convert_article_ids`, and returns HTTP success
with `"full_text":""`. **Check `get_copyright_status` for `found_in_pmc` and `is_open_access` before
dispatching a read**, and treat an empty body as a licence wall, not a transient failure.

**Copyright-verified OPEN and still unread:** `27869163` (Wwox–Brca1, CC BY-NC-ND 4.0, PMC5398941) ·
`35573960` (Front Pediatr 2022, `PMC9100683` — the tool reports `is_open_access:false` with a null
licence field, but Frontiers deposits full text, **so this one is worth exactly one fetch
attempt**).
