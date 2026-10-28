# AlgoExpert · Insertion Sort

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Insertion Sort (0:00) — `slides/01.png`

Let's solve Insertion Sort, an easy sorting problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Grow a sorted prefix by sinking each new element into place.

## 3. Intuition (0:15) — `slides/03.png`

Grow a sorted prefix, inserting each new element into its correct position by shifting it left.

## 4. Approach (0:21) — `slides/04.png`

Step by step. First, for each element from the second. Second, swap it left while it's smaller than its neighbour. Third, the prefix stays sorted.

## 5. Java solution (0:33) — `slides/05.png`

Here's the Java solution, starting with insertion sort. It follows the steps we just described.

## 6. Complexity (0:41) — `slides/06.png`

Time is O of n squared worst, O of n best. Space is constant.

## 7. Recap (0:47) — `slides/07.png`

To recap Insertion Sort: Grow a sorted prefix, inserting each new element into its correct position by shifting it left. Try re-implementing it from scratch without looking.
