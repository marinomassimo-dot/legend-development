> Persisted verbatim by the Orchestrator's dispatch of 2026-09-27 (BATCH_20260927_004 wave-2 blind audit round). The auditor was **blind**: it received only the `(proposition, quote, anchor)` triples of the packets below, the source artefacts under `files/fulltext/`, and the current text of the target claims — no candidate, no dossier, no reader identity, no conclusions. Packets covered: CC-20260826-DOSE-ADJUDICATION-01, CC-20260826-DOSE-DECISION-TABLE-01, CC-20260922-CLAIM011-DOSE-ENDPOINTS-01, CC-20260826-AAV9-ENDPOINT-SPLIT-01.

# Blind locator audit A — four packets

Sources actually found and read (tag-stripped full text, whole-file string search):
- `/home/desktop/legend-development/files/fulltext/PMID42422765_Obeid2026_PMC_2026-09-27.xml` — present, 170,134 bytes, full JATS body + all figure captions.
- `/home/desktop/legend-development/files/fulltext/PMID34747138_Repudi2021_PMC.xml` — **present**, 163,659 bytes, full body + captions. Several anchors declare these bytes "absent from this checkout"; that declaration is wrong for this checkout and the affected text quotes were verified directly (noted per triple).
- No supplementary artefact exists for either PMID in `files/fulltext/` (no `mmc1.pdf`, no `*supplement*` for 42422765 or 34747138). Every S-figure / panel-value triple is therefore unverifiable here, and figure panel pixels are in no case text-matchable from the XML, which carries captions only.
- Superscripts are flattened by tag-stripping, so `1.23 × 1011 vg` in a packet matches `1.23 × 10^11 vg` in the source; treated as verbatim.

## CC-20260826-DOSE-ADJUDICATION-01

| # | proposition (short) | verdict | reason |
|---|---|---|---|
| 1 | WPRE removal was a precaution, not a safety result | SUPPORTED | Quote verbatim in Discussion, exactly as anchored: "Although no overt toxicity was observed in prior studies, we removed WPRE as a proactive risk-mitigation step to improve the predictability and control of neuronal WWOX expression for potential clinical translation." Source says the same, no more. |
| 2 | lower expression must be bought back with more capsid | SUPPORTED (note) | Quote verbatim and is indeed the final sentence of the Results subsection titled "Removal of WPRE enables controlled WWOX expression while maintaining therapeutic efficacy at higher vector doses". Note: the trailing clause "which is what makes a vg number a property of the construct rather than of the biology" is the reader's inference; the source asserts only the dose necessity. |
| 3 | doses printed as bare `vg`, no unit convention in running text | SUPPORTED | Quote verbatim. Verified exhaustively: every dose token in the article (4 × 10^10, 8 × 10^10, 1.23 × 10^11, 2.63 × 10^11) is printed as bare "vg" in body text and in the Figure 2, 3, 4, 5 and 6 captions; no "/hemisphere", "/animal" or "total" qualifier occurs anywhere with a dose. |
| 4 | Methods state no dose; only the titre assay | SUPPORTED | Quote verbatim and is the final sentence of "Plasmid vectors", the first Materials-and-methods subsection. Verified: no dose figure of any kind occurs after "Materials and methods" — the only vector quantity is "Viral titers were determined by RT-qPCR using bGH primers." |
| 5 | bilateral, one injection per hemisphere, bounding ambiguity at 2× | SUPPORTED | Quote verbatim in "ICV injection of AAV particles into P0-P5 Wwox-null mice"; the next-but-two sentence closes it: "The procedure was repeated for the contralateral hemisphere." |
| 6 | Repudi's total is ≈4 × 10^10 GC (per hemisphere, twice) | SUPPORTED (note) | The anchor's "artifact bytes absent, attestation carried forward" is incorrect: the file is present and the quote is verbatim — "Approximately 1 µl (2 × 10^10 GC/hemisphere) virus was dispensed using a NanoFil syringe … The other hemisphere was injected in the same way." Results corroborate: "Viral particles (2 × 10^10 /hemisphere) … were injected into the ICV region". The ≈4 × 10^10 total is arithmetic on two sourced sentences, not a source statement. Note: "re-acquisition owed" is not owed. |

Counts: SUPPORTED 6 (2 with notes) · OVERSHOOT 0 · UNDERSHOOT 0 · NOT_IN_SOURCE 0 · UNVERIFIABLE_SURFACE 0.

## CC-20260826-DOSE-DECISION-TABLE-01

| # | proposition (short) | verdict | reason |
|---|---|---|---|
| 1 | Methods contain no dose, only the titre assay | SUPPORTED | Same verification as packet 1 #4: quote verbatim, final sentence of "Plasmid vectors", and no dose figure occurs anywhere in Materials and methods. |
| 2 | bilateral, one per hemisphere → `vg` ambiguous by exactly 2× | SUPPORTED | Quote verbatim; "The procedure was repeated for the contralateral hemisphere." is in the same subsection. |
| 3 | doses printed as bare `vg`, no per-hemisphere/per-animal qualifier | SUPPORTED | Quote verbatim; no dose token in the article carries a basis qualifier. |
| 4 | Repudi basis per hemisphere, both injected, comparator total ≈4 × 10^10 GC | SUPPORTED (note) | Quote verbatim in the Repudi Methods, which are present in this checkout despite the "bytes absent" declaration; the total is arithmetic over the two sourced sentences. |
| 5 | S3E region-dependent non-linearity (cortex 3.0, hippocampus 3.0, midbrain 5.5, cerebellum 16.7) | UNVERIFIABLE_SURFACE | Supplementary Figure S3 panel E: no supplementary file for PMID 42422765 exists in `files/fulltext/` (no `mmc1.pdf`), and panel densitometry is not text in the JATS. Nearest source text neither states nor contradicts the ratios: "immunohistochemical and immunoblot analyses of WWOX expression confirmed a dose-dependent increase, with low expression observed at 4 × 10^10 vg in the absence of WPRE and markedly higher levels at 8 × 10^10 vg" and "increasing the vector dose in the absence of WPRE failed to recapitulate the expression levels achieved with lower dose (LD) containing WPRE (Figure S3F)" — no per-region multiplier anywhere. Note: the entry is a sentence fragment, not a proposition, so even with bytes there would be nothing to test MORE/LESS against. |

Counts: SUPPORTED 4 (1 with note) · OVERSHOOT 0 · UNDERSHOOT 0 · NOT_IN_SOURCE 0 · UNVERIFIABLE_SURFACE 1.

## CC-20260922-CLAIM011-DOSE-ENDPOINTS-01

| # | proposition (short) | verdict | reason |
|---|---|---|---|
| 1 | LD and HD values are in the running text, not only on a panel | SUPPORTED | Quote verbatim in the first paragraph of the Results section "WWOX gene therapy improves survival and systemic phenotypes in a dose-dependent manner", exactly as anchored. (They also recur in the Figure 3A, 5, 6F captions — consistent with, not contrary to, the proposition.) |
| 2 | Methods state no dose; only the titre assay | SUPPORTED | Quote verbatim, final sentence of "Plasmid vectors"; no dose in Methods. |
| 3 | one injection per hemisphere at a fixed volume, bounding ambiguity at two | SUPPORTED | Quote verbatim in the ICV Methods subsection. |
| 4 | contralateral hemisphere receives the same injection | SUPPORTED | "The procedure was repeated for the contralateral hemisphere." verbatim, third sentence after the pump sentence in the same subsection. |

Counts: SUPPORTED 4 · OVERSHOOT 0 · UNDERSHOOT 0 · NOT_IN_SOURCE 0 · UNVERIFIABLE_SURFACE 0.

## CC-20260826-AAV9-ENDPOINT-SPLIT-01

| # | proposition (short) | verdict | reason |
|---|---|---|---|
| 1 | text asserts no significant locomotor difference (which caption + panels refuse) | SUPPORTED (note) | Quote verbatim in the Results behaviour paragraph: "Locomotor activity parameters, including movement velocity and total distance traveled, as well as spatial exploration of center and periphery zones, showed no significant differences between groups (Figures 4B, 4D–4G)". The first clause of the proposition is fully sourced. Note: the "which the caption's asterisk definition and the panels refuse" clause is not decidable from text — see #3. Also relevant and adjacent in the same paragraph, in the source's own voice: "Treated KO mice exhibited significantly higher motor coordination and learning compared with WT mice (Figure 4K)." |
| 2 | Figure 4 caption fixes the asterisk's meaning | SUPPORTED (note) | Quote verbatim as the final sentence of the Figure 4 caption, comma and all: "Statistical analysis was performed using Student's t test (∗p < 0.05; ns, not significant), Error bars represent mean ± SD". Note: the added "so the sentence and the panels cannot both be right" depends on the panel content, which is image-only here. |
| 3 | three of eight Figure 4 panels significant vs WT, in the exceed direction (4D ~9.5 vs ~11.5; 4E ~3400 vs ~4300) | UNVERIFIABLE_SURFACE | Panel values and brackets are figure pixels; the JATS carries only captions and there is no figure asset or supplement for this PMID in `files/fulltext/`. The text moreover states the opposite for 4D–4G ("showed no significant differences between groups (Figures 4B, 4D–4G)") while conceding one exceedance outside the locomotor set ("significantly higher motor coordination and learning compared with WT mice (Figure 4K)"), so the conflict cannot be adjudicated without the bytes. |
| 4 | no untreated-disease arm at P90 and none possible; only comparison is vs WT | SUPPORTED (note) | Quoted fragment verbatim. The full source sentence is broader and carries the untreated arm, which the fragment elides: "Behavioral testing could not be performed in untreated Wwox-null mice due to severe morbidity and early lethality, and LD-treated mice did not survive to P90; therefore, analyses were limited to WT and HD-treated groups." Source says slightly MORE than the quote, and supports the proposition. |
| 5 | epilepsy panel prints a non-significant value where the text claims significance | UNVERIFIABLE_SURFACE | The text leg is verbatim: "Averaged spike counts further confirmed a significant elevation in spike activity in KO animals (Figure 7C)"; the Figure 7 caption fixes the convention ("Statistical significance was determined using Student's t test. ∗p < 0.05; ns, non-significant. … mean ± SEM; n = 5 littermates per group"). The load-bearing assertion — `0.2000` printed above the WT–KO bracket — is panel pixels, absent from this checkout, so the contradiction is not testable as text. |
| 6 | myelination in the dose study never quantified in a treated arm | UNVERIFIABLE_SURFACE | Figure S7 panel I is supplementary and no supplementary artefact for this PMID exists here. Main-figure captions are consistent with the proposition — quantification is KO-vs-WT only ("(C–E) Bar graphs showing significant reduction in brain weight (C), CC thickness (D), and MBP intensity across regions (E) in KO mice relative to WT controls") while the treated arms are "(F) Representative MBP staining in WT and AAV9-hSynI-hWWOX-treated KO mice at LD … and HD …" — but the text cites both panels for the treated result ("HD treatment achieved near-complete rescue across affected regions, whereas LD treatment produced only partial recovery relative to HD (Figures 6F; S7I)"), and whether S7I carries a graph cannot be checked. |
| 7 | on the one myelin panel comparing treated with WT, the comparison is significant against the rescue (WT ≈26 vs treated ≈52, `**`) | UNVERIFIABLE_SURFACE | The Repudi bytes are present, contrary to the anchor, but the panel values and brackets are EM-figure pixels. Caption confirms the panel exists and what it plots — "Graph represents the number of unmyelinated axons (corpus callosum) per FOV counted from representative EM images shown in D" — and the Results text states the direction-free version, with the paper's own hedge: "when comparing myelin thickness of KO+AAV-mWwox and WT corpus callosum at P17 and 6 months, we observed some minor differences in the g-ratio and the number of unmyelinated axons (Fig 5C, E and F)". The magnitude (≈2×) and the `**` marker are not text-matchable, and "minor" is the only qualifier the text supplies. |

Counts: SUPPORTED 3 (all with notes) · OVERSHOOT 0 · UNDERSHOOT 0 · NOT_IN_SOURCE 0 · UNVERIFIABLE_SURFACE 4.

## Totals across the four packets

SUPPORTED 17 · OVERSHOOT 0 · UNDERSHOOT 0 · NOT_IN_SOURCE 0 · UNVERIFIABLE_SURFACE 5 (all of them figure panels or supplementary S-figures: 4 for PMID 42422765 where no supplementary file exists in this checkout, 1 for PMID 34747138 EM panel pixels).

Cross-cutting note: three anchors in packets 1, 2 and 4 declare the PMID 34747138 artefact bytes "absent from this checkout"; the file is present and every text quote drawn from it verified verbatim. Conversely, the supplementary artefacts the S-figure triples depend on (PMID 42422765 `mmc1.pdf`) are genuinely absent.
