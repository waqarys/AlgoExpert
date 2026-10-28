# AlgoExpert · Rectangle Mania

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Rectangle Mania (0:00) — `slides/01.png`

Let's solve Rectangle Mania, a very hard graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Count axis-aligned rectangles whose four corners are all in the point set. Each pair forming a strictly up-right diagonal identifies one rectangle exactly once.

## 3. Intuition (0:23) — `slides/03.png`

Two points forming an up-right diagonal define a rectangle if the other two corners exist.

## 4. Brute force vs optimal (0:29) — `slides/04.png`

Choosing four points is n to the fourth. Using strictly up-right pairs as diagonals counts each rectangle once in quadratic time.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, put points in a set. Second, for each pair up and to the right. Third, check the other two corners. Fourth, count.

## 6. Worked example (0:51) — `slides/06.png`

Count axis-aligned rectangles formed by these points.

## 7. Worked example (0:55) — `slides/07.png`

Treat each pair where the second is strictly up and right of the first as a diagonal, and check the other corners.

## 8. Worked example (1:02) — `slides/08.png`

Each rectangle is counted exactly once this way: 6 in total.

## 9. Java solution (1:07) — `slides/09.png`

We store points, and for each ordered pair with b up and right of a, count when both other corners exist.

## 10. Complexity (1:14) — `slides/10.png`

Time is O of n squared. Space is O of n.

## 11. Edge cases & pitfalls (1:19) — `slides/11.png`

Requiring up-right ordering is what avoids counting each rectangle four times.

## 12. Interview tips & follow-ups (1:24) — `slides/12.png`

Contrast with count squares, which allows tilts.

## 13. Recap (1:28) — `slides/13.png`

To recap Rectangle Mania: Two points forming an up-right diagonal define a rectangle if the other two corners exist. Try re-implementing it from scratch without looking.
