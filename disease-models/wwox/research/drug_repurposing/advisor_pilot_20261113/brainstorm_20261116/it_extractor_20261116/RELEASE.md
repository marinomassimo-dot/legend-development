# Blind extractor: release record (IT; non-canonical; not medical advice)

Release conditions of Addendum 2a item 11, with the commits that show them (all ancestors of the commit that adds this file):
* SCI informed-arm freeze: f5b71a3f4345b61be7496a328f7cc3b02025c336 (2026-11-16T07:30:22Z).
* Baseline arm (memory-free delegate), IT: 7aa33d25656bd4d4975f5a1faa2894c245586117.
* HE baseline (ii), frequency of use: aa4657b8fba39d942fde8b1cbc33924bf2b0aef8 (folder complete at 8f193ea54e2494b87966d69682b08e43a5687217).
* No other delegate active: the second-read delegate finished before this release.
* Release time: the committer time of the commit that adds this file (UTC, from git log); the extractor is dispatched after that commit.

Extractor: legend-delegate, sonnet, effort high, not SCI and not IT. It receives only the 17-file bundle listed with sha256 in `bundle_manifest.sha256` (11 held full-text files of 11 reports, 2 text supplements, 3 abstracts fetched from Europe PMC by IT with one plain request each, and TASK.md) outside the repository, and the task text `EXTRACTOR_TASK_AS_DISPATCHED.md` (sha256 9a25f27dffc8a02b877450b260656c1dfbcba18381f88720ab626bf4479e23c2). It is not given SCI's frozen files, the baseline arm's output, the matrix, the A1 table or this plan.

Declared, not enforced: the delegate has Bash and inherits the memory index, so 'reads only the bundle' is a declaration. The bundle uses originals where held (PDF text, PMC XML, publisher HTML); PMID 38407561, 41442931 and 30061856 are abstract-only in the bundle (30061856 is a review whose full text is not held), so children in those reports can be extracted at abstract level only. The report PMID 40126049's supplement is included as text; supplementary images were not.
Disclosed exposure of IT: saw the A1 table and the three IT31 agents before this release. IT did not write any extraction row. The output will be sealed by sha256 and committed before scoring.
