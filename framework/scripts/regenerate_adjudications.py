#!/usr/bin/env python3
"""Regenerate page-adjudication crops from the source PDF, and verify them by digest.

## Why the images are not in this repository

A page adjudication reproduces the author's printed characters — that is precisely what
makes it evidence, and precisely why it cannot be redistributed. `PMID 17803050` carries
`Copyright 2007 by the American Association for Laboratory Animal Science`, has no DOI, no
PMCID and no open deposit, and the crops cover substantial portions of the printed page.

So this repository publishes the **recipe**, not the reproduction: source PDF digest, page,
crop rectangle in PDF points, dpi, and the SHA-256 of the resulting image. A reader holding
their own copy of the PDF regenerates the identical bytes and verifies the digest. Nothing
is lost — the verification is exactly as strong — and nothing copyrighted is republished.

It is the same rule the rest of the state already follows: `files/` is gitignored while
every artifact in it is fingerprinted. Page adjudications were the one place doing the
opposite.

## Why each locator carries a needle

`adjudicates: ["entries[10]"]` is a promise: it asserts that a crop shows a locator without
giving anything a command can check. The needle is the search string that resolves the
locator to a span on the printed page, which closes the chain — **needle → span → span
inside crop → crop → digest** — and makes the whole recipe verifiable end to end rather than
by eye. Two conditions, both arithmetic once the needle exists:

- the needle occurs **exactly once** on its page. A fragment that matches twice does not
  identify a location; this repository learned that three times in one day;
- the needle is a fragment of the **snippet of the locator it names**, which is what stops a
  needle from drifting to a neighbouring sentence that happens to sit in the same crop.

Where a locator quotes a table row, the row is not contiguous in the text layer — the columns
are separate runs — so the needle is the row label, or the one cell value unique on the page.

## Usage

    regenerate_adjudications.py verify [--pmid 17803050]   # digests must match; default
    regenerate_adjudications.py write  [--pmid 17803050]   # (re)create the local images

`verify` is the gate: it fails closed when a digest disagrees, when the PDF is absent, or
when the PDF itself is not the one the recipe was taken from.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from deepdive_manifest import _match_key  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
ADJUDICATIONS = ROOT / "disease-models/wwox/research/page_adjudications"
LOCATOR = re.compile(r"^entries\[(\d+)\]$")


def span_is_fully_shown(
    crop: tuple[float, float, float, float],
    span: tuple[float, float, float, float],
) -> bool:
    """Is the whole span visible inside the crop? Answered by area, not by edges.

    🔴 This is `deepdive_manifest.crop_contains_span` answered a second time, on purpose.
    Until 2026-08-11 this module IMPORTED that function, so its verdict — *«the locators
    resolve to spans the crop actually shows»* — was produced by the code a validator was
    trusting it to corroborate. A guard sharing a code path with its subject is not a guard,
    it is an echo, and a defect in the matching would have been invisible to the check built
    to confirm it. The digest half was always genuinely independent; this half was not.

    A second copy of the same four comparisons would be an echo too, just spelled differently.
    So the question is asked in a different shape: **clip the span to the crop and require the
    clipped area to equal the span's area.** Same predicate, different arithmetic — comparison
    of coordinates versus multiplication of overlaps — so the two disagree when either is
    wrong rather than agreeing because they are the same sentence twice.

    Edges count as shown, matching the other implementation: a span flush against the boundary
    is fully rendered, and being strict by a hair would reject correct artifacts and teach
    people to pad crops until the check stops complaining.

    A zero-area span — a needle resolving to an empty rectangle — is contained by this
    formulation whenever it lies inside, which is what the other implementation says too.
    """
    crop_x0, crop_y0, crop_x1, crop_y1 = crop
    span_x0, span_y0, span_x1, span_y1 = span
    span_area = max(0.0, span_x1 - span_x0) * max(0.0, span_y1 - span_y0)
    clipped_area = (
        max(0.0, min(crop_x1, span_x1) - max(crop_x0, span_x0))
        * max(0.0, min(crop_y1, span_y1) - max(crop_y0, span_y0))
    )
    if span_area == 0.0:
        # Degenerate span: area says nothing, so fall back to the point being inside.
        return (crop_x0 <= span_x0 and span_x1 <= crop_x1
                and crop_y0 <= span_y0 and span_y1 <= crop_y1)
    return clipped_area == span_area


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def manifest_state(recipe: dict) -> tuple[str, list[str] | None]:
    """Which of the three manifest states this recipe is in, and the snippets if any.

    🔴 Three, not two. The predecessor returned `None` both for *the recipe names no
    manifest* and for *the recipe names one that is not there*, and the caller printed
    "no manifest declared" for both. A one-character typo in a path therefore retired the
    locator-to-snippet check and announced it as the author's decision. The states are:

        NONE        the recipe declares no manifest — a real, allowed configuration
        UNREADABLE  it declares one that is missing or malformed — always a defect
        OK          it declares one and it loaded

    Distinguishing them costs one return value and is the difference between a skipped
    check and a silently skipped check.
    """
    relative = recipe.get("manifest")
    if not relative:
        return "NONE", None
    path = ROOT / relative
    if not path.exists():
        return "UNREADABLE", None
    try:
        entries = json.loads(path.read_text(encoding="utf-8"))["verbatim_locators"]["entries"]
    except (json.JSONDecodeError, KeyError, TypeError):
        return "UNREADABLE", None
    return "OK", [str(entry.get("snippet", "")) for entry in entries]


def check_needles(page, artifact: dict, quoted: list[str] | None,
                  label: str) -> tuple[list[str], int, int]:
    """Does each declared needle resolve, uniquely, to a span the crop actually shows?

    Returns `(problems, resolved, checked_against_manifest)`. The two counts are returned
    rather than inferred by the caller from `len(adjudicates)`: the caller cannot see which
    adjudications took an early `continue`, and inferring the count from the declaration is
    exactly how a summary comes to report work that did not happen.
    """
    problems: list[str] = []
    resolved = 0
    against_manifest = 0
    crop = tuple(artifact["crop"])

    for adjudication in artifact["adjudicates"]:
        if not isinstance(adjudication, dict):
            problems.append(
                f"{label}: {adjudication!r} is a bare locator. Every adjudication declares "
                f"the needle that resolves it on the page, so the recipe can be checked "
                f"rather than believed")
            continue

        locator = str(adjudication.get("locator", ""))
        needle = str(adjudication.get("needle", ""))
        if not locator or not needle:
            problems.append(f"{label}: adjudication {adjudication!r} lacks locator or needle")
            continue

        hits = page.search_for(needle)
        if len(hits) != 1:
            problems.append(
                f"{label} {locator}: needle {needle!r} matches {len(hits)} span(s) on page "
                f"{artifact['page']}; a needle that is not unique does not identify a location")
            continue

        span = (hits[0].x0, hits[0].y0, hits[0].x1, hits[0].y1)
        if not span_is_fully_shown(crop, span):
            problems.append(
                f"{label} {locator}: crop {crop} does not contain the span "
                f"({span[0]:.0f},{span[1]:.0f},{span[2]:.0f},{span[3]:.0f}) it adjudicates")
            continue

        resolved += 1

        if quoted is None:
            continue
        match = LOCATOR.match(locator)
        if not match or int(match.group(1)) >= len(quoted):
            problems.append(f"{label} {locator}: no such locator in the manifest")
            continue
        # Folding to alphanumerics is the right strength here and the wrong strength for a
        # quote: it is asking whether the needle belongs to this locator, not whether the
        # page says what the snippet says. The crop answers that, by being read.
        if _match_key(needle) not in _match_key(quoted[int(match.group(1))]):
            problems.append(
                f"{label} {locator}: needle {needle!r} is not a fragment of the snippet it "
                f"claims to adjudicate")
            continue
        against_manifest += 1

    return problems, resolved, against_manifest


class RecipeError(RuntimeError):
    """A recipe file cannot be read as a recipe. A verdict, never a traceback.

    🔴 A malformed recipe used to reach the caller as `KeyError: 'artifacts'` or a
    `JSONDecodeError`. It exited 1, so it failed closed — but a traceback is not a verdict: a
    consumer cannot tell it from the tool crashing, and neither can a reader. The gate says
    what is wrong with the recipe, or it is not the gate saying anything.
    """


REQUIRED_RECIPE_KEYS = ("source_pdf", "artifacts")


def recipes() -> list[tuple[Path, dict]]:
    found = []
    for path in sorted(ADJUDICATIONS.glob("*/adjudications.json")):
        relative = path.relative_to(ROOT)
        try:
            recipe = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise RecipeError(f"{relative}: not valid JSON — {exc}") from exc
        if not isinstance(recipe, dict):
            raise RecipeError(
                f"{relative}: top level is a {type(recipe).__name__}, not an object")
        missing = [k for k in REQUIRED_RECIPE_KEYS if k not in recipe]
        if missing:
            raise RecipeError(f"{relative}: recipe declares no {', '.join(missing)}")
        if not isinstance(recipe["artifacts"], list):
            raise RecipeError(
                f"{relative}: artifacts is a {type(recipe['artifacts']).__name__}, not a list")
        check_output_names(recipe["artifacts"], relative)
        found.append((path.parent, recipe))
    return found


def check_output_names(artifacts: list, relative: Path) -> None:
    """`file` must be a plain name, unique within the recipe. Raise otherwise.

    🔴 IN SCOPE, and the reason is not directory hygiene. This tool's declared contract is
    RECIPE REGENERATION — *"fails closed when a digest disagrees, when the PDF is absent, or
    when the PDF itself is not the one the recipe was taken from"* — and the test for whether
    a defect belongs to that contract is whether it can **corrupt another declared
    regeneration**. All three of these can:

    * **duplicate targets.** Two artifacts naming `a.png` both write it; the second overwrites
      the first. Measured: `artifact[0]` declares `f495b656…`, `artifact[1]` declares
      `6abfb6f0…`, and `a.png` on disk holds `6abfb6f0…`. **One declared regeneration was
      destroyed by another**, and `verify` exits 0 with a clean summary because it re-renders
      from the PDF and never reads the disk;
    * **traversal.** `"../../../../ESCAPED.png"` under
      `disease-models/wwox/research/page_adjudications/PMID99999999/` resolved to
      `disease-models/ESCAPED.png` — outside the adjudication directory, inside the repository,
      where it can overwrite a tracked file;
    * **an absolute path.** `Path(directory) / "/tmp/x.png"` is `/tmp/x.png` in pathlib, so
      `write` left a file entirely outside the repository. Measured, not reasoned.

    **A zero-area crop is deliberately NOT handled here**: it is already refused, by geometry —
    `crop (100,100,100,100) does not contain the span (72,87,154,104) it adjudicates`. Patching
    every mutation someone can name would widen the contract past what the tool promises; this
    one is out of scope **and correctly ignored**, which is a different verdict from out of
    scope and silent.
    """
    seen: dict[str, int] = {}
    for index, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            raise RecipeError(f"{relative}: artifacts[{index}] is not an object")
        name = artifact.get("file")
        if not isinstance(name, str) or not name:
            raise RecipeError(f"{relative}: artifacts[{index}] declares no file name")
        if name != Path(name).name or name in (".", ".."):
            raise RecipeError(
                f"{relative}: artifacts[{index}] file {name!r} is not a plain name. An output "
                f"path that leaves its own directory can overwrite another artifact, or a "
                f"tracked file, or a file outside the repository")
        if name in seen:
            raise RecipeError(
                f"{relative}: artifacts[{index}] and artifacts[{seen[name]}] both write "
                f"{name!r}; one regeneration would silently destroy the other")
        seen[name] = index


IMAGE_SUFFIXES = frozenset({".png", ".jpg", ".jpeg", ".tif", ".tiff"})


def observe_directories() -> dict[str, list[str]]:
    """What is on disk under `page_adjudications/`, beside what the recipes declare.

    🔴 This exists because three different degraded states produced a summary **byte-identical
    to a clean run** — same text, same exit 0:

        a declared PNG replaced with 16 bytes of garbage
        an undeclared PNG sitting in an adjudicated directory
        a whole study directory with images, a README, and no `adjudications.json`

    `verify` re-renders from the PDF and compares to the recipe, so it never opens the file on
    disk and never looks at the directory at all. That is **correct for what it promises** —
    its own docstring says it fails closed on a digest disagreement, an absent PDF, or the wrong
    PDF, and rule 5e governs what is *published*, while these images are gitignored and are not.

    So nothing here is made to fail. What changes is that the summary can no longer claim, in
    the same words, both "everything was verified" and "there is material here I never looked
    at". **A gate is not required to check everything; it is required not to be silent about
    what it did not check.**
    """
    observed: dict[str, list[str]] = {"undeclared": [], "unrecipe_directories": [],
                                      "declared_absent": [], "declared_stale": []}
    if not ADJUDICATIONS.is_dir():
        return observed

    for directory in sorted(p for p in ADJUDICATIONS.iterdir() if p.is_dir()):
        recipe_path = directory / "adjudications.json"
        images = sorted(p for p in directory.iterdir()
                        if p.suffix.lower() in IMAGE_SUFFIXES)
        if not recipe_path.is_file():
            if images:
                observed["unrecipe_directories"].append(
                    f"{directory.name} ({len(images)} image file(s), no adjudications.json)")
            continue
        try:
            artifacts = json.loads(recipe_path.read_text(encoding="utf-8")).get("artifacts", [])
            declared = {a.get("file"): a.get("sha256") for a in artifacts}
        except (json.JSONDecodeError, AttributeError, TypeError):
            continue          # a malformed recipe is reported by the verification pass itself
        for image in images:
            if image.name not in declared:
                observed["undeclared"].append(f"{directory.name}/{image.name}")
        for name, expected in sorted((n, d) for n, d in declared.items() if n):
            on_disk = directory / name
            if not on_disk.is_file():
                # 🔴 NOT reported. Rule 5e publishes the recipe and not the image, and the
                # images are gitignored, so "declared but not on disk" is the DESIGNED state
                # of a fresh checkout. Reporting it on every normal run would fill the block
                # below with expected noise and teach a reader to skip past the lines that
                # are not expected — which is how a real observation gets missed.
                continue
            if expected and digest(on_disk.read_bytes()) != expected:
                # The local copy has drifted from the recipe. Not a failure — the recipe is
                # what is published and it still regenerates — but a reader opening that file
                # is not looking at the adjudicated crop, and nothing said so.
                observed["declared_stale"].append(f"{directory.name}/{name}")
    return observed


def render(pdf, page_number: int, crop: list[float], dpi: int) -> bytes:
    import fitz  # noqa: PLC0415 — optional dependency, only needed to regenerate

    page = pdf[page_number - 1]
    pixmap = page.get_pixmap(clip=fitz.Rect(*crop), dpi=dpi)
    return pixmap.tobytes("png")


def run(action: str, only: str | None, artifact_root: Path | None = None) -> int:
    try:
        import fitz  # noqa: F401, PLC0415
    except ImportError:
        print("PyMuPDF is required to regenerate adjudication crops: pip install pymupdf",
              file=sys.stderr)
        return 2

    import fitz  # noqa: PLC0415

    failures: list[str] = []
    # 🔴 One counter per question the summary asks, because one counter answering three
    # questions is how `OK: 2 artifacts regenerate to their declared digest` was printed
    # two lines under `no digest declared` — twice. `checked` was incremented where the
    # image was RENDERED and reported where it had been COMPARED, and nothing in between
    # noticed that those are different events. A count is a claim; it must be incremented
    # at the moment the claim becomes true, never at the moment the work begins.
    rendered = 0            # an image was produced from the PDF
    digest_declared = 0     # the recipe states what that image must hash to
    digest_matched = 0      # it does
    digest_absent = 0       # it does not state it — nothing was compared
    locators_declared = 0   # adjudications the recipe lists
    locators_resolved = 0   # …that resolve uniquely to a span the crop shows
    locators_vs_manifest = 0  # …that were also checked against the snippet they name
    studies_seen = 0
    studies_skipped = 0

    for directory, recipe in recipes():
        pmid = str(recipe.get("pmid", directory.name))
        if only and pmid != only:
            continue
        studies_seen += 1

        source = recipe["source_pdf"]
        # files/ is gitignored and does NOT travel with a branch, so a worktree can hold the
        # recipe and not the article. --artifact-workspace points at the tree that has the
        # PDFs, exactly as deepdive_manifest.py and fulltext_receipts.py already do.
        pdf_path = (artifact_root or ROOT) / source["path"]
        if not pdf_path.exists():
            studies_skipped += 1
            hint = ("" if artifact_root else
                    " If the article is in another checkout, re-run with "
                    "--artifact-workspace <that tree>.")
            failures.append(
                f"{pmid}: source PDF absent at {source['path']}. The recipe cannot be run "
                f"without your own copy of the article; this repository does not ship it.{hint}")
            continue
        actual = digest(pdf_path.read_bytes())
        if actual != source["sha256"]:
            studies_skipped += 1
            failures.append(
                f"{pmid}: source PDF digest mismatch. Expected {source['sha256'][:16]}…, "
                f"found {actual[:16]}…. A different copy of the same article can carry a "
                f"different typesetting, and the crop rectangles are specific to this one")
            continue

        # 🔴 Three manifest states, not two. `snippets()` returned None both for "the recipe
        # names no manifest" and for "the recipe names one and it is not there", so a
        # misspelled path printed *no manifest declared* — a sentence about a recipe that
        # had declared one. A typo silently retired an entire class of check and reported
        # the retirement as the author's intention.
        state, quoted = manifest_state(recipe)
        if state == "UNREADABLE":
            failures.append(
                f"{pmid}: recipe declares manifest {recipe['manifest']!r} and it cannot be "
                f"read. This is not the same as declaring none: the locator-to-snippet check "
                f"would be skipped silently, so it fails instead")
            continue
        if state == "NONE":
            print(f"  {pmid}: no manifest declared — needles will be verified for uniqueness "
                  f"and containment, but not against the locators they name")

        with fitz.open(pdf_path) as pdf:
            for artifact in recipe["artifacts"]:
                name = artifact["file"]
                image = render(pdf, artifact["page"], artifact["crop"], artifact["dpi"])
                produced = digest(image)
                declared = artifact.get("sha256")
                rendered += 1

                problems, resolved, vs_manifest = check_needles(
                    pdf[artifact["page"] - 1], artifact, quoted, f"{pmid} {name}")
                failures.extend(problems)
                locators_declared += len(artifact["adjudicates"])
                locators_resolved += resolved
                locators_vs_manifest += vs_manifest

                if action == "write":
                    (directory / name).write_bytes(image)

                if declared is None:
                    digest_absent += 1
                    print(f"  {pmid} {name}: no digest declared, produced {produced}")
                else:
                    digest_declared += 1
                    if produced != declared:
                        failures.append(
                            f"{pmid}: {name} regenerated to {produced[:16]}…, recipe declares "
                            f"{declared[:16]}…")
                    else:
                        digest_matched += 1
                        print(f"  {pmid} {name}: OK {produced[:16]}…")

    # 🔴 Everything below is the fail-closed half, and it is the half that did not exist.
    # Each of these returned 0 with `OK: 0 …`: an empty adjudications directory, an absent
    # one, a --pmid that matches nothing, a --pmid misspelled by one digit, and a recipe
    # whose artifacts list is empty. A gate that reports success for having looked at
    # nothing is not a gate, and `verify` is documented as the gate.
    if action == "verify":
        if only and studies_seen == 0:
            failures.append(
                f"--pmid {only!r} selected no study. {len(recipes())} recipe(s) exist; "
                f"verifying nothing is not verifying")
        elif studies_seen == 0:
            failures.append(
                f"no adjudication recipe found under "
                f"{ADJUDICATIONS.relative_to(ROOT)}. Nothing was verified")
        elif rendered == 0 and studies_skipped == 0:
            failures.append(
                "every recipe selected declares zero artifacts; nothing was rendered "
                "and nothing was compared")
        if digest_absent:
            failures.append(
                f"{digest_absent} artifact(s) declare no sha256, so nothing was compared for "
                f"them. Run `write` to record the digests; `verify` will not pass an artifact "
                f"it did not check")

    if failures:
        print(f"\nFAILED — {len(failures)} problem(s); "
              f"{rendered} artifact(s) rendered, {digest_matched} digest(s) matched, "
              f"{locators_resolved} of {locators_declared} locator(s) resolved:",
              file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    # 🔴 The summary states what was compared, not what was walked past. Every noun below is
    # a counter incremented at the point the thing became true.
    manifest_note = (f", and {locators_vs_manifest} of them against the snippet each names"
                     if locators_vs_manifest else
                     ", none of them against a snippet — no manifest was declared")
    print(f"\nOK: {digest_matched} of {digest_declared} declared digest(s) matched across "
          f"{rendered} rendered artifact(s) in {studies_seen} study(ies); "
          f"{locators_resolved} of {locators_declared} locator(s) resolved to a span inside "
          f"the crop that shows them{manifest_note}")

    # 🔴 The scope disclaimer is unconditional, and that is the point. It is printed on a clean
    # run too, so a reader learns the boundary of the claim from the tool rather than from its
    # source, and so that a run WITH unverified material cannot be mistaken for one without.
    observed = observe_directories()
    print(f"\nSCOPE: this verifies RECIPES — every declared crop is re-rendered from the source "
          f"PDF and compared to its declared digest. It does NOT read the image files on disk, "
          f"so a corrupted local {'PNG'} is outside what the line above asserts.")
    noted = 0
    for label, items in (("image file(s) present and declared by no recipe", observed["undeclared"]),
                         ("directory(ies) holding images with no adjudications.json",
                          observed["unrecipe_directories"]),
                         ("declared artifact(s) on disk whose bytes differ from the recipe",
                          observed["declared_stale"])):
        if items:
            noted += len(items)
            print(f"OBSERVED, NOT VERIFIED — {len(items)} {label}:")
            for item in items:
                print(f"  · {item}")
    if not noted:
        print("OBSERVED, NOT VERIFIED — nothing: every file under page_adjudications/ is "
              "declared by a recipe, and every declared artifact is present.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("action", nargs="?", default="verify", choices=("verify", "write"))
    parser.add_argument("--pmid", default=None, help="restrict to one study")
    parser.add_argument(
        "--artifact-workspace", default=None,
        help="workspace root used ONLY to resolve source PDFs; recipes are still read from "
             "this checkout. files/ is gitignored and does not travel with a branch, so a "
             "worktree can hold the recipe and not the article")
    arguments = parser.parse_args()
    root = Path(arguments.artifact_workspace).resolve() if arguments.artifact_workspace else None
    try:
        return run(arguments.action, arguments.pmid, root)
    except RecipeError as exc:
        print(f"\nFAILED — the recipe cannot be read as a recipe:\n- {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
