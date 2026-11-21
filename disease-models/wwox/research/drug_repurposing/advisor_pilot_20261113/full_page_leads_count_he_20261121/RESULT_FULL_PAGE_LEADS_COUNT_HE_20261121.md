# Count of the two full-edition leads from ADV-129 (HE, 2026-11-21): counted, not fixed

Mode: **static** (rendered HTML files, not painted text), heuristic, one pass; script `english_fragments_static_count.py` (run `python3 -I` from the repository root). Text nodes outside `<script>`, `<style>`
and elements marked `class="orig"` or `lang="it"`/`lang="en"`; a node counts as English-looking when it has at least two English function or content words from a short list and none of the page
language's own. A painted scan (the ADV-128 method) would exclude hidden nodes and is the next step if a fix is decided.

| Lead | Count |
|---|---|
| English-looking text nodes on the FULL fr page | 1060 of 4942 distinct nodes |
| ... on the FULL de page | 528 of 4938 |
| ... on the FULL es page | 718 of 4940 |
| `4-PBA / acido fenilbutirrico` (Italian compound name) on the FULL EN page | 2 occurrences (the shareable EN page: 0) |

The samples are long authored English sentences of the evidence and method sections (`(a decision from the data that exist) are different statements ...`, `(the sources were asked and returned no
row for the record)`, `1 catalogue family(ies); L2 over 2 (family, need) cell(s): ...`), not a few fragments: the class is far above a few dozen nodes, so by ADV's rule it is reported before any fix.
The detector over-counts (a table cell can hold a code and an English gloss; the fr list has the most because French shares fewer function words with the short English list), so the figure is an upper
bound on a class, not a defect count. The shareable edition, which is the one that leaves the repository, is clean by the ADV-128 detectors except the known false positives.

Decision left to ADV: whether the full-edition English-authored passages should enter the content catalogue for fr/de/es (a translation job of the size of ADV-129), or stay English as the source
language of those sections with a one-line label as the pilot cases now have. The 2 compound-name occurrences are a small fix and can go with the next generator change.
