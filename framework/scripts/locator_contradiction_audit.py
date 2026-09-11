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
    python3 framework/scripts/locator_contradiction_audit.py --self-test

Exit codes:
  0  the corpus was screened and the ratio reported (findings do NOT change this)
  2  invalid invocation
  3  nothing could be screened - the result is void, not clean
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
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
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

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
