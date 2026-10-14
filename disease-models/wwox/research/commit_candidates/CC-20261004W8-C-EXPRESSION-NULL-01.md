# CC-20261004W8-C-EXPRESSION-NULL-01 — a second expression-null control for the ganglion lesion, with function and imaging: what PMID 35229008 adds to the held DRG-attribution records, and what it leaves open

`context_policy: SOURCE_FIRST`. **Author:** ACTOR_ID `scientist`, Scientist C of intake wave 8, 2026-10-04. **Change class: MINOR** (one research-line record; narrows no `consolidated baseline` claim). **Nothing here is medical advice.** WWOX occurs zero times in the source.
Sources: PMID 35229008 (`FTR-20261004-35229008-01`, manifest PASS); cargo-swap context from PMID 30073179 and PMID 30073178 (receipts as in their manifests).

## 1 · Finding

PMID 35229008 is a controlled experiment, not a description (the selection note's "mixed species and route" is wrong: one species, one route, four weeks, two animals per sex per group). In cynomolgus monkeys given AAV9 into the cisterna magna, an AAV9 "Null" genome (no functional promoter, start-codon-disrupted cDNA) reached the DRG, cord and brain at vector DNA levels similar to or higher than the expressing vector and produced **no DRG neuronal degeneration**, while every expressing-vector animal had the lesion, whatever the purification route (74, 86 or 96 percent full capsids). Lesion location was lumbosacral first. Functionally, sensory and motor nerve conduction were unchanged in all 16 expressing-vector animals; intraepidermal fibre density fell below the control range in some animals at the lower dose and not at the highest dose; MRI (highest dose and controls only) showed nerve and dorsal-cord signal and anisotropy changes.

## 2 · Increments against what is held

| Held record or candidate | What it carries | What PMID 35229008 adds | Limit |
|---|---|---|---|
| `CC-20261003W5-C-TRANSGENE-NULL-IMMUNOSUPPRESSION-01` and the Aihara-based record (empty and promoterless negatives) | lesion needs a transcriptionally productive vector | **Independent second source**: a promoter-lacking genome with DRG DNA parity in the same species and route, plus an empty-capsid-fraction gradient. Corroborates; adds the DNA-parity measurement | n = 4 per group, single Null construct and dose, four weeks; the Null also differs in cDNA and intron features; an in-vitro check found about 25 stray RPE65-mapping reads per sample in human neurons |
| DRG-attribution records (infiltrate at every dose; route, not capsid) | route is the variable | **Adds** that capsid fullness is not (three purification routes) and that the lesion at 3.1e13 and 1.1e14 GC has similar lumbosacral severity with extension to cervical level at the higher dose (Figure 2, inspected) | the two doses were not run in a purification-matched design for all arms |
| Restoration-spec off-target-organ row | DRG toxicity as a class effect; functional negatives in other programmes | **Adds** a within-study triple: histology positive, conduction negative, MRI positive (highest dose) | function negative at four weeks only; authors: conduction can stay normal with limited ganglion loss |
| `CC-20261004W7-C2-DRG-IMAGING-01` (the DRG imaging endpoint in the corpus measures storage, not injury) | no imaging endpoint tied to vector injury | **Bounds that sentence**: here an MRI change (T2/STIR signal, lower fractional anisotropy, reduction of 24 percent or more in two animals with the most pathology) tracks histology at one dose in a primate | highest-dose group only, no Null imaging, two-animal anchoring, sponsor-authored |
| Cargo-swap reading (PMID 30073179 vs PMID 30073178, same capsid, promoter, route, species) | lesion exists with both cargoes | **Adds** an expression-null arm on the same background in a third study | cross-study contrast; INFERENZA that severity depends on the cargo |

## 3 · Wording check

The authors conclude DRG toxicity "is primarily mediated by transgene overexpression". The data show lesion requires something present only in the expressing genome (transcription, protein or the specific cDNA); they do not measure expression in DRG neurons or separate mRNA from protein; "overexpression" is an interpretation (INFERENZA). Their immunity statement ("immune suppression ablated T cell responses, but not DRG pathology") overstates the two cited primaries (see `CC-20261004W8-C-IMMUNOSUPPRESSION-PRIMARIES-01`).

## 4 · Transfer limits

Cynomolgus, cisterna magna, AAV9, CB7 promoter, secreted lysosomal-enzyme cargo, four weeks. No immune manipulation, no WWOX cassette, no intracellular cargo, no age or dose-scaling statement. Brain findings seen only with the expressing vector are attributed by the authors to an immune response to the human protein (no immune read-out beyond antibodies).

## 5 · Ops (provisional)

### 5.1 · `disease-models/wwox/research/research_lines_current.md`

| field | value |
|---|---|
| op | `append` (new record after the current final research-line record) |
| record | `RL-C-20261004w8c2 — A second expression-null control for the DRG lesion (DNA parity, no lesion), capsid fullness not a determinant, and a histology-positive / conduction-negative / MRI-positive triple in cynomolgus ICM` |
| status | `open` |
| tag | `INFERENZA` (readings are `DATO`) |
| body | §1, §2 and §4 of this candidate verbatim |
| class | MINOR |

## 6 · What would change this

- **Would strengthen** "expression-dependent": a promoter-matched control that produces mRNA but no protein (the authors cite an earlier parenchymal-injection control with a functional CAG promoter that did cause cord degeneration), or reduction of DRG-neuron expression with a miRNA target.
- **Would falsify** the Null reading: DRG degeneration with a Null genome at a larger n or higher dose.

## 7 · Brief premises tested

- "Species and route mix may be heterogeneous" — false.
- "A characterisation study, so it describes rather than tests" — it tests (Null arm, three purifications).

### LOCATOR TRIPLES FOR BLIND AUDIT

Format: `(proposition | verbatim quote | anchor)`. Each artefact is on disk and each quote was verified by the manifest validator against the artefact named for the PMID in brackets. Figure entries are attestations of panels read at native resolution, not string matches.

- [PMID 35229008, artefact `files/fulltext/PMID35229008_Buss2022_PMC.xml`] (Group size was two animals per sex per group, cynomolgus monkeys, single cisterna magna dose. | Groups of cynomolgus monkeys (2/sex/group) | Results, In-life assessment)
- [PMID 35229008, artefact `files/fulltext/PMID35229008_Buss2022_PMC.xml`] (The control vector was designed to transduce as efficiently as the expressing vector without producing mRNA from either strand. | This was designed to transduce cells as efficiently as AAV9.hCLN2 without producing mRNA from either DNA strand of the vector genome | Discussion, para 3)
- [PMID 35229008, artefact `files/fulltext/PMID35229008_Buss2022_PMC.xml`] (In human neurons in vitro the Null vector gave an average of 25 RPE65-mapping reads per sample. | an average of 25 reads mapping to human RPE65 was detected per sample | Materials and methods, Test article, para 3)
- [PMID 35229008, artefact `files/fulltext/PMID35229008_Buss2022_PMC.xml`] (Null vector DNA in brain, cord and DRG was at levels similar to or greater than with the expressing vector. | at similar or greater levels than those seen with AAV9.hCLN2-treated cynomolgus monkeys | Results, Biodistribution, para 1)
- [PMID 35229008, artefact `files/fulltext/PMID35229008_Buss2022_PMC.xml`] (The authors report no DRG toxicity or other treatment-related finding with the Null vector. | there was no evidence of DRG toxicity or any other treatment-related findings in these AAV9.Null-treated animals | Discussion, para 3)
- [PMID 35229008, artefact `files/fulltext/PMID35229008_Buss2022_PMC.xml`] (The results section records increased cellularity in lumbosacral DRG in two of four Null-vector animals against one of four vehicle animals. | a higher incidence of increased cellularity (two of four animals) in the DRG (LS only) | Results, Histopathology, para 1)
- [PMID 35229008, artefact `files/figures/PMID35229008/gr2.jpg`] (Figure 2: lumbosacral DRG neuronal degeneration scores about 1 to 2 in all expressing-vector groups and zero for the Null group in every region; cervical and thoracic DRG degeneration only at the 1.1e14 dose; lumbosacral nerve-root degeneration about 3 to 4 in expressing groups. | [figure attestation — pixels cannot be quote-matched] Fig 2 rows cervical, thoracic, lumbar, lumbosacral by columns DRG neuronal degeneration, spinal nerve root degeneration, spinal cord dorsal-tract degeneration: AAV9.Null (open circles) scores 0 in every panel; expressing-vector groups score about 1 to 2 for lumbosacral DRG; the 1.1e14 group (diamonds) alone scores above 0 in cervical, thoracic and lumbar DRG; lumbosacral nerve-root scores about 3 to 4. | Figure 2, DRG and nerve-root columns)
- [PMID 35229008, artefact `files/fulltext/PMID35229008_Buss2022_PMC.xml`] (Three purification routes with 74, 86 and 96 percent full capsids all gave the lesion; the authors conclude purification and empty-capsid fraction are not major determinants. | indicating that the purification process and relative amount of empty capsid are not major determinants of the DRG toxicity | Discussion, para 2)
- [PMID 35229008, artefact `files/fulltext/PMID35229008_Buss2022_PMC.xml`] (No effect on sensory or motor nerve conduction in animals with histological change. | no effects were seen in the neuro-electrophysiological endpoints | Results, Peripheral nerve conduction)
- [PMID 35229008, artefact `files/fulltext/PMID35229008_Buss2022_PMC.xml`] (Intraepidermal nerve fibre density fell below the control range in some animals with no dose relationship. | Thus, the reduction in nerve fiber density was considered to be likely test-article-related in some animals but showed no relationship to dose. | Results, Intraepidermal nerve fiber density)
- [PMID 35229008, artefact `files/figures/PMID35229008/gr4.jpg`] (Figure 4: in the low-dose groups some animals fall from the pre-dose range to about 25 to 30 fibres per mm; the 1.1e14 group shows no fall; group means overlap the control band. | [figure attestation — pixels cannot be quote-matched] Fig 4 scatter, pre-dose versus week 4 per group: AEX 3.1e13, CEX 3.1e13 and UC 3.1e13 groups show some week-4 values near 25 to 45 fibres per mm; the 1.1e14 AEX group is about 40 to 50 at both times; Null and control near unchanged; grey band is the pre-treatment range. | Figure 4)
- [PMID 35229008, artefact `files/fulltext/PMID35229008_Buss2022_PMC.xml`] (MRI was done only in the 1.1e14 hCLN2 group and controls. | the only AAV9.hCLN2 group evaluated | Results, MRI)
- [PMID 35229008, artefact `files/fulltext/PMID35229008_Buss2022_PMC.xml`] (The authors conclude DRG toxicity after intrathecal AAV9 is primarily mediated by transgene overexpression, on this study alongside other published data. | supports a hypothesis that the DRG toxicity in NHPs following intrathecal administration of rAAV9 is primarily mediated by transgene overexpression | Discussion, final paragraph)
- [PMID 35229008, artefact `files/fulltext/PMID35229008_Buss2022_PMC.xml`] (The authors describe the Null genome as lacking a functional promoter and producing neither mRNA nor protein. | which lacked a functional promoter and does not produce mRNA or protein | Discussion, para 3)

## BATCH DISPOSITION — `BATCH_20261004_002` (2026-10-04, ACTOR_ID `scientist`, Scientist L), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** `PROPAGATED` (MINOR).
**Surfaces written:** research_lines_current.md · discovery_ledger_current.md

Landed as **`RL-C-20261004w8c2`**, plus **one corroboration line inside `DL-METH-118`** and **one §7.2 in-place correction of `RL-C-20261004w7c1` (b)** — rather than a second window record, because the proposition family already had a home.
🔴 **This is the batch's sharpest result.** `RL-C-20261004w7c1` (b) stated, as a fact about the corpus, *«no source held measures it for the DRG, and the held promoterless negative is hepatic»*. `PAPER 232` **is** that design, for the DRG, in primates, with vector-DNA parity. A fact about a past act may be corrected in place under § 7.2, so it is, **with the superseded wording quoted verbatim inside the corrected bullet**; the half that survives is kept explicitly (the design still does not separate immune from expression cause, because no immune read-out beyond antibodies was taken and expression was never measured in DRG neurons), and **no stated conclusion was overwritten**.
⚠️ **A CONTRADICTED blind-audit verdict, repaired at source.** The candidate's Figure 2 attestation said cervical and thoracic DRG degeneration occurred **only** at 1.1 × 10¹⁴ GC. An auditor measured the panel: in the **cervical** DRG a 3.1 × 10¹³ group has one animal at severity 1, group bar about 0.25. **The universal quantifier is withdrawn** and the landed record states which segments are high-dose-only and which are not.
⚠️ **A second attestation failed and was repaired by re-sourcing.** The intraepidermal fibre-density figure attestation was wrong in two particulars (the high-dose group's pre-dose values, and a low-dose group's week-4 minimum), and the grey band is the **pre-treatment range of all samples**, not a control band. The finding itself is carried by the Results sentences, which the record now cites instead of the panel — the same repair `BATCH_20261003_005` and `BATCH_20261004_001` each made once.
⚠️ Two further narrowings: the authors' conclusion is *«supports a hypothesis that»* and their route is **cisterna magna** while the sentence generalises to *«intrathecal»*; and the nerve-conduction assessment *«focused on sensory»*, with motor on one pathway. The record also carries, rather than hides, that the Null arm shows increased cellularity in two of four animals against one of four vehicle animals — an internal tension in the source.

**Not medical advice.**
