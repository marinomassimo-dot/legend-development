#!/usr/bin/env python3
"""ADV-089 step 2 (IT, 2026-11-19): the reader's classification of every MISS_ALL_HELD item of scan_items_it_20261119.tsv.
Each category was assigned by reading the item's sentence in the claim record (context column), not by a rule; the script only
checks that every such item has one and writes scan_adjudication_it_20261119.tsv. Fails (exit 1) when an item has none, so a
rerun that produces a new miss cannot pass unread.   Usage: python3 adjudicate_it_20261119.py | --help"""
import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0)
OWN = "REGISTRY_OWN_WORDS"            # a label, an earlier wording of this record, a rejected wording, or a Title quoted in a note
DOC = "OTHER_DOCUMENT_QUOTE"          # quoted from a repository audit or manifest, not from the paper
ABS = "SEARCH_TERM_ASSERTED_ABSENT"   # the record says the string is NOT in the paper; a miss is the expected result
FIG = "FIGURE_READ_BY_EYE_OR_PIXELS"  # the record itself labels the value as read from a figure
DER = "DERIVED_COUNT_OR_ARITHMETIC"
LOC = "LOCATOR_OR_ID_NUMBER"          # a section number, queue pointer or similar, not a finding
M = {
    ("CLAIM 002", "GABA depolarizzante / firma GABAergica immatura"): (OWN, "Italian label of an IPOTESI"),
    ("CLAIM 002", "2.267"): (DER, "row count of a deposited table ('zero rows of 2,267'), not a cell value"),
    ("CLAIM 002", "untested"): (OWN, "the record's own first wording, quoted in the correction note"),
    ("CLAIM 002", "This is a source-availability outcome, not a judgement on the triples."): (DOC, "quoted from the locator audit"),
    ("CLAIM 002", "Rescues organoid phenotype"): (OWN, "the claim's own Title"),
    ("CLAIM 046", "a homology argument rather than a validation"): (OWN, "a wording the record calls false"),
    ("CLAIM 046", "standard curve"): (ABS, "the record states no panel carries it"),
    ("CLAIM 046", "limit of detection"): (ABS, "same"),
    ("CLAIM 046", "calibrat"): (ABS, "same"),
    ("CLAIM 046", "about elevenfold overexpression"): (OWN, "a bare wording the record warns would overstate"),
    ("CLAIM 003", "journal page 3071 (PDF page 11)"): (DOC, "a manifest locator string"),
    ("CLAIM 004", "artifact bytes absent from this checkout, attestation carried forward, re-acquisition owed"): (DOC, "an earlier annotation string of the record"),
    ("CLAIM 003", "sits on journal page 3072 (not 3071, as this batch's own first draft had it)"): (DOC, "a manifest locator string"),
    ("CLAIM 004", "2.1"): (LOC, "section number of a repository note"),
    ("CLAIM 025", "rapporto più basso = peggio"): (OWN, "a form of inference the record says is not authorised"),
    ("CLAIM 025", "a Drosophila model shows a WWOX metabolic effect that is HIF1α-INDEPENDENT (via ATF4/UPR; neuroprotection via methionine suppression, not lactate)"): (OWN, "the record's own earlier wording kept per prompt_batch_commit 7.2"),
    ("CLAIM 025", "via ATF4/UPR"): (OWN, "fragment of that earlier wording"),
    ("CLAIM 025", "neuroprotection via methionine suppression, not lactate"): (OWN, "fragment of that earlier wording"),
    ("CLAIM 025", "009"): (LOC, "queue pointer FT-009"),
    ("CLAIM 040", "nessun effetto"): (OWN, "Italian reading the record warns against"),
    ("CLAIM 040", "p > 0.05 significa nessun effetto"): (OWN, "a premise tag, Italian"),
    ("CLAIM 040", "crisi"): (OWN, "Italian word under discussion"),
    ("CLAIM 040", "5,2"): (DER, "binomial coefficient C(5,2) in the exact-test arithmetic"),
    ("CLAIM 040", "2.2"): (LOC, "section number of a repository note"),
    ("CLAIM 040", "4.1"): (LOC, "section number of a repository note"),
    ("CLAIM 006", "not progressive"): (OWN, "wording of backlog candidates, quoted to reject"),
    ("CLAIM 014", "the knockdown and the comparability of the arms are not demonstrated there"): (OWN, "the record's earlier wording in a 'corrected from' note"),
    ("CLAIM 015", "developmentally pre-wired"): (OWN, "a wording the record says must not be read as demonstrated"),
    ("CLAIM 015", "prenatally demonstrated"): (OWN, "same"),
}
PIX = {"CLAIM 046": {"0.11", "0.25", "2.3", "0.58", "0.21", "0.30", "18.7"},
       "CLAIM 004": {"0.8", "0.95", "105", "68", "77", "135", "87"}}
rows = list(csv.DictReader((HERE / "scan_items_it_20261119.tsv").open(encoding="utf-8"), delimiter="\t"))
out, miss = {}, []
for r in rows:
    if r["class"] != "MISS_ALL_HELD" or r["informative"] != "yes":
        continue
    k = (r["claim"], r["item"])
    if r["kind"] == "number" and r["item"] in PIX.get(r["claim"], set()):
        out[(r["claim"], r["kind"], r["item"])] = (FIG, "the record labels it read from a figure (pixels or by eye, with '~')", r["scope"])
    elif k in M:
        out[(r["claim"], r["kind"], r["item"])] = (*M[k], r["scope"])
    else:
        miss.append(k)
if miss:
    print("UNADJUDICATED:", sorted(set(miss)))
    raise SystemExit(1)
with (HERE / "scan_adjudication_it_20261119.tsv").open("w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["claim", "kind", "item", "scope", "category", "reason"])
    for (c, kd, it), (cat, why, sc) in sorted(out.items()):
        w.writerow([c, kd, it, sc, cat, why])
import collections
print(len(out), dict(collections.Counter(v[0] for v in out.values())))
