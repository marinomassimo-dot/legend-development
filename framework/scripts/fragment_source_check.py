#!/usr/bin/env python3
"""Before a composed sentence goes to a blind reader: which of its numbers does the cited source never print?

WHY THIS EXISTS
---------------
IT28 (2026-11-28): 4 of 7 hand-back sentences needed a change of substance at the first blind round
(57 percent, above the 25 to 45 percent band). Three of the four were a number or a negative that
the hand-back carried and the composer copied without matching it to the source text: ages "about
29 and 31" where the main text prints 28 and 31, a residue "S281" that the source never prints (a
count derived from "12 residues upstream"), and "no such effect is reported" where the source
reports a null. A mechanical pre-check is cheaper than a blind round and catches exactly those.

WHAT IT DOES (and only this)
----------------------------
For each fragment, against the source text files you name:
  * NUMBERS the source never prints as a whole token (a derived or mistyped number is listed);
  * ABSOLUTE or scope words (only, no, none, every, never, always, all, any, largest, independent ...)
    that need every row of the source read;
  * NEGATIVE phrases ("no such", "not reported", "not stated", "absent") that need a date and a query.
It does NOT judge meaning, units, species or direction. A number printed in the source in another
context passes: this is a floor, not a verdict. Advisory: exit 0 unless --strict and a number is unsupported.

USAGE
-----
  python3 framework/scripts/fragment_source_check.py --fragment "text" --source a.xml --source b.txt
  python3 framework/scripts/fragment_source_check.py --edits edits.py [--tag S1] --source a.xml
where edits.py defines X = [dict(old=..., new=..., tag=...)] (the fragment-edit files of the card and
ledger batches). XML/HTML tags are stripped; text is lower-cased and whitespace collapsed.
"""
import argparse, importlib.util, re, sys
from pathlib import Path

ABSOLUTE = ["only", "none", "never", "always", "every", "all", "any", "largest", "smallest", "sole",
            "independent", "no", "not"]
NEGATIVE = re.compile(r"\b(no such|not reported|not stated|not given|not recorded|none found|absent|never read|"
                      r"no [a-z\- ]{0,30}reported|without [a-z\- ]{0,20}data)\b", re.I)
UNIT = r"(?:years?|yrs?|y|months?|mo|weeks?|wk|days?|d|hours?|h|ms|msec|s|min|µv|uv|mv|v|µm|um|mm|µl|ul|ml|mg|µm|hz|%|percent|-?fold|×|x)"
NUMBER = re.compile(r"(?<![\d.])(\d+(?:[.,]\d+)?)(?!\d)")
NUMUNIT = re.compile(r"(?<![\d.])(\d+(?:[.,]\d+)?)\s*-?\s*(" + UNIT + r")(?![a-z])")


def normalise(text):
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace(" ", " ").replace("−", "-").replace("–", "-")
    return re.sub(r"\s+", " ", text).lower()


def source_numbers(texts):
    """Whole-token numbers, and number+unit pairs ('29-year-old' gives ('29', 'year'))."""
    out = set()
    for t in texts:
        for m in NUMBER.finditer(t):
            out.add(m.group(1).replace(",", "."))
        for m in NUMUNIT.finditer(t):
            out.add(m.group(1).replace(",", ".") + "|" + m.group(2).rstrip("s"))
    return out


def check(fragment, numbers):
    frag = fragment.lower()
    unsupported = set()
    for m in NUMBER.finditer(frag):
        n = m.group(1).replace(",", ".")
        if len(n.replace(".", "")) >= 5:   # identifiers (PMID, PMC) are not measurements
            continue
        u = NUMUNIT.match(frag, m.start())
        if u:
            if n + "|" + u.group(2).rstrip("s") not in numbers:
                unsupported.add(n + " " + u.group(2))
        elif n not in numbers:
            unsupported.add(n)
    unsupported = sorted(unsupported, key=lambda s: (len(s), s))
    absolutes = sorted({w for w in ABSOLUTE if re.search(r"\b" + w + r"\b", frag) and w not in ("no", "not")}
                       | ({"no/not"} if re.search(r"\b(no|not)\b", frag) else set()))
    negatives = sorted({m.group(0).lower() for m in NEGATIVE.finditer(fragment)})
    return unsupported, absolutes, negatives


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--fragment")
    ap.add_argument("--edits")
    ap.add_argument("--tag")
    ap.add_argument("--source", action="append", required=True)
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args(argv)
    texts = [normalise(Path(p).read_text(encoding="utf-8", errors="replace")) for p in a.source]
    numbers = source_numbers(texts)
    frags = []
    if a.fragment:
        frags.append(("fragment", a.fragment))
    if a.edits:
        spec = importlib.util.spec_from_file_location("edits_mod", a.edits)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        frags += [(x["tag"], x["new"]) for x in mod.X if not a.tag or x["tag"] == a.tag]
    if not frags:
        ap.error("give --fragment or --edits")
    bad = 0
    for tag, frag in frags:
        unsupported, absolutes, negatives = check(frag, numbers)
        bad += bool(unsupported)
        print(f"[{tag}] numbers not printed in the sources: {unsupported or 'none'}")
        print(f"[{tag}] absolute or negation words (need every row read): {absolutes or 'none'}")
        print(f"[{tag}] negative phrases (need a date and a query): {negatives or 'none'}")
    return 1 if (a.strict and bad) else 0


if __name__ == "__main__":
    sys.exit(main())
