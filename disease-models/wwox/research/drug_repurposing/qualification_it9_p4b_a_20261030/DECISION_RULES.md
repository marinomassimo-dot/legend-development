# Decision rules for group A (written 2026-10-30 before the acquisition outcome was read)

Scope: P3-01 balsalazide, P3-02 ramelteon, P3-03 belzutifan, P3-04 ceperognastat, P3-14 AR-12, P3-15 dichloroacetate (reference). The acquisition script `qualify_p4b_a.py` had been written and started when this file was committed; none of its output had been opened.

Allowed decisions: DROP (a decisive datum is named), KEEP-AS-PROPOSAL (next experiment, readout, control, falsifier), REFERENCE-ONLY, INCONCLUSIVE (the exact missing datum). "Insufficient support" and "no activity" are different statements and are labelled differently.

Rules fixed now:
1. DROP on exposure only if a primary source (label or paper) states the parent or active species is not systemically absorbed or does not reach the nervous system, or states no measurable plasma level; a general-knowledge impression is not a decisive datum (it stays UNVERIFIED and gives INCONCLUSIVE).
2. DROP on the edge only if the edge record shows that the relation is not a transcriptional effect on the seed readout (for example a post-translational record applied to a transcript seed) AND no alternative edge through the same target exists in the network files; otherwise the edge defect is a stated limit, not a drop.
3. DROP on target engagement if the compound has no measured activity at the declared main target in ChEMBL and the declared target is traced to another compound or a name collision.
4. KEEP-AS-PROPOSAL requires: an in-vitro experiment in a WWOX-deficient neural system that is feasible with a named readout; the target is expressed (HPA, adult, stated as such) in a relevant neural cell type; no decisive datum under rules 1 to 3. The next experiment must name a readout that separates adaptive from harmful valence (not only a transcript).
5. Scores are kept separate: biological promise (WWOX seed link and target action only), depth of evidence, feasibility, priority of the next experiment. Each on a three-level scale LOW / MEDIUM / HIGH with the reason; no sum.
6. A seed-direction conditional (PDK1, PDHA1 uncertain) is never resolved for convenience; a candidate that depends on it is labelled conditional.
7. Counts of spontaneous reports (openFDA adverse events) are counts, never rates, never a comparison between drugs.
8. Expression: HPA is adult (and cell-line/tissue) data; no developmental-age value is claimed from it.
