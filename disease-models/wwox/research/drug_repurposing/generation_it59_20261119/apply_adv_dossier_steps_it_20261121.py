"""IT 2026-11-21: two dated dossier steps requested by ADV (idempotent; old text kept).
(1) INV-15 / ADV-139: a per-animal association between the cellular-recovery measure and the EEG measure makes the link
    measurable; it does not show that the first effect causes the second, so it is not L3 (needs a mediation-type test).
(2) CIRM funder page, TX-007 monitor: sponsor-reported IND cleared and study start-up initiated; not a registry record.
Run from the repository root:  python3 disease-models/wwox/research/drug_repurposing/generation_it59_20261119/apply_adv_dossier_steps_it_20261121.py"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
WW = DR.parent.parent
sys.path.insert(0, str(HERE))
from apply_adv139_inv15_it_20261121 import edit_rows  # noqa: E402

M1 = "[Update 2026-11-21 (ADV), correction to the L3 clause above:"
INV_ADD = (" " + M1 + " a per-animal association between the cellular-recovery measure and the EEG measure would make the link measurable, "
           "but it would not show that the first effect causes the second, so it does NOT meet L3; L3 ('the cellular recovery explains the EEG effect') needs a "
           "mediation-type test (an intervention on the first step with a test that the second follows), as in the cell-type-specific rescue, silencing or occlusion arms named above. "
           "The resume condition may ask for a per-animal measure with n as an association, and must not read it as L3. "
           "Two readings that move together do not identify a mechanism.]")

README_ADD = ("\n\nSecond line 2026-11-21 (ADV, dated; the text above is kept as written): a per-animal association between the cellular-recovery measure and the EEG measure would make the "
              "discharge-EEG link measurable but would not show that the first effect causes the second; it is not L3, which needs a mediation-type test. See INV-15 in "
              "`ranking_it8_p9_20261029/investigations_it20.tsv`.\n")

CENSUS_ADD = (
    "\n\n## Update 2026-11-21 (ADV monitor of the CIRM award page; IT; the table above is kept as written)\n"
    "CIRM-reported programme update, 2026-11-21: IND reported cleared and study start-up reported initiated (sponsor text on a funder page); NOT a registry record, "
    "NOT an enrolment, NOT an outcome; ClinicalTrials.gov for MZ-9138 = 0, WOREE = natural history only. "
    "The CIRM award page (HTTP 200, read by ADV on 2026-11-21) now says, under Final Operational Milestone #6, that the grant 'enabled Mahzi to successfully submit and clear an "
    "Investigational New Drug Application with the FDA and initiate study start-up activities to support our first in human study'; the product named there is MZ-9138 "
    "(AAV9, hSyn1 promoter, ICM injection; designations stated on the page: Rare Pediatric Disease, Orphan Drug, Fast Track). The scout log of 2026-10-10 had the page without this "
    "sentence, so it was not consumed before. ClinicalTrials.gov, queried 2026-11-21: MZ-9138 returns 0; WOREE returns only NCT01793168, a broad natural-history registry. "
    "The row 'Sponsor-declared authorisation (e.g. an IND cleared)' above therefore reads, as of 2026-11-21, REPORTED by the sponsor on a funder page (not independently confirmed); "
    "the other rows (public regulatory confirmation, registration, enrolment, first dose) are unchanged. The `UNKNOWN` access fields of the cards cite this census as of 2026-10-20 and are not edited. "
    "No ranking changes.\n")

TX_ADD = (
    "\n\n## Update 2026-11-21, third line (ADV CIRM monitor, IT; the text above is kept as written)\n"
    "CIRM-reported programme update, 2026-11-21: IND reported cleared and study start-up reported initiated (sponsor text on a funder page); NOT a registry record, NOT an enrolment, NOT an outcome; "
    "ClinicalTrials.gov for MZ-9138 = 0, WOREE = natural history only (see `../research/drug_repurposing/clinical_census_20261020.md`, same date). "
    "The vector class named for that programme (AAV9, hSyn1 promoter, ICM injection) is the same class as the benchmark (Obeid 2026) and the organoid rescue (AAV9-SynapsinI): "
    "a class-level fact only; no inference on doses is drawn. No ranking changes.\n")


def append_before_trailer(p, add, marker, trailer="**Not medical advice.**"):
    t = p.read_text(encoding="utf-8")
    if marker in t:
        return False
    t = t.rstrip("\n")
    if t.endswith(trailer):
        t = t[: -len(trailer)].rstrip("\n") + "\n" + add + "\n" + trailer + "\n"
    else:
        t += add
    p.write_text(t, encoding="utf-8")
    return True


def main():
    done = edit_rows(DR / "ranking_it8_p9_20261029/investigations_it20.tsv", "inv_id", "INV-15",
                     [("movement_note", lambda s: s if M1 in s else s + INV_ADD)])
    print("INV-15", done)
    p = DR / "nappi_poster_it32_20261107/README.md"
    t = p.read_text(encoding="utf-8")
    if "Second line 2026-11-21 (ADV, dated" not in t:
        p.write_text(t.rstrip("\n") + README_ADD, encoding="utf-8")
        print("README done")
    print("census", append_before_trailer(DR / "clinical_census_20261020.md", CENSUS_ADD, "## Update 2026-11-21 (ADV monitor of the CIRM award page"))
    p = WW / "analysis/tx007_window_and_ceiling_20260921.md"
    t = p.read_text(encoding="utf-8")
    if "third line (ADV CIRM monitor" not in t:
        p.write_text(t.rstrip("\n") + TX_ADD, encoding="utf-8")
        print("tx007 done")


if __name__ == "__main__":
    main()
