# AlgoExpert · Count Squares

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Count Squares (0:00) — `slides/01.png`

Let's solve Count Squares, a hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Number of squares (any orientation) whose four corners are all in the point set. For each pair as a diagonal, compute the other two corners; each square is found twice.

## 3. Intuition (0:23) — `slides/03.png`

Any two points can be a square's diagonal; the other two corners are then fixed, so just check they exist.

## 4. Approach (0:30) — `slides/04.png`

Step by step. First, put all points in a hash set. Second, for each pair, compute the two remaining corners by rotating around the midpoint. Third, count when both exist. Fourth, divide by two since each square has two diagonals.

## 5. Java solution (0:48) — `slides/05.png`

Here's the Java solution, starting with count squares. It follows the steps we just described.

## 6. Complexity (0:55) — `slides/06.png`

Time is O of n squared. Space is O of n.

## 7. Recap (1:00) — `slides/07.png`

To recap Count Squares: Any two points can be a square's diagonal; the other two corners are then fixed, so just check they exist. Try re-implementing it from scratch without looking.
