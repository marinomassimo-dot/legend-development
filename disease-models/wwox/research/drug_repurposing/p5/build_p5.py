#!/usr/bin/env python3
"""Build the P5 visible-dimension cells from the stored cards. Writes cells.json and the two
tables (tables_deep.md, tables_early.md). Every cell is a contiguous piece of the card's own field
(or the literal string UNKNOWN when the card has no such field). No score, rank or index is computed.
Run from anywhere: python3 build_p5.py"""
import json, glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DRUG = os.path.join(HERE, "..")
CUT = " [cut: the card's field continues]"


def sentence_prefix(text, limit=260):
    t = text.strip()
    if len(t) <= limit:
        return t, False
    # first sentence boundary inside the limit, else a word boundary
    m = [x.end() for x in re.finditer(r"[.;] ", t[:limit])]
    if m:
        return t[: m[-1]].rstrip(), True
    cut = t[:limit].rsplit(" ", 1)[0]
    return cut, True


def get(d, path):
    cur = d
    for k in path.split("."):
        if isinstance(cur, dict) and k in cur:
            cur = cur[k]
        else:
            return None
    return cur


def cell(card, path, pick=None):
    """Return a cell dict. pick: a contiguous substring to show (must occur in the field)."""
    v = get(card, path)
    if v is None:
        return {"value": "UNKNOWN", "card_field": None, "note": "the card has no such field"}
    if isinstance(v, list):
        v = " | ".join(str(x) for x in v)
    v = str(v)
    if pick is not None:
        assert pick in v, (path, pick)
        shown, cut = pick, len(pick) < len(v)
    else:
        shown, cut = sentence_prefix(v)
    return {"value": shown, "card_field": "input." + path, "cut": cut}


DEEP = [  # id, file, label, kind, risk override
    ("P4-A-01", "A01_pba_class", "4-phenylbutyrate class and bile-acid chemical chaperones", "candidate"),
    ("P4-A-02", "A02_proteasome_inhibitor_class", "proteasome-inhibitor class", "candidate"),
    ("P4-B-01", "B01_amlexanox", "amlexanox (PTC alleles only)", "candidate"),
    ("P4-C-01", "C01_aav9_wwox", "AAV9-delivered human WWOX", "candidate"),
    ("P4-D-01", "D01_a51", "A51, multi-kinase inhibitor", "candidate"),
    ("P4-A-03", "A03_client_binding_chaperone", "client-binding pharmacological chaperone", "abstention"),
    ("P4-A-04", "A04_er_proteostasis_regulators", "ER-proteostasis regulators", "abstention"),
    ("P4-A-05", "A05_hsp70_axis", "HSP70-axis modulation", "abstention"),
    ("P4-B-02", "B02_readthrough_class", "PTC read-through class", "abstention"),
    ("P4-C-02", "C02_splice_aso", "splice-correcting ASO / editing", "abstention"),
    ("P4-C-03", "C03_crispra_boost", "endogenous boost (CRISPRa or equivalent)", "abstention"),
    ("P4-D-02", "D02_wnt_tankyrase", "Wnt-lowering agents and GSK3 modulation", "abstention"),
]
EARLY = [
    ("EB-KD-01", "ketogenic diet", "candidate"),
    ("EB-VGB-01", "vigabatrin", "candidate"),
    ("EB-ETX-01", "ethosuximide (T-type contrast)", "candidate"),
    ("EB-GROWTH-AX-01", "growth (endpoint axis, not an intervention)", "abstention"),
    ("EB-DEV-AX-01", "development / disease modification (axis)", "abstention"),
    ("EB-PDANCHOR-AX-01", "pharmacodynamic anchor (axis)", "abstention"),
    ("EB-HORM-AX-01", "ACTH, corticosteroids, phenobarbital regimens", "abstention"),
    ("EB-CBD-AX-01", "cannabidiol", "abstention"),
    ("EB-MTOR-AX-01", "mTOR-inhibitor class", "abstention"),
]

# hand-picked contiguous pieces where the automatic prefix would cut the wrong part
PICK_DEEP = {
    ("P4-A-02", "risk"): ("p4_card.pharmacology", None),
    ("P4-C-01", "risk"): ("p4_card.evidence_for_and_against.against", "No tumour surveillance of any kind in a pro-apoptotic tumour suppressor delivered irreversibly; no measured ceiling."),
    ("P4-D-01", "risk"): ("p4_card.evidence_for_and_against.against", "one grade 3 hepatic failure with encephalopathy at the highest tested level, a level the study then discontinued for potential serious liver injury although its maximum-tolerated-dose criteria were not met."),
    ("P4-D-01", "block1"): ("p4_card.status_reason", None),
    ("P4-A-01", "risk"): ("p4_card.pharmacology", None),
    ("P4-B-01", "risk"): ("p4_card.evidence_for_and_against.against", "The entire safety argument in the originating paper is historic use for other indications; no paediatric, CNS or pharmacokinetic datum."),
    ("P4-C-01", "access"): ("p4_card.time_to_access", None),
    ("P4-C-01", "benefit_time"): ("p4_card.time_to_benefit", None),
}


def deep_rows():
    rows = []
    for pid, f, label, kind in DEEP:
        c = json.load(open(os.path.join(DRUG, "cards", f + ".card.json")))
        inp = c["input"]
        row = {"id": pid, "candidate": label, "kind": kind, "card_file": f"cards/{f}.card.json",
               "bridge_directional_summary": c["directional_summary"], "dims": {}}
        D = row["dims"]
        # BENEFIT: the one endpoint, and whether symptomatic or modifying (the card's expected_contribution)
        D["benefit_endpoint"] = cell(c, "input.p4_fields.endpoint_pursued") if False else cell(inp, "p4_fields.endpoint_pursued")
        D["benefit_type"] = cell(inp, "p4_card.expected_contribution")
        # EVIDENCE
        D["evidence_state"] = cell(inp, "p4_card.state_of_known_roads")
        D["evidence_functional"] = cell(inp, "p4_fields.functional_evidence_available")
        # RISK (class-level observations only) and BLOCK-1
        rp, rpick = PICK_DEEP.get((pid, "risk"), ("p4_card.pharmacology", None))
        D["risk"] = cell(inp, rp, rpick)
        bp, bpick = PICK_DEEP.get((pid, "block1"), (None, None))
        if bp:
            D["block1"] = cell(inp, bp, bpick)
        else:
            D["block1"] = {"value": "UNKNOWN", "card_field": None,
                           "note": "no BLOCK-1 field or statement on this card; UNKNOWN is not a pass"}
        # TIME (separate)
        ap, apick = PICK_DEEP.get((pid, "access"), ("p4_card.time_to_access", None))
        tp, tpick = PICK_DEEP.get((pid, "benefit_time"), ("p4_card.time_to_benefit", None))
        D["time_to_access"] = cell(inp, ap, apick)
        D["time_to_benefit"] = cell(inp, tp, tpick)
        # FEASIBILITY: what has to exist for it to be tested
        D["feasibility"] = cell(inp, "p4_card.next_measurement")
        if kind == "abstention":
            D["missing_datum"] = cell(inp, "abstention_card.missing_datum")
        if pid == "P4-D-01":
            # The card now carries the audited reading of the cited pharmacokinetic table (card rewritten 2026-10-22,
            # R4c; sourced to manifest 40665325 entries 6, 12 and 21), so this is an ordinary verbatim cell.
            D["exposure_proportionality"] = cell(inp, "p4_card.evidence_for_and_against.against",
                "The paper states plasma exposure was dose-proportional between its lowest and highest levels; its printed table, with N per cohort 1, 1, 3, 3, 3, 8, 5 across seven levels and printed CVs of 4.1 to 79 percent (only for cohorts of three or more), gives day 5 exposure (AUC) roughly proportional to dose from the second to the sixth cohort (log-log slope about 0.95 by the two end points, about 0.98 over the five points, a span that still begins at a cohort of one), supralinear only when the lowest cohort, a single patient, is included (slope about 1.38), and 1.27-fold higher at the top cohort than at the one below for a 2.0-fold dose ratio; the day 1 exposure cell of the top cohort is blank.")
        rows.append(row)
    return rows


def early_rows():
    rows = []
    for pid, label, kind in EARLY:
        c = json.load(open(os.path.join(DRUG, "cards_early", pid + ".card.json")))
        inp = c["input"]
        R = "p4_roadmap_fields."
        row = {"id": pid, "candidate": label, "kind": kind, "card_file": f"cards_early/{pid}.card.json",
               "bridge_directional_summary": c["directional_summary"], "dims": {}}
        D = row["dims"]
        D["benefit_endpoint"] = cell(inp, "p4_fields.endpoint_pursued")
        D["benefit_type"] = cell(inp, R + "expected_contribution")
        D["evidence_state"] = cell(inp, R + "known_roads_state")
        D["evidence_functional"] = cell(inp, "p4_fields.functional_evidence_available")
        D["risk"] = cell(inp, R + "paediatrics_and_interactions")
        D["block1"] = {"value": "UNKNOWN", "card_field": None,
                       "note": "no BLOCK-1 field or statement on this card; UNKNOWN is not a pass"}
        D["time_to_access"] = cell(inp, R + "time_to_access", None)
        D["time_to_benefit"] = cell(inp, R + "time_to_benefit")
        D["feasibility"] = cell(inp, R + "next_measure")
        if kind == "abstention":
            D["status_missing_datum"] = cell(inp, R + "status")
        rows.append(row)
    return rows


COLS = [("benefit_endpoint", "Benefit: the ONE endpoint"), ("benefit_type", "Benefit: symptomatic or modifying (card's expected contribution)"),
        ("evidence_state", "Evidence: state"), ("evidence_functional", "Evidence: functional evidence available"),
        ("risk", "Risk (class-level, as the card carries it)"), ("block1", "BLOCK-1 status"),
        ("time_to_access", "Time to ACCESS"), ("time_to_benefit", "Time to BENEFIT"), ("feasibility", "Feasibility: what must exist to test it")]


def esc(s):
    return s.replace("|", "\\|").replace("\n", " ")


def render(rows, title):
    out = [f"## {title}", ""]
    for r in rows:
        out.append(f"### {r['id']} · {r['candidate']} · {r['kind'].upper()} · bridge `directional_summary` = {r['bridge_directional_summary']}")
        out.append("")
        out.append("| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |")
        out.append("|---|---|---|")
        for key, name in COLS:
            c = r["dims"][key]
            v = esc(c["value"]) + (CUT if c.get("cut") else "")
            f = c["card_field"] or "(none)"
            if c["value"] == "UNKNOWN":
                v = "**UNKNOWN**" + (f" ({c['note']})" if c.get("note") else "")
            out.append(f"| {name} | {v} | `{f}` |")
        if "exposure_proportionality" in r["dims"]:
            c = r["dims"]["exposure_proportionality"]
            out.append(f"| Exposure versus dose in the cited adult study (class-level fact of a cited study, NOT WWOX EVIDENCE) | {esc(c['value'])}{CUT if c.get('cut') else ''} | `{c['card_field']}` |")
        for extra in ("missing_datum", "status_missing_datum"):
            if extra in r["dims"]:
                c = r["dims"][extra]
                out.append(f"| ABSTENTION: the missing datum | {esc(c['value'])}{CUT if c.get('cut') else ''} | `{c['card_field']}` |")
        out.append("")
    return "\n".join(out)


def main():
    deep, early = deep_rows(), early_rows()
    json.dump({"schema": "p5-cells-1", "note": "cells are verbatim pieces of the stored cards or UNKNOWN; no score, rank, probability or index exists in this file",
               "RECUPERO_PROFONDO": deep, "BENEFICIO_PRECOCE": early},
              open(os.path.join(HERE, "cells.json"), "w"), indent=1, ensure_ascii=False)
    open(os.path.join(HERE, "tables_deep.md"), "w").write(
        "# P5 · RECUPERO_PROFONDO: one block per row, in card-axis order (the order is NOT a preference)\n\n"
        "Candidates first (5), then abstentions (7); within each group the order is the cards' axis order.\n\n"
        + render(deep, "Rows") + "\n")
    open(os.path.join(HERE, "tables_early.md"), "w").write(
        "# P5 · BENEFICIO_PRECOCE: one block per row, in card order (the order is NOT a preference)\n\n"
        "Candidates first (3), then abstentions (6).\n\n" + render(early, "Rows") + "\n")
    keys = ["benefit_endpoint", "benefit_type", "evidence_state", "evidence_functional", "risk", "block1", "time_to_access", "time_to_benefit", "feasibility"]
    names = ["endpoint", "b.type", "ev.state", "ev.func", "risk", "BLOCK-1", "t.access", "t.benefit", "feasib."]
    def sym(c):
        v = c["value"].strip().lower()
        if v.startswith("unknown"):
            return "U"
        if v.startswith("not applicable"):
            return "n/a"
        return "V"
    out = ["# Where each row carries a value (V), is UNKNOWN-led (U) or not applicable (n/a)", "",
           "V says only that the card's cell holds content. V is NOT favourable and U is NOT unfavourable; a V can be a harm, a negative or a limit. "
           "Derived mechanically from cells.json by build_p5.py (first word of the cell). Two limits of that mechanism: (1) a U-led cell can carry content after its UNKNOWN (for example the ethosuximide risk cell names a class-level in-vitro signal); (2) for the deep abstentions the `ev.state` V is a pointer to a repository note, not an evidence statement. The tables hold the text.", ""]
    for title, rows in (("RECUPERO_PROFONDO", deep), ("BENEFICIO_PRECOCE", early)):
        out += [f"## {title}", "", "| Row | kind | " + " | ".join(names) + " |", "|---|---|" + "---|" * len(names)]
        for r in rows:
            out.append(f"| {r['id']} | {r['kind']} | " + " | ".join(sym(r['dims'][k]) for k in keys) + " |")
        out.append("")
    open(os.path.join(HERE, "matrix.md"), "w").write("\n".join(out))
    print("rows:", len(deep), len(early))


if __name__ == "__main__":
    main()
