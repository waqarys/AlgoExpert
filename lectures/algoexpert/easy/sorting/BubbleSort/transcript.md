# AlgoExpert · Bubble Sort

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Bubble Sort (0:00) — `slides/01.png`

Let's solve Bubble Sort, an easy sorting problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Repeatedly swap adjacent out-of-order pairs; stop early when a pass makes no swaps.

## 3. Intuition (0:18) — `slides/03.png`

Repeatedly swap neighbours that are out of order; each pass bubbles the largest remaining item to the end.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, loop until a pass makes no swaps. Second, swap adjacent pairs that are out of order. Third, shrink the range each pass.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with bubble sort. It follows the steps we just described.

## 6. Complexity (0:44) — `slides/06.png`

Time is O of n squared worst, O of n best. Space is constant.

## 7. Recap (0:50) — `slides/07.png`

To recap Bubble Sort: Repeatedly swap neighbours that are out of order; each pass bubbles the largest remaining item to the end. Try re-implementing it from scratch without looking.
