# AlgoExpert · Kruskals Algorithm

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Kruskals Algorithm (0:00) — `slides/01.png`

Let's solve Kruskals Algorithm, a hard famous algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Undirected weighted graph as adjacency list ( dest, weight ); return its minimum spanning tree (forest) in the same format. Sort edges plus union-find.

## 3. Intuition (0:24) — `slides/03.png`

Add edges from lightest to heaviest, skipping any that would form a cycle, detected with union-find.

## 4. Brute force vs optimal (0:31) — `slides/04.png`

Enumerating spanning trees is exponential. Kruskal sorts edges and adds each cheapest one that doesn't form a cycle, checked with union-find, in E log E.

## 5. Approach (0:41) — `slides/05.png`

Step by step. First, collect and sort edges by weight. Second, union-find over vertices. Third, add edges joining different sets. Fourth, return as adjacency list.

## 6. Worked example (0:55) — `slides/06.png`

Next cheapest edge: 1 to 2, weight 1. They're in different components, so add it.

## 7. Worked example (1:02) — `slides/07.png`

Next cheapest edge: 2 to 3, weight 2. They're in different components, so add it.

## 8. Worked example (1:09) — `slides/08.png`

Next cheapest edge: 0 to 1, weight 3. They're in different components, so add it.

## 9. Worked example (1:17) — `slides/09.png`

Next cheapest edge: 0 to 2, weight 5. They're already connected, so it would form a cycle; skip it.

## 10. Worked example (1:25) — `slides/10.png`

Next cheapest edge: 3 to 4, weight 6. They're in different components, so add it.

## 11. Worked example (1:32) — `slides/11.png`

Next cheapest edge: 2 to 4, weight 7. They're already connected, so it would form a cycle; skip it.

## 12. Java solution (1/2) (1:40) — `slides/12.png`

We collect each edge once, sort by weight, and for each edge union the two roots if different, recording it in both adjacency lists.

## 13. Java solution (2/2) (1:48) — `slides/13.png`

We collect each edge once, sort by weight, and for each edge union the two roots if different, recording it in both adjacency lists.

## 14. Complexity (1:56) — `slides/14.png`

Time is O of e log e. Space is O of v plus e.

## 15. Edge cases & pitfalls (2:00) — `slides/15.png`

Each undirected edge appears in both lists; add it once. A disconnected graph yields a forest.

## 16. Interview tips & follow-ups (2:08) — `slides/16.png`

The cut property explains why the cheapest crossing edge is safe. Kruskal suits sparse graphs; Prim with a heap suits dense ones.

## 17. Recap (2:17) — `slides/17.png`

To recap Kruskals Algorithm: Add edges from lightest to heaviest, skipping any that would form a cycle, detected with union-find. Try re-implementing it from scratch without looking.
