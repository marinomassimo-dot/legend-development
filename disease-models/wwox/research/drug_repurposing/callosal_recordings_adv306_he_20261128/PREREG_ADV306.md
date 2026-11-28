# PREREG ADV-306: do public callosal or optic-nerve conduction recordings exist that give a slope? (HE, 2026-11-28)

Written before the first search. Assignment: ADV-306 (ADV message of 2026-11-28; key
public-callosal-conduction-recordings-availability-search), under the operator brief
LAB-RESUME-COMPOUND-FOLLOWTHROUGH-20261128. Read-only, plain unauthenticated requests, no login, no contact, no e-mail,
no spend; downloads under 20 MB each, deleted after reading. A 401, 403, 429 or challenge page is recorded as a result.

## What counts

A hit is a deposited dataset or supplement file with compound action potential or latency data from corpus callosum
(slice or in vivo) or optic nerve, in a mouse hypomyelination or dysmyelination line, a Wwox-deficient line (any species),
or a 4-aminopyridine/dalfampridine or clemastine design.

- USABLE-FOR-SLOPE: per-recording values or raw traces, at two or more stated conduction distances (or identified proximal
  and distal components with their distances), with an absolute early-recruitment amplitude and the stimulus stated.
- LATENCY-ONLY: latencies or conduction velocity usable at one distance, or summaries without the proximal-distal pairing
  or without absolute recruitment.
- NOT USABLE: anything else, with the reason.

## Where and with which queries (frozen)

APIs: DataCite (covers Zenodo, Figshare, Dryad, Mendeley Data, OSF, EBRAINS and G-Node DOIs), then the native search of
Zenodo, Figshare, Dryad, DANDI, G-Node GIN, OSF and EBRAINS where it answers without login.
Queries: Q1 "compound action potential" "corpus callosum"; Q2 callosal conduction velocity myelin mouse; Q3 "optic nerve"
"compound action potential" mouse; Q4 hypomyelination electrophysiology conduction; Q5 shiverer conduction; Q6 Wwox
electrophysiology; Q7 4-aminopyridine "compound action potential"; Q8 clemastine conduction. A repository whose search
cannot take a phrase gets the plain words. One further query may be added only after a hit that names a line or a design
not covered, and it is listed as added.
Papers: data-availability statements and held supplements of Repudi 2021 Brain (PMID 33914858), Cheng 2020
(PMID 32000863) and Breton 2021 (PMID 34634460).

## Predictions (ADV's) and rejecting observations

- Zero public Wwox-line datasets with proximal and distal components and absolute recruitment.
- At least one such dataset (USABLE-FOR-SLOPE) in an independent hypomyelination line.
- Rejecting: a public Wwox-line dataset with distances (IT's ADV-304 gets a direct route); zero in any line (the contrast
  stays a structure-to-latency bridge).
- HE's own expectation, stated before searching and not part of ADV's test: the second prediction is likely to fail,
  because CAP studies mostly deposit nothing; at most one USABLE-FOR-SLOPE hit.

## Limits declared before the search

Search by metadata only: a dataset whose title and description never name the tract or the potential is missed; paywalled
supplements are not opened; a zero is "not found by these queries on this date", never "does not exist".
