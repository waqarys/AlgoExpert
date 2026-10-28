# AlgoExpert · Largest Range

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Largest Range (0:00) — `slides/01.png`

Let's solve Largest Range, a hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. lo, hi of the longest run of consecutive integers present in the array.

## 3. Intuition (0:18) — `slides/03.png`

Only start counting at a number that has no predecessor, so each run is scanned exactly once.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Sorting and scanning for consecutive runs is n log n. With a hash set, expand only from numbers with no predecessor; each number is touched at most twice, so it's linear.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, put all numbers in a set. Second, for each number without number minus one, extend upward. Third, track the longest run's bounds.

## 6. Worked example (0:48) — `slides/06.png`

0 has no predecessor, so it starts a range. Walking up gives 0 to 7. The best so far is 0 to 7.

## 7. Worked example (0:58) — `slides/07.png`

10 has no predecessor, so it starts a range. Walking up gives 10 to 12. The best so far is 0 to 7.

## 8. Worked example (1:07) — `slides/08.png`

15 has no predecessor, so it starts a range. Walking up gives 15 to 15. The best so far is 0 to 7.

## 9. Java solution (1:17) — `slides/09.png`

We put everything in a set. For each value with no predecessor, we walk up while the next exists, and keep the widest range.

## 10. Complexity (1:26) — `slides/10.png`

Time is O of n. Space is O of n.

## 11. Edge cases & pitfalls (1:30) — `slides/11.png`

If you expand from every number, it's quadratic. Only start where x minus one is missing.

## 12. Interview tips & follow-ups (1:37) — `slides/12.png`

This is the longest consecutive sequence problem.

## 13. Recap (1:41) — `slides/13.png`

To recap Largest Range: Only start counting at a number that has no predecessor, so each run is scanned exactly once. Try re-implementing it from scratch without looking.
