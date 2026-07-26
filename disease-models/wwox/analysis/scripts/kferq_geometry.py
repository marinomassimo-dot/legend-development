#!/usr/bin/env python3
"""Audit the static geometry of a candidate chaperone-recognition motif.

The script reports sampled relative SASA for a declared motif and exact atom
identities for minimum contacts to declared anchor residues. Static geometry
does not demonstrate motif recognition, induced exposure, binding, flux or a
degradation pathway.

Dependency: NumPy. No network access and no patient-level input.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np


VDW = {"C": 1.70, "N": 1.55, "O": 1.52, "S": 1.80}
MAX_ASA = {
    "ALA": 129, "ARG": 274, "ASN": 195, "ASP": 193, "CYS": 167,
    "GLU": 223, "GLN": 225, "GLY": 104, "HIS": 224, "ILE": 197,
    "LEU": 201, "LYS": 236, "MET": 224, "PHE": 240, "PRO": 159,
    "SER": 155, "THR": 172, "TRP": 285, "TYR": 263, "VAL": 174,
}
THREE_TO_ONE = {
    "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C",
    "GLU": "E", "GLN": "Q", "GLY": "G", "HIS": "H", "ILE": "I",
    "LEU": "L", "LYS": "K", "MET": "M", "PHE": "F", "PRO": "P",
    "SER": "S", "THR": "T", "TRP": "W", "TYR": "Y", "VAL": "V",
}
BACKBONE = {"N", "CA", "C", "O", "OXT"}


def parse_atoms(path: str) -> list[tuple[int, str, str, np.ndarray, float]]:
    atoms = []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("ENDMDL"):
                break
            if not line.startswith("ATOM") or line[16] not in (" ", "A"):
                continue
            element = line[76:78].strip() or line[12:16].strip()[0]
            atoms.append(
                (
                    int(line[22:26]),
                    line[17:20].strip(),
                    line[12:16].strip(),
                    np.array(
                        [
                            float(line[30:38]),
                            float(line[38:46]),
                            float(line[46:54]),
                        ]
                    ),
                    VDW.get(element, 1.70),
                )
            )
    return atoms


def sampled_sasa(
    atoms: list[tuple[int, str, str, np.ndarray, float]],
    point_count: int = 200,
) -> np.ndarray:
    coords = np.array([atom[3] for atom in atoms])
    radii = np.array([atom[4] for atom in atoms]) + 1.4
    index = np.arange(point_count) + 0.5
    phi = np.arccos(1 - 2 * index / point_count)
    theta = math.pi * (1 + 5**0.5) * index
    sphere = np.c_[
        np.cos(theta) * np.sin(phi),
        np.sin(theta) * np.sin(phi),
        np.cos(phi),
    ]
    output = np.zeros(len(atoms))
    for atom_index in range(len(atoms)):
        samples = coords[atom_index] + radii[atom_index] * sphere
        distances = np.linalg.norm(
            coords[None, :, :] - samples[:, None, :],
            axis=2,
        )
        distances[:, atom_index] = 1e9
        accessible = (distances >= radii[None, :]).all(axis=1).sum()
        output[atom_index] = (
            4 * math.pi * radii[atom_index] ** 2 * accessible / point_count
        )
    return output


def minimum_contact(
    atoms: list[tuple[int, str, str, np.ndarray, float]],
    source: int,
    targets: list[int],
    sidechain_only: bool = False,
) -> dict[str, object] | None:
    source_atoms = [
        atom for atom in atoms
        if atom[0] == source and (not sidechain_only or atom[2] not in BACKBONE)
    ]
    target_atoms = [
        atom for atom in atoms
        if atom[0] in targets and (not sidechain_only or atom[2] not in BACKBONE)
    ]
    best = None
    for source_atom in source_atoms:
        for target_atom in target_atoms:
            distance = float(np.linalg.norm(source_atom[3] - target_atom[3]))
            item = {
                "distance_A": round(distance, 3),
                "source_atom": source_atom[2],
                "target_resnum": target_atom[0],
                "target_aa": THREE_TO_ONE.get(target_atom[1], target_atom[1]),
                "target_atom": target_atom[2],
            }
            if best is None or distance < float(best["distance_A"]):
                best = item
    return best


def analyse(
    pdb_path: str,
    motif: list[int],
    anchors: list[int],
    probes: list[int],
    point_count: int = 200,
) -> dict[str, object]:
    atoms = parse_atoms(pdb_path)
    if not atoms:
        raise ValueError("No ATOM records were parsed")
    atom_sasa = sampled_sasa(atoms, point_count)
    residue_sasa: dict[int, float] = defaultdict(float)
    residue_names: dict[int, str] = {}
    for atom, area in zip(atoms, atom_sasa):
        residue_sasa[atom[0]] += float(area)
        residue_names[atom[0]] = atom[1]

    motif_output = []
    for residue in motif:
        if residue not in residue_names:
            continue
        residue_name = residue_names[residue]
        relative_sasa = residue_sasa[residue] / MAX_ASA.get(residue_name, 200)
        motif_output.append(
            {
                "resnum": residue,
                "aa": THREE_TO_ONE.get(residue_name, residue_name),
                "sampled_sasa_A2": round(residue_sasa[residue], 3),
                "relative_sasa": round(relative_sasa, 3),
            }
        )

    probe_output = []
    for residue in probes:
        if residue not in residue_names:
            continue
        residue_name = residue_names[residue]
        relative_sasa = residue_sasa[residue] / MAX_ASA.get(residue_name, 200)
        probe_output.append(
            {
                "resnum": residue,
                "aa": THREE_TO_ONE.get(residue_name, residue_name),
                "relative_sasa": round(relative_sasa, 3),
                "minimum_all_atom_contact": minimum_contact(
                    atoms, residue, anchors
                ),
                "minimum_sidechain_contact": minimum_contact(
                    atoms, residue, anchors, sidechain_only=True
                ),
            }
        )

    return {
        "pdb": str(Path(pdb_path).name),
        "motif_residues": motif,
        "anchor_residues": anchors,
        "sampling_points_per_atom": point_count,
        "motif_static_accessibility": motif_output,
        "probe_to_anchor_contacts": probe_output,
        "interpretation": (
            "static exploratory geometry; not evidence of recognition, "
            "binding, induced exposure or degradation"
        ),
    }


def parse_numbers(value: str) -> list[int]:
    return [int(item) for item in value.split(",") if item.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdb", required=True)
    parser.add_argument("--motif", default="187,188,189,190,191")
    parser.add_argument("--anchors", default="187,190")
    parser.add_argument("--probes", default="47,230,239,252,282,372")
    parser.add_argument("--points", type=int, default=200)
    parser.add_argument("--output", help="optional JSON output path")
    args = parser.parse_args()

    try:
        result = analyse(
            args.pdb,
            parse_numbers(args.motif),
            parse_numbers(args.anchors),
            parse_numbers(args.probes),
            point_count=args.points,
        )
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    rendered = json.dumps(result, indent=2)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
