# AlgoExpert · Heap Sort

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Heap Sort (0:00) — `slides/01.png`

Let's solve Heap Sort, a hard sorting problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:10) — `slides/02.png`

Here's the problem. Build a max-heap in place then repeatedly move the max to the end.

## 3. Intuition (0:17) — `slides/03.png`

Build a max-heap in place, then repeatedly move the maximum to the end and restore the heap.

## 4. Brute force vs optimal (0:23) — `slides/04.png`

Selection sort finds the max by scanning each time. A heap finds it in log n, giving n log n in place.

## 5. Approach (0:31) — `slides/05.png`

Step by step. First, heapify from the last parent down. Second, swap root with the last element. Third, sift down within the shrinking heap.

## 6. Worked example (0:43) — `slides/06.png`

First build a max-heap bottom-up. The largest, nine, is at the root.

## 7. Worked example (0:50) — `slides/07.png`

Swap the root into position 6; that part is sorted. Sift the new root down to restore the heap.

## 8. Worked example (0:57) — `slides/08.png`

Swap the root into position 5; that part is sorted. Sift the new root down to restore the heap.

## 9. Worked example (1:04) — `slides/09.png`

Swap the root into position 4; that part is sorted. Sift the new root down to restore the heap.

## 10. Worked example (1:12) — `slides/10.png`

Swap the root into position 2; that part is sorted. Sift the new root down to restore the heap.

## 11. Worked example (1:19) — `slides/11.png`

Swap the root into position 1; that part is sorted. Sift the new root down to restore the heap.

## 12. Java solution (1:26) — `slides/12.png`

We sift down from the last parent to build the heap, then repeatedly swap the root with end and sift the root down within end.

## 13. Complexity (1:33) — `slides/13.png`

Time is O of n log n. Space is constant.

## 14. Edge cases & pitfalls (1:37) — `slides/14.png`

Build bottom-up, and shrink the heap boundary each step.

## 15. Interview tips & follow-ups (1:42) — `slides/15.png`

Heap sort guarantees n log n with constant memory, but is cache-unfriendly and unstable.

## 16. Recap (1:48) — `slides/16.png`

To recap Heap Sort: Build a max-heap in place, then repeatedly move the maximum to the end and restore the heap. Try re-implementing it from scratch without looking.
