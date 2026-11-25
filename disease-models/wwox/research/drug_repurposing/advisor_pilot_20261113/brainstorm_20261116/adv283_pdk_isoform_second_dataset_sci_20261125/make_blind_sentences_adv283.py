#!/usr/bin/env python3
"""Build the blind-reader sentence file for ADV-283 from pdk_second_dataset_adv283.tsv (nothing retyped).
Usage (python3 -I -P -E): make_blind_sentences_adv283.py <tsv> <out.md>"""
import csv, sys
rows = list(csv.DictReader(open(sys.argv[1]), delimiter="\t"))
def get(ds, comp, gene):
    for r in rows:
        if r["dataset"].startswith(ds) and r["comparison"].startswith(comp) and r["gene"] == gene:
            return r
    raise KeyError((ds, comp, gene))
def arm(r):
    return f"{r['deficient_libraries_TPM']} against {r['control_libraries_TPM']} TPM, n {r['n_deficient_v_control'].replace(' v ', ' against ')}"
k3, k1 = get("D2", "KO v WT", "Pdk3"), get("D2", "KO v WT", "Pdk1")
s3, s1 = get("D2", "S KO", "Pdk3"), get("D2", "S KO", "Pdk1")
c3, c1 = get("D3", "S KO", "Pdk3"), get("D3", "S KO", "Pdk1")
n3 = get("D2", "N KO", "Pdk3")
h = [get("D4", "hNSC", "Pdk3"), get("D4", "neurons", "Pdk3"), get("D4", "hNSC", "Pdk1"), get("D4", "neurons", "Pdk1")]
cc3, ck3 = get("D5", "ctrl", "Pdk3"), get("D5", "ko", "Pdk3")
S = []
S.append(("S1", "In two held mouse datasets from one study (GSE158681 hippocampus and GSE158682 cortex, postnatal day 17, transcript TPM summed to gene) Pdk3 is not higher in the Wwox-deficient arm. "
 f"Hippocampus, global null KO against wild type: Pdk3 ratio of arm means {k3['ratio']} ({arm(k3)}), every knockout library below every wild-type library. "
 f"Hippocampus, neuron-targeted (Synapsin-Cre) KO against control: Pdk3 {s3['ratio']} ({arm(s3)}). Nestin-Cre arm: Pdk3 {n3['ratio']} ({arm(n3)}). "
 f"Cortex, neuron-targeted KO against control: Pdk3 {c3['ratio']} ({arm(c3)}). The anchor's higher Pdk3 (1.55 times in human organoids, 4 knockout libraries against 2 wild-type) is therefore a single-deposit observation."))
S.append(("S2", f"Pdk1 is lower (ratio 0.83 or less with every deficient library below every control library) only in the neuron-targeted hippocampal arm ({s1['ratio']}; {arm(s1)}); it is not lower in the global null hippocampus ({k1['ratio']}; {arm(k1)}), the nestin-Cre arm, or the cortex ({c1['ratio']}; {arm(c1)}). The isoform pattern PDK3 higher with PDK1 lower is therefore not seen together in any primary comparison."))
S.append(("S3", f"In the human neural stem cell and neuron CAGE deposit GSE126075 (one sample per arm, no replicate, merged TPM by gene symbol), PDK3 is lower with WWOX depletion in both cell types (hNSC {h[0]['ratio']}, neurons {h[1]['ratio']}) and PDK1 is lower in both (hNSC {h[2]['ratio']}, neurons {h[3]['ratio']}); with n of 1 per arm this is descriptive and is not counted toward support or failure."))
S.append(("S4", f"In the mouse hippocampal snRNA-seq deposit GSE158684 (one control and one knockout library, no cell-class labels held) Pdk3 is detected in both libraries (control: {cc3['mean_TPM_deficient_or_total_UMI']} UMI in {cc3['mean_TPM_control_or_nuclei_nonzero']} of {cc3['n_deficient_v_control'].split(', ')[1]}; knockout: {ck3['mean_TPM_deficient_or_total_UMI']} UMI in {ck3['mean_TPM_control_or_nuclei_nonzero']} of {ck3['n_deficient_v_control'].split(', ')[1]}); this is a coverage statement and no direction is claimed."))
S.append(("S5", "One 2017 document (CHEMBL4007440; ELISA, full-length His6-PDHA1 substrate, 30 minutes) gives dichloroacetate IC50 PDK1 1.03 mM, PDK2 0.50 mM, PDK3 5.56 mM in one assay. Because PDK3 is the isoform least inhibited in that assay and is not higher in the two held mouse Wwox-deficient tissues, the sheet is not read with PDK3 as the relevant target in this genotype class on this evidence."))
with open(sys.argv[2], "w") as o:
    o.write("# Blind sentences, ADV-283 (verbatim repository sentences built by script; verdicts MUST CHANGE / ADD / STANDS; do not assume right or wrong)\n\n")
    o.write("Held sources for S1 and S2: /home/desktop/legend-development/files/geo/GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz ; /home/desktop/legend-development/files/geo/GSE158682/GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz ; transcript to gene mapping: /home/desktop/legend-development/files/reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz (headers). The deposits state no paper; the paper the repository links them to is PMID 33914858 (Repudi 2021, files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.txt) by identical n per arm.\n")
    o.write("Held sources for S3: /home/desktop/legend-development/files/geo/GSE126075/GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz and gse126075_soft_full.txt (same folder).\n")
    o.write("Held sources for S4: /home/desktop/legend-development/files/geo/GSE158684/ (the six GSE158684_ctrl_ and GSE158684_ko_ filtered files).\n")
    o.write("Held source for S5 (read only the lines on dichloroacetate and PDK isozymes): disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/adv098_agent_sheets_he_20261119/BATCH8_broad_ISRIB_trazodone_omaveloxolone_dichloroacetate_HE_20261120.md under /home/desktop/legend-development/.claude/worktrees/sci_am_20261125/ ; the anchor deposit for the 1.55 times in S1 is files/geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz (counts, one library per column cko1-4, cwt1-2).\n\n")
    for k, t in S:
        o.write(f"## {k}\n\n{t}\n\n")
