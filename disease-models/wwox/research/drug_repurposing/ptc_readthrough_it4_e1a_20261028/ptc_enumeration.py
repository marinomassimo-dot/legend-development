#!/usr/bin/env python3
"""Enumerate the single-nucleotide WWOX nonsense alleles in the committed ClinVar snapshot.

Offline and deterministic. For each allele: stop-codon identity, the +4 nucleotide, the original codon and
amino acid, the codon position of the substitution, whether the original amino acid is among the residues
that ataluren/aminoglycoside read-through is reported to insert at that stop (Roy 2016, PMID 27702906:
Gln/Lys/Tyr at UAA or UAG, Trp/Arg/Cys at UGA, mispairing at codon positions 1 and 3), the protein
domain hit, and the position relative to the last exon-exon junction (50-55 nt rule).
A PREDICTION from sequence only; nothing here is a measurement of NMD or of read-through.

  python3 -I ptc_enumeration.py --gb input_NM_016373.4.gb --clinvar ../../../analysis/data/WWOX_clinvar_all_variants.csv --out ptc_alleles.tsv
"""
import argparse, csv, hashlib, re

EXONS = [(1,232),(233,297),(298,355),(356,534),(535,641),(642,730),(731,916),(917,1181),(1182,2241)]
CDS_START = 126            # transcript coordinate of c.1 (NM_016373.4 CDS 126..1370)
LAST_JUNCTION_C = 1056     # last c. nucleotide of exon 8 (= transcript 1181 - 125)
OBSERVED = {"UAA": set("QKY"), "UAG": set("QKY"), "UGA": set("WRC")}   # PMID 27702906 abstract
B = "TCAG"; AA = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODON = {x+y+z: AA[16*i+4*j+k] for i,x in enumerate(B) for j,y in enumerate(B) for k,z in enumerate(B)}

def domain(p):   # UniProt Q9NZC7 (features read 2026-10-28): WW1 16-49, WW2 57-90, NLS 50-55, SDR region 125-414, active site Y293
    if 16 <= p <= 49: return "WW1"
    if 57 <= p <= 90: return "WW2"
    if p < 125: return "N-terminal/linker"
    return "region 125-414, before Y293" if p <= 293 else "region 125-414, after Y293"

def nmd_class(last_stop_nt):
    d = LAST_JUNCTION_C - last_stop_nt      # nt between end of the stop codon and the last junction
    if d > 55: return d, "NMD-predicted"
    if d >= 50: return d, "borderline-50-55nt"
    return d, "NMD-escape-predicted"

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--gb"); ap.add_argument("--clinvar"); ap.add_argument("--out")
    a = ap.parse_args()
    gb = open(a.gb).read()
    seq = re.sub(r"[^acgt]", "", gb.split("ORIGIN")[1].split("//")[0]).upper(); assert len(seq) == 2241
    cds = seq[CDS_START-1:1370]; assert cds[:3] == "ATG" and cds[-3:] in ("TAA","TAG","TGA")
    rows = []
    for x in csv.DictReader(open(a.clinvar)):
        m = re.fullmatch(r"p\.([A-Za-z]{3})(\d+)Ter", x["protein"]); mc = re.fullmatch(r"c\.(\d+)([ACGT])>([ACGT])", x["cdna"])
        if not (m and mc) or m.group(1) == "Ter": continue
        pos, cp = int(m.group(2)), int(mc.group(1)); cod = (pos-1)*3; ref = cds[cod:cod+3]
        assert cod <= cp-1 < cod+3 and cds[cp-1] == mc.group(2), x["cdna"]
        mut = list(ref); mut[cp-1-cod] = mc.group(3); mut = "".join(mut); assert mut in ("TAA","TAG","TGA"), x["cdna"]
        stop = mut.replace("T","U"); mm = cp-cod
        d, nmd = nmd_class(cod+3)
        ex = next(i for i,(s,e) in enumerate(EXONS,1) if s <= CDS_START-1+cp <= e)
        wt = CODON[ref]
        rows.append(dict(cdna=x["cdna"], protein=x["protein"], clinvar=x["accession"], classification=x["classification"],
            review=x["review_status"], exon=ex, wt_codon=ref, wt_aa=wt, stop=stop, plus4=cds[cod+3].replace("T","U"),
            context=stop+"-"+cds[cod+3].replace("T","U"), mismatch_codon_pos=mm, nt_to_last_junction=d, nmd_prediction=nmd,
            domain=domain(pos), wt_aa_in_reported_insertion_set=wt in OBSERVED[stop],
            wt_restoring_plausible=(wt in OBSERVED[stop]) and mm in (1,3)))
    rows.sort(key=lambda r: int(re.search(r"\d+", r["cdna"]).group()))
    with open(a.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t"); w.writeheader(); w.writerows(rows)
    from collections import Counter
    print("alleles", len(rows), dict(Counter(r["nmd_prediction"] for r in rows)))
    print("contexts", dict(Counter(r["context"] for r in rows)))
    print("wt_restoring_plausible", sum(r["wt_restoring_plausible"] for r in rows))
    print("gb sha256", hashlib.sha256(open(a.gb,"rb").read()).hexdigest())

if __name__ == "__main__": main()
