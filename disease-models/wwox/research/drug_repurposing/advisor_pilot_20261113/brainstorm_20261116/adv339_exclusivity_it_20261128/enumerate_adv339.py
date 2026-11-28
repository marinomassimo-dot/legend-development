"""Candidate net for ADV-339: exclusivity-marker sentences in claim records (see PREREG_ADV339.md)."""
import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
sys.path.insert(0, str(ROOT / "framework" / "scripts"))
import registry_records as rr  # noqa: E402

MARK = re.compile(
    r"\b(only|alone|every|all remaining|no other|none|solo|soltanto|solamente|unic[oaie]|ogni|tutt[ie]|"
    r"nessun[ao]?|esclusivamente)\b", re.I)
ARM = re.compile(
    r"KO\b|knock|null|line[as]?\b|linea|arm\b|bracci|genotip|genotype|model|mouse|mice|topo|topi|rat\b|ratt|"
    r"cell|cellul|neuron|oligo|astro|organoid|spheroid|sferoid|fibroblast|iPSC|fly|Drosophila|zebrafish|"
    r"EM\b|assay|endpoint|measure|misur|conteg|count|blot|stain|immuno", re.I)

records = rr.load_all(ROOT, "wwox", ["claim_registry_current"])["claim_registry_current"]
out = []
for rec in records:
    text = getattr(rec, "text", None) or getattr(rec, "body", "")
    title = getattr(rec, "record_id", None) or getattr(rec, "id", "")
    if not str(title).startswith("CLAIM "):
        continue
    pmids = sorted(set(re.findall(r"PMID:?\s*(\d{7,8})", text)))
    for para in text.split("\n"):
        for sent in re.split(r"(?<=[.;])\s+(?=[A-ZÀ-Ý*`«🔴⚠🔵(])", para):
            if MARK.search(sent) and ARM.search(sent):
                out.append({"claim": title, "sentence": sent.strip(), "claim_pmids": pmids})
print(len(records), "records;", len(out), "candidate sentences;", len({o["claim"] for o in out}), "claims", file=sys.stderr)
json.dump(out, sys.stdout, ensure_ascii=False, indent=0)
