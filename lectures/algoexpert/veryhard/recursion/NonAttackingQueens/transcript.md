# AlgoExpert · Non Attacking Queens

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Non Attacking Queens (0:00) — `slides/01.png`

Let's solve Non Attacking Queens, a very hard recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Number of ways to place n queens on an n x n board with no two attacking. Backtracking with column or diagonal bitmasks.

## 3. Intuition (0:22) — `slides/03.png`

Place one queen per row; track used columns and both diagonals for constant-time checks.

## 4. Brute force vs optimal (0:28) — `slides/04.png`

Trying every placement is hopeless. Backtracking one row at a time with blocked sets prunes hard; bitmasks make it very fast.

## 5. Approach (0:37) — `slides/05.png`

Step by step. First, recurse row by row. Second, try each free column. Third, mark column and diagonals. Fourth, count full placements.

## 6. Worked example (0:50) — `slides/06.png`

Place one queen per row. Three bitmasks track blocked columns and both diagonals.

## 7. Worked example (0:57) — `slides/07.png`

Free positions are the bits not blocked. Take each lowest set bit, recurse, shifting the diagonal masks for the next row.

## 8. Worked example (1:05) — `slides/08.png`

For four queens there are two solutions; for eight, ninety-two.

## 9. Java solution (1:10) — `slides/09.png`

Place returns one when all rows are filled. Otherwise it loops over free bits, recursing with the column added and diagonals shifted left and right.

## 10. Complexity (1:20) — `slides/10.png`

Time is O of n factorial. Space is O of n.

## 11. Edge cases & pitfalls (1:25) — `slides/11.png`

Mask to n bits after shifting.

## 12. Interview tips & follow-ups (1:29) — `slides/12.png`

Mirror symmetry halves the work.

## 13. Recap (1:32) — `slides/13.png`

To recap Non Attacking Queens: Place one queen per row; track used columns and both diagonals for constant-time checks. Try re-implementing it from scratch without looking.
