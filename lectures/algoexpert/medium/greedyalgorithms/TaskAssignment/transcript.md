# AlgoExpert · Task Assignment

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Task Assignment (0:00) — `slides/01.png`

Let's solve Task Assignment, a medium greedy algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. 2k tasks with durations, k workers doing two tasks each in parallel; minimise the longest worker time. Pair shortest with longest. Returns index pairs.

## 3. Intuition (0:25) — `slides/03.png`

Pair the shortest task with the longest so no worker gets two long tasks.

## 4. Brute force vs optimal (0:31) — `slides/04.png`

Trying every pairing explodes combinatorially. Sorting and pairing the shortest with the longest balances the load in n log n. An exchange argument shows any other pairing can't lower the maximum.

## 5. Approach (0:44) — `slides/05.png`

Step by step. First, sort task indices by duration. Second, pair the ends moving inward. Third, return the index pairs.

## 6. Worked example (0:55) — `slides/06.png`

Sort the task indices by duration, keeping the original indices so we can report them.

## 7. Worked example (1:01) — `slides/07.png`

Worker 1 gets the shortest remaining task, 1, with the longest, 5, for a total of 6.

## 8. Worked example (1:08) — `slides/08.png`

Worker 2 gets the shortest remaining task, 1, with the longest, 4, for a total of 5.

## 9. Worked example (1:15) — `slides/09.png`

Worker 3 gets the shortest remaining task, 3, with the longest, 3, for a total of 6.

## 10. Java solution (1:22) — `slides/10.png`

We build a list of indices, sort it by task duration, and for i from zero to k pair the i-th smallest with the i-th largest.

## 11. Complexity (1:30) — `slides/11.png`

Time is O of n log n. Space is O of n.

## 12. Edge cases & pitfalls (1:34) — `slides/12.png`

Sort indices rather than values, so duplicates still map to the right task numbers.

## 13. Interview tips & follow-ups (1:40) — `slides/13.png`

Sketch the exchange argument briefly. If each worker can take more than two tasks, it becomes a much harder partition problem.

## 14. Recap (1:48) — `slides/14.png`

To recap Task Assignment: Pair the shortest task with the longest so no worker gets two long tasks. Try re-implementing it from scratch without looking.
