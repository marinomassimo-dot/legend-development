# P4CD-03 infigratinib (Q5 expression, FGFR3 -P-> MAP3K7 -P-> NFKBIB -T-> IL1B, mimics): INCONCLUSIVE (insufficient support; low priority)

Scientist-a4, 2026-10-30. Not medical advice. A 'mimics' proposal predicts that FGFR inhibition would push IL1B in the direction of the Wwox-deficient datum (up); it is a test of a possible harm, not a rescue lever. Valence unresolved.

**Proposal as generated.** Seed IL1B transcript up (S084, P47T knock-in cerebellum, n 6 per group, distributions overlap wild type; also TNF). Chain FGFR3 -P(+)-> MAP3K7 [SIGNOR] -P(-)-> NFKBIB [SIGNOR] -T(+)-> IL1B [CollecTRI]; net action of an FGFR3 inhibitor on IL1B +1 (mimics); z 7.1 (smallest of the three nulls, cluster of 28 FGFR3 families).

## 1 Identity
Infigratinib CHEMBL1852688 (free base), InChIKey QADPYRIHXKWUSV-UHFFFAOYSA-N; PubChem agrees by name (infigratinib, BGJ398) and by key. The catalogue family also contains the phosphate salt CHEMBL1834657. VERIFIED by structure.

## 2 Target, action, measures
Curated mechanism: FGFR inhibitor. Human (binding/biochemical, nM, not pooled across assay formats): FGFR1 IC50 20 rows 0.59 to 2,570 (14 documents); FGFR2 0.46 to 4,680; FGFR3 26 '=' rows 0.66 to 3,036 (10 documents) and one A-class value of 1.8; FGFR4 0.82 to 88,320; KDR 180 to 1,449; LCK about 2,500; ABL1 2,300. Broad FGFR1-3 family inhibitor; FGFR3 is not specific.

## 3 Exposure and nervous system
openFDA label: no record (HTTP 404 'no matches': absent datum, not a negative). Paediatric: phase 3 in children 3 to 17 years with achondroplasia, 0.25 mg/kg daily for 52 weeks (NEJM abstract, 42370681; efficacy on height velocity; adverse-event data not extracted), phase 2 in children aged 3 to 11 and in children under 3 (recruiting), extension studies, hypochondroplasia studies. Adults: a phase 2 in recurrent glioblastoma (NCT01975701); a withdrawn paediatric CNS-tumour study (NCT05222165). No CSF or brain concentration retrieved. (The 'neurodevelopment' slice returned 5 achondroplasia trials because I added that term to the slice; they are skeletal, not neurodevelopmental trials.)

## 4 Safety and counter-evidence
Label not retrieved; class effects (hyperphosphatemia, ocular and nail toxicity) are general knowledge, UNVERIFIED. Seizure: Europe PMC 'infigratinib x seizure/epilepsy' 0 hits. Counter-evidence to the proposal's direction: the pan-FGFR inhibitor rogaratinib REDUCED microglial reactivity and synaptic loss after mouse traumatic brain injury (39635532, abstract; PMC copy not read), the opposite of the 'mimics' prediction of raised IL1B.

## 5 Edge provenance (see edge_provenance_judged.tsv)
FGFR3 -> TAK1 (24466111, PMC download, abstract, Introduction and start of Methods read): protein interaction and phosphorylation, in myeloma and bladder cancer lines, HeLa/HEK293 and a yeast two-hybrid library; no neural cell. MAP3K7 -> NFKBIB (9480845): abstract shows TAK1 stimulates NF-kB activation; the network's 'inhibits IkBb' reading is an interpretation (UNVERIFIED). NFKBIB -> IL1B (7 references): IkBb is a co-activator at the IL-1b promoter in mouse macrophages, with IkBb-null mice protected from LPS (20975042), also in RAW264.7 and BMDM (28753596); (a) YES, (b) macrophage (an immune context, not microglia or astrocyte), (c) sign matches, (d) no FGFR or TAK1 manipulation. The P edges are cancer-line records.

## 6 Expression (adult HPA, nCPM)
FGFR3: astrocyte 516, Bergmann glia 252, endothelium 18, OPC 58; CNS macrophage 5.7; microglia (single-cell) 5.6; neurons 0.4 to 1.1. IL1B: CNS macrophage 27, microglia 19, astrocyte 0.1. NFKBIB 4 to 17 everywhere; MAP3K7 72 to 197. Organoid: FGFR3 312 to 407 vs 217/284 CPM (1.45 x), IL1B about 0. Reading: the target is an astrocyte gene, the seed an immune-compartment gene; the chain joins two cell types that share neither node in the atlas.

## 7 Trials registry
Done (above): neuro slices 0 for epilepsy, hypomyelination, neuroinflammation, WWOX; paediatric achondroplasia studies listed.

## 8 Feasibility and limits
An astrocyte-intrinsic test is possible: WWOX-deficient astrocytes (or organoid-derived astrocytes) with and without FGFR-pathway stimulation (FGF2) and infigratinib; readouts TAK1 phosphorylation, IkBb level, IL1B mRNA, and IL1B-independent damage markers. The prior that it will show anything is low (counter-evidence above; astrocytes do not express IL1B in the atlas). Limits: FGFR3 inhibition at the doses used for skeletal indications is systemic; CNS exposure unknown.

## Decision and scores
**INCONCLUSIVE** (insufficient support, not 'no activity'). Missing datum: FGFR3-dependent TAK1/IkBb regulation and IL1B induction in a glial cell, and any FGFR inhibitor effect on IL1B in a WWOX-deficient glial system. Pre-registered rule N2 caps promise (terminal edge valid in macrophages; P edges only in cancer lines). Promise LOW; depth MEDIUM (chain edges located and partly read); feasibility MEDIUM-HIGH (oral, paediatric exposure data exist); priority LOW.
