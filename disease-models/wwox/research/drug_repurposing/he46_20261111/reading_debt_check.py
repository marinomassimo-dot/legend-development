#!/usr/bin/env python3
"""HE46 H5: what a reading that has no receipt still leaves behind, checked mechanically.

For each paper: the sha256 of the source bytes the reader worked from, the receipts that name the paper (ledger and staged) and the share of the quoted
sentences of the reader's report that occur verbatim in those bytes. It writes nothing to the ledger and decides nothing: whether a receipt may be recorded
(and of which kind) is the Orchestrator's act; a quotation found in the bytes shows the reader had the text, not that the whole text was read.

    python3 reading_debt_check.py --verdicts ../generation_it45_20261111/verify_s10/VERDICTS.md \
        --paper 38116420=pmc.html --paper 31411465=hal.html --paper 21964340=nat.xml --source-dir <folder holding the bytes>
"""
import argparse, glob, hashlib, html, json, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]


def norm(t: str) -> str:
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def section(text: str, pmid: str) -> str:
    parts = re.split(r"(?m)^#{2,3} ", text)
    return "\n".join(p for p in parts if p.startswith(pmid) or re.match(rf"[A-Za-z0-9. ]*{pmid}", p[:40]))


def receipts_naming(pmid: str):
    n_ledger = sum(1 for l in open(REPO / "disease-models/wwox/registries/fulltext_read_receipts.jsonl", encoding="utf-8") if f'"pmid": "{pmid}"' in l)
    staged = [p for p in glob.glob(str(REPO / "disease-models/wwox/research/**/receipts/FTR-*.json"), recursive=True) if f"-{pmid}-" in p]
    return n_ledger, len(staged)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--verdicts", required=True)
    ap.add_argument("--paper", action="append", required=True, help="PMID=file name inside --source-dir")
    ap.add_argument("--source-dir", required=True)
    a = ap.parse_args()
    report = Path(a.verdicts).read_text(encoding="utf-8")
    print("pmid\tsource_file\tsha256\tbytes\tledger_receipts\tstaged_receipts\tquoted_sentences\tfound_verbatim")
    for item in a.paper:
        pmid, name = item.split("=", 1)
        raw = (Path(a.source_dir) / name).read_bytes()
        hay = norm(raw.decode("utf-8", "ignore"))
        sec = section(report, pmid)
        quotes = []
        for line in sec.splitlines():          # quotation marks pair up inside one line only (1-2, 3-4, ...); a span that crosses a table cell is not a quotation
            marks = [m.start() for m in re.finditer('"', line)]
            for i in range(0, len(marks) - 1, 2):
                q = line[marks[i] + 1:marks[i + 1]]
                if len(q) >= 40 and "|" not in q:
                    quotes.append(q)
        found = sum(1 for q in quotes if norm(q) and norm(q) in hay)
        led, stg = receipts_naming(pmid)
        print("\t".join(map(str, (pmid, name, hashlib.sha256(raw).hexdigest(), len(raw), led, stg, len(quotes), found))))


if __name__ == "__main__":
    sys.exit(main())
