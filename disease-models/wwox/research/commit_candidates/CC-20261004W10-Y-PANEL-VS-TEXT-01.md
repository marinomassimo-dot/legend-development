# CC-20261004W10-Y-PANEL-VS-TEXT-01 — two sentences of PMID 42397075 that its own panels do not support, and one lead whose bytes are gone

`context_policy: SOURCE_FIRST` · intake wave 10, 2026-10-04, Scientist Y
**Change class: MINOR.** Both items qualify what a source *says* against what its *panels plot*.
No claim's `Status`, `Type`, `Summary`, `Transferability` or `Source` moves, and no measurement in
any claim is withdrawn.

## Item 1 — the patient-genotype contrast is the opposite ordering from the panel it cites

The paper writes that WWOX-KO **and WOREE** organoids showed *"a prominent increase in the relative
number of total recognized RG cells (RGs) (Fig. 2D-F), while SCAR12 organoids (modeling a relatively
milder disease) exhibited an RG population similar to WT."*

🔴 **Measured at panel 2F against the panel's own axis ticks** — ticks located by pixel scan at
−3, −2, −1, 0, +1, giving 229 px per log2 unit at 900 dpi, bar extents read against them:

| genotype | RGs log2FC | Neu log2FC |
|---|---|---|
| WWOX-KO | 0 → **+0.98** | **−2.36** → 0 |
| SCAR12 | **−0.25** → 0 | 0 → **+0.18** |
| WOREE | 0 → **+0.07** | −0.04 → −0.01 |

**WOREE's radial-glia deviation (+0.07) is the smallest of the three.** SCAR12's (−0.25) is three to
four times larger in magnitude and runs the **other way**. "Similar to WT" describes WOREE; it does
not describe SCAR12. The sentence's contrast between the two patient genotypes is inverted relative
to what the panel plots.

⚠️ **Caveat stated against this finding.** The RGs bar is drawn as a colour composite of the
radial-glia subtypes, so a scalar read from its extent is the extent of the block and not
necessarily one fitted log2FC. The caveat applies **identically to all three rows**, which are drawn
the same way — so the *ordering* survives it even where the absolute value does not.

🔵 Cell counts recomputed from panel D: 5649 + 3020 + 3422 + 5916 = **18 007**, which is the n
printed on panel A. ✅

## Item 2 — the abstract's cell-cycle sentence merges a bin that rises with a phase whose bin falls

The abstract: *"dynamics leading to an accumulation of cells in the G2/M and S phases."*
Measured at Fig. 4C (`cell proportion log2 FC (KO/WT)` in radial glia): **S ≈ +0.77**,
**G2M ≈ +0.50**, **M ≈ −0.37**, **G1/G0 ≈ −0.28**. The `S` and `G2M` bins rise; the separately
plotted **`M` bin falls**. The panel carries **no error bars and no significance marks**: it is a
point estimate from the single scRNA-seq experiment (`WWOX-KO n = 2396 cells`, `WT n = 2152 cells`).

## Item 3 — the A51 lead cannot be re-audited, and the preprint cannot rescue it

The discovery lead `DL-THER-081` (A51, a multi-kinase Wnt/MYC suppressor, recorded at `IPOTESI`
with a BLOCK-1 question) rests on the published supplement `brain-2025-03809-File009.pdf` for its
dose and schedule, and on supplementary figures for its readouts. **Those bytes exist nowhere.**

🔴 **And the preprint cannot supply them.** The bioRxiv v2 full PDF was obtained free (63 pp, posted
2025-09-25) and carries the full Materials and Methods inline — but the A51 experiment is **absent
from the preprint entirely**. Measured by token count over both derived texts: `A51` **0** in the
preprint versus **3** in the published article; `MYC inhibition` **0** versus **5**; `multi-kinase`
**0** versus **1**. The experiment was added in revision.

**So `DL-THER-081` is not withdrawn — it is un-re-verifiable**, and that is a different and more
precise state than "unaudited".

## Ops

### Op 1 — `paper_registry_current.md`, record `PAPER 094`, append both panel findings to `**Role:**`

- `old` (measured unique in `PAPER 094`):
  `**Role:** **the mechanistic organoid reading**: MYC as the top significantly upregulated gene in WWOX-deficient radial glia, and the cell-cycle route to reduced neuronal generation.`
- `new`:
  `**Role:** **the mechanistic organoid reading**: MYC as the top significantly upregulated gene in WWOX-deficient radial glia, and the cell-cycle route to reduced neuronal generation. ⚠️ **Two sentences of this paper are not what its own panels plot (2026-10-04, \`CC-20261004W10-Y-PANEL-VS-TEXT-01\`, measured at 900 dpi against each panel's own axis ticks).** (a) The running text assigns a *"prominent increase"* in radial glia to the knockout **and to WOREE** and calls SCAR12 *"similar to WT"*; panel 2F plots the **opposite ordering** — WOREE's radial-glia deviation is **+0.07 log2FC, the smallest of the three**, while SCAR12's is **−0.25**, three to four times larger in magnitude and of the **opposite sign**. (The radial-glia bar is a colour composite of the subtypes, so the extent is the block's; the caveat applies identically to all three rows, so the ordering survives it.) (b) The abstract's *"accumulation of cells in the G2/M and S phases"* holds for the \`S\` (≈ +0.77) and \`G2M\` (≈ +0.50) bins of panel 4C while the separately plotted **\`M\` bin falls (≈ −0.37)**; that panel carries no error bars and no significance marks, being a point estimate from the single scRNA-seq experiment (\`WWOX-KO n = 2396\`, \`WT n = 2152\` cells). 🔵 Cell counts recomputed from panel D sum to the n printed on panel A: 5649 + 3020 + 3422 + 5916 = 18 007.`

### Op 2 — `discovery_ledger_current.md`, lead `DL-THER-081`, append the provenance state

- `old` (to be measured unique in `DL-THER-081` by the integrator; the lead's status line as it
  stands — this op is **provisional on that measurement**, since this actor does not edit ledgers
  and the lead's current wording was not read in this session):
  the final sentence of `DL-THER-081`.
- `new`: append —
  `🔴 **Provenance state, measured 2026-10-04 (\`CC-20261004W10-Y-PANEL-VS-TEXT-01\`): this lead is UN-RE-VERIFIABLE, not merely unaudited.** Its dose and schedule (125 nM, weeks 8-15) and its readouts come from the published supplement \`brain-2025-03809-File009.pdf\` and the supplementary figures volume of PMID 42397075. **Neither exists in any checkout or on the host**, and neither is obtainable by any lawful free route reachable today: Oxford Academic answers 403 behind an interstitial and there is no PMC deposit. ⚠️ **The preprint cannot rescue it:** the bioRxiv v2 full PDF was obtained free and carries the full Materials and Methods inline, but the A51 experiment is **absent from the preprint entirely** — \`A51\` 0 occurrences versus 3 in the published article, \`MYC inhibition\` 0 versus 5, \`multi-kinase\` 0 versus 1 — because it was added in revision. The lead stands at \`IPOTESI\` with its BLOCK-1 question; what it cannot do until the published supplement is obtained is be re-audited against its source.`

## DEFAULTS_TAKEN

- Op 2 is marked **provisional**: `DL-THER-081`'s current text was deliberately not read in this
  session (ledger records are not this actor's to edit, and the lead was not needed to measure the
  source). The integrator measures the `old` string before applying it, or drops the op; the finding
  it carries stands on its own in this candidate either way.

### LOCATOR TRIPLES FOR BLIND AUDIT

(Each artefact confirmed on disk before the triple was written.)

1. (The running text assigns a prominent radial-glia increase to WOREE and calls SCAR12 similar to wild type | `number of total recognized RG cells (RGs) (Fig. 2D-F), while SCAR12 organoids (modeling a ` | `files/fulltext/PMID42397075_Steinberg2026_OUP-AM_fitz.txt`, Results, p. 7)
2. (The panel that sentence cites plots the opposite ordering by magnitude | `[figure attestation] Figure 2F, axis ticks located by pixel scan at -3, -2, -1, 0, +1, 229 px per log2 unit at 900 dpi: WWOX-KO RGs 0 to +0.98 and Neu -2.36 to 0; SCAR12 RGs -0.25 to 0 and Neu 0 to +0.18; WOREE RGs 0 to +0.07 and Neu -0.04 to -0.01` | `files/fulltext/PMID42397075_Steinberg2026_assets/fig2F_600dpi.png`, Figure 2 panel F)
3. (The abstract states the accumulation as a joint G2/M-and-S statement | `dynamics leading to an accumulation of cells in the G2/M and S phases, overexpression of the ` | `files/fulltext/PMID42397075_Steinberg2026_OUP-AM_fitz.txt`, Abstract)
4. (The phase panel raises the S and G2M bins while the M bin falls, with no error bars and no significance marks | `[figure attestation] Figure 4C, 'cell cycle phase changes in KO versus WT RG cells', x-axis 'cell proportion log2 FC (KO/WT)': S about +0.77, G2M about +0.50, M about -0.37, G1/G0 about -0.28; panel A declares WWOX-KO n=2396 cells and WT n=2152 cells` | `files/fulltext/PMID42397075_Steinberg2026_assets/figs/fig_p35_1430x749.png`, Figure 4 panels A and C)
5. (The paper names the A51 compound as a multi-kinase inhibitor, and that experiment exists only in the published version | `this end, we performed a MYC inhibition experiment, using a multi-kinase inhibitor (A51)` | `files/fulltext/PMID42397075_Steinberg2026_OUP-AM_layout.txt`, Results; absent from `files/fulltext/PPR960425_Steinberg2025_bioRxiv-v2.full_layout.txt`, where the token count is zero)

---

## BATCH DISPOSITION — `BATCH_20261004_004` (2026-10-04, ACTOR_ID `scientist`, Scientist N), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED — **both ops landed. Op 2's provisional target was re-measured and is a different record from the one the candidate named, and one of its two factual premises was wrong.**

**Class, re-judged:** **MINOR**. `PAPER 094` gains panel-versus-text qualifications; no claim's `Status`, `Type`, `Summary`, `Transferability` or `Source` moves and no measurement is withdrawn.

**Blind locator audit (separate sub-agent, 5 triples, Fig. 2F measured at 600 dpi and Fig. 4C on the native raster):** **5/5 SUPPORTED**, 0 UNVERIFIABLE, with two fidelity notes that were folded in.

🔴 **Op 2's target was `DL-THER-081` and that lead no longer carries this content.** The entry was renumbered to **`DL-THER-089`** on 2026-08-10, in a declared merge-collision note in the ledger itself; `DL-THER-081` is a different lead. The candidate marked the op provisional and asked the integrator to measure the old string or drop it — it was measured, the target corrected, and the op applied to `DL-THER-089`, with the renumbering named inside the landed text so the next reader is not sent back to the wrong id.

🔴 **And the op's premise was half wrong, which the audit caught.** The lead's **dose and schedule are printed in the article itself** (*«A51 drug (125 nM), from week 8 to week 15 in vitro»*, with the compound credited in the Acknowledgements), so they are verifiable today on the re-acquired artefact. What is un-re-verifiable is narrower and was landed as such: the **Suppl. Fig. 7F–G panel values**. The preprint finding stands exactly as measured — `A51` 0 against 3, `MYC inhibition` 0 against 5, `multi-kinase` 0 against 1, the experiment added in revision — and the auditor added that none of the preprint's nine `inhibitor` hits is a MYC-inhibition experiment.

🔵 **Two fidelity notes folded into `PAPER 094`'s `Role`.** (a) The paper's running text does qualify itself — *«This result was more pronounced in the WWOX-KO organoids, compared to the WOREE organoids»* — so the landed finding is stated fairly: what panel 2F contradicts is *«SCAR12 similar to WT»*, since **WOREE's radial-glia deviation (+0.05 to +0.08) is the smallest of the three** while **SCAR12's is about −0.25 and of the opposite sign**. (b) The radial-glia bar was verified to be a **colour composite** of the subtypes at 600 dpi, so the composite caveat is kept with the finding, and the ordering is what survives it. Fig. 4C was confirmed to carry **no error bars and no significance marks** by a pixel scan of the panel's gaps and margins.

**Not medical advice.**
