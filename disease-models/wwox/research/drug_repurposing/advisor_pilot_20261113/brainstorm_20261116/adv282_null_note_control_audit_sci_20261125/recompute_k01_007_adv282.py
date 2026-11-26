import gzip,re,math,statistics as st
D="/home/desktop/legend-development/files/"
g={}
with gzip.open(D+"reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz","rt") as h:
    for l in h:
        if l[0]==">":
            m=re.match(r">(ENSMUST\d+)\.\d+ .*gene:(ENSMUSG\d+)\.\d+ .*gene_symbol:(\S+)",l)
            if m: g[m.group(1)]=m.group(3)
C=[("H_S","GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz",["S_KO_1","S_KO_2","S_KO_3"],["S_Ctrl_1","S_Ctrl_2"]),
("H_N","GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz",["N_KO_1","N_KO_2"],["N_Ctrl_1","N_Ctrl_2"]),
("H_germ","GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz",["KO_1","KO_2"],["WT_1","WT_2","WT_3"]),
("Cx_S","GSE158682/GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz",["CRTX_S_KO_1","CRTX_S_KO_2","CRTX_S_KO_3"],["CRTX_S_Ctrl_1","CRTX_S_Ctrl_2","CRTX_S_Ctrl_3","CRTX_S_Ctrl_4"])]
genes=["Wwox","Hif1a","Epas1","Hk2","Slc2a1","Ldha","Pgk1","Ndrg1","P4ha1","Gfap"]
for name,f,ko,ct in C:
    with gzip.open(D+"geo/"+f,"rt") as h:
        hdr=h.readline().rstrip("\n").split("\t"); idx={c:i for i,c in enumerate(hdr)}
        acc={s:{} for s in genes}
        for l in h:
            p=l.rstrip("\n").split("\t"); s=g.get(p[0].split(".")[0])
            if s in acc:
                for c in ko+ct: acc[s][c]=acc[s].get(c,0)+float(p[idx[c]])
    out=[]
    for s in genes:
        k=st.mean(acc[s][c] for c in ko); c_=st.mean(acc[s][c] for c in ct)
        out.append(f"{s} {math.log2((k+0.01)/(c_+0.01)):+.2f}")
    print(name,"|"," ".join(out))
