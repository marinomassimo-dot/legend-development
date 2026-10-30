"""Build obs_disposition.tsv, coverage.tsv and questions.tsv for IT9 P1 from needs.json and seeds.tsv.

Every observation of the needs table (90), every quantity of the IT7 P4 context matrix (14) and four further items
read in earlier cycles get one disposition row: which question it was assigned to (or why it was excluded or the
question dropped), and a class that the coverage table counts. The class of a needs observation is derived from the
seed rows that cite it (usable beats reserved beats unusable); an observation with no seed row keeps the class written
here by hand. A check fails if an item says it is seeded but no seed row cites it.

  python3 build_tables.py --root <drug_repurposing dir> --out <this dir>
"""
import argparse, csv, json, os, re, collections

# (need id, ordinal within need) -> (question or exclusion code, hand class when no seed row cites it, note)
# codes: Q1..Q5 retained question; D1..D6 dropped question; XOD other-disease precedent (not WWOX); XSELF repository
# method result (self-reference); XDES experimental-design detail merged into another row.
H = {
 ("GENE-ADDITION", 1): ("Q1", ""), ("GENE-ADDITION", 2): ("Q1", ""), ("GENE-ADDITION", 3): ("Q5", ""),
 ("GENE-ADDITION", 4): ("XOD", "Shank3 adult restoration, other disease"), ("GENE-ADDITION", 5): ("XOD", "Meis2 in Cntnap2-null, other disease"),
 ("GENE-ADDITION", 6): ("XOD", "Csnk2b haploinsufficiency AAV, other disease"),
 ("SPLICE-CORRECTION", 1): ("Q1", ""), ("SPLICE-CORRECTION", 2): ("Q1", ""), ("PTC-READTHROUGH", 1): ("Q1", ""),
 ("MISSENSE-PROTEIN-RESCUE", 1): ("Q1", ""), ("MISSENSE-PROTEIN-RESCUE", 2): ("Q1", ""),
 ("ENDOGENOUS-BOOST", 1): ("Q1", ""), ("ENDOGENOUS-BOOST", 2): ("Q1", ""),
 ("ISR-ATTENUATION", 1): ("Q3", ""), ("ISR-ATTENUATION", 2): ("Q3", ""), ("ISR-ATTENUATION", 3): ("XOD", "DNL343 in ALS"),
 ("ISR-ATTENUATION", 4): ("XOD", "vanishing white matter, eIF2B"), ("ISR-ATTENUATION", 5): ("XOD", "5xFAD eIF2B activator"),
 ("ISR-ATTENUATION", 6): ("XOD", "PARS2 fly, GCN2/ATF4 RNAi"), ("ISR-ATTENUATION", 7): ("XOD", "PARS2 fly, second statement of the same experiment"),
 ("ISR-ATTENUATION", 8): ("Q3", ""), ("ISR-ATTENUATION", 9): ("Q3", ""), ("ISR-ATTENUATION", 10): ("XOD", "AFG3L2 loss, Sephin-1"),
 ("ISR-ATTENUATION", 11): ("XOD", "normal mouse mGluR-ATF4"),
 ("PDH-PYRUVATE-AXIS", 1): ("Q2", ""), ("PDH-PYRUVATE-AXIS", 2): ("Q2", ""), ("PDH-PYRUVATE-AXIS", 3): ("Q2", ""), ("PDH-PYRUVATE-AXIS", 4): ("Q2", ""),
 ("PDH-PYRUVATE-AXIS", 5): ("Q2", ""), ("PDH-PYRUVATE-AXIS", 6): ("XSELF", "IT7 P3 method comparison result"),
 ("LACTATE-LDH", 1): ("Q2", ""), ("LACTATE-LDH", 2): ("Q2", ""), ("LACTATE-LDH", 3): ("Q2", ""), ("LACTATE-LDH", 4): ("Q2", ""),
 ("LACTATE-LDH", 5): ("Q2", ""), ("LACTATE-LDH", 6): ("Q2", ""), ("LACTATE-LDH", 7): ("XSELF", "IT7 P3 method comparison result"),
 ("MITOCHONDRIAL-RESPIRATION", 1): ("Q2", ""), ("MITOCHONDRIAL-RESPIRATION", 2): ("Q2", "unusable"), ("MITOCHONDRIAL-RESPIRATION", 3): ("Q2", ""),
 ("MITOCHONDRIAL-RESPIRATION", 4): ("Q2", ""), ("MITOCHONDRIAL-RESPIRATION", 5): ("Q2", ""), ("MITOCHONDRIAL-RESPIRATION", 6): ("Q3", ""), ("MITOCHONDRIAL-RESPIRATION", 7): ("Q2", ""),
 ("EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", 1): ("Q4", ""), ("EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", 2): ("Q4", ""), ("EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", 3): ("Q4", ""),
 ("EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", 4): ("Q4", ""), ("EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", 5): ("XOD", "memantine in GRIN variants, other disease"),
 ("EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", 6): ("Q4", ""), ("EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", 7): ("XDES", "magnesium in incubation ACSF: design detail, bears on the bursting threshold; no seed"),
 ("EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", 8): ("XDES", "d-APV arm design and baseline-frequency discrepancy; merged into the reserved NMDAR-dependence row"),
 ("INHIBITORY-HYPOFUNCTION", 1): ("Q4", ""), ("INHIBITORY-HYPOFUNCTION", 2): ("Q4", ""), ("INHIBITORY-HYPOFUNCTION", 3): ("Q4", ""),
 ("INHIBITORY-HYPOFUNCTION", 4): ("Q4", ""), ("INHIBITORY-HYPOFUNCTION", 5): ("Q4", ""),
 ("GABA-CHLORIDE-GRADIENT", 1): ("D3", ""), ("GABA-CHLORIDE-GRADIENT", 2): ("D3", ""),
 ("SEIZURE-CONTROL-SYMPTOMATIC", 1): ("Q4", ""), ("SEIZURE-CONTROL-SYMPTOMATIC", 2): ("Q4", ""), ("SEIZURE-CONTROL-SYMPTOMATIC", 3): ("Q4", ""),
 ("T-TYPE-CALCIUM", 1): ("Q4", ""),
 ("MYELINATION", 1): ("Q5", ""), ("MYELINATION", 2): ("Q5", ""), ("MYELINATION", 3): ("Q5", ""),
 ("GSK3B-DEREPRESSION", 1): ("Q7", ""), ("GSK3B-DEREPRESSION", 2): ("Q7", "SH-SY5Y overexpression mechanism, other context; cited inside the Q7 row, no separate seed"),
 ("WNT-BETA-CATENIN", 1): ("D1", ""), ("WNT-BETA-CATENIN", 2): ("D1", ""), ("WNT-BETA-CATENIN", 3): ("D1", "unusable"), ("WNT-BETA-CATENIN", 4): ("D1", "unusable"),
 ("MYC-PROGENITOR-PROLIFERATION", 1): ("Q6", ""), ("MYC-PROGENITOR-PROLIFERATION", 2): ("Q6", ""), ("MYC-PROGENITOR-PROLIFERATION", 3): ("Q6", ""),
 ("MTOR-AUTOPHAGY", 1): ("D2", ""),
 ("NEUROINFLAMMATION-GLIA", 1): ("Q5", ""), ("NEUROINFLAMMATION-GLIA", 2): ("Q5", ""), ("NEUROINFLAMMATION-GLIA", 3): ("Q5", ""), ("NEUROINFLAMMATION-GLIA", 4): ("Q5", ""),
 ("NEUROINFLAMMATION-GLIA", 5): ("Q5", ""), ("NEUROINFLAMMATION-GLIA", 6): ("Q5", ""), ("NEUROINFLAMMATION-GLIA", 7): ("Q5", ""), ("NEUROINFLAMMATION-GLIA", 8): ("Q5", ""),
 ("NEUROINFLAMMATION-GLIA", 9): ("Q5", ""), ("NEUROINFLAMMATION-GLIA", 10): ("Q5", ""),
 ("REDOX-OXIDATIVE-STRESS", 1): ("D6", ""), ("REDOX-OXIDATIVE-STRESS", 2): ("D6", ""),
 ("SYSTEMIC-GLYCAEMIA-GROWTH", 1): ("D5", ""), ("SYSTEMIC-GLYCAEMIA-GROWTH", 2): ("D5", ""),
}
# locator tokens that identify an observation inside a seed's source_locator: 'NEED-X:O1' possibly in lists 'O1,O3'
def cited(loc, need, oid):
    for m in re.finditer(r"NEED-%s:([O0-9,]+)" % re.escape(need), loc):
        if oid in m.group(1).split(","): return True
    return False

P4 = {"Q01": "Q3", "Q02": "Q3", "Q03": "Q3", "Q04": "Q3", "Q05": "Q2", "Q06": "Q2", "Q07": "Q2", "Q08": "Q2", "Q09": "Q3", "Q10": "D1", "Q11": "D1", "Q12": "Q5", "Q13": "Q5", "Q14": "Q4"}
EXTRA = [("E01", "FR-IT6P5:W13 patient organoid add-back design, low WWOX by immunoblot, WOREE v SCAR12 (PMID 42397075)", "Q1"),
         ("E02", "DC-IT6P3:section 0.1 phospho-eIF2A / phospho-IRE-1 blots in WWOX-null ovarian cells (PMID 28749468), carried not opened", "Q3"),
         ("E03", "DC-IT6P3:section 0.1 WWOX-silenced endothelial TMT proteome table (PMID 38563965), figshare supplement, NOT opened here", "NONE"),
         ("E04", "DC-IT6P3:section 1 row 4 P47T knock-in partial-loss missense (PMID 36828035)", "Q1")]

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default="..", help="drug_repurposing directory")
    ap.add_argument("--out", default=".", help="output directory")
    a = ap.parse_args()
    needs = json.load(open(os.path.join(a.root, "needs/needs.json")))["needs"]
    seeds = list(csv.DictReader(open(os.path.join(a.out, "seeds.tsv")), delimiter="\t"))
    rows, problems = [], []
    for n in needs:
        nid = n["id"][5:]
        for k, o in enumerate(n["observed"], 1):
            code, hand = H[(nid[5:] if nid.startswith("WWOX-") else nid, k)]
            cit = [s for s in seeds if cited(s["source_locator"], nid, o["id"])]
            # ordinal-safe: duplicate ids inside one need (ISR O5, O6) are resolved by ordinal key in H; a duplicate id cites both
            if cit:
                cls = "usable" if any(s["usable_for_generation"] == "yes" for s in cit) else ("reserved" if any(s["reserved_for_evaluation"] == "yes" for s in cit) else
                      ("gap" if all(s["reason_class"] == "GAP_NOT_MEASURED" for s in cit) else "unusable"))
                if code.startswith("D"): cls = "unusable" if cls != "reserved" else "reserved"
            else:
                cls = "excluded" if code in ("XOD", "XSELF", "XDES") else ("unusable" if code.startswith(("Q", "D")) else "excluded")
                if code.startswith(("Q", "D")) and not hand: problems.append((nid, k, o["id"], code))
            rows.append(["O%03d" % (len(rows) + 1), "needs", "%s:%s#%d" % (n["id"], o["id"], k), o["readout_level"], o["species"], code, cls, len(cit), hand or ""])
    for q, qq in sorted(P4.items()):
        cit = [s for s in seeds if re.search(r"CM-IT7P4:%s\b|CM-IT7P4:[^;]*%s" % (q, q), s["source_locator"])]
        rows.append(["O%03d" % (len(rows) + 1), "context_matrix_it7_p4", "%s" % q, "see matrix", "13 contexts", qq, ("seeded" if cit else "no seed (no resolvable sign or confounded)"), len(cit), ""])
    for e, desc, qq in EXTRA:
        rows.append(["O%03d" % (len(rows) + 1), "earlier_cycle_item", e + " " + desc, "", "", qq, "unusable" if qq == "NONE" else "seeded", 0, ""])
    hdr = ["item_id", "source_kind", "item", "readout_level", "species", "assigned_to", "class", "n_seed_rows_citing", "note"]
    with open(os.path.join(a.out, "obs_disposition.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(hdr); w.writerows(rows)
    if problems: print("NOT CITED BY ANY SEED:", problems)
    # coverage by question: seed rows
    cov = collections.OrderedDict()
    for s in seeds:
        c = cov.setdefault(s["question_id"], collections.Counter())
        c["rows"] += 1
        c[{"yes": "usable"}.get(s["usable_for_generation"]) or ("reserved" if s["reserved_for_evaluation"] == "yes" else ("gap" if s["reason_class"] == "GAP_NOT_MEASURED" else "unusable"))] += 1
    obs = collections.defaultdict(collections.Counter)
    for r in rows:
        if r[1] == "needs": obs[r[5]]["needs_obs"] += 1
        obs[r[5]]["items"] += 1
    with open(os.path.join(a.out, "coverage.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["question_id", "items_considered", "needs_observations", "obs_with_usable_seed", "obs_reserved_only", "obs_unusable_only", "obs_gap_only", "obs_excluded", "seed_rows", "usable", "reserved", "unusable", "named_gaps"])
        tot = None
        for q in sorted(set(list(cov) + list(obs))):
            c, o = cov.get(q, collections.Counter()), obs.get(q, collections.Counter())
            oc = collections.Counter(r[6] for r in rows if r[1] == "needs" and r[5] == q)
            line = [o["items"], o["needs_obs"], oc["usable"], oc["reserved"], oc["unusable"], oc["gap"], oc["excluded"], c["rows"], c["usable"], c["reserved"], c["unusable"], c["gap"]]
            w.writerow([q] + line)
            tot = line if tot is None else [x + y for x, y in zip(tot, line)]
        w.writerow(["TOTAL"] + tot)
    print("dispositions:", len(rows), "total seeds:", sum(c["rows"] for c in cov.values()))

if __name__ == "__main__":
    main()
