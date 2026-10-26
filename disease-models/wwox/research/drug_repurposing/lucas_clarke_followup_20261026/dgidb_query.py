#!/usr/bin/env python3
"""DGIdb query for the resolved targets of the Lucas-Clarke follow-up (scientist-c, 2026-10-26).
Uses kg_thin_slice.drug_packet unchanged (the repository's DGIdb door); symbols are HGNC symbols
resolved in target_resolution.tsv. Writes the packet and a flat TSV of every interaction returned.
Run from the repository root: python3 <this file>"""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / ".claude/skills/legend-hypothesis-forge/scripts"))
import kg_thin_slice as k
HERE = Path(__file__).resolve().parent
SYMS = ["PDK1","PDK2","PDK3","PDK4","LDHA","LDHB","LDHC","ATF4","EIF2AK1","EIF2AK2","EIF2AK3","EIF2AK4",
        "EIF2B1","EIF2B2","EIF2B3","EIF2B4","EIF2B5","PPP1R15A","PPP1R15B","EIF2S1","SLC16A1"]
pk = k.drug_packet(set(SYMS), raw_dir=HERE / "dgidb_raw")
(HERE / "dgidb_packet.json").write_text(json.dumps({x: pk[x] for x in ("status","unmatched_symbols","coverage_statement","batches")}, indent=1))
rows = []
for gene, ints in sorted(pk["interactions"].items()):
    for it in ints:
        rows.append("\t".join([gene, it["drug"]["name"], it["drug"]["conceptId"] or "", str(it["drug"]["approved"]),
            ";".join(f'{t["type"]}({t["directionality"]})' if t.get("type") else "" for t in it["interactionTypes"]) or "NO_TYPE",
            ";".join(sorted({s["sourceDbName"] for s in it["sources"]})), str(len(it["publications"]))]))
(HERE / "dgidb_interactions.tsv").write_text("gene\tdrug\tconcept\tapproved\taction_types\tsources\tn_pubs\n" + "\n".join(rows) + "\n")
print(pk["status"], pk["unmatched_symbols"], len(rows), "interactions;", {g: len(v) for g, v in pk["interactions"].items()})
