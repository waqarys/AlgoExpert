# AlgoExpert · Node Swap

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Node Swap (0:00) — `slides/01.png`

Let's solve Node Swap, a very hard linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Swap every pair of adjacent nodes (not values); return the new head.

## 3. Intuition (0:18) — `slides/03.png`

Swap pairs by rewiring three links at a time, using a dummy head.

## 4. Approach (0:23) — `slides/04.png`

Step by step. First, dummy before head. Second, for each pair, rewire previous, first and second. Third, advance by two.

## 5. Java solution (0:35) — `slides/05.png`

Here's the Java solution, starting with node swap. It follows the steps we just described.

## 6. Complexity (0:42) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:46) — `slides/07.png`

To recap Node Swap: Swap pairs by rewiring three links at a time, using a dummy head. Try re-implementing it from scratch without looking.
