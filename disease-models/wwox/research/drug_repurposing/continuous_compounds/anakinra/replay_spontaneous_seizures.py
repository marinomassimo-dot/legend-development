#!/usr/bin/env python3
"""Replay aggregate denominators and consistency checks from cited studies."""

from fractions import Fraction
from math import comb


def fisher_two_sided(events_a, total_a, events_b, total_b):
    events = events_a + events_b
    observed = comb(total_a, events_a) * comb(total_b, events_b)
    weights = (
        comb(total_a, a) * comb(total_b, events - a)
        for a in range(max(0, events - total_b), min(events, total_a) + 1)
    )
    return Fraction(
        sum(weight for weight in weights if weight <= observed),
        comb(total_a + total_b, events),
    )


def percent_candidates(target, denominators):
    return [
        (events, count)
        for count in denominators
        for events in range(count + 1)
        if abs(Fraction(100 * events, count) - target) < Fraction(1, 2)
    ]


def print_pair_candidates(label, percentage_a, percentage_b, denominators):
    for a in percent_candidates(percentage_a, denominators):
        for b in percent_candidates(percentage_b, denominators):
            description = f"{a[0]}/{a[1]} vs {b[0]}/{b[1]}"
            probability = fisher_two_sided(*a, *b)
            print(f"{label}\t{float(probability):.5f}\tFisher p\t{description}")


def print_video_2023():
    # Zubareva §2.1 (observed) and §4.2 (allocated), anakinra versus untreated TLE.
    treated_events, treated_observed, treated_allocated = 6, 11, 16
    control_events, control_observed, control_allocated = 9, 15, 19
    observed_difference = Fraction(treated_events, treated_observed) - Fraction(
        control_events, control_observed
    )
    worst = Fraction(treated_events, treated_allocated) - Fraction(
        control_events + control_allocated - control_observed, control_allocated
    )
    best = Fraction(
        treated_events + treated_allocated - treated_observed, treated_allocated
    ) - Fraction(control_events, control_allocated)
    print(f"video_observed_difference\t{100 * float(observed_difference):.2f}\tpp\t6/11 vs 9/15")
    print(f"video_allocation_lower\t{100 * float(worst):.2f}\tpp\t6/16 vs 13/19")
    print(f"video_allocation_upper\t{100 * float(best):.2f}\tpp\t11/16 vs 9/19")


def main():
    print("check\tvalue\tunit\tinput")
    print_video_2023()
    # Taraschenko §3.1, screened and selected animals, with 12+8 randomized.
    print(f"anti_nmdar_screen_excluded\t{100 * (6 + 5) / 31:.2f}\tpercent\t(6 + 5)/31")
    # Semple Fig. 6B graph estimates and Fig. 7B caption percentages and n bounds.
    print_pair_candidates("semple_fig6b_compatible", 95, 87, range(15, 20))
    print_pair_candidates("semple_fig7b_caption_range", 58, 21, range(15, 20))
    print_pair_candidates("semple_fig7b_extend_to_14", 58, 21, range(14, 20))


if __name__ == "__main__":
    main()
