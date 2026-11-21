# ADV-132 parity rule (IT, 2026-11-21): a mechanical number, name, negation and hedge check, written BEFORE it is run

Reference-genotype class only; page text; nothing here is medical advice. No model takes part: the check is a script (`parity_check.py`) with the fixed rule below. It compares a source passage (English) with one rendering (fr, de or es) and flags a row; a flag is not a verdict, each flag is then classified by hand as FALSE POSITIVE (the two texts agree, the rule is too crude) or REAL DRIFT (the rendering differs from the source), with the reason.

## Tokens compared (per row, as multisets: a count matters)
1. NUMBERS. Normalisation first: NFC; non-breaking and thin spaces and ordinary spaces inside a digit group removed (`10 000` is `10000`); a decimal comma becomes a point (`57,3` is `57.3`); a leading minus or en dash glued to a number and not preceded by a digit or letter is a sign (`-52`), otherwise it is a range mark. Tokens: every number (with its sign) as a string.
2. UNITS. A number directly followed (optional single space) by a unit of this fixed list is one token `number+unit`: pA nA uA mV ms Hz kHz uM mM nM mg kg ug ng mL uL mm um nm kDa Da bp kb % (the micro sign is read as `u`; `degrees C` is `C`). The words percent, pour cent, Prozent and por ciento after a number count as `%`.
3. P-VALUE AND COMPARATOR FORMS. `p`, `P` followed by `=`, `<`, `>` or the symbols for at-most and at-least, and the numbers after it, are one token (`p<0.05`); a bare `<`, `>`, at-most and at-least sign is a token.
4. SYMBOLS (gene, protein, compound, variant, assay names), by maximal tokens of letters, digits and underscore: (a) a token that holds both a letter and a digit (`GluN2B`, `NKCC1`, `Q230P`, `ATF4`, `eIF2`, `1alpha`) is one symbol; (b) in any other token, every run of two or more capital letters (`NMDAR`, `GABA`, `TTX`; in `sIPSC` and `IPSCs` the run `IPSC`) is one symbol; (c) a token with an underscore (`E_GABA`) is one symbol. Rule (a), (b), (c) multisets are compared both ways.
5. NAMES. A capitalised token of the SOURCE that is not the first word of the passage or of a sentence or a clause after a colon (`Wwox`, `Breton`, `Wnt`, `Tau`, `KCl`) must appear in the rendering (case-insensitively, as a whole token or as a part of a hyphenated or compound token). One direction only (German capitalises every noun).
6. NEGATION AND HEDGE CUES, counted by category. Fixed lexicons (lower case, whole word):
   * EN negation: not, no, never, none, cannot, nothing, without, neither, nor, nobody, nowhere. EN hedge: may, might, would, could, possibly, perhaps, probably, likely, about, approximately, roughly, apparently, unknown, unclear, presumably.
   * FR negation: pas, non, aucun, aucune, jamais, sans, ni, rien, nullement. FR hedge: peut, peuvent, pourrait, pourraient, probablement, vraisemblablement, environ, approximativement, apparemment, inconnu, inconnue, inconnus, incertain, plus any word ending in `rait` or `raient`.
   * DE negation: nicht, kein, keine, keinen, keinem, keiner, keines, nie, niemals, nichts, ohne, weder, noch (only when preceded by `weder`). DE hedge: kann, können, könnte, könnten, würde, würden, wahrscheinlich, vermutlich, etwa, ungefähr, ca, unbekannt, unklar, möglicherweise, vielleicht.
   * ES negation: no, ningún, ninguno, ninguna, nunca, jamás, sin, ni, nada, nadie. ES hedge: puede, pueden, podría, podrían, probablemente, aproximadamente, aproximado, desconoce, desconocido, desconocida, desconocidos, incierto, quizá, quizás, presumiblemente, plus any word ending in `ría` or `rían`.
   The number of negation cues and the number of hedge cues in the source and in the rendering are compared as two integers. A prefix negation (`un-`, `non-`, `in-`) is not a cue in the source, so a rendering that translates it with a cue word (`non apparentés` for `unrelated`) is expected to flag: classify it as FALSE POSITIVE when the source word is prefix-negated.

## Fail condition
A row FAILS (is flagged) if any of: the multiset of tokens of 1, 2 or 3 differs; the multiset of symbols (4) differs; a name of 5 is missing; the negation count or the hedge count differs. The flag names the token or category that differs.

## What the check does not see
Meaning, scope, attachment of a modifier, a hedge or negation expressed in a way not in the lexicon, a changed quantifier (`any`, `all`, `at least`), a wrong referent. It is a floor under the blind check, not a replacement for it.

## Procedure
Run `parity_check.py` on the 150 existing ADV-131 rows (50 passages x fr, de, es, as they stand in the catalogue now); classify every flag by hand with the reason; then run it on every row of the ADV-132 batch before and after the blind check. The rule is not edited after the first run; a rule change is a new rule with its own record.
