"""IT59 / ADV-076 (2026-11-19): SCI's deletion-completeness and Olig2-against-Mbp note mapped in ONE pass (mapping only; wording is SCI's note; no tier change; the frozen ADV-068 to ADV-070 criteria are not rewritten).
(1) NEED-INHIBITORY-HYPOFUNCTION counter_evidence item; (2) RS-NP3A1 dated line; (3) the arm-table dated line (per-animal, per-region protein-level deletion completeness in the pilot description; the Olig2 and Mbp reading; the supply item). Idempotent."""
import csv, json
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
B = "advisor_pilot_20261113/brainstorm_20261116/"
N = B + "i_deletion_completeness_olig2_adv076_sci_20261119/DELETION_COMPLETENESS_AND_OLIG2_ADV076_SCI_20261119.md"
CE = ("SCI 2026-11-19 (ADV-076, bulk P17 deposits; wording supplied by SCI, mapped here by IT; " + N + "): in the cortex contrast behind ADV-068 one of the three knockout animals (KO3: Wwox 9.0 TPM, 48 percent of the control mean) lies inside the control range (8.0 to 26.5) and its PV and late-set values lie inside the control range too; "
      "across the three animals the PV signature orders with residual Wwox (residual 20, 27, 48 percent give -0.95, -0.72, -0.29); the late set does not order strictly; stage score and deletion depth cannot be separated at n = 3. Residual bulk Wwox is not deletion completeness (control cortex expresses about five times the hippocampal Wwox; non-neuronal expression stays). "
      "Sensitivity, not the primary: without KO3, two knockouts remain (below the three-animal threshold). The decision is unchanged: no PV-specific premise from these transcripts.")
RS = (" Dated 2026-11-19 (IT, on SCI's ADV-076): the per-animal PV contrast contains one knockout animal with Wwox inside the control range (KO3, 48 percent residual) and the PV signature orders with residual Wwox across the three animals; stage and deletion depth are not separable at n = 3. "
      "The measurement that would settle the cell-level question must record deletion completeness per animal and per region at the protein level (immunostaining or a per-slice check); a transcript residual is not a substitute. Source: " + N + ".")
ARM = ("\n\nUpdate 2026-11-19 (IT59, on SCI's ADV-076, " + N + "; the text above is not edited; no tier change): (1) Pilot-design description: do not assume a Synapsin-Cre deletion is uniform across regions and animals; record deletion completeness per animal and per region at the PROTEIN level (immunostaining or a per-slice check) and report every effect against it; "
       "a transcript residual is not a substitute (bulk P17 deposits: one knockout animal inside the control range for Wwox; the PV signature orders with residual Wwox; stage and deletion depth not separable at n = 3). "
       "(2) Olig2 counts against Mbp area (Hussain 2023, P47T knock-in): the audit item is NOT a usable dissociation (cross-region: Olig2 counted in the corpus callosum with n = 3 mice and regions as units, Mbp stained in the parietal cortex, its supplement not held); it supports only 'fewer Olig2-positive cells in the callosum at two adult ages' as a composition caveat for any P47T bulk readout, not 'oligodendrocytes lost without hypomyelination'; "
       "the structural myelin endpoints of the myelin cards are unchanged. (3) Supply list: the Hussain 2023 supplement (Mbp panels and tables) is the one item that would settle the Mbp side. Hypothesis level; no dose.")
csv.field_size_limit(10**9)
p = DR / "needs/needs.json"; raw = p.read_text(encoding="utf-8"); d = json.loads(raw); items = d if isinstance(d, list) else d["needs"]
n = [x for x in items if x["id"] == "NEED-INHIBITORY-HYPOFUNCTION"][0]
if not any("ADV-076" in c for c in n["counter_evidence"]):
    n["counter_evidence"].append(CE); p.write_text(json.dumps(d, indent=1, ensure_ascii=False), encoding="utf-8")
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"; rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t")); i = rows[0].index("status_evidence")
for r in rows[1:]:
    if r[0] == "RS-NP3A1" and "ADV-076" not in r[i]: r[i] += RS
with open(p, "w", newline="", encoding="utf-8") as f: csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
pa = DR / (B + "ARM_TABLE_V9_NOTES_IT_20261117.md"); s = pa.read_text(encoding="utf-8")
if "(IT59, on SCI's ADV-076" not in s: pa.write_text(s.rstrip("\n") + ARM + "\n", encoding="utf-8")
print("ok")
