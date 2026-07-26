#!/usr/bin/env python3
"""Reproducible exploratory WWOX molecular-dynamics pilot.

This program validates structure preparation and short simulation plumbing for
public disease-model variants.  It does not establish a molecular mechanism,
biological effect, treatment response, or clinical recommendation.

OpenMM and PDBFixer are optional, deliberately isolated dependencies.  A clean
clone can run ``--dry-run`` and ``--help`` without installing them.
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
    / "WWOX_Q9NZC7_AlphaFold.pdb"
)
MUTATIONS = {
    "WT": None,
    "Q230P": "GLN-230-PRO",
    "P252A": "PRO-252-ALA",
    "P282A": "PRO-282-ALA",
}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--variant", choices=tuple(MUTATIONS), required=True)
    parser.add_argument("--output-root", type=Path, default=Path("md-output/pilot"))
    parser.add_argument("--steps", type=int, default=2_000)
    parser.add_argument("--box-nm", type=float, default=12.0)
    parser.add_argument("--seed", type=int, default=230)
    parser.add_argument(
        "--platform",
        default="auto",
        help="OpenMM platform name, or 'auto' to try OpenCL, CUDA, then CPU",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="validate inputs and print the execution plan without MD dependencies",
    )
    return parser.parse_args(argv)


def validate_args(args: argparse.Namespace) -> None:
    if not args.input.is_file():
        raise ValueError(f"input PDB does not exist: {args.input}")
    if args.steps < 1:
        raise ValueError("--steps must be positive")
    if args.box_nm <= 0:
        raise ValueError("--box-nm must be positive")


def execution_plan(args: argparse.Namespace) -> dict[str, object]:
    return {
        "status": "EXPLO",
        "purpose": "pipeline feasibility only; not biological evidence",
        "input": str(args.input.resolve()),
        "variant": args.variant,
        "mutation": MUTATIONS[args.variant],
        "steps": args.steps,
        "simulated_ps": args.steps * 0.002,
        "box_nm": args.box_nm,
        "seed": args.seed,
        "platform_request": args.platform,
        "output_root": str(args.output_root),
    }


def load_dependencies():
    try:
        from openmm import (
            LangevinMiddleIntegrator,
            MonteCarloBarostat,
            Platform,
            Vec3,
            unit,
        )
        from openmm.app import (
            ForceField,
            HBonds,
            Modeller,
            PME,
            PDBFile,
            Simulation,
            StateDataReporter,
        )
        from pdbfixer import PDBFixer
    except ImportError as exc:
        raise RuntimeError(
            "MD dependencies are not installed. Install OpenMM and PDBFixer "
            "in an isolated environment, or use --dry-run."
        ) from exc
    return {
        "LangevinMiddleIntegrator": LangevinMiddleIntegrator,
        "MonteCarloBarostat": MonteCarloBarostat,
        "Platform": Platform,
        "Vec3": Vec3,
        "unit": unit,
        "ForceField": ForceField,
        "HBonds": HBonds,
        "Modeller": Modeller,
        "PME": PME,
        "PDBFile": PDBFile,
        "Simulation": Simulation,
        "StateDataReporter": StateDataReporter,
        "PDBFixer": PDBFixer,
    }


def select_platform(platform_class, requested: str):
    if requested != "auto":
        return platform_class.getPlatformByName(requested)
    errors = []
    for candidate in ("OpenCL", "CUDA", "CPU"):
        try:
            return platform_class.getPlatformByName(candidate)
        except Exception as exc:  # platform availability is runtime-specific
            errors.append(f"{candidate}: {exc}")
    raise RuntimeError("no OpenMM platform available (" + "; ".join(errors) + ")")


def run(args: argparse.Namespace) -> dict[str, object]:
    dep = load_dependencies()
    unit = dep["unit"]
    fixer = dep["PDBFixer"](filename=str(args.input))
    mutation = MUTATIONS[args.variant]
    if mutation:
        fixer.applyMutations([mutation], "A")
    fixer.findMissingResidues()
    fixer.findMissingAtoms()
    fixer.addMissingAtoms()

    forcefield = dep["ForceField"]("amber14-all.xml", "amber14/tip3pfb.xml")
    modeller = dep["Modeller"](fixer.topology, fixer.positions)
    modeller.addHydrogens(forcefield, pH=7.4)
    modeller.addSolvent(
        forcefield,
        boxSize=dep["Vec3"](args.box_nm, args.box_nm, args.box_nm)
        * unit.nanometer,
        ionicStrength=0.15 * unit.molar,
        positiveIon="Na+",
        negativeIon="Cl-",
    )
    system = forcefield.createSystem(
        modeller.topology,
        nonbondedMethod=dep["PME"],
        nonbondedCutoff=0.9 * unit.nanometer,
        constraints=dep["HBonds"],
    )
    system.addForce(
        dep["MonteCarloBarostat"](1.0 * unit.bar, 300 * unit.kelvin, 25)
    )
    integrator = dep["LangevinMiddleIntegrator"](
        300 * unit.kelvin,
        1.0 / unit.picosecond,
        0.002 * unit.picoseconds,
    )
    integrator.setRandomNumberSeed(args.seed)
    platform = select_platform(dep["Platform"], args.platform)

    output = args.output_root / args.variant.lower()
    output.mkdir(parents=True, exist_ok=True)
    simulation = dep["Simulation"](
        modeller.topology, system, integrator, platform
    )
    simulation.context.setPositions(modeller.positions)
    simulation.minimizeEnergy(maxIterations=500)
    simulation.context.setVelocitiesToTemperature(
        300 * unit.kelvin, args.seed
    )
    simulation.reporters.append(
        dep["StateDataReporter"](
            str(output / "state.tsv"),
            100,
            step=True,
            time=True,
            potentialEnergy=True,
            kineticEnergy=True,
            temperature=True,
            density=True,
            speed=True,
            separator="\t",
        )
    )
    started = time.time()
    simulation.step(args.steps)
    state = simulation.context.getState(getPositions=True, getEnergy=True)
    with (output / "final.pdb").open("w", encoding="utf-8") as handle:
        dep["PDBFile"].writeFile(
            simulation.topology, state.getPositions(), handle
        )
    summary = execution_plan(args) | {
        "atoms": simulation.topology.getNumAtoms(),
        "residues": simulation.topology.getNumResidues(),
        "platform": platform.getName(),
        "potential_energy_kj_mol": state.getPotentialEnergy().value_in_unit(
            unit.kilojoule_per_mole
        ),
        "wall_seconds": round(time.time() - started, 2),
    }
    (output / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    return summary


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        validate_args(args)
        summary = execution_plan(args) if args.dry_run else run(args)
    except (RuntimeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
