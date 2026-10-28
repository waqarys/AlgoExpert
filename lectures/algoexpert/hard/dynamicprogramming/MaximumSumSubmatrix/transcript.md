# AlgoExpert · Maximum Sum Submatrix

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Maximum Sum Submatrix (0:00) — `slides/01.png`

Let's solve Maximum Sum Submatrix, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Largest sum among all size x size square submatrices, using 2D prefix sums.

## 3. Intuition (0:20) — `slides/03.png`

Two-dimensional prefix sums give any rectangle's sum in constant time.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Summing each block directly costs k squared per block. With two-dimensional prefix sums, each block is four lookups, linear overall.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, build prefix sums. Second, for each bottom-right corner, compute the size by size square sum. Third, track the maximum.

## 6. Worked example (0:47) — `slides/06.png`

Build prefix sums: each cell holds the sum of everything above and to the left.

## 7. Worked example (0:52) — `slides/07.png`

Any k by k sum is four lookups. The best two-by-two block sums to 18.

## 8. Java solution (0:59) — `slides/08.png`

We build the padded prefix table, then for each bottom-right corner compute the block via inclusion-exclusion and keep the max.

## 9. Complexity (1:07) — `slides/09.png`

Time is O of w times h. Space is O of w times h.

## 10. Edge cases & pitfalls (1:12) — `slides/10.png`

Remember to add back the corner you subtracted twice.

## 11. Interview tips & follow-ups (1:16) — `slides/11.png`

For any size, combine column compression with Kadane.

## 12. Recap (1:21) — `slides/12.png`

To recap Maximum Sum Submatrix: Two-dimensional prefix sums give any rectangle's sum in constant time. Try re-implementing it from scratch without looking.
