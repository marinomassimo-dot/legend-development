#!/usr/bin/env python3
"""Benchmark input surface — build it, prove it, freeze it.

The problem this exists for:

`framework/protocols/controlled_benchmark_ab.md` asks a blind first pass to be a property
of the *surface* handed to each reader rather than a promise each reader makes. A promise
cannot be checked after the fact; a directory whose entire content is enumerated and
digested can be, by anyone, from the manifest alone.

Four acts, four subcommands, one digest function shared by all of them:

    build       copy an allowlist into one directory per actor, from a source root
    verify      the ex-ante checks: parity across surfaces, forbidden paths absent, no
                file outside the allowlist, and a content scan for the paper's own
                identifiers in everything that is not the paper
    freeze      the tree digest of one surface, and every file digest under it
    population  enumerate the paper's structural evidence units, by declared pattern,
                before anyone reads — so the denominator of every coverage number is
                fixed and cannot be redefined once the readings exist

What this refuses to do, deliberately:

  * it never invents an allowlist. Every path comes from a spec file that is reviewed
    like any other governance artifact, and a file that is not in the spec does not
    reach a surface;
  * it never repairs a mismatch. `verify` reports and exits non-zero; a surface that
    fails is rebuilt from the spec, not patched;
  * it makes no claim that a reader cannot read outside the surface. Nothing here
    enforces anything at runtime (Annex J.0). It makes the blind path the default path,
    the allowlist enumerable, and any departure from it visible in the locators.

Exit codes:  0 clean · 1 findings · 2 refuses to guess (missing input, unreadable spec)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any

SPEC_VERSION = 1
# A digest of bytes, never of a normalized or re-encoded form: the whole point is that
# two surfaces hold the identical file, and normalization would hide the case where they
# do not.
CHUNK = 1 << 20


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            block = handle.read(CHUNK)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def iter_files(root: Path) -> list[Path]:
    """Every regular file under root, .git excluded, sorted by relative path.

    `.git` is excluded because the surface is a standalone repository and its object
    store is an artifact of the actor's own commits, not of the surface handed over.
    Anything else present is reported: a file nobody put in the allowlist is exactly
    what `verify` exists to catch.
    """
    out = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        if ".git" in path.relative_to(root).parts:
            continue
        out.append(path)
    return out


def tree_digest(root: Path) -> tuple[str, list[tuple[str, str]]]:
    """SHA-256 over the sorted `path\\0sha256\\n` lines of every regular file.

    One function for build, verify and freeze, so the number in a frozen receipt and
    the number in a handover block are the same kind of object. Byte layout is pinned
    here for the reason P5.2 pins its own: a value computed two ways is two values.
    """
    pairs = [(str(path.relative_to(root)), sha256_file(path)) for path in iter_files(root)]
    pairs.sort(key=lambda item: item[0])
    serialized = "".join(f"{rel}\0{digest}\n" for rel, digest in pairs)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest(), pairs


def load_spec(path: Path) -> dict[str, Any]:
    if not path.is_file():
        sys.exit(f"REFUSE: spec not found: {path}")
    try:
        spec = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        sys.exit(f"REFUSE: spec is not valid JSON: {exc}")
    version = spec.get("spec_version")
    if version != SPEC_VERSION:
        sys.exit(f"REFUSE: spec_version {version!r}; this tool speaks {SPEC_VERSION}")
    for key in ("benchmark_id", "actors", "common_files", "source_files", "per_actor_files",
                "empty_dirs", "forbidden_prior_output_paths", "content_scan"):
        if key not in spec:
            sys.exit(f"REFUSE: spec is missing required key {key!r}")
    return spec


def _entries(spec: dict[str, Any], key: str) -> list[dict[str, str]]:
    """`[{source, surface, kind?}]` — the source path is relative to --source-root."""
    return list(spec[key])


def surface_root(out_root: Path, benchmark_id: str, actor: str) -> Path:
    return out_root / benchmark_id / actor


def cmd_build(args: argparse.Namespace) -> int:
    spec = load_spec(Path(args.spec))
    source_root = Path(args.source_root).resolve()
    out_root = Path(args.out).resolve()
    if not source_root.is_dir():
        sys.exit(f"REFUSE: source root is not a directory: {source_root}")

    common = _entries(spec, "common_files") + _entries(spec, "source_files")
    findings: list[str] = []
    built: dict[str, dict[str, str]] = {}

    for actor in spec["actors"]:
        root = surface_root(out_root, spec["benchmark_id"], actor)
        if root.exists():
            if not args.force:
                sys.exit(f"REFUSE: surface already exists: {root} (use --force to rebuild)")
            shutil.rmtree(root)
        root.mkdir(parents=True)

        per_actor = spec["per_actor_files"].get(actor)
        if per_actor is None:
            sys.exit(f"REFUSE: spec has no per_actor_files entry for actor {actor!r}")

        digests: dict[str, str] = {}
        for entry in common + list(per_actor):
            src = source_root / entry["source"]
            if not src.is_file():
                findings.append(f"MISSING SOURCE  {actor}  {entry['source']}")
                continue
            dst = root / entry["surface"]
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dst)
            digests[entry["surface"]] = sha256_file(dst)

        for rel in spec["empty_dirs"]:
            (root / rel).mkdir(parents=True, exist_ok=True)
            # An empty directory does not survive a copy or a clone. `.gitkeep` is content,
            # so it is declared in the allowlist by construction rather than smuggled in.
            keep = root / rel / ".gitkeep"
            keep.write_bytes(b"")
            digests[str(keep.relative_to(root))] = sha256_file(keep)

        built[actor] = digests
        print(f"BUILT  {actor}  {len(digests)} file(s)  {root}")

    if findings:
        for item in findings:
            print(f"  [BLOCK] {item}")
        print(f"VERDICT: FAIL — {len(findings)} missing source file(s); surfaces are incomplete")
        return 1

    if args.emit_digests:
        Path(args.emit_digests).write_text(
            json.dumps(built, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"digests written to {args.emit_digests}")
    print("VERDICT: BUILT — run `verify` before any handover; building is not proving")
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    spec = load_spec(Path(args.spec))
    out_root = Path(args.surfaces).resolve()
    actors = list(spec["actors"])
    if len(actors) != 2:
        sys.exit(f"REFUSE: parity is defined over exactly two surfaces; spec declares {len(actors)}")

    roots = {actor: surface_root(out_root, spec["benchmark_id"], actor) for actor in actors}
    for actor, root in roots.items():
        if not root.is_dir():
            sys.exit(f"REFUSE: surface not found: {root}")

    findings: list[str] = []
    allowed: dict[str, set[str]] = {actor: set() for actor in actors}
    per_actor_surfaces = {
        entry["surface"]
        for actor in actors for entry in spec["per_actor_files"][actor]
    }

    # 1 · every declared common/source path exists in both surfaces with equal digests
    identical = _entries(spec, "common_files") + _entries(spec, "source_files")
    for entry in identical:
        rel = entry["surface"]
        digests = {}
        for actor in actors:
            path = roots[actor] / rel
            allowed[actor].add(rel)
            if not path.is_file():
                findings.append(f"ABSENT          {actor}  {rel}")
                continue
            digests[actor] = sha256_file(path)
        if len(digests) == 2 and len(set(digests.values())) != 1:
            findings.append(
                f"PARITY BROKEN   {rel}  "
                + "  ".join(f"{actor}={digest[:16]}…" for actor, digest in digests.items()))

    # 2 · the per-actor paths: present, and NOT equal across actors unless the spec says so
    for actor in actors:
        for entry in spec["per_actor_files"][actor]:
            rel = entry["surface"]
            allowed[actor].add(rel)
            if not (roots[actor] / rel).is_file():
                findings.append(f"ABSENT          {actor}  {rel}  (per-actor)")
    for rel in sorted(per_actor_surfaces):
        digests = {
            actor: sha256_file(roots[actor] / rel)
            for actor in actors if (roots[actor] / rel).is_file()
        }
        if len(digests) == 2 and len(set(digests.values())) == 1 and not spec.get(
                "per_actor_may_be_identical", []).__contains__(rel):
            findings.append(
                f"NOT DIFFERING   {rel}  identical across actors, but declared per-actor")

    # 3 · empty output slots: their .gitkeep is allowed, nothing else may be there at handover
    for rel in spec["empty_dirs"]:
        for actor in actors:
            allowed[actor].add(f"{rel}/.gitkeep")
            directory = roots[actor] / rel
            if not directory.is_dir():
                findings.append(f"ABSENT          {actor}  {rel}/  (output slot)")
                continue
            extra = [
                str(path.relative_to(roots[actor]))
                for path in iter_files(directory) if path.name != ".gitkeep"
            ]
            if extra and not args.post_read:
                findings.append(
                    f"NOT EMPTY       {actor}  {rel}/  {len(extra)} file(s) before handover")

    # 4 · nothing in a surface outside the allowlist
    for actor in actors:
        present = {str(path.relative_to(roots[actor])) for path in iter_files(roots[actor])}
        if args.post_read:
            present = {
                rel for rel in present
                if not any(rel.startswith(f"{d}/") for d in spec["empty_dirs"])
            }
        for rel in sorted(present - allowed[actor]):
            findings.append(f"NOT ALLOWLISTED {actor}  {rel}")

    # 5 · forbidden prior-output paths absent from both surfaces
    #
    # 🔴 The reader's OWN manifest lands at exactly the path LEGEND's prior manifest occupies
    # — `deepdive_manifest.py` derives that path from disease and PMID, so it cannot be
    # elsewhere without breaking the validator. Post-read the two are indistinguishable BY
    # PATH, and nothing here can tell authorship apart. So the guarantee is carried by the
    # pre-handover run, where the slot is proven empty and the forbidden path proven absent,
    # plus the freeze receipt that pins what the tree held at completion. Post-read, output
    # slots are skipped rather than reported on evidence this check does not have.
    #
    # This collision is also the sharpest argument for §2.1 of the protocol: in a checkout of
    # the repository, the reader would be writing its manifest on top of the prior one.
    for rel in spec["forbidden_prior_output_paths"]:
        if args.post_read and any(rel.startswith(f"{d}/") for d in spec["empty_dirs"]):
            continue
        for actor in actors:
            if (roots[actor] / rel).exists():
                findings.append(f"PRIOR OUTPUT    {actor}  {rel}  present in surface")

    # 6 · content scan — the paper's identifiers must not appear in anything that is not
    #     the paper. The packet and the instruction files are exempt by declaration: the
    #     instructions must name the PMID, and the paper is the paper.
    scan = spec["content_scan"]
    pattern = re.compile(scan["pattern"], re.IGNORECASE)
    exempt = set(scan.get("exempt_surface_paths", []))
    suffixes = tuple(scan.get("text_suffixes", [".md", ".txt", ".json", ".py", ".yaml", ".yml"]))
    for actor in actors:
        for path in iter_files(roots[actor]):
            rel = str(path.relative_to(roots[actor]))
            # 🔴 In --post-read the output slots hold the READER'S OWN work, which names the
            # paper by construction — a manifest must carry the PMID. Scanning them reports
            # a leak on every honest reading, and a check that fires on the correct case is
            # a check people learn to ignore. Found by running this on a synthetic output
            # tree before any reader ever saw the tool.
            if args.post_read and any(rel.startswith(f"{d}/") for d in spec["empty_dirs"]):
                continue
            if rel in exempt or not rel.endswith(suffixes):
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="strict")
            except (UnicodeDecodeError, OSError):
                continue
            hits = pattern.findall(text)
            if hits:
                findings.append(
                    f"IDENTIFIER LEAK {actor}  {rel}  {len(hits)} hit(s): "
                    + ", ".join(sorted({str(h) for h in hits})[:5]))

    for item in findings:
        print(f"  [BLOCK] {item}")
    for actor in actors:
        digest, pairs = tree_digest(roots[actor])
        print(f"  {actor}  tree_sha256 {digest}  files {len(pairs)}")
    if findings:
        print(f"VERDICT: FAIL — {len(findings)} finding(s). A surface that fails is rebuilt "
              "from the spec, never patched.")
        return 1
    print("VERDICT: PASS — parity holds, allowlist is exhaustive, no prior output, no leak. "
          "This says nothing about what a reader may open by absolute path (Annex J.0).")
    return 0


def cmd_freeze(args: argparse.Namespace) -> int:
    root = Path(args.surface).resolve()
    if not root.is_dir():
        sys.exit(f"REFUSE: not a directory: {root}")
    digest, pairs = tree_digest(root)
    record = {
        "_schema": "LEGEND benchmark · frozen surface receipt v1",
        "surface": str(root),
        "actor_id": args.actor_id,
        "benchmark_id": args.benchmark_id,
        "tree_sha256": digest,
        "file_count": len(pairs),
        "files": [{"path": rel, "sha256": sha} for rel, sha in pairs],
        "note": ("Digests of bytes at freeze time. The freeze is taken on the completion "
                 "declaration and BEFORE the content is read, so that the timing is a "
                 "property of the record and not of anyone's account of it."),
    }
    if args.out:
        Path(args.out).write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        print(f"FROZEN  {args.actor_id}  {digest}  {len(pairs)} file(s)  → {args.out}")
    else:
        print(json.dumps(record, indent=2))
    return 0


def _pdf_pages(path: Path) -> list[str]:
    try:
        import fitz  # type: ignore
    except ImportError:
        sys.exit("REFUSE: PyMuPDF is required to enumerate units from a PDF artifact")
    with fitz.open(str(path)) as doc:
        return [page.get_text() for page in doc]


def cmd_population(args: argparse.Namespace) -> int:
    """Enumerate structural evidence units, by declared pattern, before anyone reads.

    Structural enumeration is not a reading: it lists what the paper CONTAINS — figures,
    their lettered panels, tables, Results subsections, supplementary items — and says
    nothing about what any of it shows. That is why Plan may run it without crossing the
    epistemic boundary (body §28), and why it must be fixed before the readings exist:
    a denominator chosen afterwards is a denominator chosen to fit.
    """
    spec = load_spec(Path(args.spec))
    population_spec = spec.get("population")
    if population_spec is None:
        sys.exit("REFUSE: spec has no `population` block")
    source_root = Path(args.source_root).resolve()

    units: list[dict[str, Any]] = []
    for source in population_spec["sources"]:
        path = source_root / source["source"]
        if not path.is_file():
            sys.exit(f"REFUSE: population source missing: {path}")
        artifact = source["surface"]
        # 🔴 One segment per PAGE for a PDF, and ONE segment for the whole text file — not
        # one per line. A caption window that stops at the end of the line the label sits on
        # finds the first panel and no other: measured on this paper, per-line segmentation
        # reported 1 panel for a six-panel figure. The window has to cross line boundaries,
        # so the locus is computed from the match offset instead of from the segment.
        if path.suffix.lower() == ".pdf":
            segments = [(f"p{i + 1}", None, text) for i, text in enumerate(_pdf_pages(path))]
        else:
            whole = path.read_text(encoding="utf-8", errors="replace")
            segments = [(None, "line", whole)]

        for rule in source["rules"]:
            pattern = re.compile(rule["pattern"], re.MULTILINE)
            panel_pattern = re.compile(rule["panel_pattern"]) if rule.get("panel_pattern") else None
            range_pattern = (re.compile(rule["panel_range_pattern"])
                             if rule.get("panel_range_pattern") else None)
            seen: set[str] = set()
            for fixed_locus, locus_mode, text in segments:
                for match in pattern.finditer(text):
                    label = " ".join(match.group("label").split())
                    if label in seen:
                        continue
                    seen.add(label)
                    locus = (fixed_locus if fixed_locus is not None
                             else f"l{text.count(chr(10), 0, match.start()) + 1}")
                    unit = {
                        "unit_id": f"{rule['kind']}:{label}",
                        "kind": rule["kind"],
                        "label": label,
                        "artifact": artifact,
                        "locus": locus,
                    }
                    if panel_pattern is not None:
                        tail = text[match.end(): match.end() + rule.get("panel_window", 2600)]
                        found = {m.group(1) for m in panel_pattern.finditer(tail)}
                        # 🔴 A caption may label a range — `(C-D)` — and a pattern that reads
                        # only single letters silently drops every panel inside one. Measured
                        # on this paper: Figure 6 reported A,B,E and contains A,B,C,D,E. A
                        # denominator short by two panels is a coverage number that flatters
                        # both readers, so ranges are expanded rather than approximated.
                        if range_pattern is not None:
                            for m in range_pattern.finditer(tail):
                                start, stop = ord(m.group(1)), ord(m.group(2))
                                if start <= stop:
                                    found.update(chr(code) for code in range(start, stop + 1))
                        unit["panels"] = sorted(found)
                    units.append(unit)

    units.sort(key=lambda item: (item["kind"], item["label"]))
    panel_units = sum(len(unit.get("panels", [])) for unit in units)
    record = {
        "_schema": "LEGEND benchmark · evaluation population v1",
        "benchmark_id": spec["benchmark_id"],
        "pmid": spec.get("pmid"),
        "derivation": ("framework/scripts/benchmark_input_surface.py population "
                       "--spec <spec> --source-root <root>"),
        "note": ("Structural enumeration only. It lists what the paper contains, never what "
                 "any unit shows, and it does NOT rank units by importance — which of them "
                 "matter is exactly what the readings and the adjudication are for."),
        # Carried verbatim from the spec: caption anomalies and extraction limits observed
        # when the population was first derived. They belong beside the numbers, not in a
        # separate file a reader of the numbers never opens.
        "declared_notes": population_spec.get("notes", []),
        "counts": {"units": len(units), "panels": panel_units,
                   "by_kind": {kind: sum(1 for unit in units if unit["kind"] == kind)
                               for kind in sorted({unit["kind"] for unit in units})}},
        "units": units,
    }
    if args.out:
        Path(args.out).write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        print(f"POPULATION  {len(units)} unit(s), {panel_units} panel(s) → {args.out}")
        for kind, count in record["counts"]["by_kind"].items():
            print(f"  {kind:24s} {count}")
    else:
        print(json.dumps(record, indent=2))
    return 0


def _allowed_paths(spec: dict[str, Any], actor: str) -> set[str]:
    allowed = {entry["surface"]
               for entry in _entries(spec, "common_files") + _entries(spec, "source_files")}
    allowed |= {entry["surface"] for entry in spec["per_actor_files"][actor]}
    allowed |= {f"{rel}/.gitkeep" for rel in spec["empty_dirs"]}
    return allowed


def cmd_locators(args: argparse.Namespace) -> int:
    """After a reading: does every locator point INSIDE the surface it was read in?

    `verify` proves what was handed over. This proves what was cited — the other half, and
    the only one that speaks to where the reader actually went. A locator naming an artifact
    outside the allowlist is a reading that left the surface and said so in its own record;
    it is reported per entry, never dropped, because a dropped entry is a reading that looks
    clean and is not.

    A render the reader made under an output directory is legitimate and is admitted: it is
    derived from the packet, inside the surface, and declared with its digest. What is not
    admitted is any path that is neither allowlisted nor produced here.
    """
    spec = load_spec(Path(args.spec))
    root = Path(args.surface).resolve()
    manifest_path = (root / "disease-models" / args.disease / "research" / "deepdive_manifests"
                     / f"PMID{args.pmid}.json")
    if not manifest_path.is_file():
        sys.exit(f"REFUSE: no manifest at {manifest_path}")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        sys.exit(f"REFUSE: manifest is not valid JSON: {exc}")

    allowed = _allowed_paths(spec, args.actor_id)
    produced = tuple(f"{rel}/" for rel in spec["empty_dirs"])
    findings: list[str] = []

    def check(path_value: str, where: str) -> None:
        if path_value in allowed or path_value.startswith(produced):
            return
        findings.append(f"OUTSIDE SURFACE  {where}  {path_value}")

    for index, artifact in enumerate(manifest.get("source_artifacts") or []):
        check(str(artifact.get("path", "")), f"source_artifacts[{index}]")
    entries = (manifest.get("verbatim_locators") or {}).get("entries") or []
    for index, entry in enumerate(entries):
        check(str(entry.get("artifact", "")), f"entries[{index}]")

    for item in findings:
        print(f"  [BLOCK] {item}")
    print(f"  checked {len(manifest.get('source_artifacts') or [])} artifact(s), "
          f"{len(entries)} locator(s)")
    if findings:
        print(f"VERDICT: FAIL — {len(findings)} citation(s) outside the benchmark surface. "
              "Each is recorded as BENCH_INVALID for that entry, not removed.")
        return 1
    print("VERDICT: PASS — every cited artifact is inside the surface or was produced in it.")
    return 0


def cmd_tree_digest(args: argparse.Namespace) -> int:
    root = Path(args.path).resolve()
    if not root.is_dir():
        sys.exit(f"REFUSE: not a directory: {root}")
    digest, pairs = tree_digest(root)
    print(f"{digest}  {len(pairs)} file(s)  {root}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    build = sub.add_parser("build", help="copy the allowlist into one surface per actor")
    build.add_argument("--spec", required=True)
    build.add_argument("--source-root", required=True)
    build.add_argument("--out", required=True)
    build.add_argument("--force", action="store_true", help="rebuild over an existing surface")
    build.add_argument("--emit-digests", help="write the per-actor digest map to this path")
    build.set_defaults(func=cmd_build)

    verify = sub.add_parser("verify", help="the ex-ante checks; run before any handover")
    verify.add_argument("--spec", required=True)
    verify.add_argument("--surfaces", required=True)
    verify.add_argument("--post-read", action="store_true",
                        help="after a reading: allow content in the output slots, still "
                             "enforce parity, allowlist and prior-output absence elsewhere")
    verify.set_defaults(func=cmd_verify)

    freeze = sub.add_parser("freeze", help="tree digest and per-file digests of one surface")
    freeze.add_argument("--surface", required=True)
    freeze.add_argument("--actor-id", required=True)
    freeze.add_argument("--benchmark-id", required=True)
    freeze.add_argument("--out")
    freeze.set_defaults(func=cmd_freeze)

    population = sub.add_parser("population", help="enumerate structural evidence units")
    population.add_argument("--spec", required=True)
    population.add_argument("--source-root", required=True)
    population.add_argument("--out")
    population.set_defaults(func=cmd_population)

    locators = sub.add_parser(
        "locators", help="after a reading: every cited artifact is inside the surface")
    locators.add_argument("--spec", required=True)
    locators.add_argument("--surface", required=True)
    locators.add_argument("--actor-id", required=True)
    locators.add_argument("--pmid", required=True)
    locators.add_argument("--disease", default="wwox")
    locators.set_defaults(func=cmd_locators)

    digest = sub.add_parser("tree-digest", help="the shared tree digest, on any directory")
    digest.add_argument("--path", required=True)
    digest.set_defaults(func=cmd_tree_digest)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
