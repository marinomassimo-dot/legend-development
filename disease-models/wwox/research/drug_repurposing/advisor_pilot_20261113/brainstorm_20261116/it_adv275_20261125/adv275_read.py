"""ADV-275 step 3: WWOX and sentinel values in deposited neural HDAC-inhibitor series.

Usage: python3 -I adv275_read.py <data_dir> <out_dir>
Reading rules are those of PREREG_ADV275_IT_20261125.md section 3. Standard library only.
"""
import collections
import csv
import gzip
import io
import json
import math
import pathlib
import re
import sys
import tarfile
import zipfile
import xml.etree.ElementTree as ET

D = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2])
csv.field_size_limit(10 ** 9)

GENES = ("WWOX", "H1F0", "CDKN1A")
SYMBOLS = {"wwox": "WWOX", "h1-0": "H1F0", "h1f0": "H1F0", "cdkn1a": "CDKN1A"}
ENTREZ = {"51741": "WWOX", "3005": "H1F0", "1026": "CDKN1A", "80707": "WWOX", "14958": "H1F0", "12575": "CDKN1A"}
ENSEMBL = {"ENSG00000186153": "WWOX", "ENSG00000189060": "H1F0", "ENSG00000124762": "CDKN1A",
           "ENSMUSG00000004637": "WWOX", "ENSMUSG00000096210": "H1F0", "ENSMUSG00000023067": "CDKN1A"}


def gene_of(token):
    t = str(token).strip().strip('"')
    base = t.split(".")[0]
    if base in ENSEMBL:
        return ENSEMBL[base]
    return SYMBOLS.get(t.lower())


# ---------------------------------------------------------------- statistics
def betacf(a, b, x):
    qab, qap, qam = a + b, a + 1, a - 1
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) > 1e-300 else 1e-300)
    h = d
    for m in range(1, 400):
        m2 = 2 * m
        for aa in (m * (b - m) * x / ((qam + m2) * (a + m2)),
                   -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))):
            d = 1.0 + aa * d
            d = 1.0 / (d if abs(d) > 1e-300 else 1e-300)
            c = 1.0 + aa / c
            c = c if abs(c) > 1e-300 else 1e-300
            h *= d * c
        if abs(d * c - 1) < 1e-12:
            break
    return h


def betai(a, b, x):
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    bt = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1 - x))
    if x < (a + 1) / (a + b + 2):
        return bt * betacf(a, b, x) / a
    return 1 - bt * betacf(b, a, 1 - x) / b


def welch(x, y):
    nx, ny = len(x), len(y)
    if nx < 2 or ny < 2:
        return None
    mx, my = sum(x) / nx, sum(y) / ny
    vx = sum((v - mx) ** 2 for v in x) / (nx - 1)
    vy = sum((v - my) ** 2 for v in y) / (ny - 1)
    se2 = vx / nx + vy / ny
    if se2 == 0:
        return 1.0 if mx == my else 0.0
    t = (mx - my) / math.sqrt(se2)
    df = se2 ** 2 / ((vx / nx) ** 2 / (nx - 1) + (vy / ny) ** 2 / (ny - 1))
    return betai(df / 2, 0.5, df / (df + t * t))


# ---------------------------------------------------------------- loaders
# every loader returns (kind, {sample_name: {row_id: value}} restricted to GENES, extra)
def series_meta_and_table(path, want_rows):
    meta, rows, header, intable = collections.defaultdict(list), {}, None, False
    sample_q = []
    with gzip.open(path, "rt", errors="replace") as f:
        for line in f:
            if line.startswith("!series_matrix_table_begin"):
                intable = True
                continue
            if line.startswith("!series_matrix_table_end"):
                break
            if intable:
                p = line.rstrip("\n").split("\t")
                if header is None:
                    header = [x.strip('"') for x in p[1:]]
                    continue
                vals = []
                for v in p[1:]:
                    try:
                        vals.append(float(v.strip('"')))
                    except ValueError:
                        vals.append(float("nan"))
                rows[p[0].strip('"')] = vals
            elif line.startswith("!Sample_"):
                p = line.rstrip("\n").split("\t")
                meta[p[0][8:]].append([x.strip('"') for x in p[1:]])
    return meta, header, rows


def platform_probes(gpl):
    probes = {}
    annot = D / f"{gpl}.annot.gz"
    table = D / f"{gpl}.table.txt"
    if gpl == "GPL15798":
        return {f"{k}_at": v for k, v in ENTREZ.items()}
    if annot.exists():
        with gzip.open(annot, "rt", errors="replace") as f:
            col = None
            for line in f:
                p = line.rstrip("\n").split("\t")
                if col is None:
                    if p[0] == "ID" and "Gene symbol" in p:
                        col = p.index("Gene symbol")
                    continue
                if len(p) > col:
                    parts = p[col].split("///")
                    for s in parts:
                        g = gene_of(s)
                        if g:
                            probes[p[0]] = g + ("" if len(parts) == 1 else "(multi)")
        return probes
    with open(table, errors="replace") as f:
        header = None
        for line in f:
            p = line.rstrip("\n").split("\t")
            if header is None:
                if p[0] == "ID":
                    header = p
                continue
            row = dict(zip(header, p))
            symbols = []
            if "GENE_SYMBOL" in row:
                symbols = [row["GENE_SYMBOL"]]
            elif "gene_assignment" in row:
                symbols = [a.split("//")[1].strip() for a in row["gene_assignment"].split("///") if "//" in a]
            for s in set(symbols):
                g = gene_of(s)
                if g:
                    probes[p[0]] = g
    return probes


def load_array(acc, gpl):
    path = D / f"{acc}_series_matrix.txt.gz"
    if not path.exists():
        path = D / f"{acc}-{gpl}_series_matrix.txt.gz"
    meta, header, rows = series_meta_and_table(path, None)
    probes = platform_probes(gpl)
    gsm = meta["geo_accession"][0]
    titles = dict(zip(gsm, meta["title"][0]))
    finite = [v for r in list(rows.values())[:5000] for v in r if v == v]
    logged = max(finite) < 100
    # per-array 25th percentile on the deposited scale
    columns = list(zip(*rows.values()))
    q25 = []
    for col in columns:
        s = sorted(v for v in col if v == v)
        q25.append(s[len(s) // 4])
    data, low = {}, {}
    for i, g in enumerate(header):
        name = titles[g]
        data[name] = {}
        for pid, gene in probes.items():
            if pid in rows:
                v = rows[pid][i]
                if v != v:
                    continue
                if not logged:
                    v = math.log2(max(v, 1.0))
                data[name][(gene, pid)] = v
                low.setdefault((gene, pid), []).append(rows[pid][i] < q25[i])
    background = {k: sum(v) / len(v) > 0.5 for k, v in low.items()}
    return data, background


def counts_to_data(samples, table, library=None):
    """table: {gene_id: [counts]}; rows for the three genes -> log2(CPM) data."""
    n = len(samples)
    totals = library or [sum(r[i] for r in table.values()) for i in range(n)]
    data = {s: {} for s in samples}
    raw = {}
    for gid, row in table.items():
        gene = gid[1]
        if gene is None:
            continue
        for i, s in enumerate(samples):
            cpm = row[i] / totals[i] * 1e6
            data[s][(gene, gid[0])] = math.log2(cpm + 0.05)
        raw[(gene, gid[0])] = row
    return data, raw


def delimited(text, sep, id_col, sample_cols=None, gene_col=None, entrez=False):
    reader = csv.reader(io.StringIO(text), delimiter=sep)
    header = next(reader)
    first = next(reader)
    if len(first) == len(header) + 1:
        header = ["id"] + header
    idx = sample_cols(header) if callable(sample_cols) else list(range(1, len(header)))
    samples = [header[i] for i in idx]
    table = {}
    for p in [first, *reader]:
        if len(p) <= max(idx):
            continue
        key = p[id_col]
        if entrez:
            gene = ENTREZ.get(key)
        else:
            gene = gene_of(p[gene_col]) if gene_col is not None else gene_of(key)
        try:
            row = [float(p[i] or 0) for i in idx]
        except ValueError:
            continue
        table[(key, gene)] = row
    return samples, table


def gz(name):
    return gzip.open(D / name, "rt", errors="replace").read()


def load_ncbi(acc):
    path = next(D.glob(f"{acc}_raw_counts_*NCBI.tsv.gz"))
    samples, table = delimited(gzip.open(path, "rt").read(), "\t", 0, entrez=True)
    meta, _, _ = series_meta_and_table(next(iter(sorted(D.glob(f"{acc}[_-]*series_matrix.txt.gz")))), None)
    titles = {}
    for p in sorted(D.glob(f"{acc}[_-]*series_matrix.txt.gz")):
        m, _, _ = series_meta_and_table(p, None)
        titles.update(dict(zip(m["geo_accession"][0], m["title"][0])))
    data, raw = counts_to_data(samples, table)
    return {titles.get(s, s): v for s, v in data.items()}, ([titles.get(s, s) for s in samples], raw)


def load_tar(acc, count_col=-1):
    tables, samples = {}, []
    with tarfile.open(D / f"{acc}_RAW.tar") as tar:
        members = sorted(m.name for m in tar.getmembers() if m.isfile())
        per = []
        for name in members:
            text = gzip.decompress(tar.extractfile(name).read()).decode("utf8", "replace")
            counts = {}
            for line in text.splitlines():
                p = line.split("\t") if "\t" in line else line.split()
                if len(p) < 2 or p[0].startswith("__") or p[0].startswith("N_"):
                    continue
                try:
                    counts[p[0]] = float(p[count_col])
                except ValueError:
                    continue
            per.append(counts)
            samples.append(re.sub(r"\.txt\.gz$|\.gz$", "", name))
    ids = set().union(*per)
    table = {(g, gene_of(g)): [c.get(g, 0.0) for c in per] for g in ids}
    data, raw = counts_to_data(samples, table)
    return data, (samples, raw)


def load_delim(name, sep, id_col=0, gene_col=None, cols=None):
    samples, table = delimited(gz(name), sep, id_col, cols, gene_col)
    data, raw = counts_to_data(samples, table)
    return data, (samples, raw)


def load_log_matrix(name, sep, drop=1):
    """already log-scale or normalised values: used as deposited (linear = 2^x if logged)."""
    samples, table = delimited(gz(name), sep, 0)
    values = [v for r in list(table.values())[:3000] for v in r]
    logged = max(values) < 40
    data = {s: {} for s in samples}
    for (key, gene), row in table.items():
        if gene:
            for i, s in enumerate(samples):
                data[s][(gene, key)] = row[i] if logged else math.log2(row[i] + 0.05)
    return data, (samples, {})


def xlsx_rows(path):
    ns = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
    with zipfile.ZipFile(path) as z:
        shared = []
        if "xl/sharedStrings.xml" in z.namelist():
            for si in ET.fromstring(z.read("xl/sharedStrings.xml")).iter(ns + "si"):
                shared.append("".join(t.text or "" for t in si.iter(ns + "t")))
        sheet = sorted(n for n in z.namelist() if n.startswith("xl/worksheets/sheet"))[0]
        for row in ET.fromstring(z.read(sheet)).iter(ns + "row"):
            cells = {}
            for c in row.findall(ns + "c"):
                col = re.match(r"[A-Z]+", c.get("r")).group()
                n = 0
                for ch in col:
                    n = n * 26 + ord(ch) - 64
                v = c.find(ns + "v")
                if v is None:
                    continue
                cells[n - 1] = shared[int(v.text)] if c.get("t") == "s" else v.text
            yield [cells.get(i, "") for i in range(max(cells) + 1)] if cells else []


def load_xlsx_counts(name):
    rows = xlsx_rows(D / name)
    header = next(rows)
    body = list(rows)

    def numeric(i):
        try:
            [float(r[i]) for r in body[:50]]
            return True
        except (ValueError, IndexError):
            return False

    idx = [i for i in range(len(header)) if numeric(i) and re.search(r"ctrl|vpa|chi|tha", str(header[i]), re.I)]
    samples = [header[i] for i in idx]
    table = {}
    for r in body:
        gene = None
        for i in range(len(r)):
            if i not in idx and gene_of(r[i]):
                gene = gene_of(r[i])
        try:
            table[(r[0], gene)] = [float(r[i]) for i in idx]
        except (ValueError, IndexError):
            continue
    data, raw = counts_to_data(samples, table)
    return data, (samples, raw)


def load_renc():
    want_samples = {}
    m, _, _ = series_meta_and_table(D / "GSE164788_series_matrix.txt.gz", None)
    titles = m["title"][0]
    for t in titles:
        want_samples[t.split()[0]] = t
    totals = collections.Counter()
    rows = collections.defaultdict(dict)
    with gzip.open(D / "GSE164788_deduplicated_counts.csv.gz", "rt") as f:
        next(f)
        for line in f:
            p = line.rstrip("\n").replace('"', "").split("\t" if "\t" in line else ",")
            sample, gid, count = p[0], p[1], float(p[2])
            totals[sample] += count
            gene = gene_of(gid)
            if gene:
                rows[(gid, gene)][sample] = count
    samples = [s for s in totals if s in want_samples]
    table = {k: [v.get(s, 0.0) for s in samples] for k, v in rows.items()}
    data, raw = counts_to_data(samples, table, [totals[s] for s in samples])
    names = [want_samples[s] for s in samples]
    return {want_samples[s]: data[s] for s in samples}, (names, raw)


def load_sheet(matrix, sheet):
    """deposited log2 normalised FPKM; arm names come from the deposited sample sheet."""
    meta = list(csv.DictReader(io.StringIO(gz(sheet)), delimiter="\t"))
    names = {m["SampleName"]: f"{m['treatment'].strip()}|{m['Virus']}|{m['Label']}|{m['SampleName']}" for m in meta}
    samples, table = delimited(gz(matrix), "\t", 0)
    data = {names[s]: {} for s in samples}
    for (key, gene), row in table.items():
        if gene:
            for i, s in enumerate(samples):
                data[names[s]][(gene, key)] = row[i]
    return data, (list(data), {})


def load_log2_symbol(name):
    samples, table = delimited(gz(name), ",", 0)
    data = {s: {} for s in samples}
    for (key, gene), row in table.items():
        if gene:
            for i, s in enumerate(samples):
                data[s][(gene, key)] = row[i]
    return data, (samples, {})


def load_cpm328496():
    lines = gz("GSE328496_normalized_counts_batch_CPM.txt.gz").splitlines()
    samples = lines[0].split()[2:]
    data = {s: {} for s in samples}
    for line in lines[1:]:
        p = line.split()
        gene = gene_of(p[0])
        if gene:
            for s, v in zip(samples, p[2:]):
                data[s][(gene, p[0])] = math.log2(max(float(v), 0) + 0.05)
    return data, (samples, {})


# ---------------------------------------------------------------- contrasts
def C(acc, load, system, species, exposure, control, treated, tier="A", family="independent"):
    return dict(acc=acc, load=load, system=system, species=species, exposure=exposure, control=control,
                treated=treated, tier=tier, family=family)


def arr(acc, gpl):
    return ("array", acc, gpl)


KON, UKK = "platform A family (Konstanz)", "platform A family (Cologne)"
SPEC = []
for dose in ("0.33 mM", "1 mM"):
    for day in ("1 days", "7 days"):
        SPEC.append(C("GSE64123", arr("GSE64123", "GPL15798"), "hESC embryoid-body neuroectoderm (ESNATS UKK)", "human",
                      f"VPA {dose}, {day}", rf"^{day}, DMSO|^{day}, unexposed", rf"^{day}, valproic acid {dose}",
                      family=UKK))
SPEC += [
    C("GSE129241", ("ncbi", "GSE129241"), "NGN2 induced neurons (hESC)", "human", "VPA, added day 1, 72-96 h",
      r"^Ctrl day1[ _-]", r"^VPA day1[ _-]"),
    C("GSE129241", ("ncbi", "GSE129241"), "NGN2 induced neurons (hESC)", "human", "VPA, added day 21, 72-96 h",
      r"^Ctrl day21", r"^VPA day21"),
    C("GSE129241", ("ncbi", "GSE129241"), "NGN2 induced neurons (hESC)", "human", "VPA, added day 50-56, 72-96 h",
      r"^Ctrl day50", r"^VPA day50"),
    C("GSE232218", ("ncbi", "GSE232218"), "iPSC brain organoids day 6", "human", "VPA 200 uM", r"Vehicle", r"VPA200"),
    C("GSE232218", ("ncbi", "GSE232218"), "iPSC brain organoids day 6", "human", "VPA 400 uM", r"Vehicle", r"VPA400"),
    C("GSE241903", ("ncbi", "GSE241903"), "iPSC spinal cord organoids", "human", "VPA, 96 h", r"FGF", r"VPA \d|VPA[_ ]rep|organoids, VPA(?![+])"),
    C("GSE305320", ("xlsx", "GSE305320_counts_final_drug.xlsx"), "hESC posterior spinal-cord organoids (hPCO)", "human",
      "VPA", r"ctrl", r"vpa"),
    C("GSE214885", ("tar", "GSE214885"), "MECP2-null hESC neurons/organoids, day 8", "human", "VPA", r"M8-DM", r"M8-VPA"),
    C("GSE214885", ("tar", "GSE214885"), "MECP2-null hESC neurons/organoids, day 20", "human", "VPA", r"M20-DM", r"M20-VPA"),
    C("GSE157676", ("ncbi", "GSE157676"), "NPC1-mutant iNSC brain organoids, 4 weeks", "human", "VPA from day 21",
      r"NPC(?!.*VPA)", r"VPA"),
    C("GSE256142", ("delim", "GSE256142_ImPheNet_counts_1_v2.csv.gz", ";"), "iPSC brain organoids d90 (control line)",
      "human", "VPA", r"^CTL_iPSC_d90_n", r"^CTL_iPSC_d90_VPA"),
    C("GSE256142", ("delim", "GSE256142_ImPheNet_counts_1_v2.csv.gz", ";"), "iPSC brain organoids d90 (Dravet line)",
      "human", "VPA", r"^DS_iPSC_d90_n", r"^DS_iPSC_d90_VPA"),
    C("GSE222509", ("ncbi", "GSE222509"), "iPSC neurons day 64", "human", "VPA 200 ug/ml, 24 h", r"vehicle", r"VPA"),
    C("GSE302545", ("delim", "GSE302545_counts_matrix_GEO.csv.gz", ","), "iPSC cortical neurons", "human",
      "TSA 60 ng/ml, 24 h", r"^FGM_Control", r"^TSA_well"),
    C("GSE290300", ("log", "GSE290300_raw_counts_all_samples.csv.gz", ","), "hESC (cell type as deposited: hESC)", "human",
      "VPA 300 uM", r"CONTROL", r"VPA300", tier="not neural as deposited"),
    C("GSE166297", ("ncbi", "GSE166297"), "ESC-derived neural progenitors / neuron-astrocyte co-culture", "human",
      "VPA IC5", r"__control__", r"Valproic_acid_IC5"),
    C("GSE166297", ("ncbi", "GSE166297"), "ESC-derived neural progenitors / neuron-astrocyte co-culture", "human",
      "VPA IC20", r"__control__", r"Valproic_acid_IC20"),
    C("GSE46043", arr("GSE46043", "GPL17077"), "iPSC-derived neurons (uninfected)", "human", "sodium butyrate",
      r"uninfected(?!.*(NaB|BVdU))", r"uninfected \+ NaB"),
]
for compound, dose in (("vorinostat", "10 uM"), ("vorinostat", "1 uM"), ("belinostat", "10 uM"),
                       ("belinostat", "1 uM"), ("entinostat", "10 uM"), ("entinostat", "1 uM")):
    plate = "dge1" if compound == "entinostat" else "dge2"
    SPEC.append(C("GSE164788", ("renc",), "ReNcell VM neural cells (v-myc immortalised progenitor line)", "human",
                  f"{compound} {dose}", rf"^{plate}_\S+ .*treated with .*dmso",
                  rf"^{plate}_\S+ .*treated with {dose} {compound}"))
SPEC += [
    C("GSE197966", ("ncbi", "GSE197966"), "NT2-N neuron-like cells (teratocarcinoma origin)", "human", "VPA",
      r"H2O vehicle", r"Valproate", tier="B"),
    C("GSE147270", arr("GSE147270", "GPL570"), "UKN1 hESC neuroectoderm (H9), 6 days", "human", "VPA 0.6 mM", r"__ukn1ctl__",
      r"__ukn1vpa__", family=KON),
    # mouse
    C("GSE17735", arr("GSE17735", "GPL6885"), "frontal cortex, wild type, chronic in vivo", "mouse", "VPA chronic",
      r"^FC-Wildtype-Vehicle", r"^FC-Wildtype-Valproate"),
    C("GSE17735", arr("GSE17735", "GPL6885"), "hippocampus, wild type, chronic in vivo", "mouse", "VPA chronic",
      r"^HIP-Wildtype-Vehicle", r"^HIP-Wildtype-Valproate"),
    C("GSE17735", arr("GSE17735", "GPL6885"), "striatum, wild type, chronic in vivo", "mouse", "VPA chronic",
      r"^STR-Wildtype-Vehicle", r"^STR-Wildtype-Valproate"),
    C("GSE17735", arr("GSE17735", "GPL6885"), "brain stem, wild type, chronic in vivo", "mouse", "VPA chronic",
      r"^BS-Wildtype-Vehicle", r"^BS-Wildtype-Valproate"),
    C("GSE42904", arr("GSE42904", "GPL1261"), "embryonic brain E14 after maternal dosing", "mouse", "VPA prenatal",
      r"^E14, MC", r"^E14, VPA"),
    C("GSE42904", arr("GSE42904", "GPL1261"), "E18 forebrain after maternal dosing", "mouse", "VPA prenatal",
      r"^E18, MC, FB", r"^E18, VPA, FB"),
    C("GSE42904", arr("GSE42904", "GPL1261"), "E18 hippocampus after maternal dosing", "mouse", "VPA prenatal",
      r"^E18, MC, HC", r"^E18, VPA, HC"),
    C("GSE101239", ("tar", "GSE101239"), "E15 forebrain neural stem/progenitor cells", "mouse",
      "VPA 300 mg/kg/day maternal, E12-E14", r"Control_E15", r"VPA_E15"),
    C("GSE249964", ("delim", "GSE249964_all_counts.txt.gz", "\t", "cols_len"), "E16.5 cortical neurons, Kat6b wild type",
      "mouse", "VPA 1 mM, 4 days", r"Kat6b_WT_.*_Vehicle", r"Kat6b_WT_.*_VPA"),
    C("GSE50215", arr("GSE50215", "GPL6246"), "mESC-derived neurons day 16", "mouse", "VPA", r"PBS", r"VPA",
      family="ESNATS-linked (not counted as independent)"),
    C("GSE56780", arr("GSE56780", "GPL1261"), "half brain, Mecp2 knockout, in vivo", "mouse", "VPA", r"Saline", r"VPA"),
    C("GSE31792", arr("GSE31792", "GPL1261"), "E15.5 striatal neurospheres", "mouse", "TSA 50 nM, 6 h",
      r"^Control, 6h", r"^TSA treatment, 6h"),
    C("GSE31792", arr("GSE31792", "GPL1261"), "E15.5 striatal neurospheres", "mouse", "TSA 50 nM, 24 h",
      r"^Control, 24h", r"^TSA treatment, 24h"),
    C("GSE43051", arr("GSE43051", "GPL6246"), "hippocampus, wild type, standard cage", "mouse", "TSA in vivo",
      r"^Wild-type Standard Cage Vehicle", r"^Wild-type Standard Cage TSA"),
    C("GSE29419", arr("GSE29419", "GPL6246"), "frontal cortex", "mouse", "SAHA 20 mg/kg x 21 days", r"saline", r"SAHA"),
    C("GSE62240", arr("GSE62240", "GPL16570"), "hippocampus, Tg model, chronic", "mouse", "SAHA chronic",
      r"Hippocampus vehicle", r"Hippocampus SAHA\. "),
    C("GSE159441", ("delim_ens", "GSE159441"), "hippocampal CA1", "mouse", "vorinostat", r"__none__", r"__none__"),
    C("GSE185453", ("delim", "GSE185453_RNA_raw_counts_matrix.txt.gz", "\t"), "hippocampus, in vivo", "mouse",
      "CI-994", r"hippocampus_Veh-Context", r"hippocampus_HDACi-Context"),
    C("GSE185453", ("delim", "GSE185453_RNA_raw_counts_matrix.txt.gz", "\t"), "striatum, in vivo", "mouse",
      "CI-994", r"striatum_Veh-Context", r"striatum_HDACi-Context"),
    C("GSE132382", ("tar", "GSE132382"), "L4-L6 dorsal root ganglia after axotomy", "mouse", "MS-275 12 mg/kg",
      r"Vehicle", r"MS275"),
    C("GSE176194", ("tar", "GSE176194"), "embryonic cortex, Baf155 knockout", "mouse", "TSA", r"Srg3cKOVeh", r"Srg3cKOTSA"),
]

M1 = ("sheet", "GSE115205_normalizedFPKM_SAHA_iPSC_Neurons.txt.gz", "GSE115205_metaData_SampleSheet_SAHA_iPSC_Neurons.txt.gz")
for line_label, who in (("Control", "control line"), ("Patient", "tau A152T line")):
    for key, dose in (("1uM_SAHA", "SAHA 1 uM"), ("2.5uM SAHA", "SAHA 2.5 uM")):
        SPEC.append(C("GSE115205", M1, f"iPSC-derived neurons, {who}", "human", dose,
                      rf"^DMSO\|NoVirus\|{line_label}", rf"^{re.escape(key)}\|NoVirus\|{line_label}"))
SPEC += [
    C("GSE187006", ("log2csv", "GSE187006_Processed_data.csv.gz"), "forebrain organoids, line U1M", "human", "VPA",
      r"U1M\.NC", r"U1M\.V"),
    C("GSE187006", ("log2csv", "GSE187006_Processed_data.csv.gz"), "forebrain organoids, line U2F", "human", "VPA",
      r"U2F\.NC", r"U2F\.V"),
    C("GSE115206", ("sheet", "GSE115206_normalizedFPKM_SAHA_corticalNeurons.txt.gz",
                    "GSE115206_metaData_SampleSheet_SAHA_corticalNeurons.txt.gz"),
      "primary cortical neurons, control virus", "mouse", "SAHA 1 uM", r"^DMSO\|control", r"^1uM_SAHA\|control"),
    C("GSE160374", ("delim", "GSE160374_mouse_HDAC_counts.csv.gz", ","), "ventral tegmental area, wild type, in vivo",
      "mouse", "VPA", r"__vta_veh__", r"__vta_vpa__"),
    C("GSE328496", ("cpm",), "hippocampal neurons, trisomic (Ts65Dn-type) mice, in vivo", "mouse", "SAHA",
      r"^X(26|30|33|35)R$", r"^X(25|38|82)R$"),
]

CACHE = {}


def load(spec):
    key = spec
    if key in CACHE:
        return CACHE[key]
    kind = spec[0]
    background, raw = {}, None
    if kind == "array":
        data, background = load_array(spec[1], spec[2])
    elif kind == "ncbi":
        data, raw = load_ncbi(spec[1])
    elif kind == "tar":
        data, raw = load_tar(spec[1])
    elif kind == "xlsx":
        data, raw = load_xlsx_counts(spec[1])
    elif kind == "delim":
        cols = None
        gene_col = None
        if spec[1].startswith("GSE256142"):
            gene_col = None

            def cols(h):
                return [i for i, x in enumerate(h) if re.match(r"(CTL|DS)_iPSC", x)]
        if spec[1].startswith("GSE249964"):
            def cols(h):
                return list(range(2, len(h)))
            # NCBI Entrez identifiers in the first column
            samples, table = delimited(gz(spec[1]), "\t", 0, cols, None, entrez=True)
            data, rows = counts_to_data(samples, table)
            raw = (samples, rows)
        else:
            data, raw = load_delim(spec[1], spec[2], cols=cols)
    elif kind == "sheet":
        data, raw = load_sheet(spec[1], spec[2])
    elif kind == "log2csv":
        data, raw = load_log2_symbol(spec[1])
    elif kind == "cpm":
        data, raw = load_cpm328496()
    elif kind == "log":
        data, raw = load_log_matrix(spec[1], spec[2])
    elif kind == "renc":
        data, raw = load_renc()
    else:
        raise ValueError(f"no loader for {kind}")
    CACHE[key] = (data, background, raw)
    return CACHE[key]


def select(names, pattern, acc):
    if pattern == "__control__":  # GSE166297: untreated wells titled 'control'
        return [n for n in names if re.match(r"control", n, re.I)]
    if pattern.startswith("__vta"):
        meta, _, _ = series_meta_and_table(D / f"{acc}_series_matrix.txt.gz", None)
        want = "treatment: VEH_VPA" if "veh" in pattern else "treatment: VPA"
        rows = meta["characteristics_ch1"]
        treat = next(r for r in rows if any(v.startswith("treatment:") for v in r))
        geno = next(r for r in rows if any(v.startswith("genotype:") for v in r))
        chosen = {d for d, t, g in zip(meta["description"][-1], treat, geno) if t == want and g == "genotype: Wildtype"}
        return [n for n in names if n in chosen]
    if pattern in ("__ukn1ctl__", "__ukn1vpa__"):
        meta, _, _ = series_meta_and_table(D / f"{acc}_series_matrix.txt.gz", None)
        titles, source = meta["title"][0], meta["source_name_ch1"][0]
        chosen = []
        for t, s in zip(titles, source):
            if pattern == "__ukn1vpa__" and re.search(r"0\.6 ?mM VPA|600 ?.M VPA", s) and "144h" in s:
                chosen.append(t)
            if pattern == "__ukn1ctl__" and re.match(r"UKN1.*_ND_144h", t):
                chosen.append(t)
        return chosen
    return [n for n in names if re.search(pattern, n, re.I)]


# replicate units, read from each deposit's own design and protocol text (added after the blind check):
# GSE249964 two sequencing runs per mouse; GSE302545 one "extra" technical replicate of well 1;
# GSE129241 "Ctrl day21 Rep4" is annotated as valproate-treated in its characteristics and is dropped;
# GSE166297 states N=1 experiment with 8 technical replicates, so no direction call.
UNIT = {"GSE249964": lambda n: re.sub(r"_(300823|080923)$", "", n),
        "GSE302545": lambda n: re.sub(r"_extra$", "", n)}
DROP = {"GSE129241": {"Ctrl day21 Rep4"}}
SINGLE_EXPERIMENT = {"GSE166297"}


def units(data, arm, key, acc):
    """one log2 value per biological unit: technical replicates are averaged on the linear scale."""
    groups = collections.OrderedDict()
    for n in arm:
        if key in data[n]:
            groups.setdefault(UNIT.get(acc, lambda x: x)(n), []).append(2 ** data[n][key])
    return [math.log2(sum(v) / len(v)) for v in groups.values()]


def main():
    # excluded after arm inspection (reason in the result file): GSE147270 (platform A; treated and control arrays
    # from different experiments), GSE290300 (cell type deposited as hESC), GSE159441 (arm map not recovered)
    SPEC[:] = [c for c in SPEC if c["acc"] not in ("GSE147270", "GSE290300", "GSE159441")]
    results, problems = [], []
    for c in SPEC:
        try:
            data, background, raw = load(c["load"])
        except Exception as e:  # a series that cannot be parsed is reported, never silently dropped
            problems.append(f"{c['acc']} {c['exposure']}: load failed: {type(e).__name__}: {e}")
            continue
        names = [n for n in data if n not in DROP.get(c["acc"], set())]
        ctl, trt = select(names, c["control"], c["acc"]), select(names, c["treated"], c["acc"])
        if len(ctl) < 1 or len(trt) < 1 or set(ctl) & set(trt):
            problems.append(f"{c['acc']} {c['exposure']} {c['system']}: arms ctl={len(ctl)} trt={len(trt)} "
                            f"overlap={len(set(ctl) & set(trt))}; names e.g. {names[:4]}")
            continue
        keys = sorted({k for n in ctl + trt for k in data[n]})
        out = dict(c)
        out.pop("load")
        unit = UNIT.get(c["acc"], lambda x: x)
        out.update(n_ctl=len({unit(n) for n in ctl}), n_trt=len({unit(n) for n in trt}), ctl_samples=ctl,
                   trt_samples=trt, probes=[])
        for key in keys:
            x = units(data, trt, key, c["acc"])
            y = units(data, ctl, key, c["acc"])
            if not x or not y:
                continue
            ratio = (sum(2 ** v for v in x) / len(x)) / (sum(2 ** v for v in y) / len(y))
            p = welch(x, y) if len(x) >= 3 and len(y) >= 3 and c["acc"] not in SINGLE_EXPERIMENT else None
            near = bool(background.get(key, False))
            mean_counts = None
            if raw and key in raw[1]:
                order, row = raw[0], raw[1][key]
                mc = [sum(row[order.index(n)] for n in arm) / len(arm) for arm in (ctl, trt)]
                mean_counts = [round(v, 1) for v in mc]
                near = max(mc) < 20
            if near:
                call = "near background"
            elif p is None:
                call = "descriptive"
            elif p < 0.05 and ratio >= 1.25:
                call = "up"
            elif p < 0.05 and ratio <= 0.80:
                call = "down"
            else:
                call = "not distinguished"
            sentinel_p = welch(x, y) if len(x) >= 3 and len(y) >= 3 and c["acc"] not in SINGLE_EXPERIMENT else None
            out["probes"].append(dict(sentinel_p=sentinel_p, gene=key[0], probe=key[1], ratio=round(ratio, 3),
                                      p=None if p is None else float(f"{p:.3g}"), call=call, mean_counts=mean_counts))
        sentinel = [q for q in out["probes"] if q["gene"] in ("H1F0", "CDKN1A")]
        out["sentinel_pass"] = any(q["ratio"] >= 1.5 and q["call"] != "near background" for q in sentinel)
        out["sentinel_pass_p05"] = any(q["ratio"] >= 1.5 and q["call"] != "near background" and q["sentinel_p"] is not None
                                       and q["sentinel_p"] < 0.05 for q in sentinel)
        calls = {q["call"] for q in out["probes"] if q["gene"].startswith("WWOX")}
        directional = calls & {"up", "down"}
        if not calls:
            series = "WWOX row not found"
        elif len(directional) == 2:
            series = "mixed"
        elif directional:
            series = directional.pop()
        elif "not distinguished" in calls:
            series = "not distinguished"
        elif "descriptive" in calls:
            series = "descriptive (n<3)"
        else:
            series = "near background"
        out["wwox_call"] = series
        results.append(out)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "results.json").write_text(json.dumps(results, indent=1))
    for r in results:
        w = "; ".join(f"{q['probe']}={q['ratio']}(p={q['p']},{q['call']})" for q in r["probes"] if q["gene"].startswith("WWOX"))
        s = "; ".join(f"{q['gene']}:{q['ratio']}" for q in r["probes"] if not q["gene"].startswith("WWOX"))
        print(f"{r['acc']} | {r['species']} | {r['system'][:40]} | {r['exposure']} | n {r['n_ctl']}/{r['n_trt']} | "
              f"S {'PASS' if r['sentinel_pass'] else 'fail'} [{s[:90]}] | {r['wwox_call']} | {w[:330]}")
    print("\nPROBLEMS:")
    print("\n".join(problems))


if __name__ == "__main__":
    main()
