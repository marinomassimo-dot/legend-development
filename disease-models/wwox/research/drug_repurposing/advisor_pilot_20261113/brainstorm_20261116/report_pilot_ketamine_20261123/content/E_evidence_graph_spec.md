# E. Evidence graph specification (for the renderer; no layout is prescribed)

AI-curated research brief for discussion with a clinical team. Hypothesis level. Machine-readable files in this folder: `E_evidence_graph_nodes.tsv` (18 nodes) and `E_evidence_graph_edges.tsv` (19 edges). Numbers in square brackets are entries of list B.

## Purpose
To show where the transfer from the published slice finding to ketamine breaks, and which single readout would discriminate the rivals. A reader should be able to follow every node to a source and see which statements are observed and which are hypothesised.

## Node kinds
* `observation` (D): read in a source; the locator is in A.
* `inference` (I): reasoned from observations.
* `claim`: a statement about one drug class. The competitive-antagonist claim (N4) is supported for d-APV only; the pore-blocker claim (N5) has no direct support.
* `alternative` (H): a rival reading that predicts the same burst readout.
* `experiment` (E): a proposed measurement.
* `gap`: a documented absence (N18).

## Edge labels (every edge carries one status)
* **OBSERVED:** the link is a stated measurement or a documented absence, with its source in the edge row.
* **HYPOTHESISED:** the link is a reasoned or predicted relation; none has been tested.
The break in transfer is edge G4 (N3 to N5, `transfer_break`) with the rivals G7, G10, G12 and G14 pointing into N5 and the discriminating readout N17 (edges G16 to G18) separating them. The only contradicting-leaning observation is G13 (bursting recorded in vivo with ketamine on board), shown with its three limits in the edge label.

## Suggested reading order for a figure
N1, N2 to N3 (the finding), then N4 against N5 (the two claims), then the three alternatives (N8, N11, N13) each with their motivating observations, then N17 as the readout, then N16 and N18 as the two limits (exposure and the missing direct test).

## What the graph does not do
It does not weight or score the alternatives, does not sum evidence across unlike models, and does not imply that any drug should or should not be used. A graph-coverage percentage is not shown: an earlier brief's coverage numbers reproduced arithmetically but changed with the node definitions and the denominator, so they do not travel (see D).
