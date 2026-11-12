"""SCI46 package P: the Orchestrator's tables (hypotheses, outcome matrix, experiment ladder) and the engine-shaped package (`engine/comparison.tsv`, `new_measurements.tsv`,
`decisive.tsv`, `id_map.tsv`, `assay_rows.tsv`) in the layout of pdh_pdk_sci44_20261110/engine and ampa_comparison_it41_20261109/output. `engine/decisive.tsv` is the verified producer table
(output/decisive.tsv with the V8 annotations) unchanged, the engine ids equal the producer ids; no proposition is added. `engine/derived_roles_check.tsv` is the result of the engine's existing `derive`
run read-only on a copy of the compound-view row V19 whose name list carries the name 'KI-696' (the engine's alias table is hard-coded, see consumer_delta.md).
  python3 build_tables.py"""
import csv, shutil, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent; ROOT = HERE.parents[4]
OUT = HERE / "engine"

def write(path, head, rows):
    for r in rows: assert len(r) == len(head), (path.name, r[0], len(r), len(head))
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(head); w.writerows(rows)

HYP_COLS = ["hyp_id", "observation_DATO", "relation_INFERENZA", "action_IPOTESI", "context_cell_and_time", "compound_or_class_and_role", "expected_result", "counter_evidence", "possible_harm", "refuting_experiment", "class", "consumer", "evidence_rows"]
HYP = [
["NH1", "NFE2L2 0.75x and NQO1 0.73x lower in a KO organoid, NFE2L2 lower in shWWOX neural cells (transcript only, n 4 v 2 and n 1 per arm); NRF2 protein, nuclear NRF2 and target activity are not measured in any WWOX-deficient neural system (INV-08 W01, W02, W08)",
 "If the response is insufficient (H1), nuclear NRF2 and target-gene activity are lower by genotype and rise on KEAP1-Kelch occupancy; the rise needs NRF2",
 "Occupy the KEAP1 Kelch pocket with a non-covalent binder (no cysteine chemistry) and read target activity and a function endpoint in neurons and astrocytes separately, each with and without a verified NFE2L2 loss",
 "neurons and astrocytes separately, early postnatal-equivalent stage, acute exposure under one fixed oxidant challenge; endpoint time with the knockdown shown adequate at that time",
 "KI-696 (CHEMBL3819587): PROBE (structure confirmed; nanomolar in epithelium, 40 uM needed with one enantiomer in LUHMES; brain exposure and neuronal permeability unknown); not a candidate",
 "a genotype difference at baseline or after challenge; the compound raises nuclear NRF2 and two target genes in KO more than in control; effect lost under adequate loss; function endpoint follows",
 "NQO1 and G6PD higher in shWWOX (W02); HMOX1 and SRXN1 higher in organoid and P47T (W01, W05): the transcripts are mixed; no WWOX-system protein datum",
 "Sustained NRF2 activation changes metabolism and redox in ways not studied in this cell (IPOTESI); the one human neuronal use found (Zhu 2025) moved ferroptosis markers in the harmful direction on a KEAP1-overexpressing, NRF2-high background",
 "no genotype difference at baseline (axis moves toward inert); no rise of target genes in neurons at any tolerated exposure; effect unchanged under verified NFE2L2 loss (independent route); worsening",
 "new combination in the repository (a binder with a documented NRF2-loss arm in glia, applied to the WWOX premise); novelty against the literature not assessed",
 "INV-08 steps X0-X2 and open question IT45-Q03 (reagent pair now named); compound view V19 name list", "D01-D11; D19; D20; D21"],
["NH2", "HMOX1, SRXN1 and GSR higher in organoid, Hmox1 and Srxn1 modestly higher in P47T brain (W01, W05); KI696 on KEAP1-overexpressing, NRF2/HO-1-high hiPSC cortical interneurons raised Fe2+, MDA and cytokines and lowered GSH and GPX4 (Zhu 2025, no loss arm)",
 "If the response is already induced but insufficient (H2) or maladaptive, further KEAP1 disruption adds little or worsens, and the benefit-versus-risk curve across graded occupancy is informative; a single concentration cannot show it",
 "Use the binder as a graded ladder (several on-target response levels, matched by nuclear NRF2 and two target genes) and read a benefit endpoint and a risk panel (GSH, GPX4, lipid peroxidation, cytokines, viability) in the same wells, KO against control",
 "same cultures as NH1; the ladder runs at the endpoint time and again after a second, later exposure",
 "KI-696: PROBE for the ladder; bardoxolone methyl (covalent, neurotoxic in LUHMES above nanomolar): conditional COMPARATOR only inside a non-toxic window; fumarate esters: comparator with documented NRF2-independent routes",
 "a genotype x occupancy interaction: benefit at low occupancy, none or harm above it in KO; control cells monotone",
 "a monotone benefit across the ladder in KO cells; a Zhu-like harm in control cells too (then not a genotype effect)",
 "the risk panel moves without a function change (marker without consequence); a Zhu-like change could be caused by the KEAP1 overexpression and not by the binder",
 "a monotone benefit across occupancy with an unchanged risk panel in KO",
 "new combination (ferroptosis-axis readouts as the risk arm of the NRF2 ladder); novelty not assessed",
 "INV-08 step X1 (add a risk panel and a graded series); DL-MECH-125 (GPX4); W07 (ferroptosis in a cancer-cell abstract)", "D21; D09; D08; D10"],
["NH3", "Verified loss of Nrf2 in primary rat microglia removes the induction by the binder (HO1, NQO1, GCLC about 4-8-fold to about 1) and the protection, and KEAP1 loss occludes it (Wu 2024); RA839, another non-covalent binder, regulated 105 probe sets in macrophages and two in Nrf2 knock-out cells (abstract only); a fumarate keeps an HCAR2-dependent route on Tnf, Il1b, Hmox1 and Nr4a2 in a microglial line (Parodi) and modifies 24 other proteins in neurons and astrocytes (abstract)",
 "The count and identity of genes that a reagent still regulates after verified NRF2 loss measure its NRF2-independent action, which NQO1 alone cannot; for the binder it should be near zero, for a fumarate not",
 "Run the covalent and the non-covalent reagent in the same cell, each at matched on-target response, with a verified NFE2L2 loss arm and a KEAP1-loss occlusion arm, and read a transcript panel or array: the survivors after loss are the independent action",
 "one cell class at a time (neurons, astrocytes, microglia-like cells); same time and medium for both reagents",
 "KI-696 (probe) against dimethyl fumarate and monomethyl fumarate (comparators), RA839 (conditional second binder, abstract-level) to show the result is not one chemotype; bardoxolone methyl only if a non-toxic window is shown",
 "binder: survivors near zero and occlusion by KEAP1 loss; fumarate: a residual set on inflammatory genes; both lose the target-gene panel under loss",
 "the binder keeps a residual set under verified loss (its action is not only through NRF2 in that cell); both classes lose everything (no discrimination between them in that cell)",
 "an array or panel survivor count depends on the knockdown adequacy and on the baseline; a floor effect (Wu CCK-8 0.20) can mimic dependence on viability endpoints",
 "survivor genes of the binder equal those of the fumarate",
 "known-but-unused design (Winkel's array arm, abstract only) applied to a neural cell: new combination; novelty not assessed",
 "S6 design in INV-08 X2; comparison engine rows C-K1 to C-K3; IT45-Q03", "D10; D11; D14; D15; D20; D19"],
["NH4", "The neuron-specific Wwox deletion carries the phenotype and glia deletions do not (W09, flat and underpowered); tBHQ-induced neuronal gene change depended on astrocytic Nrf2 in mixed cortical cultures (Kraft 2004, abstract only)",
 "Whether the benefit of a KEAP1 binder reaches a WWOX-deficient neuron through its own NRF2 or through astrocytic NRF2 (H3) cannot be seen in a mixed culture; cell-type-restricted loss separates the two",
 "Co-cultures in which only the astrocytes, or only the neurons, lack NFE2L2, with the binder against vehicle, reading neuronal network function and viability",
 "neuron-astrocyte co-culture; WWOX-null neurons with NFE2L2-intact or -null astrocytes, and NFE2L2-null neurons with intact astrocytes",
 "KI-696 (probe); no compound is needed to read the genetic arms alone (the genetic arm first)",
 "benefit lost when astrocytes lack NFE2L2 and kept when neurons do (compartment H3); the reverse (cell-autonomous)",
 "the neuron deletion data (W09) show astrocytes alone do not produce the phenotype, not that they cannot rescue; the binder has not been used in astrocytes in any source reached",
 "astrocytic NRF2 activation may shift composition or glial reactivity (IPOTESI)",
 "loss in either compartment leaves the effect unchanged (compartment does not matter) or no effect in any arm",
 "known-but-unused (Kraft abstract) with a binder: new combination; novelty not assessed",
 "INV-08 step X3; open question IT45-Q03", "D12; D18; transfer.tsv T04"],
]
OUT_COLS = ["outcome_id", "result", "favoured_explanation", "alternatives_still_open", "pharmacological_choice_changed", "limit_of_the_conclusion"]
OUTM = [
["O1", "No genotype difference in nuclear NRF2 or target-gene activity at baseline or after the fixed challenge, and function normal", "the axis is inert in this model (H6 / none)", "a deficit only at another stage, in another cell class or after a different challenge (H4)", "no activation arm is run; the reagents stay in the catalogue as probes", "one challenge and the tested stages; transcripts are not activity"],
["O2", "Lower baseline target activity; the binder raises it; the rise and the function benefit are lost under verified NFE2L2 loss; KEAP1 loss occludes the binder", "insufficient response (H1) with an NRF2-dependent benefit of the binder", "a benefit through another route that also needs NRF2-dependent genes; composition shift", "the binder becomes the dependence probe for the next model; the covalent reagent is added only for contrast", "the endpoint and cell class tested; viability or network activity in culture is not recovery of function in the animal; exposure unknown"],
["O3", "Target activity already high at baseline; the binder adds little or the risk panel (GSH, GPX4, lipid peroxidation, cytokines) worsens", "already induced and insufficient, or maladaptive (H2 / H6)", "the risk panel moves without a function change; an off-NRF2 action of the binder", "stop raising NRF2; the question moves to the downstream deficit; the ladder stays a risk arm", "a marker change is not harm to function; the one human neuronal precedent (Zhu) has no loss arm"],
["O4", "The binder's effect is unchanged under verified adequate NFE2L2 loss", "an NRF2-independent route or off-target action of the binder for that endpoint (H5)", "the reagent's own off-target effect; a second KEAP1 function", "the binder is not a dependence probe for that endpoint; test the second binder and the enantiomer pair before any claim", "adequacy is shown only for the genes and the time measured; a different endpoint may still be dependent"],
["O5", "The effect is unchanged but the NFE2L2 loss is partial (protein remains, target genes not suppressed at the endpoint time)", "none: uninterpretable (the Costa pattern)", "partial dependence; independence; floor effect", "no choice changes; the loss arm is repeated until adequate by the preregistered criterion", "residual protein can carry the effect; the paper's own wording was 'could not definitely exclude'"],
["O6", "The binder's effect is lost under loss and a fumarate retains a residual set", "the fumarate has an NRF2-independent route in that cell (H5 for the fumarate)", "HCAR2, NF-kB, protein modification: not separated from each other", "the binder is the NRF2 probe; the fumarate is a lever with another mechanism and needs its own arms (an HCAR2 arm)", "the matching on on-target response must hold; a mismatch can fake a residual"],
["O7", "Both reagents lose the target-gene panel and the endpoint under verified loss", "the endpoint is NRF2-dependent for both classes", "dependence of the panel, not of every consequence; shared off-target of the arm itself", "choose between them by tolerability and exposure (the covalent bardoxolone was neurotoxic in LUHMES above nanomolar)", "does not show specificity beyond NRF2 or a benefit for WWOX"],
["O8", "The benefit is lost when astrocytes lack NFE2L2 and kept when neurons lack it", "a compartment effect (H3): the astrocyte carries the benefit", "composition or reactivity change in astrocytes", "astrocyte-directed exposure and composition counts become part of the arm", "co-culture is not tissue; one compound, one genotype combination"],
["O9", "The benefit appears at one stage only", "stage dependence (H4)", "composition differences between stages", "exposure is timed to that stage in any later model", "stages of a culture are not postnatal ages"],
["O10", "After KEAP1 loss the binder still changes the target genes", "an action not through KEAP1 (off-target)", "residual KEAP1 protein (incomplete loss)", "the binder is excluded as a KEAP1 probe in that cell", "incomplete KEAP1 loss mimics this; the verification of the occlusion arm is part of the result"],
]
LAD_COLS = ["step", "question", "kind", "readout", "decision_it_changes", "can_run_now"]
LAD = [
["L1", "Is the identity of the binder fixed and are the numbers per article kept apart?", "executable now (done)", "identity.tsv; ChEMBL, PDB, PubChem keys", "which compound name the comparison rows carry", "yes (done)"],
["L2", "Does a reachable source show the binder's NRF2-loss arm with numbers?", "executable now (partly done)", "Wu 2024 (microglia, verified loss); Davies arm only as categorical [CH]; Winkel RA839 abstract", "whether the binder is a dependence probe at all", "yes (done); the Davies Supporting Information is the first undone step"],
["L3", "NRF2 protein, nuclear NRF2, target-gene activity and a risk panel by genotype, per cell class, with and without a fixed challenge", "indispensable new measurement (INV-08 X0)", "nuclear fractionation or imaging; two target genes plus NQO1 enzyme activity; GSH, GPX4, lipid peroxidation", "whether any activation arm is run (O1)", "no"],
["L4", "Adequacy criterion for the NFE2L2 loss fixed in advance", "design, before L5", "protein and target-gene suppression at the endpoint time", "whether a maintained effect can be read at all (O4 versus O5)", "yes (a preregistration text, not a measurement)"],
["L5", "The pair with and without verified loss, with the KEAP1-loss occlusion arm and an array or panel of survivors", "indispensable new measurement (INV-08 X2)", "survivor-gene count and identity; the endpoint; viability", "O2 to O7, O10", "no"],
["L6", "Compartment-restricted loss", "later validation (INV-08 X3)", "network function with neuron-only or astrocyte-only NFE2L2 loss", "O8", "no"],
["L7", "Brain exposure and neuronal permeability of the binder (an acid; 40 uM in LUHMES against nanomolar in epithelium)", "not resolvable by the literature reached", "free concentration in the culture medium, then tissue", "whether the binder can leave the probe role", "no"],
["L8", "Does WWOX loss change NRF2 turnover in a neural cell (the HCC abstract has WWOX activity lowering nuclear NRF2)?", "not resolvable by the literature reached", "NRF2 half-life and ubiquitination in KO and control", "the direction of H1 against H2", "no"],
]
CMP_COLS = ["row_id", "action_context_hypothesised_benefit", "compound_or_probe", "identity_status", "documented_action_and_limits", "functional_comparison", "mechanism_discriminating_control",
            "measurement_that_makes_it_interpretable", "outcome_favourable", "outcome_contrary", "outcome_unresolved", "explanations_not_separated", "source_locator_depth", "public_or_new_measurement", "needs_new_experiment"]
CMP = [
["C-K1", "IPOTESI: occupy the KEAP1 Kelch pocket with a non-covalent binder in the neural cell class where an NRF2 deficit is measured, to ask whether target activity and a function endpoint rise NRF2-dependently (NH1); the first decision is the premise, not the molecule",
 "KI-696 (probe)", "structure confirmed (ChEMBL CHEMBL3819587 = PDB L6I = PubChem CID 118170767, one stereo-defined structure); name KI-696 is a ChEMBL curator synonym and a statement of Wu and Callahan, not a sentence of the Davies abstract; Davies text unreachable; numbers per article (Davies 7 [CH], Tran 9, Wu C7, Callahan 4); Costa's enantiomers Ki 696-1/-2 not assigned to the ChEMBL structure",
 "Kelch binding ITC Kd 1.3 nM [CH], SPR 1.4 nM (Tran); NRF2-siRNA arms of Davies categorical only [CH]; primary rat microglia: induction and protection lost under verified loss, KEAP1 loss occludes (Wu; no direct binding measurement there); LUHMES: 40 uM with one enantiomer, loss incomplete; hiPSC interneurons: harm direction on a KEAP1-high background (Zhu); no primary neuron or astrocyte",
 "nuclear NRF2 and at least two target genes beside NQO1, then a function endpoint and viability, in neurons and astrocytes separately",
 "NFE2L2 loss shown adequate at protein and target-gene level at the endpoint time; KEAP1-loss occlusion arm; vehicle", "M-K1; M-K2; M-K3; M-K5",
 "effect lost under adequate loss and occluded by KEAP1 loss", "effect unchanged under adequate loss; worsening", "loss incomplete (the Costa pattern)", "viability versus function; composition", "D01-D11; D20; D21", "new measurement", "yes: M-K1; M-K2; M-K5"],
["C-K2", "IPOTESI: the covalent comparator in the same cell, matched on on-target response, to ask which part of an electrophile's effect survives NRF2 loss (NH3)",
 "dimethyl fumarate and monomethyl fumarate (comparators); bardoxolone methyl (conditional comparator)", "fumarates: ChEMBL typed EC50 rows from two documents that disagree (5.114 against 7.93 uM; not interchangeable); bardoxolone methyl and the acid are two structures",
 "NRF2-dependence of the DMF benefit in EAE mice (abstract); HCAR2 route for MMF in N9 microglia (antibody arm); 24 other proteins modified in neurons and astrocytes (abstract); bardoxolone extremely neurotoxic above nanomolar in LUHMES (Costa); Davies [CH] has bardoxolone methyl 100 nM in the same NRF2-siRNA design as the binder at 1 uM, categorical labels only",
 "the same panel, endpoint and loss arm as C-K1 at matched nuclear NRF2 and two-gene response", "HCAR2 arm; the verified NFE2L2 loss; the occlusion arm", "M-K3; M-K4",
 "a residual set after loss attributable to a named route", "no residual (both classes lose everything)", "which independent route", "HCAR2, NF-kB, protein modification", "D05; D13; D14; D15", "new measurement", "yes: M-K3; M-K4"],
["C-K3", "IPOTESI: genetic arms as the reference of the design: verified NFE2L2 loss and KEAP1 loss before any compound",
 "NFE2L2 siRNA, shRNA or CRISPR knockout; KEAP1 knockout (controls)", "not compounds; reagents specific to the transcript; off-target effects of the reagent not tested in the papers read",
 "adequacy was verified in Wu (mRNA about 0.10 and 0.05 of control by figure read, faint bands remain) and was partial in Costa (protein 0.68, mRNA 0.36, NQO1 mRNA 0.63)",
 "loss verified at protein and two target genes at the endpoint time", "the adequacy criterion fixed before the experiment", "M-K2",
 "target-gene induction by the reagent falls to the vehicle interval", "a visible residual protein with a maintained effect", "adequacy cannot be shown", "partial dependence against independence", "D09; D10; D11", "new measurement", "yes: M-K2"],
["C-K4", "IPOTESI: an NRF2-lowering tool is not needed if the genetic arm is adequate; ML385 and halofuginone are not used as controls",
 "ML385 (unqualified); halofuginone (excluded as an NRF2-selective control); brusatol (excluded)", "ML385: NRF2 interaction by pull-down, FP IC50 1.9 uM, about 170 kinases clean at 5 uM, selective in KEAP1-mutant over wild-type knock-in H460; no neural cell; halofuginone and brusatol repress synthesis generally",
 "lung lines only for ML385; used in microglia by Wu without concentration or specificity shown", "none beyond the genetic arm", "genetic arm", "M-K2", "the genetic arm answers", "an inhibitor is needed where a genetic arm is impossible", "off-target", "NRF2 inhibition against translation repression", "D16; D17", "new measurement", "no: use C-K3"],
["C-K5", "IPOTESI: compartment-restricted loss to ask whether a benefit in WWOX-deficient neurons needs astrocytic NRF2 (NH4)",
 "genetic cell-type-restricted NFE2L2 loss; KI-696 as the probe", "see C-K1", "mixed cortical cultures: tBHQ neuronal gene change depended on astrocytic Nrf2 (Kraft, abstract only); no binder in astrocytes",
 "neuronal network function and viability", "neuron-only and astrocyte-only loss co-cultures", "M-K6", "benefit lost with astrocytic loss", "benefit lost with neuronal loss", "neither", "cell-autonomous against astrocyte-mediated", "D12; D18; T04", "new measurement", "yes: M-K6"],
["C-K6", "IPOTESI: a second non-covalent chemotype to show a result is not one scaffold, and to import the array design",
 "RA839 (conditional probe, abstract-level)", "(3S)-1-[4-[(2,3,5,6-tetramethylphenyl)sulfonylamino]-1-naphthyl]pyrrolidine-3-carboxylic acid per the abstract; Kd about 6 uM; no catalogue row checked in this package", "binds the Kelch domain (ITC, X-ray); regulated 105 probe sets in macrophages and two in Nrf2 knock-out macrophages; CDDO-Me and Keap1 silencing as comparators (abstract); full text not reached",
 "an array of survivors after loss", "Nrf2-null cells; Keap1 silencing", "M-K4", "survivors near zero", "survivors present", "full text and the knock-out verification not seen", "myeloid not neural", "D20", "new measurement", "yes: M-K4"],
]
MEAS_COLS = ["meas_id", "measurement", "why_no_literature_can_substitute", "blocks_which_comparison_row"]
MEAS = [
["M-K1", "INV-08 step X0 on marker-resolved or sorted neural material: nuclear and total NRF2 protein, KEAP1, NQO1 enzyme activity plus at least two other target genes, a risk panel (GSH, GPX4, lipid peroxidation) by genotype, with and without one fixed oxidant challenge", "No source measures NRF2 protein, localisation or target activity in a WWOX-deficient neural cell (W08); transcripts are mixed and composition-confounded", "C-K1; C-K2"],
["M-K2", "Adequacy of the NFE2L2 and KEAP1 loss at the endpoint time: protein, nuclear fraction and two target genes, with a criterion written before the experiment", "Costa's loss left 0.68 of nuclear protein and the maintained protection was uninterpretable; Wu's loss was strong in microglia only; neither tells what is adequate in a neuron", "C-K1; C-K3; C-K4"],
["M-K3", "Dose-response of each reagent on nuclear NRF2 and two target genes in the neural cell, then the matched-response concentration for the pair; free concentration in the medium", "Nanomolar in epithelium against 40 uM in LUHMES; cross-paper potencies are not interchangeable (DMF 5.114 against 7.93 uM)", "C-K1; C-K2"],
["M-K4", "Panel or array of genes regulated by each reagent with and without verified NRF2 loss; the survivors after loss are the independent action", "Only an abstract (Winkel) reports a genome-wide survivor count for a binder (2 of 105); no source has it for a covalent reagent or in a neural cell", "C-K2; C-K6"],
["M-K5", "Viability and a function readout (network activity) in the same wells as the genes", "A viability rescue is not recovery of function; the only function readout found is locomotor in a rat model without a loss arm", "C-K1"],
["M-K6", "Neuron-only and astrocyte-only NFE2L2 loss in co-culture with the reagent against vehicle", "Kraft is an abstract with tBHQ; no source has a binder or a WWOX-deficient neuron here", "C-K5"],
]

def main():
    OUT.mkdir(exist_ok=True)
    write(HERE / "hypotheses.tsv", HYP_COLS, HYP); write(HERE / "outcome_matrix.tsv", OUT_COLS, OUTM); write(HERE / "experiment_ladder.tsv", LAD_COLS, LAD)
    write(OUT / "comparison.tsv", CMP_COLS, CMP); write(OUT / "new_measurements.tsv", MEAS_COLS, MEAS)
    # engine decisive = the verified producer table, unchanged; id_map identity
    # the engine reads depth by its prefix and class by its vocabulary; only those two cells are normalised (the producer's words are kept in parentheses)
    CLASS = {"D03": "absence", "D18": "absence", "D19": "derived"}
    src = list(csv.reader(open(HERE / "output/decisive.tsv", encoding="utf-8", newline=""), delimiter="\t")); head, rows = src[0], src[1:]
    di, ci = head.index("depth"), head.index("class")
    for r in rows:
        if r[di].startswith(("database record plus", "partial full text", "search perimeter plus")): r[di] = f"partial_fulltext_read ({r[di]})"
        r[ci] = CLASS.get(r[0], "compound/class read")
    write(OUT / "decisive.tsv", head, rows)
    ids = [r[0] for r in rows]
    write(OUT / "id_map.tsv", ["engine_prop_id", "source_table", "source_prop_id"], [[i, "output/decisive.tsv", i] for i in ids])
    # the value table for the generator: the producer's assay rows with the V8 annotations, same columns
    shutil.copyfile(HERE / "output/assay_rows.tsv", OUT / "assay_rows.tsv")
    sys.path.insert(0, str(ROOT / "framework/scripts")); sys.path.insert(0, str(DR / "generation_it43_20261110"))
    import hypothesis_package as hp, comparison_engine as ce
    items = [r for r in csv.DictReader(open(DR / "generation_it41_20261109/compound_view.tsv", encoding="utf-8"), delimiter="\t") if r["item_id"] == "V19"]
    for r in items: r["name_full"] = r["name_full"].replace("a non-covalent KEAP1 binder (catalogue tool probe)", "KI-696 (non-covalent KEAP1 binder, catalogue tool probe)")
    pkg = hp.load_comparison(OUT)
    res = ce.merge(ce.derive(items, pkg, "sci46"))
    with open(OUT / "derived_roles_check.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, ce.OUT_FIELDS, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(res)
    for r in res: print(r["item_id"], r["name"], r["evidence_tier"], r["role_derived"], "|", r["comparison_state"][:80], "|", r["premise_needed"][:50])

if __name__ == "__main__":
    main()
