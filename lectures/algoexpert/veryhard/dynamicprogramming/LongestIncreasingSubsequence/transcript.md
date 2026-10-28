# AlgoExpert · Longest Increasing Subsequence

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Longest Increasing Subsequence (0:00) — `slides/01.png`

Let's solve Longest Increasing Subsequence, a very hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:13) — `slides/02.png`

Here's the problem. One strictly increasing subsequence of maximum length (patience sorting with predecessor links).

## 3. Intuition (0:21) — `slides/03.png`

Patience sorting: keep the smallest possible tail for each length and binary search where each number goes.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, tails array of indices. Second, binary search the position. Third, record predecessors. Fourth, rebuild from the last tail.

## 5. Java solution (0:41) — `slides/05.png`

Here's the Java solution, starting with longest increasing subsequence. It follows the steps we just described.

## 6. Complexity (0:49) — `slides/06.png`

Time is O of n log n. Space is O of n.

## 7. Recap (0:53) — `slides/07.png`

To recap Longest Increasing Subsequence: Patience sorting: keep the smallest possible tail for each length and binary search where each number goes. Try re-implementing it from scratch without looking.
