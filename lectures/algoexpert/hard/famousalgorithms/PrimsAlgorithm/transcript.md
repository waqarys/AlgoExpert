# AlgoExpert · Prims Algorithm

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Prims Algorithm (0:00) — `slides/01.png`

Let's solve Prims Algorithm, a hard famous algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Minimum spanning tree of a connected undirected weighted graph (adjacency list of dest, weight ), grown from vertex 0 with a min-heap of frontier edges.

## 3. Intuition (0:23) — `slides/03.png`

Grow one tree from a start vertex, always adding the cheapest edge leaving it.

## 4. Approach (0:28) — `slides/04.png`

Step by step. First, min-heap of edges from visited vertices. Second, pop the lightest to an unvisited vertex. Third, add it and push its edges. Fourth, repeat.

## 5. Java solution (0:43) — `slides/05.png`

Here's the Java solution, starting with prims algorithm. It follows the steps we just described.

## 6. Complexity (0:50) — `slides/06.png`

Time is O of e log v. Space is O of v plus e.

## 7. Recap (0:54) — `slides/07.png`

To recap Prims Algorithm: Grow one tree from a start vertex, always adding the cheapest edge leaving it. Try re-implementing it from scratch without looking.
