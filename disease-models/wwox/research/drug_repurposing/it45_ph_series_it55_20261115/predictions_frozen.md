# Predictions frozen before any paper body was opened (IT45-Q06, IT45-Q07, IT45-Q08)

Non-canonical working note. Not medical advice; no dose, schedule or route; no compound nominated. Reference genotype class only. Date 2026-11-15. context_policy: QUESTION_DRIVEN.

State of knowledge when this file was written: the two briefs; `ph_k2p_sci45_20261111/` (consumer_delta.md, output/tools.tsv, tools_roles.tsv, ph_sensitivity.tsv, evidence.tsv); `k2p_pointers_sci45_20261111/` (consumer_delta.md, output/answers.md, pointers.tsv); `nmda_asic_ph_sci45_20261111/` (consumer_delta.md, output/answers.md, proton_sensitivity.tsv, queries.tsv); the ledger status for PMID 40365404. These are repository secondary notes of earlier delegates, not bodies. No body of any paper on the candidate list below had been opened by this delegate. Metadata-level searches (Europe PMC REST, title/abstract/identifier only) may follow this freeze; any candidate added after it is logged in `queries.tsv` and, if it changes a prediction, in a dated addendum commit before its body is opened.

## IT45-Q06 (tools across pH 7.4 versus 7.6)

Tool list (from the SCI45 P1 tools_roles.tsv): ML365 (probe), PK-THPP and A1899 (family-level comparators), spadin (excluded), Zn2+ (TASK-3, conditional), ONO-TR-772 (TREK-1/TREK-2 inhibitor pointer), ONO-2920632, BL-1249, riluzole (restorability probes).

* P1. For ML365, PK-THPP and A1899, no primary read will contain a potency at two or more pH values for the same compound and preparation (about 85 percent each). The answer for these three will be "not stated" (not "insensitive"). Known single conditions: ML365 pH 7.4 (Tl+ flux, QPatch); A1899 and PK-THPP pH 7.4 in the recombinant parts read earlier.
* P2. A two-pH potency, if one exists for any K2P tool in the list, is most likely for the Zn2+ block of TASK-3 (H98/E70 dependence) or for a compound of another class acting on TASK/TREK (not a named tool); about 40 percent that any named tool has one.
* P3. Spadin (Mazella 2010 and later) and ONO-TR-772 have one pH only (oocyte pH 7.6 and CHO-K1 pH 7.4 respectively); BL-1249/riluzole activation at two pH: not found (70 percent).
* P4. Where a K2P compound shows a pH-dependent effect, it will be because the channel itself is pH-gated (TASK-1 pH50 about 7.3-7.4, TREK-1 about 7.5, TASK-3 about 6.3-6.5), so a change of "potency" will be confounded with a change of baseline current; a study separating the two will be absent.
* P5. Papers reaching a body read: 3 to 5 of at most 10; some candidates (J Med Chem, BMCL, JBC) will be paywalled or behind a bot check (about 40 percent of attempts).

## IT45-Q07 (true patch-clamp potency of the TREK-1/TREK-2 dual-inhibitor pointer)

Primary paper: PMID 40365404 (compound 14c / VU6018042; ONO-TR-772), already read partially by SCI45 Q1 (receipts -85, -86, source PMC bucket text plus SI). Candidate second-source: follow-up PMID 41104520 (methods).

* P6. The body states human TREK-1 manual patch-clamp IC50 15 nM explicitly in the abstract/results (about 70 percent); the QPatch 0.15 uM and Tl+ flux 0.26 uM are separate columns in a table. Therefore 15 nM is "the manual patch-clamp value as printed", 0.15 uM the automated patch-clamp value; both are patch clamp, and the question is which is the true one.
* P7. The paper's "more than 67-fold" selectivity is arithmetically 10 uM / 0.15 uM, which sides with 0.15 uM as the reference potency for selectivity, not with 15 nM (about 65 percent that the body or SI makes this reading checkable; about 25 percent that a decisive statement such as a table footnote exists).
* P8. Species human TREK-1 in CHO (stable line), mouse TREK-1 in the manual series; temperature room temperature or not stated (50 percent not stated); bath pH 7.4 or not stated (60 percent not stated for this compound); holding/step voltage not stated in the main text (60 percent); n per concentration reported as range or not stated (60 percent).
* P9. No pH series in the paper.

## IT45-Q08 (NMDAR proton response of GluN2B and triheteromers at 35 C, 1.3 mM Mg2+; layer II/III)

* P10. No source meeting both 35 C and 1.3 mM Mg2+ for GluN2B-containing or triheteromeric receptors will be found by the allowed routes (about 90 percent). Result: a supported abstention listing queries and returns.
* P11. A source with Mg2+ present (0.5 to 1 mM) and a pH series exists for native or recombinant NMDAR (about 35 percent; early Traynelis/Cull-Candy or Vyklicky work), without temperature near 35 C and without subunit identity.
* P12. A source at 30-37 C for NMDAR proton sensitivity exists as an abstract only (about 40 percent; earlier query returned PMID 8287051 unopened) and is not subunit-specific.
* P13. No layer II/III neuron source with a NMDAR proton series (about 90 percent). Native proton data will stay at P13-P19 isolated prefrontal neurons (Evlanenkov 2023) or cultured neurons.
* P14. A triheteromer proton midpoint, slope and residual will remain "not found in a primary" (about 80 percent); at most a qualitative statement (Hansen 2014 / Cheriyan 2016 indirect facts, already read).

## Budget and stop

At most 10 papers; one plain request per source; Europe PMC REST for identifiers/metadata (each query logged); PMC article pages for bodies; no PMC bursts; 8-12 s spacing; proof-of-work, captcha, bot check or HTTP 403 means access-blocked and a stop on that source.
