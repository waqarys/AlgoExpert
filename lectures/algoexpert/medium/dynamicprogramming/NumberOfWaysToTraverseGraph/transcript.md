# AlgoExpert · Number Of Ways To Traverse Graph

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Number Of Ways To Traverse Graph (0:00) — `slides/01.png`

Let's solve Number Of Ways To Traverse Graph, a medium dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Paths from top-left to bottom-right of a width x height grid moving only right or down. Equals C(w plus h-2, w-1), computed incrementally to avoid overflow.

## 3. Intuition (0:26) — `slides/03.png`

Paths to a cell come from above or from the left; this is also a binomial coefficient.

## 4. Brute force vs optimal (0:32) — `slides/04.png`

Plain recursion recomputes paths exponentially. A DP grid fills in w times h. Since every path is just an ordering of rights and downs, a binomial coefficient gives the answer directly.

## 5. Approach (0:46) — `slides/05.png`

Step by step. First, first row and column have one way. Second, each cell sums its top and left neighbours. Third, return the bottom-right cell.

## 6. Worked example (0:58) — `slides/06.png`

Cells on the top row or left column can only be reached one way.

## 7. Worked example (1:02) — `slides/07.png`

Every other cell adds the ways from above and from the left. Cell one-one is one plus one, two.

## 8. Worked example (1:10) — `slides/08.png`

Filling the grid, the bottom-right cell holds 10 paths.

## 9. Worked example (1:14) — `slides/09.png`

The solution here uses a shortcut: every path is some arrangement of three rights and two downs, so the count is five choose two, ten. That's constant space and linear time.

## 10. Java solution (1:25) — `slides/10.png`

We compute n as total moves and k as the smaller dimension minus one, then build the binomial coefficient incrementally: multiply by n minus k plus i and divide by i, which always stays an integer.

## 11. Complexity (1:34) — `slides/11.png`

Time is O of min(w, h). Space is constant.

## 12. Edge cases & pitfalls (1:40) — `slides/12.png`

A single row or column has one path. Compute the binomial incrementally, multiplying then dividing, to keep values exact and avoid overflow.

## 13. Interview tips & follow-ups (1:50) — `slides/13.png`

Present the DP first, then mention the formula. With obstacles, the formula breaks and DP is required.

## 14. Recap (1:59) — `slides/14.png`

To recap Number Of Ways To Traverse Graph: Paths to a cell come from above or from the left; this is also a binomial coefficient. Try re-implementing it from scratch without looking.
