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
