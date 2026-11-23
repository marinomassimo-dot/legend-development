"""ADV-189 (IT, 2026-11-23): one optional design clause appended to the WO-07 status_evidence, old text kept; idempotent (marker 'ADV-189').
Wording: Codex return 30 (REPLY_30_CODEX.md), as relayed by ADV, which replaces SCI's earlier clause. The INV-07 explanations row is NOT touched (it feeds the views).
Run from the repository root. Hypothesis level, no dose, reference genotype class only; no arm, ranking, compound or direction change."""
from pathlib import Path

DR = Path("disease-models/wwox/research/drug_repurposing")
CL = (" [ADV-189 with Codex return 30, 2026-11-23, optional design clause; adjacent mouse neuron and HEK preparation, no WWOX direction] "
      "Reduced pyruvate oxidation or ATP leaves the limiting step unresolved. Matrix pyruvate dynamics reflect net entry minus utilization and any efflux. "
      "Attribute the deficit to entry or PDH only if the two sides can be separated in matched preparations by calibrated, orthogonal measurements or perturbations, with target engagement, suitable precision and biological replication. "
      "Identify entry using an independently qualified transport-sensitive contrast, and PDH using directly measured active enzyme or state preserved at sampling. "
      "If attribution rests on a plateau or net slope alone, or if an entry control and a utilization control produce overlapping responses, record indeterminate. "
      "A normal net slope cannot establish normal import; a PDH-side control must have its direction checked against active PDH (raising activity with a PDK inhibitor and lowering it are opposing perturbations and cannot both be assumed to raise the pyruvate pool); "
      "a missing rise can also reflect a real change in compensation or limited dynamic range; ATP and oxidation can corroborate function. "
      "In the adjacent source (Tiwari 2024, PMID 39546604, Fig 2) a matrix pyruvate reporter responds in a carrier-dependent way under the tested conditions; it is not validated against a PDH, PDK or consumption perturbation. "
      "Source: advisor_pilot_20261113/brainstorm_20261116/adv189_tiwari_pyruvate_sensor_sci_20261123/RESULT_ADV189_TIWARI_PYRUVATE_SENSOR_SCI_20261123.md]")
PTR = (" [ADV-190 pointer, 2026-11-23, weak, contained source pointer (SCI NARROW; not a PDH discriminator): Arce-Molina et al. 2020 (eLife, PMID 32142409; mouse cortical astrocyte cultures, room temperature): matrix pyruvate by PyronicSF; "
       "initial accumulation (about 69% inhibited by UK-5099) and depletion after the block are read as separate rates, and the depletion rate moves reversibly with an uncoupler (up about 3.4 times) and azide (down to about 0.39) in the same cells. "
       "The depletion is a lower bound on aggregate net utilization under a partial block, with efflux unaddressed, no pH control reported for the respiratory challenges, replicates counted as cells, and no PDH-side perturbation; it is not a PDH flux. "
       "Source: advisor_pilot_20261113/brainstorm_20261116/adv190_arce_molina_pyronicsf_depletion_sci_20261123/RESULT_ADV190_ARCE_MOLINA_PYRONICSF_DEPLETION_SCI_20261123.md]")
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"
L = p.read_text(encoding="utf-8").split("\n"); h = L[0].split("\t"); n = 0
for i, l in enumerate(L):
    f = l.split("\t")
    if i and len(f) == len(h) and f[0] == "WO-07" and "ADV-189" not in f[h.index("status_evidence")]:
        f[h.index("status_evidence")] += CL
        f[h.index("last_touched")] = max(f[h.index("last_touched")], "2026-11-23")
        L[i] = "\t".join(f); n += 1
p.write_text("\n".join(L), encoding="utf-8")
L = p.read_text(encoding="utf-8").split("\n"); m = 0
for i, l in enumerate(L):
    f = l.split("\t")
    if i and len(f) == len(h) and f[0] == "WO-07" and "ADV-190" not in f[h.index("status_evidence")]:
        f[h.index("status_evidence")] += PTR; L[i] = "\t".join(f); m += 1
p.write_text("\n".join(L), encoding="utf-8")
print("WO-07", n, "pointer", m)
