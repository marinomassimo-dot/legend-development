# Dated addendum (2026-11-20) to the RP-019 first pass: Pvalb in the held hippocampal nuclei deposit GSE158684 (SCI successor window; descriptive; hypothesis level; no dose, no target assumed; not medical advice)

**Answer first.** The held single-nucleus deposit of the neuronal-deletion mouse (GSE158684, hippocampus, P17, one pool per arm) cannot inform the PV question: it holds **46 control and 58 knockout inhibitory nuclei** (of 3182 and 2920 nuclei), and **Pvalb is detected in 1 of the 46 and 2 of the 58**. No value and no test is reported. The first pass stands: PV stays "not a target", revival trigger unchanged (a fate-mapped total-interneuron count with the PV fraction per animal; a second independent report of PV counts; or PV-identified physiology).

**Pre-registration (written before the matrices were opened; the same session had already re-read the held texts of Hussain 2019, Breton 2021, Cheng 2020, Steinberg 2021 and Repudi 2021, which agree with the first pass).** Inhibitory nucleus = Gad1 + Gad2 + Slc32a1 UMI >= 2 and Slc17a7 + Camk2a + Satb2 UMI = 0. Within inhibitory nuclei: number and fraction with >= 1 UMI of Pvalb, Sst, Vip, Npy, Lamp5, Cck. No p-value (one pool per arm). A Pvalb shift would have been called large only if the knockout over control ratio fell outside 0.67 to 1.5 while Sst or Npy moved less than half as far. This is simpler than the unit A2 scoring (not re-used), so the inhibitory set may differ slightly from the one in A2.

| Arm | Nuclei | Inhibitory (fraction) | Pvalb | Sst | Vip | Npy | Lamp5 | Cck |
|---|---|---|---|---|---|---|---|---|
| control | 3182 | 46 (0.014) | 1 | 5 | 1 | 7 | 8 | 11 |
| knockout | 2920 | 58 (0.020) | 2 | 10 | 5 | 7 | 5 | 9 |
Counts are inhibitory nuclei with at least one UMI of the gene. Median UMI per nucleus 4772 (control) and 4342 (knockout).

**Reading.** With 1 v 2 nuclei the ratio is arithmetic noise, so the registered shift criterion cannot be evaluated and no direction is stated. The inhibitory fraction (0.014 v 0.020) is tiny for hippocampus, which suggests the nuclear preparation under-samples interneurons or the strict rule loses most of them; either way the deposit has no PV resolution. **Not a measure of the P2 premise of CLAIM 005 (a germline knockout at 2 weeks, a different line and age).** Deposit bytes: `files/geo/GSE158684/` (`SHA256SUMS` there). Script: inline, not kept; the rule above reproduces the counts from the three files per arm.
