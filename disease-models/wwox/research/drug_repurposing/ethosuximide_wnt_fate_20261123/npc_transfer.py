"""Transfer a locked WNT3A signature across neural preparations."""
import argparse
from collections import Counter, defaultdict
import csv
import gzip
import hashlib
from itertools import combinations
import json
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile

import numpy as np

from analyze import TARGETS, write


def reference(book_path):
    with zipfile.ZipFile(book_path) as book:
        strings = ["".join(node.itertext()) for node in ET.fromstring(book.read("xl/sharedStrings.xml"))]
        names = [s.get("name") for s in ET.fromstring(book.read("xl/workbook.xml")).findall(".//{*}sheet")]
        assert names == ["Description", "A. WNT3A vs Vehicle", "B. CHIR vs Vehicle", "C. WNT3A+XAV vs WNT3A"]
        tables = []
        for number in [2, 3, 4]:
            table = {}
            duplicates = set()
            author_threshold_count = 0
            for _, row in ET.iterparse(book.open(f"xl/worksheets/sheet{number}.xml"), events=("end",)):
                if not row.tag.endswith("}row"):
                    continue
                columns = {}
                for cell in row:
                    value = cell.findtext("{*}v", "")
                    columns[cell.get("r").rstrip("0123456789")] = strings[int(value)] if cell.get("t") == "s" else value
                row.clear()
                if columns.get("H") in (None, "", "NA", "#N/A", "Shrunken logFC SE"):
                    continue
                # Both the description sheet and the published DEG counts identify
                # G as baseMean, H as log2FoldChange, I as SE, J/K as raw/adjusted P.
                fc = float(columns["H"])
                padj = float(columns["K"]) if columns.get("K") not in (None, "", "NA", "#N/A") else np.nan
                if padj < .1 and abs(fc) > .5:
                    author_threshold_count += 1
                if columns.get("C") != "protein_coding":
                    continue
                assert float(columns["G"]) >= 0 and np.isfinite(fc)
                gene = columns["B"]
                if gene in table:
                    duplicates.add(gene)
                table[gene] = (fc, padj)
            if number in (2, 3):
                assert author_threshold_count == {2:762, 3:3031}[number]
            tables.append({g:v for g,v in table.items() if g not in duplicates})
    candidates = {g:fc for g,(fc,p) in tables[0].items() if p < .05 and g not in TARGETS}
    ranked = sorted(candidates, key=lambda g:(candidates[g],g))
    arms = [list(reversed(ranked[-20:])), ranked[:20]]
    assert min(candidates[g] for g in arms[0]) > 0 > max(candidates[g] for g in arms[1])
    return arms, tables


def orthologs(hgnc_path, mouse_path):
    hgnc = json.loads(hgnc_path.read_text())["response"]["docs"]
    used = Counter(m for row in hgnc for m in row.get("mgd_id",[]))
    mouse = defaultdict(list)
    with gzip.open(mouse_path, "rt") as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            for key in row["dbXrefs"].split("|"):
                if key.startswith("MGI:MGI:"):
                    mouse[key[4:]].append(row["Symbol"])
    mapping = {}
    for row in hgnc:
        ids = row.get("mgd_id", [])
        if len(ids) == 1 and used[ids[0]] == 1 and len(mouse[ids[0]]) == 1:
            mapping[row["symbol"]] = mouse[ids[0]][0]
    return mapping


def expression(path, mouse):
    offset = 8 if mouse else 1
    with gzip.open(path, "rt") as stream:
        reader = csv.reader(stream, delimiter="\t")
        samples = next(reader)[offset:]
        matrix, duplicates = {}, set()
        total = np.zeros(len(samples))
        for row in reader:
            name = row[3 if mouse else 0]
            counts = np.asarray(row[offset:], dtype=float)
            total += counts
            if name in matrix:
                duplicates.add(name)
            matrix[name] = counts
    return samples, {g:x*1e6/total for g,x in matrix.items() if g not in duplicates}


def arm_values(arms, matrix, baseline, lookup, drug):
    panels, rows = [], []
    for arm,genes in zip(["up","down"],arms,strict=True):
        values = []
        for g in genes:
            name = lookup.get(g)
            if name not in matrix:
                rows.append([arm,g,name or "",False,"NA"])
                continue
            x = matrix[name]
            base = (np.median if drug else np.mean)(x[baseline])
            if base >= 1:
                values.append(np.log2(1+x))
            rows.append([arm,g,name,base >= 1,base])
        panels.append(np.asarray(values))
    return panels,rows


def calculate(args):
    out = args.out
    out.mkdir(exist_ok=True,parents=True)
    arms,tables = reference(args.table)
    validation = []
    for i,genes in enumerate(arms):
        for j,contrast in enumerate(["WNT3A", "CHIR", "WNT3A_XAV_vs_WNT3A"]):
            observed = [tables[j][g][0] for g in genes if g in tables[j]]
            expected_sign = (-1)**(i+(j==2))
            validation.append([contrast,["up","down"][i],len(observed),
                               sum(np.sign(x)==expected_sign for x in observed), np.median(observed)])
    write(out/"npc_reference.tsv","contrast arm present expected_sign median_log2FC",validation)
    with gzip.open(args.meta,"rt") as f:
        meta = {r[0]:r[1:] for r in csv.reader(f,delimiter="\t") if r and r[0] in ("!Sample_title","!Sample_description")}
    labels = dict(zip(meta["!Sample_description"], meta["!Sample_title"], strict=True))
    ids,mouse = expression(args.counts,True)
    treated, = [j for j,t in enumerate(ids) if labels[t].startswith("Ethosuximide [")]
    controls = np.array([j for j,t in enumerate(ids) if labels[t].startswith("Vehicle-")])
    drugs = [j for j in range(len(ids)) if j not in controls]
    block = [j for j in drugs if ids[j].split(".")[1] == ids[treated].split(".")[1]]
    assert len(controls)==9 and len(drugs)==218
    case = defaultdict(list)
    for symbol in mouse:
        case[symbol.upper()].append(symbol)
    mappings = {"symbol":{g:v[0] for g,v in case.items() if len(v)==1},
                "orthology":orthologs(args.hgnc,args.mouseinfo)}
    drug_rows, gene_rows = [], []
    for mode,lookup in mappings.items():
        panels,rows = arm_values(arms,mouse,controls,lookup,True)
        gene_rows.extend([[mode,*r] for r in rows])
        if min(map(len,panels))==0:
            raise ValueError(f"No mapped genes for {mode}")
        up,down = [np.mean(y-np.median(y[:,controls],axis=1)[:,None],axis=0) for y in panels]
        score = (up-down)/2
        null = []
        for j in controls:
            delta = [np.mean(y[:,j]-np.median(y[:,controls[controls!=j]],axis=1)) for y in panels]
            null.append((delta[0]-delta[1])/2)
        rank = 1+sum(score[j]>score[treated] for j in drugs)
        decision = "partial_coverage"
        if min(map(len,panels))>=8:
            decision = "inconclusive"
            if up[treated]>0>down[treated] and score[treated]>max(null) and rank<=len(drugs)*.1:
                decision = "activation_like"
            if up[treated]<0<down[treated] and score[treated]<min(null) and rank>len(drugs)*.9:
                decision = "inhibition_like"
        drug_rows.append([mode,*map(len,panels),up[treated],down[treated],score[treated],min(null),max(null),rank,
                         len(drugs),1+sum(score[j]>score[treated] for j in block),len(block),decision])
    write(out/"npc_drug.tsv","mapping n_up n_down up_delta down_delta score vehicle_min vehicle_max rank n_drugs block_rank block_n decision",drug_rows)
    ids,human = expression(args.wwox,False)
    wt = [j for j,t in enumerate(ids) if t.startswith("cwt")]
    ko = [j for j,t in enumerate(ids) if t.startswith("cko")]
    assert len(wt)==2 and len(ko)==4
    panels,rows = arm_values(arms,human,wt,{g:g for g in human},False)
    gene_rows.extend([["human",*r] for r in rows])
    write(out/"npc_coverage.tsv","mapping arm reference_gene target_symbol eligible mean_or_median_baseline_CPM",gene_rows)
    up,down = [np.mean(y,axis=0) for y in panels]
    score = (up-down)/2
    def contrast(x,controls,cases):
        return np.mean(x[cases])-np.mean(x[controls])
    disease = contrast(score,wt,ko)
    loo = [contrast(score,[k for k in wt if k!=j],[k for k in ko if k!=j]) for j in range(len(ids))]
    permutations = [contrast(score,list(pair),[i for i in range(len(ids)) if i not in pair]) for pair in combinations(range(len(ids)),2)]
    write(out/"npc_disease.tsv","n_up n_down up_delta down_delta score omit_min omit_max assignments_ge assignments_le total_assignments coverage",
          [[*map(len,panels),contrast(up,wt,ko),contrast(down,wt,ko),disease,min(loo),max(loo),
            sum(x>=disease-1e-12 for x in permutations),sum(x<=disease+1e-12 for x in permutations),len(permutations),min(map(len,panels))>=8]])
    write(out/"npc_inputs.tsv","input sha256",[(p.name,hashlib.sha256(p.read_bytes()).hexdigest()) for k,p in vars(args).items() if k!="out"])


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ("table","counts","meta","hgnc","mouseinfo","wwox","out"):
        parser.add_argument(key,type=Path)
    calculate(parser.parse_args())
