#!/usr/bin/env python3
"""IT14 P6 trial: function -> target -> action -> compound relations for a declared set, from the module's
existing sources and from candidate sources. Standard library only. Public key-less routes only.
`--help` is safe. `--fetch` performs the network pulls (raw responses saved with SHA-256 under raw/);
default re-reads raw/ and rebuilds relations.tsv and recovery.tsv offline."""
import argparse, csv, gzip, hashlib, json, os, re, sys, time, urllib.parse, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
CACHE = "/home/desktop/legend-development/disease-models/wwox/research/drug_repurposing/catalog/cache"
ADAPTERS = "/home/desktop/legend-development/.claude/worktrees/it14-p6"
# declared set: key -> (ChEMBL id, GtoPdb ligand id, DrugCentral name, Pharos name, expected genes)
SET = {
 "ethosuximide": ("CHEMBL696", "7182", "ethosuximide", "ethosuximide", {"CACNA1G","CACNA1H","CACNA1I","KCNJ6"}),
 "d-AP5": ("CHEMBL84612", "4168", None, "d-AP5", {"GRIN1","GRIN2A","GRIN2B","GRIN2C","GRIN2D"}),
 "ezogabine": ("CHEMBL41355", "2601", "retigabine", "retigabine", {"KCNQ2","KCNQ3"}),
 "bumetanide": ("CHEMBL1072", "4837", "bumetanide", "bumetanide", {"SLC12A2","SLC12A1"}),
 "radiprodil": ("CHEMBL182066", None, None, "radiprodil", {"GRIN2B"}),
 "Ro 25-6981": ("CHEMBL305195", None, None, "Ro 25-6981", {"GRIN2B"}),
 "apinocaltamide": ("CHEMBL4217292", None, None, "apinocaltamide", {"CACNA1G","CACNA1H","CACNA1I"}),
 "memantine": ("CHEMBL807", "4253", "memantine", "memantine", {"GRIN1","GRIN2A","GRIN2B","GRIN2C","GRIN2D"}),
}
FUNCTION_GENES = {"GRIN2B": "Q13224", "KCNQ2": "O43526", "CACNA1G": "O43497", "SLC12A2": "P55011"}
UA = "legend-it14-p6-trial/1 (public key-less GET/POST)"
NM = {"nM": 1.0, "uM": 1e3, "mM": 1e6, "pM": 1e-3}

def http(url, body=None, headers=None, timeout=60):
    h = {"User-Agent": UA, "Accept": "application/json"}; h.update(headers or {})
    req = urllib.request.Request(url, data=body, headers=h)
    for k in range(3):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and k < 2: time.sleep(3 * (k + 1)); continue
            return e.code, e.read()
        except Exception as e:
            if k < 2: time.sleep(3); continue
            return 0, str(e).encode()

def save(name, data):
    os.makedirs(RAW, exist_ok=True)
    p = os.path.join(RAW, name)
    with open(p, "wb") as f: f.write(data)
    return hashlib.sha256(data).hexdigest()

def fetch_all():
    log = []
    def get(name, url, body=None, headers=None):
        st, d = http(url, body, headers); h = save(name, d); log.append((name, url, st, len(d), h)); return st, d
    CH = "https://www.ebi.ac.uk/chembl/api/data"
    get("chembl_status.json", f"{CH}/status.json")
    tids = set()
    for k, (cid, *_rest) in SET.items():
        st, d = get(f"chembl_mech_{cid}.json", f"{CH}/mechanism.json?molecule_chembl_id={cid}&limit=50")
        if st == 200 and not json.loads(d).get("mechanisms"):
            st, d = get(f"chembl_mech_{cid}.json", f"{CH}/mechanism.json?parent_molecule_chembl_id={cid}&limit=50")
        for m in json.loads(d).get("mechanisms", []) if st == 200 else []: tids.add(m["target_chembl_id"])
        # activities through the module's own adapter (molecule-first)
        sys.path.insert(0, ADAPTERS)
        from framework.adapters import chembl
        out = chembl.query({"molecule": cid, "types": ["IC50", "Ki", "Kd", "EC50"], "max_rows": 2000})
        save(f"chembl_act_{cid}.json", json.dumps(out, sort_keys=True).encode())
        for h in out["hits"]: tids.add(h["target_chembl_id"])
        log.append((f"chembl_act_{cid}.json", "adapter chembl molecule=" + cid, 200, out.get("retrieved"), "total=%s truncated=%s" % (out.get("total_count"), out.get("truncated"))))
    tids = sorted(t for t in tids if t)
    for i in range(0, len(tids), 40):
        get(f"chembl_targets_{i//40}.json", f"{CH}/target.json?target_chembl_id__in={','.join(tids[i:i+40])}&limit=100")
    # Open Targets mechanism
    for k, (cid, *_r) in SET.items():
        q = '{ drug(chemblId:"%s"){ name mechanismsOfAction{ rows{ mechanismOfAction actionType targets{ approvedSymbol } } } } }' % cid
        get(f"ot_{cid}.json", "https://api.platform.opentargets.org/api/v4/graphql", json.dumps({"query": q}).encode(), {"Content-Type": "application/json"})
    # Pharos ligand-first
    for k, (_c, _g, _d, ph, _e) in SET.items():
        q = '{ ligand(ligid:"%s"){ name isdrug activities{ type value moa target{ sym name } } } }' % ph
        get(f"pharos_{re.sub(r'[^A-Za-z0-9]','_',ph)}.json", "https://pharos-api.ncats.io/graphql", json.dumps({"query": q}).encode(), {"Content-Type": "application/json"})
    # Pharos target-first
    for g in FUNCTION_GENES:
        q = '{ target(q:{sym:"%s"}){ name tdl ligandCounts{name value} ligands(top:400){ name isdrug activities{type value moa} } } }' % g
        get(f"pharos_target_{g}.json", "https://pharos-api.ncats.io/graphql", json.dumps({"query": q}).encode(), {"Content-Type": "application/json"})
    # BindingDB: compound-first by SMILES (similarity 0.99) and target-first by UniProt
    for k, (cid, *_r) in SET.items():
        st, d = http(f"{CH}/molecule/{cid}.json"); m = json.loads(d)
        smi = (m.get("molecule_structures") or {}).get("canonical_smiles")
        if smi:
            get(f"bdb_cmpd_{cid}.json", "https://www.bindingdb.org/rest/getTargetByCompound?smiles=" + urllib.parse.quote(smi) + "&cutoff=0.99")
            save(f"chembl_smiles_{cid}.txt", smi.encode())
    for g, u in FUNCTION_GENES.items():
        get(f"bdb_target_{g}.json", f"https://www.bindingdb.org/rest/getLigandsByUniprots?uniprot={u}&cutoff=10000&code=0&response=application/json")
    # ChEMBL target-first through the adapter: targets of the accession, then the declared molecules among them
    sys.path.insert(0, ADAPTERS)
    from framework.adapters import chembl as _ch
    ids = ",".join(v[0] for v in SET.values())
    tf = {}
    for g, u in FUNCTION_GENES.items():
        o = _ch.query({"uniprot": u}); tf[g] = {"targets": [(h.get("target_chembl_id"), h.get("pref_name"), h.get("target_type")) for h in o["hits"]], "counts": {}}
        for h in o["hits"]:
            t = h.get("target_chembl_id")
            st, d = http(f"{CH}/activity.json?target_chembl_id={t}&standard_type__in=IC50,Ki,Kd,EC50&limit=1")
            tot = json.loads(d)["page_meta"]["total_count"] if st == 200 else None
            st, d = http(f"{CH}/activity.json?target_chembl_id={t}&standard_type__in=IC50,Ki,Kd,EC50&molecule_chembl_id__in={ids}&limit=200")
            mine = sorted({a["molecule_chembl_id"] for a in json.loads(d).get("activities", [])}) if st == 200 else None
            tf[g]["counts"][t] = {"total_rows": tot, "declared_molecules_present": mine}
    save("chembl_target_first.json", json.dumps(tf, sort_keys=True, indent=1).encode())
    # DrugCentral file
    get("dc_drug.target.interaction.tsv.gz", "https://unmtid-dbs.net/download/DrugCentral/2027/drug.target.interaction.tsv.gz")
    with open(os.path.join(RAW, "fetch_log.tsv"), "w") as f:
        f.write("file\turl\thttp\tbytes\tsha256_or_note\n")
        for r in log: f.write("\t".join(map(str, r)) + "\n")

def rd(name):
    p = os.path.join(RAW, name)
    return open(p, "rb").read() if os.path.exists(p) else None

def to_nm(v, u):
    try: return float(v) * NM.get(u, float("nan"))
    except Exception: return None

def px_to_nm(px):
    try: return 10 ** (9 - float(px))
    except Exception: return None

def build():
    rows = []  # source, compound, gene, target_label, action, type, rel, value_nM, species, ref
    def add(*a): rows.append(a)
    # target resolution (ChEMBL)
    tg = {}
    for fn in sorted(os.listdir(RAW)):
        if fn.startswith("chembl_targets_"):
            for t in json.loads(rd(fn)).get("targets", []):
                genes = sorted({s["component_synonym"] for c in t.get("target_components", []) for s in c.get("target_component_synonyms", []) if s["syn_type"] == "GENE_SYMBOL"})
                tg[t["target_chembl_id"]] = (genes, t["pref_name"], t["target_type"], t.get("organism"))
    for comp, (cid, gid, dcn, ph, exp) in SET.items():
        d = rd(f"chembl_mech_{cid}.json")
        for m in (json.loads(d).get("mechanisms", []) if d else []):
            g, pn, tt, org = tg.get(m["target_chembl_id"], ([], "?", "?", "?"))
            add("chembl_mechanism", comp, "|".join(g), pn, m["action_type"], "", "", None, org, f"{m['target_chembl_id']};" + ",".join(f"{r['ref_type']}:{r['ref_id']}" for r in m.get("mechanism_refs", [])))
        d = rd(f"chembl_act_{cid}.json")
        if d:
            for h in json.loads(d)["hits"]:
                g, pn, tt, org = tg.get(h["target_chembl_id"], ([], h["target_pref_name"], "?", h["target_organism"]))
                v = h["standard_value"]; u = h["standard_units"]
                add("chembl_activity", comp, "|".join(g), h["target_pref_name"], "", h["standard_type"], h["standard_relation"] or "", to_nm(v, u) if u in NM else None, h["target_organism"], f"{h['target_chembl_id']};{h['document_chembl_id']};{h['assay_chembl_id']}")
        d = rd(f"ot_{cid}.json")
        if d:
            dd = (json.loads(d).get("data") or {}).get("drug") or {}
            for m in (dd.get("mechanismsOfAction") or {}).get("rows", []):
                add("opentargets_mechanism", comp, "|".join(t["approvedSymbol"] for t in m["targets"]), m["mechanismOfAction"], m["actionType"], "", "", None, "", cid)
        d = rd(f"pharos_{re.sub(r'[^A-Za-z0-9]','_',ph)}.json")
        if d:
            lg = (json.loads(d).get("data") or {}).get("ligand")
            for a in (lg or {}).get("activities", []):
                add("pharos_ligand", comp, a["target"]["sym"], a["target"]["name"], a["moa"] or "", a["type"] or "", "", px_to_nm(a["value"]) if a["value"] else None, "", "pX=%s" % a["value"])
        # GtoPdb
        if gid:
            R = list(csv.reader(open(CACHE + "/gtopdb/interactions.csv")))[1:]
            h = R[0]
            for r in R[1:]:
                x = dict(zip(h, r))
                if x["Ligand ID"] == gid:
                    v = x["Affinity Median"]
                    add("gtopdb", comp, x["Target Gene Symbol"], x["Target"], x["Action"], x["Affinity Units"], x["Original Affinity Relation"], px_to_nm(v) if (v and x["Affinity Units"].startswith("p")) else None, x["Target Species"], "PMID:" + x["PubMed ID"] + ";sel=" + x["Selectivity"] + ";primary=" + x["Primary Target"])
        # DGIdb
        names = {comp.upper(), (dcn or "").upper(), ph.upper()}
        if comp == "ezogabine": names |= {"EZOGABINE", "RETIGABINE"}
        # DrugCentral
    dc = rd("dc_drug.target.interaction.tsv.gz")
    if dc:
        T = list(csv.DictReader(gzip.decompress(dc).decode().splitlines(), delimiter="\t"))
        for comp, (cid, gid, dcn, ph, exp) in SET.items():
            for r in T:
                if dcn and r["DRUG_NAME"].lower() == dcn.lower():
                    add("drugcentral", comp, r["GENE"], r["TARGET_NAME"], r["ACTION_TYPE"], r["ACT_TYPE"], r["RELATION"], px_to_nm(r["ACT_VALUE"]) if r["ACT_VALUE"] else None, r["ORGANISM"], r["ACT_SOURCE"] + ";" + (r["ACT_SOURCE_URL"] or r["MOA_SOURCE"]))
    # DGIdb file
    names = {}
    for comp, (cid, gid, dcn, ph, exp) in SET.items():
        names[comp] = {comp.upper(), (dcn or comp).upper(), ph.upper(), cid}
        if comp == "ezogabine": names[comp] |= {"EZOGABINE", "RETIGABINE"}
        if comp == "d-AP5": names[comp] |= {"D-AP5", "2-AMINO-5-PHOSPHONOVALERIC ACID", "D-2-AMINO-5-PHOSPHONOVALERATE"}
    for r in csv.DictReader(open(CACHE + "/dgidb/interactions.tsv"), delimiter="\t"):
        for comp, nm in names.items():
            if r["drug_name"].upper() in nm or r["drug_claim_name"].upper() in nm or r["drug_concept_id"].upper().replace("CHEMBL:", "CHEMBL").replace("CHEMBL", "CHEMBL") in nm:
                add("dgidb", comp, r["gene_name"], "", r["interaction_type"], "", "", None, "", r["interaction_source_db_name"])
    # BindingDB compound-first
    for comp, (cid, *_r) in SET.items():
        d = rd(f"bdb_cmpd_{cid}.json"); smi = rd(f"chembl_smiles_{cid}.txt")
        if d and d.strip().startswith(b"{"):
            j = json.loads(d); resp = next(iter(j.values()))
            for a in resp.get("bdb.affinities", []) or []:
                v = a.get("bdb.affinity", ""); num = re.sub(r"[<>~= ]", "", v)
                rel = "".join(c for c in v if c in "<>~=")
                try: val = float(num)
                except Exception: val = None
                same = (a.get("bdb.smiles") or "").split(" ")[0] == (smi or b"").decode()
                add("bindingdb_compound", comp, "", a.get("bdb.target"), "", a.get("bdb.affinity_type"), rel, val, a.get("bdb.species"), "monomer=%s;smiles_string_equal=%s" % (a.get("bdb.monomerid"), same))
    return rows

# BindingDB returns protein names, not gene symbols; this hand-written alias table is the (declared) mapping used for recovery counts
BDB_ALIAS = {"GRIN1": ["NMDA 1", "NMDA 1/"], "GRIN2A": ["NMDA 2A", "NMDA 1/2A"], "GRIN2B": ["NMDA 2B", "NMDA 1/2B"], "GRIN2C": ["NMDA 2C", "NMDA 1/2C"],
             "GRIN2D": ["NMDA 2D", "NMDA 1/2D"], "KCNQ2": ["member 2"], "KCNQ3": ["member 3", "member 2/member 3"], "CACNA1G": ["alpha-1G"], "CACNA1H": ["alpha-1H"],
             "CACNA1I": ["alpha-1I"], "SLC12A2": ["family 12 member 2"], "SLC12A1": ["family 12 member 1"], "KCNJ6": ["GIRK2", "subfamily J member 6"]}

def recovery(rows):
    out = []
    srcs = ["chembl_mechanism","chembl_activity","gtopdb","dgidb","drugcentral","opentargets_mechanism","pharos_ligand","bindingdb_compound"]
    for comp, (cid, gid, dcn, ph, exp) in SET.items():
        for g in sorted(exp):
            for s in srcs:
                hit = [r for r in rows if r[0] == s and r[1] == comp and (g in r[2].split("|") or (s == "bindingdb_compound" and any(a.lower() in r[3].lower() for a in BDB_ALIAS.get(g, []))))]
                acts = sorted({r[4] for r in hit if r[4]}); vals = [r[7] for r in hit if r[7] is not None]
                out.append((comp, g, s, len(hit), ";".join(acts), "%d" % len(vals), ("%.3g-%.3g" % (min(vals), max(vals))) if vals else ""))
    return out

def target_first():
    out = []
    ids = {v[0]: k for k, v in SET.items()}
    # ChEMBL
    d = rd("chembl_target_first.json")
    tf = json.loads(d) if d else {}
    # compound-first BindingDB monomer ids whose SMILES string equals ChEMBL canonical SMILES
    bdb_ids = {}
    for comp, (cid, *_r) in SET.items():
        dd = rd(f"bdb_cmpd_{cid}.json"); smi = rd(f"chembl_smiles_{cid}.txt")
        if dd and smi and dd.strip().startswith(b"{"):
            for a in next(iter(json.loads(dd).values())).get("bdb.affinities", []) or []:
                if (a.get("bdb.smiles") or "").split(" ")[0] == smi.decode(): bdb_ids[str(a["bdb.monomerid"])] = comp
    for g, u in FUNCTION_GENES.items():
        exp = sorted(c for c, v in SET.items() if g in v[4])
        # chembl
        present = set(); tot = 0
        for t, c in tf.get(g, {}).get("counts", {}).items():
            tot += c["total_rows"] or 0; present |= {ids[m] for m in (c["declared_molecules_present"] or []) if m in ids}
        out.append((g, "chembl_target_first(adapter uniprot->targets->activity)", sum(1 for _ in tf.get(g, {}).get("targets", [])), tot, ";".join(exp), ";".join(sorted(present & set(exp))), ";".join(sorted(set(exp) - present))))
        # pharos
        d = rd(f"pharos_target_{g}.json"); n = 0; found = set()
        if d:
            tt = (json.loads(d).get("data") or {}).get("target") or {}
            L = tt.get("ligands", []) or []; n = len(L)
            names = [x["name"].lower() for x in L]
            for c in exp:
                key = SET[c][3].lower()
                if any(key == nm for nm in names): found.add(c)
        out.append((g, "pharos_target_first(ligands top400)", 1 if d else 0, n, ";".join(exp), ";".join(sorted(found)), ";".join(sorted(set(exp) - found))))
        # bindingdb
        d = rd(f"bdb_target_{g}.json"); n = 0; found = set()
        if d and d.strip().startswith(b"{"):
            A = next(iter(json.loads(d).values())).get("affinities", []) or []
            n = len(A)
            for a in A:
                if str(a.get("monomerid")) in bdb_ids: found.add(bdb_ids[str(a["monomerid"])])
        out.append((g, "bindingdb_target_first(UniProt; matched by exact SMILES string only)", 1 if d else 0, n, ";".join(exp), ";".join(sorted(found & set(exp))), ";".join(sorted(set(exp) - found))))
        # gtopdb / drugcentral by gene
        R = list(csv.reader(open(CACHE + "/gtopdb/interactions.csv")))[1:]; h = R[0]
        lig = {v[1]: k for k, v in SET.items() if v[1]}; fg = set(); n = 0
        for r in R[1:]:
            x = dict(zip(h, r))
            if g in x["Target Gene Symbol"].split("|"):
                n += 1
                if x["Ligand ID"] in lig: fg.add(lig[x["Ligand ID"]])
        out.append((g, "gtopdb_target_first(interactions.csv)", 1, n, ";".join(exp), ";".join(sorted(fg & set(exp))), ";".join(sorted(set(exp) - fg))))
        dc = rd("dc_drug.target.interaction.tsv.gz"); fd = set(); n = 0
        if dc:
            for r in csv.DictReader(gzip.decompress(dc).decode().splitlines(), delimiter="\t"):
                if g in r["GENE"].upper().split("|"):
                    n += 1
                    for c, v in SET.items():
                        if v[2] and r["DRUG_NAME"].lower() == v[2].lower(): fd.add(c)
        out.append((g, "drugcentral_target_first(file)", 1, n, ";".join(exp), ";".join(sorted(fd & set(exp))), ";".join(sorted(set(exp) - fd))))
    return out

def main():
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("--fetch", action="store_true", help="network pulls into raw/")
    a = ap.parse_args()
    if a.fetch: fetch_all()
    rows = build()
    with open(os.path.join(HERE, "relations.tsv"), "w") as f:
        f.write("source\tcompound\tgene\ttarget_label\taction\tmeasure_type\trelation\tvalue_nM\tspecies\tref\n")
        for r in rows: f.write("\t".join("" if x is None else str(x).replace("\t", " ").replace("\n", " ") for x in r) + "\n")
    with open(os.path.join(HERE, "recovery.tsv"), "w") as f:
        f.write("compound\texpected_gene\tsource\trows\tactions\tn_quantitative\tvalue_nM_range\n")
        for r in recovery(rows): f.write("\t".join(map(str, r)) + "\n")
    with open(os.path.join(HERE, "target_first.tsv"), "w") as f:
        f.write("function_gene\troute\ttargets_or_tables\tn_rows_or_ligands\tdeclared_compounds_expected\tfound\tnot_found\n")
        for r in target_first(): f.write("\t".join(map(str, r)) + "\n")
    print(len(rows), "relation rows")
if __name__ == "__main__": main()
