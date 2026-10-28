# AlgoExpert · Cycle In Graph

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Cycle In Graph (0:00) — `slides/01.png`

Let's solve Cycle In Graph, a medium graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Directed graph as adjacency list; does it contain a cycle? 3-colour DFS.

## 3. Intuition (0:20) — `slides/03.png`

A cycle exists if depth-first search meets a node that's still on the current recursion stack.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, colour nodes white, grey, black. Second, grey means on the stack. Third, edge to a grey node is a back edge, a cycle.

## 5. Java solution (0:38) — `slides/05.png`

Here's the Java solution, starting with cycle in graph. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is O of v plus e. Space is O of v.

## 7. Recap (0:49) — `slides/07.png`

To recap Cycle In Graph: A cycle exists if depth-first search meets a node that's still on the current recursion stack. Try re-implementing it from scratch without looking.
