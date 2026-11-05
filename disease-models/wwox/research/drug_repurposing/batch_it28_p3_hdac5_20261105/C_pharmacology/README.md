# IT28 P3-C: pracinostat at HDAC5, the 47 nM versus 5,113 nM discordance (pharmacology)

Scope: sub-question C only (assay design, quantity, comparators, CNS exposure). The origin of the
edge (A) and class IIa catalytic biology (B) are other packages. Public edition, no individual
data. Nothing here is medical advice. No doses are given. Nothing is averaged or reconciled, and
nothing is transferred from pracinostat to other class members.

## 1. Verdict

**UNRESOLVED, with the exact missing datum named.** Not a lineage error, not a curation error,
and the assay-design hypothesis is neither confirmed nor refuted, because the two methods
sections that decide it could not be read free of charge.

What was established:

1. The three papers cannot be read free. Europe PMC and PMC have no full text for any of them;
   publisher pages return HTTP 403; OpenAlex marks all three closed. **All three were read as
   abstract plus ChEMBL assay records only.** Unpaywall and contact-based routes were not used.
2. The discordance is **not confined to HDAC5.** ChEMBL document CHEMBL4706478 (PMID 29360358)
   gives pracinostat HDAC4, 7, 9 IC50 > 10,000 nM and HDAC5 5,113 nM. The originator values
   reprinted in Table 1 of PMC12747566 are HDAC4 56, HDAC5 47, HDAC7 137 nM, and the St Jude
   document (PMID 25637120) gives Ki HDAC4 16, HDAC5 21, HDAC7 107, HDAC9 24 nM. So it is a
   class IIa-wide split between one document (micromolar or above) and two documents (tens to
   about a hundred nM), not an isolated HDAC5 curation slip.
3. The 2018 document **did** use a different substrate for the class IIa rows. Per the ChEMBL
   assay records (fetched 2026-11-05): HDAC1, HDAC2, HDAC3/NCoR2, HDAC6, HDAC10 rows say
   "fluorogenic HDAC substrate 3"; HDAC4, 5, 7, 8, 9, 11 rows say "fluorogenic HDAC class2a as
   substrate". That is a ChEMBL curator's wording; that the "class2a" substrate is a
   trifluoroacetyl-lysine peptide is an inference from the literature (below), not read in the
   paper.
4. The 47 nM and 5,113 nM values are **not shown to be the same quantity.** Both are labelled
   IC50, but an IC50 depends on substrate identity, substrate concentration relative to Km,
   enzyme construct and concentration, and pre-incubation. For the 2010 originator paper none of
   these is available to me (GtoPdb assay field blank; paper not read). For the 2018 paper only
   substrate class, a 30 min read and the constructs for HDAC4/7/9 are recorded; the HDAC5
   construct is "unknown origin" in ChEMBL.

## 2. Why the substrate class matters (read in full text)

Bradner 2010, Nat Chem Biol, PMID 20139990, PMC2822059 (full text read; pracinostat is not in it).

- Results, section "Inhibition of Class IIa deacetylases by acetylated lysine": "Substrate 3
  shows no appreciable turn-over with human Class IIa deacetylases, despite possessing the
  acetylated lysine feature present in post-translationally modified proteins."
- Results, "Comparative study of HDAC inhibitors": they built "a new tripeptide substrate 6, which,
  like substrate 4, features the relatively labile and sterically more demanding trifluoroacetyl
  group that is readily hydrolyzed by the catalytically less avid Class IIa HDACs", and with it
  "the Class IIa enzymes are not targeted by most HDACi at pharmacologically-relevant
  concentrations."
- Methods, "Biochemical HDAC assay": "recombinant, full-length HDAC protein (BPS Biosciences) was
  incubated with fluorophore conjugated substrates 3 and 6 at a concentration equivalent to the
  substrate Km"; buffer "50 mM HEPES, 100 mM KCl, 0.001% Tween-20, 0.05% BSA, 200 uM TCEP, pH
  7.4". Methods, "Statistical methods": "Calculation of Ki was determined using a derivation of the
  standard formula Ki = [Inhibitor]/((V0/Vi)*(1+S/Km))-[Substrate]/Km)-1."
- Lahm 2007, PNAS, PMID 17956988 (abstract only in the PMC record fetched): "We also identified
  trifluoroacetyl-lysine as a class IIa-specific substrate in vitro."

Consequence (inference, tagged as such): a standard acetyl-lysine assay run on a class IIa enzyme
is turned over poorly, so an IC50 from it may reflect trace activity or co-purifying partner
activity rather than the class IIa catalytic domain; a trifluoroacetyl-lysine assay is the
documented way to measure class IIa catalytic turnover. If the 2010 originator HDAC5 value was
obtained with an acetyl-lysine substrate and the 2018 value with a trifluoroacetyl substrate,
the gap would be an assay-design effect. **That conditional cannot be checked here.** The 2010
substrate is not available to me, and a 109-fold difference could equally come from enzyme
construct, enzyme concentration, or Km relative to substrate concentration.

Also note (a pattern, not proof): the 2018 row set gave HDAC8 (a class I enzyme) 2,835 nM with the
class2a substrate while HDAC1/3 gave 50/70 nM with the standard substrate. Class I enzymes
accept the trifluoroacetyl substrate as well (Bradner, Results: HDAC8 "inhibitor sensitivity
emulates the substrate preferences"), so the substrate switch alone is a plausible modulator of
apparent potency even for a class I enzyme. This is one compound and one document.

## 3. Which value is pertinent

- For the question "does pracinostat inhibit class IIa **catalytic turnover of a class
  IIa-appropriate substrate**": the only record with an explicit class IIa substrate descriptor is
  the 2018 document, 5,113 nM at HDAC5. Its pertinence is limited: construct for HDAC5
  unrecorded, paper methods unread, and one document.
- For the question "does pracinostat **bind HDAC5**": a non-catalytic orthogonal read exists,
  Kotsull and Pflum 2025 (PMID 41473577, PMC12747566, full text read). In HeLa lysate, endogenous
  HDAC5 shifted by +9 degC with pracinostat (1.5 uM), more than TMP269 (+4 degC at 400 uM) and
  SAHA (0 degC at 400 uM); Results 2.2: "HDAC5 was best stabilized by SB939, with a Tagg value of
  67 +/- 1 degC compared to the 58 +/- 1 degC DMSO control". This favours binding well below the
  5 uM level, but a Tagg shift is not a Kd, the concentrations differ across compounds, and
  lysate HDAC5 may sit in a complex with HDAC3/NCoR (the paper cites that biology, ref 43), so
  the shift may report the complex. It does not select between 47 and 5,113 nM.
- The same paper's Table 1 IC50 column is a compilation: footnote b, "The previously determined
  IC50 values of each inhibitor and isoform were determined using the deacetylase activity assay
  [31,37,38,50,51]." Its 47 nM for pracinostat is therefore the originator value re-printed,
  **not an independent confirmation**. The authors also write that fluorinated-substrate assays
  "could poorly reflect inhibitor binding" (Discussion).
- Ki 21 nM (PMID 25637120): a different quantity (Ki), method unknown (ChEMBL text "Inhibition of
  human HDAC5"), different laboratory. Kept separate; not comparable with either IC50.

No source tells which value reflects HDAC5 engagement or inhibition in a neuron. The question is
open.

## 4. Lineage

PMID 29360358 authors include Wang H (last author); PMID 20197387 authors include Wang H
(fifteenth of seventeen). Same name only, identity not verified beyond affiliation context from IT27. Both
documents agree on HDAC1 (49 and 50 nM) and diverge only on the class IIa rows, which is the
pattern expected if the standard-substrate HDAC1 assay was reproduced and only the class IIa
format differs. It is also compatible with other explanations. A "lineage error" (one value
copied wrongly) is not supported: ChEMBL's own row for HDAC5 carries its own assay record
(CHEMBL4707188), and the originator value is reprinted by a third group.

## 5. Class IIa-selective comparators (TMP269, MC1568, LMK235)

- TMP269: compiled IC50 in PMC12747566 Table 1: HDAC4 157, HDAC5 97, HDAC7 43, HDAC1 > 40,000 nM;
  GtoPdb (PMID 23524983, Lobera 2013) pIC50 HDAC4 6.80, HDAC5 7.01, HDAC7 7.37, HDAC9 7.64. The
  primary paper is not in PMC; **abstract only**; its substrate and conditions were not read
  (the abstract says it describes a trifluoromethyloxadiazole zinc-binding group, "TFMO",
  and "a nonchelating zinc-binding group"). Pracinostat is not in that document per GtoPdb.
  So there is **no activity assay found in which pracinostat and TMP269 were run together.** The
  only same-experiment comparison is the thermal shift (binding), where pracinostat shifted HDAC5
  more than TMP269, but TMP269 did not shift HDAC4 at all ("HDAC4 was not stabilized (DTagg value
  of 0)") and shifted HDAC5 only modestly, which the authors call unexpected. That is a caution on
  TMP269 as the clean alternative, within one lysate assay.
- MC1568: no class IIa IC50 retrieved. Its structure was reassigned (PMID 24450497, abstract) and
  it is described as an HDAC6/8 inhibitor in PMID 27739328 (abstract) and in a 2026 paper
  (PMC13341649). Treat "class IIa selective" as contested; not resolved here.
- LMK235: only a title-level statement (PMID 34119632, "small molecule inhibitor of HDAC4/5").
  No biochemical value retrieved. Not determinable here.

## 6. CNS exposure of pracinostat

No measured brain or CSF concentration was found in the free sources searched. A 2025
compilation (PMID 41087426, PMC12521396, Table 2) lists pracinostat "Penetration through the
CSF?" as "n.d." (not determined), with rule-based items only (5 of 7 BBB requirements met;
P-glycoprotein substrate "No"), which is a computed property, not a measurement. The SB939
abstract reports tumour accumulation in mice, not brain. A glioma cell-line study (PMID 35622308,
abstract only) shows in vitro/in vivo anti-glioma effects but the abstract does not state
brain exposure. A phase 1 trial (PMC5901648) excluded CNS involvement (Methods, exclusion
criteria). **Pracinostat CNS exposure: not determined.**

## 7. Missing data that would close it

1. SB939 originator paper (Mol Cancer Ther 2010, PMID 20197387): the HDAC isoform table and its
   methods: enzyme source and construct for HDAC4/5/7, substrate identity (acetyl- or
   trifluoroacetyl-lysine), substrate versus Km, enzyme concentration, incubation. This single
   section decides whether the two IC50s are the same quantity.
2. J Med Chem 2018 (PMID 29360358): methods and SI for "HDAC class2a substrate", HDAC5
   construct, top concentration tested (the > 10,000 nM censoring), and whether pracinostat was
   run on the same plate series as the class I rows.
3. St Jude 2015 (PMID 25637120): how the Ki values were produced.
4. Any run of pracinostat and TMP269 in one class IIa activity assay.

## 8. For the lever decision (not transferred to the class)

- Pracinostat as an HDAC5 lever: the activity potency at HDAC5 is **unresolved between about 50 nM
  and about 5 uM**, with orthogonal binding evidence (lysate thermal shift) favouring genuine
  engagement. CNS exposure is undetermined. These do not support a claim either way.
- TMP269 as alternative: class IIa-selective by compiled activity data, but the primary paper was
  read as abstract only, a thermal-shift comparison shows weak engagement of HDAC4/5 in lysate,
  and the same trifluoroacetyl-substrate caveat applies to its own IC50s. No CNS data were
  sought here.

## Files

- `hdac5_pharmacology_it28p3c.tsv` comparable measures with assay descriptors (not averaged).
- `receipts/FTR-20261105-20139990-04.json` Bradner 2010 (PMC2822059), partial full text.
- `receipts/FTR-20261105-41473577-04.json` Kotsull and Pflum 2025 (PMC12747566), partial full text.
- `receipts/FTR-20261105-41087426-04.json` Sci Rep 2025 review (PMC12521396), Table 2 only.
- No receipt for the three target papers: no full text was obtainable; they are abstract-level.
  Receipts are drafts, not recorded.
