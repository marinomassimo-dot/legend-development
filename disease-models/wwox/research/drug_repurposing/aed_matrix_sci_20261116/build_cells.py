#!/usr/bin/env python3
"""PRESIDIO-010 (SCI, informed arm): draft convergence-matrix cells for antiseizure mechanism classes.

Inputs are the thread files named in THREADS (mechanism content only; no clinical-outcome table is read).
Writes output/cells.tsv, output/scores.tsv, output/stability.tsv and output/summary.txt into the folder given
as the only argument (default: ./output). No network, no other writes.

Rule: PLAN_8H.md "Rule v1". Sign in {match, neutral, aggravation, unknown}; unknown is never neutral.
Score = sum over DISTINCT (axis, origin) pairs of tier x directness, match cells only; aggravation is a
separate column and is never netted; unknown cells are counted, not scored.
"""
import csv
import itertools
import os
import random
import sys

CLASSES = [
    "sodium-channel", "T-type calcium", "SV2A", "AMPA antagonists", "NMDAR pore blockers", "GluN2B NAMs",
    "GABA-A PAM (non-benzodiazepine)", "benzodiazepines", "GABA-AT/GAT", "Kv7 openers",
    "carbonic-anhydrase/multi-target", "valproate-type", "steroid/ACTH", "ketogenic diet",
    "cannabidiol/fenfluramine-type",
]
# Primary targets of each class: background pharmacology (INFERENZA, not a held-file locator).
CLASS_TARGETS = {
    "sodium-channel": "Nav, use-dependent firing", "T-type calcium": "Cav3.x", "SV2A": "SV2A, release",
    "AMPA antagonists": "AMPAR", "NMDAR pore blockers": "NMDAR channel pore, subunit-agnostic",
    "GluN2B NAMs": "GluN2B-containing NMDAR", "GABA-A PAM (non-benzodiazepine)": "GABA-A",
    "benzodiazepines": "GABA-A (alpha1/2/3/5, gamma2)", "GABA-AT/GAT": "GABA catabolism or reuptake",
    "Kv7 openers": "Kv7.2/7.3", "carbonic-anhydrase/multi-target": "CA plus Nav/Cav (agent dependent)",
    "valproate-type": "Nav, Cav, GABA-AT, HDAC, GSK3 (broad)", "steroid/ACTH": "hormonal, MC2R (mechanism unsettled)",
    "ketogenic diet": "metabolic (ketones, KATP, GABA/glutamate cycling)",
    "cannabidiol/fenfluramine-type": "CBD multi-target; fenfluramine serotonergic/sigma-1",
}

DR = "disease-models/wwox/research/drug_repurposing/"
B21 = ("registry CLAIM 021 and PAPER 031 (PMID 34634460), wave note 2026-10-29; fulltext_dossiers/PMID34634460.md; "
       + DR + "nmda_inv05_20261107/output/README.md items 1-2")
# thread -> endpoint, window, axis, origin, tier (0-3), contrast flags, unit, locator, note
THREADS = {
    "T1": dict(name="NMDAR-dependent neocortical bursts, neuron-targeted Wwox loss", endpoint="seizure", window="P13-P15",
               axis="glutamatergic-excitation", origin="O-BRETON21", tier=3, gt=True, dxg=False, unit="slices; d-APV arm 5 slices/3 animals",
               loc=B21, note="36/42 KO v 0/11 WT slices burst; d-APV 50 uM abolished bursts in KO only, no test; slices P13-P17"),
    "T2": dict(name="reduced spontaneous inhibition in L2/3 pyramidal cells", endpoint="seizure", window="P13-P15",
               axis="GABAergic-inhibition", origin="O-BRETON21", tier=3, gt=True, dxg=False, unit="cells (pooled control)",
               loc=B21 + "; analysis/mechanism_intervention_map.md line 101 (M3)", note="control-group caveat CC-20260826-CLAIM032-01; one paper"),
    "T13": dict(name="intrinsic excitability: depolarisation, firing, sag, post-inhibitory rebound (SCI addition)", endpoint="seizure", window="P13-P15",
                axis="intrinsic-excitability", origin="O-BRETON21", tier=3, gt=True, dxg=False, unit="cells",
                loc="registry CLAIM 021 Summary (PMID 34634460)", note="channels not identified; rebound has several possible carriers"),
    "T3": dict(name="PTZ-provoked seizure score, ethosuximide late phase, Wwox-null pups", endpoint="seizure", window="later/unspecified",
               axis="PTZ-generic", origin="O-CHENG20", tier=0, gt=False, dxg=False, unit="animals, n=6 per arm",
               loc=DR + "fig7_quant_ethosuximide_lithium_sci_20261115/README.md; " + DR + "ttype_20261107/output/README.md item 1",
               note="PTZ-generic only; WT at floor, no interaction test (plan rule: never WWOX-specific)"),
    "T4": dict(name="lithium acts in all three genotypes", endpoint="seizure", window="later/unspecified",
               axis="GSK3-nonspecific", origin="O-CHENG20", tier=0, gt=False, dxg=False, unit="animals",
               loc=DR + "fig7_quant_ethosuximide_lithium_sci_20261115/README.md; " + DR + "gsk3_inv09_20261107/output/README.md",
               note="directness 0 for every class by rule"),
    "T5": dict(name="T-type calcium route (Cav3), channel unmeasured in Wwox tissue", endpoint="seizure", window="later/unspecified",
               axis="Cav3", origin="O-TTYPE", tier=1, gt=False, dxg=False, unit="n/a (abstract-level and tool pharmacology)",
               loc=DR + "ttype_20261107/output/README.md items 2-5; " + DR + "cav3_pair_gaps_rp016_sci_20261115/README.md", note="B. NON RISOLTO"),
    "T7": dict(name="K channel arms (K2P, Kir2, Kv7), tool pharmacology outside WWOX", endpoint="seizure", window="later/unspecified",
               axis="K-channel", origin="O-KARMS", tier=1, gt=False, dxg=False, unit="n/a",
               loc=DR + "second_reader_it44_it45_live_text_sci_20261115/README.md; " + DR + "second_reader_v14_k2p_sci_20261115/README.md", note="no WWOX measurement"),
    "T14": dict(name="organoid GABAergic markers up (GAD1/2) with GABA-A receptor components down (GABRB2/3)", endpoint="seizure", window="later/unspecified",
                axis="GABAergic-markers", origin="O-STEINBERG", tier=2, gt=True, dxg=False, unit="organoid libraries (transcript level)",
                loc="registry CLAIM 002 (PMID 42397075 superseding preprint, PAPER 094); analysis/mechanism_intervention_map.md line 101 (M3, GABA paradox)",
                note="marker-level, not function; disagrees in direction with the slice measurement (T2): the GABA axis is disputed"),
    "T15": dict(name="parvalbumin marker loss (-44% whole hippocampus)", endpoint="seizure", window="later/unspecified",
                axis="PV-interneuron", origin="O-PVMARKER", tier=2, gt=True, dxg=False, unit="tissue marker level",
                loc="registry CLAIM 005 via analysis/mechanism_intervention_map.md line 101 (M3)", note="markers, not firing; hippocampus does not burst (Breton 2021)"),
    "T11": dict(name="GluN2B share of evoked NMDAR EPSC falls with age (wild-type barrel cortex)", endpoint="seizure", window="P6-P8",
                axis="GluN2B-ontogeny", origin="O-MIERAU04", tier=1, gt=False, dxg=False, unit="cells",
                loc=DR + "second_reader_wo11_sci_20261115/README.md; " + DR + "wo11_mierau_it55_20261115/README.md",
                note="53% P6-P8 v 14% (0-34) P13-P15, not WWOX, not burst slice; WO-10 open"),
    "T8": dict(name="ISR / eIF2B", endpoint="development", window="later/unspecified", axis="ISR", origin="O-ISR", tier=1, gt=False, dxg=False,
               unit="n/a", loc=DR + "isr_cellclass_he50_20261113/README.md", note="no antiseizure class targets this axis"),
    "T9": dict(name="myelin / OPC (CTGF unresolved)", endpoint="development", window="later/unspecified", axis="myelin", origin="O-CTGF", tier=1,
               gt=False, dxg=False, unit="n/a", loc=DR + "ctgf_held_data_adv007_20261114/README.md", note="composition-explained; no class link"),
    "T10": dict(name="metabolic route (PDH/lactate)", endpoint="development", window="later/unspecified", axis="metabolic", origin="O-I7", tier=0,
                gt=False, dxg=False, unit="n/a", loc=DR + "metabolic_inv07_20261107/output/README.md", note="NON RISOLTO; no neural measurement"),
}
EXCLUDED = {"T6": "GABA-AT clinical series is an outcome source: opened only after both freezes",
            "T12": "aggravation by sodium-channel agents: unknown until a held exposure-with-worsening statement exists (none read)"}

# (thread, class) -> (sign, directness, why)
L = {}
def link(t, cls, sign, d, why):
    L[(t, cls)] = (sign, d, why)

for c, d, w in [("NMDAR pore blockers", 3, "class target = thread target; d-APV (competitive antagonist) abolished bursts in KO"),
                ("GluN2B NAMs", 2, "same axis; GluN2B share of the burst-slice current unmeasured (WO-10 open)"),
                ("AMPA antagonists", 2, "same excitatory pathway; no AMPAR drug tested in WWOX slices"),
                ("sodium-channel", 1, "plausible: reduces recurrent firing; no test"),
                ("valproate-type", 1, "plausible via Nav/Cav; breadth flag (L6)"),
                ("carbonic-anhydrase/multi-target", 1, "plausible via Nav component; agent dependent"),
                ("SV2A", 1, "plausible: release reduction; no test")]:
    link("T1", c, "match", d, w)
for c, d, w in [("GABA-A PAM (non-benzodiazepine)", 3, "class target = thread target (inhibition deficit); GABA response unmeasured (RC-001)"),
                ("benzodiazepines", 3, "same target; subtype selectivity dispute (ADV-004) not WWOX-specific"),
                ("GABA-AT/GAT", 2, "raises GABA at synapse; same pathway; no WWOX test"),
                ("valproate-type", 1, "partial GABA-AT component"),
                ("cannabidiol/fenfluramine-type", 1, "plausible: reported GABA-A modulation of CBD; weak")]:
    link("T2", c, "match", d, w)
for c, d, w in [("sodium-channel", 2, "same pathway: firing is Nav dependent; depolarisation and increased firing measured"),
                ("T-type calcium", 2, "same pathway: post-inhibitory rebound is partly T-type driven; carrier unidentified"),
                ("Kv7 openers", 1, "plausible: hyperpolarising lever against depolarisation; K conductance unidentified"),
                ("valproate-type", 1, "plausible via Nav/Cav"), ("carbonic-anhydrase/multi-target", 1, "plausible via Nav component")]:
    link("T13", c, "match", d, w)
for c, d in [("GABA-A PAM (non-benzodiazepine)", 3), ("benzodiazepines", 3), ("GABA-AT/GAT", 2)]:
    link("T14", c, "unknown", d, "direction disputed across origins (markers up v receptor components down; slice inhibition down)")
    link("T15", c, "unknown", d, "marker loss is not a measured firing or inhibition deficit; sign left open")
link("T3", "T-type calcium", "match", 3, "ethosuximide-sensitive late phase, but PTZ-generic: tier 0 contributes 0")
link("T5", "T-type calcium", "unknown", 3, "involvement of Cav3 in the WWOX system unresolved")
link("T5", "valproate-type", "unknown", 1, "partial Cav3 block; unresolved")
link("T7", "Kv7 openers", "unknown", 3, "class target = thread target; K-channel involvement in WWOX unmeasured")
link("T11", "GluN2B NAMs", "unknown", 3, "better match early only if NMDAR-dependent excitation exists at P6-P8 (no WWOX data there)")
link("T11", "NMDAR pore blockers", "neutral", 0, "subunit-agnostic: composition does not change the class")
# Aggravation hypotheses (recorded apart, never netted), endpoint-specific
AGG = [
    ("T12", "sodium-channel", "seizure", "P13-P15", "unknown", 0, 1, "O-AH1", "inhibition-deficit logic transferred from Nav1.1 DEEs; needs interneuron firing to depend on Nav (LEAP-1); no held statement",
     "analysis/mechanism_intervention_map.md line 101 (M3); PV interneuron data RP-019 open"),
    ("T16", "NMDAR pore blockers", "development", "P6-P8", "aggravation", 1, 3, "O-IKON99", "NMDAR block in early neonatal rodents triggered apoptotic neurodegeneration (abstract-only premise, not WWOX)",
     DR + "nmdar_pharmacology_it6_p9_20261029/README.md line 169 (Ikonomidou 1999, PMID 9872743)"),
    ("T17", "GABA-A PAM (non-benzodiazepine)", "seizure", "P6-P8", "unknown", 0, 3, "O-RC001", "GABA response and chloride gradient unmeasured in WWOX models; GABA may be depolarising early",
     "analysis/mechanism_intervention_map.md lines 138-139 (RC-001, NKCC1/KCC2)"),
    ("T17", "benzodiazepines", "seizure", "P6-P8", "unknown", 0, 3, "O-RC001", "same premise as T17 for GABA-A PAM", "analysis/mechanism_intervention_map.md lines 138-139 (RC-001)"),
]

AGG_IDS = {a[0] for a in AGG}

def build_cells():
    rows = []
    for t, th in THREADS.items():
        for c in CLASSES:
            sign, d, why = L.get((t, c), ("neutral", 0, "no shared target by class pharmacology (background, INFERENZA)"))
            if t == "T4":
                sign, d, why = "neutral", 0, "lithium: directness 0 for every class (plan rule)"
            if th["endpoint"] == "development":
                sign, d, why = "neutral", 0, "no antiseizure class targets this axis"
            rows.append(dict(thread=t, cls=c, endpoint=th["endpoint"], window=th["window"], sign=sign, tier=th["tier"], directness=d,
                             axis=th["axis"], origin=th["origin"], has_genotype_contrast=int(th["gt"]), has_drug_by_genotype=int(th["dxg"]),
                             unit=th["unit"], locator=th["loc"], why=why, transfer=0))
    # carry the only WWOX-system window (P13-P15) to children: declared transfer, mouse age is not mapped to child age
    extra = []
    for r in rows:
        if r["window"] == "P13-P15" and r["endpoint"] == "seizure":
            q = dict(r); q["window"] = "later/unspecified"; q["transfer"] = 1; extra.append(q)
    rows += extra
    for aid, cls, ep, win, sign, tier, d, origin, why, loc in AGG:
        rows.append(dict(thread=aid, cls=cls, endpoint=ep, window=win, sign=sign, tier=tier, directness=d, axis="aggravation-" + aid, origin=origin,
                         has_genotype_contrast=0, has_drug_by_genotype=0, unit="n/a", locator=loc, why=why, transfer=0))
    return rows

CLASS_ID = {"sodium-channel": "sodium_channel", "T-type calcium": "t_type_calcium", "SV2A": "sv2a", "AMPA antagonists": "ampa_antagonist",
            "NMDAR pore blockers": "nmdar_pore_blocker", "GluN2B NAMs": "glun2b_nam", "GABA-A PAM (non-benzodiazepine)": "gabaa_pam_nonbzd",
            "benzodiazepines": "benzodiazepine", "GABA-AT/GAT": "gaba_at_gat", "Kv7 openers": "kv7_opener",
            "carbonic-anhydrase/multi-target": "carbonic_anhydrase_multitarget", "valproate-type": "valproate_type", "steroid/ACTH": "steroid_acth",
            "ketogenic diet": "ketogenic_diet", "cannabidiol/fenfluramine-type": "cbd_fenfluramine"}

# The form's unit is one of cells, animals, children: the nearest category of the evidence's unit of observation (true unit stays in cells.tsv).
FORM_UNIT = {"T1": "cells", "T2": "cells", "T13": "cells", "T3": "animals", "T4": "animals", "T5": "cells", "T7": "cells", "T8": "cells",
             "T9": "cells", "T10": "animals", "T11": "cells", "T14": "cells", "T15": "animals", "T12": "animals", "T16": "animals", "T17": "animals"}

def export_form(rows, outdir):
    """cells_form.tsv in the column set of framework/scripts/aed_matrix.py (HE's form), plus threads.tsv (the declared thread list)."""
    cols = ["cell_id", "thread_id", "class_id", "agent_id", "endpoint", "age", "sign", "evidence_tier", "link_directness", "axis", "origin_id",
            "has_genotype_contrast", "has_drug_by_genotype", "unit", "source_locator"]
    with open(os.path.join(outdir, "cells_form.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(cols)
        for r in rows:
            age = r["window"].replace("/", "_")
            cid = f"{r['thread']}-{CLASS_ID[r['cls']]}-{r['endpoint']}-{age}"
            w.writerow([cid, r["thread"], CLASS_ID[r["cls"]], "", r["endpoint"], age, r["sign"], r["tier"], r["directness"], r["axis"], r["origin"],
                        "yes" if r["has_genotype_contrast"] else "no", "yes" if r["has_drug_by_genotype"] else "no", FORM_UNIT[r["thread"]], r["locator"]])
    used = sorted({r["thread"] for r in rows}, key=lambda t: int(t[1:]))
    with open(os.path.join(outdir, "threads.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["thread_id", "name", "origin", "axis", "tier"])
        for t in used:
            th = THREADS.get(t)
            w.writerow([t, th["name"] if th else "aggravation premise (see cells)", th["origin"] if th else "", th["axis"] if th else "", th["tier"] if th else ""])

def scores(rows, tier_shift=None, collapse=False):
    out = {}
    for ep, win in sorted({(r["endpoint"], r["window"]) for r in rows}):
        for c in CLASSES:
            pairs, agg, unk = {}, 0, 0
            for r in rows:
                if (r["endpoint"], r["window"], r["cls"]) != (ep, win, c) or r["thread"] in AGG_IDS:
                    if (r["endpoint"], r["window"], r["cls"]) == (ep, win, c) and r["sign"] == "aggravation":
                        agg += r["tier"] * r["directness"]
                    continue
                tier = r["tier"] if not tier_shift else max(0, min(3, r["tier"] + tier_shift.get(r["thread"], 0)))
                if r["sign"] == "match":
                    pairs[(r["axis"], r["origin"])] = tier * r["directness"]
                elif r["sign"] == "unknown":
                    unk += 1
            if collapse:
                per_origin = {}
                for (ax, og), v in pairs.items():
                    per_origin[og] = max(per_origin.get(og, 0), v)
                match = sum(per_origin.values())
            else:
                match = sum(pairs.values())
            out[(ep, win, c)] = dict(match=match, aggravation=agg, unknown=unk, n_pairs=len(pairs))
    return out

def top_set(sc, ep, win):
    best = max(sc[(ep, win, c)]["match"] for c in CLASSES)
    return (frozenset(c for c in CLASSES if sc[(ep, win, c)]["match"] == best), best)

def permutation_null(rows, ep, win, draws=5000, seed=20261116):
    """Class-degree-preserving null: each class's (directness, sign) multiset over the threads of the window is shuffled
    across those threads (tiers stay with the thread). Excess = observed - null mean; p = P(null >= observed)."""
    rng = random.Random(seed)
    ths = sorted({r["thread"] for r in rows if (r["endpoint"], r["window"]) == (ep, win) and not r["thread"] in AGG_IDS})
    tier = {r["thread"]: r["tier"] for r in rows if (r["endpoint"], r["window"]) == (ep, win)}
    cell = {(r["thread"], r["cls"]): r for r in rows if (r["endpoint"], r["window"]) == (ep, win)}
    obs = scores(rows)
    out = {}
    for c in CLASSES:
        vec = [(cell[(t, c)]["directness"], cell[(t, c)]["sign"]) for t in ths]
        tot, cnt, seen = 0.0, 0, set()
        for _ in range(draws):
            v = vec[:]; rng.shuffle(v)
            sc = sum(tier[t] * d for t, (d, sg) in zip(ths, v) if sg == "match")
            tot += sc; cnt += sc >= obs[(ep, win, c)]["match"]; seen.add(sc)
        # RULE_AMENDMENTS 3: a degenerate null (one value only) is "null undefined", never a p-value
        out[c] = (obs[(ep, win, c)]["match"], tot / draws, cnt / draws if len(seen) > 1 else "null undefined")
    return out

def voi(rows, ep, win):
    """One-input-at-a-time perturbation of the match cells and thread tiers; does the tied top set change?"""
    base_top, base_best = top_set(scores(rows), ep, win)
    res = []
    keys = [i for i, r in enumerate(rows) if (r["endpoint"], r["window"]) == (ep, win) and r["sign"] == "match" and r["directness"] > 0
            and not r["thread"] in AGG_IDS]
    for i in keys:
        r = rows[i]
        for dd in (-1, 1):
            nd = r["directness"] + dd
            if nd < 0 or nd > 3:
                continue
            mod = [dict(x) for x in rows]; mod[i]["directness"] = nd
            top, best = top_set(scores(mod), ep, win)
            res.append((f"link {r['thread']}-{r['cls']} directness {r['directness']}->{nd}", top != base_top, sorted(top), best))
    return base_top, base_best, res

def stability(rows, ep, win):
    ths = sorted({r["thread"] for r in rows if (r["endpoint"], r["window"]) == (ep, win) and r["tier"] > 0 and not r["thread"] in AGG_IDS})
    combos = list(itertools.product((-1, 0, 1), repeat=len(ths)))
    freq = {c: 0 for c in CLASSES}
    for combo in combos:
        sc = scores(rows, dict(zip(ths, combo)))
        top, best = top_set(sc, ep, win)
        if best > 0:
            for c in top:
                freq[c] += 1
    return {c: freq[c] / len(combos) for c in CLASSES}, len(combos), ths

def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    rows = build_cells()
    cols = ["thread", "cls", "endpoint", "window", "sign", "tier", "directness", "axis", "origin", "has_genotype_contrast",
            "has_drug_by_genotype", "unit", "transfer", "locator", "why"]
    with open(os.path.join(outdir, "cells.tsv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader(); w.writerows(rows)
    export_form(rows, outdir)
    sc, scc = scores(rows), scores(rows, collapse=True)
    lines = []
    with open(os.path.join(outdir, "scores.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["endpoint", "window", "class", "match_score", "origin_collapsed_score", "aggravation_score", "unknown_cells", "n_axis_origin_pairs",
                    "permutation_mean", "permutation_p_ge_observed", "top_share_under_tier_pm1", "breadth_adjusted(match/n_pairs)"])
        for ep, win in sorted({(r["endpoint"], r["window"]) for r in rows}):
            nul = permutation_null(rows, ep, win)
            stab, ncomb, ths = stability(rows, ep, win)
            for c in sorted(CLASSES, key=lambda x: -sc[(ep, win, x)]["match"]):
                s = sc[(ep, win, c)]
                w.writerow([ep, win, c, s["match"], scc[(ep, win, c)]["match"], s["aggravation"], s["unknown"], s["n_pairs"],
                            round(nul[c][1], 2), nul[c][2] if isinstance(nul[c][2], str) else round(nul[c][2], 3), round(stab[c], 3),
                            round(s["match"] / s["n_pairs"], 2) if s["n_pairs"] else 0])
            top, best = top_set(sc, ep, win)
            lines.append(f"{ep} {win}: top score {best}; tied top classes: {', '.join(sorted(top)) if best else 'none (no scorable thread)'}; "
                         f"tier enumeration {ncomb} combos over {','.join(ths) or 'no thread'}")
    with open(os.path.join(outdir, "rankings.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["endpoint", "window", "ranking", "rank", "tie_set_size_k", "informativeness_1_minus_k_over_15", "claimable_as_discriminating", "classes"])
        for ep, win in sorted({(r["endpoint"], r["window"]) for r in rows}):
            for name, scd in (("per_thread_sum", sc), ("origin_collapsed", scc)):
                best = max(scd[(ep, win, c)]["match"] for c in CLASSES)
                if best == 0:
                    w.writerow([ep, win, name, "-", 15, 0.0, 0, "NULL ORDERING FROZEN: no thread links any class; all 15 tied at 0"])
                    continue
                levels = sorted({scd[(ep, win, c)]["match"] for c in CLASSES}, reverse=True)
                for rk, lv in enumerate(levels, 1):
                    cls = [c for c in CLASSES if scd[(ep, win, c)]["match"] == lv]
                    k = len(cls)
                    w.writerow([ep, win, name, rk, k, round(1 - k / 15, 3), int(rk == 1 and k <= 5), "; ".join(cls) + f" (score {lv})"])
    with open(os.path.join(outdir, "voi.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["endpoint", "window", "single_input_change", "top_set_changes", "new_top_set", "new_top_score", "partner_direction_also_changes"])
        for ep, win in (("seizure", "P13-P15"), ("seizure", "later/unspecified")):
            base_top, base_best, res = voi(rows, ep, win)
            changed = {x[0].rsplit(" directness", 0)[0].split(" directness")[0]: [] for x in res}
            for name, ch, top, best in res:
                changed[name.split(" directness")[0]].append(ch)
            for name, ch, top, best in res:
                key = name.split(" directness")[0]
                w.writerow([ep, win, name, int(ch), "; ".join(top), best, int(all(changed[key]) and len(changed[key]) == 2)])
    with open(os.path.join(outdir, "summary.txt"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        print("usage: build_cells.py [OUTPUT_DIR]   (default: ./output; reads nothing, writes only into OUTPUT_DIR)")
        sys.exit(0)
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "output"))
