#!/usr/bin/env python3
"""Per-gene centred log2 ratios for the subnetwork genes in the two human WWOX-loss transcript systems (stdlib only, deterministic).

Method = the iteration-5 same-set method, per gene (analyse_gse126075.py / p7_organoid_same_sets.py): log2((arm1 + 0.5) / (arm2 + 0.5)),
median-centred over the measurable universe (both arms at least 10 estimated tags or mean counts). No null model is computed here: these
are descriptive per-gene values, not differential-expression calls, and one CAGE library per arm is not a replicate.

Usage: derive_gene_values.py <GSE156243 counts.txt.gz> <GSE126075 gene TPM matrix.txt.gz> <genes.txt> <out.tsv>
       derive_gene_values.py --help
Reads nothing else; writes <out.tsv> and <out.tsv>.inputs.txt (input SHA-256 values, so the TSV keeps one header line). The inputs live outside the repository (files/geo/...).
Alias rule (HGNC alias/previous symbols present in a matrix, searched 2026-10-29): CAGE matrix PKM -> PKM2. SLC16A3, PDK4, MBP, MOG have no alias in the matrix; they stay absent.
"""
import sys, os, gzip, csv, hashlib, statistics, math

HELP = __doc__
CAGE_ALIAS = {"PKM": "PKM2"}
# Library sizes of the CAGE arms (tags): hNSC control recovered from the TSS table (51,007,825; see wwox_systems_comparison_it5 section 6),
# the others equal their BED line counts (bed_streamed_tagcounts_and_sha256.tsv).
NTAGS = {"hNSC": 51007825, "hNSC_WWOX_del": 14332108, "Neurons": 32686868, "Neurons_WWOX_del": 40730002}


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def centred(r, uni):
    med = statistics.median([r[i] for i in range(len(r)) if uni[i]])
    return [x - med for x in r], med


def main(argv):
    if len(argv) == 1 and argv[0] in ("-h", "--help"):
        print(HELP)
        return 0
    if len(argv) != 4:
        print(HELP, file=sys.stderr)
        return 2
    counts, cage, genefile, out = argv
    genes = [l.strip() for l in open(genefile) if l.strip() and not l.startswith("#")]
    rows = []

    # organoid: 4 knockout vs 2 wild-type libraries, counts -> cpm -> arm mean
    t = list(csv.reader(gzip.open(counts, "rt"), delimiter="\t"))
    assert t[0] == ["gene", "cko1", "cko2", "cko3", "cko4", "cwt1", "cwt2"], t[0]
    names = [r[0] for r in t[1:]]
    M = [[float(x) for x in r[1:]] for r in t[1:]]
    tot = [sum(M[i][j] for i in range(len(M))) for j in range(6)]
    ko = [sum(M[i][j] / tot[j] * 1e6 for j in range(4)) / 4 for i in range(len(M))]
    wt = [sum(M[i][j] / tot[j] * 1e6 for j in range(4, 6)) / 2 for i in range(len(M))]
    kc = [sum(M[i][:4]) / 4 for i in range(len(M))]
    wc = [sum(M[i][4:]) / 2 for i in range(len(M))]
    uni = [kc[i] >= 10 and wc[i] >= 10 for i in range(len(M))]
    R = [math.log2((ko[i] + .5) / (wt[i] + .5)) for i in range(len(M))]
    Rc, med = centred(R, uni)
    gi = {g: i for i, g in enumerate(names)}
    for g in genes:
        if g in gi:
            i = gi[g]
            rows.append((g, "organoid_ko_w15", str(bool(uni[i])), f"{Rc[i]:.3f}", f"{R[i]:.3f}", f"{kc[i]:.1f}", f"{wc[i]:.1f}", "mean_counts_ko_wt"))
        else:
            rows.append((g, "organoid_ko_w15", "False", "", "", "", "", "symbol_absent_from_counts_table"))

    # CAGE: one library per arm
    t = list(csv.reader(gzip.open(cage, "rt"), delimiter="\t"))
    arms = ["hNSC", "Neurons", "hNSC_WWOX_del", "Neurons_WWOX_del"]
    assert t[0] == ["Gene"] + arms, t[0]
    names = [r[0] for r in t[1:]]
    T = {a: [float(r[1 + k]) for r in t[1:]] for k, a in enumerate(arms)}
    gi = {g: i for i, g in enumerate(names)}
    for sysid, kd, ctl in (("hnpc_shwwox_cage", "hNSC_WWOX_del", "hNSC"), ("neuron_d14_shwwox_cage", "Neurons_WWOX_del", "Neurons")):
        tk = [x * NTAGS[kd] / 1e6 for x in T[kd]]
        tc = [x * NTAGS[ctl] / 1e6 for x in T[ctl]]
        uni = [tk[i] >= 10 and tc[i] >= 10 for i in range(len(names))]
        R = [math.log2((T[kd][i] + .5) / (T[ctl][i] + .5)) for i in range(len(names))]
        Rc, med = centred(R, uni)
        for g in genes:
            gg = g if g in gi else CAGE_ALIAS.get(g, g)
            if gg in gi:
                i = gi[gg]
                unit = "estimated_tags_kd_ctl" + ("" if gg == g else f";matrix_symbol={gg}")
                rows.append((g, sysid, str(bool(uni[i])), f"{Rc[i]:.3f}", f"{R[i]:.3f}", f"{tk[i]:.1f}", f"{tc[i]:.1f}", unit))
            else:
                rows.append((g, sysid, "False", "", "", "", "", "symbol_absent_from_matrix"))
    with open(out, "w", newline="") as f:
        f.write("gene\tsystem_id\tmeasurable\tR_centred\tR_uncentred\tsupport_kd\tsupport_ctl\tsupport_unit\n")
        for r in rows:
            f.write("\t".join(r) + "\n")
    with open(out + ".inputs.txt", "w") as f:
        f.write(f"counts\t{os.path.basename(counts)}\t{sha(counts)}\ncage\t{os.path.basename(cage)}\t{sha(cage)}\ngene_list\t{os.path.basename(genefile)}\t{sha(genefile)}\n")
    print(f"wrote {len(rows)} rows and {out}.inputs.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
