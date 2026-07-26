#!/usr/bin/env python3
"""Reconstruct the public structural inputs used by the red-team package.

The repository already ships the AlphaFold DB WWOX model. This script:

1. copies that model into an operator-selected output directory;
2. deterministically derives the lid-removal control by deleting ATOM records
   for residues 227–249;
3. optionally downloads the matching AlphaFold PAE JSON and experimental PDB
   entry 1WMV from their primary public repositories.

Every output is checked against the SHA-256 recorded during the original
public-data audit. Network retrieval is opt-in. No clinical or patient-level
input is accepted.

AlphaFold DB data are CC BY 4.0 and require AlphaFold/EMBL-EBI attribution.
RCSB PDB data-use terms and primary-structure citations apply to 1WMV.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
import urllib.request
from pathlib import Path


ALPHAFOLD_PDB_SHA256 = (
    "ccbc3367c4fe390fe8c67e7ce57900cf737595b5a495fb781b812726dc9d56cc"
)
NOHELIX_SHA256 = (
    "c099410c9e853bac362b72c968c914e47ca4b421d86e7230b0c2a382986252a4"
)
ALPHAFOLD_PAE_SHA256 = (
    "c7666bcc4c5223fd92d0ed363156e9a6c486f0367e8f615c956550e0b4d30cfd"
)
PDB_1WMV_SHA256 = (
    "cd475b4cf64607d1abe327f5faba6210e9c48916a5024ba3e3289ef6c499bf73"
)

PAE_URL = (
    "https://alphafold.ebi.ac.uk/files/"
    "AF-Q9NZC7-F1-predicted_aligned_error_v6.json"
)
PDB_1WMV_URL = "https://files.rcsb.org/download/1WMV.pdb"


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def verify(payload: bytes, expected: str, label: str) -> None:
    observed = sha256_bytes(payload)
    if observed != expected:
        raise ValueError(
            f"{label} SHA-256 mismatch: expected {expected}, observed {observed}"
        )


def derive_nohelix(
    alphafold_pdb: bytes,
    first_residue: int = 227,
    last_residue: int = 249,
) -> bytes:
    """Delete a residue interval while retaining original PDB atom serials."""
    output = []
    for line in alphafold_pdb.decode("ascii").splitlines():
        if line.startswith("ATOM"):
            residue_number = int(line[22:26])
            if first_residue <= residue_number <= last_residue:
                continue
        output.append(line)
    return ("\n".join(output) + "\n").encode("ascii")


def download(url: str, timeout: int = 60) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "legend-public-structure-audit/1.0"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def write_checked(
    destination: Path,
    payload: bytes,
    expected_sha256: str,
    force: bool = False,
) -> None:
    verify(payload, expected_sha256, destination.name)
    if destination.exists() and not force:
        existing = destination.read_bytes()
        verify(existing, expected_sha256, f"existing {destination.name}")
        return
    destination.write_bytes(payload)


def prepare(
    alphafold_path: Path,
    output_dir: Path,
    fetch_public: bool = False,
    force: bool = False,
) -> list[Path]:
    alphafold_payload = alphafold_path.read_bytes()
    verify(alphafold_payload, ALPHAFOLD_PDB_SHA256, "AlphaFold WWOX PDB")
    nohelix_payload = derive_nohelix(alphafold_payload)
    verify(nohelix_payload, NOHELIX_SHA256, "lid-removal control")

    output_dir.mkdir(parents=True, exist_ok=True)
    written = []
    targets = [
        (
            output_dir / "AF-Q9NZC7-F1.pdb",
            alphafold_payload,
            ALPHAFOLD_PDB_SHA256,
        ),
        (
            output_dir / "AF_nohelix.pdb",
            nohelix_payload,
            NOHELIX_SHA256,
        ),
    ]
    if fetch_public:
        targets.extend(
            [
                (
                    output_dir / "AF-Q9NZC7-F1-PAE.json",
                    download(PAE_URL),
                    ALPHAFOLD_PAE_SHA256,
                ),
                (
                    output_dir / "1WMV.pdb",
                    download(PDB_1WMV_URL),
                    PDB_1WMV_SHA256,
                ),
            ]
        )
    for destination, payload, checksum in targets:
        write_checked(destination, payload, checksum, force=force)
        written.append(destination)
    return written


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--alphafold-pdb", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument(
        "--fetch-public",
        action="store_true",
        help="also fetch AlphaFold PAE and RCSB 1WMV from primary repositories",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="replace existing outputs only after downloaded/input bytes verify",
    )
    args = parser.parse_args()

    try:
        paths = prepare(
            Path(args.alphafold_pdb),
            Path(args.output_dir),
            fetch_public=args.fetch_public,
            force=args.force,
        )
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    for path in paths:
        print(f"{sha256_bytes(path.read_bytes())}  {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
