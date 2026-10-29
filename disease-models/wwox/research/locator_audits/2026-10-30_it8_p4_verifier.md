# IT8 P4 independent verification: marginal value of the WWOX inputs in the IT7 network comparison

Verifier (not the producer). Tree under test: branch task/it8-p4, commit e662aa9b. Method: own code written from the IT7 P3 committed inputs
(edge tables with OmniPath/CollecTRI, family list, compound-action table, results), not the producer's scripts; the producer's two scripts were
run only for a byte-identity check. Descriptive and exploratory; not medical advice.

## Verdict

PASS with defects. No blocker. The decisive numerical claims (1) to (5) reproduce; the decision "no new experiment justified" and the reading of the
IT7 wording are right. Defects: one statement about reachability that the producer's own result contradicts (medium), one unreproducible figure
(phase II, medium), a few classification reason-code mismatches and one mixed row (low), and the reopening conditions omit the one route the
diagnosis itself points to (a change of the method's input grammar).

## 1. Decisive claims, recomputed

| Claim | Recomputation | Result |
|---|---|---|
| (1) 4 of 4 HIF1A edges already present, same sign; 0 new edges, nodes, signs | own edge reader (per-row complex expansion, sign conflicts dropped), 70,461 signed edges, 8,769 genes | HIF1A to HK2, SLC2A1, LDHA: CollecTRI sign +1; HIF1A to PDK1: SIGNOR only, through the expanded ARNT_HIF1A complex, sign +1. HIF1A to all six readouts present, sign +1 (LDHB, BNIP3 and PDK1 via the SIGNOR complex row). Out-degree 306. CONFIRMED |
| Duplicate-weight mechanism (306 to 310) | IT7 builds NET-WWOX as the external list plus four more tuples, with no de-duplication, and normalises each weight by the out-degree count | the added condition is four parallel edges. CONFIRMED |
| (2) 80 of 256 families change; max 1.36e-5 (0.0097 SD); none above 1e-4 | own propagation (K=3, gamma 0.5, 256 families from the committed family table) | NET-EXT and NET-WWOX reproduce the committed scores to 4.6e-8 and 5.0e-8; 80 changed; max 1.3553e-5; 0 above 1e-4; 0.0097 SD (0.0097 with sd taken at ddof=1 or 0); 143 non-zero; Spearman of the two vectors 0.99993; rho against O_E 0.0474 and 0.0459. CONFIRMED |
| (3) WWOX a sink (7 in, 0 out); no family targets WWOX or the 7 regulators | direct count over the 256 family target sets | in-edges NFKB1, NFKB2, REL, RELA, RELB, TFAP2C (+1) and E2F1 (-1); 0 families with any of the eight as a direct target. CONFIRMED (but see defect D1 on what it implies) |
| (4) hypothetical edges | own code | one WWOX to HIF1A edge: 0 families, 0.0 change. Six WWOX to readout edges: 24 families, max 2.96e-5, delta rho +1.7e-5 (module sign) or -1.2e-3 (opposite sign, not reported by the producer). CONFIRMED |
| (4) random-edge sizing | own simulation, fresh seed, random pairs of external nodes, random signs, 20 to 40 replicates per size | 4 edges: 0 families, 0 change; 100 edges: median 14 families, median abs delta rho 0.00013 (p95 0.0058); 1,600 edges: 110 families, 0.0043 (p95 0.029); 6,400 edges: 152 families, 0.0247 (p95 0.061). The order of magnitude and the monotone shape reproduce; the producer's 100-edge (0.0003) and 6,400-edge (0.028) medians are within sampling spread, the 1,600-edge median differs by a factor 2 (0.0098 against 0.0043). Replicates are few (12 to 30) and one random stream is shared across sizes, so the three-digit medians in the README are not stable figures. QUALIFIED |
| (5) power | Fisher approximation | SE 0.0629 and MDE 0.1563 at n=256; SE 0.129 and MDE 0.321 at n=63. CONFIRMED (approximation; for Spearman the SE is slightly larger, so the MDE is if anything understated) |
| (5) signature quality | own filter from the LINCS signature metrics table (distil_cc_q75 >= 0.2, pct_self_rank_q25 in [0,5]) over the 1,239 committed signature scores | 324 of 788 (B) and 140 of 451 (E) pass; 154 families with a passing B signature, 92 with a passing E signature, 63 with both. Landmark status: BNIP3 only. CONFIRMED |
| (5) phase II: 46 of 256 families, 236 neural perturbagens | no code and no input in the commit; the GSE70138 table is not in the repository | NOT REPRODUCIBLE (D2) |
| Byte identity | classify_inputs.py re-run into a scratch file | identical to the committed TSV |

Also checked against the IT7 PRE_REGISTRATION: S3 was declared there as covering "exactly two increments" and its stated expected outcome was that the HIF1A
edges are already in the external network, so the producer's finding confirms an expectation rather than reversing one (see section 4).

## 2. Defects, severity ranked

D1 (medium). "0 of 256 families have a direct target among the 7 regulators, so a compound cannot reach a WWOX out-edge within the 3 propagation hops that matter"
is wrong as written and is contradicted by the producer's own S_B result (24 families move). Direct targeting is only the one-hop case. Counting mass at the
WWOX node by first hop, 0 families reach it at hop 1, 24 at hop 2 and 62 more at hop 3 (86 in total), because their targets act on a regulator. A WWOX
out-edge to a readout is therefore reachable for 24 families (hop 2 then readout at hop 3), which is exactly the 24 that S_B changes. S_A (WWOX to HIF1A)
changes nothing for a different reason: it needs WWOX at hop 2 and the readout one hop further, past the K=3 horizon. The sizing conclusion survives
(the effect is below 3e-5 either way) but the sentence in section 4 of the README should read: 86 families reach WWOX within three hops, 24 in a way that a WWOX to readout edge could change their score,
and the change is below 3e-5 because the mass arriving at WWOX is small.

D2 (medium). The phase II figures (236 neural perturbagens, 46 of 256 families, GSE70138) rest on a table in the session scratch area that is not committed; section 8
of the README discloses this, but no script or checksum in the folder produces them, so the figure is unverifiable by anyone but the producer. It also feeds
reopening condition 4. Either commit the extraction (script plus accession file hash) or mark the figure UNVERIFIED in the section 6 table, not only in section 8.

D3 (low-medium). The random-edge table is stated to three digits from 12 to 30 replicates on one shared random stream. My independent run gives the same shape
and order of magnitude but a different 1,600-edge median. State the medians to one digit, or with replicate count and an interval, and say that the 0.03
threshold is "reached at roughly 6,000 or more random edges" rather than "half the time at 9 percent".

D4 (low-medium). Reopening condition 2 asks for "numbers of the order of hundreds" of reachable WWOX relations. That figure comes from the random-edge simulation, which the
README itself says bounds size only. A targeted set placed on the paths that carry mass to the readouts would behave differently (the producer's S_B shows a
targeted placement moves nothing only because the mass at WWOX is tiny). State the threshold as a condition on reach and weight (relations on a path that
carries non-negligible mass from compound targets to the six readouts), not as a count.

D5 (low). Mixed row N:PDH-PYRUVATE-AXIS#1:O1 (mouse embryonic fibroblast, non-neural) is labelled ALREADY_REPRESENTED (A2). Only the HIF1A to PDK1 leg is in the
network; the WWOX to HIF1A leg is not representable, and the observation "PDK1 transcript up" in this non-neural system runs opposite to the PDK1-down readout
direction used by the module. It should be split or labelled with the sign conflict (the producer's own note carries the first half only).

D6 (low). Reason-code text does not match the row in a few places. N:WNT-BETA-CATENIN#3:O3 is a human cerebral organoid row (an early-versus-late cell contrast,
not a genotype contrast) but carries S2 "other species or non-neural context (fly, non-neural cell line, fibroblast)"; the right code is S1 (not WWOX evidence).
N:GSK3B-DEREPRESSION#2:O2 (SH-SY5Y, differentiated human neuronal-like line, tau phospho) carries S2 although it is a protein/phospho-level row (N1 by the producer's own
rule). The 11 P1 rows with direction "consistent" that are labelled S3 ("single system, n=1 or 4 v 2, discordant") are the four mouse Myelin_OL contrasts and
the seven PDK_family no_change contrasts, none of which is discordant; their real reasons are N5/seen-set. Classes are unaffected in all of them.

D7 (low). The class ALREADY_REPRESENTED for 14 P1 and 4 needs rows (code A1) is true by construction: the six-gene readout was derived from these very observations, and 11 of
the 14 P1 rows carry the flag "conflict" in the P1 table. "Already represented" here means "consumed to define the readout", not "supported". One sentence in section 3
would prevent the 25-row figure being read as 25 supported relations.

D8 (low). Cards: 16 rows are coded N2 (intervention response, firewall) although several of them state "0 endpoint outcomes" (for example the amlexanox and A01 class cards). A card with no
endpoint outcome holds no answer to protect; S4 would be the exact code. Class is unaffected only if a reader treats both as non-usable, which they are.

D9 (documentary, IT7 side, not the producer's). PRE_REGISTRATION.md names the four edges ED080 to ED083; in the committed edge table they are ED077 to ED080 (a P1 repair
renumbered them), and p3_run.py selects them by content. The producer cites ED077 to ED080 correctly; the pre-registration text should carry a one-line pointer.

## 3. Classification: independent re-derivation of 36 rows from their source locators

Sampled 22 needs rows (random seed fixed, read against the structured observed item in needs.json: statement, model type, readout level, direction), the 14 A1/A2 rows (all
P1 and needs rows with those codes, read against the edge table and system table), plus 6 P4 and 8 card rows read against their cited files. Result per class:

* ALREADY_REPRESENTED: 14 of 14 correct in class. A1 rows match the six genes and the build direction; A2 rows (ED077 to ED080) verified against the OmniPath tables above. One mixed row (D5).
* NEW_BUT_NOT_USABLE: 13 of 13 sampled correct (functional/protein/phospho/activity/clinical levels have no node type; intervention responses are the held-out truth; the IT7 self-reference rows are not WWOX observations).
* NOT_SUFFICIENTLY_SUPPORTED: 15 of 15 sampled correct in class; 3 reason-code mismatches (D6).
* Rejections of USABLE that I examined as candidates: (a) the three-line concordant MYC finding (N:MYC-PROGENITOR-PROLIFERATION#2:O2, radial-glia pseudobulk MYC up in the engineered knockout and
  two patient lines, logFC about 1.6 to 1.8) is coded N1 by the row level "protein", although its second half is a transcript-level observation in human neural cells; it is the nearest thing to a usable
  observation in the set. It is still not usable by this method: the readout is fixed at six genes, MYC is not a readout, and adding MYC as a readout would define a new outcome, not feed an existing one; the sibling row #1 is coded S3
  for composition confounding. The row should carry both reasons. (b) The seen mouse P17 contrasts are consumed by IT6. (c) The IT7 P3 P47T contrast is the held-out control. (d) No WWOX interactor that is itself a drug target appears
  in any of the 85 needs observations (searched for GSK3B, ERBB4, TP73, RUNX2, JUN, DVL, interactions), so the "validated interactor" route cannot be filled from the held record.
  I found no observation that should be USABLE.

Is "0 usable" defensible? Yes, with one framing correction: zero is a property of the method's input grammar (compound-target seeds, signed gene edges, a fixed six-gene readout, a no-answer-in-the-input firewall),
not a finding about the WWOX record. The producer says this in the last paragraph of section 7; it should be in the section 1 decision row as well.

## 4. The IT7 wording and the label "WWOX-enriched condition"

* The producer's correction "largely contains" to "contains all four" is right (4 of 4, same sign; the PDK1 edge exists only through the SIGNOR ARNT/HIF1A complex expansion, a dependency the producer lists as unaudited in section 8 and which I
  confirm: without complex expansion the HIF1A to PDK1 edge would be absent, 3 of 4).
* The IT7 pre-registration already said S3 "covers exactly two increments ... and says nothing about WWOX knowledge in general", and listed the HIF1A edges as expected to be already present. The correction is therefore a tightening of
  the README wording, not a reversal; the verdict "no added value" is unchanged and, now, uninformative.
* Implication for the label: the four edges are curated HIF1A to gene relations from non-neural and non-WWOX papers (system "background", type inferred, status single_system in the P1 table); they are not WWOX data. The label "WWOX-enriched" suggests knowledge about
  WWOX was added. What was added is a duplicate-weight perturbation of 0.006 percent of the edges. A neutral label ("NET-EXT plus 4 duplicate HIF1A edges", or "NET-HIF1A-dup") is accurate. Strings to revisit (read-only here, not edited):
  IT7 P3 README results row and its limits paragraph; the loop-demonstration README row; needs.json (three statements); cards E02 and I01 and their packets and the joined cards file; discovery ledger entry DL-MECH-174;
  therapeutic hypotheses ledger; the drug_repurposing README table row; the physician view and its shareable copies (Italian section "Prova predittiva"); the P5 comparison table; the commit candidate carrying the same sentence. Where a sentence says
  "no added value for a WWOX-enriched network" it should say "the S3 increment was four duplicate edges; no inference about WWOX knowledge".

## 5. The decision and the reopening conditions

* "No new experiment justified": agreed. The delta is below the numerical scale of the score (0.0097 SD), and the other grounds (new data, independent control, quality, pharmacology) are either absent, spent or power-costly.
* Missing from the reopening list: a change of the method itself. The diagnosis says the method "has no place to put" function, protein, activity and variant-level WWOX knowledge and that WWOX is a sink with no compound
  reaching it. A fifth condition is warranted: a re-specified method that takes WWOX-loss state as a seed or node, or a readout with a documented link to compounds beyond six transcripts, registered before any run.
  Condition 3 (larger replicated module) is the transcript-level case of this, and condition 2 should be stated by reach and weight (D4).
* Condition 4 (a pharmacological table from IT8 P3) is correctly marked UNVERIFIED; it should not be listed among reasons the present answer stands until that package is verified.
* Not required but useful: report the circular scenario S_B with both signs (the opposite sign moves delta rho by -1.2e-3, still negligible), so that no reader infers a sign dependence from the one reported.

## 6. Severity-ranked defect list (summary)

1. D1 medium: reachability sentence contradicted by S_B; 86 families reach WWOX within three hops (24 at hop 2).
2. D2 medium: phase II figures (46 of 256, 236 perturbagens) not reproducible from the commit.
3. D3 low-medium: simulation medians stated to three digits from few replicates; 1,600-edge median differs by 2x in a fresh run.
4. D4 low-medium: reopening condition 2 threshold ("hundreds") derives from random edges, not targeted ones.
5. Missing reopening condition: re-specified method (section 5).
6. D5 low: mixed MEF row labelled A2 with an unflagged sign conflict.
7. D6 low: reason-code mismatches (WNT#3, GSK3B#2, 11 consistent P1 rows).
8. D7 low: A1 means consumed, not supported.
9. D8 low: card rows coded N2 with "0 endpoint outcomes".
10. D9 documentary: pre-registration edge ids ED080 to ED083 versus ED077 to ED080.

No identifier of an individual, no contact or registration action, no spend, and no access-control bypass was involved. Scratch computations stayed outside the repository.
