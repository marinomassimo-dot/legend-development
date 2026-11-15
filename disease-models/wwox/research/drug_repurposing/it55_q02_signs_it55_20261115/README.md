# IT55-Q02 part 1: the six confirmed differentiation hits of paper 1's Table 1 against the frozen case-1 signs (IT, 2026-11-15)

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. No frozen sign, count, ranking or card is edited. **Not blind:** IT had already seen the six rows and EC50s while verifying SCI's second read, so no prediction could be frozen for this comparison. One reader. The frozen signs are those of `phenotype_first_it29_20261105/comparison_case1_it29.tsv` (column `evidence_direction`); the paper-1 values are Table 1 of PMID 27592856 (PMC5011342), read from the open-access XML (receipt `FTR-20261115-27592856-01`, tables only; 7/7 verbatim rows found mechanically, `verbatim.tsv`).

## Answer first
**Six agreements, no disagreement, from a real differentiation readout; five frozen compounds have no readout in paper 1.** Every one of the six compounds in Table 1 carries the frozen sign "favourable", and Table 1 lists confirmed differentiation hits (percent of the positive control, EC50): so each is an agreement of the frozen direction with a primary differentiation measurement. The earlier "five contradictions" were an artefact of the wrong endpoint (the viability screen) and are withdrawn (IT30); this note does not add a new disagreement.

| Compound | Frozen sign (evidence rows) | Paper 1 Table 1: differentiation, percent of positive control (EC50, micromolar) | Comparison |
|---|---|---|---|
| tamoxifen | favourable (R32 R36) | 85 (0.2) | agrees |
| quetiapine | favourable (R13) | 109 (0.4) | agrees (in Table 1 as a hit; the viability sheet used it as the normaliser, a different file) |
| benztropine | favourable (R01 R02 R06 R14) | 66 (0.3) | agrees |
| oxybutynin | favourable (R08) | 67 (2.6) | agrees |
| ipratropium (printed "Ipatropium") | favourable (R08) | 58 (8.5) | agrees |
| ifenprodil | favourable (R36 R37) | 93 (0.4) | agrees |
| clobetasol | favourable (R23 R25 R26; sign source is the reference) | not in the paper's text | no readout |
| ketoconazole | favourable (R30; sign source is the reference) | not in the paper's text | no readout |
| miconazole | favourable (R22 R24 R28 R30) | not in the paper's text | no readout |
| liothyronine | favourable (R35) | not in the paper's text | no readout (the paper uses thyroid hormone as its positive control; no table of its own values in anything deposited) |
| mevastatin | adverse (R34; sign source is the reference) | not in the paper's text (a keyword match in my first pass was the word "devastating", a false hit; the scout's "agreement" came from the withdrawn viability sheet) | no readout |
Counts: of the 20 frozen compounds, 6 agree with a differentiation readout, 0 disagree, 5 have no readout in paper 1 (above), and 9 were reported by the scout as absent from the library (not re-checked here).

## What it does and does not settle
* **Settles:** the case-1 comparison **can** cite a real differentiation readout for six compounds; the claimed assay-system dependence of the favourable signs (decision cell of IT29-P12) **is not supported by this paper**: the apparent disagreements came from the wrong endpoint, and the four compounds that the viability sheet had counted as "contradictions" have no differentiation value at all. Where the frozen signs for clobetasol, miconazole and ketoconazole come from (mouse lesion and in vitro myelination evidence, rows R22-R30), that is a different system from rat OPC immunofluorescence, so cross-system agreement or disagreement for those three stays untested.
* **Does not settle:** Table 1 lists only confirmed hits, so this paper cannot return an adverse direction; a compound absent from it is untested or not a hit, not adverse. Percent of the positive control is a rescue-style scale, not an effect size. One reader, tables only, methods and supplements not opened by IT.

## Part 2 (the 2015 OPC screen supplement, public MEA screens): not reachable, written absence
The map cell names no identifier. The candidate by content is the 2015 drug-based remyelination screen paper (PMID 25896324, PMC4528969; it names miconazole and clobetasol 72 times each; a receipt for it exists). Routes tried, one request each: (1) Europe PMC search (identified the paper); (2) the PMC article page (served the article, 83,250 characters; it lists four supplements: a docx, Table S1 as pdf and two xlsx tables), then **one request for supplementary table 2: a proof-of-work interstitial (1,817 bytes of HTML), a stop**; (3) Europe PMC `supplementaryFiles`: returned only a figure gif. Public MEA datasets were not searched (stop result: if only part 1 can be done, deliver it). What part 2 would need: a lawful route to those two xlsx tables (the publisher's own page, or an author deposit) and a reader to compare their compound values with the frozen signs, then a decision whether any public MEA screen exists for the four compounds.
