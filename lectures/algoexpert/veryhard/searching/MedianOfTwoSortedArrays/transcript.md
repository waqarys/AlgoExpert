# AlgoExpert · Median Of Two Sorted Arrays

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Median Of Two Sorted Arrays (0:00) — `slides/01.png`

Let's solve Median Of Two Sorted Arrays, a very hard searching problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Median of the union of two sorted arrays via binary-searched partition.

## 3. Intuition (0:19) — `slides/03.png`

Binary search a cut in the smaller array so the left halves of both hold exactly half the elements.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, search the cut in the smaller array. Second, derive the cut in the other. Third, check that the edges are in order. Fourth, median from the edge values.

## 5. Java solution (0:39) — `slides/05.png`

Here's the Java solution, starting with median of two sorted arrays. It follows the steps we just described.

## 6. Complexity (0:47) — `slides/06.png`

Time is O(log(min(n, m))). Space is constant.

## 7. Recap (0:54) — `slides/07.png`

To recap Median Of Two Sorted Arrays: Binary search a cut in the smaller array so the left halves of both hold exactly half the elements. Try re-implementing it from scratch without looking.
