# RP-004 (ADV-011): SCI reading of PMID 18620777, JNK inhibitor x WWOX gain and loss in HCC lines (2026-11-15)

Non-canonical research material. Not medical advice; no dose, route or recommendation; reference genotype class only. Written for: IT Orchestrator (scores the case predictions, closes `ORCH-RP004-LENS-20261115`) and the ADV presidio. In silico, one free lawful page request, zero spend, no contact parameter. Assignment: `mechanism_lens_it55_20261115/BRIEF_SCI.md`; record `ORCH-RP004-SCI-20261115`. Labels: DATO (read in the original body), INFERENZA (inferred here).

## Answer first

**Verdict: contrast carried with limits.** The body does carry a WWOX-status-by-inhibitor contrast in both directions, in two lines. It cannot say that the inhibitor effect belongs to WWOX status, to JNK, or to the inhibitor at all, as opposed to a baseline difference, the line or the clone.

1. **What is carried (DATO).** Gain: the two stable SNU387 WWOX clones show more apoptosis than vector, and SP600129 at 25 uM for 6 h "significantly enhanced" it (Figure 5B text). Loss: in SNU449, shRNA knockdown makes SP600129-induced apoptosis "significantly decreased" (Figure 5E text). The inhibitor reduced proliferation of SNU449 cells to about 25% of control; the text does not say whether that is vector or knockdown cells, and the knockdown's proliferation gain was not completely abrogated (V17, V18, V21). The direction is the same as with staurosporine in both arms (V20; Figure 3 and 4 text).
2. **What it cannot separate (INFERENZA from DATO).**
   * **Line identity and p53.** The two arms are two lines with different p53 alterations (SNU449 codon 161 Ala to Thr; SNU387 truncated at codon 164, V03). Each arm has its own vector control, so each contrast is within one line; the "gain in one line, loss in the other" picture is not one experiment.
   * **Baseline against inhibitor-specific effect.** Forced WWOX causes apoptosis by itself (up to 95% cell death at 72 h in the transient setting) and the knockdown lowers baseline apoptosis (V06, V19). The text states no interaction or baseline-normalised comparison and names no test, so "the inhibitor sensitises" is not separated from "WWOX cells die more, with or without it". The paper's own wording is that the inhibitor "enhanced WWOX-induced apoptosis" (V26).
   * **Clone and selection.** The gain clones survived 12 to 16 weeks of selection after transient expression killed most cells, and high-expressing clones could not be selected (V05, V07). The loss arm is a partial knockdown (40% mRNA, 30% protein) with one shRNA, no second shRNA and no rescue (V08, V09).
   * **Off-target activity and JNK identity.** One compound, one stated concentration and time (25 uM, 6 h, SNU387 only), no dose-response, no second chemotype, no genetic JNK control; no phospho-JNK or phospho-c-Jun readout (0 string hits, read by eye). The only pathway readout is phospho-ERK in the gain line (V15, V16). So the paper cannot assign the effect to JNK. The WWOX-JNK1 phosphorylation mechanism is cited, not measured (V23).
   * **Compound name.** The text writes SP600129 throughout; the paper's own reference 66 is "SP600125, an anthrapyrazolone inhibitor of Jun N-terminal kinase" (V11). The "[sic]" in the brief is supported by the paper's own citation; I did not check the compound beyond that.
3. **Transfer (DATO).** Only two HCC lines carry any functional assay; no neural cell, no tau readout, no non-cancer functional cell (F6). The authors themselves say the JNK effect is pro- or anti-apoptotic "depending on the cell type and system" (V22). Nothing here tests the case predictions P-a or P-b.
4. **Frozen predictions (scored before anything else, wording untouched): F1, F2, F3, F4, F6 HELD; F5 and F7 NOT DETERMINABLE; none MISSED.** Per-row basis in `prediction_scores.tsv`. F5 and F7 turn on numbers and bars that are in the five figure images, which I did not view.

## Extraction (brief item 3)

`extraction.tsv`, seven rows E01 to E07: the two lines and their WWOX levels, the constructs, the one inhibitor with its one stated concentration, the apoptosis and proliferation assays and the absence of any n, the JNK-activity readout by status, and the inhibitor-alone effect by status.

## What I read, and how

* **Route.** One plain request for the PMC article page (generic client, HTTP 200, 236,983 bytes). It is an article, not an interstitial (title, Abstract to Discussion, Table 1, five figure legends, reference list). Digest in `access.tsv`; copy under `files/fulltext/rp004_lens_20261115/` (gitignored).
* **Read in the original (DATO):** Abstract, Introduction, Materials and Methods, Results, Discussion, Table 1 (clinical characteristics, not used), the figure legends and reference entries 65, 66 and 68. **Not read:** the figure images, references otherwise, the publisher version.
* **Mechanical check.** `verify_quotes.py <page> verbatim.tsv`: all 26 rows found (PASS). Its six absence searches were read one by one: "dominant negative" (4 hits) is about WWOX splice variants, "triplicate" is the qPCR standards, "um sp" is the 25 uM statement; phospho-JNK/c-Jun, a second inhibitor and a neuronal or non-cancer functional cell have 0 hits. A zero is a count of strings in the text, not a finding about the images.
* **Receipt.** `receipts/FTR-20261115-18620777-01.json`, depth `partial_fulltext_read` because the figures are captions only (the protocol downgrades to partial); `fulltext_receipts.py record --dry-run` is OK. **Not appended to the ledger by me:** the integrator appends in event-ID order.
* **No blind verifier.** The decisive propositions are quotations that the script checks against the page; the weak point is the reading of "same direction" and "not separated", which is my inference from text. Called by me, not required by the brief.

## Limits

One paper, one author group, two lines; text only (figures unseen). The frozen predictions were scored from the body, after the body was read; the brief, the frozen file and IT's README (which quotes the abstract) were read first, and I had no other source for the paper. Not checked: the publisher version, the figure panels, any later paper by the group.

## What could change the verdict

Viewing the five figure panels (n, error bars, vector-plus-DMSO against vector-plus-inhibitor by line, concentrations for SNU449) could move F5 and F7 and might show a baseline-normalised effect; that is five more requests to a service whose rule here is one request per item, so it was not done without asking. A second line with both gain and loss, or a second chemotype, would answer the line and off-target limits.
