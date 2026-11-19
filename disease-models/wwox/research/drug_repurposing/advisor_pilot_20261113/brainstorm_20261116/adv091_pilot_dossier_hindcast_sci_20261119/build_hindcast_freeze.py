#!/usr/bin/env python3
"""Build the ADV-091 hindcast freeze files from the pair table below.

What it does: checks that every source sentence of every pair is a verbatim substring of
the abstract copy held outside git (files/hindcast_abstracts_adv091/abs_<pmid>.json, copied
from Europe PMC by plain GET on 2026-11-19), assigns disguised ids by a seeded shuffle, and
writes two files next to this script: the KEY (identities, sentences, labels; never shown to a
scorer) and the SCORER SHEET (disguised ids, class-level descriptors, date-cut, components,
rubric, analysis plan; no outcome). It writes nothing else and scores nothing.

usage: build_hindcast_freeze.py [--abstracts DIR] [--check]
  --abstracts DIR  folder holding the abs_<pmid>.json copies (default: files/hindcast_abstracts_adv091
                   under the repository root, found by walking up from this script)
  --check          verify the quotes only; write no file

Hypothesis level. A diagnostic of a scoring method on known outcomes, not a licence for any
use of any agent in any person. Not medical advice.
"""
import argparse
import hashlib
import json
import os
import random
import sys

SEED = 20261119
HERE = os.path.dirname(os.path.abspath(__file__))

# label: POS or NEG by the outcome rule in the SCORER SHEET section 2 (rule fixed before scoring).
# cut: last year of literature the scorer may use (source year minus 2, see section 3 of the sheet).
PAIRS = [
    dict(key="stiripentol_dravet", pmid="11089822", year=2000, label="POS", design="randomised placebo-controlled add-on trial, 41 children",
         identity="stiripentol add-on in severe myoclonic epilepsy of infancy (Dravet syndrome; by syndrome, the gene is not named in this source)",
         desc="A GABA-A positive allosteric modulator that also inhibits cytochrome P450 (raising co-administered clobazam and valproate), as add-on, in an infant-onset epileptic encephalopathy attributed to sodium-channel haploinsufficiency; children; endpoint: clonic or tonic-clonic seizure frequency.",
         quote="15 (71%) patients were responders on stiripentol (including nine free of clonic or tonic-clonic seizures), whereas there was only one (5%) on placebo (none were seizure free; stiripentol 95% CI 52.1-90.7 vs placebo 0-14.6)."),
    dict(key="everolimus_tsc", pmid="27613521", year=2016, label="POS", design="randomised placebo-controlled phase 3 (EXIST-3), 366 patients",
         identity="everolimus add-on in tuberous sclerosis complex, focal-onset seizures",
         desc="An inhibitor of the nutrient-sensing kinase complex mTORC1, as add-on, in a disorder of constitutive overactivation of that complex (loss of a two-protein repressor); ages 2 to 65 years; endpoint: seizure response rate and frequency.",
         quote="The response rate was 15·1% with placebo (95% CI 9·2-22·8; 18 patients) compared with 28·2% for low-exposure everolimus (95% CI 20·3-37·3; 33 patients; p=0·0077) and 40·0% for high-exposure everolimus (95% CI 31·5-49·0; 52 patients; p<0·0001)."),
    dict(key="ganaxolone_cdkl5", pmid="35429480", year=2022, label="POS", design="randomised placebo-controlled phase 3 (Marigold), 101 patients",
         identity="ganaxolone add-on in CDKL5 deficiency disorder",
         desc="A neuroactive-steroid GABA-A positive allosteric modulator, as add-on, in an X-linked developmental and epileptic encephalopathy from loss of a brain-expressed kinase; ages 2 to 21 years; endpoint: major motor seizure frequency.",
         quote="There was a median percentage change in 28-day major motor seizure frequency of -30·7% (IQR -49·5 to -1·9) in the ganaxolone group and of -6·9% (-24·1 to 39·7) in the placebo group (p=0·0036)."),
    dict(key="ketogenic_glut1", pmid="16217704", year=2005, label="POS", design="prospective follow-up cohort, 15 children",
         identity="ketogenic diet in GLUT1 deficiency syndrome",
         desc="A high-fat, low-carbohydrate diet supplying ketones as an alternative brain fuel, in a disorder of impaired glucose transport into the brain (heterozygous loss of function of the transporter); children, 2 to 5 years of follow-up; endpoint: seizure freedom.",
         quote="10/15 patients remained seizure-free on the ketogenic diet in monotherapy."),
    dict(key="pyridoxine_aldh7a1", pmid="27882480", year=2017, label="POS", design="retrospective series, 11 patients (the disease is defined by pyridoxine response: circular by construction)",
         identity="pyridoxine in pyridoxine-dependent epilepsy due to ALDH7A1 deficiency",
         desc="A cofactor vitamin that is inactivated by an accumulating lysine-degradation metabolite, in an inborn error of lysine degradation (loss of an aldehyde dehydrogenase) presenting with neonatal seizures; endpoint: seizure freedom on the vitamin.",
         quote="73% of the patients became seizure free on pyridoxine."),
    dict(key="nachannel_blockers_kcnq2", pmid="42610455", year=2026, label="POS", design="retrospective multicentre cohort, 282 individuals; no proportion in the abstract",
         identity="sodium-channel blockers (carbamazepine, oxcarbazepine) in KCNQ2 loss-of-function disorders",
         desc="Use-dependent sodium-channel blockers in neonatal-onset epilepsies from loss of function of a voltage-gated potassium channel (Kv7 family) that restrains neuronal firing; neonates and infants; endpoint: seizure control and offset.",
         quote="SCBs, especially carbamazepine (CBZ) and oxcarbazepine (OXC), emerged as the most effective ASMs in both LOF groups."),
    dict(key="lamotrigine_sme", pmid="9596203", year=1998, label="NEG", design="open case series, 21 patients",
         identity="lamotrigine in severe myoclonic epilepsy of infancy (Dravet syndrome; by syndrome, the gene is not named in this source)",
         desc="A use-dependent sodium-channel blocker, mostly as add-on, in an infant-onset epileptic encephalopathy attributed to sodium-channel haploinsufficiency; children 2 to 18 years; endpoint: change in each seizure type.",
         quote="LTG induced worsening in 17 (80%) patients, no change in three, and improvement in one."),
    dict(key="bumetanide_neonatal_hie", pmid="25765333", year=2015, label="NEG", design="open-label phase 1/2 dose-finding trial, 14 infants",
         identity="bumetanide add-on to phenobarbital for seizures in neonatal hypoxic-ischaemic encephalopathy (not a genetic class)",
         desc="A loop diuretic that blocks the chloride importer NKCC1 (to lower intraneuronal chloride and restore GABA inhibition), as add-on to a barbiturate, in full-term newborns with electrographic seizures after perinatal asphyxia; endpoint: reduction of electrographic seizure burden.",
         quote="The trial was stopped early because of serious adverse reactions and limited evidence for seizure reduction."),
    dict(key="nachannel_blockers_scn2a_late", pmid="28379373", year=2017, label="NEG", design="retrospective review of 66 patients with SCN2A variants (late-onset, truncating group)",
         identity="sodium-channel blockers in SCN2A-related epilepsies with onset from 3 months (loss-of-function class)",
         desc="Use-dependent sodium-channel blockers in epilepsies from variants of a brain sodium-channel gene whose variants in this subgroup are truncating or loss-of-function; onset from 3 months of age; endpoint: seizure reduction or freedom.",
         quote="In contrast, sodium channel blockers were rarely effective in epilepsies with later onset (≥3 months) and sometimes induced seizure worsening."),
    dict(key="soticlestat_dravet", pmid="41784472", year=2026, label="NEG", design="randomised placebo-controlled phase 3 (SKYLINE), 144 participants; primary endpoint not met (p = .061); borderline",
         identity="soticlestat add-on in Dravet syndrome",
         desc="An inhibitor of the brain cholesterol-24-hydroxylase (lowering a glutamatergic-receptor-potentiating oxysterol), as add-on, in an infant-onset epileptic encephalopathy attributed to sodium-channel haploinsufficiency; ages 2 to 21 years; endpoint: monthly convulsive seizure frequency.",
         quote="Median change from baseline in convulsive seizure frequency over the full treatment period was -8.64% with placebo (n\u2009=\u200971) and -22.16% with soticlestat (n\u2009=\u200973), a difference of -15.64% (p\u2009=\u2009.061)"),
    dict(key="triheptanoin_glut1", pmid="35441706", year=2022, label="NEG", design="randomised placebo-controlled trial, 36 patients",
         identity="triheptanoin in GLUT1 deficiency syndrome, drug-resistant seizures, not on a ketogenic diet",
         desc="A medium-odd-chain triglyceride that supplies an anaplerotic brain fuel, in a disorder of impaired glucose transport into the brain; patients over 1 year old not on a ketogenic diet; endpoint: overall seizure frequency.",
         quote="A median 12.6% reduction in overall seizure frequency was observed in the triheptanoin arm relative to baseline, and a 13.5% difference was observed relative to placebo (p\xa0=\xa0.58)."),
    dict(key="quinidine_kcnt1", pmid="35940594", year=2022, label="NEG", design="systematic review of 82 patient records from 27 studies (case-level literature)",
         identity="quinidine in KCNT1-related epilepsies",
         desc="A potassium-channel blocker with sodium-channel activity, in epilepsies from gain-of-function variants of a sodium-activated potassium channel; infants and children; endpoint: at least 50 percent seizure reduction.",
         quote="Records of 80 patients with 33 KCNT1 mutations were analysed, of which 20 patients had gained ≥50% seizure reduction due to quinidine therapy."),
]

# Read and verified in the same window but NOT in the primary 12 (balance rule, sheet section 1).
RESERVE = [
    dict(key="fenfluramine_dravet", pmid="31862249", year=2019, label="POS", design="randomised placebo-controlled trial, 119 patients",
         identity="fenfluramine add-on in Dravet syndrome (same disease as stiripentol: skipped by the one-positive-per-disease rule)",
         quote="In Dravet syndrome, fenfluramine provided significantly greater reduction in convulsive seizure frequency compared with placebo and was generally well tolerated, with no observed valvular heart disease or pulmonary arterial hypertension."),
    dict(key="cannabidiol_dravet", pmid="28538134", year=2017, label="POS", design="randomised placebo-controlled trial, 120 patients",
         identity="cannabidiol add-on in Dravet syndrome (same disease as stiripentol: skipped by the one-positive-per-disease rule)",
         quote="The median frequency of convulsive seizures per month decreased from 12.4 to 5.9 with cannabidiol, as compared with a decrease from 14.9 to 14.1 with placebo (adjusted median difference between the cannabidiol group and the placebo group in change in seizure frequency, -22.8 percentage points; 95% confidence interval [CI], -41.1 to -5.4; P=0.01)."),
    dict(key="nachannel_blockers_scn2a_early", pmid="28379373", year=2017, label="POS", design="retrospective review of 66 patients with SCN2A variants (early-onset, gain-of-function group)",
         identity="sodium-channel blockers in SCN2A-related early infantile epilepsies (the other half of the SCN2A source: same paper as an included negative, so left out of the primary set)",
         quote="We find that the use of sodium channel blockers was often associated with clinically relevant seizure reduction or seizure freedom in children with early infantile epilepsies (<3 months), whereas other antiepileptic drugs were less effective."),
    dict(key="phenytoin_scn8a", pmid="26252990", year=2016, label="POS", design="case series, 4 patients",
         identity="phenytoin in SCN8A-related epilepsy with a missense variant (a second sodium-channel-blocker positive: reserve)",
         quote="Herein, we describe 4 patients with a missense SCN8A mutation and epilepsy who all show a remarkably good response on high doses of phenytoin and loss of seizure control when phenytoin medication was reduced, while side effects were relatively mild."),
]


def default_abstract_dir():
    d = HERE
    for _ in range(12):
        cand = os.path.join(d, "files", "hindcast_abstracts_adv091")
        if os.path.isdir(cand):
            return cand
        d = os.path.dirname(d)
    return os.path.join(HERE, "abstracts_missing")


def check(pairs, adir):
    bad = 0
    for p in pairs:
        path = os.path.join(adir, "abs_%s.json" % p["pmid"])
        try:
            ab = json.load(open(path, encoding="utf-8"))["abstract"]
        except OSError:
            print("MISSING copy:", path)
            bad += 1
            continue
        ok = p["quote"] in ab
        p["abstract_sha256"] = hashlib.sha256(open(path, "rb").read()).hexdigest()
        print(("OK   " if ok else "FAIL ") + p["key"] + " " + p["pmid"])
        bad += 0 if ok else 1
    return bad


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--abstracts", default=None)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    adir = a.abstracts or default_abstract_dir()
    allp = PAIRS + RESERVE
    bad = check(allp, adir)
    if bad:
        print("quotes not verified:", bad)
        return 1
    if a.check:
        return 0
    order = list(range(len(PAIRS)))
    random.Random(SEED).shuffle(order)
    ids = {}
    for rank, idx in enumerate(order, 1):
        ids[PAIRS[idx]["key"]] = "HC-%02d" % rank
    for p in PAIRS:
        p["hid"] = ids[p["key"]]
    rows = sorted(PAIRS, key=lambda p: p["hid"])
    # KEY
    k = ["# Hindcast freeze, KEY file (never shown to a scorer): identities, source sentences, labels (SCI, ADV-091, 2026-11-19)", "",
         "Hypothesis level. A diagnostic of a scoring method on known outcomes, not a licence for any use of any agent in any person. Not medical advice. No individual-level information is used or recorded.", "",
         "Seeded shuffle for the disguised ids: random.Random(" + str(SEED) + ") over the table order of build_hindcast_freeze.py. Source of each sentence: the abstract text of the paper, copied from Europe PMC by plain GET on 2026-11-19 (copy held outside git; digests below; full texts NOT read). Each sentence was checked by the script as a verbatim substring of its copy.", "",
         "## Primary set (12 pairs: 6 POS, 6 NEG)", "",
         "| id | label | pair | design | PMID | year | date-cut | abstract copy sha256 |", "|---|---|---|---|---|---|---|---|"]
    for p in rows:
        k.append("| %s | %s | %s | %s | %s | %d | %d | `%s` |" % (p["hid"], p["label"], p["identity"], p["design"], p["pmid"], p["year"], p["year"] - 2, p["abstract_sha256"]))
    k += ["", "## Source sentence per pair (verbatim; the sentence that fixed the label)", ""]
    for p in rows:
        k.append("* **%s** (%s, %s): \"%s\"" % (p["hid"], p["key"], p["label"], p["quote"]))
    k += ["", "## Read and not in the primary set (reserve; not scored unless the sheet's section 1 says so)", ""]
    for p in RESERVE:
        k.append("* **%s** (%s, %s; %s; PMID %s, %d): \"%s\"" % (p["key"], p["label"], p["identity"], p["design"], p["pmid"], p["year"], p["quote"]))
    k += ["", "## Dropped from the original list of 13 (ADV-091 addendum: number dropped stated)", "",
          "**1 dropped:** trofinetide on seizures in Rett syndrome. No source sentence stating a seizure outcome for the drug was found by one Europe PMC title search of 2026-11-19 (the hits were a case report, a computational paper and economic or safety papers), and the pivotal trial's endpoints are not seizure frequency, so the pair fails the one-endpoint-class rule as well as the reading rule. Absence of a source here is one route only. **Substituted, not dropped:** the original pair 'sodium-channel blockers in SCN1A' was read as lamotrigine in severe myoclonic epilepsy of infancy (the source names the drug and the syndrome, not the gene). **Added after reading (not on the original list):** soticlestat in Dravet syndrome, triheptanoin in GLUT1 deficiency, quinidine in KCNT1, to give the negatives a count equal to the positives.", ""]
    open(os.path.join(HERE, "HINDCAST_FREEZE_KEY_ADV091_SCI_20261119.md"), "w", encoding="utf-8").write("\n".join(k) + "\n")
    # SCORER SHEET
    s = open(os.path.join(HERE, "scorer_sheet_template.md"), encoding="utf-8").read()
    table = ["| id | class-level descriptor (no names, no outcome) | date-cut |", "|---|---|---|"]
    for p in rows:
        table.append("| %s | %s | %d |" % (p["hid"], p["desc"], p["year"] - 2))
    s = s.replace("@@PAIR_TABLE@@", "\n".join(table))
    open(os.path.join(HERE, "HINDCAST_FREEZE_SCORER_SHEET_ADV091_SCI_20261119.md"), "w", encoding="utf-8").write(s)
    print("wrote KEY and SCORER SHEET;", len(rows), "pairs;", sum(1 for p in rows if p["label"] == "POS"), "POS,", sum(1 for p in rows if p["label"] == "NEG"), "NEG")
    return 0


if __name__ == "__main__":
    sys.exit(main())
