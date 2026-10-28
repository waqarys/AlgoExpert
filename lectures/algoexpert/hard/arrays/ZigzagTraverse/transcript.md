# AlgoExpert · Zigzag Traverse

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Zigzag Traverse (0:00) — `slides/01.png`

Let's solve Zigzag Traverse, a hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Read a matrix along anti-diagonals in zigzag, starting at top-left and moving down first (odd diagonals are read bottom-to-top, even ones top-to-bottom).

## 3. Intuition (0:22) — `slides/03.png`

Walk diagonals, bouncing off the edges and flipping direction each time.

## 4. Brute force vs optimal (0:27) — `slides/04.png`

Simulating with direction flags works but is fiddly at the edges. Iterating anti-diagonals, where row plus column is constant, and alternating direction is cleaner and still visits each cell once.

## 5. Approach (0:39) — `slides/05.png`

Step by step. First, start at top-left heading down. Second, move diagonally. Third, at an edge, step along it and flip direction. Fourth, stop after every cell.

## 6. Worked example (0:54) — `slides/06.png`

Diagonal 0 goes down: 1.

## 7. Worked example (0:58) — `slides/07.png`

Diagonal 1 goes up: 2, 3.

## 8. Worked example (1:02) — `slides/08.png`

Diagonal 2 goes down: 4, 5, 6.

## 9. Worked example (1:06) — `slides/09.png`

Diagonal 3 goes up: 7, 8, 9, 10.

## 10. Worked example (1:11) — `slides/10.png`

Diagonal 5 goes up: 14, 15.

## 11. Worked example (1:15) — `slides/11.png`

Diagonal 6 goes down: 16.

## 12. Java solution (1:19) — `slides/12.png`

For each diagonal d, the rows run from max zero, d minus C plus one, to min d, R minus one. Even diagonals go down, odd go up, reading column d minus r.

## 13. Complexity (1:31) — `slides/13.png`

Time is O of n. Space is O of n.

## 14. Edge cases & pitfalls (1:34) — `slides/14.png`

Clamp the row range per diagonal so it works for non-square matrices.

## 15. Interview tips & follow-ups (1:39) — `slides/15.png`

Draw the diagonals first; the indexing follows.

## 16. Recap (1:43) — `slides/16.png`

To recap Zigzag Traverse: Walk diagonals, bouncing off the edges and flipping direction each time. Try re-implementing it from scratch without looking.
