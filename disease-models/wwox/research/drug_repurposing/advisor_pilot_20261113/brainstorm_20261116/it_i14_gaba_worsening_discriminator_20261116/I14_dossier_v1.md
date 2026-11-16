# I14 Raised ambient GABA and the emergent seizure types: a clinical discriminator between the pictures (dossier v1; IT; non-canonical; hypothesis; not medical advice)

Written for: ADV (cross-reading), SCI (owner of I1, I6, I13), HE, and a clinician-researcher for D5c. Reference genotype class only. Mechanism level; no agent recommended; BLOCK-1 flags only from public labels (not run here). Status ADVANCE; depth: chain with an experiment-ready search design. Labels: KNOWN / HELD-DATA / ASSUMED / INFERRED. All counts are from the sealed per-child table (`it_i2_semiology_20261116/extraction_v1`), exposure-row or child counts, not independent tests, post hoc where marked.

**Answer first.** Two children had myoclonic seizures noted after vigabatrin and one had spasms about three months after topiramate. These cannot discriminate the pictures: in all three the exposure CONTROLLED the treated seizure type ('resolved'), the new type is not stated as worse, the start age and latency are not printed for two of them, and the same sequence (spasms, then myoclonic or tonic types) occurs in children who never received a GABA-transaminase inhibitor. Counted from the same table (post hoc, recounted by script): of 23 children with spasms at onset, 14 had a GABA-transaminase inhibitor and 9 did not; a later myoclonic course is stated for 1 of the 14 (Al-Baradie 2.1, the case above) and for 4 of the 9 (Johannsen 1 and 2, Al-Baradie 1.2, Chong 4). Ten of the 23 are Oliver children whose table lists seizure types 'at onset' with no later ordering, so 'not stated' there is not 'absent'. The unexposed children are older at report (follow-up to 10 years against months), so the comparison is confounded by follow-up time and cannot show that the drug is irrelevant either. The honest reading: the held reports give a natural-course baseline for spasm-to-myoclonic evolution that is as large as the emergent rate after vigabatrin, and no discrimination. The value of I14 is the design: what each picture predicts for age, semiology and latency, and one cheap search that can discriminate.

## D1 Chain
1. Vigabatrin raises ambient GABA (KNOWN, class mechanism: GABA-transaminase inhibition; a label-level fact). GAT-1 blockers do the same by another route.
2. In the reference genotype class, the burst-type network is held to be near threshold (HELD-DATA, neocortex, P13-P17 slices; I1).
3. Consequence of raised ambient GABA differs by picture (INFERRED, each from a dossier): I13 tonic brake strengthened; I1/I10 hyperpolarisation recruits rebound; I6 chloride loading makes GABA depolarising in a high-chloride state.
4. A new seizure type after exposure could be (i) the drug acting by one of those routes, (ii) unmasking: control of the dominant type reveals others (ASSUMED, general), (iii) natural evolution of the age-dependent semiology (HELD-DATA: ordered semiologies in children.tsv).

## D2 Why non-obvious
The usual question is 'does the drug work'. This asks which sign of a side-effect would each mechanistic picture predict, and uses that sign, not the efficacy, as the discriminator; and it requires the natural-course baseline, which the case reports hold but nobody tabulated.

## D3 Predictions by picture (the table is the dossier's main output)
| picture | worsening expected after ambient GABA up? | semiology | age window | latency after start | dose-withdrawal pattern |
|---|---|---|---|---|---|
| I13 tonic brake | NO (bursts down) | none new from this route | any | none | no reversal |
| I1/I10 rebound (thalamocortical, state-dependent) | YES | myoclonic, absence-like, sleep-transition clusters | after the thalamocortical circuit is mature (months, not the first weeks) | days to weeks, dose-related | reverses on dose reduction |
| I6 chloride-loaded (depolarising GABA) | YES, different course | spasms/focal clusters, any in the youngest | youngest window; fades as extrusion matures | hours to days | fades with age more than with dose |
| natural evolution (null for I14) | independent of drug | spasm to myoclonic/tonic order | age-locked (months 3-12 for spasms in the reports) | none relative to start | none |
| unmasking | after good control of dominant type | any | any | after control, so weeks | none |
**Surprising prediction.** If the I1/I10 picture holds, vigabatrin-type exposure should produce events that cluster in sleep transitions and respond to dose, a signature no spasm-control study looks for; if I13 holds, an extended GABA-raising exposure should lower, not raise, the events of the burst type. Two opposite signs for one exposure is what makes it a discriminator.

## D4 Model
SCI's `rebound_oscillator.py` (slice) gives the sign for tonic and phasic potentiation: silencing in almost all parameter sets, aggravation only in a steep-rebound regime with tonic target (2 of 47 sets). So the slice model is on I13's side; the thalamocortical prediction needs a thalamus that the model lacks (stated in the model's limits). A thalamocortical extension is the model task, assigned to nobody yet.

## D5 Discriminating experiments
(a) No new data (post hoc, labelled; the same 14 reports, a different question): per child, (1) spasm-at-onset children, (2) later myoclonic/absence-like/tonic types stated, (3) exposure to GABA-raising agents before that statement, (4) age at report as follow-up proxy. Done above in counts; the missing items are the onset age of the later type and the start age of the agent (150 of 170 exposure rows have no line of therapy; start age is blank for the two vigabatrin children; Shaukat 1 had prednisolone before vigabatrin, so the order is steroid then vigabatrin, a co-therapy confound). What the three rows can exclude: nothing. What they cannot: any picture. What they show: the new type appears after control, in an age-window where the same evolution occurs without the drug.
(b) New data, cheapest: a search for exposure-with-worsening statements in OTHER reports (not the 14): the same rubric (RUBRIC_FROZEN.md plus addendum 1) applied by a delegate that has not read any cells, to reports of children with the reference genotype class or of infantile-onset epilepsies in which a GABA-raising agent was given, recording start age, latency, semiology of the new type, dose change, sleep timing and the control of the dominant type. The extraction would also give V2.1 an allowed outcome table (made after the merge commit by someone who has not read the cells). Sources: lawful public reports only; a reCAPTCHA is a stop; no e-mail address to any service.
(c) Clinical-observational (a clinician-researcher): when a GABA-raising agent is started in the reference class, a structured diary for 8 weeks: seizure types with sleep-wake timing, EEG at baseline and week 4 (sleep), dose changes; the picture-by-picture table in D3 is the analysis plan; both outcomes: new myoclonic/absence-like events clustering in sleep and dose-related favours I1/I10; none, with falling events, favours I13; early events in the youngest that fade favour I6.

## D6 Intervention logic (labels, no recommendation)
Links acted on: ambient GABA (GABA-transaminase inhibitor, GAT-1 blocker); the rebound gate (T-type-like blockers, HCN blockers); chloride (KCC2/NKCC1 modulators, research tools); tonic receptor (neurosteroid-type, delta-preferring). Aggravation counterparts: for ambient GABA, the dose-dependent worsening predicted by I1/I10. BLOCK-1 from public labels: the GABA-transaminase inhibitor class has a boxed warning for permanent vision loss (public label); the GAT-1 blocker has none in a boxed-warning screen, which is not safety.

## D7 Combination
It discriminates among I13, I1/I10 and I6 and brings I2 (semiology and age) into the same table; it needs I10's sleep-staged recording. Contradiction to settle: slice model says silencing, the clinical lead (if real) says new types; both can be true only at different circuit levels (my I1 attack).

## D8 Stronger / killed
Stronger: other-report extraction with latencies showing dose-related, sleep-clustered, reversible events. Killed by a test: in the other-report extraction, emergent types after GABA-raising agents occur at the rate of the unexposed natural course at matched ages and show no dose or sleep signature (the aggravation arm of I1/I10 and I6 weakens; I13 survives).

## D9 Cheapest next step, no new literature search for me today
Table the natural-course baseline properly (ages of first myoclonic mention per child, from children.tsv; IT, 20 minutes); then draft the extraction brief for the other-report search (IT), to be run by a delegate after ADV releases it, with V2.1's perimeter respected.
