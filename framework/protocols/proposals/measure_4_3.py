#!/usr/bin/env python3
"""Measurement behind proposal §4.3 of 2026-09-09_receipt_schema_proposals.md.

Read-only. Numbers move; re-run rather than quoting the table.
Run from the repository root: python3 framework/protocols/proposals/measure_4_3.py
"""
import os, sys, pathlib
_ROOT = pathlib.Path(__file__).resolve().parents[3]
os.chdir(_ROOT)
sys.path.insert(0, str(_ROOT / "framework/scripts"))
import json, pathlib, collections
MAN = pathlib.Path('disease-models/wwox/research/deepdive_manifests')
COUPLED = {"text_contradicted_by_panel", "panel_qualifies_text"}

rows = []
for path in sorted(MAN.glob('PMID*.json')):
    doc = json.loads(path.read_text(encoding='utf-8'))
    for i, e in enumerate((doc.get('verbatim_locators') or {}).get('entries') or []):
        if isinstance(e, dict):
            rows.append((path.name, i, str(e.get('surface') or '—'),
                         'page_anchor' in e,
                         str(e.get('panel_text_relation') or '—')))

n = len(rows)
adj = [r for r in rows if r[3]]
coupled = [r for r in rows if r[4] in COUPLED]
adj_manifests = sorted({r[0] for r in adj})
adj_fig = [r for r in adj if r[2] == 'figure']

print(f"manifests scanned                          : {len(set(r[0] for r in rows))}")
print(f"locator entries                            : {n}")
print(f"coupled-relation locators                  : {len(coupled)}")
print(f"  by surface                               : "
      f"{dict(collections.Counter(r[2] for r in coupled))}")
print(f"page-adjudicated locators (rule 5e)        : {len(adj)} "
      f"across {len(adj_manifests)} manifest(s)")
print(f"  by surface                               : "
      f"{dict(collections.Counter(r[2] for r in adj))}")
print(f"  ...declaring surface `figure`             : {len(adj_fig)}")
print(f"page-adjudicated AND carrying a relation   : "
      f"{len([r for r in adj if r[4] in COUPLED])}")
print(f"  relation values used on adjudicated rows : "
      f"{dict(collections.Counter(r[4] for r in adj))}")
# 🔴 Only the reader who drew a crop knows whether it shows a paragraph or a blot. Nothing in
# the JSON records it, so this count is what a NOTE happens to say — a lower bound on the
# adjudicated-text population, never a measurement of it. That is the proposal's whole point.
self_declared_text = 0
per_manifest = collections.Counter()
for path in sorted(MAN.glob('PMID*.json')):
    doc = json.loads(path.read_text(encoding='utf-8'))
    for e in (doc.get('verbatim_locators') or {}).get('entries') or []:
        if isinstance(e, dict) and 'page_anchor' in e:
            if 'ADJUDICATED TEXT' in str(e.get('note') or '').upper():
                self_declared_text += 1
                per_manifest[path.name] += 1
print(f"  ...self-declaring ADJUDICATED TEXT in a note : {self_declared_text} "
      f"{dict(per_manifest)}")
print()
print("🔴 The collision, stated as a count: on the `figure` surface,")
print(f"   {len(adj_fig)} entries are PAGE CROPS and "
      f"{len([r for r in rows if r[2]=='figure' and not r[3]])} are direct panel readings.")
print("   `surface` says `figure` for both, so it no longer separates a rendering of running")
print("   text from a reading of a panel — and a rule that keys the coupled relation on")
print("   `surface == figure` can no longer tell them apart. How many of the 74 crops show")
print("   text is NOT derivable from the manifests: only the note above hints at it.")
print()
print("manifests using page adjudication:")
for m in adj_manifests:
    a = [r for r in adj if r[0] == m]
    print(f"   {m}: {len(a)} adjudicated locator(s)")
