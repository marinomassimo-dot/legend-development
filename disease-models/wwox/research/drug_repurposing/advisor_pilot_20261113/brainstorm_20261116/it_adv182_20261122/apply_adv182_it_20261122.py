"""ADV-182 (IT, 2026-11-22): four dated consumer clauses in one pass. Old text kept; idempotent (markers).
1 INV-07 (investigations.tsv, investigations_it20.tsv, ranking.json): lactate as label-resolved pools (stocks), a flux claim needs a kinetic readout (ADV-177 with ADV-178).
2 INV-06 (same three files) plus a dated line in the X1 README: MBP-positive count and area as lineage or material readouts; two separate claims (ADV-181 with Codex return 23).
3 RP-043 (research_portfolio.tsv, outcome column): a developmental-map match is state resemblance at sampling (ADV-179; not view-feeding).
4 WO-17 (open_questions_map.tsv status_evidence): the weak optional ADV-173 baseline Kv7 readout, unchanged in substance.
Run from the repository root. Hypothesis level; no dose; no ranking, compound, mechanistic or WWOX claim; nothing is medical advice."""
import json
from pathlib import Path
DR = Path("disease-models/wwox/research/drug_repurposing")
RK = DR / "ranking_it8_p9_20261029"
INV07 = (" [ADV-177 with the ADV-178 addendum, 2026-11-22, optional readout qualification: in the astrocyte class read lactate as label-resolved pools in cells and in medium from the same wells (the labelled and the unlabelled pool, as stocks), next to oxygen consumption and extracellular acidification; "
         "do not read acidification, proton efflux or a total lactate pool as production. Pools are stocks set together by production, export, uptake and consumption, so a flux or rate claim needs its own kinetic readout (a labelled-substrate time course or an efflux measurement with controls for uptake and consumption, viability and normalisation). "
         "In the one adjacent measured case (an astrocyte-restricted mouse perturbation) a labelled panel of three cultures showed no detected difference in the labelled pools, which is not equivalence, and an unlabelled pool does not name the origin of its material. The comparison itself is unchanged and no arm is promoted.]")
INV06 = (" [ADV-181 with Codex return 23, 2026-11-22, optional readout qualification (adjacent primary-culture source; test-design logic only): treat MBP-positive count and area as lineage or material readouts. Attribute an increase to newly formed sheaths only with an origin-resolved structural readout per cell, "
         "naming the field or culture denominator and controlling for retained MBP-bearing material where applicable (hiding a fluorescence channel visually does not exclude donor material from the analysed measurement). Two separate claims: origin-resolved morphology per cell can substantiate newly formed sheaths; "
         "conduction is reported separately as a functional outcome and cannot substitute for new-sheath evidence, because neuronal physiology can change conduction independently of new myelination. Keep cell counts, the per-cell result, the field or culture denominator and the biological replicate distinct. "
         "Residual only, no follow-up unless a decision depends on it: in the source, the NG2 share of one panel does not match the counts of two other panels.]")
EDITS = {"INV-07": ("ADV-177 with the ADV-178", INV07), "INV-06": ("ADV-181 with Codex return 23", INV06)}
RP043 = (" [IT 2026-11-22, ADV-182 (from ADV-179 and Codex return 21), consumer wording: a developmental-map match is evidence of STATE RESEMBLANCE at the sampling time, conditional on the reference and the scoring; it does not measure a developmental trajectory or how and when the cells arrived there. "
         "In the adjacent mouse control system the aggregate example used different lines and cells, and non-significance in the small linked comparison does not show equivalence. A within-line readout at several ages can test a maturation explanation (ADV-146 rival B), and attributing an activity difference to maturation may still need a discriminating comparison. "
         "No change to P-SCI-1, ranking or any candidate.]")
WO17 = (" [ADV-173, 2026-11-22, weak optional readout (adjacent human channel-gene model; one variant; test-design logic only): in the session that carries the burst ladder, record one baseline Kv7 readout in cells from the same animals and slices (same age window, control cells beside, sex recorded): a drug-free current sensitive to a Kv7 blocker, or, if an opener-defined current is used, stated as a ceiling; "
        "and treat control cells or slices with the same ladder on the same readout the burst panel uses where the control preparation shows activity. Reading rule: a suppression of null-slice bursts is read as an effect of the opener, and as a correction of the null state only if the baseline current differs from control at that age and the control preparation does not respond alike; otherwise it is a brake. Not a gate, not an arm, no dose. Source note: ADV-173 result.]")
X1 = ("\n\nDated line (IT, 2026-11-22, ADV-182; the text above is unchanged): any X1 readout that counts MBP-positive material is read under the INV-06 qualification of ADV-181 (lineage or material readout; newly formed sheaths need an origin-resolved per-cell structural readout with the field or culture denominator named and retained material controlled; conduction is a separate functional outcome). No new arm.\n")


def edit_tsv(p):
    L = p.read_text(encoding="utf-8").split("\n"); h = L[0].split("\t"); n = 0
    for i, l in enumerate(L):
        f = l.split("\t")
        if i and len(f) == len(h) and f[h.index("inv_id")] in EDITS:
            mark, add = EDITS[f[h.index("inv_id")]]; c = h.index("next_test")
            if mark not in f[c]:
                f[c] += add; L[i] = "\t".join(f); n += 1
    p.write_text("\n".join(L), encoding="utf-8"); return n


def edit_json(p):
    raw = p.read_text(encoding="utf-8"); d = json.loads(raw); n = 0
    for x in [y for k in ("investigations", "further_investigations", "conditional_hypotheses") for y in d.get(k, [])]:
        if x["inv_id"] in EDITS:
            mark, add = EDITS[x["inv_id"]]
            if mark in x["next_test"]:
                continue
            old = json.dumps(x["next_test"], ensure_ascii=False)[1:-1]
            assert raw.count(old) == 1, x["inv_id"]
            raw = raw.replace(old, old + json.dumps(add, ensure_ascii=False)[1:-1]); n += 1
    p.write_text(raw, encoding="utf-8"); return n


def edit_cell(p, key, keycol, col, add, mark):
    L = p.read_text(encoding="utf-8").split("\n"); h = L[0].split("\t"); n = 0
    for i, l in enumerate(L):
        f = l.split("\t")
        if i and len(f) == len(h) and f[h.index(keycol)] == key and mark not in f[h.index(col)]:
            f[h.index(col)] += add; L[i] = "\t".join(f); n += 1
    p.write_text("\n".join(L), encoding="utf-8"); return n


def main():
    print("investigations.tsv", edit_tsv(RK / "investigations.tsv"))
    print("investigations_it20.tsv", edit_tsv(RK / "investigations_it20.tsv"))
    print("ranking.json", edit_json(RK / "ranking.json"))
    print("RP-043 outcome", edit_cell(DR / "research_portfolio.tsv", "RP-043", "id", "outcome", RP043, "ADV-182 (from ADV-179"))
    print("WO-17 evidence", edit_cell(DR / "batch_sci_20261105/map/open_questions_map.tsv", "WO-17", "qid", "status_evidence", WO17, "ADV-173, 2026-11-22"))
    mp = DR / "batch_sci_20261105/map/open_questions_map.tsv"
    xr = DR / "x1_discriminating_observations_presidio005_20261115/README.md"
    t = xr.read_text(encoding="utf-8")
    if "ADV-182" not in t:
        xr.write_text(t.rstrip("\n") + X1, encoding="utf-8"); print("X1 README appended")


if __name__ == "__main__":
    main()
