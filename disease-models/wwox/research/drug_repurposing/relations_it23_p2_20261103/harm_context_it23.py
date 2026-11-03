#!/usr/bin/env python3
"""IT23 P2: turn the two EC-KG relation types the generator had no table for into things the generator can carry, from the already-extracted permissive rows.

  harm_context_it23.py            writes harm_signals_it23.tsv and sign_discordance_it23.tsv next to this file

1. harm_signals_it23.tsv: FAERS spontaneous-report adverse-event rows (infores:faers, CC0, carried by EC-KG under CC BY 4.0) whose event is a seizure, convulsion, epilepsy or
   status epilepticus, joined to LEGEND chemical families through the compound ids of novelty.tsv (id join, never a name join). A spontaneous report is an ASSOCIATION with a
   confounded denominator (the people treated may already have epilepsy); it is carried as a limit on a proposal, never as a verdict, never as evidence of safety when absent.
2. sign_discordance_it23.tsv: the pairs where EC-KG's activity sign opposes the generator's, with LEGEND's own row (group, scope, flags) and what EC-KG rests on (prediction only or
   not). A discordance is a prompt to read the source; it does not say which side is wrong.
Standard library only; recomputes nothing but the join.
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import csv, gzip, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
SEIZURE = re.compile(r"seiz|convuls|epilep|status epilepticus", re.I)


def rd(p):
    with open(p, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def main():
    nov = rd(HERE / "novelty.tsv")
    fams = {}
    for r in nov:
        for f in (r["legend_families"] or "").split(";"):
            if f:
                fams.setdefault(r["compound_id"], set()).add(f)
    ext = rd(HERE / "extract_ecKG_wwox.tsv")
    out = {}
    for r in ext:
        if r["predicate"] != "biolink:has_adverse_event" or r["primary_knowledge_source"] != "infores:faers" or not SEIZURE.search(r["object_name"]):
            continue
        for f in fams.get(r["subject"], ()):
            e = out.setdefault((f, r["subject"]), dict(family_id=f, compound_id=r["subject"], compound_name=r["subject_name"], events=set(), source="infores:faers", licence=r["source_licence_stated"] or "CC0 (FAERS, via EC-KG CC BY 4.0)"))
            e["events"].add(r["object_name"])
    rows = [dict(e, events="; ".join(sorted(e["events"])), n_events=len(e["events"]),
                 reading="spontaneous reports: an association with a confounded denominator, not a safety verdict; absence is not evidence of safety") for e in out.values()]
    rows.sort(key=lambda x: (x["compound_name"].lower(), x["family_id"]))
    with open(HERE / "harm_signals_it23.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["family_id", "compound_id", "compound_name", "n_events", "events", "source", "licence", "reading"], delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    act = {}
    for r in csv.DictReader(gzip.open(DR / "generation_it21_p2_20261103/results/actions/family_actions.tsv.gz", "rt", encoding="utf-8"), delimiter="\t"):
        act[(r["family_id"], r["target_symbol"].upper())] = r
    disc = []
    for r in nov:
        if r["status"] != "IN_LEGEND_OPPOSITE_SIGN":
            continue
        for f in (r["legend_families"] or "").split(";"):
            a = act.get((f, r["target_symbol_in_legend"].upper()))
            if a:
                disc.append(dict(compound_name=r["compound_name"], target=r["target_symbol_in_legend"], family_id=f, legend_sign=a["mean_sign"], legend_group=a["groups"], legend_scope=a["scopes"], legend_flags=a["flags"],
                                 eckg_sign=r["eckg_activity_sign"], eckg_non_prediction_origins=r["origins_non_prediction"], eckg_best_evidence=r["best_evidence_class"],
                                 reading="prompt to read the source; EC-KG rests on prediction rows only" if not r["origins_non_prediction"] else "prompt to read the source; both sides have a non-prediction origin"))
    with open(HERE / "sign_discordance_it23.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(disc[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(disc)
    print(len(rows), "family-level seizure signals;", len(disc), "sign discordances")


if __name__ == "__main__":
    main()
