# AlgoExpert · Height Balanced Binary Tree

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Height Balanced Binary Tree (0:00) — `slides/01.png`

Let's solve Height Balanced Binary Tree, a medium binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. For every node, do left or right subtree heights differ by at most 1? Returns -1 from the helper as an "unbalanced" sentinel.

## 3. Intuition (0:23) — `slides/03.png`

Compute heights bottom-up and fail fast if any node's subtrees differ by more than one.

## 4. Approach (0:28) — `slides/04.png`

Step by step. First, post-order returns height and balance. Second, compare child heights. Third, propagate any imbalance up.

## 5. Java solution (0:40) — `slides/05.png`

Here's the Java solution, starting with height balanced binary tree. It follows the steps we just described.

## 6. Complexity (0:47) — `slides/06.png`

Time is O of n. Space is O of h.

## 7. Recap (0:51) — `slides/07.png`

To recap Height Balanced Binary Tree: Compute heights bottom-up and fail fast if any node's subtrees differ by more than one. Try re-implementing it from scratch without looking.
