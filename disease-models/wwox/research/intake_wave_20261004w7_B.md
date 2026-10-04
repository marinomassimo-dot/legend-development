# Intake wave 7 — 2026-10-04 — Scientist B: who the counted patients are, and which allele class each cohort counted

**context_policy:** `SOURCE_FIRST` — each source was read (JATS body, tables cell-wise, legends, figures as stated, supplements) and a first-pass dossier was committed (d0efc59) before any registry record, ledger lead or held dossier was opened. Before reading I knew only identity, acquisition state (`paper_packet.py`: identity none, receipts 0, for all six) and the group question. Held sources were opened afterwards, to test patient overlap and allele identity.
**ACTOR_ID:** `scientist` (Scientist B), branch `task/sci-B-20261004w7`. **Not medical advice.**

## Question (from the selection record, group B)
What does each source add to, or limit in, the claim that WWOX-DEE patient counts can be de-duplicated and tied to an allele class — and for each source, how many WWOX patients does it contain, what is their variant, and is the record new or a re-description of one already held?

## Per paper

| PMID | Verdict | WWOX patients | Allele class (consequence: measured / predicted) | New vs held | Receipt file |
|---|---|---|---|---|---|
| 42394473 Karaer 2026 | **INGEST** | 2 | homozygous nonsense `c.790C>T p.Arg264*` (predicted, PVS1) | **new** (held homozygotes of this allele are Indian; held Turkish patients carry L239R); relatedness of the two not stated | `sciB_42394473_1.json` (complete) |
| 36937954 Alotibi 2023 | **INGEST** (allele presence only) | 2 (INFERENZA from two homozygous rows) | homozygous canonical acceptor `c.606-1G>A`; homozygous frameshift `c.33del` (both predicted) | acceptor homozygote **undetermined** vs four held reports of the same allele; `c.33del` new | `sciB_36937954_1.json` (complete) |
| 40429983 Sabau 2025 | **INGEST** | 1 (supplement only) | compound heterozygous: exon-5 copy **gain** + intron-6 donor `c.605+1_605+2delinsAA` (both predicted; gain unconfirmed by array) | **new** | `sciB_40429983_1.json` (complete) |
| 42807679 Khadija 2026 | **INGEST** (carrier, not allele class) | 0 WWOX-DEE; 1 heterozygous carrier | de novo heterozygous ~13 Mb 16q23q24 contiguous deletion including WWOX; other allele not examined | new carrier; **cannot** bear on Tabarki 2015 | `sciB_42807679_1.json` (partial) |
| 41345172 De 2025 | **OFF-AXIS for WWOX-DEE** (population CNV) | 0 | common intronic deletion, AF 0.47 (SANAD) / 0.339 (gnomAD, 1447 homozygotes) | — | `sciB_41345172_1.json` (partial) |
| 42248868 Zhao 2026 | **INGEST** | 1 (no detail) | intron-8 donor `c.1056+5G>C` — **measured** in blood RNA: partial exon deletion, VUS → LP | new; unmatched (no detail printed) | `sciB_42248868_1.json` (complete) |

Dossiers: `research/fulltext_dossiers/PMID<pmid>.md`. Manifests: `research/deepdive_manifests/PMID<pmid>.json` — all six PASS `--verify-artifacts --require-current-schema`. Receipts in `scratchpad/receipts_pending_w7/`, dry-checked on throwaway copies of the ledger and state manifest: all six accepted (exit 0); the real ledger and manifest untouched.

## Answer to the assigned question
1. **Net new WWOX-DEE patients after de-duplication: 5 certain, 1 undetermined.** Two homozygous p.Arg264* (Turkey), one homozygous `c.33del`, one compound heterozygote (exon-5 gain / intron-6 donor), one `c.1056+5G>C` case; plus one homozygous `c.606-1G>A` that can be neither matched to nor excluded from the held Gulf/Saudi reports of that allele. The 16q-deletion carrier and the common-CNV population are not WWOX-DEE patients.
2. **Allele-class tying works only where the source prints a per-patient row.** Karaer and Sabau (supplement) do; Alotibi prints variants without patients; Zhao prints one variant and no person. De-duplication by allele pair + sex + onset + course + outcome is therefore possible for three of the six and impossible for the Alotibi acceptor homozygote — exactly the allele whose held reports already carry an open overlap (Al Baradie family 3 vs Tabarki 2015).
3. **Measured vs predicted, the question that matters most:** of the seven WWOX alleles in this wave, **one** has a measured consequence (`c.1056+5G>C`, blood RNA, partial exon deletion; no fraction, frame, NMD or protein). The canonical acceptor `c.606-1G>A`, the intron-6 donor delins, the exon-5 gain, the nonsense and the frameshift are all predicted. The acceptor allele deserves the warning the held splice analysis already wrote: exon 7 is 186 nt, so an exon-7 skip would be **in frame** — "canonical splice site ⇒ null" is not safe for it.
4. **What the CNV records say and do not say.** Khadija's carrier: examined by karyotype and array only; the other WWOX allele was never sequenced; dozens of genes deleted — not a haploinsufficiency datum, not an allele class. De 2025's deletion: intronic, common, homozygous in > 1000 healthy-population genomes, nominally associated with drug response — not a disease allele, not a dose datum. Sabau's gain: one allele of a compound heterozygote, called by a commercial panel, with no array and no breakpoint — a predicted allele, not a measured dose increase.

## What would change the model if true, and what would falsify it
- *If* blood RNA reads WWOX junctions reliably (Zhao), a blood-RNA measurement of the reference genotype's acceptor allele is feasible without fibroblasts; a failed amplification or a WWOX blood TPM below the assay's informative range would falsify that transfer. Nothing changes in the working model now (MINOR annotations only).
- *If* the Alotibi `c.606-1G>A` homozygote is one of the held patients, the count of independent families for that allele falls; the authors' per-patient data (sex, onset, outcome) would settle it. Not requested (§21d: outreach is not mine).
- *If* the exon-5 gain is a tandem in-transcript duplication, it is predicted out of frame; an RNA or breakpoint study would test it.

## What the brief/selection record got wrong (tested against source)
- **42394473:** "regression and abnormal MRI" are not table-level; they appear only in one Discussion sentence. "Phenotype is table-level" holds for onset and seizure type only.
- **36937954:** "with transcript accession and pathogenicity call" is right, but the two rows are variants, not patients; "consanguinity not stated per case" understates it — nothing is stated per case.
- **40429983:** "confirmed by SNP array/array-CGH" is **false** for WWOX (array cell "no"; the body's three confirmations are other children). "One patient" is right but the allele is not alone: it is a **compound heterozygote** with an intron-6 donor allele, a fact only the supplement carries. "Treatment rows are per-gene-list" — the supplement does give a per-patient impact row (drug impact 1).
- **42807679:** it does **not** bear on the Tabarki 2015 overlap: Tabarki is held as a homozygous sequence allele, this is a heterozygous de novo contiguous deletion. The "same country and referral stream" premise is irrelevant to the identity question.
- **41345172:** "meta-p 4.65e-22 at chr16:79,043,240" does not belong to the 47 % deletion (~660 kb away; the deletion's own best p is 1.68e-4); the "methylated read counts … across three cohorts" are **cancer** cohorts (Ewing sarcoma, paediatric brain tumours, CLL); WWOX occurs 22 times in the XML (case-insensitive, references included), not 14.
- **42248868:** "WWOX appears twice only, so the transfer is methodological" is **wrong**: one of the two occurrences is a **measured** WWOX splice outcome (Case 5), the first at the exon 8 / intron 8 boundary.

## Reading-debt discharge (correction 15)
None of the six was a cited-and-unread primary behind a registry statement (no PAPER/LIT record existed for any). Debts named: Repudi 2021 (PMID 33914858) and Bednarek 2000 (PMID 10786676) remain without complete receipts (queued in the De manifest); PMID 26345274 and Tabarki 2015 remain unread and now carry one more unresolved overlap.

## Candidates
| id | class | target | triples |
|---|---|---|---|
| `CC-20261004W7-B-REGISTRY-01` | MINOR | `PAPER 201`–`206`, `LIT-0494`–`0499` (provisional) | 7 |
| `CC-20261004W7-B-PATIENT-OVERLAP-01` | MINOR | `PAPER 171`, `PAPER 143` (Role sentences) | 5 |
| `CC-20261004W7-B-SPLICE-MEASURED-01` | MINOR | `CLAIM 033` (annotation), `DL-BIO-002` (append-only bullet) | 5 |
| `CC-20261004W7-B-CNV-CARRIER-01` | MINOR | `CLAIM 032` (annotation), new `DIS-035` (provisional) | 6 |

All op lists dry-run exit 0 with `record_scoped_edit.py apply` on main 70513cd; every triple's quote verified against its artefact with the manifest verifier's own matcher.

## What was not read
- 42807679: Figure 2 (patient photographs) deliberately not opened; Figures 1, 3–6 by legend → `partial_fulltext_read`.
- 41345172: main Figures 1–6 by legend; supplementary figures other than pages 3, 17, 21 by caption; Supplementary Tables other than 4 checked for WWOX strings only; Table 4 meta and Australian sheets summarised by script → `partial_fulltext_read`.
- Two supplement PDFs (36937954 Datasheet1; 42248868 MOESM1) have fonts without a ToUnicode CMap: their text layers were discarded and the WWOX rows anchored to rendered pages; the `c.33del` row values of Datasheet1 are not carried.

## Halt record
No safety-classifier halt occurred in this session.
