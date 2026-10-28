# AlgoExpert · Count Squares

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Count Squares (0:00) — `slides/01.png`

Let's solve Count Squares, a hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Number of squares (any orientation) whose four corners are all in the point set. For each pair as a diagonal, compute the other two corners; each square is found twice.

## 3. Intuition (0:23) — `slides/03.png`

Any two points can be a square's diagonal; the other two corners are then fixed, so just check they exist.

## 4. Brute force vs optimal (0:30) — `slides/04.png`

Checking every group of four points is n to the fourth. Treating each pair as a diagonal and looking up the other two corners in a hash set is quadratic.

## 5. Approach (0:40) — `slides/05.png`

Step by step. First, put all points in a hash set. Second, for each pair, compute the two remaining corners by rotating around the midpoint. Third, count when both exist. Fourth, divide by two since each square has two diagonals.

## 6. Worked example (0:57) — `slides/06.png`

Here are seven points. We'll treat each pair as a square's diagonal.

## 7. Worked example (1:03) — `slides/07.png`

Take (1, 1) and (0, 0) as a diagonal. The midpoint is the square's centre.

## 8. Worked example (1:11) — `slides/08.png`

Rotating the half-diagonal ninety degrees gives the other two corners. Both are in the set, so this is a square.

## 9. Worked example (1:19) — `slides/09.png`

We found 8 ordered diagonal pairs. Each square has two diagonals in two orders, so divide by four: 2.

## 10. Java solution (1:27) — `slides/10.png`

We store doubled coordinates in a set. For each ordered pair, compute the midpoint and the half-diagonal, rotate it to get the other two corners, and count if both exist. Return count over four.

## 11. Complexity (1:41) — `slides/11.png`

Time is O of n squared. Space is O of n.

## 12. Edge cases & pitfalls (1:46) — `slides/12.png`

Each square is counted four times, so divide. Doubling every coordinate keeps midpoints integral, avoiding floating-point keys.

## 13. Interview tips & follow-ups (1:55) — `slides/13.png`

This counts tilted squares too, not just axis-aligned ones. Mention the edge-based variant as an alternative.

## 14. Recap (2:03) — `slides/14.png`

To recap Count Squares: Any two points can be a square's diagonal; the other two corners are then fixed, so just check they exist. Try re-implementing it from scratch without looking.
