#!/usr/bin/env python3
"""Regression tests for the public study deduplication runtime."""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import study_dedup_triage as triage  # noqa: E402


def _reference_lcs(a: str, b: str) -> int:
    """Textbook dynamic programme: the oracle for the bit-parallel bound."""
    previous = [0] * (len(b) + 1)
    for x in a:
        row = [0]
        for j, y in enumerate(b, 1):
            row.append(previous[j - 1] + 1 if x == y else max(previous[j], row[-1]))
        previous = row
    return previous[-1]


def _reference_best(query: str, titles: list[str]) -> tuple[float, int | None]:
    """The scan `match_row` used to run: every title, file order, strict `>`, no pruning."""
    best: tuple[float, int | None] = (0.0, None)
    for index, title in enumerate(titles):
        if title:
            ratio = triage.difflib.SequenceMatcher(None, query, title).ratio()
            if ratio > best[0]:
                best = ratio, index
    return best


def check_title_bound(failures: list[str]) -> None:
    """The LCS bound is exact, is a true upper bound, and `best_title` equals the full scan.

    Small alphabets on purpose: they force repeated characters, full matches (a carry into the
    guard bit), duplicate titles (ties) and empty titles — the cases a bound-ordered walk gets
    wrong if its stopping rule is off by one."""
    import random
    rng = random.Random(20260929)
    alphabets = ("ab", "abc", "abcdefgh", "abcdefghijklmnopqrstuvwxyz ", "aé漢字 ")
    for case in range(400):
        alphabet = alphabets[case % len(alphabets)]
        pool = ["".join(rng.choice(alphabet) for _ in range(rng.randint(0, 14)))
                for _ in range(rng.randint(1, 9))]
        titles = pool + [rng.choice(pool) for _ in range(rng.randint(0, 3))]   # duplicates: ties
        query = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 16)))
        key = tuple(titles)
        lengths = triage._TitleBound(key).lcs_lengths(query, key)
        for title, length in zip(titles, lengths):
            expected = _reference_lcs(query, title) if title else 0
            if length != expected:
                failures.append(f"LCS {query!r} vs {title!r}: {length} != {expected}")
                return
            if title:
                bound = 2.0 * length / (len(query) + len(title))
                ratio = triage.difflib.SequenceMatcher(None, query, title).ratio()
                if ratio > bound:
                    failures.append(f"bound {bound} below ratio {ratio} for {query!r}/{title!r}")
                    return
        got, want = triage.best_title(query, titles), _reference_best(query, titles)
        if got != want:
            failures.append(f"best_title {got} != full scan {want} for {query!r} in {titles!r}")
            return
    if triage.best_title("zzz", ["abc", "", "ab"]) != (0.0, None):
        failures.append("a query sharing no character must select nothing")
    if triage.best_title("abc", ["", "abc", "abc"]) != (1.0, 1):
        failures.append("an exact tie must go to the earlier title")
    # a real corpus sample: the shipped registry titles, perturbed, against the full scan
    root = Path(__file__).resolve().parents[4]
    records = triage.build_index(root)
    real = [record["norm_title"] for record in records]
    populated = [i for i, title in enumerate(real) if len(title) >= 18]
    for step, index in enumerate(populated[:: max(1, len(populated) // 12)][:12]):
        chars = list(real[index])
        for _ in range(rng.randint(0, 8)):
            chars[rng.randrange(len(chars))] = rng.choice("abcdefghijklmnopqrstuvwxyz ")
        query = "".join(chars)
        if triage.best_title(query, real) != _reference_best(query, real):
            failures.append(f"real-corpus sample {step}: best_title differs from the full scan")
            return


def main() -> int:
    failures: list[str] = []
    check_title_bound(failures)

    identifiers = triage.extract_identifiers(
        "PMID: 12345678 DOI 10.1000/example.1 PMCID PMC123456"
    )
    if identifiers["pmid"] != {"12345678"}:
        failures.append("PMID extraction failed")
    if identifiers["doi"] != {"10.1000/example.1"}:
        failures.append("DOI extraction failed")
    if identifiers["pmcid"] != {"PMC123456"}:
        failures.append("PMCID extraction failed")

    rows = triage.split_input(
        "First paper. Author A. 2020. PMID: 12345678\n"
        "Second paper. Author B. 2021. PMID: 23456789\n"
        "Third paper. Author C. 2022. PMID: 34567890\n"
    )
    if len(rows) != 3:
        failures.append(f"line-per-record split expected 3 rows, got {len(rows)}")

    unknown = {"line": "99999991", "lineno": "1", "aggregate": "no", "raw": ""}
    if triage.match_row(unknown, [], {})["class"] != "NEW":
        failures.append("unknown bare PMID was not classified NEW")

    if triage.match_row(
        {"line": "xx", "lineno": "1", "aggregate": "no", "raw": ""},
        [],
        {},
    )["class"] != "INSUFFICIENT_METADATA":
        failures.append("short metadata was not classified INSUFFICIENT_METADATA")

    with tempfile.TemporaryDirectory() as temporary:
        workspace = Path(temporary)
        registry = workspace / triage.REGISTRY_FILES[0]
        registry.parent.mkdir(parents=True)
        registry.write_text(
            "## PAPER 001\n"
            "**Full title:** A public mechanistic WWOX study\n"
            "**Authors:** Example A\n"
            "**Year:** 2024\n"
            "**Identifier:** PMID: 45678901\n",
            encoding="utf-8",
        )
        records = triage.build_index(workspace)
        index = triage.build_identifier_index(workspace)
        known = {"line": "45678901", "lineno": "1", "aggregate": "no", "raw": ""}
        if triage.match_row(known, records, index)["class"] != "KNOWN_INTEGRATED":
            failures.append("known PMID was not classified KNOWN_INTEGRATED")

        registry.write_text(
            registry.read_text(encoding="utf-8")
            + "\n## PAPER 002\n"
            + "**Full title:** A second primary study\n"
            + "**Identifier:** PMID: 56789012\n"
            + "**Note:** This record cites unread PMID 67890123 as future work.\n",
            encoding="utf-8",
        )
        records = triage.build_index(workspace)
        index = triage.build_identifier_index(workspace)
        incidental = {
            "line": "67890123", "lineno": "1", "aggregate": "no", "raw": ""
        }
        result = triage.match_row(incidental, records, index)
        if result["class"] != "NEW":
            failures.append(
                "PMID cited only inside record prose was treated as record identity: "
                + result["class"]
            )

    # 🔴 THE EXACT SHAPE OF THE 2026-09-28 DEFECT. A promoted corpus placeholder is re-statused
    # and KEPT, so one PMID owns two paper-registry records: the stub, written first and therefore
    # standing first in physical file order, and the record that replaced it. `match_row` returned
    # the first match, so `PMID 30356099` was resolved by `CORPUS-STUB-059` (`superseded`) and the
    # batch queue's headline counted a paper as unprocessed that the registry holds at
    # partial-full-text depth with three receipts.
    with tempfile.TemporaryDirectory() as temporary:
        workspace = Path(temporary)
        registry = workspace / triage.REGISTRY_FILES[0]
        registry.parent.mkdir(parents=True)
        registry.write_text(
            "## CORPUS-STUB-059\n"
            "**Full title:** Genetic and phenotypic spectrum of WWOX\n"
            "**Identifier:** PMID 30356099 / DOI 10.1038/s41436-018-0339-3\n"
            "**Status:** superseded\n"
            "\n---\n\n"
            "## PAPER 117\n"
            "**Full title:** Genetic and phenotypic spectrum of WWOX\n"
            "**Identifier:** PMID 30356099 / PMCID PMC6752669 / DOI 10.1038/s41436-018-0339-3\n"
            "**Status:** processed\n"
            "**Evidence depth:** `partial_fulltext_read` - receipts FTR-20260811-30356099-01\n",
            encoding="utf-8",
        )
        records = triage.build_index(workspace)
        index = triage.build_identifier_index(workspace)
        if [record["id"] for record in records] != ["CORPUS-STUB-059", "PAPER 117"]:
            failures.append("fixture does not reproduce the two-record shape in file order")
        for anchor in ("PMID 30356099", "DOI 10.1038/s41436-018-0339-3"):
            verdict = triage.match_row(
                {"line": f"Spectrum of WWOX in twenty cases. - {anchor} - YEAR 2019",
                 "lineno": "1", "aggregate": "no", "raw": ""}, records, index)
            if verdict["match"] != "PAPER 117":
                failures.append(f"{anchor} resolved to {verdict['match']!r}, not the promoted "
                                "record PAPER 117")
            if verdict["class"] != "KNOWN_INTEGRATED":
                failures.append(f"{anchor} classified {verdict['class']}, not KNOWN_INTEGRATED")
            if "CORPUS-STUB-059" not in verdict["reason"]:
                failures.append("the reason does not name the superseded record it beat")

        # A stub with NO promoted sibling still resolves to itself: the fix is a tie-break among
        # several records, not a demotion of placeholders.
        registry.write_text(
            "## CORPUS-STUB-060\n"
            "**Full title:** An unpromoted catalogue entry about WWOX\n"
            "**Identifier:** PMID 30356100\n"
            "**Status:** not_processed\n",
            encoding="utf-8",
        )
        records = triage.build_index(workspace)
        index = triage.build_identifier_index(workspace)
        alone = triage.match_row({"line": "30356100", "lineno": "1", "aggregate": "no", "raw": ""},
                                 records, index)
        if alone["class"] != "CORPUS_CATALOGUED" or alone["match"] != "CORPUS-STUB-060":
            failures.append("a lone corpus placeholder stopped resolving to itself: "
                            + f"{alone['class']} / {alone['match']}")
        if "most promoted" in alone["reason"]:
            failures.append("a single match reported a tie-break that did not happen")

    # 🔴 The tie-break is WITHIN a surface. Ranking the class across surfaces was measured and
    # rejected: a `LIT-...` tracking-log row is KNOWN_INTEGRATED to `resolve_known_class`, so it
    # would beat a corpus stub in the paper registry and turn "screened" into "done" for ~140
    # seeds. The paper registry answers first, exactly as `classify_seen_files` says.
    with tempfile.TemporaryDirectory() as temporary:
        workspace = Path(temporary)
        papers = workspace / triage.REGISTRY_FILES[0]
        papers.parent.mkdir(parents=True)
        papers.write_text("## CORPUS-STUB-087\n**Full title:** A catalogued WWOX paper\n"
                          "**Identifier:** PMID 33914858\n**Status:** not_processed\n",
                          encoding="utf-8")
        tracking = workspace / triage.REGISTRY_FILES[1]
        tracking.parent.mkdir(parents=True, exist_ok=True)
        tracking.write_text("## LIT-0110\n**Full title:** A catalogued WWOX paper\n"
                            "**Identifier value:** PMID 33914858\n**Status:** discovered\n",
                            encoding="utf-8")
        records = triage.build_index(workspace)
        index = triage.build_identifier_index(workspace)
        crossed = triage.match_row({"line": "33914858", "lineno": "1", "aggregate": "no",
                                    "raw": ""}, records, index)
        if crossed["match"] != "CORPUS-STUB-087":
            failures.append("a tracking-log row outranked a paper-registry placeholder: "
                            + f"{crossed['match']} / {crossed['class']}")

    if failures:
        print("FAIL")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print("OK — study deduplication guards passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
