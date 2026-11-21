"""Re-check the claims of README.md against the held bytes of the two item-5 pages (IT49-Q11 and IT55-Q02), IT 2026-11-21.
The files are NOT stored in the repository. Fetch each once (one request per URL) into an empty directory D:
  https://pmc-oa-opendata.s3.amazonaws.com/PMC12434521.1/ml5c00297_si_001.pdf                         -> D/si49.pdf
  https://pmc-oa-opendata.s3.amazonaws.com/PMC4528969.1/NIHMS665856-supplement-supp_table_2.xlsx     -> D/s2.xlsx
  https://pmc-oa-opendata.s3.amazonaws.com/PMC4528969.1/NIHMS665856-supplement-supp_table_3.xlsx     -> D/s3.xlsx
  https://pmc-oa-opendata.s3.amazonaws.com/PMC4528969.1/NIHMS665856-supplement-Table_S1.pdf          -> D/s1.pdf
  https://pmc-oa-opendata.s3.amazonaws.com/PMC4528969.1/NIHMS665856-supplement-1.docx                -> D/d.docx
  https://pmc-oa-opendata.s3.amazonaws.com/PMC4528969.1/PMC4528969.1.txt                              -> D/m55.txt
Run:  python3 -I verify_held_bytes.py D      (needs pdftotext on the path)"""
import hashlib
import re
import subprocess
import sys
import zipfile
from pathlib import Path

D = Path(sys.argv[1])
SHA = {
    "si49.pdf": "1c6b39d36eb7ea62af8b04e372b8d2c30b77e4a644b4674e15db0f97e645e1e4",
    "s2.xlsx": "bc97c11220172ae838afc5a0e67ac9b8feb6c18cd9621625adbace06bb64e802",
    "s3.xlsx": "fd46c68b1e2397b290710bd390cad923aab45341ec0abf5cc457681bb1e52192",
    "s1.pdf": "9655b114237e7ff7dd6f47be69e02f90fab343167bb10af3baf26da9932f2a08",
    "d.docx": "4c08ccede571f1ada88715a4c55a9c56d5074b8611497a4db9c6327ab343e466",
    "m55.txt": "e89ba3a9095673fd5032e827d0a04cb70754d9dd0c733ed35154d38df2e0f132",
}
bad = 0
for n, h in SHA.items():
    got = hashlib.sha256((D / n).read_bytes()).hexdigest()
    ok = got == h
    bad += not ok
    print("SHA", "OK " if ok else "DIFF", n)


def pdf_text(p):
    return re.sub(r"\s+", " ", subprocess.run(["pdftotext", "-layout", str(p), "-"], capture_output=True, text=True).stdout)


si = pdf_text(D / "si49.pdf")
checks = [
    ("SI Table S2 5s row", "5s 5.9 (101) 0.35 (100) 2.1 fold 2.5 fold" in si),
    ("SI MPC pH and temperature", "room temperature" in si and "pH 7.35" in si),
    ("SI names no hERG, Kir6, Kir7.1, Kir2.4 or K2P data for 5s (reference list excepted)", not re.search(r"hERG|Kir7\.1|Kir2\.4|K2P|TREK|TASK", si)),
    ("SI Kir1.1 and Kir4.1 only 'as previously described'", "Tl+ flux assays for Kir1.1 and Kir4.1 were conducted as previously described" in si),
]
docx = re.sub(r"<[^>]+>", " ", zipfile.ZipFile(D / "d.docx").read("word/document.xml").decode("utf8"))
docx = re.sub(r"\s+", " ", docx)
m = re.sub(r"\s+", " ", (D / "m55.txt").read_text(encoding="utf-8"))
s1 = pdf_text(D / "s1.pdf")
checks += [
    ("docx index: Table S1 + western scans, Table 2 kinase, Table 3 phosphoproteomics", "Supplementary Table 1 and Supplementary Figures 1 and 2" in docx and "Supplementary Table 2 (kinase assay results)" in docx and "Supplementary Table 3" in docx),
    ("Table S1 pdf is the blood-brain-barrier table", "Miconazole and clobetasol cross the blood brain barrier" in s1 and not re.search(r"ketoconazole|liothyronine|MBP", s1.split("Supplementary Figure 1")[0])),
    ("main text: ketoconazole named once, in the slice-culture drug list; liothyronine absent", len(re.findall("ketoconazole", m, re.I)) == 1 and "liothyronine" not in m.lower()),
    ("main text: Extended Data Fig. 2a is cited for the slice ranking", "Fig. 1d and Extended Data Fig. 2a" in m),
]


def xl_first_col(p):
    z = zipfile.ZipFile(p)
    ss = re.findall(r"<t[^>]*>([^<]*)</t>", z.read("xl/sharedStrings.xml").decode("utf8"))
    return set(ss)


a = xl_first_col(D / "s2.xlsx") | xl_first_col(D / "s3.xlsx")
checks.append(("xlsx tables name clobetasol and miconazole only (no ketoconazole, liothyronine, differentiation column)",
               {"Clobetasol", "Miconazole"} <= a and not any(re.search(r"ketoconazole|liothyronine|\bMBP\b", x, re.I) for x in a)))
for name, ok in checks:
    bad += not ok
    print("CHECK", "OK  " if ok else "FAIL", name)
sys.exit(1 if bad else 0)
