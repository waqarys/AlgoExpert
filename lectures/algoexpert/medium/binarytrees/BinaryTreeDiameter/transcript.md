# AlgoExpert · Binary Tree Diameter

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Binary Tree Diameter (0:00) — `slides/01.png`

Let's solve Binary Tree Diameter, a medium binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Number of edges on the longest path between any two nodes.

## 3. Intuition (0:18) — `slides/03.png`

The longest path through a node joins the heights of its two subtrees.

## 4. Approach (0:23) — `slides/04.png`

Step by step. First, post-order returns each subtree's height. Second, at each node, left height plus right height is a candidate. Third, track the maximum.

## 5. Java solution (0:35) — `slides/05.png`

Here's the Java solution, starting with binary tree diameter. It follows the steps we just described.

## 6. Complexity (0:43) — `slides/06.png`

Time is O of n. Space is O of h.

## 7. Recap (0:47) — `slides/07.png`

To recap Binary Tree Diameter: The longest path through a node joins the heights of its two subtrees. Try re-implementing it from scratch without looking.
