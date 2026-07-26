#!/usr/bin/env python3
"""Validate the reusable public agent layer referenced by LEGEND skills."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / ".claude" / "agents"
EXPECTED = {
    "fulltext-dossier.md": "fulltext-dossier",
    "legend-deepdive.md": "legend-deepdive",
    "research-group-analyst.md": "research-group-analyst",
    "study-intake-triage.md": "study-intake-triage",
    "wwox-scout.md": "wwox-scout",
}
LEGACY_ROOT = re.compile(
    r"(?m)(?:^|[`/])(?:00_state|01_instruction|02_current|03_meta|"
    r"04_research|05_analysis|06_operational|07_protocols|08_master|"
    r"09_private)(?:/|`)"
)


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---\n", 4)
    return "" if end < 0 else text[4:end]


class AgentPipelineContractTests(unittest.TestCase):
    def test_all_referenced_public_agents_exist(self) -> None:
        missing = [
            str((AGENTS / filename).relative_to(ROOT))
            for filename in EXPECTED
            if not (AGENTS / filename).is_file()
        ]
        self.assertFalse(
            missing,
            "Reusable agents referenced by the public pipeline are missing:\n"
            + "\n".join(missing),
        )

    def test_agent_frontmatter_and_public_paths(self) -> None:
        failures = []
        for filename, expected_name in EXPECTED.items():
            path = AGENTS / filename
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            header = frontmatter(text)
            if not header:
                failures.append(f"{filename}: missing YAML frontmatter")
                continue
            name = re.search(r"(?m)^name:\s*['\"]?([^'\"\n]+)", header)
            description = re.search(r"(?m)^description:\s*(.+)", header)
            if not name or name.group(1).strip() != expected_name:
                failures.append(f"{filename}: name must be {expected_name}")
            if not description or len(description.group(1).strip()) < 20:
                failures.append(f"{filename}: substantive description missing")
            legacy = LEGACY_ROOT.search(text)
            if legacy:
                line = text.count("\n", 0, legacy.start()) + 1
                failures.append(
                    f"{filename}:{line}: legacy private-layer path remains"
                )
        self.assertFalse(failures, "\n".join(failures))

    def test_skill_named_agent_dependencies_are_materialized(self) -> None:
        declared = set(EXPECTED.values())
        unresolved = []
        for path in sorted((ROOT / ".claude" / "skills").rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            for name in declared:
                if re.search(rf"(?i)`?{re.escape(name)}`?.{{0,40}}subagent", text):
                    if not (AGENTS / f"{name}.md").is_file():
                        unresolved.append(
                            f"{path.relative_to(ROOT)} -> .claude/agents/{name}.md"
                        )
        self.assertFalse(
            unresolved,
            "Named subagent dependencies do not resolve:\n"
            + "\n".join(unresolved),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
