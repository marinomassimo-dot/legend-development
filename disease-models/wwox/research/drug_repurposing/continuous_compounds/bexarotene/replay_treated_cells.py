"""Replay marker-gated, per-mouse transcript contrasts in GEO GSE283905."""
import argparse
import csv
import gzip
import hashlib
import io
from pathlib import Path
import tarfile

import h5py
import numpy as np


MARKERS = {
    "astrocyte": ("Aldh1l1", "Slc1a3", "Aqp4", "Slc1a2"),
    "microglia_homeostatic_enriched": ("P2ry12", "Tmem119", "Cx3cr1", "Hexb"),
    "opc": ("Pdgfra", "Vcan", "Cspg4", "Olig1"),
    "mature_oligodendrocyte": ("Mog", "Mag", "Mobp", "Plp1"),
}
TARGETS = tuple("Rxra Rxrb Rxrg Nr1h3 Nr1h2 Abca1 Abcg1 Apoe Hmgcr Hmgcs1 Fdft1 Sqle".split())
GENES = sorted(set(TARGETS).union(*MARKERS.values()))


def sample_arms(metadata):
    arms = {}
    with gzip.open(metadata, "rt") as handle:
        for line in handle:
            if line.startswith("^SAMPLE = "):
                sample = line.strip().split(" = ")[-1]
            if line.startswith("!Sample_characteristics_ch1 = treatment: "):
                arm = line.strip().rsplit(" ", 1)[-1].lower()
                arms[sample] = arm
    assert sorted(arms.values()) == ["bexarotene"] * 4 + ["vehicle"] * 4
    return arms


def select_counts(content):
    with h5py.File(io.BytesIO(content)) as handle:
        matrix = handle["matrix"]
        names = np.char.decode(matrix["features/name"][:])
        positions = matrix["indices"][:]
        offsets = matrix["indptr"][:]
        values = matrix["data"][:]
    tracked = np.full(len(names), -1, dtype=np.int32)
    for index, gene in enumerate(GENES):
        hit, = np.flatnonzero(names == gene)
        tracked[hit] = index
    selected = tracked[positions]
    keep = selected >= 0
    columns = np.searchsorted(offsets[1:], np.flatnonzero(keep), side="right")
    counts = np.zeros((len(GENES), len(offsets) - 1), dtype=np.int64)
    np.add.at(counts, (selected[keep], columns), values[keep])
    library_sizes = np.diff(np.r_[0, np.cumsum(values, dtype=np.int64)][offsets])
    return dict(zip(GENES, counts)), library_sizes


def sample_counts(archive, arms):
    with tarfile.open(archive) as source:
        for member in sorted(source.getmembers(), key=lambda item: item.name):
            sample = Path(member.name).name.split("_")[0]
            counts, total = select_counts(source.extractfile(member).read())
            hits = np.stack([sum((counts[g] > 0).astype(int) for g in genes)
                             for genes in MARKERS.values()])
            unique = (hits == hits.max(axis=0)).sum(axis=0) == 1
            for floor in (2, 3):
                for row, cell_type in enumerate(MARKERS):
                    selected = unique & (hits[row] >= floor) & (hits[row] == hits.max(axis=0))
                    if cell_type == "opc":
                        selected &= counts["Pdgfra"] > 0
                    cells = int(selected.sum())
                    umis = int(total[selected].sum())
                    for gene in TARGETS:
                        yield (sample, arms[sample], floor, cell_type, gene, cells, umis,
                               int(counts[gene][selected].sum()))


def contrasts(records):
    for floor in (2, 3):
        for cell_type in MARKERS:
            for gene in TARGETS:
                groups = {"vehicle": [], "bexarotene": []}
                for _, arm, min_markers, cls, label, n_cells, depth, count in records:
                    if (min_markers, cls, label) == (floor, cell_type, gene) and n_cells >= 20:
                        groups[arm].append(count / depth * 1e6)
                vehicle, treated = (np.array(groups[name]) for name in ("vehicle", "bexarotene"))
                if min(len(vehicle), len(treated)) < 2:
                    yield (floor, cell_type, gene, len(vehicle), len(treated), *("NA",) * 5)
                    continue
                log_vehicle, log_treated = np.log2(1 + vehicle), np.log2(1 + treated)
                deltas = [np.delete(log_treated, i).mean() - log_vehicle.mean() for i in range(len(treated))]
                deltas += [log_treated.mean() - np.delete(log_vehicle, i).mean() for i in range(len(vehicle))]
                summaries = (vehicle.mean(), treated.mean(), log_treated.mean() - log_vehicle.mean(),
                             min(deltas), max(deltas))
                yield (floor, cell_type, gene, len(vehicle), len(treated), *(f"{value:.7g}" for value in summaries))


def write_tsv(path, headings, rows):
    with path.open("w") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(headings.split())
        writer.writerows(rows)


def main(directory, archive, metadata):
    with (Path(__file__).parent / "treated_inputs.tsv").open() as handle:
        fingerprints = {row["filename"]: row["sha256"] for row in csv.DictReader(handle, delimiter="\t")}
    for path in (archive, metadata):
        canonical = "GSE283905_RAW.tar" if path == archive else "GSE283905_family.soft.gz"
        with path.open("rb") as source:
            assert hashlib.file_digest(source, "sha256").hexdigest() == fingerprints[canonical], canonical
    records = list(sample_counts(archive, sample_arms(metadata)))
    write_tsv(directory / "treated_per_sample.tsv", "sample arm gate cell_type gene cells depth gene_umis", records)
    write_tsv(directory / "treated_contrasts.tsv",
              "gate cell_type gene vehicle_n treated_n vehicle_mean_cpm treated_mean_cpm delta_log2p1 omit_min omit_max",
              contrasts(records))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("archive", type=Path)
    parser.add_argument("metadata", type=Path)
    args = parser.parse_args()
    main(args.output, args.archive, args.metadata)
