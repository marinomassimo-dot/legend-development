#!/usr/bin/env python3
"""Build and check the IT7-P1 typed WWOX subnetwork (stdlib only, deterministic, offline).

Usage:
  subnetwork.py --help       print this text and exit (no work)
  subnetwork.py build        regenerate systems/evidence/nodes/observations/edges .tsv in this directory from the repository sources
  subnetwork.py check        validate the committed tables (exit 0 = clean, 1 = problems listed)

What `check` verifies (nothing is trusted from the tables themselves):
  * every file is rectangular, has one header, no blank or trailing-note lines; ids are unique;
  * node identities match their pattern (HGNC:n, ENSG/ENSMUSG, UniProt, MGI:n, CHEMBL, GO/CHEBI); human genes agree with the HGNC
    complete set when --hgnc <json> is given (optional; skipped and reported otherwise);
  * edge types, sign vocabulary, source states and readout levels are inside their closed vocabularies; every edge/observation
    resolves to a node, a system and evidence; a `measured` edge points at observation rows of the same node and system;
  * every numeric observation is re-read from its source file row and its sign is recomputed (|R| >= 0.25 for a gene, outside the
    matched null for a set); every manifest/document/tsv_row evidence anchor is found in its file;
  * node sign columns and the human_concordance rule are recomputed from the observations; edge direction_status and counter
    evidence are recomputed;
  * the firewall: no compound, signature-reversal or compound-response vocabulary appears in any table.
"""
import csv, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
DR = os.path.relpath(os.path.join(HERE, ".."), ROOT)          # drug_repurposing directory, repo-relative
THR = 0.25                                                      # descriptive bin for a per-gene centred log2 ratio, not a test

FILES = ["systems.tsv", "evidence.tsv", "nodes.tsv", "observations.tsv", "edges.tsv"]
SIGNS = ["up", "down", "no_change", "mixed", "UNKNOWN"]
EDGE_TYPES = ["measured", "inferred", "hypothesised", "association"]
READOUTS = ["transcript", "protein", "activity", "flux", "metabolite", "functional", "set_transcript", "none"]
NODE_TYPES = ["gene", "set", "process", "metabolite", "perturbation"]
EVID_KINDS = ["manifest", "document", "tsv_row", "pubmed_abstract", "geo_record"]
ROLES = ["perturbation", "signature_candidate", "network_context", "positive_control", "process_readout"]
FORBIDDEN = ["lincs", "l1000", "sigcom", "reverser", "dichloroacetate", "vigabatrin", "lithium", "memantine", "phenylbutyrate", "bumetanide",
             "apinocaltamide", "amlexanox", "oxamate", "metformin", "rapamycin", "compound", "inhibitor", "agonist", "antagonist",
             "q230p", "c.1057-2a>g"]

SYSTEMS = [  # id, role, species, model, perturbation, tissue, stage, n, unit, platform, accession, pmid, reuse, time
    ("organoid_ko_w15", "training_human", "human", "cerebral organoid, WWOX knockout", "WWOX exon-deletion knockout versus wild type",
     "bulk organoid RNA", "culture week 15", "4 knockout v 2 wild-type libraries", "library (differentiation batch not stated; UNVERIFIED)",
     "RNA-seq counts", "GSE156243", "34268881", "GEO public; no licence text in the record; only derived summaries are committed", "single time point"),
    ("hnpc_shwwox_cage", "training_human", "human", "H9-derived neural progenitors, lentiviral shRNA", "WWOX knockdown (depth not shown in CAGE tags) versus control arm",
     "2D clonal progenitor line", "undifferentiated progenitor", "1 library per arm", "library (not a replicate)", "CAGE promoter sums", "GSE126075", "31543760",
     "GEO public; no licence text in the record; only derived summaries are committed", "single time point"),
    ("neuron_d14_shwwox_cage", "training_human", "human", "same line differentiated to neurons, shRNA", "WWOX knockdown about 3 to 4 fold lower tags versus control arm",
     "2D neurons", "differentiation day 14", "1 library per arm", "library (not a replicate)", "CAGE promoter sums", "GSE126075", "31543760",
     "GEO public; no licence text in the record; only derived summaries are committed", "single time point"),
    ("mouse_p17_hipp_S", "seen_comparison", "mouse", "neuron-targeted Wwox deletion (series label S)", "S deletion versus S control",
     "hippocampus bulk", "P17", "3 v 2 animals", "animal", "RNA-seq transcript TPM", "GSE158681", "", "GEO public; driver identity and paper link UNVERIFIED", "P17"),
    ("mouse_p17_hipp_N", "seen_comparison", "mouse", "neural stem/progenitor-targeted Wwox deletion (series label N)", "N deletion versus N control",
     "hippocampus bulk", "P17", "2 v 2 animals", "animal", "RNA-seq transcript TPM", "GSE158681", "", "GEO public; driver identity and paper link UNVERIFIED", "P17"),
    ("mouse_p17_hipp_null", "seen_comparison", "mouse", "germline Wwox null", "null versus wild type (controls differ from the Cre-line controls)",
     "hippocampus bulk", "P17", "2 v 3 animals", "animal", "RNA-seq transcript TPM", "GSE158681", "", "GEO public; systemic illness confound", "P17"),
    ("mouse_p17_ctx_S", "seen_comparison", "mouse", "neuron-targeted Wwox deletion (series label S)", "S deletion versus S control",
     "cortex bulk", "P17", "3 v 4 animals", "animal", "RNA-seq transcript TPM", "GSE158682", "", "GEO public; deletion depth overlaps controls", "P17"),
    ("mef_null", "context_other", "mouse", "embryonic fibroblasts", "Wwox knockout versus wild type", "mouse embryonic fibroblasts (non-neural)", "not applicable",
     "not extracted", "not extracted", "qPCR, Western, flux", "", "25012504", "published figures", "normoxia versus hypoxia"),
    ("fibroblast_ko", "context_other", "human", "human fibroblast line, WWOX knockout (figure arm; knockdown wording UNVERIFIED)", "knockout versus control",
     "non-neural fibroblast", "not applicable", "n not stated for the PDH panel", "not extracted", "enzyme assays, Western", "", "35328751", "published figures",
     "four oxygen x glucose conditions"),
    ("fly_head_rnai_abeta", "context_other", "Drosophila melanogaster", "pan-neuronal Wwox RNAi, with and without Abeta42", "knockdown plus Abeta42 versus Abeta42 alone",
     "adult head", "adult day 14", "5 pooled-head replicates", "pool of heads", "RNA-seq, HILIC LC-MS", "", "42909904", "published tables; amyloid context", "day 14"),
    ("patient_mrs", "context_other", "human", "one patient with a confounding second variant", "single case", "brain MRS voxel", "child", "1", "patient",
     "MRS", "", "", "registry entry; uncontrolled", "single scan"),
    ("p47t_knockin_brain", "heldout_candidate", "mouse", "Wwox P47T knock-in (WW1 domain missense, partial loss)", "homozygous versus wild type",
     "prefrontal cortex, parietal cortex, hippocampus, cerebellum", "age not extracted (UNVERIFIED)", "5 v 5 animals (cerebellum 4 v 3); the same animals supply all regions",
     "animal", "RNA-seq integer counts (processed table)", "GSE215425", "36828035", "GEO public; counts not inspected for any network gene", "single time point"),
    ("fly_head_factorial", "heldout_candidate", "Drosophila melanogaster", "pan-neuronal Wwox RNAi and CRISPRa, each with and without Abeta42", "2 x 2 factorial",
     "adult head", "adult", "4 pooled-head libraries per cell", "pool of heads", "featureCounts per library", "E-MTAB-14948;E-MTAB-14949", "42909904",
     "ArrayExpress public; perturbation depth not visible in the deposit", "single time point"),
    ("mouse_p17_hipp_snrna", "heldout_candidate", "mouse", "neuron-targeted Wwox deletion, nuclei", "S deletion versus S control", "hippocampal nuclei", "P17",
     "1 library per arm", "library (pseudo-replicated by nuclei)", "snRNA-seq", "GSE158684", "", "GEO public; same series family as the seen mouse contrasts", "P17"),
    ("human_organoid_scrna", "heldout_candidate", "human", "cerebral organoids, WWOX loss", "loss versus control", "organoid cells", "not extracted", "not accessible",
     "not accessible", "scRNA-seq", "E-MTAB-14792", "", "access refused (403); no request sent", "not accessible"),
]

# gene id table: symbol -> (hgnc, ensg, uniprot, mgi, mouse_symbol, ensmusg, chembl, fly, name)   (HGNC complete set 2026-10-22; Ensembl REST; ChEMBL REST; 2026-10-29)
G = {
    "WWOX": ("HGNC:12799", "ENSG00000186153", "Q9NZC7", "MGI:1931237", "Wwox", "ENSMUSG00000004637", "", "", "WW domain containing oxidoreductase"),
    "HIF1A": ("HGNC:4910", "ENSG00000100644", "Q16665", "MGI:106918", "Hif1a", "ENSMUSG00000021109", "CHEMBL4261", "", "hypoxia inducible factor 1 subunit alpha"),
    "SLC2A1": ("HGNC:11005", "ENSG00000117394", "P11166", "MGI:95755", "Slc2a1", "ENSMUSG00000028645", "CHEMBL2535", "", "solute carrier family 2 member 1"),
    "SLC2A3": ("HGNC:11007", "ENSG00000059804", "P11169", "MGI:95757", "Slc2a3", "ENSMUSG00000003153", "CHEMBL5215", "", "solute carrier family 2 member 3"),
    "HK1": ("HGNC:4922", "ENSG00000156515", "P19367", "MGI:96103", "Hk1", "ENSMUSG00000037012", "CHEMBL2688", "", "hexokinase 1"),
    "HK2": ("HGNC:4923", "ENSG00000159399", "P52789", "MGI:1315197", "Hk2", "ENSMUSG00000000628", "CHEMBL2640", "", "hexokinase 2"),
    "PFKP": ("HGNC:8878", "ENSG00000067057", "Q01813", "MGI:1891833", "Pfkp", "ENSMUSG00000021196", "CHEMBL2972", "", "phosphofructokinase, platelet"),
    "ALDOA": ("HGNC:414", "ENSG00000149925", "P04075", "MGI:87994", "Aldoa", "ENSMUSG00000030695", "CHEMBL2106", "", "aldolase, fructose-bisphosphate A"),
    "PGK1": ("HGNC:8896", "ENSG00000102144", "P00558", "MGI:97555", "Pgk1", "ENSMUSG00000062070", "CHEMBL2886", "", "phosphoglycerate kinase 1"),
    "ENO1": ("HGNC:3350", "ENSG00000074800", "P06733", "MGI:95393", "Eno1", "ENSMUSG00000063524", "CHEMBL3298", "", "enolase 1"),
    "PKM": ("HGNC:9021", "ENSG00000067225", "P14618", "MGI:97591", "Pkm", "ENSMUSG00000032294", "CHEMBL1075189", "", "pyruvate kinase M1/2"),
    "LDHA": ("HGNC:6535", "ENSG00000134333", "P00338", "MGI:96759", "Ldha", "ENSMUSG00000063229", "CHEMBL4835", "FBgn0001258", "lactate dehydrogenase A"),
    "LDHB": ("HGNC:6541", "ENSG00000111716", "P07195", "MGI:96763", "Ldhb", "ENSMUSG00000030246", "CHEMBL4940", "FBgn0001258", "lactate dehydrogenase B"),
    "BNIP3": ("HGNC:1084", "ENSG00000176171", "Q12983", "MGI:109326", "Bnip3", "ENSMUSG00000078566", "", "", "BCL2 interacting protein 3"),
    "SLC16A1": ("HGNC:10922", "ENSG00000155380", "P53985", "MGI:106013", "Slc16a1", "ENSMUSG00000032902", "CHEMBL4360", "", "solute carrier family 16 member 1"),
    "SLC16A3": ("HGNC:10924", "ENSG00000141526", "O15427", "MGI:1933438", "Slc16a3", "ENSMUSG00000025161", "CHEMBL2073663", "", "solute carrier family 16 member 3"),
    "PDK1": ("HGNC:8809", "ENSG00000152256", "Q15118", "MGI:1926119", "Pdk1", "ENSMUSG00000006494", "CHEMBL4766", "FBgn0017558", "pyruvate dehydrogenase kinase 1"),
    "PDK2": ("HGNC:8810", "ENSG00000005882", "Q15119", "MGI:1343087", "Pdk2", "ENSMUSG00000038967", "CHEMBL3861", "FBgn0017558", "pyruvate dehydrogenase kinase 2"),
    "PDK3": ("HGNC:8811", "ENSG00000067992", "Q15120", "MGI:2384308", "Pdk3", "ENSMUSG00000035232", "CHEMBL3893", "FBgn0017558", "pyruvate dehydrogenase kinase 3"),
    "PDK4": ("HGNC:8812", "ENSG00000004799", "Q16654", "MGI:1351481", "Pdk4", "ENSMUSG00000019577", "CHEMBL4141", "FBgn0017558", "pyruvate dehydrogenase kinase 4"),
    "PDHA1": ("HGNC:8806", "ENSG00000131828", "P08559", "MGI:97532", "Pdha1", "ENSMUSG00000031299", "CHEMBL2092", "", "pyruvate dehydrogenase E1 subunit alpha 1"),
    "MBP": ("HGNC:6925", "ENSG00000197971", "P02686", "MGI:96925", "Mbp", "ENSMUSG00000041607", "", "", "myelin basic protein"),
    "PLP1": ("HGNC:9086", "ENSG00000123560", "P60201", "MGI:97623", "Plp1", "ENSMUSG00000031425", "", "", "proteolipid protein 1"),
    "MOG": ("HGNC:7197", "ENSG00000204655", "Q16653", "MGI:97435", "Mog", "ENSMUSG00000076439", "", "", "myelin oligodendrocyte glycoprotein"),
}
MYELIN_MEMBERS = ["HGNC:6925", "HGNC:9086", "HGNC:7197", "HGNC:6783", "HGNC:7189", "HGNC:8514", "HGNC:2158", "HGNC:6817", "HGNC:20707", "HGNC:12555"]
GLY10 = ["SLC2A1", "HK2", "PFKP", "ALDOA", "PGK1", "ENO1", "LDHA", "PKM", "BNIP3", "LDHB"]
PDKF = ["PDK1", "PDK2", "PDK3", "PDK4"]
HUMAN_SYS = ["organoid_ko_w15", "hnpc_shwwox_cage", "neuron_d14_shwwox_cage"]
MOUSE_SYS = {"H_S": "mouse_p17_hipp_S", "H_N": "mouse_p17_hipp_N", "H_null": "mouse_p17_hipp_null", "C_S": "mouse_p17_ctx_S"}
OBS_SYS = HUMAN_SYS + list(MOUSE_SYS.values()) + ["mef_null", "fibroblast_ko", "fly_head_rnai_abeta", "patient_mrs"]
CAVEAT = {
    "HK2": "organoid +2.17 is large; neuron CAGE value is below the 10-tag rule; hNPC one library per arm",
    "LDHA": "organoid value is confounded with maturity (falls with culture time in an unrelated spheroid series); mouse P17 not concordant",
    "LDHB": "set-member only; mouse P17 lower in the cell-targeted contrasts",
    "BNIP3": "author-declared set member, not a regulator edge; hNPC one library per arm",
    "SLC2A1": "organoid and hNPC only; mouse P17 flat or lower",
    "PDK1": "lower in sign only in both human systems; inside the single-gene null in both (p about 0.30 and 0.49 per wwox_systems_comparison_it5); a rise was predicted by the chain and is not seen",
}
SET_META = {
    "SET:GLYCOLYSIS_LACTATE_10": ("Glycolysis_lactate", GLY10),
    "SET:PDK_FAMILY_4": ("PDK_family", PDKF),
    "SET:MYELIN_OL_10": ("Myelin_OL", None),
}
PROCESS = {  # id -> (label, type, other_id, module)
    "GO:0006096": ("glycolytic process (flux)", "process", "GO:0006096"),
    "GO:0004739": ("pyruvate dehydrogenase (acetyl-transferring) activity", "process", "GO:0004739"),
    "CHEBI:24996": ("lactate", "metabolite", "CHEBI:24996"),
}

EVIDENCE = [  # id, kind, pmid, path, anchor, status
    ("E01", "manifest", "25012504", "disease-models/wwox/research/deepdive_manifests/PMID25012504.json#4", "wwox loss raises hif1alpha protein", "full-text receipt FTR-20260814-25012504-01"),
    ("E02", "manifest", "25012504", "disease-models/wwox/research/deepdive_manifests/PMID25012504.json#2", "pdk1", "full-text receipt FTR-20260814-25012504-01"),
    ("E03", "manifest", "25012504", "disease-models/wwox/research/deepdive_manifests/PMID25012504.json#1", "glycolytic/respiratory shift", "full-text receipt FTR-20260814-25012504-01"),
    ("E04", "manifest", "25012504", "disease-models/wwox/research/deepdive_manifests/PMID25012504.json#5", "disappears under hypoxia", "full-text receipt FTR-20260814-25012504-01"),
    ("E05", "manifest", "35328751", "disease-models/wwox/research/deepdive_manifests/PMID35328751.json#7", "lactate is higher in the knockout in all four", "manifest entry; figure attestation by hand reading"),
    ("E06", "manifest", "35328751", "disease-models/wwox/research/deepdive_manifests/PMID35328751.json#9", "two of the four conditions", "manifest entry"),
    ("E07", "manifest", "35328751", "disease-models/wwox/research/deepdive_manifests/PMID35328751.json#7", "no knockout-versus-control bracket", "manifest entry; figure attestation by hand reading"),
    ("E08", "manifest", "42909904", "disease-models/wwox/research/deepdive_manifests/PMID42909904.json#29", "ldh is higher", "manifest entry; amyloid fly model"),
    ("E09", "manifest", "42909904", "disease-models/wwox/research/deepdive_manifests/PMID42909904.json#43", "l-lactate relative abundance", "manifest entry; amyloid fly model"),
    ("E10", "manifest", "42909904", "disease-models/wwox/research/deepdive_manifests/PMID42909904.json#46", "no differences in atp", "manifest entry; amyloid fly model"),
    ("E11", "pubmed_abstract", "25012504", "", "WWOX, via its first WW domain, physically interacts with HIF1", "abstract read via PubMed 2026-10-29; association, not a causal edge"),
    ("E12", "pubmed_abstract", "16517406", "", "inducing pyruvate dehydrogenase kinase 1", "abstract read via PubMed 2026-10-29; non-WWOX background, full text not read"),
    ("E13", "document", "", DR + "/gse156243/prediction_hif1a_pdk_chain_20261025.md", "Its chain is:", "document; chain as declared before the organoid genes were read"),
    ("E14", "document", "", DR + "/needs/needs.json", "extremely low", "registry-backed entry DL-BIO-008 quoted in the need; n=1, confounded"),
    ("E15", "document", "", DR + "/needs/needs.json", "human_neural_progenitor_shrna_knockdown", "need observation O5; transcript, one library per arm"),
    ("E16", "document", "", DR + "/hnpc_gse126075_it5_20261029/PRE_ANALYSIS.md", "SLC16A1, SLC16A3 per gene", "pre-analysis set declaration"),
    ("E18", "pubmed_abstract", "25012504", "", "Wwox-deficient cells exhibited increased HIF1", "abstract read via PubMed 2026-10-29; mouse embryonic fibroblasts and cancer cells"),
    ("E19", "document", "", DR + "/wwox_systems_comparison_it5_20261029.md", "HIF1A mRNA flat", "comparison paragraph: HIF1A mRNA is flat in organoid and hNPC; HIF1A is stability-controlled"),
]


def read_tsv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.reader(f, delimiter="\t"))


def tsv_rows(relpath):
    t = read_tsv(os.path.join(ROOT, relpath))
    return [dict(zip(t[0], r)) for r in t[1:]]


def find_row(relpath, key):
    want = dict(p.split("=", 1) for p in key.split(";"))
    for r in tsv_rows(relpath):
        if all(r.get(k) == v for k, v in want.items()):
            return r
    return None


def sign_gene(v):
    return "up" if v >= THR else "down" if v <= -THR else "no_change"


def fmt(x):
    return f"{x:.3f}"


# ------------------------------------------------------------------ build
def build_observations():
    obs = []
    D = DR + "/subnetwork_it7_p1_20261029/derived_gene_values.tsv"
    K = DR + "/mouse_wwox_p17_it6_p4_20261029/results/key_genes.tsv"
    keyrows = {(r["contrast"], r["gene"]): r for r in tsv_rows(K)}
    derived = {(r["gene"], r["system_id"]): r for r in tsv_rows(D)}
    for sym in G:
        hid = G[sym][0]
        for sysid in HUMAN_SYS:
            r = derived[(sym, sysid)]
            if r["measurable"] == "True":
                v = float(r["R_centred"])
                obs.append([hid, sysid, "transcript", sign_gene(v), fmt(v), "centred log2 ratio", D, f"gene={sym};system_id={sysid}", "R_centred", "", "descriptive per-gene value, not a differential-expression call"])
            else:
                note = "not measurable under the universe rule (below the count/tag threshold or symbol absent)"
                val = fmt(float(r["R_centred"])) if r["R_centred"] else ""
                obs.append([hid, sysid, "transcript", "UNKNOWN", val, "centred log2 ratio", D, f"gene={sym};system_id={sysid}", "R_centred", "", note])
        for c, sysid in MOUSE_SYS.items():
            ms = G[sym][4]
            r = keyrows.get((c, ms))
            if r is None:
                obs.append([hid, sysid, "transcript", "UNKNOWN", "", "", "", "", "", "", "gene not tabulated per gene in the P4 key_genes table (set-level values only)"])
            elif r["measurable"] == "True":
                v = float(r["R_centred"])
                obs.append([hid, sysid, "transcript", sign_gene(v), fmt(v), "centred log2 ratio", K, f"contrast={c};gene={ms}", "R_centred", "", "animal-level separation not used here; 2 to 3 animals per arm"])
            else:
                obs.append([hid, sysid, "transcript", "UNKNOWN", fmt(float(r["R_centred"])), "centred log2 ratio", K, f"contrast={c};gene={ms}", "R_centred", "", "below the 1 TPM universe threshold in this contrast"])
    # sets
    O = DR + "/hnpc_gse126075_it5_20261029/p7_organoid_set_summary.tsv"
    H = DR + "/hnpc_gse126075_it5_20261029/set_summary.tsv"
    M = DR + "/mouse_wwox_p17_it6_p4_20261029/results/set_summary.tsv"
    for sid, (sname, _m) in SET_META.items():
        for sysid in HUMAN_SYS:
            if sname == "Myelin_OL":
                obs.append([sid, sysid, "set_transcript", "UNKNOWN", "", "", "", "", "", "", "set not examined in this system"])
                continue
            if sysid == "organoid_ko_w15":
                f, key, col = O, f"set={sname}", "mean_centred_R"
            else:
                f, key, col = H, f"set={sname};contrast={'C_hNPC' if sysid.startswith('hnpc') else 'C_neuron'}", "mean_primary"
            r = find_row(f, key)
            v, lo, hi = float(r[col]), float(r["null_lo"]), float(r["null_hi"])
            s = "up" if v > hi else "down" if v < lo else "no_change"
            obs.append([sid, sysid, "set_transcript", s, fmt(v), "centred log2 ratio of set mean; sign = outside matched null", f, key, col, "", f"matched-null band [{lo:.3f}, {hi:.3f}]"])
        for c, sysid in MOUSE_SYS.items():
            key = f"contrast={c};universe_thr_tpm=1.0;set={sname}"
            r = find_row(M, key)
            v = float(r["mean"])
            s = ("up" if v > 0 else "down") if r["outside"] == "True" else "no_change"
            obs.append([sid, sysid, "set_transcript", s, fmt(v), "centred log2 ratio of set mean; sign = outside matched null", M, key, "mean", "", f"outside={r['outside']}; matched-null band [{r['null_lo']}, {r['null_hi']}]"])
    # literal observations
    def lit(node, sysid, level, sign, ev, note):
        obs.append([node, sysid, level, sign, "", "", "", "", "", ev, note])
    lit("HGNC:4910", "mef_null", "protein", "up", "E01", "HIF1A protein raised under normoxia; difference disappears under hypoxia (E04)")
    lit("HGNC:4910", "fibroblast_ko", "protein", "mixed", "E06", "cytoplasmic HIF1A lower in two of four oxygen x glucose conditions")
    lit("HGNC:8809", "mef_null", "transcript", "up", "E02", "PDK1 reported as higher; level named only as 'higher levels' in the cited sentence")
    lit("GO:0004739", "fibroblast_ko", "activity", "no_change", "E07", "no knockout-versus-control difference in any condition; n not stated")
    lit("CHEBI:24996", "fibroblast_ko", "metabolite", "up", "E05", "higher in the knockout in all four conditions")
    lit("CHEBI:24996", "fly_head_rnai_abeta", "metabolite", "mixed", "E09", "up only in knockdown plus Abeta42; nominally lower without Abeta42; amyloid context")
    lit("CHEBI:24996", "patient_mrs", "functional", "down", "E14", "cerebral lactate reported extremely low; n=1, confounded by a second variant")
    lit("GO:0006096", "mef_null", "flux", "up", "E03", "glycolytic/respiratory shift measured directly (oxygen consumption lower)")
    lit("HGNC:6535", "fly_head_rnai_abeta", "transcript", "up", "E08", "fly Ldh, log2 fold change about 1.29 in knockdown plus Abeta42 versus Abeta42; ortholog not one-to-one")
    # fill UNKNOWN for every unobserved (node, system) of process nodes and perturbation-free combos
    have = {(o[0], o[1]) for o in obs}
    for nid in list(PROCESS):
        for sysid in OBS_SYS:
            if (nid, sysid) not in have:
                obs.append([nid, sysid, "none", "UNKNOWN", "", "", "", "", "", "", "not measured in this system in any source read"])
    for sym in ("HIF1A", "PDK1"):
        hid = G[sym][0]
        for sysid in ("mef_null", "fibroblast_ko", "fly_head_rnai_abeta", "patient_mrs"):
            if (hid, sysid) not in have:
                obs.append([hid, sysid, "none", "UNKNOWN", "", "", "", "", "", "", "not measured in this system in any source read"])
    out = []
    for i, o in enumerate(obs, 1):
        out.append([f"O{i:04d}"] + o)
    return out


OBS_HEADER = ["obs_id", "node_id", "system_id", "readout_level", "sign", "value", "value_meaning", "source_file", "source_key", "source_col", "evidence_id", "note"]


def build_nodes(obs):
    byns = {(o[1], o[2]): o for o in obs}
    hdr = ["node_id", "node_type", "symbol", "name", "hgnc_id", "uniprot", "ensembl_gene_human", "mgi_id", "mouse_symbol", "ensembl_gene_mouse",
           "chembl_target", "fly_ortholog", "other_id", "members", "module", "role", "human_concordance", "mouse_agreement", "caveat"] + ["sign_" + s for s in OBS_SYS]
    rows = []
    for sym, g in G.items():
        hid = g[0]
        if sym == "WWOX":
            ntype, module, role = "perturbation", "perturbation", "perturbation"
        elif sym in ("MBP", "PLP1", "MOG"):
            ntype, module, role = "gene", "positive_control_myelin", "positive_control"
        else:
            ntype, module, role = "gene", "glycolysis_pdh_lactate", "network_context"
        signs = {s: (byns[(hid, s)][4] if (hid, s) in byns else "UNKNOWN") for s in OBS_SYS}
        conc, agree = concordance(hid, byns)
        if conc in ("concordant_up", "concordant_down") and module == "glycolysis_pdh_lactate":
            role = "signature_candidate"
        rows.append([hid, ntype, sym, g[8], hid, g[2], g[1], g[3], g[4], g[5], g[6], g[7], "", "", module, role, conc if ntype == "gene" else "not_applicable",
                     agree if ntype == "gene" else "not_applicable", CAVEAT.get(sym, "")] + [signs[s] for s in OBS_SYS])
    for sid, (sname, mem) in SET_META.items():
        members = ";".join(G[m][0] for m in mem) if mem else ";".join(MYELIN_MEMBERS)
        label = {"SET:GLYCOLYSIS_LACTATE_10": "HIF-type glycolysis and lactate set (10 declared genes)", "SET:PDK_FAMILY_4": "PDK family (4 genes)",
                 "SET:MYELIN_OL_10": "myelin/oligodendrocyte set (10 declared genes; UGT8A in the declaration is mouse Ugt8a = HGNC UGT8)"}[sid]
        module = "positive_control_myelin" if sname == "Myelin_OL" else "glycolysis_pdh_lactate"
        role = "positive_control" if sname == "Myelin_OL" else "network_context"
        signs = {s: (byns[(sid, s)][4] if (sid, s) in byns else "UNKNOWN") for s in OBS_SYS}
        rows.append([sid, "set", sname, label, "", "", "", "", "", "", "", "", "", members, module, role, "not_applicable", "not_applicable", "set membership declared by the author in iteration 5; not externally validated"] + [signs[s] for s in OBS_SYS])
    for pid, (lab, ntype, oid) in PROCESS.items():
        signs = {s: (byns[(pid, s)][4] if (pid, s) in byns else "UNKNOWN") for s in OBS_SYS}
        rows.append([pid, ntype, lab, lab, "", "", "", "", "", "", "", "", oid, "", "glycolysis_pdh_lactate", "process_readout", "not_applicable", "not_applicable",
                     "readout of a process; transcripts above are not this process"] + [signs[s] for s in OBS_SYS])
    return hdr, rows


def concordance(hid, byns):
    o, h = byns.get((hid, "organoid_ko_w15")), byns.get((hid, "hnpc_shwwox_cage"))
    if not o or not h or o[4] == "UNKNOWN" or h[4] == "UNKNOWN":
        return "UNKNOWN", ""
    vo, vh = float(o[5]), float(h[5])
    if vo >= THR and vh >= THR:
        c = "concordant_up"
    elif vo <= -THR and vh <= -THR:
        c = "concordant_down"
    else:
        return "not_concordant", ""
    want = "up" if c.endswith("up") else "down"
    ag = op = no = 0
    for s in MOUSE_SYS.values():
        m = byns.get((hid, s))
        sg = m[4] if m else "UNKNOWN"
        if sg == want:
            ag += 1
        elif sg in ("up", "down"):
            op += 1
        else:
            no += 1
    return c, f"agree:{ag};oppose:{op};flat_or_unknown:{no}"


EDGE_HEADER = ["edge_id", "source_node", "source_state", "target_node", "target_readout", "edge_type", "sign", "system_id", "genotype", "tissue_or_cell", "stage", "endpoint",
               "time", "direction_status", "evidence_ids", "counter_evidence_ids", "note"]
MEASURED_TARGETS = ["HGNC:6535", "HGNC:6541", "HGNC:4923", "HGNC:11005", "HGNC:1084", "HGNC:8809", "HGNC:8806", "HGNC:4910",
                    "SET:GLYCOLYSIS_LACTATE_10", "SET:PDK_FAMILY_4", "SET:MYELIN_OL_10", "GO:0006096", "GO:0004739", "CHEBI:24996"]


def build_edges(obs):
    sysrow = {s[0]: s for s in SYSTEMS}
    edges = []
    n = 0

    def add(*a):
        nonlocal n
        n += 1
        edges.append([f"ED{n:03d}"] + list(a))
    wwox = G["WWOX"][0]
    by = {}
    for o in obs:
        by.setdefault(o[1], []).append(o)
    for t in MEASURED_TARGETS:
        rows = [o for o in by[t] if o[4] != "UNKNOWN"]
        for o in rows:
            others = [x for x in rows if x[2] != o[2] and x[3] == o[3]]
            counter = [x[0] for x in others if x[4] != o[4]]
            if not others:
                status = "single_system"
            else:
                status = "conflict" if counter else "consistent"
            s = sysrow[o[2]]
            note = o[11] if o[11] else ""
            add(wwox, "loss", t, o[3], "measured", o[4], o[2], s[4], s[5], s[6], o[3], s[13], status, o[0], ";".join(counter), note)
    # structural edges
    add(wwox, "present", "HGNC:4910", "protein", "association", "UNKNOWN", "background", "Wwox-deficient cells and cancer lines; WW1 domain", "cell lines (non-neural)", "not applicable", "physical interaction", "not applicable", "single_system", "E11", "E06", "association only: a physical interaction is not modulation; modulation of HIF1A level is the separate measured edge")
    for tg in ("HGNC:4923", "HGNC:11005", "HGNC:6535"):
        add("HGNC:4910", "up", tg, "transcript", "inferred", "up", "background", "Wwox-deficient mouse fibroblasts and cancer cells (HIF1A-dependent glycolytic gene expression)", "non-neural cells", "not applicable", "glycolytic gene expression", "not applicable", "single_system", "E18;E13", "E19", "regulation by HIF1A inferred from non-neural WWOX work; HIF1A mRNA is flat in the human neural systems and HIF1A is stability-controlled")
    add("HGNC:4910", "up", "HGNC:8809", "transcript", "inferred", "up", "background", "mouse and human cells in hypoxia (non-WWOX)", "cell lines", "not applicable", "PDK1 induction", "not applicable", "single_system", "E12;E13", "", "background mechanism from a non-WWOX paper (abstract level); PDK1 transcript is not raised in the human neural systems")
    add("HGNC:8809", "up", "GO:0004739", "activity", "inferred", "down", "background", "non-WWOX cells", "cell lines", "not applicable", "PDH inhibition by phosphorylation", "not applicable", "single_system", "E12", "E07", "background mechanism; PDH activity shows no difference in the one WWOX-deficient human line measured")
    add("GO:0004739", "down", "CHEBI:24996", "metabolite", "hypothesised", "up", "none", "not tested", "not tested", "not tested", "lactate level", "not tested", "untested", "E13", "E14;E07", "hypothesised by mass action; brain lactate reported low in one patient; lactate is up in a fibroblast line and in an amyloid fly only")
    add("HGNC:6535", "up", "CHEBI:24996", "metabolite", "hypothesised", "up", "none", "not tested", "not tested", "not tested", "lactate level", "not tested", "untested", "E15", "E14", "transcript rise does not establish lactate; no lactate is measured in any human neural WWOX system")
    for tg in ("HGNC:10922", "HGNC:10924"):
        add(tg, "present", "CHEBI:24996", "metabolite", "association", "UNKNOWN", "background", "not applicable", "not applicable", "not applicable", "monocarboxylate transport", "not applicable", "untested", "E16", "", "transporter-to-metabolite association only; no direction asserted")
    return edges


def build_nodes_extra_syntax(rows):
    return rows


def write(name, header, rows):
    with open(os.path.join(HERE, name), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def build():
    write("systems.tsv", ["system_id", "role", "species", "model", "perturbation", "tissue_or_cell", "stage", "n", "unit", "platform", "accession", "pmid", "reuse_terms", "time"], SYSTEMS)
    write("evidence.tsv", ["evidence_id", "kind", "pmid", "path", "anchor", "status"], EVIDENCE)
    obs = build_observations()
    write("observations.tsv", OBS_HEADER, obs)
    hdr, rows = build_nodes(obs)
    write("nodes.tsv", hdr, rows)
    write("edges.tsv", EDGE_HEADER, build_edges(obs))
    print("built", ", ".join(FILES))
    return 0


# ------------------------------------------------------------------ check
def check(hgnc_path=None):
    P = []
    T = {}
    for f in FILES:
        p = os.path.join(HERE, f)
        if not os.path.isfile(p):
            P.append(f"{f}: missing")
            continue
        raw = open(p, encoding="utf-8").read()
        if not raw.endswith("\n") or raw.endswith("\n\n"):
            P.append(f"{f}: must end with exactly one newline (no trailing notes or blank lines)")
        t = read_tsv(p)
        w = len(t[0])
        for i, r in enumerate(t[1:], 2):
            if len(r) != w:
                P.append(f"{f}: line {i} has {len(r)} fields, header has {w}")
            if not any(r):
                P.append(f"{f}: line {i} blank")
        T[f] = [dict(zip(t[0], r)) for r in t[1:]]
        low = raw.lower()
        for tok in FORBIDDEN:
            if tok in low:
                P.append(f"{f}: firewall vocabulary {tok!r} present")
    if P:
        return P
    sysd = {r["system_id"]: r for r in T["systems.tsv"]}
    ev = {r["evidence_id"]: r for r in T["evidence.tsv"]}
    nodes = {r["node_id"]: r for r in T["nodes.tsv"]}
    obs = {r["obs_id"]: r for r in T["observations.tsv"]}
    for f, k in (("systems.tsv", "system_id"), ("evidence.tsv", "evidence_id"), ("nodes.tsv", "node_id"), ("observations.tsv", "obs_id"), ("edges.tsv", "edge_id")):
        ids = [r[k] for r in T[f]]
        if len(ids) != len(set(ids)):
            P.append(f"{f}: duplicate {k}")
    pat = {"hgnc_id": r"HGNC:\d+", "ensembl_gene_human": r"ENSG\d{11}", "uniprot": r"[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}",
           "mgi_id": r"MGI:\d+", "ensembl_gene_mouse": r"ENSMUSG\d{11}", "chembl_target": r"CHEMBL\d+", "fly_ortholog": r"FBgn\d{7}"}
    hg = None
    if hgnc_path:
        hg = {d["symbol"]: d for d in json.load(open(hgnc_path))["response"]["docs"]}
    for n in T["nodes.tsv"]:
        if n["node_type"] not in NODE_TYPES:
            P.append(f"node {n['node_id']}: node_type")
        if n["role"] not in ROLES:
            P.append(f"node {n['node_id']}: role")
        if n["node_type"] in ("gene", "perturbation"):
            for c, rx in pat.items():
                if n[c] and not re.fullmatch(rx, n[c]):
                    P.append(f"node {n['node_id']}: {c} {n[c]!r} does not match")
            if not n["hgnc_id"] or n["node_id"] != n["hgnc_id"] or not n["uniprot"] or not n["ensembl_gene_human"] or not n["mgi_id"]:
                P.append(f"node {n['node_id']}: gene identity incomplete")
            if hg is not None:
                d = hg.get(n["symbol"])
                if not d or d["hgnc_id"] != n["hgnc_id"] or d.get("ensembl_gene_id") != n["ensembl_gene_human"] or n["uniprot"] not in d.get("uniprot_ids", []) or n["mgi_id"] not in d.get("mgd_id", []):
                    P.append(f"node {n['node_id']}: disagrees with the HGNC complete set")
        elif n["node_type"] == "set":
            if not n["node_id"].startswith("SET:") or not n["members"]:
                P.append(f"node {n['node_id']}: set without members")
            for m in n["members"].split(";"):
                if m not in nodes and not re.fullmatch(r"HGNC:\d+", m):
                    P.append(f"node {n['node_id']}: member {m} is not an HGNC id")
        else:
            if not re.fullmatch(r"(GO:\d{7}|CHEBI:\d+)", n["node_id"]) or n["other_id"] != n["node_id"]:
                P.append(f"node {n['node_id']}: process/metabolite id")
    if hg is None:
        print("note: --hgnc not given; HGNC cross-check skipped")
    # evidence
    for e in T["evidence.tsv"]:
        if e["kind"] not in EVID_KINDS:
            P.append(f"{e['evidence_id']}: kind")
        if e["kind"] in ("manifest", "document"):
            path, _, idx = e["path"].partition("#")
            fp = os.path.join(ROOT, path)
            if not os.path.isfile(fp):
                P.append(f"{e['evidence_id']}: file missing {path}")
                continue
            if e["kind"] == "manifest":
                ents = json.load(open(fp))["verbatim_locators"]["entries"]
                i = int(idx)
                if not 0 <= i < len(ents):
                    P.append(f"{e['evidence_id']}: entry out of range")
                elif e["anchor"].lower() not in (ents[i].get("proposition", "") + " " + ents[i].get("snippet", "")).lower():
                    P.append(f"{e['evidence_id']}: anchor not in manifest entry")
            else:
                if e["anchor"] not in open(fp, encoding="utf-8").read():
                    P.append(f"{e['evidence_id']}: anchor not in document")
        if e["kind"] == "pubmed_abstract" and not re.fullmatch(r"\d+", e["pmid"]):
            P.append(f"{e['evidence_id']}: pmid")
    # observations
    for o in T["observations.tsv"]:
        oid = o["obs_id"]
        if o["node_id"] not in nodes:
            P.append(f"{oid}: node")
        if o["system_id"] not in sysd:
            P.append(f"{oid}: system")
        if o["sign"] not in SIGNS:
            P.append(f"{oid}: sign")
        if o["readout_level"] not in READOUTS:
            P.append(f"{oid}: readout")
        if sysd.get(o["system_id"], {}).get("role") == "heldout_candidate":
            P.append(f"{oid}: an observation exists in a held-out candidate system (firewall)")
        if o["evidence_id"] and o["evidence_id"] not in ev:
            P.append(f"{oid}: evidence id")
        if o["sign"] != "UNKNOWN" and not o["evidence_id"] and not o["source_file"]:
            P.append(f"{oid}: observed sign without provenance")
        if o["source_file"]:
            r = find_row(o["source_file"], o["source_key"])
            if r is None:
                P.append(f"{oid}: source row not found")
                continue
            if r[o["source_col"]] == "":
                if o["value"] != "" or o["sign"] != "UNKNOWN":
                    P.append(f"{oid}: source value empty but observation has one")
                continue
            v = float(r[o["source_col"]])
            if o["value"] == "" or abs(v - float(o["value"])) > 0.0006:
                P.append(f"{oid}: value differs from source ({o['value']} vs {v})")
            if o["node_id"].startswith("SET:"):
                if "outside" in r:
                    s = ("up" if v > 0 else "down") if r["outside"] == "True" else "no_change"
                else:
                    s = "up" if v > float(r["null_hi"]) else "down" if v < float(r["null_lo"]) else "no_change"
            else:
                meas = r.get("measurable", "True") == "True"
                s = sign_gene(v) if meas else "UNKNOWN"
            if s != o["sign"]:
                P.append(f"{oid}: sign {o['sign']} but source gives {s}")
    # nodes: derived columns
    byns = {}
    for o in T["observations.tsv"]:
        byns[(o["node_id"], o["system_id"])] = [o["obs_id"], o["node_id"], o["system_id"], o["readout_level"], o["sign"], o["value"]]
    for n in T["nodes.tsv"]:
        for s in OBS_SYS:
            want = byns[(n["node_id"], s)][4] if (n["node_id"], s) in byns else "UNKNOWN"
            if n["sign_" + s] != want:
                P.append(f"node {n['node_id']}: sign_{s} {n['sign_' + s]} != observations {want}")
        if n["node_type"] == "gene":
            c, a = concordance(n["node_id"], byns)
            if n["human_concordance"] != c or n["mouse_agreement"] != a:
                P.append(f"node {n['node_id']}: human_concordance/mouse_agreement not reproducible")
            if n["role"] == "signature_candidate" and c not in ("concordant_up", "concordant_down"):
                P.append(f"node {n['node_id']}: signature candidate without concordance")
    # edges
    for e in T["edges.tsv"]:
        k = e["edge_id"]
        if e["edge_type"] not in EDGE_TYPES:
            P.append(f"{k}: edge_type")
        if e["sign"] not in SIGNS:
            P.append(f"{k}: sign")
        if e["target_readout"] not in READOUTS + ["protein"]:
            P.append(f"{k}: readout")
        for c in ("source_node", "target_node"):
            if e[c] not in nodes:
                P.append(f"{k}: {c}")
        if e["system_id"] not in sysd and e["system_id"] not in ("background", "none"):
            P.append(f"{k}: system")
        if e["edge_type"] == "measured":
            if not (e["evidence_ids"] in obs and obs[e["evidence_ids"]]["node_id"] == e["target_node"] and obs[e["evidence_ids"]]["system_id"] == e["system_id"]
                    and obs[e["evidence_ids"]]["sign"] == e["sign"]):
                P.append(f"{k}: measured edge does not match its observation")
            exp = [x["obs_id"] for x in T["observations.tsv"] if x["node_id"] == e["target_node"] and x["sign"] != "UNKNOWN" and x["system_id"] != e["system_id"]
                   and x["readout_level"] == obs[e["evidence_ids"]]["readout_level"] and x["sign"] != e["sign"]] if e["evidence_ids"] in obs else []
            if sorted(exp) != sorted([x for x in e["counter_evidence_ids"].split(";") if x]):
                P.append(f"{k}: counter evidence not reproducible")
        else:
            if not e["evidence_ids"]:
                P.append(f"{k}: non-measured edge without evidence")
            if e["edge_type"] == "association" and e["sign"] != "UNKNOWN":
                P.append(f"{k}: an association edge carries no sign")
        for col in ("evidence_ids", "counter_evidence_ids"):
            for x in [y for y in e[col].split(";") if y]:
                if x not in ev and x not in obs:
                    P.append(f"{k}: {col} {x} unresolved")
        if e["source_state"] not in ("loss", "present", "up", "down"):
            P.append(f"{k}: source_state")
    return P


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "build":
        return build()
    if argv[0] == "check":
        hg = argv[argv.index("--hgnc") + 1] if "--hgnc" in argv else None
        P = check(hg)
        for p in P:
            print("PROBLEM:", p)
        print(f"{len(P)} problem(s)")
        return 1 if P else 0
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
