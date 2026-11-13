"""IT50: SCI50 (phenotype-first myelination package) consumer rows 1-3 (idempotent; dated clause; question rows from the package's own open_questions.tsv)."""
import csv, sys
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
B = DR / "myelin_phenotype_first_sci50_20261113"
CLAUSE = ("[SCI50 update] The conditioned-medium arm needs a fresh-medium baseline, a mixing arm, neuron purity, a dilution series, the B27/T3 caveat, a positive control and a detection limit taken from the monoculture's own variance; neuron-secreted CTGF is reported as necessary and sufficient to block OPC maturation in neuron-specific Tsc models (the authors' in vitro claim; no Wwox datum). "
          "Variant of step X3 behind gate 0 (T3 and T4 in the medium, blind reproduction of the null-neuron deficit, an OPC window with M1 tone): an M1-selective muscarinic antagonist and an EBP inhibitor without M1 affinity, crossed with neuron genotype; null contrasts are read only when positive; a persisting gap is predicted both by a neuronal ceiling on sheath structure and by an OPC-intrinsic block. The M1/EBP premise is unresolved. IPOTESI; the Wwox-CTGF link is unsupported.")
USE = {"OQ12": "IT50-Q01", "OQ11": "IT50-Q02", "OQ10": "IT50-Q03", "OQ1": "IT50-Q04", "OQ7": "IT50-Q05", "OQ4": "IT50-Q06", "OQ5": "IT50-Q07", "OQ6": "IT50-Q08", "OQ9": "IT50-Q10"}   # OQ3 duplicates INV-12 step 0; OQ9 (the core H4 question) was omitted from the delta list by mistake and added at the author's request
EBP = ["IT50-Q09", "myelin_phenotype_first_sci50_20261113/consumer_delta.md row 3", "Does the M1-selective antagonist used as a comparator have EBP (sterol isomerase) activity, as the reagent pair assumes it does not?", "Decides whether the reagent pair separates the M1 route from the EBP route.", "literature_executable", "OPEN", "", "myelin_phenotype_first_sci50_20261113/consumer_delta.md row 3 (the package lists the question; its own table has no row)", "2026-11-13", "Reading task; identity and EBP activity of the comparator not verified from a primary paper.", "yes", ""]
def cut(t, n):
    t = " ".join(t.split()); return t if len(t) <= n else t[: n - 1].rsplit(" ", 1)[0] + "…"
def main(check=False):
    csv.field_size_limit(10**9); n = 0
    for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
        p = DR / f; rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; i, c = h.index("inv_id"), h.index("next_test"); k = 0
        for r in rows[1:]:
            if r[i] == "INV-06" and "[SCI50 update]" not in r[c]: r[c] = (r[c] + " " + CLAUSE).strip(); k += 1
        if not check and k: csv.writer(open(p, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
        n += k
    qm = DR / "batch_sci_20261105/map/open_questions_map.tsv"
    rows = list(csv.reader(open(qm, newline="", encoding="utf-8"), delimiter="\t")); have = {r[0] for r in rows}
    src = {x["oq_id"]: x for x in csv.DictReader(open(B / "output/open_questions.tsv", encoding="utf-8"), delimiter="\t")}
    for oq, qid in USE.items():
        if qid in have: continue
        x = src[oq]; kind = x["kind"]
        rows.append([qid, "myelin_phenotype_first_sci50_20261113/output/open_questions.tsv " + oq, cut(x["question"], 300), cut(x["decision_it_changes"], 200), kind, "OPEN", "", "myelin_phenotype_first_sci50_20261113/consumer_delta.md row 3 (priority " + x["priority"] + ")", "2026-11-13",
                     cut(("Needs a measurement: " + x["decisive_measure_if_experimental"]) if kind == "wet_lab_measurement" else ("Reading task; a source may be unreachable." if oq != "OQ5" else "Executed in part (SCI50 V13); stays open for a conduction readout."), 200), "no" if kind == "wet_lab_measurement" else "yes", ""]); n += 1
    if EBP[0] not in have: rows.append(EBP); n += 1
    if not check and n: csv.writer(open(qm, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    print(("would change " if check else "changed ") + str(n))
if __name__ == "__main__":
    main("--check" in sys.argv)
