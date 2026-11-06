# Blind locator audit — R1 (post-onset restoration triples)

Method: `.claude/skills/legend-locator-audit/SKILL.md`. Two mechanical questions per triple —
does the quote support the proposition, and does the source say MORE or LESS than the
proposition claims. Verdicts: `SUPPORTED` · `OVERSHOOT` · `UNDERSHOOT` · `NOT_IN_SOURCE` ·
`UNVERIFIABLE_SURFACE`. Read-only: this audit proposes nothing and edits nothing.

The auditor received the triples file and nothing else. No registry, dossier, receipt or
manifest for these papers was opened, and no file under `batch_sci_20261105/` was read. Every
source artefact was acquired independently by open route. No contact address or e-mail
parameter was sent to any service; no service that requires one was used.

Input: 62 triples, 16 distinct sources.
Triples snapshot sha256 `e6da2f752692287dc3024fe655807f767e4f78b958b1be2a188585fc0578ad85`.

## Counts per verdict

| Verdict | Count |
|---|---|
| SUPPORTED | 42 |
| OVERSHOOT | 6 |
| UNDERSHOOT | 6 |
| NOT_IN_SOURCE | **0** |
| UNVERIFIABLE_SURFACE | 8 |
| **Total** | **62** |

No `NOT_IN_SOURCE`: every quote that had a reachable text surface was found in its source, 53
under whitespace/case/punctuation normalisation alone and 1 (`R1-R64`) after additionally
removing an intra-token space in a genotype label. Two rows carry no quote by declaration, and
six rows belong to the two sources whose full text could not be reached.

## Non-SUPPORTED triples, with the exact reason

### OVERSHOOT — the proposition claims more than the source carries

**R1-R14** (PMID 31025938) — wild-type-level latency is reported for the **second (tonic-clonic)
stage only**. The adjacent sentences record a large residual effect size versus wild-type at the
first stage, and the figure statistics show no genotype effect at the third stage. The row's
endpoint field is plural ("seizure stages") with outcome `full`.
→ Full at the tonic-clonic stage; improvement over mutants without wild-type equivalence at the
first stage; no genotype effect at hind-limb extension.

**R1-R20** (PMID 22500629) — the quoted sentence is the authors' **specificity caveat**, not a
rescue result: for avoidance learning and locomotion the compound moved wild-type animals
proportionally too. The source also reports the locomotor correction present at the longer
treatment duration but **absent at the shorter one**. Neither qualification appears in the row,
whose outcome is `full`.
→ Cite the result sentence instead, and record both caveats.

**R1-R57** (PMID 24285883) — follow-up field says "to beyond 12 weeks"; the protein and thickness
measurements were made at **postnatal day 16**. The "beyond 12 weeks" window belongs to the
survival and phenotype-scoring time courses elsewhere in the paper. Separately, the endpoint
"myelin thickness" overstates what was measured: the thickness of **myelin basic protein
immunostaining** in the corpus callosum. The paper contains no electron microscopy (0 hits).

**R1-R58** (PMID 24285883) — quote verbatim and outcome `none` is right (proteolipid protein
remained aberrant; thickness did not differ between the two mutant groups), but the same two
defects apply: measurement at postnatal day 16, and immunostaining thickness rather than myelin
thickness.

**R1-R59** (PMID 24285883) — quote verbatim and the non-cell-autonomous interpretation is the
authors' own; the follow-up field is wrong for the same reason (data collected at postnatal
day 16).

**R1-R64** (PMID 21716289) — **locator mismatch.** The quote is found (after normalising genotype
spacing) but it reports the **overall observational symptom score**, not respiration. It sits in
a passage about survival, body size and health scoring and mentions neither breathing nor
apnoea. The row's endpoint, outcome and *both* follow-up figures match a different sentence in
the same section.
→ Replace the locator with: *"two months after TAM-treatment, the respiratory pattern in 10 of 12
Mecp2Stop/y-hGFAPcreT2 mice were within normal range"*, plus *"Two mice followed over the
subsequent five-month period maintained a regular breathing patterns"*.

### UNDERSHOOT — the source says more than the proposition claims

The skill names this the rarer and more dangerous direction: a narrowing nobody challenges
becomes a silent false negative. Six of them here.

**R1-R04** (PMID 17289941) — outcome `partial` for body weight. The source says obesity "was also
lost" and that the two features "were both reversed", with scores reverting at or close to
wild-type. No partiality qualifier attaches to weight.

**R1-R07** (PMID 26886798) — outcome `partial` for striatal spine density. The source reports
density increased versus knockouts and, in the next sentence, **significantly higher than
wild-type**. That is over-correction, not incomplete correction; `partial` misstates the
direction. (Cohort age 6–12 months and testing at least 6 weeks after treatment both confirmed.)

**R1-R22** (PMID 22500629) — outcome `none` with an endpoint field naming *both* arms. The single
quoted sentence reports **rescue when treatment began at birth**; only the 6-week start failed.
The row erases the positive arm. It is also a **second-hand account of a cited 2011 study**, not
data from the audited source, and does not declare that.
→ Split the row by arm and declare the provenance.

**R1-R25** (PMID 39855191) — outcome `partial` for a bundle of four endpoints, all four of which
the source reports as rescued in the six-week female arm (locomotor activity reduced to control
levels, sociability rescued, rotarod comparable to wild-type, clasping rescued). The quote's
exception is working memory, which this endpoint list does not contain. Worth carrying forward:
the no-tamoxifen leaky-Cre control also mitigated hyperactivity in one line.

**R1-R53** (PMID 22525157) — outcome `partial` for soma size, dendritic length and hippocampal
spine density. The source states that, cortical thickness excepted, all parameters were **not
significantly different from age-matched wild-type controls**, with a significant treatment
effect for exactly those three. The residual deficits are cortical thickness (its own row,
`R1-R55`) and dendritic complexity at 2 of 11 radii. Also: the source says about **70 % of
neurons**, where the row says 70 % of brain cells.

**R1-R54** (PMID 22525157) — outcome `partial` against a quoted summary sentence that asserts
**normalisation** of morphological changes. `partial` is carried only by adjacent caveats the row
does not name.

### UNVERIFIABLE_SURFACE

Two declared attestations (legitimate, and correctly carrying no quote):

- **R1-R33** (PMID 34651584) — `attestation_without_quote`, outcome `not_measured` for spine
  density/morphology in the restoration arms. **Consistent with the source**: spine measurements
  appear only for the adult-deletion arm; no occurrence of "spine" sits near any mention of the
  rescue group. Must stand as a declared attestation.
- **R1-R49** (PMID 18389497) — `attestation_without_quote`, outcome `not_measured` for
  myelination. Cannot be checked at all, because this source's full text is unreachable.

Six rows whose quotes are full-text sentences in a source whose full text could not be reached
(see below). These are **not** `NOT_IN_SOURCE`: the artefact is missing, not the sentence.

| Triple | Abstract-level corroboration available |
|---|---|
| R1-R44 | direction only — late treatment suppressed seizures and prolonged survival in animals that had already developed epilepsy; the denominator is unverified |
| R1-R45 | none — the abstract reports prolonged survival but says nothing about deaths during the treatment period |
| R1-R46 | direction only — astrogliosis and neuronal disorganisation inhibited, without separating arms or claiming incompleteness |
| R1-R47 | none — the abstract says nothing about withdrawal or dependence on continued treatment |
| R1-R48 | direction only — astrogliosis inhibited and brain size affected, but not restricted to the early arm and the two regions are not named |
| R1-R50 | the abstract says myelination was **improved**, not "effectively restored"; on that surface the outcome reads `partial`, not `full` |

## Notes on SUPPORTED rows worth carrying forward

These stay `SUPPORTED` but the integrator may want the detail:

- **R1-R16** (PMID 31025938) — outcome `none` is right, but the quoted sentence only establishes
  the deficit; the failure to improve is carried by the **next** sentence (no phase effect, no
  phase-by-genotype interaction). Suggest extending the locator.
- **R1-R24** (PMID 39855191) — the authors' word is "becomes limited", which is weaker than
  `none`; the `none` label rests on the separate statistical statement in `R1-R23`.
- **R1-R09** (PMID 26886798) — social preference is reported at wild-type level, but grooming is
  reported as significantly reduced versus knockouts **without** an explicit wild-type-level
  statement, so `full` is slightly strong for that component.
- **R1-R41** (PMID 30082419) — the outcome is verified in the abstract, but the induction age and
  the recording window are methods details absent from the only reachable surface and remain
  unverified.
- **R1-R05** (PMID 17289941) — the source says survivors "have survived for 15 months"; the row
  says "over 15 months".
- **R1-R74** (PMID 41997465) — the source hedges ("molecular experiments suggest that"), though
  the title asserts the negative outright.

## Artefacts read

All downloads were saved outside the repository, in this session's scratchpad folder
`…/scratchpad/audit_R1/`. sha256 is of the downloaded bytes, at full length.

| Source | Route | Bytes | sha256 |
|---|---|---|---|
| PMID 17289941 | NCBI efetch db=pmc PMC7610836 (JATS XML, full body) | 45331 | `0b8108807542b9ee85bde8ef10b235d318d451d4607d64b15aeb67a8f8fa00fe` |
| PMID 26886798 | Europe PMC REST fullTextXML PMC4898763 | 99357 | `86139db6a72b28ba960414c6bd9e20fb2e1421f8c8be0cee6cb7642f6bed6b00` |
| PMID 31025938 | Europe PMC REST fullTextXML PMC6504227 | 191392 | `33d35c64746afc90520f6ecb65ae12c86769ed26a266085e19d5f0e5b6538720` |
| PMID 22500629 | NCBI efetch db=pmc PMC8822597 (JATS XML, full body) | 91385 | `aeec8f2097e9debdd6a93eab9b3ed5a2067b707f09f9ad0dbb8798e0e874f3f4` |
| PMID 39855191 | Europe PMC REST fullTextXML PMC11866500 | 196483 | `e0f7fa9c8b34dd1d59da323b396ede50f283a4472c5769d5fee2db30fec008a2` |
| PMID 34651584 | publisher open-access HTML `jci.org/articles/view/143655` | 194059 | `d8fddc3ff18a212611922006249705a75d65b11a60747e3872943be1352737c7` |
| PMID 25866966 | publisher open-access HTML `jci.org/articles/view/80554` | 115213 | `8fe1b1b5d83d5dcb83b6b9b7cdc29a52ea4bc6def76c07a2eb790ff73d80a22a` |
| PMID 30082419 | NCBI efetch db=pubmed (abstract + significance statement) | 54724 | `9cac3f8cda675b50f734db3bdd7f02bd995367cc7b31afbf31f5287228c979a7` |
| PMID 22525157 | PMC article HTML `pmc.ncbi.nlm.nih.gov/articles/PMC3437019` | 226812 | `b0de349824d3e4ff76953b42c7bf9f30925871ccb2644cb5f39a74aca80be630` |
| PMID 24285883 | PMC article HTML `pmc.ncbi.nlm.nih.gov/articles/PMC3841446` | 201930 | `72bb8f3ca09969b60f59530d701f25477ad5c51acf8cb77510d1f497351a2447` |
| PMID 21716289 | NCBI efetch db=pmc PMC3268776 (JATS XML, full body) | 69481 | `23b46debcf1071abf3a785262c85ceef022619fd9abe32b1ed5f58f276aa89d5` |
| PMID 35535852 | Europe PMC REST fullTextXML PMC9090324 | 237716 | `aae95060fb82302125c771fcdf71481ae5028f2cbd07082c2c32682dd085a290` |
| PMID 41509287 | Europe PMC REST fullTextXML PMC12776099 | 161346 | `7896832383287dc199b6e6eb7826274d073b04f1284d79a5d3c9d8b5d4671f88` |
| PMID 41997465 | NCBI efetch db=pubmed (abstract only; not in PMC) | 10357 | `d5ac0f090e0664f84cf1139d646501e97c5ec1ce0cb6207daff5bc82a7b1f474` |
| PMID 18389497 | NCBI efetch db=pubmed (**abstract only** — full text unreachable) | 18418 | `836e130e445494326b1e639e051f6263bb6bbe84ac88eb78b89b589c11a575b3` |
| PMID 18495876 | NCBI efetch db=pubmed (**abstract only** — full text unreachable) | 28343 | `64291f7324897784bb0c2e72368a6854851193d37feda014537d993b5ac6d0ce` |

Also retained, as evidence that the PMC XML route returns metadata without a body for the
author-manuscript records: `ncbi_18389497_PMC3937593.xml`
(`a5ec401428a66b537c41e6fa9597b32d2c64ca11f1d031d7ad1dc223e1428d26`),
`ncbi_18495876_PMC2633923.xml` (`198b4ae9dd8e2b7720a31aed1d680366890c5eadbbcebcd79431b88ede3ef326`),
`ncbi_22525157_PMC3437019.xml` (`7b592d6d8d8940f04f5556425728e9388a0fb9d699140bd767a1d0bd2990c3c4`),
`ncbi_24285883_PMC3841446.xml` (`018cbe38d542650d8acc8386e0357cd1e30b10d5b39d5c3986e80f31b0209ef4`),
`ncbi_25866966_PMC4463212.xml` (`806a74527f53986ba6237ff9b6cd012fd78f73b56ca53c369a9194b8541f931e`),
`ncbi_30082419_PMC6596147.xml` (`5589842137e44e5b25c3f425eabadaa0f1f44e3ccd68f45788608b20613c6cc2`),
`ncbi_34651584_PMC8516470.xml` (`07fc74e02dd3dfa471be7178fc7447393876378050422b7c38a9d228c26a776e`).

## What could not be reached

**PMID 18389497 — full text (6 triples: R1-R44 … R1-R49).**
**PMID 18495876 — full text (1 triple: R1-R50).**

Routes attempted, in order, for both:

1. Europe PMC REST `fullTextXML` for the PMC record → HTTP 500 (restricted author manuscript),
   although the Europe PMC search record reports `inEPMC=Y`.
2. NCBI E-utilities `efetch db=pmc` → metadata only, **no `<body>` element**.
3. PMC article HTML → HTTP 200 but the body is a **bot-check interstitial**, not the article.
   Reported as unreachable; not worked around.
4. Europe PMC rendered PDF (`?pdf=render`, listed as "Free" in the record's own
   `fullTextUrlList`) → HTTP 403 bot check.
5. PMC OAI-PMH `GetRecord` with `metadataPrefix=pmc` → `cannotDisseminateFormat`.
6. Publisher pages, including the open PDF that OpenAlex lists as the best OA location for
   PMID 18495876 (free after 6 months) → HTTP 403 bot check.
7. Europe PMC annotations API → annotations exist for **title and abstract only**; no full-text
   sentence surface.

Deliberately not used: any service that requires a contact address or e-mail parameter.

For these seven triples the abstract was acquired and used as the only available surface. The
quotes are full-text sentences and are absent from it, so they are recorded as
`UNVERIFIABLE_SURFACE` with the reason, **not** as `NOT_IN_SOURCE` — an all-unverifiable block
means the artefact is missing, not that the reading is unsupported. Re-acquire both full texts
and re-run the audit over those seven rows.

## Shared-scratchpad re-run

Mid-audit the Orchestrator reported that several verifiers share one scratchpad root and that a
matcher script there had been overwritten by another auditor. The flattening and matching
scripts and the derived plain text had indeed been written to the shared root. All of it was
rebuilt inside this audit's own folder (`audit_R1/tools/`, `audit_R1/txt/`) and re-run from
there:

- all 23 downloaded artefacts re-hashed → **every sha256 unchanged**;
- the triples input snapshotted and hashed into the audit folder;
- all 62 triples re-matched → **every match status reproduced identically**
  (53 exact under whitespace/case/punctuation normalisation, 1 after genotype respacing,
  2 no-quote rows, 6 with no reachable surface);
- the context windows behind all 12 judgement-based verdicts re-read from the freshly
  regenerated text → all confirmed.

The shared root was left untouched rather than cleaned, so that no peer's in-flight work could
be destroyed; nothing in it was used to produce this audit.

---

Not medical advice. No dose, schedule, route or preparation appears anywhere in this audit or
in `audit_R1.tsv`; where a source sentence carried one, the quotation was shortened.
