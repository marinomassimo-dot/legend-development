"""ADV-156 (IT, 2026-11-21): dated lines where claims live. Old text is kept; every edit is an appended dated line; idempotent (marker 'ADV-156').

A. Three demotions (one line each, with its source), at the live sites:
   1. the simulated class order is no longer an argument for the tonic-inhibition arm (selection note, arm table notes);
   2. the Kv7 class stays penalised until a margin is measured (selection note, opportunity map row OPP-05);
   3. the T-type attribution arm is demoted, not the ethosuximide observation (selection note, opportunity map row OPP-03, by-endpoint comparison).
B. POOLED-ONLY (ADV, from SCI's last reply): the week-16 WOREE-over-SCAR12 contrast, at every consumer that cites it as an input
   (context-differences README and matrix rows, portfolio row RP-043, the registry wording candidate, the two analysis records).
C. A dated correction of IT's own ADV-154 contribution (levetiracetam row: a juvenile mouse pharmacokinetic study exists).
Run from the repository root:  python3 disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_adv156_20261121/apply_adv156_it_20261121.py
Class level, hypothesis level, no dose; the compound ranking does not change."""
import csv
import sys
from pathlib import Path

W = Path("disease-models/wwox")
DR = W / "research/drug_repurposing"
BS = DR / "advisor_pilot_20261113/brainstorm_20261116"
MARK = "ADV-156"
SYN = "advisor_pilot_20261113/brainstorm_20261116/predictive_brainstorm_20261121/SYNTHESIS_ADV_PREDICTIVE_BRAINSTORM_20261121.md"
CON = "advisor_pilot_20261113/brainstorm_20261116/predictive_brainstorm_20261121/CONTRIBUTION_IT_ADV154_20261121.md"
PAR = "advisor_pilot_20261113/brainstorm_20261116/deepening_he_20261116/sim_harness/parametric_sensitivity_20261119/RESULT_PARAMETRIC_SENSITIVITY_HE_20261120.md"
A142 = "advisor_pilot_20261113/brainstorm_20261116/adv142_baseline_five_metric_sci_20261121/RESULT_ADV142_BASELINE_FIVE_METRIC_SCI_20261121.md"
A140 = "advisor_pilot_20261113/brainstorm_20261116/adv140_aqeilan_fig6_sci_20261121/RESULT_ADV140_AQEILAN_FIG6_SCI_20261121.md"

D1 = ("Demotion 1 (the simulated class order as an argument for the tonic-inhibition arm): the simulated order (a neurosteroid-type class second, T-type last) is no longer used as an argument for that arm; "
      "it comes from one oscillator and one structure with part of the order imposed by per-arm scales (" + PAR + "), and the class has no juvenile exposure and no measured tonic conductance; "
      "the arm waits for the E_GABA recording and a tonic-conductance measurement. Source: " + SYN + ".")
D2 = ("Demotion 2 (the Kv7 class): it stays penalised until a margin between effective and harmful exposure is measured in juveniles; effective and harmful exposures overlap in the one juvenile set, "
      "and Kv7 enters the model only as an assumed drive offset, so no simulated perturbation lifts it. Source: " + SYN + " and the data sheet of the Kv7 batch (adv098_agent_sheets_he_20261119).")
D3 = ("Demotion 3 (the T-type attribution arm, not the ethosuximide observation): the arm that attributes the ethosuximide effect to T-type channels waits; the simulation puts T-type last, held transcripts are flat from P14 to P28 and no T-type measurement exists in Wwox tissue; "
      "the in vivo ethosuximide observation itself stands as an observation. Source: " + SYN + " and the by-endpoint comparison, update on the T-type lane.")
POOL = ("POOLED-ONLY (ADV, from SCI's reading): the week-16 WOREE-over-SCAR12 contrast (printed pooled event-rate ratio about 3.4, no test printed) is carried as POOLED-ONLY: week-16 pooled; "
        "per-line ordering is unsupported at the one age with per-line data, week 7, where four lines lie within about 10 percent; the pooled gap is confounded with AAV9-EGFP exposure from week 10; "
        "the per-line week-16 table is not printed. No mechanism row and no circuit parameter may use a WOREE-specific rate until the per-line table exists. Sources: " + A142 + " and " + A140 + ". The text above is unchanged.")
CORR = ("Dated correction (IT, 2026-11-21, ADV-156; the text above is unchanged): in the first table of section 2a the levetiracetam row said 'not mapped in held sheets' for exposure and left the link missing at three places. "
        "Two routes (ChEMBL by id; PubMed field-tagged title and abstract search with metadata) now give: target action LINK MISSING (the one SV2A row carries an implausible printed value, not a potency); "
        "exposure JUVENILE_MOUSE_SINGLE_AGE (P19 CD1 mice, serum half-life 3.2 h against 1.5 h in adults, brain tissue at 4 h, total not free; abstract level); "
        "harm: no increase of developmental cell death in neonatal mice or in rat pups (abstract level); WWOX rationale NONE_HELD (no PubMed hit with WWOX terms). Perampanel, stiripentol, cannabidiol, magnesium and the vitamin and cofactor supplements are mapped in the same way in "
        "advisor_pilot_20261113/brainstorm_20261116/it_adv156_20261121/agent_states_it_adv156_20261121.tsv; the sentence 'the five or six agents with no sheet look empty because nobody looked' is now partly answered: each was searched by two routes and the result is in that table.")


def append(path, text, heading=None):
    p = Path(path)
    t = p.read_text(encoding="utf-8")
    if MARK in t:
        return "already"
    if not t.endswith("\n"):
        t += "\n"
    t += "\n" + (heading + "\n" if heading else "") + text + "\n"
    p.write_text(t, encoding="utf-8")
    return "appended"


def insert_before_last(path, anchor, text):
    p = Path(path)
    t = p.read_text(encoding="utf-8")
    if MARK in t:
        return "already"
    i = t.rindex(anchor)
    p.write_text(t[:i] + text + "\n\n" + t[i:], encoding="utf-8")
    return "inserted"


def edit_cell(path, match, col, fn):
    p = Path(path)
    lines = p.read_text(encoding="utf-8").split("\n")
    head = lines[0].split("\t")
    n_done = 0
    for n, ln in enumerate(lines):
        f = ln.split("\t")
        if n and len(f) == len(head) and all(f[head.index(k)] == v for k, v in match.items()):
            i = head.index(col)
            new = fn(f[i])
            if new != f[i]:
                f[i] = new
                lines[n] = "\t".join(f)
                n_done += 1
    if not n_done:
        return "unchanged"
    p.write_text("\n".join(lines), encoding="utf-8")
    return f"{n_done} cell(s)"


def once(add):
    return lambda s: s if MARK in s else (s + " " + add)


def main():
    out = []
    # A. demotions
    sel = BS / "generative_engine_funding_adv_20261119/SELECTION_NOTE_V1_ADV_20261119.md"
    out.append(("selection note", append(sel, "- " + D1 + "\n- " + D2 + "\n- " + D3,
                                         "## Dated lines (IT, 2026-11-21, ADV-156): three demotions after the predictive-modelling meeting (the text above is unchanged; no compound ranking changes)")))
    opp = BS / "generative_engine_funding_adv_20261119/it_adv092_20261119/opportunities.tsv"
    out.append(("OPP-05", edit_cell(opp, {"opp_id": "OPP-05"}, "chain_notes", once("[Dated 2026-11-21, IT, ADV-156: " + D2 + "]"))))
    out.append(("OPP-03", edit_cell(opp, {"opp_id": "OPP-03"}, "chain_notes", once("[Dated 2026-11-21, IT, ADV-156: " + D3 + "]"))))
    arm = BS / "ARM_TABLE_V9_NOTES_IT_20261117.md"
    out.append(("arm table notes", append(arm, "Update 2026-11-21 (IT, ADV-156; the text above is not edited; no cell, tier, origin or arm changes; hypothesis level; not medical advice): " + D1)))
    be = BS / "it_adv053_20261118/COMPARISON_BY_ENDPOINT_ADV053_IT_20261118.md"
    out.append(("by-endpoint", append(be, "## Update 2026-11-21 (IT, ADV-156; the text above is not edited): " + D3)))
    # B. pooled-only
    ctx = DR / "context_differences_it7_p4_20261029/README.md"
    out.append(("context README", append(ctx, POOL, "## Dated line (IT, 2026-11-21, ADV-156): week-16 WOREE-over-SCAR12 contrast")))
    cm = DR / "context_differences_it7_p4_20261029/context_matrix.tsv"
    for cid in ("ORG_PW", "ORG_PS"):
        out.append(("context matrix " + cid, edit_cell(cm, {"quantity_id": "Q14", "context_id": cid}, "key_caveats", once("[Dated 2026-11-21, ADV-156: week-16 WOREE-over-SCAR12 contrast is POOLED-ONLY (about 3.4, no test printed; per-line ordering unsupported at week 7; confounded with AAV9-EGFP exposure from week 10; per-line week-16 table not printed); no WOREE-specific rate may enter a mechanism row or circuit parameter.]"))))
    out.append(("RP-043", edit_cell(DR / "research_portfolio.tsv", {"id": "RP-043"}, "outcome", once("[Dated 2026-11-21, IT, ADV-156: " + POOL.split(" The text above")[0] + "]"))))
    cc = W / "research/commit_candidates/CC-20261121-ORCHESTRATOR-ADV140-FIG6-WORDING-01.md"
    out.append(("registry candidate", insert_before_last(cc, "**Not medical advice.**", "**Dated line 2026-11-21 (IT, ADV-156, same candidate; the sections above are unchanged):** " + POOL + " When this candidate is committed, the clause of 3.1 carries the pooled-only wording; the registry file itself changes only through the batch commit.")))
    out.append(("tx007", append(W / "analysis/tx007_window_and_ceiling_20260921.md", "Dated line 2026-11-21 (IT, ADV-156): " + POOL)))
    out.append(("rescue window", append(DR / "rescue_window_it6_20261029.md", "Dated line 2026-11-21 (IT, ADV-156): " + POOL)))
    # C. correction of the ADV-154 contribution
    out.append(("ADV-154 contribution", append(BS / "predictive_brainstorm_20261121/CONTRIBUTION_IT_ADV154_20261121.md", CORR)))
    for k, v in out:
        print(f"{k:28s} {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
