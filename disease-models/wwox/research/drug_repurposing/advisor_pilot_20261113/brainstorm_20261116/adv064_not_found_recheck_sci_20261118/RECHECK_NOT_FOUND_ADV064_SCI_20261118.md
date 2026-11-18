# ADV-064: blind re-search of the abstract-level "not found" items of the age-window table (SCI, 2026-11-18; non-canonical; abstract level; mechanism and evidence level only; no dose, no schedule, no recommendation; reference genotype class only; not medical advice)

Written for: ADV (host); IT (arm-table consumer); a dated correction follows in the ADV-054 note, the in vivo brief and the VOI ranking. One delegate (`legend-delegate`, sonnet medium requested; transcript reads back claude-sonnet-5-5 on 35 turns plus one turn labelled claude-opus-5-5, unexplained), 12 tool calls, about 87,000 tokens. It was given only the nine items, the age window and the routes (Europe PMC field-tagged queries, PubMed abstracts, at least two independent formulations per item) and opened no repository file; I re-matched four pivotal quotes against its saved abstracts (all present) and resolved three PMIDs from its saved files. Producer table: `NOT_FOUND_RESEARCH_PRODUCER_DELEGATE_20261118.md`.

## Answer first
**One of my "not found" statements is overturned (diazepam ontogeny); one is partly updated (fenfluramine); six are confirmed.**
| Item | My ADV-054 statement | Blind re-search | Verdict |
|---|---|---|---|
| Z944 | not found in an age-window seizure paper | none found by routes A and B; adult ulixacaltamide (Harman 2026) and thalamic slices only | **confirmed** |
| TTA-A2 | not found | none with a stated age; one mouse electroshock paper (Sakkaki 2016, age not stated in the abstract, full text not open) | **confirmed, with an age-unresolved paper** |
| mibefradil | not found | adult WAG/Rij rats only | **confirmed** |
| ICA-069673 | not found | no rodent in vivo seizure paper at all | **confirmed** |
| XE991 in vivo | not found at P7 to P28; only in vitro | two in vivo mouse papers (Greene 2018, Xu 2017) with no age in the abstract; juvenile slices only | **confirmed for a stated age; two age-unstated in vivo papers exist** |
| eliprodil | not found in an age-window paper | adult kindling only | **confirmed** |
| other selective Cav3 blockers | none | none; an infant-rat pilocarpine paper measured Cav3.2 mRNA without a blocker | **confirmed** |
| fenfluramine | no acute provoked-seizure age comparison; the chronic Scn1a+/- paper had survival and pathology endpoints | same paper (Cha 2024, treatment from P7); plus one Scn1a+/- rat hyperthermia-seizure paper (Qian 2026) with the age not stated in the abstract | **partly updated**: still no acute age comparison; one age-unstated seizure-frequency datum added |
| diazepam ontogeny | "only a P10 rat datum inside a flupirtine paper; no dedicated diazepam ontogeny paper found" | **six papers, three with an explicit age comparison** (below) | **overturned** |

## The overturned item: diazepam (DATO at abstract level; saved abstracts matched)
* **Hasson 2008 (PMID 18337179, rat, P9, P15, P21, kainate and lithium-pilocarpine status epilepticus):** "high doses of DZP and PTB are needed to stop prolonged SE in developing rats, but their effectiveness is age dependent": at P9 diazepam did not stop the status epilepticus; at P15 and P21 it did, dose-dependently.
* **Suchomelova 2006 (PMID 16439585, rat, P15 and P28, lithium-pilocarpine):** "Diazepam was effective against acute SE at all time points tested" (the diazepam statements in the abstract are P15-specific; an early dose reduced later spontaneous seizures).
* **Kasahara 2019 (PMID 31058209, MOUSE, P11 and P14, hyperthermia-induced febrile seizures):** low-dose diazepam decreased clonic seizures at P11, and "high-dose administration of diazepam and pentobarbital exacerbated the behavioral and electrophysiological phenotypes of the induction phase of experimental FSs at P11 but not at P14" (a **paradoxical, age-dependent** effect in the mouse, at the lower edge of the experiment window).
* Single-age papers: Smythe 1988 (P7, PTZ, anticonvulsant), Albertson 1990 (23 to 25 days, amygdala kindling, anticonvulsant), Minlebaev 2011 (P5 to P9, flurothyl, anticonvulsant).

## What this changes
1. **Age-window table (ADV-054), the GABA-A row:** diazepam is **not** age-flat: status-epilepticus termination fails at P9 and works from P15 (rat); in the mouse a high dose worsens induction at P11 and not at P14. The row "midazolam, clonazepam, ganaxolone present at all ages (rat PTZ)" stands for PTZ; the diazepam statement ("only a P10 datum") is replaced by the above. Dated line added to the ADV-054 note.
2. **In vivo brief:** the only statement affected is section 6 item 3, where "diazepam ontogeny" is listed among the not-found items; it is now found. The assay-sensitivity panel (valproate, carbamazepine or CBD, ifenprodil or Ro 25-6981) names no benzodiazepine and is unchanged; the age series is **more** needed, not less, since an agent can flip direction between P11 and P14 in the mouse. Dated line 9.5 added.
3. **Arm-table cell I10 (PAM `+` or `0`, in vivo, owned by ADV and IT):** the evidence does not make the cell negative, but a benzodiazepine at high dose can be **pro-convulsant at P11 in the mouse**; the cell should carry "age-dependent, high dose paradoxical at P11" before it is read as flat.
4. **VOI ranking, #6 (E_GABA):** the earlier dated line argued that GABA-A modulators already work from about P10, which lowered #6 for the P13 to P17 window. The new diazepam rows are consistent with a mature chloride gradient from about P14 (the mouse exacerbation is at P11 and not at P14, and the rat status-epilepticus failure is at P9), and they weaken "from about P10": #6 stays lower for P13 to P17 and **stays as it was for any younger window**. Dated line added.
5. **Unchanged:** the T-type, Kv7-tool and GluN2B items (Z944, TTA-A2, mibefradil, ICA-069673, XE991, eliprodil): still no in-window rodent datum with a stated age; the arm order and the parked state of those strands do not change.

## Limits
Abstract level only; the diazepam result sets were large (306, 1,449 and 55 records) and the searcher reviewed the first 25 to 60 per query, so the diazepam list is representative, not exhaustive, and the fenfluramine, XE991 and TTA-A2 age questions remain open where the abstract states no age; one searcher and one comparison, the same discipline as the original table.
