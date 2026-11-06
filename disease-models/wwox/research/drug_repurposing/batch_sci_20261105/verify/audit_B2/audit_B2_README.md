# Blind locator audit — triple set B2

Method: `legend-locator-audit`. Two mechanical questions per triple — does the quote occur in
the source and does *this* sentence carry *this* statement; does the source say MORE or LESS
than the labelled fields claim (population, age at first exposure or the statement that it is
not stated, endpoint, finding and its size, reversibility, co-factors, and whether an
association was tested and found absent or was merely not reported).

Blind conditions held: no registry, dossier, receipt or manifest for any of these papers was
opened, nothing under the batch directory was read, and the producer of the rows was not asked
or inferred. Every source was re-acquired from an open route named per row. Verdicts are
read-only; this directory contains no edit to any canonical file.

Rows audited: **23**. Row `B2-B1-29` carries no quote surface and was left unsearched by
instruction.

## Counts per verdict

| Verdict | Rows |
|---|---|
| SUPPORTED | 12 |
| OVERSHOOT | 7 |
| UNDERSHOOT | 3 |
| NOT_IN_SOURCE | 0 |
| UNVERIFIABLE_SURFACE | 1 |
| **Total** | **23** |

Every quote that had a surface was located in its source. No row failed to resolve, so nothing
here blocks on a missing locator; the eleven divergences are all in the labelled fields or in
one quote's transcription.

## Non-SUPPORTED rows, with the exact reason

### OVERSHOOT

**`B2-B1-03` — PMID36601084.** The finding field says rapamycin "was the only factor associated
with the abnormality" while the same field invokes univariate regression. On univariate
regression the source reports four significant factors, not one: tuberous sclerosis complex and
concomitant rapamycin as protective, topiramate and hormonal co-therapy as risk. Rapamycin was
the only *independent* factor, and the word "independent" is present in the quote the row
supplies but dropped from the proposition. Second, smaller divergence in the same field: days of
exposure was non-significant on univariate regression but never entered the final multivariate
model, so it cannot be reported as non-significant there. Governing: Table 3 univariate rows,
and the narrative sentences beginning "Considering VABAM as an outcome event" and "After LASSO
regression analysis, the indicators of".

**`B2-B1-06` — PMID36601084.** The symptom breakdown is exact to the sentence. The cofactors
field is mis-scoped: the row declares its population as the 38 with the abnormality, and within
those 38 the source states that no factor was associated with the symptomatic form. The
hormonal and topiramate univariate association the row reports comes from the whole 172-child
cohort, a different denominator. Governing: "Logistic regression analysis showed no
risk/protective factor associated with symptomatic VABAM in the patients with VABAM (n = 38,
Table S2)", then "In the whole VGB exposure cohort (n = 172)".

**`B2-B1-19` — PMID42033488.** Imaging pattern, the additional findings on the same examination
and the resolution are exact. But `age_at_first_exposure: started in the neonatal period` is not
stated: the source dates only the start of the clinical history, at 22 days of life, and never
dates the start of exposure. A separate gap in the same row: the source names a concomitant
anti-seizure co-medication that the cofactors field omits. Governing: Case report, "The clinical
history of this boy began at 22 days of life with neonatal admission for focal seizures".

**`B2-B1-40` — PMID18783433.** Counts, durations, reversibility and the unexposed comparison
group are exact. But the median eleven months against five years is reported by the source as
the age at time of imaging — the variable the abstract's methods sentence names — not the age at
first exposure the field claims. Governing: "Patients were assessed for age at time of MRI,
diagnosis, duration"; "Affected versus unaffected patients, respectively, had a median age of
11 months versus 5 years".

**`B2-B1-42` — PMID19258289.** Examination counts, the significance, the transience, the timing
of the peak and the independence from epilepsy duration and type are exact. But the nine-month
figure is the age of the reviewed infants, attached in the source to the word "infants", not an
age at first exposure; and the source's own statement that the finding is maximal 3 to 6 months
after initiation implies initiation earlier than nine months. Governing: "The authors
retrospectively blindly review 34 brain magnetic resonance imaging of 22 epileptic infants
(age: 9 +/- 1 months)".

**`B2-B1-43` — PMID42470358.** The quantitation limits, the measurable comparator in all three
tissues, the retina-to-plasma ratio of about 4.3, the two-day comparison and the pointer to the
earlier conference report are all exact, and the row is correctly careful to present the
toxicology record as a pointer rather than a result. But the source describes the animals only
as male C57BL/6J mice; it never states their age, so both "adult male mice" and
`age_at_first_exposure: adult` are unstated. Governing: OV329 section, Toxicology, "To evaluate
the tissue distribution of OV329 in the eye, male C57BL/6J mice received a two-day".

**`B2-B1-44` — PMID27796063.** The cell-number, myelination, internode-length, activity-block
and AMPA or kainate results are each exact. The cofactors field hardens a hedge: it states that
a permissive axonal factor "is required" for the GABA effect, where the abstract only suggests
the effect "may require" one. Lowest-severity row in this set, but it is a modality change, not
a paraphrase. Governing: "suggesting that control of myelination by endogenous GABA may require
a permissive factor to be released from axons".

### UNDERSHOOT

**`B2-B1-14` — PMID37690269.** Reversibility and lesion distribution are exact. The finding
field narrows the non-resolving set to the thalami. The source gives two lists of regions where
complete resolution *was* seen; the thalami are absent from both, but the globus pallidi are
also absent from the T2/FLAIR list — and the globus pallidi are the structure the same row calls
most affected. Two further points: non-resolution here is inferred from absence from a list,
which is an attestation rather than a reported comparison, and the source assessed resolution
only in the twelve examined after discontinuation, which the row does state. Governing: "On MRI
after vigabatrin discontinuation, complete resolution of lesions on T2/FLAIR in all patients was
seen in".

**`B2-B1-17` — PMID35183975.** Both contrasts the row reports are exact. The row's own endpoint
pairs spectroscopic GABA with the MRI finding, and the source tested exactly that comparison and
found it non-significant. The row does not record that absent association; it reports instead
the exposed-versus-control contrast, which was significant. A reader of the field alone would
take the spectroscopic measure to support the MRI-finding association. Governing: "The GABA/Cr
tended to be higher in VABAM (0.48 +/- 0.10) than in non-VABAM cases (0.31 +/- 0.15)
(P = 0.31)".

**`B2-B1-41` — PMID20384718.** Cohort counts, the rate, the risk statement and all four
reversibility outcomes are exact. The denominator of the triple-examination subset is
understated: the source scanned fourteen before, during and after treatment, of whom four had
the abnormality. The row reads "of four imaged before, during and after", which loses the
ten who were imaged in all three phases without the finding. Governing: "Analysis of patients
undergoing scans before, during, and after VGB treatment (n = 14) revealed that four patients
had abnormal MRI signal".

### UNVERIFIABLE_SURFACE

**`B2-B1-29` — PMID23194644.** The quote field begins `attestation_without_quote`, declaring
that the sentence carrying the direction of effect also carries an administered amount, so no
quote of it is reproduced. There is therefore no quote to match. Per the brief, no search of
this source was run and no artefact was opened for this row; the labelled fields are
consequently neither confirmed nor contested here. The declaration is the legitimate form for
this surface, and it is correctly made.

## Quote-surface defect on a row whose fields are SUPPORTED

**`B2-B1-46` — PMID31349008.** Every labelled field checks out, including the antagonist
reversal, the inactive GABA-A agonist and the kinase-inhibitor attenuation. The quote does not
occur as written: the source reads "specific GABA" followed by a subscript B then "R agonist",
and the given quote reads "GABAR", dropping the B. The row declares "the receptor subscript is
lost in the record read", but the lost character is the subtype letter, not a typographic
subscript: no rendering of the source yields "GABAR". As transcribed the quote describes the
agonist as unselective among GABA receptors, which is the one distinction the paper exists to
draw. The quote should be repaired before it is persisted; the proposition itself needs no
change. Verdict left at SUPPORTED because both audit questions concern the proposition, and the
defect is recorded in `quote_found_as`.

## Normalisation needed to match the quotes

- Every row: XML tag strip, HTML entity unescape, Unicode NFKC, whitespace collapse.
- `B2-B1-17`: the Greek mu in the concentration unit, encoded as a numeric character reference in
  the record, normalised to a latin rendering on both sides.
- `B2-B1-44`: the receptor subscript A rendered inline, so that the source's "GABA" + subscript
  + " receptors" matches the quote's run-together form. Legitimate rendering artefact.
- `B2-B1-41`: the record's own ASCII rendering of the inequality is reproduced in the quote as
  given; no change needed.
- `B2-B1-46`: see above — matched only after restoring a character that carries meaning. This is
  outside the permitted normalisation set and is reported as a defect, not as normalisation.
- `B2-B1-19`, `B2-B1-20`, `B2-B1-43`: quotes are exact raw substrings of the fetched artefact,
  before any normalisation.

## Artefacts read

Routes used: Europe PMC REST `fullTextXML` for the four records with an open-access PMC version,
and NCBI E-utilities `efetch db=pubmed&rettype=abstract&retmode=xml` for the abstract-level
rows. No contact parameter, no address and no API key was sent to any service. All downloads and
scripts were kept outside the repository, each in its own directory. SHA-256 is of the fetched
bytes, recomputed from the file at emit time.

### Full text

| Source | Route | Bytes | SHA-256 |
|---|---|---|---|
| PMID36601084 / PMC9806385 | Europe PMC fullTextXML | 130472 | `fc7239945736952175610aa28e3c6b54e0a9f41eb05b5dceedb20a9c9fd278f3` |
| PMID42033488 / PMC13357445 | Europe PMC fullTextXML | 36816 | `6d81ab30859a5cd911667130bedfda4c5a803abff0ffb1cafae45fb3e138a8ab` |
| PMID42355787 / PMC13300765 | Europe PMC fullTextXML | 137497 | `3b6142fdf3b7bb22d032d78862f85c2cf20e8a4b51e979e14dc2e10964a49769` |
| PMID42470358 / PMC13675778 | Europe PMC fullTextXML | 278737 | `5409f901b358e52bb2018f4e51ddd15c024b848423816c0d0f225076b04c3840` |

### Abstract records

| Source | Route | Bytes | SHA-256 |
|---|---|---|---|
| PMID1940119 | E-utilities efetch | 6980 | `7203f74660c47cda451fef524056f23917d0df2a452b43c7c8346e5f01b83fd3` |
| PMID10840396 | E-utilities efetch | 7431 | `88ef169abb05e4a44e6507103f99fb8aa921360c52604833d351ba0b0843d9a7` |
| PMID15150739 | E-utilities efetch | 6327 | `a8208cdc706afc308903b94be1511b1e96631027e51f0b77686397eb85ac9fb5` |
| PMID18783433 | E-utilities efetch | 9133 | `da160fce43acdfc138b169513a45fc4322e909da5551e0d6ab92f490ae6af606` |
| PMID19054414 | E-utilities efetch | 9802 | `d3cb9b506b34939382dd0edf5ff6fc8ff461d091b6b3fefdf48e6869674d43ef` |
| PMID19194884 | E-utilities efetch | 25202 | `b3d98c89a61e04899b7033fad96affd94bc3a97c90fa58996e6677f1356e5996` |
| PMID19258289 | E-utilities efetch | 6686 | `bd96ea4e98fdac052291a28ebda95fa27b66c1362f16113511ecbb028d4885f5` |
| PMID20384718 | E-utilities efetch | 6934 | `1bf4f5bd8c072669ca419ac11550be345c81b0199917a5e00adfab4652e46601` |
| PMID23789722 | E-utilities efetch | 9532 | `d925f4c352e7c4a1eeee690855a1dcbe564594133f2c463c3575d5e4c20b192a` |
| PMID25062867 | E-utilities efetch | 8107 | `f8e8a4ae1e3c45141e1434ae5e2b24a2f37eb4d237ccf0ea5f16e90f2f9db381` |
| PMID27796063 | E-utilities efetch | 32701 | `9d4e7e174a6773606ca070c734da239bf7226c3f432c894d7858dcbdb695779b` |
| PMID31349008 | E-utilities efetch | 9314 | `8743061b04d209f70dd17eff302d020034a7b4856e99440878c51051e20d1485` |
| PMID35183975 | E-utilities efetch | 10131 | `e042e45406e45478add264741b72684b8125aa1c816c19bfb03c725fdf4b9b7b` |
| PMID35980256 | E-utilities efetch | 39500 | `264a4e7e836626aef5ba8118f8d2b896020197d4022121d97be22d529a2a3063` |
| PMID37690269 | E-utilities efetch | 9545 | `4f3f857e873acbc667f680fba6741d3d363b2b5dffcdbaf94103fb014a1e80e3` |
| PMID40527948 | E-utilities efetch | 15264 | `9930c69bdc97f35486e22408e579d0831000829cb032b7f0ed0e4db1e44da045` |

Also fetched and hashed but **not used** for any verdict: the abstract records of PMID36601084
(29642 bytes, `cdc63ace99ecd4e0eea2cb77ea807312136a81ce3a6089a43ef912c450588752`), PMID42033488
(11446 bytes, `c0c91adf78f759b66d916bed59ce77f5eb6486a0216223d822ac55bd88e0a5b6`), PMID42355787
(33774 bytes, `93418572e43b6d30ae9f9aa148e1d6845ac1bdc99727ed50681a5352455f457b`) and PMID42470358
(57468 bytes, `d8fe4e77ce4a2ad0b6411fbfe301e11f8d66cfbbee397c4f622061081375709b`), superseded by
the open-access full text of the same four records; and PMID23194644 (8015 bytes,
`035ca0f12a5f1c4284e82b2e0503aeae04db8d29b23ea90f492792ff1195119c` — fetched in the opening
batch before the row was classified, then left unopened per the brief).

## What could not be reached

- **PMID40527948 full text.** Europe PMC returns no PMC identifier for this record and reports
  it as not open access and not in Europe PMC, so no full-text route was available and none was
  forced. The row is labelled "(Abstract, Results)" and its quote is an abstract sentence; every
  labelled field in that row — the imaged denominator, the rate, the diffusion pattern and its
  commonest site, the three significant risk factors, the non-associated duration and the four
  tested co-factors, and the reversibility wording — is present in the abstract, so the verdict
  did not depend on the unreachable sections. One consequence to note: the row's derivation of a
  rate per exposed child is arithmetic from two abstract figures, is declared as such in the
  proposition, and could not be checked against a Results denominator.
- Nothing else was blocked. No route refused automated access and no bot check was encountered.

## Scope note

The audit answers only the two mechanical questions above. It is not a re-reading of any paper,
not a second derivation, and not a scientific opinion on any source. Nothing here is clinical
advice or drafted clinical wording; where a labelled field is not supported, this file points to
the passage of the source that should govern it and drafts nothing in its place.
