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
import posixpath
import re
import shutil
import sys
from pathlib import Path
from typing import Any

SPEC_VERSION = 2
# A digest of bytes, never of a normalized or re-encoded form: the whole point is that
# two surfaces hold the identical file, and normalization would hide the case where they
# do not.
CHUNK = 1 << 20
REFUSE = 2

# The scan's default reach when a spec declares no `text_suffixes`. Named here because
# `scan_skip_reason()` and the scan loop must not each carry their own copy of it.
DEFAULT_TEXT_SUFFIXES = (".md", ".txt", ".json", ".py", ".yaml", ".yml")


def refuse(message: str) -> "NoReturn":  # type: ignore[valid-type]
    """Exit 2, the code the docstring promises for a refusal.

    🔴 `sys.exit("text")` prints and exits **1**, which is the code for FINDINGS. A
    refusal and a finding were therefore indistinguishable to any caller that reads the
    return code — including the protocol's own handover checklist, which branches on it.
    """
    print(message, file=sys.stderr)
    sys.exit(REFUSE)


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

    Symlinks are NOT returned here — their bytes live somewhere this tool did not look,
    so digesting them would attribute foreign content to the surface. They are not
    ignored either: `iter_symlinks` collects them and `verify` reports every one.
    """
    out = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        if ".git" in path.relative_to(root).parts:
            continue
        out.append(path)
    return out


def iter_symlinks(root: Path) -> list[tuple[str, str]]:
    """Every symlink under root, with the target it resolves to.

    🔴 `iter_files` skips symlinks, and for a while nothing else looked at them. A
    surface holding a file symlink to LEGEND's prior manifest, or a directory symlink to
    `deepdive_manifests/`, printed *"PASS — allowlist is exhaustive, no prior output"*:
    every check ran, and every one of them looked past the link. Plan builds by copy, so
    no built surface has one — but `verify` is the instrument a reviewer is told to
    trust INSTEAD of Plan's account, and an instrument that cannot see a class of object
    must say so rather than pass over it.

    `rglob` does not descend into a directory symlink, so the link itself is reported
    and its contents are never walked; that is the correct order — report the door,
    do not inventory the room behind it as though it were this one.
    """
    out = []
    for path in sorted(root.rglob("*")):
        if not path.is_symlink():
            continue
        if ".git" in path.relative_to(root).parts:
            continue
        try:
            target = str(path.resolve())
        except (OSError, RuntimeError):  # broken link, or a symlink loop
            target = f"<unresolvable: {path.readlink()}>"
        out.append((str(path.relative_to(root)), target))
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
        refuse(f"REFUSE: spec not found: {path}")
    try:
        spec = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        refuse(f"REFUSE: spec is not valid JSON: {exc}")
    version = spec.get("spec_version")
    if version != SPEC_VERSION:
        refuse(f"REFUSE: spec_version {version!r}; this tool speaks {SPEC_VERSION}")
    for key in ("benchmark_id", "actors", "common_files", "source_files", "per_actor_files",
                "empty_dirs", "forbidden_prior_output_paths", "content_scan",
                "expected_output_paths", "expected_output_prefixes"):
        if key not in spec:
            refuse(f"REFUSE: spec is missing required key {key!r}")
    return spec


def _entries(spec: dict[str, Any], key: str) -> list[dict[str, str]]:
    """`[{source, surface, kind?}]` — the source path is relative to --source-root."""
    return list(spec[key])


def _under_expected_prefix(rel: str, spec: dict[str, Any]) -> str | None:
    """The declared output prefix this path sits under, or None."""
    for prefix in spec["expected_output_prefixes"]:
        if rel.startswith(prefix):
            return prefix
    return None


def _is_decodable_text(path: Path) -> bool:
    """Can this tool read these bytes at all? The scan's reach, asked as a question.

    The exemption under an output prefix is written on **bytes**, not on position, and
    this is the predicate that decides it. Same rule the content scan uses to read a
    file, so the two cannot disagree about which files are readable.
    """
    try:
        path.read_text(encoding="utf-8", errors="strict")
    except (UnicodeDecodeError, OSError):
        return False
    return True


def _is_expected_output(rel: str, spec: dict[str, Any], path: Path) -> bool:
    """Is this the exact path a reader was TOLD to write, or a render under a slot?

    🔴 Revision 2's predicate was *"anywhere under an output slot"* narrowed to the exact
    declared list **or** any path under `expected_output_prefixes`. The exact list is right.
    The prefix was not: it exempted a path from the allowlist check AND from the content
    scan **on position alone**, so a decodable text file placed at `output/renders/` — a
    copy of prior LEGEND output, identifiers and all — passed `--post-read` with a
    `VERDICT: PASS`, while the same bytes one directory away produced `NOT ALLOWLISTED`
    plus `IDENTIFIER LEAK` (Mirror `M-2`).

    So the prefix now admits only what the exemption was written for: **a render is
    pixels**. A file under a declared output prefix is an expected output when this tool
    **cannot decode its bytes**; a decodable one is not exempt from anything and takes the
    same checks it would take anywhere else in the tree. That keeps every legitimate render
    working — the instructions ask for image renders and nothing else — and leaves the
    unchecked surface exactly the set `unchecked_surface()` enumerates and `verify` prints.

    `path` is required rather than optional on purpose: a caller that cannot see the bytes
    cannot decide this question, and an optional argument is how it would decide it anyway.
    """
    if rel in set(spec["expected_output_paths"]):
        return True
    if _under_expected_prefix(rel, spec) is None:
        return False
    return not _is_decodable_text(path)


def declared_blind_spots(spec: dict[str, Any]) -> list[str]:
    """Forbidden paths that a legitimate reader output would occupy anyway.

    Computed, never asserted: it is the intersection of what the reader is told to write
    with what must not be present. Printing it on every `--post-read` run is the point —
    a blind spot named in a comment is a blind spot the reader of the output never sees.

    This is the **exact-path** population only, and it is not the whole unchecked surface.
    `unchecked_surface()` is; read that one before writing a sentence about what
    `--post-read` establishes.
    """
    return sorted(set(spec["expected_output_paths"])
                  & set(spec["forbidden_prior_output_paths"]))


# 🔴 The census classes, and the one place their explanations live.
#
# Mirror `M-3`: revision 3's census enumerated the three populations that come out of
# ONE of the content scan's four skip conditions, and the tool then printed that the
# list was the whole of it. It was not: a declared scan-exempt input and a file whose
# suffix is outside `text_suffixes` are skipped by the scan and were named by nothing,
# and so was a text-suffixed file whose bytes do not decode. On a clean build that is
# sixteen present files per surface, before any reader exists.
#
# `expected` answers "is this a consequence the protocol declares", which is a different
# question from "was its content read". `still_covered_by` answers the question a
# reviewer asks next, and it is deliberately narrow: it names the checks that DID run,
# never a check that merely exists.
SCAN_SKIP_CLASSES: dict[str, dict[str, Any]] = {
    "blind_spot": {
        "expected": True,
        "reason": "blind-spot path, PRESENT; whose bytes these are is not decidable here",
        "still_covered_by": "the pre-handover verify run and the freeze receipt",
    },
    "scan_exempt_present": {
        "expected": True,
        "reason": "declared output, present; its content is not scanned, because it must "
                  "name the paper",
        "still_covered_by": "the forbidden-path check and the freeze receipt",
    },
    "undecodable_prefix": {
        "expected": True,
        "reason": "under a declared output prefix and not decodable as text; its content "
                  "was not scanned",
        "still_covered_by": "the forbidden-path check and the freeze receipt",
    },
    "scan_exempt_input": {
        "expected": True,
        "reason": "declared scan-exempt input; its content is not scanned, because the "
                  "instructions and the paper must name the paper",
        "still_covered_by": "the allowlist check, the forbidden-path check, cross-surface "
                            "parity for a change made to one surface only, and the freeze "
                            "receipt",
    },
    "suffix_not_scanned": {
        "expected": True,
        "reason": "suffix outside content_scan.text_suffixes; the scan never opened it",
        "still_covered_by": "the allowlist check, the forbidden-path check and the freeze "
                            "receipt",
    },
    "undecodable_text": {
        "expected": False,
        "reason": "a text suffix whose bytes did not decode as UTF-8; the scan could not "
                  "read it, and the protocol does not anticipate this file being binary",
        "still_covered_by": "the allowlist check, the forbidden-path check and the freeze "
                            "receipt",
    },
}


def scan_skip_reason(rel: str, spec: dict[str, Any], path: Path,
                     post_read: bool) -> str | None:
    """Why the content scan does not read this file's bytes — or `None` if it does.

    🔴 ONE predicate, called by the scan loop AND by the census, because Mirror `M-3` is
    what happens when they are two. Revision 3's census re-derived the skip conditions
    beside the loop that implements them, got one of four, and the tool printed that the
    result was complete. An equality maintained by two copies of a rule is an equality
    that holds until one copy is edited; here `actual unscanned == declared unscanned`
    holds because it is the same call.

    The order below is the scan loop's order and must stay that way: the class reported
    is the reason the file was ACTUALLY skipped, not the first reason that would also
    have applied. A PDF is `suffix_not_scanned` rather than `undecodable_text` because
    the suffix test is what returned first.
    """
    scan = spec["content_scan"]
    if post_read and _is_expected_output(rel, spec, path):
        if rel in set(declared_blind_spots(spec)):
            return "blind_spot"
        if rel in set(spec["expected_output_paths"]):
            return "scan_exempt_present"
        return "undecodable_prefix"
    if rel in set(scan.get("exempt_surface_paths", [])):
        return "scan_exempt_input"
    if not rel.endswith(tuple(scan.get("text_suffixes", DEFAULT_TEXT_SUFFIXES))):
        return "suffix_not_scanned"
    if not _is_decodable_text(path):
        return "undecodable_text"
    return None


def unchecked_surface(root: Path, spec: dict[str, Any],
                      post_read: bool = True) -> dict[str, list[str]]:
    """Every PRESENT file whose content the identifier scan did not read, by path.

    🔴 Mirror `M-2`: the census was computed over `expected_output_paths` while the
    exemption was spread over that key **and** `expected_output_prefixes`, so three
    artifacts asserted the unchecked region was one path when it was one path plus a
    prefix. Mirror `M-3`: the repair enumerated three populations out of one skip
    condition and three artifacts then asserted THAT was the whole of it, while a
    declared scan-exempt input, a file with a non-text suffix and a text-suffixed file
    that does not decode were skipped and named by nothing. A derived number inherits
    the incompleteness of its inputs and looks authoritative while doing it — twice.

    So it is no longer derived here at all. The classes are `SCAN_SKIP_CLASSES` and the
    predicate is `scan_skip_reason()`, the same call the scan loop makes; a file is in
    this census exactly when the scan skipped it. There is no third class because there
    is no second implementation.

    Enumerated from the tree at run time, not from the spec, because what is exposed is
    what is *there*.
    """
    census: dict[str, list[str]] = {name: [] for name in SCAN_SKIP_CLASSES}
    for path in iter_files(root):
        rel = str(path.relative_to(root))
        reason = scan_skip_reason(rel, spec, path, post_read)
        if reason is not None:
            census[reason].append(rel)
    return {key: sorted(value) for key, value in census.items()}


def surface_root(out_root: Path, benchmark_id: str, actor: str) -> Path:
    return out_root / benchmark_id / actor


def cmd_build(args: argparse.Namespace) -> int:
    spec = load_spec(Path(args.spec))
    source_root = Path(args.source_root).resolve()
    out_root = Path(args.out).resolve()
    if not source_root.is_dir():
        refuse(f"REFUSE: source root is not a directory: {source_root}")

    common = _entries(spec, "common_files") + _entries(spec, "source_files")
    findings: list[str] = []
    built: dict[str, dict[str, str]] = {}

    for actor in spec["actors"]:
        root = surface_root(out_root, spec["benchmark_id"], actor)
        if root.exists():
            if not args.force:
                refuse(f"REFUSE: surface already exists: {root} (use --force to rebuild)")
            shutil.rmtree(root)
        root.mkdir(parents=True)

        per_actor = spec["per_actor_files"].get(actor)
        if per_actor is None:
            refuse(f"REFUSE: spec has no per_actor_files entry for actor {actor!r}")

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
        refuse(f"REFUSE: parity is defined over exactly two surfaces; spec declares {len(actors)}")

    # 🔴 EXACTLY TWO, by design and not by accident. Parity, "NOT DIFFERING" and the per-actor
    # comparison are all binary relations here. A three-arm benchmark is a tool change, not a
    # spec change, and this refusal is where that cost is declared rather than discovered
    # (Mirror R-7).
    roots = {actor: surface_root(out_root, spec["benchmark_id"], actor) for actor in actors}
    for actor, root in roots.items():
        if not root.is_dir():
            refuse(f"REFUSE: surface not found: {root}")

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
            present = {rel for rel in present
                       if not _is_expected_output(rel, spec, roots[actor] / rel)}
        for rel in sorted(present - allowed[actor]):
            findings.append(f"NOT ALLOWLISTED {actor}  {rel}")

    # 4b · symlinks, at every stage. A link's bytes are somewhere this tool did not look.
    for actor in actors:
        for rel, target in iter_symlinks(roots[actor]):
            findings.append(f"SYMLINK         {actor}  {rel}  →  {target}")

    # 5 · forbidden prior-output paths absent from both surfaces
    #
    # 🔴 ONE forbidden path is genuinely undecidable post-read: the reader's own manifest
    # lands exactly where LEGEND's prior manifest lives, because `deepdive_manifest.py`
    # derives that path from disease and PMID and cannot put it elsewhere without breaking
    # the validator. Authorship is not decidable from a path, so for THAT path — and only
    # that path — the guarantee is carried by the pre-handover run plus the freeze receipt.
    # The set is computed from the spec, printed on every post-read run, and is currently
    # of size one. Every other forbidden path is checked post-read as it is pre-read.
    #
    # This collision is also the sharpest argument for §2.1 of the protocol: in a checkout
    # of the repository, the reader would be writing its manifest on top of the prior one.
    blind = declared_blind_spots(spec)
    for rel in spec["forbidden_prior_output_paths"]:
        if args.post_read and rel in blind:
            continue
        for actor in actors:
            if (roots[actor] / rel).exists() or (roots[actor] / rel).is_symlink():
                findings.append(f"PRIOR OUTPUT    {actor}  {rel}  present in surface")

    # 6 · content scan — the paper's identifiers must not appear in anything that is not
    #     the paper. The packet and the instruction files are exempt by declaration: the
    #     instructions must name the PMID, and the paper is the paper.
    scan = spec["content_scan"]
    pattern = re.compile(scan["pattern"], re.IGNORECASE)
    for actor in actors:
        for path in iter_files(roots[actor]):
            rel = str(path.relative_to(roots[actor]))
            # 🔴 In --post-read the reader's OWN declared outputs name the paper by
            # construction — a manifest must carry the PMID. Scanning them reports a leak
            # on every honest reading, and a check that fires on the correct case is a
            # check people learn to ignore. Found by running this on a synthetic output
            # tree before any reader ever saw the tool. The exemption is the EXACT declared
            # output set, not the whole slot: a file the reader was never asked to write is
            # scanned wherever it sits — and under an output PREFIX it is exempt only if
            # its bytes cannot be decoded at all (Mirror M-2). A render is pixels; a
            # markdown file under output/renders/ is read here like any other.
            #
            # 🔴 The four skip conditions used to be written out here and re-derived,
            # partially, in the census. They are now one call, and every non-None answer
            # is printed by name below (Mirror M-3). Skipping a file silently is no
            # longer expressible: the same predicate decides the skip and the printing.
            if scan_skip_reason(rel, spec, path, args.post_read) is not None:
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="strict")
            except (UnicodeDecodeError, OSError):
                # Unreachable through `scan_skip_reason`, which already answered this
                # question; kept because a file can change between two syscalls and a
                # traceback is a worse answer than a finding.
                findings.append(f"UNREADABLE      {actor}  {rel}  became unreadable "
                                "between the skip decision and the scan")
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
    if args.post_read:
        # 🔴 Two populations, printed separately because they are different objects: what
        # the SPEC declares unchecked, and what is ACTUALLY unchecked in these trees.
        # Revision 2 printed the first alone — the spec-level intersection — and three
        # artifacts then said the unchecked region was that one path. It was that path plus
        # everything a prefix admitted, and nothing printed the second half (Mirror M-2).
        for rel in blind:
            print(f"  [BLIND SPOT] {rel}  — declared: the reader writes here by "
                  "construction; authorship is not decidable from a path post-read")
        if not blind:
            print("  [BLIND SPOT] none declared — no declared reader output path collides "
                  "with a forbidden path")
        # 🔴 Every class of SCAN_SKIP_CLASSES, in one loop, so adding a skip condition to
        # `scan_skip_reason()` without giving it an explanation is a KeyError at the first
        # run rather than a file that quietly stops being printed (Mirror M-3).
        total = 0
        unexpected_skips = 0
        for actor in actors:
            census = unchecked_surface(roots[actor], spec, args.post_read)
            total += sum(len(value) for value in census.values())
            for name, described in SCAN_SKIP_CLASSES.items():
                for rel in census[name]:
                    if not described["expected"]:
                        unexpected_skips += 1
                    print(f"  [UNCHECKED] {actor}  {rel}  — {name}: {described['reason']}; "
                          f"EXPECTED_BY_PROTOCOL "
                          f"{'yes' if described['expected'] else 'NO'}; still covered by "
                          f"{described['still_covered_by']}")
        print(f"  [UNCHECKED SURFACE] {total} present file(s), each named above with the "
              "class and reason its content was not read. Every other present file was "
              "scanned. Each file above still took every check its class does not exempt "
              "it from, and its line says which.")
        if unexpected_skips:
            print(f"  [UNCHECKED SURFACE] {unexpected_skips} of them are NOT a consequence "
                  "the protocol declares — read those lines first.")
    if findings:
        print(f"VERDICT: FAIL — {len(findings)} finding(s). A surface that fails is rebuilt "
              "from the spec, never patched.")
        return 1
    # 🔴 The PASS sentence is the reviewer's evidence, so it states what was CHECKED, not
    # what is true. Every clause here has a probe behind it in test_benchmark_surface.py;
    # the previous sentence claimed "allowlist is exhaustive, no prior output" over a tree
    # whose symlinks nothing had looked at.
    print("VERDICT: PASS — parity holds across the two surfaces; every present file is "
          "allowlisted or is a declared output; no symlink; no forbidden prior-output path "
          "outside the printed blind spot; every present file was either scanned for the "
          "paper's identifiers or printed above under [UNCHECKED] with the reason it was "
          "not, and nothing scanned leaked an identifier.")
    print("  NOT CHECKED, and no clause above implies it: what a reader may open by "
          "absolute path outside this tree (Annex J.0); the authorship of bytes at a "
          "blind-spot path; the content of every file printed above as [UNCHECKED]. "
          "SCANNED and [UNCHECKED] partition the present files — one predicate decides "
          "both, so no present file is skipped by the identifier scan without appearing "
          "in that list, and none appears in it that was scanned.")
    return 0


RECEIPT_SCHEMA_VERSION = 2
FIRST_PASS_STATES = ("COMPLETE_DECLARED_BY_ACTOR", "ABANDONED", "TIMED_OUT")


def _front_matter(path: Path) -> dict[str, str]:
    """The `key: value` block between the first two `---` lines.

    Deliberately not a YAML parser: these blocks are flat scalars, and a dependency the
    surface does not carry is a dependency the freeze cannot rely on.
    """
    if not path.is_file():
        refuse(f"REFUSE: the surface has no {path.name} to read its identity from: {path}")
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if not lines or lines[0].strip() != "---":
        refuse(f"REFUSE: {path.name} has no front matter; identity cannot be verified")
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        key, separator, value = line.partition(":")
        if separator:
            fields[key.strip()] = value.strip()
    refuse(f"REFUSE: {path.name} front matter is unterminated")


def _git(root: Path, *arguments: str) -> str | None:
    try:
        import subprocess
        result = subprocess.run(("git", "-C", str(root)) + arguments,
                                capture_output=True, text=True, timeout=30)
    except (OSError, ImportError):
        return None
    return result.stdout.strip() if result.returncode == 0 else None


def _classify(rel: str, spec: dict[str, Any] | None, actor: str, path: Path) -> str:
    """input / output / unexpected — allowlist first, so scaffolding is not counted as work.

    The `.gitkeep` that holds an empty slot open sits under an output prefix and is
    allowlisted input. Testing the prefix first counted it as a reader's output and made
    OUTPUT_FILE_SET wrong in the one direction nobody would check.

    🔴 It shares `_is_expected_output` with `verify` deliberately, and Mirror `M-2` is why
    that matters: while the prefix admitted anything by position, a smuggled markdown file
    at `output/renders/` was classified `role: "output"` here and left
    `UNEXPECTED_FILE_SET` empty, so the freeze receipt agreed with the verifier about a
    file neither of them had looked at. One predicate, one answer.
    """
    if spec is None:
        return "unclassified"
    if rel in _allowed_paths(spec, actor):
        return "input"
    if _is_expected_output(rel, spec, path):
        return "output"
    return "unexpected"


def cmd_freeze(args: argparse.Namespace) -> int:
    """Bind one first pass to the bytes it consisted of, at the moment it was declared done.

    🔴 Revision 1 of this command recorded `surface` as an ABSOLUTE local path — the very
    `BENCH_ROOT` the protocol says is never written down — and took `--actor-id` and
    `--benchmark-id` as free text: A's tree froze happily as `scientist-b` / `BENCH-XX-999`.
    It emitted no timestamp, no commit, no mode, no input-manifest digest and no first-pass
    state, while §4.3 named it as half of the compensation for a check that cannot see
    authorship. A receipt that is trusted to carry a guarantee has to verify what it says.

    Every identity field below is READ FROM THE TREE — `ASSIGNMENT.md` and the two
    instruction files inside the surface — and the command line is checked AGAINST it, not
    copied into it. A disagreement is a refusal, because a receipt naming the wrong actor
    is worse than no receipt: it is a wrong answer with a digest beside it.
    """
    root = Path(args.surface).resolve()
    if not root.is_dir():
        refuse(f"REFUSE: not a directory: {root}")

    symlinks = iter_symlinks(root)
    if symlinks:
        for rel, target in symlinks:
            print(f"  [BLOCK] SYMLINK  {rel}  →  {target}", file=sys.stderr)
        refuse("REFUSE: the surface holds symlink(s). A freeze must digest bytes that are "
               "here; a link's bytes are somewhere this command did not look.")

    assignment = _front_matter(root / "ASSIGNMENT.md")
    instructions = _front_matter(root / "benchmark" / "BENCHMARK_INSTRUCTIONS.md")
    schema = _front_matter(root / "benchmark" / "OUTPUT_SCHEMA.md")

    for flag, field, source in (("actor_id", "actor_id", "ASSIGNMENT.md"),
                                ("benchmark_id", "benchmark_id", "ASSIGNMENT.md")):
        declared = getattr(args, flag)
        found = assignment.get(field)
        if found is None:
            refuse(f"REFUSE: {source} declares no {field}; identity cannot be verified")
        if declared != found:
            refuse(f"REFUSE: --{flag.replace('_', '-')} is {declared!r}, but {source} inside "
                   f"this surface says {found!r}. The tree decides, and it disagrees.")
    if assignment.get("benchmark_id") != instructions.get("benchmark_id"):
        refuse("REFUSE: ASSIGNMENT.md and BENCHMARK_INSTRUCTIONS.md name different "
               f"benchmarks ({assignment.get('benchmark_id')!r} vs "
               f"{instructions.get('benchmark_id')!r})")
    if args.first_pass_state not in FIRST_PASS_STATES:
        refuse(f"REFUSE: --first-pass-state must be one of {FIRST_PASS_STATES}")

    spec = load_spec(Path(args.spec)) if args.spec else None
    input_manifest = Path(args.input_manifest) if args.input_manifest else None
    if input_manifest is not None and not input_manifest.is_file():
        refuse(f"REFUSE: input manifest not found: {input_manifest}")

    digest, pairs = tree_digest(root)
    actor = assignment["actor_id"]
    files = [{"path": rel, "sha256": sha, "role": _classify(rel, spec, actor, root / rel)}
             for rel, sha in pairs]
    outputs = [entry["path"] for entry in files if entry["role"] == "output"]
    unexpected = [entry["path"] for entry in files if entry["role"] == "unexpected"]

    from datetime import datetime, timezone
    record = {
        "_schema": "LEGEND benchmark · frozen surface receipt",
        "RECEIPT_SCHEMA_VERSION": RECEIPT_SCHEMA_VERSION,

        "BENCHMARK_ID": assignment["benchmark_id"],
        "ACTOR_ID": actor,
        "TASK_ID": assignment.get("task_id"),
        "MODE": assignment.get("mode"),
        "PARALLEL_READ_GROUP": assignment.get("parallel_read_group"),
        "IDENTITY_SOURCE": ("ASSIGNMENT.md inside the frozen tree; the command-line "
                            "--actor-id and --benchmark-id were checked against it and "
                            "agreed. They are not the source."),

        "INSTRUCTIONS_VERSION": instructions.get("instructions_version"),
        "OUTPUT_SCHEMA_VERSION": schema.get("schema_version"),
        "MANIFEST_SCHEMA_VERSION": schema.get("manifest_schema_version"),

        # Surface-relative and nothing more. `<BENCHMARK_ID>/<ACTOR_ID>` is the layout
        # `build` creates; BENCH_ROOT is a local-instance value and is deliberately absent.
        "SURFACE_RELATIVE": f"{assignment['benchmark_id']}/{actor}",
        "SURFACE_ABSOLUTE_PATH": "NOT RECORDED — local-instance value (protocol §2.3)",
        "SURFACE_COMMIT": _git(root, "rev-parse", "HEAD") or "DECLARED_ABSENT — not a git repo",
        "SURFACE_BRANCH": _git(root, "rev-parse", "--abbrev-ref", "HEAD") or "DECLARED_ABSENT",
        "SURFACE_DIRTY": bool(_git(root, "status", "--porcelain")),

        "INPUT_MANIFEST_PATH": str(input_manifest.name) if input_manifest else None,
        "INPUT_MANIFEST_SHA256": sha256_file(input_manifest) if input_manifest else None,

        "FREEZE_TIMESTAMP_UTC": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "FIRST_PASS_STATE": args.first_pass_state,

        "TREE_SHA256": digest,
        "FILE_COUNT": len(pairs),
        "OUTPUT_FILE_SET": sorted(outputs),
        "UNEXPECTED_FILE_SET": sorted(unexpected),
        "SYMLINKS": [],
        "FILES": files,

        "GUARANTEE_PROVIDED": [
            "These bytes, under these paths, were present in this tree when the freeze ran.",
            "Any later addition, removal or edit under the tree is detected by "
            "`verify-freeze`, which recomputes and compares set-wise, not by count.",
            "The actor and benchmark named here were read from inside the tree, so a "
            "receipt cannot be mislabelled by a wrong command line.",
            "The instruction and schema versions the reading ran under are pinned, and the "
            "instruction bytes are covered transitively by TREE_SHA256.",
        ],
        "FAILURE_MODE_STILL_POSSIBLE": [
            "AUTHORSHIP: this cannot show WHO wrote a file, only what was there. A path on "
            "the declared blind-spot list is bytes at a path, nothing more.",
            "TIMING: FREEZE_TIMESTAMP_UTC is this process's clock, attested by nothing "
            "else. It orders the two freezes on one machine; it proves nothing to a party "
            "that does not trust the clock.",
            "ORDER: that the second reader was not shown the first reader's output before "
            "its own freeze is PROCEDURAL (Annex J.0). Nothing here enforces it; the two "
            "receipts and their timestamps make a violation of it visible afterwards.",
            "PRE-FREEZE SUBSTITUTION: a swap made BEFORE the freeze ran is inside the "
            "freeze. Only the pre-handover `verify` run speaks to that end of the window.",
        ],
        "DETECTION": "framework/scripts/benchmark_input_surface.py verify-freeze "
                     "--receipt <this file> --surface <the tree>",
    }
    if args.out:
        Path(args.out).write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        print(f"FROZEN  {actor}  {digest}  {len(pairs)} file(s)  → {args.out}")
        print(f"  mode {record['MODE']}  task {record['TASK_ID']}  "
              f"state {record['FIRST_PASS_STATE']}  at {record['FREEZE_TIMESTAMP_UTC']}")
        print(f"  outputs {len(outputs)}  unexpected {len(unexpected)}")
        if unexpected:
            for rel in sorted(unexpected):
                print(f"  [NOTE] UNEXPECTED FILE  {rel}  — frozen and flagged, not removed")
    else:
        print(json.dumps(record, indent=2))
    return 0


def cmd_verify_freeze(args: argparse.Namespace) -> int:
    """Does the tree still hold exactly what the receipt froze?

    Set-wise, never count-wise. Two trees with the same number of files and different
    files in them is precisely the substitution this exists to catch, and a count says
    they agree. The comparison is therefore ADDED / REMOVED / MODIFIED, each enumerated.
    """
    receipt_path = Path(args.receipt)
    if not receipt_path.is_file():
        refuse(f"REFUSE: receipt not found: {receipt_path}")
    try:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        refuse(f"REFUSE: receipt is not valid JSON: {exc}")
    version = receipt.get("RECEIPT_SCHEMA_VERSION")
    if version != RECEIPT_SCHEMA_VERSION:
        refuse(f"REFUSE: receipt schema version {version!r}; this tool speaks "
               f"{RECEIPT_SCHEMA_VERSION}")
    root = Path(args.surface).resolve()
    if not root.is_dir():
        refuse(f"REFUSE: not a directory: {root}")

    findings: list[str] = []
    for rel, target in iter_symlinks(root):
        findings.append(f"SYMLINK APPEARED  {rel}  →  {target}")

    frozen = {entry["path"]: entry["sha256"] for entry in receipt["FILES"]}
    digest, pairs = tree_digest(root)
    present = dict(pairs)

    for rel in sorted(set(present) - set(frozen)):
        findings.append(f"ADDED             {rel}  {present[rel][:16]}…")
    for rel in sorted(set(frozen) - set(present)):
        findings.append(f"REMOVED           {rel}  was {frozen[rel][:16]}…")
    for rel in sorted(set(frozen) & set(present)):
        if frozen[rel] != present[rel]:
            findings.append(f"MODIFIED          {rel}  "
                            f"was {frozen[rel][:16]}…  now {present[rel][:16]}…")

    # The identity the receipt asserts must still be the identity the tree asserts. A
    # substitution that swapped ASSIGNMENT.md would already show as MODIFIED; this catches
    # the case where a receipt is pointed at a DIFFERENT actor's tree entirely.
    assignment = root / "ASSIGNMENT.md"
    if assignment.is_file():
        found = _front_matter(assignment)
        for field, key in (("actor_id", "ACTOR_ID"), ("benchmark_id", "BENCHMARK_ID")):
            if found.get(field) != receipt.get(key):
                findings.append(f"IDENTITY MISMATCH {key}: receipt {receipt.get(key)!r}, "
                                f"tree {found.get(field)!r}")
    else:
        findings.append("IDENTITY MISMATCH ASSIGNMENT.md absent from the tree")

    for item in findings:
        print(f"  [BLOCK] {item}")
    print(f"  receipt {receipt['ACTOR_ID']} · {receipt['BENCHMARK_ID']} · "
          f"frozen {receipt['FREEZE_TIMESTAMP_UTC']} · state {receipt['FIRST_PASS_STATE']}")
    print(f"  frozen tree_sha256 {receipt['TREE_SHA256']}  {receipt['FILE_COUNT']} file(s)")
    print(f"  present tree_sha256 {digest}  {len(pairs)} file(s)")
    if findings:
        print(f"VERDICT: FAIL — {len(findings)} difference(s) from the frozen tree. The "
              "comparison is against the frozen objects, so this is what the evaluation "
              "must be told it is reading.")
        return 1
    if digest != receipt["TREE_SHA256"]:
        # Belt and braces: the per-file comparison found nothing, so a digest disagreement
        # would mean the digest function itself changed under us. Say that, rather than
        # printing PASS over a number that does not match.
        print("VERDICT: FAIL — every file matches but the tree digest does not. The digest "
              "function is not the one that produced this receipt.")
        return 1
    print("VERDICT: PASS — the tree holds exactly the frozen file set, byte for byte, and "
          "still names the actor and benchmark the receipt does.")
    return 0


def _pdf_pages(path: Path) -> list[str]:
    try:
        import fitz  # type: ignore
    except ImportError:
        refuse("REFUSE: PyMuPDF is required to enumerate units from a PDF artifact")
    with fitz.open(str(path)) as doc:
        return [page.get_text() for page in doc]


def _pdf_lines(path: Path) -> list[dict[str, Any]]:
    """Every typographic line of a PDF, in reading order, with font, size and centre.

    The flattened text of this paper does not mark its own structure: a Methods heading
    is not bounded by a blank line, is not punctuated, and is not distinguishable from
    the sentence under it by any character. It IS distinguishable by font and size, and
    a table's merged category row is distinguishable from a column cell by being centred
    where the column cell is not. Reading those properties off the source is what makes
    the enumeration a function of (spec, source) in more than the trivial sense (R-6).
    """
    try:
        import fitz  # type: ignore
    except ImportError:
        refuse("REFUSE: PyMuPDF is required to enumerate units from a PDF artifact")
    lines: list[dict[str, Any]] = []
    with fitz.open(str(path)) as doc:
        for number, page in enumerate(doc, 1):
            for block in page.get_text("dict")["blocks"]:
                for line in block.get("lines", []):
                    # 🔴 Whitespace-only spans are dropped BEFORE any style test. A heading
                    # line in File009 ends in a plain-roman space span, and an "every span
                    # is bold" test that counted it rejected two real Methods headings —
                    # including the ChIP-seq analysis section this population was missing.
                    spans = [s for s in line.get("spans", []) if s["text"].strip()]
                    if not spans:
                        continue
                    text = " ".join("".join(s["text"] for s in spans).split())
                    x0 = min(span["bbox"][0] for span in spans)
                    x1 = max(span["bbox"][2] for span in spans)
                    lines.append({
                        "page": number,
                        "text": text,
                        "fonts": sorted({span["font"] for span in spans}),
                        "size": max(span["size"] for span in spans),
                        "center_x": (x0 + x1) / 2,
                    })
    return lines


def _matches_style(line: dict[str, Any], style: dict[str, Any]) -> bool:
    """Does one typographic line carry the declared style?

    Every criterion is optional; every criterion that IS declared must hold.
    `font_contains` is a substring test over every font on the line, so a line mixing
    faces fails it — which is the point: a heading is set in one face.
    """
    needle = style.get("font_contains")
    if needle is not None and not all(needle in font for font in line["fonts"]):
        return False
    size = style.get("size")
    if size is not None and abs(line["size"] - size) > style.get("size_tolerance", 0.05):
        return False
    center = style.get("center_x")
    if center is not None and abs(line["center_x"] - center) > style.get(
            "center_tolerance", 2.0):
        return False
    if line["page"] < style.get("page_from", 1):
        return False
    text = style.get("text")
    if text is not None and line["text"].rstrip(" .") != text:
        return False
    text_pattern = style.get("text_pattern")
    if text_pattern is not None and not re.search(text_pattern, line["text"]):
        return False
    return True


def _scope_slice(lines: list[dict[str, Any]], scope: dict[str, Any]) -> list[dict[str, Any]]:
    """Restrict the line stream to the region a rule declares it measures.

    `start_after` and `stop_before` are themselves styles, matched against the same
    stream. That is what keeps a Results-subsection rule out of Discussion and a Methods
    rule out of the reference list — two failure modes a bare size filter cannot refuse.
    A boundary marker that never matches is a REFUSAL, not an empty result: silently
    measuring the whole document is exactly the kind of wrong denominator this repairs.
    """
    start = 0
    after = scope.get("start_after")
    if after is not None:
        start = None
        for index, line in enumerate(lines):
            if _matches_style(line, after):
                start = index + 1
                break
        if start is None:
            refuse(f"REFUSE: population scope start_after never matched: {after!r}")
    stop = len(lines)
    before = scope.get("stop_before")
    if before is not None:
        stop = None
        for index in range(start, len(lines)):
            if _matches_style(lines[index], before):
                stop = index
                break
        if stop is None:
            refuse(f"REFUSE: population scope stop_before never matched: {before!r}")
    return lines[start:stop]


def _typography_units(lines: list[dict[str, Any]], rule: dict[str, Any],
                      artifact: str) -> list[dict[str, Any]]:
    """Units whose boundary in the source is typographic, not lexical."""
    scoped = _scope_slice(lines, rule.get("scope", {}))
    # 🔴 Adjacency is tested on a stream with the declared furniture removed first. This
    # manuscript numbers its lines in the margin, and each number is a text line of its
    # own sitting BETWEEN the two halves of a wrapped heading. Testing adjacency on the
    # raw stream, four wrapped Results headings came back as eight sections — a
    # denominator inflated by a typesetting artefact, which is the same class of error
    # as the phantom panels, arriving from the other direction.
    ignore = rule.get("join_wrapped_ignore")
    stream = ([line for line in scoped if not _matches_style(line, ignore)]
              if ignore else scoped)
    selected = [(index, line) for index, line in enumerate(stream)
                if _matches_style(line, rule["heading"])]
    excluded = set(rule.get("exclude_labels", []))

    groups: list[list[dict[str, Any]]] = []
    previous = None
    for index, line in selected:
        # 🔴 A heading too long for its column wraps onto the next line and is still ONE
        # heading. Consecutive selected lines — nothing of body style between them — join.
        # A blank-line or lexical rule cannot see this and drops the wrapped section
        # entirely; that is one of the four sections this enumeration recovers over the
        # hand-written list it replaces.
        if rule.get("join_wrapped") and previous is not None and index == previous + 1:
            groups[-1].append(line)
        else:
            groups.append([line])
        previous = index

    units = []
    for group in groups:
        label = " ".join(" ".join(line["text"] for line in group).split()).rstrip(" .")
        if label in excluded:
            continue
        units.append({
            "unit_id": f"{rule['kind']}:{label}",
            "kind": rule["kind"],
            "label": label,
            "artifact": artifact,
            "locus": f"p{group[0]['page']}",
        })
    return units


def _regex_units(segments: list[tuple[Any, str]], rule: dict[str, Any],
                 artifact: str) -> list[dict[str, Any]]:
    """Units whose extent runs to the next occurrence of their own label.

    🔴 The window is bounded by the NEXT MATCH OF THIS RULE, or by the end of the
    segment — never by a character count. A fixed window is a bound on the wrong axis:
    the axis a caption window fails on is *does it respect the next label*, and no
    integer bounds that. Measured on this paper, a 3600-character window ran 925
    characters past Figure 2's caption into Figure 3's and reported twelve panels for a
    caption that prints six — six units no locator could ever anchor.
    """
    pattern = re.compile(rule["pattern"], re.MULTILINE)
    sub_pattern = (re.compile(rule["sub_unit_pattern"])
                   if rule.get("sub_unit_pattern") else None)
    range_pattern = (re.compile(rule["sub_unit_range_pattern"])
                     if rule.get("sub_unit_range_pattern") else None)
    seen: set[str] = set()
    units = []
    for locus, text in segments:
        matches = list(pattern.finditer(text))
        for index, match in enumerate(matches):
            label = " ".join(match.group("label").split())
            bound = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            if label in seen:
                # A repeated label is one unit met twice — this paper reprints every figure
                # label in a trailing size listing. The FIRST occurrence is the caption and
                # is kept; the repeat is skipped only AFTER it has served as the bound of
                # its predecessor, which is why `bound` is computed above this test.
                continue
            seen.add(label)
            unit = {
                "unit_id": f"{rule['kind']}:{label}",
                "kind": rule["kind"],
                "label": label,
                "artifact": artifact,
                "locus": (locus if locus is not None
                          else f"l{text.count(chr(10), 0, match.start()) + 1}"),
            }
            if sub_pattern is not None:
                window = text[match.end():bound]
                found = {m.group(1) for m in sub_pattern.finditer(window)}
                # 🔴 A caption may label a range — `(C-D)` — and a pattern reading only
                # single letters silently drops every panel inside one. Measured here:
                # Figure 6 reported A,B,E and contains A,B,C,D,E. A short denominator
                # flatters both readers, so ranges are expanded, never approximated.
                if range_pattern is not None:
                    for m in range_pattern.finditer(window):
                        start, stop = ord(m.group(1)), ord(m.group(2))
                        if start <= stop:
                            found.update(chr(code) for code in range(start, stop + 1))
                unit["sub_unit_kind"] = rule.get("sub_unit_kind", "panel")
                unit["sub_units"] = sorted(found)
                unit["window_chars"] = len(window)
            units.append(unit)
    return units


def cmd_population(args: argparse.Namespace) -> int:
    """Enumerate structural evidence units, by declared rule, before anyone reads.

    Structural enumeration is not a reading: it lists what the paper CONTAINS — figures,
    their lettered panels, tables, Results subsections, Methods sections, source-data
    panels — and says nothing about what any of it shows. That is why Plan may run it
    without crossing the epistemic boundary (body §28), and why it must be right before
    the readings exist: a denominator chosen afterwards is a denominator chosen to fit.

    Two extractors, because this source marks its units two different ways:

      `regex`       the unit announces itself with a label in the text, and its extent
                    runs to the next such label or to the end of the segment
      `typography`  the unit announces itself with a font, a size or a position, and its
                    extent is a region declared by two typographic boundary markers

    Every packet source must be classified — including one that yields NO units.
    `declared_empty_sources` is not a courtesy: an unlisted source is an unmeasured one,
    and this command refuses a spec that leaves any source unaccounted for.
    """
    spec = load_spec(Path(args.spec))
    population_spec = spec.get("population")
    if population_spec is None:
        refuse("REFUSE: spec has no `population` block")
    source_root = Path(args.source_root).resolve()

    units: list[dict[str, Any]] = []
    for source in population_spec["sources"]:
        path = source_root / source["source"]
        if not path.is_file():
            refuse(f"REFUSE: population source missing: {path}")
        artifact = source["surface"]
        extraction = source.get("extraction", "regex")

        if extraction == "typography":
            lines = _pdf_lines(path)
            for rule in source["rules"]:
                units.extend(_typography_units(lines, rule, artifact))
        elif extraction == "regex":
            # 🔴 One segment per PAGE for a PDF, ONE segment for a whole text file — never
            # one per line. A caption window that stops at the end of the line its label
            # sits on finds the first panel and no other: measured on this paper, per-line
            # segmentation reported 1 panel for a six-panel figure.
            if path.suffix.lower() == ".pdf":
                segments = [(f"p{i + 1}", text) for i, text in enumerate(_pdf_pages(path))]
            else:
                segments = [(None, path.read_text(encoding="utf-8", errors="replace"))]
            for rule in source["rules"]:
                units.extend(_regex_units(segments, rule, artifact))
        else:
            refuse(f"REFUSE: unknown extraction {extraction!r} for {source['source']}")

    # Completeness against the packet: every article and supplement handed to the readers
    # either produces units or is declared to produce none, with its reason. A source
    # silently absent from this block is coverage nobody can measure and nobody was told
    # was unmeasurable — which is what §8.1 promised and the spec did not deliver.
    declared_empty = {entry["source"]: entry["reason"]
                      for entry in population_spec.get("declared_empty_sources", [])}
    enumerated = {source["source"] for source in population_spec["sources"]}
    packet = {entry["source"] for entry in _entries(spec, "source_files")}
    findings = [f"UNACCOUNTED SOURCE    {item}"
                for item in sorted(packet - enumerated - set(declared_empty))]
    findings += [f"DOUBLE-DECLARED SOURCE {item}"
                 for item in sorted(set(declared_empty) & enumerated)]
    if findings:
        for item in findings:
            print(f"  [BLOCK] {item}")
        print("VERDICT: FAIL — a packet source is neither enumerated nor declared empty, "
              "or is both. Coverage over it would be unmeasurable and unstated.")
        return 1

    units.sort(key=lambda item: (item["kind"], item["label"]))
    sub_unit_total = sum(len(unit.get("sub_units", [])) for unit in units)
    panel_units = sum(len(unit.get("sub_units", []))
                      for unit in units if unit.get("sub_unit_kind") == "panel")
    # 🔴 Every DECLARED kind appears in the count, including one that measured zero. A
    # by_kind built only from the units found cannot distinguish "the rule ran and the
    # paper has none" from "no rule was ever written" — and those are the two halves of
    # B-1. `main_table: 0` is a measurement; its absence would be an omission.
    declared_kinds = {rule["kind"] for source in population_spec["sources"]
                      for rule in source["rules"]}
    by_kind = {kind: 0 for kind in sorted(declared_kinds)}
    for unit in units:
        by_kind[unit["kind"]] = by_kind.get(unit["kind"], 0) + 1
    record = {
        "_schema": "LEGEND benchmark · evaluation population v2",
        "benchmark_id": spec["benchmark_id"],
        "pmid": spec.get("pmid"),
        "derivation": ("framework/scripts/benchmark_input_surface.py population "
                       "--spec <spec> --source-root <root>"),
        "note": ("Structural enumeration only. It lists what the paper contains, never what "
                 "any unit shows, and it does NOT rank units by importance — which of them "
                 "matter is exactly what the readings and the adjudication are for."),
        # Carried verbatim from the spec: caption anomalies and extraction limits observed
        # when the population was derived. They belong beside the numbers, not in a
        # separate file a reader of the numbers never opens.
        "declared_notes": population_spec.get("notes", []),
        "declared_empty_sources": population_spec.get("declared_empty_sources", []),
        "counts": {"units": len(units), "sub_units": sub_unit_total, "panels": panel_units,
                   "by_kind": dict(sorted(by_kind.items()))},
        "units": units,
    }
    if args.out:
        Path(args.out).write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        print(f"POPULATION  {len(units)} unit(s), {panel_units} panel(s), "
              f"{sub_unit_total} sub-unit(s) → {args.out}")
        for kind, count in record["counts"]["by_kind"].items():
            print(f"  {kind:28s} {count}")
        for entry in record["declared_empty_sources"]:
            print(f"  DECLARED EMPTY  {entry['source']}  — {entry['reason']}")
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

    🔴 Three ways a citation used to walk straight through this check, all of them found by
    taking its PASS sentence — *"every cited artifact is inside the surface"* — literally
    and building the cheapest state that makes it false:

      * a forbidden prior-output path that happens to sit UNDER an output slot. LEGEND's
        own dossier lives at `…/fulltext_dossiers/PMID42397075_partial_locators.md`, which
        starts with an admitted prefix, so "produced in the surface" admitted it verbatim —
        at exactly the path the repository always cites it by;
      * `output/../../../…` — a prefix test is a string test, and `..` satisfies it while
        pointing anywhere on the machine;
      * an absolute path was caught, but only because it failed the prefix test by luck.

    So: normalize first, refuse traversal and absolute paths outright, and check the
    forbidden set BEFORE the prefix, never after.
    """
    spec = load_spec(Path(args.spec))
    root = Path(args.surface).resolve()
    manifest_path = (root / "disease-models" / args.disease / "research" / "deepdive_manifests"
                     / f"PMID{args.pmid}.json")
    if not manifest_path.is_file():
        refuse(f"REFUSE: no manifest at {manifest_path}")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        refuse(f"REFUSE: manifest is not valid JSON: {exc}")

    allowed = _allowed_paths(spec, args.actor_id)
    forbidden = set(spec["forbidden_prior_output_paths"])
    produced = tuple(f"{rel}/" for rel in spec["empty_dirs"])
    findings: list[str] = []

    def check(path_value: str, where: str) -> None:
        raw = path_value.strip()
        if not raw:
            findings.append(f"EMPTY PATH       {where}")
            return
        if posixpath.isabs(raw) or re.match(r"^[A-Za-z]:[\\/]", raw):
            findings.append(f"ABSOLUTE PATH    {where}  {raw}")
            return
        normalized = posixpath.normpath(raw.replace("\\", "/"))
        if normalized == ".." or normalized.startswith("../"):
            findings.append(f"TRAVERSAL        {where}  {raw}  → {normalized}")
            return
        if raw != normalized:
            # Not fatal on its own, but a citation that needed normalizing is a citation
            # whose literal form does not name the file it resolves to. Say so, then judge
            # the resolved form.
            findings.append(f"NON-CANONICAL    {where}  {raw}  → {normalized}")
        # The forbidden set is checked BEFORE the produced-prefix, and independently of it.
        # Provenance, not position: a path on this list is prior LEGEND output wherever it
        # is found, including inside a slot the reader legitimately writes to.
        if normalized in forbidden:
            findings.append(f"FORBIDDEN SOURCE {where}  {normalized}  "
                            "(prior LEGEND output, cited by path)")
            return
        if normalized in allowed or normalized.startswith(produced):
            return
        findings.append(f"OUTSIDE SURFACE  {where}  {normalized}")

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
    print("VERDICT: PASS — every cited path is relative, free of traversal, not on the "
          "forbidden prior-output list, and either allowlisted or written into an output "
          "slot of this surface.")
    print("  NOT CHECKED: that the reader actually opened only what it cited (Annex J.0); "
          "a citation is a declaration, and this reads the declaration.")
    return 0


def cmd_tree_digest(args: argparse.Namespace) -> int:
    root = Path(args.path).resolve()
    if not root.is_dir():
        refuse(f"REFUSE: not a directory: {root}")
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

    freeze = sub.add_parser(
        "freeze", help="bind one first pass to its bytes; identity verified from the tree")
    freeze.add_argument("--surface", required=True)
    freeze.add_argument("--actor-id", required=True,
                        help="checked against ASSIGNMENT.md in the tree; a disagreement refuses")
    freeze.add_argument("--benchmark-id", required=True,
                        help="checked against ASSIGNMENT.md in the tree; a disagreement refuses")
    freeze.add_argument("--first-pass-state", default="COMPLETE_DECLARED_BY_ACTOR",
                        choices=list(FIRST_PASS_STATES))
    freeze.add_argument("--spec", help="classify each frozen file as input / output / unexpected")
    freeze.add_argument("--input-manifest", help="the benchmark manifest the run was handed")
    freeze.add_argument("--out")
    freeze.set_defaults(func=cmd_freeze)

    verify_freeze = sub.add_parser(
        "verify-freeze", help="does the tree still hold exactly what the receipt froze?")
    verify_freeze.add_argument("--receipt", required=True)
    verify_freeze.add_argument("--surface", required=True)
    verify_freeze.set_defaults(func=cmd_verify_freeze)

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
