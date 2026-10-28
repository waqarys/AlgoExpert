# AlgoExpert · Optimal Assembly Line

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Optimal Assembly Line (0:00) — `slides/01.png`

Let's solve Optimal Assembly Line, a very hard searching problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Split step durations (in order) into k contiguous stations minimising the longest station time. Binary search on the answer with a greedy feasibility check.

## 3. Intuition (0:24) — `slides/03.png`

Binary search the maximum station time; greedily check whether k stations suffice.

## 4. Approach (0:30) — `slides/04.png`

Step by step. First, bounds are the largest step and the total. Second, greedily fill stations. Third, shrink the range when feasible.

## 5. Java solution (0:42) — `slides/05.png`

Here's the Java solution, starting with optimal assembly line. It follows the steps we just described.

## 6. Complexity (0:49) — `slides/06.png`

Time is O of n log S. Space is constant.

## 7. Recap (0:53) — `slides/07.png`

To recap Optimal Assembly Line: Binary search the maximum station time; greedily check whether k stations suffice. Try re-implementing it from scratch without looking.
