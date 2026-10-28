# AlgoExpert · Number Of Ways To Make Change

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Number Of Ways To Make Change (0:00) — `slides/01.png`

Let's solve Number Of Ways To Make Change, a medium dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Count combinations of unlimited coins that sum to n.

## 3. Intuition (0:18) — `slides/03.png`

Count combinations by processing one coin at a time so order doesn't matter.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, ways of zero is one. Second, for each coin, for each amount, add ways of amount minus coin. Third, return ways of n.

## 5. Java solution (0:36) — `slides/05.png`

Here's the Java solution, starting with number of ways to make change. It follows the steps we just described.

## 6. Complexity (0:44) — `slides/06.png`

Time is O of n times d. Space is O of n.

## 7. Recap (0:48) — `slides/07.png`

To recap Number Of Ways To Make Change: Count combinations by processing one coin at a time so order doesn't matter. Try re-implementing it from scratch without looking.
