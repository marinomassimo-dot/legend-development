#!/usr/bin/env python3
"""Regression tests for public_release_gate.py."""

from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


GATE_PATH = Path(__file__).with_name("public_release_gate.py")
SPEC = importlib.util.spec_from_file_location("public_release_gate", GATE_PATH)
assert SPEC and SPEC.loader
GATE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = GATE
SPEC.loader.exec_module(GATE)


class GateTests(unittest.TestCase):
    def make_repo(self) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "README.md").write_text("# Public project\n", encoding="utf-8")
        return root

    def test_direct_identifier_blocks(self) -> None:
        root = self.make_repo()
        (root / "note.md").write_text("Bim" + "ba", encoding="utf-8")
        findings = []
        GATE.scan_privacy_and_secrets(root, findings)
        self.assertIn("DIRECT_IDENTIFIER", {item.code for item in findings})

    def test_detector_sources_do_not_embed_sensitive_vocabulary(self) -> None:
        sensitive_codepoints = (
            (66, 101, 97),
            (66, 101, 97, 116, 114, 105, 99, 101),
            (66, 105, 109, 98, 97),
            (77, 97, 115, 115, 105, 109, 111),
            (66, 101, 114, 103, 97, 109, 111),
        )
        sources = [
            GATE_PATH,
            GATE_PATH.with_name("independent_privacy_scan.py"),
        ]
        leaks = []
        for path in sources:
            lowered = path.read_text(encoding="utf-8").lower()
            for codepoints in sensitive_codepoints:
                token = "".join(map(chr, codepoints)).lower()
                if token in lowered:
                    leaks.append(f"{path.name}: sensitive detector token embedded")
        self.assertFalse(leaks, "\n".join(leaks))

    def test_common_lowercase_homonym_does_not_block(self) -> None:
        root = self.make_repo()
        (root / "note.md").write_text(
            "Use the massimo available context.", encoding="utf-8"
        )
        findings = []
        GATE.scan_privacy_and_secrets(root, findings)
        self.assertNotIn(
            "DIRECT_IDENTIFIER", {item.code for item in findings}
        )

    def test_identifier_like_substring_inside_sha256_does_not_block(self) -> None:
        root = self.make_repo()
        digest = "".join((
            "6f", "83", "e1", "2f", "4e", "c4", "d6", "45", "4b", "ea", "02", "50",
            "b7", "5b", "41", "1c", "1f", "70", "06", "26", "4d", "63", "90", "30",
            "e1", "3e", "6e", "89", "90", "8e", "f5", "ed",
        ))
        (root / "note.md").write_text(
            f"sha256: {digest}",
            encoding="utf-8",
        )
        findings = []
        GATE.scan_privacy_and_secrets(root, findings)
        self.assertNotIn("DIRECT_IDENTIFIER", {item.code for item in findings})

    def test_uppercase_identifier_inside_compound_token_blocks(self) -> None:
        root = self.make_repo()
        sensitive = "".join(map(chr, (66, 101, 97))).upper()
        (root / "note.md").write_text(
            f"MODE: {sensitive}_PRIORITY_MATRIX", encoding="utf-8"
        )
        findings = []
        GATE.scan_privacy_and_secrets(root, findings)
        self.assertIn(
            "DIRECT_IDENTIFIER", {item.code for item in findings}
        )

    def test_case_linkage_blocks(self) -> None:
        root = self.make_repo()
        (root / "note.md").write_text(
            "The proband has maternal c.1057-2A>G and paternal Q230P.",
            encoding="utf-8",
        )
        findings = []
        GATE.scan_privacy_and_secrets(root, findings)
        codes = {item.code for item in findings}
        self.assertIn("REIDENTIFYING_VARIANT_COMBINATION", codes)
        self.assertIn("PARENT_OF_ORIGIN_LINKAGE", codes)
        self.assertIn("PARENT_OF_ORIGIN_VARIANT_LINKAGE", codes)

    def test_parent_origin_variant_blocks_without_person_noun(self) -> None:
        root = self.make_repo()
        (root / "note.md").write_text(
            "The maternally inherited allele was c.1057−2A>G.",
            encoding="utf-8",
        )
        findings = []
        GATE.scan_privacy_and_secrets(root, findings)
        self.assertIn(
            "PARENT_OF_ORIGIN_VARIANT_LINKAGE",
            {item.code for item in findings},
        )

    def test_italian_parent_origin_after_exact_variants_blocks(self) -> None:
        root = self.make_repo()
        (root / "note.md").write_text(
            "Genotipo compound eterozigote: c.1057-2A>G, materno, "
            "e Q230P, paterno.",
            encoding="utf-8",
        )
        findings = []
        GATE.scan_privacy_and_secrets(root, findings)
        codes = {item.code for item in findings}
        self.assertIn("PARENT_OF_ORIGIN_VARIANT_LINKAGE", codes)
        self.assertIn("REIDENTIFYING_VARIANT_COMBINATION", codes)

    def test_unrelated_negation_does_not_suppress_parent_origin(self) -> None:
        root = self.make_repo()
        (root / "note.md").write_text(
            'Not "find a stabilizer": the compound het has maternal '
            "c.1057-2A>G and paternal Q230P.",
            encoding="utf-8",
        )
        findings = []
        GATE.scan_privacy_and_secrets(root, findings)
        codes = {item.code for item in findings}
        self.assertIn("PARENT_OF_ORIGIN_VARIANT_LINKAGE", codes)
        self.assertIn("REIDENTIFYING_VARIANT_COMBINATION", codes)

    def test_parent_origin_reference_genotype_blocks_without_variant(self) -> None:
        root = self.make_repo()
        (root / "note.md").write_text(
            "The maternal side of the reference genotype is splice-related.",
            encoding="utf-8",
        )
        findings = []
        GATE.scan_privacy_and_secrets(root, findings)
        self.assertIn(
            "PARENT_OF_ORIGIN_REFERENCE_GENOTYPE",
            {item.code for item in findings},
        )

    def test_parent_origin_sides_pairing_blocks_without_exact_variants(self) -> None:
        root = self.make_repo()
        (root / "note.md").write_text(
            "A bypass would avoid both maternal splicing and paternal "
            "misfolding.",
            encoding="utf-8",
        )
        findings = []
        GATE.scan_privacy_and_secrets(root, findings)
        self.assertIn(
            "PARENT_OF_ORIGIN_PAIRING",
            {item.code for item in findings},
        )

    def _codes(self, root: Path) -> set[str]:
        findings: list = []
        GATE.scan_privacy_and_secrets(root, findings)
        return {item.code for item in findings}

    def test_pairing_attributed_to_a_published_study_is_reviewed_not_blocked(self) -> None:
        """🔴 The net's population is every paragraph naming both parents; its target is the
        private individual. A repository built on trio literature lives in the complement."""
        root = self.make_repo()
        (root / "note.md").write_text(
            "## FT-099\n**Paper:** PMID 39416860 — a published case report\n\n"
            "Both parents were heterozygous; the maternal allele was wild type for the "
            "second gene, which is what makes that allele paternal.\n",
            encoding="utf-8")
        codes = self._codes(root)
        self.assertIn("PARENT_OF_ORIGIN_ATTRIBUTED", codes)
        self.assertNotIn("PARENT_OF_ORIGIN_PAIRING", codes)

    def test_the_suppression_is_reported_and_not_silent(self) -> None:
        """A privacy exemption nobody can see in the output stops being reviewed."""
        root = self.make_repo()
        (root / "note.md").write_text(
            "## FT-099\n**Paper:** PMID 39416860\n\n"
            "maternal and paternal alleles both measured\n", encoding="utf-8")
        findings: list = []
        GATE.scan_privacy_and_secrets(root, findings)
        reviewed = [item for item in findings if item.code == "PARENT_OF_ORIGIN_ATTRIBUTED"]
        self.assertEqual(len(reviewed), 1)
        self.assertEqual(reviewed[0].severity, "REVIEW")

    def test_pairing_with_no_published_study_still_blocks(self) -> None:
        """The net is narrowed, not removed."""
        root = self.make_repo()
        (root / "note.md").write_text(
            "A bypass would avoid both maternal splicing and paternal misfolding.",
            encoding="utf-8")
        self.assertIn("PARENT_OF_ORIGIN_PAIRING", self._codes(root))

    def test_attribution_cannot_release_the_reference_genotype(self) -> None:
        """🔴 The safeguard that makes the narrowing safe: citing a paper must never be a way
        to publish the private individual's parents."""
        for marker in ("p.(Gln230Pro)", "c.1057-2 A>G", "the reference genotype"):
            with self.subTest(marker=marker):
                root = self.make_repo()
                (root / "note.md").write_text(
                    "## FT-099\n**Paper:** PMID 39416860\n\n"
                    f"maternal and paternal transmission of {marker} was recorded\n",
                    encoding="utf-8")
                codes = self._codes(root)
                self.assertIn("PARENT_OF_ORIGIN_PAIRING", codes)
                self.assertNotIn("PARENT_OF_ORIGIN_ATTRIBUTED", codes)

    def test_a_reference_variant_in_the_heading_still_blocks(self) -> None:
        """🔴 The fifth case, and the one that separates a safeguard from something that looks
        like one.

        The first version evaluated attribution on the WIDE window and the safeguard on the
        narrow block, so a heading naming `Q230P` widened what could suspend the rule without
        widening the rule's protection. A safeguard must be at least as wide as whatever can
        suspend it. Found by trying the neighbour of the declared test rather than the test.
        """
        root = self.make_repo()
        (root / "note.md").write_text(
            "## FT-099 p.(Gln230Pro) — PMID 39416860\n\n"
            "maternal and paternal transmission was recorded\n", encoding="utf-8")
        codes = self._codes(root)
        self.assertIn("PARENT_OF_ORIGIN_PAIRING", codes)
        self.assertNotIn("PARENT_OF_ORIGIN_ATTRIBUTED", codes)

    def test_a_json_record_is_scoped_to_the_file_and_that_is_deliberate(self) -> None:
        """🔴 JSON has no blank lines, so `semantic_blocks` yields a manifest WHOLE and every
        block-scoped rule silently becomes file-scoped — measured at 19 680 characters on
        `PMID39416860.json`. For a per-paper record the file is the record, so the attribution
        window says so instead of depending on where a formatter put its newlines."""
        text = '{\n "pmid": "39416860",\n "note": "maternal and paternal"\n}\n'
        window = GATE.attribution_window(text, 0, text, "x/PMID39416860.json")
        self.assertEqual(window, text)

    def test_a_markdown_window_reaches_back_to_its_heading_and_no_further(self) -> None:
        text = ("## FT-001\n**Paper:** PMID 11111111\n\nfirst para\n\n"
                "## FT-002\n\nmaternal and paternal here\n")
        offset = text.index("maternal")
        window = GATE.attribution_window(text, offset, "maternal and paternal here", "q.md")
        self.assertIn("FT-002", window)
        self.assertNotIn("PMID 11111111", window)

    def test_compound_genotype_blocks_without_proband_word(self) -> None:
        root = self.make_repo()
        (root / "note.md").write_text(
            "The biallelic genotype comprised p.(Gln230Pro) and "
            "c.1057–2 A>G in trans.",
            encoding="utf-8",
        )
        findings = []
        GATE.scan_privacy_and_secrets(root, findings)
        self.assertIn(
            "REIDENTIFYING_VARIANT_COMBINATION",
            {item.code for item in findings},
        )

    def test_cross_paragraph_compound_summary_blocks(self) -> None:
        root = self.make_repo()
        (root / "note.md").write_text(
            "Worked example one: Q230P is a folding defect.\n\n"
            "Worked example two: c.1057-2A>G is a splice defect.\n\n"
            "Together these two variants illustrate one "
            "compound-heterozygous genotype.\n",
            encoding="utf-8",
        )
        findings = []
        GATE.scan_privacy_and_secrets(root, findings)
        self.assertIn(
            "REIDENTIFYING_VARIANT_COMBINATION",
            {item.code for item in findings},
        )

    def test_affected_individual_carrying_both_variants_blocks(self) -> None:
        root = self.make_repo()
        (root / "note.md").write_text(
            "The affected individual carried both Q230P and c.1057-2A>G.",
            encoding="utf-8",
        )
        findings = []
        GATE.scan_privacy_and_secrets(root, findings)
        self.assertIn(
            "REIDENTIFYING_VARIANT_COMBINATION",
            {item.code for item in findings},
        )

    def test_explicitly_decoupled_parent_origin_policy_passes(self) -> None:
        root = self.make_repo()
        (root / "note.md").write_text(
            "Q230P is a public disease example; parent-of-origin has been "
            "removed and decoupled from every variant.",
            encoding="utf-8",
        )
        findings = []
        GATE.scan_privacy_and_secrets(root, findings)
        self.assertNotIn(
            "PARENT_OF_ORIGIN_VARIANT_LINKAGE",
            {item.code for item in findings},
        )

    def test_explicit_privacy_exclusion_is_not_case_linkage(self) -> None:
        root = self.make_repo()
        (root / "note.md").write_text(
            "All individual-linking material has been removed: no identified "
            "person, no clinical regimen, no parent-of-origin, no institution. "
            "Q230P is a disease-level worked example.",
            encoding="utf-8",
        )
        findings = []
        GATE.scan_privacy_and_secrets(root, findings)
        codes = {item.code for item in findings}
        self.assertNotIn("CLINICAL_CASE_LINKAGE", codes)
        self.assertNotIn("GEOGRAPHIC_CASE_LINKAGE", codes)
        self.assertNotIn("PARENT_OF_ORIGIN_LINKAGE", codes)

    def test_broken_relative_link_blocks(self) -> None:
        root = self.make_repo()
        (root / "README.md").write_text("[missing](missing.md)\n", encoding="utf-8")
        findings = []
        GATE.scan_links(root, findings)
        self.assertIn("BROKEN_MARKDOWN_LINK", {item.code for item in findings})

    def test_batch_commit_snapshot_directory_is_not_scanned(self) -> None:
        """Obeying the BATCH_COMMIT backup phase must not fail the gate.

        Phase 3 of the protocol requires a snapshot of the canonical files under `backup/`
        before any canonical write. The copies keep the originals' relative links, which no
        longer resolve from the snapshot's depth — so scanning them turned the mandatory
        backup into a BLOCK. A gate that punishes the backup teaches sessions to skip it.
        """
        root = self.make_repo()
        snapshot = root / "backup" / "snap_20260726_1600" / "registries"
        snapshot.mkdir(parents=True)
        (snapshot / "working_model_current.md").write_text(
            "[narrative view](../disease_model.md)\n", encoding="utf-8"
        )
        findings = []
        GATE.scan_links(root, findings)
        self.assertEqual([], [item.code for item in findings])

    def test_secret_blocks(self) -> None:
        root = self.make_repo()
        (root / "config.txt").write_text(
            "OPENAI_API_KEY=" + "sk-" + ("a" * 32),
            encoding="utf-8",
        )
        findings = []
        GATE.scan_privacy_and_secrets(root, findings)
        self.assertIn("OPENAI_KEY", {item.code for item in findings})

    def test_real_email_blocks_but_placeholders_pass(self) -> None:
        root = self.make_repo()
        (root / "contacts.md").write_text(
            "Contact researcher@real-lab.org.\n"
            "Example: your-email@example.com or gate@example.invalid.\n",
            encoding="utf-8",
        )
        findings = []
        GATE.scan_privacy_and_secrets(root, findings)
        email_findings = [
            item for item in findings if item.code == "EMAIL_ADDRESS"
        ]
        self.assertEqual(1, len(email_findings))
        self.assertEqual(1, email_findings[0].line)

    def test_nested_disease_data_requires_provenance(self) -> None:
        root = self.make_repo()
        asset = root / "disease-models" / "wwox" / "analysis" / "data"
        asset.mkdir(parents=True)
        (asset / "result.csv").write_text("x\n1\n", encoding="utf-8")
        (root / "DATA_SOURCES.md").write_text(
            "# Data sources\nNo declared assets.\n", encoding="utf-8"
        )
        findings = []
        GATE.scan_provenance(root, findings)
        self.assertIn(
            "UNDECLARED_DATA_ASSET", {item.code for item in findings}
        )

    def test_nested_disease_data_matches_declared_scope(self) -> None:
        root = self.make_repo()
        asset = root / "disease-models" / "wwox" / "analysis" / "data"
        asset.mkdir(parents=True)
        (asset / "result.csv").write_text("x\n1\n", encoding="utf-8")
        (root / "DATA_SOURCES.md").write_text(
            "# Data sources\n`analysis/data/*.csv`\n", encoding="utf-8"
        )
        findings = []
        GATE.scan_provenance(root, findings)
        self.assertNotIn(
            "UNDECLARED_DATA_ASSET", {item.code for item in findings}
        )

    def test_public_variants_without_person_link_do_not_trigger_combo(self) -> None:
        root = self.make_repo()
        (root / "examples.md").write_text(
            "Q230P is a public worked example.\n"
            "c.1057-2A>G is independently discussed as a splice example.\n",
            encoding="utf-8",
        )
        findings = []
        GATE.scan_privacy_and_secrets(root, findings)
        self.assertNotIn(
            "REIDENTIFYING_VARIANT_COMBINATION",
            {item.code for item in findings},
        )

    def test_clean_git_archive_executes_gate(self) -> None:
        root = self.make_repo()
        (root / "scripts").mkdir()
        shutil.copy2(GATE_PATH, root / "scripts" / "public_release_gate.py")
        (root / "DATA_SOURCES.md").write_text(
            "# Data sources\nNo shipped data assets.\n", encoding="utf-8"
        )
        (root / "THIRD_PARTY_NOTICES.md").write_text(
            "# Third-party notices\nNone.\n", encoding="utf-8"
        )
        (root / "_external_repos").mkdir()
        (root / "_external_repos" / "MANIFEST.md").write_text(
            "# External repositories\nNone vendored.\n", encoding="utf-8"
        )
        workflow = root / ".github" / "workflows"
        workflow.mkdir(parents=True)
        (workflow / "public-release-gate.yml").write_text(
            "name: test\n", encoding="utf-8"
        )
        commands = [
            ["git", "init", "-q"],
            ["git", "config", "user.email", "gate@example.invalid"],
            ["git", "config", "user.name", "Release Gate Test"],
            ["git", "add", "."],
            ["git", "commit", "-qm", "fixture"],
        ]
        for command in commands:
            subprocess.run(command, cwd=root, check=True)
        findings = []
        GATE.run_clean_clone(root, findings, None)
        self.assertNotIn(
            "CLEAN_CLONE_GATE_FAILED",
            {item.code for item in findings},
            msg="\n".join(item.message for item in findings),
        )


class UnpublishableExemptionTests(unittest.TestCase):
    """The scan exemption must key on publishability, not on directory name.

    A gitignored *and* untracked file cannot reach a published clone, so scanning
    it only produces noise about deliberately private material. The moment the
    same file is force-added it becomes publishable, and the gate must see it
    again. A directory allowlist cannot express that distinction — it exempts the
    dangerous case along with the safe one.
    """

    def make_git_repo(self) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "README.md").write_text("# Public project\n", encoding="utf-8")
        (root / ".gitignore").write_text("grants/\n", encoding="utf-8")
        for command in (
            ["git", "init", "-q"],
            ["git", "config", "user.email", "gate@example.invalid"],
            ["git", "config", "user.name", "Release Gate Test"],
            ["git", "add", "README.md", ".gitignore"],
            ["git", "commit", "-qm", "fixture"],
        ):
            subprocess.run(command, cwd=root, check=True)
        return root

    def write_sensitive_dossier(self, root: Path) -> Path:
        dossier = root / "grants" / "call" / "answers.md"
        dossier.parent.mkdir(parents=True)
        dossier.write_text(
            "Primary contact: someone@example.org\n", encoding="utf-8"
        )
        return dossier

    def test_untracked_gitignored_dossier_is_not_scanned(self) -> None:
        root = self.make_git_repo()
        self.write_sensitive_dossier(root)
        scanned = {path.relative_to(root).as_posix() for path in GATE.iter_files(root)}
        self.assertNotIn("grants/call/answers.md", scanned)

    def test_force_added_dossier_is_scanned_and_blocks(self) -> None:
        root = self.make_git_repo()
        self.write_sensitive_dossier(root)
        subprocess.run(
            ["git", "add", "-f", "grants/call/answers.md"], cwd=root, check=True
        )

        scanned = {path.relative_to(root).as_posix() for path in GATE.iter_files(root)}
        self.assertIn(
            "grants/call/answers.md",
            scanned,
            msg="a tracked file is publishable and must never be exempt",
        )

        findings: list = []
        GATE.scan_privacy_and_secrets(root, findings)
        offending = {
            item.code for item in findings
            if item.path == "grants/call/answers.md"
        }
        self.assertIn("EMAIL_ADDRESS", offending)

    def test_exemption_is_empty_outside_a_git_checkout(self) -> None:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.assertEqual(frozenset(), GATE.unpublishable_paths(Path(temp.name)))


class NestedCheckoutTests(unittest.TestCase):
    """A checkout inside the checkout is not this repository's publishable material.

    `git ls-files --others --ignored` does not descend into one: it returns the directory
    as a single entry with a trailing slash. Exempting by exact string therefore exempted
    the directory and nothing in it, and the gate scanned every file of the nested
    checkout — including its own negative fixtures, which are privacy-violating on purpose.

    Measured when per-session worktrees arrived: 340 files scanned, 37 BLOCKs, all false.
    These tests mount a nested checkout so the next walker added to this module cannot
    quietly reintroduce it.
    """

    def mount(self) -> tuple[Path, Path]:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "README.md").write_text("# Public project\n", encoding="utf-8")
        (root / ".gitignore").write_text(".claude/worktrees/\n", encoding="utf-8")
        for command in (
            ["git", "init", "-q"],
            ["git", "config", "user.email", "gate@example.invalid"],
            ["git", "config", "user.name", "Release Gate Test"],
            ["git", "add", "README.md", ".gitignore"],
            ["git", "commit", "-qm", "fixture"],
        ):
            subprocess.run(command, cwd=root, check=True)

        nested = root / ".claude" / "worktrees" / "session"
        nested.mkdir(parents=True)
        subprocess.run(["git", "init", "-q"], cwd=nested, check=True)
        offending = nested / "scripts" / "fixture.py"
        offending.parent.mkdir()
        # The shape that produced the false positives: a negative fixture whose whole job is
        # to contain a marker the gate must fire on — in a checkout that is not ours.
        offending.write_text("CONTACT = 'someone@example.org'\n", encoding="utf-8")
        return root, offending

    def test_files_of_a_nested_checkout_are_not_scanned(self) -> None:
        root, offending = self.mount()
        scanned = {path.relative_to(root).as_posix() for path in GATE.iter_files(root)}
        self.assertNotIn(offending.relative_to(root).as_posix(), scanned)
        self.assertIn("README.md", scanned)

    def test_a_nested_checkout_raises_no_finding(self) -> None:
        root, _ = self.mount()
        findings: list = []
        GATE.scan_privacy_and_secrets(root, findings)
        self.assertEqual(
            [], [item for item in findings if ".claude/worktrees/" in item.path],
            msg="a finding about another checkout is noise the real signal hides behind")

    def test_the_exemption_is_a_prefix_not_an_exact_path(self) -> None:
        """The unit underneath, stated directly so a refactor cannot lose it."""
        exempt = frozenset({".claude/worktrees/"})
        self.assertTrue(GATE.is_exempt(".claude/worktrees/session/scripts/fixture.py", exempt))
        self.assertTrue(GATE.is_exempt(".claude/worktrees/", exempt))
        self.assertFalse(GATE.is_exempt(".claude/settings.json", exempt))
        self.assertFalse(
            GATE.is_exempt("grants/call/answers.md", frozenset({"grants/call/answers.md/"})),
            msg="a file entry never gains prefix authority over unrelated paths")

    def test_a_nested_checkout_outside_gitignore_is_still_skipped(self) -> None:
        """The case the prefix exemption cannot reach, and the reason pruning also exists.

        Mutation-tested: disabling `is_nested_checkout` left every other test in this class
        green, because `.claude/worktrees/` is gitignored and the prefix rule already
        covered it. A checkout mounted somewhere *not* ignored is invisible to
        `ls-files --others --ignored` altogether — nothing exempts it, and only the walker
        refusing to descend keeps another repository's files out of this gate.
        """
        root, _ = self.mount()
        stray = root / "vendor" / "other-repo"
        stray.mkdir(parents=True)
        subprocess.run(["git", "init", "-q"], cwd=stray, check=True)
        (stray / "leak.md").write_text("Contact: someone@example.org\n", encoding="utf-8")

        scanned = {path.relative_to(root).as_posix() for path in GATE.iter_files(root)}
        self.assertNotIn("vendor/other-repo/leak.md", scanned)
        self.assertNotIn("vendor/other-repo", {
            path.relative_to(root).as_posix() for path in GATE.walk_publishable(root)})

    def test_directories_of_a_nested_checkout_do_not_enter_the_name_index(self) -> None:
        """The second walker: wikilink resolution indexes directory names too."""
        root, _ = self.mount()
        walked = {path.relative_to(root).as_posix() for path in GATE.walk_publishable(root)}
        self.assertFalse({item for item in walked if item.startswith(".claude/worktrees/")})


if __name__ == "__main__":
    unittest.main()
