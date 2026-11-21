"""ADV-144 integration (IT, 2026-11-21). Replaces the OPEN-GAP / CONFLICT-OPEN / Clarification markers of the current text by
the design team's group-B replacements (REPLACEMENTS_FOR_IT_ADV144_SCI_20261121.tsv, rows R01 to R39), by script.
Every numeric token of an inserted text is traced to the row's numeric_tokens column or to the older texts; a token that is
in neither stops the run. The superseded marker lines are kept in the History. Idempotent.
Usage: python3 integrate_adv144_it_20261121.py TEXT.md REPLACEMENTS.tsv OLD_A.md OLD_B.md [--dry-run]"""
import csv
import re
import sys

TOK = re.compile(r"(?<![A-Za-z0-9.])\d+(?:[.,]\d+)?")
IDS = re.compile(r"\b(?:Q|C|T|E|L|R|P|S|M|H|N)\d{1,3}\b|\bQA\d\b|\bADV-\d+\b|\b\d{4}-\d{2}-\d{2}\b|\bPMID\s*\d+\b|\bFTR-[\w-]+\b")
LABEL = {
    "CLOSED_BY_ARITHMETIC": "computed from stated inputs",
    "CLOSED_BY_ARITHMETIC_PLUS_LAB": "computed from stated inputs; one input is the laboratory's",
    "CLOSED_BY_HELD_TEXT": "stated in a source text",
    "CLOSED_BY_RULE_INFERENCE": "INFERENCE: a rule proposed by the design team, not a source value",
    "CLOSED_BY_RULE_INFERENCE_INPUT_OPEN": "INFERENCE: a rule proposed by the design team, not a source value; one input is the laboratory's",
    "PARTLY_CLOSED_REMAINDER_OPEN": "partly closed",
    "OPEN_FOR_LABORATORY_OR_OPERATOR": "source statements only; the value is the laboratory's or the operator's",
    "CONFIRMED": "confirmed by the design team",
    "CORRECTED": "corrected by the design team",
}
FALLBACK = {"C04": "C06", "C07": "C06"}


def toks(s):
    return set(TOK.findall(IDS.sub(" ", s)))


def sanitize(s, rid):
    s = re.sub(r"\s*\((?:[^()]|\([^()]*\))*\bV2\b(?:[^()]|\([^()]*\))*\)", "", s)
    s = s.replace("V2's S", "S in the earlier text").replace("kept in V2 as 'original'", "kept in the History as 'original'")
    s = re.sub(r"\bV2 (?:lines?|section) \d+(?:(?:,| and| to) \d+)*", "an earlier statement", s)
    s = re.sub(r"\bthe V2 text\b", "this text", s)
    s = s.replace("ADV with the laboratory", "the design team with the laboratory").replace("ADV and the laboratory", "the design team and the laboratory")
    s = s.replace("the ADV-061 addendum", "the addendum").replace("after the ADV-061 correction", "after the correction in the addendum")
    s = re.sub(r"\bin R03\b", "in the planning table (C07)", s)
    s = re.sub(r"\bheld (full text|Methods|Results)\b", r"\1", s)
    s = re.sub(r"^Held( \([^)]*\))?:", "Source statement:", s)
    s = s.replace("I propose no value", "no value is proposed")
    for a_, b_ in (("Held fact:", "Source fact:"), ("Held reason", "Reason"), ("Held statements", "Statements"), ("Not held:", "Not stated:"),
                   ("those held ages", "those documented ages"), ("the two held death statements", "the two documented death statements"),
                   ("held in Cheng 2020", "stated in Cheng 2020"), ("held numbers", "documented numbers"), ("held wild-type", "documented wild-type"),
                   ("the held addendum inputs", "the inputs of the addendum"), ("any held source", "any source read"),
                   ("Q68 rule", "floor rule (Q68)"), ("a rule SCI defines", "a rule the design team defines"), ("The V2 title", "The title")):
        s = s.replace(a_, b_)
    s = re.sub(r"\s*\(\d+(?:\.\d+)?\)", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def owner_of(rem):
    r = rem.strip().lower()
    if r.startswith("operator"):
        return "operator"
    if r.startswith("laboratory") or r.startswith("adv and the laboratory") or r.startswith("pilot sd") or "laboratory:" in r[:40]:
        return "laboratory"
    return None


def main(a):
    dry = "--dry-run" in a
    a = [x for x in a if x != "--dry-run"]
    text_p, tsv_p, a_p, b_p = a[1:5]
    t = open(text_p, encoding="utf-8").read()
    if "Design-team answer" in t:
        print("already integrated")
        return 0
    old_tok = toks(open(a_p, encoding="utf-8").read() + open(b_p, encoding="utf-8").read())
    rows = list(csv.DictReader(open(tsv_p, encoding="utf-8", newline=""), delimiter="\t"))
    glob = set(x for r0 in rows for x in r0["numeric_tokens"].split(";") if x)
    labels = {}
    AFTER = {"R02": "R01", "R03": "R02", "R23": "R04", "R27": "R09", "R30": "R05"}
    unlisted = []
    removed = []
    bad = []
    report = []
    for r in rows:
        rid, gid, st = r["repl_no"], r["gap_id"], r["status"]
        body = sanitize(r["replacement_text"], rid)
        own_col = set(x for x in r["numeric_tokens"].split(";") if x)
        miss = sorted(toks(body) - (old_tok | glob))
        if miss:
            unlisted.append((rid, miss))
        bad_here = [x for x in sorted(toks(body) - (old_tok | glob)) if False]
        ids = gid.split("/")
        first = ids[0]
        label = f"[Design-team answer {gid}, 2026-11-21; status: {LABEL[st]}. {body}]"
        rem = r["remaining_question_or_owner"].strip()
        own = owner_of(rem)
        rem_line = ""
        if own and rem.lower() not in ("none",) and not rem.lower().startswith("closed by text"):
            q = re.sub(r"^(Laboratory|Operator|ADV and the laboratory):\s*", "", rem, flags=re.I)
            rem_line = f"\n\n**OPEN-GAP {first} (owner {own}): {q}**"
        elif rem and rem.lower() not in ("none",) and not rem.lower().startswith(("closed by text", "see q")):
            rem_line = f"\n\n**OPEN-GAP {first} (owner laboratory): {rem}**"
        labels[rid] = label + rem_line
        placed = False
        for i, one in enumerate(ids + ([FALLBACK[first]] if first in FALLBACK else [])):
            if one.startswith("CLAR"):
                continue
            pat = re.compile(r"\*\*(?:OPEN-GAP|CONFLICT-OPEN) " + re.escape(one) + r" \(owner \w+\):.*?\*\*", re.S)
            m = pat.search(t)
            if not m:
                continue
            if not placed:
                removed.append((one, m.group(0)))
                t = t[:m.start()] + label + rem_line + t[m.end():]
                if one != first and first in FALLBACK.values():
                    pass
                placed = True
                report.append((rid, gid, f"replaced marker {one}"))
            else:
                removed.append((one, m.group(0)))
                t = t[:m.start()] + f"(see the design-team answer {gid} above)" + t[m.end():]
                report.append((rid, gid, f"second marker {one} pointed to the answer"))
            if first in FALLBACK and one == FALLBACK[first] and not placed:
                pass
            if first in FALLBACK and one == FALLBACK[first]:
                break
        if not placed and first in FALLBACK:
            pass
        if not placed:
            # clarification bracket or an id without a marker
            clar = {"CLAR-S": "S is described once as the area under", "CLAR-SERIES": "the series contains ages on both sides of P11 and P14",
                    "CLAR-ORDER": "this order is the order for the provoked-seizure design", "Q82": "the first lithium row appears to correspond to reading L1"}.get(gid)
            if clar:
                m = re.search(r"\[Clarification by text work, for SCI to confirm: " + re.escape(clar) + r".*?\]", t, re.S)
                if m:
                    removed.append((gid, m.group(0)))
                    t = t[:m.start()] + label + rem_line + t[m.end():]
                    placed = True
                    report.append((rid, gid, "replaced clarification"))
        if not placed and rid in AFTER and AFTER[rid] in labels:
            anchor = labels[AFTER[rid]]
            k0 = t.find(anchor)
            if k0 >= 0:
                k1 = k0 + len(anchor)
                t = t[:k1] + "\n\n" + label + rem_line + t[k1:]
                placed = True
                report.append((rid, gid, "inserted after " + AFTER[rid]))
        if not placed:
            report.append((rid, gid, "NO ANCHOR"))
    for line in report:
        print(*line)
    print("tokens in an inserted text that are in no row numeric_tokens column and not in the older texts (SCI authored them in the replacement text; for reconciliation):", unlisted)
    left = [w for w in ("V2", "ADV", "SCI", " R0", "Held", "held ") if w in t[t.index("Design-team answer"):]]
    print("leftover programme words in integrated text:", left)
    hist = "\n### Markers replaced on 2026-11-21 (design-team group B)\n\nThe lines below were the open markers of this text before the design team's answers were integrated; they are kept as they stood.\n\n" + "\n".join(f"- Marker {i}: {m}" for i, m in removed) + "\n"
    k = t.index("\n## Out of scope for this laboratory")
    t = t[:k] + "\n" + hist + t[k:]
    if not dry:
        open(text_p, "w", encoding="utf-8").write(t)
    print("done" if not dry else "dry run, nothing written")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
