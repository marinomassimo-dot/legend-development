# ADV-222 pre-registration: a reading batch of eight owed-and-held data sections whose product is new open questions (SCI, 2026-11-24)

Hypothesis level; reference genotype class; nothing here is medical advice. Written BEFORE any of the eight sections was opened. Assignment ADV-222 (ADV message 2026-11-24, brief adv222.txt). About 120 minutes in two increments, no spend, no download, no outside contact, no e-mail address to any service. Checkpoint AC, RP-045, the sealed ADV-174/175 material untouched; no registry or ledger edit by hand (proposed edits only, as a list for IT's batch route). Receipts only by `fulltext_receipts.py record`.

## 1. What I had seen before freezing (honest list)
* The ADV-219 result and its list `class_b_data_bearing_held_best_state_adv219.tsv` (100 flags, 92 studies: study key, section, latest-receipt label, held file name); the titles of the held files (first lines of the PDFs, `article-title` of the XML) and the portfolio rows (research_portfolio.tsv, theme and opportunity text); whether a registry record exists for each paper (catalog identifier match).
* NOT seen: any section of the eight papers beyond the title; the registry or dossier statement about any of them; the earlier receipts' verbatim locators.

## 2. Selection rule (frozen) and the eight sections
Rule: from the best-state data-bearing class B list, keep sections whose paper (a) belongs to a strand of the portfolio that points at a drug-repurposing or registry decision (RP-016 antiseizure comparisons, RP-018 integrated stress response, RP-030 vigabatrin / GABA transaminase, RP-033 energy supply and glial state after onset, RP-040 gene-addition benchmark, RP-015/WWOX-specific registry claims), or (b) carries a registry statement (a PAPER or CORPUS record). Not by OPEN-row link. At most two sections per paper, none of the ADV-216 records (PAPER 495, 157, 447). Strand diversity: at most two sections per strand. Within a strand the section chosen is the one with more numbers in it by its name (tables over results over figures) when both qualify; otherwise the first by study key. Records with a registry statement are preferred inside a strand.

| # | Study | Section | Held file | Strand | Registry record |
|---|---|---|---|---|---|
| S1 | OMA1-mediated ISR in a spastic-ataxia type 5 model (PMID 37804316) | tables | PMC10907083 europepmc XML | RP-018 ISR | CORPUS-STUB-190 |
| S2 | Translational control by ribosome pausing during amino-acid limitation (PMID 30029003) | tables | PMC6516488 XML | RP-018 ISR | none |
| S3 | Clobazam with stiripentol, phase 2 drug-drug interaction trial (PMID 32652616) | results | 32652616.xml | RP-016 antiseizure | none |
| S4 | GABA transaminase ABAT and mitochondrial nucleoside metabolism (PMID 25738457) | tables | abat.xml | RP-030 vigabatrin / ABAT | none |
| S5 | Long-term safety of dichloroacetate in congenital lactic acidosis (PMID 23611579) | tables | Abdelmalak2013 PMC XML | RP-033 energy supply | PAPER 557 |
| S6 | NAD-brain pharmacokinetics of oral NAD precursors (PMID 41858901) | tables | human_time.xml | RP-033 energy supply | none |
| S7 | CSNK2B gene replacement rescues phenotypes, EEG biomarkers (PMID 42190665) | results | PMC13293933 europepmc XML | RP-040 gene addition | CORPUS-STUB-193 |
| S8 | WWOX, DNA damage and somatic instability in Huntington's disease (PMID 42395553) | figures | Petrozziello2026 bioRxiv PDF | WWOX-specific | PAPER 532 |

Rejected neighbours (named): the other two lamotrigine/CBD-clobazam table papers (RP-016 limited to one), the Shank3 restoration paper (RP-040 limited to one), ketogenic-diet review and the Dravet review (reviews, no primary data section), WWOX glioblastoma and fragile-site records (WWOX-specific limited to one; chosen the one with figures and a supplement).

## 3. Predictions fixed before reading (each with a rejecting observation)
* P1: for at least 5 of the 8 sections, the section reports at least one number or panel that the repository statement about the paper (registry record where it exists, otherwise the earlier receipt or manifest that cites it) does not carry. Rejected if fewer than 5 qualify.
* P2: at most 4 of the 8 sections yield a NEW open question that a held source can answer (the remaining sections yield a narrowed row, a stated "unchanged", or a question that needs new data). Rejected if 5 or more yield a held-answerable question.
* P3: no section contradicts a registry statement. Rejected if one does (statement and quote named, no edit).
* P4: the two papers with a registry statement of their own (S5, S7) show a gap between the statement and the table or results section, in the direction that the statement is shorter than the data. Rejected if both statements already carry the headline numbers of the section.

## 4. Method and reporting rules
* Route per section: the held file only; the section read completely (tables, table footnotes, figure panels, the supplementary table inside the PDF where one exists); for S8 figure panels are read from the rendered pages of the held PDF, hand readings labelled READ-OFF with resolution, text values labelled TEXT. A failure to render is a stated limit, not a skipped record.
* Baseline: before opening the section, read the repository statement about the paper (registry record via `registry_records.py get`, else a grep of the research folders by identifier) and note its content in the result; then read the section.
* Per section the result gives: (a) what it reports that the baseline does not carry; (b) one of: NEW open question (a question and the observation that would answer it), narrowed row, contradiction (statement and quote, no edit), unchanged; (c) counter-check: what could the earlier, narrower read NOT have seen; (d) whether a held source could answer a new question (yes: which file; no: what would be needed).
* Receipt per paper by `fulltext_receipts.py record --dry-run` first; coverage states from the closed vocabulary; the section read becomes `read` only if I read all of it; verbatim locators from the text; `analysis_at` before `event_at`. After recording: `reading_state.py`, `coverage_report.py` (with the dirty-input reason) and `ranking_it8.py run`, committed together.
* Ranking of the new questions: (1) answerable now from a held source, (2) answerable from a source that is catalogued but not held, (3) needs new data; within a class, by distance to a portfolio decision.
* Count discipline: the mandate status line read before any count is written. Increments: 1 = S1 to S4; 2 = S5 to S8, the result, the landing.
