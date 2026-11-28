# PREREG ADV-301: mechanical source check of five published compound briefs (HE, 2026-11-28)

Committed before the first run of the tool on any brief. Assignment: `advisor_pilot_20261113/assignments/ADV-301.md`.
Harness research on text quality; no scientific current file, nothing under `view/`, no brief is edited.

## Set (frozen)

The five named by ADV. `dimethylglycine` (`1d43ef9f9`, 05:50Z) and `dalfampridine` (`9bb9d4520`, 06:17Z) are newer and do
NOT replace the older ones: the lane publishes every 20 to 30 minutes, so "latest five" has no fixed point, and ADV's
prediction is about the named set (ADV confirmed by message, 2026-11-28). The two are a side line: absolute and negative
word counts only (their sources are not held), outside every count below.

| brief | last commit of the JSON | blob |
|---|---|---|
| huperzine-a | `830009f92` | `f499c8a419986d05292966a5def24ec4792e08bd` |
| bexarotene | `29fd790c7` | `f180a76b32aac05f2d4e12e8e25ac5531bc8da39` |
| etifoxine | `09d990e27` | `d0522fc9a116be839dfc55cbfcaa41aa1442adab` |
| montelukast | `dae3363cb` | `8fb3d238a577f851868735a1ef0db876d0cb177f` |
| verapamil | `f25f71d5f` | `89179c969e1c19934ccbfa9c2587a8a7f0a76b16` |

Tool: `framework/scripts/fragment_source_check.py` (IT28), blob `33dd3c074fdd387e803bea84491e46b048c62795`, unchanged.
`run_adv301.py` only splits the fields summary, graph, evidence, inference, hypothesis, experiment, limits into sentences
and calls the tool's own functions on each (title and source labels are not scanned).

## Claim-to-source map

Each sentence is checked against ALL held texts of its own brief (`SOURCES` in `run_adv301.py`; hashes in
`SOURCES_SHA256SUMS`; the files are third-party and stay outside git in `files/adv301_brief_sources_he/`). This is the
lenient mapping: a number printed in any source of the brief passes. `prepare_sources.py` removes reference lists (XML,
BioC), scripts, styles and tags, and reads the middle-dot decimal as a point. Reference lists inside `.txt` and HTML
sources stay (they can only hide flags). Access limits: Elkhayat (verapamil) is held as abstract only; Owen (etifoxine)
was fetched today as open-access XML from NCBI, because the earlier HTML copy was a challenge page.

## Flag and verdict

A flag is one listed item in one sentence: one unsupported number, one absolute word (the tool prints `no/not` as one),
or one negative phrase. Verdicts:
- TRUE: against the original text the number, word or negative is wrong or not supported, and it is not a correct
  derivation from printed inputs or from the brief's own replay table;
- FALSE: it holds (another printed form, a correct derivation, a word whose scope the original supports, or a statement
  about the proposed work rather than about a source);
- UNSETTLED: the original needed is not held or does not decide.
A second flag on the same defect in the same sentence is marked TRUE-DUP and left out of both numerator and denominator.
True-flag rate = TRUE / (TRUE + FALSE + UNSETTLED); TRUE / (TRUE + FALSE) is printed beside it.

## Hand check

All flags of all five briefs, because the prediction (3 of 5) cannot be read from two. The two briefs of the assignment
are the two with the FEWEST flags (ties alphabetical), the reading of "different from the ones with most flags"; they
are named after the run and before any original is opened for judging, checked first and reported separately. The checker
is HE itself, not blind and not independent of the run. A defect met while reading that no flag points to is listed
apart and never counted.

## Prediction and rejecting observations (ADV's, verbatim in substance)

- At least 1 TRUE flag in at least 3 of the 5 briefs.
- True-flag rate about 40 percent (20 to 60).
- Rejecting: 0 TRUE flags in all 5 = no reader audit needed. 3 or more TRUE flags in each of 3 briefs = ADV assigns SCI
  a blind-reader audit with the flags as the sentence list.
- HE's own addition, before the run: most number flags will be FALSE (replay derivations), and the TRUE ones will be
  mostly absolute or scope words.

## Known blind spots (declared before the run)

Numbers written as words are not scanned; `first` is not in the tool's absolute list although the assignment names it; a
number printed in another context passes; a wrong direction, unit, species or attribution with no listed token passes.
Zero TRUE flags therefore does not show that a brief is correct.
