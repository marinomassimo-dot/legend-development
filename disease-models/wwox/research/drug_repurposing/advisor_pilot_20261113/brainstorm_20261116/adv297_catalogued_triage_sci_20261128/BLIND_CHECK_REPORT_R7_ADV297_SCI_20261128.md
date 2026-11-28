# ADV-297 blind check of record 7 (the one MISS candidate)

legend-delegate, claude-sonnet-5-5, effort high on 4 of 4 turns; it saw only the packet (sha256 3e1a63d460037910c46f4bc833ec97d9b9beeb18ead8bffc42663ad8e1033254; held sentences with context, source passage, rule; not step A, not the first reader) and the paper text. Items H1..H6 are the first reader data D1 (H1, H2), D2 (H3), D3 (H4, H5), D4 (H6). Model output, hypothesis level, not medical advice; saved verbatim, not edited.

---

BLIND CHECK, PMID 25662954 (PMC4374002). I read only PACKET.md and paper_25662954.txt, wrote no file, and found no instructions in the paper text that I needed to act on. Line numbers below are from /home/desktop/.claude/jobs/fc428159/tmp/adv297/blind7/paper_25662954.txt. This is hypothesis-level research, not medical advice.

| Item | Verdict | Evidence level of the datum | Does the paper's text disagree with its own table? |
|---|---|---|---|
| H1 | YES (weak) | stated without data | no table involved |
| H2 | NO | stated without data (retinal activity); commentary on another group's work | no table involved |
| H3 | YES | aligned and modelled in silico | no table involved (the figure legends have a motif-name inconsistency) |
| H4 | YES | shown data with error, n at least 3 (ITC) | yes |
| H5 | YES | shown data with error, n at least 3 (ITC) | yes |
| H6 | YES | shown data with error, n at least 3 (ITC), peptide only | yes |

**H1: YES (weak)**
- Quote, line 92: "While still in preliminary stage, biochemical studies conducted on a high-quality bacterially-purified recombinant protein in my laboratory indeed confirm that the SDR domain of WWOX is a bona fide retinal oxidoreductase—not only does it catalyze the oxidation of retinol to retinal aldehyde but it also appears to efficiently catalyze the reversible reaction." The same line adds that the domain "may also be involved in the oxidative catalysis of retinal to retinoic acid."
- This is the author's own reported observation. It affects the first clause, "has rested on one laboratory's crude-extract enzymology". It does not affect what the sentence says about the binding measurement.
- Changed sentence: "**Why it matters:** the corpus's SDR reading has rested on one laboratory's crude-extract enzymology; a second laboratory (Farooq, PMID 25662954) states, without showing any data, that preliminary assays on bacterially purified recombinant protein find retinol/retinal oxidoreductase activity, an unverified catalytic statement. This is an independent measurement **on the same region** that is nevertheless **not** enzymology, so it raises the SDR's standing as a *binding* surface and adds nothing to its standing as a *catalytic* one."
- Limits: no rate, Km, cofactor condition, replicate or control is given. The construct is not specified (SDR domain alone or full length).
- If the caller's bar is that only data shown can change a sentence about what the corpus "has rested on", this becomes NO. Under the packet rule, which allows "reported" observations and a change of evidence level or scope, I judge it YES.

**H2: NO**
- Condition 3 fails. The held sentence describes one specific reading (PMID 21476439: steroid substrates, apparent Km, crude extract, no purified-protein binding). The review's own retinal statement (line 92) concerns a different substrate class. It gives no binding constant, Km or stabilisation datum, so nothing in the sentence changes.
- The review's criticism of the steroid study fails condition 1, because it is commentary on another group's work. Line 88: "this analysis was conducted in whole cell lysates in lieu of an isolated recombinant protein".
- Side flag: the review says "whole cell lysates", while the held sentence says "bacterial crude extract". I cannot settle this without PMID 21476439, and the review's description is second-hand.

**H3: YES**
- Quotes, line 92: "the GXXXGXG motif that is involved in accommodating the NADP+/NADPH cofactor, while the YXXXK consensus sequence represents the active site motif"; "an absolutely conserved serine (S260 in WWOX) is required for the stabilization of retinoid substrate".
- Line 96: "The YXXXK active site motif, where Y and K are respectively Y293 and K297". Line 98: "Y293 and K297 active site residues act as general acid and base".
- Line 158: the SDR structure is a "structural model ... built in several stages using the MODELLER software based on homology modeling".
- A text search finds no "S281" or "Ser281" and no "Q230". The cofactor named for WWOX is NADP+/NADPH, not NAD. The cited source is a homology model and alignment, not an experimental structure.
- Changed sentence (only the first part changes; the text from "Gln→Pro" onward stays): "**Catena di ragionamento**: Q230 cade nel **dominio SDR**, ma non è fra i residui catalitici nominati dalla fonte: PMC4374002 (review; allineamento di sequenza e **modello per omologia in silico**, non struttura sperimentale) indica S260 (stabilizzazione del substrato retinoide), la **diade Y293/K297 del motivo YxxxK** (catalisi) e il motivo GxxxGxG per il cofattore **NADP+/NADPH**; **non nomina S281**. Q230 è quindi presumibilmente **strutturale**, non catalitico → ..."
- The paper does not itself say that Q230 is non-catalytic. That remains an inference from its absence from the named residues.
- Internal inconsistency: the legends of Figures 7 and 8 (lines 158, 160) say "RXXXK", while the body and the Figure 6 legend say "YXXXK". Line 158 also says "YXXXK" later in the same legend.

**Table 1 basis for H4 to H6**
- Lines 162-174: apparent Kd in µM, WW1 alone against the WW1-WW2 tandem, ITC at 25 °C and pH 7, "at least three independent measurements", one SD.
- Recomputed ratios (approximate propagated error):

| Peptide | WW1 / WW1-WW2 (µM) | Fold |
|---|---|---|
| p73 | 107±9 / 60±6 | 1.78±0.23 |
| ErbB4 | 179±10 / 75±8 | 2.39±0.29 |
| TMG2 | 202±23 / 84±9 | 2.40±0.38 |
| WBP1 | 368±44 / 141±12 | 2.61±0.38 |
| WBP2 | 133±18 / 42±7 | 3.17±0.68 |
| PTCH1 | 278±19 / 79±8 | 3.52±0.43 |
| PTPN14 | 763±62 / 214±30 | 3.57±0.58 |
| SMAD7 | 272±29 / 53±8 | 5.13±0.95 |

- Rule 1: line 56 calls p73, PTCH1, PTPN14, SMAD7 and TMG2 "our recent biophysical analysis ... (unpublished observations)", so those rows are this paper's own. ErbB4 and WBP1/2 are attributed in the text to earlier publications (refs 14, 32) and do not count as new data here.
- Disagreement: line 56 says WW2 enhanced binding for those five new ligands "between two- to three-folds". Their own table rows give 1.8 to 5.1.

**H4: YES**
- The range "2-3×" widens, and the new rows alone are enough to widen it.
- Changed sentence: "WW1 **nel modulo tandem** lega più forte che da solo, con un intervallo più ampio di 2-3×: **1,8-5,1×** sugli otto peptidi PPXY della Tabella 1 di PMID 25662954 (ITC; i cinque dati nuovi: p73 1,8×, TMG2 2,4×, PTCH1 3,5×, PTPN14 3,6×, SMAD7 5,1×), con **guadagno entropico** (dalla fonte dell'entry; la Tabella 1 riporta solo Kd)."
- The review gives no ΔH or TΔS. Its entropic remark (line 64) is a conjecture, so it adds nothing to the entropic clause.

**H5: YES**
- All the Table 1 peptides carry a single PPxY motif, yet the tandem still binds more tightly than WW1 alone. The held sentence states the improvement for "dual PPxY-containing partners", so its scope widens.
- Changed sentence (second sentence of the Summary): "Cooperative WW1–WW2 architecture improves recognition not only of dual PPxY-containing partners but also of single-PPxY peptides (about 1.8- to 5.1-fold lower apparent Kd for WW1-WW2 than for WW1 alone; ITC on 12-mer peptides, PMID 25662954 Table 1)."
- This does not show WW2 occupancy and says nothing about variants. The rest of the Summary stays as it is.

**H6: YES**
- Line 170: "SMAD7 LESPPPPYSRYP 272 ± 29 53 ± 8".
- The premise "WWOX is a WW protein that binds PPXY" gains a direct in vitro measurement on the SMAD7 motif. The competition hypothesis stays untested.
- Changed sentence: "WWOX è una proteina a dominio WW che lega PPXY, e **per il motivo di SMAD7 il legame è misurato in vitro**: peptide LESPPPPYSRYP, Kd apparente 272 ± 29 µM con WW1 e 53 ± 8 µM con il tandem WW1-WW2 (ITC, 25 °C, pH 7, almeno tre misure; PMID 25662954, Tabella 1). **Ipotesi competitiva mai testata qui: WWOX stabilizza Smad4 competendo con Smurf per gli stessi motivi PPXY.** `IPOTESI`: la competizione con Smurf, il legame con le proteine intere in cellula, il legame con Smad2 e l'effetto su Smad4 non sono misurati."
- "Qui" and "questo paper" in the held text refer to the entry's own source, which stays true. The affinity is weak (tens of µM) and measured on a peptide only. Line 56 says "two- to three-folds", but SMAD7 is 5.1-fold.

**What I could not assess (source not provided)**
- PMID 21476439, the other measurement discussed in H1, and the repository note of 2026-10-20 (H1, H2).
- PMID 37248434 itself (H1).
- Whether S281, NAD or the Q230 interpretation in H3 come from another source, and the working-model statement H3 cites.
- Figure images: only legends are in the text file, so I could not check what the Figure 6 alignment shows at S281 or Q230.
- PMID 25703206, so I do not know which ligands or fold values the H4 sentence was based on.
- CLAIM 024's other sources, which may already cover single-PPxY enhancement (H5).
- The source paper of DL-MECH-113 (H6).
- Refs 14 and 32, and whether the unpublished Table 1 rows or the retinal assays were published elsewhere or already recorded in the corpus.


