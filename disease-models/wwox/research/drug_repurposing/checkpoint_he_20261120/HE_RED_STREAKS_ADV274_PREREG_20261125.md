# ADV-274 preregistration: red streaks on main and what the landing selection would have named (HE, 2026-11-25 ~10:00Z)

Written and committed before any failing-suite annotation of this set was read.

**Seen before writing** (so these are not predictions): the conclusions of the runs from #2246 to #2432, hence the streak boundaries; and, from HE checkpoints N to P and `HE_RED_MAIN_ADV237_20261125.md`, the causes of some of these reds (#2322, #2353, #2404). The current path rules were partly written from those reds.

## Set
Gate runs on `main`, #2340 to #2432 (93 runs). A run not concluded at the single read is excluded and counted.

## Unit
A **red streak**: consecutive concluded-failure runs, ended by a concluded success; unfinished and cancelled runs neither end nor extend it. A streak counts when at least one of its red runs is in the set; its first red run may lie before #2340. A failing suite that appears inside a streak and was not failing at its first red run is a **later cause**, counted with the streaks as a cause but not as a streak.

## Runs red for a reason outside the commit
A failed run with no `release regression` annotation, or whose failed step is a runner, setup, dependency, rate-limit or timeout step, or whose failing suite passes locally on the same tree for an environmental reason, is excluded from the cause count and listed with its reason.

## Change replayed
The diff from the commit of the preceding gate run to the commit of the first run showing the cause (one run per push). A cause is **named** when the selection holds the failing suite file; a class entry names it only if the failing test is in that class. Two readings:
1. rules **in force** when the red landed (out-of-sample);
2. rules **current** at `071ad65e4` (partly in-sample), then after any rule added here ("before / after").

## Duration
Push time of a streak's first red run to push time of the next green run. An open streak is censored and shown apart. Median over the closed streaks from #2246 to #2432.

## Reading budget
One run list (already cached, two requests); annotations only for the first red run of each streak, its last red run, and intermediate runs by bisection when the two differ. At most 30 requests.

## Expected
- Causes in the set: 4 to 6.
- Named by the rules in force at the time: at most 2.
- Named by the current rules: all but 0 to 2.

## What changes the plan
- Most escapes in one class: one rule for that class.
- Escapes that no path selects cheaply (long suites): no rule; report the class to ADV.
- A rule is added only for an escape class with two or more cases, or one case with a cheap trigger.
