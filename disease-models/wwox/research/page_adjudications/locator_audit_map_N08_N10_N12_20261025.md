# Locator audit, map records N-08, N-10 and N-12 after their second repair (blind, 2026-10-25)

Blind audit under `legend-locator-audit`, read-only toward every manifest, registry, ledger and
analysis file. Scope: the current wording of three records of `analysis/mechanism_intervention_map.md`,
judged only against the artefacts they quote. Nothing was repaired. Disclosure: while locating the
layout template, the header and count table of the earlier audit file were seen (its verdict words
for the first rewrite); no verdict reasoning for these three records was used, and every reading
below was made fresh from the artefacts.

## Artefacts opened

| Record | Artefact | Held at |
|---|---|---|
| N-08 | Abdelmalak 2013 | `files/fulltext/PMID23611579_Abdelmalak2013_PMC_r2.xml` |
| N-08 | Lee 2022 (pilocarpine rat, DCA with pyruvate) | `files/fulltext/PMID36432491_Lee2022_PMC_r2.xml` |
| N-10 | Cheerie 2025 Data S1 (text layer) and main text | `files/supplement/PMID40139194_r2/mmc1_pymupdf.txt`, `files/fulltext/PMID40139194_Cheerie2025_PMC_r2.xml` |
| N-10 | milasen report (Kim 2019) | `files/fulltext/PMID31597037_Kim2019_PMC_r2.xml` |
| N-12 | Fog 2018 | `files/fulltext/PMID30497978_Fog2018_PMC_r2.xml` |
| N-12 | `D-03` | `research/dismissal_ledger_current.md` row D-03 |

## Counts

| Record | Quotations verbatim | Verdict |
|---|---|---|
| N-08 | 11 of 11 (10 Abdelmalak, 1 Lee) | UNDERSHOOT (measurement written as not made) |
| N-10 | 6 of 6 (Data S1 x4, main text x1, table with ellipsis) | OVERSHOOT (consequence the table contradicts) |
| N-12 | 3 of 3 (2 Fog, 1 D-03) | SUPPORTED |

Adverse rate, mode stated: 2 of 3 records carry one adverse proposition each (record level, blind,
whole record against its quoted artefacts); 0 of 20 quotations are non-verbatim. All the defects are
at proposition level, none at quotation level.

## N-08, dichloroacetate: UNDERSHOOT

Population repair holds. The cohort is stated as 8 patients, 3.5 to 40.2 years at start, one adult;
the authors' own scope sentence and the contrast with the MELAS trial (older adolescents and adults)
are quoted whole, the symptomatic finding is attributed to the other study, and no age range is
transferred. The "asymptomatic" qualifier is kept. Patient 8 persisted longest and is described by the
source as the oldest subject treated; the record's use of that is accurate. Chronic foot numbness in
patient 8 is stated by the source to be unaffected by DCA, so "asymptomatic" for the nerve-conduction
effect stands.

Adverse proposition 1 (measured written as not measured). Record: the Lee paper states *"low doses
of DCA or pyruvate alone do not significantly reduce neuronal cell death due to seizure"* "citing
prior work, not measuring it". Source, Lee 2022 section 2.4: *"the seizure group comprised DCA,
pyruvate, and combined DCA and pyruvate groups"*, and in the Discussion *"When hippocampal neuron
survival was evaluated using neuronal nuclei (NeuN) staining in this study, it was found that the
administration of only DCA or pyruvate once a day for one week after seizure was ineffective compared
to the results of the seizure group."* The quoted sentence does cite prior work, but the paper also
measured single-agent arms itself. The same passage reports that the co-treatment *"significantly
reduced degenerating neurons after seizure"* and improved hippocampal neuron survival; the record
lists only oxidative-stress and glial-activation readouts. A reader would believe the single-agent
null is borrowed and the combination's benefit is confined to those readouts; the paper measured the
null and reports a neuronal-survival benefit.

Lesser, not counted as adverse: the record says the paper "instead postulates" technical variability,
disease course, exposure and advancing age. The sentence immediately before it in the source adds that
*"vulnerability to DCA-induced neuropathy in rodent models is directly associated with age"*; the
record's argument that age cannot carry the symptom split is its own inference and omits that the
authors cite age-dependent vulnerability as background.

## N-10, splice-switching ASO: OVERSHOOT

Quotations are verbatim, including the ellipsis in the table quote (it removes two other criteria, not
a qualifier) and the "most likely not eligible" paragraph, now quoted through *"classified as 'not
eligible' for this approach"*. The earlier stopped-one-sentence-early defect is gone.

Adverse proposition. Record: a transcript measurement showing residual wild-type splicing "would move
it from the guideline's *destroyed* to its *weakened* class — *unlikely eligible*, not *not eligible*
— and make an SSO a live question again", while the same record states the positional criterion "is
met on sequence alone" and that "the class verdict stands on position". Source, Data S1 eligibility
table, Not eligible column: *"Canonical splice site and branchpoints are destroyed OR … OR Variant
within 5 bp of the canonical splice site"*; the figure note: *"Anything within 5 bp is considered not
eligible for targeting with an ASO"*. The criteria are joined by OR, so residual wild-type transcript
removes only the first criterion; a canonical acceptor allele stays "Not eligible" by the 5-bp
criterion. The record's reopening condition is a hypothesis stated as the guideline's outcome, and it
is inconsistent with the record's own scope paragraph. The headline ("what is missing is the
measurement that would place this allele in that class") carries the same slant.

Qualifiers dropped from the source's own surroundings: the figure note continues *"Avoiding +/-5 bp
… is recommended because these variants are most likely destroying canonical splicing … which cannot
be corrected … there are currently ongoing research efforts that aim at identifying ways to
counteract aberrant splicing caused by variants within this region. Should this approach become
feasible in the future, the guidelines will be adjusted."* The record presents the 5-bp rule as an
independent experiment-free route without saying the guideline itself frames it as a proxy for
destroyed splicing. Footnote 7, attached to the quoted "not eligible" sentence, lists two exceptions
(frame-restoring skipping of adjacent exons; ASO-induced exon skipping after cryptic-site usage); the
record handles frame-restoring skipping separately through its exon-9 argument but does not say the
quoted sentence carries a footnoted exception. Milasen statements (gained cryptic acceptor deep in
intron 6, minority of patients amenable, not suited to other patients) match Kim 2019.

A reader trusting only the record would believe that a residual-wild-type result would reclassify the
allele; the guideline's table says it would not.

## N-12, HSP70 co-inducers: SUPPORTED

Both Fog 2018 quotations are verbatim and the first now keeps *"in primary GD fibroblasts"*; the
population is named, the neuronal MASC sentence is kept as its own result with its limit, and the
n = 2-4 per cell line figure matches the Fig. 4c legend. "Could not demonstrate reduced substrate
storage" matches the source (no GlcCer increase in GD fibroblasts, GlcSph undeterminable). The funder
is the compound's owner, as the source states. The three-layer separation holds: the P252A item is
tagged measurement, the acceleration prediction is tagged hypothesis, and D-03's *"could accelerate"*
is verbatim in the dismissal ledger. A reader would not come away believing anything the source does
not say. One unverified observation outside the quoted artefacts: the sentence that arimoclomol
appears "only in a full-text-queue entry and in `D-03`" may be stale, since `paper_registry_current.md`
now holds a Fog 2018 arimoclomol record; it does not bear on any quoted proposition.
