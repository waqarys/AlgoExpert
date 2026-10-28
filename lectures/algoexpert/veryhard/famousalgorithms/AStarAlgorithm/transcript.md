# AlgoExpert · A Star Algorithm

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. A Star Algorithm (0:00) — `slides/01.png`

Let's solve A Star Algorithm, a very hard famous algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Shortest 4-directional path on a grid (0 free, 1 obstacle) from start to end using Manhattan-distance heuristic. Returns the list of row, col positions, or if unreachable.

## 3. Intuition (0:26) — `slides/03.png`

Like Dijkstra, but the heap is ordered by distance plus a Manhattan heuristic toward the goal.

## 4. Brute force vs optimal (0:32) — `slides/04.png`

BFS and Dijkstra explore in all directions. A star adds a heuristic that pulls the search toward the goal while staying optimal if it never overestimates.

## 5. Approach (0:42) — `slides/05.png`

Step by step. First, open set ordered by f equals g plus h. Second, expand the best node. Third, update neighbours' g. Fourth, rebuild the path when reaching the end.

## 6. Worked example (0:56) — `slides/06.png`

A star orders the frontier by f, the cost so far plus a heuristic estimate to the goal; here Manhattan distance.

## 7. Worked example (1:03) — `slides/07.png`

Pop the cell with the lowest f, relax its four neighbours, skipping walls, and push improvements.

## 8. Worked example (1:09) — `slides/08.png`

When we pop the end, follow back-pointers to rebuild the path.

## 9. Java solution (1/2) (1:14) — `slides/09.png`

We set g to max, push the start with its heuristic, and loop: pop, stop at the end, and for each open neighbour with a better g, update it, record from, and push with g plus h. Then rebuild the path.

## 10. Java solution (2/2) (1:27) — `slides/10.png`

We set g to max, push the start with its heuristic, and loop: pop, stop at the end, and for each open neighbour with a better g, update it, record from, and push with g plus h. Then rebuild the path.

## 11. Complexity (1:40) — `slides/11.png`

Time is O of w times h log(w times h). Space is O of w times h.

## 12. Edge cases & pitfalls (1:47) — `slides/12.png`

Manhattan distance is admissible on a four-direction grid.

## 13. Interview tips & follow-ups (1:52) — `slides/13.png`

Dijkstra is A star with a zero heuristic.

## 14. Recap (1:56) — `slides/14.png`

To recap A Star Algorithm: Like Dijkstra, but the heap is ordered by distance plus a Manhattan heuristic toward the goal. Try re-implementing it from scratch without looking.
