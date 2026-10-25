# Draft: asking about the release status of E-MTAB-14792 — NOT SENT

**Status: a draft for the operator, written 2026-10-25. Nothing in this file has been sent to anyone.** Contacting EBI curators
or the study's authors is an outward commitment on the operator's behalf, and the choice of sender, tone and whether to ask the
authors rather than the archive is the operator's.

## What is established (each point measured on 2026-10-25, none inferred)
- The accession is **E-MTAB-14792**, named identically in the published article's Data availability statement and in the bioRxiv
  v2 preprint: "The single-cell RNA sequencing data have been uploaded to ArrayExpress with accession number: E-MTAB-14792."
- The article is Steinberg DJ, Zonca A, Abdellatif D, et al., "Disrupted WWOX-MYC interplay impairs neurogenesis in human brain
  organoids", *Brain*, published online 2026-07-03, DOI 10.1093/brain/awag239 (PMID 42397075).
- The BioStudies API distinguishes the cases: a nonexistent accession returns **404 "Study not found"**; **E-MTAB-14792 returns
  403 "Study not accessible"**. So the record **exists** and is **not publicly accessible**. Neighbouring accessions E-MTAB-14791, -14793,
  -14794 and -14795 resolve (200); E-MTAB-14800 returns the same 403.
- The article has been public for nearly four months, so a release held only until publication would already have lapsed.
- **Not established:** whether the study is awaiting a release step, was released only to the submitter, or was suspended. The API uses
  one message for all of them.

## The request (one question, answerable from the archive's own records)
> Subject: Release status of ArrayExpress/BioStudies accession E-MTAB-14792
>
> Dear ArrayExpress / BioStudies team,
>
> The article "Disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids" (Brain, 2026, DOI 10.1093/brain/awag239)
> states in its Data availability section that the single-cell RNA sequencing data were deposited under accession E-MTAB-14792.
> The BioStudies API currently answers "Study not accessible" (HTTP 403) for this accession, while neighbouring accessions resolve.
> Could you tell us whether the study is scheduled for public release, and if so when, or whether anything is needed from the
> submitting authors to complete it? We would like to reuse the processed expression matrix and cell annotation for a comparison of
> Wnt-pathway genes within matched cell populations, and will cite the study and its authors.
>
> With thanks for maintaining the archive,
> [sender]

**If the archive points to the authors:** the same question can go to the corresponding author named on the article, asking
whether the release is pending on their side. That is a scientific courtesy contact and is the operator's to make.

## What is being asked for and what is not
Only the release status, and, once public, the processed count matrix and cell annotation. Not the raw reads, not any controlled-access
material, and nothing that is not already stated in the article as deposited.
