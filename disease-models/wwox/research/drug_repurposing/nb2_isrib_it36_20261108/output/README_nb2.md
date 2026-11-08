# NB-2 again (IT36 P2): Tau phosphorylation and beta-catenin under different GSK3 inhibitor classes

Non-canonical research material. Not medical advice; no dose, no candidate promoted. Nothing was recorded in a ledger; receipts are staged (suffix 97).

## Answer first

* DATO: the two prime sources are still unread beyond abstracts. PMID 16014628 (the 2005 JBC study): Europe PMC lists a publisher PDF address; one request returned a Cloudflare "Just a moment" page, HTTP 403, 5,478 bytes; stopped for that source. PMID 33621689: Elsevier, no PMC copy, no open flag, no preprint (Europe PMC preprint-source title search 0 hits); the DOI page was not requested. Neither is in the held corpus (`files/fulltext`, `files/supplement` checked by PMID and DOI fragments).
* NON RISOLTO: classification (3) "none reached" therefore still holds for a Tau-versus-beta-catenin split, and it is a statement about the routes in `queries_nb2.tsv`, not about the literature. Whether 16014628 measured Tau under SB415286, and whether 33621689 measured beta-catenin under the three inhibitors, stays open.
* DATO (classification 2, partial precedent, abstract level): PMID 20362550 reports, in rat neurons treated with okadaic acid, that lithium chloride (non-ATP-competitive) and 6-BIO (ATP-competitive) both reversed the raised phosphorylation of Tau, beta-catenin and CRMP2. Two classes, both readouts, one preparation; no split. The beta-catenin readout is its phosphorylation, which does not separate total, nuclear and transcriptionally active catenin. Row N6.
* DATO (partial): PMID 11696357 (PC12): the small ATP-competitive inhibitors and FRAT1 overexpression both inhibit GSK3 activity towards Tau and beta-catenin, but only the small molecules also modulate glycogen synthase. So a substrate-selective split by inhibitory mode exists in a neuron-like line, and it is GS versus Tau/catenin, not Tau versus catenin. Abstract only. Rows N7, N8.
* DATO (full text read, a near miss): PMID 21671254 (SH-SY5Y, PMC record read through NCBI efetch) uses two classes (LiCl, the thiadiazolidinone TDZD-8) and blots both Tau and beta-catenin, but never crosses them: pT181 only under LiCl, beta-catenin only without an inhibitor, TDZD-8 only on neurite length. It is a counter row for any claim that this paper supplies a paired readout. Rows N1 to N3.
* INFERENZA: the only direction reported by any source read is that Tau and beta-catenin readouts move together under GSK3 inhibition (N4, N6, N7, N9). That is not a negative for a dissociation: the sources did not have an arm designed to produce one, and the catenin readouts are mostly phospho or total protein, not transcriptional activity.
* INFERENZA: the thiadiazolidinone class (TDZD-8) and the substrate-competitive peptide class (L803-mts) have no source with a Tau-and-catenin pair under them in the PubMed searches run (one to two hits per class-specific string; the relevant ones were read; the only TDZD-8 neuron paper found with a catenin blot is 21671254, which crosses nothing). The searched strings were narrow.
* IPOTESI: the improved discriminating design below; nothing in this session shows it would split.

## Depth and routes

Full text read: 21671254 (PMC record; abstract, Introduction, Methods, Results, Discussion, Table I, captions; figure images not looked at). Abstract only: 11696357, 11279265, 20362550, 18266928, and the carried prime sources 16014628, 33621689 (IT35 rows, not re-read). The Europe PMC fullTextXML route returned HTTP 500 for the PMC records I tried; the NCBI E-utilities efetch route returned the PMC XML (new route, worked). That route does not help where there is no PMC record.

Not reached: 16014628 (Cloudflare challenge on the publisher PDF; I did not go round it), 33621689 (no open route), 16919965 (not read: one inhibitor, Wnt perturbed by DKK1; it cannot change the answer), 15001529 (optional, publisher challenge; part B).

## Output classification

1. Precedent actually shown: none reached.
2. Partial precedent: 20362550 (two classes, both readouts, okadaic-acid rat neurons, move together; abstract); 11696357 (inhibitory mode splits GS from Tau/catenin; abstract); 11279265 (single class, move together; abstract).
3. Search perimeter for "none": PubMed tool strings QA6 to QA9 (title/abstract hits only), Europe PMC link/flag checks QA1, QA12, held-corpus check QA2; not searched: full texts of the 16 hits except 21671254, ChEMBL document-level text, preprint servers other than Europe PMC's PPR source. A real paired source with different wording can exist.
4. Improved design for `NEED-GSK3B-DEREPRESSION` / INV-09 (IPOTESI):

| Item | Proposal |
|---|---|
| Preparation | one human neuron-like culture, one lysate and one fixed coverslip set per well, so the two readouts share the culture; WWOX-deficient and corrected pair if available |
| Arms | untreated; lithium (Mg-competitive); an ATP-competitive inhibitor (two different chemotypes); a thiadiazolidinone (TDZD-8) and/or a substrate-competitive peptide (L803-mts); a Wnt ligand or a destruction-complex-independent activator as the positive control for the catenin readout; a CDK5 inhibitor (as N1 shows a lithium effect on pT181 may pass through CDK5) |
| Controls that separate GSK3 from off-target kinase action | GSK3 alpha/beta knock-down (isoform), a kinase-dead or inhibitor-resistant GSK3 rescue where feasible, a structurally related inactive analogue per chemotype, a CDK5 arm, and the okadaic-acid challenge (N6) as a stimulated context |
| Readouts per arm, same well | p-Tau at two named sites with total Tau (antibody listed, normalised per total Tau); phospho-beta-catenin (Ser33/37/Thr41 degron) and total beta-catenin by Western; nuclear versus cytosolic beta-catenin by fractionation or imaging; TCF/LEF reporter activity for the transcriptionally active pool; GSK3 Ser9 and Tyr216 |
| Time points | at least an early (hour-scale, kinase readouts) and a later (day-scale, reporter) point, because a phospho-site, a protein pool and a reporter follow different clocks (as the 1 h exposures of N1 show a short window) |
| Interpretation | a split is claimed only if two classes diverge in the same well and the divergence survives the isoform and inactive-analogue controls; the catenin pool named (total, nuclear, active) must be stated, because phospho-catenin alone cannot separate them |

Not shown by anything here: that any arm of this design would split the two readouts.

## Files

`evidence_nb2.tsv` (N1 to N10; 10 rows: 2 counter, 5 support or partial support, 3 context), `queries_nb2.tsv`, `receipts/INDEX.tsv` (the five NB-2 PMIDs 21671254, 11696357, 11279265, 20362550, 18266928 among the eleven staged receipts), `consumer_delta.md`.

## Added after the independent audit (`../verify/audit_p23.md`)
All ten rows supported (R1 to R3 against PMC full text, the rest at abstract level, the ceiling on open routes). Cautions from the audit: three of the source papers each carry a thesis that limits their use as a GSK3 readout (the LiCl effect on Abeta is reported independent of GSK3; the Tau 1 reversal is partly ERK-dependent; Ser9 phosphorylation rose under okadaic acid with GSK3 still active), so "readouts move together" is weaker than it reads.
