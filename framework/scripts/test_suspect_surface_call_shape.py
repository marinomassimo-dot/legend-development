#!/usr/bin/env python3
"""Regressions for the ARGUMENT-SHAPE guard on `_refuse_suspect_surface`.

🔴 WHY THIS FILE EXISTS. On 2026-09-09, while reading PMID 16223882, the screen was called
as `_refuse_suspect_surface(text, path_string)` — arguments inverted. It returned normally.
`path` is not touched before the loop, so the loop screened the FILENAME, which holds no
control characters, and the caller read the silent return as CLEAN. The surface it was
actually asking about carried 191 C0 controls and zero comparators; the correct call refuses
it. A screen whose failure mode is a silent pass is worse than no screen, because the caller
now has a green result to point at.

The mistake was caught only because the same reader had independently counted the raw
characters and disbelieved the verdict. These tests are what makes that catch mechanical.

Each test names the failure it prevents, so a future reader deleting one knows the cost.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import deepdive_manifest as dm  # noqa: E402

CLEAN = "The quick brown fox jumps over the lazy dog. P < 0.05 and 25 microgram were loaded."
SUSPECT = "Wwox\x01/\x01 mice were compared with controls at P \x02 0.05 across every cohort."


def _case(name, fn, expect, needle=""):
    try:
        fn()
    except expect as exc:  # noqa: PERF203 - one case per call, clarity over speed
        if needle and needle not in str(exc):
            return f"FAIL {name}: raised {expect.__name__} without {needle!r}"
        return f"PASS {name}"
    except Exception as exc:  # noqa: BLE001
        return f"FAIL {name}: raised {type(exc).__name__} instead of {expect.__name__}: {exc}"
    return f"FAIL {name}: did not raise {expect.__name__}"


def main() -> int:
    results = []
    tmp = Path(__file__).resolve().parent / "_suspect_shape_fixture.txt"
    tmp.write_text(CLEAN, encoding="utf-8")
    try:
        # 1. The behaviour that must NOT change: a correct call over clean text still passes.
        try:
            dm._refuse_suspect_surface(tmp, CLEAN)
            results.append("PASS correct_call_over_clean_text_returns")
        except Exception as exc:  # noqa: BLE001
            results.append(f"FAIL correct_call_over_clean_text_returns: {type(exc).__name__}: {exc}")

        # 2. The behaviour that must NOT change: a correct call over a defective surface refuses.
        results.append(_case(
            "correct_call_over_suspect_text_refuses",
            lambda: dm._refuse_suspect_surface(tmp, SUSPECT),
            ValueError, "SUSPECT text surface"))

        # 3. THE DEFECT: arguments inverted. Before the guard this returned None — a silent
        #    CLEAN on a surface nobody screened.
        results.append(_case(
            "inverted_arguments_are_refused",
            lambda: dm._refuse_suspect_surface(SUSPECT, str(tmp)),
            TypeError, "must be os.PathLike"))

        # 4. The inversion is refused even when the text happens to be clean: the guard is
        #    about the SHAPE of the call, not about what the text turns out to contain.
        results.append(_case(
            "inverted_arguments_refused_even_for_clean_text",
            lambda: dm._refuse_suspect_surface(CLEAN, str(tmp)),
            TypeError, "must be os.PathLike"))

        # 5. The mirror image: the path passed as the part to screen. This is exactly what the
        #    inverted call ended up screening, and screening a filename always passes.
        results.append(_case(
            "path_string_as_part_is_refused",
            lambda: dm._refuse_suspect_surface(tmp, str(tmp)),
            TypeError, "not its text"))

        # 6. Same, with the bare filename.
        results.append(_case(
            "bare_filename_as_part_is_refused",
            lambda: dm._refuse_suspect_surface(tmp, tmp.name),
            TypeError, "not its text"))

        # 7. A non-str part is a caller error, not something to coerce.
        results.append(_case(
            "non_str_part_is_refused",
            lambda: dm._refuse_suspect_surface(tmp, b"bytes are not text"),
            TypeError, "must be the document text"))

        # 8. A legitimate document that merely CONTAINS its own filename is not refused: the
        #    guard compares the whole stripped part, never a substring. Without this the guard
        #    would refuse real surfaces — a false positive is how a guard gets deleted.
        try:
            dm._refuse_suspect_surface(tmp, f"Supplementary data are provided in {tmp.name} alongside the main text of the article.")
            results.append("PASS document_mentioning_its_own_filename_still_passes")
        except Exception as exc:  # noqa: BLE001
            results.append(f"FAIL document_mentioning_its_own_filename_still_passes: {type(exc).__name__}: {exc}")

        # 9. Multi-part calls keep working, and a defect in a later part is still found.
        results.append(_case(
            "suspect_text_in_a_later_part_is_still_found",
            lambda: dm._refuse_suspect_surface(tmp, CLEAN, SUSPECT),
            ValueError, "SUSPECT text surface"))
    finally:
        tmp.unlink(missing_ok=True)

    for line in results:
        print(line)
    failed = [r for r in results if r.startswith("FAIL")]
    print(f"\n{len(results) - len(failed)}/{len(results)} PASS")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
