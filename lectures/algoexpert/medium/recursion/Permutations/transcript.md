# AlgoExpert · Permutations

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Permutations (0:00) — `slides/01.png`

Let's solve Permutations, a medium recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. All orderings of a list of distinct ints (empty input yields an empty list).

## 3. Intuition (0:19) — `slides/03.png`

Build permutations by swapping each remaining element into the current position.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Inserting each element into every position of smaller permutations works but copies a lot. Swap-based backtracking fixes one position at a time in place. Either way the output itself is n factorial.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, recurse on index i. Second, swap each later element into position i. Third, recurse, then swap back.

## 6. Worked example (0:48) — `slides/06.png`

All positions are fixed, so we record 1, 2, 3.

## 7. Worked example (0:53) — `slides/07.png`

All positions are fixed, so we record 1, 3, 2.

## 8. Worked example (0:58) — `slides/08.png`

All positions are fixed, so we record 2, 1, 3.

## 9. Worked example (1:03) — `slides/09.png`

All positions are fixed, so we record 2, 3, 1.

## 10. Worked example (1:08) — `slides/10.png`

All positions are fixed, so we record 3, 2, 1.

## 11. Worked example (1:12) — `slides/11.png`

All positions are fixed, so we record 3, 1, 2.

## 12. Java solution (1:17) — `slides/12.png`

If the array is non-empty we call permute from zero. At the last index we record a copy. Otherwise, for each j from i, swap i and j, recurse, and swap back.

## 13. Complexity (1:30) — `slides/13.png`

Time is O of n times n factorial. Space is O of n times n factorial.

## 14. Edge cases & pitfalls (1:36) — `slides/14.png`

Always undo the swap after recursing, and copy the array when you record it, or every result ends up the same list.

## 15. Interview tips & follow-ups (1:44) — `slides/15.png`

With duplicates, skip values already used at a position. Next permutation is a common sibling question.

## 16. Recap (1:52) — `slides/16.png`

To recap Permutations: Build permutations by swapping each remaining element into the current position. Try re-implementing it from scratch without looking.
