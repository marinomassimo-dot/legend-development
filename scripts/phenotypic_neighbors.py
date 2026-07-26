#!/usr/bin/env python3
"""Phenotypic-similarity neighbours of a disease, from public HPO annotations.

Given a query disease (default: WOREE / OMIM:616211) this computes the
information-content-weighted phenotypic similarity (Resnik best-match, symmetric
"phenodigm"-style average) between the query's HPO profile and every other
disease annotated in the HPO ``phenotype.hpoa`` file, and prints a ranked list
of the phenotypically nearest diseases.

It is the offline, stdlib-only re-implementation of the Monarch semantic-
similarity capability (semsimian / OAK). It reproduces the same score family
while depending on nothing but the Python standard library and two public files:

  * ``phenotype.hpoa``  — HPO disease-phenotype annotations (HPO project)
  * ``hp.obo``          — the Human Phenotype Ontology (is_a graph)

Both are public, disease-level resources. **No patient data is used or required**
— the input is a disease identifier, not an individual. Output is a research
prioritisation aid: phenotypic proximity is *not* mechanistic transfer, and a
neighbour is a lead to read, never a conclusion.

Example
-------
    python3 phenotypic_neighbors.py \
        --hpoa phenotype.hpoa --hp-obo hp.obo \
        --query OMIM:616211 --top 25 --out woree_neighbors.tsv

Data retrieval
--------------
    curl -L -o phenotype.hpoa https://purl.obolibrary.org/obo/hp/hpoa/phenotype.hpoa
    curl -L -o hp.obo         https://purl.obolibrary.org/obo/hp.obo
"""

from __future__ import annotations

import argparse
import math
import sys
from functools import lru_cache
from pathlib import Path


def load_hpoa(path: Path) -> tuple[dict[str, set[str]], dict[str, str]]:
    """Return (disease_id -> set(HP terms), disease_id -> disease_name).

    Negated annotations (qualifier == "NOT") are excluded.
    """
    lines = [ln.rstrip("\n") for ln in path.read_text(encoding="utf-8").splitlines()
             if ln and not ln.startswith("#")]
    header = lines[0].split("\t")
    idx = {name: header.index(name) for name in
           ("database_id", "hpo_id", "disease_name", "qualifier")}
    profiles: dict[str, set[str]] = {}
    names: dict[str, str] = {}
    for row in (ln.split("\t") for ln in lines[1:]):
        if len(row) <= max(idx.values()):
            continue
        if row[idx["qualifier"]] == "NOT":
            continue
        hp = row[idx["hpo_id"]]
        if not hp.startswith("HP:"):
            continue
        disease = row[idx["database_id"]]
        profiles.setdefault(disease, set()).add(hp)
        names[disease] = row[idx["disease_name"]]
    return profiles, names


def load_hp_parents(path: Path) -> dict[str, set[str]]:
    """Parse hp.obo into term -> set(direct is_a parents), HP terms only."""
    parents: dict[str, set[str]] = {}
    current: str | None = None
    in_term = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line == "[Term]":
            in_term, current = True, None
        elif line.startswith("[") and line.endswith("]"):
            in_term = False
        elif in_term and line.startswith("id: HP:"):
            current = line[4:].strip()
            parents.setdefault(current, set())
        elif in_term and current and line.startswith("is_a: HP:"):
            parent = line[len("is_a:"):].split("!")[0].strip()
            if parent.startswith("HP:"):
                parents[current].add(parent)
    return parents


def build_ancestors(parents: dict[str, set[str]]):
    """Return a memoised ancestors(term) -> frozenset including the term itself."""

    @lru_cache(maxsize=None)
    def ancestors(term: str) -> frozenset[str]:
        acc = {term}
        for parent in parents.get(term, ()):  # missing terms behave as roots
            acc |= ancestors(parent)
        return frozenset(acc)

    return ancestors


def information_content(profiles, ancestors) -> dict[str, float]:
    """IC(term) = -log(freq), freq = fraction of diseases whose ancestor-expanded
    profile contains the term. Computed over the annotation corpus itself."""
    n = len(profiles)
    counts: dict[str, int] = {}
    for terms in profiles.values():
        expanded: set[str] = set()
        for term in terms:
            expanded |= ancestors(term)
        for anc in expanded:
            counts[anc] = counts.get(anc, 0) + 1
    return {term: -math.log(count / n) for term, count in counts.items()}


def resnik_mica(a: str, b: str, ancestors, ic) -> float:
    """Resnik similarity: IC of the most informative common ancestor."""
    common = ancestors(a) & ancestors(b)
    return max((ic.get(term, 0.0) for term in common), default=0.0)


def phenodigm(profile_a: set[str], profile_b: set[str], ancestors, ic) -> float:
    """Symmetric best-match average of Resnik MICA scores (phenodigm-style)."""
    if not profile_a or not profile_b:
        return 0.0
    a_to_b = sum(max(resnik_mica(a, b, ancestors, ic) for b in profile_b)
                 for a in profile_a) / len(profile_a)
    b_to_a = sum(max(resnik_mica(a, b, ancestors, ic) for a in profile_a)
                 for b in profile_b) / len(profile_b)
    return (a_to_b + b_to_a) / 2.0


def rank_neighbours(query: str, profiles, names, ancestors, ic, min_shared: int):
    """Rank all diseases by phenotypic similarity to ``query``.

    A cheap candidate pre-filter (shared ancestor-expanded terms) keeps the
    all-vs-one comparison tractable without changing the top of the ranking.
    """
    if query not in profiles:
        raise KeyError(query)
    q_terms = profiles[query]
    q_expanded: set[str] = set()
    for term in q_terms:
        q_expanded |= ancestors(term)

    ranked = []
    for disease, terms in profiles.items():
        if disease == query:
            continue
        expanded: set[str] = set()
        for term in terms:
            expanded |= ancestors(term)
        if len(expanded & q_expanded) < min_shared:
            continue
        score = phenodigm(q_terms, terms, ancestors, ic)
        ranked.append((score, disease, len(terms & q_terms), names.get(disease, "")))
    ranked.sort(reverse=True)
    return ranked


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--hpoa", required=True, type=Path, help="phenotype.hpoa")
    parser.add_argument("--hp-obo", required=True, type=Path, help="hp.obo")
    parser.add_argument("--query", default="OMIM:616211",
                        help="Query disease id (default OMIM:616211 = WOREE)")
    parser.add_argument("--min-shared", type=int, default=6,
                        help="Candidate pre-filter: min shared expanded terms")
    parser.add_argument("--top", type=int, default=25, help="Rows to print")
    parser.add_argument("--out", type=Path, help="Optional TSV output of --top rows")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    profiles, names = load_hpoa(args.hpoa)
    parents = load_hp_parents(args.hp_obo)
    ancestors = build_ancestors(parents)
    ic = information_content(profiles, ancestors)
    try:
        ranked = rank_neighbours(args.query, profiles, names, ancestors, ic,
                                 args.min_shared)
    except KeyError:
        print(f"Query disease {args.query!r} not found in annotations",
              file=sys.stderr)
        return 1

    q_name = names.get(args.query, "")
    print(f"# phenotypic neighbours of {args.query} ({q_name})")
    print(f"# diseases={len(profiles)}  candidates={len(ranked)}")
    print("score\tshared\tdisease_id\tdisease_name")
    rows = [f"{s:.3f}\t{sh}\t{d}\t{nm}" for s, d, sh, nm in ranked[:args.top]]
    print("\n".join(rows))
    if args.out:
        header = "score\tshared\tdisease_id\tdisease_name\n"
        args.out.write_text(header + "\n".join(rows) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
