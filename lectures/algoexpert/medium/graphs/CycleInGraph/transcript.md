# AlgoExpert · Cycle In Graph

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Cycle In Graph (0:00) — `slides/01.png`

Let's solve Cycle In Graph, a medium graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Directed graph as adjacency list; does it contain a cycle? 3-colour DFS.

## 3. Intuition (0:20) — `slides/03.png`

A cycle exists if depth-first search meets a node that's still on the current recursion stack.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

Running a separate search from every node to see if it returns is slow. One depth-first search with three colours finds a cycle in linear time: an edge to a node that's still on the recursion stack is a back edge. Kahn's algorithm is an alternative.

## 5. Approach (0:40) — `slides/05.png`

Step by step. First, colour nodes white, grey, black. Second, grey means on the stack. Third, edge to a grey node is a back edge, a cycle.

## 6. Worked example (0:53) — `slides/06.png`

Enter node 0 and colour it grey, meaning it's on the current path.

## 7. Worked example (0:58) — `slides/07.png`

Enter node 1 and colour it grey, meaning it's on the current path.

## 8. Worked example (1:03) — `slides/08.png`

Enter node 2 and colour it grey, meaning it's on the current path.

## 9. Worked example (1:07) — `slides/09.png`

Node 2 has an edge to 0, which is still grey, on the current path. That's a back edge, so there's a cycle.

## 10. Java solution (1:16) — `slides/10.png`

We colour every node white, then DFS from each unvisited node. DFS marks the node grey, returns true if any neighbour is grey or if recursing into a white neighbour finds a cycle, and marks the node black when finished.

## 11. Complexity (1:29) — `slides/11.png`

Time is O of v plus e. Space is O of v.

## 12. Edge cases & pitfalls (1:33) — `slides/12.png`

Don't confuse visited with on the stack: reaching a finished node isn't a cycle. Self-loops count, and you must start from every unvisited node to cover disconnected parts.

## 13. Interview tips & follow-ups (1:44) — `slides/13.png`

Explain the three colours clearly. For undirected graphs, the rule changes: ignore the edge back to the parent.

## 14. Recap (1:52) — `slides/14.png`

To recap Cycle In Graph: A cycle exists if depth-first search meets a node that's still on the current recursion stack. Try re-implementing it from scratch without looking.
