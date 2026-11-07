# INV-06 myelin recovery: delta (label my-p, receipt suffix 95), 2026-11-07

Non-canonical research, not medical advice. WWOX-DEE reference genotype class only. Row ids E01-E40: `evidence.tsv`; levels: `levels.tsv`; comparison: `experiment.tsv`.

## Answer first
No pharmacological class is sustained as a recovery strategy by what was read. Sustained: (1) the WWOX base supports a neuron-side contribution, not "the oligodendrocyte is intrinsically normal" and not "a soluble signal is missing"; (2) the GSK3 sign on differentiation is divided; (3) any enhancer must be read at four levels (maturation, sheath, conduction, network), because neonatal clemastine moved two of them in opposite directions.

## 1. WWOX base, corrected
- DATO. Olig2-Cre and GFAP-Cre validations (Supp Fig 1E, 1F) are one field each, no count or efficiency (E01, E02); the Olig2-Cre P17 MBP result is qualitative (Supp Fig 8 viewed, no n; E04). Reporter percentages from other loci do not transfer.
- INFERENZA. This excludes a large intrinsic effect on P17 MBP only; EM, node, conduction and challenge phenotypes stay open (repository preprint rows E24-E26: differentiation block in cuprizone recovery, cited not re-read).
- DATO. Co-culture: embryonic DRG neurons, wild-type OPCs, two experiments, n = 4 v 4; fewer myelinating-class, more premyelinating-class cells on null neurons (E05-E07). No conditioned-medium, transwell, activity or factor arm in the text read.
- INFERENZA. Neuron-side contribution supported; contact or substrate integrity, neuronal state and a soluble product are not separated; peripheral, seizure-free neurons.
- DATO. S-KO at P17 has all four levels measured (E08-E11); latency does not name its cause.
- IPOTESI. The Lundgaard coculture format without added neuregulin was activity independent (E30); if Repudi's behaves alike, bursts are an unlikely cause of its deficit.

## 2. GSK3 direction
- DATO. Azim and Butt (abstract only; full text behind subscription): several inhibitor chemotypes raise differentiation and proliferation; CREB up, Notch1 down; Wnt3a opposes (E19-E22).
- DATO. Dong 2020 (full text): after Foxg1 knockdown GSK-3 beta protein rose, beta-catenin fell; SB216763 reversed that and lowered the CNPase-positive share (E13-E15). In this paper the inhibitor opposes differentiation: not confirmation of Azim and Butt, and it cites the opposite view itself (E18). No phospho-GSK3 or activity readout is listed (E16); one compound, in vitro rescue, adult injury.
- DATO (abstracts). Genetic GSK3 beta loss in mature oligodendrocytes changed survival, not differentiation (E23); Cdk5 loss came with more GSK-3 signalling and failed maturation, an association (E24).
- INFERENZA. Proliferation and survival rise in every source; the differentiation sign depends on level, context and arm (Wnt, CREB, Notch). Which arm is live in null-neuron OPCs is unknown. Lithium's effect on provoked seizures implies neither myelin recovery nor one target.
- NON RISOLTO. Reopen with a genetic oligodendrocyte-lineage differentiation test in developing myelination (Q12).

## 3. Activity and myelination
- DATO. Allen 2026 (full text): neonatal mouse (P0-P8; P4 slice), less excitatory activity raised premyelinating and maturing shares, more lowered them, AMPAR block mimicked silencing; markers only, ending before robust myelination (E25-E29). Lundgaard 2013 (full text): sheath formation was activity independent without added neuregulin, NMDA-receptor dependent with neuregulin or BDNF; adult lesion repair needed NMDA receptors (E30-E34).
- INFERENZA. Different levels (marker shares versus wrapping and g-ratio), stages and modes; "adult" versus "neonatal" does not settle them.
- IPOTESI (tests in `experiment.tsv`): H1 loss of a favourable signal (X1, X2 factor arm); H2 pathological activity obstructing maturation (X0, X2); H3 axonal or substrate defect (X1 fixed-neuron arm); mixtures. Allen's window ends at P8, S-KO bursts are recorded P13-P17 (E11): H2 needs evidence of early hyperactivity that does not exist.

## 4. Link with INV-05
DATO: activity or AMPAR block raised differentiation markers in the neonate (E27); NMDAR block removed sheath formation only where neuregulin or BDNF had set that mode (E31). INFERENZA: neither shows myelin damage or benefit from fewer bursts; neuronal and oligodendroglial receptors are not separated (E29, E34). Shared comparison: X2, one arm set for both packages, firing verified in the dish.

## 5. Comparators
- Clemastine: Pdk1 icKO rescue (E38) is marker, synapse and behaviour recovery in an intrinsic seizure-free defect, no conduction after treatment; wild-type neonatal treatment raised differentiation yet slowed callosal conduction and cut nodes (E39, E40). Not a universal positive control; each enhancer arm needs conduction, EM and a wild-type arm (X3).
- Pdk1 is 3-phosphoinositide-dependent protein kinase-1, upstream of Akt-mTOR, not a pyruvate dehydrogenase kinase (E35). The constitutive lineage deletion had seizures from P14 (E37): the arrow can run from myelin failure to seizures.
- T3 was in the medium of every spheroid yet KO hypomyelination appeared (E12); no T3-free arm, so not a rescue test. T3 or GSK3 recovery would not place the defect wholly at maturation. Multi-chemotype convergence is the only attribution control seen (E19).

## Open question, minimum comparison
Priority: is the null-neuron deficit carried by contact or substrate, a soluble product, or activity? Minimum: X1 then X2 in the existing co-culture with existing null embryos, no new colony; X0 (descriptive re-read of the deposited S-KO nuclei; pooled, no replicate structure invented) first. Strengthens a signal or substrate hypothesis: deficit persists with activity blocked and appears with fixed null neurons. Weakens it: deficit tracks the activity arms. Changes it: factor addition rescues (switch-type signal).

## Proposed updates (nothing changed here)
IT29 P3-C C04: validations are single fields; co-culture does not separate contact from soluble. Signed-coupling table: GSK3 differentiation sign `undetermined`, level and arm beside it. Clemastine card: conduction discordance as a design requirement. INV-05: adopt X2.

## Not reached
Azim and Butt full text (subscription, stopped). Stage 2 abstracts only (29761559, 25080600; gap named in Q8). New-source figures not viewed. `../gsk3_eif2b_20261107/` absent in this worktree; GSK3 background from `../target_first_it15_qb_gsk3_20261101/README.md` by identifier only. New sources 6 of 8. Receipts: `receipts/INDEX.tsv`.
