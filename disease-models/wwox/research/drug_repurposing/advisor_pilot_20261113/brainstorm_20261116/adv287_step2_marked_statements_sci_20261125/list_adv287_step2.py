#!/usr/bin/env python3
"""ADV-287 step 2: the 22 card statements carrying a superlative or count word, with the word role
frozen from the sentence alone. Run: python3 -P -E list_adv287_step2.py -> list_adv287_step2.tsv"""
import csv, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
STEP1 = os.path.join(HERE, "../adv287_card_statements_sci_20261125")
PAT = r"\bthe one\b|\bthe only\b|\blargest\b|\bthree independent\b|\bnone\b|\bat least\b|\bevery\b|\bindependent\b"
def read(p): return list(csv.DictReader(open(p), delimiter="\t", quoting=csv.QUOTE_NONE))
uni = [r for r in read(os.path.join(STEP1, "universe_adv287.tsv")) if not r["card_exclusion"] and not r["obeid_flag"]]
hits = [r for r in uni if re.search(PAT, r["sentence"], re.I)]
st1 = read(os.path.join(STEP1, "producer/STEP1_TABLE_ADV287.tsv"))
# k -> step-1 n (matched on card and sentence), word role judged on the sentence alone
INCIDENTAL = {3: "'is not the only candidate' is a hedge", 6: "'the one below' is a pronoun",
              16: "'every 3 to 6 months' is an interval", 21: "'independent clones' inside a proposed design"}
out = []
for k, r in enumerate(hits, 1):
    prior = [x for x in st1 if x["card"] == r["card"] and x["sentence"][:80] == r["sentence"][:80]]
    words = ";".join(m.group(0) for m in re.finditer(PAT, r["sentence"], re.I))
    status = ("AUDITED_STEP1 n=%s" % prior[0]["n"]) if prior else ("OBEID_STOP" if k == 5 else "NEW")
    out.append((str(k), r["card"], words, "INCIDENTAL: " + INCIDENTAL[k] if k in INCIDENTAL else "LOAD_BEARING",
                status, r["field_paths"], r["sentence"]))
with open(os.path.join(HERE, "list_adv287_step2.tsv"), "w") as o:
    o.write("k\tcard\tmatched_words\tword_role\tstatus\tfield_paths\tsentence\n")
    for row in out: o.write("\t".join(row) + "\n")
import collections
print(len(out), collections.Counter(x[4].split()[0] for x in out),
      collections.Counter(x[3].split(":")[0] for x in out if x[4] == "NEW"))
# comparator: step-1 assessable statements split by the same pattern
ass = [x for x in st1 if x["class"].upper().startswith(("CORRECT", "INCOMPLETE", "WRONG"))]
agreed_err = {"1", "2", "3", "14", "15", "20"}   # RESULT ADV-287 section 1 (both readers)
for label, flag in (("marked", True), ("unmarked", False)):
    sub = [x for x in ass if bool(re.search(PAT, x["sentence"], re.I)) is flag]
    print(label, len(sub), sorted((x["n"] for x in sub), key=int), "errors", sorted((x["n"] for x in sub if x["n"] in agreed_err), key=int))
