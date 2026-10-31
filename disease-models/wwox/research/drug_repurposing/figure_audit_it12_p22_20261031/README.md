# IT12 P2.2: figure attestations still UNVERIFIABLE, ranked by decision weight, top group re-read (2026-10-31)

Not medical advice. Public edition, WWOX-DEE genotype class, no individual-level record. All five papers are NOT WWOX EVIDENCE (non-WWOX systems).

## Decision first

1. **The 28 are located**: the R2 rerun table (`page_adjudications/locator_audit_R2_figures_rerun_20261022.md`, "Not rendered (UNVERIFIABLE, 28)") = 40834072 entries 10-15 (6), 24953239 entries 4, 8-12 (6), 42536722 entries 6, 7, 17-22 (8), 37275776 entries 2, 7, 13-17 (7), 32719346 entry 17 (1, S7 clause only). Triples drawn with `locator_audit.py --pmid <PMID> --triples 0`. The later R2h repairs file does not touch them. The figures were never missing: the corpus copies are byte-identical to the PMC public images (sha256 compared); the earlier failure was the image reader.
2. **No card, need, seed or K01/L01/M01 packet cites any of the five papers** (git grep, join excluded). They reach decisions only through the discovery ledger entry DL-MECH-170 (counter-evidence block, marked "unaudited") and, through it, the early ethosuximide card EB-ETX-01 and the apinocaltamide card H01, and the ethosuximide (G2b) / apinocaltamide (G4a) caveats of the IT8 ranking. The decisions at stake are therefore: how far ethosuximide's result stands for T-type mediation, whether a T-type-class benefit may be called disease-modifying, what a first WWOX-system test must measure, and how far a missense versus null contrast transfers to the reference genotype class.
3. **Eight triples re-read at the image (PMC figures; supplement PDF via Europe PMC REST), 6 SUPPORTED, 1 WRONG on one clause, 1 OVERSTATED (one word).** No ranking group, no card path and no need changes; two caveats change text:
   * **37275776 entry 7 (Fig 7B) changes a quantitative statement.** The stored text puts the GIRK2 50-percent crossings (about 0.03 to 0.06 mM) "inside the shaded therapeutic range". The PMC image shows them 4 to 8 times below the band (about 0.25 to 0.9 mM); GIRK2 homomers are 85 to 90 percent blocked across the band. The proposition also omits the two GIRK1/2 + Gbeta-gamma curves, which the authors call the brain-predominant composition: they cross at about 0.4 to 1 mM, i.e. only partly blocked (about 20 to 60 percent) in the band. Net: ethosuximide has a measured non-T-type target at labelled exposure in oocytes, which the ranking's "T-type potency is weak against the labelled range" wording does not show; it does not make GIRK the WWOX mechanism (oocyte, no WWOX data, neuronal GIRK2 homomer abundance unknown per the authors).
   * **42536722 entry 19 (Fig 3J)**: star and P = 0.042 are right, "remains lost" overstates (triple mutant mean about 0.2 vs control about 0.3; Fisher exact on n = 12 vs 22). The Cacna1g-deletion result is a borderline genetic separation and must not be counted as a second confirmation of the ethosuximide result (entry 18, Fig 2E, t-tests P = 0.034 and 0.016), which is SUPPORTED.
4. **What the SUPPORTED re-reads add to the ethosuximide lead (DL-MECH-170)**: in 37275776 Fig 4A the wild-type arm is at about 3 SWD against about 35 in the mutant, with only genotype contrasts per time point (no drug-by-genotype term), so the wild-type floor hazard cited by the ledger is confirmed at the image; in 24953239 the relay-neuron T-type current is smaller, not larger, in the absence strain and the burst-threshold difference converges under ZD7288 (Ih), so an ethosuximide effect is not evidence of T-type excess; in 32719346 S7-S9 ethosuximide leaves wild-type behaviour and the PAK3 and FMR1 social-memory deficits unchanged (no vehicle arm, n 7 to 13). Kept as caveats; nothing here is new compound activity in a WWOX system.
5. **Left for later: 20 triples** (list below). The next one worth a read is 42536722 entry 21 (Fig 5, PV chemogenetic activation rescues SWD and social novelty), because it touches the Q4 PV-interneuron seeds.

Proposed text changes are in `proposed_changes.tsv` (not applied). Proposed receipts are in `proposed_receipts.tsv` (nothing written to the ledger).

## Method and what I knew beforehand (not blind)

Read before judging: the stored propositions and quotes of all 28 (blind packets, but I read them with their anchors), the R2 rerun and R2h files, DL-MECH-170 and its counter-evidence block, EB-ETX-01 and H01 cards, the IT8 ranking README section 3, `needs.json` hits, and the R2 scientist-b notes. The judgement is informed by those and is not blind; the R2 audits were. I judged each proposition against the figure panel and the legend or Results text, not the reverse.

Ranking rule (`ranked_28.tsv`, weight 1 to 5): 5 = a decision statement in the ranking caveats, DL-MECH-170 or EB-ETX-01 rests on it and the figure can change it; 4 = bears on specificity, allele class or the first experimental readout; 3 = supporting premise or duplicate of a higher entry; 1 to 2 = model or phenotype description, precedent from another lesion. The top group is weight 4 to 5 (8 triples). Entries 6 and 7 of 42536722 are the same panels as 18 and 19 (same observation, a second proposition): I looked at them in passing, they are not independent confirmations and are not counted in the 8.

## Verdict table (full text and locators in `verdicts_top8.tsv`)

| Rank | Triple | Stored | Verdict now | Depth viewed | Note |
|---|---|---|---|---|---|
| 1 | 37275776 #7 Fig 7B | UNVERIFIABLE | WRONG (one clause); substance SUPPORTED | image + legend + Discussion text | IC50 below, not inside, the band; GIRK1/2 + Gbg curves omitted |
| 2 | 37275776 #2 Fig 4A | UNVERIFIABLE | SUPPORTED | image + legend | genotype-only stats; WT floor |
| 3 | 37275776 #17 Fig 2 | UNVERIFIABLE | SUPPORTED | image + legend | missense vs deletion clear |
| 4 | 24953239 #4 Fig 5 | UNVERIFIABLE | SUPPORTED | image + legend + text | current at P7-P9, mRNA/protein adult; panel e two stars vs text p < 0.001 |
| 5 | 24953239 #12 Fig 6 | UNVERIFIABLE | SUPPORTED | image + legend + text | resting potential not restorable under ZD7288 |
| 6 | 42536722 #18 Fig 2 | UNVERIFIABLE | SUPPORTED | image + legend + text | not-rescued rests on two t-tests |
| 7 | 42536722 #19 Fig 3 | UNVERIFIABLE | OVERSTATED (minor) | image + legend + text | "remains lost" vs mean about 0.2 vs 0.3, Fisher P = 0.042 |
| 8 | 32719346 #17 S7-S9 | UNVERIFIABLE (S7) | SUPPORTED | S7 image from public PDF; S8, S9 corpus raster of that PDF; legends from public PDF | no vehicle arm, n 7 to 13 |

Source-internal discrepancies found (not the proposition's fault): 24953239 Fig 5e two stars vs text p < 0.001; 42536722 text cites Fig 3 "H and I" for panels I and J and gives KO N = 9 vs N = 8 in the 3G legend.

## Ranked table of all 28

See `ranked_28.tsv` (rank, PMID, entry, figure, decisions fed, weight, group, justification, whether audited here). Summary: group A (8, audited): 37275776 #7, #2, #17; 24953239 #4, #12; 42536722 #18, #19; 32719346 #17. Group B (weight 2 to 3, 8): 42536722 #21, #7, #6; 37275776 #16, #15; 24953239 #10, #9, and #14 of 37275776. Group C (weight 1 to 2, 12): the remaining.

## Left for later (20) and why

| Triple | Reason |
|---|---|
| 42536722 #21 (Fig 5, PV chemogenetics) | weight 3; next in line, touches Q4 seeds; proposes no drug |
| 37275776 #16 (Fig 6 oocyte Gbeta dose), #15 (Fig 5 baclofen currents) | weight 3; premises for GIRK gain and allele-class caution; no current statement hinges on them beyond what #17 and #7 carry |
| 24953239 #10 (Fig 3 Ih), #9 (Fig 2; values cross-read in Fig 6b controls only), #8, #11 | supporting detail of Ih premise; #12 is the decisive test and is audited |
| 42536722 #7, #6 | same panels as #19, #18; viewed incidentally, same observation; verdict not recorded as independent |
| 42536722 #17, #20, #22 | model characterisation and a vehicle control; no statement depends on them |
| 40834072 #10-#15 (all six) | Cntnap2 precedent only, "T-type change is lesion-specific"; no ranking, card or need statement uses a number from these figures |
| 37275776 #13, #14 | phenotype description and MEA context |

Reopening condition for any of them: a decision statement starts to cite a number or a significance mark from that panel, or the operator asks; the public route (PMC article page and CDN image, Europe PMC REST supplementaryFiles) worked for all five papers.

## Access (`access_log.tsv`)

PMC article pages and CDN images with the default agent: all worked; the images are byte-identical to the corpus copies. Europe PMC REST supplementaryFiles: worked (slow). Two routes were blocked and not circumvented: `europepmc.org/articles/.../bin/...` (HTTP 403 bot-check page) and the PMC supplement `bin` link (reCAPTCHA page); neither was needed. No e-mail address or personal data sent. Downloads were kept in the scratchpad (`/tmp/claude-1000/-home-desktop-legend-development/4325d70d-8bea-4789-8046-d7a9ee74c97f/scratchpad/it12c/`), not in the repository; the corpus under `files/` was only read.

## Limits and UNVERIFIED

* Band edges and curve crossings in Fig 7B are read by eye from a 708 x 482 image (band about 0.25 to 0.9 mM, consistent with the ranking README's labelled 283 to 708 uM); no digitisation. The GIRK1/2 + Gbg crossings (0.4 to 1 mM) are by eye and agree with the authors' "EC50 ~1 mM" for the wild-type Gbg case.
* S8 and S9 pixels were viewed on the corpus page rasters of the same supplement PDF, not byte-compared to renders of the public PDF; the legends were read in the public PDF and agree.
* The other 20 triples and all supplement items other than S7-S9 of 32719346 stay UNVERIFIED; the 37275776 Data Sheet was not opened.
* The ledger DL-MECH-170 statements built on these figures stay labelled unaudited until the batch records the proposed receipts.

## For the batch path

1. Apply or reject `proposed_changes.tsv` PC1 to PC8 (manifest wording repairs for 37275776 #7, 42536722 #19, 24953239 #4/#12, 32719346 #17 qualifiers; ledger and ranking-caveat text; EB-ETX-01 card text). PC9: nothing else cites these papers.
2. Re-run `locator_audit.py --pmid` for 37275776 and 42536722 after the repairs (blind), since entry 7 and entry 19 would be new wording.
3. Record the four proposed receipts (`proposed_receipts.tsv`) in event order after the usual scratch-clone trial; none was written here.
4. Update the R2 rerun accounting: of the 28 open triples, 8 now judged (6 SUPPORTED, 1 WRONG clause, 1 OVERSTATED), 20 open; the adverse count for the rerun lot becomes 1 + 2.
5. Queue: 42536722 #21 next; the rest only on demand.
