# CC-20261004W11-A-ORTHOGONAL-01 — an independent laboratory measures a WWOX interaction that maps to the SDR region, and it is a protein partner, not a substrate

`context_policy: SOURCE_FIRST`. **Author:** ACTOR_ID `scientist`, Scientist A of intake wave 11,
2026-10-04. **Source:** PMID 37248434, receipt `FTR-20261004-37248434-01`, manifest
`deepdive_manifests/PMID37248434.json` (11 locators, strict PASS, 0 gaps).
**Change class: MINOR.** It adds a lead and narrows nothing that is a `consolidated baseline` claim;
it introduces no new claim record. **Nothing here is medical advice.**

## 1 · What the source adds

The WWOX enzymology question this wave is auditing asks whether anyone outside the
Bednarek / Aqeilan / Chang–Aldaz chain has measured a WWOX *enzymatic* or *ligand-binding* activity.
This source is the first orthogonal-laboratory measurement of a WWOX **binding** event that the
corpus has read in this wave: an Institut Curie / INSERM group, with its own antibody and its own
two-hybrid pipeline, measures a WWOX–MERIT40 interaction by three independent formats (yeast
two-hybrid, co-immunoprecipitation of tagged constructs in HEK293, endogenous co-IP in MCF7).

Three facts from it matter to the SDR question, and all three are about **protein binding**:

1. The interaction **does not use WW1**: a Y33R mutation that abolishes PPxY binding leaves it intact.
2. The determinant maps to a **WW2-SDR** fragment, while a WW1-WW2 fragment does not bind at all;
   the authors place it "in the N terminal part of the SDR domain".
3. The mapping is nonetheless **fragment-level and suggestive**, not a contact map: no purified
   protein, no affinity constant, no stoichiometry, no structure, and no catalytic-site mutant.

## 2 · What it does NOT add — stated so nobody over-reads it

- **No enzymology whatsoever.** No substrate, no cofactor, no oxidoreductase assay, no NAD(P)H, no
  catalytically dead control. The SDR appears only as a fragment boundary.
- **No affinity.** Every readout is a pull-down or a two-hybrid; the paper's own basis for calling the
  interaction direct is the two-hybrid format plus a personal communication.
- **No allele.** Wild-type WWOX, WWOXv2, Y33R and two fragments only — **no P47T, no Q230P, no G372R,
  no A141T, no P252A**, no neurological system, no patient material.
- The HR direction is contested **in the source's own words**, between this group plus Schrock on one
  side and Aqeilan on the other, with cell type offered as the explanation.

## 3 · Proposed op (append-only; the discovery ledger is append-only on leads)

- **file** `disease-models/wwox/research/discovery_ledger_current.md`
- **record** new lead `DL-MECH-NNN` in the section `MECH — indizi meccanicistici (aghi nel pagliaio)`
  (the integrator assigns the next free `DL-MECH` number)
- **op** append
- **new** (content, not formatting):
  > **DL-MECH-NNN — The SDR region of WWOX carries a measured protein-binding determinant, independent of WW1 and of the originating laboratories.** Status: open · Tag: **DATO** for the binding and the fragment mapping, **INFERENZA** for any functional reading of it · What is measured: a WWOX–MERIT40 interaction, in yeast two-hybrid, in HEK293 co-IP of tagged constructs and in an endogenous MCF7 co-IP · Matrix: yeast, HEK293 overexpression, MCF7 crude extract · Domain: binding lost with a WW1-WW2 fragment, retained with a WW2-SDR fragment, unaffected by the WW1 ligand mutant Y33R · Source: PMID 37248434 (Institut Curie / INSERM, receipt `FTR-20261004-37248434-01`) · **Transfer limit:** this is protein–protein binding and says nothing about catalysis, substrate or cofactor; no affinity constant exists; no WWOX disease allele is studied, and nothing here transfers between P47T, Q230P, G372R, A141T and P252A · What would falsify it: a purified-protein binding experiment (ITC or NMR) showing no WWOX-SDR/MERIT40 interaction, or a demonstration that the co-IP signal is bridged by a third protein · Why it matters: the corpus's SDR reading has rested on one laboratory's crude-extract enzymology; this is an independent measurement **on the same region** that is nevertheless **not** enzymology, so it raises the SDR's standing as a *binding* surface without adding anything to its standing as a *catalytic* one.

## 4 · What must NOT be written from this source

- Not "an independent laboratory has confirmed WWOX enzymatic activity". It has not; the paper
  contains no enzymatic measurement.
- Not a numeric affinity for anything.
- No individual-level description of the 499-tumour cohort (public edition).

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

The two-hybrid bait was not full-length WWOX but an isoform with the two WW domains and only a truncated SDR. | containing only the WW1 and WW2 domains, and a truncated SDR domain | Results, WWOX interacts with MERIT40, first paragraph — files/fulltext/PMID37248434_Taouis2023_PMC.xml

Directness is asserted from the assay format and a personal communication, not from a biochemical experiment with purified protein. | it is very likely that it is a direct interaction | Results, WWOX interacts with MERIT40, first paragraph — files/fulltext/PMID37248434_Taouis2023_PMC.xml

The binding determinant lies outside the WW pair: a WW1-WW2 fragment does not bind, a WW2-SDR fragment does. | the N-terminal region of WWOX containing only the WW1 and WW2 domains did not interact with MERIT40, whereas the region composed of the WW2 and SDR domains did | Results, WWOX interacts with MERIT40, third paragraph — files/fulltext/PMID37248434_Taouis2023_PMC.xml

The authors place the determinant in the N-terminal part of the SDR domain and state it as a suggestion. | the domain of WWOX interacting with MERIT40 is located in the N terminal part of the SDR domain | Results, WWOX interacts with MERIT40, closing sentence — files/fulltext/PMID37248434_Taouis2023_PMC.xml

The only WWOX point mutant used is a WW1 ligand-binding mutant, not a catalytic one. | a mutant form of WWOX harboring a Y33R point mutation in the WW1 domain inhibiting its ability to interact with the PPXY motifs of different proteins | Results, WWOX interacts with MERIT40, third paragraph — files/fulltext/PMID37248434_Taouis2023_PMC.xml

Abolishing WW1 ligand binding does not disturb this interaction. | this mutation did not affect the WWOX-MERIT40 association | Results, WWOX interacts with MERIT40, third paragraph — files/fulltext/PMID37248434_Taouis2023_PMC.xml

The endogenous interaction was detected by immunoprecipitation from a crude cell extract with the group's own antibody. | of total proteins were subjected to direct immunoprecipitation with the anti-WWOX antibody produced by Eurogentec | Materials and methods, Co-immnunoprecipitation and western blot — files/fulltext/PMID37248434_Taouis2023_PMC.xml

The direction of WWOX's effect on homologous recombination is unsettled in the source's own words. | The effect of WWOX on HR seems therefore to depend on the cell type. | Discussion, second paragraph — files/fulltext/PMID37248434_Taouis2023_PMC.xml

A mechanistic step of the paper's own model rests on unpublished data. | We found that WWOX promotes the formation of BRCA1-A (unpublished data). | Discussion, third paragraph — files/fulltext/PMID37248434_Taouis2023_PMC.xml

The authors close by calling their interpretation a hypothesis still to be validated. | Further analysis have to be perform to validate these hypotheses. | Discussion, final sentence — files/fulltext/PMID37248434_Taouis2023_PMC.xml

The imaging experiment behind the foci conclusion was done once on 50 cells per condition. | 50 cells were counted in each condition, the experiment was done once | Figure 3 legend, panel B — files/fulltext/PMID37248434_Taouis2023_PMC.xml

---

## BATCH DISPOSITION — `BATCH_20261004_005` (2026-10-04, ACTOR_ID `scientist`, Scientist O), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED

Class re-judged **MINOR** (a research-layer lead; no claim created or narrowed). Landed as **`DL-MECH-115`** in `discovery_ledger_current.md`, with the source's registry landing as **`PAPER 245`** (the promotion of `CORPUS-STUB-041`; the candidate's provisional `PAPER 235` was taken, and the number was re-measured with `registry_records.py catalog` at `2d2077f47e83`). **Blind locator audit before propagation: 11 triples, 11 QUOTE_FOUND, 11 SUPPORTED, 0 UNVERIFIABLE**, by an auditor that had seen no candidate. Two amendments folded in at source: the fragment mapping is recorded as **co-immunoprecipitation in cells, not purified protein** (Fig. 1D-E), and the hypotheses the paper's closing sentence leaves to be validated are about **aneuploidy**, not about the binding. The auditor also measured, independently, that the paper contains **zero** enzymatic or oxidoreductase measurements of WWOX and **zero** affinity, stoichiometry or purified-protein experiments — which is what makes the lead's own transfer limit a measurement rather than a caution.

🔵 **One classifier interruption, reported as it happened:** this audit's first run was cut off mid-hand-back by a safety classifier after two verdicts. It was **re-dispatched unchanged on a different model**, as the runtime error message itself advises; nothing was reworded and no verdict was reconstructed from the truncated report.

**Not medical advice.**
