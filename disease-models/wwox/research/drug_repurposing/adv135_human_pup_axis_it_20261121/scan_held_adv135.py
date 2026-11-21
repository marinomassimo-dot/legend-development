"""ADV-135 counted scan of held material (IT, 2026-11-21). A scan hit is a prompt to read, never a finding.
Usage: python3 -I scan_held_adv135.py <out_dir> <dossier_dir> <fulltext_dir>
Reads text only (md, txt, xml/html with tags removed, pdf through pdftotext); writes counts.tsv and sentences.tsv.
A source is 'human-spectrum' when it names WWOX and one of WOREE, SCAR12, or a human-case word, as a mention in text."""
import os, re, sys, csv, subprocess, html, hashlib

ANALYTES = {
    "calcium": r"\b(hypo|hyper)?calc(a)?emi\w*|\bcalcium\b|\bCa2\+|\bionised calcium|\bionized calcium|\bparathyroid\w*|\bPTH\b|\bvitamin D\b",
    "phosphate": r"\bphosphate\b|\bphosphorus\b|\bhypophosphat\w*|\bhyperphosphat\w*",
    "glucose": r"\bhypoglyc\w*|\bhyperglyc\w*|\bglycem\w*|\bglucose\b|\bblood sugar\b",
    "lipids": r"\blipid\w*|\bcholesterol\b|\btriglycerid\w*|\bHDL\b|\bLDL\b|\bdyslipid\w*|\bApoA",
    "cortisol_adrenal": r"\bcortisol\b|\badrenal\w*|\bACTH\b|\bcorticosteroid\w*|\bcorticosterone\b",
    "thyroid": r"\bthyroid\w*|\bTSH\b|\bhypothyroid\w*|\bfT4\b|\bthyroxine\b",
    "gh_igf1": r"\bgrowth hormone\b|\bIGF-?1\b|\bsomatomedin\w*|\bGH deficiency\b",
    "metabolic_workup": r"\bmetabolic (work-?up|screen\w*|investigation\w*|disorder\w*|test\w*|evaluation)\b|\binborn errors?\b|\bamino acids?\b|\borganic acids?\b|\bacylcarnitine\w*|\bcarnitine\b|\blactate\b|\bammonia\b|\bpterin\w*|\bneurotransmitter\w*",
    "lab_general": r"\blaborator\w*|\bbiochemical\w*|\bserum\b|\bblood (test|count|chemistr\w*)\w*|\bwithin normal limits\b",
    "failure_to_thrive": r"\bfailure to thrive\b|\bpoor weight gain\b|\bgrowth retardation\b|\bfeeding (difficult\w*|problem\w*)\b",
}
CASE_WORDS = r"\b(patients?|probands?|individuals?|child(ren)?|infants?|neonat\w*|newborn|proband|cases?|siblings?|boys?|girls?)\b"
HUMAN_SPEC = r"\bWOREE\b|\bSCAR12\b|\bWWOX[- ]related\b|\bdevelopmental and epileptic encephalopath\w*"

def read_text(path):
    low = path.lower()
    try:
        if low.endswith((".md", ".txt", ".tsv", ".csv")):
            return open(path, encoding="utf-8", errors="replace").read()
        if low.endswith((".xml", ".html", ".htm")):
            t = open(path, encoding="utf-8", errors="replace").read()
            t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S | re.I)
            t = re.sub(r"<[^>]+>", " ", t)
            return html.unescape(re.sub(r"\s+", " ", t))
        if low.endswith(".pdf"):
            r = subprocess.run(["pdftotext", "-q", "-layout", path, "-"], capture_output=True, timeout=120)
            return r.stdout.decode("utf-8", errors="replace")
    except Exception as e:
        return ""
    return ""

EMAIL_RX = re.compile(r"[\w.+-]+@[\w-]+(\.[\w-]+)+")

def redact(s):
    """Public-release hygiene: author contact addresses are removed from listed sentences; a sentence naming both parental
    sides is withheld (the listing is a prompt to read the source, never a finding)."""
    s = EMAIL_RX.sub("[address removed]", s)
    if re.search(r"\bmaternal\b", s, re.I) and re.search(r"\bpaternal\b", s, re.I):
        return "[sentence withheld in the listing: see the source]"
    return s

def pmid_of(path):
    m = re.search(r"PMID[_-]?(\d{6,9})", path, re.I)
    return m.group(1) if m else ""

def sentences(t):
    t = re.sub(r"\s+", " ", t)
    return re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\[(])", t)

def main():
    out, dos, ft = sys.argv[1:4]
    os.makedirs(out, exist_ok=True)
    files = []
    for root in (dos, ft):
        for dp, dn, fn in os.walk(root):
            for f in fn:
                if f.lower().endswith((".md", ".txt", ".xml", ".html", ".htm", ".pdf")):
                    files.append((root, os.path.join(dp, f)))
    files.sort(key=lambda x: x[1])
    with open(os.path.join(out, "counts.tsv"), "w", newline="", encoding="utf-8") as cf, \
         open(os.path.join(out, "sentences.tsv"), "w", newline="", encoding="utf-8") as sf:
        cw = csv.writer(cf, delimiter="\t"); sw = csv.writer(sf, delimiter="\t")
        cw.writerow(["kind", "path", "pmid", "bytes", "wwox", "human_spec", "case_words"] + list(ANALYTES))
        sw.writerow(["path", "pmid", "analyte", "sentence"])
        for root, p in files:
            t = read_text(p)
            if not t:
                continue
            wwox = len(re.findall(r"\bWWOX\b|\bWwox\b", t))
            if wwox == 0:
                continue
            hs = len(re.findall(HUMAN_SPEC, t, re.I)); cwn = len(re.findall(CASE_WORDS, t, re.I))
            counts = {k: len(re.findall(rx, t, re.I)) for k, rx in ANALYTES.items()}
            kind = "dossier" if root == dos else "fulltext"
            cw.writerow([kind, os.path.relpath(p, root), pmid_of(p), len(t), wwox, hs, cwn] + [counts[k] for k in ANALYTES])
            if hs or cwn >= 5:
                for s in sentences(t):
                    if len(s) > 1500:
                        s = s[:1500]
                    for k, rx in ANALYTES.items():
                        if k in ("lab_general",):
                            continue
                        if re.search(rx, s, re.I) and re.search(CASE_WORDS + "|" + HUMAN_SPEC, s, re.I):
                            sw.writerow([os.path.relpath(p, root), pmid_of(p), k, redact(s.strip())])
                            break
if __name__ == "__main__":
    main()
