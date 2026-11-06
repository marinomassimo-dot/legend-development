# Wave-2 briefs (2026-11-05): two questions found open, executable at zero spend and unclaimed by the map

Read `BRIEF_COMMON.md` first; it binds (open routes only, no e-mail or contact parameter, no administered-dose numbers, depth honesty, write only inside your directory, claim each PMID with `paper_packet.py claim`, stage receipts and never record them). The deliverable shapes of `BRIEF_COMMON.md` apply (README answer first, one evidence table, `queries.tsv`, `module_inputs.md`, `receipts/` with `INDEX.tsv`). Two further binding rules found during wave 1:
* Do not write any of these phrases anywhere: proband, index patient, index case, case subject, affected child, affected individual, individual patient, study participant, patient-derived, patient-specific, patient cells; do not write the words Italy, Italia, Italian or the string mg/kg.
* Keep every script and intermediate file in your own subfolder of the scratchpad given in your task, never in the scratchpad root (several actors share it).
Where a rule of wave 1 does not fit your question, say so in the README instead of bending the table.

The map of open questions is `batch_sci_20261105/map/open_questions_map.tsv` (look up your row by `qid`) with its README. Both questions below are rows of that map; the map's own text for them is in `map/README.md` section "The five open questions executable at zero spend".

---

## W2-ISR (label `sb-w1`, directory `w2_isr_seizure/`, receipt `NN` = `26`)

Map row `WO-06`. **Question.** (1) Is there a mammalian primary study of integrated-stress-response (ISR) modulation on seizures or epilepsy models (ISRIB or other eIF2B activators, PERK or GCN2 inhibitors, agents that raise eIF2-alpha phosphorylation, genetic loss of a kinase or of PPP1R15A/B), and in which direction, at which node, in which stress class and cell type did it move seizure threshold, seizure frequency, interictal activity or survival? (2) What does the paper that rebuts the claim that Sephin1 (and guanabenz) inhibit the eIF2-alpha phosphatase (PMID 29618508) actually show, and does it change how the module should word any ISR lever that cites Sephin1? (3) Do the five abstract-only glial/myelin papers listed in `batch_it28_p4_isr_role_20261105/A_glia_myelin/README.md` change at full text?

**Decision at stake.** The design of the premise test of investigation `INV-02` (rank 1, the ISR sign in WWOX-deficient human neural cells) and the order of ISR lever classes. The IT28 verdict is that no lever class is preferable until the protein-level sign is measured; a seizure precedent would be the first mammalian row for either direction. The challenge `CH-IT28-ISR-ROLE` names a mammalian ISR-modulation seizure study as its own re-evaluation condition.

**Done: cite, do not repeat.** Read `batch_it28_p4_isr_role_20261105/README.md`, `A_glia_myelin/README.md` and `B_neurons/README.md` (it says the seizure search was title and keyword searches of Europe PMC and not exhaustive), `needs/needs.json` need `NEED-ISR-ATTENUATION`, card `E01_isr_modulators`. Their sources have receipts: use `depth.py` (see BRIEF_COMMON) before reading any PMID again; re-open a source only for a stated new reason and set `prior_receipt`.

**Table** `evidence_w1.tsv`, columns in this order: `row_id, role, system, species_and_model, isr_node_perturbed, perturbation_type, stress_class, cell_type, endpoint_class, endpoint_detail, direction_on_endpoint, effect_note, attribution, source_id, source_depth, locator_quote, transfer_conditions, transfer_breakers`. `perturbation_type`: genetic_loss | genetic_gain | compound | other. `direction_on_endpoint`: favourable | adverse | null | context_dependent | undetermined. `attribution`: target_controlled | compound_only | not_applicable. `endpoint_class`: seizure | interictal | survival | neuronal_function | glia_myelin | other. `role`: support | counter | context. A compound effect is not attributed to a node without a target-specific control in the source.

**Consequences fixed before you search.**
| Return | Consumer action |
|---|---|
| a mammalian primary seizure study of ISR modulation exists | the row is recorded with node, stress class and direction as a precedent; `CH-IT28-ISR-ROLE` reevaluate_when is met; the INV-02 test text gets one line naming the precedent; no lever is promoted |
| none after the bounded search | stated as "not found after: <queries>" with the Europe PMC and PubMed strings; the hole in the IT28 seizure search is closed or confirmed |
| the Sephin1 rebuttal shows the compound does not act as the module's lever text says | the wording of every ISR lever row that cites Sephin1 or guanabenz is listed with the sentence that must change (proposal only) |
| the five glial papers change at full text | stated per paper with the passage; unchanged otherwise |

Breadth: 8 to 12 sources at full text; stop when answered or exhausted.

---

## W2-SUPP (label `sb-w2`, directory `w2_suppressors/`, receipt `NN` = `27`)

Map row `RS-R6`. **Question.** Is there any perturbation that suppresses, or any gene that modifies, the phenotype of WWOX deficiency (loss or hypomorph) in Drosophila, zebrafish, mouse, rat or a human cell or organoid system, found by a genetic screen, a cross, a CRISPR screen or a co-dependency analysis? The three lookups proposed on 2026-10-31 were never run: FlyBase genetic interactions for the Drosophila Wwox gene; BioGRID ORCS CRISPR screens for WWOX; DepMap WWOX co-dependencies. IT12 found DepMap behind a human-verification page.

**Decision at stake.** A lever that needs no residual WWOX protein would be the first for the missense and null classes of the reference genotype; IT10 and IT12 found none in the literature they reached. A bounded negative is also a result and closes a reopen row (`recovery_it10_p23_20261031/reopen_searches.tsv`, row R6).

**Done: cite, do not repeat.** `recovery_it10_p23_20261031/README.md` item 6 and `reopen_searches.tsv` row R6; the map row `RS-R6` (the Alliance of Genome Resources API answered key-less for the human gene record and the genetic-interactions endpoint on 2026-11-05T22:51Z; content not analysed).

**Work.** (1) Alliance of Genome Resources API (key-less): the WWOX gene records and genetic and physical interactions for human WWOX, mouse Wwox, rat Wwox, zebrafish wwox and Drosophila Wwox (fly gene symbol and identifier to be resolved from the Alliance, not recalled), plus the disease-association annotations; report what is there and its evidence codes, including FlyBase-sourced interactions. (2) BioGRID ORCS: the public screen listing for WWOX (bulk download or the web table; no access key, no account; if only a key route exists, record it as blocked). (3) DepMap: only a route that needs no account and no human verification; otherwise record the block. (4) PubMed and Europe PMC: `Wwox` with suppress*, rescue*, modifier, enhancer, epistasis, synthetic, screen, in the organism terms; read the decisive primary sources found. Keep what the database says apart from what a paper reads; a database interaction is a lead, not evidence of suppression, until the primary study is read.

**Table** `evidence_w2.tsv`, columns in this order: `row_id, role, organism_or_system, wwox_perturbation, interactor_or_modifier, interaction_type_as_stated, evidence_code_or_assay, phenotype_modified, direction, source_database_or_paper, source_depth, locator_quote, transfer_conditions, transfer_breakers`. `direction`: suppresses | enhances | no_effect | undetermined. `role`: support | counter | context.

**Consequences fixed before you search.**
| Return | Consumer action |
|---|---|
| a suppressor or modifier of a WWOX-deficiency phenotype is documented in a primary study | recorded as a lead with organism, assay and direction; reopen row R6 is re-statused (proposal) and the gene is proposed for the needs table only as `exploratory_question` |
| only database annotations without a primary study that shows suppression | listed as leads to read, not as findings |
| nothing in any route | R6 becomes "bounded lookups run on <date>: none"; the three routes and their blocks are named |

Breadth: all four routes once; read at most 8 primary sources at full text. Stop when answered or exhausted.
