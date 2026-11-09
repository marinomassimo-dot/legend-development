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

Which packages are consumed is explicit: `hypothesis_packages.tsv` lists each folder, its role and why. A folder
that is merely present is not read. Two roles are kept apart, because their rows mean different things:
`physiological_hypotheses` (hypotheses, alternatives, experiments, matrix; linked to investigations by the package's
consumer_links.tsv) and `pharmacological_comparison` (comparison.tsv rows with new_measurements.tsv and decisive.tsv;
linked by the manifest's inv_id). Every returned row carries `source_ref` (repo-relative file and line). An alternative's
`matrix_column`, when the package writes one, is read and validated against the matrix header; a blank stays unmapped.

Unresolved tokens are classified by simple rules, never by meaning: AGE (P13), CARD_ID (a card file with that prefix),
PROBE_NAME (named in the package's probes.tsv), BROKEN_REFERENCE (the id family exists but that number does not) and
UNCLASSIFIED. Only BROKEN_REFERENCE is a defect. Naming a term in a cell shows it is named; only the output of a path
that calls `record_for` / `comparison_for` shows it is consumed.

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
MANIFEST = DR / "hypothesis_packages.tsv"
ROLES = ("physiological_hypotheses", "pharmacological_comparison")
MANIFEST_FIELDS = ("package", "dir", "role", "inv_id", "why")
LINK_FIELDS = ("hyp_id", "kind", "need_id", "inv_id", "card_ids", "link_state", "carried_check", "source")
LINK_STATES = ("PROPOSED_NOT_APPLIED", "CARRIED_IN_TEXT")
INV_TABLES = ("investigations_it20.tsv", "investigations.tsv")
INV_DIR = DR / "ranking_it8_p9_20261029"
REF_CLASSES = ("AGE", "CARD_ID", "PROBE_NAME", "BROKEN_REFERENCE", "UNCLASSIFIED")


class PackageError(ValueError):
    pass


def _rel(path: Path) -> str:
    try:
        return str(Path(path).resolve().relative_to(REPO))
    except ValueError:
        return str(path)


def _tsv_lined(path: Path) -> list[tuple[dict, str]]:
    """Rows verbatim, each with its repo-relative file:line (the line where the row starts)."""
    out = []
    with open(path, newline="", encoding="utf-8") as f:
        rd = csv.DictReader(f, delimiter="\t")
        rd.fieldnames  # reads the header, so the next row starts on the line after it
        last = rd.line_num
        for r in rd:
            out.append((r, f"{_rel(path)}:{last + 1}"))
            last = rd.line_num
    return out


def _tsv(path: Path) -> list[dict]:
    return [r for r, _ in _tsv_lined(path)]


def _blocked_keys(cell: str, all_keys) -> list[str]:
    """Comparison keys a measurement blocks: tokens before ' (' separated by ';', or every key for the literal words 'all rows'."""
    toks = [t.split(" (")[0].strip() for t in (cell or "").split(";") if t.strip()]
    return list(all_keys) if any(t.lower() == "all rows" for t in toks) else toks


def _tokens(text: str, known) -> tuple[list[str], list[str]]:
    """Known ids found as whole tokens in text, in order, and id-shaped tokens that match none."""
    hit, miss = [], []
    for t in re.findall(r"\b[A-Z]{1,3}\d{1,3}\b", text or ""):
        (hit if t in known else miss).append(t)
    return list(dict.fromkeys(hit)), list(dict.fromkeys(miss))


def classify_ref(token: str, known, probe_text: str = "", cards: Path | None = None) -> str:
    """Simple, checkable rules; never a reading of meaning. BROKEN_REFERENCE is the only defect class."""
    cards = (DR / "cards") if cards is None else cards
    if cards.is_dir() and any(cards.glob(f"{token}_*.card.json")):
        return "CARD_ID"
    if re.fullmatch(r"P\d{1,3}", token):
        return "AGE"
    if token.lower() in probe_text:
        return "PROBE_NAME"
    m = re.fullmatch(r"([A-Z]{1,3})(\d{1,3})", token)
    if m and any(re.fullmatch(rf"{m.group(1)}\d{{{len(m.group(2))}}}", k) for k in known):
        return "BROKEN_REFERENCE"
    return "UNCLASSIFIED"


def load_package(pkg: Path) -> dict:
    pkg = Path(pkg)
    out = pkg / "output" if (pkg / "output").is_dir() else pkg
    refs = {}

    def keyed(name, key, tag):
        d = {}
        for r, ref in _tsv_lined(out / name):
            d[r[key]] = r
            refs[f"{tag}:{r[key]}"] = ref
        return d

    hyps = keyed("hypotheses.tsv", "hyp_id", "hyp")
    alts = keyed("alternatives.tsv", "alt_id", "alt")
    exps = keyed("experiments.tsv", "exp_id", "exp")
    mp = out / "prediction_matrix.tsv"
    arms = keyed("prediction_matrix.tsv", "arm_id", "arm") if mp.exists() else {}
    op = out / "observations.tsv"
    obs = {r[next(iter(r))] for r in _tsv(op)} if op.exists() else set()
    pp = out / "probes.tsv"
    probe_text = pp.read_text(encoding="utf-8").lower() if pp.exists() else ""
    lp = out / "consumer_links.tsv"
    links = _tsv(lp) if lp.exists() else []
    return {"role": "physiological_hypotheses", "dir": out, "hyps": hyps, "alts": alts, "exps": exps, "arms": arms, "obs": obs,
            "links": links, "refs": refs, "probe_text": probe_text}


def load_comparison(pkg: Path) -> dict:
    """A pharmacological comparison: comparison.tsv rows (keyed by the text before ' ('), new_measurements.tsv, decisive.tsv."""
    pkg = Path(pkg)
    out = pkg / "output" if (pkg / "output").is_dir() else pkg
    refs, rows, meas, dec = {}, {}, {}, {}
    for r, ref in _tsv_lined(out / "comparison.tsv"):
        k = r["hyp_id"].split(" (")[0].strip()
        rows[k] = r
        refs[f"cmp:{k}"] = ref
    for r, ref in _tsv_lined(out / "new_measurements.tsv"):
        meas[r["meas_id"]] = r
        refs[f"meas:{r['meas_id']}"] = ref
    dp = out / "decisive.tsv"
    if dp.exists():
        for r, ref in _tsv_lined(dp):
            dec[r["prop_id"]] = r
            refs[f"dec:{r['prop_id']}"] = ref
    return {"role": "pharmacological_comparison", "dir": out, "cmp": rows, "meas": meas, "dec": dec, "refs": refs}


def _need_ids() -> set[str]:
    with open(DR / "needs/needs.json", encoding="utf-8") as f:
        return {n["id"] for n in json.load(f)["needs"]}


def _inv_rows(inv_dir: Path = INV_DIR) -> dict[str, dict]:
    for name in INV_TABLES:
        if (inv_dir / name).exists():
            return {r["inv_id"]: r for r in _tsv(inv_dir / name)}
    raise PackageError("no investigations table found")


def read_manifest(path: Path = MANIFEST) -> list[dict]:
    return _tsv(path) if Path(path).exists() else []


def load_all(manifest: Path = MANIFEST) -> list[dict]:
    """Only the folders the manifest names, in its order. A folder that is merely present is not read."""
    out = []
    for m in read_manifest(manifest):
        d = DR / m["dir"]
        p = load_package(d) if m["role"] == "physiological_hypotheses" else load_comparison(d)
        p.update({"name": m["package"], "inv_id": m.get("inv_id") or "", "why": m.get("why") or ""})
        out.append(p)
    return out


def alt_columns(pkg: dict) -> dict[str, str]:
    """alt_id -> matrix column header, from the alternatives' own `matrix_column` cell; blank stays unmapped."""
    return {a: r["matrix_column"].strip() for a, r in pkg["alts"].items() if (r.get("matrix_column") or "").strip()}


def validate(pkg: dict, needs: set[str] | None = None, invs: dict | None = None, cards: Path | None = None) -> list[str]:
    needs = _need_ids() if needs is None else needs
    invs = _inv_rows() if invs is None else invs
    cards = (DR / "cards") if cards is None else cards
    errs = []
    if pkg.get("role") == "pharmacological_comparison":
        w = f"{pkg['dir'].parent.name} comparison"
        if pkg.get("inv_id") not in invs:
            errs.append(f"{w}: manifest inv_id {pkg.get('inv_id')!r} not in the investigations table")
        for k, r in pkg["meas"].items():
            blocked = _blocked_keys(r["blocks_which_comparison_row"], pkg["cmp"])
            errs += [f"{w}: measurement {k} blocks {b!r}, not a comparison row key" for b in blocked if b not in pkg["cmp"]]
        return errs
    cols = set(_matrix_columns(pkg).values())
    for a, c in alt_columns(pkg).items():
        if c not in cols:
            errs.append(f"{pkg['dir'].parent.name} alternative {a}: matrix_column {c!r} is not a column of prediction_matrix.tsv")
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


def validate_manifest(manifest: Path = MANIFEST) -> list[str]:
    errs = []
    for i, m in enumerate(read_manifest(manifest)):
        w = f"manifest row {i} ({m.get('package')})"
        if any(not (m.get(k) or "").strip() for k in ("package", "dir", "role", "why")):
            errs.append(f"{w}: package, dir, role and why are required")
        if m.get("role") not in ROLES:
            errs.append(f"{w}: role {m.get('role')!r}")
        if not (DR / (m.get("dir") or "x")).is_dir():
            errs.append(f"{w}: directory {m.get('dir')!r} not found")
        if m.get("role") == "pharmacological_comparison" and not (m.get("inv_id") or "").strip():
            errs.append(f"{w}: a comparison names the investigation it belongs to")
    return errs


def unlisted_packages(manifest: Path = MANIFEST) -> list[str]:
    """Package folders that look like inputs but are not in the manifest: information, never a reason to read them."""
    listed = {m["dir"] for m in read_manifest(manifest)}
    found = []
    for out in sorted(DR.glob("*/output")):
        if (out / "hypotheses.tsv").exists() or (out / "comparison.tsv").exists():
            d = out.parent.name
            if d not in listed:
                found.append(d)
    return found


HYP_CELLS = ("status", "chain", "competing_explanation", "counter_evidence", "weakening_result",
             "discriminating_experiment", "what_would_change_the_decision")


def _matrix_columns(pkg: dict) -> dict[str, str]:
    """Matrix columns named H<n>_<label>, keyed by their literal prefix H<n>."""
    if not pkg["arms"]:
        return {}
    first = next(iter(pkg["arms"].values()))
    return {k.split("_")[0]: k for k in first if re.match(r"H\d+_", k)}


def record_for(pkgs: list[dict], inv_id: str) -> dict:
    """The consumer record for one investigation: every linked physiological hypothesis with its alternatives, experiments and arms, verbatim."""
    hyps = []
    for pkg in (p for p in pkgs if p.get("role") == "physiological_hypotheses"):
        alts, arms, cols = pkg["alts"], pkg["arms"], _matrix_columns(pkg)
        acol = alt_columns(pkg)
        known = set(alts) | set(pkg["hyps"]) | set(arms) | set(cols) | set(pkg["exps"]) | pkg["obs"]
        for l in (x for x in pkg["links"] if x["inv_id"] == inv_id):
            h = pkg["hyps"][l["hyp_id"]]
            cited = {c: _tokens(h.get(c, ""), known)[0] for c in HYP_CELLS}
            ids = list(dict.fromkeys(t for c in HYP_CELLS for t in cited[c]))
            unresolved = list(dict.fromkeys(t for c in HYP_CELLS for t in _tokens(h.get(c, ""), known)[1]))
            cited_cols = {x: cols[x] for x in ids if x in cols}
            direct = [x for x in ids if x in alts]
            # an alternative that writes the column of a matrix column the hypothesis cites is reached by that column
            via = [a for a, c in acol.items() if c in cited_cols.values() and a not in direct]
            want_cols = list(dict.fromkeys([acol[a] for a in direct if a in acol] + list(cited_cols.values())))
            exp_rows = []
            refs = {f"hyp:{l['hyp_id']}": pkg["refs"].get(f"hyp:{l['hyp_id']}")}
            for a in direct + via:
                refs[f"alt:{a}"] = pkg["refs"].get(f"alt:{a}")
            for e in pkg["exps"].values():
                if l["hyp_id"] in _tokens(e["hypothesis"], set(pkg["hyps"]))[0]:
                    e_ids, e_miss = _tokens(e["comparison_arms"], known)
                    e_arms = [arms[x] for x in e_ids if x in arms]
                    refs[f"exp:{e['exp_id']}"] = pkg["refs"].get(f"exp:{e['exp_id']}")
                    expected = []
                    for ar in e_arms:
                        refs[f"arm:{ar['arm_id']}"] = pkg["refs"].get(f"arm:{ar['arm_id']}")
                        for c in want_cols:
                            if c in ar:
                                expected.append({"arm_id": ar["arm_id"], "column": c, "predicted": ar[c], "prediction_label": ar.get("prediction_label", "")})
                    exp_rows.append({"row": e, "arms": e_arms, "alternatives": [x for x in e_ids if x in alts],
                                     "expected_results": expected, "unresolved_refs": e_miss})
            hyps.append({
                "hyp_id": l["hyp_id"], "package": pkg["dir"].parent.name, "kind": l["kind"], "gene_arc": False,
                "need_id": l["need_id"], "card_ids": [c for c in l["card_ids"].split(";") if c],
                "link_state": l["link_state"], "hypothesis": h,
                "alternatives": [alts[x] for x in direct],
                "alternatives_via_matrix_column": [alts[x] for x in via],
                "other_hypotheses_cited": [x for x in ids if x in pkg["hyps"] and x != l["hyp_id"]],
                "matrix_columns_cited": cited_cols,
                "arms_cited": [x for x in ids if x in arms],
                "unresolved_refs": unresolved,
                "ref_classes": {t: classify_ref(t, known, pkg["probe_text"]) for t in unresolved},
                "experiments": exp_rows,
                "experiment_state": "STATED" if exp_rows else "NO_EXPERIMENT",
                "source_refs": refs,
            })
    return {"inv_id": inv_id, "state": "LINKED" if hyps else "UNLINKED", "hypotheses": hyps}


def comparison_for(pkgs: list[dict], inv_id: str) -> dict:
    """The pharmacological comparison rows of the packages the manifest ties to this investigation: a different kind of record, not merged with hypotheses."""
    out = []
    for pkg in (p for p in pkgs if p.get("role") == "pharmacological_comparison" and p.get("inv_id") == inv_id):
        known_d = set(pkg["dec"])
        for k, r in pkg["cmp"].items():
            meas = [m for m in pkg["meas"].values() if k in _blocked_keys(m["blocks_which_comparison_row"], pkg["cmp"])]
            cited, miss = _tokens(" ".join(v for v in r.values()), known_d | set(pkg["meas"]))
            d_hit = [t for t in cited if t in known_d]
            d_miss = [t for t in miss if re.fullmatch(r"D\d{2}", t)]
            out.append({"key": k, "package": pkg["dir"].parent.name, "kind": "pharmacological_comparison", "gene_arc": False,
                        "row": r, "new_measurements": meas, "decisive_cited": [pkg["dec"][t] for t in d_hit],
                        "broken_decisive_refs": d_miss,
                        "qualifier_cells": {c: r[c] for c in r if c.startswith("compound_or_probe") or c.endswith("_limits") or c.startswith("conditions") or c.startswith("outcome_")},
                        "source_refs": {f"cmp:{k}": pkg["refs"][f"cmp:{k}"], **{f"meas:{m['meas_id']}": pkg["refs"][f"meas:{m['meas_id']}"] for m in meas},
                                        **{f"dec:{t}": pkg["refs"][f"dec:{t}"] for t in d_hit}}})
    return {"inv_id": inv_id, "state": "COMPARISON_PRESENT" if out else "NO_COMPARISON_LISTED", "rows": out}


def _brief(rec: dict) -> str:
    L = [f"{rec['inv_id']}: {rec['state']}"]
    if rec["state"] == "UNLINKED":
        L.append("  no package states a hypothesis for this investigation; that is not evidence against it or its compounds")
    for h in rec["hypotheses"]:
        L.append(f"  {h['hyp_id']} [{h['package']}] kind={h['kind']} gene_arc={h['gene_arc']} need={h['need_id']} state={h['link_state']} cards={','.join(h['card_ids']) or '-'}")
        L.append(f"    status: {h['hypothesis']['status'][:140]}")
        L.append(f"    rivals (alternatives): {', '.join(a['alt_id'] for a in h['alternatives']) or '-'}   via matrix column: {', '.join(a['alt_id'] for a in h['alternatives_via_matrix_column']) or '-'}   other hypotheses: {', '.join(h['other_hypotheses_cited']) or '-'}   matrix columns: {', '.join(h['matrix_columns_cited'].values()) or '-'}")
        by = {}
        for t, c in h["ref_classes"].items():
            by.setdefault(c, []).append(t)
        L.append("    unresolved refs by class: " + ("; ".join(f"{c}: {','.join(v)}" for c, v in sorted(by.items())) or "-"))
        for e in h["experiments"]:
            L.append(f"    {e['row']['exp_id']} arms={','.join(a['arm_id'] for a in e['arms']) or '-'} alts={','.join(e['alternatives']) or '-'} expected_results={len(e['expected_results'])}")
        if not h["experiments"]:
            L.append("    NO_EXPERIMENT (not stated here)")
    return "\n".join(L)


def _brief_cmp(rec: dict) -> str:
    L = [f"{rec['inv_id']} pharmacological comparison: {rec['state']}"]
    for r in rec["rows"]:
        L.append(f"  {r['key']} [{r['package']}] measurements={','.join(m['meas_id'] for m in r['new_measurements']) or '-'} decisive={','.join(d['prop_id'] for d in r['decisive_cited']) or '-'} broken={','.join(r['broken_decisive_refs']) or '-'} ref={r['source_refs']['cmp:' + r['key']]}")
    return "\n".join(L)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("show", help="print the consumer records for one investigation (hypotheses and comparison, apart)")
    s.add_argument("--inv", required=True)
    s.add_argument("--json", action="store_true")
    sub.add_parser("check", help="validate the manifest and every package's links against the real ids")
    a = ap.parse_args(argv)
    errs = validate_manifest()
    pkgs = load_all() if not errs else []
    if a.cmd == "check":
        errs += [e for p in pkgs for e in validate(p)]
        broken = []
        for p in (p for p in pkgs if p["role"] == "physiological_hypotheses"):
            for inv in {l["inv_id"] for l in p["links"]}:
                for h in record_for([p], inv)["hypotheses"]:
                    broken += [f"{h['package']} {h['hyp_id']}: BROKEN_REFERENCE {t}" for t, c in h["ref_classes"].items() if c == "BROKEN_REFERENCE"]
        for inv in {p["inv_id"] for p in pkgs if p["role"] == "pharmacological_comparison"}:
            for r in comparison_for(pkgs, inv)["rows"]:
                broken += [f"{r['package']} {r['key']}: BROKEN_REFERENCE {t}" for t in r["broken_decisive_refs"]]
        n = sum(len(p.get("links", [])) + len(p.get("cmp", {})) for p in pkgs)
        print("\n".join(errs + [f"WARN {b}" for b in broken]) if errs or broken else f"OK: {n} rows over {len(pkgs)} manifest packages")
        for d in unlisted_packages():
            print(f"INFO not in manifest, not read: {d}")
        return 1 if errs else 0
    rec, cmp_ = record_for(pkgs, a.inv), comparison_for(pkgs, a.inv)
    print(json.dumps({"hypotheses": rec, "comparison": cmp_}, indent=1, ensure_ascii=False) if a.json else _brief(rec) + "\n" + _brief_cmp(cmp_))
    return 0


if __name__ == "__main__":
    sys.exit(main())
