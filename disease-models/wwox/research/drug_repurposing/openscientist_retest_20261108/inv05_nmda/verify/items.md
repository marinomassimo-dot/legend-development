# Items for the blind verifier (statement, report anchor, source, locator hint, class) — the producer's reasoning and prior-check notes are withheld

## D01
- statement: DATO+INFERENZA: the report makes a GluN2B-selective NAM (radiprodil) the lead and a direct test of the GluN2B hypothesis, but its only in vivo support (PMID 38529699) is a GluN2A gain-of-function mouse line, so that support shows a GluN2B-directed circuit lever, not that GluN2B carries the WWOX burst.
- report anchor: L36,L102,L119 (F003; Evidence Base; Which Agents)
- source cited or found: PMID 38529699 (cited); PMID 40994429 (cited)
- locator hint: PMID 38529699 Abstract and Methods (genotype, sex, acute pre-stimulus dosing); PMID 40994429 variant panel (GRIN1 and GRIN2B only)
- class: binding/action/benefit

## D02
- statement: DATO: the "+" for radiprodil developmental safety and "human-safe" rest on one background sentence in an abstract ("appears to be safe in humans"), with no infant, synaptogenesis-window or WWOX datum; INFERENZA: the report scores it "+" while arguing the class carries apoptotic liability.
- report anchor: L36,L88,L101 (F003; matrix)
- source cited or found: PMID 40994429 (cited; abstract read 2026-11-08, receipt -33)
- locator hint: PMID 40994429 Introduction and Discussion (sources of the human-safety statement; full text unreachable)
- class: compound/class

## D03
- statement: INFERENZA: the claim that an NMDA-antagonist route is "novel (not yet explored in WOREE)" rests on a three-node knowledge base; found after: PubMed 2026-11-08, (WWOX OR Wwox) AND (memantine OR ketamine OR radiprodil OR ifenprodil OR NMDA receptor antagonist) = 0 hits; (WWOX OR Wwox) AND (NMDA OR GluN2B OR GRIN2B OR glutamate receptor) = 5 hits, titles not screened apart from PMID 34634460; earlier package: Europe PMC strings, titles only. Absence is bounded to title and abstract level, not a negative result.
- report anchor: L51 (F008)
- source cited or found: none (dismech knowledge base); queries.tsv Q10 and Q11
- locator hint: PubMed result lists; INV-05 row Queried column
- class: absence

## D04
- statement: INFERENZA: the "Refuted / not viable" verdict is applied to the availability of a tolerated competitive, pan-subunit drug, which is an availability claim; it is not an experimental refutation of anything, and the d-APV dependence of the burst (one drug, one preparation) is untouched.
- report anchor: L125 (Supported vs Refuted)
- source cited or found: none (report label); PMID 15335108 and the perzinfotel gap (see D05, D09)
- locator hint: Report L125 wording only
- class: absence

## D05
- statement: DATO: perzinfotel (EAA-090) failure for psychotomimetic or neurotoxic effects and excess mortality is not found in PubMed (term perzinfotel, 11 hits on 2026-11-08, titles and abstracts screened: preclinical pharmacology, veterinary anaesthesia and pain studies, a prodrug paper; none a clinical failure report); excess deaths belong to selfotel. PMID 15075380 abstract: EAA-090 is 10 times more potent at NR2A than NR2B or NR2C receptors.
- report anchor: L9,L161 (Summary; Falsification)
- source cited or found: none cited by the report; PMID 15075380 (found)
- locator hint: PMID 15075380 Abstract; clinical-development record of perzinfotel outside PubMed not searched
- class: absence

## D06
- statement: DATO: the dextromethorphan "weak, discouraging encephalopathy data" has no citation; the nearest source (PMID 22261077) is a ketogenic-diet paper whose abstract states in one sentence that ketamine and dextromethorphan in neonatal nonketotic hyperglycinemia "have been tried but the outcome is usually poor", with no data. Found after: PubMed 2026-11-08, dextromethorphan AND (encephalopathy OR nonketotic hyperglycinemia) AND (neonatal OR infant) = 47 hits, not screened.
- report anchor: L92,L122,L48 (matrix; Which Agents; F007)
- source cited or found: PMID 22261077 (cited for NKH only)
- locator hint: PMID 22261077 Abstract; primary NKH dextromethorphan series not identified
- class: compound/class

## D07
- statement: INFERENZA: the memantine (plus ketamine) response in one ATP1A2-related DEE infant is a transfer from another monogenic disorder; concomitant ketamine, timing (genetic result in the second week of memantine) and authors "apparent efficacy" wording limit attribution; the report calls it "the most direct precedent" and "direct DEE precedent".
- report anchor: L13,L48,L113,L120 (F007; Which Agents)
- source cited or found: PMID 39970743 (cited)
- locator hint: PMID 39970743 case description and Discussion (timing, concomitant treatment)
- class: transfer from other system

## D08
- statement: INFERENZA: the report states NMDAR block is sufficient so gap-junction co-dependence does not matter (L26) and also that it complicates attribution and justifies combinations (L132, L153); the underlying gap-junction label rests on carbenoxolone, which the WWOX source itself lists as also blocking NMDA receptors and pannexin, with effect incomplete on washout.
- report anchor: L26,L132,L153 (Reference Pharmacology; Limitations; Follow-up)
- source cited or found: PMID 34634460 (cited); module manifest PMID34634460.json (found)
- locator hint: PMID 34634460 Results 2.4 and Discussion 3.4 carbenoxolone paragraph; Fig 3 and Table S1
- class: WWOX datum

## D09
- statement: DATO: for selfotel the head-injury phase-III trial was aborted because concurrent low-dose stroke studies showed more deaths; a retrospective analysis did not confirm increased mortality in head injury (PMID 15335108 abstract); the report cites it as the competitive class failing "for excess deaths and adverse events".
- report anchor: L42,L108 (F005)
- source cited or found: PMID 15335108 (cited; found to fit)
- locator hint: PMID 15335108 Abstract
- class: compound/class

## D10
- statement: INFERENZA: GluN2B dominance of immature cortex is used to infer GluN2B carriage of the WWOX burst, which the report itself calls inferential; one of the two cited sources (PMID 28782587) is a neonatal-rat ketamine-exposure study and may not support the stated EPSC claim; no WWOX subunit datum exists.
- report anchor: L33,L128 (F002; Limitations)
- source cited or found: PMID 21896318; PMID 28782587 (cited; identity checked, not read)
- locator hint: PMID 28782587 Results (EPSC decay and ifenprodil sensitivity); PMID 21896318 mouse regional data
- class: transcript/protein/activity/phenotype

## D11
- statement: DATO+INFERENZA: in autaptic rat hippocampal culture memantine blocked synaptic NMDAR current substantially and an operationally defined extrasynaptic current about twice as much, so "tonic means inaccessible to channel blockers" is not supported as stated; whether the WWOX burst drive is tonic or phasic and what the recording Mg2+ was remain unmeasured.
- report anchor: L11,L45,L157 (Summary; F006; Falsification)
- source cited or found: PMID 15717010 (cited, not read); PMID 20720132 (module, read)
- locator hint: PMID 20720132 Results (1 uM and 10 uM with 1 mM Mg2+); PMID 34634460 Methods (perfusate Mg2+)
- class: binding/action/benefit

## D12
- statement: IPOTESI: developmental apoptosis could make a burst-suppressing concentration unsafe in the infantile window; the cited sources are reviews and a high-dose MgSO4 mouse study read by nobody here, and the therapeutic-index ratio in WWOX tissue is unmeasured; discriminating test: caspase-3 and viability across the efficacious range in age-matched tissue.
- report anchor: L38,L81,L149 (F004; overlay; Follow-up)
- source cited or found: PMID 12520755; PMID 17312200; PMID 19204407; PMID 23395831 (cited; identity checked, not read)
- locator hint: PMID 12520755 (review); PMID 19204407 Methods (dose and age)
- class: transfer from other system

## D13
- statement: DATO: d-APV at a single concentration eliminated the Wwox neuron-knockout cortical slice bursts (51 bursts, 5 slices, 3 animals, postnatal day 13 to 17); this is dependence of the burst on NMDAR activity, one drug and one preparation, and it does not show receptor alteration, subunit, or a spared physiological window.
- report anchor: L26,L30 (F001)
- source cited or found: PMID 34634460 (cited; complete read in module)
- locator hint: PMID 34634460 Fig 3 and legend, Table S1
- class: WWOX datum

## D14
- statement: INFERENZA: efficacy of ketamine in refractory status epilepticus (56 percent pooled termination) and neonatal sequelae are generic non-WWOX data; sequelae after status epilepticus treatment are not attributable to the drug, and the pooled figure does not speak to a WWOX burst.
- report anchor: L48,L111,L112 (F007)
- source cited or found: PMID 41409370; PMID 37334223 (cited; identity checked, not read)
- locator hint: PMID 41409370 Results (heterogeneity, definitions); PMID 37334223 case report
- class: transfer from other system
