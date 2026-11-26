# Ketamine report pilot, rendering side (ADV-201)

Status: pilot, hypothesis level, not medical advice. The brief is a LAYOUT pilot on stand-in content: every sentence in `pilot_stand_in.json` is condensed from `view/research_reports/ketamine.json` (evidence reviewed through 22 November 2026), and every field that file does not state is the literal token PLACEHOLDER, printed in bold on the page. SCI's content pack (ADV-200, `../content/`) replaces the stand-in. Nothing here is published; the old PDF and `framework/scripts/repurposing_research_reports.py` are untouched.

## Files

| File | What it is |
|---|---|
| `build_pilot.py` | The renderer. PyMuPDF Story for text and tables; the evidence graph is drawn natively on its own page. `python3 -I build_pilot.py` writes `out/ketamine_pilot_20261123.pdf`. Same input gives the same bytes. |
| `pilot_stand_in.json` | The stand-in content: decision table rows (statement, type, model and endpoint, numbered reference with locator), reading guide, graph nodes, methods, appendix rows. |
| `out/ketamine_pilot_20261123.pdf` | The one pilot PDF, 6 pages A4: decision evidence first, evidence graph, Methods and coverage, Appendix A (negative and ambiguous), Appendix B (quantities with their definitions), one numbered bibliography. |
| `out/pages/p1.png` to `p6.png` | The pages as checked by eye (80 dpi). |
| `layout_test_figure.py`, `out/layout_test_page.pdf`, `out/pages/layout_test.png` | A figure-route test with SYNTHETIC values, labelled as such. It is not part of the brief. |

## What the pilot shows

* The criteria of the meeting record (agenda item 2) a, b and c: decision table first with ANCHOR and RIVAL flags; three evidence classes kept apart (WWOX preclinical, other indications, proposed comparison); numbered references with locators; Methods and coverage; appendices; an evidence graph in which every edge is OBSERVED (heavy line) or HYPOTHESISED (dashed), with a double bar at the break in transfer. Status is carried by line style, fill pattern and words, never by colour.
* Criterion d (second quantitative figure) is deliberately not drawn: the stand-in has no assay, unit and exposure definitions. The page states the rule instead.
* Criterion f (cold read) is not self-certified. A "Where to find what" box points to the anchor, the compound measured in Wwox tissue, the weakening evidence and the measurement that would change the choice, so a fresh reader can be tested against it.

## What the pilot cannot do, and the cheapest answer

* **Internal links.** Reference numbers link out to the source (108 live links); a reference number does not jump to the bibliography page, because Story does not wire internal anchors. A small post-pass with `page.insert_link` would add them.
* **Backgrounds in tables.** In PyMuPDF 1.28.2 a background on a table cell, a table header or an inline span leaves a displaced 8 pt strip of that colour elsewhere on the page. The pilot therefore uses borders and words, no shaded cells. A shaded header would need drawing the tables natively.
* **Repeated table headers.** A table that breaks across a page does not repeat its header; each evidence class has its own header and the pilot's tables fit, but a longer pack may not.
* **The graph is hand laid out** (six nodes, fixed coordinates; text that overflows a node raises an error). A different graph shape needs new coordinates. Graphviz is not installed here; an automatic layout would need it (EPL licence) or networkx with matplotlib (BSD).
* **Accessibility.** No tagged PDF and no alternative text; PyMuPDF does not write structure tags. Only the document language is set. A tagged PDF would need another renderer.
* **Figure library.** matplotlib 3.10.3 works for a vector figure with embedded TrueType fonts, but it lives in `~/.local/legend-figures-libs`, appended to `sys.path` after the system packages inside the pilot script only. Proposal, one line: a rebuild or a test should read a `LEGEND_FIGURE_LIBS` environment variable that defaults to that folder, and skip the figure test when it is absent.
* **Panel-level locators and animal denominators** are PLACEHOLDER until the content pack supplies them.

## Increment 2: the final PDF from the content pack (2026-11-23)

* `build_final.py` reads `../content/` (A to F: markdown tables, the two graph TSVs) and writes `out/ketamine_brief_pilot_final.pdf`. Run: `python3 -I build_final.py --landed <main sha>`; the sha is checked with git to contain the content commit. Output is deterministic (two runs compare byte-equal).
* Built from content commit d2ed139d4 (SCI's three corrections), landed on main as 00b47c935e7c. Both shas and the SHA-256 of all nine input files are printed on the last page, written into the PDF keywords, and the two shas are in every page footer.
* 16 pages: decision evidence (Blocks 1 to 4), the 18-node, 19-edge evidence graph with its edge list, the one measurement that would change the choice, negative results, the exposure table in three matrices (nominal bath, total plasma, CSF), conversions, methods, references with PMID and DOI links, provenance.
* Rows read from the abstract only carry a heavy bar at the left edge and the words [ABSTRACT-ONLY]. The one residual from the content team (the sIPSC plus/minus statistic of Breton et al. is not named) is flagged on page 1.
* Page images used for the check: `out/final_pages/f01.png` to `f16.png` (85 dpi). The blind cold read is not self-certified.
* What the builder cannot do: the graph layout is fixed per node id (an unknown id or a changed edge set needs new coordinates); no internal links, no tagged PDF, no alternative text.
* Story trap found on this pack: a heading placed straight after a table made pymupdf's Story loop for ever once the corrected rows moved the page break. Every table is now followed by a 1 pt spacer block, and `story_doc` stops with an error after 25 pages instead of hanging.

## Revision after the first cold read (2026-11-23)

* Built from content commit a37f1def8 (SCI's cold-read fixes), landed on main as 0faa71c03c44. The pack's `00_README_CONTENT_PACK.md` says what to render; `INTERNAL_NOTES_NOT_FOR_READERS.md` is not rendered and not hashed. The sections are now rendered by the pack's own titles (no hand-written claims box any more, so nothing there can go stale; the page-order line is the only text of mine on page 1 and it is computed).
* Repeated table headers: Story reports where each row landed; a header copy is inserted before the first row of every continuation page, and a spacer row keeps the copy from stranding at a page foot. A heading is kept with its table the same way. Story ignores `page-break-before` and loops on it after a table, so no forced break is used. A spacer that fills a page to within 1 pt makes Story drop the rest of the text silently (found on the CSF matrix); the spacer stops 5 pt short and every Story is checked for the words at the end of its text.
* Reflow: the edge list shares pages with the deciding measurement, the negative-results and quantitative section runs without forced page breaks, and Methods, References and Provenance flow together. 14 pages; the pages that are not full end a section before a change of orientation.
* Figure 1: four columns, five elbows instead of ten, white halos so a heavy line bridges a lighter one at a crossing; node text 7.5 to 8.2 pt (smallest scale 0.92), edge tags 8 pt. Edge status OBSERVED solid, INFERRED dashed, HYPOTHESISED dotted; `context_only` (G13) is drawn lightly in grey; node kinds observation, inference, claim (double outline), alternative (dashed), experiment (black), gap (dotted). The key draws the lines and boxes themselves.
* Typography: plus-minus sign, micro sign (uM), degree sign (35 C) are applied to all displayed text; bold inside a table cell is set to the cell's size (Story draws it larger otherwise).

## Second round after the cold read (2026-11-23)

* Page order is now: decision evidence and the deciding measurement (portrait, pp. 1 to 6), Figure 1 (landscape), then the edge list, the negative and ambiguous results and the quantitative details (landscape), then Methods, References and build provenance (portrait). This removed the two-thirds-blank page that came before the figure.
* A heading is kept with its table even when the heading's own section has no text of its own (Block 4 had stranded its heading and header at the foot of a page). The headings since the last paragraph are all paired with the next table, and the file title and intro lines no longer release the chain.
* A spacer after a table that ends exactly at the page foot can spill onto an empty last page of a Story; empty trailing pages are dropped.
* Figure 1: each node's text is set at the largest size from 10 down to 7.2 pt that fits its box without shrinking (probed on a scratch page, so nothing is drawn twice). The dashed INFERRED pattern is the same in the figure and in the key; `CONTEXT ONLY` is accepted as an edge status in the pack and drawn lightly; the two bus lanes (G17, G18) are moved right and the horizontal edges carry their tag beside the hub.
* The provenance heading reads "Build provenance (for the project team)".

## Content changed after the build (2026-11-26)

* `../content/A_decision_evidence.md` row W3 and ledger row V3 were corrected on 2026-11-26 (IT27; the Table S1 baseline is pooled over all slices, and brilliant blue FCF's duration median is as low as carbenoxolone's). The PDFs in `out/` predate this and were not rebuilt.
