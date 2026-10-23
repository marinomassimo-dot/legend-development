# Module batch 2026-10-23 — selection note, rows Q-N-01 to Q-N-07 (scientist-a)

Task `MODULE-A-20261023`. Class-level, de-identified. Every paper that is not a WWOX paper is
**NOT WWOX EVIDENCE**. No dose, administration or suitability is stated; not medical advice.
Receipts are staged under `receipt_staging/scientist-a/`, never recorded by me.

## 1 · What the rows turned out to be

The seven rows say `NO_RECEIPTED_EVIDENCE` and ask the selector to resolve the author-year
citations of the map record. **The map records N-01 to N-07 (mechanism_intervention_map.md,
lines 630 to 690) contain no author-year citation and no PMID at all.** The support is named
elsewhere: in the discovery-ledger records the map links by wikilink (DL-BIO-009, DL-REPO-001,
DL-MOL-009, DL-MECH-034, HYP-20260709-03), in claims (CLAIM 019, 030) and in commit candidates.
The join looks at the map record's own text, so it found nothing, and printed an abstention that
is **false for 6 of 7 rows**: the papers behind them are already receipted, several at
`complete_fulltext_read`. What was missing was not reading but (a) the link from the query to the
papers and (b) locators for the specific sentences the map's wording rests on.

## 2 · Step 1 — resolution, identity, registry state

Identity: `pubmed_identity_check.py` MATCH for every PMID below except 39039877 (CROSSREF_UNAVAILABLE,
Chinese-language record; PubMed title and authors only).

| Row | Citation reached (via) | PMID | Registry / receipt state before this batch |
|---|---|---|---|
| Q-N-01 | Steinberg 2021 (DL-MECH-034, CC-20260826-MTOR-DIRECTION-01) | 34268881 | 8 receipts, 43 locators, **none** on mTOR/autophagy/4E-BP1 |
| | CORPUS-STUB-043 | not resolved | stub, not processed |
| | CORPUS-STUB-177 (EBV-LMP1/AKT-mTOR, nasopharyngeal carcinoma) | 31966718 | stub, no receipt; not WWOX-neural; not read |
| Q-N-02 | Cheng 2020 | 32000863 | complete, 31 locators incl. Fig 7d wild-type lithium effect (map claim fully locatored) |
| | Wang 2012 (GSK3B L404) | 22193544 | complete, 6 events, locatored |
| Q-N-03 | Riccardi 2026 (DL-REPO-001, abstract only) | 42190144 | **no receipt**; OA copy exists in an institutional repository but is behind a proof-of-work bot challenge |
| | Abdel-Salam 2014, Szymanska 2014, Elsaadany 2016, Oliver 2023 (found by corpus search of local full texts for sodium-channel-blocker names) | 24456803, 24949445, 27495153, 36779245 | first and last complete; middle two not read by me |
| Q-N-04 | Choi 2026 (VABAM n=2) | 41442931 | registry "integrated", **0 receipts**; closed access |
| | You 2024 | 39101447 | complete |
| | Shaukat 2018 | 30361190 | complete, only 1 vigabatrin locator |
| | Wang 2024 (Chinese cohort) | 39039877 | stub, closed access |
| Q-N-05 | Johannsen 2018 (Q230P, protein not detected) | 29808465 | complete |
| | Hua 2015 (miR-153, source of anti-miR-153) | 25708809 | **no receipt, no manifest** (now read) |
| | Obeid 2026 (dose-dependent AAV) | 42422765 | 14 events |
| Q-N-06 | Shaukat 2018, Abdel-Salam 2014, Davids 2019, Battaglia 2023, Abu-Remaileh 2014, Steinberg 2021 (DL-BIO-009) | 30361190, 24456803, 30362252, 38161429, 25012504, 34268881 | all receipted; Davids and Battaglia only partial; metabolic items had no locator in Shaukat or Davids |
| Q-N-07 | Abu-Remaileh and Aqeilan 2014 (DL-MOL-009); Abu-Remaileh 2018 | 25012504, 29724996 | complete, locatored (digoxin entries 14, 20); dose "unverified" status not re-opened (no dose written here) |

Additional papers searched (PubMed, 2018 onward): mTOR/WWOX returned only 35984507 (Zfra1-31,
already receipted) and non-neural lung and cancer papers; lithium/WWOX returned nothing new;
digoxin/HIF1A/WWOX in neural tissue returned nothing. Three-test outcome for new candidates:
Riccardi 2026 passes substance and question but fails lawful-body for me (bot challenge);
Choi 2026 and Wang 2024 fail lawful-body (closed access, no repository copy, Europe PMC absent);
Hua 2015 passes all three. Remaining hits (cancer or review papers) fail the question test.

## 3 · Step 2 — readings (6 staged receipts; manifests PASS, strength-scan clean)

| PMID | Row | Depth | Receipt (staged) | New locators |
|---|---|---|---|---|
| 34268881 | N-01, N-06, N-05 | partial (QUESTION_DRIVEN resume) | FTR-20261023-34268881-01 | 9 (entries 43-51) |
| 30362252 | N-06, N-03 | partial (figures captions-only, supplement unavailable) | FTR-20261023-30362252-01 | 5 |
| 36779245 | N-03, N-04 | partial (Results, Table 2) | FTR-20261023-36779245-01 | 8 |
| 30361190 | N-06, N-04 | partial (Results) | FTR-20261023-30361190-01 | 6 |
| 24456803 | N-06, N-03 | partial (Results) | FTR-20261023-24456803-01 | 2 |
| 25708809 | N-05 | first read, partial (supplement images unopened) | FTR-20261023-25708809-01 | 12 (4 figure attestations) |

Parked, with cascade: Riccardi 2026 (PMC absent, Europe PMC absent, OpenAlex green copy at an
institutional repository: the file route returns an Anubis proof-of-work page; not bypassed;
`OA-but-bot-blocked`, operator-browser route). Choi 2026 and Wang 2024 (OpenAlex closed, Europe
PMC not indexed, no repository copy). Davids 2019 figures: PMC bucket lacks them; NCBI and Europe
PMC figure routes are challenged. No Unpaywall-type service was used.

FIRST-PASS OBSERVATIONS COMPLETE → PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: the readings were
QUESTION_DRIVEN (I had seen the map and ledger wording before opening the papers).

### What the readings found, per row (NOT WWOX EVIDENCE labels apply to Hua 2015 only as to tissue: it is a WWOX paper in liver cancer)

* **Q-N-01 mTOR.** In the paper's own deposited WWOX-KO organoid lists (WT n=2 vs KO n=4, nominal-P
  sets): EIF4EBP1 down (log2 -0.87), but **MTOR itself up** (+0.4, adjusted P 0.0498), DDIT4 up,
  DEPTOR up, EIF4EBP2 up, TSC2 down, RPS6KB2 down, RB1CC1 down; RPTOR, RICTOR, RPS6KB1, ULK1,
  ATG5/7, BECN1, MAP1LC3B, SQSTM1 absent from both lists. The article text contains no mTOR,
  autophagy, 4E-BP or rapamycin string. So the wording "mTOR/EIF4EBP1 down" (DL-MECH-034) is
  not what the table shows; the axis is mixed at transcript level and says nothing of
  signalling. This **supports INSUFFICIENT** and sharpens it. Separately, a referee of the
  submitted version remarks on detrimental overexpression effects (figure not held).
* **Q-N-02 lithium.** Already fully receipted (Cheng 2020 Fig 7d). Nothing new needed; the row
  was a linking failure only.
* **Q-N-03 sodium-channel blockers.** Oliver 2023 Table 2: 8 of 13 patients list at least one
  sodium-channel-blocking drug (class label mine), 7 of 13 one of carbamazepine, oxcarbazepine,
  phenytoin; 12 of 13 drug-resistant; the one non-resistant patient lists none; **no per-drug
  response is reported**, so the map's revival trigger ("documented response") cannot be met or
  refuted from this cohort. Two other local papers record a partial response to
  valproate plus lamotrigine (Abdel-Salam, receipted locator) and phenytoin failing (Elsaadany,
  not read by me). Oliver also states burst-suppression is not described in WWOX-DEE, which
  conflicts with the "WWOX-BS" framing of the map and DL-REPO-001 (Riccardi unread).
* **Q-N-04 GABAergic / vigabatrin.** Shaukat 2018: child 1 spasms resolved on vigabatrin, child 2
  only a partial response and persistent hemispasms on four drugs; Oliver: vigabatrin in 8 of
  13, no response reported. The map's "resolved spasms in a null child" is true but one of two.
  Choi 2026 (the MRI-toxicity half) remains unread.
* **Q-N-05 boosting expression.** Hua 2015: antagomir raised WWOX in **liver tumours** of a
  chemical-carcinogenesis mouse model, shown as one blot of two lanes per group, unquantified;
  all cell work in two HCC lines; no neural tissue; dose/vehicle not in Methods; the paper has
  typographical errors (miR-163, miR-300) and a text-versus-panel direction conflict in its
  survival analysis. The HYP wording "in liver" is slightly generous: it is in tumours.
* **Q-N-06 lactate.** Davids 2019: MRS lactate "extremely low" is one sentence in one patient,
  with no spectrum, value or figure; the paper attributes HSPG2 to skeletal features, **not** to
  the MRS finding (the map's "confounding" is the map's inference); the same patient had
  neonatal hypoglycaemia and the Discussion says "some findings of the metabolic syndrome"
  reported in mice. Shaukat: lactate, ammonia, acylcarnitine, uric acid, homocysteine, amino and
  organic acids normal; transferrin isoforms only in child 1 (child 2 has sulfocystine).
  Abdel-Salam: serum lactate and ammonia normal; **no muscle biopsy and no mitochondrial study
  anywhere in the text**, contradicting DL-BIO-009 and the map ("muscle biopsy included").
  Steinberg 2021: HK2, SLC2A1, LDHA up, PDK1/PKM/HIF1A absent from the lists.
* **Q-N-07 digoxin.** No new reading; already locatored (glycaemia endpoint). Row is a linking failure.

## 4 · Observations on the module row (for the operator's diagnosis)

**Was the Ask the right ask?** Partly. "Resolve the author-year citations of this record to PMIDs"
presumes the record carries citations. For all seven it carries none (verified by regex over lines
620-700 and the whole map: author-year strings occur only at lines 407-784 in unrelated records).
The citations live one hop away (the ledger records the map wikilinks, claims, commit
candidates). The ask should be "resolve the support of this record, following its wikilinks one
hop", or the join should follow the wikilinks itself.

**What I needed that the row did not say.** (1) The hop-1 records to read (DL-BIO-009 etc.). (2)
The fact that most cited papers were already receipted, so that "NO_RECEIPTED_EVIDENCE" was
false and the real question was "which sentence has no locator". (3) Which claim sentence of the
map was to be tested (e.g. "muscle biopsy included", "mTOR/EIF4EBP1 down", "HSPG2 confounds MRS").
(4) Whether a bot-blocked open-access copy counts as acquirable. (5) Per-row coverage hints: partial
receipts (Davids, Battaglia) and receipts with zero locators on the point (Shaukat metabolic list,
Steinberg mTOR) were invisible to the row, which counts papers, not locators on the claim.

**Citation resolution.** Map records N-01..N-07: 0 author-year citations, 0 PMIDs. Hop-1 ledger records
named 14 author-year citations across the seven rows (Steinberg 2021, Cheng 2020, Wang 2012,
Riccardi 2026, Choi 2026 via registry, You 2024, Shaukat 2018, Abdel-Salam 2014, Davids 2019,
Battaglia 2023, Abu-Remaileh 2014, Johannsen 2018, Hua 2015 (journal and year only, no author in
the hypothesis text), Breton 2021). Resolved cleanly to a PMID by the registry: 12; resolved only
by me through PubMed title search: 1 (Hua 2015, the hypothesis names no author or PMID); not
resolved: 1 (CORPUS-STUB-043, "the only other record naming mTOR", no PMID reachable from the
stub in the time spent) plus the two unreceipted rows whose PMID resolved but whose body was
inaccessible (Riccardi, Choi). None was ambiguous by author-year alone.

**Did the map's wording match the papers?** Four mismatches found, three of them against
already-receipted papers: (a) "mTOR/EIF4EBP1 down": MTOR is up in the deposited table (the
N-01 body is already cautious; the ledger tag was the problem); (b) "muscle biopsy included" /
"complete metabolic and mitochondrial screen": not in Abdel-Salam, and an existing locator already
said so, so the prose was never reconciled with the manifest; (c) "transferrin isoforms normal in
both patients": child 2's list differs; (d) "HSPG2 confounds the MRS lactate": the paper
attributes HSPG2 to skeletal findings only. Also "WWOX-BS": Oliver says burst-suppression is not
described in WWOX-DEE. Matches: lithium (Fig 7d), digoxin endpoint, vigabatrin n=2.

**What the module cannot see (my evidence).** It counts papers, not locators on the sentence; it
reads the map record text only, not hop-1; it cannot see that a registry "integrated" paper (Choi)
has zero receipts; it cannot flag bot-blocked open access; and its abstention string treats "no
link" as "no evidence".

## 5 · Owed / not done

* Riccardi 2026 and Choi 2026 and Wang 2024 full text (operator-side browser or ILL).
* Battaglia 2023 MRS statement (partial receipt) and Johannsen 2018 MRS, Elsaadany 2016 and Szymanska
  2014 drug statements: identified, not read (budget of effort, not of the 12-paper cap).
* Blind locator audit of the 40 new locators; Appendix Fig S3A of Steinberg 2021 (unavailable);
  CORPUS-STUB-043 identity.
