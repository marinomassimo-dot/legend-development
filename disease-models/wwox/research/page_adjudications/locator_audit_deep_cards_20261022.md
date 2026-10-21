# Blind locator audit - drug-repurposing deep cards (12 packets, 5 cards, 7 abstentions)

Non-canonical adjudication record. Auditor: blind, read-only toward every canonical file. Scope:
the twelve `*.packet.json` files in `disease-models/wwox/research/drug_repurposing/cards/` (the
cards are the bridge's unedited rebuild of them), tested against the repository's own sources.
Not medical advice. No edit is proposed. No ranking is made or implied. The author's note and
the self-evaluations were not opened before the verdicts were formed.

Method. (a) Every double-quoted or single-quoted string of twelve characters or more in every
packet was extracted by script and searched, whitespace- and case-normalised, in all `.md`,
`.json`, `.jsonl` and `.txt` files under `disease-models/`, `framework/` and `governance/`
(card files excluded). (b) The claims that matter were then opened in the source: the R1, R3
notes, the known-roads note, the rescue-reference scaffold, CLAIM 011 and CLAIM 019, the
CLAIM 011 adjudication candidate, the discovery ledger, the splice, NMD and therapeutic-class
censuses, and the clinical census. (c) For the manifests the cards lean on, the sha256 of every
source artefact of PMIDs 40665325, 42422765, 22938201, 40544182 and 42875792 was recomputed
against the manifest and all matched; the Supplemental Table 3 of PMID 40665325 was re-read from
the stored docx. Not verified: the artefacts behind the other R1 readings and behind PMID
42397075 (the repository itself records the A51 panel values as no longer re-auditable); card
statements resting on those were tested against the repository's note of them, not the paper.

## 0 - What `check_cards.py` does and does not check

Run: `12 packets checked, 0 problem(s)`.

It checks: the bridge rebuilds each packet and the stored card equals the rebuild; the card is
IPOTESI and non-canonical; the twenty P4 keys are present and non-empty (UNKNOWN allowed);
status is in the four-word vocabulary; `time_to_access` and `time_to_benefit` are both present;
`label_lookup` is NOT_ATTEMPTED; an abstention names a missing datum and a search record;
`not_known` is non-empty; no dictionary key matches score, rank, probab, index or weight; no
text token matches a number-plus-unit, `mg/kg`, a q-hours schedule, an e-mail or an ellipsis; each
`FTR-` receipt id appears as a string in the ledger; non-WWOX drug assertions carry the words
NOT WWOX EVIDENCE.

It does NOT check: that any quoted passage is verbatim in a source; that a source supports the
sentence that cites it; that the packet uses the repaired wording rather than the withdrawn one;
that a negative states where it looked; that a stated absence is bounded by its scope; that
`dose-dependent`, `threshold`, `sub-proportional` or `inactive` are used within what the
repository allows; internal consistency between fields or between packets; receipt content
(string presence only); artefact digests. Every defect below passed it.

## 1 - Per-card verdict

| Card | Verdict | Named defect (packet field) |
|---|---|---|
| A01 PBA class | DEFECT | `not_known[1]` (and A02 `not_known[1]`): "six measured divergences in R1" - R1 section 5 question 2 counts 33914734 (function "not measurable") and 32023956 (an assay-reproducibility disagreement) among the six; the butyrate case is repaired to "partial dissociation, not a clean quantity-up, function-flat case". `p4_card.scope_of_checks.formal_checks`: states an R1 audit "is running in parallel; its outcome is not available" and that the R1 narrowings are "OWED" - the R1 audit has run (95 triples, 15 overshoot, 2 undershoot) and the repairs are unaudited. |
| A02 proteasome class | DEFECT | `drug_assertions[DR-A02-003]` direction NO_CHANGE / "MEASURED NO FUNCTION" and `p4_card.evidence_for_and_against.against[1]` "inactive": R1 says "no enzyme activity could be measured in this study"; inactivity is cited from earlier work, and the stabilisation was through the Hsp110 axis, not proteasome blockade. `evidence_for_and_against.for[0]` "from undetectable": the source reads "barely detectable ... about 3 percent". `indication_and_transfer` carries "normal mRNA, protein absent" without the R1 repair (the transcript level is cited from an earlier report, not established in that paper). Plus A01's two items. |
| A03 client-binding chaperone | HOLDS | none; two negatives not established (below) |
| A04 ER-proteostasis regulators | HOLDS | none; two negatives not established (below) |
| A05 HSP70 axis | DEFECT | `abstention_card.missing_datum` and `adjacent_context_not_wwox_evidence[0]`: "stabilisation gave insoluble, inactive protein" - same overshoot as DR-A02-003 (activity could not be measured). `search_record` is not a search (no query, no source, no date of a query). |
| B01 amlexanox | HOLDS (core) | Check 11 passes. Minor: `DR-B01-002` direction NO_CHANGE sits on a target list that includes full-length protein, while the source reports FANCA full-length protein significantly induced to about 9 percent (the note carries the 9 percent; the encoded direction understates it). `not_known[2]` 57 percent null/null: source not located. |
| B02 read-through class | DEFECT | `abstention_card.search_record` / `novelty_for_woree`: "ataluren, PTC124, ELX-02, read-through and nonsense suppression 0 across the repository" is false as worded: `analysis/woree_therapeutic_class_census_20260921.md` carries a READ-THROUGH class row naming "ataluren-class", and `analysis/ft116_cohort_triage_20260921.md` calls p.(Arg264Ter) "a READ-THROUGH candidate". The WWOX-literature body sweep (`wwox_nmd_assay_census_20260922.md`, agent names) does support a zero for the agent names in that corpus. |
| C01 AAV9-WWOX | DEFECT | `p4_card.evidence_for_and_against.against[1]` and `scope_of_checks.card_inferences_owed_audit`: "A THRESHOLD, NOT A CONTINUUM for survival", labelled "the repository's NARROW adjudication". The string is the pre-adjudication wording of the known-roads note (section 2.1, limit 2). The adjudication (CLAIM 011, appended block) says survival "is a step", and also that "a step and a steep continuum are indistinguishable" and the step reading is "strengthened, not established". The card contradicts itself (`p4_fields.temporal_or_model_limit` "threshold not located"; `next_measurement` "whether this is a threshold or a steep continuum"). `against[1]` "proposed": the adjudicated block is in the claim registry. |
| C02 splice ASO | DEFECT (scope) | `abstention_card.search_record`: "'antisense' and 'oligonucleotide' 0 across the whole WWOX literature in the records" - the zero in the cited census is a census-set result (19 of 20 records read at abstract depth) and the later PubMed leg is the phrase "antisense oligonucleotide OR splice-switching"; the records hold WWOX papers that use an antisense construct (PMID 19366691) or a morpholino knockdown (PMID 25649963). The ratio negative ("no aberrant-to-normal ratio exists") is supported by the later three-query leg with a passing positive control. |
| C03 CRISPRa boost | HOLDS | none; "never attempted" rests on no dedicated query (declared by the card) |
| D01 A51 | DEFECT | (i) `evidence_for_and_against.against[2]`: "pharmacokinetics sub-proportional at the top" - withdrawn as a general statement in the repaired R3; the table supports neither proportionality nor sub-proportionality (N = 1 at two levels, CV 22 to 79 percent); the "so" joining it to the grading of "dose-dependent" is a non sequitur. (ii) `scope_of_checks.support_and_replication`: the "review writes 'restored' ... primary shows partial recovery and the bracket is not drawn" is DL-MECH-086, which concerns WWOX re-expression (the primary shows up to about eleven times wild type), not A51. (iii) `evidence_for_and_against.for[0]` "normalised" for pan-neuronal marking: the ledger reads NeuN "recovered" (about 18 vs about 30 percent wild type), and not-significant-versus-wild-type is not equivalence. (iv) `mechanism` "Wnt and MYC output down" and the sources block omit the repaired R3 wording that the Myc effect is "stated, not demonstrated". (v) `formal_checks` "blind locator audit of all R3 manifests OWED": it ran on six readings (129 triples, 46 overshoot, 4 undershoot, 1 unverifiable); repairs unaudited. |
| D02 Wnt/tankyrase | DEFECT (minor) | `abstention_card.missing_datum`: "Wnt/GSK3/CK1 modulation ... Never administered in any WWOX system" - the sibling D01 card records A51, a CK1-alpha inhibitor, given to WWOX-knockout organoids. |

## 2 - Counts of quoted or source-attributed claims tested, by verdict

| Card | SUPPORTED | OVERSHOOT | UNDERSHOOT | UNVERIFIABLE | Total |
|---|---|---|---|---|---|
| A01 | 9 | 1 | 1 | 1 | 12 |
| A02 | 6 | 3 | 1 | 1 | 11 |
| A03 | 4 | 0 | 0 | 2 | 6 |
| A04 | 3 | 0 | 0 | 2 | 5 |
| A05 | 3 | 1 | 0 | 1 | 5 |
| B01 | 9 | 0 | 1 | 2 | 12 |
| B02 | 3 | 1 | 0 | 1 | 5 |
| C01 | 17 | 1 | 1 | 1 | 20 |
| C02 | 2 | 1 | 0 | 1 | 4 |
| C03 | 2 | 0 | 0 | 1 | 3 |
| D01 | 13 | 4 | 1 | 1 | 19 |
| D02 | 4 | 1 | 0 | 2 | 7 |
| All | 75 | 13 | 5 | 16 | 109 |

UNDERSHOOT here means the packet states less than the repository holds (stale status lines, or a
direction code that understates a measured rise).

## 3 - Verbatim check of quotations

About forty-six quoted strings were extracted. All appear in the repository sources except two.
`'replicated mWwox ~ hWWOX'` (C01): the repository holds `"mWwox ≈ hWWOX, replicated"` and the
Italian `«replicato mWwox≈hWWOX»`; the card's English string is a rendering inside quotation marks,
the substance (a within-study control, not a replication) is SUPPORTED. `'threshold not a
continuum'` (C01) matches the known-roads text `threshold, not a continuum` except for the comma;
the problem is attribution, not spelling (section 1). The amlexanox sentence "Thus, this study
suggests that a partial downregulation of p53 per se is not sufficient to produce phenotypic
rescue in human cells" was also matched in the stored article XML; "a multi-kinase inhibitor
(A51) established to suppress Wnt and MYC expression" is verbatim in DL-THER-089.

## 4 - The numbered checks

1. Verbatim: see section 3.
2. Source supports statement: tested; failures are in section 1.
3. Score, rank, probability, blended index, dose, route, schedule, paediatric suitability: none
   carried or implied in any packet. Vector quantities, concentrations and exposures are not
   reproduced. The `next_measurement` fields name designs (an intermediate-level arm "as a fraction
   of the primary's higher level", "dose-by-timing series") with no value. Passes.
4. Non-WWOX presented as WWOX: not found. Every adjacent source is labelled NOT WWOX EVIDENCE;
   the C01 and D01 contexts are engineered-null mouse and engineered-knockout organoid and say so.
   One transfer problem inside D01 (the DL-MECH-086 sentence, section 1) moves a finding about a
   different intervention onto A51.
5. Missing hit as proof of absence; NON_TROVATO_NELLA_RICERCA never MAI_TENTATO: the label is
   never converted to MAI_TENTATO and the dated-census caution is carried on every card. Scope
   overreach in B02 and C02 (section 1). A05, A04, D01 and C03 give no query for the
   NON_TROVATO state (C03, A01 declare that no dedicated query was run).
6. Symptomatic benefit and slowing; "protection"; quantity as function: the word "protection"
   does not appear. The fly seizure-like-episode result is labelled as such. Quantity is not taken
   as function in A01 or A02; the one slip is "inactive" (A02, A05), a unmeasured activity read
   as a measured null.
7. "Dose-dependent": not used affirmatively anywhere. D01 quotes it and narrows it; C01 states
   dose-dependence "NOT TESTED" on the one endpoint that has one dose. The CLAIM 011 limits are
   respected except for the survival "threshold" wording (C01).
8. Time to access and time to benefit: separate on all twelve cards. C01 puts the mouse recording
   window (about two weeks after birth, seven days) in `time_to_benefit` under an explicit
   "UNKNOWN in humans"; that is a measurement window, not an onset time.
9. Repaired R1 wording: no card cites the withdrawn polysome-profiling limitation or the withdrawn
   insoluble-pool statement (no packet mentions polysome or 31402619); the butyrate wording and the
   INCONCLUSIVE-for-missense restatement of the zebrafish null are the repaired ones. Repaired R3
   wording: NOT carried in D01 - "sub-proportional at the top" is the withdrawn statement and the
   "stated, not demonstrated" qualifier for the Myc effect is absent. The MYC-not-shown-suppressed
   statement for the RUNX1-mutant line is correct (figure attestation, declared as such in the
   manifest). Recomputed from the stored table: the Day 5 AUC ratio is 1.27 for a 2.0 dose ratio
   from 21 to 42 mg; the 1 to 21 mg end-point slope is above 1, so exposure is supralinear there.
10. C01 against the CLAIM 011 adjudication: "the lower level only postpones death" SUPPORTED
    (partly as: postponed from a marker centred near day 17 to near day 79, then extinct); "two
    dose points cannot locate a threshold" SUPPORTED; "no replication by an independent laboratory"
    SUPPORTED within the repository (two papers, shared senior author and institution; the card
    keeps the within-study control separate from replication); "a threshold, not a continuum"
    OVERSHOOT against the adjudication. The card does not claim more than CLAIM 011 about
    myelination, gliosis, body weight or SWD.
11. B01: the card says the reference missense has no premature stop codon, that read-through is
    "not a mechanism for it at any dose by any agent", that other actions are separate untested
    hypotheses, and `next_measurement` says "the mechanism does not apply". No exposure, agent or
    dose is implied to change that. Passes.

## 5 - Negatives that could not be established

- A03: "no WWOX-SDR ligand in the records" and "no experimental structure of the SDR domain
  exists in the repository" - the only support found is a statement inside one paper's manifest
  that every structural model there is computational; no repository-wide search is recorded.
- A04: "no measurement places the variant in ER or cytosolic quality control"; the search record
  gives no query.
- A05: the search record is the withdrawal of one candidate, not a search.
- A01, A02: "NON_TROVATO as a test in any WWOX system" rests on the known-roads table; no query
  for these molecules was run (declared by A01).
- B01: "seven registry surfaces 0 records" is true only at its 2026-10-20 date (amlexanox is now
  in the registries); PubMed zeros not re-runnable offline; the 57 percent null/null figure
  was not located in the registries, and its placement under a read-through card is a question
  because the pooled "null" class contains nonsense alleles.
- B02, C02: the PubMed zeros are not re-runnable here.
- C01: "no independent replication" holds for the two registered mouse papers; the human-organoid
  AAV9-WWOX source (not opened here) was not tested for the same claim.
- D01: "NON_TROVATO in any animal or patient WWOX system" - no query stated.
- D02: "returned 2 records, one read" - only one read could be matched.
