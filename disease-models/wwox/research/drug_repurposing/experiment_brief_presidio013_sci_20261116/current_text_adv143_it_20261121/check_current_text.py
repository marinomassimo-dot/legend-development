"""ADV-143 checks for the governing current text (IT, 2026-11-21).

Usage: python3 check_current_text.py NEW.md OLD_A.md OLD_B.md [REPLACEMENTS.tsv]
  Optional 4th argument: the design team's replacements file; its numeric_tokens columns (all rows) are then also allowed in the
  body, and numbers that occur in an inserted answer but in no numeric_tokens column are listed as [4] for reconciliation.
  1. numeric tokens: every number in the laboratory body of NEW (outside headings, the status box, OPEN-GAP markers
     and the history section) must also occur as a token in OLD_A or OLD_B; prints the ones that do not.
  2. history: every blockquote line of the history section (lines starting with '> ') must occur verbatim, after
     whitespace and markdown-emphasis normalisation, in OLD_A or OLD_B.
  3. dropped numbers (information): numeric tokens of the old texts that occur nowhere in NEW (body or history).
Exit 1 when check 1 or 2 finds anything. It reads files only and writes nothing."""
import re
import sys

TOK = re.compile(r"(?<![A-Za-z0-9.])\d+(?:[.,]\d+)?")
IDS = re.compile(r"\b(?:Q|C|T|E|L|R|P|S|M|H|N)\d{1,3}\b|\bADV-\d+\b|\b\d{4}-\d{2}-\d{2}\b|\bPMID\s*\d+\b|\bFTR-[\w-]+\b")


def norm(s):
    s = re.sub(r"[*_`]", "", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def tokens(text):
    text = IDS.sub(" ", text)
    return set(TOK.findall(text))


def split_new(text):
    """Return (body_lines, history_lines). Body excludes headings, the status box (between STATUS-BOX markers),
    OPEN-GAP lines, and everything from the line '## History' on."""
    body, hist, mode, box = [], [], "body", False
    for ln in text.split("\n"):
        if ln.startswith("## ") and "history" in ln.lower():
            mode = "hist"
        if "<!-- STATUS-BOX -->" in ln:
            box = not box
            continue
        if mode == "hist":
            hist.append(ln)
        elif not box and not ln.startswith("#") and "OPEN-GAP" not in ln:
            body.append(ln)
    return body, hist


def main(argv):
    new_p, a_p, b_p = argv[1:4]
    new, a, b = (open(p, encoding="utf-8").read() for p in (new_p, a_p, b_p))
    old = a + "\n" + b
    old_tok, old_norm = tokens(old), norm(old)
    extra, own = set(), set()
    if len(argv) > 4:
        import csv
        for r in csv.DictReader(open(argv[4], encoding="utf-8", newline=""), delimiter="\t"):
            extra |= set(x.strip() for x in r["numeric_tokens"].split(";") if re.fullmatch(r"\d+(?:[.,]\d+)?", x.strip()))
            for x in r["numeric_tokens"].split(";"):
                if x.strip() and not x.strip().startswith(("see text", "every number traces")) and not re.fullmatch(r"\d+(?:[.,]\d+)?", x.strip()):
                    print(f"[note] {r['repl_no']}: numeric_tokens entry is not a number: {x.strip()[:80]!r}")
            own |= tokens(r["replacement_text"])
        old_tok = old_tok | extra
    body, hist = split_new(new)
    bad = []
    for n, ln in enumerate(body, 1):
        miss = sorted(tokens(ln) - old_tok)
        if miss:
            bad.append((n, miss, ln.strip()[:140]))
    print(f"[1] numeric tokens in the body that are not in the old texts: {len(bad)} line(s)")
    for n, miss, ln in bad:
        print(f"    body line {n}: {miss} :: {ln}")
    bad2 = []
    for ln in hist:
        if ln.startswith("> "):
            q = norm(ln[2:])
            if q and q not in old_norm:
                bad2.append(q[:140])
    print(f"[2] history quotation lines not verbatim in the old texts: {len(bad2)}")
    for q in bad2:
        print("    ", q)
    new_tok = tokens("\n".join(body + hist))
    dropped = sorted(old_tok - new_tok, key=lambda x: float(x.replace(",", ".")))
    print(f"[3] (information) numeric tokens of the old texts absent from the new text: {len(dropped)}")
    print("    ", dropped[:80])
    if len(argv) > 4:
        unl = sorted((own - extra) - tokens(old), key=lambda x: float(x.replace(",", ".")))
        print(f"[4] numbers that occur in an inserted answer but in no numeric_tokens column and not in the older texts: {len(unl)}")
        print("    ", unl)
        inbody = sorted(tokens("\n".join(body)) - tokens(old) - extra)
        print(f"[5] numbers in the body that are in neither the older texts nor any numeric_tokens column: {len(inbody)}")
        print("    ", inbody)
        bad = [x for x in bad if sorted(tokens(x[2]) - old_tok)] if False else bad
    return 1 if (bad or bad2) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
