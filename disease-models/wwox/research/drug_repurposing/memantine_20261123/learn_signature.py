"""Learn an NMDA-versus-silencing expression contrast from paired preparations."""
import argparse
import csv
import gzip
from pathlib import Path
import re

import numpy as np


def write(path, fields, records):
    with path.open("w") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        writer.writerow(fields.split())
        for row in records:
            writer.writerow(f"{v:.6f}" if isinstance(v, (float, np.floating)) else v for v in row)


def study(counts, soft):
    metadata = {}
    with gzip.open(soft, "rt") as f:
        for line in f:
            if line.startswith("!Sample_title ="):
                sample, prep, treatment = re.fullmatch(r"!Sample_title = (\d+) \((\d+), (.+)\)\s*", line).groups()
                assert (int(prep), treatment) not in metadata
                metadata[int(prep), treatment] = sample
    with gzip.open(counts, "rt") as f:
        reader = csv.reader(f)
        samples = next(reader)[1:]
        genes, data = [], []
        for g, *values in reader:
            genes.append(g)
            data.append(values)
    assert len(set(genes)) == len(genes) and set(metadata.values()) == set(samples)
    x = np.asarray(data, dtype=float)
    cpm = 1e6*x/x.sum(axis=0)
    return genes, cpm, np.log2(1+cpm), {k: samples.index(v) for k,v in metadata.items()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("counts", "soft", "out"):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    args.out.mkdir(exist_ok=True, parents=True)
    genes, cpm, x, columns = study(args.counts, args.soft)
    train = [1, 3, 6]
    held = [7, 8]

    def values(condition, preparations, data=x):
        return data[:, [columns[p, condition] for p in preparations]]

    def change(a,b,preps=train):
        return values(a, preps) - values(b, preps)

    baseline = values("Control", train, cpm).mean(axis=1)
    induction = change("1h Bic", "Control")
    passive = change("1h Bic + 1h TTX", "2h Bic")
    active = change("1h Bic + 1h TTX & NMDA", "1h Bic + 1h TTX")
    eligible = (baseline>=1) & np.all(induction>0,axis=1) & (induction.mean(axis=1)>=0.5)
    hit_set = np.flatnonzero(eligible & np.all(active<0,axis=1))
    hits = sorted(hit_set, key=lambda g: (active[g].mean(), genes[g]))[:20]
    pool = set(np.flatnonzero(eligible & (abs(active.mean(axis=1))<=0.15))) - set(hits)
    features = np.column_stack([np.log2(1+baseline),induction.mean(axis=1),passive.mean(axis=1)])
    scale = features[eligible].std(axis=0)
    assert np.all(scale>0)
    # Preserve the eligible comparator set for the matching-order sensitivity.
    write(args.out/"candidate_pool.tsv", "ensembl basal_logCPM induction passive NMDA_added",
          [(genes[g], *features[g], active[g].mean()) for g in sorted(pool,key=lambda i:genes[i])])
    pairs = []
    for h in hits:
        if not pool:
            break
        def distance(c):
            return np.linalg.norm((features[h]-features[c])/scale)
        c = min(pool,key=lambda g:(distance(g),genes[g]))
        pairs.append((h,c))
        pool.remove(c)
    roster = []
    for i,(h,c) in enumerate(pairs,1):
        for role,g in (("hit",h),("control",c)):
            roster.append([i,role,genes[g],*features[g],active[g].mean()])
    write(args.out/"pairs.tsv","pair arm ensembl basal_logCPM induction passive NMDA_added",roster)
    write(args.out/"matching.tsv", "covariate eligible_sd hit_mean control_mean mean_gap_in_sd",
          [(n,scale[i],np.mean([features[h,i] for h,c in pairs]), np.mean([features[c,i] for h,c in pairs]),
            np.mean([(features[h,i]-features[c,i])/scale[i] for h,c in pairs]))
           for i,n in enumerate(["basal_logCPM","induction","passive"])])
    h,c = map(list,zip(*pairs))
    rows = []
    for label,a,b in [
        ("NMDA_at_1h","1h Bic + 1h TTX & NMDA","1h Bic + 1h TTX"),
        ("NMDA_at_30min","0.5h Bic + 0.5h TTX & NMDA","0.5h Bic + 0.5h TTX"),
        ("TBOA_at_1h","1h Bic + 1h TBOA","2h Bic"),
        ("induction","1h Bic","Control"),
        ("passive","1h Bic + 1h TTX","2h Bic"),
    ]:
        for prep in train+held:
            delta = change(a,b,[prep])[:,0]
            rows.append([label,prep,"training" if prep in train else "held_out",len(pairs),
                         delta[h].mean(), delta[c].mean(), np.mean(delta[h]-delta[c])])
    write(args.out/"validation.tsv","contrast preparation partition pairs hit control hit_minus_control",rows)
    write(args.out/"selection.tsv", "expressed_induced consistent_negative chosen_pairs",
          [[int(eligible.sum()),len(hit_set),len(pairs)]])


if __name__ == "__main__":
    main()
