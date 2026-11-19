"""IT59 (2026-11-19), ADV-097 item 3: SCI's unit A (pre-registered premise screen, ADV-095; folder adv095_selection_sci_20261119) carried into six existing open-question rows as dated lines.
Each line splits the in-silico uncertainty that can still change the comparison from the measurement only an experiment supplies. No row is added, no status changes; cards, the investigation
table and the needs file (ranking inputs) are deliberately NOT edited (ADV decision: unit A is pathway-level, no compound was screened; revisit when SCI's compound-level units deliver). Idempotent."""
import csv
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
MARK = "IT 2026-11-19, ADV-097 consumption, on SCI's unit A"
REC = " Record: advisor_pilot_20261113/brainstorm_20261116/adv097_consumption_it_20261119/CONSUMPTION_RECORD_ADV097_IT_20261119.md section 7."
BASE = (" Limits that bind every unit A reading: premise screen on held deposits (organoid 2 v 4 libraries, one parental line, the organoid negative control moved so every organoid shift is 'reference moved'; mouse cortex 3 v 4, one laboratory and cohort family); "
        "labels are readings with uncalibrated thresholds; the blind recompute matched the pivotal numbers; an absent or opposite RNA change is not an exclusion of a lever.")
LINES = {
    "WO-21": (" [" + MARK + ": the GSK-3 premise 'Wnt output lower' is NOT supported in the organoid (Wnt targets higher raw in both knockout clusters, +0.71 and +0.77; adjusted sign depends on the maturity-covariate construction) and is borderline against random sets in the mouse cortex (lower, adjusted -0.71, inside the matched-random band): GSK-3/Wnt is WEAKENED as a broad candidate and carried as sign-divided (consumers: lithium U24, Wnt-lowering U11, cards G01 and D02, INV-09). "
              "IN-SILICO part: nothing more from these deposits (2 to 4 animals per arm; the screen reached its reasoned stop). MEASUREMENT only an experiment supplies: GSK-3 activity at protein level (p-Ser9, beta-catenin; the one held p-Ser9 blot has no activity measure), a second GSK-3 class and the inositol add-back; unchanged, and the question stays whether any part of the lithium effect is genotype-specific." + BASE + REC + "]"),
    "WO-27": (" [" + MARK + ": mature-oligodendrocyte transcripts are LOWER in all four mouse P17 contrasts; in the only labelable one (cortex 3 v 4) stage-adjusted -0.58, outside the matched-random band, sign kept in every leave-one-animal-out fit; about 45 percent of the raw shift is carried by the stage covariate (confounder or maturation delay: not separable here); OPC-lineage set only mildly lower (-0.14 adjusted); registered rule: NEITHER differentiation block nor lineage loss; the organoid does not show it. MOUSE-ONLY, composition-confounded, one laboratory's cohort family: it is NOT a confirmation by the structural myelin endpoints of the AAV9 papers (different model, different level, counts per field in 3 animals). "
              "IN-SILICO part that can still change the comparison (block against delay against loss): SCI's lineage-stage analysis (unit A2) and the delay-equivalent check against the unaffected P14-to-P28 myelin trajectory of ADV-088. MEASUREMENT only an experiment supplies: whether the Wwox-deficient neuron still emits the activity-dependent axonal signal (isogenic control, before any compound); unchanged." + BASE + REC + "]"),
    "WO-04": (" [" + MARK + ": ATF4 target set LOWER in both organoid clusters (raw -0.39 and -0.34; adjusted -0.82 and -0.36), flat in the mouse cortex; the only qualifying reading is the OPPOSITE sign to the premise 'ISR higher'; opposite is not exclusion (an adaptive response may be absent, protein-level activity may differ); the proteome echo detected 3 of 16 ATF4 targets (mean +0.09), too sparse to decide. "
              "IN-SILICO part: none left in the held data. MEASUREMENT only an experiment supplies: the sign of the ISR at protein and translation level, by cell type and stage, before any lever class is chosen; unchanged and now more necessary (the transcript reading points the other way)." + BASE + REC + "]"),
    "IT52-Q01": (" [IT 2026-11-19, ADV-097 consumption, on the catalogue contribution: a NAME lookup in the catalogue returns no record for ISRIB, sephin1, icerguastat or ceapin and does hold the PERK inhibitors GSK2606414 and GSK2656157 (EIF2AK3, action down, direction unresolved, no status statement); the BY-MOLECULE activity query (ChEMBL) was NOT run: the ChEMBL and GtoPdb caches are absent on this machine, so the part of this question about an eIF2B activator found by molecule stays open and executable where the cache exists. No verified pharmacology record is held for any ISR class (ranking unit U12 carries none)." + REC + "]"),
    "WO-07": (" [" + MARK + ": glycolysis and PDK targets ADJUSTMENT_DEPENDENT: higher raw in both organoid clusters (+0.46, +0.52) but not after the maturity adjustment (-0.07, +0.40) and flat in the mouse cortex (-0.06 raw, -0.04 adjusted); no transcript-level premise for a PDH block. "
              "IN-SILICO part: none left in the held data; of the compounds, only dichloroacetate has a verified pharmacological comparison record (U14, CMP-05), AZD7545, thiamine and lipoic acid are catalogue identities only. MEASUREMENT only an experiment supplies: PDH phosphorylation or flux and the genotype-by-inhibitor interaction; unchanged." + BASE + REC + "]"),
    "WO-36": (" [" + MARK + ": NRF2 targets FLAT by the registered label (mouse cortex -0.11 raw and -0.27 adjusted; organoid -0.13 and +0.02 raw, -0.77 and -0.23 adjusted); no transcript-level premise; this is not an exclusion (protein activity and ROS are unmeasured, the held nuclei carry no cytokine-expressing compartment). "
              "IN-SILICO part: none left in the held data. MEASUREMENT only an experiment supplies: NRF2 target activity, ROS and IL-6 and IL-1 beta protein against isogenic corrected cells; unchanged, card L01 stays open." + BASE + REC + "]"),
}
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"
rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t"))
i = rows[0].index("status_evidence"); j = rows[0].index("last_touched")
n = 0
for r in rows[1:]:
    if r[0] in LINES and "on SCI's unit A" not in r[i] and (r[0] != "IT52-Q01" or "catalogue contribution" not in r[i]):
        r[i] += LINES[r[0]]; r[j] = "2026-11-19"; n += 1
with open(p, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("ok", n)
