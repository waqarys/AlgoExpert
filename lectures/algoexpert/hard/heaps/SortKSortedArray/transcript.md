# AlgoExpert · Sort K Sorted Array

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Sort K Sorted Array (0:00) — `slides/01.png`

Let's solve Sort K Sorted Array, a hard heaps problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Every element is at most k positions from its sorted position; sort with a size-(k plus 1) min-heap.

## 3. Intuition (0:20) — `slides/03.png`

Every element is within k of its spot, so the minimum of the next k plus one items is always next in order.

## 4. Brute force vs optimal (0:27) — `slides/04.png`

A full sort ignores the structure. Since each element is at most k away from its spot, the smallest of the next k plus one elements is always next, so a heap of size k plus one gives n log k.

## 5. Approach (0:39) — `slides/05.png`

Step by step. First, fill a min-heap with k plus one items. Second, pop the min into place. Third, push the next item. Fourth, drain the heap.

## 6. Worked example (0:52) — `slides/06.png`

Push 3. The heap isn't full yet.

## 7. Worked example (0:57) — `slides/07.png`

Push 1. The heap isn't full yet.

## 8. Worked example (1:01) — `slides/08.png`

Push 5. The heap has more than 3, so pop the smallest, 1, which must be in its final place.

## 9. Worked example (1:09) — `slides/09.png`

Push 7. The heap has more than 3, so pop the smallest, 3, which must be in its final place.

## 10. Worked example (1:17) — `slides/10.png`

Push 6. The heap has more than 3, so pop the smallest, 4, which must be in its final place.

## 11. Worked example (1:24) — `slides/11.png`

Drain the rest of the heap. The array is sorted.

## 12. Java solution (1:29) — `slides/12.png`

We push each element, and once the heap exceeds k, poll into the next write slot. Then drain the heap.

## 13. Complexity (1:37) — `slides/13.png`

Time is O of n log k. Space is O of k.

## 14. Edge cases & pitfalls (1:41) — `slides/14.png`

With k zero it's already sorted.

## 15. Interview tips & follow-ups (1:44) — `slides/15.png`

Explain why the minimum of the window is safe to place.

## 16. Recap (1:49) — `slides/16.png`

To recap Sort K Sorted Array: Every element is within k of its spot, so the minimum of the next k plus one items is always next in order. Try re-implementing it from scratch without looking.
