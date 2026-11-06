# Blind locator audit — R1b triples

Method: `legend-locator-audit`. Blind by construction. The auditor received the triples file and
nothing else: no dossier, no registry, no receipt, no manifest, no reader identity. Each source was
acquired independently by an open route and each quote was matched mechanically against the acquired
text before any judgement was formed.

- Input: 50 triples, 18 distinct sources (all PMIDs).
- Scope per row: every labelled field that asserts something — model, lesion class, restoration mode,
  cells restored, timing relative to the stated onset, endpoint and its level, outcome grade,
  follow-up and comparator.
- Two questions per row: does the quote occur in the source and does *this* sentence carry *this*
  statement; and does the source say MORE or LESS than the labelled fields claim.

## Counts per verdict

| Verdict | Rows |
|---|---|
| SUPPORTED | 39 |
| OVERSHOOT | 6 |
| UNDERSHOOT | 3 |
| UNVERIFIABLE_SURFACE | 2 |
| NOT_IN_SOURCE | 0 |
| **Total** | **50** |

No row was absent from its source. 44 quotes matched exactly under whitespace and case
normalisation alone; 3 matched after one further character normalisation each (noted below); 1 is
present but not contiguous; 2 rows carry an attestation marker instead of a quote.

## Non-SUPPORTED rows, with the exact reason

### OVERSHOOT (6)

**R1b-R24 — PMID 39855191 — lesion class.** The quoted summary sentence is explicitly scoped to
females, and so is the endpoint. The source states that germline loss produces no behavioural
seizures in adult mice and that it is heterozygous females which develop them with aging. Naming
hemizygous males in the lesion field of a seizure row claims a model the source excludes for this
endpoint. Governing passage: Results, electrographic section, the sentence beginning *"germline loss
of CDKL5 does not result in behavioral seizures in adult mice"*.
Note, in the row's favour: the outcome grade `none` for the late arm is better supported than the
quoted summary word *"limited"* — the Results sentence for that figure states the decrease in spasm
number was not present in the late condition. The defect is the lesion field, not the grade.

**R1b-R25 — PMID 39855191 — follow-up.** The row claims follow-up to about ten months for four
behavioural endpoints. The source states the behavioural battery concluded at four to five months of
age, deliberately, to stay ahead of the age-dependent seizure phenotype; the ten-month timepoint
belongs to the separate video-recording seizure endpoint (which is row R1b-R24). Governing passage:
Results, first behavioural section, the sentence beginning *"these behavioral tests concluded when
the mice were four to five months of age"*.

**R1b-R90, R1b-R91, R1b-R92 — PMID 34135323 — lesion class (one defect, replicated three times).**
All three rows name both the cell-type-restricted haploinsufficiency *and* the knockout, with
outcome `full`. The in vivo pharmacological arm is haploinsufficient only: the treated animals are
the haploinsufficient conditional line and its genotype-matched littermate controls. The homozygous
condition was tested only in organotypic culture, where the source reports reversal of two measures
as partial and *no* significant effect on the proportion of innervation formed. Narrowing the lesion
field to haploinsufficiency for these three rows repairs all three at once. Governing passages:
Results, culture section, the sentence beginning *"in cultures from homozygous mutant mice, the same
rapamycin treatment only partially reversed"*; and Results, in vivo section, the sentence beginning
*"finally, we tested whether short-term rapamycin treatment"*.
R1b-R92 carries a second, smaller overshoot: its comparator field claims treatment windows were
compared, whereas the in vivo treatment is a single stated interval.

**R1b-R95 — PMID 32125365 — cells restored.** This row's endpoint *is* the distribution of transgene
expression achieved, and its own quote names hippocampal neurons and cerebellar Purkinje cells. The
abstract attributes neuron-plus-astrocyte transduction to a separate marker experiment in adult
wild-type animals used to compare two vector serotypes — which the row's own comparator field
correctly identifies. Carrying astrocytes into the cells-restored field of the row whose endpoint is
that very distribution conflicts with the row's quote. Governing passage: abstract, the sentence
beginning *"Intrajugular delivery of green fluorescence protein"*.

### UNDERSHOOT (3)

**R1b-R52 — PMID 18495876 — outcome grade.** The row grades the combined endpoint `none`. Three of
its four measures are indeed unchanged or non-significant: dysplasia and migration are reported
unchanged, and the spine-density change under treatment is explicitly non-significant. The fourth is
not: the source reports a statistically significant increase in spine length under treatment,
relative to *both* the untreated mutant and the control. A grade of `none` drops a significant
treatment effect that happens to run past the control value rather than toward it. Governing
passage: Results, spine-morphology figure and table, the clause reporting the significant increase
in spine length compared with both mutant and control.

**R1b-R74 — PMID 41997465 — outcome grade on a glia-classed row.** The quote is verbatim and the
molecular endpoint is indeed unchanged. But the abstract's next sentence reports *increased* levels
of marker co-expressing cells, and cells of altered morphology, in the same animals carrying the
transgene. On a row classed to glia with outcome `none`, that adjacent positive finding is the
source saying more than the row claims. Governing passage: abstract, the sentence beginning
*"However, we also find increased levels of Olig2 and GFAP co-expressing cells"*.

**R1b-R83 — PMID 34369389 — the level of the endpoint.** The row's endpoint is the restoration level
achieved in that treatment arm, stated as one range. The quote is a contiguous mid-sentence span,
which is acceptable as a surface matter, but the same sentence continues with two further regional
values — one far higher, one lower — so the level actually reached across the brain is wider than
the field states. Governing passage: Results, post-treatment expression paragraph, the continuation
of the quoted sentence giving the striatal and cerebellar values.

### UNVERIFIABLE_SURFACE (2)

Both are legitimate and are already declared as attestations in the triples file; neither is a
defect. Each was nevertheless checked against the source, and in both cases the attestation holds.

**R1b-R33 — PMID 34651584.** Quote field is `attestation_without_quote`, so there is nothing to
match. The row asserts that spine analyses were not performed in the restored arms. Verified: every
spine measurement in the source is made in the constitutive-knockin or the adult-deletion line, and
the abstract's restoration sentence names behaviour and receptor signalling but not spine
morphology.

**R1b-R49 — PMID 18389497.** Quote field is `attestation_without_quote`. The row asserts myelination
was not measured in either arm. Verified: no myelin measure of any kind appears anywhere in the
source — Methods, Results or figures.

## Surface observations that did not change a verdict

Recorded because they are locator hygiene, not claim defects.

- **R1b-R16 (PMID 31025938)** — the quote is present but **not contiguous**: an inline parenthetical
  statistic is dropped from the middle without an ellipsis. The statement is unaffected, and the
  row's reading of the design is correct — the two "phases" are the pre- and post-restoration
  recording sessions in the same animals, as the Methods state, so the within-animal framing and the
  genotype-without-phase result both hold.
- **R1b-R53 (PMID 22525157)** — the span is exact but begins immediately *after* the governing
  exception clause, so the quote standing alone reads as a stronger statement than the sentence
  makes. The proposition itself is narrower and correct, and the clipped exception is the subject of
  row R1b-R54, so nothing is lost at the batch level.
- **R1b-R04 (PMID 17289941)** — the quoted sentence is an explicitly introduced single-animal
  example; the arm-level statement sits one sentence earlier. Substantively supported either way.
- **R1b-R93 / R1b-R94 (PMID 32125365)** — these two rows carry the same astrocyte descriptor flagged
  under R1b-R95, but in their case the cells-restored field is contextual rather than the endpoint
  itself, and R1b-R95's comparator field states where the datum comes from. Graded SUPPORTED, listed
  here so the descriptor can be corrected across all three rows together.
- **R1b-R20 (PMID 22500629)** — checked specifically for the failure mode where "not reported"
  becomes "tested and found absent". It is not that: the source states in so many words that the
  locomotor measure *was* tested at the shorter duration and not corrected.

Normalisations needed, beyond whitespace and case:

| Row | Normalisation |
|---|---|
| R1b-R03 | whitespace inside a genotype label (comma spacing) |
| R1b-R57 | tilde operator to a plain tilde |
| R1b-R59 | en dash to a hyphen |
| R1b-R86 | a Greek letter that the quote renders as a Latin capital, plus spacing |

## Artefacts read

Digests are sha256, full length, computed from the file at emit time. No contact parameter and no
address of any kind was sent to any service on any request.

| PMID | Route | Bytes | sha256 |
|---|---|---|---|
| 17289941 | NCBI E-utilities efetch db=pmc, PMC7610836 | 45331 | `0b8108807542b9ee85bde8ef10b235d318d451d4607d64b15aeb67a8f8fa00fe` |
| 18389497 | PMC article HTML, PMC3937593 | 176422 | `e634ab626dbb31cb78a3426ac314edc34e4070032b406f5d51301eb200e836c6` |
| 18495876 | PMC article HTML, PMC2633923 | 236673 | `855fb917ede414a8e5b91c245052daff936a48cf52a65645bb1fb3d2c5e7431e` |
| 21716289 | NCBI E-utilities efetch db=pmc, PMC3268776 | 69481 | `23b46debcf1071abf3a785262c85ceef022619fd9abe32b1ed5f58f276aa89d5` |
| 22500629 | NCBI E-utilities efetch db=pmc, PMC8822597 | 91385 | `aeec8f2097e9debdd6a93eab9b3ed5a2067b707f09f9ad0dbb8798e0e874f3f4` |
| 22525157 | PMC article HTML, PMC3437019 | 226812 | `ffb59c09e33c76890883c7e32b11bc04f3bba3d833122c410ad647dc9fc82a94` |
| 24285883 | PMC article HTML, PMC3841446 | 201930 | `da87eee9ba838827ebf1da032d79dd27d8b977104ba3f82f97cfc66ae8076217` |
| 25866966 | PMC article HTML, PMC4463212 | 168508 | `28f1426863d52768f24905a67aa600b3082bb05efd8093608ee9bbdf50990857` |
| 26886798 | Europe PMC REST fullTextXML, PMC4898763 | 99357 | `86139db6a72b28ba960414c6bd9e20fb2e1421f8c8be0cee6cb7642f6bed6b00` |
| 30082419 | PMC article HTML, PMC6596147 | 326219 | `d5102bc8b9618a200f57e5db09cf057e61299e57ad2152b3c995be3f633342ac` |
| 31025938 | Europe PMC REST fullTextXML, PMC6504227 | 191392 | `33d35c64746afc90520f6ecb65ae12c86769ed26a266085e19d5f0e5b6538720` |
| 32125365 | NCBI E-utilities efetch db=pubmed, abstract | 12929 | `4a89902108e36ca55e2e2edcc9136408ddb85dc05db18c5827746e621dc39011` |
| 34135323 | Europe PMC REST fullTextXML, PMC8209106 | 199444 | `b71fe463d781bb85821b6facff7da4876b25ead35b8512c9362713a030b62eef` |
| 34369389 | Europe PMC REST fullTextXML, PMC8410092 | 90021 | `8053bc962f9482d15a257d37e057794afeb856ceafe43cd1b3b0f93981560bc1` |
| 34651584 | PMC article HTML, PMC8516470 | 242632 | `6242b905442e1bbb5524002b9d16e503b8fd182c941b4aec39ea572ab7e8c345` |
| 36594817 | Europe PMC REST fullTextXML, PMC9904759 | 288338 | `b437f0ffffd90a6258d68f6025f1ece8aa66938deccbb9875b0a0bf18bb41456` |
| 39855191 | Europe PMC REST fullTextXML, PMC11866500 | 196483 | `e0f7fa9c8b34dd1d59da323b396ede50f283a4472c5769d5fee2db30fec008a2` |
| 41997465 | NCBI E-utilities efetch db=pubmed, abstract | 10357 | `d5ac0f090e0664f84cf1139d646501e97c5ec1ce0cb6207daff5bc82a7b1f474` |

Route notes, for anyone repeating this:

- Europe PMC `fullTextXML` serves only the open-access records. For the eight non-open-access
  records in this set it answered HTTP 500, so those went to the other two routes.
- `efetch db=pmc` returned a complete body for three of them and a front-matter-only stub for the
  rest; the stubs were discarded rather than audited, and those records went to the PMC article HTML
  page, which carried the full body in every case.
- Two records have no PMC record at all (PMIDs 32125365 and 41997465). Both were audited at
  abstract level, which is what their rows are scoped to: the rows for 41997465 declare follow-up
  and comparator as not read, and the rows for 32125365 assert nothing below abstract level.
- One request met a transient HTTP 429 rate limit and succeeded on a single retry.

## Anything that could not be reached

**Nothing.** All 18 sources were reached and all 50 rows were adjudicated against a source artefact.

This includes the two records flagged in the brief as unreachable by an earlier auditor, PMIDs
18389497 and 18495876. Both carry rows R1b-R44 through R1b-R52. Neither is in the open-access subset,
so both fail the Europe PMC full-text route and return only front matter from `efetch db=pmc` — which
is the likely shape of the earlier failure. Both were obtained in full from the **PMC article HTML
page, HTTP 200**, with complete Results and figure legends. The nine rows resting on them were
audited on the full text, not marked `UNVERIFIABLE_SURFACE`: seven SUPPORTED, one UNDERSHOOT
(R1b-R52), one UNVERIFIABLE_SURFACE for the declared attestation that carries no quote (R1b-R49).

## Standing

This audit is READ-ONLY toward every canonical file. It produces a verdict per triple and no edit.
Per the skill: no `NOT_IN_SOURCE` means nothing here blocks the reading from touching canonical
state, but the six OVERSHOOT and three UNDERSHOOT rows must be answered before `BATCH_COMMIT` —
either the proposition is rewritten to what the source carries, or the divergence is argued
explicitly in the commit candidate. The three replicated lesion-field overshoots (R1b-R90 to
R1b-R92) and the replicated cells-restored descriptor (R1b-R93 to R1b-R95) are each one repair, not
three.

Nothing in this audit is clinical advice, and no clinical wording is drafted anywhere in it.
