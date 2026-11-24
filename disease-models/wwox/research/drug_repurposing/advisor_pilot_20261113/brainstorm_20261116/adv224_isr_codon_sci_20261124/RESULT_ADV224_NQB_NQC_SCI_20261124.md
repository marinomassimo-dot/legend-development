# ADV-224 result: NQ-B (nine ISR readout genes) and NQ-C (per-codon pausing) (SCI, 2026-11-24)

Hypothesis level; reference genotype class; nothing here is medical advice. Pre-registration: `PREREG_ADV224_SCI_20261124.md` (digest in `PREREG_ADV224_SHA256.txt`, time in `PREREG_ADV224_TIME_UTC.txt`, 23:21Z; written before any nine-gene value or codon density was computed; the file was committed to the repository after the analyses because the worktree was locked by a running gate, the digest and time were fixed first). No receipt (no paper text read), no ledger or registry edit, no contact, no spend; one public processed archive downloaded (9.0 MB, no raw reads). Checkpoint AC, RP-045 and the sealed material untouched.

## 1. Answer first

| Question | Disposition | One line |
|---|---|---|
| NQ-B: the nine ISR readout genes of the OMA1 paper's Table 1 in Wwox-deficient neural tissue | **ALREADY CARRIED for five genes, ANSWERED for three, NOT RESOLVABLE for one** | Atf4, Ddit3 (Chop), Chac1, Eif2ak1 (Hri), Ppp1r15a are tabulated in `mouse_wwox_p17_it6_p4_20261029/results/key_genes.tsv` (IT6 P4, 2026-10-29; my loader reproduces all 35 of its centred values to 0.01). Newly tabulated here: Herpud1 and Eif2s2 (neither moves) and Fgf21 (not measurable). Dele1 is absent from the pinned annotation under any name. **No gene of the nine reaches a verdict of LOWER or HIGHER**; the set is not moved, as IT6 already said for its eleven-gene target set. |
| NQ-C: per-codon lysine pausing, GSE113751 | **NEEDS A SOURCE WE DO NOT HOLD for lysine; ANSWERED for the arginine codon statement** | The deposit has no lysine condition (arginine, leucine, rich medium only). The codon statement the dossier cites is about arginine and **is testable from the public processed tables**: under my frozen rule it reproduces in 1 of 3 cell lines (HeLa: CGT and CGC), not in HEK293T or HCT116; the same two codons lead the arginine-over-rich ratio in all three lines (post hoc). |
| PAPER 532 "WWOX added, not lost" line | **Record correction, not a claim-level correction candidate** | The record has "Claim links: none" and no claim in the registries cites the line; it is an identity-line edit for the registry route (proposal 1 in ADV-222 section 6). |

## 2. NQ-B in detail

Duplicate check first (what ADV asked): ADV-114 is the IT eIF2B reagent search, not a gene table. ADV-095 unit A tabulated an ISR set (ATF4, DDIT3, CHAC1 among 16 genes) in organoid data, not in these mouse tables. **IT6 P4 is the carrier**: ISR_targets (11 genes), ISR_core5, and a `key_genes.tsv` that names Atf4, Ddit3, Chac1, Eif2ak1 and Ppp1r15a per contrast with TPM per animal. Not in IT6: Fgf21, Herpud1, Dele1, Eif2s2. So the question as ADV worded it ("if the nine were already tabulated, stop") is half true: five were, four were not.

Method as frozen: one GEO sample = one animal (assumed, not verified); contrasts of IT6 P4 (H_S, H_N, H_null, C_S counted; CC_SW, CC_NW, CC_SN as noise floor); centred log2 ratio with 0.5 pseudocount, measurable if both arm means are at least 1 TPM; call LOWER or HIGHER only if centred |R| is at least 0.3 and the KO animals are separated from every control; gene verdict needs the same call in two hippocampal contrasts (or C_S plus one hippocampal), and is downgraded if a control-versus-control contrast also calls. Script `isr_nine_genes_adv224.py`, table `isr_nine_genes_adv224.tsv`.

| Gene | H_S | H_N | H_null | C_S | Verdict | Note |
|---|---|---|---|---|---|---|
| Atf4 (carried) | -0.16 | **-0.71 LOWER** | -0.39 | -0.51 | NOT RESOLVED | one separated call; sign lower in all four, as IT6 said (mRNA only) |
| Ddit3 / Chop (carried) | +0.71 | +0.12 | **-0.36 LOWER** | +0.15 | NOT RESOLVED | signs disagree |
| Chac1 (carried) | +0.42 | -0.03 | +0.17 | +0.07 | NOT RESOLVED | HIGHER in two control-versus-control contrasts: noise-prone |
| Eif2ak1 / Hri (carried) | +0.46 | **+0.40 HIGHER** | +0.02 | +0.20 | NOT RESOLVED | one call |
| Ppp1r15a (carried) | +0.91 | **+0.62 HIGHER** | +0.23 | +0.62 | NOT RESOLVED | higher in all four by sign; separated in one; two to three KO animals per arm |
| Fgf21 (new) | not measurable | not measurable | not measurable | not measurable | NOT MEASURABLE | below 1 TPM in every contrast (the highest arm mean is 1.2 TPM, H_S knockouts, against 0.03 in their controls) |
| Herpud1 (new) | +0.50 | +0.31 | **-0.58 LOWER** | -0.14 | NOT RESOLVED | one separated call, opposite sign to two hippocampal contrasts |
| Dele1 (new) | | | | | NOT MEASURABLE (annotation) | no transcript carries the symbol Dele1 or Kiaa0141 or the protein name in the pinned Ensembl release-92 headers; a gap of the key, not of expression |
| Eif2s2 (new) | +0.26 | +0.09 | +0.21 | +0.47 | NOT RESOLVED | LOWER in two control-versus-control contrasts: noise-prone |

Predictions: B1 (Fgf21 not measurable everywhere) held; B2 (none of Herpud1, Dele1, Eif2s2 moves) held; B3 (Herpud1 measurable everywhere) held. The RP-018 reading does not change: no newly tabulated gene receives a verdict other than NOT RESOLVED or NOT MEASURABLE. Caveats: two to four animals per arm; GEO sample = animal assumed; same laboratory and cohort family as the held single-nucleus data (not independent origins, ADV-068); composition differences (stage, glia) are not adjusted here; an mRNA table says nothing about eIF2 alpha phosphorylation or ATF4 protein, which is what the ISR question needs (ADV-131's open question). The few separated calls do not agree in sign across contrasts (Herpud1 and Ddit3 LOWER in H_null; Eif2ak1 and Ppp1r15a HIGHER in H_N; Atf4 LOWER in H_N), which is not the pattern of one coherent response; with two to three animals per arm this is a description, not a test.

## 3. NQ-C in detail

What the dossier claim rests on. Two claims, separate: (a) the **fly depletion**: untargeted metabolomics of fly heads (five pools of ten day-14 female heads per group; peaks 231 and 1665 identified against deposited reference standards; relative signal 0.47 and 0.52 of control in the LacZ background, 0.25 and 0.32 in the Abeta42 background; neither interaction passed the study's adjusted criterion; tissue extract intensity, not a free neuronal concentration; the dossier says so itself). It rests on the Brain Communications paper's Supplementary Table 4 and the MetaboLights deposit, and on nothing in GSE113751. (b) the **codon-level sentence** ("in human cells under arginine deprivation, elongation slowing affected two of the six codons for that amino acid"): it is about arginine, cites the ribosome-pausing paper, and the dossier itself states that neither study measures lysine added in WWOX. So the lysine premise has no ribosome-profiling support at all; GSE113751 cannot supply any.

Public processed tables: GSE113751 holds, per sample, a processed `codon.ribo.density` table (codon rows by positions -150 to +150) and a `cds.counts` table; samples are HEK293T (several lines and times), HCT116, HeLa in arginine starvation, leucine starvation and rich medium. Downloading it is lawful and free; no raw-read processing was done. Archive digest recorded in `GSE113751_RAW_SHA256.txt`.

Frozen rule: per codon, S = maximum of the density row over positions -10 to +10; SLOWED if S(arginine) over S(rich) is at least 1.5 and at least 1.5 times the leucine-over-rich ratio. Script `codon_density_adv224.py`, table `codon_density_adv224.tsv`.

| Cell line (3 h) | CGT | CGC | CGA | CGG | AGA | AGG | SLOWED count |
|---|---|---|---|---|---|---|---|
| HEK293T | 1.27 | 1.30 | 0.92 | 1.02 | 1.11 | 1.04 | **0** |
| HCT116 | 1.36 | 1.47 | 0.81 | 0.92 | 1.04 | 0.80 | **0** |
| HeLa | **1.80** | **2.18** | 1.03 | 1.06 | 1.00 | 1.00 | **2** |

(Ratio of S(arginine starvation) to S(rich); the leucine-over-rich ratios of CGT and CGC are 0.96 to 1.12 in all three lines.) Predictions: C1 (exactly two SLOWED codons in HEK293T) **rejected** (zero); C2 (same codons in HCT116 and HeLa) **rejected** (the sets differ: none, none, two); C3 (no lysine condition) held. Post hoc, labelled as such: CGT and CGC are the two highest arginine-over-rich ratios in every cell line, and the leucine control is flat at those codons, so the direction of the published statement is visible in all three lines but crosses my 1.5 line in one. The threshold and window are mine and were not tuned. Limits: the deposit's own normalisation; one sample per condition and line (no replicate, no p value); a density maximum is not a pause time; arginine starvation of cancer-derived lines says nothing about WWOX; the 6 h HEK293T arginine sample shows CGT 1.72 and CGC 1.74 over the 3 h rich sample, not like-for-like.

What this means for the lysine hypothesis: nothing for lysine, and that is the point. The decisive observation the dossier asks for (charged lysyl-tRNA, absolute amount, protein synthesis, arginine use under lysine addition in a WWOX system) is not supplied by any public table found in this pass. **Source we do not hold:** a ribosome-profiling or charged-tRNA measurement under lysine limitation (none located here, not searched beyond the deposit's own file list), and a WWOX-deficient neural system measured the same way.

## 4. PAPER 532

One line: the identity line "WWOX added, not lost" is wrong as a description of the arms (the preprint also has WWOX-lowering arms; ADV-222 section 6, proposal 1), but because the record carries "Claim links: none" and no claim in the registries cites it, it is a record-level edit for the registry route, not a claim-level correction candidate. I made no edit.

## 5. What surprised me

That the two questions had opposite fates: the nine-gene table I was ready to build was mostly already built four weeks ago (IT6 P4, 2026-10-29) and reproduces to the third decimal from the same files, while the codon question was cheaper than I expected (a 9 MB public archive, not raw reads) and gave a partial answer: the statement the lysine dossier leans on is only borderline reproducible from the deposit's own processed density, in one cell line of three.

## 6. Limits

Public processed tables only; no raw-read processing; no replicate; thresholds fixed by me before the data; the nine-gene verdicts are mRNA from two to four animals per arm and say nothing about ISR activation; Dele1 could not be resolved with the pinned annotation (a newer annotation might); the identity-line judgement rests on a grep over the registries, not on a claim-by-claim read; no blind recheck run.

## 7. Files in this folder

`PREREG_ADV224_SCI_20261124.md` (+ digest, time) · `isr_nine_genes_adv224.py` · `isr_nine_genes_adv224.tsv` · `codon_density_adv224.py` · `codon_density_adv224.tsv` · `GSE113751_RAW_SHA256.txt`.

## 8. DREAM line

Changed: the nine-gene question is closed (five carried, three answered not moved, one annotation gap); the arginine codon statement has a measured, partial reproduction; the lysine premise is recorded as having no ribosome-profiling support. Consumer: ADV (stop spending on ISR mRNA tables; the missing observation is protein/phospho-level), IT (PAPER 532 identity edit), the lysine dossier owner (the codon sentence can carry the measured wording above). Nothing here moves a scientific claim.
