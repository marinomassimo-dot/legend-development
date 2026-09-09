# STATE MANIFEST — LEGEND (public disease-level fixture)

> **Foundational file.** Active state of the LEGEND system.
> This is the only **state-control** file updatable outside a `BATCH_COMMIT`.
> Designated non-canonical append-only ledgers are explicit carve-outs: they may append
> through their validated writers, but never replace the four scientific current files.
> Every operational event (ingest, lint, commit candidate, batch commit, branch) must update it.
>
> **Public edition note.** This is a **disease-level fixture**, not the operational state of any private working instance. It carries no patient record and no session-specific operational history. It exists so the framework is internally coherent and (eventually) LINT-passable at the disease-model level. Values are illustrative placeholders for the public WWOX disease model.

---

## 0. PURPOSE

Track, unambiguously and readably:

- active framework version
- active disease-model (working-model) version
- state of each `*_current.md` file
- last completed `BATCH_COMMIT`
- last `LINT` run
- current operational state of the system
- active parallel branches (if any)

Without an up-to-date manifest → system in `UNKNOWN` state → `BLOCK_SYSTEM`.

---

## 1. SYSTEM VERSION

```yaml
framework_version: v3.3.1
framework_file: framework/instruction/LEGEND_CORE.md
manifest_schema_version: 1.0
edition: public
```

---

## 2. DISEASE-MODEL (WORKING-MODEL) VERSION

```yaml
working_model_version: WM_v4.3
working_model_file: disease-models/wwox/registries/working_model_current.md
narrative_view: disease-models/wwox/disease_model.md
notes: "Canonical disease-level working model derived from public literature; disease_model.md is its narrative reader-facing view. The private individual-level record is not part of this edition."
```

**Rule:** every `BATCH_COMMIT` that modifies the disease model **must** bump `working_model_version` (format `WM_vMAJOR.MINOR`).

- MINOR bump: claim addition/modification, block update without reversals
- MAJOR bump: reversal of a baseline claim, block redefinition, authorized urgent commit

Commit candidates must declare their intended `target_wm_version`.

---

## 3. CURRENT FILES STATE

### 3.1 Disease-model canonical files

| File | Status | Notes |
|------|--------|-------|
| `disease-models/wwox/registries/working_model_current.md` | present | **canonical** disease-level working model — claim mirror, changelog, decision blocks |
| `disease-models/wwox/disease_model.md` | present | narrative reader-facing view of the same model |
| `disease-models/wwox/registries/claim_registry_current.md` | present | canonical claims (public literature) |
| `disease-models/wwox/registries/paper_registry_current.md` | present | integrated / baseline-linked papers |
| `disease-models/wwox/registries/literature_tracking_log_current.md` | present | lifecycle state of every paper in the pipeline |

### 3.2 Meta-analyses

| File | Status |
|------|--------|
| `disease-models/wwox/meta/meta_index_current.md` | present |
| `disease-models/wwox/meta/meta_network_myelin_glia_current.md` | present |
| `disease-models/wwox/meta/meta_metabolism_current.md` | present |
| `disease-models/wwox/meta/meta_prenatal_structure_current.md` | present |
| `disease-models/wwox/meta/meta_human_spectrum_current.md` | present |
| `disease-models/wwox/meta/meta_gaba_paradox_current.md` | present |

### 3.3 Compounding-memory files (non-canonical, append-only)

| File | Status | Notes |
|------|--------|-------|
| `disease-models/wwox/research/discovery_ledger_current.md` | present | cumulative discovery capital — leads toward biomarkers, molecules, repurposing |
| `disease-models/wwox/research/therapeutic_hypotheses_ledger_current.md` | present | scored hypothesis portfolio from the co-scientist loop |
| `disease-models/wwox/research/dismissal_ledger_current.md` | present | rejections with their `REVIVAL_TRIGGER` — nothing dies in silence |
| `framework/eval/learned_gates_registry.md` | present | reusable error-prevention gates distilled from failures |
| `disease-models/wwox/registries/fulltext_read_receipts.jsonl` | present | authoritative append-only full-text event ledger; hash-chained and tail-anchored (§6.1), LINT-verified; includes explicitly non-contemporaneous legacy reconstructions |

### 3.4 Operational files (private overlay — not in this repository)

| File | Status | Notes |
|------|--------|-------|
| `inbox_current.md` | not shipped | ingest quarantine |
| `session_commit_log.md` | not shipped | commit-candidate queue; the LINT checks it when present |
| `legend_activity_log.md` | not shipped | operational timeline |
| `capability_scout_log.md` | not shipped | capability-growth log |

---

## 4. LAST BATCH_COMMIT

```yaml
last_batch_commit_id: BATCH_20260815_001
last_batch_commit_date: 2026-08-15
last_batch_commit_type: MINOR
commit_candidates_propagated: 15
commit_candidates_superseded: 1
commit_candidates_deferred: 1
batch_20260815_001_scope: "PROPAGATED 15 candidate packages after semantic comparison with the canonical state. Added PAPER 064-080 and LIT-0406-0409; completed thirteen existing literature records. Corrected PAPER 011/024/039 and qualified CLAIM 009/011/032/034/036. CC-20260810-34831305-01 was already propagated and was not duplicated. CC-20260814-23370280-01 supersedes bullet 3 of CC-20260810-41984841-01. The infrastructure-only evidence-pair ratchet proposal remains deferred. No baseline reversal or therapeutic promotion. Snapshot backup/snap_20260815_batch_wm43; LINT, receipt chain, growth anchors and self-eval PASS."
batch_20260810_005_scope: "PROPAGATED 2, and the batch's own subject is a defect it found while propagating: THE WORKING-MODEL CLAIM MIRROR HAD NOT MOVED WITH THE CLAIMS. BATCH_20260810_001 flagged CLAIM 004 and CLAIM 011 for review in the claim registry and left the working_model mirror showing both as consolidated baseline — a reader of the model alone saw two healthy baselines where the registry recorded two defects, for four batches. Corrected in both directions. (1) CC-20260810-34831305-01: CORPUS-STUB-003 promoted to PAPER 063 (PMID 34831305, Steinberg & Aqeilan 2021, model atlas), placeholder preserved append-only, LIT-0030 completed. It is a review and is recorded as one — Claim links: none, BACKGROUND as claim evidence, no independent corroboration of the primaries it enumerates. (2) PMID 34747138 complete-read propagation, no candidate file: the content is deepdive_manifests/PMID34747138.json (20 locators, validator PASS) and the registry work is mechanics over it, the same shape as PAPER 060/061/062. CLAIM 004 RETURNS to consolidated baseline because its flag is RESOLVED, not waived: the missing comparator is now written into the claim. Where the rescue is compared to WT, either the comparison is not drawn (myelinated axons per field, CC1+, PDGFRa+ — every bracket runs WT-vs-KO and KO-vs-rescued) or it is significant AGAINST the rescue (unmyelinated axons per field, ~26 in WT versus ~52 in treated, **). The g-ratio does normalise. Corollaries recorded: 60-70% neuronal transduction, oligodendrocytes never transduced, P0 window with the stated reason and post-natal dosing declared future work, n=3 for EM, ketamine for the electrophysiology, and a tumour non-finding qualified three times in a tumour suppressor whose periphery stays null. CLAIM 003 gains the boundary of 'non-cell-autonomous': it is a component, not the whole phenomenon, and the authors' attribution of the residue to an oligodendrocyte-autonomous WWOX function is their IPOTESI while the residual gap is DATO. CLAIM 011 STAYS flagged and the threshold is now written into the three narrative working-model lines that repeated 'dose-dependent' — the lexicon of a continuum where Figure 3B shows a threshold between 1.23 and 2.63 x 10^11 vg. CLAIM 016 receives a boundary its own primary's locator had carried since the day of the reading and that never reached canonical: lithium suppressed PTZ seizures in ALL THREE genotypes including wild-type (PMID 32000863 Fig 7b, read from the image), so the experiment does not establish a WWOX-specific pharmacological rescue. The same gap was found independently from the other side, because PAPER 063 transmits the genotype-specific reading the primary's panel does not support. Registry correction: PAPER 005 named CORPUS-STUB-042 as its own duplicate and it is not — 042 is PMID 35107375, filovirus VP40 — so an innocent placeholder was one batch away from being absorbed into another record. PMID 21212533 locator debt CLOSED: the 2026-07-26 reading predated the requirement and carried a declared waiver; the text layer is SUSPECT and no XML/HTML surface exists for the article, so 14 locators are anchored to the printed page through 11 crops that regenerate to their declared digest (regenerate_adjudications.py verify PASS over 18 artifacts and 37 locator resolutions; manifest schema-2, strict validator PASS, 0 gaps). Opening the figures corrected three things in DL-MECH-068: the '~3-10x' factor is not a measurement and understates — the two titration series are not matched (beta1 0-3 ug/mL, beta2 0-10, no shared maximum) and there is no densitometry, so the panel supports >=10x by inspection and no ratio; Figure 4 marks the insert between V303 and K304 against the UniProt K303 the ledger cited, one residue apart with nothing load-bearing moved; and Figure 5 says MORE than the text did, since beta1-deltaCT phosphorylates tau as well as WT with visibly LESS enzyme while beta2-deltaCT falls to mock level with a strong band. Figure 1's total-tau control is not equal across lanes and the asymmetry runs against the paper's conclusion, not with it. Also merged, as integrator and not on the branch's word: codex/pmid-34831305, whose stated precondition was that its two figures exist in the shared files/ with a verified hash — they do, checked by running the strict validator with the shared checkout as artifact root, PASS with 0 gaps over all three artifacts. codex/pmid-42422765-s8 is NOT merged: it appends a receipt on the same ledger prev_hash as this branch did, so the two cannot both be kept by concatenation, and the operator's own precondition is that it incorporate main first. LINT PASS pre-flight and post-propagation; growth anchors PASS with papers +1 declared through the tool; ledger 63 chained and tail-anchored."
batch_20260810_004_scope: "PROPAGATED 1, closing the debt BATCH_20260810_003 exposed rather than leaving it named. CORPUS-STUB-108 promoted to PAPER 062 (PMID 24871327, Iatan 2014), placeholder preserved append-only, LIT-0128 completed, and meta_metabolism now names the PAPER record instead of the placeholder it had to point at yesterday. No commit-candidate file existed for this reading: the content comes from deepdive_manifests/PMID24871327.json and fulltext_dossiers/PMID24871327_locators.md, which are the reading, and the registry work is mechanics over them — the same shape as PAPER 060 and PAPER 061. THE FINDING THE RECORD NOW CARRIES: this is the primary that PAPER 055 called 'strong evidence' for the WWOX -> lipid homeostasis -> myelin bridge, and the label does not transfer. The paper's central result is a NEGATIVE — removing Wwox from hepatocytes does NOT lower circulating HDL; the HDL effect appears only in the whole-body null, measured in two-day-old pups that die by four weeks. What the primary licenses is WWOX -> ApoA-I/ABCA1 -> HDL biogenesis, whole-body and not hepatocyte-autonomous. The second leg, lipid homeostasis -> myelin, gets NOTHING here: the paper measures no neural endpoint anywhere. PREMISE_TAG on any inference that crossed from this node to myelin. Claim links: none, and the reading is the reason none is created. The node stays open as ESPANSIONE — ApoA-I and ABCA1 are independently relevant to CNS lipid handling — to be tested, not as a supported inference. FT-039 closed. Declared debt: Supplementary unavailable (AHA all-rights-reserved, cascade documented) carrying the P=0.0025 triglyceride datum, and the multi-hop is FT-046."
batch_20260810_003_scope: "PROPAGATED 1, and the queue of deferred candidates is now empty. CC-20260810-30755385: CORPUS-STUB-039 promoted to PAPER 061 (PMID 30755385, AbuRemaileh 2019, muscle-specific Wwox KO), placeholder preserved append-only, LIT-0063 completed. Linked to CLAIM 009 as supporting evidence that skeletal-muscle WWOX loss is SUFFICIENT for local and systemic metabolic phenotypes, with two boundaries written into both the claim and the paper record: the model is a conditional muscle KO and not a WWOX-DEE allele, so nothing transfers to CNS; and mitochondrial glucose oxidation was NEVER MEASURED — no respirometry, no flux assay. meta_metabolism_current.md listed 'reduced glucose oxidation' under Core Findings (DATO); it was an inference from upstream markers sitting among the data, and is now labelled, with the promotion condition attached (ex-vivo flux on primary fibres, or muscle-specific rescue). CLAIM 009 stays INFERENZA and its Type is unchanged. The causal boundary is recorded too: tissue-specific deletion plus local FDG plus acute C2C12 knock-down support a muscle-intrinsic component and do not prove the whole in-vivo phenotype is tissue-autonomous. The 'tissue of measurement is not tissue of necessity' inference is written into the integrated model as INFERENZA with its three sources and its promotion condition. Two things it exposed and did not hide: PMID 24871327 is read but still CORPUS-STUB-108, so the meta names the placeholder rather than a PAPER record that does not exist; and the ITT age discrepancy (Figure 2 caption 10 months, Methods 4.4 six months) is carried on the paper record with the instruction to declare both ages until it is resolved at source."
batch_20260810_002_scope: "PROPAGATED 2. CC-20260810-42422765-S8: the shorthand 'finestra terapeutica P1-P5' is removed from the PAPER record for PMID 42422765 and replaced with what Figure S8 shows — efficacy at several early postnatal doses including P5, the interval incompletely sampled per endpoint, the upper boundary beyond P5 untested. S8 has no P0 group; survival to P40 omits P4 and to P300 keeps only P1 and P5; weight and glucose at P14 draw WT-vs-KO and WT-vs-P5 with no treated-vs-KO comparison, and ns is not equivalence; panels E-I test P5 only. 'P1-P5' read as a validated continuous window what is a sparse set of sampled points with the comparison that matters never drawn. CC-20260805-001: CORPUS-STUB-095 promoted to PAPER 060 (PMID 37519886, Kolat 2023), placeholder preserved append-only, LIT-0117 completed from 'corpus paper 95' to full metadata with its complete_fulltext_read receipt. Promotion of provenance, not of scope: T3, clinical relevance LOW, no claim link, DISCOVERY_ONLY. STILL DEFERRED 1: CC-20260810-30755385, whose registry promotion is mechanical but which also asks for a meta_metabolism rewrite separating direct measurement from inferred mitochondrial glucose oxidation, and a CLAIM 009 link. Half-applying it would leave the registry claiming a reading the meta does not carry. Its two most transferable products are already recorded outside the canonical layer and are not waiting on it: FT-048 (the ITT age discrepancy) and FT-049 (tissue of measurement is not tissue of necessity, as INFERENZA with its three sources)."
target_wm_version: WM_v4.3
last_wm_update: 2026-08-15
last_wm_batch_commit_id: BATCH_20260815_001
trigger: "explicit operator authorization 2026-08-15; threshold also met"
batch_20260810_001_scope: "PROPAGATED 3: step 0 (batch_commit_gate BLOCK_BATCH_COMMIT -> OPEN, with the reopening recorded as road 3 and not the condition originally written); CC-20260810-CLAIM004-REVIEW (CLAIM 004 -> flagged for review, comparator missing); CC-20260810-CLAIM011-REVIEW (CLAIM 011 -> flagged for review, dose-response continuum concealing a threshold; the instruction named CLAIM 020, which is Teplyshova natural history and unrelated — flagging it would have marked an innocent claim and left the defect standing). Coupled with step 0 and applied in the same window: deepdive_manifests/PMID17803050.json re-anchored, 29 body/table locators moved off the refused .html onto page crops with needle, crop, dpi and image digest; validator PASS, 0 gaps. DEFERRED 3, declared not forgotten: CC-20260805-001 (PMID 37519886 registry promotion), CC-20260810-30755385 (CORPUS-STUB-039/LIT-0063 promotion + meta_metabolism + CLAIM 009 link), CC-20260810-42422765-S8 (the 'finestra terapeutica P1-P5' shorthand in paper_registry line 261 is wrong: S8 contains no P0 group, survival to P40 omits P4, and the drawn tests are WT-vs-KO and WT-vs-P5 with no treated-vs-KO comparison). Each deferred candidate is a registry rewrite needing its source open, and a batch that half-applies one is worse than a batch that declares it. Full-text queue entries FT-048 and FT-049 were added ahead of this batch, outside it: the queue is not a canonical scientific file."
notes: "BATCH_20260806_002 (MINOR, WM_v4.0 → WM_v4.1). Four candidates propagated: CC-20260806-19936220, CC-20260806-19500159, CC-20260806-17803050 and CC-20260806-31340538. CC-20260806-19936220 item 1 was SUPERSEDED by CC-20260806-19500159 item 1 before propagation — the verdict moved from 'unsupported' to 'contradicted' once the terminus was read — so the superseded count is 1. THE IMPORTED-PREMISE CHAIN UNDER CLAIM 005 IS NOW TRACED END TO END, EVERY LINK READ IN FULL: early death is first-hand in PMID 19936220, but epileptogenesis is not measured there in any form, and the terminal source PMID 19500159 states in three places, plus a Table 2 whose Epilepsy row is empty for both mouse models, that Wwox-null MICE SHOW NO EPILEPSY. Two citation hops had converted an explicit negative about a rat into a positive assertion about a mouse; the co-cited premise in the same sentence was true, which is why it read as verified. New claims 036 (systemic metabolic decompensation of the P18 mouse null as a quantified confounder, with PREMISE: DEFAULT_FROM_TEXTBOOK on brain ablation never shown), 037 (the seizure phenotype as a rat lde/lde phenotype, EEG-documented, allele corrected to structurally frameshift and functionally protein-null), 038 (recurring BUN/creatinine with two competing untested explanations, renal insufficiency versus seizure-driven hypercatabolism, the second competing directly with the renal-tubular-acidosis hypothesis PMID 19936220 never tested), 039 (ataxia 95 percent versus 0 percent, non-cerebellar, the most penetrant lde phenotype and one the downstream literature dropped). PAPER 057/058/059 and LIT-0405 created; CORPUS P295 and P363 marked promoted append-only. PAPER 021 metadata corrected: the author is Tochigi, not Kumada, and the record carried an INVENTED TITLE naming lissencephaly, a word absent from the paper, which had been steering it toward a migration/layering reading the study does not make; CLAIM 014/015 now bound it to early postnatal maturation (PND5-21) and meta_prenatal_structure reclassifies it as the postnatal bridge. DIS-011 and DIS-012 entered in the dismissal ledger with revival triggers. meta_gaba_paradox given a provenance correction and the competing systemic-confounder explanation. Integrity status fields added to the held records PMID 16223882 (expression of concern) and PMID 23446842 (retracted), closing a debt declared at session start; no canonical claim rests on either. Pre-flight and post-propagation LINT PASS; release gate PASS/0; receipts 52 chained and tail-anchored; self-eval PASS with active complete reads 15. Snapshot backup/snap_20260806_batch_wm41. Prev: CC-20260806-30290271 → CLAIM 005 narrowed to what PMID 30290271 measures and its medication caution DELETED (the source tests no drug, no GABA concentration, no inhibitory function); PAPER 006 / LIT-006 identifiers normalized; CORPUS-STUB-085 resolved as duplicate, preserved append-only; meta_gaba_paradox corrected from interneuron loss to marker-positive abundance, NPY marked DG-only, Il6-not-Tnf-a recorded. MAJOR because removing safety language from a consolidated baseline claim is a policy change even when it removes rather than adds; the experimental datum is NOT demoted. Publication-integrity audit of the 7 held records run first (staging/audit_publication_integrity_20260806.md): no canonical claim rests on any of them. Pre-flight and post-propagation LINT PASS; snapshot backup/snap_20260806_batch_wm40. Prev: BATCH_20260726_001 (MINOR, WM_v3.2) — CC-20260726-001, CC-20260726-002 and CC-20260726-003 → PAPER 054/055/056, CLAIM 034/035 new, CLAIM 009/016/024 modified; snapshot backup/snap_20260726_1600. (Identifiers expanded 2026-08-10 from the shorthand 'CC-20260726-001/002/003': a compressed range reads fine to a person and names exactly one candidate to a machine, so the backlog counter reported 002 and 003 as pending forever. The record is unchanged in meaning; it is now readable by the thing that reads it.)."
```

---

## 5. LAST LINT

```yaml
last_lint_type: LINT_AUTOMATIC
last_lint_id: LINT_20260906_HARNESS_AGILE
last_lint_date: 2026-09-06
last_lint_result: PASS
notes: "PMID 30290271 read completely from article HTML/PDF with all six figures, Table 1, both supplements and 90 references audited. Receipt FTR-20260806-30290271-01 appended (46 -> 47 events). After adversarial cross-review, its schema-v2 manifest carries 14 exact body-text locators plus 7 fingerprinted figure locators and passes strict verification with zero gaps. The candidate is explicitly MAJOR (target WM_v4.0_2026-08-06), deletes unsupported medication-safety language and requires operator authorization; unread-premise baseline is the live 13/13 and self-eval is 24/24 PASS. PubMed pipeline commits 212850e, 510414d and d9ccac9 merged and independently hardened. A fresh 2026-08-06 harvest preserves 706/706 records, 693 abstracts in the gitignored NOT_EVIDENCE corpus and a tracked no-abstract projection with 40 correction links. RefType direction was corrected: 7 affected publications are held, while 4 editorial notices remain admissible audit sources. Five held PMIDs occur on current surfaces, but none is integrated as a canonical PAPER and no claim wikilink depends on one; PMID 28151481 was already explicitly excluded. Legacy receipt FTR-20260726-23446842-01 was the sole receipt-to-PAPER identity mismatch and is quarantined append-only by FTR-20260806-23446842-02; active depth and generated coverage no longer attribute it to PMID 23446842. LINT PASS; public release gate PASS/BLOCKS 0. The pre-refresh clean-worktree release suite passed with one declared local-fulltext skip; post-refresh suite pending this lint event. 2026-08-06 continuation (LINT_20260806_007): an independent blind review with no context on the code reproduced eight further defects, all fixed — the corpus content firewall was disabled by the process working directory (fail-open at write, fail-closed forever at read); the same guard refused honest prose describing a permitted triage use; the LINT integrity gate could not see the CORPUS placeholders two held records live in, and blocked claims citing the retraction notice itself; `status --pmid` ignored invalidations. Earlier in the same pass, an invalidation was found to withdraw a paper's whole reading history instead of the named event. Firewall detection re-tuned against the seed's real column set: six of eight escapes closed, both false positives gone, gzip/UTF-16 declared open rather than patched. Withdrawing a complete read now requires re-opening the reading debt. Two DisMech consumers left uncorrected by design: their SHA-256 is sealed into the Phase-2 baseline and re-sealing without re-deriving would falsify provenance. BATCH_20260806_001 propagated (MAJOR, WM_v4.0). Release regressions PASS WITH SKIPS on a clean worktree. 2026-08-06 continuation (LINT_20260806_008): FT-043 closed — PMID 19936220 (Ludes-Meyers 2009, PLoS ONE) retrieved open-access and read completely; receipts FTR-20260806-19936220-01 and its correction -02 appended (48 -> 50 events); schema-v2 manifest carries 23 verified locators (18 body, 2 table, 3 figure), zero gaps, zero waivers, and was mutation-tested 8/8 before persistence including proof that an abstract-only sentence cannot validate a body locator. THE PREMISE SPLITS: early death is first-hand and quantified in PMID 19936220 (43% dead by 72 h, 77% by day 17, none past weaning), but EPILEPTOGENESIS IS NOT MEASURED THERE IN ANY FORM — no EEG, seizure, behaviour or brain histology; the only brain measurement in the paper is organ weight. It enters only as a Discussion citation of the rat lde model (PMID 19500159/17803050: 13-bp exon-9 deletion, C-terminal frameshift, NOT a null, audiogenic seizures), so five canonical surfaces credit a mouse paper with a rat phenotype across two allele classes. FT-042 and FT-041 re-prioritised as the actual terminus. Also recorded: EIIA-Cre here versus BK5-Cre in PMID 30290271 (shared allele, different knockout); Wwox ablation shown only in kidney, lung and spleen with no brain lysate anywhere (tagged PREMISE: DEFAULT_FROM_TEXTBOOK with a revival trigger); a measured systemic metabolic crisis at P18 that makes brain-phenotype confounding quantified rather than speculative; brain weight is relative-only brain sparing, not overgrowth; the osteosarcoma conflict with PMID 17360458 is explicit and unresolved; and the paper's own renal-tubular-acidosis hypothesis is the sole PubMed record on WWOX and acidosis, untested for seventeen years. Corrections isolated in staging/commit_candidate_20260806_19936220.md (MINOR, target WM_v4.1); no canonical scientific current file edited. The session's own trace-contract regression caught this session's receipt naming a gitignored staging path as an output — corrected append-only, never rewritten. Two gates added: IMPORTED_PREMISE_ATTRIBUTION_GATE and SEALED_CONSUMER_CIRCULARITY_GATE. LINT PASS; release gate PASS/BLOCKS 0; self-eval PASS with active complete reads 12 -> 13. Release regressions FAIL on exactly the three declared at session start (DisMech seal, its runner-verdict echo, and the environmental release-surface roots); the DisMech Phase-2 window decision remains open and is deliberately unresolved. 2026-08-06 continuation (LINT_20260806_009): FT-042 closed — PMID 19500159 (Suzuki 2009, Genes Brain Behav) obtained by the operator through institutional access after eight automated retrieval tiers refused it (bronze OA, single Wiley location, Cloudflare), then read completely; receipt FTR-20260806-19500159-01 appended (50 -> 51 events); schema-v2 manifest carries 30 verified locators (24 body, 2 table, 4 figure), zero gaps, zero section waivers. THE CHAIN IS NOW CLOSED AND THE PREMISE IS NOT UNSUPPORTED BUT CONTRADICTED: the terminal source states in three places, and in a Table 2 whose Epilepsy row is empty for both mouse models, that WWOX KNOCKOUT MICE SHOW NO EPILEPSY. Two citation hops converted an explicit negative about a rat into a positive assertion about a mouse. The rat phenotype is instead solid and first-hand: 95% audiogenic penetrance (19/20), 60% spontaneous (30/50), 0/14 controls, kindling-like latency shortening, interictal ~10 Hz spikes in all mutants unstimulated, hippocampal vacuoles 9/9 versus 0/10. Yesterday's allele-class note is corrected: the lde allele is structurally a C-terminal frameshift and functionally a protein-level null (mRNA normal, no 47 or 42 kDa species, antibody epitope outside the altered region). Recorded with revival triggers: the paper attributes the mutant protein's disappearance to the ubiquitin-proteasome system with no turnover assay, inhibitor or route determination, the same default falsified on 2026-07-12; the headline 95% is a female-only cohort stated only in the Figure 6 caption; and Figure 1's caption misassigns its own panels. OPEN AND CONTESTED: the paper's 'clearly excluded' rejection of a systemic metabolic cause rests entirely on unread FT-041, whose abstract — supplied by the operator, recorded as abstract_only with NO receipt because an abstract is not a reading — reports significantly increased urea nitrogen, creatinine and phosphate. FT-041 is now the highest-value unread paper in the repository. Supplementary declared unavailable, not skipped: HTTP 403 on both Wiley routes, no embedded files. Because the paper exists in no structured form, its PDF text layer was transcribed into a local HTML artifact with the abstract in a recognised container, and the abstract/body separation was proven before use rather than assumed. Mutation testing found two defects in the validator itself, not in the reading: abstract_snippet was never matched against the abstract (fixed in deepdive_manifest.py with two regression tests, the new test itself proven able to fail), and source_fulltext_indexed remains a self-declared boolean nothing verifies (recorded as open debt, not silenced). Corrections isolated in staging/commit_candidate_20260806_19500159.md (MINOR, target WM_v4.1), superseding item 1 of the 19936220 candidate; no canonical scientific current file edited. The operator closed the DisMech Phase-2 window and re-sealed with a three-tier scope (970ded7), so that pair is green and SEALED_CONSUMER_CIRCULARITY_GATE is marked SUPERSEDED by the stronger executable FREEZE_SCOPE_GATE. LINT PASS; release gate PASS/BLOCKS 0; self-eval PASS with active complete reads 13 -> 14; release regressions FAIL only on the environmental release-surface roots. 2026-08-06 continuation (LINT_20260806_010): FT-041 closed — PMID 17803050 (Suzuki 2007, Comparative Medicine; NO DOI, no PMCID, unaddressable by every OA aggregator) supplied by the operator and read completely; receipt FTR-20260806-17803050-01 appended (51 -> 52 events); schema-v2 manifest with 32 verified locators (25 body, 4 table, 3 figure), zero gaps, mutation-tested 6/6. THE CHAIN IS NOW TRACED END TO END, EVERY LINK READ IN FULL. Split verdict on FT-042's 'clearly excluded': the SPECIFIC mouse/rat serum contrast is CONFIRMED (glucose, calcium and electrolytes all non-significant in the rat), but the blanket statement is FALSE — BUN is 3.2-3.5x normal and creatinine significantly raised, so the rat is uraemic without being hypoglycaemic and the systemic confounder is not eliminated but different in kind. THE FINDING THIS READ ADDS: the authors propose that raised BUN/creatinine may reflect hypercatabolism and muscle disruption from repeated seizures rather than renal failure, with the SER strain as named precedent — a hypothesis that competes directly with the renal-tubular-acidosis explanation PMID 19936220 built for the mouse on the same marker and never considered; WWOX AND (hypercatabolism OR muscle disruption) returns 0 PubMed records. A SECOND FT-042 CLAIM IS REFUTED BY ITS OWN SOURCE: the attribution of lde dwarfism to low pituitary growth hormone rests on a phrase that exists only in THIS PAPER'S ABSTRACT; the body reports the difference as not significant and concludes the dwarfism cannot be explained by low GH. That is the third instance in one session of a citation firming up its source, and the first where the overstatement originates inside the source's own abstract. METHOD NOTE: the operator had supplied that abstract hours earlier and it was recorded as abstract_only with NO receipt, leaving FT-041 open; had it been accepted as a reading, 'decreased plasma GH' would have entered the model as a datum, and it is not one. Also recorded: ataxia at 95 percent and non-cerebellar is the most penetrant lde phenotype, more than the 34 percent seizures, and the downstream literature carries it not at all; the seizure incidence is a floor by the authors' own statement; the Mendelian chi-square rests on a survivor-selected 33 of 254 litters; brain sparing recurs with male absolute brain weight not significantly reduced; and the paper was accepted two years before the same group mapped lde to Wwox, with none of its 35 references WWOX-related, so its phenotypes cannot be a WWOX-motivated result. The abstract_snippet guard added earlier today ran in production on this manifest, validated a real anchor and caught a fabricated one. Corrections isolated in staging/commit_candidate_20260806_17803050.md (MINOR, target WM_v4.1), completing the trilogy with the 19936220 and 19500159 candidates; no canonical scientific current file edited. LINT PASS; release gate PASS/BLOCKS 0; self-eval PASS with active complete reads 14 -> 15."
```

---

## 6. OPERATIONAL STATE

```yaml
current_state: READY
deep_dive_gate: OPEN
ingest_gate: OPEN
batch_commit_gate: OPEN
active_parallel_branches: none
```

### Why `batch_commit_gate` is closed — 2026-08-09

**Not because the verifier is weak.** It was, and it has been repaired and mutation-tested
8/8. The gate is closed because of what the repaired verifier now *reports*.

`files/fulltext/PMID17803050_Suzuki2007.html` — the declared `article_text` behind `PAPER 059`,
the primary source of `CLAIM 038` and `CLAIM 039` — carries **34 C0 controls standing in for
characters that did not survive extraction**: 17 × `U+001D`, 9 × `U+000C`, 5 × `U+001E`,
3 × `U+001F`. Two are confirmed against the printed page: `(P \x1d 0.023)` for `(P < 0.023)`,
and `Ca2\x0c` for `Ca²⁺`. The validator now refuses that surface outright, so **29 canonical
locators are unverifiable** — by the system's own check, not by anyone's opinion.

Reading and locator capture stay safe, which is why this is `BLOCK_BATCH_COMMIT` and **not**
`BLOCK_SYSTEM`: nothing about acquiring evidence is compromised. Promotion is what must wait,
because promoting now would consolidate claims whose evidence chain the validator rejects.

**What lifts it:** the surface re-derived from the source — never hand-corrected. A manual fix
across 34 points is indistinguishable from a rewrite and verifiable by nothing. Then the 29
locators re-verified against the new artifact, and any that fail re-captured from the document.

The conclusions of `CLAIM 038` and `CLAIM 039` are **not** in question here. A human read them
off the paper. What is in question is whether the repository can still *prove* it.

### Reopened 2026-08-10 — by a different route than the one written above

🔴 **The condition as written was not met, and the gate is opened anyway.** Recorded, because
a gate lifted on a condition nobody re-read is how a gate stops meaning anything.

The surface was **not** re-derived. `PMID17803050_Suzuki2007.html` is still `SUSPECT` and the
validator still refuses it — correctly, and that has not changed. What was done instead is
road 3 of the three the reading laid out: the 29 locators were **re-anchored to the printed
page**, the surface the corruption cannot reach because the drawn glyph is the author's.

What stands behind them, each machine-checked rather than argued:

- every locator resolves through a **needle unique on its page**, verified to be a fragment of
  the snippet of the locator it names — so a crop cannot adjudicate the right character for
  the wrong sentence;
- every span sits **inside the crop that claims to show it** (`crop_contains_span`),
  re-checked after the crop rectangles were rounded to integers;
- the seven crops **regenerate to their declared digest** from the source PDF
  (`regenerate_adjudications.py verify`), so the evidence is reproducible without the images
  being redistributed — the article is all-rights-reserved.

Six of the 29 carried corruption inside what they assert; all six were read off the page and
**not one changes a value, a direction or a significance verdict**. `CLAIM 038` and `CLAIM 039`
stand as written. What had been lost was the repository's ability to prove them.

**Applied in this batch:** `deepdive_manifests/PMID17803050.json` no longer declares the
refused `.html` as a source artifact. Its 29 body/table locators now carry `surface: figure`
and name the page crop that attests them, each with page, crop rectangle in PDF points, dpi,
needle and image digest. The three figure locators were already anchored to the PDF and are
untouched. `deepdive_manifest.py --pmid 17803050` returns PASS with 0 gaps.

**The debt that remains, and is not cleared by this:** the text surface is still refused, so
`PMID 17803050` cannot back a *new* text locator. Anyone reopening that paper in full owes
road 2 — the surface rebuilt from the rendering, declared as a new artifact with its own
extraction method. `FT-041` carries it.

---

## 6.1 FULL-TEXT RECEIPT LEDGER ANCHOR

The full-text receipt ledger is append-only. A per-event hash chain makes a rewritten or
deleted historical event detectable; it cannot detect a *truncated tail*, because the
surviving prefix stays self-consistent. The anchor below closes that gap: it pins how many
events the ledger must hold and the digest of its last one. `LINT_AUTOMATIC` verifies both,
and a mismatch is `BLOCK_SYSTEM` — reading history you cannot trust is worse than none.

```yaml
fulltext_ledger_path: disease-models/wwox/registries/fulltext_read_receipts.jsonl
fulltext_ledger_events: 154
fulltext_ledger_head: eb17f1398dce2861b4df40f00243c01b2222a4921e2eb3b785cfefbf757ae576
```

Maintained automatically — `fulltext_receipts.py record` re-anchors after every append.
To re-anchor by hand after an authorized repair:

```bash
python3 framework/scripts/fulltext_receipts.py anchor
python3 framework/scripts/fulltext_receipts.py verify
```

## 6.1bis SYNC EPOCH LEDGER ANCHOR

Several actors work in their own worktrees against one shared checkout. Realigning that
checkout is what turns a landed state into a **dependency** other actors must consume, so the
decision to move it — **and the decision not to move it** — is operational state. Announced in
a message it survives until the session ends; recorded in the ledger it survives the session.

The full history lives in the JSONL and is **not** duplicated in these notes. Only the anchor
is here, for the same reason as §6.1: a hash chain cannot see a truncated tail.

```yaml
sync_epoch_ledger_path: framework/state/sync_epochs.jsonl
sync_epoch_ledger_events: 1
sync_epoch_ledger_head: 1f10fc71a601d092fee56b9ced6ced72772e3c928de51e33f9463b2b18df1fdf
```

Plan is the only writer. Other actors read the ledger, measure state with allowlisted
read-only commands, supply **attributed** observations and may propose a trigger; they do not
append, re-anchor or move the shared checkout.

```bash
python3 framework/scripts/sync_epochs.py record --event event.json
python3 framework/scripts/sync_epochs.py verify
python3 framework/scripts/sync_epochs.py status
```

## 6.2 GROWTH ANCHORS

Every constant below that says *"how big the system is right now"* is written by
[`growth_anchors.py`](../scripts/growth_anchors.py) and by nothing else. **No value in this
section may be typed by hand.** The rule it enforces is stricter than "automate it": *updating
a constraint must cost at least as much as complying with it.* The recorder re-measures the
registries and refuses a declared delta that does not match them, so a number cannot be bumped
to make a suite green — the only way to move it is to have made the change you declare.

```yaml
growth_anchor_ledger: framework/state/growth_anchors.jsonl
growth_anchor_events: 22
growth_anchor_head: 6ae2f309a69c080fe3e4e3ffdb6c0361b62ad3248136e00dbc1b0054ac277518
```

```bash
python3 framework/scripts/growth_anchors.py check     # live vs anchors
python3 framework/scripts/growth_anchors.py verify    # chain + tail anchor
python3 framework/scripts/growth_anchors.py record --batch <ID> --claims +4 --papers +3
python3 framework/scripts/growth_anchors.py tighten   # a ratchet fell; re-anchor it
```

The two ratchets documented below keep their own fields for backwards compatibility —
`legend_lint.py` and `session_self_eval.py` read them directly — but those fields are now
**written by `growth_anchors.py tighten`**, never by a person. The asymmetry is deliberate and
recorded here so a later reader does not mistake it for an oversight.

### Registry-declaration ratchet

Twenty registry records carry a historical `full text reviewed` declaration with no
surviving complete-coverage receipt. They are kept visible rather than deleted or
retroactively upgraded — the work happened, the evidence of *how completely* did not
survive. The baseline below is a **ratchet**: history is grandfathered by both count and
exact record identity. A count alone is insufficient because one old declaration could be
removed while a different unsupported declaration is added. Any *new* full-text declaration
must be backed by a persisted `complete_fulltext_read` receipt, or `LINT_AUTOMATIC` returns
`BLOCK_BATCH_COMMIT`.

```yaml
registry_only_fulltext_declarations_baseline: 13
registry_only_fulltext_declaration_ids: ["PAPER 012", "PAPER 014", "PAPER 016", "PAPER 028", "PAPER 032", "PAPER 042", "PAPER 043", "PAPER 044", "PAPER 045", "PAPER 046", "PAPER 049", "PAPER 050", "PAPER 053"]
```

Lowering the baseline is the intended direction of travel: back-fill a record with real
evidence, re-run `coverage_report.py`, then lower the number and remove that resolved ID
from the grandfathered list.

### Unread-premise ratchet

A separate and harsher debt, measured on 2026-07-26 by `session_self_eval.py`. The *reasoning*
layer — metas, therapeutic strategies, the analysis files — cites papers as **support for
conclusions**. The first measurement found seventeen of eighteen PMIDs with **no
complete-read receipt, no registry full-text declaration and no full-text-queue entry**. The
ratchet has since fallen as papers were read or their debt was made explicit; the current
baseline below must equal the live count, never preserve historical padding.

This is the failure mode that let PMID 22193544 be load-bearing in five files while unread,
with every existing check passing. It is invisible by construction, because leaning on a paper
writes nothing anywhere. So it is measured instead of assumed.

```yaml
unread_premise_baseline: 3
unread_premise_measured_on: 2026-09-09
```

**It is a ratchet, not a wall.** Blocking on the whole legacy backlog would only teach sessions
to route around the check; capping it makes every *new* unread premise a visible regression
(`UNREAD_PREMISE` → `BLOCK_BATCH_COMMIT`). Three things clear a citation, and only three: a
persisted `complete_fulltext_read` receipt, a registry record declaring the full text reviewed,
or an explicit `full_text_queue_current.md` entry. The third is what keeps the check honest
rather than punitive — **declared reading debt is legitimate work in progress; silence is not.**

### 6.4 — `panel_text_relation`: manifests that do not say whether anyone looked at the panel

A locator's `surface` records which surface a quote came **from**. It cannot record whether the
*other* surface was ever opened, and that is a different fact with its own failure mode. On
**2026-08-04** a figure panel reversed a conclusion the running text did not contain; on
**2026-08-06** an unmarked asterisk was the difference between *«not significant»* and *«not
tested»*; on **2026-08-10** Figure 3B turned a *«dose-dependent»* continuum into a threshold,
and a second panel showed that the comparison a rescue claim rested on had never been drawn.
In every case the text was **accurate and incomplete** — the one thing a text-only pipeline
cannot see.

So each schema-v2 locator declares `panel_text_relation`: `text_only` · `panel_only` ·
`text_confirmed_by_panel` · `text_contradicted_by_panel` · `panel_qualifies_text` ·
`unknown_legacy`. The two **coupled** relations must name the locator they bear on, as
`contradicts: "entries[N]"` and `qualifies: "entries[N]"`, and that pointer is a `BLOCK` when
missing — an unpointed assertion about another locator is prose in a JSON field that no reader
can trace and no command can check.

🔴 **`panel_qualifies_text` was added on 2026-08-10, on six independent instances across five
papers found by three actors who had not spoken.** The panel bears on the sentence and
*neither agrees nor disagrees with it*: on `PMID 36779245` the text says one versus two
missense variants make no difference while Figure 4A orders null/missense **above**
missense/missense with overlapping bands; on `PMID 32000863` the caption says lithium
suppressed seizures in `Wwox−/−` mice — **which is true** — and the panel shows the same
suppression in `+/+` and `+/−`; on `PMID 38182577` two pairs were **downgraded from
contradiction** after checking that the panel is not the one the sentence cites.

Every admitted value was **false** on those entries: `text_only` denies a panel that exists,
`panel_only` denies a text relation that exists, `text_confirmed_by_panel` is false,
`text_contradicted_by_panel` is the word that had been removed *after being verified wrong*,
and `unknown_legacy` is false for a reading made today. **When no admitted value is true, the
defect is the enum, not the choice** — forcing one would write a known falsehood into
canonical state, and that outlasts any ordering of contracts. *«Incomplete is not false»* is
the shortest statement of the relation.

The needle field is `qualifies_needle`, not the bare `needle` the value was first emitted
with. That is the **smaller** vocabulary, not the larger: `contradicts`/`contradicts_needle`
already fixes the grammar as `<pointer>`/`<pointer>_needle`, so a bare `needle` would be a
second naming convention living beside the first.

🔴 **And the pointer alone is not enough, because `entries[N]` is a position in an array that
can be reordered.** The three checks around it — the target exists, it is a text surface, it
is not this one — are every one of them blind to a **slip**: insert a locator above the target
and the index silently resolves to a different sentence, with all fields still well formed.
The prevention was already in the repository and had been **half-copied**: `adjudications.json`
never writes `entries[N]` alone, it writes it beside a **needle**, and `check_needles` asks two
arithmetic questions — does the needle occur exactly once, and is it a fragment of the snippet
of the locator it names. `contradicts` had taken the addressing grammar and left behind the
half that makes the address safe. So a contradiction now also carries `contradicts_needle`: a
fragment that must belong to the snippet the index resolves to and to **no other entry's**.
Address by content as well as by position — the move this repository makes everywhere else,
applied to the one place it had been left uncovered.

### 6.5 — the commit-candidate backlog: read, and not promoted

§6.3 measures what the reasoning layer leans on **without having read it**. Nothing measured
the mirror: a reading finished and never propagated. Leaning on a paper writes nothing
anywhere — and neither does stopping one step short of the registry.

Measured 2026-08-10, and the defect sat one level earlier than *"nobody counts them"*.
`staging/` held **12** `commit_candidate_*.md` of which most were long propagated, and only
5 carried a `Status:` line at all — in every case a claim's or a paper's status copied into the
body, never the candidate's own lifecycle. **The population a counter would count had no
state**, so a *"≥ 5 candidates"* trigger reading that directory would have fired permanently
and meant nothing.

The state is therefore **derived, never declared**. A `candidate_status:` field would be a
value someone must remember to flip, and flipping costs less than propagating — so on the day
the queue is inconvenient the field moves instead of the work. The signal already existed,
written for another purpose: **every `batch_*_scope` above names the candidates that batch
propagated.** Consumed = named in a scope; pending = on disk and named nowhere. The only way
to lower the number is to propagate, because the scope is what records it.

**A trigger, deliberately not a ratchet.** A ratchet would make accumulating candidates an
offence, and it is not one — between batches the backlog is *supposed* to grow, because the
system reads faster than it propagates. What must not happen is that it grows silently, so
above the trigger the next `BATCH_COMMIT` either propagates or records why not. Same contract
as `SCALE_TRIGGER`: nothing is wrong, something is due.

Its first run found a record no machine could read: `BATCH_20260726_001` had written
`CC-20260726-001/002/003`, a compressed range that names one candidate to a matcher and three
to a person, so 002 and 003 read as pending forever. **The manifest note was expanded rather
than the matcher loosened** — a matcher that guessed at ranges would eventually guess wrong in
the quiet direction, reporting as done work that nobody did.

```yaml
panel_relation_legacy_baseline: 13
panel_relation_legacy_ids: ["PMID17803050", "PMID19500159", "PMID19936220", "PMID22193544", "PMID24871327", "PMID30290271", "PMID30755385", "PMID31340538", "PMID33255508", "PMID34747138", "PMID35716775", "PMID37519886", "PMID40875931"]
```

🔴 **The eighteen are `unknown_legacy`, and the field is NOT backfilled by inference.** A
`surface: body` locator is not `text_only` by construction — it may be contradicted by a panel
nobody has opened. **The absence of a recorded contradiction is not evidence of its absence**,
so deriving the relation from the surface would manufacture eighteen manifests' worth of
reassurance out of no observation at all. `unknown_legacy` is the honest answer, and it is
paid down by re-reading, not by deducing.

**The split, and why it is a split.** `deepdive_manifest.validate` checks what one manifest can
answer about itself — that the value is in the enum, and that a contradiction names a text
locator that exists and is not itself. Whether a manifest is *allowed* to omit the field is a
fact about the corpus, not about the file, so it lives here: a manifest already in
`panel_relation_legacy_ids` is grandfathered, and one that is **not** appears as a new member
of a ratchet that may only fall (`RATCHET_VIOLATION` → `BLOCK`). That is "the validator refuses
new work without it", enforced where the information actually is.

**Why the ID list and not just the count.** Same reason as §6.3: a number is something a hand
can edit to make a suite green, and this repository has watched that happen, diligent comment
and all. The list is a claim the tool re-derives — lowering the baseline means naming which
manifest left the set, and `growth_anchors.py evaluate` goes and looks. Both fields are written
only by `growth_anchors.py record` / `tighten`; neither is typed by a human.

Membership is per manifest and one bare locator is enough. A reading that classified nineteen
locators and left one unclassified **has an unclassified locator** — the way out of the set is
to finish, not to average.

---

## 7. NOTES

Harness startup audit, 2026-09-09 (`plan`): task-specific context loading implemented;
measurements and validation: [session record](../../learning/plan/SLR-plan-20260909-startup-context-audit.md).

Harness maintenance, 2026-09-06: agile task closure, non-destructive Git option handling,
automatic regression discovery and weekly scouting at session start were implemented by
the operator-assigned `plan` actor. LINT PASS; scientific current files unchanged.
The Codex session could not write `.git/index.lock`; a Claude Code continuation of the same
actor re-verified every check, put the diff through a blind review (one BLOCK, repaired:
a conflicting merge no longer leaves `main` mid-merge) and landed it on `main` the same day.
Validation and session review: [SLR-plan-20260906-agile-closure](../../learning/plan/SLR-plan-20260906-agile-closure.md).

This fixture is intentionally free of any individual patient's operational history. The public edition separates three layers: the generic `framework/`, the disease-level `disease-models/wwox/`, and a private N-of-1 overlay that is **not** part of this repository.
