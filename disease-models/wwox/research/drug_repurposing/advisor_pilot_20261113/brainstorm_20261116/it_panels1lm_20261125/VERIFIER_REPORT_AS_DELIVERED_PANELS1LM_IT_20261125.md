# Blind verifier report as delivered (IT, ADV panels 1L/1M re-read, 2026-11-25)

Subagent `legend-delegate`, asked sonnet / effort high, read back sonnet-5-5 / high on 16 of 16 turns (16 turns, 40,479 output tokens, birth context 26,970). The delegate could not write its own report file (the harness refused a Write by a subagent); this is the text it returned, unedited. The verifier was not shown any of IT's numbers, the pre-registration, or any file under disease-models/. It did not see the methods sentence quoted in the result (blots quantified 2-3 times, representative images shown).

## Blind re-read of Supplementary Fig. 1L and 1M immunoblots (nothing here is medical advice)

**REPORT.md was not written.** The Write tool refused it ("Subagents should return findings as text, not write report files") and I did not work around that. This message is the full report; save it if you need the file. Scripts and images are in `/home/desktop/.claude/jobs/06001577/tmp/verify_p1lm/code/` and `/home/desktop/.claude/jobs/06001577/tmp/verify_p1lm/data/`.

**Inputs.** File012 pages 6 and 7, the File010 page 2 image and the page 3 legend. No `disease-models/`, other file about the paper, web or network was used. Listing the source folder showed other file names, including a reading note; I opened none of them.

**Method.**
- The signal is the sum of (background - grey) in a rectangle, taken on the **lower** band, which is the only one the composite shows.
- It is divided by HSP90 and expressed relative to JH WT on the same membrane.
- The median [min-max] comes from 216 combinations of window height and width, WWOX background (3 kinds) and HSP90 window and background.
- A second method used one common row window for all lanes.
- These ranges reflect analysis choices only. There is one blot per panel, so no replicate uncertainty.

### 1L
There are 7 sample lanes and one ladder, and all 7 lanes are in the composite.

| Lane | Printed | Lower/HSP90 | Common window | No HSP90 | Optical density/HSP90 | (Upper+lower)/HSP90 | Verdict (factor 1.5) |
|---|---|---|---|---|---|---|---|
| JH WT | 1 | 1 | 1 | 1 | 1 | 1 | reference |
| WSM S2 | none | 0.023 [0.016-0.030] | 0.024 | 0.026 | 0.010 | 0.045 | - |
| WSM S5 | none | 0.009 [0.001-0.014] | 0.011 | 0.006 | 0.005 | 0.017 | - |
| LM-iPS | 0.2 | 0.16 [0.14-0.18] | 0.17 | 0.09 | 0.11 | 0.085 | reproduced, sensitive |
| WSM S2 AAV9 | 0.4 | 0.45 [0.41-0.49] | 0.46 | 0.22 | 0.34 | 0.23 | reproduced |
| WSM S5 AAV9 | 0.4 | 0.39 [0.35-0.44] | 0.41 | 0.17 | 0.31 | 0.21 | reproduced |
| LM-iPS AAV9 | 0.9 | 1.07 [0.92-1.19] | 1.15 | 0.29 | 0.98 | 0.57 | reproduced |

- **Window and background:** under linear grey they change no verdict. LM-iPS is closest to the limit (factor 1.47 at its minimum).
- **Normalisation:** without HSP90, all four values fail (factor 1.8-3.1).
- **Band choice:** with upper+lower, LM-iPS, S2 AAV9 and S5 AAV9 fail, and LM-iPS AAV9 is marginal (1.6).
- **Optical density:** only LM-iPS fails (1.9).
- **HSP90 relative to WT:** 1.19, 0.69, 0.59, 0.49, 0.43 and 0.27 in table order from S2 to LM-iPS AAV9, so loading is very uneven.
- **Published composite pixels:** these give 0.14, 0.39, 0.35 and 0.85 for the four printed lanes.

### 1M
There are 7 sample lanes, with ladders on both sides of the WWOX strip. The composite shows 5; **WPM D1 AAV9 and WPM D3 AAV9 are absent**.

| Lane | Printed | Lower/HSP90 | Common window | No HSP90 | Optical density/HSP90 | (Upper+lower)/HSP90 | Verdict (factor 1.5) |
|---|---|---|---|---|---|---|---|
| JH WT | 1 | 1 | 1 | 1 | 1 | 1 | reference |
| WPM S1 | 0.1 | 0.10 [0.07-0.13] | 0.10 | 0.13 | 0.065 | 0.17 | reproduced, sensitive |
| WPM D1 | 0.1 | 0.10 [0.07-0.12] | 0.11 | 0.12 | 0.064 | 0.05 | reproduced, sensitive |
| WPM D3 | 0.3 | 0.24 [0.18-0.29] | 0.26 | 0.25 | 0.18 | 0.59 | reproduced, sensitive |
| WPM S1 AAV9 | **7** | 0.97 [0.61-1.21] | 1.25 [1.15-1.66] | 1.58 [1.03-1.88] | 0.97 | 0.34 | **not reproduced** |
| WPM D1 AAV9 (not in composite) | - | 0.13 [0.02-0.21] | 0.18 | 0.18 | 0.07 | 0.05 | - |
| WPM D3 AAV9 (not in composite) | - | 1.24 [0.93-1.42] | 1.37 | 1.52 | 1.83 | 0.67 | - |

- **The value 7:** no route gives more than about 2.2 for S1 AAV9 vs WT, including no normalisation and the composite's own pixels (1.09 [0.72-1.40] normalised there). The verdict does not depend on my choices.
- **A possible but unverified source of 7:** S1 AAV9 over untreated S1 is about 9.3 [6.8-12.5], so a number of that order arises with a non-WT reference. I cannot establish what computation produced 7.
- **The 0.1 values:** optical density gives a factor of about 1.55 (marginal fail). Upper+lower gives 1.7 for S1 and 2.0 for D1.
- **The 0.3 value:** the factor is 1.23 at the median and 1.65 at the lowest variant. It fails with optical density (1.7) and with upper+lower (2.0).
- **HSP90 relative to WT:** S1 1.31, D1 1.14, D3 1.03, S1 AAV9 1.65, D1 AAV9 1.47, D3 AAV9 1.23.

### Rescued lanes
**1L**
- S2 AAV9 and S5 AAV9 are alike (ratio 1.14 [1.07-1.22]). LM-iPS AAV9 is 2.4-2.7 times either.
- That advantage comes largely from its weak HSP90 band; without normalisation it is only 1.3-1.7 times.
- LM-iPS AAV9 over untreated LM-iPS is 6.7 [5.9-7.8], or 3.1 without HSP90.
- Untreated S2 and S5 are near background, so their fold changes (about 20 and 38) are unstable.

**1M**
- S1 AAV9 and D3 AAV9 are comparable (D3/S1 1.26 [1.16-1.54] normalised, 0.94 raw), both about WT level.
- Against untreated lines, S1 AAV9 is 9.3 times S1 and D3 AAV9 is 5.1 [4.5-5.9] times D3.
- **D1 AAV9 is about one tenth of the other two rescued lanes.** Against untreated D1 it is 1.2 [0.2-1.8], so there is no clear increase in the integrated window.
- Contrast enhancement shows a very faint D1 AAV9 band at the height of the AAV9-lane bands (0.13 vs 0.07 for D1 with re-centred windows). It is a trace at most.
- The composite therefore shows one of three SCAR12 rescued lanes. The legend restricts L and M to lines "included in the sc-RNA-seq experiment"; I cannot check whether that explains the omission.

### Outside the composite
**1L**
- A very strong JH WT upper band at about 50 kDa, with a faint band just below it.
- Faint partial bands at the top strip edge in S2 and S5.
- No comparable upper band in LM-iPS or the AAV9 lanes.
- A black spot and a bottom dark line on the HSP90 strip.

**1M**
- Upper bands relative to WT (normalised): WT very strong (1), S1 0.21, D3 0.75, D3 AAV9 0.38. D1, S1 AAV9 and D1 AAV9 are about 0.03 or less.
- Faint top-edge signal in D1 and D1 AAV9, and a faint band under D3's upper band.
- Diffuse signal below the lower band in S1 AAV9 and D3 AAV9.
- High-molecular-weight signal at the top of the HSP90 strip.
- The upper band is strong in D3 but essentially absent in D1 (same genotype group by label), and present in S1 but absent in S1 AAV9. I cannot explain this from these files.

**Legend footnote.** It says "The specific WWOX bands are the lower 46kDa band and the upper band at ~48kDa". Its asterisk is attached in the text to panel (G), so whether it governs L and M is unstated. If it does, the composite omits specific signal. The printed values other than 7 fit the lower band alone.

### Clipping
- **1M HSP90 is clipped in all 7 lanes** (about 470-950 pixels at grey 0-5 per window). Normalisation there rests on saturated bands, and loading differences are probably compressed.
- **1M WWOX:** the WT upper band is at the black floor. D3 upper, D3 AAV9 upper and D3 AAV9 lower are near it, so D3 AAV9 may be underestimated.
- WT lower (minimum grey 31) and S1 AAV9 lower (47) are not clipped, so WWOX clipping does not explain the failure of 7.
- **1L:** the WT upper band has a few pixels at 0. WT lower is not clipped (minimum 24). WT and S2 HSP90 are near-black (12-13) but not clipped.

### What I cannot establish
- **Lane identity:** it rests on label order. Seven labels, seven HSP90 bands and the WWOX positions agree in page coordinates, but near-empty lanes are identified by position only.
- **Strips:** HSP90 and WWOX are separate cut strips with no uncropped membrane, so registration is unverifiable. The 1M HSP90 strip has no ladder.
- **1L co-migration:** WT lower peaks at pixel row 96, as do faint signals in S2 (97) and LM-iPS (95). The main band in LM-iPS and the AAV9 lanes sits higher (rows 78-86), and HSP90 shows no matching tilt. I cannot show it is the same species as the WT band.
- **1M co-migration:** a similar offset (WT about 103; S1 AAV9 94, D3 AAV9 80-89, D1 AAV9 about 90).
- **Ladder:** the printed 50 and 37 kDa labels sit at the top and bottom ladder blocks. The handwritten "50" and "37" on the 1M strip sit lower, so "46" vs "~48" cannot be settled.
- **Methods:** these pages give no densitometry method, normalisation formula or replicate number.
- **Image limits:** these are 8-bit JPEG exports of unknown linearity. I used rectangular windows, not fitted profiles, and optical density here is only a stress test.

