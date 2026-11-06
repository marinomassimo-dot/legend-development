# Blind locator audit, triples_A1 (57 triples, 14 sources)

Emitted 2026-11-06 by the blind auditor (no access to the batch directory, registries, dossiers, receipts or manifests). Input: the triples file only. Method: framework skill legend-locator-audit (two questions per triple; verdict vocabulary SUPPORTED, OVERSHOOT, UNDERSHOOT, NOT_IN_SOURCE, UNVERIFIABLE_SURFACE). Not medical advice. Every quote was first matched mechanically (split on bracketed ellipses; normalisation levels 0 whitespace, 1 case, 2 NFKC + ligatures + Greek letters + unicode dashes/quotes, 3 strip underline marks and punctuation), then the passage around each hit was read to judge each asserted element (which child; intervention and tried/continued/stopped/added-on; symptomatic outcome and instrument; developmental outcome and instrument; imaging; label).

## Counts per verdict

- SUPPORTED: 45
- OVERSHOOT: 7
- UNDERSHOOT: 5
- NOT_IN_SOURCE: 0
- UNVERIFIABLE_SURFACE: 0
- total: 57

All 57 quotes were located as text (no figure/image cell was needed). Seven quote parts failed a flat search in the held two-column .txt extractions (Shaukat 2018, Tarta-Arsene 2017, Johannsen 2018) because of end-of-line hyphenation and interleaved columns; all seven matched verbatim in the PDF text layer after joining hyphenation (one needed the fi ligature normalised). The 18 Oliver 2023 Table 2 rows matched only after stripping underline marks (level 3); the underline semantics (underlined = current drug) was verified in the raw JATS markup (<underline underline-style="single">).

## Non-SUPPORTED triples and the exact reason

| triple | source | verdict | reason | suggested wording |
|---|---|---|---|---|
| A1-A1-03 | PMID 30361190 | UNDERSHOOT | Vigabatrin added with partial response, hemispasms in clusters at 11 months, Table 1 case 2 Poor with 4 AEDs, development: all carried. Imaging element omits bilateral posterior (parietal) polymicrogyria stated in text and Figure 3B caption. | imaging: MRI at two months: thin dysplastic corpus callosum, mild ventricular dilatation, wide CSF spaces with reduced white matter volume, bilateral posterior (parietal) polymicrogyria |
| A1-A1-18 | PMID 35573960 | UNDERSHOOT | Vigabatrin listed as ineffective and among current ASMs; up to 50 seizures a day; no milestones, never sat. Imaging omits the stated mild signal alterations of the pons and dentate nuclei and thinned corpus callosum at 2 years 4 months. | imaging: MRI at 2 years 4 months: mild progression of atrophy, marked periventricular white matter reduction with signal alterations (parieto-occipital), thinned corpus callosum, squared lateral ventricles, mild signal alterations of the pons and dentate nuclei; not discussed as drug-related |
| A1-A1-19 | PMID 35573960 | UNDERSHOOT | CBD oil listed as ineffective; stopped is inferred from the current-ASM sentence (vigabatrin, clobazam, clonazepam), which excludes it. Development carried. Same imaging omission as A1-18 (pons and dentate nuclei signal alterations). | imaging: MRI at 2 years 4 months: mild progression of atrophy, marked periventricular white matter reduction with signal alterations (parieto-occipital), thinned corpus callosum, squared lateral ventricles, mild signal alterations of the pons and dentate nuclei; not discussed as drug-related |
| A1-A1-20 | PMID 35573960 | UNDERSHOOT | ACTH had very poor results; development carried. Same imaging omission as A1-18 (pons and dentate nuclei signal alterations, thinned corpus callosum). | imaging: MRI at 2 years 4 months: mild progression of atrophy, marked periventricular white matter reduction with signal alterations (parieto-occipital), thinned corpus callosum, squared lateral ventricles, mild signal alterations of the pons and dentate nuclei; not discussed as drug-related |
| A1-A1-21 | PMID 35573960 | UNDERSHOOT | Diet did not significantly improve seizures and was suspended; development carried. Same imaging omission as A1-18 (pons and dentate nuclei signal alterations, thinned corpus callosum). | imaging: MRI at 2 years 4 months: mild progression of atrophy, marked periventricular white matter reduction with signal alterations (parieto-occipital), thinned corpus callosum, squared lateral ventricles, mild signal alterations of the pons and dentate nuclei; not discussed as drug-related |
| A1-A1-22 | PMID 42092735 | OVERSHOOT | Vigabatrin added to phenobarbital, spasms continued: none carried. Instrument overstated: the reported EEG precedes vigabatrin (at spasm recurrence) and the next EEG follows clobazam; no EEG is tied to this step. Development, imaging carried. | symptomatic outcome: none (clinical report; no EEG reported for the vigabatrin step) |
| A1-A1-32 | PMID 35792847 | OVERSHOOT | Seizures controlled on levetiracetam and topiramate at last visit carried. Improved rests on a one-time status (recently sitting alone, up to 10 words) not linked to the drugs. Source adds acute lymphoblastic leukaemia; last visit was a chemotherapy admission. | developmental outcome: not_reported (status at 2 years 5 months: global developmental delay with recent gains, sitting alone, up to 10 single words; not attributed to treatment) |
| A1-A1-33 | PMID 35792847 | OVERSHOOT | Vigabatrin added to valproic acid, topiramate, clonazepam at about 4 years 4 months; no outcome stated. Regressed is a status/history (profound delay and regression) at 4 years 6 months, not an outcome of a two-month-old addition. CT, no MRI carried. | developmental outcome: not_reported (status: profound developmental delay and regression; timing relative to vigabatrin not stated) |
| A1-A1-35 | PMID 35792847 | OVERSHOOT | Diet started at 11 months, tolerated, still followed; breakthrough seizures with fever; seizure-free about nine months at last visit. Source never says vigabatrin was current then, and adds that weaning off the diet was being considered. | symptomatic outcome: not_reported by diet (seizure-free about nine months at last visit, regimen not restated; breakthrough seizures with febrile illness; weaning off the diet under consideration) |
| A1-A1-55 | PMID 40126049 | OVERSHOOT | Table 2 WWOX (3 pts): 50 percent responder rate 2/3 supports two unlabelled responders; criterion and diaries/records per Methods. Add-on status is not stated for these patients; the source reports prior ASMs only. CGI 2/3, no development or imaging. | cannabidiol (tried; adjunctive status not stated for these patients) |
| A1-A1-56 | PMID 40126049 | OVERSHOOT | As A1-55: second of two unlabelled responders is an exact decomposition of 2/3; outcome and instrument carried. Add-on status not stated per patient. Developmental and imaging elements correctly absent. | cannabidiol (tried; adjunctive status not stated for these patients) |
| A1-A1-57 | PMID 40126049 | OVERSHOOT | 2/3 implies one non-responder (below 50 percent reduction), not zero benefit; none is the coder label. Supplement lists all 15 seizure-worsening and 19 CGI-worsening variants without WWOX, so worsening is excluded. Add-on status not stated. | cannabidiol (tried; adjunctive status not stated); symptomatic outcome: none by criterion (below 50 percent reduction; no worsening listed) |

Grouping: A1-18 to A1-21 share one imaging element for the same child; a single correction fixes all four. A1-55 to A1-57 share one unstated element (adjunctive status) for the same aggregate row. A1-32, A1-33 both code a one-time developmental status as an outcome of the intervention. A1-22 overstates the instrument for one step. A1-35 asserts a current drug the source does not restate. A1-03 omits a cortical malformation from the imaging element.

## Caveats recorded on SUPPORTED rows (no verdict change)

- A1-A1-08: source internally inconsistent: narrative chunk says progressive volume loss, Table 1 cell says stable volume loss; the row follows the chunk it cites.
- A1-A1-09: abstract speaks of the two children collectively; the per-child attribution is the plain reading of a two-case report, not an individuated statement.
- A1-A1-10: as A1-09.
- A1-A1-14: outcome cell PES, SF (6) is self-contradictory in the source; not an element of this row beyond the hormonal failure.
- A1-A1-17: imaging element omits the widened frontotemporal extracerebral space and widened left ventricle from the Figure 1 caption and text (same category as the listed findings).
- A1-A1-27: the source says responder (at least 90 percent reduction) at all three time points; partial is the coder floor because seizure freedom is not stated.
- A1-A1-30: the source says under control / controlled, not seizure-free; resolved is the coder mapping.
- A1-A1-39: MRI 8 m cell also lists cerebellum and peduncles; omitted from the row.
- A1-A1-45: the running text names hormonal therapy only for Patients 2 and 11; Table 2 lists PRED and ACTH for Patient 7 as well; the row follows Table 2.
- A1-A1-54: running text says died at age 8; Table 1 gives 8 y 3 m (deceased); consistent.
- A1-A1-19 (UNDERSHOOT on imaging): stopped is an inference from the current-ASM sentence, not an explicit statement.

## Artefacts read (route, bytes, sha256 computed from the file at emit time)

| key | route | file | bytes | sha256 |
|---|---|---|---|---|
| shaukat_pdf | held files/fulltext (read-only); PDF text layer via pdftotext, reading order + layout | /home/desktop/legend-development/files/fulltext/PMID30361190_Shaukat2018_JLE.pdf | 2144290 | 12e0930fa60a2c06a9ea3ca867506a24ff7d3a2d5eb5b7abeb686cd18d620958 |
| shaukat_txt | held files/fulltext (read-only); two-column interleaved text extraction | /home/desktop/legend-development/files/fulltext/PMID30361190_Shaukat2018_JLE.txt | 75964 | ae3103d907aceef77695534708bca43e6b476fca12b401ca0f8c0785842ade78 |
| chong_txt | held files/fulltext (read-only); Scholar Gateway delivered chunks 0,1,2,18,22-25 only | /home/desktop/legend-development/files/fulltext/PMID36537114_Chong2023_SGchunks_text_2026-10-21.txt | 29880 | b3a6d7a077c020ba402ae29556d9a8eba825c0d8d729216613d0d3cc69322ad9 |
| chong_json | held files/fulltext (read-only); Scholar Gateway JSON of the same chunks | /home/desktop/legend-development/files/fulltext/PMID36537114_Chong2023_ScholarGateway_20260929.json | 55601 | 8e2f19186b843000427b53c66c755bcbdd1a0aeb1088d119b258ea9f0fb4ba9b |
| pubmed_xml | NCBI E-utilities efetch db=pubmed retmode=xml, PMIDs 41442931,38407561 (abstract only; no contact parameter sent) | /tmp/claude-1000/-home-desktop-legend-development/9400b253-25a0-4b03-8822-96361325fc16/scratchpad/audit_A1/downloads/pubmed_41442931_38407561.xml | 23068 | a3b05956c00d035aad81237cb412b6a440de6ffc0788970d6cef5a912cfb0525 |
| nagarajan_xml | held files/fulltext (read-only); PMC JATS XML, tables rendered as cells | /home/desktop/legend-development/files/fulltext/PMID37583270_Nagarajan2023_PMC.xml | 250812 | 7820a11b0bbc0a35e091817dae382d9d5a16a55f8777ce122426d48512e364f6 |
| you_xml | held files/fulltext (read-only); PMC JATS XML | /home/desktop/legend-development/files/fulltext/PMID39101447_You2024_PMC.xml | 71261 | d077cc45b50e52dea87555d2c5ce0263aa5e4d97ee5b6032a26d9731426f312e |
| riva_xml | held files/fulltext (read-only); PMC JATS XML | /home/desktop/legend-development/files/fulltext/PMID35573960_Riva2022_PMC.xml | 57567 | e74bfe47c66e4ed906d4c61be665cc28e66717dc2dd98868a39094fba51c4ddc |
| serce_xml | held files/fulltext (read-only); PMC JATS XML | /home/desktop/legend-development/files/fulltext/PMID42092735_SercePehlevan2026_PMC.xml | 44418 | 19d041ace7703e21c54d75c2b27e69da9732603f6a0cab2ab6f0c401c5bf16e7 |
| oliver_xml | held files/fulltext (read-only); PMC JATS XML; <underline underline-style=single> marks checked in raw markup | /home/desktop/legend-development/files/fulltext/PMID36779245_Oliver2023_PMC_2026-09-27.xml | 180365 | 780f42de9b3982fa5bf9bf1e6bb76f71384c943aa197fb2d4de80be7ac7e7a34 |
| albaradie_html | held files/fulltext (read-only); JLE full-text HTML | /home/desktop/legend-development/files/fulltext/PMID35792847_AlBaradie2022_JLE_fulltext.html | 109376 | 034512f32f31e8483b95e83dfbd16973e6f459ebeabe970e62497fa723d81f87 |
| albaradie_pdf | held files/fulltext (read-only); JLE PDF text layer via pdftotext -layout (brief named *_fulltext.pdf, which is absent; this is the PDF present) | /home/desktop/legend-development/files/fulltext/PMID35792847_AlBaradie2022_JLE.pdf | 1644269 | 799208b99f5c7b1b9bac081d258a2d455491b644f5501a3ae42666127f1dc37e |
| tarta_pdf | held files/fulltext (read-only); PDF text layer via pdftotext, hyphenation joined | /home/desktop/legend-development/files/fulltext/PMID28721938_TartaArsene2017_JLE.pdf | 1280260 | a8ffcb4d19275c65a91a7eafd25411d2ef0eafbc569f52a92df06d570eb7fb8b |
| tarta_txt | held files/fulltext (read-only); text extraction | /home/desktop/legend-development/files/fulltext/PMID28721938_TartaArsene2017_JLE.txt | 17339 | d7fd2309280eca318ad4c4d8d8f204fc558c94ae8238168c5b16323ee6a1f879 |
| johannsen_pdf | held files/fulltext (read-only); PDF text layer via pdftotext, hyphenation joined | /home/desktop/legend-development/files/fulltext/PMID29808465_Johannsen2018.pdf | 1673779 | 0b2bce6f124ef868b0c12bb3b7eb439399ffb627f28babd424621988a52f8e49 |
| johannsen_txt | held files/fulltext (read-only); two-column interleaved text extraction | /home/desktop/legend-development/files/fulltext/PMID29808465_Johannsen2018.txt | 37558 | d41eda3764b7bcd93a523d0323cccbe8747c2bb572c991c89c192044ea1ac07d |
| ko_xml | Europe PMC REST fullTextXML for PMC6054992 (acquired by the auditor; no contact parameter sent) | /tmp/claude-1000/-home-desktop-legend-development/9400b253-25a0-4b03-8822-96361325fc16/scratchpad/audit_A1/downloads/PMC6054992_epmc_fullTextXML.xml | 96907 | e6f629eeac644299ebfd3a23fb763009f79623b0bf025947c2270dae53eced8c |
| cerulli_xml | held files/fulltext (read-only); PMC JATS XML | /home/desktop/legend-development/files/fulltext/PMID40126049_CerulliIrelli2025_PMC.xml | 128252 | 4f9434222213ea63e33d4c953cd914213084b4ce260214f79cd8aa25fd6e1438 |
| cerulli_supp_txt | held files/fulltext (read-only); supplement Appendix S1 text (pdftotext -layout) | /home/desktop/legend-development/files/fulltext/PMID40126049_CerulliIrelli2025_supplement/EPI-66-2253-s001.pdftotext-layout.txt | 8985 | fd7959ffaaa18277a728597aad0758fbb1277fa17d672250268ab29df7a6c84c |
| cerulli_supp_pdf | held files/fulltext (read-only); supplement Appendix S1 PDF | /home/desktop/legend-development/files/fulltext/PMID40126049_CerulliIrelli2025_supplement/EPI-66-2253-s001.pdf | 355581 | 324b37e3c39b179c5e4d1b60c3ee34f49a992a1fca6517f4a55d416e22dcd8db |

Supplement folders inspected but not needed for a verdict: PMID37583270_Nagarajan2023_supplement and PMID37583270_wwoxrows_supplement (Table 4 is text in the main XML); PMID36779245_Oliver2023_assets (figure images). PMID 30356099 (Piard 2019) was named in the brief but no triple cites it; it was not read.

## What could not be reached or does not exist

- PMID 36537114 (Chong 2023): no open full text (Europe PMC: not in EPMC, not OA). Only the eight delivered Scholar Gateway chunks (0, 1, 2, 18, 22, 23, 24, 25) were available; case narratives for patients 1 to 4 live in undelivered chunks, so every A1-04 to A1-08 verdict is scoped to the delivered surface, as the propositions themselves state.
- PMID 41442931 and PMID 38407561: abstract only (not OA on Europe PMC); fetched via NCBI efetch without any contact parameter. Rows A1-09, A1-10, A1-28 are abstract-level.
- PMID 30061856 (Ko 2018): acquired as Europe PMC fullTextXML for PMC6054992 (OA). Table 3 is text.
- The brief named PMID35792847_AlBaradie2022_JLE_fulltext.pdf, which does not exist in files/fulltext; the PDF present is PMID35792847_AlBaradie2022_JLE.pdf and was used (its text layer carries the clinical Table 1 with the Ambulation row that the HTML Table 1 lacks).
- PMID 40126049 supplement: the Appendix S1 text contains the Supplementary Results with both complete worsening lists (15 and 19 variants; WWOX absent) and only the heading of Table S1; Table S1 content is not in the text layer and was not needed.
- No bot check or blocked route was encountered. No e-mail address or contact parameter was sent to any service.

## Working files

Scripts (jats2txt.py, html2txt.py, dehyph.py, match_quotes.py, emit_audit.py), downloads and text conversions are in /tmp/claude-1000/-home-desktop-legend-development/9400b253-25a0-4b03-8822-96361325fc16/scratchpad/audit_A1/ (outside the repository). Match reports: match_report.txt and match_report_pdf.txt in that folder. Nothing was committed.

