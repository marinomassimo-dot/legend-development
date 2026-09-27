> Persisted verbatim by the Orchestrator's dispatch of 2026-09-27 (BATCH_20260927_004 wave-2 blind audit round). The auditor was **blind**: it received only the `(proposition, quote, anchor)` triples of the packets below, the source artefacts under `files/fulltext/`, and the current text of the target claims — no candidate, no dossier, no reader identity, no conclusions. Packets covered: CC-20260921-TX007-CEILING-AND-DOSE-CONTROL-01, CC-20260826-CLAIM002-01, CC-20260826-PROVENANCE-01.

# Blind locator audit B

Sources read: `files/fulltext/PMID42422765_Obeid2026_PMC_2026-09-27.xml`,
`files/fulltext/PMID34268881_Steinberg2021_PMC.xml`.
Absent from `files/fulltext/` (checked recursively): any artefact for PMID 34634460, PMID 42397075,
PMID 42128308.

## CC-20260921-TX007-CEILING-AND-DOSE-CONTROL-01

| # | proposition (short) | verdict | reason |
|---|---|---|---|
| 1 | WPRE removed as a precaution absent observed harm | SUPPORTED | Quote verbatim, single occurrence, inside the Discussion (offset 42490; Discussion begins 37885). The sentence is exactly a non-observation plus a proactive step; no safety result is asserted. |
| 2 | Price of removal: higher vector dose | SUPPORTED | Quote verbatim, single occurrence, last sentence of the WPRE Results subsection (next words are the heading "WWOX gene therapy improves survival and systemic phenotypes in a dose-dependent manner"). |
| 3 | Minimum effective dose known as capsids, not biology (Fig. 5 attestation) | UNVERIFIABLE_SURFACE | Figure/graph content: panel-level `ns` marks and survival outcomes are not matchable as text, and the named manifest is outside allowed reads. Partial text corroboration only: the Fig. 5 legend confirms twelve panels A–L at P30 and the two doses "LD (1.23 × 1011 vg) and HD (2.63 × 1011 vg)", and states "∗p < 0.05; ns, not significant; in G and H it is near significant, p value = 0.08 and 0.06, respectively". The "7 of 8 comparisons ns" count and the "opposite survival outcomes" pairing cannot be checked from the text. |
| 4 | P300 expression regional, cerebellum reached least (S5J / S6D attestation) | UNVERIFIABLE_SURFACE | Supplementary-figure numeric values are not present as text. Direction is text-corroborated but not the numbers: "Immunoblot analyses at P30 revealed a marked dose-dependent increase in WWOX protein, most prominently in the cortex and to a lesser extent in the hippocampus, midbrain, and cerebellum"; and "widespread, stable expression was maintained at P240 and P300 throughout the cortex, hippocampus, midbrain, cerebellum, and spinal cord (Figures S5J–S5K; Figures S6B–S6D)". |
| 5 | Expression explanation conditioned on the outcome (S5A–D "Dead" labels) | UNVERIFIABLE_SURFACE | Panel labels and the 1 HD / 3 LD split are image content; not matchable as text. The qualitative half is text-corroborated: "Notably, mice from either treatment group that failed to survive exhibited reduced WWOX expression, reinforcing the link between effective protein restoration and survival (Figures S5A–S5D)." |

Counts: SUPPORTED 2 · OVERSHOOT 0 · UNDERSHOOT 0 · NOT_IN_SOURCE 0 · UNVERIFIABLE_SURFACE 3.

Notes (not failures): triple 4's anchor lists two manifest entries covering two different supplementary figures; the text ties S5J–S5K and S6B–S6D to one P240/P300 statement, so the split between "S5J at P300" and "S6D at P300" is an anchor-granularity slip, not a meaning change.

## CC-20260826-CLAIM002-01

| # | proposition (short) | verdict | reason |
|---|---|---|---|
| 1 | All depolarizing-GABA language confined to one Discussion paragraph, support is general developmental neuroscience | SUPPORTED | Quote verbatim, one occurrence. "depolarizing" occurs 3× in the whole source, all three inside that one paragraph; every cited support in it is external (Obata 1978; Ben-Ari 2007; Murata & Colonnese 2020; Khalilov 2005) and no WWOX chloride/polarity measurement appears. |
| 2 | Depolarizing GABA stated as an idea strengthened, not a result | SUPPORTED | Quote verbatim: "...further strengthens the idea that depolarizing GABA plays a key role in seizure susceptibility", with the spectral-power evidence as the subject clause preceding it. |
| 3 | The clinical sentence drawn from that idea, not from a measurement here | SUPPORTED | Quote verbatim and is the sentence immediately after triple 2's, and it cites only external work: "These findings shed a new light on the lack of efficacy of common anticonvulsant therapies on immature neurons (Khalilov et al, 2005; Murata & Colonnese, 2020)". |
| 4 | Markers surprising to the authors, so marker direction cannot discriminate the two mechanisms | OVERSHOOT | Quote verbatim, and the surprise is the authors' own. The "cannot discriminate between the two mechanisms" half is not in the source; the source's own reading of the same pattern is: "This can indicate a disruption in development of normal and balanced neuronal networks, supporting the increased electrical activity observed in these organoids." The source says less than the proposition. |
| 5 | One functional inhibitory measurement, amplitude more than halved (sIPSC values) | UNVERIFIABLE_SURFACE | Source file absent: no artefact for PMID 34634460 anywhere under `files/fulltext/`, and the named deepdive manifest is outside allowed reads. |
| 6 | Source locates the effect in amplitude, not polarity | UNVERIFIABLE_SURFACE | Same absent source (PMID 34634460). |
| — | Machine-checked absences | SUPPORTED (partially) | Reproduced over `PMID34268881_Steinberg2021_PMC.xml`: `KCC2` 0, `NKCC1` 0, `gramicidin` 0, `bumetanide` 0. The "ten structured surfaces" table cannot be reproduced blind — it references the candidate's §2, which is outside allowed reads. |

Counts: SUPPORTED 3 · OVERSHOOT 1 · UNDERSHOOT 0 · NOT_IN_SOURCE 0 · UNVERIFIABLE_SURFACE 2 (plus one partially reproduced absence block).

Notes (not failures): two anchor-position slips of no consequence — triple 1's paragraph is the same paragraph that carries the GABAergic-marker sentence, not the one following it; triple 4's sentence sits mid-paragraph, the paragraph opening being "DEEs are a group of severe neurological syndromes whose underlying molecular pathology is unknown".

## CC-20260826-PROVENANCE-01

| # | proposition (short) | verdict | reason |
|---|---|---|---|
| 1 | Text asserts a WT comparison the panel does not draw | UNVERIFIABLE_SURFACE | Source file absent: no artefact for PMID 42397075 under `files/fulltext/` (recursive check). |
| 2 | No WT-versus-treated bracket in Fig. 6A(ii) | UNVERIFIABLE_SURFACE | Source file absent (PMID 42397075) and, additionally, declared figure/pixel content. |
| 3 | Scope of the rescue ("without correcting RG abnormalities") | UNVERIFIABLE_SURFACE | Source file absent (PMID 42397075). |
| 4 | Delivered WWOX spans 0.4×–7× WT (Suppl. Fig. 1 K–M) | UNVERIFIABLE_SURFACE | Source file absent (PMID 42397075); supplementary figure values also declared unmatchable as text. |
| 5 | Composition phenotype is the engineered KO's (Fig. 2D–F) | UNVERIFIABLE_SURFACE | Source file absent (PMID 42397075); figure content. |
| 6 | No randomization or blinding declared | UNVERIFIABLE_SURFACE | Source file absent (PMID 42397075). |
| 7 | Preprint identity has live downstream traffic | UNVERIFIABLE_SURFACE | Source file absent: no artefact for PMID 42128308 under `files/fulltext/`. |

Counts: SUPPORTED 0 · OVERSHOOT 0 · UNDERSHOOT 0 · NOT_IN_SOURCE 0 · UNVERIFIABLE_SURFACE 7.

Note: nothing in this packet was adjudicable blind; every anchor names a PMID whose full text is not in this checkout. This is a source-availability outcome, not a judgement on the triples.

## Totals across the three packets

SUPPORTED 5 · OVERSHOOT 1 · UNDERSHOOT 0 · NOT_IN_SOURCE 0 · UNVERIFIABLE_SURFACE 12.
