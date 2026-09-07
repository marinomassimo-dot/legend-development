#!/usr/bin/env python3
"""Reproduce every degraded state of `regenerate_adjudications.py verify`, and grade each one.

## Why this is a command and not a table

The matrix that justified the fail-closed repair was produced once, by hand, in a session, and
would otherwise have survived only as prose. A table of exit codes copied into a document is a
measurement that decays silently: the script changes, the table does not, and the first reader to
trust it is reading last month's behaviour. **So the evidence is the command.**

Run it against the current script to see today's behaviour; run it with `--script` against an
older copy to see what changed. Both arms of the repair's mutation battery are the same
invocation pointed at two files.

## What it does

Builds an isolated sandbox that mimics the repository layout — so the subject's
`ROOT = parents[2]` lands inside it — with a synthetic two-page PDF whose text is known and a
recipe whose digests are produced by the subject's own render path, so the clean case is genuinely
clean. Then, for each state: restore the pristine tree, apply exactly ONE mutation, run `verify`,
record the exit code and the summary line.

🔴 **Two harness failures are designed against, because both happened while this was being
written, and both produced a confident wrong answer rather than an error.**

* the pristine tree is **named**, never derived from the sandbox's path. Deriving it made restore
  copy the ORIGINAL script over a patched sandbox on every case, and the battery returned a
  perfect row-for-row match with the unrepaired run — a comparison whose two arms are the same
  object agrees completely;
* the sandbox is **probed before any case runs**. When the subject could not import its own
  dependencies, both arms died identically at startup and reported 11 failures each.

A harness that silently substitutes its control for its subject is the most convincing possible
source of a wrong result.

## Grading

`CAN_BE_MISTAKEN_FOR_PASS` is the column that matters: it asks only whether a consumer reading the
exit code would record success. `MESSAGE_IS_FALSE` is stricter and asks whether the summary
sentence asserts work that did not happen.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_SCRIPT = HERE / "regenerate_adjudications.py"

# (id, description, mutation, argv-suffix)
# Each mutation receives the sandbox paths and changes exactly one thing.


def _recipe(box):
    return json.loads(box["recipe"].read_text())


def _put(box, recipe):
    box["recipe"].write_text(json.dumps(recipe, indent=2))


def m_noop(box):
    pass


def m_empty_dir(box):
    shutil.rmtree(box["adj"])


def m_no_root(box):
    shutil.rmtree(box["adj"].parent)


def m_all_digests_absent(box):
    r = _recipe(box)
    for a in r["artifacts"]:
        a.pop("sha256", None)
    _put(box, r)


def m_one_digest_absent(box):
    r = _recipe(box)
    r["artifacts"][0].pop("sha256", None)
    _put(box, r)


def m_digest_wrong(box):
    r = _recipe(box)
    r["artifacts"][0]["sha256"] = "0" * 64
    _put(box, r)


def m_no_manifest_declared(box):
    r = _recipe(box)
    r.pop("manifest", None)
    _put(box, r)


def m_manifest_missing(box):
    box["manifest"].unlink()


def m_manifest_misspelled(box):
    r = _recipe(box)
    r["manifest"] = r["manifest"].replace("99999999", "99999998")
    _put(box, r)


def m_artifacts_empty(box):
    r = _recipe(box)
    r["artifacts"] = []
    _put(box, r)


def m_adjudicates_empty(box):
    r = _recipe(box)
    for a in r["artifacts"]:
        a["adjudicates"] = []
    _put(box, r)


def m_needle_not_unique(box):
    r = _recipe(box)
    r["artifacts"][0]["adjudicates"][0]["needle"] = "DUPLICATE token"
    _put(box, r)


def m_needle_outside_crop(box):
    r = _recipe(box)
    r["artifacts"][0]["adjudicates"][0]["needle"] = "CHARLIE on the second"
    _put(box, r)


def m_bare_locator(box):
    r = _recipe(box)
    r["artifacts"][0]["adjudicates"] = ["entries[0]"]
    _put(box, r)


def m_needle_wrong_snippet(box):
    r = _recipe(box)
    r["artifacts"][0]["adjudicates"][0]["needle"] = "BRAVO a second"
    r["artifacts"][0]["crop"] = [60.0, 80.0, 400.0, 155.0]
    _put(box, r)


def m_pdf_absent(box):
    box["pdf"].unlink()


def m_pdf_tampered(box):
    box["pdf"].write_bytes(box["pdf"].read_bytes() + b"\n% tampered")


def m_stale_image(box):
    subprocess.run([sys.executable, str(box["script"]), "write"],
                   capture_output=True, cwd=box["root"])
    (box["adj"] / "a.png").write_bytes(b"not a png at all")


def m_no_artifacts_key(box):
    r = _recipe(box)
    r.pop("artifacts", None)
    _put(box, r)


def m_bad_json(box):
    box["recipe"].write_text("{ this is not json")


def m_second_study_broken(box):
    other = box["adj"].parent / "PMID88888888"
    shutil.copytree(box["adj"], other)
    r = json.loads((other / "adjudications.json").read_text())
    r["pmid"] = "88888888"
    r["source_pdf"]["path"] = "files/fulltext/does_not_exist.pdf"
    (other / "adjudications.json").write_text(json.dumps(r, indent=2))


STATES = [
    ("S00", "clean — control", m_noop, ()),
    ("S01", "adjudications directory empty", m_empty_dir, ()),
    ("S02", "page_adjudications root absent", m_no_root, ()),
    ("S03", "--pmid names no existing study", m_noop, ("--pmid", "00000000")),
    ("S04", "--pmid misspelled by one digit", m_noop, ("--pmid", "9999999")),
    ("S05", "all recipe digests absent", m_all_digests_absent, ()),
    ("S06", "one digest absent of two", m_one_digest_absent, ()),
    ("S07", "one declared digest wrong", m_digest_wrong, ()),
    ("S08", "recipe declares no manifest", m_no_manifest_declared, ()),
    ("S09", "manifest declared, file missing", m_manifest_missing, ()),
    ("S10", "manifest path misspelled", m_manifest_misspelled, ()),
    ("S11", "artifacts list empty", m_artifacts_empty, ()),
    ("S12", "adjudicates empty everywhere", m_adjudicates_empty, ()),
    ("S13", "needle matches twice", m_needle_not_unique, ()),
    ("S14", "needle resolves outside the crop", m_needle_outside_crop, ()),
    ("S15", "bare locator, no needle", m_bare_locator, ()),
    ("S16", "needle not a fragment of its snippet", m_needle_wrong_snippet, ()),
    ("S17", "source PDF absent", m_pdf_absent, ()),
    ("S18", "source PDF digest mismatch", m_pdf_tampered, ()),
    ("S19", "PyMuPDF unavailable", m_noop, ()),          # handled via PYTHONPATH stub
    ("S20", "on-disk image stale after write", m_stale_image, ()),
    ("S21", "recipe missing the artifacts key", m_no_artifacts_key, ()),
    ("S22", "recipe is not valid JSON", m_bad_json, ()),
    ("S23", "two studies, one broken", m_second_study_broken, ()),
]


def build(root: Path, script: Path, deps: Path) -> dict:
    import fitz

    (root / "framework/scripts").mkdir(parents=True)
    (root / "files/fulltext").mkdir(parents=True)
    (root / "disease-models/wwox/research/deepdive_manifests").mkdir(parents=True)
    adj = root / "disease-models/wwox/research/page_adjudications/PMID99999999"
    adj.mkdir(parents=True)

    # 🔴 dependencies come from a NAMED directory, never globbed from the subject's own folder.
    # A candidate copy sits alone; globbing beside it produced a sandbox that could not import
    # `deepdive_manifest`, and both arms of the battery then failed identically.
    for source in deps.glob("*.py"):
        shutil.copy2(source, root / "framework/scripts" / source.name)
    shutil.copy2(script, root / "framework/scripts/regenerate_adjudications.py")
    subject = root / "framework/scripts/regenerate_adjudications.py"

    probe = subprocess.run([sys.executable, str(subject), "--help"],
                           capture_output=True, text=True)
    if probe.returncode != 0:
        raise SystemExit(f"sandbox cannot run the subject: {probe.stderr.strip()}")

    document = fitz.open()
    page = document.new_page(width=612, height=792)
    page.insert_text((72, 100), "ALPHA the first unique needle here", fontsize=12)
    page.insert_text((72, 140), "BRAVO a second unique needle here", fontsize=12)
    page.insert_text((72, 180), "DUPLICATE token appears twice", fontsize=12)
    page.insert_text((72, 220), "DUPLICATE token appears twice", fontsize=12)
    second = document.new_page(width=612, height=792)
    second.insert_text((72, 100), "CHARLIE on the second page", fontsize=12)
    pdf = root / "files/fulltext/PMID99999999_synthetic.pdf"
    document.save(str(pdf))
    document.close()

    manifest_rel = "disease-models/wwox/research/deepdive_manifests/PMID99999999.json"
    (root / manifest_rel).write_text(json.dumps({"verbatim_locators": {"entries": [
        {"snippet": "ALPHA the first unique needle here"},
        {"snippet": "BRAVO a second unique needle here"},
    ]}}))

    def crop_digest(crop):
        opened = fitz.open(str(pdf))
        image = opened[0].get_pixmap(clip=fitz.Rect(*crop), dpi=150).tobytes("png")
        opened.close()
        return hashlib.sha256(image).hexdigest()

    crop_a, crop_b = [60.0, 80.0, 400.0, 115.0], [60.0, 120.0, 400.0, 155.0]
    (adj / "adjudications.json").write_text(json.dumps({
        "pmid": "99999999",
        "manifest": manifest_rel,
        "source_pdf": {"path": "files/fulltext/PMID99999999_synthetic.pdf",
                       "sha256": hashlib.sha256(pdf.read_bytes()).hexdigest()},
        "artifacts": [
            {"file": "a.png", "page": 1, "crop": crop_a, "dpi": 150, "sha256": crop_digest(crop_a),
             "adjudicates": [{"locator": "entries[0]", "needle": "ALPHA the first"}]},
            {"file": "b.png", "page": 1, "crop": crop_b, "dpi": 150, "sha256": crop_digest(crop_b),
             "adjudicates": [{"locator": "entries[1]", "needle": "BRAVO a second"}]},
        ],
    }, indent=2))

    stub = root / "noimport"
    stub.mkdir()
    (stub / "fitz.py").write_text("raise ImportError('PyMuPDF absent (simulated)')\n")

    return {"root": root, "adj": adj, "recipe": adj / "adjudications.json",
            "manifest": root / manifest_rel, "pdf": pdf, "script": subject, "stub": stub}


def run_state(box, extra, stub_fitz=False):
    env = dict(os.environ)
    if stub_fitz:
        env["PYTHONPATH"] = str(box["stub"])
    result = subprocess.run([sys.executable, str(box["script"]), "verify", *extra],
                            capture_output=True, text=True, env=env, cwd=box["root"])
    output = (result.stdout + result.stderr).strip().splitlines()
    summary = ""
    for line in output:
        stripped = line.strip()
        if stripped.startswith("OK:") or stripped.startswith("FAILED"):
            summary = stripped
    if not summary and output:
        summary = output[-1].strip()
    return result.returncode, summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--script", type=Path, default=DEFAULT_SCRIPT,
                        help="the copy of regenerate_adjudications.py to grade")
    parser.add_argument("--deps", type=Path, default=HERE,
                        help="directory holding the subject's imports; NAMED, never inferred")
    parser.add_argument("--quiet", action="store_true")
    arguments = parser.parse_args()

    try:
        import fitz  # noqa: F401
    except ImportError:
        print("PyMuPDF is required to build the synthetic source PDF", file=sys.stderr)
        return 2

    workspace = Path(tempfile.mkdtemp())
    pristine = workspace / "pristine"
    build(pristine, arguments.script, arguments.deps)

    rows = []
    for index, (ident, description, mutate, extra) in enumerate(STATES):
        live = workspace / f"case{index}"
        shutil.copytree(pristine, live)
        box = {"root": live, "adj": live / "disease-models/wwox/research/page_adjudications/PMID99999999",
               "recipe": live / "disease-models/wwox/research/page_adjudications/PMID99999999/adjudications.json",
               "manifest": live / "disease-models/wwox/research/deepdive_manifests/PMID99999999.json",
               "pdf": live / "files/fulltext/PMID99999999_synthetic.pdf",
               "script": live / "framework/scripts/regenerate_adjudications.py",
               "stub": live / "noimport"}
        try:
            mutate(box)
        except Exception as exc:  # a mutation that cannot be applied tested nothing
            rows.append((ident, description, "SETUP", f"mutation failed: {exc}"))
            continue
        code, summary = run_state(box, extra, stub_fitz=(ident == "S19"))
        rows.append((ident, description, code, summary))

    width = max(len(d) for _, d, _, _ in rows)
    print(f"subject: {arguments.script}")
    print(f"{'ID':4s} {'PRECONDITION'.ljust(width)}  EXIT  SUMMARY")
    print("-" * (width + 100))
    mistakable = []
    for ident, description, code, summary in rows:
        flag = ""
        if ident != "S00" and code == 0:
            mistakable.append(ident)
            flag = "  <- exit 0"
        print(f"{ident:4s} {description.ljust(width)}  {str(code):>4s}  {summary[:96]}{flag}")

    print(f"\n{len(rows)} state(s) exercised.")
    print(f"exit 0 on a degraded precondition: {len(mistakable)} -> "
          f"{', '.join(mistakable) if mistakable else 'none'}")
    print("A consumer reading only the exit code records success for every id listed above.")
    shutil.rmtree(workspace, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
