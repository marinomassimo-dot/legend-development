"""ADV-186 (IT, 2026-11-22): two conditional consumer clauses, old text kept except one replaced clause (stated in the assignment).
1. INV-16 Step 1: surface-readout qualification (ADV-184 result, with Codex's refinement in ADV-186 Amendment 1) appended to next_test in the two ranking
   tables and ranking.json.
2. IT59-Q01 (open-question map) and the RP-038 portfolio row: the 2006 full text has been read (SCI L supply result), so the clause 'provisional until the 2006
   Cell full text is read' is replaced in the question text (300-character column) and the full wording sits in status_evidence.
Idempotent (marker strings). Run from the repository root. Hypothesis level, no dose, reference genotype class only; no arm, ranking or compound change."""
import json
from pathlib import Path

DR = Path("disease-models/wwox/research/drug_repurposing")
MARK16 = "ADV-184 with ADV-186"
INV16 = (" [ADV-184 with ADV-186 Amendment 1, 2026-11-22, optional readout qualification for Step 1 (adjacent source: tagged overexpression of GLUT1 variants in endothelial and HeLa cells, partial figure coverage; "
         "test-design logic only, nothing about HDAC5 or WWOX): where feasible, quantify endogenous surface GLUT1 per cell with a surface-specific assay (non-permeant labelling with an intracellular-leakage control, or an extracellular epitope in non-permeabilised cells) "
         "and report total protein and glucose uptake or entry in the matched conditions as paired measures. A colocalisation coefficient with a membrane marker in fixed, permeabilised cells is a spatial metric and cannot quantify the surface pool "
         "(in the source, two variants had wild-type-like membrane coefficients, about 0.68 and 0.63 against 0.67, with lysosomal overlap about 0.76 and 0.64 against 0.27). "
         "Uptake normalised to surface abundance is an optional secondary ratio, shown with both inputs and their uncertainty; before attributing a discrepancy to intrinsic transport, require a reliable denominator and a GLUT1-specific functional control, "
         "because other transporters or assay conditions can change measured uptake. A fall in entry with a stable surface amount is compatible with impaired transport despite surface presence, not automatically a GLUT1 defect. No new arm, ranking or compound change.]")
OLDQ = "provisional until the 2006 Cell full text is read"
NEWQ = "2006 full text read: ICD signalling represses astrogenesis; open on the WWOX side, see evidence"
MARKQ = "ADV-186"
EVQ = (" [IT 2026-11-22, ADV-186 (from the SCI L supply result, section Consumers): the 2006 full text has been read: ICD signalling represses astrogenesis (rat E14.5 precursor cultures, mouse E17.5 cortex); the remaining provisionality is on the WWOX side: "
       "ICD retention is cited from the 2005 report, 2007 tumour data show no WWOX-nuclear-ErbB4 association, and a stabilisation arm (less ErbB4 without WWOX) is untested in neural cells; the attribution caution (P47T disrupts all WW1-PPxY partners) is unchanged. "
       "The question text above replaced 'provisional until the 2006 Cell full text is read'. No candidate, direction or ranking change. Source: advisor_pilot_20261113/brainstorm_20261116/l_supply_sardi_aqeilan07_sci_20261122/RESULT_L_SUPPLY_SARDI2006_AQEILAN2007_SCI_20261122.md]")
RP038 = (" [IT 2026-11-22, ADV-186: the sign premise that was provisional until the 2006 full text is read is answered for the Sardi side (ICD signalling represses astrogenesis in rat and mouse cortical precursors); "
         "the binding premise moves to the WWOX side (ICD retention cited from 2005; no WWOX-nuclear-ErbB4 association in 2007 tumour data; stabilisation arm untested in neural cells). Nothing about PV cells; no candidate, direction or ranking change.]")


def edit_tsv(p):
    L = p.read_text(encoding="utf-8").split("\n"); h = L[0].split("\t"); n = 0
    for i, l in enumerate(L):
        f = l.split("\t")
        if i and len(f) == len(h) and f[h.index("inv_id")] == "INV-16":
            c = h.index("next_test")
            if MARK16 not in f[c]:
                f[c] += INV16; L[i] = "\t".join(f); n += 1
    p.write_text("\n".join(L), encoding="utf-8"); return n


def edit_json(p):
    raw = p.read_text(encoding="utf-8"); d = json.loads(raw); n = 0
    for x in [y for k in ("investigations", "further_investigations", "conditional_hypotheses") for y in d.get(k, [])]:
        if x["inv_id"] == "INV-16" and MARK16 not in x["next_test"]:
            old = json.dumps(x["next_test"], ensure_ascii=False)[1:-1]
            assert raw.count(old) == 1
            raw = raw.replace(old, old + json.dumps(INV16, ensure_ascii=False)[1:-1]); n += 1
    p.write_text(raw, encoding="utf-8"); return n


def edit_row(p, keycol, key, edits):
    L = p.read_text(encoding="utf-8").split("\n"); h = L[0].split("\t"); n = 0
    for i, l in enumerate(L):
        f = l.split("\t")
        if i and len(f) == len(h) and f[h.index(keycol)] == key:
            for col, fn in edits:
                new = fn(f[h.index(col)])
                if new != f[h.index(col)]:
                    f[h.index(col)] = new; n += 1
            L[i] = "\t".join(f)
    p.write_text("\n".join(L), encoding="utf-8"); return n


def main():
    r = DR / "ranking_it8_p9_20261029"
    print("investigations_it20.tsv", edit_tsv(r / "investigations_it20.tsv"))
    print("investigations.tsv", edit_tsv(r / "investigations.tsv"))
    print("ranking.json", edit_json(r / "ranking.json"))
    def q(s):
        s2 = s.replace(OLDQ, NEWQ) if OLDQ in s else s
        assert len(s2) <= 300, len(s2)
        return s2
    ev = lambda s: s if MARKQ in s else s + EVQ
    print("map IT59-Q01", edit_row(DR / "batch_sci_20261105/map/open_questions_map.tsv", "qid", "IT59-Q01",
                                     [("question_text_max300", q), ("status_evidence", ev), ("last_touched", lambda s: "2026-11-22" if s < "2026-11-22" else s)]))
    print("RP-038", edit_row(DR / "research_portfolio.tsv", "id", "RP-038",
                             [("outcome", lambda s: s if "ADV-186" in s else s + RP038), ("updated_utc", lambda s: "2026-11-22T21:05:00Z" if s < "2026-11-22T21:05:00Z" else s)]))


if __name__ == "__main__":
    main()
