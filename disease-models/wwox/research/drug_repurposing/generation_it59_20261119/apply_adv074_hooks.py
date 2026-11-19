"""IT59 / ADV-074 (2026-11-19): SCI's glucose and metabolic axis first pass mapped in ONE pass (mapping only; wording is SCI's note and the R4 report as delivered; no tier change; no new comparison).
(1) one open-question row; (2) NEED-SYSTEMIC-GLYCAEMIA-GROWTH counter_evidence item (qualification only); (3) E04 packet not_known item, card rebuilt by repurposing_bridge.py (U15 reads the card);
(4) the arm-table dated line (decision: an optional glucose series tied to seizure timing in the pup brief, not a diet or glucose arm). Idempotent."""
import csv, json, subprocess
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
B = "advisor_pilot_20261113/brainstorm_20261116/"
H = B + "h_glucose_axis_adv074_sci_20261119/GLUCOSE_METABOLIC_AXIS_FIRST_PASS_ADV074_SCI_20261119.md"
R4 = B + "h_glucose_axis_adv074_sci_20261119/R4_READING_REPORT_AS_DELIVERED.md"
Q4 = ["IT59-Q04", H,
      "Does hypoglycaemia or another metabolic state drive excitability, seizures and death in the Wwox-null pup, or only accompany them? (glucose in the S-KO and N-KO lines, glucose with same-animal EEG/ECoG from P9, a restoration arm without WWOX restoration, ketone, lactate, insulin by age)",
      "Whether a glucose measurement series enters the pup design (optional, tied to seizure timing); the metabolic lever stays out of the comparison set.",
      "wet_lab_measurement", "OPEN", "main",
      "[IT 2026-11-19, mapped from SCI's ADV-074 first pass, note " + H + " and R4 report as delivered] SCI's wording in full: 'Does hypoglycaemia or another metabolic state drive excitability, seizures and death in the Wwox-null pup, or only accompany them? Separating measurements: glucose in the S-KO and N-KO seizure-and-death lines (never reported), "
      "glucose at seizure time with same-animal EEG/ECoG from P9, a glucose-restoration arm without WWOX restoration, ketone/lactate/insulin by age and milk intake (none measured in any held original).' The held originals cannot answer it: no original manipulates glucose; the neuronal rescues normalise glucose, growth, seizures and survival together (a central origin of the hypoglycaemia, not glucose as the cause of seizures); no glucose before P10 although the neuron-targeted deletion seizes from P9; "
      "no glucose at the time of any seizure; ECoG starts at P14. Access: the lde/lde rat original is not held or recoverable (the receipt cites two absent files). Stop rule as written by ADV is not met (age-resolved glucose beyond P10 exists, the link to seizure timing does not): the axis is not closed.",
      "2026-11-19", "Needs a laboratory with the seizure-and-death lines and same-animal glucose and EEG or ECoG; the rat original needs a supply path.", "no", ""]
CE = ("SCI 2026-11-19 (ADV-074, in the held originals only; wording supplied by SCI, mapped here by IT; " + H + " and " + R4 + "): this need carries the 2026 values only and omitted (a) the 2009 germline-null table (Ludes-Meyers 2009, P18 survivors: glucose 143.5 ± 8.8, n = 4, against heterozygote 227.0 ± 11.7, n = 3, and wild type 250.6 ± 5.0, n = 3; "
      "units and the test not named in the text; text only) and (b) the 2021 gene-therapy statement ('hypoglycemic from the second week'; the Appendix glucose panels are not held, so text only). Limits: the held originals do not show that hypoglycaemia drives seizures and death rather than accompanies them (the neuronal rescues normalise glucose, growth, seizures and survival together: a central origin, not a cause); "
      "no glucose before P10 although seizures start at P9 in the neuron-targeted deletion; none at seizure time. Dissociations: death with near-normal glucose (low-dose neuronal vector, glucose measured at P30; the cytomegalovirus-promoter vector, glucose normal at P14 ONLY, so 'glucose normalises while animals die' is half-supported); "
      "seizures without documented hypoglycaemia (P47T adults, neuron-targeted deletion where glucose was never measured). Peripheral arm: the skeletal-muscle conditional knockout gives the OPPOSITE sign in adults (fasting hyperglycaemia, insulin resistance, higher lactate, lower muscle FDG uptake), with no seizure or survival data; it does not explain the pup hypoglycaemia.")
NK = ("SCI 2026-11-19 (ADV-074, " + H + "; mapped by IT): the card's evidence is clinical and tiny with no metabolic readout in any WWOX-deficient neural system; on the held originals its rationale neither gains nor loses decisively: it would gain plausibility (an alternative brain fuel) only if hypoglycaemia or glucose use contributes to excitability, which nothing shows, "
      "and it would reduce to a generic anticonvulsant action if seizures occur with normal glucose (the P47T adults and the neuron-targeted line suggest they may). A diet that lowers blood glucose would act on pups that are already hypoglycaemic from about P10 and die: whether it helps or harms is unknown (a hypothesis-level caution, not advice). No change of tier.")
ARM = ("\n\nUpdate 2026-11-19 (IT59, on SCI's ADV-074 glucose and metabolic axis first pass, " + H + "; the text above is not edited; no tier change): the held originals do not show whether hypoglycaemia drives seizures and death or only accompanies them. Decision it changes: a glucose measurement series enters the pup design as an OPTIONAL addition tied to seizure timing "
       "(glucose in the seizure-and-death lines, glucose at seizure time with same-animal EEG or ECoG, ketone, lactate and insulin by age), not a diet or a glucose arm; the metabolic lever stays out of the comparison set (U15, the ketogenic row, WEAK, unchanged). Correction carried: for the cytomegalovirus vector glucose was measured at P14 only. Open question IT59-Q04. Hypothesis level; no dose.")
def main():
    csv.field_size_limit(10**9)
    assert len(Q4[2]) <= 300 and len(Q4[3]) <= 200, (len(Q4[2]), len(Q4[3]))
    p = DR / "batch_sci_20261105/map/open_questions_map.tsv"; rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t"))
    if Q4[0] not in {r[0] for r in rows}:
        j = [k for k, r in enumerate(rows) if r[0] == "IT59-Q03"][0]; rows.insert(j + 1, Q4)
    with open(p, "w", newline="", encoding="utf-8") as f: csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
    p = DR / "needs/needs.json"; raw = p.read_text(encoding="utf-8"); d = json.loads(raw); items = d if isinstance(d, list) else d["needs"]
    n = [x for x in items if x["id"] == "NEED-SYSTEMIC-GLYCAEMIA-GROWTH"][0]
    if not any("ADV-074" in c for c in n["counter_evidence"]):
        n["counter_evidence"].append(CE); p.write_text(json.dumps(d, indent=1, ensure_ascii=False), encoding="utf-8")
    pp = DR / "cards/E04_ketogenic_lactate_axis.packet.json"; pk = json.loads(pp.read_text(encoding="utf-8"))
    if not any("ADV-074" in x for x in pk["not_known"]):
        pk["not_known"].append(NK); pp.write_text(json.dumps(pk, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        out = subprocess.run(["python3", str(DR.parent.parent.parent.parent / "framework/scripts/repurposing_bridge.py"), str(pp)], capture_output=True, text=True, check=True).stdout
        (DR / "cards/E04_ketogenic_lactate_axis.card.json").write_text(out, encoding="utf-8")
    pa = DR / (B + "ARM_TABLE_V9_NOTES_IT_20261117.md"); s = pa.read_text(encoding="utf-8")
    if "on SCI's ADV-074 glucose" not in s: pa.write_text(s.rstrip("\n") + ARM + "\n", encoding="utf-8")
    print("ok")
if __name__ == "__main__":
    main()
