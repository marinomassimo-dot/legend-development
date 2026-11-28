"""Compare the MitoCarta respiratory subunit sets across held WWOX RNA profiles."""
import argparse
import csv
from hashlib import sha256
from pathlib import Path
import sys

import numpy as np

COMPLEXES = ("CI_subunits", "CII_subunits", "CIII_subunits", "CIV_subunits", "CV_subunits")
GMX_DIGESTS = {
    "Human": "789fa45a052ef1b905c297c230472f3cd03b83b2e4a2b808ce870dbbf04a2084",
    "Mouse": "45fe258b0c9506d2a987c486b0bf6e1c8bd81b1fd36e511f65cd973abe28907f",
}


def read_sets(source, species):
    path = source / f"{species}.MitoPathways3.0.gmx"
    if sha256(path.read_bytes()).hexdigest() != GMX_DIGESTS[species]:
        raise ValueError(f"Unexpected input {path}")
    with path.open() as handle:
        rows = csv.reader(handle, delimiter="\t")
        headings = next(rows)
        next(rows)
        cols = {key: headings.index(key) for key in COMPLEXES}
        selected = {key: set() for key in COMPLEXES}
        for row in rows:
            for key, index in cols.items():
                if index < len(row) and row[index].strip():
                    selected[key].add(row[index].strip())
    return {key: sorted(symbols) for key, symbols in selected.items()}


def matrix_rows(research, files, gmx):
    sys.path.insert(0, str(research / "continuous_compounds" / "copper_histidinate"))
    from replay_copper_comparison import MODELS, load_target, reference, verify

    manifest = research / "memantine_magnesium_20261123" / "inputs.tsv"
    with manifest.open() as handle:
        hashes = {row["input"]: row["sha256"] for row in csv.DictReader(handle, delimiter="\t")}
    verify(next((files / "reference_ensembl_r92").glob("*.fa.gz")), hashes)
    transcript_map, _ = reference(files)
    pathways = {species: read_sets(gmx, species) for species in GMX_DIGESTS}
    for accession, model, wt_start, ko_start, n_wt, n_ko in MODELS:
        human = accession == "GSE156243"
        species = "Human" if human else "Mouse"
        found = pathways[species]
        wanted = set().union(*found.values())
        pattern = "*count_table.txt.gz" if human else "*TPM_Table.txt.gz"
        path, = (files / "geo" / accession).glob(pattern)
        verify(path, hashes)
        samples, values = load_target(path, wanted, None if human else transcript_map)
        control = [i for i, sample in enumerate(samples) if sample.startswith(wt_start)]
        case = [i for i, sample in enumerate(samples) if sample.startswith(ko_start)]
        assert (len(control), len(case)) == (n_wt, n_ko)
        is_eligible = {gene for gene in wanted if gene in values
                       and np.count_nonzero(values[gene][control] > 0) * 2 >= n_wt}
        for panel in ("eligible", "nuclear_only"):
            groups = {key: [gene for gene in genes
                            if panel == "eligible" or not gene.upper().startswith("MT-")]
                      for key, genes in found.items()}
            used = {key: [gene for gene in genes if gene in is_eligible] for key, genes in groups.items()}
            scores = {key: np.mean([np.log2(1 + values[gene]) for gene in genes], axis=0)
                      for key, genes in used.items()}
            key = "CI_minus_mean_CII_to_CV"
            scores[key] = scores[COMPLEXES[0]] - np.mean([scores[c] for c in COMPLEXES[1:]], axis=0)
            for measure, score in scores.items():
                def difference(omit):
                    return float(score[[i for i in case if i != omit]].mean()
                                 - score[[i for i in control if i != omit]].mean())
                omitted = [difference(i) for i in case + control]
                numerator = len(used[measure]) if measure in used else sum(map(len, used.values()))
                denominator = len(groups[measure]) if measure in groups else sum(map(len, groups.values()))
                yield (accession, model, panel, measure, n_wt, n_ko, numerator, denominator,
                       difference(None), min(omitted), max(omitted))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("research", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("gmx", type=Path)
    args = parser.parse_args()
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(("accession", "preparation", "gene_panel", "measure", "WT_n", "KO_n",
                  "used", "annotated", "KO_minus_WT", "LOO_min", "LOO_max"))
    for row in matrix_rows(args.research, args.files, args.gmx):
        out.writerow([f"{value:.6f}" if isinstance(value, float) else value for value in row])


if __name__ == "__main__":
    main()
