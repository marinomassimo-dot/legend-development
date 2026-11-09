#!/usr/bin/env python3
"""IT40: apply the membrane (A) and AMPA/NMDA (B) consumer proposals to needs, investigations, packets and the open-question map. Idempotent; prints before/after sizes."""
import csv, io, json, sys
from pathlib import Path
R = Path(__file__).resolve().parent.parent
TAG = "[IT40] "
log = []

def need_edit(needs, nid, field, add, obs=None, mode="append_item"):
    n = next(x for x in needs if x["id"] == nid)
    if obs:
        o = next(x for x in n["observed"] if x["id"] == obs)
        if add in o[field]: return
        log.append((nid, f"{obs}.{field}", len(o[field]))); o[field] = o[field].rstrip() + " " + add
    elif isinstance(n[field], list):
        if add in n[field]: return
        log.append((nid, field, len(n[field]))); n[field].append(add)
    else:
        if add in n[field]: return
        log.append((nid, field, len(n[field]))); n[field] = n[field].rstrip() + " " + add

nj = R / "needs/needs.json"; d = json.loads(nj.read_text()); needs = d["needs"]
X = "NEED-INTRINSIC-EXCITABILITY"; G = "NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR"
need_edit(needs, X, "inferred", TAG + "A1 Time constant nearly unchanged (18.55, 18.79, 21.25 ms) while input resistance rises 39 percent: a pure loss of resting K+ conductance at constant capacitance would give a time constant of about 25.8 ms, above both observed mutant values, so Table 1 does not fit a pure leak loss; the implied capacitance (about 180, 131, 149 pF) carries a stated uncertainty of about 14 percent and is not an established difference (the producer's standard-error multiples were not recomputed here). Recorded as an inference from the printed means.")
need_edit(needs, X, "limits", TAG + "A2 Intrinsic properties were recorded with a K-gluconate internal, 3.5 mM external K+ and no liquid-junction correction; pyramidal identity was confirmed from input resistance and time constant (a selection on the measured properties); access resistance up to 40 MOhm was accepted; the Methods pharmacology paragraph lists only TTX, d-APV, carbenoxolone and brilliant blue FCF, so the intrinsic recordings were probably made without a synaptic blocker (inference from the drug list), while 36 of 42 knockout slices burst.", obs="O1")
need_edit(needs, X, "counter_evidence", TAG + "A5 Ivabradine reduces sag (about 2.65 to 1.4 mV at -200 pA, n 6) and hyperpolarises cortical layer 5/6 neurons of normal rats (25-35 days; 3 micromol/L in the text, 30 in the figure legend); in vivo it needed an efflux inhibitor to reach a free brain level of about 184 nmol/L; the oral dose-response bars of its Fig 2 disagree with the text, so no percentage is quotable. 'Removes sag' in the IT39 line above reads 'reduces'. In GAERS thalamic neurons more Ih came with lower input resistance and unchanged rest and sag. A tool response shows that the target contributes in that cell; it does not show a defect of the target in Wwox cells (A6).")
need_edit(needs, G, "inferred", TAG + "B1 AMPAR dependence of the burst is untested in the paper text and supplement (no AMPA/kainate antagonist applied). The knockout mEPSC amplitude shift at -70 mV with a decay of about 5 ms is an inference for an AMPA-type quantum; the pooled-event KS p values are inflated and are not confirmation; AMPA/kainate tools do not separate a kainate contribution.")
need_edit(needs, G, "limits", TAG + "B2 Figure read (Suppl Fig S3B-C, inference, 10-15 percent): d-APV lowered the delayed-response amplitude to about 0.4 of baseline at 100 uA and washout overshot to about 1.3; the amplitude is read at the benchmark latency in every genotype, so wild type reads about 0.115 mV (a floor) and against that floor about 20 percent of the delayed component remains. The residual is not evidence of incomplete block (this corrects the IT38 wording). The text says 'reversibly suppressed'. Abolition applies to the spontaneous bursts only.", obs="O2")
need_edit(needs, G, "limits", TAG + "B3 Disagreements among text, legend, table and figure for the same quantity: baseline 2.29 per minute (text) against 0.84 (Table S1) for the same 119 bursts, 18 slices, 9 animals; carbenoxolone n 36 bursts/4 slices (legend) against 13/6 (Table S1); brilliant blue FCF 73/6 against 25/6; carbenoxolone amplitude 'no change' (text) against a median 0.36 to 0.53 mV (Table S1); Suppl Fig S1 burst counts 126 and 102 + 41 against 119; Fig 4 S-CTL 18 cells against 14 + 17. Fig 3D and Table S1 compare drug groups with one pooled baseline by unpaired tests, so no printed drug percent change is a within-slice effect. A comparison may rest only on direction and non-recovery (carbenoxolone), 'no reduction' (brilliant blue FCF), d-APV abolition of bursts and the incidence 36/42, 4/23, 0/11.", obs="O8")
need_edit(needs, G, "counter_evidence", TAG + "B4 Carbenoxolone 100 uM in autaptic mouse hippocampal culture (room temperature) reduced AMPA EPSC to 63 percent and NMDA EPSC to 69 percent (presynaptic), broadened spikes (+24.5 percent) and lowered input resistance (-20.6 percent); the IPSC reduction (to about 50 percent) was fully reversible. The AMPA-only glutamate-current test ran with NMDAR blocked, so direct NMDAR channel block is neither shown nor excluded. In rat CA1 slices the reversed-uptake ischaemic glutamate current was not significantly changed by carbenoxolone alone (22 percent lower, n 6 against 14, P 0.46, low power); that current is not evoked release, so it neither contradicts the culture result nor excludes an NMDAR block. Brilliant blue FCF blocks mouse Panx1 in oocytes (IC50 0.27 uM) with no Panx1 engagement readout in the slice. The gap-junction half of the carbenoxolone attribution has no supporting datum in the sources read.")
nj.write_text(json.dumps(d, indent=1, ensure_ascii=False))

# investigations (INV-05, INV-18)
ip = R / "ranking_it8_p9_20261029/investigations_it20.tsv"
raw = ip.read_text(); rows = list(csv.reader(io.StringIO(raw), delimiter="\t")); h = rows[0]; ix = {k: i for i, k in enumerate(h)}
def inv_edit(inv, field, add):
    r = next(r for r in rows[1:] if r[0] == inv)
    if add in r[ix[field]]: return
    log.append((inv, field, len(r[ix[field]]))); r[ix[field]] = r[ix[field]].rstrip() + " " + add
inv_edit("INV-18", "decisive_uncertainty", TAG + "A3 Whether the excess sag and rebound persist at matched potential and matched deflection, whether capacitance differs, and whether the recordings were under synaptic blockade; only then whether a blocker-sensitive current differs. A blocker response shows that the current contributes, not that it is defective in Wwox cells.")
inv_edit("INV-18", "next_test", TAG + "A4 Report access resistance, bridge balance and capacitance by genotype; add a Ba2+- or XE991-sensitive difference current with its zero-crossing against E_K (about -97 to -98 mV from the declared solutions; the recorded potentials need a junction correction of about -13 mV that 34634460 did not measure, which puts the estimated sag peaks about 16-21 mV below E_K, so the prediction applies to the voltage-clamp difference current, not to the sag peak).")
inv_edit("INV-18", "evidence_available", TAG + "A7 Tool notes: ZD7288 (20 umol/L in thalamic neurons: about 17 mV hyperpolarisation, sag 0.4-2.1 mV left) is reported to block sodium and T-type current (abstract level for those papers); the Kv7 openers retigabine and SCR2682 were read at abstract level only; K2P and Kir tool papers exist but none is shown to work in layer II/III pyramidal neurons.")
inv_edit("INV-05", "decisive_uncertainty", TAG + "B5 Radiprodil is GluN2B-selective in oocytes (the selectivity sentence rests on an unread supplementary figure) with 45 percent maximum inhibition of GluN2A/GluN2B triheteromers and very slow washout; its use or activity dependence was not tested; its slice precedent is CA1 at P17-P22 with bath magnesium stated as 1.5 mM in the Methods and 0.2 mM in the legends. TCN-201 acts on recombinant GluN2A only, potency set by glycine, maximum inhibition 73-81 percent, so a TCN-201 arm needs a measured slice co-agonist level.")
inv_edit("INV-05", "next_test", TAG + "B6 Report bath magnesium, K+, temperature and blockers actually present as measured values; use a within-slice paired design; add an AMPA/kainate block arm verified by the fast EPSC (abolition alone is not informative, because loss of magnesium relief would abolish an NMDAR-regenerative burst too); add a matched-effect control read on at least two metrics with a receptor-agnostic release-reducing control; add a GABA-A arm because the sIPSC amplitude is halved; state the order of application and washout as part of the design.")
out = io.StringIO(); csv.writer(out, delimiter="\t", lineterminator="\n").writerows(rows); ip.write_text(out.getvalue())

# cards: packets are the inputs
def pk(name, field, add):
    p = R / f"cards/{name}.packet.json"; d = json.loads(p.read_text())
    if add in d[field]: return
    log.append((name, field, len(d[field]))); d[field].append(add); p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n")
pk("F01_glutamate_receptor_node", "not_known", "Whether slice exposure to perampanel is adequate: it is a noncompetitive AMPA/kainate antagonist with no effect on NMDA currents in culture and slow onset and offset (seconds), so exposure must be verified by the evoked response; the potency in the source is submicromolar to about one micromolar (a text-versus-figure conflict was withdrawn as a probable axis misread, inference), while a kinetic dissociation constant in the same paper is several-fold higher and is not reconciled there.")
pk("F04_nmdar_intervention_class", "not_known", "NBQX and GYKI 52466 have no primary mechanism source read in this work: an AMPA arm that uses them is use-only, mechanism not read.")

# open-question map: three new rows (B9-B11)
mp = R / "batch_sci_20261105/map/open_questions_map.tsv"
rows = list(csv.reader(io.StringIO(mp.read_text()), delimiter="\t")); h = rows[0]
have = {r[0] for r in rows}
new = [("IT40-Q01", "Does the burst survive a verified AMPA/kainate block? Abolition alone does not answer it (loss of Mg2+ relief would abolish an NMDAR-regenerative burst too); informative are survival under verified block, or ordering against matched controls on two metrics.", "Decides whether an AMPA-directed arm exists at all and whether the d-APV result is NMDAR-gain, permissive necessity or AMPAR-led drive.", "wet_lab_measurement"),
       ("IT40-Q02", "Does a matched-effect control (graded antagonist plus a receptor-agnostic release-reducing manipulation, two metrics) reproduce the carbenoxolone burst fall in these slices?", "Decides whether the carbenoxolone fall can be read as anything about gap junctions (no datum supports it now).", "wet_lab_measurement"),
       ("IT40-Q03", "Does GABA-A potentiation stop bursts without any change in glutamate receptor currents (alternative AB06)?", "Separates reduced inhibition from receptor gain as the origin of the burst; kainate separation needs a tool whose mechanism paper is read.", "wet_lab_measurement")]
for q, t, dsn, k in new:
    if q in have: continue
    r = [""] * len(h); v = dict(qid=q, source_ref="disease-models/wwox/research/drug_repurposing/ampa_nmda_discrim_20261108/output/consumer_delta.md#B9-B11", question_text_max300=t[:300], decision_at_stake_max200=dsn[:200], kind=k, status="OPEN", published_on="task/it40", status_evidence="ampa_nmda_discrim_20261108/output/prediction_matrix.tsv; IT40 reconciliation", last_touched="2026-11-09", blocking_reason="New measurement in the burst slice preparation; other preparations do not answer it.", executable_zero_spend="no", claimed_by="")
    for k2, x in v.items(): r[h.index(k2)] = x
    rows.append(r); log.append((q, "map row", 0))
out = io.StringIO(); csv.writer(out, delimiter="\t", lineterminator="\n").writerows(rows); mp.write_text(out.getvalue())
for l in log: print(*l)
