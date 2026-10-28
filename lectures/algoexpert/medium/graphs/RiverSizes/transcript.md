# AlgoExpert · River Sizes

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. River Sizes (0:00) — `slides/01.png`

Let's solve River Sizes, a medium graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. In a 0 or 1 matrix, sizes of all 4-directionally connected groups of 1s (any order).

## 3. Intuition (0:19) — `slides/03.png`

Each river is a connected component of ones; flood-fill to measure it.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, scan every cell. Second, on an unvisited one, DFS or BFS to count its size. Third, mark visited cells.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with river sizes. It follows the steps we just described.

## 6. Complexity (0:44) — `slides/06.png`

Time is O of w times h. Space is O of w times h.

## 7. Recap (0:49) — `slides/07.png`

To recap River Sizes: Each river is a connected component of ones; flood-fill to measure it. Try re-implementing it from scratch without looking.
