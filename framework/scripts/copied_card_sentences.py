#!/usr/bin/env python3
"""Does a current surface still hold a card sentence that this change replaced?

Cards (`cards/` and `cards_early/` of a drug-repurposing module) are copied into pages, derived JSON and hand-kept
tables. A card that gains a qualifier leaves the unqualified sentence in every copy that nobody rebuilt or edited
(2026-11-25: a ketogenic-diet sentence stood unqualified on the public page for 12 hours). This compares the cards
changed between two commits with the surfaces at the newer one.

    python3 framework/scripts/copied_card_sentences.py --base <rev> [--head <rev>] [--repo <dir>]

Reads git objects only; writes nothing. Exit 0: nothing found. Exit 1: findings, each with the file, the card and the
exact old text. Exit 3: the check could not be run.

A copy that is a marked cut of the current string (the shareable page's `pharm_cut`, an ellipsis) is current: the cut
is the builder's choice and no rebuild changes it.

What it sees: exact copies of a card string, or of a sentence of it, of at least 60 characters and 8 words. Not
paraphrases, not translations, not a clipped copy shorter than 200 characters that is not a whole sentence.

A refusal on a generated file is repaired by rebuilding in order: `repurposing_join.py run` (for `join/cards.json`;
first, because coverage reads `join/measure_next.json`), `repurposing_coverage.py run`, `ranking_it8.py run`,
`repurposing_view.py run` and its package. A page of a language other than the default one (`index.<lang>.html`) moves
only with `run --lang all` (and `--source shareable --lang all`). `investigations_it*.tsv` and `assertion_pertinence.tsv` are kept by hand
(`investigations.tsv` is built from the former): there the row is edited first.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
from pathlib import Path

MIN_CHARS, MIN_WORDS = 60, 8
MODULE = re.compile(r"^(disease-models/[^/]+/research/drug_repurposing)/")
CARD = re.compile(r"/drug_repurposing/(?:cards|cards_early)/[^/]+\.(?:card|packet)\.json$")
#: Relative to the module. Of `join/`, `cards.json` is the file that copies packet text (`repurposing_join.py run` rebuilds it, `check` says whether it is current).
SURFACES = re.compile(
    r"^(?:view/index[^/]*\.html|view/shareable_package/index\.html"
    r"|coverage/(?:priorities\.json|coverage_matrix\.json|assertion_pertinence\.tsv)|join/cards\.json"
    r"|ranking_it8_p9_[0-9]+/(?:ranking\.json|units\.tsv|unit_members\.tsv|selections\.tsv|member_evidence\.tsv"
    r"|investigations\.tsv|investigations_it[0-9]+\.tsv))$")
ADDED_MIN, ADDED_PREFIX = 20, 60
CLIP = 200      # some columns keep only the start of a card string (the ranking table clips): that start is looked for too
#: What a surface prints right after a string it cut on purpose: the page's cut flag (the shareable edition clips pharmacology and says so) or the ellipsis of ranking.json's clip.
CUT_MARK = re.compile(r'\s?\u2026|",\s?"pharm_cut":\s?true')
SENTENCE_END = re.compile(r"(?<=[.;])\s+(?=[A-Z\[(\"'])")


class CheckError(RuntimeError):
    pass


def git(repo: Path, *args: str) -> str:
    done = subprocess.run(["git", "-C", str(repo), "-c", "core.quotepath=off", *args], capture_output=True)
    if done.returncode != 0:
        raise CheckError(f"git {' '.join(args)}: {done.stderr.decode('utf-8', 'replace').strip()[:300]}")
    return done.stdout.decode("utf-8", "replace")


def squeeze(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def json_strings(value, into: list[str]) -> list[str]:
    if isinstance(value, str):
        into.append(value)
    elif isinstance(value, dict):
        for item in value.values():
            json_strings(item, into)
    elif isinstance(value, list):
        for item in value:
            json_strings(item, into)
    return into


def long_enough(text: str) -> bool:
    return len(text) >= MIN_CHARS and text.count(" ") >= MIN_WORDS - 1


def card_strings(repo: Path, rev: str, path: str) -> set[str]:
    try:
        value = json.loads(git(repo, "show", f"{rev}:{path}"))
    except json.JSONDecodeError as exc:
        raise CheckError(f"{path} at {rev} is not JSON: {exc}") from exc
    return {squeeze(s) for s in json_strings(value, [])}


def surface_text(path: str, raw: str) -> str:
    """One searchable text, with the escapes of the container removed so that equal sentences compare equal."""
    if path.endswith(".json"):
        try:
            return squeeze("\n\x00".join(json_strings(json.loads(raw), [])))
        except json.JSONDecodeError:
            pass
    if path.endswith(".html"):
        raw = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), raw)
        raw = raw.replace('\\"', '"').replace("\\/", "/").replace("\\n", " ").replace("\\t", " ")
        raw = html.unescape(raw)
    return squeeze(raw)


def has_the_addition(text: str, old: str, holder: str) -> bool:
    """True when `text` also holds what `holder` (a current card string) adds around `old`: a page that shows the new
    string in parts, or clipped after the addition began, is not behind."""
    added = [part.strip(" ,;()[]") for part in holder.split(old)]
    added = [part for part in added if len(part) >= ADDED_MIN]
    return bool(added) and all(part[:ADDED_PREFIX] in text for part in added)


def inside_a_marked_cut(text: str, old: str, holders: list[str]) -> int:
    """Occurrences of `old` inside a marked cut of a current card string: the surface prints the start of the NEW string and says it stopped.
    Rebuilding cannot add what the cut leaves out, so these are not behind (2026-11-25: four of the replayed refusals were only this)."""
    seen: set[int] = set()
    for holder in holders:
        at, start = holder.find(old), holder[:40]
        for mark in CUT_MARK.finditer(text):
            begin = text.rfind(start, 0, mark.start())
            if begin >= 0 and mark.start() - begin >= at + len(old) and holder.startswith(text[begin:mark.start()]):
                seen.add(begin + at)
    return len(seen)


def find(repo: Path, base: str, head: str = "HEAD") -> tuple[list[dict], dict]:
    """(findings, counts). A finding: card file, old text, surfaces still holding it."""
    changed = [line.split("\t") for line in git(repo, "diff", "--name-status", "--no-renames", base, head).splitlines()]
    changed = [(status, path) for status, path in (c for c in changed if len(c) == 2) if CARD.search(path)]
    counts = {"cards_changed": len(changed), "surfaces": 0, "old_texts": 0}
    if not changed:
        return [], counts
    modules = {MODULE.match(path).group(1) for _, path in changed if MODULE.match(path)}
    findings: list[dict] = []
    for module in sorted(modules):
        tree = git(repo, "ls-tree", "-r", "--name-only", head, "--", module).splitlines()
        current: set[str] = set()
        for path in tree:
            if CARD.search(path):
                current |= card_strings(repo, head, path)
        current_blob = "\n".join(current)
        candidates: list[tuple[str, str, list[str]]] = []      # (card file, old text, current strings that contain it)
        for status, path in changed:
            if status == "A" or not path.startswith(module + "/"):
                continue
            for old in card_strings(repo, base, path):
                if not long_enough(old) or old in current:
                    continue
                holders = [c for c in current if old in c]
                maximal = [h for h in holders if not any(h != other and h in other for other in holders)]
                candidates.append((path, old, maximal))
                parts = SENTENCE_END.split(old) + ([old[:CLIP]] if len(old) > CLIP else [])
                for part in parts:      # a copy may keep one sentence of the string, or its clipped start
                    if part != old and long_enough(part) and part not in current_blob:
                        candidates.append((path, part, []))
        counts["old_texts"] += len(candidates)
        if not candidates:
            continue
        surfaces = {path: surface_text(path, git(repo, "show", f"{head}:{path}"))
                    for path in tree if SURFACES.match(path[len(module) + 1:])}
        counts["surfaces"] += len(surfaces)
        for card, old, holders in sorted(candidates, key=lambda c: (c[0], -len(c[1]), c[1])):
            stale = [path for path, text in surfaces.items()
                     if old in text and text.count(old) > sum(text.count(h) * h.count(old) for h in holders) + inside_a_marked_cut(text, old, holders)
                     and not any(has_the_addition(text, old, h) for h in holders)]
            if not stale:
                continue
            if any(old in f["old"] and set(stale) <= set(f["files"]) for f in findings):
                continue      # a part of a longer finding on the same files, or the same text in the card's packet
            findings.append({"card": card, "old": old, "files": sorted(stale)})
    return findings, counts


def report(findings: list[dict]) -> str:
    out = []
    for number, finding in enumerate(findings, 1):
        out.append(f"[{number}] card {finding['card']}")
        out.append("    still held by: " + ", ".join(finding["files"]))
        out.append(f"    old text: {finding['old']}")
    out.append("hand-kept tables (investigations_it*.tsv, assertion_pertinence.tsv): edit the row. Everything else is built: rebuild in order "
               "(repurposing_join.py run for join/cards.json, then repurposing_coverage.py run, ranking_it8.py run, repurposing_view.py run and package; a language page index.<lang>.html needs run --lang all, "
               "also with --source shareable)")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--base", required=True, help="revision the change starts from (the remote tip at a landing)")
    parser.add_argument("--head", default="HEAD", help="revision whose cards and surfaces are judged (default HEAD)")
    parser.add_argument("--repo", default=".", help="repository root")
    args = parser.parse_args(argv)
    try:
        findings, counts = find(Path(args.repo), args.base, args.head)
    except Exception as exc:      # fail closed
        print(f"COPIED_CARD_SENTENCES_ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 3
    print(f"COPIED_CARD_SENTENCES: {counts['cards_changed']} card file(s) changed, {counts['old_texts']} replaced text(s), "
          f"{counts['surfaces']} surface(s) read, {len(findings)} still held")
    if findings:
        print(report(findings))
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
