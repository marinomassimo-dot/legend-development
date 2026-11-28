"""Enumerate claim-registry sentences that use a corroboration term (deterministic)."""
import csv, hashlib, re, sys

REG = "disease-models/wwox/registries/claim_registry_current.md"
TERMS = re.compile(
    r"independen|indipenden|corrobor|confirm|conferm|replicat|replica[zt]|reproduc|riprodu|converg"
    r"|two (?:studies|groups|papers|reports|cohorts|laborator|independent|labs|separate)"
    r"|due (?:studi|gruppi|lavori|coorti|laborator|fonti|report)"
    r"|both (?:studies|papers|reports|groups)|entramb[ie] (?:gli|i|le) (?:studi|lavori|gruppi|fonti|coorti)"
    r"|second (?:study|group|paper|source|laborator|report)|secondo (?:studio|gruppo|lavoro|laborator)"
    r"|consistent with|coerente con|in agreement|agrees with|in accordo"
    r"|three (?:studies|groups|independent)|tre (?:studi|gruppi)", re.I)
SPLIT = re.compile(r"(?<=[.;!?])\s+(?=[A-ZÀ-Ü0-9*(\[🔴⚠`\"“«-])|(?<=\*\*)\s+(?=\*\*)|\s\|\s")

def main(out):
    raw = open(REG, "rb").read()
    claim, rows = "", []
    for n, line in enumerate(raw.decode().split("\n"), 1):
        m = re.match(r"## CLAIM (\w+)", line)
        if m:
            claim = m.group(1)
            continue
        if not claim:
            continue
        field = re.match(r"\*\*([^*]{1,60}?):?\*\*", line)
        for i, s in enumerate(SPLIT.split(line), 1):
            hits = sorted({h.lower() for h in TERMS.findall(s)})
            if hits:
                rows.append([f"L{n}.{i}", claim, field.group(1) if field else "", ";".join(hits), s.replace("\t", " ").strip()])
    with open(out, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, quotechar=None, escapechar=None)
        w.writerow(["id", "claim", "field", "terms", "sentence"])
        w.writerows(rows)
    print(len(rows), "sentences; registry sha256", hashlib.sha256(raw).hexdigest())

main(sys.argv[1])
