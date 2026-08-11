#!/usr/bin/env python3
"""Does every locator's quote actually occur in the artifact it was taken from?

## The gap this fills, and the one it does not

`deepdive_manifest --verify-artifacts` already matches every text locator against its declared
artifact, character for character. It can only do that for **schema-v2** manifests, because
only those declare an artifact per locator. The seven legacy manifests in this corpus declare
none, so their quotes have never been matched against anything — not once, by any tool, since
they were written.

That is not a hypothetical debt. Audited on 2026-08-10, `PMID 32000863` had **five locators out
of twenty-two that did not occur in its own XML**, all failing for one reason: they had been
*transcribed as the page reads* rather than *extracted as the artifact contains*. Superscripts
lost their spacing, cross-references lost their figure number, citation markers vanished. None
changed meaning; two lost information — which figure a result points at, and which references
support which clause.

**A locator captured by transcription is not a locator captured from the artifact**, and
nothing sees the difference until something matches exactly. This script is that something,
for the manifests the validator cannot reach.

🔴 **It is the mechanical half of `legend-locator-audit` and never a substitute for it.** This
asks only whether the sentence EXISTS in the source. Whether the sentence SUPPORTS the
proposition written above it — overshoot, undershoot — is a judgement, it is what that skill's
blind auditor exists for, and no amount of string matching approaches it. Running this first is
worth it because it is free and it removes the triples that would have wasted the auditor's
attention.

## Usage

    locator_audit.py                      # every manifest, artifacts resolved from the corpus
    locator_audit.py --pmid 32000863      # one study
    locator_audit.py --strict             # non-zero exit when a quote is not found

`--corpus` overrides where the artifacts live, because `files/` is gitignored and exists in
one checkout while sessions run in worktrees. Without a readable corpus this script reports
that it could not look, which is a different statement from finding nothing wrong.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import deepdive_manifest as dm  # noqa: E402
import surface_census as census  # noqa: E402

ROOT = HERE.parents[1]
TEXT_SUFFIXES = {".xml", ".html", ".htm", ".txt", ".docx"}

# 🔴 How much of this backlog is a debt with a floor, and how much is a tap still running.
# Verified in the code rather than assumed, and it comes out NARROWER than it was first put
# to me: `fulltext_receipts.append_receipt` calls `require_work_manifest(..., strict=True)`,
# which runs the validator with `verify_artifacts` and `require_current_schema` BEFORE the
# receipt is chained — so a quote that is not in its artifact cannot ride in behind a new
# complete read. But `require_work_manifest` returns early for anything that is not a
# `complete_fulltext_read` contemporaneous receipt: partial reads, legacy reconstructions and
# receipt corrections are explicitly untouched, and the docstring says so on purpose.
#
# So the honest statement is not "this cannot recur". It is: the strongest claim is gated, and
# the door that remains is narrower and real. Today nothing exploits it — the partial reads in
# this corpus write dossiers rather than manifests — which is a fact about today, not a
# property of the design. Saying "closed" would be exactly the over-claim this tool exists to
# find in other people's sentences.
CLOSED_SET_NOTE = (
    "\nSCOPE OF THIS BACKLOG: every quote above sits in a manifest written before the "
    "persistence gate existed. `append_receipt` now validates snippets against their declared "
    "artifact before a new `complete_fulltext_read` is chained, so this class cannot enter "
    "again behind the strongest claim. It is NOT sealed: `require_work_manifest` deliberately "
    "exempts partial reads, legacy reconstructions and receipt corrections, so a locator "
    "added by one of those is still unchecked at write time. A debt with a floor, plus one "
    "narrower door — not a tap, and not a closed set either."
)


def manifests(root: Path, disease: str) -> list[Path]:
    directory = root / "disease-models" / disease / "research" / "deepdive_manifests"
    return sorted(directory.glob("PMID*.json")) if directory.is_dir() else []


def text_artifact(pmid: str, corpus: Path) -> Path | None:
    """The structured surface a legacy manifest would have to declare, if one exists.

    Deliberately only structured text. A PDF is refused as a text surface by
    `_artifact_text` and rule 5d says so for good reason, so a manifest whose only local file
    is a PDF is reported as unauditable rather than matched against a text layer this
    repository does not trust.
    """
    if not corpus.is_dir():
        return None
    by_pmid, _ = census.corpus_index(corpus)
    best: Path | None = None
    for name, kind in by_pmid.get(pmid, []):
        if kind == "structured" and Path(name).suffix.lower() in TEXT_SUFFIXES:
            candidate = corpus / name
            if best is None or candidate.stat().st_size > best.stat().st_size:
                best = candidate
    return best


def audit_one(path: Path, corpus: Path) -> dict:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    pmid = str(manifest.get("pmid", path.stem.replace("PMID", "")))
    locators = manifest.get("verbatim_locators")
    entries = locators.get("entries") if isinstance(locators, dict) else None
    result = {"pmid": pmid, "schema": manifest.get("schema_version"), "entries": 0,
              "matched": [], "missing": [], "image": [], "artifact": None, "reason": None,
              "cause": None}
    if not isinstance(entries, list) or not entries:
        result["reason"] = "no locator entries (waived or empty)"
        return result
    result["entries"] = len(entries)

    # 🔴 A schema-v2 manifest DECLARES its artifacts, and a locator may legitimately quote a
    # supplement rather than the article. Guessing one file per study and matching everything
    # against it manufactures failures: the first run of this script reported entry 16 of
    # PMID 37519886 as missing, when that manifest passes `--verify-artifacts` because the
    # quote is in a surface it declares and the guess did not pick. Declared beats resolved
    # wherever a declaration exists; resolution is the fallback for the legacy manifests,
    # which are the only ones that need it.
    declared = [str(item.get("path", "")) for item in manifest.get("source_artifacts") or []
                if str(item.get("kind")) in {"article_text", "supplement_text", "table"}]
    # A declared path is repository-relative and `files/` is gitignored, so in a worktree it
    # resolves to nothing while the same bytes sit under the corpus this run was pointed at.
    # Trying both is the difference between auditing a manifest and reporting it unauditable
    # — and the first run of this script did the latter for a supplement it could have read.
    surfaces: list[Path] = []
    absent: list[str] = []
    for relative in declared:
        for candidate in (ROOT / relative, corpus / Path(relative).name):
            if candidate.is_file():
                surfaces.append(candidate)
                break
        else:
            absent.append(relative)
    if not surfaces:
        artifact = text_artifact(pmid, corpus)
        if artifact is None:
            # 🔴 Two opposite causes wear the same word, and collapsing them was a defect.
            # "This study has no structured surface anywhere" is a fact about the paper, and
            # the reading has to live with it. "This study declares a surface that is not in
            # THIS tree" is a fact about the checkout, it is the COMMON case rather than an
            # edge — anyone running from a branch other than the one that fetched the
            # artifacts lands here — and it is repaired by fetching, not by re-reading. One
            # is a limit, the other is an errand, and a reader who cannot tell them apart
            # will treat both as neither. It is the same distinction `NOTHING AUDITED` draws
            # for a whole run, which had simply never been drawn per manifest.
            result["reason"] = (
                f"declares {len(absent)} text surface(s) that are absent from this tree "
                f"({', '.join(absent)}) — fetch them, this is not a defect in the reading"
                if absent else
                "no structured text surface declared or in the corpus — unauditable here")
            result["cause"] = "surface_absent_here" if absent else "no_surface_known"
            return result
        surfaces = [artifact]
    result["artifact"] = ", ".join(path.name for path in surfaces)

    body = ""
    for path in surfaces:
        try:
            text, _abstract = dm._artifact_text(path, "article_text")
        except Exception as exc:  # noqa: BLE001 — a refused SUSPECT surface lands here
            result["reason"] = f"surface refused: {exc}"
            return result
        body += "\n" + text

    for index, entry in enumerate(entries):
        snippet = str(entry.get("snippet", ""))
        surface = entry.get("surface")
        # A figure locator is an attestation about pixels; matching it as text would be
        # asking the wrong question and answering it wrongly.
        if surface == "figure" or snippet.strip().startswith("["):
            result["image"].append(index)
            continue
        found, _mode = dm._quote_matches(snippet, body)
        (result["matched"] if found else result["missing"]).append(index)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--corpus", default="")
    parser.add_argument("--pmid", default="")
    parser.add_argument("--strict", action="store_true",
                        help="exit non-zero when a quote is not found in its artifact")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    corpus = Path(args.corpus) if args.corpus else root / "files" / "fulltext"

    audited = unauditable = missing_total = 0
    for path in manifests(root, args.disease):
        if args.pmid and args.pmid not in path.stem:
            continue
        result = audit_one(path, corpus)
        if result["reason"]:
            unauditable += 1
            print(f"  {result['pmid']:>10}  schema={result['schema']}  "
                  f"— {result['reason']}")
            continue
        audited += 1
        missing_total += len(result["missing"])
        verdict = "OK" if not result["missing"] else f"{len(result['missing'])} NOT FOUND"
        print(f"  {result['pmid']:>10}  schema={result['schema']}  "
              f"{len(result['matched'])}/{len(result['matched']) + len(result['missing'])} text "
              f"matched, {len(result['image'])} image  [{verdict}]  {result['artifact']}")
        if result["missing"]:
            print(f"             entries {result['missing']} do not occur in the artifact. A "
                  f"quote that cannot be found was written from the page, not taken from the "
                  f"file — re-capture it, do not reword it")

    print(f"\n{audited} manifest(s) audited, {unauditable} unauditable, "
          f"{missing_total} quote(s) not found")
    if missing_total:
        print(CLOSED_SET_NOTE)
    if not audited:
        print("NOTHING AUDITED — a corpus that cannot be read is not a corpus with no defects")
        return 0
    if missing_total and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
