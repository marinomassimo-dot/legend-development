# Acknowledgements — the external sources the Drug Repurposing module draws on

Rendered by `python3 framework/scripts/repurposing_adapter.py acknowledgements --write` from the
`INFO` block of every adapter in `framework/adapters/`; never edited by hand. Adding or removing an
adapter re-renders it (the `add` and `remove` commands do so), and `test_repurposing_adapter.py`
fails when the committed file no longer matches the adapters. Every licence and citation below was
read from the source's own licence or terms page on the date given, not from memory.

We are sincerely grateful to the maintainers, curators and funders of these resources. Each of them
makes carefully curated public data available without a key or a fee, and asks in return only for
attribution and a citation; this module honours both, copies their fields verbatim, computes no score
from them, and labels everything it receives **NOT WWOX EVIDENCE** so that their work is never
misrepresented as something it is not. Thank you.

Nothing here is medical advice. Not one of these sources certifies efficacy, safety or suitability.

## chembl

- **What we use:** curated mechanism of action per drug with its reference; ChEMBL targets per gene
- **Access:** GET https://www.ebi.ac.uk/chembl/api/data/{status,molecule/search,mechanism,target/search}.json
- **Licence:** CC BY-SA 3.0; key-less, no payment
- **Licence source:** https://chembl.gitbook.io/chembl-interface-documentation/about (Data Licensing) and https://www.ebi.ac.uk/about/terms-of-use — read on 2026-10-23
- **Terms as read:** 'The ChEMBL data is made available on a Creative Commons Attribution-Share Alike 3.0 Unported License' (share-alike: an adaptation of the data is redistributed under the same licence; this module copies fields verbatim and does not redistribute a derived database). Web services under the EMBL-EBI terms of use: 'EMBL-EBI expects attribution'; no numeric rate limit, use must not prevent service to others. Calculated compound properties come from commercial software and carry their own terms (not consumed here).
- **Citation requested:** Zdrazil B. et al. The ChEMBL Database in 2023: a drug discovery platform spanning multiple bioactivity data types and time periods. Nucleic Acids Res 2024;52(D1):D1180-D1192. https://doi.org/10.1093/nar/gkad1004; web services: Davies M. et al. 2015 (Nucleic Acids Res 43:W612)
- **Attribution line printed with the data:** Data from ChEMBL (EMBL-EBI), CC BY-SA 3.0, https://www.ebi.ac.uk/chembl/

## ilincs

- **What we use:** which LINCS signatures exist for a compound, cell line, dose and time (a census, not a concordance)
- **Access:** GET https://www.ilincs.org/api/SignatureMeta
- **Licence:** LINCS data terms (public); API key-less, no payment
- **Licence source:** https://www.ilincs.org/help/iLINCS-paper — read on 2026-10-23
- **Terms as read:** 'iLINCS is under Creative Commons (CC BY) license.' 'Use of iLINCS is free for everyone.' 'You are free to use the results of iLINCS analysis as you see fit, as long as attribution is given by citing the iLINCS paper below.' No API rate limit stated. Underlying LINCS signatures carry the LINCS consortium's public data terms.
- **Citation requested:** Pilarczyk M., Fazel-Najafabadi M., Kouril M., Shamsaei B. et al. Connecting omics signatures and revealing biological mechanisms with iLINCS. Nat Commun 2022;13:4678. https://doi.org/10.1038/s41467-022-32205-3 (requested 'within any publication that uses any methods or results inspired by iLINCS website or APIs')
- **Attribution line printed with the data:** Signature metadata from iLINCS (CC BY), https://www.ilincs.org

## openfda

- **What we use:** SPL label sections (indications, contraindications, pediatric use, interactions) and FAERS spontaneous-report reaction counts per drug
- **Access:** GET https://api.fda.gov/drug/label.json and /drug/event.json
- **Licence:** US public domain (CC0); key-less, no payment (optional key not used)
- **Licence source:** https://open.fda.gov/terms/ and https://open.fda.gov/apis/authentication/ — read on 2026-10-23
- **Terms as read:** 'made available with a Creative Commons CC0 1.0 Universal dedication'; works where CC0 does not apply 'will be clearly marked'; attribution requested, not required: 'we ask that proper credit be given' with the text 'Data provided by the U.S. Food and Drug Administration'; 'FDA makes no warranty that openFDA data will be error free'; every payload carries 'Do not rely on openFDA to make decisions regarding medical care'. Rate limits without a key: 240 requests per minute and 1,000 per day per IP (with a key 120,000 per day; no key is used).
- **Citation requested:** Data provided by the U.S. Food and Drug Administration (openFDA), https://open.fda.gov — the credit line the terms page asks for
- **Attribution line printed with the data:** Data provided by the U.S. Food and Drug Administration

## opentargets

- **What we use:** target-disease associations by evidence type, tractability buckets, drug and clinical candidates per target
- **Access:** POST https://api.platform.opentargets.org/api/v4/graphql
- **Licence:** data CC0; API key-less, no payment
- **Licence source:** https://platform-docs.opentargets.org/licence — read on 2026-10-23
- **Terms as read:** Data: 'Open Targets Platform is marked with CC0 1.0' (public domain dedication). API and code: Apache License 2.0. No rate limit stated; questions to the Open Targets Community. Individual upstream sources carry their own licences (CC BY 4.0, CC BY-SA 3.0) and 'have agreed to unrestricted use by Open Targets users'.
- **Citation requested:** Buniello A. et al. Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research 2025;53(D1):D1467-D1475. https://doi.org/10.1093/nar/gkae1128 (the page asks: 'If you use our code and/or our data, please cite our latest publication')
- **Attribution line printed with the data:** Data from the Open Targets Platform (CC0 1.0), https://platform.opentargets.org

## orphadata

- **What we use:** ORPHAcodes, preferred terms and ICD/OMIM/MONDO cross-references for rare disorders
- **Access:** GET https://api.orphadata.com/rd-cross-referencing/orphacodes/names/{name}
- **Licence:** CC BY 4.0; key-less, no payment
- **Licence source:** https://www.orphadata.com/legal-notice/ and https://sciences.orphadata.com/ ; the API payload's own __licence field — read on 2026-10-23
- **Terms as read:** The API response declares '__licence: CC-BY-4.0' in every payload (measured 2026-10-22 and 2026-10-23); Orphadata Science: 'All files are available under the Commons Attribution 4.0 International (CC BY 4.0) licence'. The legal notice adds for CC BY 4.0 data: cite the provenance, 'You must indicate if you have made changes to the data', and 'Any use of our data distributed under the CC BY 4.0 licence in LLM/AI-based tools/services' must state that Orphanet/Orphadata data was used; Orphanet is not responsible for outputs built on it. Orphadata Products (bulk services) are under a Data Transfer Agreement and are NOT used here. Logos need prior approval and are not used.
- **Citation requested:** Orphanet: an online rare disease and orphan drug data base. © INSERM 1999. Available on https://www.orpha.net. Accessed (date in retrieved_at). Data via Orphadata, https://www.orphadata.com, data version as in source_version
- **Attribution line printed with the data:** This output uses Orphanet/Orphadata data (© INSERM 1999, CC BY 4.0) in an AI-assisted research tool; the data are copied unchanged and Orphanet is not responsible for this tool's outputs

## pubtator3

- **What we use:** pre-computed gene-chemical-disease-variant relations over PubMed and PMC-OA with publication counts
- **Access:** GET https://www.ncbi.nlm.nih.gov/research/pubtator3-api/relations
- **Licence:** NCBI public domain; key-less, no payment; 3 req/s limit
- **Licence source:** https://www.ncbi.nlm.nih.gov/home/about/policies/ — read on 2026-10-23
- **Terms as read:** NCBI policies: 'Information that is created by or for the US government on this site is within the public domain'; NLM asks for acknowledgment when reused; 'Make no more than 3 requests every 1 second'; large series on weekends or overnight US Eastern; the government 'does not warrant or assume any legal liability or responsibility for the accuracy'. The PubTator3 web pages themselves render no terms text (measured 2026-10-23, three pages); the policy above is NCBI-wide. This adapter sends one request per query and names itself in the User-Agent; no e-mail is sent (none may be recorded here).
- **Citation requested:** Wei C-H. et al. PubTator 3.0: an AI-powered literature resource for unlocking biomedical knowledge. Nucleic Acids Res 2024;52(W1):W540-W546. https://doi.org/10.1093/nar/gkae235
- **Attribution line printed with the data:** Relations from PubTator 3 (NCBI/NLM/NIH), public domain, https://www.ncbi.nlm.nih.gov/research/pubtator3/
