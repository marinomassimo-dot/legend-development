#!/usr/bin/env python3
"""IT22 P4 batch2: writes locators_batch2.tsv and the receipts/ JSON files, after matching every verbatim quote against the text served on 2026-11-03.
  make_receipts_batch2.py --help
  make_receipts_batch2.py write TEXT_DIR      TEXT_DIR holds the served texts (PMC*.txt, abs_*.txt, vtama_label.txt); each quote must be found there (whitespace-normalised) or the script stops.
No receipt is appended to any ledger by this script."""
import sys, json, re, pathlib
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
D = pathlib.Path(__file__).resolve().parent
TXT = {"26199140": "PMC4525167.txt", "31888761": "PMC6937672.txt", "30329130": "PMC6326801.txt", "38297124": "PMC10881400.txt", "32049046": "PMC7321798.txt",
       "40607255": "PMC12210381.txt", "23240617": "PMC4540228.txt", "20486776": "PMC3128757.txt", "40494548": "PMC12782159.txt", "36523606": "PMC9745199.txt",
       "VTAMA": "vtama_label.txt"}
for p in ["23358665", "28595996", "15790560", "34713415", "40126804", "24673513", "38154665", "21741596", "26299268", "40945864", "39067626"]:
    TXT[p] = f"abs_{p}.txt"
# (id, pmid, paper, section, quote, what it is evidence for)
LOC = [
 ("L1", "26199140", "Cho 2015 Nat Commun (the only reference of the DOT1L -> MYC edge)", "Discussion", "Although DOT1L did not change the total level of c-Myc expression (Fig. 4e), c-Myc was recruited to the DOT1L-occupied region of EMT-TF promoters", "the edge's own reference reports no change in MYC level: the relation is co-binding at EMT-TF promoters in breast epithelial cells, not DOT1L raising MYC"),
 ("L2", "26199140", "Cho 2015", "Results", "The knockdown of c-Myc using siRNA blocked the increased EMT-TF expression caused by DOT1L overexpression in MCF10A cells", "MYC acts downstream of / with DOT1L on EMT-TFs (direction MYC needed for DOT1L effect), in MCF10A"),
 ("L3", "26199140", "Cho 2015", "Results", "inhibition of DOT1L enzymatic activity with EPZ004777 treatment reversed DOT1L-induced EMT-TF expression in MCF10A cells", "EPZ004777 was the tool in the edge reference, with an EMT-TF (not MYC) readout"),
 ("L4", "31888761", "Zhang 2019 Clin Epigenetics (colorectal cancer lines)", "Results", "both c-Myc RNA levels and protein levels were reduced after DOT1L silencing or inhibition", "a second, non-reference context in which DOT1L inhibition (EPZ004777) lowers MYC RNA and protein: the edge sign is context-dependent"),
 ("L5", "31888761", "Zhang 2019", "Results", "The results showed that 30 μM and 50 μM EPZ004777 significantly reduced cell viability of SW480 cells in a dose-dependent manner", "cell-level concentrations of tens of micromolar against a biochemical IC50 of 0.4 nM"),
 ("L6", "31888761", "Zhang 2019", "Results", "However, HCT116 was less sensitive to EPZ004777 treatment.", "sensitivity differs between lines"),
 ("L7", "30329130", "Franz 2019 Nucleic Acids Res (mouse cortex)", "Results", "Loss of DOT1L reduced the total number of PAX6- and SATB2-positive cells at E18.", "genetic Dot1l loss in telencephalon reduces progenitors (PAX6) and upper-layer neurons (SATB2); SATB2 is already lower in the WWOX-KO organoid"),
 ("L8", "30329130", "Franz 2019", "Abstract", "Loss of DOT1L results in reduced numbers of progenitors expressing genes including SoxB1 gene family members.", "DOT1L is required to keep progenitor numbers in mouse cortex"),
 ("L9", "38297124", "Ciceri 2024 Nature (human PSC-derived cortical neurons)", "Abstract", "Transient inhibition of EZH2, EHMT1 and EHMT2 or DOT1L, at progenitor stage primes newly born neurons to rapidly acquire mature properties upon differentiation.", "human-NPC datum pointing the other way: transient DOT1L inhibition accelerates neuronal maturation"),
 ("L10", "38297124", "Ciceri 2024", "Results", "Transient inhibition of EZH2, EHMT1/2 and DOT1L in NPCs using GSK343, UNC0638 and EPZ004777, respectively, induced increased NEFH and STX1A expression in d35 neurons", "EPZ004777 itself was used in human NPCs (dose and schedule not found in the text served)"),
 ("L11", "32049046", "Jiang 2020 Cancer Cell (the only reference of the AURKB -> MYC edge)", "Results", "indicating a specific regulation of (c-)MYC, but not N-MYC, by Aurora B kinase.", "AURKB-dependent stabilisation is c-MYC specific, N-MYC unchanged in neuroblastoma cells; neural progenitors rely heavily on MYCN"),
 ("L12", "32049046", "Jiang 2020", "Results", "Pharmacologic targeting of AURKB by AZD1152, which specifically suppresses AURKB autophosphorylation (Figure S1C), diminished MYC expression as well in multiple T-ALL cells", "the inhibitor used was AZD1152 (barasertib), not TAK-901; T-ALL cells"),
 ("L13", "32049046", "Jiang 2020", "Results", "In contrast, Jurkat and PEER cells were resistant to AZD1152 associated with unchanged MYC abundance", "even inside leukaemia the MYC response is not universal"),
 ("L14", "32049046", "Jiang 2020", "Results", "These data suggest that decrease in MYC expression is required for T-ALL cells to respond to AZD1152 and expression of functional FBXW7 predicts anti-T-ALL efficacy.", "the edge needs functional FBXW7-dependent degradation; FBXW7 status of WWOX-deficient radial glia is unknown"),
 ("L15", "40607255", "Melatonin / AhR-Nrf2 in microglia, Int J Biol Sci 2025", "Results", "Lentivirus transfection of AhR or FICZ significantly increased Nrf2 DNA-binding activity in LPS-treated cells", "AhR agonist (FICZ) raises Nrf2 DNA-binding in LPS-treated microglia (BV2 / primary): direction AhR -> NRF2 up in a neural cell type"),
 ("L16", "40607255", "Int J Biol Sci 2025", "Results", "In an EMSA, LPS decreased AhR-regulated Nrf2 binding, which was blocked by melatonin or FICZ at 4 hours.", "same, under inflammatory stimulus; not a basal or WWOX system"),
 ("L17", "23240617", "Latchney 2013 J Neurochem (adult hippocampal neurogenesis)", "Abstract", "AhR-deficient mice displayed reduced cell birth, decreased cell survival, and diminished neuronal differentiation in the DG.", "AhR is needed for normal adult neurogenesis (both loss and activation are adverse in this paper)"),
 ("L18", "23240617", "Latchney 2013", "Abstract", "Following TCDD exposure, wild-type mice exhibited impaired hippocampal-dependent contextual memory, decreased cell birth, reduced neuronal differentiation, and fewer mature neurons in the DG.", "adverse effects of AhR activation by a persistent agonist (TCDD); not transferable to a rapidly metabolised ligand without a measurement"),
 ("L19", "20486776", "Neural precursor cells and TCDD, Stem Cells Dev 2011", "Abstract", "TCDD suppresses NPC proliferation in a concentration-dependent manner without the loss of cell viability", "AhR activation by TCDD slows NPC proliferation (G1 arrest) in vitro: abstract level"),
 ("L20", "36523606", "AHR modulation in zebrafish brain, Front Mol Neurosci 2022", "Abstract", "Early embryonic TCDD exposure impaired embryonic brain morphogenesis, resulted in ventriculomegaly, and disrupted neural connectivity", "developmental neural hazard of AhR agonism (TCDD), abstract level"),
 ("A1", "23358665", "Farrell 2013 Mol Cancer Ther (TAK-901 characterisation)", "Abstract", "TAK-901 exhibited time-dependent, tight-binding inhibition of Aurora B, but not Aurora A.", "primary description of TAK-901 selectivity between Aurora kinases (differs from the ChEMBL AURKA/TPX2 IC50 of 21 nM)"),
 ("A2", "23358665", "Farrell 2013", "Abstract", "TAK-901 suppressed cellular histone H3 phosphorylation and induced polyploidy.", "documented cellular engagement and the expected mitotic-failure phenotype"),
 ("A3", "23358665", "Farrell 2013", "Abstract", "In various human cancer cell lines, TAK-901 inhibited cell proliferation with effective concentration values from 40 to 500 nmol/L.", "cellular potency range (cancer lines)"),
 ("A4", "23358665", "Farrell 2013", "Abstract", "TAK-901 potently inhibited only a few kinases other than Aurora B in intact cells, including FLT3 and FGFR2.", "off-targets in intact cells named by the authors"),
 ("A5", "28595996", "Smith 2017 J Invest Dermatol (tapinarof)", "Abstract", "tapinarof binds and activates AhR in multiple cell types, including cells of the target tissue-human skin", "AhR agonism of the compound (primary)"),
 ("A6", "28595996", "Smith 2017", "Abstract", "tapinarof has no impact on imiquimod-induced skin inflammation in AhR-deficient mice", "the anti-inflammatory effect in skin depends on AhR"),
 ("A7", "15790560", "Miao 2005 J Biol Chem (the AHR -> NFE2L2 edge)", "Abstract", "Cells with silenced AHR expression using siRNA also lost NRF2 mRNA induction by 2,3,7,8-tetrachlorodibenzo-p-dioxin.", "AHR-dependence of NRF2 transcript induction (TCDD, XRE-like elements in the mouse Nrf2 promoter); cell type not named in the abstract"),
 ("A8", "34713415", "Tapinarof maximal use trial, Am J Clin Dermatol 2022", "Abstract", "Tapinarof plasma exposure was low, with the majority of concentrations being below detectable limits.", "systemic exposure after topical use in adults"),
 ("A9", "40126804", "Tapinarof paediatric maximal usage trial, Am J Clin Dermatol 2025", "Abstract", "Mean maximum plasma concentration (Cmax) was 2.44 ng/mL", "highest systemic exposure figure found (children 2 years and older, extensive atopic dermatitis); total plasma, not brain"),
 ("A10", "24673513", "Benvitimod healthy-subject study, Br J Dermatol 2014 (as indexed)", "Abstract", "Following topical application, systemic absorption was negligible.", "systemic absorption in healthy subjects"),
 ("A11", "38154665", "Tapinarof clinical review, J Allergy Clin Immunol 2024", "Abstract", "avoiding systemic safety concerns, drug interactions, or off-target effects", "a review's claim about local exposure (a claim, not a measurement; the same abstract says AhR may be a target in nervous system diseases)"),
 ("A12", "40945864", "Tapinarof AhR/Nrf2 in HaCaT, Toxicol Appl Pharmacol 2025", "Abstract", "Tapinarof potentiated PM-induced CYP1A1 and HO-1 expression, confirming AhR/Nrf2 activation.", "tapinarof activates the NRF2 arm in human keratinocytes (skin, not neural)"),
 ("A13", "40945864", "Tapinarof AhR/Nrf2 in HaCaT 2025", "Abstract", "This dual pathway activation protected cells from PM-induced oxidative stress and cell death, as validated using the AhR antagonist, CH223191, and Nrf2 inhibitor, brusatol.", "protection needed both arms in that model; whether NRF2 activation is downstream of AhR was not separated in the abstract"),
 ("A14", "39067626", "Tapinarof redox chemistry and phototoxicity, Free Radic Biol Med 2024", "Abstract", "tapinarof, being a moderate electron donor, is able to scavenge the ABTS radical and inhibit lipid peroxidation.", "the molecule has intrinsic redox chemistry: an AhR-independent route to NRF2 tone cannot be excluded"),
 ("A15", "39067626", "Free Radic Biol Med 2024", "Abstract", "In aqueous media at pH 7.4, we observed an ∼50 % degradation of tapinarof after 48 h at laboratory temperature.", "chemical instability in aqueous medium: an in vitro dosing problem for multi-day neural cultures"),
 ("A16", "26299268", "Roidl 2016 Stem Cells (cortical NSCs)", "Abstract", "The pharmacological inhibition and shRNA-mediated knockdown of DOT1L impaired proliferation and survival of NSCs.", "DOT1L is needed for proliferation and survival of cortical neural stem cells in vitro"),
 ("A17", "40494548", "DOT1L loss and neurodevelopmental disorder, Brain 2026", "Abstract", "In primary cortical neurons, Dot1l knockdown disrupts transcription of synaptic genes, neuron branching, expression of a synaptic protein and neuronal activity.", "human monoallelic DOT1L loss-of-function variants are linked to a neurodevelopmental disorder; neuronal, not progenitor, readouts"),
 ("A18", "21741596", "Daigle 2011 Cancer Cell (EPZ004777)", "Abstract", "Exposure of leukemic cells to EPZ004777 results in selective killing of those cells bearing the MLL gene translocation, with little effect on non-MLL-translocated cells.", "the compound's primary description: MLL-r-selective cytotoxicity"),
 ("D1", "VTAMA", "VTAMA (tapinarof) cream US label, DailyMed set id 9309d20f-8cd4-4c96-93fa-7f730e83c7ab, SPL version 4, 2025-07-30", "12.3", "Plasma concentration of tapinarof was below the quantifiable limits (BQL) of the assay (lower limit of quantification was 50 pg/mL) in 68% of the PK samples.", "adult plaque psoriasis maximal use"),
 ("D2", "VTAMA", "VTAMA label", "12.3", "Human plasma protein binding of tapinarof is approximately 99% in vitro.", "high protein binding: free systemic fraction is small"),
 ("D3", "VTAMA", "VTAMA label", "12.1", "Tapinarof is an aryl hydrocarbon receptor (AhR) agonist. The specific mechanisms by which VTAMA cream exerts its therapeutic actions are unknown.", "label states AhR agonism and that the mechanism of therapeutic action is unknown"),
 ("D4", "VTAMA", "VTAMA label", "8.1", "No tapinarof-related effects on postnatal development, neurobehavioral or reproductive performance of offspring were noted at doses up to 30 mg/kg/day", "rat reproductive study, subcutaneous dosing; offspring neurobehaviour: the only developmental neural-adjacent safety datum found, not a brain-exposure measurement"),
]
def norm(s): return re.sub(r"\s+", " ", s).strip()
def check(textdir):
    bad = []
    for lid, pm, _, _, q, _ in LOC:
        t = norm((textdir / TXT[pm]).read_text(encoding="utf8"))
        if norm(q) not in t: bad.append((lid, pm))
    return bad
# receipts: paper -> (doi, depth, coverage overrides, question, basis text, locator ids, source_kind, source_locator)
def cov(abstract="read", **kw):
    c = {k: "not_read" for k in ["introduction", "methods", "results", "discussion", "figures", "tables", "supplementary", "references", "limitations"]}
    c["abstract"] = abstract; c["figures"] = "unavailable"; c["supplementary"] = "unavailable"
    c.update(kw); return c
ABS = {k: "unavailable" for k in ["introduction", "methods", "results", "discussion", "limitations", "figures", "tables", "supplementary", "references"]}; ABS["abstract"] = "read"
P = {
 "26199140": ("10.1038/ncomms8821", "partial_fulltext_read", cov(introduction="read", results="read", discussion="read"), "Does the only reference of the DOT1L -> MYC edge show that DOT1L changes MYC level or activity in a way an inhibitor would reverse?", "Open article (Nat Commun 2015, human breast epithelial and cancer cell lines). NOT WWOX EVIDENCE. Read: abstract, two introduction paragraphs, the results sections on DOT1L and EMT-TFs and on c-Myc as prerequisite, and the discussion paragraphs on c-Myc; methods, figures and supplement not read.", ["L1", "L2", "L3"], "fulltext_remote", "Europe PMC full-text XML for PMC4525167, rendered to text, 2026-11-03; bytes not saved to the repository"),
 "31888761": ("10.1186/s13148-019-0778-y", "partial_fulltext_read", cov(results="read"), "Does DOT1L inhibition by EPZ004777 lower MYC (RNA, protein) in any cell system, at what concentration?", "Open article (Clin Epigenetics 2019, colorectal cancer lines and xenografts). NOT WWOX EVIDENCE. Read: abstract, the results section 'DOT1L silencing or inhibition demethylates H3K79 and suppresses transcription of c-Myc' in full, and the EPZ004777 concentration passages by keyword search; the other results sections, methods and discussion were not read in full.", ["L4", "L5", "L6"], "fulltext_remote", "Europe PMC full-text XML for PMC6937672, rendered to text, 2026-11-03; bytes not saved to the repository"),
 "30329130": ("10.1093/nar/gky953", "partial_fulltext_read", cov(), "What does genetic Dot1l loss do to progenitor numbers and SATB2 neurons in mouse cortex?", "Open article (Nucleic Acids Res 2019, mouse). NOT WWOX EVIDENCE. Read: abstract and the passages on PAX6, SATB2 and the inhibitors SGC0946 / EPZ5676 found by keyword search (no results section read in full); methods, figures and supplement not read.", ["L7", "L8"], "fulltext_remote", "Europe PMC full-text XML for PMC6326801, rendered to text, 2026-11-03; bytes not saved to the repository"),
 "38297124": ("10.1038/s41586-023-06984-8", "partial_fulltext_read", cov(), "Was EPZ004777 or DOT1L inhibition tested in human NPCs, and what did it do?", "Open article (Nature 2024, human PSC-derived cortical neurons). NOT WWOX EVIDENCE. Read: abstract and the passages naming DOT1L, EPZ004777, GSK343 found by keyword search; no section read in full; the dose and schedule of EPZ004777 were not found in the text served; figures and extended data not read.", ["L9", "L10"], "fulltext_remote", "Europe PMC full-text XML for PMC10881400, rendered to text, 2026-11-03; bytes not saved to the repository"),
 "32049046": ("10.1016/j.ccell.2020.01.001", "partial_fulltext_read", cov(results="read"), "Which inhibitor, cell types and MYC family member does the AURKB -> MYC edge reference establish, and is the effect general?", "Open article (Cancer Cell 2020, T-ALL cells, patient-derived xenografts). NOT WWOX EVIDENCE. Read: abstract, the results section 'AURKB inhibition destabilizes MYC' in full, and the AZD1152 / FBXW7 / N-MYC passages found by keyword search; the other sections, STAR methods and supplement not read.", ["L11", "L12", "L13", "L14"], "fulltext_remote", "NCBI PMC efetch XML for PMC7321798, rendered to text, 2026-11-03; bytes not saved to the repository"),
 "40607255": ("10.7150/ijbs.105081", "partial_fulltext_read", cov(), "In microglia, does an AhR agonist raise Nrf2 activity (direction of the AhR -> NRF2 edge in a neural cell type)?", "Open article (Int J Biol Sci 2025, BV2 / primary microglia, mouse). NOT WWOX EVIDENCE. Read: abstract, introduction opening and the AhR / Nrf2 / FICZ passages found by keyword search; methods, figures and the in vivo part not read. Compound used is melatonin and FICZ, not tapinarof.", ["L15", "L16"], "fulltext_remote", "Europe PMC full-text XML for PMC12210381, rendered to text, 2026-11-03; bytes not saved to the repository"),
 "23240617": ("10.1111/jnc.12130", "abstract_only", ABS, "Is AhR activation or loss adverse for neurogenesis in the adult brain?", "Abstract analysed in full (plus the first introduction paragraph of the PMC text); used for one qualification fact: both AhR deletion and TCDD activation impaired hippocampal neurogenesis in mice. NOT WWOX EVIDENCE.", ["L17", "L18"], "fulltext_remote", "PMC4540228 via NCBI PMC efetch, 2026-11-03 (only the abstract and introduction opening were used)"),
 "20486776": ("10.1089/scd.2009.0529", "abstract_only", ABS, "Does AhR activation by TCDD change neural precursor proliferation?", "Abstract analysed in full; the PMC record served was the abstract only. NOT WWOX EVIDENCE.", ["L19"], "abstract", "PubMed / PMC record for PMID 20486776 (abstract as served 2026-11-03)"),
 "36523606": ("10.3389/fnmol.2022.1032302", "abstract_only", ABS, "Is AhR activation by an agonist adverse for embryonic brain development in a vertebrate model?", "Abstract analysed (the first part as printed); the PMC text was retrieved but not read beyond the abstract. NOT WWOX EVIDENCE.", ["L20"], "abstract", "PubMed record for PMID 36523606 (abstract as served 2026-11-03)"),
 "40494548": ("10.1093/brain/awaf212", "abstract_only", ABS, "Is DOT1L loss linked to a human neurodevelopmental disorder?", "Abstract analysed in full; the PMC record served contained the abstract only. NOT WWOX EVIDENCE.", ["A17"], "abstract", "PMC12782159 via NCBI PMC efetch, 2026-11-03 (abstract only)"),
}
for p, why in {"23358665": "primary characterisation of TAK-901: selectivity, cellular engagement, phenotype", "28595996": "primary identification of tapinarof as an AhR agonist", "15790560": "the AHR -> NFE2L2 transcriptional edge",
               "34713415": "systemic exposure of tapinarof after topical use (adult maximal use)", "40126804": "systemic exposure of tapinarof in children (maximal use)", "24673513": "systemic absorption of benvitimod (tapinarof) in healthy subjects",
               "38154665": "a review's statement on local exposure and AhR as a neurological target (claim only)", "21741596": "primary description of EPZ004777 selectivity for MLL-rearranged cells",
               "26299268": "DOT1L need in cortical neural stem cells", "40945864": "tapinarof activation of AhR and NRF2 arms in keratinocytes", "39067626": "tapinarof redox chemistry, stability and phototoxicity"}.items():
    P[p] = (None, "abstract_only", ABS, why + "?", f"Abstract analysed in full; used for one labelled fact ({why}); no full text was obtained. NOT WWOX EVIDENCE.", [], "abstract", f"PubMed record for PMID {p} (abstract and metadata as served 2026-11-03)")
DOI = {}
def doi_from_xml(textdir, pm):
    f = textdir / f"abs_{pm}.xml"
    if not f.exists(): return None
    m = re.search(r'<ArticleId IdType="doi">([^<]+)</ArticleId>', f.read_text(encoding="utf8"))
    return m.group(1) if m else None
LIDS = {}
for l in LOC: LIDS.setdefault(l[1], []).append(l)
OUT = [f"disease-models/wwox/research/drug_repurposing/qualification_it22_p4_20261103/batch2/{f}" for f in ("README.md", "qualification_it22_p4_batch2.tsv")]
def write(textdir):
    bad = check(textdir)
    if bad: raise SystemExit(f"quotes not found verbatim: {bad}")
    L = ["locator_id\tpmid_or_source\tpaper\tsection\tverbatim_quote\twhat_it_is_evidence_for"] + ["\t".join(r) for r in LOC]
    (D / "locators_batch2.tsv").write_text("\n".join(L) + "\n")
    (D / "receipts").mkdir(exist_ok=True)
    n = 0
    for pm, (doi, depth, cv, q, basis, lids, sk, sl) in P.items():
        ev = ["coverage_map", basis]
        for l in LIDS.get(pm, []):
            if l[0] in lids or depth == "abstract_only" or True:
                ev.append(f"locator {l[0]} ({l[3]}), verbatim: \"{l[4]}\"")
        d = {"analysis_at": "2026-11-03T14:30:00Z", "analysis_time_precision": "minute", "coverage": cv, "event_at": "2026-11-03T14:40:00Z", "event_id": f"FTR-20261103-{pm}-01",
             "evidence_basis": ev, "evidence_depth": depth, "outputs": OUT, "prior_receipt": None, "record_kind": "contemporaneous_receipt", "reread_reason": "first_read",
             "source_fingerprint": None, "source_kind": sk, "source_locator": sl, "study_id": {"doi": doi or doi_from_xml(textdir, pm), "pmid": pm},
             "workflow": "IT22 P4 batch2 qualification (qualification_it22_p4_20261103/batch2), question-driven: " + q + " Prepared as a JSON file for the integrator; was not appended by the preparing actor. The served text was not snapshotted to files/, so locator text cannot be machine-matched against a local artefact; the quotes were matched against the text as served at preparation time."}
        (D / "receipts" / f"FTR-20261103-{pm}-01.json").write_text(json.dumps(d, indent=1, sort_keys=True) + "\n"); n += 1
    print("locators", len(LOC), "receipts", n)
if sys.argv[1] == "write": write(pathlib.Path(sys.argv[2]))
