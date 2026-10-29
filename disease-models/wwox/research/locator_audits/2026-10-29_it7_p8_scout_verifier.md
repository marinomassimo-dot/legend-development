# Independent verification of the iteration-7 scout (P8), 2026-10-29

Scope: read-only re-check at the sources of `scout_it7_20261029.md` (commit b6a02b52).
No registration, no contact, no spend. Sources: GitHub API and raw files, Harvard
Dataverse record API, Hugging Face API, Zenodo API, Europe PMC, PubMed metadata,
reactome.org, wwox.org, rareshift.org. One venv created outside the repository for the
ToolUniverse re-run and deleted afterwards (confirmed absent).

## Defects, ranked by severity

| # | Severity | Defect | Evidence at source | Repair |
|---|---|---|---|---|
| 1 | MEDIUM | Orphanet set described as "available upon request (not usable)". The leakage repository README says the opposite: the Orphanet test set is a proprietary dataset "which we are unable to share publicly". "Upon request" was not found in the README or in the paper passage that mentions Orphanet. | repo README, results section; Europe PMC full text of the paper | Replace with "not shared publicly (README)"; drop "upon request" or cite where it was read |
| 2 | MEDIUM | Section 4 says the ToolUniverse wrapper adds two hazards. Only one is added: the 404 reported as `success` with empty data (confirmed). The symbol-mixes-four-species behaviour belongs to Reactome itself: the direct call returns the same 12 rows (the producer's own table says so). | direct call with symbol WWOX: 12 rows, 3 each of Homo sapiens, Bos taurus, Canis familiaris, Sus scrofa; wrapper returns the same | Reword: one wrapper-added hazard; the species mixing is a property of the service that the adapter must handle with an explicit species filter |
| 3 | MEDIUM | PMID 42587157 (Nature 2026) is marked "WATCH until the abstract is read in full" with the abstract "cut". The PubMed abstract is complete and is directly relevant to the rescue-after-onset question: upregulating one gene (Meis2) in PV interneurons of one NDD risk mouse model in adulthood restored PV plasticity, improved cognition and suppressed seizures. The table also says "NDD models" (plural); the abstract reports one risk model as proof of concept. | PubMed metadata for 42587157 | Upgrade to READ for the timing arm; state "one model" |
| 4 | LOW-MEDIUM | PMID 37804316: "the HRI arm (not GCN2/PERK) is shown to be protective". The abstract shows HRI/DELE1 silencing lowers p-eIF2a and "affects cell growth", and that Sephin-1 potentiation helps; it does not test GCN2 or PERK. "Not GCN2/PERK" is inference, not abstract content. Also the Sephin-1 benefit is shown by downstream phosphatase inhibition, not by HRI manipulation in vivo. | PubMed abstract | Remove "not GCN2/PERK" or mark as inference |
| 5 | LOW | PMID 39684432: "microglial state is cell-autonomous (can precede seizures)". The abstract reports a pro-inflammatory quiescent state and impaired phagocytosis; it has no timing against seizure onset and does not establish cell-autonomy. | PubMed abstract | Mark as inference or delete |
| 6 | LOW | PMID 41706892: "abstract truncated in my fetch: remainder UNVERIFIED". The full abstract is in PubMed (protein up without transcript change; OXPHOS protein down; ATF4 deletion in excitatory neurons impairs mGluR-LTD). The claims in the table are supported. | PubMed abstract | Close the UNVERIFIED flag |
| 7 | LOW | Licence-file items listed as UNVERIFIED are in fact retrievable. KG-Bench: `License.md` at the root (MIT, "Copyright (c) 2025 CMBI"). CANDO: `LICENSE.md` (BSD 3-clause text, "Copyright 2019 William Mangione"). drexml: `LICENSE.txt` is MIT but still the unfilled template ("Copyright (c) [year] [fullname]"), a weak grant worth noting. The "LICENSE 404" probe used the wrong filename. | GitHub contents listings and raw files | Update sect. 2 and sect. 5; note the drexml template defect |
| 8 | LOW | rareSHIFT FAQ: "raw sequence-level data excluded (needs additional consent)". The FAQ text read says identifiers, including genetic sequence data, are removed before any sharing. The "additional consent" wording was not found in the passages read. DUA, non-commercial and "Unravel owns the data/results" statements are confirmed. | rareshift.org/faq | Quote the sentence actually read |
| 9 | LOW | The lincs figure "neural-cell shift of 0.147 AUROC" is the README's average class shift across 58 matched mechanism classes (cancer vs iPSC-derived neural), direction unspecified, and a headline of an unreviewed single-author repo; the table's phrasing is close but compresses this. | README | Phrase as "average per-class AUROC shift of 0.147 across 58 classes" |
| 10 | INFO | Not re-checked by me: Creative Commons sub-type of the open-access papers (CC BY-NC-ND etc.), the PMC-flag statements beyond existence of a PMCID, the Section 6 search counts, the Hetionet use in the leakage benchmark, PrimeKG upstream terms, the GitHub star counts. The PMC IDs given exist for all papers marked OA; 40010346 has no PMCID, consistent with "No". | PubMed identifiers | none |
| 11 | INFO | PMID 41512078: PubMed strips italic gene names ("in and transgenic mice"), so the "Mecp2 and Disc1" claim cannot be confirmed from this record. | PubMed abstract | check at the article |

## Confirmed without defect

Licences and facts matching the producer at the source:

- Reactome licence page: "All data in the Reactome database and files derived from that data are licensed under the Creative Commons Public Domain Dedication (CC0)".
- Leakage repository: MIT `LICENSE` ("Copyright 2024 Galadriel Brière"); paper CC BY (Europe PMC).
- KG-Bench paper CC BY; abstract values (AUC 0.91; F1 0.28 at 1:100) match; repo licence MIT (file found, defect 7).
- lincs-detectability-atlas: contents are `.gitignore`, `README.md`, `code`, `results`; the license endpoint returns Not Found, so no LICENSE; README states 86 classes, 11 clearly separable (AUROC >= 0.90), 48 near chance, 0.147 average shift, antiseizure mechanisms (neurosteroids, carbonic-anhydrase inhibitors) detectable only in neural cells. Last push 2026-07-23.
- PrimeKG Dataverse record: version 2, CC0 1.0, last update 2022-05-02. OptimusKG: version 3, CC BY-NC-SA 4.0, updated 2026-09-09.
- Hetionet README: original content CC0, source licences apply, some sources have no licence; last push 2023-04-03.
- opentargets/mira: Apache-2.0 `LICENSE`, last push 2026-10-19. K-Dense: MIT `LICENSE.md`. CANDO last push 2026-07-23. drexml push 2026-06-05.
- TxAgent-T1 model tags include `license:llama3.1` (licence text not read, as the producer states).
- TxGNN: last push 2024-05-06; `txgnn.org` gives no connection (curl code 000) from this host, as stated.
- MATRIX scores: not gated, card has no licence field, README carries only the "Research use only" notice, modified 2026-07-01, 39,508,102 rows. kg-nodes: `LICENSE.md` text matches the quote (CC BY 4.0 for Every Cure's own contribution, upstream restrictions remain), modified 2026-05-28.
- NeMoCAD Zenodo 7692713: access right restricted, version 1.0.1-2, published 2023-03-02, modified 2024-07-12, no licence field. The "free academic and non-commercial" sentence is not in the API description; I could not confirm it (the producer read the web page).
- wwox.org/current-research: the Unravel RNA-map sentences match; no accession or matrix.
- All 19 PMIDs in the mechanism table match the stated titles, journals and DOIs in PubMed (e.g. 42823914 and 42559713 are the PDH guideline and outcomes papers; 39847501 is the SCN1B paper, DOI 10.1172/JCI182584). The WWOX gene-therapy abstract (42422765) matches "neuron-specific, dose-dependent, durable"; SCN1B (P2 not P10) and CSNK2B ("can be corrected after birth", early postnatal replacement) match; Shank3 adult restoration matches.

## ToolUniverse re-run (fresh isolated venv, version 1.5.7)

Install 484 MB, 2,719 tools loaded. `Reactome_map_uniprot_to_pathways`:

| Input | Wrapper result | Direct HTTP |
|---|---|---|
| invalid accession ZZZZZ9 | `status: success`, `data: []`, note "No pathways found" | HTTP 404 |
| symbol WWOX | `status: success`, species Bos taurus, Canis familiaris, Homo sapiens, Sus scrofa | same 12 rows, 3 per species, HTTP 200 |
| Q9NZC7 | success, Homo sapiens only | not re-run |

Both claims are confirmed. The venv directory was deleted and is absent.

## Verdicts against the criteria

The verdicts are consistent with the stated criteria (question served, added value, licence, cost, removal). Reactome TRIAL, leakage-check TRIAL, ToolUniverse REMOVE, OptimusKG REJECT, TxAgent REJECT (cost-based, licence text unread) and the WATCH rows are defensible. Two caveats: the leakage TRIAL should say that the Orphanet comparison set cannot be reproduced (defect 1), so the "cold-start vs independent set" check can only be borrowed in its split logic; and the TxAgent REJECT rests on a hardware assumption, not a measurement.
