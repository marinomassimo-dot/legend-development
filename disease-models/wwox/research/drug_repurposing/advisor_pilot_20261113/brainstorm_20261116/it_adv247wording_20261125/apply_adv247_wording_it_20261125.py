"""ADV-247 independence wording (IT, 2026-11-25; SCI's section 4 of the audit, relayed by ADV): carried limits in card packets (not_known) and dated clauses in investigations
(evidence_available) for the unit statements, plus the organoid clone limit on the remaining organoid consumers named in SCI's table (cards F02, F04, J01, L01, F03; INV-02, 06, 07, 08, 19).
Text-level, idempotent; cards are rebuilt by repurposing_bridge.py afterwards. Run from the repository root. Hypothesis level; nothing is medical advice."""
import importlib.util, json
from pathlib import Path
DR = Path("disease-models/wwox/research/drug_repurposing")
spec = importlib.util.spec_from_file_location("b", DR / "advisor_pilot_20261113/brainstorm_20261116/it_adv244wording_20261125/apply_adv244b_it_20261125.py")
b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
ORG_NK = b.NEW_NK
M = "[IT 2026-11-25, ADV-247"
P47T = ("Whether agreement across the P47T brain regions on this card is replication: the hippocampus, prefrontal cortex, parietal cortex and cerebellum libraries come from the same mice "
        "(five per group; cerebellum four against three), so agreement across regions is one set of animals seen several times, not replication. " + M + "]")
HIPP = ("Whether the hippocampal bulk contrasts on this card rest on independent animals: the arms are 2 or 3 libraries (GSE158681), one mouse per library is not stated in the sources read, "
        "and whether the same mice gave the cortices is not stated. " + M + "]")
C1 = ("Whether the shRNA contrasts on this card (GSE126075) are independent: one shRNA population per arm in one cell line, and the two stages (progenitor, differentiated) are not independent knockdowns. " + M + "]")
CARDS = {"K01_hif_axis_glycolytic_shift": [P47T], "J01_glial_reactivity_modulation": [ORG_NK, P47T, HIPP], "L01_nrf2_axis": [ORG_NK, P47T],
         "F03_bumetanide_chloride_gradient": [ORG_NK, HIPP], "F02_myelination_activity_sign": [ORG_NK], "F04_nmdar_intervention_class": [ORG_NK],
         "I01_pdk_inhibition_dca_premise_seizure_glycaemia": [C1]}
CL_ORG = (" [IT 2026-11-25, ADV-244: the organoid transcript set behind this row is four knockout organoids of one CRISPR clone (1B) against two parental organoids, apparently from one batch "
          "(authors' Methods: organoids from the same batch unless stated otherwise), so it is not shown to be independent of the clone; the other clone was not sequenced.]")
CL_P47T = (" " + M + ": the P47T region libraries come from the same mice (five per group; cerebellum four against three), so agreement across regions is one set of animals seen several times, not replication.]")
CL_SN = (" " + M + ": one single-nucleus dataset per genotype; number of animals not stated; nuclei are not replicates.]")
CL_HIPP = (" " + M + ": hippocampal bulk arms of 2 or 3 libraries; one mouse per library is not stated.]")
CL_C1 = (" " + M + ": one shRNA population per arm in one cell line; the two stages are not independent knockdowns.]")
INV = {"INV-02": [CL_ORG, CL_C1], "INV-06": [CL_ORG, CL_HIPP], "INV-07": [CL_ORG], "INV-08": [CL_ORG], "INV-15": [CL_SN, CL_HIPP], "INV-16": [CL_P47T], "INV-19": [CL_ORG]}
def j(s): return json.dumps(s, ensure_ascii=False)[1:-1]
def packets():
    n = 0
    for c, items in CARDS.items():
        p = DR / f"cards/{c}.packet.json"
        for it in items:
            raw = p.read_text(encoding="utf-8")
            if j(it) in raw: continue
            d = json.loads(raw); old = json.dumps(d["not_known"][-1], ensure_ascii=False)
            i = raw.index(old, raw.index('"not_known"')); k = raw.rindex("\n", 0, i) + 1; ind = raw[k:i]; assert ind.strip() == ""
            raw = raw[:i + len(old)] + ",\n" + ind + json.dumps(it, ensure_ascii=False) + raw[i + len(old):]
            json.loads(raw); p.write_text(raw, encoding="utf-8"); n += 1
    return n
def inv_tsv(p):
    t = p.read_text(encoding="utf-8"); L = t.split("\n"); h = L[0].split("\t"); c = h.index("evidence_available"); k = h.index("inv_id"); n = 0
    for i, l in enumerate(L):
        f = l.split("\t")
        if i and len(f) == len(h) and f[k] in INV:
            for cl in INV[f[k]]:
                if cl not in f[c] and cl.strip()[:40] not in f[c]: f[c] = f[c].rstrip() + cl; n += 1
            L[i] = "\t".join(f)
    p.write_text("\n".join(L), encoding="utf-8"); return n
def inv_json(p):
    raw = p.read_text(encoding="utf-8"); d = json.loads(raw); n = 0
    for x in [y for k in ("investigations", "further_investigations", "conditional_hypotheses") for y in d.get(k, [])]:
        if x.get("inv_id") in INV:
            old = j(x["evidence_available"]); assert raw.count(old) == 1, x["inv_id"]
            add = "".join(cl for cl in INV[x["inv_id"]] if cl.strip()[:40] not in x["evidence_available"])
            if add: raw = raw.replace(old, old + j(add)); n += 1
    p.write_text(raw, encoding="utf-8"); return n
if __name__ == "__main__":
    RK = DR / "ranking_it8_p9_20261029"
    print("packets", packets(), "tsv", inv_tsv(RK / "investigations.tsv"), inv_tsv(RK / "investigations_it20.tsv"), "json", inv_json(RK / "ranking.json"))
