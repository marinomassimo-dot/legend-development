#!/usr/bin/env python3
"""Which readings contradicted a locator that was already persisted, and were they audited.

WHY THIS EXISTS
---------------
The 2026-09-09 sweep produced six near-errors that were one step from landing, and the
machines caught none of them (`2026-09-09_actor_retrospective.md` § 5.2). The one this
script is named after was caught by nobody but the reader: working from a 667 px
rendering, an actor began drafting a correction to an existing locator that was exactly
right, and stopped only because it re-opened the figure at 400 dpi before writing rather
than after. It touched no `consolidated baseline` claim, so the blind-audit floor never
fired.

Annex C.1 and `legend-locator-audit` now put that act at R4: contradicting, correcting or
replacing a persisted `verbatim_locator` requires a blind audit of the contradicted
triples, whatever the claim status. This script measures compliance. It reports a RATIO
and never blocks — the population is small (3 occurrences in eleven waves) and a gate that
fires on everything is a gate that gets switched off.

WHAT IS SCREENED, AND WHAT CANNOT BE
------------------------------------
§ 9.1 proposed detecting the act by grepping locator prose for correction language. That
was measured here before being implemented and it does not work: the naive pattern
`correct|contradic|replac|supersed|withdraw|revis` matches 11 of 38 locator entries on
PMID 29724996 and 12 of 41 on PMID 18674750 — papers whose readings contradicted at most
one prior locator each. Scientific prose is full of corrected genotypes, replaced media
and revised estimates. A detector with that false-positive rate reports a number nobody
will read, which is the failure mode this repository has already paid for twice.

So the authoritative signal is STRUCTURAL: a locator entry that contradicts a persisted
one declares

    "contradicts_locator": {
        "manifest": "<repo-relative path to the manifest holding the prior locator>",
        "entry": <int index>,                 # or "receipt": "<FTR-...>"
        "what_changed": "<one sentence>",
        "audit": {"auditors": <int>, "verdicts": ["CONFIRMED"|"OVERSHOOT"|...]}
    }

and the prose detector survives only in a deliberately NARROW form, as a review queue for
readings that predate the field: a correction verb that co-occurs with a reference to a
prior reading (an ISO date, an `entries[n]` pointer, or an explicit "prior/earlier/
existing locator"). Narrow-prose hits are reported as UNDECLARED_CANDIDATE — a prompt to
look, never a finding.

Every verdict says what it screened. A run over zero manifests is INSUFFICIENT_DATA, not
a clean bill: the shape `screen_verdict.py` makes unrepresentable is the same shape that
produced this sweep's worst near-error, and a measurement tool is not exempt from it.

    python3 framework/scripts/locator_contradiction_audit.py [--json] [--queue]
    python3 framework/scripts/locator_contradiction_audit.py --history [--include-same-day]
    python3 framework/scripts/locator_contradiction_audit.py --working-tree [--fail-on-undeclared]
    python3 framework/scripts/locator_contradiction_audit.py --self-test

THE SILENT REVERSAL (Mirror REV-EXPOST-20260911-001 F2, task MF-3b)
--------------------------------------------------------------------
A reader who overwrites a persisted locator IN PLACE and declares nothing meets no structural
signal at all: the entry has no `contradicts_locator`, its prose has no correction verb, and
the strict validator sees one well-formed manifest. That shape is only visible as a DIFF, so
two modes read history instead of the file:

  --history       for every manifest, every pair of consecutive committed revisions: an entry
                  whose `snippet` or `proposition` changed at the same index, with no
                  `contradicts_locator` object on the new revision, is an UNDECLARED_REVISION.
                  Measured by this mode on its first run over the corpus (2026-09-11, 81
                  manifests): 240 field changes over 125 revision pairs, of which 187 were
                  same-day edits inside the wave that wrote the entry — refinement, not
                  contradiction — and 53 crossed a commit date, i.e. touched a reading that
                  had already closed; 0 were declared, the field being younger than all of
                  them. The default therefore reports the cross-date set and counts the
                  same-day set; `--include-same-day` lists both.
  --working-tree  the same comparison between HEAD and the uncommitted file — the pre-landing
                  check a reader runs at M3 before committing an edit to an existing manifest.
                  `--fail-on-undeclared` exits 1 on any undeclared change, which is how the
                  Fig 6A near-error's shape is refused before it lands rather than queued after.

Neither mode judges: a changed snippet may be a re-anchoring to a fresh extraction, and only a
reader can say. What they establish is that the change HAPPENED and was or was not declared.

Exit codes:
  0  the corpus was screened and the ratio reported (findings do NOT change this)
  1  --fail-on-undeclared and an undeclared working-tree revision exists
  2  invalid invocation
  3  nothing could be screened - the result is void, not clean
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST_DIR = ROOT / "disease-models" / "wwox" / "research" / "deepdive_manifests"

# The measured-useless pattern, kept executable so the claim above stays checkable and so
# nobody re-proposes it from the retrospective's text.
NAIVE_PROSE = re.compile(r"correct|contradic|replac|supersed|withdraw|revis", re.I)

CORRECTION_VERB = re.compile(
    r"\b(correct(?:ed|ion|s)?|contradict(?:s|ed|ing)?|replac(?:es|ed|ing)|"
    r"supersed(?:es|ed|ing)|withdraw(?:n|s)?|revis(?:ed|es|ing))\b",
    re.I,
)
# What turns a correction verb into a claim ABOUT A PRIOR LOCATOR rather than about the
# science: a date, a locator pointer, or the words a reader uses for an earlier reading.
PRIOR_REFERENCE = re.compile(
    r"(20\d{2}-\d{2}-\d{2}|\b20\d{2}\b\s+reading|entries\[\d+\]|FTR-\d{8}-|"
    r"(prior|earlier|existing|previous|persisted)\s+(locator|reading|entry|receipt))",
    re.I,
)
PROXIMITY = 160  # characters between the verb and the reference, measured per field

# Evidence that a blind audit actually happened. Three states, not a boolean: the first
# corpus run of this tool reported the ONE contradiction known to have been audited
# (PMID 34268881 entries[14]) as unaudited, because its audit is recorded in the anchor
# prose - "Wording corrected after blind locator audit 2026-09-09 (verdict OVERSHOOT on
# 'untested')" - and the detector only looked at field NAMES. The tool was wrong and the
# record was right, which is the direction this repository requires: fix the instrument.
AUDIT_WORD = re.compile(r"\baudit(?:ed|or|ors|_status|_note)?\b", re.I)
AUDIT_VERDICT = re.compile(
    r"\b(CONFIRMED|OVERSHOOT|UNDERSHOOT|NOT_IN_SOURCE|UNVERIFIABLE_SURFACE|"
    r"blind locator audit|blind audit)\b", re.I,
)


@dataclass
class Finding:
    manifest: str
    entry: int
    kind: str          # DECLARED_CONTRADICTION | UNDECLARED_CANDIDATE
    audit_evidence: str  # STRUCTURED | PROSE | NONE
    detail: str

    @property
    def audited(self) -> bool:
        return self.audit_evidence != "NONE"


@dataclass
class Result:
    verdict: str
    screened_manifests: int = 0
    screened_entries: int = 0
    screened_bytes: int = 0
    digest: str = ""
    findings: list[Finding] = field(default_factory=list)
    naive_prose_hits: int = 0
    missing: str = ""

    @property
    def declared(self) -> list[Finding]:
        return [f for f in self.findings if f.kind == "DECLARED_CONTRADICTION"]

    @property
    def audited(self) -> list[Finding]:
        return [f for f in self.declared if f.audited]

    @property
    def candidates(self) -> list[Finding]:
        return [f for f in self.findings if f.kind == "UNDECLARED_CANDIDATE"]

    @property
    def malformed(self) -> list[Finding]:
        return [f for f in self.findings if f.kind == "MALFORMED_DECLARATION"]


def _entry_audit_evidence(entry: dict, manifest: dict) -> str:
    """STRUCTURED | PROSE | NONE - what evidence exists that an audit was run.

    Tightened after Mirror REV-EXPOST-20260911-001 F2, which showed the first version counting
    ANY key containing "audit" - `audit_status: "NOT AUDITED - pending"`, a manifest-level
    `figure_audit_table: "see dossier"` - as STRUCTURED evidence, so the compliance ratio read
    100 % the moment anyone declared. Now: STRUCTURED is a `contradicts_locator.audit` object
    carrying an auditor count or a verdict list, or an entry-level `audit_status` that names an
    audit AND a date AND does not negate itself. Manifest-level keys never count: an audit of one
    triple is not an audit of the contradiction in another. PROSE is a real state and not a
    courtesy: an audit recorded only in an anchor sentence happened.
    """
    negated = re.compile(r"\b(NOT|UN|pending|planned|awaiting|todo)\b", re.I)
    dated = re.compile(r"20\d{2}-\d{2}-\d{2}")
    declared = entry.get("contradicts_locator")
    if isinstance(declared, dict):
        audit = declared.get("audit")
        if isinstance(audit, dict) and (
            isinstance(audit.get("auditors"), int) and audit["auditors"] > 0
            or isinstance(audit.get("verdicts"), list) and audit["verdicts"]
        ):
            return "STRUCTURED"
    status = entry.get("audit_status")
    if isinstance(status, str) and AUDIT_WORD.search(status) and dated.search(status) \
            and not negated.search(status):
        return "STRUCTURED"
    for key in ("anchor", "proposition", "snippet"):
        text = entry.get(key)
        if isinstance(text, str) and AUDIT_WORD.search(text) and AUDIT_VERDICT.search(text) \
                and not negated.search(text[:80]):
            return "PROSE"
    return "NONE"


def _narrow_prose_hit(entry: dict) -> str:
    """A correction verb near a reference to a PRIOR reading, field by field.

    Per field, not over the whole serialised entry: proximity across a JSON boundary is
    not proximity, and joining the fields is how a detector acquires its false positives.
    """
    for key in ("anchor", "audit_status", "proposition", "snippet"):
        text = entry.get(key)
        if not isinstance(text, str):
            continue
        for verb in CORRECTION_VERB.finditer(text):
            window = text[max(0, verb.start() - PROXIMITY): verb.end() + PROXIMITY]
            reference = PRIOR_REFERENCE.search(window)
            if reference:
                return f"{key}: …{window.strip()[:200]}…"
    return ""


def screen(manifest_dir: Path = MANIFEST_DIR) -> Result:
    paths = sorted(manifest_dir.glob("*.json")) if manifest_dir.is_dir() else []
    if not paths:
        return Result(
            verdict="INSUFFICIENT_DATA",
            missing=f"no manifest JSON under {manifest_dir}",
        )

    digest = hashlib.sha256()
    result = Result(verdict="SCREENED")
    for path in paths:
        raw = path.read_bytes()
        digest.update(raw)
        result.screened_bytes += len(raw)
        try:
            manifest = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            result.findings.append(
                Finding(path.name, -1, "UNREADABLE", "NONE", f"{type(exc).__name__}: {exc}")
            )
            continue
        result.screened_manifests += 1
        entries = (manifest.get("verbatim_locators") or {}).get("entries") or []
        for index, entry in enumerate(entries):
            if not isinstance(entry, dict):
                continue
            result.screened_entries += 1
            if NAIVE_PROSE.search(json.dumps(entry, ensure_ascii=False)):
                result.naive_prose_hits += 1
            declared = entry.get("contradicts_locator")
            if declared is not None and not isinstance(declared, dict):
                result.findings.append(Finding(
                    path.name, index, "MALFORMED_DECLARATION", "NONE",
                    f"contradicts_locator must be an object, got {type(declared).__name__}"))
                continue
            if isinstance(declared, dict):
                result.findings.append(Finding(
                    path.name, index, "DECLARED_CONTRADICTION",
                    _entry_audit_evidence(entry, manifest),
                    str(declared.get("what_changed", ""))[:200],
                ))
                continue
            hit = _narrow_prose_hit(entry)
            if hit:
                result.findings.append(Finding(
                    path.name, index, "UNDECLARED_CANDIDATE",
                    _entry_audit_evidence(entry, manifest), hit,
                ))
    result.digest = digest.hexdigest()
    return result


# --- history: the diff the file cannot show ---------------------------------------------

REVISION_FIELDS = ("snippet", "proposition")


@dataclass
class Revision:
    manifest: str
    entry: int
    field: str
    commit: str        # short sha, or WORKING_TREE
    date: str          # commit date of the new revision, or WORKING_TREE
    prior_date: str
    cross_date: bool
    declared: bool
    before: str
    after: str

    @property
    def kind(self) -> str:
        return "DECLARED_REVISION" if self.declared else "UNDECLARED_REVISION"


@dataclass
class HistoryResult:
    verdict: str
    manifests: int = 0
    revision_pairs: int = 0
    revisions: list[Revision] = field(default_factory=list)
    missing: str = ""

    def undeclared(self, include_same_day: bool) -> list[Revision]:
        return [r for r in self.revisions
                if not r.declared and (include_same_day or r.cross_date)]

    @property
    def same_day_undeclared(self) -> int:
        return sum(1 for r in self.revisions if not r.declared and not r.cross_date)


def _git(root: Path, *args: str) -> str | None:
    try:
        done = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
    except OSError:
        return None
    return done.stdout if done.returncode == 0 else None


def _entries_of(raw: str) -> list | None:
    try:
        manifest = json.loads(raw)
    except ValueError:
        return None
    if not isinstance(manifest, dict):
        return None
    return (manifest.get("verbatim_locators") or {}).get("entries") or []


def _compare(before: list, after: list, *, manifest: str, commit: str, date: str,
             prior_date: str) -> list[Revision]:
    found: list[Revision] = []
    for index, (old, new) in enumerate(zip(before, after)):
        if not (isinstance(old, dict) and isinstance(new, dict)):
            continue
        for key in REVISION_FIELDS:
            if old.get(key) is None or old.get(key) == new.get(key):
                continue
            found.append(Revision(
                manifest=manifest, entry=index, field=key, commit=commit, date=date,
                prior_date=prior_date,
                cross_date=(date != prior_date),
                declared=isinstance(new.get("contradicts_locator"), dict),
                before=str(old.get(key))[:160], after=str(new.get(key))[:160]))
    return found


def _toplevel(root: Path) -> Path | None:
    top = _git(root, "rev-parse", "--show-toplevel")
    return Path(top.strip()).resolve() if top else None


def _repo_relative(top: Path, path: Path) -> str | None:
    # Every git call below runs with -C <toplevel>, so a pathspec relative to the toplevel is
    # right for `log`, `show` and `status` alike. The first version ran from the manifest
    # directory with a toplevel-relative pathspec: `log` found nothing and the mode reported
    # manifests=0 as SCREENED — the exact void-as-clean shape this file exists to refuse.
    try:
        return str(path.resolve().relative_to(top)).replace("\\", "/")
    except ValueError:
        return None


def screen_history(manifest_dir: Path = MANIFEST_DIR, root: Path | None = None) -> HistoryResult:
    """Every consecutive pair of committed revisions of every manifest, compared by entry index."""
    root = root or manifest_dir
    paths = sorted(manifest_dir.glob("*.json")) if manifest_dir.is_dir() else []
    if not paths:
        return HistoryResult("INSUFFICIENT_DATA", missing=f"no manifest JSON under {manifest_dir}")
    top = _toplevel(root)
    if top is None:
        return HistoryResult("INSUFFICIENT_DATA",
                             missing=f"{root} is not inside a git repository; history is unreadable")
    result = HistoryResult("SCREENED")
    for path in paths:
        rel = _repo_relative(top, path)
        if rel is None:
            continue
        log = _git(top, "log", "--format=%H|%ad", "--date=short", "--", rel) or ""
        revisions = [line.split("|", 1) for line in log.splitlines() if "|" in line][::-1]
        if not revisions:
            continue
        result.manifests += 1
        prior: tuple[list, str] | None = None
        for sha, date in revisions:
            raw = _git(top, "show", f"{sha}:{rel}")
            entries = _entries_of(raw) if raw is not None else None
            if entries is None:
                prior = None
                continue
            if prior is not None:
                result.revision_pairs += 1
                result.revisions.extend(_compare(
                    prior[0], entries, manifest=path.name, commit=sha[:7], date=date,
                    prior_date=prior[1]))
            prior = (entries, date)
    if result.manifests == 0:
        return HistoryResult("INSUFFICIENT_DATA", missing=f"none of {len(paths)} manifest(s) has a "
                             f"committed revision under {top}; there is no history to compare")
    return result


def screen_working_tree(manifest_dir: Path = MANIFEST_DIR, root: Path | None = None) -> HistoryResult:
    """HEAD against the uncommitted file, for every manifest the working tree has modified."""
    root = root or manifest_dir
    paths = sorted(manifest_dir.glob("*.json")) if manifest_dir.is_dir() else []
    if not paths:
        return HistoryResult("INSUFFICIENT_DATA", missing=f"no manifest JSON under {manifest_dir}")
    top = _toplevel(root)
    if top is None:
        return HistoryResult("INSUFFICIENT_DATA",
                             missing=f"{root} is not inside a git repository; HEAD is unreadable")
    result = HistoryResult("SCREENED")
    for path in paths:
        rel = _repo_relative(top, path)
        if rel is None:
            continue
        result.manifests += 1
        head = _git(top, "show", f"HEAD:{rel}")
        if head is None:
            continue  # untracked: nothing persisted to contradict
        before = _entries_of(head)
        try:
            after = _entries_of(path.read_text(encoding="utf-8"))
        except OSError:
            after = None
        if before is None or after is None:
            continue
        result.revision_pairs += 1
        head_date = (_git(top, "log", "-1", "--format=%ad", "--date=short", "--", rel) or "").strip()
        result.revisions.extend(_compare(
            before, after, manifest=path.name, commit="WORKING_TREE", date="WORKING_TREE",
            prior_date=head_date or "HEAD"))
    return result


def render_history(result: HistoryResult, include_same_day: bool, mode: str) -> str:
    if result.verdict == "INSUFFICIENT_DATA":
        return f"INSUFFICIENT_DATA: {result.missing}"
    listed = result.undeclared(include_same_day)
    declared = [r for r in result.revisions if r.declared]
    lines = [f"screened ({mode}): manifests={result.manifests} revision_pairs={result.revision_pairs} "
             f"entry_field_changes={len(result.revisions)}",
             f"declared revisions: {len(declared)} · undeclared, crossing a commit date: "
             f"{sum(1 for r in result.revisions if not r.declared and r.cross_date)} · "
             f"undeclared, same day as the prior revision: {result.same_day_undeclared}"
             + ("" if include_same_day else " (counted, not listed; --include-same-day)")]
    for r in listed:
        lines.append(f"  [{r.kind}] {r.manifest} entries[{r.entry}].{r.field} @ {r.commit} "
                     f"({r.prior_date} -> {r.date})")
        lines.append(f"      before: {r.before[:110]}")
        lines.append(f"      after : {r.after[:110]}")
    if mode == "working-tree" and not listed:
        lines.append("  no undeclared locator revision in the working tree")
    return "\n".join(lines)


def render(result: Result, queue: bool) -> str:
    if result.verdict == "INSUFFICIENT_DATA":
        return f"INSUFFICIENT_DATA: {result.missing}"
    lines = [
        f"screened: manifests={result.screened_manifests} "
        f"locator_entries={result.screened_entries} bytes={result.screened_bytes} "
        f"digest={result.digest[:16]}",
    ]
    declared, audited = result.declared, result.audited
    lines.append(f"declared contradictions audited: {len(audited)}/{len(declared)}")
    if result.malformed:
        lines.append(f"MALFORMED declarations (a string where an object is required): "
                     f"{len(result.malformed)}")
    candidates = result.candidates
    with_audit = [f for f in candidates if f.audited]
    lines.append(
        f"undeclared candidates (review queue): {len(candidates)}, "
        f"of which carry audit evidence: {len(with_audit)} "
        f"(structured {sum(1 for f in candidates if f.audit_evidence == 'STRUCTURED')}, "
        f"prose {sum(1 for f in candidates if f.audit_evidence == 'PROSE')})"
    )
    lines.append(
        f"naive-prose comparator (measured useless, not a finding): "
        f"{result.naive_prose_hits} of {result.screened_entries} entries"
    )
    if queue:
        for finding in result.findings:
            if finding.kind == "UNREADABLE" or not finding.audited or finding.kind == "UNDECLARED_CANDIDATE":
                flag = f"AUDIT:{finding.audit_evidence}"
                lines.append(
                    f"  [{finding.kind}/{flag}] {finding.manifest} entries[{finding.entry}] "
                    f"{finding.detail}"
                )
    return "\n".join(lines)


def self_test() -> int:
    """Calls `screen`, this module's entry point, on fixtures AND on the real corpus.

    A self-test that never calls its own entry point is not a self-test: on 2026-09-09 a
    tool reported 12/12 green while crashing corpus-wide, because its cases exercised two
    helpers and never the function that ran in production.
    """
    import tempfile

    passed, failed = 0, 0

    def check(name: str, condition: bool) -> None:
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"  ok   {name}")
        else:
            failed += 1
            print(f"  FAIL {name}")

    with tempfile.TemporaryDirectory() as tmp:
        directory = Path(tmp)
        check("empty corpus is INSUFFICIENT_DATA, not clean",
              screen(directory).verdict == "INSUFFICIENT_DATA")

        (directory / "PMID1.json").write_text(json.dumps({
            "pmid": "1",
            "verbatim_locators": {"entries": [
                {"proposition": "p", "anchor": "Figure 1",
                 "contradicts_locator": {"manifest": "PMID2.json", "entry": 3,
                                         "what_changed": "counts", "audit": {"auditors": 2}}},
                {"proposition": "q", "anchor": "Figure 2",
                 "contradicts_locator": {"manifest": "PMID2.json", "entry": 4,
                                         "what_changed": "sign"}},
            ]},
        }), encoding="utf-8")
        result = screen(directory)
        check("a declared contradiction with an audit counts as audited",
              len(result.declared) == 2 and len(result.audited) == 1)
        check("the audit evidence is STRUCTURED when it is a field",
              result.declared[0].audit_evidence == "STRUCTURED"
              and result.declared[1].audit_evidence == "NONE")
        check("the screen reports the digest of what it screened",
              len(result.digest) == 64 and result.screened_entries == 2)

        (directory / "PMID3.json").write_text(json.dumps({
            "pmid": "3",
            "verbatim_locators": {"entries": [
                {"proposition": "the authors corrected the medium to DMEM",
                 "anchor": "Methods"},
                {"proposition": "value restated",
                 "anchor": "Figure 4. Wording corrected after blind locator audit 2026-09-09."},
            ]},
        }), encoding="utf-8")
        result = screen(directory)
        candidates = [f for f in result.candidates if f.manifest == "PMID3.json"]
        check("a correction verb with no reference to a prior reading is NOT a candidate",
              all(f.entry != 0 for f in candidates))
        check("a correction verb next to a date IS a candidate",
              any(f.entry == 1 for f in candidates))
        check("an audit recorded only in prose is PROSE, not NONE",
              any(f.entry == 1 and f.audit_evidence == "PROSE" for f in candidates))

    live = screen()
    check("the entry point runs against the real corpus",
          live.verdict == "SCREENED" and live.screened_manifests > 0)
    check("the naive comparator is measurably worse than the narrow detector",
          live.naive_prose_hits > len(live.candidates) + len(live.declared))

    print(f"\nself-test: {passed} passed, {failed} failed")
    return 0 if failed == 0 else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--queue", action="store_true", help="list the review queue")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--manifest-dir", type=Path, default=MANIFEST_DIR)
    parser.add_argument("--history", action="store_true",
                        help="compare every pair of committed revisions of every manifest")
    parser.add_argument("--working-tree", action="store_true",
                        help="compare HEAD against the uncommitted manifests (run before committing)")
    parser.add_argument("--include-same-day", action="store_true",
                        help="also list undeclared revisions made the same day as the prior one")
    parser.add_argument("--fail-on-undeclared", action="store_true",
                        help="with --working-tree: exit 1 on any undeclared revision")
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

    if args.history or args.working_tree:
        if args.history and args.working_tree:
            parser.error("--history and --working-tree are separate questions; ask one")
        mode = "history" if args.history else "working-tree"
        hist = screen_history(args.manifest_dir) if args.history else screen_working_tree(args.manifest_dir)
        # In the working tree the same-day distinction is meaningless: the edit is now.
        include = args.include_same_day or args.working_tree
        undeclared = hist.undeclared(include)
        if args.json:
            print(json.dumps({
                "verdict": hist.verdict, "mode": mode,
                "screened": {"manifests": hist.manifests, "revision_pairs": hist.revision_pairs},
                "entry_field_changes": len(hist.revisions),
                "declared": sum(1 for r in hist.revisions if r.declared),
                "undeclared_listed": len(undeclared),
                "undeclared_same_day": hist.same_day_undeclared,
                "missing": hist.missing,
                "revisions": [dict(vars(r), kind=r.kind) for r in (undeclared if not include
                                                                 else hist.revisions)],
            }, indent=1))
        else:
            print(render_history(hist, include, mode))
        if hist.verdict == "INSUFFICIENT_DATA":
            return 3
        if args.fail_on_undeclared and undeclared:
            return 1
        return 0

    result = screen(args.manifest_dir)
    if args.json:
        print(json.dumps({
            "verdict": result.verdict,
            "screened": {"manifests": result.screened_manifests,
                         "locator_entries": result.screened_entries,
                         "bytes": result.screened_bytes,
                         "digest": result.digest},
            "declared_contradictions": len(result.declared),
            "declared_contradictions_audited": len(result.audited),
            "malformed_declarations": len(result.malformed),
            "undeclared_candidates": len(result.candidates),
            "undeclared_candidates_with_audit_evidence":
                sum(1 for f in result.candidates if f.audited),
            "naive_prose_comparator": result.naive_prose_hits,
            "missing": result.missing,
            "findings": [vars(f) for f in result.findings],
        }, indent=1))
    else:
        print(render(result, args.queue))
    return 3 if result.verdict == "INSUFFICIENT_DATA" else 0


if __name__ == "__main__":
    sys.exit(main())
