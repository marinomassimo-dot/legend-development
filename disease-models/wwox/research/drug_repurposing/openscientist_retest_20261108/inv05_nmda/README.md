# INV-05 NMDA: full-input repeat of the OpenScientist assessment (os-05, 2026-11-08)

Not medical advice. No dose, schedule or route appears. Source cap for Phase 2: at most 5 newly read sources; 5 read, all `abstract_only` (no overrun). Staged receipts (suffix 33, not recorded) are in `receipts/`.

## Answer first

1. DATO: the report contains one WWOX datum, the d-APV-sensitive burst in Wwox neuron-knockout slices (`PMID 34634460`, already completely read in LEGEND). Everything about radiprodil, memantine and ketamine is transfer from other systems. The previous package (`nmda_inv05_20261107`) already held the main correction; the report adds items the earlier brief did not carry (gap junctions, developmental apoptosis as a gate, combinations, the in vivo Wwox test, perzinfotel, dextromethorphan, nitrous oxide).
2. INFERENZA: the report's lead (radiprodil as "closest match and direct test of GluN2B") stands only as a comparison arm. The only radiprodil in vivo datum it cites is a GluN2A gain-of-function line (D01); the human-safety "+" is a background sentence in an abstract (D02); and its premise that GluN2B NAMs are "not use-dependent" is contradicted for the class prototypes at abstract level and unverified for radiprodil (D15, verifier-read abstracts).
3. DATO: two assertions the report presents as facts do not hold as written. Perzinfotel's clinical failure for psychotomimetic or neurotoxic effects with excess mortality was not found (D05), and the selfotel head-injury trial was aborted because of deaths seen in concurrent stroke studies, with a retrospective analysis not confirming excess mortality in head injury (D09).
4. INFERENZA: the report's "gap junction dependent" burst rests on carbenoxolone, which the WWOX source says could also block NMDA receptors and blocks pannexin channels, with incomplete washout (D08). The report's L26 and L132/L153 contradict each other, and L125 ("the one competitive agent") contradicts L9/L30/L161 (two agents) (D04).
5. DATO: the report's "only direct NMDAR evidence" (L51) and "No WWOX-specific NMDAR data" (L136) are too absolute: the source also reports a larger d-APV-sensitive delayed evoked response in the knockout (D13). Its GluN2B-dominance evidence is misattributed in one case: the cited neonatal EPSC sentence describes a ketamine-induced increase (D10).

## (a) Coverage

* Items: 91 (E91 added after the audit). By kind: observation 19, compound 13, inference 10, limit 10, counter_evidence 9, other 7, experiment 6, target 5, hypothesis_favourable 4, recommendation 3, mechanism_step 2, open_question 2, alternative_explanation 1.
* By `legend_class` (per item): already_present_and_used 23, present_not_used 33, verified_or_corrected 15, new_to_legend 5, unverified 10, superseded_or_contradicted 4 (E11 nitrous oxide reclassified after the audit; E91 not yet classified in `reconcile.tsv`: unlabelled uncited matrix scores, same treatment as E57).
* By `prior_brief_fate` (per item): kept 22, modified 29, narrowed 12, omitted 23 (E13 "not addressed" counted with omitted; three items not applicable).
* Sources: 24 rows; identity check run on all 21 PMIDs (`queries.tsv` Q01).

## (b) What the previous brief kept, narrowed, modified, omitted

Kept: the d-APV datum and its limits (E01, E03), memantine premise via `PMID 20720132` (E07), precedents A and B (E15, E44), the genotype-receptor question (E63). Modified: "radiprodil, memantine, ketamine as comparators" became GluN2B NAM versus matched-current d-APV with memantine second-line (E16, E54 to E56, E64 to E66); age-implies-composition rejected (E27). Narrowed: apoptosis and therapeutic window ("do not deduce a window from fraction blocked"; E36 to E41, E67), failures of single antagonists (E20 to E22), combinations ("later developments", E69). Omitted: gap junctions (E04, E05, E70), perzinfotel, dextromethorphan, amantadine and nitrous oxide as items, the ketamine status-epilepticus literature, drug-resistance framing, the in vivo Wwox test, GABAergic partners.

## (c) Sustainable favourable reasons

* DATO: NMDAR activity is required for the burst in this preparation (D13). INFERENZA: this justifies a mechanism-directed comparison with total-current matching (X2 in `nmda_inv05_20261107/output/experiment.tsv`), not a drug choice.
* DATO: radiprodil blocks GluN2B receptors and acts on most tested GRIN1/GRIN2B variants in vitro (EV02, abstract only); it delays PTZ seizures in a GluN2B gain-of-function mouse (abstract). Transfer to WWOX is IPOTESI.
* INFERENZA: the report's decision structure (subunit axis; tonic-versus-phasic axis; Mg2+ and voltage stated) is sound and is already X2 and X5.

## (d) Errors and counter-evidence found

D01 (GluN2A model supports GluN2B drug), D15 (class NAMs activity-dependent at abstract level), D02 (safety "+" unsupported), D04 ("Refuted" wording), D05 (perzinfotel), D06 (dextromethorphan encephalopathy uncited; nearest source is a ketogenic-diet paper with a background sentence), D08 (carbenoxolone), D09 (selfotel), D10 (PMID 28782587 is a neonatal ketamine-exposure study; fit uncertain). Citation fit: PMID 12365832 is an AMPA-antagonist review (abstract does carry the stroke list); PMID 22261077 and 34747138 are not primary for the claims they carry; PMID 15772895 has no stored DOI. All of these are identity or abstract-level findings, none a full-text reading.

## (e) Hypotheses still explorable and what would weaken them

* IPOTESI: GluN2B-containing receptors participate in sustaining bursts. Weakened if a matched-current total NMDAR reduction does the same (X2), or if GluN2A-preferring block works equally.
* IPOTESI: channel blockers reproduce the d-APV effect if the drive is regenerative. Weakened if memantine at a stated Mg2+ and holding voltage fails while d-APV works; a failure needs verified exposure (BRIEF rule).
* IPOTESI: a gap-junction or pannexin contribution adds to the NMDAR dependence. Weakened if a more selective blocker than carbenoxolone has no effect.

## (f) Priority question and experiment

Does the burst need GluN2B-containing current, or does any matched reduction of total NMDAR current do the same (X2), with the recording Mg2+ stated (X0)? The report's version (radiprodil versus a GluN2A-preferring antagonist) is a subset; the matched-current form separates subunit from network gain.

## (g) Consequence for drug repurposing, with novelty class

* GluN2B NAM versus matched-current d-APV in the burst assay: already_in_legend (X2); literature novelty not assessed.
* Memantine as second-line premise test: already_in_legend (X5).
* Ketamine as positive control: new_to_legend as an arm; the prior package found memantine and ketamine indistinguishable on several measures at abstract level, so a ketamine arm adds little; literature novelty not assessed.
* Gap-junction or pannexin partner for an NMDAR arm: new_to_legend as a combination; the carbenoxolone caveat is already_in_legend; literature novelty not assessed.
* Perzinfotel, amantadine, nitrous oxide, dextromethorphan: no change; none is carried (amantadine, dextromethorphan named in F04; nitrous oxide is present in `profiles_it23_p4_20261103/identity_join.tsv` line 1457, so new only within the NMDAR card and package perimeter).
* Developmental-safety gate before any translation: already_in_legend as a principle (viability and maturation separate); the report's caspase-3 assay is a design suggestion, new_to_legend only in form.

## (h) Consumers to update

None edited. Proposals: INV-05 rationale text could add D05 and D09 as corrections to the external report's class argument and D08 as the carbenoxolone caveat on the gap-junction half of the cited quote; `cards/F04_nmdar_intervention_class.card.json` selfotel line could read "head-injury trial stopped after a stroke-study signal; later analysis did not confirm excess mortality in head injury" (abstract level, PMID 15335108). Reason for no more: no new WWOX datum was read.

## (i) Not reachable or not done

Full text of PMID 40994429 (Europe PMC HTTP 500; PMC tool returned an empty body). Not read by anyone: PMIDs 15717010, 21896318, 28782587, 12520755, 17312200, 19204407, 23395831, 12849400, 15772895, 41409370, 37334223, 34747138, 30356099 (identity checked only). Dextromethorphan search (47 hits) not screened. The Wwox plus NMDA search gave 5 hits unquoted and 4 with "glutamate receptor" quoted (Q11, Q13); I did not screen titles; the verifier did (three irrelevant hits). Perzinfotel's clinical development record outside PubMed (company or regulatory sources) not searched. No cited source was opened beyond abstracts; no figure viewed.

## (j) Queries run

See `queries.tsv` (Q01 to Q13). Evidence rows: `evidence.tsv`; decisive propositions: `decisive.tsv`; item-level comparison: `reconcile.tsv`; first-phase files: `extraction.tsv`, `sources_cited.tsv`, `chains.tsv`, `phase1_note.md`.

## Audit appendix (blind verifier vf-05, 2026-11-08)

Verdicts: the audit states 12 SUPPORTED and 1 PARTLY (D11), 0 NOT SUPPORTED, 0 UNVERIFIABLE; its table lists 14 rows (D01 to D14), 13 of them SUPPORTED, so its stated total of 13 is one short (the table is taken as correct). D11 is PARTLY because the magnitude of synaptic block is not in the abstract and comes from the previous package. Coverage check of the first extraction: 12 points, 8 PRESENT, 3 PRESENT_NARROWED (pore-blocker trapping in the diagram, amantadine cells, the per-agent match-to-d-APV scores), 1 MISSING (radiprodil and other CNS-exposure matrix cells), now repaired by E91 and by additions to E02, E09, E32. Reconciliation sample: 8 rows; E11 and E78 corrected, E36 to E40 attribution fixed, 5 passed. Evidence sample: 7 rows verbatim; EV07 role changed to context; evidence rows added for the other propositions (EV08 to EV22).

Narrowings applied: D01 (the only radiprodil in vivo datum the report cites; the cited paper has more), D03 (4 hits, three irrelevant hits named; string recorded), D08 (carbenoxolone detail from the source), D09 (psychotomimetic unsupported in the cited paper), D10 (misattributed EPSC sentence; P7 scope), D11 (Mg2+ not stated, report hedges), D12 (no damage at P14, doses slightly larger than clinical), D13 (Fig S3 datum, Synapsin-Cre, heterozygotes, late-stage caveat), D14 (paediatric 50 percent, 5 of 8 survivors, concomitant anaesthetics). New proposition D15 added from the verifier. D13 and D08 rest on the verifier full-text reading of `PMID 34634460`; I did not read that paper in this phase. Rows of `evidence.tsv` from EV08 to EV21 are abstract-level readings by the verifier or quotes carried from the previous package, without receipts of mine; the five receipts of mine are for `PMID 40994429`, `15335108`, `22261077`, `15075380`, `12365832`.

Not reached by anyone: full text of `PMID 40994429` and `20720132` (PMC tool empty; Europe PMC HTTP 500), every source beyond its abstract except `PMID 34634460`, Supplementary Table S1 and Fig S3 of `PMID 34634460`, radiprodil gating properties from a primary source, perzinfotel clinical-development records outside PubMed. A new read of `PMID 40994429` Results or of the radiprodil mechanism would be needed to settle D15 for radiprodil and D02; recorded as an open need (cap of 5 already used).
