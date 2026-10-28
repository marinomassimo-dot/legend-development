# Independent audit of target_roles.tsv and source_artefacts.tsv, 2026-10-28

Producer: orchestrator. Verifier: independent subagent. Applied: all artefact rules; ABAT evidence text; ABAT, CACNA1G (seizure), PTC read-through and the other WWOX qualifiers; CACNA1G (seizure) and PTC read-through demoted to unresolved. NOT applied: GRIN2A/GRIN2B demotion (kept at class level, reasoning in coverage/README.md).

# Audit: coverage/target_roles.tsv (17 rows) and coverage/source_artefacts.tsv (6 rows)

Verifier: independent, read-only. Paths below are relative to disease-models/wwox/research/drug_repurposing/.
Method: needs/needs.json (intervention_direction, observed[], inferred, counter_evidence) for each need; catalog/catalog.jsonl.gz and coverage/associations.jsonl.gz read with python gzip; all counts recomputed.

Code semantics (framework/scripts/repurposing_search.py consistency()): coupling `same` + need direction down/up/restore means a drug acting "down"/"up" on the target is labelled `consistent`. Any coupling other than same/opposite gives `direction_unresolved`. No role row also gives `direction_unresolved`.

## A. target_roles.tsv

Verdict key: CONFIRMED = coupling direction supported by a measured WWOX datum or by the need's own definition; OVERCLAIMED = `same` (or the qualifier) is stronger than the evidence; UNDERCLAIMED = `unresolved` where evidence is clear; CANNOT_JUDGE = no source reachable.

| Row (need / symbol) | Verdict | Reason and anchor |
|---|---|---|
| EXCITATORY-GAIN / GRIN1 | CONFIRMED (limit stated) | GluN1 is obligatory, so any NMDAR block reduces GRIN1-containing receptors. Measured datum: needs.json EXCITATORY-GAIN O2, d-APV abolishes bursting (normalised frequency 1.0 to 0; n 5 slices, 3 animals; PMID 34634460, neuron-specific Wwox-null slices). It is a perturbation with one full competitive block, not a reversal inference; the need's own `do_not_assume` says so. Qualifier names the single d-APV block and the GRIN-series split. I recomputed 14/19 vs 3/15 against the need's O5 and the F01 card: it matches. The labels `consistent`/`opposed` on GRIN1 are corrupted by an artefact (section B), not by this row. |
| EXCITATORY-GAIN / GRIN2A | OVERCLAIMED (mild) | d-APV (competitive, glutamate site) is not subunit-resolved; no GluN2A datum exists (the qualifier admits "no subunit-level datum"). `same` makes a GluN2A-selective drug `consistent`, and that assumes the burst depends on GluN2A. The need's own target role for GRIN2A reads "human genetics: burst-suppression", and in GRIN disease loss of function is an epilepsy mechanism. Wording is honest; the coupling is stronger than the data. Suggest `unresolved` for subunit-selective action, `same` only for pan-NMDAR action. |
| EXCITATORY-GAIN / GRIN2B | OVERCLAIMED (mild) | Same as GRIN2A. |
| EXCITATORY-GAIN / GRIA1-GRIA4 (4 rows) | CONFIRMED (`unresolved` is right) | The need says "NMDAR, possibly AMPAR". O2 limits: "AMPAR contribution was not tested". O3 (sEPSC amplitude about equal, 23.3 vs 24.7 pA) gives no AMPAR gain. No UNDERCLAIMING: nothing here supports a sign. The qualifier "a guess, not measured" is accurate. |
| T-TYPE-CALCIUM / CACNA1G | CONFIRMED by definition; the need itself is only `inferred` | The need's quantity IS T-type current, so `same` is tautological. The evidence is one ethosuximide experiment (O1, PMID 32000863). Ethosuximide reduced the late-phase PTZ seizure score significantly only in the null genotype, with no drug-by-genotype test and a possible floor effect in wild type. Lithium acted in all three genotypes, and the T-type action of ethosuximide rests on the paper's Methods wording only. The qualifier states most of this. It does not mention the floor effect or that the T-type mechanism was not measured in Wwox tissue. |
| T-TYPE-CALCIUM / CACNA1H | CONFIRMED only at class level | No isoform datum. The qualifier says so for H and I. An isoform-selective drug would be labelled `consistent` with nothing behind it. |
| T-TYPE-CALCIUM / CACNA1I | CONFIRMED only at class level | As CACNA1H. |
| SEIZURE-CONTROL / CACNA1G | OVERCLAIMED | The seizure need's own sources (cards EB-KD-01, EB-VGB-01, EB-CBD-AX-01, EB-HORM-AX-01, EB-DEV-AX-01; PMIDs 36537114, 30361190) contain no T-type datum. The coupling is borrowed from the T-type need, which is one mouse ethosuximide experiment in provoked (PTZ) seizure. The seizure need's `intervention_direction.do_not_assume` says the direction "is the clinical aim and is not derived from a pathway". CACNA1H/I are absent from this need, so CACNA1G alone is an arbitrary subset of the T-type class. 22 records are `consistent` (associations.jsonl.gz: CACNA1G / SEIZURE-CONTROL). The qualifier "symptom-level inference, not mechanism-linked to WWOX" is true but does not say there is no T-type datum in this need or that the only datum is a single provoked-seizure ethosuximide result. |
| SEIZURE-CONTROL / ABAT | OVERCLAIMED (qualifier) | Direction rests on the vigabatrin class pharmacology plus WWOX case reports (O2), which are mixed. Spasms resolved in 1 of 2 null children; the second had a partial response; one child had visible-seizure reduction with electrical attacks still on video-EEG; one null/null child had it ineffective; one case was vigabatrin-resistant. A brain-MRI abnormality (VABAM) signal is recorded in two cases. All are n of 1-2, with queried-not-read depth. The qualifier mentions none of this. Coupling `same` is defensible as a mechanism hypothesis, not as support. Only vigabatrin is `consistent` (2 association rows: ChEMBL INHIBITOR and DGIdb-ChEMBL inhibitor). |
| WWOX-GENE-ADDITION / WWOX | CONFIRMED (qualifier too thin) | Measured: O1/O2, neuron-promoter AAV9-WWOX in Wwox-null mouse (PMID 42422765) gives survival plateau about 76-77% and spike-wave discharges 0.635 to 0.13 per hour at high dose; the low dose fails. More WWOX gives a better phenotype in this model. Qualifier "none beyond the need's own text" hides the need's main caveat: "no ceiling is measured", organoids went beyond wild type, applied recombinant WWOX lowered viability of human neurons (preprint), and the efficacious window is perinatal. |
| WWOX-SPLICE-CORRECTION / WWOX | OVERCLAIMED (qualifier) | The need's quantity is an aberrant-to-normal transcript RATIO, not WWOX level. Certainty is "inferred (conditional on the unresolved cryptic-site outcome)", and the only datum for the reference allele is COMPUTATIONAL_RESULT (SpliceAI DS_AL 0.96; the +8 cryptic acceptor could give an in-frame 6 nt deletion, which is hypomorphic). Qualifier "none" is wrong. |
| WWOX-PTC-READTHROUGH / WWOX | OVERCLAIMED | The need's only scope is UNVERIFIED_HYPOTHESIS ("no read-through experiment on WWOX was found"); certainty "unknown". needs.json reading_rules say such a need "is a question, not an established need". Role says `same` with "none beyond the need's own text". |
| WWOX-MISSENSE-PROTEIN-RESCUE / WWOX | OVERCLAIMED | The need's quantity is FUNCTIONAL mutant protein "not merely detectable". Inferred item: "raising abundance raises function" is not known (CLAIM 030, "stable but inert" exists). Certainty `inferred`, direction conditional on an unresolved bottleneck. Qualifier "none" omits all of it. |
| WWOX-ENDOGENOUS-BOOST / WWOX | OVERCLAIMED | Certainty `context_dependent`. The need says "neither too little nor too much", WWOX is pro-apoptotic in some contexts, and a non-allele-specific boost may push splice-allele transcript toward NMD (inferred, map N-05). The only benefit datum is a Drosophila amyloid CRISPRa result (WWOX_BIOLOGY_OTHER_CONTEXT). Qualifier "none" is wrong. |

Note on the 5 WWOX rows: every WWOX association in associations.jsonl.gz is `direction_unresolved` or a placeholder (3 + 1 per need), so none of these rows changes a label today. The risk is future-facing: any later catalogue action on WWOX would become `consistent`.

Absent role rows (checked): NEED-MYELINATION is direction `restore` and has an intervention target CHRM1, with no role row. Its 212 associations are all `direction_unresolved` ("no explicit role row"). That is conservative and correct. NEED-MISSENSE pathway members (HSPA8 etc.) are not evaluable by design. No UNDERCLAIMED row found.

## B. source_artefacts.tsv

Recomputed from catalog.jsonl.gz (44,211 records; 24,423 carry a target block).

1. Pattern and count: CONFIRMED. 89 records link to ABAT (88 via DGIdb `gene` plus 1 via ChEMBL curated mechanism). 77 have ABAT only from claim_source GuideToPharmacology (matches "77 of 89", and the 78 `source_artefact` rows in associations.jsonl.gz come from those 77 plus the explicit rule). All 77 are adenosine-receptor ligands (adenosine, caffeine, istradefylline, CPT, capadenoson, neladenoson, MRS7469, LUF5831 ...).
   - Imprecision: the evidence text says these rows "carry the gene list ABAT, ABCA1, ABCA2, ABCA3". Only 45 of 77 carry all of ABAT+ABCA1+ABCA2+ABCA3. 63 carry at least one of ABCA1-3; 14 carry ABAT alone (e.g. capadenoson, neladenoson, LUF5831); 22 carry fewer than 3 early symbols, which the evidence acknowledges (55 flagged + 22 = 77). A more accurate description: ABAT/ABCA1/2/3 look like A1/A2/A3 adenosine-subtype tokens expanded to symbol-prefix matches.
   - "The genuine ones have a ChEMBL or other-source ABAT row" is overbroad. The 12 non-GtoP-only ABAT records are: vigabatrin (ChEMBL+TEND+TTD+TdgClinicalTrial), valproic acid, divalproex, DP-VPA, CPP-115, tiagabine, pyridoxal phosphate, alanine, pyruvic acid, 4-hydroxybenzaldehyde, and the placeholder "Null". Alanine, pyruvic acid, 4-hydroxybenzaldehyde and PLP are substrates or cofactors, and tiagabine is a GAT-1 (SLC6A1) inhibitor whose ABAT row (TEND, TdgClinicalTrial, no interaction type) is doubtful. Only vigabatrin is `consistent`, so there is no label damage. Reword to "have a second source" rather than "genuine".

2. ABCA1/2/3 rows: CONFIRMED as "not a gene of any need".

3. PDK1 alias_risk: not re-audited in depth. In the catalogue PDK1 has 7 DGIdb records and none are GtoP-only, which is consistent.

4. The generic detector is too narrow: CONFIRMED to catch only ABAT among need genes (55 flagged). My recount of the early set (top 8% of distinct DGIdb gene symbols = 401 symbols, to ARSD) agrees. It misses a second artefact class: Guide-to-Pharmacology rows whose single gene (or whose whole record) is pharmacologically implausible, on need genes that are NOT in the early 8% and sit on records with fewer than 3 early symbols. Counts below are GtoP-only records (no second source on that gene), from the catalogue; names inspected by me.

| Need symbol (kind) | GtoP-only / all DGIdb records | What they are | In counts? |
|---|---|---|---|
| GRIN1 (intervention_target, role `same`) | 10 / 48 | all STING agonists or the STING inhibitor H-151 (ADU-S100, 2'3'-cGAMP, diABZI-4, SNX281, ulevostinag, ...). No NMDAR pharmacology. | Counted. 9 labelled `opposed`, H-151 `consistent`. H-151 gets priority `consistent_mechanism_candidate` for NEED-EXCITATORY-GAIN (FAM:CAT:DGIDB:828b6a80dfbe). 9 of the 15 GRIN1 `opposed` rows are these artefacts. |
| GRIA1 (intervention_target) | 2 / 31 | L6H21, Neoceptin-3 (not AMPAR ligands) | Counted, unresolved |
| GRIA2 | 2 / 33 | telaglenastat, IPN60090 (glutaminase inhibitors) | Counted, unresolved |
| GRIA4 | 3 / 22 | BAY-069 (+HOXB@), compounds 27 and 42 [PMID 26938474] (probable, not checked at source) | Counted, unresolved |
| GRIN2A / GRIN2B | about 35 / 37 GtoP-only, almost all genuine NMDAR ligands; implausible ones: zolbetuximab (anti-CLDN18.2 antibody) on GRIN2A; semapimod, GRP94 inhibitor 54 on GRIN2B (probable) | | Counted. These rows also carry spurious companion genes ASS1P10/ASS1P14 (not need genes). |
| ATF4 (pathway_member, ISR) | 28 / 29 | all nicotinic-receptor ligands (PNU-282987, bungarotoxin, mecamylamine, epibatidine, encenicline ...) | Counted in "incl. pathway members", unresolved |
| CTNNB1 (pathway_member, Wnt) | 30 / 67 | all p38 MAPK inhibitors (SB202190, SB203580, losmapimod, doramapimod ...) | Counted apart, unresolved |
| EIF4EBP1 (readout_marker, mTOR) | 21 / 22 | CDK4/6 and other CDK inhibitors (palbociclib, abemaciclib ...) | Not a link (readout), but listed |
| EIF2S1 (pathway_member) | 2 / 3 | SY-5609 (CDK7), CDK12 inhibitor 2 (contiguous EIF run) | Counted apart |
| GSK3B (intervention_target, uncertain) | 1 / 46 | relatlimab (anti-LAG3 antibody) | Counted |
| ATP5F1A (readout) / COX4I1 (readout) | 5 / 5 ; 1 / 1 | Ca2+, Mg2+, H+, 2-APB, ruthenium red ; compound 9 [PMID 11606127] | Not links |
| CACNA1H, GRIA3, PDK2-4, GAD2 | 8, 20, 2+1+1, 1 GtoP-only | genuine target ligands (Z944, ML218, TTA-A2, ACT-709478, AMPAR modulators, AZD7545, S-allylglycine). Companion spurious genes only (ATP6AP1, GRM5, CNTN1). | Fine |
| CACNA1G, CACNA1I, GABRB2/3 | 0 GtoP-only | none | |

   Totals for need-gene artefacts I judge implausible: GRIN1 10, ATF4 28, CTNNB1 30, EIF4EBP1 21, EIF2S1 2, GRIA1 2, GRIA2 2, GRIA4 3, GSK3B 1 (about 99 gene-record pairs, plus 3 probable on GRIN2A/B). The strongest harm is GRIN1: they produce `opposed`/`consistent` labels on an intervention target with a role row. None is a pure alphabetical-prefix pattern in the sense of the detector; they look like short-name/alias token collisions (STING, p38, alpha-7 nAChR, CDK4/6) in the same upstream source.

## C. Proposed edits

target_roles.tsv
1. EXCITATORY-GAIN / GRIN2A and GRIN2B: coupling -> `unresolved` for subunit-selective action, or keep `same` and append to qualifier: "pan-NMDAR block only (d-APV is not GluN2-selective); no GluN2A or GluN2B datum; GRIN2A loss of function is itself an epilepsy mechanism". Prefer `unresolved`.
2. SEIZURE-CONTROL / CACNA1G: coupling -> `unresolved`, or qualifier -> "borrowed from NEED-T-TYPE-CALCIUM (one ethosuximide PTZ experiment, PMID 32000863); no T-type datum in this need's sources; CACNA1H/I not listed here".
3. SEIZURE-CONTROL / ABAT: qualifier -> "symptom-level; WWOX vigabatrin reports are mixed (resolved 1, partial 1, ineffective 1-2, resistant 1; VABAM signal in 2), n of 1-2, queried-not-read; mechanism not tied to WWOX".
4. WWOX-GENE-ADDITION: qualifier -> "measured: high-dose AAV9-WWOX rescue in Wwox-null mouse (PMID 42422765); no ceiling measured; overshoot beyond wild type in organoids; recombinant WWOX reduced neuron viability (preprint); perinatal window".
5. WWOX-SPLICE-CORRECTION: qualifier -> "quantity is the aberrant-to-normal transcript ratio; null-like status of the reference allele is predicted only (SpliceAI), cryptic +8 acceptor may be in frame".
6. WWOX-PTC-READTHROUGH: coupling -> `unresolved`; qualifier -> "UNVERIFIED_HYPOTHESIS: no WWOX read-through or NMD measurement".
7. WWOX-MISSENSE-PROTEIN-RESCUE: qualifier -> "raising abundance is not raising function (CLAIM 030); bottleneck unresolved; need certainty inferred".
8. WWOX-ENDOGENOUS-BOOST: qualifier -> "context_dependent: neither too little nor too much; pro-apoptotic in some contexts; only benefit datum is Drosophila amyloid".
9. T-type rows (CACNA1G/H/I): append "ethosuximide T-type action rests on Methods wording only; possible floor effect in wild type".

source_artefacts.tsv
10. ABAT evidence text: replace "carry the gene list ABAT, ABCA1, ABCA2, ABCA3" with "carry ABAT with ABCA1-3 on 63 of 77 (45 with all three; 14 carry ABAT alone)"; replace "the genuine ones (...) have a ChEMBL or other-source ABAT row" with "12 records have a second source, of which only vigabatrin is a documented ABAT inhibitor; valproate is weakly supported; tiagabine, alanine, pyruvate, 4-hydroxybenzaldehyde, PLP and 'Null' are not ABAT inhibitors".
11. Add rows (rule `require_second_source`, claim_source GuideToPharmacology) for GRIN1, GRIA1, GRIA2, GRIA4, GSK3B (symbol-level), and ATF4, CTNNB1, EIF4EBP1, EIF2S1 (pathway/readout kinds, so no headline change). GRIN1 and GRIA* need a caution: GRIN2A/2B must NOT get a blanket rule (their GtoP rows are genuine NMDAR ligands). For GRIN1 a blanket `require_second_source` is safe only if its genuine GtoP-only NMDAR ligands are listed by second source; in my check all 10 GtoP-only GRIN1 rows are the STING set, so a blanket rule on GRIN1 loses nothing.
12. Add a second generic detector, not alphabet-based: GtoP-only rows on an intervention_target whose record has no ChEMBL or other-source link and whose compound class does not match the need's pharmacology (needs human curation); until then, run the symbol rules in 11.
13. Re-run `python3 -B framework/scripts/repurposing_coverage.py run`, then `check`, and regenerate the view. Expected effect: H-151 loses its `consistent_mechanism_candidate` priority; the 9 STING `opposed` rows and 1 `consistent` row move to `not_evaluable` (source_artefact). Not run by me (read-only audit).
