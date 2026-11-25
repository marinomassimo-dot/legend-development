# PREREG, ADV-284: equivalence-margin audit of the "not different from wild type" restoration rows (SCI, 2026-11-25)

Hypothesis level; reference genotype class; nothing is medical advice. Written and hashed before any n, spread or statistic of any row's source was opened. What I had seen before: the six card notes in `equivalence_rows_adv281.tsv` (their by-eye values, e.g. SOX2+MYC+ about 72 to about 50 percent), written by the previous window.

## 0. Scope and one deviation, fixed first

Five of the six rows (DR-AAV-GFAP-P5HD, DR-AAV-GFAPAREA-HD, DR-AAV-GLU20-HD, DR-AAV-MOTOR-HD, DR-C01-001) have Obeid 2026 (PMID 42422765, PAPER 011) as their only source. A safety classifier stopped the session's response during the extraction of that article in ADV-282; that stop is not retried, rephrased or substituted, and its manifest, receipt text and supplement are not opened. These five rows are recorded "not audited, classifier stop, operator list", with the reason, next to DA-W2-011 and DA-I01-006. The audit covers the one remaining row: **DR-D01-001** (card D01_a51; Steinberg 2026, PMID 42397075; SOX2+MYC+ progenitor fraction, A51-treated knockout organoids). Sources: held bytes only (the accepted-manuscript PDF and the Brain supplement of PMID 42397075 in `files/fulltext/`), no acquisition, no spend, no contact.

## 1. Classes (frozen)

* **MARGIN GIVEN:** the held source states, in the text, legend or methods, a pre-specified smallest difference that would matter, a test of equivalence (TOST or similar), a confidence interval of the difference between the treated and the reference arm, or a power calculation for the endpoint. Locator required. A non-significant P value against wild type is not a margin.
* **DERIVABLE:** no margin, but n per arm (independent unit stated) and a spread measure (SD or SEM given, or box quartiles or point values legible in the held figure image) are held, so a smallest detectable difference can be computed.
* **NOT DERIVABLE:** n or spread cannot be obtained from the held bytes, or the unit of n is not independent (e.g. fields or sections pooled from a few organoids); the missing item is named.
* The class never decides a direction.

## 2. Computation (frozen, for DERIVABLE)

* Smallest detectable difference (SDD) between the treated arm and wild type, two-sided alpha 0.05, power 0.80, two independent groups, equal-variance t approximation: SDD = (t(1-alpha/2, df) + t(power, df)) x sp x sqrt(1/n1 + 1/n2), with df = n1 + n2 - 2 and sp the pooled SD of the two arms as read from the source (SD from SEM times sqrt(n); from box quartiles only when the whiskers/points give the SD within the stated reading error, and then marked "by eye"). Formula and every input are written beside the result with sheet/figure, panel and arm.
* The comparison to read against: the **disease effect** = the knockout-minus-wild-type difference in the same panel (read as printed or by eye, labelled). Residual fraction detectable = SDD / disease effect.
* If the source gives per-organoid values, they are used; if only fields or sections are plotted, the unit is declared and the class is NOT DERIVABLE unless the number of organoids is also given.

## 3. "Claims more than the data can bear" (frozen before the numbers)

The row's card sentence claims more than the data bear if BOTH hold:
1. it states or implies sameness or restoration (any of: not different from wild type, restored, normalised, rescued to wild-type level, indistinguishable), AND
2. the class is NOT DERIVABLE, or the class is DERIVABLE (or MARGIN GIVEN with a margin wider than half the disease effect) and **SDD is at least half of the disease effect** (the data could not exclude that half of the disease effect persists).
It does NOT claim more than the data bear if a MARGIN GIVEN margin is at most half the disease effect and the interval or test lies inside it, or if the sentence is already confined to "not significantly different" with n and the SDD stated. The one matching rule applies to the one blind reader and to me alike; counts are given under it only.

## 4. Prediction and rejecting observation

* For the one assessable row: P(class DERIVABLE) 50 percent, NOT DERIVABLE 40, MARGIN GIVEN 10 (small n and an uncorrected multiple-arm comparison are expected; the card already says "no treated-wild-type arm" in its note). P(claims more than the data bear | assessable) 70 percent. Range for "claims more than" over the one row: 0 or 1; the six-row range ADV asked for is not testable with five rows blocked (stated).
* Rejecting observation: a MARGIN GIVEN class or an SDD below half the disease effect with the sentence confined to what the data show (the row survives the rule).

## 5. Blind reader

One blind reader (legend-delegate, sonnet, effort high; stated and read back from the census) receives only the verbatim card sentence built by script, the held-source paths and the formula's inputs request (not my numbers, not the class, not this PREREG): it answers MUST CHANGE / ADD / STANDS and gives its own class and SDD from its own reading. It may not open the audit folder, PREREG, RESULT, or any card text. Consumers: card D01_a51 (IT) with one proposed corrected sentence; the premise-check strand (ADV).
