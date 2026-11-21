"""IT 2026-11-21: apply the ADV-139 consumer lines (INV-15 reopened at the level the public material supports).

Dated qualifiers, old text kept; idempotent (a marker per edit). Run from the repository root:
    python3 disease-models/wwox/research/drug_repurposing/generation_it59_20261119/apply_adv139_inv15_it_20261121.py
Source: advisor_pilot_20261113/brainstorm_20261116/adv139_nappi_inv15_sci_20261121/RESULT_ADV139_NAPPI_INV15_SCI_20261121.md
Class level, hypothesis level, no dose; no parvalbumin, molecule or target is inferred from either abstract."""
import csv
import sys
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
RES = "advisor_pilot_20261113/brainstorm_20261116/adv139_nappi_inv15_sci_20261121/RESULT_ADV139_NAPPI_INV15_SCI_20261121.md"
MARK = "ADV-139"

QUAL = ("2026-11-21: an inhibitory-neuron-restricted deletion is now reported at abstract level (AES 2026, 1.019, public 17 Nov 2026): "
        "class only, no Cre line, no subtype, no recombination check, no age, no n; not a parvalbumin result; "
        "unverifiable until a manuscript, poster or slides state them.")

Q_PREFIX = ("2026-11-21: a public conference abstract (AES 2026, 1.019; same programme as SfN NANO11.01) reports, at class level only, that Wwox deletion in "
            "inhibitory neurons was sufficient to produce spontaneous seizures and premature mortality (no Cre line, subtype, recombination check, age or n stated; "
            "reported, unverifiable; not a parvalbumin result), and that a pharmacological treatment improved neuronal firing ex vivo and reduced seizure burden in vivo "
            "(no treated model, cell, comparator, EEG measure, n or molecule; L1 and L2 unanchored, L3 not met). Before the six layers below: which inhibitory class "
            "(parvalbumin or another) carries the effect, and how was it identified? Then: ")

PV_OLD = "and names parvalbumin interneurons as the population of interest; it reports no quantitative result"
PV_NEW = ("and, in a background sentence only, states that parvalbumin-expressing interneurons regulate network excitability and synchronisation "
          "(it names no population of interest and no PV change; see nappi_poster_it32_20261107/README.md); it reports no quantitative result")

EV_ADD = (" [Update 2026-11-21, ADV-139 (" + RES + "): two newer public abstracts of the same programme (SfN Neuroscience 2026 NANO11.01 and AES 2026 1.019, public 17 Nov 2026) "
          "supply result statements, not per-animal data: " + QUAL + " The treatment statements (reduced seizure burden in vivo; partly restored or improved firing) are L1-unanchored and L2-unanchored; L3 (recovery explains the EEG effect) is not met; "
          "neither abstract names parvalbumin, so the PV question does not move and the RP-019 trigger is not met.]")

NOV_ADD = (" [Update 2026-11-21, ADV-139: AES 2026 1.019 and SfN NANO11.01 were read at abstract level (" + RES + "); a result statement exists at class level, not per-animal data; "
           "no PV is named. A search of this module and of the routes listed there, not a statement about the literature.]")

MV_OLD = ("names parvalbumin interneurons and slice and in vivo recordings as approaches and supplies no result, so the position is unchanged; per-animal data from that programme would reopen it.")
MV_NEW = ("states, as background, that parvalbumin-expressing interneurons regulate network excitability and describes its approaches (genetic mouse models, in vivo electrophysiology, ex vivo slice recordings) and supplies no result, "
          "so the position was unchanged; per-animal data from that programme would reopen it.")
MV_ADD = (" [Update 2026-11-21, ADV-139: rank STAYS 6 (INV-15 gates PV-directed levers and the order of the inhibitory contrasts; no PV is named, so that decision is untouched); what changes is the first layer of the question. "
          "RESUME CONDITION: any one document that states, for the treated preparation, the identified cell type and how (Cre, reporter or marker), the model and age, the comparison against untreated mutant and wild type with n cells and n animals, "
          "the per-animal EEG measure and a vehicle comparator; for the inhibitory-sufficiency statement to be verified, also the Cre line, the recombination check and the age of deletion. "
          "Documents in order of likelihood: the AES 2026 poster 1.019 (5 Dec 2026, Denver) or its virtual poster gallery (attendees, up to 90 days); the SfN NANO11.01 slides or recording; "
          "a manuscript or preprint by the programme on Wwox in inhibitory neurons. RE-CHECK dates: 2026-12-06, 2026-12-21, 2027-03-06. L2 becomes anchored by a named subtype with restoration compared against untreated mutant and wild type; "
          "L3 only by a cell-type-specific rescue, silencing or occlusion arm, or a per-animal association with n.]")


def read_tsv(p):
    with open(p, encoding="utf-8", newline="") as fh:
        text = fh.read()
    return text


def edit_rows(path, key_col, key, edits):
    """edits: list of (column, function old->new). Rewrites only the keyed row, preserving the rest byte for byte."""
    text = read_tsv(path)
    lines = text.split("\n")
    head = lines[0].split("\t")
    done = []
    for n, ln in enumerate(lines):
        f = ln.split("\t")
        if n and len(f) == len(head) and f[head.index(key_col)] == key:
            for col, fn in edits:
                i = head.index(col)
                new = fn(f[i])
                if new != f[i]:
                    f[i] = new
                    done.append(col)
            lines[n] = "\t".join(f)
            break
    else:
        sys.exit(f"row {key} not found in {path}")
    Path(path).write_text("\n".join(lines), encoding="utf-8")
    return done


def add_once(add):
    return lambda s: s if MARK in s else s + add


def replace_once(old, new):
    def fn(s):
        if old in s:
            return s.replace(old, new)
        return s
    return fn


def inv15():
    p = DR / "ranking_it8_p9_20261029/investigations_it20.tsv"
    return edit_rows(p, "inv_id", "INV-15", [
        ("question", lambda s: s if s.startswith("2026-11-21: a public conference abstract (AES") else Q_PREFIX + s),
        ("evidence_available", lambda s: add_once(EV_ADD)(replace_once(PV_OLD, PV_NEW)(s))),
        ("novelty_perimeter", add_once(NOV_ADD)),
        ("movement_note", lambda s: add_once(MV_ADD)(replace_once(MV_OLD, MV_NEW)(s))),
    ])


def c08():
    p = DR / "openscientist_retest_20261108/inv15_pv/chains.tsv"
    return edit_rows(p, "chain_id", "C08", [
        ("observation", add_once(" [Update 2026-11-21, ADV-139: the absolute \"no interneuron-restricted model exists\" is now contradicted at class level by a public abstract; " + QUAL + " See " + RES + ".]")),
        ("relation_hypothesised", add_once(" [Update 2026-11-21, ADV-139: for the inhibitory class as a whole, cell autonomy is reported at abstract level and unverifiable; for parvalbumin cells and for the lineage it stays unresolved.]")),
    ])


def m24():
    p = DR / "measurement_reconciliation_adv006_20261114/output/measurements.tsv"
    return edit_rows(p, "m_id", "M24", [
        ("indispensable_or_substitutable", add_once(" [Update 2026-11-21, ADV-139: the interneuron-class arm is now reported at abstract level without a reporter (" + QUAL + "); the pyramidal-specific arm is reported in neither abstract; the pre- versus postsynaptic question stays open. See " + RES + ".]")),
    ])


def m24_scope():
    """Column not_decided_by_it of M24 is the one the design-step generator maps into the scope cell of design row 31
    (generation_it40_20261109/conditional_design_steps_it50.tsv); that table is GENERATED (run conditional_proposals.py
    there after this script) and must never be edited by hand: test_design_rows_he50 compares it with the generator."""
    p = DR / "measurement_reconciliation_adv006_20261114/output/measurements.tsv"
    return edit_rows(p, "m_id", "M24", [
        ("not_decided_by_it", add_once(" [Update 2026-11-21, ADV-139: the interneuron-class arm is now reported at abstract level without a reporter (AES 2026 1.019; class only, no Cre line, subtype, recombination check, age or n; not a PV result; unverifiable); the pyramidal-specific arm is reported in neither abstract; the pre- versus postsynaptic question stays open.]")),
    ])


def readme():
    p = DR / "nappi_poster_it32_20261107/README.md"
    t = p.read_text(encoding="utf-8")
    if MARK in t:
        return []
    t = t.rstrip("\n") + (
        "\n\n## Update 2026-11-21 (ADV-139, dated pointer; the text above is kept as written)\n"
        "Two newer public abstracts of the same programme exist (SfN Neuroscience 2026 NANO11.01 and AES 2026 1.019, public 17 Nov 2026): the result-statement half of the reopening condition is met at class level, "
        "the per-animal half is not, and neither names parvalbumin. See `../" + RES + "` and INV-15 in `ranking_it8_p9_20261029/investigations_it20.tsv` (rank stays 6; resume condition and re-check dates are there).\n")
    p.write_text(t, encoding="utf-8")
    return ["README"]


if __name__ == "__main__":
    for fn in (inv15, c08, m24, m24_scope, readme):
        print(fn.__name__, fn())
