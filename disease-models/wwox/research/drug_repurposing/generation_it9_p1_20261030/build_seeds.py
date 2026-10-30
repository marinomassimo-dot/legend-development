"""Build seeds.tsv, process_ids.tsv and hgnc_check.tsv for IT9 P1 (question-first seed table).

The seed rows are typed by hand from qualified WWOX observations (needs.json, IT7 P1 derived values, IT7 P4 context
matrix, IT5/IT6 re-analyses); every row names its locator. This script only assembles the rows, validates the
vocabularies, and (with --check-hgnc) verifies every gene symbol against the live HGNC REST service (read-only, key-less,
sends gene symbols only). Nothing here is evidence of efficacy.

  python3 build_seeds.py --help
  python3 build_seeds.py --out . [--check-hgnc]
"""
import argparse, csv, json, os, sys, time, urllib.request

# ---- vocabularies ---------------------------------------------------------------------------------------------------
ETYPE = {"gene", "protein", "process", "state"}
LEVEL = {"expression", "protein", "phospho", "activity", "function", "pathology"}
DIRN = {"up", "down", "uncertain", "unchanged"}   # 'unchanged' is an addition to the brief's three values (documented in README)
YN = {"yes", "no"}
RC = {  # reason classes (coverage table)
    "USABLE": "usable",
    "RESERVED_INTERVENTION_RESPONSE": "reserved", "RESERVED_ENDPOINT": "reserved",
    "UNUSABLE_PREDICTION_ONLY": "unusable", "UNUSABLE_MATURITY_OR_COMPOSITION": "unusable",
    "UNUSABLE_OTHER_CONTEXT": "unusable", "UNUSABLE_UNVERIFIED_CARRIED": "unusable",
    "UNUSABLE_NONSPECIFIC": "unusable", "UNUSABLE_NOT_EVALUABLE": "unusable", "UNUSABLE_CASE_LEVEL": "unusable",
    "UNUSABLE_DIRECTION_NOT_TABULATED": "unusable", "UNUSABLE_DROPPED_QUESTION": "unusable",
    "GAP_NOT_MEASURED": "gap",
}

N = "disease-models/wwox/research/drug_repurposing/needs/needs.json"  # not repeated in rows; 'NEED-X:On' names the statement
rows = []

def add(q, ent, et, level, d, ctx, use, res, rc, reason, loc, sp, tier, oc, guard="", proc=False):
    rows.append(dict(question_id=q, entity=ent, entity_type=et, level=level, direction=d, context=ctx,
                     usable_for_generation=use, reserved_for_evaluation=res, reason=reason, source_locator=loc,
                     species_observed=sp, context_tier=tier, observation_class=oc, reason_class=rc, evaluation_guard=guard))

U, RI, RE = "USABLE", "RESERVED_INTERVENTION_RESPONSE", "RESERVED_ENDPOINT"
# tiers: A human neural WWOX-loss system; B non-human neural WWOX-loss (mouse/rat); C non-neural WWOX-loss (cells, blood);
#        D other species / other context (fly with amyloid, cancer overexpression, other disease)
def usable(q, ent, et, level, d, ctx, reason, loc, sp, tier, oc, guard=""):
    add(q, ent, et, level, d, ctx, "yes", "no", U, reason, loc, sp, tier, oc, guard)
def reserved(q, ent, et, level, d, ctx, reason, loc, sp, tier, oc, rc=RI, guard=""):
    add(q, ent, et, level, d, ctx, "no", "yes", rc, reason, loc, sp, tier, oc, guard)
def unusable(q, ent, et, level, d, ctx, rc, reason, loc, sp, tier, oc, guard=""):
    add(q, ent, et, level, d, ctx, "no", "no", rc, reason, loc, sp, tier, oc, guard)

NR = "NEED-WWOX-MISSENSE-PROTEIN-RESCUE"
# ======================================================================================================================
# Q1 residual function and protein fate  (track B, broad durable recovery)
# ======================================================================================================================
usable("Q1", "WWOX", "protein", "protein", "down",
       "human; skin fibroblast line, one donor, non-neural; adult-derived; p.Gln230Pro homozygote (destabilising SDR missense class); 2D culture",
       "no WWOX band on one western membrane at one exposure, confirmed on a second harvest of the same line; sensitivity limit, not a proven zero",
       NR + ":O1 (PMID 29808465)", "human", "C", "protein_or_phospho")
usable("Q1", "WWOX", "gene", "expression", "unchanged",
       "human; skin fibroblast line, one donor, non-neural; p.Gln230Pro homozygote",
       "transcript reported comparable to reference lines (one bar per line, no n); together with the protein row it locates the bottleneck after transcription (translation or turnover), which is inferred, not measured",
       "NEED-WWOX-ENDOGENOUS-BOOST:O2 (PMID 29808465)", "human", "C", "expression")
usable("Q1", "WWOX", "gene", "expression", "down",
       "human; blood-derived cDNA, non-neural; c.517-2A>G homozygote (canonical splice-acceptor class, a different allele from the reference class's splice-acceptor allele)",
       "full-length exon-6-containing product absent; only the shorter product (504 bp, interpreted as an 89 bp exon-6 deletion) found, whereas another genotype class shows two products; sequenced per the Methods",
       "NEED-WWOX-SPLICE-CORRECTION:O1 (PMID 30853297)", "human", "C", "expression")
usable("Q1", "WWOX", "protein", "protein", "down",
       "human; patient iPSC-derived cerebral organoids, week 16; WOREE lines (3 individuals, compound-heterozygous severe) and SCAR12 lines (2 individuals, missense, milder)",
       "both patient-line classes carry very low WWOX by immunoblot (per the IT6 P5 reading of the paper) yet differ in phenotype; amount relative to wild type not seen in the text passage",
       "FR-IT6P5:W13 (PMID 42397075)", "human", "A", "protein_or_phospho")
usable("Q1", "STATE:ALLELE_SEVERITY_NOT_TRACKED_BY_PROTEIN_AMOUNT", "state", "function", "uncertain",
       "human; patient iPSC organoids week 16; WOREE (severe) versus SCAR12 (milder) at similarly low WWOX immunoblot signal",
       "phenotype differs at comparable low protein: residual function per molecule, not amount, is the unmeasured variable (quantity R in IT6 P5 section 5); direction of the residual-function effect is not a number anyone holds",
       "FR-IT6P5:W13 + section 5; CM-IT7P4:Q14:ORG_PW,ORG_PS", "human", "A", "functional_effect")
usable("Q1", "STATE:WW1_PARTIAL_LOSS_MISSENSE_WITH_PHENOTYPE", "state", "pathology", "up",
       "mouse; P47T knock-in homozygote (WW1 PPxY-binding impaired, partial loss), hippocampus/cortex/cerebellum; 80 to 250 days",
       "a partial-loss missense with residual function produces disease-level phenotype (progressive astrogliosis; chronic spontaneous generalised seizures in adults older than 6 weeks, video EEG, 3 per genotype): a different residue and domain from the reference class's SDR lesions, transfer not established",
       "DC-IT6P3:section 1 row 4; CM-IT7P4:Q14:P47T; NEED-NEUROINFLAMMATION-GLIA:O2 (PMID 36828035)", "mouse", "B", "functional_effect")
unusable("Q1", "WWOX", "protein", "protein", "down", "human; thyroid-carcinoma lines CAL-62 and BCPAP, stable over-expression, non-neural; p.Pro252Ala (a different SDR missense)",
         "UNUSABLE_UNVERIFIED_CARRIED",
         "protein much lower than wild type with mRNA not decreased; the assignment of statements to P252A versus P282A is UNVERIFIED at the original typography (variant superscripts dropped in the PMC text, IT6 P5 W09) and the context is over-expression in cancer lines",
         NR + ":O2 (PMID 41124647); FR-IT6P5:W09", "human", "D", "protein_or_phospho")
unusable("Q1", "STATE:FASTER_TURNOVER_OF_DESTABILISED_MISSENSE", "state", "function", "up", "human; thyroid-carcinoma lines CAL-62, BCPAP; p.Pro252Ala; cycloheximide chase",
         "UNUSABLE_UNVERIFIED_CARRIED", "faster turnover of the P252A protein; same assignment and over-expression limits as the abundance row; abundance and function are confounded in that study",
         NR + ":O2 (PMID 41124647)", "human", "D", "functional_effect")
reserved("Q1", "GO:0061684", "process", "function", "uncertain",
         "human; thyroid-carcinoma lines; p.Pro252Ala; chloroquine and ammonium chloride restore the protein, MG-132 and 3-MA do not",
         "pharmacological rescue pattern pointing at a lysosomal route; the abstract names HSC70-mediated chaperone-mediated autophagy which the manifest reads as the authors' speculation. This is an intervention-response datum on another allele in another cell type: held out so that the generator is not handed the route (process id is a search hint, not a claim that CMA acts on Q230P)",
         NR + ":O2 (PMID 41124647)", "human", "D", "functional_effect")
unusable("Q1", "STATE:STABLE_BUT_INERT_MISSENSE", "state", "function", "down", "human; thyroid-carcinoma lines; p.Pro282Ala (stable, loses POLE4 binding and tumour-suppressive function)",
         "UNUSABLE_UNVERIFIED_CARRIED", "reported separation of stable-but-inert from unstable; assignment unverified at source, cancer-assay-dead is not neurologically null; a proband homozygous for both had no WWOX-related nervous-system disease",
         NR + ":O2 (PMID 41124647); FR-IT6P5:W09", "human", "D", "functional_effect")
unusable("Q1", "WWOX", "gene", "function", "down", "human; in silico; the reference class's canonical splice-acceptor allele (worked example)", "UNUSABLE_PREDICTION_ONLY",
         "SpliceAI acceptor loss 0.96, cryptic acceptor gain 0.64 at +8, MaxEntScan 7.28 to -0.67; no transcript measurement of this allele exists in the sources read",
         "NEED-WWOX-SPLICE-CORRECTION:O2", "human", "D", "prediction")
unusable("Q1", "WWOX", "gene", "expression", "down", "human; in silico; 32 single-nucleotide stop-gained alleles of NM_016373.4 (ClinVar snapshot, undated)", "UNUSABLE_PREDICTION_ONLY",
         "23 predicted NMD-sensitive, 1 borderline, 8 predicted to escape by the 50-55 nt rule; no read-through or NMD measurement on WWOX exists; reference genotype class carries no premature stop in the stated analysis (itself resting on an unmeasured intron-8 retention prediction)",
         "NEED-WWOX-PTC-READTHROUGH:O1", "human", "D", "prediction")
reserved("Q1", "WWOX", "gene", "function", "up", "mouse; Wwox-null, neonatal neuron-promoter AAV9-WWOX; low versus high dose; survival to day 300",
         "dose-dependent survival (high dose plateau about 76-77 percent; low dose 0 percent by about day 77): intervention response, the answer a generator must not see",
         "NEED-WWOX-GENE-ADDITION:O1 (PMID 42422765)", "mouse", "B", "functional_effect", rc=RI)
reserved("Q1", "WWOX", "gene", "function", "up", "mouse; Wwox-null; AAV9-WWOX high dose; cortical ECoG, spike-wave discharges per hour about 0.635 to about 0.13",
         "endpoint under gene addition; held out", "NEED-WWOX-GENE-ADDITION:O2 (PMID 42422765)", "mouse", "B", "functional_effect", rc=RE)
reserved("Q1", "WWOX", "gene", "function", "up", "human; WWOX-null, WOREE and SCAR12 patient organoids; AAV9-WWOX versus AAV9-EGFP at week 10; spontaneous Ca2+ firing",
         "add-back response in human neural organoids; held out", "FR-IT6P5:W13; CM-IT7P4:Q14:ORG_PW,ORG_PS (PMID 42397075)", "human", "A", "functional_effect", rc=RI)
reserved("Q1", "WWOX", "gene", "function", "up", "Drosophila; neuronal Wwox CRISPRa in an Abeta42 model; lifespan and climbing", "expression-boost response in a fly amyloid model, not DEE; held out",
         "NEED-WWOX-ENDOGENOUS-BOOST:O1 (PMID 42909904)", "fly", "D", "functional_effect", rc=RI)

# ======================================================================================================================
# Q2 glycolysis / lactate / PDH / HIF1A  (partial or bridge)
# ======================================================================================================================
SN = "SN-IT7P1:derived_gene_values.tsv"
ORG = "human; cerebral organoid, WWOX knockout (exon deletion, WWOX mRNA not lower), week 15, bulk RNA-seq 4 KO v 2 WT libraries (GSE156243)"
HNPC = "human; H9-derived neural progenitors, shWWOX, CAGE, one library per arm (GSE126075)"
def g2(sym, od, hd, extra, guard=""):
    ctx = "two human neural systems read with one method: " + ORG + " | " + HNPC
    usable("Q2", sym, "gene", "expression", "up" if (od > 0.25 and hd > 0.25) else "uncertain", ctx,
           "centred log2 ratio organoid %+.3f, hNPC %+.3f; %s" % (od, hd, extra),
           "%s gene=%s;system_id=organoid_ko_w15,hnpc_shwwox_cage; DC-IT5P6/P7 matrix" % (SN, sym), "human", "A", "expression", guard)
IT7G = "The same six genes (SLC2A1, HK2, LDHA, LDHB, BNIP3 up; PDK1 down) were the IT7 P3 evaluation readout (signature reversal in wild-type LINCS cells, outcome opened in IT7): a generator seeded with them must not be scored by reversal of this readout; score on a different level (see questions.tsv Q2)"
g2("SLC2A1", 1.371, 0.524, "neuron d14 library disagrees (-0.348); single-gene value inside noise at n=1/4v2, module-level outside matched null", IT7G)
g2("HK2", 2.169, 0.614, "neuron d14 not measurable; mean counts 3,094 v 583 in organoid", IT7G)
g2("LDHA", 0.717, 1.258, "also +0.698 in neuron d14; falls with culture time in an unrelated spheroid series (maturity confound)", IT7G)
g2("LDHB", 0.327, 0.443, "neuron d14 flat (-0.076); mouse P17 argues against LDHA/LDHB", IT7G)
g2("BNIP3", 0.420, 0.546, "also +0.398 in neuron d14; the only readout gene that is a measured L1000 landmark", IT7G)
g2("PDK1", -0.385, -0.674, "lower in SIGN only: inside the single-gene null in both (p about 0.30 and 0.49) and the hNPC Poisson interval spans zero; neuron d14 +0.442; the HIF1A-PDK-PDH chain predicts the opposite", IT7G)
rows[-1]["direction"] = "uncertain"
usable("Q2", "HIF1A", "gene", "expression", "unchanged", "two human neural systems: organoid KO week 15 | shWWOX hNPC",
       "HIF1A mRNA flat (centred -0.285 organoid, -0.119 hNPC; neuron d14 -0.577); HIF activity would act at protein level, so mRNA is not informative about the axis",
       SN + " gene=HIF1A;system_id=organoid_ko_w15,hnpc_shwwox_cage,neuron_d14_shwwox_cage", "human", "A", "expression")
usable("Q2", "PDHA1", "gene", "expression", "uncertain", "two human neural systems: organoid KO week 15 (+0.968) | shWWOX hNPC (+0.145)",
       "organoid higher, hNPC near zero, neuron d14 -0.091; no PDH phosphorylation or activity observed in any neural system",
       SN + " gene=PDHA1;system_id=organoid_ko_w15,hnpc_shwwox_cage", "human", "A", "expression")
usable("Q2", "SET:GLYCOLYSIS_LACTATE_10", "process", "expression", "up",
       "two human neural systems: organoid KO week 15 (centred +0.53) | shWWOX hNPC (+0.46), both outside their own decile-matched random-set null; a broader 19-gene glycolysis panel is NOT distinguishable from chance in hNPC (+0.24, rank 0.20)",
       "HIF-type glycolysis/lactate set (members in process_ids.tsv) higher at transcript level; transcript is not flux; neuron d14 +0.20 at the null edge",
       "CM-IT7P4:Q05:ORG_KO,HNPC_KD,NEUR_KD; NEED-PDH-PYRUVATE-AXIS:O3,O4; NEED-LACTATE-LDH:O3,O5", "human", "A", "expression", IT7G)
usable("Q2", "SET:GLYCOLYSIS_LACTATE_10", "process", "expression", "unchanged",
       "mouse; P17 hippocampus (neuron-targeted S 3v2, progenitor-targeted N 2v2, null 2v3) and cortex S 3v4 (GSE158681/2)",
       "NOT MOVED in all four contrasts (centred -0.09, -0.19, -0.18, +0.11; none outside null); this is the third-system disagreement the human module has to survive",
       "CM-IT7P4:Q05:MS_HIP,MN_HIP,MNULL_HIP,MS_CTX; MP17-IT6P4:results/verdicts.tsv Glycolysis_lactate", "mouse", "B", "expression")
usable("Q2", "SET:GLYCOLYSIS_LACTATE_10", "process", "expression", "uncertain",
       "mouse; P47T knock-in homozygote hippocampus, bulk RNA-seq 5v5 (GSE215425)",
       "six-gene module +0.329, inside its null (95th percentile 0.389; exact one-sided p 0.060); registered IT7 verdict INCONCLUSIVE; LDHA +0.48, HK2 +0.66, SLC2A1 +0.18 in the build direction, LDHB -0.10 against; already used as the IT7 independent contrast, so spent as a held-out",
       "NEED-PDH-PYRUVATE-AXIS:O5; NEED-LACTATE-LDH:O6", "mouse", "B", "expression", IT7G)
usable("Q2", "HIF1A", "protein", "protein", "up", "mouse; Wwox-null embryonic fibroblasts (MEF), non-neural; normoxia (the difference disappears under hypoxia)",
       "HIF1alpha protein raised under normoxia; PDK1 raised at transcript level in the same cells; the only protein-level observation on the axis, in a non-neural proliferative cell type",
       "NEED-PDH-PYRUVATE-AXIS:O1 (PMID 25012504)", "mouse", "C", "protein_or_phospho")
usable("Q2", "PDK1", "gene", "expression", "up", "mouse; Wwox-null embryonic fibroblasts (MEF), non-neural", "PDK1 transcript raised in MEF (qRT-PCR); opposite in sign to the two human neural systems (lower in sign only)",
       "NEED-PDH-PYRUVATE-AXIS:O1 (PMID 25012504)", "mouse", "C", "expression")
usable("Q2", "GO:0004739", "process", "activity", "unchanged", "human; WWOX-knockout fibroblast line, non-neural; four oxygen x glucose conditions",
       "PDH activity shows no knockout-versus-control difference in any condition (n unstated); no PDK activity or protein measured; the only PDH activity measure in a human WWOX-loss cell",
       "NEED-PDH-PYRUVATE-AXIS:O2 (PMID 35328751)", "human", "C", "protein_or_phospho")
usable("Q2", "CHEBI:24996", "process", "function", "up", "human; WWOX-knockout fibroblast line, non-neural; all four oxygen x glucose conditions",
       "lactate higher in the knockout in all four conditions; cytoplasmic HIF1alpha lower in two of four conditions", "NEED-PDH-PYRUVATE-AXIS:O2 (PMID 35328751)", "human", "C", "functional_effect")
usable("Q2", "GO:0006096", "process", "function", "up", "mouse; Wwox-null embryonic fibroblasts, non-neural",
       "respiratory-to-glycolytic shift measured directly (flux-type readout, abstract-level in this repository), succinate only a non-significant trend",
       "NEED-MITOCHONDRIAL-RESPIRATION:O1 (PMID 25012504)", "mouse", "C", "functional_effect")
usable("Q2", "STATE:MITOCHONDRIAL_REDOX_ACTIVITY_RESAZURIN", "state", "function", "down",
       "human; H9-derived neural progenitors, shWWOX, 2D, undifferentiated; five time points over 270 min",
       "resazurin reduction (authors' mitochondrial redox activity, a dye readout, not OCR, ECAR, PDH or NAD) about 32 percent lower at 270 min, all five time points starred; replicates not described here",
       "NEED-MITOCHONDRIAL-RESPIRATION:O5 (PMID 31543760)", "human", "A", "functional_effect")
unusable("Q2", "CHEBI:24996", "process", "function", "down", "human; brain MRS, one WWOX patient (child), a confounding second variant recorded", "UNUSABLE_CASE_LEVEL",
         "cerebral lactate 'extremely low', opposite to the Warburg-type prediction; n=1 with a confounding variant", "NEED-LACTATE-LDH:O4", "human", "C", "functional_effect")
unusable("Q2", "CHEBI:24996", "process", "function", "uncertain", "Drosophila; neuronal Wwox RNAi head; with versus without Abeta42", "UNUSABLE_OTHER_CONTEXT",
         "lactate and Ldh up only with Abeta42, nominally lower without; whole-head ATP no difference; amyloid-dependent fly context, not DEE", "NEED-LACTATE-LDH:O1; NEED-MITOCHONDRIAL-RESPIRATION:O3 (PMID 42909904)", "fly", "D", "functional_effect")
unusable("Q2", "SET:OXPHOS_NUCLEAR_73", "process", "expression", "down", "human organoid, hNPC, neurons; mouse P17", "UNUSABLE_NONSPECIFIC",
         "nuclear OXPHOS transcripts move no more than an unrelated cytosolic-ribosome control set in every contrast (organoid -0.20 v -0.26; neuron -0.33 v -0.47): no OXPHOS-specific shift",
         "NEED-MITOCHONDRIAL-RESPIRATION:O7; CM-IT7P4:Q08", "human", "A", "expression")
unusable("Q2", "STATE:HUMAN_SYSTEMIC_METABOLIC_SCREENS_NORMAL", "state", "function", "unchanged", "human; blood, urine, muscle biopsy, brain MRS in WWOX cases where done", "UNUSABLE_CASE_LEVEL",
         "reported normal in the cases tested (count disputed in the map: one complete screen plus one MRS case in the opposite direction); peripheral, not neural", "NEED-MITOCHONDRIAL-RESPIRATION:O4", "human", "C", "functional_effect")
reserved("Q2", "LDHA", "gene", "function", "down", "Drosophila; Ldh RNAi in Wwox-knockdown + Abeta42 flies; climbing days 14-28", "partial rescue by Ldh knockdown in the fly amyloid model: intervention response, held out",
         "NEED-LACTATE-LDH:O2 (PMID 42909904)", "fly", "D", "functional_effect", rc=RI)
reserved("Q2", "STATE:SEIZURE_BURDEN", "state", "pathology", "uncertain", "human; ketogenic diet in 3 of 5 patients (clinician-reported seizure control), series", "dietary response, case-level, no instrument: held out; also the main reason the lactate axis was explored",
         "NEED-SEIZURE-CONTROL-SYMPTOMATIC:O1 (PMID 36537114)", "human", "C", "clinical_response", rc=RI)

# ======================================================================================================================
# Q3 integrated stress response, proteostasis-adjacent and mitochondrial translation stress  (partial or bridge)
# ======================================================================================================================
P7K = "P7:hnpc_gse126075_it5_20261029/p7_organoid_key_genes.tsv gene=%s; P6:hnpc_gse126075_it5_20261029/per_gene_in_sets.tsv set=ISR_targets;contrast=C_hNPC,C_neuron;symbol=%s"
def isr(sym, o, h, d, extra):
    usable("Q3", sym, "gene", "expression", d,
           "two human neural systems with opposite set-level sign: organoid KO week 15 (4v2) | shWWOX hNPC (n=1 library) [neuron d14 in reason]",
           "centred log2 ratio organoid %+.3f, hNPC %+.3f; %s" % (o, h, extra), P7K % (sym, sym), "human", "A", "expression",
           "ISR set direction is the unresolved variable: do not score candidates by reversal of an ISR transcript set before the sign is resolved")
isr("CHAC1", -0.763, 2.597, "uncertain", "organoid t -11.6 (solid); hNPC rise rests on 134 v 47 tags; neuron d14 +3.14; seen before the sets were fixed, so per-gene direction is not blind")
isr("TRIB3", -0.682, 1.217, "uncertain", "organoid t -4.1; neuron d14 +1.85")
isr("SESN2", -0.393, 0.977, "uncertain", "organoid t -4.3; neuron d14 +1.23")
isr("PSAT1", 0.390, 1.342, "up", "the only ISR-set gene up in every system measured (neuron d14 +1.64); a serine-pathway gene that also moves with proliferation")
isr("ATF5", -0.428, 0.821, "uncertain", "neuron d14 sparse (31 v 6 tags)")
usable("Q3", "ATF4", "gene", "expression", "unchanged", "organoid KO week 15 (-0.229) | shWWOX hNPC (-0.155); neuron d14 sparse (6 v 41 tags, below the 10-tag rule); mouse P17 lower in sign only (-0.16 to -0.71)",
       "ATF4 mRNA flat; ATF4 is translationally controlled, so its transcript is not ATF4 activity", "CM-IT7P4:Q01:ORG_KO,HNPC_KD,NEUR_KD,MS_HIP,MN_HIP,MNULL_HIP,MS_CTX", "human", "A", "expression")
usable("Q3", "SET:ISR_TARGETS_12", "process", "expression", "uncertain",
       "organoid KO week 15: LOWER (-0.33, outside null; P 0.0005 uncorrected over nine set tests) | shWWOX hNPC HIGHER (+0.64) | neuron d14 HIGHER (+1.32, composition-sensitive)",
       "opposite signs from systems of very different design; the direction of the human ISR transcript signal is UNRESOLVED; pre-declared set, per-gene seen first for CHAC1/TRIB3/PHGDH",
       "CM-IT7P4:Q02; NEED-ISR-ATTENUATION:O2,O7,O8", "human", "A", "expression",
       "ISR set direction is the unresolved variable: do not score candidates by reversal of an ISR transcript set before the sign is resolved")
usable("Q3", "SET:ISR_TARGETS_12", "process", "expression", "unchanged", "mouse; P17 hippocampus (S, N, null) and cortex S; GSE158681/2",
       "no resolvable sign at about 0.3 in any contrast (+0.13, -0.13, -0.02, +0.05); an organoid-sized fall is not excluded in the 2v2 contrast",
       "CM-IT7P4:Q02:MS_HIP,MN_HIP,MNULL_HIP,MS_CTX; MP17-IT6P4:results/verdicts.tsv ISR_targets", "mouse", "B", "expression")
usable("Q3", "SET:MITO_TRANSLATION_MRP", "process", "expression", "uncertain",
       "organoid KO week 15 LOWER (-0.154, outside null) | shWWOX hNPC HIGHER (+0.281, outside null; authors' GSEA mitochondrial translation q 0.119) | mouse mixed (lower in N, higher in cortex S)",
       "discordant signs between designs that are not comparable one to one", "CM-IT7P4:Q09; NEED-MITOCHONDRIAL-RESPIRATION:O6,O7", "human", "A", "expression")
for goid, lab, q in (("GO:0042254", "ribosome biogenesis", "q 0.055"), ("GO:0008652", "amino acid biosynthesis and metabolism (paper's term alpha-amino acid biosynthetic process, q 0.065, is obsolete in GO; nearest current term)", "q 0.065 to 0.175"),
                     ("GO:0006418", "tRNA aminoacylation for protein translation (paper's term amino acid activation, q 0.173, is obsolete in GO; nearest current term)", "q 0.173"),
                     ("GO:1904292", "regulation of ERAD pathway", "q 0.091")):
    usable("Q3", goid, "process", "expression", "up", "human; H9-derived neural progenitors, shWWOX, CAGE, one library per arm, undifferentiated (authors' GSEA, GSE126075)",
           "%s: set on the knockdown side (%s, nominal FDR below 0.25); the sign is derived from the GSEA convention (IT5 P6 adjudication, not printed by the paper); n=1; no ISR/UPR/ER-stress/amino-acid-starvation set named in either table" % (lab, q),
           "NEED-ISR-ATTENUATION:O7; NEED-MITOCHONDRIAL-RESPIRATION:O6; DC-IT5P6:section 1 (PMID 31543760)", "human", "A", "expression")
unusable("Q3", "ATF4", "protein", "protein", "uncertain", "any WWOX-deficient neural system", "GAP_NOT_MEASURED",
         "no ATF4 protein (or puromycin, ribosome profiling) measurement found in a WWOX-deficient neural system by the IT6 P3 search (not found is not shown absent)", "DC-IT6P3:section 0.1, 3(b)", "human", "A", "protein_or_phospho")
unusable("Q3", "EIF2S1", "protein", "phospho", "uncertain", "any WWOX-deficient neural system", "GAP_NOT_MEASURED",
         "no eIF2alpha-P measurement in a WWOX-deficient neural system found; the gene is EIF2S1 (protein eIF2alpha)", "DC-IT6P3:section 0.1, 3(b)", "human", "A", "protein_or_phospho")
unusable("Q3", "EIF2AK3", "protein", "phospho", "uncertain", "any WWOX-deficient neural system (PERK; GCN2 = EIF2AK4)", "GAP_NOT_MEASURED",
         "PERK/GCN2 activation unmeasured in a WWOX-deficient neural system; the only PERK band is a total-PERK shift in non-neural ovarian cells with no change reported", "DC-IT6P3:section 0.1; gcn2_perk_measurement_gap_it3_20261028.md", "human", "A", "protein_or_phospho")
unusable("Q3", "EIF2S1", "protein", "phospho", "unchanged", "human; WWOX-null versus add-back ovarian cancer cells (non-neural); phospho-eIF2A and phospho-IRE-1 blots", "UNUSABLE_UNVERIFIED_CARRIED",
         "authors report no change by WWOX status; carried from the IT6 P3 census, not opened at source here; non-neural cancer cells", "DC-IT6P3:section 0.1 (PMID 28749468)", "human", "C", "protein_or_phospho")
unusable("Q3", "ATF4", "protein", "protein", "up", "Drosophila; neuronal Wwox RNAi adult brain, day 14; six brains per group", "UNUSABLE_OTHER_CONTEXT",
         "Atf4 immunofluorescence about 1.0 to 1.28 only with neuronal Abeta42 (P 0.0022); not significant without amyloid (P 0.93; interval about +/-1.3 SD, so an effect of that size is not excluded); no interaction test; amyloid-dependent fly context",
         "NEED-ISR-ATTENUATION:O1 (PMID 42909904)", "fly", "D", "protein_or_phospho")

# ======================================================================================================================
# Q4 excitation-inhibition state, inhibitory interneurons  (partial or bridge)
# ======================================================================================================================
NS = "mouse; Synapsin-Cre neuron-specific Wwox deletion, neocortical slices layer II/III, P13-P17"
usable("Q4", "STATE:NETWORK_HYPEREXCITABILITY", "state", "pathology", "up", NS + " (and Wwox-null in vivo)",
       "presence of the phenotype only: spontaneous slice bursting in 36 of 42 knockout, 4 of 23 heterozygote, 0 of 11 wild-type slices; replicated as higher hyperexcitability across systems (organoid, mouse deposits, P47T, patient organoids) at function level",
       "NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR:O1 (PMID 34634460); CM-IT7P4:Q14", "mouse", "B", "functional_effect",
       "burst frequency, seizure stage, SWD rate are held-out endpoints: never use their change under a compound as the evaluation of a seed that came from the same slices")
usable("Q4", "STATE:NETWORK_HYPEREXCITABILITY", "state", "pathology", "up", "human; WWOX-knockout cerebral organoids (LFP, week 7) and WOREE/SCAR12 patient-derived organoids (Ca2+ imaging, weeks 7 and 16)",
       "knockout organoid LFP spectral power higher at week 7 (the first recording) and then falling over time; patient lines firing higher than wild type at weeks 7 and 16 (WOREE about 3-fold above SCAR12 at week 16); one laboratory; organoid-age dependent",
       "CM-IT7P4:Q14:ORG_KO,ORG_PW,ORG_PS; FR-IT6P5:W13", "human", "A", "functional_effect")
usable("Q4", "STATE:INHIBITORY_SYNAPTIC_DRIVE", "state", "function", "down", NS + "; layer II/III pyramidal neurons",
       "spontaneous inhibitory current amplitude more than halved (control 57.3 pA, pooled WT+het, v knockout 27.5 pA); the largest separation of the synaptic readouts",
       "NEED-INHIBITORY-HYPOFUNCTION:O1 (PMID 34634460)", "mouse", "B", "functional_effect")
usable("Q4", "STATE:EXCITATORY_SYNAPTIC_AMPLITUDE", "state", "function", "uncertain", NS + "; layer II/III pyramidal neurons",
       "spontaneous excitatory amplitude 23.3 v 24.7 pA; miniature and spontaneous amplitude curves almost superimposed with a sliver separation marked significant: unchanged to slight",
       "NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR:O3 (PMID 34634460)", "mouse", "B", "functional_effect")
usable("Q4", "STATE:RESTING_MEMBRANE_POTENTIAL", "state", "function", "up", NS + "; layer II/III pyramidal neurons",
       "more depolarised at rest: -79.25 mV WT, -75.51 mV heterozygote, -73.62 mV knockout (het and KO marked different from WT); in vitro preparation holds neurons more hyperpolarised than in vivo",
       "NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR:O6 (PMID 34634460)", "mouse", "B", "functional_effect")
usable("Q4", "PVALB", "protein", "protein", "down", "mouse; Wwox constitutive null, hippocampus (dentate, CA1, whole), two weeks; immunostaining counts",
       "PV-positive interneuron counts reduced by 44 percent (CA3 no mark); systemic null, so systemic illness is a confound", "NEED-INHIBITORY-HYPOFUNCTION:O2 (PMID 30290271)", "mouse", "B", "protein_or_phospho")
usable("Q4", "GAD1", "protein", "protein", "down", "mouse; Wwox constitutive null, hippocampus, two weeks; western, five lanes per genotype",
       "GAD65/67 protein lower on combined densitometry (the antibody does not separate GAD1 from GAD2)", "NEED-INHIBITORY-HYPOFUNCTION:O2 (PMID 30290271)", "mouse", "B", "protein_or_phospho")
usable("Q4", "GAD2", "protein", "protein", "down", "mouse; Wwox constitutive null, hippocampus, two weeks; western, five lanes per genotype",
       "same combined GAD65/67 densitometry as the GAD1 row", "NEED-INHIBITORY-HYPOFUNCTION:O2 (PMID 30290271)", "mouse", "B", "protein_or_phospho")
usable("Q4", "NPY", "protein", "protein", "down", "mouse; Wwox constitutive null, hippocampus dentate gyrus; NPY-positive interneuron counts",
       "reduced by about 30 percent in the dentate gyrus only (CA1, CA3 no obvious difference); human knockout organoid NPY transcript also strongly down (log2 -6.24)",
       "NEED-INHIBITORY-HYPOFUNCTION:O2,O3 (PMID 30290271, 34268881)", "mouse", "B", "protein_or_phospho")
usable("Q4", "GAD1", "gene", "expression", "uncertain", "human; WWOX-knockout cerebral organoids week 8-15 (transcript, deposit tables) and GAD67 surface area per nucleus",
       "GAD1 transcript about 8.5 v 1 in knockout and GAD67 area about 1.0 v 0.2: GABAergic markers UP, opposite to the mouse protein; composition (neurons lost, radial glia gained in the engineered knockout) can explain it; wild-type GAD1 values are 3.46 and 0.20 (two libraries)",
       "NEED-INHIBITORY-HYPOFUNCTION:O3 (PMID 34268881); NEED-GABA-CHLORIDE-GRADIENT:O2", "human", "A", "expression",
       "the protein-versus-transcript split (rescue normalises GAD67 area but not transcript) is an add-back response and is held out")
usable("Q4", "GABRB2", "gene", "expression", "down", "human; WWOX-knockout organoid week 15, bulk RNA, 4 KO v 2 WT",
       "about a quarter of wild type (KO mean 2.7 v WT 10.2 CPM); composition cannot be excluded", "NEED-INHIBITORY-HYPOFUNCTION:O5", "human", "A", "expression")
usable("Q4", "GABRB3", "gene", "expression", "down", "human; WWOX-knockout organoid week 15, bulk RNA, 4 KO v 2 WT",
       "about half of wild type (18.5 v 37.7 CPM); composition cannot be excluded", "NEED-INHIBITORY-HYPOFUNCTION:O5", "human", "A", "expression")
unusable("Q4", "STATE:INHIBITORY_POSTSYNAPTIC_POTENTIAL", "state", "expression", "uncertain", "mouse; P47T knock-in hippocampus/cortex enrichment analyses (80-250 days)", "UNUSABLE_NOT_EVALUABLE",
         "GO inhibitory postsynaptic potential in the ACTIVATED column while KEGG of the same tissue is read as suppression; cortex GABAergic and glutamatergic terms both suppressed: mixed, no signed reading", "NEED-INHIBITORY-HYPOFUNCTION:O4 (PMID 36828035)", "mouse", "B", "expression")
unusable("D3", "SLC12A5", "gene", "expression", "unchanged", "human; WWOX-knockout organoid week 15, NKCC1/KCC2 transcript ratio", "GAP_NOT_MEASURED",
         "ratio 0.24-0.29-0.13-0.14 in four knockouts v 0.29-0.30 in two wild types (not higher); E_GABA, intracellular chloride and GABA response are unmeasured in any WWOX system", "NEED-GABA-CHLORIDE-GRADIENT:O1,O2", "human", "A", "expression")
reserved("Q4", "STATE:NMDAR_DEPENDENCE_OF_BURSTING", "state", "function", "down", NS, "d-APV (competitive NMDAR antagonist) abolishes bursting (n 5 slices from 3 animals; no variance); this is the pharmacological answer for the glutamate-receptor node, held out",
         "NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR:O2,O8 (PMID 34634460)", "mouse", "B", "functional_effect", rc=RI)
reserved("Q4", "PANX1", "gene", "function", "up", NS, "pannexin blocker (brilliant blue FCF) raised burst frequency to about 2.55, untested; carbenoxolone suppressed bursts but is not attributable to gap junctions: drug responses, held out",
         "NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR:O4 (PMID 34634460)", "mouse", "B", "functional_effect", rc=RI)
reserved("Q4", "CACNA1G", "gene", "function", "down", "mouse; Wwox-null pups, PTZ-provoked seizure score late phase; ethosuximide", "ethosuximide suppressed the late phase only in the null genotype (drug-by-genotype interaction not tested): drug response, held out",
         "NEED-T-TYPE-CALCIUM:O1 (PMID 32000863)", "mouse", "B", "functional_effect", rc=RI)
reserved("Q4", "STATE:SEIZURE_BURDEN", "state", "pathology", "up", "mouse; neuron-specific deletion spontaneous tonic-clonic seizures from P9; null spike-wave discharges about 0.635 per hour v about 0.03 in wild type",
         "seizure and SWD burden are the primary held-out endpoints of the question", "NEED-WWOX-GENE-ADDITION:O2; CM-IT7P4:Q14 (PMID 33914858, 42422765)", "mouse", "B", "functional_effect", rc=RE)
reserved("Q4", "STATE:SEIZURE_BURDEN", "state", "pathology", "uncertain", "human; vigabatrin, cannabidiol, ACTH/corticosteroid/phenobarbital regimens, ketogenic diet; case reports and series",
         "mixed, case-level clinician-reported responses without comparator or genotype stratification: held out so that the generator does not collapse onto antiseizure agents",
         "NEED-SEIZURE-CONTROL-SYMPTOMATIC:O1,O2,O3", "human", "C", "clinical_response", rc=RI)

# ======================================================================================================================
# Q5 myelination and glial state, non-cell-autonomous  (partial or bridge)
# ======================================================================================================================
usable("Q5", "GO:0042552", "process", "pathology", "down", "mouse; Synapsin-Cre neuron-specific Wwox deletion, corpus callosum and optic nerve, P17",
       "myelin deficit (about 3.3 times fewer myelinated axons, authors' counts) arises from neuron-specific deletion; the state (hypomyelination caused by loss in neurons) is the seed, the count is the endpoint",
       "NEED-MYELINATION:O1; NEED-WWOX-GENE-ADDITION:O3 (PMID 33914858)", "mouse", "B", "functional_effect",
       "the myelinated-axon count, g-ratio and CC1+/PDGFRA+ counts are held-out endpoints of any pro-myelinating or add-back candidate")
usable("Q5", "STATE:OLIGODENDROCYTE_OR_ASTROCYTE_SPECIFIC_DELETION_NO_PHENOTYPE", "state", "function", "unchanged",
       "mouse; Olig2-Cre and GFAP-Cre Wwox deletion; development, weight, survival scored",
       "no evident anomaly (no gliosis, EEG or seizure measurement reported for them in the passages read; a cell-autonomous astroglial function is not excluded): the myelin deficit is non-cell-autonomous, driven from neurons",
       "NEED-MYELINATION:O1; NEED-NEUROINFLAMMATION-GLIA:O5 (PMID 33914858)", "mouse", "B", "functional_effect")
usable("Q5", "SET:MYELIN_OL_10", "process", "expression", "down", "mouse; P17 hippocampus S, N, null and cortex S (GSE158681/2)",
       "lower in all four contrasts (centred -1.78, -1.02, -1.66, -0.80, outside null); the registered verdict is NOT MOVED because control-versus-control contrasts (Cre line) are also outside null and the ribosome control moves with the same sign in one contrast: a direction with a Cre-line artefact risk",
       "CM-IT7P4:Q12:MS_HIP,MN_HIP,MNULL_HIP,MS_CTX; MP17-IT6P4:results/verdicts.tsv Myelin_OL", "mouse", "B", "expression")
usable("Q5", "GFAP", "protein", "protein", "up", "mouse; Wwox constitutive null, hippocampus (CA1, CA3, whole) two weeks; and null brain P20 (region not stated)",
       "IBA1 and GFAP area fractions increased at two weeks; at P20 GFAP area about 3.7 (WT) v 23.7 (KO) percent; the earliest spike activity in the same paper starts about P14, so no glial read exists before that age",
       "NEED-NEUROINFLAMMATION-GLIA:O1,O6 (PMID 30290271, 42422765)", "mouse", "B", "protein_or_phospho")
usable("Q5", "AIF1", "protein", "protein", "up", "mouse; Wwox constitutive null; hippocampus two weeks (IBA1 protein symbol = AIF1) and P20 (Iba1 area about 4.5 v 7.6 percent)",
       "much smaller than GFAP (about 1.7-fold v six-fold); in the neuronal-AAV9 supplement the Iba1 panel shows no significant difference among arms",
       "NEED-NEUROINFLAMMATION-GLIA:O1,O3,O6 (PMID 30290271, 42422765)", "mouse", "B", "protein_or_phospho")
usable("Q5", "GFAP", "protein", "protein", "up", "mouse; P47T knock-in homozygote; hippocampus, cortex, cerebellum; 80 to 250 days",
       "astrogliosis progressive in number and area; microglial abundance not shown to change with age (only morphology)", "NEED-NEUROINFLAMMATION-GLIA:O2 (PMID 36828035)", "mouse", "B", "protein_or_phospho")
usable("Q5", "GFAP", "protein", "protein", "down", "rat; lde/lde (13 bp exon 9 deletion) cerebral cortex PND 5-21; at least 3 males per genotype per age",
       "GFAP-positive cells LOWER than wild type from PND 5 (e.g. about 470 v 255, then 1570 v 850 per mm2 at the last age as printed); Iba1 equal at PND 5 then lower; the opposite sign from mouse null and P47T",
       "NEED-NEUROINFLAMMATION-GLIA:O4 (PMID 31340538)", "rat", "B", "protein_or_phospho")
usable("Q5", "IL1B", "gene", "expression", "up", "mouse; P47T knock-in homozygote cerebellum, qPCR/RNA-seq n 6 per group", "IL1B and TNF transcripts at least two-fold up in mutant cerebellum; distributions overlap the wild-type range; regulator activation is a transcriptomic inference, not a cytokine measurement",
       "NEED-NEUROINFLAMMATION-GLIA:O2 (PMID 36828035)", "mouse", "B", "expression")
usable("Q5", "TNF", "gene", "expression", "uncertain", "mouse; P47T cerebellum (at least two-fold up) versus Wwox-null hippocampus qPCR (Tnf not significant, n 4)",
       "sign not consistent across the two mouse models", "NEED-NEUROINFLAMMATION-GLIA:O1,O2 (PMID 30290271, 36828035)", "mouse", "B", "expression")
usable("Q5", "IL6", "gene", "expression", "up", "mouse; Wwox constitutive null hippocampus two weeks, qPCR n 4 per group (registry reading)", "Il6, not Tnf, significant by qPCR", "NEED-NEUROINFLAMMATION-GLIA:O1 (PMID 30290271)", "mouse", "B", "expression")
unusable("Q5", "STATE:REACTIVE_GLIAL_PROGRAMME", "state", "expression", "unchanged", "human; WWOX-knockout cerebral organoid week 15, bulk RNA; microglial markers at or near zero", "UNUSABLE_NOT_EVALUABLE",
         "no reactive programme (only VIM, CD44 raised, progenitor-associated); the system has no microglia and no annotated oligodendrocyte cluster, so it cannot test glial reactivity or myelination", "NEED-NEUROINFLAMMATION-GLIA:O7; NEED-MYELINATION:O3 (PMID 42397075)", "human", "A", "expression")
unusable("Q5", "MBP", "gene", "expression", "up", "human; WWOX-knockout organoid week 15 (MBP +0.625, PLP1 +0.863); shWWOX hNPC PLP1 -1.67 on 25-32 tags", "UNUSABLE_NOT_EVALUABLE",
         "oligodendrocyte genes are not expressed meaningfully in these systems; unplanned look; no oligodendrocyte population", "SN-IT7P1:derived_gene_values.tsv gene=MBP,PLP1; NEED-MYELINATION:O3", "human", "A", "expression")
unusable("Q5", "STATE:HETEROZYGOUS_UNCHALLENGED_GLIA_NORMAL", "state", "protein", "unchanged", "mouse; P47T heterozygote, unchallenged; Iba1 and Gfap immunostaining", "UNUSABLE_UNVERIFIED_CARRIED",
         "reported as no difference from wild type, declared 'data not shown': an unverifiable negative that may not be cited as heterozygote normality", "NEED-NEUROINFLAMMATION-GLIA:O9 (PMID 36828035)", "mouse", "B", "protein_or_phospho")
unusable("Q5", "STATE:ASTROCYTE_ACTIVATION_GENES_IN_DEG_LIST", "state", "expression", "uncertain", "mouse; neuron-specific deletion P17 cortex 4v3 and hippocampus 2v3", "UNUSABLE_DIRECTION_NOT_TABULATED",
         "genes elicited during epileptic insults 'including activation of astrocytes' among top differentially expressed genes; individual genes and direction not tabulated", "NEED-NEUROINFLAMMATION-GLIA:O10 (PMID 33914858)", "mouse", "B", "expression")
unusable("Q5", "GFAP", "gene", "expression", "unchanged", "mouse; P47T homozygote thresholded differential-expression sheets (two-fold, forebrain regions)", "UNUSABLE_NOT_EVALUABLE",
         "Gfap, Aif1, Il1b, Tnf, Il6, Lcn2, Serpina3n, Nlrp3, Stat3, Socs3 are not listed in any region: absence from a thresholded list is not a measurement of no change", "NEED-NEUROINFLAMMATION-GLIA:O8 (PMID 36828035)", "mouse", "B", "expression")
reserved("Q5", "GFAP", "protein", "protein", "down", "mouse; Wwox-null, neuron-restricted AAV9-WWOX; GFAP-positive cells about 44 (KO) v about 5 (WT) v about 5 (treated)", "gliosis lowered by neuronal add-back: intervention response, held out",
         "NEED-NEUROINFLAMMATION-GLIA:O3 (PMID 42422765)", "mouse", "B", "protein_or_phospho", rc=RI)
reserved("Q5", "GO:0042552", "process", "pathology", "up", "mouse; neuronal AAV9 rescue: g-ratio normalises, CC1+ and PDGFRA+ counts toward WT, unmyelinated axons about two-fold above WT", "partial myelin rescue by add-back: held-out endpoint; the source reports WWOX absent from oligodendrocytes (not transduced)",
         "NEED-MYELINATION:O2 (PMID 34747138)", "mouse", "B", "functional_effect", rc=RE)

# ======================================================================================================================
# Dropped questions D1..D6 (rows kept so a verifier can re-derive why they are unusable)
# ======================================================================================================================
D1 = "UNUSABLE_MATURITY_OR_COMPOSITION"
for sym, v in (("AXIN2", "+0.79"), ("LEF1", "+1.00"), ("TCF7L2", "+1.04"), ("CTNNB1", "+0.56"), ("NKD1", "+1.23"), ("WNT8B", "+3.17")):
    unusable("D1", sym, "gene", "expression", "up", "human; WWOX-knockout cerebral organoids week 15, bulk RNA (padj at most 1.6e-2)", D1,
             "log2 %s; Wnt readouts move with elapsed culture time in 62 unperturbed spheroid samples; the 4v2 permutation reanalysis could not separate a WWOX effect from composition/maturity (min single-gene p 1/15); symbol note: the Wnt factor the papers call TCF4 is TCF7L2, HGNC TCF4 is a different gene" % v,
             "NEED-WNT-BETA-CATENIN:O1,O4 (PMID 34268881)", "human", "A", "expression")
unusable("D1", "MYC", "gene", "expression", "up", "human; WWOX-deficient radial glia, organoid single-cell RNA-seq", D1, "top upregulated gene in WWOX-deficient radial glia; radial glia shifted toward S/G2M without error bars; engineered knockout composition differs (neurons lost, radial glia up)",
         "NEED-MYC-PROGENITOR-PROLIFERATION:O1 (PMID 42397075)", "human", "A", "expression")
unusable("D1", "MYC", "protein", "protein", "up", "human; engineered knockout and two patient-derived organoid lines, week 16; MYC+ fraction of SOX2+ cells", D1,
         "about 60, 50 and 55 percent v about 20 percent in WT, up in all three lines; patient lines sit close to WT in composition but invert the early/late neuronal balance (Fig 5F): maturity not excluded",
         "NEED-MYC-PROGENITOR-PROLIFERATION:O2 (PMID 42397075)", "human", "A", "protein_or_phospho")
reserved("D1", "MYC", "protein", "function", "down", "human; knockout organoids with A51 (multi-kinase inhibitor)", "SOX2+ 60 to 33 percent, NEUN+ 6 to 18 percent: drug response, held out", "NEED-MYC-PROGENITOR-PROLIFERATION:O3 (PMID 42397075)", "human", "A", "functional_effect", rc=RI)
DD = "UNUSABLE_DROPPED_QUESTION"
reserved("D1", "CTNNB1", "gene", "expression", "uncertain", "human; WWOX-knockout organoids, AAV-WWOX add-back, qPCR bar heights read from Figure 4D", "Wnt ligands WNT1/WNT3/WNT5A/ROR2 toward wild type, WNT3A below, WNT2B/WNT8B and effectors LEF1/TCF7/TCF4-plotted further from wild type under add-back: add-back response, held out",
         "NEED-WNT-BETA-CATENIN:O2 (PMID 34268881)", "human", "A", "expression", rc=RI)
unusable("D2", "GSK3B", "protein", "phospho", "down", "mouse; Wwox-null cerebellum, hippocampus, cortex lysates, P20; western (images), n=3", DD,
         "inhibitory Ser9 phosphorylation lower with total GSK3B unchanged; the only phospho measurement in neural WWOX-loss tissue, but one laboratory, n=3, images only, kinase activity not measured, and WWOX docking inhibition of GSK3B is S9-independent in SH-SY5Y",
         "NEED-GSK3B-DEREPRESSION:O1,O2 (PMID 32000863, 22193544)", "mouse", "B", "protein_or_phospho")
for sym, d, v in (("EIF4EBP1", "down", "log2 -0.87, adj P 5.8e-4"), ("RB1CC1", "down", "log2 -0.99"), ("MTOR", "up", "+0.4, adj P 0.0498"), ("DEPTOR", "up", "+1.16")):
    unusable("D2", sym, "gene", "expression", d, "human; WWOX-knockout organoid, bulk RNA, weeks 8-15", DD, "transcript %s; nothing at protein or phospho level; mixed signs" % v, "NEED-MTOR-AUTOPHAGY:O1 (PMID 34268881)", "human", "A", "expression")
unusable("D3", "SLC12A2", "gene", "expression", "unchanged", "human; WWOX-knockout organoid, NKCC1 transcript", "GAP_NOT_MEASURED", "no E_GABA, chloride or GABA response measured in any WWOX system; transcript ratio not higher", "NEED-GABA-CHLORIDE-GRADIENT:O1,O2", "human", "A", "expression")
reserved("D5", "STATE:SYSTEMIC_GLYCAEMIA_AND_GROWTH", "state", "function", "down", "mouse null P10-P30 (glucose about 95 v 130; weight lower from birth) and 5 WOREE patients (failure to thrive)", "endpoint and confounder of every null-mouse readout; held out",
         "NEED-SYSTEMIC-GLYCAEMIA-GROWTH:O1,O2 (PMID 42422765, 36537114)", "mouse", "B", "functional_effect", rc=RE)
unusable("D6", "SOD1", "gene", "function", "uncertain", "Drosophila wing mitochondrial H2O2 reporter (up); diabetic mouse photoreceptors (WWOX up, knockdown lowers superoxide); fly CM-H2DCFDA (Wwox loss lowers)", "UNUSABLE_OTHER_CONTEXT",
         "sign runs counter-directionally in two independent non-DEE systems; no neural WWOX-loss redox measurement; target SOD1 is a need-table pathway member, not an observation", "NEED-REDOX-OXIDATIVE-STRESS:O1,O2", "fly", "D", "functional_effect")

# ======================================================================================================================
PROCESSES = [
 ("SET:GLYCOLYSIS_LACTATE_10", "HIF-type glycolysis and lactate set (10 declared genes)", "gene_set", "SLC2A1,HK2,PFKP,ALDOA,PGK1,ENO1,LDHA,PKM,BNIP3,LDHB", "subnetwork_it7_p1_20261029/subnetwork.py GLY10"),
 ("SET:ISR_TARGETS_12", "canonical ATF4/ISR target set (12 declared; 11 measurable in the CAGE systems)", "gene_set", "ASNS,ATF5,CHAC1,DDIT3,GADD45A,PCK2,PHGDH,PSAT1,PSPH,SESN2,TRIB3,SLC7A11", "hnpc_gse126075_it5_20261029/per_gene_in_sets.tsv set=ISR_targets + p4_mouse_same_sets.py extra SLC7A11"),
 ("SET:MITO_TRANSLATION_MRP", "mitochondrial translation set (MRPL/MRPS and translation factors; 78 genes in the hNPC table)", "gene_set", "MRPL*,MRPS*,GFM1,GFM2 (members in hnpc_gse126075_it5_20261029/per_gene_in_sets.tsv set=Mito_translation)", "hnpc_gse126075_it5_20261029/per_gene_in_sets.tsv"),
 ("SET:MYELIN_OL_10", "myelin/oligodendrocyte set (10 declared genes; UGT8A in the declaration is mouse Ugt8a = HGNC UGT8)", "gene_set", "MBP,PLP1,MOG,MAG,MOBP,CLDN11,CNP,MAL,OPALIN,UGT8", "mouse_wwox_p17_it6_p4_20261029/p4_mouse_same_sets.py sets_h['Myelin_OL']"),
 ("SET:OXPHOS_NUCLEAR_73", "nuclear OXPHOS transcript set (73 genes)", "gene_set", "(members in hnpc_gse126075_it5_20261029/per_gene_in_sets.tsv set=OXPHOS_nuclear)", "hnpc_gse126075_it5_20261029/per_gene_in_sets.tsv"),
 ("GO:0004739", "pyruvate dehydrogenase (acetyl-transferring) activity", "go_mf", "PDHA1,PDHB (activity, not expression)", "QuickGO 2026-10-30; current"),
 ("GO:0006096", "glycolysis (GO label; the IT7 P1 table calls it glycolytic process)", "go_bp", "", "QuickGO 2026-10-30; current"),
 ("CHEBI:24996", "lactate", "metabolite", "", "subnetwork_it7_p1_20261029/nodes.tsv"),
 ("GO:0061684", "chaperone-mediated autophagy (search hint only)", "go_bp", "", "QuickGO 2026-10-30; current"),
 ("GO:0042254", "ribosome biogenesis", "go_bp", "", "QuickGO 2026-10-30; current"),
 ("GO:0008652", "amino acid biosynthetic process (nearest current term to the obsolete GO:1901607 the paper's table names)", "go_bp", "", "QuickGO 2026-10-30; GO:1901607 obsolete, no replacement"),
 ("GO:0006418", "tRNA aminoacylation for protein translation (nearest current term to the obsolete GO:0043038 amino acid activation)", "go_bp", "", "QuickGO 2026-10-30; GO:0043038 obsolete, no replacement"),
 ("GO:1904292", "regulation of ERAD pathway", "go_bp", "", "QuickGO 2026-10-30; current"),
 ("GO:0042552", "myelination", "go_bp", "", "QuickGO 2026-10-30; current"),
]
# STATE:* ids are local, declared here (not external ontology terms)
for sid in sorted({r["entity"] for r in rows if r["entity"].startswith("STATE:")}):
    PROCESSES.append((sid, sid[6:].replace("_", " ").lower(), "local_state", "", "defined by the rows that use it in seeds.tsv"))

# ======================================================================================================================
def hgnc_fetch(sym):
    for url in ("https://rest.genenames.org/fetch/symbol/%s" % sym, "https://rest.genenames.org/fetch/alias_symbol/%s" % sym):
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req, timeout=20) as r:
                    docs = json.load(r)["response"]["docs"]
                break
            except Exception:
                time.sleep(1.5); docs = None
        if docs:
            d = docs[0]
            return dict(symbol=d["symbol"], hgnc_id=d["hgnc_id"], name=d["name"], status=d["status"], mgd_id=";".join(d.get("mgd_id", [])),
                        via="symbol" if "fetch/symbol" in url else "alias_symbol")
        time.sleep(0.4)
    return None

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=".", help="output folder")
    ap.add_argument("--check-hgnc", action="store_true", help="query the live HGNC REST service for every gene symbol and write hgnc_check.tsv")
    a = ap.parse_args()
    genes = sorted({r["entity"] for r in rows if r["entity_type"] in ("gene", "protein") and not r["entity"].startswith(("GO:", "SET:", "STATE:", "CHEBI:"))})
    chk_path = os.path.join(a.out, "hgnc_check.tsv")
    chk = {}
    if a.check_hgnc:
        with open(chk_path, "w", newline="") as f:
            w = csv.writer(f, delimiter="\t", lineterminator="\n")
            w.writerow(["symbol", "hgnc_id", "approved_symbol", "approved_name", "status", "matched_via", "mgd_id_ortholog_link"])
            for g in genes:
                d = hgnc_fetch(g); chk[g] = d
                w.writerow([g] + ([d["hgnc_id"], d["symbol"], d["name"], d["status"], d["via"], d["mgd_id"]] if d else ["", "", "", "NOT_FOUND", "", ""]))
    elif os.path.exists(chk_path):
        for r in csv.DictReader(open(chk_path), delimiter="\t"):
            chk[r["symbol"]] = dict(hgnc_id=r["hgnc_id"], symbol=r["approved_symbol"], status=r["status"], via=r["matched_via"]) if r["hgnc_id"] else None
    bad = [g for g in genes if chk and (not chk.get(g) or chk[g]["symbol"] != g or chk[g]["status"] != "Approved")]
    if bad: print("HGNC PROBLEM:", bad, file=sys.stderr)
    # validate and write seeds
    cols = ["seed_id", "question_id", "entity_symbol", "process_id", "entity_type", "level", "direction", "context", "usable_for_generation",
            "reserved_for_evaluation", "reason", "source_locator", "hgnc_id", "species_observed", "context_tier", "observation_class", "reason_class", "evaluation_guard"]
    out = []
    for i, r in enumerate(rows, 1):
        assert r["entity_type"] in ETYPE and r["level"] in LEVEL and r["direction"] in DIRN, r
        assert r["usable_for_generation"] in YN and r["reserved_for_evaluation"] in YN and r["reason_class"] in RC, r
        assert not (r["usable_for_generation"] == "yes" and r["reserved_for_evaluation"] == "yes"), r
        assert (RC[r["reason_class"]] == "usable") == (r["usable_for_generation"] == "yes"), r
        isgene = r["entity_type"] in ("gene", "protein") and not r["entity"].startswith(("GO:", "SET:", "STATE:", "CHEBI:"))
        sym, pid = (r["entity"], "") if isgene else ("", r["entity"])
        hid = chk[r["entity"]]["hgnc_id"] if isgene and chk.get(r["entity"]) else ""
        out.append([("S%03d" % i), r["question_id"], sym, pid, r["entity_type"], r["level"], r["direction"], r["context"], r["usable_for_generation"],
                    r["reserved_for_evaluation"], r["reason"], r["source_locator"], hid, r["species_observed"], r["context_tier"], r["observation_class"], r["reason_class"], r["evaluation_guard"]])
    for row in out:
        for c in row: assert "\t" not in c and "\n" not in c
    with open(os.path.join(a.out, "seeds.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(cols); w.writerows(out)
    with open(os.path.join(a.out, "process_ids.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["process_id", "label", "kind", "members_hgnc", "definition_source"]); w.writerows(PROCESSES)
    print("seeds:", len(out), "genes checked:", len(genes))

if __name__ == "__main__":
    main()
