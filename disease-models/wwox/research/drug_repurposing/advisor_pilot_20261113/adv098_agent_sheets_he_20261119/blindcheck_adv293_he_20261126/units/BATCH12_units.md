# Sheet batch 12: BATCH12_ADV113_M1comparators_pirenzepine_telenzepine_VU0255035_and_TMP195_classIIa_OL_null_HE_20261120.md
Each numbered unit is a sentence of the repository sheet, in order. L = line in the sheet.


## Answer first
U12.1 (L6) **Part A (IT50-Q09): no disclosed-structure M1-selective antagonist has a measured EBP datum by the routes searched, and the one primary datum that exists is indirect and does not name its compounds in the text layer.**
U12.2 (L6) ChEMBL holds 334 activity rows on the four EBP targets (264 molecules) and none is for pirenzepine, telenzepine, VU0255035, clemastine or benztropine; Europe PMC abstract searches pairing EBP, emopamil binding protein or sterol isomerase with pirenzepine, telenzepine or "M1 antagonist" returned 0 records.
U12.3 (L6) The only primary datum is Hubler 2018 (PMID 30046109, held full text): of a panel of six muscarinic antagonists that all inhibited M1, M3 and M5 at the 2 microM screening dose, **only clemastine and benztropine inhibited EBP in OPCs**; the six are named only in an Extended Data figure that the text layer does not carry.
U12.4 (L6) So the pair is separated from the muscarinic route **inside Hubler's own panel by four non-EBP muscarinic antagonists whose identity I could not read**; pirenzepine and telenzepine are two of five muscarinic reagents named in the Methods (INFERENCE that they are among the four).
U12.5 (L6) The design therefore cannot rest on "the M1-selective comparator has no EBP activity" as an assumption: it needs a measured sterol arm for the comparator chosen.
U12.6 (L7) **Part B (WO-32): a bounded null, with two routes and the second one now run.**
U12.7 (L7) No record found by Europe PMC (SCI, 41 title-and-abstract records, 2026-11-18; HE census, 2026-11-20) or by a PubMed-native title/abstract search (HE, 2026-11-20) reports a loss-of-function, gain-of-function or class IIa-inhibitor result in an oligodendrocyte-lineage cell with a differentiation or myelin readout.
U12.8 (L7) The class IIa myelin results with a function readout are Schwann-cell (peripheral).
U12.9 (L7) It is a bounded null of abstract-level searches, **not a verified absence** (section "What it cannot say").

## Identity (one line per agent, how it was resolved)
U12.10 (L10) | Agent | Resolution | ChEMBL read | Structure key |
U12.11 (L12) | pirenzepine | the ChEMBL molecule record carries the preferred name PIRENZEPINE (parent equals itself in all 173 rows) | CHEMBL9967 | InChIKey RMHMFHUVIITRHF-UHFFFAOYSA-N (ChEMBL molecule record, read 2026-11-20) |
U12.12 (L13) | telenzepine | the ChEMBL molecule record carries the preferred name TELENZEPINE (7 rows) | CHEMBL253978 | InChIKey VSWPGAIWKHPTKX-UHFFFAOYSA-N (ChEMBL) |
U12.13 (L14) | VU0255035 | no preferred name stored in ChEMBL; resolved by structure: PubChem name lookup "VU0255035" returns CID 24768606 (C18H20N6O3S2, N-[3-oxo-3-(4-pyridin-4-ylpiperazin-1-yl)propyl]-2,1,3-benzothiadiazole-4-sulfonamide), whose InChIKey equals the ChEMBL molecule's | CHEMBL1628667 (3 rows) | InChIKey WXDHQWPQLKGANZ-UHFFFAOYSA-N (both) |
U12.14 (L15) | TMP195 | resolved in batch 10 by structure (PubChem name lookup, then the ChEMBL molecule with the same InChIKey) | CHEMBL4751615 | PubChem CID 67324851, InChIKey QTCSXAUJBQZZSN-UHFFFAOYSA-N (batch 10, line 9) |

## COMPARABLE?
U12.15 (L18) **Pirenzepine M1 selectivity: comparable only within a document, and the within-document ratios run from about 1.7-fold (M5 against M1, CHEMBL1137537, 2007) to about 180-fold depending on the document, subtype and species.**
U12.16 (L18) Human receptors: CHEMBL2311283 (2013, Ki, nM) M1 9.1, M2 524, M3 158, M4 105, M5 126 (M3 17-fold, M5 14-fold, M2 58-fold above M1); CHEMBL1132561 (1999, IC50, nM) M1 28.2, M2 968, M3 956, M4 247, M5 341 (M3 34-fold, M5 12-fold); CHEMBL1155803 (2008, Ki) M1 2.8, M2 174, M3 48, M4 13.8 (M3 17-fold, M4 5-fold).
U12.17 (L18) Rat receptors: CHEMBL1127012 (1993, Ki) M1 5.2, M2 267, M3 28 (M3 5.4-fold); CHEMBL1126912 (1993, Ki) M1 6.5, M2 794, M3 174, M4 34.7 (M3 27-fold, M4 5.4-fold); CHEMBL1131857 (1999, IC50) M1 3.8, M2 690, M3 300 (M3 79-fold).
U12.18 (L18) Medians of the rows in each document; one document is one origin, and the documents are not independent of each other where one quotes another (not checked).
U12.19 (L18) **No single selectivity figure is given.**
U12.20 (L18) Rows labelled only "Muscarinic acetylcholine receptor" without a subtype (CHEMBL1124460, mouse in vivo binding, 750 nM; CHEMBL1125425, rat cortical homogenate, 213 and 322 nM) are whole-tissue measurements, not subtype data, and are not used.
U12.21 (L19) **Telenzepine against pirenzepine: one document has both (CHEMBL1125581, 1991, rat, Ki, nM).**
U12.22 (L19) Telenzepine M1 1.8, M2 50.3, M3 6.9, M4 17.4 (M3 only 3.8-fold above M1); pirenzepine in the same document M1 29, M2 610, M3 240, M4 330 (M3 8.3-fold).
U12.23 (L19) Telenzepine is about 16-fold more potent at M1 than pirenzepine in that document and **less** M1-selective against M3.
U12.24 (L19) Telenzepine has no other subtype document in the pull (7 rows: 4 muscarinic, 1 BSEP, 2 SARS-CoV-2).
U12.25 (L20) **VU0255035: M1 only, no selectivity panel in the rows.**
U12.26 (L20) Human M1 antagonist IC50 690 nM in two documents (CHEMBL1938324 and CHEMBL2057199, both 2012, calcium-mobilisation assays in CHO cells; the two are the same laboratory's numbers quoted in two documents, so one origin until shown otherwise) and rat M1 240 nM (CHEMBL1938324).
U12.27 (L20) The subtype selectivity it is known for is **not in these rows**: not found by that route, not absence.
U12.28 (L21) **The screening dose changes what "M1-selective" can mean in Hubler's panel (INFERENCE, arithmetic only).**
U12.29 (L21) At the 2 microM screening dose the ratio of dose to the human pirenzepine Ki (CHEMBL2311283) is about 220 at M1, 16 at M5, 13 at M3 and 4 at M2.
U12.30 (L21) Ratios only: they ignore agonist competition, assay conditions and the species of the receptors in Hubler's assay; they say the panel tested muscarinic blockade at M1, M3 and M5, which Hubler states, not M1 selectivity.

## Pirenzepine (CHEMBL9967)
U12.31 (L25) **Potency (173 rows):** muscarinic subtype rows as in COMPARABLE?; off-target rows are two: human BSEP IC50 above 1,000,000 nM (CHEMBL4017441, 2012) and SARS-CoV-2 cytotoxicity-protection IC50 above 20,000 nM (2 rows, CHEMBL4651402, 2021).
U12.32 (L25) **No row on EBP (CHEMBL4931, CHEMBL5525, CHEMBL3774293, CHEMBL2311238).**
U12.33 (L26) **EBP, repository lane (read):** `m1_ebp_reagents_sci51_20261113/README.md` (the reagent PIPE-307 has no public structure; Correction PMID 39432800 and Expression of Concern PMID 40512803 are in that README; SCI51 reformulated Q09 to "measure EBP of a disclosed-structure M1-selective antagonist"); `ebp_reannotation_adv001_20261113/verify/audit.md` lines 31 and 76 (Hubler's Methods name scopolamine, homatropine, pirenzepine, telenzepine and p-fluorohexahydro-sila-difenidol as muscarinic reagents; "probably among" the four inert slots, INFERENZA there).
U12.34 (L27) **EBP, held primary text (read in the held XML, `PMC6423962`):** "a panel of six muscarinic receptor antagonists that all showed near-completed inhibition of the M1, M3, and M5 muscarinic receptor subtypes at the HTS dose of 2 uM (Extended Data Fig.
U12.35 (L27) Among these molecules, only clemastine and benztropine inhibited EBP in OPCs, and only clemastine and benztropine enhanced oligodendrocyte formation." The Methods reagent list names scopolamine and homatropine among purchased compounds, followed by "Pirenzepine and Telenzepine were purchased from Sigma-Aldrich as a 10 mM DMSO solution" (p-fluorohexahydro-sila-difenidol is named in the repository's audit of the Methods, not found in the text layer by my search for its abbreviation).
U12.36 (L27) **The six are not named in the text layer; their membership of the panel is inferred, not read.**
U12.37 (L27) Readout: sterol intermediates in EpiSC-derived OPCs at one dose; no Ki, no concentration-response.
U12.38 (L28) **Not checked:** the Extended Data figure itself (a human visit or a figure read), Sax 2022 supplement, PubChem BioAssay, Allimuthu 2019 Data S1/S2.

## Telenzepine (CHEMBL253978)
U12.39 (L31) **Potency (7 rows):** as in COMPARABLE?.
U12.40 (L31) In Hubler's Methods with pirenzepine (see above).

## VU0255035 (CHEMBL1628667)
U12.41 (L34) **Potency (3 rows):** as in COMPARABLE?; no EBP row.
U12.42 (L34) It does not appear in Hubler's Methods list as read.
U12.43 (L35) **Why it matters:** it is the best-known disclosed-structure M1-selective antagonist outside the classic pair, but its EBP activity is **not found by these routes**.

## EBP-target pull (the negative side of the question)
U12.44 (L38) **Rows:** EBP targets CHEMBL4931 (human, 145 rows), CHEMBL5525 (guinea pig, 132), CHEMBL3774293 (mouse, 53) and CHEMBL2311238 (EBP-like, 4): **334 activity rows, 264 molecules**; none of the five molecules of this question (pirenzepine, telenzepine, VU0255035, clemastine CHEMBL1626, benztropine CHEMBL1201203) is among them.
U12.45 (L38) The rows are recomputable by the recipe line and are not saved in git.
U12.46 (L39) **Europe PMC (abstract level, 2026-11-20):** EBP, emopamil-binding protein or sterol isomerase with pirenzepine, telenzepine or an M1 antagonist: 0 records.
U12.47 (L39) **Not found by those two routes; a second kind of route (PubChem BioAssay, supplementary tables) was not run.**

## What was tested, where, at what exposure
U12.48 (L43) **No oligodendrocyte-lineage experiment was found.**
U12.49 (L43) The held reading of SCI (`WO32_LITERATURE_HALF_SCI_20261118.md`, verdict "mixed": bounded null for function, discordant for expression) stands; I re-ran it from the other side without reusing its strings.
U12.50 (L44) **Europe PMC (HE, abstract level, earlier on 2026-11-20 in the previous HE window; counts carried from that window's working notes and not re-run in this one):** class IIa with oligodendrocyte, myelination or OPC terms: 9 records; TMP195 with oligodendro or myelin: 9 (none relevant: glioblastoma, astrocytic HDAC7, reviews); MC1568 with OL terms: 25 (reviews and stroke); title-level HDAC4, 5, 7, 9 or class IIa with OL or myelin: 1 record, PMID 29472387 (Schwann cells, J Cell Biol 2018: peripheral).
U12.51 (L44) Two queries (HDAC4 and HDAC5 with oligodendro*, myelin* or OPC in title or abstract) timed out in the previous window and were **re-run in this one** (plain request, no contact parameter, 2026-11-20): HDAC4 10 records, HDAC5 8.
U12.52 (L44) Besides records already counted (Schwann cells 29472387 and 35076395 with its preprint, the two stroke papers 24657831 and 25967576, 27103167, 39238786, 37104592, 40650056 review, 30913399 Schwann cell line autophagy), the new titles are: 25791281 (2015, HDAC and co-factor expression mapping in human gliomas: a tumour study), 30269419 (2019, sympathetic nervous system and skeletal muscle innervation), 38244175 (2024, exercise and fluoride-induced learning impairment in mice), 36943192 (2023, miR-124-3p and Gpm6a in the hippocampus of stressed rats) and a 2026 preprint on histone acetylation, BDNF and the hippocampal transcriptome; **by title, none is an oligodendrocyte-lineage experiment** (titles only; abstracts of these five were not read).
U12.53 (L45) **PubMed-native (HE, 2026-11-20, plain client, title/abstract field tags; the second route SCI's note says was missing):** HDAC4 with oligodendrocyte or myelination: 5 records (29472387 Schwann; 35076395 Schwann, eLife 2022; 24657831 rat stroke, expression only; 27103167 rat stroke, MC1568; 39238786 optic neuritis blood transcriptomics, not a lineage experiment).
U12.54 (L45) HDAC5: 2 (29472387; 37104592, a 2023 Science study of human-specific deletions in conserved elements whose abstract mentions HDAC and myelination gene expression after reverting a deletion: abstract only, not a class IIa perturbation in a lineage cell).
U12.55 (L45) HDAC7: 3 (35076395; 39238786; 41591814, a 2026 JCI glioblastoma study in which the transcription factor OLIG2 recruits HDAC7 to repress CXCL10: tumour stem-like cells and macrophages, not oligodendrocyte myelination).
U12.56 (L45) HDAC9: 1 (35076395).
U12.57 (L45) The inhibitors MC1568, TMP269, TMP195 or LMK235 with oligodendrocyte, myelin or remyelination: 1 (27103167).
U12.58 (L45) **Distinct records returned by the five PubMed queries: 7 (29472387, 35076395, 24657831, 27103167, 39238786, 37104592, 41591814; the others are overlaps); none is an oligodendrocyte-lineage experiment.**
U12.59 (L45) I read only abstracts (the abstracts of 37104592, 41591814 and 39238786 in full from the metadata record; the others as SCI and IT29 read them, from their notes).
U12.60 (L46) **The only class IIa result with a myelin readout and an inhibitor is a stroke outcome study (27103167):** MC1568, a class IIa inhibitor, started 24 h after stroke in rats, increased mortality and lesion volume and lowered MBP among other markers; SCI and IT29 read it as confounded by viability.
U12.61 (L46) **Exposure in the oligodendrocyte lineage: not stated** (abstract level); not an OPC experiment.
U12.62 (L47) **Where class IIa HDACs and myelination do meet with a function readout it is peripheral:** Schwann cells (29472387, 35076395): HDAC4 and HDAC5 are needed together for timely myelination, with HDAC7 then HDAC9 compensating after further loss.
U12.63 (L47) This is PNS, a delay under double or triple loss, not a CNS myelin lever.
U12.64 (L48) **RNA half (IT, 2026-11-15, held tables):** all four class IIa genes are detectable in the mouse lineage (GSE52564), none is oligodendrocyte-enriched; in the human adult cortex groups (GSE73721) the oligodendrocyte group is below the 1.0 floor for HDAC4, 5 and 7.
U12.65 (L48) One 2012 immunostaining abstract (23671795) reports HDAC9 absent from oligodendrocytes (methods not read by SCI; PMC page returned a reCAPTCHA).
U12.66 (L48) Expression: discordant, not resolved.

## TMP195 (CHEMBL4751615), the three passes
U12.67 (L51) **Pass 1, label, registry and first papers:** no label (a research compound); ClinicalTrials.gov intervention search 0 studies; potency and exposure as in batch 10 (class IIa enzyme IC50 2.4 to 354 nM; cell activity 0.9 to 3.0 microM; no brain cell data).
U12.68 (L52) **Pass 2, the repository's own lane (read):** `wo32_classiia_ol_it55_20261115/README.md` (RNA half and the 2026-11-18 update) and `WO32_LITERATURE_HALF_SCI_20261118.md` (Tier 1: 41 records; Tier 2: 107 titles advanced and screened at abstract level; **0 of 107** met the gene-and-lineage filter).
U12.69 (L52) I did not redo SCI's screens.
U12.70 (L53) **Pass 3, harm-term re-search (PubMed, title/abstract, 2026-11-20):** (TMP195 or TMP269) with neurotoxicity, toxicity or neuron: 5 records.
U12.71 (L53) Read at abstract level: (a) PMID 39362994 (Commun Biol 2024, KMT2A-rearranged leukaemia xenograft): "the maximum achievable dose of LMK-235 was insufficient to induce anti-leukemic effects in vivo.
U12.72 (L53) Similar results were obtained for the specific class IIA HDAC inhibitors MC1568 and TMP195": an **exposure-limited** in vivo result in a non-neural tumour model, not a toxicity finding; (b) PMID 42332767 (Alzheimers Res Ther 2026, APP/PS1 mice): TMP195 given intraperitoneally "attenuated IKK-NF-kB signaling, reduced the presence of neurotoxic reactive astrocytes, and rescued neurodegeneration and cognitive deficits": the abstract states **no adverse effect and no myelin or oligodendrocyte readout**, and the dose, brain concentration and any safety observations are **not read** (full text not read); (c) 36732057, 36362189, 28839000: radiosensitisation and leukaemia studies with TMP269/TMP195 or a class IIa inhibitor, no neural tissue.
U12.73 (L53) **Not found by these routes: a published adverse effect of TMP195 on myelin, oligodendrocytes or neurons; this is the absence of a result in abstracts, not evidence of safety.**

## What it cannot say
U12.74 (L56) **It cannot say class IIa inhibition is harmless or inert in oligodendrocytes.**
U12.75 (L56) No oligodendrocyte-lineage experiment was found; absence of a result is not a result of no effect.
U12.76 (L57) **Abstract level only.**
U12.77 (L57) Class IIa genes can be studied in a Hdac4 conditional knockout whose abstract names neither oligodendrocytes nor myelin, or in a table; full-text matches were screened only by title (SCI's 692 Tier 2 titles, 107 advanced and read at abstract level); IT's census counts of 278 (HDAC9) and 215 (HDAC7) full-text-wide records were never opened and are not reconciled with SCI's counts (different query strings).
U12.78 (L58) **TMP195 exposure in the central nervous system is not known from these routes**: no brain or plasma concentration was found (batch 10), and the one in vivo brain-disease paper (42332767) has no exposure figure in its abstract.
U12.79 (L59) **Two further routes not run** (Google Scholar, OpenAlex full text): the rule that an absence claim needs two routes is met only for the abstract-level searches (Europe PMC plus PubMed), not for full text.
U12.80 (L60) **Species and age:** the stroke work is adult rat, the lineage RNA is mouse P17 sorted classes and human adult cortex groups, the Schwann work is mouse and rat.

## What is not found by these routes
U12.81 (L63) **Part A:** a measured EBP activity, or a documented absence, for pirenzepine, telenzepine, VU0255035 or any disclosed-structure M1-selective antagonist, in ChEMBL (334 EBP rows) or in a Europe PMC abstract search; the names of the six muscarinic antagonists of Hubler's panel (the Extended Data figure); an M1 selectivity panel for VU0255035 in ChEMBL.
U12.82 (L64) **Part B:** a primary report of class IIa HDAC loss, inhibition or overexpression in an oligodendrocyte-lineage cell with a differentiation or myelin readout (Europe PMC and PubMed title/abstract); a published adverse effect of TMP195 on myelin, oligodendrocytes or neurons; a TMP195 brain or plasma concentration.

## Dated addition, 2026-11-20 (HE, ADV-113): batch 10's TMP195 exposure line, and the checkpoint's wording on Part A
U12.83 (L67) **Batch 10, TMP195 exposure bullet ("whether TMP195 was given to animals ... is not read"):** the abstract of PMID 42332767 (2026, APP/PS1 mice) states that TMP195 was given by intraperitoneal injection and attenuated neurotoxic astrocyte signalling and rescued neurodegeneration and cognitive deficits; the astrocytic HDAC7 paper therefore **did** give TMP195 to animals.
U12.84 (L67) Its dose, any brain concentration and any safety observation are not read (abstract only).
U12.85 (L67) PMID 39362994 (xenograft) reports that the maximum achievable dose of class IIa inhibitors including TMP195 did not produce an anti-leukaemic effect in vivo, an exposure-limited result in a non-neural model.
U12.86 (L67) The original wording above in batch 10 is unchanged.
U12.87 (L68) **Correction to my own earlier working note (not in a sheet):** I had described the documents CHEMBL1124460 and CHEMBL1125425 as a "panel placeholder" giving one value for all five subtypes.
U12.88 (L68) Read in the rows, they are subtype-less whole-tissue binding rows (mouse in vivo, rat cortical homogenate), not subtype panels; they are excluded from the selectivity figures for that reason.
U12.89 (L68) I had also described the pirenzepine selectivity documents as rat only; ChEMBL holds three human-receptor documents (CHEMBL2311283, CHEMBL1132561, CHEMBL1155803), listed in COMPARABLE?.

## What changes
U12.90 (L71) **For the benztropine/clemastine reagent pair:** the pair cannot be justified by "the M1-selective comparator has no EBP activity" from public data: there is no measured EBP datum for any disclosed M1-selective antagonist.
U12.91 (L71) The one primary datum (Hubler's six-antagonist panel) is a one-dose, indirect readout, and the four inert antagonists are not named in the text layer.
U12.92 (L71) Candidates for a no-EBP comparator, if they were in the six: pirenzepine and telenzepine (INFERENCE), but their M1 selectivity within documents is only 4- to 180-fold and at Hubler's 2 microM dose it is erased; telenzepine is less M1-selective against M3 than pirenzepine in the one document that holds both.
U12.93 (L71) **The design needs its own measured sterol arm for the comparator it chooses**; the decision (a pair, or clemastine alone, ADV-113's question) rests on that arm, not on a literature value.
U12.94 (L72) **For WO-32:** the class IIa row is a bounded null for oligodendrocyte-lineage myelination by Europe PMC and PubMed abstract searches, with a search record (this sheet and SCI's note) a later reader can reuse; it does not keep TMP195 out of a comparison on safety grounds, because no harm finding was made and no exposure was found, and it does not put it in on efficacy grounds, because no lineage result exists.
U12.95 (L72) **What would reopen it:** an oligodendrocyte-lineage deletion or catalytic-dead allele of HDAC4 or HDAC5 (with HDAC7 and HDAC9) with a CC1, MBP or g-ratio readout, or a class IIa compound with a knockout control in OPC differentiation culture; or a read of 23671795's methods.
