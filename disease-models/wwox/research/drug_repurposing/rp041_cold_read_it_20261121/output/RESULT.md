# RESULT: can the laboratory start without a call? (cold reader, two documents only)

## Answer first

**Only with named gaps closed. Not without a call as the documents stand.**

A laboratory can see the idea (a PTZ-provoked seizure test in knockout, heterozygous and wild-type pups, with ethosuximide and lithium arms, a reference-drug panel and a wild-type age series). It cannot run it, because the two documents do not (1) say which of them is current, (2) specify the stimulus, the seizure scale and the ethosuximide regimen, (3) give one sample-size target, (4) give a coherent pilot, (5) list the cells to run, (6) name the line, the genotyping and the source of wild-type pups, (7) give a rescue rule and an expected death rate, (8) supply the priors file that is said to govern conflicts, (9) state who pays, who owns the data and whom to ask, (10) give numbers for "panel valid" and "floor". None of these is a scientific objection; each is something a laboratory must write into a protocol and cannot find.

The two documents are not the same text. Document A (consolidated, dated 2026-11-19) folds the dated lines 9.1 to 9.12 of the original. Document B is the original (dated 2026-11-18) with its dated lines still appended, up to 9.17 on 2026-11-21, so it is later than A in some respects and earlier in others. Both are written for a "collaborating laboratory that reads this cold", but A also contains an operator section and first-person notes.

## Counts

| List | Items | Of which blocking a start |
|---|---|---|
| QUESTIONS.tsv (cannot answer from the documents) | 85 | 27 marked yes |
| CONFLICTS.tsv (conflicts or tensions) | 39 | n/a (each has a stated "follow today" or "cannot tell") |
| TERMS.tsv (terms needing plainer wording) | 75 | n/a |

Question categories: design 14, readouts 12, document_structure 11, genotype_and_controls 7, statistics 7, logistics 7, n_and_power 6, welfare_and_stopping 6, exposure_and_delivery 5, ages 5, terminology 5.

Conflicts where the laboratory "cannot tell" which text to follow (19 of 39): C02, C03, C05, C06, C08, C09, C16, C17, C18, C22, C23, C24, C25, C30, C31, C32, C33, C35, C36. In the other 20 a later or more specific line wins on its face, but the superseded text still stands next to it.

## The ten items that would block a start, ranked

1. **Which text governs (Q01, Q03, Q04; C17, C18).** A says it folds "9.1 to 9.12 of the original"; B carries dated lines to 9.17 (2026-11-21), after A's date, and keeps superseded body text (lithium "design variable", "four equal cells", "structure precedes seizure"). The number 9.12 is used for two different texts. No sentence tells the laboratory which to follow.
2. **Stimulus, scale and regimens are not specified (Q12, Q13, Q14, Q18).** PTZ is named only as what Cheng 2020 used; the laboratory is told to use "its own published standard assay". The lithium "replication condition" has no dose, route or interval between the three injections; ethosuximide has no regimen at all; grades 0, 1, 2 and 6 of the 0 to 6 scale are undefined.
3. **No single sample-size target (Q31, Q32, Q33, Q34; C04 to C08).** Per-cell n of 11, 22, 31, 36 to 109, 44, 50 and 180 to 320 are all in force; the interaction arithmetic is stated as "four times" and "twice"; "twice 36 to 109" is 72 to 218, not 180 to 320 (my arithmetic); the planning totals rest on an SD the text calls "not credible"; the 27-cell total does not apply the "vehicle about twice a test arm" rule; litter counts of 19, 25, 53 and 75 have unclear bases.
4. **The pilot cannot be run as written (Q19, Q20, Q21, Q22, Q37, Q39; C09, C10, C24).** It is "vehicle pups at candidate assay ages" with no ages listed, yet its stop rule and dose-check decision need panel-agent pups; "stage-matched wild-type response" is undefined; the stimulus fixed in the pilot must also serve older wild-type ages the pilot does not cover; the primary outcome (S or an incidence) is unresolved; knockout death is "about 4 weeks" in one place and "about day 17" in another.
5. **No cell and arm list (Q23, Q24, Q25, Q26; C20, C35).** The "27 cells" cover ethosuximide and two panel agents only; the T-type arm is inside the stage 2 row but optional; the lithium-alone arm, a second regimen and the second GSK-3 arm are added in text with no genotype coverage; "nine genotype-by-arm cells" is not enumerated.
6. **Line, genotyping and wild-type source (Q42, Q43, Q45; C25).** No allele, strain, source or repository; genotype must be "read before the test" with no method, sampling age or turnaround; "Wild-type and heterozygous animals are not limiting" is contradicted by 21 wild-type cells from 1:2:1 crosses (about 132 litters at 11 per cell, my arithmetic).
7. **Rescue rule and expected harm (Q61, Q62).** A rescue rule is "a requirement" but its trigger, procedure and whether a rescue drug is allowed are left open; deaths are expected ("a pup that dies keeps stage 6") yet only "about half of PTZ-injected knockouts reached status" is given. An ethics submission cannot be completed.
8. **The priors file is not supplied (Q06; Q84, T32, T33, T75).** "The hashed text governs any conflict" and it defines "generalised" for "P8"; the laboratory has only the hash.
9. **Terms of the collaboration and a contact route (Q74, Q75).** Funding, data ownership and authorship are "promised" by no one; no laboratory is named and "no agent contacts anyone", so the laboratory has nobody to ask.
10. **No numbers for "panel valid" and "floor" (Q67, Q68).** Every reading of a null depends on the panel being valid at an age and on vehicle S being above the floor; neither has a criterion.

## Other things the laboratory would meet at once (not in the ten)

- Add-ons and B lines 9.12 to 9.17 mix a second (neuron-targeted) line, serum chemistry, sIPSC recordings, a gene-addition benchmark and a "partial-restoration readout" that the design does not contain (C26, C27, C30 to C33, Q57, Q58).
- The sentence "This brief carries only the heterozygote bursting incidence" refers to a value neither document states (C16, Q55).
- Several referenced files are "reference not available to the laboratory": the priors file, EXPERIMENT_BRIEF_V1_1.md section 13.11, the slice package, ORDERING_PAGE.md, the age-window table, the dossiers and notes listed in A section 8 and the appendix.

## Files

- QUESTIONS.tsv, CONFLICTS.tsv, TERMS.tsv: the three lists.
- FOLDIN_PROPOSAL.md: a proposal for one clean current text (not an edit of either document).
- SEARCH_NOTES.md: how I read, what I could not read, my confidence per list.
