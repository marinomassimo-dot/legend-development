#!/usr/bin/env python3
"""Deduplicate and triage study lists against public LEGEND registries.

Standard-library only. The script matches DOI/PMID/PMCID identifiers first,
then normalized titles. Missing public registries are skipped deliberately:
the output can still classify new inputs, but cannot claim completeness beyond
the files present in the clone.
"""

from __future__ import annotations

import argparse
import datetime as dt
import difflib
import re
import unicodedata
from collections import defaultdict
from pathlib import Path


REGISTRY_FILES = [
    "disease-models/wwox/registries/paper_registry_current.md",
    "disease-models/wwox/registries/literature_tracking_log_current.md",
    "disease-models/wwox/research/full_text_queue_current.md",
    "disease-models/wwox/registries/session_commit_log.md",
]


def normalize_text(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii").lower()
    value = re.sub(r"https?://\S+|doi\.org/", " ", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    stop = {"the", "a", "an", "and", "or", "of", "in", "on", "for", "to", "with"}
    return " ".join(token for token in value.split() if token not in stop)


def extract_identifiers(text: str) -> dict[str, set[str]]:
    doi_re = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", re.I)
    pmid_re = re.compile(r"\bPMID[:\s]*(\d{6,9})\b", re.I)
    pmcid_re = re.compile(r"\bPMC\d{5,}\b", re.I)
    bare_pmid_re = re.compile(r"(?<![\d.])\b\d{7,9}\b(?![\d.])")
    identifiers = {
        "doi": {match.group(0).rstrip(".,;").lower() for match in doi_re.finditer(text)},
        "pmid": {match.group(1) for match in pmid_re.finditer(text)},
        "pmcid": {match.group(0).upper() for match in pmcid_re.finditer(text)},
    }
    if re.search(r"\b(?:pubmed|pmid)\b", text, re.I):
        identifiers["pmid"].update(match.group(0) for match in bare_pmid_re.finditer(text))
    return identifiers


def field(block: str, names: list[str]) -> str:
    for name in names:
        for pattern in (
            rf"^\*\*{re.escape(name)}:\*\*\s*(.+)$",
            rf"^- {re.escape(name)}:\s*(.+)$",
        ):
            match = re.search(pattern, block, re.M)
            if match:
                return match.group(1).strip()
    return ""


def is_corpus_placeholder(record_id: str, block: str, status: str) -> bool:
    if record_id.upper().startswith("CORPUS"):
        return True
    haystack = f"{block} {status}".lower()
    return "corpus placeholder" in haystack or "not_processed" in haystack


# The canonical registry conventions are owned by `framework/scripts/growth_anchors.py`. This
# file is deliberately standard-library-only so the skill runs in a fresh clone, so it cannot
# import them — it restates them, and `test_record_conventions.py` fails if the two ever
# disagree about a real record. Behavioural equivalence, verified, instead of a copy nobody
# checks.
#
# The version this replaced accepted `CORPUS` followed by any word, so the two
# `## CORPUS COVERAGE …` prose section headings were split as records: 407 blocks against 405
# real ones, and `is_corpus_placeholder()` then classified both as corpus placeholders whose
# field lookups read appendix prose. The operational conventions (INBOX / FT / CC) keep their
# looser form on purpose — `## FT-012 — STRATEGIC WATCH (not a standard FT item)` is a real
# record whose heading legitimately carries trailing text.
BLOCK_START = re.compile(
    r"^##\s+("
    r"(?:PAPER\s+\d+)"
    r"|(?:CORPUS(?:-STUB-|\s+P)\d+)"
    r"|(?:LIT-(?!\[)[A-Z0-9-]+)"
    r"|(?:(?:INBOX|FT|CC)[-\s]?\w+.*?)"
    r")$",
    re.M,
)


def split_blocks(text: str) -> list[tuple[str, str]]:
    starts = list(BLOCK_START.finditer(text))
    blocks = []
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        blocks.append((match.group(1).strip(), text[match.start():end]))
    return blocks


def build_index(workspace: Path) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for relative in REGISTRY_FILES:
        path = workspace / relative
        if not path.exists():
            continue
        text = path.read_text(errors="replace")
        for record_id, block in split_blocks(text):
            title = field(block, ["Full title", "Title", "Paper"])
            short = field(block, ["Short title"])
            authors = field(block, ["Authors"])
            year = field(block, ["Year"])
            status = field(block, ["Status", "Current status"])
            # Identity belongs to the record's bibliographic fields, not to every
            # identifier mentioned in its prose.  A full block may cite another
            # PMID as evidence or reading debt; indexing that citation as the
            # record itself turns an unread paper into a false KNOWN_INTEGRATED.
            identifier = " ".join(
                [
                    field(block, ["Identifier"]),
                    field(block, ["Identifier value"]),
                    field(block, ["URL/DOI"]),
                    field(block, ["Paper", "Papers"]),
                    field(block, ["PMID"]),
                    field(block, ["PMCID"]),
                    field(block, ["DOI"]),
                ]
            )
            identifiers = extract_identifiers(identifier)
            best_title = title or short
            if not (best_title or any(identifiers.values())):
                continue
            records.append(
                {
                    "id": record_id,
                    "source_file": relative,
                    "title": best_title,
                    "short_title": short,
                    "norm_title": normalize_text(best_title),
                    "authors": authors,
                    "year": year,
                    "status": status,
                    "placeholder": str(is_corpus_placeholder(record_id, block, status)),
                    "doi": ";".join(sorted(identifiers["doi"])),
                    "pmid": ";".join(sorted(identifiers["pmid"])),
                    "pmcid": ";".join(sorted(identifiers["pmcid"])),
                }
            )
    return records


def build_identifier_index(workspace: Path) -> dict[tuple[str, str], set[str]]:
    """Index record identity fields without treating prose citations as identity."""
    seen: dict[tuple[str, str], set[str]] = defaultdict(set)
    for record in build_index(workspace):
        for kind in ("pmid", "doi", "pmcid"):
            for value in filter(None, record[kind].split(";")):
                seen[(kind, value)].add(record["source_file"])
    return seen


def classify_seen_files(files: set[str]) -> tuple[str, str]:
    if any("paper_registry" in path for path in files):
        return "KNOWN_INTEGRATED", "paper_registry_current.md"
    if any(("inbox" in path or "queue" in path or "session_commit" in path) for path in files):
        source = next(
            path for path in files
            if ("inbox" in path or "queue" in path or "session_commit" in path)
        )
        return "IN_PIPELINE", source
    source = sorted(files)[0]
    return "KNOWN_TRACKED", source


def years(text: str) -> set[str]:
    return set(re.findall(r"\b(?:19|20)\d{2}\b", text))


def _bibliographic_row(block_lines: list[str], line_number: int) -> dict[str, str]:
    title = block_lines[0]
    extra_title = []
    for line in block_lines[1:4]:
        if re.search(r"\b(?:PMID|doi:|J |Proc |Cell |Brain |Nat |Neuro|Front |PLoS|Sci |Mol |Curr |Cells)\b", line):
            break
        if "," in line and re.search(r"\b[A-Z][a-z]+ [A-Z]\b", line):
            break
        extra_title.append(line)
    if extra_title:
        title = " ".join([title] + extra_title)
    block = "\n".join(block_lines)
    identifiers = extract_identifiers(block)
    bits = []
    if identifiers["pmid"]:
        bits.append("PMID " + ",".join(sorted(identifiers["pmid"])))
    if identifiers["doi"]:
        bits.append("DOI " + ",".join(sorted(identifiers["doi"])))
    if identifiers["pmcid"]:
        bits.append("PMCID " + ",".join(sorted(identifiers["pmcid"])))
    found_years = sorted(years(block))
    if found_years:
        bits.append("YEAR " + found_years[-1])
    return {
        "line": title + ((" — " + " · ".join(bits)) if bits else ""),
        "lineno": str(line_number),
        "aggregate": "no",
        "raw": block,
    }


def split_pubmed_records(raw: str) -> list[dict[str, str]]:
    lines = raw.splitlines()
    starts = [index for index, line in enumerate(lines) if re.match(r"^\s*\d+\.\s*$", line)]
    if not starts:
        return split_pubmed_clipboard_blocks(raw)
    rows = []
    for index, start in enumerate(starts):
        end = starts[index + 1] if index + 1 < len(starts) else len(lines)
        block_lines = [line.strip() for line in lines[start + 1:end] if line.strip()]
        if block_lines:
            rows.append(_bibliographic_row(block_lines, start + 1))
    return rows


def split_pubmed_clipboard_blocks(raw: str) -> list[dict[str, str]]:
    chunks = re.split(r"\n\s*\n+", raw.strip())
    expanded: list[str] = []
    for chunk in chunks:
        lines = [line.strip() for line in chunk.splitlines() if line.strip()]
        per_line = [line for line in lines if extract_identifiers(line)["pmid"]]
        if len(lines) >= 2 and len(extract_identifiers(chunk)["pmid"]) >= 2 and len(per_line) == len(lines):
            expanded.extend(lines)
        else:
            expanded.append(chunk)

    rows = []
    search_from = 0
    for chunk in expanded:
        block_lines = [line.strip() for line in chunk.splitlines() if line.strip()]
        if not block_lines:
            continue
        identifiers = extract_identifiers(chunk)
        if len(block_lines) < 2 and not identifiers["pmid"]:
            continue
        if not (identifiers["pmid"] or identifiers["doi"]):
            continue
        offset = raw.find(chunk, search_from)
        line_number = raw[:max(offset, 0)].count("\n") + 1
        rows.append(_bibliographic_row(block_lines, line_number))
        if offset >= 0:
            search_from = offset + len(chunk)
    return rows


def split_input(raw: str) -> list[dict[str, str]]:
    pubmed_rows = split_pubmed_records(raw)
    if pubmed_rows:
        return pubmed_rows
    rows = []
    for line_number, line in enumerate(raw.splitlines(), 1):
        clean = line.strip()
        if not clean:
            continue
        clean = re.sub(r"^\s*[-*•]\s*", "", clean)
        clean = re.sub(r"^\s*\d+[\).]\s+", "", clean)
        parts = re.split(
            r"\s+\|\s+|\s+;\s+(?=(?:PMID|doi|DOI|10\.|[A-Z][A-Za-z]+.*,))",
            clean,
        )
        if len(parts) > 1:
            rows.append({"line": clean, "lineno": str(line_number), "aggregate": "yes"})
            rows.extend(
                {"line": part.strip(), "lineno": str(line_number), "aggregate": "part"}
                for part in parts if part.strip()
            )
        else:
            rows.append({"line": clean, "lineno": str(line_number), "aggregate": "no"})
    return rows


def first_author(text: str) -> str:
    match = re.match(r"([A-Z][A-Za-z'\-]+)", text.lstrip())
    return match.group(1).lower() if match else ""


def title_candidate(line: str) -> str:
    value = re.sub(r"\bPMID[:\s]*\d{6,9}\b", " ", line, flags=re.I)
    value = re.sub(r"\bPMC\d{5,}\b", " ", value, flags=re.I)
    value = re.sub(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", " ", value, flags=re.I)
    value = re.sub(r"\b(?:19|20)\d{2}\b", " ", value)
    return value.strip(" .;-")


def has_scope_signal(text: str) -> bool:
    terms = [
        "wwox", "ww domain-containing oxidoreductase", "woree", "scar12",
        "epileptic encephalopathy", "developmental and epileptic", "seizure",
        "epilepsy", "infantile spasms", "myelin", "hypomyelination",
        "oligodendro", "gsk3", "gaba", "gene therapy", "aav", "splicing",
        "splice", "neurodevelopment", "rare disease", "chaperone", "proteostasis",
    ]
    lowered = text.lower()
    return any(term in lowered for term in terms)


def priority_labels(text: str) -> list[str]:
    lowered = text.lower()
    groups = [
        ("EVOLVING_PRIORITY", ["myc", "wnt", "beta-catenin", "hippo", "neuroinflammation", "microglia", "astrocyte", "cytokine", "zfra", "peptide", "lithium", "gsk3", "tau", "q230p", "misfolding", "chaperone", "stabilizer", "proteostasis", "folding", "stability", "splice acceptor", "cryptic splice", "splice rescue", "sso", "aso"]),
        ("THERAPEUTIC_LEAD", ["therapy", "therapeutic", "treatment", "drug", "compound", "peptide", "lithium", "inhibitor", "activator", "chaperone", "proteostasis", "rescue", "gene therapy", "aav", "aso", "repurposing"]),
        ("VARIANT_STRUCTURE", ["variant", "mutation", "polymorphism", "domain", "structural", "structure", "folding", "stability", "allosteric", "ppxy", "ww2", "sdr"]),
        ("NEURO_BRIDGE", ["epilepsy", "epileptic", "seizure", "neuro", "brain", "cortical", "tau", "alzheimer", "gsk3", "gaba", "myelin", "microglia", "glioblastoma", "neuronal", "oscillation", "excitability"]),
        ("MECHANISM_HIGH", ["interactome", "pathway", "metabolism", "hif1", "p73", "p53", "jnk", "apoptosis", "stress", "inflammation", "emt", "hippo", "wnt", "myc", "mitochond", "glycolysis", "signal", "signaling"]),
        ("PHENOTYPE_CONTEXT", ["woree", "scar12", "case report", "clinical", "phenotypic", "phenotype", "developmental and epileptic encephalopathy"]),
        ("TRANSLATIONAL_BRIDGE", ["cancer", "carcinoma", "tumor", "tumour", "oncolog", "breast", "lung", "ovarian", "hepatocellular", "glioblastoma", "alzheimer", "diabetes", "ards", "copd"]),
    ]

    def contains(term: str) -> bool:
        if re.search(r"[^a-z0-9]", term):
            return term in lowered
        return bool(re.search(rf"\b{re.escape(term)}\b", lowered))

    labels = [label for label, terms in groups if any(contains(term) for term in terms)]
    if "wwox" in lowered or "ww domain-containing oxidoreductase" in lowered:
        labels.insert(0, "WWOX_DIRECT")
    return list(dict.fromkeys(labels)) or ["BACKGROUND_LOW"]


def priority_rank(labels: list[str]) -> int:
    weights = {
        "THERAPEUTIC_LEAD": 6, "EVOLVING_PRIORITY": 6,
        "VARIANT_STRUCTURE": 5, "MECHANISM_HIGH": 5,
        "NEURO_BRIDGE": 4, "TRANSLATIONAL_BRIDGE": 3,
        "WWOX_DIRECT": 3, "PHENOTYPE_CONTEXT": 2, "BACKGROUND_LOW": 1,
    }
    return max(weights.get(label, 1) for label in labels)


def new_or_out_of_scope(line: str, score: int, match: str, reason: str) -> dict[str, str]:
    if has_scope_signal(line):
        return {"class": "NEW", "score": str(score), "match": match, "reason": reason}
    return {
        "class": "OUT_OF_SCOPE_LIKELY",
        "score": str(score),
        "match": match,
        "reason": "no WWOX/WOREE/bridge signal in title/citation",
    }


def resolve_known_class(record: dict[str, str]) -> str:
    if any(token in record["source_file"] for token in ("inbox", "queue", "session_commit")):
        return "IN_PIPELINE"
    if record.get("placeholder") == "True":
        return "CORPUS_CATALOGUED"
    return "KNOWN_INTEGRATED"


def match_row(
    row: dict[str, str],
    records: list[dict[str, str]],
    id_index: dict[tuple[str, str], set[str]] | None = None,
) -> dict[str, str]:
    line = row["line"]
    source_text = f"{line}\n{row.get('raw', '')}"
    if row["aggregate"] == "yes":
        return {"class": "AGGREGATE_LINE", "score": "0", "match": "", "reason": "row contains multiple candidate studies"}

    identifiers = extract_identifiers(source_text)
    if not identifiers["pmid"]:
        bare = re.fullmatch(r"\s*(\d{7,9})\s*", line)
        if bare:
            identifiers["pmid"].add(bare.group(1))

    for record in records:
        for kind in ("doi", "pmid", "pmcid"):
            record_ids = set(filter(None, record[kind].split(";")))
            if identifiers[kind] and record_ids and identifiers[kind] & record_ids:
                return {
                    "class": resolve_known_class(record),
                    "score": "100",
                    "match": record["id"],
                    "reason": f"exact {kind.upper()} match in {record['source_file']}",
                }

    if id_index:
        for kind in ("pmid", "doi", "pmcid"):
            for value in identifiers[kind]:
                files = id_index.get((kind, value))
                if files:
                    klass, source = classify_seen_files(files)
                    return {
                        "class": klass, "score": "100", "match": source,
                        "reason": f"exact {kind.upper()} {value} found in {source}",
                    }

    candidate = title_candidate(line)
    normalized = normalize_text(candidate)
    if len(normalized) < 18:
        if any(identifiers.values()):
            return {"class": "NEW", "score": "0", "match": "", "reason": "identifier not found; fetch metadata at ingest"}
        return {"class": "INSUFFICIENT_METADATA", "score": "0", "match": "", "reason": "no strong identifier and title too short"}

    line_years = years(source_text)
    line_author = first_author(line)
    best: tuple[float, dict[str, str] | None] = (0.0, None)
    for record in records:
        if record["norm_title"]:
            ratio = difflib.SequenceMatcher(None, normalized, record["norm_title"]).ratio()
            if ratio > best[0]:
                best = ratio, record
    ratio, record = best
    if record is None:
        return new_or_out_of_scope(line, 0, "", "no candidate match")

    score = int(round(ratio * 100))
    year_ok = bool(line_years and record["year"] and any(year in record["year"] for year in line_years))
    author_ok = bool(line_author and record["authors"] and line_author in record["authors"].lower())
    pipeline = any(token in record["source_file"] for token in ("inbox", "queue", "session_commit"))
    if pipeline and score >= 88:
        return {"class": "IN_PIPELINE", "score": str(score), "match": record["id"], "reason": f"strong title match in {record['source_file']}"}
    if score >= 96 or (score >= 92 and (year_ok or author_ok)):
        return {"class": resolve_known_class(record), "score": str(score), "match": record["id"], "reason": f"high title match in {record['source_file']}"}
    if score >= 78:
        return {"class": "AMBIGUOUS", "score": str(score), "match": record["id"], "reason": "possible title match; verify metadata"}
    return new_or_out_of_scope(line, score, record["id"], "no match above ambiguity threshold")


def render(rows: list[dict[str, str]], matches: list[dict[str, str]]) -> str:
    counts: dict[str, int] = {}
    for match in matches:
        counts[match["class"]] = counts.get(match["class"], 0) + 1
    lines = [
        f"# STUDY INTAKE TRIAGE — {dt.date.today().isoformat()}",
        "", "## Summary", "", "| Class | Count |", "|---|---:|",
    ]
    lines.extend(f"| {key} | {counts[key]} |" for key in sorted(counts))
    lines += ["", "## Rows", "", "| # | Class | Score | Match | Reason | Input |", "|---:|---|---:|---|---|---|"]
    for index, (row, match) in enumerate(zip(rows, matches), 1):
        lines.append(
            f"| {index} | {match['class']} | {match['score']} | {match['match']} | "
            f"{match['reason'].replace('|', '/')} | {row['line'].replace('|', '/')} |"
        )

    prioritized = []
    for index, (row, match) in enumerate(zip(rows, matches), 1):
        if match["class"] == "NEW":
            labels = priority_labels(f"{row['line']}\n{row.get('raw', '')}")
            prioritized.append((priority_rank(labels), index, labels, row["line"]))
    if prioritized:
        lines += [
            "", "## NEW priority shortlist", "",
            "Priority is inferential value for the disease model, not disease-label proximity.",
            "", "| # | Labels | Input |", "|---:|---|---|",
        ]
        for _rank, index, labels, line in sorted(prioritized, key=lambda item: (-item[0], item[1]))[:40]:
            lines.append(f"| {index} | {', '.join(labels)} | {line.replace('|', '/')} |")

    lines += [
        "", "## Next actions", "",
        "- `KNOWN_INTEGRATED`: do not repeat a deep dive without an explicit upgrade.",
        "- `CORPUS_CATALOGUED`: registered placeholder, never analytically integrated.",
        "- `IN_PIPELINE`: update the existing pipeline item.",
        "- `NEW`: route to ingest.",
        "- `OUT_OF_SCOPE_LIKELY`: retain as low-signal bridge literature; do not discard.",
        "- `AMBIGUOUS`: resolve identifiers before ingest.",
        "- `AGGREGATE_LINE`: split and rerun.",
        "- `INSUFFICIENT_METADATA`: request DOI, PMID, or full title.",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    workspace = Path(args.workspace).resolve()
    raw = Path(args.input).read_text(errors="replace")
    records = build_index(workspace)
    identifier_index = build_identifier_index(workspace)
    rows = split_input(raw)
    matches = [match_row(row, records, identifier_index) for row in rows]
    report = render(rows, matches)
    if args.out:
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(report, encoding="utf-8")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
