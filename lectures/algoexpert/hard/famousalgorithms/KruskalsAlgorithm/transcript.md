# AlgoExpert · Kruskals Algorithm

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Kruskals Algorithm (0:00) — `slides/01.png`

Let's solve Kruskals Algorithm, a hard famous algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Undirected weighted graph as adjacency list ( dest, weight ); return its minimum spanning tree (forest) in the same format. Sort edges plus union-find.

## 3. Intuition (0:24) — `slides/03.png`

Add edges from lightest to heaviest, skipping any that would form a cycle, detected with union-find.

## 4. Approach (0:31) — `slides/04.png`

Step by step. First, collect and sort edges by weight. Second, union-find over vertices. Third, add edges joining different sets. Fourth, return as adjacency list.

## 5. Java solution (1/2) (0:45) — `slides/05.png`

Here's the Java solution, starting with kruskals algorithm. It follows the steps we just described.

## 6. Java solution (2/2) (0:53) — `slides/06.png`

Continuing with find.

## 7. Complexity (0:56) — `slides/07.png`

Time is O of e log e. Space is O of v plus e.

## 8. Recap (1:00) — `slides/08.png`

To recap Kruskals Algorithm: Add edges from lightest to heaviest, skipping any that would form a cycle, detected with union-find. Try re-implementing it from scratch without looking.
