# AlgoExpert · Heap Sort

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Heap Sort (0:00) — `slides/01.png`

Let's solve Heap Sort, a hard sorting problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:10) — `slides/02.png`

Here's the problem. Build a max-heap in place then repeatedly move the max to the end.

## 3. Intuition (0:17) — `slides/03.png`

Build a max-heap in place, then repeatedly move the maximum to the end and restore the heap.

## 4. Approach (0:23) — `slides/04.png`

Step by step. First, heapify from the last parent down. Second, swap root with the last element. Third, sift down within the shrinking heap.

## 5. Java solution (0:35) — `slides/05.png`

Here's the Java solution, starting with heap sort. It follows the steps we just described.

## 6. Complexity (0:42) — `slides/06.png`

Time is O of n log n. Space is constant.

## 7. Recap (0:46) — `slides/07.png`

To recap Heap Sort: Build a max-heap in place, then repeatedly move the maximum to the end and restore the heap. Try re-implementing it from scratch without looking.
