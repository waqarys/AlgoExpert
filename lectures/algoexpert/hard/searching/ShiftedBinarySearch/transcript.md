# AlgoExpert · Shifted Binary Search

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Shifted Binary Search (0:00) — `slides/01.png`

Let's solve Shifted Binary Search, a hard searching problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Find target's index in a sorted array of distinct ints rotated by some amount; -1 if absent.

## 3. Intuition (0:20) — `slides/03.png`

In a rotated sorted array, one half is always sorted; check if the target lies in it.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

A linear scan ignores sorting. At every mid, one half is sorted; check if the target lies within that half and discard the other, log n.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, find the middle. Second, decide which half is sorted. Third, check whether the target is in that half. Fourth, recurse into the right half.

## 6. Worked example (0:49) — `slides/06.png`

Mid is 73. The left half is sorted, and 33 is not within it, so go right.

## 7. Worked example (0:56) — `slides/07.png`

Mid is 21. The left half is sorted, and 33 is not within it, so go right.

## 8. Worked example (1:03) — `slides/08.png`

Mid is 33: found it at index 8.

## 9. Java solution (1:07) — `slides/09.png`

While lo is at most hi: return on a match; if the left half is sorted, go left when the target is in its range, else right; otherwise mirror for the right half.

## 10. Complexity (1:17) — `slides/10.png`

Time is O of log n. Space is constant.

## 11. Edge cases & pitfalls (1:21) — `slides/11.png`

Use less-or-equal when deciding which half is sorted. Duplicates can force linear time.

## 12. Interview tips & follow-ups (1:28) — `slides/12.png`

With duplicates, worst case degrades to linear.

## 13. Recap (1:32) — `slides/13.png`

To recap Shifted Binary Search: In a rotated sorted array, one half is always sorted; check if the target lies in it. Try re-implementing it from scratch without looking.
