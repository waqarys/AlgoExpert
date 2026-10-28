# AlgoExpert · Merge Sorted Arrays

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Merge Sorted Arrays (0:00) — `slides/01.png`

Let's solve Merge Sorted Arrays, a very hard heaps problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Merge k sorted lists into one sorted list using a min-heap of (value, list, index).

## 3. Intuition (0:19) — `slides/03.png`

A min-heap holds the head of each list; popping it always gives the next smallest overall.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Concatenating and sorting ignores the existing order. A min-heap holding one element per array always yields the next smallest in log k.

## 5. Approach (0:34) — `slides/05.png`

Step by step. First, push each list's first element. Second, pop the min and append. Third, push the next from that list. Fourth, repeat.

## 6. Worked example (0:48) — `slides/06.png`

Pop the smallest, -124, from array 2, and push that array's next element.

## 7. Worked example (0:54) — `slides/07.png`

Pop the smallest, 0, from array 1, and push that array's next element.

## 8. Worked example (1:00) — `slides/08.png`

Pop the smallest, 3, from array 3, and push that array's next element.

## 9. Worked example (1:05) — `slides/09.png`

Pop the smallest, 9, from array 0, and push that array's next element.

## 10. Worked example (1:11) — `slides/10.png`

Pop the smallest, 121, from array 2, and push that array's next element.

## 11. Java solution (1:17) — `slides/11.png`

We seed the heap with each array's first element, then poll, append, and push that array's next element.

## 12. Complexity (1:24) — `slides/12.png`

Time is O of n log k. Space is O of n plus k.

## 13. Edge cases & pitfalls (1:28) — `slides/13.png`

Skip empty arrays when seeding the heap.

## 14. Interview tips & follow-ups (1:32) — `slides/14.png`

Pairwise divide-and-conquer merging is also N log k.

## 15. Recap (1:36) — `slides/15.png`

To recap Merge Sorted Arrays: A min-heap holds the head of each list; popping it always gives the next smallest overall. Try re-implementing it from scratch without looking.
