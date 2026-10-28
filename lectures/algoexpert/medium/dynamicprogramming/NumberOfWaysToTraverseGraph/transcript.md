# AlgoExpert · Number Of Ways To Traverse Graph

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Number Of Ways To Traverse Graph (0:00) — `slides/01.png`

Let's solve Number Of Ways To Traverse Graph, a medium dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Paths from top-left to bottom-right of a width x height grid moving only right or down. Equals C(w plus h-2, w-1), computed incrementally to avoid overflow.

## 3. Intuition (0:26) — `slides/03.png`

Paths to a cell come from above or from the left; this is also a binomial coefficient.

## 4. Approach (0:32) — `slides/04.png`

Step by step. First, first row and column have one way. Second, each cell sums its top and left neighbours. Third, return the bottom-right cell.

## 5. Java solution (0:44) — `slides/05.png`

Here's the Java solution, starting with number of ways to traverse graph. It follows the steps we just described.

## 6. Complexity (0:52) — `slides/06.png`

Time is O of min(w, h). Space is constant.

## 7. Recap (0:58) — `slides/07.png`

To recap Number Of Ways To Traverse Graph: Paths to a cell come from above or from the left; this is also a binomial coefficient. Try re-implementing it from scratch without looking.
