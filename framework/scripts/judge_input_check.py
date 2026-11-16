#!/usr/bin/env python3
"""Cheap completeness check of an anonymised judge input, BEFORE any judge is launched.

    python3 framework/scripts/judge_input_check.py --input FILE [FILE ...] [--block-regex RE] [--min-chars N] [--manifest TSV --min-share F]
                                                  [--forbidden WORD,WORD] [--expect-blocks N] [--criteria FILE --expect-criteria-sha256 HEX]
    python3 framework/scripts/judge_input_check.py --help

Why. On 2026-11-16 the first judge run of the leap round was INVALID: the anonymiser deleted every line containing the word 'Perspective', which blanked the whole body of the ten one-line or
one-paragraph hypotheses; the judge saw 14 full hypotheses, 5 titles and 5 absent, and scored the blanked ones as 'no' (77 turns, 54,395 output tokens, no use). A completeness check
costs no model call. It reads the anonymised input and refuses when
  1. a block (a heading matching --block-regex, default `^#{2,3} J\\d+`) has fewer than --min-chars (default 400) characters of text after its id, heading line included (a one-paragraph hypothesis sits on its heading line);
  2. with --manifest (a TSV `block_id<TAB>original_chars` written by the anonymiser from the ORIGINAL text) a block kept less than --min-share (default 0.6) of its original length, or a block of the manifest is missing;
  3. a --forbidden word (case-insensitive; the perspective, arm or session vocabulary the anonymiser must have removed) is still present;
  4. with --expect-blocks N: another number of blocks than N; and, whatever N, a gap in the numbering J01..Jn (a deleted heading line removes a block altogether);
  5. with --criteria and --expect-criteria-sha256: the criteria file is not exactly the frozen one (the comparison criteria stay stable: a change is a new round, not an edit).
It prints the block table and exits 0 only when every check holds. Thresholds are arguments recorded in the setup file BEFORE the run; the tool does not choose them. Not medical advice.
"""
import argparse, csv, hashlib, re, sys
from pathlib import Path

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", nargs="+"); ap.add_argument("--block-regex", default=r"^#{2,3} J\d+"); ap.add_argument("--min-chars", type=int, default=400)
    ap.add_argument("--manifest"); ap.add_argument("--min-share", type=float, default=0.6); ap.add_argument("--forbidden", default="")
    ap.add_argument("--criteria"); ap.add_argument("--expect-criteria-sha256"); ap.add_argument("--expect-blocks", type=int)
    a = ap.parse_args()
    if not a.input:
        ap.print_help(); sys.exit(0)
    rx = re.compile(a.block_regex)
    blocks, problems = {}, []
    for f in a.input:
        cur = None
        for line in Path(f).read_text(encoding="utf-8").splitlines():
            if rx.match(line):
                m = re.match(r"^#+\s*(\S+?)[.\s]", line + " ")
                cur = m.group(1) if m else line[:12]
                blocks[cur] = {"file": Path(f).name, "heading": line, "body": []}
            elif cur is not None:
                blocks[cur]["body"].append(line)
    if not blocks:
        problems.append(f"no block matches {a.block_regex!r}: the input is not what the check expects")
    if a.expect_blocks is not None and len(blocks) != a.expect_blocks:
        problems.append(f"{len(blocks)} blocks found, {a.expect_blocks} expected (the judge is told how many hypotheses it has: a deleted heading line removes a block altogether)")
    nums = sorted(int(m.group(2)) for b in blocks for m in [re.match(r"^([A-Za-z]+)(\d+)$", b)] if m)
    if nums and len(nums) == len(blocks):
        gaps = [n for n in range(1, nums[-1] + 1) if n not in nums]
        if gaps:
            problems.append("the numbering has gaps, so blocks are missing: " + ", ".join(str(g) for g in gaps[:10]))
    manifest = {}
    if a.manifest:
        manifest = {r[0]: int(r[1]) for r in csv.reader(open(a.manifest, encoding="utf-8"), delimiter="\t") if r and r[0] != "block_id"}
        for bid in manifest:
            if bid not in blocks:
                problems.append(f"block {bid} of the manifest is absent from the input")
    rows = []
    for bid, b in blocks.items():
        n = len((re.sub(r"^#+\s*\S+?[.\s]", "", b["heading"] + " ", count=1) + "\n" + "\n".join(b["body"])).strip())      # a one-paragraph hypothesis sits on its own heading line: heading text after the id counts
        row = [bid, b["file"], n]
        if n < a.min_chars:
            problems.append(f"block {bid}: text of {n} characters, below the floor {a.min_chars} (a blanked or truncated hypothesis)")
        if bid in manifest:
            share = n / max(manifest[bid], 1); row.append(f"{share:.2f}")
            if share < a.min_share:
                problems.append(f"block {bid}: kept {share:.0%} of its original {manifest[bid]} characters, below {a.min_share:.0%}")
        rows.append(row)
    text = "\n".join("\n".join([b["heading"]] + b["body"]) for b in blocks.values())
    for w in [x.strip() for x in a.forbidden.split(",") if x.strip()]:
        hits = len(re.findall(re.escape(w), text, re.I))
        if hits:
            problems.append(f"forbidden word {w!r} is still present ({hits} time(s)): the anonymiser did not remove it")
    if a.criteria:
        got = hashlib.sha256(Path(a.criteria).read_bytes()).hexdigest()
        if not a.expect_criteria_sha256:
            problems.append("--criteria needs --expect-criteria-sha256: the criteria are frozen by their digest")
        elif got != a.expect_criteria_sha256:
            problems.append(f"the criteria file is not the frozen one (sha256 {got[:12]}..., expected {a.expect_criteria_sha256[:12]}...): a change of criteria is a new round")
    print("block\tfile\tbody_chars" + ("\tshare_of_original" if manifest else ""))
    for r in rows: print("\t".join(map(str, r)))
    print(f"blocks {len(blocks)}; smallest body {min((r[2] for r in rows), default=0)} characters")
    for p in problems: print("REFUSED:", p, file=sys.stderr)
    print("OK: the input is complete by the stated thresholds" if not problems else f"NOT OK: {len(problems)} problem(s); no judge should be launched on this input")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
