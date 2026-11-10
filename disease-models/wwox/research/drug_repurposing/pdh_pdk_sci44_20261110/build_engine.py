"""SCI44 package A: the engine-readable form of the pharmacological comparison for INV-07 (`engine/comparison.tsv`, `engine/new_measurements.tsv`, `engine/decisive.tsv`, the layout of
ampa_comparison_it41_20261109/output). Built mechanically from the verified producer tables (output/a3/decisive.tsv, output/a4/decisive.tsv, output/decisive.tsv, with their V1/V2 corrections) and the
Orchestrator's comparison rows below; no proposition is added. The engine's own `derive` is then run on a copy of the compound-view row V13 (read-only) to show that the roles and premises come from these inputs
with no hand-written exception: `engine/derived_roles_check.tsv`. Nothing outside this folder is edited.
  python3 build_engine.py"""
import csv, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
ROOT = HERE.parents[4]
OUT = HERE / "engine"

# engine propositions: (engine id, source table, source id, class, species/system string for the comparability rule)
PROPS = [
 ("a3/decisive.tsv", "A3D01", "compound/class read", "recombinant human SUMO-PDK1 and PDK3, radiolabel kinase assay, E1p on the E2p/E3BP core (in vitro enzyme)"),
 ("a3/decisive.tsv", "A3D02", "compound/class read", "recombinant human PDK1 and PDK3, core-free versus core-bound (in vitro enzyme)"),
 ("a3/decisive.tsv", "A3D03", "compound/class read", "recombinant human PDK4, core-free (in vitro enzyme)"),
 ("a3/decisive.tsv", "A3D04", "compound/class read", "repository value origin; primary not reached"),
 ("a3/decisive.tsv", "A3D06", "compound/class read", "four PDK constructs, DELFIA E1-substrate assay, 5 uM ATP, species not named (in vitro enzyme)"),
 ("a3/decisive.tsv", "A3D07", "compound/class read", "human PC-3 cells and PDK-2 crystal (cell line, not neural)"),
 ("a3/decisive.tsv", "A3D09", "compound/class read", "recombinant human PDK1, PDK2, PDK3, PDK4 (in vitro enzyme); 1998 Ki abstract only"),
 ("a3/decisive.tsv", "A3D10", "compound/class read", "recombinant PDK1 structure; neural results copied"),
 ("a3/decisive.tsv", "A3D12", "compound/class read", "sponsor-affiliated review of devimistat targets"),
 ("a4/decisive.tsv", "A4D01", "compound/class read", "adult mouse hippocampal-stimulation status epilepticus, in vivo, oxamate i.p."),
 ("a4/decisive.tsv", "A4D02", "compound/class read", "acute mouse CA1 slice, 5 mM K+, 30 C for sEPSC (slice)"),
 ("a4/decisive.tsv", "A4D03", "compound/class read", "abstract only: LDH inhibition and stiripentol, mouse neurons"),
 ("a4/decisive.tsv", "A4D06", "compound/class read", "recombinant GABA-A receptors in HEK293T cells (HEK)"),
 ("a4/decisive.tsv", "A4D07", "transfer", "review table, values copied from papers not read"),
 ("a4/decisive.tsv", "A4D13", "compound/class read", "rat cortical neuron cultures, 24 h, UK5099 5-10 uM"),
 ("a4/decisive.tsv", "A4D14", "transfer", "chronic pilocarpine epileptic mouse hippocampal mitochondria; triheptanoin diet"),
 ("a4/decisive.tsv", "A4D08", "transfer", "P12-16 mouse dentate granule neurons, cell-attached KATP (slice)"),
 ("a4/decisive.tsv", "A4D12", "absence", "perimeter statement, overturned in part by verification"),
]
CMP_COLS = ["row_id", "action_context_hypothesised_benefit", "compound_or_probe", "identity_status", "documented_action_and_limits", "functional_comparison", "mechanism_discriminating_control",
            "measurement_that_makes_it_interpretable", "outcome_favourable", "outcome_contrary", "outcome_unresolved", "explanations_not_separated", "source_locator_depth", "public_or_new_measurement", "needs_new_experiment"]
CMP = [
["C-PDK1", "IPOTESI: lower PDK activity to release PDH in the neural cell class where a restraint is measured; dichloroacetate is the reference of the design (millimolar, pyruvate-site); the first decision is the premise, not the molecule",
 "dichloroacetate (reference)", "typed ChEMBL family record (CHEMBL2096665) and DGIdb records; acid and salt not joined by the salt-stripping key", "see A3D09, A3D10 (D09-D10 here): isoform-dependent millimolar inhibition in vitro; neural results mixed; neuropathy in one trial (abstract)",
 "PDH phosphorylation and activity change, lactate, pyruvate and redox state, then a functional readout", "the two other chemotypes and a genetic knockdown of the dominant isoform", "M-P1 (cell-resolved premise)",
 "phosphorylation falls and activity rises with the isoform knockdown in the same class", "no restraint measured, or a functional readout worsens", "a restraint in one class only", "dose-toxicity of a millimolar compound; peripheral effects", "A3D09; A3D10; D08-D13", "new measurement", "yes: M-P1; M-P2"],
["C-PDK2", "IPOTESI: a second chemotype at the ATP site (all four isoforms with IC50 rows) to ask whether the effect is PDK-dependent",
 "VER-246608 (probe)", "GtoPdb typed four isoform rows; catalogue record DGIdb-only", "IC50 35, 84, 40, 91 nM on four constructs in an E1-only assay; species and numbering unverified; PC-3 cells: effects on metabolism only under glucose depletion",
 "same readouts as C-PDK1 at matched phosphorylation change", "dichloroacetate and the genetic arm", "M-P1; M-P2",
 "agreement with the reference and the genetic arm", "no change where the genetic arm changes", "cell entry or construct difference", "assay differences between laboratories (not comparable with AZD7545 values)", "A3D06; A3D07", "new measurement", "yes: M-P2"],
["C-PDK3", "IPOTESI: a lipoamide-site compound as a scaffold-sign probe in the dominant-kinase class (sign depends on the E2/E3BP scaffold)",
 "AZD7545 (probe)", "GtoPdb typed PDK1 and PDK2 only; species unsupported; primary not reached", "IC50 87 nM (PDK1) and 0.60 uM (PDK3) with the core; core-free stimulation of PDK3 (10-fold), PDK4 (2.8-fold), PDK1 (marginal); PDK2 not measured in any source opened",
 "phosphorylation readout only; no functional claim", "VER-246608 and dichloroacetate", "M-P1; M-P2",
 "inhibition-like change in the phospho-readout in the cell class", "stimulation-like change in a PDK4-dominant class", "unmeasured core-bound PDK2 and PDK4", "scaffold state in the cell", "A3D01-A3D05 (as corrected)", "new measurement", "yes: M-P2"],
["C-LAC1", "IPOTESI: reduce lactate production or transport at matched suppression of the burst and ask whether the metabolic step is necessary; with pyruvate add-back",
 "oxamate (probe); stiripentol (comparator)", "oxamate NAME_PARTIAL; stiripentol NAME_EXACT (no LDH target row)", "oxamate shortened status epilepticus in adult mice and lowered CA1 calcium activity and sEPSC frequency; resting properties not measured; stiripentol GABA-A EC50 24.6-35.5 uM, LDH 500 uM copied",
 "burst incidence at matched suppression with a receptor route", "pyruvate add-back, KATP block or opener, GABA-A block", "M-P3; M-P4",
 "burst falls and returns with add-back", "burst unchanged or readout worsens", "receptor-route-only explanation", "off-target and pH actions of oxamate; GABA-A action of stiripentol", "A4D01; A4D02; A4D03; A4D06; A4D07", "new measurement", "yes: M-P3; M-P4"],
["C-PDK4", "IPOTESI: a pyruvate-entry probe at the opposite end of the node, to separate supply and transport roles",
 "UK5099 (probe)", "GtoPdb typed MPC rows; compound_identity by name returns NOT_FOUND_BY_NAME", "5-10 uM cut maximal pyruvate oxidation by more than 50 percent in rat cortical neuron cultures without cell death; protective in excitotoxicity",
 "oxidation and a functional readout in the same cells", "triheptanoin as a fuel control", "M-P1; M-P3",
 "oxidation falls and the functional readout is unchanged or improves", "functional worsening", "whether protection is benefit", "direction label is the producer's inference", "A4D13; A4D14", "new measurement", "yes: M-P3"],
]
MEAS_COLS = ["meas_id", "measurement", "why_no_literature_can_substitute", "blocks_which_comparison_row"]
MEAS = [
["M-P1", "INVESTIGATION INV-07 step 2 on marker-resolved or sorted human neural material: PDH E1-alpha amount, phosphorylation at the three sites, activity before and after dephosphorylation, PDK2-4 transcript and protein per cell class, in the INV-19 lysates", "No WWOX-deficient neural system has a PDH amount, phosphorylation, activity or flux; the kinase set differs by cell class and species (RNA)", "C-PDK1; C-PDK2; C-PDK3; C-PDK4"],
["M-P2", "Genetic knockdown of the dominant isoform of the restrained class, then VER-246608, dichloroacetate and AZD7545 at matched phosphorylation change, with the phospho-readout", "The AZD7545 sign depends on the scaffold; no isoform-resolved cellular dataset exists", "C-PDK1; C-PDK2; C-PDK3"],
["M-P3", "KO slice or neuron: lactate, pyruvate, redox, Vm and Rin (perforated patch), burst incidence with lactate-side tools, add-back, and a receptor route at matched suppression", "Resting properties under oxamate were never measured; no WWOX lactate datum in a neural preparation", "C-LAC1; C-PDK4"],
["M-P4", "Diazoxide and a sulfonylurea in KO and wild type with ATP undisturbed (perforated or cell-attached), Ba2+ difference current per pF in the same cells", "Metabolic-to-K+ coupling is measured in juvenile neocortex, CA1 and dentate neurons, but not in a Wwox neuron; pipette ATP of the Wwox methods is not recorded", "C-LAC1"],
]

def main():
    OUT.mkdir(exist_ok=True)
    src = {}
    for f in ("a3/decisive.tsv", "a4/decisive.tsv"):
        for r in csv.DictReader(open(HERE / "output" / f, encoding="utf-8"), delimiter="\t"): src[(f, r["prop_id"])] = r
    dec = []
    for i, (f, pid, cls, sysstr) in enumerate(PROPS, 1):
        r = src[(f, pid)]
        dec.append([f"D{i:02d}", r["statement"], r["source"], f"{f.split('/')[0]} {pid}; {r['locator']}", r["producer_status"], r["depth"], cls, sysstr])
    with open(OUT / "decisive.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["prop_id", "statement", "source_pmid_or_doi", "locator_hint", "producer_status", "depth", "class", "species_system_age_prep_exposure_readout"]); w.writerows(dec)
    for name, cols, rows in (("comparison.tsv", CMP_COLS, CMP), ("new_measurements.tsv", MEAS_COLS, MEAS)):
        for r in rows: assert len(r) == len(cols), (name, r[0])
        with open(OUT / name, "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(cols); w.writerows(rows)
    with open(OUT / "id_map.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["engine_prop_id", "source_table", "source_prop_id"]); w.writerows([[f"D{i:02d}", f, pid] for i, (f, pid, _, _) in enumerate(PROPS, 1)])
    # derive the roles with the engine's own function on the compound-view row V13 (read-only): no new code, no exception
    sys.path.insert(0, str(ROOT / "framework/scripts")); sys.path.insert(0, str(DR / "generation_it43_20261110"))
    import hypothesis_package as hp, comparison_engine as ce
    items = [r for r in csv.DictReader(open(DR / "generation_it41_20261109/compound_view.tsv", encoding="utf-8"), delimiter="\t") if r["item_id"] == "V13"]
    pkg = hp.load_comparison(OUT)
    res = ce.merge(ce.derive(items, pkg, "sci44"))
    with open(OUT / "derived_roles_check.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, ce.OUT_FIELDS, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(res)
    for r in res: print(r["item_id"], r["name"], r["evidence_tier"], r["role_derived"], "|", r["comparison_state"][:70], "|", r["premise_needed"])
if __name__ == "__main__":
    if len(sys.argv) > 1: print(__doc__)
    else: main()
