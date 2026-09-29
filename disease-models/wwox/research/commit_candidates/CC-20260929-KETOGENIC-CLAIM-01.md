# COMMIT CANDIDATE — CC-20260929-KETOGENIC-CLAIM-01

**Candidate ID:** CC-20260929-KETOGENIC-CLAIM-01
**Status:** `PROPOSED — NOT PROPAGATED` (see the batch disposition at the end)
**Author:** ACTOR_ID `orchestrator`, 2026-09-29.
**Operator decision, verbatim (2026-09-29):** *«ok per id di claim per chetogenica»*. This answers the question `CC-20260826-CROSS-CLAIM-CENSUS-03` reserved: a dietary-intervention datum may hold a canonical claim ID.
**Discharges:** the one residue of `CC-20260826-CROSS-CLAIM-CENSUS-03` (edit 2, the ketogenic promotion). That candidate's own condition was *"the evidence boundary a promotion would need written first (n = 5, 3/5 responders, uncontrolled, unblinded, `Chong 2023`, genotype caution, «Non è parere medico»)"*. The boundary is written below, and re-reading the source changed two of its terms.

**Not medical advice.** Nothing here says whether any person should or should not start a ketogenic diet; that is a decision for a treating clinical team.

---

## 0 · The reading this rests on

- **Source:** Chong SC, Cao Y et al. 2023, *Am J Med Genet A*, PMID 36537114, DOI 10.1002/ajmg.a.63074 (`PAPER 017`). Closed access; no PMCID; no OA copy (Europe PMC and OpenAlex, 2026-09-29).
- **Surface:** eight publisher passages retrieved through Wiley Scholar Gateway on 2026-09-29, saved as `files/fulltext/PMID36537114_Chong2023_ScholarGateway_20260929.json`, sha256 `8e2f19186b843000427b53c66c755bcbdd1a0aeb1088d119b258ea9f0fb4ba9b`. The passages are the abstract, the introduction, Table 1 (genotype and epilepsy rows), the case descriptions and the discussion and conclusion paragraphs on the diet.
- **Prior state:** the only receipt, `FTR-20260726-36537114-01`, is a legacy reconstruction whose source locator is the registry record itself. Nothing on `main` could be re-verified against a byte of the paper. This reading is recorded as a new partial receipt.

## 1 · What the source says, verbatim

| # | Passage | Where |
|---|---|---|
| Q1 | *«the institution of a ketogenic diet in patients 1, 2, and 4 notably improved seizure control»* | Discussion |
| Q2 | *«It may be premature to assert the potential beneficial effects of a ketogenic diet as they need to be evaluated carefully in a larger cohort. However, these findings suggest that the implementation of a ketogenic diet may help to improve the control of epilepsy in certain patients with WOREE syndrome.»* | Discussion |
| Q3 | Table 1, *Epilepsy* row: patients 1, 2 and 4 carry *«Responded to ketogenic diet»*; patients 3 and 5 carry seizure descriptions with **no** ketogenic-diet entry | Table 1 |
| Q4 | Patient 5: *«compound heterozygous pathogenic WWOX variants: a heterozygous missense c.689A>C (p.Gln230Pro) variant … and a heterozygous deletion of exon 5»* (parental attribution omitted in this public edition) | Case description |
| Q5 | *«All WWOX variants in these five patients are predicted to be null»* | Discussion |
| Q6 | *«The institution of a ketogenic diet should be considered for the treatment of epilepsy in these patients.»* | Conclusion |

## 2 · Two corrections the reading forces

1. 🔴 **"3/5" states a denominator the source does not give.** The paper names three responders (Q1, Q3). It does **not** say how many of the five patients were placed on the diet. Table 1 records no ketogenic-diet entry for patients 3 and 5, which is an absence of a report, not a reported non-response. The working model's and the narrative view's *"seizure improvement in 3/5 WOREE patients"* therefore reads as a response rate the source cannot support. It becomes *"three of five patients are reported as responders; the number exposed is not stated"*.
2. 🔴 **The only `Q230P` carrier in the series is not among the reported responders.** Patient 5 is `p.Gln230Pro` / exon-5 deletion (Q4). The three responders carry splice-region or exon-deletion alleles on both sides (no missense). `PAPER 017`'s *"5 pazienti WOREE (tutti null/null)"* repeats the authors' prediction (Q5) that every variant, the missense included, is null. That is a prediction, not a measurement for this allele in this paper. For the reference genotype class the relevant fact is therefore negative: this series carries **no** documented ketogenic-diet response in a `Q230P` carrier, and **no** documented non-response either.

## 3 · Proposed record — `CLAIM 042`

```text
## CLAIM 042
**Title:** In one WOREE case series, three of five patients are reported to have improved seizure control after a ketogenic diet; the number of patients exposed is not stated and no Q230P carrier is among the responders
**Status:** in observation
**Type:** DATO (uncontrolled case series, clinical report) + INFERENZA (the authors' suggestion of benefit)
**Pathway:** P1 — clinical epilepsy management; P5 — metabolic context
**Genotype/model relevance:** human WOREE, five paediatric patients; the three reported responders carry splice-region (one at +5) or exon-deletion alleles on both sides, none a missense; the one Q230P carrier (compound heterozygous with an exon-5 deletion) has no ketogenic-diet entry in the source
**Transferability:** T2 — human WOREE; not demonstrated for the Q230P-bearing genotype class
**clinical relevance:** MODERATE — a low-risk-to-describe, clinically available intervention with a small, uncontrolled human signal; not a treatment recommendation
**Summary:** Chong et al. 2023 report that «the institution of a ketogenic diet in patients 1, 2, and 4 notably improved seizure control», and Table 1 marks those three patients «Responded to ketogenic diet». The authors hedge in the discussion — «It may be premature to assert the potential beneficial effects of a ketogenic diet as they need to be evaluated carefully in a larger cohort» — and conclude more strongly that it «should be considered». Earlier reports cited by the same paper describe ketogenic-diet use in WOREE «with varying degrees of success».
**Clinical meaning:** Non cambia la pratica e non è parere medico. Documents that a ketogenic diet has been used in WOREE with reported seizure improvement in some patients, which is information for discussion with a treating clinical team, not an indication.
**Evidence boundary:** n = 5; uncontrolled, unblinded, retrospective case series; no seizure-frequency measure, no timing or duration of the diet, and no definition of «responded» in the retrieved text; the denominator of patients exposed to the diet is **not stated**, so «3/5» must not be read as a response rate; responses are reported only in patients whose alleles are splice-region changes or exon deletions on both sides, and the single Q230P carrier has **no** ketogenic-diet entry — neither response nor non-response — so nothing here transfers to the Q230P-bearing genotype class; the authors' conclusion («should be considered»; «the seizures in most patients responded») is stronger than their own discussion («may be premature») and than their own count of three; the paper calls all five genotypes «predicted null» although patient 5 carries a missense allele, and patient 5 also carries a de novo likely-pathogenic *GRIA4* variant, so her seizure course is confounded; co-medication during the diet is not reported in the retrieved passages. `PREMISE_TAG`: any statement that the ketogenic diet «works» in WOREE, or in the reference genotype, rests on this series and on uncontrolled earlier reports only. `REVIVAL_TRIGGER`: a report with the number exposed, a seizure-frequency endpoint, or any documented diet exposure in a Q230P carrier.
**Source:** [[paper_registry_current#PAPER 017]] (Chong et al. 2023, PMID 36537114; publisher passages via Scholar Gateway, receipt `FTR-20260929-36537114-02`)
**Wikilinks:** [[paper_registry_current#PAPER 017]] · [[claim_registry_current#CLAIM 001]] · [[claim_registry_current#CLAIM 009]]
**Impact on Working Model:** replaces the model prose «seizure improvement in 3/5 WOREE patients» with a pointer to this claim and its denominator caveat; no BLOCCO 1 change, no therapeutic score.
```

## 4 · Other ops

- **Working model, `working_model_current.md`** (live prose): *«Ketogenic diet associated with seizure improvement in 3/5 WOREE patients (Chong 2023).»* becomes *«Ketogenic diet: three of five patients in one WOREE series are reported as responders; the number exposed is not stated, and the one Q230P carrier has no diet entry (Chong 2023; [[claim_registry_current#CLAIM 042]]).»*
- **Narrative view, `disease_model.md`:** the same sentence, the same replacement.
- **`PAPER 017` · `Note`:** append one sentence recording the two corrections of § 2, with the new receipt, and carrying the superseded «3/5» reading as history.
- **Mirror row:** the working model's claim mirror gains a row for `042`, in the table's own format.

## 5 · Locator triples for the blind audit

| # | Proposition | Quote | Anchor |
|---|---|---|---|
| T1 | Three named patients are reported to have improved seizure control on a ketogenic diet | Q1 | Discussion |
| T2 | The source does not state how many of the five patients were placed on the diet | Q3 plus absence across the retrieved passages | Table 1 and all passages |
| T3 | The only Q230P carrier is patient 5, who has no ketogenic-diet entry | Q3 + Q4 | Table 1 and case description |
| T4 | The authors' discussion is more cautious than their conclusion | Q2 and Q6 | Discussion and conclusion |
| T5 | The three responders carry splice-region or exon-deletion alleles on both sides (no missense) | Table 1 cDNA row | Table 1 |

**Not medical advice.**

## 6 · Blind locator audit — 2026-09-29

Auditor given the five triples and the source artefact only. **T1–T5 SUPPORTED.** Two wording repairs applied above from its notes: *splice-site* → *splice-region* (patient 1 carries a `+5` change, not a canonical site); and the evidence boundary now records that the conclusion (*«most patients responded»*, *«should be considered»*) overshoots the paper's own count and discussion, that the paper calls a missense allele *predicted null*, and that patient 5 carries a de novo *GRIA4* variant confounding her seizure course. The retrieval is partial: case descriptions for patients 1–4 are not among the passages, so diet details there, if any, are unverifiable here.

---

## BATCH DISPOSITION — `BATCH_20260929_001` (2026-09-29, ACTOR_ID `orchestrator`), append-only

**Nothing above this line was rewritten.** Operator decision, verbatim: *«ok per id di claim per chetogenica»*.

**Verdict:** PROPAGATED

`CLAIM 042` appended with the evidence boundary as repaired by the blind audit; the DATA line of the working model and `disease_model.md` corrected; `PAPER 017`'s note corrected in place, carrying the superseded «3/5» reading; mirror row `042` added. Receipt `FTR-20260929-36537114-02`.

**Not medical advice.**
