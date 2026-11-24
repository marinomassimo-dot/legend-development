"""ADV-209 (IT, 2026-11-24): ONE wording line appended to INV-06 next_test in the two ranking sources and ranking.json; old text kept; idempotent (marker 'ADV-209').
Source check: HOLDS (RESULT_ADV209_MYELIMAP_IT_20261124.md, receipt FTR-20261124-41664646-01). No repo path, coordination path, 'files/' or '../' in the new text (export-card test).
No ranking, drug or priority change. Run from the repository root. Hypothesis level; reference genotype class only."""
import json
from pathlib import Path

R = Path("disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029")
MARK = "ADV-209"
LINE = (" [ADV-209, 2026-11-24, one wording constraint for any claim of restored propagation, proposal level; no ranking, drug or priority change; no new apparatus. "
        "Source checked by IT in the published open-access paper (Ahuja et al. 2026, Lab on a Chip, PMID 41664646; partial full-text read, supplementary information not opened; figure values are graph readings): "
        "human induced neurons with or without induced oligodendrocytes on a microfluidic electrode platform, with no WWOX perturbation and no tested drug. At week 8 the plotted means are about 0.36 against 0.27 m/s (co-culture against monoculture) "
        "and, in the same figure, about 1.2 against 3.15 detected responses per microchannel; the authors state that monocultures showed more responses and attribute it to axon excitability, axonal density or arrangement. "
        "Speed is the latency at the start of the stimulation train over one path length (1,960 micrometres) assumed for every point, clusters are not tied to identified axons, monocultures are in separate devices, "
        "two co-culture networks were excluded for missing stimulation artifacts, and electron microscopy is shown only for co-culture as representative images. "
        "So a faster speed summary can sit beside a smaller responding set, and the paper neither shows nor excludes that this explains its speed difference: speed alone is not recovery. "
        "For any claim of restored propagation keep four estimands separate: (a) viable axons that can be followed; (b) stimulated spikes that arrive distally within identified axons; "
        "(c) latency or conduction speed among successful impulses; (d) cost per delivered impulse at comparable activity, only when metabolic conservation is the claimed effect. "
        "Rule: more speed in a subset with fewer distal successes lowers priority for a broad functional claim unless another endpoint, such as survival or correct recruitment, supplies the decision. "
        "A fixed, paired viable-axon path with better propagation across a train despite less recruitment is a different result from the same timing change in a changed responding population; "
        "where pulse-to-axon linkage is absent, carry the contrast as a proposal (the fraction of successful propagation that is missing), not as a result. "
        "The stage and tract controls of this row and its reopening condition still apply; the energy lead of the portfolio is untouched. "
        "A stylised mixture calculation from the displayed means (Codex strategic review 25) is an identification check only and does not reconstruct the paper's estimator. "
        "Sources: the published paper and the Codex strategic review 25 (laboratory coordination directory, not in git); receipt FTR-20261124-41664646-01]")


def edit_tsv(p):
    L = p.read_text(encoding="utf-8").split("\n"); h = L[0].split("\t"); n = 0
    for i, l in enumerate(L):
        f = l.split("\t")
        if i and len(f) == len(h) and f[h.index("inv_id")] == "INV-06":
            c = h.index("next_test")
            if MARK not in f[c]:
                f[c] += LINE; L[i] = "\t".join(f); n += 1
    p.write_text("\n".join(L), encoding="utf-8"); return n


def edit_json(p):
    raw = p.read_text(encoding="utf-8"); d = json.loads(raw); n = 0
    for x in [y for k in ("investigations", "further_investigations", "conditional_hypotheses") for y in d.get(k, [])]:
        if x["inv_id"] == "INV-06" and MARK not in x["next_test"]:
            old = json.dumps(x["next_test"], ensure_ascii=False)[1:-1]
            assert raw.count(old) == 1
            raw = raw.replace(old, old + json.dumps(LINE, ensure_ascii=False)[1:-1]); n += 1
    json.loads(raw)
    p.write_text(raw, encoding="utf-8"); return n


print("investigations_it20.tsv", edit_tsv(R / "investigations_it20.tsv"))
print("investigations.tsv", edit_tsv(R / "investigations.tsv"))
print("ranking.json", edit_json(R / "ranking.json"))
