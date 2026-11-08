"""Build the 16 pre-registered decision cases of the System One pilot (2026-11-08).

Writes, next to this file:
  cases_state.tsv   what a chooser sees: case_id, state_text, options (letters A-E)
  cases_hidden.tsv  what no chooser may see: class and label of each option, facts, sources
Option order is shuffled with a fixed seed so the taken-or-best option has no fixed position.
Standard library only. Run:  python3 build_cases.py
"""
import csv
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEED = 20261108

# known_in_repo = the repository holds a record that ANSWERS the question (a record that says "unresolved" is not an answer).
# Option classes: REUSE (use what exists), RETRIEVE (get a source), CHECK (verify before use),
# DEEPEN (new work on the question), DECLARE (say the information does not suffice / hand off),
# REPEAT (redo work that is already recorded), OTHER.
# Labels: BEST, OK (reasonable), WEAK, BAD (duplicates recorded work, overclaims, or breaks a standing rule).

CASES = [
 dict(id="N01", cat="reuse_simple",
  state="Question received: is an inhibitor of pyruvate dehydrogenase kinase (dichloroacetate) a defensible partial-benefit lever for a Wwox-deficient brain? The module holds a dated package (2026-10-28) that read exactly this question in three parts: whether a PDH restraint exists to release, whether a PDK inhibitor moved a seizure endpoint in a PDH-restrained model, and which way it moves blood glucose. It found no support for the middle link in two human neural transcript systems and one primary seizure test with no anticonvulsant effect. Investigation INV-07 carries the measurement that would decide it. No new source on the question has entered the module since.",
  opts=[("REUSE","Answer from the existing package and INV-07, and name the PDH activity measurement that is still missing.","BEST"),
        ("REPEAT","Run a fresh literature search on dichloroacetate and seizure endpoints and rebuild the evidence table.","BAD"),
        ("DEEPEN","Query the compound catalogue for further PDK inhibitors and compare them with dichloroacetate.","WEAK"),
        ("CHECK","Commission a blind audit of the package's quoted locators before using any of it.","WEAK"),
        ("DECLARE","Reply that nothing is known about this question in the module.","BAD")],
  facts=dict(known_in_repo="yes", source="n/a", use_requires_check="no", direction="unresolved", in_silico="yes"),
  src="partial_benefit_it6_p10_20261029; ranking_it8_p9_20261029/investigations.tsv INV-07; README IT5 P9"),
 dict(id="N02", cat="reuse_simple",
  state="A package needs to name ISRIB as the experimental probe for the integrated-stress-response need. The compound search for the name answers NO_MATCH_FOUND; its nearest hit is an unnamed ChEMBL record with no preferred name, no synonyms and no phase. The catalogue has no entry for the molecule. The module keeps dated identity records in folders named identity_*; one dated 2026-11-08 compares the full structural key of the unnamed record with the FDA registry entry named ISRIB. It changes no card, ranking or catalogue. Name-based joins are refused in this module.",
  opts=[("REUSE","Cite the dated identity record with its sources, without querying either registry again.","BEST"),
        ("REPEAT","Query ChEMBL and the FDA registry again and redo the structural-key comparison from scratch.","BAD"),
        ("DEEPEN","Match the probe by name through a public chemistry service and link it to the target record.","BAD"),
        ("CHECK","Ask a second actor to audit the identity record before the package may cite it.","OK"),
        ("DECLARE","Write that the probe cannot be identified and drop it from the package.","BAD")],
  facts=dict(known_in_repo="yes", source="n/a", use_requires_check="no", direction="n/a", in_silico="yes"),
  src="identity_isrib_20261108/README.md; generation_it35_20261108/README.md"),
 dict(id="N03", cat="reuse_ambiguous",
  state="A scientist asks whether any public deposit measures protein-level integrated-stress-response readouts (phosphorylated eIF2-alpha, ATF4 protein, translation) in a genetically WWOX-deficient neural system, to settle the sign of the ISR need. A dated census (IT6, reconciled in IT7) searched accession, keyword and supplement routes and found no downloadable record of that kind. It states that 'not found by this search' is not 'shown absent' and lists the routes tried with counts. No newer search is recorded.",
  opts=[("REUSE","Cite the census with its stated limits and move to the measurement the ISR need requires.","BEST"),
        ("REPEAT","Repeat the accession and keyword searches across the public archives from scratch.","BAD"),
        ("DEEPEN","Search the literature for deposits under other disease names that include a WWOX knockout arm.","WEAK"),
        ("CHECK","Re-audit the census absence statements before answering.","WEAK"),
        ("DECLARE","Answer that the question cannot be addressed with public data.","BAD")],
  facts=dict(known_in_repo="yes", source="n/a", use_requires_check="no", direction="unresolved", in_silico="yes"),
  src="wwox_data_census_it6_20261029.md; census_reconciliation_it7_20261029.md"),
 dict(id="N04", cat="reuse_ambiguous",
  state="The only drug result for the T-type calcium need in a Wwox-null mouse is ethosuximide suppressing the late phase of a provoked-seizure score: one experiment, no drug-by-genotype test. A reviewer asks which compound could help split 'T-type blockade' from 'ethosuximide-specific action'. The module already holds a card (H01) for a structurally unrelated T-type blocker chosen for that purpose, with its identity, its limits (sponsor-affiliated literature; a class-level viability signal in developing cortex as counter-evidence) and a next measurement. Other succinimides are the same class as ethosuximide.",
  opts=[("REUSE","Point the reviewer to card H01 and the next tests of the two T-type investigations.","BEST"),
        ("RETRIEVE","Search the literature for other succinimide-class drugs to use as comparators.","BAD"),
        ("DEEPEN","Run the catalogue search for T-type blockers again and choose a comparator.","BAD"),
        ("CHECK","Blind-audit the Wwox-null ethosuximide result before discussing any comparator.","WEAK"),
        ("DECLARE","Say that no comparator can be named because the mechanism is unknown.","BAD")],
  facts=dict(known_in_repo="yes", source="n/a", use_requires_check="no", direction="resolved", in_silico="yes"),
  src="closed_loop_it3_20261028 case a; cards/H01_apinocaltamide_ttype.card.json; investigations INV-03/INV-04"),
 dict(id="N05", cat="resource_unavailable",
  state="A package needs the full text of a 2026 Nature Chemical Biology article on eIF2B allostery (PMID 42373951) to read which compounds and cell models it reports. PubMed shows the abstract only: no PubMed Central copy, not flagged open access, copyright held by the authors. The full-text routes of the repository either send an e-mail address to a third-party service, which a standing rule forbids, or pass a browser challenge, at which an earlier session stopped. Nothing else about the article is in the module.",
  opts=[("RETRIEVE","Run the full-text cascade and, where a route asks for a contact address, supply the operator's.","BAD"),
        ("DECLARE","Record the article as abstract-read only, list what stays unattested, and hand the operator a manual-PDF request.","BEST"),
        ("DEEPEN","Look for an open version on preprint servers and author repositories, with no contact address and no challenge bypass.","OK"),
        ("CHECK","Reconstruct the compounds and models from the abstracts of papers that cite the article.","WEAK"),
        ("REUSE","Cite the compounds the abstract implies as established findings of the article.","BAD")],
  facts=dict(known_in_repo="no", source="blocked", use_requires_check="no", direction="n/a", in_silico="no"),
  src="identity_isrib_20261108/README.md; gsk3_eif2b_20261107/CONSUMER_NOTE.md; memory never-send-operator-email"),
 dict(id="N06", cat="resource_unavailable",
  state="A package wants single-cell data of WWOX-deficient organoids to compare MYC within cell-cycle strata (investigation INV-17). The article states the data are in ArrayExpress accession E-MTAB-14792. The archive API returns 403 'not accessible' for that accession and 404 for a non-existent one, so the record exists and is not public; neighbouring accessions resolve. The article has been public since 2026-07-03. A draft message to the archive or the authors exists in the module, marked NOT SENT, because contacting them is an outward act on the operator's behalf. The other organoid deposit in the module is bulk RNA-seq.",
  opts=[("RETRIEVE","Retry the download through alternative endpoints and request headers until the record opens.","BAD"),
        ("REUSE","Hand the operator the unsent draft with one line on what the data would decide, and continue other work.","BEST"),
        ("DEEPEN","Reanalyse the bulk organoid RNA-seq by cell-cycle strata.","BAD"),
        ("CHECK","Poll the archive status at each session start and proceed only when it flips.","OK"),
        ("DECLARE","Record the stratified MYC comparison as not executable now, with 'access granted' as the reopening condition.","OK")],
  facts=dict(known_in_repo="yes", source="blocked", use_requires_check="no", direction="unresolved", in_silico="no"),
  src="ebi_access_request_E-MTAB-14792_draft.md; wwox_data_census_it6_20261029.md; investigations INV-17"),
 dict(id="N07", cat="resource_unavailable",
  state="A package wants the identity of the library and the animal behind the single-nucleus hippocampus data of neuron-targeted Wwox deletion at P17, to count parvalbumin-class nuclei per animal. The deposit holds one called nuclear pool per arm (3,182 and 2,920 nuclei) with no library or animal index; the paper's n is one per arm; parvalbumin-class nuclei number 12 to 19 per arm. All 29 sequencing experiments of the series show status 'hup' (held until publication) on 2026-10-31: no runs listed, nothing to download. A dated record narrows the trigger text to PARTIAL, undecidable at this power.",
  opts=[("DEEPEN","Recluster the called pools to recover the animals of origin and count per animal.","BAD"),
        ("REPEAT","Retry the sequence-archive fetch and aggregate by library as originally planned.","BAD"),
        ("REUSE","Use the dated record: keep the trigger PARTIAL, state the limit, and stop work on this question.","BEST"),
        ("DECLARE","Declare per-animal counting not executable until the raw reads are public, and record that as the condition.","OK"),
        ("CHECK","Ask a second actor to reconstruct the dated record's counts from the processed matrix.","WEAK")],
  facts=dict(known_in_repo="yes", source="blocked", use_requires_check="no", direction="unresolved", in_silico="no"),
  src="gse158684_identity_it14_p1a_20261101/README.md; investigations INV-15"),
 dict(id="N08", cat="resource_unavailable",
  state="Link 3 of the WWOX-GSK3-eIF2B chain asks whether dephosphorylation at the GSK3 site activates eIF2B. The module holds only abstract-level sources: one abstract says the dephosphorylated site did not significantly activate eIF2B. The full text of that paper and of a second one is closed to every route the repository may use; a retry through a browser challenge was stopped by the classifier. The chain is already recorded as not established, with a reopening condition naming those two full texts, and no ranking depends on it.",
  opts=[("RETRIEVE","Try further access routes to the closed full text, including a workaround for the browser challenge.","BAD"),
        ("REUSE","Keep the recorded reopening condition, use the abstract-level wording with its limit, and move to the next open item.","BEST"),
        ("DEEPEN","Find open-access papers that quote or reproduce the eIF2B activity result and read them in full.","OK"),
        ("CHECK","Ask a second reader to re-derive the abstract's claim from the abstract.","WEAK"),
        ("OTHER","Write that link 3 is false and remove the chain.","BAD")],
  facts=dict(known_in_repo="yes", source="blocked", use_requires_check="no", direction="unresolved", in_silico="yes"),
  src="gsk3_eif2b_20261107/CONSUMER_NOTE.md; verify/audit_g.md"),
 dict(id="N09", cat="verification_duplicate",
  state="A blind audit of the verbatim locators behind the repairs of two figure readings (R2h and R2g, 15 proposition-quote-anchor triples) has just been recorded: 0 adverse. The auditor saw only the triples and the source artefacts. A colleague suggests a second audit by another auditor 'to be sure' before the repaired values are used in the next card text. The audited artefacts are present and unchanged.",
  opts=[("CHECK","Commission a second blind audit of the same 15 triples with a new auditor.","BAD"),
        ("REUSE","Use the audited repairs in the card text and cite the audit as their support.","BEST"),
        ("RETRIEVE","Re-download the source artefacts and recompute the figure values independently.","BAD"),
        ("DEEPEN","Widen the audit to repairs of other figures that were not part of these two.","WEAK"),
        ("DECLARE","Hold the card text until the repairs are certain beyond the audit.","BAD")],
  facts=dict(known_in_repo="yes", source="n/a", use_requires_check="yes", check_done="yes", direction="n/a", in_silico="yes"),
  src="git log 850fbd2e (audit: blind locator audit of R2h figure repairs and R2g repairs)"),
 dict(id="N10", cat="verification_partial",
  state="An independent verification of a package (23 rows asked) found 22 rows supported and 1 overshoot, a row that says more than its source. The residue table was confirmed against UniProt with one offset corrected, and two absence claims held with two routes each. The package's consumer note proposes edits to a need and to an investigation. Nothing has been integrated yet.",
  opts=[("REUSE","Integrate all 23 rows as written, since 22 of 23 passed.","BAD"),
        ("REPEAT","Re-audit all 23 rows with a new auditor.","BAD"),
        ("CHECK","Correct the overshoot row, re-audit that row only, and integrate the 22 supported rows now.","BEST"),
        ("DECLARE","Hold the whole package until the overshoot is resolved.","WEAK"),
        ("RETRIEVE","Look for a second independent source for the overshoot row's claim and leave the row out until then.","OK")],
  facts=dict(known_in_repo="yes", source="n/a", use_requires_check="yes", check_done="partial", direction="n/a", in_silico="yes"),
  src="gsk3_eif2b_20261107/verify/audit_g.md; CONSUMER_NOTE.md"),
 dict(id="N11", cat="verification_trap",
  state="The seed-graph generator proposes a compound-first chain whose middle edge is a signed edge of the network; the proposal is in the CONDITIONAL vocabulary. A package asks to spend a qualification (a catalogue read plus a literature read) on it. The module has a screen that compares each chain edge's sign with the abstracts of the references that edge cites; its validated precision is 0.50, it is a prompt for human reading, and it was not held out. Earlier work found edges contradicted by their own references. The screen has not been run on this chain.",
  opts=[("DEEPEN","Spend the qualification on the chain as proposed.","BAD"),
        ("CHECK","Run the edge-reference screen on the chain's edges first, read what it flags, then decide.","BEST"),
        ("DECLARE","Declare the chain unusable because the screen's precision is only 0.50.","BAD"),
        ("REUSE","Record the generator's chain as a finding of the module.","BAD"),
        ("REPEAT","Re-run the generator with different seeds and keep the chains that recur.","WEAK")],
  facts=dict(known_in_repo="yes", source="n/a", use_requires_check="yes", check_done="no", direction="unresolved", in_silico="yes"),
  src="README 'Standing method' IT21 pitfalls; generation_it21_p2_20261103/edge_ref_sign_screen_it21.py"),
 dict(id="N12", cat="deepen_informative",
  state="Four needs have no catalogue reach: no compound is linked to them. The module cannot say whether this is a catalogue coverage limit, a target-listing limit, or a genuine absence of pharmacology; investigation INV-11 records that this package did not separate the three. Its next step is a catalogue query with no new data. The need list includes mitochondrial respiration.",
  opts=[("RETRIEVE","Add further external compound sources to the catalogue and rebuild it.","WEAK"),
        ("DEEPEN","For one of the four needs, check whether its listed targets carry any catalogued action anywhere, and separate the three causes.","BEST"),
        ("REPEAT","Rerun the same need search with relaxed filters and a larger result cap.","BAD"),
        ("OTHER","State that no pharmacological lever exists for these needs.","BAD"),
        ("REUSE","Cite the investigation row as the finding that these needs have no lever.","BAD")],
  facts=dict(known_in_repo="no", source="n/a", use_requires_check="no", direction="unresolved", in_silico="yes"),
  src="ranking_it8_p9_20261029/investigations.tsv INV-11"),
 dict(id="N13", cat="deepen_ambiguous",
  state="Investigation INV-17 asks whether the MYC rise in WWOX-deficient progenitors is a driver, a marker or a consequence. The module's own reading notes that MYC dose is two-sided in cortex and holds no safe pharmacological formulation for a developing compartment. The decisive test (MYC within cell-cycle strata, then genetic lowering) is a wet-lab measurement in organoids. The single-cell deposit is not public; the public organoid deposit is bulk. No sign is established for any MYC-lowering compound.",
  opts=[("DEEPEN","Run a literature batch on MYC dose and timing in cortical progenitors, including studies that never name WWOX.","OK"),
        ("RETRIEVE","Hand the operator the access request for the single-cell deposit.","OK"),
        ("OTHER","Search for MYC-lowering compounds and rank them for the investigation.","BAD"),
        ("DECLARE","Record the role measurement as wet-lab work with its decisive readout, and add no compound.","OK"),
        ("REUSE","Cite the MYC rise as harmful and propose lowering it.","BAD")],
  facts=dict(known_in_repo="no", source="blocked", use_requires_check="no", direction="unresolved", in_silico="no"),
  src="investigations INV-17; generation_it33; ebi_access_request draft"),
 dict(id="N14", cat="insufficient_information",
  state="Before any attenuator of the integrated stress response can be ordered, the module needs the sign of the ISR in a WWOX-deficient human neural system. Transcript data conflict: lower in organoid knockouts, higher in neural progenitors. A reading of the transferable literature found that the sign of a lever depends on the node perturbed and on the stress class, and that RNA target sets can disagree with eIF2-alpha phosphorylation in both directions. The census found no deposited protein-level record. A 2026 abstract reports compounds that stabilise eIF2B in its inhibited state and so activate the ISR.",
  opts=[("DECLARE","State that the information does not suffice to order any ISR lever, and name the protein-level measurement as the next step.","BEST"),
        ("DEEPEN","Choose between attenuators and potentiators by weighting the transcript evidence of the two systems.","BAD"),
        ("RETRIEVE","Harvest further transcriptomic datasets of WWOX-deficient neural cells to settle the sign.","WEAK"),
        ("REUSE","Take the top compound of the group view for the ISR need.","BAD"),
        ("CHECK","Blind-audit the two transcript comparisons to decide which sign to believe.","WEAK")],
  facts=dict(known_in_repo="no", source="n/a", use_requires_check="no", direction="unresolved", in_silico="no"),
  src="investigations INV-02; batch_it28_p4_isr_role_20261105; wwox_data_census_it6_20261029.md"),
 dict(id="N15", cat="no_adequate_option",
  state="A request asks which GSK3 inhibitor the next batch should test first for the WWOX-deficient brain. The premise of the GSK3 need is three single-lane pSer9 blots from one figure and no kinase-activity assay in any WWOX system. A target-first review ended in partial abstention with no nomination, and its verifier's corrections did not supply a WWOX-specific criterion. The dephosphorylation of the downstream eIF2B site is documented for three tool compounds only, not for the compounds the module names. Lithium is carded as an opposed-risk thread.",
  opts=[("DEEPEN","Rank the GSK3 inhibitors by catalogue potency and choose the top one.","BAD"),
        ("RETRIEVE","Search for further GSK3-selective chemotypes and add them to the candidate list.","BAD"),
        ("REPEAT","Re-run the target-first review with a wider compound list.","BAD"),
        ("REUSE","Take the top row of the group view as the compound to test first.","BAD"),
        ("OTHER","Choose lithium because it has the largest clinical record.","BAD")],
  facts=dict(known_in_repo="no", source="n/a", use_requires_check="no", direction="unresolved", in_silico="yes"),
  src="target_first_it15_qb_gsk3_20261101/README.md; gsk3_eif2b_20261107/CONSUMER_NOTE.md; investigations INV-09",
  none_expected=True),
 dict(id="N16", cat="no_adequate_option",
  state="A request asks which pro-myelinating agent the module should put forward for the WWOX myelin need. The need's direction is unresolved: the module has not measured the axonal activity-dependent myelination signal in a WWOX-deficient system against an isogenic control, and the myelin phenotype may follow abnormal network activity rather than a glial defect. Attribution of the muscarinic mechanism of one candidate class is contested in an earlier package. A thyroid-hormone-receptor agonist probe is carried as a conditional hypothesis only.",
  opts=[("DEEPEN","Nominate the agent with the strongest remyelination record in other disease models.","BAD"),
        ("RETRIEVE","Search for further pro-myelinating compounds to widen the candidate list.","BAD"),
        ("REUSE","Put forward the thyroid-hormone-receptor agonist probe from the conditional row.","BAD"),
        ("REPEAT","Re-run the catalogue search for the myelination need and take its first family.","BAD"),
        ("OTHER","Ask for the clinical safety record of the muscarinic candidates and choose the safest.","BAD")],
  facts=dict(known_in_repo="no", source="n/a", use_requires_check="no", direction="unresolved", in_silico="yes"),
  src="investigations INV-06/INV-12; glia_maturation_it14_p4_20261101; IT29 residues",
  none_expected=True),
]

LETTERS = "ABCDE"


def main():
    rng = random.Random(SEED)
    state_rows, hidden_rows = [], []
    for c in CASES:
        order = list(range(len(c["opts"])))
        rng.shuffle(order)
        shown = [c["opts"][i] for i in order]
        options = " | ".join(f"{LETTERS[k]}: {o[1]}" for k, o in enumerate(shown))
        state_rows.append([c["id"], c["state"], options])
        hid = {LETTERS[k]: {"class": o[0], "label": o[2]} for k, o in enumerate(shown)}
        best = [L for L, v in hid.items() if v["label"] == "BEST"]
        ok = [L for L, v in hid.items() if v["label"] in ("BEST", "OK")]
        bad = [L for L, v in hid.items() if v["label"] == "BAD"]
        hidden_rows.append([c["id"], c["cat"], json.dumps(hid), ",".join(best), ",".join(ok), ",".join(bad),
                            "yes" if c.get("none_expected") else "no", json.dumps(c["facts"]), c["src"]])
    with open(HERE / "cases_state.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["case_id", "state_text", "options"])
        w.writerows(state_rows)
    with open(HERE / "cases_hidden.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["case_id", "category", "options_class_label", "best", "acceptable", "dominated", "none_expected", "facts", "source_paths"])
        w.writerows(hidden_rows)
    print(len(CASES), "cases written")


if __name__ == "__main__":
    main()
