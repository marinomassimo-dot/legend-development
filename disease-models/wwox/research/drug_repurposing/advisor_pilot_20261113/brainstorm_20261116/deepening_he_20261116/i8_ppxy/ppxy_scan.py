#!/usr/bin/env python3
"""I8 (WWOX WW-domain / PPxY competition): proteome-scale PPxY scan of membrane channels, receptors and transporters.

    python3 ppxy_scan.py fetch --out <dir outside git>            public UniProt REST, generic client, no contact data; writes one TSV per taxon + MANIFEST.json
    python3 ppxy_scan.py scan  --raw <dir> --out <dir> [--seed 1] [--shuffles 2000]
    python3 ppxy_scan.py --help

Universe: reviewed UniProtKB entries of mouse (10090) and human (9606) that carry a transmembrane keyword AND at least one of ion channel, ion transport,
receptor, transport. Motifs: core PPxY (class I WW ligand; the PY motif NEDD4-family ligases read); relaxed LPxY (secondary tier). Region: UniProt
'Cytoplasmic' topological domains; an entry with no topology annotation is scored on every residue outside annotated transmembrane segments and is
labelled topology_unknown (never merged with the annotated tiers). Null: seeded within-protein shuffle of the cytoplasmic residues (composition and
segment lengths preserved), one-sided empirical p. Read-only on the network, zero spend. Mechanism-level only; not medical advice.
"""
import argparse, csv, gzip, hashlib, json, random, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

UA = "legend-ppxy-scan/1.0"
FIELDS = "accession,id,gene_primary,protein_name,length,keyword,ft_topo_dom,ft_transmem,sequence"
# Known gap: Cacna1g, Cacna1i and Abcc8 (matrix-class targets) have only UNREVIEWED mouse entries in this release, so the reviewed:true universe does not contain them.
QUERY = "(organism_id:{tax}) AND (reviewed:true) AND ((keyword:KW-0407) OR (keyword:KW-0406) OR (keyword:KW-0675) OR (keyword:KW-0813)) AND (keyword:KW-0812)"
TAXA = {"10090": "mouse", "9606": "human"}
CORE = re.compile(r"(?=(PP.Y))")
RELAX = re.compile(r"(?=(LP.Y))")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read(), dict(r.headers)


def fetch(out):
    out = Path(out); out.mkdir(parents=True, exist_ok=True); man = {"client": UA, "files": {}}
    for tax, name in TAXA.items():
        q = urllib.parse.urlencode({"query": QUERY.format(tax=tax), "format": "tsv", "fields": FIELDS, "compressed": "false"})
        body, h = get("https://rest.uniprot.org/uniprotkb/stream?" + q)
        p = out / f"uniprot_{name}_{tax}.tsv"; p.write_bytes(body)
        n = body.decode().count("\n") - 1
        man["files"][p.name] = {"sha256": hashlib.sha256(body).hexdigest(), "rows": n, "release": h.get("X-UniProt-Release"), "release_date": h.get("X-UniProt-Release-Date")}
        time.sleep(1)
    # WWOX domain boundaries (public feature table), to place P47T without memory
    q = urllib.parse.urlencode({"query": "gene_exact:WWOX AND reviewed:true AND (organism_id:10090 OR organism_id:9606)", "format": "tsv", "fields": "accession,organism_id,gene_primary,length,ft_domain,sequence"})
    body, h = get("https://rest.uniprot.org/uniprotkb/stream?" + q)
    p = out / "uniprot_wwox_domains.tsv"; p.write_bytes(body)
    man["files"][p.name] = {"sha256": hashlib.sha256(body).hexdigest(), "rows": body.decode().count("\n") - 1, "release": h.get("X-UniProt-Release"), "release_date": h.get("X-UniProt-Release-Date")}
    (out / "MANIFEST.json").write_text(json.dumps(man, indent=1, sort_keys=True) + "\n")
    print(json.dumps(man, indent=1, sort_keys=True))


def spans(text, tag):
    """[(a, b, note)] 1-based inclusive from a UniProt feature column like 'TOPO_DOM 1..129; /note="Cytoplasmic"; ... TOPO_DOM ...'."""
    out = []
    for m in re.finditer(tag + r" (\d+)(?:\.\.(\d+))?;(?: /note=\"([^\"]*)\")?", text or ""):
        a = int(m.group(1)); b = int(m.group(2) or a); out.append((a, b, m.group(3) or ""))
    return out


def regions(row):
    """(list of (start0, end0) cytoplasmic segments, topology label)."""
    L = int(row["Length"]); topo = spans(row["Topological domain"], "TOPO_DOM"); tm = spans(row["Transmembrane"], "TRANSMEM")
    cyt = [(a - 1, b) for a, b, n in topo if n.lower().startswith("cytoplasmic")]
    if topo:
        return cyt, "annotated"
    mask = [True] * L
    for a, b, _ in tm:
        for i in range(a - 1, min(b, L)): mask[i] = False
    segs, s = [], None
    for i, ok in enumerate(mask + [False]):
        if ok and s is None: s = i
        if not ok and s is not None: segs.append((s, i)); s = None
    return segs, "topology_unknown"


def find(seq, segs, rx):
    """[(0-based start, 4-mer)] of every overlapping motif inside the segments."""
    return [(a + m.start(), m.group(1)) for a, b in segs for m in rx.finditer(seq[a:b])]


def shuffle_p(seq, segs, obs, rx, rng, n):
    pool = [c for a, b in segs for c in seq[a:b]]; lens = [b - a for a, b in segs]; ge = 0
    for _ in range(n):
        rng.shuffle(pool); i = 0; k = 0
        for ln in lens:
            k += len(rx.findall("".join(pool[i:i + ln]))); i += ln
        if k >= obs: ge += 1
    return (1 + ge) / (n + 1)


def load(path):
    return list(csv.DictReader(open(path, encoding="utf-8"), delimiter="\t"))


def scan(raw, out, seed, shuffles):
    raw, out = Path(raw), Path(out); out.mkdir(parents=True, exist_ok=True)
    man = json.loads((raw / "MANIFEST.json").read_text())
    hits, genes = [], []
    seqs = {}
    for tax, name in TAXA.items():
        for row in load(raw / f"uniprot_{name}_{tax}.tsv"):
            seq = row["Sequence"]; segs, topo = regions(row); sym = row["Gene Names (primary)"] or row["Entry Name"]
            core = find(seq, segs, CORE); rel = find(seq, segs, RELAX)
            cyt_len = sum(b - a for a, b in segs)
            p = ""
            if core:
                p = round(shuffle_p(seq, segs, len(core), CORE, random.Random(f"{seed}:{row['Entry']}"), shuffles), 4)
            seqs[(name, row["Entry"])] = (sym, seq, segs)
            genes.append({"species": name, "accession": row["Entry"], "symbol": sym, "name": row["Protein names"].split(" (")[0], "length": row["Length"], "topology": topo, "cyt_residues": cyt_len,
                          "n_core_PPxY": len(core), "core_positions": ";".join(f"{i + 1}:{m}" for i, m in core), "n_LPxY": len(rel), "shuffle_p_core": p, "keywords": row["Keywords"]})
            for i, m in core:
                hits.append({"species": name, "accession": row["Entry"], "symbol": sym, "pos": i + 1, "motif": m, "topology": topo, "window_-4_+8": seq[max(0, i - 4):i + 8]})
    # conservation: a mouse core motif counts as conserved when the human ortholog (same symbol, upper case) has a core motif whose 12-mer window shares >= 7 identities
    hum = {g["symbol"].upper(): g for g in genes if g["species"] == "human"}
    hw = {}
    for h in hits:
        if h["species"] == "human": hw.setdefault(h["symbol"].upper(), []).append(h["window_-4_+8"])
    def ident(a, b): return sum(x == y for x, y in zip(a, b))
    for g in genes:
        if g["species"] != "mouse": g["human_ortholog_core"] = ""; continue
        mw = [h["window_-4_+8"] for h in hits if h["species"] == "mouse" and h["accession"] == g["accession"]]
        if g["symbol"].upper() not in hum: g["human_ortholog_core"] = "no_human_entry_in_universe"; continue
        hws = hw.get(g["symbol"].upper(), [])
        g["human_ortholog_core"] = "conserved" if any(ident(a, b) >= 7 for a in mw for b in hws) else ("human_has_core_other_window" if hws else "absent_in_human") if mw else ""
    cols = list(genes[0]); w = csv.DictWriter((out / "ppxy_genes.tsv").open("w", newline=""), cols, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(genes)
    cols = list(hits[0]); w = csv.DictWriter((out / "ppxy_motifs.tsv").open("w", newline=""), cols, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(hits)
    (out / "scan_run.json").write_text(json.dumps({"seed": seed, "shuffles": shuffles, "motif_core": "PP.Y", "motif_relaxed": "LP.Y", "inputs": {k: v["sha256"] for k, v in man["files"].items()}, "release": sorted({v["release"] for v in man["files"].values()}),
                                                "genes": len(genes), "genes_with_core": sum(1 for g in genes if g["n_core_PPxY"]), "motifs": len(hits)}, indent=1, sort_keys=True) + "\n")
    print(f"genes {len(genes)}; with core PPxY {sum(1 for g in genes if g['n_core_PPxY'])}; motif rows {len(hits)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    f = sub.add_parser("fetch"); f.add_argument("--out", required=True)
    s = sub.add_parser("scan"); s.add_argument("--raw", required=True); s.add_argument("--out", required=True); s.add_argument("--seed", type=int, default=1); s.add_argument("--shuffles", type=int, default=2000)
    a = ap.parse_args()
    if a.cmd == "fetch": fetch(a.out)
    elif a.cmd == "scan": scan(a.raw, a.out, a.seed, a.shuffles)
    else: ap.print_help()


if __name__ == "__main__":
    main()
