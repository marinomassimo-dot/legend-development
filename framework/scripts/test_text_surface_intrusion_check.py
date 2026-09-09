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
