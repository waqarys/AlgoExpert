# AlgoExpert · Monotonic Array

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Monotonic Array (0:00) — `slides/01.png`

Let's solve Monotonic Array, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Is the array entirely non-increasing or entirely non-decreasing?

## 3. Intuition (0:18) — `slides/03.png`

An array is monotonic if it never goes both up and down.

## 4. Brute force vs optimal (0:22) — `slides/04.png`

A common first attempt finds the direction from the first unequal pair, then checks everything again. Tracking two flags, can-still-be-increasing and can-still-be-decreasing, does it in a single pass.

## 5. Approach (0:34) — `slides/05.png`

Step by step. First, track two flags, non-increasing and non-decreasing. Second, clear the opposite flag on each rise or fall. Third, return true if either flag survives.

## 6. Worked example (0:48) — `slides/06.png`

From -1 to -5: it drops, so the array can't be non-decreasing.

## 7. Worked example (0:54) — `slides/07.png`

From -10 to -1100: it drops, so the array can't be non-decreasing.

## 8. Worked example (1:00) — `slides/08.png`

From -1100 to -1100: equal values don't break either direction.

## 9. Worked example (1:07) — `slides/09.png`

From -1102 to -9001: it drops, so the array can't be non-decreasing.

## 10. Java solution (1:14) — `slides/10.png`

We keep increasing and decreasing flags. Any drop clears increasing, any rise clears decreasing, and we return whether either survives.

## 11. Complexity (1:23) — `slides/11.png`

Time is O of n. Space is constant.

## 12. Edge cases & pitfalls (1:27) — `slides/12.png`

Empty and single-element arrays are monotonic, equal neighbours are fine, and leading equal values don't fix a direction prematurely.

## 13. Interview tips & follow-ups (1:35) — `slides/13.png`

You can return early once both flags are false. A follow-up asks for strict monotonicity.

## 14. Recap (1:42) — `slides/14.png`

To recap Monotonic Array: An array is monotonic if it never goes both up and down. Try re-implementing it from scratch without looking.
