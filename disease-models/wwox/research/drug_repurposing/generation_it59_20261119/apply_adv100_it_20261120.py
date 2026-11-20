"""IT59 (2026-11-20), ADV-097 item 3: SCI's ADV-100 (interactome round and second-system check; adv100_interactome_second_system_sci_20261120) carried as dated lines on WO-21 (GSK-3 / lithium, INV-09) and WO-27 (the broad hub).
Wording fixed by ADV: GSK-3 weakened at transcript level, partly rescued at protein level by an interaction and a pS9 direction in tension: said exactly that and no more. Class-level; no row added; cards, units and the claim registry not edited
(the registry wording is a separate correction candidate through the batch route). Idempotent."""
import csv
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
REC = " Record: advisor_pilot_20261113/brainstorm_20261116/adv097_consumption_it_20261119/CONSUMPTION_RECORD_ADV097_IT_20261119.md section 14."
MARK = "on SCI's ADV-100"
D = {
 "WO-21": (" [IT 2026-11-20, ADV-097 consumption, " + MARK + " (interactome round; one row re-read at source by a blind verifier): GSK-3 is WEAKENED at transcript level (unit A) and PARTLY RESCUED at protein level by an interaction and a pS9 direction in tension. "
           "The held literature has ONE partner meeting the three registered criteria, GSK3-beta: a residue-mapped docking motif in the SDR domain with a loss-of-binding point mutant, a functional readout in a retinoic-acid-differentiated neuroblastoma line (not neurons of a Wwox-deficient animal), pharmacology at abstract level; narrowings from the blind check: directness NOT established (lysate pull-down and co-immunoprecipitation, no purified binding), the S9-independence is NOT supported as worded (a correlation across differentiation), and the one pS9 observation in Wwox-null brain points the other way (lower pS9, representative blot, n not stated): the sources are in tension; GSK-3 activity itself is unmeasured in any Wwox-deficient neuron. Lithium alone still cannot separate a GSK-3 route from a general effect. "
           "IN-SILICO part: exhausted on the held literature. MEASUREMENT only an experiment supplies: a GSK-3 premise panel (substrate phosphorylation of tau, active-site Tyr216 and Ser9 with total GSK-3, beta-catenin), per animal, in the tissue the v2 broad experiment already collects (no extra animal): no elevation closes the GSK-3 candidate for this model; elevation, read with its pS9 pattern, opens a GSK-3-inhibitor arm of non-lithium chemistry. Cards G01 and D02 and units U24 and U11 are not edited; the registry wording is a separate correction candidate (batch route)." + REC + "]"),
 "WO-27": (" [IT 2026-11-20, ADV-097 consumption, " + MARK + ": the broad objective now has TWO named candidates with DIFFERENT premises, NOT ranked: the oligodendrocyte-lineage class (a downstream consequence, transcript-level premise, tested by the v2 head-to-head) and GSK-3 inhibition of non-lithium chemistry (an upstream, protein-level premise with a documented but not direct interaction, see WO-21). "
           "ADV's earlier stop rule ('if the interactome stops, the oligodendrocyte-class experiment stands') did not trigger because the interactome did not stop. A third human neural system (shRNA in neural stem cells and neurons, ONE library per condition) gives NO second-system support: every pair and triple count equals its permutation null and gene-level agreement with the other systems is near zero; it is not a replicated test and cannot exclude a small shared effect. The shared discriminator is the GSK-3 premise panel in the tissue of the v2 broad experiment (WO-21); it changes no v2 arm." + REC + "]"),
}
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"
rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t"))
i = rows[0].index("status_evidence"); j = rows[0].index("last_touched")
n = 0
for r in rows[1:]:
    if r[0] in D and MARK not in r[i]:
        r[i] += D[r[0]]; r[j] = "2026-11-20"; n += 1
with open(p, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("ok", n)
