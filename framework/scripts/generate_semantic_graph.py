#!/usr/bin/env python3
"""Generate a non-canonical Markdown semantic graph from public registries.

This is a derived-view generator, not an exporter or de-identification tool.
Every input must already be approved for public use. Generated notes never
become canonical state and must be regenerated after registry changes.

The output directory is protected by a marker. ``--replace`` removes an
existing directory only when that marker proves it was created by this script.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path


MARKER = ".legend-semantic-graph"
PATHWAY_LABELS = {
    "P1": "calcium network regulation",
    "P2": "inhibitory network vulnerability",
    "P3": "developmental interaction logic",
    "P4": "myelination and white matter",
    "P5": "metabolism mitochondria redox",
    "P6": "neuroinflammation and glia",
    "P7": "gene-therapy readiness",
}
CONCEPT_RULES = [
    (
        "therapy - gene therapy",
        r"\b(?:gene therapy|AAV|AAV9|delivery|trial[- ]readiness)\b",
    ),
    ("therapy - vigabatrin safety", r"\b(?:vigabatrin|VABAM)\b"),
    ("therapy - ketogenic diet", r"\b(?:ketogenic|ketogenic diet)\b"),
    (
        "therapy - mitochondrial support",
        r"\b(?:NAC|CoQ10|creatine|mitochondrial support|supplement)\b",
    ),
    (
        "biomarker - WWOX functional state",
        r"\b(?:biomarker|functional[- ]state|functional readout|"
        r"WWOX expression|mRNA|protein)\b",
    ),
    (
        "endpoint - EEG network",
        r"\b(?:EEG|qEEG|ECoG|oscillatory|spike[- ]wave|network)\b",
    ),
    (
        "endpoint - MRI myelination",
        r"\b(?:MRI|DTI|myelin|myelination|white matter)\b",
    ),
]
WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")


def slug(text: str, max_length: int = 92) -> str:
    value = re.sub(r"[\[\]#/:*?\"<>|`]+", "", text)
    value = re.sub(r"\s+", " ", value).strip()
    return value[:max_length].rstrip(" .")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def split_blocks(text: str, kind: str) -> dict[str, str]:
    pattern = re.compile(rf"^##\s+{re.escape(kind)}\s+(\d+)\b.*$", re.M)
    matches = list(pattern.finditer(text))
    output: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        output[match.group(1)] = text[match.start():end].strip()
    return output


def field(block: str, name: str) -> str:
    match = re.search(
        rf"^\*\*{re.escape(name)}:\*\*\s*(.+?)\s*$",
        block,
        re.M,
    )
    return match.group(1).strip() if match else ""


def paper_links(text: str) -> list[str]:
    return sorted(
        set(
            re.findall(
                r"\[\[paper_registry_current#PAPER\s+(\d+)\]\]",
                text,
            )
        )
    )


def claim_links_from_paper(block: str) -> list[str]:
    raw = field(block, "Claim links")
    if not raw or raw.lower() == "none":
        return []
    return sorted(
        {f"{int(identifier):03d}" for identifier in re.findall(r"\b(\d{1,3})\b", raw)}
    )


def pathway_matches(text: str) -> list[str]:
    return sorted(set(re.findall(r"\bP[1-7]\b", text)))


def concept_matches(text: str) -> list[str]:
    return [
        name
        for name, pattern in CONCEPT_RULES
        if re.search(pattern, text, re.I)
    ]


def note_link(folder: str, name: str) -> str:
    return f"[[{folder}/{name}|{name}]]"


def canonical_label(basename: str) -> str:
    """A reader-facing name for a canonical file the vault does not contain."""
    return basename.removesuffix("_current").replace("_", " ").strip() or basename


def rewrite_registry_links(
    text: str,
    paper_names: dict[str, str],
    claim_names: dict[str, str],
) -> str:
    """Retarget canonical registry links to nodes inside the derived vault.

    Every wikilink in a registry field points into the canonical repository, and the vault
    is standalone by contract: a link it cannot retarget is rendered as text, never kept.
    Until 2026-09-10 a link to any file other than the two registries — or a registry link
    with no ``#`` fragment — was returned unchanged, so the README's own command failed
    closed on the real registries (``dismissal_ledger_current``, ``full_text_queue_current``,
    ``discovery_ledger_current``, ``meta_metabolism_current`` all occur there) while the
    fixture suite, whose fixtures carried none of those, stayed green.
    """

    def replace(match: re.Match[str]) -> str:
        raw = match.group(1)
        target, separator, alias = raw.partition("|")
        basename, fragment_separator, fragment = target.partition("#")
        if basename == "paper_registry_current":
            identifier = re.search(r"\bPAPER\s+(\d+)\b", fragment)
            names = paper_names
            prefix = "PAPER"
            folder = "papers"
        elif basename == "claim_registry_current":
            identifier = re.search(r"\bCLAIM\s+(\d+)\b", fragment)
            names = claim_names
            prefix = "CLAIM"
            folder = "claims"
        else:
            # A canonical file the vault does not carry: keep the words, drop the link.
            if separator:
                return alias
            label = canonical_label(basename)
            return f"{fragment} ({label})" if fragment_separator else label
        if not fragment_separator:
            return alias if separator else canonical_label(basename)
        if not identifier:
            return alias if separator else fragment
        key = f"{int(identifier.group(1)):03d}"
        if key not in names:
            return alias if separator else f"{prefix} {key}"
        display = alias if separator else f"{prefix} {key}"
        return f"[[{folder}/{names[key]}|{display}]]"

    return WIKILINK.sub(replace, text)


def unresolved_generated_wikilinks(output: Path) -> list[str]:
    """Return wikilinks that do not resolve inside a standalone graph vault."""
    files = sorted(output.rglob("*.md"))
    relative_targets = {
        path.relative_to(output).with_suffix("").as_posix() for path in files
    }
    basename_targets = {path.stem for path in files}
    problems = []
    for path in files:
        for number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), 1
        ):
            for match in WIKILINK.finditer(line):
                target = match.group(1).split("|", 1)[0].split("#", 1)[0]
                if target not in relative_targets and target not in basename_targets:
                    problems.append(
                        f"{path.relative_to(output)}:{number}: {target}"
                    )
    return problems


def paper_note_name(identifier: str, block: str) -> str:
    title = (
        field(block, "Short title")
        or field(block, "Full title")
        or f"PAPER {identifier}"
    )
    return f"PAPER {identifier} - {slug(title, 70)}"


def claim_note_name(identifier: str, block: str) -> str:
    title = field(block, "Title") or f"CLAIM {identifier}"
    return f"CLAIM {identifier} - {slug(title, 70)}"


def write_note(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def render_field_table(names: list[str], block: str) -> str:
    rows = [
        f"| {name} | {field(block, name)} |"
        for name in names
        if field(block, name)
    ]
    if not rows:
        return ""
    return "| Field | Value |\n|---|---|\n" + "\n".join(rows) + "\n"


def prepare_output(output: Path, replace: bool) -> None:
    if output.exists():
        marker = output / MARKER
        if not replace:
            raise ValueError(
                f"Output already exists: {output}; pass --replace to regenerate"
            )
        if not marker.is_file():
            raise ValueError(
                f"Refusing to replace unmarked directory: {output}"
            )
        shutil.rmtree(output)
    output.mkdir(parents=True)
    (output / MARKER).write_text(
        "Generated derived view. Safe replacement requires this marker.\n",
        encoding="utf-8",
    )


def generate(
    paper_registry: Path,
    claim_registry: Path,
    output: Path,
    research_lines: Path | None = None,
    biomarkers: Path | None = None,
    replace: bool = False,
) -> dict[str, int]:
    prepare_output(output, replace=replace)
    paper_blocks = split_blocks(read(paper_registry), "PAPER")
    claim_blocks = split_blocks(read(claim_registry), "CLAIM")
    paper_names = {
        identifier: paper_note_name(identifier, block)
        for identifier, block in paper_blocks.items()
    }
    claim_names = {
        identifier: claim_note_name(identifier, block)
        for identifier, block in claim_blocks.items()
    }
    pathway_names = {
        identifier: f"{identifier} - {label}"
        for identifier, label in PATHWAY_LABELS.items()
    }
    pathway_sources: dict[str, list[str]] = {
        identifier: [] for identifier in PATHWAY_LABELS
    }
    concept_sources: dict[str, list[str]] = {
        name: [] for name, _pattern in CONCEPT_RULES
    }

    for identifier, block in paper_blocks.items():
        pathways = pathway_matches(block)
        concepts = concept_matches(block)
        claims = claim_links_from_paper(block)
        for pathway in pathways:
            if pathway in pathway_sources:
                pathway_sources[pathway].append(paper_names[identifier])
        for concept in concepts:
            concept_sources[concept].append(paper_names[identifier])

        links = []
        if claims:
            links += ["## Claims", ""]
            links += [
                f"- {note_link('claims', claim_names[claim])}"
                if claim in claim_names
                else f"- CLAIM {claim} (not generated)"
                for claim in claims
            ]
        if pathways:
            links += ["", "## Pathways", ""]
            links += [
                f"- {note_link('pathways', pathway_names[pathway])}"
                for pathway in pathways
                if pathway in pathway_names
            ]
        if concepts:
            links += ["", "## Concepts", ""]
            links += [
                f"- {note_link('concepts', concept)}" for concept in concepts
            ]

        table = render_field_table(
            [
                "Short title",
                "Full title",
                "Authors",
                "Year",
                "Source type",
                "Journal/source",
                "Identifier",
                "Status",
                "Evidence depth",
                "Primary pathway",
                "Secondary pathway",
                "Model/species",
                "Genotype/model",
                "Transferability",
                "Disease relevance",
                "Role",
            ],
            block,
        )
        table = rewrite_registry_links(table, paper_names, claim_names)
        summary = rewrite_registry_links(
            (
            field(block, "Note")
            or field(block, "Full title")
            or field(block, "Short title")
            ),
            paper_names,
            claim_names,
        )
        write_note(
            output / "papers" / f"{paper_names[identifier]}.md",
            f"""# {paper_names[identifier]}

> Generated non-canonical view. Source record: PAPER {identifier} in the input paper registry.

{table}
## Summary

{summary}

{chr(10).join(links)}
""",
        )

    for identifier, block in claim_blocks.items():
        papers = paper_links(block)
        pathways = pathway_matches(block)
        concepts = concept_matches(block)
        for pathway in pathways:
            if pathway in pathway_sources:
                pathway_sources[pathway].append(claim_names[identifier])
        for concept in concepts:
            concept_sources[concept].append(claim_names[identifier])

        links = []
        if papers:
            links += ["## Supporting papers", ""]
            links += [
                f"- {note_link('papers', paper_names[paper])}"
                for paper in papers
                if paper in paper_names
            ]
        if pathways:
            links += ["", "## Pathways", ""]
            links += [
                f"- {note_link('pathways', pathway_names[pathway])}"
                for pathway in pathways
                if pathway in pathway_names
            ]
        if concepts:
            links += ["", "## Concepts", ""]
            links += [
                f"- {note_link('concepts', concept)}" for concept in concepts
            ]
        table = render_field_table(
            [
                "Title",
                "Status",
                "Type",
                "Pathway",
                "Genotype/model relevance",
                "Transferability",
                "Disease relevance",
                "Impact on Working Model",
            ],
            block,
        )
        table = rewrite_registry_links(table, paper_names, claim_names)
        summary = rewrite_registry_links(
            field(block, "Summary"), paper_names, claim_names
        )
        write_note(
            output / "claims" / f"{claim_names[identifier]}.md",
            f"""# {claim_names[identifier]}

> Generated non-canonical view. Source record: CLAIM {identifier} in the input claim registry.

{table}
## Summary

{summary}

{chr(10).join(links)}
""",
        )

    for identifier, name in pathway_names.items():
        sources = sorted(set(pathway_sources[identifier]))
        rows = "\n".join(f"- [[{source}]]" for source in sources) or "- No generated nodes"
        write_note(
            output / "pathways" / f"{name}.md",
            f"""# {name}

> Generated pathway node. Non-canonical graph view.

## Connected papers and claims

{rows}
""",
        )

    for concept, sources in concept_sources.items():
        rows = (
            "\n".join(f"- [[{source}]]" for source in sorted(set(sources)))
            or "- No generated nodes"
        )
        write_note(
            output / "concepts" / f"{concept}.md",
            f"""# {concept}

> Generated concept node. Non-canonical graph view.

## Connected papers and claims

{rows}
""",
        )

    biomarker_framework_count = 0
    if biomarkers and biomarkers.is_file():
        biomarker_text = read(biomarkers)
        source_excerpt = biomarker_text.split("---", 1)[0].strip()
        write_note(
            output / "concepts" / "biomarker - candidate framework.md",
            f"""# biomarker - candidate framework

> Generated concept note from the public biomarker-candidate framework.

Canonical source: the biomarker-candidate file supplied with `--biomarkers`.

## Core links

- [[concepts/biomarker - WWOX functional state|biomarker - WWOX functional state]]
- [[pathways/P5 - metabolism mitochondria redox|P5 - metabolism mitochondria redox]]
- [[pathways/P7 - gene-therapy readiness|P7 - gene-therapy readiness]]

## Source excerpt

{source_excerpt}
""",
        )
        biomarker_framework_count = 1

    research_line_count = 0
    research_line_links = []
    if research_lines and research_lines.is_file():
        research_text = read(research_lines)
        items = re.findall(
            r"^##\s+(RL-[A-Z0-9-]+)\s+[—-]\s+(.+)$",
            research_text,
            re.M,
        )
        for identifier, title in items:
            name = f"{identifier} - {slug(title, 70)}"
            block_match = re.search(
                rf"^##\s+{re.escape(identifier)}\s+[—-].*?(?=^##\s+RL-|\Z)",
                research_text,
                re.S | re.M,
            )
            block = block_match.group(0) if block_match else ""
            pathways = pathway_matches(block)
            links = "\n".join(
                f"- {note_link('pathways', pathway_names[pathway])}"
                for pathway in pathways
                if pathway in pathway_names
            )
            write_note(
                output / "research_lines" / f"{name}.md",
                f"""# {name}

> Generated non-canonical research-line node.

{render_field_table(['Status', 'Primary pathway', 'Evidence base', 'Disease relevance', 'Reason active', 'Next action'], block)}
## Pathways

{links or '- No P1-P7 pathway detected'}
""",
            )
            research_line_links.append(
                f"- [[research_lines/{name}|{name}]]"
            )
        research_line_count = len(items)

    counts = {
        "papers": len(paper_blocks),
        "claims": len(claim_blocks),
        "pathways": len(PATHWAY_LABELS),
        "concepts": len(CONCEPT_RULES) + biomarker_framework_count,
        "research_lines": research_line_count,
    }
    count_rows = "\n".join(
        f"| {name.replace('_', ' ').title()} | {value} |"
        for name, value in counts.items()
    )
    pathway_entry_points = "\n".join(
        f"- {note_link('pathways', name)}"
        for name in pathway_names.values()
    )
    concept_entry_points = "\n".join(
        f"- {note_link('concepts', name)}"
        for name, _pattern in CONCEPT_RULES
    )
    if biomarker_framework_count:
        concept_entry_points += (
            "\n- [[concepts/biomarker - candidate framework|"
            "biomarker - candidate framework]]"
        )
    write_note(
        output / "Semantic Graph Index.md",
        f"""# Semantic Graph Index

> Generated non-canonical graph layer. Regenerate from public registries.

## Entry points

### Pathways

{pathway_entry_points}

### Concepts

{concept_entry_points}

## Counts

| Type | Count |
|---|---:|
{count_rows}

## Research lines

{chr(10).join(research_line_links) or '- None supplied'}
""",
    )
    unresolved = unresolved_generated_wikilinks(output)
    if unresolved:
        preview = "\n".join(unresolved[:20])
        remainder = len(unresolved) - 20
        if remainder > 0:
            preview += f"\n... and {remainder} more"
        raise ValueError(
            "Generated semantic graph contains unresolved wikilinks:\n"
            + preview
        )
    return counts


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper-registry", required=True)
    parser.add_argument("--claim-registry", required=True)
    parser.add_argument("--research-lines")
    parser.add_argument("--biomarkers")
    parser.add_argument("--out", required=True)
    parser.add_argument("--replace", action="store_true")
    args = parser.parse_args()

    try:
        counts = generate(
            Path(args.paper_registry),
            Path(args.claim_registry),
            Path(args.out),
            research_lines=Path(args.research_lines) if args.research_lines else None,
            biomarkers=Path(args.biomarkers) if args.biomarkers else None,
            replace=args.replace,
        )
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("Generated semantic graph:", counts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
