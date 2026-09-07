#!/usr/bin/env python3
"""CANONICAL_CROSS_CLAIM_CONTRADICTION — screen the claim registry for pairs of claims
that state incompatible things about the same entity and endpoint.

🔴 THIS IS A SCREEN, NOT A VERDICT. It returns *candidate* pairs for human adjudication.
A genuine contradiction and a species/region/stage/endpoint difference look identical to a
matcher, and most candidates it returns are NOT contradictions. Reporting its hit count as a
contradiction count would be a claim about the instrument, not about the corpus.

Provenance: written for CC-20260826-CROSS-CLAIM-CENSUS-01, which adjudicated its output by
hand — 39 claims, 741 possible pairs, 40 screened positive, 2 survived adjudication.

🔴 SCALE. This is O(n^2) over claims: 741 pairs at n=39, ~500k at n=1000, ~50M at n=10000.
It will NOT survive the thousandth batch in this form. Before it becomes a gate it must be
re-cast as an index over (entity, endpoint) buckets — linear in claims, quadratic only within
a bucket. The limit is written here rather than discovered later as a check that quietly
starts timing out.

Usage:
    python3 framework/scripts/cross_claim_contradiction_census.py [--registry PATH] [--top N]
"""
import argparse
import itertools
import re
import sys

DEFAULT_REGISTRY = "disease-models/wwox/registries/claim_registry_current.md"

MODELS = {
    "wwox_null_mouse": r"Wwox[-\s]?null|Wwox−/−|Wwox-/-|full KO|topi Wwox-null",
    "rat_lde": r"\blde\b|lethal dwarfism",
    "syn_cre": r"S-KO|Synapsin[- ]Cre|SynI-Cre|Syn-Cre",
    "nes_cre": r"N-KO|Nestin[- ]Cre|Nes-Cre",
    "het": r"Wwox\+/−|Wwox\+/-|eterozigot|heterozygo",
    "p47t": r"P47T",
    "human": r"\bWOREE\b|\bSCAR12\b|patient|paziente",
}

ENDPOINTS = {
    "seizure": r"seizur|crisi|convuls|epileps|epileptiform|SWD|spike-wave|epilettogen|epileptogen",
    "myelin": r"myelin|mielin|g-ratio|OPC|oligodendro",
    "glia": r"GFAP|Iba1|IBA1|glios|neuroinfiamm|neuroinflamm",
    "survival": r"surviv|sopravviven|letalit|lethal|mortal",
    "glucose": r"glucos|glicem|glycem|hypoglyc|ipoglic",
    "gaba": r"GABA|PV-positive|interneuron|KCC2|NKCC1",
    "gsk3": r"GSK3|glycogen synthase kinase",
}

DIRECTION = {
    "ABSENT": r"\bassente\b|\babsent\b|\bnot reported\b|non riportat|\bno epilepsy\b|\bnessun\b|mai\b",
    "PRESENT": r"\bpresent\b|\bpresente\b|\bexhibit|\bshow[ns]?\b|\bdisplay|\bosservat|\bobserved\b",
    "INCREASED": r"\bincreas|\belevat|\bhigher\b|\bhyperex|\benhanced\b|\bmaggior|↑",
    "DECREASED": r"\bdecreas|\breduc|\blower\b|\bridott|\bsuppress|\bminor|↓",
    "RESCUE": r"\brescu|\brecuper|\brestor|\bnormaliz|\bcorrect",
    "NO_RESCUE": r"\bnon recupera\b|\bfails? to rescue\b|\bincomplet|\bnon normalizza",
    # A prohibition is the highest-risk object a claim can carry: it is the only construct
    # that can make the registry self-violating, and LINT does not look for it.
    "PROHIBIT": r"may not|must not|non può|nessun[a]? (?:claim|statement|affermazione)|No canonical statement",
}

OPPOSED = [("ABSENT", "PRESENT"), ("INCREASED", "DECREASED"),
           ("RESCUE", "NO_RESCUE"), ("PROHIBIT", "PRESENT")]


def parse_claims(text):
    parts = re.split(r"\n## (CLAIM \d+)\n", text)
    return {parts[i]: parts[i + 1] for i in range(1, len(parts), 2)}


def field(body, name):
    m = re.search(r"\*\*" + name + r":\*\*\s*(.*)", body)
    return m.group(1) if m else ""


def characterise(body):
    return {
        "title": field(body, "Title"),
        "status": field(body, "Status"),
        "pmids": set(re.findall(r"PMID\s*(\d{6,9})", body)),
        "papers": set(re.findall(r"PAPER (\d+)", body)),
        # Claims this one names. A pair that cites each other has ALREADY been
        # reconciled by whoever wrote them; a pair that does not has never been
        # put side by side. That is the highest-precision signal in this file.
        "cites": {"CLAIM %s" % n for n in re.findall(r"CLAIM\s*(\d{3})", body)},
        "models": {k for k, p in MODELS.items() if re.search(p, body, re.I)},
        "endpoints": {k for k, p in ENDPOINTS.items() if re.search(p, body, re.I)},
        "direction": {k for k, p in DIRECTION.items() if re.search(p, body, re.I)},
        "body": body,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", default=DEFAULT_REGISTRY)
    ap.add_argument("--top", type=int, default=18, help="candidate pairs to print")
    args = ap.parse_args()

    try:
        text = open(args.registry, encoding="utf-8").read()
    except OSError as exc:
        print("ERROR: cannot read %s: %s" % (args.registry, exc), file=sys.stderr)
        return 2

    claims = parse_claims(text)
    if not claims:
        print("ERROR: no claims parsed from %s — refusing to report 'no contradictions' "
              "from an empty parse." % args.registry, file=sys.stderr)
        return 2

    recs = {cid: characterise(body) for cid, body in claims.items()}
    n = len(recs)
    print("claims parsed: %d  (possible pairs: %d)" % (n, n * (n - 1) // 2))

    print("\n" + "=" * 72)
    print("SIGNAL 1 — CANONICAL PROHIBITIONS (a claim that forbids a statement)")
    print("=" * 72)
    prohibitions = 0
    for cid in sorted(recs, key=lambda c: int(c.split()[1])):
        for m in re.finditer(
                r"[^.\n]*(?:No canonical statement|may not|must not|"
                r"nessun[ao]? (?:claim|statement|affermazione)|non può essere descritt)[^.\n]*\.",
                recs[cid]["body"]):
            s = m.group(0).strip()
            if len(s) > 30:
                prohibitions += 1
                print("\n[%s] %s" % (cid, s[:400]))
    print("\nprohibitions found: %d" % prohibitions)

    print("\n" + "=" * 72)
    print("SIGNAL 2 — SHARED ENTITY + SHARED ENDPOINT + OPPOSING DIRECTION")
    print("=" * 72)
    pairs = []
    for a, b in itertools.combinations(sorted(recs), 2):
        ra, rb = recs[a], recs[b]
        shared_pm = ra["pmids"] & rb["pmids"]
        shared_pa = ra["papers"] & rb["papers"]
        shared_model = ra["models"] & rb["models"]
        shared_end = ra["endpoints"] & rb["endpoints"]
        if not shared_end or not (shared_model or shared_pm or shared_pa):
            continue
        opp = [(x, y) for x, y in OPPOSED
               if (x in ra["direction"] and y in rb["direction"])
               or (y in ra["direction"] and x in rb["direction"])]
        if not opp:
            continue
        # Reciprocal-citation test. If either claim names the other, the tension is
        # on the record and someone has already looked at it. Unlinked pairs score
        # higher because nobody has.
        linked = (b in ra["cites"]) or (a in rb["cites"])
        score = (len(shared_pm) * 3 + len(shared_pa) * 3 + len(shared_model) * 2
                 + len(shared_end) * 2 + len(opp) + (0 if linked else 4))
        pairs.append((score, a, b, shared_pm, shared_pa, shared_model, shared_end, opp, linked))

    pairs.sort(reverse=True)
    shown = min(args.top, len(pairs))
    print("\ncandidate pairs: %d — showing %d" % (len(pairs), shown))
    if shown < len(pairs):
        # No silent caps: say what was dropped.
        print("NOT SHOWN: %d further pair(s) below the --top cutoff." % (len(pairs) - shown))
    print()
    unlinked = sum(1 for p in pairs if not p[8])
    for sc, a, b, pm, pa, mo, en, opp, linked in pairs[:shown]:
        print("--- score %d | %s <-> %s   [%s]"
              % (sc, a, b, "cross-linked" if linked else "NOT CROSS-LINKED"))
        print("    A: %s" % recs[a]["title"][:105])
        print("    B: %s" % recs[b]["title"][:105])
        print("    shared PMID=%s PAPER=%s model=%s endpoint=%s"
              % (sorted(pm) or "-", sorted(pa) or "-", sorted(mo) or "-", sorted(en)))
        print("    opposing: %s\n" % opp)

    print("=" * 72)
    print("%d of %d candidate pairs are NOT cross-linked." % (unlinked, len(pairs)))
    print("A pair that names each other has been reconciled by whoever wrote it -- CLAIM 009 and")
    print("CLAIM 034 are the worked example, an opposite-direction pair carrying a three-reason")
    print("non-transfer boundary. A pair that does not has never been put side by side.")
    print()
    print("These are CANDIDATES. Adjudicate each against the primaries before calling any of")
    print("them a contradiction: species, brain region, developmental stage and endpoint")
    print("differences all produce this signature legitimately. Classify each as")
    print("TRUE_CONTRADICTION / CONTEXTUAL_DISSOCIATION / NOMENCLATURE_CONFLICT / MISLOCATOR /")
    print("INSUFFICIENT -- and do not grow the count with ambiguous cases.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
