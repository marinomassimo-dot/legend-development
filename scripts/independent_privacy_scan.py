#!/usr/bin/env python3
"""Independent, read-only privacy scan for the public staging tree.

This scanner deliberately does not import or reuse public_release_gate.py.
It prints findings to stdout and never writes to the scanned repository.

Exit codes:
  0  no findings
  2  one or more findings
  3  invalid root or unreadable input
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


TEXT_SUFFIXES = {
    ".cfg",
    ".csv",
    ".ini",
    ".json",
    ".md",
    ".py",
    ".rst",
    ".toml",
    ".tsv",
    ".txt",
    ".yaml",
    ".yml",
}

SKIP_DIRS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "node_modules",
    "venv",
}

# The scanner source contains its own detector vocabulary and is excluded to
# avoid self-findings. The release runbooks contain commands, not case data.
SELF_PATH = Path("scripts/independent_privacy_scan.py")

ITALIAN_CITIES = (
    "Ancona",
    "Aosta",
    "Bari",
    "Bologna",
    "Bolzano",
    "Brescia",
    "Cagliari",
    "Catania",
    "Catanzaro",
    "Ferrara",
    "Firenze",
    "Florence",
    "Genova",
    "Genoa",
    "L'Aquila",
    "Messina",
    "Milano",
    "Milan",
    "Modena",
    "Monza",
    "Napoli",
    "Naples",
    "Padova",
    "Palermo",
    "Parma",
    "Pavia",
    "Perugia",
    "Pisa",
    "Potenza",
    "Reggio Calabria",
    "Reggio Emilia",
    "Roma",
    "Rome",
    "Salerno",
    "Siena",
    "Torino",
    "Turin",
    "Trento",
    "Trieste",
    "Venezia",
    "Venice",
    "Verona",
)

# Codepoint assembly keeps the scanner capable of detecting legacy private
# name tokens without embedding those same tokens verbatim in the public tree.
PRIVATE_FULL_NAME_CODEPOINTS = (
    (66, 101, 97, 116, 114, 105, 99, 101),
    (66, 105, 109, 98, 97),
    (77, 97, 115, 115, 105, 109, 111),
)
PRIVATE_SHORT_NAME_CODEPOINTS = (66, 101, 97)
PRIVATE_IDENTIFIER_DIGESTS = frozenset({
    "56a9baaa78e21fd28508d820a750a3bdab648145046ae5d2e91ef2480fcb240b",
    "1075bbd8b99ffc4f7392d08031e6d50389395a43a7d4cf7c5a992c2df5ade9fe",
    "91a1dafb023759ab2b7668304bb56db4a166c343b17ea4809c0536bf1dd4e4b8",
    "f4100df23c7a789e35087608882def10fccba81b106a8b9af573032ec94d1419",
    "edb1270b1e407a89a46c02743cbe544e788e511d418dd83f8580985c525e2f41",
})
CASEFOLD_IDENTIFIER_DIGESTS = frozenset({
    "b6e1557a1ed3900d7be8e28bb5f137d91812f31e59a90ceddac0276bc532d18e",
    "07356e8a472bca7eeb7a79dc0fe9a27df6d1d19ad82caee2bebc122463a1d42c",
    "84b3b06a9ad46e0cbde25d76822932275bdd7c523095911095a930c68b4dc3f3",
})
SENSITIVE_GEO_DIGESTS = frozenset({
    "bcf8000222e6d32490a0b4b6e5354d0e40257eb3e3856e23898bffc8bb025d2c",
})


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    severity: str
    category: str
    match: str
    context: str


def compile_detectors() -> tuple[tuple[str, re.Pattern[str]], ...]:
    cities = "|".join(
        sorted((re.escape(city) for city in ITALIAN_CITIES), key=len, reverse=True)
    )
    full_names = "|".join(
        re.escape("".join(map(chr, codepoints)))
        for codepoints in PRIVATE_FULL_NAME_CODEPOINTS
    )
    short_name = re.escape("".join(map(chr, PRIVATE_SHORT_NAME_CODEPOINTS)))
    return (
        (
            "STRUCTURED_ID",
            re.compile(r"(?<![A-Z0-9])[A-Z]{2,4}\d{3,6}-\d{2}(?!\d)"),
        ),
        (
            "ITALIAN_HOSPITAL",
            re.compile(
                r"\b(?:ASST|IRCCS|AO|Policlinico|Ospedale|Gaslini|Besta|Meyer)\b"
                r"|Bambino\s+Ges[uù]",
                re.IGNORECASE,
            ),
        ),
        ("ITALIAN_CITY", re.compile(rf"\b(?:{cities})\b", re.IGNORECASE)),
        ("CALENDAR_DATE", re.compile(r"(?<!\d)\d{2}[-/]\d{2}[-/]\d{4}(?!\d)")),
        (
            "EMAIL",
            re.compile(
                r"(?<![\w.+-])[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}"
                r"(?![\w.-])",
                re.IGNORECASE,
            ),
        ),
        (
            "GLUED_NAME_CANDIDATE",
            re.compile(
                rf"\b(?:[A-Za-z0-9_-]+(?:{full_names})[A-Za-z0-9_-]*"
                rf"|(?:{full_names})[A-Za-z0-9_-]+"
                rf"|[A-Za-z0-9_-]+{short_name}[A-Z0-9_-][A-Za-z0-9_-]*"
                rf"|{short_name}[A-Z0-9_-][A-Za-z0-9_-]*)\b"
            ),
        ),
    )


DETECTORS = compile_detectors()


def iter_text_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if relative == SELF_PATH or any(part in SKIP_DIRS for part in relative.parts):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in {
            "LICENSE",
            "NOTICE",
        }:
            files.append(path)
    return sorted(files)


def compact_context(line: str, start: int, end: int, radius: int = 70) -> str:
    left = max(0, start - radius)
    right = min(len(line), end + radius)
    value = line[left:right].strip()
    if left:
        value = "…" + value
    if right < len(line):
        value += "…"
    return value


def severity_for(category: str, value: str) -> str:
    """Keep known synthetic/homonym hits visible without blocking forever."""
    if category == "EMAIL":
        domain = value.rsplit("@", 1)[-1].lower()
        if domain in {"example.com", "example.invalid"}:
            return "INFO"
    if category == "ITALIAN_CITY" and value == "potenza":
        return "INFO"
    return "BLOCK"


def scan(root: Path) -> tuple[list[Finding], list[str]]:
    findings: list[Finding] = []
    errors: list[str] = []
    for path in iter_text_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
            continue
        relative = path.relative_to(root).as_posix()
        for line_number, line in enumerate(text.splitlines(), start=1):
            for token in re.finditer(r"(?<![A-Za-z])[A-Za-z]{3,24}(?![A-Za-z])", line):
                exact_digest = hashlib.sha256(
                    token.group(0).encode()
                ).hexdigest()
                folded_digest = hashlib.sha256(
                    token.group(0).casefold().encode()
                ).hexdigest()
                if (
                    exact_digest not in PRIVATE_IDENTIFIER_DIGESTS
                    and folded_digest not in CASEFOLD_IDENTIFIER_DIGESTS
                ):
                    continue
                findings.append(
                    Finding(
                        path=relative,
                        line=line_number,
                        severity="BLOCK",
                        category="PRIVATE_NAME",
                        match=token.group(0),
                        context=compact_context(
                            line, token.start(), token.end()
                        ),
                    )
                )
            for token in re.finditer(r"\b[A-Za-z]{4,30}\b", line):
                digest = hashlib.sha256(
                    token.group(0).lower().encode()
                ).hexdigest()
                if digest not in SENSITIVE_GEO_DIGESTS:
                    continue
                findings.append(
                    Finding(
                        path=relative,
                        line=line_number,
                        severity="BLOCK",
                        category="ITALIAN_CITY",
                        match=token.group(0),
                        context=compact_context(
                            line, token.start(), token.end()
                        ),
                    )
                )
            for category, pattern in DETECTORS:
                for match in pattern.finditer(line):
                    findings.append(
                        Finding(
                            path=relative,
                            line=line_number,
                            severity=severity_for(category, match.group(0)),
                            category=category,
                            match=match.group(0),
                            context=compact_context(line, match.start(), match.end()),
                        )
                    )
    return findings, errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Independent read-only privacy scan; findings go to stdout."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="repository root to scan (default: current directory)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit a JSON object instead of the line-oriented report",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"ERROR: not a directory: {root}", file=sys.stderr)
        return 3

    findings, errors = scan(root)
    counts: dict[str, int] = {}
    for finding in findings:
        counts[finding.category] = counts.get(finding.category, 0) + 1
    blocking = [finding for finding in findings if finding.severity == "BLOCK"]

    if args.json:
        print(
            json.dumps(
                {
                    "root": str(root),
                    "read_only": True,
                    "finding_count": len(findings),
                    "blocking_count": len(blocking),
                    "informational_count": len(findings) - len(blocking),
                    "counts": dict(sorted(counts.items())),
                    "findings": [asdict(finding) for finding in findings],
                    "errors": errors,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(f"ROOT\t{root}")
        print("MODE\tREAD_ONLY")
        print(f"FINDINGS\t{len(findings)}")
        print(f"BLOCKING\t{len(blocking)}")
        for category, count in sorted(counts.items()):
            print(f"COUNT\t{category}\t{count}")
        for finding in findings:
            print(
                f"{finding.path}:{finding.line}\t{finding.severity}\t"
                f"{finding.category}\t"
                f"{finding.match}\t{finding.context}"
            )
        for error in errors:
            print(f"ERROR\t{error}", file=sys.stderr)

    if errors:
        return 3
    return 2 if blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
