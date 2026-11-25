<!-- As delivered by one blind delegate (legend-delegate, claude-sonnet-5-5, effort high, read back from its transcript: 17 turns). Not edited below this line. -->
# Blind verification report

Date: 2026-11-25. Statements: `STATEMENTS.md` in this folder.

## Verdicts

| ID | Verdict | Source says more or less than the statement |
|---|---|---|
| A1 | NOT SUPPORTED | More: the body also carries the wording |
| A2 | NOT SUPPORTED | The review presents no such experiment |
| A3 | SUPPORTED (with limits) | Slightly more (other related sentences); one wording point |
| B1 | NOT SUPPORTED | Less: no such measurement |
| B2 | NOT SUPPORTED | Less: no U2OS activity assay at all |
| B3 | SUPPORTED (with limits) | More (further attempts, no reported wild-type control) |
| B4 | NOT SUPPORTED | C152W was not in the growth assay |

## Source A

File: `fulltext/PMID34359949_Hsu2021_PMC.xml` (article-type `review-article`),
SHA-256 `9a5985d0ce548f3f59117c74cc42bd908c1f1ba053ece8df2d51fe781d1beaec`.

Search: whole XML converted to text (front, abstract, keywords, body, captions, table, back matter, references). Case-insensitive: `tau|MAPT|neurofibril`; `direct|SDR`; `we (show|found|performed|determined|report|...)|our (data|study|...)|unpublished|data not shown|immunoprecipit|pull-?down|two-hybrid|FRET|surface plasmon|binding assay|Materials and Methods`; the xref targets 41 and 69.

### A1. NOT SUPPORTED

Abstract: "WWOX binds Tau via its C-terminal SDR domain and interacts with Tau phosphorylating enzymes ERK, JNK, and GSK-3β".

The body says it too, more strongly:

- Section 7, first sentence: "WWOX blocks Tau hyperphosphorylation by directly binding Tau via its C-terminal SDR domain [41,69]."
- Section 7, second sentence: "By direct binding, the SDR domain of WWOX restricts GSK3β-mediated hyperphosphorylation of Tau [41,69]."
- Section 6.1: "SDR domain binds and blocks GSK-3β-mediated tau hyperphosphorylation and thereby promotes neuronal differentiation [41,49]." (This sentence does not say unambiguously what the domain binds.)

### A2. NOT SUPPORTED

- The tau-binding sentences are all attributed to citations (section 7: [41,69]).
- Institutional Review Board Statement: "Not available for this review article." Data Availability: "Not available for this review article, except data for Figure 2 are at https://hbatlas.org/..." Figure 2 is database gene expression.
- The "our recent study" in section 9 is a p53/WWOX xenograft study cited as [76], not a binding experiment. No Methods section, and no co-immunoprecipitation or pull-down text, was found.

### A3. SUPPORTED, with these limits

- Abstract and both section 7 sentences are as quoted above; both section 7 sentences cite 41 and 69. No experiment of the review measures the binding.
- "Direct binding twice": only the first sentence names Tau as the partner. The second says "By direct binding, the SDR domain ... restricts GSK3β-mediated hyperphosphorylation of Tau" and leaves the partner implicit.
- Omitted: section 6.1 (cites 41 and 49, not 69) and section 10.3 ("WWOX needs to effectively bind tau and TPC6A∆ ... [41,69,70]", no domain named). "Citing 41 and 69" holds for section 7 only.
- Omitted: refs 41 (Sze 2004, J Biol Chem) and 69 (Sze, Wen, Chang 2020) are by authors of this review. They were not opened, so this check says nothing about whether either measured direct SDR-tau binding.
- Not checked: the Figure 1 graphic (not among the named files). The Figure 1 caption text names the SDR domain as a binding region without naming tau.

## Source B

Files: `fulltext/PMID33914734_Gersing2021_PMC8084241.xml`, SHA-256 `b21196f0f48864b045617e2d78f5e99ef215776f6cfca90d6fe4565be8ad63ea`; `supplement/PMID33914734/`; `figures/PMID33914734/`.

Search: whole XML (abstract, author summary, body, captions, methods, supplement captions, references, review sub-articles). Case-insensitive: `activ|enzym|kcat|catalytic|catalysis|assay|lysate|extract|COS|Pichia|pastoris|recombinant|purif|NAA|aspartat|U2OS|insoluble`. Response letter `s010.docx` read whole. `s009.xlsx`: sheet names and text strings only (Fig 1B, 2GH, 5FG, S1A, S1C, S5DE; no activity sheet). All main and supplementary figure images viewed (some at contact-sheet resolution; S2, S7, Fig 4 and Fig 6 individually); no activity measurement of accumulated protein found.

### B1. NOT SUPPORTED

- The only coupled enzyme assay used E. coli extracts (Methods, "Protein purification from E. coli and ASPA assays": "The reaction was initiated by addition of extracts of E. coli"), not protein accumulated by blocking degradation.
- Results: "ASPA C152W was not produced in significant amounts" (S2B Fig).
- Response letter: "it is possible that the C152W variant retains some enzyme activity, but we were unfortunately not able to test this directly".
- Growth rescue by bortezomib (Fig 2B) reads Ura3 reporter abundance, not ASPA activity.

### B2. NOT SUPPORTED

- No ASPA activity assay in U2OS cells is reported. U2OS work covers steady state, turnover, ubiquitination and solubility (Fig 6, S6-S8).
- Yeast: the lysate attempt (response letter only) failed on wild type: "there was not enough wildtype ASPA activity to obtain a reliable activity estimate". The yeast growth assay did not include C152W (S2C).
- The sentence "similar to the previous reports, we were unable to detect any enzyme activity" belongs to the E. coli extract assay, in which little or no C152W was produced. It is not a finding of no activity in yeast or U2OS.

### B3. SUPPORTED, with these limits

Support:

- Yeast, Results and Fig 4D, 4E: "The ASPA C152W protein that accumulated in absence of Hsp110 function was insoluble".
- U2OS, Results, Fig 6F and S7B: "It was completely insoluble, and accordingly also the accumulated protein in HSPH1 and HSPA4 knock-down cells was found in the insoluble fraction".
- No activity measurement of that protein (see B1).
- Too little protein: "ASPA C152W was not produced in significant amounts" (S2B; no GST-ASPA band visible in the C152W lane).
- Discussion: "Previous studies have been unable to detect any activity for ASPA C152W when expressed in COS-7 cells [15,17], while very low activity could be detected when expressed in Pichia pastoris [21]."

Limits omitted:

1. The yeast-lysate result is stated only in the response to reviewers (`s010.docx`). The article body and Methods report no yeast-lysate activity assay, and no data for it were found. The citation should say so.
2. The article reports no wild-type activity detected in the E. coli assay either ("we were unable to detect any enzyme activity"; wild-type kcat is described as very low). The assay therefore has no reported positive control. The response letter says "some wildtype ASPA" was produced.
3. The response letter lists two further routes: purification from mammalian cells was not possible because C152W is largely insoluble (cites Fig 6F), and the yeast NAA growth assay showed no ASPA-dependent effect (without C152W).
4. Insolubility is complete in U2OS; in yeast Fig 4E shows the accumulated protein mostly in the pellet with a faint soluble band. The solubility data are for Hsp110/HSPH1/HSPA4 loss (and yeast Hsp70 single deletions); the U2OS Hsp70 inhibitor experiment (Fig 6D) did not test solubility.
5. The paper is not consistent about the earlier reports. Results says previous studies "failed to show any residual enzyme activity for this variant when assayed as purified protein or in cell extracts [15,17,21]", while the Discussion and a later Results sentence ("albeit with very low activity [21]") give very low activity for ref 21. The cited papers were not opened.

### B4. NOT SUPPORTED

- S2 Fig caption (C): "Wild type yeast cells transformed with a control plasmid (vector) or an expression plasmid for wild-type ASPA were streaked ... on minimal media plates where either the carbon source (upper panel) or the nitrogen source (lower panel) was exchanged with N-acetylaspartate (NAA)."
- The S2C image has two lanes only on all four plates, "vector" and "ASPA wt". There is no C152W.
- Results: "we did not observe any ASPA-dependent effects on cell growth (S2C Fig) we did not pursue this further."
- Also: NAA was tested as carbon source or nitrogen source in separate plates. On nitrogen-source plates vector and wild type both grow, so growth there does not depend on ASPA.

## Scope notes

- Only `STATEMENTS.md` and the named source files were opened. `framework/protocols/delegation_budget.md` was not read, because the dispatch forbids reading anything else in the repository. Project instructions and a memory index were present in the session context automatically and were not used.
- No web access, no e-mail address sent, nothing from the download folders executed.
- Helper scripts are in `scripts/` in this folder; temporary text and image conversions were removed.
