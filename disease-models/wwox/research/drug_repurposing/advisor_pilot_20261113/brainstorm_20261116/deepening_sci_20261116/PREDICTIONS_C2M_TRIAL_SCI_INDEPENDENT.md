# Independent forecast of the class-to-member specification trial (SCI, 2026-11-17, host clock before 08:55Z; written and hashed BEFORE the run; probabilities mine, not evidence)

**What I know when writing:** I know the T7 result (zinc as an inhibitory ion was named in 0 of 40 final statements; v4 run B's enumeration block named zinc once as a supply item) and I know the atom; I have scored my own set-3 forecast; I have read the C2M materials (`C2M_TRIAL_FOR_FORECASTER.md`, sha256 9bb571200596becc7c00ef1fe62c87a38456f08790a89b9936357637e654bc9d: the prompt template, inputs A and B, the scoring definitions). I have no other information about the trial and I have not seen any output. I also know from the field that zinc is a classical inhibitor of cyclases and a known antidiarrhoeal ion, so I expect a tool-free model to know it too.
**Reading of the prompt:** each delegate is asked, for each lever class of the enumeration, for specific members with a direction (raises or lowers) and a mechanism, 'include members that lower'. Input A names the metal-ion class as 'Mg2+/Mn2+ metal site and metal identity'; input B names it as 'Divalent metal: Mg2+ versus Mn2+' and separately lists 'Vitamin A, zinc' as a supply item.

## Predictions (STRICT = zinc listed as a lowering member of the metal-ion class; LOOSE = any ion other than Mg2+ and Mn2+ listed as lowering)
| id | statement | P |
|---|---|---|
| i-1 | STRICT in at least one of A1, A2 | **0.80** |
| i-2 | STRICT in both A1 and A2 | **0.55** |
| i-3 | exactly one of A1, A2 is STRICT | 0.25 (consistent with the two rows above) |
| ii-1 | LOOSE in at least one of A1, A2 (any ion other than Mg2+ and Mn2+ listed as lowering; my expected members: Ca2+, Zn2+, Cu2+, Cd2+ or Co2+) | **0.93** |
| ii-2 | LOOSE in both A1 and A2 | 0.80 |
| iii-1 | B1 keeps zinc with direction 'lowers' (anywhere in its table) | **0.65** |
| iii-2 | B1 lists zinc, direction 'raises' or 'supply' only | 0.20 |
| iii-3 | B1 does not list zinc at all | 0.15 |
| x-1 | in A, Mg2+ and Mn2+ both given the direction 'raises' in both runs | 0.90 |
| x-2 | the final 'LOWERING MEMBERS:' line includes zinc, given that zinc is listed as lowering | 0.95 |
| x-3 | number of members listed for the metal-ion class per run (median, central range) | 5 (3 to 8) |
| x-4 | number of those listed as lowering per run (median, central range) | 2 (1 to 4) |
## What would change my reading
If zinc is listed as lowering in A, the class-to-member step reaches the atom the enumeration and the corpus step lost, and the failure of T7 was a specification failure (the class was named, the member was not); since zinc was a tuned-on case and is in the model's own memory, I would read that as 'the step recovers what the model knows when asked for members', not as a new capability on a target the model does not know. If zinc is not listed in A despite the explicit 'lowers' instruction, then the T7 miss was not only selection but also a limit in the model's tool-free reach for ion inhibitors. Scored literally by HE and, independently, by IT.
