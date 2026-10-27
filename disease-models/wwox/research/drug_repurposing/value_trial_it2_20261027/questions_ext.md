# Value trial IT2 - questions, condition EXT (external only)

## Allowed inputs (the only part that differs between conditions)
You may use ONLY external, public sources: the PubMed MCP tools, ToolUniverse (including ChEMBL and Open Targets), the external-query adapters named in framework/scripts/README.md used purely as network clients, and public web pages. You must NOT open, read or search any file under disease-models/, registries/, ledger/, research/, files/ or any card, dossier, ledger or registry of this repository (the instructions you were given are the only repository content you may use). If you touch repository knowledge the run is void.

Context for every case: the disease of interest is WWOX-related developmental and epileptic
encephalopathy (WOREE; biallelic WWOX loss of function, human, paediatric). The question is about
RESEARCH work, not about treating anyone: nothing here is medical advice, a dose or a recommendation.

Cases (the intervention is named; nothing else is given):
- V1  Vitamin B6 (pyridoxine / pyridoxal phosphate) in WWOX deficiency.
- V2  Sodium channel blockers (e.g. phenytoin, carbamazepine, lamotrigine) and genotype-dependent
      response, in WWOX deficiency.
- V3  Modulation of ferroptosis (e.g. ferrostatin-1, erastin-class inducers, the GPX4 / SLC7A11 axis)
      in WWOX deficiency.

Questions, asked for each case:
- Q1  Which target, in which direction (inhibit / activate), for which endpoint, in which model and
      context does the available evidence bear on this intervention in WWOX deficiency? Say which
      statements are direct (WWOX model or WWOX patients), which are inference, and which come from
      another gene, disease, tissue or species. If the evidence does not fix a direction, say so.
- Q2  What counter-evidence, limits and transfer risks (model, species, disease, tissue, variant
      class, identifier or compound-versus-target confusion) exist?
- Q3  Do you propose a next measure (a research measurement, not a treatment), or do you abstain?
      If you abstain, give the reason and the condition that would reopen the question.

Required answer format, per case: Q1 / Q2 / Q3 as headed paragraphs, then a line `SOURCES:` with the
identifiers actually consulted (PMID, DOI, database record) and a line `DEPTH:` saying for each
source whether you read full text, an abstract, or only a database row. Finish the file with
`RUN LOG:` (your own count of tool calls, minutes used, which tools / files / services were used).
Write the answer to the file path given to you by the orchestrator. Answer in English.

BUDGET (identical for all conditions, enforced by the orchestrator, stated here): at most 25 tool
calls in total (every call counts: searches, file reads, shell commands) and at most 12 minutes of
wall time. Stop and write the answer when either is reached; an answer that says what it could not
check is better than one that runs over. One run only; no retries of a failed run.
