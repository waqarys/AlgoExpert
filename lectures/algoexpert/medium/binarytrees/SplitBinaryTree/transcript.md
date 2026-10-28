# AlgoExpert · Split Binary Tree

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Split Binary Tree (0:00) — `slides/01.png`

Let's solve Split Binary Tree, a medium binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Can removing one edge split the tree into two parts with equal sums? Return that half-sum, else 0.

## 3. Intuition (0:21) — `slides/03.png`

We need a subtree whose sum is exactly half the total.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Cutting each edge and re-summing both parts is quadratic. Instead compute the total once, then a post-order pass gives every subtree sum; if any non-root subtree equals half the total, we can split.

## 5. Approach (0:37) — `slides/05.png`

Step by step. First, compute the total sum. Second, if odd, it can't split. Third, post-order subtree sums. Fourth, return true if any subtree equals half.

## 6. Worked example (0:52) — `slides/06.png`

The whole tree sums to 12, which is even, so we need some subtree summing to exactly 6.

## 7. Worked example (0:58) — `slides/07.png`

The subtree rooted at 3 sums to 6. Cutting the edge above it splits the tree into two halves of 6 each.

## 8. Java solution (1:06) — `slides/08.png`

We sum the whole tree; if the total is odd we return zero. Then check computes each subtree sum in post-order and sets a flag when a non-root subtree equals half.

## 9. Complexity (1:16) — `slides/09.png`

Time is O of n. Space is O of h.

## 10. Edge cases & pitfalls (1:20) — `slides/10.png`

An odd total can't split. Exclude the root, since cutting nothing isn't a split. With negative values, you can't prune early.

## 11. Interview tips & follow-ups (1:30) — `slides/11.png`

This version returns the half sum, or zero. A popular follow-up maximises the product of the two parts.

## 12. Recap (1:38) — `slides/12.png`

To recap Split Binary Tree: We need a subtree whose sum is exactly half the total. Try re-implementing it from scratch without looking.
