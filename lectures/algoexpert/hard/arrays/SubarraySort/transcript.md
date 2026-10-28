# AlgoExpert · Subarray Sort

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Subarray Sort (0:00) — `slides/01.png`

Let's solve Subarray Sort, a hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Smallest start, end range which, if sorted, makes the whole array sorted; -1, -1 if sorted.

## 3. Intuition (0:19) — `slides/03.png`

Find the smallest and largest values that are out of order; their correct positions bound the subarray.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

Sorting a copy and finding the first and last differences is n log n. Finding the smallest and largest out-of-order values, then where they belong, is linear.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, scan for elements out of order with a neighbour. Second, track the min and max among them. Third, find where min belongs from the left and max from the right.

## 6. Worked example (0:48) — `slides/06.png`

Mark every element that's smaller than its left neighbour or bigger than its right.

## 7. Worked example (0:54) — `slides/07.png`

Among them the smallest is 6 and the largest is 12.

## 8. Worked example (0:58) — `slides/08.png`

6 belongs right after the first value bigger than it, index 3. 12 belongs at index 9. Sorting indices 3 to 9 sorts the array.

## 9. Java solution (1:09) — `slides/09.png`

We track the min and max of out-of-order elements, return minus ones if none, then move l right while values are at most min and r left while values are at least max.

## 10. Complexity (1:19) — `slides/10.png`

Time is O of n. Space is constant.

## 11. Edge cases & pitfalls (1:22) — `slides/11.png`

If nothing is out of order, return minus one, minus one. Use less-or-equal so duplicates are handled.

## 12. Interview tips & follow-ups (1:30) — `slides/12.png`

Explain why the extreme out-of-order values define the bounds.

## 13. Recap (1:35) — `slides/13.png`

To recap Subarray Sort: Find the smallest and largest values that are out of order; their correct positions bound the subarray. Try re-implementing it from scratch without looking.
