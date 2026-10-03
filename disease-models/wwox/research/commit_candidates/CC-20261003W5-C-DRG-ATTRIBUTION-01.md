# CC-20261003W5-C-DRG-ATTRIBUTION-01 — the contested DRG question: a concurrent-control incidence is missing from most of the literature that reports it

`context_policy: SOURCE_FIRST`
**Date:** 2026-10-03 · **Author:** Scientist C, intake wave 5 · **Change class:** MINOR
**Target records:** `disease-models/wwox/research/discovery_ledger_current.md` (append one lead)

> **MINOR, and deliberately so.** This candidate narrows nothing in the canonical registry, because
> no consolidated baseline claim in this repository rests on the DRG-toxicity question. It records
> what the wave-5 sources add to a question waves 3–4 left contested, and names the procedural
> correction they license. If a later pass promotes a DRG-safety claim to `consolidated baseline`,
> **that** pass is MAJOR and must carry these triples to a blind audit first.
>
> **Nothing here is medical advice.**

---

## 1 · The state of the question before this wave

Waves 3–4 built a restoration spec and a window status in which dorsal-root-ganglion toxicity after
CSF-route AAV9 was contested: reported consistently in primate toxicology, but with the severity and
the attribution unsettled.

## 2 · What the four primary sources and two reviews of group C actually show

### 2.1 The lesion is not driven by pre-existing immunity

PMID 41210171's own Figure 6 caption says the DRG and nerve-root degeneration occurred *"across
scAAV9-CBA-mCherry-administered groups **without impact of pre-existing AAV9-Ab titers**"*. The
immunity-responsive findings in that study are elsewhere: systemic interferon response, splenic
T-cell response, CSF antibody kinetics, and — weakly — meningeal infiltrate severity.

### 2.2 The lesion does require a transcriptionally productive cassette

PMID 41257285 is the only study in the group with the arms that can test this:

> "Hepatic and DRG toxicities were only detected after administration of full AAV9 viral particles,
> but not empty capsids or Promoterless test articles."

Empty capsid at 2.73 × 10¹³ produced neither lesion. A full genome with a scrambled promoter
produced neither. **Capsid load alone is insufficient.**

### 2.3 But expression *magnitude* does not select the injured tissue

The same paper reports vector-genome load highest in liver and DRG — the injured tissues — while
transgene transcript was highest in heart and skeletal muscle, which had no consistent pathology,
and concludes that "the amount of transgene product itself is not directly predictive of the
observed toxicities".

**This contradicts the mechanistic position of PMID 42134074**, which attributes DRG toxicity
"mostly … to supraphysiological gene expression levels with strong ubiquitous promoters". The two
agree a promoter is necessary and disagree on whether its strength is the graded driver.
**The tension is recorded, not resolved.** The shared mitigation — a weaker or cell-restricted
promoter — survives either reading, which is why it is the one design recommendation this candidate
carries forward.

### 2.4 The attribution problem — the finding of this candidate

| Study | DRG lesion in treated animals | DRG lesion in concurrent controls | Incidence reported? |
|---|---|---|---|
| PMID 41948127 | 40% of animals, subclinical minimal-to-mild | **2 of 4 saline animals** | yes, in the body |
| PMID 41210171 | listed in prose; one representative sacral photomicrograph | **not reported for DRG at all** | **no — nowhere** |
| PMID 41257285 | single-cell necrosis and neuroinflammatory change | not reported | no — and the histopathology is cited to a prior report, not measured here |

For PMID 41210171 this was established exhaustively, not by assumption:

- the article contains **zero** `<table-wrap>` elements;
- its only histopathology summary, Figure 6C, tabulates **brain only** (and shows meningeal
  mononuclear infiltrate in **2 of 3 vehicle animals**, a lesion the running text nonetheless classes
  among "test-article–related microscopic findings");
- its Supplementary Document S1 was **fetched and read as a derived text layer**; it contains
  Tables S1–S3, all antibody titres, and no pathology;
- yet its Methods confirm DRG at cervical, thoracic, lumbar and sacral levels were sectioned and
  H&E-stained. **The data were generated and are not reported.**

### 2.5 The human record does not scale with dose

From PMID 42134074: two sensory cases suggestive of DRG toxicity at 1.2 × 10¹⁴ vg intrathecally,
improving with symptomatic treatment; one adult with MRI and electrophysiological signs plus pain,
improving but not resolving. Against that, **no** DRG signal on MRI and nerve conduction studies at
5 × 10¹⁴–1 × 10¹⁵ vg (CLN7, n = 4) and at 1 × 10¹⁵ vg (SPG50, n = 1). And primate DRG toxicity is
tabulated at 1.2 × 10¹³–6 × 10¹³ vg — *below* the human dose.

### 2.6 And the finding has already stopped a trial

Primate DRG findings prompted a regulatory hold on enrolment in a human paediatric intrathecal
programme, which was then terminated before its high-dose cohort filled. **Whatever the evidential
quality, the regulatory weight of this finding is established.**

## 3 · The proposed lead

`op: APPEND` one lead at the end of the lead list of
`disease-models/wwox/research/discovery_ledger_current.md`. No `old` text; this is an append.

```
### DIS-xxx (provisional) — A primate DRG finding without a concurrent-control incidence is not an attribution

**Tag:** INFERENZA
**Status:** open
**Created:** 2026-10-03 · intake wave 5, Scientist C (group C)
**Causal statement:** Minimal-to-mild dorsal-root-ganglion lesions occur in vehicle-dosed cynomolgus
macaques at a rate high enough to account for a substantial part of what is reported as AAV9-related
DRG toxicity. Where a concurrent-control incidence is reported, it is of the same order as the
treated incidence; where it is not reported — which is the common case — the attribution to the
vector is not established by the paper making it.
**Reasoning chain:**
1. In one NHP study that reports both arms, subclinical minimal-to-mild DRG lesions appeared in 40%
   of animals overall and in two of four saline-dosed controls.
2. In a second, independent NHP study, the only quantified histopathology (brain) shows meningeal
   mononuclear infiltrate in two of three vehicle animals, while the running text classes that lesion
   among test-article-related findings.
3. That same study reports DRG lesions with no incidence, no severity distribution and no control
   comparison anywhere in the article or its supplement, although its methods confirm DRG at four
   spinal levels were sectioned and stained.
4. The lesion is explicitly stated by one of these studies to occur independently of pre-existing
   anti-capsid antibody titre, so it is not the immune-driven component.
5. The human record does not scale monotonically with dose: signals at 1.2e14 vg intrathecally,
   none detected by MRI and nerve conduction at 5e14-1e15 vg in two separate programmes.
**Counter-evidence:** primate DRG findings have real regulatory weight - they produced a hold on
enrolment in a human paediatric intrathecal programme that was then terminated early. Human DRG
toxicity has appeared, with imaging and electrophysiological correlates in at least one adult.
Background lesions in controls do not mean the vector adds nothing; they mean the increment has not
been measured in most reports. n = 4 and n = 3 control arms cannot exclude a modest increment.
**Falsifying experiment:** an NHP study powered to report DRG incidence and severity **by arm**,
with a concurrent vehicle group, at two or more dose levels, with the expression cassette varied
(full vector / weak or cell-restricted promoter / promoterless) and functional electrophysiology at
baseline and terminal. The lead predicts a control incidence of the same order as the low-dose
treated incidence; a clean treated-only lesion with a dose gradient refutes it.
**Operational consequence (proposed, not a gate):** a DRG-safety statement entering this repository
from a primate source must record the concurrent-control incidence, or record that the source does
not report one. The second is a legitimate and common answer.
**Transfer limit to WWOX:** none of the six sources mentions WWOX. A WWOX restoration cassette is a
promoter-driven protein transgene and therefore sits on the toxic side of the capsid-versus-
expression line established above; the knockdown cargo whose safety conclusion is most reassuring in
this group is a U6-driven small RNA and does not stand proxy for it.
**Links:** `research/intake_wave_20261003w5_C.md` §4; dossiers `PMID41210171.md` §5,
`PMID41948127.md` §2, `PMID41257285.md` §2, `PMID42134074.md` §2.
**Not medical advice.**
```

## 4 · What this candidate explicitly does NOT assert

- It does **not** assert that intrathecal AAV9 is safe for the DRG.
- It does **not** assert that the primate findings are artefactual — only that the increment over
  control is unmeasured in most reports.
- It does **not** promote any statement to `consolidated baseline`, and no existing canonical claim
  is edited.
- It does **not** transfer the reassuring conclusion of PMID 41948127 to a WWOX cassette; §3's
  transfer limit forbids it explicitly.

## 5 · LOCATOR TRIPLES FOR BLIND AUDIT

```
(Dorsal-root-ganglion lesions were present in concurrent saline-dosed control animals in this primate study | Forty percent of animals showed subclinical, minimal-to-mild lesions in the dorsal root ganglia, which were also found in two saline-treated animals, suggesting these were unrelated to test article. | files/fulltext/PMID41948127_Stavrou2026_PMC.xml — Results, 'IT of AAV9.U6.miR871 shows a strong safety profile in NHPs')

(The figure caption of the same study, read alone, denies that treated animals showed dorsal-root-ganglion abnormality | (A) H&E staining of representative dorsal root ganglia (DRG) from miR871-treated animals show no significant histological abnormalities compared to control. | files/fulltext/PMID41948127_Stavrou2026_PMC.xml — Figure 5 caption, panel A)

(The second primate study reports dorsal-root-ganglion pathology in prose, keyed to a single representative photomicrograph, without an incidence or severity count | These histopathology findings were mostly minimal to slight in severity with high individual variabilities and included mononuclear cell infiltrate, neuronal degeneration, axonal degeneration, and gliosis in the brain, intrathecal injection site, spinal cord, cauda equina/spinal nerve roots, and/or DRG (Figure 6A). | files/fulltext/PMID41210171_Vono2025_PMC.xml — Results, 'Clinical evaluations and pathology assessments over 4 weeks excluded major safety concerns')

(That study sectioned and stained dorsal root ganglia at four spinal levels, so the unreported data were generated | Paraffin-embedded tissues (brain, spinal cord [cervical, thoracic, and lumbar], intrathecal injection site, cauda equina/nerve root, DRG [cervical, thoracic, lumbar, and sacral], liver, and heart) were routinely processed, sectioned, and stained with hematoxylin and eosin (H&E). | files/fulltext/PMID41210171_Vono2025_PMC.xml — Materials and methods, 'Light microscopy evaluation (histopathology)')

(The dorsal-root-ganglion pathology in that study occurred independently of pre-existing anti-capsid antibody titre | Representative photomicrograph of scAAV9-CBA-mCherry-related findings observed in animals across scAAV9-CBA-mCherry-administered groups without impact of pre-existing AAV9-Ab titers (A). | files/fulltext/PMID41210171_Vono2025_PMC.xml — Figure 6 caption, panel A)

(Liver and dorsal-root-ganglion toxicity required a transcriptionally productive vector and was not produced by empty capsids or by a genome without a working promoter | Hepatic and DRG toxicities were only detected after administration of full AAV9 viral particles, but not empty capsids or Promoterless test articles. | files/fulltext/PMID41257285_Aihara2025_PMC.xml — Results, 'In-life summary and organ toxicities')

(In the same study the magnitude of transgene expression did not predict which tissue was injured | This discrepancy between vector genome biodistribution and transgene transcript level suggests that while both the capsid and an active payload are necessary to cause tissue pathology (liver and DRGs), the amount of transgene product itself is not directly predictive of the observed toxicities (even when expressing a foreign protein such as GFP). | files/fulltext/PMID41257285_Aihara2025_PMC.xml — Results, 'In-life summary and organ toxicities', closing sentence)

(A review of the same field attributes the toxicity to expression level under strong ubiquitous promoters, which is the position the preceding quote is in tension with | One of the main concerns that have to be addressed in future studies is the DRG toxicity mostly related to supraphysiological gene expression levels with strong ubiquitous promoters. | files/fulltext/PMID42134074_Kagiava2026_PMC.xml — Outstanding questions)

(Primate dorsal-root-ganglion findings produced a regulatory hold on enrolment in a human paediatric intrathecal programme | Concerns for DRG toxicity identified in NHPs by other investigators81 prompted the FDA to issue a hold on further enrolment. | files/fulltext/PMID42134074_Kagiava2026_PMC.xml — Clinical applications, 'Spinal muscular atrophy (SMA)')

(At the highest human intrathecal doses reported, dorsal-root-ganglion integrity was assessed by imaging and nerve conduction and no signal was found | Notably there were no signs of DRG toxicity when assessed by MRI and peripheral nerve conduction studies. | files/fulltext/PMID42134074_Kagiava2026_PMC.xml — Clinical applications, 'Ceroid lipofuscinosis type 7 (CLN7)')

(The same negative was obtained clinically and electrophysiologically in a separate single-patient programme | There was no clinical or electrophysiologic evidence of DRG toxicity: no neuropathic pain, and normal sensory exams and nerve conduction studies. | files/fulltext/PMID42134074_Kagiava2026_PMC.xml — Clinical applications, 'Spastic paraplegia type 50 (SPG50)')

(In the human single-patient intracisternal report, dorsal-root-ganglion function was not measured at all | Although no formal nerve conduction studies were performed, due to the protocol being a treatment investigational new drug (IND), the subject did not complain of paresthesias and did not demonstrate abnormal deep tendon reflexes, suggesting there was no clinically significant dorsal root ganglion (DRG) toxicity. | files/fulltext/PMID41966056_Wang2026_PMC.xml — Discussion, DRG paragraph)
```

**Artefacts confirmed on disk before writing these triples:** all four JATS XML files named above,
plus `files/figure_renders/sciC_w5/PMID41948127_fig5.jpg` and
`files/figure_renders/sciC_w5/PMID41210171_fig6.jpg`; digests are recorded in full in the
corresponding deep-dive manifests, each of which passes
`deepdive_manifest.py --pmid N --verify-artifacts`.
