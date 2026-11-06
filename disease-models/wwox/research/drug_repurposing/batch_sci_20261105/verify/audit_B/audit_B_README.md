# Blind locator audit — package B

Mechanical audit of 38 `(proposition, quote, anchor)` triples from `triples_B.tsv`, against sources
acquired independently by the auditor. The auditor held no dossier, no registry, no receipt, no
manifest, no reader identity and no conclusions: only the triples file and the method in
`legend-locator-audit`. Both audit questions were answered per triple — does this quote carry this
proposition, and does the source say more or less than the proposition claims.

Nothing here is medical advice. No amount, schedule, administration route or preparation is recorded
anywhere in this audit, including inside quoted material.

## Counts per verdict

| Verdict | n |
|---|---|
| SUPPORTED | 25 |
| OVERSHOOT | 9 |
| UNDERSHOOT | 2 |
| NOT_IN_SOURCE | 0 |
| UNVERIFIABLE_SURFACE | 2 |
| **Total** | **38** |

**Every one of the 36 quoted triples was located in its source.** 35 matched exactly after
whitespace, case, dash, ligature and Greek-letter normalisation; one (B1-35) needed punctuation
normalisation only. There is no `NOT_IN_SOURCE`, so nothing in this package is blocked from
canonical state on locator grounds. The 11 over- and undershoots are all element-level and all
repairable by rewording; eight of the nine overshoots leave the central finding of the row intact.

## Non-SUPPORTED triples, with the exact reason

### OVERSHOOT (9)

**B1-B1-03 — PMID36601084.** Locator mismatch. The quote, *"VABAM may occur even at the conventional
dosage of VGB"*, is a Highlights/Conclusion sentence about occurrence at a conventional amount; it
does not carry the asserted result that peak amount, cumulative amount and days of exposure were
each unassociated. The substance is correct: Table 3 gives all three non-significant on univariate
regression, and Table 1 gives the longer exposure and lower rate in the tuberous sclerosis group.
Repair is re-anchoring, not rewriting the finding.

**B1-B1-14 — PMID37690269.** Population overshoot. The proposition says *"43 children imaged before,
during and after exposure."* The source reports examinations of 43 as 13 before initiation, 18 during
treatment and 12 after discontinuation — the counts sum to 43, so these are not 43 children each
imaged at three time points. This matters because the reversibility element rests on the 12 examined
after stopping, not on 43. The row's own wording *"complete resolution … in several regions"* is
otherwise careful and correct: resolution was complete in all cases only in some regions, and
notably not in the thalami.

**B1-B1-15 — PMID23789722.** Two additions. (i) The reversibility list presents four outcomes as
resolutions, but the source says one case *"had improvement on withdrawing"* — improvement, not
resolution. (ii) The proposition states the typical changes appeared *"in 2 of those 8"*; the source
says only *"were noted in two infants"* and gives no denominator. The separate *"two out of eight"*
in the source's interpretation refers to causal plausibility, not to imaging, so the denominator
looks transferred from a different sentence. The headline element — imaging changes not specifically
related to the movement disorder, 2 cases versus 3 of 10 comparison infants — is exact.

**B1-B1-17 — PMID35183975.** Co-factor relabelled. The source describes the two cases with the
finding as very-low-birth-weight preterm infants with post-haemorrhagic hydrocephalus. The
proposition records *"pre-existing haemorrhagic white-matter injury."* Hydrocephalus following
haemorrhage is not a white-matter injury, and in a white-matter package that upgrade is
load-bearing. Both GABA comparisons and all denominators are exact.

**B1-B1-19 — PMID42033488.** Locator mismatch. The pasted quote is the *"Additional findings"*
sentence (delayed myelination, mild callosal hypoplasia, focal hypoperfusion). It does not carry the
asserted deep-grey and brainstem endpoint. Every asserted element — the bilateral symmetric
involvement by region, mild dentate change without diffusion restriction, onset during febrile focal
status epilepticus, absence of a lactate peak, and complete resolution without residual change eight
months after gradual discontinuation — verifies in the immediately preceding sentences, the
Discussion and the figure captions.

**B1-B1-20 — PMID42355787.** The most substantive finding in this package. The proposition's
reversibility element attributes complete resolution of the movement disorder and the imaging to the
vigabatrin change. The case body reports that vigabatrin was stopped and that steroid pulses plus
antimicrobial and antiviral treatment ran concurrently, and the Discussion states explicitly that it
is impossible to say whether the changes would have resolved without the steroid, adding that this
approach cannot be recommended. A reversibility claim built on this row therefore rests on an
uncontrolled co-intervention the authors themselves flagged. Two further defects: the exposure window
is given as *"from four to eight months of age"*, but four months is the epilepsy onset — exposure
began when the spasms syndrome was recognised, at about six and a half months; and the abstract's
*"strategic reduction"* (which the row follows) is contradicted by the body's *"Vigabatrin was
discontinued"*, an internal inconsistency in the source worth recording either way.

**B1-B1-22 — PMID1940119.** The timing element asserts *"not infants."* This abstract-level source
reports no ages at all; it describes only refractory epilepsy before neurosurgery or death on
long-term treatment. The inference is probably sound for a 1991 surgical cohort, but it is the
reader's, not the source's — and it is the element that decides whether this human negative bears on
the immature-brain animal findings. The three negative findings and both counts (62 treated, ten
untreated comparison cases) are exact.

**B1-B1-25 — PMID15150739.** The species element asserts *"rat, adult … first exposure adult."* The
abstract states neither age nor developmental stage, only littermate controls. Compare B1-26 and
B1-27, where the same reader correctly wrote *"not stated as immature"* — the convention exists and
was not applied here. Every experimental element, including the incomplete resolution of
microvacuolation after the twelve-week recovery phase, is exact.

**B1-B1-29 — PMID23194644.** Exposure timing mis-attributed. The proposition's timing element reads
*"first exposure adult, from day 3 of the model onward."* In the source, day 3 onward is the schedule
of the **exogenous GABA** arm, which aggravated disease; no timing is reported for the vigabatrin
arm, whose effect is described only as prophylactic as well as therapeutic. The animals' age is not
stated either. The two directional findings — aggravation by exogenous GABA, benefit from raising
endogenous GABA — are exact. The quote is also a verb-less fragment, cut before its predicate.

### UNDERSHOOT (2)

**B1-B1-06 — PMID36601084.** The symptom breakdown records *"movement disorder in seven."* The source
says seven had movement disorder **alone**, and three more had motor plus non-motor symptoms — so
ten of the thirteen symptomatic cases had a movement disorder. The row uses totals for the other two
symptom classes (five, one) but the alone-count for movement disorder, which silently understates the
most frequent symptom by three cases. The 13/38 and 25/38 split and the co-factor element (hormonal
and topiramate co-therapy significant univariately only) are exact.

**B1-B1-23 — PMID10840396.** The recovery element records *"MRI normal and microvacuolation gone, but
myelination recovered only partially and behaviour remained abnormal."* The source's recovery list
has a fourth item the row omits: T2 relaxation time **remained elevated in the hypothalamus**. The
row asserts normal imaging while dropping the one reported persistent imaging abnormality — the
classic silent narrowing, and material to any claim about how completely the immature-brain changes
reverse.

### UNVERIFIABLE_SURFACE (2)

**B1-B1-37 and B1-B1-38 — `bounded_null_search`.** The quote field is `no_quote_bounded_null`. These
are bounded-search results, not sources, so there is no sentence to match and no artefact to hash.
Per the audit brief no search of the auditor's own was run for either. Both are legitimate, and both
must be **declared as attestations** carrying their query set and date, never counted as verified
quotes.

## Notes recorded on SUPPORTED rows

These did not change a verdict but belong in the record:

- **B1-01** — the source calls discontinuation the *major* therapeutic strategy, not the only
  management; as a statement about what the article names, the row holds. Group figures are medians
  with interquartile ranges, not means.
- **B1-02** — the quote is a Discussion-level summary; the univariate half of the element is carried
  by the Table 3 rows named in the row's own anchor.
- **B1-08, B1-29** — quotes truncated before their predicates; extend them so each locator carries
  its own verb.
- **B1-18** — the anisotropy rise after stopping was measured in 6 of the 11 in that group, with one
  of the two values at p = 0.050; and *"9 days to 22 months"* is the cohort's age span, while
  reported exposure start ran 9 days to about 20 months.
- **B1-21** — *"the earliest human exposure window found"* is a claim about the reader's corpus, not
  about this source, and is not checkable here.
- **B1-27** — the abstract does not say in which of the three species vacuolation was seen, so
  *"across species"* must not be read as *"in all three"*. A companion abstract in this same set
  (PMID1940119) reports the change in rodents and dogs but not primates.
- **B1-30** — the gamma-hydroxybutyrate correlation (R = -0.683) is slightly weaker than the GABA one
  (R = -0.722); their inseparability is the reader's inference, not a statement by the authors.
- **B1-33** — *"myelin"* and *"MRI"* occur nowhere in that article; *"white matter"* occurs once, in
  the introduction's background on vigabatrin. The row's wording (*no such endpoint*) is exact, which
  a looser wording (*no mention*) would not have been.
- **B1-34** — zero occurrences of myelin, vacuolation, white matter or intramyelinic in either full
  text, so the row's negative holds for the main texts; supplementary files were not held, and the
  Methods of PMID34617595 point to a Supplement. The second article's mice were 5 to 11 weeks old,
  and only its electroencephalography cohort is called adult.
- **B1-35** — the quote matched only after punctuation normalisation: the source wraps the phrase
  *VABAM-like MRI abnormalities not VGB-related* in quotation marks, which the triple drops.

## Artefacts read

All acquired by the auditor from open routes, saved outside the repository, and digested in full. No
contact address and no e-mail parameter was sent to any service, and no service requiring one was
used.

| PMID | Route | Bytes | sha256 |
|---|---|---|---|
| 36601084 | Europe PMC REST fullTextXML (PMC9806385) | 130472 | `fc7239945736952175610aa28e3c6b54e0a9f41eb05b5dceedb20a9c9fd278f3` |
| 40670421 | Europe PMC REST fullTextXML (PMC12267420) | 99799 | `df2f1db7425b25c921ccdeb95368ad2ff33d94d2bd44163f3e257c885fdacf34` |
| 42033488 | Europe PMC REST fullTextXML (PMC13357445) | 36816 | `6d81ab30859a5cd911667130bedfda4c5a803abff0ffb1cafae45fb3e138a8ab` |
| 42355787 | Europe PMC REST fullTextXML (PMC13300765) | 137497 | `3b6142fdf3b7bb22d032d78862f85c2cf20e8a4b51e979e14dc2e10964a49769` |
| 40741980 | Europe PMC REST fullTextXML (PMC12623846) | 191349 | `45462833148e7d0fd961d87d0a9c6ea6896dc349f6fb040c5da446551f087d83` |
| 38937107 | Europe PMC REST fullTextXML (PMC11236575) | 132501 | `c19f4b7013de8e0a94d4a57b570b4c13265492f8a63603b690955f575756caff` |
| 39641935 | Europe PMC REST fullTextXML (PMC11827727) | 125545 | `391016fa02ee6fc5ea4010e58ceccff58981b20d267de9e3ba769987da42a491` |
| 39570186 | Europe PMC REST fullTextXML (PMC11803263) | 68384 | `df1556afdb926e3b62fdc625b032a5a709aeea28df3c8539daebf1e04c436310` |
| 22128851 | NCBI E-utilities efetch db=pmc (PMC3257419) | 140055 | `4855497efc0154e6ac308d255643acfac0c03f8d83a5dfd3e8a1b9c810618362` |
| 24321005 | NCBI E-utilities efetch db=pmc (PMC4102583) | 79403 | `cd48e0f125a467c66a64a2fb68bf26600b4581008e3fc7cd4b7887cfd31c6137` |
| 34617595 | NCBI E-utilities efetch db=pmc (PMC8639636) | 101760 | `e7d236fde9815d6f37e25a78182b1dfb22da81803d05d13e7a0add4d34899078` |
| 40527948 | NCBI E-utilities efetch db=pubmed (abstract of record) | 15264 | `9930c69bdc97f35486e22408e579d0831000829cb032b7f0ed0e4db1e44da045` |
| 42735667 | NCBI E-utilities efetch db=pubmed (abstract of record) | 9142 | `be05335bab10c41698b9b8cf35496042e0297152de9b6adb6fc65e3fa9aa9b22` |
| 28230253 | NCBI E-utilities efetch db=pubmed (abstract of record) | 9635 | `fdf6d4af6e301144e9d3775a3266f949ba514b9168fe8c7f7c8578219b56f624` |
| 34786694 | NCBI E-utilities efetch db=pubmed (abstract of record) | 15422 | `5907ac902ceb0b4dd7d8242bc678e5e6304a40c767559d2e40fb62fcb0feab8a` |
| 37690269 | NCBI E-utilities efetch db=pubmed (abstract of record) | 9545 | `4f3f857e873acbc667f680fba6741d3d363b2b5dffcdbaf94103fb014a1e80e3` |
| 23789722 | NCBI E-utilities efetch db=pubmed (abstract of record) | 9532 | `d925f4c352e7c4a1eeee690855a1dcbe564594133f2c463c3575d5e4c20b192a` |
| 35180571 | NCBI E-utilities efetch db=pubmed (abstract of record) | 9713 | `4c741b81401fad4714ef21474eab674eb6f94ae5d305f61c2220c17f2ae08d82` |
| 35183975 | NCBI E-utilities efetch db=pubmed (abstract of record) | 10131 | `e042e45406e45478add264741b72684b8125aa1c816c19bfb03c725fdf4b9b7b` |
| 7788110 | NCBI E-utilities efetch db=pubmed (abstract of record) | 6767 | `20aad6fcde4655605fbbabdbb1883a2bd171496a73c90ba7409a6a3321959c7d` |
| 1940119 | NCBI E-utilities efetch db=pubmed (abstract of record) | 6980 | `7203f74660c47cda451fef524056f23917d0df2a452b43c7c8346e5f01b83fd3` |
| 10840396 | NCBI E-utilities efetch db=pubmed (abstract of record) | 7431 | `88ef169abb05e4a44e6507103f99fb8aa921360c52604833d351ba0b0843d9a7` |
| 9168839 | NCBI E-utilities efetch db=pubmed (abstract of record) | 7958 | `615519c83ace85a93cb4256102371eb8b3895f9fad06c03db09020fd7753b2e7` |
| 15150739 | NCBI E-utilities efetch db=pubmed (abstract of record) | 6327 | `a8208cdc706afc308903b94be1511b1e96631027e51f0b77686397eb85ac9fb5` |
| 3616399 | NCBI E-utilities efetch db=pubmed (abstract of record) | 6428 | `232982b01359a777613df44d933fe31bc14fff4509c05b1a7775af7abab95271` |
| 2767014 | NCBI E-utilities efetch db=pubmed (abstract of record) | 4742 | `01e57c98672dc8b44e3c1b6b926bd4f25546977f46350dafbf197f33dd87f8c7` |
| 2757909 | NCBI E-utilities efetch db=pubmed (abstract of record) | 8081 | `506b43209924a079ede072adcf8da18bd1668ee566357676a8e21e9790294214` |
| 23194644 | NCBI E-utilities efetch db=pubmed (abstract of record) | 8015 | `035ca0f12a5f1c4284e82b2e0503aeae04db8d29b23ea90f492792ff1195119c` |
| 27376954 | NCBI E-utilities efetch db=pubmed (abstract of record) | 10235 | `4565a519e05c69d77b296682efb6215abaf9f98bec6badf695a6d7e72fbda9bc` |

Also fetched and retained but not used for a verdict: the Europe PMC core record for every PMID (OA
status and identifier resolution), the PubMed abstract for the eleven records whose full text was
obtained, and `efetch_pmc_2757909_PMC1379679.xml` (6574 bytes, sha256
`4aca47018ee64fbbe77601fd6aa947c6938fdadeff13e0e173bba31337b9aee0`), a stub record for a 1989 article
whose row is abstract-level in any case.

## What could not be reached

- **Europe PMC `fullTextXML` returned HTTP 500 for four non-open-access PMC records** —
  PMC3257419, PMC4102583, PMC8639636 and PMC1379679. Three were recovered in full through NCBI
  `efetch db=pmc`, so B1-32, B1-33 and B1-34 are full-text verdicts. The fourth (PMC1379679) yielded
  only a stub; B1-28 is abstract-level by its own declaration and was verified against the PubMed
  abstract of record.
- **Supplementary files were not held for any source.** This bounds three rows. B1-34's negative
  ("no myelin, vacuolation, white-matter or intramyelinic endpoint") is verified for the two main
  texts, while PMID34617595's Methods point to a Supplement for the histological detail. B1-06's
  univariate symptomatic analysis is reported in the running text that was verified, with the
  underlying tables supplementary. B1-35's symptom table is likewise supplementary.
- **Eighteen rows rest on abstracts** because the articles are not in PMC (PMIDs 40527948, 42735667,
  28230253, 34786694, 37690269, 23789722, 35180571, 35183975, 7788110, 1940119, 10840396, 9168839,
  15150739, 3616399, 2767014, 2757909, 23194644, 27376954). Each of those triples declares
  "(Abstract)" in its own source field, so this is a bound on the reading, not a defect in it — but
  it is precisely why B1-22 and B1-25 are overshoots: both assert a population age that an abstract
  does not carry.
- Nothing else was unreachable. No source in the triples file failed acquisition.

## Provenance of this audit

Sources, extraction tooling and intermediates all live under the auditor's own scratchpad folder
(`audit_B/`, with scripts in `audit_B/_scripts/`), never in the shared scratchpad root. A matcher
belonging to another verifier exists at the scratchpad root; it was never imported or executed here —
every run used `python3 -I` with `sys.path` pinned to the auditor's own folder. After the
Orchestrator's warning about the shared root, the full 38-triple match was re-run from the auditor's
own folder and reproduced identically (35 exact, 1 punctuation-normalised, 2 with no quote), and all
29 artefact digests were re-verified unchanged. One digest transcription slip was caught in that
recheck, after which every digest in these deliverables is computed from the artefact at emit time
rather than transcribed.
