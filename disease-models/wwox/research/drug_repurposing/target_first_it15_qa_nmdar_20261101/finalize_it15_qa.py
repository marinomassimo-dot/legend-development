"""Offline: adds compound names/phase and a reviewer note to graded_comparisons_qa.tsv (the imported grade column is left untouched), appends source/identity rows
to perimeter_log.tsv, and writes identity_qa.tsv. Reads relations_qa.tsv, raw/molecules_all.json, raw/failures_*.json. --help is safe."""
import argparse, csv, glob, json, os, re, collections
argparse.ArgumentParser(description=__doc__).parse_args()
H = os.path.dirname(os.path.abspath(__file__))
M = json.load(open(os.path.join(H, "raw/molecules_all.json")))["molecules"]
NOTE = {
 "chembl:CHEMBL4308825": "reviewer (corrected after verification): CHEMBL4308825 is a REVIEW (Burnell 2018, PMID 29446949) compiling ifenprodil from Hess 1996 (PMID 8768735; human, oocytes, 3 uM glycine, -40 mV) and Ro 25-6981 from Fischer 1997 (PMID 9400004; same pair also in CHEMBL1132364 = one origin counted twice). Each ratio is internally same-paper; conditions differ between the two compounds. A grade on a compilation is not a grade on one experiment",
 "chembl:CHEMBL5625199": "reviewer: GluN2A value carries 'Outside typical range'; descriptions are terse; ratio not relied on",
 "chembl:CHEMBL1759939": "reviewer: one document, FLIPR calcium flux in U2OS, no holding voltage exists; pore-blocker potency depends on voltage and Mg2+; ratio <=4x is inside assay noise",
 "chembl:CHEMBL6115009": "reviewer: one document, CHO FLIPR calcium flux, 24 h incubation, unknown-origin receptors, no holding voltage; the grade does not make it transferable to a slice",
 "chembl:CHEMBL6083260": "reviewer: 30-fold spread inside one GluN2B arm (510 to 15,220 nM), larger than any between-subunit ratio",
 "chembl:CHEMBL1146243": "reviewer: oocyte NR1/NR2A vs NR1/NR2B; holding voltage not in the ChEMBL text (primary paper not opened)",
 "chembl:CHEMBL4024770": "reviewer: rat oocyte TEVC functional Ki for all four subunits; validity comment on 2C and 2D; agonist concentrations not in ChEMBL text",
 "chembl:CHEMBL1143579": "reviewer: rat oocyte functional Ki (Morley 2005 per verifier)",
 "chembl:CHEMBL5131569": "reviewer: positive allosteric modulator (Hill 2022, PMID 35785990, HEK293 patch -70 mV); EC50 not a block potency; opposed action",
 "chembl:CHEMBL1137121": "reviewer: generic seven-gene complex value is not a subunit value; no ratio",
}
rows = list(csv.DictReader(open(os.path.join(H, "graded_comparisons_qa.tsv")), delimiter="\t"))
cols = ["compound", "compound_name_chembl", "max_phase_as_stated", "document", "measure", "species", "n_targets", "grade", "limits", "targets_median_nM [n; min-max; censored]", "ratio_extreme_target_medians", "ratio_not_computed_because", "reviewer_note"]
with open(os.path.join(H, "graded_comparisons_qa.tsv"), "w") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(cols)
    for r in rows:
        m = M.get(r["compound"], {})
        w.writerow([r["compound"], m.get("pref_name") or "", m.get("max_phase") if m.get("max_phase") is not None else "", r["document"], r["measure"], r["species"], r["n_targets"], r["grade"], r["limits"], r["targets_median_nM [n; min-max; censored]"], r["ratio_extreme_target_medians"], r["ratio_not_computed_because"], NOTE.get(r["document"].split("#")[0], "")])
# perimeter log additions
extra = []
for fn in sorted(glob.glob(os.path.join(H, "raw/targets_*.json"))):
    o = json.load(open(fn)); extra.append([os.path.basename(fn)[:-5], "chembl adapter uniprot=" + o["request"].get("uniprot", ""), o.get("source_version", ""), o["status"], "", len(o["hits"]), "", (o.get("error") or "")[:80].replace("\n", " "), "target discovery by accession; QUERY_ERROR = not retrieved, not 'no target'; 3 attempts (1 + 2 retries)"])
for fn in sorted(glob.glob(os.path.join(H, "raw/genesearch_*.json"))):
    o = json.load(open(fn)); extra.append([os.path.basename(fn)[:-5], "chembl adapter gene=" + o["request"].get("gene", "") + " (target/search, limit 20, all organisms)", o.get("source_version", ""), o["status"], "", len(o["hits"]), "possible: limit 20", (o.get("error") or "")[:80].replace("\n", " "), "fallback target discovery after accession query failed (deviation D1)"])
nm = json.load(open(os.path.join(H, "raw/molecules_all.json")))
extra.append(["molecule_identity_lookup", "chembl molecule.json?molecule_chembl_id__in batches of 100", "", "OK" if not nm["failed_batches"] else "PARTIAL", nm["requested"], nm["found"], "", "", "identity of all parent ids in relations_qa; synonyms kept first 10 only"])
fl = sum(len(json.load(open(p))) for p in glob.glob(os.path.join(H, "raw/failures_*.json")))
extra.append(["http_failures_logged", "all stages, each failed attempt (5xx or transport)", "", "", "", fl, "", "", "failed attempts, not failed queries; see raw/failures_*.json"])
rel = list(csv.DictReader(open(os.path.join(H, "relations_qa.tsv")), delimiter="\t"))
for s in ("gtopdb", "dgidb", "drugcentral"):
    extra.append(["file_" + s, {"gtopdb": "catalog/cache/gtopdb/interactions.csv, Target Gene Symbol starts GRIN (release 2026.3.1)", "dgidb": "catalog/cache/dgidb/interactions.tsv gene_name starts GRIN (export 2024-06-10), GRINA excluded (not an NMDAR subunit)", "drugcentral": "unmtid-dbs.net/download/DrugCentral/2027/drug.target.interaction.tsv.gz (SHA-256 1908684983a79a067a44da952e1f6fd26b0f34cc36560cd9be0f0843bbfee1e1), GENE contains GRIN; file downloaded for this task (0.96 MB), not in the catalog cache"}[s], "", "FILE_READ", "", sum(1 for r in rel if r["source"] == s), "", "", "complete file scan; direction only for dgidb (no value); values of drugcentral/gtopdb copied from ChEMBL/IUPHAR are one origin, not counted again"])
with open(os.path.join(H, "perimeter_log.tsv"), "a") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    for e in extra: w.writerow(e)
# identity table
ID = [
 ("CHEMBL84612", "d-AP5 / d-APV", "competitive glutamate-site antagonist", "single enantiomer (D); GtoPdb ligand 4168; Breton 2021 used d-APV", "tool, no salt in ChEMBL parent", "GtoPdb Antagonist (GluN2A-D); DGIdb inhibitor"),
 ("CHEMBL305187", "ifenprodil", "GluN2B NAM (ifenprodil site)", "ChEMBL parent CHEMBL305187 chirality 0 (racemic/unspecified); stereo entries CHEMBL319706 (S), CHEMBL49623 (R,S), CHEMBL113830 (S,R) kept apart", "tartrate/other salts merged to parent", "not in GtoPdb NMDAR rows of this cache; DrugCentral Ki/IC50 GluN2B copied from ChEMBL-type sources; ChEMBL max_phase 2 (as stated)"),
 ("CHEMBL305195", "Ro 25-6981", "GluN2B NAM (tool)", "no pref_name in ChEMBL; resolved by id used in IT6/IT14 (InChIKey route there)", "maleate salt not distinguished", "ChEMBL activity only; no mechanism row"),
 ("CHEMBL182066", "radiprodil", "GluN2B NAM (clinical stage)", "single compound", "-", "ChEMBL mechanism ANTAGONIST on GRIN1/GRIN2B complex target CHEMBL1907603; DGIdb inhibitor"),
 ("CHEMBL807", "memantine", "use-dependent pore blocker (low affinity)", "single compound; salt merged", "HCl merged", "ChEMBL label NEGATIVE ALLOSTERIC MODULATOR on generic group CHEMBL2094124, record on the salt CHEMBL1699 (non-competitive; not an ifenprodil-site NAM); DrugCentral NAM; DGIdb negative modulator"),
 ("CHEMBL742", "ketamine", "use-dependent pore blocker", "CHEMBL742 chirality 0 (racemate); esketamine is a separate parent CHEMBL395091 and is not merged; arketamine not found in perimeter", "HCl merged (mechanism record sits on the salt CHEMBL1714; parent query returns none)", "ChEMBL NAM label on generic group CHEMBL2094124 = non-competitive, not site- or subunit-resolved; DrugCentral BLOCKER; DGIdb blocker/negative modulator"),
 ("CHEMBL395091", "esketamine (S-ketamine)", "use-dependent pore blocker", "single enantiomer; 13 generic-complex Ki rows of ketamine share one value (180 nM, one origin)", "-", "ChEMBL NAM label; DrugCentral ANTAGONIST; no GluN2B value found for esketamine itself"),
 ("CHEMBL284237", "dizocilpine (MK-801)", "slow-trapping use-dependent pore blocker (class from prior knowledge, UNVERIFIED in this run)", "pref_name DIZOCILPINE; enantiomer not stated in the rows read", "maleate salt merged", "GtoPdb None (channel blocker); DGIdb blocker"),
 ("CHEMBL275528", "phencyclidine", "use-dependent pore blocker", "single compound", "-", "GtoPdb None; DrugCentral; DGIdb blocker"),
 ("CHEMBL52440", "dextromethorphan", "use-dependent pore blocker (via dextrorphan); also sigma-1 agonist", "d-isomer; levomethorphan CHEMBL separate; dextrorphan CHEMBL1254766 (metabolite) kept apart", "HBr/polistirex merged", "ChEMBL ANTAGONIST on GRIN2A target CHEMBL1972 (label 'epsilon 1' is the mouse alias of the GluN2A gene name); DrugCentral BLOCKER GRIN2C"),
 ("CHEMBL660", "amantadine", "low-affinity pore blocker", "HCl merged (CHEMBL1569)", "-", "ChEMBL ANTAGONIST on generic group; DrugCentral BLOCKER"),
 ("CHEMBL17350", "traxoprodil (CP-101,606)", "GluN2B NAM (ifenprodil site)", "single compound", "-", "ChEMBL ANTAGONIST on GRIN1/GRIN2B complex"),
 ("CHEMBL28564", "eliprodil", "GluN2B NAM (ifenprodil site)", "single compound", "-", "no mechanism row read; activity rows [3H]ifenprodil displacement Ki 13 nM (repeated across 9 documents: one origin)"),
 ("CHEMBL39664", "selfotel (CGS 19755)", "competitive glutamate-site antagonist", "single compound", "-", "GtoPdb Antagonist; rows are rat membrane binding on the generic complex"),
 ("CHEMBL5095095", "dalzanemdor (SAGE-718)", "NMDAR positive allosteric modulator (OPPOSED action)", "GtoPdb SAGE-718 (ligand 12050) and ChEMBL dalzanemdor: identical values 79-86 nM, probable one origin (not verified by document id)", "-", "GtoPdb Positive; DGIdb modulator"),
 ("CHEMBL1201293", "acamprosate", "queue anchor", "resolves in ChEMBL; 89 activities, none on NMDAR targets; no mechanism record", "-", "DrugCentral ANTAGONIST (no value); DGIdb inhibitor"),
 ("CHEMBL3545351", "AV-101 (L-4-chlorokynurenine)", "queue anchor (glycine-site prodrug class, prior knowledge)", "resolves; phase 3 as stated; mechanism record only, 0 activity rows", "-", "ChEMBL mechanism: Glutamate [NMDA] receptor antagonist on CHEMBL2094124"),
 ("CHEMBL3707355", "AZD8108", "queue anchor", "resolves; mechanism record only, 0 activity rows", "-", "ChEMBL mechanism antagonist on CHEMBL2094124"),
 ("CHEMBL2106165", "delucemine (NPS-1506)", "queue anchor", "resolves as DELUCEMINE HYDROCHLORIDE; no mechanism, no activity", "HCl", "DGIdb inhibitor only"),
 ("CHEMBL3707400", "indantadol", "queue anchor", "resolves; mechanism NMDA antagonist + MAO-A inhibitor; 0 activity rows", "-", "ChEMBL mechanism antagonist on CHEMBL2094124"),
 ("CHEMBL2106798", "neramexane", "queue anchor", "resolves as neramexane mesylate; 0 activity rows", "mesylate", "ChEMBL mechanism antagonist on CHEMBL2094124 (plus alpha9/alpha10 nAChR)"),
 ("CHEMBL2107771", "ralfinamide", "queue anchor", "resolves; 16 activities none on NMDAR targets", "-", "ChEMBL mechanism antagonist on CHEMBL2094124 (plus Ca/Na channel, MAO-B)"),
 ("CHEMBL1094", "felbamate", "queue anchor", "resolves; about 70 GluN2B (CHEMBL1904) rows of type Kapp (0.87-34.5 mM) and % inhibition (61-90%) are invisible to the IC50/Ki/Kd/EC50 filter of this package (perimeter limit)", "-", "ChEMBL mechanism antagonist on CHEMBL2094124; DrugCentral GluN2B IC50 pX 4.28"),
 ("CHEMBL771", "cycloserine (D-cycloserine)", "glycine-site partial agonist (OPPOSED action)", "pref_name CYCLOSERINE (D-isomer by use; stereo not read in ChEMBL parent record here); L-form not separated", "-", "ChEMBL mechanism rows are bacterial (alanine racemase); NMDAR action from DrugCentral/ChEMBL activity EC50 rows only"),
]
with open(os.path.join(H, "identity_qa.tsv"), "w") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["chembl_parent", "name_used", "mechanism_class_as_assigned", "identity_notes (parent / stereoisomer / metabolite)", "salt_note", "action_direction_sources", "pref_name_in_chembl", "max_phase_as_stated", "molecule_type", "chirality_flag", "n_chembl_rows_in_perimeter"])
    cnt = collections.Counter(r["compound"] for r in rel if r["source"] == "chembl_activity")
    for i, n, c, idn, salt, act in ID:
        m = M.get(i, {}); w.writerow([i, n, c, idn, salt, act, m.get("pref_name") or "", m.get("max_phase") if m.get("max_phase") is not None else "", m.get("molecule_type") or "", m.get("chirality") if m.get("chirality") is not None else "", cnt.get(i, 0)])
print("ok")
