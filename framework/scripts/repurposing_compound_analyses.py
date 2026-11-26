"""Render the public compound analysis index from the two published decision registers."""

from html import escape
from pathlib import Path
import re

REPOSITORY = "https://github.com/marinomassimo-dot/legend-development/blob/main/"
DATA_PATH = "disease-models/wwox/research/drug_repurposing/"
LINK = re.compile(r"\[([^\]\n]+)\]\(([^)\s]+)\)")
DOSSIER = re.compile(r"(?:continuous_compounds/)?[a-z0-9_-]+/[a-zA-Z0-9_.-]+\.md")
RUNTIME_LABEL = re.compile(r"\b(?:(?:SCI(?:ENCE)?[ _-]+)?CODEX(?:[ _-]+STRATEGY)?|CLAUDE(?:[ _-]+CODE)?)\b", re.I)
RETAINED_COMPARISON = re.compile(r"\bretain(?:ed)?\s+(?:as|for)\s+[^.!?]{0,65}\b(?:probe|comparator|comparison)\b", re.I)
GROUPS = (
    ("Priority follow-up", "priority"),
    ("Targeted comparison", "comparison"),
    ("Lower-priority follow-up", "lower"),
    ("In progress", "active"),
    ("Not yet ranked", "unranked"),
    ("Deferred", "deferred"),
)


def text(markdown: str) -> str:
    plain = LINK.sub(r"\1", markdown).replace("**", "").replace("`", "")
    return " ".join(RUNTIME_LABEL.sub("", plain).split())


def table(source: str):
    for line in source.splitlines():
        cells = [c.strip() for c in line.strip("|").split("|")]
        if line.startswith("|") and len(cells) == 3:
            yield cells


def read_register(dr: Path, relative: str) -> str:
    path = dr / relative
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def dossier_links(dr: Path, source: str, prefix: str = "") -> dict[str, str]:
    links = {}
    for label, target in LINK.findall(source):
        if not prefix and not target.startswith("../"):
            continue
        path = prefix + target.removeprefix("../")
        if DOSSIER.fullmatch(path) and not RUNTIME_LABEL.search(path) and (dr / path).is_file():
            links[path] = text(label)
    return links


def name_key(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", name.casefold().replace("β", "beta")).strip()


def programme_cards(dr: Path):
    register = read_register(dr, "continuous_compounds/README.md")
    programme, _, checkpoint = register.partition("## Current checkpoint")
    questions = {}
    for order, description, question in table(programme):
        if order.isdecimal():
            name, _, strand = description.partition(", ")
            questions[name_key(name)] = (name, strand, text(question))
    cards = {}
    for line in checkpoint.splitlines():
        summary = re.match(r"\*\*(.+?)\*\*\s*(.*)", line)
        if not summary:
            continue
        label, body = summary.groups()
        links = dossier_links(dr, body, "continuous_compounds/")
        if not links:
            continue
        slug = next(iter(links)).split("/")[1]
        if slug in cards:
            cards[slug]["links"].update(links)
            continue
        name = re.split(r"\s+(?:parked|deferred|retained)\b", label.split(": ", 1)[-1], maxsplit=1, flags=re.I)[0].rstrip(".")
        key = name_key(name)
        question = questions.get(key)
        if question is None:
            question = next((v for k, v in questions.items() if k.startswith(key + " ") or key.startswith(k + " ")), None)
        _, strand, question = question or (name, "", "")
        lead = re.split(r"\s+\[", body, maxsplit=1)[0].replace(" · ", "").rstrip()
        disposition = label + " " + lead
        group = "unranked"
        if label.startswith("Active compound:"):
            group = "active"
        elif RETAINED_COMPARISON.search(disposition):
            # The source may defer a trial and explicitly retain an experiment.
            group = "comparison"
        elif re.search(r"\b(?:parked|deferred)\b", disposition, re.I):
            group = "deferred"
        elif re.search(r"\b(?:high(?:est)? priority|priority follow-up)\b", disposition, re.I):
            group = "priority"
        elif re.search(r"\b(?:retained|prioritize|targeted comparison)\b", disposition, re.I):
            group = "comparison"
        dossier = f"continuous_compounds/{slug}/README.md"
        if (dr / dossier).is_file():
            links = {dossier: "Full dossier", **links}
        cards[slug] = dict(name=name[0].upper() + name[1:], strand=strand, question=question, result=text(lead), group=group, links=links)

    # A newly published README can appear before the next checkpoint update.
    for path in sorted((dr / "continuous_compounds").glob("*/README.md")):
        slug = path.parent.name
        if slug not in cards and re.fullmatch(r"[a-z0-9_-]+", slug):
            name, strand, question = questions.get(name_key(slug), (slug.replace("_", " ").capitalize(), "", ""))
            cards[slug] = dict(name=name, strand=strand, question=question, result="", group="unranked",
                               links={path.relative_to(dr).as_posix(): "Full dossier"})
    return cards


def cycle_cards(dr: Path):
    register = read_register(dr, "cycle_20261123/README.md")
    links = dossier_links(dr, register)
    cards = {}
    for name, result, question in table(register):
        slug = name_key(name).replace(" ", "_")
        sources = {path: label for path, label in links.items() if path.startswith(slug + "_")}
        if not sources:
            continue
        group = "unranked"
        if result.startswith("Highest priority "):
            group = "priority"
        elif result.startswith("Prioritize "):
            group = "comparison"
        elif result.startswith("Lower priority "):
            group = "lower"
        cards[slug] = dict(name=name, strand="Circuit excitability", question=text(LINK.sub("", question)).strip(" ·"),
                           result=text(result), group=group, links=sources)
    return cards


def render_card(slug: str, card: dict, label: str, pdf_reports: set[str]) -> str:
    title = escape(card["name"])
    links = "".join(f'<li><a href="{REPOSITORY}{DATA_PATH}{p}">{escape(t)}</a></li>' for p, t in card["links"].items())
    if slug in pdf_reports:
        links = f'<li><a href="reports/{slug}.pdf">Research report (PDF)</a></li>' + links
    strand = f'<p class="ca-strand">{escape(card["strand"])}</p>' if card["strand"] else ""
    result = f'<p>{escape(card["result"])}</p>' if card["result"] else ""
    question = f'<p class="ca-question"><strong>Research question</strong> {escape(card["question"])}</p>' if card["question"] else ""
    return (f'<article class="ca-card" id="analysis-{slug}"><span class="ca-tag">{label}</span>'
            f'<h4>{title}</h4>{strand}{result}<details><summary>Evidence and follow-up</summary>{question}'
            f'<ul>{links}</ul></details></article>')


def load_cards(dr: Path) -> dict:
    cards = cycle_cards(dr)
    for slug, card in programme_cards(dr).items():
        if slug in cards:
            card["links"] = {**cards[slug]["links"], **card["links"]}
        cards[slug] = card
    return cards


def render(dr: Path, pdf_reports: set[str]) -> str:
    cards = load_cards(dr)
    if not cards:
        return ""

    sections = []
    for label, group in GROUPS:
        rows = sorted(((slug, c) for slug, c in cards.items() if c["group"] == group), key=lambda row: row[1]["name"].casefold())
        if not rows:
            continue
        rendered = "".join(render_card(slug, card, label, pdf_reports) for slug, card in rows)
        heading = f'<h3>{label} <span>{len(rows)}</span></h3>'
        grid = f'<div class="ca-grid">{rendered}</div>'
        if group == "deferred":
            sections.append(f'<details class="ca-section ca-archive" id="ca-{group}"><summary>{label} <span>{len(rows)}</span></summary>{grid}</details>')
        else:
            sections.append(f'<div class="ca-section" id="ca-{group}">{heading}{grid}</div>')
    active = sum(c["group"] == "active" for c in cards.values())
    priority = sum(c["group"] == "priority" for c in cards.values())
    active_link = f'<a href="#ca-active">{active} in progress</a>' if active else ""
    return (f'<section id="compound-analyses" class="compound-analyses" aria-labelledby="ca-title"><header class="ca-hero">'
            f'<h2 id="ca-title">Compound Analyses</h2><p>Follow the evidence behind WWOX drug repurposing.</p>'
            f'<div class="ca-metrics"><span>{len(cards)} compounds</span><span>{priority} priority follow-ups</span>{active_link}</div></header>'
            '<p class="ca-method">Ordered by documented research priority. Compounds within a tier are listed alphabetically. '
            'These priorities describe what to study.</p>'
            '<div class="ca-search" hidden><label for="ca-query">Find a compound</label>'
            '<input id="ca-query" type="search" placeholder="Search by name or pathway"><span role="status"></span></div>'
            + "".join(sections) + "</section>")
