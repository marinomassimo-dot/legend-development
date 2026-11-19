#!/usr/bin/env python3
"""List corpus-seed PMIDs with no receipt at all, flag neural or mechanism titles and held files.

ADV-086 (SCI, 2026-11-19). Read-only. Joins the corpus seed list against the receipt ledger and the
staged receipts, and against the shared full-text folder. A title is not a reading: the output is a
census for a human or delegate to rank, never a verdict.

Usage: python3 -I list_unread_corpus.py REPO_ROOT FULLTEXT_DIR OUT_TSV
"""
import csv
import json
import re
import sys
from pathlib import Path

NEURAL = re.compile(
    r"neur|brain|cortic|hippocamp|cerebell|seiz|epilep|encephalopath|myelin|oligodendro|astro|glia|"
    r"synap|axon|dendrit|interneuron|GABA|NMDA|glutamat|ataxia|microcephal|intellectual|autis|"
    r"developmental|infant|child|patient|case|mutation|variant|mouse|mice|rat |knock|null|deficien|"
    r"calcium|channel|mitochond|metabol|glucose|insulin|lipid|autophag|chaperon|ubiquitin|proteasom|"
    r"ERBB4|ErbB4|WW domain|PPxY|PPXY|binding|interact|splic|isoform|rescue|therap|gene therapy|"
    r"oxidative|stress|retina|spinal|motor|cognit|behavio|Parkinson|Alzheimer|amyloid|tau",
    re.I,
)
CANCER = re.compile(
    r"carcinoma|cancer|tumou?r|leukemia|lymphoma|melanoma|glioma|neoplas|metasta|oncogen|malignan|"
    r"methylation|polymorphism|prognos|chemotherap|cell line|apoptosis",
    re.I,
)


def receipt_pmids(root: Path):
    seen = set()
    ledger = root / "disease-models/wwox/registries/fulltext_read_receipts.jsonl"
    for line in ledger.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        ev = json.loads(line)
        pm = str((ev.get("study_id") or {}).get("pmid") or "")
        if pm:
            seen.add(pm)
    for p in (root / "disease-models/wwox/research/receipt_staging").rglob("*.json"):
        try:
            ev = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if isinstance(ev, dict):
            pm = str((ev.get("study_id") or {}).get("pmid") or "")
            if pm:
                seen.add(pm)
    return seen


def held_files(ft_dir: Path):
    held = {}
    for p in ft_dir.iterdir():
        m = re.search(r"PMID(\d+)", p.name) or re.match(r"(\d{6,9})[_.]", p.name)
        if m:
            held.setdefault(m.group(1), []).append(p.name)
    return held


def main(argv):
    if len(argv) != 4 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0 if len(argv) > 1 and argv[1] in ("-h", "--help") else 2
    root, ft_dir, out = Path(argv[1]), Path(argv[2]), Path(argv[3])
    seen = receipt_pmids(root)
    held = held_files(ft_dir)
    seed = root / "disease-models/wwox/registries/corpus_seed_pubmed_20260806.tsv"
    rows = list(csv.DictReader(seed.open(encoding="utf-8"), delimiter="\t"))
    out_rows = []
    for r in rows:
        pm = r["pmid"]
        has = pm in seen
        t = r["title"]
        out_rows.append(
            {
                "pmid": pm,
                "year": r["year"],
                "free_ft": r["pubmed_free_full_text_link"],
                "pmcid": r["pmcid"],
                "receipt": "yes" if has else "no",
                "held_file": ";".join(held.get(pm, [])),
                "neural_term": "1" if NEURAL.search(t) else "0",
                "cancer_term": "1" if CANCER.search(t) else "0",
                "title": t,
            }
        )
    with out.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out_rows[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out_rows)
    nr = [x for x in out_rows if x["receipt"] == "no"]
    print(f"seed {len(rows)}; with receipt {len(rows) - len(nr)}; no receipt {len(nr)}")
    print(f"no receipt and held file: {sum(1 for x in nr if x['held_file'])}")
    print(f"no receipt, free full text flag yes: {sum(1 for x in nr if x['free_ft'] == 'yes')}")
    print(f"no receipt, neural term and no cancer term: {sum(1 for x in nr if x['neural_term']=='1' and x['cancer_term']=='0')}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
