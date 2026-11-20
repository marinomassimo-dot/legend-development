"""IT59 (2026-11-20), ADV-097 item 3: HE's final ADV-096 result (parametric sensitivity, 84 cells; RESULT_PARAMETRIC_SENSITIVITY_HE_20261120) carried as one dated line on IT56-Q01 and one dated paragraph on the arm-table notes;
IT's own two cross-parameter sentences in the consumption record (section 2) are corrected in place with a dated bracket. No row added; no status change; cards and ranking inputs not edited. Idempotent."""
import csv
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
B = "advisor_pilot_20261113/brainstorm_20261116/"
REC = " Record: " + B + "adv097_consumption_it_20261119/CONSUMPTION_RECORD_ADV097_IT_20261119.md section 15."
MARK = "on HE's final parametric-sensitivity result"
Q01 = (" [IT 2026-11-20, ADV-097 consumption, " + MARK + " (84 cells: 7 baseline, 77 continuation; no ranks, no winner): the in-silico part of this row is now EXECUTED and is descriptive only: the neurosteroid-type composite arm's crossing stays within a narrow range of its tonic parameter across all 11 variants, the narrowest of the seven classes, which describes this model's sensitivity and is not evidence for the class; the same class across variants is scale-free; "
       "the variants are not re-fitted (their baseline burst counts are 0.06 to 3.05 times the baseline) and the Kv7 variants are an assumed drive offset, not a current; this is parametric sensitivity of one circuit structure, not alternative structures. The model cannot represent what the potency sheets show decides real agents (voltage dependence of pore block, competitive against uncompetitive action, kinetics), so no further simulator compute is planned for the class choice; the MEASUREMENT only an experiment supplies is unchanged." + REC + "]")
ARM = ("\n\nUpdate 2026-11-20 (IT59, " + MARK + ", ADV-096 closed; the text above is not edited; no cell, tier, origin or arm changes; hypothesis level; not medical advice): per class the crossing multiplier is reported with its bracket as numerical resolution (not a confidence interval); the same class across 11 parameter variants is scale-free; d-APV and the NMDAR pore blocker, one perturbation of one parameter in the model, are indistinguishable in all 12 variants (the published order is not a finding under any variant); comparisons between classes acting on different parameters are NOT identifiable and no class is ranked. "
       "Interpretations corrected wherever found: 'T-type last or inactive' is an explored-range result (in four lower-excitability states it crosses); a percent change of different parameters is not a potency; 'robust ordering' or 'stable across structures' is wrong (parametric sensitivity of the same equations, not alternative structures); the neurosteroid-type crossing is not a preference. Limits to carry with any number: the variants are not re-fitted; Kv7 is an assumed drive offset. No cell above is changed: C007, C011, C054, C013, C015 and C055 use the simulation only for within-arm signs.")
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"
rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t"))
i = rows[0].index("status_evidence"); j = rows[0].index("last_touched")
n = 0
for r in rows[1:]:
    if r[0] == "IT56-Q01" and MARK not in r[i]:
        r[i] += Q01; r[j] = "2026-11-20"; n += 1
with open(p, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
pa = DR / (B + "ARM_TABLE_V9_NOTES_IT_20261117.md"); s = pa.read_text(encoding="utf-8")
if MARK not in s:
    pa.write_text(s.rstrip("\n") + ARM + "\n", encoding="utf-8"); n += 1
pr = DR / (B + "adv097_consumption_it_20261119/CONSUMPTION_RECORD_ADV097_IT_20261119.md"); s = pr.read_text(encoding="utf-8")
old = "Sodium passes the NMDAR classes on the multiplier axis (-11 percent against -18 percent); T-type stays last (more than -58 percent), which is a model statement, not a statement about ethosuximide."
new = "[CORRECTED 2026-11-20, section 15: the two cross-parameter statements that stood here, 'sodium passes the NMDAR classes on the multiplier axis' and 'T-type stays last (more than -58 percent)', are NOT identifiable comparisons and 'last' is an explored-range result (T-type crosses in four lower-excitability states); they are withdrawn as findings.]"
if old in s:
    pr.write_text(s.replace(old, new), encoding="utf-8"); n += 1
print("ok", n)
