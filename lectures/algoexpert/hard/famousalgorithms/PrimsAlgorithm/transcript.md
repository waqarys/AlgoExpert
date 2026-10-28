# AlgoExpert · Prims Algorithm

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Prims Algorithm (0:00) — `slides/01.png`

Let's solve Prims Algorithm, a hard famous algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Minimum spanning tree of a connected undirected weighted graph (adjacency list of dest, weight ), grown from vertex 0 with a min-heap of frontier edges.

## 3. Intuition (0:23) — `slides/03.png`

Grow one tree from a start vertex, always adding the cheapest edge leaving it.

## 4. Brute force vs optimal (0:28) — `slides/04.png`

Prim grows one tree, always adding the cheapest edge that leaves it. With a heap, that's E log V.

## 5. Approach (0:36) — `slides/05.png`

Step by step. First, min-heap of edges from visited vertices. Second, pop the lightest to an unvisited vertex. Third, add it and push its edges. Fourth, repeat.

## 6. Worked example (0:50) — `slides/06.png`

Start with vertex zero in the tree, and its edges in a min-heap.

## 7. Worked example (0:55) — `slides/07.png`

The cheapest edge leaving the tree is 0 to 1, weight 3. Add 1 and push its edges.

## 8. Worked example (1:02) — `slides/08.png`

The cheapest edge leaving the tree is 1 to 2, weight 1. Add 2 and push its edges.

## 9. Worked example (1:09) — `slides/09.png`

The cheapest edge leaving the tree is 2 to 3, weight 2. Add 3 and push its edges.

## 10. Worked example (1:16) — `slides/10.png`

The cheapest edge leaving the tree is 3 to 4, weight 6. Add 4 and push its edges.

## 11. Java solution (1:23) — `slides/11.png`

We mark zero as in, push its edges, and repeatedly poll the cheapest; if its endpoint is new, add the edge both ways and push that vertex's outgoing edges.

## 12. Complexity (1:32) — `slides/12.png`

Time is O of e log v. Space is O of v plus e.

## 13. Edge cases & pitfalls (1:36) — `slides/13.png`

Lazy deletion again: skip heap edges that lead back into the tree.

## 14. Interview tips & follow-ups (1:41) — `slides/14.png`

Same cut property argument as Kruskal.

## 15. Recap (1:45) — `slides/15.png`

To recap Prims Algorithm: Grow one tree from a start vertex, always adding the cheapest edge leaving it. Try re-implementing it from scratch without looking.
