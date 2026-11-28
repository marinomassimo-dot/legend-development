# ADV-308 result: does the etifoxine burst-versus-spike split appear in a second dataset? (SCI, window 64fc909a, 2026-11-28)

Hypothesis level; reference genotype class only; not medical advice. Rule frozen first: `PREREG_ADV308_SCI_20261128.md` (sha256 f2743f60770ed1bdf1c5205f43589474f06524aa5a448d86a92f72fbee4524d0; what had been seen before freezing is disclosed there). Sources: public full texts through Europe PMC (no contact, no spend, no address sent to any service).

## Label
**NOT TESTABLE FROM HELD SOURCES.** No second dataset in the preparation class frozen in the PREREG (primary neuronal network under a convulsant, a burst endpoint, a GABA-A modulator arm and a selective TSPO ligand arm, vehicle or convulsant alone) was found. This is a result about the held and open literature on 2026-11-28, not a negative on the split. My prediction ("it does not replicate outside the culture panel") is neither confirmed nor refuted: it was untestable.

## Dated search (2026-11-28, NCBI E-utilities via the repository's PubMed helper; counts are hits)
| Query (abridged) | Hits | Outcome |
|---|---|---|
| (TSPO OR translocator protein OR XBD173 OR emapunil OR PK11195 OR etifoxine) AND (multielectrode array OR MEA OR local field potential OR network bursts OR burst) | 17 | only 40561753 itself fits; the rest are imaging, microglia, mitochondria, depression, cattle |
| (XBD173 OR emapunil OR etifoxine) AND (hyperexcitab* OR epileptiform OR seizure OR 4-aminopyridine) | 9 | 40561753; seven whole-animal convulsion papers on etifoxine (1985 to 2014), no network recording |
| (XBD173 OR emapunil OR TSPO ligand* OR PK11195 OR etifoxine) AND (neuronal/cortical culture, primary neurons, hippocampal slice, organotypic) AND (burst* OR epileptiform OR network activity OR spontaneous activity) | 1 | 42589596 (read; see below) |
| etifoxine AND (slice OR culture OR patch-clamp) AND (burst* OR epileptiform OR network) | 1 | 26913957 (amygdala, pain; abstract only; whole-animal behaviour plus patch-clamp, no network burst) |
| Banerji Patel Baraban gluconeogenesis zebrafish Dravet PK11195 | 1 | 33842883, read (below) |
Held full texts naming XBD173, emapunil or PK11195 (keyword sweep of `files/fulltext/`, 4 files): one Kv7 paper with a single PK11195 mention (PMID 32248813), an infantile-spasm review (no TSPO ligand arm), and two Israeli society abstract books (TSPO and cell death, binding in Alzheimer brain): none is a network recording with a modulator arm.

## The two papers read, and why neither counts
1. **Banerji 2021 (PMID 33842883, the earlier Scn1Lab paper from the same group, reference 22 of 40561753).** 6-dpf Scn1Lab larvae, tectal LFP, 10-min epochs: 3 h of 10 microM PK11195 lowers the frequency of ictal-like and inter-ictal-like events, ictal duration unchanged; stiripentol is used only as a positive control in the swim-behaviour screens and has no LFP arm; no XBD173, no etifoxine, no burst counter (the Axion burst detector appears only in the 2025 paper). Whole larva, not a network preparation with a modulator arm, and no burst endpoint: **does not count** (PREREG: larval datasets excluded). It adds one point: the same group had already seen event-frequency suppression by PK11195 in larvae, which is the spike-side pattern of 40561753, not the burst side.
2. **Bieletzki et al. 2026 (PMID 42589596, PMC13466293, open access).** Wild-type mouse neocortical slice cultures, spontaneous up-states (no convulsant), multi-unit recordings; high-frequency activity (HFA) is the first 50 ms of each up-state, low-frequency activity (LFA) is 75 to 1200 ms. Arms: midazolam 100 nM, allopregnanolone 50 nM, XBD173 3 microM (exposure 30 min instead of 12 min "to allow endogenous neurosteroidogenesis"). Values are drug against sham, as printed in Tables A3 and A4 (normalised activity; my ratio of drug to sham in brackets, recomputed):

| arm | HFA drug / sham (ratio), n, p | LFA drug / sham (ratio), n, p |
|---|---|---|
| midazolam 100 nM | 0.89 / 1.01 (0.88), 32/31, p = .036 | 0.88 / 1.11 (0.79), 37/34, p = .043 |
| allopregnanolone 50 nM | 1.00 / 1.05 (0.95), 19/20, p = .47 | 0.31 / 1.20 (0.26), 24/20, p < .0001 |
| XBD173 3 microM | 0.87 / 0.86 (1.01), 72/71, p = .52 | 0.58 / 0.95 (0.61), 76/78, p < .0001 |
n is slices or recordings as printed (the paper does not give animals here); P values are the authors' uncorrected tests. **Does not count** because there is no convulsant, no burst count (HFA is a time window inside an up-state, not a burst number), no etifoxine or non-steroidogenic TSPO arm (PK11195), and the benzodiazepine is midazolam at a sedative concentration, not etifoxine.

## Adjacent observation (listed apart, not a replication)
In slices the TSPO agonist XBD173 behaves as the neurosteroid does (sustained firing down, onset firing untouched), and the benzodiazepine alone trims onset firing (about 12 per cent, p = .036 uncorrected). That is the same direction as the 2025 culture panel, in which XBD173 lowered spikes and rate more than bursts and the GABA-A modulators lowered bursts. It is compatible with E-A, but (a) the endpoints differ, (b) the midazolam effect is small and uncorrected, and (c) no steroid-synthesis block was applied in either paper, so the steroidogenic reading of XBD173 is the authors' assumption in both. In the slices a 30-minute XBD173 exposure was enough to see an allopregnanolone-like effect on sustained firing, which weakens the "timing masks the steroidogenic route" explanation (E-B) for the sustained-firing endpoint, but does not test it for bursts.

## Counterexample sought
None found: no dataset has a selective TSPO ligand suppressing bursts, and none has etifoxine suppressing bursts together with every TSPO ligand.

## What it changes
* **Etifoxine role (conditional probe): unchanged.** The split rests on one culture panel (n per arm not stated) and stays a one-panel observation.
* **XBD173 comparator entry (INV-10):** keep XBD173 as the TSPO-selective comparator; note that its published network effect in two preparations (cultures: spikes and rate; slices: sustained firing) is on the sustained-firing side, and carry the slice dataset (3 microM, 30 min) as the second preparation for the steroid-like profile.
* **Registered missing observation:** one preparation, one convulsant, one burst counter with fixed detector settings, with arms etifoxine (or another GABA-A modulator such as ganaxolone), XBD173 and PK11195, preincubation 1 h and 3 h, and a neurosteroid-synthesis block (finasteride) or TSPO knockdown on the XBD173 and etifoxine arms. Nothing in the held or open literature on 2026-11-28 supplies it.
* **Rotation:** this was the second INV-10 etifoxine increment; the strand rotates.

## Not done
No receipt (no complete read; the two papers were read for the stated question only, from the XML text; figures of 42589596 and Fig 6 of 33842883 were not opened, the tables are quoted from the XML). No delegate used. The abstract-only paper 26913957 and the 4 held files were not read beyond the keyword context.
