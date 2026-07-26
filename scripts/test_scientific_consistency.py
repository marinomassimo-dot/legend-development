#!/usr/bin/env python3
"""Fail-closed guards against reintroducing retracted scientific inferences.

These checks do not decide biology. They enforce corrections already recorded
in the public canonical claim and therapeutic-strategy files across older
summaries and cumulative memory.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WWOX = ROOT / "disease-models" / "wwox"


def markdown_lines():
    for path in sorted(WWOX.rglob("*.md")):
        for number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), 1
        ):
            yield path.relative_to(ROOT), number, line


class ScientificConsistencyTests(unittest.TestCase):
    def test_k63_is_not_presented_as_a_universal_cma_route(self) -> None:
        stale = []
        shortcuts = (
            re.compile(r"(?i)K63\s*(?:→|->)\s*autophagy/CMA"),
            re.compile(r"(?i)K63\s*(?:→|->)\s*NO\b"),
            re.compile(
                r"(?i)K63.{0,40}enhances HSC70 recognition"
                r"|potenzia il riconoscimento da HSC70"
            ),
        )
        for path in sorted(ROOT.rglob("*.md")):
            for number, line in enumerate(
                path.read_text(encoding="utf-8").splitlines(), 1
            ):
                if any(pattern.search(line) for pattern in shortcuts):
                    stale.append(
                        f"{path.relative_to(ROOT)}:{number}: {line.strip()}"
                    )
        self.assertFalse(
            stale,
            "K63 is presented as a universal or proven CMA shortcut:\n"
            + "\n".join(stale),
        )

    def test_canonical_corrections_are_present(self) -> None:
        claims = (
            WWOX / "registries" / "claim_registry_current.md"
        ).read_text(encoding="utf-8")
        strategies = (
            WWOX / "therapeutics" / "therapeutic_strategies_current.md"
        ).read_text(encoding="utf-8")
        required = {
            "claim registry: recoverability heuristic withdrawal":
                "non ha valore predittivo dimostrato" in claims,
            "claim registry: mechanism unresolved":
                "CAUSA NON RISOLTA" in claims,
            "strategy: P47T equivalence retracted":
                "P47T↔Q230P equivalence were retracted" in strategies,
            "strategy: ASO does not repair sequence":
                "An ASO does not repair the sequence" in strategies,
        }
        missing = [label for label, present in required.items() if not present]
        self.assertFalse(
            missing,
            "Canonical correction anchors missing:\n" + "\n".join(missing),
        )

    def test_p47t_is_not_asserted_as_q230p_read_across_proof(self) -> None:
        stale = []
        negation = re.compile(
            r"(?i)\b(?:not|non|no proof|retract(?:ed|ion)?|ritirat|withdrawn|"
            r"comparator|caution|non dimostrat)\b"
        )
        for path, number, line in markdown_lines():
            if not re.search(r"(?i)\bP47T\b", line):
                continue
            if not re.search(r"(?i)read[- ]across|legge attraverso", line):
                continue
            if negation.search(line):
                continue
            stale.append(f"{path}:{number}: {line.strip()}")
        self.assertFalse(
            stale,
            "Retracted P47T→Q230P read-across remains asserted:\n"
            + "\n".join(stale),
        )

    def test_retracted_recoverable_window_is_not_reasserted(self) -> None:
        stale = []
        window = re.compile(
            r"(?i)(?:recoverable (?:stability )?window|finestra recuperabile)"
        )
        qualification = re.compile(
            r"(?i)(?:retract|withdrawn|ritirat|non validat|not validat|"
            r"no predictive|non ha valore predittivo|does not discriminate|"
            r"non discrimina|heuristic|euristic|not a guarantee)"
        )
        for path, number, line in markdown_lines():
            if window.search(line) and not qualification.search(line):
                stale.append(f"{path}:{number}: {line.strip()}")
        self.assertFalse(
            stale,
            "Retracted ΔΔG recoverability window remains asserted:\n"
            + "\n".join(stale),
        )

    def test_wildtype_geometry_does_not_prove_mutant_function(self) -> None:
        stale = []
        assertions = (
            re.compile(r"(?i)enzymatic machinery is intact"),
            re.compile(r"(?i)Q230 is structural, not catalytic"),
        )
        qualification = re.compile(
            r"(?i)(?:does not (?:prove|establish|demonstrate)|"
            r"wild[- ]type geometry|mutant function (?:is )?unknown|"
            r"not directly a catalytic residue)"
        )
        for path, number, line in markdown_lines():
            if any(pattern.search(line) for pattern in assertions):
                if not qualification.search(line):
                    stale.append(f"{path}:{number}: {line.strip()}")
        self.assertFalse(
            stale,
            "Wild-type structural distance is presented as proof of mutant function:\n"
            + "\n".join(stale),
        )

    def test_exact_splice_example_does_not_overclaim_aso_repair(self) -> None:
        stale = []
        overclaim = re.compile(
            r"(?i)(?:ASO.{0,160}(?:force correct splicing|"
            r"force correct splicing.{0,160}ASO|"
            r"mechanism-matched|targeted by a splice-switching ASO))"
        )
        qualification = re.compile(
            r"(?i)(?:does not repair|cannot repair|cannot recreate|"
            r"productive outcome|base edit|prime edit|editing|conditional)"
        )
        variant = re.compile(r"(?i)c\.\s*1057\s*-\s*2\s*A\s*>\s*G")
        for path, number, line in markdown_lines():
            if (
                variant.search(line)
                and overclaim.search(line)
                and not qualification.search(line)
            ):
                stale.append(f"{path}:{number}: {line.strip()}")
        self.assertFalse(
            stale,
            "Exact splice-site example overclaims ASO sequence repair:\n"
            + "\n".join(stale),
        )

    def test_q230p_protein_loss_cause_remains_unresolved(self) -> None:
        """Normal RNA + low protein must not be collapsed to degradation.

        The canonical correction explicitly keeps impaired translation,
        insolubility and accelerated turnover open. Older summaries may retain
        an instability hypothesis, but only when they also expose at least one
        competing mechanism or state that the cause remains unresolved.
        """
        stale = []
        collapsed_conclusions = (
            re.compile(
                r"(?i)sposta il bersaglio terapeutico.{0,120}"
                r"(?:degradazione|turnover)"
            ),
            re.compile(
                r"(?i)would confirm the post[- ]translational mechanism"
            ),
            re.compile(
                r"(?i)\bQ230P\b.{0,220}\bis a degradation lesion\b"
            ),
            re.compile(
                r"(?i)\bQ230\b.{0,520}\bmisfolding\s*(?:→|->)\s*"
                r"(?:degradation|degradazione)\b"
            ),
            re.compile(
                r"(?i)sostegno alla misfolding-dominance.{0,160}"
                r"Johannsen.{0,80}(?:dato wet|wet)"
            ),
        )
        q230p = re.compile(r"(?i)\b(?:Q230P|Gln230Pro)\b")
        protein_loss_claim = re.compile(
            r"(?i)(?:unstable/misfolded protein|protein degradation|"
            r"degradazione proteica|normal mRNA.{0,100}(?:low|absent|reduced)"
            r".{0,40}protein)"
        )
        competing_mechanism = re.compile(
            r"(?i)(?:cause remains unresolved|causa non risolta|"
            r"mechanism remains unresolved|meccanismo non risolto|"
            r"impaired translation|traduzione compromessa|insolubility|"
            r"insolubilit[aà])"
        )
        explicit_retraction = re.compile(
            r"(?i)(?:was an inference|era un['’]inferenza|not (?:a )?data|"
            r"non (?:è|era) un dato|cause (?:remains|is) unresolved|"
            r"causa resta non risolta|withdrawn|ritirat)"
        )

        for path in sorted(WWOX.rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            lines = text.splitlines()
            for number, line in enumerate(lines, 1):
                if (
                    any(pattern.search(line) for pattern in collapsed_conclusions)
                    and not explicit_retraction.search(line)
                ):
                    stale.append(f"{path.relative_to(ROOT)}:{number}: {line.strip()}")
            if (
                q230p.search(text)
                and protein_loss_claim.search(text)
                and not competing_mechanism.search(text)
            ):
                stale.append(
                    f"{path.relative_to(ROOT)}: document asserts a protein-loss "
                    "mechanism without preserving the unresolved alternatives"
                )

        self.assertFalse(
            stale,
            "Q230P protein loss is collapsed to degradation/instability even "
            "though the canonical cause is unresolved:\n" + "\n".join(stale),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
