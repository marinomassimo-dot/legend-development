# P1 reconcile: package-to-consumer map (IT36), answer first

Non-canonical, not medical advice. Mechanical extraction from the ten packages' READMEs and audits (the audit prevails) against `needs/needs.json`, `investigations_it20.tsv`, `investigations_context_it21.json` and `cards/*.card.json`. No consumer edited, no new reading of any paper.

**49 rows in `map.tsv`: 25 class 1 (editorial narrowing), 19 class 2 (new scientific conclusion), 5 class 3 (new quantitative analysis).**

Rows per package: ttype 6, nmda 5, myelin 6, metabolic 6, nrf2 4, gsk3 4, seizure 5, pv 6, hdac5 4, hcn 3.

**Already in the consumers (`consumer_already_says` not NONE): 34 rows.** Most are class 1 rows where the consumer already carries the caution (T-type attribution by Methods wording only, floor effect, lithium in all genotypes, "reporter in another context does not measure excision", pooled events, sag as inference, recombinant-assay limit of compound X, non-neural fibroblast). The column `consumer_already_says` marks each one (34 rows have a quote).

**Class 2 or 3 rows (go to a source check), 24 rows.**
- Class 3 (5): MELAS trial counts (metabolic); KS p-value floor and declared-count mismatch (pv, two rows); Table 1 passive/sag arithmetic and the unreproduced Welch p values (hcn, two rows). Each row records test, unit, SEM assumption, rounding and the wording "not reproducible under these assumptions", never "data false".
- Class 2 (19): worm cca-1 control; Z944 class-not-isoform; HIF isoform specificity and no WWOX-T-type link; memantine extrasynaptic ratio; GSK3 differentiation sign; clemastine conduction; early-hyperactivity gap; ECAR; GSK3-beta-TrCP route; astrocyte NRF2 precedent; CT99021 per-compound selectivity; PI4KIIalpha branch; perampanel exposure wording; 12-child series; LGS 31 percent anchor; hyaluronan-net absence; His/Tyr direction; HDAC5-HIF reports; ZD7288 off-target.

**Preserve rules.** No row proposes anything that conflicts: MYC not touched by any package; INV-10 keeps four discordant children (three withdrawn); NRF2 row 25 proposes no canonical correction (retracted reference absent from the consumers); HDAC5-HIF row states no therapeutic link; HCN rows do not identify an Ih defect; T-type rows do not identify Cav3 or genotype specificity; Syn1-Cre percentages are not transferred.

**Could not map or not verified.**
- `consumer_already_says` quotes were taken from grep output of the consumers; a few cards were matched by phrase only, not read in full (cards/ holds many files; coverage by phrase, not exhaustive).
- Rows 10 and 16 cite burst source papers marked "to confirm" (burst data paper not re-opened here).
- Consumers named in the package notes but outside this brief's list were not checked (compare_it28_p9 README, hif_it10_p21 README, CONSUMERS.md, nb4_delta CONSUMER_NOTE, IT29 coupling table, WO-30/WO-32).
- PMIDs in `source_to_check` come from the package evidence tables; none was opened by me.
- Receipts: no row depended on a receipt, so the ledger was not consulted.
- The README paragraph on per-package counts above is approximate; `map.tsv` is the count of record.
