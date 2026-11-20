"""IT59 (2026-11-20): dated lines on the open-questions map for the FOURTH packet change (HE ADV-098 batch 11 with its two dated corrections, SCI's T-type comparison): WO-24 (T-type involvement: what the compound-level material
adds, class level, nothing about WWOX) and WO-20 (the ethosuximide reproducibility design: the within-document ethosuximide arm of another assay is not a contrast). Lines are appended, never rewritten; no row is closed. Idempotent."""
import csv
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
REC = " Record: advisor_pilot_20261113/brainstorm_20261116/adv097_consumption_it_20261119/CONSUMPTION_RECORD_ADV097_IT_20261119.md section 24."
D = {
 "WO-24": ("T-type compound-level sheet (HE batch 11",
  " [IT 2026-11-20, T-type compound-level sheet (HE batch 11 with its two dated corrections) and SCI's comparison consumed at class level, not WWOX evidence: the T-type rows of the three selective agents are one origin each and no two agents are tested in one assay, so potency, state dependence and exposure do not order them and ethosuximide stays the anchor; the one within-document ethosuximide arm of another assay (adult mouse atypical absence, a crossover) gives equal percentage reductions from separate comparisons against vehicle and is NOT a direct contrast; ulixacaltamide shows sedation at higher doses in adult rats and a kindling-progression delay without suppression in fully kindled rats; apinocaltamide's comparator in the 2025 abstract is unread; no brain concentration of any selective agent was found by these routes. None of this measures a T-type current, a burst or a Cav3 contribution in a Wwox-deficient system: this question stays OPEN." + REC + "]"),
 "WO-20": ("within-document ethosuximide arm of another assay",
  " [IT 2026-11-20, a within-document ethosuximide arm of another assay (adult mouse atypical absence, ethosuximide and ulixacaltamide in one crossover) is now held at class level: it shows ethosuximide effective in that model in adult mice and gives no contrast with a selective blocker; on IT's reading it is not a reproduction of the Wwox late-phase result and adds nothing about genotype specificity." + REC + "]"),
}
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"
rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t"))
i = rows[0].index("status_evidence"); j = rows[0].index("last_touched")
n = 0
for r in rows[1:]:
    if r[0] in D:
        mark, text = D[r[0]]
        if mark not in r[i]:
            r[i] += text; r[j] = "2026-11-20"; n += 1
with open(p, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("ok", n)
