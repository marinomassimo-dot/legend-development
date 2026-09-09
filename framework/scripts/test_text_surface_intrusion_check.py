#!/usr/bin/env python3
"""Regressions for text_surface_intrusion_check.

The positive fixture is the real one: the two-column extraction of PMID 21731849 that would
have produced a locator matching a sentence nobody wrote. It is reproduced here as a string so
the regression does not depend on `files/`, which is gitignored by design.

🔴 The negative fixtures matter more than the positive one, and two of them exist because the
FIRST version of this checker produced them in production on 2026-09-09. Run against the
PMID 20530675 supplement it reported chart axis ticks ('80', '70', '60') as page numbers and
repeated table rows ('Lung  M  S  +') as running headers. Neither is page furniture. A checker
that cries wolf on every bar chart and every table is one that gets switched off, so both
classes are now fixtures rather than field reports.

Note the deliberate consequence of the page-numbering chain rule: a SINGLE isolated integer is
no longer treated as page furniture, because nothing distinguishes it from a wrapped numeral in
prose. Real documents number consecutively, so the rule costs nothing where it matters.
"""

from __future__ import annotations

import importlib.util
import pathlib
import sys

_spec = importlib.util.spec_from_file_location(
    "tsic", pathlib.Path(__file__).with_name("text_surface_intrusion_check.py")
)
tsic = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tsic)
find_intrusions = tsic.find_intrusions


# The real case, 2026-09-09, PMID 21731849 pages 586-588, with the consecutive numbering a
# real article always carries.
REAL_INTERLEAVED = """\
Numerous studies have correlated loss of WWOX expression with cancer development,
586
suggesting a growth advantage for tumors with loss of WWOX.
Radiographic analyses in our mice reveal decreased bone density as compared with
587
wild type littermates, confirming reduced bone formation.
Using this protocol, osteosarcomas are detected in
588
100% of the post-natal mice prior to their death.
Analyses by others of other Wwox null rodent models failed to detect osteosarcomas.
"""

# The same document extracted in reading order: the furniture is gone.
REAL_CLEAN = """\
Numerous studies have correlated loss of WWOX expression with cancer development,
suggesting a growth advantage for tumors with loss of WWOX.
Radiographic analyses in our mice reveal decreased bone density as compared with
wild type littermates, confirming reduced bone formation.
Using this protocol, osteosarcomas are detected in
100% of the post-natal mice prior to their death.
Analyses by others of other Wwox null rodent models failed to detect osteosarcomas.
"""

# Page numbers where page numbers belong: between finished sentences. No quote can be damaged.
BENIGN_PAGE_BREAK = """\
These results indicate that WWOX expression is altered in tumours.
586
The next section describes the mouse model in detail.
587
A further section describes the cell lines used.
588
A final section describes the statistics.
"""

# Field report, 2026-09-09: chart axis ticks on a figure page of the PMID 20530675 supplement.
# They descend and step by ten, so they are not a page-numbering chain.
CHART_AXIS_TICKS = """\
Colony formation assay for KHOS, KHOS EV and KHOS
80
70
60
WWOX stable cells showing reduced ability of colony
50
formation compared to the control clone.
"""

# Field report, 2026-09-09: repeated table rows in the same supplement. They repeat, they are
# short, and they are separated by wide inter-column gaps — a table, not a header.
REPEATED_TABLE_ROWS = """\
Distal femur       R            60             S          -
Lung               M                           S          +
7     9     M     Proximal humerus   B                     R          -
Lung               M                           S          +
8     4     F     Distal femur       B                     S          +
Lung               M                           S          +
9     19    M     Distal femur       R            70       S          -
"""

RUNNING_HEADER = """\
Molecular analysis of osteogenesis markers in bones reveals that WWOX
WWOX in bone biology and osteosarcoma
deletion results in decreased levels of osteoblastic genes.
And more complete text follows here to pad the document.
WWOX in bone biology and osteosarcoma
Another complete sentence sits here.
WWOX in bone biology and osteosarcoma
A third complete sentence sits here.
"""


def test_real_interleaved_case_is_caught() -> None:
    found = find_intrusions(REAL_INTERLEAVED)
    pages = [f for f in found if f["kind"] == "page_number"]
    assert len(pages) == 3, found
    target = [f for f in pages if f["intrusion"] == "588"]
    assert len(target) == 1, found
    # The whole point: the reconstruction shows the two halves a quote must not span.
    assert "osteosarcomas are detected in" in target[0]["reconstructed"]
    assert "100% of the post-natal mice" in target[0]["reconstructed"]


def test_reading_order_extraction_is_clean() -> None:
    assert find_intrusions(REAL_CLEAN) == []


def test_page_numbers_between_sentences_are_not_reported() -> None:
    """Every previous line ends with '.', so no quote can be damaged. Must stay silent."""
    assert find_intrusions(BENIGN_PAGE_BREAK) == []


def test_chart_axis_ticks_are_not_page_numbers() -> None:
    """Field-reported false positive, 2026-09-09. Ticks descend; they form no numbering chain."""
    assert find_intrusions(CHART_AXIS_TICKS) == []


def test_repeated_table_rows_are_not_running_headers() -> None:
    """Field-reported false positive, 2026-09-09. Wide inter-column gaps mark a table row."""
    assert find_intrusions(REPEATED_TABLE_ROWS) == []


def test_running_header_inside_a_sentence_is_caught() -> None:
    found = find_intrusions(RUNNING_HEADER)
    headers = [f for f in found if f["kind"] == "running_header"]
    assert len(headers) == 1, found
    assert headers[0]["intrusion"] == "WWOX in bone biology and osteosarcoma"
    assert "osteoblastic genes" in headers[0]["reconstructed"]


def test_the_detector_distinguishes_the_two_extractions() -> None:
    """Proof the positive test is not vacuous: a detector that always returned [] would pass
    every negative test above, so assert the two extractions of ONE document differ."""
    assert find_intrusions(REAL_INTERLEAVED) != find_intrusions(REAL_CLEAN)
    assert find_intrusions(REAL_CLEAN) == []


# --------------------------------------------------------------------------------------
# 🔴 Regressions for the DISPERSION test, added 2026-09-09 from the second production run
# (PMID 18460020). Each of the three encodes a case that actually occurred; the third is the
# counterexample that decided the SHAPE of the fix and would be invisible without it.
# --------------------------------------------------------------------------------------

# PyMuPDF get_text() emits ONE TABLE CELL PER LINE, so a table's repeated values arrive as
# short repeated lines with no inter-column gaps for TABLE_ROW_RE to catch. On PMID 18460020
# this produced 25 false positives on a 7-page paper.
_PROSE = ["Supporting prose that carries the argument forward in an ordinary way."] * 60

ONE_CELL_PER_LINE_TABLE = "\n".join(
    _PROSE +
    ["The frequencies of methylation were measured in every resected specimen and the",
     "counts are given in Table 1 below, which reports each subgroup separately.",
     "Table 1. Association with clinicopathological findings",
     "Lymphatic vessels infiltration", "Negative", "3 (9%)", "2 (6%)", "1 (3%)", "0.881",
     "Positive", "29 (91%)", "23 (72%)", "6 (19%)",
     "Venous vessels infiltration", "Negative", "5 (16%)", "2 (7%)", "3 (9%)", "0.057",
     "Positive", "27 (84%)", "23 (71%)", "4 (13%)",
     "Lymph node metastasis", "Negative", "7 (22%)", "3 (9%)", "4 (13%)", "0.026",
     "Positive", "25 (78%)", "22 (69%)", "3 (9%)",
     "and the analysis was repeated for every subgroup listed above without exception."]
    + _PROSE)


def test_repeated_table_cells_emitted_one_per_line_are_not_running_headers() -> None:
    """The defect this fix exists for: no column gaps to detect, so the earlier exclusion
    could not fire and legitimate table values were reported as page furniture."""
    found = find_intrusions(ONE_CELL_PER_LINE_TABLE)
    bad = [f for f in found if str(f.get("intrusion", "")) in
           {"Negative", "Positive", "3 (9%)", "4 (13%)", "1 (3%)"}]
    assert bad == [], bad


def test_a_genuine_header_spread_across_the_document_is_still_caught() -> None:
    """Proof the fix does not simply silence the detector: the SAME repeated line, dispersed
    the way page furniture actually is, must still be reported.

    NOTE the varied surrounding sentences. An earlier version of this fixture repeated ONE
    sentence around every header, which made those sentences repeat often enough to be
    classified as furniture themselves - and a furniture line between two furniture lines is
    correctly NOT an intrusion into a sentence. The tool was right and the fixture was wrong.
    """
    header = "Cancer Sci | July 2008 | vol. 99 | no. 7"
    doc: list[str] = []
    for index in range(4):
        doc += [f"clause number {index} runs past the page boundary and does not end here",
                header,
                f"and it resumes below in lower case for block {index} of the article."]
        doc += [f"Filler sentence {index}-{n} carrying the argument forward." for n in range(60)]
    found = find_intrusions("\n".join(doc))
    assert any(f["kind"] == "running_header" and f.get("intrusion") == header
               for f in found), found


def test_dispersion_is_measured_by_span_and_not_by_gap_between_occurrences() -> None:
    """🔴 THE COUNTEREXAMPLE THAT CHOSE THE SHAPE OF THE FIX. The separator '|' of a running
    header is emitted as its own line, so its occurrences cluster in threes with a median gap
    of 2 - yet it is genuine page furniture, spanning 70% of the document. A median-gap test
    would have discarded real furniture in order to remove false furniture; a span test keeps
    it. Without this test the two designs are indistinguishable on every other case."""
    doc: list[str] = []
    for index in range(4):
        doc += [f"clause number {index} is cut off mid-sentence by the furniture below",
                "Cancer Sci", "|", "July 2008", "|", "vol. 99", "|", "no. 7",
                f"and then continues in lower case on page {index} of the article."]
        doc += [f"Ordinary prose {index}-{n} continuing the paragraph." for n in range(60)]
    found = find_intrusions("\n".join(doc))
    assert any(str(f.get("intrusion")) == "|" for f in found), \
        "the '|' separator is genuine furniture and must survive the dispersion test"


def _run() -> int:
    failures = 0
    for name, function in sorted(globals().items()):
        if name.startswith("test_") and callable(function):
            try:
                function()
                print(f"PASS {name}")
            except AssertionError as exc:
                failures += 1
                print(f"FAIL {name}: {exc}")
    print(f"\n{failures} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(_run())
