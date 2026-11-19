"""ADV-097 / ADV-095 catalogue contribution, three levels (IT, 2026-11-19): for each queried name of catalogue_lookup_it_20261119.tsv keep only EXACT-name catalogue records
(substring matches such as paromomycin for omomyc are noise) and separate three things that a catalogue match tends to blur:
  L_present      the compound is a catalogue record (identity, status class, access flag);
  L_target       a target annotation exists for the thread's need (target, action, direction state of the NEED); an annotation is a database row, not an effect in WWOX cells;
  L_pharm        VERIFIED pharmacological support held in the repository: a ranking unit that mentions the name AND carries a pharmacological comparison record (CMP-nn);
                 otherwise 'none held'. Nothing was verified in this window (the ChEMBL and GtoPdb caches are absent on this machine).
Also: ranking_text_hits (how often the name occurs in ranking.json) and the units naming it. Read-only. Usage: python3 -I three_levels_it_20261119.py REPO_ROOT | --help"""
import csv, json, re, sys
from pathlib import Path

if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0 if len(sys.argv) > 1 else 2)
ROOT = Path(sys.argv[1]).resolve()
HERE = Path(__file__).resolve().parent
rk = json.loads((ROOT / "disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/ranking.json").read_text(encoding="utf-8"))
units = {u["unit_id"]: u for u in rk["units"]}
unit_text = {k: json.dumps(v, ensure_ascii=False).lower() for k, v in units.items()}
ALIAS = {"dichloroacetate": ["dichloroacetic acid", "sodium dichloroacetate", "dichloroacetate"], "4-phenylbutyrate": ["4-phenylbutyric acid", "4-phenylbutyrate"],
         "valproate": ["valproic acid", "valproate", "sodium valproate"], "tert-butylhydroquinone": ["tert-butylhydroquinone", "tbhq"]}
LABEL = {k: str(v.get("label") or v.get("name") or v.get("unit_label") or v.get("title") or "").lower() for k, v in units.items()}
whole = json.dumps(rk, ensure_ascii=False).lower()
rows = list(csv.DictReader((HERE / "catalogue_lookup_it_20261119.tsv").open(encoding="utf-8"), delimiter="\t"))
out = []
seen = set()
for r in rows:
    q = r["queried_name"].lower()
    thread = r["thread"]
    key = (thread, q)
    if key in seen:
        continue
    seen.add(key)
    mine = [x for x in rows if x["thread"] == thread and x["queried_name"].lower() == q]
    names = ALIAS.get(q, [q])
    exact = [x for x in mine if x["result"] == "IN_CATALOGUE" and any(x["catalogue_name"].lower().replace("-", "") .startswith(n.replace("-", "")) for n in names)]
    named_units = sorted(k for k, t in unit_text.items() if q in t)
    # verified pharmacology = the unit's OWN label names the compound or class and the unit carries a pharmacological comparison record; a mention in other units' text is not a record on the compound
    cmp_units = [f"{k}:{units[k]['comparison_record']}" for k in named_units if units[k].get("comparison_record") and any(n in LABEL[k] for n in names)]
    hits = whole.count(q)
    if not exact:
        out.append((thread, r["queried_name"], "no", "", "", "", "none", "none held", hits, ",".join(named_units)))
        continue
    st = sorted({x["status_class"] for x in exact}); ac = sorted({x["access"] for x in exact if x["access"]})
    tg = sorted({t.strip() for x in exact for t in x["targets_and_needs"].split(";")[1:] if t.strip()})
    tgt_n = max(int(re.search(r"target_rows=(\d+)", x["targets_and_needs"]).group(1)) for x in exact)
    on_need = "; ".join(tg) if tg else "no target row on a named need"
    out.append((thread, r["queried_name"], "yes", "|".join(sorted({x['catalogue_id'] for x in exact})), "|".join(st), "|".join(ac) or "unknown/unverified", f"{tgt_n} rows total; {on_need}"[:400], ("; ".join(cmp_units) if cmp_units else "none held"), hits, ",".join(named_units)))
with (HERE / "catalogue_three_levels_it_20261119.tsv").open("w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["thread", "queried_name", "L_present", "catalogue_ids", "status_class", "access_flag", "L_target_annotation", "L_pharm_verified_in_repository", "ranking_text_hits", "ranking_units_naming_it"])
    w.writerows(out)
print(len(out), sum(1 for o in out if o[2] == "yes"), sum(1 for o in out if o[7] != "none held"))
