# AlgoExpert · Laptop Rentals

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Laptop Rentals (0:00) — `slides/01.png`

Let's solve Laptop Rentals, a hard heaps problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Given start, end) rental intervals, minimum number of laptops needed so nobody waits.

## 3. Intuition (0:19) — `slides/03.png`

The number of laptops needed equals the maximum number of overlapping rentals.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Counting overlaps pairwise is quadratic. Sorting by start and keeping a min-heap of end times reuses the laptop that frees up earliest, in n log n.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, sort starts and ends separately. Second, sweep with two pointers. Third, a start before the next end needs a laptop. Fourth, otherwise reuse one.

## 6. Worked example (0:49) — `slides/06.png`

Interval 0 to 2: the earliest laptop is free by then, so reuse it. That's 1 in use.

## 7. Worked example (0:57) — `slides/07.png`

Interval 0 to 4: no laptop is free yet, so we need another. That's 2 in use.

## 8. Worked example (1:04) — `slides/08.png`

Interval 1 to 4: no laptop is free yet, so we need another. That's 3 in use.

## 9. Worked example (1:11) — `slides/09.png`

Interval 4 to 6: the earliest laptop is free by then, so reuse it. That's 3 in use.

## 10. Worked example (1:18) — `slides/10.png`

Interval 7 to 8: the earliest laptop is free by then, so reuse it. That's 3 in use.

## 11. Worked example (1:26) — `slides/11.png`

Interval 9 to 11: the earliest laptop is free by then, so reuse it. That's 3 in use.

## 12. Java solution (1:34) — `slides/12.png`

We sort by start, and for each interval pop the heap if its earliest end is at most the start, then push the end. The heap size is the answer.

## 13. Complexity (1:43) — `slides/13.png`

Time is O of n log n. Space is O of n.

## 14. Edge cases & pitfalls (1:47) — `slides/14.png`

A laptop returned at time t can be reused for a rental starting at t.

## 15. Interview tips & follow-ups (1:53) — `slides/15.png`

This is meeting rooms two.

## 16. Recap (1:55) — `slides/16.png`

To recap Laptop Rentals: The number of laptops needed equals the maximum number of overlapping rentals. Try re-implementing it from scratch without looking.
