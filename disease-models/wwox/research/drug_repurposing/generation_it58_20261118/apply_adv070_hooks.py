"""IT58 / ADV-070 (2026-11-19): SCI's stage-adjusted re-read mapped as dated lines only, in one pass (mapping only; wording is SCI's: STAGE_ADJUSTED_REREAD_RESULT_ADV070_SCI_20261119.md sections 1, 4;
ADV's instruction: dated lines, no tier change). Checked first: no cell of IT quotes the P3a Kcnq2 transcript shift as support (investigations, needs, cards, packages, open questions quote only cell-type expression and channel biophysics),
so no cell needed the 'background-confounded' qualifier. Idempotent."""
import csv
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
NOTE = "advisor_pilot_20261113/brainstorm_20261116/adv070_stage_adjusted_p3a_sci_20261119/STAGE_ADJUSTED_REREAD_RESULT_ADV070_SCI_20261119.md"
ARM = ("\n\nUpdate 2026-11-19 (IT58, on SCI's ADV-070 stage-adjusted re-read of the held P17 deposits, " + NOTE + " sections 1 and 4; the text above is not edited; no tier change): stage adjustment is NOT decisive on the held data "
       "(the covariate has little leverage in the only contrast with at least 3 per arm; cortex and hippocampus disagree for Kcnj9, Slc12a5, Grm3, Grin2c, Kcnq2). Annotations, in SCI's words: Kv7 opener probe: premise unchanged; Kcnq2 transcript lower in cortex (background-confounded, "
       "stage-adjusted shift stands in cortex only, 0 of 3 hippocampal contrasts retain it) and it is quoted only with that qualifier; the XE991-sensitive current is the measurement. Ethosuximide (T-type, GIRK1/2): 'not raised' stands. GluN2B/NMDAR cells: no transcript-level subunit support "
       "survives the covariate in more than one contrast; the isolated NMDAR current stays the measurement. Chloride layout: unchanged (KCC2 stands in cortex, about zero after adjustment in hippocampus; NKCC1 composition not addressed; a bulk transcript is not a gradient). "
       "Activity: the activity-regulated panel is lower, no activity-regulated hyper-signature at sampling, not a measure of E/I; Npy higher, background-confounded. Interneuron row: Pvalb unstable and shrinking (consistent with ADV-068), no PV-directed premise. Hypothesis level; no dose.")
RS = (" Dated 2026-11-19 (IT, on SCI's ADV-070): Pvalb is unstable under stage adjustment and shrinks in the hippocampal contrast (consistent with ADV-068); a related open question, in SCI's words: 'do PV, KCC2 and myelin move together per animal with a general late-maturation score, and before seizure onset?'; "
      "the two-age tissue measurement named in the in vivo brief (Addendum 19) is the observation that would answer it. Source: " + NOTE + ".")
Q01 = (" Dated 2026-11-19 (IT, on SCI's ADV-070): the chloride layout is unchanged by the stage adjustment (KCC2 stands in cortex, about zero after adjustment in hippocampus; NKCC1 composition not addressed; a bulk transcript is not a gradient); E_GABA in the same cells with a two-age control stays the measurement. Source: " + NOTE + ".")
csv.field_size_limit(10**9)
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"; rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t")); i = rows[0].index("status_evidence")
for r in rows[1:]:
    if r[0] == "RS-NP3A1" and "ADV-070" not in r[i]: r[i] += RS
    if r[0] == "IT57-Q01" and "ADV-070" not in r[i]: r[i] += Q01
with open(p, "w", newline="", encoding="utf-8") as f: csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
p = DR / "advisor_pilot_20261113/brainstorm_20261116/ARM_TABLE_V9_NOTES_IT_20261117.md"; s = p.read_text(encoding="utf-8")
if "on SCI's ADV-070" not in s: p.write_text(s.rstrip("\n") + ARM + "\n", encoding="utf-8")
print("ok")
