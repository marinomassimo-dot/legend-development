"""IT41 P10: consume the HIF1A-to-BNIP3 package (hif1a_bnip3_it41_20261109/consumer_delta.md rows 1-5): a premise row set, a premise-measurement investigation (INV-19) so that the three BNIP3 chains get a premise of their own instead of the HK2 one, the K01 packet, the need. Idempotent; marker [IT41b]. Row 6 (identities) stays with Harness."""
import csv, io, json
from pathlib import Path
R = Path(__file__).resolve().parent.parent; T = "[IT41b] "; log = []
# 1 premises
pp = R / "case_it9_p6_hif_axis_20261030/premises.tsv"; rows = list(csv.reader(io.StringIO(pp.read_text()), delimiter="\t")); h = rows[0]
new = [("P11", "BNIP3 in the WWOX-deficient human organoid: transcript +0.46 log2 (1.38-fold), not robust (4 against 2 libraries); the raw neuron-library sign is a scale artefact; mouse P17 flat", "hif1a_bnip3_it41_20261109/output/decisive.tsv D01-D03; GEO deposits (re-derived by the package verifier)"),
       ("P12", "No BNIP3 protein or mitophagy-flux measurement exists in a WWOX-deficient neural system (a search result, not a statement about the literature)", "hif1a_bnip3_it41_20261109/output/decisive.tsv D14; queries.tsv"),
       ("P13", "Direction of BNIP3 is context dependent in the neural cells read: protein up in hypoxia with glucose and down in oxygen-glucose deprivation in HT22, with BNIP3 loss harmful in the deprivation arm; the rat epilepsy HIF-inhibitor test lowered HIF-1alpha and raised BNIP3", "hif1a_bnip3_it41_20261109/output/decisive.tsv D07, D11-D12"),
       ("P14", "The HIF1A-to-BNIP3 relation of the engine is non-neural in its primary record", "hif1a_bnip3_it41_20261109/output/decisive.tsv D04")]
for pid, prem, where in new:
    if not any(r[0] == pid for r in rows[1:]): rows.append([pid, prem, where]); log.append(("premises", pid))
o = io.StringIO(); csv.writer(o, delimiter="\t", lineterminator="\n").writerows(rows); pp.write_text(o.getvalue())
# 3 investigation INV-19 (premise measurement; no compound; no rank movement)
ip = R / "ranking_it8_p9_20261029/investigations_it20.tsv"; rows = list(csv.reader(io.StringIO(ip.read_text()), delimiter="\t")); h = rows[0]; ix = {k: i for i, k in enumerate(h)}
if not any(r[0] == "INV-19" for r in rows[1:]):
    v = dict(inv_id="INV-19", rank="7", need_id="NEED-PDH-PYRUVATE-AXIS",
      intervention="No compound: measurement of the premise behind the HIF1A-to-BNIP3 chains (BNIP3 protein, mitophagy flux and direction in WWOX-deficient human neural cells)",
      question="In isogenic WWOX-deficient against add-back human neural cells at matched oxygen: does BNIP3 protein rise, does it fall on HIF1A and EPAS1 knockdown, and does BNIP3 knockdown make survival, ROS and membrane potential better or worse?",
      why_now="Three generated proposals (IT21P2-0001 to 0003) carry a HIF1A-to-BNIP3 chain; until now they showed no premise of their own and would have read as the HIF1A-to-HK2 premise. The package finds the transcript signal small and partly an artefact, no protein or flux measurement, and a context-dependent direction: the correct output today is an abstention with this question.",
      evidence_available="WWOX-system: organoid transcript +0.46 log2, not robust; the raw neuron-library sign is a scale artefact; no protein or flux. Non-WWOX neural: protein up in hypoxia with glucose and down in oxygen-glucose deprivation in HT22, with BNIP3 loss harmful in the deprivation arm; rat epilepsy HIF-inhibitor test lowered HIF-1alpha and raised BNIP3 (hif1a_bnip3_it41_20261109, partial full texts, one embargoed).",
      decisive_uncertainty="Whether BNIP3 is raised at protein level in WWOX-deficient neural cells, whether the rise is HIF-driven, HIF-independent or a culture-state artefact, and whether the function is protective or harmful there; until then no pharmacological direction at BNIP3 is sustainable and no compound is proposed.",
      next_test="Step 1, no compound: BNIP3 and BNIP3L protein and mRNA from the same lysates, WWOX-deficient against add-back human neural cells at 21, 5 and 1 percent oxygen; step 2: HIF1A and EPAS1 knockdown with HIF target readouts; step 3: BNIP3 knockdown with survival, ROS and membrane potential. The full list of measurements is in the package table of the HIF1A-to-BNIP3 delivery.",
      feasibility="Wet-lab measurement on isogenic human neural lines; not executable from this module. Possible in silico first: recompute the neuron-library scale and the EGR1 observation (IPOTESI) on the deposits. Reopen if a WWOX-deficient neural BNIP3 protein or flux datum is published. Priority: below the ten-row line; it gates three proposals, not the module.",
      origin_class="known_in_wwox", novelty_perimeter="Queried on 2026-11-09 to 2026-11-10 in the package hif1a_bnip3_it41_20261109 (search of this module and open sources, not a statement about the literature).", direction_state="unresolved", status="premise_measurement",
      origin_detail="Known in the WWOX system: the organoid transcript observation; the premise question is restated from the IT41 package B.", evidence_solidity="Premise measurement: transcript only; protein and role not measured.",
      movement_note="New row, enters at rank 7 below the ten-row line. Reasons: it gives three proposals a premise of their own and records an abstention. Not rewarded: novelty.")
    n = [""] * len(h)
    for k, x in v.items(): n[ix[k]] = x
    rows.append(n); log.append(("investigations", "INV-19"))
    o = io.StringIO(); csv.writer(o, delimiter="\t", lineterminator="\n").writerows(rows); ip.write_text(o.getvalue())
# 2 premise map row
mp = R / "generation_it21_p2_20261103/investigation_premises_it32.tsv"; s = mp.read_text()
line = "INV-19\tHIF1A -T\\(\\+\\)-> BNIP3\tthe proposal assumes that HIF1A raises BNIP3 in WWOX-deficient neural cells; the transcript signal is small and partly a scale artefact, no protein or flux is measured, the direction of BNIP3 is context dependent, and the correct output today is an abstention with the discriminating question\n"
if "INV-19\t" not in s: mp.write_text(s.rstrip("\n") + "\n" + line); log.append(("premise map", "INV-19"))
# 4 K01 packet
p = R / "cards/K01_hif_axis_glycolytic_shift.packet.json"; k = json.loads(p.read_text())
a = "In the one neural in-vivo test of a HIF inhibitor read (rat epilepsy, abstract level) HIF-1alpha fell and BNIP3 rose with a lower autophagy marker, and in HT22 cells BNIP3 loss was harmful in oxygen-glucose deprivation; both are non-WWOX, so the direction of any BNIP3-directed action is unresolved."
if a not in k["evidence_against"]: k["evidence_against"].append(a); p.write_text(json.dumps(k, indent=1, ensure_ascii=False) + "\n"); log.append(("K01", "evidence_against"))
# 5 need
nj = R / "needs/needs.json"; d = json.loads(nj.read_text()); n = next(x for x in d["needs"] if x["id"] == "NEED-PDH-PYRUVATE-AXIS")
add = T + "BNIP3 protein and mitophagy flux are unmeasured in any WWOX-deficient neural system; the organoid transcript signal is small (+0.46 log2) and the raw neuron-library sign is a scale artefact; the open measurements are listed in hif1a_bnip3_it41_20261109/output/new_measurements.tsv and carried by INV-19."
if add not in n["notes"]: n["notes"] = n["notes"].rstrip() + " " + add; log.append(("needs", n["id"], "notes"))
nj.write_text(json.dumps(d, indent=1, ensure_ascii=False))
for l in log: print(*l)
