# AlgoExpert · Topological Sort

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Topological Sort (0:00) — `slides/01.png`

Let's solve Topological Sort, a hard famous algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Jobs with prereq, job dependencies; return a valid order or if there is a cycle (Kahn's algorithm).

## 3. Intuition (0:21) — `slides/03.png`

Kahn's algorithm: repeatedly take jobs with no remaining prerequisites.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

Scanning repeatedly for a free job is quadratic. Kahn's algorithm keeps in-degrees and a queue of free jobs, linear time. A depth-first post-order also works.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, count in-degrees. Second, queue jobs with zero. Third, pop, append, and decrement dependents. Fourth, if not all jobs appear, there's a cycle.

## 6. Worked example (0:52) — `slides/06.png`

Job 1 has no remaining prerequisites, so it goes next. It frees nothing new.

## 7. Worked example (0:59) — `slides/07.png`

Job 4 has no remaining prerequisites, so it goes next. That frees 3.

## 8. Worked example (1:06) — `slides/08.png`

Job 3 has no remaining prerequisites, so it goes next. That frees 2.

## 9. Worked example (1:13) — `slides/09.png`

Job 2 has no remaining prerequisites, so it goes next. It frees nothing new.

## 10. Java solution (1:19) — `slides/10.png`

We build adjacency lists and in-degrees, queue jobs with zero, and repeatedly output one, decrementing its dependents and queuing any that hit zero. If not everything is output, return empty.

## 11. Complexity (1:32) — `slides/11.png`

Time is O of j plus d. Space is O of j plus d.

## 12. Edge cases & pitfalls (1:36) — `slides/12.png`

If a cycle exists, some jobs never reach in-degree zero, so return an empty list.

## 13. Interview tips & follow-ups (1:42) — `slides/13.png`

Mention the DFS approach and how it detects cycles with colours.

## 14. Recap (1:47) — `slides/14.png`

To recap Topological Sort: Kahn's algorithm: repeatedly take jobs with no remaining prerequisites. Try re-implementing it from scratch without looking.
