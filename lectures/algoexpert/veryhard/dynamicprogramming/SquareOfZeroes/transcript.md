# AlgoExpert · Square Of Zeroes

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Square Of Zeroes (0:00) — `slides/01.png`

Let's solve Square Of Zeroes, a very hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Does the 0 or 1 matrix contain a square (side over equals 2) whose border is entirely 0s? Precompute consecutive zeros to the right and downward per cell.

## 3. Intuition (0:25) — `slides/03.png`

Precompute zeros to the right and below each cell, so each square border is checked in constant time.

## 4. Approach (0:31) — `slides/04.png`

Step by step. First, build right and down zero counts. Second, for each top-left and size. Third, check the four sides with the counts. Fourth, return true on success.

## 5. Java solution (0:46) — `slides/05.png`

Here's the Java solution, starting with square of zeroes. It follows the steps we just described.

## 6. Complexity (0:53) — `slides/06.png`

Time is O of n cubed. Space is O of n squared.

## 7. Recap (0:58) — `slides/07.png`

To recap Square Of Zeroes: Precompute zeros to the right and below each cell, so each square border is checked in constant time. Try re-implementing it from scratch without looking.
