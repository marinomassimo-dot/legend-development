# ISRIB: identity, target and discriminating use (IT36 P3)

Non-canonical research material. Not medical advice; no administered dose, schedule or route; no efficacy claim; ISRIB is a research probe here, not a candidate. Nothing was recorded in a ledger; receipts are staged (suffix 97). Tables: `probe_entry.tsv` (16 rows in the four layers `identity`, `mechanism`, `function`, `wwox_transfer`), `evidence_isrib.tsv` (33 rows: 16 support, 11 counter, 6 context), `queries_isrib.tsv`.

## Answer first

* DATO (identity): the first report (PMID 23741617, text read) describes ISRIB as a symmetric bis-glycolamide with a central cyclohexane in cis and trans forms, gives the trans isomer the descriptors (1r,4r) in its synthesis section, and finds trans about 100-fold more potent in the cell reporter. This matches the registry title (trans-1,4-cyclohexanediyl bis-amide) on the branch `task/isrib-identity`, which I reuse as given. INFERENZA: the paper's text is not an independent derivation of the registry copies in any demonstrable sense (a registry may have taken its structure from this literature); it is a primary source for the structure, not a second check on the InChIKey. The drawn structure (Figure 2A) was not looked at. One flag: the 2018 structure paper (29599213) says the modelled side chains project "to the same face" of the cyclohexane ring; without its figure this cannot be read as cis or trans, so it is neither a contradiction nor a confirmation (row EI19).
* DATO (target and site): ISRIB binds eIF2B at the interface of the beta and delta regulatory subunits (PMID 29599245, 4.1 angstrom, endogenous human complex) and bridges the two tetramers across the central symmetry interface of the decamer (PMID 29599213, 2.8 angstrom). The catalytic HEAT domain of the epsilon subunit is unresolved in both structures. These support binding to the eIF2B complex. They do not support binding to, or acting through, the single subunit EIF2B5.
* DATO (nature of the action): an eIF2B activator that stabilises the assembled complex and offsets the brake of phosphorylated eIF2; it does not stop eIF2 alpha being phosphorylated (rows EI04, EI27) and does not repair an mTOR-type translation block (EI05). Its effect shrinks as phosphorylated eIF2 approaches the amount of substrate (hardly any stimulation at a 1:1 mix in vitro, EI10), and a cited finding gives a threshold of phospho-eIF2 alpha above which it fails (EI24; the cited paper was not read).
* DATO (what the drug does with the ISR off): the sources disagree on the basal exchange effect. A partially purified rabbit eIF2B extract gave a three-fold rise without phosphorylated eIF2 (EI11); the recombinant decamer showed no significant activation (EI15) and the module's earlier row E21 says only minimal acceleration. In animals, the authors of 33531382 report no noticeable effect in wild-type mice (EI26). Reversibility after withdrawal was not found in the passages read: NON RISOLTO.
* DATO (dose-response, source facts only): bell-shaped in the tetramer system in vitro (assembly at 1 micromolar, none at 10 micromolar, EI17); neuronal survival rose over a wide range in 32457286 (EI21). Not a rule for any other system.
* DATO (function in neural systems): in primary rat cortical neurons with mutant SOD1, ISRIB raised survival and lowered a UPR reporter (readouts: longitudinal survival, UPR reporter), but in the same neurons it did not lower ATF4 under thapsigargin, unlike HEK293 (EI21, EI22), and it did not help neurons with the other toxic protein tested (EI23). In AD-model mouse hippocampus it corrected the oligomer-driven fall in protein synthesis (readout SUnSET, EI25). INFERENZA: ATF4 is not a safe engagement readout in cultured neurons; global translation labelling is.
* DATO (WWOX): no source tests ISRIB, GSK3 or eIF2B in a WWOX system; the module's own summary is "The chain is not established." (EI32). IPOTESI only below.

## The four links, kept separate

| Link | Supported by | Not supported by |
|---|---|---|
| Binding to the eIF2B complex (beta-delta interface, decamer stabilisation) | 25875391 (activation, assembly), 29599245, 29599213 | nothing here argues against it |
| Action on the single subunit EIF2B5 (epsilon) | 25875391 shows eIF2B5 knock-down lowers the response (an abundance requirement) | all binding data: pocket on beta and delta; epsilon catalytic domain unresolved (EI14, EI18) |
| Effect on the phosphorylation state of the GSK3 serine of epsilon (rat Ser535, human Ser540) | one measurement: 23741617 states that ISRIB 'did not reduce phosphorylation of S539' of epsilon (HEK293T, ER stress; direction only, figure not viewed); whether S539 is the GSK3 serine (rat 535, human 540) is open | everything read; the module's audit |
| Functional rescue in a WWOX system | nothing | no WWOX measurement found (module Q03, Q-E1, Q-E3, Q-E4) |

## Probe use: which ISRIB result would discriminate (IPOTESI; no source tests this)

Same preparation (isogenic WWOX-deficient and corrected human neurons, or the closest available), arms run side by side: untreated; ISRIB (a concentration series, not one concentration); a positive-stress arm in the same plate (an ISR inducer) as the engagement control; a GSK3 inhibitor of one class and one of another (module H1); rapamycin or an mTOR inhibitor as the ISRIB-specificity control (EI05). Readouts in the same wells: phospho-eIF2 alpha (Ser51) and total, ATF4 only as a secondary readout, phospho-epsilon at the GSK3 serine and at the priming serine with total epsilon, global translation (puromycin labelling), and an eIF2B assembly readout (sedimentation shift, EI08, EI16) as direct engagement.

| Observation | Reading |
|---|---|
| Phospho-eIF2 alpha and the ISR markers are raised at baseline; ISRIB restores translation; engagement control works | phospho-eIF2-driven ISR in that preparation; says nothing on GSK3 |
| Phospho-eIF2 alpha not raised, phospho-epsilon at the GSK3 serine raised, translation lowered; a GSK3 inhibitor of two classes raises translation; ISRIB gives little although the engagement control shows it works | the GSK3 to eIF2B-epsilon route is the better reading; this is the only pattern ISRIB discriminates cleanly |
| Phospho-eIF2 alpha not raised, translation lowered, ISRIB raises translation | not discriminating: ISRIB may raise eIF2B activity generally (EI11) or compensate a destabilised complex (EI29); it does not exclude the GSK3 route |
| Phospho-eIF2 alpha not raised, translation not lowered | no eIF2B-limited defect in this preparation; the premise fails |
| ISRIB gives nothing and the engagement control also fails | uninformative (dose, bell-shaped response, resistance) |

ISRIB is uninformative or confounding when: the ISR is off and nothing needs offsetting (EI26); ATF4 is the only readout in rat cortical cultures under thapsigargin (EI22); a rescue appears with phospho-eIF2 alpha not raised (above); the translation lesion is mTOR-type (EI05); a single concentration sits where the in-vitro effect fades (EI17); the GSK3 inhibitors also change protein synthesis by routes other than epsilon (12133000, EI30; module row E07); the preparation is at a stage where the GSK3 brake is weak (module E18: phospho-Ser535 higher in adult than developing retina).

## Optional sources

12133000: a second route (NCBI efetch of the PMC record) returned the abstract and no body; the Europe PMC pdf render and 15001529's publisher PDF both returned Cloudflare challenge pages (403, 5,498 and 5,589 bytes); stopped for those routes. The depth for the GSK3 to eIF2B link therefore stays abstract only (EI30: the three inhibitors dephosphorylated the serine without significant eIF2B activation). 15001529: not reached.

## Depth and what was not reached

Text read in part (PMC records through NCBI efetch; Methods and figure images mostly not read): 23741617, 25875391, 29599245, 29599213, 32457286, 33531382. Carried unread-again: 33220178, 29489452 (module rows E20 to E26). Not read: the cited Rabouw paper, the 2026 allostery paper (reference only, abstract), figures, supplements, the ISRIB-engagement results in the GSK3 setting, any antibody-level detail. The cryo-EM structures are two datasets of the same complex; author overlap was not checked, so I do not count them as independent teams.

## Added after the independent audit (`../verify/audit_p23.md`: 10 NB-2 rows supported; ISRIB rows 32 supported, 1 undershoot; probe entry 11 supported, 4 overshoot, 1 undershoot; units U1 to U6 supported)
- Corrected at the modified point (the Discussion sentence on S539 was re-found by the Orchestrator in the PMC text): a phospho-epsilon measurement under ISRIB exists in the 2013 paper (not reduced; direction only), numbering relative to the GSK3 serine unresolved. 'Leaves phospho-eIF2 alpha unchanged' becomes 'does not reduce it' (it rose further under tunicamycin at 120 min). Basal-condition effects are disputed inside the cited set. The ATF4 non-response holds for rat cortical cultures under thapsigargin only. The 'dephosphorylation did not activate eIF2B' wording of 12133000 is restored. The library sample was likely a cis/trans mixture; 'same face' of the ring reads as cis by convention and stays unresolved without the figure.
- NB-2 papers R4 to R6 each carry a thesis limiting their use as a GSK3 readout (LiCl effect on Abeta independent of GSK3; Tau 1 reversal partly ERK-dependent; Ser9 raised under okadaic acid with GSK3 still active). Abstract level only for all but R1 to R3.
