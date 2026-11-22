# Printable compound research briefs

When an in-depth study of a compound is ready to share, use the existing briefs here as templates. Add the dated English summary, the matching dashboard investigation ID and the public source links to one JSON file per report. Use the four stages **Data / Evidence → Inference → Hypothesis → Experiment** in every brief. Give each stage a short node in the knowledge graph and explain it below. State which observations support the inference, which prediction remains open, what the proposed experiment would compare, and the limits of transfer to WOREE. Use only public evidence and omit individual patient details, dosing instructions and treatment recommendations.

For a substantial study, use the opening page as the synopsis and add chapters for the source audit, comparisons, quantitative analyses, safety and decision-changing experiments. Include evidence depth, negative results and the relevant source links. Use tables for comparisons that readers need to scan.

Build the printable PDF and regenerate the dashboard and its publication package from the repository root.

```sh
python3 -B framework/scripts/repurposing_research_reports.py
python3 -B framework/scripts/repurposing_view.py run --source shareable
python3 -B framework/scripts/repurposing_view.py package
```

The dashboard links each PDF from its investigation. Keep the PDF and its JSON source together so future updates can be regenerated and checked.
