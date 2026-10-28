# AlgoExpert · Find Nodes Distance K

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Find Nodes Distance K (0:00) — `slides/01.png`

Let's solve Find Nodes Distance K, a hard binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Values of all nodes exactly k edges from the node with value target (unique values). Build parent links, then BFS.

## 3. Intuition (0:22) — `slides/03.png`

Treat the tree as an undirected graph with parent links, then BFS k steps from the target.

## 4. Brute force vs optimal (0:29) — `slides/04.png`

A tree only lets you go down, but distance can go up too. Recording parents turns it into an undirected graph, and BFS k levels from the target gives the answer in linear time.

## 5. Approach (0:40) — `slides/05.png`

Step by step. First, map each node to its parent. Second, find the target. Third, bFS over left, right and parent. Fourth, collect nodes at distance k.

## 6. Worked example (0:54) — `slides/06.png`

We want nodes at distance two from three. First record each node's parent, then BFS from three.

## 7. Worked example (1:02) — `slides/07.png`

At distance 1, moving to children and to the parent, we reach 6, 1.

## 8. Worked example (1:07) — `slides/08.png`

At distance 2, moving to children and to the parent, we reach 7, 8, 2.

## 9. Java solution (1:13) — `slides/09.png`

We DFS to build the parent map and locate the target, then BFS k levels, enqueuing unseen children and parent, and return the values in the queue.

## 10. Complexity (1:22) — `slides/10.png`

Time is O of n. Space is O of n.

## 11. Edge cases & pitfalls (1:26) — `slides/11.png`

If k is zero, return the target itself. The seen set stops you from walking back along the same edge.

## 12. Interview tips & follow-ups (1:34) — `slides/12.png`

There's also a recursive solution without parent maps.

## 13. Recap (1:38) — `slides/13.png`

To recap Find Nodes Distance K: Treat the tree as an undirected graph with parent links, then BFS k steps from the target. Try re-implementing it from scratch without looking.
