# AlgoExpert · Find Nodes Distance K

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Find Nodes Distance K (0:00) — `slides/01.png`

Let's solve Find Nodes Distance K, a hard binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Values of all nodes exactly k edges from the node with value target (unique values). Build parent links, then BFS.

## 3. Intuition (0:22) — `slides/03.png`

Treat the tree as an undirected graph with parent links, then BFS k steps from the target.

## 4. Approach (0:29) — `slides/04.png`

Step by step. First, map each node to its parent. Second, find the target. Third, bFS over left, right and parent. Fourth, collect nodes at distance k.

## 5. Java solution (0:43) — `slides/05.png`

Here's the Java solution, starting with find nodes distance k. It follows the steps we just described.

## 6. Complexity (0:51) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:54) — `slides/07.png`

To recap Find Nodes Distance K: Treat the tree as an undirected graph with parent links, then BFS k steps from the target. Try re-implementing it from scratch without looking.
