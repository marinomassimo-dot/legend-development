# CC-20261004W8-C-IMMUNOSUPPRESSION-PRIMARIES-01 — the two 2018 rhesus primaries behind the "rebound after antimetabolite withdrawal" relay: what they measure, and where the relayed wording outruns them

`context_policy: SOURCE_FIRST` (first pass on all six wave-8 sources written to dossiers before any registry record or candidate on the subject was opened; the comparison followed).
**Author:** ACTOR_ID `scientist`, Scientist C of intake wave 8, 2026-10-04. **Change class: MINOR.** One research-line record in the research layer; no `consolidated baseline` claim is narrowed or reversed. **Nothing here is medical advice.** Neither source names WWOX (zero occurrences in each persisted artefact).
Sources: PMID 30073179 (`FTR-20261004-30073179-01`) and PMID 30073178 (`FTR-20261004-30073178-01`), plus PMID 35229008 (`FTR-20261004-35229008-01`) for a secondary citation of both. All three manifests `VERDICT: PASS`.

## 1 · Finding in one paragraph

The wave-7 candidate `CC-20261004W7-C1-DRG-ATTRIBUTION-01` relayed, from a commentary, that a time-limited antimetabolite withdrawn at day 60 was followed by a rebound and a delayed DRG phenotype, and flagged the two earlier macaque papers as unread. They are now read. Both used mycophenolate mofetil to day 60 plus rapamycin to day 90 with a **single necropsy at day 90**, so a delayed or rebound DRG phenotype cannot be observed in them: there is no later time point and no earlier DRG time point (DRG were not sampled in the study that holds the day-14 and day-180 animals). What they measure is a small arm (three and five animals) whose ganglion score is **not clearly lower** with immunosuppression, and in the second paper is **higher** at the low dose. The "rebound" is a conjecture of the primaries, attached to a late CSF-cell peak and later T-cell responses, not to DRG histology.

## 2 · What each primary adds to the held and relayed statements

| Statement | Where held or relayed | PMID 30073179 (hIDUA) | PMID 30073178 (hIDS) |
|---|---|---|---|
| Immunosuppression reduces DRG toxicity severity "in some animals" | relayed by the wave-7 commentary record | **Partly holds**: axonopathy score about 2.4 against about 5.0 at three animals, errors overlapping; DRG score about 2.0 against 2.7, overlapping (Figure 3G, inspected). The text says "trended toward lower scores"; the panel qualifies it | **Does not hold at low dose, holds weakly at high**: DRG about 3.0 (two animals) against 3.4 at high dose; about 4.7 with immunosuppression against about 1.1 without at low dose; axonopathy 2.0 against 4.0 high, 3.3 against 2.0 low (Figure 3F, inspected). The authors: "IS did not prevent neuronal degeneration" |
| Rebound after antimetabolite withdrawal gave a delayed phenotype | relayed (wave 7) | **Not observable**: one necropsy at day 90; the paper says later T-cell responses are "likely reflecting MMF withdrawal on day 60" (a T-cell statement, not DRG) | **Not observable**: single day-90 necropsy; a late CSF-cell peak in one low-dose immunosuppressed animal "perhaps due to MMF withdrawal" |
| Immunosuppression "ablated T cell responses" | wording in PMID 35229008 citing both | **Overstated**: one of three immunosuppressed animals had a transgene T-cell response; antibodies to the transgene were abolished | Transgene T-cell response was seen in one non-immunosuppressed low-dose animal only, so the comparison is not informative |
| Regimen is clean | implicit | The regimen itself caused anorexia, diarrhoea, weight loss and anaemia starting before vector dosing; one animal's MMF was stopped at day 35 | Same; one high-dose animal was withdrawn before dosing |
| Lesion needs immune effectors | held as an open question | Infiltrate is CD3 and CD20 cells clustered around transgene-positive neurons, and persists with immunosuppression; authors: immunity may "worsen an initial injury" | Authors: "probably not the only explanation, as IS did not prevent neuronal degeneration" |

## 3 · Transfer limits, stated exactly

Rhesus macaque, suboccipital (ICM) injection, AAV9 capsid, CB7-type promoter, a secreted lysosomal-enzyme cargo, one necropsy at day 90 for the immunosuppressed groups, three and five animals in those groups, regimen of one antimetabolite plus an mTOR inhibitor, no taper study, the immunosuppressed arm confounded by its own morbidity. Nothing about an intracellular cargo, a WWOX cassette, any human regimen, or a time course.

## 4 · Ops (provisional; the integrator re-measures the insertion point and the record number)

### 4.1 · `disease-models/wwox/research/research_lines_current.md`

| field | value |
|---|---|
| op | `append` (new record, after the current final research-line record) |
| record | `RL-C-20261004w8c1 — The two 2018 rhesus ICM primaries behind the immunosuppression-rebound relay: single day-90 necropsy, small arms, no consistent reduction in the ganglion score, and one wording overreach in a secondary citation` |
| status | `open` |
| tag | `INFERENZA` (the readings are `DATO`; the comparison across the two studies is inference) |
| body | §1 and §3 of this candidate verbatim, with the §2 table |
| anchor | none required for an append |
| class | MINOR |

No `old` text is edited anywhere.

## 5 · What would change this, and what would falsify it

- **Would strengthen the rebound reading:** a primate study with DRG histology at several times after antimetabolite withdrawal against a never-withdrawn arm.
- **Would falsify it:** the same design with no rise after withdrawal.
- **Would reverse the "not clearly lower" reading:** an immunosuppressed arm of adequate size with a ganglion score outside the overlap of the untreated arm.

## 6 · Brief premises tested

- The selection said the first paper has "no immune-modulation arm". It has one (three animals), and the second has five.
- The selection called the first paper "the DRG-densest" and "the original observation". Both papers appeared together in the same issue; the second cites the first as a related paper. The lesion is also described earlier in piglets and juvenile macaques after intravenous AAV9-SMN1 (authors' own statement).
- The Discussion of PMID 30073179 says IS "can help alleviate", and in the same paragraph "hard to draw any definitive conclusions"; the panel supports only the second.

### LOCATOR TRIPLES FOR BLIND AUDIT

Format: `(proposition | verbatim quote | anchor)`. Each artefact is on disk and each quote was verified by the manifest validator against the artefact named for the PMID in brackets. Figure entries are attestations of panels read at native resolution, not string matches.

- [PMID 30073179, artefact `files/fulltext/PMID30073179_Hordeaux2018a_PMC.xml`] (MMF was withdrawn on day 60 (earlier in one animal), rapamycin continued; the regimen began three weeks before dosing. | Rapamycin was used for the entirety of the study, whereas MMF was stopped on study day 60. | Materials and Methods, Immunosuppression)
- [PMID 30073179, artefact `files/fulltext/PMID30073179_Hordeaux2018a_PMC.xml`] (The immunosuppression regimen itself caused diarrhoea, anorexia, weight loss and anaemia, starting before vector dosing. | The IS regimen administered to three animals caused adverse effects of decreased appetite, diarrhea, and weight loss that all started prior to test article administration. | Results, In-Life Safety Parameters, para 2)
- [PMID 30073179, artefact `files/fulltext/PMID30073179_Hordeaux2018a_PMC.xml`] (The text says incidence and severity trended lower with immunosuppression. | Overall, the incidence and severity of the DRG degeneration and axonopathy trended toward lower scores in the HD IS animals (Figure 3G). | Results, Histopathology, para 2)
- [PMID 30073179, artefact `files/figures/PMID30073179/gr3.jpg`] (Figure 3G: DRG cumulative score is about 2.7 (high dose), about 2.0 (high dose with immunosuppression) and about 2.3 (low dose), with overlapping error bars at three animals per group; axonopathy score is about 5.0 and 4.7 (high dose, day 90 and 180), about 2.4 (with immunosuppression) and about 4.4 (low dose), vehicle and day-14 zero. | [figure attestation — pixels cannot be quote-matched] Fig 3G bar charts, read at native resolution: DRG cumulative score bars Vehicle 0, HD D90 about 2.7, HD+IS D90 about 2.0, LD D90 about 2.3; axonopathy cumulative score Vehicle 0, HD D14 0, HD D90 about 5, HD D180 about 4.7, HD+IS D90 about 2.4, LD D90 about 4.4; error bars (SD) overlap in the DRG panel; individual animals plotted as symbols. | Figure 3, panel G)
- [PMID 30073179, artefact `files/fulltext/PMID30073179_Hordeaux2018a_PMC.xml`] (The authors state the DRG and axonopathy findings and the transgene-directed lymphocyte clustering were present in animals whose T-cell responses were pharmacologically suppressed. | However, these findings were still present in animals with pharmacologically suppressed T cell responses. | Discussion, para 3)
- [PMID 30073179, artefact `files/fulltext/PMID30073179_Hordeaux2018a_PMC.xml`] (The authors say immunosuppression may help but no definitive conclusion can be drawn because of cohort size. | it is hard to draw any definitive conclusions due to study limitations, such as cohort size | Discussion, para 6)
- [PMID 30073178, artefact `files/fulltext/PMID30073178_Hordeaux2018b_PMC.xml`] (The immunosuppressed arm is five animals at the two doses; mycophenolate mofetil from three weeks before dosing to day 60 and rapamycin to day 90. | The second experiment evaluated the two vector doses with a concurrent immune suppression (IS) regimen (n = 5). | Results, Study Design)
- [PMID 30073178, artefact `files/fulltext/PMID30073178_Hordeaux2018b_PMC.xml`] (The immunosuppression regimen caused anorexia, diarrhoea and weight loss starting before vector dosing. | Six animals received an IS regimen, which caused adverse effects of decreased appetite, diarrhea, and weight loss that all started prior to test article administration. | Results, In-Life Safety Parameters, para 1)
- [PMID 30073178, artefact `files/figures/PMID30073178/gr3.jpg`] (Figure 3F: DRG cumulative score about 3.4 (high dose), 1.1 (low dose), 3.0 (high dose with immunosuppression, two animals), 4.7 (low dose with immunosuppression); axonopathy about 4.0, 2.0, 2.0 and 3.3; vehicle zero; groups of two to three animals with wide SD. | [figure attestation — pixels cannot be quote-matched] Fig 3F bar charts, read at native resolution: DRG cumulative score Vehicle 0, HD about 3.4, LD about 1.1, HD+IS about 3.0 (two points), LD+IS about 4.7; axonopathy cumulative score Vehicle 0, HD about 4.0, LD about 2.0, HD+IS about 2.0 (two points), LD+IS about 3.3; individual animals plotted as symbols, SD error bars. | Figure 3, panel F)
- [PMID 30073178, artefact `files/fulltext/PMID30073178_Hordeaux2018b_PMC.xml`] (The authors state immunosuppression did not prevent neuronal degeneration, so the immune response is probably not the only explanation. | However, immune responses are probably not the only explanation, as IS did not prevent neuronal degeneration. | Discussion, para 3)
- [PMID 35229008, artefact `files/fulltext/PMID35229008_Buss2022_PMC.xml`] (The authors write that in earlier NHP studies immune suppression ablated T-cell responses but not DRG pathology. | immune suppression ablated T cell responses, but not DRG pathology | Discussion, para 9)
