# Printable compound research briefs

When an in-depth study of a compound is ready to share, use the existing briefs here as templates. Add the dated English summary, the matching dashboard investigation ID and the public source links to one JSON file per report. Describe the evidence, the limits of transfer to WOREE and the remaining research question. Use only public evidence and omit individual patient details, dosing instructions and treatment recommendations.

Build the printable PDF and regenerate the dashboard and its publication package from the repository root.

```sh
python3 -B framework/scripts/repurposing_research_reports.py
python3 -B framework/scripts/repurposing_view.py run --source shareable
python3 -B framework/scripts/repurposing_view.py package
```

The dashboard links each PDF from its investigation. Keep the PDF and its JSON source together so future updates can be regenerated and checked.
