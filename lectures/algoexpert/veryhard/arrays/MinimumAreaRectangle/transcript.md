# AlgoExpert · Minimum Area Rectangle

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Minimum Area Rectangle (0:00) — `slides/01.png`

Let's solve Minimum Area Rectangle, a very hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Smallest-area axis-aligned rectangle whose 4 corners are in the point set, else 0. Treat each pair as a diagonal and check the other two corners.

## 3. Intuition (0:23) — `slides/03.png`

Any two points that could be opposite corners determine the other two, so check them in a hash set.

## 4. Brute force vs optimal (0:29) — `slides/04.png`

Checking all groups of four is n to the fourth. Treating pairs as diagonals with a hash set is quadratic.

## 5. Approach (0:37) — `slides/05.png`

Step by step. First, put points in a set. Second, for each pair with different x and y, check the other corners. Third, track the smallest area.

## 6. Worked example (0:49) — `slides/06.png`

Find the smallest axis-aligned rectangle using four of these points.

## 7. Worked example (0:54) — `slides/07.png`

Treat each pair as opposite corners. If the other two corners exist in the set, it's a rectangle.

## 8. Worked example (1:02) — `slides/08.png`

The smallest such rectangle has area 3.

## 9. Java solution (1:06) — `slides/09.png`

We store points in a set, and for each pair with different x and y, check the other two corners and keep the min area.

## 10. Complexity (1:13) — `slides/10.png`

Time is O of n squared. Space is O of n.

## 11. Edge cases & pitfalls (1:18) — `slides/11.png`

Skip pairs on the same row or column; return zero if none.

## 12. Interview tips & follow-ups (1:23) — `slides/12.png`

Grouping by columns is another quadratic approach.

## 13. Recap (1:27) — `slides/13.png`

To recap Minimum Area Rectangle: Any two points that could be opposite corners determine the other two, so check them in a hash set. Try re-implementing it from scratch without looking.
