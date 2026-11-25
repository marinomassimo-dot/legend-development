"""IT 2026-11-25: qualifies my own ADV-238 wording after SCI's ADV-239 (message of 2026-11-25): 'do not survive removal of M6 and F8' is true on q < 0.05 only.
TNFA is lost without the pair (cortex reverses; M6 alone reverses it); IL6/JAK/STAT3 and HYPOXIA lose q < 0.05 in some or all regions but keep a positive score in all three forebrain regions.
Edits: IT6 README row 5 bracket, IT12 README K01 Update line, the proposed candidate CC-20261125-ORCHESTRATOR-ADV238-P47T-TWO-ANIMALS-01 (PROPOSED, not propagated). Idempotent; wording only.
Run from the repository root."""
from pathlib import Path
DR = Path("disease-models/wwox/research/drug_repurposing")
A239 = "advisor_pilot_20261113/brainstorm_20261116/adv239_influence_audit_sci_20261125/RESULT_ADV239_INFLUENCE_AUDIT_SCI_20261125.md"
n = 0
def edit(path, old, new, marker):
    global n
    t = path.read_text(encoding="utf-8")
    if marker in t: return
    assert t.count(old) == 1, (str(path), t.count(old), old[:70])
    path.write_text(t.replace(old, new), encoding="utf-8"); n += 1
edit(DR / "partial_benefit_it6_p10_20261029/README.md",
 "the TNFA and IL6/JAK/STAT3 hallmark enrichments do not survive removal of M6 and F8, the two animals that also carry the activity-gene surge (IT12 premises P8, 2026-10-31); read as a state of two of five mutants, not as a genotype-wide inflammatory signature;",
 "qualified by ADV-239 the same day: without M6 and F8 the TNFA enrichment is lost (cortex reverses, M6 alone is enough) and the IL6/JAK/STAT3 and HYPOXIA enrichments lose q < 0.05 in some or all regions but keep a positive score in all three forebrain regions (about three quarters of the full score); the two animals also carry the activity-gene surge (IT12 premises P8, 2026-10-31); read TNFA as resting on one or two animals and IL6/JAK/STAT3 and HYPOXIA as sign-stable but threshold-dependent, not as a genotype-wide inflammatory signature;",
 "qualified by ADV-239 the same day")
edit(DR / "p47t_it12_20261031/README.md",
 "HYPOXIA survives only in hippocampus; the TNFA and IL6/JAK/STAT3 enrichments do not survive in any region. Wording only, no number above changes.]",
 "HYPOXIA keeps q < 0.05 only in hippocampus; the TNFA enrichment does not survive in any region (cortex reverses), and IL6/JAK/STAT3 and HYPOXIA lose q < 0.05 but keep a positive score in all three regions without the pair (qualified by ADV-239, " + A239 + "). Wording only, no number above changes.]",
 "qualified by ADV-239")
c = DR / "../commit_candidates/CC-20261125-ORCHESTRATOR-ADV238-P47T-TWO-ANIMALS-01.md"
c = Path("disease-models/wwox/research/commit_candidates/CC-20261125-ORCHESTRATOR-ADV238-P47T-TWO-ANIMALS-01.md")
M = "Qualified by ADV-239"
edit(c, "**TNFA_VIA_NFKB and IL6_JAK_STAT3 are met in no forebrain region without them; HYPOXIA only in hippocampus; GLYCOLYSIS in all three.**",
 "**on q < 0.05 TNFA_VIA_NFKB is met in no forebrain region without them (cortex reverses; M6 alone is enough), IL6_JAK_STAT3 and HYPOXIA lose q < 0.05 in some or all regions but keep a positive score in all three regions (about three quarters of the full score); GLYCOLYSIS stays in all three.** [" + M + " (SCI, 2026-11-25): the first draft of this sentence said 'met in no region' without the threshold.]", M)
edit(c, "append: \" In a leave-two-out check (ADV-233) the TNFA and IL6-JAK-STAT3 enrichments behind it are met in no region without the two animals (M6, F8) that carry the activity-gene surge; read as a state of two of five mutants.\"",
 "append (SCI's wording, ADV-239 section 4): \" TNFA/NF-kB rests more than half on animal M6 (cortex reverses without it). IL6/JAK/STAT3 loses the q threshold without M6 and F8 but keeps its sign and about three quarters of its enrichment score.\"", "SCI's wording, ADV-239 section 4")
edit(c, "append: \" It also rests on two of five animals (ADV-233).\"", "append: \" The TNFA part also rests on one or two animals (ADV-233, ADV-239).\"", "The TNFA part also rests")
edit(c, "GLYCOLYSIS stays enriched in all three forebrain regions without M6 and F8; HYPOXIA only in hippocampus.\"",
 "GLYCOLYSIS stays enriched in all three forebrain regions without M6 and F8; HYPOXIA keeps q < 0.05 only in hippocampus but keeps a positive score in all three regions (ADV-239).\"", "keeps a positive score in all three regions (ADV-239)")
edit(c, "finds TNFA and IL6-JAK-STAT3 met in no region without two of the five mutants.]\"",
 "finds the TNFA enrichment lost without two of the five mutants (cortex reverses) and IL6-JAK-STAT3 below q 0.05 but sign-stable.]\"", "sign-stable.]")
edit(c, "1. In ADV-233's `disposition_adv233.tsv`, TNFA_VIA_NFKB and IL6_JAK_STAT3 are met in no forebrain region without M6 and F8; HYPOXIA in hippocampus only; GLYCOLYSIS in all three.",
 "1. In ADV-233's `disposition_adv233.tsv`, on q < 0.05 TNFA_VIA_NFKB and IL6_JAK_STAT3 are met in no forebrain region without M6 and F8, HYPOXIA in hippocampus only, GLYCOLYSIS in all three; and in ADV-239's `gsea_loo_adv239.tsv` the scores of IL6_JAK_STAT3 and HYPOXIA stay positive in all three regions without the pair, TNFA reverses in cortex.\n4. **Further consumers and wording:** ADV-239 RESULT section 4 (SCI) gives wording for K01, J01, L01, F02, F03, INV-06, INV-15, INV-16, T19 and CLAIM 005; it is to be taken into this candidate at propagation, after the blind check, and none of it is applied here.", "ADV-239's `gsea_loo_adv239.tsv`")
print("edits", n)
