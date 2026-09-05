#!/usr/bin/env python3
"""Fail closed when a public skill exists but cannot be loaded.

The public release must preserve executable capabilities, not merely retain
directories named like skills.  This dependency-free check validates the
frontmatter subset used by the repository and catches YAML's ``colon + space``
plain-scalar failure mode.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".claude" / "skills"
EXPECTED_COUNT = 22
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EXPECTED_NON_CONTENT_ASSETS = {
    "legend-batch-inferential-sweep/scripts/batch_inferential_sweep.py",
    "legend-batch-inferential-sweep/scripts/test_batch_inferential_sweep.py",
    "legend-dashboard/agents/openai.yaml",
    "legend-hypothesis-forge/scripts/kg_thin_slice.py",
    "legend-lint-repair-plan/agents/openai.yaml",
    "legend-proband-priority-matrix/scripts/score_proband_priority.py",
    "legend-research-loop/agents/openai.yaml",
    "legend-study-intake-triage/scripts/retraction_check.py",
    "legend-study-intake-triage/scripts/study_dedup_triage.py",
    "legend-study-intake-triage/scripts/test_study_dedup_triage.py",
}


def frontmatter(skill_file: Path) -> tuple[dict[str, str], list[str]]:
    lines = skill_file.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    if not lines or lines[0] != "---":
        return {}, ["missing opening frontmatter delimiter"]
    try:
        closing = lines.index("---", 1)
    except ValueError:
        return {}, ["missing closing frontmatter delimiter"]

    fields: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:closing], 2):
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"line {line_number}: malformed field")
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if key in fields:
            errors.append(f"line {line_number}: duplicate field {key}")
        fields[key] = value
        if (
            value
            and not value.startswith(("'", '"', "|", ">"))
            and ": " in value
        ):
            errors.append(
                f"line {line_number}: unquoted colon makes invalid YAML"
            )
    return fields, errors


def package_errors() -> list[str]:
    errors: list[str] = []
    skill_files = sorted(SKILLS.glob("*/SKILL.md"))
    if len(skill_files) != EXPECTED_COUNT:
        errors.append(
            f"expected {EXPECTED_COUNT} skill packages, found {len(skill_files)}"
        )
    for skill_file in skill_files:
        relative = skill_file.relative_to(ROOT)
        fields, local_errors = frontmatter(skill_file)
        name = fields.get("name", "").strip("\"'")
        description = fields.get("description", "").strip()
        if not name:
            local_errors.append("missing name")
        elif not NAME.fullmatch(name):
            local_errors.append(f"invalid skill name: {name}")
        elif name != skill_file.parent.name:
            local_errors.append(
                f"name {name!r} does not match directory {skill_file.parent.name!r}"
            )
        if not description:
            local_errors.append("missing description")
        for error in local_errors:
            errors.append(f"{relative}: {error}")
    return errors


# Reader-facing documents that state how many skills ship. The count is a promise about
# the repository's contents, so it is derived from the filesystem and never trusted as prose.
COUNT_CLAIM_DOCUMENTS = (
    "README.md", "SKILLS.md", "CLAUDE.md", "AGENTS.md", "FAQ.md",
    "ARCHITECTURE.md", "CITATION.cff", "framework/ADOPTING.md",
)
# Matches "20 skills", "20 composable skills", "20 reusable workflows" and the subset form
# "17 of the 20 skills", where it is the second number that must equal the shipped count.
COUNT_CLAIM = re.compile(
    r"(\d+)\s+(?:of\s+the\s+(\d+)\s+)?"
    r"(?:composable\s+|operational\s+|reusable\s+)?(?:skills?|reusable\s+workflows)\b"
)


class SkillPackageTests(unittest.TestCase):
    def test_documented_skill_count_matches_what_ships(self) -> None:
        """Prose that counts the skills must agree with the directory that holds them.

        `EXPECTED_COUNT` was already 20 while every reader-facing document still said 19:
        the machine-readable count was updated when `legend-session-self-eval` was added and
        the prose was not, so the repository under-reported its own contents and no check
        objected. A count is a claim about what a clone contains — the same class of claim
        the maturity vocabulary exists to keep honest — so it is derived here, not asserted.
        """
        shipped = len([path for path in SKILLS.iterdir() if path.is_dir()])
        self.assertEqual(EXPECTED_COUNT, shipped)
        stale = []
        for relative in COUNT_CLAIM_DOCUMENTS:
            text = " ".join((ROOT / relative).read_text(encoding="utf-8").split())
            for match in COUNT_CLAIM.finditer(text):
                claimed = int(match.group(2) or match.group(1))
                if claimed != shipped:
                    stale.append(f"{relative}: {match.group(0).strip()!r} (ships {shipped})")
        self.assertEqual(
            [],
            stale,
            "Documented skill counts disagree with the shipped skills:\n" + "\n".join(stale),
        )

    def test_every_shipped_skill_appears_in_the_catalogue(self) -> None:
        """SKILLS.md calls itself the catalogue; a skill missing from it is unfindable.

        `legend-session-self-eval` shipped, was referenced by the CLAUDE.md bootstrap table,
        and appeared in neither SKILLS.md nor ARCHITECTURE.md — present in the clone and
        invisible to the reader.
        """
        catalogue = (ROOT / "SKILLS.md").read_text(encoding="utf-8")
        architecture = (ROOT / "ARCHITECTURE.md").read_text(encoding="utf-8")
        missing = [
            f"{path.name}: absent from {'SKILLS.md' if path.name not in catalogue else 'ARCHITECTURE.md'}"
            for path in sorted(SKILLS.iterdir())
            if path.is_dir() and (path.name not in catalogue or path.name not in architecture)
        ]
        self.assertEqual([], missing, "Shipped skills missing from the catalogue:\n" + "\n".join(missing))

    def test_all_public_skills_are_loadable(self) -> None:
        errors = package_errors()
        self.assertEqual(
            [],
            errors,
            "Invalid public skill packages:\n" + "\n".join(errors),
        )

    def test_non_content_skill_assets_are_complete(self) -> None:
        observed = {
            path.relative_to(SKILLS).as_posix()
            for path in SKILLS.rglob("*")
            if path.is_file()
            and path.suffix.lower() not in {".md", ".json", ".csv"}
            and "__pycache__" not in path.parts
        }
        self.assertEqual(EXPECTED_NON_CONTENT_ASSETS, observed)

    def test_skill_python_assets_compile_without_writing_bytecode(self) -> None:
        failures = []
        for relative in sorted(EXPECTED_NON_CONTENT_ASSETS):
            if not relative.endswith(".py"):
                continue
            path = SKILLS / relative
            try:
                compile(path.read_text(encoding="utf-8"), str(path), "exec")
            except SyntaxError as exc:
                failures.append(f"{relative}: {exc}")
        self.assertFalse(failures, "\n".join(failures))

    def test_agent_metadata_has_required_interface_fields(self) -> None:
        failures = []
        for relative in sorted(EXPECTED_NON_CONTENT_ASSETS):
            if not relative.endswith("/agents/openai.yaml"):
                continue
            text = (SKILLS / relative).read_text(encoding="utf-8")
            for field in ("interface:", "display_name:", "short_description:", "default_prompt:"):
                if field not in text:
                    failures.append(f"{relative}: missing {field}")
        self.assertFalse(failures, "\n".join(failures))


if __name__ == "__main__":
    unittest.main(verbosity=2)
