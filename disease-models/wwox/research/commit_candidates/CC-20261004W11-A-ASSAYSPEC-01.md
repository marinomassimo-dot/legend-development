# CC-20261004W11-A-ASSAYSPEC-01 — the assay specification the WWOX WW/SDR binding question needs, taken from an adjacent tandem-WW paper

`context_policy: SOURCE_FIRST`. **Author:** ACTOR_ID `scientist`, Scientist A of intake wave 11,
2026-10-04. **Source:** PMID 38719828, receipt `FTR-20261004-38719828-01`, manifest
`deepdive_manifests/PMID38719828.json` (9 locators, strict PASS, 0 gaps).
**Change class: MINOR** — it proposes one new, explicitly method-only lead and changes no claim.
**Nothing here is medical advice.**

## 1 · The transfer limit, stated before the content

WWOX occurs **three times** in this source, all inside one Discussion sentence and its reference; the
paper performs **no WWOX experiment**. Its WWOX citation points at PMID 22634283, which this
laboratory already holds with a `complete_fulltext_read` receipt. **Nothing numeric transfers.** What
transfers is the *shape of an experiment* and one *field-level baseline*, and it transfers to the WW
domains only — the paper never touches an SDR domain of any protein.

## 2 · What the source gives

A structural-biology group determines, on purified protein, what a tandem WW pair binds, how tightly,
with what stoichiometry, and whether a proposed regulatory mechanism is causal. Six elements of its
design answer questions the WWOX literature currently answers by annotation:

| Question | How this source answers it | How the WWOX chain currently answers it |
|---|---|---|
| Where does the domain start and end? | By showing that a previously published tandem structure was built on a truncated construct and is inconsistent with new SAXS and RDC data | By sequence annotation |
| Are the two domains coupled or independent? | By relaxation, RDC and PRE measurements | By assertion, and by a chaperoning proposal cited from one 2012 paper |
| How tight is the interaction, with what stoichiometry? | By ITC on purified protein, at least in duplicate, buffer and temperature stated | For the SDR: not at all |
| Is the regulatory mechanism causal? | By mutating the motif and recovering the lost affinity | — |
| Does it hold in a cell? | By IP-MS against a mutated-construct control | — |
| Is the interpretation robust? | Two orthogonal solution techniques must agree | One laboratory, one format |

The field baseline it states is directly usable: an isolated WW domain binding a proline-rich peptide
is "typically in the range of hundreds of micromolar". Any WWOX WW affinity should be read against
that scale, not against an intuition of what "binds" means.

And one caution the source supplies against the corpus's own habit: the intra-tandem **chaperoning**
idea that the WWOX literature treats as settled was tested here for PRPF40A and **failed** — "our
data demonstrate that WW2 can be folded independently of WW1". The analogy is a hypothesis in both
directions.

## 3 · Proposed op (append-only)

- **file** `disease-models/wwox/research/discovery_ledger_current.md`
- **record** new lead `DL-MECH-NNN` in the section `MECH — indizi meccanicistici (aghi nel pagliaio)`
  (the integrator assigns the next free number)
- **op** append
- **new** (content, not formatting):
  > **DL-MECH-NNN — Assay specification for any future WWOX domain-binding measurement (method-only lead; no WWOX datum).** Status: open · Tag: **ESPANSIONE** (a method imported from an adjacent literature; nothing about WWOX is measured here) · Source: PMID 38719828 (Helmholtz Munich / TUM, receipt `FTR-20261004-38719828-01`), in which WWOX occurs three times, all in one Discussion citation of PMID 22634283, and no WWOX experiment is performed · **What it specifies:** a WWOX WW-domain or SDR-region binding claim should be supported by (1) a construct whose boundaries are justified by data rather than by annotation — a published tandem structure in that paper was wrong because it was truncated; (2) affinity and stoichiometry by ITC on purified protein, with buffer, temperature and replication stated; (3) a test of whether the two domains are coupled or independent, by relaxation/RDC/PRE rather than by assertion; (4) a causal mutant that removes the proposed determinant and restores the behaviour it was said to suppress; (5) a cellular check against a mutated-construct control, not against an untagged control alone; (6) agreement between two orthogonal techniques before a structural interpretation is believed · **Baseline to read any WWOX number against:** an isolated WW domain binding a proline-rich peptide is typically hundreds of micromolar · **Caution it supplies:** the intra-tandem chaperoning idea attributed to WWOX's WW pair failed when tested for PRPF40A, whose WW2 folds independently of WW1 — the analogy is a hypothesis in both directions · **Transfer limit:** this is assay design only. No affinity, residue, motif or conclusion of that paper applies to WWOX, and the paper touches no SDR domain of any protein. No WWOX allele is involved and nothing transfers across P47T, Q230P, G372R, A141T or P252A.

## 4 · What must NOT be written from this source

- Not a WWOX affinity, a WWOX Kd or a WWOX stoichiometry — none is measured anywhere in it.
- Not "WWOX is autoinhibited": WWOX is explicitly absent from the authors' own list of WW-tandem
  proteins that may be, and their generalisation is stated as needing further analysis.
- Nothing about the SDR domain, which the source never discusses.

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

The only WWOX content in this source is a Discussion citation of an intra-tandem chaperoning interpretation; the paper performs no WWOX experiment. | the presence of one WW domain may have a chaperone activity for the other, promoting its folding, as in the case of WW domains of WWOX | Discussion, Structure of PRPF40A tandem WW domains and proline-rich peptide recognition — files/fulltext/PMID38719828_MartinezLumbreras2024_PMC.xml

When the same chaperoning proposal was tested for this group's own protein, it failed. | However, our data demonstrate that WW2 can be folded independently of WW1 | Discussion, Structure of PRPF40A tandem WW domains and proline-rich peptide recognition — files/fulltext/PMID38719828_MartinezLumbreras2024_PMC.xml

The field baseline for an isolated WW domain binding a proline-rich peptide is hundreds of micromolar. | The affinity of individual WW domains for proline-rich peptides is normally modest with a dissociation constant typically in the range of hundreds of micromolar | Discussion, Intramolecular autoinhibition proofreads the binding selectivity of WW domains — files/fulltext/PMID38719828_MartinezLumbreras2024_PMC.xml

A published tandem-WW structure was wrong because it was built on a truncated construct. | a previously reported structure of the PRPF40A WW domain tandem | Results, The WW domains of PRPF40A are folded independently and exhibit significant domain mobility — files/fulltext/PMID38719828_MartinezLumbreras2024_PMC.xml

Correcting it required two orthogonal solution techniques to agree. | we have validated our ensemble in contrast to the truncated published model | Discussion, Structure of PRPF40A tandem WW domains and proline-rich peptide recognition — files/fulltext/PMID38719828_MartinezLumbreras2024_PMC.xml

Affinities were measured on purified protein by ITC under stated conditions, at least in duplicate. | Experiments were conducted on a MicroCAl PEAQ-ITC (Malvern Instruments, UK) at 25 | Methods, Isothermal titration calorimetry (ITC) — files/fulltext/PMID38719828_MartinezLumbreras2024_PMC.xml

A motif called high-affinity by sequence inspection is not one until it is titrated. | except in the case of the highest affinity peptide | Results, PRPF40A recognizes a specific proline-rich motif in the SF1 C-terminal region — files/fulltext/PMID38719828_MartinezLumbreras2024_PMC.xml

The proposed mechanism was tested causally by mutating the motif and recovering the affinity. | This restored the binding affinity to be comparable to the isolated WW tandem | Results, Intramolecular interactions provide specificity for WW domain peptide recognition — files/fulltext/PMID38719828_MartinezLumbreras2024_PMC.xml

The authors state their generalisation to other WW-tandem proteins as a hypothesis still to be tested. | Whether the internal proline-rich sequences that these proteins have, act in a similar way as in PRPF40A still needs further analysis | Discussion, Intramolecular autoinhibition proofreads the binding selectivity of WW domains — files/fulltext/PMID38719828_MartinezLumbreras2024_PMC.xml

---

## BATCH DISPOSITION — `BATCH_20261004_005` (2026-10-04, ACTOR_ID `scientist`, Scientist O), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED

Class re-judged **MINOR** (a method-only research-layer lead). Landed as **`DL-MECH-116`**; the source's registry landing is **`CORPUS-STUB-181`** / **`LIT-0540`** (the candidate's provisional `CORPUS-STUB-180` and `LIT-0527` were both taken by earlier batches and were re-measured). **Blind locator audit: 9 triples, 9 QUOTE_FOUND, 7 SUPPORTED, 2 NOT_SUPPORTED_AS_LABELLED.** Both adverse verdicts were **repaired at source before landing**: (1) the candidate said a published tandem-WW structure *«was wrong because it was built on a truncated construct»*; the source hedges and offers **two** causes — a truncation of the C-terminal helix **or** erroneous automated NOE assignments — so the landed text states the requirement (boundaries justified by data) without asserting the cause; (2) *«a motif called high-affinity by sequence inspection is not one until it is titrated»* is **the reader's maxim, not the source's**, and is not carried. Two further qualifications folded in: the hundreds-of-micromolar baseline is **cited** (with the paper's own 150-600 micromolar individual-domain values and a Kd of about 1 micromolar for the highest-affinity tandem peptide), and the source **uses** two orthogonal techniques rather than declaring them required. The auditor confirmed the candidate's own prohibition: **WWOX is not in the authors' list** of WW-tandem proteins that may be autoinhibited.

**Not medical advice.**
