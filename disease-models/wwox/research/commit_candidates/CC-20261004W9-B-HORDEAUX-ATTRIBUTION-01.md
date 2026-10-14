# CC-20261004W9-B-HORDEAUX-ATTRIBUTION-01 — what two newly readable primate papers add to the DRG record, and one attribution corrected

- `context_policy: SOURCE_FIRST` for both sources (first pass written and committed before any DRG record or candidate was opened); the comparison below followed and is `QUESTION_DRIVEN`.
- Sources: PMID 32355866 (`FTR-20261004-32355866-01`) and PMID 35333110 (`FTR-20261004-35333110-01`); both `partial_fulltext_read`; both manifests `VERDICT: PASS`. **Neither mentions WWOX** (zero occurrences in each persisted JATS body).
- Change class: **MINOR.** One research-line record; narrows no `consolidated baseline` claim and reverses none. It adds increments to `RL-C-20261003w6` and `RL-C-20261004w7c1`; it does not restate their findings.
- **Nothing here is medical advice.**

## 1 · The finding in one sentence

PMID 32355866 is **Bey 2020 (Nantes), not Hordeaux 2020**, and adds a descriptive DRG baseline for lumbar-intrathecal and intracerebroventricular AAV9/AAVrh10 under a **triple immunosuppressive regimen** (infiltrate present, graded only descriptively, three weeks); PMID 35333110 adds a **graded, GLP, no-immunosuppression** ICM dose-response in juvenile rhesus (three doses, 3 and 6 months) for a **secreted-enzyme** cargo in which DRG neuronal degeneration never exceeds a minimal score while a secondary dorsal-column axonopathy is dose dependent and reaches grade 3 at the top dose — a lesion the paper's own sentence ("minimal to mild") understates.

## 2 · What each source adds to, bounds or leaves untouched

| Held record | Statement it carries | PMID 32355866 (Bey 2020) | PMID 35333110 (Hordeaux 2022) |
|---|---|---|---|
| `RL-C-20261003w6` (infiltrate at every dose and under every regimen; neuron loss only above a threshold) | dose and immune state act on two endpoints | **Adds a third immunosuppressed primate dataset**: sirolimus + prednisolone + mycophenolate in all eight animals; mild-to-moderate mononuclear infiltration in DRG or DRG fibres in all six lumbar-intrathecal animals by the text (the two ICV animals are not mentioned; Figure S5 shows six representative panels; no grade table); brain clean. **Bounds**: no unmedicated arm, GFP reporter, three weeks, so the regimen is not shown to have suppressed anything and nothing speaks to neuronal degeneration | **Adds the no-immunosuppression graded arm at a lower dose range than the 1.68E14 vg datum**: 4.5E12, 1.5E13, 4.5E13 GC per animal (5.0E10 to 5.0E11 GC/g brain); DRG neuronal degeneration at most grade 1 at every dose (group means about 0 / 0.1 / 0.35 / 0.5 by Figure 5C); dorsal axonopathy dose dependent. **Does not test the record's falsifier** (flat neuronal degeneration across dose while infiltrate varies): infiltrate is not reported separately and neuronal degeneration rises modestly with dose. Vector-genome units are per animal and per gram brain, a different capsid, promoter and cargo, so the threshold of the held 1.68E14 study is not comparable |
| `RL-C-20261004w7c1` (duration of immunosuppression; promoterless discriminator; three stimuli) | immunosuppression partial, untapered | **Leaves untouched** (no withdrawal, three weeks) | **Adds a no-immunosuppression stability datum**: incidence and severity similar at days 90 and 180 (no progression over six months), which bounds the rebound claim only for the no-immunosuppression condition |
| Dog versus primate sensitivity (unrecorded in the held lines) | not carried | — | **Adds**: dogs treated ICM at 3.0E13 GC (n = 4 treated) showed no DRG finding; the authors say the dog is less sensitive than the primate; the dog arm expresses a canine transgene. Species limit: one of the two sources of "DRG findings are a class effect" is not true of dogs in this dataset |
| Secreted versus intracellular cargo (`RL-C-20261003w6` transfer limits) | secreted-cargo logic does not carry to an intracellular protein | — | **Corroborates the limit and adds a case**: GALC is secreted and cross-corrects, antibodies and T cells to the human transgene product in macaques were frequent (14 of 18 T-cell responses), and the DRG read-out is interpreted with that confound |

## 3 · Attribution correction

The wave-9 selection record names PMID 32355866 "Hordeaux 2020" and describes it as the same group as PMID 35333110. The persisted artefact gives **first author Bey, senior authors Moullier and Colle, Nantes/Oniris**, with Hordeaux J as the seventh of 22 authors; PMID 35333110 is the Pennsylvania (Wilson) group. Any held or future record that cites "Hordeaux 2020" for the intra-CSF comparison paper should cite Bey 2020. A search of the held registries and candidates finds no such record, so the correction is carried by the new `PAPER` title in `CC-20261004W9-B-REGISTRY-01`. A third paper, PMID 33177182 (a 2020 Hordeaux paper on miRNA detargeting, still blocked), is probably the source of the confusion; that is an inference and was not tested.

Separately, the dependency screen flagged one cited reference of PMID 32355866 (a 2010 SMA rescue paper, retracted in 2022). It is a **citation-only** dependency in the Introduction (reference 3); no datum of this paper depends on it.

## 4 · The record this candidate proposes, and its transfer limits

One new research-line record (`INFERENZA`) holding the §1 and §2 increments and §3.

| field | value |
|---|---|
| file | `disease-models/wwox/research/research_lines_current.md` |
| op | `append` (new record, after the current final research-line record; provisional id `RL-C-20261004w9b`; the integrator re-measures the insertion point and the id) |
| record | `RL-C-20261004w9b — Increments on the CSF-route AAV DRG record from a triple-immunosuppression primate reporter study and a graded GLP ICM dose-response without immunosuppression` |
| status | `open` |
| tag | `DATO` for each measurement · `INFERENZA` for the comparison |
| body | §1 and §2 of this candidate verbatim; §3; the transfer limits below; cross-references `RL-C-20261003w6` · `RL-C-20261004w7c1` · `RL-C-20261003w4a` · `DIS-031` |
| anchor | none required for an append |
| class | MINOR |

**Transfer limits (binding).** Cynomolgus (reporter, 8 animals, three weeks, triple immunosuppression) and rhesus (a secreted lysosomal enzyme, 6 per dose, 3 and 6 months, no immunosuppression, juvenile); dog (canine transgene). No WWOX construct exists in either source, so no dose in these units transfers to one; a WWOX cassette is an intracellular protein transgene, so the secreted-cargo cross-correction of PMID 35333110 does not carry to it. No immunosuppression arm exists inside either paper for contrast. P47T, Q230P, G372R, A141T and P252A are not interchangeable with each other or with a null. Not medical advice.

## 5 · What would change this, and what would falsify it

- **Would strengthen the immunosuppression-limit reading:** DRG histology with a grade table from the Bey animals, or an unmedicated reporter arm in the same design.
- **Would falsify "DRG neuronal degeneration is minimal at 5E11 GC/g brain under no immunosuppression":** a primate study at similar GC/g brain with a non-secreted cargo showing grade 2 or more.
- **Would change the dog-versus-primate bound:** DRG histology of dogs treated with a human transgene.

## 6 · Brief premises tested

- "Hordeaux 2020" for PMID 32355866: false (Bey 2020).
- "The only record in the wave where a DRG-risk decision was actually made in favour of dosing": the paper states DRG risk "seems low" on its minimal and sporadic findings and names a clinical-trial identifier in the abstract; that is the authors' decision statement, read as such, not a measurement.
- "No immune-modulation arm exists" for PMID 32355866: true in the sense that all animals were immunosuppressed and none was not.

## 7 · Registry presence needed

`PAPER 221` and `PAPER 222` (provisional) from `CC-20261004W9-B-REGISTRY-01`.

### LOCATOR TRIPLES FOR BLIND AUDIT

Format: `(proposition | verbatim quote | anchor)`.

- [PMID 32355866, artefact `files/fulltext/PMID32355866_Bey2020_PMC.xml`] (All injected animals received three immunosuppressive drugs. | The injected animals were immunosuppressed with sirolimus 2 mg/kg/day (Rapamune), prednisolone 1 to 2 mg/kg/day (Dermipred), and mycophenolate mofetil 40 mg/kg/day (CellCept) | Materials and Methods, In Vivo AAV Injections)
- [PMID 32355866, same artefact] (Mild infiltration in two AAVrh10 animals | Subsequent histopathological examination revealed multifocal mild mononuclear cell infiltration in thoracic and lumbar DRG for LIT-KT AAVrh10-injected Mac 1 and Mac 2 animals, respectively (Figure S5). | Results, DRG, para 1)
- [PMID 32355866, same artefact] (Moderate infiltration in one AAV9 animal | Moderate mononuclear cell infiltration was observed in cervical and lumbar DRG for Mac 3 animals (Figure S5). | Results, DRG, para 1)
- [PMID 32355866, same artefact] (LIT-KT dose 2.5E+13 vg per animal | An inferior dose (2.5E+13 vg per NHP) was injected by LIT-KT administration in the present study. | Discussion, dose paragraph)
- [PMID 32355866, same artefact] (Selection of animals with low neutralising titres | We selected primates that had no detectable or low titers (<1/50) of neutralizing factors against AAV serotypes 9 and 10 in the serum. | Materials and Methods, Animals)
- [PMID 35333110, artefact `files/fulltext/PMID35333110_Hordeaux2022_PMC.xml`] (No immunosuppression in the NHP arm, half euthanised at 3 and half at 6 months | without immune-suppression treatment. We euthanized half of the animals at 3 months postdosing and the other half at 6 months postdosing. | Results, NHP, para 1)
- [PMID 35333110, same artefact] (Minimal sporadic DRG neuronal degeneration with secondary axonopathy | Test article administration resulted in minimal sporadic degeneration of primarily DRG sensory neurons, which led to secondary degeneration of associated central and peripheral axons (i.e., axonopathy). | Results, NHP, para 4)
- [PMID 35333110, same artefact] (Text: axonopathy minimal to mild when present | Secondary axonopathy associated with DRG lesions was minimal to mild when present, with many sections showing no findings | Results, NHP, para 4)
- [PMID 35333110, same artefact] (Axonopathy dose dependent | The secondary dorsal axonopathy was dose dependent, with the HD group showing the most histological findings | Results, NHP, para 4)
- [PMID 35333110, same artefact] (No progression between 90 and 180 days | The incidence and severity were similar at days 90 and 180, showing a lack of pathology progression | Results, NHP, para 5)
- [PMID 35333110, same artefact] (Dog arm without immunosuppression | The dogs did not receive any immune suppression or anti-inflammatory regimen. | Results, canine model, para 2)
- [PMID 35333110, same artefact] (Dog less sensitive than NHP | suggests that dog is less sensitive than NHP | Discussion, DRG paragraph)
- [PMID 35333110, same artefact] (Severity scale 0-5 | (0 = normal, 1 = minimal, 2 = mild, 3 = moderate, 4 = marked, and 5 = severe) | Figure 5 legend, panel C)

## BATCH DISPOSITION — `BATCH_20261004_003` (2026-10-04, ACTOR_ID `scientist`, Scientist M), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** `PROPAGATED` (MINOR, WM_v7.15 → WM_v7.16).

**Surfaces written:** research_lines_current.md

One new research line, **`RL-C-20261004w9b`**, carrying § 1–§ 3 and the transfer limits. Research lines on this surface are addressable **by heading, not by id** — `--id` returns `ANCHOR_MISSING` — so the append chain was anchored on heading text. **Blind locator audit:** not run on this candidate (its two artefacts were the ones absent from disk at audit dispatch time, and its propositions are descriptive increments to an open research line rather than claim- or baseline-touching); the attribution finding was instead **verified directly on the restored JATS front matter** at integration, which is the stronger check for an identity question. Sampled rather than audited, and named here so the asymmetry is visible.

**Not medical advice.**
