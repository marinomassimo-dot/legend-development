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
    props = rd(DR / "generation_it22_p1_20261103/results_p4/proposals_it21.tsv")
    norm = lambda s: re.sub(r"[^a-z0-9]+", "", (s or "").lower())
    fam_names = {}
    for r in props:
        fam_names.setdefault(r["family_id"], set()).update({norm(r["compound"]), norm(r["base_name"])})
    fams = {}
    for r in nov:
        for f in (r["legend_families"] or "").split(";"):
            # IT23 P6 verifier F16: the family map of novelty.tsv was built by name for most nodes; keep a join only when the EC-KG name equals one of the family's own compound names exactly
            # (an ion or a counter-ion node such as 'citrate(3-)' no longer reaches a lithium-citrate family), and record the route
            if f and norm(r["compound_name"]) in fam_names.get(f, ()):
                fams.setdefault(r["compound_id"], set()).add(f)
    ext = rd(HERE / "extract_ecKG_wwox.tsv")
    out = {}
    for r in ext:
        if r["predicate"] != "biolink:has_adverse_event" or r["primary_knowledge_source"] != "infores:faers" or not SEIZURE.search(r["object_name"]):
            continue
        for f in fams.get(r["subject"], ()):
            e = out.setdefault((f, r["subject"]), dict(family_id=f, compound_id=r["subject"], compound_name=r["subject_name"], events=set(), match_route="exact normalised name (EC-KG nodes expose no ChEMBL cross-reference)", source="infores:faers", licence=r["source_licence_stated"] or "CC0 (FAERS, via EC-KG CC BY 4.0)"))
            e["events"].add(r["object_name"])
    rows = [dict(e, events="; ".join(sorted(e["events"])), n_events=len(e["events"]),
                 completeness="INCOMPLETE BY CONSTRUCTION: only events whose disease node is a direct WWOX neighbour in the extract; the generic 'Seizure' term is not covered",
                 reading="spontaneous reports: an association with a confounded denominator, not a safety verdict; absence is not evidence of safety") for e in out.values()]
    rows.sort(key=lambda x: (x["compound_name"].lower(), x["family_id"]))
    with open(HERE / "harm_signals_it23.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["family_id", "compound_id", "compound_name", "n_events", "events", "match_route", "completeness", "source", "licence", "reading"], delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    act = {}
    for r in csv.DictReader(gzip.open(DR / "generation_it21_p2_20261103/results/actions/family_actions.tsv.gz", "rt", encoding="utf-8"), delimiter="\t"):
        act[(r["family_id"], r["target_symbol"].upper())] = r
    # IT24 P12: the provenance of the SIGN, not of the pair. `novelty.tsv` aggregates origins and evidence classes over every edge of a pair; the sign can rest on a different edge
    # (a prediction) than the one that makes the pair look observed. sign_rows_it24.tsv holds only the sign-bearing edges of the discordant pairs (source, evidence class).
    signrows = {}
    if (HERE / "sign_rows_it24.tsv").exists():
        for x in rd(HERE / "sign_rows_it24.tsv"):
            signrows.setdefault((x["compound"], x["target"]), []).append(x)
    disc = []
    for r in nov:
        if r["status"] != "IN_LEGEND_OPPOSITE_SIGN":
            continue
        for f in (r["legend_families"] or "").split(";"):
            a = act.get((f, r["target_symbol_in_legend"].upper()))
            if a:
                disc.append(dict(compound_name=r["compound_name"], target=r["target_symbol_in_legend"], family_id=f, legend_sign=a["mean_sign"], legend_group=a["groups"], legend_scope=a["scopes"], legend_flags=a["flags"],
                                 eckg_sign=r["eckg_activity_sign"], eckg_non_prediction_origins=r["origins_non_prediction"], eckg_best_evidence=r["best_evidence_class"],
                                 eckg_sign_evidence=";".join(sorted({x["evidence"] for x in signrows.get((r["compound_name"], r["target_symbol_in_legend"]), [])})),
                                 eckg_sign_origins=";".join(sorted({x["source"] for x in signrows.get((r["compound_name"], r["target_symbol_in_legend"]), []) if x["evidence"] != "PREDICTION"}))))
                disc[-1]["reading"] = ("prompt to read the source; the EC-KG SIGN rests on prediction rows only" + ("" if not r["origins_non_prediction"] else " (the pair has non-prediction origins, none of them carries this sign)")
                                       if signrows and not disc[-1]["eckg_sign_origins"] else "prompt to read the source; the EC-KG sign has a non-prediction origin" if signrows else
                                       ("prompt to read the source; EC-KG rests on prediction rows only" if not r["origins_non_prediction"] else "prompt to read the source; pair-level origins only (sign provenance not available)"))
    with open(HERE / "sign_discordance_it23.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(disc[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(disc)
    print(len(rows), "family-level seizure signals;", len(disc), "sign discordances")


if __name__ == "__main__":
    main()
