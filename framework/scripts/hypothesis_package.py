#!/usr/bin/env python3
"""Read a physiological-hypothesis package in place and hand a consumer the whole chain for one investigation.

A package folder (for example membrane_hypotheses_20261108/output/) already holds hypotheses.tsv,
alternatives.tsv, experiments.tsv and, for some packages, prediction_matrix.tsv. This reader joins them by the
identifiers they already carry and returns the rows verbatim, so no copy exists to fall out of step and no
interpretation is hidden in a parser. The one interpretive step — which need, investigation and card a hypothesis
would reach — is a committed, reviewable file in the package (consumer_links.tsv), checked here against the real
ids in needs.json and the investigations table.

What a record is: a physiological hypothesis about a preparation (kind physiological_hypothesis). It has no gene
pair, no HGNC id, no sign and no direction; none is made up, and `gene_arc` is always False. Bridges stay in
bridges.tsv.

Cross-references are literal identifier tokens found in the cells (an alternative id inside
competing_explanation, a hypothesis id inside an experiment's `hypothesis` cell, an arm id inside
comparison_arms). A token that matches no known id is listed in `unresolved_refs`, never guessed. The matrix
columns (H1..H7) are the producer's own labels and are not mapped to alternative ids.

A missing link is UNLINKED, and a missing experiment is NO_EXPERIMENT: both mean "not stated here", never
"tested and absent", and never evidence against a compound.

  python3 framework/scripts/hypothesis_package.py show --inv INV-05
  python3 framework/scripts/hypothesis_package.py check
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DR = REPO / "disease-models/wwox/research/drug_repurposing"
PACKAGES = ("membrane_hypotheses_20261108", "ampa_nmda_discrim_20261108")
LINK_FIELDS = ("hyp_id", "kind", "need_id", "inv_id", "card_ids", "link_state", "carried_check", "source")
LINK_STATES = ("PROPOSED_NOT_APPLIED", "CARRIED_IN_TEXT")
INV_TABLES = ("investigations_it20.tsv", "investigations.tsv")
INV_DIR = DR / "ranking_it8_p9_20261029"


class PackageError(ValueError):
    pass


def _tsv(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def _tokens(text: str, known) -> tuple[list[str], list[str]]:
    """Known ids found as whole tokens in text, in order, and id-shaped tokens that match none."""
    hit, miss = [], []
    for t in re.findall(r"\b[A-Z]{1,3}\d{1,3}\b", text or ""):
        (hit if t in known else miss).append(t)
    return list(dict.fromkeys(hit)), list(dict.fromkeys(miss))


def load_package(pkg: Path) -> dict:
    pkg = Path(pkg)
    out = pkg / "output" if (pkg / "output").is_dir() else pkg
    hyps = {r["hyp_id"]: r for r in _tsv(out / "hypotheses.tsv")}
    alts = {r["alt_id"]: r for r in _tsv(out / "alternatives.tsv")}
    exps = {r["exp_id"]: r for r in _tsv(out / "experiments.tsv")}
    mp = out / "prediction_matrix.tsv"
    arms = {r["arm_id"]: r for r in _tsv(mp)} if mp.exists() else {}
    op = out / "observations.tsv"
    obs = {r[next(iter(r))] for r in _tsv(op)} if op.exists() else set()
    lp = out / "consumer_links.tsv"
    links = _tsv(lp) if lp.exists() else []
    return {"dir": out, "hyps": hyps, "alts": alts, "exps": exps, "arms": arms, "obs": obs, "links": links}


def _need_ids() -> set[str]:
    with open(DR / "needs/needs.json", encoding="utf-8") as f:
        return {n["id"] for n in json.load(f)["needs"]}


def _inv_rows(inv_dir: Path = INV_DIR) -> dict[str, dict]:
    for name in INV_TABLES:
        if (inv_dir / name).exists():
            return {r["inv_id"]: r for r in _tsv(inv_dir / name)}
    raise PackageError("no investigations table found")


def validate(pkg: dict, needs: set[str] | None = None, invs: dict | None = None, cards: Path | None = None) -> list[str]:
    needs = _need_ids() if needs is None else needs
    invs = _inv_rows() if invs is None else invs
    cards = (DR / "cards") if cards is None else cards
    errs = []
    for i, l in enumerate(pkg["links"]):
        w = f"{pkg['dir'].parent.name} link {i} ({l.get('hyp_id')})"
        miss = [k for k in LINK_FIELDS if k not in l]
        if miss:
            errs.append(f"{w}: missing {miss}")
            continue
        if l["hyp_id"] not in pkg["hyps"]:
            errs.append(f"{w}: hypothesis id not in hypotheses.tsv")
        if l["kind"] != "physiological_hypothesis":
            errs.append(f"{w}: kind {l['kind']!r} (this reader carries physiological hypotheses only)")
        if l["need_id"] not in needs:
            errs.append(f"{w}: need {l['need_id']!r} not in needs.json")
        if l["inv_id"] not in invs:
            errs.append(f"{w}: investigation {l['inv_id']!r} not in the investigations table")
        if l["link_state"] not in LINK_STATES:
            errs.append(f"{w}: link_state {l['link_state']!r}")
        for c in filter(None, l["card_ids"].split(";")):
            if not (cards / f"{c}.card.json").exists():
                errs.append(f"{w}: card {c!r} not found")
        for chk in filter(None, l["carried_check"].split(";")):
            fld, _, sub = chk.partition(":")
            if l["link_state"] == "CARRIED_IN_TEXT" and sub not in (invs.get(l["inv_id"], {}).get(fld) or ""):
                errs.append(f"{w}: carried_check {chk!r} not found in {l['inv_id']}.{fld}")
        if l["link_state"] == "CARRIED_IN_TEXT" and not l["carried_check"]:
            errs.append(f"{w}: CARRIED_IN_TEXT without a carried_check")
    return errs


HYP_CELLS = ("status", "chain", "competing_explanation", "counter_evidence", "weakening_result",
             "discriminating_experiment", "what_would_change_the_decision")


def record_for(pkgs: list[dict], inv_id: str) -> dict:
    """The consumer record for one investigation: every linked hypothesis with its alternatives, experiments and arms, verbatim."""
    hyps = []
    for pkg in pkgs:
        alts, arms, cols = pkg["alts"], pkg["arms"], _matrix_columns(pkg)
        known = set(alts) | set(pkg["hyps"]) | set(arms) | set(cols) | set(pkg["exps"]) | pkg["obs"]
        for l in (x for x in pkg["links"] if x["inv_id"] == inv_id):
            h = pkg["hyps"][l["hyp_id"]]
            cited = {c: _tokens(h.get(c, ""), known)[0] for c in HYP_CELLS}
            ids = list(dict.fromkeys(t for c in HYP_CELLS for t in cited[c]))
            unresolved = list(dict.fromkeys(t for c in HYP_CELLS for t in _tokens(h.get(c, ""), known)[1]))
            exp_rows = []
            for e in pkg["exps"].values():
                if l["hyp_id"] in _tokens(e["hypothesis"], set(pkg["hyps"]))[0]:
                    e_ids, e_miss = _tokens(e["comparison_arms"], known)
                    exp_rows.append({"row": e, "arms": [arms[x] for x in e_ids if x in arms],
                                     "alternatives": [x for x in e_ids if x in alts], "unresolved_refs": e_miss})
            hyps.append({
                "hyp_id": l["hyp_id"], "package": pkg["dir"].parent.name, "kind": l["kind"], "gene_arc": False,
                "need_id": l["need_id"], "card_ids": [c for c in l["card_ids"].split(";") if c],
                "link_state": l["link_state"], "hypothesis": h,
                "alternatives": [alts[x] for x in ids if x in alts],
                "other_hypotheses_cited": [x for x in ids if x in pkg["hyps"] and x != l["hyp_id"]],
                "matrix_columns_cited": {x: cols[x] for x in ids if x in cols},
                "arms_cited": [x for x in ids if x in arms],
                "unresolved_refs": unresolved,
                "experiments": exp_rows,
                "experiment_state": "STATED" if exp_rows else "NO_EXPERIMENT",
            })
    return {"inv_id": inv_id, "state": "LINKED" if hyps else "UNLINKED", "hypotheses": hyps}


def _matrix_columns(pkg: dict) -> dict[str, str]:
    """Matrix columns named H<n>_<label>: the producer's own labels, matched by their literal prefix and never mapped to alternative ids."""
    if not pkg["arms"]:
        return {}
    first = next(iter(pkg["arms"].values()))
    return {k.split("_")[0]: k for k in first if re.match(r"H\d+_", k)}


def load_all() -> list[dict]:
    return [load_package(DR / p) for p in PACKAGES]


def _brief(rec: dict) -> str:
    L = [f"{rec['inv_id']}: {rec['state']}"]
    if rec["state"] == "UNLINKED":
        L.append("  no package states a hypothesis for this investigation; that is not evidence against it or its compounds")
    for h in rec["hypotheses"]:
        L.append(f"  {h['hyp_id']} [{h['package']}] kind={h['kind']} gene_arc={h['gene_arc']} need={h['need_id']} state={h['link_state']} cards={','.join(h['card_ids']) or '-'}")
        L.append(f"    status: {h['hypothesis']['status'][:140]}")
        L.append(f"    rivals (alternatives): {', '.join(a['alt_id'] for a in h['alternatives']) or '-'}   other hypotheses: {', '.join(h['other_hypotheses_cited']) or '-'}   matrix columns: {', '.join(h['matrix_columns_cited'].values()) or '-'}")
        L.append(f"    unresolved refs: {', '.join(h['unresolved_refs']) or '-'}")
        for e in h["experiments"]:
            L.append(f"    {e['row']['exp_id']} arms={','.join(a['arm_id'] for a in e['arms']) or '-'} alts={','.join(e['alternatives']) or '-'} unresolved={','.join(e['unresolved_refs']) or '-'}")
        if not h["experiments"]:
            L.append("    NO_EXPERIMENT (not stated here)")
    return "\n".join(L)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("show", help="print the consumer record for one investigation")
    s.add_argument("--inv", required=True)
    s.add_argument("--json", action="store_true")
    sub.add_parser("check", help="validate every package's consumer_links.tsv against the real ids")
    a = ap.parse_args(argv)
    pkgs = load_all()
    if a.cmd == "check":
        errs = [e for p in pkgs for e in validate(p)]
        print("\n".join(errs) if errs else f"OK: {sum(len(p['links']) for p in pkgs)} links over {len(pkgs)} packages")
        return 1 if errs else 0
    rec = record_for(pkgs, a.inv)
    print(json.dumps(rec, indent=1, ensure_ascii=False) if a.json else _brief(rec))
    return 0


if __name__ == "__main__":
    sys.exit(main())
