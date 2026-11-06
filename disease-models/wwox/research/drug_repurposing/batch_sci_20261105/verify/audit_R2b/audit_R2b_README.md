# Blind locator audit — R2b

Thirty-four triples, fifteen named sources. The auditor received the triples file and nothing
else: no dossier, no registry, no receipt, no reader identity. Each source was acquired
independently from an open route and each quote was matched mechanically against the acquired
text before any judgement was formed.

## Counts per verdict

| Verdict | Rows |
|---|---|
| SUPPORTED | 27 |
| OVERSHOOT | 5 |
| UNDERSHOOT | 1 |
| NOT_IN_SOURCE | 0 |
| UNVERIFIABLE_SURFACE | 1 |
| **Total** | **34** |

Every quote in all thirty-four rows was located verbatim in its named source. There is no
`NOT_IN_SOURCE`, so no row blocks canonical state on that ground.

## Normalisation applied

Matching ran over tag-stripped text, NFKC-normalised, lowercased, with whitespace collapsed.
These substitutions were needed in practice:

- superscripts and subscripts rendered inline, so a genotype label printed with a raised
  allele name matches the flat spelling used in the triples;
- unicode dashes, the soft hyphen and the minus sign folded to a plain hyphen;
- the tilde operator and the "approximately" sign folded to a plain tilde;
- the plus-minus sign, the greater-or-equal and less-or-equal signs expanded to ASCII;
- Greek letters spelled out, which is what made the beta-subunit and the alpha-subunit
  sentences match;
- **the middle-dot decimal separator folded to a full stop** — without this, the follow-up
  figures in PMID 35065785 appear absent from a source that states them plainly;
- ligatures and the non-breaking, thin and hair spaces folded.

Three rows carry a section label before the quote (`Results:`, `Abstract:`,
`Figure 3 caption:`); the label was stripped before matching and is not treated as part of the
quote.

## Non-SUPPORTED rows, with the exact reason

### R2b-R19 — PMID 36173683 — OVERSHOOT

The quote is verbatim. The record grades the outcome `worse`, reading the fall in novel-arm
time in the normal-genotype arm as a cost of the intervention. The source reports a fall in a
median with **no statistical test stated** — unlike the two neighbouring sentences, where the
authors say explicitly that a difference did not reach significance — and the whole passage sits
under a section heading that concludes the opposite. Grading it `worse` asserts a harm the
authors do not.

*Governing pointer:* Results, section heading beginning "ASO-mediated Kcnt1 reduction in +/+
mice is well tolerated"; and, two sentences earlier, "this difference did not reach statistical
significance".

### R2b-R31 — PMID 32610343 — OVERSHOOT

The quote is verbatim in the Abstract and the myelin figures in the record (near half of the
normal genotype, incomplete compaction, endpoint at 18 months) are all correct. The defect is
in `comparator_and_controls`: it names the three control arms of the **oligonucleotide**
experiment for a row whose restoration mode is **germline** editing at the zygote stage. The
germline arm is compared only against the untreated mutant and the normal genotype; no
oligonucleotide control exists in it. The field claims a control design this arm does not have.

*Governing pointer:* Results, sentence beginning "While jimpy mice showed severe tremor, ataxia,
seizures".

### R2b-R45 — PMID 35065785 — OVERSHOOT

The quote is verbatim and the follow-up figures are exact. The defect is the timing field. The
record labels the row `pre_onset` and attributes the motor result at two and three years to
treatment before onset "in both disease subtypes". The source reports those differences for the
treated groups **overall**, and one of the two subtypes admitted children who were already
early-symptomatic at treatment; the paper separately stratifies that subtype by symptomatic
status. The quote says benefits were *particularly* apparent before onset, which is a comparison
within a mixed cohort, not a restriction to it.

*Governing pointer:* Methods, "Patients", sentence beginning "Eligible patients had a molecular
and biochemical diagnosis of MLD of either pre-symptomatic late-infantile or".

### R2b-R55 — PMID 28100454 — UNDERSHOOT

The rarer direction, and the reason this row is flagged rather than passed. The quote is
verbatim and the apoptosis magnitudes (about half of counted cells falling to about one in
twenty) are right. But the record declares the magnitude "a figure reading declared as an
attestation". It is not: the source reports these values **in the running prose**, with
dispersion and p values, and reports the macrophage counts the same way. Only the astrogliosis
statement is qualitative. Demoting a reported, tested quantity to a panel reading discards
evidential strength the source actually supplies — a silent narrowing of the kind this audit
exists to catch.

*Governing pointer:* Results, sentence beginning "while apoptotic oligodendrocytes were much
reduced in treated animals", and the macrophage count reported in the same paragraph.

### R2b-R74 — PMID 37149081 — OVERSHOOT

Minor, hedge-level. The improvement and the blunting in old animals are stated plainly. The
record then says the authors attribute the limit to neuronal rather than oligodendrocyte
recovery; the source hedges that attribution with "potentially due to". The hedge is dropped
from a causal claim.

*Governing pointer:* Abstract, sentence beginning "Also, this effect of ASPA re-expression is
blunted in old mice, potentially due to limited ability".

### R2b-R77 — PMID 23011033 — OVERSHOOT

The quote is verbatim; the age, the transduction range and the modest survival gain are all
stated. What is not stated anywhere in the available surface is that the model is **already
symptomatic** at that age — the record asserts it, and the `post_onset_early` label rests on it.
The abstract gives no onset statement for this model, so the timing field is carried by outside
knowledge rather than by the source. Only the abstract was reachable for this record, so the
finding is scoped to that surface.

*Governing pointer:* Abstract, sentence beginning "While the brain transduction efficiency in
juvenile mice was low".

### R2b-R43 — PMID 39847501 — UNVERIFIABLE_SURFACE

Not a defect; a correct declaration. The row asserts a **whole-document absence** — that no
myelin or glial endpoint was measured — and its quote, while verbatim in the Results, concerns
regional distribution instead. No single sentence can carry a negative of this shape, which the
row itself says. The absence was checked independently and holds: a term census over the whole
document returns **zero** occurrences of myelin-, oligodendrocyte- and myelin-basic-protein
terms, and the two glial markers appear once each, used only to show that the transgene was
*not* expressed in those cells — which is a specificity control, not a glial endpoint. The row
must stay declared as an attestation rather than a verified quote.

*Governing pointer:* Results, section beginning "Cellular and temporal specificity of
AAV-Navbeta1 expression in Scn1b-null mouse brain"; plus the term census over the whole
document.

## Observations recorded without a verdict change

These did not alter a verdict but belong in the record:

- **R2b-R41** anchors its quote to the Figure 3 caption. The sentence is there verbatim, and it
  carries the interneuron half of the claim; the pyramidal-neuron half is carried by the
  **identically worded** closing sentence of the Figure 4 caption. The anchor is incomplete, not
  wrong.
- **R2b-R58** quotes the lead-in clause of a sentence that stops before the result. The survival
  figures the row asserts are in the continuation of that same sentence, so the content holds,
  but the locator as cut carries no outcome on its own.
- **R2b-R28** bins an optic-nerve conduction-velocity result under `neuronal structure`. The
  numbers are exact; the bin describes an electrophysiological measure as a structural one.
- **R2b-R62** names both of the paper's models in `gene_model` although the result in the row
  was obtained in only one of them. The endpoint detail says "this model", so the row is
  self-consistent.
- **R2b-R78** states a comparison against the untreated normal genotype. The abstract does not
  name that arm; the comparison is presupposed by the sentence rather than stated.
- **R2b-R33** and **R2b-R75** describe the restoration mode as suppression of the
  mutant-bearing transcript. Both sources describe gene-level, not allele-level, selectivity.
  Neither row claims allele selectivity, so neither is flagged.

## Artefacts read

All downloads live outside the repository, in the session scratch folder
`audit_R2b/src/`. Hashes are sha256 over the file as fetched, computed at emit time.

| Source | Route | Bytes | sha256 |
|---|---|---|---|
| PMID 35013317 | Europe PMC REST fullTextXML, PMC8748984 | 187003 | `728dfa04be02f9a2b80f1a569fc0e0113af2f90669fa13626593f554327edc62` |
| PMID 36173683 | Europe PMC REST fullTextXML, PMC9746904 | 144514 | `6714d5fc7f5f1c056e68113bf7b9b6ecd87526a11c0ee70387423b5a1993a703` |
| PMID 32610343 | Europe PMC REST fullTextXML, PMC7810164 | 154697 | `f8374f8752df1ee987bc3de206ab4621fc6376007f35dbbace55d9fbe33c8b7f` |
| PMID 31943325 | Europe PMC REST fullTextXML, PMC7064908 | 79882 | `dddc9a6f01e0007086b4cecfe7714cea492e441628ba4d0960995568a29c4ce9` |
| PMID 39847501 | Europe PMC REST fullTextXML, PMC11870736 | 146693 | `61ab73c4264ebec5b1c1638187f4464007f89379899186eee573a6b8477a7986` |
| PMID 35065785 | Europe PMC REST fullTextXML, PMC8795071 | 117194 | `b7d3f944f3e19e3e2f6dc75da2a448ff293d946795c0ac23c1e2bb8007900cba` |
| PMID 35715566 | Europe PMC REST fullTextXML, PMC9205281 | 140419 | `06b73cf63373d2f82537cf452e221b7cd0faa98e55b4c7d6092e78245547dc5a` |
| PMID 37901435 | Europe PMC REST fullTextXML, PMC10603267 | 85881 | `3cc7aeb464ce512c7eb16842c977c998d88be247f9780b95fbee77cf62d2cf06` |
| PMID 40051162 | Europe PMC REST fullTextXML, PMC11997501 | 188801 | `24c026b3b3ab33949716e71a9d5352dfcf4f1aa5ca564df15450ee177607b4f7` |
| 15 abstracts, one request | NCBI E-utilities efetch, db=pubmed | 511316 | `c1fa942317cdf618d28b09b9a0c6828e97124f46b40ad83862c81e4409d18582` |
| PMID 41883162, abstract extract | derived from the above | 1743 | `0fa421b8a7148f0b20938837f18ee1e022f369e3b18cb07ae18f3e65039f8bd6` |
| PMID 23817205, abstract extract | derived from the above | 1476 | `76c220cfc3167c0f820ea733f8fffd8d5ea684c387693f43a9d0e90e82c43641` |
| PMID 37149081, abstract extract | derived from the above | 2006 | `1c04b31d8fec21139ba96140ba31ff13cb2ac6af3d0ea4082a36ae7a32c15db5` |
| PMID 41566774, abstract extract | derived from the above | 1665 | `4b1a3b32095d55d8ba963717e059d279579c0672983d167e2633f5d8f4b353a8` |
| PMID 23011033, abstract extract | derived from the above | 1641 | `0572d416bcd9ec8788d835d12896f649e84ee2d1062bdae4aa3bbe82d123d15a` |
| PMID 37149081, body | NCBI E-utilities efetch, db=pmc, three records in one request | 129389 | `fde1640e37a5236ec616c245beade4120364407477e8f5bf7491abcec95054d4` |
| PMID 28100454, front matter only | NCBI E-utilities efetch, db=pmc, PMC5837386 | 12206 | `597c705d59969a056626dd9e6d520125250b246baa68cfbfcc9926ac92bba973` |

No contact parameter and no address of any kind was sent to any service, on any request.

## What could not be reached

**PMID 28100454 — full text, as a file.** Four routes were tried.

1. Europe PMC REST `fullTextXML` for PMC5837386 returns HTTP 500 on repeat, although the record
   is indexed as present; the same endpoint returns 500 for PMC3863789 and PMC3536818 too.
2. NCBI `efetch db=pmc` returns the front matter with an explicit publisher note that the full
   text may not be downloaded in XML. That 12 KB file is what the hash above covers.
3. The publisher's own open file answers HTTP 403 behind a bot check.
4. The article page answers with a bot-check interstitial to a direct request.

No circumvention was attempted on any of these. The article page **was** readable through the
session's page-fetch tool, which is the route the brief names for exactly this case, and both
quotes in rows R2b-R55 and R2b-R58 were returned verbatim from it, together with the onset
statement, the quantified apoptosis and macrophage values, the age at administration and the
observation window. That tool returns rendered text rather than a file, so **no sha256 of the
full text exists for this record**; the hash recorded against those two rows is the front-matter
file from route 2, and the route column states the limitation. The two verdicts are sound, but
they rest on a rendered reading rather than on a hashed artefact — the one place in this audit
where that is true.

**PMID 41883162 and PMID 41566774** have no PMC record at all. Rows R2b-R65, R2b-R75 and
R2b-R76 quote the Abstract and were verified against it; nothing in those three rows needed a
surface the abstract does not carry, and each declares where the abstract is silent. The same
holds for the abstract-level rows of PMID 23817205 and PMID 23011033 — with the exception noted
for R2b-R77, where the timing field needs a statement the abstract does not make.
