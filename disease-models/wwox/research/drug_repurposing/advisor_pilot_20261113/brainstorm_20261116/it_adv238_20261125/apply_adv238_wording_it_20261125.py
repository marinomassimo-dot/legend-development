"""ADV-238 (IT, 2026-11-25, wording only, no number changed): applies SCI's ADV-233 leave-two-out result to the ordinary-route consumers:
 (a) IT6 P4 README row 5 (dated bracket inside the Result cell);
 (c) IT12 README: the K01/L01 table row (line 15) and the K01 and L01 paragraphs of section 6 (dated Update lines appended);
 (e) one dated line on map row ADV228-Q01 (the duplicate check searched genes, not animal ids; the lesson for any per-animal claim).
Registry, card and dossier consumers go through the candidate CC-20261125-ORCHESTRATOR-ADV238-P47T-TWO-ANIMALS-01.md, not here.
Idempotent (one marker each). Run from the repository root."""
import csv
from pathlib import Path
DR = Path("disease-models/wwox/research/drug_repurposing")
R233 = "advisor_pilot_20261113/brainstorm_20261116/adv233_p47t_two_animals_sci_20261125/RESULT_ADV233_P47T_TWO_ANIMALS_SCI_20261125.md"
n = 0
def edit(path, old, new, marker):
    global n
    t = path.read_text(encoding="utf-8")
    if marker in t:
        return
    assert t.count(old) == 1, (path, t.count(old), old[:60])
    path.write_text(t.replace(old, new), encoding="utf-8"); n += 1
# (a) IT6 README row 5
edit(DR / "partial_benefit_it6_p10_20261029/README.md",
     "ADV-233 tests the other carried signatures] |",
     "ADV-233 tests the other carried signatures] [ADV-233, 2026-11-25 (SCI, leave-two-out): the TNFA and IL6/JAK/STAT3 hallmark enrichments do not survive removal of M6 and F8, the two animals that also carry the activity-gene surge (IT12 premises P8, 2026-10-31); "
     "read as a state of two of five mutants, not as a genotype-wide inflammatory signature; the authors' upstream-regulator tool itself was not re-run; GLYCOLYSIS is robust to the removal] |",
     "[ADV-233, 2026-11-25 (SCI, leave-two-out)")
# (c) IT12 README
p = DR / "p47t_it12_20261031/README.md"
edit(p, "H-glia (composition). **L01: nothing changes** in selection or priority; a datum is added (modest NRF2-target increase, composition-confounded). |",
     "H-glia (composition). **L01: nothing changes** in selection or priority; a datum is added (modest NRF2-target increase, composition-confounded). [Update 2026-11-25, ADV-233 (SCI, leave-two-out, details in section 6): see the dated lines under K01 and L01 below.] |",
     "[Update 2026-11-25, ADV-233 (SCI, leave-two-out, details in section 6)")
edit(p, "No change of research priority is proposed. Candidate text is in `proposals/`.",
     "No change of research priority is proposed. Candidate text is in `proposals/`. "
     "[Update 2026-11-25, ADV-233 (SCI, leave-two-out; " + R233 + "): GLYCOLYSIS enrichment survives removal of M6 and F8 in all three forebrain regions; HYPOXIA survives only in hippocampus; the TNFA and IL6/JAK/STAT3 enrichments do not survive in any region. Wording only, no number above changes.]",
     "[Update 2026-11-25, ADV-233 (SCI, leave-two-out; advisor_pilot_20261113/brainstorm_20261116/adv233")
edit(p, "Cerebellar ROS hallmark: leading edge is antioxidant enzymes plus myelin genes.",
     "Cerebellar ROS hallmark: leading edge is antioxidant enzymes plus myelin genes. [Update 2026-11-25, ADV-233 (SCI, leave-two-out): the NRF2_5 'up' reading in hippocampus falls below the rule without M6 and F8 (+0.26, p 0.089); read as not resolvable, not as absent.]",
     "[Update 2026-11-25, ADV-233 (SCI, leave-two-out): the NRF2_5")
# (e) map row ADV228-Q01
MAP = DR / "batch_sci_20261105/map/open_questions_map.tsv"
MARK = "[IT 2026-11-25 ADV-238"
LINE = (" [IT 2026-11-25 ADV-238, lesson for any per-animal claim: the duplicate checks of ADV-231 and ADV-233 searched gene names, not animal identifiers, and so missed that IT12 premises P8 (2026-10-31) already named M6 and F8; "
        "before quoting or building on a bulk-tissue pathway inference, search the animal ids and run leave-flagged-animals-out. Consumers reworded: " + "brainstorm_20261116/it_adv238_20261125/RESULT_ADV238_IT_20261125.md" + ".]")
rows = list(csv.reader(open(MAP, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]
for r in rows[1:]:
    if r[0] == "ADV228-Q01" and MARK not in r[h.index("status_evidence")]:
        r[h.index("status_evidence")] += LINE; r[h.index("last_touched")] = "2026-11-25"; n += 1
with open(MAP, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("edits", n)
