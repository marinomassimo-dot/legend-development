# CC-20261003W3-C-ALLELE-CLASS-01 — the WWOX P252A / P282A record is wrong in two measurable ways

- `context_policy: QUESTION_DRIVEN` (declared in the dossier for PMID 41124647: the prior receipt's
  interpretive `evidence_basis` had to be read before the first pass in order to choose a
  `reread_reason`).
- Source: PMID 41124647 · DOI 10.1002/advs.202507602 · receipt `FTR-20261003-41124647-02`
  (prepared, not yet recorded) · manifest `disease-models/wwox/research/deepdive_manifests/PMID41124647.json`
  (VERDICT: PASS) · dossier `disease-models/wwox/research/fulltext_dossiers/PMID41124647.md`.
- Change class: **MINOR**. No `consolidated baseline` claim in `claim_registry_current.md` rests on
  this paper — `registry_records.py get --pmid 41124647` returns identity records plus two
  discovery-ledger mentions and no CLAIM. The candidate narrows two research-layer statements and
  fixes a publication year, and it *strengthens* rather than reverses the standing caution that this
  paper carries no neurological endpoint.

## Why

Two facts were out of reach of the 2026-09-21 reading, which declared figures, tables and
supplementary **unavailable**, and both are now on disk and inspected.

1. **The paper does state the domain architecture — in Figure 1D — and it puts P282A outside the
   SDR.** The figure draws a 414-residue protein with two WW boxes (ticks 16–49, 57–90) and an **SDR
   box spanning 125–262**; the P252A tick is inside that box and the P282A tick is to the right of
   its boundary. So only **one** of the two alleles is an SDR missense substitution. The repository
   currently says both are.
2. **Both alleles are common.** Supplementary Table 4 gives gnomAD allele frequencies of **0.0063**
   (P252A) and **0.0733** (P282A), with SIFT "Tolerated" and MutationTaster "Polymorphism automatic"
   for P282A. Under Hardy-Weinberg those predict homozygotes at roughly 4 × 10⁻⁵ and 5 × 10⁻³ of the
   population — orders of magnitude too common for an allele that abolishes WWOX function in a living
   human. This is a harder constraint on "complete loss of tumor-suppressive activity" than the
   authors' own hedge, and it is the population-genetic reason the proband has no WOREE phenotype.

Neither fact changes what the paper demonstrates about **P252A's degradation route**, which stands:
post-transcriptional loss, lysosome-dependent, proteasome-independent, macroautophagy-independent,
with an HSC70 co-IP and a *predicted* KFERQ-like motif.

## Ops (provisional; anchors re-measured at commit time)

### 1 · `disease-models/wwox/research/discovery_ledger_current.md`

| field | value |
|---|---|
| record id | `DL-MECH-047` |
| op | `replace-within` |
| old | `**Il dato.** Paziente con varianti germinali omozigoti **P252A** e **P282A**, entrambe nel dominio SDR (cancro tiroideo misto; **nessuna malattia neurologica**).` |
| new | `**Il dato.** Paziente con varianti germinali omozigoti **P252A** e **P282A** (cancro tiroideo misto; **nessuna malattia neurologica**). 🟠 **Rettifica 2026-10-03 (intake wave 3, receipt `FTR-20261003-41124647-02`):** solo **P252A** cade nel dominio SDR. La Figura 1D del paper — non ispezionabile nella lettura del 2026-09-21, ora sì — disegna il dominio **SDR fra i residui 125 e 262** su una proteina di 414 residui, e colloca **P282A fuori** da quel confine. Inoltre la Supplementary Table 4 riporta frequenze alleliche gnomAD di **0,0063 per P252A** e **0,0733 per P282A**: sotto Hardy-Weinberg gli omozigoti attesi sono ~4 × 10⁻⁵ e ~5 × 10⁻³ della popolazione, quindi **nessuno dei due alleli può essere un nullo funzionale in un organismo**. «Perdita completa di attività tumore-soppressiva» è un enunciato su un saggio di sovraespressione ingegnerizzata, non sull'allele in vivo.` |

### 2 · `disease-models/wwox/research/discovery_ledger_current.md`

| field | value |
|---|---|
| record id | `DL-BIO-001` |
| op | `replace-within` |
| old | `la collocazione dei due residui nello span SDR è **aritmetica del lettore, non del paper** — ` |
| new | `la collocazione dei due residui nello span SDR era **aritmetica del lettore** rispetto al **corpo del testo** — ma **non** rispetto al paper: la Figura 1D, ispezionata il 2026-10-03, dichiara il dominio **SDR 125–262** e colloca **P282A fuori** da esso, quindi solo P252A è un missenso del dominio SDR — ` |

### 3 · `disease-models/wwox/registries/paper_registry_current.md`

| field | value |
|---|---|
| record id | `CORPUS P348` |
| op | `replace-within` |
| old | `**Year:** 2026` |
| new | `**Year:** 2025` |

(PubMed gives a 2025-10-22 publication date for *Adv Sci* 13(1):e07602; the record says 2026. The
string is unique **within** record `CORPUS P348`.)

### 4 · `disease-models/wwox/registries/literature_tracking_log_current.md`

| field | value |
|---|---|
| record id | `LIT-0348` |
| op | `replace-within` |
| old | `**Year:** 2026` |
| new | `**Year:** 2025` |

## What would falsify this

For op 1 and 2: a reading of Figure 1D that places the P282A tick inside the SDR box, or a statement
elsewhere in the article giving different domain boundaries. For the frequency argument: a
demonstration that the gnomAD figures in Supplementary Table 4 are misreported, or evidence that the
allele is not in Hardy-Weinberg equilibrium in the relevant population — which would weaken the
expected-homozygote arithmetic without touching the raw frequencies.

### LOCATOR TRIPLES FOR BLIND AUDIT

(The paper's own domain schematic places P252A inside the SDR and P282A outside it. | [figure attestation — pixels cannot be quote-matched] Figure 1D, lower panel: a 414-residue protein bar with two diamond 'WW' boxes at ticks 16-49 and 57-90 and a box labelled 'SDR' spanning ticks 125-262; the labelled P252A tick falls inside the SDR box and the labelled P282A tick falls to the right of its 262 boundary. | Figure 1D, `files/fulltext/PMID41124647_Zhang2025_supplement/ADVS-13-e07602-g003.jpg`)

(Both alleles are common in gnomAD and P282A is called tolerated by two of the paper's own predictors. | [figure attestation — pixels cannot be quote-matched] (a table published only as a rendered page in the supplementary document) Supplementary Table 4 'WWOX germline variants detected in the patient': row 1 WWOX NM_016373 c.754C>G P252A, SIFT Deleterious, MutationTaster Disease causing, gnomAD allele frequency 0.0063, Genotype Homo; row 2 WWOX NM_016373 c.844C>G P282A, SIFT Tolerated, MutationTaster 'Polymorphism automatic', gnomAD allele frequency 0.0733, Genotype Homo. | Supplementary Table 4, `files/fulltext/PMID41124647_Zhang2025_supplement/ADVS-13-e07602-s001.docx`)

(The proband, homozygous for both missense alleles, had no WWOX-related neurological disease. | the cancer patient harboring germline homozygous WWOX P252A and P282A variants did not suffer from WWOX‐related nervous system disease | Discussion, para 2, `files/fulltext/PMID41124647_Zhang2025_PMC.xml`)

(The authors allow residual function rather than a complete null. | may have some residual protein function to maintain the development of the neurological system | Discussion, para 2, `files/fulltext/PMID41124647_Zhang2025_PMC.xml`)

(Chaperone-mediated autophagy is the authors' speculation, not their finding. | we speculated that lysosomal degradation of WWOX252A mutant protein occurred through chaperone‐mediated autophagy | Results, degradation section, `files/fulltext/PMID41124647_Zhang2025_PMC.xml`)

(Abundance and function are confounded for P252A and the paper says so. | likely due to the low abundance of the unstable WWOXP252A mutant | Results, POLE4 section, `files/fulltext/PMID41124647_Zhang2025_PMC.xml`)

(No nucleotide-excision-repair assay supports the POLE4 claim. | the functional relevance of WWOX‐POLE4 interaction in nucleotide excision repair remains to be elucidated | Discussion, POLE4 para, `files/fulltext/PMID41124647_Zhang2025_PMC.xml`)


---

## BATCH DISPOSITION — `BATCH_20261003_002` (2026-10-03, ACTOR_ID `scientist`, Scientist G), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED (MINOR — no claim rests on PMID 41124647)

All four ops applied (`DL-MECH-047`, `DL-BIO-001`, `CORPUS P348`, `LIT-0348`). Blind audit: 7 triples — 4 SUPPORTED (including the Figure 1D domain geometry, read directly: SDR 125–262, P282A outside), 2 SUPPORTED_NARROWER, **1 NOT_SUPPORTED**. 🔴 **The failure:** the triple *«chaperone-mediated autophagy is the authors' speculation, not their finding»* is false — the speculation is followed by an HSC70 co-IP and LAMP1 co-localisation and a declarative conclusion of degradation *through chaperone-mediated autophagy in the lysosome* (no CMA-specific loss-of-function test such as LAMP2A knockdown is reported). **No op of this candidate writes that proposition**, so nothing propagated rests on it; it is recorded here so no later writer carries it. **Narrowings:** P252A at 0.0063 is below the conventional 1% threshold, so only P282A is *common*; and four of the paper's own predictors call P282A damaging. **Integrator amendment:** the Hardy-Weinberg conclusion in `DL-MECH-047` is now tagged INFERENZA with its two premises.

**Not medical advice.**
