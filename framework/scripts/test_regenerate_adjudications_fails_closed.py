#!/usr/bin/env python3
"""`verify` must fail closed on every state where it verified less than it reports.

🔴 Why this file exists. `test_regenerate_adjudications.py` imports exactly one name —
`check_needles` — and never calls `run()`. The predicate and the geometry were covered; the
orchestration that decides the exit code was covered by nothing, and that is where every
fail-open lived. The tested surface and the degraded surface were disjoint.

Each test drives the real script as a subprocess against a synthetic PDF, so what is measured
is the exit code a gate would read, not an internal return value.

Every test below is a mutation arm: it FAILS against the pre-repair script. Running this file
with LEGEND_ADJ_SCRIPT pointed at the old copy is the way to confirm that.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(os.environ.get(
    "LEGEND_ADJ_SCRIPT",
    Path(__file__).resolve().parent / "regenerate_adjudications.py"))
# 🔴 The subject and its dependencies come from different places when the subject is a
# candidate copy. Globbing the subject's own directory for `*.py` silently produced a sandbox
# with no `deepdive_manifest`, so BOTH arms died at import and failed identically — a mutation
# battery whose two arms agree because neither one ran is the most convincing wrong answer
# available. The dependency directory is therefore named, not inferred.
DEPS = Path(os.environ.get("LEGEND_ADJ_DEPS", SCRIPT.parent))

try:
    import fitz  # noqa: F401
except ImportError:  # pragma: no cover - environment without PyMuPDF
    fitz = None


def build(root: Path) -> dict:
    """A sandbox whose layout makes the script resolve ROOT inside it."""
    (root / "framework/scripts").mkdir(parents=True)
    (root / "files/fulltext").mkdir(parents=True)
    (root / "disease-models/wwox/research/deepdive_manifests").mkdir(parents=True)
    adj = root / "disease-models/wwox/research/page_adjudications/PMID99999999"
    adj.mkdir(parents=True)

    for source in DEPS.glob("*.py"):
        shutil.copy2(source, root / "framework/scripts" / source.name)
    shutil.copy2(SCRIPT, root / "framework/scripts/regenerate_adjudications.py")
    # A sandbox that cannot import the subject would make every assertion below vacuous.
    probe = subprocess.run(
        [sys.executable, str(root / "framework/scripts/regenerate_adjudications.py"), "--help"],
        capture_output=True, text=True)
    if probe.returncode != 0:
        raise RuntimeError(f"sandbox cannot run the subject: {probe.stderr.strip()}")

    document = fitz.open()
    page = document.new_page(width=612, height=792)
    page.insert_text((72, 100), "ALPHA the first unique needle here", fontsize=12)
    page.insert_text((72, 140), "BRAVO a second unique needle here", fontsize=12)
    pdf = root / "files/fulltext/PMID99999999_synthetic.pdf"
    document.save(str(pdf))
    document.close()

    manifest = "disease-models/wwox/research/deepdive_manifests/PMID99999999.json"
    (root / manifest).write_text(json.dumps({"verbatim_locators": {"entries": [
        {"snippet": "ALPHA the first unique needle here"},
        {"snippet": "BRAVO a second unique needle here"},
    ]}}))

    def crop_digest(crop):
        opened = fitz.open(str(pdf))
        image = opened[0].get_pixmap(clip=fitz.Rect(*crop), dpi=150).tobytes("png")
        opened.close()
        return hashlib.sha256(image).hexdigest()

    crop_a, crop_b = [60.0, 80.0, 400.0, 115.0], [60.0, 120.0, 400.0, 155.0]
    recipe = {
        "pmid": "99999999",
        "manifest": manifest,
        "source_pdf": {"path": "files/fulltext/PMID99999999_synthetic.pdf",
                       "sha256": hashlib.sha256(pdf.read_bytes()).hexdigest()},
        "artifacts": [
            {"file": "a.png", "page": 1, "crop": crop_a, "dpi": 150,
             "sha256": crop_digest(crop_a),
             "adjudicates": [{"locator": "entries[0]", "needle": "ALPHA the first"}]},
            {"file": "b.png", "page": 1, "crop": crop_b, "dpi": 150,
             "sha256": crop_digest(crop_b),
             "adjudicates": [{"locator": "entries[1]", "needle": "BRAVO a second"}]},
        ],
    }
    (adj / "adjudications.json").write_text(json.dumps(recipe, indent=2))
    return {"root": root, "adj": adj, "recipe": adj / "adjudications.json",
            "manifest": root / manifest, "pdf": pdf,
            "script": root / "framework/scripts/regenerate_adjudications.py"}


@unittest.skipIf(fitz is None, "PyMuPDF is required to build the synthetic source PDF")
class VerifyFailsClosed(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.box = build(Path(self.tmp) / "repo")

    def verify(self, *extra):
        result = subprocess.run(
            [sys.executable,
             str(self.box["root"] / "framework/scripts/regenerate_adjudications.py"),
             "verify", *extra],
            capture_output=True, text=True)
        return result.returncode, result.stdout + result.stderr

    def recipe(self):
        return json.loads(self.box["recipe"].read_text())

    def write(self, recipe):
        self.box["recipe"].write_text(json.dumps(recipe, indent=2))

    # --- the control, without which none of the rest means anything -----------------------
    def test_the_clean_case_still_passes(self):
        code, output = self.verify()
        self.assertEqual(code, 0, output)
        self.assertIn("2 of 2 declared digest(s) matched", output)

    # --- zero coverage --------------------------------------------------------------------
    def test_an_empty_adjudications_directory_is_not_a_pass(self):
        shutil.rmtree(self.box["adj"])
        code, output = self.verify()
        self.assertEqual(code, 1, output)
        self.assertIn("Nothing was verified", output)

    def test_a_pmid_that_selects_no_study_is_not_a_pass(self):
        code, output = self.verify("--pmid", "00000000")
        self.assertEqual(code, 1, output)
        self.assertIn("selected no study", output)

    def test_a_pmid_misspelled_by_one_digit_is_not_a_pass(self):
        code, output = self.verify("--pmid", "9999999")
        self.assertEqual(code, 1, output)
        self.assertIn("selected no study", output)

    def test_an_empty_artifacts_list_is_not_a_pass(self):
        recipe = self.recipe()
        recipe["artifacts"] = []
        self.write(recipe)
        code, output = self.verify()
        self.assertEqual(code, 1, output)
        self.assertIn("nothing was rendered", output)

    # --- counted but never compared -------------------------------------------------------
    def test_an_artifact_with_no_declared_digest_is_not_reported_as_matching_one(self):
        recipe = self.recipe()
        for artifact in recipe["artifacts"]:
            artifact.pop("sha256")
        self.write(recipe)
        code, output = self.verify()
        self.assertEqual(code, 1, output)
        self.assertIn("declare no sha256", output)
        self.assertNotIn("2 of 2 declared digest(s) matched", output)

    def test_one_missing_digest_among_two_is_not_absorbed_by_the_other(self):
        recipe = self.recipe()
        recipe["artifacts"][0].pop("sha256")
        self.write(recipe)
        code, output = self.verify()
        self.assertEqual(code, 1, output)
        self.assertIn("1 artifact(s) declare no sha256", output)

    # --- the manifest's third state -------------------------------------------------------
    def test_a_declared_manifest_that_is_missing_is_not_reported_as_undeclared(self):
        self.box["manifest"].unlink()
        code, output = self.verify()
        self.assertEqual(code, 1, output)
        self.assertIn("cannot be read", output)
        self.assertNotIn("no manifest declared", output)

    def test_a_misspelled_manifest_path_is_not_reported_as_undeclared(self):
        recipe = self.recipe()
        recipe["manifest"] = recipe["manifest"].replace("99999999", "99999998")
        self.write(recipe)
        code, output = self.verify()
        self.assertEqual(code, 1, output)
        self.assertIn("cannot be read", output)
        self.assertNotIn("no manifest declared", output)

    def test_declaring_no_manifest_at_all_remains_allowed(self):
        """The legitimate configuration must survive the repair, or the repair overshot."""
        recipe = self.recipe()
        recipe.pop("manifest")
        self.write(recipe)
        code, output = self.verify()
        self.assertEqual(code, 0, output)
        self.assertIn("no manifest declared", output)
        self.assertIn("none of them against a snippet", output)

    # --- states that already failed closed, asserted so a repair cannot silently relax them
    def test_a_wrong_declared_digest_still_fails(self):
        recipe = self.recipe()
        recipe["artifacts"][0]["sha256"] = "0" * 64
        self.write(recipe)
        self.assertEqual(self.verify()[0], 1)

    def test_an_absent_source_pdf_still_fails(self):
        self.box["pdf"].unlink()
        self.assertEqual(self.verify()[0], 1)

    def test_a_tampered_source_pdf_still_fails(self):
        self.box["pdf"].write_bytes(self.box["pdf"].read_bytes() + b"\n% tampered")
        self.assertEqual(self.verify()[0], 1)

    def test_the_summary_counts_locators_it_actually_resolved(self):
        recipe = self.recipe()
        for artifact in recipe["artifacts"]:
            artifact["adjudicates"] = []
        self.write(recipe)
        code, output = self.verify()
        self.assertEqual(code, 0, output)
        self.assertIn("0 of 0 locator(s) resolved", output)


class NoDegradedStateLooksLikeACleanRun(unittest.TestCase):
    """🔴 The question that decides whether this is fail-closed at all.

    Three states produced output **byte-identical to a clean run** — same text, same exit 0:
    a declared PNG replaced with garbage, an undeclared PNG in an adjudicated directory, and a
    whole study directory holding images and no `adjudications.json`. `verify` re-renders from
    the PDF and compares to the recipe, so it never opens a file on disk and never looks at the
    directory.

    **Nothing here was made to fail**, and that is deliberate: the tool promises recipe
    verification, and rule 5e governs what is *published*, while these images are gitignored.
    What changed is that the summary can no longer say "everything was verified" and stay
    silent about material it never looked at. A gate need not check everything; it must not be
    quiet about what it did not check.
    """

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.box = build(Path(self.tmp) / "repo")

    def verify(self):
        result = subprocess.run(
            [sys.executable, str(self.box["root"] / "framework/scripts/regenerate_adjudications.py"),
             "verify"], capture_output=True, text=True)
        return result.returncode, result.stdout + result.stderr

    def test_a_clean_run_states_the_boundary_of_its_own_claim(self):
        code, output = self.verify()
        self.assertEqual(code, 0, output)
        self.assertIn("SCOPE: this verifies RECIPES", output)
        self.assertIn("OBSERVED, NOT VERIFIED — nothing", output)

    def test_a_corrupted_declared_image_is_reported(self):
        subprocess.run([sys.executable, str(self.box["script"]), "write"],
                       capture_output=True, cwd=self.box["root"])
        (self.box["adj"] / "a.png").write_bytes(b"NOT A PNG AT ALL")
        code, output = self.verify()
        self.assertEqual(code, 0, output)
        self.assertIn("bytes differ from the recipe", output)
        self.assertNotIn("OBSERVED, NOT VERIFIED — nothing", output)

    def test_an_undeclared_image_is_reported(self):
        (self.box["adj"] / "z_undeclared.png").write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00" * 32)
        code, output = self.verify()
        self.assertEqual(code, 0, output)
        self.assertIn("declared by no recipe", output)

    def test_a_directory_with_images_and_no_recipe_is_reported(self):
        other = self.box["adj"].parent / "PMID77777777"
        other.mkdir()
        (other / "p01.png").write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00" * 32)
        code, output = self.verify()
        self.assertEqual(code, 0, output)
        self.assertIn("no adjudications.json", output)

    def test_the_three_states_are_pairwise_distinguishable_from_clean_and_each_other(self):
        """The arm that makes the three tests above mean something together."""
        import hashlib

        def fresh():
            box = build(Path(tempfile.mkdtemp()) / "repo")
            return box

        outputs = {}
        for name, mutate in (
            ("clean", lambda b: None),
            ("corrupt", lambda b: ((subprocess.run(
                [sys.executable, str(b["script"]), "write"], capture_output=True, cwd=b["root"]),
                (b["adj"] / "a.png").write_bytes(b"garbage")) and None)),
            ("undeclared", lambda b: (b["adj"] / "extra.png").write_bytes(b"\x89PNG") and None),
            ("no_recipe", lambda b: ((b["adj"].parent / "PMID77777777").mkdir(),
                                     (b["adj"].parent / "PMID77777777" / "p.png").write_bytes(
                                         b"\x89PNG")) and None),
        ):
            box = fresh()
            mutate(box)
            result = subprocess.run(
                [sys.executable, str(box["script"]), "verify"],
                capture_output=True, text=True, cwd=box["root"])
            outputs[name] = hashlib.sha256((result.stdout + result.stderr).encode()).hexdigest()
        self.assertEqual(len(set(outputs.values())), 4,
                         f"two states produce identical output: {outputs}")


class AMalformedRecipeIsAVerdictNotATraceback(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.box = build(Path(self.tmp) / "repo")

    def verify(self):
        result = subprocess.run(
            [sys.executable, str(self.box["script"]), "verify"],
            capture_output=True, text=True, cwd=self.box["root"])
        return result.returncode, result.stdout + result.stderr

    def test_a_missing_artifacts_key_names_the_file_and_the_key(self):
        recipe = json.loads(self.box["recipe"].read_text())
        recipe.pop("artifacts")
        self.box["recipe"].write_text(json.dumps(recipe))
        code, output = self.verify()
        self.assertEqual(code, 1, output)
        self.assertNotIn("Traceback", output)
        self.assertIn("declares no artifacts", output)

    def test_invalid_json_names_the_file(self):
        self.box["recipe"].write_text("{ not json")
        code, output = self.verify()
        self.assertEqual(code, 1, output)
        self.assertNotIn("Traceback", output)
        self.assertIn("not valid JSON", output)

    def test_a_non_object_recipe_is_refused(self):
        self.box["recipe"].write_text('["a", "list"]')
        code, output = self.verify()
        self.assertEqual(code, 1, output)
        self.assertNotIn("Traceback", output)


class OneRegenerationCannotDestroyAnother(unittest.TestCase):
    """🔴 IN SCOPE, by the tool's own contract rather than by tidiness.

    The declared contract is RECIPE REGENERATION, not directory integrity. The test for
    membership is whether a defect can **corrupt another declared regeneration**. Measured:

      duplicate targets   artifact[0] declares f495b656…, artifact[1] declares 6abfb6f0…,
                          and a.png on disk held 6abfb6f0… — one output destroyed the other,
                          while verify exited 0 with a clean summary
      traversal           "../../../../ESCAPED.png" landed in disease-models/, outside the
                          adjudication directory and inside the repository
      absolute path       Path(dir) / "/tmp/x.png" is /tmp/x.png, so write left a file
                          entirely outside the repository

    A zero-area crop is NOT handled here and has its own test below: it is already refused by
    geometry. Out of scope AND correctly ignored is a different verdict from out of scope and
    silent, and patching every nameable mutation would widen the contract past its promise.
    """

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.box = build(Path(self.tmp) / "repo")

    def run_tool(self, action="verify"):
        result = subprocess.run([sys.executable, str(self.box["script"]), action],
                                capture_output=True, text=True, cwd=self.box["root"])
        return result.returncode, result.stdout + result.stderr

    def recipe(self):
        return json.loads(self.box["recipe"].read_text())

    def write_recipe(self, recipe):
        self.box["recipe"].write_text(json.dumps(recipe, indent=2))

    def test_two_artifacts_writing_one_name_is_refused(self):
        recipe = self.recipe()
        recipe["artifacts"][1]["file"] = recipe["artifacts"][0]["file"]
        self.write_recipe(recipe)
        for action in ("verify", "write"):
            with self.subTest(action=action):
                code, output = self.run_tool(action)
                self.assertEqual(code, 1, output)
                self.assertIn("silently destroy", output)

    def test_a_traversing_output_name_is_refused_and_writes_nothing(self):
        recipe = self.recipe()
        recipe["artifacts"][0]["file"] = "../../../../ESCAPED.png"
        self.write_recipe(recipe)
        code, output = self.run_tool("write")
        self.assertEqual(code, 1, output)
        self.assertIn("not a plain name", output)
        self.assertEqual(list(Path(self.tmp).rglob("ESCAPED.png")), [])

    def test_an_absolute_output_name_is_refused_and_writes_nothing(self):
        escape = Path(self.tmp) / "ABSOLUTE_ESCAPE.png"
        recipe = self.recipe()
        recipe["artifacts"][0]["file"] = str(escape)
        self.write_recipe(recipe)
        code, output = self.run_tool("write")
        self.assertEqual(code, 1, output)
        self.assertFalse(escape.exists(), "write left a file outside the adjudication directory")

    def test_a_plain_unique_name_is_still_accepted(self):
        """The control. Without it, a check that refused every recipe would pass the three above."""
        code, output = self.run_tool("verify")
        self.assertEqual(code, 0, output)

    def test_a_zero_area_crop_is_refused_by_geometry_not_by_this_check(self):
        """Out of scope for the name check, and NOT silent — the distinction is the point."""
        recipe = self.recipe()
        recipe["artifacts"][0]["crop"] = [100.0, 100.0, 100.0, 100.0]
        self.write_recipe(recipe)
        code, output = self.run_tool("verify")
        self.assertEqual(code, 1, output)
        self.assertIn("does not contain the span", output)
        self.assertNotIn("not a plain name", output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
