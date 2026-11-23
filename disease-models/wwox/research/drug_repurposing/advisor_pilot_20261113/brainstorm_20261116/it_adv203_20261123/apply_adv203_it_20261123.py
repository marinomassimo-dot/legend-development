"""ADV-203 (IT, 2026-11-23): ONE readout line appended to INV-06 next_test in the two ranking sources and ranking.json; old text kept; idempotent (marker 'ADV-203').
Reading carried: SCI's ADV-203 result on Prakash et al. (XDP mouse myelin): causal transfer CLOSED as untested; the one constraint INV-06 and ADV-181 did not state is a lineage-nested readout.
No ranking, drug or priority change. Run from the repository root. Hypothesis level; reference genotype class only."""
import json
from pathlib import Path

R = Path("disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029")
MARK = "ADV-203"
LINE = (" [ADV-203, 2026-11-23, one readout constraint (adjacent mouse model of a different disease, X-linked dystonia-parkinsonism; males at postnatal day 21, three animals per genotype, broad Nestin-lineage model; "
        "preprint plus an abstract-only final paper; the Luxol fast blue p value was read from a figure image; SCI reading: causal transfer untested): "
        "where a readout asks whether a myelination deficit is a loss of the oligodendrocyte lineage or an arrest of maturation, report SOX10-positive cells per area and PDGFRA-positive cells as a fraction of SOX10-positive cells, "
        "region by region in the same sections of the same animals; single-label percentages of all nuclei cannot separate the two. No ranking, drug or priority change. "
        "Source: advisor_pilot_20261113/brainstorm_20261116/adv203_prakash_xdp_myelin_sci_20261123/RESULT_ADV203_PRAKASH_XDP_MYELIN_SCI_20261123.md]")


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
    p.write_text(raw, encoding="utf-8"); return n


print("investigations_it20.tsv", edit_tsv(R / "investigations_it20.tsv"))
print("investigations.tsv", edit_tsv(R / "investigations.tsv"))
print("ranking.json", edit_json(R / "ranking.json"))
