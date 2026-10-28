# AlgoExpert · Quickselect

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Quickselect (0:00) — `slides/01.png`

Let's solve Quickselect, a hard searching problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Kth smallest element (1-based) of an unsorted array, in place with Hoare-style partitioning.

## 3. Intuition (0:19) — `slides/03.png`

Partition like quicksort, but only recurse into the side containing the kth position.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Sorting finds the k-th smallest in n log n. A heap of size k is n log k. Quickselect partitions and recurses into one side only, linear on average.

## 5. Approach (0:36) — `slides/05.png`

Step by step. First, pick a pivot and partition. Second, if the pivot lands at k minus one, done. Third, else continue on one side.

## 6. Worked example (0:48) — `slides/06.png`

Partition around 8: it lands at index 5. The target is left of it, so we only recurse there.

## 7. Worked example (0:56) — `slides/07.png`

Partition around 6: it lands at index 3. The target is left of it, so we only recurse there.

## 8. Worked example (1:04) — `slides/08.png`

Partition around 3: it lands at index 1. The target is right of it, so we only recurse there.

## 9. Worked example (1:11) — `slides/09.png`

Partition around 5: it lands at index 2. That's the target!

## 10. Java solution (1:17) — `slides/10.png`

We partition with the first element as pivot, swapping out-of-place pairs, place the pivot at r, and narrow lo or hi toward the target.

## 11. Complexity (1:25) — `slides/11.png`

Time is O of n avg, O of n squared worst. Space is constant.

## 12. Edge cases & pitfalls (1:32) — `slides/12.png`

Worst case is quadratic; randomise the pivot. Remember k is one-indexed.

## 13. Interview tips & follow-ups (1:38) — `slides/13.png`

Median of medians guarantees linear worst case.

## 14. Recap (1:43) — `slides/14.png`

To recap Quickselect: Partition like quicksort, but only recurse into the side containing the kth position. Try re-implementing it from scratch without looking.
