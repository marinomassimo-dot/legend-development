# Closing the data gaps the seven deep-recovery abstentions name

> **Actor** `scientist-a` · task `REPURP-10H-FILL-A-20261022` · 2026-10-22 (session clock 2026-10-21). Non-canonical
> research record; touches no card, packet, current file or `repurposing_bridge.py`. **Not medical advice.** Class
> level; no dose, route, schedule or paediatric suitability. Every paper that is not a WWOX study is **NOT WWOX
> EVIDENCE**. Hand-off to the card author, who decides. Statements marked INFERENZA are OWED a blind audit by
> someone else; nothing here narrows a registry claim.

## 0 · What was done and what was not

One new reading was needed and made: PMID 38509072 (read-through determinants; receipt `FTR-20261022-38509072-01`
STAGED not recorded, manifest PASS, 11 locators, `staged_receipt_check.py --check-doi` OK). The other answers came
from papers the repository had already read; for each I re-opened the stored artefact (not the dossier) and say
which surface, because a reading budget is not a licence to read twice what is on disk. Searches (PubMed through the
connector, title/abstract unless stated, 2026-10-21): WWOX with SDR-structure terms, with chaperone/ER terms, with
splice terms, with antisense/read-through terms, with CRISPRa/translation terms, with GSK3/lithium/tankyrase terms,
with missense/stability terms, and a date-limited sweep of WWOX records from 2026-06-01 to 2026-10-22 (20 records,
none a splice-RNA, structure or stability study). A title/abstract zero licenses only "no paper is indexed" (D-37).
Not done: the Neurology 2025 genotype cohort (40875931) and the 2026 Argentine series (42721537) have no lawful
full-text body (not in PMC; the supplement of the first is absent); their variant lists are therefore not read.
Used the shared `files/` layout, but `paper_packet.py rank` found no figure surface because the packet looks under
the worktree; Figure 2 was opened at the native JPEG.

## 1 · A03 client-binding chaperone: STAYS AN ABSTENTION, with a sharper datum

*Missing datum as the card states it*: a ligand known to bind the SDR domain, and a measured instability of Q230P.
*Found*: the card's "no ligand" is too strong. The repository's own reading of the 2011 enzymology paper (21476439;
PDF text re-opened) reports seven steroid substrates with apparent Km values for a WWOX fusion protein, but only in
a bacterial crude extract, unreplicated, no purified protein, no immunodetection of the fusion; the dossier records
that purification destroyed activity. That is a substrate screen, not a binder, and it says nothing about
stabilisation. Instability: none for Q230P; the sole WWOX SDR missense with a turnover assay is P252A (41124647,
stable cell lines, cycloheximide chase): P252A decays faster than wild type and P282A does not (P282A loses
function without a stability defect, same paper). *Sharper datum*: purified wild-type and Q230P protein with a
thermal-shift or limited-proteolysis read, with and without the cofactor and one steroid substrate. *Surfaces looked
at*: Results text, Methods, Table II (dossier, read from the rendered page), Discussion of 29808465 for the Q230P
statement. Absence is not carried by a quote: searched PubMed as above and the repository by string.

## 2 · A04 ER-proteostasis regulators: UNANSWERABLE FROM THE LITERATURE; name the experiment

*Found*: the ER idea originates in the first Q230P report (29808465, PDF re-opened, Discussion): protein loss "more
likely" through ER quality control, with no ER fractionation, marker or inhibitor anywhere in its Methods or Results
(string search for endoplasmic, ER, fraction, MG132, proteasom, lysosom, inhibitor). It is an unmeasured remark. The
only measured route for a WWOX SDR missense is P252A in 41124647 (body text re-opened): the proteasome inhibitor did
not raise wild type, P252A or P282A; chloroquine and ammonium chloride restored P252A; 3-methyladenine did not; the
lost protein is K63-ubiquitinated. Non-neural cells, a different variant, one 6 h proteasome exposure. *Experiment*:
patient fibroblasts, cycloheximide chase with and without lysosome versus proteasome inhibition, three-fraction
(soluble, pellet, total) lysis; this places the lesion before any UPR/ERAD modulator is chosen. INFERENZA: on the
measured evidence a UPR/ERAD modulator has no stated target for this lesion.

## 3 · A05 HSP70 axis: STAYS AN ABSTENTION, sharper

*Found*: the only WWOX measurement involving HSC70 (41124647) is a co-immunoprecipitation with P252A and not with
wild type or P282A, a KFERQ-like motif (residues 187 to 191) and docking; HSC70 was never manipulated, and no function
assay was run under chloroquine (the dossier states this; the interactome paper's list, 30619736, lacks HSPA8).
The abundance of P252A rose under lysosome inhibition; whether the rescued protein works is unmeasured, and P282A shows
a variant can lose function with normal turnover. *Sharper datum*: knock-down of HSC70 or the lysosomal receptor, or
mutation of that motif, on P252A with a function read; then whether the Q230P protein carries the motif exposed.
The sign for Q230P stays unmeasured.

## 4 · B02 read-through class: CAN NOW BECOME A CARD at enumeration and eligibility level (INFERENZA, OWED audit)

*Missing datum*: the enumeration with stop-codon identity and the nucleotide after it. *Supplied* (derived, not read
from a paper): the repository's ClinVar table (1,327 entries, file dated 2026-09-18) with the RefSeq coding sequence
of the transcript fetched this session (1,245 nt; the 33 stop-gain entries all matched the reference codon). 32
single-nucleotide nonsense entries (27 pathogenic or likely pathogenic by the table) plus one duplication-derived
stop. Stop identity: 12 UAG, 10 UAA, 10 UGA. Nucleotide after the stop: 20 G, 6 U, 4 A, 2 C. Position: 24 lie
upstream of the last exon junction (nonsense-mediated-decay-sensitive by the usual rule, so mRNA presence is itself in
question), 8 are in the last exon. *Meaning* (NOT WWOX EVIDENCE; aminoglycosides in HEK293T, ribosome profiling plus
15 CFTR reporter alleles, 13 usable; PMID 38509072): readthrough ranks UGA over UAG over UAA, and C over U over A/G
after the stop; UGAC most permissive, UAAG least; the paper's prediction correlated 0.7 with G418 reporter readthrough
and 0.2 for UAG alleles. By that ranking no entry is in the most permissive combination and 7 are UAAG, the least
(INFERENZA: ranking carried from aminoglycoside data; ataluren and amlexanox contexts are not tested in the paper,
verified by searching the body: the agents occur only in its reference list). *Limits*: ClinVar entries are
submissions, not affected individuals; the pooled "null" class of the largest cohort (56.8 percent null/null in the
abstract of 40875931) is not a nonsense count; no WWOX read-through was ever measured. *Kept*: the reference missense
has no premature stop codon, so none of this applies to it. *Sharper remaining datum*: a dual-luciferase reporter of
the allele contexts (three codons each side, which that paper shows sufficient) under the candidate agent, and mRNA
level for the 24 decay-sensitive alleles.

## 5 · C02 splice ASO: UNANSWERABLE FROM THE LITERATURE; name the experiment

No new WWOX splice-RNA record exists since the repository's census of 2026-09-22 (date-limited sweep above). The
three measured splice alleles remain abstract-depth except the minigene paper (39101447: exon 2 skipping, no
quantification, no NMD block). *Experiment* (already designed, `TX-001`): junction RT-PCR on donor cells with and
without a translation block, capillary electrophoresis and Sanger of every band. The class limit stands: an antisense
cannot rebuild a destroyed acceptor (DL-MOL-011), and for an acceptor in the last exon "skipping" is not a defined
outcome (splice_allele_rna_evidence_20260922.md).

## 6 · C03 CRISPRa boost: UNANSWERABLE FROM THE LITERATURE; name the experiment

Query WWOX with CRISPRa, dCas9, translation efficiency, upstream open reading frame, ribosome profiling or half-life:
1 record (a breast-cancer hypoxia paper, irrelevant). *Experiment*: Q230P versus wild-type cDNA at graded
expression in null cells, cycloheximide chase and three-fraction lysis. A fragment of prior: the P252A and P282A
stable overexpression lines show detectable protein with different turnover, so an overexpressed SDR missense can
accumulate (it does not show that the endogenous message is translation-limited). The never-measured fold of the
variant remains the datum.

## 7 · D02 Wnt/tankyrase: STAYS AN ABSTENTION, sharper (and the direction itself is in tension)

*Found*: a GSK3 inhibitor (lithium) was given acutely before a convulsant challenge to Wwox-null mice and reduced
seizure activity; GSK3 beta serine-9 was dephosphorylated (more active kinase) in cerebellum, hippocampus and cortex
at postnatal day 20 (32000863, body text re-opened, Methods and Results; dose omitted here). No beta-catenin or
reporter was measured and no timing series exists. INFERENZA: a more active GSK3 predicts lower, not higher, Wnt
output, the opposite of the organoid transcript direction the card assumes; the two are different species, ages and
readouts, so the direction is unresolved, not refuted. *Sharper datum*: GSK3 activity and nuclear beta-catenin or a
reporter, in the same null neural tissue and age, with and without the inhibitor. The "never administered" wording of
the card is repaired in the card repair of the same day.

## 8 · The gap that would most change which card is worth discussing

Whether the Q230P protein is made and cleared (by which route) or never made. It decides A02, A03, A04, A05 and C03
together; the repository holds one patient-fibroblast western and no inhibitor arm. As a question for a treating
team's discussion, never advice: which of these routes is open to testing in material that already exists?

## 9 · DEFAULTS_TAKEN, OWED, STOP, self-evaluation

DEFAULTS_TAKEN: re-opened stored artefacts instead of re-reading papers formally; used ClinVar and the RefSeq CDS as
databases, not as readings; dates per session clock. OWED: blind audit of §2 (the proteasome-insensitive wording),
§4 (census arithmetic and the transfer from aminoglycoside data), §7 (the GSK3 direction tension). STOP_LOG: empty;
the gap-fill task was interrupted once by the card repair and resumed. Self-evaluation: the weakest link is §4's
transfer across agents; I stated it, did not test it. A second reading (the genome-wide aminoglycoside source) would
check the ranking and was not made.
