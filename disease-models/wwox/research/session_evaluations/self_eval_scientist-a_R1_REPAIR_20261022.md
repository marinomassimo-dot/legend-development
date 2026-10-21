# Self-evaluation — scientist-a, R1 repair after the blind audit, 2026-10-22

Verdict: 19 of 95 triples (20 percent counting UNVERIFIABLE; 15 OVERSHOOT, 2 UNDERSHOOT, 2 UNVERIFIABLE) were adverse. All repaired in six manifests with declared `contradicts_locator`; `locator_contradiction_audit.py --working-tree --fail-on-undeclared` clean; the six manifests PASS. **The repairs are the repairer's own and are unaudited.**

Why it happened (the shape named in D-22: asserting what a source does not say without cross-reading the surfaces that might say it): **not applied, and catchable** in most cases. 31402619 entry 1: the adjacent sentence (176 mRNAs read as altered synthesis) and Fig 1B sat in the same paragraph I quoted from; entry 3: a search of the supplementary captions and Figure 9 would have corrected the blot inventory; 42157447 entry 16: I wrote a negative about the whole paper without opening Figure 7; 38378758 entries 7, 15: I dropped the authors' hedges and wrote "only compound". Partly not catchable by the method I used: absence claims cannot be carried by a quote at all, and my manifests had no slot for 'established by search on these surfaces'. The text-versus-panel conflicts I recorded (r 0.9448, N = 3) were confirmed by the audit: those were caught.

Micro-upgrade: an absence claim is now written in the proposition as 'ABSENCE CLAIM, established by search of <surfaces>, not carried by this quote', with unopened surfaces named; and a 'hedge check' before closing a manifest (does the proposition contain a word stronger than the quote's own hedge: likely, suggests, substantial, globally). Both are reader practice, not a gate.

Also repaired: an ellipsis-stitched quotation in my own note (PB-2 row), a rule this repository already has.

```
ATTRIBUTION_CENSUS
incidents: 8
machine: 0   blind_auditor: 6   peer: 0   self: 2
severity_high: 6   of which self: 0
undetected_known: 19
```

Incidents: one per paper-level class (six audited papers carried adverse triples: 31402619, 42157447, 38731820, 32023956, 38378758, 42875792), plus the ellipsis quotation and the manifest-format check that caught two undeclared appended resolutions (self, via the contradiction screen, which is a machine; counted as self because I ran the screen on purpose). `undetected_known` is the 19 adverse triples, found later and attributed back to wave R1.
