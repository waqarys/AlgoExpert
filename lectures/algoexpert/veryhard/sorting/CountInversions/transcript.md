# AlgoExpert · Count Inversions

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Count Inversions (0:00) — `slides/01.png`

Let's solve Count Inversions, a very hard sorting problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Number of pairs i under j with a i over a j , counted during merge sort.

## 3. Intuition (0:18) — `slides/03.png`

Merge sort counts inversions: when a right element is placed before remaining left elements, they all form inversions.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Checking all pairs is quadratic. Counting during merge sort is n log n.

## 5. Approach (0:31) — `slides/05.png`

Step by step. First, sort halves recursively. Second, during merge, add remaining left count when taking from the right. Third, sum.

## 6. Worked example (0:43) — `slides/06.png`

An inversion is a pair where the earlier value is bigger. There are 5 here.

## 7. Worked example (0:49) — `slides/07.png`

Merge sort counts inversions within each half recursively.

## 8. Worked example (0:54) — `slides/08.png`

While merging, each time a right element goes before remaining left elements, those left elements each form an inversion with it.

## 9. Java solution (1:01) — `slides/09.png`

Count recursively sorts both halves, copies to aux, and merges; when taking from the right, it adds mid minus i plus one.

## 10. Complexity (1:09) — `slides/10.png`

Time is O of n log n. Space is O of n.

## 11. Edge cases & pitfalls (1:13) — `slides/11.png`

Take from the left on ties so equal values aren't counted.

## 12. Interview tips & follow-ups (1:18) — `slides/12.png`

A Fenwick tree also works.

## 13. Recap (1:21) — `slides/13.png`

To recap Count Inversions: Merge sort counts inversions: when a right element is placed before remaining left elements, they all form inversions. Try re-implementing it from scratch without looking.
