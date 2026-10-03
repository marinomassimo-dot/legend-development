# CC-20261003w4-C-REGISTRY-01 — registry landing for the six group-C PMIDs of intake wave 4

- `context_policy: SOURCE_FIRST`
- Change class: **MINOR**. No claim is created, narrowed or reversed. This candidate gives each of
  the six PMIDs a structured landing so that none becomes an orphan complete-read; without it LINT
  blocks `BATCH_COMMIT` with `ORPHAN_COMPLETE_READ`.
- Sources: PMID 42349402, 41992613, 42458834, 41404412, 35331006, 36700120. All six first readings,
  all six `partial_fulltext_read`, all six manifests `VERDICT: PASS`
  (`deepdive_manifest.py --pmid <PMID> --verify-artifacts --require-current-schema`).
- Receipts prepared and **not** appended:
  `scratchpad/receipts_pending_w4/sciC_<pmid>_1.json`, event ids `FTR-20261003-<pmid>-01`.
- **None of the six mentions WWOX** (`grep -icE 'wwox|wox1|16q23|fragile site FRA16D'` returns 0 on
  each artefact). Every record below is therefore `Transferability: T3` and
  `clinical relevance: BACKGROUND`, and every record states its transfer limit.
- **Nothing here is medical advice.**

## Registry presence needed, per PMID

Every one of the six needs **both** a `PAPER` record and a `LIT` record: `paper_packet.py packet
--pmid <PMID>` returned, for all six, "identity: DOI (none recorded) · (no title recorded)",
"manifest: none — this is a first reading", "prior read: depth=none · receipts=0" and
"acquisition: no route recorded". No existing registry statement rests on any of them.

## Next-free identifiers — PROVISIONAL

Measured with `registry_records.py catalog` after merging `main` at commit 31da5fa, 2026-10-03:
`PAPER` max **142**, `LIT` max **440**. Declared **provisional**: other branches land continuously
and the integrator must re-measure and renumber before applying these ops.

| # | PMID | Provisional PAPER | Provisional LIT |
|---|---|---|---|
| C1 | 42349402 | PAPER 143 | LIT-0441 |
| C2 | 41992613 | PAPER 144 | LIT-0442 |
| C3 | 42458834 | PAPER 145 | LIT-0443 |
| C4 | 41404412 | PAPER 146 | LIT-0444 |
| C5 | 35331006 | PAPER 147 | LIT-0445 |
| C6 | 36700120 | PAPER 148 | LIT-0446 |

## Ops

### 1 · `disease-models/wwox/registries/paper_registry_current.md`

| field | value |
|---|---|
| op | `append` × 6 (new records) |
| anchor | after the current final `PAPER` record; `old` not required for an append, and the integrator re-measures the insertion point |

Each record carries the field set of `PAPER 132` (the existing template for an off-gene background
source): **Short title · Full title · Authors · Year · Source type · Journal/source · Identifier ·
Status · Record provenance · Evidence depth · Primary pathway · Model/species · Genotype/model ·
Transferability · clinical relevance · Claim links · Role · LIT link · Note**.

Common to all six: `Status: processed`; `Record provenance: created by
CC-20261003w4-C-REGISTRY-01 (intake wave 4 2026-10-03, Scientist C, group C)`; `Evidence depth:
partial_fulltext_read` with the receipt id, the manifest path and the dossier path, plus "figure
panels not inspected as images and no supplementary file fetched — owed";
`Genotype/model: no WWOX allele; this source does not mention WWOX`;
`Transferability: T3`; `clinical relevance: BACKGROUND — transferable method only, not evidence`;
`Claim links: none — no canonical claim is touched`; `Note: class-level record; no individual-level
detail is carried in this public edition. Not medical advice.`

| record | Short title | Primary pathway | Model/species | Role |
|---|---|---|---|---|
| PAPER 143 | Fukai 2026 Mol Ther — a compact 410-bp mouse Gad1 promoter (cmGAD67) driving selective AAV expression in inhibitory neurons | P7 gene-therapy design | mouse (C57BL/6J, VGAT-tdTomato), AAV-PHP.eB intravenous and intraparenchymal | The group's only quantified promoter-specificity measurement: 92.2 % ± 1.3 % inhibitory-neuron specificity systemically, ≈85 % of PV⁺ neurons transduced and >60 % of transduced cells PV⁺. 🔴 **Specificity is route-contingent**: the same cassette falls to 63.9 % ± 4.1 % after direct hippocampal injection, which the authors attribute to local vector concentration. **Transfer limit:** mouse promoter, no human orthologue tested; one dose throughout, so no dose-response; **no toxicology of any kind**; and this is circuit modulation by adding GAD65, not restoration of a deficient protein |
| PAPER 144 | Song 2026 Mol Ther — EXG001-307, a dose-optimised intra-CSF AAV9 for SMA; the two-sided dose claim, with its upper limb unmeasured | P7 gene-therapy design | SMNΔ7 mouse, Wistar Han rat (male only), juvenile cynomolgus macaque | The only two-sided dose claim in the corpus. Lower limb **measured** (i.c.v. median survival 23 d at 2 × 10¹⁰ vg/animal to 373 d at 2 × 10¹¹; MED 2 × 10¹⁰). Upper limb **inferred**: it comes from a different construct at a higher dose, that cohort received no necropsy or histopathology, and the authors write that the measurement "would be valuable to define this therapeutic window". In primates the highest dose tested became the NOAEL, so no toxic dose was reached. **Transfer limit:** sponsor study on its own candidate; *SMN* dose sensitivity does not transfer to WWOX; mouse DRG never harvested; three mutually incompatible vg/kg normalisations of the same rat doses |
| PAPER 145 | Boitnott 2026 Mol Ther — unregulated DDX3X overexpression after an intra-CSF injection kills newborn mice from the heart | P7 gene-therapy design | wild-type C57BL/6J mouse, bilateral i.c.v. at P1 and intrathecal at P21 | The group's hardest negative, and sponsor-adverse: all high-dose animals dead by P8 from myocardial degeneration, with hepatic steatosis and a >1000-fold cardiac *Ifnb1* rise, while a promoter-matched control vector carrying a different transgene elicited none of it. The lethal dose, scaled by neonatal brain mass, equals a dose the paper says is in clinical use. 🔴 "The brain was overall unaffected" is a **morphology** statement: brain *Cxcl10* rose ≈23-fold in the same animals. **Transfer limit:** DDX3X's own roles in RIG-I/MAVS signalling and *Ddit3* transcription are plausibly the mechanism, so the magnitude does not transfer; WWOX dose sensitivity is neither shown nor excluded. n per group is reported nowhere in the main text |
| PAPER 146 | Grubor 2025 Mol Ther Methods Clin Dev — immune events precede AAV DRG pathology in macaques, and dexamethasone plus tacrolimus reduce it across three cargos | P7 gene-therapy design / BLOCK-1 safety | cynomolgus macaque, intra-cisterna magna and intrathecal lumbar | One pole of an **unresolved contradiction** (see `CC-20261003w4-C-DRG-CONTRADICTION-01`). Measures what no other source in the group measures: ultrastructural change and immune infiltrates from day 5, before the first lesion at day 15. Mitigation across three cargos including one expressing no protein, with transgene expression unchanged. **Transfer limit:** sponsor study; the causal claim rests on a multi-target pharmacological block with n = 3 per group; no antigen-specific T cells were detected and the effector mechanism is the authors' postulate; healthy animals, no efficacy endpoint; longest arm 43 days against the authors' own predicted six-month requirement; and the authors state the immune mechanism **does not hold in mouse** |
| PAPER 147 | Tukov 2022 Hum Gene Ther — intrathecal onasemnogene DRG and trigeminal findings, not mitigated by prednisolone or by rituximab plus everolimus | P7 gene-therapy design / BLOCK-1 safety | cynomolgus macaque, intrathecal lumbar with iohexol contrast, plus an intravenous arm | The other pole of the same contradiction. Findings from the anticipated clinical dose upward and **with no dose response**; nerve conduction normal in every arm; high vector transcript colocalised with the degenerating neurons. 🔴 The negative is scoped by the authors to **adaptive** immunity, and they state that innate activation "was not excluded"; no calcineurin inhibitor was tested. "Resolution" is explicitly redefined as lower incidence and severity, because neuronal loss is not reversible. **Transfer limit:** sponsor study run to answer a regulatory partial clinical hold; the negative rests on n = 3 per sex interim and **n = 2 per sex terminal** with no power statement; human relevance declared unknown |
| PAPER 148 | Johnson 2022 Mol Ther Methods Clin Dev — blood and CSF NfL against AAV9 DRG injury in 260 macaques, with per-animal operating characteristics | P7 gene-therapy design / toxicity surveillance | cynomolgus macaque, nine pooled studies, intrathecal and intravenous | The assay source, over the group's largest denominator: 78 % incidence at 2–12 weeks falling to 42 % by 52 weeks; 18–21 DRG per animal on a five-point scale under pathologist peer review; ROC AUC 0.85 (blood) and 0.95 excluding minimal grade, with sensitivity and specificity at five fold-change cut-offs. Empty capsid and promoter-less vectors caused neither lesion nor NfL rise. **Transfer limits, three:** (1) under `LEGEND_CORE` §13 NfL is **Tier 3** for WWOX — a biomarker of vector toxicity, never a WWOX disease biomarker; (2) not clinically validated, by the authors' own statement, and raised NfL "is not disease specific"; (3) 🔴 **not independent of `PAPER 147`** — same sponsor, four shared authors, data drawn from the sponsor's own study warehouse |

### 2 · `disease-models/wwox/registries/literature_tracking_log_current.md`

| field | value |
|---|---|
| op | `append` × 6 (new records, `LIT-0441` … `LIT-0446`) |
| anchor | after the current final `LIT` record |

Each record carries the field set of `LIT-0431`: **Short title · Authors · Year · Source type ·
Journal/source · Identifier type · Identifier value · Date discovered · Date processed · Discovery
source · Status · Status note · Primary pathway · Species · Transferability · clinical relevance ·
Claim links · Working Model impact · Report mentions · Next action · Evidence depth**.

Common to all six: `Date discovered: 2026-10-03 (Orchestrator selection record of intake wave 4)`;
`Date processed: 2026-10-03 (first-hand read)`; `Discovery source: Orchestrator selection record of
intake wave 4 2026-10-03, group C`; `Status: processed`; `Status note: partial_fulltext_read — figure
panels not inspected as images and no supplementary file fetched; record created by
CC-20261003w4-C-REGISTRY-01`; `Transferability: T3`; `clinical relevance: BACKGROUND`;
`Claim links: none`; `Working Model impact: none — no block is redefined`; `Report mentions:
research/intake_wave_20261003w4_C.md · CC-20261003w4-C-REGISTRY-01` plus the topic candidate that
cites it; `Next action: supplement and figure panels owed for a complete read`; `Evidence depth:
partial_fulltext_read — manifest deepdive_manifests/PMID<pmid>.json`.

Identifier values, exactly as PubMed gives them:

| record | Identifier value |
|---|---|
| LIT-0441 | PMID 42349402 / DOI 10.1016/j.ymthe.2026.06.007 / PMC13555566 |
| LIT-0442 | PMID 41992613 / DOI 10.1016/j.ymthe.2026.04.027 / PMC13330066 |
| LIT-0443 | PMID 42458834 / DOI 10.1016/j.ymthe.2026.07.032 / PMC13555558 |
| LIT-0444 | PMID 41404412 / DOI 10.1016/j.omtm.2025.101643 / PMC12704302 |
| LIT-0445 | PMID 35331006 / DOI 10.1089/hum.2021.255 / PMC9347375 |
| LIT-0446 | PMID 36700120 / DOI 10.1016/j.omtm.2022.12.012 / PMC9852542 |

### 3 · Cross-links

Each `PAPER` record's `LIT link` field wikilinks its paired record, zero-padded to four digits,
matching the existing convention at `PAPER 132` — that is, a double-bracket link whose target is
`literature_tracking_log_current` and whose fragment is the paired `LIT-NNNN` record id. The link
is written at commit time, not here: these records do not yet exist, and a live wikilink to a
record that has not been appended fails `scripts/test_link_targets.py` (both the record-target and
the exact-heading test). The integrator writes the links in the same op list that creates the
targets.

## Integrity facts the integrator should carry forward

- No retraction, expression of concern or erratum on any of the six (PubMed article metadata,
  2026-10-03; article types "Journal Article", with PMID 35331006 additionally "Research Support,
  Non-U.S. Gov't").
- Reference lists: all six `SCREENED_CLEAN` by `dependency_integrity.py screen --manifest-block`
  against the Retraction Watch snapshot of 2026-09-10 (72 476 rows, sha256
  `8ff64393b342e18ec2c04b06d54dba834e37e77575913c97fa93c8da41dde3d5`), with 1–4 references per paper
  `UNSCREENABLE_NO_DOI` and zero flagged.
- Artefact digests, in full:

| PMID | artefact | sha256 |
|---|---|---|
| 42349402 | `files/fulltext/PMID42349402_Fukai2026_PMC.xml` | `6dc844f6610a108e88b23f67004363b6084b4e4bfdf4cd6d77ff089e27a96a65` |
| 41992613 | `files/fulltext/PMID41992613_Song2026_PMC.xml` | `9788b805bb85b3301ec063db3b29e663d3e800d43c7e6f6800e5cb3ac2ed6cdf` |
| 42458834 | `files/fulltext/PMID42458834_Boitnott2026_PMC.xml` | `38121405e364e7e1ef81bae4088f31ea8d396512d3a001fbf7f7763d5e1da69f` |
| 41404412 | `files/fulltext/PMID41404412_Grubor2025_PMC.xml` | `9c9f8a5bff55b0fa6c5483d854a24a4ad5e4f33b05735ddbb9d1eb2f6297c685` |
| 35331006 | `files/fulltext/PMID35331006_Tukov2022_PMC.xml` | `5154e8c1bc02b6d025538d2fcb4ce528ad670b9e395a8f66a21fb766c55a8deb` |
| 36700120 | `files/fulltext/PMID36700120_Johnson2022_PMC.xml` | `b1d3ce745474b78203f619c42841bba91931851febe7f9c6555d626acd4c6be8` |

### LOCATOR TRIPLES FOR BLIND AUDIT

(This source does not mention the gene at all, which is why its registry record is marked as a transferable method source rather than evidence. | Epilepsy arises from disruption of excitation-inhibition (E/I) balance | Abstract first sentence, `files/fulltext/PMID42349402_Fukai2026_PMC.xml`)

(The promoter is derived from the mouse locus, so the cassette itself is not a human reagent. | we conducted a systematic analysis of the Gad1 locus and identified a compact 410-bp sequence, termed the compact mouse GAD67 (cmGAD67) promoter | Introduction, `files/fulltext/PMID42349402_Fukai2026_PMC.xml`)

(Specificity dropped by about a third when the route changed from systemic to direct parenchymal injection. | direct hippocampal injection of AAV-GFP or AAV-hM4D(Gi) resulted in reduced specificity | Results, chemogenetic manipulation, `files/fulltext/PMID42349402_Fukai2026_PMC.xml`)

(The cohort that defines the upper limit of the dose range received no pathology workup. | did not undergo comprehensive necropsy or histopathological evaluation | Results, codon-optimised variants, `files/fulltext/PMID41992613_Song2026_PMC.xml`)

(The authors state that the therapeutic window is not yet defined by their own data. | would be valuable to define this therapeutic window and substantiate this conclusion | Results, codon-optimised variants, `files/fulltext/PMID41992613_Song2026_PMC.xml`)

(No adverse effect was found at the top dose tested in primates, so the primate arm bounds nothing from above. | the high dose was designated the no-observed-adverse-effect level | Results, overall safety conclusion, `files/fulltext/PMID41992613_Song2026_PMC.xml`)

(The sensory ganglia were never collected in the rodent efficacy studies. | DRGs were not harvested or analyzed | Results, route comparison and tissue expression, `files/fulltext/PMID41992613_Song2026_PMC.xml`)

(Death followed a CSF injection within a week, from a peripheral organ. | died abruptly by P8, 1 week post injection | Results, rapid death due to myocardial degeneration, `files/fulltext/PMID42458834_Boitnott2026_PMC.xml`)

(The lethal animal dose was scaled to a human dose by brain mass, which is what makes the result transferable at all. | if extrapolated by neonatal brain mass | Materials and methods, viral vector injections, `files/fulltext/PMID42458834_Boitnott2026_PMC.xml`)

(The brain showed a large chemokine induction in the same animals whose brains were called unaffected. | Cxcl10 mRNA levels were also increased in the brain | Results, type I interferon signalling, `files/fulltext/PMID42458834_Boitnott2026_PMC.xml`)

(The operational lesson the authors draw is about promoter strength rather than about this particular gene. | we raise caution to the use of strong promoters like CBA | Discussion, final paragraph, `files/fulltext/PMID42458834_Boitnott2026_PMC.xml`)

(Immune cells arrived before any lesion could be detected. | prior to detectable neuronal cell body degeneration/necrosis observed on day 15 by both histopathology and electron microscopy | Results, type I interferon signalling and immune cell recruitment, `files/fulltext/PMID41404412_Grubor2025_PMC.xml`)

(In the first of the three mitigation studies the drugs began after the vector, not before it. | Immunosuppression (IMS) dosing started on day 2 | Materials and methods, AAVhu68-hSMN1 immunosuppression study #1, `files/fulltext/PMID41404412_Grubor2025_PMC.xml`)

(The authors state that the immune mechanism they report does not hold in the mouse. | immune infiltration into the DRG in mice is considered a secondary response to neuronal degeneration | Discussion, species comparison, `files/fulltext/PMID41404412_Grubor2025_PMC.xml`)

(The regimens tested in the other primate programme did not reduce the lesion. | microscopic DRG findings were not mitigated with coadministration of anti-inflammatory or immunosuppressive regimens | Conclusions, `files/fulltext/PMID35331006_Tukov2022_PMC.xml`)

(That negative is scoped by its own authors to adaptive immunity, not to immunity as such. | suggesting that primary adaptive immune responses may not be a critical mediator | Discussion, immunosuppression paragraph, `files/fulltext/PMID35331006_Tukov2022_PMC.xml`)

(The same authors leave innate immune activation explicitly open. | activation of the innate immune response in transduced cells was not excluded | Discussion, pathogenesis paragraph, `files/fulltext/PMID35331006_Tukov2022_PMC.xml`)

(The lesion did not scale with dose across the range tested. | did not demonstrate a dose response | Discussion, comparison with other AAV gene therapies, `files/fulltext/PMID35331006_Tukov2022_PMC.xml`)

(The word resolution is redefined by the authors and does not mean the neurons recovered. | Neuronal cell degeneration/neuron loss is generally not considered a reversible finding | Discussion, resolution paragraph, `files/fulltext/PMID35331006_Tukov2022_PMC.xml`)

(A per-animal detection threshold with sensitivity and specificity does exist for the toxicity biomarker. | A cutoff of 1.5-fold in NfL from pre-dose values leads to the greatest sensitivity | Results, correlation between NfL changes and DRG histopathology, `files/fulltext/PMID36700120_Johnson2022_PMC.xml`)

(The lesion requires transgene expression: capsid alone produced nothing. | No DRG microscopic findings were observed in cynomolgus macaques administered empty AAV9 capsid | Results, DRG microscopic evaluation, `files/fulltext/PMID36700120_Johnson2022_PMC.xml`)

(The biomarker is not validated for clinical use, by its own authors. | To date, NfL measurements have not been incorporated into clinical trials for AAV therapies. | Discussion, clinical translation paragraph, `files/fulltext/PMID36700120_Johnson2022_PMC.xml`)

(The pooled dataset comes from one sponsor's own warehouse, which is the basis for treating it as not independent of the other sponsor paper. | extracted from the Novartis study data warehouse | Materials and methods, data extraction and analyses, `files/fulltext/PMID36700120_Johnson2022_PMC.xml`)
