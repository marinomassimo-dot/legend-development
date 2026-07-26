#!/usr/bin/env python3
"""Run the LEGEND batch inferential sweep.

Parse a study list or intake report, optionally retrieve PubMed metadata and
open PMC text, rank every record for evidence-integrity, mechanistic,
therapeutic, safety, endpoint, and repurposing value, then apply the public
disease-level proband matrix. Standard-library only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import textwrap
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


DEFAULT_PROBAND_MATRIX = (
    Path(__file__).resolve().parents[2]
    / "legend-proband-priority-matrix"
    / "references"
    / "proband_priority_matrix.json"
)

LABELS: dict[str, list[str]] = {
    "INTEGRITY_SIGNAL": ["retraction", "retracted", "expression of concern", "withdrawn", "editorial concern"],
    "WWOX_DIRECT": ["wwox", "ww domain-containing oxidoreductase", "ww domain containing oxidoreductase", "woree", "scar12"],
    "VARIANT_OF_INTEREST": ["q230p", "gln230pro", "splice acceptor", "exon 9", "sdr domain"],
    "NEURO_NETWORK": ["epilep", "seizure", "brain", "neuro", "sleep", "circadian", "nmdar", "grin", "gaba", "tau", "tdp-43", "myelin"],
    "INFLAMMATION": ["inflamm", "microglia", "astro", "macrophage", "cytokine", "jak", "stat", "pd-l1", "nf-k", "il-6", "il-1", "tnf"],
    "METABOLIC": ["hif", "hif1", "p73", "glycolysis", "mitochond", "redox", "ros", "oleic", "scd5", "lipid", "metabolism"],
    "PROTEOSTASIS": ["folding", "chaperone", "proteostasis", "lysosom", "bcl-xl", "mcl-1", "ubiquitin", "degradation", "apoptosis"],
    "THERAPY": ["therapy", "therapeutic", "drug", "treatment", "repurpos", "inhibitor", "activator", "gene delivery", "aav", "aso", "peptide", "zfra", "cisplatin", "immunotherapy"],
    "GENETIC_METHOD": ["gwas", "multi-omics", "mendelian", "variant", "genotype", "haplotype", "polymorphism", "functional validation"],
    "PEDIATRIC_DEE": ["pediatric", "infant", "child", "developmental and epileptic", "infantile spasms", "dee"],
    "SAFETY": ["side effect", "toxicity", "corrigendum", "resistance", "immune evasion", "pd-l1", "jak2/stat3", "bcl-xl", "mcl-1"],
}

WEIGHTS = {
    "INTEGRITY_SIGNAL": 12,
    "WWOX_DIRECT": 8,
    "VARIANT_OF_INTEREST": 8,
    "THERAPY": 4,
    "NEURO_NETWORK": 4,
    "PEDIATRIC_DEE": 4,
    "INFLAMMATION": 3,
    "METABOLIC": 3,
    "PROTEOSTASIS": 3,
    "SAFETY": 3,
    "GENETIC_METHOD": 1,
}


def triage_row_identifiers(text: str) -> dict[str, str]:
    """Map bare PMIDs in a triage report's `## Rows` table to their intake class.

    `study_dedup_triage.py` echoes the operator's input verbatim in the last column, so a
    plain PMID list produces rows whose identifier carries no `PMID` prefix. Without this,
    the prefix-only scan below finds nothing and the whole sweep silently yields zero
    records on the most natural input a batch can have. Scoped to the Rows table on
    purpose: a bare 6-9 digit scan over free text would also swallow years and counts.
    """
    rows = text.partition("## Rows")[2]
    rows = rows.partition("\n## ")[0]
    classes: dict[str, str] = {}
    for line in rows.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2 or not cells[0].isdigit():
            continue
        match = re.search(r"\b(\d{6,9})\b", cells[-1])
        if match:
            classes[match.group(1)] = cells[1]
    return classes


def extract_pmids(text: str) -> list[str]:
    pmids = set(re.findall(r"\bPMID[:\s]*(\d{6,9})\b", text, re.I))
    pmids.update(re.findall(r"\bPMID\s+(\d{6,9})\b", text, re.I))
    pmids.update(triage_row_identifiers(text))
    return sorted(pmids, key=int, reverse=True)


def parse_triage_classes(text: str) -> dict[str, str]:
    classes: dict[str, str] = dict(triage_row_identifiers(text))
    for line in text.splitlines():
        match = re.match(r"\|\s*\d+\s*\|\s*([^|]+?)\s*\|.*?PMID\s+(\d{6,9})", line)
        if match:
            classes[match.group(2)] = match.group(1).strip()
    return classes


def parse_expected_count(text: str) -> int | None:
    """Read the intake summary count used by the completeness gate."""
    summary = text.partition("## Summary")[2].partition("## Rows")[0]
    counts = [
        int(value)
        for value in re.findall(r"^\|\s*[A-Z_]+\s*\|\s*(\d+)\s*\|$", summary, re.M)
    ]
    return sum(counts) if counts else None


def fetch_pubmed(pmids: list[str]) -> list[dict[str, object]]:
    if not pmids:
        return []
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "id": ",".join(pmids), "retmode": "xml"}
    )
    root = ET.fromstring(urllib.request.urlopen(url, timeout=40).read())
    records: list[dict[str, object]] = []
    for publication in root.findall("./PubmedArticle"):
        citation = publication.find("./MedlineCitation")
        article = citation.find("./Article") if citation is not None else None
        pmid = citation.findtext("./PMID") if citation is not None else ""
        title = ""
        title_node = article.find("./ArticleTitle") if article is not None else None
        if title_node is not None:
            title = "".join(title_node.itertext())
        abstract_parts = []
        if article is not None:
            for node in article.findall("./Abstract/AbstractText"):
                value = " ".join("".join(node.itertext()).split())
                if value:
                    label = node.attrib.get("Label")
                    abstract_parts.append(f"{label}: {value}" if label else value)
        doi = ""
        pmcid = ""
        identifiers = publication.find("./PubmedData/ArticleIdList")
        if identifiers is not None:
            for identifier in identifiers.findall("./ArticleId"):
                if identifier.attrib.get("IdType") == "doi":
                    doi = identifier.text or ""
                elif identifier.attrib.get("IdType") == "pmc":
                    pmcid = identifier.text or ""
        records.append(
            {
                "pmid": pmid,
                "title": title,
                "abstract": "\n".join(abstract_parts),
                "doi": doi,
                "pmcid": pmcid,
                "journal": article.findtext("./Journal/Title") if article is not None else "",
                "year": article.findtext("./Journal/JournalIssue/PubDate/Year") if article is not None else "",
            }
        )
    return records


def fallback_records(text: str, classes: dict[str, str]) -> list[dict[str, object]]:
    del classes
    records = []
    for pmid in extract_pmids(text):
        title = ""
        for line in text.splitlines():
            if f"PMID {pmid}" in line or f"PMID: {pmid}" in line:
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                title = cells[-1] if cells else ""
                title = re.sub(r"\s+—\s+PMID.*$", "", title)
                break
        records.append(
            {"pmid": pmid, "title": title, "abstract": "", "doi": "", "pmcid": "", "journal": "", "year": ""}
        )
    return records


def labels_for(text: str) -> list[str]:
    lowered = text.lower()
    return [
        label for label, terms in LABELS.items()
        if any(term in lowered for term in terms)
    ]


def classify(labels: list[str], intake_class: str, text: str) -> tuple[str, int, str]:
    score = sum(WEIGHTS.get(label, 1) for label in labels)
    lowered = text.lower()
    reasons = []
    if intake_class in {"NEW", "CORPUS_CATALOGUED"} and "WWOX_DIRECT" in labels:
        score += 4
        reasons.append("new/tracked WWOX-direct")
    if "VARIANT_OF_INTEREST" in labels:
        reasons.append("variant/domain signal")
    if "SAFETY" in labels:
        reasons.append("safety/evidence-correction signal")
    if "THERAPY" in labels:
        reasons.append("therapy/repurposing language")

    reason = "; ".join(reasons)
    if "INTEGRITY_SIGNAL" in labels or "corrigendum" in lowered:
        return "SAFETY_SIGNAL", score, f"{reason}; publication-integrity signal".strip("; ")
    if "SAFETY" in labels and "WWOX_DIRECT" in labels:
        return "SAFETY_SIGNAL", score, reason or "safety keyword"
    if score >= 18 and "WWOX_DIRECT" in labels and intake_class in {"NEW", "CORPUS_CATALOGUED", "IN_PIPELINE"}:
        return "CANONICAL_CANDIDATE", score, reason or "high WWOX direct score"
    if "THERAPY" in labels and ("WWOX_DIRECT" in labels or "VARIANT_OF_INTEREST" in labels):
        return "REPURPOSING_SEED", score, reason or "therapy signal"
    if "NEURO_NETWORK" in labels or "PEDIATRIC_DEE" in labels:
        return "ENDPOINT_SEED", score, reason or "network/DEE endpoint signal"
    if score >= 9 and any(
        label in labels
        for label in ("WWOX_DIRECT", "INFLAMMATION", "METABOLIC", "PROTEOSTASIS")
    ):
        return "DISCOVERY_ONLY", score, reason or "mechanistic bridge"
    return "READ_QUEUE_TAIL", score, "no strong keyword signal — READ LATER, not discarded"


def fetch_pmc_text(pmcid: str, output_dir: Path) -> tuple[str, int]:
    clean = pmcid.upper().replace("PMC", "")
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?" + urllib.parse.urlencode(
        {"db": "pmc", "id": clean, "retmode": "xml"}
    )
    data = urllib.request.urlopen(url, timeout=40).read()
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / f"PMC{clean}.xml").write_bytes(data)
    root = ET.fromstring(data)
    title_node = root.find(".//article-title")
    title = " ".join("".join(title_node.itertext()).split()) if title_node is not None else ""
    body = " ".join(
        " ".join("".join(node.itertext()).split())
        for node in root.findall(".//body//p")
    )
    (output_dir / f"PMC{clean}.txt").write_text(
        (title + "\n\n" + body[:50000]).strip() + "\n",
        encoding="utf-8",
    )
    return title, len(body)


def score_records(
    records: list[dict[str, object]], classes: dict[str, str]
) -> list[dict[str, object]]:
    ranked = []
    for record in records:
        text = f"{record.get('title', '')} {record.get('abstract', '')}"
        labels = labels_for(text)
        intake = classes.get(str(record.get("pmid", "")), "UNKNOWN")
        klass, score, reason = classify(labels, intake, text)
        enriched = dict(record)
        enriched.update(
            {
                "sweep_class": klass,
                "sweep_score": score,
                "sweep_labels": labels,
                "intake_class": intake,
                "sweep_reason": reason,
            }
        )
        ranked.append(enriched)
    ranked.sort(key=lambda item: (-int(item["sweep_score"]), str(item.get("pmid", ""))))
    return ranked


def matrix_term_hit(text: str, terms: list[str]) -> bool:
    lowered = text.lower()
    for term in terms:
        needle = term.lower()
        if len(needle) <= 4 and needle.replace("-", "").isalnum():
            if re.search(rf"(?<![a-z0-9]){re.escape(needle)}(?![a-z0-9])", lowered):
                return True
        elif needle in lowered:
            return True
    return False


def matrix_condition_hit(record: dict[str, object], condition: str) -> bool:
    key, separator, value = condition.partition(":")
    return bool(separator and key and value and str(record.get(key, "")) == value)


def apply_proband_matrix(
    records: list[dict[str, object]], matrix_path: Path
) -> list[dict[str, object]]:
    if not matrix_path.exists():
        return records
    matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
    enriched_records = []
    for record in records:
        text = " ".join(
            str(record.get(key, ""))
            for key in ("title", "abstract", "sweep_reason", "journal")
        )
        score = 0
        axes_hit = []
        for axis in matrix.get("axes", []):
            if matrix_term_hit(text, axis.get("terms", [])):
                weight = int(axis.get("weight", 0))
                score += weight
                axes_hit.append({"id": axis["id"], "label": axis.get("label", axis["id"]), "weight": weight})

        axis_ids = {str(axis["id"]) for axis in axes_hit}
        penalties_hit = []
        for penalty in matrix.get("penalties", []):
            unless = set(penalty.get("unless_any_axis", []))
            if unless and axis_ids.intersection(unless):
                continue
            if matrix_term_hit(text, penalty.get("terms", [])):
                weight = int(penalty.get("weight", 0))
                score += weight
                penalties_hit.append({"id": penalty["id"], "weight": weight})

        boosts_hit = []
        for boost in matrix.get("boosts", []):
            if matrix_condition_hit(record, str(boost.get("condition", ""))):
                weight = int(boost.get("weight", 0))
                score += weight
                boosts_hit.append({"condition": boost["condition"], "weight": weight})

        tier = "P4_BACKGROUND"
        for candidate in matrix.get("tiers", []):
            if score >= int(candidate.get("min_score", -999)):
                tier = str(candidate["name"])
                break

        enriched = dict(record)
        enriched["proband_score"] = score
        enriched["proband_priority_tier"] = tier
        enriched["proband_axes"] = axes_hit
        enriched["proband_penalties"] = penalties_hit
        enriched["proband_boosts"] = boosts_hit
        enriched["proband_rationale"] = (
            ", ".join(str(axis["label"]) for axis in axes_hit[:5])
            or "No strong disease-model axis hit"
        )
        enriched_records.append(enriched)

    enriched_records.sort(
        key=lambda item: (
            -int(item.get("proband_score", 0)),
            -int(item.get("sweep_score", 0)),
            str(item.get("pmid", "")),
        )
    )
    return enriched_records


def render(
    ranked: list[dict[str, object]],
    pmc_results: dict[str, str],
    expected_count: int | None = None,
) -> str:
    counts: dict[str, int] = {}
    proband_counts: dict[str, int] = {}
    for record in ranked:
        klass = str(record["sweep_class"])
        tier = str(record.get("proband_priority_tier", "NA"))
        counts[klass] = counts.get(klass, 0) + 1
        proband_counts[tier] = proband_counts.get(tier, 0) + 1

    complete = expected_count is None or expected_count == len(ranked)
    lines = [
        f"# Batch Inferential Sweep — {dt.date.today().isoformat()}",
        "", "## Completeness Gate", "",
        f"- Expected records from triage summary: {expected_count if expected_count is not None else 'UNKNOWN'}",
        f"- Records emitted by sweep: {len(ranked)}",
        f"- Status: {'PASS' if complete else 'BLOCKED_INCOMPLETE — recover missing sources before trusting ranking'}",
        "", "## Sweep Summary", "", "| Class | Count |", "|---|---:|",
    ]
    lines.extend(f"| {key} | {counts[key]} |" for key in sorted(counts))
    if any(key != "NA" for key in proband_counts):
        lines += ["", "## Proband Priority Summary", "", "| Tier | Count |", "|---|---:|"]
        for tier in ("P0_FAST_TRACK", "P1_HIGH", "P2_MEDIUM", "P3_LOW", "P4_BACKGROUND", "NA"):
            if tier in proband_counts:
                lines.append(f"| {tier} | {proband_counts[tier]} |")

    lines += [
        "", "## Ranked Records", "",
        "| Rank | Proband tier | Proband score | Axes | Sweep class | Score | PMID | Intake | PMCID | Labels | Title | Reason | Abstract signal |",
        "|---:|---|---:|---|---|---:|---|---|---|---|---|---|---|",
    ]
    for index, record in enumerate(ranked, 1):
        abstract = textwrap.shorten(
            " ".join(str(record.get("abstract", "")).split()),
            width=280,
            placeholder="...",
        )
        axes = ", ".join(
            str(axis.get("label", axis.get("id", "")))
            for axis in record.get("proband_axes", [])[:4]
        )
        lines.append(
            f"| {index} | {record.get('proband_priority_tier', 'NA')} | "
            f"{record.get('proband_score', '')} | {axes or 'NA'} | "
            f"{record['sweep_class']} | {record['sweep_score']} | "
            f"{record.get('pmid', '')} | {record['intake_class']} | "
            f"{record.get('pmcid', '')} | {', '.join(record['sweep_labels']) or 'LOW_SIGNAL'} | "
            f"{str(record.get('title', '')).replace('|', '/')} | "
            f"{str(record['sweep_reason']).replace('|', '/')} | {abstract.replace('|', '/')} |"
        )

    if pmc_results:
        lines += ["", "## PMC Full Text Retrieved", "", "| PMCID | Result |", "|---|---|"]
        lines.extend(
            f"| {pmcid} | {result.replace('|', '/')} |"
            for pmcid, result in sorted(pmc_results.items())
        )
    lines += [
        "", "## Routing", "",
        "- `CANONICAL_CANDIDATE` -> consider `legend-deepdive`.",
        "- `DISCOVERY_ONLY` / `ENDPOINT_SEED` -> discovery and/or endpoint ledger.",
        "- `REPURPOSING_SEED` -> hypothesis forge, then safety triage for concrete molecules.",
        "- `SAFETY_SIGNAL` -> BLOCK-1/evidence-quality review before promotion.",
        "- `P0_FAST_TRACK` / `P1_HIGH` -> review first; evidence and safety gates still apply.",
        "- `READ_QUEUE_TAIL` -> tracked reading debt. Never discarded or closed.",
        "",
        "No class authorizes skipping a study. Disease-label proximity does not equal usefulness:",
        "oncology often carries WWOX folding/stability/degradation mechanism, while adult",
        "neurology can carry shared pathways, biomarkers, and human-tested molecules.",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--fetch-pubmed", action="store_true")
    parser.add_argument("--pmc-dir", default="")
    parser.add_argument("--max-pmc", type=int, default=10)
    parser.add_argument("--json-out", default="")
    parser.add_argument("--proband-matrix", default=str(DEFAULT_PROBAND_MATRIX))
    args = parser.parse_args()

    raw = Path(args.input).read_text(errors="replace")
    expected_count = parse_expected_count(raw)
    classes = parse_triage_classes(raw)
    pmids = extract_pmids(raw)
    records = fetch_pubmed(pmids) if args.fetch_pubmed and pmids else fallback_records(raw, classes)
    by_pmid = {str(record.get("pmid")): record for record in records}
    for pmid in pmids:
        by_pmid.setdefault(
            pmid,
            {"pmid": pmid, "title": "", "abstract": "", "doi": "", "pmcid": "", "journal": "", "year": ""},
        )
    ranked = score_records(list(by_pmid.values()), classes)
    if args.proband_matrix:
        ranked = apply_proband_matrix(ranked, Path(args.proband_matrix))

    pmc_results: dict[str, str] = {}
    if args.pmc_dir:
        candidates = [
            (int(record["sweep_score"]), str(record["pmcid"]))
            for record in ranked if record.get("pmcid")
        ]
        for _score, pmcid in sorted(set(candidates), reverse=True)[:args.max_pmc]:
            try:
                title, length = fetch_pmc_text(pmcid, Path(args.pmc_dir))
                pmc_results[pmcid] = f"OK — {title[:80]} ({length} chars body)"
            except Exception as exc:  # noqa: BLE001
                pmc_results[pmcid] = f"ERROR — {exc}"

    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render(ranked, pmc_results, expected_count), encoding="utf-8")
    if args.json_out:
        Path(args.json_out).write_text(
            json.dumps({"records": ranked, "pmc_retrieved": pmc_results}, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
    return 2 if expected_count is not None and expected_count != len(ranked) else 0


if __name__ == "__main__":
    raise SystemExit(main())
