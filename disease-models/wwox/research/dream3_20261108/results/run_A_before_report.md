# IGF axis in WWOX-deficient animal models: what is known, what is open (proposal, not conclusion)
Paths are relative to /tmp/legend-dream3-rgzkfo9h/before/disease-models/wwox/.

## 1. What the repository holds
- Only one animal datum on the axis: plasma GH in the lde/lde rat (PMID 17803050, Suzuki 2007, Comp Med). Body text: GH "slightly lower in mutant ... difference was not significant"; dwarfism "cannot be explained solely by low levels of plasma GH"; GH-positive cells present (research/fulltext_dossiers/PMID17803050.md:30-37; research/dismissal_ledger_current.md:305). Sample size in that paper's Table 2 is n=4 normal / 5 mutant per sex (dossier line 50); I did not confirm that the same n applies to the GH panel (Fig 6C).
- The abstract of 17803050 says "decreased concentrations of plasma growth hormone" without qualification. The 2009 citing paper PMID 19500159 repeated that. The repository rejects it as DIS-012 (dismissal_ledger_current.md:301-309; discovery_ledger_current.md:2254-2279; fulltext_dossiers/PMID19500159.md:203).
- Explicitly not done, per DIS-012 (dismissal_ledger_current.md:307-309): no GH rescue, no IGF-1 axis measurement, small sample. Cause of lde dwarfism is recorded as unknown. Revival triggers: adequately powered GH assay, GH rescue in lde/lde, IGF-1 axis measurement.
- Counter-regulatory panel (insulin, glucagon, epinephrine, GH, cortisol, FFA) is recorded as never measured in WWOX models or cases (research/commit_candidates/CC-20261019-SCIENTIST-B-H3-AUTONOMIC-HYPOGLYCAEMIA-01.md:32; fulltext_dossiers/PMID38397994.md:24,37; fulltext_dossiers/PMID34747138.md:7 gives the null-mouse hypoglycaemia as a glucometer reading, n=5 per group, single tail-prick, no hormones). IGF-1 and IGFBPs are not named in these.
- IGF/IGFBP names occur only as co-occurrences, which are not links: IGFBP7 SNP vs WWOX SNP in an infant brain-volume GWAS, two separate hits (analysis/human_prenatal_infant_wave1_20260921.md:58-60,147,439; PMID 28763065); IGF1 and WWOX in a hypertension gene-based study title (fulltext_dossiers/PMID22479346.md:1; human, not an animal model).

## 2. Searched / not re-searched
- Not re-searched: whether GH was reduced in lde rats (answered above). I only grepped the repository for IGF/IGFBP/GH terms (file list truncated to first 50 hits, mostly drug-repurposing TSV/JSON gene lists, which I did not read; they are gene-list occurrences, not evidence).
- PubMed: WWOX AND (IGF OR insulin-like growth factor OR IGFBP OR growth hormone) gave 4 records: 38056170 (cattle meat-quality GWAS listing WWOX among candidate genes; no WWOX-deficiency measurement), 28763065 (above), 23666471 (osteosarcoma review listing both names), 22479346 (human hypertension). None measures IGF-1, GH or IGFBPs in a WWOX-deficient animal. Only abstracts read. The repository's "growth hormone returns 0" (mechanism_intervention_map.md:1267; dismissal_ledger_current.md:308) is thus consistent for animal models with the combined query but the term alone is no longer 0 in a combined OR query (see 4).

## 3. Rivals and proposed measurement
Proposed single measurement: serum/plasma IGF-1 together with IGFBP-3 and GH, from the same sample, in Wwox-null mice (or lde/lde rats) versus littermate controls at a fixed pre-moribund age, fed state, with body weight, plus glucose in the same sample. Sample size should be stated and powered; n=4-5 was inadequate in 17803050.
Rivals for the growth failure: (A) primary GH/IGF-1 axis defect; (B) secondary to illness: hypoglycaemia, seizures, poor feeding or renal impairment (BUN about 3.2-3.5x normal, creatinine raised in lde: fulltext_dossiers/PMID17803050.md:50-60) lowering hepatic IGF-1 (nutritional/hepatic GH resistance); (C) tissue-autonomous skeletal/growth-plate defect with a normal axis.
- Low IGF-1 with normal or high GH and low glucose/weight: favours B (GH resistance of starvation type) over A; this pattern is not Laron-type receptor loss only if IGFBP-3 is also interpreted with it.
- Low GH and low IGF-1: favours A (pituitary), and would justify the GH-rescue trigger.
- Normal IGF-1, GH and IGFBP-3 despite dwarfism: favours C; the axis is then not the cause.
- Raised IGFBP-1 would additionally point to hypoglycaemia/insulin-low state (B). A weight-matched pair-fed control would separate B from A; I did not design that fully.

## 4. Possibly out of date
- The "0 PubMed records" statements for WWOX AND growth hormone were dated by the files' session (DIS-012 in dismissal_ledger_current.md:308; map line 1267); I did not find a date there and the count has not been re-run by me for the single term. The combined query now returns 4 records, none relevant. Statements are in Italian in the dismissal ledger (files are meant to be English), which is a format point, not science.
- The dossier PMID17803050.md:45 says "third instance today": time-bound wording.

## 5. Tool calls
About 4 Bash shell commands (one recursive grep -l over the snapshot, three targeted grep/sed reads of about 15 files), 2 PubMed calls (1 search, 1 metadata fetch of 3 records), 0 full-text retrievals, no web. Elapsed wall time was roughly 1-2 minutes (the shell clock showed about 13 s between two checkpoints).
Not checked: the lde full paper itself (only the repository's dossier of it), mouse Wwox-null papers outside this repository (e.g. growth curves, Wwox-null body weight), IGF terms in the large TSV/JSON files, PubMed with different synonyms (Wwox knockout, Aqp, somatomedin), registries not opened (working_model_current.md).
