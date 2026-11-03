#!/usr/bin/env python3
"""IT21 P4a: prepares FULLTEXT_READ_RECEIPT JSON files (one partial full-text reading, abstract-only receipts for the abstracts that decided an edge) in receipts/.
  make_receipts_p4a_it21.py write    writes receipts/*.json (NOT appended to the ledger; the integrator records them in event-ID order after a dry run)
Each file passes `fulltext_receipts.py record --receipt <file> --dry-run`. Appending stales ranking/coverage/reading_state, which is why this package hands the files back."""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = "disease-models/wwox/research/drug_repurposing/qualification_it21_p4a_20261103"
OUT = [f"{PKG}/README.md", f"{PKG}/qualification_it21_p4a.tsv", f"{PKG}/edge_provenance_it21_p4a.tsv"]

ABS = {   # pmid: (doi, citation, what the abstract was used for)
    "22190494": ("10.1073/pnas.1105304109", "Menssen 2012 PNAS", "sign of SIRT1 on c-MYC (SIRT1 stabilises and promotes c-MYC): counter-evidence to the SIRT1 -> MYC (-) edge"),
    "19364925": ("10.1083/jcb.200809167", "Yuan 2009 J Cell Biol", "sign of SIRT1 on c-Myc (SIRT1 decreases stability): supports the SIRT1 -> MYC (-) edge at protein level"),
    "29132376": ("10.1186/s12974-017-0993-4", "Yin 2017 J Neuroinflammation", "cited reference of EZH2 -> IL6/TNF reporting that EZH2 inhibition raises IL6, IL1B and TNF in glioblastoma/microglia co-culture"),
    "25868794": ("10.1002/ijc.29566", "Zhang 2015 Int J Cancer", "EZH2 inhibitors incl. GSK343 are P-gp and BCRP substrates in vitro"),
    "37391829": ("10.1186/s12974-023-02842-6", "Mannino 2023 J Neuroinflammation", "GSK-343 reduced neuroinflammation and cytokine expression in an MPTP mouse model"),
    "38212578": ("10.1038/s41589-023-01512-1", "Zhang 2024 Nat Chem Biol", "CGI1746 acts through the sigma-1 receptor to block ferroptosis (off-target action)"),
    "39759071": ("10.1016/j.isci.2024.110961", "Akintola 2024 iScience", "CGI-1746 inhibits the 26S proteasome, also in cells that do not express BTK (off-target action)"),
    "20061378": ("10.1074/jbc.M109.088682", "Pacholec 2010 J Biol Chem", "dispute whether STACs are direct SIRT1 activators (fluorophore-peptide artefact)"),
    "23471411": ("10.1126/science.1231097", "Hubbard 2013 Science", "allosteric SIRT1 activation by STACs, substrate-motif dependent, Glu230"),
    "22991226": ("10.1530/JME-12-0095", "Raichur 2012 J Mol Endocrinol", "sole reference of HDAC5 -> SLC2A1: HDAC5 knockdown lowers GLUT1 expression in human primary muscle cells"),
    "22483777": ("10.1016/j.bcp.2012.03.014", "Kim 2012 Biochem Pharmacol", "TRRUST reference of SIRT1 -> MYC: SIRT1 knockdown or inhibitor raises c-Myc in K562 cells"),
    "22245592": ("10.1016/j.taap.2011.12.025", "Hong 2012 Toxicol Appl Pharmacol", "TRRUST reference of SIRT1 -> MYC: SIRT1 destabilises c-Myc under hypoxia in HepG2 cells"),
    "28689659": ("10.1016/j.molcel.2017.06.011", "Wang 2017 Mol Cell", "SIGNOR reference of MAPK1 -> BCL3: Erk2 phosphorylates Bcl3 and converts it to a transcriptional coregulator"),
    "9751072": ("10.1016/s0006-2952(98)00122-1", "Uckun 1998 Biochem Pharmacol", "SIGNOR reference of BTK -> STAT3: a review of BTK in B-cell apoptosis"),
    "21080647": ("10.1021/jm101177s", "Moffat 2010 J Med Chem", "CHR-3996 (nanatinostat) described as a class I selective HDAC inhibitor"),
    "31710489": ("10.1021/acs.jmedchem.9b01295", "Ward 2019 J Med Chem", "AZD0364 (tizaterkib) described as a potent and selective ERK1/2 inhibitor, cellular IC50 6 nM"),
    "25574479": ("10.1002/acn3.135", "Jiang 2014 Ann Clin Transl Neurol", "SRT2104 penetrated the blood-brain barrier in a Huntington disease mouse model"),
    "29207681": ("10.18632/oncotarget.19176", "Zhang 2017 Oncotarget", "SIGNOR reference of KDM4C -> HIF1A is a review of JMJD2C in tumours"),
}
TAIL = "ALL_COVERAGE_UNAVAILABLE_EXCEPT_ABSTRACT"
COV_ABS = {"abstract": "read", "introduction": "unavailable", "methods": "unavailable", "results": "unavailable", "figures": "unavailable", "tables": "unavailable",
           "discussion": "unavailable", "limitations": "unavailable", "supplementary": "unavailable", "references": "unavailable"}


def abstract_receipt(pmid, doi, cite, use, n):
    return {
        "analysis_at": "2026-11-03T08:30:00Z", "analysis_time_precision": "minute",
        "coverage": COV_ABS, "event_at": "2026-11-03T08:45:00Z", "event_id": f"FTR-20261103-{pmid}-01",
        "evidence_basis": [f"abstract analysed in full ({cite}); used for one qualification fact: {use}",
                           "no experimental detail absent from the abstract is used; every statement carried into the tables is marked abstract-level",
                           "coverage uses `unavailable` for the sections not obtained: full text was not acquired in this package"],
        "evidence_depth": "abstract_only", "outputs": OUT, "prior_receipt": None, "record_kind": "contemporaneous_receipt", "reread_reason": "first_read",
        "source_fingerprint": None, "source_kind": "abstract", "source_locator": f"PubMed record for PMID {pmid} (abstract and metadata as served 2026-11-03)",
        "study_id": {"doi": doi, "pmid": pmid},
        "workflow": ("IT21 P4a qualification (qualification_it21_p4a_20261103). Abstract analysed through the PubMed route for one fact of an edge or a compound record; no full text was retrieved and none was "
                     "required for the labelled fact. Prepared as a JSON file for the integrator; was not appended by the preparing actor."),
    }


def hopkinson():
    return {
        "analysis_at": "2026-11-03T08:30:00Z", "analysis_time_precision": "minute",
        "coverage": {"abstract": "read", "introduction": "read", "methods": "not_present", "results": "read", "figures": "not_read", "tables": "not_read", "discussion": "read",
                     "limitations": "not_read", "supplementary": "unavailable", "references": "not_read"},
        "event_at": "2026-11-03T08:45:00Z", "event_id": "FTR-20261103-26682036-01",
        "evidence_basis": ["coverage_map",
                           "Peer-reviewed, open article (Chem Sci 2013). NOT WWOX EVIDENCE: the paper contains no WWOX or neural-cell analysis.",
                           "Read: abstract, introduction, the combined Results and Discussion (enzyme panel, crystal-structure section, cellular activity of IOX1) and conclusions, from the open article text; "
                           "the two tables, the three figures and the supplementary information were not read; the article has no separate Methods section.",
                           "Four verbatim locators are in locators_it21_p4a.tsv (L1 to L4) and were matched against the saved PMC XML (sha256 in source_fingerprint)."],
        "evidence_depth": "partial_fulltext_read", "outputs": OUT, "prior_receipt": None, "record_kind": "contemporaneous_receipt", "reread_reason": "first_read",
        "source_fingerprint": "1aa6a161bf9bb82e6562a6a536175e5ba82b3b52995cfd60be30b989fd44ebb5", "source_kind": "fulltext_local",
        "source_locator": "files/fulltext/PMC4678600_PMID26682036_Hopkinson2013_IOX1.xml",
        "study_id": {"doi": "10.1039/C3SC51122G", "pmid": "26682036"},
        "workflow": ("IT21 P4a question-driven reading (qualification_it21_p4a_20261103): does the compound IOX1 raise or lower HIF in cells, and at what concentration relative to its KDM4 inhibition? "
                     "Open article text obtained through the PubMed full-text route and PMC efetch XML, flattened to text, quotes located by exact string search. Prepared as a JSON file for the integrator; "
                     "was not appended by the preparing actor. The saved XML is under the worktree's gitignored files/ tree and is not transported by the branch."),
    }


def main():
    if len(sys.argv) < 2 or sys.argv[1] != "write":
        print(__doc__)
        return
    d = HERE / "receipts"
    d.mkdir(exist_ok=True)
    recs = [hopkinson()] + [abstract_receipt(p, *v, i) for i, (p, v) in enumerate(ABS.items())]
    for r in recs:
        (d / f"{r['event_id']}.json").write_text(json.dumps(r, indent=1, sort_keys=True) + "\n")
    print("wrote", len(recs), "receipts")


if __name__ == "__main__":
    main()
