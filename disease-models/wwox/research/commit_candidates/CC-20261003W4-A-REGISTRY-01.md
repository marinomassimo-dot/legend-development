# COMMIT CANDIDATE — CC-20261003W4-A-REGISTRY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 4 2026-10-03, branch `task/sci-A-20261003w4`.
**context_policy:** `SOURCE_FIRST` — first pass written from the sources before any registry record was opened; comparison afterwards (see `research/intake_wave_20261003w4_A.md`).
**Not medical advice.** Class-level statements about published genotypes only.

## Target
- `paper_registry_current.md`: **create** `PAPER 151` (Tarta-Arsene 2017 — no identity record existed), `PAPER 152` (Zhao 2020, promotes `CORPUS-STUB-056`), `PAPER 153` (Kośla 2020, promotes `CORPUS-STUB-007`), `PAPER 154` (Baryła 2022 — only `LIT-0029` existed), `PAPER 155` (Li 2014, promotes `CORPUS-STUB-037`); two field updates on each promoted stub.
- `literature_tracking_log_current.md`: **create** `LIT-0444` (Tarta-Arsene); update `LIT-0080`, `LIT-0034`, `LIT-0029`, `LIT-0061`, `LIT-0356`.

## Registry landing per PMID handled (wave-1 correction 8)
| PMID | PAPER record | LIT record | needs creation? | evidence-depth update carried by |
|---|---|---|---|---|
| 30361190 | `PAPER 045` (exists; `CORPUS P356` kept) | `LIT-0356` (exists) | no | `CC-20261003W4-A-SHAUKAT-01` (PAPER) · this candidate (LIT) |
| 28721938 | `PAPER 151` (new) | `LIT-0444` (new) | **yes — only `FT-121` existed** | this candidate |
| 33300063 | `PAPER 152` (new, promotes `CORPUS-STUB-056`) | `LIT-0080` (exists) | PAPER yes | this candidate |
| 32389029 | `PAPER 153` (new, promotes `CORPUS-STUB-007`) | `LIT-0034` (exists) | PAPER yes | this candidate |
| 36271927 | `PAPER 154` (new) | `LIT-0029` (exists) | PAPER yes — no `CORPUS` or `PAPER` record existed | this candidate |
| 24520212 | `PAPER 155` (new, promotes `CORPUS-STUB-037`) | `LIT-0061` (exists) | PAPER yes | this candidate |

**Numbers are provisional.** Measured 2026-10-03 ~11:30Z with `registry_records.py catalog` after merging `main` 663970a: highest landed `PAPER 150`, `LIT-0443` (`BATCH_20261003_002` propagated the wave-3 registry candidates). This candidate takes `PAPER 151`-`155` and `LIT-0444`; the first draft's `PAPER 148`-`152` / `LIT-0442` collided with that batch and were renumbered before landing. Wave-4 peers B and C may claim the same numbers; the integrator renumbers in event order, updates the wikilinks `PAPER 151`-`155` used in the other `CC-20261003W4-A-*` candidates, and re-anchors the first `insert-after` of each list on the highest `PAPER` / `LIT` record then present (the dry run anchored on the landed `PAPER 150` / `LIT-0443`).

## Change class
**MINOR** — paper additions and placeholder promotion (§ 7). No claim status, no working-model block.

## Ordering
Receipts (prepared, not appended): `FTR-20261003-{30361190,28721938,33300063,32389029,36271927,24520212}-01`. They must be appended before this candidate is propagated, so no record cites a receipt the ledger does not hold.

## Op list — `paper_registry_current.md` (record-scoped; dry run 2026-10-03 with `record_scoped_edit.py apply` on copies of `main` 663970a (merged into the branch, after `BATCH_20261003_002` landed): exit 0, 11 op(s), keys ['PAPER 150', 'PAPER 151', 'PAPER 152', 'PAPER 153', 'PAPER 154', 'CORPUS-STUB-056', 'CORPUS-STUB-056', 'CORPUS-STUB-007', 'CORPUS-STUB-007', 'CORPUS-STUB-037', 'CORPUS-STUB-037'])

```json
[
 {
  "op": "insert-after",
  "id": "PAPER 150",
  "text": "\n## PAPER 151\n**Short title:** Tarta-Arsene 2017 Epileptic Disord — one WOREE patient, normal head circumference; the same patient as Piard 2019 P8\n**Full title:** Practical clues for diagnosing WWOX encephalopathy\n**Authors:** Tarta-Arsene O, Barca D, Craiu D, Iliescu C\n**Year:** 2017\n**Source type:** primary research — clinical commentary on a single case\n**Journal/source:** *Epileptic Disord* 2017;19(3):357-361\n**Identifier:** PMID 28721938 / DOI 10.1684/epd.2017.0924 — bronze OA (publisher PDF)\n**Status:** processed\n**Record provenance:** created by `CC-20261003W4-A-REGISTRY-01` (intake wave 4 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`. No earlier `CORPUS`, `PAPER` or `LIT` record existed (`FT-121`).\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-28721938-01`; manifest `deepdive_manifests/PMID28721938.json`; dossier `research/fulltext_dossiers/PMID28721938.md`\n**Primary pathway:** clinical spectrum / WWOX-DEE\n**Model/species:** human\n**Genotype/model:** compound heterozygous `c.173-1G>T` (intron 2 acceptor; splice effect predicted in this paper, measured as exon 3 skipping for the same allele in another patient of PMID 30356099) + `c.918del p.(Glu306Aspfs*21)`; predicted null / null\n**Transferability:** T1 for the null/null clinical course\n**clinical relevance:** MODERATE\n**Claim links:** none\n**Role:** Normal head circumference throughout with progressive atrophy; first MRI thin corpus callosum with normal myelination for age; death at almost 3 years. 🔴 **Count once:** identical genotype and every compared attribute match [[paper_registry_current#PAPER 117]] Patient 8, which Piard presents as novel without citing this report (`PREMISE: INFERENZA`, `CC-20261003W4-A-PATIENT-OVERLAP-01`). Do not sum the two sources.\n**LIT link:** [[literature_tracking_log_current#LIT-0444]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 151",
  "text": "\n## PAPER 152\n**Short title:** Zhao 2020 Mol Med Rep — WWOX lowers Beclin-1/LC3 and raises p-mTOR in paclitaxel-treated ovarian carcinoma lines; flux not clamped on any WWOX arm\n**Full title:** WWOX promotes apoptosis and inhibits autophagy in paclitaxel-treated ovarian carcinoma cells\n**Authors:** Zhao Y, Wang W, Pan W, Yu Y, Huang W, Gao J, Zhang Y, Zhang S\n**Year:** 2020\n**Source type:** primary research — cell-line study\n**Journal/source:** *Mol Med Rep* 2021;23(2):115 (epub 2020-12-10)\n**Identifier:** PMID 33300063 / DOI 10.3892/mmr.2020.11754 — bronze OA (publisher PDF)\n**Status:** processed\n**Record provenance:** created by `CC-20261003W4-A-REGISTRY-01` (intake wave 4 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`. Promotes [[paper_registry_current#CORPUS-STUB-056]] (kept as history).\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-33300063-01`; manifest `deepdive_manifests/PMID33300063.json`; dossier `research/fulltext_dossiers/PMID33300063.md`\n**Primary pathway:** autophagy / mTOR (cancer)\n**Model/species:** human ovarian carcinoma cell lines\n**Genotype/model:** plasmid overexpression and one siRNA in A2780 / A2780-T / SKOV3; no human allele modelled\n**Transferability:** T3 — epithelial cancer lines, overexpression\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** Sign on steady-state abundance: WWOX up → Beclin-1 and LC3 down, p-mTOR up; WWOX down → the reverse (representative blots, no densitometry, no statistics). The only chloroquine clamp is on the paclitaxel arm; p-p70S6K barely detected although the Discussion says 'mTOR/p70S6K'; no mTOR-inhibitor epistasis. The abstract's 'reduced WWOX' in the resistant line contradicts its Results (highest basal WWOX there). See `FT-074`, `CC-20261003W4-A-AUTOPHAGY-01`.\n**LIT link:** [[literature_tracking_log_current#LIT-0080]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 152",
  "text": "\n## PAPER 153\n**Short title:** Kośla 2020 Exp Biol Med — review, WWOX in brain development and pathology (Lodz group)\n**Full title:** The WWOX gene in brain development and pathology\n**Authors:** Kośla K, Kałuzińska Ż, Bednarek AK\n**Year:** 2020\n**Source type:** **narrative review** — no primary data\n**Journal/source:** *Exp Biol Med (Maywood)* 2020;245(13):1122-1129\n**Identifier:** PMID 32389029 / PMCID PMC7400721 / DOI 10.1177/1535370220924618\n**Status:** processed\n**Record provenance:** created by `CC-20261003W4-A-REGISTRY-01` (intake wave 4 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`. Promotes [[paper_registry_current#CORPUS-STUB-007]] (kept as history).\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-32389029-01` (figure images unobtainable; schematics read as captions); manifest `deepdive_manifests/PMID32389029.json`; dossier `research/fulltext_dossiers/PMID32389029.md`\n**Primary pathway:** CNS development / review\n**Model/species:** review\n**Genotype/model:** n/a\n**Transferability:** T3 — background only\n**clinical relevance:** LOW\n**Claim links:** none — background\n**Role:** Background only, not a claim source. Same group as [[paper_registry_current#PAPER 154]]; the two are not independent. 🔴 Its Table 1 reference numbers disagree with its running text for the same findings; its WOREE definition ('premature STOP codons in two alleles … complete lack of WWOX') is narrower than the cohort it cites; the heterozygous-animal memory sentence is cited to a Zfra/3xTg paper and is unverified; 'in great majority may be lethal in embryonic development' is uncited.\n**LIT link:** [[literature_tracking_log_current#LIT-0034]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 153",
  "text": "\n## PAPER 154\n**Short title:** Baryła 2022 J Mol Med — review, WWOX and metabolic regulation (Lodz group)\n**Full title:** WWOX and metabolic regulation in normal and pathological conditions\n**Authors:** Baryła I, Kośla K, Bednarek AK\n**Year:** 2022\n**Source type:** **narrative review** — no primary data\n**Journal/source:** *J Mol Med (Berl)* 2022;100(12):1691-1702\n**Identifier:** PMID 36271927 / PMCID PMC9691486 / DOI 10.1007/s00109-022-02265-5\n**Status:** processed\n**Record provenance:** created by `CC-20261003W4-A-REGISTRY-01` (intake wave 4 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`. Only `LIT-0029` existed (no `CORPUS` or `PAPER` record).\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-36271927-01` (earlier `FTR-20260921-36271927-01`, partial: no figure, no bibliography); manifest `deepdive_manifests/PMID36271927.json`; dossier `research/fulltext_dossiers/PMID36271927.md`\n**Primary pathway:** metabolism / review\n**Model/species:** review\n**Genotype/model:** n/a\n**Transferability:** T3 — background only\n**clinical relevance:** LOW\n**Claim links:** none — background\n**Role:** Background only. The HIF1A arc resolves to refs 26, 14, 15, 74, 84, 88; refs 15 and 74 are the authors' own. 🔴 'MRI of WOREE patients … usually shows also reduced myelination' is not supported by its cited Piard aggregate (delayed myelination 2/34) and its evidence list cites one patient twice (refs 13 and 66). Osteopenia, listed in the abstract beside human conditions, rests on homozygous knockout mice only. See `FT-111`, `CC-20261003W4-A-REVIEWS-01`.\n**LIT link:** [[literature_tracking_log_current#LIT-0029]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 154",
  "text": "\n## PAPER 155\n**Short title:** Li 2014 Int J Biol Sci — review, WWOX in metabolic disorders and tumours\n**Full title:** Common Chromosomal Fragile Site Gene WWOX in Metabolic Disorders and Tumors\n**Authors:** Li J, Liu J, Ren Y, Yang J, Liu P\n**Year:** 2014\n**Source type:** **narrative review** — no primary data\n**Journal/source:** *Int J Biol Sci* 2014;10(2):142-148\n**Identifier:** PMID 24520212 / PMCID PMC3920169 / DOI 10.7150/ijbs.7727\n**Status:** processed\n**Record provenance:** created by `CC-20261003W4-A-REGISTRY-01` (intake wave 4 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`. Promotes [[paper_registry_current#CORPUS-STUB-037]] (kept as history).\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-24520212-01`; manifest `deepdive_manifests/PMID24520212.json`; dossier `research/fulltext_dossiers/PMID24520212.md`\n**Primary pathway:** metabolism / tumour suppression / review\n**Model/species:** review\n**Genotype/model:** n/a\n**Transferability:** T3 — background only\n**clinical relevance:** LOW\n**Claim links:** none — background\n**Role:** Background only; nothing neural. 🔴 **Do not cite for the heterozygote tumour figure:** it attaches 10/58 vs 2/60 to ENU-treated mice and lung papillary carcinoma, whereas the corpus's reading of the cited primary ([[paper_registry_current#PAPER 078]], `CLAIM 032`) has those numbers as spontaneous tumours. Its skeletal sentence says 'mice' and cites the rat *lde* paper.\n**LIT link:** [[literature_tracking_log_current#LIT-0061]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-056",
  "old": "**Status:** not_processed",
  "new": "**Status:** promoted — see [[paper_registry_current#PAPER 152]]"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-056",
  "old": "**Next action:** screening / triage required",
  "new": "**Next action:** none — upgraded to [[paper_registry_current#PAPER 152]] by `CC-20261003W4-A-REGISTRY-01`; this placeholder is kept as history"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-007",
  "old": "**Status:** not_processed",
  "new": "**Status:** promoted — see [[paper_registry_current#PAPER 153]]"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-007",
  "old": "**Next action:** screening / triage required",
  "new": "**Next action:** none — upgraded to [[paper_registry_current#PAPER 153]] by `CC-20261003W4-A-REGISTRY-01`; this placeholder is kept as history"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-037",
  "old": "**Status:** not_processed",
  "new": "**Status:** promoted — see [[paper_registry_current#PAPER 155]]"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-037",
  "old": "**Next action:** screening / triage required",
  "new": "**Next action:** none — upgraded to [[paper_registry_current#PAPER 155]] by `CC-20261003W4-A-REGISTRY-01`; this placeholder is kept as history"
 }
]
```

## Op list — `literature_tracking_log_current.md` (record-scoped; dry run 2026-10-03 with `record_scoped_edit.py apply` on copies of `main` 663970a (merged into the branch, after `BATCH_20261003_002` landed): exit 0, 6 op(s), keys ['LIT-0443', 'LIT-0080', 'LIT-0034', 'LIT-0029', 'LIT-0061', 'LIT-0356'])

```json
[
 {
  "op": "insert-after",
  "id": "LIT-0443",
  "text": "\n## LIT-0444\n**Short title:** Tarta-Arsene 2017 Epileptic Disord — one WOREE patient, normal head circumference (= Piard 2019 P8)\n**Authors:** Tarta-Arsene O, Barca D, Craiu D, Iliescu C\n**Year:** 2017\n**Source type:** primary research — clinical commentary, single case\n**Journal/source:** *Epileptic Disord* 2017;19(3):357-361\n**Identifier type:** PMID / DOI\n**Identifier value:** PMID 28721938 / DOI 10.1684/epd.2017.0924\n**Date discovered:** 2026-09-21 (harvest-to-registry gap, `FT-121`)\n**Date processed:** 2026-10-03 (`FTR-20261003-28721938-01`)\n**Discovery source:** Orchestrator selection record of intake wave 4 2026-10-03\n**Status:** processed\n**Status note:** `complete_fulltext_read`; record created by `CC-20261003W4-A-REGISTRY-01`\n**Primary pathway:** clinical spectrum / WWOX-DEE\n**Transferability:** T1 for the null/null clinical course\n**clinical relevance:** MODERATE\n**Claim links:** none\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w4_A.md` · `CC-20261003W4-A-REGISTRY-01` · `CC-20261003W4-A-PATIENT-OVERLAP-01`\n**Next action:** none owed — count the patient once with Piard 2019 P8\n**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID28721938.json`\n"
 },
 {
  "op": "replace-within",
  "id": "LIT-0080",
  "old": "**Next action:** screening and tier assignment",
  "new": "**Next action:** none — processed 2026-10-03 (`FTR-20261003-33300063-01`) and recorded as [[paper_registry_current#PAPER 152]] by `CC-20261003W4-A-REGISTRY-01`; Zhao Y et al. 2020, *Mol Med Rep* 23:115; steady-state autophagy proteins only, ovarian cancer lines; the placeholder fields above are kept as history"
 },
 {
  "op": "replace-within",
  "id": "LIT-0034",
  "old": "**Next action:** screening and tier assignment",
  "new": "**Next action:** none — processed 2026-10-03 (`FTR-20261003-32389029-01`) and recorded as [[paper_registry_current#PAPER 153]] by `CC-20261003W4-A-REGISTRY-01`; Kośla K et al. 2020, *Exp Biol Med* 245:1122; narrative review, `partial_fulltext_read` (figure images unobtainable); the placeholder fields above are kept as history"
 },
 {
  "op": "replace-within",
  "id": "LIT-0029",
  "old": "**Next action:** screening and tier assignment",
  "new": "**Next action:** none — processed 2026-10-03 (`FTR-20261003-36271927-01`) and recorded as [[paper_registry_current#PAPER 154]] by `CC-20261003W4-A-REGISTRY-01`; Baryła I et al. 2022, *J Mol Med* 100:1691; narrative review; earlier partial read `FTR-20260921-36271927-01`; the placeholder fields above are kept as history"
 },
 {
  "op": "replace-within",
  "id": "LIT-0061",
  "old": "**Next action:** screening and tier assignment",
  "new": "**Next action:** none — processed 2026-10-03 (`FTR-20261003-24520212-01`) and recorded as [[paper_registry_current#PAPER 155]] by `CC-20261003W4-A-REGISTRY-01`; Li J et al. 2014, *Int J Biol Sci* 10:142; narrative review; the placeholder fields above are kept as history"
 },
 {
  "op": "replace-within",
  "id": "LIT-0356",
  "old": "**Next action:** full-text retrieval + deep-dive in next session",
  "new": "**Next action:** none — promoted earlier to [[paper_registry_current#PAPER 045]]; first receipted full-text read 2026-10-03 (`FTR-20261003-30361190-01`, `complete_fulltext_read`; the earlier `FTR-20260726-30361190-01` is a legacy reconstruction); see `CC-20261003W4-A-SHAUKAT-01`"
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(the intron-2 acceptor allele's splice effect is predicted in this paper | v.2.7.1) predicted a likely aberrant effect on splic- | PMID 28721938, Case study; files/fulltext/PMID28721938_TartaArsene2017_JLE.txt)
(the only lysosomal clamp is on the paclitaxel arm in the sensitive line | agic flux induced by PTX, A2780 cells were co‑treated with | PMID 33300063, Results 'PTX increases autophagic flux'; files/fulltext/PMID33300063_Zhao2020_Spandidos.txt)
(Table 1's reference numbers for astrocytoma differ from the running text's | Its expression was determined in astrocytoma tumor samples of various grades from 38 patients by immunohistochemical staining | PMID 32389029, section 'Astrocytomas' (ref 70) vs Table 1 (ref 68); files/fulltext/PMID32389029_Kosla2020_PMC.xml)


## BATCH DISPOSITION — `BATCH_20261003_003` (2026-10-03, ACTOR_ID `scientist`, Scientist H), append-only

**Verdict:** PROPAGATED

**PROPAGATED.** Eleven ops on `paper_registry_current.md` and six on `literature_tracking_log_current.md`, record-scoped, exit 0. Numbers measured with `registry_records.py catalog` at `f110c76` (highest `PAPER 150`, `LIT-0443`): the declared `PAPER 151`–`155` and `LIT-0444` were **all free**, so nothing was renumbered here; the B and C chains were anchored after them instead (`PAPER 156`–`158`, `159`–`164`, `LIT-0445`–`0453`). One integrator amendment (AM3, from blind audit 2 T05): `PAPER 151`'s Role now carries the age with the myelination finding — the first MRI at 5 weeks reads normal myelination *for age*, the second at 2.6 years reads delayed myelination. A later repair also added *(partial full text)* to `PAPER 153`'s depth line, because `partial_fulltext_read` alone is not a marker `coverage_report` reads.
