#!/usr/bin/env python3
"""Exploratory high-temperature screen of WWOX residues 226–251.

The screen measures a fast, simulated structural response across WT, Q230P,
P252A and P282A.  It cannot demonstrate degron exposure, chaperone binding,
turnover, treatment response, or clinical relevance.  All outputs are ``EXPLO``.

Heavy dependencies are loaded only for execution.  ``--help`` and ``--dry-run``
work in a clean clone without OpenMM, PDBFixer or MDTraj.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
DEFAULT_INPUT = (
    ROOT
    / "disease-models"
    / "wwox"
    / "analysis"
    / "data"
    / "redteam"
    / "AF_SDR.pdb"
)
MUTATIONS = {
    "WT": (),
    "Q230P": ("GLN-230-PRO",),
    "P252A": ("PRO-252-ALA",),
    "P282A": ("PRO-282-ALA",),
}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--variant", choices=tuple(MUTATIONS), required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--ns", type=float, default=10.0)
    parser.add_argument("--temp-k", type=float, default=400.0)
    parser.add_argument("--padding-nm", type=float, default=1.2)
    parser.add_argument("--output-root", type=Path, default=Path("md-output/helix-screen"))
    parser.add_argument("--implicit", action="store_true")
    parser.add_argument("--benchmark", action="store_true")
    parser.add_argument("--platform", default="auto")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def validate_args(args: argparse.Namespace) -> None:
    if not args.input.is_file():
        raise ValueError(f"input PDB does not exist: {args.input}")
    if args.ns <= 0:
        raise ValueError("--ns must be positive")
    if not 273.15 <= args.temp_k <= 500:
        raise ValueError("--temp-k must be between 273.15 and 500")
    if args.padding_nm <= 0:
        raise ValueError("--padding-nm must be positive")


def execution_plan(args: argparse.Namespace) -> dict[str, object]:
    return {
        "status": "EXPLO",
        "warning": "simulated structural response; not biological evidence",
        "input": str(args.input.resolve()),
        "variant": args.variant,
        "mutations": list(MUTATIONS[args.variant]),
        "seed": args.seed,
        "production_ns": args.ns,
        "temperature_k": args.temp_k,
        "solvent": "implicit GBn2" if args.implicit else "explicit TIP3P",
        "platform_request": args.platform,
        "output_root": str(args.output_root),
        "benchmark_only": args.benchmark,
    }


def load_dependencies():
    try:
        import numpy as np
        from mdtraj.reporters import DCDReporter
        from openmm import (
            LangevinMiddleIntegrator,
            MonteCarloBarostat,
            Platform,
            unit,
        )
        from openmm.app import (
            ForceField,
            HBonds,
            Modeller,
            NoCutoff,
            PDBFile,
            PME,
            Simulation,
            StateDataReporter,
        )
        from pdbfixer import PDBFixer
    except ImportError as exc:
        raise RuntimeError(
            "MD dependencies are not installed. Use an isolated environment "
            "with NumPy, OpenMM, PDBFixer and MDTraj, or use --dry-run."
        ) from exc
    return locals()


def select_platform(platform_class, requested: str):
    if requested != "auto":
        return platform_class.getPlatformByName(requested)
    errors = []
    for candidate in ("OpenCL", "CUDA", "CPU"):
        try:
            return platform_class.getPlatformByName(candidate)
        except Exception as exc:
            errors.append(f"{candidate}: {exc}")
    raise RuntimeError("no OpenMM platform available (" + "; ".join(errors) + ")")


def build_model(dep, args: argparse.Namespace):
    fixer = dep["PDBFixer"](filename=str(args.input))
    if MUTATIONS[args.variant]:
        fixer.applyMutations(list(MUTATIONS[args.variant]), "A")
    fixer.findMissingResidues()
    fixer.findMissingAtoms()
    fixer.addMissingAtoms()
    modeller_class = dep["Modeller"]
    unit = dep["unit"]
    if args.implicit:
        forcefield = dep["ForceField"]("amber14-all.xml", "implicit/gbn2.xml")
        modeller = modeller_class(fixer.topology, fixer.positions)
        modeller.addHydrogens(forcefield, pH=7.4)
        return modeller, forcefield
    forcefield = dep["ForceField"]("amber14-all.xml", "amber14/tip3pfb.xml")
    modeller = modeller_class(fixer.topology, fixer.positions)
    modeller.addHydrogens(forcefield, pH=7.4)
    modeller.addSolvent(
        forcefield,
        padding=args.padding_nm * unit.nanometer,
        ionicStrength=0.15 * unit.molar,
        positiveIon="Na+",
        negativeIon="Cl-",
        model="tip3p",
    )
    return modeller, forcefield


def run(args: argparse.Namespace) -> dict[str, object]:
    dep = load_dependencies()
    unit = dep["unit"]
    modeller, forcefield = build_model(dep, args)
    if args.implicit:
        system = forcefield.createSystem(
            modeller.topology,
            nonbondedMethod=dep["NoCutoff"],
            constraints=dep["HBonds"],
            hydrogenMass=4 * unit.amu,
        )
    else:
        system = forcefield.createSystem(
            modeller.topology,
            nonbondedMethod=dep["PME"],
            nonbondedCutoff=1.0 * unit.nanometer,
            constraints=dep["HBonds"],
            hydrogenMass=4 * unit.amu,
        )
        system.addForce(
            dep["MonteCarloBarostat"](
                1.0 * unit.bar, args.temp_k * unit.kelvin, 25
            )
        )
    integrator = dep["LangevinMiddleIntegrator"](
        300 * unit.kelvin,
        1.0 / unit.picosecond,
        0.004 * unit.picoseconds,
    )
    integrator.setRandomNumberSeed(args.seed)
    platform = select_platform(dep["Platform"], args.platform)
    simulation = dep["Simulation"](
        modeller.topology, system, integrator, platform
    )
    simulation.context.setPositions(modeller.positions)
    simulation.minimizeEnergy(maxIterations=2_000)
    simulation.context.setVelocitiesToTemperature(
        300 * unit.kelvin, args.seed
    )

    if args.benchmark:
        simulation.step(500)
        started = time.time()
        simulation.step(2_500)
        elapsed = time.time() - started
        ns_per_day = (2_500 * 0.004 / 1_000) / (elapsed / 86_400)
        return execution_plan(args) | {
            "atoms": system.getNumParticles(),
            "platform": platform.getName(),
            "ns_per_day": round(ns_per_day, 1),
            "estimated_hours": round(args.ns / ns_per_day * 24, 1),
        }

    output = args.output_root / f"{args.variant}_seed{args.seed}"
    output.mkdir(parents=True, exist_ok=True)
    production_steps = int(args.ns * 1_000 / 0.004)
    protein_atoms = [
        atom.index
        for atom in simulation.topology.atoms()
        if atom.residue.name not in ("HOH", "NA", "CL")
    ]
    # Construct reporters before equilibration so API incompatibilities fail fast.
    dcd_reporter = dep["DCDReporter"](
        str(output / "traj.dcd"), 5_000, atomSubset=protein_atoms
    )
    state_reporter = dep["StateDataReporter"](
        str(output / "state.tsv"),
        5_000,
        step=True,
        time=True,
        potentialEnergy=True,
        temperature=True,
        density=not args.implicit,
        speed=True,
        progress=True,
        totalSteps=production_steps,
        separator="\t",
    )

    simulation.step(25_000)
    for temperature in dep["np"].linspace(300, args.temp_k, 6)[1:]:
        integrator.setTemperature(float(temperature) * unit.kelvin)
        simulation.step(12_500)
    simulation.step(50_000)
    simulation.context.setTime(0 * unit.picoseconds)
    simulation.reporters.extend([dcd_reporter, state_reporter])

    state = simulation.context.getState(getPositions=True)
    protein_model = dep["Modeller"](
        simulation.topology, state.getPositions()
    )
    protein_model.delete(
        [
            residue
            for residue in protein_model.topology.residues()
            if residue.name in ("HOH", "NA", "CL")
        ]
    )
    with (output / "topology.pdb").open("w", encoding="utf-8") as handle:
        dep["PDBFile"].writeFile(
            protein_model.topology, protein_model.positions, handle
        )

    started = time.time()
    simulation.step(production_steps)
    summary = execution_plan(args) | {
        "atoms": system.getNumParticles(),
        "platform": platform.getName(),
        "timestep_fs": 4,
        "hydrogen_mass_repartitioning": True,
        "wall_hours": round((time.time() - started) / 3_600, 3),
        "analysis_exclusion": (
            "Do not count O226...N230: loss is topological for proline, "
            "not a propagated dynamic observation."
        ),
    }
    (output / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    return summary


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        validate_args(args)
        result = execution_plan(args) if args.dry_run else run(args)
    except (RuntimeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
