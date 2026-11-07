# NB-4 delta: two checks on the recombination premise (Synapsin I-Cre, Wwox conditional deletion)

Non-canonical, not medical advice. Reference genotype class only. Label `nb4d-p`, receipt suffix 50. Delta against `nb4_gse158684_glia_20261107`; nothing in a shared consumer was changed.

## Answer first

* DATO. Check A: the direct characterisation of the line (PMID 35966957, same stock, Jax 003966) was read as text by me (Europe PMC fullTextXML; receipt depth partial_fulltext_read, references not read; figures captions only). Its reporter is an X-linked Mecp2-mCherry-Stop allele, read in male mice at 6-8 weeks. It reports 26.2 percent recombined reporter DNA in whole brain (Southern) and reporter activation in 36 percent of NeuN-high nuclei (flow, n = 3 per genotype). `A05 A06 A04`
* DATO. The same paper reports incomplete activation in cortex, efficient in dentate gyrus and CA3, minimal in cerebellum and CA1 (one mouse per genotype, qualitative), and says it cannot rule out reporter activity in a significant subset of glia. It never measures parvalbumin cells, Wwox, progenitors or any age before 6 weeks. `A07 A08 A12 A13`
* DATO. Check B: there is no tdTomato panel in the places the pilot pointed to. Supplementary Fig 1C-D are WWOX immunostainings (NeuN and CC1 counterstains) at P17, not reporter images; tdTomato is named once, in Methods. Panel D shows WWOX present in CC1-positive cells of the S-KO corpus callosum; panel C shows WWOX lost in four arrowed NeuN-positive cortical cells, with other NeuN-positive cells in the same S-KO field still showing signal. `B01 B04 B05`
* INFERENZA. The mosaic-deletion premise is confirmed in direction and withdrawn as a number: "a third of neurons" may not be written for Wwox, for the cortex, for P9-P21 or for parvalbumin cells.
* INFERENZA. Glial reading (d) of the pilot (recombination beyond the expected cells) loses support for mature oligodendrocytes of one callosal field and stays open for astrocytes, microglia, progenitors and cortical glia (no S-KO astrocyte panel exists; the glial markers in Paton are absent). Not excluded.
* IPOTESI. Parvalbumin-cell recombination under Synapsin-Cre is unknown and could be lower, equal or higher than the whole-brain neuron figure; the test that discriminates is the per-animal control at the end.

## Confirm

The deletion is mosaic or incomplete in part of the brain: both an independent adult reporter study (36 percent of NeuN-high nuclei; cortex "incomplete") and the Wwox paper's own S-KO cortical field (unarrowed NeuN-positive cells with WWOX signal) point the same way. `A06 A07 B04`. The stock number is the same (003966, both papers, `A02 B02`); neither paper shows that the two colonies are the same.

## Narrow

* "Reporter in about a third of neurons" (pilot note, from the auditor's secondary description) becomes: 36 percent of NeuN-high nuclei, whole brain, males, 6-8 weeks, Mecp2-mCherry-Stop reporter, n = 3. Reporter protein activation in nuclei is not excision of a floxed Wwox exon, and the locus, the allele type and the age differ from the Wwox cross (Wwox exon 1 floxed, Rosa26 reporter, mixed 129 background, phenotype P9 to death at 3-4 weeks). Do not carry 36 or 26.2 or 25 percent from one condition to another. `A04 A05 A06 B02 B03`
* Reading (d): the one glial datum with an actual Wwox read-out is Supp Fig 1D, mature-oligodendrocyte marker, corpus callosum, one field, P17, no count, WWOX present in S-KO. This weakens (d) for that lineage and place only. `B05`
* The glial negative in Paton is not a negative: neuron-level reporter is at least six-fold stronger than glial, so activated glia would be hard to see; NeuN-low nuclei also include NeuN-poor neurons (Purkinje, mitral). `A08 A09`

## Withdraw

* The pilot's expectation that Supplementary Fig 1C-D would show a tdTomato panel: they are WWOX stainings; no tdTomato panel was found in any text surface or in the one supplementary page viewed (`B01`). Other image pages were not viewed, so this is "not found in the surfaces read", not "no such image exists".
* "Read by the auditor": superseded. The only reading with a receipt is mine (full text of the Paton article, figures as captions; the Zenodo extended data and Supplementary Fig 1 gating were not reached). Nothing is backdated to the auditor.
* Any reading of Supp Fig 1C as proof of neuron-wide deletion: it is a single representative field.

## Still open

* Fraction of parvalbumin cells recombined in S-KO (no source read). Fraction by cortical layer and region at P9-P21. Astrocyte, microglia and progenitor recombination under this Cre with a Wwox read-out. Whether Cre passage through the male line produced germline Wwox recombination (Paton: weak reporter activity in testes; Paton did not measure transmission; the Wwox paper text read states no breeding direction). Whether a tdTomato image exists in unviewed main or supplementary figure pages. The locus-specific efficiency of Cre at Wwox exon 1 versus Mecp2-Stop: unmeasured. `A11 A12 A13 B01`
* Reading and depth: Paton figures captions only; Zenodo underlying data not fetched; gene symbols were stripped by the PMC text tool and recovered from the XML (degraded route, no gap filled by inference).

## Proposed wording for INV-15 (replaces the pilot's sentence on the Cre line)

"The deletion is neuron-targeted by design (Synapsin I-Cre, Jax 003966). An independent characterisation of the same line with an Mecp2 reporter in adult male mice found reporter activation in 36 percent of NeuN-high brain nuclei, incomplete in cortex and minimal in cerebellum, and could not exclude activity in a subset of glia; the Wwox paper's own P17 cortical field shows WWOX retained in some NeuN-positive cells; in one callosal field WWOX is present in some CC1-positive cells of the knockout. Neither source measured parvalbumin cells. The neuronal deletion is therefore treated as incomplete and cell-type unknown; no recombination percentage is assigned to parvalbumin cells."

## The experimental control the new data make necessary

* IPOTESI, test: in every animal used for a parvalbumin measurement (S-KO and controls, P14-P17 so as to match the phenotype window, not adulthood), on the same sections: a parvalbumin marker, the already-present Rosa26 tdTomato reporter, and a Wwox read-out (WWOX immunostaining validated against the glial-Cre positive panels, or Wwox in situ). Report per animal: fraction of parvalbumin cells tdTomato-positive, fraction WWOX-negative, and their concordance (WWOX in tdTomato-positive versus -negative parvalbumin cells), by region and layer. Reporter recombination is a proxy; the concordance is what licenses using it. Add a glial arm (astrocyte and oligodendrocyte-lineage markers) in the S-KO and note the Cre transmission direction of each breeding.
* Not decided by these data: whether the S-KO phenotype needs more than the recombined share, or whether Wwox exon 1 recombines more efficiently than Mecp2-Stop.

## Held-artefact note

Wwox paper: held print text, supplement File009 (page 7 only rendered and viewed) and three xlsx files searched by shared strings; the held artefacts are in the shared checkout under `files/fulltext/`. `prior_receipt` for PMID 33914858 is `FTR-20261101-33914858-01` (latest by event time; earlier receipts, including `FTR-20261003-33914858-03` with figures read, are listed in the receipt). Figures were viewed only for Supplementary Fig 1 (A-F, page 7).

Counts: evidence rows 21 (rows that are counter-evidence in role: A09, A13, B04, B06, B07; the rest support or describe). Queries: `queries.tsv`. Receipts: `receipts/INDEX.tsv`.

## Added after the independent audit (`../verify/audit_nb4d.md`: 19 of 21 supported; A10 and B02 narrowed in `evidence.tsv`)

Points the auditor adds, now part of the reading: (1) Paton's 26.2, 36 and 25 percent describe an X-linked Mecp2 reporter in hemizygous males at 6-8 weeks, not excision of the autosomal floxed Wwox exon 1 (flox/flox, P17); none transfers to Wwox excision in any cell class. (2) Paton sampled adults, whereas S-KO animals seize from P9 and die at 3-4 weeks; the only developmental statement, E12.5 onset, is Zhu's LacZ result cited by both papers. (3) The Wwox paper's "neurons, but not in other cells" rests on one glial type, mature CC1-positive oligodendrocytes in one callosal field; Supp Fig 1C shows loss in the four arrowed cells with no counts (one field per genotype); Supp Fig 1D is patchy, and CC1 marks mature oligodendrocytes only. (4) Genetic background differs (C57BL/6JCrl in Paton; a C57BL6/J;129sv mix in the Wwox conditional models). (5) Paton's references carry two germline-recombination reports (Rempe 2006; Luo 2020) and it saw weak testis activity; the Wwox paper does not discuss germline excision of the Wwox flox allele. (6) Both sources agree that Syn1-cre excision is partial and mosaic; neither measures glia directly. The absence claims (no tdTomato panel in Supp Fig 1, main Fig 4 and 6 as images, nor in any text surface; no parvalbumin, Wwox, glial-subtype or progenitor mention in Paton) were confirmed; main Fig 1-3, 5, 7 and Supp Fig 2-9 were not viewed as images by anyone. The corrections narrow wording at the points the audit named and were rechecked only by string comparison against the audit text.
