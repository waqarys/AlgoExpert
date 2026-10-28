# AlgoExpert · Quick Sort

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Quick Sort (0:00) — `slides/01.png`

Let's solve Quick Sort, a hard sorting problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. In-place quicksort, recursing into the smaller partition first to bound stack depth.

## 3. Intuition (0:18) — `slides/03.png`

Partition around a pivot so smaller values go left and larger right, then sort each side.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, pick a pivot. Second, partition with two pointers. Third, recurse into the smaller side first. Fourth, loop on the larger to bound the stack.

## 5. Java solution (0:38) — `slides/05.png`

Here's the Java solution, starting with quick sort. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is O of n log n avg, O of n squared worst. Space is O of log n.

## 7. Recap (0:52) — `slides/07.png`

To recap Quick Sort: Partition around a pivot so smaller values go left and larger right, then sort each side. Try re-implementing it from scratch without looking.
