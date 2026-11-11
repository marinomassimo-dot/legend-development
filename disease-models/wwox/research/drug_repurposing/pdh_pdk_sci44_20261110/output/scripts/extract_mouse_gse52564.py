"""Extract gene rows from the per-sample GEO xls.gz files of GSE52564 (Zhang 2014 mouse cortex RNA-seq). usage: python3 -I extract_mouse_gse52564.py <raw_dir> <xlrd_dir> <out_tsv>
No network. Reads local files given as arguments.
"""
import sys
if "--help" in sys.argv or "-h" in sys.argv:
    print(__doc__)
    sys.exit(0)
import sys, os, gzip, hashlib, io
raw, xdir, out = sys.argv[1:4]
sys.path.insert(0, xdir)
import xlrd
genes = ["Pdk1","Pdk2","Pdk3","Pdk4","Pdp1","Pdp2","Pdha1","Pdhb","Dlat","Pdpr","Pdhx","Dld","Pdk","Ldha","Slc16a1","Mpc1","Mpc2","Gfap","Rbfox3","Snap25","Aif1","Cx3cr1","Pecam1","Mbp","Pdgfra","Aldh1l1","Slc17a7","Gad1"]
rows = []
for fn in sorted(os.listdir(raw)):
    if not fn.endswith(".xls.gz"): continue
    p = os.path.join(raw, fn)
    data = gzip.open(p).read()
    sha = hashlib.sha256(open(p, "rb").read()).hexdigest()
    wb = xlrd.open_workbook(file_contents=data)
    sh = wb.sheet_by_name("UCSC Genes FPKM") if "UCSC Genes FPKM" in wb.sheet_names() else wb.sheet_by_index(0)
    hdr = [str(c) for c in sh.row_values(0)]
    for r in range(1, sh.nrows):
        v = sh.row_values(r)
        if str(v[0]) in genes:
            rows.append([fn, sha, str(v[0]), str(v[1]), ";".join(hdr[:3])])
with open(out, "w") as f:
    f.write("file\tfile_sha256\tgene\tfpkm\theader_first3\n")
    for r in rows:
        f.write("\t".join(r) + "\n")
print(len(rows), "rows;", "sheets:", wb.sheet_names(), "header:", hdr)
