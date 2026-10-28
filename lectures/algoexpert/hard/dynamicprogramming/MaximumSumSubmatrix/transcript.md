# AlgoExpert · Maximum Sum Submatrix

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Maximum Sum Submatrix (0:00) — `slides/01.png`

Let's solve Maximum Sum Submatrix, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Largest sum among all size x size square submatrices, using 2D prefix sums.

## 3. Intuition (0:20) — `slides/03.png`

Two-dimensional prefix sums give any rectangle's sum in constant time.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, build prefix sums. Second, for each bottom-right corner, compute the size by size square sum. Third, track the maximum.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with maximum sum submatrix. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is O of w times h. Space is O of w times h.

## 7. Recap (0:50) — `slides/07.png`

To recap Maximum Sum Submatrix: Two-dimensional prefix sums give any rectangle's sum in constant time. Try re-implementing it from scratch without looking.
