"""ADV-250 follow-up (IT, 2026-11-25, approved by ADV): extend the placed hippocampal-libraries wording (ADV-247) with the upper-bound statement, in cards J01 and F03 (packet not_known, in place)
and in INV-06 and INV-15 (dated clause). Also writes the copy of SCI's independence table with the column 'n_as_stated_is_upper_bound'. Text-level, idempotent; cards rebuilt afterwards by repurposing_bridge.py.
Run from the repository root. Hypothesis level; nothing is medical advice."""
import csv, importlib.util, json
from pathlib import Path
DR = Path("disease-models/wwox/research/drug_repurposing")
spec = importlib.util.spec_from_file_location("a", DR / "advisor_pilot_20261113/brainstorm_20261116/it_adv247wording_20261125/apply_adv247_wording_it_20261125.py")
a = importlib.util.module_from_spec(spec); spec.loader.exec_module(a)
OLD_TAIL = " [IT 2026-11-25, ADV-247]"
EXT = (" Whatever a library contains it is at most one independent unit, so the library count is an upper bound on n; if a library is one mouse, the 2 control libraries "
       "cover at most 2 of the 4 control cortices, so the control hippocampi and cortices are not all the same mice. [IT 2026-11-25, ADV-250]")
CL = (" [IT 2026-11-25, ADV-250: a hippocampal library is at most one independent unit, so the library count is an upper bound on n; if a library is one mouse, "
      "the 2 control libraries cover at most 2 of the 4 control cortices.]")
def cards():
    n = 0
    for c in ("J01_glial_reactivity_modulation", "F03_bumetanide_chloride_gradient"):
        p = DR / f"cards/{c}.packet.json"; raw = p.read_text(encoding="utf-8")
        if "ADV-250" in raw: continue
        old = a.j(a.HIPP); assert raw.count(old) == 1, c
        raw = raw.replace(old, old + a.j(EXT)); json.loads(raw); p.write_text(raw, encoding="utf-8"); n += 1
    return n
if __name__ == "__main__":
    a.INV = {"INV-06": [CL], "INV-15": [CL]}
    RK = DR / "ranking_it8_p9_20261029"
    print("cards", cards(), "tsv", a.inv_tsv(RK / "investigations.tsv"), a.inv_tsv(RK / "investigations_it20.tsv"), "json", a.inv_json(RK / "ranking.json"))
    S = DR / "advisor_pilot_20261113/brainstorm_20261116/adv247_independence_audit_sci_20261125/independence_adv247.tsv"
    O = Path(__file__).parent / "independence_adv247_upperbound_it_20261125.tsv"
    rows = list(csv.DictReader(open(S, encoding="utf-8"), delimiter="\t")); h = list(rows[0].keys()) + ["n_as_stated_is_upper_bound", "adv250_note"]
    for r in rows:
        if r["disposition"] == "not stated":
            r["n_as_stated_is_upper_bound"] = "yes (the library or sample count caps the independent units whatever the missing sentence says)"
            r["adv250_note"] = ("H1: RNA-seq n named as mice in the legend, one newborn per preparation by the Methods; library-to-pup identity and passage not stated (weak resolution)" if r["id"] == "H1"
                                else "hippocampal libraries: not resolvable from GEO and BioSample records, paper Methods or Figure 3 legend; ENA has no run rows")
        else:
            r["n_as_stated_is_upper_bound"] = "yes; effective n already shown"; r["adv250_note"] = ""
    with open(O, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=h, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
    print("table rows", len(rows))
