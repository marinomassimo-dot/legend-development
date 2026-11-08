# Phase 1 note — INV-18 membrane physiology (os-18)

Source: `INV-18_membrane.txt`, 155 lines by the verifier's count (154 by the Phase-1 count; the Bottom Line is L155), read in full. Anchors in the TSVs are line numbers of that file.

* What it is: an AI-generated exploratory report (question L1; "View full report" interface text L2-3) on increased sag, post-inhibitory rebound and depolarized RMP in Wwox-deficient cortical neurons. Structure: Summary, six Key Findings (F001-F006), three hypotheses (H1 HCN number, H2 lipid/scaffold gating, H3 non-HCN composite), an ASCII model, a side-by-side table, a discriminating-logic table, Evidence Base, Supported/Refuted, Limitations, follow-up experiments, Bottom Line.
* Measured vs reasoned: the only WWOX electrophysiology cited is one mouse study (the triad); the other WWOX data are serum HDL/lipids and GSK3beta/lithium seizure data. Everything linking WWOX to HCN, Kv7 or Cav3 is stated by the report itself as inferential (L143). HCN-lipid, PIP2, filamin A, Kv7, T-type and GAERS items are transfers from other systems.
* Internal tensions in the text:
  - the Wwox data are called an "in-vitro" immature model and, in F001, a "neuronal culture" class preparation, while the probes are on "neocortical slices"; the developmental stage is never given;
  - "Ih reverses near -30 mV" is uncited;
  - the report says increased Ih is restraining in "multiple models", but the text supports one (GAERS) plus the CaV3.3 knockout for rebound;
  - the L12 sentence about "at least one genetic epilepsy model" and the GAERS item are the same source;
  - sag is treated as HCN-exclusive, so the H3 rejection criterion (the Kv7 plus T-type combination cannot abolish sag) is close to circular; row 3 of the discriminating table gives "Partial/No" for HCN while H3's rebound/RMP arm is said to be separable;
  - L150 says elevated HCN protein with unchanged V1/2 "favors H1", which differs from L52 (rejects H2) only by direction of emphasis;
  - the report concedes no input-resistance control (L141), though sag depends on it, yet builds the whole logic on sag;
  - three corroborating PMIDs per claim (e.g. L23) are listed without any content description.
* Sentences addressed to a reader/agent: "View full report" (L2) is interface text; no instruction to the agent. The "Proposed Follow-up Experiments" are recommendations, recorded as items, not acted on.
* Counts: 59 extraction rows, 24 rows in sources_cited (23 PMIDs plus a MONDO id), 6 chains.
