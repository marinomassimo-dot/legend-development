"""Build isoform_expression.tsv from the five derived tables (SCI44 A2). No network.
usage: python3 -I build_expression_table.py <derived_dir> <out_tsv>
"""
import sys
if "--help" in sys.argv or "-h" in sys.argv:
    print(__doc__)
    sys.exit(0)
import os
d, out = sys.argv[1:3]
HG = {"PDK1":"HGNC:8809","PDK2":"HGNC:8810","PDK3":"HGNC:8811","PDK4":"HGNC:8812","PDP1":"HGNC:9279","PDP2":"HGNC:30263","PDHA1":"HGNC:8806","PDHB":"HGNC:8808","DLAT":"HGNC:2896"}
GENES = list(HG)
HDR = ["row_id","gene","hgnc_id","cell_class","species","age_stage","region","measure","value","unit","preparation","biological_unit","n","source_pmid_or_doi","locator","input_sha256","script","producer_status","kind"]
rows = []
def add(**k):
    k["row_id"] = "IE%03d" % (len(rows) + 1)
    rows.append([k.get(h, "") for h in HDR])
def read(fn):
    with open(os.path.join(d, fn), encoding="utf-8") as f:
        h = f.readline().rstrip("\n").split("\t")
        return [dict(zip(h, l.rstrip("\n").split("\t"))) for l in f if l.strip()]
TAR14 = "4cb522fba1720a0a900511593a7ebb3ed8a6be5beeb14a7cf22d3824f99427d0"
# ---- Zhang 2014 mouse (GEO GSE52564 processed per-sample tables)
M = read("mouse_gse52564_extract.tsv")
mcls = {
 "Neuron":("cortical neurons (L1CAM-selected; excitatory and inhibitory not separable)","P7","immunopanning (negative panning, then L1CAM)"),
 "Astrocyte":("astrocytes","P7","FACS, Aldh1l1-EGFP"),
 "OPC":("oligodendrocyte precursor cells","P17","immunopanning (PDGFRA)"),
 "NFO":("newly formed oligodendrocytes","P17","immunopanning (GalC)"),
 "MO":("myelinating oligodendrocytes","P17","immunopanning (MOG)"),
 "Microglia":("microglia (CD45-selected; macrophage contamination minimised by perfusion)","not stated in the text read; same suspension as the P17 oligodendrocyte-lineage preparation (inference)","immunopanning (CD45)"),
 "Endothelial":("endothelial cells","P7","FACS, Tie2-EGFP"),
}
sym14 = {"PDK1":"Pdk1","PDK2":"Pdk2","PDK3":"Pdk3","PDK4":"Pdk4","PDP1":"Pdp1","PDP2":"Pdp2","PDHA1":"Pdha1","PDHB":"Pdhb","DLAT":"Dlat"}
for g in GENES:
    for key, (cls, age, prep) in mcls.items():
        recs = [r for r in M if r["gene"] == sym14[g] and r["file"].split("_")[1].rstrip("12.xlsg").rstrip(".") .startswith(key[:3]) and r["file"].split("_")[1].startswith(key)]
        assert len(recs) == 2, (g, key, len(recs))
        vals = [float(r["fpkm"]) for r in recs]
        files = ";".join(r["file"].replace(".xls.gz", "") for r in recs)
        add(gene=g, hgnc_id=HG[g], cell_class=cls, species="mouse (strain FVN/Swiss per GEO sample record)", age_stage=age, region="cerebral cortex", measure="RNA",
            value="%.2f" % (sum(vals)/2), unit="FPKM (Cufflinks, mean of 2 replicates)", preparation=prep + "; poly(A) RNA-seq, Illumina HiSeq 2000",
            biological_unit="animals pooled per replicate (3-12 mice per litter pool); replicate = one pool; cells inside a pool are not replicates",
            n="2 pools", source_pmid_or_doi="25186741", locator="GEO GSE52564 sheet 'UCSC Genes FPKM', row %s; replicates %s; %s" % (sym14[g], ";".join("%.2f" % v for v in vals), files),
            input_sha256=TAR14, script="scripts/extract_mouse_gse52564.py; scripts/build_expression_table.py", producer_status="read", kind="measured")
# ---- Zhang 2016 human (GSE73721)
H = read("human_gse73721_extract.tsv")
hcls = [
 ("astro_fetal_ctx","fetal astrocytes / astrocyte precursor cells (HEPACAM-selected)","human","fetal, 17-20 gestational weeks in the text; 18.0-18.5 in the Fig 4C legend","cerebral cortex (fetal)","6 patients","immunopanning (HepaCAM), shortened binding procedure for fetal samples"),
 ("astro_mature_ctx","mature astrocytes (HEPACAM-selected)","human","juvenile to adult, 8-63 years (per-column ages in locator)","temporal lobe cortex resected as normal (MRI, EEG, pathology) during epilepsy surgery","12 patients","immunopanning (HepaCAM)"),
 ("neuron_ctx","cortical neurons (Thy1-selected; subtype not resolved)","human","adult, 25 years","cortex (temporal lobe resection, normal)","1 patient","immunopanning (Thy1)"),
 ("oligo_ctx","oligodendrocytes (GalC and O4 panning described; maturation stage not resolved in the text read)","human","juvenile to adult, 22-63 years","cortex (temporal lobe resection, normal)","5 patients","immunopanning"),
 ("myeloid_ctx","microglia and macrophages (CD45-selected; not separable)","human","adult, 45-63 years","cortex (temporal lobe resection, normal)","3 patients","immunopanning"),
 ("endo_ctx","endothelial cells (BSL-1-selected)","human","13 and 47 years","cortex (temporal lobe resection, normal)","2 patients","immunopanning"),
 ("mouse_astro","astrocytes","mouse (strain not read)","1, 4, 7 and 9 months","cortex","4 batches","immunopanning (HepaCAM)"),
]
for g in GENES:
    for grp, cls, sp, age, reg, n, prep in hcls:
        r = [x for x in H if x["gene"] == g and x["group"] == grp]
        assert len(r) == 1, (g, grp)
        r = r[0]; vals = [float(v) for v in r["values"].split(";")]
        unit_bio = "patients (one sample per patient)" if sp == "human" else "batches of astrocytes, 3 mouse brains combined per batch"
        add(gene=g, hgnc_id=HG[g], cell_class=cls, species=sp, age_stage=age, region=reg, measure="RNA", value=r["mean_fpkm"],
            unit="FPKM (Cufflinks via Galaxy, mean over columns; table symbols are mouse-style capitalised)", preparation=prep + "; RNA-seq, Illumina NextSeq 150 bp paired-end",
            biological_unit=unit_bio + "; cells inside a sample are not replicates", n=n, source_pmid_or_doi="26687838",
            locator="GEO GSE73721 Human_and_mouse_table, row %s; %d columns, min %.2f max %.2f; values %s; columns %s" % (g.capitalize() if False else g, len(vals), min(vals), max(vals), r["values"], r["column_labels"]),
            input_sha256=r["input_sha256"], script="scripts/extract_human_gse73721.py; scripts/build_expression_table.py", producer_status="read", kind="measured")
# ---- HPA single-nuclei brain clusters (adult human)
N = read("hpa_snRNA_brain.tsv")
ncls = [
 ("upper-layer intratelencephalic","excitatory cortical neurons, upper-layer intratelencephalic cluster"),
 ("deep-layer intratelencephalic","excitatory cortical neurons, deep-layer intratelencephalic cluster"),
 ("deep-layer near-projecting","excitatory cortical neurons, deep-layer near-projecting cluster"),
 ("deep-layer corticothalamic and 6b","excitatory cortical neurons, deep-layer corticothalamic and 6b cluster"),
 ("MGE interneuron","inhibitory neurons, MGE interneuron cluster"),
 ("CGE interneuron","inhibitory neurons, CGE interneuron cluster"),
 ("LAMP5-LHX6 and Chandelier","inhibitory neurons, LAMP5-LHX6 and Chandelier cluster"),
 ("astrocyte","astrocytes"),
 ("oligodendrocyte precursor cell","oligodendrocyte precursor cells"),
 ("committed oligodendrocyte precursor","committed oligodendrocyte precursors (newly formed lineage stage)"),
 ("oligodendrocyte","oligodendrocytes"),
 ("central nervous system macrophage","microglia / CNS macrophages"),
 ("endothelial cell","endothelial cells"),
]
for g in GENES:
    for key, cls in ncls:
        r = [x for x in N if x["gene"] == g and x["cluster_type"] == key]
        assert len(r) == 1, (g, key)
        r = r[0]
        add(gene=g, hgnc_id=HG[g], cell_class=cls, species="human", age_stage="adult (donor ages not stated in the file or the pages opened)", region="brain-wide cluster type (region composition not given in the file; cortical cluster names are region-labelled by HPA)", measure="RNA",
            value=r["nCPM"], unit="nCPM (HPA normalised counts per million, cluster level)", preparation="single-nucleus RNA-seq, cluster-level aggregate in an HPA download; source dataset not opened",
            biological_unit="nuclei pooled into one HPA cluster across donors; nuclei are not donors and the donor number is not stated", n="not stated", source_pmid_or_doi="HPA download rna_single_nuclei_cluster_type.tsv (release file dated 2025-11-06)",
            locator="rna_single_nuclei_cluster_type.tsv, gene %s, cluster type '%s'" % (g, key), input_sha256=r["input_sha256"], script="scripts/extract_hpa.py; scripts/build_expression_table.py", producer_status="read", kind="copied")
# ---- HPA single cell type (aggregate across datasets)
C = read("hpa_scRNA_celltype.tsv")
ccls = [("brain excitatory neurons","excitatory neurons (brain)"),("brain inhibitory neurons","inhibitory neurons (brain)"),("astrocytes","astrocytes"),("oligodendrocyte progenitor cells","oligodendrocyte progenitor cells"),("oligodendrocytes","oligodendrocytes"),("microglia","microglia"),("vascular endothelial cells","vascular endothelial cells (all tissues pooled by HPA, not brain-specific)")]
for g in GENES:
    for key, cls in ccls:
        r = [x for x in C if x["gene"] == g and x["cell_type"] == key]
        assert len(r) == 1, (g, key)
        r = r[0]
        add(gene=g, hgnc_id=HG[g], cell_class=cls, species="human", age_stage="not stated (HPA aggregate)", region="not stated (HPA aggregate across source datasets)", measure="RNA",
            value=r["nCPM"], unit="nCPM (HPA normalised counts per million, cell-type level)", preparation="single-cell / single-nucleus RNA-seq aggregate in an HPA download; source datasets not opened",
            biological_unit="cells or nuclei pooled by HPA into one cell type across datasets; not donors", n="not stated", source_pmid_or_doi="HPA download rna_single_cell_type.tsv (release file dated 2025-12-12)",
            locator="rna_single_cell_type.tsv, gene %s, cell type '%s'" % (g, key), input_sha256=r["input_sha256"], script="scripts/extract_hpa.py; scripts/build_expression_table.py", producer_status="read", kind="copied")
# ---- HPA IHC protein, cerebral cortex and hippocampus
I = read("hpa_ihc_brain.tsv")
for g in GENES:
    for r in [x for x in I if x["gene"] == g]:
        add(gene=g, hgnc_id=HG[g], cell_class="%s (IHC compartment label)" % r["cell_type"], species="human", age_stage="not stated in the file", region=r["tissue"], measure="protein",
            value=r["level"], unit="IHC staining category (Not detected / Low / Medium / High), ordinal, not an amount", preparation="immunohistochemistry on normal tissue, HPA; antibody reliability '%s'" % r["reliability"],
            biological_unit="normal-tissue donors (number and ages not stated in the file); compartment label, not a sorted cell population", n="not stated", source_pmid_or_doi="HPA download normal_ihc_data.tsv",
            locator="normal_ihc_data.tsv, gene %s, tissue %s, cell type '%s'; reliability %s" % (g, r["tissue"], r["cell_type"], r["reliability"]), input_sha256=r["input_sha256"], script="scripts/extract_hpa.py; scripts/build_expression_table.py", producer_status="read", kind="copied")
with open(out, "w", encoding="utf-8") as f:
    f.write("\t".join(HDR) + "\n")
    for r in rows:
        assert len(r) == len(HDR) and not any(("\t" in c or "\n" in c) for c in r), r
        f.write("\t".join(r) + "\n")
print(len(rows), "rows")
