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

## Priority order for a human with one hour

1. **A1** (`15126504`) — settles a live mechanistic question *and* surfaces a therapeutic lever.
2. **A5** (`24369382`) — directly tests a standing commit candidate's central premise.
3. **A3** (`15026124`) — resolves a four-way disagreement in the field's own restatements.
4. **A2** (`27569545`) — settles whether a widely-cited odds ratio exists.
5. **A4** (`33914858`) — removes a second-hand dependency.

> **If a PDF arrives:** this checkout has **no PDF tooling**, so a PDF alone will not be readable
> here. Extracted text or HTML is preferable; if only a PDF exists, the text layer should be
> extracted wherever it is opened and supplied alongside it.
