# AlgoExpert · Selection Sort

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Selection Sort (0:00) — `slides/01.png`

Let's solve Selection Sort, an easy sorting problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Repeatedly select the minimum of the unsorted suffix and swap it to the front.

## 3. Intuition (0:18) — `slides/03.png`

Repeatedly select the smallest remaining element and swap it into the next position.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Selection sort always does quadratic comparisons, even on sorted input. Its niche is making at most n minus one swaps, which matters when writes are expensive.

## 5. Approach (0:34) — `slides/05.png`

Step by step. First, for each position. Second, find the minimum in the unsorted suffix. Third, swap it into place.

## 6. Worked example (0:45) — `slides/06.png`

The smallest value in the unsorted part is 2, so we swap it into index 0.

## 7. Worked example (0:51) — `slides/07.png`

The smallest value in the unsorted part is 3, so we swap it into index 1.

## 8. Worked example (0:57) — `slides/08.png`

The smallest value in the unsorted part is 5, so we swap it into index 2.

## 9. Worked example (1:02) — `slides/09.png`

The smallest value in the unsorted part is 6, so we swap it into index 4.

## 10. Worked example (1:08) — `slides/10.png`

The smallest value in the unsorted part is 8, so we swap it into index 5.

## 11. Java solution (1:13) — `slides/11.png`

For each starting index we scan the rest to find the smallest index, then swap it into the start position.

## 12. Complexity (1:20) — `slides/12.png`

Time is O of n squared. Space is constant.

## 13. Edge cases & pitfalls (1:25) — `slides/13.png`

Selection sort isn't stable because of its long-distance swaps. Track the index of the minimum, not just its value.

## 14. Interview tips & follow-ups (1:34) — `slides/14.png`

Compare it with bubble and insertion sort, and know how to make it stable by shifting instead of swapping.

## 15. Recap (1:40) — `slides/15.png`

To recap Selection Sort: Repeatedly select the smallest remaining element and swap it into the next position. Try re-implementing it from scratch without looking.
