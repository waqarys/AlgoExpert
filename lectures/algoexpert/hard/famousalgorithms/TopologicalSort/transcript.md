# AlgoExpert · Topological Sort

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Topological Sort (0:00) — `slides/01.png`

Let's solve Topological Sort, a hard famous algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Jobs with prereq, job dependencies; return a valid order or if there is a cycle (Kahn's algorithm).

## 3. Intuition (0:21) — `slides/03.png`

Kahn's algorithm: repeatedly take jobs with no remaining prerequisites.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, count in-degrees. Second, queue jobs with zero. Third, pop, append, and decrement dependents. Fourth, if not all jobs appear, there's a cycle.

## 5. Java solution (0:41) — `slides/05.png`

Here's the Java solution, starting with topological sort. It follows the steps we just described.

## 6. Complexity (0:48) — `slides/06.png`

Time is O of j plus d. Space is O of j plus d.

## 7. Recap (0:53) — `slides/07.png`

To recap Topological Sort: Kahn's algorithm: repeatedly take jobs with no remaining prerequisites. Try re-implementing it from scratch without looking.
