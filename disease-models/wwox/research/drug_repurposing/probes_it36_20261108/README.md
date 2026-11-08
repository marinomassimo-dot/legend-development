# Probe supplement (IT36 P4): a tool compound the catalogue does not hold

`output/probe_links.tsv` holds one row, ISRIB, written by the Orchestrator from the audited `probe_entry.tsv` of `nb2_isrib_it36_20261108/` (identity: a ChEMBL record without a name that shares the full InChIKey with the FDA-SRS record named ISRIB). The molecule is **not in the catalogue** (checked 2026-11-08 against the cached catalogue: no record holds CHEMBL4303573), so no raw ChEMBL data was altered and no catalogue row was invented; the row is joined at read time by `repurposing_search.py need <id> --probes packages`.

What the row does: the target is the eIF2B complex, given as a group of its five subunit genes. Under NEED-ISR-ATTENUATION it matches all five intervention targets and is shown **once**, not once per subunit and not as EIF2B5 alone. It is labelled a research probe, is never counted among the headline links, carries no consistency label and no sign.

What it does not do: it asserts no action on the epsilon subunit or on the GSK3 serine, no WWOX result and no benefit. Whether a given ISRIB arm separates a phospho-eIF2 route from a GSK3 route is the discriminating-use grid in `nb2_isrib_it36_20261108/output/README_isrib.md`.
