# CC-20261003W5-C-TRANSGENE-NULL-IMMUNOSUPPRESSION-01 — four CSF-route programmes converge on triple immunosuppression when the recipient is predicted null for the transgene product

`context_policy: SOURCE_FIRST`
**Date:** 2026-10-03 · **Author:** Scientist C, intake wave 5 · **Change class:** MINOR
**Target records:** `disease-models/wwox/research/discovery_ledger_current.md` (append one lead)

> **MINOR.** No canonical claim is edited and nothing is promoted. This candidate records a
> transferable pattern in human clinical practice and states the exact limit of its transfer to a
> WWOX genotype class.
>
> **Nothing here is medical advice.** Therapeutic output supports discussion with a treating clinical
> team and never substitutes for one.

---

## 1 · The pattern

Across the human CSF-route programmes reachable in this wave, the immunosuppression regimen tracks
one variable: **whether the recipient is predicted to have any endogenous expression of the protein
the vector will express.**

| Programme | Regimen | Rationale as the sources state it | Source |
|---|---|---|---|
| Giant axonal neuropathy | prednisolone + sirolimus + tacrolimus | cohort included CRIM-negative individuals "at higher risk of developing an immune response to transgene-expressed gigaxonin protein" | PMID 42134074 |
| Ceroid lipofuscinosis type 7 | prednisone + sirolimus, tacrolimus in some cases | "Modelled off the GAN clinical trial" | PMID 42134074 |
| Spastic paraplegia type 50 | prednisolone + sirolimus + tacrolimus | "to mitigate immune responses and promote tolerance to AP4M1, given the predicted absence of endogenous expression for this patient" | PMID 42134074 |
| Mucopolysaccharidosis I (intracisternal) | methylprednisolone, prednisone taper, tacrolimus to 32 weeks, sirolimus to 48 weeks | recipient carried high-titre anti-enzyme antibody from prior enzyme replacement | PMID 41966056 |
| Spinal muscular atrophy | **prednisone alone**, ~1 mg/kg/day for ~2 months | endogenous SMN protein is present via the paralogous backup gene | PMID 42134074 |

Four programmes with a predicted-null or pre-sensitised recipient use three agents. The one
programme whose recipients retain endogenous protein uses one.

## 2 · Two independent lines of support that the transgene product itself can be the toxic agent

1. **A large-animal event.** PMID 42134074's index table reports, for intrathecal AAV9 carrying GFP
   in dogs: *"Encephalitis associated with a T-cell response to the transgene product."* The injury
   is attributed to what the vector expressed, not to the capsid.
2. **A primate dissection of the same point.** PMID 41257285 found that empty capsids and a
   promoterless genome produced neither the liver nor the DRG toxicity that the full expressing
   vector produced at comparable capsid dose — so a productive cassette is necessary for the organ
   toxicity of concern.

Together these make "what is expressed, and whether the recipient's immune system has seen it
before" a load-bearing design variable rather than a formality.

## 3 · The transfer to a WWOX-DEE genotype class — and exactly where it stops

**The inference.** A recipient with a **biallelic loss-of-function WWOX genotype** is, by
construction, in the predicted-null class: no endogenous WWOX protein has been presented to the
immune system, so a WWOX restoration cassette would express a protein that is self by sequence but
novel to that individual's immune system — the CRIM-negative-analogous situation the GAN, CLN7 and
SPG50 protocols were designed around. **The relevant precedent for such a programme is therefore
the triple regimen, not the single-steroid regimen.**

**Where this stops, stated exactly, item by item:**

1. **It is an inference from genotype class to immunological class.** It is **not measured for
   WWOX**. No source in this wave mentions WWOX; all six are earned nulls for the gene.
2. **No controlled comparison exists.** Not one of these programmes compared triple against
   single-agent prophylaxis. The pattern is a correlation across programmes that differ in disease,
   gene, cargo, dose, age and era.
3. **It does not transfer across WWOX allele classes.** P47T, Q230P, G372R, A141T and P252A are not
   interchangeable with one another or with a null. **A missense allele producing a stable but
   non-functional protein is not predicted-null**, because that protein has been presented to the
   immune system; such a recipient does not inherit this precedent. A heterozygote is neither a
   demonstrated negative nor a demonstrated positive for anything here.
4. **The regimens themselves are not interchangeable.** They differ in agent, dose, target trough
   and duration — 48 weeks in the MPS I case, approximately 2 months of steroid in SMA.
5. **Immunosuppression carries its own burden, and the sources say so.** In the MPS I case, of 23
   recorded adverse events, 17 occurred in the first year and **16 of those 17 were assessed as
   possibly related to the immunosuppression** rather than to the vector. Choosing the heavier
   regimen moves the adverse-event burden rather than removing it.
6. **A mechanistic caveat from a third source.** PMID 41257285 identifies the transcriptional
   response as interferon / JAK-STAT rather than NF-κB and offers this as a reason glucocorticoids
   may be less protective than assumed. If correct, the steroid component of any of these regimens
   is the weakest part. This is the authors' hypothesis — no immunosuppressed arm was run in that
   study — and it is recorded as a hypothesis.
7. **Durability, not only toxicity, is at stake.** In the MPS I case, CSF transgene product peaked
   at 35 weeks and **declined once immunosuppression was weaned**, settling at 6.8% of control. The
   immune component governs how long expression lasts, not merely whether the procedure is tolerated.
   ⚠️ That observation is for a **secreted** enzyme in a recipient with pre-existing anti-enzyme
   antibody; WWOX protein is intracellular and the antibody mechanism is not the same. What may
   transfer is loss of transduced cells to a cellular response, which this source does not measure.

## 3b · A convergence with wave 4 that sharpens which agent matters

`CC-20261003w4-C-DRG-CONTRADICTION-01` found that a **tacrolimus**-containing primate regimen reduced
DRG pathology across three cargos while **prednisolone**, and **rituximab + everolimus** under
complete B-cell depletion, did not. Its most parsimonious explanation was drug class — offered,
as that candidate notes, by the party whose regimen worked.

Every predicted-null regimen tabulated in §1 above **contains tacrolimus** (the CLN7 programme used
it "in some cases"). The programme that used a steroid alone is the one whose recipients retain
endogenous protein. So the human practice tabulated here and the primate mitigation result in
wave 4 point at the same agent class from opposite ends of the evidence.

**Two cautions against over-reading this.** First, the human regimens were chosen to prevent
**anti-transgene** immune responses, not to protect the DRG; their DRG outcomes are incidental.
Second, **mTOR inhibition does not separate the two results** — everolimus sat in wave 4's failed
arm while sirolimus sits in every one of these human regimens — so if drug class is the explanation,
the active element is calcineurin inhibition and the sirolimus component is doing something else or
nothing. That is a prediction, not a finding, and §5's falsifying experiment is the way to test it.

## 4 · The nearest human disease precedent, and its limit

**CLN7** — a paediatric, neurodegenerative, seizure-bearing disorder, dosed intrathecally with
scAAV9 at 5 × 10¹⁴–1 × 10¹⁵ vg in patients aged 1–18 years, under triple immunosuppression, with DRG
assessed by MRI and nerve conduction studies, followed more than two years, reporting "relative
stability in their seizures" while the disease nonetheless progressed in all subjects.

In route, capsid, age band, immunosuppression, DRG monitoring and phenotype class this is the closest
match in the wave to a hypothetical WWOX-DEE programme. **The limits:** MFSD8 is not WWOX; n = 4;
the efficacy comparison is uncontrolled against historical natural history; and the disease still
progressed.

## 5 · Op — discovery_ledger_current.md

`op: APPEND` one lead at the end of the lead list of
`disease-models/wwox/research/discovery_ledger_current.md`. No `old` text; this is an append.

```
### DIS-xxx (provisional) — Immunosuppression for a CSF-route gene-replacement dose is chosen by the recipient's predicted endogenous expression, not by the route

**Tag:** IPOTESI (transfer from adjacent genes to a WWOX genotype class)
**Status:** open
**Created:** 2026-10-03 · intake wave 5, Scientist C (group C)
**Causal statement:** Across human CSF-route AAV9 programmes, the prophylactic immunosuppression
regimen tracks whether the recipient is predicted to express any endogenous copy of the transgene
product. Programmes whose recipients are predicted null, or already sensitised, use a steroid plus
sirolimus plus tacrolimus; the one programme whose recipients retain endogenous protein uses a
steroid alone. A biallelic loss-of-function WWOX genotype falls in the predicted-null class by
construction, so the triple regimen is the applicable precedent for a WWOX restoration cassette.
**Reasoning chain:**
1. Three intrathecal programmes in different diseases adopt prednisolone/prednisone + sirolimus +
   tacrolimus, two of them stating the predicted absence of endogenous transgene product as the
   reason; one intracisternal programme in a pre-sensitised recipient uses the same three agents for
   48 weeks.
2. The approved intrathecal programme whose recipients retain endogenous protein via a paralogous
   gene uses prednisone alone for about two months.
3. A large-animal study reports encephalitis attributed to a T-cell response to the transgene
   product, not to the capsid.
4. A primate study shows the organ toxicity of concern requires a transcriptionally productive
   cassette: neither empty capsids nor a promoterless genome reproduced it.
**Counter-evidence / what would refute this lead:** no controlled comparison of triple versus
single-agent prophylaxis exists in any of these programmes; the pattern is correlational across
diseases, cargoes, doses, ages and eras. Immunosuppression carries its own burden - in the
intracisternal case, 16 of the 17 first-year adverse events were attributed to the immunosuppression
rather than the vector. And a third source argues the relevant pathway is interferon/JAK-STAT rather
than NF-kappa-B, which would make the steroid component the weakest part of all these regimens.
**Falsifying experiment:** a CRIM-negative cohort randomised to triple versus steroid-alone
prophylaxis around a fixed CSF-route dose, with anti-transgene ELISpot, transgene product
persistence and adverse-event burden as endpoints. The lead predicts fewer anti-transgene responses
and better persistence on the triple arm, at the cost of a higher immunosuppression-attributable
adverse-event count.
**Transfer limits (binding):** not measured for WWOX - all six wave-5 group-C sources are earned
nulls for the gene. Does NOT transfer to a WWOX missense allele that produces a stable but
non-functional protein, which is not predicted-null; P47T, Q230P, G372R, A141T and P252A are not
interchangeable with each other or with a null, and a heterozygote is neither a demonstrated
negative nor a positive. The durability observation it rests on was made for a secreted enzyme in a
recipient with pre-existing anti-enzyme antibody; WWOX protein is intracellular and that antibody
mechanism does not carry over.
**Links:** `research/intake_wave_20261003w5_C.md` §3; dossiers `PMID42134074.md` §5,
`PMID41966056.md` §3, `PMID41257285.md` §2.
**Not medical advice.**
```

## 6 · LOCATOR TRIPLES FOR BLIND AUDIT

```
(One intrathecal programme chose a three-agent immunosuppression regimen because the recipient was predicted to have no endogenous expression of the transgene product | An immunosuppression regimen modelled from the GAN trial (prednisolone, sirolimus, and tacrolimus) was used to mitigate immune responses and promote tolerance to AP4M1, given the predicted absence of endogenous expression for this patient. | files/fulltext/PMID42134074_Kagiava2026_PMC.xml — Clinical applications, 'Spastic paraplegia type 50 (SPG50)')

(The programme those regimens were modelled on enrolled participants predicted to have no residual endogenous protein and stated anti-transgene immune risk as the reason | The cohort included individuals predicted to have no residual gigaxonin expression (CRIM-negative) and thus at higher risk of developing an immune response to transgene-expressed gigaxonin protein, as well as participants who were AAV9-seropositive (neutralising antibody titre ≥1:5) or seronegative at baseline. | files/fulltext/PMID42134074_Kagiava2026_PMC.xml — Clinical applications, 'Giant axonal neuropathy (GAN)')

(A third intrathecal programme in a paediatric neurodegenerative disorder adopted the same three-agent approach and found no dorsal-root-ganglion signal on imaging and nerve conduction | Notably there were no signs of DRG toxicity when assessed by MRI and peripheral nerve conduction studies. | files/fulltext/PMID42134074_Kagiava2026_PMC.xml — Clinical applications, 'Ceroid lipofuscinosis type 7 (CLN7)')

(The approved intrathecal programme whose recipients retain endogenous protein via a paralogous gene used a single steroid for about two months | Prednisone prophylaxis 1 mg/kg/day for approximately 2 months was used, as with the earlier IV studies. | files/fulltext/PMID42134074_Kagiava2026_PMC.xml — Clinical applications, 'Spinal muscular atrophy (SMA)')

(The human intracisternal programme used three agents around a single dose and continued them for forty-eight weeks | Immunosuppression (for full regimen, see Supplemental Text, Protocol) was continued for a total of 48 weeks after RGX-111 dosing. | files/fulltext/PMID41966056_Wang2026_PMC.xml — Materials and methods, 'Human subjects')

(In that programme the investigators attributed most first-year adverse events to the immunosuppression rather than to the vector | In total, 23 adverse events have been recorded to date (see Table S3); 17 occurred in the first year following dosing, and 16 of those were assessed to be possibly related to immunosuppression. | files/fulltext/PMID41966056_Wang2026_PMC.xml — Results, 'Adverse events')

(In that programme transgene product in cerebrospinal fluid declined once immunosuppression was weaned | (A) CSF IDUA enzyme levels measured over 290 weeks suggest rapid-onset IDUA transgene expression (week 8), which peaked at 35 weeks and subsequently declined after weaning of immunosuppression began (blue arrow). | files/fulltext/PMID41966056_Wang2026_PMC.xml — Figure 1 caption, panel A)

(The organ toxicity of concern requires a transcriptionally productive cassette rather than capsid exposure alone | Hepatic and DRG toxicities were only detected after administration of full AAV9 viral particles, but not empty capsids or Promoterless test articles. | files/fulltext/PMID41257285_Aihara2025_PMC.xml — Results, 'In-life summary and organ toxicities')

(The pathway identified in that primate study signals through JAK/STAT rather than NF-kappa-B, which the authors offer as a reason glucocorticoid prophylaxis may be insufficient | This could provide some explanation as to why glucocorticoids are not always as potent as expected in preventing AAV-driven toxicity. | files/fulltext/PMID41257285_Aihara2025_PMC.xml — Discussion, interferon pathway paragraph)

(No immunosuppression was given in that primate study, so the modifiability of the immune component is untested in it | However, it is important to note that unlike patients who receive glucocorticoids, which are potent nuclear factor (NF)-κB inhibitors, no immunosuppressive regimen was provided to animals included in studies A or B. | files/fulltext/PMID41257285_Aihara2025_PMC.xml — Discussion, immunosuppression paragraph)
```

**Artefacts confirmed on disk before writing these triples:**
`files/fulltext/PMID42134074_Kagiava2026_PMC.xml`,
`files/fulltext/PMID41966056_Wang2026_PMC.xml`,
`files/fulltext/PMID41257285_Aihara2025_PMC.xml`. Digests are recorded in full in the corresponding
deep-dive manifests, each of which passes `deepdive_manifest.py --pmid N --verify-artifacts`.

> Note for the auditor: triple 4 quotes a sentence about prednisone prophylaxis in the SMA
> programme. Please check in particular whether the source supports the *contrast* the candidate
> draws between that programme and the three-agent programmes, or only the bare fact of the
> prednisone regimen.

---

## BATCH DISPOSITION — `BATCH_20261003_004` (2026-10-03, ACTOR_ID `scientist`, Scientist I), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED — **MERGED into `RL-GT-002`**, not written as a record of its own. (The closing vocabulary `growth_anchors.py` reads is `PROPAGATED` / `INTEGRATED` / `SUPERSEDED` / `CLOSED` / `NOT INTEGRATED`; `MERGED` alone is not in it and would leave this candidate counted as open, so the verdict names both.)

This candidate and `CC-20261003W5-A-TRANSGENE-IMMUNITY-01` state the same finding (a recipient predicted to express no endogenous transgene product is given the intensified regimen, and that class is where a biallelic null sits) from **disjoint** source sets. The batch wrote one record carrying both, with this candidate's reasoning chain, counter-evidence, falsifying experiment and **binding transfer limits** preserved inside it. Its op named `discovery_ledger_current.md` with a provisional `DIS-xxx` id; the merged home is the research-line record, which is where the two source sets can be read together.

**Three integrator amendments (blind audit).** (1) In the CLN7 programme the review's own words are *«prednisone, sirolimus, and in some cases tacrolimus»* — the third agent is not universal there. (2) The *«48 weeks»* of the intracisternal programme is the regimen total, not each agent's duration (sirolimus 48 weeks, prednisone about 8, tacrolimus 24). (3) The 16-of-17 adverse-event attribution is *«possibly related to immunosuppression»* in a single patient, with several events also recorded as possibly related to study treatment — not an exclusive attribution against the vector.

**Not medical advice.**
