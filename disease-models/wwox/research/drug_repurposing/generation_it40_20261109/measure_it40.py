#!/usr/bin/env python3
"""IT40 P7: the same cases under (a) the current generator path (S16 = S17), (b) a simple baseline (catalogue lookup by target symbol, free-text cells), (c) the new path (conditional proposals + mechanism-first search). Counts only; no score; no predictive claim."""
import csv, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
import conditional_proposals as cp
def tsv(p): return list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))
out = []
def row(case, metric, a, b, c, note=""): out.append([case, metric, a, b, c, note])
props = tsv(HERE / "results_s17/proposals_it21.tsv")
s16 = tsv(DR / "generation_it39_20261109/results_s16/proposals_it21.tsv")
inv = {r["inv_id"]: r for r in tsv(DR / "ranking_it8_p9_20261029/investigations_it20.tsv")}
ba = cp.by_action(); on = {r["proposal_id"]: r for r in cp.rows(True)}; off = {r["proposal_id"]: r for r in cp.rows(False)}
pat = re.compile(r"GRIN|GRIA|GRIK|HCN|KCNQ|GABR|SLC12A|GJD2|PANX")
touch = sum(1 for r in props if pat.search(r["main_target"] or ""))
# case 1 physiological hypothesis without a proven gene pair (MH1)
row("1 physiological hypothesis, no gene pair (membrane MH1)", "generator proposals whose main target is a receptor/channel of these hypotheses", f"{touch} of {len(props)}", f"{touch} of {len(props)}", "6 conditional records (3 membrane, 3 AMPA/NMDA)", "the gene-graph generator has no representation for them; unchanged by IT40")
row("1", "chars of the hypothesis chain, rivals, expected results reaching a consumer", "INV-18 next_test+decisive_uncertainty cells only", "same", f"MH1 record: chain {len(on['CP-MH1']['starting_observation_and_chain'])}, rivals {len(on['CP-MH1']['competing_explanations'])}, expected results {len(on['CP-MH1']['expected_result_by_explanation'])} chars, nomination {on['CP-MH1']['nomination']}", "")
# case 2 AMPA/NMDA competing explanations
nmat = len({(m.group(1), h) for k in ("CP-BH1", "CP-BH2", "CP-BH3") for m in re.finditer(r"(M\d\d): (.*?) \| arms do not", on[k]["expected_result_by_explanation"]) for h in re.findall(r"\b(H\d)=", m.group(2))})   # distinct (arm, explanation) pairs; an arm shared by several hypotheses counts once
row("2 AMPA/NMDA with competing explanations (BH1-3)", "expected-result cells (arm x explanation) a consumer can read", "0", "0 (INV-05 free text names d-APV and GluN2B NAM arms)", f"{nmat}", "ablation without the package link: 0 (conditional_proposals_nolink.tsv)")
row("2", "competing explanations reachable by id", "0", "names in free text", str(sum(on[k]["competing_explanations"].count("AB") for k in ("CP-BH1","CP-BH2","CP-BH3"))) + " alternative-id mentions + the hypothesis cell text", "BH1 rivals are reachable only through the matrix column map added in IT40")
# case 2b mechanism-first on GluN2B
r1 = [r for r in ba["R1"] if r["catalogue_id"]]
mol = lambda rs_: len({r["parent_molecule"] for r in rs_})
asm = [r for r in r1 if r["target_record_granularity"] == "two_gene_assembly_record"]
row("2b GluN2B-directed comparison", "molecules returned for the symbol GRIN2B", f"{mol(r1)} (simple lookup)", f"{mol(r1)}", f"{mol(r1)} listed; {mol(asm)} with a GluN1/GluN2B assembly record (max phase {max(float(r['max_phase']) for r in asm):g}); the rest with a family record, subunit unresolved", "granularity of the catalogue record, not selectivity")
up = [r for r in r1 if r["direction"] != "down"]
row("2b", "entries that RAISE receptor activity inside a request for antagonists", "not separated", "not separated", f"{mol(up)} molecules flagged by direction", "")
r3 = [r for r in ba["R3"] if r["catalogue_id"]]; r3d = [r for r in r3 if r["direction"] == "down"]
row("2c AMPA/kainate antagonism", "rows -> distinct molecules -> antagonists", f"{len(r3)} rows", f"{len(r3)} rows", f"{mol(r3)} molecules, {mol(r3d)} antagonists", "one record is repeated per gene symbol")
# case 3 premise already consumed
same = all(a[c] == b[c] for a, b in zip(s16, props) for c in a if c in b)
row("3 premise already consumed (HIF1A->HK2; ISRIB)", "columns changed in 994 proposals, S16 vs S17 regenerated with IT40 inputs", "-", "0", "0" if same else "CHANGED", "nothing is added where nothing is needed; hand-overs identical (15), eligible 220")
# case 4 abstention
r5 = [r for r in ba["R5"] if r["catalogue_id"]]; op = [r for r in r5 if r["direction"] == "up"]
row("4 abstention (Kv7 / resting K+ conductance)", "compounds offered", f"{mol(r5)} molecules on KCNQ2-5, {mol(op)} openers (simple lookup)", f"{mol(r5)}", f"0 nominated: {on['CP-MH1']['nomination']}; reason: a drug response would not show a leak deficit", "the knowledge that decides it: Rin up with flat tau (inference), recording without blockade, E_K arithmetic")
tools = tsv(DR / "mechsearch_it40_20261109/identity_check.tsv")
ok = sum(1 for t in tools if t["verdict"] == "TARGET_CONFIRMED")
row("5 identity of tools named by the packages", "tools with a catalogue record carrying the intended target", f"{sum(1 for t in tools if t['verdict'] != 'NOT_IN_CATALOGUE')} of {len(tools)} found by name", f"{sum(1 for t in tools if t['verdict'] != 'NOT_IN_CATALOGUE')}", f"{ok} confirmed; {len(tools) - ok} not (not in catalogue, record without the intended target, or name mismatch)", "the verifier corrected two first verdicts (d-APV present as D-Ap5; ivabradine HCN1)")
with open(HERE / "measure_it40.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["case", "metric", "current generator path", "simple baseline", "new path", "note"]); w.writerows(out)
for r in out: print(" | ".join(r)[:330])
