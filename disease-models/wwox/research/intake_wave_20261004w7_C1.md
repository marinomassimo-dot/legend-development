context_policy: SOURCE_FIRST

# Intake wave 7 (2026-10-04), Scientist C1 — restoration spec: dose-driven, immune-driven or route-driven harm, and what part of DRG injury is addressable

Sources: PMID 42137271, PMID 42170349, PMID 41751597. Branch `task/sci-C1-20261004w7`. Receipts prepared (not appended): `scratchpad/receipts_pending_w7/sciC1_<pmid>_1.json`. Dossiers: `fulltext_dossiers/PMID<pmid>.md`. Manifests: `deepdive_manifests/PMID<pmid>.json` (all `VERDICT: PASS`). Candidates: `CC-20261004W7-C1-DRG-ATTRIBUTION-01`, `CC-20261004W7-C1-AGE-DOSE-CONFOUND-01`, `CC-20261004w7-C1-REGISTRY-01`. **None of the three mentions WWOX** (zero occurrences in each persisted artefact), which is an earned null for the gene; every lesson below is transferable only, with its limit stated. Not medical advice.

## First pass (written before any registry record, ledger or earlier candidate was opened)

| PMID | What it is | What it measures | What it states that matters here |
|---|---|---|---|
| 42137271 | Two-author commentary (PubMed type News), no abstract, no data | Nothing; relays a macaque primary | Severity of AAV DRG toxicity tracks transgene expression; whole-study dexamethasone plus tacrolimus plus mycophenolate reduced but did not eliminate it; the primary did not taper, found no direct T-cell killing, and did not place immunity upstream of cell stress; earlier work (relayed) saw a rebound after antimetabolite withdrawal at day 60; the decisive experiment is a promoterless payload with an immune response then DRG toxicity; lowering dose or restricting expression is favoured over broad immunosuppression |
| 42170349 | Single-author commentary (News), no data | Nothing; relays a liver profiling primary (systemic high-dose AAV9-SMN1, macaque and rat) | Unfolded-protein response (PERK branch) magnitude tracked transgene expression, rats expressed less and lacked it; three dose-scaled stimuli (vector DNA damage response, innate sensing by TLR2 and TLR9, supra-physiologic transgene synthesis); DRG dose-related toxicity is mentioned in one sentence with two citations |
| 41751597 | Peer-reviewed mouse study (*Genes*), wild type, self-complementary AAV9 with strong promoter and GFP | Vector genomes by qPCR and GFP IHC across four routes and four ages, survival, H&E of euthanised animals | Day-1 IT 47 percent mortality, day-1 IT plus ICV 39 percent, day-5 IT 70 and 17 percent by dose, none by IV at any age, no significant survival difference at day 10 or 28; every euthanised animal had spinal cord injury and **no DRG abnormality**, while DRG GFP area was about 60 to 90 percent at day 1 and day 5 by every route; the authors attribute deaths to local GFP overexpression, untested |

## The answer to the assigned question, with limits

**Question.** Is the harm of a CSF-route AAV dose dose-driven, immune-driven or route-driven, and is DRG injury an addressable and measurable lesion?

**What these three sources support.**

1. *Dose-driven and route-driven are shown measurably only in the mouse study, and they are confounded with the transgene.* In neonatal mice the same capsid and the same total vg killed 47 percent by lumbar intrathecal and none by ICV or IV (day 1), mortality rose from 17 to 70 percent with a doubling of IT dose (day 5), and the half-dose IT within IT plus ICV killed fewer than IT alone. That ordering follows local spinal exposure and dose. It does not separate those from a toxic transgene: GFP, a strong promoter and a self-complementary genome are all in play, there is no null-cassette arm, no expression measurement in the dead animals, and no immune endpoint.
2. *Immune-driven is argued, not measured, in both commentaries.* Neither measures anything. They relay a primate result in which immunosuppression reduced but did not eliminate DRG toxicity, and they add a duration caveat (no taper; rebound after withdrawal in earlier work) and a design that would place the immune response relative to cell stress (promoterless payload), which nobody has run.
3. *DRG injury as addressable and measurable.* Measurable: yes in primates (histology, relayed) and the mouse study shows DRG exposure can be quantified by IHC. Addressable: the commentary camp says by limiting transgene burden (dose, promoter, microRNA-binding sites) first, innate-step suppression second, broad immunosuppression last; the mouse study shows **DRG spared despite heavy transduction in euthanised animals** and the lesion that killed was in the spinal cord. That is a lesion-location result, not evidence that the mouse DRG is safe (survivors' DRG histology is not reported).

**What the three do not support.** A bound on any WWOX cassette, dose, route or age; any statement about WWOX-driven ER stress; any human infant regimen; any tolerisation claim; any neurofilament or other biomarker.

## Comparison with what is held (read only after the first pass)

Records compared: `RL-C-20261003w4a` (landed), `CC-20261003W6-C-DRG-ATTRIBUTION-01`, `CC-20261003W6-C-IMMUNOSUPPRESSION-LIMIT-01`, `CC-20261003W5-C-TRANSGENE-NULL-IMMUNOSUPPRESSION-01`, `CC-20261003W3-C-RESTORATION-SPEC-01`, `CC-20261003W5-C-DOSE-SCALAR-01`, `CC-20261003W5-A-WINDOW-STATUS-01`, `CC-20261003w4-C-WINDOW-SPEC-01`. The row-by-row table of what each source **adds, bounds or leaves untouched** is §2 of `CC-20261004W7-C1-DRG-ATTRIBUTION-01`. In short:

- **Identical to held, merged and not restated:** the partial effect of immunosuppression on DRG toxicity and its dependence on transgene expression (both are findings of the Biogen primary already held as PMID 41404412; the commentary only reads it).
- **Increments added:** the withdrawal-rebound datum (relayed, not read first-hand), the promoterless-payload discriminator, the three-stimulus decomposition of "dose", the mouse exposure-without-DRG-injury datum, and the age-by-dose-per-tissue confound with qualification of the "younger is higher" sentence.
- **Bounded:** the held sentence that the immune mechanism does not hold in mouse, so no rodent WWOX study can test the question, is neither confirmed nor refuted; this mouse study shows exposure is present, but reports no DRG histology of survivors and has no immune endpoint.
- **Untouched:** the calcineurin-inhibitor hypothesis, neonatal tolerisation (measured nowhere in this set), every WWOX claim.

## Panel and table checks (the wave-4 lesson, applied)

Reading panels changed one summary sentence of the mouse paper. The authors' "regardless of route, younger is higher" is carried by CSF-route IHC; the IV arm shows no fall with age (about 10, 16 and 14 percent caudal GFP area at days 1, 5 and 28, panel read) and whole-cerebrum qPCR is not monotonic (ICV 0.294 at day 1 versus 0.396 at day 28; table cells). The same panel read confirmed the survival percentages (Figure 1a and 1b group sizes reproduce them and the Table 1 survivor counts), so Table 1 lists survivors and a footnote marks the high-mortality group as not fully enrolled. Figure 6 (eye) and Figures 4 and 5 were not inspected as images.

## Brief premises tested

- "PMID 42137271 is the direct counterweight to the wave-6 C1 reading": **wrong in scope.** It is a commentary on a macaque primary already held; it contributes no data.
- "PMID 42170349 is the dose-side counterpart naming mechanisms that scale with dose rather than immunity": **partly wrong.** It is a liver, systemic-route commentary; its mechanisms (DNA damage, innate sensing, overexpression) include an immune arm, so it does not separate dose from immunity; its DRG content is one citation-backed sentence.
- "PMID 41751597 has no toxicity endpoint named in the abstract": true of the abstract, **wrong of the paper** (mortality and spinal-cord histology are in the Results; Table A2).
- "Hordeaux 2020 reported age at injection as significant but is publisher-blocked; this is measurable and open": **partly wrong.** The mouse paper measures biodistribution, not toxicity, by age, and its age effect is dose-per-tissue confounded; it does not replace a toxicity-by-age primate source.

## Harness finding (not acted on)

`deepdive_manifest.py`'s printable-substitution screen refuses any surface where a one-character token ¼ stands between alphanumerics ("rotated ¼ turn" in a clean MDPI JATS), a false positive of a pattern written for Elsevier/LiveCycle text layers. Worked around by declaring the JATS as `article_binary` and a documented derived text layer as `article_text`. A better fix would exempt publisher JATS or require the pattern to co-occur with another substitution; left to Harness Engineering.

## What I did not read

The relayed liver primary behind PMID 42170349 (a PubMed record exists; not acquired); the two earlier rhesus ICM papers and the microRNA-detargeting paper cited in PMID 42137271; the 62 references of PMID 41751597 beyond enumeration and screening; Figures 4 to 6 and A1 to A5, A7 to A11 of PMID 41751597 as images.

## DEFAULTS_TAKEN

1. Declared the JATS of PMID 41751597 `article_binary` and a derived text layer `article_text` (reason above); the receipt's `source_locator` is the derived text.
2. Gave the two commentaries `complete_fulltext_read` (every existing section read; figure inspected) and the mouse paper `partial_fulltext_read` (figures partly captions-only).
3. Wrote two research-line candidates and one registry candidate rather than editing any held record; no `old` text is edited anywhere.
4. Hard-linked `files/` into the worktree to run the dependency screen and the manifest verifier.

## DECISIONS_TAKEN

None that §21d reserves.

## STOP_LOG

None. No classifier halt occurred in this run.
