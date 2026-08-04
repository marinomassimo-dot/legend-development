#!/usr/bin/env python3
"""Phase 4, offline: validate the dry-run YAML against the pinned DisMech schema.

The field mapping was written by reading the schema, and reading is not checking. This
compares what the exporter emits against what `dismech.yaml` actually declares: slot names
per class, permissible enum values, required slots.

It is not the upstream validator. `just qc` also resolves ontology terms and matches
snippets against cached references, and neither is possible here without cloning the
repository and reaching the network. What this does check is the part that fails silently:
a key the schema does not have is simply ignored by a permissive reader, and a key the
schema requires is missing without anything saying so.

The schema is supplied as a file so the check runs offline and against a pinned blob:

    curl / gh api ... > dismech.yaml     # blob e1a5bde3…
    validate_dismech_yaml.py --schema dismech.yaml --dir staging/dismech_dryrun
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

PINNED_BLOB = "e1a5bde3b0d35b23808018648a8fc267dc96b10c"


def git_blob_sha(payload: bytes) -> str:
    """Git's object id for a blob, so the pin can be checked without git."""
    header = f"blob {len(payload)}\0".encode()
    return hashlib.sha1(header + payload).hexdigest()


def parse_classes(schema: str) -> dict[str, dict]:
    """Slot names per class, following is_a and slot_usage. Deliberately shallow."""
    classes: dict[str, dict] = {}
    block = re.search(r"\nclasses:\n(.*?)(?=\n[a-z_]+:\n|\Z)", schema, re.S)
    body = block.group(1) if block else schema
    for match in re.finditer(r"\n  ([A-Z]\w+):\n(.*?)(?=\n  [A-Z]\w+:\n|\Z)", body, re.S):
        name, definition = match.group(1), match.group(2)
        slots = re.findall(r"^\s{4,6}- (\w+)\s*$", definition, re.M)
        parent = re.search(r"^\s+is_a:\s*(\w+)", definition, re.M)
        classes[name] = {"slots": set(slots), "is_a": parent.group(1) if parent else None}
    for name, entry in classes.items():
        seen, parent = set(entry["slots"]), entry["is_a"]
        while parent and parent in classes:
            seen |= classes[parent]["slots"]
            parent = classes[parent]["is_a"]
        entry["effective"] = seen
    return classes


def parse_enums(schema: str) -> dict[str, set[str]]:
    enums: dict[str, set[str]] = {}
    for match in re.finditer(r"\n  (\w+Enum):\n(.*?)(?=\n  \w+:\n|\Z)", schema, re.S):
        enums[match.group(1)] = set(re.findall(r"^\s{6}([A-Z][A-Z0-9_]+):", match.group(2), re.M))
    return enums


def load_yaml(text: str):
    """Read back exactly what the exporter's dumper writes. Nothing more."""
    def parse(lines, indent):
        out, index = None, 0
        while index < len(lines):
            raw = lines[index]
            if not raw.strip():
                index += 1
                continue
            level = len(raw) - len(raw.lstrip())
            if level < indent:
                break
            stripped = raw.strip()
            if stripped == "-" or stripped.startswith("- "):
                if out is None:
                    out = []
                if stripped == "-":
                    child, used = parse(lines[index + 1:], level + 2)
                    out.append(child)
                    index += 1 + used
                else:
                    out.append(scalar(stripped[2:]))
                    index += 1
                continue
            key, _, rest = stripped.partition(":")
            if out is None:
                out = {}
            rest = rest.strip()
            if rest:
                out[key] = scalar(rest)
                index += 1
            else:
                child, used = parse(lines[index + 1:], level + 1)
                out[key] = child if child is not None else {}
                index += 1 + used
        return out, index

    def scalar(text):
        text = text.strip()
        if text in ("null", ""):
            return None
        if text in ("true", "false"):
            return text == "true"
        if text.startswith('"'):
            return json.loads(text)
        if text in ("{}", "[]"):
            return {} if text == "{}" else []
        return text

    parsed, _ = parse(text.splitlines(), 0)
    return parsed


def check(entry: dict, classes: dict, enums: dict, name: str) -> list[str]:
    problems: list[str] = []
    disease = classes.get("Disease", {}).get("effective", set())
    patho = classes.get("Pathophysiology", {}).get("effective", set())
    evidence = classes.get("EvidenceItem", {}).get("effective", set())
    confidence = enums.get("MechanismConfidenceEnum", set())
    supports = enums.get("EvidenceItemSupportEnum", set())
    sources = enums.get("EvidenceSourceEnum", set())

    for key in entry:
        if key not in disease:
            problems.append(f"{name}: Disease has no slot '{key}'")
    if "name" not in entry:
        problems.append(f"{name}: Disease.name is required")

    for position, node in enumerate(entry.get("pathophysiology") or [], 1):
        where = f"{name}: pathophysiology[{position}]"
        for key in node:
            if key not in patho:
                problems.append(f"{where}: Pathophysiology has no slot '{key}'")
        if node.get("mechanism_confidence") not in confidence:
            problems.append(f"{where}: mechanism_confidence "
                            f"{node.get('mechanism_confidence')!r} not in the enum")
        for e_position, item in enumerate(node.get("evidence") or [], 1):
            spot = f"{where}.evidence[{e_position}]"
            for key in item:
                if key not in evidence:
                    problems.append(f"{spot}: EvidenceItem has no slot '{key}'")
            if item.get("supports") not in supports:
                problems.append(f"{spot}: supports {item.get('supports')!r} not in the enum")
            if item.get("evidence_source") not in sources:
                problems.append(f"{spot}: evidence_source "
                                f"{item.get('evidence_source')!r} not in the enum")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--dir", type=Path, required=True)
    arguments = parser.parse_args()

    payload = arguments.schema.read_bytes()
    actual = git_blob_sha(payload)
    if actual != PINNED_BLOB:
        print(f"REFUSED: schema blob {actual} is not the pinned {PINNED_BLOB}")
        return 2
    print(f"schema pin verified: {actual}")

    schema = payload.decode("utf-8")
    classes, enums = parse_classes(schema), parse_enums(schema)

    total = 0
    for path in sorted(arguments.dir.glob("MONDO_*.yaml")):
        entry = load_yaml(path.read_text(encoding="utf-8"))
        problems = check(entry, classes, enums, path.name)
        total += len(problems)
        print(f"\n{path.name}: {len(problems)} problem(s)")
        seen = set()
        for problem in problems:
            key = re.sub(r"\[\d+\]", "[n]", problem)
            if key in seen:
                continue
            seen.add(key)
            print(f"  {key}")
        if len(problems) > len(seen):
            print(f"  … {len(problems) - len(seen)} further occurrences of the same shapes")
    print(f"\nTOTAL: {total} schema problem(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
