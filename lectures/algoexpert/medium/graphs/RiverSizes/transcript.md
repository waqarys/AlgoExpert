# AlgoExpert · River Sizes

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. River Sizes (0:00) — `slides/01.png`

Let's solve River Sizes, a medium graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. In a 0 or 1 matrix, sizes of all 4-directionally connected groups of 1s (any order).

## 3. Intuition (0:19) — `slides/03.png`

Each river is a connected component of ones; flood-fill to measure it.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Exploring from every one without remembering visits repeats work. With a visited matrix, each cell is processed once, linear in the grid size.

## 5. Approach (0:34) — `slides/05.png`

Step by step. First, scan every cell. Second, on an unvisited one, DFS or BFS to count its size. Third, mark visited cells.

## 6. Worked example (0:47) — `slides/06.png`

Scanning reaches an unvisited one at row 0, column 0. A flood fill finds a river of size 2.

## 7. Worked example (0:54) — `slides/07.png`

Scanning reaches an unvisited one at row 0, column 3. A flood fill finds a river of size 1.

## 8. Worked example (1:02) — `slides/08.png`

Scanning reaches an unvisited one at row 1, column 2. A flood fill finds a river of size 5.

## 9. Worked example (1:10) — `slides/09.png`

Scanning reaches an unvisited one at row 2, column 4. A flood fill finds a river of size 2.

## 10. Worked example (1:18) — `slides/10.png`

Scanning reaches an unvisited one at row 3, column 0. A flood fill finds a river of size 2.

## 11. Java solution (1:25) — `slides/11.png`

We scan every cell. On an unvisited one, we start a stack-based flood fill, counting popped cells and pushing unvisited neighbouring ones, then record the size.

## 12. Complexity (1:36) — `slides/12.png`

Time is O of w times h. Space is O of w times h.

## 13. Edge cases & pitfalls (1:41) — `slides/13.png`

Mark cells visited when you push them, otherwise the same cell can be pushed twice and counted twice.

## 14. Interview tips & follow-ups (1:47) — `slides/14.png`

Union-find is an alternative. The hard follow-up flips one zero to maximise an island.

## 15. Recap (1:54) — `slides/15.png`

To recap River Sizes: Each river is a connected component of ones; flood-fill to measure it. Try re-implementing it from scratch without looking.
