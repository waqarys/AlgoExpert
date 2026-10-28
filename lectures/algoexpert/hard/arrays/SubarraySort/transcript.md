# AlgoExpert · Subarray Sort

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Subarray Sort (0:00) — `slides/01.png`

Let's solve Subarray Sort, a hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Smallest start, end range which, if sorted, makes the whole array sorted; -1, -1 if sorted.

## 3. Intuition (0:19) — `slides/03.png`

Find the smallest and largest values that are out of order; their correct positions bound the subarray.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, scan for elements out of order with a neighbour. Second, track the min and max among them. Third, find where min belongs from the left and max from the right.

## 5. Java solution (0:39) — `slides/05.png`

Here's the Java solution, starting with subarray sort. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:50) — `slides/07.png`

To recap Subarray Sort: Find the smallest and largest values that are out of order; their correct positions bound the subarray. Try re-implementing it from scratch without looking.
