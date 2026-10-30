#!/usr/bin/env python3
"""IT8 P4: classify every qualified WWOX input into one of four classes against the IT7 P3 method.

Classes (the method = signed gene-to-gene propagation from compound targets, K=3, to six readout genes; plus LINCS signatures):
  ALREADY_REPRESENTED            the external network or the IT7 readout set already carries the content
  NEW_BUT_NOT_USABLE             the content is new but the method has no node/edge type for it, it sits at the wrong level,
                                 has no compound-level link, or it is held-out truth (firewall) that must not become input
  USABLE_NO_CONTAMINATION        would change the input in a stated way without exposing held-out truth
  NOT_SUFFICIENTLY_SUPPORTED     the observation itself is too weak, discordant, unmeasured or not WWOX evidence to encode

Sources: needs/needs.json (observed items), subnetwork_it7_p1 edges.tsv, context_differences_it7_p4 context_matrix.tsv
(14 quantities), cards/*.card.json (27). The assignment of the needs rows is an explicit table below (reviewable line by line);
P1 edges, P4 quantities and cards are assigned by stated rules. Nothing is scored.

Usage: classify_inputs.py --root DRUG_REPURPOSING_DIR --out TSV ; --help answers without work.
"""
import sys, os, csv, json, glob, gzip, collections

if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) == 1:
    print(__doc__); sys.exit(0)

def arg(n, d=None): return sys.argv[sys.argv.index(n) + 1] if n in sys.argv else d
ROOT = arg("--root"); OUT = arg("--out")
AR, NU, US, NS = "ALREADY_REPRESENTED", "NEW_BUT_NOT_USABLE", "USABLE_NO_CONTAMINATION", "NOT_SUFFICIENTLY_SUPPORTED"

REASONS = {
    "A1": "consumed to define the readout, NOT shown to be supported (most of these rows carry a conflict flag): content is the six-gene readout set (SLC2A1, HK2, LDHA, LDHB, BNIP3 up; PDK1 down) already fixed from the two human build systems in IT7 P1/P3; it enters as a readout, not as an edge",
    "A2": "the relation is a gene-to-gene edge already in the external network with the same sign (SIGNOR and CollecTRI via OmniPath)",
    "N1": "wrong level: the endpoint (function, protein, phospho, flux, activity, clinical, histology, cell fraction) has no node or edge type in a transcript-propagation graph and no compound-level link",
    "N2": "intervention response or held-out evaluation datum: using it as input would expose the answer (IT7 firewall); no usable LINCS signature exists for most of the compounds involved",
    "N3": "variant, lesion, stage or cell-type context: the method has no node, edge attribute or filter for it, so it cannot change any score",
    "N4": "self-reference: a result of the IT7 comparison itself, not an observation about WWOX",
    "N5": "no readout of this content exists in the perturbation resource (oligodendrocyte genes are not expressed in the neural cell lines of LINCS)",
    "N6": "a WWOX-loss state change is not a compound-reachable relation: WWOX is a sink in the external graph (7 in-edges, 0 out-edges) and no pilot family in the universe targets WWOX or any of its 7 regulators",
    "S1": "not WWOX-DEE evidence: another disease, a class-level precedent, or WWOX biology in another context (scope OTHER_DISEASE_PRECEDENT or WWOX_BIOLOGY_OTHER_CONTEXT)",
    "S2": "other species or non-neural context (fly, non-neural cell line, fibroblast): ortholog mapping and cell-context transfer unverified; not a human neural network input",
    "S3": "single system, n=1 or 4 v 2 libraries, discordant between systems, sign unresolved or composition-confounded; encoding it would invent a sign",
    "S4": "unmeasured or no observation exists (abstention, card with 0 endpoint outcomes, design record, data not shown)",
    "S5": "case-series or single-patient report without denominator or replication",
    "S6": "concordant absence of signal: nothing to encode",
}

# (need_id_suffix, 1-based index in observed[]) -> (class, reason). Reviewed against each row's readout level, scope, species and direction.
A = {
 ("WWOX-GENE-ADDITION", 1): (NU, "N2"), ("WWOX-GENE-ADDITION", 2): (NU, "N2"), ("WWOX-GENE-ADDITION", 3): (NU, "N1"),
 ("WWOX-SPLICE-CORRECTION", 1): (NU, "N3"), ("WWOX-SPLICE-CORRECTION", 2): (NU, "N3"),
 ("WWOX-PTC-READTHROUGH", 1): (NS, "S4"),
 ("WWOX-MISSENSE-PROTEIN-RESCUE", 1): (NU, "N3"), ("WWOX-MISSENSE-PROTEIN-RESCUE", 2): (NS, "S2"),
 ("WWOX-ENDOGENOUS-BOOST", 1): (NS, "S2"), ("WWOX-ENDOGENOUS-BOOST", 2): (NU, "N3"),
 ("ISR-ATTENUATION", 1): (NS, "S2"), ("ISR-ATTENUATION", 2): (NS, "S3"), ("ISR-ATTENUATION", 3): (NS, "S1"),
 ("ISR-ATTENUATION", 4): (NS, "S1"), ("ISR-ATTENUATION", 5): (NS, "S1"), ("ISR-ATTENUATION", 6): (NS, "S1"),
 ("ISR-ATTENUATION", 7): (NS, "S1"), ("ISR-ATTENUATION", 8): (NS, "S3"), ("ISR-ATTENUATION", 9): (NS, "S3"),
 ("PDH-PYRUVATE-AXIS", 1): (NU, "N6"), ("PDH-PYRUVATE-AXIS", 2): (NU, "N1"), ("PDH-PYRUVATE-AXIS", 3): (AR, "A1"),
 ("PDH-PYRUVATE-AXIS", 4): (AR, "A1"), ("PDH-PYRUVATE-AXIS", 5): (NU, "N2"), ("PDH-PYRUVATE-AXIS", 6): (NU, "N4"),
 ("LACTATE-LDH", 1): (NS, "S2"), ("LACTATE-LDH", 2): (NS, "S2"), ("LACTATE-LDH", 3): (AR, "A1"), ("LACTATE-LDH", 4): (NS, "S5"),
 ("LACTATE-LDH", 5): (AR, "A1"), ("LACTATE-LDH", 6): (NU, "N2"), ("LACTATE-LDH", 7): (NU, "N4"),
 ("MITOCHONDRIAL-RESPIRATION", 1): (NU, "N1"), ("MITOCHONDRIAL-RESPIRATION", 2): (NS, "S3"), ("MITOCHONDRIAL-RESPIRATION", 3): (NS, "S2"),
 ("MITOCHONDRIAL-RESPIRATION", 4): (NU, "N1"), ("MITOCHONDRIAL-RESPIRATION", 5): (NU, "N1"), ("MITOCHONDRIAL-RESPIRATION", 6): (NS, "S3"),
 ("MITOCHONDRIAL-RESPIRATION", 7): (NS, "S3"),
 ("EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", 1): (NU, "N1"), ("EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", 2): (NU, "N1"),
 ("EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", 3): (NU, "N1"), ("EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", 4): (NU, "N1"),
 ("EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", 5): (NS, "S1"), ("EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", 6): (NU, "N1"),
 ("EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", 7): (NS, "S4"), ("EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", 8): (NS, "S4"),
 ("INHIBITORY-HYPOFUNCTION", 1): (NU, "N1"), ("INHIBITORY-HYPOFUNCTION", 2): (NU, "N1"), ("INHIBITORY-HYPOFUNCTION", 3): (NS, "S3"),
 ("INHIBITORY-HYPOFUNCTION", 4): (NS, "S3"), ("INHIBITORY-HYPOFUNCTION", 5): (NS, "S3"),
 ("GABA-CHLORIDE-GRADIENT", 1): (NS, "S4"), ("GABA-CHLORIDE-GRADIENT", 2): (NS, "S3"),
 ("SEIZURE-CONTROL-SYMPTOMATIC", 1): (NS, "S5"), ("SEIZURE-CONTROL-SYMPTOMATIC", 2): (NS, "S5"), ("SEIZURE-CONTROL-SYMPTOMATIC", 3): (NS, "S5"),
 ("T-TYPE-CALCIUM", 1): (NU, "N2"),
 ("MYELINATION", 1): (NU, "N1"), ("MYELINATION", 2): (NU, "N2"), ("MYELINATION", 3): (NS, "S3"),
 ("GSK3B-DEREPRESSION", 1): (NU, "N1"), ("GSK3B-DEREPRESSION", 2): (NU, "N1"),
 ("WNT-BETA-CATENIN", 1): (NS, "S3"), ("WNT-BETA-CATENIN", 2): (NS, "S3"), ("WNT-BETA-CATENIN", 3): (NS, "S1"), ("WNT-BETA-CATENIN", 4): (NS, "S3"),
 ("MYC-PROGENITOR-PROLIFERATION", 1): (NS, "S3"), ("MYC-PROGENITOR-PROLIFERATION", 2): (NU, "N1"), ("MYC-PROGENITOR-PROLIFERATION", 3): (NU, "N1"),
 ("MTOR-AUTOPHAGY", 1): (NS, "S3"),
 ("NEUROINFLAMMATION-GLIA", 1): (NU, "N1"), ("NEUROINFLAMMATION-GLIA", 2): (NU, "N1"), ("NEUROINFLAMMATION-GLIA", 3): (NU, "N2"),
 ("NEUROINFLAMMATION-GLIA", 4): (NU, "N1"), ("NEUROINFLAMMATION-GLIA", 5): (NU, "N1"), ("NEUROINFLAMMATION-GLIA", 6): (NU, "N1"),
 ("NEUROINFLAMMATION-GLIA", 7): (NS, "S3"), ("NEUROINFLAMMATION-GLIA", 8): (NS, "S3"), ("NEUROINFLAMMATION-GLIA", 9): (NS, "S4"),
 ("NEUROINFLAMMATION-GLIA", 10): (NS, "S3"),
 ("REDOX-OXIDATIVE-STRESS", 1): (NS, "S2"), ("REDOX-OXIDATIVE-STRESS", 2): (NS, "S2"),
 ("SYSTEMIC-GLYCAEMIA-GROWTH", 1): (NU, "N1"), ("SYSTEMIC-GLYCAEMIA-GROWTH", 2): (NU, "N1"),
}

def trunc(s, n=150):
    s = " ".join(str(s).replace("\t", " ").split()); return s if len(s) <= n else s[: n - 3] + "..."

def could_add(level, model, age, comparison, content):
    out = []
    t = (content or "").lower()
    if any(w in t for w in ("up", "higher", "lower", "decreas", "increas", "down", "rais")): out.append("direction")
    if level in ("protein", "phospho", "activity", "flux", "cellular (immunostained cell fractions)", "metabolite"): out.append("compartment")
    if any(w in model for w in ("missense", "patient", "knock_in", "knockin", "splice", "knockout", "deletion", "rnai", "shrna")): out.append("variant")
    if any(w in (model + " " + t) for w in ("neuron", "astro", "microgl", "progenitor", "organoid", "oligodend", "pv-")): out.append("cell_type")
    if age and not age.lower().startswith(("not applicable", "unknown")): out.append("stage")
    if level in ("functional", "clinical", "flux", "activity", "protein", "phospho", "metabolite", "cellular (immunostained cell fractions)"): out.append("endpoint")
    if any(w in ((comparison or "") + " " + t) for w in ("treat", "rescue", "inhibitor", "drug", "block", "improved", "response")): out.append("intervention_response")
    return ";".join(dict.fromkeys(out)) or "none"

rows = []
def add(**k): rows.append(k)

# ---- needs --------------------------------------------------------------------------------------------------------
needs = json.load(open(f"{ROOT}/needs/needs.json"))["needs"]
missing = []
for n in needs:
    nid = n["id"].replace("NEED-", "")
    for i, o in enumerate(n["observed"], 1):
        key = (nid, i)
        if key not in A: missing.append(key); continue
        c, rc = A[key]
        add(input_id=f"N:{nid}#{i}:{o['id']}", source_set="needs", source_ref=f"needs/needs.json need {n['id']} observed[{i}] id {o['id']} (PMID {o.get('pmid','')})",
            system=f"{o['model_type']}; {o['species']}; {trunc(o['tissue_or_cells'], 60)}", level=o["readout_level"], content=trunc(f"{o['readout']} -> {o['direction_observed']}"),
            could_add=could_add(o["readout_level"], o["model_type"], o["age_stage"], o["comparison"], o["direction_observed"]),
            cls=c, reason_code=rc, reason=REASONS[rc], scope=o["evidence_scope"],
            representation_or_delta=("only the HIF1A->PDK1 leg is in the network (SIGNOR, ARNT_HIF1A complex, +1); the WWOX->HIF1A leg is not representable (WWOX sink, past the K=3 horizon); observed PDK1 UP opposes the PDK1-DOWN readout" if (nid, i) == ("PDH-PYRUVATE-AXIS", 1) else {"A1": "readout set (p3_run.py UP5/DOWN1); 0 network edges", "A2": "HIF1A->PDK1 present in SIGNOR (ARNT_HIF1A complex) with sign +1"}.get(rc, "no input delta")))
if missing: sys.exit(f"unassigned needs observations: {missing}")

# ---- P1 edges -----------------------------------------------------------------------------------------------------
P1 = f"{ROOT}/subnetwork_it7_p1_20261029"
nodes = {r["node_id"]: r for r in csv.DictReader(open(f"{P1}/nodes.tsv"), delimiter="\t")}
SIX = {"SLC2A1", "HK2", "LDHA", "LDHB", "BNIP3", "PDK1"}
HUMAN_BUILD = {"organoid_ko_w15", "hnpc_shwwox_cage", "neuron_d14_shwwox_cage"}
for e in csv.DictReader(open(f"{P1}/edges.tsv"), delimiter="\t"):
    tgt = nodes[e["target_node"]]; sym = tgt["symbol"]; et = e["edge_type"]; lvl = e["target_readout"]; sy = e["system_id"]
    if et == "inferred" and e["source_node"].startswith("HGNC:") and e["target_node"].startswith("HGNC:") and e["source_node"] != "HGNC:12799":
        c, rc, rep = AR, "A2", f"{nodes[e['source_node']]['symbol']}->{sym} present in the external network (same sign); 0 new edges"
    elif et == "measured" and e["direction_status"] == "consistent" and e["sign"] == "no_change":
        c, rc, rep = NS, "S6", "concordant absence of signal across systems; nothing to encode"
    elif et == "measured" and e["direction_status"] == "consistent" and sym == "Myelin_OL":
        c, rc, rep = NU, "N5", "concordant mouse decrease; no readout of oligodendrocyte genes in the neural LINCS lines"
    elif et == "measured" and lvl in ("transcript", "set_transcript") and sym in SIX and sy in HUMAN_BUILD and e["sign"] == ("down" if sym == "PDK1" else "up"):
        c, rc, rep = AR, "A1", "readout gene of the six-gene set; sign equals the build direction in a human build system"
    elif et == "measured" and lvl in ("transcript", "set_transcript") and sy.startswith("mouse_p17"):
        c, rc, rep = NS, "S3", "mouse P17 contrast already seen (IT6 P4); inside null or control-group dependent; not an input"
    elif et == "measured" and lvl in ("transcript", "set_transcript") and (e["direction_status"] in ("conflict", "single_system", "untested") or e["sign"] in ("no_change", "UNKNOWN", "mixed")):
        c, rc, rep = NS, "S3", "disease-state transcript change, not a compound-reachable edge; sign conflicting, single-system or null"
    elif et == "measured" and lvl in ("transcript", "set_transcript"):
        c, rc, rep = NU, "N6", "disease-state transcript change (WWOX sink)"
    elif lvl in ("protein", "functional", "metabolite", "activity"):
        c, rc, rep = NU, "N1", "no node of this type in the graph"
    else:
        c, rc, rep = NS, "S3", "association or hypothesis without a resolved sign"
    if et in ("association", "hypothesised") and c == NU: c, rc = NS, "S3"
    add(input_id=f"P1:{e['edge_id']}", source_set="p1_edges", source_ref=f"subnetwork_it7_p1_20261029/edges.tsv {e['edge_id']}",
        system=f"{sy}; {e['tissue_or_cell'][:60]}; {e['stage'][:40]}", level=lvl, content=trunc(f"{nodes[e['source_node']]['symbol']} {e['source_state']} -> {sym} {e['sign']} [{et}; {e['direction_status']}]"),
        could_add=could_add(lvl, "knockout" if "KO" in sy.upper() or "ko" in sy else "", e["stage"], "", e["sign"]), cls=c, reason_code=rc, reason=REASONS[rc], scope=et, representation_or_delta=rep)

# ---- P4 quantities -------------------------------------------------------------------------------------------------
Q = {"Q01": (NS, "S3"), "Q02": (NS, "S3"), "Q03": (NS, "S4"), "Q04": (NS, "S6"), "Q05": (AR, "A1"), "Q06": (AR, "A1"), "Q07": (NS, "S4"), "Q08": (NS, "S3"),
     "Q09": (NS, "S3"), "Q10": (NU, "N3"), "Q11": (NU, "N3"), "Q12": (NU, "N5"), "Q13": (NS, "S3"), "Q14": (NU, "N1")}
seen = {}
for r in csv.DictReader(open(f"{ROOT}/context_differences_it7_p4_20261029/context_matrix.tsv"), delimiter="\t"):
    seen.setdefault(r["quantity_id"], r)
for q, r in seen.items():
    c, rc = Q[q]
    add(input_id=f"P4:{q}", source_set="p4_context_matrix", source_ref=f"context_differences_it7_p4_20261029/context_matrix.tsv {q} (13 contexts)", system="13 contexts; about 6 independent models",
        level=r["evidence_class"], content=r["quantity"], could_add="direction;cell_type;stage;variant" if q in ("Q10", "Q11") else ("endpoint" if q in ("Q07", "Q14") else "direction"),
        cls=c, reason_code=rc, reason=REASONS[rc], scope="cross-system matrix", representation_or_delta="readout set" if rc == "A1" else "no input delta")

# ---- cards ---------------------------------------------------------------------------------------------------------
for f in sorted(glob.glob(f"{ROOT}/cards/*.card.json")):
    cd = json.load(open(f)); cid = os.path.basename(f)[: -len(".card.json")]
    abst = bool(cd.get("abstention"))
    n_out = len(cd.get("endpoint_outcomes") or [])
    c, rc = (NS, "S4") if (abst or n_out == 0) else (NU, "N2")
    add(input_id=f"C:{cid}", source_set="cards", source_ref=f"cards/{cid}.card.json", system="compound-class card", level="intervention",
        content=trunc(f"{cd.get('directional_summary')}; {'abstention' if abst else str(len(cd.get('comparisons') or [])) + ' comparisons, ' + str(len(cd.get('endpoint_outcomes') or [])) + ' endpoint outcomes'}"),
        could_add="intervention_response;endpoint" if not abst else "none", cls=c, reason_code=rc, reason=REASONS[rc], scope="card", representation_or_delta="no input delta (compound-target actions come from the P2 tables, not from cards)")

cols = ["input_id", "source_set", "source_ref", "system", "level", "content", "could_add", "cls", "reason_code", "reason", "scope", "representation_or_delta"]
with open(OUT, "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["class" if c == "cls" else c for c in cols])
    for r in rows: w.writerow([r[c] for c in cols])
cnt = collections.Counter((r["source_set"], r["cls"]) for r in rows); tot = collections.Counter(r["cls"] for r in rows)
print("rows", len(rows)); print(json.dumps({f"{a}|{b}": v for (a, b), v in sorted(cnt.items())}, indent=1)); print(dict(tot))
