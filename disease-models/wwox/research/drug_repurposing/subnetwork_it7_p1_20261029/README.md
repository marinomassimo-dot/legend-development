# IT7 P1 (roadmap R1): a typed, signed glycolysis / PDH / lactate subnetwork for the first predictive comparison

Scientist-a, 2026-10-29. Exploratory. A curated, partly signed table of observations, not a validated causal model and not a patient molecular twin.
Transcript level except where a row says otherwise. Association is not modulation is not rescue. Not medical advice.
Nothing here edits a scientific current file, the receipt ledger, a card or a need.

## 1. The question (fixed here, before any evaluation contrast was opened)

**Is the HIF-type glycolysis / lactate transcript module that is raised in the two human WWOX-loss neural systems (knockout organoid; shRNA
progenitors, plus neurons from the same line) a reproducible WWOX-loss feature that also appears in an independent WWOX-loss contrast, and
does the PDK1 -> PDH link that the chain needs have any support at all?**

The signed subnetwork that carries the question is in `nodes.tsv` / `edges.tsv`. Its "signature candidates" are chosen by a fixed, mechanical rule
(`human_concordance` in `nodes.tsv`, recomputed by `subnetwork.py check`): a gene is concordant when its centred log2 ratio is at least 0.25
in the same direction in BOTH the organoid and the progenitor library. That rule yields five genes up (SLC2A1, HK2, LDHA, LDHB, BNIP3) and one down
(PDK1). The 0.25 bin is a descriptive reading aid, not a test; PDK1 is lower in sign only (inside its single-gene null in both systems) and is kept
because the chain predicts the opposite, not because it is evidenced.

### Why this question and not the others considered
| Candidate | Decision | Reason |
|---|---|---|
| ISR target set | not chosen | the sign is unresolved (organoid lower, progenitor line higher, mouse inside the null at about 0.3); a signature built on it would inherit a sign nobody can state |
| Myelin / oligodendrocyte set | kept only as a positive-control module | lower in all four mouse deletion contrasts (-0.8 to -1.8), but mouse only; the human systems cannot test it (hNPC and neuron libraries have the genes at 25 to 32 tags; the week-15 organoid shows MBP +0.63, PLP1 +0.86, an unplanned look recorded in `observations.tsv`); composition-confounded; oligodendrocyte genes are not expressed in the usual cell lines that perturbation data come from, so no signature-reversal question about them is evaluable |
| Excitability / NMDAR | not chosen | the data are electrophysiology and pharmacology, not a transcript contrast, and the module records three unseparated readings |
| Glycolysis / PDH / lactate | **chosen** | (a) a signed transcript observation exists in two independent human neural systems; (b) the same module was looked at in the mouse (seen, not concordant for LDHA/LDHB), so the prior is genuinely uncertain and a pre-registered test can come out either way; (c) the genes are expressed in the cell-line perturbation resources the later method needs (which of them are in a measured gene panel is UNVERIFIED here); (d) a rival explanation (a less mature tissue) is already stated, so a failure has a reading; (e) cards E02, E03, E04 and I01 already exist, so the result lands somewhere |

## 2. Data audit (what exists, per unit of replication; `systems.tsv` holds the same facts machine-readably)

| System | Role | Unit and n | Platform | Notes |
|---|---|---|---|---|
| GSE156243 organoid knockout, week 15 | build | 4 v 2 libraries (batch/differentiation not stated) | RNA-seq counts | the exon deletion leaves the WWOX transcript (+0.42), so the transcript is not a depth check |
| GSE126075 shWWOX progenitors | build | 1 library per arm | CAGE | knockdown depth not shown in the progenitor tags; control arm may be untransduced; not a replicate |
| GSE126075 day-14 neurons | build (support only) | 1 library per arm | CAGE | WWOX about 3 to 4 fold lower; composition-sensitive |
| GSE158681/2 mouse P17 (4 contrasts) | **seen**: already analysed in IT6 P4, so not held-out | 2 to 3 animals per arm | transcript TPM | used as a comparison column, never as evaluation |
| MEF null, human fibroblast knockout, fly head, one patient MRS | context | not extracted / 5 pools / 1 | protein, activity, metabolite | different species or non-neural; they carry the only protein, activity and metabolite observations and are kept as separate columns |
| **GSE215425 P47T knock-in** (PMID 36828035) | evaluation candidate 1 | 5 v 5 animals; cerebellum 4 v 3; the SAME animals supply all four regions, so regions are not independent | RNA-seq integer counts, processed table | public; read at the source: 37 samples, sex not balanced (wild type 3 male 2 female, mutant 2 male 3 female by sample names); age not extracted (UNVERIFIED); a partial-loss missense in the WW1 domain, not a null. Only the file header and two unrelated rows were inspected; **no network gene was looked at** |
| E-MTAB-14948/14949 fly factorial | candidate 2 | 4 pooled-head libraries per cell | featureCounts | perturbation depth is not visible in the deposit; ortholog mapping is not one-to-one; amyloid context |
| GSE158684 snRNA, hippocampal nuclei | candidate 3 | 1 library per arm (nuclei are not replicates) | snRNA-seq | same series family as the seen mouse contrasts, so not independent of them |
| E-MTAB-14792 human organoid scRNA | candidate 4 | not accessible (403) | scRNA-seq | no request was sent; operator decision |

Reuse terms: every deposit is public on GEO or ArrayExpress with no licence text in the record. Redistribution terms are therefore UNVERIFIED;
only derived summary numbers are committed here, never a raw table. Free access is not a redistribution licence.

## 3. What the later evaluation (P3) can and cannot be

* **Can be, with limits (exploratory):** a pre-registered transfer test. Fix the six signature genes and their directions from the table
  (organoid + progenitor library only), then ask whether the same directions, and the module mean against its decile-matched null, appear in
  GSE215425 (animal as the unit, one contrast per region, regions not pooled, sex as a covariate or stratum) and, as a weaker second check, in the fly
  factorial. A negative result narrows "WWOX-loss feature" to "human neural systems of this design"; a positive one is one partial-loss mouse genotype agreeing
  with two human systems, not a rescue or a mechanism. Mouse P17 already argues against LDHA/LDHB, so a flat P47T result is the expected null, not a surprise.
* **Cannot be:** a test of any compound's effect on WWOX loss. No public record has a compound response in a WWOX-deficient system with a molecular
  readout (IT6 P3 census), so a held-out compound truth does not exist. Any compound-level comparison is limited to mechanism recovery in
  perturbation resources (does a method rank agents acting on module nodes above random), which is recovery of known examples, not accuracy.
* **The six-gene signature is small.** Whether a reference signature-reversal method has enough genes in its gene panel to be informative is UNVERIFIED and
  is a P3 pre-registration item; if not, the honest outcome is "inconclusive: signature too small", not a lowered bar.
* **The missing comparison:** a human neural WWOX-deficient system with biological replication and a matched protein, activity or flux readout
  (PDH phosphorylation or activity, lactate, ECAR). Until it exists, the PDK -> PDH -> lactate links stay `inferred` or `hypothesised` and every
  evaluation of them is exploratory.
* Never pool: replicates are not combined across studies; regions of one animal are not independent; one library is not a replicate.

## 4. Firewall (what is excluded from the network so it cannot become held-out truth)

Excluded entirely: every perturbation-reversal output and list from earlier iterations (signature-query results, ranked reverser lists, frequent-hitter
tables, local level-5 summaries); every named agent and every agent-to-target edge (the catalogue and cards own those; P3 joins them afterwards);
the card ratings and priority labels; the fly double-knockdown behavioural result (an intervention response, kept in the need, not here); and every
observation from the evaluation candidates (`systems.tsv` marks them `heldout_candidate`; `subnetwork.py check` fails if an observation row names one).
`check` also fails if agent or reversal vocabulary appears in any table. Target identities (ChEMBL target ids) are kept: they say what a protein is, not what
anything did to a WWOX-deficient system.

## 5. Files

`nodes.tsv` (30 nodes: 23 genes, 1 perturbation (WWOX), 3 sets, 3 process/metabolite; identity ids, per-system sign columns, concordance) · `edges.tsv` (88 edges: 78 measured, 5 inferred, 2 hypothesised, 3 association) · `observations.tsv` (231 rows, one per node and system, UNKNOWN kept) · `systems.tsv` (15 systems with genotype, tissue, stage, n, unit,
platform, accession, PMID, reuse terms, time) · `evidence.tsv` (18 verifiable anchors: manifest entry, document phrase, or abstract) ·
`derived_gene_values.tsv` + `derive_gene_values.py` (per-gene centred values for the three human libraries, recomputed from the deposits with the iteration-5 method;
inputs are outside the repository, their SHA-256 is printed) · `gene_list.txt` · `subnetwork.py` (`--help`, `build`, `check`).

Edge sign means: the direction of the target when the source is in `source_state` (WWOX "loss" for measured edges). `no_change` is an observation; `UNKNOWN` is absence of one.
Measured edges are one per system; counter-evidence ids point at the same node in other systems with a different sign (conflicts are kept, never averaged).

Reproduce: `python3 subnetwork.py build && python3 subnetwork.py check --hgnc <hgnc_complete_set.json>` (the HGNC file is optional; without it identities are format-checked only).

## 6. UNVERIFIED and open

* Cre drivers, control genotype, sex and batch of GSE158681/2; the link of those deposits to a paper; mouse ages of GSE215425.
* Whether the 0.25 bin and the six-gene rule survive resampling: not tested here; P3 must declare its own decision rule before opening the evaluation.
* Ortholog one-to-one for PDK, SLC16, SLC2, HK, LDH genes (fly Ldh is shared by LDHA and LDHB in the table; mouse mapping by symbol).
* HIF1A -> PDK1 -> PDH links rest on an abstract-level reading of a non-WWOX paper and on a WWOX paper's MEF/cancer-cell results; full text of the former was not read here.
* Which module genes a perturbation resource measures directly.
* Mouse per-gene values for PFKP, ALDOA, PGK1, ENO1, PKM and BNIP3 are UNKNOWN because the P4 key-gene table does not hold them (set-level values do).
* Human fibroblast line: the figure arm is called knockout in the data and knockdown in the paper's wording; n of the PDH panel is not stated.
* PubMed attribution: abstracts of PMID 25012504 and 16517406 were retrieved via PubMed on 2026-10-29.
* HGNC / Ensembl / ChEMBL ids were fetched from the local HGNC complete set (2026-10-22) and the public Ensembl and ChEMBL REST services on 2026-10-29; three Ensembl lookups were completed from the iteration-6 resolution table.
