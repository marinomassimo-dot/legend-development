#!/usr/bin/env python3
"""Benchmark J — can record-scoped editing replace the FULL whole-file rewrite of BATCH_COMMIT?

WHY THIS EXISTS
---------------
`.claude/skills/legend-commit/SKILL.md` step 4 propagates a batch into the four scientific
current files by *"full rewrite, unchanged sections copied verbatim"*. A full rewrite can lose
or alter text nobody meant to touch; a record-scoped editor (`record_scoped_edit.py`) cannot —
but it might be unable to express an edit a batch legitimately makes. This command measures
both sides on the repository's own history, with the rules fixed in
`framework/eval/benchmarks/BENCH-J-RECORD-SCOPED-EDIT/PREREGISTRATION.md` before any replay.

  j0  CORPUS — every non-merge commit that changed a batch-rewritten file, segmented per record
      with `registry_records.partition`, every changed hunk labelled by the pre-registered
      cascade (INTENDED · LEGITIMATE_COLLATERAL · ACCIDENTAL_COLLATERAL · VERBATIM_COPY_DRIFT ·
      FORMATTING_ONLY), residual hunks labelled by hand in `labels_spec.json`.
  j2  REPLAY — for every corpus (commit, file): derive record-scoped operations from the
      INTENDED + LEGITIMATE_COLLATERAL hunks, apply them with `record_scoped_edit.py` to the
      parent's bytes, and compare the result with the child.

🔴 Nothing here writes a registry. Every file is read from git objects (`git show REV:PATH`),
and replay happens in memory. The corpus JSON stores digests, line numbers and rule names, never
record text, so the committed fixture carries no identifier literal of its own.

    python3 framework/scripts/record_edit_bench.py j0 --repo <full-history clone> --rev <sha>
    python3 framework/scripts/record_edit_bench.py j2 --repo <full-history clone>

Exit codes: 0 done · 1 a commit could not be processed · 2 invalid invocation.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import registry_records  # noqa: E402

BENCH = ROOT / "framework/eval/benchmarks/BENCH-J-RECORD-SCOPED-EDIT"
SPEC = BENCH / "labels_spec.json"
CORPUS = BENCH / "j0_corpus.json"
J2_RESULTS = BENCH / "j2_results.json"

# The files BATCH_COMMIT rewrites — `prompt_batch_commit.md` Phase 3 (snapshot list) and Phase 4
# (4.1–4.6), restricted to those that exist in this edition. The derived surfaces of Phase 4.7
# are GENERATED, not rewritten, and are outside the corpus.
CORE = [
    "disease-models/wwox/registries/working_model_current.md",
    "disease-models/wwox/registries/claim_registry_current.md",
    "disease-models/wwox/registries/paper_registry_current.md",
    "disease-models/wwox/registries/literature_tracking_log_current.md",
]
EXTRA_GLOBS = ("disease-models/wwox/meta/", )
EXTRA = [
    "disease-models/wwox/research/research_lines_current.md",
    "disease-models/wwox/research/research_candidates_current.md",
]
# Phase 4.7's generated surfaces and the growth counter: they enumerate every record, so their
# added lines would name every id and make every record a "target". Declared, not discovered.
GENERATED = (
    "disease-models/wwox/registries/coverage_report.md",
    "disease-models/wwox/registries/batch_queue.md",
    "disease-models/wwox/registries/reading_state.md",
    "disease-models/wwox/analysis/pathograph_inventory.md",
    "disease-models/wwox/analysis/data/pathograph_export.jsonl",
    "disease-models/wwox/research/surface_census.md",
    "framework/state/growth_anchors.jsonl",
)

LABELS = ("INTENDED", "LEGITIMATE_COLLATERAL", "ACCIDENTAL_COLLATERAL",
          "VERBATIM_COPY_DRIFT", "FORMATTING_ONLY")


# ---------------------------------------------------------------- git

def git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True,
                          check=True).stdout


def git_bytes(repo: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True,
                          check=True).stdout


def show(repo: Path, rev: str, path: str) -> str | None:
    done = subprocess.run(["git", "-C", str(repo), "show", f"{rev}:{path}"], capture_output=True)
    return done.stdout.decode("utf-8") if done.returncode == 0 else None


def corpus_files(repo: Path, rev: str) -> list[str]:
    listed = git(repo, "ls-tree", "-r", "--name-only", rev, "--", *EXTRA_GLOBS).split()
    metas = sorted(p for p in listed if p.endswith("_current.md"))
    return CORE + metas + EXTRA


def stem_levels(path: str) -> tuple[int, ...]:
    stem = Path(path).stem
    return registry_records.IDENTITY_LEVELS.get(stem, (2,))


# ---------------------------------------------------------------- identifiers named by a commit

NUM_LIST = r"(\d+)((?:\s*(?:[-–/]|,|\band\b|\be\b)\s*\d+)*)"
ID_PATTERNS = [
    ("PAPER", re.compile(r"\bPAPER\s+" + NUM_LIST, re.I)),
    ("CLAIM", re.compile(r"\bCLAIMS?\s+" + NUM_LIST, re.I)),
    ("BLOCK", re.compile(r"\bBLOC(?:K|CO)\s+" + NUM_LIST, re.I)),
    ("LIT-EX", re.compile(r"\bLIT-EX-" + NUM_LIST)),
    ("LIT", re.compile(r"\bLIT-(?!EX)" + NUM_LIST)),
    ("CORPUS P", re.compile(r"\bCORPUS\s+P" + NUM_LIST)),
    ("CORPUS PMID", re.compile(r"\bCORPUS\s+PMID\s+(\d+)()")),
    ("CORPUS-STUB", re.compile(r"\bCORPUS-STUB-" + NUM_LIST)),
    ("RL", re.compile(r"\bRL-((?:[A-Z]+-)?\d+)()")),
]
PMID = re.compile(r"(?<![\d.])(\d{7,8})(?![\d.])")
DOI = re.compile(r"\b10\.\d{4,9}/[^\s\]\)|,;]+", re.I)
BATCH_ID = re.compile(r"\bBATCH_\d{8}_[A-Z0-9_]+\b")


def _expand(first: str, tail: str, family: str) -> list[str]:
    if family == "RL":
        return [first.upper()]
    out = [int(first)]
    previous = int(first)
    for sep, number in re.findall(r"\s*([-–/]|,|\band\b|\be\b)\s*(\d+)", tail):
        value = int(number)
        if sep in "-–" and value > previous and value - previous <= 60:
            out.extend(range(previous + 1, value + 1))
        else:
            out.append(value)
        previous = value
    return [str(v) for v in out]


def named_ids(text: str) -> set[tuple[str, str]]:
    found: set[tuple[str, str]] = set()
    for family, pattern in ID_PATTERNS:
        for match in pattern.finditer(text):
            for value in _expand(match.group(1), match.group(2) or "", family):
                found.add((family, value))
    return found


def heading_id(heading: str) -> set[tuple[str, str]]:
    """The id a unit heading DEFINES: the named ids at its very start, after decoration."""
    bare = registry_records.DECORATION.sub("", heading.strip())
    token = registry_records.identity_token(bare)
    if token:
        return named_ids(token)
    rl = re.match(r"RL-((?:[A-Z]+-)?\d+)\b", bare)
    return {("RL", rl.group(1).upper())} if rl else set()


def identifiers(text: str) -> set[str]:
    values = {m.group(1) for m in PMID.finditer(text)}
    values |= {m.group(0).lower().rstrip(".") for m in DOI.finditer(text)}
    return values


def record_identifiers(unit_text: str) -> set[str]:
    out: set[str] = set()
    for raw in unit_text.splitlines():
        match = re.match(r"\*\*(Identifier(?: value)?|PMID|DOI):\*\*\s*(.*)$", raw.strip(), re.I)
        if match:
            out |= identifiers(match.group(2))
    return out


# ---------------------------------------------------------------- hunk rules (PREREGISTRATION § 3)

VERSION_LINE = re.compile(
    r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:Version|Versione|Last update|Last updated|Ultimo aggiornamento|"
    r"Date baseline|Updated|Date|Status of this file|working_model_version)\b", re.I)
CHANGELOG_HEAD = re.compile(r"change-?\s?log|cronologia|storico modifiche|version history", re.I)
LINK_FIELD = re.compile(r"^\s*(?:[-*]\s*)?\*\*(?:Wikilinks|Claim links|Related|Links|"
                        r"Collegamenti)[^*]*\*\*", re.I)
WIKILINK = re.compile(r"\[\[[^\]]+\]\]")
MIRROR_ROW = re.compile(r"^\|\s*(\d{3})\s*\|")


def norm(lines: list[str]) -> str:
    return " ".join(" ".join(lines).split())


def heading_path(unit_text: str, line_index: int) -> list[str]:
    """Headings enclosing line `line_index` (0-based, unit-relative), outermost first."""
    stack: list[tuple[int, str]] = []
    fenced = False
    for number, line in enumerate(unit_text.splitlines()):
        if number > line_index:
            break
        if registry_records.FENCE.match(line):
            fenced = not fenced
            continue
        if fenced:
            continue
        match = registry_records.HEADING.match(line)
        if match:
            level = len(match.group("hashes"))
            stack = [s for s in stack if s[0] < level] + [(level, match.group("text"))]
    return [s[1] for s in stack]


def sweep_field(changed: list[str], message: str) -> bool:
    """Every changed line declares a field, all those fields share one word, and a sentence of
    the commit message applies a sweep to that word (`every … Status`, `all … Status`)."""
    names = []
    for line in changed:
        declared = registry_records.declared_fields(line, bulleted=True)
        if not declared:
            return False
        names.extend(name.lower().replace("-", " ") for name, _ in declared)
    if not names:
        return False
    shared = set.intersection(*(set(name.split()) for name in names))
    sentences = re.split(r"(?<=[.!?:])\s+|\n\s*\n", message.lower().replace("-", " "))
    return any(re.search(r"\b(?:every|all)\b", sentence) and re.search(
        r"\b" + re.escape(word) + r"\b", sentence) for word in shared for sentence in sentences)


def classify(rem: list[str], add: list[str], *, targeted: bool, path_p: list[str],
             path_c: list[str], targets: set[tuple[str, str]], batch_ids: set[str],
             structural: bool, message: str) -> tuple[str, str, str]:
    """(label, sublabel, rule) for one hunk of a unit present on both sides, or UNRESOLVED."""
    changed = [line for line in rem + add if line.strip()]
    only_seps = all(line.strip() in ("", "---") for line in rem + add)
    if only_seps:
        if not rem or all(not line.strip() for line in rem):
            return "LEGITIMATE_COLLATERAL", "separator", "R1-separator-added"
        if targeted or structural:
            return "FORMATTING_ONLY", "separator", "R1-separator-in-target"
        return "VERBATIM_COPY_DRIFT", "lost-separator", "R1-separator-removed"
    if norm(rem) == norm(add):
        if targeted or structural:
            return "FORMATTING_ONLY", "whitespace", "R2-whitespace-in-target"
        return "VERBATIM_COPY_DRIFT", "whitespace", "R2-whitespace-outside-target"
    if changed and all(VERSION_LINE.match(line) for line in changed):
        return "LEGITIMATE_COLLATERAL", "version", "R3-version-lines"
    if any(CHANGELOG_HEAD.search(h) for h in path_p + path_c):
        return "LEGITIMATE_COLLATERAL", "changelog", "R4-under-changelog-heading"
    if WIKILINK.sub("", " ".join(rem)).split() == WIKILINK.sub("", " ".join(add)).split() or (
            changed and all(LINK_FIELD.match(line) for line in changed)):
        return "LEGITIMATE_COLLATERAL", "crosslink", "R5-links-only"
    if targeted:
        return "INTENDED", "record", "R6-target-record"
    added_text = "\n".join(add)
    if batch_ids and any(b in added_text for b in batch_ids):
        return "INTENDED", "batch-tagged", "R7-names-this-batch"
    mentioned = named_ids("\n".join(rem + add))
    rows = {("CLAIM", str(int(m.group(1)))) for line in rem + add
            for m in [MIRROR_ROW.match(line)] if m}
    if (mentioned | rows) & targets:
        return "INTENDED", "mirror", "R8-names-a-target"
    if sweep_field(changed, message):
        return "INTENDED", "field-sweep", "R11-message-declares-a-field-sweep"
    return "UNRESOLVED", "", "R9-judgement"


# ---------------------------------------------------------------- j0

def unit_map(text: str, levels: tuple[int, ...]) -> list[registry_records.Block]:
    return registry_records.partition(text, levels)


def digest(*parts: Any) -> str:
    return hashlib.sha256(json.dumps(parts, ensure_ascii=False).encode()).hexdigest()[:16]


def commit_context(repo: Path, sha: str, files: list[str], parent: str = "",
                   brought: str = "", strict: bool = False) -> dict[str, Any]:
    """What a commit says it changes. For an evil merge, `parent` is the side it is replayed
    from and `brought` the other side: the messages of the commits the merge brings in count."""
    message = git(repo, "log", "-1", "--format=%B", sha)
    subject = message.splitlines()[0] if message else ""
    parent = parent or f"{sha}^"
    if brought:
        message += "\n" + git(repo, "log", "--format=%B", f"{parent}..{brought}")
    changed = git(repo, "diff-tree", "--no-commit-id", "-r", "--name-only", parent, sha).split()
    companions = [p for p in changed if p not in files and p not in GENERATED]
    added: list[str] = []
    for path in companions:
        diff = git(repo, "diff", "--no-color", "-U0", parent, sha, "--", path)
        added.extend(line[1:] for line in diff.splitlines()
                     if line.startswith("+") and not line.startswith("+++"))
    companion_text = "\n".join(added)
    if strict:      # sensitivity: what the commit's own message attributes, nothing else
        companion_text = ""
    targets = named_ids(message) | named_ids(companion_text)
    named = identifiers(message) | identifiers(companion_text)
    structural = bool(re.search(r"\bstructural\b|no scientific change|traceability repair|"
                                r"vocabulary", message, re.I))
    return {"sha": sha, "parent": parent, "subject": subject, "message": message,
            "targets": targets,
            "named_identifiers": named, "batch_ids": set(BATCH_ID.findall(subject)),
            "companions": companions, "structural": structural}


def unit_targeted(block: registry_records.Block, text: str, ctx: dict[str, Any]) -> str:
    """Why this unit is a target of the commit, or ``."""
    ids = heading_id(block.heading) if block.kind != "preamble" else set()
    if ids & ctx["targets"]:
        return "id-named"
    if block.kind == "record" and record_identifiers(text) & ctx["named_identifiers"]:
        return "identifier-named"
    return ""


def label_file(repo: Path, ctx: dict[str, Any], path: str, spec: dict[str, Any]
               ) -> dict[str, Any]:
    sha = ctx["sha"]
    before, after = show(repo, ctx["parent"], path), show(repo, sha, path)
    event: dict[str, Any] = {"commit": sha[:12], "file": path, "units_parent": 0,
                             "units_child": 0, "hunks": [], "unit_events": []}
    if before is None or after is None:
        event["file_event"] = "created" if before is None else "deleted"
        return event
    levels = stem_levels(path)
    pu, cu = unit_map(before, levels), unit_map(after, levels)
    event["units_parent"], event["units_child"] = len(pu), len(cu)
    pkeys, ckeys = [u.key for u in pu], [u.key for u in cu]
    pdup = [k for k, n in Counter(pkeys).items() if n > 1]
    cdup = [k for k, n in Counter(ckeys).items() if n > 1]
    event["duplicate_keys_parent"], event["duplicate_keys_child"] = pdup, cdup
    pby = {u.key: u for u in pu}
    cby = {u.key: u for u in cu}
    ptext = {k: before[u.start:u.end] for k, u in pby.items()}
    ctext = {k: after[u.start:u.end] for k, u in cby.items()}
    # order: keys common to both, compared by longest common subsequence
    common = [k for k in pkeys if k in cby]
    common_c = [k for k in ckeys if k in pby]
    matcher = difflib.SequenceMatcher(None, common, common_c, autojunk=False)
    in_order = {common[i] for block in matcher.get_matching_blocks()
                for i in range(block.a, block.a + block.size)}
    removed_keys = [k for k in pkeys if k not in cby]
    added_keys = [k for k in ckeys if k not in pby]
    renames = pair_renames(removed_keys, added_keys, ptext, ctext)
    for old, new in renames:
        removed_keys.remove(old)
        added_keys.remove(new)

    def emit(unit_key: str, kind: str, rem: list[str], add: list[str], p_line: int,
             c_line: int, label: str, sub: str, rule: str, why: str, path_c: list[str]) -> None:
        key = digest(sha[:12], path, unit_key, rem, add)
        record = {"id": key, "unit": unit_key, "unit_kind": kind, "parent_line": p_line,
                  "child_line": c_line, "removed": len(rem), "added": len(add),
                  "heading_path": path_c[-2:], "label": label, "sublabel": sub,
                  "rule": rule, "target_reason": why, "_add": add}
        event["hunks"].append(record)

    # modified units (same key, or renamed pair)
    pairs = [(k, k) for k in pkeys if k in cby] + renames
    for old, new in pairs:
        a_text, b_text = ptext[old], ctext[new]
        pu_block, cu_block = pby[old], cby[new]
        why = unit_targeted(pu_block, a_text, ctx) or unit_targeted(cu_block, b_text, ctx)
        kind = pu_block.kind
        if old != new:
            event["unit_events"].append({"event": "renamed", "from": old, "to": new,
                                         "target_reason": why})
        if old not in in_order and old == new:
            label = "INTENDED" if why else "VERBATIM_COPY_DRIFT"
            event["unit_events"].append({"event": "moved", "unit": old, "label": label,
                                         "target_reason": why})
        if a_text == b_text:
            continue
        a_lines, b_lines = a_text.splitlines(), b_text.splitlines()
        ops = difflib.SequenceMatcher(None, a_lines, b_lines, autojunk=False).get_opcodes()
        base_p = before.count("\n", 0, pu_block.start) + 1
        base_c = after.count("\n", 0, cu_block.start) + 1
        for tag, i1, i2, j1, j2 in ops:
            if tag == "equal":
                continue
            rem, add = a_lines[i1:i2], b_lines[j1:j2]
            path_p = heading_path(a_text, max(i1 - 1, 0) if i1 == i2 else i1)
            path_c = heading_path(b_text, max(j1 - 1, 0) if j1 == j2 else j1)
            label, sub, rule = classify(
                rem, add, targeted=bool(why), path_p=path_p, path_c=path_c,
                targets=ctx["targets"], batch_ids=ctx["batch_ids"],
                structural=ctx["structural"], message=ctx["message"])
            if old != new and not why and label == "UNRESOLVED":
                label, sub, rule = "UNRESOLVED", "", "R9-judgement"
            emit(new, kind, rem, add, base_p + i1, base_c + j1, label, sub, rule, why, path_c)
    # added units
    for key in added_keys:
        block, text = cby[key], ctext[key]
        why = unit_targeted(block, text, ctx)
        lines = text.splitlines()
        if why:
            label, sub, rule = "INTENDED", "new-unit", "R6-target-record"
        elif ctx["batch_ids"] and any(b in text for b in ctx["batch_ids"]):
            label, sub, rule = "INTENDED", "new-unit", "R7-names-this-batch"
        elif any(CHANGELOG_HEAD.search(h) for h in [block.heading]):
            label, sub, rule = "LEGITIMATE_COLLATERAL", "changelog", "R4-under-changelog-heading"
        else:
            label, sub, rule = "UNRESOLVED", "new-unit", "R9-judgement"
        emit(key, block.kind, [], lines, 0, after.count("\n", 0, block.start) + 1,
             label, sub, rule, why, [block.heading])
        event["unit_events"].append({"event": "added", "unit": key, "target_reason": why})
    # deleted units
    for key in removed_keys:
        block, text = pby[key], ptext[key]
        why = unit_targeted(block, text, ctx)
        label, sub, rule = (("INTENDED", "deleted-unit", "R6-target-record") if why else
                            ("VERBATIM_COPY_DRIFT", "lost-unit", "R10-unit-lost"))
        emit(key, block.kind, text.splitlines(), [], before.count("\n", 0, block.start) + 1, 0,
             label, sub, rule, why, [block.heading])
        event["unit_events"].append({"event": "deleted", "unit": key, "target_reason": why})
    return event


def resolve_commit(events: list[dict[str, Any]], spec: dict[str, Any]) -> None:
    """Commit-level rules, then the hand labels.

    R12 — a unit the commit's own INTENDED hunks name (a promoted stub named by the record that
    replaces it, a LIT record named by its PAPER) is part of the same intended change. Then every
    hunk whose id `labels_spec.json` lists takes the judgement recorded there, with its rationale.
    """
    intended = "\n".join(line for event in events for hunk in event["hunks"]
                         if hunk["label"] == "INTENDED" for line in hunk["_add"])
    linked = named_ids(intended)
    for event in events:
        for hunk in event["hunks"]:
            if hunk["label"] == "UNRESOLVED" and heading_id(hunk["unit"]) & linked:
                hunk.update(label="INTENDED", sublabel="linked-by-target",
                            rule="R12-named-by-an-intended-hunk")
            override = spec.get(hunk["id"])
            if override:
                hunk.update(label=override["label"], sublabel=override.get("sublabel", ""),
                            rule="J-judgement", judgement=override["rationale"])
            hunk.pop("_add", None)


def pair_renames(removed: list[str], added: list[str], ptext: dict[str, str],
                 ctext: dict[str, str]) -> list[tuple[str, str]]:
    """A unit whose heading changed: same Identifier values, or the new unit names the old key."""
    pairs: list[tuple[str, str]] = []
    free = list(added)
    for old in removed:
        old_ids = record_identifiers(ptext[old])
        for new in free:
            new_ids = record_identifiers(ctext[new])
            if (old_ids and old_ids == new_ids) or re.search(
                    r"(?<![\w-])" + re.escape(old) + r"(?![\w-])", ctext[new]) and old_ids & new_ids:
                pairs.append((old, new))
                free.remove(new)
                break
    return pairs


def j0(repo: Path, rev: str) -> dict[str, Any]:
    files = corpus_files(repo, rev)
    spec_doc = json.loads(SPEC.read_text(encoding="utf-8")) if SPEC.is_file() else {}
    spec = {item["id"]: item for item in spec_doc.get("judgements", [])}
    log = git(repo, "log", "--full-history", "--no-merges", "--reverse", "--format=%H %P", rev,
              "--", *files).splitlines()
    merges = git(repo, "log", "--merges", "--format=%H", rev, "--", *files).split()
    evil = [m[:12] for m in merges
            if git(repo, "diff-tree", "--cc", "--no-commit-id", m, "--", *files).strip()]
    commits, excluded, strict_commits = [], [], []
    order = [(line.split()[0], line.split()[1:], "") for line in log]
    order.extend(evil_full(repo, rev, files))
    patches: dict[str, str] = {}
    for sha, parents, brought in order:
        if not parents:
            excluded.append({"commit": sha[:12], "reason": "root commit: no parent to replay"})
            continue
        ctx = commit_context(repo, sha, files, parents[0], brought)
        changed = git(repo, "diff-tree", "--no-commit-id", "-r", "--name-only", ctx["parent"],
                      sha, "--", *files).split()
        events = [label_file(repo, ctx, path, spec) for path in changed]
        resolve_commit(events, spec)
        sctx = commit_context(repo, sha, files, parents[0], brought, strict=True)
        strict_events = [label_file(repo, sctx, path, {}) for path in changed]
        resolve_commit(strict_events, {})
        pid = patch_id(repo, ctx["parent"], sha, files)
        duplicate = patches.setdefault(pid, sha[:12])
        commits.append({
            "commit": sha[:12], "parent": git(repo, "rev-parse", ctx["parent"]).strip()[:12],
            "kind": "evil-merge" if brought else "commit",
            "duplicate_of": duplicate if duplicate != sha[:12] else "",
            "subject": ctx["subject"],
            "batch_ids": sorted(ctx["batch_ids"]), "structural": ctx["structural"],
            "targets": sorted(f"{a} {b}" for a, b in ctx["targets"]),
            "named_identifier_count": len(ctx["named_identifiers"]),
            "companions": ctx["companions"], "files": events})
        strict_commits.append({"duplicate_of": commits[-1]["duplicate_of"],
                               "files": strict_events})
    unique = [c for c in commits if not c["duplicate_of"]]
    return {"rev": git(repo, "rev-parse", rev).strip(), "files": files,
            "merges_touching_files": len(merges), "evil_merges": evil,
            "excluded": excluded, "summary": summarise(commits),
            "summary_unique_patches": summarise(unique),
            "summary_strict_message_only": summarise(
                [c for c in strict_commits if not c["duplicate_of"]]),
            "commits": commits}


def evil_full(repo: Path, rev: str, files: list[str]) -> list[tuple[str, list[str], str]]:
    """Merges whose combined diff touches a corpus file: content neither parent had.

    Replayed from the parent whose diff to the merge, over the corpus files, is smallest — that
    diff is the merge's own edit plus what the other side brought, and the other side's commit
    messages are part of what the merge says it does."""
    out = []
    for merge in git(repo, "log", "--merges", "--format=%H", rev, "--", *files).split():
        if not git(repo, "diff-tree", "--cc", "--no-commit-id", merge, "--", *files).strip():
            continue
        parents = git(repo, "log", "-1", "--format=%P", merge).split()
        sizes = [(len(git(repo, "diff", p, merge, "--", *files)), p) for p in parents]
        chosen = min(sizes)[1]
        other = next(p for p in parents if p != chosen)
        out.append((merge, [chosen], other))
    return out


def patch_id(repo: Path, parent: str, sha: str, files: list[str]) -> str:
    diff = git_bytes(repo, "diff", parent, sha, "--", *files)
    done = subprocess.run(["git", "-C", str(repo), "patch-id", "--stable"], input=diff,
                          capture_output=True, check=True).stdout.decode().split()
    return done[0] if done else hashlib.sha256(diff).hexdigest()


def summarise(commits: list[dict[str, Any]]) -> dict[str, Any]:
    labels: Counter[str] = Counter()
    rules: Counter[str] = Counter()
    per_file: dict[str, Counter[str]] = {}
    units: Counter[str] = Counter()
    events = 0
    for commit in commits:
        for event in commit["files"]:
            events += 1
            name = Path(event["file"]).name
            per_file.setdefault(name, Counter())
            for hunk in event["hunks"]:
                labels[hunk["label"]] += 1
                rules[hunk["rule"]] += 1
                per_file[name][hunk["label"]] += 1
            for unit in event["unit_events"]:
                units[unit["event"]] += 1
    return {"commits": len(commits), "file_events": events,
            "hunks": sum(labels.values()), "labels": dict(labels.most_common()),
            "rules": dict(sorted(rules.items())),
            "per_file": {k: dict(v.most_common()) for k, v in sorted(per_file.items())},
            "unit_events": dict(units)}


def dump(doc: dict[str, Any], path: Path) -> None:
    """One hunk per line: reviewable in a diff, and the file stays proportional to the corpus."""
    lines = ["{"]
    keys = list(doc)
    for index, key in enumerate(keys):
        comma = "," if index < len(keys) - 1 else ""
        if key != "commits":
            lines.append(f"  {json.dumps(key)}: {json.dumps(doc[key], ensure_ascii=False)}{comma}")
            continue
        lines.append('  "commits": [')
        for ci, commit in enumerate(doc["commits"]):
            head = {k: v for k, v in commit.items() if k != "files"}
            lines.append("    {" + json.dumps(head, ensure_ascii=False)[1:-1] + ', "files": [')
            for fi, event in enumerate(commit["files"]):
                ehead = {k: v for k, v in event.items() if k != "hunks"}
                lines.append("      {" + json.dumps(ehead, ensure_ascii=False)[1:-1]
                             + ', "hunks": [')
                for hi, hunk in enumerate(event["hunks"]):
                    tail = "," if hi < len(event["hunks"]) - 1 else ""
                    lines.append("        " + json.dumps(hunk, ensure_ascii=False) + tail)
                lines.append("      ]}" + ("," if fi < len(commit["files"]) - 1 else ""))
            lines.append("    ]}" + ("," if ci < len(doc["commits"]) - 1 else ""))
        lines.append("  ]" + comma)
    lines.append("}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    p0 = sub.add_parser("j0", help="build and label the historical corpus")
    p0.add_argument("--repo", type=Path, default=ROOT)
    p0.add_argument("--rev", default="HEAD")
    p0.add_argument("--out", type=Path, default=CORPUS)
    args = parser.parse_args(argv)
    if args.command == "j0":
        doc = j0(args.repo, args.rev)
        dump(doc, args.out)
        print(json.dumps(doc["summary"], indent=1))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
