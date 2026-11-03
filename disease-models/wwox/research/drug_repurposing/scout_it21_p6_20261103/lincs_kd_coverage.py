#!/usr/bin/env python3
"""IT21 P6: which genes of a declared panel have an NPC (neural progenitor) shRNA knockdown signature in LINCS
LIB_6 (iLINCS, free, key-less)? Panel is public gene symbols fixed before the run. Census only: a signature in
the census is not a verified knockdown (non-landmark genes are not measured).

    python3 lincs_kd_coverage.py --help
    python3 lincs_kd_coverage.py
"""
import argparse
import json
import sys
import urllib.parse
import urllib.request

URL = "https://www.ilincs.org/api/SignatureMeta"
UA = {"User-Agent": "legend-scout/1.0 (research; no contact)"}
PANEL = ["WWOX", "HIF1A", "MTOR", "NFE2L2", "ATF4", "ERBB4", "TP73", "RUNX2", "GRIN2A", "GRIN2B", "KCNQ2", "SCN1A",
         "SCN2A", "SCN8A", "STXBP1", "CDKL5", "CACNA1G", "SLC2A1", "HK2", "LDHA", "PDK1", "BNIP3", "SLC12A2"]


def main():
    argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter).parse_args()
    flt = json.dumps({"where": {"cellline": "NPC", "libraryid": "LIB_6"}, "limit": 3000})
    req = urllib.request.Request(URL + "?filter=" + urllib.parse.quote(flt), headers=UA)
    rows = json.load(urllib.request.urlopen(req, timeout=120))
    genes = {r["compound"] for r in rows}
    print(f"NPC LIB_6 signatures {len(rows)}; distinct genes {len(genes)}")
    print("panel with NPC knockdown signature:", [g for g in PANEL if g in genes])
    print("panel without:", [g for g in PANEL if g not in genes])


if __name__ == "__main__":
    sys.exit(main())
