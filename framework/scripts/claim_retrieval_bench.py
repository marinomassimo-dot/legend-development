#!/usr/bin/env python3
"""Benchmark I — can targeted claim retrieval replace loading the whole claim registry?

WHY THIS EXISTS
---------------
`framework/manuals/operator_manual.md` § 1.1 keeps `claim_registry_current.md` whole in every
scientific profile, and gives the reason in one line: *"una claim che il paper contraddice può
non essere collegata al paper — un recupero selettivo non può garantirlo"*. That is a testable
sentence. This command tests it on the repository's own history, and it separates the two ways
the whole-registry preload could be needed:

  I1  RETRIEVAL — does the affected claim reach the candidate set at all? Deterministic, no model.
  I2  ATTENTION — when it does, does a model find it as reliably in the small context as in the
      whole registry? A model is involved, so I2 is a separate experiment with its own runner.

A miss in I1 is a retrieval failure; a miss in I2 is an attention failure. Mixing them would
let a good retriever hide a bad reader, or the reverse.

WHAT IS HELD FIXED, AND WHY
---------------------------
- 🔴 **Ground truth is the historical diff, not the retriever.** `build` derives each fixture's
  target claims from the claim-registry diff of the commit that changed them, by the rule named
  in `fixture_spec.json`. The retriever never sees the targets.
- 🔴 **Retrieval runs against the registries as they stood BEFORE the change** (`C^`), in a
  detached worktree. At `C` the paper's own record already links the claim it changed — the
  consequence would be retrieving its own cause.
- 🔴 **The seed is what the reader held before comparison**: the verbatim locator snippets of
  the paper's deepdive manifest at `C^`, with every `CLAIM nnn` and wikilink scrubbed and
  counted. The reader's propositions are a secondary seed only, because they are LEGEND's
  framing of the paper, not the paper.
- 🔴 **`registry_records.py` is called, not re-implemented.** Both strategies are its own
  operations (`get --pmid --hops 1`; `get --theme … --match any --source claim_registry_current`),
  so the benchmark measures the tool the routes would use.

STRATEGIES (I1)
---------------
  FULL        not a retrieval — every claim, by definition; the context-size reference.
  CURRENT     `registry_records.py get --pmid <PMID> --hops 1` over every surface: what the
              comparison stage of `legend` already runs. Claims reached by mention or by one
              wikilink hop from any record that identifies or mentions the paper.
  PROGRESSIVE CURRENT ∪ a literal term query over the claim registry. Terms are the seed's
              word tokens (length ≥ 4, or ≥ 3 with a digit), kept when the tool's own term report
              says they occur in at least 1 and at most `df_cap` claim records — the cap
              removes words that name the whole corpus (WWOX, mice, protein), and nothing else
              is filtered. No stemming, synonyms, embeddings or ranking: the union is returned
              whole, and its size is reported rather than capped.

    python3 framework/scripts/claim_retrieval_bench.py build
    python3 framework/scripts/claim_retrieval_bench.py i1
    python3 framework/scripts/claim_retrieval_bench.py i1 --df-cap-fraction 0.2 --out /tmp/x.json

Exit codes: 0 done · 1 a fixture could not be built or run · 2 invalid invocation.
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Iterator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import registry_records  # noqa: E402

BENCH = ROOT / "framework/eval/benchmarks/BENCH-I-CLAIM-RETRIEVAL"
SPEC = BENCH / "fixture_spec.json"
FIXTURES = BENCH / "fixtures.json"
I1_RESULTS = BENCH / "i1_results.json"
CLAIMS = "disease-models/wwox/registries/claim_registry_current.md"
PAPERS = "disease-models/wwox/registries/paper_registry_current.md"
MANIFEST = "disease-models/wwox/research/deepdive_manifests/PMID{pmid}.json"
CLAIM_STEM = "claim_registry_current"

# Pre-registered in PREREGISTRATION.md before any fixture was run. The sensitivity values are
# reported beside the primary one and never replace it.
DF_CAP_FRACTION = 0.10
DF_CAP_SENSITIVITY = (0.05, 0.20)

CLAIM_HEAD = re.compile(r"(?m)^(?=## )")
CLAIM_ID = re.compile(r"## (CLAIM \d+)\s*$", re.M)
SCRUB_CLAIM = re.compile(r"\bCLAIM\s+\d+\b", re.I)
SCRUB_LINK = re.compile(r"\[\[[^\]]*\]\]")
TOKEN = re.compile(r"[^\W_](?:[\w\-]*[^\W_])?")


def git(*args: str, cwd: Path = ROOT) -> str:
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True,
                          check=True).stdout


def show(rev: str, path: str) -> str:
    done = subprocess.run(["git", "show", f"{rev}:{path}"], cwd=ROOT, capture_output=True,
                          text=True)
    return done.stdout if done.returncode == 0 else ""


def shown(path: Path) -> str:
    path = path.resolve()
    return str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)


def claim_records(text: str) -> dict[str, str]:
    """`## CLAIM nnn` blocks to the next `##` — the parser's own boundary for this surface."""
    out: dict[str, str] = {}
    for block in CLAIM_HEAD.split(text):
        match = CLAIM_ID.match(block.splitlines()[0] if block else "")
        if match:
            out[match.group(1)] = block
    return out


def diff_lines(before: str, after: str) -> tuple[str, str]:
    import difflib
    added, removed = [], []
    for line in difflib.unified_diff(before.splitlines(), after.splitlines(), lineterm="", n=0):
        if line.startswith("+") and not line.startswith("+++"):
            added.append(line[1:])
        elif line.startswith("-") and not line.startswith("---"):
            removed.append(line[1:])
    return "\n".join(added), "\n".join(removed)


def paper_ids_for(rev: str, pmid: str) -> list[str]:
    """Every paper-registry record whose Identifier at `rev` names the PMID."""
    ids = []
    for block in CLAIM_HEAD.split(show(rev, PAPERS)):
        head = block.splitlines()[0] if block else ""
        found = re.search(r"^\*\*Identifier:\*\*(.*)$", block, re.M)
        if head.startswith("## ") and found and re.search(rf"\b{pmid}\b", found.group(1)):
            ids.append(head[3:].split(" — ")[0].strip())
    return ids


def label_targets(commit: str, pmid: str) -> dict[str, Any]:
    """The labeling rule of fixture_spec.json, applied to the event commit's diff."""
    before, after = claim_records(show(f"{commit}^", CLAIMS)), claim_records(show(commit, CLAIMS))
    ids = paper_ids_for(commit, pmid)

    def refs(text: str) -> int:
        return text.count(pmid) + sum(len(re.findall(r"#" + re.escape(i) + r"\]\]", text))
                                      for i in ids)
    targets, evidence = [], {}
    for claim, body in after.items():
        if claim in before and before[claim] != body:
            added, removed = diff_lines(before[claim], body)
            if refs(added) > refs(removed):
                targets.append(claim)
                evidence[claim] = {"refs_added": refs(added), "refs_removed": refs(removed),
                                   "added_sha256": hashlib.sha256(added.encode()).hexdigest()}
    return {"targets": targets, "paper_ids": ids, "evidence": evidence}


def scrub(text: str) -> tuple[str, int]:
    """Wikilinks first, then bare claim ids — a claim id inside a link is one leak, not two."""
    links = len(SCRUB_LINK.findall(text))
    text = SCRUB_LINK.sub(" ", text)
    return SCRUB_CLAIM.sub(" ", text), links + len(SCRUB_CLAIM.findall(text))


def seed_for(rev: str, pmid: str) -> dict[str, Any]:
    raw = show(rev, MANIFEST.format(pmid=pmid))
    if not raw:
        return {}
    entries = (json.loads(raw).get("verbatim_locators") or {}).get("entries") or []
    snippets, snip_scrubbed = scrub("\n".join(str(e.get("snippet", "")) for e in entries))
    props, prop_scrubbed = scrub("\n".join(str(e.get("proposition", "")) for e in entries))
    return {"manifest_rev": rev, "manifest_sha256": hashlib.sha256(raw.encode()).hexdigest(),
            "locator_entries": len(entries), "snippet_text": snippets,
            "snippet_scrubbed_tokens": snip_scrubbed, "proposition_text": props,
            "proposition_scrubbed_tokens": prop_scrubbed}


def build(spec_path: Path = SPEC, out_path: Path = FIXTURES) -> int:
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    fixtures, failures = [], []
    for case in spec["cases"]:
        commit = git("rev-parse", case["commit"]).strip()
        label = label_targets(commit, case["pmid"])
        targets = case.get("target_override") or label["targets"]
        seed = seed_for(f"{commit}^", case["pmid"])
        before = claim_records(show(f"{commit}^", CLAIMS))
        problems = [t for t in targets if t not in before]
        if not targets or not seed or problems:
            failures.append(f"{case['fixture_id']}: targets={targets} seed={'yes' if seed else 'no'}"
                            f" missing_at_parent={problems}")
        fixtures.append({**{k: v for k, v in case.items() if k != "commit"},
                         "commit": commit, "parent": git("rev-parse", f"{commit}^").strip(),
                         "targets": targets, "rule_targets": label["targets"],
                         "target_source": "override" if case.get("target_override") else "rule",
                         "label_evidence": label["evidence"], "paper_ids_at_commit":
                         label["paper_ids"], "seed": seed})
    control = spec.get("no_change_control")
    if control:
        added = git("log", "--diff-filter=A", "--format=%H", "--",
                    MANIFEST.format(pmid=control["pmid"])).split()[-1]
        control = {**control, "commit": added, "parent": git("rev-parse", f"{added}^").strip(),
                   "targets": [], "seed": seed_for(added, control["pmid"]),
                   "_seed_note": "The manifest was added in this commit, so the seed is read AT it; "
                                 "the registries are read at its parent, like every fixture."}
    out = {"_schema": "LEGEND Benchmark I · built fixtures v1", "built_from": shown(spec_path), "spec_sha256": hashlib.sha256(
        spec_path.read_bytes()).hexdigest(), "fixtures": fixtures, "no_change_control": control,
        "invalid": spec.get("invalid", [])}
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"built {len(fixtures)} fixtures -> {shown(out_path)}")
    for line in failures:
        print(f"  FIXTURE NOT BUILDABLE: {line}")
    return 1 if failures else 0


@contextlib.contextmanager
def tree_at(rev: str) -> Iterator[Path]:
    """A detached worktree at `rev`, removed on exit — so every answer is BOUND to that commit."""
    base = Path(tempfile.mkdtemp(prefix="bench-i-"))
    path = base / rev[:12]
    git("worktree", "add", "--detach", "--quiet", str(path), rev)
    try:
        yield path
    finally:
        git("worktree", "remove", "--force", str(path))
        base.rmdir()


def terms_of(text: str) -> list[str]:
    seen: dict[str, None] = {}
    for token in TOKEN.findall(text):
        token = token.lower()
        if len(token) >= 4 or (len(token) >= 3 and any(ch.isdigit() for ch in token)):
            seen.setdefault(token, None)
    return list(seen)


def claims_in(selection: registry_records.Selection) -> list[tuple[str, int, str]]:
    return [(record.identity_id.upper(), len(record.text.encode("utf-8")), why)
            for record, why in selection.hits
            if record.source == CLAIM_STEM and record.kind == "record"]


def run_current(root: Path, pmid: str) -> dict[str, Any]:
    started = time.perf_counter()
    found = registry_records.select(root, "wwox", pmid=pmid, hops=1)
    elapsed = time.perf_counter() - started
    claims = claims_in(found)
    return {"operations": [f"registry_records.select(pmid={pmid}, hops=1, sources=ALL)"],
            "candidates": [c for c, _b, _w in claims],
            "selection_path": {c: w for c, _b, w in claims},
            "claim_bytes": sum(b for _c, b, _w in claims),
            "all_records_returned": len(found.hits),
            "all_bytes_returned": sum(len(r.text.encode("utf-8")) for r, _w in found.hits),
            "binding": found.repository.get("state"), "commit_read": found.repository.get("commit"),
            "runtime_s": round(elapsed, 3)}


def run_terms(root: Path, text: str, cap_fraction: float, n_claims: int) -> dict[str, Any]:
    started = time.perf_counter()
    terms = terms_of(text)
    cap = max(1, int(cap_fraction * n_claims))
    probe = registry_records.select(root, "wwox", theme=terms, match="any",
                                    sources=[CLAIM_STEM], hops=0) if terms else None
    df = {row["term"].lower(): row["records_containing"] for row in (probe.term_report
                                                                      if probe else [])}
    kept = [t for t in terms if 1 <= df.get(t, 0) <= cap]
    found = registry_records.select(root, "wwox", theme=kept, match="any",
                                    sources=[CLAIM_STEM], hops=0) if kept else None
    elapsed = time.perf_counter() - started
    claims = claims_in(found) if found else []
    reason: dict[str, list[str]] = {}
    if found:
        for record, _why in found.hits:
            lowered = record.text.lower()
            reason[record.identity_id.upper()] = [t for t in kept if t in lowered]
    return {"operations": [f"df probe: select(theme=<{len(terms)} terms>, match=any, "
                           f"sources=[{CLAIM_STEM}], hops=0).term_report",
                           f"select(theme=<{len(kept)} kept terms>, match=any, "
                           f"sources=[{CLAIM_STEM}], hops=0)"],
            "df_cap": cap, "terms_extracted": len(terms), "terms_kept": len(kept),
            "terms_absent": sum(1 for t in terms if df.get(t, 0) == 0),
            "terms_over_cap": sum(1 for t in terms if df.get(t, 0) > cap),
            "candidates": [c for c, _b, _w in claims], "matched_terms": reason,
            "runtime_s": round(elapsed, 3)}


def registry_size(root: Path) -> tuple[int, int]:
    path = root / CLAIMS
    records = [r for r in registry_records.parse_records(root, "wwox", CLAIM_STEM)
               if r.kind == "record"]
    return path.stat().st_size, len(records)


def evaluate(fixture: dict[str, Any], root: Path, cap_fraction: float,
             seed_key: str = "snippet_text") -> dict[str, Any]:
    registry_bytes, n_claims = registry_size(root)
    record_bytes = {r.identity_id.upper(): len(r.text.encode("utf-8"))
                    for r in registry_records.parse_records(root, "wwox", CLAIM_STEM)
                    if r.kind == "record"}
    targets = fixture["targets"]
    current = run_current(root, fixture["pmid"])
    terms = run_terms(root, fixture["seed"].get(seed_key, ""), cap_fraction, n_claims)
    union = list(dict.fromkeys(current["candidates"] + terms["candidates"]))
    progressive = {"operations": current["operations"] + terms["operations"],
                   "candidates": union,
                   "selection_path": {c: ("pmid route: " + current["selection_path"][c])
                                      if c in current["selection_path"] else
                                      "term route: " + ", ".join(terms["matched_terms"].get(c, []))
                                      for c in union},
                   "claim_bytes": sum(record_bytes.get(c, 0) for c in union),
                   "term_route": {k: v for k, v in terms.items() if k != "matched_terms"},
                   "runtime_s": round(current["runtime_s"] + terms["runtime_s"], 3)}
    out: dict[str, Any] = {"fixture_id": fixture["fixture_id"], "pmid": fixture["pmid"],
                           "class": fixture["class"], "targets": targets,
                           "registry_bytes": registry_bytes, "registry_claims": n_claims,
                           "binding": current["binding"], "commit_read": current["commit_read"],
                           "seed": seed_key, "df_cap_fraction": cap_fraction, "strategies": {}}
    for name, result in (("CURRENT", current), ("PROGRESSIVE", progressive)):
        hit = [t for t in targets if t in result["candidates"]]
        out["strategies"][name] = {
            **result, "targets_retrieved": hit,
            "target_recall": round(len(hit) / len(targets), 4) if targets else None,
            "all_targets_retrieved": bool(targets) and len(hit) == len(targets),
            "candidate_count": len(result["candidates"]),
            "registry_fraction": round(result["claim_bytes"] / registry_bytes, 4)}
    out["strategies"]["FULL"] = {"candidate_count": n_claims, "claim_bytes": sum(
        record_bytes.values()), "registry_bytes": registry_bytes, "registry_fraction": 1.0,
        "note": "not a retrieval: every claim by definition"}
    return out


def i1(fixtures_path: Path, out_path: Path, cap_fraction: float, seed_key: str,
       sensitivity: bool) -> int:
    data = json.loads(fixtures_path.read_text(encoding="utf-8"))
    fixtures = list(data["fixtures"])
    if data.get("no_change_control"):
        fixtures.append(data["no_change_control"] | {"class": "NO_CHANGE_CONTROL"})
    rows: list[dict[str, Any]] = []
    extra: dict[str, list[dict[str, Any]]] = {}
    by_parent: dict[str, list[dict[str, Any]]] = {}
    for fixture in fixtures:
        by_parent.setdefault(fixture["parent"], []).append(fixture)
    for parent, group in by_parent.items():
        with tree_at(parent) as root:
            for fixture in group:
                rows.append(evaluate(fixture, root, cap_fraction, seed_key))
                if sensitivity:
                    for cap in DF_CAP_SENSITIVITY:
                        extra.setdefault(str(cap), []).append(
                            evaluate(fixture, root, cap, seed_key))
                    extra.setdefault("proposition_seed", []).append(
                        evaluate(fixture, root, cap_fraction, "proposition_text"))
    order = {f["fixture_id"]: i for i, f in enumerate(fixtures)}
    rows.sort(key=lambda r: order[r["fixture_id"]])
    for block in extra.values():
        block.sort(key=lambda r: order[r["fixture_id"]])
    out = {"_schema": "LEGEND Benchmark I · I1 deterministic retrieval results v1",
           "fixtures_sha256": hashlib.sha256(fixtures_path.read_bytes()).hexdigest(),
           "tool_sha256": {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
                           for name in ("registry_records.py", "claim_retrieval_bench.py")},
           "primary": {"df_cap_fraction": cap_fraction, "seed": seed_key},
           "summary": summarise(rows), "rows": rows,
           "sensitivity": {k: {"summary": summarise(v), "rows": [
               {"fixture_id": r["fixture_id"], **{s: {"hit": r["strategies"][s][
                   "targets_retrieved"], "candidate_count": r["strategies"][s]["candidate_count"],
                   "registry_fraction": r["strategies"][s]["registry_fraction"]}
                   for s in ("CURRENT", "PROGRESSIVE")}} for r in v]} for k, v in extra.items()}}
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out["summary"], indent=1))
    return 0


def summarise(rows: list[dict[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for klass in ("STRONG", "USABLE_WITH_LIMITATION"):
        subset = [r for r in rows if r["class"] == klass]
        entry: dict[str, Any] = {"fixtures": len(subset),
                                 "target_labels": sum(len(r["targets"]) for r in subset)}
        for name in ("CURRENT", "PROGRESSIVE"):
            got = sum(len(r["strategies"][name]["targets_retrieved"]) for r in subset)
            entry[name] = {
                "targets_retrieved": got,
                "fixtures_fully_retrieved": sum(r["strategies"][name]["all_targets_retrieved"]
                                                for r in subset),
                "median_candidates": median([r["strategies"][name]["candidate_count"]
                                             for r in subset]),
                "max_candidates": max((r["strategies"][name]["candidate_count"] for r in subset),
                                      default=0),
                "median_registry_fraction": median([r["strategies"][name]["registry_fraction"]
                                                    for r in subset])}
        out[klass] = entry
    return out


def median(values: list[float]) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    mid = len(ordered) // 2
    return ordered[mid] if len(ordered) % 2 else round((ordered[mid - 1] + ordered[mid]) / 2, 4)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("action", choices=("build", "i1"))
    parser.add_argument("--spec", default=str(SPEC))
    parser.add_argument("--fixtures", default=str(FIXTURES))
    parser.add_argument("--out", default="")
    parser.add_argument("--df-cap-fraction", type=float, default=DF_CAP_FRACTION)
    parser.add_argument("--seed", choices=("snippet_text", "proposition_text"),
                        default="snippet_text")
    parser.add_argument("--no-sensitivity", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.action == "build":
            return build(Path(args.spec), Path(args.out or FIXTURES))
        return i1(Path(args.fixtures), Path(args.out or I1_RESULTS), args.df_cap_fraction,
                  args.seed, not args.no_sensitivity)
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        print(f"TOOL ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
