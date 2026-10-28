# AlgoExpert · Square Of Zeroes

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Square Of Zeroes (0:00) — `slides/01.png`

Let's solve Square Of Zeroes, a very hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Does the 0 or 1 matrix contain a square (side over equals 2) whose border is entirely 0s? Precompute consecutive zeros to the right and downward per cell.

## 3. Intuition (0:25) — `slides/03.png`

Precompute zeros to the right and below each cell, so each square border is checked in constant time.

## 4. Brute force vs optimal (0:31) — `slides/04.png`

Checking every border cell by cell is n to the fourth. Precomputing zero runs right and down makes each square a constant-time check, n cubed overall.

## 5. Approach (0:41) — `slides/05.png`

Step by step. First, build right and down zero counts. Second, for each top-left and size. Third, check the four sides with the counts. Fourth, return true on success.

## 6. Worked example (0:55) — `slides/06.png`

Is there a square, at least two by two, whose border is entirely zeros?

## 7. Worked example (1:01) — `slides/07.png`

Precompute how many consecutive zeros extend right and down from every cell.

## 8. Worked example (1:06) — `slides/08.png`

For each top-left corner and size, four lookups check all four sides. Here, the five-by-five square from row one, column zero works.

## 9. Java solution (1:16) — `slides/09.png`

We fill right and down from the bottom-right, then for each corner and size check right and down at the top-left, right at the bottom-left, and down at the top-right.

## 10. Complexity (1:24) — `slides/10.png`

Time is O of n cubed. Space is O of n squared.

## 11. Edge cases & pitfalls (1:30) — `slides/11.png`

Squares must be at least two by two.

## 12. Interview tips & follow-ups (1:33) — `slides/12.png`

Spell out the four checks: top, left, bottom, right.

## 13. Recap (1:38) — `slides/13.png`

To recap Square Of Zeroes: Precompute zeros to the right and below each cell, so each square border is checked in constant time. Try re-implementing it from scratch without looking.
