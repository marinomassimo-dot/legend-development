#!/usr/bin/env python3
"""IT23 P3: assemble the small Q5 (cytokine) network inputs from LEGEND's qualified files.
Writes inputs_q5/: edges_qualified.tsv (subset of the IT7 SIGNOR+CollecTRI signed tables, nothing invented),
edges_assumed.tsv (hand-written, every row labelled ASSUMED with the reason), actions_explicit.tsv (explicit-sign-only
compound actions from family_actions, conflicts/unknown dropped and counted), seeds_q5.tsv (the Q5 seed rows with their levels).
  usage: python3 build_inputs_q5.py [--help]    (stdlib only)
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import csv, gzip, collections, hashlib
from pathlib import Path
HERE = Path(__file__).resolve().parent
DRUG = HERE.parent
NET = DRUG / "network_comparison_it7_p3_20261029" / "inputs"
ACT = DRUG / "generation_it21_p2_20261103" / "results" / "actions" / "family_actions.tsv.gz"
SEEDS = DRUG / "generation_it22_p1_20261103" / "inputs_it22" / "seeds.tsv"
OUT = HERE / "inputs_q5"; OUT.mkdir(exist_ok=True)
NODES = {"RELA", "STAT3", "IL6", "TNF", "IL1B", "CASP1", "NLRP3", "BRD4", "EP300", "SOCS3", "GFAP", "JAK2", "IKBKB", "NFKB1"}
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()

# 1. qualified edges: only pairs whose BOTH ends are in NODES, signed +-1 as exported (unsigned edges were already excluded in IT7)
rows = collections.OrderedDict()
for fn, tag in (("signor_omnipath_edges.tsv.gz", "SIGNOR"), ("collectri_omnipath_edges.tsv.gz", "CollecTRI")):
    with gzip.open(NET / fn, "rt") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["source_symbol"] in NODES and r["target_symbol"] in NODES:
                k = (r["source_symbol"], r["target_symbol"], r["sign"], tag, r["type"])
                rows[k] = rows.get(k, 0) + 1
with open(OUT / "edges_qualified.tsv", "w") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["source", "target", "sign", "table", "type", "n_duplicate_rows", "source_file_sha256", "level_note"])
    for (s, t, sg, tag, ty), n in sorted(rows.items()):
        fn = "signor_omnipath_edges.tsv.gz" if tag == "SIGNOR" else "collectri_omnipath_edges.tsv.gz"
        w.writerow([s, t, sg, tag, ty, n, sha(NET / fn)[:12], "literature-curated regulation sign; no cell type, no mouse/human tag, no logic (AND/OR) in the source"])

# 2. assumed edges: not in the qualified network. Each is textbook biology the IT7 export does not carry; used ONLY as labelled premises.
assumed = [
 ("IL6_sig", "JAK2", "+1", "ligand-receptor-JAK step; the IT7 signed tables carry no edge out of IL6 (checked: 0 outgoing edges)", "RECEPTOR"),
 ("TNF_sig", "IKBKB", "+1", "TNF receptor to IKK; no outgoing edge from TNF in the IT7 tables except one", "RECEPTOR"),
 ("IL1B_sig", "IKBKB", "+1", "IL1R1 to IKK; no outgoing edge from IL1B in the IT7 tables", "RECEPTOR"),
 ("IKBKB", "RELA", "+1", "IKK frees NF-kB (via IkB); SIGNOR has IKBKB -> NFKB1_RELA with sign -1 and CHUK_IKBKB_IKBKG -> NFKBIA -1, i.e. the signed export cannot express this step without the IkB node", "NFKB_CORE"),
 ("SOCS3", "JAK2", "-1", "SOCS3 inhibits JAK signalling; not in the IT7 tables", "NEGFB"),
 ("WWOX_loss", "TRIG", "+1", "UNKNOWN link: what makes cytokines rise in the null mouse is the open question; this edge is a scenario premise, not an observation", "SCENARIO"),
 ("WWOX_loss", "W_route", "+1", "Q5 seed S077 (neuron-specific deletion, myelinated axons down, level pathology) - a phenotype observation, not a molecular edge", "SCENARIO"),
 ("CYT", "MYELIN_OL", "+/-1 by scenario", "role of the cytokine program in myelin is the unknown being scenario-tested; the five roles are premises", "SCENARIO"),
 ("NLRP3_signal2", "CASP1", "+1", "inflammasome second signal (input node ACT2); NFKB -> NLRP3 and CASP1 -> IL1B are qualified, the second signal is not", "NLRP3"),
]
with open(OUT / "edges_assumed.tsv", "w") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["source", "target", "sign", "status", "reason", "premise_switch"])
    for a in assumed:
        w.writerow([a[0], a[1], a[2], "ASSUMED_NOT_QUALIFIED", a[3], a[4]])

# 3. explicit actions: a family-target pair enters only if mean_sign is exactly +-1 (no mixed sign), flags recorded, unknown never present
acts = collections.defaultdict(list)
with gzip.open(ACT, "rt") as fh:
    for r in csv.DictReader(fh, delimiter="\t"):
        if r["target_symbol"] in {"BRD4", "EP300", "JAK2", "IKBKB", "NLRP3", "IL6", "TNF", "IL1B", "STAT3", "RELA", "SOCS3"}:
            acts[r["target_symbol"]].append(r)
with open(OUT / "actions_explicit.tsv", "w") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["target", "n_families_total", "n_explicit_minus1", "n_explicit_plus1", "n_mixed_or_zero_dropped", "n_with_flags", "action_used_in_sim", "node_layer_acted_on", "note"])
    layer = {"IL6": "IL6_sig (protein/activity; neutraliser)", "TNF": "TNF_sig (protein/activity; neutraliser)", "IL1B": "IL1B_sig (protein/activity; neutraliser)",
             "JAK2": "JAK2 activity", "IKBKB": "IKBKB activity", "NLRP3": "NLRP3 activity", "BRD4": "BRD4 activity (cofactor)", "EP300": "EP300 activity (cofactor)",
             "STAT3": "STAT3 activity", "RELA": "RELA activity", "SOCS3": "SOCS3"}
    for t in sorted(acts):
        s = acts[t]; m = sum(float(x["mean_sign"]) == -1 for x in s); p = sum(float(x["mean_sign"]) == 1 for x in s)
        dropped = len(s) - m - p; fl = sum(bool(x["flags"]) for x in s)
        use = "inhibit" if m and not p else "mixed_by_family" if m and p else "activate"
        w.writerow([t, len(s), m, p, dropped, fl, use, layer[t], "family-level sign from the catalogue; EP300 has one activating family" if t == "EP300" else ""])

# 4. seeds (levels kept distinct)
with open(SEEDS) as fh, open(OUT / "seeds_q5.tsv", "w") as out:
    rd = csv.DictReader(fh, delimiter="\t")
    w = csv.writer(out, delimiter="\t", lineterminator="\n")
    w.writerow(["seed_id", "entity_symbol", "level", "direction", "species_observed", "usable_for_generation", "reserved_for_evaluation", "reason_class", "context_short"])
    for r in rd:
        if r["question_id"] == "Q5":
            w.writerow([r["seed_id"], r["entity_symbol"], r["level"], r["direction"], r["species_observed"], r["usable_for_generation"], r["reserved_for_evaluation"], r["reason_class"], r["context"][:140]])
print("wrote", sorted(p.name for p in OUT.iterdir()))
