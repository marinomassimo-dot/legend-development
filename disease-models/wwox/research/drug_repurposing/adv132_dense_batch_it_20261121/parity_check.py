"""ADV-132 mechanical parity check: numbers, units, p-forms, symbols, names, negation and hedge cue counts, source (English) against a rendering. Rule: PARITY_RULE_ADV132_IT_20261121.md.
Usage: python3 -I parity_check.py <selected.json> <translations.json> [--lang fr,de,es]    selected: [{"n":..,"text":..}], translations: {"n": {"fr":..,"de":..,"es":..}}"""
import json, re, sys, unicodedata
from collections import Counter

UNITS = r"(?:pA|nA|uA|mV|ms|Hz|kHz|uM|mM|nM|mg|kg|ug|ng|mL|uL|mm|um|nm|kDa|Da|bp|kb|%)"
PCT_WORDS = r"(?:percent|pour cent|Prozent|por ciento)"
NEG = {
    "en": "not no never none cannot nothing without neither nor nobody nowhere",
    "fr": "pas non aucun aucune jamais sans ni rien nullement",
    "de": "nicht kein keine keinen keinem keiner keines nie niemals nichts ohne weder",
    "es": "no ningún ninguno ninguna nunca jamás sin ni nada nadie",
}
HEDGE = {
    "en": "may might would could possibly perhaps probably likely about approximately roughly apparently unknown unclear presumably",
    "fr": "peut peuvent pourrait pourraient probablement vraisemblablement environ approximativement apparemment inconnu inconnue inconnus incertain",
    "de": "kann können könnte könnten würde würden wahrscheinlich vermutlich etwa ungefähr ca unbekannt unklar möglicherweise vielleicht",
    "es": "puede pueden podría podrían probablemente aproximadamente aproximado desconoce desconocido desconocida desconocidos incierto quizá quizás presumiblemente",
}


def norm(t: str) -> str:
    t = unicodedata.normalize("NFC", t).replace("µ", "u").replace("μ", "u").replace("−", "-").replace("–", "-")
    t = re.sub(r"(?<=\d)[    ](?=\d{3}\b)", "", t)
    t = re.sub(r"(?<=\d),(?=\d)", ".", t)
    t = re.sub(r"(\d)\s*" + PCT_WORDS + r"\b", r"\1%", t, flags=re.I)
    return t


def numeric_tokens(t: str) -> Counter:
    t = norm(t)
    out = Counter()
    for m in re.finditer(r"\b[pP]\s*([<>=≤≥])\s*(\d+(?:\.\d+)?)", t):
        out[f"p{m.group(1)}{m.group(2)}"] += 1
    t = re.sub(r"\b[pP]\s*[<>=≤≥]\s*\d+(?:\.\d+)?", " ", t)
    for m in re.finditer(r"(?<![\w.])([<>≤≥])(?![\w])", t):
        out["cmp" + m.group(1)] += 1
    for m in re.finditer(r"(?<![\w-])(-?)(\d+(?:\.\d+)?)(?!\d)(\s?" + UNITS + r"(?![A-Za-z]))?", re.sub(r"[A-Za-z_]+\d+[A-Za-z0-9_]*|\d+[A-Za-z_][A-Za-z0-9_]*", " ", t)):
        unit = (m.group(3) or "").strip()
        out[f"{m.group(1)}{m.group(2)}{('+' + unit) if unit else ''}"] += 1
    return out


def symbol_tokens(t: str) -> Counter:
    t = norm(t)
    out = Counter()
    for tok in re.findall(r"[A-Za-z0-9_]+", t):
        if "_" in tok and re.search(r"[A-Za-z]", tok):
            out[tok] += 1
        elif re.search(r"[A-Za-z]", tok) and re.search(r"\d", tok):
            out[tok] += 1
        else:
            for run in re.findall(r"[A-Z]{2,}", tok):
                out[run] += 1
    return out


def source_names(t: str) -> list:
    names, prev_boundary = [], True
    for m in re.finditer(r"[A-Za-z0-9_À-ÿ]+|[.:;?!]", t):
        w = m.group(0)
        if w in ".:;?!":
            prev_boundary = True
            continue
        if w[0].isupper() and not prev_boundary and not re.fullmatch(r"[A-Z]{2,}\d*", w) and not re.search(r"\d", w):
            names.append(w)
        prev_boundary = False
    return names


def cues(t: str, lang: str):
    w = re.findall(r"[a-zà-ÿ]+", t.lower())
    neg, hedge = set(NEG[lang].split()), set(HEDGE[lang].split())
    n = 0
    for i, x in enumerate(w):
        if x == "noch" and lang == "de":
            n += 1 if i and w[i - 1] == "weder" else 0
        elif x in neg:
            n += 1
    h = sum(x in hedge for x in w)
    if lang == "fr":
        h += sum(bool(re.search(r"(rait|raient)$", x)) and x not in hedge for x in w)
    if lang == "es":
        h += sum(bool(re.search(r"r(ía|ían)$", x)) and x not in hedge for x in w)
    return n, h


def diff(a: Counter, b: Counter) -> str:
    d = []
    for k in sorted(set(a) | set(b)):
        if a[k] != b[k]:
            d.append(f"{k}: source {a[k]} / rendering {b[k]}")
    return "; ".join(d)


def check_row(src: str, ren: str, lang: str) -> list:
    flags = []
    d = diff(numeric_tokens(src), numeric_tokens(ren))
    if d: flags.append("NUMBER " + d)
    d = diff(symbol_tokens(src), symbol_tokens(ren))
    if d: flags.append("SYMBOL " + d)
    low = norm(ren).lower()
    missing = [n for n in source_names(src) if n.lower() not in low]
    if missing: flags.append("NAME missing " + ", ".join(missing))
    sn, sh = cues(src, "en"); rn, rh = cues(ren, lang)
    if sn != rn: flags.append(f"NEGATION source {sn} / rendering {rn}")
    if sh != rh: flags.append(f"HEDGE source {sh} / rendering {rh}")
    return flags


def main(argv):
    sel = {str(o["n"]): o["text"] for o in json.load(open(argv[0], encoding="utf-8"))}
    tr = json.load(open(argv[1], encoding="utf-8"))
    langs = argv[argv.index("--lang") + 1].split(",") if "--lang" in argv else ["fr", "de", "es"]
    rows = flagged = 0
    for n in sorted(tr, key=int):
        for l in langs:
            rows += 1
            f = check_row(sel[n], tr[n][l], l)
            if f:
                flagged += 1
                print(f"{n}-{l.upper()} | " + " | ".join(f))
    print(f"ROWS {rows} FLAGGED {flagged}")


if __name__ == "__main__":
    main(sys.argv[1:])
