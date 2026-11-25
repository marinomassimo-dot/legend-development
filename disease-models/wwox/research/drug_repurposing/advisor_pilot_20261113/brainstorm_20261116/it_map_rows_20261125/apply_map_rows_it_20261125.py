"""IT 2026-11-25 (ADV decision): rows for the ADV-222 questions NQ-A to NQ-G (NQ-B and NQ-C as CONCLUDED, pointing to ADV-224), the three ADV-228 rows by file path,
and two dated method-precondition lines (IT-C on WO-03, IT-B on NR-03) from ADV-225. Appended or marker-guarded; idempotent. Run from the repository root.
Hypothesis level; no status change of an existing row; no ranking, drug or priority change."""
import csv
from pathlib import Path
DR = Path("disease-models/wwox/research/drug_repurposing")
BS = "advisor_pilot_20261113/brainstorm_20261116/"
MAP = DR / "batch_sci_20261105/map/open_questions_map.tsv"
ADV228 = DR / BS / "adv228_pmc_open_batch_sci_20261124/new_questions_adv228.tsv"
R222 = BS + "adv222_held_data_sections_batch_sci_20261124/RESULT_ADV222_HELD_DATA_SECTIONS_SCI_20261124.md"
R224 = BS + "adv224_isr_codon_sci_20261124/RESULT_ADV224_NQB_NQC_SCI_20261124.md"
DAY = "2026-11-25"
def row(qid, ref, q, d, kind, status, ev, block, zero):
    assert len(q) <= 300 and len(d) <= 200, (qid, len(q), len(d))
    return dict(qid=qid, source_ref=ref, question_text_max300=q, decision_at_stake_max200=d, kind=kind, status=status, published_on="main",
                status_evidence=ev, last_touched=DAY, blocking_reason=block, executable_zero_spend=zero, claimed_by="")
NEW = [
 row("IT-ADV222-NQA", R222 + "#NQ-A", "Does a PV-linked cortical ECoG panel (gamma and theta relative power, theta/gamma, gamma coherence, gamma Granger strength) differ in Wwox-null or hypomorphic mice, and does neonatal gene addition move it, as in CSNK2B haploinsufficiency?",
     "Decides whether the gene-addition and PV-circuit rows (RP-019, RP-040) gain a measurable cortical endpoint panel.", "wet_lab_measurement", "OPEN",
     "[SCI ADV-222, 2026-11-24; added by IT 2026-11-25] Partly held: a Wwox-knockout slice paper reports delta-to-gamma phase-amplitude coupling in bursts, no relative power, no PV, no coherence; the P47T paper contains none of these terms. n at least 6 per arm needed.",
     "No held source answers it fully; needs the five endpoints in Wwox-null and untreated against neonatal-addition pups.", "no"),
 row("IT-ADV222-NQB", R224 + "#1", "Are the nine ISR readout genes of the OMA1 paper's Table 1 (Atf4, Chop, Chac1, Fgf21, Herpud1, Ppp1r15a, Dele1, Hri, Eif2s2) raised, lowered or unchanged in Wwox-deficient neural tissue?",
     "Decides whether the ISR row (RP-018) has any transcript-level direction in held mouse tables.", "literature_executable", "CONCLUDED",
     "[SCI ADV-224, 2026-11-24; added by IT 2026-11-25] Answered from held tables: five genes were already carried (IT6 P4), Herpud1 and Eif2s2 do not move, Fgf21 is not measurable (below 1 TPM), Dele1 is absent from the pinned annotation; no gene reaches LOWER or HIGHER; RP-018 reading unchanged. mRNA only; two to four animals per arm.",
     "", "yes"),
 row("IT-ADV222-NQC", R224 + "#3-nq-c-in-detail", "Do lysine codons pause under lysine limitation as arginine codons do under arginine limitation, per codon?",
     "Decides whether the lysine dossier's per-codon statement has a public ribosome-profiling basis.", "literature_executable", "CONCLUDED",
     "[SCI ADV-224, 2026-11-24; added by IT 2026-11-25] Answered for arginine only: the public deposit (GSE113751) has no lysine condition; the arginine statement reproduces in 1 of 3 cell lines under the frozen rule (HeLa CGT and CGC). For lysine, a source we do not hold: ribosome profiling or charged-tRNA measurement under lysine limitation.",
     "Lysine part needs a source not held; closed as asked of the deposit.", "yes"),
 row("IT-ADV222-NQD", R222 + "#NQ-D", "Does recombinant-WWOX-induced gamma-H2AX persist when cell death is blocked or at a time before viability falls, and does a WWOX-enriched lysate with more WWOX raise it further?",
     "Decides whether the preprint's gain-side gamma-H2AX signal is separable from toxicity (DIS-028).", "wet_lab_measurement", "OPEN",
     "[SCI ADV-222, 2026-11-24; added by IT 2026-11-25] The preprint gives both endpoints at the same doses (coincidence at 100 and 150 ng/mL) but no dissociating arm. Loss arms exist and are small (siWWOX lowers gamma-H2AX about 10 percent, p 0.0044).",
     "Needs a caspase-inhibitor or earlier-time arm; not in the preprint.", "no"),
 row("IT-ADV222-NQE", R222 + "#NQ-E", "What explains the 6.8 against 3.4 pre-treatment metabolite-to-parent ratio between arms of the clobazam and cannabidiol trial (genotype, co-medication, chance with n 10 and 3)?",
     "Decides whether the clobazam mixture-design README can use the first-exposure ratios as stated.", "data_access_blocked", "OPEN",
     "[SCI ADV-222, 2026-11-24; added by IT 2026-11-25] The ratios rest on 10 treated and 3 placebo participants, not 20; CYP2C19 status and enzyme-inducing co-medication by participant are not in the paper.",
     "Participant-level data not in the paper.", "no"),
 row("IT-ADV222-NQF", R222 + "#NQ-F", "Is the cerebral NAD response to a precursor reproducible within a person (augmentation ICC 0.75, CI -0.14 to 0.97, n 5)?",
     "Low portfolio value: tells whether the NAD-precursor comparison (+39.7 against +29.4 percent) carries an age and variance confound.", "data_access_blocked", "OPEN",
     "[SCI ADV-222, 2026-11-24; added by IT 2026-11-25] Groups differ in age (46 against 63.8 years, p 0.01); 82.5 percent of the augmentation variance is between persons; individual data are not public.",
     "Individual data not public; repeated paired measurement would be needed.", "no"),
 row("IT-ADV222-NQG", R222 + "#NQ-G", "Which three patients had conduction worsening on dichloroacetate, and what were their GSTZ1 haplotypes?",
     "Decides whether a dichloroacetate-neuropathy-by-haplotype statement can be made from the long-term paper (RP-033, WO-07 safety side).", "data_access_blocked", "OPEN",
     "[SCI ADV-222, 2026-11-24; added by IT 2026-11-25] Table 1 gives eight patients and haplotypes (two not determined) but no per-patient outcome; the text records conduction worsening in three without linking them to a haplotype.",
     "Patient-level nerve conduction with the haplotype column is not in the paper.", "no"),
]
LINES = {
 "WO-03": (" [IT 2026-11-25 ADV-225 IT-C, method precondition, no status change: before any pharmacological-chaperone screen of WWOX missense proteins, fix the assay format and the amenability criterion in advance; "
           "in 32023956 these two choices alone reclassify 12.9 to 18.0 percent of 178 variants (tables read by IT, ADV-225; ADV re-checked the denominator from the abstract). Result: brainstorm_20261116/it_adv225_20261124/RESULT_ADV225_IT_20261124.md.]"),
 "NR-03": (" [IT 2026-11-25 ADV-225 IT-B, method precondition, no status change: stiripentol acts as a complex I inhibitor in the cell line of 41570991, so a stiripentol readout on ATP, lactate or NADH/NAD+ in one neuronal preparation needs a complex I-independent respiration control and an LDH knock-down arm; "
           "in that paper total ATP rises in one line while the ATP/ADP ratio falls. Result: brainstorm_20261116/it_adv225_20261124/RESULT_ADV225_IT_20261124.md.]"),
}
rows = list(csv.reader(open(MAP, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; ix = {k: i for i, k in enumerate(h)}
have = {r[0] for r in rows}; n = 0
add = list(NEW)
for d in csv.DictReader(open(ADV228, newline="", encoding="utf-8"), delimiter="\t"):
    if d["qid"] not in have:
        d["source_ref"] = DR.as_posix() + "/" + d["source_ref"] if not d["source_ref"].startswith("disease-models") else d["source_ref"]
        add.append(d)
for d in add:
    if d["qid"] in have: continue
    rows.append([d.get(k, "") for k in h]); have.add(d["qid"]); n += 1
for r in rows[1:]:
    q = r[0]
    if q in LINES and LINES[q][:40] not in r[ix["status_evidence"]]:
        r[ix["status_evidence"]] += LINES[q]; r[ix["last_touched"]] = DAY; n += 1
with open(MAP, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("edits", n)
