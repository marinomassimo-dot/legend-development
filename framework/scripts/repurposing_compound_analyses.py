"""Render the public compound analysis index from the published decision registers."""

from html import escape
from pathlib import Path
import re

REPOSITORY = "https://github.com/marinomassimo-dot/legend-development/blob/main/"
DATA_PATH = "disease-models/wwox/research/drug_repurposing/"
LINK = re.compile(r"\[([^\]\n]+)\]\(([^)\s]+)\)")
DOSSIER = re.compile(r"(?:continuous_compounds/)?[a-z0-9_-]+/[a-zA-Z0-9_.-]+\.md")
RUNTIME_LABEL = re.compile(r"\b(?:(?:SCI(?:ENCE)?[ _-]+)?CODEX(?:[ _-]+STRATEGY)?|CLAUDE(?:[ _-]+CODE)?)\b", re.I)
# A kept research role: "retain as a ... probe", or a clause that begins with Retain or Keep, or "stays a ... comparator". A clause start excludes a result sentence such as "8/10 slices retained a response".
RETAINED_COMPARISON = re.compile(r"\bretain(?:ed)?\s+(?:as|for)\s+[^.!?]{0,65}\b(?:probe|comparator|comparison)\b"
                                 r"|(?:^|[.!?]\s+|\band\s+|;\s+)(?:retain|keep)\b|\bstays\s+an?\s+[^.!?]{0,40}\b(?:probe|comparator|comparison)\b", re.I)
# The checkpoint writes the base form too ("Park for pediatric WWOX trial priority").
PARKED_OR_DEFERRED = re.compile(r"\b(?:park(?:ed|ing)?|defer(?:red|ring)?)\b", re.I)
GROUPS = (
    ("Priority follow-up", "priority"),
    ("Targeted comparison", "comparison"),
    ("Lower-priority follow-up", "lower"),
    ("In progress", "active"),
    ("Assessment available", "unranked"),
    ("Follow-up deferred", "deferred"),
    ("Analysis pending", "pending"),
)


def text(markdown: str) -> str:
    plain = LINK.sub(r"\1", markdown).replace("**", "").replace("`", "")
    return " ".join(RUNTIME_LABEL.sub("", plain).split())


def table(source: str, columns: int = 3):
    for line in source.splitlines():
        cells = [c.strip() for c in line.strip("|").split("|")]
        if line.startswith("|") and len(cells) == columns:
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
        elif PARKED_OR_DEFERRED.search(disposition):
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
    report_slug = slug if slug in pdf_reports else slug.replace("_", "-")
    pdf = f'<a href="reports/{report_slug}.pdf">Research report (PDF)</a>' if report_slug in pdf_reports else ""
    strand = f'<p class="ca-strand">{escape(card["strand"])}</p>' if card["strand"] else ""
    role = card.get("role")
    rationale, *reopen = re.split(r"(?<=[.!?])\s+(?=Reopen\s+(?:for|when|if)\s+)", card["result"], maxsplit=1, flags=re.I)
    next_step = card.get("next_step")
    if not next_step and reopen:
        next_step = re.split(r"(?<=[.!?])\s+(?=[A-Z])", reopen[0], maxsplit=1)[0]
    fields = [("Why it matters" if card.get("why") else "What the analysis found", card.get("why") or rationale),
              ("What is still uncertain", card.get("limit")),
              ("What would move it forward", next_step or card["question"])]
    facts = "".join(f'<div><dt>{heading}</dt><dd>{escape(value)}</dd></div>' for heading, value in fields if value)
    pinned = f'<a class="ca-permalink" href="#analysis-{slug}" aria-label="Link to {title} analysis">Link to this analysis</a>'
    investigation = card.get("investigation")
    thread = f'<a href="#{investigation}">Related investigation</a>' if investigation else ""
    summary = card["result"] if card.get("why") or reopen else ""
    details = f'<p>{escape(summary)}</p>' if summary else ""
    if next_step and card["question"] and card["question"] != next_step:
        details += f'<p><strong>Research question</strong> {escape(card["question"])}</p>'
    if links:
        details += f'<ul>{links}</ul>'
    more = f'<details><summary>Evidence and scientific detail</summary>{details}</details>' if details else ""
    return (f'<article class="ca-card" id="analysis-{slug}"><span class="ca-tag">{label}</span>'
            f'<h4>{title}</h4>{strand}' + (f'<p class="ca-role">{escape(role)}</p>' if role else "")
            + (f'<dl class="ca-facts">{facts}</dl>' if facts else "")
            + f'<div class="ca-links">{pinned}{pdf}{thread}</div>{more}</article>')


def comparison_cards(dr: Path):
    """Summarise specific research uses from the existing public compound register."""
    _, _, source = read_register(dr, "continuous_compounds/README.md").partition("\n## Comparisons by research question\n")
    for slug, name, strand, investigation, role, why, limit, next_step, reference in table(source, 9):
        if not re.fullmatch(r"[a-z][a-z0-9_]*", slug) or (investigation and not re.fullmatch(r"INV-\d+", investigation)):
            continue
        if not name or not next_step:
            continue
        yield slug, dict(name=text(name), strand=text(strand), investigation=investigation, role=text(role),
                         why=text(why), limit=text(limit), next_step=text(next_step),
                         links=dossier_links(dr, reference))


def public_slug(label: str) -> str:
    key = name_key(label)
    return {"dichloroacetate": "sodium_dichloroacetate"}.get(key, key.replace(" ", "_"))


def load_cards(dr: Path, public_compounds=()) -> dict:
    cards = cycle_cards(dr)
    for slug, card in programme_cards(dr).items():
        if slug in cards:
            card["links"] = {**cards[slug]["links"], **card["links"]}
        cards[slug] = card
    for slug, comparison in comparison_cards(dr):
        card = cards.setdefault(slug, dict(result="", question="", group="comparison", links={}))
        cards[slug] = {**card, **comparison, "links": {**card["links"], **comparison["links"]}}
    for item in public_compounds:
        for name in item.get("names_public") or ():
            label = name["label"]
            slug = public_slug(label)
            if not slug or slug in cards:
                continue
            question = text(str(item.get("next_test") or "")) or "Establish what this compound can distinguish in the published comparison."
            cards[slug] = dict(name=label, strand="", role="Named in an investigation", result="",
                               question=question, group="pending", links={})
    return cards


def render(dr: Path, pdf_reports: set[str], cards: dict | None = None) -> str:
    cards = load_cards(dr) if cards is None else cards
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
    strands = {}
    for slug, card in cards.items():
        if card.get("why"):
            strands.setdefault(card["strand"], []).append((slug, card))
    choices = []
    for strand, entries in strands.items():
        items = "".join(f'<li><a href="#analysis-{slug}">{escape(card["name"])}</a>'
                        f'<span>{escape(card["role"])}</span></li>' for slug, card in entries)
        choices.append(f'<div><h4>{escape(strand)}</h4><ul>{items}</ul></div>')
    research = (f'<div class="ca-pathways" role="region" aria-labelledby="ca-pathways-title"><h3 id="ca-pathways-title">'
                f'Where to look next</h3><div class="ca-pathway-grid">{"".join(choices)}</div></div>') if choices else ""
    return (f'<section id="compound-analyses" class="compound-analyses" aria-labelledby="ca-title"><header class="ca-hero">'
            f'<h2 id="ca-title">Compound Analyses</h2><p>Find the evidence, the biggest uncertainty and the next useful comparison for each WWOX research lead.</p>'
            f'<div class="ca-metrics"><span>{len(cards)} compounds</span><a href="#ca-browse">Browse all analyses</a></div></header>'
            + research +
            '<p class="ca-method" id="ca-browse">The order reflects documented research priorities. Names within each group are alphabetical. Research use only. Not medical advice.</p>'
            '<div class="ca-search" hidden><label for="ca-query">Find a compound</label>'
            '<input id="ca-query" type="search" placeholder="Search by name or mechanism"><span role="status"></span></div>'
            + "".join(sections) + "</section>")
