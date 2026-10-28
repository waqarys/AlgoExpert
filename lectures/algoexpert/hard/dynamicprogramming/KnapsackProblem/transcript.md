# AlgoExpert · Knapsack Problem

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Knapsack Problem (0:00) — `slides/01.png`

Let's solve Knapsack Problem, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Items are value, weight . Returns maxValue , item indices .

## 3. Intuition (0:20) — `slides/03.png`

Each item is taken or skipped; a table over items and capacities captures every choice.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

Trying all subsets is exponential. A table over items and capacity is n times C, pseudo-polynomial, and backtracking recovers the items.

## 5. Approach (0:36) — `slides/05.png`

Step by step. First, row per item, column per capacity. Second, skip copies the row above. Third, take adds the value to the row above at capacity minus weight. Fourth, backtrack to list items.

## 6. Worked example (0:52) — `slides/06.png`

Add the item worth 1 weighing 2. Green cells improved by taking it. Best for capacity ten is now 1.

## 7. Worked example (1:01) — `slides/07.png`

Add the item worth 4 weighing 3. Green cells improved by taking it. Best for capacity ten is now 5.

## 8. Worked example (1:10) — `slides/08.png`

Add the item worth 5 weighing 6. Green cells improved by taking it. Best for capacity ten is now 9.

## 9. Worked example (1:19) — `slides/09.png`

Add the item worth 6 weighing 7. Green cells improved by taking it. Best for capacity ten is now 10.

## 10. Worked example (1:28) — `slides/10.png`

Backtracking from the bottom-right, the chosen items are [1, 3], worth 10.

## 11. Java solution (1:34) — `slides/11.png`

Dp of i, c is either skipping the item, or taking it if it fits. Then from the bottom-right, a change between rows means the item was taken.

## 12. Complexity (1:44) — `slides/12.png`

Time is O of n times c. Space is O of n times c.

## 13. Edge cases & pitfalls (1:48) — `slides/13.png`

This is pseudo-polynomial. The one-dimensional version must iterate capacity downward.

## 14. Interview tips & follow-ups (1:55) — `slides/14.png`

Contrast zero-one with unbounded knapsack.

## 15. Recap (1:59) — `slides/15.png`

To recap Knapsack Problem: Each item is taken or skipped; a table over items and capacities captures every choice. Try re-implementing it from scratch without looking.
