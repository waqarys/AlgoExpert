# AlgoExpert · Three Number Sum

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Three Number Sum (0:00) — `slides/01.png`

Let's solve Three Number Sum, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. All triplets of distinct integers summing to target, each triplet ascending and the list sorted. Sort then sweep with two pointers.

## 3. Intuition (0:21) — `slides/03.png`

Fix one number, then find pairs in the sorted remainder with two pointers.

## 4. Brute force vs optimal (0:27) — `slides/04.png`

Three nested loops are cubic. Fixing one number and using a hash set for the other two is quadratic with extra memory. Sorting, fixing one number, and closing in with two pointers is quadratic with constant extra space, and naturally sorted output.

## 5. Approach (0:43) — `slides/05.png`

Step by step. First, sort the array. Second, for each index, set left and right pointers after it. Third, move them based on the current sum. Fourth, record exact matches.

## 6. Worked example (0:57) — `slides/06.png`

With -8 fixed, -6 plus 12 gives -2. Too small, so move left forward.

## 7. Worked example (1:05) — `slides/07.png`

With -8 fixed, 1 plus 12 gives 5. Too big, so move right back.

## 8. Worked example (1:12) — `slides/08.png`

With -8 fixed, 1 plus 6 gives -1. Too small, so move left forward.

## 9. Worked example (1:19) — `slides/09.png`

With -8 fixed, 2 plus 6 gives 0. That's a match; record it and move both pointers.

## 10. Worked example (1:26) — `slides/10.png`

With -8 fixed, 3 plus 5 gives 0. That's a match; record it and move both pointers.

## 11. Worked example (1:34) — `slides/11.png`

With -6 fixed, 1 plus 12 gives 7. Too big, so move right back.

## 12. Java solution (1:41) — `slides/12.png`

We sort, then for each index i set l right after it and r at the end. We compute the sum; on a match we record and move both, otherwise move l forward if too small or r back if too big.

## 13. Complexity (1:52) — `slides/13.png`

Time is O of n squared. Space is O of n.

## 14. Edge cases & pitfalls (1:58) — `slides/14.png`

This problem has distinct values. With duplicates you'd skip repeated values to avoid duplicate triplets. After a match, move both pointers.

## 15. Interview tips & follow-ups (2:08) — `slides/15.png`

Mention that this generalises to k-sum, and a common follow-up is the closest three-sum.

## 16. Recap (2:14) — `slides/16.png`

To recap Three Number Sum: Fix one number, then find pairs in the sorted remainder with two pointers. Try re-implementing it from scratch without looking.
