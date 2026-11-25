# ADV-279 increment 2: report of the blind second reading (legend-delegate, model sonnet, effort high stated in the dispatch)

Saved as returned (final message of the delegate, harness indentation removed). Statements: BLIND_STATEMENTS_INC2_SCI_20261125.md.
Hypothesis level; not medical advice.

Hypothesis level; not medical advice. All six statements come out **not supported**. Each rests on a figure, table or text I opened directly.

| ID | Verdict | Short reason |
|---|---|---|
| T1 | not supported | sorbitol on G544D is about 177% in panel a and about 103% in panel b |
| T2 | not supported | the body states it explicitly, twice in Section 7 |
| T3 | not supported | Y33R/WT per immunoprecipitated MERIT40 is 0.61 |
| T4 | not supported | the whole-curve half-inhibiting values (about 1 to 2 mM) are above the shaded band |
| T5 | not supported | the median from the source data is 95 days, not 97 |
| T6 | not supported | Methods give 100 mg/kg; Results and legend give 150 mg/kg |

## T1 (PMID 30266908): not supported
**Panel.** `41467_2018_6507_MOESM1_ESM.pdf`, page 19, Supplementary Figure 12:
- panel a, G544D bar graph, "Sorbitol, 200 mM";
- panel b, "Sorbitol" graph, sixth bar (order: Control, WT, P335L, R406H, P480L, G544D, G544V).

**How.** I rendered the page, extracted the embedded image and enlarged the crops. Heights are pixel positions read by eye against the axis ticks, so about ±3 percentage points.

**Numbers** (value = (baseline y − bar-top y) / pixels per 1%):
- **Panel a:** about 177% of control, marked *. The three dots read about 230, 164 and 132.
- **Panel b:** about 103% of control, no asterisk. The three dots read about 112, 103 and 95.
- The increase is therefore about +77% in a and about +3% in b. The two sets of dots do not overlap.

**Legend.** "(b) Same as in (a), except that HEK293T cells were transfected with plasmids expressing WT or mutant Munc18-1 in absence or presence of 5 mM 4-phenylbutyrate, 200 mM sorbitol, or 200 mM trehalose." Each panel has n = 3.

**Easy to miss:**
- Trehalose 200 mM on G544D agrees between the panels (about 237% and 235%), so this is not a general offset between a and b.
- Phenylbutyrate on G544D differs less (about 182% and 155%).
- Panel b's sorbitol graph does show rises for other variants (R406H about 197%, G544V about 155%). Reading the wrong bar would mislead.

## T2 (PMID 34359949): not supported
**Locators** (body, "7. WWOX in Alzheimer's Disease"):
- "WWOX blocks Tau hyperphosphorylation by directly binding Tau via its C-terminal SDR domain [41,69]."
- "By direct binding, the SDR domain of WWOX restricts GSK3β-mediated hyperphosphorylation of Tau [41,69]."

**Also in the body:**
- Section 6.1: "SDR domain binds and blocks GSK-3β-mediated tau hyperphosphorylation …". This one is ambiguous as to what is bound.
- Figure 1 lists Tau in the box "SDR domain & binding partners".

**Abstract.** "WWOX binds Tau via its C-terminal SDR domain …"

**How.** I parsed the XML (abstract and body searched separately for Tau and SDR sentences), printed the three figure captions and viewed the three figures.

**Easy to miss.** The abstract does not use the word "directly"; the body does. This is a review citing refs 41 and 69, which I did not open. Presence in the body is not primary evidence of direct binding.

## T3 (PMID 37248434): not supported
**Panel.** `Fig1.png`, Figure 1B, viewed enlarged. The lanes are WT only, Y33R only, MERIT40 only, WT+MERIT40, Y33R+MERIT40.

| Row | Printed densities |
|---|---|
| WWOX bound (IP Flag, blot HA) | 270, 326, 200, 12360, 9243 |
| MERIT40 (IP Flag, blot Flag) | "284  129/39842/41508/50699", i.e. 284, 129, 39842, 41508, 50699 |
| WWOX (blot HA) | "21775/13801", 0, 20003, 21002 |

**Calculations:**
- WT: 12360 / 41508 = 0.298.
- Y33R: 9243 / 50699 = 0.182.
- Y33R/WT = **0.61**, about 39% less.
- Subtracting the MERIT40-only lane (200) from both numerators: 0.61.
- Also dividing by the WWOX blot-HA values (20003 and 21002): 0.58.
- Without any normalisation: 9243 / 12360 = 0.75.

**What cuts against it.** The text says the opposite qualitatively: "this mutation did not affect the WWOX-MERIT40 association (Fig. 1B)". Y33R clearly still binds.

**Limits.**
- It is one blot. I found no replicate number or statistic for Figure 1B in the legend or body search.
- Linearity and saturation of the densitometry are unknown.
- So the densities do not support "same degree", but they do not establish a reproducible reduction either.

## T4 (PMID 37275776): not supported
**Every half-inhibiting value I found for GIRK1/2 with wild-type Gβγ:**

| Value | Where printed |
|---|---|
| One-site Kd,app 1.2 mM | `Data_Sheet_1.PDF` p.11, Supplementary Fig. 6B table (an image, so a text search misses it) |
| Hill Kd,app **1.24 mM** (nH 0.68) | same table |
| Two-site model: 0.32 mM and 7.779 mM (high-affinity fraction 0.57) | same table |
| "Both basal and Gβγ-evoked GIRK1/2 currents … EC50 of ~1.5–2 mM" | Results text (XML and main PDF) |
| "the Gβγ-activated GIRK1/2 … shows EC50 of ~1 mM" | Discussion |
| Red curve crosses the 50% line at about 1.22 mM (my measurement, not printed) | Figure 7B |

**Band.** I measured it from `fncel-17-1175895-g0007.jpg`. The log-axis ticks are 53.25 px per decade, with 1 mM at x = 538.5. The band spans x of about 505 to 534.5, giving **about 0.23 to 0.84 mM** (concentration = 10^((x − 538.5) / 53.25)).

**Computed from the printed parameters:**
- The two-site curve 0.57·x/(x+0.32) + 0.43·x/(x+7.779) = 0.5 at x = **1.14 mM**.
- The Hill curve gives about 43% inhibition at the band's upper edge.

**What cuts against it, or is easy to miss:**
- The 0.32 mM two-site component does lie inside the band. It is one affinity component, not the half-inhibiting concentration of the channel's total inhibition.
- The text's therapeutic range is "between 300 and 750 μM … and can go as high as 1.1 mM". The Discussion speaks of "higher therapeutic doses of ETX (0.7–1.1 mM)". The "~1 mM" value falls inside that wider textual ceiling, though right of the shaded band.
- The **K78R** Gβγ value for GIRK1/2 (0.54 one-site, 0.56 Hill; green curve about 0.56 mM) is inside the band. It is easy to confuse with wild type.
- The "~1.5–2 mM" sentence disagrees with the table: basal is 3.3 to 3.4 mM and WT Gβγ 1.2 to 1.24 mM.
- The Figure 7 legend sends the reader to "Supplementary Figure 5B" for the fits. The table is in Supplementary Fig. 6B; Fig. 5 is action-potential firing.

## T5 (PMID 36278433): not supported
**Source.** `EMMM-14-e15343-s003.xlsx`, sheet "Fig5f" ("Mice survival"). The workbook's legend calls it Figure 6, sheet 5. It corresponds to published Figure 6F (g012).

**Data.**
- **Stiripentol**, n = 15, all events: 74, 75, 83, 84, 86, 87, 93, 95, 96, 97, 98, 98, 99, 100, 102.
- **Vehicle**, n = 16, all events: 60, 61, 66, 70, 70, 74, 80, 80, 86, 88, 88, 89, 90, 92, 93, 95.

**Median** (Kaplan–Meier, first time S ≤ 50%):
- **Stiripentol = 95 days.** S is 53.3% after day 93 and 46.7% at day 95. It never sits at exactly 50%, so every convention gives 95, as does the ordinary median (8th of 15). The mean is 91.1.
- **Vehicle** sits at exactly 50% from day 80 to day 86. "First S ≤ 50%" gives 80; "first S < 50%" gives 86; the midpoint convention gives 83.

**Checks.**
- My log-rank is χ² = 9.655, p = 0.0019, matching the sheet (9.655, 1.9E-3). So this is the dataset behind the statistics.
- No hidden rows or columns were flagged in the sheet XML.
- In enlarged panel F the red step crosses 50% at day 95.

**Easy to miss.** The Results print "median survival was 80 days for control mice and 97 days for stiripentol-treated mice". So the statement repeats the paper's number but not what its source data give. The median gain is 15 days under the first-S≤50% rule, not 17.

## T6 (PMID 36278433): not supported
**Locators** (XML, confirmed in `PMC9728051.1.pdf`):
- **Methods**, Intracranial implantation (PDF p.14): "bevacizumab injections (10 mg/kg ip), and/or stiripentol (**100 mg/kg** ip), or phenformin (50 mg/kg ip) injection 3 times a week."
- **Results** (PDF p.11): "intraperitoneally injected with **150 mg/kg** of stiripentol."
- **Figure 6F legend** (PDF p.11): "stiripentol at **150 mg/kg** (red) (n = 15–16 mice per group)."

**How.** XML sentence search for dose strings, then a dose search through every page of the PDF. The three-times-a-week frequency appears in the Methods sentence; I saw none in the Results or legend sentences.

**Likely explanation, from outside T6's named files.** `EMMM-14-e15343-s005.pdf`, the peer-review file in the same supplement folder, has an author reply: a previous experiment used 100 mg/kg, then "we have increased the stiripentol to 150 mg/kg … as shown in the new graph in Fig 6F". It also mentions an initial 300 mg/kg attempt. This suggests the Methods kept the older dose, which is my inference. The verdict does not depend on this file.

## Scope
- **Repository inputs.** Apart from the statements file, I opened only source files under `/home/desktop/legend-development/files/` for these six items; no records, cards, ledgers or notes. The one extension is the peer-review file noted under T6.
- **Auto-loaded context.** The project instructions and memory index were in my context automatically; I used nothing from them for any verdict.
- **Not read.** I did not open `framework/protocols/delegation_budget.md`, in keeping with the dispatch's file restriction.
- **Not done.** No network, commits or repository edits.
- **Scripts and images** are in `/home/desktop/.claude/jobs/8ee4045d/tmp/verify_inc2/tools/` and `/home/desktop/.claude/jobs/8ee4045d/tmp/verify_inc2/img/`.
