#!/usr/bin/env python3
"""ADV-281 STEP 0: list null-wording card assertion notes by two routes. Run from the repository root; writes a TSV next to itself."""
import glob, json, re, sys
from pathlib import Path

PHRASES = [
    r"\bno (change|effect|rescue|difference|increase|decrease|reduction|improvement|benefit|recovery|response|alteration|significant)",
    r"\bnot (significant|rescued|restored|changed|altered|reduced|increased|improved|affected|reversed|recovered|prevented|detected|different)",
    r"\bnon[- ]?significant",
    r"\bn\.s\.",
    r"\bun(changed|affected|altered)\b",
    r"\b(did|does|do|was|were) not\b",
    r"\bfail(ed|s)? to\b",
    r"\bdid nothing\b",
    r"\b(had|has|have|with) no\b",
    r"\bwithout (an? )?(effect|change|rescue)",
    r"\bnull\b",
    r"\bneither\b",
    r"\bindistinguishable\b",
    r"\bremain(ed|s) (low|high|unchanged|absent)",
]
RX = [re.compile(p, re.I) for p in PHRASES]
TEN = ["DR-A01-003", "DR-A01-004", "DR-A02-002", "DR-A02-009", "DR-E03-001", "DR-H01-001", "DR-H01-003", "DR-L01-001", "DR-M01-001", "DR-P11-006"]


def rows():
    for f in sorted(glob.glob("disease-models/wwox/research/drug_repurposing/cards/*.card.json")):
        inp = json.load(open(f))["input"]
        for key in ("drug_assertions", "disease_assertions", "disease_assertion"):
            v = inp.get(key)
            if v is None:
                continue
            for a in (v if isinstance(v, list) else [v]):
                yield Path(f).name.split("_")[0], key, a


def main():
    seen = {}
    for card, key, a in rows():
        text = " || ".join(x for x in (a.get("measured_result_note"), a.get("note")) if x)
        hits = []
        for rx in RX:
            m = rx.search(text)
            if m:
                hits.append(m.group(0))
        s = a.get("direction") == "NO_CHANGE"
        if a["id"] in seen:
            seen[a["id"]]["cards"].add(card)
            if (text, a.get("direction")) != (seen[a["id"]]["text"], seen[a["id"]]["direction"]):
                seen[a["id"]]["differs"] = True
            continue
        seen[a["id"]] = dict(cards={card}, key=key, s=s, hits=hits, text=text, direction=a.get("direction"),
                             source=a.get("source", ""), receipt=a.get("receipt") or a.get("receipt_reference") or "", differs=False)
    found = {i: r for i, r in seen.items() if r["s"] or r["hits"] or i in TEN}
    out = Path(__file__).with_name("route_hits_adv281.tsv")
    with out.open("w") as fh:
        fh.write("id\tcards\tfield\tdirection\troute_S\troute_T\tin_ten\tphrases\tsource\treceipt\trows_differ\tnote\n")
        for i in sorted(found):
            r = found[i]
            clean = lambda t: str(t).replace("\t", " ").replace("\n", " ")
            fh.write("\t".join([i, ",".join(sorted(r["cards"])), r["key"], str(r["direction"]), "Y" if r["s"] else "N", "Y" if r["hits"] else "N",
                                "Y" if i in TEN else "N", "|".join(r["hits"]), clean(r["source"]), clean(r["receipt"]), "Y" if r["differs"] else "N", clean(r["text"])]) + "\n")
    s = {i for i, r in seen.items() if r["s"]}
    t = {i for i, r in seen.items() if r["hits"]}
    print("distinct ids", len(seen), "S", len(s), "T", len(t), "both", len(s & t), "S only", len(s - t), "T only", len(t - s), "union", len(s | t))
    for i in TEN:
        print(i, "S" if i in s else "-", "T" if i in t else "-")


if __name__ == "__main__":
    sys.exit(main())
