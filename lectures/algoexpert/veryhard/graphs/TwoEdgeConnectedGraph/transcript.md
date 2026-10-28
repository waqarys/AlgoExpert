# AlgoExpert · Two Edge Connected Graph

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Two Edge Connected Graph (0:00) — `slides/01.png`

Let's solve Two Edge Connected Graph, a very hard graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Undirected adjacency list; is the graph connected and free of bridges (stays connected after removing any single edge)? Empty graph counts as true. Tarjan low-link.

## 3. Intuition (0:25) — `slides/03.png`

A graph has no bridges if every DFS subtree has a back edge reaching above its root.

## 4. Brute force vs optimal (0:31) — `slides/04.png`

Removing each edge and re-checking connectivity is E times V plus E. Tarjan's single DFS finds bridges in linear time.

## 5. Approach (0:39) — `slides/05.png`

Step by step. First, dFS with arrival times. Second, compute the lowest reachable arrival time. Third, a child with low time above the parent is a bridge. Fourth, check connectivity too.

## 6. Worked example (0:54) — `slides/06.png`

A graph is two-edge-connected if it's connected and removing any single edge keeps it connected, meaning no bridges.

## 7. Worked example (1:02) — `slides/07.png`

During DFS, track discovery time and low link: the earliest discovery time reachable from v's subtree with one back edge.

## 8. Worked example (1:10) — `slides/08.png`

If a child's low is greater than the parent's discovery time, the edge between them is a bridge. Also fail if DFS didn't reach everything.

## 9. Java solution (1/2) (1:19) — `slides/09.png`

Has bridge assigns disc and low, recurses into unvisited neighbours, returns true if low of the child exceeds disc of v, and updates low from children and back edges. Then we check all vertices were visited.

## 10. Java solution (2/2) (1:31) — `slides/10.png`

Has bridge assigns disc and low, recurses into unvisited neighbours, returns true if low of the child exceeds disc of v, and updates low from children and back edges. Then we check all vertices were visited.

## 11. Complexity (1:44) — `slides/11.png`

Time is O of v plus e. Space is O of v.

## 12. Edge cases & pitfalls (1:48) — `slides/12.png`

Skip the edge back to the parent, and check every vertex was visited.

## 13. Interview tips & follow-ups (1:53) — `slides/13.png`

The same DFS finds articulation points.

## 14. Recap (1:57) — `slides/14.png`

To recap Two Edge Connected Graph: A graph has no bridges if every DFS subtree has a back edge reaching above its root. Try re-implementing it from scratch without looking.
