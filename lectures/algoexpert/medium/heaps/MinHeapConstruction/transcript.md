# AlgoExpert · Min Heap Construction

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Min Heap Construction (0:00) — `slides/01.png`

Let's solve Min Heap Construction, a medium heaps problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Array-backed min-heap with buildHeap (O of n sift-down), siftUp, siftDown, peek, insert and remove.

## 3. Intuition (0:20) — `slides/03.png`

A heap is an array tree; sift up after insert, sift down after removal.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, build by sifting down from the last parent. Second, insert at the end and sift up. Third, remove by swapping root with last and sifting down.

## 5. Java solution (1/2) (0:38) — `slides/05.png`

Here's the Java solution, starting with min heap. It follows the steps we just described.

## 6. Java solution (2/2) (0:45) — `slides/06.png`

Continuing with peek, remove, insert.

## 7. Complexity (0:49) — `slides/07.png`

Time is build O of n, insert or remove O of log n, peek constant. Space is O of n.

## 8. Recap (0:57) — `slides/08.png`

To recap Min Heap Construction: A heap is an array tree; sift up after insert, sift down after removal. Try re-implementing it from scratch without looking.
