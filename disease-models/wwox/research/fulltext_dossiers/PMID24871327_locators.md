# PMID 24871327 — Iatan et al. 2014, *Circ Cardiovasc Genet* 7:491–504

**The WWOX Gene Modulates HDL and Lipid Metabolism** · DOI 10.1161/CIRCGENETICS.113.000248 ·
PMCID PMC4315188 (author manuscript, NIHMS626914)

Complete full-text read of 2026-08-10, opened from [[full_text_queue_current#FT-039]]. The
queue asked one question and this record answers it: PMID 33255508 calls this paper *strong
evidence* for the first leg of the bridge `WWOX → lipid homeostasis → myelin`, and LEGEND had
never opened it. What the primary supports, and what it does not, is below.

## Why this paper was next

It was the only crossing of two lists: papers with a **priority declared in the queue**, and
papers with a **structured surface already local**. Twenty-two local XML/HTML full texts have
no complete read; exactly one of them, this one, is also ranked. That is a finding about the
queue, recorded at the end.

## Surfaces and artifacts

| artifact | kind | sha256 | note |
|---|---|---|---|
| `files/fulltext/PMID24871327_Iatan2014_PMC.html` | `article_text` | `b3a7c087c9d45f13919338e658f248fe9483643c97f2cea479586a3133ff4562` | PMC HTML. Screened clean; body 79 577 chars, abstract 2 043 chars, cleanly separated |
| `files/fulltext/figures/PMID24871327/nihms626914f1a.jpg` | `figure` | `3215f9d4206fead25127326054bc4ef9e5a14fb2aa0d26907ffa42b5b05af777` | Fig. 1A pedigree, family 1 |
| `…f1b.jpg` | `figure` | `e1ab81a487bdc539c06cc6a229b28362ecb1a71da120c0e1dddad283f64132f5` | Fig. 1B pedigree, family 2 |
| `…f2.jpg` | `figure` | `d309e3d03018c510e3489773cb47e8bdc1a196c312e8b590555b358eaeede5d3` | Fig. 2 IPA functions/pathways |
| `…f3.jpg` | `figure` | `205d21c0da70ce4afac4c50c698d9544e44bf8711339c88922dc3a962edd4c63` | Fig. 3 lipid-gene heatmaps |
| `…f4.jpg` | `figure` | `9824297d9255a0f05cb2d1474b36286c2d487cf27499359044d304cba2c6248f` | Fig. 4 `Wwox^hep−/−` |
| `…f5.jpg` | `figure` | `f53566df132ad65541292de8b2231c94cc02b7a35103de4afacd78fb2f1fee80` | Fig. 5 `Wwox^−/−` |

**No PDF was used and none is needed.** The paper has a PMC HTML surface, so rule 5d's
preference applies without exception; the text layer of a PDF never entered this reading.

### Resolution ceiling, measured before rendering

Figures were fetched at their maximum PMC resolution and the ceiling computed **before**
inspecting anything, so that no panel is read at a magnification the pixels do not support.
At *Circ Cardiovasc Genet*'s double-column width (~7.0 in; ~5.0 in for the portrait 1B):

| figure | pixels | effective ppi |
|---|---|---|
| f1a · f2 · f4 · f5 | 1050 × … | **150** |
| f3 | 1043 × 1050 | **149** |
| f1b (portrait) | 713 × 1050 | **143** |

≈150 ppi is the ceiling. Dense panels were therefore read by **cropping and enlarging**
(LANCZOS ×3) rather than by re-rendering larger, which would have invented detail. Every
panel-level finding below was confirmed on an enlarged crop, not on the full-page view.

### Supplementary: unavailable, cascade documented

`NIHMS626914-supplement-Supplemental_Material.pdf` (1.4 MB) is **not retrievable**. This is
not a "we did not find it": five routes were tried, and the reason is structural — the paper
is an NIH author manuscript that is *not* in the open-access subset.

| route | result |
|---|---|
| `pmc…/articles/instance/4315188/bin/<file>.pdf` | HTTP 200 serving a JS "Preparing to download" interstitial, not the PDF |
| same, with cookie jar + referer, two-step | same interstitial |
| `pmc…/articles/PMC4315188/bin/<file>.pdf` | 404 |
| Europe PMC `…/PMC4315188/supplementaryFiles` | `Article with id PMC4315188 is not open access one` |
| PMC OA service `oa.fcgi?id=PMC4315188` | `error code="idIsNotOpenAccess"` |

**What this costs, stated rather than glossed.** Suppl. Figure 1 holds the serum lipid
measurements — including the `P=0.0025` triglyceride result in older females that the whole
sex-specific story starts from; Suppl. Tables 2A/2B hold the 64 and 56 lipid genes; Suppl.
Figure 4 holds the WGCNA module correlations. Those are read here **only as the running text
reports them**, and no proposition below rests on a supplementary value alone.

## Coverage map

| section | status |
|---|---|
| abstract · introduction · methods · results · discussion | `read` |
| Table 1, Table 2 | `read` (extracted as grids from the HTML) |
| Figures 1A, 1B, 2, 3, 4, 5 | `read` — as images, at the ceiling above, with crops |
| supplementary (1 PDF: Suppl. Figs 1–4, Suppl. Tables 1–3) | `unavailable` — cascade above |
| references | `read` (enumerated; multi-hop not performed in this session) |

## Verbatim locators

Sixteen text/table locators, all verified against the declared artifact before being written
here, none of them anchorable to the abstract. Five figure locators are attestations of what
a panel shows — pixels cannot be quote-matched, and they are marked as such.

### The result the queue asked for

**1.** *The liver-specific knockout does not reproduce the HDL phenotype.*
> "sole deletion of Wwox in hepatocytes did not result in significant differences in HDL-C plasma concentrations in mice of both genders"

`surface: body` · Results, "Validation of gene expression changes…", closing paragraph.

**2.** *The whole-body knockout does.*
> "HPLC serum characterization revealed a marked reduction in HDL-C (Figure 5A), concomitant with a significant decrease in circulating ApoA-I levels"

`surface: body` · Results, "Impaired HDL biogenesis in Wwox null mice".

**3.** *The authors' own first explanation for the gap is incomplete knockdown, not biology.*
> "Wwox levels were only reduced by 2.85 fold in female and 2.34 fold in male Wwoxhep−/− mice, which might be insufficient to decrease whole-body circulating HDL-C levels"

`surface: body` · Discussion. Second explanation, same paragraph:
> "livers contain other cells including stellate, sinusoidal endothelial and Kupffer cells, which may express Wwox in the livers that were isolated"

**4.** *And the compensating tissue they propose is the intestine — a hypothesis, untested here.*
> "The intestine may thus compensate for plasma HDL biosynthesis in this mouse model, warranting additional investigations"

`surface: body` · Discussion. 🔴 `PREMISE: IPOTESI` — declared by the authors as warranting
investigation, not demonstrated.

**5.** *The whole-body result is measured in two-day-old pups.*
> "we thus assessed the effect of Wwox deletion in hepatic tissues from two days old Wwox KO mice"

`surface: body` · Discussion. This matters for any transfer: `Wwox^−/−` mice die by ~4 weeks
with growth retardation, so the HDL phenotype is measured in an animal that is systemically
failing. Fig. 5A shows the VLDL/LDL peak reduced alongside HDL — the loss is not
HDL-selective on the trace.

### Human genetics: what the pedigrees show and the text does not

**6.**
> "All 16 affected family members except one shared the variant allele haplotype"

`surface: body` · Results. And the caption:
> "Fifteen of the 16 affected subjects with HDL-C<5th age-sex specific population percentile have the risk alleles"

**7.** 🔴 **Figure 1A shows the haplotype is neither necessary nor sufficient, and only the
pedigree shows it.** `surface: figure` · artifact `…f1a.jpg`, family-1 pedigree, read at 150
ppi.
- the **one exception** is identifiable: individual **401**, generation IV, daughter of the
  affected 309 — a filled symbol with **no boxed haplotype**. Affected, not a carrier;
- founder **102** carries the boxed risk haplotype and is an **unfilled symbol**, i.e. HDL-C
  >10th percentile by the figure's own key. A carrier who is not affected.

The text says the haplotype "perfectly co-segregated with the low HDL-C in families"
(Discussion). That claim is about the affected; the pedigree adds an unaffected obligate
carrier, which the running text never mentions. **Incomplete penetrance in a 16-member
segregation is not a footnote — it is the difference between a causal allele and a linked
marker.**

**8.** *Every co-segregating variant is intronic; the only exonic one fails.*
> "among the 8 variants, there is only one nonsynonymous variant (rs289723) in the NLRC5 gene which did not co-segregate with low HDL-C in these families"

`surface: body`. Table 2 gives it `P-value 0.3131` against `0.0005` for the top WWOX intronic
variants. `surface: table`. So the human evidence is **positional**: no coding change in
WWOX is implicated, and no functional mechanism for the intronic haplotype is shown here.

**9.** *Sex is confounded with affection in the sequenced set.* Table 1: all four resequenced
affected individuals are **female** (210, 212, 201, 301); three of four controls are female,
one male. `surface: table`. Any "gender effect" downstream inherits this design.

### Two numbers the panels arbitrate, and the text and captions disagree on

**10.** Text:
> "Hepatic ABCA1 and ApoA-I protein levels were also significantly reduced, by 40% and 80%, respectively (Abca1 **P=0.015, ApoA-I ***P=0.0007, Figure 5G–J)"

Caption of Fig. 5: `**P=0.0015 and ***P=0.007`. The two disagree **in both directions**.
`surface: figure` · `…f5.jpg`, panels H and J, read on a ×3 crop:
- **panel H prints `**P = 0.0015`** → the caption is right, the text has a typo;
- **panel J prints `***P = 0.0007`** → the text is right, the caption has a typo.

Neither could be settled from text or captions alone; only the panel decides, and it decides
one each way.

**11.** 🔴 *The text claims two mRNA reductions where the panel marks one.* Text:
> "Levels of both AbcA1 and ApoA-I mRNA were decreased in Wwox−/− compared to WT, as assessed by RT-PCR (AbcA1 ***P<0.00058, Figure 5E)"

`surface: figure` · `…f5.jpg` panel E, ×3 crop: the significance bracket sits **over Abca1
only**. ApoAI shows WT 1.0 versus KO ≈0.72 with **no bracket and no asterisk**, and visibly
overlapping error bars. ApoA-I mRNA reaches significance only in the *separate* pure-FVB
model of panel F (`*P=0.0145`).

**This is the `CLAIM 005` distinction again**: the panel does not say ApoA-I mRNA is
unchanged, it says the paper does not mark it significant there. The proposition the text
carries — "both were decreased" — is stronger than the panel it cites.

### The sex-specific mechanism runs against its own figure

**12.** Discussion:
> "the increased production of hepatic Angptl4 in Wwoxhep−/− females (Suppl. Table 2A, Figure 4C, F) was concomitant with the observed elevated serum TG levels"

**13.** 🔴 `surface: figure` · `…f4.jpg` **panel F**, ×3 crop: the panel prints
**`*P = 0.0229` for males** and **`P = 0.0877` for females** — no asterisk on the females.
The ANGPTL4 protein increase is significant **in males and not in females**.

These two numbers appear **nowhere else**: not in the Results text, not in the figure caption.
The female-specific triglyceride mechanism is therefore built on the one group in which the
proposed mediator does not rise significantly. The TG phenotype itself is female-specific and
visible (panel J: the female VLDL-TG peak roughly doubles; panel I: males near-superimposed)
— it is the *Angptl4 explanation* for it that the panel undercuts, not the phenotype.

**14.** 🔴 *The "female-dominant" reading holds for one ranking and inverts for another.*
`surface: figure` · `…f2.jpg`. Panel A vs C: lipid metabolism is the **1st** molecular
function in females and **7th** in males — as the text says. But panels B and D, the canonical
pathways, are plotted on different x-axes: **females top out at −log₁₀(p) ≈ 2.0** (P ≈ 0.01)
while **males reach ≈ 5.3** (P ≈ 5×10⁻⁶, acute-phase response). Every female canonical pathway
the text lists sits between P≈0.013 and P≈0.048, and **no FDR is reported for that panel** —
the Benjamini-Hochberg adjustment quoted in the text applies to the *functions* of panel A,
not to these pathways. Against:
> "These data support the observation that Wwox seems to play a more prominent role in female HDL, TG and FA metabolisms"

**15.** `surface: figure` · `…f3.jpg`: panel B, the "56 male lipid-metabolism genes", is
dominated by acute-phase and immune genes (`Saa1`, `Saa3`, `Apcs`, `Socs3`, `Stat3`, `Hpx`,
`Cp`). The IPA "lipid metabolism" label carries a broader gene set than the phrase implies.

**16.** *All comparisons are unadjusted two-group t-tests.*
> "Two-tailed Student’s t-test was used for comparisons between two groups as applicable"

`surface: body` · Methods, Statistical analysis. No multiplicity correction is declared for
the protein/serum panels.

## What this does to FT-039's question

The queue asked whether *strong evidence* transfers to the node. **It does not transfer intact,
and the paper itself is the reason** — its central negative is that removing Wwox from
hepatocytes does **not** lower circulating HDL.

| the bridge needs | what the primary gives |
|---|---|
| a model | two: liver-specific (no HDL effect) and whole-body (HDL effect, measured in 2-day-old pups that die by 4 weeks) |
| a perturbation | complete `Wwox` ablation in mouse; in humans, an **intronic** haplotype with no coding change and no functional assay |
| an endpoint | serum HDL-C, ApoA-I, ABCA1, TG — **peripheral lipid measures**. No neural, no myelin, no CNS endpoint anywhere in the paper |
| effect sizes | ApoA-I protein −55%/−50% (hep KO), −80% (total KO); ABCA1 −50% males, unchanged females; HDL-C markedly reduced in total KO only |

**The label "strong evidence" is defensible for what this paper is about — WWOX and HDL — and
is not transferable to myelin by this paper.** The step it actually licenses is
`WWOX → ApoA-I/ABCA1 → HDL biogenesis`, whole-body and not hepatocyte-autonomous. The second
leg of the bridge, `lipid homeostasis → myelin`, gets **nothing** from here: this paper never
measures a neural endpoint. 🔴 `PREMISE_TAG` — any inference that crossed from this node to
myelin was resting on a premise this primary does not contain.

The `ESPANSIONE` worth keeping is narrower and real: **Wwox loss lowers ApoA-I and ABCA1
protein in liver, and the whole-body null has markedly reduced HDL and ApoA-I.** ApoA-I and
ABCA1 are independently relevant to CNS lipid handling, so the node stays open — as an
expansion to be tested, not as a supported inference.

## Reading debt this session opens

- **Supplementary Material** — `unavailable` by the cascade above. The only route left is the
  publisher (AHA, all rights reserved) or an author request. It carries the `P=0.0025`
  triglyceride datum the sex-specific story starts from.
- **Multi-hop not performed.** Reference 44 (Lichtenstein, ANGPTL4 → LPL inactivation) is the
  load-bearing external premise for locator 12's mechanism and is unread. References 10, 11,
  13, 20 (the `Wwox^−/−` and `Wwox^flox` source papers, Aqeilan/Aldaz) are cited for the model
  itself; 33255508 is already read.
- **`PMID 21212533` locators** remain owed from an earlier session; unchanged by today.

## A finding about the queue, not about the paper

Twenty-two local structured full texts have no complete read. **Twenty-one of them are not in
the full-text queue at all** — including the whole local Aqeilan series (`27308416`,
`27308504`, `27551470`, `29724996`, `30082886`, `30755385`, `32300104`, `34831305`,
`26256646`, `27550453`), the founding oncology papers, and `42395553`/`42422765`. They were
acquired and never ranked.

The queue therefore ranks what someone thought to enqueue, not what is in hand: a paper can be
sitting on disk in a clean structured surface and be invisible to the very list that decides
what gets read next. Logged for the queue's owner; not repaired here, because today is for
reading.
