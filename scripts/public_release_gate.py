#!/usr/bin/env python3
"""Fail-closed public-release gate for the public LEGEND repository.

The gate is deliberately standard-library only. It checks:
privacy and case linkage, common secrets, provenance coverage, local links,
README/repository consistency, and execution from a clean Git archive.

Exit codes:
  0 = PASS
  2 = BLOCK_PUBLICATION
  3 = gate/internal error
"""

from __future__ import annotations

import argparse
import fnmatch
import functools
import hashlib
import inspect
import importlib.util
import json
import os
import re
import subprocess
import sys
import tarfile
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


TEXT_SUFFIXES = {
    # `.jsonl` sits beside `.json` deliberately: it was absent while `.json` was present,
    # so every line-oriented ledger in the tree — read receipts, approval queue, corpus
    # seed — was outside the gate's reach and could not have raised a finding of any kind.
    ".md", ".txt", ".json", ".jsonl", ".csv", ".tsv", ".yaml", ".yml", ".toml",
    ".py", ".sh", ".rst",
}
# Text-like suffixes the PRIVACY scan also opens (IT9, closing the blind spot measured in IT8:
# 24 tracked files and 184 history-only files were never read). They are NOT added to
# TEXT_SUFFIXES: the link, wikilink and corpus checks keep their old perimeter, and only
# `scan_privacy_and_secrets` reads these. Compressed files (.gz) stay outside on purpose:
# reading them needs decompression limits and carve-outs for substance codes and for a
# public registry's investigator names that are not a small, safe change (see the IT9 P7 record).
PRIVACY_EXTRA_SUFFIXES = {".html", ".js", ".css", ".patch", ".diff", ".cff", ".example"}
# Pages and bundles of these kinds embed data as one line of megabytes; a block-scoped rule over
# such a line degenerates to file scope. They are therefore evaluated in overlapping windows.
EXTRA_WINDOW = 1400
# `backup/` is the BATCH_COMMIT Phase-3 snapshot root: gitignored, never part of a release
# copy, and a byte-identical duplicate of the canonical files. Scanning it made the mandatory
# pre-commit backup itself raise BROKEN_MARKDOWN_LINK on the copies' relative links.
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", "backup"}
PLACEHOLDER_TOKENS = {
    "your-email@example.com", "example@example.com", "changeme",
    "replace_me", "placeholder",
    # The project's own git identity: quoted verbatim by review records that cite commit
    # metadata, and publishable by construction (it is the author of every commit).
    "legend-project@users.noreply.github.com",
}
MARKDOWN_LINK_EXAMPLES = {"url", "path", "relative/path.md"}
WIKILINK_EXAMPLES = {
    "file", "file_current", "future_concept_current",
    "nuovo_concetto_da_creare", "DEEP_DIVE",
    # POSIX bracket expressions quoted inside code spans ("[[:space:]]") are not wikilinks.
    ":space:", ":alpha:", ":alnum:", ":digit:", ":upper:", ":lower:", ":punct:",
}
GATE_INTERNAL_FILES = {
    "scripts/public_release_gate.py",
    "scripts/test_public_release_gate.py",
}


@dataclass(order=True)
class Finding:
    severity: str
    code: str
    path: str
    line: int
    message: str


def unpublishable_paths(root: Path) -> frozenset[str]:
    """Paths that are simultaneously untracked *and* gitignored.

    Such a file cannot reach a published clone: it is not in the index, and
    `.gitignore` prevents it from being added by accident. Scanning it produces
    findings about material that is, by construction, private — which is how the
    working-tree scan ended up reporting BLOCKs for the funding dossiers under
    `grants/` and for local scratch directories.

    The condition is deliberately a conjunction, not a directory allowlist. A
    file that is gitignored but has been force-added (`git add -f`) *is* tracked,
    is therefore publishable, and must still be scanned — an allowlist keyed on
    directory names would silently exempt exactly the case that matters. Outside
    a git checkout (an exported release copy) nothing is exempt.
    """
    try:
        completed = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z",
             "--others", "--ignored", "--exclude-standard"],
            check=True, capture_output=True, text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return frozenset()
    return frozenset(entry for entry in completed.stdout.split("\0") if entry)


def is_exempt(relative: str, exempt: frozenset[str]) -> bool:
    """Exact match, or *under* a directory entry that git collapsed.

    🔴 `git ls-files --others --ignored` does not descend into a nested checkout: it
    returns the directory as one entry with a trailing slash. Matching those entries by
    exact string therefore exempts the directory and nothing inside it, so every file of a
    nested checkout is scanned as if it were publishable material of this repository.

    Measured when per-session worktrees were introduced under `.claude/worktrees/`: the
    gate scanned 340 files of a nested checkout and reported 37 BLOCKs, of which every one
    was false — 22 from `test_public_release_gate.py`, whose negative fixtures are
    privacy-violating strings *on purpose*, and 12 from the gate scanning its own source.
    A publication gate that cries wolf 37 times is worse than no gate: the day a real
    marker appears it will be item 38 of a list nobody reads.
    """
    if relative in exempt:
        return True
    return any(entry.endswith("/") and relative.startswith(entry) for entry in exempt)


def tracked_paths(root: Path) -> frozenset[str] | None:
    """Every path this repository tracks, relative to `root` — or `None` if git cannot say.

    🔴 The first draft returned an empty frozenset on every failure, which reads as "this
    repository tracks nothing" and is indistinguishable from it. Every predicate below then
    concludes that no directory holds tracked content, which is the *pruning* answer — so a
    tool that could not run git pruned more, silently, in the direction that loses files.

    🔴 The second draft returned `None` on every failure, and that was the same mistake with
    the sign flipped. Two failures were being merged again, and this time the merge broke two
    controls that were already green:

        test_the_ignore_audit_does_not_walk_into_another_checkout   FAIL
        test_markdown_of_a_nested_checkout_is_not_collected         FAIL

    Both fixtures mount a real nested checkout inside a temp directory that is deliberately
    NOT a repository. There, "the outer index claims nothing inside this subdirectory" is not
    an unanswered question — it is simply true, because there is no outer index at all, and a
    subtree with its own `.git` is unambiguously a different repository's disk. Pruning is
    correct, and refusing to prune made the walker collect another repository's files.

    So the two cases are separated rather than compressed onto one sentinel:

        not inside a work tree      frozenset()   nothing outer is claimed, so nested
                                                  checkouts prune — an archive extraction,
                                                  a plain directory, a test fixture
        inside one, index unread    None          the question was asked and not answered;
                                                  callers must not prune on it

    Absence of an index is not the same as absence of an answer, and only the second one is
    a reason to distrust the result.
    """
    inside = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "--is-inside-work-tree"],
        check=False, capture_output=True, text=True,
    )
    if inside.returncode != 0 or inside.stdout.strip() != "true":
        return frozenset()
    try:
        completed = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z"],
            check=True, capture_output=True, text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return frozenset(entry for entry in completed.stdout.split("\0") if entry)


def tracked_documents(root: Path, suffix: str = ".md") -> list[Path]:
    """The DOCUMENTATION population: what a reader of a clone actually holds.

    🔴 This is deliberately NOT `walk_publishable`, and the difference is the whole point.

    The two questions are not the same question:

      PUBLISHABLE   — "what could leak from here?"  Asked of the DISK, and answered
                      over-inclusively on purpose: an untracked file one commit away from
                      shipping must be scanned, because the cost of a miss is a published
                      privacy breach.
      DOCUMENTATION — "what does a reader hold?"  Asked of the INDEX. A promise is made to
                      whoever receives the repository, and what they receive is what git
                      tracks.

    On a clean checkout the two sets are identical — measured at `788c357d`, 281 markdown
    files each, set-equal — which is exactly why one helper looked adequate for both. They
    separate only under local filesystem state, and that is the state the guards must be
    immune to:

        untracked, not ignored `NOTES.md`   publishable 282 · tracked 281
                                            -> the documentation guard turns RED for a file
                                               in no commit and no clone
        tracked document deleted on disk    publishable 280 · tracked 281
                                            -> a tracked governance document leaves the
                                               population because somebody ran `rm`

    Both are answered by asking the index instead of the disk. Nothing a local working tree
    does — a stray marker, a deletion, a scratch file, a rename — can move this population.

    Nested checkouts need no pruning here: their files are not in this repository's index.
    A submodule appears as its own gitlink path and carries no `.md` suffix, so it drops out
    of the filter rather than contributing its contents.

    🔴 An empty answer is refused, not returned. `tracked_paths` says `frozenset()` for "not
    a repository", which is the right answer for a pruning predicate and a catastrophic one
    here: a documentation guard handed an empty population checks nothing and exits 0. That
    is the vacuous pass `test_release_surface` already names in
    `test_an_empty_index_is_a_refusal_not_a_pass`, arriving through a different door.
    """
    tracked = tracked_paths(root)
    if not tracked:
        raise RuntimeError(
            f"tracked_documents({root}): the index is empty or unreadable. The documentation "
            "population is defined by the index, an empty population is a guard that checks "
            "nothing, and there is no disk-based substitute that is not the defect this "
            "function exists to avoid."
        )
    return sorted(
        root / entry for entry in tracked
        if entry.endswith(suffix) and (root / entry).is_file()
    )


def is_nested_checkout(path: Path, root: Path, tracked: frozenset[str] | None) -> bool:
    """A directory that is a checkout of a DIFFERENT repository than `root`.

    🔴 The predecessor was `(path / ".git").exists()` and nothing else, which is a filesystem
    NAME, not repository metadata. Any untracked one-line file called `.git` — a stray editor
    artefact, a half-finished `git init`, a copied directory, anything — made this return True
    and pruned the whole subtree.

    Measured on a clean checkout of `main`, dropping a bare `.git` file into `governance/`:

        281 publishable markdown  ->  246
        35 TRACKED documents removed, including GOVERNANCE_v3.1.1.md and every annex

    and, with a broken markdown link planted in one of them first:

        without the marker   VERDICT: BLOCK_PUBLICATION   BLOCKS: 1
        with the marker      VERDICT: PASS                BLOCKS: 0

    **A one-line untracked file turned a publication BLOCK into a PASS.** The gate did not
    fail to detect the violation; it removed the file holding it from its own population, and
    then reported that it had found nothing.

    The repair asks the OUTER repository instead of the filesystem: a directory is a nested
    checkout only if it looks like one **and this repository tracks nothing inside it.** A real
    nested worktree holds zero tracked paths of ours, so it still prunes — whether or not an
    ignore rule reaches it; a tracked tree with a stray marker holds tracked paths, so it does
    not. Content of the index decides, not a name on the disk.

    🔴 `root` and `tracked` are REQUIRED. The first repair made them optional and fell back to
    the old name-only answer, so `walk_publishable` was fixed and the two other call sites —
    `test_link_targets.markdown_files` and `test_release_surface.walk_this_checkout` — kept
    the defect, because "existing callers keep working" meant "existing callers keep the
    bypass". Measured on that repair, at the level of the test that owns each guard:

        test_release_surface  ReleaseSurfaceTests.test_no_public_file_is_silently_gitignored
            without marker  FAILED (failures=1)      with marker  OK
        test_link_targets     LinkTargetTests.test_markdown_fragments_resolve_to_headings
            without marker  FAILED (failures=1)      with marker  OK

    A caller that cannot name the repository it means has not decided what it is asking, and a
    `TypeError` says so where a wrong boolean would not.

    `tracked is None` means git could not be asked. That is not a licence to prune: pruning on
    an unanswered question is how the original defect lost 35 documents. Uncertainty resolves
    towards scanning more, which is noisy and visible, and never towards scanning less.
    """
    if not (path / ".git").exists():
        return False
    if tracked is None:
        return False
    prefix = path.relative_to(root).as_posix() + "/"
    return not any(entry.startswith(prefix) for entry in tracked)


def walk_publishable(root: Path) -> Iterable[Path]:
    """Every file and directory that could reach a published clone of *this* repository.

    Pruning happens at the directory level rather than per path, so a nested checkout costs
    nothing to skip and cannot leak through a walker that forgot to filter. All three
    walkers in this module route through here: the defect above existed because they did
    not.
    """
    exempt = unpublishable_paths(root)
    tracked = tracked_paths(root)
    for dirpath, dirnames, filenames in os.walk(root):
        here = Path(dirpath)
        dirnames[:] = sorted(
            name for name in dirnames
            if name not in SKIP_DIRS
            and not is_nested_checkout(here / name, root, tracked)
            and not is_exempt((here / name).relative_to(root).as_posix() + "/", exempt)
        )
        if here != root:
            yield here
        for name in sorted(filenames):
            path = here / name
            relative = path.relative_to(root)
            if any(part in SKIP_DIRS for part in relative.parts):
                continue
            if is_exempt(relative.as_posix(), exempt):
                continue
            yield path


# 🔴 PER-FILE PRE-CHECK (ADV-041, 2026-11-18). When set (by `--paths` or `--changed-since`), the two
# content scans that read one file at a time (privacy and case linkage, local links) read ONLY these
# repository-relative paths. It is a way to learn in seconds, before the serialized queue, what the
# gate would say about the files of one commit. It is NOT the gate: the tree-level scans, the
# provenance and README checks and the clean clone are not run, and a clean pre-check says nothing
# about a file that was not named. `None` is the full gate and the default.
ONLY_PATHS: frozenset[str] | None = None

# Opt-in per-file cache of the privacy scan (ADV-057). `None` is today's behaviour and the default: the privacy scan walks every file.
# Set only by `scan_privacy_cached`, for the duration of one call, to the files whose result the cache could not give.
PRIVACY_FILES: Iterable[Path] | None = None
PRIVACY_TEXT: dict[Path, str] = {}      # opt-in cache only: the text of the ONE file being scanned, decoded from the very bytes that were hashed


def in_scope(root: Path, path: Path) -> bool:
    if ONLY_PATHS is None:
        return True
    try:
        return path.relative_to(root).as_posix() in ONLY_PATHS
    except ValueError:
        return False


def iter_files(root: Path) -> Iterable[Path]:
    for path in walk_publishable(root):
        if path.is_file():
            yield path


def scoped_files(root: Path) -> Iterable[Path]:
    """The named files of a pre-check, with the same exemptions the full walk applies; no tree walk."""
    exempt = unpublishable_paths(root)
    for rel in sorted(ONLY_PATHS or ()):
        path = root / rel
        if (not path.is_file() or any(part in SKIP_DIRS for part in Path(rel).parts)
                or is_exempt(rel, exempt)):
            continue
        yield path


def iter_text_files(root: Path) -> Iterable[Path]:
    for path in (iter_files(root) if ONLY_PATHS is None else scoped_files(root)):
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in {
            "LICENSE", ".gitignore",
        }:
            yield path


def iter_privacy_files(root: Path) -> Iterable[Path]:
    """Every file the privacy scan reads: the text suffixes plus PRIVACY_EXTRA_SUFFIXES."""
    if PRIVACY_FILES is not None:        # opt-in cache only: the cache wrapper hands over the files it could not answer
        yield from PRIVACY_FILES
        return
    for path in (iter_files(root) if ONLY_PATHS is None else scoped_files(root)):
        if (
            path.suffix.lower() in TEXT_SUFFIXES
            or path.suffix.lower() in PRIVACY_EXTRA_SUFFIXES
            or path.name in {"LICENSE", ".gitignore"}
        ):
            yield path


def read_text(path: Path) -> str:
    if PRIVACY_TEXT and path in PRIVACY_TEXT:     # cache pass only (empty, hence skipped, in every other run)
        return PRIVACY_TEXT[path]
    return path.read_text(encoding="utf-8", errors="replace")


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def add_matches(
    findings: list[Finding],
    root: Path,
    path: Path,
    text: str,
    code: str,
    pattern: re.Pattern[str],
    message: str,
) -> None:
    for match in pattern.finditer(text):
        findings.append(
            Finding(
                "BLOCK",
                code,
                str(path.relative_to(root)),
                line_number(text, match.start()),
                message,
            )
        )


def semantic_blocks(text: str) -> Iterable[tuple[int, str]]:
    """Yield paragraph/list-record sized blocks with their source offsets."""
    start = 0
    for match in re.finditer(r"\n[ \t]*\n", text):
        block = text[start:match.start()]
        if block.strip():
            yield start, block
        start = match.end()
    block = text[start:]
    if block.strip():
        yield start, block


STUDY_IDENTIFIER = re.compile(
    r"(?i)\bPMID[\s:_-]*\d{6,9}\b|\bPMC\d{5,9}\b|\b10\.\d{4,9}/\S{3,}"
)

# One definition of "this text names a maternal side", and one of the paternal side.
#
# 🔴 There used to be three hand-written copies of this vocabulary and they had drifted
# apart, which is a sharper defect than the missing word that exposed it. The detector
# required a possessive in English (`mother'?s`) while accepting the bare noun in Italian
# (`madre`); the negation recogniser — the clause that SUPPRESSES these rules — listed the
# bare English nouns. So the escape hatch recognised more parental language than the net it
# was allowed to open. Nobody chose that; two lists were written at different times from the
# same idea. `PATTERN_ALREADY_SOLVED_GATE`: the failure mode of this repository is uneven
# application, so the fix is one definition every rule composes from, not a fourth list.
#
# Measured before widening, over exactly the surface the gate walks: 20 bare-noun occurrences
# in 3 files. 8 are this file's own patterns (exempt via GATE_INTERNAL_FILES), 11 are in
# `PMID39416860.json`, a manifest the narrow net already flags, and 1 is the heading "The
# mother rule" in a skill — a metaphor, and unpairable because no paternal word follows it.
# So the widening changes no verdict today, which is the only safe moment to install it: the
# corpus is 15 complete reads on its way to hundreds of thousands, and trio papers are the
# normal case in this field, not the exception.
MATERNAL_WORDS = r"maternal(?:ly)?|mothers?(?:'s?)?|materno|materna|madre"
PATERNAL_WORDS = r"paternal(?:ly)?|fathers?(?:'s?)?|paterno|paterna|padre"
PARENT_OF_ORIGIN_WORDS = r"parent[- ]of[- ]origin"
MATERNAL_ORIGIN = re.compile(rf"(?i)\b(?:{MATERNAL_WORDS})\b")
PATERNAL_ORIGIN = re.compile(rf"(?i)\b(?:{PATERNAL_WORDS})\b")
PARENT_ORIGIN = re.compile(
    rf"(?i)\b(?:{MATERNAL_WORDS}|{PATERNAL_WORDS}|{PARENT_OF_ORIGIN_WORDS})\b"
)


def record_blocks(text: str, rel: str) -> Iterable[tuple[int, str]]:
    """The unit a block-scoped rule is evaluated over.

    🔴 A `.jsonl` file has no blank lines, so `semantic_blocks` yielded it whole and every
    block-scoped rule degenerated to file scope — over 706 unrelated published papers in the
    corpus seed, over 400 unrelated propositions in the Pathograph export. Measured before
    this helper existed: a maternal word in one record and a paternal word in another, 630
    records apart, were reported as one pairing, and the reference-genotype safeguard was
    evaluated over the whole file, so the pairing became a BLOCK on a line that contains no
    variant at all. For a line-oriented ledger the record IS the line, and a rule that
    describes "one record" must be evaluated over exactly that unit (Mirror, 2026-08-26).
    """
    if rel.endswith(".jsonl"):
        offset = 0
        for raw in text.splitlines(keepends=True):
            line = raw.rstrip("\r\n")
            if line.strip():
                yield offset, line
            offset += len(raw)
        return
    if Path(rel).suffix.lower() in PRIVACY_EXTRA_SUFFIXES:
        for offset, block in semantic_blocks(text):
            if len(block) <= EXTRA_WINDOW:
                yield offset, block
                continue
            step = EXTRA_WINDOW // 2
            for start in range(0, len(block), step):
                yield offset + start, block[start:start + EXTRA_WINDOW]
                if start + EXTRA_WINDOW >= len(block):
                    break
        return
    yield from semantic_blocks(text)


def attribution_window(text: str, block_offset: int, block: str, rel: str) -> str:
    """The text a block's parental claim may be attributed to.

    🔴 A JSON file has no blank lines, so `semantic_blocks` yields it whole and every
    block-scoped rule silently becomes file-scoped. Measured: `PMID39416860.json` is ONE block
    of 19 680 characters, so "maternal and paternal in the same block" degenerates to "both
    words appear somewhere in this manifest" — guaranteed for any manifest about a trio paper.
    That is not the rule anyone wrote. For a per-paper record the file IS the record, and its
    `pmid` field is the attribution, so the window is the file and the scoping question is
    answered honestly rather than by accident.

    For prose the window reaches back to the enclosing `##` heading, because a queue entry
    names its paper in the heading block and argues about it three paragraphs later. Without
    that reach, attribution would depend on how the author happened to break paragraphs.
    """
    if rel.endswith(".json"):
        return text
    if rel.endswith(".jsonl"):
        # One record per line: the record is its own attribution window, and nothing
        # outside it — a heading search would reach back to offset 0, i.e. the whole file.
        return block
    start = text.rfind("\n## ", 0, block_offset)
    return text[start if start >= 0 else 0: block_offset + len(block)]


def parent_origin_is_explicitly_negated(window: str) -> bool:
    """Allow policy statements that explicitly remove/decouple this linkage."""
    # Composed from the same vocabulary the detector uses, so this clause can never again
    # recognise parental language that the rules it suppresses do not.
    subject = rf"(?:{PARENT_OF_ORIGIN_WORDS}|{MATERNAL_WORDS}|{PATERNAL_WORDS})"
    before = (
        r"(?:no|without|removed|redacted|decoupled|de[- ]identified|"
        r"neutralized|excluded)"
    )
    after = (
        r"(?:has been|have been|was|were|is|are)?\s*"
        r"(?:removed|redacted|decoupled|de[- ]identified|neutralized|"
        r"excluded|not (?:retained|linked|reported|included))"
    )
    return bool(
        re.search(rf"(?i)\b{before}\b.{{0,45}}\b{subject}\b", window)
        or re.search(rf"(?i)\b{subject}\b.{{0,45}}\b{after}\b", window)
    )


def person_context_is_explicitly_negated(window: str) -> bool:
    subject = (
        r"(?:person|proband|patient|individual|case|participant|"
        r"clinical regimen|parent[- ]of[- ]origin|institution)"
    )
    negation = (
        r"(?:no|not|without|removed|redacted|decoupled|de[- ]identified|"
        r"never|excluded)"
    )
    return bool(
        re.search(rf"(?i){negation}.{{0,100}}{subject}", window)
        or re.search(rf"(?i){subject}.{{0,100}}{negation}", window)
    )


# ---------------------------------------------------------------------------------------------
# Opt-in per-file result cache for the privacy scan (ADV-057). OFF by default; nothing below runs, and
# nothing is written, unless `--cache`, `--cache-verify` or LEGEND_GATE_CACHE=1 is given (`--no-cache` wins).
#
# What it relies on, and tests: the privacy scan is a function of one file's text and its repository-relative
# path and of nothing else (every finding it emits carries that path; the per-file loop reads no other
# file). It is NOT used for the link, README-consistency or provenance scans, which are cross-file and
# always run in full. The cache answers a file only when the key matches exactly:
#   key = sha256(digest of THIS script's bytes, relative path, digest of the file's bytes)
# so editing the script (any detector pattern or digest list, any constant) changes every key, and
# editing a file changes its key. The cache file carries a seal over its content: a missing, unreadable,
# malformed, wrongly-sealed or other-format cache is no cache, and the scan runs in full.
# The cache lives next to the git landing lock (`<git common dir>/legend_gate_cache/`), is rewritten
# atomically and holds only the files of the current run.
CACHE_FORMAT = 1
CACHE_ENV = "LEGEND_GATE_CACHE"
CACHE_FILE_ENV = "LEGEND_GATE_CACHE_FILE"


def gate_digest() -> str:
    """The script's own bytes (every pattern, digest list and constant) and the interpreter's version (its `re` and Unicode tables decide what a pattern matches)."""
    return hashlib.sha256(Path(__file__).read_bytes() + b"\0" + sys.version.encode("utf-8")).hexdigest()


def cache_file(root: Path) -> Path | None:
    override = os.environ.get(CACHE_FILE_ENV)
    if override:
        return Path(override)
    try:
        out = subprocess.run(["git", "-C", str(root), "rev-parse", "--git-common-dir"],
                             check=True, capture_output=True, text=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None
    common = Path(out)
    common = common if common.is_absolute() else root / common
    return common / "legend_gate_cache" / f"privacy_v{CACHE_FORMAT}.json"


def cache_seal(gate: str, entries: dict) -> str:
    body = json.dumps({"format": CACHE_FORMAT, "gate_sha256": gate, "entries": entries},
                      sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(body.encode("ascii")).hexdigest()


def cache_load(path: Path | None, gate: str) -> dict | None:
    """The stored entries, or None when there is nothing trustworthy (absent, unreadable, malformed, other gate, bad seal)."""
    if path is None:
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        entries = data["entries"]
        if (data["format"] != CACHE_FORMAT or data["gate_sha256"] != gate or not isinstance(entries, dict)
                or data["seal"] != cache_seal(gate, entries)):
            return None
        for key, items in entries.items():
            if not isinstance(key, str) or not isinstance(items, list):
                return None
            for item in items:
                if (not isinstance(item, list) or len(item) != 5 or not all(isinstance(x, str) for x in (item[0], item[1], item[2], item[4]))
                        or not isinstance(item[3], int)):
                    return None
        return entries
    except (OSError, ValueError, KeyError, TypeError):
        return None


def cache_store(path: Path | None, gate: str, entries: dict) -> bool:
    if path is None:
        return False
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_name(path.name + f".{os.getpid()}.tmp")
        tmp.write_text(json.dumps({"format": CACHE_FORMAT, "gate_sha256": gate, "entries": entries,
                                   "seal": cache_seal(gate, entries)}, sort_keys=True),
                       encoding="utf-8")
        os.replace(tmp, path)
        return True
    except (OSError, ValueError, TypeError):
        return False


def cache_key(gate: str, rel: str, raw: bytes) -> str:
    return hashlib.sha256(gate.encode("ascii") + b"\0" + rel.encode("utf-8", "surrogateescape") + b"\0" + hashlib.sha256(raw).hexdigest().encode("ascii")).hexdigest()


def decode_like_read_text(raw: bytes) -> str:
    """The text `Path.read_text(encoding="utf-8", errors="replace")` returns for these bytes (decoding, then universal-newline translation)."""
    return raw.decode("utf-8", errors="replace").replace("\r\n", "\n").replace("\r", "\n")


def scan_privacy_cached(root: Path, findings: list[Finding], verify: bool = False) -> dict:
    """The privacy scan with a per-file cache. Returns counts; `mismatch` lists files whose cached findings differ from a fresh scan (verify mode only).
    Findings are the same set, to the field, as `scan_privacy_and_secrets(root, findings)` gives; `deduplicate` orders them afterwards, as today."""
    global PRIVACY_FILES
    assert PRIVACY_FILES is None, "scan_privacy_cached is not re-entrant"
    gate = gate_digest()
    path = cache_file(root)
    stored = None if verify else cache_load(path, gate)
    old = cache_load(path, gate) if verify else None
    files = list(iter_privacy_files(root))
    answered: dict[str, list] = {}
    answered_entries: dict[str, list] = {}
    misses: list[Path] = []
    for file in files:
        rel = str(file.relative_to(root))
        try:
            raw = file.read_bytes()
        except OSError:
            misses.append(file)         # unreadable: the scan below meets it exactly as it does today
            continue
        key = cache_key(gate, rel, raw)
        if stored is not None and key in stored:
            answered[rel] = stored[key]
            answered_entries[key] = stored[key]
        else:
            misses.append(file)
    # The files the cache could not answer are read AGAIN, one at a time, and that second read is the one that is both hashed and
    # scanned (the loop's read_text hands back the text decoded from those very bytes), so a file that changes, or changes and changes back,
    # between the first pass and the scan can never be stored under the hash of other bytes than the ones that were judged.
    final_keys: dict[str, str | None] = {}

    def lazily(paths: list[Path]) -> Iterable[Path]:
        for file in paths:
            rel = str(file.relative_to(root))
            PRIVACY_TEXT.clear()
            try:
                raw = file.read_bytes()
            except OSError:
                final_keys[rel] = None
                yield file
                continue
            final_keys[rel] = cache_key(gate, rel, raw)
            PRIVACY_TEXT[file] = decode_like_read_text(raw)
            yield file
        PRIVACY_TEXT.clear()

    fresh: list[Finding] = []
    PRIVACY_FILES = lazily(misses)
    try:
        scan_privacy_and_secrets(root, fresh)
    finally:
        PRIVACY_FILES = None
        PRIVACY_TEXT.clear()
    missed = {str(file.relative_to(root)) for file in misses}
    per_file: dict[str, list] = {rel: [] for rel in missed}
    cacheable = True
    for finding in fresh:
        if finding.path in per_file:
            per_file[finding.path].append([finding.severity, finding.code, finding.path, finding.line, finding.message])
        else:
            cacheable = False           # a finding not tied to a scanned file: nothing is stored from this run
    for items in answered.values():
        findings.extend(Finding(*item) for item in items)
    findings.extend(fresh)
    mismatch = []
    if verify and old is not None:
        for rel, items in per_file.items():
            if final_keys.get(rel) in old and old[final_keys[rel]] != items:
                mismatch.append(rel)
    stored_now = False
    if cacheable:
        entries = {final_keys[rel]: items for rel, items in per_file.items() if final_keys.get(rel)}
        entries.update(answered_entries)
        stored_now = cache_store(path, gate, entries)
    return {"files": len(files), "hits": len(answered), "misses": len(misses), "stored": stored_now, "mismatch": mismatch}


# The search guards inside `scan_privacy_and_secrets` skip a search for a file that cannot match it. They were written
# for ONE version of the scan: this is its digest. Any other version is searched in full (slower, never blind).
GUARDS_WRITTEN_FOR = "0de73db64a94cc0b014a5210f7aee747a21e87739d069744908babad18d9f7f1"


def scan_source_digest() -> str:
    """Digest of everything that decides what the privacy scan can match; "" when the source cannot be read."""
    try:
        parts = [inspect.getsource(part) for part in SCAN_PARTS]
    except (OSError, TypeError):
        return ""
    parts += [pattern.pattern for pattern in (MATERNAL_ORIGIN, PATERNAL_ORIGIN, PARENT_ORIGIN)]
    return hashlib.sha256("\0".join(parts).encode("utf-8")).hexdigest()


def scan_privacy_and_secrets(root: Path, findings: list[Finding]) -> None:
    private_identifier_digests = frozenset({
        "56a9baaa78e21fd28508d820a750a3bdab648145046ae5d2e91ef2480fcb240b",
        "1075bbd8b99ffc4f7392d08031e6d50389395a43a7d4cf7c5a992c2df5ade9fe",
        "91a1dafb023759ab2b7668304bb56db4a166c343b17ea4809c0536bf1dd4e4b8",
        "f4100df23c7a789e35087608882def10fccba81b106a8b9af573032ec94d1419",
        "edb1270b1e407a89a46c02743cbe544e788e511d418dd83f8580985c525e2f41",
    })
    # These identifiers are sensitive in every capitalization, including
    # uppercase segments inside compound mode/file names.  Keep only digests
    # in the publishable detector source.
    casefold_identifier_digests = frozenset({
        "b6e1557a1ed3900d7be8e28bb5f137d91812f31e59a90ceddac0276bc532d18e",
        "07356e8a472bca7eeb7a79dc0fe9a27df6d1d19ad82caee2bebc122463a1d42c",
        "84b3b06a9ad46e0cbde25d76822932275bdd7c523095911095a930c68b4dc3f3",
    })
    identifier_token = re.compile(r"(?<![A-Za-z])[A-Za-z]{3,24}(?![A-Za-z])")
    # A cryptographic digest is not prose, and the letters inside one are not a name.
    # A long digest can contain a three-letter sensitive token by chance — the longer the
    # repository carries content-addressed seals, the more often. Matches that fall inside
    # a long hexadecimal run are therefore skipped, so that re-sealing a baseline cannot
    # trip the privacy gate at random. This narrows only the digest interior: an identifier
    # in ordinary text is unaffected.
    hex_run = re.compile(r"(?<![0-9A-Fa-f])[0-9A-Fa-f]{32,}(?![0-9A-Fa-f])")
    # The same argument at content-address FRAGMENT length. Candidate identifiers in this
    # repository are `RPC-` + 12 hex characters, and a three-letter private token occurred by
    # chance inside three of them (`pathograph_export.jsonl`, measured 2026-09-07: 3 BLOCKs,
    # all false). Twelve hex characters carrying at least one digit are a content address,
    # not a word; the digit is what separates them from letters, and only the digest
    # interior is narrowed — a token bounded by non-letters outside such a run is unaffected.
    hex_fragment = re.compile(
        r"(?<![0-9A-Za-z])(?=[0-9A-Fa-f]*[0-9])[0-9A-Fa-f]{12,}(?![0-9A-Za-z])"
    )
    # 🔴 THE THRESHOLD IS NOT LOWERED, AND THIS IS WHERE THAT DECISION IS RECORDED.
    # An 8-hex abbreviation of a digest (`abcd1234…`) is SHORTER than the carve-out above, so an
    # alphabetic run inside it reads as a candidate identifier and the gate blocks. That happened
    # to two agents on 2026-09-28; both wrote the full 64-hex digest instead, which is this
    # repository's convention and exempt by construction, and shipped. Considered and rejected:
    #   - lowering the carve-out to 8: at 8 characters the "it is an address, not a word" argument
    #     stops holding. A three-letter name needs only five hex neighbours to disappear, and the
    #     gate is a privacy control: a weakening that buys convenience is the wrong trade, and one
    #     nobody would notice, because a false NEGATIVE prints nothing. MEASURED on this
    #     repository, 2026-09-28: over 1614 scanned text files, 1013 alphabetic candidate tokens
    #     sit inside an 8-11 hex run and are examined today; a carve-out at 8 would stop examining
    #     all 1013. That is the cost, and it buys the author nothing a full digest does not.
    #   - exempting a truncated digest next to a digest-ish context word: that makes the exemption
    #     depend on prose the author controls, i.e. an author who writes "sha256" gets a carve-out
    #     an author who does not write it never sees. A privacy carve-out steered by an adjacent
    #     word is a carve-out anybody can request by typing the word.
    # So detection is UNCHANGED and the inconvenience is answered where it is met: a block whose
    # token sits inside a short hex run carries the convention in its message (see below).
    # The pattern is used for the HINT ONLY and never to skip a finding.
    short_hex_fragment = re.compile(
        r"(?<![0-9A-Za-z])(?=[0-9A-Fa-f]*[0-9])[0-9A-Fa-f]{8,11}(?![0-9A-Za-z])"
    )
    uuid_identifier = re.compile(
        r"(?<![0-9A-Za-z])[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}"
        r"-[0-9A-Fa-f]{12}(?![0-9A-Za-z])"
    )
    TRUNCATED_DIGEST_HINT = (
        " If this is a truncated digest or short commit SHA, write the full 64-hex digest: "
        "the repository's convention, exempt by construction (a 12+ hex run is read as a "
        "content address). The threshold is deliberately not lowered for abbreviations."
    )
    # A fourth token is exact-only in the private set above, and deliberately so: it is also
    # an ordinary Italian word, and `test_common_lowercase_homonym_does_not_block` pins that.
    # Inside a FILESYSTEM PATH it cannot be that word, so its casefolded digest is consulted
    # there and nowhere else. The path rule is root-anchored (Mirror v2 § 1.6, 2026-08-26),
    # not separator-anchored: the first shipped predicate — "preceded by a slash, followed by
    # a terminator" — blocked the Italian superlative pair `minimo/<token>` (F-1) and, in
    # this whole-file scanner, missed a path that ends a LINE (F-2). Both close structurally
    # once the rule starts from a closed set of path roots and reads the run that follows:
    # a slash-pair has no root, so no special case is written for it. The run ends at
    # whitespace, a quote, or list punctuation (`,` `;` `|` and brackets) — the characters
    # that separate CELLS and never sit inside a segment of a machine path — so a table row
    # or a CSV field holding a path and then the homonym is two runs, not one. A sentence
    # period, markdown bold or a colon stays INSIDE the run and is harmless: only alphabetic
    # sub-runs are hashed, and the token precedes the punctuation.
    path_casefold_identifier_digests = frozenset({
        "f805bcb3efc982ec60744b3cc23f11ed1a4a0c4b783f345c1dc64ebab616da91",
    })
    path_digests = casefold_identifier_digests | path_casefold_identifier_digests
    path_root = re.compile(
        r"(?<![A-Za-z0-9_.~-])(?:/Users/|/home/|/var/folders/|~/)"
        r"|(?<![A-Za-z0-9])[A-Za-z]:\\Users\\"
    )
    path_run = re.compile(r"[^\s\"'`,;|()\[\]<>]+")
    path_word = re.compile(r"[A-Za-z]{3,}")
    # Harvested bibliographic metadata: a published author may share a given name with a
    # private identifier, and a digest scanner cannot tell them apart. The one structural
    # context that says "this is a PubMed author, not the private individual" is the
    # `fore_name` / `last_name` field of a record in a harvested corpus seed. There the match
    # is REPORTED — as REVIEW, never silently — under its own code, so a reader sees it and
    # the file is not blocked for carrying public bibliography. Option C of the Mirror
    # decision packet (names and institutions permitted, contact fields restricted) is what
    # the operator chose on 2026-09-07, when affiliation e-mails were redacted from the seed.
    corpus_seed = re.compile(r"(?:^|/)registries/corpus_seed_pubmed_[0-9]{8}\.jsonl$")
    bibliographic_name_field = re.compile(r"\"(?:fore_name|last_name)\": \"$")
    email_address = re.compile(
        r"(?i)(?<![A-Z0-9._%+-])"
        r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}"
        r"(?![A-Z0-9_%+-])"
    )
    report_id = re.compile(r"(?i)\b(?:referto|report)\s+(?:id\s*)?(?<![A-Za-z0-9])((?-i:NG)[-\d]{5,})\b")
    private_key = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")
    token_patterns = [
        ("OPENAI_KEY", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
        ("GITHUB_TOKEN", re.compile(r"\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}\b")),
        ("AWS_KEY", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
        (
            "PASSWORD_ASSIGNMENT",
            re.compile(r"(?i)\b(?:password|passwd|pwd)\s*[:=]\s*[\"']?[^ \n\"']{8,}"),
        ),
    ]

    variant_a = re.compile(
        r"(?i)(?:\bQ\s*230\s*P\b|\bp\.\s*\(?Gln\s*230\s*Pro\)?\b|"
        r"\bGln\s*230\s*Pro\b)"
    )
    variant_b = re.compile(
        r"(?i)\bc\.\s*1057\s*[-\N{MINUS SIGN}\N{EN DASH}]\s*2\s*A\s*>\s*G\b"
    )
    person_context = re.compile(
        r"(?i)\b(?:the\s+proband|proband|index patient|patient-specific|"
        r"patient-derived|individual patient|"
        r"index case|case subject|affected child|affected individual|"
        r"study participant)\b"
    )
    # The gap recorded here on 2026-08-10 — `mother'?s` matched *mother's* but not bare
    # *mother* — is closed at the module-level vocabulary, with the measurement that the
    # deferral demanded written beside it.
    parent_origin = PARENT_ORIGIN
    maternal_origin = MATERNAL_ORIGIN
    paternal_origin = PATERNAL_ORIGIN
    compound_linkage = re.compile(
        r"(?i)\b(?:compound[- ]het(?:erozyg(?:ous|osity)?)?|"
        r"biallelic(?: genotype)?|"
        r"compound[- ]eterozigot[eo]|eterozigosi composta|"
        r"genotipo biallelico|biallelic[oa]|"
        r"in trans|paired alleles?|allelic combination|compound genotype|"
        r"same (?:case|individual|patient|person)|co[- ]?occurr(?:ing|ed|ence)|"
        r"carr(?:y|ies|ied) both|two[- ]variant genotype)\b"
    )
    cross_paragraph_pairing = re.compile(
        r"(?is)\b(?:"
        r"(?:these|the)\s+two\s+(?:variants?|alleles?)|"
        r"together.{0,120}(?:variants?|alleles?)|"
        r"(?:variants?|alleles?).{0,120}together|"
        r"combin(?:e|es|ed|ing).{0,120}(?:variants?|alleles?)"
        r")\b"
    )
    clinical_context = re.compile(
        r"(?i)\b(?:folinate|folinato|lamotrigine|levetiracetam|mg/kg|"
        r"ketogenic diet|AED titration|clinical record|clinical regimen|"
        r"patient cells?|cellule (?:del|di|the) proband)\b"
    )
    geography = re.compile(r"(?i)\b(?:Italy|Italia|Italian)\b")
    reference_genotype = re.compile(
        r"(?i)\b(?:reference genotype|genotipo di riferimento|"
        r"worked[- ]example alleles?)\b"
    )
    public_taint = re.compile(
        r"(?im)^\s*(?:source_scope|provenance)\s*:\s*(?:PRIVATE|MIXED)\b"
    )

    # The digest membership test runs FIRST and is cached per distinct word. Both tests below
    # only ever skip a word, so their order cannot change a finding — but the digest-interior
    # test is a scan over every hex span in the file, and running it for each of ~4M words
    # before asking whether the word is sensitive at all cost ~45 s of a ~70 s gate
    # (measured 2026-09-24). Almost no word is sensitive, so the span scan now runs only for
    # the rare word that would otherwise become a finding.
    @functools.lru_cache(maxsize=None)
    def is_sensitive(word: str) -> bool:
        return (
            hashlib.sha256(word.encode()).hexdigest() in private_identifier_digests
            or hashlib.sha256(word.casefold().encode()).hexdigest()
            in casefold_identifier_digests
        )

    # 🔴 SPEED ONLY (HE, 2026-11-25): a search is skipped for a file that cannot match it. Every guard below names, for
    # EVERY alternative of the pattern it guards, a literal that any match must contain. The guards are in force only
    # while this function and its patterns are the ones they were written for (`GUARDS_WRITTEN_FOR`): after ANY change
    # everything is searched in full until the guards have been re-read and the digest updated, which
    # `test_search_guards_are_in_force` asks for. `test_every_alternative_behind_a_search_guard_is_still_reached`
    # plants one positive per alternative. The guards read the lowercased text, which says the same as `(?i)` for ASCII
    # letters except for three non-ASCII characters (İ ı ſ): a file holding any of them is searched in full. (The
    # fourth such character, the Kelvin sign, lowercases to k and needs nothing.)
    guarding = scan_source_digest() == GUARDS_WRITTEN_FOR
    unusual_case = ("\u0130", "\u0131", "\u017f")
    letter_runs = re.compile(r"[A-Za-z]{3,}")
    harmless: set[str] = set()             # words already hashed and found not sensitive

    for path in iter_privacy_files(root):
        if not in_scope(root, path):
            continue
        text = read_text(path)
        rel = str(path.relative_to(root))
        if rel in GATE_INTERNAL_FILES:
            continue
        lowered = text.lower()
        search_all = not guarding or any(char in text for char in unusual_case)

        def may(*literals: str) -> bool:               # for a case-insensitive pattern
            return search_all or any(literal in lowered for literal in literals)

        def has(*literals: str) -> bool:               # for a case-sensitive one
            return search_all or any(literal in text for literal in literals)

        has_230, has_1057 = has("230"), has("1057")                # variant_a, variant_b
        has_maternal = may("materna", "materno", "mother", "madre")
        has_paternal = may("paterna", "paterno", "father", "padre")
        has_parent = has_maternal or has_paternal or may("parent")
        # an identifier is a whole run of 3 to 24 letters: with none of them sensitive, the loop below finds nothing
        new_words = set(letter_runs.findall(text)) - harmless
        sensitive = {word for word in new_words if len(word) <= 24 and is_sensitive(word)}
        harmless.update(new_words - sensitive)
        if sensitive or not guarding:
            digest_spans = [m.span() for m in hex_run.finditer(text)]
            digest_spans += [m.span() for m in hex_fragment.finditer(text)]
            # Not added to `digest_spans`: these spans change no verdict, only a message.
            short_spans = [m.span() for m in short_hex_fragment.finditer(text)]
            identifiers = identifier_token.finditer(text)
        else:
            digest_spans, short_spans, identifiers = [], [], ()
        uuid_spans: list[tuple[int, int]] | None = None
        for match in identifiers:
            if not is_sensitive(match.group(0)):
                continue
            if any(start <= match.start() and match.end() <= end
                   for start, end in digest_spans):
                continue
            # A canonical UUID (8-4-4-4-12 hex, at least one digit) is a record identifier, not
            # prose. Its 8- and 4-hex groups are below the 12-hex carve-out, so the one private
            # token made only of hex letters read as a name inside DailyMed set-ids and
            # Signature Commons entity ids (measured on history, IT8: 15 findings, 6 blobs,
            # every one inside a UUID). Only a match CONTAINED in the UUID is skipped: a token
            # beside a UUID (space, hyphen, comma) or glued to it is outside the span and
            # still blocks. Computed lazily, once per file, only for a sensitive word.
            if uuid_spans is None:
                uuid_spans = [m.span() for m in uuid_identifier.finditer(text)
                              if any(ch.isdigit() for ch in m.group(0))]
            if any(start <= match.start() and match.end() <= end
                   for start, end in uuid_spans):
                continue
            if (
                corpus_seed.search(rel)
                and text[match.end():match.end() + 1] == '"'
                and bibliographic_name_field.search(text[max(0, match.start() - 14):match.start()])
            ):
                findings.append(
                    Finding(
                        "REVIEW",
                        "PUBLIC_BIBLIOGRAPHIC_AUTHOR",
                        rel,
                        line_number(text, match.start()),
                        "A published author's name field in a harvested corpus seed matches "
                        "a private identifier digest. Not blocked; confirm it is the author.",
                    )
                )
                continue
            hint = (TRUNCATED_DIGEST_HINT
                    if any(start <= match.start() and match.end() <= end
                           for start, end in short_spans) else "")
            findings.append(
                Finding(
                    "BLOCK",
                    "DIRECT_IDENTIFIER",
                    rel,
                    line_number(text, match.start()),
                    "Legacy personal identifier remains in public material." + hint,
                )
            )
        for root_match in path_root.finditer(text) if has("Users", "/home/", "/var/folders/", "~/") else ():
            run = path_run.match(text, root_match.start())
            if run is None:
                continue
            for word in path_word.finditer(run.group(0)):
                folded = hashlib.sha256(word.group(0).casefold().encode()).hexdigest()
                if folded not in path_digests:
                    continue
                findings.append(
                    Finding(
                        "BLOCK",
                        "DIRECT_IDENTIFIER",
                        rel,
                        line_number(text, run.start() + word.start()),
                        "Personal identifier inside a machine-local path in public material.",
                    )
                )
        for match in email_address.finditer(text) if has("@") else ():
            address = match.group(0).lower()
            if (
                address in PLACEHOLDER_TOKENS
                or address.endswith("@example.invalid")
                or address.endswith("@example.test")
            ):
                continue
            findings.append(
                Finding(
                    "BLOCK",
                    "EMAIL_ADDRESS",
                    rel,
                    line_number(text, match.start()),
                    "A non-placeholder email address remains in public material.",
                )
            )
        if has("NG") and may("report", "referto"):
            add_matches(
                findings, root, path, text, "REPORT_IDENTIFIER",
                report_id, "A case/report identifier remains in public material.",
            )
        if has("PRIVATE KEY-----"):
            add_matches(
                findings, root, path, text, "PRIVATE_KEY",
                private_key, "Private key material detected.",
            )
        if may("source_scope", "provenance"):
            add_matches(
                findings, root, path, text, "NON_PUBLIC_PROVENANCE",
                public_taint, "Explicit PRIVATE/MIXED provenance is not publishable.",
            )

        is_placeholder_file = any(token in lowered for token in PLACEHOLDER_TOKENS)
        token_possible = {
            "OPENAI_KEY": has("sk-"),
            "GITHUB_TOKEN": has("ghp_", "github_pat_"),
            "AWS_KEY": has("AKIA"),
            "PASSWORD_ASSIGNMENT": may("passw", "pwd"),
        }
        for code, pattern in token_patterns:
            for match in pattern.finditer(text) if token_possible.get(code, True) else ():
                matched = match.group(0).lower()
                if is_placeholder_file and any(
                    token in matched for token in PLACEHOLDER_TOKENS
                ):
                    continue
                findings.append(
                    Finding(
                        "BLOCK", code, rel, line_number(text, match.start()),
                        "Potential secret or credential detected.",
                    )
                )

        # A linked two-variant genotype can re-identify even when words such as
        # "proband" have been removed. A generic disease-level genotype rule
        # beside independent worked examples must remain allowed.
        # both findings of a record need the two variants, or the two parental sides, inside it
        variants_here, sides_here = has_230 and has_1057, has_maternal and has_paternal
        for block_offset, block in record_blocks(text, rel) if variants_here or sides_here else ():
            relationship = (compound_linkage.search(block)
                            if search_all or (variants_here and "230" in block and "1057" in block) else None)
            if (
                relationship
                and variant_a.search(block)
                and variant_b.search(block)
            ):
                findings.append(
                    Finding(
                        "BLOCK",
                        "REIDENTIFYING_VARIANT_COMBINATION",
                        rel,
                        line_number(text, block_offset + relationship.start()),
                        "An exact two-variant combination is linked as one genotype/case.",
                    )
                )
            maternal = maternal_origin.search(block) if sides_here else None
            paternal = paternal_origin.search(block) if maternal else None
            if (
                maternal
                and paternal
                and not parent_origin_is_explicitly_negated(block)
            ):
                # 🔴 ATTRIBUTION, added 2026-08-10 after this rule blocked a published case
                # report and the two sharp rules stayed silent — correctly, because the
                # variants involved are not the reference genotype's.
                #
                # This is the broad net of the three: a maternal word and a paternal word in
                # one block, no variant, no person noun, no reference genotype. Its POPULATION
                # is "every paragraph naming both parents"; its TARGET is "paragraphs about the
                # private individual". A repository built on trio literature lives in the
                # complement, and the corpus had only avoided it by accident — no earlier paper
                # happened to mention both parents in one paragraph.
                #
                # What the line actually is, measured against what already passes: this state
                # carries published individual-level readings throughout — a single-patient case
                # report with age, sex and a ClinVar accession; a thirteen-patient cohort with
                # per-patient variants. All on `main`, all through this gate. So the boundary
                # the repository enforces is not "no individual data", it is "not the private
                # overlay's individual", which is exactly what `CLAUDE.md` says the layering is.
                #
                # So the net now asks whose parents these are, by the only mechanical proxy
                # that separates the two: is this record ATTRIBUTED to a published study. The
                # reference genotype is never suppressed — its variants below force the BLOCK
                # whatever the attribution says, and the two sharp rules fire independently.
                #
                # And a suppression is REPORTED, not silent. A privacy exemption nobody can see
                # in the output is the one that stops being reviewed.
                window = attribution_window(text, block_offset, block, rel)
                # 🔴 THE SAME WINDOW FOR BOTH QUESTIONS, and the first version got this wrong
                # in the dangerous direction: attribution was evaluated on the wide window and
                # the safeguard on the narrow block. A heading naming `Q230P` then WIDENED the
                # attribution without widening the protection, so the reference genotype
                # stopped being unsuppressable exactly when its variant sat in a section title
                # instead of a paragraph — which is the realistic shape, a queue entry titled
                # with its paper and arguing three paragraphs below.
                #
                # A safeguard must be at least as wide as whatever can suspend it. Widening it
                # is conservative in one direction only: it can produce more BLOCKs, never
                # fewer. Found by a reader who tried the neighbouring case instead of the one
                # the test declared.
                reference_present = bool(
                    variant_a.search(window)
                    or variant_b.search(window)
                    or reference_genotype.search(window)
                )
                attributed = bool(STUDY_IDENTIFIER.search(window))
                line = line_number(
                    text, block_offset + min(maternal.start(), paternal.start()))
                if attributed and not reference_present:
                    findings.append(
                        Finding(
                            "REVIEW",
                            "PARENT_OF_ORIGIN_ATTRIBUTED",
                            rel,
                            line,
                            "Maternal and paternal sides are paired, and the record is "
                            "attributed to a published study whose variants are not the "
                            "reference genotype's. Not blocked; read it before publishing.",
                        )
                    )
                else:
                    findings.append(
                        Finding(
                            "BLOCK",
                            "PARENT_OF_ORIGIN_PAIRING",
                            rel,
                            line,
                            "Maternal and paternal disease-model sides are paired in one "
                            "record, with no published study to attribute them to.",
                        )
                    )
        # Catch a concluding cross-paragraph reassembly only when it uses
        # explicit pairing language such as "these two variants" or "together".
        for pairing in cross_paragraph_pairing.finditer(text) if has_230 and has_1057 else ():
            start = max(0, pairing.start() - 2200)
            end = min(len(text), pairing.end() + 500)
            window = text[start:end]
            relationship = compound_linkage.search(window)
            if (
                relationship
                and variant_a.search(window)
                and variant_b.search(window)
            ):
                findings.append(
                    Finding(
                        "BLOCK",
                        "REIDENTIFYING_VARIANT_COMBINATION",
                        rel,
                        line_number(text, pairing.start()),
                        "Separated worked examples are explicitly reassembled as one genotype.",
                    )
                )

        # Parent-of-origin plus an exact variant is itself identifying linkage;
        # it does not require an explicit person noun. Explicit statements that
        # the relationship was removed or decoupled are allowed.
        # both findings need a parental word and, near it, a variant or the reference genotype
        near = has_230 or has_1057 or may("reference genotype", "genotipo di riferimento", "example allele")
        for marker in parent_origin.finditer(text) if has_parent and near else ():
            start = max(0, marker.start() - 350)
            end = min(len(text), marker.end() + 350)
            if rel.endswith(".jsonl"):
                # One record per line: a parental word in one record and a variant in the
                # next are two records, and this window must not reach across them.
                start = max(start, text.rfind("\n", 0, marker.start()) + 1)
                line_end = text.find("\n", marker.end())
                end = min(end, len(text) if line_end < 0 else line_end)
            window = text[start:end]
            if (
                (variant_a.search(window) or variant_b.search(window))
                and not parent_origin_is_explicitly_negated(window)
            ):
                findings.append(
                    Finding(
                        "BLOCK",
                        "PARENT_OF_ORIGIN_VARIANT_LINKAGE",
                        rel,
                        line_number(text, marker.start()),
                        "Parent-of-origin is linked to an exact variant.",
                    )
                )
            if (
                reference_genotype.search(window)
                and not parent_origin_is_explicitly_negated(window)
            ):
                findings.append(
                    Finding(
                        "BLOCK",
                        "PARENT_OF_ORIGIN_REFERENCE_GENOTYPE",
                        rel,
                        line_number(text, marker.start()),
                        "Parent-of-origin is linked to the persistent reference genotype.",
                    )
                )

        # Semantic/case-linkage checks use local windows, not isolated keywords.
        # a person noun is a finding only beside: both variants; a parental word and one variant; a clinical term; a country
        person_possible = may("proband", "patient", "index case", "case subject", "affected ", "study participant") and (
            (has_230 and has_1057) or (has_parent and (has_230 or has_1057))
            or may("folinat", "lamotrigine", "levetiracetam", "mg/kg", "ketogenic", "titration", "clinical r",
                   "patient cell", "cellule", "italy", "italia"))
        for marker in person_context.finditer(text) if person_possible else ():
            local_context = text[
                max(0, marker.start() - 120):min(len(text), marker.end() + 120)
            ]
            if person_context_is_explicitly_negated(local_context):
                continue
            start = max(0, marker.start() - 700)
            end = min(len(text), marker.end() + 700)
            # Deliberately NOT clipped to one record on `.jsonl`: clipping it removed
            # cross-record BLOCKs (a person noun in one record, the two variants in the
            # next two) that the file-wide window raised. Uncertainty resolves towards
            # scanning more, never less; the parental-word window above is the one record
            # rule, because a parental word and a variant in different records are not a
            # transmission claim. Blind review R-1, 2026-09-08.
            window = text[start:end]
            if variant_a.search(window) and variant_b.search(window):
                findings.append(
                    Finding(
                        "BLOCK", "REIDENTIFYING_VARIANT_COMBINATION", rel,
                        line_number(text, marker.start()),
                        "A person/proband is linked to the exact two-variant combination.",
                    )
                )
            if parent_origin.search(window) and (
                variant_a.search(window) or variant_b.search(window)
            ):
                findings.append(
                    Finding(
                        "BLOCK", "PARENT_OF_ORIGIN_LINKAGE", rel,
                        line_number(text, marker.start()),
                        "Parent-of-origin is linked to a person and a specific variant.",
                    )
                )
            if clinical_context.search(window):
                findings.append(
                    Finding(
                        "BLOCK", "CLINICAL_CASE_LINKAGE", rel,
                        line_number(text, marker.start()),
                        "Clinical regimen/sample detail is linked to a person/proband.",
                    )
                )
            if geography.search(window):
                findings.append(
                    Finding(
                        "BLOCK", "GEOGRAPHIC_CASE_LINKAGE", rel,
                        line_number(text, marker.start()),
                        "Geography is linked to a person/proband context.",
                    )
                )


# bound here, not by name at call time: a test that wraps the scan must not read as a changed scan
SCAN_PARTS = (scan_privacy_and_secrets, record_blocks, semantic_blocks)


def scan_links(root: Path, findings: list[Finding]) -> None:
    markdown_link = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    wikilink = re.compile(r"\[\[([^\]#|]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
    by_name: dict[str, list[Path]] = {}

    def fill_names() -> None:
        for file_path in iter_files(root):
            by_name.setdefault(file_path.name, []).append(file_path)
            by_name.setdefault(file_path.stem, []).append(file_path)
        for directory in walk_publishable(root):
            if directory.is_dir():
                by_name.setdefault(directory.name, []).append(directory)

    if ONLY_PATHS is None:
        fill_names()            # the full gate builds the name index up front, as before
    names_filled = ONLY_PATHS is None

    for path in iter_text_files(root):
        if path.suffix.lower() != ".md" or not in_scope(root, path):
            continue
        text = read_text(path)
        rel = str(path.relative_to(root))
        for match in markdown_link.finditer(text):
            target = match.group(1).strip()
            if (
                not target
                or target.startswith(("#", "http://", "https://", "mailto:"))
                or "://" in target
            ):
                continue
            clean = target.split("#", 1)[0].split("?", 1)[0]
            if clean in MARKDOWN_LINK_EXAMPLES:
                continue
            resolved = (path.parent / clean).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                findings.append(
                    Finding(
                        "BLOCK", "LINK_ESCAPES_REPO", rel,
                        line_number(text, match.start()),
                        f"Relative link escapes repository: {target}",
                    )
                )
                continue
            if not resolved.exists():
                findings.append(
                    Finding(
                        "BLOCK", "BROKEN_MARKDOWN_LINK", rel,
                        line_number(text, match.start()),
                        f"Missing relative-link target: {target}",
                    )
                )

        for match in wikilink.finditer(text):
            target = match.group(1).strip()
            if target in WIKILINK_EXAMPLES:
                continue
            name = Path(target).name
            candidates = {name, f"{name}.md"}
            if not names_filled:    # a pre-check builds the whole-tree name index only when a wikilink needs it
                fill_names()
                names_filled = True
            if not any(candidate in by_name for candidate in candidates):
                findings.append(
                    Finding(
                        "BLOCK", "BROKEN_WIKILINK", rel,
                        line_number(text, match.start()),
                        f"Missing wikilink target: {target}",
                    )
                )


def declared_data_patterns(data_sources_text: str) -> list[str]:
    patterns: list[str] = []
    for match in re.finditer(r"`((?:analysis/data|eval/data)/[^`]+)`", data_sources_text):
        patterns.append(match.group(1))
    return patterns


def provenance_scopes(relative: str) -> list[str]:
    """Return DATA_SOURCES-style paths for a repository-relative asset."""
    path = Path(relative)
    candidates = [relative]
    parts = path.parts
    if len(parts) >= 4 and parts[0] == "disease-models":
        candidates.append(Path(*parts[2:]).as_posix())
    if len(parts) >= 3 and parts[0] == "framework":
        candidates.append(Path(*parts[1:]).as_posix())
    return candidates


def scan_provenance(root: Path, findings: list[Finding]) -> None:
    required = [
        root / "DATA_SOURCES.md",
        root / "THIRD_PARTY_NOTICES.md",
        root / "_external_repos" / "MANIFEST.md",
    ]
    for path in required:
        if not path.exists():
            findings.append(
                Finding(
                    "BLOCK", "MISSING_PROVENANCE_FILE",
                    str(path.relative_to(root)), 1,
                    "Required provenance/licensing manifest is missing.",
                )
            )

    data_sources = root / "DATA_SOURCES.md"
    if not data_sources.exists():
        return
    text = read_text(data_sources)
    for marker in ("TBD", "VERIFY BEFORE RELEASE", "UNKNOWN LICENSE"):
        for match in re.finditer(re.escape(marker), text, flags=re.IGNORECASE):
            findings.append(
                Finding(
                    "BLOCK", "UNRESOLVED_PROVENANCE", "DATA_SOURCES.md",
                    line_number(text, match.start()),
                    f"Unresolved provenance marker: {marker}",
                )
            )

    patterns = declared_data_patterns(text)
    for path in iter_files(root):
        rel = str(path.relative_to(root))
        scopes = provenance_scopes(rel)
        if not any(
            scope.startswith(("analysis/data/", "eval/data/"))
            for scope in scopes
        ):
            continue
        if not any(
            fnmatch.fnmatch(scope, pattern)
            for scope in scopes
            for pattern in patterns
        ):
            findings.append(
                Finding(
                    "BLOCK", "UNDECLARED_DATA_ASSET", rel, 1,
                    "Data asset is not covered by DATA_SOURCES.md.",
                )
            )


def scan_readme_consistency(root: Path, findings: list[Finding]) -> None:
    readme = root / "README.md"
    if not readme.exists():
        findings.append(
            Finding("BLOCK", "MISSING_README", "README.md", 1, "README.md is missing.")
        )
        return
    text = read_text(readme)
    lower = text.lower()
    # Through the shared walker: a nested checkout would otherwise double this count and
    # make an overclaim check pass on code that is not part of this repository at all.
    python_files = [path for path in iter_files(root) if path.suffix == ".py"]

    if "full machine" in lower and len(python_files) <= 1:
        findings.append(
            Finding(
                "BLOCK", "README_CAPABILITY_OVERCLAIM", "README.md",
                line_number(lower, lower.index("full machine")),
                "README claims a full machine but ships no operational implementation.",
            )
        )
    if "sponsored by" in lower and not (root / "SPONSORSHIP.md").exists():
        findings.append(
            Finding(
                "BLOCK", "UNVERIFIED_SPONSORSHIP", "README.md",
                line_number(lower, lower.index("sponsored by")),
                "Sponsorship claim requires a committed SPONSORSHIP.md attestation.",
            )
        )

    corpus = "\n".join(
        read_text(path)
        for path in iter_text_files(root)
        if str(path.relative_to(root)) not in GATE_INTERNAL_FILES
    )
    no_patient_claim = re.search(
        r"(?i)(?:no (?:real )?patient (?:is )?referenced|"
        r"contains no patient(?:'s)? clinical record)",
        corpus,
    )
    patient_markers = re.search(
        r"(?i)(?:(?<![A-Za-z0-9])(?-i:NG)[-\d]{5,}(?![-\dA-Za-z])|allele materno|allele paterno|"
        r"maternal\s+c\.1057-2A>G|paternal\s+(?:Q230P|p\.Gln230Pro)|"
        r"the proband.{0,200}(?:folinato|folinate|mg/kg|patient cells))",
        corpus,
        flags=re.DOTALL,
    )
    if no_patient_claim and patient_markers:
        findings.append(
            Finding(
                "BLOCK", "README_PRIVACY_CONTRADICTION", "README.md", 1,
                "Repository claims no patient is referenced, but case-linkage markers remain.",
            )
        )

    required_ci = root / ".github" / "workflows" / "public-release-gate.yml"
    if not required_ci.exists():
        findings.append(
            Finding(
                "BLOCK", "MISSING_RELEASE_CI",
                ".github/workflows/public-release-gate.yml", 1,
                "Release-gate CI workflow is missing.",
            )
        )


def run_clean_clone(root: Path, findings: list[Finding], report_json: str | None) -> None:
    git_dir = root / ".git"
    if not git_dir.exists():
        findings.append(
            Finding(
                "BLOCK", "NOT_A_GIT_CLONE", ".", 1,
                "Clean-clone execution requires a Git repository.",
            )
        )
        return
    status = subprocess.run(
        ["git", "-C", str(root), "status", "--porcelain"],
        check=False, capture_output=True, text=True,
    )
    if status.returncode != 0:
        findings.append(
            Finding("BLOCK", "GIT_STATUS_FAILED", ".", 1, status.stderr.strip())
        )
        return
    if status.stdout.strip():
        findings.append(
            Finding(
                "BLOCK", "DIRTY_RELEASE_TREE", ".", 1,
                "Final release review must run from a clean committed tree.",
            )
        )
        return

    with tempfile.TemporaryDirectory(prefix="legend-public-gate-") as temp_dir:
        archive = Path(temp_dir) / "repo.tar"
        clone = Path(temp_dir) / "clone"
        clone.mkdir()
        with archive.open("wb") as handle:
            proc = subprocess.run(
                ["git", "-C", str(root), "archive", "HEAD"],
                check=False, stdout=handle, stderr=subprocess.PIPE,
            )
        if proc.returncode != 0:
            findings.append(
                Finding(
                    "BLOCK", "GIT_ARCHIVE_FAILED", ".", 1,
                    proc.stderr.decode("utf-8", errors="replace").strip(),
                )
            )
            return
        with tarfile.open(archive) as tar:
            # git archive contains repository-relative members only. Validate
            # again for compatibility with Python versions predating filter=.
            for member in tar.getmembers():
                destination = (clone / member.name).resolve()
                try:
                    destination.relative_to(clone.resolve())
                except ValueError as exc:
                    raise RuntimeError(
                        f"Unsafe path in git archive: {member.name}"
                    ) from exc
            tar.extractall(clone)
        gate = clone / "scripts" / "public_release_gate.py"
        command = [
            sys.executable, str(gate), "--root", str(clone),
            "--mode", "clone", "--skip-clean-clone",
        ]
        if report_json:
            command.extend(["--report-json", str(Path(temp_dir) / "clone-report.json")])
        proc = subprocess.run(command, check=False, capture_output=True, text=True)
        if proc.returncode != 0:
            findings.append(
                Finding(
                    "BLOCK", "CLEAN_CLONE_GATE_FAILED", ".", 1,
                    "Gate failed in clean archive:\n" + proc.stdout[-3000:],
                )
            )


def deduplicate(findings: list[Finding]) -> list[Finding]:
    unique: dict[tuple[str, str, str, int, str], Finding] = {}
    for finding in findings:
        key = (
            finding.severity, finding.code, finding.path,
            finding.line, finding.message,
        )
        unique[key] = finding
    return sorted(unique.values(), key=lambda f: (f.path, f.line, f.code))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument(
        "--mode", choices=("staging", "release", "clone"), default="staging"
    )
    parser.add_argument("--report-json", help="Write machine-readable report")
    parser.add_argument("--skip-clean-clone", action="store_true")
    parser.add_argument(
        "--paths", nargs="+", metavar="FILE",
        help=("PRE-CHECK, not the gate: run only the per-file content scans (privacy and case "
              "linkage, secrets, local markdown links) on these repository-relative files"))
    parser.add_argument(
        "--cache", action="store_true",
        help=("OPT-IN, off by default: reuse the stored result of the per-file privacy scan for files whose bytes and the "
              "gate script are unchanged (also LEGEND_GATE_CACHE=1). The link, README and provenance scans always run in full."))
    parser.add_argument(
        "--no-cache", action="store_true",
        help="Never read or write the privacy cache, whatever LEGEND_GATE_CACHE says: exactly today's behaviour")
    parser.add_argument(
        "--cache-verify", action="store_true",
        help=("Audit: scan every file in full, compare with the stored result, exit 3 (CACHE_MISMATCH) on any difference, "
              "then rewrite the cache from the fresh scan"))
    parser.add_argument(
        "--changed-since", metavar="REF",
        help=("PRE-CHECK, not the gate: the same per-file scans on the files changed since REF "
              "(git diff REF, plus untracked files not ignored)"))
    return parser.parse_args()


def documented_commands_precheck(root: Path) -> tuple[str, list[str]]:
    """ADV-060, pre-check only: the cheap half of `scripts/test_documented_commands.py` (do the Python paths that documents name exist), over the
    whole documented surface, about five seconds. Its slow half (running `--help` of every documented command) is not run. The gate does not call this."""
    path = root / "scripts" / "test_documented_commands.py"
    if not path.is_file():
        return "not run (scripts/test_documented_commands.py is absent in this root)", []
    try:
        spec = importlib.util.spec_from_file_location("documented_commands_precheck", path)
        module = importlib.util.module_from_spec(spec)
        sys.modules["documented_commands_precheck"] = module
        spec.loader.exec_module(module)
        missing = module.missing_documented_commands()
    except Exception as exc:   # a scan that could not run is said so; it is never read as a pass
        return f"not run ({type(exc).__name__}: {str(exc)[:160]})", []
    return ("PASS" if not missing else f"FAIL: {len(missing)} documented Python path(s) do not exist"), list(missing)


def changed_since(root: Path, ref: str) -> list[str]:
    """Repository-relative paths changed since `ref` in the working tree, plus untracked files."""
    def git(*cmd: str) -> list[str]:
        done = subprocess.run(["git", "-C", str(root), *cmd], capture_output=True, text=True)
        if done.returncode != 0:
            raise RuntimeError(f"git {' '.join(cmd)}: {done.stderr.strip()[:200]}")
        return [line for line in done.stdout.splitlines() if line.strip()]
    return sorted(set(git("diff", "--name-only", "--diff-filter=ACMR", ref))
                  | set(git("ls-files", "--others", "--exclude-standard")))


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"GATE_ERROR: root is not a directory: {root}", file=sys.stderr)
        return 3

    global ONLY_PATHS
    precheck = bool(args.paths or args.changed_since)
    if precheck:
        try:
            named = list(args.paths or []) + (changed_since(root, args.changed_since) if args.changed_since else [])
        except (RuntimeError, OSError) as exc:
            print(f"GATE_ERROR: {exc}", file=sys.stderr)
            return 3
        ONLY_PATHS = frozenset(Path(p).as_posix().lstrip("./") if not Path(p).is_absolute()
                               else Path(p).resolve().relative_to(root).as_posix() for p in named)

    findings: list[Finding] = []
    try:
        use_cache = not args.no_cache and not precheck and (
            args.cache or args.cache_verify or os.environ.get(CACHE_ENV) == "1")
        if use_cache:
            stats = scan_privacy_cached(root, findings, verify=args.cache_verify)
            print(f"GATE_CACHE: files={stats['files']} hits={stats['hits']} misses={stats['misses']} stored={stats['stored']}",
                  file=sys.stderr)
            if stats["mismatch"]:
                print("GATE_ERROR: CACHE_MISMATCH: the stored privacy result differs from a fresh scan for: "
                      + ", ".join(stats["mismatch"][:20]), file=sys.stderr)
                return 3
        else:
            scan_privacy_and_secrets(root, findings)
        scan_links(root, findings)
        if precheck:
            pass    # tree-level scans and the clean clone belong to the gate, not to the pre-check
        else:
            scan_provenance(root, findings)
        scan_readme_consistency(root, findings)
        if args.mode in {"release", "clone"} and not args.skip_clean_clone:
            run_clean_clone(root, findings, args.report_json)
    except Exception as exc:  # fail closed
        print(f"GATE_ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 3

    if precheck:
        # tree-level findings that the privacy function also emits (a missing CI workflow, for one) are the gate's business: keep the ones about the named files
        findings = [finding for finding in findings if finding.path in (ONLY_PATHS or ())]
    findings = deduplicate(findings)
    blocks = [finding for finding in findings if finding.severity == "BLOCK"]
    result = {
        "verdict": "BLOCK_PUBLICATION" if blocks else "PASS",
        "mode": args.mode,
        "root": str(root),
        "block_count": len(blocks),
        "findings": [asdict(finding) for finding in findings],
    }
    if args.report_json:
        report_path = Path(args.report_json)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(
            json.dumps(result, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    if precheck:
        result["mode"] = "precheck"
        print(f"PRECHECK_VERDICT: {'BLOCK' if blocks else 'PASS'} (per-file scans only; this is NOT a gate verdict)")
        print(f"FILES NAMED: {len(ONLY_PATHS or ())}; BLOCKS: {len(blocks)}")
        print("NOT CHECKED: provenance coverage, README and repository consistency, the clean clone, "
              "and every file that was not named. Only the full gate (`safe_push.py`) may publish.")
    else:
        print(f"VERDICT: {result['verdict']}")
        print(f"BLOCKS: {len(blocks)}")
    documented_failed = False
    if precheck:
        status, missing = documented_commands_precheck(root)
        print(f"DOCUMENTED_COMMANDS_PRECHECK: {status} (the path half of scripts/test_documented_commands.py over every documented Markdown file; "
              "its --help half is not run)")
        for line in missing[:30]:
            print(f"[BLOCK] DOCUMENTED_COMMAND_MISSING {line}")
        documented_failed = status.startswith("FAIL")
        # ADV-057/HE: a reminder only (no scan, no verdict, no effect on the exit status): a generated surface that a change makes stale is
        # refused later, at the exact tree, by the freshness check; naming it here moves that discovery before the queue.
        print("REMINDER (not run here, no verdict): derived surfaces are not checked by this pre-check; before the queue run "
              "`python3 framework/scripts/candidate_tree_freshness.py --paths <the files you changed>`.")
        if any(str(rel).endswith("fulltext_read_receipts.jsonl") for rel in (ONLY_PATHS or ())):
            # 2026-11-19 (ADV, twice in a day): a receipts landing leaves coverage_report.md and reading_state.md behind the ledger, and CI fails test_coverage_report and test_reading_state.
            print("REMINDER (receipts ledger in this change): coverage_report.md, reading_state.md and batch_queue.md are derived from it; regenerate both on the tip before the queue "
                  "(the freshness command above prints the exact lines), or land with `safe_push.py ... --serialize --regenerate-derived`, which regenerates what is stale under the landing lock; then run `python3 framework/scripts/test_coverage_report.py` and `python3 framework/scripts/test_reading_state.py`.")
    for finding in findings:
        print(
            f"[{finding.severity}] {finding.code} "
            f"{finding.path}:{finding.line} — {finding.message}"
        )
    return 2 if blocks or documented_failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
