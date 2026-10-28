# AlgoExpert · Non Attacking Queens

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Non Attacking Queens (0:00) — `slides/01.png`

Let's solve Non Attacking Queens, a very hard recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Number of ways to place n queens on an n x n board with no two attacking. Backtracking with column or diagonal bitmasks.

## 3. Intuition (0:22) — `slides/03.png`

Place one queen per row; track used columns and both diagonals for constant-time checks.

## 4. Approach (0:28) — `slides/04.png`

Step by step. First, recurse row by row. Second, try each free column. Third, mark column and diagonals. Fourth, count full placements.

## 5. Java solution (0:41) — `slides/05.png`

Here's the Java solution, starting with non attacking queens. It follows the steps we just described.

## 6. Complexity (0:49) — `slides/06.png`

Time is O of n factorial. Space is O of n.

## 7. Recap (0:54) — `slides/07.png`

To recap Non Attacking Queens: Place one queen per row; track used columns and both diagonals for constant-time checks. Try re-implementing it from scratch without looking.
