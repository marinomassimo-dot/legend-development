#!/usr/bin/env python3
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print("IT22 P6 EZH2/glia dossier builder (make_ezh2_glia_p6_it22.py); run with no argument from this folder; writes only files next to it.")
    raise SystemExit(0)
"""IT22 P6 EZH2/glia qualification: writes locators, receipts. Run: python3 make_ezh2_glia_p6_it22.py write"""
import json, sys, pathlib
D = pathlib.Path(__file__).resolve().parent
OUT = ["disease-models/wwox/research/drug_repurposing/qualification_it22_p6_20261103/ezh2_glia/README.md",
       "disease-models/wwox/research/drug_repurposing/qualification_it22_p6_20261103/ezh2_glia/qualification_ezh2_glia_it22_p6.tsv"]
LOC = [
 ("L1","29132376","Yin 2017 J Neuroinflammation","Methods","The EZH2 functional inhibitor, DZNep, was purchased from Sigma-Aldrich.","the edge reference used DZNep and siEZH2, not GSK343 or any selective catalytic inhibitor"),
 ("L2","29132376","Yin 2017","Results","The qPCR results showed that knockdown of EZH2 in GBM cells induced decline of TGFβ1-3 and IL10 and elevation of IL1β and IL6","IL1B and IL6 rise was measured in the glioblastoma cell lines, not in microglia"),
 ("L3","29132376","Yin 2017","Results","significant increase of TNFα and iNOS were observed with no change of IL1β, IL6, and CD11c in microglia co-cultivated with murine GBM cells pre-treated with siEZH2 and DZNep","in microglia, IL1B and IL6 did not change; TNF and iNOS rose only indirectly (microglia exposed to EZH2-suppressed tumour-cell medium)"),
 ("L4","29132376","Yin 2017","Results","mRNA levels of some cytokines such as IL12α, TNFα, IFNγ, and iNOS are too low to detect in three GBM cell lines by qPCR","TNF was not measurable in the tumour cells: the TNF rise is a microglial readout"),
 ("L5","37391829","Mannino 2023 J Neuroinflammation","Background","Concerning GSK-343, little is known about its ability to cross the BBB","no brain exposure of GSK343 is measured; the paper states the gap itself"),
 ("L6","37391829","Mannino 2023","Methods","The levels of IL-1β, IL-2, IL-6, and IL-17A were evaluated on brain tissues extracts","cytokines were read by ELISA in whole-tissue extracts: no cell-type attribution (microglia v astrocyte v neuron)"),
 ("L7","37391829","Mannino 2023","Results","GSK-343 (1 mg/kg, 5 mg/kg and 10 mg/kg) administration demonstrated its ability to significantly reduce cytokine levels in a dose-dependent manner, compared to MPTP-injected mice","cytokine fall under GSK343 in an injury model (MPTP, adult CD1 male), against an MPTP-raised baseline"),
 ("L8","37391829","Mannino 2023","Methods","Experimental data regarding sham groups + GSK-343 1, 5 and 10 mg/kg, besides behavioral tests, were not shown","the effect of GSK343 on cytokines in uninjured animals is not shown, so a cytokine effect without the injury is not documented"),
 ("L9","32937136","Wang 2020 Cell Rep","Results","These results indicate that the generation of OLs, not OPCs, is delayed in the absence of Ezh2.","Ezh2 loss alone delays oligodendrocyte generation (recovered by P10)"),
 ("L10","32937136","Wang 2020","Results","PRC2 is required for the formation of OLs, but not for the generation of OPCs, and that PRC2-Ezh1 and PRC2-Ezh2 act redundantly to promote postnatal myelination within the CNS in mice.","dual PRC2 loss (Eed) gives no recovery of myelination: EZH1 compensates for EZH2"),
 ("L11","32937136","Wang 2020","Results","both Notch inhibition and Wnt inhibition significantly rescued Mbp expression and OL morphology in the Eed null OL lineage","mechanism of the block: de-repressed Notch and Wnt; a Wnt/Notch restraint rescues it in this model"),
 ("L12","32937136","Wang 2020","Discussion","Thus, boosting PRC2 activity to repress Notch-NFIA and Wnt may represent a novel therapeutic venue to facilitate remyelination in adults.","the authors' own therapeutic reading is the opposite of PRC2 inhibition for the myelin axis"),
 ("L13","32937136","Wang 2020","Results","Mbp/Plp1OLs were markedly reduced at P3 and did not recover even at P10 in the spinal cord","(text-extraction note: italics and genotype names were stripped in the served text) Eed cKO: no recovery at P10; death P13-P17 stated in the same section"),
 ("A1","25868794","ABCB1 and ABCG2 restrict the brain penetration of a panel of novel EZH2-Inhibitors; Int J Cancer 2015","abstract","All EZH2 inhibitors are transported by P-gp and BCRP","abstract level: five compounds incl. GSK343, GSK126, EPZ-6438"),
 ("A2","25868794","Int J Cancer 2015","abstract","the oral bioavailability of GSK126 is only 0.2% in WT mice, which increases to 14.4% in Abcb1;Abcg2 knockout mice","abstract level"),
 ("A3","25868794","Int J Cancer 2015","abstract","the brain accumulation of EPZ-6438 is limited by P-gp only and efflux of EPZ-6438 was completely abrogated by elacridar","abstract level; EPZ-6438 = tazemetostat"),
 ("A4","35300079","Liang 2022 ACS Med Chem Lett","abstract","the current array of EZH2 inhibitors have poor brain penetrance","abstract level: a statement by the authors, supported inside the paper by data not read here"),
 ("A5","37228094","Pediatric MATCH APEC1621C 2023","abstract","The most frequent diagnoses were atypical teratoid rhabdoid tumor (n = 8) and malignant rhabdoid tumor (n = 4).","abstract level: children with CNS tumours were dosed; no CNS pharmacokinetics in the abstract"),
]
COV_ABS = {k:"unavailable" for k in ["discussion","figures","introduction","limitations","methods","references","results","supplementary","tables"]}; COV_ABS["abstract"]="read"
def cov_partial(**kw):
    c = {"abstract":"read","introduction":"read","methods":"read","results":"read","discussion":"read","limitations":"not_present",
         "figures":"unavailable","tables":"not_present","supplementary":"unavailable","references":"not_read"}
    c.update(kw); return c
PAPERS = {
 "29132376":dict(doi="10.1186/s12974-017-0993-4",pmc="PMC5684749",depth="partial_fulltext_read",cov=cov_partial(),
   q="Which EZH2 inhibitor was used in this edge reference, in which cell type were IL1B/IL6/TNF measured, and did the sign reach microglia directly?",
   basis=["Peer-reviewed open article (J Neuroinflammation 2017). NOT WWOX EVIDENCE.","Read: abstract, introduction, methods, results, discussion and conclusions in the PMC article text as served by the PubMed full-text tool; the figure images and legends, and the additional files, were not served and were not read; the article has no limitations section. Locators L1-L4 are in locators_ezh2_glia_it22_p6.tsv."]),
 "37391829":dict(doi="10.1186/s12974-023-02842-6",pmc="PMC10311910",depth="partial_fulltext_read",cov=cov_partial(),
   q="What exactly was measured for GSK343 in the brain (cytokine matrix, cell type, exposure, uninjured controls)?",
   basis=["Peer-reviewed open article (J Neuroinflammation 2023, MPTP mouse). NOT WWOX EVIDENCE.","Read: abstract, background, methods, results, discussion and conclusions in the PMC article text as served; figures and their statistics (the paper reports densitometry and ELISA in figures) were not served and were not read, so effect sizes and n per group are NOT taken from it. Locators L5-L8."]),
 "32937136":dict(doi="10.1016/j.celrep.2020.108147",pmc="PMC8070886",depth="partial_fulltext_read",cov=cov_partial(),
   q="Does loss of PRC2 (Ezh2, Ezh1, Eed) alter oligodendrocyte-lineage differentiation, by which mechanism, and does Ezh1 compensate?",
   basis=["Peer-reviewed open article (Cell Rep 2020, mouse and chick). NOT WWOX EVIDENCE: no Wwox manipulation.","Read: abstract, introduction, results, discussion and STAR methods in the PMC article text as served; figures, key resources table and supplementary items were not served and were not read; italic gene and genotype names were stripped in the served text, so some sentences are garbled (genotype labels missing). Locators L9-L13."]),
 "25868794":dict(doi="10.1002/ijc.29566",pmc=None,depth="abstract_only",cov=COV_ABS,
   q="Do ABCB1/ABCG2 restrict brain penetration of the EZH2 inhibitors (GSK343, GSK126, EPZ-6438)?",
   basis=["abstract analysed in full; no PMC full text found in the PubMed record; used for one fact: efflux-transporter substrate status and mouse brain-penetration limits (abstract-level).","no experimental detail absent from the abstract is used; no tissue-to-plasma value is quoted."]),
 "35300079":dict(doi="10.1021/acsmedchemlett.1c00448",pmc="PMC8919293",depth="abstract_only",cov=COV_ABS,
   q="Is a brain-penetrant EZH2 inhibitor documented, and what does the paper say of the existing inhibitors?",
   basis=["abstract analysed in full; used for the authors' statement that current EZH2 inhibitors have poor brain penetrance and that TDI-6118 is a brain-penetrant EZH2 inhibitor (abstract-level).","a PMC full text exists; it was not read in this package."]),
 "37228094":dict(doi="10.1093/jnci/djad085",pmc="PMC11009504",depth="abstract_only",cov=COV_ABS,
   q="Was tazemetostat given to children with CNS tumours, and is any CNS exposure reported?",
   basis=["abstract analysed in full; used for: 20 patients aged 1-21, 8 atypical teratoid rhabdoid tumours, one objective response (non-Langerhans histiocytosis), no CNS exposure reported in the abstract.","a PMC full text exists; it was not read in this package, so tolerability and any CSF/brain data are UNVERIFIED."]),
}
PRIOR = {"29132376":"FTR-20261103-29132376-01","37391829":"FTR-20261103-37391829-01"}  # IT21 P4a abstract-only events
def write():
    L = ["locator_id\tpmid\tpaper\tsection\tverbatim_quote\twhat_it_is_evidence_for"]
    for r in LOC: L.append("\t".join(r))
    (D/"locators_ezh2_glia_it22_p6.tsv").write_text("\n".join(L)+"\n")
    rd = D/"receipts"; rd.mkdir(exist_ok=True)
    for pmid,p in PAPERS.items():
        if pmid=="25868794": continue  # abstract-only receipt FTR-20261103-25868794-01 already exists (IT21 P4a)
        fulltext = p["depth"]!="abstract_only"
        r = {"analysis_at":"2026-11-03T12:00:00Z","analysis_time_precision":"minute","coverage":p["cov"],
             "event_at":"2026-11-03T12:10:00Z","event_id":f"FTR-20261103-{pmid}-02",
             "evidence_basis":(["coverage_map"] if fulltext else [])+p["basis"],
             "evidence_depth":p["depth"],"outputs":OUT,"prior_receipt":PRIOR.get(pmid),"record_kind":"contemporaneous_receipt",
             "reread_reason":"inadequate_prior_coverage" if pmid in PRIOR else "first_read",
             "source_fingerprint":None,"source_kind":"fulltext_remote" if fulltext else "abstract",
             "source_locator":(f"PubMed Central {p['pmc']} article text via the PubMed full-text tool, 2026-11-03; bytes were not saved locally" if fulltext else f"PubMed record for PMID {pmid} (abstract and metadata as served 2026-11-03)"),
             "study_id":{"doi":p["doi"],"pmid":pmid},
             "workflow":"IT22 P6 EZH2/glia qualification (qualification_it22_p6_20261103/ezh2_glia), question-driven: "+p["q"]+" Prepared as a JSON file for the integrator; was not appended by the preparing actor."+(" The article text was not snapshotted to files/, so locator text cannot be machine-matched against a local artefact; source_kind is fulltext_remote for that reason." if fulltext else "")}
        (rd/f"{r['event_id']}.json").write_text(json.dumps(r,indent=1,sort_keys=True)+"\n")
if __name__=="__main__" and sys.argv[1:]==["write"]: write()
