# ADV-279 pre-registration, part 1: the held-bytes rule, in words, before the counted run (SCI, 2026-11-25, 2026-11-25T16:13Z)

Hypothesis level; reference genotype class; nothing here is medical advice. Actor `orchestrator` (SCI, `claude-sonnet-5-5`, effort high). Brief: `assignments/ADV-279.md`, plus ADV's message of the same day (state the wider rule first, report both counts by two routes, keep text-class and figure-class yield apart, do not pad). Held bytes only: no acquisition, no spend, no contact, no e-mail address to any service. Not the frozen RP-045 prediction; the sealed ADV-174 and ADV-175 folders are excluded from every scan.

## What had already been seen when this was written (disclosure)
An exploratory run, made before this text: the ADV-265 ranking script and its containment script, re-run on today's ledger (the old rule left 3 candidates outside the earlier batches), and one rough path scan for image, PDF and supplement files (it named about 64 of 109 studies as possibly coverable, with false hits likely). The rule below is therefore not blind to the size of the pool. It is fixed before any paper of this batch is opened and before the counted run.

## Population
Studies whose latest receipt is `partial_fulltext_read` with bytes held (ADV-265 rule), with at least one consumer unit (ADV-265 route 2) and at least one unread class (best state over all receipts is `not_read` or `captions_only`, among discussion, figures, tables, supplementary, limitations). Excluded: every study with a receipt whose workflow or outputs name ADV-265, ADV-269, ADV-272 or ADV-276.

## Old rule (ADV-265), kept for comparison
An unread class counts as contained only if the receipt's own held file scans as having it, or, for supplementary, a file named like a supplement carries the PMID.

## Wider rule (this batch)
An unread class counts as readable from held bytes if:
1. **figures:** an image file of one of the article's main figures is held anywhere under `files/`, or a PDF of the main article is held (pages can be rendered and looked at). Images of supplementary figures count toward supplementary, not figures.
2. **supplementary:** a supplement file of that article is held (PDF, spreadsheet, document, archive or supplementary image).
3. **discussion, tables, limitations:** the class is present in any held text of the article (XML, PDF, HTML or text), not only in the receipt's own file.

## Two routes, reported side by side
* **Route A, identifier path scan:** files under `files/` whose path carries the PMID or the PMCID as a whole number.
* **Route B, declared-name match:** the file names that the article's own held XML declares (figure graphics and supplementary-material links), looked up by name anywhere under `files/`. It does not depend on how a folder was named. A study without a held XML has no route B and is marked so.
A class enters the batch when either route finds it; the table shows which route found it. A file is only a candidate until it is opened and seen to belong to the article.

## What a figure reading means for the receipt
`figures` is recorded as read only when every main figure was opened as an image (the held image file, or the rendered page of the held PDF) and looked at; the result lists each image file with its sha256 (and, for a rendered page, the PDF's sha256, the page and the PNG's sha256). Otherwise it stays `captions_only` or `not_read`. A value read from a plot is labelled an image reading, with panel and row, and is approximate. The 4-of-10 yield of ADV-276 was measured on text classes, so this batch reports **text-class yield and figure-class yield separately**.
