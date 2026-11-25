"""ADV-228 selection of six PMC-open catalogued-only records. Print-only; implements PREREG_ADV228_SCI_20261124.md section 2.
Reads: IT's candidate list (48 entries), the repository via `git grep` (run from the disease-models/wwox folder of a checkout).
Usage: python3 -I select_six_adv228.py <oa_candidates.json>   (cwd = <checkout>/disease-models/wwox)
"""
import sys

if len(sys.argv) != 2:
    print(__doc__)
    raise SystemExit(0)
import json, subprocess

EXCL_PMIDS = {"25051421", "33691672", "31123603", "42991897", "37804316", "30029003", "32652616", "25738457", "23611579",
              "41858901", "42190665", "42395553"}
EXCL_RECORDS = {"PAPER 495", "PAPER 157", "PAPER 447"}
A_NAMES = ("working_model_current.md", "working_model_history.md", "disease_model.md")
BAD = ("corpus_seed", "fulltext_read_receipts", "paper_registry_current", "batch_queue", "literature_tracking", "/view/", "coverage_report",
       "reading_state", "ranking", "unit_inputs", "deepdive_manifests", "/PMID", "census.tsv", "corpus_unread", "reading_debt",
       "selection_table", "pmid_list", "extract_ecKG", "counts.tsv", "result_adv164", "cards.json", "evidence.json", "generation_it59",
       "queries.json", "ops.json", "producer.json", "verifier.json", "history_units.json", "full_text_queue", "UNREAD_CORPUS_RANKING")

def files(pmid):
    r = subprocess.run(["git", "grep", "-l", "-w", "-e", pmid, "--", "."], capture_output=True, text=True)
    return {x for x in r.stdout.split("\n") if x and not any(b in x for b in BAD)}

rows = []
for pmid, rid, title, meta in json.load(open(sys.argv[1])):
    if pmid in EXCL_PMIDS or rid in EXCL_RECORDS:
        continue
    fs = files(pmid)
    a = sorted(f for f in fs if f.endswith(A_NAMES) or f.split("/")[-1].startswith("CC-"))
    b = sorted(f for f in fs if f not in a)
    score = (3 if a else 0) + (2 if b else 0) + (1 if len(a) + len(b) >= 2 else 0)
    n = int("".join(ch for ch in rid.split("-")[-1] if ch.isdigit()) or 0)
    rows.append((-score, n, pmid, rid, len(a), len(b), title[:80]))
rows.sort()
print("rank\tscore\tpmid\trecord\tclaim_files\tnote_files\ttitle")
for i, (s, n, pmid, rid, na, nb, t) in enumerate(rows[:14], 1):
    print("%d\t%d\t%s\t%s\t%d\t%d\t%s" % (i, -s, pmid, rid, na, nb, t))
