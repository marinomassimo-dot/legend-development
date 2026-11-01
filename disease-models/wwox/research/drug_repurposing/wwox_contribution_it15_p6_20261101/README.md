# What WWOX knowledge adds, measured on the two IT15 questions (P6, 2026-11-01)

Non-canonical research material; not medical advice; no efficacy claim. Counts come from `compare_p6.py` over the package tables (rerunnable offline; `comparison_p6.tsv`); they are derived, not pinned by a test.

## What was compared

For each question three paths over the same inputs: (1) simple target-action retrieval (ChEMBL target-first, graded by `selectivity_p6.py`); (2) the same retrieval read through WWOX context (the pre-registered selection criteria, the slice system, the premises the module holds); (3) the earlier generator output where it addressed the question (the IT10 Q7 direct search on GSK3B; the NMDAR deepening queue from the catalogue rule for Q-A). The network generator was **not** run again: for Q-A it does not represent the question (it is a signed-edge ranking, and the question is about a subunit-discriminating experiment), and for Q-B its earlier output is the comparator.

## What each path produced (see `comparison_p6.tsv` for the numbers)

| Question | Simple target-action | WWOX-informed | Earlier path |
|---|---|---|---|
| Q-A NMDAR (partial benefit) | thousands of activity rows and several thousand parent compounds, only a small fraction named; same-document groups graded; most subunit pairs cannot be compared without conditions | four cases; a stated prediction with its upper-bound formula; a list of controls; the premise that the NMDAR gain is unmeasured kept visible | queue of 34 catalogue compounds, 20 of them on the NMDAR need, chosen by a documented direction-consistent action; reconciliation (P3.1) found some already assessed or mentioned elsewhere (counts for the 20 and for the whole queue in `comparison_p6.tsv`) |
| Q-B GSK3 (broader compensation) | several thousand GSK3B and GSK3A rows; isoform pairs exist, kinase panels are panels | abstention for any compound; one tool experiment with falsifiers and a Wnt-direction control | IT10 Q7: 50 names, all DIAGNOSTIC_ONLY; target-first adds 2 names, no therapeutic candidate |

## What the WWOX knowledge specifically contributed (and what it did not)

Contributed, each with its anchor:
1. **The question and its endpoint.** The slice burst is d-APV-sensitive and the NMDAR current was never measured (Breton 2021); that turns "NMDAR drugs" into a subunit-discriminating experiment (a GluN2B-sensitive share to be measured, with equal-current controls). Without the WWOX observation the retrieval has no stopping point: the retrieval holds several thousand parent compounds with an activity row on an NMDAR subunit target.
2. **A premise limit that stopped a candidate.** The GSK3 de-repression rests on a single blot (one lane per genotype per region, no n or statistics), no kinase-activity assay exists in any WWOX system, and lithium acted equally in wild type. That is why the output is a tool experiment and not a nomination; the simple path alone would have listed hundreds of GSK3 inhibitors with potencies.
3. **A direction conflict made visible.** Higher GSK3 activity predicts lower Wnt output; the organoid shows Wnt targets up. The verifier weakened this conflict (Wnt signalling does not use Ser9; confounded by maturity) but it remains a reason to include a Wnt-direction control.

Not contributed by WWOX knowledge (it came from the new quantitative grading or from general pharmacology): the avoidance of generic-complex pseudo-selectivities, of the "negative allosteric modulator" vocabulary label on pore blockers, of single tideglusib potency numbers, of treating lithium salts as having activity (the activity sits on the ion).

## Errors avoided and errors caught (counted from the packages and their verification)

* Avoided by the grading: values on a generic NMDAR complex used as subunit values; a defined-complex-versus-component comparison read as selectivity; a panel across gene families read as selectivity; a GSK3A|GSK3B group value read as one isoform (a defect found in the grader itself in IT15 and fixed with regressions).
* Caught only by independent verification, not by the producers: a review document read as one experiment with concordant arms (Q-A H1); a prediction stated as a point value although it is an upper bound; two claims of absence (no isoform lever; no document pairing Tau and catenin) that did not survive a search by assay description; an identity mislabel (a "Cys-199-dependent" title belonging to another compound). Each changed text; none changed the status of the cases.

## What this does and does not show

* Coverage: the target-first path recovers what the catalogue queue holds and more (the queue entries all resolve in ChEMBL once the queue IDs are used; the producer's "not found" was a naming miss).
* Matching quality: the grade prevents specific false links (listed above; the counts of grades are in `comparison_p6.tsv`, the false links avoided are named cases, not a rate).
* Hypothesis generation: the WWOX-informed path produced two comparable case sets, each with a falsifier; the simple path produced tables.
* Predictive accuracy: **not measured**. No independent outcome set exists for either question (no GluN2B-NAM or GSK3-inhibitor result in a WWOX preparation), so this is not a benchmark of efficacy and no case is a prediction that has been tested.
* Biological benefit: none demonstrated.
* Cost: producers ran about 53 minutes (Q-A) and 25 minutes (Q-B), plus verification of about 9 and 16 minutes, with several hundred ChEMBL requests and repeated HTTP 500 retries; the verifier changed the text of both packages, so verification is not optional overhead.
* Limit that prevents a stronger claim: the module has no case where the WWOX-informed path and the simple path disagree about a compound that was later tested.
