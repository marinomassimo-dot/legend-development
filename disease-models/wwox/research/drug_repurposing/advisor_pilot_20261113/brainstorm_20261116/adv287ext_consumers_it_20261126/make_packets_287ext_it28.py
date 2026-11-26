"""Builds BLIND_PACKET_{H,A,R}_287EXT_IT28.txt: each block carries the new fragment inside its field text (about 350 characters each side), the record's source line and
the held source paths; never a card, never a result file. Run from the repository root: make_packets_287ext_it28.py OUTDIR"""
import importlib.util, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("a", HERE / "apply_287ext_it28.py"); A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)
E = A.E; DR = A.DR
R = "/home/desktop/legend-development/files"
SRC = {
 "H02-26": "Vigabatrin prescribing-information label sections 5.3 and 5.4 (the card's source line: openFDA label JSON effective 2026-06-15; that version is NOT held). Held sibling labels: search /home/desktop/legend-development/files for vigabatrin label JSON/extract files by name (find files -iname '*vigabatrin*'; look in label_extracts_it9_p4c_e too). PMID 19054414 (abstract only, via the PubMed tool: public read).",
 "H02-05": "PMID 19054414 abstract (PubMed tool); the label sections as above.",
 "H02-03": "PMID 20384718 abstract (PubMed tool).",
 "H02-17": f"{R}/fulltext/PMID36601084_ADV272_PMC9806385_epmc_20261125.xml (PMID 36601084)",
 "H02-29": f"{R}/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.txt ; {R}/fulltext/PMID33914858_Repudi2021_OUP_browserprint.pdf (Figure 5 on PDF page 27; render and view it)",
 "A01-04": f"{R}/fulltext/PMID30266908_Guiberson2018_PMC6162227.xml ; {R}/figures/PMID30266908/ (all images, view Supplementary Figure 12 and Figure 6) ; {R}/supplement/PMID30266908/",
 "A01-03": "same as A01-04", "A01-08, A01-16": "same as A01-04", "A01-11, A01-14, A01-15": "same as A01-04 (Figures 3, 4 and 6)",
 "A01-13": f"{R}/fulltext/PMID41274966_Tubastatin2025_PMC_r2.xml ; {R}/figures/PMID41274966_r2/ ; {R}/supplement/PMID41274966_r2/ and _r3/",
 "R-34": f"{R}/fulltext/PMID32023956_Lukas2020_PMC7037350.xml",
 "R-37": f"{R}/fulltext/PMID34268881_Steinberg2021_PMC_r2.xml ; {R}/fulltext/PMID34268881_Steinberg2021.pdf ; {R}/figures/PMID34268881_r2/ ; {R}/supplement/PMID34268881_r2/",
 "R-35": f"{R}/fulltext/PMID36537114_Chong2023_SGchunks_text_2026-10-21.txt ; {R}/fulltext/PMID36537114_Chong2023_ScholarGateway_20260929.json",
 "R-24": f"{R}/fulltext/PMID39041895_Mijatovic2024_PMC11264351_epmc_2026-10-29.xml (Figures 5 and 6 are not held as images: text and legends only)",
 "R-06": "same as R-24",
 "R-29": f"{R}/geo/ (GSE156243 deposit files; find them) ; {R}/fulltext/PMID34268881_Steinberg2021_PMC_r2.xml",
 "R-19": "same as R-29",
 "R-04": f"{R}/fulltext/PMID36828035_Hussain2023_PMC.xml ; {R}/fulltext/PMID36828035_Hussain2023.pdf ; {R}/figures/PMID36828035/ (Fig 9d,e) ; {R}/supplement/PMID36828035/",
 "R-07": f"{R}/fulltext/PMID42397075_Steinberg2026_OUP-AM_layout.txt ; {R}/fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf ; {R}/fulltext/PMID42397075_Steinberg2026_assets/ ; {R}/fulltext/PMID42397075_Steinberg2026_OUP-Supplement/",
 "R-08": "same as R-07 (Supplementary Fig 7F/7G in the supplement PDF)",
 "R-11": f"{R}/fulltext/PMID35222658_ADV272_PMC8752995_epmc_20261125.xml",
 "R-05": f"{R}/fulltext/PMID41489401_Karnstedt2026_Epilepsia_PMC13075606.xml ; {R}/fulltext/PMID41489401_Karnstedt2026_Epilepsia_PMC13075606_supp_S1_functional.docx ; ..._supp_S2_clinical.xlsx",
}
HEAD = """BLIND VERIFICATION PACKET (IT28, ADV-287 extension consumers; hypothesis level; public, class level; nothing here is medical advice)

Each block holds a NEW text fragment (marked >>> ... <<<) inside the field it will sit in. Check the fragment, and the sentence it sits in where it depends on it, against the held sources only. Do not open any other repository file; no search of the repository for cards or result files; no network except the PubMed tool for the two PMIDs named as abstract-only (a public read). Nothing is written into the repository.
Verdicts per block: MUST CHANGE (a word, number, unit, species, age, group size, comparator, direction, test or generalisation is wrong, unsupported or says more than the source), ADD (supported, but an omission would mislead a reader who sees only this text), STANDS.
Grade every clause. Absolute words (only, no, none, every, not found) need the whole source read; say UNSETTLED where you cannot settle. Numbers read from a figure: name figure, panel and bar, and view the image. Say for each number which group, unit (animal, slice, organoid, library, field), species and age it belongs to.
Clauses about what this repository holds or has searched are OUTSIDE your check: say OUTSIDE. For MUST CHANGE and ADD give minimal replacement wording; no dose and no compound recommendation may appear.
Report: a summary table, then per block the findings with locators and which files and figures you opened. Return the whole report as your final handback.
"""
def ctx(x):
    packet = json.loads((DR / f"cards/{x['card']}.packet.json").read_text(encoding="utf-8"))
    cont, key = A.locate(packet, x["where"]); old = cont[key]; i = old.index(x["old"])
    pre, post = old[max(0, i - 350):i], old[i + len(x["old"]):i + len(x["old"]) + 350]
    return pre + ">>>" + x["new"] + "<<<" + post, x["old"]
def build(tags):
    out = HEAD
    for x in E.X:
        if x["tag"] not in tags: continue
        c, old = ctx(x)
        out += f"\n=== BLOCK {x['tag']}\nSOURCES: {SRC.get(x['tag'], 'see above')}\nFIELD CONTEXT WITH NEW FRAGMENT:\n{c}\nREPLACES (old fragment): {old}\n"
    return out
H = ["H02-26", "H02-05", "H02-03", "H02-17", "H02-29"]
Ablk = ["A01-04", "A01-03", "A01-08, A01-16", "A01-11, A01-14, A01-15", "A01-13"]
Rblk = [x["tag"] for x in E.X if x["tag"].startswith("R-")]
if __name__ == "__main__":
    o = Path(sys.argv[1]); o.mkdir(parents=True, exist_ok=True)
    for name, t in (("H", H), ("A", Ablk), ("R", Rblk)):
        (o / f"BLIND_PACKET_{name}_287EXT_IT28.txt").write_text(build(t), encoding="utf-8")
        print(name, len(t), "blocks")
