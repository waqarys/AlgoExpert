# AlgoExpert · Split Binary Tree

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Split Binary Tree (0:00) — `slides/01.png`

Let's solve Split Binary Tree, a medium binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Can removing one edge split the tree into two parts with equal sums? Return that half-sum, else 0.

## 3. Intuition (0:21) — `slides/03.png`

We need a subtree whose sum is exactly half the total.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, compute the total sum. Second, if odd, it can't split. Third, post-order subtree sums. Fourth, return true if any subtree equals half.

## 5. Java solution (0:40) — `slides/05.png`

Here's the Java solution, starting with split binary tree. It follows the steps we just described.

## 6. Complexity (0:47) — `slides/06.png`

Time is O of n. Space is O of h.

## 7. Recap (0:51) — `slides/07.png`

To recap Split Binary Tree: We need a subtree whose sum is exactly half the total. Try re-implementing it from scratch without looking.
