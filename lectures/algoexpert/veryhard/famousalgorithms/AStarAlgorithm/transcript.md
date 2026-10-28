# AlgoExpert · A Star Algorithm

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. A Star Algorithm (0:00) — `slides/01.png`

Let's solve A Star Algorithm, a very hard famous algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Shortest 4-directional path on a grid (0 free, 1 obstacle) from start to end using Manhattan-distance heuristic. Returns the list of row, col positions, or if unreachable.

## 3. Intuition (0:26) — `slides/03.png`

Like Dijkstra, but the heap is ordered by distance plus a Manhattan heuristic toward the goal.

## 4. Approach (0:32) — `slides/04.png`

Step by step. First, open set ordered by f equals g plus h. Second, expand the best node. Third, update neighbours' g. Fourth, rebuild the path when reaching the end.

## 5. Java solution (1/2) (0:46) — `slides/05.png`

Here's the Java solution, starting with a star algorithm. It follows the steps we just described.

## 6. Java solution (2/2) (0:53) — `slides/06.png`

Continuing with h.

## 7. Complexity (0:56) — `slides/07.png`

Time is O of w times h log(w times h). Space is O of w times h.

## 8. Recap (1:03) — `slides/08.png`

To recap A Star Algorithm: Like Dijkstra, but the heap is ordered by distance plus a Manhattan heuristic toward the goal. Try re-implementing it from scratch without looking.
