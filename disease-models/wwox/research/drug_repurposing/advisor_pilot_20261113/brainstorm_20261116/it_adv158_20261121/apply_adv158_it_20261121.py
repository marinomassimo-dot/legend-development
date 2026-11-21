"""ADV-158 (IT, 2026-11-21): consumer-gap fixes found by the check of ADV-156's delta. Old text is kept; every edit is an appended dated line or the
replacement of an 'unknown' cell by its content with source; idempotent (marker 'ADV-158' in the added text).

1. The Kv7 'effective and harmful exposures overlap' wording of ADV-156 (selection note, opportunity map OPP-05 chain notes, state table row) is stronger than the
   source: repeated-dose exposure was not measured and the apoptosis tests are one-tailed and uncorrected (HE batch 2 sheet, three dated lines, SCI ADV-119).
2. The funding view printed safety_cell 'unknown' for OPP-01 and OPP-05 while the state table held content; OPP-03's cell gets the symmetric statement for ethosuximide.
3. The state table rows for ethosuximide and the Kv7 openers carry the dated qualification.
Run from the repository root:  python3 disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_adv158_20261121/apply_adv158_it_20261121.py
Hypothesis level, no dose, reference genotype class only; the compound ranking does not change."""
import sys
from pathlib import Path

DR = Path("disease-models/wwox/research/drug_repurposing")
BS = DR / "advisor_pilot_20261113/brainstorm_20261116"
MARK = "ADV-158"
SHEET = "advisor_pilot_20261113/adv098_agent_sheets_he_20261119/BATCH2_Kv7_ezogabine_azetukalner_ICA069673_XE991_HE_20261119.md"
RES = "advisor_pilot_20261113/brainstorm_20261116/it_adv158_20261121/ADV158_TWO_COMPARISONS_AND_CONSUMER_CHECK_IT_20261121.md"

KV7 = ("Qualification of 'overlap' (IT, ADV-158): the held juvenile-rat paper (Brown 2016, PMID 26865186; read at passage level by SCI, qualified by SCI's ADV-119 result, as written on the Kv7 sheet " + SHEET + ") gives single-dose pup total brain values of 330, 1296 and 2013 ng/ml at 5, 15 and 30 mg/kg "
       "(1.09, 4.27 and 6.64 microM on SCI's 1 ml per g assumption; the time point is not in the text read) and apoptosis after repeated dosing in 5 of 8 regions, with one-tailed a priori tests, no correction across regions, males only, the striatum not assessable, and "
       "repeated-dose exposure NOT measured (the authors infer it did not exceed the 30 mg/kg single-dose level). So 'overlap' is an inference from a single-dose exposure and a repeated-dose harm, not a measured margin; the adult mouse effective brain values (2.23 and 3.58 microM, two experiments) come from another species and age. "
       "The Kv7 penalty stands for the reason the ADV-156 line gave first: no margin has been measured in juveniles. Result file: " + RES + ".")
OPP05_SAFETY = ("Dated 2026-11-21 (IT, ADV-158; source: HE batch 2 sheet with SCI's ADV-119 limits, not re-read by IT): juvenile rat P7, repeated dosing: apoptosis in 5 of 8 brain regions (one-tailed, uncorrected, males; repeated-dose exposure not measured); "
                "single-dose pup total brain 1.09, 4.27 and 6.64 microM at three rodent research levels; no mouse juvenile value; no label read here; state table: it_adv156_20261121/agent_states_it_adv156_20261121.tsv, row retigabine and azetukalner")
OPP01_SAFETY = ("Dated 2026-11-21 (IT, ADV-158; source: HE batch 5 sheet, openFDA label text, not re-read by IT): label states safety and effectiveness not established below 18 years, a potent in vitro displacement of bilirubin with sera from critically ill neonates, "
                "and a boxed warning on profound diuresis; brain penetration is transporter-limited (titles); state table: it_adv156_20261121/agent_states_it_adv156_20261121.tsv, row bumetanide")
OPP03_ADD = ("[Dated 2026-11-21, IT, ADV-158: developing-brain harm for ethosuximide was searched by two routes (PubMed title and abstract field-tagged: three hits, none on a developing brain; Bittigau 2002 abstract, PMID 12417760, names phenytoin, phenobarbital, diazepam, clonazepam, vigabatrin and valproate and does not name ethosuximide; its full text was not reached, PMC sent none). "
             "That is a search result, not a statement that ethosuximide is harmless to a developing brain; it makes the comparison with the Kv7 opener asymmetric in what was measured, not in margin.]")
ETX_ADD = (" [Dated 2026-11-21 ADV-158: the 134.9 microg/g value is the saline arm of an ethosuximide-plus-sildenafil ED50 experiment and its unit (per g tissue or per g of a 1:2 homogenate) is not settled by the text (ADV-122, via the sheet); the harm cell is the label limit plus a searched-not-found developing-brain result (two routes), not a measured margin.]")
KV7_ROW = (" [Dated 2026-11-21 ADV-158: exposure is single-dose total brain (330, 1296, 2013 ng/ml at 5, 15, 30 mg/kg; time point not in the text read); the harm cell 'overlap' is an inference: apoptosis was seen after repeated dosing whose exposure was not measured (SCI ADV-119 limits).]")


def append(path, text, heading=None):
    p = Path(path)
    t = p.read_text(encoding="utf-8")
    if MARK in t:
        return "already"
    if not t.endswith("\n"):
        t += "\n"
    p.write_text(t + "\n" + (heading + "\n" if heading else "") + text + "\n", encoding="utf-8")
    return "appended"


def edit_cell(path, match, col, fn):
    p = Path(path)
    lines = p.read_text(encoding="utf-8").split("\n")
    head = lines[0].split("\t")
    n_done = 0
    for n, ln in enumerate(lines):
        f = ln.split("\t")
        if n and len(f) == len(head) and all(f[head.index(k)].startswith(v) if k == "agent" else f[head.index(k)] == v for k, v in match.items()):
            i = head.index(col)
            new = fn(f[i])
            if new != f[i]:
                f[i] = new
                lines[n] = "\t".join(f)
                n_done += 1
    if not n_done:
        return "unchanged"
    p.write_text("\n".join(lines), encoding="utf-8")
    return f"{n_done} cell(s)"


def add(text):
    return lambda s: s if MARK in s else (s + text)


def replace_unknown(text):
    return lambda s: text if s == "unknown" else s


def main():
    out = []
    sel = BS / "generative_engine_funding_adv_20261119/SELECTION_NOTE_V1_ADV_20261119.md"
    out.append(("selection note", append(sel, "- " + KV7, "## Dated qualification (IT, 2026-11-21, ADV-158): the word 'overlap' in demotion 2 and in the Kv7 row of the updated comparison (the text above is unchanged; no compound ranking changes)")))
    opp = BS / "generative_engine_funding_adv_20261119/it_adv092_20261119/opportunities.tsv"
    out.append(("OPP-05 chain_notes", edit_cell(opp, {"opp_id": "OPP-05"}, "chain_notes", add(" [Dated 2026-11-21, IT, ADV-158: " + KV7 + "]"))))
    out.append(("OPP-05 safety_cell", edit_cell(opp, {"opp_id": "OPP-05"}, "safety_cell", replace_unknown(OPP05_SAFETY))))
    out.append(("OPP-01 safety_cell", edit_cell(opp, {"opp_id": "OPP-01"}, "safety_cell", replace_unknown(OPP01_SAFETY))))
    out.append(("OPP-03 safety_cell", edit_cell(opp, {"opp_id": "OPP-03"}, "safety_cell", add(" " + OPP03_ADD))))
    st = BS / "it_adv156_20261121/agent_states_it_adv156_20261121.tsv"
    out.append(("state row ethosuximide", edit_cell(st, {"agent": "ethosuximide"}, "exposure_basis", add(ETX_ADD))))
    out.append(("state row Kv7 exposure", edit_cell(st, {"agent": "retigabine"}, "exposure_basis", add(KV7_ROW))))
    out.append(("state row Kv7 harm", edit_cell(st, {"agent": "retigabine"}, "harm_basis", add(" [Dated 2026-11-21 ADV-158: see the exposure basis; 'overlap' is an inference, not a measured margin.]"))))
    short = ("Dated qualification (IT, 2026-11-21, ADV-158; the text above is unchanged): 'effective and harmful exposures overlap' for the Kv7 openers is an inference from a single-dose pup exposure and a repeated-dose harm whose exposure was not measured (one-tailed uncorrected tests; SCI ADV-119); no margin is measured. See " + RES + ".")
    out.append(("ADV-154 contribution", append(BS / "predictive_brainstorm_20261121/CONTRIBUTION_IT_ADV154_20261121.md", short)))
    out.append(("SCI unit C", append(BS / "adv095_selection_sci_20261119/UNIT_C_BRIDGE_COMPARATIVE_CASE_ADV095_SCI_20261120.md", short, "## Dated line (IT, 2026-11-21, ADV-158)")))
    mp = DR / "batch_sci_20261105/map/open_questions_map.tsv"
    out.append(("map IT56-Q14 evidence", edit_cell(mp, {"qid": "IT56-Q14"}, "status_evidence", add(" [IT 2026-11-21, ADV-158: the Kv7 'effective and harmful exposures overlapping' of this row is an inference, not a measured margin (repeated-dose exposure not measured; one-tailed uncorrected tests); no status change. " + RES + "]"))))
    out.append(("map IT56-Q14 touched", edit_cell(mp, {"qid": "IT56-Q14"}, "last_touched", lambda s: "2026-11-21" if s < "2026-11-21" else s)))
    rd = BS / "it_adv156_20261121/README.md"
    out.append(("ADV-156 README", append(rd, "Dated correction (IT, 2026-11-21, ADV-158; the text above is unchanged): the harm cell 'overlap' for the Kv7 openers and the three demotion lines are qualified in " + RES + ": overlap is an inference (repeated-dose exposure not measured), and the funding view's safety cells for OPP-01 and OPP-05 now carry the state table's content.")))
    for k, v in out:
        print(f"{k:26s} {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
