# AlgoExpert · Reconstruct Bst

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Reconstruct Bst (0:00) — `slides/01.png`

Let's solve Reconstruct Bst, a medium binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Rebuild a BST from its pre-order traversal (duplicates go right) using value bounds.

## 3. Intuition (0:20) — `slides/03.png`

In pre-order, the root comes first and everything smaller goes left, so we build with value bounds.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, read values in order. Second, each recursion accepts values within a lower and upper bound. Third, root first, then left with an upper bound, then right.

## 5. Java solution (0:41) — `slides/05.png`

Here's the Java solution, starting with reconstruct bst. It follows the steps we just described.

## 6. Complexity (0:48) — `slides/06.png`

Time is O of n. Space is O of h.

## 7. Recap (0:52) — `slides/07.png`

To recap Reconstruct Bst: In pre-order, the root comes first and everything smaller goes left, so we build with value bounds. Try re-implementing it from scratch without looking.
