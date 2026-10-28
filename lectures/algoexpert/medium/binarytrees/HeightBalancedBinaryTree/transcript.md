# AlgoExpert · Height Balanced Binary Tree

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Height Balanced Binary Tree (0:00) — `slides/01.png`

Let's solve Height Balanced Binary Tree, a medium binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. For every node, do left or right subtree heights differ by at most 1? Returns -1 from the helper as an "unbalanced" sentinel.

## 3. Intuition (0:23) — `slides/03.png`

Compute heights bottom-up and fail fast if any node's subtrees differ by more than one.

## 4. Brute force vs optimal (0:28) — `slides/04.png`

Calling a separate height function at every node repeats work and is quadratic on skewed trees. A single post-order pass that returns the height, or minus one for unbalanced, checks everything in linear time.

## 5. Approach (0:41) — `slides/05.png`

Step by step. First, post-order returns height and balance. Second, compare child heights. Third, propagate any imbalance up.

## 6. Worked example (0:52) — `slides/06.png`

At node 4, the subtree heights are 0 and 0. That's balanced, with height 1.

## 7. Worked example (0:59) — `slides/07.png`

At node 8, the subtree heights are 0 and 0. That's balanced, with height 1.

## 8. Worked example (1:05) — `slides/08.png`

At node 2, the subtree heights are 1 and 2. That's balanced, with height 3.

## 9. Worked example (1:12) — `slides/09.png`

At node 6, the subtree heights are 0 and 0. That's balanced, with height 1.

## 10. Worked example (1:19) — `slides/10.png`

At node 1, the subtree heights are 3 and 2. That's balanced, with height 4.

## 11. Java solution (1:26) — `slides/11.png`

The helper returns zero for null. It computes both child heights; if either is minus one or they differ by more than one, it returns minus one. Otherwise it returns one plus the larger.

## 12. Complexity (1:38) — `slides/12.png`

Time is O of n. Space is O of h.

## 13. Edge cases & pitfalls (1:42) — `slides/13.png`

An empty tree is balanced, and the condition must hold at every node, not just the root.

## 14. Interview tips & follow-ups (1:48) — `slides/14.png`

In a real codebase, return a small object with height and balanced flag. A follow-up is how AVL trees rebalance with rotations.

## 15. Recap (1:57) — `slides/15.png`

To recap Height Balanced Binary Tree: Compute heights bottom-up and fail fast if any node's subtrees differ by more than one. Try re-implementing it from scratch without looking.
