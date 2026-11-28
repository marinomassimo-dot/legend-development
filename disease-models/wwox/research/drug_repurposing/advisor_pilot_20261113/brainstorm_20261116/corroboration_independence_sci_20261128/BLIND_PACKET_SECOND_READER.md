# Blind packet: are the sources behind each statement independent?

You are a second reader. For each item, judge whether the listed sources are independent support for the PROPOSITION.
Two sources are independent only if all three hold:
 a. primary data differ: each carries its own measurement or observation of the proposition, from different patients,
    animals, samples or deposited datasets (if a source does not carry any such observation, say so);
 b. no shared first author and no shared last author (note shared middle authors, and any case where the first author of
    one is the last author of another; they are noted, not counted);
 c. neither restates the other, and the two do not restate one common source (review or citation transmission).
Item verdict: HOLDS (at least two sources independent of each other), FAILS (no such pair; give the failing letters) or
UNSETTLED (a needed source is not held). With three or more sources also give the largest mutually independent set.
Do not grade whether the proposition is true or its scope. Do not edit anything in the repository.

Held full texts are under /home/desktop/legend-development/files/fulltext/ (names start with PMID<number>). Read only held
source files there (and files/check_runs/PMID19500159.txt). Do NOT read anything under any disease-models/ directory,
any ledger, registry, checkpoint or review of this repository, or any other folder under files/ (some are sealed).
Do not read or quote drug, vector, dose or treatment passages. Author lists may be taken from the held file, or from
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=<ids>&retmode=json (no e-mail, no other service).
A source with no held file: say "not held", use its author list only. No new acquisition.

| item | PROPOSITION | sources (PMID) |
|---|---|---|
| A | A child-onset phenotype recorded with the WWOX p.Pro47Arg variant in trans with an exon-1 truncating allele (the second source is offered as independent corroboration of the first) | 33916893 (Table 1 and supplement), 26499798 (Figure 2B) |
| B | Loss of Wwox disrupts brain development before birth (stated as convergence of several papers) | 32581702, 31340538, 31543760 |
| C | WWOX regulates a partner protein by something other than binding alone | 15070730, 21115974 |
| D | Wwox loss in mice gives early systemic collapse with bone or endocrine abnormalities | 19936220, 23254685, 18974271, 17360458 |
| E | Wwox-null rodent models of other groups did not detect osteosarcoma | 19936220, 19500159 |
| F | WWOX protein abundance does not predict clinical severity | 34268881, 24369382, 29808465, 24456803 |
| G | Blood urea nitrogen is raised in the Wwox-deficient rat and mouse | 17803050, 19936220 |

Write your table to /home/desktop/.claude/jobs/7fd08ff1/tmp/blind/SECOND_READING.md with, per item: verdict, failing
letters, largest independent set, one locator per data claim (file, section or figure/table), shared authors, and what you
could not check. Then return the same table (keep it under 60 lines).
