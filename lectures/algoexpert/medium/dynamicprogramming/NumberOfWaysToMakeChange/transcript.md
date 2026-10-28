# AlgoExpert · Number Of Ways To Make Change

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Number Of Ways To Make Change (0:00) — `slides/01.png`

Let's solve Number Of Ways To Make Change, a medium dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Count combinations of unlimited coins that sum to n.

## 3. Intuition (0:18) — `slides/03.png`

Count combinations by processing one coin at a time so order doesn't matter.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Naive recursion is exponential and easily counts the same combination in different orders. Putting coins in the outer loop means each combination is built in a fixed coin order, so it's counted exactly once.

## 5. Approach (0:37) — `slides/05.png`

Step by step. First, ways of zero is one. Second, for each coin, for each amount, add ways of amount minus coin. Third, return ways of n.

## 6. Worked example (0:49) — `slides/06.png`

There's exactly one way to make zero: use no coins.

## 7. Worked example (0:53) — `slides/07.png`

Adding coin 1: every amount from 1 up gains the ways to make the remainder. With coins one and five, there are 1 ways to make six: six ones, or five plus one.

## 8. Worked example (1:04) — `slides/08.png`

Adding coin 5: every amount from 5 up gains the ways to make the remainder. With coins one and five, there are 2 ways to make six: six ones, or five plus one.

## 9. Java solution (1:15) — `slides/09.png`

We set ways of zero to one. For each coin, for each amount from that coin to n, add the ways for amount minus coin. Return ways of n.

## 10. Complexity (1:25) — `slides/10.png`

Time is O of n times d. Space is O of n.

## 11. Edge cases & pitfalls (1:29) — `slides/11.png`

If you swap the loops you count permutations instead of combinations, a very common bug.

## 12. Interview tips & follow-ups (1:35) — `slides/12.png`

Explain the combination versus permutation distinction clearly. A follow-up limits how many of each coin you have.

## 13. Recap (1:43) — `slides/13.png`

To recap Number Of Ways To Make Change: Count combinations by processing one coin at a time so order doesn't matter. Try re-implementing it from scratch without looking.
