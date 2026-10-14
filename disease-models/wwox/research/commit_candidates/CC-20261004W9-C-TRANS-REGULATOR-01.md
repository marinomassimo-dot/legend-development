# CC-20261004W9-C-TRANS-REGULATOR-01 — a *trans*-acting splicing pathway that lowers Wwox transcript: what the panel shows and what the citation does not

`context_policy: SOURCE_FIRST`. **Author:** ACTOR_ID `scientist`, Scientist C of intake wave 9,
2026-10-04. **Change class: MINOR** (one research-line record; narrows no `consolidated baseline`
claim). **Nothing here is medical advice.**

Source: PMID 42770556 (`FTR-20261004-42770556-01`, manifest PASS). The dossier for this paper was
not written: the write was halted by a model safety classifier and the halt is recorded in the
receipt and in the wave note. The reading itself is carried by the manifest and this candidate.

## 1 · Finding

In mouse cranial neural crest cells, loss of PRMT1 or knockdown of the splicing factor SFPQ raises
intron retention in long genes with long introns, and the retained-intron transcripts are degraded
by nonsense-mediated decay. **Wwox is named as one of those genes** — 913 kb with a 639 kb retained
intron — and the Discussion states it shows increased retention of introns 3 and 4 with decreased
expression on either perturbation. This is the first *trans*-acting candidate regulator of WWOX
transcript level the model would hold.

**Three measured qualifications, all from this source:**

1. **The panel does not mark the abundance fall for Wwox.** In Figure 8A the Wwox intron-retention
   bars carry significance stars for both siRNAs; **the TPM bars carry none**, and Wwox TPM sits
   within a few TPM of zero on a 0–400 axis. The caption's "decreased mRNA abundance" is a
   statement about the gene set, not a marked result for Wwox.
2. **The retained fraction is small.** Read from the panel, roughly 0.8 % of Wwox mRNAs retain an
   intron in control and roughly 1.2–1.4 % after knockdown. INFERENZA: NMD of every retaining
   molecule would remove about half a percent of the pool — too little to explain a dose change by
   that route alone. The paper does not discriminate.
3. **No Wwox-specific experiment exists.** No RT-PCR, qPCR, NMD-inhibitor arm or CLIP peak is shown
   for Wwox; the NMD demonstration is on three matrix genes, and the SFPQ binding data are a
   reanalysis of embryonic **brain** CLIP-seq, not these cells.

## 2 · A citation that does not support its sentence

The Discussion links the Wwox observation to human WWOX epileptic encephalopathy with large intronic
deletions and cites **Dvinge and Bradley 2015** — a pan-cancer intron-retention paper. Its Europe PMC
full text (133 557 B, fetched 2026-10-04) contains **zero** occurrences of "WWOX", "epileptic" or
"encephalopathy". The sentence is uncited in substance. It is also the sentence a reader is most
likely to carry.

## 3 · Internal inconsistency

Results name a single 639 kb retained intron for Wwox; the Discussion names introns 3 and 4. Neither
is accompanied by coordinates and the figures do not resolve it.

## 4 · Why it still matters, stated at its real strength

Read backwards, a pathway whose failure lowers WWOX transcript is a candidate pathway for **raising**
it without a cassette. What this source supports is only: *a splicing-factor-dependent mechanism
exists that changes the intron-retention fraction of Wwox in mouse neural crest*. It does not
support a dose-restoration lever, a neuronal relevance, or a protein effect. Wwox may simply be
caught by a length-dependent mechanism along with every other long gene — the paper's own framing
(median length ~100 kb for IR-elevated genes versus ~10 kb) makes that the leading alternative.

## 5 · Transfer limits

Mouse craniofacial neural crest and a stromal cell line; 50 % knockdown, not loss; transcript, not
protein; no neuron, no human cell, no WWOX allele, no rescue arm. Nothing transfers to any WWOX
allele class.

## 6 · Ops (provisional)

### 6.1 · `disease-models/wwox/research/research_lines_current.md`

| field | value |
|---|---|
| op | `append` (new record after the current final research-line record) |
| record | `RL-C-20261004w9c3 — PRMT1-SFPQ intron retention and Wwox: a trans-acting candidate regulator of WWOX transcript in mouse neural crest; retention marked, abundance not marked, retained fraction about one percent, and the human-disease sentence rests on a citation without WWOX content` |
| status | `open` |
| tag | `DATO` for the panel and text readings, `INFERENZA` for the arithmetic in §1.2 |
| body | §1–§5 of this candidate verbatim |
| class | MINOR |

## 7 · What would change this

- **Would strengthen:** a Wwox-specific RT-PCR with an NMD-inhibitor arm, in neurons, showing a
  protein-level fall; or an SFPQ-raising perturbation that raises WWOX protein.
- **Would falsify the regulator reading:** showing the effect is explained by gene length alone,
  with no SFPQ binding in Wwox introns.

## 8 · Brief premise tested

The selection called this "the first *trans*-acting regulator of WWOX dose the model would hold" and
noted the length-artefact risk. Both halves survive, but the selection's "decreased expression" for
Wwox is **unmarked in the figure**, which the selection could not see from the text.

### LOCATOR TRIPLES FOR BLIND AUDIT

Format: `(proposition | verbatim quote | anchor)`. The figure entry is an attestation of a panel
read at native resolution, not a string match.

- [PMID 42770556, artefact `files/fulltext/PMID42770556_Lima2026_PMC.xml`] (Wwox is named as a 913 kb gene with a 639 kb retained intron. | Of note, Wnt pathway gene Wwox and matrix genes St6galnac3 are 913 and 526 kb in length, and their retained introns are 639 and 215 kb in length, respectively | Results, long-gene section)
- [PMID 42770556, artefact `files/fulltext/PMID42770556_Lima2026_PMC.xml`] (The Discussion states increased retention of introns 3 and 4 with decreased expression on either perturbation. | the long gene Wwox exhibited increased retention of long introns (introns 3 and 4) and decreased expression upon Prmt1 or Sfpq deficiency | Discussion)
- [PMID 42770556, artefact `files/figures/PMID42770556/elife-101386-fig8.webp`] (PANEL: for Wwox the intron-retention bars are starred for both siRNAs while the abundance bars are not. | [figure attestation - pixels cannot be quote-matched] Figure 8A, Wwox row: right-hand intron-retention bars for both siRNAs each carry an asterisk, reaching roughly 1.2-1.4 percent against roughly 0.8 percent for the control on a 0-10 percent axis; left-hand TPM bars carry no asterisk and lie within a few TPM of zero on a 0-400 TPM axis. | Figure 8A, Wwox row)
- [PMID 42770556, artefact `files/fulltext/PMID42770556_Lima2026_PMC.xml`] (The knockdown reduced Sfpq by about half. | SFPQ knockdown caused around 50% reduction in Sfpq expression in CNCCs | Figure 7A legend)
- [PMID 42770556, artefact `files/fulltext/PMID42770556_Lima2026_PMC.xml`] (The human-disease sentence is the one that carries the citation under challenge. | In human patients, pathogenic variants of WWOX with large deletions within the long introns have been associated with epileptic encephalopathy syndrome manifesting shared facial phenotype | Discussion)
- [PMID 42770556, artefact `files/fulltext/PMID42770556_Lima2026_PMC.xml`] (IR-elevated genes are long: median about 100 kb against about 10 kb in controls. | the genes with increased IR in Sfpq -depleted CNCCs have a median length of ~100 kb | Results, long-gene section)

## BATCH DISPOSITION — `BATCH_20261004_003` (2026-10-04, ACTOR_ID `scientist`, Scientist M), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** `PROPAGATED` (MINOR, WM_v7.15 → WM_v7.16).

**Surfaces written:** research_lines_current.md

One new research line, **`RL-C-20261004w9c3`**. The record states the finding at the strength the source carries and no further: the intron-retention rise for *Wwox* **is** marked, the abundance fall is **not**, the retained fraction is about one percent, no *Wwox*-specific experiment exists, and the Discussion's human-disease sentence rests on a citation whose full text contains **zero** occurrences of WWOX, *epileptic* or *encephalopathy*. The Results/Discussion inconsistency on which intron is retained is **recorded, not reconciled**, with the standing rule restated: an intron number the source does not print is a **derivation** and must carry `INFERENZA`. ⚠️ The paper has **no dossier** — the write was halted by a model safety classifier — and `PAPER 243`'s `Evidence depth` field says so rather than naming a file that does not exist. **Blind locator audit:** not run (research-layer record, no claim or baseline touched); sampled by the integrator against the manifest only, and named here so the asymmetry is visible.

**Not medical advice.**
