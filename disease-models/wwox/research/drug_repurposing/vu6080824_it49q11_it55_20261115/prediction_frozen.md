# IT49-Q11: predictions frozen before the body of PMC12434521 (PMID 40959251) was read

Written 2026-11-15 by IT. The page was fetched once earlier today and measured (size, section names, count of the compound name) but its text was not read. What I know of the paper is what SCI49 B recorded (`kir2_drugname_sci49_20261112/output/evidence.tsv` E09-E11, `compounds.tsv` C05): 5s = VU6080824, Kir2.1 manual patch clamp at pH 7.4, IC50 0.35 uM, Emax 100%, ML133 retested at 1.51 uM, rat IV cassette PK.

* F1 (held if the body agrees): the main text states 0.35 uM / pH 7.4 / manual patch clamp for 5s as SCI49 B recorded. Missed if a different value or condition is given.
* F2: the main text gives **no** counter-screen of 5s against Kir2.2, Kir2.3, Kir4.1, Kir6.2, Kir7.1 or hERG. Missed if a table in the body gives any of them.
* F3: the supporting information, if linked, is hosted by the publisher, not by PMC, and is not reachable by one plain request; the page lists it only. Missed if the SI is a PMC-hosted file.
* F4: no native neuron or brain-slice recording with 5s. Missed if one is described.
* F5 (case-level): the answer will be an abstention: VU6080824 is a Kir2.1 comparator by mechanism, not a probe, for the INV-18 arm; I expect nothing in the body that lifts it to a probe because the selectivity evidence sits in an unreached counter-screen.
Predictive capacity: none claimed; this is a check of what a second reading adds.
