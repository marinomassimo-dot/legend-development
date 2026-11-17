# Family-first cue step, stage 0 (tuned-on T7, tool-free): result (HE; 2026-11-17; non-canonical; not medical advice)

**CANDIDATE STEP, DEVELOPMENT ON A TUNED-ON TARGET: no claim of improvement.** Written for: ADV, SCI (scores her own forecast: hash `afdab1474c0154f42ffbcdf5c0291d8b6170a7bc40b0b563ff5c2990fe78405d`, written 08:52:17Z before any run). Frozen: `FREEZE_FAMILY_FIRST_CANDIDATE.md` sha256 1b88c3c73026dccefa3c2957b8681c55249560aaf83fb3228ec33af472316c9a; prompt template sha256 9fd8a13233bf3255f226865663886faaea0313e98afb3ebe0460387ee5a77d4c; composed T7 prompt sha256 caf884f850eae15cb81225448834b7800719c76e7d3558a1e880e773501cf725; ADV's 'go' on stage 0 with a cap of 62,000 tokens.
## Runs (two tool-free delegates, sonnet, `legend-deepdive`, same composed prompt; nothing changed between runs)
| run | tokens | tool calls |
|---|---|---|
| FF1 | 29,729 | none |
| FF2 | 29,744 | none |
Total **59,473 tokens** (estimate 60k; cap 62,000; the cumulative development steps are 87,817 + 59,473 = 147,290, under ADV's 150k); no usage-limit message. Outputs verbatim: `OUT_FF1.txt` e2d92a2b, `OUT_FF2.txt` f726d23c.
## Result (scored by me, mechanically and by reading; not blind)
| item | FF1 | FF2 |
|---|---|---|
| zinc (Zn2+) anywhere in the output | **0 mentions** | **0 mentions** |
| STRICT (zinc lowering in MODULATORS and carried to STEP C or the 15) | NO | NO |
| LOOSE (zinc lowering in MODULATORS, any family) | NO | NO |
| zinc in the 15 hypotheses | no | no |
| related families named | other receptor GCs (GC-A/B/D/E/F/G), soluble GC, adenylyl cyclases (plus the protein kinase / pseudokinase fold, PDEs and effectors as pathway components) | other receptor GCs, adenylyl cyclases and soluble AC, soluble GC, the pseudokinase / kinase fold (plus PDEs, MRP4/5, PKG as pathway components) |
| metal-ion modulators listed | Mg2+, Mn2+ (as cofactors, Mn2+ higher), Ca2+ (GCAP and AC modulators; sGC) | Mg2+, Mn2+, Ca2+ |
| MODULATORS table rows (lines starting with a pipe, counting headers) | 77 | 61 |
| STEP C states the defect as a GAIN of function and says which entries would not correct it | yes | yes |
**The idea is closed at this stage: a family-first cue (the closest related families named, every known modulator of any member listed with its direction) did not make the model list zinc as a modulator of the receptor guanylyl cyclase family or of adenylyl and soluble guanylyl cyclases, in either of two runs, although the same model knows zinc inhibits cyclases (T7 probe) and lists zinc when it is in view (C2M run B1).** SCI's forecast (hashed before the run) is scored by her; this file is held out of the repo until she says she has scored. My own stage-1 prediction in the freeze (FF names the atom's member in the table 45 percent per target) did not come true on T7.
## What it says, and what not
Combined with the C2M trial (zinc not volunteered from a class named by an enumeration), this is a second negative on T7 with a different cue: the model reaches for Mg2+, Mn2+ and Ca2+ as the metal modulators of cyclases and does not volunteer zinc, in four of four uncued runs (C2M A1 and A2, FF1 and FF2), and keeps it in the one run where it was in the input (B1). The gap is retrieval of a member that is not in view, not specification of the class and not a missing neighbouring family: the prompt did name the right neighbours (adenylyl cyclases, sGC), and the model listed their Ca2+, Mn2+, P-site and forskolin-class modulators, but not zinc. Limits: one target (tuned-on), two runs, scoring by me (not blind), mechanical zinc count over text; the prompt asks for a very wide table, which may dilute the tail entries; a different neighbour family or a narrower question per family (zinc, copper, iron, calcium as 'ions of the family') could still surface it, which this stage-0 does not test and the frozen design does not include.
