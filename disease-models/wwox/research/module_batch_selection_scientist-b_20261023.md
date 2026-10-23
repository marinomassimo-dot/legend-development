# Module batch 2026-10-23 — selection note and observations, rows Q-N-08 to Q-N-15 (scientist-b)

Task `MODULE-B-20261023`, under `ORCH-MODULE-BATCH-20261023`. Input: the handoff rows of
[`repurposing_batch_selection_20261023_module.md`](repurposing_batch_selection_20261023_module.md).
Reading mode: `PRIMARY_EVIDENCE_READ`, context declared `QUESTION_DRIVEN` (the map's conclusion was in
context before reading). Every paper below that is not about WWOX is **NOT WWOX EVIDENCE**. No dose,
administration or suitability is stated or implied anywhere in this note. Not medical advice. Class-level
only; no individual-level record.

## 0 · Result in six lines

1. The eight map records (`mechanism_intervention_map.md` lines 697 to 760) contain **no author-year
   citation, no PMID and no wikilink**. The row's Ask ("resolve the author-year citations of this record")
   had nothing to resolve. The support lives in the discovery ledger, the dismissal ledger, the claim
   registry and the paper registry; I reached it with `registry_records.py get --theme` and `--pmid`.
2. "NO_RECEIPTED_EVIDENCE" is false for seven of the eight rows. It is a property of the row's empty PMID
   cell, not of the repository: behind N-09 to N-15 there are already between two and thirteen receipted
   papers (counted in section 4.1). It is true only for one premise: the **dichloroacetate neuropathy premise of N-08 has
   no source anywhere in the registries**.
3. Seven reads were done (six new papers, one completing pass on a partial receipt), all staged, none
   recorded. Against the map's wording they show it saying more than its sources in N-08 (paediatric
   neuropathy) and N-10 (cannot versus most likely not eligible); the same is true of N-12 (a hypothesis
   written as a finding) and of N-15 (a dropped qualifier), the last two from registry records, not from a
   new read.
4. The strongest new finding is on N-10: an expert consensus (the N=1 Collaborative guideline) classifies a
   variant that fully abolishes canonical splicing as **not eligible** for splice correction, and sets a hard
   rule at 5 bp from the boundary. That supports the map's direction, and it also shows the map's wording
   ("the modality cannot do the job") is stronger than the guideline's own ("most likely not eligible"),
   because the guideline's test for "destroyed" is a functional transcript measurement that has never been
   made for the reference acceptor allele.
5. The completing pass on the myelin preprint (N-13) found a **text-figure disagreement**: the Results give
   59.1 versus 36.1 myelinated axons per field after remyelination, the bars in Figure 3d read about 106
   versus about 58 (hand reading). Direction identical; which is right is UNVERIFIED.
6. Parked, acquisition-limited and not read: Lo 2008 (the primary behind N-09), and four WWOX clinical
   papers relevant to N-15 (all closed access). Cascade below.

## 1 · Step 1 — selector work, per row

Legend for the three tests: **A** abstract substantive, **B** lawful full-text body obtainable, **C** a
question the paper could change. "Receipt state" is read from the ledger and the staged receipts on
2026-10-23 with `registry_records.py`, `paper_packet.py` and the receipt ledger; PubMed identity by
`pubmed_identity_check.py` (title overlap 1.0 and DOI resolving, for every paper read or proposed below).

### Q-N-08 Dichloroacetate (map line 697)

| Source the map's wording rests on | PMID | Receipt state |
|---|---|---|
| Map cites nothing. Neighbouring rows in the ledger: the WWOX-HIF1A-PDK arm (digoxin target validation) | 25012504 | complete read, 2026-08-14 |
| Human fibroblast WWOX-silencing metabolism primary and its review (neither mentions dichloroacetate; term count zero in both) | 35328751, 36271927 | complete reads |
| **The neuropathy premise ("dose-dependent peripheral neurotoxicity in a child")** | none found | **no source in any registry record** |

Additional papers (up to three): 23611579 (long-term safety in congenital lactic acidosis, PMC author
manuscript; A yes, B yes, C yes: it is paediatric neuropathy data) **read**; 36432491 (combination with
pyruvate after an acquired seizure in adult rats, PMC open; A yes, B yes, C yes: the opposite sign to the
map's framing) **read**; 31208525 (a review of the neuropathy, closed access, B no) not read; 31624634
(adult cancer cohort, GSTZ1 genotype and pharmacokinetics, open) proposed, not read (B yes, C weak: adults).

### Q-N-09 pTyr33-WWOX peptide (line 703)

| Source | PMID | Receipt state |
|---|---|---|
| Primary: Lo 2008, MPP+ neuronal death involves Tyr33 phosphorylation of WOX1 | 18371080 | **no receipt; closed access**; identity check passes |
| Commentary that over-interpreted it: Sze 2015 | 26355344 | two receipts (2026-09-20, 2026-10-19), commentary |
| Chang 2015, aggregation cascade (also carries pTyr33 as a readout) | 25650666 | three receipts, last complete |
| Carvalho 2022, WWOX inhibition by the Zfra peptide restores mitochondrial homeostasis in neuronal cells | 35984507 | three receipts, last 2026-10-19 |
| Liu 2022 review of pY33 to pS14 transition | 35883580 | receipted 2026-10-19 |

Additional papers: none lawful. 15664696 (Chen 2005, light-induced retinal damage, Tyr33) is closed
(Europe PMC OA flag N); 29067327 (Zfra in Alzheimer mice) is open but already receipted twice. The
load-bearing primary (Lo 2008) is acquisition-limited: Europe PMC `inEPMC=N`, OpenAlex `closed`. It goes to
the human acquisition packet, not to a reading queue (a point already made in the ledger).

### Q-N-10 Splice-switching ASO for a canonical acceptor allele (line 712)

| Source | PMID | Receipt state |
|---|---|---|
| Rat *lde*, exon 9 frameshift, protein absent (Suzuki 2009) | 19500159 | complete read, 2026-08-06 |
| Rat *lde* full text (Tochigi 2019) | 31340538 | two receipts, last 2026-10-19 |
| The one WWOX canonical-site transcript measurements the ledger cites (a donor allele, 2024) | 39101447 | receipted |
| An acceptor allele with exon 6 skipping, abstract-only in the ledger | 30853297 | no receipt, not obtained |
| "The Milasen precedent is regulatory" | none cited in the map | Kim 2019 was not receipted |

Additional papers: 40139194 (Cheerie 2025, N1C VARIANT consensus guidelines; A yes, B yes with Data S1, C
yes: it is the counterexample search the map says was never run) **read**; 31597037 (Kim 2019, milasen; B
yes) **read**; 37438524 (Kim 2023, taxonomy of ASO-amenable variants; B yes) **read, targeted**.

### Q-N-11 4-PBA / TUDCA on the ER-chaperone rationale (line 720)

| Source | PMID | Receipt state |
|---|---|---|
| `DIS-004` / `D-02` (wrong compartment); the cytosolic-lysosomal route rests on `DL-MECH-047` | 41124647 | three receipts, last complete-ish 2026-10-04 |
| Aldaz 2014 review of WWOX degradation pathways (`DL-MECH-036`) | 24932569 | three receipts |
| R1 proteostasis lot already read 2026-10-21/22 | 42587736, 42650175, 41378214, 41373471, 42569303, 40421674, 39013852, 40449593, 42161426, 41274966 | all receipted, checked first, **not re-read** |
| 4-PBA in SLC6A1 disorders, "pharmacochaperoning over HDAC inhibition" (the revival-trigger question) | 42157447 | complete read, 2026-10-21 (outside the R1 list above, found by title search) |

Additional papers: none needed; the revival trigger of `DIS-004` (HDAC-inhibitor route) is already
addressed by 42157447 in a non-WWOX system. One further statement on HDAC inhibitors acting through HSP
modulation was found in the Discussion of 30497978 (read for N-12).

### Q-N-12 HSP70 co-inducers (line 726)

| Source | PMID | Receipt state |
|---|---|---|
| `D-03`; "HSC70 delivers to the lysosome" rests on `DL-MECH-047` (P252A model) | 41124647 | three receipts |
| WWOX induction degrades Bcl-xL and Mcl-1 through a lysosomal pathway (adjacent, not on the map) | 41677633 | three receipts |
| Arimoclomol | none cited | the only registry mention is one full-text-queue record |

Additional papers: 30497978 (Fog 2018, arimoclomol and mutant glucocerebrosidase; A yes, B yes, C yes: it
tests the sign for an ER-synthesised lysosomal client) **read**; 34418116 (arimoclomol phase 2/3 in a
paediatric lysosomal disease, open) proposed, not read (C weak: clinical efficacy in another disease).

### Q-N-13 Pro-myelinating agents (line 731)

| Source | PMID | Receipt state |
|---|---|---|
| Neuronal deletion causes epilepsy and myelin defects; astrocyte and oligodendrocyte conditional deletions show no evident anomaly (Repudi 2021, Brain) | 33914858 | three receipts; bronze OA |
| Neonatal neuronal gene therapy (Repudi 2021, EMBO Mol Med) | 34747138 | many receipts |
| Neuron-specific gene therapy 2026 and the review | 42422765, 42128308 | many receipts |
| Rat *lde* hypomyelination (window PND5-21) | 31340538 | two receipts |
| "Review-sourced primary still queued" (an oligodendroglia-lineage deletion preprint) | DOI 10.1101/2025.11.22.689900 | one partial receipt (figures and supplementary captions only) |
| Clemastine impairs developmental myelination (not on the map) | 35372341 | complete read, 2026-10-21 |

Additional papers: the preprint was the partial receipt, so priority one: **completing pass done**. Others
considered, open, not read: 39820244 (incomplete remyelination via enhanced oligogenesis, C weak),
37460763 (liothyronine safety, adults, C weak).

### Q-N-14 Antioxidants (line 744)

| Source | PMID | Receipt state |
|---|---|---|
| Diabetic mouse photoreceptors, WWOX up and knockdown lowers superoxide (Saadane 2021) | 34214506 | three complete receipts |
| Fly Wwox, Idh and Sod genetics, thresholded CM-H2DCFDA | 21075834 | two receipts, last partial (supplementary captions only) |
| Human fibroblast metabolism primary | 35328751 | complete |
| Clinical lactate signal (Chong 2023) | 36537114 | receipted |
| Bladder cancer gain-of-WWOX ROS | 36364214 | complete |
| Muscle-specific ablation | 30755385 | receipted |

Additional papers: **none**. A PubMed query for WWOX with N-acetylcysteine, antioxidant or NAC returned four
records, all in the UV/cold-shock "bubbling cell death" line; I did not open them. No paper testing an
antioxidant in a WWOX-deficient system was found, which is itself the finding for this row.

### Q-N-15 Counting seizure control as developmental protection (line 754)

| Source | PMID | Receipt state |
|---|---|---|
| The quoted outcome sentences (Shaukat 2018, two children and a literature table) | 30361190 | complete read, 2026-10-03 |
| Mortality and drug-resistance cohort (Oliver 2023) | 36779245 | seven receipts |
| Registry cohort where the genotype-mortality contrast does not replicate (Gao 2025) | 40875931 | two receipts |
| Other series already receipted | 33916893, 36537114, 28721938, 39507621 | receipted |

Additional papers (A yes, C yes, B **no** for all four): 25411445 (Mignot 2015), 41442931 (vigabatrin
MRI changes, 2026), 42721537 (seven-patient series, 2026), 39039877 (Chinese cohort, 2024). OpenAlex
`closed` for the first three, Europe PMC `OA=N` for all. Parked for the acquisition packet.

## 2 · Step 2 — the seven reads (all staged; none recorded)

All manifests PASS (`deepdive_manifest.py --verify-artifacts --require-current-schema`), strength scan run
(advisory; two wording flags fixed before commit), numerals appear in the quotes, `paper_packet.py check`
run on the first paper, receipts checked with `staged_receipt_check.py --check-doi`. Figure values: none
written from an image placeholder; the only figure readings are on the preprint and Figure 2 of Kim 2023,
both opened as images; hand readings are labelled.

| PMID | Paper (NOT WWOX EVIDENCE unless stated) | Row | Depth | Receipt staged | Manifest | Locators |
|---|---|---|---|---|---|---|
| 23611579 | Long-term safety of dichloroacetate in congenital lactic acidosis, 2013 | N-08 | partial (figures unavailable, Table 1 not opened) | FTR-20261023-23611579-01 | PASS | 8 |
| 36432491 | Dichloroacetic acid plus pyruvate after seizure in rats, 2022 | N-08 | partial (Methods 2.5-2.14, figures not read) | FTR-20261023-36432491-01 | PASS | 8 |
| 40139194 | N1C VARIANT consensus guidelines for ASO eligibility, 2025 | N-10 | partial (main text whole, Data S1 targeted) | FTR-20261023-40139194-01 | PASS | 8 |
| 31597037 | Patient-customised oligonucleotide therapy (milasen), 2019 | N-10 | partial (figures, appendix unavailable) | FTR-20261023-31597037-01 | PASS | 7 |
| 37438524 | Framework for individualised splice-switching ASO therapy, 2023 | N-10 | partial, targeted | FTR-20261023-37438524-01 | PASS | 6 (5 text, 1 figure) |
| 30497978 | Arimoclomol and glucocerebrosidase refolding, 2018 | N-12 | partial (Intro, Methods, figures not read) | FTR-20261023-30497978-01 | PASS | 7 |
| PPR1124524 | Oligodendroglia-lineage Wwox deletion and remyelination (**WWOX, PREPRINT, not peer reviewed**) | N-13 | partial; completing pass: main figures now read | FTR-20261023-PPR1124524-02 | none (preprints carry none in this repository) | n/a |

What each read says, with the limit:

- **23611579.** Eight patients with congenital lactic acidosis, long follow-up, open label. Three had the
  drug paused or reduced for *asymptomatic* worsening of lower-limb nerve conduction. Symptomatic neuropathy
  that ended a trial is attributed to an older adolescent and adult MELAS trial; the authors name age
  (metabolism falls with age) and a gene haplotype as modifiers, and say the design cannot separate drug
  from disease. The efficacy endpoint is blood lactate. No WWOX, no neuronal bioenergetics.
- **36432491.** Adult male rats, pilocarpine seizure injury. Seizure raised PDK2 and lowered ATP; the
  *combination* with pyruvate raised neuron counts, and the authors state each agent alone was ineffective.
  Groups of five and eight; one week of treatment; one sensorimotor test. The authors themselves note a
  neurotoxicity ceiling citing other work. An acquired injury, not a WWOX or developmental model.
- **40139194.** Expert consensus, not an experiment ("no gold-standard evidence for many considerations").
  Data S1: canonical splicing destroyed means the variant is "most likely not eligible"; "destroyed" means
  no wild-type transcript seen in functional analysis, and faint wild-type bands in a gel should be looked
  for because authors sometimes overstate; variants within 5 bp of the boundary are not eligible; the first
  and last coding exons are usually not eligible for exon skipping. Table 2 lists one canonical donor
  variant as a "not eligible" training example. Nothing about WWOX.
- **31597037.** The drug targeted a *gained* cryptic acceptor 119 bp upstream of a retrotransposon insertion
  deep in an intron; it masks; it raised the normal-to-mutant ratio in patient cells. One patient, no
  control; seizure frequency and duration fell by more than half on EEG while MRI showed continued brain
  volume loss. The authors say only a minority of patients have mutations amenable to this strategy and
  that the drug is not transferable.
- **37438524.** Taxonomy: gain of a splice site is more amenable than weakened exon definition; severe
  canonical damage routes to "unlikely amenable" (Figure 2, read as an image); 72 percent of amenable
  events deep intronic; the validated set was probably or possibly amenable variants, so the "unlikely"
  class was not tested in this paper. Only the Results subsection on amenable variants, the taxonomy
  Methods, the Discussion and Figure 2 were read.
- **30497978.** In patient fibroblasts and stem-cell-derived neuron-like cells the heat shock co-inducer
  raised the level of mutant glucocerebrosidase (an ER-synthesised lysosomal enzyme), including the
  EndoH-resistant fraction; the authors could not resolve which HSP70 family member acts, could not show a
  fall in substrate storage, and the compound belongs to the funder. The Discussion records that HDAC
  inhibitors rescue the same client partly through HSP90/HSP70 modulation. Cytosolic client: not tested.
- **Preprint completing pass.** Main Figures 1 to 6 opened. New: Figure 3c has no knockout bar for the
  normal-diet group (control N=3 only; N=2 per genotype in demyelination; N=3 in remyelination); Figure 3d
  right panel reads about 117 vs 125 (normal diet), about 53 vs 56 (demyelination), about 106 vs 58
  (remyelination) while the Results give 59.1 vs 36.1 for remyelination; the MBP text says 60 vs 40 and
  the bars read about 59 vs 36 (hand readings, plus or minus about 3). WWOX appears faint, not absent, in
  the knockout Oli-neu lanes of Figure 6f (150 dpi, UNVERIFIED at higher resolution).

## 3 · M4b — prior knowledge admitted for comparison

`FIRST-PASS OBSERVATIONS COMPLETE → PRIOR KNOWLEDGE ADMITTED FOR COMPARISON.` Admitted: the map records
N-08 to N-15, `DIS-004`, `D-02`, `D-03`, `DL-MECH-039`, `CLAIM 031`, `CLAIM 009`, `CLAIM 005`. The six new
PMIDs return **empty** from `registry_records.py get --pmid ... --hops 1`: that is a statement about that
query, not about the laboratory's knowledge.

| Row | Map wording | What the read papers say | Match |
|---|---|---|---|
| N-08 | dose-dependent peripheral neurotoxicity "in a child with encephalopathy" is an unfavourable ratio | children in a long open-label series: asymptomatic nerve-conduction worsening in three of eight, drug paused or reduced; symptomatic neuropathy sits in an older-adult trial; age and genotype modify exposure | **partly**; the paediatric statement is stronger than the paper, the adult statement is stronger than "in a child"; no source for the premise existed |
| N-08 | "dominated" by the ketogenic diet | not tested in any paper read; the seizure-injury rat paper argues the opposite sign for the combination only | not assessable |
| N-10 | SSOs mask, cannot create sites; "the modality cannot do the job" | guideline: canonical splicing destroyed means most likely not eligible; within 5 bp not eligible; last coding exon usually not eligible for skipping; milasen was a gained deep-intronic cryptic acceptor | **direction matches; headline is stronger** than the source, because "destroyed" is a transcript measurement not yet made for the reference acceptor allele |
| N-10 | "Milasen is regulatory, not proof of amenability" | the paper itself: gained cryptic site, one patient, not transferable | matches |
| N-12 | "may accelerate the damage" | arimoclomol raised mutant ER-to-lysosome enzyme in vitro; no cytosolic client tested; mechanism unresolved by the authors | map is a hypothesis; paper neither supports nor refutes it |
| N-13 | oligodendrocyte deletion "produces no evident anomaly" | in the preprint true at baseline; ageing and cuprizone unmask a remyelination defect, with a text-figure disagreement in the numbers | holds for development only; "partial benefit not excluded" is the right caveat |
| N-15 | impairment "does not improve when epileptic activity is controlled" | not read by me (already receipted); the registry's own `CLAIM 031` records the qualifier "in some of these cases" and an order-of-onset ambiguity; the map record carries neither; milasen (a different disease) shows seizure reduction with continued volume loss | **map not synchronised with the claim it rests on** |

## 4 · Observations on the module row (for the operator's diagnosis)

### 4.1 Cross-cutting

**What the join measured.** All eight rows say `Dependence measured: NO_RECEIPTED_EVIDENCE` with an empty
PMID cell. The measurement is a property of the row (no PMID attached), not of the repository. Counting
the receipted papers behind each row from the registry (tables in section 1): N-08 zero on the DCA premise
(three adjacent), N-09 four plus one unreceipted primary, N-10 three plus one abstract-only record, N-11
thirteen (including the ten of the R1 lot), N-12 two plus the R1 context, N-13 six plus the preprint's
partial receipt, N-14 six, N-15 seven. So a reader taking the row at its word would have sent a Scientist to "find evidence" for rows that already have
dozens of receipts, and would have missed the one row (N-08's neuropathy premise) that truly has none.

**Citation resolution score.** Author-year citations in the eight map records: **0 of 0**. Nothing
resolved cleanly because nothing was there; the row text ("the mechanism map cites the support in prose by
author-year") is wrong for this lot. What I did instead, and what worked: take the record's *premise*
(dismissal-ledger `DIS-nnn` and `D-nn` ids, claim and paper ids named in neighbouring records) and run
`registry_records.py get --theme <literal>`. That found 32 distinct source PMIDs across the eight rows (excluding the ten R1 papers); 30 were
already receipted (two, Lo 2008 and an acceptor-allele abstract-only record, were not). Of the 32, a
reader could reach the PMID from the map alone for **zero**.

**Was the Ask the right ask?** No, in three ways. (1) It asks for a lookup that has no object; the right
Ask is "list the papers this record's premise rests on, with their receipt state, and say which premise
has none". (2) It never asks the question the record itself marks as open: N-10 says "stress-tested, not
refuted: no systematic counterexample search was run" and that is exactly what a Scientist should do (I did:
three papers); N-09 says "if the full text says otherwise it re-opens" (acquisition-limited); N-13 says a
primary is "still queued" (it was already partly read). The open clause of each record is the Ask. (3) It
says "propose reading rows" but the failure modes are mostly *about a premise*, so the productive output
was premise-level (is the neuropathy premise sourced? is the compartment premise sourced?), not
paper-level.

**What I needed that the row did not say.**
- The record's own premise ids (`DIS-004`, `D-02`, `D-03`, `DL-MECH-047`) and which claim id the wording
  feeds (`CLAIM 031`, `CLAIM 009`, `CLAIM 005`); I found them by theme search, which a tool could print.
- The receipt state *by theme*, not by row PMID; the row's `PMIDs` column is empty for every row of this lot
  and a join over the registry's own PAPER ids would have filled it.
- Whether the decisive paper is **lawfully obtainable**: the primaries behind N-09 (Lo 2008) and N-15 (four
  clinical papers) are closed access; the row should carry an acquisition state, so a Scientist does not
  spend an hour discovering it. For N-09 the ledger already said so.
- The **revival trigger** and the paper that could trip it (`DIS-004` names the HDAC-inhibitor route; a
  receipted paper on exactly that already existed and the row did not say).
- A **non-WWOX labelling rule** and the "no dose" rule for DCA, arimoclomol, 4-PBA: this came from the
  dispatch message, not from the row.
- The **overlap with the R1 proteostasis lot**; again from the dispatch message. A join that knows the
  receipted set would have marked N-11 and N-12 as "covered by receipts X".

**Did the map's wording match the papers?** Mostly in direction, in four places not in strength: N-08
(paediatric neuropathy), N-10 (cannot versus most likely not eligible), N-15 (missing qualifier), N-12 (a
hypothesis written as a finding, "may accelerate"). N-09 and N-13 matched what they cite; N-14 matched its
registry sources but cannot be extended because no paper tests an antioxidant in a WWOX system.

### 4.2 Row by row (one finding each)

- **N-08.** The Ask was the wrong ask: the load-bearing premise (DCA neurotoxic in children) had no source;
  the useful act was to find one. Found, and it is weaker than the map's wording. A second paper pushes
  the opposite sign in an acquired seizure model (combination only).
- **N-09.** Ask not satisfiable: the primary is closed. The row should have said "acquisition-limited, go
  to operator PDF pack". Selection work: 5 sources resolved, 0 new lawful.
- **N-10.** Right row, best result: the counterexample search the map said was missing. Needed: the row to
  carry the sentence "no systematic counterexample search was run" as the Ask.
- **N-11.** Already answered by receipts, including a paper on the revival trigger found by title search;
  the row cost the repository an hour of re-derivation. No read was added; one non-WWOX statement relevant
  to the trigger was recorded from the N-12 paper's Discussion.
- **N-12.** Arimoclomol appears in the registry only in a queue record, never in the map's text with a
  source; the read supplies a non-WWOX comparator, no more. The row's phrase "may accelerate the damage"
  should be tagged as a hypothesis in the map.
- **N-13.** The row hid a partial receipt (the preprint). The completing pass was the single most
  productive act of the lot and was possible only because I read the map's last sentence.
- **N-14.** Nothing to add; the row should say "no intervention paper exists in a WWOX system" instead of
  "no receipted evidence".
- **N-15.** The map and the claim registry have drifted apart; the row had no way to see it. A "wording
  checked against the claim it feeds" column would have caught it.

### 4.3 What the module cannot see (my evidence for the diagnosis)

1. **Receipts by premise.** It sees PMIDs typed in the record; this lot has none, so it sees nothing.
2. **Prose-cited and id-cited support.** The map cites through ledger ids, not through PMIDs.
3. **Acquisition state** (closed, bronze, preprint-only).
4. **Claim drift** between the map and the claim registry (N-15 qualifier).
5. **A premise with no source** (N-08) looks identical to a premise with ten.
6. **Typed pharmacological assertions**: "neurotoxic", "dominated", "delivers to the lysosome", "may
   accelerate" are assertions about a drug; each needs a typed field (assertion, source id, tag
   FINDING / HYPOTHESIS / DEFAULT, direction, system), which the map prose does not carry.

## 5 · Parked, with the cascade run

| Item | Why | Cascade run |
|---|---|---|
| 18371080 Lo 2008 | closed access, no PMC | PubMed identity; Europe PMC `inEPMC=N`, `OA=N`; OpenAlex `closed`; no author-manuscript route found |
| 25411445, 41442931, 42721537, 39039877 (N-15) | closed access | Europe PMC OA flag N for all four; OpenAlex `closed` for the first three; not run: interlibrary routes, author-email |
| 31208525 DCA neuropathy review | closed | PubMed record only |
| Unpaywall | not used | its terms ask for a contact address; I did not send the operator's address |

I did not run the full `find-fulltext` cascade for these; I ran the two public OA indices above. Stated so
that nobody reads "parked" as "exhaustively searched".

## 6 · Defaults taken

- Receipts depth understated: `partial_fulltext_read` for all seven; supplement and figure coverage
  declared `not_read`, `captions_only` or `unavailable` per paper.
- Text-layer of Data S1 re-derived with PyMuPDF after `pdftotext` left form-feed control characters that
  the manifest verifier refuses; the control-character file was deleted, not stripped.
- The 12-paper ceiling was not reached: seven reads. The remaining candidates were closed, already
  receipted, or low-yield for their row.
