# AlgoExpert · Reconstruct Bst

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Reconstruct Bst (0:00) — `slides/01.png`

Let's solve Reconstruct Bst, a medium binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Rebuild a BST from its pre-order traversal (duplicates go right) using value bounds.

## 3. Intuition (0:20) — `slides/03.png`

In pre-order, the root comes first and everything smaller goes left, so we build with value bounds.

## 4. Brute force vs optimal (0:27) — `slides/04.png`

Inserting each value from the root is quadratic in the worst case. Scanning for where the right subtree begins is also quadratic. Passing value bounds down and consuming the pre-order list with one shared index builds the tree in linear time.

## 5. Approach (0:42) — `slides/05.png`

Step by step. First, read values in order. Second, each recursion accepts values within a lower and upper bound. Third, root first, then left with an upper bound, then right.

## 6. Worked example (0:56) — `slides/06.png`

The next value, 10, fits within the bounds, so it becomes a node here. Its left subtree accepts values below 10, its right subtree values from 10 up.

## 7. Worked example (1:06) — `slides/07.png`

The next value, 4, fits within the bounds, so it becomes a node here. Its left subtree accepts values below 4, its right subtree values from 4 up.

## 8. Worked example (1:17) — `slides/08.png`

The next value, 1, fits within the bounds, so it becomes a node here. Its left subtree accepts values below 1, its right subtree values from 1 up.

## 9. Worked example (1:27) — `slides/09.png`

The next value, 5, fits within the bounds, so it becomes a node here. Its left subtree accepts values below 5, its right subtree values from 5 up.

## 10. Worked example (1:38) — `slides/10.png`

The next value, 19, fits within the bounds, so it becomes a node here. Its left subtree accepts values below 19, its right subtree values from 19 up.

## 11. Worked example (1:49) — `slides/11.png`

The next value, 18, fits within the bounds, so it becomes a node here. Its left subtree accepts values below 18, its right subtree values from 18 up.

## 12. Java solution (2:01) — `slides/12.png`

We keep a shared index. Build returns null if the list is exhausted or the next value falls outside the current bounds. Otherwise it consumes the value, creates a node, builds the left with upper bound v, then the right with lower bound v.

## 13. Complexity (2:16) — `slides/13.png`

Time is O of n. Space is O of h.

## 14. Edge cases & pitfalls (2:19) — `slides/14.png`

Duplicates belong on the right, so the left bound is inclusive and the right exclusive. Use long bounds for infinity.

## 15. Interview tips & follow-ups (2:28) — `slides/15.png`

Explain that each value is consumed exactly once. Follow-ups rebuild from post-order, or a general binary tree from in-order and pre-order.

## 16. Recap (2:38) — `slides/16.png`

To recap Reconstruct Bst: In pre-order, the root comes first and everything smaller goes left, so we build with value bounds. Try re-implementing it from scratch without looking.
