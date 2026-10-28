# AlgoExpert · Depth First Search

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Depth First Search (0:00) — `slides/01.png`

Let's solve Depth First Search, an easy graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Given a tree-like graph of named nodes, return names in DFS (pre-order) order.

## 3. Intuition (0:19) — `slides/03.png`

Depth-first search visits a node, then fully explores each child before moving to the next sibling.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Depth-first search is already linear in vertices plus edges. What matters is the order: we go as deep as possible before backtracking, unlike breadth-first search, which goes level by level.

## 5. Approach (0:36) — `slides/05.png`

Step by step. First, append the node's name. Second, recurse into each child in order. Third, return the collected list.

## 6. Worked example (0:48) — `slides/06.png`

We visit A and append it. Then we dive into its first child before touching its siblings.

## 7. Worked example (0:54) — `slides/07.png`

We visit E and append it. Then we dive into its first child before touching its siblings.

## 8. Worked example (1:01) — `slides/08.png`

We visit I and append it. Then we dive into its first child before touching its siblings.

## 9. Worked example (1:08) — `slides/09.png`

We visit C and append it. Then we dive into its first child before touching its siblings.

## 10. Worked example (1:15) — `slides/10.png`

We visit G and append it. Then we dive into its first child before touching its siblings.

## 11. Worked example (1:22) — `slides/11.png`

We visit H and append it. Then we dive into its first child before touching its siblings.

## 12. Java solution (1:29) — `slides/12.png`

The method appends this node's name, then calls depth-first search on each child in order, passing the same list, and returns it.

## 13. Complexity (1:36) — `slides/13.png`

Time is O of v plus e. Space is O of v.

## 14. Edge cases & pitfalls (1:40) — `slides/14.png`

Children must be visited left to right. If you use an explicit stack, push children in reverse. On general graphs, add a visited set to avoid cycles.

## 15. Interview tips & follow-ups (1:51) — `slides/15.png`

Know both the recursive and iterative versions; DFS underpins cycle detection and topological sort.

## 16. Recap (1:58) — `slides/16.png`

To recap Depth First Search: Depth-first search visits a node, then fully explores each child before moving to the next sibling. Try re-implementing it from scratch without looking.
