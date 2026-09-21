# The `Wwox^gt/gt` hypomorph sentence inside `CLAIM 032`, and the therapeutic threshold it is carrying

**Date:** 2026-09-21 · **Actor:** Orchestrator · **Node:** `MODIFIER_RESILIENCE` / dose-threshold logic
**Status:** non-canonical analysis file. **No canonical file edited.** One commit candidate proposed
separately. **Not medical advice.**

> **Why this was opened.** The operator's brief asks what biology separates severe WOREE from
> unexpectedly mild WWOX deficiency, and — downstream of that — *how much WWOX is enough*. That
> number is the efficacy threshold of every restoration lever in the portfolio (`TX-007` gene
> addition, `TX-002` CRISPRa, `TX-003` proteostatic rescue, `TX-001` splice correction). LEGEND
> already holds an answer to it inside [[claim_registry_current#CLAIM 032]]. This file audits the
> sentence that carries it.

---

## 0 · The sentence under audit

`CLAIM 032`'s Summary ends with:

> *«Inoltre, il topo **ipomorfo** `Wwox^gt/gt` (proteina bassa **ma rilevabile**) è **vitale**,
> mentre il null muore a 3-4 settimane ⇒ **la soglia fra letale e vitale sta sotto il 50%**.»*

This is the only sentence anywhere in the canonical state that places the viability threshold
**below** the heterozygote's ~50%. Everything else in `CLAIM 032` is a statement about
**heterozygotes**. `CLAIM 032`'s Clinical meaning then converts it into portfolio guidance —
*"non serve efficienza elevata … un mosaicismo terapeutico parziale può bastare"* — and its
Impact line says it *"abbassa la soglia di efficacia richiesta a tutte le leve di ripristino"*.

**Four defects, in ascending order of consequence.**

---

## 1 · The datum is not in the claim's own `Source` line

`CLAIM 032`'s `Source` names `PAPER 053` (Aldaz 2014), `PAPER 021` (Tochigi 2019), `PAPER 043`,
`PAPER 045`, `PAPER 049`, `PAPER 042`. **None of them is the hypomorph paper.** The
`Wwox^gt/gt` mouse was reported in:

> **PMID 17823927** — Ludes-Meyers JH, Kil H, Nuñez MI, Conti CJ, Parker-Thornburg J, Bedford MT,
> Aldaz CM. *"WWOX hypomorphic mice display a higher incidence of B-cell lymphomas and develop
> testicular atrophy."* **Genes Chromosomes Cancer** 2007;46(12):1129–36.
> DOI [10.1002/gcc.20497](https://doi.org/10.1002/gcc.20497)

The datum therefore enters the canonical state **through a review** (`PAPER 053`, Aldaz 2014 is a
review), with the primary neither cited nor read. That is the
`IMPORTED_PREMISE_ATTRIBUTION_GATE` pattern this repository already has a gate for, and the same
shape as the 2026-08-06 citation trilogy.

## 2 · The primary has never been read, and cannot be read from here

Established today by the authoritative method — **attempt the fetch, measure the body**:

| Check | Tool | Result |
|---|---|---|
| Receipt exists? | `fulltext_receipts.py status --pmid 17823927` | `[]` — **no receipt of any depth** |
| PMCID exists? | `get_article_metadata` | `PMC4143238` — **yes** |
| Body retrievable? | `get_full_text_article(["PMC4143238"])` | `"full_text": ""` — **0 bytes. The stub trap.** |
| Licence | `get_copyright_status` | `"(c) 2007 Wiley-Liss, Inc."`, `license: null`, `found_in_pmc: 0` |

⚠️ **A PMCID existing is not a body.** `PMC4143238` resolves and returns HTTP success with an
empty `full_text`. This is the third instance of the stub trap recorded in this repository
(`PMC4935222`, `PMC6965410`, now `PMC4143238`). **Verdict: `EVIDENCE_BLOCKED` (licence wall),
verified — not untested.** It goes to the acquisition packet, not back into the read queue.

> 🔵 **Extraction-damage note, observed live.** The abstract returned by
> `get_full_text_article` reads *"Homozygous Wwox gene-trap mice () had no detectable Wwox
> protein…"* — the italicised genotype token has been **deleted by the extractor**. The same
> sentence from `get_article_metadata` retains it. Every quotation below is taken from the
> **PubMed metadata abstract**, never from the PMC extraction. This is the
> `extraction_damage_report.py` rule demonstrated in production rather than recited.

## 3 · The sentence says more than its own abstract does

Verbatim from the PubMed metadata abstract of **PMID 17823927** (copied in the same act, tokens
checked):

> *"Homozygous Wwox gene-trap mice (Wwox(gt/gt)) had **no detectable Wwox protein in most tissues
> examined**, although, **a low level could be detected in a minority of tissues**."*

> *"Remarkably, Wwox hypomorphic mice are **viable** in contrast to the recently reported
> postnatal lethality of Wwox knockout mice."*

> *"We observed that the Wwox(gt/gt) mice had a **significantly shorter lifespan**, and female
> hypomorphs had a higher incidence of spontaneous B-cell lymphomas."*

Three things follow, and `CLAIM 032` carries none of them.

1. 🔴 **"proteina bassa ma rilevabile" inverts the emphasis.** The source says protein was
   **undetectable in most tissues** and detectable **only in a minority**. The canonical sentence
   reads as a uniformly low-but-present animal; the abstract describes a mostly-absent one with
   islands of residual expression.
2. 🔴 **The abstract names none of those tissues, and does not name brain.** The entire
   therapeutic inference — *how much WWOX does the recipient organ need* — depends on **which**
   minority of tissues kept protein. That information is in the body, and the body is unreadable
   from here. **It is therefore not merely unread; it is currently unknowable in this
   environment.**
3. 🔴 **"viable" is not "unaffected".** The same abstract reports a **significantly shorter
   lifespan**, testicular atrophy with reduced fertility, and increased B-cell lymphoma. A
   canonical sentence that carries only the word *vitale* into a therapeutic-threshold argument
   drops the phenotype the source reports in the same breath.

## 4 · The comparison spans two genotype classes and (at least) two null lines

**4a — genotype class.** `CLAIM 032` is titled and framed around **haploinsufficiency** — the loss
of *one* allele. `Wwox^gt/gt` is **homozygous** for a gene-trap allele: a near-null, not a
heterozygote. Under the operator's §17 rule (`null/null` · `splice/null` · `splice/missense` ·
`missense/missense` · `CNV/deletion` · `residual protein` · `uncertain expression` kept separate),
**these are two different classes inside one claim's Summary**, and the claim's own title covers
only the first.

**4b — which null.** The sentence says the null *"muore a 3-4 settimane"*. LEGEND's own complete,
receipted, locator-verified read of the Aldaz null (**PMID 19936220**, `FTR-20260806-19936220-01`,
23 strict-verified non-abstract locators) records something earlier and sharper:

> *"As early as 72 h after birth 43% (15 of 35) of Wwox KOs had died and 77% had died by 17 days
> after birth and no mice survived past weaning"* — `deepdive_manifests/PMID19936220.json`

> *"100% of Wwox KO mice died before weaning (21 days). WT, n = 18; HET, n = 43; KO, n = 8"* — ibid.

Separately, the discovery ledger records a Wwox-null line with *"letalità postnatale ~4 settimane
con ipoglicemia"* from the HIF1α/metabolism work — **a different laboratory's line**. ⚠️ Per §12,
two separately published animals are not one animal. **"3-4 settimane" is a single figure standing
where LEGEND holds at least two distinct measured survivals from two distinct lines**, and the one
whose lab also built the hypomorph — the only comparison that would be internally controlled —
reports **death before day 21, 77% of it by day 17**.

> ✅ **What this does NOT overturn.** Ludes-Meyers 2007 (hypomorph) and Ludes-Meyers 2009 (null)
> are **the same first author and the same laboratory** (Aldaz, MD Anderson). The hypomorph-vs-null
> viability contrast is therefore *within one group*, which is the strongest form the comparison
> could take. The defect is not that the contrast is cross-lab; it is that the canonical sentence
> imports a survival figure that is not the one that lab measured.

---

## 5 · What the threshold evidence actually supports, restated

| Level of WWOX | What is measured, and by whom | What may be said |
|---|---|---|
| **~50 %** (heterozygote) | mouse `+/−` lifespan indistinguishable from WT (Aldaz 2014); rat `+/lde` band at *"almost half"* intensity with normal cortical IHC (Tochigi 2019); every published human carrier parent clinically well | **Tolerated on the endpoints measured** — neoplasia, lifespan, growth, gross morphology. `PREMISE: NOBODY_LOOKED` on cognition, EEG, network excitability. **This limb stands.** |
| **between 0 and 50 %** | **only** `Wwox^gt/gt` — **unread, unreadable, tissue map unknown, shorter lifespan, tumour-prone** | 🔴 **Nothing may be concluded about a therapeutic threshold.** Viability of a near-null animal with unmapped residual expression does not establish how much WWOX a developing brain needs. |
| **0 %** (null) | Aldaz line: 43 % dead by 72 h, 77 % by day 17, none past weaning, with a measured systemic metabolic crisis | Lethal — **and lethal systemically**, which is the point below. |

🔴 **The inference that does not survive, stated plainly.** The Wwox-null mouse dies of a
**systemic** crisis (hypoglycaemia; raised BUN and creatinine on LEGEND's own reads of
`19936220` / `17803050`), not of brain failure. So *"hypomorph viable, null lethal"* localises a
threshold **for whatever tissue drives postnatal lethality** — plausibly liver, pancreas or
kidney. If that tissue is among the *"minority"* that retained protein, the contrast says nothing
whatever about the **neurodevelopmental** threshold. **The sentence currently reads as though it
did**, and `TX-003` / `TX-007` inherit it.

**Direction of the correction: the uncertainty goes UP, not down.** `CLAIM 032`'s conclusion for
heterozygotes is unchanged. What must go is the extra step below 50 %.

---

## 6 · Therapeutic consequence, per lever

| Lever | What it inherited | What it should inherit |
|---|---|---|
| `TX-007` AAV9-WWOX | *"non serve efficienza elevata; un mosaicismo parziale può bastare"* | **Unchanged for ≥50 % equivalence; unsupported below it.** And [[claim_registry_current#CLAIM 011]] already holds the opposite shape from a real dose series: Fig. 3B of PMID 42422765 places a **threshold** between 1.23 × 10¹¹ and 2.63 × 10¹¹ vg, with **no survival rescue below it**. 🔴 **A measured threshold in the therapy's own dose–response outranks an inference from an unread hypomorph, and the two point in opposite directions.** |
| `TX-003` chaperone / proteostasis | *"raising a residual pool a little may suffice"* | The only sub-50 % viable animal has an **unknown residual-protein tissue map**. The permissive reading is not evidenced. |
| `TX-002` CRISPRa | same | same |
| `TX-001` splice correction | *"a small corrected fraction may suffice"* | Already has no baseline fraction measured in any allele; this removes a borrowed floor it should not have had. |

🔴 **The cross-check that makes this worth landing.** `CLAIM 011` (dose threshold, measured in the
actual therapeutic vector, figure-verified) and `CLAIM 032` (dose threshold, inferred from an
unread hypomorph) are **in tension**, and the portfolio currently carries the permissive one into
its "partial counts" language. That tension was not visible while the hypomorph sentence had no
source to check.

---

## 7 · What LEGEND already knew, kept separate from what is new

**Already held (do not re-report as new):**
- `CLAIM 032` already carries `PREMISE: NOBODY_LOOKED` for cognition/EEG/excitability and already
  states the threshold is known for survival and morphology only.
- `CLAIM 011` already records the vg dose threshold and the "dose-dependent describes a continuum
  where the panel shows a threshold" defect.
- `CLAIM 030` already records that severity tracks residual **function**, not abundance.
- The stub trap and the `is_open_access:false` / `checked_sources:["pubmed"]` rule were both
  already written down; this file applies them, it does not discover them.

**New here:**
1. The `Wwox^gt/gt` sentence has **no source** in `CLAIM 032`'s `Source` line. *(new)*
2. Its primary **PMID 17823927 has no receipt of any depth**. *(new — and it is a live premise
   under a `clinical relevance: VERY HIGH` claim, so the `UNREAD_PREMISE` ratchet's `0` is true of
   the measured surface and not of this sentence.)*
3. `PMC4143238` is a **third confirmed metadata-only stub**. *(new)*
4. The abstract says *most tissues undetectable / a minority detectable* — the canonical sentence
   inverts this, and **brain is not named**. *(new)*
5. The hypomorph has a **significantly shorter lifespan** and tumour susceptibility; *vitale*
   alone is not faithful. *(new)*
6. Genotype-class conflation: a **homozygous near-null** sits inside a **haploinsufficiency**
   claim. *(new)*
7. `CLAIM 032`'s *"3-4 settimane"* does not match the survival the **same laboratory** measured for
   its own null (*before weaning; 77 % by day 17*). *(new)*
8. `CLAIM 011` ↔ `CLAIM 032` threshold tension, now visible. *(new)*

## 8 · Corrections against prior LEGEND text

- **`AUTONOMOUS_SESSION_STATE.md`** records *"the accessible reading queue is EMPTY … every
  copyright-verified open paper carrying no receipt has been read."* That is **true of the queue as
  it was enumerated**, and **false as a statement about the repository's premises**: `PMID 17823927`
  carried no receipt, was never in the queue, and is load-bearing under a VERY HIGH claim. **A queue
  can only be empty of what was put in it.** The unread-premise sweep measures *cited* papers; this
  one is used without being cited, which is precisely the invisible case the ratchet was built for
  and the one it cannot see.
- No canonical claim is reversed by this file. `CLAIM 032`'s heterozygote conclusion stands.

## 9 · The single cheapest missing experiment — and it is not an experiment

**Ask a human for eight pages.** `PMID 17823927`, *Genes Chromosomes Cancer* 2007;46(12):1129–36.
The decisive content is **one western-blot panel and its tissue labels**: *which* minority of
tissues retained Wwox protein in `Wwox^gt/gt`, and **whether brain is among them**. One
institutional PDF resolves a premise standing under the efficacy threshold of four therapeutic
strategies. It is packet-grade work, not bench work.

**If and only if brain is among the retaining tissues**, the bench experiment that follows is
video-EEG plus a myelination readout on `Wwox^gt/gt` — the sub-50 % neurodevelopmental threshold
nobody has measured, in an animal that already exists and is already viable.

---

*Sources retrieved from **PubMed / PubMed Central**.
DOIs — [17823927](https://doi.org/10.1002/gcc.20497) ·
[19936220](https://doi.org/10.1371/journal.pone.0007775) ·
[24932569](https://doi.org/10.1016/j.bbcan.2014.06.001).
No canonical file edited. No receipt claimed: **no reading occurred** — `PMC4143238` returned a
zero-length body, and an abstract is not a read. Not medical advice.*
