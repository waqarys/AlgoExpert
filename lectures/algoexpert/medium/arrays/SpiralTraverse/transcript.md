# AlgoExpert · Spiral Traverse

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Spiral Traverse (0:00) — `slides/01.png`

Let's solve Spiral Traverse, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Read a (possibly non-square) matrix in clockwise spiral order.

## 3. Intuition (0:18) — `slides/03.png`

Peel the matrix layer by layer: top row, right column, bottom row, left column, then shrink.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, keep four boundaries. Second, walk the perimeter. Third, guard single rows or columns. Fourth, shrink and repeat.

## 5. Java solution (0:38) — `slides/05.png`

Here's the Java solution, starting with spiral traverse. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is O of n cells. Space is O of n output.

## 7. Recap (0:50) — `slides/07.png`

To recap Spiral Traverse: Peel the matrix layer by layer: top row, right column, bottom row, left column, then shrink. Try re-implementing it from scratch without looking.
