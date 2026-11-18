# I1 predictions written BEFORE the class scan was run (SCI, 2026-11-16 ~17:35Z; model = rebound_oscillator.py with the fitted baseline; hypothesis generator, not evidence)
Rule: sign of the change of median interval (INT) and median duration (DUR) relative to the fitted baseline, at the largest magnitude of each class. "~0" = within 15%.
| id | mechanism class (what changes in the model) | predicted INT | predicted DUR | note |
|---|---|---|---|---|
| C1 | T-type-like blockade (J_T x0.5) | up | ~0 | the trigger half of the hypothesis |
| C2 | NMDAR-active, strong (J_N x0.85) | up | down | both change: the clean dissociation will NOT hold |
| C3 | GABA-A positive modulation (pam 1.0: tonic and phasic scaled together) | down (rate up) | ~0 or up | rebound gate raised: aggravation predicted |
| C4 | KCC2 enhancement (tau_c x0.5) | up | down | chloride recovers faster, inhibition stays strong |
| C5 | KCC2 inhibition or NKCC1 loading (tau_c x2) | down | up | the mirror of C4 |
| C6 | adenosine augmentation (J_a x1.4) | up | ~0 | slow variable acting on the interval |
| C7 | HCN blockade (hcn_block 1.0) | up | ~0 | removes a depolarising tonic share |
| C8 | presynaptic brake, NPY-like (brake 0.10) | up, with a cliff to silence | down | I3 |
| C9 | persistent sodium-type reduction (sigma x0.7) | up | ~0 | noise-driven ignition |
| C10 | tonic GABA increase only (tonic_gaba x1.5) | up | ~0 | against C3: tonic vs phasic |
Surprising prediction fixed in advance: a threshold exists where a change of one parameter by less than 30% takes the network from bursting (rate > 0.5/min) to silent; the parameter(s) with that property will be reported by the one-at-a-time scan, not chosen afterwards.
