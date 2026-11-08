#!/usr/bin/env python3
"""Prompts for the model arms, the simple-rule arm (B) and the scorer.

  python3 arms.py prompt A|C|V [--reverse]   print the chooser prompt for the 16 cases (stdout)
  python3 arms.py rule                       write results/arm_B_rule.tsv and results/arm_B_keywords.tsv
  python3 arms.py score FILE [--reverse]     score one arm file against cases_hidden.tsv

Arm files are tab-separated: case_id <TAB> pick (letter or NONE) <TAB> free note.
With --reverse the shown option order was reversed and relabelled; the scorer maps letters back.
Standard library only.
"""
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LETTERS = "ABCDE"


def load_state():
    return list(csv.DictReader(open(HERE / "cases_state.tsv"), delimiter="\t"))


def load_hidden():
    return {r["case_id"]: r for r in csv.DictReader(open(HERE / "cases_hidden.tsv"), delimiter="\t")}


def split_options(s):
    return [p.split(": ", 1)[1] for p in s.split(" | ")]


def shown(row, reverse):
    opts = split_options(row["options"])
    if reverse:
        opts = opts[::-1]
    return opts


HEAD = {
 "A": ("For each case below, choose the next piece of work that you consider best. "
       "Answer with one letter, or NONE if no option is adequate, and a note of at most 15 words."),
 "C": ("For each case below, score every option from 0 (wrong or wasteful) to 3 (clearly the best next piece of work) "
       "against the state, then choose. NONE is allowed when no option scores 2 or more. Give, in at most 15 words, "
       "the fact missing from the state that would most change your choice, or '-'."),
 "V": ("For each case below, mark every option REASONABLE, WEAK or UNREASONABLE as a next piece of work, given only the state. "
       "Several options may be REASONABLE. Add NONE_SUFFICIENT=yes if no option is adequate, else no."),
}
FORMAT = {
 "A": "Output exactly one line per case, tab-separated: case_id<TAB>letter-or-NONE<TAB>note.",
 "C": "Output exactly one line per case, tab-separated: case_id<TAB>chosen letter-or-NONE<TAB>scores like A=3,B=0,C=1,D=0,E=2<TAB>missing fact.",
 "V": "Output exactly one line per case, tab-separated: case_id<TAB>marks like A=R,B=W,C=U,D=R,E=U (R reasonable, W weak, U unreasonable)<TAB>NONE_SUFFICIENT=yes|no.",
}


def prompt(kind, reverse):
    out = [HEAD[kind],
           "Use only what is written here. Do not call any tool, do not read any file, do not search. "
           "A score or a choice ranks actions against a state; it is not a probability that anything is biologically true. "
           "The listed options are not necessarily in a meaningful order.",
           FORMAT[kind], ""]
    for r in load_state():
        out.append(f"### {r['case_id']}")
        out.append("STATE: " + r["state_text"])
        for k, o in enumerate(shown(r, reverse)):
            out.append(f"{LETTERS[k]}: {o}")
        out.append("")
    return "\n".join(out)


def unmap(letter, n, reverse):
    if letter in ("NONE", "", None) or letter not in LETTERS[:n]:
        return letter
    return LETTERS[n - 1 - LETTERS.index(letter)] if reverse else letter


def rule_b(facts):
    """Simple relevant rule over typed facts. Returns an option class (never REPEAT)."""
    if facts.get("use_requires_check") == "yes" and facts.get("check_done") in ("no", "partial"):
        return "CHECK"
    if facts.get("known_in_repo") == "yes":
        return "REUSE"
    if facts.get("source") == "blocked":
        return "DECLARE"
    if facts.get("source") == "retrievable":
        return "RETRIEVE"
    if facts.get("direction") == "unresolved":
        return "DECLARE"
    if facts.get("in_silico") == "yes":
        return "DEEPEN"
    return "DECLARE"


def rule_keywords(state):
    """Naive rule over the state text only (what a grep-based router could do without typed facts)."""
    s = state.lower()
    if re.search(r"not accessible|403|hup|closed to every route|no pubmed central|not flagged open access", s):
        return "DECLARE"
    if re.search(r"holds a|already holds|dated|keeps dated|has just been recorded|reconciled", s):
        return "REUSE"
    return "DEEPEN"


def pick_by_class(row_hidden, cls):
    hid = json.loads(row_hidden["options_class_label"])
    for L in LETTERS:
        if L in hid and hid[L]["class"] == cls:
            return L
    return "NONE"


def run_rules():
    (HERE / "results").mkdir(exist_ok=True)
    hidden = load_hidden()
    for name, fn in (("arm_B_rule.tsv", lambda r, h: rule_b(json.loads(h["facts"]))),
                     ("arm_B_keywords.tsv", lambda r, h: rule_keywords(r["state_text"]))):
        with open(HERE / "results" / name, "w") as f:
            for r in load_state():
                h = hidden[r["case_id"]]
                cls = fn(r, h)
                f.write(f"{r['case_id']}\t{pick_by_class(h, cls)}\t{cls}\n")


def score(path, reverse=False):
    hidden = load_hidden()
    n_ok = n_best = n_bestcases = n_bad = n_none_ok = n_none_cases = n_none_false = n_cases = 0
    detail = []
    for line in open(path):
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 2 or parts[0] not in hidden:
            continue
        cid, pick = parts[0], parts[1].strip().upper()
        h = hidden[cid]
        n = len(json.loads(h["options_class_label"]))
        pick = unmap(pick, n, reverse)
        ok = set(filter(None, h["acceptable"].split(",")))
        best = set(filter(None, h["best"].split(",")))
        bad = set(filter(None, h["dominated"].split(",")))
        none_exp = h["none_expected"] == "yes"
        n_cases += 1
        hit = (pick == "NONE") if none_exp else (pick in ok)
        n_ok += hit
        if best:
            n_bestcases += 1
            n_best += pick in best
        n_bad += pick in bad
        if none_exp:
            n_none_cases += 1
            n_none_ok += pick == "NONE"
        elif pick == "NONE":
            n_none_false += 1
        detail.append(f"{cid}:{pick}{'+' if hit else '-'}")
    return dict(cases=n_cases, acceptable=n_ok, best=f"{n_best}/{n_bestcases}", dominated_picked=n_bad,
                none_correct=f"{n_none_ok}/{n_none_cases}", none_wrong=n_none_false, detail=" ".join(detail))


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["prompt"]:
        print(prompt(a[1], "--reverse" in a))
    elif a[:1] == ["rule"]:
        run_rules()
    elif a[:1] == ["score"]:
        print(json.dumps(score(a[1], "--reverse" in a), indent=1))
    else:
        print(__doc__)
