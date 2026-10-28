# AlgoExpert · Spiral Traverse

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Spiral Traverse (0:00) — `slides/01.png`

Let's solve Spiral Traverse, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Read a (possibly non-square) matrix in clockwise spiral order.

## 3. Intuition (0:18) — `slides/03.png`

Peel the matrix layer by layer: top row, right column, bottom row, left column, then shrink.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

One approach walks with a direction and turns when it hits a visited cell, which needs a visited matrix. Shrinking four boundaries layer by layer avoids that extra memory.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, keep four boundaries. Second, walk the perimeter. Third, guard single rows or columns. Fourth, shrink and repeat.

## 6. Worked example (0:49) — `slides/06.png`

Layer 0, top row: we add 1, 2, 3, 4.

## 7. Worked example (0:54) — `slides/07.png`

Layer 0, right col, bottom row, left col: we add 5, 6, 7, 8, 9, 10, 11, 12.

## 8. Worked example (1:02) — `slides/08.png`

Layer 1, top row: we add 13, 14.

## 9. Worked example (1:06) — `slides/09.png`

Layer 1, right col, bottom row, left col: we add 15, 16.

## 10. Java solution (1:12) — `slides/10.png`

We keep start and end row and column. Each loop walks the top row, the right column, then the bottom row and left column with guards for single rows or columns, and finally shrinks all four boundaries.

## 11. Complexity (1:24) — `slides/11.png`

Time is O of n cells. Space is O of n output.

## 12. Edge cases & pitfalls (1:29) — `slides/12.png`

The trickiest cases are a single remaining row or column, where the bottom and left passes would repeat cells. The guards sr less than er and sc less than ec prevent that.

## 13. Interview tips & follow-ups (1:40) — `slides/13.png`

A natural follow-up is the reverse: filling an n by n matrix with one to n squared in spiral order.

## 14. Recap (1:47) — `slides/14.png`

To recap Spiral Traverse: Peel the matrix layer by layer: top row, right column, bottom row, left column, then shrink. Try re-implementing it from scratch without looking.
