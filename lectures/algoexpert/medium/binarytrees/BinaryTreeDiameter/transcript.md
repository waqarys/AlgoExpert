# AlgoExpert · Binary Tree Diameter

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Binary Tree Diameter (0:00) — `slides/01.png`

Let's solve Binary Tree Diameter, a medium binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Number of edges on the longest path between any two nodes.

## 3. Intuition (0:18) — `slides/03.png`

The longest path through a node joins the heights of its two subtrees.

## 4. Brute force vs optimal (0:23) — `slides/04.png`

Computing heights separately for every node repeats work and is quadratic. A single post-order pass returns each subtree's height and, along the way, checks the path that bends through each node.

## 5. Approach (0:34) — `slides/05.png`

Step by step. First, post-order returns each subtree's height. Second, at each node, left height plus right height is a candidate. Third, track the maximum.

## 6. Worked example (0:47) — `slides/06.png`

At node 8, the left height is 1 and the right height is 0. A path through here has 1 edges. Best so far: 1.

## 7. Worked example (0:56) — `slides/07.png`

At node 7, the left height is 2 and the right height is 0. A path through here has 2 edges. Best so far: 2.

## 8. Worked example (1:05) — `slides/08.png`

At node 5, the left height is 1 and the right height is 0. A path through here has 1 edges. Best so far: 2.

## 9. Worked example (1:15) — `slides/09.png`

At node 3, the left height is 3 and the right height is 3. A path through here has 6 edges. Best so far: 6.

## 10. Worked example (1:24) — `slides/10.png`

At node 1, the left height is 4 and the right height is 1. A path through here has 5 edges. Best so far: 6.

## 11. Java solution (1:34) — `slides/11.png`

Height returns zero for null. It computes left and right heights, updates the best diameter with their sum, and returns one plus the larger height.

## 12. Complexity (1:44) — `slides/12.png`

Time is O of n. Space is O of h.

## 13. Edge cases & pitfalls (1:47) — `slides/13.png`

The diameter counts edges, and it often doesn't pass through the root, as in this example.

## 14. Interview tips & follow-ups (1:53) — `slides/14.png`

Return the height and track the best in a shared variable. The hard follow-up maximises path sum instead of length.

## 15. Recap (2:01) — `slides/15.png`

To recap Binary Tree Diameter: The longest path through a node joins the heights of its two subtrees. Try re-implementing it from scratch without looking.
