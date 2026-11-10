# IT40 P10 — what to investigate next, by decision that can change

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Order = (1) the decision the result can change, (2) importance for the questions the dashboard carries (INV-05, INV-18), (3) cost *as documented* in the package `cost_note` cells (qualitative; no figure is invented). It is an order of investigations, not a ranking of treatments, and not an in-vivo experiment per hypothesis. Source rows: `membrane_hypotheses_20261108/output/experiments.tsv`, `ampa_nmda_discrim_20261108/output/experiments.tsv`, the open-question map rows `IT40-Q01..03`, `RS-NP3B2`, and `mechsearch_it40_20261109/identity_check.tsv`.

## A. Can be settled with public data or in-silico work (zero spend, no new measurement)

| # | Question | Decision it can change | Why it is well posed | State |
|---|---|---|---|---|
| A1 | Primary mechanism papers for the AMPA/kainate tools NBQX and GYKI 52466 and the GluN2B tools ifenprodil and Ro 25-6981 | Whether an AMPA or GluN2B arm may name a tool as more than "use-only, mechanism not read" (cards F04, INV-05) | A reading task; the tools exist in the literature (110 PubMed records for one title string in the package) | Open need named by the packages; **no reading started in IT40** |
| A2 | Catalogue identity of four tools: GYKI 52466 resolves by name to a record called GYKI 53784; Ro 25-6981 resolves to a record named by a ChEMBL id with a different target (DRD1); ifenprodil's records carry no GluN2B mechanism row; Brilliant Blue FCF is absent (Brilliant Blue G is a different dye) | Prevents a wrong molecule entering any comparator or probe row | Resolve each name in the public registries and record the identity source, as was done for ISRIB | `identity_check.tsv` states the symptom; the resolution is **open** |
| A3 | HIF1A→BNIP3 premise (three proposals without an investigation) | Whether the chain deserves its own premise-measuring investigation | A literature question; must not be recycled from the HK2 row | Queued in P11 |
| A4 | Single-cell contrast of the knockout, SCAR12-class and WOREE-class libraries (DL-MECH-181) | Whether the composition-sensitive human-neural signatures of ten needs replicate within matched cell populations | Only after the deposit is released; the access request stays an unsent draft with the operator | **Blocked on access**, not on analysis |
| A5 | Wang 2016 full text and the Methods of the neuronal Kv7-opener recording papers | Whether a Kv7 or leak arm has a primary source in neurons | Reading tasks; bot-checked pages not retried | Open need |

## B. Needs a new measurement (the answer is not in other literature)

Ordered by decision changed first, then cost as documented.

| # | Measurement | Decision it changes | Documented cost | Depends on |
|---|---|---|---|---|
| B1 | **BE0**: measured bath magnesium, potassium, temperature, blockers actually present, a time-matched vehicle arm, a within-slice paired design | Makes every later arm interpretable; the source states only the incubation medium | Low; no drug | none |
| B2 | **E1** (membrane): sag, rebound and input resistance at matched potential and matched deflection, with capacitance, access resistance and bridge balance by genotype, with and without synaptic blockade | Decides whether *any* pharmacological arm for sag is needed (MH1/MH2/MH3) | Existing equipment; animals, not cells, are the replicate; no drug | B1 conditions |
| B3 | **BE1 / IT40-Q01**: does the burst survive a verified AMPA/kainate block? | Whether an AMPA arm exists at all and how the NMDA-receptor result is read | Moderate (block onset in tissue unmeasured) | B1 |
| B4 | **BE4**: the design rule (pre-specified block threshold; two metrics; receptor-agnostic release-reducing control) | Without it matched-effect comparisons depend on the metric | Low; a design rule | none |
| B5 | **BE2**: isolated NMDA-receptor current, matched-current curves, sensitive fraction of a GluN2B-selective modulator | Total-receptor reduction versus GluN2B-weighted comparison (BH2) | High | B1, B4, tool identity A1–A2 |
| B6 | **BE3 / IT40-Q02**: gap-junction tool with EPSCs, spike width, input resistance, coupling; matched-effect control; pannexin-1 blocker with engagement | Whether the burst fall can ever be attributed to coupling | Moderate to high | B1, B4 |
| B7 | **E3, E4** (membrane): Ba2+- or XE991-sensitive difference current; two-chemotype Ih tool arm on bursts | Moves HCN from "contributes" to "differs" only if B2 shows a matched-condition excess | Junction offset must be measured; space-clamp limit | B2 |
| B8 | **BE5 / IT40-Q03**: GABA-A arm with evoked IPSC | Separates reduced inhibition from receptor gain | Moderate | B1 |
| B9 | **E5**: age series and layer V | Maturation versus cell-autonomous difference | Breeding cost; the knockout dies at weeks 3–4 | B2 |

## C. Not yet well posed (do not run; sharpen first)

* **Gap-junction attribution of the carbenoxolone burst fall (BH3).** The audit leaves no datum for it; the question becomes posable only after B6's matched-effect control.
* **Voltage-clamp Ih density in P13–P17 layer II/III cells (E2).** Space clamp under-clamps dendritic Ih at this age; the question needs a design that is not a whole-cell voltage clamp of the soma.
* **Kainate-receptor contribution (AB14).** No tool separates it, and the tools' mechanism papers are unread (A1).
* **"Which of H1–H7 is true".** The matrix gives no single arm that separates them; the order above is a sequence of partial separations, not a test.

## What this changes in practice

The next package should be small: A1+A2 (readings and identities that block B3/B5 tool choices), run by the science session or a delegate with the originals; B1/B2/B4 are design statements the laboratory can adopt before any compound is discussed. A new broad batch is not proposed before A1+A2 are consumed.
