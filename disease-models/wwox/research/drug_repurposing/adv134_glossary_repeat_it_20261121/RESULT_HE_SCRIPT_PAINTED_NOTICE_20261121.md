# HE result (2026-11-21): the English passages that stood with no notice now have one

Reference-genotype class only. Limit stated first: the one new notice text was translated by me and checked by one blind reader of the same model family (no native specialist); the counts below are from one page load per language at 1280 px.

## Finding (measured, fr shareable page, then de and es)
Of the 50 ADV-131 passages, 19 were painted as English outside the two translated sections. They stand in 19 painted `<section>` elements:
- 16 need cards nested in `priorities-cur`. That parent section carries a notice above them, so these were never unlabelled (the earlier count by nearest id read them as unlabelled).
- 3 sections with no notice: `explore`, `navigate`, `candidates`. The cause is not the detector threshold: these sections paint their cards and lists with the page script from the embedded data object, and the static scan masks scripts, so it cannot see the passages.

## Decision: the notice, not the section
Extending `EN_SCOPE_SECTIONS` to these sections would change pages wherever the same hash stands (IT's checkpoint fact), and ADV-134 is measuring the translation first. So the three sections are labelled.

## Change
- UI key `sec_en_part` ("Some passages of this section are in English ... they are not translated"): the truthful partial wording, translated en/fr/de/es, blind check 4 of 4 OK (sonnet, effort low, read back from the hand-back; no correction).
- `SCRIPT_PAINTED_ENGLISH_SECTIONS = ("explore", "navigate", "candidates")` in `repurposing_view.py`: `mark_english_sections` inserts the partial notice after the heading of these sections when the static scan finds none; no other section changes.
- Guard `test_sections_painted_by_the_page_script_carry_the_partial_notice` (positive control by stripping the notice; the English page carries none; the translations differ from each other and from `sec_en_src`).
- Pages (full x 5, shareable x 5) and the package regenerated; `check` current; `i18n check` 0 stale; `test_repurposing_view_i18n` 31 OK.
- After: on fr, de and es shareable pages no painted ADV-131 passage stands in an id-bearing section without a notice; the 16 cards sit under the `priorities-cur` notice.

## Not done, still open (mine)
- The ranking-section notice wording: `sec_en_part` is now available for it, and the decision waits for the ADV-134 repeat.
- The section notice above the 16 cards still says the whole text is English ("not translated"); `sec_en_part` would be truer there too.
