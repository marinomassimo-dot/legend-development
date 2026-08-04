# Axis 3 — blind reviewer's raw reply

> Verbatim, unedited. A tally can be recomputed from the verdicts; a justification cannot be
> reconstructed once discarded, and the justifications are where the reviewer's reasoning is
> checkable.
>
> Reviewer: fresh session, no repository access, sides shuffled independently per anchor.
> Prompt: `dismech_axis3_blind_reviewer_prompt.md`. De-blinded analysis:
> `dismech_axis3_review_result.md`.

---

| id | verdict | one-line justification |
|---|---|---|
| α1 | DIFFERENT | β1 captures only the necessity of residues 388–407; it does not assert direct binding through the ADH/SDR domain or the specific requirement for L404. |
| α2 | ABSENT | β1 says nothing about inhibition of GSK3β kinase activity toward Tau. |
| β1 | SUBSUMED | The requirement for residues 388–407 is contained within α1, which additionally specifies the domain, direct binding and L404. |
| α3 | SUBSUMED | β2 expresses the same de-repression interpretation but additionally identifies increased Tau-directed output and excludes a GSK3β level change. |
| β2 | DIFFERENT | It adds experimental and mechanistic claims—Tau-directed output rises and GSK3β abundance does not—that α3 does not assert. |
| α4 | SAME | Both state that GSK3β abundance is elevated in the cortex, hippocampus and cerebellum of Wwox-null mice. |
| α5 | SAME | Both state that lithium suppresses PTZ-induced seizure susceptibility in Wwox-null mice. |
| β3 | SAME | Equivalent to α4, with "abundance" making explicit what "elevated" refers to. |
| β4 | SAME | Equivalent to α5; "significantly" does not change the underlying reported result. |
| α6 | ABSENT | β5 does not mention WW2 pre-ordering or stabilising WW1. |
| α7 | SAME | Both state that WW2 can directly bind the second PPxY motif when sequence and topology—including spacing, linker and orientation—are compatible. |
| β5 | SAME | Equivalent to α7 despite the more compact wording. |
| α8 | SUBSUMED | Its engineered-short-linker result forms the first part of β6, which also contrasts it with the native ErbB4 linker. |
| α9 | DIFFERENT | β6 reports only a weaker native-linker interaction; it does not assert predominant WW1 binding, tandem-affinity gain or very weak apparent WW2 affinity. |
| β6 | SPLIT | Its engineered-linker claim corresponds to α8, while its native-ErbB4 comparison corresponds partially to α9. |
| α10 | DIFFERENT | α10 generalises to any single PPxY peptide, whereas β7 is specifically about ErbB4 PY3 and also reports enhanced tandem-domain binding. |
| α11 | SAME | Both state that WW2 stabilises the otherwise unstable WW1 domain. |
| β7 | DIFFERENT | It concerns a particular ErbB4 motif and includes quantitative tandem-versus-WW1 affinity information absent from α10. |
| β8 | SAME | Equivalent to α11. |
| α12 | SUBSUMED | The 388–407 requirement is included in β10, which additionally compares the region with known GSK3β-binding motifs. |
| α13 | DIFFERENT | β10 gives only general similarity of residues 388–407 to Axin/FRAT/GSKIP motifs; it does not identify the 388–412 FXXXLI/VXRLE motif as conserved. |
| α14 | SUBSUMED | L404 dependence is contained in β11, which additionally reports the negative L311 control. |
| β9 | ABSENT | None of the α propositions explicitly states that binding occurs through the ADH/SDR domain. |
| β10 | SPLIT | It combines α12's residue-requirement claim with part of α13's motif-similarity claim. |
| β11 | DIFFERENT | It includes both L404 dependence and the informative L311 control, whereas α14 states only the former. |
| α15 | DIFFERENT | β12 omits the WT-versus-L404A comparison and GSK3β-dependent attribution, while adding that S422 is an MKK4 site. |
| α16 | ABSENT | β12 says nothing about restoration of Tau-dependent microtubule assembly. |
| α17 | ABSENT | β12 says nothing about RA-induced neurite outgrowth or SH-SY5Y cells. |
| β12 | DIFFERENT | Its site-specific phosphorylation claim lacks the L404A control and includes an MKK4-site attribution absent from α15. |
| α18 | SAME | Reciprocal co-immunoprecipitation is a specific method demonstrating the endogenous WWOX–GSK3β interaction described by β13. |
| β13 | SAME | Equivalent to α18 at the assertion level, although it omits the precise detection method. |
| α19 | DIFFERENT | α19 specifies RA differentiation, rising WWOX and falling Tau S396/S404 phosphorylation; β14 states only unchanged S9 and reduced GSK3β output. |
| β14 | DIFFERENT | "GSK3β output falls" is an interpretation, while α19 reports specific Tau phosphorylation changes and additional temporal context. |
| α20 | DIFFERENT | β15 includes loss of the WWOX effect after Tau knockdown but not loss of the GSK3β-knockdown effect; instead, it adds non-additivity. |
| α21 | SPLIT | Its non-additivity result corresponds to β15, while its linear-pathway interpretation corresponds to β16. |
| β15 | SPLIT | Its Tau-knockdown clause corresponds to part of α20, and its non-additivity clause corresponds to part of α21. |
| β16 | SUBSUMED | The linear WWOX–GSK3β–Tau pathway with Tau as effector is contained in α21, which also states the supporting non-additivity result. |

| anchor | split agrees (yes/no) | note |
|---|---|---|
| 1 | no | α produced two assertions; β produced one. |
| 2 | yes | Each reader produced one assertion. |
| 3 | yes | Each reader produced two assertions with matching boundaries. |
| 4 | no | α separated WW1 stabilisation from second-motif binding; β retained only the latter. |
| 5 | no | α separated engineered and native-peptide findings; β combined them. |
| 6 | yes | Each reader produced two assertions, although the first pair differs in scope and content. |
| 7 | yes | Each reader produced three assertions, but β combines the residue and motif claims differently and separately adds the domain claim. |
| 8 | no | α produced three assertions; β produced one. |
| 9 | yes | Each reader produced one assertion. |
| 10 | yes | Each reader produced one assertion, despite substantial semantic differences. |
| 11 | yes | Each reader produced two assertions, but the clause groupings differ. |

| verdict | tally |
|---|---:|
| SAME | 10 |
| SUBSUMED | 6 |
| SPLIT | 4 |
| DIFFERENT | 12 |
| ABSENT | 5 |
| **Total** | **37** |
