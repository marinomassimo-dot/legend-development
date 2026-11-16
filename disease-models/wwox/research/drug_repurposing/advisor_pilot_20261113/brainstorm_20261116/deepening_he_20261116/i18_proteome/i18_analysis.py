#!/usr/bin/env python3
"""I18 analysis, exactly as PREREGISTRATION.md fixes it. Run only after the preregistration is committed.

    python3 i18_analysis.py fetch   --table <parsed TSV outside git> --out <dir outside git>          (UniProt public REST, generic client)
    python3 i18_analysis.py analyse --table <parsed TSV> --seqs <dir with uniprot_sequences.tsv> --prereg PREREGISTRATION.md --out <results dir in git>
    python3 i18_analysis.py --help

The per-protein fold changes of the third-party table stay outside git; the results folder holds aggregates, strata, counts and the carrier lists (accession, symbol, motif positions) only.
Seeds: permutation and bootstrap seed 1 (numpy default_rng); 10,000 permutations, 5,000 bootstrap draws. Not medical advice.
"""
import argparse, csv, hashlib, importlib.util, json, re, sys, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
sub = ap.add_subparsers(dest="cmd")
f = sub.add_parser("fetch"); f.add_argument("--table", required=True); f.add_argument("--out", required=True)
s = sub.add_parser("analyse"); s.add_argument("--table", required=True); s.add_argument("--seqs", required=True); s.add_argument("--prereg", required=True); s.add_argument("--out", required=True)
a = ap.parse_args()
if not a.cmd:
    ap.print_help(); sys.exit(0)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
FIELDS = "accession,gene_primary,length,ft_topo_dom,ft_transmem,sequence"
UA = "legend-ppxy-scan/1.0"

def fetch():
    acc = [r["uniprot"] for r in csv.DictReader(open(a.table), delimiter="\t")]
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True); lines = []; hdr = None
    cache = out / "batches"; cache.mkdir(exist_ok=True)
    for i in range(0, len(acc), 40):
        cf = cache / f"b{i:05d}.tsv"
        if not cf.exists():
            q = "(" + " OR ".join(f"accession:{x}" for x in acc[i:i + 40]) + ")"
            url = "https://rest.uniprot.org/uniprotkb/stream?" + urllib.parse.urlencode({"query": q, "format": "tsv", "fields": FIELDS})
            for attempt in range(8):                                   # a 429 is a rate limit: wait as the server says (default 60 s), never hammer
                try:
                    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=120) as r:
                        cf.write_text(r.read().decode()); break
                except urllib.error.HTTPError as e:
                    if e.code != 429: raise
                    time.sleep(int(e.headers.get("Retry-After", "60")) + 5)
            else:
                sys.exit("REFUSED: rate-limited eight times; stop and try later")
            time.sleep(4)
        t = cf.read_text().splitlines(); hdr = hdr or t[0]; lines += t[1:]
    (out / "uniprot_sequences.tsv").write_text(hdr + "\n" + "\n".join(lines) + "\n")
    (out / "MANIFEST.json").write_text(json.dumps({"table_sha256": sha(a.table), "sequences_sha256": sha(out / "uniprot_sequences.tsv"), "rows": len(lines), "accessions_requested": len(acc)}, indent=1, sort_keys=True) + "\n")
    print((out / "MANIFEST.json").read_text())

def analyse():
    import numpy as np
    spec = importlib.util.spec_from_file_location("ppxy_scan", Path(__file__).resolve().parent.parent / "i8_ppxy/ppxy_scan.py"); sc = importlib.util.module_from_spec(spec); sys.argv = ["x"]; spec.loader.exec_module(sc)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    tab = list(csv.DictReader(open(a.table), delimiter="\t"))
    seq = {}
    for r in csv.DictReader(open(Path(a.seqs) / "uniprot_sequences.tsv"), delimiter="\t"): seq[r["Entry"]] = r
    rx = {"P": re.compile(r"(?=(PP.Y))"), "T": re.compile(r"(?=(LP.Y))"), "F": re.compile(r"(?=(PP.F))"), "A": re.compile(r"(?=(PP.A))")}
    prot = []
    for r in tab:
        u = r["uniprot"]
        if r["log2_int_control"] == "NA" or r["log2_int_silenced"] == "NA" or u not in seq: continue
        e = seq[u]; row = {"Length": e["Length"], "Topological domain": e["Topological domain"], "Transmembrane": e["Transmembrane"]}
        segs, topo = sc.regions(row); s_ = e["Sequence"]
        hits = {k: len(sc.find(s_, segs, v)) for k, v in rx.items()}; anyp = len(re.findall(r"(?=PP.Y)", s_))
        prot.append({"u": u, "sym": r["symbol"], "lfc": float(r["log2fc"]), "p": (float(r["bh_adj_p"]) if r["bh_adj_p"] != "NA" else 1.0), "int": (float(r["log2_int_control"]) + float(r["log2_int_silenced"])) / 2,
                     "mem": "membrane" if "TRANSMEM" in e["Transmembrane"] else "soluble", "topo": topo, "P": hits["P"], "S": anyp, "T": hits["T"], "F": hits["F"], "A": hits["A"]})
    n_all = len(prot); dropped = len(tab) - n_all
    ints = np.array([p["int"] for p in prot]); edges = np.quantile(ints, np.linspace(0, 1, 11)[1:-1])
    for p in prot: p["dec"] = int(np.searchsorted(edges, p["int"]))
    clean = lambda p: p["P"] == 0 and p["S"] == 0 and p["T"] == 0 and p["F"] == 0 and p["A"] == 0
    SETS = {"P_primary": lambda p: p["P"] > 0, "S_secondary_anywhere": lambda p: p["S"] > 0, "T_LPxY_only": lambda p: p["T"] > 0 and p["P"] == 0 and p["S"] == 0,
            "decoy_PPxF": lambda p: p["F"] > 0 and p["P"] == 0 and p["S"] == 0, "decoy_PPxA": lambda p: p["A"] > 0 and p["P"] == 0 and p["S"] == 0}
    rng = np.random.default_rng(1); res = []; strata_rows = []
    def strata_of(sel, pool):
        st = {}
        for p in pool:
            k = (p["dec"], p["mem"]); st.setdefault(k, ([], []))
            if sel(p): st[k][0].append(p["lfc"])
            elif clean(p): st[k][1].append(p["lfc"])
        used = {k: (np.array(c), np.array(n)) for k, (c, n) in st.items() if len(c) >= 3 and len(n) >= 3}
        return used, len(st) - len(used)
    def D_of(used, perm=False, boot=False):
        num = den = 0.0
        for k, (c, n) in used.items():
            if perm:
                allv = np.concatenate([c, n]); rng.shuffle(allv); c2, n2 = allv[:len(c)], allv[len(c):]
            elif boot:
                c2, n2 = rng.choice(c, len(c)), rng.choice(n, len(n))
            else:
                c2, n2 = c, n
            num += len(c) * (np.median(c2) - np.median(n2)); den += len(c)
        return num / den if den else float("nan")
    def run(name, sel, pool, label=None):
        used, dropped_s = strata_of(sel, pool); ncar = sum(len(c) for c, _ in used.values()); nnon = sum(len(n) for _, n in used.values())
        D = D_of(used); perm = np.array([D_of(used, perm=True) for _ in range(10000)]); p = (1 + np.sum(np.abs(perm) >= abs(D))) / (len(perm) + 1)
        bs = np.array([D_of(used, boot=True) for _ in range(5000)]); lo, hi = np.percentile(bs, [2.5, 97.5])
        res.append([label or name, ncar, nnon, len(used), dropped_s, f"{D:+.4f}", f"{p:.4f}", f"{lo:+.4f}", f"{hi:+.4f}"])
        if (label or name) == "P_primary":
            for k, (c, n) in sorted(used.items()): strata_rows.append([k[0], k[1], len(c), len(n), f"{np.median(c):+.3f}", f"{np.median(n):+.3f}"])
        return D, p, lo, hi
    out_res = {}
    for name, sel in SETS.items(): out_res[name] = run(name, sel, prot)
    cut = np.quantile(ints, 0.95); run("P_primary", SETS["P_primary"], [p for p in prot if p["int"] < cut], label="P_primary_without_top5pct_intensity")
    for comp in ("membrane", "soluble"):                                  # POST HOC, not in the preregistration: labelled as such in the set name; appended after the preregistered runs so their random streams are unchanged
        run("P_primary", SETS["P_primary"], [p for p in prot if p["mem"] == comp], label=f"POSTHOC_P_primary_{comp}_only")
    cars = [p for p in prot if SETS["P_primary"](p)]
    up = lambda g: sum(1 for p in g if p["p"] < 0.05 and p["lfc"] > 0); dn = lambda g: sum(1 for p in g if p["p"] < 0.05 and p["lfc"] < 0)
    non = [p for p in prot if clean(p)]
    with open(out / "results_summary.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["set", "carriers_used", "non_carriers_used", "strata_used", "strata_dropped", "D_log2", "perm_p_two_sided", "boot95_lo", "boot95_hi"]); w.writerows(res)
    with open(out / "strata_primary.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["intensity_decile", "compartment", "carriers", "non_carriers", "median_lfc_carriers", "median_lfc_non_carriers"]); w.writerows(strata_rows)
    with open(out / "carriers_primary.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["uniprot", "symbol", "compartment", "topology", "n_PPxY_in_region"]); [w.writerow([p["u"], p["sym"], p["mem"], p["topo"], p["P"]]) for p in sorted(cars, key=lambda x: x["sym"])]
    D, p, lo, hi = out_res["P_primary"]; dec = [abs(out_res["decoy_PPxF"][0]), abs(out_res["decoy_PPxA"][0])]
    if hi < 0.05 and lo > -0.05: verdict = "KILL (for this table): the 95% interval lies inside (-0.05, +0.05)"
    elif D <= -0.05 and p < 0.05 and max(dec) < 0.5 * abs(D): verdict = "SUPPORT M- (shield: carriers fall)"
    elif D >= 0.05 and p < 0.05 and max(dec) < 0.5 * abs(D): verdict = "SUPPORT M+ (adaptor: carriers rise)"
    else: verdict = "INCONCLUSIVE"
    note = [f"verdict by the preregistered rule: {verdict}", f"proteins analysed {n_all} of {len(tab)} rows (dropped: no sequence or NA intensity: {dropped})", f"carriers P in the whole table {len(cars)}; clean non-carriers {len(non)}",
            f"BH<0.05 share, carriers: up {up(cars)}, down {dn(cars)} of {len(cars)}; non-carriers: up {up(non)}, down {dn(non)} of {len(non)}",
            f"inputs: table {sha(a.table)}; sequences {sha(Path(a.seqs) / 'uniprot_sequences.tsv')}; preregistration {sha(a.prereg)}"]
    (out / "run_note.txt").write_text("\n".join(note) + "\n"); print("\n".join(note)); print(open(out / "results_summary.tsv").read())

fetch() if a.cmd == "fetch" else analyse()
