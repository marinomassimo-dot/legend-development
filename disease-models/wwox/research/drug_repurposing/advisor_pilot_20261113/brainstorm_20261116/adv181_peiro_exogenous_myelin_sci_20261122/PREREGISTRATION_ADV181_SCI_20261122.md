# ADV-181 pre-registration: does Peiro-Moreno et al. 2026 (Glia; PMID 41496652) change how an observed myelin readout would distinguish (a) lineage expansion or survival, (b) debris or substrate uptake, (c) true new sheath formation, beyond INV-06 and SCI50 X1/H4? (SCI successor Z, 2026-11-22; test-design comparison; adjacent non-WWOX primary culture model; no drug promotion, no direction transfer, no WWOX efficacy inference, no assay commission; no contact with authors; no e-mail address to any service; not medical advice)

Fixed BEFORE any body text, figure or supplement of the paper was read.

## What had been seen when this was written
* ADV-181's text: the abstract-level summary (in primary cultures, myelin exposure raises OPC proliferation and lineage progression, with more complexity and a larger myelinated area PER CELL and no change in the OPC-to-mature ratio; in vivo the injected myelin goes mostly into microglia), the identifiers, and the file hashes. Step 0 (reported to ADV): the XML SHA-256 `7fd0519e...ccb8` verified; the PMC open-data bucket route gave the article XML, PDF, eight figure JPEGs (g001 to g008) and a supplement docx, all HTTP 200. From the file names only; nothing of their content.
* The repository, read first: the INV-06 row (its next_test is a neuron-activity-dependent signal, a Wwox-null monoculture or co-culture arm, a conditioned-medium arm, a fixed-neuron arm and a factor arm; readouts are an MBP-positive share and "sheath structure"; it names no separation of new sheath from retained extracellular material or from lineage expansion; I found no text about debris, uptake, lipid droplets or per-cell denominators in the row); the X1 discriminating-observations README (O1: a lower MBP+ share with null medium; "compatible with all three" lists a lower MBP+ share in live co-culture alone); the SCI50 H4-CTGF row (a soluble-versus-contact arm with a positive control); the ADV-123 map header (myelin readout moving with function, no row separates the route to function from myelin; MBP measured as bulk intensity in one Wwox row). I did not open the held neuron/OPC record in full.
* Not seen: anything of the Peiro-Moreno text, methods, figures, supplement or numbers.

## What the paper must establish for any call (units and outputs)
Species and age of cells; the OPC source and the culture type (OPC monoculture, neuron-OPC co-culture, mixed glia); the myelin preparation (source, purification, labelling, dose, exposure time, controls such as heat-inactivated, delipidated or non-myelin lipid particles); the biological unit of each readout (cells, coverslips, wells, independent cultures or animals); and for each output which of these it measures: survival, precursor abundance, mature proportion, newly formed sheath, retained or incorporated pre-existing material, function.

## Readings (fixed)
* **(a) expansion or survival:** more cells (proliferation index, total counts, death) with an unchanged mature fraction; the paper reports an unchanged OPC-to-mature ratio, so a per-cell or per-well "area" rise can follow from more cells without any change per cell.
* **(b) uptake of retained material:** a myelin-derived signal (MBP, PLP, a membrane dye, lipid droplets, or an exogenous-myelin label) inside or on the cell that would be scored as "myelin" or "complexity" without being new synthesis.
* **(c) new sheath:** a per-cell newly formed sheath (an origin-resolved readout: a tag or a synthesis-dependent marker that exogenous material does not carry; a sheath around an axon or a fiber, with a per-cell count and length) or conduction or function.
Rival interpretations are non-exclusive; the call is about which readout in the paper separates them.

## Exits (fixed)
* **KEEP:** a measured readout in the paper is exposed to the (b)-for-(c) or (a)-for-(c) trap in a way INV-06 and X1 do not already guard, and I can name ONE endpoint or control delta that would separate them (with the strongest rival and a refuting observation), with the paper's controls explaining why it is justified.
* **NARROW:** the trap is real but only as a unit or denominator boundary (per-cell against per-well, counts against recovery) or the paper offers only part of the control; then one labelled readout or boundary, not a new arm.
* **CLOSE:** INV-06 and X1 already require a reliable separation; or the primary cannot justify a sharper control; or the readouts cannot be assigned to a unit. Also valid: markers or area change while independent per-cell new sheaths or conduction do not, weakening a functional-rescue reading.

## Checks (fixed)
Whether the exogenous myelin is distinguishable from cell-made myelin in the readouts; whether "myelinated area per cell" has a denominator that includes the added material; whether proliferation and survival were measured in the same cultures; whether any readout is per-cell new sheath or electrophysiology; the in vivo result (microglia uptake) and its denominator; the n and unit; the supplement docx read for controls (headings and captions first); no author contact; the lipid-droplet link to RP-036 is a DREAM candidate only.

## DREAM (fixed)
Do the INV-06 nulls and the count-versus-recovery distinction from ADV-179 (clones recovered against starting lineages) and RP-043 expose the same trap (a numerator that follows how many cells or how much material was recovered)? A weak association is a valid answer.

## Rejecting observation (named in advance)
If the paper's "myelinated area per cell" is computed per cell with a marker that exogenous myelin cannot carry, or the paper already runs a tagged-exogenous-myelin control, or INV-06's separation is already specific, then (b) for (c) is already guarded and the result is CLOSE or NARROW, not KEEP.

## Consumers
ADV (result and path, KEEP/NARROW/CLOSE). IT only if a concrete consumer delta exists.
