# AlgoExpert · Task Assignment

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Task Assignment (0:00) — `slides/01.png`

Let's solve Task Assignment, a medium greedy algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. 2k tasks with durations, k workers doing two tasks each in parallel; minimise the longest worker time. Pair shortest with longest. Returns index pairs.

## 3. Intuition (0:25) — `slides/03.png`

Pair the shortest task with the longest so no worker gets two long tasks.

## 4. Approach (0:31) — `slides/04.png`

Step by step. First, sort task indices by duration. Second, pair the ends moving inward. Third, return the index pairs.

## 5. Java solution (0:42) — `slides/05.png`

Here's the Java solution, starting with task assignment. It follows the steps we just described.

## 6. Complexity (0:49) — `slides/06.png`

Time is O of n log n. Space is O of n.

## 7. Recap (0:53) — `slides/07.png`

To recap Task Assignment: Pair the shortest task with the longest so no worker gets two long tasks. Try re-implementing it from scratch without looking.
