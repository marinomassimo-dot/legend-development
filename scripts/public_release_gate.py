#!/usr/bin/env python3
"""Fail-closed public-release gate for the public LEGEND repository.

The gate is deliberately standard-library only. It checks:
privacy and case linkage, common secrets, provenance coverage, local links,
README/repository consistency, and execution from a clean Git archive.

Exit codes:
  0 = PASS
  2 = BLOCK_PUBLICATION
  3 = gate/internal error
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
import re
import subprocess
import sys
import tarfile
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


TEXT_SUFFIXES = {
    ".md", ".txt", ".json", ".csv", ".tsv", ".yaml", ".yml", ".toml",
    ".py", ".sh", ".rst",
}
# `backup/` is the BATCH_COMMIT Phase-3 snapshot root: gitignored, never part of a release
# copy, and a byte-identical duplicate of the canonical files. Scanning it made the mandatory
# pre-commit backup itself raise BROKEN_MARKDOWN_LINK on the copies' relative links.
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", "backup"}
PLACEHOLDER_TOKENS = {
    "your-email@example.com", "example@example.com", "changeme",
    "replace_me", "placeholder",
}
MARKDOWN_LINK_EXAMPLES = {"url", "path", "relative/path.md"}
WIKILINK_EXAMPLES = {
    "file", "file_current", "future_concept_current",
    "nuovo_concetto_da_creare", "DEEP_DIVE",
}
GATE_INTERNAL_FILES = {
    "scripts/public_release_gate.py",
    "scripts/test_public_release_gate.py",
}


@dataclass(order=True)
class Finding:
    severity: str
    code: str
    path: str
    line: int
    message: str


def unpublishable_paths(root: Path) -> frozenset[str]:
    """Paths that are simultaneously untracked *and* gitignored.

    Such a file cannot reach a published clone: it is not in the index, and
    `.gitignore` prevents it from being added by accident. Scanning it produces
    findings about material that is, by construction, private — which is how the
    working-tree scan ended up reporting BLOCKs for the funding dossiers under
    `grants/` and for local scratch directories.

    The condition is deliberately a conjunction, not a directory allowlist. A
    file that is gitignored but has been force-added (`git add -f`) *is* tracked,
    is therefore publishable, and must still be scanned — an allowlist keyed on
    directory names would silently exempt exactly the case that matters. Outside
    a git checkout (an exported release copy) nothing is exempt.
    """
    try:
        completed = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z",
             "--others", "--ignored", "--exclude-standard"],
            check=True, capture_output=True, text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return frozenset()
    return frozenset(entry for entry in completed.stdout.split("\0") if entry)


def iter_files(root: Path) -> Iterable[Path]:
    exempt = unpublishable_paths(root)
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if any(part in SKIP_DIRS for part in relative.parts):
            continue
        if relative.as_posix() in exempt:
            continue
        yield path


def iter_text_files(root: Path) -> Iterable[Path]:
    for path in iter_files(root):
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in {
            "LICENSE", ".gitignore",
        }:
            yield path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def add_matches(
    findings: list[Finding],
    root: Path,
    path: Path,
    text: str,
    code: str,
    pattern: re.Pattern[str],
    message: str,
) -> None:
    for match in pattern.finditer(text):
        findings.append(
            Finding(
                "BLOCK",
                code,
                str(path.relative_to(root)),
                line_number(text, match.start()),
                message,
            )
        )


def semantic_blocks(text: str) -> Iterable[tuple[int, str]]:
    """Yield paragraph/list-record sized blocks with their source offsets."""
    start = 0
    for match in re.finditer(r"\n[ \t]*\n", text):
        block = text[start:match.start()]
        if block.strip():
            yield start, block
        start = match.end()
    block = text[start:]
    if block.strip():
        yield start, block


def parent_origin_is_explicitly_negated(window: str) -> bool:
    """Allow policy statements that explicitly remove/decouple this linkage."""
    subject = (
        r"(?:parent[- ]of[- ]origin|maternal|paternal|mother|father|"
        r"allele materno|allele paterno|materno|paterno|madre|padre)"
    )
    before = (
        r"(?:no|without|removed|redacted|decoupled|de[- ]identified|"
        r"neutralized|excluded)"
    )
    after = (
        r"(?:has been|have been|was|were|is|are)?\s*"
        r"(?:removed|redacted|decoupled|de[- ]identified|neutralized|"
        r"excluded|not (?:retained|linked|reported|included))"
    )
    return bool(
        re.search(rf"(?i)\b{before}\b.{{0,45}}\b{subject}\b", window)
        or re.search(rf"(?i)\b{subject}\b.{{0,45}}\b{after}\b", window)
    )


def person_context_is_explicitly_negated(window: str) -> bool:
    subject = (
        r"(?:person|proband|patient|individual|case|participant|"
        r"clinical regimen|parent[- ]of[- ]origin|institution)"
    )
    negation = (
        r"(?:no|not|without|removed|redacted|decoupled|de[- ]identified|"
        r"never|excluded)"
    )
    return bool(
        re.search(rf"(?i){negation}.{{0,100}}{subject}", window)
        or re.search(rf"(?i){subject}.{{0,100}}{negation}", window)
    )


def scan_privacy_and_secrets(root: Path, findings: list[Finding]) -> None:
    private_identifier_digests = frozenset({
        "56a9baaa78e21fd28508d820a750a3bdab648145046ae5d2e91ef2480fcb240b",
        "1075bbd8b99ffc4f7392d08031e6d50389395a43a7d4cf7c5a992c2df5ade9fe",
        "91a1dafb023759ab2b7668304bb56db4a166c343b17ea4809c0536bf1dd4e4b8",
        "f4100df23c7a789e35087608882def10fccba81b106a8b9af573032ec94d1419",
        "edb1270b1e407a89a46c02743cbe544e788e511d418dd83f8580985c525e2f41",
    })
    # These identifiers are sensitive in every capitalization, including
    # uppercase segments inside compound mode/file names.  Keep only digests
    # in the publishable detector source.
    casefold_identifier_digests = frozenset({
        "b6e1557a1ed3900d7be8e28bb5f137d91812f31e59a90ceddac0276bc532d18e",
        "07356e8a472bca7eeb7a79dc0fe9a27df6d1d19ad82caee2bebc122463a1d42c",
        "84b3b06a9ad46e0cbde25d76822932275bdd7c523095911095a930c68b4dc3f3",
    })
    identifier_token = re.compile(r"(?<![A-Za-z])[A-Za-z]{3,24}(?![A-Za-z])")
    # A cryptographic digest is not prose, and the letters inside one are not a name.
    # A long digest can contain a three-letter sensitive token by chance — the longer the
    # repository carries content-addressed seals, the more often. Matches that fall inside
    # a long hexadecimal run are therefore skipped, so that re-sealing a baseline cannot
    # trip the privacy gate at random. This narrows only the digest interior: an identifier
    # in ordinary text is unaffected.
    hex_run = re.compile(r"(?<![0-9A-Fa-f])[0-9A-Fa-f]{32,}(?![0-9A-Fa-f])")
    email_address = re.compile(
        r"(?i)(?<![A-Z0-9._%+-])"
        r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}"
        r"(?![A-Z0-9_%+-])"
    )
    report_id = re.compile(r"(?i)\b(?:referto|report)\s+(?:id\s*)?(NG[-\d]{5,})\b")
    private_key = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")
    token_patterns = [
        ("OPENAI_KEY", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
        ("GITHUB_TOKEN", re.compile(r"\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}\b")),
        ("AWS_KEY", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
        (
            "PASSWORD_ASSIGNMENT",
            re.compile(r"(?i)\b(?:password|passwd|pwd)\s*[:=]\s*[\"']?[^ \n\"']{8,}"),
        ),
    ]

    variant_a = re.compile(
        r"(?i)(?:\bQ\s*230\s*P\b|\bp\.\s*\(?Gln\s*230\s*Pro\)?\b|"
        r"\bGln\s*230\s*Pro\b)"
    )
    variant_b = re.compile(
        r"(?i)\bc\.\s*1057\s*[-\N{MINUS SIGN}\N{EN DASH}]\s*2\s*A\s*>\s*G\b"
    )
    person_context = re.compile(
        r"(?i)\b(?:the\s+proband|proband|index patient|patient-specific|"
        r"patient-derived|individual patient|"
        r"index case|case subject|affected child|affected individual|"
        r"study participant)\b"
    )
    parent_origin = re.compile(
        r"(?i)\b(?:maternal(?:ly)?|paternal(?:ly)?|mother'?s|father'?s|"
        r"parent[- ]of[- ]origin|inherited from (?:the )?(?:mother|father)|"
        r"allele materno|allele paterno|materno|paterno|madre|padre)\b"
    )
    maternal_origin = re.compile(
        r"(?i)\b(?:maternal(?:ly)?|mother'?s|materno|materna|madre)\b"
    )
    paternal_origin = re.compile(
        r"(?i)\b(?:paternal(?:ly)?|father'?s|paterno|paterna|padre)\b"
    )
    compound_linkage = re.compile(
        r"(?i)\b(?:compound[- ]het(?:erozyg(?:ous|osity)?)?|"
        r"biallelic(?: genotype)?|"
        r"compound[- ]eterozigot[eo]|eterozigosi composta|"
        r"genotipo biallelico|biallelic[oa]|"
        r"in trans|paired alleles?|allelic combination|compound genotype|"
        r"same (?:case|individual|patient|person)|co[- ]?occurr(?:ing|ed|ence)|"
        r"carr(?:y|ies|ied) both|two[- ]variant genotype)\b"
    )
    cross_paragraph_pairing = re.compile(
        r"(?is)\b(?:"
        r"(?:these|the)\s+two\s+(?:variants?|alleles?)|"
        r"together.{0,120}(?:variants?|alleles?)|"
        r"(?:variants?|alleles?).{0,120}together|"
        r"combin(?:e|es|ed|ing).{0,120}(?:variants?|alleles?)"
        r")\b"
    )
    clinical_context = re.compile(
        r"(?i)\b(?:folinate|folinato|lamotrigine|levetiracetam|mg/kg|"
        r"ketogenic diet|AED titration|clinical record|clinical regimen|"
        r"patient cells?|cellule (?:del|di|the) proband)\b"
    )
    geography = re.compile(r"(?i)\b(?:Italy|Italia|Italian)\b")
    reference_genotype = re.compile(
        r"(?i)\b(?:reference genotype|genotipo di riferimento|"
        r"worked[- ]example alleles?)\b"
    )
    public_taint = re.compile(
        r"(?im)^\s*(?:source_scope|provenance)\s*:\s*(?:PRIVATE|MIXED)\b"
    )

    for path in iter_text_files(root):
        text = read_text(path)
        rel = str(path.relative_to(root))
        if rel in GATE_INTERNAL_FILES:
            continue
        digest_spans = [m.span() for m in hex_run.finditer(text)]
        for match in identifier_token.finditer(text):
            if any(start <= match.start() and match.end() <= end
                   for start, end in digest_spans):
                continue
            exact_digest = hashlib.sha256(match.group(0).encode()).hexdigest()
            folded_digest = hashlib.sha256(
                match.group(0).casefold().encode()
            ).hexdigest()
            if (
                exact_digest not in private_identifier_digests
                and folded_digest not in casefold_identifier_digests
            ):
                continue
            findings.append(
                Finding(
                    "BLOCK",
                    "DIRECT_IDENTIFIER",
                    rel,
                    line_number(text, match.start()),
                    "Legacy personal identifier remains in public material.",
                )
            )
        for match in email_address.finditer(text):
            address = match.group(0).lower()
            if (
                address in PLACEHOLDER_TOKENS
                or address.endswith("@example.invalid")
                or address.endswith("@example.test")
            ):
                continue
            findings.append(
                Finding(
                    "BLOCK",
                    "EMAIL_ADDRESS",
                    rel,
                    line_number(text, match.start()),
                    "A non-placeholder email address remains in public material.",
                )
            )
        add_matches(
            findings, root, path, text, "REPORT_IDENTIFIER",
            report_id, "A case/report identifier remains in public material.",
        )
        add_matches(
            findings, root, path, text, "PRIVATE_KEY",
            private_key, "Private key material detected.",
        )
        add_matches(
            findings, root, path, text, "NON_PUBLIC_PROVENANCE",
            public_taint, "Explicit PRIVATE/MIXED provenance is not publishable.",
        )

        lowered = text.lower()
        is_placeholder_file = any(token in lowered for token in PLACEHOLDER_TOKENS)
        for code, pattern in token_patterns:
            for match in pattern.finditer(text):
                matched = match.group(0).lower()
                if is_placeholder_file and any(
                    token in matched for token in PLACEHOLDER_TOKENS
                ):
                    continue
                findings.append(
                    Finding(
                        "BLOCK", code, rel, line_number(text, match.start()),
                        "Potential secret or credential detected.",
                    )
                )

        # A linked two-variant genotype can re-identify even when words such as
        # "proband" have been removed. A generic disease-level genotype rule
        # beside independent worked examples must remain allowed.
        for block_offset, block in semantic_blocks(text):
            relationship = compound_linkage.search(block)
            if (
                relationship
                and variant_a.search(block)
                and variant_b.search(block)
            ):
                findings.append(
                    Finding(
                        "BLOCK",
                        "REIDENTIFYING_VARIANT_COMBINATION",
                        rel,
                        line_number(text, block_offset + relationship.start()),
                        "An exact two-variant combination is linked as one genotype/case.",
                    )
                )
            maternal = maternal_origin.search(block)
            paternal = paternal_origin.search(block)
            if (
                maternal
                and paternal
                and not parent_origin_is_explicitly_negated(block)
            ):
                findings.append(
                    Finding(
                        "BLOCK",
                        "PARENT_OF_ORIGIN_PAIRING",
                        rel,
                        line_number(
                            text,
                            block_offset + min(maternal.start(), paternal.start()),
                        ),
                        "Maternal and paternal disease-model sides are paired in one record.",
                    )
                )
        # Catch a concluding cross-paragraph reassembly only when it uses
        # explicit pairing language such as "these two variants" or "together".
        for pairing in cross_paragraph_pairing.finditer(text):
            start = max(0, pairing.start() - 2200)
            end = min(len(text), pairing.end() + 500)
            window = text[start:end]
            relationship = compound_linkage.search(window)
            if (
                relationship
                and variant_a.search(window)
                and variant_b.search(window)
            ):
                findings.append(
                    Finding(
                        "BLOCK",
                        "REIDENTIFYING_VARIANT_COMBINATION",
                        rel,
                        line_number(text, pairing.start()),
                        "Separated worked examples are explicitly reassembled as one genotype.",
                    )
                )

        # Parent-of-origin plus an exact variant is itself identifying linkage;
        # it does not require an explicit person noun. Explicit statements that
        # the relationship was removed or decoupled are allowed.
        for marker in parent_origin.finditer(text):
            start = max(0, marker.start() - 350)
            end = min(len(text), marker.end() + 350)
            window = text[start:end]
            if (
                (variant_a.search(window) or variant_b.search(window))
                and not parent_origin_is_explicitly_negated(window)
            ):
                findings.append(
                    Finding(
                        "BLOCK",
                        "PARENT_OF_ORIGIN_VARIANT_LINKAGE",
                        rel,
                        line_number(text, marker.start()),
                        "Parent-of-origin is linked to an exact variant.",
                    )
                )
            if (
                reference_genotype.search(window)
                and not parent_origin_is_explicitly_negated(window)
            ):
                findings.append(
                    Finding(
                        "BLOCK",
                        "PARENT_OF_ORIGIN_REFERENCE_GENOTYPE",
                        rel,
                        line_number(text, marker.start()),
                        "Parent-of-origin is linked to the persistent reference genotype.",
                    )
                )

        # Semantic/case-linkage checks use local windows, not isolated keywords.
        for marker in person_context.finditer(text):
            local_context = text[
                max(0, marker.start() - 120):min(len(text), marker.end() + 120)
            ]
            if person_context_is_explicitly_negated(local_context):
                continue
            start = max(0, marker.start() - 700)
            end = min(len(text), marker.end() + 700)
            window = text[start:end]
            if variant_a.search(window) and variant_b.search(window):
                findings.append(
                    Finding(
                        "BLOCK", "REIDENTIFYING_VARIANT_COMBINATION", rel,
                        line_number(text, marker.start()),
                        "A person/proband is linked to the exact two-variant combination.",
                    )
                )
            if parent_origin.search(window) and (
                variant_a.search(window) or variant_b.search(window)
            ):
                findings.append(
                    Finding(
                        "BLOCK", "PARENT_OF_ORIGIN_LINKAGE", rel,
                        line_number(text, marker.start()),
                        "Parent-of-origin is linked to a person and a specific variant.",
                    )
                )
            if clinical_context.search(window):
                findings.append(
                    Finding(
                        "BLOCK", "CLINICAL_CASE_LINKAGE", rel,
                        line_number(text, marker.start()),
                        "Clinical regimen/sample detail is linked to a person/proband.",
                    )
                )
            if geography.search(window):
                findings.append(
                    Finding(
                        "BLOCK", "GEOGRAPHIC_CASE_LINKAGE", rel,
                        line_number(text, marker.start()),
                        "Geography is linked to a person/proband context.",
                    )
                )


def scan_links(root: Path, findings: list[Finding]) -> None:
    markdown_link = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    wikilink = re.compile(r"\[\[([^\]#|]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
    by_name: dict[str, list[Path]] = {}
    for file_path in iter_files(root):
        by_name.setdefault(file_path.name, []).append(file_path)
        by_name.setdefault(file_path.stem, []).append(file_path)
    for directory in root.rglob("*"):
        if directory.is_dir() and not any(
            part in SKIP_DIRS for part in directory.relative_to(root).parts
        ):
            by_name.setdefault(directory.name, []).append(directory)

    for path in iter_text_files(root):
        if path.suffix.lower() != ".md":
            continue
        text = read_text(path)
        rel = str(path.relative_to(root))
        for match in markdown_link.finditer(text):
            target = match.group(1).strip()
            if (
                not target
                or target.startswith(("#", "http://", "https://", "mailto:"))
                or "://" in target
            ):
                continue
            clean = target.split("#", 1)[0].split("?", 1)[0]
            if clean in MARKDOWN_LINK_EXAMPLES:
                continue
            resolved = (path.parent / clean).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                findings.append(
                    Finding(
                        "BLOCK", "LINK_ESCAPES_REPO", rel,
                        line_number(text, match.start()),
                        f"Relative link escapes repository: {target}",
                    )
                )
                continue
            if not resolved.exists():
                findings.append(
                    Finding(
                        "BLOCK", "BROKEN_MARKDOWN_LINK", rel,
                        line_number(text, match.start()),
                        f"Missing relative-link target: {target}",
                    )
                )

        for match in wikilink.finditer(text):
            target = match.group(1).strip()
            if target in WIKILINK_EXAMPLES:
                continue
            name = Path(target).name
            candidates = {name, f"{name}.md"}
            if not any(candidate in by_name for candidate in candidates):
                findings.append(
                    Finding(
                        "BLOCK", "BROKEN_WIKILINK", rel,
                        line_number(text, match.start()),
                        f"Missing wikilink target: {target}",
                    )
                )


def declared_data_patterns(data_sources_text: str) -> list[str]:
    patterns: list[str] = []
    for match in re.finditer(r"`((?:analysis/data|eval/data)/[^`]+)`", data_sources_text):
        patterns.append(match.group(1))
    return patterns


def provenance_scopes(relative: str) -> list[str]:
    """Return DATA_SOURCES-style paths for a repository-relative asset."""
    path = Path(relative)
    candidates = [relative]
    parts = path.parts
    if len(parts) >= 4 and parts[0] == "disease-models":
        candidates.append(Path(*parts[2:]).as_posix())
    if len(parts) >= 3 and parts[0] == "framework":
        candidates.append(Path(*parts[1:]).as_posix())
    return candidates


def scan_provenance(root: Path, findings: list[Finding]) -> None:
    required = [
        root / "DATA_SOURCES.md",
        root / "THIRD_PARTY_NOTICES.md",
        root / "_external_repos" / "MANIFEST.md",
    ]
    for path in required:
        if not path.exists():
            findings.append(
                Finding(
                    "BLOCK", "MISSING_PROVENANCE_FILE",
                    str(path.relative_to(root)), 1,
                    "Required provenance/licensing manifest is missing.",
                )
            )

    data_sources = root / "DATA_SOURCES.md"
    if not data_sources.exists():
        return
    text = read_text(data_sources)
    for marker in ("TBD", "VERIFY BEFORE RELEASE", "UNKNOWN LICENSE"):
        for match in re.finditer(re.escape(marker), text, flags=re.IGNORECASE):
            findings.append(
                Finding(
                    "BLOCK", "UNRESOLVED_PROVENANCE", "DATA_SOURCES.md",
                    line_number(text, match.start()),
                    f"Unresolved provenance marker: {marker}",
                )
            )

    patterns = declared_data_patterns(text)
    for path in iter_files(root):
        rel = str(path.relative_to(root))
        scopes = provenance_scopes(rel)
        if not any(
            scope.startswith(("analysis/data/", "eval/data/"))
            for scope in scopes
        ):
            continue
        if not any(
            fnmatch.fnmatch(scope, pattern)
            for scope in scopes
            for pattern in patterns
        ):
            findings.append(
                Finding(
                    "BLOCK", "UNDECLARED_DATA_ASSET", rel, 1,
                    "Data asset is not covered by DATA_SOURCES.md.",
                )
            )


def scan_readme_consistency(root: Path, findings: list[Finding]) -> None:
    readme = root / "README.md"
    if not readme.exists():
        findings.append(
            Finding("BLOCK", "MISSING_README", "README.md", 1, "README.md is missing.")
        )
        return
    text = read_text(readme)
    lower = text.lower()
    python_files = list(root.rglob("*.py"))

    if "full machine" in lower and len(python_files) <= 1:
        findings.append(
            Finding(
                "BLOCK", "README_CAPABILITY_OVERCLAIM", "README.md",
                line_number(lower, lower.index("full machine")),
                "README claims a full machine but ships no operational implementation.",
            )
        )
    if "sponsored by" in lower and not (root / "SPONSORSHIP.md").exists():
        findings.append(
            Finding(
                "BLOCK", "UNVERIFIED_SPONSORSHIP", "README.md",
                line_number(lower, lower.index("sponsored by")),
                "Sponsorship claim requires a committed SPONSORSHIP.md attestation.",
            )
        )

    corpus = "\n".join(
        read_text(path)
        for path in iter_text_files(root)
        if str(path.relative_to(root)) not in GATE_INTERNAL_FILES
    )
    no_patient_claim = re.search(
        r"(?i)(?:no (?:real )?patient (?:is )?referenced|"
        r"contains no patient(?:'s)? clinical record)",
        corpus,
    )
    patient_markers = re.search(
        r"(?i)(?:NG[-\d]{5,}|allele materno|allele paterno|"
        r"maternal\s+c\.1057-2A>G|paternal\s+(?:Q230P|p\.Gln230Pro)|"
        r"the proband.{0,200}(?:folinato|folinate|mg/kg|patient cells))",
        corpus,
        flags=re.DOTALL,
    )
    if no_patient_claim and patient_markers:
        findings.append(
            Finding(
                "BLOCK", "README_PRIVACY_CONTRADICTION", "README.md", 1,
                "Repository claims no patient is referenced, but case-linkage markers remain.",
            )
        )

    required_ci = root / ".github" / "workflows" / "public-release-gate.yml"
    if not required_ci.exists():
        findings.append(
            Finding(
                "BLOCK", "MISSING_RELEASE_CI",
                ".github/workflows/public-release-gate.yml", 1,
                "Release-gate CI workflow is missing.",
            )
        )


def run_clean_clone(root: Path, findings: list[Finding], report_json: str | None) -> None:
    git_dir = root / ".git"
    if not git_dir.exists():
        findings.append(
            Finding(
                "BLOCK", "NOT_A_GIT_CLONE", ".", 1,
                "Clean-clone execution requires a Git repository.",
            )
        )
        return
    status = subprocess.run(
        ["git", "-C", str(root), "status", "--porcelain"],
        check=False, capture_output=True, text=True,
    )
    if status.returncode != 0:
        findings.append(
            Finding("BLOCK", "GIT_STATUS_FAILED", ".", 1, status.stderr.strip())
        )
        return
    if status.stdout.strip():
        findings.append(
            Finding(
                "BLOCK", "DIRTY_RELEASE_TREE", ".", 1,
                "Final release review must run from a clean committed tree.",
            )
        )
        return

    with tempfile.TemporaryDirectory(prefix="legend-public-gate-") as temp_dir:
        archive = Path(temp_dir) / "repo.tar"
        clone = Path(temp_dir) / "clone"
        clone.mkdir()
        with archive.open("wb") as handle:
            proc = subprocess.run(
                ["git", "-C", str(root), "archive", "HEAD"],
                check=False, stdout=handle, stderr=subprocess.PIPE,
            )
        if proc.returncode != 0:
            findings.append(
                Finding(
                    "BLOCK", "GIT_ARCHIVE_FAILED", ".", 1,
                    proc.stderr.decode("utf-8", errors="replace").strip(),
                )
            )
            return
        with tarfile.open(archive) as tar:
            # git archive contains repository-relative members only. Validate
            # again for compatibility with Python versions predating filter=.
            for member in tar.getmembers():
                destination = (clone / member.name).resolve()
                try:
                    destination.relative_to(clone.resolve())
                except ValueError as exc:
                    raise RuntimeError(
                        f"Unsafe path in git archive: {member.name}"
                    ) from exc
            tar.extractall(clone)
        gate = clone / "scripts" / "public_release_gate.py"
        command = [
            sys.executable, str(gate), "--root", str(clone),
            "--mode", "clone", "--skip-clean-clone",
        ]
        if report_json:
            command.extend(["--report-json", str(Path(temp_dir) / "clone-report.json")])
        proc = subprocess.run(command, check=False, capture_output=True, text=True)
        if proc.returncode != 0:
            findings.append(
                Finding(
                    "BLOCK", "CLEAN_CLONE_GATE_FAILED", ".", 1,
                    "Gate failed in clean archive:\n" + proc.stdout[-3000:],
                )
            )


def deduplicate(findings: list[Finding]) -> list[Finding]:
    unique: dict[tuple[str, str, str, int, str], Finding] = {}
    for finding in findings:
        key = (
            finding.severity, finding.code, finding.path,
            finding.line, finding.message,
        )
        unique[key] = finding
    return sorted(unique.values(), key=lambda f: (f.path, f.line, f.code))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument(
        "--mode", choices=("staging", "release", "clone"), default="staging"
    )
    parser.add_argument("--report-json", help="Write machine-readable report")
    parser.add_argument("--skip-clean-clone", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"GATE_ERROR: root is not a directory: {root}", file=sys.stderr)
        return 3

    findings: list[Finding] = []
    try:
        scan_privacy_and_secrets(root, findings)
        scan_links(root, findings)
        scan_provenance(root, findings)
        scan_readme_consistency(root, findings)
        if args.mode in {"release", "clone"} and not args.skip_clean_clone:
            run_clean_clone(root, findings, args.report_json)
    except Exception as exc:  # fail closed
        print(f"GATE_ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 3

    findings = deduplicate(findings)
    blocks = [finding for finding in findings if finding.severity == "BLOCK"]
    result = {
        "verdict": "BLOCK_PUBLICATION" if blocks else "PASS",
        "mode": args.mode,
        "root": str(root),
        "block_count": len(blocks),
        "findings": [asdict(finding) for finding in findings],
    }
    if args.report_json:
        report_path = Path(args.report_json)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(
            json.dumps(result, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    print(f"VERDICT: {result['verdict']}")
    print(f"BLOCKS: {len(blocks)}")
    for finding in findings:
        print(
            f"[{finding.severity}] {finding.code} "
            f"{finding.path}:{finding.line} — {finding.message}"
        )
    return 2 if blocks else 0


if __name__ == "__main__":
    raise SystemExit(main())
