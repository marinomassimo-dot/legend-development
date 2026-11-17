# T6 (Villani 2026, phage-encoded DNA ligase; NEGATIVE CONTROL) — my own first pass, written BEFORE the blind reader's answer

Written 2026-11-17 on the shuffled input (blind_input.md sha256 fed02a042db6c82584adbb8c2c46a44f12022e5d163201e6fee8a2062aedcdba); key file hash 8644a48c0109e3db17bedbc9b072ee31cb1dbe0378ded0ccd900a5c7f313e5cb.
Disclosure: before writing this pass I ran a keyword listing that printed the arm label next to each ligase or end-joining statement, so this pass is NOT blind to the arm for those 14 statements. The judgements below follow the statement text and the frozen rule only; the reader (who sees no arm) is the scorer.

Strict rule (a phage-encoded DNA ligase, alone or inside a Ku/ligase end-joining module, joins the nuclease-cut ends, with a loss of survival when it is deleted and an end-joining-type indel scar at the repaired site): by text, Z05, Z06, Z22, Z37, Z54, Z56 = 6 of 60 (Z05 says "phage- or host-encoded", the weakest). 
Ligase religation with a scarless wild-type site (Z19, Z30, Z57): ligase lever, but the predicted sequence is wild type, not an end-joining scar: strict NO, loose and lever-class YES.
Host-driven microhomology end joining (Z51): not phage-encoded: loose borderline, strict NO.
Resection or annealing without a ligase lever (Z01, Z07, Z27, Z47): not strict.
Loose and lever-class counts over all 60 (any phage repair or end-joining activity, including recombinases and annealases): not hand-counted; the frozen rule uses the reader's counts.
Memory probe: negative on the finding (it names no study) but it states a ligase resealing as a plausible mechanism after its question named the ligase; scored in RESULT_T6.md.
