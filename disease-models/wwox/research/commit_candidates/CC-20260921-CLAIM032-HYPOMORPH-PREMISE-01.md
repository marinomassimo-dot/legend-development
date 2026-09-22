# COMMIT CANDIDATE — CC-20260921-CLAIM032-HYPOMORPH-PREMISE-01

**Source:** not a reading — **no reading was possible**. An unsourced premise inside a canonical
claim, found by the Orchestrator while scouting modifier/resilience biology, and verified against
PubMed metadata plus LEGEND's own verified locator manifest. Full audit:
[`hypomorph_threshold_premise_audit_20260921.md`](../../analysis/hypomorph_threshold_premise_audit_20260921.md).
**Ledger:** `fulltext_receipts.py verify` → **OK: 188 chained receipt(s), tail anchored**.
**LINT at drafting:** PASS · **release gate:** PASS / BLOCKS 0 · **growth anchors:** PASS.
**Change class:** **MINOR** — one sentence narrowed inside one claim, one `Source` line corrected,
one acquisition entry, one ledger row. **No claim reversed. No status changed. No block redefined.**
**Target:** `working_model_version` MINOR bump at batch time. No `BLOCCO 1` change.
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R2.** `CLAIM 032`'s conclusion for heterozygotes is unchanged and its status
(`in observation`) does not move. What is removed is an **extra inference below 50 %** that the
claim's own `Source` line never supported. `legend-locator-audit` (R4) does not apply: no
`consolidated baseline` claim is narrowed, and the premise being removed **has no locator to audit**
— that is the defect.

---

## 1 · The premise, and the four things wrong with it

`CLAIM 032`'s Summary ends:

> *«Inoltre, il topo **ipomorfo** `Wwox^gt/gt` (proteina bassa **ma rilevabile**) è **vitale**,
> mentre il null muore a 3-4 settimane ⇒ **la soglia fra letale e vitale sta sotto il 50%**.»*

| # | Defect | Evidence |
|---|---|---|
| 1 | **No source.** `CLAIM 032`'s `Source` line names `PAPER 053`, `021`, `043`, `045`, `049`, `042`. The hypomorph paper is **not among them**. The datum enters through a **review** (`PAPER 053` = Aldaz 2014). | `claim_registry_current.md`, `CLAIM 032` `Source` line |
| 2 | **The primary is unread, and unreadable from here.** `PMID 17823927` (Ludes-Meyers 2007, *Genes Chromosomes Cancer* 46(12):1129–36). `fulltext_receipts.py status --pmid 17823927` → `[]`. `get_full_text_article(["PMC4143238"])` → **`"full_text": ""`, 0 bytes**. `get_copyright_status` → `"(c) 2007 Wiley-Liss, Inc."`, `license: null`, `found_in_pmc: 0`. **Third confirmed metadata-only PMC stub.** | verified 2026-09-21 |
| 3 | **The sentence inverts its own abstract.** Verbatim (PubMed metadata, not the PMC extraction, which deletes the italicised genotype token): *"Homozygous Wwox gene-trap mice (Wwox(gt/gt)) had **no detectable Wwox protein in most tissues examined**, although, **a low level could be detected in a minority of tissues**."* The abstract **names none of those tissues and does not name brain**. The same abstract also reports *"a **significantly shorter lifespan**"* and higher B-cell lymphoma incidence — so *vitale* alone is not faithful. | PMID 17823927 abstract |
| 4 | **Genotype-class conflation.** `CLAIM 032` is titled and framed around **haploinsufficiency** (one allele). `Wwox^gt/gt` is a **homozygous near-null**. Two classes inside one claim's Summary; the title covers only the first. | §17 genotype-class separation |

**Plus one figure that does not match LEGEND's own read.** The sentence says the null *"muore a 3-4
settimane"*. The complete, receipted, strict-verified read of the **same laboratory's** null
(`PMID 19936220`, `FTR-20260806-19936220-01`) records:

> *"As early as 72 h after birth 43% (15 of 35) of Wwox KOs had died and 77% had died by 17 days
> after birth and no mice survived past weaning"* — `deepdive_manifests/PMID19936220.json`

⚠️ A separate Wwox-null line carries *"letalità postnatale ~4 settimane con ipoglicemia"* in the
discovery ledger. Per §12, two separately published animals are not one animal: **one figure is
standing where LEGEND holds two, from two lines.**

## 2 · Why it is not cosmetic — it is load-bearing on four therapeutic strategies

`CLAIM 032` carries `clinical relevance: VERY HIGH`, and its `Impact on Working Model` reads
*«abbassa la soglia di efficacia richiesta a tutte le leve di ripristino; da riflettere in TX-003 e
TX-007»*. Its Clinical meaning says *«non serve efficienza elevata … un mosaicismo terapeutico
parziale può bastare»*.

🔴 **The heterozygote limb licenses that down to ~50 %. Only the hypomorph sentence licenses it
below 50 %, and that sentence has no source.**

🔴 **And a measured threshold in the therapy's own dose–response points the other way.**
`CLAIM 011` records, from the figure of `PMID 42422765`: **LD = 1.23 × 10¹¹ vg does not rescue
survival; HD = 2.63 × 10¹¹ vg plateaus at ~80 %** — *«non è una differenza graduata su un asse: è
qualitativa»*. A measured vector dose threshold outranks an inference from an unread hypomorph, and
the two disagree. That tension was invisible while the hypomorph sentence had nothing to check.

🔴 **The mechanistic reason the inference does not transfer to brain.** The Wwox-null mouse dies of
a **systemic** crisis — hypoglycaemia, raised BUN and creatinine on LEGEND's own complete reads of
`19936220` and `17803050` — not of brain failure. So *"hypomorph viable, null lethal"* localises a
threshold **for whichever tissue drives postnatal lethality**. If that tissue is among the
*"minority"* that retained protein, the contrast says **nothing** about the neurodevelopmental
threshold. **Direction of the correction: uncertainty goes UP.**

## 3 · What is proposed

**(a) `CLAIM 032` Summary — replace the final sentence** with a sourced, class-separated form:

> ⚠️ **Sotto il 50 % non è stabilito nulla.** L'unico animale vitale con meno del 50 % di WWOX è il
> topo **ipomorfo omozigote** `Wwox^gt/gt` (`PMID 17823927`, Ludes-Meyers 2007) — **una classe
> genotipica diversa da questa claim**, e **mai letto da LEGEND**: `PMC4143238` è un deposito di soli
> metadati (`full_text: ""`), licenza Wiley 2007. Il suo abstract dice che la proteina era **non
> rilevabile nella maggior parte dei tessuti** e rilevabile **solo in una minoranza**, **senza
> nominarli e senza nominare il cervello**, e riporta nello stesso respiro **lifespan
> significativamente ridotta**, atrofia testicolare e maggiore incidenza di linfomi B. *Vitale* non
> è *indenne*. 🔴 `PREMISE: UNREAD_PRIMARY` + `PREMISE: NOBODY_LOOKED` (mappa tissutale della
> proteina residua). **Nessuna soglia terapeutica sub-50 % è sostenuta**, e per il cervello nemmeno
> la soglia di sopravvivenza trasferisce: il nullo muore per crisi **sistemica**
> ([[claim_registry_current#CLAIM 019]] e le letture di `19936220`/`17803050`), non per
> insufficienza cerebrale. `REVIVAL_TRIGGER`: il pannello western per tessuto di `PMID 17823927`,
> o un video-EEG + readout mielinico su `Wwox^gt/gt`.

**(b) `CLAIM 032` `Source` line** — append the attribution that was missing, marked as what it is:

> · `PMID 17823927` (Ludes-Meyers 2007 — ipomorfo `Wwox^gt/gt`) **— ABSTRACT ONLY, nessuna
> ricevuta, primario non recuperabile (`PMC4143238` stub)**; entrato finora nello stato **solo
> attraverso `PAPER 053` (review)**.

**(c) `CLAIM 032` — correct the null's survival figure** to name its line:

> il nullo della **stessa linea e dello stesso laboratorio** muore **prima dello svezzamento**
> (43 % entro 72 h, 77 % entro il giorno 17, nessuno oltre i 21 giorni — `PMID 19936220`, lettura
> completa `FTR-20260806-19936220-01`); *"~4 settimane"* appartiene a **un'altra linea nulla**.

**(d) `full_text_queue_current.md` / acquisition packet** — new entry:

> **`FT-111` / packet item `A10` — `PMID 17823927`.** `EVIDENCE_BLOCKED`, licence wall **verified**
> (fetch attempted, body 0 bytes; `found_in_pmc: 0`; Wiley 2007). **Do not retry automated
> routes.** What to ask a human for: **the tissue western-blot panel and its labels** — *which*
> minority of tissues retained Wwox protein, and **whether brain is among them**. Eight pages;
> resolves a premise standing under `TX-001`, `TX-002`, `TX-003` and `TX-007`.

**(e) `dismissal_ledger_current.md` → `🩸 DEFAULTS THAT BIT US`** — one row:

> **D-18** · *"a premise cited by a review is a premise the repository holds"* · **Why it is FALSE
> here:** `CLAIM 032` carried a mouse phenotype, a protein-abundance statement and a therapeutic
> threshold from `PMID 17823927` for the whole life of the claim, with the paper **absent from its
> `Source` line, absent from the full-text queue, and absent from the receipt ledger**. The
> `UNREAD_PREMISE` ratchet read **0** throughout, correctly: it measures *cited* papers, and this
> one was **used without being cited**. **A premise that is never named is invisible to every check
> built to find unread premises.** `REVIVAL_TRIGGER` / detection rule: when a claim's Summary names
> a **model, allele or animal** that its `Source` line does not account for, that is an unsourced
> premise — check it before the claim is quoted again.

⚠️ **Numbering:** `D-17` was proposed on 2026-09-21 and **DEFERRED by the operator**; it is **reserved, not free**, and is not in the ledger. This session's candidates propose `D-18`–`D-23`, one each. **Do not renumber into `D-17`.**

## 4 · What is explicitly REFUSED

- ❌ **No new gate, auditor, registry or workflow.** Per the operator's §26, a scientific defect is
  repaired by correcting the science and reusing existing mechanism. `D-18` is a **ledger row with
  a detection rule**, which is the existing mechanism.
- ❌ **`CLAIM 032`'s heterozygote conclusion is NOT touched.** ~50 % is tolerated on the endpoints
  measured; `PREMISE: NOBODY_LOOKED` on cognition/EEG stays exactly as landed in
  `BATCH_20260921_001`.
- ❌ **`CLAIM 032`'s status does not move** (`in observation`).
- ❌ **No claim is made about what `PMID 17823927` contains beyond its abstract.** An abstract is
  not a reading, and **no receipt is claimed by this candidate**.
- ❌ **`CLAIM 011` is not edited here.** The tension is *recorded*; resolving it needs the
  intermediate-dose arm `CLAIM 011` already names as its own most informative experiment.

## 5 · Growth delta

`claims +0 · papers +0 · corpus +0`. `CLAIM 032` is modified, not added. `PMID 17823927` enters as a
**queue/acquisition entry**, not as a `PAPER` record — it has no reading behind it and must not
acquire the appearance of one.

---

*Sources retrieved from **PubMed / PubMed Central**.
DOIs — [17823927](https://doi.org/10.1002/gcc.20497) ·
[19936220](https://doi.org/10.1371/journal.pone.0007775) ·
[24932569](https://doi.org/10.1016/j.bbcan.2014.06.001).
Not medical advice.*

---

## Cross-reference added 2026-09-22 — bind this to the CNS qualification candidate

This candidate and [`CC-20260922-GTGT-CNS-QUALIFICATION-01`](CC-20260922-GTGT-CNS-QUALIFICATION-01.md)
are about **the same animal and the same unperformed measurement**, and must be read together so
their wordings cannot drift:

- **This candidate** removes the unsupported generalisation from `CLAIM 032` — *"proteina bassa ma
  rilevabile"* is asserted as a **general property of the `gt/gt`**, whereas the primary says only
  *low level in a minority of tissues*, **naming no tissue and not naming brain**.
- **The CNS candidate** (see its **§1b**) establishes the complementary fact and its correct framing:
  **no published evidence quantifies WWOX in `gt/gt` brain or cerebellum at all.**

> 🔴 **Both must be stated as an ABSENCE OF MEASUREMENT, never as a property of the animal.**
> Neither candidate licenses *"the `gt/gt` has no residual brain WWOX."* That sentence is unsupported
> in exactly the same way as the one this candidate removes — it merely errs in the opposite
> direction.

⭐ **And the retained option value carries across.** The `gt/gt` is disqualified **today** as a
platform for CNS protein rescue, but the disqualifier is **one unperformed Western**, not an adverse
result. A single quantification on `gt/gt` brain and cerebellum would settle **both** candidates at
once: it would tell us whether brain is in the *minority* the abstract refers to, and whether the
animal is a usable `TX-002`/`TX-003` platform.

⚠️ Unchanged and still required by this candidate independently: the *"vitale"* / **"viable to 2
years"** reading must not propagate while the primary reports a **significantly shorter lifespan**.
