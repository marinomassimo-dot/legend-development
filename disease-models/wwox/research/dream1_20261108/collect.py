#!/usr/bin/env python3
"""Collect the 16 DREAM-1 runs: mechanical retrieval measures, census numbers and a blinded grading packet.

    python3 collect.py <tasks dir> <census script> <packet out> <key out>

Reads runs.json (case, condition, agent id), the transcripts <tasks dir>/<id>.output, runs
transcript_probe.py and session_model_census.py on each, writes results/runs.json and results/runs.tsv,
a shuffled packet for the blind grader (case question, rubric, answer; no condition) and the key.
Standard library only.
"""
import json
import random
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
tasks, census, packet_out, key_out = sys.argv[1:5]
cases = {c["id"]: c for c in json.load(open(HERE / "cases.json"))}
runs = json.load(open(HERE / "runs.json"))
rows = []
for r in runs:
    t = f"{tasks}/{r['agent']}.output"
    probe = json.loads(subprocess.run([sys.executable, str(HERE / "transcript_probe.py"), t, "--anchors-json", json.dumps(cases[r["case"]]["anchors"])],
                                      capture_output=True, text=True, check=True).stdout)
    c = subprocess.run([sys.executable, census, t], capture_output=True, text=True).stdout
    num = lambda pat: int(re.search(pat, c).group(1).replace(",", "")) if re.search(pat, c) else None
    rows.append({**r, "tool_calls": sum(probe["tool_calls"].values()), "files_read": len(probe["distinct_read_files"]),
                 "anchors": probe["anchors"], "final": probe["final"],
                 "birth": num(r"birth context ([\d,]+)"), "peak": num(r"peak ([\d,]+)"), "output": num(r"output ([\d,]+)"),
                 "cache_read": num(r"cache read ([\d,]+)"), "turns": num(r"turns (\d+)")})
json.dump(rows, open(HERE / "results" / "runs.json", "w"), indent=1)
with open(HERE / "results" / "runs.tsv", "w") as f:
    f.write("case\tcond\tbirth\tpeak\toutput\tcache_read\tturns\ttool_calls\tfiles_read\tanchors_in_context\n")
    for x in rows:
        seen = ",".join(k for k, v in x["anchors"].items() if v["in_context"]) or "-"
        f.write(f"{x['case']}\t{x['cond']}\t{x['birth']}\t{x['peak']}\t{x['output']}\t{x['cache_read']}\t{x['turns']}\t{x['tool_calls']}\t{x['files_read']}\t{seen}\n")
rng = random.Random(20261108)
order = list(range(len(rows)))
rng.shuffle(order)
packet, key = [], {}
for n, i in enumerate(order, 1):
    x, c = rows[i], cases[rows[i]["case"]]
    key[f"R{n:02d}"] = {"case": x["case"], "cond": x["cond"], "agent": x["agent"]}
    packet.append(f"=== R{n:02d} ===\nQUESTION: {c['question']}\nREQUIRED (each should be present and right):\n" + "\n".join(f"  r{j+1}. {t}" for j, t in enumerate(c["required"])) +
                  "\nFORBIDDEN:\n" + "\n".join(f"  - {t}" for t in c["forbidden"]) + f"\nANSWER:\n{x['final']}\n")
Path(packet_out).write_text("\n".join(packet))
json.dump(key, open(key_out, "w"), indent=1)
print(len(rows), "runs collected")
