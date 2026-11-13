"""IT49: SCI49 package B (Kir2 drug-name route) consumer rows 1-3 (idempotent; dated clauses; question rows built from the package's own open_questions.tsv)."""
import csv, sys
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
B = DR / "kir2_drugname_sci49_20261112"
PREMISE = ("[SCI49] Direct-mechanism Kir2.1 activators acting through a channel cysteine (Cys311) exist in recombinant cells (three marketed drugs, named in the package) and none is tested in neurons; one of them spares the Kir2.1+2.2 and 2.1+2.3 heteromers and is also a Na+ channel blocker; two are at abstract depth; "
           "the claimed opener listed here rests on one laboratory in hypoxic CHO cells; direction of benefit unresolved.")
NOTE = "[SCI49] ChEMBL by name returns no activity rows for these on the four Kir2 targets: the primary papers carry the pharmacology (the earlier statement that no Kir2 activator is catalogued was a by-symbol search artefact)."
STEP = ("[SCI49 update] A Kir2-directed step is testable at family level with a blocker probe once KATP is blocked pharmacologically, the range is kept subthreshold (hERG block within about 2.7-fold of Kir2.1 on one platform), a positive control is recorded the same day, and pipette versus bath delivery is used if the site of action permits; "
        "it cannot separate Kir2 isoforms or exclude K2P, and a bath effect cannot separate neuron from glia. IPOTESI; direction of benefit not assumed.")
Q01_EV = "drug-name half CONCLUDED (SCI49 B: ten compounds read, verifier census; two string sets found no juvenile P13-P17 Ba2+ share, not an absence claim); the juvenile share half stays open"
Q44_NOTE = " [SCI49 B] No Kir2.2 or Kir2.3 opener was found."
USE = {"OQ1": "IT49-Q05", "OQ2": "IT49-Q06", "OQ5": "IT49-Q07", "OQ8": "IT49-Q08", "OQ9": "IT49-Q09", "OQ10": "IT49-Q10", "OQ11": "IT49-Q11"}   # OQ3 duplicates IT48-Q01 (the juvenile share) and is not added

def cut(t, n):
    t = " ".join(t.split()); return t if len(t) <= n else t[: n - 1].rsplit(" ", 1)[0] + "…"

def edit(path, idcol, idval, col, fn, tag, check):
    rows = list(csv.reader(open(path, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; n = 0
    i, c = h.index(idcol), h.index(col)
    for r in rows[1:]:
        if r[i] == idval and tag not in r[c]:
            r[c] = fn(r[c]); n += 1
    if not check and n: csv.writer(open(path, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    return n

def main(check=False):
    csv.field_size_limit(10**9); n = 0
    cv = DR / "generation_it41_20261109/compound_view.tsv"
    n += edit(cv, "item_id", "V14", "name_full", lambda t: t.replace("zacopride (Kir2.1 opener)", "zacopride (claimed Kir2.1 opener, one laboratory)"), "claimed Kir2.1", check)
    n += edit(cv, "item_id", "V14", "open_premise", lambda t: t + " " + PREMISE, "[SCI49]", check)
    n += edit(cv, "item_id", "V14", "registry_note", lambda t: t + " " + NOTE, "[SCI49]", check)
    for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
        n += edit(DR / f, "inv_id", "INV-18", "next_test", lambda t: t + " " + STEP, "[SCI49 update]", check)
    qm = DR / "batch_sci_20261105/map/open_questions_map.tsv"
    rows = list(csv.reader(open(qm, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; have = {r[0] for r in rows}
    for r in rows[1:]:
        if r[0] == "IT48-Q01" and "SCI49 B" not in r[h.index("status_evidence")]:
            r[h.index("status_evidence")] += "; " + Q01_EV; r[h.index("last_touched")] = "2026-11-12"; n += 1
        if r[0] == "IT44-Q01" and "[SCI49 B]" not in r[h.index("status_evidence")]:
            r[h.index("status_evidence")] += Q44_NOTE; n += 1
    src = {x["oq_id"]: x for x in csv.DictReader(open(B / "output/open_questions.tsv", encoding="utf-8"), delimiter="\t")}
    for oq, qid in USE.items():
        if qid in have: continue
        x = src[oq]; kind = x["kind"]
        rows.append([qid, "kir2_drugname_sci49_20261112/output/open_questions.tsv " + oq, cut(x["question"], 300), cut(x["decision_it_changes"], 200), kind, "OPEN", "", "kir2_drugname_sci49_20261112/consumer_delta.md row 3 (priority " + x["priority"] + ")", "2026-11-12",
                     cut("Needs a measurement: " + x["decisive_measure_if_experimental"] if kind == "wet_lab_measurement" else "Reading task; a source may be unreachable (not an absence claim).", 200), "no" if kind == "wet_lab_measurement" else "yes", ""]); n += 1
    if not check and n: csv.writer(open(qm, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    print(("would change " if check else "changed ") + str(n))
if __name__ == "__main__":
    main("--check" in sys.argv)
