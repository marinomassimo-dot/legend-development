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

## `--strength-scan` — the WORD, not the quote (advisory, exit 0, writes nothing)

    locator_audit.py --strength-scan [--pmid 32000863] [--loose]

Two checks already stand: the validator proves a quote EXISTS, and the numeral check proves
every NUMERAL of a proposition is in its quote. Neither sees a WORD. This mode lists, per
`verbatim_locators.entries` item, the quantifier, null-result, causal or exclusivity word the
PROPOSITION carries and the QUOTE does not (table `STRENGTH_WORDS`, each row with the audit
triples that justified it), plus two dropped-qualifier rows: a quote that hedges ("plays a role
in", "no SIGNIFICANT difference") under a proposition that does not. Measured against the
blind audits (R1, R3, R3 repairs, R3c, R4 cards, R4b/R2b: 58 quote-bearing adverse triples,
700 passed ones, in-sample): it flags about 31 percent of those adverse triples and about 4 percent
of the passed ones (`--loose`: 40 and 11 percent). It is a
PROMPT to re-read the quote, never a verdict; it cannot see scope, period, counting or
direction errors, and it does NOT decide whether a quote supports its proposition - that is a
judgement, and it needs a blind audit (`legend-locator-audit`). No baseline, no gate.

`--corpus` overrides where the artifacts live, because `files/` is gitignored and exists in
one checkout while sessions run in worktrees. Without a readable corpus this script reports
that it could not look, which is a different statement from finding nothing wrong.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
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


# --- strength scan -------------------------------------------------------------------------
# One row per word family: (label, kind, in-proposition regex, in-quote regex, excused-in-
# proposition regex, one-line why, origin). Text is lower-cased, punctuation collapsed to single
# spaces and padded with one space each side, so ` word ` matches whole words.
#   kind "absent":  flag when the proposition matches and the quote does NOT match the quote regex
#   kind "dropped": flag when the proposition matches, the quote matches, and the proposition
#                   does not already carry the quote's qualifier (the excused regex)
# Edit here and nowhere else. A row earns its place by an audit triple (manifest-index, audit
# file); a row with none was dropped on 2026-10-22 (first, replicated/confirmed, never/none,
# in vivo / in patients scope): 0 of 21 passed-triple hits were adverse, so they only cost trust.
_QW = (r"(?:significan\w*|substantial\w*|apparent\w*|statistically|grossly|overt\w*|obvious\w*|"
       r"clear\w*|marked\w*|appreciabl\w*|detectabl\w*|reliabl\w*)")
_HEDGE = (r" may | might | could | suggest\w* | potential\w* | possibl\w* | likely | appear\w* | "
          r"indicat\w* | role | associat\w* | correlat\w* | seem\w* | putative | propos\w* | "
          r"hypothes\w* | predict\w* ")
_NEGATIVE = (r" never | no | not | none | without | neither | nor | fail\w* | absent | lack\w* | "
             r"n t | ns | similar | comparable | unchanged | equal ")
STRENGTH_WORDS = (
    ("null", "absent", r" null | no difference | did not differ | no effect | no change | failed | underpowered | under powered ",
     _NEGATIVE, "", "null-result wording in the proposition, no negation in the quote",
     "36538782 #4 #9 #12 and 39625912 #8 'did not differ' for an interval covering the powered effect (R4b_R2b, R4_cards)"),
    ("dose-dependent", "absent", r" dose dependen\w* | dose response | dose proportional\w* ", r" dose ",
     "", "dose-dependence in the proposition, no 'dose' in the quote",
     "40665325 #21 (R3, R3 repairs)"),
    ("significant", "absent", r" significan\w* ", r" significan\w* | p | \d \d+ ",
     "", "'significant' in the proposition, no significance wording or statistic in the quote",
     "38731820 #3 (R1)"),
    ("prevents", "absent", r" prevent\w* | protect\w* | rescu\w* | abolish\w* | eliminat\w* ",
     r" prevent\w* | protect\w* | rescu\w* | abolish\w* | eliminat\w* | block\w* | attenuat\w* | restor\w* | revers\w* | ameliorat\w* ",
     "", "protective / rescue verb in the proposition, none in the quote",
     "35589394 #3 'prevented the injury' (R3c)"),
    ("mediates", "absent",
     r" mediat\w* | drives | driven | drove | driving | causes | caused | causal\w* | proves | proved | requires | required | necessary | sufficient | responsible ",
     r" mediat\w* | driv\w* | drove | caus\w* | prov\w* | requir\w* | necessar\w* | sufficien\w* | responsible | dependen\w* ",
     "", "causal / strength verb in the proposition, not in the quote",
     "35589394 #8 'mediates' (R3c)"),
    ("hedge-dropped", "dropped",
     r" mediates | drives | causes | proves | prevents | demonstrates | establishes | confirms | rescues | protects ",
     _HEDGE, _HEDGE, "strong verb in the proposition while the quote hedges ('plays a role in', 'suggests')",
     "35589394 #8 'plays a significant role in mediating' -> 'mediates' (R3c)"),
    ("qualifier-dropped", "dropped",
     r" did not \w+ | do not \w+ | does not \w+ | no \w+ | unchanged | not \w+ | never ",
     r" (?:no|not|non|nor|without|neither) (?:\w+ ){0,2}?" + _QW + " ", _QW,
     "quote says 'no SIGNIFICANT / substantial ...', proposition says plain 'no / did not'",
     "42334048 #7, 41980417 #7 #8, 38147624 #6, 38378758 #7, 36538782 #4 (R1, R3, R4b_R2b)"),
)


# The quantifier rows the brief names. Measured on the blind audits (700 passed triples, 58 quote-
# bearing adverse ones) they added 5 hits for 37 more passed triples flagged - about the base rate
# of adverse triples, so no information - and were taken out of the default list. `--loose` puts
# them back for a manifest whose propositions are heavy on "every / all / only".
LOOSE_WORDS = (
    ("every", "absent", r" every | always | all | entire ",
     r" every | all | each | always | any | both | entire | whole | throughout | across ",
     "", "universal quantifier in the proposition, none in the quote",
     "41250984 #12 'every class' and 42286026 #7 'all four' (R4b_R2b); 38378758 #13 (R1)"),
    ("only", "absent", r" only | solely | exclusively | sole ",
     r" only | sole | solely | exclusively | alone | unique\w* | restricted | limited | specific\w* | just ",
     "", "exclusivity in the proposition, none in the quote",
     "31402619 #3, 38731820 #3, 38378758 #15 (R1); 29940337 #0, 42310739 #10 (R3 repairs); 42389070 #5 (R4b_R2b)"),
)


def _words(text: str) -> str:
    return " " + re.sub(r"[^a-z0-9]+", " ", str(text).lower().replace("\u2019", "'")) + " "


def strength_flags(entry: dict, loose: bool = False) -> list[tuple[str, str, str]]:
    """(label, word in the proposition, why) for each strength word the quote lacks; [] if none."""
    proposition, quote = _words(entry.get("proposition", "")), _words(entry.get("snippet", ""))
    flags = []
    for label, kind, prop_rx, quote_rx, excused_rx, why, _origin in (
            STRENGTH_WORDS + LOOSE_WORDS if loose else STRENGTH_WORDS):
        found = re.search(prop_rx, proposition)
        if not found:
            continue
        if kind == "absent":
            hit = not re.search(quote_rx, quote)
        else:
            hit = bool(re.search(quote_rx, quote)) and not re.search(excused_rx, proposition)
        if hit:
            flags.append((label, found.group(0).strip(), why))
    return flags


def strength_scan(root: Path, disease: str, pmid: str = "", loose: bool = False) -> int:
    """Advisory: print the strength words each proposition carries that its quote does not."""
    scanned = flagged = unquoted = attested = 0
    for path in manifests(root, disease):
        if pmid and pmid not in path.stem:
            continue
        try:
            entries = json.loads(path.read_text(encoding="utf-8"))["verbatim_locators"]["entries"]
        except (OSError, ValueError, KeyError, TypeError):
            continue
        if not isinstance(entries, list):
            continue
        for index, entry in enumerate(entries):
            if not isinstance(entry, dict):
                continue
            quote = str(entry.get("snippet") or "").strip()
            if not quote:
                unquoted += 1
                print(f"  {path.stem.removeprefix('PMID'):>10}  #{index:<3} (no quote - nothing to compare)")
                continue
            if quote.startswith("[figure attestation"):
                attested += 1  # a description of pixels, not a sentence of the source
                continue
            scanned += 1
            flags = strength_flags(entry, loose)
            flagged += bool(flags)
            for label, word, why in flags:
                print(f"  {path.stem.removeprefix('PMID'):>10}  #{index:<3} {label:<17} \"{word}\" - {why}")
    print(f"\nstrength scan (ADVISORY, exit 0): {scanned} quoted entries read, {flagged} with a "
          f"word the quote lacks; {attested} figure attestations and {unquoted} entries without a "
          f"quote not read.\nA flag is a prompt to re-read the quote against the proposition, not a "
          f"finding; whether a quote SUPPORTS its proposition is judgement and needs a blind audit.")
    return 0


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
        # asking the wrong question and answering it wrongly. `rendered_text` is the same
        # act on a page of running text whose text layer was refused (P10, 2026-09-14).
        if surface in dm.PIXEL_ATTESTED_SURFACES or snippet.strip().startswith("["):
            result["image"].append(index)
            continue
        found, _mode = dm._quote_matches(snippet, body)
        (result["matched"] if found else result["missing"]).append(index)
    return result


def primary_checkout_corpus(root: Path) -> Path | None:
    """The corpus of the checkout that owns this repository, when `root` is a linked worktree.

    `files/` is gitignored, so it exists in the one checkout that fetched the artifacts and in
    no worktree. `git rev-parse --git-common-dir` names the `.git` every worktree shares; its
    parent is that checkout. Returns None when it cannot be derived, when `root` IS that
    checkout, or when the checkout holds no corpus — a hint must never name a place that is
    not there.
    """
    result = subprocess.run(["git", "-C", str(root), "rev-parse", "--path-format=absolute",
                             "--git-common-dir"], capture_output=True, text=True)
    if result.returncode != 0 or not result.stdout.strip():
        return None
    primary = Path(result.stdout.strip()).parent
    if primary.resolve() == root.resolve():
        return None
    candidate = primary / "files" / "fulltext"
    return candidate if candidate.is_dir() else None


def corpus_hint(root: Path, corpus: Path, absent_here: int) -> str:
    """One line for a run that could not see its surfaces — the errand, not the defect.

    HANDOFF-2 of CC-20260826-PMID36828035-DURABILITY-01: in a worktree the absence of `files/`
    is the NORMAL state, and a run that only said `unauditable` cost every reader one failed
    run per worktree before they found `--corpus`. Empty when there is nothing to hint.
    """
    if not absent_here and corpus.is_dir():
        return ""
    what = (f"{absent_here} manifest(s) declare surfaces absent from this tree"
            if absent_here else f"no corpus at {corpus}")
    primary = primary_checkout_corpus(root)
    target = str(primary) if primary else "<checkout that holds files/>/files/fulltext"
    return (f"HINT: {what} — files/ is gitignored and exists only in the checkout that "
            f"fetched it; re-run with --corpus {target}")


def print_triples(root: Path, disease: str, pmid: str, count: int, seed: str) -> int:
    """The blind input of a locator audit, sampled, carrying nothing but the triples.

    N7 (metabolic batch 2026-10-19): blind audits run voluntarily caught propositions that
    overshot their quotes after every gate had passed (23 of 101 in one wave, none caught by
    the reader's own re-read). Assembling the packet by hand was the cost that kept the audit
    voluntary. Only proposition, quote, anchor, surface and artifact leave the manifest: no
    receipt, reader, dossier, landing or assessment field, so the auditor stays blind.
    """
    import random
    path = root / "disease-models" / disease / "research" / "deepdive_manifests" / f"PMID{pmid}.json"
    try:
        entries = json.loads(path.read_text(encoding="utf-8"))["verbatim_locators"]["entries"]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"locator_audit: no locator entries for PMID {pmid}: {exc}", file=sys.stderr)
        return 2
    indexed = list(enumerate(entries))
    if count and count < len(indexed):
        indexed = sorted(random.Random(seed).sample(indexed, count))
    packet = [{"entry": i, "proposition": e.get("proposition", ""),
               "quote": e.get("snippet", ""), "anchor": e.get("anchor", ""),
               "surface": e.get("surface", ""), "artifact": e.get("artifact", "")}
              for i, e in indexed]
    print(json.dumps({"pmid": pmid, "sampled": len(packet), "of": len(entries),
                      "seed": seed, "triples": packet}, indent=1, ensure_ascii=False))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--corpus", default="")
    parser.add_argument("--pmid", default="")
    parser.add_argument("--strict", action="store_true",
                        help="exit non-zero when a quote is not found in its artifact")
    parser.add_argument("--triples", type=int, default=None, metavar="N",
                        help=("with --pmid: print a BLIND audit packet instead - N sampled "
                              "(proposition, quote, anchor) triples as JSON, 0 for all, and "
                              "nothing else from the manifest (legend-locator-audit input)"))
    parser.add_argument("--strength-scan", action="store_true",
                        help=("advisory: per entry, the strength / negation / result / scope words "
                              "the proposition carries and the quote lacks (honours --pmid; exit 0)"))
    parser.add_argument("--loose", action="store_true",
                        help="with --strength-scan: also the noisy every / all / only rows")
    parser.add_argument("--seed", default="", help="--triples sample seed (default: the PMID)")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if args.strength_scan:
        return strength_scan(root, args.disease, args.pmid, args.loose)
    if args.triples is not None:
        if not args.pmid:
            parser.error("--triples needs --pmid")
        return print_triples(root, args.disease, args.pmid, args.triples, args.seed or args.pmid)
    corpus = Path(args.corpus) if args.corpus else root / "files" / "fulltext"

    audited = unauditable = missing_total = absent_here = 0
    for path in manifests(root, args.disease):
        if args.pmid and args.pmid not in path.stem:
            continue
        result = audit_one(path, corpus)
        if result["reason"]:
            unauditable += 1
            absent_here += result.get("cause") == "surface_absent_here"
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
    hint = corpus_hint(root, corpus, absent_here)
    if hint:
        print(hint)
    if not audited:
        print("NOTHING AUDITED — a corpus that cannot be read is not a corpus with no defects")
        return 0
    if missing_total and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
