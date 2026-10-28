# AlgoExpert · Dijkstras Algorithm

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Dijkstras Algorithm (0:00) — `slides/01.png`

Let's solve Dijkstras Algorithm, a hard famous algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Edges v lists destination, weight (non-negative). Shortest distance from start to every vertex, -1 if unreachable.

## 3. Intuition (0:23) — `slides/03.png`

Always expand the closest unvisited vertex; with non-negative weights its distance is final.

## 4. Brute force vs optimal (0:29) — `slides/04.png`

Bellman-Ford relaxes every edge repeatedly and handles negative weights, but it's V times E. Dijkstra always finalises the closest unfinished vertex; with a heap that's E log V.

## 5. Approach (0:40) — `slides/05.png`

Step by step. First, distances start at infinity. Second, use a min-heap of distance and vertex. Third, relax outgoing edges. Fourth, unreached vertices are minus one.

## 6. Worked example (0:55) — `slides/06.png`

Pop vertex 0, the closest unfinished one at distance 0. Relaxing its edges improves 1.

## 7. Worked example (1:02) — `slides/07.png`

Pop vertex 1, the closest unfinished one at distance 7. Relaxing its edges improves 2, 3, 4.

## 8. Worked example (1:11) — `slides/08.png`

Pop vertex 4, the closest unfinished one at distance 10. No edge improves anything.

## 9. Worked example (1:18) — `slides/09.png`

Pop vertex 2, the closest unfinished one at distance 13. No edge improves anything.

## 10. Worked example (1:25) — `slides/10.png`

Pop vertex 3, the closest unfinished one at distance 27. No edge improves anything.

## 11. Java solution (1:33) — `slides/11.png`

Distances start at max except the start. We poll the heap, skip stale entries, and relax each edge, pushing improved distances. Finally we map max value to minus one.

## 12. Complexity (1:45) — `slides/12.png`

Time is O of (v plus e) log v. Space is O of v.

## 13. Edge cases & pitfalls (1:50) — `slides/13.png`

Dijkstra needs non-negative weights. Lazy deletion means skipping heap entries whose distance is stale.

## 14. Interview tips & follow-ups (1:57) — `slides/14.png`

Explain why the closest vertex can be finalised. Follow-ups reconstruct paths or add a heuristic, which is A star.

## 15. Recap (2:06) — `slides/15.png`

To recap Dijkstras Algorithm: Always expand the closest unvisited vertex; with non-negative weights its distance is final. Try re-implementing it from scratch without looking.
