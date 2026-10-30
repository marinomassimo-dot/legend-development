#!/usr/bin/env python3
"""Writes reconstruction_it11_p21.tsv: one row per phenotype lead (5 molecules + 2 out-of-method). Computed columns (Q1..Q7 relevance, targets, universe) come from targets.tsv, pairs.tsv, universe.tsv
(reconstruct_it11_p21.py); curated columns (identity, cause, pointers) are written here with the file and field they rest on.  Read-only toward every earlier package."""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import csv, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
rd = lambda n: list(csv.DictReader(open(HERE / n, encoding="utf-8"), delimiter="\t"))
T, P, U = rd("targets.tsv"), rd("pairs.tsv"), rd("universe.tsv")
Z = lambda x: abs(float(x)) > 0


REP = {"ethosuximide": "FAM:CAT:CHEMBL696", "lithium": "FAM:CAT:CHEMBL1200826", "vigabatrin": "FAM:CAT:CHEMBL89598", "d-APV": "FAM:CAT:DGIDB:b0ca5cf2303c", "A51": "FAM:CAT:CHEMBL4754493"}   # one representative family per molecule: name twins carry identical target sets


def qrel(mol):
    out = {}
    for q in range(1, 8):
        parts = []
        for lvl, tag in (("expression", "E"), ("protein", "P"), ("phospho", "P")):
            pr = [r for r in P if r["molecule"] == mol and r["signed_usable"] == "1" and r["seed_set"].startswith(f"Q{q}_{lvl}") and r["family_id"] == REP[mol]]
            un = [r for r in U if r["molecule"] == mol and r["seed_set"].startswith(f"Q{q}_{lvl}")]
            if not un:
                continue
            direct = sorted({f"{r['target']}={r['seed_gene']}" for r in pr if r["direct_target_is_seed"] == "1"})
            v4 = [r for r in pr if Z(r["influence_v4"]) and r["direct_target_is_seed"] != "1"]
            f1 = [r for r in pr if Z(r["influence_all"]) and not Z(r["influence_v3"])]
            f5 = [r for r in pr if Z(r["influence_v3"]) and not Z(r["influence_v4"])]
            ch = sorted({r["chain_v4"].split(" [")[0] + ("..." if "; " in r["chain_v4"] else "") for r in v4 if r["chain_v4"]})[:2]
            parts.append(f"Q{q}{tag}: direct[{','.join(direct) or '-'}] v4-admissible_pairs={len({(r['family_id'],r['target'],r['seed_gene']) for r in v4})} F1-lost={len({(r['target'],r['seed_gene']) for r in f1})} F5-lost={len({(r['target'],r['seed_gene']) for r in f5})}"
                         + (f" e.g. {ch[0]}" if ch else ""))
        out[f"Q{q}"] = " || ".join(parts) if parts else "no_pair"
    return out


def tg(mol, fams):
    s = []
    for r in T:
        if r["molecule"] == mol and r["family_id"] in fams and r["signed_usable"] == "1":
            s.append(f"{r['target']}({r['mean_sign']};{r['scopes']};{r['hgnc_id']};out={r['network_out_edges']},in={r['network_in_edges']})")
    return " | ".join(sorted(set(s))) or "none"


def unsigned(mol, fams):
    r = [x for x in T if x["molecule"] == mol and x["family_id"] in fams and x["signed_usable"] == "0"]
    return f"{len({x['target'] for x in r})} targets with no usable sign (claim_source without action type): " + ",".join(sorted({x['target'] for x in r})[:12]) + ("..." if len({x['target'] for x in r}) > 12 else "") if r else "0"


A = "disease-models/wwox/research/drug_repurposing/"
ROWS = [
 dict(molecule="ethosuximide", wwox_unit="U17", tested_form="ethosuximide (systemic pretreatment, mouse; salt not applicable: neutral molecule)",
      identity="parent molecule, no salt, no prodrug (ChEMBL CHEMBL696 chemistry.prodrug=0). Two families, name twins not merged: FAM:CAT:CHEMBL696 (ChEMBL curated, approved_any_source) and FAM:CAT:DGIDB:6998a1a2d947 (DGIdb, no ChEMBL id)",
      families="FAM:CAT:CHEMBL696:3 signed;FAM:CAT:DGIDB:6998a1a2d947:3 signed (+CYP3A4,SCN1A unsigned)",
      universe="in catalogue Y; mnet_usable Y (family_meta); examined in the ten seed sets? target nodes CACNA1G/CACNA1H are in the network (in-edges only) so the family counts as examined, but it has no row in any proposals table because every arm is exactly 0",
      signed_targets=tg("ethosuximide", {"FAM:CAT:CHEMBL696", "FAM:CAT:DGIDB:6998a1a2d947"}), unsigned_targets=unsigned("ethosuximide", {"FAM:CAT:DGIDB:6998a1a2d947"}),
      f2_f3="F2: HGNC-resolved (HGNC:1394/1395/1396, ChEMBL PROTEIN FAMILY row, scope complex_or_group); not in alias_collision or complex_not_credited lists of build_funnel_v3.json; F3: no prodrug flag",
      network_status="CACNA1G out=0 in=1; CACNA1H out=0 in=6; CACNA1I out=0 in=0: all three are sink or isolated nodes",
      can_score="NO by construction: a target with no outgoing edge can contribute only as a direct hit on a seed gene, and no seed set contains a CACNA1x gene",
      pf_entry="PHENOTYPE_FIRST, graph_status NO_GRAPH_ROW (results/phenotype_first.tsv row U17)",
      wwox_context="Wwox-/- constitutive null mouse; whole organism; PTZ-provoked behavioural seizure score, late phase, graphical reading; DECREASE; complete_fulltext_read; PMID 32000863 Fig 7b; receipts FTR-20260804-32000863-01 and FTR-20261021-32000863-03; cards_early/EB-ETX-01.packet.json A-ETX-1",
      primary_cause="NO_PATH_TO_ANY_SEED", subtype="SINK_TARGETS (target nodes exist, no outgoing edge)",
      secondary="REPRESENTATION_GAP: ion-channel targets are sinks in a TF/kinase network (201 channel/receptor-subunit genes among 2,373 signed targets, 12 with an outgoing edge); function-level endpoint (seizure score) is not a seed level",
      premise="none: zero rows is the correct reading", pointers=f"{A}generation_it9_p2_20261030/v3/results/actions/family_actions.tsv.gz (3 rows per family); {A}coverage_it11_p21_20261031/targets.tsv; pairs.tsv (no ethosuximide row)"),
 dict(molecule="lithium", wwox_unit="U24", tested_form="lithium chloride, 60 mg/kg (Fig 7d legend: 'LiCl'); NOT in the catalogue as a family (no lithium chloride record)",
      identity="active moiety = Li+ ion; the catalogue holds the ion record (FAM:CAT:CHEMBL1201333 LITHIUM, 0 target rows, card identity of G01) and SEPARATE salt/name-twin families that carry the actions: CHEMBL1200826 carbonate, CHEMBL1201170 citrate anhydrous (parent of CHEMBL2103738 citrate, which is not a family of its own in actions), CHEMBL3707288 succinate (0 targets), DGIDB:be65bb20ae7f Lithium (42 unsigned claims), DGIDB:50ccc7b5c33e carbonate, DGIDB:cfa5bd0a6c8c citrate, DGIDB:0408436e6031 cation (0), DGIDB:bc9225cea0c7 succinate (0)",
      families="signed: CHEMBL1200826, CHEMBL1201170, DGIDB:50ccc7b5c33e, DGIDB:cfa5bd0a6c8c (each GSK3A,GSK3B,IMPA1 inhibitor); unsigned only: DGIDB:be65bb20ae7f; no target: CHEMBL1201333, CHEMBL3707288, DGIDB:0408436e6031, DGIDB:bc9225cea0c7",
      universe="in catalogue Y (salts), tested salt LiCl N; mnet_usable Y for the four signed families; examined in all seed sets",
      signed_targets=tg("lithium", {"FAM:CAT:CHEMBL1200826"}), unsigned_targets=unsigned("lithium", {"FAM:CAT:DGIDB:be65bb20ae7f"}),
      f2_f3="F2: HGNC-resolved (GSK3A/B via ChEMBL PROTEIN FAMILY scope complex_or_group, IMPA1 single protein); no alias or complex exclusion; F3: no prodrug flag (inorganic salts)",
      network_status="GSK3A out=6 in=7; GSK3B out=35 in=58; IMPA1 out=0 in=0",
      can_score="YES: scored in Q1 (0), Q2 (-1.25e-4), Q3 (0), Q5 (+2.05e-4), Q6 expression (-1.22e-3); Q7 direct hit on GSK3B but the seed is a phospho-site of uncertain direction (arms cancel, Q_net 0); Q4 pairs exist at hop 2 and are lost to F5; not in Q6 protein (F1 and F5)",
      pf_entry="PHENOTYPE_FIRST, IT10 graph_status NAME_TWIN_SCORED_NOT_SPECIFIC:Q2,Q5,Q6; corrected here to NAME_TWIN_IN_SEED_SPECIFIC_ARM:Q6/mimics (phenotype_first_it11.tsv)",
      wwox_context="Wwox-/- null versus +/+ littermates, preweaning mouse, whole organism, behavioural seizure stage after PTZ; DECREASE in the null panel; the same suppression is significant in +/+ and +/- panels (figure read, locator entry 22), so NOT Wwox-specific; complete_fulltext_read; PMID 32000863 Fig 7d; receipt FTR-20260804-32000863-01; G01_lithium_gsk3.packet.json DR-LI-001",
      primary_cause="LOW_RANK_SCORED", subtype="seed-specific in all three nulls in Q6 expression (mimics arm; z -12.1/-8.9/-6.4) at rank 67-70 of 232 (v4); rank 26-29 of 247 in IT9 v3, just beyond the 25-row display cut; the IT10 lookup read only the truncated tables",
      secondary="PHENOTYPE_FIRST_LOOKUP_TRUNCATION (IT10 label wrong); ADMISSIBLE_PATH_REJECTED_BY_FILTER at protein level and for Q3/Q4 (F1, F5); NULL_CONTRIBUTION in Q1/Q3/Q7; NO_ACTION_RECORD for the ion record U24 is linked to; tested salt (LiCl) OUT_OF_UNIVERSE; the Q6 hit concerns MYC expression (human), unrelated to the seizure endpoint",
      premise="CORRECTION: the graph did return lithium (four name-twin families) as a seed-specific mimics hit in Q6 expression; IT10 README 3D and test_it10_p1.py (asserts NAME_TWIN_SCORED_NOT_SPECIFIC) rest on the truncated candidate tables",
      pointers=f"{A}generation_it10_p1_20261031/results_v4/v3_seed_specific_all_nulls.tsv (Q6, mimics, ranks 82-85 of the file; z columns); results_v4/candidates_Q6.tsv (no lithium row: top 25 only); coverage_it11_p21_20261031/pairs.tsv; universe.tsv"),
 dict(molecule="vigabatrin", wwox_unit="U20", tested_form="vigabatrin (clinical use in WWOX-DEE cases; racemate, neutral molecule)",
      identity="parent molecule, no salt, no prodrug (CHEMBL89598). Families: FAM:CAT:CHEMBL89598 (ChEMBL) and FAM:CAT:DGIDB:358b8a817686 (DGIdb). Related but separate unit members, not the tested molecule: CPP-115 (CHEMBL146927/CHEMBL4297273/DGIDB:0a2199127751) and class members (U20 unit_members.tsv)",
      families="FAM:CAT:CHEMBL89598:1 signed;FAM:CAT:DGIDB:358b8a817686:2 signed (+GABBR1 unsigned)",
      universe="in catalogue Y; mnet_usable Y; NOT examined: no signed target is a node of the network (in_graph=0, funnel counts only in_graph>0)",
      signed_targets=tg("vigabatrin", {"FAM:CAT:CHEMBL89598", "FAM:CAT:DGIDB:358b8a817686"}), unsigned_targets=unsigned("vigabatrin", {"FAM:CAT:DGIDB:358b8a817686"}),
      f2_f3="F2: HGNC-resolved (ABAT HGNC:23; SLC32A1 HGNC:11018); no exclusion; F3: no flag",
      network_status="ABAT out=0 in=0; SLC32A1 out=0 in=0 (not nodes); GABBR1 (unsigned) has 4 outgoing edges but no path to any seed",
      can_score="NO: neither signed target is in the network",
      pf_entry="PHENOTYPE_FIRST, graph_status NO_GRAPH_ROW",
      wwox_context="WWOX-DEE patients (human, whole organism): clinical case reports; 7 assertions (2 benefit, 3 null, 1 partial, 1 unresolved); queried_not_full_read; cards_early/EB-VGB-01.packet.json A-VGB-1..6, A-VGB-10; no receipt",
      primary_cause="NO_PATH_TO_ANY_SEED", subtype="TARGETS_NOT_A_NODE (family not examined)",
      secondary="OUT_OF_UNIVERSE in the narrow sense that the family is not in the examined set; REPRESENTATION_GAP: the mechanism acts through raised GABA (a metabolite), which the network cannot express; endpoint is clinical",
      premise="none: zero rows is the correct reading", pointers=f"{A}generation_it9_p2_20261030/v3/results/actions/family_actions.tsv.gz; coverage_it11_p21_20261031/targets.tsv"),
 dict(molecule="d-APV", wwox_unit="U21", tested_form="d-APV in the paper = D-AP5 (alias declared in dispose_it10.py PHENO_ALIASES; standard synonym, not re-verified against the paper's chemical identifier)",
      identity="catalogue family FAM:CAT:DGIDB:b0ca5cf2303c 'D-Ap5' (DGIdb-only; GtoPdb ligand 4168, ChEMBL CHEMBL84612 asserted by GtoPdb but out of the catalogue selection: relations.gtopdb_reconciliation decision out_of_selection). Not memantine, perampanel or other U21 class members",
      families="FAM:CAT:DGIDB:b0ca5cf2303c:4 signed",
      universe="in catalogue Y; mnet_usable Y; examined in every seed set; has a proposals row only where a direct hit or a path exists (Q4 expression)",
      signed_targets=tg("d-APV", {"FAM:CAT:DGIDB:b0ca5cf2303c"}), unsigned_targets="0",
      f2_f3="F2: HGNC concept ids resolved (GRIN2A-D, GtoPdb claims, scope single_protein_among_siblings: one claim per subunit, the antagonism is not subunit-selective); F3: no flag",
      network_status="GRIN2A out=3 in=6; GRIN2B out=3 in=20; GRIN2C out=3 in=6; GRIN2D out=3 in=4",
      can_score="YES, only as a direct hit: GRIN2C is a Q4 seed (mouse expression, down); GRIN2A/B/D have no admissible chain to GRIN2C, GRM3, KCNA2 or NPY",
      pf_entry="PHENOTYPE_FIRST, graph_status DIRECT_HIT_ZERO_SCORE:Q4 (zero refers to Q_net_ind, the indirect part; Q_direct is -0.5, Z_full_robust -15.78, call 'mimics')",
      wwox_context="Synapsin-Cre Wwox knockout mouse neocortex, ex vivo slice, juvenile ~2 weeks; burst frequency, spontaneous bursting eliminated and recovered on washout; n=5 slices from 3 animals; DECREASE; complete_fulltext_read; PMID 34634460 Results 2.2; receipt FTR-20260810-34634460-02; F01_glutamate_receptor_node.packet.json DR-W2-001; tool compound, NMDAR-selective",
      primary_cause="NULL_CONTRIBUTION", subtype="indirect contribution is 0 because the target IS the seed (hop 0 only); the direct component is non-zero and sits in the diagnostic direct_search arm (Q4 rank 24, disposition DIAGNOSTIC_ONLY), not in opposes/mimics",
      secondary="NO_PATH_TO_ANY_SEED for GRIN2A/GRIN2B/GRIN2D (indirect); level mismatch (seed = GRIN2C transcript in mouse, drug = receptor antagonist; expression is not function); role of the GRIN2C decrease unknown, so 'mimics' is a conditional H_PROTECT, not a benefit",
      premise="PARTIAL CORRECTION: d-APV was returned (direct_search) with a non-zero direct score; 'zero score' in IT10 is the indirect part only",
      pointers=f"{A}generation_it10_p1_20261031/results_v4/proposals_p1_Q4_expression_tiersAB.tsv.gz (family row); results/dispositions_Q4.tsv rank 24; coverage_it11_p21_20261031/universe.tsv"),
 dict(molecule="A51", wwox_unit="U10", tested_form="'A51, a multi-kinase inhibitor' in a WWOX-knockout human cerebral organoid (PMID 42397075 per the card); no structure, no identifier",
      identity="NOT resolved. The card states a CK1-alpha/CDK7/CDK9 phase-1 agent as the 'compound class' and that sameness of formulation is not verified (D01_a51.card.json p4_card.identity). The catalogue has a name-lookalike FAM:CAT:CHEMBL4754493 BTX-A51 (clinical_candidate, 0 target rows, E0) whose identity with the organoid compound is NOT established here and is not assumed",
      families="none attached; candidate lookalike CHEMBL4754493 (not attached)",
      universe="not in the universe: no catalogue identity (unit_members.tsv U10: 'no catalogue identity')",
      signed_targets="none", unsigned_targets="0", f2_f3="not applicable",
      network_status="CSNK1A1 out=8; CDK7 out=11; CDK9 out=6 (card-named kinases; what-if only)",
      can_score="NO: no identity, and the lookalike has no action record",
      pf_entry="PHENOTYPE_FIRST, graph_status NOT_EXAMINABLE_NO_CATALOGUE_IDENTITY",
      wwox_context="WWOX knockout (constitutive engineered null) human cerebral organoid, culture weeks 8-15; SOX2+MYC+ progenitor fraction DECREASE (DR-D01-001) and SATB2/CTIP2 layer-neuron fractions NO_CHANGE (DR-D01-002); complete_fulltext_read; receipt FTR-20260810-42397075-04; panel values not re-auditable (card measured_result_note); cards/D01_a51.card.json",
      primary_cause="IDENTITY_UNRESOLVED", subtype="name exists only inside the paper; ChEMBL fuzzy hit is an unnamed molecule (typed_assertions note)",
      secondary="NO_ACTION_RECORD if BTX-A51 were the compound (CHEMBL4754493 has no target rows); relevant to Q6 (MYC up, human) by the card's stated Wnt/MYC action, which the graph never saw. What-if (whatif_a51.tsv, not a classification input): crediting CSNK1A1/CDK7 as inhibitors gives a v4 expression chain to MYC for CSNK1A1 (CSNK1A1 -P(-)-> FOXO6 -T(+)-> MYC) whose compatible direction is 'mimics' (MYC up), the OPPOSITE of the MYC suppression the card reports",
      premise="none", pointers=f"{A}cards/D01_a51.card.json (input.p4_card.identity); {A}typed_assertions_20261023.tsv rows DR-D01-001/002; {A}ranking_it8_p9_20261029/unit_members.tsv U10; coverage_it11_p21_20261031/whatif_a51.tsv"),
 dict(molecule="AAV9-delivered human WWOX (gene addition)", wwox_unit="U07", tested_form="gene addition", identity="not a molecule", families="none (catalog/non_molecule_modalities.tsv: gene_replacement_vector)", universe="out of method (modality)",
      signed_targets="n/a", unsigned_targets="n/a", f2_f3="n/a", network_status="n/a", can_score="NO: out of method", pf_entry="OUT_OF_METHOD_MODALITY", wwox_context="Wwox-null mouse; spike-wave discharge rate; 5 benefit, 1 mixed, 2 null, 2 partial, 2 unquantified; PMID 42422765; complete_fulltext_read",
      primary_cause="OUT_OF_METHOD (not in the closed list)", subtype="modality", secondary="", premise="none", pointers=f"{A}catalog/non_molecule_modalities.tsv; ranking_it8_p9_20261029/member_evidence.tsv U07"),
 dict(molecule="Ketogenic diet", wwox_unit="U15", tested_form="diet", identity="not a molecule", families="none (non_molecule_modalities.tsv E04_ketogenic_lactate_axis: dietary_intervention_plus_transport_blockade)", universe="out of method (modality)",
      signed_targets="n/a", unsigned_targets="n/a", f2_f3="n/a", network_status="n/a", can_score="NO: out of method", pf_entry="OUT_OF_METHOD_MODALITY", wwox_context="WOREE patients (human); clinician-reported seizure control; 1 benefit, 1 null; PMID 35573960; complete/partial fulltext",
      primary_cause="OUT_OF_METHOD (not in the closed list)", subtype="modality", secondary="", premise="none", pointers=f"{A}catalog/non_molecule_modalities.tsv; ranking_it8_p9_20261029/member_evidence.tsv U15"),
]
KEYS = ["molecule", "wwox_unit", "tested_form", "identity", "families", "universe", "signed_targets", "unsigned_targets", "f2_f3", "network_status"]
cols = KEYS + [f"Q{q}" for q in range(1, 8)] + ["can_score", "pf_entry", "wwox_context", "primary_cause", "subtype", "secondary", "premise", "pointers"]
FAMS = {"ethosuximide": "ethosuximide", "lithium": "lithium", "vigabatrin": "vigabatrin", "d-APV": "d-APV", "A51": "A51"}
with open(HERE / "reconstruction_it11_p21.tsv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n")
    w.writeheader()
    for r in ROWS:
        q = qrel(r["molecule"]) if r["molecule"] in FAMS else {f"Q{i}": "n/a" for i in range(1, 8)}
        w.writerow({**r, **q})
print("rows", len(ROWS))
