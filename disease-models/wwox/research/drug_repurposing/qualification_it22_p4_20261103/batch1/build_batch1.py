#!/usr/bin/env python3
"""IT22 P4 batch 1: writes the qualification table, typed potency table, edge provenance, locators, reading depth, raw digests and receipt JSON files.
  build_batch1.py --help
  build_batch1.py write RAW_DIR XML_DIR      RAW_DIR holds the served ChEMBL JSON (raw/mol_*, raw/mech_*, raw/act_*) and OmniPath TSV; XML_DIR the five PMC article XML files
Third-party raw files are NOT in git: only their sha256 (raw_hashes_it22_p4_b1.tsv). Receipts are prepared files for the integrator; nothing is appended to the ledger here."""
import sys
if len(sys.argv) < 4 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import csv, hashlib, html, json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import rows_it22_p4_b1 as RW

RAW, XML = Path(sys.argv[2]), Path(sys.argv[3])
PKG = "disease-models/wwox/research/drug_repurposing/qualification_it22_p4_20261103/batch1"
OUT = [f"{PKG}/README.md", f"{PKG}/qualification_it22_p4_b1.tsv", f"{PKG}/edge_provenance_it22_p4_b1.tsv", f"{PKG}/locators_it22_p4_b1.tsv"]


def tsv(path, cols, rows):
    with open(HERE / path, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(cols)
        for r in rows:
            w.writerow([str(r.get(c, "")).replace("\t", " ").replace("\n", " ") for c in cols])


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


# 1 qualification table
tsv("qualification_it22_p4_b1.tsv", RW.COLS, RW.R)

# 2 typed potency (ChEMBL rows, never pooled across type or unit; documents resolved by hand in the README)
DOC = {"CHEMBL4706478": "29360358", "CHEMBL3596180": "25637120", "CHEMBL3390834": "(no PMID; Medchemcomm 2012 doi 10.1039/C1MD00199J)", "CHEMBL4609972": "(not resolved)", "CHEMBL2440014": "(not resolved)",
       "CHEMBL3991601": "29191878", "CHEMBL3880434": "(patent compilation 2013, no PMID)", "CHEMBL4020778": "28506751", "CHEMBL5257016": "(not resolved)", "CHEMBL5346869": "(not resolved)",
       "CHEMBL6115055": "40263713", "CHEMBL3886495": "(patent US-9242996-B2, no PMID)", "CHEMBL5230103": "32791404", "CHEMBL4385610": "(not resolved)", "CHEMBL4808148": "(not resolved)"}
KEEP = {"CHEMBL1851943": lambda n: "deacetylase" in n.lower() or "HDAC" in n,
        "CHEMBL4650314": lambda n: True,
        "CHEMBL3544960": lambda n: any(k in n for k in ("Rho-associated", "RAC-", "cAMP-dependent", "Ribosomal protein S6", "Sgk3", "MAP kinase-activated", "Serine/threonine-protein kinase N", "Serine/threonine-protein kinase AKT", "Protein kinase C delta", "LATS1", "Beta-adrenergic receptor kinase")),
        "CHEMBL3909517": lambda n: True}
NAMES = {"CHEMBL1851943": "pracinostat", "CHEMBL4650314": "desidustat", "CHEMBL3544960": "AT-13148", "CHEMBL3909517": "rineterkib"}
rows = []
for c, f in KEEP.items():
    for x in json.load(open(RAW / f"act_{c}.json"))["activities"]:
        n = x.get("target_pref_name") or ""
        if x["standard_units"] != "nM" or x["standard_type"] not in ("IC50", "Ki", "Kd", "EC50") or not f(n):
            continue
        rows.append(dict(compound=NAMES[c], target=n, measure_type=x["standard_type"], relation=x["standard_relation"], value_nM=x["standard_value"], assay_type=x.get("assay_type"),
                         document=x.get("document_chembl_id"), pmid_of_document=DOC.get(x.get("document_chembl_id"), ""), assay_description=(x.get("assay_description") or "")[:140]))
rows.sort(key=lambda r: (r["compound"], r["target"], r["measure_type"], float(r["value_nM"])))
tsv("typed_potency_it22_p4_b1.tsv", ["compound", "target", "measure_type", "relation", "value_nM", "assay_type", "document", "pmid_of_document", "assay_description"], rows)

# 3 locators: each quote is matched against the flattened article text of the saved XML
def flat(p):
    t = re.sub(r"<[^>]+>", "", Path(p).read_text(encoding="utf8"))
    return re.sub(r"\s+", " ", html.unescape(t))


ART = {"PMC4083087": ("24990963", "Genes Dev 2014 (EglN2/FOXO3a)"), "PMC6571149": ("28689659", "Mol Cell 2017 (Bcl3 phosphorylation)"), "PMC2854092": ("20181828", "Mol Biol Cell 2010 (p8, FoxO3, bnip3)"),
       "PMC7611345": ("32616501", "Clin Cancer Res 2020 (AT13148 first-in-human)"), "PMC12063501": ("39914641", "Exp Neurol 2025 (desidustat, stroke, CKD mice)")}
L = [
    ("L1", "PMC4083087", "abstract", "EglN2 hydroxylates FOXO3a (edge EGLN2 -| FOXO3)", "EglN2 can hydroxylate FOXO3a on two specific prolyl residues in vitro and in vivo"),
    ("L2", "PMC4083087", "Results, Regulation of FOXO3a by EglN2 is HIF-independent", "pharmacological PHD inhibitors raise FOXO3a only where EglN2 is present; no isoform-selective agent used", "Treatment of T47D cells with various pharmacological prolyl hydroxylase inhibitors promoted the accumulation of FOXO3a in EglN2-proficient cells but did not further induce FOXO3a in cells already expressing high levels of FOXO3a by virtue of shRNA-mediated EglN2 depletion"),
    ("L3", "PMC4083087", "Figure 4 legend", "the agents named are non-selective (DMOG, DFO), none is desidustat", "1 mM DMOG, 200 μM DFO"),
    ("L4", "PMC6571149", "abstract", "Erk2 phosphorylation converts Bcl3 into a DNA-recruited coregulator (edge MAPK1 -> BCL3)", "Phosphorylation by Erk2 and IKK1/2 of Ser114 and Ser446 convert Bcl3 into a transcriptional coregulator by facilitating its recruitment to DNA"),
    ("L5", "PMC6571149", "abstract", "unphosphorylated Bcl3 removes p50/p52 from DNA (second possible sign route)", "Unphosphorylated Bcl3 acts as classical IκB-like inhibitor, removes p50 and p52 from bound DNA"),
    ("L6", "PMC6571149", "Results, Erk2 phosphorylation at Ser114", "ERK dependence shown in HeLa reporter cells, not in glia or macrophage TNF", "p52/Bcl3-driven luciferase activity was reduced in the presence of Erk inhibitor II (Figure 5A left panel) as well as in Erk2 KD HeLa cells"),
    ("L7", "PMC2854092", "abstract", "FOXO3 -> BNIP3 reference is a de-repression experiment in cardiomyocytes/U2OS (edge FOXO3 -> BNIP3)", "p8 RNAi increases FoxO3 association with bnip3 promoter, a known proautophagic FoxO3 target, resulting in higher bnip3 RNA and protein levels"),
    ("L8", "PMC7611345", "abstract/conclusions", "clinical development advised against", "The narrow therapeutic index and the pharmacokinetic profile led to recommend not developing this compound further"),
    ("L9", "PMC7611345", "Discussion", "ROCK is the more potent target (IC50 type, same panel as AKT)", "for ROCK I and ROCK 2 was 6 nM and 4 nM"),
    ("L10", "PMC7611345", "Results, Pharmacokinetics", "exposure at the maximum tolerated dose below preclinical efficacy levels", "At the tolerable dose of 180 mg free drug levels or exposure were below those measured in preclinical efficacy experiments"),
    ("L11", "PMC7611345", "Results, Safety", "hypotension attributed to ROCK inhibition (on-target)", "The most common known on-target toxicity of AT13148 included hypotension"),
    ("L12", "PMC12063501", "Results 3.3", "desidustat is a HIF-PH inhibitor (class action stated, isoform not measured)", "Desidustat, a hypoxia-inducible factor prolyl hydroxylase (HIF-PH) inhibitor"),
    ("L13", "PMC12063501", "Results 3.3", "neurological benefit in a stroke-CKD mouse model (not WWOX)", "desidustat-treated mice exhibited significantly improved neurological functioning on days 3, 7, 14, 21, and 28 following stroke compared to vehicle-treated mice"),
    ("L14", "PMC12063501", "Results 3.3", "the cited prior neuroprotection is attributed to PHD2 inhibition", "Previous studies have suggested that PHD2 inhibition exerts neuroprotective effects following stroke"),
    ("L15", "PMC12063501", "Discussion, limitations", "adult male mice only", "our current proof-of-concept study exclusively used male mice"),
]
FT = {k: flat(XML / f"{k}.xml") for k in ART}
loc = []
for lid, pmc, sec, ev, q in L:
    ok = q in FT[pmc]
    assert ok, (lid, q[:60])
    loc.append(dict(locator_id=lid, pmid=ART[pmc][0], source_artifact=f"{pmc} full-text XML (sha256 {sha(XML / (pmc + '.xml'))}; fetched 2026-11-03; not in git)", section=sec, evidence_for=ev, verbatim_quote=q, quote_verified_in_saved_text="yes (exact match after tag stripping and whitespace normalisation)"))
abs_chk = {"PMC7611345": ["MK2", "MAPKAP", "CDC25"], "PMC12063501": ["FOXO", "BNIP3", "EGLN"], "PMC6571149": ["TNF"]}
notes = {k: {s: len(re.findall(s, FT[k])) for s in v} for k, v in abs_chk.items()}
loc.append(dict(locator_id="N1", pmid="32616501", source_artifact="PMC7611345 full-text XML", section="whole text", evidence_for="ABSENCE locator (a string search, not a quote): no MK2/MAPKAP/CDC25 string in the first-in-human article text",
                verbatim_quote="(none) occurrences " + json.dumps(notes["PMC7611345"]), quote_verified_in_saved_text="search result"))
loc.append(dict(locator_id="N2", pmid="39914641", source_artifact="PMC12063501 full-text XML", section="whole text", evidence_for="ABSENCE locator: no HIF target gene, FOXO or BNIP3 readout in the desidustat stroke paper",
                verbatim_quote="(none) occurrences " + json.dumps(notes["PMC12063501"]), quote_verified_in_saved_text="search result"))
loc.append(dict(locator_id="N3", pmid="28689659", source_artifact="PMC6571149 full-text XML", section="whole text", evidence_for="ABSENCE locator: the Bcl3 phosphorylation paper contains one TNF string (introduction) and no TNF measurement",
                verbatim_quote="(none) occurrences " + json.dumps(notes["PMC6571149"]), quote_verified_in_saved_text="search result"))
tsv("locators_it22_p4_b1.tsv", ["locator_id", "pmid", "source_artifact", "section", "evidence_for", "verbatim_quote", "quote_verified_in_saved_text"], loc)

# 4 reading depth
DEPTH = [
    ("24990963", "PMC4083087", "EglN2/FOXO3a 2014 Genes Dev", "partial_fulltext_read (existing ledger event FTR-20261030-24990963-01); this package re-inspected abstract and selected passages and verified L1-L3; NO new receipt", "EGLN2 -| FOXO3; agents used were non-selective", "none (earlier receipt stands)"),
    ("28689659", "PMC6571149", "Bcl3 phosphorylation 2017 Mol Cell", "queried_not_full_read (selected passages of the open text via keyword search; abstract_only receipt FTR-20261103-28689659-01 exists)", "MAPK1 -> BCL3; sign routes; no TNF datum; L4-L6, N3", "receipts/FTR-20261103-28689659-02.json"),
    ("20181828", "PMC2854092", "p8/FoxO3/bnip3 2010 Mol Biol Cell", "abstract_only (text matched only for the two abstract quotes)", "FOXO3 -> BNIP3 reference; L7", "receipts/FTR-20261103-20181828-01.json"),
    ("32616501", "PMC7611345", "AT13148 first-in-human 2020 Clin Cancer Res", "partial_fulltext_read (Introduction, Methods, Results, Discussion read; figures, tables, supplement, references not read)", "AT-13148 ROCK/AKT profile, toxicity, no MK2 string; L8-L11, N1", "receipts/FTR-20261103-32616501-01.json"),
    ("39914641", "PMC12063501", "desidustat stroke CKD mice 2025 Exp Neurol", "partial_fulltext_read (Introduction through Conclusion read; figures, supplement, references not read)", "desidustat in CNS-relevant mouse model, class action, PK, no FOXO/BNIP3 readout; L12-L15, N2", "receipts/FTR-20261103-39914641-01.json"),
    ("22991226", "", "HDAC5 glucose uptake 2012 J Mol Endocrinol", "abstract_only (existing event FTR-20261103-22991226-01)", "HDAC5 knockdown lowers GLUT1 in muscle; pan-HDACi GLUT1 not stated", "none (existing receipt stands)"),
]
ABSR = {"15629715": ("10.1016/j.molcel.2004.11.021", "MAPKAP kinase-2 checkpoint kinase 2005 Mol Cell", "MK2 phosphorylates Cdc25B/C (Cdc25A not named in the abstract)"),
        "17292828": ("10.1016/j.ccr.2006.11.024", "p38MAPK/MK2 in p53-deficient cells 2007 Cancer Cell", "MK2 depletion abrogates the Cdc25A-mediated S-phase checkpoint in p53-deficient cells after cisplatin"),
        "21670150": ("10.1128/MCB.05523-11", "Cdc25A/Foxo1 breast cancer 2011 Mol Cell Biol", "Cdc25A enhances Foxo1 stability by dephosphorylating Cdk2 in breast cancer cells (full-text route returned an empty body)"),
        "16783365": ("10.1038/nn1731", "hypothalamic Foxo1 2006 Nat Neurosci", "hypothalamic Foxo1 stimulates NPY and AgRP transcription through PI3K/Akt"),
        "15465827": ("10.1074/jbc.M404246200", "BCL-3 and p50 2004 J Biol Chem", "BCL-3 with p50 attenuates LPS-induced TNFalpha in macrophages, HDAC1 recruitment"),
        "22798670": ("10.4049/jimmunol.1102803", "Cyclophilin B / Bcl-3 2012 J Immunol", "Bcl-3 induction reduces TNFalpha in LPS-stimulated macrophages; knockdown restores"),
        "22781553": ("10.1158/1078-0432.CCR-11-3313", "AT13148 multi-AGC inhibitor 2012 Clin Cancer Res", "AT13148 is a multi-AGC kinase inhibitor (AKT, p70S6K, PKA, ROCK, SGK); no MK2 named; a ChEMBL mechanism reference for MK2"),
        "25840982": ("10.1158/0008-5472.CAN-14-2156", "Rho kinase inhibitors block melanoma 2015 Cancer Res", "AT13148 inhibits ROCK1/2 in melanoma cells; no MK2 named; a ChEMBL mechanism reference for MK2"),
        "29360358": ("10.1021/acs.jmedchem.7b01465", "Fused pyrimidine hydroxamates 2018 J Med Chem", "document behind the pracinostat HDAC panel IC50 values in ChEMBL (abstract does not state them)"),
        "39383771": ("10.1016/j.lungcan.2024.107964", "naporafenib + rineterkib phase 1b 2024 Lung Cancer", "rineterkib is an ERK1/2 inhibitor; RDE 200 mg QD; DUSP6 mRNA -45.5% on treatment with naporafenib"),
        "38759372": ("10.1016/j.intimp.2024.112246", "SB939 EAE 2024 Int Immunopharmacol", "pracinostat (SB939) halts EAE in mice, neuronal IDO1-dependent"),
        "30841499": ("10.3390/ijms20051109", "HDACi BDNF neurite outgrowth 2019 Int J Mol Sci", "SB-939 raised BDNF expression and neurite outgrowth in hNPC-derived neurons"),
        "42415186": ("10.1186/s13148-026-02192-z", "HDACi safety in children 2026 Clin Epigenetics", "paediatric toxicity of six HDAC inhibitors incl. pracinostat, mainly haematological")}
for p, (doi, cite, use) in ABSR.items():
    DEPTH.append((p, "", cite, "abstract_only", use, f"receipts/FTR-20261103-{p}-01.json"))
for p, why in (("30290271", "seed paper (Wwox KO mouse hippocampus): NPY interneuron loss, Tnf/Il6 up; existing ledger events"), ("36828035", "seed paper (P47T mouse): neuroinflammation; existing ledger events"),
               ("34268881", "seed paper (organoid model); existing ledger events")):
    DEPTH.append((p, "", "(seed paper)", "abstract_only in this package (existing ledger events not re-read)", why, "none"))
for p, why in (("29191878", "Kd values (kinobeads) incl. MAPKAPK2 > 30000 nM: taken from the ChEMBL activity row only"), ("25637120", "pracinostat Ki panel: ChEMBL row only"), ("40263713", "desidustat enzyme panel: ChEMBL row only"),
               ("32791404", "review compilation of cell IC50: ChEMBL row only")):
    DEPTH.append((p, "", "(not read)", "title/ChEMBL row only; paper NOT read", why, "none"))
tsv("reading_depth_it22_p4_b1.tsv", ["pmid", "pmcid", "citation", "depth_in_this_package", "used_for", "receipt_prepared"], [dict(zip(["pmid", "pmcid", "citation", "depth_in_this_package", "used_for", "receipt_prepared"], d)) for d in DEPTH])

# 5 edge provenance
E = [
    ("IT21P2-0005", "pracinostat -| HDAC5", "GtoPdb IC50 47 nM; ChEMBL IC50 5113 nM (class IIa substrate) and Ki 21 nM", "29360358; 25637120", "enzyme panels", "ChEMBL rows (papers not read)", "human recombinant HDAC", "enzyme activity", "inhibition", "inhibits", "yes, but 109-fold disagreement between two IC50 sources", "measurement", "no", "HDAC5 350-468 cpm organoid", "CONFLICTING"),
    ("IT21P2-0005", "HDAC5 -T(+)-> SLC2A1", "CollecTRI/TRRUST/ExTRI2; 1 distinct reference", "22991226", "primary research", "abstract (existing receipt)", "human primary skeletal muscle cells, HDAC5 knockdown", "GLUT1 expression", "knockdown lowers GLUT1", "+", "yes", "measurement (one cell type)", "no (muscle)", "HDAC5 0.81x v SLC2A1 2.67x in KO organoid: association opposite", "WEAK"),
    ("IT21P2-0043", "desidustat -| EGLN2", "DGIdb/GtoPdb claim, no affinity", "40263713 (EGLN1 only)", "enzyme panel", "ChEMBL row (paper not read)", "human recombinant PHD2", "enzyme activity", "EGLN1/PHD2 IC50 1300 nM; EGLN2 not measured", "inhibits", "isoform not measured", "none for EGLN2", "no", "EGLN2 88-104 cpm; hNPC 21-115 TPM", "UNMEASURED"),
    ("IT21P2-0043", "EGLN2 -P(-)-> FOXO3", "SIGNOR; 1 reference", "24990963", "primary research, Genes Dev 2014", "partial full text (existing event) + passages", "T47D, MCF-7, MEFs; breast cancer", "FOXO3a protein stability", "EglN2 hydroxylation destabilises FOXO3a; non-selective PHD inhibitors raise it", "-", "yes", "measurement", "no (breast cancer)", "FOXO3 1.19x KO organoid (transcript)", "SUPPORTED_IN_OTHER_SYSTEM"),
    ("IT21P2-0043", "FOXO3 -T(+)-> BNIP3", "CollecTRI/CollecTRI2/ExTRI/DoRothEA; about 33 references, one read", "20181828", "primary research, Mol Biol Cell 2010", "abstract (text matched for quotes)", "cardiomyocytes, H9C2, U2OS; p8-/- mouse heart", "bnip3 RNA/protein", "p8 knockdown raises FoxO3 on the bnip3 promoter and bnip3 levels", "+", "yes (indirect, de-repression)", "measurement", "no", "BNIP3 1.38x KO organoid", "PARTLY_SUPPORTED"),
    ("IT21P2-0052", "AT-13148 -| MAPKAPK2", "ChEMBL curated mechanism (references: pipeline page, 22781553, 25840982); no activity row", "22781553; 25840982; 32616501 (text)", "preclinical and clinical papers", "abstracts; full text of 32616501", "n/a", "n/a", "no MK2 value; Kd > 30000 nM (kinobeads, 29191878)", "inhibits", "NOT SHOWN", "none", "no", "MAPKAPK2 136-157 cpm organoid; hNPC ABSENT", "UNSUPPORTED"),
    ("IT21P2-0052", "MAPKAPK2 -P(-)-> CDC25A", "SIGNOR + SPIKE; references 15629715, 17292828", "15629715; 17292828", "primary research", "abstracts", "mammalian cells, UV; p53-deficient cancer cells after cisplatin", "Cdc25B/C phosphorylation; Cdc25A-mediated S checkpoint", "MK2 depletion abrogates Cdc25A checkpoint", "-", "partly (15629715 names Cdc25B/C)", "measurement", "no", "CDC25A 1.50x KO organoid", "OTHER_SYSTEM"),
    ("IT21P2-0052", "CDC25A -P(+)-> FOXO1", "SIGNOR; 1 reference", "21670150", "primary research", "abstract", "breast cancer cells", "Foxo1 stability via Cdk2", "Cdc25A enhances Foxo1 stability", "+", "yes", "measurement", "no", "FOXO1 2.31x KO organoid", "OTHER_SYSTEM"),
    ("IT21P2-0052", "FOXO1 -T(+)-> NPY", "CollecTRI/DoRothEA/SIGNOR; 13 references, one read", "16783365", "primary research, Nat Neurosci 2006", "abstract", "mouse hypothalamus", "NPY/AgRP transcription", "Foxo1 stimulates NPY transcription through PI3K/Akt", "+", "yes", "measurement", "no (hypothalamic feeding circuit)", "NPY 0.01x KO organoid while FOXO1 up", "COUNTER_LOCAL"),
    ("IT21P2-0380", "rineterkib -| MAPK1", "DGIdb/GtoPdb claim; ChEMBL IC50 0.0261 nM (one patent document)", "patent US-9242996-B2", "biochemical", "ChEMBL row", "activated ERK2, 20 pM enzyme", "enzyme activity", "IC50 0.0261 nM; single measured target", "inhibits", "yes", "measurement", "no", "MAPK1 114-135 cpm organoid", "SINGLE_TARGET_NO_SELECTIVITY"),
    ("IT21P2-0380", "MAPK1 -P(+)-> BCL3", "SIGNOR; 1 reference", "28689659", "primary research, Mol Cell 2017", "queried_not_full_read", "HeLa, HEK293T, RAW 264.7", "Bcl3 phosphorylation and DNA recruitment", "Erk2 phosphorylates Bcl3 Ser114; Erk inhibitor II lowers p52/Bcl3 reporter", "+", "yes", "measurement", "no", "BCL3 4-7 cpm organoid; hNPC ABSENT", "OTHER_SYSTEM"),
    ("IT21P2-0380", "BCL3 -T(-)-> TNF", "CollecTRI family; the record carries stimulation AND inhibition; 15 references, two read", "15465827; 22798670", "primary research", "abstracts", "mouse/human macrophages, LPS", "TNF promoter/transcript", "Bcl-3 (with p50, HDAC1) represses LPS-induced TNF", "-", "yes (macrophage)", "measurement", "no", "TNF 0-0.03 cpm organoid; hNPC ABSENT", "OTHER_SYSTEM; MIXED_SIGN_IN_NETWORK"),
    ("IT21P2-0380", "ERK -> TNF (direct, competing)", "not in the chain; carried from the tizaterkib record (IT21P4A, title-level)", "(not re-read here)", "primary research", "title only (carried)", "macrophages", "TNF production", "ERK required for LPS-induced TNF", "+ (opposite to the chain)", "n/a", "carried", "no", "n/a", "UNRESOLVED_COMPETITOR"),
]
EC = ["proposal_id", "edge", "network_record", "reference_pmids_checked", "what_the_reference_is", "reading_depth", "system_species_tissue", "level", "sign_in_reference", "sign_in_network", "matches", "evidence_type", "disease_transferred", "local_data_check", "grade"]
tsv("edge_provenance_it22_p4_b1.tsv", EC, [dict(zip(EC, e)) for e in E])

# 6 raw digests
rh = []
for p in sorted(list(RAW.glob("mol_*.json")) + list(RAW.glob("mech_*.json")) + list(RAW.glob("act_*.json")) + [RAW / "at13148.json"] + list(RAW.glob("op_*.tsv")) + [XML / f"{k}.xml" for k in ART]):
    if p.exists():
        rh.append(dict(file=p.name, sha256=sha(p), bytes=p.stat().st_size, source="ChEMBL REST (ChEMBL_37 as served 2026-11-03)" if p.suffix == ".json" and "PMC" not in p.name else ("OmniPath interactions service 2026-11-03 (filters ignored by the service: filtered locally by gene symbol)" if p.suffix == ".tsv" else "NCBI PMC / Europe PMC full-text XML 2026-11-03")))
tsv("raw_hashes_it22_p4_b1.tsv", ["file", "sha256", "bytes", "source"], rh)

# 7 receipts (prepared files; nothing is appended)
COVA = {k: "unavailable" for k in ("introduction", "methods", "results", "figures", "tables", "discussion", "limitations", "supplementary", "references")}
COVA["abstract"] = "read"
WF = ("IT22 P4 batch 1 qualification (qualification_it22_p4_20261103/batch1). %s Prepared as a JSON file for the integrator; it was not appended at preparation time.")


def base(pmid, doi, n):
    return {"analysis_at": "2026-11-03T18:50:00Z", "analysis_time_precision": "minute", "event_at": "2026-11-03T19:10:00Z", "event_id": f"FTR-20261103-{pmid}-{n:02d}", "outputs": OUT,
            "prior_receipt": None, "record_kind": "contemporaneous_receipt", "reread_reason": "first_read", "study_id": {"doi": doi, "pmid": pmid}}


rc = []
for p, (doi, cite, use) in ABSR.items():
    r = base(p, doi, 1)
    r.update(coverage=COVA, evidence_depth="abstract_only", source_kind="abstract", source_fingerprint=None, source_locator=f"PubMed record for PMID {p} (abstract and metadata as served 2026-11-03)",
             evidence_basis=[f"abstract analysed in full ({cite}); used for one qualification fact: {use}", "no experimental detail absent from the abstract is used; statements carried into the tables are marked abstract-level",
                             "coverage uses `unavailable` for the sections not obtained: full text was not read in this package"],
             workflow=WF % "Abstract analysed for one fact of an edge or compound record; no full text was read.")
    rc.append(r)
r = base("20181828", "10.1091/mbc.e09-09-0818", 1)
r.update(coverage=COVA, evidence_depth="abstract_only", source_kind="abstract", source_fingerprint=None, source_locator="PubMed record for PMID 20181828 (abstract and metadata as served 2026-11-03)",
         evidence_basis=["abstract analysed in full (Mol Biol Cell 2010, p8 / FoxO3 / bnip3); used for one fact: p8 knockdown increases FoxO3 association with the bnip3 promoter and bnip3 levels (the FOXO3 -> BNIP3 reference of the desidustat chain)",
                         "the article text was fetched and the two abstract sentences were matched against it (locator L7); no other part of the text was read"],
         workflow=WF % "Abstract analysed for one fact of an edge record.")
rc.append(r)
CF = lambda **k: {**{x: "not_read" for x in ("introduction", "methods", "results", "figures", "tables", "discussion", "limitations", "supplementary", "references")}, "abstract": "read", **k}
r = base("28689659", "10.1016/j.molcel.2017.06.011", 2)
r.update(prior_receipt="FTR-20261103-28689659-01", reread_reason="new_question_outside_prior_coverage", coverage=CF(), evidence_depth="queried_not_full_read", source_kind="fulltext_remote", source_fingerprint=sha(XML / "PMC6571149.xml"),
         source_locator="PMC6571149 full-text XML as served by NCBI PMC (db=pmc), retrieved 2026-11-03",
         evidence_basis=["Selected passages of the open text inspected by keyword search (Erk inhibitor II, Erk2 knockdown, LPS/macrophage, TNF, MEK); the article was NOT read section by section, so every section other than the abstract is declared not_read",
                         "Question: does the Erk2 -> Bcl3 edge predict the sign of TNF change after ERK inhibition? Finding: ERK dependence of Bcl3 activity was shown in HeLa reporter cells; the paper has no TNF measurement (one TNF string, introduction)",
                         "Verbatim locators L4, L5, L6 and absence locator N3 are in locators_it22_p4_b1.tsv and were matched against the saved XML text (sha256 in source_fingerprint)"],
         workflow=WF % "Question-driven keyword reading of the open text after the earlier abstract-only event.")
rc.append(r)
r = base("32616501", "10.1158/1078-0432.CCR-20-0700", 1)
r.update(coverage={"abstract": "read", "introduction": "read", "methods": "read", "results": "read", "discussion": "read", "limitations": "not_present", "figures": "not_read", "tables": "not_read", "supplementary": "not_read", "references": "not_read"},
         evidence_depth="partial_fulltext_read", source_kind="fulltext_remote", source_fingerprint=sha(XML / "PMC7611345.xml"), source_locator="PMC7611345 full-text XML as served by NCBI PMC (db=pmc), retrieved 2026-11-03",
         evidence_basis=["coverage_map", "Peer-reviewed open article. NOT WWOX EVIDENCE: no neural, CNS or WWOX analysis.",
                         "Read end to end as flattened text: Introduction, Methods, Results (safety, PK, PD, efficacy), Discussion; figures, tables, supplementary files and the reference list were not read (the flattened text carries no table content)",
                         "Question: is MAPKAPK2 a documented target of AT-13148 and what is its measured profile in humans? Finding: no MAPKAP/MK2/CDC25 string; ROCK IC50 6 and 4 nM v AKT 38-402 nM; narrow therapeutic index, development not recommended",
                         "Verbatim locators L8-L11 and absence locator N1 are in locators_it22_p4_b1.tsv and were matched against the saved XML text"],
         workflow=WF % "Question-driven reading of the open article text.")
rc.append(r)
r = base("39914641", "10.1016/j.expneurol.2025.115181", 1)
r.update(coverage={"abstract": "read", "introduction": "read", "methods": "read", "results": "read", "discussion": "read", "limitations": "read", "figures": "not_read", "tables": "not_read", "supplementary": "not_read", "references": "not_read"},
         evidence_depth="partial_fulltext_read", source_kind="fulltext_remote", source_fingerprint=sha(XML / "PMC12063501.xml"), source_locator="PMC12063501 full-text XML as served by NCBI PMC (db=pmc), retrieved 2026-11-03",
         evidence_basis=["coverage_map", "Peer-reviewed open article. NOT WWOX EVIDENCE: adult male mice, adenine-CKD plus embolic stroke, human iMG cells.",
                         "Read end to end as flattened text: Introduction, Methods, Results, Discussion with its limitations paragraph; figures, supplement and reference list not read",
                         "Question: what is known of desidustat in neural tissue and does the paper measure HIF, FOXO3 or BNIP3? Finding: improved neurological scores and lower p-NFkB/ADAM17 in brain sections; mouse blood PK only; no HIF/FOXO/BNIP3 or EGLN isoform readout (absence locator N2)",
                         "Verbatim locators L12-L15 and N2 are in locators_it22_p4_b1.tsv and were matched against the saved XML text"],
         workflow=WF % "Question-driven reading of the open article text.")
rc.append(r)
(HERE / "receipts").mkdir(exist_ok=True)
for r in rc:
    json.dump(r, open(HERE / "receipts" / f"{r['event_id']}.json", "w"), indent=1, sort_keys=True)
    open(HERE / "receipts" / f"{r['event_id']}.json", "a").write("\n")
print("rows", len(RW.R), "typed", len(rows), "locators", len(loc), "receipts", len(rc), "raw", len(rh))
