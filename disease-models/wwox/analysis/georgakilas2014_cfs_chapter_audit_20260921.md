# Audit of PMID 25238782 — Georgakilas *et al.* 2014, the CFS "functional units" chapter

**Target.** Georgakilas AG, Tsantoulis P, Kotsinas A, Michalopoulos I, Townsend P, Gorgoulis VG.
"Are common fragile sites merely structural domains or highly organized 'functional' units
susceptible to oncogenic stress?" *Cell Mol Life Sci* 2014;71(23):4519–4544.
PMID 25238782 · PMCID PMC4232749 · DOI 10.1007/s00018-014-1717-x · licence CC BY 4.0
(source: PubMed / PMC; identifiers verified against the target before any file was written and
they match on all four fields plus journal, volume, issue and page range).

**Artefact.** `files/fulltext/PMID25238782_PMC_MCPtext.txt` — 38,213 bytes, 5,749 words,
sha256 `3c51d26fe676c756a62525dbeb6d3115ed1c2923b98efad41e23b3ab03b7239c`.
Verbatim body as returned by the MCP extractor, unmodified and untruncated at my end
(no trailing newline added; the file ends `...for the cell when affected.`).

---

## 0 · VERDICT

**THE 2016 FRAMING IS FAITHFUL — this chapter proposes, it does not conclude.** Its own words for
its central answer are "we propose", "may not be merely", and "a tempting but speculative answer";
the words "conclude", "conclusion" and "hypothesis" do not occur in the body at all, and the
chapter's most assertive sentence about passive-versus-active is a **question** in its abstract,
not an answer.

---

## 1 · Question 1 — Genre

**It is a hybrid: a narrative review carrying original in-silico secondary analysis of public
databases, and no primary experimental data.** PubMed types it `Journal Article`,
`Research Support, Non-U.S. Gov't`, `Review`. It is one chapter of a multi-author *CMLS* special
issue on fragile sites — it repeatedly defers to its sibling chapters ("see A. Nussenzweig chapter
in this issue"; "see B. Kerem chapter in this issue"; "see M. Debatisse chapter in this issue";
"see K. Huebner and R. Aqeilan chapters in this issue").

The chapter states its own two-part design (*Introduction*):

> "Attempting to address these questions, in the current work we conducted an extensive review on
> the nature of their heterogeneity that accounts for their preferential instability. Next, by
> applying bioinformatic tools on data from the latest miRbase and the ENCODE project, we reveal
> that these sites are enriched in various (coding and non-coding) elements, such as cancer-related
> genes, miRs, and binding elements, as well as specific variations in histone modifications"

The original component is real but is entirely re-analysis of existing public resources — KEGG,
miRBase v20, ENCODE ChIP-seq. Its concrete outputs are:

- *Fragile sites and cancer-associated genes*: "We found that 110 cancer-related genes (33.6 % of
  all cancer-related genes) are located within CFSs"; density "37.2 % higher".
- *Fragile sites and microRNA genes*: "found 686 miRs out of 1,871 (36.7 %) within cytogenetically
  defined fragile sites"; relative density "57 % higher than in the rest of the genome".
- *Fragile sites and regions with regulatory potential*: CTCF sites within molecularly mapped CFSs
  "ranges between 2.76 and 3.20 % in different cell lines", an "18 % (10–25 %)-fold increase".
- *Fragile sites and histone modifications*: an ANOVA across cell-line groups, "(< 0.001, ANOVA)"
  — the italic *P* has been deleted by the extractor.

**What it can support:** the CFS literature as of 2014 as summarised by these authors; genomic
co-location statistics computed from KEGG/miRBase/ENCODE, at the coarse resolution the chapter
itself flags. **What it cannot support:** any experimental claim about fragility mechanism, any
gene-function claim, any causal claim, and anything at nucleotide resolution — the chapter says so
itself: "Our current understanding of CFSs is traditionally based on a static mapping, often
cytogenetic and imprecise, which cannot fully capture the interaction of non-coding DNA,
regulatory elements, and histone modifications with vulnerability to RS."

---

## 2 · Question 2 — What does the chapter actually CONCLUDE about passive versus active fragility?

**It does not conclude. It proposes, three times, each time hedged, and its terminal sentence is a
double modal.** There is no passage anywhere in the body that settles the question.

The chapter's position is stated in three places.

**(a) Abstract** (reproduced here, not in the artefact — it is a separate metadata field). The
passive/active dichotomy is put as a *question*, and the answer is explicitly a *proposal*:

> "Given that a number of oncogenes and tumor suppressors are located within CFSs, a question that
> emerges is whether fragility in these regions is only a structural "passive" incident or an event
> with a profound biological effect. … **We propose** that CFSs are not only susceptible structural
> domains, but highly organized "functional" entities that when targeted, severe repercussion for
> cell homeostasis occurs."

**(b) *Introduction*, closing sentence:**

> "Based on these findings, **we propose** that these sites **may** represent unique "functional"
> units of the genome that **may** have a complex role upon OIRS with implications both in normal
> cell survival and cancer progression."

**(c) *CFSs as "functional" units: a new perception*, the chapter's final sentence — this is the
strongest statement it ever makes, and it is a double modal:**

> "Overall, CFSs **may not be** merely structural domains vulnerable only to breakage but highly
> organized "functional" units that **may** have deeper biological consequences for the cell when
> affected."

Three further features fix the strength. First, the **title is itself an unresolved question**
("Are common fragile sites merely structural domains or highly organized 'functional' units…?") and
nowhere in the body is it answered in the declarative. Second, the section that carries the
position is titled "a new perception" — a perception, not a finding. Third, the words **"conclude"
and "conclusion" occur zero times in the body**, as does "hypothesis"; these are Roman-type tokens,
so those zeros are informative, not an artefact of the extractor (see §8).

So: the chapter **reviews both sides of the mechanism literature** (§*Fragility of CFS* ends
"there is no single mechanism that can explain the fragility of CFSs but rather a multitude … The
only common shared aspect by all these mechanisms is that they can eventually lead to a mechanical
breakage of CFSs" — i.e. it leaves the *mechanical* account standing) **and then proposes, without
claiming to have shown, that the consequences of that breakage are not merely structural.** It
leans; it does not settle. The lean is real and is placed in the title, the abstract and the last
sentence — but every single statement of it is modalised.

---

## 3 · Question 3 — Does "unlikely only a structural 'passive' incident" appear? (Rule D-15)

**No. Not verbatim, and not in substance as an assertion.** The finding is sharper than a simple
mismatch, and it is of a specific, nameable kind.

- The token **"passive" occurs zero times in the body text.** "Passive" is Roman type inside double
  quotes, not italic, so this zero is an informative negative and not an instrument reading.
- The phrase **does** occur, near-verbatim, in the **abstract** — but there it is the **question**,
  not the answer, and it carries **no** "unlikely":

  > "a question that emerges is whether fragility in these regions is **only a structural "passive"
  > incident** or an event with a profound biological effect."

- The nearest thing the body offers is the terminal sentence quoted in §2(c): "CFSs **may not be**
  merely structural domains vulnerable only to breakage…".

**Distance from the attribution.** The noun phrase "only a structural 'passive' incident" is the
chapter's own wording, lifted accurately. Two things are added by the citing author and are not the
chapter's: (i) the modal **"unlikely"**, which converts the chapter's interrogative into a
declarative with a probabilistic lean; and (ii) the reporting verb **"concluded"**, which upgrades a
proposal into a finding. In strength, "unlikely only …" is roughly comparable to the chapter's own
"may not be merely …"; the load-bearing distortion is therefore **not** the adjective but the
**reporting verb**. What the chapter asked as a question is re-issued as what the chapter answered.

This is a re-voicing error, not a fabrication: every word of the quoted noun phrase is in the source,
and the only way to catch it is to notice that the sentence it came from ends in a question mark.

---

## 4 · Question 4 — The "sensors" proposal

**It is offered explicitly as speculation, and the chapter labels it so in the same sentence.**
Section *CFSs as "functional" units: a new perception*:

> "An important question that emerges is why CFSs are not selected for elimination from the genome,
> but are rather conserved features in mammals? **A tempting but speculative answer is** that by
> locating a set of important coding and non-coding elements in regions that replicate late and/or
> with delay and thus are prone to instability, **they may function as alarm sensors** scattered
> throughout the genome in various chromosomes, to signify detrimental effects from the RS on the
> cell. As long as the mammalian checkpoints and repair mechanisms are not compromised, cells can
> monitor and protect their genome and functional integrity through such a dynamic interaction.
> Nevertheless, this imposes the risk that if the checkpoints and the anti-tumor barriers gradually
> fail, tumor promotion ensues (Fig.)."

Two observations. First, the phrase **"tempting but speculative"** is used twice in the chapter, the
other time for the MUS81-EME1 premalignancy model ("A tempting but speculative model is that during
premalignant stages, MUS81-EME1 cleavage activity is probably aberrantly increased…"). It is the
authors' standing marker for a hypothesis they are not claiming to have established. Second,
**"sensor" occurs exactly once in the whole body** — in the sentence above. The sensors idea is a
single speculative sentence in a concluding section, not a developed argument with supporting
analysis. The chapter's own supporting evidence for it is the co-location statistics (§1), which
establish *where things sit*, not *what they do*, and the chapter concedes the gap directly for the
CTCF case: "Although it is impossible to know whether CTCF binding at these sites exerts a
meaningful effect…".

Anything downstream that builds on "the sensors proposal" is therefore building on an acknowledged
speculation, and must carry that tag.

---

## 5 · Question 5 — WWOX / FRA16D

**The gene symbol `WWOX` cannot be counted on this surface** — it occurs zero times, as does `FHIT`,
and both zeros are instrument readings, not negatives (§8). The deletions are directly visible in the
text as run-together words. The locus name **FRA16D is Roman type and survives, six times.** Every
substantive passage:

1. *Heterogeneity of fragile sites*:
   > "The second most fragile site, FRA16D, is very frequently affected in epithelial breast cancer
   > cell lines (20–25 %), but only occasionally in colon epithelial cells (~5 %)."

2. *Heterogeneity of fragile sites*:
   > "In a study of 20 normal adults [], only FRA3B and FRA16D were found to be fragile in all
   > individuals, and only 42 % of CFSs (19 of 45 identified) were present in the majority of
   > individuals."

3. *Fragility of CFS* — the large-gene passage, with both symbols deleted by the extractor:
   > "Thegene in FRA3B andin FRA16D are striking examples, measuring approximately 1.5 and 1.1 Mb
   > respectively, compared with a mean of 10–15 kb for protein coding genes."

   Read with the deletion repaired from the surrounding syntax and the size figures, this is *FHIT*
   in FRA3B at ~1.5 Mb and the FRA16D gene at ~1.1 Mb. I flag that the identity of the FRA16D gene
   here is inferred from context, not read: the token itself is gone.

4. *Fragile sites in carcinogenesis*:
   > "For example, FRA2F, FRA3B, FRA4F, FRA5H, and FRA16D were most affected while others, like
   > FRA2B and FRA4B, were least affected."
   (context: "Multiple clusters of homozygous deletions, usually small, have been detected over known
   CFSs in an exhaustive survey of cancer genomes but their expression profile is variable")

5. *Fragile sites in carcinogenesis* — again with both symbols deleted:
   > "Recurrent alterations have been identified in FRA3B and FRA16D in several cancer types, leading
   > to further investigation of theandgenes, respectively, in mouse models (see K. Huebner and
   > R. Aqeilan chapters in this issue)."

6. *Fragile sites and histone modifications* — an original result of this chapter:
   > "Although cytogenetically defined CFSs as a whole do not show a large deviation from the mean,
   > some sites in particular, like FRA3B and FRA16D, seem to be on average poor in H3K4me3 while
   > others, like FRA2E, FRA3C, and FRA7D seem to be on average rich in H3K4me3"

**Does it treat WWOX as a tumour suppressor only?** It does not characterise the FRA16D gene at all.
It never states a function for it — not "tumour suppressor", not anything else. The gene appears
only as (i) a size exemplar for the large-gene fragility mechanism and (ii) a pointer to *somebody
else's* chapter for the mouse-model work ("see K. Huebner and R. Aqeilan chapters in this issue").
The framing around it is uniformly oncological, and the only functional language in the vicinity is
generic: "CFS breaks can amplify oncogenes, delete tumor suppressors or, most importantly, initiate
persistent chromosomal instability."

**It reaches no non-cancer phenotype for this gene, or for any gene.**

---

## 6 · Question 6 — Anything bearing on a neurological or developmental phenotype?

**No. The chapter is cancer-framed throughout, without exception.** Counts over the body, all of
Roman-type tokens whose zeros are therefore informative: `brain` 0, `neuron` 0, `neural` 0, `CNS` 0,
`epilep*` 0, `seizure` 0, `cognit*` 0, `intellect*` 0. Every one of the nine occurrences of
`develop*` is "cancer development" or "cancer progression" — there is no developmental biology in
this chapter in any sense.

The only two gestures outside oncology in the entire body are both incidental and neither concerns
CFS consequence:

> "Their fragility is due to expansions of the micro- or mini-satellites sequences that they contain
> and in some cases are responsible for inherited diseases []. Therefore, RFSs will not be further
> discussed in this work."

— this is about **rare** fragile sites, and the chapter immediately excludes them from scope; and

> "Interestingly, these elements are the most abundant mobile elements, and thus potentially
> recombinogenic in the human genome, and are implicated in various inherited human diseases and in
> cancer []."

— this is about the **Alu** family, not about CFS fragility outcome.

**What this means for how LEGEND may cite this chapter.** It may be cited for CFS architecture and
for the cancer-genomics framing of FRA16D fragility, and for nothing else. It carries **no** evidence
bearing on a neurodevelopmental phenotype, and any use of it in a WWOX-DEE argument would be an
out-of-scope extension of a cancer-only source. If this repository cites it at all, the citation must
travel with the scope tag: *cancer-framed CFS review with in-silico co-location analysis; silent on
non-cancer phenotype*.

---

## 7 · What LEGEND may now infer, and what this does to the citation-fidelity finding

**7.1 The finding survives the audit and becomes more precise.** The two framings are not equally
faithful. The chapter proposes and hedges; it does not conclude. Therefore:

- **PMID 27551470's framing — passive-versus-active as an open, two-sided question, with this chapter
  cited for a "sensors" proposal to build on — is faithful to what the chapter says.** The chapter is
  a proposal and labels its sensors idea "a tempting but speculative answer".
- **PMID 25238781's framing — this chapter as having *concluded* — is not faithful.** The quoted noun
  phrase is genuinely the chapter's, but it comes from the chapter's *question sentence* in the
  abstract, and the chapter's own strongest answer is "may not be merely".

**7.2 The failure mode is nameable and screenable.** This is **interrogative-to-declarative
re-voicing**: a citing author lifts a source's own framing question, strips the question mark, adds a
modal, and reports it with an assertive verb. It leaves no lexical fingerprint — the quoted words all
check out against the source — so quote-matching alone will not catch it. The only detector is
reading the sentence the quoted phrase sits in, and checking its mood. LEGEND should treat any
attributed phrase that reproduces a source's *title or abstract framing question* as suspect by
default, because those are exactly the sentences that get re-voiced.

**7.3 Both citing papers share a senior author.** The discrepancy is therefore not a disagreement
between rival groups but an inconsistency in how one group represented its own chapter thirteen
months apart. That makes the 2014 report an overstatement rather than a misreading, which is worth
recording separately: overstatement of one's own prior work is a different signal from misreading
someone else's.

**7.4 What this chapter may now be entered as, if entered.** Genre: review plus original in-silico
secondary analysis, no primary data. Epistemic status of its central claim: **proposal / speculative
hypothesis**, never elevated above that by the source itself. Scope: cancer only. It may support
co-location statistics (110/327 KEGG cancer genes, 686/1,871 miRBase v20 miRs, 2.76–3.20 % CTCF
sites within CFSs) and reviewed CFS architecture facts (FRA16D second most fragile; fragile in all of
20 normal adults; among the most affected by homozygous deletion clusters in cancer genomes; on
average poor in H3K4me3). It may not support any statement about WWOX function or any non-cancer
phenotype.

**7.5 What I did not do.** I did not attempt to resolve the "ref. 6" pointer from PMID 27551470 into
this chapter's bibliography. The extractor destroys the reference list entirely, so the resolution is
not available on this surface and any attempt would have been a guess. Confirming that PMID 27551470's
ref. 6 is this chapter requires the publisher PDF or the PMC reference list, neither reachable here.

---

## 8 · Declared limits

- **Author:** Scientist B. **Date:** 2026-09-21. **READ-ONLY** — no canonical LEGEND file, registry,
  queue, ledger or current file was read-modified or written. Exactly two files were created: the
  verbatim artefact and this analysis.
- **Extraction defect: PRESENT and severe, confirmed on this paper.** The MCP extractor silently
  deleted every italicised token. Direct evidence in the retrieved body: "Thegene in FRA3B andin
  FRA16D", "Thegene, at approximately 1.4 Mb is also associated with FRA6E", "further investigation
  of theandgenes", "the FRA10G-localizedis rearranged with the FRA10C-localized tumor suppressor
  gene", "theoncogene is flanked by CFSs FRA8C and FRA8D", "oramplification", "hyperplastic mouse
  urothelium fromtransgenic mice", "such as in the yeast[]", "(< 0.001, ANOVA)" (italic *P* gone).
  Consequently **`WWOX` = 0 and `FHIT` = 0 are instrument readings and are offered nowhere in this
  audit as evidence about the paper.** Where I counted Roman-type tokens (`passive`, `conclude`,
  `hypothesis`, `sensor`, `brain`, `neuron`, `CNS`, `epilep*`, `seizure`, `cognit*`, `intellect*`,
  `FRA16D`, `FRA3B`), I have said so at the point of counting, and those counts are informative.
- **Tables, figure legends, figure images and the entire reference list are absent** from the
  retrieved body. Inline figure and reference cross-references arrive as empty parentheses and
  brackets ("(Fig.)", "(Table)", "[]", "[,]", "[–]"), so no locator in this audit resolves to a
  numbered figure, table or reference.
- **No figure was inspected** — none is inspectable on this surface. Per rule **D-14**, no negative
  asserted only by a figure is adjudicated here. Specifically, the chapter's H3K27ac / H3K4me3
  distributional results are carried by Fig. 2b–c, and my §5 item 6 quotation reports only the
  running-text statement of them, not the figure.
- **Truncation: no narrative truncation detected, but completeness is not verifiable.** The body runs
  continuously from *Introduction* through *Heterogeneity of fragile sites*, *Fragility of CFS*,
  *Maintenance of fragile site integrity*, *Functional elements in fragile sites* (with its four
  sub-sections), *Fragile sites in carcinogenesis*, to *CFSs as "functional" units: a new perception*,
  and terminates on a formed concluding sentence. No section heading is orphaned and no paragraph
  breaks off mid-sentence. The retrieved body is 5,749 words against a 26-page journal span
  (pp. 4519–4544); the shortfall is plausibly accounted for by the dropped tables (which include a
  110-gene list and a 686-miRNA list), figure legends and reference list, but I cannot confirm that,
  and I have not reasoned anywhere in this audit from the absence of a passage.
- Attribution: article data retrieved from PubMed / PubMed Central. DOI:
  [10.1007/s00018-014-1717-x](https://doi.org/10.1007/s00018-014-1717-x). Licence CC BY 4.0,
  © The Author(s) 2014.
