"""Parse declared Claim links, never identifiers inside a refusal or an annotation.

The leading declaration is authoritative. A none/pending prefix declares no edges;
parenthesised qualifications do not add edges. Unknown prose ends the declaration.
This parses links, not their scientific validity.
"""
import re


def declared_claim_links(value: str | None) -> set[str]:
    text = (value or "").strip()
    if re.match(r"(?i)^(?:none|pending)\b", text):
        return set()
    text = text.removeprefix("→").strip()
    text = re.sub(r"\[\[claim_registry_current#(CLAIM\s+\d{1,3})(?:\|[^\]]*)?\]\]", r"\1", text)
    text = re.sub(r"\([^)]*\)", "", text)
    links = set()
    while text:
        match = re.match(r"(?:CLAIM\s+)?(\d{1,3})(?![\d.])", text, re.I)
        if not match:
            break
        links.add(f"CLAIM {int(match[1]):03d}")
        text = text[match.end():].lstrip()
        separator = re.match(r"(?:[,;/·+&]|and\b)\s*", text, re.I)
        if not separator:
            break
        text = text[separator.end():]
    return links
