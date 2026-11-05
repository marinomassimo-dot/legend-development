# Frozen current-method output (IT29 P0), taken before any new material

* Repository SHA: `8c7c46cf47b449716292fe9c5dc6422a0975493a` (IT28 closure).
* Catalogue: `LEGEND_CATALOG_CACHE=…/catalog/cache` (committed manifest at that SHA).
* Command: `python3 framework/scripts/repurposing_search.py need <NEED> [--json]`; the full JSON files are 0.2 to 2 MB and are not kept in git. Their digests and association counts are in `json_digests.txt`; the `.txt` files are the default 30-row listings.
* Current generator stage (IT28 P6, `generation_it28_p6_20261105/results_s9/`), sha256:

| file | sha256 |
|---|---|
| proposals_it21.tsv | cf55b05adce621992ab47daf3606e1f8061350efcc3f280d95cfa1ac1bc41809 |
| handoff_it21.tsv | 7b1814dfaa227e8fa9a26b637398ab1ed5a030143928a539e95cb0c82b70f553 |
| mechanism_clusters_it21.tsv | d000edb4cf4accd817739c5e8dbc641dc1b398463e0056360c14cbe63f47289a |
| carried_prior_decisions.tsv | 4f8494608b1e75e34f16cca7f3bbf2457018af94f10c79b9a3040a7b3fe78a52 |
| summary_it21.json | de621013d2d04043847b62f1f46d0c5e393762a62ffdc0a0901c31fcdedaca2b |

* Universe: the 994-row stage, 220 eligible, 15 hand-overs; selection rule `order_key` as documented in the Standing method.
