# COMMIT CANDIDATE — CC-20261003-B-CASCADE-INDEPENDENCE-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 2 2026-10-03, branch `task/sci-B-20261003`.
**context_policy:** `SOURCE_FIRST` for all six readings; LEGEND's own records were opened only after each first pass was written (see `research/intake_wave_20261003_B.md`).
**Not medical advice.** Class-level statements about published models and genotypes only.

## Target
- `claim_registry_current.md`: **create** `CLAIM 043`, inserted after `CLAIM 042`.

**Number is provisional.** `CLAIM 043` is the next free number measured by `registry_records.py catalog` on `main` f5f9468 (max is `CLAIM 042`). A peer of this wave may claim it; the integrator renumbers in event order and updates the wikilinks in `CC-20261003-B-WWOX-DIRECTION-01` and in the six `PAPER` records of `CC-20261003-B-REGISTRY-01`.

## Change class
**MINOR** (§ 7). A new claim at `in observation`; it narrows no `consolidated baseline` record and touches no working-model block. It does, however, state a bound that every future tau- or amyloid-directed rationale inherits, so it is written to be falsifiable rather than decorative.

## Ordering
Apply **before** `CC-20261003-B-WWOX-DIRECTION-01` (that candidate's `CLAIM 044` anchors on `CLAIM 043`) and **before** `CC-20261003-B-REGISTRY-01`, whose `PAPER` records link to `043`. The six receipts `FTR-20261003-<pmid>-0N` must be appended first, so that no record declares a reading without a persisted receipt.

## Why this record exists
The six sources of group B are a single laboratory's account of a single mechanism. The question this wave was given was which link of that mechanism is a direct neuronal measurement. The answer is: none. That is a fact about the evidence, not about the biology, and it has to live somewhere a future reader will meet it before building on the cascade — otherwise the next session will carry the cascade forward as if it were a measured chain.

## Dependencies on reagents, stated once
Every claim in the chain depends on two homemade rabbit antisera validated by peptide blocking alone. The record names the one-blot experiment that would ground or dissolve the chain, because naming a cheap discriminating experiment is more useful than listing caveats.

## Op list — `claim_registry_current.md` (record-scoped; dry run 2026-10-02 against `main` f5f9468: exit 0, 1 op, key `['CLAIM 042']`, `inserted_bytes` 4735, `replaced_bytes` 0, scope proof *bytes outside each edited range identical; every other block identical; record set as declared*)

```json
[
 {
  "op": "insert-after",
  "id": "CLAIM 042",
  "text": "\n## CLAIM 043\n**Title:** The WWOX → TRAPPC6AΔ/TIAF1 → caspase → tau/Aβ cascade has no link measured in a neuron carrying a WWOX genotype, and no link measured outside one laboratory\n**Status:** in observation\n**Type:** DATO (what each cited link measures, read at source) + PREMISE (the independence counts)\n**Pathway:** P4 — proteostasis / aggregation cascade\n**Genotype/model relevance:** none of the sources carries a human WWOX allele; the in-vivo genotype is a constitutive mouse null that dies at about a month, and one heterozygote cohort\n**Transferability:** T3 for every link\n**clinical relevance:** HIGH — this cascade is the mechanistic bridge by which a tau/amyloid therapeutic rationale would reach a WWOX genotype class, so the class of evidence under it decides what may be built on it\n**Summary:** Read at source on 2026-10-03 (intake wave 2, Scientist B), the eight links of the proposed chain carry these evidence classes. **L1 WWOX binds TPC6A** — one endogenous reciprocal co-IP in **HEK293**; all other binding is FRET between over-expressed fusions in COS7. **L2 WWOX loss → TPC6AΔ aggregation** — siRNA in **COS7** and shuttling kinetics in `Wwox−/−` **MEF**, i.e. fibroblasts. **L3 ordering of TPC6AΔ before TIAF1** — co-localisation plus antibody-FRET in `Wwox−/−` cortex, in a figure whose only control is the same knockout tissue with the antibodies peptide-blocked. **L4 aggregation → caspase 3** and **L8 → cell death** — transient over-expression in the neuroblastoma line SK-N-SH, in which **wild-type TPC6A is equally potent as the Δ isoform**, so the assay does not establish the isoform specificity it is cited for. **L5 caspase → APP → Aβ** — an immunostaining ratio in the same over-expressing line; the Thr688 step is asserted in reviews and measured in none of the six sources. **L6 WWOX loss → tau** — pT181-tau **aggregate counts on brain sections** (n = 5, p = 0.0176), not tau biochemistry, and with the heterozygote mean **below** wild type. **L7 WWOX binds tau via the SDR domain and restrains GSK-3β/ERK/JNK** — **not measured in any of these sources**: the direct-binding phrasing occurs only in the abstract of the group's own review, whose body states the GSK-3β version and cites two same-laboratory primaries. **Independence, counted on PubMed 2026-10-02:** `WWOX AND TIAF1` returns 9 records and `WWOX AND TIAF1 NOT Chang NS[au]` returns **0**; `\"TRAPPC6A\" AND (aggregation OR plaque)` returns **4**, all four from this laboratory; `Zfra` returns 17 and the single non-Chang hit is an unrelated zebrafish androgen-receptor paper matching the string by accident. Self-citation in the sources' own bibliographies: 54%, 41%, 48%, 52%, 47% and 21%.\n**Clinical meaning:** The cascade may be real. What this record fixes is that **nothing in it has been measured in a neuron with a WWOX genotype, and nothing in it has been measured twice by independent hands.** Any therapeutic rationale that reaches a WWOX genotype class through tau or amyloid therefore inherits a single-laboratory, single-reagent dependency, and must say so. Not medical advice.\n**Source:** [[paper_registry_current#PAPER 119]] (ordering, PMID 27551439) · [[paper_registry_current#PAPER 120]] (first node and the tau datum, PMID 25650666) · [[paper_registry_current#PAPER 121]] (MPP+ arm and heterozygote, PMID 36498839) · [[paper_registry_current#PAPER 122]] (intervention, PMID 29067327) · [[paper_registry_current#PAPER 124]] (review, provenance of L7, PMID 34359949)\n**Wikilinks:** [[paper_registry_current#PAPER 119]] · [[paper_registry_current#PAPER 120]] · [[paper_registry_current#PAPER 121]] · [[paper_registry_current#PAPER 122]] · [[paper_registry_current#PAPER 124]] · [[claim_registry_current#CLAIM 032]] · [[claim_registry_current#CLAIM 044]]\n**Impact on Working Model:** none to BLOCCO 1. It bounds the evidence class under any tau- or amyloid-directed rationale and makes the single-reagent dependency explicit.\n🔴 **The cheapest discriminating experiment is a reagent control, not another mouse.** Every claim of the cascade depends on two homemade rabbit antisera — anti-TPC6AΔ (peptide 24–38) and anti-pS35-TPC6AΔ — validated by **peptide blocking only**, in every paper of the group. Running them against `TRAPPC6A`-knockout lysate would either ground or dissolve the whole chain in one blot.\n🔴 **`REVIVAL_TRIGGER`:** any of — (a) TPC6AΔ aggregation measured in WWOX-deficient **neurons** (iPSC-derived or primary) by a laboratory other than the originating one; (b) a genetic-null validation of either antiserum; (c) an isoform-resolved human measurement; (d) a WWOX–tau interaction measured outside this laboratory.\n"
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT

(Transient over-expression is the cell-death assay, and it does not discriminate the isoform | `Transiently overexpressed TPC6A and TPC6A` | PMID 27551439, Results, 'Transiently overexpressed TPC6AΔ induces apoptosis and counteracts the function of WWOX in activating promoter governed by NF-κB')

(The one endogenous WWOX/TPC6A interaction is in an embryonic kidney fibroblast line | `Embryonic kidney fibroblast HEK293 cells` | PMID 27551439, Results, 'TPC6A physically binds to the C-terminal D3 tail of WWOX')

(The human aggregation comparison for this protein is null | `No significant difference was shown in TPC6A or TIAF1 aggregation` | PMID 25650666, Figure 3 legend / Results, 'Aggregation of TPC6A and TIAF1 in nondemented human hippocampi')

(The human measurement cannot resolve the isoforms | `Western blotting was then carried out using specific antibodies for TPC6A (pan-specific)` | PMID 25650666, Figure 3 legend, panel A)

(Antibody validation is peptide blocking only | `Specificity of the antisera was tested using the synthetic peptides to block immunostaining` | PMID 25650666, Methods, 'Antibodies and antibody production in rabbits')

(The tau datum is an aggregate count on brain hemisphere sections | `pT181-Tau aggregates were significantly increased in the brain hemisphere sections` | PMID 25650666, Results, 'Wwox gene ablation induces TPC6AΔ and tau aggregation in the brain of 3-week-old knockout mice')

(The in-vivo model's survival caps any latency statement made from it | `The mice can only survive for about a month` | PMID 25650666, Results, same section)

(The SDR-domain mechanism as the body of the review states it, attributed to two same-laboratory primaries | `SDR domain binds and blocks GSK-3β-mediated tau hyperphosphorylation and thereby promotes neuronal differentiation` | PMID 34359949, Section 6.1, 'WWOX-Interacting Partners for AD')

(The developmental-timing statement | `it only takes less than 15 days after birth to let the brain proteins polymerize and aggregate in a cascade-like manner` | PMID 34359949, Section 7.2)

(Two load-bearing mechanistic steps are unpublished data of the same laboratory | `, unpublished). By filter retardation assay` | PMID 27551439, Discussion, paragraph on TGF-β/Hyal-2/WWOX/Smad4 signalling)

(Figure attestation: the in-vivo figure's control is the same knockout tissue with the antibodies blocked | `[figure attestation - pixels cannot be quote-matched] Fig 7a 'Wwox-/- brain cortex' FRETc = 75+/-9; Fig 7b same tissue, 'Antibodies blocked with peptides', FRETc = 5+/-3; Fig 7c pS35-TPC6A/TIAF1 FRETc = 105+/-7; Fig 7d 'Wwox-/- mouse brain' p-TPC6A at 40x/100x/400x over 'p-TPC6A (peptide blocking)'. No Wwox+/+ panel appears anywhere in the figure.` | PMID 27551439, Figure 7, `files/figures/PMID27551439/native/cddiscovery20153-f7.jpg`)

(Figure attestation: the human null is not an assay failure | `[figure attestation - pixels cannot be quote-matched] Fig 3A bar chart '% Protein aggregation in hippocampus', C vs AD pairs: TPC6A p=0.942, TIAF1 p=0.850, p-WWOX p=0.036, NFT p=0.014, Abeta p=0.003.` | PMID 25650666, Figure 3A, `files/figure_renders/PMID25650666/pdfimg_p05_0.jpeg`)
