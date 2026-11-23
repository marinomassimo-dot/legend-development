# Evidence graph specification (for the renderer; no layout is prescribed)

AI-curated research brief for discussion with a clinical team. Hypothesis level. Machine-readable files: the nodes table (18 nodes) and the edges table (19 edges). Numbers in square brackets are entries of the reference list.

## Purpose
To show where the transfer from the published slice finding to ketamine breaks, and which single readout would discriminate the rivals. A reader should be able to follow every node to a source and see which statements are observed and which are hypothesised.

## Node kinds
* `observation` (D): read in a source; the locator is in the decision-evidence section.
* `inference` (I): reasoned from observations.
* `claim`: a statement about one drug class. The competitive-antagonist claim (N4) is supported for d-APV only; the pore-blocker claim (N5) has no direct support.
* `alternative` (H): a rival reading that predicts the same burst readout.
* `experiment` (E): a proposed measurement.
* `gap`: a documented absence (N18).

## Edge status (every edge carries exactly one of four)
* **OBSERVED:** the link itself is stated by the source, or is a documented absence found by a search. It is not merely that the datum at one end was observed.
* **INFERRED:** a reasoning step from observations (for example "this observation makes that alternative a candidate", or the inference that d-APV bursts suppression supports an NMDA-receptor contribution). Drawn dashed.
* **HYPOTHESISED:** a predicted relation or competing prediction; none has been tested. Drawn dotted.
* **CONTEXT_ONLY:** shown for completeness, not as evidence for or against the link; its own label says why (edge G13). Drawn lightly.
The break in transfer is edge G4 (N3 to N5), which is a documented fact: no pore-blocker arm exists. The rivals G7, G10, G12 and G14 point into N5 and the discriminating readout N17 (edges G16 to G18) separates the first three. Edge G13 (bursting recorded in vivo with ketamine on board) is CONTEXT_ONLY and should be drawn lightly: its own label says it is not a test.

## Suggested reading order for a figure
N1, N2 to N3 (the finding), then N4 against N5 (the two claims), then the four alternatives (N8, N11, N13 and N15) with the observations that motivate them (N15, the sedation or co-medication context, is motivated by the clinical series rather than by a slice observation), then N17 as the readout, then N16 and N18 as the two limits (exposure and the missing direct test).

## What the graph does not do
It does not weight or score the alternatives, does not sum evidence across unlike models, and does not imply that any drug should or should not be used. A graph-coverage percentage is not shown: coverage percentages from an earlier team draft reproduced arithmetically but changed with the node definitions and the denominator, so they do not travel (see the negative-results and quantitative section).
