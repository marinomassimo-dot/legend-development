# CC-20261003W5-A-CARGO-CASSETTE-01 — cargo size and cassette: the one restoration parameter that is now bounded by measurement rather than by analogy

- `context_policy: SOURCE_FIRST`
- Sources (all first reads, all `partial_fulltext_read`): PMID 40988338 (`FTR-20261003-40988338-01`),
  PMID 41712282 (`FTR-20261003-41712282-01`), PMID 41314141 (`FTR-20261003-41314141-01`),
  PMID 39358605 (`FTR-20261003-39358605-01`), PMID 41712149 (`FTR-20261003-41712149-01`).
  All five manifests validate (VERDICT: PASS). **None mentions WWOX.**
- Change class: **MINOR** — one research-line record in the research layer. It adds a parameter that
  `CC-20261003W3-C-RESTORATION-SPEC-01` did not have sources for, and narrows nothing.
- **Nothing here is medical advice.**

## The finding, in one sentence

Wave 3 listed six parameters of a WWOX-restoration strategy and found route, cell-type reach and
off-target organ risk well measured, dose measured only as vector genomes, and the window not
measured at all; **cargo size and cassette design was not among the six**, and it is the one
parameter this wave's sources measure end to end — with a quantified penalty at every step above the
packaging limit and a quantified bonus below half of it.

## The measured ladder, from smallest cargo to largest

| Cargo | What was measured | Source |
|---|---|---|
| **1.7 kb coding sequence + minimal promoter** | A short synthetic promoter is what *permits* self-complementary packaging; self-complementary AAV is stated to "stably transduce at least 10-fold more cells than single-stranded AAV" | PMID 41712282 |
| **A coding sequence under a weak minimal promoter, self-complementary, in a clinical lot** | The lot delivered to children was **42% genome-containing particles**, so a 1×10^15 vg dose carried 2.38×10^15 capsids; the authors separately credit the weak promoter with limiting overexpression-driven dorsal-root-ganglion toxicity | PMID 41314141 |
| **A cDNA under a strong, large ubiquitous promoter** | Works and gives the best rescue of the two promoters tested, but the authors state the trade directly: this promoter "combined with larger transgene lengths often exceeds the limits of AAV9 packaging capacity so this strategy cannot always be implemented" | PMID 39358605 |
| **5.136 kb ITR-to-ITR, above the ~4.7 kb nominal limit** | Packages, with a measured penalty: a **two-fold loss of yield** against a 4.617 kb control made the same day (2.78 versus 4.25 relative yield); full-to-empty 94.60:5.40 by electron microscopy; and, read from the supplement rather than the body, the "75.81% full-length" figure is the **4–6 kb size bin**, with 8.96% at 3 kb and **15.22% above 6 kb** | PMID 40988338 |
| **>6.0 kb open reading frame** | Single-vector replacement is impossible; the answer is a **split-intein dual-vector** architecture plus cell-class-specific enhancers, which improved survival and reduced seizures in two models — and has no human data | PMID 41712149 |

## What this licenses and what it does not

**Licensed.** The cassette decision for a WWOX programme is a *measurable* decision with a known
cost function, and the costs are not symmetric. Below roughly half the packaging limit a programme
can buy self-complementary packaging — on PMID 41712282's statement, an order of magnitude more
transduced cells — at the price of accepting a minimal promoter, which PMID 41314141 then shows is
not purely a cost, because promoter weakness is also an overexpression-safety lever. Above the limit
a programme pays twice: in yield and in genome heterogeneity, and the second payment is visible only
in the supplement.

**Not licensed.** This repository has **no record of the size of a WWOX expression cassette** — no
coding-sequence length, no promoter choice, no regulatory-element or poly(A) budget, and no stated
isoform. Which rung of the ladder a WWOX programme stands on is therefore unknown, and it is the
cheapest unknown in the whole restoration spec to close: it is an arithmetic question about a
sequence, not an experiment. Until it is closed, nothing above can be applied, and the
PMID 41712149 route (dual vector) cannot be ruled in or out.

**A second unlicensed inference, flagged because it is tempting.** PMID 40988338 shows that an
oversized genome can still yield full-length protein in vivo. That is not a licence to oversize a
WWOX cassette: the isoform question is prior. PMID 40988338 delivered **one** isoform of a
multi-isoform gene and names the single-isoform choice as a candidate reason its neonatal arm failed
behaviourally. A WWOX cassette that silently picks one isoform inherits that risk without inheriting
its evidence.

## Non-independence of the sources, which must be stated

Three of the six sources in this group share vector-design lineage and should not be counted as
three independent observations of promoter behaviour: PMID 41314141's vector uses the minimal JeT
promoter and its inventor is an author; PMID 41712282 is from the same institution and uses a
JeT-plus-intron promoter (UsP); and PMID 39358605's reagents-and-tools table records that its CBh
plasmid was provided by that same investigator. The promoter-strength trade-off is therefore
attested by one design tradition plus one independent group (PMID 40988338, hSyn1), not by four
independent ones.

## Ops (provisional ids; re-measured at commit time)

### 1 · `disease-models/wwox/research/research_lines_current.md` — `append` (new record)

```
---

## RL-GT-003 — Cargo size and cassette design: the WWOX restoration parameter that is bounded by measurement
**Status:** active — bounded externally, blocked internally on one unmeasured number
**Primary pathway:** P7 (gene therapy design), vector architecture
**Evidence base:** PMID 41712282 (`FTR-20261003-41712282-01`), PMID 41314141 (`FTR-20261003-41314141-01`), PMID 39358605 (`FTR-20261003-39358605-01`), PMID 40988338 (`FTR-20261003-40988338-01`), PMID 41712149 (`FTR-20261003-41712149-01`) — none of which mentions WWOX
**Clinical relevance:** HIGH strategic / NOT clinically validated
**Reason active:** this is the only parameter of the six in RL-held restoration spec work whose cost function is measured end to end in the 2024–2026 literature, and the costs are asymmetric. Below about half the ~4.7 kb packaging limit a short synthetic promoter permits self-complementary packaging, stated to transduce at least ten-fold more cells; a weak minimal promoter is simultaneously an overexpression-safety lever, since dorsal-root-ganglion toxicity is attributed to transgene overexpression. Above the limit the penalty is measured twice: a two-fold yield loss against a same-day control within the limit, and a genome population in which the reported "75.81% full length" is a 4–6 kb size bin with a further 15.22% above 6 kb — a fact readable only in the supplement, not in the body. Above ~6 kb single-vector replacement is impossible and the only route is split-intein dual vector, which has no human data. A strong large promoter gives the better rescue but cannot be combined with a large transgene.
**Next action:** measure and record the WWOX expression-cassette budget — coding-sequence length for the stated isoform, promoter, regulatory elements and poly(A), ITR to ITR — before any dose, route or window statement is attempted. It is arithmetic on a sequence, not an experiment, and no statement in this record can be applied until it exists. Note that three of the five sources share vector-design lineage (JeT/CBh, one investigator) and must not be counted as independent attestations of promoter behaviour.
```

## What would change the model if true, and what would falsify it

**Would change it:** the WWOX cassette budget itself — a single number — which immediately selects a
rung of the ladder and with it the promoter, the packaging mode and whether the dual-vector route is
needed. **Would falsify the central claim here:** a demonstration that oversized packaging carries no
yield or heterogeneity penalty under modern production (which would collapse the ladder into one
rung), or that self-complementary packaging does not deliver the stated multiple of transduced cells
when measured rather than predicted — note that PMID 41712282's ten-fold figure is explicitly a
*prediction* carried from citations, not a measurement in that paper.

### LOCATOR TRIPLES FOR BLIND AUDIT

(A minimal promoter is what allows self-complementary packaging of this coding sequence. | use of the short UsP allows self-complementary packaging of the 1.7 kb SLC13A5 coding sequence | Results, vector design, `files/fulltext/PMID41712282_Bailey2026_PMC.xml`)

(Self-complementary packaging is claimed to reach far more cells than single-stranded. | predicted to stably transduce at least 10-fold more cells than single-stranded AAV | Results, vector design, `files/fulltext/PMID41712282_Bailey2026_PMC.xml`)

(Most of the particles in the dosed lot carried no genome, so the capsid burden exceeded the vector-genome dose. | 42% genome-containing particles | Discussion, dose paragraph, `files/fulltext/PMID41314141_Greenberg2026_PMC.xml`)

(A strong ubiquitous promoter cannot always be used because of the packaging limit. | this promoter combined with larger transgene lengths often exceeds the limits of AAV9 packaging capacity | Discussion, promoter paragraph, `files/fulltext/PMID39358605_Wiseman2024_PMC.xml`)

(The cassette exceeds the nominal AAV packaging limit. | a construct size of 5.1 kb ITR-to-ITR | Results, transgene generation, `files/fulltext/PMID40988338_Quinlan2025_PMC.xml`)

(Packaging an oversized genome halved the yield relative to a same-day control within the limit. | a 2-fold reduction in viral yield for our oversized construct | Results, transgene generation, `files/fulltext/PMID40988338_Quinlan2025_PMC.xml`)

(The empty-capsid fraction was measured by electron microscopy. | a full-to-empty capsid ratio of approximately 94.6:5.4 | Results, transgene generation, `files/fulltext/PMID40988338_Quinlan2025_PMC.xml`)

(The coding sequence of this gene exceeds what one vector can carry, which forced a two-vector architecture. | genome size constraints (~4.7 kb), which preclude packaging the full human  | Gene-based therapies, preclinical gene replacement, `files/fulltext/PMID41712149_Balestrini2026_PMC.xml`)

(The two-vector split-intein approach worked in two disease models. | employing a dual-vector delivery approach | Gene-based therapies, preclinical gene replacement, `files/fulltext/PMID41712149_Balestrini2026_PMC.xml`)
