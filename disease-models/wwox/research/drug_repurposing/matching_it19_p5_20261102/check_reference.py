#!/usr/bin/env python3
"""IT19 P5 step 2 check: the reference table obeys the protocol written in SELECTION.md.

  check_reference.py --selection F --reference F [--json]

Checks (each has a regression test in test_check_reference.py):
  * one reference row per selected pair, same pair ids, same (need, compound) keys;
  * label is one of compatible / opposite / indeterminable / unknown;
  * a determinate label (compatible or opposite) carries a status that starts with `determinate`,
    a target at the measured resolution, a measure type and a source locator;
  * an `unknown` row carries no label other than unknown and states the bounded search;
  * dependency is declared on every row from the closed vocabulary;
  * no row claims a subunit-level direction while its measure is binding only.
Offline; --help and import do nothing else.
"""
import argparse
import collections
import csv
import json
import sys
from pathlib import Path

LABELS = {"compatible", "opposite", "indeterminable", "unknown"}
DEPS = {"independent_of_module_input", "shared_derivation_mechanism_citation", "partly_shared", "not_applicable"}
BINDING_ONLY = ("radioligand binding only", "radioligand binding (no direction")


def read_tsv(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def check(selection, reference):
    errs = []
    sel = {r["pair_id"]: r for r in selection}
    ref = {r["pair_id"]: r for r in reference}
    if set(sel) != set(ref):
        errs.append("pair ids differ: %s" % sorted(set(sel) ^ set(ref)))
    for pid, r in sorted(ref.items()):
        s = sel.get(pid)
        if s and (s["need_id"], s["parent_chembl_id"]) != (r["need_id"], r["parent_chembl_id"]):
            errs.append("%s: (need, compound) does not match the selection" % pid)
        if r["reference_label"] not in LABELS:
            errs.append("%s: label %r outside the vocabulary" % (pid, r["reference_label"]))
        if r["dependency_on_module_sources"].split(" ")[0] not in DEPS:
            errs.append("%s: dependency %r outside the vocabulary" % (pid, r["dependency_on_module_sources"]))
        det = r["reference_label"] in ("compatible", "opposite")
        if det:
            if not r["status"].startswith("determinate"):
                errs.append("%s: determinate label with status %r" % (pid, r["status"]))
            for f in ("target_at_measured_resolution", "measure_type", "source_locator", "action_and_context"):
                if not r[f].strip():
                    errs.append("%s: determinate label without %s" % (pid, f))
            if r["measure_type"].startswith(BINDING_ONLY):
                errs.append("%s: determinate direction from a binding-only measure" % pid)
        if r["reference_label"] == "unknown":
            if not r["status"].startswith("unknown"):
                errs.append("%s: unknown label with status %r" % (pid, r["status"]))
            if "no" not in r["resolution_note"]:
                errs.append("%s: unknown row does not state what is missing" % pid)
        if r["reference_label"] == "indeterminable" and not r["status"].startswith("indeterminable"):
            errs.append("%s: indeterminable label with status %r" % (pid, r["status"]))
    counts = collections.Counter(r["reference_label"] for r in reference)
    status = collections.Counter(r["status"] for r in reference)
    deps = collections.Counter(r["dependency_on_module_sources"].split(" ")[0] for r in reference)
    determinate = [r["pair_id"] for r in reference if r["reference_label"] in ("compatible", "opposite")]
    return errs, {"rows": len(reference), "labels": dict(counts), "status": dict(status), "dependency": dict(deps),
                  "determinate_pairs": determinate,
                  "determinate_functional": sorted(r["pair_id"] for r in reference if r["status"] == "determinate_functional"),
                  "usable_rows": len(determinate), "error_attribution": dict(collections.Counter(r["error_attribution"].split(":")[0] for r in reference))}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selection", required=True)
    ap.add_argument("--reference", required=True)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    errs, summary = check(read_tsv(a.selection), read_tsv(a.reference))
    print(json.dumps(summary, indent=1) if a.json else "\n".join("%s: %s" % kv for kv in summary.items()))
    for e in errs:
        print("DEFECT", e, file=sys.stderr)
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
