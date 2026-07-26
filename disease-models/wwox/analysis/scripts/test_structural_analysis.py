#!/usr/bin/env python3
"""Regression and public-data smoke tests for structural analysis scripts."""

from __future__ import annotations

import importlib.util
import hashlib
import math
import tempfile
import unittest
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"


def load_module(filename: str, name: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


RESIDUE = load_module("residue_context.py", "residue_context")
KFERQ = load_module("kferq_geometry.py", "kferq_geometry")
PREPARE = load_module(
    "prepare_redteam_structures.py", "prepare_redteam_structures"
)


class StructuralAnalysisTests(unittest.TestCase):
    def test_sphere_points_are_unit_length(self) -> None:
        points = RESIDUE.sphere_points(50)
        self.assertEqual(points.shape, (50, 3))
        np.testing.assert_allclose(
            np.linalg.norm(points, axis=1),
            np.ones(50),
            atol=1e-12,
        )

    def test_public_alphafold_residue_context(self) -> None:
        result = RESIDUE.analyse(
            str(DATA / "WWOX_Q9NZC7_AlphaFold.pdb"),
            [230, 252, 282],
            point_count=80,
        )
        by_residue = {row["resnum"]: row for row in result}
        self.assertEqual(set(by_residue), {230, 252, 282})
        self.assertEqual(by_residue[230]["aa"], "Q")
        self.assertGreater(by_residue[230]["pLDDT"], 90)
        self.assertLess(by_residue[230]["relSASA"], 0.10)
        self.assertGreater(by_residue[252]["relSASA"], by_residue[230]["relSASA"])

    def test_public_alphafold_motif_geometry(self) -> None:
        result = KFERQ.analyse(
            str(DATA / "WWOX_Q9NZC7_AlphaFold.pdb"),
            motif=[187, 188, 189, 190, 191],
            anchors=[187, 190],
            probes=[230, 252],
            point_count=60,
        )
        self.assertEqual(len(result["motif_static_accessibility"]), 5)
        contacts = {
            row["resnum"]: row for row in result["probe_to_anchor_contacts"]
        }
        self.assertIsNotNone(contacts[230]["minimum_all_atom_contact"])
        self.assertTrue(
            math.isfinite(
                contacts[230]["minimum_all_atom_contact"]["distance_A"]
            )
        )

    def test_missing_atom_file_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            empty = Path(temporary) / "empty.pdb"
            empty.write_text("HEADER empty\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                RESIDUE.analyse(str(empty), [230], point_count=10)
            with self.assertRaises(ValueError):
                KFERQ.analyse(
                    str(empty), [187], [187], [230], point_count=10
                )

    def test_redteam_structure_derivation_is_byte_reproducible(self) -> None:
        source = (DATA / "WWOX_Q9NZC7_AlphaFold.pdb").read_bytes()
        derived = PREPARE.derive_nohelix(source)
        self.assertEqual(
            hashlib.sha256(source).hexdigest(),
            PREPARE.ALPHAFOLD_PDB_SHA256,
        )
        self.assertEqual(
            hashlib.sha256(derived).hexdigest(),
            PREPARE.NOHELIX_SHA256,
        )
        atom_residues = {
            int(line[22:26])
            for line in derived.decode("ascii").splitlines()
            if line.startswith("ATOM")
        }
        self.assertFalse(atom_residues.intersection(range(227, 250)))

    def test_structure_preparation_writes_only_verified_local_derivatives(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            outputs = PREPARE.prepare(
                DATA / "WWOX_Q9NZC7_AlphaFold.pdb",
                Path(temporary),
                fetch_public=False,
            )
            self.assertEqual(
                {path.name for path in outputs},
                {"AF-Q9NZC7-F1.pdb", "AF_nohelix.pdb"},
            )
            for output in outputs:
                self.assertTrue(output.is_file())


if __name__ == "__main__":
    unittest.main()
