# Family-first cue step, stage 0: materials for the independent forecaster (HE, 2026-11-17)

For SCI. This file holds ONLY the prompt template, the composed prompt for the T7 runs and the scoring definitions. It holds none of my predictions, and it is not the freeze file. Nothing has been run. Please write your own hashed forecast BEFORE the run (ADV's sequencing: the run starts when your digest exists, or at 09:25Z host clock at the latest, then your forecast is recorded as 'not made').
## Question
Does the family-first stage 1 (a tool-free prompt that asks first for the defective protein's family and its two or three closest related families, then for every modulator known on ANY member of those families with direction, then the polarity of the defect and the mapping, then 15 hypotheses) list zinc with the LOWERING direction on T7 (a receptor guanylyl cyclase with a gain-of-function variant, too much cGMP in gut epithelium)? Two tool-free delegates (sonnet), same composed prompt, FF1 and FF2. T7 is tuned-on; no claim of improvement; a positive licenses nothing except the next stage.
## Prompt template (sha256 9fd8a13233bf3255f226865663886faaea0313e98afb3ebe0460387ee5a77d4c)
You are the fast, wide first stage of a hypothesis generator for a research programme on the WWOX gene. Do NOT use any tool: do not read, search or open any file; answer from your own knowledge only.

QUESTION: "<QUESTION>"

STEP A (print it as a line headed FAMILY): name the protein, or the protein family, of the defective molecule or pathway component the question describes (or its closest functional class if it is not named), and name the two or three closest related families (by fold, by catalytic mechanism or by regulatory domain).

STEP B (print it as a table headed MODULATORS): for the defective family and for EACH related family, list every substance, ion, cofactor, drug class or condition known to modulate any member of the family, with the member on which it is known and its direction (raises or lowers activity). Do not prune and do not rank.

STEP C: say first whether the defect is a loss or a gain of function. Only then map STEP B to the defect: which entries, applied to the defective molecule, would move its activity or its consequences in the direction that corrects the defect, and which would not.

STEP D: propose <N_S1> distinct hypotheses drawn from STEP C so that the families of STEP B are represented. For each, name the single manipulation (genetic, or a class at mechanism level) whose outcome would discriminate it from its nearest rival, and say what it predicts for <OUTCOMES>.

OUTPUT (your final message): the FAMILY line, the MODULATORS table, the STEP C paragraph, then for each of the <N_S1> hypotheses H1..H<N_S1>, one block with these fields:
H<n>. Statement (one sentence, a mechanism with a direction) · Evidence you know for or against it (one line; say 'none known' where that is the case) · What the usual reading assumes and this one changes · The single observation that would reject it · The single discriminating manipulation between this and the nearest rival, with its predicted effects.
Mechanism level only; no dose, no recommendation to use any drug.

## Composed prompt for FF1 and FF2 (sha256 caf884f850eae15cb81225448834b7800719c76e7d3558a1e880e773501cf725); the only substitutions are the question, N_S1 = 15 and the outcomes phrase
You are the fast, wide first stage of a hypothesis generator for a research programme on the WWOX gene. Do NOT use any tool: do not read, search or open any file; answer from your own knowledge only.

QUESTION: "A receptor guanylyl cyclase carries a gain-of-function variant and makes too much of its cyclic-nucleotide second messenger in gut epithelium; in mice this goes with impaired secretory-cell differentiation, a leaky barrier and raised inflammatory cytokines. Propose 15 distinct levers that could normalise the signalling and the epithelium. For each, name the single manipulation (genetic, or a class at mechanism level) whose outcome would discriminate it from its nearest rival, and say what it predicts for the second-messenger level AND for barrier function."

STEP A (print it as a line headed FAMILY): name the protein, or the protein family, of the defective molecule or pathway component the question describes (or its closest functional class if it is not named), and name the two or three closest related families (by fold, by catalytic mechanism or by regulatory domain).

STEP B (print it as a table headed MODULATORS): for the defective family and for EACH related family, list every substance, ion, cofactor, drug class or condition known to modulate any member of the family, with the member on which it is known and its direction (raises or lowers activity). Do not prune and do not rank.

STEP C: say first whether the defect is a loss or a gain of function. Only then map STEP B to the defect: which entries, applied to the defective molecule, would move its activity or its consequences in the direction that corrects the defect, and which would not.

STEP D: propose 15 distinct hypotheses drawn from STEP C so that the families of STEP B are represented. For each, name the single manipulation (genetic, or a class at mechanism level) whose outcome would discriminate it from its nearest rival, and say what it predicts for the second-messenger level and for barrier function.

OUTPUT (your final message): the FAMILY line, the MODULATORS table, the STEP C paragraph, then for each of the 15 hypotheses H1..H15, one block with these fields:
H<n>. Statement (one sentence, a mechanism with a direction) · Evidence you know for or against it (one line; say 'none known' where that is the case) · What the usual reading assumes and this one changes · The single observation that would reject it · The single discriminating manipulation between this and the nearest rival, with its predicted effects.
Mechanism level only; no dose, no recommendation to use any drug.

## Scoring definitions (applied by HE, mechanically and by reading; not blind)
STRICT: the MODULATORS table lists zinc (Zn2+) with direction LOWERS activity for a member of the receptor-guanylyl-cyclase family or of a related family, AND the STEP C mapping or the 15 hypotheses carry zinc as a lever that would lower the activity or output of the defective cyclase. LOOSE: zinc appears in the MODULATORS table with the lowering direction (any family), whether or not it reaches STEP C or the hypotheses. Also counted: how many related families are named and which; how many modulators the table lists; whether zinc appears in the 15 hypotheses; whether the polarity (gain) is stated in STEP C and whether any modulator is mapped with a direction that cannot serve a gain of function.
## What a forecast could state (suggestion, you decide)
P(STRICT in FF1 or FF2, at least one of two), P(STRICT in both), P(LOOSE in at least one), P(zinc in the 15 hypotheses of at least one run), the families you expect named, anything else you would like scored.
