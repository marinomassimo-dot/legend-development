# Consumer note: WWOX, GSK3 beta, eIF2B (for the integrating session; nothing in a shared consumer was changed, nothing promoted)

Non-canonical, not medical advice. Package `gsk3_eif2b_20261107/`; verified by `verify/audit_g.md` (23 rows asked: 22 supported, 1 overshoot; residue table confirmed against UniProt with one offset corrected; the two absence claims held with two routes each).

**Result.** The chain is not established. Only the second link (GSK3 phosphorylates eIF2B epsilon) has support, outside WWOX. Link 1 rests on one single-lane Ser9 blot in Wwox-null mouse brain at P20, after seizure onset, with a heterozygote that is not intermediate; link 3 is split (one abstract says the dephosphorylated site did not significantly activate eIF2B; a mouse neuron paper shows a protein-synthesis labelling gain, which is not an exchange assay); links 4 and 5 are unmeasured in any WWOX system; "without a rise in phospho-eIF2 alpha" was tested by no source read. The path does give hypotheses distinct from "inhibit the ISR", but they are tests of the premise first. ISRIB is a discriminating probe, not an assumed rescue: its action depends on phospho-eIF2, and every rescue assay of the mutant-eIF2B paper included phospho-eIF2.

| Consumer | Proposed change and reason |
|---|---|
| `NEED-GSK3B-DEREPRESSION`, observation O1 | State that Ser9 is an inhibitory-site proxy from a single-lane blot at one stage, with a non-intermediate heterozygote; add phospho-eIF2B epsilon (rat Ser535 = human Ser540 = mouse Ser536) and the GSK3 isoform as the downstream read-out. |
| `NEED-ISR-ATTENUATION`, card `E01_isr_modulators` | An ISR-attenuation arm does not test the GSK3-eIF2B link: add a phospho-eIF2 alpha-independent arm to any design; do not read a GSK3 route as equivalent to phospho-eIF2 alpha inhibition. |
| INV-02 design | Add phospho-epsilon, exchange activity and per-cell translation read-outs beside phospho-eIF2 alpha and ATF4. |
| Priority | No promotion. A priority would rise only if phospho-epsilon at the GSK3 site is raised in WWOX-deficient neurons at matched stage; it would fall if it is not. The IT15 abstention on GSK3 compounds stands: Ser535 dephosphorylation is documented for LiCl, SB-415286 and SB-216763 only, not for the compounds the module names. |
| Receipts to record (staged, validated with the DOI check; event-ID order) | `FTR-20261107-12133000-70`, `-15001529-70`, `-15126504-70` (abstract only), `-26974342-70`, `-33220178-70`, `-29489452-70` (partial full text). Copies in `receipt_staging/gsk3eif2b/`. |

Condition to reopen the unreachable decisive datum: the full text of PMID 12133000 (the eIF2B activity result) and of 15001529 by a route the repository may use; or a deposited Wwox-null phosphoproteome or translatome (public-dataset search not run here; LEGEND can do it in silico). Title-only or unread leads: 32512016 (GSK-3 with PKR), 38352041, 11756553, 11500362, 11311121, 36572560, 34058790, 22193544. Everything beyond the residue table and that dataset search needs a laboratory (`output/experiment.tsv`).

Incident to know: a retry of a PMC page after a browser challenge was refused by the auto-mode classifier as bot-check circumvention; the producer stopped, nothing was worked around.
