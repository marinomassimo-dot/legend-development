"""Mechanical retrieval measures from one delegate transcript (no judgement).

    python3 transcript_probe.py <agent.jsonl> --anchors a1 a2 ...

Prints JSON: tool calls by name, distinct repository files opened with Read, whether each anchor
string reached the agent's context (appears in a tool RESULT) or only appeared in its own tool INPUT
(a search pattern is not a retrieval), and the final message. Standard library only.
"""
import argparse
import json
import sys


def blocks(content):
    if isinstance(content, list):
        for b in content:
            if isinstance(b, dict):
                yield b


def text_of(x):
    if isinstance(x, str):
        return x
    if isinstance(x, list):
        return "\n".join(text_of(i.get("text", "") if isinstance(i, dict) else i) for i in x)
    return json.dumps(x)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript")
    ap.add_argument("--anchors", nargs="*", default=[])
    ap.add_argument("--anchors-json", help="JSON list of anchors (use when an anchor starts with --)")
    a = ap.parse_args()
    if a.anchors_json:
        a.anchors = json.loads(a.anchors_json)
    calls, files, inputs, results, final = {}, set(), [], [], ""
    for line in open(a.transcript):
        try:
            d = json.loads(line)
        except ValueError:
            continue
        m = d.get("message")
        if not isinstance(m, dict):
            continue
        for b in blocks(m.get("content")):
            t = b.get("type")
            if t == "tool_use":
                calls[b.get("name")] = calls.get(b.get("name"), 0) + 1
                inp = b.get("input", {})
                inputs.append(json.dumps(inp))
                if b.get("name") == "Read" and inp.get("file_path"):
                    files.add(inp["file_path"])
                if b.get("name") == "SubagentHandback":
                    final = inp.get("message", "")
            elif t == "tool_result":
                results.append(text_of(b.get("content")))
            elif t == "text" and m.get("role") == "assistant":
                final = final or b.get("text", "")
    ins, res = "\n".join(inputs), "\n".join(results)
    out = {
        "tool_calls": calls,
        "distinct_read_files": sorted(files),
        "anchors": {x: {"in_context": x in res, "in_own_input_only": (x in ins) and x not in res} for x in a.anchors},
        "final": final,
    }
    json.dump(out, sys.stdout, indent=1)
    print()


if __name__ == "__main__":
    main()
