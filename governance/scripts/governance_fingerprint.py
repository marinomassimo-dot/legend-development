#!/usr/bin/env python3
"""Compose APPLICABLE_GOVERNANCE_FINGERPRINT for a role, per plan_defined_parameters.md § P2.

The pertinence sets are NOT duplicated here. They are parsed out of § P2.2 of
plan_defined_parameters.md, so the governance document stays the single source of truth and
this script cannot drift from it: if the prose changes, the computed fingerprint changes with
it, and if the prose stops parsing, this fails loudly instead of using a stale copy.

  governance_fingerprint.py compose --role plan
  governance_fingerprint.py compose --all
  governance_fingerprint.py inputs --role scientist
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

GOVERNANCE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = GOVERNANCE_DIR.parent
PARAMETERS = GOVERNANCE_DIR / "plan_defined_parameters.md"

ROLE_CONTRACT_PLACEHOLDER = "<the actor's own role contract>"
# Scientists A/B/C share one contract by design (roles/scientist.md); see roles/scientist.md.
ROLE_CONTRACT = {
    "plan": "roles/plan.md",
    "mirror": "roles/mirror.md",
    "orchestrator": "roles/orchestrator.md",
    "scientist": "roles/scientist.md",
    # Junior Harness Engineer — DEC-20260905-AGILE-HARNESS-MODE, LEGEND_CORE §21e.
    "junior-harness": "roles/junior_harness.md",
}


class CompositionError(RuntimeError):
    """The governance could not be read as a composition. Never fall back to a default."""


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise CompositionError(f"cannot read {path}: {exc}") from exc


def _annex_path(letter: str) -> Path:
    matches = sorted(GOVERNANCE_DIR.glob(f"annex_{letter.lower()}_*.md"))
    if len(matches) != 1:
        raise CompositionError(
            f"expected exactly one file for Annex {letter.upper()}, found {len(matches)}"
        )
    return matches[0]


def _resolve(token: str) -> str:
    """Turn one governance reference into a canonical identifier.

    'Annex C'                              -> governance/annex_c_review_protocol.md
    'Annex J § J.1'                        -> governance/annex_j_runtime_control_plane.md#J.1
    'annex_a_task_contract.md'             -> governance/annex_a_task_contract.md
    'annex_j_...md § J.0'                  -> governance/annex_j_...md#J.0
    """
    token = token.strip().strip("`").strip()
    section = None
    if "§" in token:
        token, section = (part.strip() for part in token.split("§", 1))
        token = token.strip()

    match = re.fullmatch(r"Annex\s+([A-J])", token, flags=re.IGNORECASE)
    if match:
        rel = _annex_path(match.group(1)).relative_to(REPO_ROOT).as_posix()
    elif token.endswith(".md"):
        candidate = GOVERNANCE_DIR / token
        if not candidate.exists():
            candidate = REPO_ROOT / token
        if not candidate.exists():
            raise CompositionError(f"referenced artifact does not exist: {token}")
        rel = candidate.relative_to(REPO_ROOT).as_posix()
    else:
        raise CompositionError(f"unrecognised governance reference: {token!r}")

    return f"{rel}#{section}" if section else rel


def _extract_section(text: str, section: str) -> str:
    """Bytes of one section: its heading line up to the next heading of equal or higher level."""
    pattern = re.compile(
        rf"^(?P<hashes>#{{1,6}})\s+{re.escape(section)}(?![0-9])", re.MULTILINE
    )
    match = pattern.search(text)
    if not match:
        raise CompositionError(f"section {section} not found")
    level = len(match.group("hashes"))
    tail = text[match.end():]
    following = re.search(rf"^#{{1,{level}}}\s", tail, re.MULTILINE)
    end = match.end() + (following.start() if following else len(tail))
    return text[match.start():end]


def _digest(identifier: str) -> str:
    path_part, _, section = identifier.partition("#")
    text = _read(REPO_ROOT / path_part)
    if section:
        text = _extract_section(text, section)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def parse_pertinence_sets() -> tuple[list[str], dict[str, list[str]]]:
    """Read CORE and the per-role additions out of § P2.2. Raise rather than guess."""
    text = _read(PARAMETERS)
    start = text.find("### P2.2")
    if start == -1:
        raise CompositionError("§ P2.2 not found in plan_defined_parameters.md")
    section = text[start:]
    section = section[: section.find("\n### ", 1) if "\n### " in section[1:] else len(section)]

    block = re.search(r"```\n(CORE\s*=.*?)```", section, re.DOTALL)
    if not block:
        raise CompositionError("the CORE block in § P2.2 did not parse")
    core: list[str] = []
    for raw in block.group(1).splitlines():
        line = raw.strip()
        if not line:
            continue
        line = re.sub(r"^CORE\s*=\s*", "", line)
        line = re.sub(r"^\+\s*", "", line)
        core.append(line)
    if ROLE_CONTRACT_PLACEHOLDER not in core:
        raise CompositionError("CORE must include the actor's own role contract")

    roles: dict[str, list[str]] = {}
    for row in re.finditer(r"^\|\s*`([a-z-]+)`[^|]*\|([^|]*)\|", section, re.MULTILINE):
        role, additions = row.group(1), row.group(2)
        roles[role] = [tok.strip() for tok in additions.split(",") if tok.strip()]
    if not roles:
        raise CompositionError("no per-role rows parsed from § P2.2")
    return core, roles


def inputs_for(role: str) -> list[str]:
    core, roles = parse_pertinence_sets()
    if role not in roles:
        raise CompositionError(f"unknown role {role!r}; known: {', '.join(sorted(roles))}")
    if role not in ROLE_CONTRACT:
        raise CompositionError(f"no role contract mapped for {role!r}")

    identifiers = set()
    for token in core:
        if token == ROLE_CONTRACT_PLACEHOLDER:
            contract = REPO_ROOT / ROLE_CONTRACT[role]
            if not contract.exists():
                raise CompositionError(f"role contract missing: {ROLE_CONTRACT[role]}")
            identifiers.add(ROLE_CONTRACT[role])
        else:
            identifiers.add(_resolve(token))
    for token in roles[role]:
        identifiers.add(_resolve(token))
    return sorted(identifiers)


def compose(role: str) -> tuple[str, list[tuple[str, str]]]:
    pairs = [(identifier, _digest(identifier)) for identifier in inputs_for(role)]
    serialized = "".join(f"{identifier}:{digest}\n" for identifier, digest in pairs)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest(), pairs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("compose", "inputs"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--role")
        cmd.add_argument("--all", action="store_true")
    args = parser.parse_args()

    try:
        _, roles = parse_pertinence_sets()
        targets = sorted(roles) if args.all else [args.role]
        if not args.all and not args.role:
            parser.error("give --role or --all")
        for role in targets:
            fingerprint, pairs = compose(role)
            if args.command == "inputs":
                print(f"{role}:")
                for identifier, digest in pairs:
                    print(f"  {digest[:12]}…  {identifier}")
            print(f"{role}\t{fingerprint}")
    except CompositionError as exc:
        print(f"COMPOSITION FAILED: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
