Independent verification, IT7 package P0a (census reconciliation, `census_reconciliation_it7_20261029.md`, commit 6fdf4942), 2026-10-29

Verifier is not the producer. Non-canonical, not medical advice. Method: public endpoints and papers reopened today (about 15:00 to 15:40 UTC) by API calls and downloads into new empty directories; no registration, no contact address, no e-mail, no spend, no access-control bypass (a 403, 401 or 404 was recorded as such and not retried by another route). Registry statements were looked up with `registry_records.py`, never by grep of the two large registries. The reference genotype class is not named by allele.

Overall: the central conclusion (no deposited, downloadable record adequate for the protein, phospho, flux or recovery questions in a genetically WWOX-deficient neural system) is SUPPORTED, and every accessibility and deposit fact I re-tested reproduces. The narrowing keeps "not found by this search" apart from "shown absent". There is no HIGH defect. Five MEDIUM and five LOW defects: one wording overstatement that the producer then propagated into four places (phospho-PERK), one missing control in the add-back adequacy call, one missed unqualified absence sentence, an incomplete "non-neural records exist" list, and one scope ambiguity in the README row. No canonical file was edited.

## 1. Rows re-checked against the source (14 rows, 17 facts)

| Row or statement | What I re-checked | Result |
|---|---|---|
| 1, E-MTAB-14792 | BioStudies API study and `/info`; FTP path | 403 "Study not accessible" (both), FTP 404. Reproduced |
| 1, E-MTAB-14792 content | Preprint v2 (local copy) methods, "5 libraries", WT 6,792 / WWOX-KO 4,124 / SCAR12 4,454 / WOREE 7,687 / WOREE-WWOX 5,151, 28,208 total, 26,352 kept | Reproduced. Whether the add-back library is deposited stays UNVERIFIED (correctly so) |
| 1, Brain 2026 text | Data statement names E-MTAB-14792; AAV9 at week 10, "followed by 6 weeks of culture"; Fig 6C-E compares neurons of AAV9-WWOX-treated WOREE organoids "versus non-treated" | Reproduced. See M2 for what the comparator implies |
| 3, PMID 42422765 | Europe PMC JATS: "Data and code availability Not relevant." and Data Availability Statement "Not relevant." | Reproduced |
| 4, PMID 34747138 | JATS: "This study includes no data deposited in external repositories." | Reproduced |
| 5, E-MTAB-14948 / -14949 | API | 200, release 2025-04-18 for both, titles as stated. Reproduced |
| 5, PXD071676 | PRIDE project API | 404 "not in the database". Reproduced |
| 5, MTBLS12344 | web service; public FTP folder | 401 "User has no permission" and 404. Reproduced |
| 2, GSE156243 | GEO text record | Public since 2021-07-01, 6 samples (2 untreated, 4 KO), three supplementary files (count table, 1,246 up, 1,021 down). No add-back sample. Reproduced |
| 12, GSE158681 | GEO text record | Series exists; the status line reads "Public on Oct 01 2026" (the producer says only "public"; see L5). GEO series carry no PubMed link. Reproduced |
| 11, PMID 38563965 | figshare API; PDF download | Files: Supplemental Table S1 PDF 149,536 bytes (sha256 `774aa45d...25c`, equal to the producer's), figures PDF 76,348 bytes; CC BY 4.0; published 2024-02-02. Table has 2,051 numbered rows. Data statement "Data will be made available upon reasonable request"; no PRIDE or ProteomeXchange term in the paper. Reproduced |
| 11, table content | text layer of the PDF | ATF4, DDIT3, EIF2AK3, EIF2AK4, CHAC1, TRIB3, SESN2, PDK1, MYC, HIF1A, ASNS, PPP1R15A: 0 rows. EIF2S1, PDHA1, LDHA, HSPA5, SOD2, ZYX: one row each. "WWOX" appears only in the column header, not as a protein row. Reproduced. The table also has 20 rows named Decoy (see L3) |
| 6, PMID 28749468 | JATS Methods | PEO1 "homozygously deleted for WWOX exons 4-8 and lacks WWOX protein"; stable WWOX-7/-8 against Vector-9/-p2; phospho-eIF2A antibody (CST 9721); GRP78 and eIF2A phosphorylation induced by paclitaxel or tunicamycin (Fig 4a). Reproduced, with the PERK correction in M1 |
| 7, PMID 25012504 | Europe PMC abstract | "enhanced glycolysis and diminished mitochondrial respiration", increased glucose uptake. Reproduced at abstract level (the producer says the same) |
| 2, PMID 34268881 | local JATS | Data statement lists only "RNA-seq data for week 15 cerebral organoids ... GSE156243"; Western week 24 WT n=2, KO n=4, one batch; lentivirus given at day 35 (Methods) and described as "week 6" in the Fig 2 legend; see L1 |
| GEO and PRIDE counts | GEO DataSets `WWOX[All Fields] AND gse` | 39 series (reproduced). `Wwox[All Fields]` also 39. A wider alias query (WOREE, SCAR12, FRA16D, WOX1) gives 44, none a new neural WWOX perturbation. PRIDE keyword WWOX: PXD024909 only (OpenCell). Reproduced |

## 2. Defects, ranked

### MEDIUM

**M1. "phospho-PERK" overstates what the ovarian paper shows (PMID 28749468).** The paper uses a *total* PERK antibody (Cell Signaling 3192; Methods and Fig 5 legend), and the Results describe "induction or increase of phosphorylation" of PERK without a phospho-PERK antibody. The only phospho-specific antibodies are phospho-eIF2A, phospho-JNK and phospho-IRE-1. The reconciliation (row 6, C1, C18), the census (item 1, table (b)), the README row, and the proposed replacement texts for the discovery and therapeutic ledgers all write "phospho-PERK blots". The honest wording is "a PERK band shift read by the authors as phosphorylation (total-PERK antibody)". Because this feeds the proposed canonical-batch wording, it should be fixed before it is carried to the orchestrator.

**M2. The add-back adequacy call omits that the single-cell comparator is untreated, not vector-treated (PMID 42397075, row 1, level d).** The text compares AAV9-WWOX-treated WOREE neurons "versus non-treated", and the five libraries contain no AAV9-EGFP library (the AAV9-EGFP arm exists only in the functional assays). The producer's own adequacy criterion (iv) is "controls match"; the R: PARTIAL call lists one library per arm, one time point and the locked deposit, but not that the transcript-level recovery contrast has no vector control. This belongs in row 1 (d), in census row 5 and in the proposed P1 qualifier.

**M3. A missed global absence sentence: `rescue_window_it6_20261029.md`, conditional/inducible row ("all conditional alleles in the corpus are constitutive-from-development Cre lines (Nestin, Synapsin, GFAP, Olig2, Alb, BK5, Cd19, Osterix)").** The sentence has no neural qualifier and is false as written: PMID 38563965 (in the corpus, PAPER 113) uses a tamoxifen-inducible Cdh5-CreERT2 Wwox deletion (Methods, confirmed in the local HTML). The producer audited the neighbouring sentence (P2, "no inducible neural deletion or restoration is known") and saw the Cdh5-CreERT2 line, but not this one. The sentence needs "neural" and "found", or the endothelial inducible allele added to the list.

**M4. The "non-neural records exist ... are listed" sentence is not a complete list, and the flux search shares the vocabulary limit the producer found for eIF2.** The census item 1 and the README say non-neural records "are listed". A title/abstract query for WWOX with metabolic terms (oxygen consumption, glycolysis, lactate, ATP, mitochondrial, pyruvate, NADH) returns 39 records; the producer's query with Seahorse/OCR/ECAR terms returned 3. Records it did not list: PMID 30755385 (Wwox ablated in mouse skeletal muscle; fewer mitochondria, lower mitochondrial activity and glucose oxidation, impaired AMPK activation), PMID 21075834 with GSE22689 (Drosophila Wwox proteomic and microarray interactors, ROS), and PMID 31543760, a **neural** record: WWOX-silenced human neural progenitors with "lowered mitochondrial redox potential" (the paper behind GSE126075, whose census row 13 says "mRNA" only). The KEEP on C19 (OCR/ECAR, lactate, PDH, NAD(H) in a neural system) still holds, since a redox-dye readout is not one of those assays, but C19 should carry the same "vocabulary-limited" caveat as C18 and the neural redox-potential record should be cited as the nearest neural metabolic readout (the 2021 organoid paper itself cites it). "Listed" should read "examples".

**M5. README row P3 contains a self-contradicting scope.** After the sentence listing non-neural ovarian phospho blots, the row says "Add-back records exist at functional and transcript level ..., none with a protein, phospho or flux readout". Taken literally it is false (the ovarian add-back has phospho blots; the organoid papers have WWOX and cell-marker immunostaining; the mouse papers have WWOX protein). The intended meaning is "none with a protein, phospho or flux readout of the ISR or metabolic pathways in a neural system" (the wording the census itself uses in (d)). Same sentence appears in the proposed ledger text in section 5.3.

### LOW

**L1. Row 2 (b), "Add-back arms are measured only by IF and qPCR", omits the lentivirus MEA recording.** The Fig 2F,G legend reports the spectral power of two KO lines infected with lenti-WWOX at week 7 ("recovery of the KO line"). The row's level (d) R call is nonetheless reasoned correctly (arm precedes the earliest recording). The source also gives two different treatment times for the lentivirus (Methods day 35; Fig 2 legend "week 6"); neither the row nor P7 notes the discrepancy.

**L2. Verdict P1 (KEEP) leaves an unqualified "only" in three places.** "The only post-onset add-back" and "the only genetic add-back after a documented phenotype" stay in `rescue_window_it6_20261029.md`, README row P7 and `needs/needs.json` (NEED line on gene addition). The producer proposed the qualifier (one library per arm, deposit locked) as a "P7 owner" edit, but did not apply it to the README row it did edit, and neither "found by this search" nor the missing vector control (M2) is attached. KEEP is defensible for the fact; the sentence should still be bounded.

**L3. The 2,051 / decoy discrepancy is resolvable from the public table and is left UNVERIFIED.** The table has 20 rows named Decoy (rows 423 onward, `...-DECOY` accessions), so 2,031 non-decoy proteins; the paper's "2,051 distinct proteins" counts decoys. The new C17 text and census row use "2,051 proteins". "Run in triplicate" (technical or biological) rightly stays UNVERIFIED.

**L4. C18 is labelled NARROW although the producer's own reason is that the clause "stands".** The change made is a vocabulary caveat, i.e. a KEEP-with-note. Tally would read 13 KEEP, 6 NARROW, 8 CORRECT. Cosmetic, but the 12/7/8 figure is quoted in the README row.

**L5. GSE158681 status is not recorded as dated.** The GEO record states "Public on Oct 01 2026". The census row says "public"; the date matters because the P4 deposit was said to be usable on the date P4 ran, and the record's last update is the same day.

## 3. NARROW and KEEP verdicts

NARROW (7): C1, C2, C8, C18, C22, C23, C26 are all right in direction: each names the routes actually run and ends with "not found by this search". C22 is correct to downgrade a count to UNVERIFIED because the 960 hits were never screened. C23 is the most useful: accession and keyword routes are blind to a supplement-only table, and Zeng 2024 (found only by a deficiency-term title/abstract query) proves it. No NARROW verdict was too weak, apart from M1, M2 and M4 inside the new wording.

KEEP (12): none hides an over-global absence that I could break. C24 (neural series list) was re-tested: the GEO alias query returned no further neural WWOX perturbation series. C19 and C21 stay, with the caveat in M4. C14 ("not searched in depth") is honest. C9 and C25 are text-level and keyword-level and say so.

CORRECT (8): C3, C6, C12, C13, C15, C17, C20, C27 each fix a statement that is wrong or stale; the three I rechecked at the source (C12 wrong paper, C15 Cre drivers, C17 Zeng) are right.

## 4. Missed absence statements (search of the census, IT6 README section, cards, needs, batch notes)

1. `rescue_window_it6_20261029.md` conditional/inducible row: M3.
2. `rescue_window_it6_20261029.md`, README row P7 and the needs entry: "only post-onset add-back", L2.
3. `wwox_systems_comparison_it5_20261029.md` row "Protein/phospho ISR, flux, lactate, ATP, OCR": "measured in no human neural WWOX system" is perimeter-explicit and consistent; P4 KEEP is right. It lists the hNPC resazurin result, which is the neural redox record in M4.
4. Cards (C01, C04, J01, A01) and needs: the absence-type sentences found ("no treated-after-onset arm exists", "no study reads glia and EEG in the same animals", "brain exposure not measured in any R1 paper") are bounded to a named corpus or paper in their own text; "no treated-after-onset arm exists" restates the authors' "not explored" and is fine. `J01` "no study reads glia and EEG in the same animals over the days that bracket onset" is a global claim without "found"; I did not test it (outside P0a scope), but it is the same class and should be audited.
5. IT6 batch notes: the batch review and verifier notes were not re-audited line by line; the registry tool returned exactly one record carrying the sentence "a census of public records found none", consistent with the producer's consumer table (section 5.3 of the note). I could not independently confirm the producer's claim that DL-MECH-020, DL-REPO-004, HYP-20260709-01 and HYP-20261026-11 carry no absence statement beyond that theme check.

## 5. Not independently re-run

MassIVE metadata filter (the producer marks it UNVERIFIED for today; I did not re-run it either). Europe PMC open-access full-text zero for the census spellings and the "eIF2A" one-hit result (I confirmed the paper, not the query count). Supplementary Figures of Steinberg 2026 and Supplementary Figure 1 of the fly paper (supplement not on this host). bioRxiv was not requested (the producer hit a 429; the preprint text was read from the local copy).

## 6. Checks on scope rules

- Canonical files: the commit touches only the research README, the census, the new note and seven staged receipt JSON files under `receipt_staging/scientist-b/`. No registry, ledger, current file, working-model block or receipt ledger is edited. Verified from the commit's file list.
- "Not found" versus "shown absent": preserved in C1, C2, C18, C22, C23, C26, in the README row and in the census header. The one place where the distinction is blurred is M5.
- The note names no scratch path or session identifier; the alleles of the reference genotype class are not named together (the only allele-type token is a mouse knock-in name in a table row).
