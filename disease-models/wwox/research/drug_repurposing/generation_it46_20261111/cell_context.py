"""IT46 P1: join a relation's target symbols to a held cell-class expression table.

  cell_context.py            -> writes cell_context_it46.tsv (every relation of the IT40 search and the IT43/IT44 relation tables)
  from cell_context import context_for; context_for(["KCNQ2", "KCNQ3"])  -> (rows, one-sentence design consequence)

What it answers: for the genes a relation acts on, in which cell class does a held table say they are read, and so can a
difference current or a drug effect attributed to that relation be assigned to a neuron without a cell-specific control?
What it does not answer: channel number, current, share, age or layer. The tables are RNA class means (FPKM) from the
SCI44 coda; the age of a class is part of its label and is carried into every row.

Three conventions, stated here so a reader can change them (they are not biology):
  FLOOR = 1.0 FPKM  below this in every class the gene is "not detected in this table" (unknown, not absent)
  FOLD  = 3.0       a class value this many times the best other class counts as enriched
  a gene that is not in a table is NOT_IN_TABLE: nobody queried it; it is never read as low."""
import ast, csv, functools, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
FLOOR, FOLD = 1.0, 3.0
TABLES = [
    dict(key="mouse", species="mouse", path=DR / "kchan_expression_sci44_20261111/kchan_expression_mouse.tsv", cls="cell_class", val="mean_fpkm", n="n_samples", neuron=r"^neurons?\b", skip=r"^$"),
    dict(key="human", species="human", path=DR / "kchan_expression_sci44_20261111/kchan_expression_human.tsv", cls="group", val="mean_fpkm", n="n_columns", neuron=r"^neuron_", skip=r"^(whole_cortex|mouse_astro)$"),
    # IT46 P8: the same inputs and extraction, GABA and chloride-transport genes (chloride_gaba_expression.py)
    dict(key="mouse_gaba", species="mouse", path=HERE / "expr/chloride_gaba_expression_mouse.tsv", cls="cell_class", val="mean_fpkm", n="n_samples", neuron=r"^neurons?\b", skip=r"^$"),
    # IT46 P5 (SCI46 queue item): the NRF2-axis genes, same inputs and extraction (nrf2_expression_sci46_20261111)
    dict(key="mouse_nrf2", species="mouse", path=DR / "nrf2_expression_sci46_20261111/nrf2_expression_mouse.tsv", cls="cell_class", val="mean_fpkm", n="n_samples", neuron=r"^neurons?\b", skip=r"^$"),
    dict(key="human_nrf2", species="human", path=DR / "nrf2_expression_sci46_20261111/nrf2_expression_human.tsv", cls="group", val="mean_fpkm", n="n_columns", neuron=r"^neuron_", skip=r"^(whole_cortex|mouse_astro)$"),
    # IT47 queue B1: the 30 target genes that had no row (generation_it47_20261112/b1_cellclass), same inputs and extraction
    dict(key="mouse_targets", species="mouse", path=DR / "generation_it47_20261112/b1_cellclass/targets_expression_mouse.tsv", cls="cell_class", val="mean_fpkm", n="n_samples", neuron=r"^neurons?\b", skip=r"^$"),
    dict(key="human_targets", species="human", path=DR / "generation_it47_20261112/b1_cellclass/targets_expression_human.tsv", cls="group", val="mean_fpkm", n="n_columns", neuron=r"^neuron_", skip=r"^(whole_cortex|mouse_astro)$"),
    dict(key="human_gaba", species="human", path=HERE / "expr/chloride_gaba_expression_human.tsv", cls="group", val="mean_fpkm", n="n_columns", neuron=r"^neuron_", skip=r"^(whole_cortex|mouse_astro)$"),
]
FIELDS = ["relation_id", "gene", "table", "species", "state", "neuron_class", "neuron_fpkm", "best_other_class", "best_other_fpkm", "n_samples_neuron", "attributable_to_neuron", "caveat"]


@functools.lru_cache(maxsize=None)
def _load_cached(path, cls, val, n, skip):
    return _read(path, cls, val, n, skip)


def _load(t):
    return _load_cached(str(t["path"]), t["cls"], t["val"], t["n"], t["skip"])


def _read(path, cls, val, n, skip):
    out = {}
    for r in csv.DictReader(open(path, encoding="utf-8"), delimiter="\t"):
        if re.search(skip, r[cls]):
            continue
        out.setdefault(r["gene"].upper(), {})[r[cls]] = (float(r[val]), r[n])
    return out


def classify(classes, neuron_re):
    """classes: {label: (fpkm, n)} -> (state, neuron_label, neuron_val, other_label, other_val, n_neuron)"""
    nl = [k for k in classes if re.search(neuron_re, k)]
    if not nl:
        return "NO_NEURON_CLASS", "", None, "", None, ""
    nk = max(nl, key=lambda k: classes[k][0]); nv = classes[nk][0]
    others = {k: v[0] for k, v in classes.items() if k not in nl}
    ok = max(others, key=others.get) if others else ""; ov = others.get(ok)
    if max([nv] + list(others.values())) < FLOOR:
        s = "NOT_DETECTED_IN_TABLE"
    elif ov is None or nv >= FOLD * max(ov, 1e-9) and nv >= FLOOR:
        s = "NEURON_ENRICHED"
    elif ov >= FOLD * max(nv, 1e-9) and ov >= FLOOR:
        s = "OTHER_ENRICHED"
    else:
        s = "SHARED"
    return s, nk, nv, ok, ov, classes[nk][1]


def join(symbols, relation_id=""):
    rows = []
    for t in TABLES:
        data = _load(t)
        for g in symbols:
            c = data.get(g.upper())
            if c is None:
                rows.append(dict(relation_id=relation_id, gene=g, table=t["key"], species=t["species"], state="NOT_IN_TABLE", neuron_class="", neuron_fpkm="", best_other_class="", best_other_fpkm="",
                                 n_samples_neuron="", attributable_to_neuron="unknown", caveat="not queried in this table: unknown, not low"))
                continue
            s, nk, nv, ok, ov, n = classify(c, t["neuron"])
            att = {"NEURON_ENRICHED": "yes", "OTHER_ENRICHED": "no", "SHARED": "partly", "NOT_DETECTED_IN_TABLE": "unknown", "NO_NEURON_CLASS": "unknown"}[s]
            rows.append(dict(relation_id=relation_id, gene=g, table=t["key"], species=t["species"], state=s, neuron_class=nk, neuron_fpkm=f"{nv:.2f}" if nv is not None else "", best_other_class=ok,
                             best_other_fpkm=f"{ov:.2f}" if ov is not None else "", n_samples_neuron=n, attributable_to_neuron=att,
                             caveat="RNA class mean, not current or share; the class label carries the age; not the age or layer of the phenotype record"))
    return rows


def consequence(rows):
    """One sentence about the design, derived only from the rows, per gene and per table (the tables are not pooled: they can disagree)."""
    g = {}
    for r in rows:
        g.setdefault(r["gene"], []).append(r)
    known = {k: v for k, v in g.items() if any(x["state"] != "NOT_IN_TABLE" for x in v)}
    unknown = sorted(k for k in g if k not in known)
    if not known:
        return "no held table carries these genes: cell-class attribution is an open question, not an answer"
    short = {"NEURON_ENRICHED": "neuron-enriched", "OTHER_ENRICHED": "enriched elsewhere", "SHARED": "shared", "NOT_DETECTED_IN_TABLE": "not detected", "NOT_IN_TABLE": "not queried", "NO_NEURON_CLASS": "no neuron class"}
    parts, clean, needs = [], [], []
    for k, v in sorted(known.items()):
        seen = [x for x in v if x["state"] != "NOT_IN_TABLE"]
        parts.append(k + " (" + ", ".join(f"{x['species']} {short[x['state']]}" for x in seen) + ")")
        (clean if all(x["state"] == "NEURON_ENRICHED" for x in seen) else needs).append(k)
    out = "; ".join(parts)
    if unknown:
        out += "; not in any table (unknown): " + ", ".join(unknown)
    if needs:
        out += ". An effect or difference current attributed to " + ", ".join(needs) + " cannot be assigned to neurons from these tables (shared, elsewhere, not detected, or the tables disagree): it needs a cell-specific control"
    if clean:
        out += ". Neuron-enriched in every table that carries it: " + ", ".join(clean) + " (RNA, one age; not current)"
    return out


def context_for(symbols, relation_id=""):
    rows = join(symbols, relation_id)
    return rows, consequence(rows)


def relations():
    """relation id -> symbols, from the IT40 search script (parsed, not imported: importing it needs the catalogue cache) and the IT43/IT44 relation tables."""
    out = {}
    src = (DR / "mechsearch_it40_20261109/mechanism_search.py").read_text(encoding="utf-8")
    for node in ast.parse(src).body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "RELATIONS":
            for rid, _a, syms, *_ in ast.literal_eval(node.value):
                out[rid] = list(syms)
    for f in sorted(DR.glob("generation_it4[1-9]_*/relations*.tsv")):
        for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"):
            if r.get("relation_id") and r.get("target_symbols"):
                out[r["relation_id"]] = [s for s in re.split(r"[;,]", r["target_symbols"]) if s]
    return out


if __name__ == "__main__":
    rel = relations(); allr = []
    for rid in sorted(rel, key=lambda s: (s[0], int(re.sub(r"\D", "", s) or 0))):
        allr += join(rel[rid], rid)
    with open(HERE / "cell_context_it46.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, FIELDS, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(allr)
    print(len(rel), "relations,", len(allr), "rows -> cell_context_it46.tsv")
