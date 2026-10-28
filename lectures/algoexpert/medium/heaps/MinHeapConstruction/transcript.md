# AlgoExpert · Min Heap Construction

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Min Heap Construction (0:00) — `slides/01.png`

Let's solve Min Heap Construction, a medium heaps problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Array-backed min-heap with buildHeap (O of n sift-down), siftUp, siftDown, peek, insert and remove.

## 3. Intuition (0:20) — `slides/03.png`

A heap is an array tree; sift up after insert, sift down after removal.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Inserting elements one at a time costs n log n. Building bottom-up, sifting down from the last parent to the root, is linear, because most nodes sit near the bottom and move only a little.

## 5. Approach (0:36) — `slides/05.png`

Step by step. First, build by sifting down from the last parent. Second, insert at the end and sift up. Third, remove by swapping root with last and sifting down.

## 6. Worked example (0:49) — `slides/06.png`

View the array as a complete binary tree: children of index i are at two i plus one and two i plus two.

## 7. Worked example (0:55) — `slides/07.png`

Sift down the value 17 at index 3, swapping with its smaller child until it's no bigger than both children.

## 8. Worked example (1:03) — `slides/08.png`

Sift down the value 23 at index 2, swapping with its smaller child until it's no bigger than both children.

## 9. Worked example (1:10) — `slides/09.png`

Sift down the value 102 at index 1, swapping with its smaller child until it's no bigger than both children.

## 10. Worked example (1:17) — `slides/10.png`

Sift down the value 30 at index 0, swapping with its smaller child until it's no bigger than both children.

## 11. Java solution (1/2) (1:25) — `slides/11.png`

Build heap sifts down from the last parent to index zero. Sift down picks the smaller child, stops if it isn't smaller, otherwise swaps and continues. Sift up swaps with the parent while the parent is bigger.

## 12. Java solution (2/2) (1:38) — `slides/12.png`

Build heap sifts down from the last parent to index zero. Sift down picks the smaller child, stops if it isn't smaller, otherwise swaps and continues. Sift up swaps with the parent while the parent is bigger.

## 13. Complexity (1:52) — `slides/13.png`

Time is build O of n, insert or remove O of log n, peek constant. Space is O of n.

## 14. Edge cases & pitfalls (2:00) — `slides/14.png`

The last parent is at n minus two over two. Always swap with the smaller child. Remove swaps the root with the last element, pops, and sifts down.

## 15. Interview tips & follow-ups (2:10) — `slides/15.png`

Be ready to explain the linear build. Heaps power k-th largest and merging k sorted lists.

## 16. Recap (2:18) — `slides/16.png`

To recap Min Heap Construction: A heap is an array tree; sift up after insert, sift down after removal. Try re-implementing it from scratch without looking.
