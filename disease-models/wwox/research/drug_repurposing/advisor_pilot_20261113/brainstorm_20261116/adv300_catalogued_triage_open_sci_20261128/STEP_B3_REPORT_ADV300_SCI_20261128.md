# ADV-300 step B batch 3 (records 5, 6) full-text reader

legend-delegate, claude-sonnet-5-5, effort high on 33 of 33 model turns read back. Model output, hypothesis level, not medical advice; saved verbatim.

---

FULL-TEXT CHECK, records 5 and 6. Hypothesis-level reading of public literature; nothing here is medical advice. Paths below are under /home/desktop/legend-development/.claude/worktrees/sci_aw_20261128/disease-models/wwox/. I wrote no repository file (git status is clean).

**Result:** record 5 has 0 counted data. Record 6 has 1 counted datum, and it is a marginal call.

## Record 5, PMID 25710931

**(1) What it reviews.** This is a review with no wet-lab measurement of its own. It classifies how tandem WW domains cooperate:
- joint or additive binding (YAP2)
- WW2 chaperoning WW1 (WWOX)
- binding-induced binding (Nedd4L)
- modulation of binding conformation (FBP11)
- stabilisation competing with binding (Su(dx))

It also covers linker structure, multivalency, dimerisation and isoforms. Its WWOX statements are all cited from other work.

**(2) Counted data:** none.

**(3) Uncounted data (own, but no held sentence depends on them)**
- Future outlook: the authors' "simple inspection" of 55 human proteins with bona fide WW domains. About half have more than one WW domain, linker lengths vary widely, and 15 are expressed as isoforms differing in WW repeat number.
- Figure 3: previously solved tandem-WW structures, re-oriented for display.

Not counted because they fail condition 1 (cited, or a synthesis of cited work):
- WWOX WW1 folds only in the tandem, with 2 to 3-fold higher affinity.
- WW2 binding is restored by E66R/Y85W.
- None of 16 high-throughput WWOX WW2 ligands was recapitulated in a later study.
- Positive cooperativity has so far been reported only where in-tandem binding is reduced.

**(4) Searches**
- Identifiers (PMID, PMCID, DOI) in all permitted files: no hit.
- `WW1|WW2|WW domain|WW-domain|tandem|PPxY|PPXY` in the claim registry, working model, disease_model, both ledgers, portfolio, open-questions map, all card folders and comparator TSVs. I read the matching lines, including CLAIM 023/024, the working-model "Domain cooperativity" paragraph and the A01, J01 and K01 card hits. Ledger lines were read truncated.
- `WW-containing proteins|proteome|isoform|linker` restricted to lines with WW: nothing depends on the proteome counts.

**Figures:** I looked at all three main figures (jpg). I did not open the gif thumbnails.

## Record 6, PMID 35563688

**(1) What it measured.** Human bladder-cancer lines RT-112, HT-1376 and CAL-29, each with six stable lentiviral variants: control, AP-2α, AP-2γ, WWOX, WWOX+AP-2α and WWOX+AP-2γ.
- CAGE-seq (GSE193659), with the three lines treated as biological replicates.
- Pathway, network and PCA analyses.
- Western validation of FGFR3, STAT6, EFNA1, GSK3B, PIK3CB and SOS1 in biological and technical triplicates per line. KIF7 was not detected.

WWOX is only overexpressed. There is no loss-of-function arm, no neural cell and no activity assay.

**(2) Counted: 1 (marginal)**

**Datum.** Stable WWOX overexpression lowers total GSK3β protein, GAPDH-normalised, in all three lines (control to WWOX, mean ± error as printed):

| Line | Control | WWOX | Significance in Fig 6D |
|---|---|---|---|
| RT-112 | 2.2982 ± 0.2843 | 0.7414 ± 0.1291 | ** |
| HT-1376 | 0.7606 ± 0.0318 | 0.3938 ± 0.0148 | *** |
| CAL-29 | 0.6696 ± 0.0284 | 0.5818 ± 0.0257 | * |

The GSK3B transcript is also slightly lower.

- **Locators:** Results 3.4; Figure 6D; Figure 5A, GSK3B box (WWOX/control pale blue, down arrow); Discussion, "GSK3B and CTNNB1, were downregulated by WWOX".
- **My check of the printed band intensities:** the normalised means reproduce for RT-112 and CAL-29; HT-1376 is consistent.
- **Caveat on the raw bands:** raw GSK3B (WWOX/control) is about 0.58, 0.34 and 1.12. In CAL-29 the fall exists only after GAPDH normalisation. In RT-112, GAPDH is about 1.75-fold higher in the WWOX lanes, with one low control lane (1782 against 4142 and 4299).

**Held sentence**, registries/claim_registry_current.md:355 (CLAIM 016), elided:
> "WWOX non è soltanto correlata al livello di GSK3β — ne è un **inibitore fisico diretto**, tramite il motivo di docking Axin-like 388–407/L404 del dominio SDR [...]. L'affermazione causale si sposta quindi da *«GSK3β è elevata»* (osservazione di abbondanza) a *«GSK3β è de-repressa»* (perdita di un freno fisico)."

**Changed sentence:**
> "WWOX is a direct physical inhibitor of GSK3β (388–407/L404 docking); in three human bladder-cancer lines, stable WWOX overexpression also lowers the GSK3B transcript and total GSK3β protein (western, GAPDH-normalised). The causal statement for WWOX loss remains de-repression, but an abundance component is measured under gain of function in cancer cells and is untested in loss or in neural tissue."

**Why marginal.** The change adds a species and an abundance-level route to a general mechanism sentence. The count becomes 0 if a change requires the same system as the held sentence. These are scoped to the Wwox-null mouse or to SH-SY5Y and would read the same:
- claim_registry_current.md:354, :357 and :362
- card G01 `target_expression` (research/drug_repurposing/cards/G01_lithium_gsk3.card.json:73 and :204, "total protein unchanged between genotypes")
- research/discovery_ledger_current.md:1658

It does not change the CLAIM 035 phospho-S9 warning or answer the open question on GSK3 output in WWOX loss (WO-22).

**(3) Uncounted data worth knowing (all under WWOX overexpression)**
- **Wnt transcripts:** CTNNB1 slightly down; WNT11, WNT16 and BMP4 up. DL-MOL-003 (discovery_ledger_current.md:95, statement at :99) would read the same, since no canonical Wnt activity is measured and the context is cancer.
- **Oxidative and chaperone genes:** the text says PRDX1, HSP90B1 and HSP90AB1 are decreased. The L01 card sentence on PRDX1 (cards/L01_nrf2_axis.card.json:144) is about knockout organoid libraries and would not change.
- **PI3K, Ras and MAPK:** AKT3, SOS1, SOS2, PIK3CB and VAV3 down. PIK3CB and SOS1 are also checked by western.
- **Up with WWOX:** FGFR3 and STAT6 (western); TGFB1, TGFBR2, MAP3K5, TCF7L1, CALML3, THBS1 and PLCE1 (transcript).
- **UPF1:** I saw no mention in the text, so DL-MECH-069 (discovery_ledger_current.md:1863) is not touched by anything I could read. The deposit and network labels were not checked.
- **New deposit:** GSE193659 is a WWOX gain-of-function transcriptome. I found no held sentence it changes.

**(4) Searches**
- Identifiers and GSE193659 in all permitted files: no hit.
- Counts across all permitted files for bladder/urothel, AP-2/TFAP2, CAGE, the paper's main genes, catenin, TGF-β, Rap1, HSP90 and antioxidant genes. I then read the hits for CAGE, bladder, HSP90, PRDX1 and GSTP1.
- GSK3 with abundance, expression or total-protein wording; Wnt/catenin with overexpression or cancer wording; Wnt lines in the registries and therapeutic ledger; AKT with expression wording.
- WWOX gain-of-function transcriptome wording and PMID 30619736.
- Comparator TSVs for GSK3, catenin and bladder.
- Cards read at the relevant fields: G01, D02, D01, L01, A03, E03/I01 and the early cards' GSK3 hits.
- The MTOR early card was looked for under the wrong folder and not opened for AKT.

**Figures:** I looked at main Figures 1 to 8 and Figures S1 to S3, and enlarged crops of Figures 5 and 6D. I did not open the gif thumbnails; the `s/` subfolder is empty.

## (5) What I could not read, and failures
- Gene labels and per-gene values in S1, S2 and S3 are mostly illegible at the resolution I viewed, and I did not enlarge them. I did not access GSE193659.
- My first grep failed (ugrep pattern complexity limit) and was replaced by simpler searches. PIL was absent, so I cropped with ImageMagick. The scratch folder is deleted.
- Two display commands lacked the exclusion filter for the barred PMID (claim registry lines 536 to 545, and one line-number grep for DL-MECH-019/064 in the discovery ledger). No line naming it appeared. Some count-only and filename-only searches were also unfiltered.
- Minor scope slip: after deleting scratch I listed /home/desktop/.claude/jobs/919d2041/tmp/adv300/, which is outside the allowed folders. I saw file names, including other steps' reports, and opened none.
- As the dispatch directed, I did not open framework/protocols. I opened no memory file; a memory index was already in my context at start.

