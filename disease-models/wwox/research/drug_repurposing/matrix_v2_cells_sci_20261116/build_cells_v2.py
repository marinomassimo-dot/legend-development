#!/usr/bin/env python3
"""Matrix V2 cells (SCI, prospective; never scored against the sealed table). Builds output/cells_v2_form.tsv for framework/scripts/aed_matrix.py
under rule_v2.json (R1-R3), from the frozen V1 cell builder plus the post-hoc corrections (IT second read) and the V2 class list.

    python3 build_cells_v2.py <repo_root> <out_dir>

Imports aed_matrix_sci_20261116/build_cells.py (V1, unchanged). V2 changes, each declared: (1) class ids per rule_v2.json; (2) 'GABA-A PAM
(non-benzodiazepine)' split into gabaa_pam_synaptic_selective and gabaa_neurosteroid_extrasynaptic, 'cannabidiol/fenfluramine-type' into cannabidiol and
fenfluramine_type, with agent ids on every cell of the four children (R3); (3) new classes hcn_ih_blocker and glial_reactivity_modulator; (4) the IT
second-read corrections (T14 and T15 tier 3; T2 x sodium-channel unknown with directness 1; T14 locator); (5) new thread rows T18 to T22 (unknown sign
where the sign is not established). Not medical advice; mechanism labels only.
"""
import csv
import importlib.util
import os
import sys

if len(sys.argv) != 3 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    sys.exit(0 if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help") else 2)
repo, out = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location("bc", os.path.join(repo, "disease-models/wwox/research/drug_repurposing/aed_matrix_sci_20261116/build_cells.py"))
bc = importlib.util.module_from_spec(spec)
sys.argv = ["build_cells.py", "--help-not-run"]  # the module only runs main() under __main__
spec.loader.exec_module(bc)
DR = bc.DR

V2 = ["sodium_channel", "t_type_calcium", "sv2a", "ampa_antagonist", "nmdar_pore_blocker", "glun2b_nam", "gabaa_pam_synaptic_selective",
      "gabaa_neurosteroid_extrasynaptic", "benzodiazepine", "gaba_at_gat", "kv7_opener", "carbonic_anhydrase_multitarget", "valproate_type", "steroid_acth",
      "ketogenic_diet", "cannabidiol", "fenfluramine_type", "hcn_ih_blocker", "glial_reactivity_modulator"]
SAME = {"sodium-channel": "sodium_channel", "T-type calcium": "t_type_calcium", "SV2A": "sv2a", "AMPA antagonists": "ampa_antagonist", "NMDAR pore blockers": "nmdar_pore_blocker",
        "GluN2B NAMs": "glun2b_nam", "benzodiazepines": "benzodiazepine", "GABA-AT/GAT": "gaba_at_gat", "Kv7 openers": "kv7_opener",
        "carbonic-anhydrase/multi-target": "carbonic_anhydrase_multitarget", "valproate-type": "valproate_type", "steroid/ACTH": "steroid_acth", "ketogenic diet": "ketogenic_diet"}
# representatives per split child: catalogue-level mechanism labels with a held source (IT BLOCK-1 triage and held function-pharmacology files); NOT recommendations
REPS = {"gabaa_pam_synaptic_selective": ["zolpidem", "eszopiclone"], "gabaa_neurosteroid_extrasynaptic": ["ganaxolone", "brexanolone"],
        "cannabidiol": ["cannabidiol"], "fenfluramine_type": ["fenfluramine", "norfenfluramine"]}
UNIT = {"T1": "cells", "T2": "cells", "T13": "cells", "T3": "animals", "T4": "animals", "T5": "cells", "T7": "cells", "T8": "cells", "T9": "cells", "T10": "animals",
        "T11": "cells", "T14": "cells", "T15": "animals", "T12": "animals", "T16": "animals", "T17": "animals", "T18": "animals", "T19": "animals", "T20": "animals",
        "T21": "animals", "T22": "animals"}


def cell(thread, cls, endpoint, age, sign, tier, d, axis, origin, gt, unit, loc, agent=""):
    return dict(thread=thread, cls=cls, endpoint=endpoint, age=age, sign=sign, tier=tier, directness=d, axis=axis, origin=origin, gt=gt, unit=unit, loc=loc, agent=agent)


base = bc.build_cells()
cells = []
for r in base:
    r = dict(r)
    # post-hoc corrections (IT second read, CORRECTIONS_20261116.md)
    if r["thread"] in ("T14", "T15") and r["tier"] == 2:
        r["tier"] = 3
    if r["thread"] == "T14":
        r["locator"] = r["locator"].replace("(PMID 42397075 superseding preprint, PAPER 094)", "(PMID 34268881 Steinberg 2021, PAPER 039; the superseding PMID 42397075 not shown to carry the GAD and GABRB data in the held partial surface)")
    if r["thread"] == "T2" and r["cls"] == "sodium-channel" and r["sign"] == "neutral":
        r["sign"], r["directness"], r["why"] = "unknown", 1, "T12/AH1 scores the same class against the same deficit at directness 1, sign unknown (IT second read)"
    age = r["window"].replace("/", "_")
    common = dict(thread=r["thread"], endpoint=r["endpoint"], age=age, sign=r["sign"], tier=r["tier"], d=r["directness"], axis=r["axis"], origin=r["origin"],
                  gt=r["has_genotype_contrast"], unit=UNIT[r["thread"]], loc=r["locator"])
    if r["cls"] in SAME:
        cells.append(cell(cls=SAME[r["cls"]], **common))
    elif r["cls"] == "GABA-A PAM (non-benzodiazepine)":
        for child, dd in (("gabaa_pam_synaptic_selective", None), ("gabaa_neurosteroid_extrasynaptic", -1)):
            c = dict(common)
            if dd and c["d"] >= 2 and r["thread"] == "T2":
                c["d"] = 2  # tonic component unmeasured (SCI42): neurosteroid directness 2
            for ag in REPS[child]:
                cells.append(cell(cls=child, agent=ag, **c))
    elif r["cls"] == "cannabidiol/fenfluramine-type":
        for child in ("cannabidiol", "fenfluramine_type"):
            c = dict(common)
            if child == "fenfluramine_type" and r["thread"] == "T2":
                c["sign"], c["d"] = "neutral", 0
            for ag in REPS[child]:
                cells.append(cell(cls=child, agent=ag, **c))
# grid of existing (thread, endpoint, age) for the two NEW classes: neutral by default, with the links named in the V2 proposal
grid = sorted({(c["thread"], c["endpoint"], c["age"], c["tier"], c["axis"], c["origin"], c["gt"], c["unit"], c["loc"]) for c in cells if c["thread"] not in ("T12", "T16", "T17")})
for th, ep, age, tier, axis, origin, gt, unit, loc in grid:
    for newc in ("hcn_ih_blocker", "glial_reactivity_modulator"):
        sign, d = "neutral", 0
        if th == "T13" and newc == "hcn_ih_blocker":
            sign, d = "match", 2
        cells.append(cell(th, newc, ep, age, sign, tier, d, axis, origin, gt, unit, loc))
# fenfluramine and sigma-1: class expectation only, sign unknown (does not link under R1)
for ag in REPS["fenfluramine_type"]:
    cells.append(cell("T1", "fenfluramine_type", "seizure", "P13-P15", "unknown", 3, 1, "glutamatergic-excitation", "O-BRETON21", True, "cells", "class expectation: sigma-1 reaches NMDAR function; no WWOX measurement", ag))
# new thread rows (V2 proposal; PRESIDIO-012 candidates and the gliosis signature)
NEWT = [
    ("T18", "PV-interneuron-number", "O-ALDAZ19", 3, "seizure", "P13-P15", "Hussain 2019 PMID 30290271 (PAPER 006; independent laboratory; hippocampus, 2 weeks, n 7 v 7); sign unknown until the Aldaz measurement shows the loss in neocortex",
     {"gabaa_pam_synaptic_selective": 3, "gabaa_neurosteroid_extrasynaptic": 2, "benzodiazepine": 3, "gaba_at_gat": 2}),
    ("T19", "NMDAR-glutamate-transcripts", "O-ALDAZ19", 1, "seizure", "P13-P15", "Hussain 2019 PMID 30290271: NMDA receptor, glutamate receptor and Kv channel genes down (hippocampal RNA n 4 v 4); transcript only", {"nmdar_pore_blocker": 1, "glun2b_nam": 1}),
    ("T20", "Kv-transcripts", "O-ALDAZ19", 1, "seizure", "P13-P15", "Hussain 2019 PMID 30290271: KCNA2 (Kv1.2) down; Kv1.2 is not Kv7", {"kv7_opener": 1}),
    ("T21", "gliosis", "O-AQEILAN-DEL", 3, "seizure", "later_unspecified", "committed neuron-deletion tables (wwox_data_it24_p4_20261104): Gfap up in three contrasts, Aif1, Cd68, Serpina3n, Stat3 up; Tmem119 and P2ry12 down; Il1b, Il1a, Il6, Tnf, Ccl2 not detected",
     {"glial_reactivity_modulator": 2, "steroid_acth": 1}),
    ("T22", "gliosis", "O-ALDAZ-LINES", 3, "seizure", "later_unspecified", "Hussain 2019 (microglia and astrocyte activation) and the P47T paper (progressive neuroinflammation; Aif1 +0.65 CTX FDR 0.036, Serpina3n +0.81 CTX FDR 0.047 in the held tables)",
     {"glial_reactivity_modulator": 2, "steroid_acth": 1}),
]
for th, axis, origin, tier, ep, age, loc, links in NEWT:
    for cls in V2:
        agents = REPS.get(cls, [""])
        for ag in agents:
            d = links.get(cls, 0)
            sign = "unknown" if d else "neutral"
            cells.append(cell(th, cls, ep, age, sign, tier, d, axis, origin, True, UNIT[th], loc, ag))
# form export
os.makedirs(out, exist_ok=True)
cols = ["cell_id", "thread_id", "class_id", "agent_id", "endpoint", "age", "sign", "evidence_tier", "link_directness", "axis", "origin_id", "has_genotype_contrast",
        "has_drug_by_genotype", "unit", "source_locator"]
seen = set()
with open(os.path.join(out, "cells_v2_form.tsv"), "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(cols)
    for c in cells:
        cid = f"{c['thread']}-{c['cls']}-{c['endpoint']}-{c['age']}" + (f"-{c['agent']}" if c["agent"] else "")
        if cid in seen:
            continue
        seen.add(cid)
        w.writerow([cid, c["thread"], c["cls"], c["agent"], c["endpoint"], c["age"], c["sign"], c["tier"], c["directness"], c["axis"], c["origin"],
                    "yes" if c["gt"] else "no", "no", c["unit"], c["loc"]])
print(len(seen), "cells")
