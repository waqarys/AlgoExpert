# AlgoExpert · Two Edge Connected Graph

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Two Edge Connected Graph (0:00) — `slides/01.png`

Let's solve Two Edge Connected Graph, a very hard graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Undirected adjacency list; is the graph connected and free of bridges (stays connected after removing any single edge)? Empty graph counts as true. Tarjan low-link.

## 3. Intuition (0:25) — `slides/03.png`

A graph has no bridges if every DFS subtree has a back edge reaching above its root.

## 4. Approach (0:31) — `slides/04.png`

Step by step. First, dFS with arrival times. Second, compute the lowest reachable arrival time. Third, a child with low time above the parent is a bridge. Fourth, check connectivity too.

## 5. Java solution (1/2) (0:47) — `slides/05.png`

Here's the Java solution, starting with two edge connected graph. It follows the steps we just described.

## 6. Java solution (2/2) (0:55) — `slides/06.png`

Continuing with has bridge.

## 7. Complexity (0:58) — `slides/07.png`

Time is O of v plus e. Space is O of v.

## 8. Recap (1:02) — `slides/08.png`

To recap Two Edge Connected Graph: A graph has no bridges if every DFS subtree has a back edge reaching above its root. Try re-implementing it from scratch without looking.
