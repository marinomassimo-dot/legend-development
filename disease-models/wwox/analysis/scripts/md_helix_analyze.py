#!/usr/bin/env python3
"""Measure predeclared observables from the exploratory WWOX helix screen.

The analyser deliberately does not emit an automatic KEEP/DISCARD verdict.
P252A and P282A are biological comparators from a different mechanistic
context; separation on this simulated helix observable would not establish
assay sensitivity for turnover or chaperone-mediated processes.

Outputs remain ``EXPLO`` and require independent scientific review.
"""

from __future__ import annotations

import argparse
import glob
import json
import math
import sys
from pathlib import Path


HELIX = (226, 251)
EXCLUDED_HBOND_START = 226
MOTIF = tuple(range(187, 192))
TAIL = tuple(range(402, 410))
SYSTEMS = ("WT", "Q230P", "P252A", "P282A")
HBOND_CUTOFF_NM = 0.35
DISCARD_FRACTION = 0.5


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("md-output/helix-screen"))
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="list discoverable completed runs without loading MDTraj",
    )
    return parser.parse_args(argv)


def discover_runs(root: Path) -> dict[str, list[Path]]:
    runs = {system: [] for system in SYSTEMS}
    for directory in sorted(root.glob("*_seed*")):
        system = directory.name.rsplit("_seed", 1)[0]
        topology = directory / "topology.pdb"
        trajectories = sorted(directory.glob("traj*.dcd"))
        if system in runs and topology.is_file() and trajectories:
            runs[system].append(directory)
    return runs


def load_dependencies():
    try:
        import mdtraj as md
        import numpy as np
    except ImportError as exc:
        raise RuntimeError(
            "analysis dependencies are not installed. Install MDTraj and NumPy "
            "in an isolated environment, or use --dry-run."
        ) from exc
    return md, np


def helix_hbond_occupancy(trajectory, md, np):
    """Return mean and per-bond O(i)-N(i+4) geometric occupancy."""
    per_bond: dict[int, float] = {}
    topology = trajectory.topology
    for residue in range(HELIX[0], HELIX[1] - 3):
        if residue == EXCLUDED_HBOND_START:
            continue
        oxygen = topology.select(f"resSeq {residue} and name O")
        nitrogen = topology.select(f"resSeq {residue + 4} and name N")
        if len(oxygen) == 0 or len(nitrogen) == 0:
            continue
        distances = md.compute_distances(
            trajectory, [[oxygen[0], nitrogen[0]]]
        )[:, 0]
        per_bond[residue] = float((distances < HBOND_CUTOFF_NM).mean())
    mean = (
        float(np.mean(list(per_bond.values())))
        if per_bond
        else float("nan")
    )
    return mean, per_bond


def mean_residue_sasa(sasa, residue_index: dict[int, int], residues, np):
    values = [
        sasa[:, residue_index[residue]].mean()
        for residue in residues
        if residue in residue_index
    ]
    return float(np.mean(values)) if values else None


def analyse_run(directory: Path, md, np) -> dict[str, object]:
    trajectories = sorted(directory.glob("traj*.dcd"))
    topology = directory / "topology.pdb"
    loaded = (
        md.load([str(path) for path in trajectories], top=str(topology))
        if len(trajectories) > 1
        else md.load(str(trajectories[0]), top=str(topology))
    )
    protein = loaded.topology.select("protein")
    loaded = loaded.atom_slice(protein)
    loaded = loaded[int(len(loaded) * DISCARD_FRACTION):]
    if len(loaded) < 5:
        raise ValueError(f"too few post-discard frames in {directory}")

    occupancy, per_bond = helix_hbond_occupancy(loaded, md, np)
    if math.isnan(occupancy):
        raise ValueError(f"no helix hydrogen-bond observables in {directory}")
    stable_core = loaded.topology.select("name CA and resSeq 150 to 400")
    if len(stable_core) == 0:
        raise ValueError(f"stable alignment core absent in {directory}")
    loaded.superpose(loaded, 0, atom_indices=stable_core)
    helix_ca = loaded.topology.select(
        f"name CA and resSeq {HELIX[0]} to {HELIX[1]}"
    )
    if len(helix_ca) == 0:
        raise ValueError(f"helix C-alpha atoms absent in {directory}")
    coordinates = loaded.xyz[:, helix_ca, :]
    rmsf = float(
        np.sqrt(
            ((coordinates - coordinates.mean(0)) ** 2).sum(-1).mean(0)
        ).mean()
    )

    sasa = md.shrake_rupley(loaded, mode="residue")
    residue_index = {
        residue.resSeq: residue.index
        for residue in loaded.topology.residues
    }
    return {
        "run": directory.name,
        "frames_used": len(loaded),
        "helix_hbond_occupancy": occupancy,
        "per_bond": per_bond,
        "helix_rmsf_nm": rmsf,
        "motif_sasa_nm2_exploratory": mean_residue_sasa(
            sasa, residue_index, MOTIF, np
        ),
        "tail_402_409_sasa_nm2": mean_residue_sasa(
            sasa, residue_index, TAIL, np
        ),
    }


def finite(values):
    return [value for value in values if not math.isnan(value)]


def aggregate(results: dict[str, list[dict[str, object]]]) -> dict[str, object]:
    summary: dict[str, object] = {}
    for system in SYSTEMS:
        runs = results.get(system, [])
        occupancies = finite(
            [float(run["helix_hbond_occupancy"]) for run in runs]
        )
        rmsf_values = finite([float(run["helix_rmsf_nm"]) for run in runs])
        if not occupancies:
            summary[system] = {"n": 0}
            continue
        occupancy_mean = sum(occupancies) / len(occupancies)
        occupancy_sd = (
            math.sqrt(
                sum((value - occupancy_mean) ** 2 for value in occupancies)
                / (len(occupancies) - 1)
            )
            if len(occupancies) > 1
            else 0.0
        )
        summary[system] = {
            "n": len(occupancies),
            "occupancy_mean": occupancy_mean,
            "occupancy_sd": occupancy_sd,
            "rmsf_mean_nm": (
                sum(rmsf_values) / len(rmsf_values)
                if rmsf_values
                else None
            ),
        }
    return summary


def report(results: dict[str, list[dict[str, object]]]) -> dict[str, object]:
    return {
        "status": "EXPLO",
        "decision": "NOT_AUTOMATED",
        "decision_reason": (
            "The available biological comparators do not calibrate assay "
            "sensitivity for this simulated helix observable."
        ),
        "topological_exclusion": (
            "O226...N230 is excluded because proline lacks the backbone "
            "amide hydrogen; its loss is not dynamic evidence."
        ),
        "summary": aggregate(results),
        "runs": results,
    }


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    discovered = discover_runs(args.root)
    if args.dry_run:
        print(
            json.dumps(
                {
                    "status": "EXPLO",
                    "discoverable_runs": {
                        system: [str(path) for path in paths]
                        for system, paths in discovered.items()
                    },
                },
                indent=2,
            )
        )
        return 0
    try:
        md, np = load_dependencies()
        results = {
            system: [analyse_run(path, md, np) for path in paths]
            for system, paths in discovered.items()
        }
        payload = report(results)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    rendered = json.dumps(payload, indent=2, allow_nan=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
