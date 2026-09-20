# ACQUISITION PACKET — 2026-09-20

**What this is.** Five high-value papers that **cannot be obtained by any automated route available
in this environment**, packaged so a human with institutional access can clear them in one sitting.
Each entry says what the paper would settle, which routes were tried, what each returned, and what
remains. **Non-canonical, read-only.**

**Why a packet rather than more retries.** Every route below was tried and failed with a recorded
reason. Re-running them costs turns and returns the same refusal. The operating rule that produced
this file: *never let one inaccessible paper stop the queue — park it with its evidence and move on.*

## Routes measured in this environment (do not re-test)

| Route | Result |
|---|---|
| `curl` → `eutils.ncbi.nlm.nih.gov`, `ebi.ac.uk` | `403 CONNECT` (agent-proxy policy denial, logged) |
| `WebFetch` → `pmc.ncbi.nlm.nih.gov`, `jbc.org`, `sciencedirect.com` | `EGRESS_BLOCKED` |
| `OpenAlex`, `Unpaywall`, `Semantic Scholar` | `403 CONNECT` |
| `WebSearch` | works — **finds** papers, returns snippets. **A snippet is not a read** and may not ground a finding |
| PubMed MCP `get_full_text_article` | **the only reading route**; PMC **open-access subset only** |
| PDF tooling (`fitz`, `pdftotext`, `pdftoppm`, `pdfimages`) | all absent (`tool_preflight.py`) → **no figure panel is inspectable at all** |

---

## A1 · `PMID 15126504` — Sze, Chang 2004, *J Biol Chem* 279(29):30498–506 · `FT-024`
**DOI** 10.1074/jbc.M401399200 · **no PMCID** (confirmed via `convert_article_ids`)

**What it settles, in one sentence:** whether the GSK-3β phosphorylation that rises on WWOX knockdown
is the **activating pTyr216** or the **inhibitory pSer9** — because `CLAIM 035` records that a pS9
readout in this system produces a **false negative**, and the abstract does not name the site.

**Why it is worth a human's time:** it is the **third source** of the entire WWOX→GSK3β→Tau arc. The
field is three papers; LEGEND has read the other two completely. It also carries the only
pharmacological rescue of a WWOX-*loss* phenotype anywhere in the literature (SP600125 and PD-98059
blocking Tau phosphorylation and NFT formation in WOX1-knockdown cells) — a better-evidenced lever
on that axis than lithium, and currently absent from the therapeutic portfolio.

**Routes remaining:** ASBMB/JBC open archive via institutional login · ILL · corresponding author.
**Ask for:** the Results passage naming the GSK-3β phospho-site, and the SP600125/PD-98059 figure
with its concentrations.

---

## A2 · `PMID 27569545` — Leppa, Geschwind 2016, *Am J Hum Genet* 99(3):540–554 · `FT-105`
**DOI** 10.1016/j.ajhg.2016.06.036 · **PMCID PMC5011063 — in PMC, NOT in the OA subset**

🔴 **Licence wall, not a transient failure.** `get_full_text_article` returns `"full_text": ""`;
`get_copyright_status` returns *All rights reserved*, `is_open_access: false`. **Do not re-queue on
the PMC route — it will always return empty.**

**What it settles:** whether the WWOX CNV figure circulating in the field is real. The primary's
abstract contains **one clause** about WWOX and **no number at all**. The circulating
`12/3565 vs 1/2633, p=0.01, OR=8.8` comes from a 2020 review; the **same senior author's 2019
review** reports the same result as *"9 affected children, with very high odds ratio"* against
**1,532 families** and **no numeric OR**. Count, unit, denominator and the existence of a number all
differ between the two.

**Routes remaining:** AJHG PDF / ScienceDirect HTML via institutional access · corresponding author
(senior author at UCLA; the address is on the PubMed record and is deliberately not reproduced in
this public-edition file) · ILL.
**Ask for:** the Results sentence and table row carrying the WWOX CNV counts, the denominators, the
deletion/duplication split, and any sentence about FRA16D or platform matching between cases and
siblings.

---

## A3 · `PMID 15026124` — Chen, Chang 2004, *Neuroscience* 124(4):831–9
**No PMC deposit** (confirmed) · Elsevier

**What it settles:** the **developmental expression timing of WWOX in the nervous system**, with
E-day/P-day resolution. This is the single largest gap in the developmental picture.

🔴 **Why this one is unusually worth obtaining:** **four secondary sources restate it four
incompatible ways** — *"low during the early embryonic stage"*, *"highly expressed in the developing
nervous system of mouse embryos"*, *"ubiquitously expressed in all brain regions"* (no time term),
and *"reduced in the newborns"*. The field is restating a paper none of us can open, and the
disagreement cannot be resolved without it.

**Routes remaining:** Elsevier institutional access · ILL · corresponding author.
**Ask for:** the figure and Results text giving stage-by-stage expression, and whether the trend is
up or down across the perinatal transition.

---

## A4 · `PMID 33914858` — Repudi 2021, *Brain* · **no PMCID**
**What it settles:** an Aqeilan-lab primary on WWOX neurodevelopment already cited by records LEGEND
holds. Lower priority than A1–A3 because LEGEND already carries much of its content second-hand
through `PAPER 063` and related records — **but that is exactly the dependency worth removing.**
**Routes remaining:** OUP institutional access · ILL.

---

## A5 · `PMID 24369382` — Mallaret 2014 · **PMC deposit returns an empty body**
**What it settles:** the primary behind the "carrier parents are unaffected" leg of `CLAIM 032`.
With `CC-20260920-CLAIM032-ENDPOINT-QUALIFIER-01` standing, the question is narrow and specific:
**were the carrier parents examined, and with what?** If the answer is "clinical observation only",
that confirms the candidate's `PREMISE: NOBODY_LOOKED`; if there is an EEG or a neuropsych battery,
the candidate needs weakening.
**Routes remaining:** publisher access · ILL · authors.

---

## A6 · `PMID 18371080` — Lo, Chen 2008, *Eur J Neurosci* 27(7):1634–46 · `DL-MOL-008` / `HYP-20260709-04`
**DOI** 10.1111/j.1460-9568.2008.06139.x · **no PMCID** (confirmed via `convert_article_ids`: the
record returns the PMID alone) · Wiley paywall. *Added 2026-09-21.*

**What it settles, in one sentence:** whether the pTyr33-WWOX peptide — the **only explicit
therapeutic pointer with an in-vivo neurological result anywhere in this batch** — works by
*supplying* a WWOX-dependent signal or by *blocking* one, because those two readings point in
**opposite** directions for a genotype with no functional WWOX protein.

**Why it is worth a human's time:** the peptide reached a therapeutic hypothesis in this repository
on the strength of a **commentary from the same laboratory** (Sze 2015, `PMID 26355344`), which
glosses it as useful *"in the restoration of neural function under WWOX deficiency"*. The primary's
own abstract says the opposite about the direction of the pathway: *"activated WOX1 plays an
essential role in the MPP+-induced neuronal death"*, and *"Dominant-negative WOX1, a potent
inhibitor of Tyr33 phosphorylation, abolished this event."* On that reading the peptide is an
**antagonist of an activated-WWOX death pathway**, which has nothing to antagonise in a
WWOX-deficient brain. `HYP-20260709-04` is already `refuted` on this basis and `DL-MOL-008` is now
closed in the same direction — **but both closures rest on an abstract, and an abstract is not a
read.** This paper is the one document that can confirm or overturn them.

**What to look for, specifically:** (1) the peptide's proposed **mechanism of action** in the
Discussion — decoy/competitive inhibitor versus signal substitute; (2) **dose, route of
administration, BBB penetration and duration of effect**, none of which appear in either the
abstract or the commentary; (3) whether any arm tested the peptide in a **WWOX-depleted** background
rather than an MPP+-intoxicated wild-type one; (4) the controls on the non-phospho peptide arm.

**Routes remaining:** Wiley via institutional login · ILL · corresponding author (Chen Shur-Tzu /
Chang Nan-Shan, National Cheng Kung University). **Do not re-test automated routes** — no PMCID
exists and Wiley is unreachable from this deployment.
**Ask for:** the Discussion passage on mechanism, and the peptide methods paragraph (sequence, dose,
route, vehicle, timing).

---

## A7 · `PMID 25416187` — Tabarki, Al Mutairi, Al Hashem 2015, *Exp Biol Med (Maywood)* 240(3):400–2 · `FT-090`
**DOI** 10.1177/1535370214561952 · **PMCID PMC4935222 exists but is a metadata-only stub** —
`get_full_text_article` returns HTTP success with `"full_text":""`, and `get_copyright_status`
returns `is_open_access: false`, `found_in_pmc: 0`. SAGE has deposited no free body text. *Added
2026-09-21.*

**What it settles, in one sentence:** which **primary** source, if any, stands behind the only
sentence in `PMID 27551470` that reaches a WWOX neurological phenotype — because this source, its
ref. 14, turns out to be a **review**, so the citation chain passes through it rather than bottoming
out in it.

**Why it is worth a human's time:** the genre question is already answered from metadata
(`article_types` = `["Journal Article","Review"]`; the abstract says *"The aim of **this review**
is to summarize the roles of WWOX in the developing brain"*), and answering it was most of the
value. What remains is **the reference list**, and that is the real prize: the abstract states a
specific clinical phenotype — *"The neurologic phenotype of WWOX mutation includes seizures,
ataxia, developmental delay, and spasticity of variable severity"* — and this repository cannot
currently name the case series that phenotype came from. A three-page review's bibliography is a
short, high-yield object.

**What to look for, specifically:** (1) **the reference list**, and specifically which references
carry the seizure/ataxia/spasticity phenotype and which carry the expression data; (2) whether the
expression claim — *"WWOX is highly expressed in different brain regions during murine fetal
development and remained unchanged in the cortex and the corpus callosum in adult mice"* — is
sourced to a primary or asserted; (3) whether the review names consanguinity or an ascertainment
context for the homozygous cases.

**Routes remaining:** SAGE via institutional login · Europe PMC (untried from here; the MCP surface
is PMC-only) · ILL · corresponding author, whose address is in the PubMed record.
**Ask for:** the reference list first, the body second. **A scan of the bibliography alone would
discharge most of this debt.**

---

## Priority order for a human with one hour

1. **A1** (`15126504`) — settles a live mechanistic question *and* surfaces a therapeutic lever.
2. **A5** (`24369382`) — directly tests a standing commit candidate's central premise.
3. **A3** (`15026124`) — resolves a four-way disagreement in the field's own restatements.
4. **A2** (`27569545`) — settles whether a widely-cited odds ratio exists.
5. **A4** (`33914858`) — removes a second-hand dependency.

*(Added 2026-09-21, and it belongs near the top if the hour is a **therapeutic** hour rather than a
mechanistic one:)*

- **A6** (`18371080`) — the only in-vivo therapeutic pointer in the batch, currently closed in the
  negative **on an abstract alone**. It is the cheapest way to either recover a therapeutic lead or
  retire one for good.
- **A7** (`25416187`) — **cheapest item in the packet.** Its genre question is already settled; only
  its three-page reference list is needed, and it is the sole route to the primary behind a
  phenotype statement this repository currently cannot source.

> **If a PDF arrives:** this checkout has **no PDF tooling**, so a PDF alone will not be readable
> here. Extracted text or HTML is preferable; if only a PDF exists, the text layer should be
> extracted wherever it is opened and supplied alongside it.
