# Intake wave 10 — 2026-10-04 — Scientist X

`context_policy: SOURCE_FIRST` · branch `task/sci-X-20261004w10` · **Not medical advice.**

One paper, read in full: **PMID 21476439**, Sałuda-Gorgul A, Seta K, Nowakowska M, Bednarek AK,
*WWOX Oxidoreductase – Substrate and Enzymatic Characterization*, Z. Naturforsch. 66 c, 73–82 (2011),
issue 1–2. The article prints no DOI on its own front matter; PubMed records none either, which is
why it resisted DOI-keyed acquisition for seven batches.

**Verdict: INGEST.** Read in full from the version of record, seven batches after it was first
queued. Not a duplicate: `fulltext_receipts.py status --pmid 21476439` returned `[]` and
`paper_packet.py` reported `prior read: depth=none · receipts=0`, so this is a first reading.

| artefact | |
|---|---|
| dossier | `disease-models/wwox/research/fulltext_dossiers/PMID21476439.md` |
| manifest | `disease-models/wwox/research/deepdive_manifests/PMID21476439.json` — `--verify-artifacts --require-current-schema` **PASS, 0 gaps**, 17 verbatim locators |
| receipt (prepared, **not recorded**) | `scratchpad/receipts_pending_w10/sciX_21476439_1.json`, also at `~/legend-receipts-backup-20261004/receipts_pending_w10/` |
| candidates | `CC-20261004W10-X-ENZYMOLOGY-01` (MINOR) · `CC-20261004W10-X-REGISTRY-01` (MINOR) |

## The assigned question, answered

**What enzymatic activity was actually measured on WWOX?** Oxidation of seven steroids
(5α-androstane-3,17-dione, 4-androstene-3,17-dione, 17β-estradiol, estrone,
5α-dihydroprogesterone-*allo*, progesterone, testosterone), followed only as NAD(P)H formation at
340 nm over 30 min at 25 °C. Protein source: the **soluble fraction of an unfractionated *E. coli*
crude extract** (400 µg total protein per 1 ml) containing a NusA-WWOX fusion from pET 44a(+) in
Origami B (DE3) pLysS, or a GST-WWOX fusion from pGEX 2TK. Constructs: **full-length wild-type human
WWOX cDNA, subcloned whole**; no domain-only construct, no deletion, no point mutant. Controls: the
matched empty-vector extract with substrate, and both extracts without substrate. Kinetics: apparent
Km by Lineweaver–Burk, Table II, units 10⁻⁵ M. Replicates: "at least two or three demonstrations";
Fig. 2's curves are "from one of two experiments". **No units of activity, no Vmax, no kcat, no
specific activity, no reaction product identified by any method.**

**What was predicted rather than measured.** Everything structural. The GANSGIG cofactor site at
131–137, the YNRSK substrate site at 293–297 and the serine twelve residues upstream of the YNRSK
tyrosine are **sequence annotations cited to the group's own 2000 paper and to Duax & Ghosh 1997**,
not measurements. The 17β-HSD3 relationship is a clustering citation. The attribution of the
activity *to the SDR domain* is an inference from a full-length protein, because no SDR-only
construct and no catalytically-dead mutant was ever made. "Only one site for the steroid-to-substrate
bond" is read off the shape of a progress curve. And the identity of the band as a WWOX fusion is
itself predicted from expected migration: Figure 1 has no molecular-weight ladder in either panel and
the paper contains no Western blot, antibody or mass spectrometry.

**What a missense or splice allele of the reference genotype class would mean for it — the transfer
limit, stated exactly.** **Nothing transfers.** The paper contains no allele of any kind, no patient
material, no mammalian cell and no neurological readout. P47T ≠ Q230P ≠ G372R ≠ A141T ≠ P252A, and
none of the five was made or tested here; an acceptor allele is not a donor allele, and the paper has
no RNA work at all, so read fraction, frame, NMD and residual protein are untouched. What the paper
establishes is a **wild-type reference property**, with the limits above. The one position-level fact
an allele argument could reach for — the two motif coordinates — is an annotation carried from
another paper, and proximity of a residue to a motif is not a measured functional consequence. Any
sentence of the form "allele X disrupts the WWOX SDR catalytic site" remains `INFERENZA`, and this
paper supplies no datum to raise it.

**Could it be an endpoint or a pharmacodynamic assay under LEGEND_CORE §13?** §13 read. **The concept
is Tier 1** — §13 names "enzymatic activity" as a direct gene readout — **but this assay is not usable
as one, and it is not an endpoint.** It has no purified enzyme, no product identification, no activity
units, a substrate-independent background of a quarter to a half of signal, a host background of up to
65 % of signal on the very substrate the conclusion rests on, and no catalytically-dead control; its
dynamic range is an absorbance difference between two bacterial lysates, with no demonstration in any
mammalian matrix. As a pharmacodynamic assay it fails additionally on matrix and on the absence of any
intervention. And a biomarker is not an endpoint in any case. Nothing here is "validated" in §13's
sense, which requires sensitivity and specificity evidence in the disease population.

**Independence of the laboratory: none from the gene's discovery.** The corresponding author is first
author of the WWOX discovery paper (PMID 10786676) and of PMID 11719429; the WWOX cDNA "came from
A. K. Bednarek's collection"; and both motif annotations are cited to his 2000 paper. Two departments
of the Medical University of Lodz appear on the article — Analytical Chemistry (first author) and
**Molecular Cancerogenesis** (the corresponding author), which `FT-130` currently records as
Analytical Chemistry alone. No orthogonal laboratory has replicated this enzymology in anything the
paper cites.

## Recomputations that changed what I would carry

1. **No Vmax exists.** Methods promise it; the word occurs once in the paper, in that promise.
2. **Table II's Km is a difference of two Km values**, by the table's own footnote.
3. **13 of 14 Km values lie below the lowest substrate concentration Table I used** (lowest [S] / Km
   = 1.06–4.13), so almost every Km is an extrapolation from the saturated arm; 13 of 14 confidence
   intervals are asymmetric about their own Km and two span 3–3.5 × it.
4. **All 14 printed Mann–Whitney p values are unattainable with the stated n.** The exact test's
   smallest two-sided p is 0.333 at n = 2 and 0.100 at n = 3; the printed values run 0.0000–0.0091.
5. **The NAD⁺ curves consume 78–89 % of the substrate in 30 min** (ε = 6270 M⁻¹ cm⁻¹ against
   0.24 µmol/ml), so they are end-point, not initial-velocity, curves.
6. **The Results text mis-ranks its own panels**: the three substrates it calls "3- to 6-fold" measure
   1.55–2.46 ×, and the four it calls "blank level" measure 2.67–4.68 ×.
7. **Estrone, which carries the paper's central inference, is its weakest case** — largest host
   background of all seven (0.80 of a 1.24 trace), smallest WWOX-specific increment (0.44).

## Reading debt discharged, and what it changed

Four landed statements now have a primary behind them and **hold as worded**: `FT-130`'s "crude
extract, not endogenous protein, not human cells, not patient-derived, not a single disease allele";
`FT-147`'s "heterologous expression reported at least twice", "no purified, folded, biophysically
characterised WWOX SDR protein exists", and "no yield, purity, Tm or monomer fraction is reported
anywhere". The six caveats of `CC-20260921-WWOX-ENZYMOLOGY-P306-01` §2/§2bis are **all confirmed**;
its HALF ONE and HALF TWO both survive.

Four do **not** hold as worded, and are proposed for correction in `CC-20261004W10-X-ENZYMOLOGY-01`:

- `FT-147`'s self-correction **over-corrected**. It retracted "the SDR domain has never been expressed
  or purified by anyone" on the strength of this paper's abstract — but the paper expressed
  **full-length WWOX**, never the domain, and purified nothing. Read narrowly, the retracted sentence
  was true. The practical consequence runs the other way too: the paper does not lower the cost of a
  purified-SDR route, it documents a failure mode (activity lost on both resins).
- `CC-20260921` §2bis's "**live contradiction**" with the 2015 retinal-oxidoreductase proposal **is
  not a contradiction**: this paper never tested all-trans-retinal. Its negative covers the same seven
  steroids with NADH/NADPH and is reported "results not shown". The two concern different substrates
  and have never been tested against each other.
- `FT-130` over-weights that negative as "a real constraint on assay design": it is an unillustrated
  results-not-shown sentence with no panel, table, number or statistic.
- `FT-130`'s title, acquisition verdict and affiliation line are superseded or misassigned.

## What would change the model if true, and what would falsify it

**If true and extended:** that WWOX carries a real steroid-oxidising activity *per molecule* would
make an allele-resolved enzymatic assay a Tier-1 readout, which is the thing the proteostasis
programme's step 5 needs and the thing `TX-003` is blocked on. Nothing in this paper gets there,
because it never resolves WWOX from the lysate.

**What would falsify the paper's own claim:** a catalytically-dead point mutant of the YNRSK motif,
expressed and assayed side by side in the same crude-extract format. If the activity survived, it was
never WWOX's. That experiment is cheap, was available in 2011, and was not done — which is the single
most informative absence in the paper.

**What would make it usable:** purified WWOX (or a construct whose activity survives purification),
a product identified by HPLC or MS, activity in units per mg of resolved protein, and the dead-mutant
control. `FT-147`'s `REVIVAL_TRIGGER` — "if this body reports purified enzyme with a dead-triad
control" — **does not fire**: the body reports neither.

## Anything in the brief that was wrong

Nothing material. Two refinements:

- The brief calls the artefact "10 typeset pages with a clean text layer" — true, **but the text layer
  is lossy exactly where the paper's numbers live**: Table II is typeset rotated 90° and its row order
  is not recoverable from the flattened text. It had to be read from a rendered, rotated page image.
  A reader who trusted the text layer would have mis-assigned every Km to the wrong substrate.
- The brief asks whether the paper "could be an endpoint **or** a pharmacodynamic assay". §13 makes
  those different questions with different answers, and the dossier answers them separately.

## Open reading debt this reading creates

Six gene-direct references queued in the manifest, led by **PMID 10786676** (Bednarek 2000) — the
sole source of the two sequence motifs this paper's whole interpretation rests on, and still unread.
Also **PMID 11896615** (the tumour transcripts lacking the substrate-binding part of the SDR domain,
which is the paper's only bridge from enzymology to disease) and **PMID 12829805** (one of the two
clustering analyses that are the only basis for a regiochemistry the paper never measured).
