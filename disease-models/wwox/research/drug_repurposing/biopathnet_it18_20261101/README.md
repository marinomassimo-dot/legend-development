# IT18 P-BIOPATHNET — does a path-based method add relevant relations or verifiable explanations?

Actor `scientist`, 2026-11-01. Non-canonical research material; **not medical advice**; computational link prediction only. Public edition, WWOX-DEE genotype class. Nothing here is WWOX efficacy evidence.

Prior context: PROTON was discarded for the current question (undirected graph, saturated scores, 0 of 61 added relations with activity records, WOREE not specific: `../proton_it18_20261101/README.md`); the P4 contextual path showed that reference coverage, not the direction field, is the bottleneck (`../matching_it18_p4_20261101/README.md`).

## Stage 1 — before any trial (2026-11-01)

**Revision.** Code `emyyue/BioPathNet` at `b051a9003a1363b5655cdb7dfdad60609c0e4fe3` (2026-02-19, last push the same day); tag `v0.1`, Zenodo `10.5281/zenodo.16944506` (code zip only). Full table: [`availability_terms.tsv`](availability_terms.tsv).

**Inputs, node mapping, relation types.** BioPathNet reads tab-separated triplets: `train1.txt` = background regulatory graph (BRG, message passing only), `train2.txt` = supervision graph G1, `valid.txt`, `test.txt`, plus `entity_types.txt` (entity -> type id, used for node-type-aware negatives and for ranking only same-type tails) and `entity_names.txt`. Nodes are plain strings (HGNC symbols, `CHEBI:` ids, `hsa` KEGG ids); there is no identifier-mapping layer — mapping is the user's job. Reverse relations are added internally. The released gene-function data has 13 BRG relation types from Pathway Commons 12 SIF (counts: chemical-affects 618,094; interacts-with 517,390; controls-state-change-of 191,548; in-complex-with 191,275; catalysis-precedes 147,948; controls-expression-of 125,860; consumption-controlled-by 22,659; controls-production-of 21,262; controls-phosphorylation-of 17,660; used-to-produce 14,747; controls-transport-of 7,899; reacts-with 4,063; controls-transport-of-chemical 3,741) and one supervised relation `KEGGPathway` (gene -> pathway, 321 pathways). `controls-*`, `catalysis-precedes`, `used-to-produce`, `consumption-controlled-by` and `chemical-affects` are stored as ordered pairs (directed); none carries a sign (activation / inhibition).

**WWOX in the released graph.** 640 BRG rows (interacts-with 569, chemical-affects 53, controls-expression-of 6, controls-state-change-of 5, controls-transport-of 3, controls-phosphorylation-of 2, in-complex-with 2); directed examples as stored: `SRC controls-phosphorylation-of WWOX`, `TNK2 controls-phosphorylation-of WWOX`, `WWOX controls-transport-of TP73`, `WWOX controls-state-change-of YAP1`. **No KEGG annotation of WWOX** in train, valid or test.

**Checkpoints actually retrievable.** One: the gene-function model `model_epoch_12.pth` (110,765,951 bytes) stored by Git LFS in the repository; downloaded by public GET and its sha256 equals the LFS oid. Its log: PC_KEGG_0602, 31,410 entities, 14 relations, 15 epochs on one GPU (about 8 h), test MRR 0.5579. **No drug-repurposing (PrimeKG) checkpoint exists** in the tree, the release, Zenodo or the paper; the paper's code availability names only the GitHub code. The PrimeKG data would have to be rebuilt with the TxGNN split code and trained.

**CPU feasibility and dependencies — what was verified and what was not.** The README says `--gpus null` runs on CPU, and the C++ extension loader has a CPU branch (`generalized_spmm.cpp` compiled without CUDA). Dependencies: torch, torch-scatter, torchdrug (README pins torch 2.0.1 and Python 3.10; this host has Python 3.12, gcc/g++, 4 cores, 15 GB RAM, 82 GB free disk). **Not yet verified**: that torchdrug installs and compiles on this Python/torch, that the checkpoint loads, and the time and memory per query on the 1.9-million-row graph — these are step 0 of the trial, with a stop rule. Training on PrimeKG on CPU is **not** proportionate (the authors trained on GPU; NBFNet on that graph was over 48 h per epoch on GPUs) and is not attempted.

**Licences and terms.** Code MIT. The checkpoint ships in the MIT repository with no separate model terms. The data have **no licence of their own** and derive from Pathway Commons 12, which aggregates sources with restrictions (HumanCyc under SRI licence, PhosphoSitePlus CC BY-NC-SA, DrugBank CC BY-NC/academic, KEGG, CTD, NetPath); the supervision labels are KEGG memberships via ConsensusPathDB. Not cleared for redistribution: nothing raw is committed. Paper CC BY 4.0.

Data digests (sha256, equal to the LFS oids): entity_names.txt c1113fe726f25d8ebe1cbb017461f1b2b3645d8ecb23b305e31ebcd721d9bd34; entity_types.txt 02a3fc629b0c3bc540d4544fe09d9cb5a3818d845229d495c79416ab5c5dfdba; test.txt d002b54d454ee0344c53ec712079e7b93bc612f31409fa68b659ff47d6c11f48; train1.txt 7eada252e712da7788f02a546e66dfa9ce3fb6f60be29af493de5b561f0d02e3; train2.txt f6d20ef0e055091bf16e02451b3423bb9f6c6a51a6c1413d6b2bf3174548153f; valid.txt 41e111bc36fe68fa14b6d39a51b63b9cb17ab9998e607921a892ae01bf115259.

**Small relevant example.** The repository's `data/mock` is a toy (12 pathways, a few genes) for checking that the pipeline runs; it is not relevant. The relevant small example is a single WWOX query on the released gene-function model. Leakage risk recorded in advance: Pathway Commons 12 contains KEGG 07/2011 interactions, so some BRG steps may encode the same knowledge as the KEGG labels.

**Stage 1 verdict.** Passes proportionately for **one** small trial of the distinct capability (typed, partly directed explanation paths) on the released model; fails for the drug question (no model, training disproportionate). Design: [`PRE_REGISTRATION.md`](PRE_REGISTRATION.md).

## Stage 2 — one small trial, stopped at the pre-registered memory limit (2026-11-01)

Design committed first (`751d80eb`). Outputs: [`results.json`](results.json) (ranks, names, coarse classes), [`wwox_step_provenance.tsv`](wwox_step_provenance.tsv), [`decisions.tsv`](decisions.tsv).

**Step 0, feasibility — what was verified.**
- Attempt 1 (torch 2.4.0 CPU): torchdrug 0.2.1's C++ extension does not compile (`ATen/SparseTensorUtils.h` not found).
- Attempt 2 (torch 2.0.1 CPU, the README pin, Python 3.10): it compiles, the checkpoint loads, and **prediction runs**: 11 queries in 318 s (about 29 s per query on 2 threads, 1.5 GB RSS).
- **Explanation does not fit.** The repository's `visualize` method (gradient edge importance plus beam search) needs gradients through the whole 1.9-million-row graph. On the first query it was **killed by the kernel (signal 9) after 82 s at 11.27 GB RSS**, on a 15 GB host shared with another job. That is above the pre-registered 8 GB limit, so it was not retried.
- The 100-triplet sanity sample was not run, because the stop rule was reached before it. The loaded weights are therefore not checked against the logged MRR. One sign that they are not random: the control genes' top pathways are plausible and distinct from each other, for example NME5 -> purine and pyrimidine metabolism, SMARCA5 -> basal transcription. That is an observation, not a test.

**(a) Predictions for `(WWOX, KEGGPathway, ?)`, descriptive.**
- BioPathNet top-10: HSV-1 infection, **Hippo signaling (rank 2)**, endocytosis, MODY, tight junction, ER protein processing, mRNA surveillance, ubiquitin-mediated proteolysis, RNA transport, spliceosome.
- Neighbour vote B top-10 is led by large neurodegeneration and RNA pathways: spliceosome, prion, multi-neurodegeneration, ALS, ... Hippo is at rank 13 in B.
- Need-relevant pathways in the top-10: BioPathNet 7, B 9. The base rate is 186 of 321 pathways (58 percent), because the needs name 97 target symbols. The difference is under 3, so no statement is made.
- Overlap between the two top-10 lists: 4 pathways.
- Hippo is a pathway the module already holds through the WWOX-YAP/TAZ literature, so it is a recovery of known biology, not an added relation.
- The relations BioPathNet adds that are not need-relevant (MODY, tight junction, mRNA surveillance) carry no explanation, because step (c) could not run.

**(b) Specificity: passes.**
- Median Jaccard between WWOX's top-10 and the top-10 of each of the 10 degree-matched controls is **0.05**; no pathway reaches the top-10 of 8 of the 11 genes.
- The controls are unannotated genes with BRG degree within 0.8-1.25 times WWOX's. Excluding annotated genes was a clarification made before any prediction was computed.
- This is unlike PROTON, whose added links were hubs.

**(c) Explanations: not obtained** (OOM above). The decisive capability, a model path whose steps can be checked, was therefore not shown on this host.

**What was checked against sources: the graph's own WWOX steps, not model explanations.** The released BRG stores 16 directed WWOX rows (plus 2 undirected in-complex-with rows). In the Pathway Commons 12 extended SIF, each row carries a data source and usually PubMed ids, so step-level provenance does exist. Three steps were checked at **abstract level only** (an abstract is not a read):

| Step | Cited source | Result at abstract level |
|---|---|---|
| `WWOX controls-transport-of TP73` | PMID 15070730, [doi](https://doi.org/10.1073/pnas.0400805101) | consistent: Wwox redistributes nuclear p73 to the cytoplasm |
| `TNK2 controls-phosphorylation-of WWOX` | PMID 16288044, [doi](https://doi.org/10.1158/0008-5472.CAN-05-1127) | consistent: Ack1 phosphorylates Wwox Tyr287, which leads to degradation; the edge carries **no sign**, so the degradation is lost |
| `WWOX controls-transport-of YAP1` | first cited PMID 12807903, [doi](https://doi.org/10.1074/jbc.M305597200) | **does not name WWOX** (YAP-ErbB4 paper); the second PMID was not checked |

Other issues in the same rows:
- 4 of the 6 `controls-expression-of WWOX` rows come from MSigDB C3 motif sets. These are predictions, stored under the same relation type as curated regulation.
- Pathway Commons 12 contains KEGG 2011 interactions, so some BRG steps may carry the same knowledge as the KEGG labels. This label-leakage risk was not measured.

So the steps can be checked, but they are unsigned, of mixed evidential kind, and at least one is mis-cited. A path built from them would inherit all of this.

**Against LEGEND's current path and PROTON.**
- BioPathNet's graph is typed and partly directed, where NeuroKG is undirected. That is the capability gap the brief named, and it is real at the input level.
- No relation is signed, and the only released model predicts gene-pathway membership, not drug-target or drug-disease relations. **For the current question (compounds for the WWOX needs), it adds nothing runnable.**
- The P4 contextual path still supplies the direction that no graph here encodes.

## Reading

Targeted reading of the paper (Europe PMC JATS XML, CC BY 4.0) under the standing method. Receipt: [`receipt_FTR-20261102-41559192-01.json`](receipt_FTR-20261102-41559192-01.json), `partial_fulltext_read`, 15 section locators; `record --dry-run` passed against ledger tail `614dacd8`. It is staged for the integrator; if PROTON's receipt is recorded first, order the two by event ID. Artefact: `files/fulltext/PMC13472943_Hu2026_BioPathNet.xml`.

Decisive points from the paper:
- An explanation is a **gradient-based local approximation**: edge importance summed along paths. An influential path is not a mechanism.
- The drug task needs PrimeKG retraining per disease split, and NBFNet-class training was infeasible above 48 h per epoch even on GPUs.
- The drug task shows degree bias (0.23).
- Drug performance collapses without drug-gene edges.
- Drugs absent from PrimeKG cannot be predicted (memantine, lecanemab).

## Decision

**WATCH** (row in [`decisions.tsv`](decisions.tsv)).
- BioPathNet runs on CPU for prediction, and its WWOX gene-pathway ranking is specific.
- The capability that would justify it over LEGEND's path and PROTON, checkable explanation paths, needs more than 11 GB per query on CPU and was not obtained within the pre-registered limit.
- No drug model exists.

Reopen if any of these holds:
1. Explanation fits in 8 GB, or a larger host or an operator-authorised GPU is available. Then run step (c) unchanged.
2. A PrimeKG checkpoint is released with a DEE/WOREE-covering split.
3. A signed drug-target graph is available.

No card, IPOTESI or queue entry was created.

## What is in git and what was removed

In git: this README, the pre-registration, the availability table, `results.json`, the two TSVs and the receipt JSON. Not in git: no BioPathNet code, weights, Pathway Commons or KEGG rows.

Removed from scratch at the end:
- the venv (Python 3.10 + torch 2.0.1, about 1.3 GB (measured)), the uv cache and Python install
- the code clone (43 MB), the checkpoint (111 MB), `PC_KEGG_0602` (62 MB)
- the Pathway Commons 12 extended SIF (176 MB), the compiled extensions
- the run outputs and driver scripts

## Reproducibility record, added 2026-11-02 (IT19 P4)

Added by `scientist` after the fact. The trial was **not** rerun. Each item says whether it is **recovered** (verbatim from the original run's own record) or **reconstructed** (written now from recovered material).

**Where the original material survives.** Git holds only the package files: the `it18-biopath` branch was merged (`b8969305`) and its two commits (`751d80eb`, `4bcc1a72`) carry no driver. The scratch tree was deleted. The driver, every command and every tool output survive in the delegate's local session transcript (`agent-a32a58f8c2f709fe6.jsonl` under the orchestrator session `4325d70d`, sha256 `b49b87dfadf83fd4624d90c50891cfcad3ed73cf10b0844ec91b47ca5265dad9` on 2026-11-02). It is outside git and may be lost.

**Recovered: environment, in the order it was built (2026-11-01, 23:00-23:04 UTC).** All installs were public GETs.
1. `uv venv -p 3.10` with `UV_CACHE_DIR` and `UV_PYTHON_INSTALL_DIR` in scratch. `python3 -m venv` had failed because the host has no `ensurepip`. The result was Python 3.10.21.
2. `torch==2.4.0` (CPU index `https://download.pytorch.org/whl/cpu`), `torch_scatter` (wheels `https://data.pyg.org/whl/torch-2.4.0+cpu.html`), `torchdrug==0.2.1 --no-deps`, `"numpy<2" rdkit decorator matplotlib tqdm networkx ninja jinja2 lmdb easydict pyyaml setuptools`.
3. The import errors were fixed one at a time: `rdkit==2023.9.6` (torchdrug imports `mplCanvas`), `ogb==1.3.6 --no-deps` plus `pandas scikit-learn outdated urllib3 six`, `torch_cluster`, `fair-esm==2.0.0 --no-deps`, and the venv `bin` on `PATH` so that ninja is found.
4. With torch 2.4.0 the extension build failed: `ATen/SparseTensorUtils.h: No such file or directory`.
5. Then `torch==2.0.1` (CPU), with `torch_scatter torch_cluster --reinstall` from `https://data.pyg.org/whl/torch-2.0.1+cpu.html` (giving 2.1.2+pt20cpu and 1.6.3+pt20cpu), and `"setuptools<70"` because `pkg_resources` was missing. After this the extension compiled, with `TORCH_EXTENSIONS_DIR` in scratch.

**Recovered: inputs and digests.**
- Code: `git clone` of `https://github.com/emyyue/BioPathNet.git` with `GIT_LFS_SKIP_SMUDGE=1`, HEAD `b051a9003a1363b5655cdb7dfdad60609c0e4fe3`.
- Checkpoint: `https://media.githubusercontent.com/media/emyyue/BioPathNet/main/experiments/KnowledgeGraphCompletionBiomed/biomedical/NBFNet/2025-05-17-23-27-40-436508/model_epoch_12.pth`, 110,765,951 bytes, sha256 `da298d1039b055852366362b494e773e86f5030abab33c8a620b2725c1ffe441`. Its training log is the `log.txt` beside it, sha256 `f77f95e58de8e932b776e7a94cf48437f03da941de1b810b86f7d8cf9f80466b`.
- Data: the six `PC_KEGG_0602` files from the same media path. Their sha256 values are in Stage 1 above and were checked against the LFS oids.
- Pathway Commons 12 `PathwayCommons12.All.hgnc.txt.gz` from `https://download.baderlab.org/PathwayCommons/PC2/v12/`, sha256 `e468612ca08c2c02f2131158019973d03e60c9892104fd20e2a331393127144e`.
- Paper XML: `files/fulltext/PMC13472943_Hu2026_BioPathNet.xml`, sha256 `83b0b3713d75257ea63d73d0c4077e4bb00e703278e3ebc1ce92f23eae99015b`. This one is still on disk.

**Recovered: configuration.** The driver builds the model in code with the architecture from the checkpoint's training log (`gfun.yaml`): NBFNet, `input_dim` 32, `hidden_dims` 6 x 32, `distmult`, `pna`, `short_cut`, `layer_norm`, `dependent`, `remove_one_hop`, `num_negative` 32, `strict_negative`, `adversarial_temperature` 1, `heterogeneous_negative` and `heterogeneous_evaluation`, `full_batch_eval`. Inference-only settings: `gpus: null`, `batch_size` 2, `torch.set_num_threads(2)`, seed 1024, and `remove_pos` true only in sanity mode. Dataset files: `train1.txt`, `train2.txt`, `valid.txt`, plus one query file, which differs by mode. The query files were:
- `test_pred.txt`: WWOX and the 10 controls, each against `hsa04390` as a placeholder tail.
- `test_vis.txt`: WWOX against `hsa05168`, `hsa04390` and `hsa04144`.

**Recovered: commands** (scratch paths abbreviated; `V` = venv, `S` = scratch; the driver was named `drive.py` in scratch).
```
export PATH=$V/bin:$PATH TORCH_EXTENSIONS_DIR=$S/torch_ext
/usr/bin/time -v $V/bin/python drive_it18_recovered.py $S/src $S/run/data $S/ckpt/model_epoch_12.pth $S/run predict    # exit 0, 5:24.83 wall, max RSS 1,519,840 kB
/usr/bin/time -v $V/bin/python drive_it18_recovered.py $S/src $S/run/data $S/ckpt/model_epoch_12.pth $S/run visualize  # "Command terminated by signal 9", 1:22.27 wall, max RSS 11,267,116 kB
```

**Recovered: the limit, and what kind of limit it was.** The 8 GB limit was a **threshold read after the fact**: nothing enforced it. The job ran with no memory cap and was stopped by the host's global OOM killer at 11.27 GB, so it overshot the limit by 3.3 GB. The user journal records `turbovnc-desktop.service: A process of this unit has been killed by the OOM killer` at 23:11:56 and the unit restarting at 23:12:06. That unit is the desktop user service in which the sessions and the trial ran. So the overshoot reached the shared session, not only the job. `/usr/bin/time` printed `Exit status: 0` beside `Command terminated by signal 9`, so its exit-status line alone does not show a kill.

**Reconstructed: how a rerun would enforce the limit.** This is the IT19 P4 recipe, measured on a harmless load and recorded in the repurposing adapter convention. Prefix the visualize command with `systemd-run --user --scope --collect -p MemoryMax=8G -p MemorySwapMax=0 --quiet`. The kernel then kills the job inside its own cgroup at 8 GB, and the job exits 137. This is the reopen condition 1 in Decision, made enforceable. It was not run on BioPathNet.

**Recovered: helper scripts, not reproduced here** (sha256 of the text as written):
- `prep.py` `006b10921911a4689321fc6c6b7aab8b0da040b5c8168156db21887ac281cc36`: degree-matched unannotated controls by lowest symbol sha256, the 100-triplet sample, and the query file.
- `refB.py` `2973d2a9a708ffa44beae452f003c6ea04c04da1b99b2088b5fe55c496b4b7fa`: neighbour vote B and the need-relevant pathway set.
- `measure.py` `ccc69fe0e65bf42f475770ae1fc9d0c2dafe718e8c3bc2d4bbe414782395f372`: the counts, Jaccard values and hubs in `results.json`.
- `prov.py` `58d9cd03de9910def90eecc851d0e1555fce5a12b539688853b38010976d075d`: provenance of explanation steps from Pathway Commons 12. It was never run, because there were no explanations.

**Recovered: the driver**, verbatim, as [`drive_it18_recovered.py`](drive_it18_recovered.py), sha256 `b478913dd25cfca752aeb8c18e319a532cf680a1b86bf595324b22cfc2bbab0e`. It is the same text that was written to scratch on 2026-11-01 at 23:01:54 UTC, and it is LEGEND's own code: it contains no BioPathNet code and imports the MIT clone from the path given as `SRC`. Usage: `drive_it18_recovered.py SRC DATA CKPT OUT {sanity,predict,visualize}`. It has no `--help`, and it is a historical executable note, not a reusable tool.

**Not re-imported.** No BioPathNet code, weights, Pathway Commons or KEGG rows were downloaded again for this addition. The terms are as in Stage 1: data not cleared for redistribution.
