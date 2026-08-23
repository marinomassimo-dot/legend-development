#!/usr/bin/env python3
"""DISCOVERY — enumerate LEGEND artifacts, classify them, and report. Nothing else.

It reads, it reports, it changes nothing and it gates nothing. Exit status is 0 whether
findings exist or not: discovery reports, it does not judge. That is what makes it safe to
build while eight governance proposals remain undecided — nothing it does depends on how any
of them is resolved.

**Every rule below is a defect this repository actually produced**, on 2026-08-23, across
three seats. They are listed with the failure they prevent because a later reader will be
tempted to simplify exactly these:

1.  **The class list is PARSED from the convention, never restated here.**
    `framework/protocols/legend_operating_convention_v1.md` section B.1.2 is the single
    source. If the prose stops parsing this fails loudly rather than using a stale copy —
    the discipline `governance_fingerprint.py` and `candidate_content_hash.py` already use.
    `test_record_conventions.py` exists because five modules once held five private copies of
    one definition and the shortest was wrong: 168 records went uncounted and one registry
    record silently absorbed 168 stub bodies.

2.  **Two emission forms, always.** A field is written either `NAME: value` or column-aligned
    `NAME␣␣␣value` with no colon at all. A colon-only parser reports 6 of 14 review
    declarations and 3 of 9 manifest declarations as ABSENT — confidently, and wrongly. Three
    seats spent an afternoon rediscovering this on one field.

3.  **The population is enumerated BEFORE any pattern runs**, by an instrument that cannot
    express the property being hunted (`git ls-files`, `git ls-tree`). A count whose
    denominator is "whatever my pattern matched" is not a measurement. Two seats produced
    `0 of 39`, `8`, and `14` for one field this way; the numbers only became comparable once
    the 39 came from `ls-tree` first.

4.  **Tracked-on-ref and present-in-working-tree are different populations**, and the report
    always says which it swept. Measured on one HEAD: a clean `git archive` extraction passes
    the publication gate at 0 blocks while the working tree at the same HEAD blocks with 3,
    because `git archive` cannot see an untracked file by construction.

5.  **Domain comes from the P5.1 prefix match, never from what the artifact says about
    itself.** The roots are parsed from `governance/plan_defined_parameters.md`. Where an
    artifact's own transcription disagrees, the prefix wins and the disagreement is a finding.

6.  **Every count carries its command, the instant it ran, and its figure class.**
    Population-derived figures decay as branches are created; object-derived figures do not.
    A reader who gets a different number must be able to tell which happened.

7.  **Timestamps come from the raw epoch.** `stat -f '%Sm'` renders local time under whatever
    format string wraps it, so a hardcoded `Z` is a forgery.

8.  **Frozen clauses are cited by file and line, never by section number.** This appendix's
    own sections once collided with frozen Annex D on five tokens.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

CONVENTION = "framework/protocols/legend_operating_convention_v1.md"
DOMAIN_SOURCE = "governance/plan_defined_parameters.md"

# The heading that opens the parsed table. Matched on its number and its text, so a renamed
# section fails loudly instead of silently matching a different table.
CLASS_TABLE_HEADING = re.compile(r"^#{2,4}\s*B\.1\.2\s*[·.]\s*The classes that exist", re.M)
ROOTS_BLOCK = re.compile(r"CONTROL_PLANE_ROOTS:\s*\n((?:\s*-\s*\S+\s*\n)+)")

FRONTMATTER_FIELDS = ("record_type", "author", "session_ref", "status", "state")
# Fields read wherever they appear in the file, not only in frontmatter — see rule 2.
ANYWHERE_FIELDS = ("MIRROR_REVIEW",)


class ConventionParseError(RuntimeError):
    """The convention did not parse. Never fall back to a hardcoded copy — rule 1."""


def utc_now() -> str:
    """Instant stamp from the raw epoch. Rule 7."""
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time()))


def git(*args: str, cwd: Path | None = None) -> str:
    proc = subprocess.run(
        ("git", *args), cwd=str(cwd or ROOT),
        capture_output=True, text=True, check=False,
    )
    if proc.returncode != 0:
        return ""
    return proc.stdout


# ---------------------------------------------------------------- the parsed convention

@dataclass(frozen=True)
class ArtifactClass:
    name: str
    id_prefixes: tuple[str, ...]
    path_anchor: str | None      # literal directory prefix, or None when the row declares none
    path_declared: str           # the cell verbatim, so an unanchored row is visible not dropped
    domain_declared: str
    writer: str


def _cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _literal_prefix(path_cell: str) -> str | None:
    """The leading literal directory of a path template, or None.

    `governance/decisions/DEC-<YYYYMMDD>-<SLUG>.md` -> `governance/decisions/`
    `reviews/<ACTOR_ID>/REV-…`                      -> `reviews/`
    `author's own working root`                     -> None  (declared, unanchored, reported)
    """
    text = path_cell.replace("`", "").strip()
    if not text or "/" not in text:
        return None
    head = re.split(r"[<…]", text)[0]
    if "/" not in head:
        return None
    prefix = head[: head.rindex("/") + 1]
    return prefix if re.fullmatch(r"[A-Za-z0-9._/-]+/", prefix) else None


def parse_classes(convention_text: str) -> list[ArtifactClass]:
    """Rule 1: the class list lives in the convention. This function reads it there."""
    match = CLASS_TABLE_HEADING.search(convention_text)
    if not match:
        raise ConventionParseError(
            f"{CONVENTION}: section B.1.2 heading not found. The class list is parsed, never "
            "restated here — repair the heading rather than hardcoding the table."
        )
    lines = convention_text[match.end():].splitlines()
    header: list[str] | None = None
    classes: list[ArtifactClass] = []
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            if header is not None and classes:
                break
            continue
        cells = _cells(line)
        if header is None:
            header = [c.lower() for c in cells]
            continue
        if set("".join(cells)) <= set("-: "):        # the |---|---| separator
            continue
        if not cells or not cells[0].strip():        # a continuation row, not a class
            continue

        def col(*names: str) -> str:
            for name in names:
                for index, head in enumerate(header or []):
                    if name in head and index < len(cells):
                        return cells[index]
            return ""

        raw_name = col("class")
        name = re.sub(r"[*`]", "", raw_name).strip()
        if not name:
            continue
        ids = tuple(
            token for token in re.findall(r"`([A-Z][A-Z-]*-)`", col("id"))
        )
        path_cell = col("canonical path", "path")
        classes.append(ArtifactClass(
            name=name,
            id_prefixes=ids,
            path_anchor=_literal_prefix(path_cell),
            path_declared=re.sub(r"\s+", " ", path_cell)[:80],
            domain_declared=re.sub(r"[*`🔴]", "", col("domain")).strip(),
            writer=re.sub(r"[*`🔴]", "", col("writer")).strip(),
        ))
    if not classes:
        raise ConventionParseError(
            f"{CONVENTION}: section B.1.2 parsed to zero classes. Failing loudly rather than "
            "proceeding with an empty definition."
        )
    return classes


def parse_control_plane_roots(text: str) -> tuple[str, ...]:
    """Rule 5: the roots are P5.1's, parsed from the file that declares them."""
    match = ROOTS_BLOCK.search(text)
    if not match:
        raise ConventionParseError(
            f"{DOMAIN_SOURCE}: CONTROL_PLANE_ROOTS block not found. Domain is derived from the "
            "declared roots, never assumed."
        )
    roots = tuple(
        line.strip().lstrip("-").strip()
        for line in match.group(1).splitlines() if line.strip()
    )
    return tuple(r for r in roots if r)


# ---------------------------------------------------------------- field extraction

def field_patterns(name: str) -> tuple[re.Pattern[str], re.Pattern[str]]:
    """Rule 2: a field is emitted colon-delimited OR column-aligned with no colon."""
    return (
        re.compile(rf"^[ \t]*{re.escape(name)}[ \t]*:[ \t]*(.*)$", re.M | re.I),
        re.compile(rf"^[ \t]*{re.escape(name)}[ \t]{{2,}}([^\s:].*)$", re.M),
    )


def read_field(text: str, name: str) -> tuple[str | None, str | None]:
    """Return (value, emission_form). Colon form wins when both are present."""
    colon, aligned = field_patterns(name)
    hit = colon.search(text)
    if hit:
        return hit.group(1).strip() or None, "colon"
    hit = aligned.search(text)
    if hit:
        return hit.group(1).strip() or None, "aligned"
    return None, None


# ---------------------------------------------------------------- the record

@dataclass
class Record:
    path: str
    basename: str
    class_by_id: str | None = None
    class_by_path: str | None = None
    class_agreement: str = "n/a"
    domain_by_path: str = "CONTENT"
    domain_transcribed: str | None = None
    domain_agreement: str = "not_transcribed"
    record_type: str | None = None
    author: str | None = None
    session_ref: str | None = None
    status_key: str | None = None
    status_token: str | None = None
    mirror_review: str | None = None
    mirror_review_form: str | None = None
    findings: list[str] = field(default_factory=list)


def is_path_governed(cls: ArtifactClass) -> bool:
    """Derived from the table, not asserted here.

    A class is path-governed when B.1.2 gives it BOTH a literal path anchor AND id prefixes —
    which is exactly rows 1-4. Rows 6 and 7 are explicitly *not* path-governed: their home is
    "the author's own working root", and their only placement rule is the negative one — a
    working artifact never sits inside a class directory it does not belong to. Without this
    distinction the checker reports `learning/plan/HANDOFF-*.md` as misplaced, which B.1.2
    permits, and the noise buries the six that are genuinely inside a class directory.
    """
    return bool(cls.path_anchor) and bool(cls.id_prefixes)


def classify(path: str, classes: list[ArtifactClass]) -> tuple[str | None, str | None, bool]:
    base = path.rsplit("/", 1)[-1]
    by_id = next(
        (c.name for c in classes
         if c.id_prefixes and any(base.startswith(p) for p in c.id_prefixes)),
        None,
    )
    anchored = [c for c in classes if c.path_anchor and path.startswith(c.path_anchor)]
    holder = max(anchored, key=lambda c: len(c.path_anchor or "")) if anchored else None
    return by_id, (holder.name if holder else None), bool(holder and is_path_governed(holder))


def domain_of(path: str, roots: tuple[str, ...]) -> str:
    return "CONTROL_PLANE" if any(path.startswith(r) for r in roots) else "CONTENT"


def build_record(path: str, text: str, classes: list[ArtifactClass],
                 roots: tuple[str, ...]) -> Record:
    rec = Record(path=path, basename=path.rsplit("/", 1)[-1])
    rec.class_by_id, rec.class_by_path, governed_dir = classify(path, classes)
    if rec.class_by_id and rec.class_by_path and rec.class_by_id != rec.class_by_path:
        if governed_dir:
            rec.class_agreement = "CONFLICT"
            rec.findings.append(
                f"IN_A_CLASS_DIRECTORY_IT_IS_NOT: filename says {rec.class_by_id}, "
                f"directory is {rec.class_by_path}'s and is path-governed"
            )
        else:
            # An author root, which B.1.2 permits for classes 6 and 7. Not a finding.
            rec.class_agreement = "author_root"
    elif rec.class_by_id and rec.class_by_path:
        rec.class_agreement = "agree"
    elif rec.class_by_id or rec.class_by_path:
        rec.class_agreement = "partial"

    rec.domain_by_path = domain_of(path, roots)
    transcribed, _ = read_field(text, "domain")
    if transcribed:
        rec.domain_transcribed = transcribed[:60]
        head = transcribed.upper().replace(" ", "_")
        if head.startswith(("CONTENT", "CONTROL_PLANE")):
            claimed = "CONTROL_PLANE" if head.startswith("CONTROL_PLANE") else "CONTENT"
            rec.domain_agreement = "agree" if claimed == rec.domain_by_path else "CONFLICT"
            if rec.domain_agreement == "CONFLICT":
                rec.findings.append(
                    f"DOMAIN_CONFLICT: transcribed {claimed}, P5.1 prefix match says "
                    f"{rec.domain_by_path} — the prefix wins"
                )
        else:
            rec.domain_agreement = "unparsed"

    for name in ("record_type", "author", "session_ref"):
        value, _ = read_field(text, name)
        setattr(rec, name, value[:60] if value else None)
    for key in ("status", "state"):
        value, _ = read_field(text, key)
        if value:
            rec.status_key = key
            rec.status_token = re.split(r"\s+[—-]\s+", value)[0].strip()[:48]
            break

    for name in ANYWHERE_FIELDS:
        value, form = read_field(text, name)
        if value:
            rec.mirror_review, rec.mirror_review_form = value[:70], form

    if rec.class_by_id or rec.class_by_path:
        if not rec.author:
            rec.findings.append("UNATTRIBUTED: no author declared")
        if not rec.session_ref:
            rec.findings.append("NO_SESSION_REF: authoring session not declared")
    return rec


# ---------------------------------------------------------------- population, then measurement

@dataclass
class Population:
    label: str
    command: str
    instant: str
    figure_class: str
    paths: list[str]
    untracked: set[str] = field(default_factory=set)


def enumerate_working_tree() -> Population:
    """Rule 3 and 4: the set first, by an instrument blind to the properties we hunt."""
    tracked = [p for p in git("ls-files").splitlines() if p]
    others = [p for p in git("ls-files", "--others", "--exclude-standard").splitlines() if p]
    return Population(
        label="working tree (tracked + untracked)",
        command="git ls-files ; git ls-files --others --exclude-standard",
        instant=utc_now(),
        figure_class="working-tree — NOT comparable with a ref sweep",
        paths=sorted(set(tracked) | set(others)),
        untracked=set(others),
    )


def enumerate_refs() -> Population:
    refs = [r for r in git(
        "for-each-ref", "--format=%(refname)", "refs/heads", "refs/remotes", "refs/tags"
    ).splitlines() if r]
    paths: set[str] = set()
    for ref in refs:
        paths.update(p for p in git("ls-tree", "-r", "--name-only", ref).splitlines() if p)
    return Population(
        label=f"union over {len(refs)} content refs",
        command=("git for-each-ref --format='%(refname)' refs/heads refs/remotes refs/tags"
                 " ; git ls-tree -r --name-only <each>"),
        instant=utc_now(),
        figure_class="population-derived — DECAYS as branches are created",
        paths=sorted(paths),
    )


def load(path: str, population: Population) -> str:
    if path in population.untracked or population.label.startswith("working tree"):
        target = ROOT / path
        if target.is_file():
            try:
                return target.read_text(encoding="utf-8", errors="replace")
            except OSError:
                return ""
        return ""
    return git("show", f"HEAD:{path}")


# ---------------------------------------------------------------- reporting

def render(records: list[Record], classes: list[ArtifactClass], roots: tuple[str, ...],
           population: Population) -> str:
    out: list[str] = []
    add = out.append
    add("ARTIFACT INDEX — discovery only. Reports; judges nothing; exit 0 either way.")
    add("")
    add(f"POPULATION   {population.label}")
    add(f"COMMAND      {population.command}")
    add(f"INSTANT      {population.instant}")
    add(f"FIGURE CLASS {population.figure_class}")
    add(f"ENUMERATED   {len(population.paths)} paths, before any pattern ran")
    add("")
    add(f"CLASS TABLE  parsed from {CONVENTION} section B.1.2 — {len(classes)} classes, "
        "never restated in this script")
    for cls in classes:
        anchor = cls.path_anchor or f"UNANCHORED ({cls.path_declared})"
        add(f"  {cls.name:<16} ids={','.join(cls.id_prefixes) or '—':<12} {anchor}")
    add("")
    add(f"CONTROL_PLANE_ROOTS  parsed from {DOMAIN_SOURCE}: {', '.join(roots)}")
    add("")

    classified = [r for r in records if r.class_by_id or r.class_by_path]
    add(f"CLASSIFIED   {len(classified)} of {len(records)} enumerated paths")
    add("")
    counts: dict[str, int] = {}
    for rec in classified:
        key = rec.class_by_id or rec.class_by_path or "?"
        counts[key] = counts.get(key, 0) + 1
    for name, count in sorted(counts.items()):
        spans = {domain_of(r.path, roots) for r in classified
                 if (r.class_by_id or r.class_by_path) == name}
        span = "  SPANS BOTH DOMAINS" if len(spans) > 1 else ""
        add(f"  {name:<16} {count:>4}   {'/'.join(sorted(spans))}{span}")
    add("")

    findings = [(r.path, f) for r in records for f in r.findings]
    by_type: dict[str, list[str]] = {}
    for path, finding in findings:
        by_type.setdefault(finding.split(":")[0], []).append(f"{finding}  ←  {path}")
    add(f"FINDINGS     {len(findings)} in {len(by_type)} classes — reported, gating nothing")
    for kind in sorted(by_type, key=lambda k: len(by_type[k])):
        rows = by_type[kind]
        add(f"  {kind}  ({len(rows)})")
        # Attribution findings are a migration backlog and are counted, not enumerated:
        # 0 artifacts carried session_ref before this convention, so listing them all buries
        # the placement conflicts, which are the ones a reader can act on today.
        limit = 3 if kind in {"UNATTRIBUTED", "NO_SESSION_REF"} else len(rows)
        for row in rows[:limit]:
            add(f"      {row}")
        if len(rows) > limit:
            add(f"      … {len(rows) - limit} more (--json for the full set)")
    add("")

    # Reported for whichever class actually carries the field, derived — never named here.
    # Naming the class would be the sixth private copy the parse exists to prevent, and it
    # would also hide the day the field appears somewhere new.
    carriers: dict[str, list[Record]] = {}
    for rec in classified:
        if rec.mirror_review:
            carriers.setdefault(rec.class_by_id or rec.class_by_path or "?", []).append(rec)
    for holder, group in sorted(carriers.items()):
        add(f"MIRROR_REVIEW carried by class {holder} — the field a FROZEN gate reads")
        add("  vocabulary: annex_d_commit_batch.md line 38 — n/a | PASS | FAIL + REVIEW_ID")
        conforming = 0
        for rec in sorted(group, key=lambda r: r.basename):
            ok = bool(re.fullmatch(r"(n/a|PASS|FAIL)(\s.*)?", rec.mirror_review.strip(), re.I))
            conforming += 1 if ok else 0
            form = f"[{rec.mirror_review_form}]" if rec.mirror_review_form else ""
            add(f"  {'  ' if ok else '!!'} {rec.basename:<42} {form:<10} "
                f"{rec.mirror_review[:60]}")
        add(f"  conforming: {conforming} of {len(group)}   (object-derived)")
        add("")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=("Enumerate and classify LEGEND artifacts. Reads and reports; writes "
                     "nothing; gates nothing; always exits 0."),
    )
    parser.add_argument("--all-refs", action="store_true",
                        help="sweep the union over every content ref instead of the working tree")
    parser.add_argument("--json", action="store_true", help="emit records as JSON lines")
    parser.add_argument("--convention", default=CONVENTION,
                        help="path to the convention whose section B.1.2 declares the classes")
    args = parser.parse_args()

    convention_text = (ROOT / args.convention).read_text(encoding="utf-8")
    classes = parse_classes(convention_text)
    roots = parse_control_plane_roots((ROOT / DOMAIN_SOURCE).read_text(encoding="utf-8"))

    population = enumerate_refs() if args.all_refs else enumerate_working_tree()
    records = [
        build_record(path, load(path, population), classes, roots)
        for path in population.paths if path.endswith((".md", ".jsonl", ".json"))
    ]

    if args.json:
        print(json.dumps({
            "population": population.label, "command": population.command,
            "instant": population.instant, "figure_class": population.figure_class,
            "enumerated": len(population.paths),
        }))
        for rec in records:
            if rec.class_by_id or rec.class_by_path or rec.findings:
                print(json.dumps(asdict(rec)))
    else:
        print(render(records, classes, roots, population))
    return 0


if __name__ == "__main__":
    sys.exit(main())
