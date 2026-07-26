#!/usr/bin/env python3
"""Measure disease-level residue context on a public protein structure.

Computes sampled Shrake–Rupley solvent accessibility, relative accessibility,
P-SEA-like secondary structure, AlphaFold pLDDT, heavy-atom contact density and
distance to a declared catalytic triad. These are geometric model outputs, not
experimental evidence or medical advice.

Dependency: NumPy. The script performs no network access and writes only when
``--output`` is supplied.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np


MAX_ASA = {
    "ALA": 129, "ARG": 274, "ASN": 195, "ASP": 193, "CYS": 167,
    "GLN": 225, "GLU": 223, "GLY": 104, "HIS": 224, "ILE": 197,
    "LEU": 201, "LYS": 236, "MET": 224, "PHE": 240, "PRO": 159,
    "SER": 155, "THR": 172, "TRP": 285, "TYR": 263, "VAL": 174,
}
THREE_TO_ONE = {
    "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C",
    "GLN": "Q", "GLU": "E", "GLY": "G", "HIS": "H", "ILE": "I",
    "LEU": "L", "LYS": "K", "MET": "M", "PHE": "F", "PRO": "P",
    "SER": "S", "THR": "T", "TRP": "W", "TYR": "Y", "VAL": "V",
}
VDW = {
    "C": 1.70, "N": 1.55, "O": 1.52, "S": 1.80,
    "H": 1.20, "P": 1.80, "SE": 1.90,
}
PROBE_ANGSTROM = 1.4
DEFAULT_TRIAD = (281, 293, 297)


def parse_pdb(path: str):
    """Parse heavy ATOM records from the first PDB model."""
    coords, elements, residue_ids = [], [], []
    residue_names, atom_names, b_factors = [], [], []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("ENDMDL"):
                break
            if not line.startswith("ATOM") or line[16] not in (" ", "A"):
                continue
            element = (line[76:78].strip().upper() or line[12:16].strip()[0])
            if element == "H":
                continue
            coords.append(
                (float(line[30:38]), float(line[38:46]), float(line[46:54]))
            )
            elements.append(element)
            residue_ids.append(int(line[22:26]))
            residue_names.append(line[17:20].strip())
            atom_names.append(line[12:16].strip())
            b_factors.append(float(line[60:66]))
    return (
        np.array(coords),
        np.array(elements),
        np.array(residue_ids),
        np.array(residue_names),
        np.array(atom_names),
        np.array(b_factors),
    )


def sphere_points(count: int) -> np.ndarray:
    """Return nearly uniform points on a unit sphere."""
    index = np.arange(count) + 0.5
    phi = np.arccos(1 - 2 * index / count)
    theta = math.pi * (1 + 5**0.5) * index
    return np.stack(
        [
            np.cos(theta) * np.sin(phi),
            np.sin(theta) * np.sin(phi),
            np.cos(phi),
        ],
        axis=1,
    )


def shrake_rupley(
    coords: np.ndarray, elements: np.ndarray, point_count: int = 500
) -> np.ndarray:
    """Compute sampled solvent-accessible area per atom in Å²."""
    radii = np.array([VDW.get(element, 1.70) for element in elements])
    radii = radii + PROBE_ANGSTROM
    points = sphere_points(point_count)
    areas = np.zeros(len(coords))
    max_radius = radii.max()
    for atom_index in range(len(coords)):
        radius = radii[atom_index]
        distances = np.linalg.norm(coords - coords[atom_index], axis=1)
        neighbours = np.where(
            (distances < radius + max_radius)
            & (np.arange(len(coords)) != atom_index)
        )[0]
        samples = coords[atom_index] + points * radius
        if len(neighbours):
            sample_distances = np.linalg.norm(
                samples[:, None, :] - coords[neighbours][None, :, :],
                axis=2,
            )
            buried = (
                sample_distances < radii[neighbours][None, :]
            ).any(axis=1)
            accessible_fraction = 1.0 - buried.mean()
        else:
            accessible_fraction = 1.0
        areas[atom_index] = (
            4.0 * math.pi * radius * radius * accessible_fraction
        )
    return areas


def psea_sse(ca_coords: np.ndarray) -> np.ndarray:
    """Assign a simplified P-SEA-like alpha/beta/coil state from Cα distances."""
    count = len(ca_coords)
    states = np.full(count, "c", dtype="<U1")

    def distance(index: int, offset: int) -> float:
        if index + offset >= count:
            return math.inf
        return float(np.linalg.norm(ca_coords[index + offset] - ca_coords[index]))

    for index in range(count):
        d2, d3, d4 = (
            distance(index, 2),
            distance(index, 3),
            distance(index, 4),
        )
        alpha = (
            abs(d2 - 5.5) < 0.5
            and abs(d3 - 5.3) < 0.5
            and abs(d4 - 6.4) < 0.6
        )
        beta = (
            abs(d2 - 6.7) < 0.6
            and abs(d3 - 9.9) < 0.9
            and abs(d4 - 12.4) < 1.1
        )
        if alpha:
            states[index:min(index + 5, count)] = "a"
        elif beta and states[index] != "a":
            states[index:min(index + 5, count)] = "b"
    return states


def burial_label(relative_sasa: float) -> str:
    if relative_sasa < 0.10:
        return "buried_core"
    if relative_sasa < 0.30:
        return "partially_exposed"
    return "surface_exposed"


def confidence_label(plddt: float) -> str:
    if plddt > 90:
        return "very_high"
    if plddt > 70:
        return "confident"
    if plddt > 50:
        return "low_caution"
    return "disordered_not_interpretable"


def analyse(
    pdb_path: str,
    residue_numbers: list[int],
    catalytic_triad: tuple[int, ...] = DEFAULT_TRIAD,
    point_count: int = 500,
) -> list[dict[str, object]]:
    coords, elements, residue_ids, residue_names, atom_names, b_factors = (
        parse_pdb(pdb_path)
    )
    if not len(coords):
        raise ValueError("No heavy ATOM records were parsed")

    atom_sasa = shrake_rupley(coords, elements, point_count)
    ca_mask = atom_names == "CA"
    ca_residue_ids, ca_coords = residue_ids[ca_mask], coords[ca_mask]
    states = psea_sse(ca_coords)
    triad_coords = [
        ca_coords[ca_residue_ids == residue][0]
        for residue in catalytic_triad
        if (ca_residue_ids == residue).any()
    ]
    state_names = {"a": "alpha_helix", "b": "beta_strand", "c": "coil_loop"}

    output = []
    for residue_number in residue_numbers:
        residue_mask = residue_ids == residue_number
        if not residue_mask.any():
            continue
        residue_name = str(residue_names[residue_mask][0])
        residue_sasa = float(atom_sasa[residue_mask].sum())
        relative_sasa = residue_sasa / MAX_ASA.get(residue_name, math.nan)
        ca_matches = np.where(ca_residue_ids == residue_number)[0]
        if not len(ca_matches):
            continue
        ca_index = int(ca_matches[0])
        residue_coord = ca_coords[ca_index]
        atom_distances = np.linalg.norm(coords - residue_coord, axis=1)
        contacts = int(
            ((atom_distances < 5.0) & (residue_ids != residue_number)).sum()
        )
        triad_distance = (
            min(float(np.linalg.norm(residue_coord - coord)) for coord in triad_coords)
            if triad_coords
            else math.nan
        )
        plddt = float(b_factors[residue_mask].mean())
        output.append(
            {
                "resnum": residue_number,
                "aa": THREE_TO_ONE.get(residue_name, residue_name),
                "sasa_A2": round(residue_sasa, 1),
                "relSASA": round(relative_sasa, 3),
                "burial": burial_label(relative_sasa),
                "sse": state_names[str(states[ca_index])],
                "pLDDT": round(plddt, 1),
                "pLDDT_confidence": confidence_label(plddt),
                "heavy_contacts_5A": contacts,
                "min_dist_catalytic_triad_A": round(triad_distance, 1),
            }
        )
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdb", required=True)
    parser.add_argument("--resnums", required=True, help="comma-separated residue numbers")
    parser.add_argument("--triad", default="281,293,297")
    parser.add_argument("--points", type=int, default=500)
    parser.add_argument("--output", help="optional JSON output path")
    args = parser.parse_args()

    try:
        residue_numbers = [int(value) for value in args.resnums.split(",")]
        catalytic_triad = tuple(int(value) for value in args.triad.split(","))
        result = analyse(
            args.pdb,
            residue_numbers,
            catalytic_triad=catalytic_triad,
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
