# Producer brief: repurposing-readiness sheets, first-pilot arms (SCI, 2026-11-16; non-canonical; not medical advice)

You read public sources into two tables. You do NOT recommend, rank or compare agents, give no dose, schedule or route, and make no clinical statement. Reference genotype class only. Every sheet carries the words "abstract-level, not a safety review". Do not start agents. Do not send any e-mail address (the operator's or any other) to any service; use no service that asks for a contact address. Use the PubMed tools for PubMed; for a public drug label use WebFetch with the default client only (no browser-style User-Agent). If a page serves a reCAPTCHA, interstitial or login, STOP on that source and write `not reachable lawfully` in the access column; never work around it. Zero spend.

## Agents (one row each; catalogue ids from IT's `brainstorm_20261116/it_block1_triage_20261116/README.md`)
NMDAR pore blocker: memantine (CHEMBL1699), ketamine (CHEMBL1714), esketamine (CHEMBL2364609).
GABA-A positive modulator, non-benzodiazepine: zolpidem (CHEMBL911), eszopiclone (CHEMBL1522).
GABA-A positive modulator, benzodiazepine: diazepam (CHEMBL12), clobazam (CHEMBL70418), clonazepam (CHEMBL452).
T-type blocker (not T-type selective for the second): ethosuximide (CHEMBL696), zonisamide (CHEMBL750).
Sodium-channel blocker: carbamazepine (CHEMBL108), lamotrigine (CHEMBL741), phenytoin (CHEMBL16).
Work in this order and WRITE the rows to disk after each class, so partial work survives.

## Table 1: `sheets.tsv` (one row per agent)
agent_id | agent | arm | class_label | mechanism_sentence | mechanism_source (PMID or held path) | class_level_approved_indications (label wording only; name the label source) | bbb_statement (verbatim sentence from a source that says it crosses or does not cross the blood-brain barrier, or `not stated at abstract level`) | bbb_source (PMID or label) | pediatric_label_statement (verbatim, only if a public source states one at abstract or label-heading level, else `none found`) | pediatric_source | interaction_or_contraindication_class (as the source states it, e.g. a labelled class; verbatim phrase) | interaction_source | flag_for_safety_triage (`none`, `yellow` or `red`, by the rule below) | flag_basis (one sentence naming the sentence in signals.tsv that sets it) | access_notes

## Table 2: `signals.tsv` (long form, 1 to 4 rows per agent)
agent | signal_type (`boxed_or_serious`, `tolerability`, `abuse_dependence_withdrawal`, `teratogenic_or_developmental`, `interaction`, `other`) | verbatim_sentence (copy it exactly from the source; no paraphrase; at most two sentences) | pmid_or_label_source | source_kind (`abstract`, `label_heading`, `label_text`) | accessed_how

## Flag rule (the flag is the SOURCE's wording, not your judgement)
`red`: a retrieved source states a boxed warning, or states serious, life-threatening or fatal reactions for this agent. `yellow`: a retrieved source states a clinically significant tolerability issue (dependence, abuse, withdrawal, psychiatric or cognitive effects, developmental toxicity, a named interaction class) without those words. `none`: neither found in the sources you read. `none` never means safe; say in flag_basis what you did read. When in doubt between two flags give the HIGHER one and say which sentence decides.

## Sources and depth
Abstract-level. Prefer a recent review or a label-level statement per agent; give the PMID. For an approved indication or a boxed warning you may read the DailyMed label headings (public US labels) by WebFetch; copy the exact heading or sentence. Do not read full-text papers for this task unless an abstract is missing the sentence you need, and then say so. Do not infer: if a source does not say it, write `not stated`. A sentence you cannot find verbatim is not entered.

## Done when
`sheets.tsv` has 13 rows, `signals.tsv` has at least one row per agent (or `none found` with the sources read), every quote is copied from a retrieved source, and a short `README.md` lists, per agent, the sources you opened and any source that was not reachable lawfully. Hand back the paths and the count of rows by flag.
