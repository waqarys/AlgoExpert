# AlgoExpert · Insertion Sort

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Insertion Sort (0:00) — `slides/01.png`

Let's solve Insertion Sort, an easy sorting problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Grow a sorted prefix by sinking each new element into place.

## 3. Intuition (0:17) — `slides/03.png`

Grow a sorted prefix, inserting each new element into its correct position by shifting it left.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Insertion sort is quadratic in the worst case, but on nearly-sorted data it's close to linear, which is why real libraries use it for small or almost-sorted runs.

## 5. Approach (0:33) — `slides/05.png`

Step by step. First, for each element from the second. Second, swap it left while it's smaller than its neighbour. Third, the prefix stays sorted.

## 6. Worked example (0:45) — `slides/06.png`

We take element 1 and swap it left until it's no smaller than its neighbour. It lands at index 0, and the first 2 elements are now sorted.

## 7. Worked example (0:54) — `slides/07.png`

We take element 2 and swap it left until it's no smaller than its neighbour. It lands at index 0, and the first 3 elements are now sorted.

## 8. Worked example (1:04) — `slides/08.png`

We take element 3 and swap it left until it's no smaller than its neighbour. It lands at index 3, and the first 4 elements are now sorted.

## 9. Worked example (1:13) — `slides/09.png`

We take element 5 and swap it left until it's no smaller than its neighbour. It lands at index 3, and the first 6 elements are now sorted.

## 10. Worked example (1:22) — `slides/10.png`

We take element 6 and swap it left until it's no smaller than its neighbour. It lands at index 1, and the first 7 elements are now sorted.

## 11. Java solution (1:32) — `slides/11.png`

For each index from one, we swap the element left while it's smaller than the one before it.

## 12. Complexity (1:38) — `slides/12.png`

Time is O of n squared worst, O of n best. Space is constant.

## 13. Edge cases & pitfalls (1:44) — `slides/13.png`

Use a strict comparison to keep it stable. Shifting elements instead of swapping reduces writes.

## 14. Interview tips & follow-ups (1:51) — `slides/14.png`

Explain the invariant: the prefix is always sorted. A follow-up uses binary search to find the insert position, though shifting is still linear.

## 15. Recap (2:01) — `slides/15.png`

To recap Insertion Sort: Grow a sorted prefix, inserting each new element into its correct position by shifting it left. Try re-implementing it from scratch without looking.
