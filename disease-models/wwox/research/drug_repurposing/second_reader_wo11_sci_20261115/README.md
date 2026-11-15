# Second read of the WO-11 number (Mierau 2004, PMC524435), SCI, 2026-11-15

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. No ranking, card, map, need, tier or frozen package was edited. Predictive capacity of this note: none.

Label: DATO = stated in the saved article text (quote id in `verbatim.tsv`); INFERENZA = my reading.

## Answer first
IT's WO-11 note (`../wo11_mierau_it55_20261115/README.md`, landed c2859e5c3) **holds as to the number**. Every figure it prints is in the article text: 14% (C.I. 0-34%) at P13-P15 whisker-intact, control n = 15, ifenprodil n = 10; 53% (43-61%) at P6-P8 (9/5); 49% (24-71%) whisker-deprived P13-P15 (7/6); 26% whisker-deprived P26-P33 (8/6) (Q1-Q3). Bootstrap 2.5/97.5 percentile interval (Q4) and the between-cell design (Q5) are as IT states. 15/15 quotes found (`output/verify_output.txt`).

Three wording points differ from the text. None moves the number or the conditional reading; all three narrow what IT's limits paragraph says about the measurement.

| # | IT's wording | What the article text says | Proposed wording |
|---|---|---|---|
| 1 | "an L4-evoked EPSC read at 50 ms and +40 mV" | NMDA amplitude is "measured at 50 ms after stimulation" (Q9). +40 mV is stated for the **A/N ratio** (Q10). The Fig. 3 ifenprodil passage gives no holding potential. | "NMDA amplitude read at 50 ms; the holding potential of the ifenprodil comparison is not stated in the passages read (+40 mV is stated for the A/N ratio)". |
| 2 | "Treated slices were pre-incubated with ifenprodil" | Pre-incubated at least 40 min (Q5) **and** "Ifenprodil also was added to the superfusate during recording" (Q6). | Add "and present in the bath during recording". It does not change the between-cell design. |
| 3 | "The 14% is a floor on the GluN2B-containing share" | The interval is 0-34% (Q1), so 0.14 is a group-mean estimate whose interval includes zero; the paper does not test saturation (3 uM is the only concentration used, Q5). | Keep "not a saturation proof", and replace "floor" by "an estimate of the ifenprodil-sensitive share at one concentration; incomplete block would make the true GluN2B share larger, the interval allows zero". |

Also recorded, not a correction: the formula behind "percent ifenprodil-sensitive current" is not written out in the passages read. Fig. 3A says currents are "scaled to the same peak amplitude AMPA current" for display (Q13); whether the percent is taken on raw or AMPA-normalised NMDA amplitudes is not stated. IT's text does not claim either. Where the note says "between-cell difference of group means" that is my reading of Q5 and Q14, not a sentence in the paper.

## What the bootstrap used (ADV's question)
DATO (Q4 and the statistics paragraph): "The mean and confidence interval (C.I.) of the ifenprodil-sensitive NMDA-receptor-mediated current were estimated by using bootstrap resampling (B = 10,000) in s-plus"; "The observed means and the empirical 2.5 and 97.5 percentiles are reported"; group differences were tested "by using a bootstrap test". The passages read do not say what was resampled. They give no per-cell values, no SEMs for the percentages, and no description of how a percentage is formed from two groups of different cells (control n = 15, treated n = 10). INFERENZA: resampling cells within each group and recomputing the ratio of group means is the natural reading, but it is my reading and not a sentence in the paper. Consequence: the 0-34% interval cannot be re-derived from the article; only the figure it draws (Fig. 3B) could add cell-level detail, and I did not extract it.

## Time point
The P13-P15 label is the paper's own age window for whisker-intact mice in the Fig. 3 passage (Q1); it is not a single day, and no animal-level n is given (n counts cells).

## What was checked and what was not
- Read: abstract, Methods (slice preparation, bath, drug protocol, pipette, A/N, statistics), Results from the A/N section through the P26-P33 paragraph, Fig. 3 legend, and the Discussion paragraph on experience-dependent NMDA changes. This is more than IT's partial receipt (captions only); the Introduction and the rest of the Discussion were not read.
- Not read: figure images (Fig. 3B is a plot of means with intervals; I did not extract its geometry, the text gives the numbers).
- The Discussion (Q15) calls the P14 whisker-intact proportion "significantly lower" than in deprived animals and makes no statement about saturation or about layer 2/3 bursting slices, which matches IT's "not evidence about the burst".
- The paper's decay-time n (Fig. 3C legend: 15 and 9 at P13-P15 whisker-intact) differs from the 15 and 10 of the ifenprodil percentage by one cell; I take that as a cell without a usable decay fit and did not follow it up.

## Independence and access
Independence: I did not write the WO-11 note, I did not read its README before reading the article, and I did not use IT's saved page. My copy is a separate GET (`access.tsv`). Same origin as IT's source (the PMC article page), so this is a second read of one text, not a second source.

Access: one plain GET, HTTP 200, 161,814 bytes, article title present, no challenge page. **Slip, recorded**: I sent the request with a browser-style User-Agent string. The repository's rule (HE43/HE44, PMC notes) is a generic client and no browser-UA spoofing. The page was served and the content is the article, so the reading is unaffected, but the access is not the one the rule describes and I will not repeat it. No contact address was sent anywhere.

Checker bug found and fixed on the way: `verify_quotes.py` first stripped `<...>` from a plain-text body, which deleted the spans between the "P < 0.01" signs and made 7 quotes "missing". It now strips tags only from `.html` input.

Input digests: `input_digests.sha256` (page and extracted text). Saved copies are under `files/fulltext/wo11_second_read_20261115/` (gitignored).
