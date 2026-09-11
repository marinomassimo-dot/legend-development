#!/usr/bin/env python3
"""Does the DECLARED genre of an article agree with what its own deposit measures?

🔴 WHY THIS EXISTS, AND IT WAS EARNED IN ONE WAVE RATHER THAN IMAGINED.
On 2026-09-09 `scientist-b` read two papers in a single wave and the publication-type
metadata was wrong on BOTH, in OPPOSITE directions:

  PMID 27551470  a 17-reference editorial          PubMed: ['Journal Article']  PMC: editorial
                 -> the metadata is LESS specific than the deposit: UNDER-described.
                    The dispatch that assigned it called it a review, and nothing contradicted that.

  PMID 25238781  a 2-page editor's introduction    PubMed: [... 'Review' ...]   PMC: review-article
                 -> pages 4487-4488, 11 references, no abstract, no figure, received and
                    accepted the SAME DAY: OVER-described.

A repository that weights sources cannot route on `pubtype` alone, and the failure is
invisible: both labels are defensible, neither is flagged anywhere, and a triage that
believed either would have mis-weighted the paper with no error to notice.

WHAT THIS TOOL CLAIMS, AND WHAT IT REFUSES TO CLAIM.
It does NOT determine genre. Nothing here can: genre is an editorial fact about a journal's
intent. It reports DISAGREEMENT between the declared label and cheap discriminators the
deposit itself carries -- page span, reference count, figure count, abstract presence,
section count, and the received/accepted date pair. Disagreement is a reason for a human to
look, never a verdict.

🔴 THE ONE DESIGN RULE, taken straight from this actor's own wave-4 finding: a screen whose
failure mode is a SILENT PASS is worse than no screen, because the caller gets a green result
to point at. So a measurement that could not be made is INSUFFICIENT_DATA, loudly, naming
exactly which discriminator is missing -- never AGREES. `PMID 27551470` is the reason: its
deposit carries fpage 15040 and an EMPTY lpage, so its page span is unobtainable, and the
tool must say so while still catching the disagreement it CAN see.

Usage:
    python3 framework/scripts/genre_discriminator.py --artifact <deposit.xml|.html> \
            [--pubtypes "Journal Article,Review"] [--json]
    python3 framework/scripts/genre_discriminator.py --self-test
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from screen_verdict import ScreenVerdict  # noqa: E402

SCREEN = "genre_discriminator"

# Declared labels that assert a SUBSTANTIAL, refereed, surveying document.
SURVEY_LABELS = {"review", "review-article", "systematic review", "meta-analysis"}
# Declared labels that assert a SHORT, non-primary, usually invited document.
SHORT_FORM_LABELS = {"editorial", "comment", "letter", "news", "correction",
                     "published erratum", "author correction", "expression of concern"}
# A label that asserts nothing about genre at all.
# 🔴 `research-article` BELONGS HERE, AND A CONTROL RUN IS WHY. The first version of this
# module omitted it, so every ordinary primary paper -- PubMed `Journal Article`, deposit
# `research-article` -- came back UNDER_DESCRIBED. Measured on PMID 20530675: a 10-page,
# 36-reference, 5-figure research paper flagged as a metadata defect. The two labels say the
# SAME uninformative thing in two vocabularies, and a screen that fires on the corpus's most
# common case is noise, not a signal. Found by running the tool against papers whose genre
# was never in doubt, which is the check the fixtures could not perform.
UNINFORMATIVE_LABELS = {"journal article", "research support", "english abstract",
                        "research-article", "research article", "article", "brief-report"}

# A document at or below this many pages is not a survey, whatever it is called.
SHORT_PAGE_SPAN = 3
# A survey of a field cites more than this. Chosen loose on purpose: the point is to catch
# the 11-reference case, not to adjudicate a 40-reference one.
SHORT_REFERENCE_COUNT = 25


def _norm(label: str) -> str:
    return re.sub(r"\s+", " ", str(label or "")).strip().lower()


def screen(text: str, pubtypes=None) -> ScreenVerdict:
    """Screen a deposit against its declared labels, naming the bytes it screened.

    🔴 The verdict vocabulary here (AGREES / OVER_DESCRIBED / UNDER_DESCRIBED / DISAGREES /
    INSUFFICIENT_DATA) is the tool's own and is kept: it is the finding. The screen verdict
    sits beside it, because the repository-wide question — *did this screen look at the bytes
    I am asking about?* — is not answerable from a genre word. On 2026-09-09 this tool flagged
    every ordinary primary paper as UNDER_DESCRIBED while its fixtures all passed; a digest
    would not have caught that (only the control run did), but it does make each verdict
    attributable to a specific deposit afterwards, which is how such a run is audited.
    """
    uninformative = ScreenVerdict.reject_uninformative(
        SCREEN, text, expected="the deposit (JATS XML or PMC HTML)")
    if uninformative is not None:
        return uninformative

    result = classify([p for p in (pubtypes or []) if str(p).strip()], measure_deposit(text))
    if result["verdict"] == "INSUFFICIENT_DATA":
        missing = ", ".join(result["unmeasurable"]) or "a declared publication type or a deposit article-type"
        return ScreenVerdict.insufficient(
            SCREEN, missing=missing, data=text,
            detail="; ".join(result["reasons"]), evidence=result)
    if result["verdict"] == "AGREES":
        return ScreenVerdict.clean(
            SCREEN, text,
            detail=("the declared labels and the deposit's own structure do not disagree. "
                    "This never determines genre"),
            evidence=result)
    return ScreenVerdict.refused(
        SCREEN, text, signature=result["verdict"],
        detail="; ".join(result["reasons"]) or result["verdict"], evidence=result)


def measure_deposit(text: str) -> dict:
    """Cheap structural discriminators, from a JATS XML or a PMC HTML deposit.

    Every value is either a number/bool or None, and None means NOT MEASURABLE -- never
    zero. The distinction is the whole point: `figures: 0` says the deposit has no figure,
    `figures: None` says this surface could not tell us, and they must never collapse.
    """
    is_xml = "<article" in text[:4000] and "<front" in text[:8000]
    m = {"surface": "jats_xml" if is_xml else "pmc_html"}

    art = re.search(r'<article[^>]*\barticle-type="([^"]+)"', text)
    m["article_type"] = art.group(1) if art else None

    if is_xml:
        m["references"] = len(re.findall(r"<ref[ >]", text))
        m["figures"] = len(re.findall(r"<fig[ >]", text))
        m["tables"] = len(re.findall(r"<table-wrap[ >]", text))
        m["abstract"] = len(re.findall(r"<abstract[ >]", text)) > 0
        m["sections"] = len(re.findall(r"<sec[ >]", text))
        fp = re.search(r"<fpage[^>]*>(\d+)</fpage>", text)
        lp = re.search(r"<lpage[^>]*>(\d+)</lpage>", text)
        m["fpage"] = int(fp.group(1)) if fp else None
        m["lpage"] = int(lp.group(1)) if lp else None
    else:
        # 🔴 THIS PATTERN IS VERIFIED, NOT GUESSED. PMC serves at least three reference-list
        # markups across deposit vintages (`id="CR1"`, `id="bib1"`, `id="B1"`), and a pattern
        # covering only one returned None on two of three local HTML deposits -- honest, but
        # useless. The broadened form was checked against three reference counts this
        # repository had already established independently, by other readings, on other days:
        # PMID 18674750 -> 48, PMID 21115974 -> 42, PMID 25238781 -> 11. It reproduces all
        # three exactly. Any future broadening gets the same treatment: a count is adopted
        # only when it reproduces a number some other reading arrived at without it.
        m["references"] = len(re.findall(r'<li[^>]*\bid="[A-Za-z_.-]*\d+"', text)) or None
        m["figures"] = len(re.findall(r"<figure[ >]", text))
        m["tables"] = len(re.findall(r"<table[ >]", text))
        m["abstract"] = bool(re.search(r'id="[Aa]bstract|<h2[^>]*>\s*Abstract', text))
        m["sections"] = len(re.findall(r"<section[ >]", text)) or None
        pages = re.search(r"(\d{2,6})\s*[–-]\s*(\d{2,6})\s*\.?\s*doi", text)
        m["fpage"] = int(pages.group(1)) if pages else None
        m["lpage"] = int(pages.group(2)) if pages else None
        if m["lpage"] is not None and m["fpage"] is not None and m["lpage"] < m["fpage"]:
            # "4487–4488" prints in full, but "4487–88" is also published. Repair the
            # elided form rather than reporting a negative span.
            tail = str(m["lpage"])
            head = str(m["fpage"])[: len(str(m["fpage"])) - len(tail)]
            m["lpage"] = int(head + tail) if head else None

    if m["fpage"] is not None and m["lpage"] is not None and m["lpage"] >= m["fpage"]:
        m["page_span"] = m["lpage"] - m["fpage"] + 1
    else:
        m["page_span"] = None

    recv = re.search(r"[Rr]eceived[^0-9A-Za-z]{0,4}(\d{4}\s+\w{3}\s+\d{1,2})", text)
    acc = re.search(r"[Aa]ccepted[^0-9A-Za-z]{0,4}(\d{4}\s+\w{3}\s+\d{1,2})", text)
    if not recv:
        d = re.search(r"<date date-type=\"received\">(.*?)</date>", text, re.S)
        recv = d
    m["received"] = recv.group(1).strip() if recv else None
    m["accepted"] = acc.group(1).strip() if acc else None
    m["same_day_acceptance"] = (
        None if (m["received"] is None or m["accepted"] is None)
        else m["received"] == m["accepted"]
    )
    return m


def classify(pubtypes, measured: dict) -> dict:
    """Compare declared labels against measured discriminators.

    Returns a verdict plus every reason, and an explicit list of what could not be measured.
    """
    declared = [_norm(p) for p in (pubtypes or []) if _norm(p)]
    art = _norm(measured.get("article_type"))

    says_survey = any(d in SURVEY_LABELS for d in declared) or art in SURVEY_LABELS
    says_short = any(d in SHORT_FORM_LABELS for d in declared) or art in SHORT_FORM_LABELS
    declared_informative = [d for d in declared if d not in UNINFORMATIVE_LABELS]

    unmeasurable = [k for k in ("page_span", "references", "figures") if measured.get(k) is None]
    reasons, flags = [], []

    span, refs = measured.get("page_span"), measured.get("references")
    short_evidence = []
    if span is not None and span <= SHORT_PAGE_SPAN:
        short_evidence.append(f"page span {span}")
    if refs is not None and refs <= SHORT_REFERENCE_COUNT:
        short_evidence.append(f"{refs} references")
    if measured.get("abstract") is False:
        short_evidence.append("no abstract")
    if measured.get("figures") == 0:
        short_evidence.append("no figure")
    if measured.get("same_day_acceptance") is True:
        short_evidence.append("received and accepted the same day")
        flags.append("same_day_acceptance")

    verdict = "AGREES"
    # OVER-described: called a survey, measures as a short piece. Require page span or
    # reference count -- "no abstract" alone is far too weak to contradict a Review label.
    strong = (span is not None and span <= SHORT_PAGE_SPAN) or \
             (refs is not None and refs <= SHORT_REFERENCE_COUNT)
    if says_survey and strong and len(short_evidence) >= 2:
        verdict = "OVER_DESCRIBED"
        reasons.append("declared as a survey (" +
                       ", ".join(sorted({d for d in declared if d in SURVEY_LABELS} |
                                        ({art} if art in SURVEY_LABELS else set()))) +
                       ") but measures as a short piece: " + "; ".join(short_evidence))
    # UNDER-described: the declared labels assert no genre while the deposit does.
    elif not declared_informative and art and art not in UNINFORMATIVE_LABELS:
        verdict = "UNDER_DESCRIBED"
        reasons.append(
            f"declared labels {declared or ['(none)']} assert no genre, while the deposit "
            f"itself declares article-type={measured.get('article_type')!r}. The metadata is "
            "less specific than the document.")
    elif says_short and span is not None and span > 8:
        verdict = "OVER_DESCRIBED" if False else "DISAGREES"
        reasons.append(f"declared as short-form but spans {span} pages")

    # 🔴 A missing measurement never yields AGREES. See the module docstring.
    if verdict == "AGREES" and unmeasurable:
        verdict = "INSUFFICIENT_DATA"
        reasons.append(
            "no disagreement was found, but these discriminators could not be measured on "
            "this surface and their absence is NOT evidence of agreement: " +
            ", ".join(unmeasurable))
    if verdict == "AGREES" and not declared and not art:
        verdict = "INSUFFICIENT_DATA"
        reasons.append("neither a declared publication type nor a deposit article-type was given")

    return {"verdict": verdict, "reasons": reasons, "flags": flags,
            "unmeasurable": unmeasurable, "declared": declared,
            "article_type": measured.get("article_type"), "measured": measured}


# --------------------------------------------------------------------------- self-test
# Fixtures are reduced from the two real deposits that produced this tool.
_F_EDITORIAL = (
    '<article article-type="editorial" xml:lang="en"><front><article-meta>'
    "<fpage>15040</fpage><lpage/>"  # the real deposit: an EMPTY lpage, so no page span
    "</article-meta></front><body><sec><title>A</title></sec><sec><title>B</title></sec>"
    "</body><back><ref-list>" + "<ref id=\"b\"><x/></ref>" * 17 + "</ref-list></back>"
    "<floats-group><fig id=\"f1\"><graphic/></fig></floats-group></article>")

_F_SHORT_REVIEW = (
    '<article article-type="review-article"><front><article-meta>'
    "<fpage>4487</fpage><lpage>4488</lpage></article-meta></front>"
    "<body><sec><title>A</title></sec></body>"
    "<back><ref-list>" + "<ref id=\"c\"><x/></ref>" * 11 + "</ref-list></back></article>")

_F_REAL_REVIEW = (
    '<article article-type="review-article"><front><article-meta><abstract><p>x</p></abstract>'
    "<fpage>4519</fpage><lpage>4544</lpage></article-meta></front>"
    "<body>" + "<sec><title>S</title></sec>" * 9 + "</body>"
    "<back><ref-list>" + "<ref id=\"d\"><x/></ref>" * 220 + "</ref-list></back>"
    "<floats-group><fig id=\"f\"/></floats-group></article>")


def _self_test() -> int:
    ok = fail = 0

    def check(name, cond):
        nonlocal ok, fail
        if cond:
            ok += 1
        else:
            fail += 1
            print(f"  FAIL: {name}")

    m = measure_deposit(_F_EDITORIAL)
    check("editorial: article_type read", m["article_type"] == "editorial")
    check("editorial: 17 refs", m["references"] == 17)
    check("editorial: 1 fig counted even though it is in floats-group", m["figures"] == 1)
    check("editorial: EMPTY lpage yields page_span None, not 0", m["page_span"] is None)
    check("editorial: no abstract", m["abstract"] is False)
    r = classify(["Journal Article"], m)
    check("editorial: bare Journal Article over a deposit editorial is UNDER_DESCRIBED",
          r["verdict"] == "UNDER_DESCRIBED")

    m2 = measure_deposit(_F_SHORT_REVIEW)
    check("short review: page span 2", m2["page_span"] == 2)
    check("short review: 11 refs", m2["references"] == 11)
    r2 = classify(["Review", "Journal Article"], m2)
    check("short review: Review over 2 pages and 11 refs is OVER_DESCRIBED",
          r2["verdict"] == "OVER_DESCRIBED")

    m3 = measure_deposit(_F_REAL_REVIEW)
    check("real review: page span 26", m3["page_span"] == 26)
    r3 = classify(["Review", "Journal Article"], m3)
    check("real review: a genuine 26-page 220-reference review AGREES",
          r3["verdict"] == "AGREES")

    # 🔴 THE MUTATION THAT MATTERS: a missing discriminator must never read as agreement.
    m4 = dict(m3)
    m4["page_span"] = None
    m4["references"] = None
    r4 = classify(["Review", "Journal Article"], m4)
    check("unmeasurable discriminators yield INSUFFICIENT_DATA, never AGREES",
          r4["verdict"] == "INSUFFICIENT_DATA")
    check("INSUFFICIENT_DATA names what was missing",
          set(r4["unmeasurable"]) >= {"page_span", "references"})

    # A short-form label over a long document is also a disagreement.
    r5 = classify(["Editorial"], m3)
    check("Editorial over 26 pages DISAGREES", r5["verdict"] == "DISAGREES")

    # Elided page range in HTML ("4487–88") must not produce a negative span.
    m6 = measure_deposit('<html>Cell Mol Life Sci . 2014 Sep 20;71(23):4487-88 . doi: 10.1/x'
                         '<li id="CR1"></li></html>')
    check("elided HTML page range repaired to span 2", m6["page_span"] == 2)

    # 🔴 THE FALSE POSITIVE A CONTROL RUN FOUND: an ordinary primary paper must stay quiet.
    m_primary = {"article_type": "research-article", "page_span": 10, "references": 36,
                 "figures": 5, "tables": 1, "abstract": True, "sections": 20,
                 "same_day_acceptance": None}
    r_primary = classify(["Journal Article"], m_primary)
    check("an ordinary research-article over bare Journal Article is NOT flagged",
          r_primary["verdict"] == "AGREES")

    # ... while a deposit that declares a SPECIFIC genre the metadata omits still is.
    for specific in ("editorial", "comment", "letter", "correction"):
        m_s = dict(m_primary); m_s["article_type"] = specific
        check(f"a deposit {specific!r} under bare Journal Article is still UNDER_DESCRIBED",
              classify(["Journal Article"], m_s)["verdict"] == "UNDER_DESCRIBED")

    # HTML reference markups: all three PMC vintages must count, none may return None.
    for vintage, n in (("CR", 11), ("bib", 48), ("B", 42)):
        frag = "<html>x . doi: 10.1/x" + "".join(
            f'<li id="{vintage}{i}"></li>' for i in range(1, n + 1)) + "</html>"
        check(f"HTML reference vintage id={vintage}N counts {n}",
              measure_deposit(frag)["references"] == n)

    # An empty declaration on both sides is INSUFFICIENT_DATA, not AGREES.
    r7 = classify([], {"article_type": None, "page_span": 10, "references": 40,
                       "figures": 3, "abstract": True})
    check("no declaration at all is INSUFFICIENT_DATA", r7["verdict"] == "INSUFFICIENT_DATA")

    # ---------------------------------------------------------------------------
    # The verdict contract (retrospective 9.2).
    # ---------------------------------------------------------------------------
    v_clean = screen(_F_REAL_REVIEW, ["Review"])
    check("a deposit agreeing with its labels is CLEAN with a digest",
          v_clean.is_clean and (v_clean.digest or "").startswith("sha256:"))
    check("the digest is of the deposit's own bytes",
          v_clean.covers(_F_REAL_REVIEW) and not v_clean.covers(_F_SHORT_REVIEW))
    v_ref = screen(_F_SHORT_REVIEW, ["Review"])
    check("a disagreement is REFUSED and names the genre verdict as its signature",
          v_ref.is_refused and v_ref.signature == v_ref.evidence["verdict"])
    # 🔴 These two assert on WHAT IS NAMED, not merely on the word INSUFFICIENT_DATA, and
    # that distinction was found by mutation: this tool already returns INSUFFICIENT_DATA for
    # an unmeasurable deposit, so removing the input guard entirely left both cases green
    # while the verdict named "page_span, references" as the missing input for a surface that
    # was never there at all. A verdict that names the wrong missing thing sends the reader to
    # re-derive discriminators when the repair is to acquire the deposit.
    v_empty = screen("", ["Review"])
    check("an empty deposit names the DEPOSIT as the missing input, not a discriminator",
          v_empty.is_insufficient and "deposit" in v_empty.missing)
    v_path = screen(__file__, ["Review"])
    check("a path handed where the deposit belongs is refused as a path",
          v_path.is_insufficient and "always passes" in v_path.detail)

    # ---------------------------------------------------------------------------
    # 🔴 THE CONTROL RUN, and it is the reason this block exists.
    #
    # On 2026-09-09 this tool flagged EVERY ordinary primary paper as UNDER_DESCRIBED while
    # all of its fixtures passed. Fixtures are written by the author and agree with the
    # author; only real deposits whose genre was never in doubt exposed it. So the self-test
    # ends by running against the real corpus, with the declared type read out of the tracked
    # corpus seed rather than assumed here — and it says SKIP, loudly, when files/ is absent.
    #
    # What is asserted is what the defect actually was: EVERY primary flagged. It is
    # deliberately not "no primary is ever flagged" — two of the deposits in this checkout are
    # published CORRECTIONS, which are genuinely short against a bare "Journal Article" label,
    # and the coarse primary/review column here is not the paper's real PubMed type. This
    # tool reports a reason to look; an assertion stricter than the evidence would make it
    # report a reason to ignore it.
    # ---------------------------------------------------------------------------
    root = Path(__file__).resolve().parents[2]
    seed = root / "disease-models" / "wwox" / "registries" / "corpus_seed_pubmed_20260705.tsv"
    deposits = sorted((root / "files" / "fulltext").glob("*_PMC*.xml")) + \
        sorted((root / "files" / "fulltext").glob("*_PMC*.html"))
    if not deposits or not seed.is_file():
        print("  [SKIP] real-corpus control run: no deposit under files/fulltext/ (gitignored) "
              "or no corpus seed — this case did NOT run and is not counted as passed")
    else:
        import csv as _csv
        with seed.open(encoding="utf-8") as handle:
            declared_type = {row["pmid"]: row["type"]
                             for row in _csv.DictReader(handle, delimiter="\t")}
        primaries, under, crashed = 0, 0, []
        for deposit in deposits:
            match = re.match(r"PMID(\d+)", deposit.name)
            if not match:
                continue
            kind = declared_type.get(match.group(1))
            pubtypes = ["Journal Article"] + (["Review"] if kind == "review" else [])
            try:
                verdict = screen(deposit.read_text(encoding="utf-8", errors="replace"),
                                 pubtypes)
                assert verdict.screened is not None, "a real deposit was read but not hashed"
            except Exception as exc:
                crashed.append(f"{deposit.name}: {type(exc).__name__}: {exc}")
                continue
            if kind == "primary":
                primaries += 1
                under += verdict.evidence.get("verdict") == "UNDER_DESCRIBED"
        check(f"the corpus-wide control run does not crash ({len(deposits)} deposits)",
              not crashed)
        check(f"not every ordinary primary deposit is UNDER_DESCRIBED "
              f"({under} of {primaries} — 2026-09-09 baseline: all of them)",
              primaries > 0 and under < primaries)

    print(f"self-test: {ok} passed, {fail} failed")
    return 0 if fail == 0 else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--artifact", help="local JATS XML or PMC HTML deposit")
    ap.add_argument("--pubtypes", default="",
                    help="comma-separated declared publication types, e.g. 'Journal Article,Review'")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()

    if a.self_test:
        return _self_test()
    if not a.artifact:
        ap.error("--artifact is required (or use --self-test)")

    path = Path(a.artifact)
    if not path.is_file():
        verdict = ScreenVerdict.insufficient(
            SCREEN, missing=f"artifact {path}", detail="no such file")
        print(verdict.render(), file=sys.stderr)
        return 2
    verdict = screen(path.read_text(encoding="utf-8", errors="replace"),
                     [p for p in a.pubtypes.split(",") if p.strip()])
    result = verdict.evidence or {"verdict": verdict.verdict, "reasons": [verdict.detail],
                                  "flags": [], "declared": [], "article_type": None,
                                  "measured": {}}

    # 🔴 EXIT CODE FOLLOWS THE VERDICT (Mirror REV-EXPOST-20260911-001 F6, task MF-6). Until
    # 2026-09-11 a zero-length artifact produced an INSUFFICIENT_DATA record and exit 0, so a
    # caller reading the status — a shell `&&`, a harness step — read a pass over nothing
    # screened. The record was already honest; the process status was not. Now: 0 only when
    # something was screened, 2 when the verdict is uninformative, matching the other screens.
    status = 2 if verdict.is_insufficient else 0
    if a.json:
        record = verdict.as_dict()
        record["genre_verdict"] = result.get("verdict")
        record["result"] = result
        print(json.dumps(record, indent=1, ensure_ascii=False))
        return status
    print(verdict.render())
    print(f"VERDICT: {result['verdict']}")
    print(f"  declared publication types : {result['declared'] or '(none given)'}")
    print(f"  deposit article-type       : {result['article_type']}")
    md = result["measured"]
    print(f"  measured                   : pages={md.get('page_span')} refs={md.get('references')} "
          f"figs={md.get('figures')} tables={md.get('tables')} abstract={md.get('abstract')} "
          f"sections={md.get('sections')}")
    for r in result["reasons"]:
        print(f"  reason: {r}")
    for f in result["flags"]:
        print(f"  flag: {f}")
    print("  NOTE: this tool reports DISAGREEMENT between a label and the deposit's own "
          "structure. It never determines genre, and a verdict is a reason to look, not a finding.")
    return status


if __name__ == "__main__":
    raise SystemExit(main())
