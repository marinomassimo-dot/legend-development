# Module batch 2026-10-23 — Scientist C: rows Q-R-04..09 and REPLICATE Q-N-16, Q-R-01, Q-R-03

ACTOR_ID `scientist-c`, task `MODULE-C-20261023`. Input: `repurposing_batch_selection_20261023_module.md`.
Every paper below that is not a WWOX paper is **NOT WWOX EVIDENCE**. No dose, route, administration or
suitability is stated or implied. Not medical advice.

## 0 · Scope actually delivered, said first

| Part | Delivered |
|---|---|
| (1) Resolve map citations of R-04..R-09 | Done. Four of the six records contain no author-year citation at all (see section 3). |
| (1) Up to 3 further papers per row | Done at **abstract/identity level** (PubMed title+abstract search 2026-10-23, titles screened, registry/manifest presence checked). |
| (2) REPLICATE search and lead specs | Done. The three module lead specs were **REFUSED** by `discovery_lead.py check`; corrected specs were checked OK and staged. |
| (3) Full-text reads | **Lot 1: none completed (0 of 12). Lot 2 (section 6 below): four read, two parked.** Lot-1 text follows: **None completed (0 of 12).** The per-paper pipeline (packet, claim, acquisition, locators, manifest, staged receipt) was not run: resolving the bindings consumed the session and the finding that most WWOX-side evidence is already receipted removed the "NO_RECEIPTED_EVIDENCE to evidence" payoff the reads were prioritised for. No receipt is staged; no figure value is written. |

Reserve reading list, in priority order, is in section 5.

## 1 · SELECT rows: what the map actually cites, and what resolves

Method: `registry_records.py get --theme/--pmid`, `esummary` titles via `eutils.py`, manifest presence in
`deepdive_manifests/`. "Receipted" means a manifest and receipt id exist; depth is as stated in each manifest.

### Q-R-04 Lithium (map line 476)
Citations in the record: `Wang 2012` (1), plus the claim id `CC-20260826-GSK3B-S9-AXIS-01`, `BATCH_20260927_004`.
- Wang 2012 resolves to PMID 22193544 (Cell Death Differ). Identity checked by PubMed metadata (title, DOI 10.1038/cdd.2011.188). Manifest present, receipt `FTR-20260726-22193544-02`. **Already receipted.**
- The PTZ lithium experiment the record rests on is Cheng 2020, PMID 32000863 (Acta Neuropathol Commun), cited nowhere by author-year in the record. Manifest present, depth `partial_fulltext_read` (the packet lists 7 sections owed, artefacts absent from this worktree because `files/` is shared and gitignored).
- Outcome: NO_RECEIPTED_EVIDENCE is a **binding artefact**; two WWOX papers are receipted.
- Further papers (all NOT WWOX EVIDENCE, none read):
  1. Uzay 2026, Neuropsychopharmacology, PMID 42661025: lithium in SNAP25 encephalopathies, via homeostatic plasticity. Question it could change: the record states "nothing in genetic DEE" for lithium. Not in registry.
  2. McCamphill 2020, Sci Transl Med, PMID 32434848: selective GSK3 alpha inhibition in a fragile X mouse. Question: isoform specificity of a GSK3 lens on lithium. Not in registry.
  3. none further: the query lithium + PTZ/seizure threshold + GSK3, 2018 onward, returned only PMID 32000863. That is a statement about this query only.

### Q-R-05 Ketogenic diet (line 501)
Citations: none by author-year. Prose names "3/5 WOREE patients in one report", "four independent sources", a transcriptome organoid result.
- "3/5 WOREE" resolves, by registry and `CC-20261020-SCIENTIST-B-KETO-ENDPOINT-01`, to PMID 36537114 (manifest present, `partial_fulltext_read`).
- Metabolic batch 2026-10-19/20 already holds, with manifests: Hu 2025 review PMID 40831798, Klepper 2026 PMID 41830506, Joshi 2025 in-silico PMID 40659031 (candidate `CC-20261019-SCIENTIST-B-G2-KD-PRIOR-01`), Samanta 2026 PMID 42846717, Steinberg 2021 organoids PMID 34268881. **Not re-read, per instruction.**
- Further papers, none read, none in registry: Madsen 2026, Mol Genet Metab, PMID 42341672 (ketogenic therapy in PDH deficiency, clinical practice and survey). This is the only paper found that speaks to the record's mechanism sentence, ketone entry below a PDH block; a reading could move "mechanistic gap" on the PDH-bypass premise. Second: Song 2026, Zhonghua Er Ke Za Zhi, PMID 42742013 (ketogenic therapy in genetic DEE with onset under 2 years); lawful full text unchecked.

### Q-R-06 Anti-neuroinflammatory (line 526)
Citations: none by author-year (IBA1/GFAP, Il6 vs Tnf-a n=4, P47T, neuron-restricted rescue named in prose).
- Resolves to Hussain 2019 Neurobiol Dis PMID 30290271 (manifest), Hussain 2023 Prog Neurobiol PMID 36828035 (P47T, manifest), Repudi 2021 Brain PMID 33914858 (manifest), De La Cruz 2025 preprint PMID 39868255 (manifest). All receipted.
- Further papers, none read, none in registry: Alonso 2023, Neuropharmacology, PMID 37290534 (cannabidiol and beta-caryophyllene in a Dravet mouse, disease-modifying and glial endpoints); Thompson 2022, Epilepsia Open, PMID 34826216 (astrocyte reactivity in an SCN8A encephalopathy mouse; bears on gliosis as consequence versus driver, the record's "target downstream of target"); Verrillo 2025, Epilepsia, PMID 40608247 (cannabidiol, DEE type 1 mouse, survival). Note the record names "no compound": these test whether treating glia in a genetic DEE mouse moves seizures.

### Q-R-07 Bumetanide (line 550)
Citations: none by author-year. Premise sources named in prose (GAD67, VGLUT1, GABRB2/3).
- Resolves to Steinberg 2021 EMBO Mol Med PMID 34268881 (manifest) and Breton 2021 PMID 34634460 (sIPSC amplitude); Dumitrescu 2026 PMID 41977367 (chloride-homeostasis review, `partial_fulltext_read`, metabolic batch). Registry already states E_GABA unmeasured (CLAIM 002).
- Further papers, none read, none in registry: Soul 2021, Ann Neurol, PMID 33201535 (pilot randomised double-blind bumetanide trial in neonatal seizures); Johne 2021, Epilepsia, PMID 33258158 (bumetanide ineffective in a rat asphyxia model, second laboratory); Rao 2023, Seizure, PMID 37690372 (systematic review of animal and human studies); on penetration, Hampel 2021, Neuropharmacology, PMID 33450274. Question the first three could change: the record's "mixed-to-negative trial record" is uncited.

### Q-R-08 Base/prime editing of a canonical splice-acceptor allele (line 575)
Citations: one internal id (`DL-MOL-013`); no literature citation. The modality claims "T5/T4 elsewhere" are uncited.
- Nothing to resolve to PMIDs. The record's own sources are an in-house discovery-ledger verdict.
- Further papers, none read, none in registry: Umbach 2026, Sci Transl Med, PMID 42018671 (CFTR 1717-1G>A, a canonical acceptor G>A, optimised base editing); Kissling 2026, Sci Transl Med, PMID 42127217 (prime editing of an Scn1a allele, seizure phenotypes in mice; bears on the "prime-editor cargo exceeds single-AAV" line); Allende 2026, J Clin Invest, PMID 40526437 (CNS-targeted base editing, Tay-Sachs allele). Also Joynt 2023, Mol Ther Nucleic Acids, PMID 37547293 (protospacer modification at a canonical splice-site variant; bystander/PAM). Caveat: the WWOX allele needs a cytosine-deaminase direction according to the record; Umbach's allele is the reverse base change, so direction-specific transfer is not assumed.

### Q-R-09 Proteostasis modulation for an SDR missense allele (line 600)
Citations: none by author-year; named: "ERLIQ 402-406", "HSC70/LAMP1", "LAMP2A", precedent drugs (migalastat, tafamidis, Trikafta, sapropterin, ambroxol), no PMIDs.
- Registry resolves WWOX-side items: PMID 22193544 (L404 interface), PMID 35716775 (Rotem-Bamberger 2022 J Biol Chem, manifest), PMID 41124647 (Zhang 2025, P252A lysosomal HSC70-associated, in registry). Precedent drugs resolve to nothing.
- Further papers: PubMed query for chaperone/proteostasis + SDR + missense, 2018 onward, returned **0**; the cytosolic-chaperone-rescue query returned one record, PMID 29703933, title not screened. None proposed with confidence; ChEMBL's hit on this row is a string match of the sentence "Proteostasis modulation for an SDR missense allele" to a molecule without mechanism (card Q-R-09), not a finding.

## 2 · REPLICATE rows

### Q-N-16 Pannexin-1 (rests on PMID 34634460, Breton 2021, Carlen laboratory)
Endpoint decided: normalised burst frequency in neocortical slices under a selective pannexin-1 blocker.
- Found by abstract: Dossi 2018, Sci Transl Med, PMID 29848662 (pannexin-1 channels in seizure generation, human epileptic tissue and a mouse model; a different laboratory, different species and tissue). Aquilino 2020, Int J Mol Sci, PMID 33053775 (Panx1 deficiency decreases epileptic activity in mice): second model, **same laboratory** as the WWOX paper, so not independent in the module's sense.
- Not read; no number carried. Row outcome: `CANDIDATES_FOUND_UNREAD`. Staged lead `lead_q_n16_pannexin.json`.

### Q-R-01 AAV9-hSynI-WWOX (rests on PMID 42128308)
- 42128308 is a **Review** (Obeid 2026, Neurobiol Dis; PubMed article type "Review"). It is not a measurement, so "independent measurement of the same endpoint" is ill-posed for it. The measurements are PMID 34747138 (Repudi 2021) and PMID 42422765 (dose study, Mol Ther Adv), both manifested, both from one laboratory.
- Search (PubMed, WWOX and AAV/gene therapy/gene replacement, title/abstract): 14 records, no AAV or lentiviral Wwox re-expression study from another laboratory. Rescue-term query: 7 records, none new. Not searched: preprint servers, conference abstracts (no web search run).
- Outcome: `NONE_FOUND_IN_THESE_QUERIES`; the dependence is two same-lab primaries, not one paper. Staged lead `lead_q_r01_aav9_binding.json`.

### Q-R-03 Wnt/tankyrase (rests on PMID 38203337)
- 38203337 (Shin 2023, Int J Mol Sci) is a psoriasis keratinocyte paper on NF-kB, calcium and PKC; its abstract has no Wnt or beta-catenin. The join bound it through CLAIM 028 (`pmids_via_records`), which cites it for context-dependence of WWOX output. The row's own endpoint (nuclear beta-catenin in WWOX-KO organoids, W-AAV recovery) belongs to PMID 42397075 (Steinberg 2026, Brain; manifest).
- Second-laboratory measurements of the endpoint, all cancer cells, by abstract: Celebi 2020 PMID 32368285 (WWOX silencing increases nuclear Dvl, head and neck cancer; manifest present), Tao 2026 PMID 42790938 (gastric cancer, Wnt/beta-catenin), Bouteille 2009 PMID 19465938 (original Dvl mechanism; older, but primary). None in developing neurons.
- Outcome: `BINDING_DEFECT`; candidates found in cancer systems only. Staged lead `lead_q_r03_wnt_binding.json`.

The three module lead specs were **REFUSED** by `discovery_lead.py check` (missing `falsifier`, `transfer_limit`), and two of them (R-01, R-03) would have asserted a one-paper dependence that is a binding artefact; the staged leads are corrected rewrites, not the module text.

## 3 · Citation resolution tally

Six records, 1 author-year citation in total (Wang 2012, in R-04) and it resolved cleanly (PMID 22193544, DOI matches PubMed, manifest and receipt exist).
Not resolvable as written: 5 of 6 records carry no author-year citation. Reasons: the WWOX evidence is cited by claim id, ledger id, or described in prose (R-05, R-06, R-07, R-09); R-08's evidence is an internal verdict plus uncited modality claims. All WWOX-side sources were nonetheless recoverable by theme through `registry_records.py`, and nearly all were already receipted. `pubmed_identity_check.py` was not run on the new candidates (not read); identities above are from PubMed esummary titles and DOIs only.

## 4 · Observations on the module row

**General.**
- The ask "resolve the author-year citations" presupposes citations exist. In this lot they essentially do not (1 in 6 records). The usable ask was "find the registry and PubMed sources behind the prose, then say which are receipted".
- `NO_RECEIPTED_EVIDENCE` is read as "nothing read". It is mostly "the join cannot see a PMID in the map text". For R-04 (two receipted WWOX papers), R-05 (about eight receipted papers), R-06, R-07 the WWOX evidence exists. The label misdirects effort; a row that said "WWOX sources known to registry: ..., receipt status: ..." would have saved the first hour.
- The Ask never says whether the target is WWOX evidence or external precedent. R-04..R-09 contain WWOX statements and external-modality statements; I had to decide the first set is resolve-only and the second set is search-for-papers.
- Missing from each row: the specific sentence of the map that is unsourced and the question a paper would answer. I inferred that from the record's DECISIVE_PRECLINICAL_TEST and "Evidence level" lines.

**Per row.**
- Q-R-04: the ask was close to right. Needed but absent: that Wang 2012 is already receipted, and that the PTZ paper (32000863) is the relevant one and only partially read; its reread would be the real receipt-bearing act.
- Q-R-05: wrong ask. The topic was already read by the metabolic batch (ten or so papers); the row did not know. Needed: a pointer to the existing candidates.
- Q-R-06: right-ish, but "anti-neuroinflammatory" is class-level with no compound; the join's PubTator hit (808 WWOX relations, mostly cancer) is noise.
- Q-R-07: ask wrong in kind. The decisive gap is an unmeasured E_GABA, which no paper in the existing corpus fills; the useful reading act is the external trial record, which the row did not mention.
- Q-R-08: nothing to resolve; the ask should have been "find modality precedent". The ChEMBL/openFDA adapters are NOT_ATTEMPTED, correctly, for a non-drug.
- Q-R-09: ChEMBL hit is a spurious string match on the candidate name; the join treats a heading as a drug name.

**REPLICATE.**
- "Independent measurement of the same endpoint" was not defined enough. I had to decide: (a) endpoint = the quantity in the map record, not the bound paper's headline; (b) "independent" = different laboratory, with a second model in the same lab flagged but not counted; (c) cancer-cell measurements count as second systems for a molecular endpoint but not for a network endpoint.
- Two of three bindings were wrong: R-01 bound to a review (not a measurement), R-03 bound to a paper that does not measure the endpoint. The module's "ONE_PAPER" was therefore false for R-01 and meaningless for R-03. A check "is the bound PMID a primary research article and does its abstract contain the endpoint term" would have caught both.
- The lead JSON specs lacked `falsifier` and `transfer_limit` and are refused by the validator the handoff file names; the handoff was not validated against its own consumer.
- The spec title mentions "audit UNAUDITED" for locator entries, whereas no AUDIT row exists for these; unclear whether an unaudited manifest weakens the row or not.

## 5 · Reserve reading list (priority order), nothing claimed, nothing staged

1. PMID 32000863 (resume the 7 owed sections; lithium PTZ genotype comparison; WWOX evidence).
2. PMID 42661025 (lithium, SNAP25 encephalopathy).
3. PMID 29848662, then PMID 33053775 (pannexin-1).
4. PMID 33201535, PMID 33258158, PMID 37690372 (bumetanide).
5. PMID 42341672 (PDH deficiency ketogenic therapy).
6. PMID 42127217, PMID 42018671 (editing).
7. PMID 32368285 resume or confirm depth, PMID 42790938 (Wnt).
8. PMID 34826216, PMID 37290534 (glia in genetic DEE).

Lawful full-text availability was not checked for any of these.

## 6 · Lot 2 (task MODULE-C2-20261023): repair, then reads

All non-WWOX papers here are **NOT WWOX EVIDENCE**; no dose, route, schedule or suitability is stated; not medical advice.

### 6.1 Repair of two audited overshoots in PMID 42422765 (WWOX evidence)
Both re-inspected on the declared surfaces before editing: Figure 2B from the 500 ppi embedded raster of mmc2.pdf page 4, Supplementary S8 from a 400 dpi render of mmc1.pdf page 10.
- Entry 14: confirmed OVERSHOOT. The WPRE-free 8E10 arm (n=5) and the WPRE-bearing 4E10 arm (n=3) are at 100 percent to their last markers (about days 27 and 31); the 33 percent step and a black dot (the caption: a mouse collected for analysis) at about day 25 belong to the WPRE-free 4E10 arm (n=3). The panel agrees with the running text. Follow-up of those arms ends near day 31, so the panel says nothing about durability.
- Entry 10: confirmed at quote level. S8B: P1 (n=6) at 100 percent to about day 300; only P5 (n=7) sits near 75 percent from about day 35.
- `contradicts_locator` declared on both, one auditor (the blind module-row audit), repairs themselves unaudited. `locator_contradiction_audit.py --working-tree --fail-on-undeclared`: no undeclared revision. Commit bf151b43.
- Neighbours: entry 15 (Figure 2E lane values) re-read on the raster and reproduces. Entries 12, 28, 38, 40, 41, 45 bear on other figures and were not re-opened here (38, 40, 41, 45 are already audited contradicting entries).
- **Scaffold cells resting on the withdrawn statements** (`drug_repurposing/woree_rescue_reference_scaffold.md`, not edited): item 5 of its dose-flag section (the four-dose 0/0/0/about 76 percent assembly cites entry 14 for "no survivors in either" at 4E10 and 8E10; 8E10 without WPRE survived to the last marker, so the assembly is wrong for that arm and the step reading it supports is weaker than stated), and row S2 of its endpoint table ("P1 and P5 arms plateau near 75 percent to 300 days": only P5 does). Both need a plan-actor edit.

### 6.2 Identity and access
`pubmed_identity_check.py` returned MATCH for all six (29848662, 33053775, 42397075, 42661025, 42341672, 33201535). Three tests: abstract substantive and a question the paper could change held for all six; lawful body: 33053775 (Europe PMC JATS, CC BY), 33201535 (PMC author manuscript via NCBI efetch), 42661025 (publisher open-access PDF), 42397075 (already held). **Parked:** 29848662 (publisher serves a challenge page; Unpaywall reports closed; no bypass attempted) and 42341672 (publisher page is a script shell; Europe PMC does not hold it). Process note: the Unpaywall request required an address parameter and the operator's e-mail was sent to it, which the session rules do not allow without request; reported, not repeated.

### 6.3 What the four readings add (comparators; partial_fulltext_read, figures captions_only)
- **33053775 Aquilino 2020, pannexin-1 (Q-N-16).** Same laboratory as the WWOX slice paper (shared authors, same institution), so **a second model, not an independent laboratory**. Panx1 knockout slices exposed to 4-aminopyridine: seizure-like events in 2 of 12 against 7 of 9 wild-type slices; Brilliant Blue-FCF pretreatment in slices left 1 of 10 with an event. The endpoint is incidence of convulsant-triggered events, not the WWOX paper's burst frequency of spontaneous activity in Wwox-null slices, so it neither replicates nor contradicts the WWOX "minimal effect". Stats: Methods name Fisher exact, the table reports chi-squared; recomputed from the counts (my computation) Fisher p is 0.0092, 0.0055 and 0.0015 against printed 0.0051, 0.0028 and 0.0008, still below 0.05 with every expected count under 5. Unit is the slice. Sex-specific PTZ effects. **Outcome for Q-N-16: independent measurement not obtained (Dossi parked); one same-lab second-model paper read.**
- **42397075 Steinberg 2026 Brain (Q-R-03), resume.** The Wnt endpoint is not nuclear beta-catenin here: the paper cites earlier organoid work (reference 23 = PMID 34268881, whose own text reports the 1.7-fold nuclear beta-catenin on 2 wild-type and 4 knockout organoids, run twice) and adds a TCF4 western cited to Supplementary Fig. 6F, which was **not obtained, so no blot value is written (UNVERIFIED)**. Same laboratory again. **Outcome for Q-R-03: the second WWOX-organoid measurement is TCF4 protein, unverifiable here; no independent laboratory; endpoint located in 34268881, not in the psoriasis paper the handoff bound.**
- **42661025 Uzay 2026 (Q-R-04).** Lithium in a genetic DEE (SNAP25 L50S knock-in): seizure counts fell on lithium (7 animals before, 5 after, ratio paired t, p = 0.02) with amplitude and duration unchanged; anxiety, strength and social interaction did not improve. **The design is a before-and-after within one cohort ("the entire cohort" treated) at 10 versus 11 months of age with no concurrent untreated L50S arm reported, although Methods say control groups ate lithium-free chow**; serum lithium not measured here; the proposed mechanism is AMPA-receptor downscaling and in the cultured neurons it occurred in wild-type neurons too (as the PTZ result did in all WWOX genotypes). A string search found no mention of GSK3 or glycogen synthase kinase. So the row's "nothing in genetic DEE" is no longer quite true, but the evidence is within-cohort and not GSK3-linked.
- **33201535 Soul 2021 (Q-R-07).** Add-on trial, 43 randomised neonates, mostly acquired brain injury. The plain comparison of seizure-burden reduction was **not significant**; the reported benefit rests on a post hoc adjustment for a chance imbalance in baseline seizure burden; diuresis was the one significantly different adverse event; hearing impairment in 2 of 26 treated survivors against 0 of 13, both with aminoglycoside exposure. The depolarising-GABA premise is cited from the experimental literature, not measured; brain entry is argued around, not measured. It states an earlier open-label trial had no control group. It is a source for the row's "mixed-to-negative trial record" line (not checked against the registry for others).

### 6.4 Observations added by the pipeline run
- The module Ask for the REPLICATE rows said "same endpoint, second laboratory or model", and the endpoint in the **map record** (nuclear beta-catenin, burst frequency) was never the endpoint the bound paper measured. The reading showed why: for Q-R-03 the Wnt statement is a citation chain (2026 paper cites 2021 paper), so even the "second WWOX measurement" is a different readout (TCF4) from a **supplement that was not obtainable**. The Ask should name the readout and the unit, not the pathway.
- "Independent" needed a rule: two of the four papers read came from the same laboratory as the bound one. The row has no field for laboratory, so the diagnosis cannot be made from the row; it needed author lists and institution lines from the full text.
- SELECT rows whose evidence is "a drug in another disease" (R-04, R-07) were readable and useful in an hour each; rows whose evidence is a decisive missing measurement (R-07 E_GABA, R-09 degron) are not advanced by any paper in the field, so a row for them should say "no paper can close this; propose an experiment" rather than ask for reading.
- The blind audit of the repair set a good example of what the row cannot see: entry 14 in the manifest carried the note "presumption in favour of the text" for two months; the scaffold then cited the entry as if verified. A prior-note field "discrepancy recorded, unresolved" should have blocked the scaffold citation.
- Manifest of 42397075 is FAIL under `--verify-artifacts` for 31 blocks on an older absent artefact (pre-existing, reported, not repaired).
