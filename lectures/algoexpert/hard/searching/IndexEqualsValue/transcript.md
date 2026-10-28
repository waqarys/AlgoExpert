# AlgoExpert · Index Equals Value

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Index Equals Value (0:00) — `slides/01.png`

Let's solve Index Equals Value, a hard searching problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Sorted distinct ints; smallest index i with a i equals equals i, or -1. Binary search.

## 3. Intuition (0:21) — `slides/03.png`

Since values are distinct sorted integers, value minus index never decreases, so binary search works.

## 4. Brute force vs optimal (0:28) — `slides/04.png`

A linear scan works. Because values are distinct sorted integers, a i minus i never decreases, so binary search finds the first index where they match.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, binary search. Second, if the value is below the index, go right. Third, otherwise record a match and go left for the smallest.

## 6. Worked example (0:51) — `slides/06.png`

a at 3 = 3 = 3 , so record, look left.

## 7. Worked example (0:56) — `slides/07.png`

a at 1 = -3 < 1 , so go right.

## 8. Worked example (1:00) — `slides/08.png`

a at 2 = 0 < 2 , so go right.

## 9. Java solution (1:04) — `slides/09.png`

Binary search: if a mid is less than mid, go right; otherwise record a match and go left.

## 10. Complexity (1:10) — `slides/10.png`

Time is O of log n. Space is constant.

## 11. Edge cases & pitfalls (1:14) — `slides/11.png`

Keep searching left after a match to get the first one.

## 12. Interview tips & follow-ups (1:18) — `slides/12.png`

Explain why a i minus i is non-decreasing.

## 13. Recap (1:22) — `slides/13.png`

To recap Index Equals Value: Since values are distinct sorted integers, value minus index never decreases, so binary search works. Try re-implementing it from scratch without looking.
