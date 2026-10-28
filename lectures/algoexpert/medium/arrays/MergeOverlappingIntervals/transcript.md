# AlgoExpert · Merge Overlapping Intervals

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Merge Overlapping Intervals (0:00) — `slides/01.png`

Let's solve Merge Overlapping Intervals, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Merge all overlapping start, end intervals; result sorted by start.

## 3. Intuition (0:19) — `slides/03.png`

After sorting by start, overlapping intervals are adjacent, so one pass can merge them.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, sort by start. Second, keep the current merged interval. Third, extend its end on overlap. Fourth, otherwise start a new one.

## 5. Java solution (0:38) — `slides/05.png`

Here's the Java solution, starting with merge overlapping intervals. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of n log n. Space is O of n.

## 7. Recap (0:50) — `slides/07.png`

To recap Merge Overlapping Intervals: After sorting by start, overlapping intervals are adjacent, so one pass can merge them. Try re-implementing it from scratch without looking.
