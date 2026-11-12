"""IT47 P3: SCI47 package A (inhibitory_defect_sci47_20261112) consumer delta rows 1-5 and 8, applied with dated updates; the historical texts are kept. Idempotent.  python3 apply_it47_sci47.py [--check]"""
import csv, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
V21_OLD = ("the printed mean amplitude falls by about half (57.3 to 27.5 pA, a fall of 52 percent) and the printed mean frequency falls by about a fifth (10.3 to 8.4 Hz, a fall of 18 percent, with spread as large as the mean); high-chloride pipette, no evoked-current experiment. "
           "Whether the amplitude fell more than the frequency is not shown by these means: event detection, pooling of events and the spread leave the receptor response, the GABA content of each event and the interneuron output all open (inference, weak).")
V21_NEW = ("the printed mean amplitude falls by about 52 percent (57.3 to 27.5 pA) and the printed mean frequency by about 18 percent (10.3 to 8.4 Hz); high-chloride pipette, no antagonist named, no evoked-current experiment. "
           "The order of the two falls does not by itself point to the receptor response or to the GABA content of each event: the frequency change is shown only by a distribution test on pooled events, detected frequency depends on amplitude, and event identity is not shown, so the receptor response, the GABA content of each event, the interneuron output and the chloride gradient all stay open.")
UNIT = ("[IT47 SCI47] Unit-of-analysis note for the Wwox slice paper: the change in inhibitory-current frequency is shown only by a distribution test on pooled events (no per-cell or per-animal test); the pipette of the excitatory-current recordings holds about 12 mM chloride (E_Cl about -63 mV), so their isolation at -70 mV is not chloride-free; "
        "burst frequency differs between the Results (median interval 26.2 s) and the supplementary table (0.84 per minute); animal counts do not sum (4+4 against 7). Source: inhibitory_defect_sci47_20261112/output/source_table.tsv.")
Q01 = (" [IT47 SCI47] Conditions of the only transferred reversal value (Yuan 2019): -66.7 +/- 5.6 mV SEM, n = 5, 22-25 C against 35 C in the Wwox recordings, cortex and hippocampus pooled; Scn1b-null neurons -51.1 mV in the same age bin.")
Q04 = (" [IT47 SCI47] Phase 0 is drug-free and is two cohorts, not one protocol per cell (perforated patch: native-chloride sIPSC, mIPSC, evoked IPSC with paired pulse, puffed agonist, E_GABA; whole cell: series resistance, capacitance, input resistance and high-chloride measures), animals as the unit; occlusion of two levers is exploratory only (it cannot separate target, cells, saturation or floor); a burst reduction by a non-selective action is not evidence of correction.")
NOTE46 = "\n**Update 2026-11-12 (IT47 P3, SCI47 package A).** Wording and strength, with the paper rechecked: sIPSC frequency falls **by** about 18 percent (10.3 to 8.4 Hz) and amplitude **by** about 52 percent (57.3 to 27.5 pA); neither is a fall *to* a fifth. The order of the two falls does not by itself point to the receptor response or to the GABA content per event: the frequency change is shown only by a distribution test on pooled events, detected frequency depends on amplitude, and event identity is not shown. The K-gluconate pipette of the excitatory-current recordings holds about 12 mM chloride. See `../inhibitory_defect_sci47_20261112/`.\n"
NOTE_P9 = "\n**Update 2026-11-12 (IT47, SCI47 design review).** The shared generic comparator of the two designs stays only for burst-rate controls: an equal effect on one cellular quantity is not an equal effect on the burst. A burst reduction by a non-selective action is not evidence of correction.\n"
ROWS = [(DR / "generation_it41_20261109/compound_view.tsv", "item_id", "V21", "rationale", None)]


def main(check=False):
    csv.field_size_limit(10**9); changed = 0
    f = DR / "generation_it41_20261109/compound_view.tsv"
    rows = list(csv.reader(open(f, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; i, c = h.index("item_id"), h.index("rationale")
    for r in rows[1:]:
        if r[i] == "V21" and V21_OLD in r[c]:
            r[c] = r[c].replace(V21_OLD, V21_NEW); changed += 1
    if not check: csv.writer(open(f, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    for g in (DR / "ranking_it8_p9_20261029/investigations_it20.tsv", DR / "ranking_it8_p9_20261029/investigations.tsv"):
        rows = list(csv.reader(open(g, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; i, c = h.index("inv_id"), h.index("decisive_uncertainty")
        for r in rows[1:]:
            if r[i] in ("INV-18", "INV-10") and "[IT47 SCI47]" not in r[c]:
                r[c] = (r[c] + " " + UNIT).strip(); changed += 1
        if not check: csv.writer(open(g, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    m = DR / "batch_sci_20261105/map/open_questions_map.tsv"
    rows = list(csv.reader(open(m, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; b = h.index("blocking_reason")
    for r in rows[1:]:
        for q, t in (("IT46-Q01", Q01), ("IT46-Q04", Q04)):
            if r[0] == q and "[IT47 SCI47]" not in r[b]:
                r[b] += t; changed += 1
    if not check: csv.writer(open(m, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    for p, note, key in ((DR / "generation_it46_20261111/README.md", NOTE46, "SCI47 package A"), (DR / "generation_it46_20261111/s5_case/result_it46.md", NOTE46, "SCI47 package A"), (DR / "generation_it46_20261111/p9_two_levers_it46.md", NOTE_P9, "SCI47 design review")):
        t = p.read_text(encoding="utf-8")
        if key not in t:
            changed += 1
            if not check: p.write_text(t.rstrip("\n") + "\n" + note, encoding="utf-8")
    print(("would change " if check else "changed ") + str(changed))


if __name__ == "__main__":
    main("--check" in sys.argv)
