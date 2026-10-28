# AlgoExpert · Flatten Binary Tree

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Flatten Binary Tree (0:00) — `slides/01.png`

Let's solve Flatten Binary Tree, a very hard binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Rewire the tree in place into a doubly linked list in in-order order (left equals prev, right equals next); return the leftmost node.

## 3. Intuition (0:22) — `slides/03.png`

In-order linking: each subtree returns its leftmost and rightmost nodes so neighbours can be connected.

## 4. Approach (0:28) — `slides/04.png`

Step by step. First, flatten left and right recursively. Second, link left's rightmost to the node. Third, link the node to right's leftmost. Fourth, return the outer ends.

## 5. Java solution (0:43) — `slides/05.png`

Here's the Java solution, starting with flatten binary tree. It follows the steps we just described.

## 6. Complexity (0:51) — `slides/06.png`

Time is O of n. Space is O of h.

## 7. Recap (0:54) — `slides/07.png`

To recap Flatten Binary Tree: In-order linking: each subtree returns its leftmost and rightmost nodes so neighbours can be connected. Try re-implementing it from scratch without looking.
