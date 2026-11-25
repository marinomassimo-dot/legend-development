# Print-only helper (ADV-240): lists WWOX lines per supplement file (xlsx, csv, docx, doc/xls via strings, zip members). Run: python3 -I scan_supplements_adv240.py inside a folder of downloaded supplements named <pmid>_<pmcid>/. Writes nothing.
import zipfile,re,os,sys,csv,subprocess,glob
def xlsx_rows(f):
    z=zipfile.ZipFile(f)
    ss=re.findall(r"<si>(.*?)</si>",z.read("xl/sharedStrings.xml").decode("utf8","replace"),re.S) if "xl/sharedStrings.xml" in z.namelist() else []
    ss=[re.sub(r"<[^>]+>","",s) for s in ss]
    wb=z.read("xl/workbook.xml").decode(); names=re.findall(r'<sheet [^>]*name="([^"]+)"',wb)
    out={}
    for i,n in enumerate(sorted([x for x in z.namelist() if x.startswith("xl/worksheets/sheet")],key=lambda s:int(re.findall(r"\d+",s)[0]))):
        d=z.read(n).decode("utf8","replace"); rows=[]
        for r in re.findall(r"<row[^>]*>(.*?)</row>",d,re.S):
            cells=[]
            for c in re.findall(r"<c ([^>]*?)(?:/>|>(.*?)</c>)",r,re.S):
                at,body=c; v=re.search(r"<v>(.*?)</v>",body or "",re.S); isv=re.search(r"<is>.*?<t[^>]*>(.*?)</t>",body or "",re.S)
                if 't="s"' in at and v: cells.append(ss[int(v.group(1))])
                elif isv: cells.append(isv.group(1))
                elif v: cells.append(v.group(1))
                else: cells.append("")
            rows.append(cells)
        out[names[i] if i<len(names) else n]=rows
    return out
def docx_text(f):
    z=zipfile.ZipFile(f); d=z.read("word/document.xml").decode("utf8","replace")
    d=re.sub(r"</w:tc>","\t",d); d=re.sub(r"</w:tr>|</w:p>","\n",d)
    return re.sub(r"<[^>]+>","",d)
def scan(path):
    ext=path.lower().rsplit(".",1)[-1]
    lines=[]
    if ext=="xlsx":
        for sh,rows in xlsx_rows(path).items():
            for i,r in enumerate(rows): lines.append((sh,i,"\t".join(r)))
    elif ext in("csv","tsv"):
        for i,l in enumerate(open(path,encoding="utf8",errors="replace")): lines.append(("csv",i,l.rstrip("\n")))
    elif ext=="docx":
        for i,l in enumerate(docx_text(path).split("\n")): lines.append(("docx",i,l))
    elif ext in("doc","xls"):
        s=subprocess.run(["strings","-n","3",path],capture_output=True,text=True).stdout
        for i,l in enumerate(s.split("\n")): lines.append((ext,i,l))
    elif ext=="zip":
        z=zipfile.ZipFile(path)
        for n in z.namelist(): lines.append(("zip-member",0,n))
    return lines
if __name__=="__main__":
    for d in sorted(glob.glob("[0-9]*_PMC*")):
        for f in sorted(glob.glob(d+"/*")):
            if f.endswith(".py"): continue
            L=scan(f); hits=[x for x in L if re.search(r"WWOX",x[2],re.I)]
            print(f, "lines",len(L),"WWOX",len(hits))
            for h in hits[:6]: print("   ",h[0],h[1],h[2][:260].replace("\t"," | "))
