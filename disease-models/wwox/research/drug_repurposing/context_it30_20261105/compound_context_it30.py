#!/usr/bin/env python3
"""IT30: compound-level effects with their context, from the raw evidence files, without inventing a target.

Reads the evidence_it29_<letter>.tsv files (the raw columns, not the hand-curated signed table) and keeps every row whose
intervention is ONE named compound. A row naming several compounds, a combination (+, add-on, versus) or a regimen is a panel
row: it is listed as unattributed, never split. Per compound and theme (the package letter) it records which contexts gave which
direction, and flags a sign that flips with context. A flagged compound becomes a conditional question for the scientific queue.
Nothing is transferred from a compound to its class or to any other compound; the join to the stage tables is by name only and
says whether the compound is already a proposal there.

Usage: compound_context_it30.py run --out DIR [--stage generation_it30_p5_20261105/results_s11/proposals_it21.tsv]
       (any other argument prints this text)"""
import sys
if __name__ == "__main__" and (len(sys.argv) < 2 or sys.argv[1] != "run"):
    print(__doc__); raise SystemExit(0)
import argparse, collections, csv, glob, re
from pathlib import Path

csv.field_size_limit(10 ** 9)
DR = Path(__file__).resolve().parent.parent
PANEL = re.compile(r"[;,]|\+|\badd-on\b|\bversus\b|\bvs\b|\bplus\b|\bwith\b|\band\b|\bor\b|^\d|\b(antagonists?|agonists?|inhibitors?|blockers?|blockade|treatment|library|drugs|compounds|modulators|class)\b", re.I)
SIGNED = ("favourable", "adverse", "null", "context_dependent", "undetermined")
THEME = {"A": "myelination (small molecules)", "B": "myelination (genetic or pathway)", "C": "myelination (transfer conditions)",
         "D": "network discharge in developmental epilepsy", "E": "compensatory roles in developmental epilepsy"}


def name_key(s):
    s = re.sub(r"\(.*?\)", " ", s.lower())
    s = re.sub(r"\b(neonatal exposure|short pulse after spasm onset|exposure)\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def rd(p):
    with open(p, encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def build(evidence_glob):
    single, panel = collections.defaultdict(list), []
    for f in sorted(glob.glob(str(DR / evidence_glob))):
        letter = Path(f).stem.rsplit("_", 1)[-1]
        for r in rd(f):
            if r["intervention_type"] != "compound":
                continue
            r["_theme"] = letter
            if PANEL.search(r["intervention"]):
                panel.append(r)
            else:
                single[(name_key(r["intervention"]), letter)].append(r)
    return single, panel


def summarise(single):
    out = []
    for (comp, letter), rows in sorted(single.items()):
        dirs = collections.Counter(r["direction_on_endpoint"] for r in rows)
        ctx = collections.defaultdict(set)
        for r in rows:
            ctx[r["direction_on_endpoint"]].add((r["system"].split(",")[0][:60] + " | " + r["stress_or_context"][:50]).strip(" |"))
        fav, adv, nul = dirs.get("favourable", 0), dirs.get("adverse", 0), dirs.get("null", 0)
        if fav and adv:
            kind = "sign_flips_with_context"
        elif fav and (nul or dirs.get("context_dependent")):
            kind = "benefit_not_reproduced_or_context_dependent"
        elif dirs.get("context_dependent") and not fav and not adv:
            kind = "context_dependent_only"
        else:
            kind = "no_conflict_recorded"
        out.append(dict(compound=comp, theme=THEME.get(letter, letter), package=letter, n_rows=len(rows),
                        n_sources=len({r["source_id"] for r in rows}), directions="; ".join(f"{k}={v}" for k, v in sorted(dirs.items())),
                        contexts_by_direction=" || ".join(f"{k}: " + " / ".join(sorted(v)) for k, v in sorted(ctx.items())),
                        conflict=kind, attribution="compound_only" if all(r["attribution"] == "compound_only" for r in rows) else "mixed",
                        rows=",".join(r["row_id"] for r in rows)))
    return out


def stage_join(summary, stage_path):
    sys.path.insert(0, str(DR / "generation_it21_p2_20261103"))
    import importlib.util
    spec = importlib.util.spec_from_file_location("gen21", DR / "generation_it21_p2_20261103/run_generation_it21.py")
    g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
    by = collections.defaultdict(list)
    for p in rd(stage_path):
        by[g.base_name(p["compound"])].append(p)
    for s in summary:
        hits = by.get(g.base_name(s["compound"]), [])
        s["in_stage"] = "yes" if hits else "no"
        s["stage_proposals"] = ",".join(sorted({h["proposal_id"] for h in hits}))[:200]
        s["stage_handoff_eligible"] = "yes" if any(h["handoff_eligible"] == "yes" for h in hits) else ("no" if hits else "")
    return summary


def class_questions(path):
    """The lesion-class table of case 2 (agent classes, not compounds) becomes class-level conditional questions: only the classes whose sign
    differs between the two lesion types are asked. Nothing is carried to a member compound."""
    out = []
    for r in rd(path):
        if not r["separates_A_from_B"].lower().startswith("yes"):
            continue
        out.append(dict(compound=r["agent_class"] + " (class level)", theme=THEME["D"], conflict="sign_flips_with_lesion_class", in_stage="", stage_handoff_eligible="",
                        question=(f"The sign of the class {r['agent_class']} differs with the lesion: {r['predicted_sign_if_WWOX_is_A_like']} if the lesion is inhibition-loss-like, "
                                  f"{r['predicted_sign_if_WWOX_is_B_like']} if excitatory-gain-like. Which lesion class is the reference genotype's? A measurement that separates the two comes before any member of the class is read as a lever; "
                                  f"no transfer to a named compound."), evidence_rows=r["evidence_rows"]))
    return out


def question(s):
    c = s["compound"]
    if s["conflict"] == "sign_flips_with_context":
        return (f"The effect of {c} on {s['theme']} is favourable in some contexts and adverse in others ({s['contexts_by_direction']}). "
                f"Which of these contexts is the reference genotype's? Until a measurement in a matched system answers it, {c} is a probe with a stated condition, not a lever; no class transfer.")
    return (f"The effect of {c} on {s['theme']} is not reproduced across contexts ({s['directions']}). What differs between the contexts that gave a benefit and the ones that did not? "
            f"Measure it with a matched control arm before reading {c} as a lever.")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("cmd"); ap.add_argument("--out", required=True)
    ap.add_argument("--stage", default="generation_it30_p5_20261105/results_s11/proposals_it21.tsv")
    ap.add_argument("--evidence", default="phenotype_first_it29_20261105/p3_*/evidence_it29_*.tsv")
    a = ap.parse_args()
    single, panel = build(a.evidence)
    summary = stage_join(summarise(single), DR / a.stage)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    cols = list(summary[0])
    with open(out / "compound_context_it30.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(summary)
    qs = [dict(question_id=f"CQ-IT30-{i:02d}", compound=s["compound"], theme=s["theme"], conflict=s["conflict"], in_stage=s["in_stage"],
               stage_handoff_eligible=s["stage_handoff_eligible"], question=question(s), evidence_rows=s["rows"])
          for i, s in enumerate([s for s in summary if s["conflict"] in ("sign_flips_with_context", "benefit_not_reproduced_or_context_dependent")], 1)]
    qs += class_questions(DR / "phenotype_first_it29_20261105/case2_lesion_conditional_it29.tsv")
    for i, q in enumerate(qs, 1):
        q["question_id"] = f"CQ-IT30-{i:02d}"
    qs = [{**{"question_id": q["question_id"]}, **{k: v for k, v in q.items() if k != "question_id"}} for q in qs]
    with open(out / "conditional_questions_it30.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(qs[0]), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(qs)
    with open(out / "panel_rows_unattributed_it30.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["row_id", "package", "intervention", "direction_on_endpoint", "why_not_split"])
        for r in panel:
            w.writerow([r["row_id"], r["_theme"], r["intervention"], r["direction_on_endpoint"], "combination or several compounds in one row: the result belongs to the panel"])
    print(f"compounds {len(summary)} · flagged {len(qs)} · in stage {sum(s['in_stage'] == 'yes' for s in summary)} · panel rows {len(panel)}")


if __name__ == "__main__":
    main()
