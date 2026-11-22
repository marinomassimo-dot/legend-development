"""ADV-170 (IT, 2026-11-22): two dated clauses (INV-02, INV-17) in investigations.tsv, investigations_it20.tsv and ranking.json, and one dated line in the
current pup brief text (add-on e3) with its change-log line. Old text kept; idempotent (marker 'ADV-169, 2026-11-22' / 'ADV-166, 2026-11-22' / 'ADV-167, 2026-11-22').
Run from the repository root. Hypothesis level, no dose, no compound, nothing is medical advice; no ranking, compound or status change."""
import json
from pathlib import Path
DR = Path("disease-models/wwox/research/drug_repurposing")
RK = DR / "ranking_it8_p9_20261029"
INV02 = (" [ADV-169, 2026-11-22, optional narrowed clause (replaces the earlier ADV-168 wording): if ATF4 is high in the WWOX-deficient line, read baseline phospho-eIF2 alpha (total and phosphorylated, as a ratio) together with ATF4 at a stated time, "
         "and state the phospho-eIF2 alpha status before calling any eIF2B-lesion contrast an ISR contrast. As an optional controlled comparison, add the response of ATF4 to a short exposure to an mTOR or eIF4E inhibitor in the WWOX-deficient line and its isogenic control, "
         "beside a matched canonical ER-stress challenge at the same time. In the one published preparation (mouse fibroblasts), ATF4 raised by eIF2B epsilon depletion was lost under an mTOR inhibitor at 1 to 2 hours while ATF4 raised by the ER-stress challenge persisted on the same blot; "
         "that is one representative blot of three experiments with no quantification, with unmatched arms and times (protein synthesis 74.8 against 11.9 percent, and a source-sheet label that disagrees with the legend's 1 hour), and a second eIF2B-reduced preparation responded only partly. "
         "Read it as an observed pattern in that preparation, not as a classifier of route and not as an eIF2B activity measurement in WWOX. A PERK mobility shift is context for an ER-stress challenge only; "
         "read GADD34 and CHOP protein only at a late matched time, because their mRNA rises in the eIF2B-reduced state and does not separate the routes; no arm is promoted.]")
INV17 = (" [ADV-166, 2026-11-22, optional: express counts per fixed starting number (total nuclei per organoid or section), not per field, and do not use a pulse-labelled cohort as the denominator when the perturbation changes cell cycling, "
         "because the labelled cohort differed between arms in the adjacent mouse study; read at the end of each window and once at one fixed later time, so that an early favourable ratio is read beside the later absolute yield; the shrinking-pool error condition above stays.]")
EDITS = {"INV-02": ("ADV-169, 2026-11-22", INV02), "INV-17": ("ADV-166, 2026-11-22", INV17)}
BRIEF = DR / "experiment_brief_presidio013_sci_20261116/current_text_adv143_it_20261121/PUP_BRIEF_CURRENT_IT_20261121.md"
E3 = ("- **(e3), dated line 2026-11-22 (ADV-167, from Sun 2016 in an adjacent wild-type juvenile mouse visual cortex; the text above is unchanged; not an arm and not a gate):** "
      "where the preparation and age allow PV identification (PV-reporter identification starts from about two weeks after birth, so a neonatal window may not allow it), "
      "an optional state descriptor: record baseline excitatory input onto identified PV cells beside baseline phospho-ErbB4 and the sIPSC read in (e3). "
      "Sun's input measure was photostimulation-EVOKED synaptic input, whereas the earlier draft clause named SPONTANEOUS excitatory currents: they are different quantities; keep them distinct and leave the choice of measure to the preparation. "
      "In Sun the two state variables co-vary; a paired reading shows whether they co-vary or separate in Wwox tissue, but neither a paired reading nor a null shows causal moderation, an absent response, absence of engagement or a WWOX result.")
CL = "- 2026-11-22, ADV-170 (IT): dated line added to add-on (e3) (baseline PV-identified excitatory input as an optional state descriptor, evoked against spontaneous kept distinct); no arm, no gate, no design change."


def edit_tsv(p):
    t = p.read_text(encoding="utf-8"); L = t.split("\n"); h = L[0].split("\t"); n = 0
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


def edit_brief():
    t = BRIEF.read_text(encoding="utf-8")
    if "ADV-167, from Sun 2016" in t:
        return "already"
    k = t.index("**OPEN-GAP R2Q79")
    t = t[:k] + E3 + "\n\n" + t[k:]
    j = t.index("- 2026-11-21, line 9.13: folded into add-on (e3).")
    e = t.index("\n", j)
    t = t[:e + 1] + CL + "\n" + t[e + 1:]
    BRIEF.write_text(t, encoding="utf-8"); return "edited"


if __name__ == "__main__":
    print("investigations.tsv", edit_tsv(RK / "investigations.tsv"))
    print("investigations_it20.tsv", edit_tsv(RK / "investigations_it20.tsv"))
    print("ranking.json", edit_json(RK / "ranking.json"))
    print("brief", edit_brief())
