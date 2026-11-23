"""ADV-193 (IT, 2026-11-23): one dated wording clause appended to the WO-21 status_evidence, old text kept; idempotent (marker 'ADV-193').
Reading carried: SCI's NARROW result on Saha et al. 2024 (PMID 38056909). Wording of the test condition: Codex return 33 plus its additions, as relayed by ADV.
Outcome chosen: CONDITION ADDED (not 'pointer only', not 'stays as written'), because the source changes what a discriminating test must measure:
the held row asked for a differently acting GSK3 inhibitor and an inositol add-back arm 'in the same system', and did not say that the proximal readout must
separate store release from entry, that GSK3 engagement must be shown in the same preparation, or that the two arms need a matched baseline.
Run from the repository root. Hypothesis level, laboratory conditions only, no dose or regimen advice, reference genotype class only; no ranking, compound, arm or direction change."""
from pathlib import Path

DR = Path("disease-models/wwox/research/drug_repurposing")
CL = (" [IT 2026-11-23 ADV-193, wording-level, hypothesis level; the row stays OPEN; no ranking change, no drug promotion, no assay commissioned] "
      "Saha et al. 2024 (Life Sci Alliance, PMID 38056909; SCI reading NARROW, partial read: supplementary tables and several figures not read) separates an inositol-pathway route from a GSK3 route on two proximal endpoints "
      "(receptor-evoked store release in zero external calcium, and plasma-membrane PIP2 recovery) in HEK293T cells only: lithium lowers both, an IMPA1-deleted clone has the lowered phenotype by itself and shows no further lithium effect, "
      "extra inositol restores the lithium effect, and an engaged GSK3 inhibitor changes neither. In neurons (one iPSC-derived control line, lithium 1 mM for 10 days) only the lithium side was measured "
      "(spontaneous calcium transients, carbachol-evoked calcium and store release lower); there is no IMPA1-deleted neuron arm, no inositol add-back, no PIP2 readout and no GSK3 engagement readout in neurons, "
      "so the link from the proximal route to neuronal activity crosses preparations at the critical step. Two details this row did not carry: IMPA1 dependence is endpoint-specific "
      "(lithium still lowers store-operated entry in the deleted clone), and the neuronal GSK3 'no effect' is a non-significant result at a different baseline, not an equivalence. "
      "Test condition (Codex return 33): Test lithium and an independently engaged GSK3 comparator alongside an inositol-pathway rescue and its own control, in matched neural preparations with comparable baseline and time-matched vehicle. "
      "Separate receptor-evoked store release/PIP2 recovery from calcium entry, and estimate the effects with independent biological replication. "
      "A rescue that restores the proximal endpoint and the functional phenotype supports an inositol-pathway contribution. Restoration of the proximal endpoint alone leaves the functional attribution open. "
      "A small GSK3 comparator effect requires sufficient precision under credible engagement and a prespecified meaningful margin. "
      "Added per Codex: a direct electrical endpoint if the claim concerns firing (spontaneous calcium transients are an activity readout, not firing); a rescued endpoint is evidence of contribution under the tested conditions, and both mechanisms can contribute; "
      "no effect size or equivalence margin can be copied from the paper; a non-significant result at a different baseline is neither a reliable difference between mechanisms nor evidence of negligible action. "
      "The WWOX-specific lithium question is untouched and stays open (the held provoked-seizure experiment did not measure engagement). "
      "Source: advisor_pilot_20261113/brainstorm_20261116/adv193_saha_impa1_inositol_gsk3_sci_20261123/RESULT_ADV193_SAHA_IMPA1_INOSITOL_GSK3_SCI_20261123.md; receipt FTR-20261123-38056909-01]")
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"
L = p.read_text(encoding="utf-8").split("\n"); h = L[0].split("\t"); n = 0
for i, l in enumerate(L):
    f = l.split("\t")
    if i and len(f) == len(h) and f[0] == "WO-21" and "ADV-193" not in f[h.index("status_evidence")]:
        f[h.index("status_evidence")] += CL
        f[h.index("last_touched")] = max(f[h.index("last_touched")], "2026-11-23")
        L[i] = "\t".join(f); n += 1
p.write_text("\n".join(L), encoding="utf-8")
print("WO-21", n)
