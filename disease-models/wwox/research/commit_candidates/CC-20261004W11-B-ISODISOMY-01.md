# CC-20261004W11-B-ISODISOMY-01 — homozygosity is not proof of two carriers: the isodisomy route at class level

`context_policy: SOURCE_FIRST`. **Author:** ACTOR_ID `scientist`, Scientist B of intake wave 11,
2026-10-04. **Change class: MINOR** (adds a method rule to the working model's genotype
interpretation section; narrows or reverses no `consolidated baseline` claim). **Nothing here is
medical advice.** Public edition: class level only; no wording naming the parental side of any
disomy is used, here or in the proposed text.

## 1 · Brief premise tested

The selection called uniparental isodisomy unmasking a recessive WWOX allele "a mechanism the model
may not hold". **Half right.** The research layer already holds it: PMID 39101447 (You 2024; complete
reading `FTR-20261003-39101447-01`; `PAPER 016` genotype line: canonical donor `c.172+1G>C`,
homozygous, "isodisomia inferita da LOH copy-neutral", minigene exon-2 skipping). The **working model**
holds no sentence about it. PMID 40943441 adds no WWOX case — its index patient has
whole-chromosome-16 isodisomy and **no** pathogenic recessive variant on chromosome 16 — but it
states the route at class level and cites a second WWOX instance (PMID 38407561, `c.516+1G>A`,
unread, FT-135, paywalled). Henry 2025 (PMID 40183601) shows one disomy-inherited etiology in its
cohort (Figure 3C, 0.4 %) whose gene is not named, and none of its four WWOX rows is marked that way.

## 2 · Why the model should carry it (INFERENZA)

A homozygous WWOX genotype is routinely read as "both parents carriers" and, in a consanguineous
family, as identity by descent. Isodisomy breaks that inference: a single carrier's chromosome can
supply both copies, so (a) segregation in one parent only is not a contradiction of a homozygous
call, (b) an apparently homozygous allele in a patient with large copy-neutral LOH on chromosome 16
is not evidence of consanguinity, and (c) a large LOH call should prompt the question before a
second, cryptic allele is sought. It changes nothing about the allele's function.

## 3 · Ops (provisional)

### 3.1 · `disease-models/wwox/registries/working_model_current.md`, section "Genotype interpretation rules (method)"

| field | value |
|---|---|
| op | `insert_after` (new bullet after the bullet ending with the anchor) |
| anchor (verbatim, measured unique in the file: 1 hit) | `it is a **noisy proxy for residual function** (see CLAIM 033).` |
| new | `- **Homozygosity is not proof of two carrier parents.** A recessive WWOX allele can be made homozygous by uniparental isodisomy of chromosome 16 (one canonical-donor case read in full, PMID 39101447, isodisomy inferred from copy-neutral LOH; one further donor-allele case cited and unread, PMID 38407561; the route stated at class level by PMID 40943441). A homozygous call with chromosome-16 copy-neutral LOH is not evidence of consanguinity, and segregation in one parent only does not contradict it. The route says nothing about the allele's function.` |
| class | MINOR |
| changelog line | `WM: genotype-interpretation rule added — isodisomy route (CC-20261004W11-B-ISODISOMY-01).` |

## 4 · What would change this

- **Would strengthen:** a read primary that proves isodisomy for a WWOX allele with microsatellites
  or trio SNP data (PMID 38407561 if acquired; PMID 39101447 inferred it from LOH alone).
- **Would weaken:** nothing proposed here is a frequency claim; a census showing the route is
  vanishingly rare would not falsify the rule, only its practical weight.

### LOCATOR TRIPLES FOR BLIND AUDIT

- [PMID 40943441, artefact `files/fulltext/PMID40943441_Panchenko2025_PMC.xml`] (WWOX is listed among recessive genes whose disease has been unmasked by chromosome-16 uniparental disomy. | GAN [15], and WWOX [16] within the UPD | Introduction, second paragraph)
- [PMID 40943441, artefact `files/fulltext/PMID40943441_Panchenko2025_PMC.xml`] (Isodisomy makes chromosome-16 loci identical so a recessive allele can be unmasked. | associated phenotypes may be due to unmasked mutations in recessive disease-related genes like GPT2 | Discussion, second paragraph)
- [PMID 40943441, artefact `files/fulltext/PMID40943441_Panchenko2025_PMC.xml`] (Isodisomy usually arises by monosomy rescue. | Another pathomechanism of UPD (16) is monosomy 16 rescue, where most cases are isodisomic (UPiD) | Discussion, first paragraph)
- [PMID 40943441, artefact `files/fulltext/PMID40943441_Panchenko2025_PMC.xml`] (The index patient carries no unmasked pathogenic recessive variant on chromosome 16. | No unmasked pathogenic recessive genetic variants on chromosome 16 were detected | Results 2.2.4)

---

## BATCH DISPOSITION — `BATCH_20261004_005` (2026-10-04, ACTOR_ID `scientist`, Scientist O), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED

Class re-judged **MINOR but baseline-touching** — it writes a method rule into `working_model_current.md` — so the blind locator audit was **mandatory** and ran before the propagation.

**Audit: 4 triples, 3 SUPPORTED, 1 NOT_SUPPORTED_AS_LABELLED.** The adverse verdict is a **direction error** and it was removed before landing: the candidate's triple said *«isodisomy usually arises by monosomy rescue»*, while the source says most **monosomy-rescue** cases are isodisomic — and, in the same paragraph, that **most chromosome-16 uniparental disomy arises by trisomy rescue and is heterodisomic**. The landed rule makes no frequency claim at all, and the retired direction is recorded as a prohibition on `CORPUS-STUB-184`. The auditor also confirmed what the rule rests on: *«As a consequence of UPiD, homologous loci mapping to chromosome 16 are identical»*, and that the index patient is **not** a WWOX case.

🔵 **Privacy handling, stated because the subject matter invites a failure here.** The route cannot be described without a notion of parental origin, and the landed rule describes it **at class level only**: no side of origin appears in the bullet, in the stub, in the literature record or in this disposition, and the one WWOX-direct reference's published title — which names a side — is cited by identifier and **not reproduced**. `public_release_gate.py` was re-run after this op: **PASS, 0 BLOCK**.

**Not medical advice.**
