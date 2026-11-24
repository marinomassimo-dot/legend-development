# ADV-215 result: PubMed delta intake (IT, 2026-11-24)

Actor `orchestrator` (IT successor, session 7cf5e85a), task ORCH-ROADMAP-IT59-20261119. Assignment: ADV-215 (PubMed delta intake of the PMIDs in no file under `disease-models/wwox`). Table: `TRIAGE_ADV215_IT_20261124.tsv` in this folder (47 rows, 14 columns: ADV's 40 plus the 7 records ADV's scan counted as present). Nothing here is medical advice; reference genotype class only. Sources: PubMed (E-utilities count, the PubMed tool for metadata and abstracts), Europe PMC open-access flags and PMC free full text; no e-mail sent to any service, no paid route, no outside contact.

## 1. Answer in five lines
1. **ADV's list holds 40 PMIDs, not 39.** **37 are the plant gene WOX1** (WUSCHEL-related homeobox: Arabidopsis, Medicago, cucumber, soybean and similar), a false hit of the term `WOX1[Title/Abstract]`, not WWOX. The other three: one WWOX hit (a jellyfish lncRNA study that lists the gene Wwox) and two human `WOX1` = WWOX mentions (an imaging method that uses an EGFP-WOX1 construct as a label; a prostate-cancer study that reads WOX1 activation as an apoptosis marker). Those two are cited in the reference lists of three held WWOX full texts (Lee 2010, Hong 2009, Hsu 2009) but never registered.
2. **With the WWOX-only term the true miss is small.** `WWOX OR "WW domain-containing oxidoreductase"` (title or abstract) returns **708** records today (esearch, 2026-11-24). **700** carry their PMID in a registry-class file (the corpus seeds, the paper registry, the literature log or the receipt ledger), **1 more is registered under its DOI** (see point 3), and **7 are never registered: 6 are named only in research notes (so ADV's scan counted them as present) and 1 appears nowhere** (the jellyfish study).
3. **False 'absent' (held by the repository, missed by the scan): 1.** PMID 42818975 (Research Square preprint, FASD GWAS) is registered as LIT-0538 under its DOI and preprint id PPR1316475 (receipt `FTR-20261004-PPR1316475-01`, partial full text, dossier held) because **no PMID existed on 2026-10-04**; PubMed now carries one. It is a metadata upgrade, not a new paper. The dossier had already found the Discussion-versus-Table 3 conflict on placental WWOX direction that I met again independently. A PMID-only scan cannot see this class: a DOI and title pass is needed (done here for all 47: no other hit).
4. **Records to register: 9** (the 7 never-registered WWOX records plus the 2 human WOX1 mentions), as CORPUS stubs, no claim and no grade; plus one identifier line on LIT-0538. 42721537 (Argentine WOREE case series) is already full-text queue item FT-110 with an abstract-only receipt: not a miss.
5. **Standing query defect, for ADV-217:** `WOX1[Title/Abstract]` adds 40 records to the 708, of which 37 are plant WOX1; a delta tool on the 748 term will list plant papers as misses every time. Use `WWOX[tiab] OR "WW domain-containing oxidoreductase"[tiab]` as the standing term, keep `WOX1` as a separate human-only probe (exclude plant contexts), and make the tool compare **DOI and title as well as PMID** so a preprint registered before its PMID is not reported.

## 2. Counts
| Quantity | Value |
|---|---:|
| ADV's list (unique PMIDs) | 40 |
| plant WOX1 (off target) | 37 |
| human WOX1 mentions (EGFP-WOX1 label; WOX1 apoptosis readout) | 2 |
| WWOX gene listed (jellyfish) | 1 |
| PubMed count, original term (WWOX, WOX1, WW domain-containing oxidoreductase) | 748 |
| PubMed count, WWOX-only term | 708 |
| WWOX-only records with the PMID in a registry-class file | 700 |
| WWOX-only records registered by DOI only (false 'absent') | 1 (42818975) |
| WWOX-only records never registered | 7 (6 named only in research notes, 1 nowhere) |
| In pipeline, not a miss | 1 (42721537, FT-110) |
| Records proposed as CORPUS stubs | 9 |
| True misses versus false 'absent', over the 47 PMIDs of the table | 37 off target, 9 true misses, 1 false 'absent' |

Method of the counts: tokens of seven or eight digits extracted once from every tracked file (`git grep`), and separately from the four registry-class files; PMID, then DOI and a 70-character title prefix against the registries and the full-text queue for all 47; a single-pass fixed-string search of the untracked `files/` tree (only three older held papers hit, all of them reference lists naming the two human WOX1 records; no dedicated file exists for any of the 47). Retraction check on the 11 non-plant candidates: 0 flagged. `study_dedup_triage.py` on the same 11: 10 NEW and 1 IN_PIPELINE.

## 3. Triage, top rows (full table in the TSV)
The script classes (`batch_inferential_sweep.py` with the proband matrix) are keyword artefacts on abstracts and are kept as separate columns; the class and priority below are my reading of the abstract or of the free full text and override them (the script ranks the prostate HYAL1 paper P1_HIGH and the jellyfish paper CANONICAL_CANDIDATE; neither has a WWOX result).

| Pri | PMID | Year, journal | Scope | My class | Route |
|---:|---|---|---|---|---|
| 1 | 43036373 | 2026, Epilepsy Curr | Commentary on the human cerebral organoid study of WWOX loss (radial glia, MYC, WOREE and SCAR12 lines, AAV restoration) | secondary source on a held primary | PMC13769701, free, read in full |
| 2 | 42991897 | 2026, Front Genet | gnomAD v4.1.1 East Asian versus non-Finnish European frequencies of ClinVar P/LP variants in 199 epilepsy genes; four WWOX alleles among the enriched | variant population frequency | PMC13739471, free, WWOX contexts read |
| 3 | 31829254 | 2019, Mol Brain | WWOX marks a medial VTA subpopulation of TH+/VGLUT2+ neurons (mouse) | discovery only (expression map) | PMC6907252, free, WWOX contexts read |
| 4 | 42790938 | 2026, Ann Clin Lab Sci | WWOX overexpression or knockdown in gastric cancer cells and xenografts moves beta-catenin and EMT | translational bridge, abstract only | Europe PMC: not open access, not in PMC (route result) |
| 5 | 43048821 | 2026, Curr Neurovasc Res | Mendelian randomisation, programmed-cell-death genes and cognition; WWOX among three prioritised genes | discovery only, abstract only | Europe PMC: not open access (route result) |
| 6 to 9 | 42635858, 43004178, 19365417, 16140946 | various | WWOX as a listed gene, a pig GWAS candidate, a label, an apoptosis readout | background (lower), recoverable | abstract level |
| - | 42818975 | 2026, Res Sq | known preprint, PMID now assigned | KNOWN_METADATA_UPGRADE | dossier held |

## 4. The top five, and the open row each could change
**None of the five narrows an OPEN question row.** What each says:

1. **43036373 (commentary).** Restates the held Brain 2026 study (PAPER 094; PMID 42397075, read completely). It adds no measurement. It matters for one guard: it states that all WWOX-deficient organoids were hyperexcitable "with more severe abnormalities in WOREE organoids compared to SCAR12", while RP-043 carries the WOREE-over-SCAR12 week-16 contrast as **pooled-only** after ADV-140. That sentence is a review-level compression of the primary and **must not be imported over the held quantified reading** (the INV-06 and INV-01 guard of checkpoint 12). Its open questions (a developmental window beyond which gene replacement fails; knockout versus residual function in patient lines) restate what RP-043 already waits on. Consumer: RP-043 (a pointer; no edit proposed).
2. **42991897 (gnomAD).** WWOX start-loss c.2T>C: 4 of 40,686 East Asian alleles versus 3 of 1,149,400 non-Finnish European (odds ratio 36.3, one-star ClinVar entry); exploratory, low counts: p.Glu171Ter (2 of 44,864; none in NFE), c.172+1G>C (2 of 44,874; none in NFE), p.Arg54Ter (3 of 44,870 against 5 of 1,179,600; its East Asian count does not exceed the NFE count and the paper itself calls it East and South Asian enriched). These are reference-population counts for known recessive alleles with a small East Asian denominator; they carry no disease-model premise. Consumer: variant-spectrum and carrier-frequency context; no row.
3. **31829254 (VTA).** More than 70 percent of WWOX-positive VTA neurons co-express TH and VGLUT2, enriched medially (WWOX+ 197.31 +/- 16.10 cells/mm2 medial versus 70.21 +/- 6.08 lateral; 6 mice, 22 slices). A wild-type mouse expression map only; no WWOX-deficient measurement. RP-019 (circuit and cell context, parked) resumes on PV-specific evidence, which this is not. No row.
4. **42790938 (gastric cancer).** Abstract only: WWOX overexpression lowers beta-catenin (total, nuclear, cytoplasmic) and EMT markers, knockdown does the reverse, and the agonist SKL2001 and the inhibitor XAV939 reverse each effect. Cancer cell lines and nude-mouse xenografts, not a WWOX-deficient neural system (transferability class T3). Context for the Wnt strand (RP-026 done, RP-038 parked); no row.
5. **43048821 (Mendelian randomisation).** Abstract only: genetically predicted higher WWOX expression, and a methylation change in WWOX that goes with higher expression, track with better cognitive function; population-level, not a WWOX-deficient system. Direction-of-effect context only; no row.

## 5. Reading depth and honesty
* **No receipt was written and nothing here adds reading depth.** The three free PMC texts were retrieved and the WWOX contexts read (the commentary in full, the other two by the sentences and table rows that name WWOX); none was saved as a source artefact, so a receipt would claim a source the ledger cannot fingerprint. The CORPUS stubs therefore say "triaged at abstract level; full text retrieved, targeted contexts read, no receipt".
* Full text outside PMC was not attempted for the paywalled items (Europe PMC flags 42721537, 42790938, 43048821 and 42635858 as not open access and not in PMC): route results, nothing bypassed.
* The sweep script ran on the 11 non-plant candidates; the 37 plant records were classed from title and abstract (a plant context in all 37, and WOX1 never preceded by WWOX or WW domain).
* One unchecked corner: the six notes-only records were not searched for a dossier under another name; the check was PMID, DOI and a title prefix against the registries and the full-text queue.

## 6. Follow-up
* **Commit candidate:** `research/commit_candidates/CC-20261124-ORCHESTRATOR-ADV215-CORPUS-STUBS-01.md` proposes nine CORPUS stubs and the PMID line on LIT-0538, for the next `BATCH_COMMIT`. The 37 plant PMIDs are not registered; the TSV marks them OFF_TARGET_PLANT_WOX1 so the delta tool (ADV-217) can exclude them.
* **To ADV-216:** nothing for SCI from this intake; no top-five record narrows an OPEN row.
* **42721537** stays FT-110 (abstract-only receipt `FTR-20261106-42721537-21`; paywalled, not in PMC).
