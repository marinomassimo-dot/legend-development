# CC-20261004W8-B-REGISTRY-01 — registry landing for the six Group B papers of intake wave 8

```yaml
context_policy: SOURCE_FIRST
actor: scientist (Group B, intake wave 8 2026-10-04)
branch: task/sci-B-20261004w8
change_class: MINOR
targets:
  - disease-models/wwox/registries/paper_registry_current.md
  - disease-models/wwox/registries/literature_tracking_log_current.md
```

> **Not medical advice.** Public edition: class level only.

## Why this candidate exists

Wave 1 left eight PMIDs with a completed reading and no registry presence, and LINT blocks
`BATCH_COMMIT` with `ORPHAN_COMPLETE_READ` until a record exists. All six PMIDs below carry a
receipt prepared in `scratchpad/receipts_pending_w8/` and a verified manifest. **Every one of them
needs a `PAPER` record and a `LIT` record**; none has either today
(`paper_packet.py packet --pmid N` reported "no title recorded", "no manifest", "receipts=0" for all
six before this reading).

## Numbers are PROVISIONAL

Measured with `registry_records.py catalog` on this worktree at commit `1741cd33a9e3`: highest
`PAPER 200`, highest `LIT-0493`. Scientists A and C of this same wave are landing their own registry
candidates in parallel, so these numbers **will** move. **The integrator renumbers in event order
and updates the anchors.** Re-measure before applying.

## Ops — paper_registry_current.md

Six `h2` sections appended in the section where `PAPER 200` currently sits, each in the shape of the
existing `PAPER` records.

| provisional id | PMID | DOI | short title to use |
|---|---|---|---|
| `PAPER 201` | 33129329 | 10.1186/s12917-020-02638-3 | Makii 2020 BMC Vet Res — a pure WWOX-measurement protocol, and the ceiling of every direct WWOX read-out it uses |
| `PAPER 202` | 40952239 | 10.1002/jcp.70092 | Carpanese 2025 J Cell Physiol — WWOX is one unquantified row of 283 in a murine KCa3.1 proxisome |
| `PAPER 203` | 41036104 | 10.1016/j.omtm.2025.101588 | Chornyy 2025 Mol Ther Methods Clin Dev — ten CNS promoters head to head; the cell-restricted one put the most protein in the liver |
| `PAPER 204` | 42137269 | 10.1016/j.omta.2026.201681 | Chauhan 2026 Mol Ther — a 126 bp non-viral mini-promoter in AAV-DJ, whose ranking inverts between IT and ICV |
| `PAPER 205` | 42136830 | 10.3389/fmed.2026.1819594 | Haque 2026 Front Med — lumbar IT reaches primate brain at 1–4 vg/DG, with no expression measured anywhere |
| `PAPER 206` | 41744777 | 10.3390/cells15040334 | Nabakowski 2026 Cells — liver de-targeting ~127-fold, at eight-fold worse packaging and fewer brain vector genomes |

Each record carries, in the existing field order: **Short title · Full title · Authors · Year ·
Source type · Journal/source · Identifier (PMID / PMCID / DOI) · Status: `processed` · Record
provenance · Evidence depth · Primary pathway · Model/species · Genotype/model · Transferability ·
clinical relevance · Claim links · Role · LIT link · Note**.

Field values that must not be guessed by the integrator:

| provisional id | Evidence depth | Model/species | Transferability | clinical relevance |
|---|---|---|---|---|
| `PAPER 201` | `partial_fulltext_read` — receipt `FTR-20261004-33129329-01`; manifest `deepdive_manifests/PMID33129329.json`; dossier `research/fulltext_dossiers/PMID33129329.md` | canine cutaneous mast cell tumour; canine and murine mast cell lines | T4 as biology; **T1 as an assay specification and as a ceiling on it** | MODERATE — it is the corpus's only end-to-end WWOX measurement protocol |
| `PAPER 202` | `partial_fulltext_read` — receipt `FTR-20261004-40952239-01`; manifest `deepdive_manifests/PMID40952239.json`; dossier `.../PMID40952239.md` | murine pancreatic ductal adenocarcinoma cells (KPCY) | T5 — murine Wwox, non-excitable epithelium, unvalidated proximity hit | LOW |
| `PAPER 203` | `partial_fulltext_read` — receipt `FTR-20261004-41036104-01`; manifest `.../PMID41036104.json`; dossier `.../PMID41036104.md` | C57Bl/6 mouse, neonatal P0–P1, i.c.v., ssAAV9-EGFP | T3 for promoter ranking; T4 for absolute values | MODERATE — promoter choice is a restoration-spec parameter |
| `PAPER 204` | `partial_fulltext_read` — receipt `FTR-20261004-42137269-01`; manifest `.../PMID42137269.json`; dossier `.../PMID42137269.md` | FVB/NJ mouse, neonatal i.v. and adult ICV/IT, **AAV-DJ** | T3 for the route-dependence result; T4 for the capsid, which is not AAV9 | MODERATE |
| `PAPER 205` | `partial_fulltext_read` — receipt `FTR-20261004-42136830-01`; manifest `.../PMID42136830.json`; dossier `.../PMID42136830.md` | cynomolgus macaque, lumbar IT and ICM | T2 for route biodistribution — the only primate record in Group B; T5 for anything about expression, which is absent | HIGH for route selection |
| `PAPER 206` | `partial_fulltext_read` — receipt `FTR-20261004-41744777-01`; manifest `.../PMID41744777.json`; dossier `.../PMID41744777.md` | C57BL/6 mouse, i.v. tail vein, ssAAV-Fluc | T3 for liver de-targeting; T4 for the CNS claim | MODERATE |

**`Claim links:` is `none` for all six**, and that is deliberate: no claim in
`claim_registry_current` rests on any of them yet. The two non-registry candidates of this wave
(`CC-20261004W8-B-BIOMARKER-01`, `CC-20261004W8-B-RESTORATION-SPEC-01`) propose the records that
would create those links; if either lands, its own op list adds the back-link here.

**`Record provenance:` text for each of the six**, verbatim, with only the id substituted:

> created by `CC-20261004W8-B-REGISTRY-01` (intake wave 8 2026-10-04, Scientist B). Provisional
> number, measured with `registry_records.py catalog` at commit `1741cd33a9e3` (highest `PAPER 200`,
> highest `LIT-0493`); Scientists A and C of the same wave are landing registry candidates in
> parallel, so the integrator renumbers in event order and updates the anchors.

**`Note:` for all six**, verbatim:

> class-level record; no individual-level detail is carried in this public edition. Not medical
> advice.

**`Role:`** — one sentence each, taken from the dossier's own verdict line; the integrator may copy
these verbatim:

- `PAPER 201` — 🔴 **Tier 1 modality demonstration under `LEGEND_CORE` §13; not a validated
  biomarker and not an endpoint.** No limit of detection, no linear range, no calibrator, no
  sensitivity, no specificity, no disease population anywhere in the paper. Measured reliability
  ceiling for the tissue read-out: weighted κ 0.264 (intensity) and 0.273 (percent positivity).
  The functional arm is an **earned negative** for proliferation and viability.
- `PAPER 202` — ⚪ **Earned null for the gene at the evidence level**: WWOX's entire presence is one
  row in a 283-protein annotation table with no numeric cell anywhere in the sheet, plus two
  Discussion sentences. The paper's own co-immunoprecipitation arm confirmed **2 of 8** candidates
  tested; WWOX was not among them.
- `PAPER 203` — 🟡 **WWOX appears zero times; read for the promoter question.** A cell-restricted
  astrocyte promoter produced the **most** hepatic protein of any promoter tested, which bounds the
  safety argument for promoter restriction.
- `PAPER 204` — 🟡 **WWOX appears zero times; read for cassette headroom.** 126 bp, all-human,
  non-viral. The same promoter ranked best of four by intrathecal delivery and among the worst by
  intracerebroventricular delivery — **promoter and route must be specified together.**
- `PAPER 205` — 🟡 **WWOX appears zero times; read for the route question.** 1–4 vg/DG in primate
  brain at ≥ 5.8 × 10^13 vg/animal, sublinear dose scaling, cerebellum lowest. The authors forbid
  reading vg/DG as a transduced-cell fraction and measure **no expression at all**.
- `PAPER 206` — 🟡 **WWOX appears zero times; read for the dose-ceiling question.** ~127-fold hepatic
  reduction, but eight-fold worse packaging and, by the paper's own Discussion, significantly fewer
  brain vector genomes than the parent capsid. **No toxicity endpoint of any kind** — the
  dose-ceiling claim is inferential.

## Ops — literature_tracking_log_current.md

Six `h2` sections appended after `LIT-0493`, provisional ids `LIT-0494` … `LIT-0499`, mapped in
order to `PAPER 201` … `PAPER 206`. Each carries **Short title · Authors · Year · Identifier ·
Status: `processed` · PAPER link** and the same class-level `Note`. The `PAPER` record's `LIT link:`
field and the `LIT` record's `PAPER` link are a matched pair and must be renumbered together.

## Change class

**MINOR.** Six new records; nothing existing is edited, narrowed or reversed. No `old` text is
replaced anywhere in this candidate, which is why no `old`/`new` pairs appear — every op is an
append.

## Checks the integrator should re-run after renumbering

```
python3 framework/scripts/registry_records.py catalog        # confirm the chosen numbers are free
python3 framework/scripts/legend_lint.py .                   # no ORPHAN_COMPLETE_READ for the six
python3 scripts/public_release_gate.py
```

### LOCATOR TRIPLES FOR BLIND AUDIT

(Identity triples only. This candidate asserts no scientific proposition; each triple fixes the
identity of a record to be created, against the artefact on disk.)

(PMID 33129329 is a 2020 BMC Veterinary Research study whose subject is the characterisation of WWOX expression and function in canine mast cell tumours | Characterization of WWOX expression and function in canine mast cell tumors and malignant mast cell lines | files/fulltext/PMID33129329_Makii2020_PMC.xml, front matter, article-title)

(PMID 40952239 is a 2025 Journal of Cellular Physiology study of the KCa3.1 interactome by TurboID proximity labelling in pancreatic tumour cells | Intermediate Conductance Calcium‐Dependent Potassium Channel (KCa3.1) Interacting Proteins Using Turboid‐Based Proximity Labeling Technology: Insights Into Interactome and Related Signaling Pathways in Pancreatic Tumors | files/fulltext/PMID40952239_Carpanese2025_PMC.xml, front matter, article-title)

(PMID 41036104 is a 2025 comparison of cell-specific promoters in AAV9-mediated CNS gene therapy | Comparative analysis of cell-specific promoters in AAV9-mediated gene therapy targeting the central nervous system | files/fulltext/PMID41036104_Chornyy2025_PMC.xml, front matter, article-title)

(PMID 42137269 is a 2026 design and initial characterisation of a mini-promoter for CNS gene therapies | Design and initial characterization of a novel mini-promoter for gene therapies targeting the central nervous system | files/fulltext/PMID42137269_Chauhan2026_PMC.xml, front matter, article-title)

(PMID 42136830 is a 2026 report of rAAV9 biodistribution in nonhuman primate brain and spinal cord after lumbar intrathecal infusion | rAAV9 vector biodistribution in nonhuman primate brain and spinal cord following lumbar intrathecal infusion | files/fulltext/PMID42136830_Haque2026_PMC.xml, front matter, article-title)

(PMID 41744777 is a 2026 report of a rationally designed AAV9 capsid variant with minimal liver tropism | A Rationally Designed AAV9-DM Capsid with Minimal Liver Tropism | files/fulltext/PMID41744777_Nabakowski2026_PMC.xml, front matter, article-title)
