#!/usr/bin/env python3
"""ADV-057: the opt-in per-file cache of the gate's privacy scan changes no verdict and no finding.

What is proved here, and how:
* DIFFERENTIAL, in process: the whole existing gate suite (scripts/test_public_release_gate.py, every fixture, the BLOCK ones included) is run with
  `scan_privacy_and_secrets` replaced by a wrapper that scans the same tree four ways (no cache, cold cache, warm cache, verify mode) and fails if the
  findings differ by a single field; the suite's own assertions then run on the no-cache result.
* DIFFERENTIAL, through the command line: the same suite again in a subprocess with the cache switched on for every gate it starts.
* MUTATION: a copy of the gate with one detector pattern changed invalidates every entry; the formerly clean file is rescanned and flagged.
* The cache never answers from a damaged, unsealed, wrongly sealed, other-gate or other-format file; a hand-edited but resealed entry is caught by `--cache-verify`.
* OFF means off: no flag, `--no-cache`, or a pre-check writes nothing.
`GATE_CACHE_FULL_TREE=1` adds the exact-tree comparison on this repository (about ten minutes). `--help` is safe.
"""
from __future__ import annotations

import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from dataclasses import asdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
GATE_PATH = HERE / "public_release_gate.py"
BASE_PATH = HERE / "test_public_release_gate.py"
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    sys.exit(0)


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def keys(findings) -> list:
    return sorted(json.dumps(asdict(f), sort_keys=True) for f in findings)


def run_gate(root: Path, *args: str, env: dict | None = None, gate: Path = GATE_PATH):
    e = {k: v for k, v in os.environ.items() if k not in ("LEGEND_GATE_CACHE", "LEGEND_GATE_CACHE_FILE")}
    e.update(env or {})
    return subprocess.run([sys.executable, str(gate), "--root", str(root), "--skip-clean-clone", *args], capture_output=True, text=True, env=e)


def finding_lines(done) -> list:
    """The gate prints `[SEVERITY] CODE path:line - message`; a minimal tree also carries four tree-level BLOCKs (CI workflow, provenance files) that no cache touches."""
    return [line for line in done.stdout.splitlines() if line.startswith("[")]


def privacy_lines(done) -> list:
    return [line for line in finding_lines(done) if " MISSING_" not in line]


def make_tree(root: Path, extra: dict | None = None) -> None:
    (root / "README.md").write_text("# Public project\n", encoding="utf-8")
    (root / "notes.md").write_text("A harmless note.\n", encoding="utf-8")
    (root / "data.tsv").write_text("a\tb\n1\t2\n", encoding="utf-8")
    for name, text in (extra or {}).items():
        (root / name).write_text(text, encoding="utf-8")


class DifferentialSuite(unittest.TestCase):
    def test_every_existing_fixture_gives_identical_findings_cold_warm_verify_and_uncached(self) -> None:
        base = load(BASE_PATH, "gate_base_tests_for_cache")
        gate = base.GATE
        original = gate.scan_privacy_and_secrets
        counts = {"calls": 0, "with_findings": 0, "block": 0, "hits_warm": 0, "files_warm": 0}
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        prior = os.environ.get("LEGEND_GATE_CACHE_FILE")

        def differential(root, findings):
            plain: list = []
            original(root, plain)
            gate.scan_privacy_and_secrets = original            # the cached path calls the real scan for its misses
            try:
                os.environ["LEGEND_GATE_CACHE_FILE"] = str(Path(tmp.name) / f"c{counts['calls']}.json")
                cold: list = []; warm: list = []; verify: list = []
                gate.scan_privacy_cached(root, cold)
                stats = gate.scan_privacy_cached(root, warm)
                vstats = gate.scan_privacy_cached(root, verify, verify=True)
            finally:
                gate.scan_privacy_and_secrets = differential
                if prior is None:
                    os.environ.pop("LEGEND_GATE_CACHE_FILE", None)
                else:
                    os.environ["LEGEND_GATE_CACHE_FILE"] = prior
            self.assertEqual(keys(plain), keys(cold), "cold cache differs from the uncached scan")
            self.assertEqual(keys(plain), keys(warm), "warm cache differs from the uncached scan")
            self.assertEqual(keys(plain), keys(verify), "verify mode differs from the uncached scan")
            self.assertEqual(vstats["mismatch"], [])
            counts["calls"] += 1
            counts["with_findings"] += bool(plain)
            counts["block"] += any(f.severity == "BLOCK" for f in plain)
            counts["hits_warm"] += stats["hits"]; counts["files_warm"] += stats["files"]
            findings.extend(plain)

        gate.scan_privacy_and_secrets = differential
        try:
            suite = unittest.defaultTestLoader.loadTestsFromModule(base)
            result = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
        finally:
            gate.scan_privacy_and_secrets = original
        self.assertTrue(result.wasSuccessful(), [str(x[0]) + x[1][-600:] for x in result.failures + result.errors])
        self.assertEqual(result.testsRun, 87, "the base suite changed size; update the proof (and say so in the design note)")
        print("DIFFERENTIAL fixtures compared:", counts, file=sys.stderr)
        self.assertGreaterEqual(counts["calls"], 40, counts)
        self.assertGreaterEqual(counts["block"], 20, counts)                  # the BLOCK fixtures are in the comparison, not only clean trees
        self.assertEqual(counts["hits_warm"], counts["files_warm"])             # a warm run answered every file from the cache

    def test_the_whole_existing_suite_passes_with_the_cache_switched_on_for_every_command_line_gate(self) -> None:
        with tempfile.TemporaryDirectory() as t:
            env = dict(os.environ, LEGEND_GATE_CACHE="1", LEGEND_GATE_CACHE_FILE=str(Path(t) / "shared.json"))
            done = subprocess.run([sys.executable, str(BASE_PATH)], capture_output=True, text=True, env=env)
        self.assertEqual(done.returncode, 0, done.stderr[-1500:])
        self.assertIn("OK", done.stderr.splitlines()[-1])


class RaceGuard(unittest.TestCase):
    """The key that is stored is the hash of the bytes that were scanned, read once for both purposes."""
    KEY = "-----BEGIN " + "RSA PRIVATE KEY-----"

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "repo"
        self.root.mkdir()
        make_tree(self.root)
        self.gate = load(GATE_PATH, "gate_for_race")
        os.environ["LEGEND_GATE_CACHE_FILE"] = str(Path(self.tmp.name) / "race.json")
        self.addCleanup(os.environ.pop, "LEGEND_GATE_CACHE_FILE", None)

    def test_an_edit_between_the_first_pass_and_the_scan_is_judged_and_filed_as_what_it_became(self) -> None:
        original = self.gate.scan_privacy_and_secrets

        def edit_then_scan(r, findings):
            (r / "notes.md").write_text(self.KEY + "\n", encoding="utf-8")        # lands after the first hash, before the scan
            original(r, findings)
        self.gate.scan_privacy_and_secrets = edit_then_scan
        try:
            found: list = []
            self.gate.scan_privacy_cached(self.root, found)
        finally:
            self.gate.scan_privacy_and_secrets = original
        self.assertIn("PRIVATE_KEY", {f.code for f in found})                      # this run judged what was on disk when scanned, as today
        again: list = []
        stats = self.gate.scan_privacy_cached(self.root, again)
        self.assertEqual((stats["hits"], stats["misses"]), (3, 0))
        self.assertEqual(keys(found), keys(again))
        (self.root / "notes.md").write_text("A harmless note.\n", encoding="utf-8")        # back to the original bytes: a miss, clean, never the violation's entry
        clean: list = []
        self.assertEqual(self.gate.scan_privacy_cached(self.root, clean)["misses"], 1)
        self.assertNotIn("PRIVATE_KEY", {f.code for f in clean})

    def test_a_file_that_is_V_then_clean_then_V_again_cannot_store_the_clean_verdict_under_Vs_hash(self) -> None:
        """The reviewer's A-B-A race: the first pass sees V, the scan reads the clean bytes, a later read sees V again."""
        (self.root / "notes.md").write_text(self.KEY + "\n", encoding="utf-8")
        target = self.root / "notes.md"
        real = Path.read_bytes
        reads = {"n": 0}

        def toggling(self_path):
            if self_path == target:
                reads["n"] += 1
                return b"A harmless note.\n" if reads["n"] == 2 else real(self_path)      # read 1: V (first pass); read 2: clean (the scan); later reads: V
            return real(self_path)
        Path.read_bytes = toggling
        try:
            self.gate.scan_privacy_cached(self.root, [])
        finally:
            Path.read_bytes = real
        after: list = []
        self.gate.scan_privacy_cached(self.root, after)                             # the file on disk is V again
        self.assertIn("PRIVATE_KEY", {f.code for f in after}, "a clean verdict was filed under the violating file's hash")
        plain: list = []
        self.gate.scan_privacy_and_secrets(self.root, plain)
        self.assertEqual(keys(plain), keys(after))

    def test_the_text_handed_to_the_scan_equals_what_read_text_returns_for_any_bytes(self) -> None:
        samples = [b"", b"plain\n", b"a\r\nb\rc\n", b"\xef\xbb\xbfBOM\n", b"bad \xff\xfe bytes \xc3(", b"nul\x00in\n",
                   b"x" * 8191 + b"\r\n" + b"y", b"x" * 8192 + b"\r" + b"\nz", b"\xe2\x82", b"line\r", "caf\u00e9 \u0301 \U0001F600\n".encode("utf-8")]
        with tempfile.TemporaryDirectory() as t:
            for i, raw in enumerate(samples):
                f = Path(t) / f"s{i}.txt"
                f.write_bytes(raw)
                self.assertEqual(self.gate.decode_like_read_text(raw), f.read_text(encoding="utf-8", errors="replace"), raw[:30])

    def test_a_file_name_that_is_not_utf8_gives_the_same_findings_cached_and_uncached(self) -> None:
        name = os.fsdecode(b"bad\xff.md")
        (self.root / name).write_text("contact: a.person" + "@" + "real-looking-host.net\n", encoding="utf-8")
        plain: list = []
        self.gate.scan_privacy_and_secrets(self.root, plain)
        cached: list = []
        self.gate.scan_privacy_cached(self.root, cached)
        warm: list = []
        self.gate.scan_privacy_cached(self.root, warm)
        self.assertEqual(keys(plain), keys(cached))
        self.assertEqual(keys(plain), keys(warm))


class CacheBehaviour(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "repo"
        self.root.mkdir()
        self.cache = Path(self.tmp.name) / "cache" / "c.json"
        self.env = {"LEGEND_GATE_CACHE_FILE": str(self.cache)}
        self.key = "-----BEGIN " + "RSA PRIVATE KEY-----"                      # the detector's own example; no real key

    def test_off_means_off_and_a_precheck_and_no_cache_write_nothing(self) -> None:
        make_tree(self.root)
        self.assertEqual(privacy_lines(run_gate(self.root, env=self.env)), [])
        self.assertEqual(privacy_lines(run_gate(self.root, "--no-cache", "--cache", env=dict(self.env, LEGEND_GATE_CACHE="1"))), [])
        self.assertEqual(run_gate(self.root, "--cache", "--paths", "notes.md", env=self.env).returncode, 0)
        self.assertFalse(self.cache.exists() or self.cache.parent.exists(), "something was written although the cache was off")
        base = run_gate(self.root, "--no-cache", env=self.env)
        cached = run_gate(self.root, "--cache", env=self.env)
        self.assertTrue(self.cache.exists())
        self.assertEqual((cached.returncode, finding_lines(cached)), (base.returncode, finding_lines(base)))     # same verdict, same findings, tree-level BLOCKs included

    def test_an_edited_file_is_rescanned_and_flagged_and_the_others_still_hit(self) -> None:
        make_tree(self.root)
        run_gate(self.root, "--cache", env=self.env)
        (self.root / "notes.md").write_text(self.key + "\n", encoding="utf-8")
        done = run_gate(self.root, "--cache", env=self.env)
        self.assertIn("PRIVATE_KEY", done.stdout)
        self.assertRegex(done.stderr, r"hits=\d+ misses=1 ")
        plain = run_gate(self.root, "--no-cache", env=self.env)
        self.assertEqual((plain.returncode, finding_lines(plain)), (done.returncode, finding_lines(done)))

    def test_a_cache_that_is_damaged_unsealed_or_of_another_gate_is_no_cache(self) -> None:
        make_tree(self.root, {"bad.md": self.key + "\n"})
        first = run_gate(self.root, "--cache", env=self.env)
        self.assertIn("PRIVATE_KEY", first.stdout)
        good = self.cache.read_text(encoding="utf-8")
        data = json.loads(good)
        variants = {
            "garbage": "not json",
            "truncated": good[: len(good) // 2],
            "tampered, seal kept": good.replace('"PRIVATE_KEY"', '"X"'),
            "other format": json.dumps(dict(data, format=99)),
            "other gate": json.dumps(dict(data, gate_sha256="0" * 64)),
            "entries not a dict": json.dumps(dict(data, entries=[])),
        }
        for name, text in variants.items():
            self.cache.write_text(text, encoding="utf-8")
            done = run_gate(self.root, "--cache", env=self.env)
            self.assertIn("PRIVATE_KEY", done.stdout, name)
            self.assertEqual(finding_lines(done), finding_lines(first), name)
            self.assertRegex(done.stderr, r"hits=0 ", name)

    def test_verify_mode_catches_an_entry_that_was_edited_and_resealed(self) -> None:
        make_tree(self.root, {"bad.md": self.key + "\n"})
        run_gate(self.root, "--cache", env=self.env)
        gate = load(GATE_PATH, "gate_for_reseal")
        data = json.loads(self.cache.read_text(encoding="utf-8"))
        for k, items in data["entries"].items():
            if items:
                data["entries"][k] = []                                         # the cache now says bad.md is clean
        data["seal"] = gate.cache_seal(data["gate_sha256"], data["entries"])
        self.cache.write_text(json.dumps(data), encoding="utf-8")
        wrong = run_gate(self.root, "--cache", env=self.env)
        self.assertNotIn("PRIVATE_KEY", wrong.stdout, "a resealed hand edit is not detectable without --cache-verify; this is the stated limit")
        caught = run_gate(self.root, "--cache-verify", env=self.env)
        self.assertEqual(caught.returncode, 3)
        self.assertIn("CACHE_MISMATCH", caught.stderr)
        self.assertIn("PRIVATE_KEY", run_gate(self.root, "--cache", env=self.env).stdout)      # verify rewrote the cache from the fresh scan

    def test_changing_one_detector_pattern_invalidates_every_entry_and_flags_the_formerly_clean_file(self) -> None:
        make_tree(self.root, {"marker.md": "contains QXZ-TEST-TOKEN here\n"})
        original = GATE_PATH.read_text(encoding="utf-8")
        needle = 'private_key = re.compile(r"-----BEGIN'
        self.assertEqual(original.count(needle), 1)
        mutant = Path(self.tmp.name) / "gate_mutant.py"
        mutant.write_text(original.replace(needle, 'private_key = re.compile(r"QXZ-TEST-TOKEN|-----BEGIN'), encoding="utf-8")
        self.assertEqual(privacy_lines(run_gate(self.root, "--cache", env=self.env)), [])        # the real gate: clean, cached
        warm = run_gate(self.root, "--cache", env=self.env)
        self.assertRegex(warm.stderr, r"misses=0 ")                                              # every file answered from the cache
        flagged = run_gate(self.root, "--cache", env=self.env, gate=mutant)
        self.assertIn("PRIVATE_KEY", flagged.stdout)
        self.assertRegex(flagged.stderr, r"hits=0 ")                                             # the changed script answered nothing from the old cache
        self.assertIn("PRIVATE_KEY", run_gate(self.root, "--no-cache", env=self.env, gate=mutant).stdout)
        back = run_gate(self.root, "--cache", env=self.env)                                      # and back: the other gate's cache is no cache for it
        self.assertEqual(privacy_lines(back), [])
        self.assertRegex(back.stderr, r"hits=0 ")


@unittest.skipUnless(os.environ.get("GATE_CACHE_FULL_TREE") == "1", "exact-tree comparison: set GATE_CACHE_FULL_TREE=1 (about ten minutes)")
class ExactTree(unittest.TestCase):
    def test_this_repository_cold_warm_and_uncached_are_identical(self) -> None:
        root = HERE.parent
        gate = load(GATE_PATH, "gate_exact_tree")
        with tempfile.TemporaryDirectory() as t:
            os.environ["LEGEND_GATE_CACHE_FILE"] = str(Path(t) / "tree.json")
            try:
                plain, cold, warm = [], [], []
                gate.scan_privacy_and_secrets(root, plain)
                gate.scan_privacy_cached(root, cold)
                stats = gate.scan_privacy_cached(root, warm)
            finally:
                os.environ.pop("LEGEND_GATE_CACHE_FILE", None)
        self.assertEqual(keys(plain), keys(cold))
        self.assertEqual(keys(plain), keys(warm))
        self.assertEqual(stats["hits"], stats["files"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
