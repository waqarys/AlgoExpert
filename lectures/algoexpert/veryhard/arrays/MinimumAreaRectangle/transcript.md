# AlgoExpert · Minimum Area Rectangle

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Minimum Area Rectangle (0:00) — `slides/01.png`

Let's solve Minimum Area Rectangle, a very hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Smallest-area axis-aligned rectangle whose 4 corners are in the point set, else 0. Treat each pair as a diagonal and check the other two corners.

## 3. Intuition (0:23) — `slides/03.png`

Any two points that could be opposite corners determine the other two, so check them in a hash set.

## 4. Approach (0:29) — `slides/04.png`

Step by step. First, put points in a set. Second, for each pair with different x and y, check the other corners. Third, track the smallest area.

## 5. Java solution (0:42) — `slides/05.png`

Here's the Java solution, starting with minimum area rectangle. It follows the steps we just described.

## 6. Complexity (0:49) — `slides/06.png`

Time is O of n squared. Space is O of n.

## 7. Recap (0:54) — `slides/07.png`

To recap Minimum Area Rectangle: Any two points that could be opposite corners determine the other two, so check them in a hash set. Try re-implementing it from scratch without looking.
