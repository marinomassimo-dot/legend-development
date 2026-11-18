# T9 (dopamine transporter deficiency, off-defect): run record and result — RETRODICTION BY ABSENCE FROM THE CORPUS, NOT BY DATE (HE; 2026-11-17; non-canonical; not medical advice)

Written for: ADV (and SCI for the independent forecast, scored after both targets). Frozen: `../FREEZE_THIRD_SET_PART_B.md` (sha256 8920ac510a50d9e918f0ace03128bf310ce22faebecce42e9a788a217c7afb47), `../AMENDMENT_B1.md`, briefs `../briefs3/SHA256_BRIEFS.txt`. T7 was scored before T9 started; nothing of T9 is read into T7.
## Runs (REDUCED-SEQUENTIAL: v3 and v4, two replicates each, no baseline; sonnet, `legend-deepdive`, one at a time)
| step | tokens | tool calls | path audit from the transcript |
|---|---|---|---|
| v3 stage 1 A / B | 24,186 / 24,260 | none | zero file-tool calls |
| v3 stage 2 A / B | 153,916 / 171,537 | 15 Read, 1 Glob, 29 Grep / 12 Read, 2 Glob, 35 Grep | only the cut and the one S1 file |
| v4 stage 1 A / B | 30,714 / 27,655 | none | zero file-tool calls |
| v4 stage 2 A / B | 146,819 / 162,526 | 13 Read, 1 Glob, 34 Grep / 13 Read, 1 Glob, 35 Grep | only the cut and the one S1 file |
| blind reader (Z01-Z40, seed 20261202; key hashed first) | 32,200 | 2 | read only its input |
Total **773,813 tokens** (estimate about 600k; stage 2 ran above its 110-130k estimate, 147k to 172k, because the corpus held more on dose windows and chaperone routes); no usage-limit message. The selection probe and audits (M070) are not in this figure. Reports verbatim in this folder; sha256 prefixes: `V3_S1_A` e6c4997b, `V3_S1_B` 053ad561, `V3_S2_A` 39595083, `V3_S2_B` f9676cb8, `V4_S1_A` 65a8b78a, `V4_S1_B` c6441ecc, `V4_S2_A` c6fccf98, `V4_S2_B` 1b2beef4, reader answer `READER.txt` cf66a117; blind input 64d2ef23…; key `blind_key.json` a1d1f6542adf7d31a58d5e59f0983d516c580ecbd42b5529ff8676aa7085d1dc (hashed before the reader ran); my first pass `MY_FIRST_PASS_T9.md` 4423939e… (before the reader's answer, without arm labels).
Builder notes: the blind input needed the same tail patterns as T7; one run's final-ten text ended with an S1 classification table that the builder first folded into the last block of the shuffle; I removed it from that block only before my first pass and before the reader (the key and the 40 sections are unchanged); stage-1 tokens were replaced by 'a rival'.
## Result (blind reader, unblinded through the key; each cell = YES count over the 10 hypotheses of that run)
| condition | QS1 strict (synthesis inhibition lowers hyperactivity) | QS2 strict (amphetamine-type releaser) | QL loose (any off-carrier tone lowering) | QN1 chaperone or proteostasis lever ranked as a rescue | QN2 methylphenidate-type blocker |
|---|---|---|---|---|---|
| v3 A / B | 1 / 1 | 0 / 0 | 1 / 2 | 3 / 2 | 0 / 0 |
| v4 A / B | 1 / 1 | 0 / 0 | 2 / 2 | 3 / 2 | 0 / 0 |
Totals: QS1 2 of 20 (v3) and 2 of 20 (v4); QS2 0 / 0; QL 3 and 4; QN1 5 and 5; QN2 0 / 0. **Every one of the four runs carries the synthesis-inhibition lever (a tyrosine hydroxylase dosage or rate-limiting-enzyme reduction) with a predicted fall of the hyperactivity and an unchanged carrier.** My first pass counted QS1 = 4 hypotheses (same four), QS2 = 0, loose 7 (the reader counted 7 loose in all: 3 + 4), and for negative atom 1 two clear plus three conditional of 40 against the reader's 10 (the reader also counted four ERAD or chaperone-route hypotheses and two conditional ligand hypotheses as rescues).
Predictions committed first: v4 reaches (i) or (ii) in at least one replicate 25 percent: occurred (both replicates); v3 10 percent: occurred (both replicates, a miss of my prediction); chaperone ranked as a rescue lever in v4 60 percent: occurred (5 of 20 hypotheses, equal to v3).
## QY and QX (scored by me from the printed files, not blind)
| point | v3 A / B | v4 A / B |
|---|---|---|
| enumeration block: synthesis lever (tyrosine hydroxylase flux, 'synthesis-enzyme dosage') | no enumeration | yes / yes |
| enumeration block: Zn2+ (a DAT-specific Zn2+ site) | – | yes / yes (axis a) |
| the 15 of stage 1: a synthesis-lowering hypothesis | yes / yes (A H9, B H12) | yes / yes (A H8, B H9) |
| the 15 of stage 1: psychostimulant or amphetamine words | yes (as evidence lines and a paradoxical serotonergic lever) in both | yes in both |
| the 15 of stage 1: an amphetamine-type releaser as a lever | no / no | no / no |
| final ten: synthesis lever | yes / yes | yes / yes |
| final ten: releaser lever | no / no | no / no |
Atom (i) was present in the 15 of stage 1 of v3, WITHOUT an enumeration step, and survived to the final ten in all four runs: the model reaches it from memory (the paper itself notes both levers are known in DAT knock-out mice). Atom (ii) (amphetamine as a lever) was never proposed as a lever by any run; the paradoxical-stimulant fact appears only inside a serotonergic hypothesis of stage 1 that stage 2 dropped in all four runs. QX, axes named by the final tens (keyword lists fixed in `axis_coverage.py`): v3 5 and 5 (mean 5.0); v4 4 and 5 (mean 4.5); the 15 of stage 1: v3 5 and 5, v4 6 and 7; both ENUMERATION blocks name all 7.
## What it says, and what not
T9 does not separate v4 from v3: both reach atom (i) in both replicates, and neither reaches atom (ii); the chaperone false-positive rate is equal (5 of 20). The reading is a MEMORY route: the lever has knock-out precedent that the model knows, so v3 stage 1 already proposes it, which is the limit written in amendment B1; the enumeration step adds nothing visible here, and its axis spread of the final ten is not wider on this target. Limits: one target, one blind reader on four runs, a probe that did not show the knock-out knowledge but a result that does, two atoms of which one is reachable from memory.
