"""IT59 / ADV-072 + R1 (2026-11-19): SCI's continuation delivery mapped in ONE pass (mapping only; wording is SCI's, messages to IT 2026-11-19 and the notes named below; ADV's instruction: dated lines, no tier change).
(1) the PPxY branch ends in ONE open-question row (the consumption path's outcome (a): no package, no comparison row, no dossier); (2) conduction: one open-question row, and a not_known item on the F02 and H02 packets
(cards rebuilt by repurposing_bridge.py); (3) the sex, litter and cage limit once, in the arm-table pilot description; (4) the E case statement as a file. Idempotent."""
import csv, json, subprocess
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
B = "advisor_pilot_20261113/brainstorm_20261116/"
BN = B + "b_ww1_ppxy_first_pass_sci_20261119/B_WW1_PPXY_FIRST_PASS_SCI_20261119.md"
R3 = B + "r3_erbb4_sign_check_sci_20261119/R3_RESULT_SCI_20261119.md"
R1 = B + "r1_conduction_endpoint_sci_20261119/R1_CONDUCTION_ENDPOINT_NOTE_SCI_20261119.md"
EN = B + "e_materials_test_sci_20261119/E_RESULT_MATERIALS_TEST_SCI_20261119.md"
PC = B + "premise_checks_sci_20261119/PREMISE_CHECKS_A_SCI_20261119.md"
Q1 = ["IT59-Q01", BN + " ; " + R3,
      "Does WWOX WW1 bind the ERBB4 intracellular domain in neurons or interneurons? (provisional until the 2006 Cell full text is read; the P47T allele disrupts all WW1-PPxY partners, so attribution to ERBB4 needs an Erbb4 manipulation)",
      "Whether the WW1-PPxY branch gets a pharmacological comparison or a package: today a refusal row, because the relation is not established with primary evidence in a neural system.",
      "wet_lab_measurement", "OPEN", "main",
      "[IT 2026-11-19, mapped from SCI's first pass B and R3, notes " + BN + " and " + R3 + "; the refusal row of the consumption path: no package, no comparison row, no dossier] SCI's wording in full: 'Does WWOX WW1 bind the ERBB4 intracellular domain in neurons or interneurons? "
      "(the localisation test is not motivated by the astrogenesis and PV phenotypes under the release sign; provisional until the 2006 Cell full text is read; the P47T allele disrupts all WW1-PPxY partners, so attribution to ERBB4 needs an Erbb4 manipulation)'. "
      "Why a refusal: direct but weak in vitro ERBB4 PPxY binding; cellular data at abstract level; NETO2 has no evidence in any original, STRING or IntAct; at abstract level nuclear ERBB4 ICD represses astrogenesis, so the release sign is provisionally incompatible with the organoid astrogenesis; PV undetermined. "
      "Counter-evidence carried: ADV-068 (no PV-directed premise from transcripts) and ADV-070 (stage adjustment not decisive on the held deposits). First zero-spend step: read the 2006 Cell full text (supply path owed). The measure is a partner-specific manipulation (an Erbb4 manipulation).",
      "2026-11-19", "Needs a laboratory with neurons or interneurons and an Erbb4 manipulation; the 2006 full text is the zero-spend step.", "no", ""]
Q2 = ["IT59-Q02", R1 + " ; disease-models/wwox/research/drug_repurposing/cards/F02_myelination_activity_sign.card.json",
      "Can callosal-evoked conduction latency, re-measured with animal-level statistics and a rescue arm, serve as a functional endpoint for the myelin cards (F02, H02) and the pup or slice designs, and does any myelination-promoting class have an interpretable lever?",
      "Whether F02 and H02 myelin arms read a structural endpoint (neuronal rescue demonstrated) or need a conduction re-measurement first.",
      "wet_lab_measurement", "OPEN", "main",
      "[IT 2026-11-19, mapped from SCI's R1 (note " + R1 + ", extraction report as delivered)] Conduction was MEASURED ONCE, with inconsistencies: legend 8 slices from 5 animals (controls) and 8 slices from 6 (knockout); the control n is identical to another experiment's n; graph-read N1 latency about 2.5 against 3.2 ms (P 0.0104); N1/N2 ratio P 0.0030; Synapsin-Cre only; acute slices P13 to P17; no rescue; no velocity; Methods without a callosal protocol: a candidate readout that needs re-measurement. "
      "STRUCTURAL myelin endpoints are the usable ones (EM myelinated axons 180 against 55 per field; CNP, MBP, CC1; neuronal-AAV9 rescue shown for counts, g-ratio with a residual difference, MBP, CC1). Stage and sex limits as in the pilot-design line of the arm-table notes. Correction carried: the earlier statement that axonal conduction was a closed single source was wrong (SCI, 2026-11-19).",
      "2026-11-19", "Needs a laboratory with the neuron-targeted line, a rescue arm and animal-level statistics.", "no", ""]
NK = {"F02_myelination_activity_sign": ("SCI 2026-11-19 (R1, " + R1 + "; mapped by IT): conduction in the Wwox-null brain was measured once (neuron-targeted deletion, acute slices P13 to P17, 8 slices from 5 animals against 8 from 6, graph-read N1 latency about 2.5 against 3.2 ms, "
                                         "N1/N2 ratio changed, Synapsin-Cre only, no rescue, no velocity, a control n identical to another experiment's n, Methods without a callosal protocol): a candidate readout that needs re-measurement with a rescue arm and animal-level statistics. "
                                         "Structural endpoints with demonstrated neuronal rescue exist (EM myelinated axons, CNP, MBP, CC1; g-ratio with a residual difference) and are the usable ones for an arm on this card."),
      "H02_gabaat_inactivator_myelin_exposure": ("SCI 2026-11-19 (R1, " + R1 + "; mapped by IT): for any readout of a myelin effect of a GABA-AT inactivator in a Wwox-deficient brain, the structural endpoints with demonstrated neuronal rescue (EM myelinated axons, CNP, MBP, CC1; g-ratio with a residual difference) are the usable ones; "
                                                 "conduction was measured once in the Wwox-null brain (acute slices P13 to P17, inconsistent n, no rescue, no velocity) and is a candidate readout that needs re-measurement, not an endpoint yet.")}
ARM = ("\n\nUpdate 2026-11-19 (IT59, on SCI's continuation delivery, 9c802627f; the text above is not edited; no tier change): (1) the WW1-PPxY branch ends in ONE open-question row (IT59-Q01; no package, no comparison row, no dossier): the relation is not established with primary evidence in a neural system. "
       "(2) Myelin cards F02 and H02: the STRUCTURAL myelin endpoints with neuronal-AAV9 rescue (EM myelinated axons, CNP, MBP, CC1) are usable endpoints; conduction latency is a re-measurement candidate (measured once, an n inconsistency in the legend), not an endpoint yet (IT59-Q02). "
       "(3) Pilot-design limit, stated once: the held GEO deposits record no sex, litter, cage, dissection batch or animal identifier, so any per-animal result is 'per animal, uncontrolled for sex and litter'; the same applies to the design of the two-age tissue measurement unless the laboratory records them (" + PC + "). "
       "(4) The one materials comparison (E, " + EN + "): one case; both arms reached the same decision; the verifier's primary category favoured the structured arm and its secondary category the lean arm; the structure is not credited. Hypothesis level; no dose.")
def main():
    csv.field_size_limit(10**9)
    p = DR / "batch_sci_20261105/map/open_questions_map.tsv"; rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t"))
    assert len(Q1[2]) <= 300 and len(Q2[2]) <= 300 and len(Q1[3]) <= 200 and len(Q2[3]) <= 200, (len(Q1[2]), len(Q2[2]), len(Q1[3]), len(Q2[3]))
    have = {r[0] for r in rows}
    j = [k for k, r in enumerate(rows) if r[0] == "IT57-Q01"][0]
    for q in (Q2, Q1):
        if q[0] not in have: rows.insert(j + 1, q)
    with open(p, "w", newline="", encoding="utf-8") as f: csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
    for c, txt in NK.items():
        pp = DR / f"cards/{c}.packet.json"; pk = json.loads(pp.read_text(encoding="utf-8"))
        if not any("R1_CONDUCTION_ENDPOINT" in x for x in pk["not_known"]):
            pk["not_known"].append(txt); pp.write_text(json.dumps(pk, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            out = subprocess.run(["python3", str(DR.parent.parent.parent.parent / "framework/scripts/repurposing_bridge.py"), str(pp)], capture_output=True, text=True, check=True).stdout
            (DR / f"cards/{c}.card.json").write_text(out, encoding="utf-8")
    pa = DR / (B + "ARM_TABLE_V9_NOTES_IT_20261117.md"); s = pa.read_text(encoding="utf-8")
    if "(IT59, on SCI's continuation delivery" not in s: pa.write_text(s.rstrip("\n") + ARM + "\n", encoding="utf-8")
    print("ok")
if __name__ == "__main__":
    main()
