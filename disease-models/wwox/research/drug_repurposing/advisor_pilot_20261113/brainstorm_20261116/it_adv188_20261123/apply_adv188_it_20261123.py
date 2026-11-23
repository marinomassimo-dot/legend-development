"""ADV-188 (IT, 2026-11-23): one optional wording clause appended to the WO-17 status_evidence, old text kept; idempotent (marker 'ADV-188').
Wording: SCI's ADV-188 clause as refined by Codex return 29 (relayed by ADV, which asked IT to replace its earlier 00:20Z clause): a baseline deficit is judged on the
direct, blocker-defined measure and its precision, not on a drug-by-group interaction. Run from the repository root.
Hypothesis level, no dose, reference genotype class only; no arm, ranking, compound or direction change."""
from pathlib import Path

DR = Path("disease-models/wwox/research/drug_repurposing")
CL = (" [ADV-188 with Codex return 29, 2026-11-23, optional wording; adjacent mouse thalamic Kcnq3 model; one concentration; test-design logic only] "
      "A small or undetected opener response describes the measured endpoint under the tested conditions. Assess a baseline M-current deficit independently with the absolute, blocker-defined current before applying the opener. "
      "A sufficiently precise baseline comparison can rule out a deficit of a specified size in the tested preparation. Assess drug response separately from within-sample changes and a direct between-group comparison, "
      "retaining absolute units, matched age and relevant starting state and treating the animal as the biological replicate. A missing drug-by-group interaction, or a pair of within-group p-values, does not rule out a baseline deficit. "
      "Keep absolute baseline, opener increment and firing as distinct quantities, and do not imply that voltage-clamp and current-clamp measures came from the same cells (the source's counts differ). "
      "In the adjacent model the genotype shows a reduction of a target subunit, not the size of the available Kv7 pool or the drug-free current; no thalamic age, firing direction or Kcnq3 mechanism transfers. "
      "Source: advisor_pilot_20261113/brainstorm_20261116/adv188_fazio_kcnq3_opener_response_sci_20261123/RESULT_ADV188_FAZIO_KCNQ3_OPENER_RESPONSE_SCI_20261123.md]")
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"
L = p.read_text(encoding="utf-8").split("\n"); h = L[0].split("\t"); n = 0
for i, l in enumerate(L):
    f = l.split("\t")
    if i and len(f) == len(h) and f[0] == "WO-17" and "ADV-188" not in f[h.index("status_evidence")]:
        f[h.index("status_evidence")] += CL
        f[h.index("last_touched")] = max(f[h.index("last_touched")], "2026-11-23")
        L[i] = "\t".join(f); n += 1
p.write_text("\n".join(L), encoding="utf-8")
print("WO-17", n)
