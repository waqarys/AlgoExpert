# AlgoExpert · Zigzag Traverse

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Zigzag Traverse (0:00) — `slides/01.png`

Let's solve Zigzag Traverse, a hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Read a matrix along anti-diagonals in zigzag, starting at top-left and moving down first (odd diagonals are read bottom-to-top, even ones top-to-bottom).

## 3. Intuition (0:22) — `slides/03.png`

Walk diagonals, bouncing off the edges and flipping direction each time.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, start at top-left heading down. Second, move diagonally. Third, at an edge, step along it and flip direction. Fourth, stop after every cell.

## 5. Java solution (0:42) — `slides/05.png`

Here's the Java solution, starting with zigzag traverse. It follows the steps we just described.

## 6. Complexity (0:49) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:53) — `slides/07.png`

To recap Zigzag Traverse: Walk diagonals, bouncing off the edges and flipping direction each time. Try re-implementing it from scratch without looking.
