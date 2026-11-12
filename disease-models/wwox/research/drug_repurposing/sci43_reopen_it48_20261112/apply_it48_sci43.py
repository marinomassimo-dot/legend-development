"""IT48 increment 1: the verified outcome of the eight reopened SCI43 rows, applied as dated clauses (idempotent; the original text stays)."""
import csv, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
TXT = ("[IT48 update] The eight SCI43 rows that stood producer-read only were read again against the original full texts by a distinct verifier: 4 supported, 3 partly, none unsupported, 13 files kept with SHA-256 (sci43_reopen_it48_20261112/verify). "
       "The 23 percent figure survives as printed arithmetic but is the increment of one 60 uM Ba2+ dose in P28-P42 mouse auditory cortex (the preprint itself calls that age juvenile), not a measured Kir2 share; the cohorts of the Ba2+ and Ih panels are different cells. "
       "No row measures a Ba2+-sensitive resting conductance in layer II/III at about P13-P17; the juvenile evidence is Kv7 only (about 20 percent at a rest of -67 mV with synaptic blockers at room temperature, one study; the developmental Kv7 difference is not significant). "
       "The size of a resting lever in the juvenile slice therefore stays a transfer from an older age, not a measurement; the Kir2 drug-name search has not been run. No rank, sign or qualification changed.")
README_NOTE = "\n## Update 2026-11-12 (IT48, reopen condition met)\n" + TXT.replace("[IT48 update] ", "") + "\n"
Q = ["IT48-Q01", "sci43_reopen_it48_20261112/verify/VERDICTS.md",
     "Is there any measurement of the Ba2+-sensitive share of resting conductance in layer II/III pyramidal neurons at about P13-P17 (any cortex, any laboratory), and has a drug-name-led search for Kir2 blockers or openers been made?",
     "Decides whether the first INV-18 arm needs a K2P or high-Ba2+ step (ladder step 2b) or reduces to the Kv7 spiking-range arm.",
     "literature_executable", "OPEN", "", "sci43_reopen_it48_20261112/verify/VERDICTS.md (juvenile Ba2+ share not measured in the eight reread rows)", "2026-11-12",
     "The Kir2 drug-name route of the SCI43 brief was not run in IT48 increment 1.", "yes", ""]

def clause(path, idcol, idval, col, check):
    rows = list(csv.reader(open(path, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; n = 0
    i, c = h.index(idcol), h.index(col)
    for r in rows[1:]:
        if r[i] == idval and "[IT48 update]" not in r[c]:
            r[c] = (r[c] + " " + TXT).strip(); n += 1
    if not check: csv.writer(open(path, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    return n

def main(check=False):
    csv.field_size_limit(10**9); n = 0
    n += clause(DR / "potassium_conductances_sci43_20261110/output/hypotheses.tsv", "hyp_id", "KH1", "premise", check)
    for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
        n += clause(DR / f, "inv_id", "INV-18", "next_test", check)
    rd = DR / "potassium_conductances_sci43_20261110/README.md"
    if "Update 2026-11-12 (IT48" not in rd.read_text(encoding="utf-8") and not check:
        open(rd, "a", encoding="utf-8").write(README_NOTE); n += 1
    qm = DR / "batch_sci_20261105/map/open_questions_map.tsv"
    if "IT48-Q01" not in qm.read_text(encoding="utf-8") and not check:
        open(qm, "a", encoding="utf-8").write("\t".join(Q) + "\n"); n += 1
    print(("would change " if check else "changed ") + str(n))

if __name__ == "__main__":
    main("--check" in sys.argv)
