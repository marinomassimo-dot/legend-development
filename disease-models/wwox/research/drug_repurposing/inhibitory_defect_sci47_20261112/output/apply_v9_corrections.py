#!/usr/bin/env python3
"""Apply the V9 verifier's substantive corrections to the producer files (idempotent; each rule replaces a string only when it is present)."""
import csv, json, pathlib
H = pathlib.Path(__file__).parent
log = []

def sub(text, old, new, tag):
    if new in text:
        return text
    if old in text:
        log.append(f"{tag}: {text.count(old)} replacement(s)")
        return text.replace(old, new)
    return text

def tsv_edit(name, fn):
    p = H / name
    rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t"))
    hdr = rows[0]
    for r in rows[1:]:
        d = dict(zip(hdr, r))
        fn(d)
        r[:] = [d[h] for h in hdr]
    with open(p, "w", newline="", encoding="utf-8") as f:
        csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)

CL_OLD = "about 2 mM Cl, own arithmetic"
CL_NEW = "about 12 mM Cl (1 mM MgCl2 + 10 mM NaCl), own arithmetic; E_Cl about -63 mV at 35 C with about 129.5 mM external Cl, no junction correction [V9]"

def src(d):
    for k, v in list(d.items()):
        d[k] = sub(v, CL_OLD, CL_NEW, "SR chloride")
    i = d[list(d)[0]]
    if i == "SR29":
        d["value_control"] = sub(d["value_control"], "76.30 +/- 2.26", "76.30 +/- 2.2", "SR29")
    if i == "SR21":
        d["value_control"] = sub(d["value_control"], "median about -50 to -60 pA", "median about -38 to -50 pA (V9 re-read)", "SR21")
        d["value_ko"] = sub(d["value_ko"], "median about -25 to -30 pA", "median about -15 to -24 pA (V9 re-read)", "SR21")
    if i == "SR08":
        d["value_ko"] = sub(d["value_ko"], "frequency -87% (Supp S1: 0.84 to 0.03 bursts/min median)",
            "frequency -87% printed (Fig 3D, normalised); Supp Table S1 medians 0.84 to 0.03 bursts/min = -96% (own arithmetic): two statistics the source does not reconcile [V9]", "SR08")
    if i == "SR10":
        d["n_animals"] = sub(d["n_animals"], "6 text (3 in Supp legend)", "6 text; Supp S3 legend: KO 6 slices from 3 animals, S-WT 7 slices from 4 animals [V9]", "SR10")
    if i == "SR16":
        d["test_and_p"] = sub(d["test_and_p"], "KS: CTL-KO 0.9805;", "KS: first p 0.9805 is unlabelled in the legend (CTL-KO by analogy to f1, inferred);", "SR16")
    if i == "SR18":
        d["dispersion_type"] = sub(d["dispersion_type"], "SD (Results text)", "not labelled in the sIPSC sentence (SD inferred from the preceding sEPSC sentence)", "SR18")
tsv_edit("source_table.tsv", src)

def mat(d):
    i = d["obs_id"]
    if i == "O01":
        d["weakened_explanations"] = sub(d["weakened_explanations"], "E6 (smaller KO cells would be better clamped, not worse; opposite sign of the sEPSC amplitude change); ", "", "O01")
        d["compatible_explanations"] = sub(d["compatible_explanations"], "E3", "E3; E6 (series resistance by genotype is not reported, cut-off 40 Mohm: not weakened) [V9]", "O01") if "E6 (series" not in d["compatible_explanations"] else d["compatible_explanations"]
    if i == "O03":
        d["discriminating_measure"] = sub(d["discriminating_measure"], "K-gluconate-internal sIPSC (outward at -70 mV, small)",
            "K-gluconate-internal sIPSC (pipette about 12 mM Cl, E_Cl about -63 mV by own arithmetic: driving force at -70 mV a few mV, sign undetermined without junction correction) [V9]", "O03")
    if i == "O14":
        d["why"] = sub(d["why"], "No E_GABA exists for any Wwox tissue.", "No E_GABA exists for any Wwox tissue. Omitted conditions of the transferred value (Yuan 2019): recordings at 22-25 C against 35 C here, mean +/- SEM (SD about 12.5 mV), pooled cortex and hippocampus, and in the same cohort P13-17 Scn1b-null neurons at -51.1 mV [V9].", "O14")
    if i == "O16":
        d["why"] = sub(d["why"], "gives no animal-level effect size.", "gives no animal-level effect size. Counts [V9]: sIPSC components 7+7 = 14 cells sum to the pooled 14, animals 4+4 = 8 do not sum to 7; sEPSC components 14+17 = 31 cells against 18 and 5+8 = 13 animals against 10 do not sum.", "O16")
tsv_edit("matrix.tsv", mat)

def ev(d):
    if d["ev_id"] == "E05":
        d["note"] = "sIPSC component animals (4+4 = 8) do not sum to the pooled 7; the cell components (7+7 = 14) do sum; for sEPSC neither cells (14+17 = 31 against 18) nor animals (5+8 = 13 against 10) sum [V9]"
tsv_edit("evidence.tsv", ev)

def lev(d):
    if d["lever_id"] == "L2":
        d["compound_or_probe_sustained_by_a_document"] = sub(d["compound_or_probe_sustained_by_a_document"],
            "ganaxolone against placebo in CDKL5 disorder (30.7% against 6.9% motor seizures, abstract)",
            "ganaxolone (a neuroactive steroid acting on tonic receptors, not a benzodiazepine-site drug) against placebo in CDKL5 disorder (30.7% against 6.9% motor seizures, abstract)", "L2")
        d["compound_or_probe_sustained_by_a_document"] = sub(d["compound_or_probe_sustained_by_a_document"],
            "(placebo -12.1% against -68.3% drop seizures", "(placebo -12.1% against -68.3% drop seizures in the top-dose arm of three", "L2")
    if d["lever_id"] in ("L1", "L5", "L3"):
        if "[V9]" not in d["depth_of_support"]:
          d["depth_of_support"] = d["depth_of_support"] + ("; " if d["depth_of_support"] else "") + "[V9] transfer sources behind this row (vigabatrin case data, P7 RNA table, PV marker count, Kv7/HCN notes, NKCC1 trials) were not re-opened by the verifier: UNVERIFIABLE by V9, reader depth only"
tsv_edit("levers.tsv", lev)

p = H / "design_review.md"
t = p.read_text(encoding="utf-8")
t = sub(t, "A reduction of bursts by a hyperpolarising, GABA-raising or NMDAR-blocking action would appear in any bursting preparation (the d-APV result is exactly that: NMDAR dependence, not NMDAR gain). Burst reduction is therefore not evidence",
        "A burst reduction by an action that acts on many cell types (hyperpolarising, NMDAR-blocking) is not specific evidence of correction (the d-APV result is NMDAR dependence, not NMDAR gain); a GABA-raising action may not reduce bursts at all and may aggravate some seizure types or depolarised-GABA events (L1 and L2 counter-evidence). Burst reduction is therefore not evidence", "design (d) [V9]")
t = sub(t, "a reuptake blocker has no direct membrane-potential effect at rest;", "a reuptake blocker acts on membrane potential only through GABA-A conductance (tonic current), not as a direct hyperpolarisation;", "design (b) [V9]")
t = sub(t, "In each recorded cell: (i)", "Not as one protocol in every cell (high-chloride whole-cell, perforated-patch E_GABA, TTX mIPSC and evoked IPSC with paired-pulse cannot all be run in one cell without compromise [V9]); the minimum that survives is a perforated-patch cohort for native-chloride sIPSC, mIPSC and evoked IPSC plus puffed agonist, and a whole-cell cohort for the high-chloride measures, nested in the same animals. The list: (i)", "design Phase 0 [V9]")
p.write_text(t, encoding="utf-8")

p = H / "answers.md"
t = p.read_text(encoding="utf-8")
if "## V9 corrections" not in t:
    t += """
## V9 corrections (Orchestrator, after the blind verifier; the checks were redone in the paper's Methods and legends)
* **Chloride of the K-gluconate pipette.** The pipette holds 1 mM MgCl2 and 10 mM NaCl (about 12 mM Cl), so E_Cl is about -63 mV (own arithmetic, no junction correction), not about -111 mV; the KCl pipette (about 144 mM Cl) gives E_Cl about 0. Corrected in 27 rows of `source_table.tsv` and in matrix O03.
* **Counts.** sIPSC: cells 7+7 = 14 sum, animals 4+4 = 8 against 7 do not; sEPSC: 14+17 = 31 cells against 18 and 13 animals against 10 do not sum. The statement that the sIPSC cell counts do not sum (O16, E05) is withdrawn.
* **Burst frequency.** The 2.29 bursts/min of the producer's note is a conversion of the Results' median inter-burst interval (26.2 s); Supp Table S1 gives 0.84 bursts/min (71 s); the verifier's read of the Fig 1D histogram supports the supplement. Burst counts differ across the paper (119, 126, 102+41). The two are not the same quantity and the source does not reconcile them.
* **Matrix O01** no longer calls E6 weakened (series resistance by genotype is not reported). **Design review (d)** no longer says the burst reduction appears in any preparation. **L2**: ganaxolone is a neuroactive steroid, not a benzodiazepine-site drug; the clobazam figure is the top-dose arm of three.
* **Inversion table** was incomplete: the viewer, its four translations and 19 rendered pages, the landed IT46 README lines 26-27, `s5_case/result_it46.md` line 30 and `generation_it41_20261109/compound_view.tsv` V21 carry the sentence "by about a fifth ... points at the receptor response or the GABA content of each event". The wording ("by") matches the source; the inference does not. See `consumer_delta.md`.
"""
p.write_text(t, encoding="utf-8")

p = H / "receipts" / "FTR-20261112-34634460-77.json"
r = json.loads(p.read_text())
if r["coverage"].get("supplementary") == "read":
    r["coverage"]["supplementary"] = "captions_only"
    log.append("receipt -77 supplementary -> captions_only")
    p.write_text(json.dumps(r, indent=2) + "\n")
print("\n".join(log) or "nothing to do")
