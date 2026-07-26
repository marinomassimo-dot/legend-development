---
name: legend-dashboard
description: Generate or refresh Obsidian-friendly LEGEND dashboard notes from the Markdown workspace. Use when the operator asks for dashboards, Obsidian views, status pages, CC/inbox/LINT/full-text queue summaries, or navigation pages. Read-only toward scientific current files; write only under _docs/dashboards unless explicitly asked otherwise.
---

# LEGEND Dashboard

Create operational dashboard notes for LEGEND without changing canonical scientific state.

## Workflow

1. Read `framework/state/state_manifest_current.md` first.
2. Read only the operational/source files needed for the requested dashboard:
   - CC queue: the commit-candidate log
   - Inbox: the inbox
   - Activity: the activity log
   - Full-text queue: the full-text queue
   - Researchers: the research-group knowledge base
   - LINT rules: `framework/protocols/prompt_lint_integrity_check.md`, `framework/protocols/wikilink_schema.md`
3. Write dashboard notes under `_docs/dashboards/`.
4. Do not modify the 4 canonical current files.
5. If a dashboard discovers an inconsistency, report it and optionally add it to a dashboard section named `Open Checks`; do not repair canonical files.

## Dashboard Style

- Prefer Obsidian-native Markdown with stable wikilinks.
- Use compact tables for operational data.
- Use native Obsidian search blocks for robust views over legacy Markdown:

```query
"Status: PENDING" path:session_commit_log.md
```

- Add Dataview blocks only as optional enhancements and label them `Requires Dataview`.
- Keep dashboard files non-canonical. They summarize, they do not decide.

## Recommended Files

- `_docs/dashboards/legend_dashboard.md`
- `_docs/dashboards/cc_queue.md`
- `_docs/dashboards/lint_debt.md`
- `_docs/dashboards/fulltext_queue.md`
- `_docs/dashboards/research_contacts.md`

## Safety

Dashboard generation can be repeated. Preserve manual notes if present by updating clearly marked generated sections only, or ask before overwriting heavily edited dashboards.
