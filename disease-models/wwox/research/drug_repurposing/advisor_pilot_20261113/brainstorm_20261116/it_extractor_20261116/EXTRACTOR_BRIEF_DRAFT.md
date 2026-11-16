# Blind extractor brief (DRAFT; held until BOTH freezes exist; IT; non-canonical; not medical advice)

Written for: the delegate that will extract, and ADV/SCI as second readers. Reference genotype class only. Mechanism labels only; no dose, no recommendation. The extractor is a delegate, not SCI, and must not be shown the matrix, the rankings, the baselines or this plan's class scores.

## Release condition (checked by IT before dispatch)
(1) the rule v1 content hash is recorded (plan blob at f8210bc2e, sha256 f6b1af5784cf75a0d826fa3f0426cad356e374f336bfbbe9932f0e5b95184702, or its announced later version); (2) the informed-arm freeze commit (SCI) and the baseline-arm freeze commit (IT, delegate output) exist and are ancestors of the commit that adds the outcome table; (3) no read receipt of an outcome source is dated before the freeze. Not before.

## Inputs
The 14 reports of the A1 series with held full texts or abstracts and their receipts (`batch_sci_20261105/a1_wwox_reports/receipts/`, listed in `cases_a1.tsv`, `source_depth` column: 11 partial full text, 2 abstract only, 1 reused prior reading). The extractor reads the reports, not `cases_a1.tsv`.

## Task
For every child in every report, for every antiseizure agent or diet or hormonal treatment named, and for the classes the A1 table does not code (sodium-channel, valproate-type, benzodiazepine and other GABA-A modulators, SV2A, carbonic-anhydrase/multi-target, T-type, AMPA, fenfluramine-type, other), record one row: report id; child label as printed; class; agent as printed; status (tried, added, continued, stopped, not stated); seizure outcome AS STATED (a closed list: resolved, partial, none, worsened, not stated) with a verbatim locator; development outcome as stated (same list plus unchanged) with locator; a separate `worsening_statement` column holding the sentence verbatim if the text says seizures or the course worsened after or during the agent (never inferred from a failure to respond); co-therapy named at the time. `not stated` is not neutral and not negative.

## Counting rule
Counts per class and endpoint only: children exposed, with a stated outcome, with a stated worsening. Where a class has fewer than 3 children with a stated outcome it is `not scorable`; where fewer than 10 classifiable child-agent pairs exist in total the class-level test is `uninformative`, as declared in advance. Below n = 10 per class, report counts and no percentages.

## Cautions written first
Case reports favour successes and unusual courses (report bias); a child can appear in two reports (do not merge unless the text says so; list the possible links); a grouped table row is not a child; polytherapy outcomes are not attributable to one agent, and the extractor says so rather than attributing.

## After the extraction
SCI second-reads a sample (at least 20 percent of rows, all worsening rows) against the original reports before IT scores. Disclosure: IT saw A1 and the three IT31 agents before this brief; the extractor is not given them.
