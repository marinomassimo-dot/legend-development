# IT28 P12: targeted scouting, four named gaps (2026-11-05)

Non-canonical. Not medical advice. Zero spend; no registration, login or contact; no e-mail address sent anywhere. Only generic topic
words went to the search service. Nothing installed, cloned or downloaded; no third-party raw data imported. WWOX not used as keyword.
Depth: one bounded window, web search plus two page reads and one key-less repository metadata call; repositories not opened, so code
revisions are unread. Not repeated: Papyrus/BindingDB (IT21/IT24), iPSC astrocyte/microglia CRISPRi GSE182307 (IT27 P13-8), preon,
GraphGuest, scPerturb, G-SRS. Table: `candidates.tsv`.

| Gap | Hit | Verdict |
|---|---|---|
| G1 class IIa assay-level data | Papyrus 5.7 read: has AID/doc_id but no substrate, construct or assay text; PubChem/ExCAPE not searched past the Papyrus paper | REJECT (nothing new) |
| G1 | ChEMBL assay descriptions already held: use in-house | TRIAL, 3 h |
| G2 protein-level ISR v RNA | none; only non-neural ATF4-reporter CRISPRi screens and one ISR bulk-proteomics preprint | nothing new / WATCH |
| G3 shared origin | DupChecker (file-hash duplicates, 2015, Affymetrix-era) cannot see our rows; build an in-house accession/DOI grouper | REJECT tool, TRIAL in-house 4 h |
| G4 neural/glial CRISPRi with composition | iAssembloid CRISPRi (Neuron 2025) | WATCH, 2 h |

## Notes

**G1.** Papyrus keeps only molar Ki/KD/IC50/EC50 and flags type; the Papyrus++ tier filters IC50 by cross-assay concordance (0.5 log units),
which averages over exactly the substrate differences that matter for class IIa. So it hides the variable rather than exposing it. Search
context worth keeping as dossier background (secondary, abstract-level): class IIa enzymes have very low turnover on standard acetyl-lysine;
trifluoroacetyl-lysine substrate is used to get signal; some activity in HDAC4 assays was attributed to co-purified class I enzymes (Lahm 2007);
trifluoromethyl ketone binding kinetics are class-dependent (Madsen and Olsen 2016), so preincubation changes IC50. A vendor page lists CHDI-390576
values that differ with Boc-Lys-TFA format. No open dataset separates substrate class; the lawful route is ChEMBL free-text assay descriptions
(open, already held) and open-access primary papers. Expect incomplete substrate text for closed papers: report "not stated" rather than infer.

**G2.** Closest items: CARS regulates ATF4 translation independent of eIF2a-P (bioRxiv 2024, CRISPRi, ATF4 reporter sorting); DELE1-dependent
ATF4 translation; an ISR cell-type preprint (snRNA/ATAC plus bulk proteomics). Reporter ratio is a protein-level readout but in non-neural lines.
Reopen if a neural line with eIF2a-P or ATF4 protein readout and a gene list appears.

**G3.** DupChecker computes MD5 of raw files; authors state re-profiled specimens are missed, and accession IDs hide duplicates (463 of 608
samples had duplicates under different GEO ids). Bgee reports about 14 percent duplicated content. Lesson for LEGEND: shared accession is
sufficient but not necessary for shared origin; the in-house check should also group by cohort name, author-group overlap and sample counts.

**G4.** Only iAssembloid is multi-cell-type; the screen phenotype is neuronal survival, so composition is a culture feature, not an annotated
outcome. Accession not verified (GSE272094 appeared in a listing next to it).

No adoption quota applies; the two TRIAL items are in-house work, no third-party material imported.
